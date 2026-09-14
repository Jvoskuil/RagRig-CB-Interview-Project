You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "False memory",
        "occurrences": 0,
        "mechanism_constraint": "Control condition: no intended instance embedded. Paired biased scenario HE_Biased_2 specifies 1 occurrence for this bias."
      },
      {
        "bias": "Familiarity bias",
        "occurrences": 0,
        "mechanism_constraint": "Control condition: no intended instance embedded. Paired biased scenario HE_Biased_2 specifies 1 occurrence for this bias."
      }
    ],
    "target_bias_names": [
      "False memory",
      "Familiarity bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "False memory",
        "requested_occurrences": 0
      },
      {
        "bias": "Familiarity bias",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "HE_Biased_2",
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Ambigious_2",
    "domain_id": "HE",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, which requires zero intended instances of all named target biases regardless of any occurrence counts supplied for the paired biased scenario. No allocation across decision points was performed since no instances are planned.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Building type and layout (mixed-use café/apartment)",
      "Fire scenario structure and physical evidence types",
      "Four-decision-point sequence and sequencing logic",
      "Stakeholder cast (owner, adjuster, marshal, utility inspector, two witnesses)",
      "Time-pressure and resource-constraint framing",
      "Professional tone and difficulty level (subtle)",
      "Target word count (1,350 words, range 1,215-1,485)"
    ],
    "generation_warnings": [
      "The supplied exact-occurrence manifest lists False memory=1 and Familiarity bias=1, but the supplied condition for this scenario is ambiguous_control. Per CONDITION RULES, ambiguous_control requires zero intended instances of all named biases. The manifest values were therefore treated as the target set for the paired biased scenario (HE_Biased_2) only, and zero instances of False memory or Familiarity bias were planned or embedded in HE_Ambigious_2. This is not a reduction of a requested count within the biased condition; it is the correct application of the control-condition rule to a manifest that describes the paired experimental factor.",
      "Because zero occurrences are planned, occurrence_embedding_plan_internal, planned_instance_ids, intended_decision_points, intended_mechanisms, and intended_strength are intentionally empty arrays for this scenario."
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
