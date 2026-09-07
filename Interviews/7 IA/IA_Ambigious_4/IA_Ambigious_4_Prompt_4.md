You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Wishful Thinking",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; correspondent-bank turnaround evidence must remain genuinely wide-ranging with no basis for an unwarranted favorable expectation to be identifiable."
      },
      {
        "bias": "Belief bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; the vendor report must disclose its own uncertainty and no prior working theory should exist for the analyst's conclusion to conveniently confirm."
      },
      {
        "bias": "Selective Attention Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; entity prioritization must be traceable to a comparably-weighted, articulable indicator rather than pattern familiarity from a prior case."
      },
      {
        "bias": "Planning fallacy",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; the time estimate must explicitly reference the historical range rather than rely solely on a best-case task sequence."
      }
    ],
    "target_bias_names": [
      "Wishful Thinking",
      "Belief bias",
      "Selective Attention Bias",
      "Planning fallacy"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Wishful Thinking", "requested_occurrences": 0 },
      { "bias": "Belief bias", "requested_occurrences": 0 },
      { "bias": "Selective Attention Bias", "requested_occurrences": 0 },
      { "bias": "Planning fallacy", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IA_Biased_4",
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Ambigious_4",
    "domain_id": "IA",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: control condition requires zero intended occurrences of all four target biases. No instance allocation was performed. All four decision points were instead constructed with intrinsically ambiguous, wide-ranging, or self-disclosed-uncertainty evidence so that no single reasoning act resolves into a biased mechanism, while preserving structural and vocabulary parity with the paired biased scenario IA_Biased_4.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and role (financial crime/threat intelligence analyst, FIU setting)",
      "Four-decision-point structure and analogous decision types (scoping, external report evaluation, pending external data, time estimation)",
      "Technical vocabulary set and constraint categories (filing deadline, correspondent delay, competing caseload, relationship and regulatory risk)",
      "Overall emotional tone and difficulty level",
      "Target word count and probe-plan structure"
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
