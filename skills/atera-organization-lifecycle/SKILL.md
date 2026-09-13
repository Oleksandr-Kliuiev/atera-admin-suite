---
name: atera-organization-lifecycle
description: Execute end-to-end Atera Customer lifecycle in MSP accounts or Site lifecycle in IT Department accounts, including contacts or users, folders, service settings, SLA, contracts, monitoring defaults, agent deployment preparation, transfers, and safe decommissioning. Use for organization workflows spanning multiple Atera areas.
---

# Atera Organization Lifecycle

Own the complete organization workflow. Determine account mode first: use Customer and Contact in MSP mode, Site and User in IT Department mode. Never translate one mode's object into the other without verifying the live hierarchy.

## Establish context

1. Attach to the user-mentioned Atera tab when present; otherwise reuse the authenticated Atera session.
2. Verify signed-in technician, account name, mode, exact organization, and stable organization ID.
3. Inspect current state before mutation and continue partial workflows idempotently.
4. Use `.atera/operations-catalog.yaml` when available for intended profiles, folders, SLA, and maintenance windows; verify every referenced object live.
5. Read [references/browser-operation-contract.md](references/browser-operation-contract.md).

## Choose one workflow

- New Customer/Site: read [references/onboarding.md](references/onboarding.md).
- Organization transfer or configuration change: read [references/organization-change.md](references/organization-change.md).
- Customer/Site decommissioning: read [references/offboarding.md](references/offboarding.md).

## Authorization

A request for complete onboarding, change, or safe offboarding authorizes ordinary reversible configuration for the exact organization and stated profile. It does not authorize paid add-ons, destructive ticket or billing history deletion, agent uninstall, broad scripts/patches/software, remote sessions, API-key changes, or deletion of the organization itself unless explicitly included.

Production organizations and scopes are valid when requested; do not invent a pilot. Before broad assignment, verify exact folders/devices, inherited overrides, schedules, timezone, offline queue, reboot behavior, exclusions, and rollback.

## Finish

Report account mode, organization and stable ID, contacts/users, folders, SLA/contracts, monitoring and automation assignments, agent deployment readiness, completed/already-correct work, queued changes, blockers, destructive steps not performed, and human actions.
