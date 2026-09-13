---
name: atera-monitoring-alerts
description: Administer Atera monitoring and alerting through an authenticated browser, including threshold profiles, inherited assignment, alert settings, notification recipients, alert investigation, snooze and resolve actions, automatic ticket creation, custom or script-based monitors, and auto-healing. Use for monitoring-focused requests, not general script execution or patching.
---

# Atera Monitoring and Alerts

Determine account mode, then resolve Customer/Site, folder, device, threshold profile, and alert by stable IDs. Inspect effective assignment and current alert history before changing thresholds or resolving alerts.

Read [references/monitoring-alerts.md](references/monitoring-alerts.md) for profile precedence, threshold design, alert workflows, auto-ticketing, auto-healing, noise control, pagination, and verification.

Only one threshold profile is effective per device; direct Agent assignment overrides Folder, which overrides Customer/Site, which overrides the default. Newly installed agents receive the default profile until another effective assignment exists.

Resolving or deleting an alert does not prove the underlying condition is fixed. Auto-healing scripts can execute on endpoints and are critical commits; inspect script content, supported OS, execution context, trigger conditions, recurrence, target scope, and rollback before attaching or enabling them.

Finish with exact profiles and alerts, effective assignment source, threshold changes, notification/ticket effects, auto-healing scope, resolved versus independently remediated state, noise risks, and pending device observations.
