# Windows 10 device list

On **2026-09-28**, live Chrome navigation confirmed **Devices → Filters → Advanced filters**, with an **OS edition** criterion, operator, value, and Apply control. Filtering/results/export remain untested here; confirm available operators and labels live. Apply the inventory scope already loaded by the entrypoint.

1. Open **Devices → Filters**. Apply the Customer/Site scope and only requested folder/status restrictions. Clear conflicting saved filters, retaining the requested scope.
2. Open **Advanced filters → Operating system → OS edition**. Use the live supported operator/value that matches Windows 10 editions. If it is a text match, match the Windows 10 product name; if enumeration, include all relevant Windows 10 editions. Validate returned product labels. Do not identify Windows 10 from the kernel/build prefix `10.*`, which also appears on other Windows products.
3. Apply, observe the updated count and a sample of OS product names, and include the **OS edition** column. Include device name, Customer/Site, stable ID if offered, and last-seen/status fields as available. **OS version** may mean release/build on Devices; do not assume fields have identical semantics across reports.
4. Export the filtered Devices view using the observed download control (documented Excel export). Verify the export carries the scope and Windows 10 criterion; apply the common completeness check.

Sources: [Devices advanced filters](https://support.atera.com/hc/en-us/articles/115012115908-Devices-page-advanced-filters), [Devices page, columns and export](https://support.atera.com/hc/en-us/articles/9903603088284-The-Devices-page).

Fallback only if the primary route is unavailable: **Reports → Analytical reports → Presets → OS overview**, if licensed and permitted. Apply scope, then drill into the agent count for the Windows 10 product row. This route is documented but report access varies. Preset reports may be limited to 500 rows: reconcile coverage and partition scope if necessary; never call a clipped report complete. Do not purchase analytics or clone/build a custom report merely to bypass a missing primary control without authorization.

Sources: [OS overview](https://support.atera.com/hc/en-us/articles/17885207693596-Analytical-reports-OS-overview), [Analytical reports](https://support.atera.com/hc/en-us/articles/5666497171612-Atera-s-analytical-reports).
