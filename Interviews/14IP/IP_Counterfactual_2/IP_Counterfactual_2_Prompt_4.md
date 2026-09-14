You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Correlation bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as causal attribution from temporal co-occurrence (temperature vs. dimension drift) while an equally available alternative (material lot) is not tested with equivalent rigor, and must persist without reliance on the (now absent) engineer's corroborating anecdote"
      },
      {
        "bias": "Conservatism Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as insufficient belief revision toward tool wear despite strong new quantitative sensor evidence, anchored to an earlier 'tool recently replaced' assumption; unaffected by the counterfactual variable"
      }
    ],
    "target_bias_names": [
      "Correlation bias",
      "Conservatism Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Correlation bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Conservatism Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "decision_point": 2
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "mechanism": "Causal inference drawn from temporal co-movement of temperature and dimensional drift, with a comparably available material-lot explanation left untested at the same rigor level; in this variant the inference must be shown to rest on timing alone, since no corroborating anecdote is available",
        "affected_reasoning_operation": "Causal attribution and evidence-selection during root-cause hypothesis formation",
        "evidence_source": "Temperature log and material lot traveler, both available within the same investigative window; engineer's statement now disclaims prior precedent rather than confirming it",
        "distinctiveness_requirement": "This is the only planned correlation-bias instance; it must not be repeated as a second independent occurrence elsewhere, and it must not be weakened into non-occurrence merely because the anecdote is absent"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "mechanism": "Underweighting of new tool-wear sensor evidence (78% of rated life) relative to a prior belief ('tool recently replaced, unlikely worn'), resulting in a corrective action smaller than the updated evidence would justify",
        "affected_reasoning_operation": "Belief updating and proportionality of response magnitude to new evidence at decision point 3",
        "evidence_source": "Tool wear sensor reading and prior stated assumption about tool age",
        "distinctiveness_requirement": "This is the only planned conservatism-bias instance; unaffected by the counterfactual variable and must remain structurally identical to the base scenario's instance"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "strength": "moderate"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": "IP_Biased_2",
    "counterfactual_variable": {
      "name": "Presence of the process engineer's corroborating anecdote about prior temperature-linked drift on this machine",
      "original_state": "Engineer confirms he has seen temperature swings cause drift on this machine before",
      "changed_state": "Engineer states he has not previously seen this pattern on this machine",
      "variables_to_hold_constant": [
        "QA analyst role and objective",
        "Four decision points and their order",
        "Temperature rise magnitude and timing (3°C over two hours)",
        "Material lot loading timing and traveler lag",
        "Tool wear sensor readings (78% then 91%)",
        "Cpk decline (1.42 to 1.05)",
        "Offset-adjustment decision and outcome",
        "Incoming operator's report of unusual tool sound",
        "Final tool-change and deviation-report decision",
        "Post-hoc material lot hardness result (in spec)",
        "Post-tool-change return to baseline"
      ]
    },
    "scenario_id": "IP_Counterfactual_2",
    "domain_id": "IP",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias, mirroring the base scenario's allocation: correlation bias at decision point 2 (root-cause hypothesis formation) and conservatism bias at decision point 3 (halt/continue decision), preserved unchanged across the counterfactual manipulation. Only the engineer's anecdote at decision point 2 was altered as the causal variable; no reallocation across decision points was needed since neither bias's mechanism fit changed as a result.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "QA analyst role, objective, and constraints",
      "Four decision points and their sequence",
      "Temperature rise magnitude and timing",
      "Material lot loading timing and traveler lag",
      "Tool wear sensor readings and Cpk figures",
      "Offset-adjustment decision and its failure to hold",
      "Incoming operator's report of unusual tool sound",
      "Final tool-change and deviation-report recommendation",
      "Post-hoc material lot hardness result",
      "Post-tool-change return to baseline"
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
