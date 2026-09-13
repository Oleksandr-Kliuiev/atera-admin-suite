# Operations catalog schema

The catalog is YAML with `schema_version: 1`. Keep values human-reviewable and references stable. The public example is synthetic; real catalogs remain private.

## Top-level keys

- `schema_version`: required integer, currently `1`.
- `account`: required map with `name`, `mode`, `timezone`, optional `subscription`, `sla_model`, and `verified_at`.
- `maintenance_windows`: optional reusable schedules keyed by slug.
- `device_profiles`: optional intended endpoint baselines keyed by slug.
- `access_profiles`: optional technician access profiles keyed by slug.
- `approved_scripts`: optional script metadata and SHA-256 fingerprints; never script secrets.
- `organizations`: required non-empty Customer or Site map keyed by slug.
- `integrations`: optional names, owners, data domains, masked key fingerprints, and status.
- `safety`: optional protected technicians, organizations, devices, profiles, scripts, and critical actions.

## Account mode

`account.mode` must be `msp` or `it_department`.

- MSP organizations use `type: customer` and may contain Contacts.
- IT Department organizations use `type: site` and may contain Users.

Live skills must verify account mode and stable organization ID before mutation. `sla_model` may be `legacy`, `policy`, or `detected_live`; the live UI remains authoritative.

## Device profiles

A device profile may contain:

- `description`, optional `extends`, `os`, and `device_role`;
- `threshold_profile`;
- `configuration_policy`;
- `automation_profiles` list;
- `software_bundle`;
- `maintenance_window` reference;
- `offline_queue` and `reboot_policy` intent;
- `verification` conditions.

Inheritance describes intended defaults. It does not reproduce Atera semantics: one effective threshold profile, hierarchical Configuration Policy, and cumulative IT Automation profiles must still be calculated live.

## Organizations and folders

Every organization requires `type`, stable `id`, and `display_name`. It may specify `default_device_profile`, service-desk settings, contacts/users aliases, and folders. Each folder should retain its stable ID and may override the device profile.

## Approved scripts

Store script library name/ID, purpose, supported OS, immutable SHA-256 fingerprint, owner, verification condition, and rollback name. Fingerprints help detect drift; they do not authorize execution.

## Forbidden data

Never include API keys, installer tokens, passwords, session cookies, remote-access credentials, MFA/SSO secrets, private keys, recovery codes, or secret-bearing script parameters. Use `masked_key_fingerprint`, not a credential value.
