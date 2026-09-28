---
name: atera-organization-lifecycle
description: "Atera Customer/Site lifecycle: onboarding, contacts/users, folders, service/SLA/contracts, profiles, deployment preparation, transfers, and safe offboarding."
---

# Atera Organization Lifecycle

Use the existing authenticated **Chrome** session and read the [shared browser contract](references/browser-operation-contract.md) once per working context.

Own the complete organization workflow. Verify account mode, stable organization ID, and current state; continue partial work idempotently. MSP uses Customer/Contact; IT Department uses Site/User. Do not translate between them without live verification. Check relevant catalog entries for intended profiles, folders, SLA, and maintenance windows.

Read only the selected workflow:
- [Onboarding](references/onboarding.md): new or partially created Customer/Site.
- [Organization change](references/organization-change.md): rename, people/folders, service settings, profiles, or transfers.
- [Offboarding](references/offboarding.md): decommissioning and dependency cleanup.

Complete lifecycle requests authorize ordinary reversible configuration for the exact organization/profile. They exclude paid add-ons, history deletion, agent uninstall, scripts/patch/software execution, remote sessions, API-key changes, and organization deletion unless explicitly included. Use the relevant specialist checkpoint only for such included actions. Verify descendants, overrides, schedule/timezone, offline queues, reboots, exclusions, and rollback before broad assignment; do not invent a pilot.

Report organization ID/mode, people/folders, SLA/contracts, assignments, deployment readiness, completed/already-correct work, queues, blockers, destructive steps not performed, and human steps.
