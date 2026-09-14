You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is for a plan-review case study, it's voluntary, and you can skip anything you'd rather not discuss. Can you start by telling me your role and how the Meridian Tower conversion landed on your desk?

Participant: Sure. I'm a plan review official in the building and fire division, mostly permitting and life-safety sign-off. Meridian Tower came to me because it was an adaptive reuse—22-story former office tower going to mixed-use residential and retail. The atrium was the whole complication. It's a big central void running most of the building height, and the geometry didn't fit the prescriptive smoke control provisions in our code. So the design team came in with a performance-based alternative instead.

Interviewer: What was your objective going in?

Participant: Get the project through review correctly and on time. We had a 30-day statutory clock, the department was short-staffed that quarter, and the city council was leaning on us to keep housing projects moving. So there was real pressure, but the job is still to make sure people are safe if there's a fire.

Interviewer: Walk me through what happened, from the beginning.

Participant: The engineering firm on record was Halkirk & Vance—they're a big regional name, they've done dozens of performance-based atrium designs, and a neighboring jurisdiction had approved a very similar design from them the year before. They submitted a CFD-based smoke control model instead of the prescriptive system. We didn't have budget that cycle for an outside peer review of the CFD assumptions, so it was really me evaluating it against the documentation package. After I signed off, we moved to writing commissioning conditions, which is where we had to pick between two verification protocols. Construction got underway, and partway through, our inspector flagged fire-door deficiencies on three floors. Then near occupancy, the developer pushed for an early certificate before full integration testing was done. Later in construction, there was a small trash-chute fire—sprinklers knocked it down fast, nobody was hurt—but it got people looking hard at the atrium smoke system again.

Interviewer: Let's reconstruct the order more precisely. What did you know before the first big decision, and what came in afterward?

Participant: Before approving the design, I had the CFD report, the firm's track record, and the neighboring jurisdiction's prior approval. After I approved it, we moved into commissioning planning—that's when the protocol question came up. After that decision, construction started, and the door issue surfaced maybe six weeks in. The occupancy request came right at the tail end, with the fire happening after that decision, not before.

Interviewer: Let's go through the first decision—approving the performance-based design. What evidence carried the most weight for you?

Participant: Honestly, the firm's name carried a lot of it. Halkirk & Vance has been doing this specific type of atrium work for years, and I knew their stamp had held up under scrutiny elsewhere—that neighboring jurisdiction's sign-off mattered to me. I read through the CFD report, but with the review clock running and no budget for an outside check, I leaned on the fact that this firm doesn't submit sloppy work. If it had been a firm I didn't recognize, I probably would have pushed harder on the input assumptions myself.

Interviewer: Was requiring an outside peer review on the table?

Participant: It was, but it would have added about three weeks, and given who submitted it, that felt like an unnecessary delay for a firm with that reputation.

Interviewer: Second decision—the commissioning protocol. What were you weighing there?

Participant: Two options. Option A was a newer risk-informed test, better matched to this atrium's actual geometry according to the guidance documents, but its pass/fail thresholds were described in fairly qualitative terms. Option B was the old prescriptive smoke test—clear binary pass or fail, easy to defend if anyone questioned it later, but known to be less sensitive to some of the failure modes this particular atrium could have.

Interviewer: Which did you pick, and why?

Participant: Option B. I'll be straight about it—part of the appeal was that I knew exactly what passing looked like and exactly what failing looked like. Option A might have been the better technical fit, the guidance basically said so, but I didn't want to be defending a judgment call on "partially qualitative" thresholds if something went sideways. B gave me a clean line.

Interviewer: Third decision—the door deficiencies. What did you see, and how did you respond?

Participant: Our inspector found bad fire-door installations on floors 8, 11, and 14. Out of the whole building, those three stood out to me, and my read was that we had a problem crew or a bad batch of hardware concentrated there. I redirected our follow-up inspection effort to those three floors specifically.

Interviewer: Were the crews assigned by floor, or rotated?

Participant: Rotated randomly across the building, actually. And it was three deficiencies out of about 150 doors we'd checked at that point, which is close to what you'd expect on a project this size just from ordinary variation. But when you see three flagged floors, it's hard not to read that as meaning something.

Interviewer: Fourth decision—the temporary occupancy request. What was your basis for granting it?

Participant: The developer had a financing deadline, and full integration testing on the alarm and smoke systems was still three weeks out. This contractor has a good record on other city jobs I've handled, so I felt reasonably confident things would come together. A colleague also mentioned a similar building nearby that had gotten early partial occupancy and it worked out fine. I did know our own five-year numbers show something like 15 percent of these atrium smoke-control integration tests need rework citywide, but that felt like a background statistic rather than something specific to this job.

Interviewer: What would have made you deny it instead?

Participant: If the contractor's record had been shakier, or if there'd been an active known defect in the smoke system at that point, I'd have held the line. Nothing like that was flagged to me at the time.

Interviewer: How much uncertainty did you feel at each of these points?

Participant: Honestly, less than maybe I should have on the first and last ones. The door issue felt more certain than it probably was, in hindsight. The protocol choice, I knew I was trading some technical fit for administrative clarity going in.

Interviewer: Looking back now, after the trash-chute fire, how do you view the original design approval?

Participant: It's hard not to think the smoke migration issue should have jumped out at someone reading that CFD report closely. There was a sensitivity assumption buried in there about stack effect under partial door-open conditions, and looking at it now, it feels like it was sitting right there in the numbers the whole time. At the time, though, it just didn't register as something that mattered—it was one line among a lot of technical detail, and nothing about it stood out as a flag worth chasing back then.

Interviewer: If you had the same information again, would you change the occupancy call?

Participant: Probably not without new information. It felt like a reasonable bet given the contractor's history at the time.

Interviewer: Last one—what would you tell a newer reviewer handling a similar submittal?

Participant: Don't let a strong firm's name substitute for reading the assumptions line by line, and don't let a small, tidy pattern in inspection data talk you out of checking the actual numbers behind it.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Clustering illusion",
        "occurrences": 1,
        "mechanism_constraint": "Must involve inference of a systemic pattern from a small, randomly distributed sample of fire-door deficiencies."
      },
      {
        "bias": "Probability neglect or Base-Rate Neglect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve discounting or omitting an available statistical base rate in favor of a vivid anecdote."
      },
      {
        "bias": "Optimism bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve unwarranted confidence in a future project-specific outcome based on general (not case-specific) favorable track record."
      },
      {
        "bias": "Ambiguity effect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve preference for an option with clearly defined criteria over a better-matched option with less-defined criteria."
      },
      {
        "bias": "Authority Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve deference to credentials/reputation as a substitute for independent technical verification."
      },
      {
        "bias": "Hindsight bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve retrospective claim of foreseeability inconsistent with information actually available at the time of the original decision."
      }
    ],
    "target_bias_names": [
      "Clustering illusion",
      "Probability neglect or Base-Rate Neglect",
      "Optimism bias",
      "Ambiguity effect",
      "Authority Bias",
      "Hindsight bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Clustering illusion", "requested_occurrences": 1 },
      { "bias": "Probability neglect or Base-Rate Neglect", "requested_occurrences": 1 },
      { "bias": "Optimism bias", "requested_occurrences": 1 },
      { "bias": "Ambiguity effect", "requested_occurrences": 1 },
      { "bias": "Authority Bias", "requested_occurrences": 1 },
      { "bias": "Hindsight bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "auth_01", "bias": "Authority Bias" },
      { "instance_id": "hind_01", "bias": "Hindsight bias" },
      { "instance_id": "amb_01", "bias": "Ambiguity effect" },
      { "instance_id": "clu_01", "bias": "Clustering illusion" },
      { "instance_id": "opt_01", "bias": "Optimism bias" },
      { "instance_id": "prob_01", "bias": "Probability neglect or Base-Rate Neglect" }
    ],
    "intended_decision_points": [
      { "instance_id": "auth_01", "bias": "Authority Bias", "decision_point": 1 },
      { "instance_id": "hind_01", "bias": "Hindsight bias", "decision_point": 1 },
      { "instance_id": "amb_01", "bias": "Ambiguity effect", "decision_point": 2 },
      { "instance_id": "clu_01", "bias": "Clustering illusion", "decision_point": 3 },
      { "instance_id": "opt_01", "bias": "Optimism bias", "decision_point": 4 },
      { "instance_id": "prob_01", "bias": "Probability neglect or Base-Rate Neglect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "auth_01",
        "bias": "Authority Bias",
        "mechanism": "Approval decision driven by firm's reputation/credentials rather than independent verification of CFD assumptions.",
        "affected_reasoning_operation": "Evidence weighting during technical submittal review",
        "evidence_source": "Firm credentials and peer-jurisdiction precedent",
        "distinctiveness_requirement": "Must be tied to the Phase 1 approval act itself, not to a later reflection on it."
      },
      {
        "instance_id": "hind_01",
        "bias": "Hindsight bias",
        "mechanism": "Post-incident reattribution of the Phase 1 decision as having been obviously flawed, using knowledge unavailable at the time.",
        "affected_reasoning_operation": "Retrospective causal attribution in response to a closing probe",
        "evidence_source": "Post-incident knowledge of smoke migration issue, contrasted with original CFD documentation",
        "distinctiveness_requirement": "Must occur as a retrospective statement about Phase 1, temporally and evidentially distinct from the auth_01 act itself."
      },
      {
        "instance_id": "amb_01",
        "bias": "Ambiguity effect",
        "mechanism": "Preference for the protocol with clearer criteria over the better-matched but less-defined protocol.",
        "affected_reasoning_operation": "Comparative choice between two commissioning protocols",
        "evidence_source": "Guidance documents on protocol fit versus stated protocol criteria clarity",
        "distinctiveness_requirement": "Distinct decision point and evidence set from all other instances; unique to Phase 2 protocol selection."
      },
      {
        "instance_id": "clu_01",
        "bias": "Clustering illusion",
        "mechanism": "Inference of a systemic crew-level pattern from a small, randomly distributed sample of deficiencies.",
        "affected_reasoning_operation": "Pattern recognition from inspection sample data",
        "evidence_source": "Deficiency location data and random crew rotation policy",
        "distinctiveness_requirement": "Unique to Phase 3 inspection data; not reused in Phase 4 reasoning."
      },
      {
        "instance_id": "opt_01",
        "bias": "Optimism bias",
        "mechanism": "Unwarranted confidence that atrium-specific testing will pass, based on general (not case-specific) contractor track record.",
        "affected_reasoning_operation": "Forward risk forecasting for occupancy decision",
        "evidence_source": "Contractor's general historical performance across unrelated projects",
        "distinctiveness_requirement": "Distinguished from prob_01 by relying on the contractor's general reputation, not on statistical base-rate versus anecdote comparison."
      },
      {
        "instance_id": "prob_01",
        "bias": "Probability neglect or Base-Rate Neglect",
        "mechanism": "Discounting the department's own citywide statistical base rate in favor of a single salient anecdote about a nearby building.",
        "affected_reasoning_operation": "Evidence weighting between statistical data and anecdotal precedent",
        "evidence_source": "Citywide integration-test failure/rework rate data versus colleague's anecdote",
        "distinctiveness_requirement": "Distinguished from opt_01 by the specific evidentiary contrast between an available base rate and a vivid anecdote, rather than general reputation-based optimism."
      }
    ],
    "intended_strength": [
      { "instance_id": "auth_01", "bias": "Authority Bias", "strength": "subtle" },
      { "instance_id": "hind_01", "bias": "Hindsight bias", "strength": "subtle" },
      { "instance_id": "amb_01", "bias": "Ambiguity effect", "strength": "moderate" },
      { "instance_id": "clu_01", "bias": "Clustering illusion", "strength": "subtle" },
      { "instance_id": "opt_01", "bias": "Optimism bias", "strength": "subtle" },
      { "instance_id": "prob_01", "bias": "Probability neglect or Base-Rate Neglect", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "engineering_firm_reputation",
      "original_state": "Nationally recognized, previously-approved fire protection engineering firm (Halkirk & Vance)",
      "changed_state": "Locally unknown firm with no prior approval history (autoselected candidate; not applied in current biased-condition generation)",
      "variables_to_hold_constant": [
        "Atrium geometry and code non-conformance",
        "Statutory review timeline and staffing constraints",
        "Developer schedule pressure",
        "Decision points 2, 3, and 4 and their associated evidence"
      ]
    },
    "scenario_id": "HE_Biased_6",
    "domain_id": "HE",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Automatic allocation per mechanism fit and narrative realism: each bias assigned to the decision point whose evidence-processing operation most naturally instantiates its mechanism; distinct biases permitted to share a decision point (DP1: auth_01+hind_01; DP4: opt_01+prob_01) provided they use different evidence sources and reasoning operations; no bias exceeds one instance per the manifest, so the two-per-decision-point same-bias cap was never approached.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Atrium geometry and code non-conformance",
      "Statutory review timeline and staffing constraints",
      "Developer schedule pressure",
      "Contractor identity and general track record",
      "Sequence and content of the four decision points"
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
