You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Gamblers Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must involve reasoning about an upcoming independent artillery/mortar round based on prior round outcomes"
      },
      {
        "bias": "Ingroup Preference bias or In-group bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve differential weighting of two evidence sources based on unit affiliation rather than evidentiary quality"
      },
      {
        "bias": "Optimism bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve underestimating risk of a specific mission element based on a recent favorable track record"
      },
      {
        "bias": "Base-rate neglect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve disregarding sector-level or sensor-level prior probability in favor of a single specific cue"
      }
    ],
    "target_bias_names": [
      "Gamblers Fallacy",
      "Ingroup Preference bias or In-group bias",
      "Optimism bias",
      "Base-rate neglect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Gamblers Fallacy", "requested_occurrences": 1 },
      { "bias": "Ingroup Preference bias or In-group bias", "requested_occurrences": 1 },
      { "bias": "Optimism bias", "requested_occurrences": 1 },
      { "bias": "Base-rate neglect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy" },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias" },
      { "instance_id": "ob_01", "bias": "Optimism bias" },
      { "instance_id": "brn_01", "bias": "Base-rate neglect" }
    ],
    "intended_decision_points": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy", "decision_point": 1 },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias", "decision_point": 2 },
      { "instance_id": "ob_01", "bias": "Optimism bias", "decision_point": 3 },
      { "instance_id": "brn_01", "bias": "Base-rate neglect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "gf_01",
        "bias": "Gamblers Fallacy",
        "mechanism": "Belief that an independent fire-mission outcome is 'due' to succeed after consecutive misses, rather than treating each round independently",
        "affected_reasoning_operation": "Probabilistic forecasting of an independent event",
        "evidence_source": "Sequence of two prior adjustment-round outcomes",
        "distinctiveness_requirement": "Only bias-relevant instance tied to sequential round outcomes; must not overlap with any other instance's evidence"
      },
      {
        "instance_id": "ig_01",
        "bias": "Ingroup Preference bias or In-group bias",
        "mechanism": "Preferential trust in a report because it originates from the observer's own unit/service rather than on evidentiary merit",
        "affected_reasoning_operation": "Comparative weighting of two competing target-location reports",
        "evidence_source": "Battalion JTAC report vs. partner-force liaison report",
        "distinctiveness_requirement": "Only instance involving cross-unit evidence comparison; distinct evidence source and decision point from gf_01"
      },
      {
        "instance_id": "ob_01",
        "bias": "Optimism bias",
        "mechanism": "Underweighting risk indicators (tight margin, comms dropout) because of a recent favorable track record with the same asset",
        "affected_reasoning_operation": "Forward-looking risk/outcome forecasting for a danger-close CAS run",
        "evidence_source": "Recent squadron strike history plus current margin/comms conditions",
        "distinctiveness_requirement": "Only instance concerning forecast confidence about mission execution risk; independent of ig_01 and brn_01 evidence"
      },
      {
        "instance_id": "brn_01",
        "bias": "Base-rate neglect",
        "mechanism": "Approving action based on one specific-case cue while ignoring known low prior probability of true positives in this sector/sensor combination",
        "affected_reasoning_operation": "Belief updating on target identification given prior probability and single-case evidence",
        "evidence_source": "Sector activity history and sensor false-positive history vs. single sensor cue",
        "distinctiveness_requirement": "Only instance involving prior-probability neglect in target identification; final decision point"
      }
    ],
    "intended_strength": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy", "strength": "subtle" },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias", "strength": "subtle" },
      { "instance_id": "ob_01", "bias": "Optimism bias", "strength": "subtle" },
      { "instance_id": "brn_01", "bias": "Base-rate neglect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Biased_4",
    "domain_id": "MD",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism per rules 1-4; no decision point hosts more than one instance of any bias.",
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
