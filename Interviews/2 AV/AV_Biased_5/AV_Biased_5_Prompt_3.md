You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a maintenance decision-making review, and that we can reference the tail number and event details generically without naming crew.

Participant: That's fine, go ahead.

Interviewer: Great. Can you tell me your role and how you came into this event?

Participant: I'm the Director of Maintenance at our base station. I oversee line maintenance sign-offs, RTS certifications, and I'm the one who ultimately owns whether an aircraft goes back into the schedule. This one landed on my desk because it kept coming back.

Interviewer: Walk me through what the issue looked like when you first became aware of it.

Participant: We had a Hydraulic System B caution light show up on one of our E175s—momentary, cleared itself, crew wrote it up. Maintenance ran the BITE test, came back clean, no fault found. Classic CND. It happened three times over about two weeks. Each time, no fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL. The aircraft kept flying its line.

Interviewer: What did you make of that pattern at the time?

Participant: Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times. We had the holiday peak coming up and needed the airframe in rotation, so grounding it for an open-ended isolation hunt on a CND item felt like overkill at that point.

Interviewer: Did the increasing duration register as significant to you?

Participant: I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it.

Interviewer: What happened next?

Participant: Next flight day, it came back a fourth time, and this one ran about twelve seconds—longer than anything before—and the crew also noted a brief speed brake anomaly on the same leg. That's when my senior hydraulics engineer came to me and wanted to pull the aircraft and run the full fault isolation procedure out of the FIM.

Interviewer: What did you decide at that point, and how did you get there?

Participant: While we were talking about it, our OEM field rep happened to be at the hangar working a different tail. I flagged him down and asked what he thought. He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.

Interviewer: How did your engineer take that?

Participant: He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.

Interviewer: What information did you weigh most heavily there, and what didn't you dig into?

Participant: Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal. We reset the BITE, flew it two cycles clean, and I figured that confirmed we'd made the right call.

Interviewer: What came after that?

Participant: A few days later, during an unrelated task, one of the techs was near the hydraulic pump and noticed some residue around the seal. Small amount, hadn't been documented before. That was new—nothing like that had shown up in any of the earlier CND checks.

Interviewer: What did that change for you?

Participant: It told us there might be an actual mechanical source rather than just a sensor quirk. At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job.

Interviewer: Did the amount of work already done factor into that choice?

Participant: I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.

Interviewer: After the seal replacement, what did you see?

Participant: Leak check passed on the ground, static test showed no residue. Clean.

Interviewer: What happened at the final sign-off?

Participant: We needed the aircraft that afternoon for the holiday schedule, and we didn't have a test-flight crew available same-day. Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved.

Interviewer: Given the aircraft's history—three CND events and the earlier reset that didn't fully explain the seal residue—how sure were you that this was actually fixed?

Participant: Pretty sure, honestly. The ground tests were clean and that's normally what we'd rely on for a leak-related repair. I didn't have a test flight to back it up, but I didn't see a reason to hold the airplane past that.

Interviewer: If you'd had a test-flight crew available that day, would that have changed your certainty?

Participant: It would've been a nice extra data point, but I don't think it would've changed my decision to release it.

Interviewer: Looking back across the whole event, is there a point where, with the same information you had then, you'd make a different call?

Participant: Maybe the fourth event—the twelve-second one with the speed brake anomaly. If I'd leaned more toward my engineer's read there instead of the OEM rep's, we might have caught the seal issue earlier instead of a few days later.

Interviewer: If the OEM rep hadn't been on-site that day, what do you think you'd have done instead?

Participant: Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction.

Interviewer: Last one—if the seal residue had turned up before you'd started the component swaps, would the escalation decision have gone differently?

Participant: Probably, yeah. Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Optimism Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Authority Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Sunk Cost Fallacy", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Representativeness Heuristic", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Overconfidence Bias", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Optimism Bias",
      "Authority Bias",
      "Sunk Cost Fallacy",
      "Representativeness Heuristic",
      "Overconfidence Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Optimism Bias", "requested_occurrences": 1 },
      { "bias": "Authority Bias", "requested_occurrences": 1 },
      { "bias": "Sunk Cost Fallacy", "requested_occurrences": 1 },
      { "bias": "Representativeness Heuristic", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "ob_01", "bias": "Optimism Bias" },
      { "instance_id": "ab_01", "bias": "Authority Bias" },
      { "instance_id": "rh_01", "bias": "Representativeness Heuristic" },
      { "instance_id": "scf_01", "bias": "Sunk Cost Fallacy" },
      { "instance_id": "ocb_01", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "ob_01", "bias": "Optimism Bias", "decision_point": 1 },
      { "instance_id": "ab_01", "bias": "Authority Bias", "decision_point": 2 },
      { "instance_id": "rh_01", "bias": "Representativeness Heuristic", "decision_point": 2 },
      { "instance_id": "scf_01", "bias": "Sunk Cost Fallacy", "decision_point": 3 },
      { "instance_id": "ocb_01", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ob_01",
        "bias": "Optimism Bias",
        "mechanism": "Projects a benign trajectory from a worsening-duration CND pattern, favoring continued dispatch over isolation",
        "affected_reasoning_operation": "Risk/trend projection",
        "evidence_source": "Three CND write-ups with increasing light duration",
        "distinctiveness_requirement": "Only instance tied to trend projection at decision point 1; must not repeat at other points"
      },
      {
        "instance_id": "ab_01",
        "bias": "Authority Bias",
        "mechanism": "Overweights informal OEM rep opinion over senior engineer's formal procedural request based on rep's perceived status/affiliation",
        "affected_reasoning_operation": "Weighting of competing expert recommendations",
        "evidence_source": "OEM rep's verbal, informal assessment",
        "distinctiveness_requirement": "Must be evidenced via deference to rep specifically, distinct from rh_01's case-matching evidence"
      },
      {
        "instance_id": "rh_01",
        "bias": "Representativeness Heuristic",
        "mechanism": "Infers same root cause/fix from superficial symptom similarity to a prior case without checking dissimilar underlying facts",
        "affected_reasoning_operation": "Case-pattern matching",
        "evidence_source": "Recalled prior in-house case file",
        "distinctiveness_requirement": "Must be evidenced via case-recall/pattern-matching, distinct from ab_01's deference-to-person evidence, even though co-located at decision point 2"
      },
      {
        "instance_id": "scf_01",
        "bias": "Sunk Cost Fallacy",
        "mechanism": "Continues incremental repair plan due to hours/parts already invested rather than updating fully on new leak evidence",
        "affected_reasoning_operation": "Cost-based justification vs. evidence updating",
        "evidence_source": "14 labor hours and replaced components already committed",
        "distinctiveness_requirement": "Sole instance tied to past-investment justification at decision point 3"
      },
      {
        "instance_id": "ocb_01",
        "bias": "Overconfidence Bias",
        "mechanism": "Expresses certainty in fix exceeding what ground-only, non-flight-verified evidence supports",
        "affected_reasoning_operation": "Confidence calibration against evidence strength",
        "evidence_source": "Ground leak check and static test results only, no test flight",
        "distinctiveness_requirement": "Sole instance tied to final RTS certification confidence at decision point 4"
      }
    ],
    "intended_strength": [
      { "instance_id": "ob_01", "bias": "Optimism Bias", "strength": "subtle" },
      { "instance_id": "ab_01", "bias": "Authority Bias", "strength": "moderate" },
      { "instance_id": "rh_01", "bias": "Representativeness Heuristic", "strength": "moderate" },
      { "instance_id": "scf_01", "bias": "Sunk Cost Fallacy", "strength": "subtle" },
      { "instance_id": "ocb_01", "bias": "Overconfidence Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_5",
    "domain_id": "AV",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points by mechanism fit and narrative realism; decision point 2 hosts two distinct biases (Authority Bias, Representativeness Heuristic) each with a separate evidence source (informal OEM rep statement vs. recalled prior case file) per rule 4 of allocation guidance; no decision point contains two occurrences of the same bias.",
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
