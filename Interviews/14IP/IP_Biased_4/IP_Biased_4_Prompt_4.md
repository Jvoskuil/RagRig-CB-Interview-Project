You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Fundamental Attribution Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dispositional attribution (Marco's character/skill) overriding an available situational cause (lubrication interval change) at decision point 1 only."
      },
      {
        "bias": "Gambler's Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as treating independent failure events as sequentially dependent ('due for a clean run') at decision point 2 only."
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overestimating personal skill's ability to determine a diagnostically uncertain outcome at decision point 3 only."
      },
      {
        "bias": "Ambiguity effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as avoidance of the option with unknown/ambiguous probability information in favor of a known-but-worse option at decision point 4 only."
      }
    ],
    "target_bias_names": [
      "Fundamental Attribution Bias",
      "Gambler's Fallacy",
      "Illusion of control",
      "Ambiguity effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Fundamental Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Gambler's Fallacy", "requested_occurrences": 1 },
      { "bias": "Illusion of control", "requested_occurrences": 1 },
      { "bias": "Ambiguity effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias" },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy" },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control" },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias", "decision_point": 1 },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy", "decision_point": 2 },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control", "decision_point": 3 },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "IP_Biased_4_FAB_01",
        "bias": "Fundamental Attribution Bias",
        "mechanism": "Dispositional attribution of failure to Marco's personal technique/character rather than the shared situational lubrication-interval change.",
        "affected_reasoning_operation": "Causal attribution during root cause diagnosis",
        "evidence_source": "Maintenance PM record, lubrication interval change log",
        "distinctiveness_requirement": "Only intended instance of this bias; must not recur as a summary or outcome explanation later in the interview."
      },
      {
        "instance_id": "IP_Biased_4_GF_01",
        "bias": "Gambler's Fallacy",
        "mechanism": "Belief that a streak of independent failures makes the next outcome more likely to be favorable, absent any causal dependency.",
        "affected_reasoning_operation": "Prediction of near-term equipment reliability",
        "evidence_source": "Failure interval history, statistical independence of proximate causes across the three failures",
        "distinctiveness_requirement": "Must use failure-streak reasoning distinct from the attribution reasoning in decision point 1; no overlap in evidence source."
      },
      {
        "instance_id": "IP_Biased_4_IOC_01",
        "bias": "Illusion of control",
        "mechanism": "Overestimation of personal skill's capacity to guarantee a correct outcome despite unresolved diagnostic uncertainty and tightened external tolerance standards.",
        "affected_reasoning_operation": "Selection of repair method and self-assessed confidence in outcome control",
        "evidence_source": "Specialist recommendation, current alignment tolerance standard, engineer's self-reported track record",
        "distinctiveness_requirement": "Distinct from ambiguity effect at decision point 4: this instance concerns confidence in personal action, not comparison of two probability-labeled options."
      },
      {
        "instance_id": "IP_Biased_4_AE_01",
        "bias": "Ambiguity effect",
        "mechanism": "Avoidance of the OEM option due to its unknown/ambiguous success probability, favoring a known-but-inferior legacy option.",
        "affected_reasoning_operation": "Choice between two repair options under differing information quality",
        "evidence_source": "OEM vendor claims (no specific failure-rate data), legacy bearing's documented failure history",
        "distinctiveness_requirement": "Distinct from illusion of control at decision point 3: this instance concerns comparative evaluation of two options' probability information, not personal-control belief."
      }
    ],
    "intended_strength": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Biased_4",
    "domain_id": "IP",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism per allocation rules 1-4; no decision point received more than one bias instance, so the shared-decision-point distinctiveness rule was not triggered.",
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
