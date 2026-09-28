---
name: atera-integrations-api
description: "Atera integrations and API: secure key setup/reset, scoped reads/writes, imports/exports, mapping, webhooks, pagination, sync troubleshooting, and retries."
---

# Atera Integrations and API

Use the existing authenticated **Chrome** session and read the [shared browser contract](../atera-organization-lifecycle/references/browser-operation-contract.md) once per working context.

Read the relevant sections of [integration and API operations](references/integrations-api.md). Verify account/mode, integration, activation, data domains, and stable IDs. Use browser workflows by default; use API when requested or configured access materially improves the authorized task.

Before bulk operations, validate mappings, pagination, rate-limit/error handling, idempotency, rollback, and data minimization.

Never expose or persist an API key in model-visible output, prompts, history, source, catalogs, or reports. Use an approved secret store and masked fingerprint. Key reset invalidates old consumers and is a critical commit. Writes, destructive imports, activation, broader access, and webhook changes require exact authorization.

Report integration, domains, masked credential identifier, stable record IDs and read/created/updated/skipped/rejected counts, pagination, duplicates, sync/webhook state, failures, and rotation/human steps.
