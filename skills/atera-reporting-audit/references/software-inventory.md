# Devices with a specified program installed

Use this for any named installed application, not OS detection. A Software Name search for “Windows 10” can find update packages on another OS. Apply the entrypoint's inventory scope.

On **2026-09-28**, live Chrome confirmed **Reports → Classic Reports / Operational reports → Monitoring → Software inventory**, generation for a named application/customer, and per-version device detail. Export/email were not exercised. The report may appear inside an embedded legacy view; inspect its visible content.

1. Open that report and set the current request's form values:

   | Control | Value |
   |---|---|
   | Customer Name(s) | Exact named customer; **All / Select All** for “anyone / nokon” without a customer |
   | Filter By | Software Name; Software Publisher only for a publisher query |
   | Software Name / Version | Requested product; clear Version unless requested |
   | Agent Type | **Desktop for “PC / pc / PC-er / workstation”**; Server for servers; Mac for Macs; All only when device type is unrestricted |

   Verify these closed controls before **Generate**, especially **Desktop versus All**. Clear conflicting result-table searches and apply retired scope. A server in a PC-only result invalidates that scope/count; correct the filter and regenerate.
2. Resolve the requested product using displayed name, publisher, and version. Default to all versions of that product unless a version was specified. Do not count similarly named updaters, plug-ins, or bundles as the product without evidence.
3. **Total Software counts product/version rows, not unique devices.** Open each matching row's separate expand arrow at the far right of **Number of Devices**. Do not click the cell center: its hover action can open **Uninstall**. The observed arrow was a CSS icon (`i.atera-icon-maximize_filled`), not accessible text; confirm it in the current row's DOM before using that selector, or click the arrow from a fresh screenshot. Cancel unintended uninstall dialogs. Wait for the detail's actual device rows/count before reading; initial empty headings are loading. Detail shows device, Customer/Site, OS platform, installation date, Last checked and pagination. Do not select device checkboxes.
4. Reconcile unique devices across all matching versions/pages. For larger lists prefer **Export → Detailed Excel** for per-device data; a version's detail also has PDF/Excel export. Keep any download wait below the enclosing tool timeout and handle failure. If the download is not observed, inspect the current report once and continue via the per-version detail lists; do not repeat exports or abandon an accessible list. A small complete list can go in the email body. Keep customer/device/product/version/freshness only. Summary rows prove presence, not a complete list or unique count.
5. Follow [delivery](report-delivery.md) for a requested email. “If any / viss ja” means send once for qualifying matches; complete verified zero means no send. Loading/partial results, stale inventory or unsupported platforms cannot establish current absence. Stay in Reports for this workflow; do not use Software installation, Uninstall, scripts or a device refresh to gather inventory.

Source: [Software inventory](https://support.atera.com/hc/en-us/articles/115011963047-Operational-report-Software-inventory).

Inventory is cached: official FAQ documents updates approximately every 12 hours while devices are online, with offline devices retaining cached information. Include **Date last checked** where available and describe results as Atera-reported inventory, not proof of installation at this instant. Report generation time is not each device's scan time. The native Software inventory report does not provide the inverse “devices missing this program”; that requires a complete scoped device universe and set difference, with unknown/stale inventory identified. Do not turn a report request into an endpoint script or mass-refresh operation.

Source: [Operational Reports FAQ](https://support.atera.com/hc/en-us/articles/22674665627676-Operational-Reports-FAQ).
