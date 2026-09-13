# Access operations

## Role and scope model

Atera has preset Beginner and Admin roles. Beginner is view-only and new technicians can start there. Admin has unrestricted platform and all-Customer/Site access and cannot be reduced like a custom role. Keep at least one verified Admin.

For custom roles inspect categories individually, including:

- technician, group, and role administration;
- customer/site and folder scope;
- device edit/delete and remote management;
- scripts and IT Automation profiles;
- patches, software, shutdown, registry, and Event Viewer;
- ticket access, deletion, merge, private groups, and automation;
- contracts, billing, reports, exports, and account settings.

Roles may default to all Customers/Sites unless explicitly limited. Excluded RMM folders may remove operational permissions while devices remain visible. Verify both organization scope and folder exclusions.

## Invite, assign, or update

1. Verify account and mode.
2. Search enabled, disabled, and invited technicians by exact normalized email.
3. Inspect current role, scope, groups, availability, and authentication state.
4. Create or update idempotently; do not send a duplicate invitation.
5. For broad or privileged assignment, present the exact privilege delta and scope before saving.
6. Refresh and verify role, scope, group membership, and status independently.

## Deactivate

Inventory open tickets, private-group access, customer/site ownership, automation references, schedules, reports, integrations, and Admin coverage. Reassign required work first. Verify disabled status and remaining sessions where visible; do not claim SSO or external identity revocation unless observed there.

## Complete-list handling

Clear status and role filters, search exact email, and traverse pagination or virtual scrolling while tracking unique emails. Do not declare absent after one page or current group view.

Official references: [Roles and permissions](https://support.atera.com/hc/en-us/articles/218007917-Roles-and-permissions) and [Manage technician groups](https://support.atera.com/hc/en-us/articles/13859463867036-Manage-technician-groups).
