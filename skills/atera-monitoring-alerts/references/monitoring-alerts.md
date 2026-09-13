# Monitoring and alert operations

## Effective profile

Resolve the device and inspect direct, folder, Customer/Site, and default threshold assignments. The effective precedence is Agent, Folder, Customer/Site, then global default. Reassignment can silence existing expected signals or create new alerts across many devices; calculate exact descendants and overrides before saving.

## Threshold profile changes

1. Capture profile name, ID when visible, assigned scope, effective-device count, and current items.
2. For each item record metric/event, OS support, severity, threshold/operator, duration, recurrence, and attached auto-healing scripts.
3. Check for overlapping or contradictory monitors and expected transient behavior.
4. Preview affected devices including direct overrides and excluded folders.
5. Save, reopen, and verify the profile and assignment separately.
6. Observe subsequent alert generation before claiming monitoring is effective.

Custom and script-based checks require a clear success/failure contract. Long-running scripts belong in IT Automation rather than fast polling monitors.

## Alert triage

Verify alert ID, device IDs, Customer/Site, severity, source, first/last occurrence, recurrence, linked ticket, and current endpoint evidence. Classify as active issue, duplicate, transient, stale, expected maintenance, false positive, or unresolved.

Snooze requires a reason and exact expiry. Resolve only after the condition is independently fixed or when the user explicitly accepts an administrative resolution. Deleting alert history is destructive and does not remediate the endpoint.

## Automatic tickets and notifications

Before enabling automatic tickets, verify main Contact/User and device association so tickets do not become undefined. Confirm severities, organizations/folders, recipients, ticket routing, duplicate behavior, and expected volume. Organization overrides supersede global alert settings.

## Auto-healing

Treat attachment or enablement as endpoint-code deployment. Inspect each script, up to all configured healing steps, ordering, supported OS, privileges, timeout, repeated-trigger behavior, logging, and rollback. Confirm exact profile and device scope before commit.

## Official references

- [Manage threshold profiles](https://support.atera.com/hc/en-us/articles/217632337-Manage-alert-threshold-profiles)
- [Threshold profile monitoring](https://support.atera.com/hc/en-us/articles/115000294187-Threshold-profiles-monitor-events)
- [Configure alert settings](https://support.atera.com/hc/en-us/articles/360011751059-Configure-alert-settings)
