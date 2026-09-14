You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about your decision-making during the last refueling outage, not a performance review. Everything you share is for process improvement. Can you tell me your role and roughly how long you've been doing outage coordination?

Participant: Sure, happy to walk through it. I'm the maintenance planner and outage coordinator for the unit — been doing this specific role about six years, plus four years as a planner before that. My main job during the outage is to sequence work orders against the critical path, allocate craft-hours, and make sure everything closes out before we hit the mode change hold points.

Interviewer: What made this particular outage stand out from a routine one?

Participant: Honestly, the sheer volume — we had around 140 concurrent work orders competing for a fixed 21-day window, and craft-hours were tighter than usual because two contractor crews got pulled to another site mid-cycle. So there was a lot of juggling. The item that ended up taking more of my attention than I expected was FW-IV-204, one of our feedwater isolation valves.

Interviewer: Take me through the sequence of events, from initial scoping to final return to service.

Participant: At the start of scoping, FW-IV-204 had a minor packing weep — nothing new, it had shown up in two prior outage condition reports, both closed as acceptable-as-found. No trend showing it was getting worse. But right around scoping, I'd just heard a pretty detailed account from a colleague about a similar valve at a sister unit that failed and caused a multi-day slip to their critical path. That story was fresh in my head when I built the priority list. I bumped FW-IV-204 up to top-tier priority for rework. Then, once we got into execution, craft-hours were running thin one afternoon and I had to lock in a crew configuration fast for the valve job — Outage Manager wanted it settled within the hour. I went with the first configuration that cleared the minimum schedule and safety requirements. Later in the outage, during post-maintenance testing, we saw a mild vibration anomaly on the pump bearing right next to FW-IV-204. My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service.

Interviewer: Let's slow down and reconstruct the timeline in more detail. When exactly did FW-IV-204 first come onto your radar for this outage?

Participant: Right at the outset of scoping, maybe day one or two of pre-outage planning. It was already on the work list from the prior cycle's CR, so it wasn't a surprise. What changed was how I ranked it relative to everything else.

Interviewer: And the vibration anomaly — when did that surface relative to the valve work?

Participant: That was maybe day fourteen, after the valve rework was already complete and we were running post-maintenance functional tests on the adjacent feedwater pump.

Interviewer: Let's go through each of those decision points one at a time. First — the priority ranking. What information did you actually have in front of you when you made that call?

Participant: I had the two prior CRs, both closed, no adverse trend on leak rate. I also had the backlog of other work orders, some with comparable or even higher CR severity ratings. Objectively, on paper, FW-IV-204 wasn't the most urgent thing on the list.

Interviewer: So what tipped it to top-tier?

Participant: The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me. I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up.

Interviewer: Did you go back and re-check the trend data before finalizing that ranking?

Participant: No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to.

Interviewer: Understood. Second decision point — the crew configuration under the tight craft-hour window. Walk me through that.

Participant: We were maybe two-thirds through the day's craft-hour budget, and I had several configurations that would technically work — different mixes of overtime, different sequencing with other jobs. The Outage Manager wanted a decision inside the hour to protect the critical path. I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in.

Interviewer: Did you consider comparing the other options more fully?

Participant: I thought about it, but comparing all the variables — overtime cost, fatigue limits, downstream sequencing — for three or four configurations would have eaten time I didn't have. So I went with what worked and moved to the next fire.

Interviewer: What happened as a result?

Participant: It created a minor sequencing conflict later with an unrelated pump job — nothing that blew the schedule, but craft had to shuffle around it. When we reviewed it afterward, there was a configuration that would have avoided that friction. Marginally better, not dramatically.

Interviewer: Third decision point — the vibration anomaly. What was your first working theory?

Participant: Residual misalignment from the valve rework. It made sense sequentially — we'd just had hands in that area, and a little post-maintenance vibration isn't unheard of.

Interviewer: What data did you pull to check that theory?

Participant: I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis.

Interviewer: Was there other data available that you didn't request at that point?

Participant: In hindsight, yes. There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched.

Interviewer: What about the full trend history for that bearing?

Participant: Also didn't pull that at the time. The system engineer reviewed it later, after the fact.

Interviewer: Last decision point — the final return-to-service call. What was your basis for concurring?

Participant: By that point, all the CRs on the valve and the adjacent pump were formally closed, the system engineer had given written concurrence, and I did the walkdown myself with operations. Given the sign-offs and what I observed directly during the walkdown, I concurred with return to service. I did weigh the earlier vibration discussion against that documentation, but everything on paper and everything I saw in the field lined up, so I didn't see a basis to hold it further.

Interviewer: Did you consider requesting extra monitoring time before mode change?

Participant: I did think about it briefly, given the anomaly earlier in the outage, but with the engineering concurrence and a clean walkdown, holding the unit longer without a specific technical reason didn't seem justified.

Interviewer: How much time pressure were you under across these decisions, generally?

Participant: Constant, honestly, but it spiked hardest around the crew assignment call — that was the one hour deadline. The priority ranking and the vibration call had a bit more breathing room, even if it didn't always feel that way in the moment.

Interviewer: If the lubrication log had been sitting on your desk when the vibration anomaly came up, do you think it would have changed your review?

Participant: Possibly. If it had shown something inconsistent with misalignment, I probably would have widened the investigation. It just wasn't something I went looking for at the time.

Interviewer: Looking back, is there a point where a different call on FW-IV-204's priority might have changed how things unfolded?

Participant: Maybe. If I'd ranked it purely on the documented trend, it might have sat lower in the queue, and I'd have had more craft-hours free for other jobs earlier. Hard to say if that changes anything meaningfully, since the valve work itself went fine.

Interviewer: Anything you'd tell a newer planner based on this outage?

Participant: Mainly to keep coming back to the actual trend data, even when a recent story or a tight clock makes a different path feel more urgent. It's not that those instincts are wrong, just that they're easy to lean on more than the numbers warrant.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Biased_3",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Maintenance Planner / Outage Coordinator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Feedwater Isolation Valve Rework During a Refueling Outage",
    "scenario_summary_internal": "A maintenance planner/outage coordinator at a PWR station is scoping and executing a 21-day refueling outage. A recurring packing-leak issue on a feedwater isolation valve (FW-IV-204) must be scheduled alongside dozens of competing work orders under a fixed critical-path window. During execution, an unexpected vibration reading on a related pump bearing surfaces, and the coordinator must decide how to interpret it before clearing the system for startup. The narrative surfaces one vivid recalled incident from another unit that skews risk weighting (availability bias), a scoping/resourcing shortcut driven by cognitive and time load (bounded rationality), and a selective evidence-review pattern once a working theory forms about the vibration anomaly (confirmation bias). A fourth decision point (final return-to-service call) is written as a clean, non-biased judgment call to anchor the narrative and give a neutral contrast point.",
    "occupational_realism": {
      "objective": "Safely complete all critical-path maintenance and inspection work within the 21-day refueling outage window and return the unit to full power without exceeding the approved critical path or introducing latent equipment issues.",
      "setting": "Pressurized water reactor station; outage control center during a scheduled refueling outage; feedwater system and auxiliary building work areas.",
      "constraints": [
        "Fixed 21-day critical-path outage schedule with penalty exposure for schedule overrun",
        "Limited contractor craft-hours during the outage window",
        "Competing work orders across multiple systems requiring the same specialty crews (valve/rigging techs)",
        "Radiological and access control limiting work windows in certain areas",
        "Regulatory requirement to resolve open condition reports before mode change",
        "Coordinator responsible for prioritizing ~140 concurrent work orders with partial information on each"
      ],
      "stakeholders": [
        "Maintenance Planner/Outage Coordinator (interviewee)",
        "Outage Manager",
        "System Engineer for feedwater system",
        "Valve maintenance craft supervisor",
        "Operations shift manager",
        "Quality/condition report reviewer"
      ],
      "technical_terms_to_use": [
        "feedwater isolation valve (FW-IV-204)",
        "packing leak",
        "critical path",
        "work order backlog",
        "condition report (CR)",
        "bearing vibration trend",
        "return-to-service walkdown",
        "craft-hours allocation",
        "system engineer concurrence",
        "mode change hold point"
      ],
      "technical_terms_to_avoid": [
        "availability heuristic",
        "confirmation bias",
        "bounded rationality",
        "satisficing",
        "anchoring",
        "cognitive bias",
        "heuristic shortcut"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "FW-IV-204 has a known minor packing weep documented in two prior outage CRs, both closed as acceptable-as-found",
          "No trending data indicates worsening leak rate",
          "The coordinator recently heard a detailed account of a similar valve failure at a sister unit that caused a multi-day schedule slip"
        ],
        "new_information_after_decision": [
          "Craft supervisor notes the valve is functioning within spec but the packing job will consume more hours than budgeted",
          "Other queued work orders with equal or higher CR priority are pushed later in the schedule"
        ],
        "alternatives": [
          "Rank FW-IV-204 rework as top priority based on the vividly recalled sister-unit event",
          "Rank work orders strictly by documented CR severity and trend data, treating FW-IV-204 as routine",
          "Request updated trend data before assigning priority"
        ],
        "intended_action": "Coordinator elevates FW-IV-204 to top-tier priority, citing the memorable sister-unit failure more than the actual local trend data."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Craft-hour budget is nearly exhausted for the current outage day",
          "Multiple valid crew-assignment configurations exist, several requiring further comparison of overtime cost, fatigue rules, and sequencing",
          "Outage Manager wants a resourcing decision within the hour to hold the critical path"
        ],
        "new_information_after_decision": [
          "The chosen crew configuration works but creates a minor sequencing conflict with an unrelated pump job later in the shift",
          "A more thorough comparison, done later, shows a marginally better configuration existed"
        ],
        "alternatives": [
          "Run a full comparison of all feasible crew configurations against cost, fatigue, and sequencing before deciding",
          "Select the first crew configuration that meets minimum schedule and safety requirements and move on",
          "Defer the assignment decision to the next shift for a fuller review"
        ],
        "intended_action": "Coordinator picks the first workable crew configuration that clears the immediate constraints, given limited time and information-processing capacity, rather than continuing to search for the optimal configuration."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vibration monitoring shows a mild anomaly on the feedwater pump bearing adjacent to FW-IV-204 during post-maintenance testing",
          "Coordinator's working theory is that the anomaly is residual misalignment from the valve rework just completed",
          "System engineer has not yet reviewed the full vibration trend history for that bearing"
        ],
        "new_information_after_decision": [
          "A second vibration reading is taken 12 hours later and is ambiguous ",
          "The system engineer later notes an unrelated lubrication log entry that was available at the time but not requested"
        ],
        "alternatives": [
          "Pull the full bearing vibration trend history and lubrication records before attributing the anomaly to the valve rework",
          "Accept the misalignment theory, request only the specific data points that would confirm it, and proceed",
          "Treat the anomaly as unexplained and hold the item open pending independent engineering review"
        ],
        "intended_action": "Coordinator requests and reviews the vibration data segment that fits the misalignment theory, does not request the lubrication log or wider trend history, and documents the anomaly as resolved based on the theory-consistent data."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "All outstanding CRs on FW-IV-204 and the adjacent pump are formally closed",
          "System engineer has provided written concurrence for return to service",
          "Operations shift manager requests final walkdown confirmation before mode change"
        ],
        "new_information_after_decision": [
          "The unit returns to service and completes the walkdown without further anomalies",
          "A minor unrelated instrumentation drift is noted for tracking in the next outage, unrelated to the FW-IV-204 work"
        ],
        "alternatives": [
          "Concur with return to service based on completed walkdown and engineering sign-off",
          "Request an additional 24-hour monitoring period before mode change",
          "Escalate for independent review given the earlier vibration anomaly"
        ],
        "intended_action": "Coordinator conducts the walkdown, weighs the documented sign-offs against the earlier anomaly discussion, and concurs with return to service as a reasoned judgment call, without additional bias-driven distortion."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role during this outage and what your main objective was?",
        "What made this particular outage cycle stand out from a routine one?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from initial work scoping to final return to service.",
        "At what point did FW-IV-204 first come onto your radar for this outage?",
        "What happened after the vibration anomaly was first noticed?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you when you decided to prioritize FW-IV-204?",
        "Were there other work orders competing for the same priority ranking? How did you weigh them?",
        "How did you settle on the crew configuration you used for the valve rework?",
        "Did you consider comparing other resourcing options, and what stopped or allowed further comparison?",
        "When the vibration anomaly appeared, what was your first working theory about the cause?",
        "What data did you pull to check that theory, and what data did you not pull?",
        "What was your basis for signing off that the unit was ready to return to service?"
      ],
      "prior_experience": [
        "Have you dealt with a similar valve or vibration issue before? How did that shape your thinking here?",
        "Was there a past event, at this plant or elsewhere, that came to mind during this outage?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure were you under when making the crew assignment decision?",
        "How confident were you in the misalignment theory at the time, on a scale of your own judgment?",
        "Was there anything you were uncertain about but decided not to pursue further?"
      ],
      "closing_hypotheticals": [
        "If you had had more time before the crew assignment decision, would you have done anything differently?",
        "If the lubrication log had been in front of you when the vibration anomaly appeared, do you think it would have changed your review?",
        "Looking back, is there a point where a different prioritization of FW-IV-204 might have changed the outcome?",
        "What would you tell a newer planner to watch for in a similar situation?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias",
        "decision_point": 1,
        "mechanism": "Ease of recall of a vivid, recently-heard sister-unit valve failure inflates perceived probability/severity of a similar local issue, overriding the less memorable but more diagnostic local CR trend data.",
        "affected_reasoning_operation": "Risk/priority ranking of competing work orders during outage scoping",
        "evidence_available_at_time": [
          "Two prior CRs on FW-IV-204 closed as acceptable-as-found",
          "No adverse trend in packing leak rate",
          "Recently recounted sister-unit valve failure story circulating among staff"
        ],
        "required_textual_manifestation": "Coordinator explicitly cites the memorable sister-unit incident as the deciding factor for elevating FW-IV-204's priority, over the flat local trend data, without independently re-checking the trend numbers.",
        "plausible_nonbias_interpretation": "A cautious planner reasonably erring toward conservatism given any valve packing history, regardless of recall vividness.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "availability bias",
          "heuristic",
          "recall vividness",
          "cognitive bias"
        ]
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 2,
        "mechanism": "Under time pressure and limited capacity to evaluate all crew-configuration permutations, coordinator selects the first option clearing minimum constraints rather than continuing search toward an optimal allocation, consistent with satisficing under bounded cognitive/time resources.",
        "affected_reasoning_operation": "Resource/crew allocation decision-making under constraint",
        "evidence_available_at_time": [
          "Nearly exhausted craft-hour budget",
          "Multiple feasible crew configurations requiring comparison of cost, fatigue, sequencing",
          "One-hour deadline imposed by Outage Manager"
        ],
        "required_textual_manifestation": "Coordinator states they picked the first configuration that met minimum requirements 'to keep things moving' rather than comparing the remaining options, and only learns later a marginally better one existed.",
        "plausible_nonbias_interpretation": "A legitimate, expertise-based triage decision appropriate for real-time operational constraints where full optimization is infeasible.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "bounded rationality",
          "satisficing",
          "cognitive load",
          "heuristic shortcut"
        ]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3,
        "mechanism": "Coordinator forms an early working theory (misalignment from valve rework) and selectively requests/reviews only the vibration data segment consistent with that theory, while not requesting the lubrication log or full trend history that could disconfirm or complicate it.",
        "affected_reasoning_operation": "Evidence selection and interpretation during anomaly investigation",
        "evidence_available_at_time": [
          "Mild vibration anomaly on adjacent pump bearing after valve rework",
          "Unrequested lubrication log entry existing in the record system",
          "Full bearing vibration trend history not yet pulled"
        ],
        "required_textual_manifestation": "Coordinator describes requesting only the specific vibration readings that fit the misalignment explanation, closing the item on that basis, and later acknowledging the lubrication log was available but not sought at the time.",
        "plausible_nonbias_interpretation": "A time-efficient, experience-based diagnostic shortcut focusing on the most likely proximate cause given the just-completed valve work.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "confirmation bias",
          "selective evidence",
          "disconfirming evidence",
          "cognitive bias"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control generated in this specification."
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
      "Confirm exactly 4 decision points are present in the timeline",
      "Confirm exactly 1 Availability Bias instance is embedded, located only at decision point 1",
      "Confirm exactly 1 Bounded Rationality instance is embedded, located only at decision point 2",
      "Confirm exactly 1 Confirmation Bias instance is embedded, located only at decision point 3",
      "Confirm decision point 4 contains no intentionally embedded named-bias instance",
      "Confirm no bias name, definition, or psychological label appears in interview text",
      "Confirm each instance has a plausible non-bias explanation present in probe answers",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points and probe plan density",
      "Confirm consequences at each decision point do not mechanically prove bias presence or absence"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overweighting a vivid recalled sister-unit incident over flat local trend data during priority ranking."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as satisficing crew-configuration selection under time/cognitive constraint rather than exhaustive comparison."
      },
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as selective evidence request/review consistent with an existing working theory, omitting available disconfirming sources."
      }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Bounded Rationality",
      "Confirmation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Availability Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Bounded Rationality",
        "requested_occurrences": 1
      },
      {
        "bias": "Confirmation Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias",
        "decision_point": 1
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 2
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias",
        "mechanism": "Recall vividness of a memorable sister-unit valve failure inflates perceived risk of local, statistically unremarkable valve issue, overriding documented trend data during priority ranking.",
        "affected_reasoning_operation": "Risk/priority ranking of competing outage work orders",
        "evidence_source": "Verbal/recalled sister-unit incident vs. documented local CR trend data",
        "distinctiveness_requirement": "Only occurrence of Availability Bias in the interview; must not be repeated at other decision points or in hypotheticals."
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Time- and capacity-constrained selection of the first satisfactory crew configuration instead of continued search for an optimal one.",
        "affected_reasoning_operation": "Resource/crew allocation under schedule constraint",
        "evidence_source": "Craft-hour budget status and multiple feasible but uncompared crew configurations",
        "distinctiveness_requirement": "Only occurrence of Bounded Rationality in the interview; distinct decision point and reasoning operation from the other two instances."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective solicitation and interpretation of vibration data consistent with a pre-formed misalignment theory, while not requesting available disconfirming lubrication/trend records.",
        "affected_reasoning_operation": "Evidence selection and interpretation during anomaly investigation",
        "evidence_source": "Post-maintenance vibration readings vs. unrequested lubrication log and full trend history",
        "distinctiveness_requirement": "Only occurrence of Confirmation Bias in the interview; occurs at decision point 3 only, not reintroduced at decision point 4's return-to-service judgment."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias",
        "strength": "subtle"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
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
    "scenario_id": "NP_Biased_3",
    "domain_id": "NP",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1, 2, 3) selected for best mechanism fit and narrative realism; decision point 4 reserved as a neutral, non-biased judgment call to provide contrast and prevent unintended bias clustering.",
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
          "segment_type": "priority-ranking rationale",
          "raw_interview_anchor": "The sister-unit story, honestly... So I moved it up.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "avail_01"
          ],
          "ground_truth_rationale": "The participant elevates FW-IV-204 because a vivid sister-unit failure outweighed flat local CR and trend evidence."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "crew-configuration choice rationale",
          "raw_interview_anchor": "I looked at the first configuration that met minimum schedule and safety requirements... and locked it in.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "br_01"
          ],
          "ground_truth_rationale": "Under a one-hour deadline and limited processing capacity, the participant selects the first satisfactory crew configuration instead of comparing feasible alternatives."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "diagnostic evidence-selection rationale",
          "raw_interview_anchor": "They looked consistent with that, so I documented the anomaly as resolved... I didn't feel a need to widen the search.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "The participant requests theory-consistent vibration data and omits available lubrication and full-trend records that could disconfirm misalignment."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "return-to-service judgment rationale",
          "raw_interview_anchor": "Given the sign-offs and what I observed directly during the walkdown, I concurred with return to service.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Formal engineering concurrence, closed CRs, and a direct walkdown provide a documented non-biased basis for concurrence."
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
    "analysis_scope_note": "Conservative mechanism-first analysis of the CTA transcript for affirmative evidence of cognitive-bias mechanisms. No retrieved corpus passages were supplied, so identified labels rest on general knowledge of established cognitive-science taxonomy."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias", "Salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments of likelihood, frequency, or importance are influenced by how easily relevant instances come to mind, often overweighting recent, vivid, or emotionally salient examples.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Priority ranking of FW-IV-204 during pre-outage scoping",
      "decision_point_description": "Ranking FW-IV-204 as a top-tier rework priority among approximately 140 concurrent work orders at the start of the outage.",
      "affected_reasoning_operation": "Risk and urgency prioritization under uncertainty",
      "bias_specific_mechanism": "A recent, detailed, emotionally vivid anecdote about a similar sister-unit valve failure was highly available in memory and inflated the perceived probability and consequence of a similar failure at this unit, outweighing the documented no-trend condition-report history.",
      "manifestation_in_interview": "The participant explicitly stated that FW-IV-204 was not the most urgent item on paper, yet the fresh sister-unit story led him to move it to top-tier priority without re-checking updated trend data.",
      "effect_on_reasoning_or_decision": "FW-IV-204 received top-tier priority and maintenance attention, potentially displacing other work orders with comparable or higher documented severity and misallocating early-outage craft-hours.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But right around scoping, I'd just heard a pretty detailed account from a colleague about a similar valve at a sister unit that failed and caused a multi-day slip to their critical path. That story was fresh in my head when I built the priority list. I bumped FW-IV-204 up to top-tier priority for rework.",
          "evidence_explanation": "Directly links the recent, vivid sister-unit story to the priority decision, showing availability of the anecdote rather than documented trend as the driver."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Objectively, on paper, FW-IV-204 wasn't the most urgent thing on the list.",
          "evidence_explanation": "Confirms that the documented evidence did not justify the top-tier ranking, strengthening the inference that an availability-driven judgment displaced the base-rate evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me.",
          "evidence_explanation": "Illustrates the vividness and memorability of the anecdote, which are central to the availability-heuristic mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to.",
          "evidence_explanation": "Shows that the participant did not seek disconfirming trend data once the salient anecdote had heightened concern, allowing the availability-driven judgment to stand."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction during the prioritization. Retrospectively, the participant acknowledged that ranking purely on documented trend might have placed the valve lower, but noted it was hard to say whether that would have changed the outcome meaningfully.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the availability-heuristic label and mechanism rely on general knowledge of established cognitive-science taxonomy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Confirmatory search", "Selective information search"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's existing belief or hypothesis, while avoiding or underweighting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation and closure of mild vibration anomaly on pump bearing near FW-IV-204",
      "decision_point_description": "Determining the cause of a post-maintenance vibration anomaly and deciding to close it out after reviewing vibration data consistent with residual misalignment.",
      "affected_reasoning_operation": "Causal diagnosis and anomaly resolution",
      "bias_specific_mechanism": "The participant formed an initial causal hypothesis, residual misalignment from rework, then selectively requested and accepted vibration data that matched that hypothesis while not seeking available disconfirming information such as the bearing lubrication log or full trend history.",
      "manifestation_in_interview": "The participant pulled immediate vibration readings selected for consistency with misalignment and documented the anomaly as resolved, explicitly stating that the lubrication log and full trend history were not pulled because the misalignment explanation already fit.",
      "effect_on_reasoning_or_decision": "The anomaly was closed on a narrow, hypothesis-consistent data subset, leaving an alternative lubrication-related cause unevaluated at the time. The full bearing trend history was reviewed only later by the system engineer.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service.",
          "evidence_explanation": "Shows an initial causal theory guiding data selection and closure, indicating a confirmatory reasoning path."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis.",
          "evidence_explanation": "Demonstrates that the participant sought specifically theory-consistent data and accepted it as sufficient for closure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, yes. There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched.",
          "evidence_explanation": "Explicitly describes failure to seek available alternative or disconfirming information because the existing hypothesis appeared sufficient."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Also didn't pull that at the time. The system engineer reviewed it later, after the fact.",
          "evidence_explanation": "Further confirms that additional relevant trend data was available but not consulted before closing the anomaly."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that if the lubrication log had shown something inconsistent with misalignment, he probably would have widened the investigation; however, this was retrospective and did not occur before the anomaly was closed. The system engineer later reviewed the full trend history after the fact.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task; the confirmation-bias label and mechanism rely on general knowledge of established cognitive-science taxonomy.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied, so all corpus-support fields are empty and labels rely on general knowledge.",
    "The transcript is a single-participant retrospective account, so some reported reasoning may be filtered by memory and self-presentation.",
    "Several decisions occurred within the same outage timeline, so findings are separated only where a distinct bias-specific mechanism was affirmatively evidenced."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Biased_3_Sonnet_off",
  "interview_id": "NP_Biased_3",
  "system_prompt_id": "Sonnet",
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
