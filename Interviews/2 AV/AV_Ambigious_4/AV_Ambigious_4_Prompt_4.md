You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Bias Blind Spot",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Normalcy Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Experience Bias or Trusting expert intuition",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      }
    ],
    "target_bias_names": [
      "Bias Blind Spot",
      "Normalcy Bias",
      "Experience Bias or Trusting expert intuition",
      "Illusion of validity"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bias Blind Spot", "requested_occurrences": 0 },
      { "bias": "Normalcy Bias", "requested_occurrences": 0 },
      { "bias": "Experience Bias or Trusting expert intuition", "requested_occurrences": 0 },
      { "bias": "Illusion of validity", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "AV_Biased_4",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Ambigious_4",
    "domain_id": "AV",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, so no bias instances are planned. Decision points are instead structured to mirror the paired biased scenario's mechanism-fit locations (dispatch acceptance, in-flight advisory response, evaluative grading, post-flight reflection) while each is written to remain genuinely underdetermined between a defensible judgment and a less careful one, without resolving into any target bias mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and role (aviation, Check Airman/TRE)",
      "Setting (Line Check/OPC on a senior widebody captain, revenue flight)",
      "Four-decision-point structure and ordering",
      "Stakeholder roster and interaction pattern",
      "Technical vocabulary level and terminology set",
      "Difficulty level (challenging) and approximate word count",
      "Dialogue format and emotional tone"
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
