You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. Just to confirm, you're okay with this being recorded for after-action training purposes only, not for any personnel review?

Participant: Yeah, that's fine.

Interviewer: Can you describe your role and what you were responsible for when this incident began?

Participant: I'm the Situation Unit Analyst for the county EOC. During an activation, I build and maintain the Common Operating Picture — pulling together field reports, gauge data, weather updates, whatever's coming in — and I turn that into something the Branch Directors can actually act on. That night I was covering the flood side while also keeping half an eye on the fire branch, since Ridge Fire was still active and was interfering with some of our sensor and repeater coverage.

Interviewer: Walk me through how the incident began.

Participant: Around 9 PM we got a notice from the Twin Forks Reservoir Authority about a release tied to the incoming storm cell. The wording was pretty standard operational language — not alarmist, but not something I'd call reassuring either. Our downstream gauges were showing a gradual rise at that point, nothing that clearly told you how big this was going to get. The duty hydrologist was tied up on another call for at least ninety minutes, so I didn't have a technical read to lean on. Our flood Branch Director looked at it and said the pattern looked similar to releases he'd seen before, but he also flagged that the rainfall forecast for this particular storm cell was less certain than in past events — he wasn't fully reassuring, just giving me his honest read on both sides of it.

Interviewer: What did you do with that information?

Participant: I went with a monitor-and-prepare advisory rather than an immediate warning. It wasn't really one factor — it was the gradual gauge trend, the Director's qualified take, and the fact that jumping straight to a warning without more to go on has its own costs, in terms of credibility and resource strain if it turns out to be nothing. I documented specific thresholds that would trigger an upgrade if the gauges moved past them, so it wasn't an open-ended wait.

Interviewer: Did you consider seeking independent verification before finalizing that?

Participant: I did think about it, but with the hydrologist unavailable, the choice was really between acting on the best synthesis I had or delaying any messaging at all, which carries its own risk. I weighed the Director's read alongside the actual gauge numbers rather than just taking his word for it.

Interviewer: What happened next?

Participant: About ninety minutes later, the gauges spiked much faster than the early trend had suggested. The release turned out to be larger than what the gradual rise had implied.

Interviewer: Let's talk about the resource decision that followed.

Participant: Our field liaison started getting scattered water-rescue calls in two sub-neighborhoods, but the call intervals were irregular — hard to say if that was tapering off or about to surge. Around the same time, the weather service bumped up their estimate of how long the storm cell would sit over us, and a neighboring jurisdiction let us know their swift-water assets were available on a limited-time mutual-aid hold.

Interviewer: How did you decide what to request?

Participant: I went with a staged tier-2 mobilization instead of matching the confirmed calls exactly or going straight to tier-3. Part of it was the call pattern being ambiguous, part of it was the extended storm estimate, and part of it was that mutual-aid window — if I waited and needed more later, those assets might not be there. None of those three things alone would've pushed me to tier-2, but together they did.

Interviewer: Was there a specific past incident that shaped that call?

Participant: Not really one specific case I was drawing on. It was more just weighing what was in front of me that shift.

Interviewer: How did that play out?

Participant: Calls plateaued at a level that, looking back, either tier-1 or tier-2 could've handled. Some of the mutual-aid assets got used, some stayed in reserve. Hard to say in hindsight whether tier-1 would've been enough or whether we got lucky with tier-2.

Interviewer: Let's move to the evacuation decision.

Participant: This was the hardest one. Six of eight gauges were down from repeater damage tied to the Ridge Fire smoke, so I only had two reporting, both rising sharply over about twenty minutes. We do have a contingency protocol for this — when network coverage drops below half, there's a default evacuation radius around any gauge that crosses threshold. Field spotters were also seeing street flooding near one of the two working gauges, though nothing yet from the other sub-zones.

Interviewer: How did you apply that?

Participant: I followed the protocol and expanded evacuation to the zones adjacent to those two gauges. I was explicit with the team that the radius is a policy compromise — it's not a claim that we know what's happening in the unmonitored zones, it's just the standard response when coverage is this degraded. I didn't feel like I had enough to justify going wider than the protocol called for, and I also didn't think it was responsible to wait for full confirmation given the rate of rise.

Interviewer: Did you weigh expanding further than the protocol specified?

Participant: I considered it, honestly. Two gauges isn't much of the network. But going beyond what the protocol lays out felt like it would've been guessing past the point where I had a documented basis for the call.

Interviewer: What came out of that?

Participant: When backup gauges came back later, the adjacent zones matched the protocol's assumptions in some spots and not others. So it's genuinely mixed — the protocol got some of it right and missed some of it.

Interviewer: Let's talk about the hot-wash review of the initial advisory decision.

Participant: We used our standard after-action template, which forces you to separate what was known at the time from what's known now. Going through it point by point, some parts of the original advisory call still look reasonable to me given the gradual trend and the Director's qualified comment. Other parts — like the uncertain storm-duration forecast — in hindsight, maybe should've pushed us toward an earlier tier upgrade. It's not a clean verdict either way.

Interviewer: Do you think the outcome makes that decision look worse than it actually was?

Participant: That's the tension the template is designed to catch. I try to ask what a reasonable person would've concluded with only the 9 PM information, not what's obvious now that we know the release was bigger than expected. Some of it holds up under that test, some of it doesn't.

Interviewer: If the dam operator's notice had used clearly urgent language instead of standard language, would your initial call have changed?

Participant: Possibly, but it wouldn't have been the only thing driving it — I'd still have been weighing the actual gauge trend and the Director's forecast concerns alongside it.

Interviewer: And if all eight gauges had stayed online through the evacuation decision?

Participant: I'd have had a fuller picture to work with, which might have let us tighten or widen the radius with more confidence either way. Hard to say which direction it would've gone.

Interviewer: Looking back, how do you separate what was knowable in the moment from what only became clear afterward?

Participant: I lean on the template for that specifically, because otherwise it's easy to let the outcome color your memory of how clear things actually were at 9 PM. Some calls hold up, some don't, and I try not to flatten that into a single before-and-after story either way.

Interviewer: That's a good place to stop. Thanks for walking through this.

Participant: No problem.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {"bias": "Illusion of Validity", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; any confidence expressed must be tied to explicit, stated evidentiary or policy grounds, not narrative coherence alone."},
      {"bias": "Insensitivity to sample size", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; any use of partial gauge data must be framed through explicit protocol compliance with an acknowledged uncertainty caveat, not through treating the sample as sufficient on its own."},
      {"bias": "Authority Bias", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; deference to the Branch Director, if present, must be one of several jointly weighed factors, not the stated sole reason for forgoing verification."},
      {"bias": "Availability Bias", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; recalled past events or salient media, if mentioned at all, must not be stated as the decisive driver of a resource or severity estimate."},
      {"bias": "Framing Effect", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; the dam operator's wording, if referenced, must not be stated as the decisive driver of the tier classification."},
      {"bias": "Hindsight bias", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; the retrospective review must explicitly separate real-time knowledge from outcome knowledge and avoid asserting that the outcome was clearly foreseeable from the outset."}
    ],
    "target_bias_names": [
      "Illusion of Validity",
      "Insensitivity to sample size",
      "Authority Bias",
      "Availability Bias",
      "Framing Effect",
      "Hindsight bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Illusion of Validity", "requested_occurrences": 0},
      {"bias": "Insensitivity to sample size", "requested_occurrences": 0},
      {"bias": "Authority Bias", "requested_occurrences": 0},
      {"bias": "Availability Bias", "requested_occurrences": 0},
      {"bias": "Framing Effect", "requested_occurrences": 0},
      {"bias": "Hindsight bias", "requested_occurrences": 0}
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "EM_Biased_7",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Ambigious_7",
    "domain_id": "EM",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, so no bias occurrences are allocated to any decision point. The four decision points instead each carry a genuinely underdetermined judgment call supported by an explicit non-bias operational justification (joint weighing of factors in Phase 1, multi-factor staged mobilization in Phase 2, protocol-based contingency radius with explicit uncertainty caveat in Phase 3, structured after-action separation of real-time vs. outcome knowledge in Phase 4), constructed to match the paired biased scenario's structure, vocabulary, actors, and decision count without reproducing any of its bias-specific mechanisms.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and role (EOC Situation Unit Analyst)",
      "Four-decision-point chronology and topic sequence (threat classification, resource mobilization, evacuation scope, retrospective hot-wash)",
      "Stakeholder set and organizational hierarchy",
      "Technical vocabulary and terminology level",
      "Moderate difficulty and degraded-information constraints (partial gauge outage, unavailable hydrologist, smoke-limited aerial recon)",
      "Overall narrative tone and time-pressure profile",
      "Target interview length (1,215-1,485 words)"
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
