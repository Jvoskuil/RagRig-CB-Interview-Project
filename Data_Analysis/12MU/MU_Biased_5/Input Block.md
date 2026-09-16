<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary cognitive task analysis session — I'll ask about a specific incident from your work as Mine Planning Engineer, and there are no right or wrong answers. Are you okay with that?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Can you start by describing your role during the Panel 4 to Panel 5 transition?

Participant: Sure. I own the extraction sequence and the stope firing schedule for that block. I coordinate with the geotech team on ground support design, and I'm the one who signs off before a ring gets loaded and fired. At the time, we were about six percent behind our quarterly tonnage target, so there was real pressure to keep the cycle moving from Panel 4 into Panel 5 without gaps.

Interviewer: Give me an overview of what happened, start to finish.

Participant: It started overnight — seismic monitoring picked up an event near the Panel 4 abutment, and convergence readings ticked up a bit above the trailing thirty-day average. Nothing dramatic, but the geotech team flagged it and said they'd want about forty-eight hours to run a full analysis. Problem was, Panel 5's first ring was already scheduled to be drilled and loaded that same shift. So that was decision one — do we hold, or keep going.

We kept going. Then came the support design question for Panel 5. I'd actually designed the support pattern for Panel 3 myself, two years back, and it held up well — no major incidents there. Panel 5 looked similar on the face of it, so when the contractor asked whether to reuse that pattern or commission something new, I specified the Panel 3 pattern. There was exploration data showing different joint orientation in Panel 5 and a fault splay that Panel 3 didn't have, but the overall rock looked like the same family to me.

A while after that, we had a fall of ground in the Panel 5 heading. No injuries, but it wrecked a loader bucket. The incident report noted the loader was sitting under an unsupported back at the time. There was also a log entry from the previous shift flagging elevated joint density in that exact section. The operator said he'd stayed inside the marked safe zone. I logged it mainly as a positioning issue on his part.

Then the last piece — the updated stability model came back with a factor of safety of 1.42 for Panel 5, though it was still using calibration parameters from Panel 3. The scaling crew was also reporting some intermittent minor spalling that wasn't in the model inputs. The mine manager wanted a final go or no-go on firing the next ring, and the full geotech review was still about twelve hours out. I gave the go-ahead.

Interviewer: Let's reconstruct that in order. What exactly did you know at the moment the seismic alert came in?

Participant: Just the magnitude reading, the convergence trend, and the geotech team's request for more time. No damage reports, no visible ground distress reported by anyone underground at that point.

Interviewer: And between that alert and the support design decision — what changed?

Participant: Drilling for Panel 5 went ahead as scheduled. It was sometime after that a shift supervisor mentioned unusual jointing in the Panel 5 heading that hadn't been logged before — that came after I'd already committed to the pattern.

Interviewer: Take me through the incident itself and what you had in front of you right before the final firing approval.

Participant: Right before firing, I had the model's 1.42 figure, the scaling crew's spalling reports, and the manager pushing for an answer since the jumbo and support crew were both booked and costly to reshuffle. The full geotech write-up wasn't in yet.

Interviewer: Back to that first call — why continue the schedule rather than pause for the review?

Participant: Honestly, that's just how we've always operated. A single seismic event with convergence a bit above average isn't unusual for that ground — we get blips like that periodically and the standard approach has always been to keep the cycle running unless something more definitive shows up. Stopping the schedule every time there's a minor signal would grind the whole panel transition to a halt, and that's not how we do things here.

Interviewer: Did you weigh the option of a reduced advance rate as a middle ground?

Participant: It came up briefly, but going with the existing plan felt like the natural call given how things normally proceed.

Interviewer: On the support pattern — walk me through what tipped it toward reusing the Panel 3 design.

Participant: I designed that pattern myself, and it performed well for the whole life of Panel 3. When you've got something with that track record, and Panel 5 looked like a similar rock mass to me, it's hard not to lean on what you know already works. The differences in the exploration data were there, but Panel 3's success carried a lot of weight in my head at that point.

Interviewer: Did the differing joint orientation and fault splay factor into the choice at all?

Participant: I registered them, but my past experience with that pattern working out fine on a comparable-looking panel was really the deciding factor for me.

Interviewer: On the fall of ground — what led you to attribute it mainly to the operator's positioning?

Participant: He was under an unsupported section of back when it came down, and that's a positioning call he makes every shift. That's the part of the incident that was directly within his control, so that's where I put the emphasis in the report.

Interviewer: The joint density flag from the previous shift — how did that factor in?

Participant: It was noted, but the more immediate explanation was where the loader was actually sitting at the time. That's the piece that was in front of me and easiest to point to.

Interviewer: And the final firing approval — what made the 1.42 figure sufficient to move forward?

Participant: It's a specific number, calculated from our stability model, and it cleared our standard threshold. That gave me something concrete to point to when the manager needed an answer. As for the spalling reports, minor spalling happens periodically in that ground and doesn't usually change the overall picture. On top of that, I've managed plenty of ground issues before — if something came up post-blast, I was confident we could respond and adjust support on the fly. That's part of why I felt comfortable saying go rather than waiting out the review.

Interviewer: How much time pressure did you feel across these four moments?

Participant: Significant, especially by the last one. The jumbo and crew were booked, we were behind on tonnage, and the manager wanted a firm answer that day.

Interviewer: How confident were you in each call at the time?

Participant: Fairly confident on the schedule and support decisions. Less certain on the incident attribution — I knew there were two plausible explanations there. Confident again on the firing approval, mostly because of the number and my own track record handling this kind of ground.

Interviewer: What would have needed to be different for you to decide differently at any of these points?

Participant: If the full geotech review had come in before I had to commit, that would have changed things at more than one stage. Same if the model had been recalibrated specifically for Panel 5's rock mass rather than borrowing Panel 3's parameters.

Interviewer: If Panel 5 hadn't looked visually similar to Panel 3, would the support decision have gone differently?

Participant: Probably, yes. Without that resemblance I likely would have pushed harder for a fresh design straight away.

Interviewer: Looking back, what single piece of information would have most changed your approach?

Participant: Getting the geotech review completed before the firing decision, honestly. Everything else stemmed from having to act while that was still open.

Interviewer: That's a good place to end. Thanks for walking through all of that in detail.

Participant: No problem.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Biased_5",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Mine Planning Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Panel 5 Extraction Sequencing Under Seismic Uncertainty",
    "scenario_summary_internal": "A mine planning engineer at an underground hard-rock metal mine must decide whether to proceed with a scheduled transition from Panel 4 to Panel 5 sublevel stoping after an overnight seismic event and rising convergence readings near the panel 4 abutment. Production targets for the quarter are behind, the geotechnical team's report is preliminary, and the engineer must reconcile a numerical stability model, prior experience with a superficially similar panel, a minor fall-of-ground incident report, and pressure from the mine manager to keep the blast schedule intact. The narrative follows the engineer from the morning planning meeting through the shift-end review, culminating in a go/no-go call on firing the next stope ring.",
    "occupational_realism": {
      "objective": "Decide how to sequence and support the Panel 5 stope extraction while managing an emerging ground-stability concern without derailing the quarterly production schedule.",
      "setting": "Underground sublevel stoping operation, hard-rock base-metal mine, transition between Panel 4 (near completion) and Panel 5 (next scheduled panel), during a single 24-hour period spanning night shift alert through day shift planning decision.",
      "constraints": [
        "Quarterly production target is already 6% behind plan",
        "Geotechnical team has only preliminary seismic and convergence data, full analysis will take 48 hours",
        "Ground support crew and drill jumbo are scheduled and costly to remobilize if delayed",
        "Mine manager is pushing to maintain the blast cycle",
        "Panel 5 stability model was calibrated using data from Panel 3, not Panel 5's actual rock mass"
      ],
      "stakeholders": [
        "Mine Planning Engineer (interviewee)",
        "Chief Geotechnical Engineer",
        "Mine Manager",
        "Underground Shift Supervisor",
        "Ground Support Contractor",
        "Equipment Operator involved in fall-of-ground incident"
      ],
      "technical_terms_to_use": [
        "sublevel stoping",
        "convergence monitoring",
        "factor of safety (FOS)",
        "seismic event magnitude",
        "abutment stress",
        "fall of ground (FOG)",
        "ground support design",
        "stope firing schedule",
        "rock mass rating (RMR)",
        "extraction sequence"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation",
        "psychological terminology of any kind"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Overnight seismic monitoring recorded a magnitude event near the Panel 4 abutment",
          "Convergence readings in Panel 4 rose modestly above the trailing 30-day average",
          "The original firing schedule calls for Panel 5's first ring to be drilled and loaded this shift",
          "Geotechnical team requests 48 hours to complete a full review"
        ],
        "new_information_after_decision": [
          "Drilling proceeds on the original schedule",
          "A shift supervisor later flags unusual jointing patterns in the Panel 5 heading not previously logged"
        ],
        "alternatives": [
          "Proceed with the existing firing schedule as planned pending the geotech review",
          "Pause the schedule and wait for the 48-hour geotechnical review",
          "Proceed but reduce the ring advance rate as an interim precaution"
        ],
        "intended_action": "Engineer authorizes continuation of the existing schedule, treating the seismic reading as within normal operating variation because that has always been the standing procedure."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Panel 5's rock mass exhibits some visual similarities to Panel 3, which the engineer personally designed support for two years earlier",
          "Panel 3's support design performed well with no major incidents",
          "Panel 5's exploration drilling data shows different joint orientation and a fault splay not present in Panel 3",
          "Ground support contractor asks whether to use the Panel 3 pattern or commission a new design"
        ],
        "new_information_after_decision": [
          "Support pattern from Panel 3 is specified for Panel 5",
          "A geotechnical technician later notes the joint sets in Panel 5 are oriented closer to the fault splay than anything encountered in Panel 3"
        ],
        "alternatives": [
          "Reuse the Panel 3 support pattern given its past success",
          "Commission a new site-specific support design based on Panel 5's actual exploration data",
          "Request an independent geotechnical review before specifying support"
        ],
        "intended_action": "Engineer specifies the Panel 3 support pattern for Panel 5, citing personal past success with that pattern as sufficient justification."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A minor fall of ground occurs in the Panel 5 heading, injuring no one but damaging a loader bucket",
          "Incident report notes the loader was positioned under an unsupported back at the time",
          "Ground conditions log shows the affected section had elevated joint density flagged the previous shift",
          "Equipment operator states he followed the marked safe-operating zone"
        ],
        "new_information_after_decision": [
          "Incident is logged primarily as an operator positioning error",
          "A later scaling inspection finds loose ground beyond the marked zone, consistent with the joint density flag"
        ],
        "alternatives": [
          "Attribute the incident primarily to operator positioning error",
          "Attribute the incident primarily to unaddressed ground conditions flagged the prior shift",
          "Treat the cause as undetermined pending a joint investigation"
        ],
        "intended_action": "Engineer attributes the fall of ground mainly to the operator's positioning decision rather than to the previously flagged ground conditions."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Updated stability model returns a Panel 5 factor of safety of 1.42, calculated using Panel 3 calibration parameters",
          "Field scaling crew reports intermittent minor spalling not reflected in the model inputs",
          "Mine manager requests final go/no-go confirmation to fire the next ring",
          "Chief geotechnical engineer's full 48-hour review is still twelve hours from completion"
        ],
        "new_information_after_decision": [
          "Ring is fired on schedule",
          "Post-blast inspection finds greater-than-modeled fracturing near the fault splay, prompting an unplanned support upgrade"
        ],
        "alternatives": [
          "Approve firing based on the model's calculated factor of safety",
          "Delay firing until the geotechnical review is complete",
          "Approve firing with additional interim scaling and monitoring as a condition"
        ],
        "intended_action": "Engineer approves firing, treating the model's 1.42 factor of safety as a precise and sufficient basis while also expressing personal confidence in his ability to manage any ground issues that arise."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role in the Panel 4 to Panel 5 transition.",
        "Walk me through what a typical shift handover looked like before this incident."
      ],
      "timeline_reconstruction": [
        "What did you know when you first heard about the overnight seismic event?",
        "What happened between the seismic alert and the decision to specify support for Panel 5?",
        "Take me through the sequence of events around the fall-of-ground incident.",
        "What information did you have right before authorizing the final ring firing?"
      ],
      "decision_point_probes": [
        "What cues told you the seismic reading was or wasn't a concern?",
        "What sources of information did you weigh most heavily when choosing the support pattern, and why?",
        "What alternatives did you consider before deciding what caused the fall of ground?",
        "What was your basis for approving the firing given the outstanding geotechnical review?",
        "Had you handled a similar situation before? How did that shape your decision this time?",
        "How much time pressure did you feel at each of these moments?",
        "How confident were you in each decision at the time you made it?",
        "What would you have needed to see to decide differently?"
      ],
      "closing_hypotheticals": [
        "If the geotechnical review had come back before you had to decide, what might you have done differently?",
        "If Panel 5 had shown no visual similarity to Panel 3, would your support decision have changed?",
        "Looking back, what single piece of information, if available earlier, would have most changed your approach?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Status quo bias",
        "decision_point": 1,
        "mechanism": "Engineer defaults to continuing the pre-existing firing schedule despite a new seismic signal, treating deviation from the established plan as requiring more justification than continuation of the plan.",
        "affected_reasoning_operation": "Evaluation of whether to change an existing operational plan in light of new monitoring data",
        "evidence_available_at_time": [
          "Seismic event overnight near Panel 4 abutment",
          "Convergence readings modestly above trailing average",
          "Geotech team's request for 48-hour review window"
        ],
        "required_textual_manifestation": "Engineer explains continuing the schedule primarily by reference to it being the established procedure or the way things have always been run, rather than a fresh risk-based justification for that specific reading.",
        "plausible_nonbias_interpretation": "The reading may genuinely fall within normal operating variation and continuing could be a defensible engineering judgment based on threshold criteria.",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "default bias", "inertia"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Experience Bias",
        "decision_point": 2,
        "mechanism": "Engineer generalizes a personally successful past support design from Panel 3 to Panel 5 based on surface similarity, discounting Panel 5's distinct exploration data showing different joint orientation and a fault splay.",
        "affected_reasoning_operation": "Transfer of a prior solution to a new case based on recalled personal success rather than re-evaluation of case-specific evidence",
        "evidence_available_at_time": [
          "Panel 3 support pattern history and personal design authorship",
          "Panel 5 exploration drilling data showing different joint orientation and fault splay",
          "Contractor's request for confirmation of pattern choice"
        ],
        "required_textual_manifestation": "Engineer justifies reusing the Panel 3 pattern mainly by citing personal past success with it, without independently weighing the differing exploration data for Panel 5.",
        "plausible_nonbias_interpretation": "Reusing a proven design could be a reasonable efficiency measure if the engineer believed the differences were immaterial to support requirements.",
        "strength": "moderate",
        "do_not_make_explicit": ["experience bias", "overgeneralization", "past success bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Attribution Bias",
        "decision_point": 3,
        "mechanism": "Engineer attributes the fall-of-ground incident predominantly to the equipment operator's positioning choice (a dispositional/behavioral cause) while underweighting the previously logged ground-condition flag (a situational cause).",
        "affected_reasoning_operation": "Causal attribution of an adverse event to person versus situation given conflicting evidence",
        "evidence_available_at_time": [
          "Incident report noting operator positioning under an unsupported back",
          "Ground conditions log flagging elevated joint density the previous shift",
          "Operator's statement that he followed the marked safe-operating zone"
        ],
        "required_textual_manifestation": "Engineer's account of the incident foregrounds the operator's positioning decision as the primary cause and treats the joint density flag as a secondary or incidental detail, despite both being available at the time.",
        "plausible_nonbias_interpretation": "The operator may indeed have deviated from the marked zone, making a behavior-focused explanation a legitimate partial account.",
        "strength": "subtle",
        "do_not_make_explicit": ["attribution bias", "fundamental attribution error", "blame"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of validity",
        "decision_point": 4,
        "mechanism": "Engineer treats the model-derived factor of safety (1.42) as a precise and reliable indicator of ground stability, despite it being calculated from Panel 3 calibration parameters and conflicting with fresh field spalling observations.",
        "affected_reasoning_operation": "Weighting of a quantitative model output versus qualitative field observation when forming a confidence judgment about ground stability",
        "evidence_available_at_time": [
          "Stability model output of FOS 1.42 using Panel 3 calibration parameters",
          "Field scaling crew reports of intermittent minor spalling not reflected in model inputs",
          "Outstanding geotechnical review not yet complete"
        ],
        "required_textual_manifestation": "Engineer describes the numerical FOS value as a firm basis for the go decision, referencing its precision or specificity, while treating the field spalling reports as not requiring a revision of that judgment.",
        "plausible_nonbias_interpretation": "A calculated FOS above 1.0 is a legitimate standard industry threshold, so relying on it could reflect a reasonable, if incomplete, decision rule.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "false precision", "model overreliance"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Engineer expresses high personal confidence in his own ability to manage or respond to any ground issues that might arise after firing, distinct from and in addition to his reliance on the model output itself.",
        "affected_reasoning_operation": "Self-assessment of personal capability to control or mitigate uncertain future outcomes",
        "evidence_available_at_time": [
          "Personal track record of managing prior ground-support issues",
          "Outstanding uncertainty in the geotechnical review",
          "Mine manager's request for a firm go/no-go answer"
        ],
        "required_textual_manifestation": "Engineer states confidence in his personal capacity to handle whatever ground issues emerge, framed as a reason to proceed, separate from the model's numerical output.",
        "plausible_nonbias_interpretation": "Confidence grounded in genuine relevant experience and contingency planning could be a legitimate professional judgment rather than miscalibration.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence bias", "miscalibration", "self-assessment error"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the biased-condition scenario with no paired control specified in this generation cycle."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly four decision points exist and each has at least two plausible alternatives.",
      "Confirm each of the five requested biases has exactly one embedded instance with a unique instance_id.",
      "Confirm decision point 4 hosts two distinct instances (cb_04, cb_05) with different evidence sources (model output vs. self-assessed capability) and different reasoning operations.",
      "Confirm no bias label, definition, or psychological term appears in the planned interview text.",
      "Confirm each occurrence includes a plausible non-bias interpretation to avoid mechanical proof of bias.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm projected interview length falls between 1,215 and 1,485 words without repetitive exposition.",
      "Confirm technical vocabulary matches underground hard-rock mining and mine planning terminology throughout."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusion of validity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as treating the quantitative FOS model output as precise/reliable despite conflicting field evidence and mismatched calibration source."
      },
      {
        "bias": "Attribution Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as favoring a person-focused (operator) causal explanation over an available situational (ground condition) explanation for the fall-of-ground incident."
      },
      {
        "bias": "Experience Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as transferring a personally successful past design (Panel 3) to a new case (Panel 5) based on recalled experience rather than case-specific evidence."
      },
      {
        "bias": "Status quo bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as defaulting to continuation of the pre-existing schedule in response to new information rather than a fresh risk-based justification."
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an explicit expression of personal confidence in one's own capability to manage uncertain future outcomes, separate from reliance on the model output."
      }
    ],
    "target_bias_names": [
      "Illusion of validity",
      "Attribution Bias",
      "Experience Bias",
      "Status quo bias",
      "Overconfidence Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Illusion of validity", "requested_occurrences": 1 },
      { "bias": "Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Experience Bias", "requested_occurrences": 1 },
      { "bias": "Status quo bias", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Status quo bias" },
      { "instance_id": "cb_02", "bias": "Experience Bias" },
      { "instance_id": "cb_03", "bias": "Attribution Bias" },
      { "instance_id": "cb_04", "bias": "Illusion of validity" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Status quo bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Experience Bias", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Attribution Bias", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Illusion of validity", "decision_point": 4 },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Status quo bias",
        "mechanism": "Defaulting to the pre-existing firing schedule despite new seismic/convergence data, treating continuation as requiring less justification than change.",
        "affected_reasoning_operation": "Evaluation of whether to alter an existing operational plan given new monitoring data",
        "evidence_source": "Overnight seismic and convergence monitoring data",
        "distinctiveness_requirement": "Must be tied to the decision to keep the original schedule, not to any support design or attribution judgment."
      },
      {
        "instance_id": "cb_02",
        "bias": "Experience Bias",
        "mechanism": "Generalizing a personally successful past support design from a superficially similar panel without adequately weighing case-specific exploration data.",
        "affected_reasoning_operation": "Transfer of a prior solution to a new case based on recalled personal success",
        "evidence_source": "Panel 3 personal design history versus Panel 5 exploration drilling data",
        "distinctiveness_requirement": "Must be tied to support pattern selection, distinct from the scheduling decision at decision point 1."
      },
      {
        "instance_id": "cb_03",
        "bias": "Attribution Bias",
        "mechanism": "Favoring a dispositional/behavioral causal explanation (operator error) over an available situational explanation (flagged ground conditions) for the fall-of-ground incident.",
        "affected_reasoning_operation": "Causal attribution of an adverse event to person versus situation",
        "evidence_source": "Incident report and ground conditions log versus operator statement",
        "distinctiveness_requirement": "Must be tied specifically to incident causation, not to the firing approval decision at decision point 4."
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of validity",
        "mechanism": "Treating a precise numerical model output as a reliable basis for judgment despite mismatched calibration source and conflicting field evidence.",
        "affected_reasoning_operation": "Weighting of quantitative model output versus qualitative field observation",
        "evidence_source": "Stability model FOS output (1.42) calibrated on Panel 3 parameters",
        "distinctiveness_requirement": "Evidence source is the model's numerical output, distinguishing it from cb_05's evidence source of self-assessed personal capability."
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "mechanism": "Expressing high confidence in personal capability to manage uncertain future ground issues, independent of the model output itself.",
        "affected_reasoning_operation": "Self-assessment of personal capability to control or mitigate uncertain outcomes",
        "evidence_source": "Personal track record and self-assessment of managing prior ground-support issues",
        "distinctiveness_requirement": "Evidence source is self-referential capability assessment, distinguishing it from cb_04's reliance on the external model output."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Status quo bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Experience Bias", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Attribution Bias", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Illusion of validity", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_5",
    "domain_id": "MU",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across four decision points per mechanism fit and narrative realism; two occurrences (cb_04, cb_05) co-located at decision point 4 because both plausibly arise at the final go/no-go call, but assigned distinct evidence sources (external model output vs. self-referential capability judgment) and distinct reasoning operations per Rule 4 of the allocation rules; no bias received more than one instance at any single decision point.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "support_design_selection",
        "raw_interview_anchor": "Panel 5 looked similar on the face of it, so when the contractor asked whether to reuse that pattern or commission something new, I specified the Panel 3 pattern. There was exploration data showing different joint orientation in Panel 5 and a fault splay that Panel 3 didn't have, but the overall rock looked like the same family to me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "The participant transfers a personally successful Panel 3 support design to Panel 5 based on surface similarity while discounting case-specific exploration evidence."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "incident_causal_attribution",
        "raw_interview_anchor": "He was under an unsupported section of back when it came down, and that's a positioning call he makes every shift. That's the part of the incident that was directly within his control, so that's where I put the emphasis in the report. It was noted, but the more immediate explanation was where the loader was actually sitting at the time. That's the piece that was in front of me and easiest to point to.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "The participant foregrounds the operator's behavior and downweights the available elevated-joint-density ground-condition explanation when attributing the fall of ground."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "schedule_continuation_rationale",
        "raw_interview_anchor": "Honestly, that's just how we've always operated. A single seismic event with convergence a bit above average isn't unusual for that ground — we get blips like that periodically and the standard approach has always been to keep the cycle running unless something more definitive shows up. Stopping the schedule every time there's a minor signal would grind the whole panel transition to a halt, and that's not how we do things here.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "The participant justifies continuing the pre-existing schedule primarily by established practice and normal operating procedure despite new seismic and convergence information."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "final_firing_approval_rationale",
        "raw_interview_anchor": "It's a specific number, calculated from our stability model, and it cleared our standard threshold. That gave me something concrete to point to when the manager needed an answer. As for the spalling reports, minor spalling happens periodically in that ground and doesn't usually change the overall picture. On top of that, I've managed plenty of ground issues before — if something came up post-blast, I was confident we could respond and adjust support on the fly. That's part of why I felt comfortable saying go rather than waiting out the review.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_04", "cb_05"],
        "ground_truth_rationale": "The participant treats the 1.42 model output as a concrete sufficient basis despite mismatched calibration and spalling, and separately relies on confidence in personal ability to manage future ground issues."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
