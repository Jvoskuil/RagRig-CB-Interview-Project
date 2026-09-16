You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay?

Participant: Sure, that's fine.

Interviewer: Can you tell me a bit about your role?

Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also work through our open findings backlog for compliance reporting, and I sit in on the weekly risk review with application owners.

Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened.

Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. There'd also been some industry news about a breach at another company the week before, though that wasn't really something I was thinking about directly when this came in — just background noise on the security channels, the kind of thing that's always circulating.

Interviewer: When the new CVE came in, what did you do first?

Participant: I read through the advisory, checked the CVSS score and the exposure — internet-facing, no compensating control in front of it, no WAF rule that would catch this pattern — and decided it needed to jump ahead of the backlog. The database finding is serious on paper, but at that point I didn't have a confirmed exploit path for it, just the privilege configuration itself and how long it had been sitting there. So it came down to weighing a confirmed critical exposure against an older, structurally risky one without fresh evidence of active exploitability.

Interviewer: How confident were you in that call?

Participant: Reasonably, but not completely. If I'd had time to pull a fresh risk assessment on the database server that morning, it's possible that would've changed the ordering. I didn't have that luxury, and honestly both items had a legitimate claim to going first.

Interviewer: Where did you route the new CVE?

Participant: Into our standard remediation workflow, tagged toward the web-facing application team, since it touches a customer-facing API and that team handles most of our external-facing patch coordination. It turned out to be more specifically an authentication-bypass issue in the API gateway rather than a typical injection bug, which meant a slightly different exploit chain than I'd first assumed, but the initial routing wasn't far off and the handoff to the right owner happened within the same day.

Interviewer: Walk me through what happened next, later that day.

Participant: While I was cross-referencing the CVE against our asset inventory, the SIEM threw an alert — "privilege escalation, low confidence" — on an internal host. I pulled up the log entry, saw a lateral-movement timestamp that looked a little off from the usual pattern, and there was also an outbound traffic flag on the same host in the same view.

Interviewer: What did you do with that?

Participant: I looked at both — the timestamp and the outbound entry — but neither one on its own had enough corroborating detail to justify pulling away from the CVE triage right then. No matching indicator from the threat intel feed, no other host showing similar activity, nothing in the ticket history suggesting a known campaign. I made a note to loop back once the CVE work was further along and kept going.

Interviewer: Two days later that outbound entry turned out to be linked to an actual low-level compromise. Looking back, do you read that decision differently?

Participant: It's hard to say. Given what I had at the time — a low-confidence label and a somewhat unusual but unconfirmed pattern — I don't think escalating immediately was obviously the right call either. It could've gone either way with the same information in front of me. I've seen similar-looking situations resolve as nothing more than a test process before, and I've also seen them turn out to matter, so I don't think this one particular case tells me much either way about how I generally handle it.

Interviewer: Let's talk about the change window request.

Participant: Patching the API gateway meant an emergency change window during business hours, about twenty minutes of disruption to customer transactions. IT ops needed a written justification to approve that instead of waiting for the weekend cycle.

Interviewer: What went into the justification?

Participant: I put in both the EPSS number — moderate probability, not exceptional — and what the exposure meant in practical terms: the contract implications, the audit angle, and the disruption window itself. I didn't deliberately lead with one over the other, honestly. It read as a fairly standard risk memo, the same format I use for most emergency requests.

Interviewer: Which part do you think actually got it approved?

Participant: I genuinely don't know. IT ops doesn't usually explain which line convinced them. Could've been the score, could've been the business language, could've been that the ask was only for twenty minutes rather than a longer outage. I couldn't tell you with confidence which one mattered most.

Interviewer: Did anything happen afterward that would clarify that?

Participant: Not really. No exploitation was observed against that CVE in the following week, but that doesn't tell me whether the request was overstated or exactly right — we patched it, so there was nothing left to observe either way. It's genuinely inconclusive from where I sit.

Interviewer: Last decision point — scoping which systems got patched.

Participant: The scanner's default view showed two hosts with the matching vulnerable library. Given the deadline, I scoped the ticket to those two, but I also flagged a follow-up sweep of the broader asset inventory for the next week, since I know that default view doesn't always capture everything depending on how assets are tagged in different categories.

Interviewer: One of three additional hosts under a different category turned out to still have the vulnerable library a week later.

Participant: Right, and that's a fair miss. I did build in the follow-up step, it just didn't happen fast enough given everything else on my plate that week. Whether a full manual cross-check up front versus a scheduled follow-up was the better trade-off given the deadline — I go back and forth on that even now.

Interviewer: If you'd had more time before the deadline, would any of these have gone differently?

Participant: Maybe the database server would've gotten a proper fresh look instead of being compared mostly on paper. And I might've pushed the manual inventory check earlier instead of scheduling it after the ticket closed. Hard to know for sure without actually having had that time.

Interviewer: If the scanner had shown five hosts instead of two, would scoping have changed?

Participant: I'd have patched what was in front of me either way, so probably not much different in terms of process — the follow-up sweep would just have had a shorter list left to check afterward.

Interviewer: Looking back, is there anything you'd weigh differently now?

Participant: Maybe how much weight I gave the SIEM alert without a corroborating signal. Not sure I'd act differently even now with the same information, but it's the one I think about.

Interviewer: If you had to write the change-window justification again, would you present it differently?

Participant: Possibly lead more with the numbers and less with the business language, just to see if it changes anything. I don't have strong evidence either framing actually mattered to the outcome.

Interviewer: That's really helpful, thank you for walking through it in detail.

Participant: No problem, glad to help.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Ambigious_6",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Vulnerability Management Analyst",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "The Wednesday CVE: Triage Under Pressure (Ambiguous Control)",
    "scenario_summary_internal": "A vulnerability management analyst at a mid-size financial-services company must triage a newly disclosed critical CVE affecting an internet-facing application, while simultaneously managing a backlog of scanner findings, a low-confidence SIEM alert, a change-window resourcing request, and final remediation scoping, all within a compressed 48-hour compliance window. The scenario mirrors CS_Biased_6 in domain, role, structure, vocabulary, actors, and decision count, but every decision is constructed to be genuinely underdetermined: each has a plausible, defensible non-bias justification and insufficient information for an observer to conclude any specific distorted reasoning process occurred. No named bias mechanism is intentionally instantiated.",
    "occupational_realism": {
      "objective": "Correctly prioritize and scope emergency remediation of the highest-actual-risk vulnerabilities within a 48-hour compliance window, using scanner output, vendor advisories, threat intelligence, and asset criticality data.",
      "setting": "Security operations team at a mid-size financial services firm; analyst works from a vulnerability management platform dashboard, a SIEM console, an asset inventory spreadsheet, and a ticketing system, communicating with IT operations and an incident response lead.",
      "constraints": [
        "48-hour window before a scheduled compliance audit reporting deadline",
        "Emergency change windows require IT operations approval and disrupt business-hours availability",
        "Backlog of ~40 open scanner findings from the prior week's weekly scan",
        "Limited headcount: analyst is the sole triage owner for the shift",
        "General awareness of an industry breach reported the prior week, mentioned only as ambient context, not as a stated reason for any specific choice"
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
          "General industry awareness of an unrelated breach reported the prior week, not directly discussed as a decision factor",
          "Only 48 hours until compliance audit report is due"
        ],
        "new_information_after_decision": [
          "The new CVE is technically an authentication-bypass flaw in an API gateway, confirmed after deeper review",
          "The database finding is later flagged by the audit team as a severe unresolved item, though its exploitability had not been independently reassessed at triage time"
        ],
        "alternatives": [
          "Prioritize the newly disclosed CVE for immediate emergency patching",
          "Prioritize the older, higher-asset-criticality database privilege finding",
          "Split resources evenly across both in parallel"
        ],
        "intended_action": "Analyst prioritizes the newly disclosed CVE, citing its CVSS score, internet-facing exposure, and the absence of any existing compensating control, while noting the database finding lacks a similarly confirmed exploit path at that time — a judgment call between two legitimately serious but differently characterized risks."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "SIEM shows a 'privilege escalation - low confidence' alert on an internal host",
          "The alert includes a log entry showing a somewhat unusual lateral-movement timestamp",
          "Dashboard also displays an anomalous outbound traffic entry on the same host, which the analyst reviews alongside the alert",
          "Analyst is concurrently cross-referencing the new CVE against the asset inventory"
        ],
        "new_information_after_decision": [
          "Two days later, the outbound traffic entry is retroactively linked to a confirmed low-level compromise on that host",
          "IR later notes the lateral-movement timestamp was non-routine, though corroborating indicators were sparse at the time"
        ],
        "alternatives": [
          "Escalate the low-confidence alert to Incident Response for immediate review",
          "Note both the alert and the outbound traffic entry but continue asset cross-referencing given no corroborating indicator of compromise",
          "Flag for follow-up after the CVE triage is complete"
        ],
        "intended_action": "Analyst reviews both the alert and the adjacent outbound traffic entry, judges that neither individually meets the threshold for interrupting the CVE triage given the available corroborating evidence, and defers full investigation — a defensible call given genuinely limited diagnostic detail at the time, with no stated reliance on how often the alert label has resolved historically."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patching the API gateway requires an emergency change window during business hours, disrupting customer-facing transactions for an estimated 20 minutes",
          "IT Operations Manager requires a written justification to approve an emergency (vs. weekend) window",
          "EPSS score indicates moderate near-term exploitation probability, comparable to several other findings resolved on the normal weekend cycle in the past year"
        ],
        "new_information_after_decision": [
          "IT Operations approves the emergency window",
          "No exploitation attempt against this specific CVE is observed in the following week, leaving the actual urgency level unconfirmed either way"
        ],
        "alternatives": [
          "Request an emergency business-hours change window",
          "Schedule remediation for the standard weekend maintenance window",
          "Request a partial mitigation (WAF rule) now and defer full patch to the weekend window"
        ],
        "intended_action": "Analyst's justification presents both the EPSS estimate and the potential business consequences together without a stated preference for one framing over the other, and the interview does not establish which factor was actually decisive — a genuinely ambiguous resourcing judgment."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The vulnerability scanner's default dashboard view surfaces exactly two hosts matching the CVE's vulnerable library signature",
          "The asset inventory spreadsheet, outside the scanner's default view, lists three additional hosts sharing the same vulnerable library version under a different asset category",
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
        "intended_action": "Analyst scopes to the two hosts shown by the scanner and separately schedules a follow-up sweep of the broader inventory given time constraints, a partial-verification compromise whose adequacy is genuinely debatable rather than a clear case of treating one source as exhaustive."
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
        "What specific cues made you decide the way you did?",
        "What sources did you check before deciding, and which ones did you not have time to check?",
        "What were you trying to accomplish at that moment, and did that goal compete with anything else?",
        "What alternative options did you consider at that point, and why did you rule them out?",
        "What ultimately tipped the decision for you?",
        "Had you handled anything similar before? Did that experience shape this call?",
        "How much time pressure did you feel at that point?",
        "How confident were you in that judgment at the time versus in hindsight?"
      ],
      "closing_hypotheticals": [
        "If you'd had more time before the deadline, would you have approached any of these differently?",
        "If the scanner's default view had shown five hosts instead of two, would your scoping decision have changed?",
        "Looking back, is there anything you think you weighed differently than you would today?",
        "If you had to write the change-window justification again, would you present it differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "CS_Biased_6",
      "features_to_match": [
        "Domain, role, setting, and stakeholder set",
        "Four-decision-point structure and chronology",
        "Same operational objective, constraints, and 48-hour deadline",
        "Same technical vocabulary and tool set (scanner, SIEM, asset inventory, EPSS, CVSS)",
        "Same surface incident type: new critical CVE, low-confidence SIEM alert, change-window request, host-scoping decision",
        "Comparable difficulty and emotional tone (time pressure, professional composure)"
      ],
      "features_to_remove_or_change": [
        "Remove explicit attribution of urgency to a recently salient breach story",
        "Remove explicit statement that a frequently recalled ticket category or alert-label history displaced consideration of a better-fitting category",
        "Remove explicit statement that an available visual cue went completely unregistered due to narrow attentional focus",
        "Remove explicit statement that loss-oriented language, rather than probability data, drove the urgency judgment",
        "Remove explicit statement that a single tool's default output was treated as an exhaustive alternative set without any partial verification"
      ],
      "ambiguity_boundary": "Each decision point must retain at least one genuinely plausible non-bias justification and at least one detail that leaves the analyst's actual reasoning basis underdetermined, without the interview explicitly resolving which factor was decisive. The ambiguity must arise from realistically incomplete information and reasonable trade-offs, not from artificial vagueness or contradictory statements."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable for this run (ambiguous_control condition); autoselected placeholder retained for structural consistency with the paired biased scenario: prior exposure to a highly publicized industry breach report immediately before CVE triage",
      "original_state": "Not activated in this condition",
      "counterfactual_state": "Not activated in this condition",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "Analyst role, staffing, and tooling"
      ],
      "expected_causal_difference": "Not applicable; no causal manipulation is performed in this condition.",
      "causal_test_question": "Not applicable; this run is not a counterfactual condition."
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Zero intended bias instances are embedded for Recency, Availability Frequency, Exposure to limited alternatives, Loss Framing, and Selective Attention/Inattentional Blindness.",
      "Each decision point includes a genuinely plausible non-bias justification and leaves the analyst's decisive reasoning basis underdetermined.",
      "No bias name, definition, or psychological terminology appears anywhere in probes or intended interview content.",
      "Vocabulary, structure, decision count, actors, setting, and difficulty match CS_Biased_6 as required for a paired control.",
      "Consequences described (audit flag, retroactive compromise link, follow-up scan finding) do not deterministically prove any decision was biased or unbiased.",
      "Target interview length of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points, opening, timeline reconstruction, and closing hypotheticals without repetitive exposition.",
      "No named-bias mechanism from the manifest is intentionally instantiated at any decision point, probe, or hypothetical.",
      "Ambiguity is achieved through realistic informational incompleteness, not exaggerated contradiction or suspiciously neutral phrasing."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      { "bias": "Recency", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Availability Frequency", "occurrences": 0, "mechanism_constraint": "ease of recall of one category over that of another leading to the selection of that category even if the other category is a better fit." },
      { "bias": "Exposure to limited alternatives", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Loss Framing", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 0, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Recency",
      "Availability Frequency",
      "Exposure to limited alternatives",
      "Loss Framing",
      "Selective Attention Bias or Inattentional Blindness"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Recency", "requested_occurrences": 0 },
      { "bias": "Availability Frequency", "requested_occurrences": 0 },
      { "bias": "Exposure to limited alternatives", "requested_occurrences": 0 },
      { "bias": "Loss Framing", "requested_occurrences": 0 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "CS_Biased_6",
    "counterfactual_variable": {
      "name": "Not applicable in this condition",
      "original_state": "Not applicable",
      "changed_state": "Not applicable",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "Analyst role, staffing, and tooling"
      ]
    },
    "scenario_id": "CS_Ambigious_6",
    "domain_id": "CS",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "No occurrences requested; ambiguous_control condition requires zero intended instances of all named target biases. Decision points were instead constructed to preserve genuine ambiguity and plausible non-bias justifications at each of the four decision points, mirroring the structural positions used for bias instances in the paired biased scenario (CS_Biased_6) without instantiating any bias mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "CVE technical details and CVSS score",
      "Backlog composition and the older database finding",
      "48-hour compliance deadline",
      "Analyst role, staffing, and tooling",
      "Four-decision-point structure and domain vocabulary matching CS_Biased_6"
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
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "decision_point_1_prioritization",
        "raw_interview_anchor": "When the new CVE came in, what did you do first? ... I decided it needed to jump ahead of the backlog.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Zero-bias ambiguous-control segment. The prioritization is supported by CVSS, internet-facing exposure, and lack of compensating controls; the ambient industry breach is explicitly disclaimed as a decision factor."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_point_2_siem_triage",
        "raw_interview_anchor": "The SIEM threw an alert — privilege escalation, low confidence ... I made a note to loop back once the CVE work was further along and kept going.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Zero-bias ambiguous-control segment. The participant reviewed both signals and sought corroboration before deferring investigation; limited diagnostic detail and competing triage demands provide plausible non-bias explanations."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_point_3_change_window",
        "raw_interview_anchor": "Patching the API gateway meant an emergency change window ... I put in both the EPSS number ... and what the exposure meant in practical terms.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Zero-bias ambiguous-control segment. The justification presented probability and business consequences together, and the interview does not establish that either framing drove the outcome."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_point_4_patch_scoping",
        "raw_interview_anchor": "The scanner's default view showed two hosts ... I also flagged a follow-up sweep of the broader asset inventory.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Zero-bias ambiguous-control segment. Scoping the visible hosts while scheduling broader verification is an explicit time-constrained trade-off, not a hidden bias instance."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": [
        "Interviewer",
        "Participant"
      ],
      "retrieved_corpus_support_used": true,
      "analysis_scope_note": "Analysis focused on affirmative transcript evidence for cognitive biases in vulnerability management decision episodes. Speaker labels were recognized as Format B; retrieval context was used only for conceptual grounding."
    },
    "identified_bias_summary": [
      {
        "bias_label": "automation complacency",
        "identified_occurrence_count": 1
      }
    ],
    "identified_occurrences": [
      {
        "occurrence_id": "obs_001",
        "classification_status": "identified",
        "confidence": "low",
        "bias_label": "automation complacency",
        "alternative_labels": [
          "complacency",
          "automation-induced complacency",
          "automation bias"
        ],
        "taxonomy_status": "established_label",
        "bias_definition": "A tendency in human-automation interaction to under-sample or insufficiently verify available information when an automated system provides a recommendation or default output, leading to decision-making based on less verification than is needed.",
        "attributed_to_speaker": "Participant",
        "evidence_speaker": "Participant",
        "decision_episode_label": "Scoping patch targets from scanner default view",
        "decision_point_description": "The participant chose to scope the emergency patch ticket to the two hosts shown in the scanner's default view rather than performing an immediate full manual cross-check of the broader asset inventory.",
        "affected_reasoning_operation": "Information sampling and verification of an automated output during patch-scoping decision",
        "bias_specific_mechanism": "The scanner's default view served as the operative basis for the target list, and the participant did not manually verify whether that default view omitted vulnerable assets despite explicitly knowing that it can miss assets depending on tagging. This constitutes less information sampling than necessary to fully verify the automated output.",
        "manifestation_in_interview": "The participant described relying on the scanner default view to identify two vulnerable hosts and scoping the ticket to those two under deadline, while acknowledging the default view is not always complete and scheduling only a later follow-up sweep.",
        "effect_on_reasoning_or_decision": "The immediate patch scope was limited to two scanner-identified hosts; three additional hosts in a different category remained unpatched until detected about a week later, so the under-verification affected remediation coverage.",
        "interview_evidence": [
          {
            "speaker": "Participant",
            "verbatim_quote": "The scanner's default view showed two hosts with the matching vulnerable library. Given the deadline, I scoped the ticket to those two, but I also flagged a follow-up sweep of the broader asset inventory for the next week, since I know that default view doesn't always capture everything depending on how assets are tagged in different categories.",
            "evidence_explanation": "This quote directly shows that the participant used the scanner's default output as the operative patch scope while recognizing the default view is incomplete. The decision to defer broader verification rather than perform it immediately is consistent with automation complacency in information sampling."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "Right, and that's a fair miss. I did build in the follow-up step, it just didn't happen fast enough given everything else on my plate that week.",
            "evidence_explanation": "This confirms the initial patch scope missed additional vulnerable hosts and that the follow-up verification was delayed. It supports under-verification, though workload also contributed."
          }
        ],
        "correction_or_counterevidence": "The participant did not entirely ignore the limitation: they flagged a follow-up sweep for the next week and later acknowledged the miss. Competing non-bias explanations include deadline pressure and competing workload, which may have driven the choice of a scheduled follow-up rather than immediate manual verification.",
        "retrieved_corpus_support_available": true,
        "corpus_support_note": "Retrieved support comes from Parasuraman and Manzey (2010), which defines complacency in automation use as under-sampling information needed to verify an automated aid's output.",
        "corpus_evidence": [
          {
            "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
            "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
            "authors": null,
            "publication_year": "2010",
            "retrieved_passage_or_finding": "This procedure allowed the investigators to assess the level of operator complacency in interaction with the aid by contrasting the actual information sampling behavior of operators with a “normative model” of optimal behavior. According to this logic, any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid. However, participants sampling less information than that necessary to completely verify the aid's recommendation were",
            "mechanism_supported_by_source": "The passage defines complacency in automation use in terms of insufficient information sampling relative to what is needed to fully verify an automated aid's output.",
            "relevance_to_this_occurrence": "The participant’s acceptance of the scanner default view without immediate manual cross-checking parallels the under-sampling pattern described in the passage; the automated output was acted on while broader verification was deferred."
          }
        ]
      }
    ],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "plan continuation bias",
        "alternative_labels": [
          "plan continuation error"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Response to SIEM alert during critical CVE triage",
        "supporting_interview_quote": "I looked at both — the timestamp and the outbound entry — but neither one on its own had enough corroborating detail to justify pulling away from the CVE triage right then. No matching indicator from the threat intel feed, no other host showing similar activity, nothing in the ticket history suggesting a known campaign. I made a note to loop back once the CVE work was further along and kept going.",
        "plausible_mechanism": "The participant may have continued the already initiated CVE triage plan despite ambiguous security signals from the SIEM alert, which could reflect plan continuation bias.",
        "why_not_identified": "The transcript provides a strong non-bias explanation: the alert was labeled low confidence, no threat-intel match, no similar activity, and the signals were ambiguous. There is no affirmative evidence that commitment to the current plan distorted interpretation or threshold; the participant consciously weighed the signals and scheduled follow-up."
      }
    ],
    "no_supported_biases_found": false,
    "limitations": [
      "Analysis is based on retrospective self-report rather than direct observation of behavior.",
      "Retrieved corpus support was limited to the provided passages.",
      "Competing explanations such as deadline pressure and workload cannot be fully separated from automation complacency in the scoping decision."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Ambigious_6_Sonnet_on",
  "interview_id": "CS_Ambigious_6",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
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
