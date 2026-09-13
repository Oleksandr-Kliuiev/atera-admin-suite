---
name: atera-script-remediation
description: Create, review, import, schedule, run, and verify endpoint scripts through Atera's authenticated browser, including personal and shared libraries, PowerShell, CMD, Bash, MSI, parameters, offline queues, bulk execution, IT Automation scheduling, and remediation evidence. Use for script-focused work, not ordinary remote support or patch profiles.
---

# Atera Script and Remediation

Treat every script as endpoint code execution. Resolve script by stable library identity and content hash when available, and devices by AgentID/DeviceGUID. Inspect full source, provenance, parameters, supported OS, execution user, privileges, timeout, network dependencies, logging, success criteria, rollback, and target state before running.

Read [references/script-safety.md](references/script-safety.md) for source review, shared-library trust, parameters and secrets, queueing, bulk scope, critical checkpoint, result interpretation, and independent verification.

Never run a shared/community or AI-generated script based only on title or rating. Never embed credentials, API keys, tokens, private keys, remote-access secrets, or customer-specific secrets in source or parameters. Use approved secure injection where available; otherwise stop.

Creating a non-running library entry may proceed when authorized. Any run, schedule, auto-healing attachment, or broad automation assignment is a critical commit. An exit code or Atera `Completed` state does not prove the intended system change.

Finish with script identity/hash, provenance, target count and IDs, execution context, queue expiry, per-device result/exit code, independently verified effect, failures, skipped targets, logs location, and rollback status—without secret values.
