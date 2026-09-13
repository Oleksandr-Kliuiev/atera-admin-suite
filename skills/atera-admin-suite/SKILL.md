---
name: atera-admin-suite
description: Unified entrypoint for the Atera Admin Suite. Use only when the user explicitly names atera-admin-suite, with or without the $ prefix, to route and execute Atera administration across MSP or IT Department accounts, access, organizations, devices, monitoring, patching, software, scripts, remote support, service desk, PSA, reporting, or API work.
---

# Atera Admin Suite

Own the user's explicit `$atera-admin-suite` request. Select the smallest applicable suite skill, read it completely, and execute the work with the available browser tools. Do not stop after naming the route.

## Route the request

- Global account identity, timezone, subscription, defaults, or platform settings: read [atera-account-admin](../atera-account-admin/SKILL.md).
- Technicians, groups, roles, permissions, SSO, MFA, or technician deactivation: read [atera-access-admin](../atera-access-admin/SKILL.md).
- Customer/Site creation, contacts/users, folders, organization onboarding, transfer, or decommissioning: read [atera-organization-lifecycle](../atera-organization-lifecycle/SKILL.md).
- Agent installation, device onboarding, relations, moves, retirement, or deletion: read [atera-device-lifecycle](../atera-device-lifecycle/SKILL.md).
- Threshold profiles, alerts, notification routing, automatic tickets, or auto-healing: read [atera-monitoring-alerts](../atera-monitoring-alerts/SKILL.md).
- Patches, IT Automation profiles, Configuration Policies, schedules, exclusions, or reboot policy: read [atera-patch-policy-admin](../atera-patch-policy-admin/SKILL.md).
- Software bundles, package managers, App Center application deployment, updates, or uninstall: read [atera-software-deployment](../atera-software-deployment/SKILL.md).
- Script library, script review, execution, scheduling, or remediation: read [atera-script-remediation](../atera-script-remediation/SKILL.md).
- Remote access, terminal, processes, services, Event Viewer, registry, or interactive endpoint support: read [atera-remote-support](../atera-remote-support/SKILL.md).
- Tickets, queues, SLA, forms, email templates, automation rules, assignment, or ticket lifecycle: read [atera-service-desk](../atera-service-desk/SKILL.md).
- Contracts, work logs, products, expenses, rates, billing, or customer invoices: read [atera-psa-billing](../atera-psa-billing/SKILL.md).
- Read-only operational reports, inventories, Recent Processes, Audit Log, or evidence collection: read [atera-reporting-audit](../atera-reporting-audit/SKILL.md).
- API key administration, API inventory, integrations, imports, exports, or webhooks: read [atera-integrations-api](../atera-integrations-api/SKILL.md).
- Account-mode discovery, reusable profile creation, comparison, or validation: read [atera-operations-catalog](../atera-operations-catalog/SKILL.md).

Choose one owner whenever possible. Organization and device lifecycle skills own their cross-domain workflows; do not load every related specialist by default.

## Establish operational context

Treat the account and endpoints as production unless explicitly identified as a lab. Determine `msp` versus `it_department`, then verify account, Customer/Site, folder, exact object, and current state. Use `.atera/operations-catalog.yaml` when present, but treat it as intended state—not authorization or proof of live assignment.

For endpoint work, distinguish `prepared`, `assigned`, `queued`, `delivered`, `running`, `Atera-reported result`, and `independently verified`. Before retrying an uncertain mutation, read current configuration, queue, Recent Processes, and endpoint state.

## Critical commits

Immediately before a critical commit, present exact account mode, Customer/Site, target count and identifiers, online/offline count, action, schedule/timezone, queue expiry, maintenance window, reboot/user-impact behavior, rollback, and exclusions. Obtain explicit confirmation unless that exact commit was separately confirmed in the current interaction.

Critical commits include broad profile assignment, scripts, patch or software deployment, auto-healing, remote sessions, reboot/shutdown, destructive device controls, agent/organization deletion, API-key reset, privileged technician changes, and billing finalization. MFA, SSO reauthentication, remote-user consent, and physical endpoint steps remain human actions.

## Completion

Report route, account mode, exact organizations/devices/objects, before/after Atera state, effective inherited profiles, queued work and expiry, device-reported results, independently verified outcomes, failures, skipped targets, and human actions. Never call an assigned or queued change applied.
