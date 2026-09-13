---
name: atera-service-desk
description: Administer Atera Service Desk through an authenticated browser, including ticket creation and triage, assignment, technician groups, statuses, priorities, comments and replies, requester or contact handling, queues, forms, email templates, business hours, SLA policies, and ticket automation rules. Use for ticketing workflows, not endpoint remediation itself or contract billing.
---

# Atera Service Desk

Determine MSP versus IT Department mode, then resolve ticket by ticket ID and Customer/Contact or Site/User. Inspect full activity, related alert/device, current assignment, group privacy, status, priority, SLA basis, and requester-visible communication before mutation.

Read [references/service-desk.md](references/service-desk.md) for ticket state, SLA generations, rule ordering, communications, bulk actions, pagination, and verification.

Distinguish internal note from requester-visible reply. Never send a message, survey, or external notification without reviewing recipients and rendered content. Resolve or close only when the issue outcome and closure criteria are met; status changes can trigger automation, email, SLA recalculation, surveys, and child tickets.

Ticket automation rules affect future events and action order matters. Before enabling or changing a rule, model trigger, conditions, action order, scope, first-match/Always-run behavior, recipients, loops, and unintended all-ticket matches. Deleting tickets, groups, rules, templates, or history is destructive.

Finish with ticket IDs, assignment, status/priority/SLA before and after, public/internal communications, automation triggered, related alert/device outcome, breached or paused time, unresolved work, and required human follow-up.
