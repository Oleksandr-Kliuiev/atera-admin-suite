---
name: atera-reporting-audit
description: "Atera reports in Chrome: find any OS or installed program for one/all customers; inventory, audit evidence, export and authorized email. Read-only endpoints."
---

# Atera Reporting and Audit

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Choose only the needed route; do not load every recipe:
- “Still running [OS/program]?”, including Norwegian “fortsatt”, “kjører”, “nokon”: read [inventory scope](references/inventory-email.md#common-scope) and **one** recipe below. Start in Reports even without the word “report”; inventory does not mean deployment.
  - “Still has Windows 10 PCs” for a named customer: **Monitoring → Auditor**, with retired devices excluded; [Windows](references/windows-inventory.md). For broader Windows edition/licensing questions use **Monitoring → Microsoft licensing**.
  - macOS, Linux, other OS, or Windows family absent from that selector: **Analytical reports → Presets → OS Overview**; [OS overview](references/os-overview.md).
  - Installed application, optionally version/publisher: **Analytical reports → Presets → Software inventory** for a direct device list; [programs](references/software-inventory.md). OS names belong to OS reports, not Software Name.
- Other reports, Recent Processes, Audit Log, or discrepancies: read the relevant sections of [reporting evidence](references/reporting-audit.md).
- Sending any report: additionally read [Outlook web delivery](references/report-delivery.md), portable across Windows/macOS in Chrome; inventory/audit recipes need not be reread. Prepare while resolving a missing recipient.

Keep endpoint evidence gathering read-only. Inventory uninstall controls, scripts, endpoint refreshes, patches, and new recurring schedules are outside a one-time report request. Minimize exports and keep them private, outside public repositories and operations catalogs.

Report scope, unique device count or evidence IDs, generated/exported/sent state, recipient when sent, and material freshness/completeness limits. Claim only evidenced delivery and coverage.

For a device-list prompt, finish the complete requested list before summarizing. A report title, aggregate count or one example device is not a completed device-list request.
