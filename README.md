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
Check whether any customers have 7-Zip installed; email any matches to admin@example.com.
```

You can also name `$atera-admin-suite` explicitly. The suite selects one owning specialist; that specialist reads the shared Chrome contract once per working context and only the needed reference sections. Lifecycle owners coordinate related work and add a specialist only when its detailed procedure or critical action is needed.

Inventory requests route by what is being counted:

- Windows families use **Reports → Classic Reports / Operational reports → Monitoring → Microsoft licensing**, with the exact available OS selector for the requested family and all matching editions.
- Installed applications use **Reports → Classic Reports / Operational reports → Monitoring → Software inventory**, with all matching versions unless a version is requested. Device lists are deduplicated across matching versions.
- Other operating systems use **Reports → Analytical reports → Presets → OS Overview**, with complete device drilldown and customer evidence. Windows 11 readiness results do not establish complete OS inventory.

Each new request clears residual customer, software, version, and OS filters before applying the requested scope. A named customer limits the report to that customer; a general “anyone” / Norwegian “nokon” request without a customer uses all customers, including after a previous named-customer report. Results are Atera-reported inventory; report generation time does not establish endpoint freshness. A verified complete zero requires a successfully generated result covering the requested scope. Empty, loading, partial, or stale results do not establish zero.

## Operations catalog

Copy `skills/atera-operations-catalog/assets/operations-catalog.example.yaml` to `.atera/operations-catalog.yaml` in the administrator's working directory, then adapt it to the live account. Keep the real catalog private. It stores intended hierarchy, profile names, maintenance windows, and protected objects—never credentials, API keys, installer tokens, or remote-access secrets.

Without a catalog, the selected skill discovers current state in the authenticated browser and asks only for decisions that materially change the result.

## Operating model

The administrator signs in to Atera in Chrome and gives Codex the task. Skills reuse that tab and profile, execute routine authorized work, and verify persisted state. They distinguish configuration saved in Atera from assignment, offline queueing, device execution, Atera-reported completion, and the actual endpoint outcome. Critical or disruptive changes retain their specialist checkpoint and ask only for missing exact authorization; MFA, SSO reauthentication, and required remote-user consent remain human steps.

A request to email a report authorizes one send to resolved recipients within the requested scope. Skills verify the account, recipient, report, dates, format, and attachment, use Outlook on the web in the existing authorized Chrome profile on Windows and macOS. The sending mailbox belongs to the signed-in employee; no author-specific account, recipient, local path or native Outlook dependency is embedded. They report the observed generated, exported, or sent state; submission accepted is distinct from recipient delivery. An uncertain send is not retried without evidence that no submission occurred. Extra recipients, recurring schedules, paid features, and endpoint changes require their own authorization.

“If any” delivery requires qualifying matches; a verified complete zero means no email. A positive result authorizes one send to the resolved address after the scope and content checks. Conflicting displayed and `mailto:` addresses require recipient clarification while the report is prepared. Inventory can be sent as a concise device/OS or device/application list in the email body unless a file was requested; unrequested Windows and Office license keys are excluded. Inventory work never authorizes endpoint changes.

## Validation

Run `python3 scripts/check_package.py` to check package structure, local references, descriptions of at most 220 characters, implicit invocation not being disabled, and the 700-line context ceiling. Files in `tests/` are review scenarios for routing, hierarchy, authorization, and queued outcomes; they do not execute browser operations.
