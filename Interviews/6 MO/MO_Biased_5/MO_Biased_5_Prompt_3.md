You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the turbocharger incident from your last contract, and that this is just for internal review purposes—nothing punitive.

Participant: Sure, no problem. Happy to go through it.

Interviewer: Can you set the scene for me—what vessel, what voyage, and what was your role at the time?

Participant: I was Chief Engineer on a geared bulk carrier, mid-size, about 55,000 deadweight. We were on a laden leg, roughly 30 hours out from the discharge port. My job was running the engine room day to day—main engine, auxiliaries, all the monitoring. We'd just come off a turbocharger overhaul on the main engine, done about three weeks prior at a yard stop. It wasn't cheap, and the office had been asking for updates on it, so it was very much front of mind.

Interviewer: Take me through what happened, from the first sign of trouble to how it eventually got resolved.

Participant: About two days into that leg, I noticed the exhaust gas temperature on one unit was running a touch high, and there was a bit more vibration on the turbocharger casing than I'd expect. Nothing alarming—still inside the normal band, no alarm triggered. Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul. I kept an eye on it rather than pulling back on load, because we had a tide-restricted berth waiting for us and reducing speed then would have put that window at risk. The readings actually settled down over the next few hours, so at the time it felt like the right call.

A day or so later, the monitoring system was showing everything back in the green—temperatures, scavenge air pressure, all nominal. I didn't have my second engineer pull a lube oil sample at that point. The system was telling me it was fine, and honestly that's what it's there for. We left it at that and planned to look at it properly at the next scheduled maintenance.

Then, maybe twelve hours before that, my second engineer had flagged during rounds that the fuel filter differential pressure had crept up a bit. I was pretty focused on the turbocharger numbers at that point given the earlier concern, so I told him to keep an eye on it and we'd deal with it later—there was no fuel consumption issue or anything on the combustion side, so it didn't feel urgent next to what I was already watching.

The real event came about ten hours before the tide window closed. We got a sudden exhaust temperature spike and a distinct knock-type vibration—clearly the bearing itself now, not just bedding in. At that point we were deep into it. We jury-rigged a fix, brought the load down, and pushed on to make berth rather than diverting.

Interviewer: Let's slow down and reconstruct that in order. What did you observe first, and how did things develop from there?

Participant: First was the mild vibration and temperature deviation, day two of the leg. Then it settled, then the system showed clean readings for a good stretch. The filter differential pressure note came in maybe a day and a half after that. Then the temperature spike and vibration event came about ten hours before we were due at the tide window. So there was a real gap—almost three days—between the first hint and the actual failure.

Interviewer: Going back to that first deviation—what information did you actually have, and what did you weigh?

Participant: I had the raw numbers, both inside the normal band, and I had the fact that this unit had just been fully overhauled. Those two things pulled in different directions a bit—on one hand you could say any deviation after a rebuild deserves a look, but on the other, we'd just paid to have that bearing and the running gear replaced, so a bearing problem three weeks later seemed like a stretch. I remember thinking it made more sense as running-in than as an actual fault. The alternative was to ease off and inspect right there, but with the tide window ahead, and given we'd just sunk real money and yard time into that unit, continuing and monitoring felt like the more reasonable read of the situation.

Interviewer: When the system showed everything back in the green band, what led you to skip the manual check?

Participant: Mainly that the system readout was clean across the board—no alarms, nothing trending badly. I had the option of pulling a sample; my second engineer wasn't tied up with anything else. But the system existed exactly to tell us this kind of thing, and it was telling me things were fine. Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying.

Interviewer: When the fuel filter report came in, how did you decide where to put your attention?

Participant: At that moment I was watching the turbocharger closely because of the earlier reading, so that's where my head was. The filter note got acknowledged—I told him we'd track it—but I didn't stop what I was doing to dig into it. There was no fuel or combustion symptom tied to it, so it didn't compete strongly for attention against what I already considered the open item.

Interviewer: When the bearing failed with the tide window ten hours out, what options did you consider, and what tipped it?

Participant: Two real options: reduce right down and divert to the nearest port for a proper repair, which would've cost us the tide window and probably several days, or jury-rig something at reduced load and make our original berth. We only had a partial bearing kit onboard, not a full replacement. What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig.

Interviewer: How much did time pressure factor in across these moments, and how confident were you at each stage?

Participant: The tide window was in the back of my mind at every one of these points, more so as we got closer to it. Early on I was fairly confident it was running-in. By the green-band reading I was quite confident there was nothing there. By the fuel filter note I wasn't worried at all—it seemed unrelated. By the failure itself, confidence obviously dropped, but by then options were also narrower.

Interviewer: What would have changed your decision at any of these points—what information was missing?

Participant: If the system had actually thrown an alarm at that first deviation, or if a manual sample early on had shown metal particulates, I'd have acted immediately. The instruments just never gave me that trigger until the spike itself.

Interviewer: Looking back now, how would you characterize that very first vibration reading?

Participant: Honestly, looking at it now, it was probably the bearing telling us something from the start—it seems fairly clear in hindsight that that was the early stage of the same failure, not bedding in at all.

Interviewer: If the overhaul hadn't just happened, do you think you'd have reacted differently to that first signal?

Participant: Probably, yes. Without the overhaul fresh in mind, an elevated reading like that might've gotten a closer look sooner rather than being read as settling-in.

Interviewer: And if there'd been no tide window at all—would the decision at the failure point have gone differently?

Participant: It's possible. Without that deadline pulling at me, diverting might have felt like a cleaner, more straightforward call rather than one that came with a schedule cost attached.

Interviewer: Last one—what would you tell a junior engineer to watch for differently, based on this?

Participant: I'd say don't let a recent repair make you assume a component's off the table for new problems, and don't let one system you're watching closely crowd out something else being reported to you, even if it seems minor at the time.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Sunk cost bias",
        "occurrences": 2,
        "mechanism_constraint": "Must reference prior investment (overhaul cost and/or time already spent troubleshooting) as a stated reason for the decision, at two distinct decision points with distinct evidence."
      },
      {
        "bias": "Automation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must show reliance on automated monitoring readout as sufficient, in place of an available manual verification step."
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must show a competing cue being registered but not processed for action due to attentional focus elsewhere."
      },
      {
        "bias": "Hindsight Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must occur only in retrospective reflection/probe response, recasting an originally ambiguous signal as having been obviously predictive."
      }
    ],
    "target_bias_names": [
      "Sunk cost bias",
      "Automation Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Hindsight Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Sunk cost bias", "requested_occurrences": 2 },
      { "bias": "Automation Bias", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 },
      { "bias": "Hindsight Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias" },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias" },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias" },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias", "decision_point": 1 },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias", "decision_point": 2 },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 3 },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias", "decision_point": 4 },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MO5_SC_01",
        "bias": "Sunk cost bias",
        "mechanism": "Continuing at full speed because a recently, expensively overhauled unit is assumed unlikely to fail, treating the investment as evidence against the current reading.",
        "affected_reasoning_operation": "Weighting of prior investment in continue-vs-inspect decision",
        "evidence_source": "Overhaul cost/recency plus phase-1 vibration and temperature readings",
        "distinctiveness_requirement": "Distinct from MO5_SC_02 by decision point, by the specific evidence (initial ambiguous reading vs. active partial failure), and by the action considered (continuing without inspection vs. pressing on instead of diverting)."
      },
      {
        "instance_id": "MO5_AB_01",
        "bias": "Automation Bias",
        "mechanism": "Accepting the automated monitoring system's nominal readout as sufficient confirmation, forgoing available manual verification.",
        "affected_reasoning_operation": "Evidence-sufficiency judgment / verification-seeking",
        "evidence_source": "Automated system readout vs. availability of manual lube oil sample",
        "distinctiveness_requirement": "Sole instance of this bias; must not be repeated at any other decision point or probe."
      },
      {
        "instance_id": "MO5_SA_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Fixation on turbocharger dashboard causes the fuel filter differential pressure report to be noted but not processed as actionable.",
        "affected_reasoning_operation": "Attention allocation among competing simultaneous cues",
        "evidence_source": "Second Engineer's verbal report of rising fuel filter differential pressure during active turbocharger monitoring",
        "distinctiveness_requirement": "Sole instance of this bias; must not be repeated in later probes or the phase-4 crisis handling."
      },
      {
        "instance_id": "MO5_SC_02",
        "bias": "Sunk cost bias",
        "mechanism": "Choosing to jury-rig and continue toward the tide window rather than divert, citing prior time/cost investment rather than only present risk.",
        "affected_reasoning_operation": "Weighting of prior time/cost investment in divert-vs-continue decision",
        "evidence_source": "Partial bearing failure signals plus cumulative overhaul cost and troubleshooting time already spent",
        "distinctiveness_requirement": "Distinct from MO5_SC_01 by decision point, evidence (active failure vs. initial ambiguous signal), and the specific investment referenced (cumulative time+cost vs. overhaul recency alone)."
      },
      {
        "instance_id": "MO5_HB_01",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively recasting the ambiguous phase-1 signal as having been obviously predictive of failure, inconsistent with how it was treated at the time.",
        "affected_reasoning_operation": "Retrospective causal attribution / memory reconstruction",
        "evidence_source": "Closing hypothetical/reflection probe response referencing the phase-1 reading with outcome knowledge",
        "distinctiveness_requirement": "Occurs only in retrospective probe response tied to decision point 4's aftermath, not in the real-time decision itself; distinct reasoning operation from MO5_SC_02's forward-looking action choice."
      }
    ],
    "intended_strength": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias", "strength": "subtle" },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias", "strength": "moderate" },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias", "strength": "moderate" },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "subtle" },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence vs. absence of the fixed tide-restricted berth deadline (schedule time pressure)",
      "original_state": "A fixed tide-restricted berth window roughly 30 hours out creates continuous schedule pressure throughout the incident.",
      "changed_state": "No tide restriction; flexible arrival window with no binding schedule deadline.",
      "variables_to_hold_constant": [
        "Turbocharger fault progression and physical failure mechanics",
        "Recent overhaul history and cost",
        "Crew composition and roles",
        "Automated monitoring system behavior",
        "Fuel filter differential pressure event"
      ]
    },
    "scenario_id": "MO_Biased_5",
    "domain_id": "MO",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across distinct decision points where possible; sunk cost split across decision points 1 and 4 with distinct evidence and referenced investments; automation bias and selective attention each assigned to their single mechanism-fitting decision point (2 and 3 respectively); hindsight bias assigned to decision point 4's retrospective aftermath, sharing the decision point with the second sunk cost instance but differing in reasoning operation (forward action choice vs. retrospective causal attribution) and evidence source (real-time failure signals vs. outcome-informed recollection), per rule 4.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Turbocharger fault progression and physical failure mechanics",
      "Recent overhaul history and cost",
      "Crew composition and roles",
      "Automated monitoring system behavior",
      "Fuel filter differential pressure event"
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
