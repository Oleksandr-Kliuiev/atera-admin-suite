# Device lifecycle operations

## Onboard

1. Verify mode and target Customer/Site and folder IDs.
2. Search all agents for matching DeviceGUID, serial, hostname, MAC/IP context, OS, and recent retired/offline entries.
3. Select the correct OS-specific deployment method and prepare the installer without exposing its token.
4. After installation, wait for first check-in and verify AgentID, DeviceGUID, hostname, OS, agent version, serial, IP, and organization relation.
5. Assign folder and end user/contact as requested.
6. Calculate effective threshold and configuration profiles, then inspect all cumulative IT Automation profiles.
7. Assign intended profiles with exact scope and report queued/scheduled work.
8. Verify monitoring data and agent activity; endpoint software/patch outcome remains separate.

## Move or reassign

Before moving a device, inspect inherited threshold/configuration profiles, cumulative automation profiles, alert settings, user/contact relation, open tickets/alerts, billing attribution, and whether it monitors other devices. Resolve destination IDs and show the effective before/after configuration. Verify after refresh.

## Retire, uninstall, or delete

Treat retirement, dashboard deletion, and endpoint uninstall as different states. Confirm which the user wants.

- Retirement/offline handling: preserve the record and evidence according to the account policy.
- Online deletion: may send uninstall to the endpoint.
- Offline deletion: removes the dashboard record and may send uninstall when it returns online.
- Monitoring-agent dependency: reassign every dependent monitored device before deletion.

Immediately before deletion, present stable IDs, last seen, online state, dependencies, queued actions, open tickets/alerts, evidence retained, and reinstallation requirement. After commit, verify dashboard removal and report that endpoint uninstall is pending unless observed.

## Complete-list handling

Clear saved views and Customer/Site/folder/status filters. Search exact stable IDs first, then secondary identity. Traverse all pages or virtual rows while tracking AgentID/DeviceGUID. Do not infer absence from the current folder or online-only view.

## Official references

- [The Devices page](https://support.atera.com/hc/en-us/articles/9903603088284-The-Devices-page)
- [Install an agent](https://support.atera.com/hc/en-us/articles/360015643914-Install-an-agent)
- [Delete an Atera agent](https://support.atera.com/hc/en-us/articles/234734168-Delete-an-Atera-agent)
