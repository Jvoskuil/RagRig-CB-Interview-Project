You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Failure to recognize regression to the mean",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Failure to recognize regression to the mean"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Failure to recognize regression to the mean",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "mechanism": "Attributing the full magnitude of a post-outlier decline to a deliberate intervention (Steady Watch) while disregarding the statistical likelihood that an extreme deviation (week-5 spike) would revert toward the established baseline independent of that intervention.",
        "affected_reasoning_operation": "Causal attribution of trend change following an extreme data point",
        "evidence_source": "SIGACTS weekly attack counts (weeks 1-8) combined with HUMINT reporting on resolution of transient local factors coincident with the spike",
        "distinctiveness_requirement": "This is the only planned instance; no other decision point may independently manifest the same evidence-processing failure (ignoring outlier-driven reversion) with new evidence sources or moments."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence versus absence of resolvable transient confounding factors coincident with the week-5 attack spike",
      "original_state": "Transient factors (festival, cache depletion, tribal dispute mediation) present and naturally resolved by weeks 7-8",
      "changed_state": "No transient confounding factors; spike reflects sustained capability escalation with no natural reason to revert",
      "variables_to_hold_constant": [
        "Baseline attack rate weeks 1-4",
        "Timing of Steady Watch implementation",
        "Magnitude and timing of week-5 spike",
        "Analyst identity and reporting cadence",
        "Command pressure and INTSUM deadline"
      ]
    },
    "scenario_id": "MD_Biased_1",
    "domain_id": "MD",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the clearest mechanism fit: the causal-attribution judgment made immediately after an extreme SIGACTS outlier reverts toward baseline, where transient confounders provide a documentable alternative explanation the analyst can be shown to underweight. Decision points 1, 3, and 4 were deliberately kept free of independent regression-to-the-mean evidence-processing acts to avoid double-counting the single requested instance.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Baseline attack rate weeks 1-4",
      "Timing of Steady Watch implementation",
      "Magnitude and timing of week-5 spike",
      "Analyst identity and reporting cadence",
      "Command pressure and INTSUM deadline"
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
