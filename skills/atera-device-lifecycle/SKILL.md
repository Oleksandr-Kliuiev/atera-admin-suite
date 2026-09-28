---
name: atera-device-lifecycle
description: "Atera device and agent lifecycle: installation, check-in, identity, profiles, Customer/Site moves, retirement, monitored dependencies, uninstall, and deletion."
---

# Atera Device Lifecycle

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Read the relevant sections of [device lifecycle](references/device-lifecycle.md). Resolve AgentID/DeviceGUID with hostname, serial, OS, hierarchy, and last seen; hostname alone is not unique. Check duplicate-looking active, offline, and retired agents.

Protect installer tokens/credential-bearing URLs. Installation requires the correct agent's verified check-in; assignment does not prove application. Deletion is irreversible and may queue uninstall for offline agents. Before deletion retain required software/configuration evidence, inspect queued work, tickets/alerts and user relations, and reassign dependent SNMP/TCP/HTTP monitors.

Report stable IDs, hierarchy, last seen/version, effective profiles, queued/executed/verified results, dependencies, retirement/deletion/uninstall state, and human steps.
