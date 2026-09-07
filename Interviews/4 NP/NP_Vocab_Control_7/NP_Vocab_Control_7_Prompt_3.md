You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for sitting down with me. This is for our operations learning file, not a disciplinary review — nothing here goes in your personnel record. Can you tell me your role and background?

Participant: Sure. I'm a process control operator on the catalytic reforming unit, six years on this board, eleven at the refinery overall. I run the DCS console — feed rates, heater duty, reactor temps, that side of things.

Interviewer: Good. Let's start broad — walk me through the incident from the beginning.

Participant: It kicked off right at shift handover, early morning. I'd just settled in when the high-temperature alarm came up on the feed heater outlet. Annunciator lit up, tone sounded. That specific point has been noisy lately — I want to say it tripped something like eleven times over the past month, all logged as instrument drift. But before I acknowledged it, I pulled up the pressure-differential trend on the adjacent screen too, since that's a habit of mine with recurring alarms — you want to see if anything else is moving with it. That trend had been creeping upward for a couple hours, slower and less obvious than the alarm itself, but it was there. Seeing both together made me less comfortable calling it a pure nuisance trip like the others had been, so I got the field operator moving to verify the thermocouple directly rather than just silencing it and continuing on.

Interviewer: What did the field check turn up?

Participant: Confirmed the outlet reading was accurate — not an instrument fault. So now I've got a real alarm and a real trend, and I flagged both for closer attention going into handover.

Interviewer: Walk me through the handover conversation.

Participant: Night operator said things had been "stable, unremarkable" for his last four hours, which matched what I was seeing on the immediate trend. But there was an older note in the board log, a few days back, about a slow upward drift in heater duty that had been flagged and never formally closed out. Rather than just assume it had resolved itself because the recent hours looked clean, I asked him directly whether that drift had actually been corrected or just stopped showing up in the short-term data. He wasn't sure — said it hadn't come up again, but nobody had gone back and verified the root cause.

Interviewer: How did that affect what you did next?

Participant: Production wanted the feed rate bumped to bank throughput before our regeneration window, about six hours out at that point. Given the alarm, the trend, and the unresolved drift note, I didn't just run the standard increase sequence the way I normally would. I ramped it more conservatively than usual and kept a closer eye on outlet temperature through the whole move, rather than treating it as routine.

Interviewer: What happened after that?

Participant: Temperature climbed some, as expected with any increase, but then the field operator called in from a walkdown and mentioned heat shimmer near the firebox — visually distinct, not something he'd normally flag. That raised the stakes.

Interviewer: Let's go back and unpack the first decision — cross-checking the pressure trend before acknowledging. What information did you actually have at that point?

Participant: The alarm, the recent trip history, and that pressure trend, which I made a point of looking at before doing anything else.

Interviewer: What alternatives did you weigh?

Participant: I could've just silenced it like the last eleven times — would've been the fast option. Or dispatched the field guy without checking the trend first. I did a version of both, but in a specific order: checked the trend, saw it didn't look like the earlier isolated trips, then sent the field operator to verify independently rather than assuming it was drift again.

Interviewer: How confident were you in that read at the time?

Participant: Moderately. I wasn't certain something was wrong, but the combination was enough that I didn't want to treat it as routine.

Interviewer: Moving to the feed increase decision — what alternatives were on the table?

Participant: Full delay and a deep dive into the multi-day trend log, looping in the engineer before touching setpoints, or proceeding as planned. I landed somewhere in the middle — proceeded, but modified, with tighter monitoring, specifically because the drift note hadn't been confirmed resolved.

Interviewer: Was that a deliberate call, or did you default to the usual procedure?

Participant: Deliberate. I actually thought about skipping the modification since the last four hours looked fine, but the unresolved log entry bothered me enough that I didn't want to run it exactly like every other routine bump.

Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind?

Participant: The pattern — alarm, temperature climb, shimmer — had some resemblance to a compressor surge event I'd handled about a year and a half ago on a similar unit. There's also a tube-rupture incident from a couple years back that people still bring up in briefings, more dramatic, shut the unit down for weeks. Both crossed my mind. But instead of just running with either, I checked specifically for the vibration signature that had shown up in the surge event — wasn't present here at all. And I asked the engineer whether the current data showed any of the specific markers tied to the tube-rupture failure mode. It didn't match either one cleanly.

Interviewer: What did you do given that neither precedent matched?

Participant: Treated it as its own case. Pulled fresh heater-specific diagnostic data and requested an independent instrument check rather than forcing it into either historical bucket.

Interviewer: Final decision — regeneration window closing in.

Participant: Under ninety minutes left. Temps and pressure still climbing, not at trip setpoints yet. I had a short checklist of standard corrective actions. Full engineer consultation would've eaten twenty to thirty minutes I didn't have to spare, but I also didn't want to just grab the first option on the list.

Interviewer: How did you choose?

Participant: I compared the top two or three checklist options against what the diagnostic data was actually showing, picked the one that matched the pattern best, not just the first one listed, and briefed the engineer by radio while I implemented it so he could flag anything I'd missed in real time.

Interviewer: What was the outcome?

Participant: Stabilized the trend. Later review said the comparison held up reasonably well given the time we had, though the full underlying cause took longer to pin down completely.

Interviewer: If the alarm's history had been clean instead of noisy, would you have handled that first moment differently?

Participant: Probably would've moved even faster to dispatch the field operator — less hesitation about whether it was worth the disruption. The noisy history didn't stop me from checking, but it's fair to say it added a beat of consideration before I did.

Interviewer: What single piece of information, if you'd had it sooner, would have changed the most?

Participant: Confirmation on whether that multi-day drift had genuinely resolved. I was operating on an unanswered question there, and if I'd known definitively either way, the feed-increase decision would've been more clear-cut.

Interviewer: And with more time before the regeneration window?

Participant: I'd have gotten the full engineer consultation rather than the quick radio brief. The comparison I did was reasonable, but a full conversation would've added confidence.

Interviewer: Anything else stand out looking back?

Participant: Just that none of these calls were obvious in the moment. Each one had a real alternative I seriously considered, and I don't think the outcome tells you definitively whether any single step was the right one — it worked out, but there was real uncertainty the whole way through.

Interviewer: That's a good place to stop. Thanks for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Recency Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Habit Intrusion", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Salience Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Similarity Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Bounded Rationality", "occurrences": 0, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Recency Bias",
      "Habit Intrusion",
      "Salience Bias",
      "Similarity Bias",
      "Bounded Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Availability Bias", "requested_occurrences": 0 },
      { "bias": "Recency Bias", "requested_occurrences": 0 },
      { "bias": "Habit Intrusion", "requested_occurrences": 0 },
      { "bias": "Salience Bias", "requested_occurrences": 0 },
      { "bias": "Similarity Bias", "requested_occurrences": 0 },
      { "bias": "Bounded Rationality", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "NP_Biased_7",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Vocab_Control_7",
    "domain_id": "NP",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "No bias occurrences are planned or allocated; this is a vocabulary-matched zero-bias control paired to NP_Biased_7. All four decision points are constructed to mirror the paired scenario's structure, phase order, actors, constraints, and vocabulary, with each decision resolved through active, evidence-weighing reasoning rather than any shortcut mechanism associated with the six target biases.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational setting (catalytic reforming unit control room)",
      "Participant role and seniority",
      "Four-decision-point chronological structure",
      "Stakeholders (night operator, field operator, shift supervisor, process engineer)",
      "Core constraints (6-hour regeneration window, alarm nuisance history, limited field-verification availability, proxy-sensor limitation)",
      "Surface incident facts (alarm, pressure-differential trend, handover report, older drift note, heat shimmer, surge and tube-rupture precedents, closing checklist decision)",
      "Emotional tone and escalating time pressure",
      "Interview format, probe categories, and approximate word count"
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
