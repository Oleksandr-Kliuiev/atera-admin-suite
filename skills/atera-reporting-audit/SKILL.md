---
name: atera-reporting-audit
description: "Atera reports and audit: device/OS/software inventory, operational evidence, Recent Processes, Audit Log, export, and authorized email delivery. Read-only endpoints."
---

# Atera Reporting and Audit

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Choose only the needed route; do not load every recipe:
- Device/OS or installed-program inventory: read [inventory scope](references/inventory-email.md#common-scope), then [Windows 10](references/windows-inventory.md) or [installed programs](references/software-inventory.md) when applicable.
- Other reports, Recent Processes, Audit Log, or discrepancies: read the relevant sections of [reporting evidence](references/reporting-audit.md).
- Sending any report: additionally read [delivery](references/report-delivery.md); inventory/audit recipes need not be reread. Prepare while resolving a missing recipient.

Keep endpoint evidence gathering read-only. Inventory uninstall controls, scripts, endpoint refreshes, patches, and new recurring schedules are outside a one-time report request. Minimize exports and keep them private, outside public repositories and operations catalogs.

Report scope, unique device count or evidence IDs, generated/exported/sent state, recipient when sent, and material freshness/completeness limits. Claim only evidenced delivery and coverage.
