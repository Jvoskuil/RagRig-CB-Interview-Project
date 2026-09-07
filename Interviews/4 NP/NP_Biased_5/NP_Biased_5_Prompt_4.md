You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Similarity Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Habit Intrusion",
        "occurrences": 1,
        "mechanism_constraint": "human performance often can be captured by familiar behavioral patterns that occur so frequently in their experiences."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Recency Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Similarity Bias",
      "Habit Intrusion",
      "Bounded Rationality",
      "Recency Bias",
      "Imperfect Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Similarity Bias", "requested_occurrences": 1},
      {"bias": "Habit Intrusion", "requested_occurrences": 1},
      {"bias": "Bounded Rationality", "requested_occurrences": 1},
      {"bias": "Recency Bias", "requested_occurrences": 1},
      {"bias": "Imperfect Rationality", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "sb_01", "bias": "Similarity Bias"},
      {"instance_id": "hi_01", "bias": "Habit Intrusion"},
      {"instance_id": "rb_01", "bias": "Recency Bias"},
      {"instance_id": "br_01", "bias": "Bounded Rationality"},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality"}
    ],
    "intended_decision_points": [
      {"instance_id": "sb_01", "bias": "Similarity Bias", "decision_point": 1},
      {"instance_id": "hi_01", "bias": "Habit Intrusion", "decision_point": 2},
      {"instance_id": "rb_01", "bias": "Recency Bias", "decision_point": 3},
      {"instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 4},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sb_01",
        "bias": "Similarity Bias",
        "mechanism": "Applicability judged from surface resemblance between OE report equipment and local transmitter rather than confirmed technical equivalence",
        "affected_reasoning_operation": "Relevance/applicability judgment during evidence triage",
        "evidence_source": "OE report vs. local design change package",
        "distinctiveness_requirement": "Only instance of Similarity Bias; occurs solely at decision point 1 during initial OE triage, not repeated elsewhere"
      },
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "mechanism": "Well-practiced standard procedure-writing template is applied automatically instead of the new transmitter's specific requirements",
        "affected_reasoning_operation": "Action selection during procedure drafting",
        "evidence_source": "Design change package requirement vs. engineer's habitual template use",
        "distinctiveness_requirement": "Only instance of Habit Intrusion; occurs solely at decision point 2 during drafting, distinct from OE triage or data weighting"
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "mechanism": "Most recently encountered test result is disproportionately weighted as the representative baseline over more relevant older historical data",
        "affected_reasoning_operation": "Evidence weighting during validation-criteria setting",
        "evidence_source": "Five-year historical test data vs. two-week-old test result",
        "distinctiveness_requirement": "Only instance of Recency Bias; occurs solely at decision point 3 during data weighting, distinct from drafting or final judgment"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Information search terminated once readily accessible records seem minimally sufficient, under time and access constraints, rather than continuing an exhaustive search",
        "affected_reasoning_operation": "Information-gathering termination decision",
        "evidence_source": "Control room log and personal notes vs. inaccessible locked OE database",
        "distinctiveness_requirement": "Shares decision point 4 with ir_01 but addresses the search-termination operation, using a different evidence source (accessible records) and occurring earlier in the DP4 sequence than the final judgment"
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Final risk-acceptability judgment relies on a simplified holistic mental estimate rather than structured failure-mode-by-failure-mode analysis",
        "affected_reasoning_operation": "Final risk-acceptability synthesis prior to submission",
        "evidence_source": "Partial failure-mode documentation and engineer's own rough mental tally",
        "distinctiveness_requirement": "Shares decision point 4 with br_01 but addresses the final judgment-synthesis operation, occurring after the search-termination step and using the incomplete failure-mode list as its distinct evidence basis"
      }
    ],
    "intended_strength": [
      {"instance_id": "sb_01", "bias": "Similarity Bias", "strength": "subtle"},
      {"instance_id": "hi_01", "bias": "Habit Intrusion", "strength": "moderate"},
      {"instance_id": "rb_01", "bias": "Recency Bias", "strength": "subtle"},
      {"instance_id": "br_01", "bias": "Bounded Rationality", "strength": "moderate"},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Not applicable — no counterfactual condition requested",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_5",
    "domain_id": "NP",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences distributed across 4 decision points by mechanism fit and narrative realism: one bias per decision point at DPs 1-3 (Similarity Bias at OE triage, Habit Intrusion at drafting, Recency Bias at data weighting), with two distinct biases (Bounded Rationality, Imperfect Rationality) co-located at DP4 because both naturally arise under the same terminal time-pressured submission decision but target different reasoning operations (search termination vs. final judgment synthesis) with separate evidence sources, satisfying the same-bias co-location restriction and the distinct-evidence requirement.",
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
