# AI context map

Use this map to load the smallest sufficient context.

| Task | Start here | Load next only when needed |
|---|---|---|
| Explicit `$atera-admin-suite` request | `skills/atera-admin-suite/SKILL.md` | Exactly one owning skill; lifecycle may span related domains |
| Account settings and subscription | `skills/atera-account-admin/SKILL.md` | `references/account-settings.md` |
| Technicians, roles, groups, SSO/MFA | `skills/atera-access-admin/SKILL.md` | `references/access-operations.md` |
| Customer/Site onboarding or offboarding | `skills/atera-organization-lifecycle/SKILL.md` | Browser contract and one lifecycle reference |
| Agent/device onboarding, moves, retirement | `skills/atera-device-lifecycle/SKILL.md` | Device workflow reference |
| Threshold profiles, alerts, auto-healing | `skills/atera-monitoring-alerts/SKILL.md` | Monitoring reference |
| Patch, automation, configuration policy | `skills/atera-patch-policy-admin/SKILL.md` | Patch/policy reference |
| Software bundles and application deployment | `skills/atera-software-deployment/SKILL.md` | Deployment reference |
| Script creation, execution, remediation | `skills/atera-script-remediation/SKILL.md` | Script safety reference |
| Remote session or endpoint controls | `skills/atera-remote-support/SKILL.md` | Remote support reference |
| Tickets, SLA, rules, templates, queues | `skills/atera-service-desk/SKILL.md` | Service desk reference |
| Contracts, time, rates, billing | `skills/atera-psa-billing/SKILL.md` | PSA/billing reference |
| Read-only reports and audit evidence | `skills/atera-reporting-audit/SKILL.md` | Reporting reference |
| API and integrations | `skills/atera-integrations-api/SKILL.md` | Integration/API reference |
| Account profile discovery/catalog | `skills/atera-operations-catalog/SKILL.md` | Schema, example, validator |

Do not load the complete `skills/` tree for a domain task. Route by frontmatter, then read only the required reference.
