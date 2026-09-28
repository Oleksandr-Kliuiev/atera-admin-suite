---
name: atera-script-remediation
description: "Atera endpoint scripts: create/review/import library entries, PowerShell/CMD/Bash/MSI, parameters, scheduling, offline/bulk execution, and verified remediation."
---

# Atera Script and Remediation

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Read [script safety and execution](references/script-safety.md). Resolve library ID/content hash and device IDs. Review complete source, provenance, execution context, timeout, dependencies, success criteria, rollback, and target state before running; titles/ratings do not establish trust.

Never embed secrets in source or parameters. Use approved secure injection or stop. A non-running library entry may be prepared when authorized; execution, scheduling, auto-healing attachment, or broad automation assignment is a critical commit.

Report script ID/hash/provenance, target IDs/count, execution context, queue expiry, per-device results/exit codes, independently verified effects, failures, skipped targets, private log location, and rollback.
