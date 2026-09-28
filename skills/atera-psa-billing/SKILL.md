---
name: atera-psa-billing
description: "Atera PSA and billing: contracts, rates, work logs, products/expenses, block balances, service items, billing batches, invoices, taxes, and commercial reports."
---

# Atera PSA and Billing

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Read the relevant sections of [PSA and billing operations](references/psa-billing.md). Verify mode/subscription availability and stable Customer, contract, ticket, work-log, and invoice IDs.

Keep draft, approval, invoice generation, delivery, and accounting export states separate. Never infer terms, billability, rates, taxes, dates, or write-offs from ticket status. Paid contract activation, billed-record changes, invoice finalization, customer delivery, and accounting export/posting are critical commercial commits.

Report IDs, period, included/excluded work, hours/products/expenses/tax/total, draft/final/sent/exported state, duplicate checks, exceptions, and accounting/human follow-up.
