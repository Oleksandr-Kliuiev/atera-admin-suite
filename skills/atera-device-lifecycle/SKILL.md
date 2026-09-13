---
name: atera-device-lifecycle
description: Execute Atera managed-device and agent lifecycle through an authenticated browser, including agent installation preparation, first check-in, device identity, Customer or Site and folder relations, user association, profile assignment, moves, retirement, dependency reassignment, uninstall, and deletion. Use for endpoint lifecycle requests.
---

# Atera Device Lifecycle

Resolve the account mode, Customer/Site, folder, and exact endpoint by AgentID or DeviceGUID plus hostname, serial number, OS, and last seen. Hostname alone is not unique. Inspect active, offline, retired, and duplicate-looking agents before creating or deleting.

Read [references/device-lifecycle.md](references/device-lifecycle.md) for onboarding, moves, profile calculation, offline behavior, retirement, deletion, pagination, and verification.

Never expose installer tokens or URLs containing credentials. Installation is not complete until the correct agent checks in and identity is verified. Profile assignment is not endpoint application.

Agent deletion is irreversible and may queue an uninstall command for an offline endpoint. Before deletion, verify monitored SNMP/TCP/HTTP dependencies, queued work, open alerts/tickets, user relation, software and configuration evidence, and retention requirements. Reassign monitored devices first.

Finish with stable device IDs, hierarchy, online/last-seen state, agent version, effective profiles, queued and executed work, independently verified endpoint results, dependencies, retirement/deletion state, and human steps.
