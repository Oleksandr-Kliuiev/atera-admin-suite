# Send the requested report once through Outlook

Use **Outlook on the web in the same authenticated Chrome profile** on both Windows and macOS. Reuse its tab; if absent, use the Microsoft 365 app-launcher Outlook link or `https://outlook.office.com/` for standard Microsoft 365, preserving known tenant-cloud URLs. A missing tab does not mean missing authentication. Let the user complete login/MFA only if requested by the site. Do not use native Outlook, OS-specific automation, Gmail or Atera's mail sender for this workflow.

1. Resolve actual recipient addresses from explicit user instruction or a unique verified account/contact record. “Selected customer” defines report scope, not automatically its recipient. “Me” needs a verified address. If displayed email text and a `mailto:` destination disagree, neither wins: prepare the report and ask one clarification before sending to either. Never guess from names or domains.
2. In Outlook, verify the signed-in employee's mailbox and **From**, then use **New mail / New message**. Never hardcode the skill author's mailbox, browser profile, local paths, or recipients. A short complete inventory can go directly in the body unless a file was requested. If a file is needed, export the verified report, read the browser tool's current upload guidance, and use **Attach file → Browse this computer** or the current equivalent. Use the actual tool-returned file/path and supported chooser on this host, not a remembered macOS/Windows Downloads path. Verify the completed attachment, filename/type and content; do not substitute a public/OneDrive share link without authorization. If a required file cannot be attached, preserve the report and state that exact blocker; an adequate body-only report does not depend on downloading.
3. Verify **From**, resolved **To/CC/BCC** addresses, subject, report scope/count/dates and absence of unrelated client data; check actual attachment only when attaching. Do not assume Microsoft 365 admin login proves the correct sending mailbox. A specified send request is sufficient authorization; no duplicate permission checkpoint. If the list/export is incomplete or inconsistent, resolve it first or clearly present the limitation for the user's decision.
4. Select **Send** once. Check **Sent Items** for the intended recipient, subject and report/attachment. Distinguish sent/accepted from recipient delivery. If uncertain, inspect Drafts/Sent Items and **do not retry** unless evidence proves no submission occurred. Report generated/exported when sending was not completed.

Honor conditional sends: “if any / i tilfelle / i så fall / viss ja” requires qualifying matches. A verified complete zero means no email; incomplete or stale evidence is not a verified zero. Exclude unrequested licensing keys and unrelated customer data.

### Scheduling is a different task

Operational scheduling is documented at **Reports → report clock icon → parameters → Schedule**, selecting an existing enabled Contact/User or Technician and weekly/monthly timing. It sends a summary with a report link; it is not evidence of an immediate attachment send. Do not create a recurring schedule, a new contact, or modify an existing schedule for a one-time “email this report” request.

Source: [Schedule an Operational report](https://support.atera.com/hc/en-us/articles/115012156008-Schedule-an-Operational-report).

Advanced reports also document **Send Now** with permission/plan dependencies. These Atera-native options are for an explicitly requested Atera delivery/schedule, not a fallback for the Outlook workflow.

Source: [Schedule advanced reports](https://support.atera.com/hc/en-us/articles/6461075581468-Schedule-advanced-reports).

Outlook routes are documentation-backed, not a verified send: [Create and send](https://support.microsoft.com/en-us/outlook/create-and-respond-to-messages-in-outlook-web-app), [Attachments](https://support.microsoft.com/en-us/outlook/mail/add-pictures-or-attach-files-to-emails-in-outlook). Resolve localized labels from the current UI.

## Requested rehearsal

Rehearse read-only with the intended Chrome account, scope, and mailbox; verify route, export/counts, recipient resolution, attachment support, and report access. A draft does not prove sending works. Only send a test email when explicitly requested; distinguish observed results/time from documentation checks.
