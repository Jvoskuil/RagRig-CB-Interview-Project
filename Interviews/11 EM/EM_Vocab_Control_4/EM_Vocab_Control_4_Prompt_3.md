You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. This is a routine debrief on your reasoning process during the Copper Creek event, not a performance review — nothing here affects your evaluation. Okay to proceed on that basis?

Participant: Sure, that's fine.

Interviewer: Can you start by describing your role on the desk that shift?

Participant: I'm the meteorological hazard forecaster for the ESF-2/ESF-5 desk at the state EOC. I translate NWS and SPC guidance into activation-level recommendations, warning products, and messaging calls for the counties in our basin. I coordinate with the WFO, the county EMs, and on multi-state events, with neighboring forecast desks.

Interviewer: Walk me through this particular incident from the start.

Participant: It started overnight with SPC flagging a marginal severe risk for the basin, low confidence, mostly because guidance was still sparse. By the 06Z cycle we only had four members of the convection-allowing ensemble finished — the rest were still running. Three of those four showed the cluster intensifying fast over the basin within about three hours. Given that we only had four members in, I didn't want to treat that as the full picture, so instead of a basin-wide upgrade I issued a limited advisory just for the highest-confidence sub-area and flagged that the guidance sample was still thin. A couple hours later, radar showed a hook-shaped reflectivity signature that looked a lot like an event I'd forecasted successfully a couple seasons back — similar CAPE and shear profile. It was tempting to just run with that track, but the motion vector still supported two plausible paths, so I got the WFO desk on the line before committing to anything. They confirmed the dual-track concern was legitimate and we kept both options open a while longer. Then flash flood guidance started climbing in two of our sub-watersheds, and I wanted to escalate the EOC activation level and get swift-water teams moving, since they need about 45 minutes lead time. The regional director called and asked us to hold, citing a pending downstream reservoir-release update that could shift the hydrologic picture within the hour. On the interstate coordination call after that, three of four neighboring jurisdictions said they were holding, citing rainfall totals below their local thresholds. Our own numbers were still worsening, so I issued a locally scaled escalation while keeping shared language for the parts of the basin that matched their situation. Flooding started in one of our towns about fifty minutes after that call ended.

Interviewer: Let's reconstruct the sequence more precisely. What did you have at each stage, and what were you still waiting on?

Participant: At the start, just the partial ensemble and the SPC discussion — no radar-observed rotation or guidance exceedance yet. Then the radar signature came in as a qualitative cue layered on the model data. After that, the guidance numbers gave us the first hard hydrologic evidence. And the coordination call added a comparison point — what the specific data behind each jurisdiction's position looked like, not just their stance.

Interviewer: Let's go through the four moments where you had to make a call. First: the early guidance decision. What alternatives did you weigh?

Participant: Upgrade basin-wide, hold entirely for the 09Z cycle, or scale it — advisory for the sub-area with the strongest signal while noting the limited sample. I went with the scaled option.

Interviewer: What tipped it?

Participant: Honestly, the fact that it was only four members mattered a lot. Three agreeing is worth something, but with that few total runs in, I didn't think it justified a full upgrade. Splitting the difference let us respond to the signal without overstating how solid it was.

Interviewer: Did the SPC's own confidence language factor in?

Participant: Yes — they were explicit that confidence was low given how sparse guidance still was, and that lined up with my instinct not to lean too hard on just four members.

Interviewer: Second decision — the radar signature and the track call. What made you loop in the WFO before settling on one track?

Participant: The signature really did remind me of that prior event, and part of me wanted to just call it. But recognizing a shape isn't the same as confirming a track, and the motion vector still supported two paths. I didn't have hard evidence to rule either one out, so getting an independent read felt like the responsible move before committing publicly.

Interviewer: How confident were you in the moment?

Participant: Moderately — maybe six or seven out of ten on the pattern match itself, but I held the actual forecast at "two plausible tracks" until the WFO's read came back and we converged.

Interviewer: Third decision point — the activation-level call after the director's instruction. What was your read going in?

Participant: Guidance exceedance was climbing, and my inclination was to escalate and get swift-water teams moving given the lead time. When the director called for a hold, I asked him what was driving it rather than just taking the instruction at face value.

Interviewer: What did he tell you?

Participant: He said there was a downstream reservoir-release update expected within the hour that could change the exceedance timing. That's a real variable I hadn't factored in yet, so I agreed to hold — but only with a defined recheck time, given how tight the swift-water lead time already was.

Interviewer: Was there a technical case for holding, independent of his instruction?

Participant: Once he explained the reservoir piece, yes — that's genuinely relevant hydrology I didn't have. It wasn't just deferring to him; it was incorporating information I was missing.

Interviewer: Fourth decision — the coordination call and public messaging.

Participant: My numbers favored escalating messaging and issuing a WEA locally. Three of four neighboring desks said they were holding, but they backed that up with their own rainfall totals, which were genuinely lower than ours. So I compared our specific numbers against theirs rather than just matching their stance, concluded our situation was different, and issued a scaled local escalation while keeping shared language for the overlapping parts of the basin.

Interviewer: What happened afterward?

Participant: Flooding started in one of our towns about fifty minutes later. The neighboring jurisdictions' hold positions turned out to be consistent with their own lower totals, so their call made sense for their situation.

Interviewer: If the fuller ensemble had been available from the start, would the early decision have gone differently?

Participant: Maybe — if more members had agreed, I might have gone straight to a basin-wide upgrade instead of scaling it. The small sample was really the reason I hedged.

Interviewer: If the director's call hadn't included the reservoir rationale, what would you have done?

Participant: I'd have pushed back harder or escalated anyway. The hold only made sense to me once I understood what new variable was behind it.

Interviewer: Looking back, with the same information available at each point, would you change anything?

Participant: Not fundamentally. I might have pinged the WFO even earlier on the track call, just to shorten how long we sat with two options. But splitting the difference on the early advisory and separating our data from the neighboring jurisdictions' data both felt like the right calls given what we actually had.

Interviewer: That's really helpful. Thanks for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusion of Validity",
        "occurrences": 0,
        "mechanism_constraint": "Not implemented under vocabulary_control condition; pattern recognition must be paired with a request for independent confirmation and retained track ambiguity."
      },
      {
        "bias": "Insensitivity to sample size",
        "occurrences": 0,
        "mechanism_constraint": "Not implemented under vocabulary_control condition; small ensemble size must be explicitly acknowledged and factored into the decision."
      },
      {
        "bias": "Authority Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not implemented under vocabulary_control condition; compliance with the director's directive must be grounded in an evaluated technical rationale."
      },
      {
        "bias": "Bandwagon effect",
        "occurrences": 0,
        "mechanism_constraint": "Not implemented under vocabulary_control condition; alignment or divergence from peer jurisdictions must be grounded in a genuine comparison of local data."
      }
    ],
    "target_bias_names": [
      "Illusion of Validity",
      "Insensitivity to sample size",
      "Authority Bias",
      "Bandwagon effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Illusion of Validity", "requested_occurrences": 0 },
      { "bias": "Insensitivity to sample size", "requested_occurrences": 0 },
      { "bias": "Authority Bias", "requested_occurrences": 0 },
      { "bias": "Bandwagon effect", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "EM_Biased_4",
    "counterfactual_variable": {
      "name": "Presence versus absence of a technically justified rationale accompanying the regional EOC director's hold directive at decision point 3",
      "original_state": "Director's hold directive is accompanied by a specific technical rationale (pending reservoir-release update)",
      "changed_state": "Director issues the same hold directive without any accompanying technical rationale",
      "variables_to_hold_constant": [
        "Storm evolution and meteorological data timeline",
        "Forecaster's role, experience, and prior technical read",
        "Coordination call composition and neighboring-jurisdiction positions",
        "Resource constraints (rescue team lead time)"
      ]
    },
    "scenario_id": "EM_Vocab_Control_4",
    "domain_id": "EM",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "vocabulary_control zero-instance override: per condition rules, all four biases in the paired target set are suppressed regardless of the caller-supplied manifest values; no decision-point allocation of bias instances was performed. Decision points instead mirror the paired scenario's structure with evidence-integrated, non-biased resolutions.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Storm characteristics and evolution",
      "Personnel roles and organizational structure",
      "Resource constraints and timing windows",
      "Basin geography and vulnerable-community locations",
      "Four-decision-point structure and decision sequencing relative to EM_Biased_4"
    ],
    "generation_warnings": [
      "The caller-supplied exact-occurrence manifest listed 1 occurrence per bias, but per the vocabulary_control condition rule, all requested occurrences are overridden to 0 and recorded as such in exact_occurrence_manifest; this is expected condition behavior, not a planning shortfall.",
      "counterfactual_variable was autoselected per input instruction (AUTOSELECT) for documentation and future pairing purposes only; it is not activated under the current 'vocabulary_control' condition and has no bearing on the zero-occurrence requirement for this scenario."
    ]
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
