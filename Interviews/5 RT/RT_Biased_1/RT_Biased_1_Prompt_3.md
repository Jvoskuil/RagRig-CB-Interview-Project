You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. Just to confirm before we start — this is a routine cognitive task analysis interview, not an investigation. Nothing you say here goes into a disciplinary file, and you can decline any question. Comfortable to proceed?

Participant: Yeah, that's fine, happy to go through it.

Interviewer: Great. Can you tell me your role and how long you've been controlling this branch?

Participant: I'm a Rail Traffic Controller, six years on this desk, mostly overnight and weekend turns. I cover the Falcon Bank branch pretty regularly — it's single line, absolute block working, so only one train in the section at a time.

Interviewer: And what's a normal possession handback look like on a section like that?

Participant: Gang foreman calls in on the trackside telephone, confirms the line's clear of personnel and equipment, I log the time, and then it's back to normal working. Nothing unusual about that part.

Interviewer: Walk me through what actually happened that night.

Participant: Handback came through at 23:40, all routine. I had 6M42, a freight, sitting at the entry signal waiting for the road, and 2T19, a passenger service, running about eighteen minutes late further up the line. Objective was simple enough — get 6M42 through Falcon Bank and get 2T19 back on time without anyone sitting in a queue longer than they needed to. Shortly after the handback, the track circuit for the section showed occupied for about four seconds, then cleared. It did that twice in ten minutes. Light rain had just started.

Interviewer: What went through your mind when you saw that?

Participant: Honestly, my first thought was "here we go again." That circuit's had three nuisance trips in the last eight months, all rain or leaf-fall related, all logged. So I looked at it and thought, that's the same signature — short blip, self-clears, no correlation with anything physically on the track. It fit the pattern well enough that I didn't feel I needed to chase it further.

Interviewer: What alternatives did you actually have at that point?

Participant: I could've rung the foreman again on the trackside phone to get him to re-walk it, or got the on-call technician out to test the circuit, or gone to pilotman working as a precaution. All were on the table.

Interviewer: What made you choose to just proceed?

Participant: The pattern, mostly. Three prior trips, same weather trigger, same short duration. It read like the circuit doing its usual thing. Calling the foreman back would've meant holding 6M42 another ten, fifteen minutes for what I was fairly confident was nothing, and pilotman working is even longer than that to arrange. Once I had it slotted into that nuisance-trip bucket in my head, verifying it didn't feel like it was really adding anything — I'd already accounted for it, if that makes sense.

Interviewer: How confident would you say you were, on reflection, that it was genuinely just the nuisance trip and not something else?

Participant: At the time, quite confident — enough that I didn't feel the need to build in a check. Looking back, I suppose I treated it as basically closed rather than just "probably fine but still open." I gave 6M42 the road.

Interviewer: What happened next?

Participant: 6M42 entered the section, and for a few minutes everything was quiet — no more flickers, so it looked like a good call at that point. Then the foreman came back on the radio to do his readback, confirming the gang and equipment were fully clear, but the transmission was garbled by static. I caught "clear" and something like "trolley," but it wasn't a full clean readback.

Interviewer: What were your options there?

Participant: Accept it as good enough since the formal handback had already happened before that call, try to re-raise him for a clean repeat, or ring my supervisor to get a second opinion on whether a partial transmission was adequate.

Interviewer: Which did you go with, and why?

Participant: I logged it as adequate. The handback itself was already formally done and clean at 23:40 — this was just the follow-up readback, and the gang was already moving off to their next job, so re-contacting wasn't straightforward. No rule had actually been broken; the section was already possession-free by the book. It felt like a reasonable judgment call given what I had, not a great one, but reasonable.

Interviewer: Then what?

Participant: Weather got worse. Rain picked up, and a junction signal further along — separate from Falcon Bank — started throwing intermittent signal failure warnings. 2T19 was approaching that junction and needed a routing call within a couple of minutes.

Interviewer: What were you weighing there?

Participant: Send it through on the affected signal relying on backup indication and the driver's caution, divert it onto the loop line which adds six minutes, or hold it at the previous station until the fault's diagnosed. Meanwhile 6M42 was still moving through Falcon Bank fine, no further anomalies.

Interviewer: What did you decide?

Participant: I sent 2T19 round the loop. That signal issue felt different in character — a live "failure" warning rather than a short clean blip — and I didn't have any history on that particular fault to lean on, so I wasn't willing to trust backup indication on an unfamiliar problem. Six minutes felt like a cheap price for not gambling on something I hadn't seen before.

Interviewer: Interesting that you treated that one differently to the Falcon Bank flicker.

Participant: Yeah — I didn't have a pattern to fall back on there, so holding back felt like the safer default. Turned out to be an unrelated relay fault, nothing to do with Falcon Bank at all, but I didn't know that at the time.

Interviewer: What happened after that?

Participant: The Falcon Bank circuit flickered again — same kind of brief occupied indication — but this time 6M42 was confirmed still inside the section. I finally got hold of the on-call technician, who told me the circuit's wiring has a known moisture-sensitivity problem that's never been fully run down. Driver of 6M42 reported nothing unusual, normal progress, no obstruction visible. And 2T19 was closing in behind, having rejoined the main line off the loop.

Interviewer: What options did you have at that point?

Participant: Carry on as normal and let 2T19 follow into Falcon Bank once clear, treating the second flicker the same way as the first. Suspend normal working and go to pilotman working for everything through that section until it's properly looked at. Or hold 2T19 short and get the technician to physically inspect before anything else moves.

Interviewer: What did you choose?

Participant: I went to pilotman working. Once the technician mentioned there was an actual unresolved wiring issue behind it, the flicker stopped feeling like the same closed case from earlier — it felt like there was something real and undiagnosed sitting underneath it, so I wanted a person physically controlling movement rather than relying on the circuit again.

Interviewer: If the maintenance log hadn't shown those three prior nuisance trips, do you think you'd have handled the first flicker differently?

Participant: Almost certainly, yes. Without that history I think I'd have made the call to the foreman before giving 6M42 the road. The pattern is really what let me treat it as already explained.

Interviewer: Looking back, what would you change about the initial decision?

Participant: I'd probably still weigh the history heavily, but I think I'd want some cheap independent check alongside it rather than letting the pattern alone close the question. A quick call doesn't cost that much against holding a train.

Interviewer: What would need to change, procedurally, for you to verify faster next time?

Participant: Direct line to the technician's diagnostic panel instead of routing through the on-call rota — that delay probably shaped a couple of my later calls too.

Interviewer: Last one — how do you think a colleague would've handled that first flicker?

Participant: Honestly, most of the desk would've read it the same way I did. That log is well known on our shift. Whether that's the right instinct or not, I couldn't tell you for certain — nothing went wrong that night, but I know that doesn't prove it was the right call either.

Interviewer: That's a good place to stop. Thanks for your time.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Uncertainty Rejection Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as premature resolution of a genuinely ambiguous/intermittent signal into a falsely certain category (pattern-matched to prior nuisance trips), coupled with forgoing an available verification action, rather than mere risk tolerance or time-pressure heuristic use alone."
      }
    ],
    "target_bias_names": [
      "Uncertainty Rejection Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Uncertainty Rejection Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias",
        "decision_point": 1
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias",
        "mechanism": "Forcible resolution of an ambiguous intermittent track circuit indication into a familiar, certain category (nuisance trip) based on maintenance history pattern-match, followed by forgoing available independent verification (trackside telephone or pilotman working) that would have addressed the residual uncertainty.",
        "affected_reasoning_operation": "Evidence interpretation under ambiguity and the decision to seek versus forgo verification",
        "evidence_source": "Maintenance log of prior nuisance trips combined with the live intermittent occupancy indication and onset of rain",
        "distinctiveness_requirement": "This is the only planned instance of this bias; it must be textually and causally distinct from the phase 2 partial-readback acceptance and phase 3 precautionary diversion, which are governed by different reasoning operations (acceptance of incomplete confirmation; risk-averse rerouting) and must not be coded as additional bias instances."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Whether independent trackside verification was sought before authorizing movement into Falcon Bank",
      "original_state": "No verification sought; flicker treated as explained nuisance trip",
      "changed_state": "Verification sought via trackside telephone before authorizing movement",
      "variables_to_hold_constant": [
        "Weather onset and progression",
        "Maintenance log history of the circuit",
        "Garbled foreman readback content and timing",
        "Junction signal fault affecting 2T19",
        "Final technician diagnosis of the genuine intermittent short"
      ]
    },
    "scenario_id": "RT_Biased_1",
    "domain_id": "RT",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the strongest mechanism fit (ambiguous evidence requiring interpretation and a verification-seeking choice), per rule 2 of the allocation guidance; no spreading was needed since only one occurrence was requested.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Weather onset and progression",
      "Maintenance log history of the circuit",
      "Garbled foreman readback content and timing",
      "Junction signal fault affecting 2T19",
      "Final technician diagnosis of the genuine intermittent short"
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
