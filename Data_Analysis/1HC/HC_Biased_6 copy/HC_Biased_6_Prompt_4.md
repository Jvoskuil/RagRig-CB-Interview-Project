Prompt 4 - Revision Prompt
You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{ }}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Ambiguity Bias", "occurrences": 1, "mechanism_constraint": "unresolved interpretation of ambiguous eligibility language resolved unilaterally toward preferred outcome"},
      {"bias": "Sunk Costs Bias", "occurrences": 1, "mechanism_constraint": "continued resource commitment justified by prior invested effort rather than current yield"},
      {"bias": "Representativeness", "occurrences": 1, "mechanism_constraint": "causal judgment driven by surface pattern match to a textbook vignette over base-rate/chart evidence"},
      {"bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "decision influenced by peer-site social proof rather than own-site performance data"},
      {"bias": "Framing Effect", "occurrences": 1, "mechanism_constraint": "wording choice for a compliance report driven by presentation order/valence of description rather than underlying facts"},
      {"bias": "Recency Bias", "occurrences": 1, "mechanism_constraint": "disproportionate weight given to the most recently encountered comparator case"}
    ],
    "target_bias_names": [
      "Ambiguity Bias",
      "Sunk Costs Bias",
      "Representativeness",
      "Bandwagon effect",
      "Framing Effect",
      "Recency Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Ambiguity Bias", "requested_occurrences": 1},
      {"bias": "Sunk Costs Bias", "requested_occurrences": 1},
      {"bias": "Representativeness", "requested_occurrences": 1},
      {"bias": "Bandwagon effect", "requested_occurrences": 1},
      {"bias": "Framing Effect", "requested_occurrences": 1},
      {"bias": "Recency Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "hc6_01", "bias": "Ambiguity Bias"},
      {"instance_id": "hc6_02", "bias": "Sunk Costs Bias"},
      {"instance_id": "hc6_03", "bias": "Bandwagon effect"},
      {"instance_id": "hc6_04", "bias": "Representativeness"},
      {"instance_id": "hc6_05", "bias": "Recency Bias"},
      {"instance_id": "hc6_06", "bias": "Framing Effect"}
    ],
    "intended_decision_points": [
      {"instance_id": "hc6_01", "bias": "Ambiguity Bias", "decision_point": 1},
      {"instance_id": "hc6_02", "bias": "Sunk Costs Bias", "decision_point": 2},
      {"instance_id": "hc6_03", "bias": "Bandwagon effect", "decision_point": 2},
      {"instance_id": "hc6_04", "bias": "Representativeness", "decision_point": 3},
      {"instance_id": "hc6_05", "bias": "Recency Bias", "decision_point": 3},
      {"instance_id": "hc6_06", "bias": "Framing Effect", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "hc6_01",
        "bias": "Ambiguity Bias",
        "mechanism": "Unilateral resolution of genuinely ambiguous eligibility wording toward the enrollment-favoring interpretation, without escalation or documentation",
        "affected_reasoning_operation": "Interpretation of underspecified eligibility criteria",
        "evidence_source": "Amended protocol text and PI unavailability at screening",
        "distinctiveness_requirement": "Sole ambiguity-resolution act in the interview; must not recur in decision points 2-4"
      },
      {
        "instance_id": "hc6_02",
        "bias": "Sunk Costs Bias",
        "mechanism": "Continued time allocation to an underperforming pathway justified by hours already invested rather than recent yield",
        "affected_reasoning_operation": "Resource-reallocation decision under prior investment",
        "evidence_source": "Prior 40 hours of pathway setup work and its low six-week yield",
        "distinctiveness_requirement": "Must be argued via 'effort already spent' language, distinct from hc6_03's peer-comparison language at the same decision point"
      },
      {
        "instance_id": "hc6_03",
        "bias": "Bandwagon effect",
        "mechanism": "Decision to persist with the pathway additionally driven by peer-site network reports of being 'ahead of pace,' independent of own-site data",
        "affected_reasoning_operation": "Weighting of social/peer proof versus own performance data",
        "evidence_source": "Coordinator-network newsletter describing peer-site progress",
        "distinctiveness_requirement": "Must be argued via peer/network reference language, distinct from hc6_02's sunk-effort language at the same decision point"
      },
      {
        "instance_id": "hc6_04",
        "bias": "Representativeness",
        "mechanism": "Causality lean determined by surface resemblance to a textbook AE vignette, with contrary chart evidence underweighted",
        "affected_reasoning_operation": "Diagnostic/causal categorization of an adverse event",
        "evidence_source": "Investigator brochure vignette compared to symptom presentation",
        "distinctiveness_requirement": "Must be argued via pattern-resemblance language, distinct from hc6_05's recency-of-report language at the same decision point"
      },
      {
        "instance_id": "hc6_05",
        "bias": "Recency Bias",
        "mechanism": "Disproportionate weight assigned to the peer-site AE report discussed the day before, over longer-standing chart evidence, due to its recency",
        "affected_reasoning_operation": "Integration of external comparator evidence into a causality judgment",
        "evidence_source": "Peer-site AE report discussed on a call the day before assessment",
        "distinctiveness_requirement": "Must be argued via temporal-recency language, distinct from hc6_04's pattern-resemblance language at the same decision point"
      },
      {
        "instance_id": "hc6_06",
        "bias": "Framing Effect",
        "mechanism": "Selection of milder compliance-report wording because it was presented first and sounds less consequential, despite factual equivalence of alternatives",
        "affected_reasoning_operation": "Selection of description/label for an ambiguous compliance event",
        "evidence_source": "Two PI-suggested, equally defensible descriptions of the same event",
        "distinctiveness_requirement": "Sole framing/labeling act in the interview; must not recur in decision points 1-3"
      }
    ],
    "intended_strength": [
      {"instance_id": "hc6_01", "bias": "Ambiguity Bias", "strength": "subtle"},
      {"instance_id": "hc6_02", "bias": "Sunk Costs Bias", "strength": "subtle"},
      {"instance_id": "hc6_03", "bias": "Bandwagon effect", "strength": "subtle"},
      {"instance_id": "hc6_04", "bias": "Representativeness", "strength": "subtle"},
      {"instance_id": "hc6_05", "bias": "Recency Bias", "strength": "subtle"},
      {"instance_id": "hc6_06", "bias": "Framing Effect", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Biased_6",
    "domain_id": "HC",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across 4 decision points by mechanism fit and narrative realism (DP1:1, DP2:2, DP3:2, DP4:1); no decision point contains two instances of the same bias; co-located instances (DP2, DP3) use distinct evidence sources and reasoning operations per the instance independence rule.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }}}
- Validation report: {{ }}

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
