# AI context map

Use this map to load the smallest sufficient context.

| Task | Start here | Load next only when needed |
|---|---|---|
| Natural-language/voice Atera request or explicit suite invocation | `skills/atera-admin-suite/SKILL.md` | One owning specialist; lifecycle owners coordinate related domains |
| Shared Chrome session, authorization, scope, or verification | `skills/atera-organization-lifecycle/references/browser-operation-contract.md` | Read once per working context; reuse the task record |
| Account settings and subscription | `skills/atera-account-admin/SKILL.md` | `references/account-settings.md` |
| Technicians, roles, groups, SSO/MFA | `skills/atera-access-admin/SKILL.md` | `references/access-operations.md` |
| Customer/Site onboarding or offboarding | `skills/atera-organization-lifecycle/SKILL.md` | One lifecycle reference |
| Agent/device onboarding, moves, retirement | `skills/atera-device-lifecycle/SKILL.md` | Device workflow reference |
| Threshold profiles, alerts, auto-healing | `skills/atera-monitoring-alerts/SKILL.md` | Monitoring reference |
| Patch, automation, configuration policy | `skills/atera-patch-policy-admin/SKILL.md` | Patch/policy reference |
| Software bundles and application deployment | `skills/atera-software-deployment/SKILL.md` | Deployment reference |
| Script creation, execution, remediation | `skills/atera-script-remediation/SKILL.md` | Script safety reference |
| Remote session or endpoint controls | `skills/atera-remote-support/SKILL.md` | Remote support reference |
| Tickets, SLA, rules, templates, queues | `skills/atera-service-desk/SKILL.md` | Service desk reference |
| Contracts, time, rates, billing | `skills/atera-psa-billing/SKILL.md` | PSA/billing reference |
| Reports, Recent Processes, and audit evidence | `skills/atera-reporting-audit/SKILL.md` | Relevant sections of `references/reporting-audit.md` |
| Windows family inventory, named or all customers | `skills/atera-reporting-audit/SKILL.md` | `references/inventory-email.md#common-scope`, then `references/windows-inventory.md`; Reports → Monitoring → Microsoft licensing |
| Installed-application inventory, including all matching versions | `skills/atera-reporting-audit/SKILL.md` | `references/inventory-email.md#common-scope`, then `references/software-inventory.md`; Reports → Analytical reports → Presets → Software inventory |
| Other OS inventory with complete device detail | `skills/atera-reporting-audit/SKILL.md` | `references/inventory-email.md#common-scope`, then `references/os-overview.md`; Reports → Analytical reports → Presets → OS Overview |
| Requested report email delivery | `skills/atera-reporting-audit/SKILL.md` | `references/report-delivery.md`; Outlook web in Chrome on Windows/macOS; preserve send conditions and per-user mailbox identity |
| API and integrations | `skills/atera-integrations-api/SKILL.md` | Integration/API reference |
| Account profile discovery/catalog | `skills/atera-operations-catalog/SKILL.md` | Schema, example, validator |
| Package validation | `scripts/check_package.py` | Run `python3 scripts/check_package.py`; review relevant `tests/` scenarios |

Reference paths above are relative to the selected skill. Do not load the complete `skills/` tree for a domain task. Route by frontmatter, read the selected entrypoint and shared Chrome contract once, then load only required reference sections. Add another specialist only when its critical action or detailed procedure is needed. Report delivery preserves exact user authorization and requires an observed outcome.

Every new inventory request resets residual customer, software, version, and OS filters. Unnamed “anyone” / “nokon” scope covers all customers. Verify complete scope before claiming zero, deduplicate application devices across versions, and keep evidence gathering read-only. Conditional delivery sends once only when qualifying matches exist.
