# Remote support operations

## Preflight

Verify device stable IDs, Customer/Site, folder, OS, online state, last logged-in user, related ticket/request, selected remote provider, technician permission, consent policy, and maintenance/user-availability constraints. Avoid connecting to a similarly named or stale device.

## Session workflow

1. Record current device and ticket state.
2. Obtain required user consent or confirm the approved unattended-support basis.
3. Start the configured provider without exposing credentials or bypassing authentication.
4. Confirm the remote hostname/device identity after connection.
5. Observe read-only evidence first: alerts, services, processes, logs, resources, software, recent changes, and ticket history.
6. Apply only the smallest authorized change.
7. Verify the outcome in the remote session and Atera after check-in.
8. Close remote tools and record session completion.

## High-impact controls

Before process termination, service/registry modification, command execution, logout, reboot, or shutdown, summarize exact target, likely user impact, unsaved-work risk, dependencies, expected downtime, and rollback. Do not disable EDR, firewall, encryption, backup, or monitoring unless the user explicitly authorizes the exact change and a restoration plan exists.

Do not upload, download, or inspect unrelated files. Redact personal or secret-bearing screen content from reports.

## Verification

A successful connection or command acknowledgement is not the support outcome. Verify the original symptom, service/process state, application behavior, connectivity, alert recovery, or other requested condition. Keep unresolved issues open in the related ticket.

Official reference: [Atera Agent Console](https://support.atera.com/hc/en-us/articles/215951197-The-Agent-Console).
