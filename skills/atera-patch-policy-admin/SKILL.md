---
name: atera-patch-policy-admin
description: Administer Atera patching and endpoint policy through an authenticated browser, including IT Automation profiles, patch categories and exclusions, schedules, offline queues, Run now, Windows upgrade and maintenance tasks, Configuration Policies, inheritance, update behavior, restart timing, and compliance review. Use for patch or policy requests, not software bundles or arbitrary scripts.
---

# Atera Patch and Policy Admin

Resolve account mode, Customer/Site, folders, devices, OS and role, IT Automation profiles, Configuration Policies, timezone, and maintenance window. Inspect all inherited and direct assignments before mutation.

Read [references/patch-policy-operations.md](references/patch-policy-operations.md) for cumulative automation, configuration-policy precedence, scheduling, offline queues, patch exclusions, reboot behavior, execution, reporting, and rollback.

IT Automation profiles can accumulate across organization, folder, and device scopes; multiple profiles may overlap. Configuration Policies use supersession: Agent overrides Folder, Folder overrides Customer/Site, and domain GPO can still take precedence. Deleting a policy can stop enforcement without reverting device settings.

Saving a draft profile is reversible. Assigning, scheduling, or using Run now can patch, upgrade, clean disks, run maintenance, reboot, or shut down endpoints and is a critical commit. Verify exact production scope; do not invent a pilot, but honor an approved rollout strategy when present.

Finish with exact profiles/policies, assignment and effective source, target count by OS/online state, schedules and timezone, queue expiry, exclusions, reboot behavior, execution status, independently verified compliance, failures, and rollback state.
