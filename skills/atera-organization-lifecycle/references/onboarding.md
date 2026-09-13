# Customer or Site onboarding

## Required facts

Establish account mode, organization legal/display name, stable external reference when available, timezone, primary contact/user, folders, service desk requirements, SLA/business hours, contract requirement, monitoring profile, patch policy, software baseline, and agent deployment approach. Ask only for missing choices that materially change configuration.

## Idempotent workflow

1. Search active and inactive Customers/Sites by exact name, domain, external ID, and available business identifier.
2. Reconcile an existing partial organization instead of creating a duplicate.
3. Create or update the Customer/Site with verified details.
4. Create folders and contacts/users, then verify their organization linkage.
5. Configure main contact/user and support-email behavior.
6. Assign SLA/business hours and contract only when applicable to the account mode and subscription.
7. Assign intended threshold and configuration profiles; calculate inheritance and overrides.
8. Assign IT Automation profiles only after checking overlap, schedule, timezone, offline queue, and reboot behavior.
9. Prepare agent installer/deployment instructions without exposing installer tokens.
10. Refresh and verify organization, folders, people, service settings, assignments, and device readiness.

Creating the organization does not prove any agent is installed or profile applied. Report each state separately.

Official reference: [Create a customer, contract, and contact](https://support.atera.com/hc/en-us/articles/217106008-Create-a-customer-contract-and-contact).
