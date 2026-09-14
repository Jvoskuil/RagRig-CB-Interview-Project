You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Courtesy Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a softened severity classification tied to interpersonal politeness toward a specific stakeholder at one decision point, not as a general disposition or repeated behavior."
      }
    ],
    "target_bias_names": [
      "Courtesy Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Courtesy Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "mechanism": "Downgrading a life-safety-significant fire door closer deficiency from a formal citation to an informal advisory note in direct response to the building manager's apologetic, relationship-invoking demeanor, without independently re-verifying the maintenance ticket timeline or prior-year recurrence.",
        "affected_reasoning_operation": "Severity classification / risk categorization judgment under interpersonal pressure",
        "evidence_source": "In-person interaction with the building manager (apology, reassurance, appeal to cooperative history) combined with an unverified maintenance-ticket claim",
        "distinctiveness_requirement": "This is the sole instance; no other decision point may contain a second softened classification driven by interpersonal courtesy toward any stakeholder."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Building manager's interpersonal demeanor during the door-closer finding",
      "original_state": "Apologetic, cordial, relationship-invoking response from the manager",
      "changed_state": "Neutral or defensive response with identical factual content",
      "variables_to_hold_constant": [
        "Underlying technical deficiency and code classification standard",
        "Time pressure and same-day deadline",
        "All other decision points and findings",
        "Building type, layout, and renovation context"
      ]
    },
    "scenario_id": "HE_Biased_1",
    "domain_id": "HE",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point with the strongest mechanism fit (interpersonal interaction during a severity-classification judgment); no splitting needed since occurrences=1.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Underlying technical deficiency and code classification standard",
      "Time pressure and same-day deadline",
      "All other decision points and findings",
      "Building type, layout, and renovation context"
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
