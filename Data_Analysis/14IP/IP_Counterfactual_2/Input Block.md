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

Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also asked our process engineer if he'd seen anything like this before, and he said no, actually — this was the first time he'd seen a pattern like this line up with a temperature swing on this particular machine.

Interviewer: Given the engineer didn't have a precedent for you, what made you still lean toward temperature as the explanation?

Participant: The timing just lined up so cleanly on its own — the temperature started climbing and almost immediately the dimension started walking. I didn't have history to lean on this time, but the correlation itself felt tight enough to run with. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.

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

Interviewer: If the engineer had told you this machine had a history of temperature-linked drift, do you think you would have felt any more confident in the temperature explanation than you already did?

Participant: Maybe a little more confident, but honestly the timing alone did most of the convincing for me. Having a precedent would have made it feel more settled, but I don't think it would have changed what I actually did — I was already comfortable running with it based on how closely the two things tracked.

Interviewer: And if the lot hardness test had come back out of spec instead?

Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early.

Interviewer: Looking back, is there anything about how you weighed the temperature information against the lot information that you'd do differently, especially without a precedent to lean on?

Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote. Not having the engineer's backup actually should have made me want more direct evidence, not less, but in the moment the timing was persuasive enough on its own.

Interviewer: How much did the approaching shift changeover and time pressure shape your decisions overall?

Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in.

Interviewer: That's really helpful, thank you for walking through all of that in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Counterfactual_2",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Quality Assurance Analyst (Statistical Process Control)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "The Drifting Diameter (No Prior Anecdote): SPC Signal Investigation on a Precision Machining Line",
    "scenario_summary_internal": "A counterfactual variant of IP_Biased_2 holding the incident, actors, constraints, timeline, sensor readings, and decision structure constant, but removing the process engineer's corroborating anecdote about prior temperature-linked drift on this machine. In the base scenario the engineer's remark ('temperature swings have caused drift before') reinforces the analyst's temporal-correlation attribution at decision point 2. In this counterfactual, the engineer instead states he has not seen this pattern on this machine before. The manifest still requires exactly one correlation bias instance (now resting on temporal alignment alone, without anecdotal reinforcement) and exactly one conservatism bias instance (unchanged, at decision point 3), so the causal test isolates whether the corroborating anecdote is necessary for the correlation-based evidence-selection asymmetry to occur, or whether temporal co-occurrence alone is sufficient.",
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
        "lower control limit (LCL)",
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
          "Xbar-R chart shows the last three subgroup means trending downward, with the most recent point inside the warning zone (between 2-sigma and 3-sigma) but not beyond the LCL",
          "Range chart remains in control, suggesting variability within subgroups is stable",
          "No maintenance or material change has been logged yet for this shift",
          "Production is 62% through the shift's quota"
        ],
        "new_information_after_decision": [
          "The following subgroup mean crosses the LCL outright, confirming an out-of-control signal",
          "A manual spot check confirms the automated gauge reading is not a measurement artifact"
        ],
        "alternatives": [
          "Treat the warning-zone point as common-cause noise and continue monitoring without intervention",
          "Immediately flag the signal as assignable-cause and begin a root-cause investigation",
          "Increase sampling frequency temporarily before deciding either way"
        ],
        "intended_action": "Analyst increases sampling frequency and flags the trend for investigation rather than halting, judged a reasonable moderate response; unchanged from the base scenario"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Shop floor temperature log shows a 3°C rise over the same two-hour window as the dimensional drift",
          "A new material lot was received and loaded onto the line approximately 90 minutes before the drift began, per the (lagging) lot traveler",
          "Tool wear sensor has not yet been checked at this point",
          "COUNTERFACTUAL CHANGE: the process engineer states he has not previously seen temperature swings cause drift on this specific machine, offering no corroborating anecdote"
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
        "intended_action": "Analyst still attributes the drift mainly to the temperature co-movement and deprioritizes the lot-change hypothesis without requesting the hardness sample test, but must now justify this using timing alone rather than citing machine-specific precedent"
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
        "intended_action": "Analyst makes only a small in-process offset adjustment and keeps running, revising the tool-wear likelihood only slightly despite the sensor reading; unchanged from the base scenario"
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
        "intended_action": "Analyst recommends the tool change and deviation report, closing out the investigation with an accurate final root cause; unchanged from the base scenario"
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
        "When you noticed the temperature rise lined up with the drift, what made that explanation feel compelling, even without the engineer confirming he'd seen this pattern before? Did you test the lot hypothesis directly?",
        "Once the tool wear sensor showed 78% of rated life, how did that change your thinking about the tool being 'recently serviced'? What made you choose an offset adjustment over a tool change at that point?",
        "By the end of the shift, what evidence finally shifted your recommendation toward a tool change and deviation report?"
      ],
      "closing_hypotheticals": [
        "If the engineer had told you this machine had a history of temperature-linked drift, do you think you would have felt any more confident in the temperature explanation than you already did?",
        "If the material lot hardness test had come back out of spec, how would that have affected your root-cause conclusion?",
        "Looking back, is there anything about how you weighed the temperature information versus the lot information that you'd do differently, especially without a precedent to lean on?",
        "How much did the approaching shift changeover and time pressure influence your decisions?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "decision_point": 2,
        "mechanism": "Analyst observes that ambient temperature rise and dimensional drift co-occur in time and infers a causal relationship, while a second plausible cause (new material lot) with comparable temporal proximity is not investigated with equivalent rigor; in this counterfactual, the inference rests on temporal alignment alone since the engineer offers no corroborating precedent",
        "affected_reasoning_operation": "Causal attribution from an observed temporal correlation, evidence-selection favoring the co-varying signal over an equally available alternative",
        "evidence_available_at_time": [
          "Temperature log showing 3°C rise coincident with drift window",
          "Lagging material lot traveler showing a new lot loaded ~90 minutes prior",
          "Process engineer's statement that he has not previously observed this pattern on this machine"
        ],
        "required_textual_manifestation": "The analyst explicitly cites the temperature-dimension timing alignment as the reason for favoring the temperature explanation, and explains not testing the lot hypothesis at that time, without invoking any prior machine history since none is offered in this variant",
        "plausible_nonbias_interpretation": "Absent a precedent, the analyst might reasonably treat temperature as one of several open hypotheses pending further data; the counterfactual is designed to test whether the bias still manifests via timing alone",
        "strength": "moderate",
        "do_not_make_explicit": [
          "Do not name 'correlation bias'",
          "Do not have the analyst say 'correlation does not imply causation'",
          "Do not have the analyst invent or imply a prior anecdote that contradicts the engineer's stated lack of one"
        ]
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "decision_point": 3,
        "mechanism": "Analyst holds an initial belief that the tool is unlikely to be worn because it was replaced two days prior, and upon receiving strong new sensor evidence (78% of rated tool life consumed) revises the corrective action only marginally (a small offset) rather than updating substantially toward a tool change",
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
      "paired_scenario_id": "IP_Biased_2",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a counterfactual variant, not a vocabulary or ambiguous control"
    },
    "counterfactual_specification": {
      "causal_variable": "Presence of the process engineer's corroborating anecdote about prior temperature-linked drift on this specific machine, offered during the root-cause discussion at decision point 2",
      "original_state": "The process engineer states that temperature swings have caused drift on this machine before, reinforcing the analyst's temperature-based causal attribution",
      "counterfactual_state": "The process engineer states that he has not previously seen temperature swings cause drift on this machine, providing no corroborating precedent",
      "variables_to_hold_constant": [
        "The QA analyst's role, objective, and constraints",
        "All four decision points and their sequence",
        "The magnitude and timing of the temperature rise (3°C over two hours)",
        "The timing and traveler lag of the new material lot",
        "The tool wear sensor readings (78% then 91% of rated life)",
        "The Cpk decline from 1.42 to 1.05",
        "The offset-adjustment decision and its failure to hold",
        "The incoming operator's report of an unusual tool sound",
        "The final tool-change recommendation and deviation report",
        "The eventual within-spec material lot hardness result",
        "The post-tool-change return to baseline"
      ],
      "expected_causal_difference": "Removing the engineer's corroborating anecdote should not eliminate the analyst's temporal-correlation-based attribution, since the mechanism is defined as resting on temporal co-occurrence rather than social reinforcement; the analyst is expected to still favor temperature and still deprioritize the lot hypothesis, but must justify this using timing evidence alone, without appeal to machine-specific precedent",
      "causal_test_question": "Does the analyst's asymmetric evidence-selection between the temperature and material-lot hypotheses persist when the corroborating anecdote from the process engineer is absent, indicating that temporal co-occurrence alone is sufficient to produce the biased attribution rather than the anecdote being a necessary trigger?"
    },
    "generation_checks": [
      "Confirm exactly one correlation bias instance and one conservatism bias instance are embedded, each mapped to a distinct decision point (2 and 3 respectively), matching the base scenario's allocation",
      "Confirm the only material change from IP_Biased_2 is the presence/absence of the engineer's corroborating anecdote at decision point 2; all other facts, figures, and decision points remain identical",
      "Confirm no bias name, definition, or psychological label appears anywhere in the public interview text",
      "Confirm each of the four decision points contains at least two plausible alternatives and both pre- and post-decision information",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes, including at least one probe on what information would have changed the decision and one on what would have happened if a key feature had been different",
      "Confirm word count falls between 1,215 and 1,485 words, targeting 1,350",
      "Confirm the final outcome (successful tool change and deviation report) does not retroactively prove either embedded bias occurred",
      "Confirm the material lot hardness result (in spec) is revealed only as background closure, not as explicit confirmation that the earlier temperature attribution was biased",
      "Confirm no additional instances of correlation bias or conservatism bias are introduced at decision points 1 or 4",
      "Confirm the counterfactual changes only the specified causal variable (engineer's anecdote) and holds all other material facts constant"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Correlation bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as causal attribution from temporal co-occurrence (temperature vs. dimension drift) while an equally available alternative (material lot) is not tested with equivalent rigor, and must persist without reliance on the (now absent) engineer's corroborating anecdote"
      },
      {
        "bias": "Conservatism Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as insufficient belief revision toward tool wear despite strong new quantitative sensor evidence, anchored to an earlier 'tool recently replaced' assumption; unaffected by the counterfactual variable"
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
        "mechanism": "Causal inference drawn from temporal co-movement of temperature and dimensional drift, with a comparably available material-lot explanation left untested at the same rigor level; in this variant the inference must be shown to rest on timing alone, since no corroborating anecdote is available",
        "affected_reasoning_operation": "Causal attribution and evidence-selection during root-cause hypothesis formation",
        "evidence_source": "Temperature log and material lot traveler, both available within the same investigative window; engineer's statement now disclaims prior precedent rather than confirming it",
        "distinctiveness_requirement": "This is the only planned correlation-bias instance; it must not be repeated as a second independent occurrence elsewhere, and it must not be weakened into non-occurrence merely because the anecdote is absent"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "mechanism": "Underweighting of new tool-wear sensor evidence (78% of rated life) relative to a prior belief ('tool recently replaced, unlikely worn'), resulting in a corrective action smaller than the updated evidence would justify",
        "affected_reasoning_operation": "Belief updating and proportionality of response magnitude to new evidence at decision point 3",
        "evidence_source": "Tool wear sensor reading and prior stated assumption about tool age",
        "distinctiveness_requirement": "This is the only planned conservatism-bias instance; unaffected by the counterfactual variable and must remain structurally identical to the base scenario's instance"
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
    "paired_scenario_id": "IP_Biased_2",
    "counterfactual_variable": {
      "name": "Presence of the process engineer's corroborating anecdote about prior temperature-linked drift on this machine",
      "original_state": "Engineer confirms he has seen temperature swings cause drift on this machine before",
      "changed_state": "Engineer states he has not previously seen this pattern on this machine",
      "variables_to_hold_constant": [
        "QA analyst role and objective",
        "Four decision points and their order",
        "Temperature rise magnitude and timing (3°C over two hours)",
        "Material lot loading timing and traveler lag",
        "Tool wear sensor readings (78% then 91%)",
        "Cpk decline (1.42 to 1.05)",
        "Offset-adjustment decision and outcome",
        "Incoming operator's report of unusual tool sound",
        "Final tool-change and deviation-report decision",
        "Post-hoc material lot hardness result (in spec)",
        "Post-tool-change return to baseline"
      ]
    },
    "scenario_id": "IP_Counterfactual_2",
    "domain_id": "IP",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias, mirroring the base scenario's allocation: correlation bias at decision point 2 (root-cause hypothesis formation) and conservatism bias at decision point 3 (halt/continue decision), preserved unchanged across the counterfactual manipulation. Only the engineer's anecdote at decision point 2 was altered as the causal variable; no reallocation across decision points was needed since neither bias's mechanism fit changed as a result.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "QA analyst role, objective, and constraints",
      "Four decision points and their sequence",
      "Temperature rise magnitude and timing",
      "Material lot loading timing and traveler lag",
      "Tool wear sensor readings and Cpk figures",
      "Offset-adjustment decision and its failure to hold",
      "Incoming operator's report of unusual tool sound",
      "Final tool-change and deviation-report recommendation",
      "Post-hoc material lot hardness result",
      "Post-tool-change return to baseline"
    ],
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
          "segment_type": "signal_observation_and_interpretation",
          "raw_interview_anchor": "Participant: I'm the QA analyst covering statistical process control ... Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant interprets the chart pattern and distinguishes a mean shift from increased within-subgroup variability, but no hidden bias instance is manifested."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "signal_assessment",
          "raw_interview_anchor": "Participant: Honestly, at 62% through the shift's quota ... I didn't have an obvious explanation.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant gives a reasonable Western Electric assessment of a warning-zone point and trend without committing to an unsupported cause."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "sampling_and_measurement_validation",
          "raw_interview_anchor": "Participant: I tightened up sampling instead of pulling the trigger on a full stop ... I knew it was real.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant uses increased sampling and a manual spot check as proportionate process-control actions; neither is a hidden bias occurrence."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "first_decision_action_rationale",
          "raw_interview_anchor": "Participant: I could have shut it down right there ... Increasing sampling was the middle path — get more data fast without committing to downtime.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The alternatives and the moderate sampling choice are the intended non-bias response at decision point 1."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "root_cause_information_gathering",
          "raw_interview_anchor": "Participant: I pulled up everything I had access to in real time ... this was the first time he'd seen a pattern like this line up with a temperature swing on this particular machine.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This segment records the available temperature, lot, tool-wear, and engineer information; the hidden correlation occurrence is localized to the subsequent choice to favor temperature and defer the lot test."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "causal_attribution_and_evidence_selection",
          "raw_interview_anchor": "Participant: The timing just lined up so cleanly on its own ... I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["corrbias_01"],
          "ground_truth_rationale": "The participant treats temporal co-occurrence as sufficient support for the temperature explanation and does not test the comparably available material-lot hypothesis with equivalent rigor, despite lacking engineer precedent."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "tool_wear_update_and_intervention_choice",
          "raw_interview_anchor": "Participant: The tool wear sensor data finally came through ... Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["consbias_01"],
          "ground_truth_rationale": "The participant acknowledges strong 78% tool-wear evidence but remains influenced by the recently-serviced-tool assumption and chooses only a small offset rather than a tool change."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "post_adjustment_assessment",
          "raw_interview_anchor": "Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding ... a cue I obviously didn't have access to until after the handoff.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a consequence and information-availability update after the offset decision, not a separate hidden occurrence."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "final_corrective_action_rationale",
          "raw_interview_anchor": "Participant: By the end, several parts were near or slightly under the lower spec limit ... a deviation report was required regardless of what I concluded about the cause.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The final recommendation is the intended accurate tool-change and deviation-report response at decision point 4."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
