#!/usr/bin/env python3
"""Validate structural and privacy invariants of an Atera operations catalog."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:  # pragma: no cover - dependency error is user-facing
    yaml = None


FORBIDDEN_KEY = re.compile(
    r"(^|_)(password|passwd|secret|token|api_key|installer_token|access_token|"
    r"refresh_token|private_key|session_cookie|remote_credential|mfa_secret|"
    r"sso_secret|recovery_code)s?($|_)",
    re.IGNORECASE,
)
SLUG = re.compile(r"[a-z0-9][a-z0-9-]*")
SHA256 = re.compile(r"[0-9a-fA-F]{64}")
MODES = {"msp": "customer", "it_department": "site"}


def load_catalog(path: Path) -> Any:
    if yaml is None:
        raise RuntimeError(
            "PyYAML is required. Install scripts/requirements.txt in an isolated environment."
        )
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def walk_for_forbidden_keys(value: Any, location: str, errors: list[str]) -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            child_location = f"{location}.{key}" if location else str(key)
            if FORBIDDEN_KEY.search(str(key)):
                errors.append(f"secret-bearing key is forbidden: {child_location}")
            walk_for_forbidden_keys(child, child_location, errors)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            walk_for_forbidden_keys(child, f"{location}[{index}]", errors)


def validate_profile_inheritance(profiles: Any, errors: list[str]) -> set[str]:
    if profiles is None:
        return set()
    if not isinstance(profiles, dict):
        errors.append("device_profiles must be a mapping")
        return set()

    names = set(profiles)
    visiting: set[str] = set()
    visited: set[str] = set()

    for name, profile in profiles.items():
        path = f"device_profiles.{name}"
        if not isinstance(name, str) or not SLUG.fullmatch(name):
            errors.append(f"invalid device profile slug: {name!r}")
        if not isinstance(profile, dict):
            errors.append(f"{path} must be a mapping")
            continue
        parents = profile.get("extends", [])
        if isinstance(parents, str):
            parents = [parents]
        if not isinstance(parents, list) or not all(isinstance(x, str) for x in parents):
            errors.append(f"{path}.extends must be a list of profile names")
            continue
        for parent in parents:
            if parent not in names:
                errors.append(f"{path}.extends references unknown profile {parent!r}")

    def visit(name: str, trail: list[str]) -> None:
        if name in visiting:
            errors.append("profile inheritance cycle: " + " -> ".join(trail + [name]))
            return
        if name in visited:
            return
        visiting.add(name)
        profile = profiles.get(name, {})
        parents = profile.get("extends", []) if isinstance(profile, dict) else []
        if isinstance(parents, str):
            parents = [parents]
        if isinstance(parents, list):
            for parent in parents:
                if isinstance(parent, str) and parent in profiles:
                    visit(parent, trail + [name])
        visiting.remove(name)
        visited.add(name)

    for name in profiles:
        if isinstance(name, str):
            visit(name, [])
    return {name for name in names if isinstance(name, str)}


def validate_scripts(scripts: Any, errors: list[str]) -> None:
    if scripts is None:
        return
    if not isinstance(scripts, dict):
        errors.append("approved_scripts must be a mapping")
        return
    for name, script in scripts.items():
        path = f"approved_scripts.{name}"
        if not isinstance(name, str) or not SLUG.fullmatch(name):
            errors.append(f"invalid approved script slug: {name!r}")
        if not isinstance(script, dict):
            errors.append(f"{path} must be a mapping")
            continue
        digest = script.get("sha256")
        if not isinstance(digest, str) or not SHA256.fullmatch(digest):
            errors.append(f"{path}.sha256 must contain 64 hexadecimal characters")


def validate_organizations(
    organizations: Any,
    mode: str | None,
    profile_names: set[str],
    errors: list[str],
) -> None:
    if not isinstance(organizations, dict) or not organizations:
        errors.append("organizations must be a non-empty mapping")
        return

    expected_type = MODES.get(mode or "")
    seen_ids: dict[str, str] = {}
    for slug, organization in organizations.items():
        path = f"organizations.{slug}"
        if not isinstance(slug, str) or not SLUG.fullmatch(slug):
            errors.append(f"invalid organization slug: {slug!r}")
        if not isinstance(organization, dict):
            errors.append(f"{path} must be a mapping")
            continue
        organization_type = organization.get("type")
        if expected_type and organization_type != expected_type:
            errors.append(
                f"{path}.type must be {expected_type!r} for account.mode {mode!r}"
            )
        organization_id = organization.get("id")
        if not isinstance(organization_id, (int, str)) or str(organization_id).strip() == "":
            errors.append(f"{path}.id is required")
        elif str(organization_id) in seen_ids:
            errors.append(
                f"duplicate organization id {organization_id!r} in {path} and "
                f"organizations.{seen_ids[str(organization_id)]}"
            )
        else:
            seen_ids[str(organization_id)] = str(slug)
        if not organization.get("display_name"):
            errors.append(f"{path}.display_name is required")

        default_profile = organization.get("default_device_profile")
        if default_profile and default_profile not in profile_names:
            errors.append(f"{path}.default_device_profile references unknown profile")

        folders = organization.get("folders", {})
        if not isinstance(folders, dict):
            errors.append(f"{path}.folders must be a mapping")
            continue
        for folder_slug, folder in folders.items():
            folder_path = f"{path}.folders.{folder_slug}"
            if not isinstance(folder_slug, str) or not SLUG.fullmatch(folder_slug):
                errors.append(f"invalid folder slug: {folder_slug!r}")
            if not isinstance(folder, dict) or "id" not in folder:
                errors.append(f"{folder_path} must be a mapping with id")
                continue
            profile = folder.get("device_profile")
            if profile and profile not in profile_names:
                errors.append(f"{folder_path}.device_profile references unknown profile")


def validate_catalog(data: Any) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(data, dict):
        return ["catalog root must be a mapping"], warnings
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")

    account = data.get("account")
    mode: str | None = None
    if not isinstance(account, dict):
        errors.append("account must be a mapping")
    else:
        if not account.get("name"):
            errors.append("account.name is required")
        mode = account.get("mode")
        if mode not in MODES:
            errors.append("account.mode must be 'msp' or 'it_department'")
        timezone = account.get("timezone")
        if not isinstance(timezone, str) or "/" not in timezone:
            errors.append("account.timezone must be an IANA-style timezone")
        if not account.get("verified_at"):
            warnings.append("account.verified_at is missing")

    profile_names = validate_profile_inheritance(data.get("device_profiles"), errors)
    validate_scripts(data.get("approved_scripts"), errors)
    validate_organizations(data.get("organizations"), mode, profile_names, errors)
    walk_for_forbidden_keys(data, "", errors)
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("catalog", type=Path)
    args = parser.parse_args()
    try:
        data = load_catalog(args.catalog)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors, warnings = validate_catalog(data)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        print(f"Catalog invalid: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"Catalog valid: {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
