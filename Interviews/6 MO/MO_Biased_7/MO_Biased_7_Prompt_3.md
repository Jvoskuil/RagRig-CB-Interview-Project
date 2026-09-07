You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. As explained, this is a confidential debrief to understand the reasoning behind decisions during the cargo transfer alongside the platform last month — not a disciplinary review. Anything you share helps refine our procedures. Are you comfortable proceeding?

Participant: Yes, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by describing your role on that job?

Participant: I was the DPO on watch, running station-keeping in DP2 mode while we did a scheduled cargo transfer — deck cargo and some bulk — to the platform. Normally that's a fairly routine job. We hold position off the leg, crane operator on the platform takes the lifts off our deck, and we just maintain the watch circle until it's done.

Interviewer: And what made this particular job different, if anything?

Participant: Weather was closing in faster than the forecast suggested first thing that morning. We had maybe a four-hour window before significant wave height would push past the platform crane's operating limit. So there was a bit more time pressure than usual, but nothing outside normal parameters when we started.

Interviewer: Take me through what happened, from approach onward.

Participant: On final approach, I noticed a discrepancy between the HPR and one of the DGPS units — about 1.8 meters. DGPS1 and DGPS2 were agreeing closely with each other, and the system had auto-weighted those two into the primary solution, showing green across the board. HPR didn't have any maintenance flag against it, but given the other two were lined up, I read the HPR number as the odd one out and carried on with the approach. We got alongside, started the transfer, cargo went smoothly for the first several lifts. About halfway through — call it 55% of the load transferred — Thruster 3 threw a yellow caution, reduced power availability. Consequence analysis still showed adequate capability, so I kept going in the same configuration. Superintendent called in around then too, just a reminder about the transit schedule afterward. Later, on the second-to-last lift, there was a wind shift that changed the footprint plot recommendation. I was heads-down on the crane boom position at that point, watching the load come across, and I didn't clock the footprint change until the Master mentioned the vessel's attitude had shifted. Checked afterward — the indicator had been sitting there on the secondary screen the whole time. Then for the last lift, OIM asked if we could finish or wanted to stand off. I told him we were maybe eight to ten minutes out, so we pushed on. Partway through that final lift our separation from the leg closed up more than I expected, and we ended up suspending early and backing off to a safer distance. No contact, no loss of position beyond the watch circle, but closer than I'd have liked.

Interviewer: Let's reconstruct that in order. What were you actually monitoring at each stage?

Participant: Early on, reference systems and the DP status page — standard for closing distance. Once we were alongside and lifting, my attention split between the crane display, thruster status, and periodic checks of the environmental trend. As the job went on, honestly, more of my attention shifted toward the crane display than the DP overview, especially in that last third.

Interviewer: Let's go back to the reference discrepancy. Walk me through your decision process there.

Participant: DGPS1 and DGPS2 agreed within normal tolerance, HPR was off by 1.8 meters, no fault logged on it. Two out of three lined up, system auto-selected that pair and showed green, so I proceeded on that basis.

Interviewer: Did you do anything to independently check which reference was actually correct, beyond the system's selection?

Participant: Not really — the pairing agreed and the status was green, so I didn't dig into the raw HPR trace further at that point. In hindsight the offset was a multipath effect from being close to the structure, so HPR wasn't actually wrong, but at the time the two-out-of-three read as good enough.

Interviewer: What would have made you look harder at that discrepancy?

Participant: If the DGPS units had disagreed with each other too, I'd have stopped and manually cross-checked before closing in. It was really the agreement between the two that settled it for me.

Interviewer: Now the thruster caution at the halfway point — what went into staying in the same mode?

Participant: The consequence analysis still showed us within capability, so procedurally there wasn't a hard requirement to change anything. We'd already gotten through a bit more than half the cargo, and the weather window was closing, so stopping to reassess felt like it would cost us more than it bought us at that stage.

Interviewer: Did you consider switching to a more conservative setup — tightening the watch circle, adjusting reference weighting — rather than continuing exactly as before?

Participant: Not actively, no. It wasn't red, so it didn't really register as something requiring a change in how we were running things. We'd been in that configuration all shift and it had been fine.

Interviewer: Move to the final lift and the footprint change. What was pulling your attention at that point?

Participant: The crane boom, almost entirely. That's the highest-consequence thing to watch during an active lift — if the load swings or the boom's position goes wrong, that's an immediate hazard. The footprint indicator is a visual cue only, no audible alarm tied to it, so it's easy for it to sit there unnoticed if you're not specifically glancing over.

Interviewer: What would have changed that — would delegating the environmental watch to your co-operator have helped?

Participant: Probably, yes. We didn't explicitly split that responsibility during the lift. In hindsight that would have been the more robust setup.

Interviewer: Last one — the OIM's question about finishing the final lift. What did you weigh in your answer?

Participant: Mainly the time — eight to ten minutes to complete it, and the equipment status hadn't escalated past caution level. So I told him we were good to finish rather than framing it around how much margin we actually had left, which by that point had narrowed more than I'd tracked.

Interviewer: Looking back at that sequence overall, do you think there were earlier indications of how close things got at the end?

Participant: Looking back, yes — the reference offset and the thruster caution together were quietly eating into our margin the whole time, and honestly it feels like it should have been fairly obvious that was building toward something. In the moment, though, neither one individually crossed a threshold that flagged it.

Interviewer: If you were advising a newer DPO going into a similar job, what would you tell them to watch for?

Participant: Don't let a green status or a majority agreement between references close the door on checking the outlier. And separate out who's watching the environmental picture versus the load, especially late in a job when you're tired and task-focused.

Interviewer: Anything you'd do differently if this came up again?

Participant: I'd probably reassess capability actively at the first caution rather than just confirming it was still within limits, and frame those late-stage go/no-go calls around remaining margin rather than remaining minutes. Otherwise the job itself was manageable — we just let a few small things ride longer than we should have.

Interviewer: That's really helpful detail. Thank you for walking through it so thoroughly.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as reliance on agreeing DGPS pair to dismiss conflicting HPR reading without independent cross-check"},
      {"bias": "Automation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as deference to DP system's auto-weighted GREEN status over independent manual interpretation of raw discrepancy data"},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 1, "mechanism_constraint": "Must manifest as failure to notice a visually-available footprint/environmental cue due to sustained focus on the crane display"},
      {"bias": "Hindsight Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as retrospective overstatement of foreseeability of the Phase 1 reference discrepancy during closing reflection"},
      {"bias": "Sunk cost bias", "occurrences": 1, "mechanism_constraint": "Must manifest as justification for continuing based on cargo/time already invested rather than forward-looking capability reassessment"},
      {"bias": "Status Quo Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as default preservation of current DP mode/pace without active comparison of mode-change alternatives"},
      {"bias": "Framing Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as decision rationale framed around remaining time rather than narrowing safety margin"}
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Automation Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Hindsight Bias",
      "Sunk cost bias",
      "Status Quo Bias",
      "Framing Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Confirmation Bias", "requested_occurrences": 1},
      {"bias": "Automation Bias", "requested_occurrences": 1},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1},
      {"bias": "Hindsight Bias", "requested_occurrences": 1},
      {"bias": "Sunk cost bias", "requested_occurrences": 1},
      {"bias": "Status Quo Bias", "requested_occurrences": 1},
      {"bias": "Framing Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias"},
      {"instance_id": "ab_01", "bias": "Automation Bias"},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness"},
      {"instance_id": "hb_01", "bias": "Hindsight Bias"},
      {"instance_id": "sc_01", "bias": "Sunk cost bias"},
      {"instance_id": "sq_01", "bias": "Status Quo Bias"},
      {"instance_id": "fb_01", "bias": "Framing Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1},
      {"instance_id": "ab_01", "bias": "Automation Bias", "decision_point": 1},
      {"instance_id": "hb_01", "bias": "Hindsight Bias", "decision_point": 1},
      {"instance_id": "sc_01", "bias": "Sunk cost bias", "decision_point": 2},
      {"instance_id": "sq_01", "bias": "Status Quo Bias", "decision_point": 2},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 3},
      {"instance_id": "fb_01", "bias": "Framing Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective reliance on the two agreeing GPS references to confirm the preferred position estimate, dismissing the conflicting HPR reading as the outlier without independent verification",
        "affected_reasoning_operation": "evidence-selection and weighting during reference validation",
        "evidence_source": "Reference system comparison data (DGPS1, DGPS2, HPR) at Phase 1",
        "distinctiveness_requirement": "Must be distinguished from ab_01 by focusing on the DPO's own evidence-selection reasoning rather than on deference to the automated system status indicator"
      },
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "mechanism": "Deference to the DP system's automated reference-weighting and GREEN status as sufficient justification, bypassing independent manual interpretation of the underlying raw data",
        "affected_reasoning_operation": "trust calibration between automated output and manual judgment",
        "evidence_source": "DP system status indicator and auto-weighting output at Phase 1",
        "distinctiveness_requirement": "Must be distinguished from cb_01 by centering on trust in the system's output itself, not on the DPO's own selective interpretation of raw discrepancy data"
      },
      {
        "instance_id": "hb_01",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospective overstatement, during closing reflection, of how foreseeable the Phase 1 discrepancy's significance was, exceeding what the contemporaneous alert status supported",
        "affected_reasoning_operation": "retrospective foreseeability judgment elicited by closing hypothetical probe",
        "evidence_source": "DPO's closing-probe response compared against the contemporaneous Phase 1 alert status",
        "distinctiveness_requirement": "Must occur only in the closing reflective probe tied to the Phase 1 event, not as a repeated commentary elsewhere in the interview"
      },
      {
        "instance_id": "sc_01",
        "bias": "Sunk cost bias",
        "mechanism": "Justification for continuing the transfer that foregrounds cargo and time already invested rather than a forward-looking reassessment of DP capability given the new thruster caution",
        "affected_reasoning_operation": "cost-weighting in the continue-versus-suspend judgment",
        "evidence_source": "Phase 2 cargo-completion status and elapsed operation time",
        "distinctiveness_requirement": "Must be distinguished from sq_01 by explicit reference to invested cost/effort as the stated reason, rather than default preservation of the operating mode without any stated cost rationale"
      },
      {
        "instance_id": "sq_01",
        "bias": "Status Quo Bias",
        "mechanism": "Retention of the existing DP Auto configuration and operating pace after the thruster caution, without active comparison of a more conservative mode as an alternative",
        "affected_reasoning_operation": "option-generation and default-preservation when a new caution condition arises",
        "evidence_source": "Phase 2 mode/configuration status and absence of considered alternatives in DPO's account",
        "distinctiveness_requirement": "Must be distinguished from sc_01 by the absence of an invested-cost rationale; the defining feature is default retention of configuration, not a cost-based justification"
      },
      {
        "instance_id": "sa_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Sustained attentional focus on the crane boom display causes a visually-available footprint/wind-shift indicator change to go unnoticed until pointed out externally",
        "affected_reasoning_operation": "perceptual monitoring and attentional allocation across competing displays",
        "evidence_source": "Phase 3 footprint plot indicator timeline versus DPO's attention account",
        "distinctiveness_requirement": "Unique to Phase 3; concerns failure to perceive available information, not failure to act on already-perceived information"
      },
      {
        "instance_id": "fb_01",
        "bias": "Framing Bias",
        "mechanism": "The continue/suspend rationale communicated to the OIM is framed around remaining completion time rather than the narrowing safety margin, despite both being available",
        "affected_reasoning_operation": "decision framing in the final continue-versus-suspend response to a direct query",
        "evidence_source": "Phase 4 DPO response to the OIM's query, compared against available margin data",
        "distinctiveness_requirement": "Unique to Phase 4; concerns how the decision is framed/communicated, not the underlying cost or default-preservation reasoning captured by sc_01/sq_01"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle"},
      {"instance_id": "ab_01", "bias": "Automation Bias", "strength": "subtle"},
      {"instance_id": "hb_01", "bias": "Hindsight Bias", "strength": "subtle"},
      {"instance_id": "sc_01", "bias": "Sunk cost bias", "strength": "subtle"},
      {"instance_id": "sq_01", "bias": "Status Quo Bias", "strength": "subtle"},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate"},
      {"instance_id": "fb_01", "bias": "Framing Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "N/A",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MO_Biased_7",
    "domain_id": "MO",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across distinct decision points by mechanism fit and narrative realism: Phase 1 (reference discrepancy) hosts confirmation bias, automation bias, and hindsight bias as three distinct reasoning operations (evidence-selection, automation trust, retrospective foreseeability); Phase 2 (continue transfer under thruster caution) hosts sunk cost and status quo as distinct rationale types (cost-based vs. default-based); Phase 3 (final lift) hosts selective attention/inattentional blindness as the sole attentional-mechanism fit; Phase 4 (final continue/suspend decision) hosts framing bias as the sole communication-framing fit. No bias exceeds two occurrences at a single decision point, and no two co-located instances share an evidence source or reasoning operation.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
