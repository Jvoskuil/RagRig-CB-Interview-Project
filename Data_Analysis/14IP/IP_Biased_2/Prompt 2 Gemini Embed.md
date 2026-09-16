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
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "The evaluation considered only the participant's reported reasoning and decisions during the process event, using the retrieved corpus for terminology and mechanism validation."
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
      "confidence": "low",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "hypothesis-confirmation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, favor, and prioritize information that supports an existing hypothesis while under-weighting, avoiding, or failing to directly test plausible alternative hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Cause attribution after out-of-control signal",
      "decision_point_description": "Choosing whether to directly test the new material lot versus proceeding with temperature as the working explanation.",
      "affected_reasoning_operation": "Causal attribution and hypothesis testing / evidence prioritization",
      "bias_specific_mechanism": "After identifying two time-aligned possible causes, temperature rise and a new material lot, the participant selected the temperature hypothesis based on temporal correlation and an engineer's prior-experience comment. He logged the lot hypothesis as a secondary possibility but did not directly test or seek disconfirming evidence for it, describing the temperature story as sufficiently explanatory. This reflects selective prioritization of a favored hypothesis and premature closure rather than active disconfirmation.",
      "manifestation_in_interview": "The participant reported that the timing of the temperature rise 'lined up so cleanly' and that the engineer's comment reinforced the temperature explanation, while explicitly not prioritizing a lab test of the new lot because the temperature story 'felt like it explained things well enough.'",
      "effect_on_reasoning_or_decision": "The participant did not collect a hardness sample or otherwise directly test the new material lot at that point. He continued monitoring and documenting under the temperature assumption, leaving the alternative hypothesis unexamined until later evidence showed the lot was in-spec and tool wear was the actual cause.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.",
          "evidence_explanation": "This quote shows favoritism toward the temperature hypothesis and the explicit decision not to test the alternative, despite the alternative being known. The phrase 'felt like it explained things well enough' indicates premature closure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.",
          "evidence_explanation": "Confirms that the lot hypothesis was not directly checked and remained secondary while the participant focused on documentation supporting the temperature correlation."
        }
      ],
      "correction_or_counterevidence": "There were legitimate operational considerations: a lot hardness sample required lab time, and the temperature hypothesis was supported by temporal correlation and an engineer's prior experience with the same machine. The participant later acknowledged the sample 'wouldn't have cost much time' and could have closed off the alternative, which weakens the resource explanation. The eventual in-spec lab result does not retroactively impute bias but does show the untested alternative was non-causal.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages describe confirmation bias in evidence selection, prioritization, and hypothesis testing; they support the label but do not describe this specific industrial QA episode.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human Factors of the Confirmation Bias in Intelligence Analysis: Decision Support from Graphical Evidence",
          "authors": "Cook & Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at as-sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias can operate by selecting and prioritizing evidence in a way that supports an existing investigative hypothesis.",
          "relevance_to_this_occurrence": "The participant prioritized evidence and documentation supporting the temperature hypothesis and did not directly test the lot alternative, consistent with confirmatory evidence prioritization."
        },
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": "Parasuraman & Manzey",
          "publication_year": "2010",
          "retrieved_passage_or_finding": "discounting of contradictory information. In  addition, an explanation in terms of confirmation bias in processing the sampled information  or difficulties of comprehension is also unlikely,  given that the participants were very well  trained and that the system parameter always  contradicted the aid’s diagnosis in an unequivocal way.",
          "mechanism_supported_by_source": "Confirmation bias can involve discounting contradictory information or processing information in a hypothesis-consistent manner.",
          "relevance_to_this_occurrence": "The participant did not actively sample or test the contradictory lot hypothesis, leaving it as a footnote while pursuing the favored temperature explanation."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial reference point or belief and to make insufficient adjustments away from that anchor when new evidence arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to tool wear sensor data",
      "decision_point_description": "Deciding whether to stop for a tool change or make a smaller offset adjustment after seeing 78% cumulative cutting distance.",
      "affected_reasoning_operation": "Belief updating and diagnostic inference from new evidence",
      "bias_specific_mechanism": "The participant anchored on the initial representation of the cutting tool as 'basically new' because it had been swapped two days earlier. When the sensor showed 78% of rated tool life and a classic tool wear signature, he acknowledged the new data but made only incremental mental adjustment, interpreting the reading as not yet sufficient to justify a full tool change and choosing a small offset adjustment instead.",
      "manifestation_in_interview": "The participant explicitly stated that his prior mental model of the tool as recently serviced was 'a hard thing to fully shake in the moment.' He then chose a small in-process offset adjustment rather than pulling the tool, despite the sensor reading and the classic wear signature.",
      "effect_on_reasoning_or_decision": "The initial belief about the tool's recent service led the participant to under-react to objective wear data, delaying the tool change until further drift and Cpk degradation made the evidence overwhelming.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine.",
          "evidence_explanation": "This establishes the objective data contradicting the initial belief and the participant's acknowledgment that the initial anchor, 'basically new,' shaped his expectation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.",
          "evidence_explanation": "This is direct testimony that the prior belief resisted updating in the face of new evidence, which is the core mechanism of anchoring or insufficient adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away.",
          "evidence_explanation": "The behavioral consequence shows an incremental adjustment rather than full updating to the new wear information, consistent with anchoring."
        }
      ],
      "correction_or_counterevidence": "The choice of an offset adjustment was also influenced by time pressure and proximity to shift changeover, which is a plausible non-bias operational consideration. However, the participant explicitly described the residual prior model as hard to shake, and the sensor evidence objectively contradicted that prior model, supporting a distinct cognitive distortion beyond resource constraints.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passage from Rastogi et al. supports the anchoring-and-adjustment mechanism in a time-pressured decision context.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Insufficient adjustment away from an initial anchor is a resource-rational trade-off; under time pressure, adjustments are often insufficient.",
          "relevance_to_this_occurrence": "The participant exhibited insufficient adjustment away from the initial 'recently serviced tool' anchor under time pressure, choosing a smaller correction rather than a full tool change."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved passages contain extraction artifacts and are used only for terminology and mechanism validation, not as evidence of whether the biases occurred.",
    "Confidence ratings reflect transcript evidence only; low-confidence findings remain valid positive identifications under the task definition.",
    "Production pressure, time constraints, and shift-changeover considerations may partially overlap with or resemble cognitive bias mechanisms, making exact causal separation difficult.",
    "The analysis is limited to the participant's self-reported reasoning and decisions during the interview."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Biased_2_Gemini_on",
  "interview_id": "IP_Biased_2",
  "system_prompt_id": "Gemini",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
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
