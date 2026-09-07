You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Automation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as deference to ARPA's aggregate risk ranking over a conflicting independent lookout report, at Decision Point 2 only."
      },
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as risk estimation anchored to a vividly recalled prior incident rather than current plotted data, at Decision Point 3 only."
      }
    ],
    "target_bias_names": ["Automation Bias", "Availability Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Automation Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "ab_01", "bias": "Automation Bias"},
      {"instance_id": "av_01", "bias": "Availability Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "ab_01", "bias": "Automation Bias", "decision_point": 2},
      {"instance_id": "av_01", "bias": "Availability Bias", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "mechanism": "Deference to ARPA's aggregate target-ranking output over a conflicting independent visual/lookout signal, delaying escalation to manual plotting or avoidance action.",
        "affected_reasoning_operation": "Risk prioritization / escalation decision",
        "evidence_source": "ARPA target list and alarm threshold vs. lookout's visual report of erratic small-craft movement",
        "distinctiveness_requirement": "Must be textually distinct from av_01 by involving system-output deference rather than recalled-incident salience, and must occur only at Decision Point 2."
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Risk probability estimate for the fishing cluster driven by ease of recall and vividness of a recent bulletin incident rather than current plotted spacing/closing-rate data, causing temporary under-attention to the bulk carrier's tightening CPA.",
        "affected_reasoning_operation": "Probability estimation and attention allocation across concurrent contacts",
        "evidence_source": "Recalled bulletin narrative vs. current radar plot of fishing cluster and bulk carrier CPA/TCPA",
        "distinctiveness_requirement": "Must be textually distinct from ab_01 by involving recalled-incident salience rather than system-output deference, and must occur only at Decision Point 3."
      }
    ],
    "intended_strength": [
      {"instance_id": "ab_01", "bias": "Automation Bias", "strength": "moderate"},
      {"instance_id": "av_01", "bias": "Availability Bias", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence/vividness of the recent safety-bulletin near-miss narrative (autoselected; not activated under the biased condition)",
      "original_state": "Bulletin exists and is vivid/recently discussed",
      "changed_state": "not_applicable_condition_is_biased",
      "variables_to_hold_constant": [
        "Vessel type and passage route",
        "Weather sequence",
        "Contact kinematics",
        "Watch composition",
        "Decision count and structure"
      ]
    },
    "scenario_id": "MO_Biased_2",
    "domain_id": "MO",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread one-per-bias across two distinct decision points (2 and 3), chosen for mechanism fit: Automation Bias tied to system-output deference during active target tracking, Availability Bias tied to recalled-incident salience during a spatially/thematically matching hazard (fishing cluster near the bulletin's waypoint). Decision Points 1 and 4 left free of intentional bias instances to preserve narrative realism and avoid over-saturation.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vessel type, route, and TSS constraints",
      "Weather/squall sequence",
      "Number and identity of contacts (fishing boat, fishing cluster, bulk carrier)",
      "Watch composition (single OOW plus lookout, Master on standby)",
      "Four-decision-point structure and probe set"
    ],
    "generation_warnings": []
  }}}
- Validation report: {{}}

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
