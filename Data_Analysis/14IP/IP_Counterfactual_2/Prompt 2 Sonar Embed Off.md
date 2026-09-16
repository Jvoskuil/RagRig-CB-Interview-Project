You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Single-interview cognitive-bias analysis; no separate scientific-paper passages were supplied in this task, so bias labels draw on established cognitive-science knowledge and are flagged as not retrieved."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["congruence bias", "hypothesis myopia", "tunnel vision"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and retain information that confirms or supports one's pre-existing belief or hypothesis while giving disproportionately less attention to alternative hypotheses or disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Cause attribution after confirmed out-of-control signal: temperature vs. material lot",
      "decision_point_description": "Deciding whether to treat temperature as the likely cause and defer direct testing of the new material lot.",
      "affected_reasoning_operation": "causal attribution and hypothesis testing",
      "bias_specific_mechanism": "A favored causal narrative based on temporal correlation led the participant to direct attention and documentation toward the temperature explanation while acknowledging but not actively testing the competing material-lot hypothesis.",
      "manifestation_in_interview": "The participant described the temperature-drift timing as persuasive enough to run with, despite no precedent from the process engineer, and explicitly deferred the lot-hardness test because the temperature explanation felt sufficient.",
      "effect_on_reasoning_or_decision": "The participant did not initially send a hardness sample for the new lot, instead continuing to monitor under the temperature assumption. The lot remained a secondary possibility and was only later ruled out by lab results.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The timing just lined up so cleanly on its own — the temperature started climbing and almost immediately the dimension started walking. I didn't have history to lean on this time, but the correlation itself felt tight enough to run with.",
          "evidence_explanation": "This shows a causal hypothesis being accepted largely on the strength of temporal correlation, without direct evidence linking temperature to the dimensional drift."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.",
          "evidence_explanation": "The participant explicitly deprioritized testing an alternative explanation because the favored temperature explanation felt sufficient, a pattern consistent with confirmation bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not having the engineer's backup actually should have made me want more direct evidence, not less, but in the moment the timing was persuasive enough on its own.",
          "evidence_explanation": "The participant retrospectively identifies that the absence of precedent should have increased the need for direct evidence, but the compelling temporal story suppressed that concern at the time."
        }
      ],
      "correction_or_counterevidence": "The participant did log the material lot as a secondary possibility and later acknowledged that direct lot testing would have been preferable. The lab eventually ruled out the material lot, though that outcome was unknown at the time of the initial reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passages were available in this task; the label and mechanism derive from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment", "insufficient adjustment", "belief perseverance"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information, or anchor, and to inadequately adjust subsequent judgments when new diagnostic information becomes available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to tool wear sensor reading showing 78% of rated tool life",
      "decision_point_description": "Deciding whether to change the tool immediately or make a smaller offset adjustment and continue running.",
      "affected_reasoning_operation": "probabilistic updating and intervention threshold judgment after diagnostic sensor evidence",
      "bias_specific_mechanism": "The initial mental model that the tool was recently serviced and therefore 'basically new' served as an anchor. Although the participant registered the 78% wear reading and classic tool-wear signature, he insufficiently adjusted away from that prior belief when assessing whether to stop for a tool change.",
      "manifestation_in_interview": "The participant expressed surprise at the wear data because he had regarded the insert as recently serviced, then described the prior mental model as difficult to shake. He chose a small in-process offset adjustment rather than an immediate tool change.",
      "effect_on_reasoning_or_decision": "The participant made an offset adjustment instead of changing the tool. The next sample continued trending toward the lower spec limit, and tool wear later climbed to 91% with Cpk falling to 1.05 before an immediate tool change was recommended.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine.",
          "evidence_explanation": "The participant received diagnostic evidence that challenged the prior 'basically new' belief, yet the previous assumption remained salient enough to shape his initial interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.",
          "evidence_explanation": "This explicitly describes a prior mental model functioning as an anchor that resisted updating from the new sensor information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away.",
          "evidence_explanation": "The decision to use an offset rather than pull the tool is consistent with insufficient adjustment from the prior belief, delaying the intervention implied by the wear data."
        }
      ],
      "correction_or_counterevidence": "The participant did not fully dismiss the wear reading, was surprised by it, and eventually updated his judgment when the Cpk dropped to 1.05 and sensor wear climbed to 91%. Time pressure and the approaching shift changeover were also stated as reasons for avoiding an immediate stop, so operational caution likely contributed alongside the anchoring mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passages were available in this task; the label and mechanism derive from established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Analysis is based solely on a retrospective self-report; there was no direct behavioral observation or process data.",
    "No scientific-corpus passages were supplied in this task, so labels rely on established cognitive-science knowledge rather than retrieved evidence.",
    "Time pressure, quota concerns, and legitimate operational caution are present in the interview and may have contributed alongside the identified cognitive mechanisms, particularly for the tool-wear decision."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Counterfactual_2_Sonar_off",
  "interview_id": "IP_Counterfactual_2",
  "system_prompt_id": "Sonar",
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
