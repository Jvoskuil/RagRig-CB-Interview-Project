You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Wishful Thinking",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an unsupported expectation of a favorable outcome (records arriving in time) with no confirming evidence and contrary historical base rate."
      },
      {
        "bias": "Belief bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as accepting an argument's conclusion because it matches prior belief, while failing to evaluate the argument's logical/evidentiary validity despite an explicit flag."
      },
      {
        "bias": "Selective Attention Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as attention allocation driven by pattern familiarity, with a non-matching but relevant entity deprioritized without independent evaluation."
      },
      {
        "bias": "Planning fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a time estimate derived from a best-case task sequence that disregards known historical base rates and competing demands."
      }
    ],
    "target_bias_names": [
      "Wishful Thinking",
      "Belief bias",
      "Selective Attention Bias",
      "Planning fallacy"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Wishful Thinking", "requested_occurrences": 1 },
      { "bias": "Belief bias", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias", "requested_occurrences": 1 },
      { "bias": "Planning fallacy", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias" },
      { "instance_id": "bb_01", "bias": "Belief bias" },
      { "instance_id": "wt_01", "bias": "Wishful Thinking" },
      { "instance_id": "pf_01", "bias": "Planning fallacy" }
    ],
    "intended_decision_points": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias", "decision_point": 1 },
      { "instance_id": "bb_01", "bias": "Belief bias", "decision_point": 2 },
      { "instance_id": "wt_01", "bias": "Wishful Thinking", "decision_point": 3 },
      { "instance_id": "pf_01", "bias": "Planning fallacy", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sab_01",
        "bias": "Selective Attention Bias",
        "mechanism": "Attention allocated to pattern-matching entity (shared registered agent), non-matching relevant entity deprioritized without independent risk evaluation",
        "affected_reasoning_operation": "Evidence-selection / initial scoping",
        "evidence_source": "Alert batch metadata: registered-agent match vs. unrelated logistics counterparty",
        "distinctiveness_requirement": "Must be tied to the scoping act at intake, distinct in evidence source and moment from the belief-bias instance at decision point 2, which concerns argument evaluation rather than attention allocation."
      },
      {
        "instance_id": "bb_01",
        "bias": "Belief bias",
        "mechanism": "Conclusion-driven acceptance of vendor argument despite unverified premise flagged by a colleague",
        "affected_reasoning_operation": "Argument evaluation / evidence weighting",
        "evidence_source": "OSINT vendor report and colleague's flag on entity-matching validity",
        "distinctiveness_requirement": "Distinct reasoning operation (validity assessment of an argument) and evidence source (vendor report) from the attention-allocation act in decision point 1."
      },
      {
        "instance_id": "wt_01",
        "bias": "Wishful Thinking",
        "mechanism": "Unsupported expectation that outstanding records arrive in time, contrary to historical turnaround data, driving a delay in contingency drafting",
        "affected_reasoning_operation": "Prediction / risk forecasting",
        "evidence_source": "Correspondent bank historical turnaround record and absence of confirmation",
        "distinctiveness_requirement": "Distinct from bb_01 and sab_01 in that it concerns forecasting a future event under uncertainty rather than evaluating past evidence or allocating attention."
      },
      {
        "instance_id": "pf_01",
        "bias": "Planning fallacy",
        "mechanism": "Best-case task-sequence estimate ignoring historical base rate and competing caseload",
        "affected_reasoning_operation": "Time/effort estimation",
        "evidence_source": "Historical base rate for comparable cases and current competing case list",
        "distinctiveness_requirement": "Distinct from wt_01 in that it concerns a self-generated task-duration estimate rather than an expectation about an external party's action."
      }
    ],
    "intended_strength": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias", "strength": "subtle" },
      { "instance_id": "bb_01", "bias": "Belief bias", "strength": "moderate" },
      { "instance_id": "wt_01", "bias": "Wishful Thinking", "strength": "moderate" },
      { "instance_id": "pf_01", "bias": "Planning fallacy", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_4",
    "domain_id": "IA",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias assigned to a distinct decision point (1:1 mapping across the 4 decision points), chosen for mechanism fit: attention/scoping at intake (DP1), argument evaluation of external evidence (DP2), forecasting under uncertainty (DP3), and self-estimation of task duration (DP4). No bias shares a decision point, so the 'two occurrences at one decision point' distinctiveness rule was not triggered.",
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
