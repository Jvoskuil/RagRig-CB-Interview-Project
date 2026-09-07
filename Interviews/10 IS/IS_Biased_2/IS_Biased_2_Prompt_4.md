You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Irrational Escalation",
        "occurrences": 1,
        "mechanism_constraint": "Must be justified via prior sunk time/effort/expertise, not forward-looking cost-benefit reasoning"
      },
      {
        "bias": "Negativity Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve disproportionate weight on one vivid recent negative event versus a larger body of mixed/positive evidence"
      }
    ],
    "target_bias_names": [
      "Irrational Escalation",
      "Negativity Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Irrational Escalation",
        "requested_occurrences": 1
      },
      {
        "bias": "Negativity Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "decision_point": 2
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "mechanism": "Continued investment decision justified by prior sunk effort (eight months, three patch cycles, internal expertise) rather than forward-looking expected value of the alternative solution",
        "affected_reasoning_operation": "Resource-allocation choice under uncertainty",
        "evidence_source": "History of QuickCache development effort and prior patch outcomes versus profiling-based redesign recommendation",
        "distinctiveness_requirement": "Single instance at decision point 2 only; must not be repeated as a restated example, follow-up probe answer, or outcome explanation elsewhere in the interview"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "mechanism": "Disproportionate weight given to one recent, vivid negative event (Dev's outage) relative to a longer positive track record and a comparably negative but less salient pattern from another engineer (Marcus's missed deadlines)",
        "affected_reasoning_operation": "Personnel-risk assessment feeding a task-assignment decision",
        "evidence_source": "Incident postmortem and eighteen-month performance history for Dev, contrasted with Marcus's deadline record",
        "distinctiveness_requirement": "Single instance at decision point 3 only; must not be repeated as a restated example, follow-up probe answer, or outcome explanation elsewhere in the interview"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "strength": "subtle"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
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
    "scenario_id": "IS_Biased_2",
    "domain_id": "IS",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences were spread across distinct decision points (Irrational Escalation at decision point 2, Negativity Bias at decision point 3) chosen for mechanism fit and narrative realism within a single continuous incident; decision points 1 and 4 were kept clean to avoid unintended bias density and to preserve plausible non-bias explanations at every decision point.",
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
