---
name: atera-operations-catalog
description: "Atera private operations catalog: discover, create, compare, and validate reusable account, organization, device, access, service, and integration profiles."
---

# Atera Operations Catalog

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Build intended-state profiles from administrator input and read-only discovery. A catalog never grants authorization or proves live assignment. Use the requested path or `.atera/operations-catalog.yaml`; create it only when requested.

Read [catalog schema](references/catalog-schema.md) and use the [synthetic template](assets/operations-catalog.example.yaml) only when creating or materially changing a catalog. For comparison, load only relevant entries. Keep secrets, full customer/user/device exports, and unnecessary personal data out; store stable IDs, readable names, aliases, and masked fingerprints.

Discover relevant account/mode/subscription/timezone/SLA generation, hierarchy, baselines, profiles and inheritance, maintenance windows, access, service defaults, integrations, and protected assets. Compute effective assignment and record inheritance/override intent; do not turn one device's accidental state into an approved profile. Separate `observed` from approved `intended` values; resolve differences only when they change future operations. Preserve authored comments and unknown keys when practical. Run `scripts/validate_catalog.py` when Python/PyYAML are available.

Report profiles changed, unresolved differences, unverified IDs, privacy exclusions, and validation. Discovery does not authorize Atera mutations.
