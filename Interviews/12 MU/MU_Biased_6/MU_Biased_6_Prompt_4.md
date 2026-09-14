You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to recall of the specific sister-mine rockburst, not a generic caution statement." },
      { "bias": "Experience Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to overweighting supervisor tenure without verifying situational similarity." },
      { "bias": "Anchoring Bias", "occurrences": 2, "mechanism_constraint": "Each instance must reference a distinct evidence source (instrument baseline reading vs. crack photograph) at a distinct decision point." },
      { "bias": "Narrative Fallacy", "occurrences": 1, "mechanism_constraint": "Must occur only in the post-event causal explanation, not in earlier probes." },
      { "bias": "Attribution Bias", "occurrences": 1, "mechanism_constraint": "Must contrast individual worker blame against an identifiable systemic/process factor." }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Experience Bias",
      "Anchoring Bias",
      "Narrative Fallacy",
      "Attribution Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Availability Bias", "requested_occurrences": 1 },
      { "bias": "Experience Bias", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 2 },
      { "bias": "Narrative Fallacy", "requested_occurrences": 1 },
      { "bias": "Attribution Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "av_01", "bias": "Availability Bias" },
      { "instance_id": "exp_01", "bias": "Experience Bias" },
      { "instance_id": "anc_01", "bias": "Anchoring Bias" },
      { "instance_id": "anc_02", "bias": "Anchoring Bias" },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy" },
      { "instance_id": "attr_01", "bias": "Attribution Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "av_01", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "anc_01", "bias": "Anchoring Bias", "decision_point": 2 },
      { "instance_id": "exp_01", "bias": "Experience Bias", "decision_point": 3 },
      { "instance_id": "anc_02", "bias": "Anchoring Bias", "decision_point": 3 },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy", "decision_point": 4 },
      { "instance_id": "attr_01", "bias": "Attribution Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Vivid recall of the recent sister-mine rockburst inflates the perceived likelihood of the current ambiguous noise report.",
        "affected_reasoning_operation": "Risk-likelihood estimation from a verbal cue",
        "evidence_source": "Memory of a widely publicized recent industry incident",
        "distinctiveness_requirement": "Occurs only at decision point 1, tied specifically to the sister-mine memory, not repeated later."
      },
      {
        "instance_id": "anc_01",
        "bias": "Anchoring Bias",
        "mechanism": "Morning baseline extensometer reading anchors judgment of the later reading as 'still normal' instead of applying the rate-of-change rule.",
        "affected_reasoning_operation": "Comparative evaluation of updated instrument data against fixed initial reference",
        "evidence_source": "Extensometer displacement readings (05:00 baseline vs. 09:40 update)",
        "distinctiveness_requirement": "Uses instrument telemetry evidence at decision point 2; distinct from anc_02's photographic evidence at decision point 3."
      },
      {
        "instance_id": "exp_01",
        "bias": "Experience Bias",
        "mechanism": "Supervisor's tenure is treated as sufficient validation of a benign read, without checking situational similarity to today's conditions.",
        "affected_reasoning_operation": "Credibility weighting of informal expert opinion vs. threshold data",
        "evidence_source": "Supervisor's verbal recollection of a 2009 event",
        "distinctiveness_requirement": "Occurs only at decision point 3, distinct reasoning operation (credibility weighting) from anc_02's evidence comparison at the same decision point."
      },
      {
        "instance_id": "anc_02",
        "bias": "Anchoring Bias",
        "mechanism": "Prior week's photographed hairline crack anchors judgment of today's crack severity, displacing attention from the newly reached microseismic threshold.",
        "affected_reasoning_operation": "Visual/photographic comparison against a prior fixed reference",
        "evidence_source": "Crack-width photographs (last week vs. today)",
        "distinctiveness_requirement": "Uses photographic evidence at decision point 3; distinct evidence type and moment from anc_01's instrument-baseline anchor at decision point 2."
      },
      {
        "instance_id": "narr_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Multiple loosely-related factors are woven into a single tidy causal chain in the post-event report, overstating certainty of the causal linkage.",
        "affected_reasoning_operation": "Post-hoc causal reconstruction for incident reporting",
        "evidence_source": "Temperature log, shift-change timing, prior blasting record",
        "distinctiveness_requirement": "Occurs only in the decision point 4 incident narrative, not in earlier probes or hypotheticals."
      },
      {
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "mechanism": "Escalation responsibility is assigned mainly to the on-shift miner's reporting delay rather than to the missing systemic GCMP sign-off step.",
        "affected_reasoning_operation": "Causal attribution of responsibility between individual and systemic factors",
        "evidence_source": "Miner reporting timeline vs. GCMP sign-off requirement",
        "distinctiveness_requirement": "Occurs only in the decision point 4 responsibility assessment, distinct reasoning operation from narr_01's causal-chain construction at the same decision point."
      }
    ],
    "intended_strength": [
      { "instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "exp_01", "bias": "Experience Bias", "strength": "subtle" },
      { "instance_id": "anc_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "anc_02", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy", "strength": "subtle" },
      { "instance_id": "attr_01", "bias": "Attribution Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_6",
    "domain_id": "MU",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across the 4 decision points by mechanism fit and narrative realism: Availability Bias placed at the initial ambiguous-report decision (DP1) where recall of a recent vivid event is most plausible; Anchoring Bias split across DP2 (instrument baseline) and DP3 (photographic reference) using two distinct evidence sources to satisfy the same-decision-point distinctiveness rule; Experience Bias placed at DP3 alongside but reasoning-operation-distinct from the second Anchoring instance; Narrative Fallacy and Attribution Bias both placed at DP4 (post-event review) but targeting different reasoning operations (causal-chain construction vs. responsibility attribution). No bias exceeds two occurrences at a single decision point.",
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
