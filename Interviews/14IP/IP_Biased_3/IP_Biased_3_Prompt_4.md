You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Imaginability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as disproportionate causal-narrative weighting toward a vivid, recently recalled comparable incident over a statistically dominant base-rate cause, at decision point 3 only."
      },
      {
        "bias": "Ostrich effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as conscious deferral of an information-gathering step (full CEM pull/lab confirmation) motivated by avoidance of an unwelcome confirmatory finding, at decision point 2 only."
      },
      {
        "bias": "Primacy Effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an early-formed hypothesis anchoring interpretation of subsequently received, more ambiguous evidence, at decision point 1 only."
      }
    ],
    "target_bias_names": ["Imaginability Bias", "Ostrich effect", "Primacy Effect"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Imaginability Bias", "requested_occurrences": 1 },
      { "bias": "Ostrich effect", "requested_occurrences": 1 },
      { "bias": "Primacy Effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Primacy Effect" },
      { "instance_id": "cb_02", "bias": "Ostrich effect" },
      { "instance_id": "cb_03", "bias": "Imaginability Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Ostrich effect", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Imaginability Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "mechanism": "Early alarm-log-based drift hypothesis anchors interpretation of subsequent ambiguous field readings",
        "affected_reasoning_operation": "Initial hypothesis formation / subsequent evidence interpretation",
        "evidence_source": "Alarm log and sensor drift history reviewed within minutes of the alarm",
        "distinctiveness_requirement": "Distinct from cb_03 by occurring at first evidence encounter (drift history) rather than at narrative construction from a recalled external incident"
      },
      {
        "instance_id": "cb_02",
        "bias": "Ostrich effect",
        "mechanism": "Deliberate deferral of full CEM data pull/lab confirmation to avoid confirming a costly reportable exceedance",
        "affected_reasoning_operation": "Information-seeking behavior under threat of unwelcome confirmation",
        "evidence_source": "Grey-zone field VOC readings and known cost/reporting consequences of a confirmed exceedance",
        "distinctiveness_requirement": "Distinct from cb_01 and cb_03 in involving active avoidance of an available information-gathering action rather than misweighting evidence already in hand"
      },
      {
        "instance_id": "cb_03",
        "bias": "Imaginability Bias",
        "mechanism": "Vivid, recently recalled sister-plant valve-failure incident disproportionately shapes causal attribution over the statistically dominant gasket-seep base rate",
        "affected_reasoning_operation": "Causal attribution / hypothesis prioritization for incident narrative",
        "evidence_source": "Three-year maintenance log base rates versus recalled corporate webinar narrative",
        "distinctiveness_requirement": "Distinct from cb_01 by involving retrieval of an external, emotionally vivid memory to override base-rate statistical evidence, rather than anchoring on the first internally generated hypothesis"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Ostrich effect", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Imaginability Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Officer's recent exposure to a vivid comparable incident narrative (Ohio sister-plant valve failure) prior to causal-narrative construction",
      "original_state": "Officer attended a corporate webinar two weeks before the incident describing the Ohio valve failure",
      "changed_state": "Officer had no recent exposure to any vivid comparable incident narrative",
      "variables_to_hold_constant": [
        "Sensor alarm timing and drift history",
        "Community odor complaint",
        "Production deadline and shutdown cost figures",
        "Maintenance log base rates for gasket seep vs. valve failure",
        "Number and sequencing of decision points",
        "Difficulty level and word count target"
      ]
    },
    "scenario_id": "IP_Biased_3",
    "domain_id": "IP",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1, 2, 3) selected for mechanism fit and narrative realism; decision point 4 deliberately left free of intended bias instrumentation to serve as an undetermined control judgment within the same interview.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Setting, actors, and stakeholder roles",
      "Four-decision-point structure",
      "Difficulty level (challenging)",
      "Emotional tone and time-pressure framing",
      "Target word count range (1,215-1,485)"
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
