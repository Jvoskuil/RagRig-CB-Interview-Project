<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay?

Participant: Sure, no problem. Happy to walk through it.

Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart?

Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping downward, and the most recent one landed in the warning zone — inside two sigma, not over the LCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average.

Interviewer: What was going through your mind at that point?

Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three downward-trending points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation.

Interviewer: Walk me through what happened next, chronologically.

Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the LCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real.

Interviewer: At that first decision point, what alternatives did you weigh, and why did you choose to increase sampling rather than halt immediately?

Participant: I could have shut it down right there, or just logged it and kept going. Stopping the line on one warning-zone point felt premature — that costs us 45 minutes of changeover time we might not need, and we're still trying to hit quota. Ignoring it felt reckless given the trend. Increasing sampling was the middle path — get more data fast without committing to downtime.

Interviewer: Once you confirmed the out-of-control signal, what did you look at to figure out the cause?

Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also mentioned to our process engineer what I was seeing, and he said temperature swings had caused drift on that machine before.

Interviewer: Given both the temperature rise and the new lot were roughly time-aligned with the drift, what made you lean toward temperature as the explanation?

Participant: The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.

Interviewer: Did you do anything to directly check the lot hypothesis before moving forward?

Participant: Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.

Interviewer: Let's move to the next stretch of the shift. What came in after that?

Participant: The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine.

Interviewer: How did that sensor reading change your thinking about the tool?

Participant: It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment. I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one.

Interviewer: So what did you decide to do?

Participant: I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away.

Interviewer: Looking back, what alternatives did you consider there, and why didn't the offset feel like enough given what the sensor showed?

Participant: I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was "recently serviced." The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet.

Interviewer: What happened after that adjustment?

Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding. Then shift changeover happened, and the incoming night operator mentioned the tool had sounded different in the last hour — a cue I obviously didn't have access to until after the handoff.

Interviewer: Bring me to the end of the shift. What did the final data show, and what did you decide?

Participant: By the end, several parts were near or slightly under the lower spec limit. The wear sensor was up to 91%. Cpk for the last two hours had dropped from 1.42 to 1.05, which is a real capability hit. At that point I recommended an immediate tool change, a temporary update to the control chart center line, and I filed a deviation report covering the affected parts.

Interviewer: What tipped you fully toward that recommendation?

Participant: The Cpk drop was the clincher, honestly, combined with the wear number climbing another thirteen points in a short window. That's not marginal anymore, that's a tool that's clearly done. And with parts sitting near spec limits, a deviation report was required regardless of what I concluded about the cause.

Interviewer: What happened after the tool change?

Participant: It resolved it. The next shift's dimensions went right back to the historical baseline. And when the lab result on that new material lot finally came back, the hardness was within spec after all — so that wasn't a factor.

Interviewer: If the tool wear data had been available an hour earlier, do you think it would have changed your call at the offset-adjustment point?

Participant: Possibly. If I'd seen 78% that much earlier with more of the shift left, I might have leaned toward the tool change sooner rather than the offset. The compressed time at the end made a bigger intervention feel less appealing.

Interviewer: And if the lot hardness test had come back out of spec instead?

Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early.

Interviewer: Anything you'd do differently in how you weighed the temperature information against the lot information?

Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote.

Interviewer: Last one — how much did the approaching shift changeover and time pressure shape your decisions overall?

Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in.

Interviewer: That's really helpful, thank you for walking through all of that in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Biased_2",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Quality Assurance Analyst (Statistical Process Control)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Drifting Diameter: SPC Signal Investigation on a Precision Machining Line",
    "scenario_summary_internal": "A QA Analyst monitoring an Xbar-R control chart for a machined shaft's outer diameter notices a warning-zone signal. Over the course of a shift, the analyst must triage the signal, form a root-cause hypothesis among several candidate factors (tool wear, incoming material lot, ambient temperature, operator changeover), decide whether to halt the line or continue with in-process adjustment under time pressure, and finally choose a corrective/reporting action. The narrative embeds one correlation bias instance (treating a temperature-dimension co-movement as causal while not equally testing a competing lot-change explanation) and one conservatism bias instance (underweighting new tool-wear sensor evidence relative to a prior belief that the tool was 'recently serviced and unlikely to be worn').",
    "occupational_realism": {
      "objective": "Determine whether an observed shift in a critical dimensional measurement on a precision-machined part represents a true assignable-cause process shift requiring line stoppage and correction, or common-cause variation, while minimizing scrap and downtime.",
      "setting": "A CNC turning cell producing automotive shafts on a two-shift production schedule; QA Analyst monitors real-time SPC software (Xbar-R charts) from a quality office adjacent to the shop floor, with periodic gemba walks to the machine.",
      "constraints": [
        "Production quota for the shift must still be met if possible",
        "Halting the line triggers a formal deviation report and customer notification above a certain scrap threshold",
        "Tooling changeover takes 45 minutes and idles the cell",
        "Only two dimensional measurements per hour are available from the automated gauge, plus manual spot checks",
        "Material lot documentation lags real-time by roughly one hour",
        "Operator shift changeover occurred mid-investigation, creating a possible confound"
      ],
      "stakeholders": [
        "QA Analyst (protagonist)",
        "Line operator (day shift)",
        "Line operator (night shift, incoming)",
        "Process/manufacturing engineer",
        "Plant quality manager",
        "Incoming materials supplier quality contact"
      ],
      "technical_terms_to_use": [
        "Xbar-R chart",
        "upper control limit (UCL)",
        "warning zone / Western Electric rules",
        "assignable cause vs. common cause variation",
        "tool wear offset",
        "Cpk",
        "gauge R&R",
        "material lot traveler",
        "in-process adjustment",
        "deviation report"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "confirmation bias",
        "correlation bias",
        "conservatism bias",
        "heuristic",
        "anchoring",
        "base rate",
        "prior probability"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Xbar-R chart shows the last three subgroup means trending upward, with the most recent point inside the warning zone (between 2-sigma and 3-sigma) but not beyond the UCL",
          "Range chart remains in control, suggesting variability within subgroups is stable",
          "No maintenance or material change has been logged yet for this shift",
          "Production is 62% through the shift's quota"
        ],
        "new_information_after_decision": [
          "The following subgroup mean crosses the UCL outright, confirming an out-of-control signal",
          "A manual spot check confirms the automated gauge reading is not a measurement artifact"
        ],
        "alternatives": [
          "Treat the warning-zone point as common-cause noise and continue monitoring without intervention",
          "Immediately flag the signal as assignable-cause and begin a root-cause investigation",
          "Increase sampling frequency temporarily before deciding either way"
        ],
        "intended_action": "Analyst increases sampling frequency and flags the trend for investigation rather than halting, judged a reasonable moderate response"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Shop floor temperature log shows a 3°C rise over the same two-hour window as the dimensional drift",
          "A new material lot was received and loaded onto the line approximately 90 minutes before the drift began, per the (lagging) lot traveler",
          "Tool wear sensor has not yet been checked at this point",
          "Process engineer mentions temperature swings have 'caused drift before' on this machine"
        ],
        "new_information_after_decision": [
          "The lot traveler is later confirmed to show the new material lot has a hardness spec at the high end of the acceptable range, a plausible independent contributor",
          "Ambient temperature stabilizes on its own within the hour, and dimensions do not immediately return to baseline, weakening the temperature explanation retroactively"
        ],
        "alternatives": [
          "Attribute the drift primarily to the temperature rise given its clear time-alignment with the dimensional trend",
          "Treat the material lot change as an equally or more plausible cause and pull a sample for hardness/dimensional testing before concluding",
          "Hold both hypotheses open and request data on tool wear before assigning a root cause"
        ],
        "intended_action": "Analyst attributes the drift mainly to the temperature co-movement and deprioritizes the lot-change hypothesis without requesting the hardness sample test"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Analyst's working assumption, stated earlier in the shift, is that the tool was replaced two days ago and 'shouldn't be worn yet'",
          "Tool wear sensor data becomes available and shows cumulative cutting distance is already 78% of the rated tool life, well ahead of the expected pace for a two-day-old insert",
          "Dimensional drift direction (diameter trending toward undersize) is consistent with known tool wear signatures on this machine",
          "Time pressure is rising: only 90 minutes remain in the shift and shift changeover is approaching"
        ],
        "new_information_after_decision": [
          "A subsequent part sample shows the diameter continuing to trend toward the lower spec limit",
          "The incoming night-shift operator reports the tool 'sounded different' during the last hour, a cue available only after changeover"
        ],
        "alternatives": [
          "Revise the root-cause assessment substantially toward tool wear and halt the line for a tool change given the sensor reading",
          "Make a small in-process dimensional offset adjustment and continue running while monitoring closely",
          "Continue running unchanged for the remainder of the shift since the tool was 'recently serviced'"
        ],
        "intended_action": "Analyst makes only a small in-process offset adjustment and keeps running, revising the tool-wear likelihood only slightly despite the sensor reading, largely preserving the original 'tool shouldn't be worn' assessment"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "End-of-shift data shows several parts near or slightly below the lower specification limit",
          "Tool wear sensor now reads 91% of rated life",
          "Cpk calculated for the last two hours has dropped from 1.42 to 1.05",
          "A deviation report is required if any parts are confirmed out of spec"
        ],
        "new_information_after_decision": [
          "A full tool change resolves the drift on the next shift, and dimensions return to the historical baseline mean",
          "Retrospective review shows the material lot hardness was within spec after all, unrelated to the drift"
        ],
        "alternatives": [
          "Recommend an immediate tool change, update the control chart center line temporarily, and file a deviation report covering the affected parts",
          "Recommend only closer monitoring next shift without a tool change or deviation report",
          "Recommend a full process capability study before taking any corrective action"
        ],
        "intended_action": "Analyst recommends the tool change and deviation report, closing out the investigation with an accurate final root cause despite the earlier misweighting of evidence"
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first drew your attention to this control chart that shift?",
        "What was your overall objective when you started looking into the signal?"
      ],
      "timeline_reconstruction": [
        "What happened right after you noticed the warning-zone point?",
        "What information came in over the next couple of hours, and in what order?",
        "When did the tool wear sensor data become available relative to the temperature and lot information?"
      ],
      "decision_point_probes": [
        "At the point where you saw the warning-zone signal, what alternatives did you consider, and why did you choose to increase sampling rather than halt immediately?",
        "When you noticed the temperature rise lined up with the drift, what made that explanation feel more compelling than the material lot change? Did you test the lot hypothesis directly?",
        "Once the tool wear sensor showed 78% of rated life, how did that change your thinking about the tool being 'recently serviced'? What made you choose an offset adjustment over a tool change at that point?",
        "By the end of the shift, what evidence finally shifted your recommendation toward a tool change and deviation report?"
      ],
      "closing_hypotheticals": [
        "If the tool wear data had been available an hour earlier, do you think your decision at the halt/continue point would have changed?",
        "If the material lot hardness test had come back out of spec, how would that have affected your root-cause conclusion?",
        "Looking back, is there anything about how you weighed the temperature information versus the lot information that you'd do differently?",
        "How much did the approaching shift changeover and time pressure influence your decisions?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "decision_point": 2,
        "mechanism": "Analyst observes that ambient temperature rise and dimensional drift co-occur in time and infers a causal relationship, while a second plausible cause (new material lot) with comparable temporal proximity is not investigated with equivalent rigor (no hardness/dimensional sample pulled at the time)",
        "affected_reasoning_operation": "Causal attribution from an observed temporal correlation, evidence-selection favoring the co-varying signal over an equally available alternative",
        "evidence_available_at_time": [
          "Temperature log showing 3°C rise coincident with drift window",
          "Lagging material lot traveler showing a new lot loaded ~90 minutes prior",
          "Process engineer's remark that temperature has 'caused drift before'"
        ],
        "required_textual_manifestation": "The analyst explicitly cites the temperature-dimension timing alignment as the reason for favoring the temperature explanation, and explains not testing the lot hypothesis at that time (e.g., citing convenience, engineer's remark, or the lot data being harder to access) rather than citing a data-driven reason to rule out the lot",
        "plausible_nonbias_interpretation": "The engineer's stated history of temperature-related drift on this machine could be treated as legitimate domain expertise justifying a reasonable working hypothesis, not necessarily a bias",
        "strength": "moderate",
        "do_not_make_explicit": [
          "Do not name 'correlation bias'",
          "Do not have the analyst say 'correlation does not imply causation'",
          "Do not have the analyst explicitly acknowledge ignoring the lot hypothesis for no reason"
        ]
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "decision_point": 3,
        "mechanism": "Analyst holds an initial belief that the tool is unlikely to be worn because it was replaced two days prior, and upon receiving strong new sensor evidence (78% of rated tool life already consumed) revises the corrective action only marginally (a small offset) rather than updating substantially toward a tool change",
        "affected_reasoning_operation": "Belief updating in response to new quantitative evidence; selection of corrective action magnitude relative to revised risk estimate",
        "evidence_available_at_time": [
          "Prior stated assumption: tool replaced two days ago, 'shouldn't be worn yet'",
          "Tool wear sensor reading: 78% of rated cutting life consumed",
          "Dimensional drift direction consistent with known tool wear signature",
          "Time pressure from approaching shift changeover"
        ],
        "required_textual_manifestation": "The analyst acknowledges the sensor reading as notable but explains choosing a small offset adjustment rather than a tool change by reiterating the earlier assumption that the tool is still relatively new, indicating the prior belief was not substantially revised despite the strength of the new data",
        "plausible_nonbias_interpretation": "Choosing a smaller intervention could be framed as a reasonable attempt to avoid unnecessary downtime under quota pressure, a legitimate operational trade-off rather than a bias",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Do not name 'conservatism bias'",
          "Do not have the analyst say they are 'sticking to their prior belief'",
          "Do not have the analyst state the sensor reading was ignored outright; the update must be present but insufficient"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for biased condition; no control scenario is being generated under this specification"
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
      "Confirm exactly one correlation bias instance and one conservatism bias instance are embedded, each mapped to a distinct decision point (2 and 3 respectively)",
      "Confirm no bias name, definition, or psychological label appears anywhere in the public interview text",
      "Confirm each of the four decision points contains at least two plausible alternatives and both pre- and post-decision information",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes",
      "Confirm word count falls between 1,215 and 1,485 words, targeting 1,350",
      "Confirm the final outcome (successful tool change and deviation report) does not retroactively prove either embedded bias occurred, since a competent non-biased analyst could have reached the same final action via a different reasoning path",
      "Confirm the material lot hardness result (in spec) is revealed only as background closure, not as an explicit confirmation that the earlier temperature attribution was biased",
      "Confirm no additional instances of correlation bias or conservatism bias are introduced at decision points 1 or 4"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Correlation bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as causal attribution from temporal co-occurrence (temperature vs. dimension drift) while an equally available alternative (material lot) is not tested with equivalent rigor"
      },
      {
        "bias": "Conservatism Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as insufficient belief revision toward tool wear despite strong new quantitative sensor evidence, anchored to an earlier 'tool recently replaced' assumption"
      }
    ],
    "target_bias_names": [
      "Correlation bias",
      "Conservatism Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Correlation bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Conservatism Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "decision_point": 2
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "mechanism": "Causal inference drawn from temporal co-movement of temperature and dimensional drift, with a comparably available material-lot explanation left untested at the same rigor level",
        "affected_reasoning_operation": "Causal attribution and evidence-selection during root-cause hypothesis formation",
        "evidence_source": "Temperature log and material lot traveler, both available within the same investigative window",
        "distinctiveness_requirement": "This is the only planned correlation-bias instance; it must not be repeated as a second independent occurrence elsewhere (e.g., decision point 4's closure of the lot hypothesis is an outcome explanation, not a second instance)"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "mechanism": "Underweighting of new tool-wear sensor evidence (78% of rated life) relative to a prior belief ('tool recently replaced, unlikely worn'), resulting in a corrective action smaller than the updated evidence would justify",
        "affected_reasoning_operation": "Belief updating and proportionality of response magnitude to new evidence at decision point 3",
        "evidence_source": "Tool wear sensor reading and prior stated assumption about tool age",
        "distinctiveness_requirement": "This is the only planned conservatism-bias instance; the eventual full tool change at decision point 4 is a separate, later, adequately-revised decision and must not be coded as a second conservatism instance"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "strength": "moderate"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Biased_2",
    "domain_id": "IP",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (2 and 3) chosen for mechanism fit: correlation bias fits the root-cause hypothesis-formation decision where two co-varying evidence sources exist; conservatism bias fits the halt/continue decision where new quantitative evidence updates a previously stated prior belief. No bias shares a decision point with another instance of itself, so the same-decision-point differentiation rule was not triggered.",
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
          "segment_type": "signal_detection",
          "raw_interview_anchor": "Participant describes three subgroup means creeping downward, the latest point in the warning zone, and a stable range chart.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is factual signal interpretation and process monitoring, without a hidden bias manifestation."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "initial_interpretation",
          "raw_interview_anchor": "Participant weighs quota progress and Western Electric rules, distinguishing one warning-zone point from a meaningful three-point pattern.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The reasoning is a documented, plausible SPC interpretation and is not a hidden instance."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "sampling_and_measurement_check",
          "raw_interview_anchor": "Participant increases sampling, waits for confirmation, then uses a hand micrometer to rule out a gauge artifact.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a reasonable moderate response and measurement-validation action."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "alternative_weighing",
          "raw_interview_anchor": "Participant compares stopping, ignoring the signal, and increasing sampling, choosing a middle path to obtain more data without downtime.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The choice is explicitly justified as an operational trade-off and is not a planted bias."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "cause_investigation",
          "raw_interview_anchor": "Participant reviews temperature, material-lot, and unavailable tool-wear information and consults the process engineer.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This segment establishes the evidence available before the causal-attribution decision."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "causal_attribution_and_hypothesis_testing",
          "raw_interview_anchor": "Participant favors temperature because its timing lined up with the dimensional drift, cites the engineer's prior experience, and does not prioritize a hardness test of the new lot.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["corrbias_01"],
          "ground_truth_rationale": "The participant infers causality from temporal co-movement and leaves a comparably available material-lot hypothesis untested with equivalent rigor."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "new_evidence_interpretation",
          "raw_interview_anchor": "Participant receives the 78% tool-life reading and recognizes the undersize drift as a classic tool-wear signature.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This establishes strong new evidence but does not alone contain the insufficient belief revision that defines the hidden instance."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "belief_updating_and_corrective_action",
          "raw_interview_anchor": "Participant acknowledges the tool-wear reading but says the recently serviced mental model is hard to shake, then chooses a small offset instead of a tool change under time pressure.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["consbias_01"],
          "ground_truth_rationale": "Strong quantitative evidence and a matching wear signature produce only a marginal update toward corrective action because the earlier recent-tool belief remains influential."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "post_adjustment_monitoring",
          "raw_interview_anchor": "Participant reports that the next sample still approached the lower specification limit and that the incoming operator later noticed a different tool sound.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is subsequent evidence and a handoff cue, not an additional hidden bias instance."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "final_escalation_and_reporting",
          "raw_interview_anchor": "Participant uses near-limit parts, 91% tool life, and the Cpk drop to recommend a tool change, center-line update, and deviation report.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The generation specification treats this as an accurate final corrective action, not a second conservatism instance."
        },
        {
          "segment_id": "seg_011",
          "speaker": "Participant",
          "segment_type": "outcome_and_causal_closure",
          "raw_interview_anchor": "Participant reports that the tool change restored baseline dimensions and that the new lot was later confirmed within hardness specification.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is retrospective outcome information and causal closure, explicitly not a new occurrence."
        },
        {
          "segment_id": "seg_012",
          "speaker": "Participant",
          "segment_type": "retrospective_process_improvement",
          "raw_interview_anchor": "Participant says the lot sample could have been pulled earlier to close off an unexamined hypothesis.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is hindsight process improvement, not an additional bias manifestation."
        },
        {
          "segment_id": "seg_013",
          "speaker": "Participant",
          "segment_type": "retrospective_time_pressure_explanation",
          "raw_interview_anchor": "Participant explains that approaching changeover made a full stop less appealing and contributed to choosing the smaller offset first.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a plausible operational explanation of the already-mapped tool decision, not a separate hidden occurrence."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
