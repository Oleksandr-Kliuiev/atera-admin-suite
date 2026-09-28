# PSA and billing operations

## Contract setup

Verify Customer, contract name/type, active dates, SLA, currency, taxability, included services/hours/money, rates, minimums, rounding, overage behavior, billing cadence, and related tickets/projects. Search active/inactive contracts before creating.

Do not derive legal or commercial terms from another customer. Changes to an active contract may affect future and current-period calculations; inspect effective-date behavior.

## Work logs, products, and expenses

Resolve ticket and technician, work date/timezone, duration, billable flag, contract, rate, description visibility, product quantity/price, expense evidence, and prior billing state. Prevent duplicate entries by ticket, technician, date, duration/reference, and existing invoice linkage.

Do not edit billed records silently. Use supported adjustment/credit workflows and preserve audit history.

## Billing preparation

1. Select exact Customer/contract and billing period.
2. Reconcile uninvoiced work, products, expenses, blocks, retainers, taxes, discounts, and exclusions.
3. Inspect outliers: zero/negative rates, excessive duration, missing contract, duplicate work, closed tickets, and records outside the period.
4. Compare detail totals to billing summary.
5. Save a draft and reopen it.

Before final generation, sending, or export, present contract, period, item counts, hours, subtotal, tax, total, currency, exclusions, recipients, and destination system. Verify invoice ID/number, final status, delivery/export result, and remaining uninvoiced balance afterward.

## Complete-list handling

Inspect Customer, contract, technician, status, and date filters; preserve the requested scope and remove only conflicting restrictions. Traverse all pages and nested details; track stable ticket, work-log, contract, and invoice IDs. A summary total without included-record evidence is insufficient.

Official reference: [Create a customer, contract, and contact](https://support.atera.com/hc/en-us/articles/217106008-Create-a-customer-contract-and-contact).
