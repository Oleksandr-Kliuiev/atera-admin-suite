---
name: atera-account-admin
description: Administer global Atera account configuration through an authenticated browser, including account identity, timezone, language, subscription and add-ons, agent defaults, retired-device settings, support and alert defaults, and platform-wide preferences. Use for account-level settings, not endpoint execution or technician-role administration.
---

# Atera Account Admin

Verify the signed-in account, subscription, and whether the UI is in MSP or IT Department mode. Inspect dependencies and downstream scope before changing a global setting.

Read [references/account-settings.md](references/account-settings.md) for navigation, scheduling dependencies, paid features, global defaults, and verification.

Use `.atera/operations-catalog.yaml` when available for intended account mode, timezone, and defaults. Verify them live. Do not silently activate paid add-ons, change subscription quantities, alter timezone used by automation schedules, enable agent uninstall prevention, modify retired-device behavior, or apply a default to all existing organizations.

For global or paid changes, summarize before/after value, affected organizations and devices, billing or scheduling consequence, effective time, and rollback immediately before saving. Reopen the setting and independently verify persistence.

Finish with account mode, exact setting, old/new value, scope, paid effect, schedule impact, propagation, and required human action.
