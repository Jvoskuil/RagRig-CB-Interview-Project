You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Authority Bias or Higher-level prioritization Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; S3's compliance with brigade must be accompanied by formal escalation and negotiated parallel risk mitigation, not source-weighted deference."
      },
      {
        "bias": "Hindsight Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; retrospective account must explicitly preserve the real-time uncertainty that existed before the outcome was known."
      },
      {
        "bias": "Representativeness Heuristic",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; the location deviation from the enemy template must be actively investigated rather than discounted by categorical resemblance."
      },
      {
        "bias": "Status Quo Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; retention or modification of the crossing plan must be justified by explicit comparison of risk-mitigation options, not by incumbency alone."
      },
      {
        "bias": "Groupthink",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; any staff disagreement about the bridge report must be voiced and discussed openly rather than suppressed or self-censored."
      }
    ],
    "target_bias_names": [
      "Authority Bias or Higher-level prioritization Bias",
      "Hindsight Bias",
      "Representativeness Heuristic",
      "Status Quo Bias",
      "Groupthink"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Authority Bias or Higher-level prioritization Bias", "requested_occurrences": 0 },
      { "bias": "Hindsight Bias", "requested_occurrences": 0 },
      { "bias": "Representativeness Heuristic", "requested_occurrences": 0 },
      { "bias": "Status Quo Bias", "requested_occurrences": 0 },
      { "bias": "Groupthink", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MD_Biased_5",
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Vocab_Control_5",
    "domain_id": "MD",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: vocabulary_control condition requires zero intended instances of all named biases. Decision points are matched one-to-one to the paired biased scenario's four phases (scout sighting, brigade directive, bridge-report planning session, after-action reflection) for structural and vocabulary parity, with each phase's reasoning rewritten to demonstrate balanced, evidence-weighed deliberation instead of the paired scenario's intended bias mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Operational objective (secure Route BLUE crossing within 48-hour brigade synchronization window)",
      "Setting, constraints, and equipment (single MGB, weather-limited ISR, unreconned alternate ford)",
      "Actors and roles (S3, S2, battalion engineer, brigade S3, company commanders)",
      "Four-decision-point chronology and phase content (scout sighting, brigade directive, bridge-classification session, after-action review)",
      "Domain vocabulary and technical terminology",
      "Interview format, difficulty, and emotional tone",
      "Approximate target word count (1,350 words, range 1,215-1,485)"
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
