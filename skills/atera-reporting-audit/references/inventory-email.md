# Inventory scope and recipe index

Read the common scope for inventory work; read only the selected recipe. Direct specialist entrypoints link these resources without requiring this index to be scanned again.

## Common scope

Resolve scope from the current request: a named Customer (MSP)/Site (IT Department) means that exact organization; “this customer” can use the verified selected organization. “Anyone / nokon / noen” with no customer restriction means **all customers/sites accessible in this account**. Explicit global wording overrides the preceding customer's scope; do not ask which customer or silently retain it. If a genuinely ambiguous reference remains, prepare the report while resolving it.

Record scope, requested folders, OS/application and optional version/publisher. On each new request, replace conflicting saved filters: customer/site, agents, software name/version, OS/Office, and result-table searches. In operational reports verify closed controls before Generate: global scope must show All/Select All, not an empty search box. OS Overview instead requires checking its active criteria and complete customer detail; it may have no customer picker. Do not widen named-customer scope. Keep all device types unless narrowed; “PCs” means desktop/workstations, while “anyone” includes servers/Macs supported by that report. For “still has” or “still uses,” prefer **Exclude retired devices** when available and disclose the exclusion; never silently treat a view with unknown retirement status as current inventory. Include offline devices but disclose stale scan data. “Still running” is an inventory question, not permission for endpoint commands. Missing scan freshness or inaccessible/unreported platforms limit the conclusion; neither means zero.

Prefer a native export over scrolling every row. Compare unique devices with the live scoped count, check first/last rows and exported columns, and inspect for truncation. Deduplicate by AgentID/DeviceGUID when exposed; otherwise use the best available stable identity plus Customer/Site and disclose the limitation. Hostname alone is not unique. Software-version rows are not distinct devices. Count discrepancies require reconciliation before describing the list as complete.

## Windows family device list

Use [Windows inventory](windows-inventory.md). For other operating systems use [OS overview](os-overview.md).

## Devices with a specified program installed

Use [installed-program inventory](software-inventory.md).

## Send the requested report once

Use [report delivery](report-delivery.md). Do not load inventory recipes for unrelated reports.
