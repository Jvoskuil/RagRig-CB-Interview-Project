You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on the elevated I-131 reading you caught during the backshift a couple weeks ago — nothing punitive, I just want to understand how you worked through it. Can I get your role and shift context first?

Participant: Sure. I'm a radiochemistry tech, second shift lead on backshift when it happened. Reduced crew that night — just me and one other tech in the lab, supervisor was in the control room, not on the floor.

Interviewer: Good. Walk me through what happened from the top.

Participant: I was running a routine RCS grab sample, standard surveillance, hot leg sample through the panel, straight into the HPGe for the count. When I pulled the spectrum, the I-131 photopeak was way up — something like three times the trend from the week before. First thing that jumped to mind was the fuel-defect event we had last outage. I was on shift for that one too, actually caught the original spike, so I remembered exactly what that spectrum looked like, and this one had a similar shape to it. My gut said we might have a cladding defect starting.

Interviewer: What else was going on around that reading, technically?

Participant: A few things. The detector had just come back from a recalibration two days before — routine, after some maintenance work. So there was some residual uncertainty baked in there, we hadn't fully re-baselined the efficiency curve yet. Power was steady at 100%, no transients logged, letdown flow was normal. So nothing on the plant side jumped out as an obvious driver.

Interviewer: Given the recalibration was so recent, did that register as a competing explanation?

Participant: It crossed my mind, yeah. I noted it in my head — "detector was just touched, keep that in your back pocket." But honestly the fuel-defect angle felt like the more urgent thing to chase down first, because I'd lived through that exact scenario before and knew how fast it can escalate if you sit on it. So I ran with that as my working theory and figured I'd circle back to the calibration question if the fuel-defect leads didn't pan out.

Interviewer: What did you do next?

Participant: I set up a repeat count on the same sample to confirm the peak wasn't a fluke, and while that was running I started looking at secondary indicators — the Cs-137 ratio, background counts, counting geometry, that kind of thing.

Interviewer: What came out of the repeat count?

Participant: Ratio shifted slightly from the first count, not hugely, but enough that I filed it as "real signal, not noise." No corresponding power or flow change logged for the shift either, which kept the plant-transient explanation off the table.

Interviewer: That's decision point one, roughly — leaning into the fuel-defect read early. Let's move to what happened after that repeat count.

Participant: Right, so once I had a second data point, I started comparing the shape of this spectrum — the peak shape and that Cs-137 ratio — against stuff I'd seen before. And it actually reminded me a lot of a case from maybe eighteen months back, a resin intrusion event in the letdown demineralizer. Different system, different sample point, but the spectral signature had that same kind of look to it. So I started leaning toward calling it a resin-intrusion-type issue rather than purely a fuel defect.

Interviewer: Had you drawn a demineralizer effluent sample at that point to check?

Participant: Not yet, no. That sample takes a bit longer to pull and process, so I was going off the resemblance of the two spectra while that was in queue. It looked enough like the old case that I figured we were probably looking at the same kind of root cause, even though I hadn't confirmed the pathway yet.

Interviewer: What made the resemblance persuasive versus, say, waiting for the demineralizer sample first?

Participant: Time, mostly. We had a reporting window closing on us, and I wanted to have some working hypothesis in hand rather than nothing. The two sample points are physically different — I knew that — but the pattern match felt strong enough that I didn't push hard to verify the pathway before forming the call.

Interviewer: What did the demineralizer sample eventually show?

Participant: Different Cs-137 to I-131 ratio than the RCS sample, actually. And I&C confirmed no open work orders on the RCS panel valves, so cross-contamination through hardware wasn't it either. That complicated things a bit.

Interviewer: Let's talk about the escalation decision — point three. Once you had two consistent counts showing a real elevation, what did you do?

Participant: I went to the shift supervisor with a preliminary call. I told him I thought we were looking at an early fuel-defect indicator, possibly compounded by something upstream, and that I wanted to keep sampling frequency up. I'd already formed that framing in my head from the earlier steps, so that's the story I brought him.

Interviewer: Did you consider looping in reactor engineering before that formal notification?

Participant: I thought about it, but the tech spec clock was ticking and I didn't want to sit on the report. Supervisor asked right away whether I was recommending a power reduction, and reactor engineering wanted the last three surveillance points for comparison, so it kicked off a bigger conversation than I'd expected.

Interviewer: And the fourth point — finalizing the report?

Participant: By then I had the repeat count, the split sample, and the demineralizer result all in hand. Reactor engineering's fuel-performance model came back probabilistic, not a clean yes-or-no. I ended up writing the report with a ranked list of possible causes rather than pinning it to one thing, and recommended bumping up the sampling frequency for the next 24 hours instead of locking in a single root cause right away.

Interviewer: What tipped you toward the ranked approach instead of a single definitive call?

Participant: Honestly, by that point the data wasn't clean enough to be confident in one explanation. The demineralizer ratio didn't match, the valve work orders were clear, and the model wasn't definitive either. Given how the earlier assumptions hadn't fully held up, I didn't want to overcommit the final write-up.

Interviewer: Looking back, what would've changed your first read, at the very start?

Participant: If I hadn't been the one who caught that fuel-defect spike last outage, I might not have jumped there first. I might have given the recalibration explanation more weight right out of the gate instead of parking it.

Interviewer: And if you'd pulled the demineralizer sample before forming any theory at all?

Participant: I think I'd have held off longer before connecting it to that old resin-intrusion case. The pattern match was persuasive in the moment, but it turned out not to hold up once the actual pathway data came in.

Interviewer: Last one — what would you tell a newer tech about using past cases to read a new spectrum?

Participant: I'd say a prior case can point you somewhere to look, but don't let it stand in for confirming the actual pathway. Get the second sample before you commit to the story, not after.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Salience Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overweighting a vivid, personally memorable prior fuel-defect event relative to an objectively relevant competing explanation (recent recalibration) at the first data point."
      },
      {
        "bias": "Similarity Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as causal attribution based on superficial spectral resemblance to an unrelated prior case, made or strongly favored before confirmatory pathway evidence is obtained."
      }
    ],
    "target_bias_names": ["Salience Bias", "Similarity Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Salience Bias", "requested_occurrences": 1},
      {"bias": "Similarity Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "sb_01", "bias": "Salience Bias"},
      {"instance_id": "sim_01", "bias": "Similarity Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "sb_01", "bias": "Salience Bias", "decision_point": 1},
      {"instance_id": "sim_01", "bias": "Similarity Bias", "decision_point": 2}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "mechanism": "Overweighting a vivid, personally memorable prior fuel-defect event during initial hypothesis formation, at the expense of the objectively relevant recalibration-artifact explanation",
        "affected_reasoning_operation": "Initial hypothesis generation and weighting from first spectrum count",
        "evidence_source": "Technician's autobiographical memory of prior outage fuel-defect event versus the logged recalibration date",
        "distinctiveness_requirement": "Must be tied specifically to the memorability/vividness of a past personal event overriding an objectively available competing cue, not to mere pattern resemblance (which is reserved for the Similarity Bias instance)"
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "mechanism": "Causal attribution driven by superficial resemblance between the current spectrum and an unrelated prior case's spectrum, prior to obtaining confirmatory pathway-specific evidence",
        "affected_reasoning_operation": "Evidence-selection and causal-attribution act during the demineralizer cross-check",
        "evidence_source": "Visual/quantitative resemblance of peak shape and isotopic ratio between current RCS sample and prior unrelated demineralizer case, versus the un-obtained demineralizer effluent sample",
        "distinctiveness_requirement": "Must be tied specifically to surface pattern resemblance between two different physical sampling contexts, not to personal memorability of either case (reserved for the Salience Bias instance) and must occur at a distinct decision point and evidence source from sb_01"
      }
    ],
    "intended_strength": [
      {"instance_id": "sb_01", "bias": "Salience Bias", "strength": "subtle"},
      {"instance_id": "sim_01", "bias": "Similarity Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Technician's firsthand vivid experience with precedent cases (autoselected)",
      "original_state": "Technician personally experienced both precedent cases and recalls them vividly",
      "changed_state": "Technician knows both precedent cases only from secondhand written records, without vivid personal recall",
      "variables_to_hold_constant": [
        "Reactor power level and operating conditions",
        "Timing and sequence of spectrum counts and confirmatory samples",
        "Staffing level and reporting deadlines",
        "Final confirmatory data outcomes"
      ]
    },
    "scenario_id": "NP_Biased_2",
    "domain_id": "NP",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread across distinct decision points (Salience Bias at decision point 1, Similarity Bias at decision point 2) per mechanism fit: Salience Bias fits the earliest ambiguous-cue interpretation moment; Similarity Bias fits the subsequent cross-source causal-attribution moment. No decision point received more than one instance of any single bias, satisfying the max-two-per-point rule trivially since each bias has only one occurrence.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Reactor power level and operating conditions",
      "Timing and sequence of spectrum counts and confirmatory samples",
      "Staffing level and reporting deadlines",
      "Final confirmatory data outcomes"
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
