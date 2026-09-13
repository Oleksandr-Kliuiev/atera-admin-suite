# Account settings operations

## Context and navigation

Confirm account name, signed-in technician, subscription, mode, locale, and timezone. Current Atera layouts commonly group settings under `Admin`; resolve visible labels semantically because sections vary by account mode and rollout generation.

## Dependency-aware settings

- Timezone: inspect automation profiles, maintenance windows, SLA business hours, and device-local-time schedules before changing.
- Subscription/add-ons: inspect billing cadence, licensed quantity, included functionality, affected customers/sites, and cancellation behavior.
- Agent defaults: inspect uninstall prevention, offline/retired-device rules, and existing deployment methods.
- Alert defaults: inspect recipients, automatic ticket creation, organization overrides, and expected notification volume.
- Ticket/email defaults: inspect support addresses, forwarding, requester/contact mapping, templates, and automation rules.
- Remote-access defaults: inspect provider, consent, concurrent-session behavior, and technician permissions.

Changing a global default does not prove existing organizations inherited it. Determine whether the UI offers future-only or apply-to-existing behavior and report the selected scope.

## Stable interaction

Observe a fresh UI state, resolve the exact setting, make one coherent change, wait for save completion, then reopen and verify. Before retrying, read the current value. For global propagation, verify at least the affected setting and one representative child, and report that broader endpoint application remains pending unless fully observed.

Official reference: [Atera roles and account-level permissions](https://support.atera.com/hc/en-us/articles/218007917-Roles-and-permissions).
