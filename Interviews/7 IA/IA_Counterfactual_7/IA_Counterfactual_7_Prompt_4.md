You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {"bias": "Perceptual Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Wishful Thinking", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Belief bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Selective Attention Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Planning fallacy", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Authority Bias or Authority Obedience", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Framing effects", "occurrences": 1, "mechanism_constraint": null}
    ],
    "target_bias_names": [
      "Perceptual Bias",
      "Wishful Thinking",
      "Belief bias",
      "Selective Attention Bias",
      "Planning fallacy",
      "Authority Bias or Authority Obedience",
      "Framing effects"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Perceptual Bias", "requested_occurrences": 1},
      {"bias": "Wishful Thinking", "requested_occurrences": 1},
      {"bias": "Belief bias", "requested_occurrences": 1},
      {"bias": "Selective Attention Bias", "requested_occurrences": 1},
      {"bias": "Planning fallacy", "requested_occurrences": 1},
      {"bias": "Authority Bias or Authority Obedience", "requested_occurrences": 1},
      {"bias": "Framing effects", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Perceptual Bias"},
      {"instance_id": "cb_02", "bias": "Wishful Thinking"},
      {"instance_id": "cb_03", "bias": "Belief bias"},
      {"instance_id": "cb_04", "bias": "Selective Attention Bias"},
      {"instance_id": "cb_05", "bias": "Framing effects"},
      {"instance_id": "cb_06", "bias": "Planning fallacy"},
      {"instance_id": "cb_07", "bias": "Authority Bias or Authority Obedience"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Perceptual Bias", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Wishful Thinking", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Belief bias", "decision_point": 2},
      {"instance_id": "cb_04", "bias": "Selective Attention Bias", "decision_point": 2},
      {"instance_id": "cb_05", "bias": "Framing effects", "decision_point": 3},
      {"instance_id": "cb_06", "bias": "Planning fallacy", "decision_point": 3},
      {"instance_id": "cb_07", "bias": "Authority Bias or Authority Obedience", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Perceptual Bias",
        "mechanism": "Ambiguous documentary/photographic evidence interpreted as a clear pattern match to a pre-existing mental template, unaffected by the longer runway.",
        "affected_reasoning_operation": "Interpretation of raw evidence",
        "evidence_source": "Handwritten manifest fragment and container photo presented by walk-in",
        "distinctiveness_requirement": "Must be distinguished from cb_02 by focusing on interpretation of physical evidence, not on motivational confidence inflation; must show persistence despite added time."
      },
      {
        "instance_id": "cb_02",
        "bias": "Wishful Thinking",
        "mechanism": "Desire for the walk-in to be genuine (validating months of prior effort) inflates confidence in source veracity independent of the evidentiary read and independent of deadline length.",
        "affected_reasoning_operation": "Confidence estimation about source veracity",
        "evidence_source": "Officer's stated emotional reaction ('finally,' 'stroke of luck') and lack of independent vetting despite available time",
        "distinctiveness_requirement": "Must be distinguished from cb_01 by being a motivational/desirability effect on confidence, not a perceptual interpretation of documents."
      },
      {
        "instance_id": "cb_03",
        "bias": "Belief bias",
        "mechanism": "Logical validity of the access-explanation argument judged by conclusion desirability rather than argument structure, with an explicit asymmetric-standard cue, unaffected by available time to test the claim.",
        "affected_reasoning_operation": "Evaluation of explanatory argument validity",
        "evidence_source": "Walk-in's unverified claim of prior logistics role",
        "distinctiveness_requirement": "Must be distinguished from cb_04 by involving logical evaluation of an argument, not selective weighting of competing evidence streams."
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias",
        "mechanism": "Disproportionate elaboration of corroborating reporting versus minimal treatment of a genuinely contradicting technical-collection item, despite sufficient time to reconcile it.",
        "affected_reasoning_operation": "Evidence weighting/selection in drafting",
        "evidence_source": "Sub-source reporting vs. technical-collection port discrepancy and colleague's verbal concern",
        "distinctiveness_requirement": "Must be distinguished from cb_03 by involving relative attention across evidence streams, not evaluation of a single argument's logic."
      },
      {
        "instance_id": "cb_05",
        "bias": "Framing effects",
        "mechanism": "Same underlying probability estimate phrased to emphasize imminent-action likelihood rather than equivalent no-action likelihood, with an explicit fixed-estimate confirmation, independent of deadline length.",
        "affected_reasoning_operation": "Communication/presentation of a probabilistic judgment",
        "evidence_source": "Draft report wording choice for the uncertain shipment-timing estimate",
        "distinctiveness_requirement": "Must be distinguished from cb_06 by involving wording/presentation choice, not scheduling or duration estimation."
      },
      {
        "instance_id": "cb_06",
        "bias": "Planning fallacy",
        "mechanism": "Follow-on tasking timeline set on best-case assumptions despite known historical precedent of longer validation durations, and despite the extended runway comfortably permitting a historically realistic schedule.",
        "affected_reasoning_operation": "Prediction of task duration for follow-on tasking",
        "evidence_source": "Station's historical validation-sequence durations vs. compressed schedule set",
        "distinctiveness_requirement": "Must be distinguished from cb_05 by involving duration prediction, not communicative framing of probability."
      },
      {
        "instance_id": "cb_07",
        "bias": "Authority Bias or Authority Obedience",
        "mechanism": "Deference to branch chief's dissemination preference based on seniority/track record rather than independent re-evaluation of the unresolved discrepancy, unaffected by the additional available time.",
        "affected_reasoning_operation": "Final decision on caveat strength and dissemination timing",
        "evidence_source": "Branch chief's stated preference and unresolved technical-collection discrepancy from decision point 2",
        "distinctiveness_requirement": "Sole instance of this bias; no additional co-located instance required."
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Perceptual Bias", "strength": "moderate"},
      {"instance_id": "cb_02", "bias": "Wishful Thinking", "strength": "moderate"},
      {"instance_id": "cb_03", "bias": "Belief bias", "strength": "subtle"},
      {"instance_id": "cb_04", "bias": "Selective Attention Bias", "strength": "moderate"},
      {"instance_id": "cb_05", "bias": "Framing effects", "strength": "subtle"},
      {"instance_id": "cb_06", "bias": "Planning fallacy", "strength": "moderate"},
      {"instance_id": "cb_07", "bias": "Authority Bias or Authority Obedience", "strength": "moderate"}
    ],
    "paired_scenario_id": "IA_Biased_7",
    "counterfactual_variable": {
      "name": "Length of the time window before the fixed policy briefing (deadline pressure)",
      "original_state": "36-hour window before the briefing, narrowing to roughly 14 hours by the uncertainty-framing/scheduling decision",
      "changed_state": "Five-day window before the briefing, narrowing to roughly four days by the same decision point",
      "variables_to_hold_constant": [
        "The walk-in's identity, claims, and presented documents",
        "The existing months-long network hypothesis",
        "The technical-collection port discrepancy and its timing relative to the coordination call",
        "The colleague's verbal flag of the discrepancy",
        "The branch chief's identity, track record, and stated preference for prompt dissemination",
        "The four-decision-point structure and sequence",
        "The eventual mismatch between reported timing and observed shipment activity"
      ]
    },
    "scenario_id": "IA_Counterfactual_7",
    "domain_id": "IA",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across 4 decision points with two co-located pairs (DP1: cb_01/cb_02; DP2: cb_03/cb_04; DP3: cb_05/cb_06) and one singleton (DP4: cb_07), mirroring the paired biased scenario's allocation exactly so that only the deadline-length variable differs. Each co-located pair retains distinct evidence sources and distinct reasoning operations per the separation rule; assignment prioritized mechanism fit to the HUMINT reporting workflow (triage, cross-source evaluation, drafting/communication, senior-review deference) over arbitrary spread, and each instance additionally documents that the mechanism persists despite the extended timeline.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "The walk-in's identity, claims, and presented documents",
      "The existing months-long network hypothesis",
      "The technical-collection port discrepancy and its timing relative to the coordination call",
      "The colleague's verbal flag of the discrepancy",
      "The branch chief's identity, track record, and stated preference for prompt dissemination",
      "The four-decision-point structure and sequence",
      "The eventual mismatch between reported timing and observed shipment activity"
    ],
    "generation_warnings": [
      "Because the counterfactual deliberately extends available time while preserving all seven bias mechanisms unchanged, the interview must show explicit textual evidence that the officer's reasoning persisted despite having a genuine opportunity to use the extra time differently; without such evidence, an independent validator could misattribute the biased patterns to residual, unacknowledged time pressure rather than to the underlying cognitive mechanisms. Each occurrence embedding plan entry has been constrained to require an explicit 'despite having time available' or equivalent textual cue to mitigate this risk."
    ]
  }}}
- Validation report: {{VALIDATION_REPORT}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
