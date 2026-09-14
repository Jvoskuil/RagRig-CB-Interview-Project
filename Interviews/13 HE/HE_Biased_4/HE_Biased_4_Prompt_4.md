You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusion of Truth effect",
        "occurrences": 1,
        "mechanism_constraint": "Repetition of an identical unverified claim across multiple documents from a single underlying source, mistaken for independent corroboration."
      },
      {
        "bias": "Action bias",
        "occurrences": 1,
        "mechanism_constraint": "Preference for proceeding with an active step over pausing/waiting, justified primarily by the value of acting rather than by risk analysis."
      },
      {
        "bias": "Affect Bias",
        "occurrences": 1,
        "mechanism_constraint": "Risk prioritization driven by emotional reaction to a vivid, unrelated recent event rather than new technical evidence."
      },
      {
        "bias": "Default bias",
        "occurrences": 1,
        "mechanism_constraint": "Retention of pre-set software parameters over an available, more representative alternative, justified by effort/status-quo rather than technical superiority."
      }
    ],
    "target_bias_names": [
      "Illusion of Truth effect",
      "Action bias",
      "Affect Bias",
      "Default bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Illusion of Truth effect", "requested_occurrences": 1 },
      { "bias": "Action bias", "requested_occurrences": 1 },
      { "bias": "Affect Bias", "requested_occurrences": 1 },
      { "bias": "Default bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect" },
      { "instance_id": "he4_ab_01", "bias": "Action bias" },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias" },
      { "instance_id": "he4_db_01", "bias": "Default bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect", "decision_point": 1 },
      { "instance_id": "he4_ab_01", "bias": "Action bias", "decision_point": 2 },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias", "decision_point": 3 },
      { "instance_id": "he4_db_01", "bias": "Default bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "he4_iot_01",
        "bias": "Illusion of Truth effect",
        "mechanism": "Repeated exposure to the same claim across three vendor documents traced to one underlying test increases perceived credibility without independent verification.",
        "affected_reasoning_operation": "Evaluation of source credibility / evidence weighting",
        "evidence_source": "Vendor B's spec sheet, cover email, and marketing brochure, all citing the same '90-minute, independently verified' claim",
        "distinctiveness_requirement": "Must be tied to decision point 1's glazing substitution evaluation only; not restated in later decision points."
      },
      {
        "instance_id": "he4_ab_01",
        "bias": "Action bias",
        "mechanism": "Preference for authorizing an active commissioning step over waiting for a recommended re-run, justified by the value of maintaining momentum rather than analysis of the borderline CFD result.",
        "affected_reasoning_operation": "Action-versus-inaction choice under schedule pressure and uncertainty",
        "evidence_source": "Preliminary CFD visibility result and QA's re-run recommendation at decision point 2",
        "distinctiveness_requirement": "Must be tied to the fan-commissioning authorization only; not conflated with the cladding-reprioritization decision in point 3."
      },
      {
        "instance_id": "he4_afb_01",
        "bias": "Affect Bias",
        "mechanism": "Emotional salience of a vivid, unrelated recent high-rise fire shifts inspection-time allocation toward the emotionally resonant cladding system over the technically more urgent pressurization deficiency.",
        "affected_reasoning_operation": "Risk-based prioritization of remaining QA punch-list items",
        "evidence_source": "News coverage of the unrelated fire and the pre-existing pressurization fan-door deficiency log at decision point 3",
        "distinctiveness_requirement": "Must be tied to punch-list reallocation only; must not be justified by new technical cladding evidence."
      },
      {
        "instance_id": "he4_db_01",
        "bias": "Default bias",
        "mechanism": "Retention of software's generic-office default occupant parameters over available project-specific survey data, justified by effort/status-quo rather than technical fit.",
        "affected_reasoning_operation": "Selection of model input parameters for the final egress compliance run",
        "evidence_source": "Software default library and colleague's flagged project-specific survey/comparable-building data at decision point 4",
        "distinctiveness_requirement": "Must be tied to the final egress-modeling run only; must not reuse action-bias or illusion-of-truth reasoning."
      }
    ],
    "intended_strength": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect", "strength": "moderate" },
      { "instance_id": "he4_ab_01", "bias": "Action bias", "strength": "moderate" },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias", "strength": "moderate" },
      { "instance_id": "he4_db_01", "bias": "Default bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Biased_4",
    "domain_id": "HE",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism: illusion of truth at the documentary-evidence evaluation (point 1), action bias at the schedule-pressure go/no-go choice (point 2), affect bias at the risk-prioritization choice following a vivid external event (point 3), and default bias at the modeling-parameter selection (point 4). No bias shares a decision point, so no additional evidence-source separation was required.",
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
