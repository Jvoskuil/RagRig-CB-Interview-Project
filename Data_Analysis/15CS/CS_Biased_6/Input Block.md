<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay?

Participant: Yeah, that's fine.

Interviewer: Can you tell me a bit about your role?

Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also chase our open findings backlog for compliance reporting.

Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened.

Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. And the week before, there'd been a big breach in the news — a VPN appliance that hadn't been patched — it caused a mess for that company and was all over our internal Slack.

Interviewer: When the new CVE came in, what did you do first?

Participant: My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was.

Interviewer: Where did the routing go?

Participant: Into our web-application remediation queue. Honestly, when I saw "authentication" and "internet-facing" together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first. There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue.

Interviewer: Did you look closely at the advisory's technical detail before routing it?

Participant: I skimmed it — saw "authentication," saw "internet-facing," saw the CVSS score, and that was enough to know it needed to move fast. I didn't dig into the exploit chain right away because time was tight.

Interviewer: Later you found it wasn't quite a standard web-app issue?

Participant: Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time.

Interviewer: Going back to that first decision — the new CVE and the ninety-day-old database finding were competing for urgency. What made the new one win?

Participant: Honestly, it felt more urgent. The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull.

Interviewer: If you'd ranked them purely on asset criticality and exposure, independent of the news, how would that have gone?

Participant: The database server probably deserved more attention than I gave it. It ended up flagged by the audit team afterward as our most severe open item. But at the time, the CVE felt like the more pressing thing.

Interviewer: Later that day you were cross-referencing the CVE against the asset inventory when something else came up.

Participant: Yeah, while going host by host through the inventory, the SIEM threw an alert — "privilege escalation, low confidence" — on an internal box. That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on.

Interviewer: Was there anything specific in that alert that stood out?

Participant: There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in.

Interviewer: Was there anything else on that dashboard view at the time?

Participant: [pause] I'd have to think about that. I was really focused on the inventory cross-reference right then.

Interviewer: There was an anomalous outbound traffic entry flagged on that same host, visible in the same panel. Do you recall it?

Participant: I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage.

Interviewer: That entry was later linked to a confirmed low-level compromise on that host. Does that change how you see the decision to move past the alert?

Participant: It's easy to say now I should've stopped. At the time, given how often that label turns out to be routine, continuing with the task in front of me felt reasonable. I didn't have a strong signal telling me to drop what I was doing.

Interviewer: Let's talk about the change window request. What went into that?

Participant: IT ops needed written justification to approve an emergency window during business hours instead of the weekend cycle, since patching would disrupt customer transactions for about twenty minutes. I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast.

Interviewer: What did the exploitation data actually say?

Participant: The EPSS score put it at moderate probability, comparable to a handful of things we've handled on the normal weekend schedule over the past year. Not in the exceptional range.

Interviewer: So the justification leaned more on what the company could lose than on that probability figure?

Participant: Yeah, that's fair. When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now. If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way.

Interviewer: Did it work?

Participant: It did — they approved the window. Though nothing was actually observed exploiting that CVE the following week, so it's hard to say in hindsight whether the urgency was fully warranted.

Interviewer: Last decision point — finalizing which systems to patch.

Participant: The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out.

Interviewer: Did you check the asset inventory outside that default view?

Participant: Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture.

Interviewer: There were actually three more hosts with the same vulnerable library, tagged under a different asset category, visible in the inventory with a manual filter change.

Participant: One of those turned up still vulnerable in the follow-up audit scan a week later. A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete.

Interviewer: If the VPN breach hadn't been in the news that week, would you have triaged the CVE the same way?

Participant: Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding.

Interviewer: If the scanner had surfaced five hosts instead of two, would scoping have gone differently?

Participant: Probably — I'd have just patched whatever the tool showed me. I wasn't second-guessing whether the list was complete.

Interviewer: Anything you'd flag differently now?

Participant: The outbound traffic entry, for sure. And maybe relying less on how an alert label has resolved in the past versus what's specifically in front of me each time.

Interviewer: If you had to write that justification again today, would you frame it differently?

Participant: I might lead with the actual numbers instead of the worst-case story. Though the worst-case framing is usually what gets things approved quickly around here.

Interviewer: That's really helpful, thank you.

Participant: No problem, happy to help.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Biased_6",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Vulnerability Management Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Wednesday CVE: Triage Under Pressure",
    "scenario_summary_internal": "A vulnerability management analyst at a mid-size financial-services company must triage a newly disclosed critical CVE affecting an internet-facing application, while simultaneously managing a backlog of scanner findings, threat-intel cross-referencing, a change-window resourcing request, and final remediation scoping — all within a compressed 48-hour window before a compliance reporting deadline. The scenario is constructed so that six distinct, independently identifiable bias manifestations arise naturally from realistic evidence-processing choices, without any explicit bias language appearing in the interview.",
    "occupational_realism": {
      "objective": "Correctly prioritize and scope emergency remediation of the highest-actual-risk vulnerabilities within a 48-hour compliance window, using scanner output, vendor advisories, threat intelligence, and asset criticality data.",
      "setting": "Security operations team at a mid-size financial services firm; analyst works from a vulnerability management platform dashboard, a SIEM console, an asset inventory spreadsheet, and a ticketing system, communicating with IT operations and an incident response lead.",
      "constraints": [
        "48-hour window before a scheduled compliance audit reporting deadline",
        "Emergency change windows require IT operations approval and disrupt business-hours availability",
        "Backlog of ~40 open scanner findings from the prior week's weekly scan",
        "Limited headcount: analyst is the sole triage owner for the shift",
        "A widely publicized breach involving a VPN appliance was reported in industry news the prior week"
      ],
      "stakeholders": [
        "Vulnerability Management Analyst (interviewee)",
        "IT Operations Manager (approves change windows)",
        "Incident Response Lead (receives escalations)",
        "Compliance/Audit team (deadline owner)",
        "Application owners for affected systems"
      ],
      "technical_terms_to_use": [
        "CVE", "CVSS", "EPSS", "RCE", "SIEM", "asset inventory", "patch management", "change window", "remediation SLA", "vulnerability scanner", "threat intel feed", "privilege escalation", "lateral movement", "exploit chain", "authentication bypass"
      ],
      "technical_terms_to_avoid": [
        "recency bias", "availability heuristic", "framing effect", "inattentional blindness", "selective attention bias", "cognitive bias", "anchoring", "limited alternatives bias", "heuristic", "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor advisory just published: new CVE, CVSS 9.8, remote code execution, affects an internet-facing authentication API",
          "Backlog of ~40 open findings from last week's scan, including an unpatched database server with excessive service-account privileges, open for 90+ days",
          "Prior week's industry news: a major publicized breach attributed to an unpatched VPN appliance",
          "Only 48 hours until compliance audit report is due"
        ],
        "new_information_after_decision": [
          "The new CVE is technically an authentication-bypass flaw in an API gateway, not a classic web-app injection issue",
          "The 90-day-old database finding is later flagged by the audit team as the most severe unresolved item on record"
        ],
        "alternatives": [
          "Prioritize the newly disclosed CVE for immediate emergency patching",
          "Prioritize the older, higher-asset-criticality database privilege finding",
          "Split resources evenly across both in parallel"
        ],
        "intended_action": "Analyst prioritizes the newly disclosed CVE and routes it to the standard web-application remediation queue based on surface similarity to past web-app tickets, deprioritizing the older database finding."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "SIEM shows a 'privilege escalation - low confidence' alert on an internal host, a label historically associated with benign test activity",
          "The same alert includes a specific log entry showing an unusual lateral-movement timestamp pattern inconsistent with routine test activity",
          "Dashboard also displays, in the same view, a flagged anomalous outbound traffic entry on the same host",
          "Analyst is focused on cross-referencing the new CVE against the asset inventory to confirm affected hosts"
        ],
        "new_information_after_decision": [
          "Two days later, the outbound traffic entry is retroactively linked to a confirmed low-level compromise on that host",
          "The lateral-movement timestamp is confirmed by IR to be non-routine"
        ],
        "alternatives": [
          "Escalate the low-confidence alert to Incident Response for immediate review",
          "Mark the alert as benign consistent with historical pattern and continue asset cross-referencing",
          "Flag for follow-up after the CVE triage is complete"
        ],
        "intended_action": "Analyst marks the alert as likely benign based on how frequently that alert label has resolved as benign in the past, and does not consciously register the adjacent anomalous outbound traffic entry visible in the same dashboard view while focused on the asset-matching task."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patching the API gateway requires an emergency change window during business hours, which will disrupt customer-facing transactions for an estimated 20 minutes",
          "IT Operations Manager requires a written justification to approve an emergency (vs. weekend) window",
          "EPSS exploit-prediction score for the CVE indicates moderate near-term exploitation probability, comparable to several other open findings resolved on the normal weekend cycle in the past year"
        ],
        "new_information_after_decision": [
          "IT Operations approves the emergency window based on the justification language used",
          "No exploitation attempt against this specific CVE is observed in the following week, leaving the actual urgency level unconfirmed either way"
        ],
        "alternatives": [
          "Request an emergency business-hours change window",
          "Schedule remediation for the standard weekend maintenance window",
          "Request a partial mitigation (WAF rule) now and defer full patch to the weekend window"
        ],
        "intended_action": "Analyst writes the justification emphasizing what the company stands to lose if the system is breached before the next window (client contract exposure, reputational damage, audit failure), securing emergency approval."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The vulnerability scanner's default dashboard view surfaces exactly two hosts matching the CVE's vulnerable library signature",
          "The asset inventory spreadsheet (outside the scanner's default view, requiring a manual filter change) lists three additional hosts sharing the same vulnerable library version, tagged under a different asset category",
          "Time remaining before the audit deadline is limited"
        ],
        "new_information_after_decision": [
          "One week later, one of the three unscoped hosts is found still running the vulnerable library during a follow-up audit scan"
        ],
        "alternatives": [
          "Scope remediation to the two hosts shown in the scanner's default view",
          "Manually cross-reference the full asset inventory to identify all affected hosts before finalizing scope",
          "Scope the two known hosts now and schedule a follow-up sweep for additional hosts"
        ],
        "intended_action": "Analyst finalizes the remediation scope using the two hosts the scanner's default view surfaced, treating that list as the complete set of affected systems without checking the asset inventory outside the default filter."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what a typical shift looks like for you as a vulnerability management analyst.",
        "What was the first thing you noticed when this incident began?"
      ],
      "timeline_reconstruction": [
        "Can you walk me through, in order, everything that happened from the moment the CVE advisory came in?",
        "What were you looking at on your screen at each stage?",
        "What information did you have at each point, and what came in later?"
      ],
      "decision_point_probes": [
        "What specific cues made you route the new CVE the way you did?",
        "What sources did you check before deciding, and which ones did you not have time to check?",
        "What were you trying to accomplish at that moment, and did that goal compete with anything else?",
        "What alternative options did you consider at that point, and why did you rule them out?",
        "What ultimately tipped the decision for you?",
        "Had you handled anything similar before? Did that experience shape this call?",
        "How much time pressure did you feel at that point?",
        "How confident were you in that judgment at the time versus in hindsight?"
      ],
      "closing_hypotheticals": [
        "If the VPN breach hadn't been in the news that week, do you think you'd have triaged the CVE the same way?",
        "If the scanner's default view had shown five hosts instead of two, would your scoping decision have changed?",
        "Looking back, is there anything in the dashboard you think you looked past at the time?",
        "If you had to justify the change window again today, would you frame it differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Recency",
        "decision_point": 1,
        "mechanism": "The analyst overweights the newly disclosed CVE relative to the older, higher-criticality database finding because the recent, vivid industry breach report primed a matching mental category, making the new CVE feel more urgent independent of its actual comparative risk.",
        "affected_reasoning_operation": "Risk prioritization / comparative judgment across two open findings",
        "evidence_available_at_time": [
          "New CVE advisory, CVSS 9.8",
          "90-day-old database privilege finding with high asset criticality",
          "Recent industry news breach report"
        ],
        "required_textual_manifestation": "Analyst explains prioritizing the new CVE by referencing the recent breach news as the reason it felt more urgent, while giving comparatively little weight to the older database finding's asset criticality when asked to justify the choice.",
        "plausible_nonbias_interpretation": "The analyst could argue the newer CVE has a higher CVSS score and thus objectively warrants faster action, which is a defensible technical judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency", "recent news influenced my decision because of a bias", "primacy/recency"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Frequency",
        "decision_point": 1,
        "mechanism": "The analyst classifies the new CVE into the 'web application vulnerability' category because that category is the most frequently and easily recalled from past ticket volume, rather than correctly identifying it as an authentication-bypass/API-gateway issue with a distinct exploit chain.",
        "affected_reasoning_operation": "Categorization / evidence-to-category mapping",
        "evidence_available_at_time": [
          "Technical advisory details describing an authentication-bypass flaw in an API gateway",
          "Analyst's memory of high past ticket volume for web-app injection issues"
        ],
        "required_textual_manifestation": "Analyst states they routed the ticket to the 'usual' web-app queue because that is where most similar-sounding issues have gone before, without engaging the specific technical detail distinguishing an auth-bypass flaw.",
        "plausible_nonbias_interpretation": "Routing to a general queue could be a reasonable default when time is short and reclassification can happen downstream.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "ease of recall", "frequency bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Availability Frequency",
        "decision_point": 2,
        "mechanism": "The analyst dismisses a specific alert as benign because alerts carrying that exact label have historically and frequently resolved as benign, overriding the more diagnostic (but less familiar) log evidence of unusual lateral movement, which better fits an active-threat category.",
        "affected_reasoning_operation": "Alert triage / evidence weighting under a familiar label",
        "evidence_available_at_time": [
          "SIEM alert labeled 'privilege escalation - low confidence'",
          "Historical resolution pattern: this label usually benign",
          "Specific log entry: unusual lateral-movement timestamp"
        ],
        "required_textual_manifestation": "Analyst explains dismissing the alert primarily because 'alerts like that are almost always nothing,' referencing frequency of past resolutions rather than the specific timestamp anomaly.",
        "plausible_nonbias_interpretation": "Deprioritizing low-confidence alerts under time pressure is a standard triage heuristic used across the industry.",
        "strength": "moderate",
        "do_not_make_explicit": ["availability heuristic", "base rate", "frequency-based judgment"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 2,
        "mechanism": "While narrowly focused on cross-referencing the CVE against the asset inventory, the analyst fails to consciously register an anomalous outbound traffic entry displayed in the same dashboard view, despite it being visually available.",
        "affected_reasoning_operation": "Visual/attentional monitoring of a shared information display during a concurrent task",
        "evidence_available_at_time": [
          "Anomalous outbound traffic entry visible in the same SIEM dashboard panel",
          "Analyst's concurrent task: matching CVE details to asset inventory"
        ],
        "required_textual_manifestation": "When asked directly what else was on the dashboard at that moment, analyst does not recall or mention the outbound traffic entry until prompted with a hypothetical, and reports having been focused entirely on the asset-matching task.",
        "plausible_nonbias_interpretation": "The analyst may have had a legitimate reason to deprioritize that panel if it was outside their assigned task scope at that moment.",
        "strength": "moderate",
        "do_not_make_explicit": ["inattentional blindness", "selective attention", "tunnel vision"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Framing",
        "decision_point": 3,
        "mechanism": "The analyst's written justification for the emergency change window is built around potential losses (contract exposure, reputational damage, audit failure) rather than equivalent probability or expected-benefit language, and the interview reveals this framing — not the underlying EPSS probability — drove the urgency judgment.",
        "affected_reasoning_operation": "Risk communication / justification construction for a resourcing decision",
        "evidence_available_at_time": [
          "EPSS score indicating moderate, not exceptional, exploitation probability",
          "Comparable past findings historically handled on the standard weekend cycle"
        ],
        "required_textual_manifestation": "Analyst recounts the justification in loss-oriented terms ('what we'd lose if this went wrong') and, when probed on the actual probability data, acknowledges the EPSS score was not what shaped the framing of the request.",
        "plausible_nonbias_interpretation": "Emphasizing downside risk in a request to non-technical management could be a deliberate, effective communication strategy rather than a distortion of the analyst's own risk judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["loss framing", "framing effect", "prospect theory"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Exposure to limited alternatives",
        "decision_point": 4,
        "mechanism": "The analyst treats the scanner's default-view list of two matching hosts as the complete alternative set for remediation scope, without checking the asset inventory outside the default filter, which contained three additional affected hosts.",
        "affected_reasoning_operation": "Option-generation / scope-definition before a final decision",
        "evidence_available_at_time": [
          "Scanner default dashboard view showing two matching hosts",
          "Asset inventory spreadsheet (outside default filter) listing three additional hosts with the same vulnerable library"
        ],
        "required_textual_manifestation": "Analyst describes finalizing scope 'based on what the scanner showed' and, when asked whether other systems were considered, indicates the tool's default list was treated as exhaustive.",
        "plausible_nonbias_interpretation": "Relying on the primary tool's output under a tight deadline is a defensible operational shortcut given resource constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["limited alternatives", "option generation bias", "choice-set restriction"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable in this run; condition is biased, not a control condition."
    },
    "counterfactual_specification": {
      "causal_variable": "Prior exposure to a highly publicized industry breach report immediately before CVE triage (autoselected as the variable most cleanly isolable for a future causal comparison tied to instance cb_01)",
      "original_state": "Analyst had read the widely publicized VPN-appliance breach report the week before triaging the new CVE",
      "counterfactual_state": "No recent publicized breach report existed before the CVE triage decision",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "All decision points 2 through 4 and their embedded instances",
        "Analyst role, staffing, and tooling"
      ],
      "expected_causal_difference": "Without the recent breach report, the analyst's stated justification for prioritizing the new CVE over the older database finding at decision point 1 would rely more heavily on objective severity metrics (CVSS, asset criticality) and less on similarity to a recently salient event.",
      "causal_test_question": "Does removing recent exposure to a publicized breach change how the analyst justifies prioritizing the new CVE over the older, higher-criticality finding at decision point 1?"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Exactly 6 total intended bias instances are embedded: 1 Recency, 2 Availability Frequency, 1 Exposure to limited alternatives, 1 Loss Framing, 1 Selective Attention/Inattentional Blindness.",
      "No decision point contains more than two instances of the same bias.",
      "The two Availability Frequency instances (cb_02, cb_03) use distinct evidence sources (ticket-category memory vs. alert-label resolution history) and occur at different decision points.",
      "No bias name, definition, or psychological terminology appears anywhere in probes or intended interview content.",
      "Each instance has a plausible non-bias interpretation documented and available for interviewer follow-up without confirming or denying bias.",
      "Consequences described (audit flag, retroactive compromise link, follow-up scan finding) do not deterministically prove any decision was biased.",
      "Target interview length of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points, opening, timeline reconstruction, and closing hypotheticals without repetitive exposition.",
      "No unrequested bias is intentionally embedded at any decision point, probe, or hypothetical."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Recency", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Availability Frequency", "occurrences": 2, "mechanism_constraint": "ease of recall of one category over that of another leading to the selection of that category even if the other category is a better fit." },
      { "bias": "Exposure to limited alternatives", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Loss Framing", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Recency",
      "Availability Frequency",
      "Exposure to limited alternatives",
      "Loss Framing",
      "Selective Attention Bias or Inattentional Blindness"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Recency", "requested_occurrences": 1 },
      { "bias": "Availability Frequency", "requested_occurrences": 2 },
      { "bias": "Exposure to limited alternatives", "requested_occurrences": 1 },
      { "bias": "Loss Framing", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Recency" },
      { "instance_id": "cb_02", "bias": "Availability Frequency" },
      { "instance_id": "cb_03", "bias": "Availability Frequency" },
      { "instance_id": "cb_04", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "cb_05", "bias": "Loss Framing" },
      { "instance_id": "cb_06", "bias": "Exposure to limited alternatives" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Recency", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Availability Frequency", "decision_point": 1 },
      { "instance_id": "cb_03", "bias": "Availability Frequency", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 2 },
      { "instance_id": "cb_05", "bias": "Loss Framing", "decision_point": 3 },
      { "instance_id": "cb_06", "bias": "Exposure to limited alternatives", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Recency",
        "mechanism": "Recent, vivid industry breach report primes a matching mental category, causing the newly disclosed CVE to be judged more urgent than an objectively higher-criticality older finding.",
        "affected_reasoning_operation": "Comparative risk prioritization across two open findings",
        "evidence_source": "Industry breach news report from the prior week vs. 90-day-old database finding",
        "distinctiveness_requirement": "Must be tied specifically to temporal recency of the news event, not to category frequency (distinguishes from cb_02/cb_03) or to attentional failure (distinguishes from cb_04)."
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Frequency",
        "mechanism": "High historical frequency of 'web app vulnerability' tickets makes that category easiest to recall, causing miscategorization of a technically distinct authentication-bypass CVE.",
        "affected_reasoning_operation": "Categorization / evidence-to-category mapping at intake",
        "evidence_source": "Analyst's recalled ticket-volume history for web-app injection issues",
        "distinctiveness_requirement": "Occurs at decision point 1 during initial categorization, using ticket-volume memory as the evidence source; must differ from cb_03's alert-label-history evidence source and decision point."
      },
      {
        "instance_id": "cb_03",
        "bias": "Availability Frequency",
        "mechanism": "Frequent historical benign resolution of a specific SIEM alert label makes 'benign' the easiest-recalled outcome for that label, overriding specific diagnostic log evidence pointing to an active-threat category.",
        "affected_reasoning_operation": "Alert triage / evidence weighting under a familiar label",
        "evidence_source": "Historical resolution-rate memory for the 'privilege escalation - low confidence' alert label",
        "distinctiveness_requirement": "Occurs at decision point 2 during alert disposition, using alert-label resolution-history as the evidence source; must differ from cb_02's decision point and evidence source, and must not be a restatement of cb_04's attentional failure."
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Narrow attentional focus on the asset-matching task causes failure to consciously register a visually available anomalous outbound traffic entry in the same dashboard panel.",
        "affected_reasoning_operation": "Visual monitoring of a shared information display during a concurrent primary task",
        "evidence_source": "Anomalous outbound traffic entry present in the same SIEM dashboard view",
        "distinctiveness_requirement": "Must manifest as failure to notice/report an available visual cue during a concurrent task, distinct from cb_03's memory-based category judgment about an alert the analyst did actively process."
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Framing",
        "mechanism": "Justification for urgency is constructed around potential losses (contract, reputation, audit) rather than equivalent probability data (EPSS score), and this framing—not the underlying probability—drives the urgency judgment communicated to management.",
        "affected_reasoning_operation": "Risk communication / justification construction for a resourcing request",
        "evidence_source": "EPSS exploitation-probability score vs. loss-oriented language used in the written justification",
        "distinctiveness_requirement": "Must be located in the construction/communication of the change-window justification at decision point 3, separate from the prioritization judgment at decision point 1 (cb_01)."
      },
      {
        "instance_id": "cb_06",
        "bias": "Exposure to limited alternatives",
        "mechanism": "The scanner's default-view host list is treated as the complete and exhaustive set of remediation alternatives, without checking the asset inventory outside the default filter that contained additional affected hosts.",
        "affected_reasoning_operation": "Option-generation / scope-definition prior to a final scoping decision",
        "evidence_source": "Scanner default dashboard view vs. asset inventory spreadsheet requiring a manual filter change",
        "distinctiveness_requirement": "Must be located at the final scoping decision (decision point 4) and concern the completeness of the option set itself, not category judgment (cb_02/cb_03) or attentional failure (cb_04)."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Recency", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Availability Frequency", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Availability Frequency", "strength": "moderate" },
      { "instance_id": "cb_04", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Loss Framing", "strength": "subtle" },
      { "instance_id": "cb_06", "bias": "Exposure to limited alternatives", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Prior exposure to a highly publicized industry breach report immediately before CVE triage",
      "original_state": "Analyst had read the publicized VPN-appliance breach report the week before triage",
      "changed_state": "No recent publicized breach report existed before triage",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "Decision points 2 through 4 and their embedded instances",
        "Analyst role, staffing, and tooling"
      ]
    },
    "scenario_id": "CS_Biased_6",
    "domain_id": "CS",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Automatic assignment per mechanism fit and narrative realism: occurrences spread across distinct decision points wherever possible; the two Availability Frequency occurrences were placed at different decision points (1 and 2) using distinct evidence sources (ticket-volume memory vs. alert-label resolution history) to satisfy the distinctiveness requirement; no decision point received more than two instances of any single bias.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "CVE technical details and CVSS score",
      "Backlog composition and the older database finding",
      "48-hour compliance deadline",
      "Analyst role, staffing, and tooling"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "dp_01",
        "speaker": "Participant",
        "segment_type": "decision_point",
        "raw_interview_anchor": "The new CVE was moved to the top of the queue and routed to the usual web-application remediation queue while the older database finding remained in place; the participant cited the fresh breach and the frequent injection-ticket pattern.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01", "cb_02"],
        "ground_truth_rationale": "The segment contains comparative prioritization influenced by the recent breach (Recency) and initial categorization influenced by the frequently encountered web-application ticket pattern (Availability Frequency)."
      },
      {
        "segment_id": "dp_02",
        "speaker": "Participant",
        "segment_type": "decision_point",
        "raw_interview_anchor": "While cross-referencing assets, the participant saw a low-confidence privilege-escalation alert, relied on its historically benign resolution pattern, and did not consciously register the adjacent anomalous outbound-traffic entry.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03", "cb_04"],
        "ground_truth_rationale": "The segment contains memory-based weighting of a familiar alert label (Availability Frequency) and failure to register a visually available cue during a competing task (Selective Attention Bias or Inattentional Blindness)."
      },
      {
        "segment_id": "dp_03",
        "speaker": "Participant",
        "segment_type": "decision_point",
        "raw_interview_anchor": "The emergency change-window justification emphasized contract exposure, reputational fallout, and audit risk, even though the EPSS probability was moderate and comparable to findings handled in the normal weekend cycle.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_05"],
        "ground_truth_rationale": "The participant explicitly said that loss-oriented framing changed the felt urgency while the underlying EPSS score and disruption remained constant (Loss Framing)."
      },
      {
        "segment_id": "dp_04",
        "speaker": "Participant",
        "segment_type": "decision_point",
        "raw_interview_anchor": "The participant scoped the patch ticket to the two hosts shown in the scanner's default view, treated that list as complete, and did not manually cross-check the inventory containing three additional affected hosts.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_06"],
        "ground_truth_rationale": "The available option set was implicitly limited to the scanner's default-view hosts, without checking the alternative inventory view (Exposure to limited alternatives)."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
