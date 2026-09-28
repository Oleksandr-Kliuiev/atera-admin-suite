---
name: atera-service-desk
description: "Atera service desk: tickets, queues, assignment/groups, requester replies and internal notes, statuses, forms/templates, business hours, SLA, and automation rules."
---

# Atera Service Desk

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Read the relevant sections of [service desk operations](references/service-desk.md). Resolve ticket ID and mode-specific requester/organization; inspect activity, related device/alert, privacy, assignment, and SLA basis.

Distinguish internal notes from public replies; review recipients and rendered content before authorized messages, surveys, or notifications. Resolve/close only when outcome and closure criteria are met. Status changes may trigger email, surveys, child tickets, SLA recalculation, and rules. Model rule order, first-match/Always-run semantics, loops, and future scope before enabling. Deleting tickets, groups, rules, templates, or history is destructive.

Report ticket IDs, assignment, status/priority/SLA deltas, communications, triggered automation, endpoint/alert outcome, breached/paused time, and remaining work.
