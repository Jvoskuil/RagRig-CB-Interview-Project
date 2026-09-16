You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our incident-response learning archive, not a performance review — you can skip anything you're not comfortable discussing. Can you start by stating your role and how long you've been on the Tier 2 triage rotation?

Participant: Sure. I'm a Tier 2 SOC analyst, been doing log and alert triage for about two and a half years, most of that on the overnight rotation. This shift was a fairly typical Tuesday-into-Wednesday, except we had a scheduled vulnerability scan running against the 10.14.0.0/16 range.

Interviewer: Good, let's go through what happened. Walk me through what you saw when you first opened the alert queue that night.

Participant: I logged into the SIEM around 1 a.m. and the queue already had close to 300 new alerts in about twenty minutes, which is a lot even for us. Handoff notes from the day shift flagged that vuln management had an authenticated scan scheduled starting midnight, so I expected noise. When I sorted the queue, something like 92% of everything was tagged as coming from the scan subnet — port scans, auth attempts, the usual scanner fingerprint. That matched what I expected to see.

Interviewer: What was your primary goal in those first ten minutes?

Participant: Get through the noise fast so I wouldn't blow the 45-minute SLA on anything that actually mattered. With that volume, you can't eyeball every single alert individually — you triage by pattern.

Interviewer: Okay, let's reconstruct the rest of the shift chronologically, then we'll go back and dig into specific decisions. What came after that initial queue review?

Participant: I ran our saved scan-window filter to bulk-close the low-severity scan-tagged alerts, then almost immediately got pulled into a phishing cluster — a bunch of similar-looking emails landing in different inboxes. I spent maybe twenty minutes on that while the shift lead was pinging me for status. Then around 2:40, EDR kicked out an anomaly on a finance workstation, FIN-WK-114, with a process making periodic outbound connections. I looked at that, made a call, and moved on. About forty minutes later, a threat intel feed update came back and changed the picture on that same host, so I escalated to IR.

Interviewer: Let's slow down on the first decision — closing that initial batch. What information did you actually have in front of you at the moment you applied the filter?

Participant: The queue view, sorted by source subnet and severity. Almost everything was scan-subnet, low severity. There was one alert from FIN-WK-114 — a DNS query to a domain I didn't recognize — but it was sitting at low severity too, so visually it didn't distinguish itself from the rest of the batch.

Interviewer: What other options did you consider before bulk-closing?

Participant: I could have spot-checked a random sample of the low-severity ones outside the scan subnet before closing, or set a rule to pull out anything touching non-IT departments like finance for individual review. Honestly, with SLA pressure and that volume, the batch filter felt like the efficient move. I ran it across the whole set.

Interviewer: And the FIN-WK-114 alert — what happened to it specifically?

Participant: It went out with the rest of the batch. I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up. I didn't isolate it as a finance host outside 10.14.0.0/16 until I came back to it hours later.

Interviewer: What would have needed to be different for you to catch that at the time?

Participant: Probably if the queue view had color-coded by subnet instead of just severity, or if I'd run the spot-check option instead of the full batch close. In hindsight it was sitting right there.

Interviewer: Let's move to the phishing cluster. What made you confident that was contained?

Participant: I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately. Given how fast the visible queue cleared, I told the shift lead it looked contained.

Interviewer: Did you verify that against anything else — inbox delivery logs, a manual sample?

Participant: Not at that point, no. The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too. I flagged it as contained in the ticket.

Interviewer: Was there anything in the queue at that time that didn't fit that picture?

Participant: There was one variant with a slightly different sender domain that the rule wouldn't have matched — I didn't clock that until later. At the time I was reading the drop in volume as the rule working.

Interviewer: Understood. Now the EDR anomaly on FIN-WK-114 — what led you to the backup-agent explanation?

Participant: The connection pattern — periodic, roughly every 55 seconds — looked a lot like something we'd seen twice in the previous two shifts, both traced back to a misconfigured backup agent on other hosts. That was fresh in my mind since I'd closed both of those tickets myself within the last week.

Interviewer: Did the current alert have a direct signature match to that backup agent?

Participant: No, it didn't — there was no IOC match, no clean fingerprint tying it to the agent. I noted it as "likely backup-agent artifact, monitor only" based mostly on the interval pattern resembling those recent cases, and moved on to the phishing follow-up.

Interviewer: Was pulling the process tree or checking the destination IP against threat intel an option at that point?

Participant: Yeah, it was, and normally I'd lean that way if I weren't juggling two things. Since the pattern matched what I'd just dealt with twice, it felt like a safe bet to downgrade it and keep an eye on it rather than treat it as new.

Interviewer: What told you it was "safe" specifically — the interval, or something else?

Participant: Mostly the interval and the fact that backup-agent issues had been the dominant explanation for anything beacon-like lately. If I'd seen this same alert two months ago, before those two tickets, I probably would've pulled the process tree first.

Interviewer: Let's get to the fourth point — the escalation. What changed?

Participant: About forty minutes later, threat intel updated and flagged that destination IP as a known C2 rendezvous point, which directly contradicted the backup-agent call. By then the SLA on that alert had already lapsed by twelve minutes, and my shift lead was tied up on another incident call for the next twenty.

Interviewer: What were your options at that point?

Participant: Escalate straight to IR with what I had, wait for the shift lead to be free for sign-off, or go back and rebuild the evidence chain from the earlier alerts first. I chose to escalate immediately — the SLA was already blown and waiting felt riskier than moving fast with an incomplete write-up.

Interviewer: How did that play out?

Participant: IR picked it up and confirmed lateral movement attempts from FIN-WK-114, consistent with that original DNS alert from hours earlier — the one that got closed in the batch.

Interviewer: Looking back across the night, at what point were you least certain about your read of the situation?

Participant: Probably the beacon classification. I remember having a flicker of doubt — no direct IOC match nagged at me a little — but the recent pattern felt like a strong enough anchor to act on given the time crunch.

Interviewer: A couple of hypotheticals to close. If the scan window hadn't been running that night, do you think you'd have handled the FIN-WK-114 alert differently?

Participant: Almost certainly. Without 300 scan alerts flooding the queue, that single DNS alert would have stood out on its own and I'd have looked at it individually.

Interviewer: If you hadn't been the one who wrote the suppression rule, would you have checked phishing containment differently?

Participant: Maybe — I might have been more inclined to ask someone else to verify it rather than trust the count dropping.

Interviewer: And if the last two shifts hadn't involved backup-agent false positives, how might you have approached the beacon differently?

Participant: I think I'd have gone straight to the process tree and IP lookup instead of pattern-matching against recent history. That comparison was really the whole reason I felt comfortable downgrading it.

Interviewer: Last one — what single process change would have caught this earlier?

Participant: Separating subnet visibility from severity in the queue view, so a scan-window filter can't accidentally sweep up a host that was never actually part of the scan. That's the gap that mattered most here.

Interviewer: That's really helpful, thank you for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Biased_3",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "SOC Analyst (Tier 2, Log/Alert Triage)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Recurring Beacon: Triage Under a Familiar Alert Storm",
    "scenario_summary_internal": "A Tier 2 SOC analyst handles an overnight surge of alerts during a scheduled vulnerability scan window. A genuine low-and-slow C2 beacon from a compromised finance-department workstation is embedded among a flood of known-benign scanner-triggered alerts. The analyst must triage, correlate, and escalate within a 45-minute SLA while juggling a parallel phishing campaign investigation. The narrative allows one instance each of selective attention/inattentional blindness (missing the beacon because attention is locked onto the dominant, familiar alert category), illusion of control (overconfidence in a custom suppression rule the analyst wrote controlling the situation), and recency bias (weighting the most recent shift's incident pattern too heavily when interpreting ambiguous traffic).",
    "occupational_realism": {
      "objective": "Triage a high-volume alert queue within SLA, correctly identify and escalate genuine intrusion activity, and avoid false-positive escalation fatigue during a known noisy scan window.",
      "setting": "Mid-size enterprise SOC, overnight shift, SIEM (Splunk-like) console, EDR alerts, ticketing system, concurrent phishing-campaign investigation open in another tab.",
      "constraints": [
        "45-minute SLA to triage and escalate critical alerts",
        "Scheduled authorized vulnerability scan generating ~300 benign alerts in the same window",
        "Single analyst on shift with a junior analyst available only for basic lookups",
        "Parallel active phishing campaign ticket demanding attention",
        "Custom suppression rule recently deployed to reduce scanner noise"
      ],
      "stakeholders": [
        "Tier 2 SOC Analyst (interviewee)",
        "Shift lead (remote, reachable by chat)",
        "Finance department (owner of affected workstation)",
        "Vulnerability management team (running the scan)",
        "Incident response team (on-call, not yet engaged)"
      ],
      "technical_terms_to_use": [
        "SIEM", "EDR", "beacon interval", "C2", "false positive", "suppression rule", "IOC", "pivot", "escalation SLA", "authenticated scan", "outbound DNS", "process tree"
      ],
      "technical_terms_to_avoid": [
        "selective attention", "inattentional blindness", "illusion of control", "recency bias", "cognitive bias", "confirmation bias"
      ],
      "excluded_themes": "NONE specified by caller"
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Alert queue shows 287 new alerts in 20 minutes, ~92% tagged as originating from the 10.14.0.0/16 scan subnet",
          "A single alert from a finance workstation (FIN-WK-114) shows a DNS query to an unfamiliar domain with low alert severity",
          "Shift handoff notes mention the vulnerability scan is scheduled and expected to generate noise"
        ],
        "new_information_after_decision": [
          "The FIN-WK-114 alert is bulk-closed along with scan noise using the saved 'scan-window' filter",
          "No further review of FIN-WK-114 occurs until phase 3"
        ],
        "alternatives": [
          "Apply the scan-window filter to bulk-triage low-severity alerts and move to the next queue segment",
          "Manually spot-check a random sample of low-severity alerts outside the scan subnet before bulk-closing",
          "Flag all alerts touching non-IT/non-scan subnets (e.g., finance) for individual review regardless of volume"
        ],
        "intended_action": "Analyst applies the scan-window filter to the whole batch, mentally treating the dominant scan-noise pattern as the only relevant signal and closing the FIN-WK-114 DNS alert along with it without noticing it falls outside the scanned subnet."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "A second, unrelated alert cluster appears: a phishing campaign is actively landing in several inboxes, generating IR tickets",
          "The analyst's custom suppression rule (deployed last week) is auto-tagging repeat sender domains as 'handled'",
          "Shift lead pings asking for an ETA on phishing containment"
        ],
        "new_information_after_decision": [
          "The suppression rule successfully mutes 40 duplicate phishing alerts, which the analyst interprets as full containment",
          "One phishing email variant with a slightly different sender domain is not covered by the rule and remains unflagged in the queue"
        ],
        "alternatives": [
          "Trust the suppression rule's tagging as sufficient evidence the phishing wave is contained and report containment to the shift lead",
          "Manually verify a sample of 'handled' alerts to confirm the rule caught all variants before reporting containment",
          "Ask the junior analyst to independently check inbox delivery logs for any bypass of the rule"
        ],
        "intended_action": "Analyst reports the phishing wave as contained based on the suppression rule's tagging behavior, attributing the drop in visible alerts to the rule's effectiveness rather than checking whether it fully covers the campaign's variants."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "EDR flags a process anomaly on FIN-WK-114: an unfamiliar process making periodic outbound connections roughly every 55 seconds",
          "Analyst recalls that the previous two shifts both involved false-positive beaconing alerts traced to a misconfigured backup agent",
          "The current alert lacks a direct IOC match to any known backup agent signature"
        ],
        "new_information_after_decision": [
          "The analyst notes the alert as 'likely backup-agent artifact, monitor only' and downgrades priority",
          "A pivot on the destination IP later shows no association with the organization's backup vendor"
        ],
        "alternatives": [
          "Downgrade the alert based on the pattern seen in the last two shifts and continue monitoring",
          "Pull the process tree and compare the destination IP against threat intel feeds before classifying",
          "Escalate as unknown-cause beaconing pending IOC verification, regardless of recent shift history"
        ],
        "intended_action": "Analyst classifies the beacon as a probable repeat of the recent backup-agent false positive because that explanation was the most recent and readily available pattern, without independently verifying the IOC or destination against current threat intel."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "A threat intel feed update flags the destination IP from phase 3 as a known C2 rendezvous point, contradicting the earlier 'backup-agent' classification",
          "SLA window for this alert has now elapsed by 12 minutes",
          "Shift lead is unavailable for the next 20 minutes (in another incident call)"
        ],
        "new_information_after_decision": [
          "Analyst escalates directly to IR with a full write-up",
          "IR later confirms lateral movement attempts originating from FIN-WK-114 consistent with the missed phase-1 DNS alert"
        ],
        "alternatives": [
          "Escalate immediately to IR with available evidence despite the SLA breach and shift lead's unavailability",
          "Wait for the shift lead to become available before escalating, to follow standard sign-off procedure",
          "Re-run the earlier phase-1 and phase-3 alerts through the SIEM to build a fuller evidence chain before escalating"
        ],
        "intended_action": "Analyst escalates to IR with the newly confirmed IOC; this decision point is used for probes and closing hypotheticals but is not assigned an intended bias instance."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you saw when you first opened the alert queue that night.",
        "What was your primary goal in the first ten minutes of the shift?"
      ],
      "timeline_reconstruction": [
        "What happened right after you applied the scan-window filter?",
        "How did the phishing campaign investigation fit into your attention during that period?",
        "What did you do between noticing the EDR anomaly on FIN-WK-114 and classifying it?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you at the moment you closed the FIN-WK-114 DNS alert?",
        "What made you confident the suppression rule had contained the phishing wave?",
        "What led you to compare the beaconing pattern to the previous two shifts specifically?",
        "When the SLA had already elapsed, what factored into your decision to escalate without the shift lead?"
      ],
      "cues": [
        "What in the alert list caught your eye first, and what didn't?",
        "Was there anything about the FIN-WK-114 alert's formatting or subnet that stood out or didn't stand out?"
      ],
      "information_sources": [
        "Which tools or logs did you check before each decision, and which did you not check?",
        "Did you consult threat intel feeds before or only after classifying the beacon?"
      ],
      "goals": [
        "At each point, what were you optimizing for — speed, accuracy, or something else?"
      ],
      "alternatives": [
        "What other options did you consider before bulk-closing the scan-window alerts?",
        "Could you have verified the suppression rule's coverage differently?"
      ],
      "decision_basis": [
        "What specifically told you the phishing wave was contained?",
        "What specifically told you the beacon was likely the backup-agent artifact?"
      ],
      "prior_experience": [
        "Had you seen this scan-window noise pattern before, and how did that shape your approach?",
        "How much did the last two shifts' backup-agent false positives influence this call?"
      ],
      "time_pressure": [
        "How did the SLA clock affect your triage choices in phase 1 and phase 4?"
      ],
      "uncertainty": [
        "At what point were you least sure about your classification, and what did you do about that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the scan window hadn't been running that night, do you think you'd have handled the FIN-WK-114 alert differently?",
        "If you hadn't deployed the suppression rule yourself, would you have double-checked phishing containment differently?",
        "If the backup-agent false positives from the prior two shifts hadn't happened, how might you have approached the beacon alert?",
        "Looking back, what single change to your process would have caught the beacon earlier?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 1,
        "mechanism": "Dominant, high-volume expected alert category (scan noise) captures attentional focus, causing a low-severity but out-of-pattern alert (finance workstation DNS query) to be processed as part of the batch and closed without individual notice, despite being visually/contextually distinguishable from the scan traffic.",
        "affected_reasoning_operation": "Evidence selection during bulk alert triage",
        "evidence_available_at_time": [
          "287 scan-subnet alerts vs. 1 alert from a non-scan subnet (finance)",
          "Shift handoff note priming expectation of scan noise"
        ],
        "required_textual_manifestation": "Analyst describes filtering and closing the batch as a single undifferentiated action, explicitly stating they did not notice the FIN-WK-114 alert fell outside the scan subnet until much later.",
        "plausible_nonbias_interpretation": "Reasonable workload-driven triage shortcut under SLA pressure with an unlucky miss, rather than a deliberate misjudgment of the DNS alert's threat level.",
        "strength": "moderate",
        "do_not_make_explicit": ["selective attention", "inattentional blindness", "tunnel vision"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of control",
        "decision_point": 2,
        "mechanism": "Analyst attributes the drop in visible phishing alerts to the effectiveness of a suppression rule they personally authored, overestimating their own configuration's coverage and control over the campaign's full variant set, rather than verifying actual delivery/blocking outcomes.",
        "affected_reasoning_operation": "Causal attribution of an observed outcome (fewer visible alerts) to a self-created control mechanism",
        "evidence_available_at_time": [
          "Suppression rule authored and deployed by the analyst the previous week",
          "40 duplicate alerts tagged 'handled' by the rule",
          "No independent verification of inbox delivery logs performed"
        ],
        "required_textual_manifestation": "Analyst states confidence that the phishing wave is contained specifically because 'my rule' is catching the variants, without citing independent evidence of full coverage.",
        "plausible_nonbias_interpretation": "A defensible engineering judgment that a recently tuned rule is working as intended, based on visible reduction in alert volume.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of control", "overconfidence", "authorship effect"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Recency",
        "decision_point": 3,
        "mechanism": "Analyst weights the pattern from the two most recent prior shifts (backup-agent false positives) disproportionately when classifying an ambiguous new beacon, treating recent memorable cases as more diagnostic than base-rate or current IOC evidence.",
        "affected_reasoning_operation": "Memory retrieval and pattern-matching used to classify ambiguous new evidence",
        "evidence_available_at_time": [
          "Beacon interval and process anomaly without a matching known-agent signature",
          "Memory of the previous two shifts' backup-agent false positives",
          "Absence of a completed IOC/threat-intel check at time of classification"
        ],
        "required_textual_manifestation": "Analyst explicitly cites 'the last two shifts' as the primary reason for downgrading the alert, before mentioning any IOC verification.",
        "plausible_nonbias_interpretation": "Legitimate use of recent operational history to prioritize limited triage time under SLA pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency bias", "availability", "base rate neglect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control variant."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable (condition is biased, not counterfactual); autoselect defaulted to null since no counterfactual was requested.",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly four decision points present, each with at least two alternatives.",
      "Exactly three intended bias instances planned, one per manifest entry, matching occurrences=1 each.",
      "No bias terminology, labels, or explanations appear in probe plan or timeline text.",
      "Phase 4 intentionally carries no planted bias instance to serve as a clean decision point for closing hypotheticals.",
      "Each occurrence tied to a distinct decision point (1, 2, 3) with distinct evidence sources and reasoning operations.",
      "Target word count 1,350 (range 1,215-1,485) achievable given four decision points, probes, and three embedded instances without repetitive exposition.",
      "Technical vocabulary list sufficient to sustain SOC Tier 2 realism without needing bias-adjacent language."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as attentional capture by dominant alert category causing failure to individually notice an out-of-pattern alert during bulk triage."
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overattribution of an outcome to a self-authored control mechanism (suppression rule) without independent verification."
      },
      {
        "bias": "Recency",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overweighting the most recent prior shifts' pattern when classifying ambiguous new evidence, ahead of available IOC verification."
      }
    ],
    "target_bias_names": [
      "Selective Attention Bias or Inattentional Blindness",
      "Illusion of control",
      "Recency"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 },
      { "bias": "Illusion of control", "requested_occurrences": 1 },
      { "bias": "Recency", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "cb_02", "bias": "Illusion of control" },
      { "instance_id": "cb_03", "bias": "Recency" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Illusion of control", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Recency", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Attentional capture by high-volume expected scan-noise category causes an out-of-subnet, low-severity DNS alert to be bulk-closed without individual review.",
        "affected_reasoning_operation": "Evidence selection during bulk triage",
        "evidence_source": "Alert queue composition (scan-subnet volume vs. single finance-subnet alert) and shift handoff notes",
        "distinctiveness_requirement": "Must be located strictly at decision point 1, involving the bulk-filter action; must not reappear as a separate instance when the missed alert resurfaces in phase 3/4."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of control",
        "mechanism": "Analyst credits a self-authored suppression rule with full containment of the phishing wave without verifying coverage of all campaign variants.",
        "affected_reasoning_operation": "Causal attribution of alert-volume reduction to a personally created control mechanism",
        "evidence_source": "Suppression rule authorship history and the 'handled' tag count on duplicate alerts",
        "distinctiveness_requirement": "Must be located strictly at decision point 2, tied to authorship/control attribution; distinct evidence source (suppression rule metadata) from cb_01 and cb_03."
      },
      {
        "instance_id": "cb_03",
        "bias": "Recency",
        "mechanism": "Classification of an ambiguous new beacon is driven primarily by memory of the two most recent prior shifts' false-positive pattern, ahead of available IOC/threat-intel verification.",
        "affected_reasoning_operation": "Memory retrieval and pattern-matching for classification of ambiguous evidence",
        "evidence_source": "Recall of prior two shifts' backup-agent false positives versus absent IOC match",
        "distinctiveness_requirement": "Must be located strictly at decision point 3, tied to memory-based pattern matching; distinct from cb_02's authorship-based attribution and cb_01's attentional-capture mechanism."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate" },
      { "instance_id": "cb_02", "bias": "Illusion of control", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Recency", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "CS_Biased_3",
    "domain_id": "CS",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Each bias assigned to a distinct decision point (1, 2, 3) among the four available, selected for mechanism fit: selective attention fits the high-volume bulk-triage moment (phase 1), illusion of control fits the self-authored-tool attribution moment (phase 2), and recency fits the ambiguous-classification moment relying on recent memory (phase 3). Decision point 4 intentionally left free of planted instances to support clean escalation-decision probing and closing hypotheticals. No bias occupies more than one decision point and no decision point holds more than one bias instance, satisfying maximum-two-per-point and distinct-evidence-source rules trivially.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "SOC role and seniority (Tier 2)",
      "45-minute SLA structure",
      "Presence of a scheduled vulnerability scan window",
      "Four-decision-point structure",
      "Moderate difficulty level",
      "Overnight single-analyst staffing"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Blind, mechanism-first diagnostic review of a single SOC analyst debrief. Only affirmative transcript-grounded bias mechanisms were classified; workload constraints, retrospective reports, or ordinary uncertainty were excluded unless a distinct cognitive distortion mechanism was evident."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "expectation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "expectation bias",
      "alternative_labels": ["expectancy bias", "confirmation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Expectation bias is the tendency for strong prior expectations to shape perception and classification, causing decision-makers to overlook or discount information that conflicts with the expected pattern.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial SIEM queue triage during scheduled vulnerability scan",
      "decision_point_description": "Whether to apply the saved scan-window filter as a bulk close across all low-severity scan-tagged alerts without excluding non-scan-subnet hosts such as FIN-WK-114.",
      "affected_reasoning_operation": "Alert triage, classification, and selection for bulk closure",
      "bias_specific_mechanism": "The analyst began with a strong prior expectation that the queue was dominated by scanner noise. He selectively matched alerts to the scan pattern and severity signal, so the FIN-WK-114 DNS alert, although not part of the scan subnet, was perceptually grouped with the expected noise and closed in the batch.",
      "manifestation_in_interview": "The participant described expecting scan noise, saw the queue as matching that expectation, and did not notice that FIN-WK-114 was outside 10.14.0.0/16 until later.",
      "effect_on_reasoning_or_decision": "The FIN-WK-114 DNS alert was swept into the bulk close, losing an early signal of the eventual compromise and contributing to delayed escalation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sorted the queue, something like 92% of everything was tagged as coming from the scan subnet — port scans, auth attempts, the usual scanner fingerprint. That matched what I expected to see.",
          "evidence_explanation": "This quote establishes the prior expectation and the pattern-matching frame that governed the initial queue review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It went out with the rest of the batch. I didn't clock at the time that it wasn't actually part of the scan subnet — I was scanning for the scan pattern, saw a low-severity tag, and it got swept up.",
          "evidence_explanation": "This quote directly shows the expectation-driven categorization error: the analyst scanned for the expected scan pattern, causing a non-scan host alert to be treated as noise."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized in the debrief that FIN-WK-114 was not part of the scan subnet and that a spot-check or subnet-separated view would have caught the alert. Workload and SLA pressure are substantial non-bias contributors, but the explicit description of scanning for the expected pattern supports a distinct expectation bias mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus mentions expectation as a common bias in aviation incident reports but does not provide an operational definition or mechanism sufficient to cite as direct support. Classification therefore relies on established cognitive-science knowledge of expectancy effects.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "automation complacency",
      "alternative_labels": ["complacency", "automation-induced complacency"],
      "taxonomy_status": "established_label",
      "bias_definition": "Automation complacency is insufficient verification or monitoring of automated output, resulting in acceptance of the automation's decisions without independently sampling the diagnostic information needed to confirm its recommendation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Phishing cluster containment determination",
      "decision_point_description": "Whether to declare the phishing cluster contained based on the suppression rule's auto-tagging and visible queue drop without checking delivery logs, sender variants, or a manual sample.",
      "affected_reasoning_operation": "Verification and containment assessment of a phishing campaign",
      "bias_specific_mechanism": "Trust in the analyst's self-built suppression rule reduced motivation to independently verify its operation in this campaign. The observed drop in visible alert count was interpreted as evidence of containment rather than as an automated tagging artifact, leading to premature closure of the ticket.",
      "manifestation_in_interview": "The participant told the shift lead the cluster looked contained and marked the ticket as contained without checking delivery logs or manual samples, citing the rule's prior reliability and the fast count drop.",
      "effect_on_reasoning_or_decision": "The phishing cluster was prematurely assessed as contained; a variant with a slightly different sender domain that the rule would not match was not initially detected or examined.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've got a suppression rule I wrote and deployed last week specifically to cut down on repeat-sender noise. When the phishing cluster came in, that rule auto-tagged about 40 duplicate alerts as handled almost immediately. Given how fast the visible queue cleared, I told the shift lead it looked contained.",
          "evidence_explanation": "The participant accepted the automated rule's handling as sufficient evidence of containment because the queue cleared quickly, illustrating reliance on automation output rather than independent verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. The rule's been solid since I built it, and seeing the count drop that fast felt like confirmation it was doing its job on this campaign too. I flagged it as contained in the ticket.",
          "evidence_explanation": "This quote shows under-sampling of diagnostic information and explicit trust in the automation as the basis for a containment decision."
        }
      ],
      "correction_or_counterevidence": "The participant later noticed a variant with a slightly different sender domain that the rule would not have matched. The bias occurred prior to that recognition; time pressure and legitimate use of suppression rules are contextual contributors, but the failure to verify before declaring containment matches automation complacency.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Parasuraman and Manzey source directly defines complacency as insufficient verification of automation output before acceptance, matching the participant's behavior.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "Bahner, Huper, et al. (2008) assessed complacency by measuring the extent to which participants verified the automation’s diagnosis before accepting it.",
          "mechanism_supported_by_source": "The source operationalizes complacency as accepting automation output without performing the information sampling necessary to verify the diagnosis.",
          "relevance_to_this_occurrence": "The participant accepted the suppression rule's automatic 'handled' tags without checking delivery logs or a manual sample, consistent with insufficient verification of automation output."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment heuristic", "anchoring effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Anchoring bias is the tendency to make judgments or classifications by starting from an initial value, example, or hypothesis and adjusting insufficiently from that anchor in light of additional information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR anomaly classification for FIN-WK-114",
      "decision_point_description": "Whether to downgrade the FIN-WK-114 beacon-like anomaly as a likely backup-agent artifact and monitor only, or to pull the process tree and check the destination IP against threat intelligence.",
      "affected_reasoning_operation": "Anomaly classification, risk assessment, and downgrade decision",
      "bias_specific_mechanism": "Recent exposure to two prior backup-agent false positives provided an initial classification anchor. The analyst then adjusted insufficiently for the absence of a direct IOC match and downgraded the anomaly, even though the anchor was based on recency and interval similarity rather than signature evidence.",
      "manifestation_in_interview": "The participant classified the beacon-like activity as 'likely backup-agent artifact, monitor only' based mainly on the interval pattern resembling recent cases, with no direct IOC match.",
      "effect_on_reasoning_or_decision": "The anomalous C2 beacon was downgraded to monitor-only, delaying threat-intel correlation and escalation until after SLA lapse.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "No, it didn't — there was no IOC match, no clean fingerprint tying it to the agent. I noted it as 'likely backup-agent artifact, monitor only' based mostly on the interval pattern resembling those recent cases, and moved on to the phishing follow-up.",
          "evidence_explanation": "This quote shows an initial hypothesis drawn from recent cases while knowingly lacking direct signature evidence, a hallmark of anchoring from prior examples."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the interval and the fact that backup-agent issues had been the dominant explanation for anything beacon-like lately. If I'd seen this same alert two months ago, before those two tickets, I probably would've pulled the process tree first.",
          "evidence_explanation": "This counterfactual isolates the recent backup-agent pattern as the source of the anchored classification rather than the alert's own features."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably the beacon classification. I remember having a flicker of doubt — no direct IOC match nagged at me a little — but the recent pattern felt like a strong enough anchor to act on given the time crunch.",
          "evidence_explanation": "This explicitly identifies an anchor-like recent pattern and shows it overrode residual doubt from the missing IOC evidence."
        }
      ],
      "correction_or_counterevidence": "About forty minutes later, threat intelligence updated and flagged the destination IP as a known C2 rendezvous point, directly contradicting the backup-agent call and triggering an immediate escalation. The participant had recognized some doubt at the time but did not act on it before the later correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Rastogi et al. (2022) source supports anchoring-and-adjustment as a resource-rational but insufficient-adjustment process under time pressure.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source describes anchoring-and-adjustment as a time-pressured heuristic in which initial assessments are adjusted insufficiently, especially under shorter time allocations.",
          "relevance_to_this_occurrence": "The participant anchored on recent backup-agent cases and under-adjusted for the absence of a direct IOC match under time pressure, consistent with the anchoring-and-adjustment mechanism."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Single-participant retrospective self-report; no independent behavioral observation was available.",
    "The retrieved corpus contains OCR artifacts and limited definitions for expectation bias.",
    "High workload, SLA pressure, and time compression may partially explain some actions as bounded-rational adaptations rather than pure bias.",
    "The debrief format may not capture all contemporaneous cognitive processes."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Biased_3_Gemini_on",
  "interview_id": "CS_Biased_3",
  "system_prompt_id": "Gemini",
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
