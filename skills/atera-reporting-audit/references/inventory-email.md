# Inventory scope and recipe index

Read the common scope for inventory work; read only the selected recipe. Direct specialist entrypoints link these resources without requiring this index to be scanned again.

## Common scope

Reuse the selected/named Customer (MSP) or Site (IT Department); never silently widen to all organizations. Record its identity, requested folders, criterion, as-of time, and relevant saved filters. For “all devices”, include online/offline/unreachable and retired records unless the user or established profile limits scope; state exclusions. A visible online-only filter is not a complete inventory. Do not alter account-wide retirement settings.

Prefer a native export over scrolling every row. Compare unique devices with the live scoped count, check first/last rows and exported columns, and inspect for truncation. Deduplicate by AgentID/DeviceGUID when exposed; otherwise use the best available stable identity plus Customer/Site and disclose the limitation. Hostname alone is not unique. Software-version rows are not distinct devices. Count discrepancies require reconciliation before describing the list as complete.

## Windows 10 device list

Use [Windows 10 inventory](windows-inventory.md).

## Devices with a specified program installed

Use [installed-program inventory](software-inventory.md).

## Send the requested report once

Use [report delivery](report-delivery.md). Do not load inventory recipes for unrelated reports.
