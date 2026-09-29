# Windows family inventory

For “does a named customer still have Windows 10 PCs?” start in **Reports → Classic Reports / Operational reports → Monitoring → Auditor**. On **2026-09-29**, a fresh customer-scoped report with **Exclude retired devices** checked verified that the report exposes workstations, OS editions, and Last seen for each device. The report offered a customer selector, **Generate** and **Export**. Do not take one matching device page as the complete answer; use the report's current results on each run.

For broader Windows desktop/server family, edition or licensing questions, use **Reports → Classic Reports / Operational reports → Monitoring → Microsoft licensing** as below. On **2026-09-28**, Chrome showed Windows desktop and Server family options; Windows 10 generation and device results were verified. Choose the requested available family, not this example by default.

## Report path

1. Reuse an already open matching report; otherwise open **Reports → Monitoring → Microsoft licensing**. A report may render in an embedded legacy frame; inspect that visible frame. Use current labels/links, not saved element IDs or guessed routes.
2. Set **Customer Name(s)** to the exact customer/site or explicitly **All** for global scope. Keep **Agent Name(s) = All** and **Office Edition(s) = All** unless narrowed. Verify selected labels after menus close.
3. Clear previous **Operating System(s)** selections, then select the requested family (e.g. Windows 10, Windows 11, Windows Server 2019). Include its editions, such as Pro and IoT Enterprise LTSC, unless restricted. If an edition/build/version was requested, refine the generated rows accordingly. Do not substitute a different available OS for an absent option: use [OS overview](os-overview.md). This is an OS-family selector, not Software Name; update packages and kernel/build prefix `10.*` do not identify Windows 10 (Windows 11/server also use it).
4. Select **Generate** once and wait for results. Verify customer/all scope, OS filter, **Stations** count, distribution and device rows. Reconcile unique devices against Stations before any additional edition/version restriction, then give the qualifying count. Include customer, device, OS edition/version and stable ID/freshness only if exposed. Cover all rows before calling the list complete.
5. Report **Atera-reported inventory**. Generation time is not endpoint scan time; missing freshness does not establish which machines are currently online or recently checked. A positive report proves inventory matches, not live endpoint verification. Zero is usable only after correct report, complete scope and successful generation are established; an empty/loading grid or unsuccessful Devices search is not evidence of absence.
6. For “if any / i tilfelle / i så fall”, prepare delivery only when qualifying matches exist; a verified zero means report zero and do not send. If coverage/freshness is uncertain, disclose it rather than claiming no matching PCs. Follow [delivery](report-delivery.md) when sending is requested.

## Minimal disclosure and alternatives

Microsoft licensing also contains Windows/Office product keys. An OS inventory request does not need them. Send only the verified customer/device/OS list and relevant limitations; a short list in the email body is sufficient unless a file was requested. For a file, use supported column selection or build a minimal export from complete verified rows. Do not attach a raw licensing report containing unrequested keys.

If this report/OS option is unavailable, use [OS overview](os-overview.md) when licensed/permitted; preserve the requested scope and establish complete detail before conclusions.

Use Devices only for a user-requested device-view workflow or an explicitly accepted fallback. Do not return to it for this report-first request. Software Inventory answers installed-application questions; a Windows update package is not operating-system evidence. If Auditor lacks complete OS/device detail in the current UI, use Microsoft licensing or OS Overview and verify the same customer, workstation and retired-device scope before claiming a count.

Sources: [Microsoft licensing report and filters](https://support.atera.com/hc/en-us/articles/115003072068-Operational-report-Microsoft-licensing), [OS overview](https://support.atera.com/hc/en-us/articles/17885207693596-Analytical-reports-OS-overview).
