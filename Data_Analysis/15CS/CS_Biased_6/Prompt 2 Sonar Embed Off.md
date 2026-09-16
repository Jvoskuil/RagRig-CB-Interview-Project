You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "No retrieved scientific-paper corpus passages were supplied; bias labels and mechanisms are drawn from general cognitive-science knowledge and no corpus evidence is cited."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Alarm fatigue",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Automation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Inattentional blindness",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias", "Recency effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the urgency, probability, or relevance of an event by the ease with which examples come to mind, often from salience or recency.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "CVE triage prioritization versus older database finding",
      "decision_point_description": "Choosing whether to prioritize the new critical CVE or the long-open database-server finding",
      "affected_reasoning_operation": "Urgency and prioritization judgment",
      "bias_specific_mechanism": "The recent high-profile VPN breach was highly salient and easily recalled, which inflated the perceived urgency and likelihood of a similar internet-facing CVE and led the participant to prioritize it over the older database finding.",
      "manifestation_in_interview": "The participant explicitly connected the fresh breach story to the new CVE and said the story shaped how fast he moved past the database finding.",
      "effect_on_reasoning_or_decision": "The CVE was moved to the top of the queue and standardized remediation workflow while the database finding remained unaddressed; the database item was later flagged by audit as the most severe open item.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was.",
          "evidence_explanation": "Shows salience-driven initial triage based on resemblance to the recent breach rather than a comparative severity analysis of the database finding."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull.",
          "evidence_explanation": "The participant directly states that recency and salience of the breach gave the CVE stronger subjective pull than the older, objectively severe database finding."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding.",
          "evidence_explanation": "The participant acknowledges the news story likely changed the urgency judgment, supporting the availability mechanism."
        }
      ],
      "correction_or_counterevidence": "The CVE had a high CVSS score and was internet-facing, so high urgency was plausible on objective grounds. The database finding was old and had no new trigger, so deprioritizing it was not necessarily irrational.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper corpus was supplied; this label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": ["Representativeness bias", "Prototype heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Estimating category membership or likelihood by similarity to a prototype or familiar pattern while underweighting base rates or specific diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Routing the new CVE to a remediation queue",
      "decision_point_description": "Deciding which remediation queue should own the CVE",
      "affected_reasoning_operation": "Categorization and classification decision",
      "bias_specific_mechanism": "The CVE's superficial features, \"authentication\" and \"internet-facing,\" matched the participant's prototype of common injection-style web-app tickets; he categorized the CVE on that similarity and did not use the advisory's more specific diagnostic information about the API gateway.",
      "manifestation_in_interview": "The participant said his head went straight to the familiar injection-style ticket pattern and that he did not stop on the advisory line suggesting the API-gateway team was the better owner.",
      "effect_on_reasoning_or_decision": "The CVE was routed to the usual web-application remediation queue rather than the API-gateway team, then later redirected, costing time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, when I saw \"authentication\" and \"internet-facing\" together, my head just went straight to the same kind of injection-style tickets that make up most of what crosses my desk — that's the pattern I see constantly, so it's the one that came to mind first.",
          "evidence_explanation": "The participant used a familiar category prototype to classify the new CVE based on superficial features."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a line in the advisory pointing more toward the API-gateway team being the better owner, but I didn't stop on it long enough to change course, and it went into the usual queue.",
          "evidence_explanation": "Shows that diagnostic information was present but underweighted, consistent with representativeness-based classification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I skimmed it — saw \"authentication,\" saw \"internet-facing,\" saw the CVSS score, and that was enough to know it needed to move fast. I didn't dig into the exploit chain right away because time was tight.",
          "evidence_explanation": "This selective processing supports the mechanism: surface cues triggered a familiar category; deeper diagnostic detail was not processed."
        }
      ],
      "correction_or_counterevidence": "Time pressure was present, and the CVE did require rapid movement. The participant eventually accepted the redirect, suggesting the initial misclassification was recoverable and not strongly held.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper corpus was supplied; this label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Alarm fatigue",
      "alternative_labels": ["Alert fatigue", "Cry wolf effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Reduced responsiveness to warnings after frequent false or low-consequence alarms, leading to delayed or absent investigation of new alerts.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "SIEM low-confidence privilege-escalation alert triage",
      "decision_point_description": "Deciding whether to investigate the SIEM alert or continue the current asset-matching task",
      "affected_reasoning_operation": "Alert triage and investigation decision",
      "bias_specific_mechanism": "Repeated experience that the low-confidence privilege-escalation label was \"almost always nothing\" led the participant to dismiss the alert without investigating the unusual lateral-movement timestamp.",
      "manifestation_in_interview": "The participant reported seeing the same label many times and moving on despite registering an unusual log entry.",
      "effect_on_reasoning_or_decision": "He did not dig into the alert, so an unusual lateral-movement timestamp was not investigated; the same host was later linked to a confirmed low-level compromise.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on.",
          "evidence_explanation": "This is a direct report of habituation to the alert label, which is the core alarm-fatigue mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in.",
          "evidence_explanation": "Shows that he did not ignore the alert because it was completely invisible; he registered a specific unusual cue and still chose not to investigate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the time, given how often that label turns out to be routine, continuing with the task in front of me felt reasonable. I didn't have a strong signal telling me to drop what I was doing.",
          "evidence_explanation": "The participant explicitly rationalized the decision using the label's base rate, which supports the alarm-fatigue mechanism rather than a mere oversight."
        }
      ],
      "correction_or_counterevidence": "Using the label's low base rate could be a reasonable heuristic in a noisy alert environment; the alert was labeled low confidence, and the participant did not have a definitive signal at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper corpus was supplied; this label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Inattentional blindness",
      "alternative_labels": ["Perceptual blindness", "Attentional blindness"],
      "taxonomy_status": "established_label",
      "bias_definition": "Failure to perceive an unexpected visible stimulus when attention is engaged elsewhere, particularly under high cognitive load or task focus.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reviewing host inventory and SIEM side panel",
      "decision_point_description": "Whether the participant registered the anomalous outbound traffic entry visible on the same dashboard panel",
      "affected_reasoning_operation": "Attention and visual detection during inventory cross-reference",
      "bias_specific_mechanism": "The participant's attention was narrowly engaged on matching CVE-affected assets in the host inventory, so he did not register the side-panel anomalous outbound traffic entry even though it was visible.",
      "manifestation_in_interview": "The participant did not specifically remember the outbound traffic entry and said it was possible it was there and he just did not register it.",
      "effect_on_reasoning_or_decision": "The outbound traffic entry was not noticed or acted on; it was later linked to a confirmed low-level compromise on that host.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage.",
          "evidence_explanation": "This is an explicit description of attention being occupied by one task and failing to register a visible stimulus outside the attended area, matching inattentional blindness."
        }
      ],
      "correction_or_counterevidence": "The side panel was outside the participant's focal task of CVE-asset matching, so not noticing it may reflect ordinary selective attention rather than defective reasoning; however, the host and panel were part of the same dashboard view and he had alert-triage responsibilities.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper corpus was supplied; this label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Framing effect",
      "alternative_labels": ["Framing bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "When equivalent information leads to different evaluations or choices depending on whether it is framed in terms of losses or gains.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Emergency change-window justification",
      "decision_point_description": "Deciding how to write and justify the emergency patching window to IT operations",
      "affected_reasoning_operation": "Subjective urgency judgment and communication framing",
      "bias_specific_mechanism": "Evaluating the same moderate EPSS score and twenty-minute disruption through a loss-framed worst-case narrative increased the participant's subjective urgency, rather than the probability or operational facts themselves.",
      "manifestation_in_interview": "The participant explicitly said the same numbers framed as losses felt urgent, but would not have felt as urgent if framed around staying ahead of the patch cycle or keeping things running smoothly.",
      "effect_on_reasoning_or_decision": "The loss-framed justification was approved for an emergency business-hours change window, even though the EPSS score was moderate and no exploitation was observed the following week.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast.",
          "evidence_explanation": "Shows a deliberate loss-frame in the justification rather than a probability- or gain-based frame."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The EPSS score put it at moderate probability, comparable to a handful of things we've handled on the normal weekend schedule over the past year. Not in the exceptional range.",
          "evidence_explanation": "Establishes that the objective exploitation-probability information did not independently require the emergency frame."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sat down to write it, thinking through what we'd lose if it went wrong — the contract, the reputation hit, the audit exposure — made it feel like this had to move now. If I'd framed the same numbers around just getting ahead of the patch cycle or keeping things running smoothly, it probably wouldn't have felt as urgent to me, even though the underlying EPSS score and the twenty-minute disruption were exactly the same either way.",
          "evidence_explanation": "The participant directly contrasts loss and non-loss framings of identical information and reports a change in felt urgency, which is the core framing-effect pattern."
        }
      ],
      "correction_or_counterevidence": "Persuasive loss-framing may be a legitimate organizational communication strategy to secure timely remediation; the CVE was critical, and patching an internet-facing authentication API was plausible even without worst-case framing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper corpus was supplied; this label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Automation bias",
      "alternative_labels": ["Automation-induced complacency", "Overreliance on automation"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to over-rely on outputs from automated decision-support systems, treating them as complete or authoritative and reducing verification or cross-checking.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Finalizing patch scope from scanner dashboard",
      "decision_point_description": "Determining which hosts should be included in the patching ticket",
      "affected_reasoning_operation": "Scope finalization and completeness judgment",
      "bias_specific_mechanism": "The scanner dashboard's default list of two hosts was accepted as the full vulnerable population because it was the automated output in front of him; the participant did not question completeness or manually filter the asset inventory.",
      "manifestation_in_interview": "The participant said he treated the scanner's list as the full picture and was not second-guessing whether the list was complete.",
      "effect_on_reasoning_or_decision": "The ticket was scoped to two hosts; three additional vulnerable hosts were not patched, and one was still vulnerable in the follow-up audit scan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out.",
          "evidence_explanation": "Shows reliance on the default automated scanner output as the basis for the final patch list."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture.",
          "evidence_explanation": "Directly states that the scanner output was treated as complete without cross-checking the asset inventory."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "One of those turned up still vulnerable in the follow-up audit scan a week later. A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete.",
          "evidence_explanation": "Confirms that the missed hosts existed and that a manual check would have found them, while the scanner output was accepted as complete."
        }
      ],
      "correction_or_counterevidence": "The scanner dashboard was the normal workflow tool, and the deadline created time pressure; the more complete inventory view required a manual filter change that was not part of the default display.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper corpus was supplied; this label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper corpus was supplied, so findings rely on general cognitive-science knowledge rather than corpus-supported definitions or mechanisms.",
    "The analysis is based on retrospective self-report, which can be influenced by memory error or post hoc reconstruction.",
    "Several decisions occurred under genuine time pressure and with incomplete information, so some behaviors may also reflect ordinary task constraints rather than bias.",
    "The interview includes interviewer prompts that reveal later outcomes; those later outcomes were not treated as evidence of bias at the time."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Biased_6_Sonar_off",
  "interview_id": "CS_Biased_6",
  "system_prompt_id": "Sonar",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
