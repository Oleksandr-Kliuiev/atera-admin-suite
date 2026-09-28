---
name: atera-patch-policy-admin
description: "Atera patching and policies: IT Automation, Configuration Policies, inheritance, exclusions, schedules, offline queues, Run now, reboot behavior, and compliance."
---

# Atera Patch and Policy Admin

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Read the relevant sections of [patch and policy operations](references/patch-policy-operations.md). Inspect all direct and inherited assignments: IT Automation accumulates, while Configuration Policies supersede by hierarchy; GPO may override them. Policy deletion may leave endpoint settings unchanged.

Drafting a profile is reversible; assignment, scheduling, and Run now can patch, upgrade, clean disks, run maintenance, reboot, or shut down endpoints. Use the exact authorized production scope and any approved rollout strategy; do not invent a pilot.

Report profile/policy IDs, effective sources, target counts by OS/online state, schedule/timezone, queue expiry, exclusions, reboot behavior, execution, verified compliance, failures, and rollback.
