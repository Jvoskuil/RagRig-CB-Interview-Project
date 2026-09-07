You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Contextual Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as case-outcome information (confession/priors) influencing resolution of a genuinely ambiguous print feature during comparison, not as a general statement of belief in guilt."
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a post-hoc explanation constructed to preserve a pre-existing conclusion after disconfirming verifier feedback, not as a routine technical judgment offered independent of the prior conclusion."
      }
    ],
    "target_bias_names": [
      "Contextual Bias",
      "Coherence-based reasoning or Rationalisation"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Contextual Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias"
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "decision_point": 2
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "mechanism": "Extraneous confession/prior-record information received pre-analysis shifts interpretation of an ambiguous peripheral ridge region toward a match-consistent reading, absent independent print-based justification for that specific resolution.",
        "affected_reasoning_operation": "Evaluation/interpretation of ambiguous perceptual evidence during Comparison/Evaluation",
        "evidence_source": "Detective's unsolicited case-outcome remarks retained during analysis of the distorted peripheral ridge area",
        "distinctiveness_requirement": "Distinct from coh_01: occurs at the analysis/comparison stage on ambiguous perceptual data, before any conclusion has been challenged, and is driven by pre-analysis extraneous information rather than by defending an already-stated conclusion against disconfirming feedback."
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "After the verifying examiner flags a discrepancy, the examiner generates a distortion-based explanation that renders the discrepancy compatible with the already-fixed individualization conclusion, rather than treating it as evidence warranting downgrade.",
        "affected_reasoning_operation": "Evaluation of disconfirming evidence and belief updating during final report reconciliation",
        "evidence_source": "Verifying examiner's independent discrepancy flag on the peripheral ridge region, evaluated against the pre-existing draft conclusion",
        "distinctiveness_requirement": "Distinct from ctx_01: occurs post-conclusion, triggered by external disconfirming feedback from a second examiner, and operates through explanatory construction to preserve coherence with a prior commitment rather than through initial ambiguous-evidence interpretation."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "strength": "moderate"
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence versus absence of unsolicited case-outcome information at intake",
      "original_state": "Detective volunteers confession and prior-record information before analysis begins",
      "changed_state": "Case submitted blind, with no outcome information disclosed to the examiner",
      "variables_to_hold_constant": [
        "Print quality and distortion pattern",
        "Number and clarity of minutiae",
        "Deadline pressure",
        "Verification routing and staffing availability",
        "Verifier's discrepancy finding at phase 4"
      ]
    },
    "scenario_id": "LE_Biased_2",
    "domain_id": "LE",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias, each assigned to the decision point offering the best mechanism fit and narrative realism: Contextual Bias at the initial ambiguous-comparison decision (phase 2), where pre-analysis case information most plausibly biases perceptual interpretation; Coherence-based reasoning/Rationalisation at the final report-reconciliation decision (phase 4), where disconfirming verifier feedback most plausibly triggers a conclusion-preserving explanation. Decision points were kept distinct (no shared decision point) to maximize independent identifiability and avoid overlap between mechanisms.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Print quality and distortion pattern",
      "Number and clarity of minutiae",
      "Deadline pressure",
      "Staffing and verification availability",
      "Verifier's discrepancy finding"
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
