You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Retrievability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as reliance on an easily-recalled recent personal precedent rather than base-rate or matching-signature reasoning" },
      { "bias": "Search set Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as restricting information search to the habitual/familiar repository while equally accessible alternative sources go unconsulted" },
      { "bias": "Imaginability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as a vividly imaginable rehearsed scenario inflating perceived probability over an equally evidenced but less vivid alternative" }
    ],
    "target_bias_names": ["Retrievability Bias", "Search set Bias", "Imaginability Bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Retrievability Bias", "requested_occurrences": 1 },
      { "bias": "Search set Bias", "requested_occurrences": 1 },
      { "bias": "Imaginability Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias" },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias" },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias", "decision_point": 1 },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias", "decision_point": 2 },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MD3_retr_01",
        "bias": "Retrievability Bias",
        "mechanism": "Ease of recalling a recent, salient infiltration precedent inflates perceived likelihood of the current ambiguous alert being a genuine threat",
        "affected_reasoning_operation": "Initial priority classification of an ambiguous sensor alert",
        "evidence_source": "Officer's own recollection of a prior incident, contrasted with the actual (weaker) evidentiary content of the current alert",
        "distinctiveness_requirement": "Must be tied specifically to memory recall driving classification, not to search-source restriction (MD3_ss_01) or to imagined future scenarios (MD3_im_01)"
      },
      {
        "instance_id": "MD3_ss_01",
        "bias": "Search set Bias",
        "mechanism": "Restriction of the information search to the habitual own-sector repository skews the evidentiary basis for ISR tasking despite equally available alternative repositories",
        "affected_reasoning_operation": "Evidence-gathering/source-selection prior to ISR tasking",
        "evidence_source": "Comparison between the repository actually consulted (own-sector SIGINT) and the repositories available but not consulted (adjacent-unit logs, pattern-of-life database)",
        "distinctiveness_requirement": "Must be tied specifically to which sources were queried, not to memory retrieval (MD3_retr_01) or to vividness of imagined outcomes (MD3_im_01)"
      },
      {
        "instance_id": "MD3_im_01",
        "bias": "Imaginability Bias",
        "mechanism": "A vividly rehearsed ambush scenario is easier to mentally simulate than the equally evidenced mundane alternative, inflating its perceived probability and driving QRF escalation",
        "affected_reasoning_operation": "Risk assessment and QRF readiness decision based on ambiguous thermal imagery",
        "evidence_source": "Officer's account of the mental scenario constructed from recent training, contrasted with the genuinely ambiguous thermal evidence",
        "distinctiveness_requirement": "Must be tied specifically to vividness/ease of mental simulation of an outcome, not to memory of a past real event (MD3_retr_01) or to which information sources were searched (MD3_ss_01)"
      }
    ],
    "intended_strength": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias", "strength": "subtle" },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias", "strength": "subtle" },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of adjacent-unit and pattern-of-life data at ISR tasking time",
      "original_state": "Officer consults only own-sector SIGINT summaries",
      "changed_state": "Officer's workflow automatically surfaces adjacent-unit and pattern-of-life data alongside own-sector summaries",
      "variables_to_hold_constant": [
        "Initial sensor alert content and ambiguity",
        "Single available ISR asset",
        "Time pressure and staffing shortfall",
        "Subsequent QRF and reporting decisions",
        "Personnel and stakeholders involved"
      ]
    },
    "scenario_id": "MD_Biased_3",
    "domain_id": "MD",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences spread across distinct decision points (1, 2, 3) per mechanism fit and narrative realism; decision point 4 reserved as bias-free reporting/closure phase; no bias assigned to more than one decision point; no two occurrences share a decision point so no cross-evidence-source separation was required.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Initial sensor alert content and ambiguity",
      "Single available ISR asset",
      "Time pressure and staffing shortfall",
      "Personnel and stakeholders involved",
      "Overall four-decision-point structure"
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
