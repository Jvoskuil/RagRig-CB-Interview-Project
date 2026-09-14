You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "CS_Biased_3",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
