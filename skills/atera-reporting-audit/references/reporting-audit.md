# Reporting and audit operations

## Scope the evidence

Record account name/mode, Customer/Site and folder scope, report name, report generation, timezone, period/as-of time, status filters, device type/OS, inclusion of offline/retired assets, and saved-view filters. Reopen settings after generation to confirm them.

## Operational evidence

- Recent Processes: inspect per-device status for manual scripts, software, and patch actions represented there; expand rows and capture failure detail.
- Patch/automation feedback: use the dedicated report for scheduled IT Automation results not represented in Recent Processes.
- Software inventory: verify package name/publisher/version, AgentID/DeviceGUID, and inventory check-in time.
- Device/availability/health: distinguish current state from period aggregate and last seen from confirmed outage.
- Alerts: separate active, snoozed, resolved, deleted, recurring, ticket-linked, and independently remediated state.
- Tickets/SLA: capture custom statuses, business hours, paused time, policy generation, deadlines, and activity attribution.
- Billing: reconcile summary to contract, work log, product, expense, and invoice detail.
- Audit Log: identify actor, timestamp/timezone, object, before/after data when shown, and whether action originated from technician or automation.

`Completed` for a script means no returned execution error; it does not prove the intended change. Pair process evidence with target-state evidence.

## Complete lists and exports

Clear saved views and filters, use exact stable IDs, and traverse all pages or virtual rows while tracking boundaries and unique IDs. Verify exported row count, columns, date range, totals, and file name. State clearly when evidence is sampled rather than exhaustive.

## Evidence quality

A screenshot proves a visible moment, not scope completeness. Pair it with parameters, counts, stable IDs, drilldown, and as-of time. Do not claim reconciliation when only one side was examined.

Official references: [Recent Processes](https://support.atera.com/hc/en-us/articles/360013411639-Operational-reports-Recent-Processes) and [Software inventory report](https://support.atera.com/hc/en-us/articles/115011963047-Operational-report-Software-inventory).
