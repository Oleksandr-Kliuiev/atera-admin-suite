# Repository guidance

Read `docs/AI_CONTEXT_MAP.md` before changing a skill. Work inside the smallest relevant skill folder and avoid loading unrelated references.

Keep every focused skill independently usable after plugin installation. Shared hierarchy, authorization, queue, and verification invariants may be stated concisely in each entrypoint; detailed domain procedures belong in that skill's `references/` directory.

Never commit API keys, installer tokens, remote-access credentials, scripts containing secrets, device exports, customer/user lists, session material, or a real `.atera/operations-catalog.yaml`. The public catalog is synthetic.

Keep automatic invocation descriptions mutually discriminating. `atera-admin-suite` applies only when explicitly named; focused skills own ordinary Atera requests. Treat every Atera account and managed endpoint as production unless the user explicitly identifies a lab.

Before mutation, verify account mode (`msp` or `it_department`), exact customer/site, folder, device or object, current state, effective inherited profiles, and complete target scope. Distinguish assigned, queued, running, Atera-reported completion, and independently verified endpoint outcome.

Running scripts, deploying software or patches, initiating remote access, rebooting or shutting down devices, changing auto-healing, deleting agents or organizations, resetting API keys, deactivating privileged technicians, and broad assignment changes are critical commits.
