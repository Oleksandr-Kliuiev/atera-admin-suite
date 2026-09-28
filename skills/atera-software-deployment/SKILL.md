---
name: atera-software-deployment
description: "Atera software deployment: bundles, WinGet/Chocolatey/Homebrew, private packages, App Center, install/update/uninstall, queues, and verification. Excludes inventory lists."
---

# Atera Software Deployment

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

For lists of devices with installed software, use [reporting](../atera-reporting-audit/SKILL.md). For deployment, read [software operations](references/software-deployment.md) and inspect existing inventory plus queued/recent processes.

Bundles are OS-specific. Manual installs may use captured versions; automation may use current versions. Verify that choice and WinGet App Installer/Visual C++ prerequisites. Unassigned bundle edits are reversible; installation, update, uninstall, new-agent assignment, and paid/security App Center enablement are critical commits. Honor authorized production scope and rollout strategy; do not invent a pilot.

Report package/bundle IDs, source/version, targets by OS/online state, prerequisites, queue/results, independently verified inventory/service outcome, failures, skips, paid effects, and rollback.
