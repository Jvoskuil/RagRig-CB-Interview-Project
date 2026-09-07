You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. Just to confirm, this is a voluntary cognitive task analysis debrief—we're reconstructing your decision-making during a specific fire support mission, not evaluating performance for any board or investigation. You can decline any question. Comfortable proceeding?

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Great. Can you describe your role and the mission?

Participant: I was the FSO attached to the company during a daylight clearing operation. We had an enemy 82mm mortar team that had been harassing our forward positions for about two days, and intel flagged a possible staging compound near a village on the objective's north edge. My job was coordinating mortars, then CAS, then artillery, to clear both threats before the company crossed the line of departure. Objective was straightforward—suppress the mortar team, clear the compound, keep it clean for friendlies and the village.

Interviewer: What made this mission nonroutine?

Participant: Timeline was tight—we had about thirty minutes before the assault window closed, ammo for the 81s was limited since we'd already used a chunk of it earlier that morning, and comms between me and FSCC kept dropping in and out. Plus the compound was close enough to friendly squads that anything there was going to be danger-close. And the only real-time picture we had on the compound was one ISR feed, no second source.

Interviewer: Walk me through the sequence as it happened.

Participant: First mission was against the mortar position with the 81s. Fired an adjustment round, it landed short. Fired a second one, still short. Section chief checked the gun-line data once, said no fault found. Around that time, I also had two conflicting reports on where the staging activity actually was—our battalion JTAC had one grid, and the partner-force liaison next to us had a grid about three hundred meters off. Then CAS checked in for the compound piece, and finally we had that ISR cue on the compound itself right before the artillery mission.

Interviewer: Let's take these one at a time. Start with the mortar adjustment rounds.

Participant: Right, so two rounds down, both short. Section chief ran through the data once and didn't find anything wrong. At that point I had a decision—stop and have them do a full re-lay, checking level, deflection, everything from scratch, or fire the next adjustment round and see what happens.

Interviewer: What did you decide, and why?

Participant: I told them to fire again. Two shorts in a row, statistically we were about due to get one on target, and a full re-lay eats time we didn't have with the window closing.

Interviewer: What did that third round do?

Participant: Also landed short. Turned out later there was a leveling error on the gun that had nothing to do with the first two rounds—separate issue entirely. We caught it on the fourth check.

Interviewer: If the section chief had reported a confirmed fault after the first miss, would your third-round call have gone differently?

Participant: Probably, yeah. If there'd been a flagged fault I'd have stopped immediately for the recheck. Without one, I read the pattern as random scatter that would sort itself out on its own.

Interviewer: Let's move to the grid discrepancy. What information did you have?

Participant: Battalion JTAC—same battalion as me—called in Grid A for the staging activity. Almost at the same time, the partner-force liaison on our flank called Grid B, about three hundred meters away, similar confidence level in both reports, nothing that clearly outranked the other on paper.

Interviewer: How did you resolve that?

Participant: I went with Grid A, the JTAC's grid. It came through our own FSCC net, format I was used to, and honestly it's the source I'd worked with the whole deployment. The partner-force report came through a different relay and took longer to cross-check.

Interviewer: Did you request verification on Grid B?

Participant: Not before we acted on Grid A. Follow-on recon actually picked up some indicators near Grid B too, so it wasn't nothing—we just didn't chase it down at the time.

Interviewer: If the partner-force liaison's report had come through your own channel instead, do you think you'd have weighted it the same as Grid A?

Participant: Honestly, probably would've given it more credit. There's something about hearing it through your own net that makes it feel more solid, even if I can't point to a real reason the information itself was better.

Interviewer: Let's talk about the CAS run. What was the situation?

Participant: Pilot was on station, ready for a danger-close run supporting the compound clearance. We'd run several strikes with this same squadron over the deployment, all clean, standard margins, no issues. This time the friendly squad's position put us tighter than our usual margin, and we'd had a couple of comms dropouts with the lead squad in the minutes before.

Interviewer: What were your options?

Participant: Widen the margin, which meant delaying and possibly missing the window, or hold the comms until we got a stable check, versus just clearing it with the tighter margin we had.

Interviewer: What did you choose?

Participant: I cleared it hot with the tighter margin. This squadron had been reliable every time, so I expected it to go the same way.

Interviewer: What happened with comms during the final attack heading confirmation?

Participant: Dropped out again for about ten seconds. We got it back before the pilot needed the final call, so it worked out, but it was closer than I'd like on reflection.

Interviewer: If this had been the squadron's first-ever danger-close run with you, would you have set the same margin?

Participant: No. I'd have wanted the wider margin and a cleaner comms check. The history with them is what made the tighter margin feel acceptable.

Interviewer: Last decision point—the artillery mission on the compound.

Participant: Right before we committed the 155s, the ISR feed flagged one cue, "possible enemy activity" at the compound. That sector had been quiet the whole deployment, mostly normal village pattern-of-life, and that particular sensor had a track record of throwing false hits in that terrain.

Interviewer: What were the alternatives?

Participant: Get a second source to confirm before firing, given how quiet that area had been, or approve the mission off the one cue since the window was closing.

Interviewer: What did you decide?

Participant: I approved it off the single cue. We were inside the last few minutes before the assault, and the cue matched what we were looking for, so I went with it.

Interviewer: What did the post-strike assessment show?

Participant: Mixed. Some indicators of prior enemy presence, but also signs it might've been unoccupied by the time we fired. Inconclusive, honestly.

Interviewer: If the sector had a recent history of confirmed enemy activity, would that one cue have been enough on its own?

Participant: Probably would've felt the same either way at the time—I was focused on the cue itself, not really running the sector's track record against it.

Interviewer: Looking back across all four decisions, where do you think time pressure affected you most?

Participant: Probably the mortar rounds and the compound call—those felt the most rushed. The grid call and the CAS run felt more like judgment calls based on what I knew about the sources and the squadron.

Interviewer: Anything you'd do differently?

Participant: Maybe push harder for that re-lay check early, and get a second look at the compound cue. But given the clock we were working against, I think most FSOs would've made similar calls that day.

Interviewer: That's helpful. Thanks for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Gamblers Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must involve reasoning about an upcoming independent artillery/mortar round based on prior round outcomes"
      },
      {
        "bias": "Ingroup Preference bias or In-group bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve differential weighting of two evidence sources based on unit affiliation rather than evidentiary quality"
      },
      {
        "bias": "Optimism bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve underestimating risk of a specific mission element based on a recent favorable track record"
      },
      {
        "bias": "Base-rate neglect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve disregarding sector-level or sensor-level prior probability in favor of a single specific cue"
      }
    ],
    "target_bias_names": [
      "Gamblers Fallacy",
      "Ingroup Preference bias or In-group bias",
      "Optimism bias",
      "Base-rate neglect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Gamblers Fallacy", "requested_occurrences": 1 },
      { "bias": "Ingroup Preference bias or In-group bias", "requested_occurrences": 1 },
      { "bias": "Optimism bias", "requested_occurrences": 1 },
      { "bias": "Base-rate neglect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy" },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias" },
      { "instance_id": "ob_01", "bias": "Optimism bias" },
      { "instance_id": "brn_01", "bias": "Base-rate neglect" }
    ],
    "intended_decision_points": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy", "decision_point": 1 },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias", "decision_point": 2 },
      { "instance_id": "ob_01", "bias": "Optimism bias", "decision_point": 3 },
      { "instance_id": "brn_01", "bias": "Base-rate neglect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "gf_01",
        "bias": "Gamblers Fallacy",
        "mechanism": "Belief that an independent fire-mission outcome is 'due' to succeed after consecutive misses, rather than treating each round independently",
        "affected_reasoning_operation": "Probabilistic forecasting of an independent event",
        "evidence_source": "Sequence of two prior adjustment-round outcomes",
        "distinctiveness_requirement": "Only bias-relevant instance tied to sequential round outcomes; must not overlap with any other instance's evidence"
      },
      {
        "instance_id": "ig_01",
        "bias": "Ingroup Preference bias or In-group bias",
        "mechanism": "Preferential trust in a report because it originates from the observer's own unit/service rather than on evidentiary merit",
        "affected_reasoning_operation": "Comparative weighting of two competing target-location reports",
        "evidence_source": "Battalion JTAC report vs. partner-force liaison report",
        "distinctiveness_requirement": "Only instance involving cross-unit evidence comparison; distinct evidence source and decision point from gf_01"
      },
      {
        "instance_id": "ob_01",
        "bias": "Optimism bias",
        "mechanism": "Underweighting risk indicators (tight margin, comms dropout) because of a recent favorable track record with the same asset",
        "affected_reasoning_operation": "Forward-looking risk/outcome forecasting for a danger-close CAS run",
        "evidence_source": "Recent squadron strike history plus current margin/comms conditions",
        "distinctiveness_requirement": "Only instance concerning forecast confidence about mission execution risk; independent of ig_01 and brn_01 evidence"
      },
      {
        "instance_id": "brn_01",
        "bias": "Base-rate neglect",
        "mechanism": "Approving action based on one specific-case cue while ignoring known low prior probability of true positives in this sector/sensor combination",
        "affected_reasoning_operation": "Belief updating on target identification given prior probability and single-case evidence",
        "evidence_source": "Sector activity history and sensor false-positive history vs. single sensor cue",
        "distinctiveness_requirement": "Only instance involving prior-probability neglect in target identification; final decision point"
      }
    ],
    "intended_strength": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy", "strength": "subtle" },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias", "strength": "subtle" },
      { "instance_id": "ob_01", "bias": "Optimism bias", "strength": "subtle" },
      { "instance_id": "brn_01", "bias": "Base-rate neglect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Biased_4",
    "domain_id": "MD",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism per rules 1-4; no decision point hosts more than one instance of any bias.",
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
