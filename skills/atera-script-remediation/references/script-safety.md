# Script safety and execution

## Review before execution

Inspect the complete source and record a content hash when possible. Identify language/file type, supported OS and architecture, execution identity, elevation, parameters, working directory, download URLs, package/repository trust, network calls, filesystem/registry/service changes, reboot behavior, persistence, data collection, logging, idempotency, success predicate, and rollback.

Reject or escalate scripts that are obfuscated, truncated, unsigned when policy requires signing, destructive beyond scope, secret-bearing, dynamically download unpinned code, disable security controls without exact authorization, or lack a verifiable outcome.

Treat Shared Script Library and AI-generated content as untrusted until reviewed and copied into the controlled library.

## Scope and queue

Resolve every target by stable ID and classify OS, online/offline state, server/workstation role, maintenance window, and exclusions. Scripts can queue for offline devices; select the shortest queue duration consistent with the task and report expiry. Avoid overlapping execution through threshold auto-healing, IT Automation profiles, manual runs, or other scripts.

## Critical checkpoint

Present script name/hash, purpose, material changes, exact targets, execution identity, parameters with secrets redacted, queue duration, timeout, maintenance window, user/reboot impact, success predicate, and rollback. Reuse exact authorization already given; obtain only missing scope or authorization.

## Verify

Track queued, running, exit status, stdout/stderr availability, and activity/Recent Processes. `Completed` or exit code 0 means no reported execution error, not necessarily success. Independently verify the service, process, file, version, registry/configuration, account, network state, or other promised outcome.

For runs exceeding the immediate UI window, use Activity Log or Recent Processes. Before retrying, inspect prior results and target state.

Official references: [Run a script](https://support.atera.com/hc/en-us/articles/218040797-Run-a-script) and [Recent Processes](https://support.atera.com/hc/en-us/articles/360013411639-Operational-reports-Recent-Processes).
