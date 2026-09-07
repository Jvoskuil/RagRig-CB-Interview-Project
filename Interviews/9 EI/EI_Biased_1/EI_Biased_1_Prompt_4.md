You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Averaging Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as unweighted arithmetic averaging of evidentiary inputs with materially different reliability/comparability, not as a stated preference or generic heuristic mention."
      }
    ],
    "target_bias_names": [
      "Averaging Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Averaging Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "mechanism": "Unweighted arithmetic averaging of four evidentiary inputs (standardized diagnostic percentile, unverified transcript conversion, single classroom quiz grade, subjective self-report) despite their differing reliability, producing a composite figure used directly for the placement decision.",
        "affected_reasoning_operation": "Evidence integration/aggregation across heterogeneous sources",
        "evidence_source": "Diagnostic test score, transcript-derived GPA equivalent, single observation quiz grade, self-report confidence survey",
        "distinctiveness_requirement": "The manifestation must show the participant applying equal weight to sources of visibly different reliability, with no stated differentiation rationale, distinguishing it from a merely incorrect but justified composite methodology."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of an explicit department weighting protocol at the composite-scoring decision point",
      "original_state": "No explicit weighting guidance exists; teacher defaults to unweighted averaging of the four inputs.",
      "changed_state": "Department chair provides an explicit rubric prioritizing the standardized diagnostic test (at least 50% weight) over the other three sources.",
      "variables_to_hold_constant": [
        "Student identity, transcript content, and diagnostic/observation/self-report values",
        "Scheduling deadline and time pressure",
        "Decision points 1, 3, and 4 and their outcomes",
        "Stakeholders and their roles",
        "Word count and interview structure"
      ]
    },
    "scenario_id": "EI_Biased_1",
    "domain_id": "EI",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the clearest mechanism fit for Averaging Bias (composite scoring from heterogeneous evidence sources) and the greatest narrative realism within a high school placement workflow; remaining three decision points intentionally left free of any named bias per exact-occurrence rules.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Student identity, transcript content, and diagnostic/observation/self-report values",
      "Scheduling deadline and time pressure",
      "Decision points 1, 3, and 4 and their outcomes",
      "Stakeholders and their roles",
      "Word count and interview structure"
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
