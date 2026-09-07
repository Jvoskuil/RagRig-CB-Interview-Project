You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Failure to recognize regression to the mean",
        "occurrences": 0,
        "mechanism_constraint": "Must not be intentionally embedded; phase-2 reasoning must remain genuinely underdetermined between checkpoint effect and natural resolution of transient factors, without either dismissing the reversion-relevant evidence or naming/defining the bias."
      }
    ],
    "target_bias_names": [
      "Failure to recognize regression to the mean"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Failure to recognize regression to the mean",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MD_Biased_1",
    "counterfactual_variable": {
      "name": "Presence versus absence of resolvable transient confounding factors coincident with the week-5 attack spike",
      "original_state": "Transient factors (festival, cache depletion, tribal dispute mediation) present and naturally resolved by weeks 7-8, keeping the cause of the decline ambiguous",
      "changed_state": "No transient confounding factors; spike reflects sustained escalation with no independent reason to subside",
      "variables_to_hold_constant": [
        "Baseline attack rate weeks 1-4",
        "Timing of Steady Watch implementation",
        "Magnitude and timing of week-5 spike",
        "Analyst identity and reporting cadence",
        "Command pressure and INTSUM deadline"
      ]
    },
    "scenario_id": "MD_Ambigious_1",
    "domain_id": "MD",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; this is a zero-occurrence ambiguous control paired with MD_Biased_1. The single decision point that carries the bias mechanism in the paired scenario (phase 2, causal attribution of the weeks 7-8 decline) is deliberately rewritten here as an explicitly unresolved, dual-explanation judgment rather than a confident single-cause attribution, and this rewrite is not counted as a bias instance.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Setting, stakeholders, and operational constraints",
      "SIGACTS trajectory (baseline, week-5 spike, weeks 7-8 decline)",
      "Four decision-point structure and alternative sets",
      "District Y comparison and forecast-to-commander closing decision",
      "Interview length target and emotional tone"
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
