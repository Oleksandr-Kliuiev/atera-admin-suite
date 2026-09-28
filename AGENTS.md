# Repository guidance

Read `docs/AI_CONTEXT_MAP.md` before changing a skill. Work inside the smallest relevant skill folder and avoid loading unrelated references.

Keep every focused skill independently usable after plugin installation. Each specialist loads the shared Chrome contract once per working context, then only the needed domain references or sections. Keep detailed procedures in that skill's `references/` directory and reuse the task record across turns.

Never commit API keys, installer tokens, remote-access credentials, scripts containing secrets, device exports, customer/user lists, session material, or a real `.atera/operations-catalog.yaml`. The public catalog is synthetic.

Keep specialist invocation descriptions mutually discriminating. `atera-admin-suite` routes natural-language and voice requests without requiring a skill name. Select one owning specialist; lifecycle owners coordinate related domains and load another specialist only for its required critical action or detailed procedure. Treat every Atera account and managed endpoint as production unless the user explicitly identifies a lab.

Reuse the existing authenticated Chrome tab and profile, honoring mentioned tabs. Preserve the shared contract's freshness, scope, and authorization rules. Login/MFA, SSO, and required remote-user consent remain human steps.

Before mutation, verify account mode (`msp` or `it_department`), exact customer/site, folder, device or object, current state, effective inherited profiles, and complete target scope. Distinguish assigned, queued, running, Atera-reported completion, and independently verified endpoint outcome.

Running scripts, deploying software or patches, initiating remote access, rebooting or shutting down devices, changing auto-healing, deleting agents or organizations, resetting API keys, deactivating privileged technicians, and broad assignment changes are critical commits.

Reuse exact typed or spoken authorization and request only missing details. Requested report delivery authorizes one send to resolved recipients after checking account, scope, dates, format, and attachment. Prefer a supported native one-time send; otherwise use the supported export/attachment workflow in the existing authorized Chrome webmail session. Keep endpoint evidence gathering read-only. Extra recipients, recurrence, paid features, and endpoint changes need separate authorization. Verify the observed send outcome and never equate acceptance with recipient delivery or retry an uncertain send without evidence of no submission.
