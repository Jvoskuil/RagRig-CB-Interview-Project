You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for sitting down with me. Just to confirm, you're okay with this being recorded for training analysis, no names attached?

Participant: Yes, that's fine.

Interviewer: Could you give me a quick sense of your background?

Participant: Sixteen years piloting on this river system, mostly deep-draft container and bulk carriers. I've taken vessels the size of the Kalliopi up to Berth 7 probably a hundred times.

Interviewer: Let's talk through this particular transit. What did you know before boarding?

Participant: It was a fully loaded container ship, about 300 meters, drawing 14.2 meters. Port control had sent the passage plan that morning built around the tide table, giving roughly 1.2 meters of under-keel clearance at our planned transit time. That's tight but workable for that stretch under normal conditions. We had a closing tidal window, maybe ninety minutes, two tugs assigned, and wind forecast around 15 knots picking up through the afternoon.

Interviewer: What made this one feel nonroutine?

Participant: A few things stacked up together. A barge was moored tighter to the bend than charted, one of our tugs got delayed at the pilot station, and the wind ended up running hotter than forecast. Individually those are manageable. Together, they meant I was reassessing constantly instead of just running the plan as written.

Interviewer: Walk me through what happened after you boarded.

Participant: I went up to the conning position, confirmed the plan with the master, checked the draft survey again, and we got underway close to schedule. Shortly after, an outbound pilot radioed a fresh echo sounder sweep from near kilometer four, reporting less water than expected, closer to 0.7 meters instead of the 1.2 we'd planned around. Around the same time, VTS mentioned the tide gauge was reading a slower rise than the table predicted.

Interviewer: How did things develop from there?

Participant: Approaching the bend, VTS told us the barge hadn't moved despite requests, so I adjusted our track. Then the wind picked up faster than forecast right as we were down to one tug made fast, with the second still twenty minutes out. Near the berth, a cross-current pushed us off line during final approach, and we corrected with the tugs we had by then.

Interviewer: Let's take these one at a time. Starting with the clearance question after the outbound pilot's report — what were you actually weighing?

Participant: I had the morning tide table figure, and now a fresh sounding plus a tide gauge trend running slower than predicted. I didn't want to just discount either one. I asked the master to run our own echo sounder sweep as we approached that stretch to see what we were actually reading under our own hull, since the outbound vessel's trim and draft weren't identical to ours. That came back closer to the outbound pilot's number than the original table, maybe 0.8 to 0.9 meters once I accounted for our squat at the speed we were making.

Interviewer: So how did that change your plan?

Participant: I cut speed to reduce squat and shifted our track toward the deeper water on the outer edge of that stretch. Combined, cutting speed and hugging the deeper line got our effective margin back to something I was comfortable with, without needing to blow the tidal window with a full delay.

Interviewer: Did you consider just holding the original timing, or delaying instead?

Participant: Both were on the table. Holding the original timing didn't sit right once we had two independent readings pointing the same direction. A full forty-minute delay was the safer extreme, but I judged that speed and track adjustment addressed the actual shortfall without sacrificing the window. It was closer than I like, honestly, maybe a six out of ten on confidence, but it was based on our own numbers, not just the forecast.

Interviewer: Moving to the barge near the bend, what options did you weigh?

Participant: Push VTS harder for an emergency move, slow down and favor the wider side, or hold position until it cleared. I went with slowing and shifting track because waiting would have eaten into the window we'd already tightened up, and pushing VTS wasn't going to move the barge fast enough anyway.

Interviewer: How much time did you have to decide?

Participant: A couple of minutes. Enough to make a deliberate call, not enough to sit and debate it.

Interviewer: Next, the tug situation with rising wind.

Participant: With only one tug fast and the second still well out, and gusts running above forecast, I didn't want to rely purely on the bow thruster given our draft. When I heard a harbor tug not originally assigned was nearby, I requested that one instead of waiting on our delayed second tug. Getting help sooner mattered more than sticking with the original assignment.

Interviewer: Was waiting ever seriously on the table?

Participant: Briefly, yes, but the wind was trending the wrong way, and bringing in help early felt like the safer bet.

Interviewer: And the final approach, with the cross-current?

Participant: By then both tugs were fast. I chose a graduated correction rather than aborting, applying tug and thruster power progressively and watching the response. If that hadn't taken hold quickly, I would have aborted and circled. It ended up tighter to the neighboring berth than I'd like, but within what the berth operator confirmed was workable.

Interviewer: What made continuing feel safer than aborting?

Participant: The initial response to tug power told me we had steerage and margin. That's really the deciding factor in the moment, how she responds to the first correction.

Interviewer: Looking back, if the echo sounder report had reached you before you even left the pilot station, would your approach have changed?

Participant: Possibly less improvisation involved. I'd have built the speed reduction and track shift into the plan from the start rather than adjusting mid-transit. The outcome likely would have been similar, just calculated earlier with more margin to plan around.

Interviewer: If the second tug had arrived on schedule, would the bend or the berthing approach have gone differently?

Participant: The bend, not much, that was about the barge and speed. The berthing correction might have felt less tight, since we'd have had both tugs from the start rather than bringing in a substitute.

Interviewer: Anything you'd have wanted to know sooner?

Participant: I'd have liked our own sounding data earlier rather than relying on someone else's reading first. That's really a sequencing issue, not a judgment one.

Interviewer: What would you tell a less experienced pilot about a transit like this?

Participant: Don't treat any single number, old or new, as final. Cross-check it against your own instruments when the margin is tight enough to matter, and build your track and speed decisions around what you can verify yourself.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Anchoring Bias",
        "occurrences": 0,
        "mechanism_constraint": "No intentional anchoring-bias manifestation permitted; decision point 1 must show genuine integration of new evidence into a revised judgment."
      }
    ],
    "target_bias_names": [
      "Anchoring Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Anchoring Bias",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MO_Biased_1",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MO_Vocab_Control_1",
    "domain_id": "MO",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control condition requires zero intended bias instances across all decision points, so no allocation was performed.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Four-decision-point narrative structure and sequence",
      "Stakeholder roster and role functions",
      "Operational constraints (tidal window, draft, tug delay, wind forecast, barge encroachment, cross-current)",
      "Difficulty level (challenging)",
      "Emotional tone and pacing",
      "Target word count and probe plan categories"
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
