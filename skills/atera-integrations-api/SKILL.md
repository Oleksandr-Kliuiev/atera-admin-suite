---
name: atera-integrations-api
description: Administer Atera API access and integrations, including API-key handling and reset, REST inventory and writes, pagination, imports and exports, accounting or messaging integrations, webhooks, mapping validation, troubleshooting, and idempotent retries. Use for integration-focused requests; never expose or persist an Atera API key.
---

# Atera Integrations and API

Verify account name and mode, integration, data domains, requested operation, stable target IDs, and current activation. Browser remains the default for supervised UI workflows; use API only when the user requests it or configured integration access materially improves the authorized task.

Read [references/integrations-api.md](references/integrations-api.md) for key handling, reset impact, pagination, read/write boundaries, imports, webhooks, duplicate prevention, and verification.

The Atera REST API uses a sensitive account API key that can expose contacts and devices. Never reveal it in the browser, prompt, commentary, tool output, shell history, source code, catalog, or report. Use an approved secret store and masked fingerprint only. Reset invalidates consumers of the old key and is a critical commit.

API writes, destructive imports, scope expansion, integration activation, and webhook changes require exact authorization. Before bulk operations validate account mode, Customer/Site mapping, identifiers, field mapping, pagination, rate/error handling, idempotency, rollback, and data minimization.

Finish with integration, account mode, authorized data domains, masked credential identifier, records read/created/updated/skipped/rejected, pagination completeness, duplicate handling, webhook/sync state, failures, and rotation or human steps—never the key value.
