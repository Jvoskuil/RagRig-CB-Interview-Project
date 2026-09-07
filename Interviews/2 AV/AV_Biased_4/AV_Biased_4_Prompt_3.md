You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. As we discussed, this is a confidential debrief for training research purposes — I'll ask about a specific check ride, and I'd like you to walk me through what happened as concretely as you can. Nothing here goes into your personnel file. Sound okay?

Participant: Sure, happy to talk through it. It was a Line Check, OPC cycle, on one of our senior widebody captains — guy's got probably twenty-two thousand hours, most of it on type. I was in the jump seat as the TRE.

Interviewer: What was the flight supposed to accomplish, and what was your role exactly?

Participant: Standard revenue flight, but I'm there to evaluate his technical handling and CRM for his recurrent check. First officer was PM. My job is to observe, grade, and intervene only if safety requires it.

Interviewer: Take me through what actually happened, from the start.

Participant: Before we even got to the airplane, I saw the tech log had two previous write-ups — ADIRU 2 miscompare, both times it cleared on its own, maintenance found nothing conclusive, and it came back MEL'd as okay to fly. So going in, I already had that context. We did the walk-around, briefed, nothing unusual. Departure was normal. Climbing out through about FL250, we got a brief ADIRU disagree indication on the EICAS — flickered for maybe ten seconds and went away. No checklist triggered automatically, so it wasn't like the system was demanding we do anything. Then in cruise, it came back, but this time it showed up as a disagreement between the captain's and first officer's airspeed and altitude tapes. That's more attention-getting because now you've got two primary displays disagreeing with each other, not just an internal comparator flag. The captain worked through it — cross-checked against the standby instruments, talked the FO through what he was seeing, and the indications came back together within a couple minutes. Rest of the flight was uneventful. Normal approach, normal landing.

Interviewer: And afterward?

Participant: I wrote up my report. Graded the captain's overall performance. A colleague of mine, another TRE, looked at the write-up informally and asked whether I'd been a little quick to wave things off given the fault's history. I pushed back on that. Then a few days later maintenance found an intermittent connector fault in the ADIRU wiring bay — that's likely what caused all three episodes. So there was an actual physical problem the whole time, it just wasn't consistent enough to nail down on the ground.

Interviewer: Let's go back to that pre-departure moment. What went through your mind when you saw the tech log entries?

Participant: Two prior flights, same fault, both cleared themselves, maintenance had already looked at it and released it under the MEL. At that point it's a documented, dispositioned item. My read was, this is a known quantity — it's shown its behavior twice now, and both times it resolved without anything happening. So there wasn't a strong pull toward digging further.

Interviewer: Did you consider asking for another maintenance look before departure?

Participant: Briefly, yeah. But honestly the calculus was, it's already been checked twice, we're on schedule, full airplane. Asking for another inspection with no new symptom to point to would have been hard to justify to ops control. The history itself felt like the justification for going.

Interviewer: What would have had to be different on paper for you to hold the flight?

Participant: If it had shown up as a hard fault instead of self-clearing, or if maintenance had flagged something specific rather than "checked, no fault found," that changes it completely. A pattern of it clearing every time made it feel like a non-issue rather than something still unresolved.

Interviewer: Move to the climb, when the flag flickered again. Walk me through that moment specifically.

Participant: We're climbing, disagree flag pops up, I look at it, and it's gone in about ten seconds. No checklist auto-triggered. My first thought honestly was, there it is again, exactly like the tech log said — comes, sits for a few seconds, clears. I said to the captain, keep the climb going, this is the same thing we saw on the ground reports.

Interviewer: What alternative did you weigh at that point?

Participant: Leveling off and running the full non-normal procedure, get maintenance control on the radio. I considered it, but with no checklist trigger and a pattern that had already shown itself as self-resolving twice before, pausing the climb over a ten-second flicker felt like overreacting.

Interviewer: How confident were you in that read at the time?

Participant: Pretty confident, honestly. I felt like I'd basically already seen this movie — two data points on the ground, one in the air, all matching. In hindsight, three brief occurrences isn't really enough to know what an intermittent wiring fault is going to do next, but at the time it felt like a clear pattern rather than a limited sample.

Interviewer: Let's talk about cruise, when the airspeed and altitude displays actually disagreed between the two pilots' instruments. What did you observe the captain do, and how did you evaluate it?

Participant: He didn't reach for the QRH procedure in order. He went straight to the standby instruments from memory, cross-checked visually, talked the FO through it calmly, and it resolved. The first officer didn't object or suggest going to the checklist either.

Interviewer: How did you grade that?

Participant: I graded it satisfactory. He's got the experience — a guy with that many hours on type, flying that calmly under a real instrument disagreement, that tells you something. I didn't go back afterward and verify step-by-step that every QRH item had technically been hit in sequence. His outcome and his composure were the strongest signal I had.

Interviewer: If a first-year captain had handled it the identical way, would you have graded it the same?

Participant: Probably not as generously, no. I'd have wanted to see the checklist worked in order regardless of how it turned out. With him, the track record does a lot of the work.

Interviewer: Last one — the conversation with your colleague afterward. He suggested your calls that day might have been shaped by the crew's clean history. How did you respond to that?

Participant: I told him I didn't think that applied to me. I've got a structured process I follow on every check, and a long run of check rides without an incident. I said that kind of thing is more of a risk for someone earlier in their check-airman career, someone still building their pattern recognition. For me, I trust the process I've built.

Interviewer: Is there anything that would change your mind about that day, looking back?

Participant: If the connector fault had failed completely instead of intermittently, sure, that reframes everything. But it didn't — it stayed borderline the whole flight, which is exactly why none of this proves anything one way or the other about the calls I made.

Interviewer: Last question. If you ran this exact flight again with exactly the same information you had at the time, what would you do differently?

Participant: Probably not much, if I'm honest. Maybe I'd log the climb flicker more formally. But the information I had pointed the same direction every time I looked at it.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Bias Blind Spot",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dismissal of a peer's specific critique of the TRE's own judgment, contrasted with willingness to attribute similar susceptibility to other check airmen."
      },
      {
        "bias": "Normalcy Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dispatch-acceptance reasoning based on prior self-clearing fault history rather than new diagnostic confirmation."
      },
      {
        "bias": "Experience Bias or Trusting expert intuition",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as grading a nonstandard procedural deviation as satisfactory primarily on the basis of the performer's seniority/experience rather than independent verification."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as stated high confidence in predicting fault behavior from a small, self-selected pattern of past observations."
      }
    ],
    "target_bias_names": [
      "Bias Blind Spot",
      "Normalcy Bias",
      "Experience Bias or Trusting expert intuition",
      "Illusion of validity"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bias Blind Spot", "requested_occurrences": 1 },
      { "bias": "Normalcy Bias", "requested_occurrences": 1 },
      { "bias": "Experience Bias or Trusting expert intuition", "requested_occurrences": 1 },
      { "bias": "Illusion of validity", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Normalcy Bias" },
      { "instance_id": "cb_02", "bias": "Illusion of validity" },
      { "instance_id": "cb_03", "bias": "Experience Bias or Trusting expert intuition" },
      { "instance_id": "cb_04", "bias": "Bias Blind Spot" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Normalcy Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Illusion of validity", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Experience Bias or Trusting expert intuition", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Bias Blind Spot", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Normalcy Bias",
        "mechanism": "Treats repeated self-clearing of an ADIRU fault as proof of continued safety absent new diagnostic confirmation, used to justify accepting the aircraft at dispatch.",
        "affected_reasoning_operation": "Risk assessment / dispatch-acceptance judgment",
        "evidence_source": "Tech log history of two prior self-clearing occurrences plus MEL sign-off",
        "distinctiveness_requirement": "Must be tied specifically to the pre-departure dispatch decision, not to the in-flight fault recurrence in cb_02."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of validity",
        "mechanism": "Expresses unwarranted confidence in predicting the fault's future behavior from a brief, small-sample pattern rather than validated diagnostic data.",
        "affected_reasoning_operation": "Predictive judgment about fault trajectory to justify continuing climb",
        "evidence_source": "Transient EICAS ADIRU disagree flag during climb, no checklist trigger",
        "distinctiveness_requirement": "Must center on predictive confidence in a specific in-flight moment, distinct from the dispatch-history reasoning in cb_01 and the evaluative grading in cb_03."
      },
      {
        "instance_id": "cb_03",
        "bias": "Experience Bias or Trusting expert intuition",
        "mechanism": "Substitutes captain's seniority/demeanor for independent procedural verification when grading a nonstandard checklist deviation.",
        "affected_reasoning_operation": "Evaluative grading of crew performance against procedural standard",
        "evidence_source": "Captain's out-of-sequence QRH handling and stated experience level",
        "distinctiveness_requirement": "Must be an evaluative/grading act tied to the captain's actions, distinct from the TRE's own predictive or self-assessment reasoning in cb_02 and cb_04."
      },
      {
        "instance_id": "cb_04",
        "bias": "Bias Blind Spot",
        "mechanism": "Dismisses a peer's specific critique of the TRE's own judgment while affirming that other check airmen could be susceptible to the same influence.",
        "affected_reasoning_operation": "Self-assessment of personal evaluative objectivity in response to external feedback",
        "evidence_source": "Peer TRE's informal comment during report writing plus TRE's stated track record",
        "distinctiveness_requirement": "Must be a post-flight self-referential reflection, distinct from the in-flight operational judgments in cb_01-cb_03."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Normalcy Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Illusion of validity", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Experience Bias or Trusting expert intuition", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Bias Blind Spot", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_4",
    "domain_id": "AV",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One instance per named bias assigned to a distinct decision point (DP1-Normalcy Bias, DP2-Illusion of validity, DP3-Experience Bias, DP4-Bias Blind Spot), chosen for mechanism fit: dispatch-history reasoning at DP1, in-flight predictive confidence at DP2, evaluative grading of another's action at DP3, and post-flight self-referential reflection at DP4. No bias shares a decision point with another occurrence of itself, satisfying spread and distinctiveness rules.",
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
