# Atera Admin Suite

This Codex plugin provides focused skills for supervised Atera administration through an already authenticated browser session. It supports both MSP and IT Department account modes and is designed for production work: exact hierarchy resolution, complete-list handling, profile inheritance, offline queues, idempotent changes, and independently verified endpoint outcomes.

## Included skills

- `atera-admin-suite`: explicit unified entrypoint and dispatcher.
- `atera-account-admin`: global account and subscription settings.
- `atera-access-admin`: technicians, groups, roles, permissions, and authentication.
- `atera-organization-lifecycle`: Customer/Site onboarding, changes, and offboarding.
- `atera-device-lifecycle`: agent and managed-device lifecycle.
- `atera-monitoring-alerts`: thresholds, alerts, auto-ticketing, and auto-healing.
- `atera-patch-policy-admin`: patch automation, schedules, exclusions, and configuration policies.
- `atera-software-deployment`: software bundles, package managers, and App Center deployments.
- `atera-script-remediation`: script library, execution, and outcome verification.
- `atera-remote-support`: supervised remote access and endpoint controls.
- `atera-service-desk`: tickets, queues, SLAs, templates, and automation rules.
- `atera-psa-billing`: contracts, work logs, rates, products, expenses, and billing.
- `atera-reporting-audit`: read-only reports, inventory, process history, and audit evidence.
- `atera-integrations-api`: API and integration administration.
- `atera-operations-catalog`: private reusable account profiles.

Codex can select a focused skill from a natural-language request that clearly mentions Atera. Use the explicit suite entrypoint for stable routing:

```text
$atera-admin-suite onboard a new managed workstation in Atera
```

## Operations catalog

Copy `skills/atera-operations-catalog/assets/operations-catalog.example.yaml` to `.atera/operations-catalog.yaml` in the administrator's working directory, then adapt it to the live account. Keep the real catalog private. It stores intended hierarchy, profile names, maintenance windows, and protected objects—never credentials, API keys, installer tokens, or remote-access secrets.

Without a catalog, the selected skill discovers current state in the authenticated browser and asks only for decisions that materially change the result.

## Operating model

The administrator signs in to Atera and gives Codex the task. Skills execute routine authorized work and verify persisted state. They distinguish configuration saved in Atera from assignment, offline queueing, device execution, Atera-reported completion, and the actual endpoint outcome. Critical or disruptive changes pause at an exact review checkpoint when not already explicitly confirmed; MFA, SSO reauthentication, and remote-user consent remain human steps.
