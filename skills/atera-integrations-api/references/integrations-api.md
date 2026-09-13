# Integration and API operations

## Credentials

Atera API access uses an account API key sent with HTTPS requests. Treat it as a high-impact secret. Do not click Reveal unless the user explicitly needs a secure key-rotation/setup workflow and a secret destination is ready. Never emit the key through model-visible tools.

Store only integration name, owner, purpose, data domains, masked fingerprint, rotation date, and status. Resetting the key invalidates requests made with the old key; inventory every consumer and coordinate cutover first.

## API reads

Verify account mode and stable IDs before requests. The API can expose Agents, Alerts, Billing, Contacts, Contracts, Customers, Tickets, and related data depending on available endpoints. Request only necessary fields and scope. Honor documented pagination/continuation until exhaustion; record page/record counts and deduplicate by stable ID.

## API writes and retries

1. Resolve target by stable ID and read current state.
2. Validate exact desired delta and authorization.
3. Use supported idempotency or a durable external reference where available.
4. Submit the smallest mutation.
5. Read the object back independently.
6. After timeout or ambiguous response, query before retrying.

Never use display name or hostname as the sole write key. Report partial success per record.

## Imports and mappings

Before import, verify source provenance, account mode, encoding, locale/date/timezone, field mapping, Customer/Site and Contact/User semantics, folder and device identifiers, required values, duplicate strategy, validation preview, error handling, and rollback. Do not import secrets or unnecessary personal/device data.

## Webhooks and third-party integrations

Verify callback ownership, HTTPS, authentication, subscribed events, Customer/Site scope, payload minimization, retry behavior, loop prevention, and secret rotation. Integration activation or broader data access is a critical commit.

Official references: [Atera API](https://support.atera.com/hc/en-us/articles/219083397-API) and [Atera API FAQ](https://support.atera.com/hc/en-us/articles/11071761826844-API-FAQ).
