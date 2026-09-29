# Changelog

## Unreleased — 2026-09-29

- Prefer Analytical reports → Presets → Software inventory for a direct device-level application list. Refresh all matching names and versions, report every device, and reconcile installation counts with unique or active devices.
- Keep the classic Operational software report for retired-device filtering and Last checked evidence.

## 0.1.2 — 2026-09-28

- Send reports through Outlook on the web in Chrome on Windows/macOS, using each employee’s verified mailbox and runtime attachment paths.

- Route Windows family inventory to Monitoring → Microsoft licensing, applications to Monitoring → Software inventory, and other operating systems to Analytical reports → Presets → OS Overview with complete device drilldown and customer evidence.
- Reset residual customer, software, version, and OS filters for each request; support named-customer and all-customer “nokon” scope, exact OS selectors, and deduplicated devices across application versions.
- Preserve conditional one-time sends, distinguish verified zero from loading, partial, or stale results, disclose unknown freshness, resolve displayed-email/link conflicts, omit unrequested license keys, and keep endpoint evidence gathering read-only.
- Add synthetic English and Norwegian routing and safety scenarios for OS and application inventory and conditional delivery.

## 0.1.1 — 2026-09-28

- Route natural-language and voice requests to one owning specialist using the existing authenticated Chrome session; read the shared contract once and only the needed references.
- Add scoped Windows and software inventory recipes and one-time report delivery within exact user authorization, with observed send verification and duplicate-send protection.
- Align package guidance and routing/safety scenarios while retaining production scope, critical-action checkpoints, and read-only endpoint evidence gathering.
- Extend the existing package check to enforce concise descriptions and reject disabled implicit invocation.
