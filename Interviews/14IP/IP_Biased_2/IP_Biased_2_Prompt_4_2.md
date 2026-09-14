You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay?

Participant: Sure, no problem. Happy to walk through it.

Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart?

Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping downward, and the most recent one landed in the warning zone — inside two sigma, not over the UCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average.

Interviewer: What was going through your mind at that point?

Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three downward-trending points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation.

Interviewer: Walk me through what happened next, chronologically.

Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the UCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real.

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
}}
- Hidden generation specification: {{"hidden_validation_specification": {
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
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "IP_Biased_2",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Manufacturing quality assurance and statistical process control for CNC turning",
    "role": "QA analyst monitoring Xbar-R control charts for outer-diameter measurements in an automotive-shaft turning cell",
    "objective": "Identify and contain an assignable cause of dimensional drift, select an appropriate intervention, and protect process capability and product conformance.",
    "incident_type": "Progressive downward mean shift in outer diameter, later associated with tool wear and resulting in output approaching or slightly breaching the lower specification limit.",
    "confidence": 0.99
  },
  "structure_audit": {
    "estimated_word_count": 1420,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "The participant responds to three downward-trending subgroup means and one warning-zone point by increasing sampling rather than stopping the turning cell.",
        "evidence_before": [
          "Three subgroup means were trending downward.",
          "The most recent mean was in a warning zone, inside two sigma.",
          "The range chart was stable.",
          "No maintenance activity or material change had been logged.",
          "The participant was 62% through the shift quota."
        ],
        "evidence_after": [
          "The next subgroup crossed a control limit.",
          "A manual micrometer reading matched the automated gauge.",
          "The participant treated the process shift as real rather than a gauge artifact."
        ],
        "goals_constraints": [
          "Avoid an unnecessary 45-minute changeover.",
          "Preserve production progress toward quota.",
          "Acquire more diagnostic information rapidly.",
          "Avoid continuing without any response to a concerning trend."
        ],
        "alternatives": [
          "Stop the line immediately.",
          "Log the warning and continue normal production.",
          "Increase sampling while continuing production."
        ],
        "decision_basis": "The participant judged the available signal as concerning but not yet sufficient to justify a full stop, and selected intensified sampling as a proportionate information-gathering response.",
        "time_pressure": "Moderate, due to quota pressure and the stated cost of a stop and changeover.",
        "uncertainty": "Whether the downward chart movement represented common-cause fluctuation, a measurement artifact, or a developing assignable cause."
      },
      {
        "id": 2,
        "summary": "After confirming an out-of-control condition, the participant gives temperature a preferred causal role and leaves a comparably time-aligned material-lot explanation untested.",
        "evidence_before": [
          "Shop-floor temperature increased by approximately three degrees during the two-hour drift period.",
          "A new material lot was loaded approximately 90 minutes before the drift began.",
          "The lot traveler had an approximately one-hour reporting lag.",
          "The process engineer reported that temperature swings had caused drift on this machine before.",
          "Tool-wear sensor data had not yet been checked."
        ],
        "evidence_after": [
          "The participant documented the temperature correlation.",
          "The participant logged the lot as a secondary possibility.",
          "The participant continued monitoring under the temperature assumption.",
          "The lot hardness result later returned within specification."
        ],
        "goals_constraints": [
          "Develop a usable root-cause hypothesis during an active process event.",
          "Avoid delay associated with sending a hardness sample to the lab.",
          "Continue monitoring and documenting the process condition."
        ],
        "alternatives": [
          "Treat temperature as the leading explanation.",
          "Obtain an immediate hardness sample from the new lot.",
          "Treat temperature and lot effects as unresolved competing hypotheses.",
          "Wait for tool-wear data before privileging either explanation."
        ],
        "decision_basis": "The participant privileges close temporal alignment between temperature rise and dimensional drift, reinforced by the engineer's prior experience, and declines to obtain direct evidence about the material-lot alternative.",
        "time_pressure": "Moderate. Lab testing would require a wait, although the participant later states that drawing the sample itself would not have taken much time.",
        "uncertainty": "Temperature and material lot both had plausible temporal relationships to the drift, and no direct discriminating test was performed at that point."
      },
      {
        "id": 3,
        "summary": "After receiving tool-wear data showing 78% of rated life and a directionally consistent wear signature, the participant uses an offset adjustment rather than immediately changing the tool.",
        "evidence_before": [
          "The tool-wear sensor indicated cumulative cutting distance at 78% of rated tool life.",
          "The participant believed the insert was effectively new because it had been replaced two days earlier.",
          "The participant states that the observed undersize trend is a classic signature of tool wear on the machine.",
          "Approximately 90 minutes remained before shift changeover."
        ],
        "evidence_after": [
          "The participant made a small in-process offset adjustment.",
          "The next sample continued toward the lower specification limit.",
          "The offset did not hold.",
          "The incoming operator later reported an unusual tool sound, a cue unavailable before the handoff."
        ],
        "goals_constraints": [
          "Avoid a full intervention close to shift changeover.",
          "Continue production while monitoring tightly.",
          "Address the drift without committing immediately to tool-change downtime."
        ],
        "alternatives": [
          "Immediately halt and change the tool.",
          "Continue operation without an adjustment.",
          "Apply an offset and observe subsequent subgroups."
        ],
        "decision_basis": "The participant acknowledges the sensor evidence but retains substantial weight on the prior expectation that a recently serviced tool should not yet be heavily worn, leading to a smaller corrective action.",
        "time_pressure": "High, because the decision occurred approximately 90 minutes before shift changeover.",
        "uncertainty": "Whether 78% rated-life consumption represented a sufficiently urgent wear state to justify an immediate tool change rather than a temporary offset."
      },
      {
        "id": 4,
        "summary": "After continued deterioration, 91% rated tool wear, lower-limit risk, and a Cpk decline, the participant recommends an immediate tool change and containment actions.",
        "evidence_before": [
          "The offset failed to stabilize the process.",
          "Several parts were near or slightly below the lower specification limit.",
          "Tool wear rose to 91% of rated life.",
          "Cpk declined from 1.42 to 1.05 over the preceding two hours.",
          "A deviation report was required for the affected parts."
        ],
        "evidence_after": [
          "The tool was changed.",
          "Dimensions returned to the historical baseline on the next shift.",
          "The new material lot's hardness result was within specification."
        ],
        "goals_constraints": [
          "Prevent further nonconforming output.",
          "Restore capability and dimensional stability.",
          "Meet required deviation-reporting obligations.",
          "Contain affected production."
        ],
        "alternatives": [
          "Change the tool immediately and document the affected parts.",
          "Continue using offsets and increased monitoring.",
          "Defer the intervention to the next shift."
        ],
        "decision_basis": "The combination of persistent downward drift, increasing wear, declining Cpk, and parts near or beyond tolerance crossed the participant's threshold for immediate corrective action.",
        "time_pressure": "Still present, but outweighed by the now-clear quality and conformance risk.",
        "uncertainty": "Low concerning the need to change the tool and contain output; moderate concerning whether tool wear was the only causal contributor."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "corrbias_01",
      "bias": "Correlation bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "“The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking.” ... “the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.”",
      "evidence_location": "Decision point 2, in the participant's account of prioritizing temperature over a new material lot and declining to obtain a lot-hardness test.",
      "mechanism": "The participant infers that temperature is the leading cause from temporal co-occurrence between rising temperature and dimensional drift, then assigns the competing material-lot hypothesis lower investigative priority despite its similarly plausible temporal relationship. The engineer's prior observation reinforces the preferred account but does not establish causality for this event.",
      "strength": "moderate",
      "confidence": 0.92,
      "plausible_nonbias_explanation": "Temperature was a plausible provisional hypothesis because the engineer had observed prior machine-specific temperature effects and a lab test would introduce delay. However, the participant states that the temporal temperature account felt sufficiently explanatory to justify not testing the competing lot hypothesis, which establishes unequal evidentiary treatment rather than mere sequencing of work.",
      "additional_evidence_needed": "No additional evidence is needed to support the occurrence. A controlled temperature intervention or direct mechanical assessment would be needed only to establish whether temperature actually caused the drift.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, participant response beginning “The timing just lined up so cleanly.”",
        "current_defect": "No defect material to the requested correlation-bias occurrence.",
        "minimal_change_instruction": "Retain the temporal-coincidence reasoning, the available material-lot alternative, and the participant's statement that the temperature explanation led them not to prioritize the lot test.",
        "preserve": [
          "The approximately three-degree temperature increase.",
          "The new lot's temporal proximity to the drift.",
          "The engineer's prior machine-specific experience.",
          "The participant's decision not to test lot hardness immediately.",
          "The later within-specification hardness result."
        ],
        "avoid_creating": [
          "Do not add a second independent temperature-versus-material causal-attribution decision later in the interview.",
          "Do not state that correlation proves causation or explicitly name the bias.",
          "Do not make the temperature explanation obviously implausible; it should remain a reasonable but insufficiently tested working hypothesis."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "consbias_01",
      "bias": "Conservatism Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "“My mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment.” ... “I made a small in-process offset adjustment ... rather than pulling the tool right away.”",
      "evidence_location": "Decision point 3, after the tool-wear sensor reports 78% rated life and the participant identifies the downward/undersize movement as a classic tool-wear signature.",
      "mechanism": "The participant explicitly retains an earlier belief that a two-day-old tool should not be a major factor despite new, quantitative wear evidence and a directionally diagnostic process cue. This incomplete belief revision contributes to choosing a limited offset response rather than the stronger tool-change response.",
      "strength": "moderate",
      "confidence": 0.85,
      "plausible_nonbias_explanation": "The offset decision has a legitimate operational component: 78% rated life does not necessarily mean imminent failure, tool changes impose production costs, and shift changeover was imminent. The occurrence is nevertheless supported because the participant expressly identifies the recently serviced-tool assumption as difficult to dislodge after receiving striking contradictory sensor evidence.",
      "additional_evidence_needed": "No additional evidence is required. If the generator wanted to make the operational threshold clearer without increasing explicitness, it could establish that 78% exceeds the cell's usual intervention threshold; however, this is optional and should not be added merely to strengthen an already supported occurrence.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, participant response beginning “It definitely registered as a data point I couldn't dismiss.”",
        "current_defect": "No defect material to the requested conservatism-bias occurrence.",
        "minimal_change_instruction": "Retain the prior belief about the recently replaced tool, the 78% sensor reading, the classic undersize wear signature, the participant's difficulty updating, and the choice of offset over immediate replacement.",
        "preserve": [
          "The two-day-old-tool prior.",
          "The 78% rated-life sensor evidence.",
          "The 90-minute pre-changeover constraint.",
          "The offset-and-monitoring response.",
          "The later fully revised tool-change decision at decision point 4."
        ],
        "avoid_creating": [
          "Do not add a separate pre-sensor dismissal of tool wear.",
          "Do not depict the later tool-change decision as a second conservatism-bias occurrence.",
          "Do not remove all operational justification, because the intended presentation is subtle rather than cartoonishly irrational."
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Correlation bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Conservatism Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Confirmation bias",
      "decision_point": 2,
      "supporting_quote": "“And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine.”",
      "mechanism": "After favoring the temperature explanation, the participant treats a confirming anecdotal account as reinforcing evidence while not obtaining comparably diagnostic evidence for the competing material-lot account.",
      "confidence": 0.62,
      "status": "candidate",
      "plausible_nonbias_explanation": "The engineer's input may be valid local expertise, and the selective evidence treatment is already adequately captured by the correlation-bias occurrence. The interview does not independently establish a separate search for confirmation or active avoidance of disconfirming evidence.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Anchoring bias",
      "decision_point": 3,
      "supporting_quote": "“I'd been thinking of that insert as basically new — we'd swapped it two days earlier.”",
      "mechanism": "The tool's recent replacement serves as an initial reference point that constrains the participant's interpretation of the later 78% wear reading.",
      "confidence": 0.72,
      "status": "candidate",
      "plausible_nonbias_explanation": "This is more parsimoniously treated as the prior-belief mechanism within the supported conservatism-bias instance, not as a separately countable accidental bias. It arises from the same evidence, decision, and response.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Omission bias",
      "decision_point": 3,
      "supporting_quote": "“Stopping for a full tool change felt like a big move to make off one sensor reading.”",
      "mechanism": "The statement could suggest a preference for avoiding a disruptive intervention over acting under uncertainty.",
      "confidence": 0.29,
      "status": "rejected",
      "plausible_nonbias_explanation": "The participant did act by applying an offset and increasing monitoring. The preference for the smaller action is sufficiently explained by time pressure, downtime costs, and incomplete evidence; the text does not establish that harm from action was weighted differently from harm from inaction.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "Increasing sampling instead of immediately stopping the line after one warning-zone point.",
      "location": "Decision point 1.",
      "why_not_bias": "The participant distinguishes between a nonconclusive warning-zone point and a concerning three-point trend, then obtains additional data. This is a proportionate SPC response and is not by itself normalcy bias, denial, or unjustified risk acceptance."
    },
    {
      "cue": "Quota status, 45-minute changeover cost, and upcoming shift changeover.",
      "location": "Decision points 1 and 3.",
      "why_not_bias": "These are real organizational and operational constraints. They can influence a threshold for intervention, but they do not independently demonstrate a cognitive bias."
    },
    {
      "cue": "Manual confirmation using a hand micrometer.",
      "location": "Decision point 1.",
      "why_not_bias": "Checking the automated gauge against an independent manual measurement is appropriate measurement-system verification and reflects sound diagnostic practice."
    },
    {
      "cue": "The incoming operator's report that the tool had sounded different.",
      "location": "After decision point 3, at shift handoff.",
      "why_not_bias": "The cue was unavailable to the participant at the relevant decision moment. It cannot be treated as evidence that the prior decision ignored known information."
    },
    {
      "cue": "The later decision to change the tool after wear rises to 91%, Cpk declines, and parts approach or exceed the lower limit.",
      "location": "Decision point 4.",
      "why_not_bias": "The participant updates appropriately in response to accumulated evidence. The earlier conservatism occurrence does not continue merely because the participant later takes the stronger action."
    },
    {
      "cue": "The material lot later tests within hardness specification.",
      "location": "Post-incident outcome.",
      "why_not_bias": "The later test result does not prove that the earlier causal reasoning was biased. The supported correlation-bias finding rests on unbalanced causal attribution and evidence selection at decision point 2, not on whether the neglected alternative ultimately proved correct."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "Temperature rise caused the downward dimensional drift.",
        "status": "not established",
        "basis_in_text": "Temporal co-occurrence between a three-degree rise in temperature and the two-hour drift period, plus a process engineer's prior experience.",
        "assessment": "This supports a plausible working hypothesis but does not isolate temperature as the cause. No temperature intervention, comparison period, or direct mechanism check is described."
      },
      {
        "claim": "The new material lot may have caused the drift.",
        "status": "plausible at decision point 2; later weakened",
        "basis_in_text": "The new lot was loaded approximately 90 minutes before drift started, but a timely direct test was not performed.",
        "assessment": "The later within-specification hardness result weakens one material-quality explanation but does not establish that every potential lot-related mechanism was impossible. It remains appropriate to treat the lot as a reasonable alternative at the time of the earlier decision."
      },
      {
        "claim": "Tool wear caused the undersize trend.",
        "status": "strongly supported observationally",
        "basis_in_text": "The sensor rises from 78% to 91% rated life, the participant identifies the drift as a classic undersize wear signature, the offset fails, and dimensions return to baseline after tool replacement.",
        "assessment": "The converging process, sensor, and post-intervention evidence provides a much stronger causal case for tool wear than the temperature account. It remains observational rather than fully controlled because the text does not explicitly state which concurrent conditions were held stable."
      }
    ],
    "correlation_causation_risks": [
      {
        "location": "Decision point 2",
        "risk": "The participant gives causal primacy to temperature based mainly on close timing and prior anecdotal experience while leaving the similarly time-aligned lot hypothesis untested.",
        "severity": "moderate"
      },
      {
        "location": "Post-tool-change outcome",
        "risk": "Return to baseline after tool replacement is strong causal evidence, but it would be stronger if the interview clarified that material, temperature, gauge condition, program settings, and other relevant conditions did not change concurrently.",
        "severity": "low"
      }
    ],
    "counterfactual_present": false,
    "changed_variable": null,
    "held_constant": [],
    "causal_coherence": "moderate",
    "explanation": "The corrected downward trend is consistent with the later undersize and lower-specification-limit narrative, materially improving coherence. However, the interview still states that the next subgroup “crossed the UCL outright” after a downward trend. For an Xbar chart expressed in the usual measurement direction, a downward mean shift should cross the lower control limit, not the upper control limit. This is a technical terminology inconsistency rather than a bias-occurrence failure. The interview includes retrospective hypotheticals about earlier sensor availability and an out-of-spec lot, but it does not implement a formal counterfactual design with one manipulated variable and explicitly held-constant conditions."
  },
  "quality_scores": {
    "occupational_realism": 89,
    "cta_fidelity": 92,
    "bias_separability": 86,
    "bias_subtlety": 89,
    "control_fidelity": 100,
    "counterfactual_fidelity": 100,
    "narrative_coherence": 84,
    "naturalness": 90,
    "hidden_label_integrity": 93,
    "overall_quality": 89
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 2,
    "requested_occurrence_total": 2,
    "missing_occurrence_total": 0,
    "accidental_occurrence_total": 0,
    "priority": "low",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Preserve exactly four decision points.",
      "Preserve the single supported correlation-bias occurrence at decision point 2.",
      "Preserve the single supported conservatism-bias occurrence at decision point 3.",
      "Do not turn quota pressure, downtime concerns, shift changeover, or uncertainty into additional biases.",
      "Do not add another independent temperature-versus-material causal-attribution episode.",
      "Do not add another independent delay or underreaction to tool-wear evidence."
    ],
    "revision_order": [
      {
        "affected_instance_id": "additional_candidate",
        "decision_point": 1,
        "approximate_turn_or_paragraph_location": "Participant response immediately after “Walk me through what happened next, chronologically.”",
        "current_status": "Technical narrative-coherence defect; target occurrences remain supported.",
        "evidence_currently_present": "The participant reports three subgroup means “creeping downward,” followed by “the next subgroup crossed the UCL outright.” Later responses consistently describe an undersize trend toward the lower specification limit.",
        "precise_defect": "For a conventional Xbar chart using the measured outer-diameter direction described elsewhere, a downward shift should breach the lower control limit rather than the upper control limit. The current wording conflicts with the later undersize/lower-limit account.",
        "recommended_revision_type": "local_evidence_addition",
        "minimal_change_instruction": "Replace “crossed the UCL outright” with “crossed the LCL outright.” If the intended chart uses a nonstandard reversed or transformed scale, instead add one brief clarification of that scale before retaining UCL; do not make both changes.",
        "what_must_remain_unchanged": [
          "The initial downward trend.",
          "The warning-zone signal and intensified-sampling decision.",
          "The manual gauge verification.",
          "The temperature-versus-material hypothesis episode.",
          "The later tool-wear evidence, offset decision, and final tool change."
        ],
        "warning_against_creating_additional_unintended_occurrences": "Do not add new causal claims, additional diagnostic evidence, or a second opportunity to dismiss the lot or tool-wear hypotheses. This repair should be limited to chart-direction terminology.",
        "expected_post_revision_status": "supported"
      }
    ]
  },
  "failure_flags": [
    {
      "flag": "control_limit_direction_inconsistency",
      "severity": "low",
      "description": "The revised interview correctly establishes a downward dimensional trend and later undersize/lower-limit risk, but it still says the next subgroup crossed the UCL. This should ordinarily be LCL unless the chart's direction is explicitly transformed or reversed."
    }
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
