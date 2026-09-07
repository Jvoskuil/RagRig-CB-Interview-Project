You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Sunk cost bias",
        "occurrences": 2,
        "mechanism_constraint": "Must reference prior investment (overhaul cost and/or time already spent troubleshooting) as a stated reason for the decision, at two distinct decision points with distinct evidence."
      },
      {
        "bias": "Automation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must show reliance on automated monitoring readout as sufficient, in place of an available manual verification step."
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must show a competing cue being registered but not processed for action due to attentional focus elsewhere."
      },
      {
        "bias": "Hindsight Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must occur only in retrospective reflection/probe response, recasting an originally ambiguous signal as having been obviously predictive."
      }
    ],
    "target_bias_names": [
      "Sunk cost bias",
      "Automation Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Hindsight Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Sunk cost bias", "requested_occurrences": 2 },
      { "bias": "Automation Bias", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 },
      { "bias": "Hindsight Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias" },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias" },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias" },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias", "decision_point": 1 },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias", "decision_point": 2 },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 3 },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias", "decision_point": 4 },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MO5_SC_01",
        "bias": "Sunk cost bias",
        "mechanism": "Continuing at full speed because a recently, expensively overhauled unit is assumed unlikely to fail, treating the investment as evidence against the current reading.",
        "affected_reasoning_operation": "Weighting of prior investment in continue-vs-inspect decision",
        "evidence_source": "Overhaul cost/recency plus phase-1 vibration and temperature readings",
        "distinctiveness_requirement": "Distinct from MO5_SC_02 by decision point, by the specific evidence (initial ambiguous reading vs. active partial failure), and by the action considered (continuing without inspection vs. pressing on instead of diverting)."
      },
      {
        "instance_id": "MO5_AB_01",
        "bias": "Automation Bias",
        "mechanism": "Accepting the automated monitoring system's nominal readout as sufficient confirmation, forgoing available manual verification.",
        "affected_reasoning_operation": "Evidence-sufficiency judgment / verification-seeking",
        "evidence_source": "Automated system readout vs. availability of manual lube oil sample",
        "distinctiveness_requirement": "Sole instance of this bias; must not be repeated at any other decision point or probe."
      },
      {
        "instance_id": "MO5_SA_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Fixation on turbocharger dashboard causes the fuel filter differential pressure report to be noted but not processed as actionable.",
        "affected_reasoning_operation": "Attention allocation among competing simultaneous cues",
        "evidence_source": "Second Engineer's verbal report of rising fuel filter differential pressure during active turbocharger monitoring",
        "distinctiveness_requirement": "Sole instance of this bias; must not be repeated in later probes or the phase-4 crisis handling."
      },
      {
        "instance_id": "MO5_SC_02",
        "bias": "Sunk cost bias",
        "mechanism": "Choosing to jury-rig and continue toward the tide window rather than divert, citing prior time/cost investment rather than only present risk.",
        "affected_reasoning_operation": "Weighting of prior time/cost investment in divert-vs-continue decision",
        "evidence_source": "Partial bearing failure signals plus cumulative overhaul cost and troubleshooting time already spent",
        "distinctiveness_requirement": "Distinct from MO5_SC_01 by decision point, evidence (active failure vs. initial ambiguous signal), and the specific investment referenced (cumulative time+cost vs. overhaul recency alone)."
      },
      {
        "instance_id": "MO5_HB_01",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively recasting the ambiguous phase-1 signal as having been obviously predictive of failure, inconsistent with how it was treated at the time.",
        "affected_reasoning_operation": "Retrospective causal attribution / memory reconstruction",
        "evidence_source": "Closing hypothetical/reflection probe response referencing the phase-1 reading with outcome knowledge",
        "distinctiveness_requirement": "Occurs only in retrospective probe response tied to decision point 4's aftermath, not in the real-time decision itself; distinct reasoning operation from MO5_SC_02's forward-looking action choice."
      }
    ],
    "intended_strength": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias", "strength": "subtle" },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias", "strength": "moderate" },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias", "strength": "moderate" },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "subtle" },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence vs. absence of the fixed tide-restricted berth deadline (schedule time pressure)",
      "original_state": "A fixed tide-restricted berth window roughly 30 hours out creates continuous schedule pressure throughout the incident.",
      "changed_state": "No tide restriction; flexible arrival window with no binding schedule deadline.",
      "variables_to_hold_constant": [
        "Turbocharger fault progression and physical failure mechanics",
        "Recent overhaul history and cost",
        "Crew composition and roles",
        "Automated monitoring system behavior",
        "Fuel filter differential pressure event"
      ]
    },
    "scenario_id": "MO_Biased_5",
    "domain_id": "MO",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across distinct decision points where possible; sunk cost split across decision points 1 and 4 with distinct evidence and referenced investments; automation bias and selective attention each assigned to their single mechanism-fitting decision point (2 and 3 respectively); hindsight bias assigned to decision point 4's retrospective aftermath, sharing the decision point with the second sunk cost instance but differing in reasoning operation (forward action choice vs. retrospective causal attribution) and evidence source (real-time failure signals vs. outcome-informed recollection), per rule 4.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Turbocharger fault progression and physical failure mechanics",
      "Recent overhaul history and cost",
      "Crew composition and roles",
      "Automated monitoring system behavior",
      "Fuel filter differential pressure event"
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
