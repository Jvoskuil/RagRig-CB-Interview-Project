You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our incident-response learning archive, not a performance review — you can skip anything you're not comfortable discussing. Can you start by stating your role and how long you've been on the Tier 2 triage rotation?

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

Interviewer: That's really helpful, thank you for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
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
  }}}

The hidden specification may include:
- condition;
- exact occurrence manifest;
- target bias names;
- requested occurrence count for each bias;
- planned instance IDs;
- intended decision points;
- intended mechanisms;
- intended strength;
- paired scenario ID;
- counterfactual variable.

Do not treat the hidden specification as evidence that a bias exists. It is a test plan only. The interview text is the evidence. If the specification and interview conflict, report the conflict.

CORE OCCURRENCE DEFINITIONS

A supported occurrence requires all of the following:
1. A distinct decision, inference, evidence-selection act, memory retrieval, prediction, causal attribution, or response to a probe.
2. Evidence showing how the participant processed, weighted, ignored, recalled, interpreted, or updated information.
3. A mechanism consistent with the named bias.
4. Enough context to distinguish the mechanism from a justified domain judgment or an ordinary mistake.

A single occurrence may span several adjacent sentences or one answer turn. Do not count repeated wording about the same reasoning episode as multiple occurrences. Count two occurrences separately only when they have distinct evidence traces, decision moments, evidence sources, or reasoning operations.

VALIDATION TASKS

1. Identify the domain, participant role, operational objective, and incident type.
2. Reconstruct the chronology and identify the decision points. Report whether exactly four decision points are present.
3. For every target bias in the hidden occurrence manifest, independently assess each requested occurrence.
4. Identify additional candidate biases not present in the target manifest.
5. Identify apparent bias cues that should not be labeled as bias.
6. Audit causal claims and counterfactual logic.
7. Evaluate interview quality and control fidelity.
8. Produce precise revision guidance when the interview does not satisfy its occurrence requirements.

FOR EACH REQUESTED OCCURRENCE, CLASSIFY IT AS ONE OF:

- supported: a distinct, textually supported instance is present;
- weak: a possible instance is present, but evidence or mechanism is insufficient;
- absent: no defensible instance is present;
- merged: the intended instance appears to be indistinguishable from another intended occurrence of the
  same bias or from another bias;
- accidental: an unintended instance appears outside the planned occurrence map;
- misclassified: the text supports a different bias or a non-bias explanation instead.

REVISION PRINCIPLES

If a requested occurrence is absent, weak, merged, or misclassified:
- Do not recommend simply repeating the bias label.
- Do not recommend adding an obvious textbook explanation.
- Specify the minimum local narrative or dialogue change needed to make that occurrence independently identifiable.
- Preserve the occupational setting, participant role, chronology, vocabulary, approximate length, and other intended bias occurrences.
- Do not create a new occurrence elsewhere merely to compensate.
- Do not strengthen every occurrence. Revise only the affected occurrence unless the evidence shows a broader structural problem.
- If strengthening the missing occurrence would make the interview too obvious, recommend a subtle evidence change rather than explicit labeling.
- If the requested occurrence is not plausible in the scenario, recommend changing the scenario or the target occurrence manifest rather than forcing implausible behavior.
- For controls, never recommend adding a target bias. If a control contains a defensible bias, recommend neutralizing or replacing the relevant reasoning episode.
- For a counterfactual, preserve the original and changed causal variables and do not introduce a second causal change while repairing bias evidence.

REVISION TYPES

Use one or more of these revision types:
- `none`: occurrence is adequately supported;
- `local_evidence_addition`: add or alter one cue, evidence source, or participant response;
- `local_reasoning_revision`: revise how the participant interprets or weighs evidence;
- `probe_revision`: change an interviewer question or hypothetical so the existing reasoning becomes independently observable;
- `decision_point_revision`: revise one decision point while preserving the rest;
- `remove_accidental_occurrence`: neutralize an unintended additional manifestation;
- `separate_merged_occurrences`: make two intended episodes distinct;
- `reclassify_bias`: change the target label or mechanism because the current label is not defensible;
- `scenario_revision`: revise the occupational situation because the requested occurrence is implausible.

REVISION SPECIFICITY

Each revision recommendation must include:
- the affected instance ID or `additional_candidate`;
- decision point and approximate turn or paragraph location;
- current status;
- evidence currently present, or `none`;
- precise defect;
- recommended revision type;
- minimal change instruction;
- what must remain unchanged;
- a warning against creating additional unintended occurrences;
- expected post-revision status.

Do not rewrite the complete interview. Provide revision instructions only. The generation system will apply
the instructions in a separate revision step.

OUTPUT

Return valid JSON only:
{
  "validator_version": "2.0",
  "interview_id": "...",
  "condition": "biased|vocabulary_control|ambiguous_control|counterfactual|unknown",
  "domain_assessment": {
    "domain": "...",
    "role": "...",
    "objective": "...",
    "incident_type": "...",
    "confidence": 0
  },
  "structure_audit": {
    "estimated_word_count": 0,
    "within_target_range": true,
    "decision_point_count": 0,
    "decision_points": [
      {
        "id": 1,
        "summary": "...",
        "evidence_before": [],
        "evidence_after": [],
        "goals_constraints": [],
        "alternatives": [],
        "decision_basis": "...",
        "time_pressure": "...",
        "uncertainty": "..."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "...",
      "bias": "...",
      "requested_occurrences_for_bias": 0,
      "status": "supported|weak|absent|merged|accidental|misclassified",
      "decision_point": 1,
      "supporting_quote": "...",
      "evidence_location": "...",
      "mechanism": "...",
      "strength": "absent|weak|moderate|strong",
      "confidence": 0,
      "plausible_nonbias_explanation": "...",
      "additional_evidence_needed": "...",
      "revision_needed": true,
      "revision": {
        "revision_type": "none|local_evidence_addition|local_reasoning_revision|probe_revision|decision_point_revision|remove_accidental_occurrence|separate_merged_occurrences|reclassify_bias|scenario_revision",
        "location": "...",
        "current_defect": "...",
        "minimal_change_instruction": "...",
        "preserve": [],
        "avoid_creating": [],
        "expected_post_revision_status": "supported|weak|absent|merged|accidental|misclassified"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "...",
      "requested_count": 0,
      "supported_count": 0,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "...",
      "decision_point": 1,
      "supporting_quote": "...",
      "mechanism": "...",
      "confidence": 0,
      "status": "candidate|supported|weak|rejected",
      "plausible_nonbias_explanation": "...",
      "revision_recommendation": "none|remove_or_neutralize|consider_adding_to_manifest"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "...",
      "location": "...",
      "why_not_bias": "..."
    }
  ],
  "causal_audit": {
    "causal_claims": [],
    "correlation_causation_risks": [],
    "counterfactual_present": false,
    "changed_variable": "...",
    "held_constant": [],
    "causal_coherence": "not_applicable|weak|moderate|strong",
    "explanation": "..."
  },
  "quality_scores": {
    "occupational_realism": 0,
    "cta_fidelity": 0,
    "bias_separability": 0,
    "bias_subtlety": 0,
    "control_fidelity": 0,
    "counterfactual_fidelity": 0,
    "narrative_coherence": 0,
    "naturalness": 0,
    "hidden_label_integrity": 0,
    "overall_quality": 0
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 0,
    "requested_occurrence_total": 0,
    "missing_occurrence_total": 0,
    "accidental_occurrence_total": 0,
    "priority": "none|low|medium|high|reject",
    "recommended_action": "accept|revise|regenerate|reject",
    "global_revision_constraints": [],
    "revision_order": []
  },
  "failure_flags": []
}

COUNTING RULES FOR THE SUMMARY
- `supported_occurrence_total` counts only occurrences with status `supported`.
- `missing_occurrence_total` counts `weak`, `absent`, `merged`, and `misclassified` requested occurrences.
- `accidental_occurrence_total` counts unintended instances that should be removed or separately labeled.
- Set `recommended_action` to `accept` only when all requested occurrences are supported, no unacceptable accidental occurrences exist, and quality is adequate.
- Set it to `revise` when local changes can repair the interview without changing the scenario.
- Set it to `regenerate` when the scenario, decision structure, or several occurrences are fundamentally unsuitable.
- Set it to `reject` for severe incoherence, contaminated controls, or unrepairable causal confounding.

Return JSON only. Do not return a revised interview.
