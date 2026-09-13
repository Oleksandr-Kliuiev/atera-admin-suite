# Service desk operations

## Ticket handling

Resolve ticket ID, mode-specific requester, Customer/Site, device/alert, source, title, description, activity, assignment, group, privacy, status, priority/impact, tags, contract, SLA target, and attachments. Check for duplicates and parent/child relationships before creating or merging.

When writing, choose explicitly between internal note and requester-visible reply. Verify recipients, templates, dynamic fields, attachments, and sensitive content. Reopen the ticket and activity log to verify delivery/action source.

Status semantics may be customized. Treat Open, Pending, Resolved, Closed, and custom statuses according to the live workflow. Do not equate Resolved with confirmed closure. Changing status, priority, group, contract, or Customer/Site can recalculate SLA or trigger rules.

## SLA model

Detect the live SLA generation rather than relying on account age alone. Legacy and newer policy workflows can differ by Site/Customer, contract, technician group, priority or impact, business-hours calendar, and rule ordering. Newer policies can apply the first matching policy and reevaluate when relevant ticket fields change.

Before changing SLA, preview representative tickets and expected deadlines; record business timezone and paused-status behavior.

## Ticket automation rules

1. Capture rule order, enabled state, trigger, conditions, match semantics, time criteria, and actions.
2. Treat empty conditions as potentially global.
3. Assign technician group before technician-dependent actions.
4. Validate recipients and templates before send actions.
5. Check loops involving status changes, requester replies, auto-close, child tickets, alerts, and external forwarding.
6. Enable only after summarizing future scope; verify through a controlled event or activity log when authorized.

Rule changes generally affect future events, not historical tickets. Do not claim retroactive repair.

## Queues and bulk actions

Clear saved-view filters and inspect all pages. Select tickets by stable ID, not row position. Before bulk assignment/status/priority/merge/delete, reconcile count, scope, SLA effects, private-group access, notifications, and automation triggers.

## Official references

- [Tickets overview](https://support.atera.com/hc/en-us/articles/9258656888732-Tickets-overview)
- [Ticket automation rules](https://support.atera.com/hc/en-us/articles/360018434920-Ticket-automation-rules)
- [Manage SLA policies](https://support.atera.com/hc/en-us/articles/215286388-Manage-Service-Level-Agreement-SLA-policies)
