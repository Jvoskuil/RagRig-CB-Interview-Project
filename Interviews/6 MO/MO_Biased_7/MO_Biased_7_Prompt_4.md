You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{INTERVIEW}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as reliance on agreeing DGPS pair to dismiss conflicting HPR reading without independent cross-check"},
      {"bias": "Automation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as deference to DP system's auto-weighted GREEN status over independent manual interpretation of raw discrepancy data"},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 1, "mechanism_constraint": "Must manifest as failure to notice a visually-available footprint/environmental cue due to sustained focus on the crane display"},
      {"bias": "Hindsight Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as retrospective overstatement of foreseeability of the Phase 1 reference discrepancy during closing reflection"},
      {"bias": "Sunk cost bias", "occurrences": 1, "mechanism_constraint": "Must manifest as justification for continuing based on cargo/time already invested rather than forward-looking capability reassessment"},
      {"bias": "Status Quo Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as default preservation of current DP mode/pace without active comparison of mode-change alternatives"},
      {"bias": "Framing Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as decision rationale framed around remaining time rather than narrowing safety margin"}
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Automation Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Hindsight Bias",
      "Sunk cost bias",
      "Status Quo Bias",
      "Framing Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Confirmation Bias", "requested_occurrences": 1},
      {"bias": "Automation Bias", "requested_occurrences": 1},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1},
      {"bias": "Hindsight Bias", "requested_occurrences": 1},
      {"bias": "Sunk cost bias", "requested_occurrences": 1},
      {"bias": "Status Quo Bias", "requested_occurrences": 1},
      {"bias": "Framing Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias"},
      {"instance_id": "ab_01", "bias": "Automation Bias"},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness"},
      {"instance_id": "hb_01", "bias": "Hindsight Bias"},
      {"instance_id": "sc_01", "bias": "Sunk cost bias"},
      {"instance_id": "sq_01", "bias": "Status Quo Bias"},
      {"instance_id": "fb_01", "bias": "Framing Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1},
      {"instance_id": "ab_01", "bias": "Automation Bias", "decision_point": 1},
      {"instance_id": "hb_01", "bias": "Hindsight Bias", "decision_point": 1},
      {"instance_id": "sc_01", "bias": "Sunk cost bias", "decision_point": 2},
      {"instance_id": "sq_01", "bias": "Status Quo Bias", "decision_point": 2},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 3},
      {"instance_id": "fb_01", "bias": "Framing Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective reliance on the two agreeing GPS references to confirm the preferred position estimate, dismissing the conflicting HPR reading as the outlier without independent verification",
        "affected_reasoning_operation": "evidence-selection and weighting during reference validation",
        "evidence_source": "Reference system comparison data (DGPS1, DGPS2, HPR) at Phase 1",
        "distinctiveness_requirement": "Must be distinguished from ab_01 by focusing on the DPO's own evidence-selection reasoning rather than on deference to the automated system status indicator"
      },
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "mechanism": "Deference to the DP system's automated reference-weighting and GREEN status as sufficient justification, bypassing independent manual interpretation of the underlying raw data",
        "affected_reasoning_operation": "trust calibration between automated output and manual judgment",
        "evidence_source": "DP system status indicator and auto-weighting output at Phase 1",
        "distinctiveness_requirement": "Must be distinguished from cb_01 by centering on trust in the system's output itself, not on the DPO's own selective interpretation of raw discrepancy data"
      },
      {
        "instance_id": "hb_01",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospective overstatement, during closing reflection, of how foreseeable the Phase 1 discrepancy's significance was, exceeding what the contemporaneous alert status supported",
        "affected_reasoning_operation": "retrospective foreseeability judgment elicited by closing hypothetical probe",
        "evidence_source": "DPO's closing-probe response compared against the contemporaneous Phase 1 alert status",
        "distinctiveness_requirement": "Must occur only in the closing reflective probe tied to the Phase 1 event, not as a repeated commentary elsewhere in the interview"
      },
      {
        "instance_id": "sc_01",
        "bias": "Sunk cost bias",
        "mechanism": "Justification for continuing the transfer that foregrounds cargo and time already invested rather than a forward-looking reassessment of DP capability given the new thruster caution",
        "affected_reasoning_operation": "cost-weighting in the continue-versus-suspend judgment",
        "evidence_source": "Phase 2 cargo-completion status and elapsed operation time",
        "distinctiveness_requirement": "Must be distinguished from sq_01 by explicit reference to invested cost/effort as the stated reason, rather than default preservation of the operating mode without any stated cost rationale"
      },
      {
        "instance_id": "sq_01",
        "bias": "Status Quo Bias",
        "mechanism": "Retention of the existing DP Auto configuration and operating pace after the thruster caution, without active comparison of a more conservative mode as an alternative",
        "affected_reasoning_operation": "option-generation and default-preservation when a new caution condition arises",
        "evidence_source": "Phase 2 mode/configuration status and absence of considered alternatives in DPO's account",
        "distinctiveness_requirement": "Must be distinguished from sc_01 by the absence of an invested-cost rationale; the defining feature is default retention of configuration, not a cost-based justification"
      },
      {
        "instance_id": "sa_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Sustained attentional focus on the crane boom display causes a visually-available footprint/wind-shift indicator change to go unnoticed until pointed out externally",
        "affected_reasoning_operation": "perceptual monitoring and attentional allocation across competing displays",
        "evidence_source": "Phase 3 footprint plot indicator timeline versus DPO's attention account",
        "distinctiveness_requirement": "Unique to Phase 3; concerns failure to perceive available information, not failure to act on already-perceived information"
      },
      {
        "instance_id": "fb_01",
        "bias": "Framing Bias",
        "mechanism": "The continue/suspend rationale communicated to the OIM is framed around remaining completion time rather than the narrowing safety margin, despite both being available",
        "affected_reasoning_operation": "decision framing in the final continue-versus-suspend response to a direct query",
        "evidence_source": "Phase 4 DPO response to the OIM's query, compared against available margin data",
        "distinctiveness_requirement": "Unique to Phase 4; concerns how the decision is framed/communicated, not the underlying cost or default-preservation reasoning captured by sc_01/sq_01"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle"},
      {"instance_id": "ab_01", "bias": "Automation Bias", "strength": "subtle"},
      {"instance_id": "hb_01", "bias": "Hindsight Bias", "strength": "subtle"},
      {"instance_id": "sc_01", "bias": "Sunk cost bias", "strength": "subtle"},
      {"instance_id": "sq_01", "bias": "Status Quo Bias", "strength": "subtle"},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate"},
      {"instance_id": "fb_01", "bias": "Framing Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "N/A",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MO_Biased_7",
    "domain_id": "MO",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across distinct decision points by mechanism fit and narrative realism: Phase 1 (reference discrepancy) hosts confirmation bias, automation bias, and hindsight bias as three distinct reasoning operations (evidence-selection, automation trust, retrospective foreseeability); Phase 2 (continue transfer under thruster caution) hosts sunk cost and status quo as distinct rationale types (cost-based vs. default-based); Phase 3 (final lift) hosts selective attention/inattentional blindness as the sole attentional-mechanism fit; Phase 4 (final continue/suspend decision) hosts framing bias as the sole communication-framing fit. No bias exceeds two occurrences at a single decision point, and no two co-located instances share an evidence source or reasoning operation.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "MO_Biased_7",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Marine offshore dynamic-positioning operations during platform cargo transfer",
    "role": "Dynamic Positioning Operator (DPO) on watch",
    "objective": "Maintain safe station-keeping and separation from the platform while completing a scheduled cargo transfer within a deteriorating weather window",
    "incident_type": "Near-miss involving reduced propulsion capability, missed environmental/footprint cue, narrowing separation margin, and early suspension of the final lift",
    "confidence": 0.99
  },
  "structure_audit": {
    "estimated_word_count": 1510,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "The DPO proceeds with final approach despite a 1.8-metre discrepancy between HPR and the two agreeing DGPS references.",
        "evidence_before": [
          "HPR differs from the DGPS references by approximately 1.8 metres",
          "DGPS1 and DGPS2 agree closely",
          "The HPR has no maintenance fault flag",
          "The DP system auto-weights the two DGPS references and presents GREEN status"
        ],
        "evidence_after": [
          "The DPO does not inspect the raw HPR trace",
          "The vessel proceeds alongside and begins the transfer",
          "The later account identifies structural multipath as the explanation for the HPR offset"
        ],
        "goals_constraints": [
          "Complete scheduled transfer",
          "Maintain safe approach and position",
          "Operate within a shrinking weather window",
          "Interpret conflicting reference-system information"
        ],
        "alternatives": [
          "Pause approach and manually inspect the HPR trace",
          "Cross-check references through an independent method",
          "Proceed using the auto-selected DGPS pair",
          "Adjust reference weighting or increase operating margin before closing distance"
        ],
        "decision_basis": "The DPO treats agreement between two references and the system's GREEN auto-weighted solution as sufficient grounds to proceed.",
        "time_pressure": "Moderate: weather was forecast to exceed the platform crane operating limit within roughly four hours.",
        "uncertainty": "Moderate: the reference discrepancy was unexplained at the time, although no system fault was displayed."
      },
      {
        "id": 2,
        "summary": "Following a Thruster 3 yellow caution and reduced available power, the DPO continues the transfer in the same DP configuration.",
        "evidence_before": [
          "Approximately 55% of cargo has already been transferred",
          "Thruster 3 presents a yellow caution and reduced power availability",
          "Consequence analysis indicates capability remains adequate",
          "The weather window is closing",
          "The superintendent reminds the crew of the subsequent transit schedule"
        ],
        "evidence_after": [
          "No active comparison of more conservative operating alternatives occurs",
          "The DP configuration and pace remain unchanged",
          "The operation proceeds into its final stage with reduced margin"
        ],
        "goals_constraints": [
          "Complete cargo transfer before deteriorating weather",
          "Remain within DP capability",
          "Avoid disruption to onward transit",
          "Maintain adequate separation and station-keeping margin"
        ],
        "alternatives": [
          "Suspend and reassess capability",
          "Tighten the watch circle",
          "Reweight or revalidate references",
          "Adopt a more conservative DP configuration",
          "Continue in the existing configuration"
        ],
        "decision_basis": "The DPO relies on continued formal capability, completion already achieved, weather pressure, and the absence of a red alarm.",
        "time_pressure": "Moderate to high: the operating weather window and subsequent transit schedule create completion pressure.",
        "uncertainty": "Moderate: capability remains technically adequate, but degraded thrust availability changes the reserve margin."
      },
      {
        "id": 3,
        "summary": "During the late transfer stage, the DPO fails to notice a visually available footprint-plot recommendation change while monitoring the crane boom.",
        "evidence_before": [
          "A wind shift changes the footprint-plot recommendation",
          "The footprint indicator remains available on a secondary screen",
          "The DPO is closely monitoring crane boom and load position",
          "No explicit delegation of environmental-watch responsibility has been made"
        ],
        "evidence_after": [
          "The footprint change is noticed only after the Master comments on vessel attitude",
          "The DPO confirms the indicator had been displayed",
          "The environmental cue was not incorporated into the ongoing operational assessment"
        ],
        "goals_constraints": [
          "Monitor crane and suspended-load hazards",
          "Maintain environmental awareness",
          "Maintain safe vessel attitude and separation",
          "Allocate attention across competing displays during an active lift"
        ],
        "alternatives": [
          "Explicitly assign environmental monitoring to the co-operator",
          "Use a structured scan of DP overview and footprint display",
          "Continue monitoring the crane display as the dominant attentional focus"
        ],
        "decision_basis": "Attentional resources are concentrated on crane-bloom and load monitoring, leaving the secondary footprint display unmonitored.",
        "time_pressure": "High: the incident occurs during an active late-stage lift under a narrowing weather window.",
        "uncertainty": "Moderate: the environmental change is visible but is not accompanied by an audible alarm or an explicitly assigned monitoring responsibility."
      },
      {
        "id": 4,
        "summary": "When the OIM asks whether to finish the final lift or stand off, the DPO recommends finishing based primarily on an eight-to-ten-minute completion estimate.",
        "evidence_before": [
          "The final lift remains incomplete",
          "Thruster status has not escalated beyond caution",
          "The DPO estimates eight to ten minutes remaining",
          "Safety margin has narrowed more than the DPO has tracked"
        ],
        "evidence_after": [
          "The transfer continues into the final lift",
          "Separation from the platform leg closes more than expected",
          "The operation is suspended early and the vessel backs off safely"
        ],
        "goals_constraints": [
          "Complete the final lift",
          "Maintain separation margin",
          "Avoid contact with the platform leg",
          "Respond to an explicit continue-versus-stand-off question"
        ],
        "alternatives": [
          "Stand off before beginning or continuing the final lift",
          "Finish based on short expected completion time",
          "Reassess and communicate remaining DP and separation margin before deciding"
        ],
        "decision_basis": "The DPO communicates the decision in terms of expected minutes to completion rather than quantified remaining safety margin.",
        "time_pressure": "High: the decision occurs at the final stage under deteriorating conditions.",
        "uncertainty": "Moderate to high: the DPO has incomplete awareness of the narrowing margin and changing vessel attitude."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "cb_01",
      "bias": "Confirmation Bias",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 1,
      "supporting_quote": "“DGPS1 and DGPS2 agreed within normal tolerance, HPR was off by 1.8 meters... Two out of three lined up... so I proceeded on that basis.”",
      "evidence_location": "Reference-discrepancy reconstruction, especially the participant's explanation after being asked whether an independent check was performed.",
      "mechanism": "The participant gives greater weight to the agreeing DGPS pair and treats HPR as the outlier without independently resolving the discrepancy.",
      "strength": "weak",
      "confidence": 0.74,
      "plausible_nonbias_explanation": "Using two closely agreeing positioning references over one discrepant reference can be a reasonable preliminary reliability judgment, especially where the system reports no fault and the account does not establish that the DPO held a prior preferred position estimate or sought confirming evidence selectively.",
      "additional_evidence_needed": "Evidence that the DPO treated the agreeing DGPS pair as confirmation of an already preferred interpretation and discounted potentially disconfirming HPR evidence specifically because it conflicted with that interpretation, rather than simply applying an ordinary majority-reference heuristic.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_reasoning_revision",
        "location": "Decision point 1, in the answer beginning “DGPS1 and DGPS2 agreed within normal tolerance...”",
        "current_defect": "The account establishes insufficient independent verification, but it does not clearly establish motivated or selective confirmation of a pre-existing preferred estimate. The current evidence can be explained by ordinary reference-reliability reasoning.",
        "minimal_change_instruction": "Add one subtle sentence showing that the DPO had already formed the view that the DGPS pair represented the correct solution and therefore treated the HPR trace as not worth examining because it conflicted with that view; retain the absence of any independent cross-check.",
        "preserve": [
          "The 1.8-metre HPR discrepancy",
          "Agreement between DGPS1 and DGPS2",
          "The lack of an HPR fault flag",
          "The later multipath explanation",
          "The separate automation-bias evidence concerning system auto-weighting and GREEN status"
        ],
        "avoid_creating": [
          "A second confirmation-bias episode at the thruster or final-lift decision points",
          "An explicit textbook statement that the participant was seeking confirmation",
          "Additional automation-bias evidence that makes cb_01 indistinguishable from ab_01"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "ab_01",
      "bias": "Automation Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "“The pairing agreed and the status was green, so I didn't dig into the raw HPR trace further at that point.”",
      "evidence_location": "Follow-up question about independently checking the reference discrepancy.",
      "mechanism": "The DPO treats the DP system's auto-selected reference pair and GREEN status as sufficient, bypassing independent interpretation of the discrepant raw HPR information.",
      "strength": "moderate",
      "confidence": 0.93,
      "plausible_nonbias_explanation": "The automated solution may have been properly calibrated and a green status may normally be operationally sufficient; however, the participant explicitly identifies the automated pairing and status as the reason not to examine the raw trace.",
      "additional_evidence_needed": "None required for the requested occurrence.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, answer beginning “Not really — the pairing agreed and the status was green...”",
        "current_defect": "None material. The system output and the bypassed manual check are independently observable.",
        "minimal_change_instruction": "No change.",
        "preserve": [
          "The distinction between trust in the automated GREEN output and the participant's separate evidence-selection account"
        ],
        "avoid_creating": [
          "An additional automation-bias episode at the thruster caution through overreliance on consequence analysis"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "sa_01",
      "bias": "Selective Attention Bias or Inattentional Blindness",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 3,
      "supporting_quote": "“The crane boom, almost entirely... The footprint indicator is a visual cue only, no audible alarm tied to it, so it's easy for it to sit there unnoticed if you're not specifically glancing over.”",
      "evidence_location": "Final-lift and footprint-change reconstruction.",
      "mechanism": "Sustained attention to crane and load monitoring coincides with failure to perceive a visibly available footprint recommendation change until the Master calls attention to vessel attitude.",
      "strength": "weak",
      "confidence": 0.79,
      "plausible_nonbias_explanation": "The crane boom and suspended load may legitimately be the highest immediate hazard, the footprint change appears only on a secondary display, no audible alarm is provided, and the watch responsibility was not explicitly allocated. These features support an interface and work-design explanation as strongly as a maladaptive attentional bias.",
      "additional_evidence_needed": "Evidence that the DPO had a defined obligation or practicable scan routine to monitor the footprint cue during the lift, knew the cue was decision-relevant, and nevertheless maintained a non-adaptive focus on the crane display rather than arranging coverage or conducting required cross-checks.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_evidence_addition",
        "location": "Decision point 3, immediately after the answer describing the footprint indicator on the secondary screen.",
        "current_defect": "The missed cue is textually established, but the interview does not adequately distinguish attentional blindness from a reasonable prioritization of an acute crane hazard combined with poor interface salience and unassigned monitoring responsibility.",
        "minimal_change_instruction": "Add a brief operational detail that the footprint display was part of the normal late-lift scan and that the co-operator was available but not assigned because the DPO assumed a quick final lift did not warrant interrupting crane-focused monitoring. Keep the missed cue visually available and unalarmed.",
        "preserve": [
          "The wind shift",
          "The secondary-screen footprint cue",
          "The DPO's attention to the crane boom",
          "The Master's external prompt",
          "The absence of a separate environmental-monitoring assignment"
        ],
        "avoid_creating": [
          "A new plan-continuation or sunk-cost rationale at decision point 3",
          "An explicit admission of negligence",
          "A second selective-attention occurrence through repeated missed displays elsewhere"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "hb_01",
      "bias": "Hindsight Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "“Looking back, yes — the reference offset and the thruster caution together were quietly eating into our margin the whole time, and honestly it feels like it should have been fairly obvious that was building toward something.”",
      "evidence_location": "Closing reflective probe after the sequence has been reconstructed.",
      "mechanism": "After knowing that separation narrowed and the job was suspended, the DPO retrospectively describes the developing risk as something that should have been fairly obvious, despite contemporaneous indicators being non-red and individually below action thresholds.",
      "strength": "moderate",
      "confidence": 0.9,
      "plausible_nonbias_explanation": "The participant may be accurately integrating weak signals after a fuller reconstruction, rather than overstating prior foreseeability. Nevertheless, “should have been fairly obvious” is stronger than the contemporaneous account supports.",
      "additional_evidence_needed": "None required, although evidence quantifying the margin trend would strengthen the distinction between legitimate after-action learning and hindsight inflation.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Closing reflection beginning “Looking back, yes...”",
        "current_defect": "None material. The retrospective certainty is limited to the intended closing reflection and contrasts with contemporaneous ambiguity.",
        "minimal_change_instruction": "No change.",
        "preserve": [
          "The phrase indicating retrospective foreseeability",
          "The contemporaneous fact that neither cue independently crossed a threshold",
          "The restriction of this hindsight statement to the closing reflection"
        ],
        "avoid_creating": [
          "Repeated hindsight commentary at earlier decision points",
          "A factual assertion that the outcome was objectively predictable without supporting operational evidence"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "sc_01",
      "bias": "Sunk cost bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "“We'd already gotten through a bit more than half the cargo, and the weather window was closing, so stopping to reassess felt like it would cost us more than it bought us at that stage.”",
      "evidence_location": "Thruster-caution reconstruction.",
      "mechanism": "The continuation justification explicitly foregrounds cargo already transferred and operational time invested, allowing past expenditure to influence the continue-versus-reassess judgment rather than conducting a fully forward-looking margin assessment.",
      "strength": "moderate",
      "confidence": 0.95,
      "plausible_nonbias_explanation": "A shrinking weather window is forward-looking and may legitimately affect the operational choice; however, the reference to having already completed more than half the cargo is an explicit past-investment rationale.",
      "additional_evidence_needed": "None required for the requested occurrence.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, answer beginning “The consequence analysis still showed us within capability...”",
        "current_defect": "None material. The explicit already-completed cargo reference separates this episode from pure default preservation.",
        "minimal_change_instruction": "No change.",
        "preserve": [
          "The more-than-half-completed cargo status",
          "The closing weather window",
          "The continuing formal capability indication",
          "The separate status-quo account in the later follow-up"
        ],
        "avoid_creating": [
          "A second sunk-cost rationale at the OIM final-lift decision",
          "A claim that the operation was necessarily unsafe solely because cargo had already been transferred"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "sq_01",
      "bias": "Status Quo Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "“Not actively, no. It wasn't red, so it didn't really register as something requiring a change in how we were running things. We'd been in that configuration all shift and it had been fine.”",
      "evidence_location": "Follow-up concerning conservative alternatives after the thruster caution.",
      "mechanism": "A changed operating condition does not trigger active generation or comparison of alternatives; the existing configuration is retained because it is familiar, remains non-red, and has worked previously.",
      "strength": "moderate",
      "confidence": 0.94,
      "plausible_nonbias_explanation": "The consequence analysis still showed adequate capability and procedures imposed no mandatory configuration change. Nonetheless, the participant explicitly reports not actively considering the available conservative alternatives because the established configuration had been fine.",
      "additional_evidence_needed": "None required for the requested occurrence.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, response to the question about tightening the watch circle or adjusting reference weighting.",
        "current_defect": "None material. The account identifies default retention separately from the past-investment rationale in sc_01.",
        "minimal_change_instruction": "No change.",
        "preserve": [
          "The distinction between non-red status and the prior configuration's familiarity",
          "The absence of active comparison with conservative alternatives",
          "The separate cargo/time investment rationale supporting sc_01"
        ],
        "avoid_creating": [
          "A second status-quo episode at the OIM decision",
          "A procedural violation not established by the interview"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "fb_01",
      "bias": "Framing Bias",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 4,
      "supporting_quote": "“Mainly the time — eight to ten minutes to complete it... I told him we were good to finish rather than framing it around how much margin we actually had left.”",
      "evidence_location": "Response to the OIM's final-lift continue-or-stand-off question.",
      "mechanism": "The DPO uses time-to-completion as the dominant representation of the choice while insufficiently representing the same operational choice in terms of remaining safety margin.",
      "strength": "weak",
      "confidence": 0.77,
      "plausible_nonbias_explanation": "The account may reflect time pressure, inadequate situation awareness, or failure to conduct a margin reassessment rather than a framing effect. The interview does not show that an alternative presentation of equivalent information would have changed the judgment.",
      "additional_evidence_needed": "Evidence that both time-to-completion and safety-margin representations were available at the moment of choice, and that the time-based representation itself made continuation appear acceptable while a margin-based presentation would have prompted a materially different assessment.",
      "revision_needed": true,
      "revision": {
        "revision_type": "probe_revision",
        "location": "Decision point 4, after the participant explains that the answer was based mainly on eight to ten minutes remaining.",
        "current_defect": "The current wording identifies the metric communicated to the OIM, but it does not establish framing bias rather than ordinary time pressure or an unperformed safety-margin assessment.",
        "minimal_change_instruction": "Add one focused interviewer probe asking whether the DPO had the same information available in a margin format at that moment, followed by a concise response that the short-time formulation made the lift feel finishable and displaced the margin formulation from the immediate decision. Do not state that the DPO knew the exact outcome would occur.",
        "preserve": [
          "The OIM's direct continue-versus-stand-off question",
          "The eight-to-ten-minute estimate",
          "The caution-level equipment status",
          "The later recognition that margin had narrowed",
          "The separation of this episode from decision point 2"
        ],
        "avoid_creating": [
          "A second hindsight-bias statement through a retrospective claim that the margin obviously required standing off",
          "An additional sunk-cost rationale based on prior cargo completion",
          "An unsupported assertion that time and margin were objectively equivalent measures"
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Confirmation Bias",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    },
    {
      "bias": "Automation Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Selective Attention Bias or Inattentional Blindness",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    },
    {
      "bias": "Hindsight Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Sunk cost bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Status Quo Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Framing Bias",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Plan continuation bias",
      "decision_point": 2,
      "supporting_quote": "“Stopping to reassess felt like it would cost us more than it bought us at that stage.”",
      "mechanism": "The operational plan continues after a changed thrust condition, with completion and schedule considerations potentially displacing a fresh go/no-go assessment.",
      "confidence": 0.62,
      "status": "weak",
      "plausible_nonbias_explanation": "This is substantially accounted for by the intended sunk-cost and status-quo mechanisms; continued consequence-analysis capability and the deteriorating weather window also provide legitimate operational reasons to continue.",
      "revision_recommendation": "remove_or_neutralize"
    },
    {
      "bias": "Attentional tunneling",
      "decision_point": 3,
      "supporting_quote": "“The crane boom, almost entirely... [the footprint indicator] is easy for it to sit there unnoticed.”",
      "mechanism": "The DPO's attention narrows around the immediate crane/load task, reducing monitoring of the broader DP and environmental picture.",
      "confidence": 0.81,
      "status": "rejected",
      "plausible_nonbias_explanation": "This is not an additional bias because it is a near-synonymous description of the planned selective-attention/inattentional-blindness occurrence.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "Weather closing faster than forecast and a four-hour crane-operating window",
      "location": "Opening scenario and decision points 1 through 4",
      "why_not_bias": "This is a legitimate operational constraint that creates time pressure. Time pressure alone does not establish any cognitive bias."
    },
    {
      "cue": "Consequence analysis still showed adequate capability after the Thruster 3 caution",
      "location": "Decision point 2",
      "why_not_bias": "Reliance on a relevant formal capability assessment is not inherently biased. The bias-relevant issue is the participant's stated failure to compare alternatives and reliance on past investment, not the existence of the analysis."
    },
    {
      "cue": "Crane and suspended-load monitoring was treated as a high-consequence task",
      "location": "Decision point 3",
      "why_not_bias": "Prioritizing an acute load hazard can be justified expertise. It becomes possible selective-attention bias only if the interview establishes that the DPO had a practicable duty and opportunity to maintain required environmental monitoring."
    },
    {
      "cue": "The footprint indicator was on a secondary display with no audible alarm",
      "location": "Decision point 3",
      "why_not_bias": "This is evidence of display salience and work-system design limitations. It does not by itself demonstrate a cognitive bias in the DPO."
    },
    {
      "cue": "No contact occurred and the vessel remained within the watch circle",
      "location": "Incident outcome description",
      "why_not_bias": "A near-miss or unfavorable outcome cannot retrospectively establish that a prior decision was biased."
    },
    {
      "cue": "The superintendent reminded the crew about the transit schedule",
      "location": "Decision point 2",
      "why_not_bias": "This may contribute to organizational pressure, but the text does not show coercion, authority-gradient compliance, or a direct instruction to continue."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "The reference offset and thruster caution were “quietly eating into” operating margin throughout the job.",
        "support": "The HPR discrepancy, reduced Thruster 3 power availability, and later narrowing separation are described in chronological sequence.",
        "assessment": "Partially supported. Reduced thrust availability plausibly affects capability margin, but an unexplained reference discrepancy primarily affects confidence in position estimation and is not shown to reduce physical separation or propulsion margin directly."
      },
      {
        "claim": "The missed footprint change contributed to the late recognition of changed vessel attitude and narrowing separation.",
        "support": "The wind shift changed the footprint recommendation; the DPO did not notice it until the Master commented on vessel attitude; separation then closed more than expected during the final lift.",
        "assessment": "Moderately supported as a plausible contributing pathway, but the text does not establish the timing, magnitude, or operational effect of the footprint change sufficiently to attribute the later separation reduction solely to the missed cue."
      },
      {
        "claim": "Continuing after the thruster caution contributed to the final near-miss.",
        "support": "The operation continued without configuration change after reduced power availability and later encountered reduced separation margin.",
        "assessment": "Plausible but unproven. The interview lacks quantified reserve capability, environmental-force data, and an account of whether a conservative configuration would have changed the separation outcome."
      }
    ],
    "correlation_causation_risks": [
      "The closing reflection treats the HPR offset and Thruster 3 caution as a unified causal progression without demonstrating that the reference discrepancy caused a reduction in actual physical margin.",
      "The temporal sequence from wind shift to reduced separation does not isolate wind, vessel attitude, crane operations, propulsion degradation, reference reliability, or DP-controller response as causal contributors.",
      "The successful absence of contact should not be used to infer that prior continuation decisions were safe, nor should the near-miss outcome alone be used to prove they were biased."
    ],
    "counterfactual_present": false,
    "changed_variable": "N/A",
    "held_constant": [],
    "causal_coherence": "moderate",
    "explanation": "The narrative supplies a coherent near-miss sequence and identifies plausible interacting contributors, but causal attribution remains underdetermined. It should distinguish degraded physical capability, degraded confidence in reference information, missed environmental information, and operational continuation decisions. The interview contains ordinary hypothetical reflections, but not a controlled counterfactual with one specified changed variable and held-constant conditions."
  },
  "quality_scores": {
    "occupational_realism": 88,
    "cta_fidelity": 90,
    "bias_separability": 72,
    "bias_subtlety": 84,
    "control_fidelity": 100,
    "counterfactual_fidelity": 100,
    "narrative_coherence": 89,
    "naturalness": 86,
    "hidden_label_integrity": 78,
    "overall_quality": 83
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 4,
    "requested_occurrence_total": 7,
    "missing_occurrence_total": 3,
    "accidental_occurrence_total": 0,
    "priority": "medium",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Preserve the four-decision-point chronology: reference discrepancy, thruster caution, missed footprint cue, and final OIM continue-versus-stand-off decision.",
      "Do not use the adverse near-miss outcome as proof that the DPO's earlier reasoning was biased.",
      "Keep automation bias anchored to deference to auto-weighting and GREEN status, while making any confirmation-bias repair about the DPO's own selective evidence weighting.",
      "Do not convert valid time pressure, consequence analysis, crane-hazard monitoring, or secondary-display limitations into bias labels without a demonstrated reasoning mechanism.",
      "Do not add new target-bias episodes to decision points 2 or 4 while repairing the three weak occurrences.",
      "Maintain subtlety by adding observable reasoning or monitoring details rather than explicit statements naming a cognitive bias."
    ],
    "revision_order": [
      "Repair cb_01 with a narrowly targeted indication of selective confirmation of a preferred reference interpretation, distinct from reliance on automated GREEN status.",
      "Repair sa_01 by establishing a practicable expected scan or delegation alternative and the DPO's non-adaptive attentional allocation, without diminishing the legitimate crane hazard.",
      "Repair fb_01 through a focused probe that demonstrates time-to-completion framing displaced an available margin representation, rather than merely documenting time pressure or poor margin awareness.",
      "Review the closing causal reflection and retain its hindsight-bias function while avoiding an unsupported assertion that the HPR discrepancy directly reduced physical station-keeping margin."
    ]
  },
  "failure_flags": [
    "confirmation_bias_mechanism_not_fully_distinguished_from_reasonable_majority_reference_heuristic",
    "selective_attention_mechanism_confounded_by_legitimate_crane_priority_and_interface_salience",
    "framing_bias_mechanism_not_fully_distinguished_from_time_pressure_and_inadequate_margin_reassessment",
    "closing_causal_account_conflates_reference_uncertainty_with_physical_margin_reduction"
  ]
}}}

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
