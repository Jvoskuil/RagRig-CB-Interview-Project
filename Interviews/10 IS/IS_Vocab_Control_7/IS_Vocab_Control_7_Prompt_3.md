You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was "right." Everything stays in the design systems research archive. Sound okay?

Participant: Sure, happy to walk through it.

Interviewer: Can you remind me of your role and what triggered this whole evaluation?

Participant: I lead design systems for the platform org — three designers, two engineers under me. Legal flagged that we needed to hit WCAG 2.2 AA across two customer-facing squads within about ten weeks, and our internal component library had known contrast and focus-state debt. LumenKit came up because a couple of competitors use it and it's picked up some industry recognition.

Interviewer: What was your goal going into the vendor demo?

Participant: Mainly to see whether adopting something pre-built could shortcut months of remediation work, given the timeline.

Interviewer: Walk me through what happened, in order.

Participant: The solutions engineer ran about forty minutes, mostly on their accordion component — motion, keyboard handling, graceful degradation. Genuinely well done. They also said the library ships with AA-compliant color defaults. Rather than take that at face value, I asked for their contrast-ratio spec sheet on the core color and elevation tokens before deciding anything about pilot scope. When it came back, I noticed it only covered default, unthemed values — nothing about how those tokens would behave once we applied our own theming layer. That gap mattered, since our actual implementation would always be themed.

Interviewer: What did that lead you to do?

Participant: I scoped the pilot narrowly — just the token categories tied directly to our compliance gap, not the whole library — since the spec sheet couldn't tell me how the tokens would hold up once themed. We got a three-week sandbox limited to that smaller set. Both squad leads said they were interested but wanted pricing before committing engineering time.

Interviewer: Did anything push you toward a broader commitment at that point?

Participant: Not really. The demo was impressive, but impressive motion design on one component doesn't tell you much about contrast behavior on a different set of tokens, so I kept those separate in my head.

Interviewer: Let's move to licensing. What did that look like?

Participant: Procurement needed a recommendation in two weeks. Three tiers: Basic, five components, no support; Team, twelve components, limited support, priced not far below Enterprise; Enterprise, full library with dedicated support. I mapped what the narrow pilot actually needed against each tier's component list rather than just comparing the tiers to each other.

Interviewer: What did that comparison show?

Participant: Team actually covered our confirmed needs — the components we'd already scoped plus reasonable headroom for the second squad. Enterprise had things we weren't using yet. I recommended Team and flagged that we could revisit Enterprise later if adoption grew.

Interviewer: And the rollout timeline?

Participant: I hadn't set a date yet at that point. I asked both squad leads directly what their earliest realistic integration window was, given their existing release calendars, before committing to anything.

Interviewer: What did they say?

Participant: One could start in three weeks, the other in five. I set the rollout date to the later window rather than picking something in between and hoping it would work out.

Interviewer: What information would have changed that recommendation, looking back?

Participant: Honestly, not much — checking actual needs against the tier list and getting real calendar commitments from both squads is basically what I'd do again.

Interviewer: Let's get to the audit. What came back?

Participant: About seven weeks in, our internal accessibility audit found that several LumenKit color and elevation tokens failed contrast requirements in three of five tested components. I'd told the VP and both squad leads earlier that the defaults tested well in the initial spec review and pilot, but I'd also flagged at the time that full-scale testing was still pending.

Interviewer: What was your first move on the discrepancy?

Participant: I wanted to know whether the failure was in our theming layer or in the vendor's own default tokens, so I requested an independent retest of LumenKit's out-of-box tokens with no internal theming applied. I didn't want to guess at the cause.

Interviewer: What did the retest show?

Participant: It confirmed the failures originated in the vendor's default token values, not our theming. That was useful because it told us exactly which components needed to change.

Interviewer: What did you decide to do with that?

Participant: We'd put some engineering hours into customizing those tokens already, but once the retest pointed at the vendor defaults specifically, I reverted just the three affected components to our already-remediated legacy tokens and left the rest of the LumenKit components in place, since those had tested clean.

Interviewer: Did the VP or squad leads react?

Participant: The VP asked for a written explanation for the compliance file, which I could give directly from the retest data. Both squads were fine with the partial reversion once they saw which components were affected.

Interviewer: That brings us to the final call. What were the options three weeks before the deadline?

Participant: Expand LumenKit organization-wide, including the categories that had failed; adopt a hybrid — keep LumenKit's motion and layout components but source color and elevation tokens internally; or revert fully to legacy.

Interviewer: How did you weigh those?

Participant: The retest data was specific to color and elevation, not layout or motion, so a full revert seemed like it would throw away components that had actually tested fine. Full expansion seemed to reintroduce the exact risk we'd just found. The hybrid matched what the evidence actually showed — keep what tested clean, source internally what didn't.

Interviewer: So what did you recommend?

Participant: The hybrid. I documented the retest findings, the expected migration effort for each option, and the compliance risk if we expanded the failing categories anyway, and sent that to the VP and counsel before finalizing it.

Interviewer: If the audit had come in during week one instead of week seven, would your approach to the retest have changed?

Participant: Probably not the approach — I'd still want to isolate vendor tokens from theming before deciding anything. It might have just meant less customization work to unwind.

Interviewer: If the vendor's demo hadn't included that contrast-ratio spec sheet at all, do you think your initial pilot scope would have looked different?

Participant: I likely would have asked for one anyway before scoping anything broadly — a strong demo on one component isn't evidence about a different set of tokens.

Interviewer: If procurement had only offered two tiers instead of three, would Team still have been your pick?

Participant: Depends on what the two were, but I'd still have checked actual component needs against whatever was offered rather than picking based on how the options looked next to each other.

Interviewer: Starting over today, what would you keep, and what would you change?

Participant: I'd keep asking for direct evidence before scoping decisions and getting real commitments from the squads before setting dates. I'm not sure I'd change much — the one thing I'd tighten up is flagging the "pending full-scale testing" caveat more visibly in written updates, so it's not just something I remember saying.

Interviewer: This has been really useful. Thanks for walking through the reasoning in this much detail.

Participant: No problem — it's a good exercise to lay it out step by step like this.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {"bias": "Priming effect", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Cognitive Dissonance", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Decoy effect", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Halo effect", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Illusion of control", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Sunk Cost Bias", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Status Quo Bias", "occurrences": 0, "mechanism_constraint": null}
    ],
    "target_bias_names": [
      "Priming effect",
      "Cognitive Dissonance",
      "Decoy effect",
      "Halo effect",
      "Illusion of control",
      "Sunk Cost Bias",
      "Status Quo Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Priming effect", "requested_occurrences": 0},
      {"bias": "Cognitive Dissonance", "requested_occurrences": 0},
      {"bias": "Decoy effect", "requested_occurrences": 0},
      {"bias": "Halo effect", "requested_occurrences": 0},
      {"bias": "Illusion of control", "requested_occurrences": 0},
      {"bias": "Sunk Cost Bias", "requested_occurrences": 0},
      {"bias": "Status Quo Bias", "requested_occurrences": 0}
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IS_Biased_7",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IS_Vocab_Control_7",
    "domain_id": "IS",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control requires zero intended occurrences of every named bias. Decision points were instead populated with evidence-checked, alternative-considered reasoning that mirrors the paired scenario's four-phase structure (demo/pilot-scoping, licensing/timeline, post-audit continuation, final rollout-model) without instantiating priming, halo, decoy, illusion of control, cognitive dissonance, sunk cost, or status quo mechanisms.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Compliance deadline (10 weeks) and final 3-week decision window",
      "Team headcount and resourcing",
      "Vendor identity (LumenKit) and its reputation",
      "Three-tier licensing structure",
      "Audit occurrence and general timing (~week seven)",
      "Number and identity of dependent squads",
      "Four-phase decision chronology and stakeholder set matched to IS_Biased_7"
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
