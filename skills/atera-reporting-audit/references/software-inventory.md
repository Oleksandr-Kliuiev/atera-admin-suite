# Devices with a specified program installed

On **2026-09-28**, live Chrome navigation confirmed **Reports → Classic Reports → Monitoring → Software Inventory**, including Customer Name(s), Filter By, Agent Type, Exclude retired devices, and Generate controls. The report may appear inside an embedded legacy view; inspect that visible content. Generation/export/email remain documentation-backed, untested here. Apply the inventory scope already loaded by the entrypoint.

1. Open **Reports → Monitoring → Software inventory**. Set Customer/Site, **Filter By → Software Name** (publisher only when that is the requested criterion), and appropriate Agent Type. Set retired-device inclusion deliberately; click **Generate**.
2. Resolve the requested product using displayed name, publisher, and version. Default to all versions of that product unless a version was specified. Do not count similarly named updaters, plug-ins, or bundles as the product without evidence.
3. Expand each matching software row's device list and **Export** the list (PDF or Excel). For several versions, prefer the report's **Detailed Excel** export when it yields the scoped per-device data efficiently; it includes Customer/Site and date last checked. Keep the product/version columns, then reconcile unique devices across versions.
4. Never click **Uninstall** or use Software installation for inventory. If an Installed software device filter is already correctly applied and demonstrably complete, its native export can avoid regenerating the same report.

Source: [Software inventory](https://support.atera.com/hc/en-us/articles/115011963047-Operational-report-Software-inventory). Current [Devices advanced filters](https://support.atera.com/hc/en-us/articles/115012115908-Devices-page-advanced-filters) also documents an Installed software criterion.

Inventory is cached: official FAQ documents updates approximately every 12 hours while devices are online, with offline devices retaining cached information. Include **Date last checked** where available and describe results as Atera-reported inventory, not proof of installation at this instant. Report generation time is not each device's scan time. The native Software inventory report does not provide the inverse “devices missing this program”; that requires a complete scoped device universe and set difference, with unknown/stale inventory identified. Do not turn a report request into an endpoint script or mass-refresh operation.

Source: [Operational Reports FAQ](https://support.atera.com/hc/en-us/articles/22674665627676-Operational-Reports-FAQ).
