You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Omitting Subjectivity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a retrospective self-report of decision basis at the fuel-planning decision point, framing a partly subjective judgment as purely procedural/objective."
      },
      {
        "bias": "Plan Continuation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as continuing the original approach plan into destination despite mixed/disconfirming trend evidence (go-around report, flat visibility trend) available before commencing the approach."
      }
    ],
    "target_bias_names": [
      "Omitting Subjectivity",
      "Plan Continuation"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Omitting Subjectivity",
        "requested_occurrences": 1
      },
      {
        "bias": "Plan Continuation",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity"
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "decision_point": 1
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "mechanism": "Captain's self-report of the fuel-load decision omits that a subjective confidence judgment (personal history with the station's fog patterns) was material to accepting dispatch-minimum fuel, instead framing the decision as purely procedural.",
        "affected_reasoning_operation": "Retrospective justification / self-report of decision basis",
        "evidence_source": "Captain's answer to the decision-basis probe at decision point 1, contrasted with the timeline fact of his prior experience-based expectation",
        "distinctiveness_requirement": "Must be tied specifically to the fuel-acceptance decision and the framing of its basis, not to any later decision or general commentary on weather uncertainty."
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "mechanism": "Captain proceeds with the originally briefed approach into the original destination despite a go-around report and a flattening visibility trend, weighting the original forecast/plan over the newer disconfirming cues immediately before the approach attempt.",
        "affected_reasoning_operation": "Updating a prior plan given new disconfirming evidence before committing to an approach",
        "evidence_source": "Captain's account of the approach-continuation decision at decision point 3, contrasted with the mixed METAR trend and go-around PIREP available at that time",
        "distinctiveness_requirement": "Must be tied specifically to the pre-approach continuation decision at decision point 3, not to the earlier fuel decision (decision point 1) or the later post-missed-approach diversion decision (decision point 4), which must show the captain reassessing independently."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "strength": "subtle"
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_2",
    "domain_id": "AV",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias occurred once in the manifest; each was assigned to the single decision point offering the best mechanism fit and narrative realism (fuel-planning self-report for Omitting Subjectivity at decision point 1; approach-continuation choice under disconfirming trend evidence for Plan Continuation at decision point 3), per rules 2 and 3 of the allocation guidance. No decision point received more than one instance of either bias, and the two biases were kept at distinct decision points to preserve independent evidence traces.",
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
