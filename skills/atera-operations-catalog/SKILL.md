---
name: atera-operations-catalog
description: Discover, create, compare, validate, and maintain a private Atera operations catalog containing account mode, Customers or Sites, folders, device baselines, monitoring and automation profiles, maintenance windows, service desk defaults, technician access profiles, approved script fingerprints, integrations, and protected objects. Use to prepare reusable account-specific profiles; never treat the catalog as authorization.
---

# Atera Operations Catalog

Build a private intended-state catalog from administrator input and read-only Atera discovery. The catalog accelerates other Atera skills but never replaces live verification, endpoint evidence, or task authorization.

## Location and privacy

Use a user-provided path or `.atera/operations-catalog.yaml` in the current working directory. Create the parent directory only when the user asks to create a catalog.

Never store passwords, API keys, installer tokens, session cookies, MFA/SSO secrets, recovery codes, remote-access credentials, private keys, scripts containing secrets, complete customer/user/device exports, or unnecessary personal data. Use stable IDs, profile names, masked fingerprints, and aliases.

Read [references/catalog-schema.md](references/catalog-schema.md) before creating or materially changing a catalog. Use [assets/operations-catalog.example.yaml](assets/operations-catalog.example.yaml) as the structural template.

## Discovery workflow

1. Confirm signed-in technician, account name, subscription, account mode, timezone, and live SLA generation.
2. Inventory Customer/Site hierarchy, folders, device categories, threshold profiles, Configuration Policies, IT Automation profiles, software bundles, maintenance windows, technician roles, service-desk defaults, integrations, and protected assets using read-only views.
3. Compute effective assignment and record inheritance/override intent rather than copying one device's accidental state.
4. Distinguish `observed` from administrator-approved `intended` values. Ask for a decision only when the difference changes future operations.
5. Store stable Customer/Site, folder, Agent, DeviceGUID, role, policy, and profile IDs when available, retaining readable names.
6. Add protected organizations, devices, technicians, scripts, remote actions, and workflows that require exact authorization.
7. Save privately and run `scripts/validate_catalog.py` when Python and PyYAML are available.

Preserve administrator-authored comments and unknown forward-compatible keys when practical. Finish with profiles added/changed, unresolved differences, unverified IDs, privacy exclusions, and validation results. Do not mutate Atera during catalog discovery unless separately requested.
