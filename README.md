# Atera Admin Suite

This Codex plugin provides focused skills for supervised Atera administration through an existing authenticated Chrome session. Natural-language and voice requests route to the relevant specialist without requiring a skill name. It supports both MSP and IT Department account modes and is designed for production work: exact hierarchy resolution, complete-list handling, profile inheritance, offline queues, idempotent changes, and independently verified endpoint outcomes.

## Included skills

- `atera-admin-suite`: natural-language and voice entrypoint and dispatcher.
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
- `atera-reporting-audit`: reports, inventory, process history, audit evidence, and authorized report delivery; endpoint evidence gathering stays read-only.
- `atera-integrations-api`: API and integration administration.
- `atera-operations-catalog`: private reusable account profiles.

Give the task in ordinary language or voice, for example:

```text
Onboard a new managed workstation in Atera.
List Windows 10 devices for the selected customer in Atera.
```

You can also name `$atera-admin-suite` explicitly. The suite selects one owning specialist; that specialist reads the shared Chrome contract once per working context and only the needed reference sections. Lifecycle owners coordinate related work and add a specialist only when its detailed procedure or critical action is needed.

## Operations catalog

Copy `skills/atera-operations-catalog/assets/operations-catalog.example.yaml` to `.atera/operations-catalog.yaml` in the administrator's working directory, then adapt it to the live account. Keep the real catalog private. It stores intended hierarchy, profile names, maintenance windows, and protected objects—never credentials, API keys, installer tokens, or remote-access secrets.

Without a catalog, the selected skill discovers current state in the authenticated browser and asks only for decisions that materially change the result.

## Operating model

The administrator signs in to Atera in Chrome and gives Codex the task. Skills reuse that tab and profile, execute routine authorized work, and verify persisted state. They distinguish configuration saved in Atera from assignment, offline queueing, device execution, Atera-reported completion, and the actual endpoint outcome. Critical or disruptive changes retain their specialist checkpoint and ask only for missing exact authorization; MFA, SSO reauthentication, and required remote-user consent remain human steps.

A request to email a report authorizes one send to resolved recipients within the requested scope. Skills verify the account, recipient, report, dates, format, and attachment, use a native one-time send when the current report supports it, or export through an existing authorized Chrome webmail session when supported. They report the observed generated, exported, or sent state; submission accepted is distinct from recipient delivery. An uncertain send is not retried without evidence that no submission occurred. Extra recipients, recurring schedules, paid features, and endpoint changes require their own authorization.

## Validation

Run `python3 scripts/check_package.py` to check package structure, local references, descriptions of at most 220 characters, implicit invocation not being disabled, and the 700-line context ceiling. Files in `tests/` are review scenarios for routing, hierarchy, authorization, and queued outcomes; they do not execute browser operations.
