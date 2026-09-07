You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Imperfect Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Imperfect Rationality",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Under concurrent cognitive load from a non-handoff competing task (surveillance pre-brief preparation) and ascension schedule pressure, CRS selects a familiar 'good enough' checklist response over full evaluation of accessible comparative vibration trend data, satisficing rather than optimizing the continue/hold decision.",
        "affected_reasoning_operation": "Evidence integration and option evaluation prior to a continue/hold decision",
        "evidence_source": "Plant computer historical vibration trend library (accessible but not consulted) versus prior similar-event checklist experience",
        "distinctiveness_requirement": "Must show that full evaluation was feasible (data accessible) and consciously foregone in favor of a familiar heuristic response, and that this occurs even absent a handoff obligation, distinguishing it from mere reasonable time-constrained prioritization tied specifically to turnover."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": "NP_Biased_1",
    "counterfactual_variable": {
      "name": "Presence of an imminent shift-turnover handoff obligation at decision point 3",
      "original_state": "Shift turnover approaching in ~45 minutes, requiring the CRS to draft and finalize a turnover brief for the oncoming crew concurrently with monitoring the vibration trend.",
      "changed_state": "No shift turnover during this window (turnover ~4 hours away); CRS instead prepares a time-boxed pre-brief for an unrelated scheduled surveillance test due in ~45 minutes, producing an equivalent-magnitude competing-task deadline without a handoff obligation.",
      "variables_to_hold_constant": [
        "Feedwater pump 1B vibration trend magnitude and timing",
        "Steam generator level oscillation event and its resolution",
        "Ascension schedule and power hold-point timing",
        "Staffing levels and on-call engineer availability",
        "Accessibility of the plant computer historical trend library",
        "Alternatives available at all four decision points",
        "Imperfect Rationality occurrence count, decision point, mechanism, and strength"
      ]
    },
    "scenario_id": "NP_Counterfactual_1",
    "domain_id": "NP",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to decision point 3, identical to the paired base scenario NP_Biased_1, per allocation rules 2 and 3, to isolate the effect of the counterfactual causal variable while holding the bias mechanism, decision point, and strength constant.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Feedwater pump 1B vibration trend magnitude and timing",
      "Steam generator level oscillation event and its resolution",
      "Ascension schedule and power hold-point timing",
      "Staffing levels and on-call engineer availability",
      "Accessibility of the plant computer historical trend library",
      "Alternatives available at all four decision points",
      "Imperfect Rationality occurrence count (1), decision point (3), mechanism, and strength"
    ],
    "generation_warnings": []
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
