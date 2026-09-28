---
name: atera-account-admin
description: "Atera account settings: identity, timezone, subscription/add-ons, agent and support defaults, retired devices, and platform-wide preferences."
---

# Atera Account Admin

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Read [account settings](references/account-settings.md). Verify account, mode, subscription, and relevant dependencies; use only relevant catalog entries as intended state.

Do not silently activate paid add-ons, change quantities or scheduling timezone, enable uninstall prevention, change retired-device behavior, or apply defaults to existing organizations. Before global/paid changes, summarize the value delta, affected organizations/devices, billing/scheduling consequences, effective time, and rollback. Reopen to verify persistence and propagation.

Report the exact setting, old/new value, scope, paid and schedule effects, propagation evidence, and human steps.
