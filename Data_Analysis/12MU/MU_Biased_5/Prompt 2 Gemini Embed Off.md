You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Evaluated the transcript for affirmative mechanism-grounded cognitive bias occurrences. No retrieved scientific corpus passages were supplied in the RAG context, so corpus_evidence arrays are empty and classifications rely on established cognitive-science labels rather than retrieved source metadata."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Fundamental attribution error",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Status quo bias",
      "alternative_labels": [
        "Status quo preference",
        "Default bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for the current state or default course of action, often leading to maintenance of the existing plan even when new information may warrant reconsideration.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Panel 4-to-Panel 5 transition: hold-versus-continue after seismic alert",
      "decision_point_description": "Decision one: whether to hold the Panel 5 first-ring drilling/loading schedule after the geotech team requested 48 hours for analysis, or continue as scheduled.",
      "affected_reasoning_operation": "Risk evaluation and scheduling decision under uncertainty",
      "bias_specific_mechanism": "The participant treated the existing schedule as the default reference point and evaluated continuation as the natural, safe option. This shifted the comparison away from an event-specific risk assessment toward preserving the current plan, with a reduced-advance alternative considered only briefly and then set aside.",
      "manifestation_in_interview": "The participant described the existing plan as the natural course, repeatedly invoked standard practice and how things have always been done, and did not actively weigh a reduced advance rate as a risk mitigation despite acknowledging the geotech request.",
      "effect_on_reasoning_or_decision": "The schedule continued without a pause or reduced advance rate; the existing plan was preserved rather than actively compared against available seismic and convergence signals.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "So that was decision one — do we hold, or keep going. We kept going.",
          "evidence_explanation": "This establishes the choice point and the continuation outcome, though it does not by itself expose the mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, that's just how we've always operated. A single seismic event with convergence a bit above average isn't unusual for that ground — we get blips like that periodically and the standard approach has always been to keep the cycle running unless something more definitive shows up. Stopping the schedule every time there's a minor signal would grind the whole panel transition to a halt, and that's not how we do things here.",
          "evidence_explanation": "This is direct evidence of default/standard-practice framing as the basis for the decision, rather than an event-specific comparison of continuing versus pausing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It came up briefly, but going with the existing plan felt like the natural call given how things normally proceed.",
          "evidence_explanation": "This indicates that a reduced-advance middle ground was not actively analyzed; the existing plan was selected because it felt natural."
        }
      ],
      "correction_or_counterevidence": "Counterevidence: the participant offers an operational rationale that minor seismic blips are common and pausing for every blip would disrupt the panel transition. If this reflects calibrated professional base rates or a deliberate standard procedure, it would be a legitimate heuristic rather than bias. The status quo classification is therefore low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science definitions rather than retrieved source metadata.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": [
        "Representativeness bias",
        "Similarity heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A judgment heuristic in which likelihood or category membership is assessed by similarity to a prototype, often causing neglect of diagnostic base-rate or feature information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Panel 5 ground-support design selection",
      "decision_point_description": "Whether to reuse the Panel 3 support pattern or commission a new ground-support design for Panel 5.",
      "affected_reasoning_operation": "Design selection and geotechnical risk classification based on analogy",
      "bias_specific_mechanism": "The participant judged the Panel 3 pattern as suitable for Panel 5 primarily because Panel 5 looked like a similar rock mass and the pattern had succeeded before. This similarity-based judgment led him to underweight diagnostic geological differences, including different joint orientation and a fault splay present in the exploration data.",
      "manifestation_in_interview": "He acknowledged the exploration differences but stated that the prior pattern's success and visual comparability were the deciding factors; he later said that without the visual resemblance he likely would have pushed for a fresh design.",
      "effect_on_reasoning_or_decision": "The support design for Panel 5 was selected by analogy to Panel 3 rather than being driven by Panel 5-specific ground conditions, increasing reliance on a potentially mismatched support pattern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Panel 5 looked similar on the face of it, so when the contractor asked whether to reuse that pattern or commission something new, I specified the Panel 3 pattern. There was exploration data showing different joint orientation in Panel 5 and a fault splay that Panel 3 didn't have, but the overall rock looked like the same family to me.",
          "evidence_explanation": "This shows that visible similarity and prior success dominated the support choice even though diagnostic geological differences were explicitly known."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I registered them, but my past experience with that pattern working out fine on a comparable-looking panel was really the deciding factor for me.",
          "evidence_explanation": "This confirms that the divergent joint orientation and fault splay were acknowledged but treated as secondary to the similarity-based prototype judgment."
        }
      ],
      "correction_or_counterevidence": "Counterevidence: the Panel 3 pattern had a real track record, and the participant did register the divergent exploration data; visible similarity can be a legitimate initial geotechnical cue. However, his account indicates that the similarity and past success were treated as decisive despite Panel 5-specific differences, supporting the representativeness mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science definitions rather than retrieved source metadata.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Fundamental attribution error",
      "alternative_labels": [
        "Correspondence bias",
        "Over-attribution to disposition"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to over-attribute another person's actions or outcomes to dispositional traits or choices while underweighting situational or environmental causes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Panel 5 fall-of-ground incident attribution",
      "decision_point_description": "Causal attribution and incident report classification for the Panel 5 fall of ground.",
      "affected_reasoning_operation": "Causal attribution and incident classification",
      "bias_specific_mechanism": "When explaining the fall of ground, the participant emphasized the operator's positioning choice, a dispositional and controllable action, and treated the previous shift's elevated joint-density flag and unsupported back ground conditions as less central, even though both were available. This produced a person-centric causal account of the incident.",
      "manifestation_in_interview": "He stated that the operator's positioning was the piece directly within his control and the more immediate explanation that was easiest to point to, while explicitly acknowledging the joint density flag was secondary.",
      "effect_on_reasoning_or_decision": "The incident report emphasized operator positioning, potentially underweighting geotechnical and situational factors in the fall of ground and misallocating causal responsibility.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He was under an unsupported section of back when it came down, and that's a positioning call he makes every shift. That's the part of the incident that was directly within his control, so that's where I put the emphasis in the report.",
          "evidence_explanation": "This shows a dispositional attribution focused on the operator's control and decision, rather than the unsupported ground as a situational cause."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was noted, but the more immediate explanation was where the loader was actually sitting at the time. That's the piece that was in front of me and easiest to point to.",
          "evidence_explanation": "This demonstrates that the elevated joint-density flag was available but treated as less explanatory than the operator's positioning, consistent with underweighting situational factors."
        }
      ],
      "correction_or_counterevidence": "Counterevidence: loader position under unsupported back is a legitimate immediate safety and causal factor, and the operator's positioning choice may be within his control. However, the participant also had the prior shift's elevated joint-density log and the operator's statement that he stayed in the marked safe zone; the emphasis on dispositional control illustrates the attribution bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science definitions rather than retrieved source metadata.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overconfidence bias",
        "Illusion of control"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A systematic tendency to overestimate the accuracy of one's judgments, the adequacy of available information, or one's ability to control future outcomes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final Panel 5 firing approval",
      "decision_point_description": "Final go/no-go decision on firing the next Panel 5 ring before the full geotech review was complete.",
      "affected_reasoning_operation": "Safety-critical go/no-go judgment under uncertainty",
      "bias_specific_mechanism": "The participant treated the threshold-clearing factor of safety as sufficiently concrete and relied on his own prior experience to assume that any post-blast problems could be managed adaptively. This inflated confidence overshadowed known informational gaps, including Panel 3 calibration parameters and spalling reports not present in the model.",
      "manifestation_in_interview": "He pointed to the specific 1.42 number as something concrete, characterized minor spalling as not usually changing the picture, and said he was confident he could respond to post-blast issues rather than waiting for the review.",
      "effect_on_reasoning_or_decision": "The participant gave the go-ahead despite the stability model being uncalibrated for Panel 5 and excluding spalling reports, because subjective confidence and prior experience substituted for resolving the outstanding geotechnical uncertainty.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It's a specific number, calculated from our stability model, and it cleared our standard threshold. That gave me something concrete to point to when the manager needed an answer. As for the spalling reports, minor spalling happens periodically in that ground and doesn't usually change the overall picture.",
          "evidence_explanation": "This shows the participant using the threshold-clearing number as a concrete justification while downplaying spalling reports that were omitted from the model."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "On top of that, I've managed plenty of ground issues before — if something came up post-blast, I was confident we could respond and adjust support on the fly. That's part of why I felt comfortable saying go rather than waiting out the review.",
          "evidence_explanation": "This is direct evidence of overconfidence: his subjective confidence in adaptive post-blast response substituted for waiting on the incomplete geotechnical review."
        }
      ],
      "correction_or_counterevidence": "Counterevidence: the 1.42 factor of safety did clear an explicit standard threshold, and operational pressures may make a time-limited risk decision rational. However, the known calibration mismatch, omitted spalling reports, and his appeal to personal track record as a reason to proceed support overconfidence rather than a purely evidence-based decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science definitions rather than retrieved source metadata.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring effect",
      "alternative_labels": [
        "Anchoring heuristic",
        "Insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final Panel 5 firing approval",
      "supporting_interview_quote": "It's a specific number, calculated from our stability model, and it cleared our standard threshold. That gave me something concrete to point to when the manager needed an answer.",
      "plausible_mechanism": "The 1.42 factor-of-safety figure may have served as a focal numeric anchor, leading to insufficient adjustment for the fact that the model used Panel 3 calibration parameters and did not include scaling crew spalling reports.",
      "why_not_identified": "The transcript more clearly supports overconfidence and reliance on own track record; the factor-of-safety value was also an explicit threshold criterion, so a distinct anchoring effect is plausible but not separately confirmed."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied, so the bias labels and mechanisms are not validated against retrieved scientific literature in this task.",
    "The evaluation is based on retrospective self-report; the participant's account may omit or reconstruct details, which can itself introduce memory or self-presentation distortions.",
    "Objective mine data, model outputs, and incident records were not available to independently verify the decision environment or the actual influence of the described mechanisms.",
    "Some episodes contain plausible professional-heuristic explanations, so confidence ratings reflect residual uncertainty rather than definitive demonstration of distortion."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Biased_5_Gemini_off",
  "interview_id": "MU_Biased_5",
  "system_prompt_id": "Gemini",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
