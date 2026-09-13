# Browser operation contract

## Resolve the hierarchy

Confirm account name and mode before mutation and after redirects. In MSP mode resolve Customer and Contact; in IT Department mode resolve Site and User. Resolve organizations, folders, agents, tickets, contracts, profiles, and policies by stable IDs plus readable names. Never use row position or hostname alone.

## Stable interaction loop

1. Observe a fresh accessibility/UI state.
2. Resolve controls by semantic role, accessible name, visible value, or stable identifier.
3. Perform one coherent action or fill one unchanged form.
4. Wait for a meaningful readiness signal: loading completion, changed count, heading, URL, status, or acknowledgement.
5. Observe again and verify the persisted object independently.

Discard old element references after navigation, modal changes, refresh, sorting, or asynchronous updates. Before retrying any mutation, reread current state to determine whether the first attempt succeeded.

## Search, views, and pagination

Clear saved-view filters, search exact stable identifiers first, then secondary attributes. Include inactive, offline, closed, and archived states when relevant. Traverse every page or virtual row while tracking unique IDs and page boundaries. Never report `not found` after inspecting only the first page, visible folder, or default date range.

## Endpoint state and critical commits

Distinguish configuration saved in Atera from assignment, offline queueing, delivery, execution, reported completion, and independently verified outcome. Immediately before scripts, patches, software, auto-healing, remote sessions, reboot/shutdown, deletion, or broad assignments, show exact scope, online/offline count, schedule/timezone, queue expiry, user impact, exclusions, and rollback; obtain confirmation unless separately confirmed.

## Evidence and recovery

Keep a compact before/request/acknowledgement/after record. A toast is provisional. Use bounded retries and never create duplicate organizations, users, contacts, folders, agents, tickets, contracts, or profiles to compensate for uncertainty.
