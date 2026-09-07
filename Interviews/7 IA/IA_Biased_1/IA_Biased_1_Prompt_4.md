You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Complacency Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Complacency Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Complacency Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias",
        "mechanism": "Reliance on a long track record of stability to justify sustained low vigilance and forgone verification effort at the point of synthesizing newly converging multi-INT indicators, rather than treating the convergence itself as a trigger for renewed scrutiny.",
        "affected_reasoning_operation": "Evidence synthesis and confidence calibration during final judgment formation for the warning board",
        "evidence_source": "Combined imagery (Phase 1), SIGINT (Phase 2), and liaison convoy (Phase 3) indicators viewed together for the first time in Phase 4, against the backdrop of three years of prior steady-state assessments",
        "distinctiveness_requirement": "This is the only planned Complacency Bias instance; it must be identifiable specifically at the synthesis/final-judgment stage and must not be a restatement of the individual handling decisions in Phases 1-3, which are evidentiary setup rather than counted instances."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_1",
    "domain_id": "IA",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the strongest mechanism fit and narrative realism: the final synthesis/recommendation decision (Phase 4), where prior track-record reliance most plausibly suppresses appropriate re-evaluation of newly converging evidence. Phases 1-3 were designed to supply the necessary evidentiary buildup without themselves constituting counted instances, per the exact-occurrence rule limiting the bias to one independently identifiable manifestation.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
