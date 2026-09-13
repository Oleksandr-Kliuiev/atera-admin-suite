---
name: atera-reporting-audit
description: Investigate Atera operational reports and audit evidence through an authenticated browser, including device and software inventory, patch and automation feedback, Recent Processes, alerts, availability, health, SLA, ticketing, technician, billing, and Audit Log views. Use for read-only reviews, evidence collection, exports, and discrepancy analysis; do not mutate endpoints while gathering evidence.
---

# Atera Reporting and Audit

Keep the investigation read-only unless the user separately requests remediation. Determine account mode and verify account, Customer/Site scope, folders, devices, report, timezone, date range, online/offline basis, and status filters.

Read [references/reporting-audit.md](references/reporting-audit.md) for report scoping, complete-list handling, process status, drilldown, audit attribution, exports, privacy, and evidence quality.

Prefer stable IDs and report parameters over screenshots alone. Distinguish Atera configuration, assignment, queued work, process result, device inventory, and independently observed endpoint state. Recent Processes does not necessarily cover every scheduled Patch and IT Automation result; use the owning feedback report when required.

Minimize customer, user, device, ticket, and billing data. Export only necessary fields to an approved private location; never place operational exports in the public repository or operations catalog.

Finish with account mode, exact report/view, filters and timezone, as-of time, result counts and totals, stable sampled/drilled IDs, discrepancies, automation versus technician attribution, export location when requested, coverage limitations, and recommended next checks.
