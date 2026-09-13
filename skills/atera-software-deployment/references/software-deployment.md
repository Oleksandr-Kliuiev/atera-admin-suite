# Software deployment operations

## Resolve package and targets

Identify source (`WinGet`, `Chocolatey`, `Homebrew`, private repository, or App Center), exact package/app ID, publisher, architecture, intended version behavior, command options, prerequisites, licensing, restart behavior, and uninstall support. Resolve devices by AgentID/DeviceGUID and inventory rather than hostname alone.

## Bundle workflow

1. Search existing bundles by exact name and OS.
2. Inspect every package, source, version behavior, and disabled item.
3. Create or clone only when needed; use a distinct purpose/versioned name.
4. For manual deployment, verify the versions represented by the bundle.
5. For automation-profile deployment, inspect schedule, latest-version behavior, exclusions, all cumulative tasks, and `run on newly installed agents` overlap.
6. Save and reopen the bundle before any assignment or installation.

## Critical deployment checkpoint

Present Customer/Site/folders, exact target count, OS compatibility, online/offline count, package list, source and version behavior, prerequisites, maintenance window, queue duration, user interruption/reboot, expected disk/network effect, paid licensing, exclusions, and rollback/uninstall path.

## Verification

Track request, queue, Recent Processes, per-device result, and software inventory. A completed process is not sufficient when the desired outcome is a specific version, running service, browser extension, security registration, or application health. Verify the actual target condition after device check-in.

Before retrying, inspect queue, Recent Processes, package inventory, and activity log. Avoid duplicate installers and concurrent package-manager locks.

Official references: [Software bundles](https://support.atera.com/hc/en-us/articles/360016483260-Software-bundles) and [Software management FAQ](https://support.atera.com/hc/en-us/articles/10923739142172-Software-management-FAQ).
