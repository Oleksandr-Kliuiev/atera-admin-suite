# Patch and policy operations

## Inventory the effective state

For every target capture AgentID/DeviceGUID, OS/version, device role, online/last-seen state, Customer/Site/folder, direct assignments, inherited Configuration Policy, all IT Automation profiles, patch status, pending reboot, and conflicting GPO or local-update behavior where observable.

## IT Automation profiles

Inspect tasks, patch categories, application updates, approvals/postponements/exclusions, Windows upgrade, maintenance, scripts, software bundle, restore point, reboot/shutdown, schedules, account versus device-local timezone, and offline queue duration.

Automation profiles are cumulative. A direct assignment does not replace higher-level profiles. Before assigning or scheduling, compare all profiles affecting each target and detect overlapping patches, scripts, software, cleanup, reboot, or `run on newly installed agents` actions.

## Configuration Policies

Only one policy can be assigned at each Customer/Site, folder, or Agent level. Effective precedence is Agent over Folder over Customer/Site. Domain GPO is outside Atera and may win. Policy enforcement can be periodic, and restart behavior depends on interaction with IT Automation.

Before deleting or unassigning, determine whether device settings must first be reverted. Deletion alone may leave prior settings in place without continued enforcement.

## Critical execution checkpoint

Immediately before assignment, schedule enablement, or Run now, summarize exact targets and overrides, online/offline count, patch categories and exclusions, task order, maintenance window, timezone basis, queue expiry, bandwidth/storage prerequisites, pending reboot, user notifications, reboot/shutdown behavior, and rollback.

## Verify outcome

Track assignment, scheduled/queued state, execution feedback, failures, and post-run patch inventory. Atera and local Windows Update views can differ. Do not claim compliance until the device checks in and intended patch/version/reboot state is observed. Avoid retries until current queue and feedback are checked.

## Official references

- [Patch management](https://support.atera.com/hc/en-us/articles/115015878807-Atera-s-patch-management)
- [Schedule automation profiles](https://support.atera.com/hc/en-us/articles/360018810679-Schedule-an-automation-profile)
- [Configuration Policies overview](https://support.atera.com/hc/en-us/articles/5499183257884-Configuration-policies-overview)
