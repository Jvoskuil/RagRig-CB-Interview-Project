You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was "right." Everything you share stays in the design systems research archive. Sound okay?

Participant: Sounds good. Happy to walk through it — it's still fresh, honestly.

Interviewer: Great. Can you remind me of your role and what triggered this whole evaluation?

Participant: I lead design systems for the platform org — three designers, two engineers under me. Legal flagged that we needed to hit WCAG 2.2 AA across two customer-facing squads within about ten weeks, and our internal component library had known contrast and focus-state debt we hadn't prioritized. LumenKit came up because a couple of competitors use it and it's picked up some industry recognition.

Interviewer: What was your goal going into the vendor demo?

Participant: Mainly to see if we could shortcut months of remediation work by adopting something pre-built and compliant, given the clock we were on.

Interviewer: Walk me through what happened, in order.

Participant: The solutions engineer ran maybe forty minutes, almost all of it on their accordion component — the motion, the keyboard handling, the way it degraded gracefully. It was genuinely impressive, smoother than anything we'd built in-house. They mentioned the whole library ships with AA-compliant color defaults. After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down. We got a three-week sandbox with a limited component set, and both squad leads said they were interested but needed pricing before committing engineering time.

Interviewer: Did you look closely at the color and elevation tokens before making that call?

Participant: Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape. That assumption is part of why I pushed for the broad pilot instead of testing component by component first.

Interviewer: Let's move to the licensing decision. What did that look like?

Participant: Procurement needed a tier recommendation within two weeks. Vendor offered three: Basic, five components, no support; Team, twelve components with limited support, priced not far below Enterprise; and Enterprise, the full library with dedicated support. I recommended Enterprise.

Interviewer: What made Enterprise the clear choice?

Participant: Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense.

Interviewer: And the rollout timeline — how was that set?

Participant: I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads.

Interviewer: Had the two dependent squads confirmed they could hit a four-week window?

Participant: Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars. One of them came back shortly after saying their calendar genuinely couldn't accommodate that window — they had an unrelated release freeze I hadn't accounted for.

Interviewer: What information would have changed your timeline call, looking back?

Participant: Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first.

Interviewer: Let's get to the audit. What came back?

Participant: About seven weeks in, our internal accessibility audit found that several of LumenKit's color and elevation tokens failed contrast ratio requirements in three of five tested components. That was awkward, because I'd already told the VP and both squad leads that LumenKit would solve most of our contrast problems out of the box.

Interviewer: What was your first read on that discrepancy?

Participant: My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities.

Interviewer: What did you decide to do next?

Participant: We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy. The legacy components already had remediated contrast values for those same screens, so that was sitting right there as an option.

Interviewer: What made continuing the more attractive path versus reverting?

Participant: Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked.

Interviewer: Did the VP or squad leads react?

Participant: The VP wanted a written explanation for the compliance file. One squad lead quietly reverted their branch back to the legacy component for the affected screens without waiting on my decision.

Interviewer: That brings us to the final call. What were the options three weeks before the deadline?

Participant: Expand LumenKit org-wide as we'd implemented it, adopt a hybrid — keep LumenKit's motion and layout components but source color and elevation tokens internally — or revert fully to legacy.

Interviewer: How did the hybrid option evaluate against the others?

Participant: On paper it addressed the token problem directly without throwing away the layout and motion integration work we'd already done. It was arguably the cleanest fix.

Interviewer: So what did you recommend?

Participant: I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. We'd already built the governance docs, onboarding materials, and squad training around the current implementation, and switching structure again this close to the deadline felt like more disruption than it was worth, even with the hybrid's technical case being reasonably strong.

Interviewer: If the audit had surfaced in week one instead of week seven, do you think that would have changed how you weighed the hours already spent?

Participant: Probably — with less invested, reverting or pivoting to the hybrid would've felt like a much smaller loss.

Interviewer: If the vendor demo had opened with contrast-ratio data instead of the accordion, would your initial pilot decision have gone differently?

Participant: Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly.

Interviewer: If procurement had only offered two tiers instead of three, would Enterprise still have been the obvious pick?

Participant: Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team.

Interviewer: Last one — starting over today, what would you keep, and what would you change?

Participant: I'd keep the urgency and the willingness to bring in outside tooling under deadline pressure — that part was right. I'd change how early I locked in public commitments about what the library would solve, and I'd get squad confirmation on timelines before setting them rather than after.

Interviewer: This has been really useful. Thanks for being so candid about the reasoning, not just the outcome.

Participant: No problem — it's easier to see it laid out like this than it was living through it week to week.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Priming effect", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Cognitive Dissonance", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Decoy effect", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Halo effect", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Illusion of control", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Sunk Cost Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Status Quo Bias", "occurrences": 1, "mechanism_constraint": null}
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
      {"bias": "Priming effect", "requested_occurrences": 1},
      {"bias": "Cognitive Dissonance", "requested_occurrences": 1},
      {"bias": "Decoy effect", "requested_occurrences": 1},
      {"bias": "Halo effect", "requested_occurrences": 1},
      {"bias": "Illusion of control", "requested_occurrences": 1},
      {"bias": "Sunk Cost Bias", "requested_occurrences": 1},
      {"bias": "Status Quo Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Priming effect"},
      {"instance_id": "cb_02", "bias": "Halo effect"},
      {"instance_id": "cb_03", "bias": "Decoy effect"},
      {"instance_id": "cb_04", "bias": "Illusion of control"},
      {"instance_id": "cb_05", "bias": "Cognitive Dissonance"},
      {"instance_id": "cb_06", "bias": "Sunk Cost Bias"},
      {"instance_id": "cb_07", "bias": "Status Quo Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Priming effect", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Halo effect", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Decoy effect", "decision_point": 2},
      {"instance_id": "cb_04", "bias": "Illusion of control", "decision_point": 2},
      {"instance_id": "cb_05", "bias": "Cognitive Dissonance", "decision_point": 3},
      {"instance_id": "cb_06", "bias": "Sunk Cost Bias", "decision_point": 3},
      {"instance_id": "cb_07", "bias": "Status Quo Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Priming effect",
        "mechanism": "Vivid demo content of one component establishes an evaluative frame applied to the whole library before independent review",
        "affected_reasoning_operation": "Framing of pilot-commitment evaluation criteria",
        "evidence_source": "Single demoed accordion component and general demo tone",
        "distinctiveness_requirement": "Must involve generalized framing/tone transfer, not a specific attribute inference (distinguishes it from cb_02)"
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "mechanism": "Positive impression of one demoed attribute (motion quality) and vendor reputation is used to infer quality of an unrelated, unverified attribute (contrast tokens)",
        "affected_reasoning_operation": "Cross-attribute quality inference",
        "evidence_source": "Vendor awards/reputation plus demoed accordion quality",
        "distinctiveness_requirement": "Must involve a specific unverified-attribute inference (contrast tokens), not general framing (distinguishes it from cb_01)"
      },
      {
        "instance_id": "cb_03",
        "bias": "Decoy effect",
        "mechanism": "An intentionally unattractive middle tier makes the higher tier seem disproportionately better by relative contrast rather than absolute value",
        "affected_reasoning_operation": "Comparative evaluation among three licensing options",
        "evidence_source": "Three-tier pricing/feature structure presented by vendor sales",
        "distinctiveness_requirement": "Reasoning must reference comparison against the decoy tier, not an independent cost-benefit calculation"
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "mechanism": "Overconfidence that personal oversight guarantees a timeline outcome despite dependence on uncontrolled external schedules",
        "affected_reasoning_operation": "Risk/timeline-setting judgment",
        "evidence_source": "Known but unconfirmed dependency on two other squads' release calendars",
        "distinctiveness_requirement": "Must center on control attribution over an uncertain external process, distinct from cb_03's comparative-value reasoning"
      },
      {
        "instance_id": "cb_05",
        "bias": "Cognitive Dissonance",
        "mechanism": "Disconfirming audit evidence is reinterpreted as atypical/peripheral to preserve consistency with an earlier public endorsement",
        "affected_reasoning_operation": "Interpretation/weighting of new evidence against a stated prior public position",
        "evidence_source": "Internal accessibility audit results contradicting the lead's earlier statement to the VP and squad leads",
        "distinctiveness_requirement": "Must involve belief-consistency reasoning tied to a prior public statement, distinct from cb_06's continuation-cost reasoning"
      },
      {
        "instance_id": "cb_06",
        "bias": "Sunk Cost Bias",
        "mechanism": "Continuation of customization work is justified by hours already spent rather than forward-looking assessment of new evidence and available fallback",
        "affected_reasoning_operation": "Continue-vs-abandon decision after disconfirming evidence",
        "evidence_source": "40+ hours already invested in LumenKit token customization; available legacy fallback",
        "distinctiveness_requirement": "Must reference backward-looking invested-effort justification, distinct from cb_05's belief-consistency justification, even though both occur at decision point 3"
      },
      {
        "instance_id": "cb_07",
        "bias": "Status Quo Bias",
        "mechanism": "Preference for the currently implemented arrangement over a comparably or better-assessed alternative (hybrid plan), justified by continuity/familiarity rather than merit",
        "affected_reasoning_operation": "Final selection among three rollout alternatives",
        "evidence_source": "Hybrid plan assessment showing it resolves known issues while preserving prior integration work",
        "distinctiveness_requirement": "Must reference preference for current arrangement's continuity, not cost already sunk (distinguishes it from cb_06) and not belief-consistency (distinguishes it from cb_05)"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Priming effect", "strength": "moderate"},
      {"instance_id": "cb_02", "bias": "Halo effect", "strength": "moderate"},
      {"instance_id": "cb_03", "bias": "Decoy effect", "strength": "moderate"},
      {"instance_id": "cb_04", "bias": "Illusion of control", "strength": "moderate"},
      {"instance_id": "cb_05", "bias": "Cognitive Dissonance", "strength": "moderate"},
      {"instance_id": "cb_06", "bias": "Sunk Cost Bias", "strength": "moderate"},
      {"instance_id": "cb_07", "bias": "Status Quo Bias", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Vendor demo framing order (autoselected, not activated)",
      "original_state": "Demo leads with flagship accordion component before token/contrast data",
      "changed_state": "Demo leads with raw contrast-ratio token data before the flagship component",
      "variables_to_hold_constant": [
        "Compliance deadline",
        "Licensing tier structure and pricing",
        "Squad dependencies and calendars",
        "Audit findings and timing",
        "Hours invested in customization"
      ]
    },
    "scenario_id": "IS_Biased_7",
    "domain_id": "IS",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across 4 decision points (2,2,2,1) based on mechanism fit: framing/inference biases (priming, halo) placed at the initial demo-driven commitment decision; comparative/control biases (decoy, illusion of control) placed at the licensing/timeline decision; consistency/continuation biases (cognitive dissonance, sunk cost) placed at the post-audit continuation decision; the pure continuity bias (status quo) placed alone at the final rollout decision. No decision point received more than one instance of the same bias; co-located biases at the same decision point were required to use distinct evidence sources and reasoning operations per the distinctiveness_requirement fields above.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Compliance deadline (10 weeks)",
      "Team headcount and resourcing",
      "Vendor identity (LumenKit) and its reputation",
      "Three-tier licensing structure",
      "Audit timing and findings",
      "Number and identity of dependent squads"
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
