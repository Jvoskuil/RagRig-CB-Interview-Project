You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. This is a debrief interview, not a review — nothing here goes into your personnel file, and you can decline to answer anything. Is that okay?

Participant: Yeah, that's fine. I figured you'd want to talk about the Riverside call eventually.

Interviewer: Exactly. Can you start by telling me your role that shift and what you knew before you got there?

Participant: I was IC, first-due battalion. Dispatch had it as a small trash fire, exterior, rear alley of an industrial unit — auto parts store up front, warehouse space in the back. No hazmat flag, no history on the address. Two engines and a truck were coming with me.

Interviewer: What was your objective once you rolled up?

Participant: Same as always — knock it down fast, keep it from extending into the structure, make sure nobody's inside. Straightforward call, or so it looked.

Interviewer: Walk me through what actually happened, start to finish.

Participant: We pulled up and there was a moderate smoke column, more than I'd expect from a trash fire, but honestly that's not unusual — dumpster fires with pallets or packaging can push a decent amount of smoke. Dispatch had said small and exterior, so I put my first-in crew on a quick knockdown line rather than sending someone around back first. We got water on it within a couple minutes. Once the crew got to the rear of the building, that's when things changed — heavier smoke, a chemical smell, and they found a stack of drums against the rear wall, a couple of them with fire exposure. So now I've got a fire that started as trash-can-sized turning into a possible hazmat exposure.

Interviewer: What did you do at that point?

Participant: Called for a hazmat tech and requested a second alarm for staffing. We shifted into more of a hybrid posture — fire attack continuing, but treating the rear as an isolation zone until we knew what we were dealing with.

Interviewer: Let's go back to that very first call — committing the line before checking the rear. What went into that?

Participant: Dispatch said small trash fire, and that's usually reliable enough to act on immediately — you don't want to sit on a fire waiting for a full 360 when speed matters. The smoke was heavier than I'd expect for that call type, I noticed it, but I didn't want to lose time doing a full walk-around on what was described as a contained exterior fire.

Interviewer: What would have made you hold back and do the 360 first?

Participant: If dispatch had said anything about chemical storage back there, I'd have gone defensive immediately and skipped the quick-attack option entirely. Without that flag, I went with what was called in.

Interviewer: Was time pressure a factor?

Participant: Some. Every minute a small fire sits, it can grow, so there's always pressure to commit. But if I'm honest, the call type is what I leaned on more than the visual.

Interviewer: Once the hazmat tech got there, how did you go about identifying what was in those drums?

Participant: There was a placard on one drum, partially legible — rust and fire damage had eaten some of the numbers. The tech's read was that it lined up with a common solvent, the kind sold in the retail section up front, which made sense to us — warehouse storing overflow of what they sell. The night manager was on scene too, pretty shaken, and he said something like "no, that's not what's back there, it's something different," but he was contradicting himself on other details too — couldn't remember which door led where, that kind of thing.

Interviewer: How did that statement factor into your PPE and agent decisions?

Participant: We didn't weight it heavily. He was rattled, giving inconsistent answers generally, and the placard read supported what we already expected to find. We moved forward with PPE and foam suited for that solvent class.

Interviewer: Did you look for a second placard or manifest confirmation before committing?

Participant: We didn't stop operations to go find one. In hindsight, there was a second drum with an intact placard a few feet away, and it showed a different hazard class. We found the manifest fragment later, in a file cabinet, and it didn't match either.

Interviewer: What would have changed your read at the time?

Participant: A clean placard would've done it immediately. The occupant's statement alone — I probably needed more than that, given how confused he was on everything else.

Interviewer: Let's talk about the perimeter. How did that get set?

Participant: The first-arriving officer put an initial isolation line at 150 meters, standard distance for an unknown chemical exposure situation. By the time I was thinking hard about it, mutual aid units were already staging off that line, and the battalion chief who came in was operating off it too — didn't question it, just built his sector around it.

Interviewer: Did you have any reservations about that distance?

Participant: A little. Wind had started shifting toward the residential block, and I remember thinking we might want to push it out, but everybody was already set up on 150, command posts, staging, hose lays — recalculating and moving all of that would've been a real disruption, and nobody else seemed to be flagging it as a problem. So I left it.

Interviewer: What happened with the wind?

Participant: It fully shifted about twenty minutes later, confirmed by a weather update, and then air monitoring near the edge of our line came back close to the action threshold. We had to push the perimeter out on short notice, which is never clean — reshuffling people, moving apparatus.

Interviewer: If you'd recalculated independently earlier, do you think it would've gone differently?

Participant: Possibly. I had the wind information sooner than we acted on it.

Interviewer: Last decision point — the search. Tell me about that.

Participant: Interior team had cleared about ninety percent of the structure. The last piece was a small storage room right next to the drum stack, and by then the crew had been in there over half an hour, visibly gassed. The chemical ID still wasn't nailed down, and drum integrity in that room was unknown.

Interviewer: What was the call?

Participant: The battalion chief said something like, "we're not sending them back in there just to walk away from ninety percent of a search we already did — that's the whole building except one closet." Framed that way, pulling out felt like throwing away the work. So I authorized the crew to go finish it.

Interviewer: What did you find?

Participant: Room was empty. But one of the drums in there was leaking slightly, so that crew got more exposure time near an unresolved hazard than I'd have liked, in a room we didn't need to enter for life safety, since it turned out to be unoccupied.

Interviewer: Looking back at that whole call — does anything stand out as something that should have been obvious at the time?

Participant: Honestly, yeah. That smoke column at the very start was heavier than a trash fire should produce. I think if I'd trusted that visual over the dispatch description, I'd have sent someone to check the rear before committing the line. It feels like the signs were there from minute one.

Interviewer: What would you tell a newer commander to watch for in a similar situation?

Participant: Don't let the initial call type set your whole picture — cross-check it against what you're actually seeing, especially smoke volume and color. And when a perimeter's already been set by someone else, still run your own numbers if conditions change, because everyone assumes someone else already checked it.

Interviewer: Anything else you want to add?

Participant: Just that none of these calls looked wrong in the moment. It's only once you line them all up afterward that you see where it could've gone differently.

Interviewer: That's helpful. Thanks for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Framing Effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an externally supplied verbal frame (loss/effort framing) from the battalion chief that shifts the IC's risk decision at decision point 4."
      },
      {
        "bias": "Hindsight bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest only during retrospective/closing-hypothetical reflection on decision point 1, not during the real-time decision narration."
      },
      {
        "bias": "Bandwagon effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as deference to converging agreement among multiple other officers/battalion chief at decision point 3, with the IC acknowledging private doubt."
      },
      {
        "bias": "Anchoring Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as reliance on the initial dispatch description at decision point 1, insufficiently adjusted for observed smoke conditions."
      },
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as interpreting ambiguous placard/manifest evidence as supporting the initial solvent guess while discounting the occupant's contradicting statement at decision point 2."
      }
    ],
    "target_bias_names": [
      "Framing Effect",
      "Hindsight bias",
      "Bandwagon effect",
      "Anchoring Bias",
      "Confirmation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Framing Effect", "requested_occurrences": 1 },
      { "bias": "Hindsight bias", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 },
      { "bias": "Confirmation Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "anchor_01", "bias": "Anchoring Bias" },
      { "instance_id": "hindsight_01", "bias": "Hindsight bias" },
      { "instance_id": "confirm_01", "bias": "Confirmation Bias" },
      { "instance_id": "bandwagon_01", "bias": "Bandwagon effect" },
      { "instance_id": "framing_01", "bias": "Framing Effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "anchor_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "hindsight_01", "bias": "Hindsight bias", "decision_point": 1 },
      { "instance_id": "confirm_01", "bias": "Confirmation Bias", "decision_point": 2 },
      { "instance_id": "bandwagon_01", "bias": "Bandwagon effect", "decision_point": 3 },
      { "instance_id": "framing_01", "bias": "Framing Effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "anchor_01",
        "bias": "Anchoring Bias",
        "mechanism": "Strategy commitment insufficiently adjusted away from the initial dispatch-provided call description despite contrary visual cues.",
        "affected_reasoning_operation": "Initial size-up/strategy selection",
        "evidence_source": "Dispatch call description vs. observed smoke column",
        "distinctiveness_requirement": "Occurs at the moment of real-time strategy commitment, before any outcome is known; distinct from hindsight_01, which occurs only during later retrospective reflection on the same decision."
      },
      {
        "instance_id": "hindsight_01",
        "bias": "Hindsight bias",
        "mechanism": "Retrospective overstatement of the foreseeability of escalation, given outcome knowledge unavailable at the time of the original decision.",
        "affected_reasoning_operation": "Retrospective causal/foreseeability judgment",
        "evidence_source": "Closing hypothetical probe response referencing the smoke column and the eventual escalation",
        "distinctiveness_requirement": "Occurs only in retrospective narration/probe response, temporally and operationally separate from the contemporaneous anchoring judgment in anchor_01."
      },
      {
        "instance_id": "confirm_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective interpretation of ambiguous placard/manifest evidence as consistent with the prior solvent assumption, paired with active discounting of a contradicting occupant statement.",
        "affected_reasoning_operation": "Evidence weighting for hazard identification and PPE selection",
        "evidence_source": "Partial placard, manifest fragment, and occupant statement",
        "distinctiveness_requirement": "Sole confirmation-bias instance; tied to decision point 2's evidence-selection act, not repeated elsewhere."
      },
      {
        "instance_id": "bandwagon_01",
        "bias": "Bandwagon effect",
        "mechanism": "Adoption of an already-established perimeter distance because multiple other units and a superior officer are already operating on it, despite unresolved personal doubt.",
        "affected_reasoning_operation": "Perimeter/isolation-distance decision under peer convergence",
        "evidence_source": "Existing 150-meter perimeter and multi-unit operational alignment on it",
        "distinctiveness_requirement": "Sole bandwagon instance; tied specifically to decision point 3's social-convergence dynamic."
      },
      {
        "instance_id": "framing_01",
        "bias": "Framing Effect",
        "mechanism": "Decision outcome shifts based on the battalion chief's effort/loss-oriented verbal framing of the choice, rather than independent evaluation of the underlying chemical risk.",
        "affected_reasoning_operation": "Risk-based go/no-go decision for completing interior search",
        "evidence_source": "Battalion chief's stated framing of the remaining search decision",
        "distinctiveness_requirement": "Sole framing instance; tied to decision point 4's externally supplied frame, distinct from all other decision points."
      }
    ],
    "intended_strength": [
      { "instance_id": "anchor_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "hindsight_01", "bias": "Hindsight bias", "strength": "subtle" },
      { "instance_id": "confirm_01", "bias": "Confirmation Bias", "strength": "moderate" },
      { "instance_id": "bandwagon_01", "bias": "Bandwagon effect", "strength": "moderate" },
      { "instance_id": "framing_01", "bias": "Framing Effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Biased_5",
    "domain_id": "EM",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Automatic assignment per mechanism fit and narrative realism: each bias mapped to the decision point whose evidentiary structure and reasoning operation most plausibly produces that bias in an Incident Commander's retrospective account; anchor_01 and hindsight_01 co-located at decision point 1 only because they represent temporally and operationally distinct reasoning acts (contemporaneous estimation vs. retrospective foreseeability judgment) on the same underlying event, satisfying the distinct-evidence-source/moment requirement for shared decision points.",
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
