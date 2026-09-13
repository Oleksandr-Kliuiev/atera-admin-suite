---
name: atera-software-deployment
description: Deploy and manage endpoint software through Atera's authenticated browser, including OS-specific software bundles, WinGet, Chocolatey, Homebrew, private repositories, App Center applications, manual or automated installation, updates, uninstall, offline queues, and deployment verification. Use for software-focused requests, not OS patching or arbitrary scripts.
---

# Atera Software Deployment

Resolve account mode, Customer/Site, folder, exact devices, OS/architecture, online state, package source, package identity, version intent, prerequisites, and existing installation. Search software inventory and queued/recent processes before deploying.

Read [references/software-deployment.md](references/software-deployment.md) for bundles, package sources, prerequisites, version semantics, scope, offline queues, critical commits, and verification.

Software bundles are OS-specific. Manual bundle installation can use versions captured when software was added, while an automation profile can install current available versions; verify the intended behavior. WinGet may require App Installer and Visual C++ prerequisites.

Creating or editing an unassigned bundle is reversible. Installing, updating, uninstalling, assigning to new agents, or enabling paid/security App Center software is a critical commit. Validate exact production scope; do not impose a pilot unless requested or cataloged.

Finish with package/bundle and source, intended version, target count by OS and online state, prerequisites, assigned/queued/running/result states, independently verified inventory/version/service outcome, failures, skipped devices, paid effect, and rollback.
