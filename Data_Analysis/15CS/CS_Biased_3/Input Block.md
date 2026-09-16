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
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_p1",
        "speaker": "Participant",
        "segment_type": "decision_point",
        "raw_interview_anchor": "Initial queue triage: the analyst bulk-closes the low-severity batch and later says the FIN-WK-114 alert was swept up while scanning for the scan pattern.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "Dominant scan-noise volume captures attention and causes the out-of-subnet finance alert to be processed as part of the bulk batch without individual notice."
      },
      {
        "segment_id": "seg_p2",
        "speaker": "Participant",
        "segment_type": "decision_point",
        "raw_interview_anchor": "Phishing containment: the analyst relies on the self-authored suppression rule and the rapid count drop, without checking delivery logs or a manual sample.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "The analyst overattributes apparent containment to a personally authored suppression rule without independent verification of full campaign coverage."
      },
      {
        "segment_id": "seg_p3",
        "speaker": "Participant",
        "segment_type": "decision_point",
        "raw_interview_anchor": "Beacon classification: the analyst downgrades FIN-WK-114 mainly because the interval resembles backup-agent false positives from the previous two shifts, despite no direct IOC match.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "Recent prior-shift cases are weighted disproportionately ahead of available IOC or threat-intelligence verification when classifying ambiguous new evidence."
      },
      {
        "segment_id": "seg_p4",
        "speaker": "Participant",
        "segment_type": "decision_point_negative",
        "raw_interview_anchor": "After the threat-intel update and SLA breach, the analyst escalates immediately to IR while the shift lead is unavailable.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Phase 4 is intentionally unplanted and serves as a clean escalation decision point."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
