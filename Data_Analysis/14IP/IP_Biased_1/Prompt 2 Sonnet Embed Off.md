You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific incident from your work as a production planner, and I'll be asking you to walk me through what happened and why you made the calls you did. Nothing you say here affects your performance record. Sound good?

Participant: Yeah, that's fine. Happy to walk through it. It was a memorable afternoon.

Interviewer: Can you tell me a bit about your role, then give me the overview of the incident?

Participant: I'm the production planner for three parallel lines at our plant — discrete assembly, mid-volume SKUs, frequent changeovers. I sequence what runs where, manage changeover windows, and hit ship cutoffs without blowing labor budgets. This was a Friday. A subcomponent we needed for two customer orders — Order A and Order B — came in four hours late from the supplier. Both had the same end-of-shift ship cutoff, so as soon as I heard about the delay I knew I had a compressed window to get everything sequenced and out the door.

Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened after you learned about the late delivery?

Participant: Once I confirmed the component landed, I pulled up the MES to see where Line 1 and Line 2 stood — both mid-run on other SKUs, so I needed changeovers on both to get to the rush SKUs. Problem was, I only had one certified changeover tech on shift. That was my first call — which line gets the tech first. Around the same time, an operator flagged that Line 3 had thrown an intermittent alarm twice in the past hour. That line wasn't part of the original plan, but it had open capacity, so it became relevant as a potential overflow resource. Then there was a batch sitting in the Line 2 output buffer that QA hadn't released yet, which mattered because Order B needed some of those units. Finally, toward the end, a labeling issue on part of that batch ate into our remaining time right as the ship cutoff closed in. So four points where I had to make a call under pressure.

Interviewer: Let's reconstruct the timeline before we dig into each decision.

Participant: Component lands around 1pm, four hours later than the morning window. I make the technician call almost immediately, maybe 1:15. The Line 3 alarm conversation happens about 20 minutes after, while the first changeover is underway. The QA buffer question comes up around 2:30, once I'm mapping how many units Order B still needs. QA doesn't call back until 3:10, which is when the labeling discrepancy surfaces. From there it's a sprint — cutoff is 5pm, so the last call, about overtime and the carrier, happens around 3:30.

Interviewer: Let's start with the technician assignment. What information did you have?

Participant: I knew Order A was the bigger order by unit count, and Line 2 had a tighter downstream packaging slot later on. Technically Line 2's changeover being late would ripple further because packaging was booked tight. In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs. I didn't split the tech's time across both lines in shorter blocks, which was an option, because that would have delayed both changeovers instead of finishing one cleanly.

Interviewer: Any hesitation about the packaging slot issue?

Participant: A little. But finishing one line's changeover completely felt more reliable than half-finishing two, and Order A's volume backed that up.

Interviewer: Let's move to the Line 3 alarm. Walk me through that call.

Participant: The operator told me the alarm had come up before and "usually clears itself" — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience. Given that, and given I had two other things actively unfolding — the changeover and the ship cutoff clock — I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue.

Interviewer: Did you look into whether anything else depended on Line 3's output during that window?

Participant: Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3. It turned out a smaller order, Order C, also needed Line 3 output that same shift, but I didn't find that out until later. I wasn't ignoring it on purpose, it just wasn't on my radar with everything else going on.

Interviewer: When you found out about Order C afterward, what was your reaction?

Participant: A bit of an "oh, right" moment. Not catastrophic — we fit it in later — but it made me realize I'd made that overflow call pretty quickly without stepping back to check what else was in play on that line.

Interviewer: Let's talk about the QA buffer decision. What was going through your mind?

Participant: Order B needed units from that batch plus new production to hit full quantity. QA hadn't confirmed release yet, and their lead was off-site with spotty response time. I decided to provisionally build the buffer units into the Order B plan rather than wait, because waiting with no ETA on a callback risked losing time I couldn't get back. I told the team we'd adjust if QA flagged something.

Interviewer: What made provisional inclusion feel right versus excluding those units?

Participant: Excluding them would have guaranteed a lower fill rate regardless of what QA said, and historically that batch type passes more often than not. It felt like a reasonable bet given the clock, not a guarantee.

Interviewer: And QA did call back?

Participant: About forty minutes later. They confirmed the batch passed, but flagged a labeling discrepancy on a subset of units, meaning rework.

Interviewer: That leads to the final decision — rework and shipment. What were you weighing?

Participant: The rework was going to eat twenty minutes of Line 2 time, and cutoff was ninety minutes out. Order A was tracking fine. Order B was now at risk. Overtime authorization had just come through, but it adds cost. I could also have accepted a partial shipment and expedited the rest next shift, or called the account manager to renegotiate the cutoff.

Interviewer: Why overtime and carrier coordination instead of the other two?

Participant: Partial shipment felt like a worse customer experience than a slightly late full shipment, and renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally. Overtime plus talking to the carrier directly gave me a shot at getting the full order out with minimal disruption, even shipping a few minutes past official cutoff.

Interviewer: How did that play out?

Participant: Order B shipped about twelve minutes past cutoff after the carrier agreed to hold pickup briefly. Order A shipped on time. Not a clean day, but nothing was lost.

Interviewer: Looking back, if you'd known upfront that Order C depended on Line 3, would you have handled that decision differently?

Participant: Probably. I likely would have taken two minutes to check the schedule before committing Line 3 as overflow, rather than just going with the operator's read on the alarm. It wouldn't have changed the outcome much, but I'd have made the call with a clearer picture.

Interviewer: And if you'd had fifteen more minutes before the technician assignment, would anything have changed?

Participant: Maybe I'd have looked harder at splitting the tech's time, but I think I still land on Order A first given the volume difference.

Interviewer: Is there a point in this sequence where, in hindsight, you wish you'd gathered more information before deciding?

Participant: The Line 3 call, for sure. Everything else I feel like I had a reasonable handle on given what was knowable at the time. That one I moved through fast because I was juggling two other things, and it's the one place where a little more digging would have given me a fuller picture before I committed the line.

Interviewer: That's really helpful, thank you. I think that covers everything I need.

Participant: No problem, glad it was useful.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "IP_Biased_1",
    "domain_id": "IP",
    "domain": "Industrial Production Processes",
    "role": "Production Planner / Scheduler",
    "condition": "biased",
    "generation_specification": {
      "scenario_title_internal": "The Friday Rush Reallocation",
      "scenario_summary_internal": "A production planner at a mid-size discrete-manufacturing plant must re-sequence three parallel production lines after a supplier delivers a critical subcomponent four hours late, threatening two customer ship dates on the same day. The planner must decide how to reallocate machine time, changeovers, and overtime labor across the remaining shift window while juggling incomplete visibility into downstream quality-hold status and a second, unrelated machine alarm. The incident unfolds over one afternoon shift and culminates in a shipment decision made under compressed time.",
      "occupational_realism": {
        "objective": "Re-sequence production across three lines to meet two conflicting customer ship windows after a late component delivery, without violating changeover, labor, or quality-hold constraints.",
        "setting": "Discrete-parts manufacturing plant, afternoon shift, ERP/MES scheduling system with partial real-time visibility, planner working from a control-room terminal with radio contact to line supervisors.",
        "constraints": [
          "Component delivery arrived 4 hours behind schedule",
          "Two customer orders (Order A, Order B) share a common ship cutoff at end of shift",
          "Line 3 has a pending unrelated intermittent alarm of unknown root cause",
          "Changeover from current SKU to rush SKU costs 45 minutes per line",
          "Only one certified changeover technician available for two lines needing changeover simultaneously",
          "Overtime authorization requires supervisor sign-off with a 30-minute approval lag",
          "Quality hold status on a prior batch is not yet confirmed by QA at decision time"
        ],
        "stakeholders": [
          "Production Planner (interviewee)",
          "Shift Supervisor",
          "Line 3 Machine Operator",
          "Changeover Technician",
          "Quality Assurance Lead",
          "Customer Account Manager (Order A)",
          "Customer Account Manager (Order B)"
        ],
        "technical_terms_to_use": [
          "changeover window",
          "line sequencing",
          "ship cutoff",
          "quality hold",
          "takt time",
          "overtime authorization",
          "bottleneck resource",
          "WIP buffer"
        ],
        "technical_terms_to_avoid": [
          "bounded rationality",
          "satisficing",
          "cognitive load",
          "heuristic",
          "decision bias",
          "suboptimal search"
        ]
      },
      "timeline": [
        {
          "phase": 1,
          "decision_point": true,
          "facts_available_before_decision": [
            "Component delivery is 4 hours late",
            "Order A and Order B both have end-of-shift ship cutoffs",
            "Line 1 and Line 2 are currently mid-run on unrelated SKUs",
            "Only one changeover technician is on shift"
          ],
          "new_information_after_decision": [
            "Line 1 changeover technician assignment leaves Line 2 changeover delayed by 45 minutes",
            "Order B account manager calls asking for status"
          ],
          "alternatives": [
            "Assign technician to Line 1 first (higher unit count order)",
            "Assign technician to Line 2 first (tighter downstream packaging slot)",
            "Split technician time across both lines in shorter intervals"
          ],
          "intended_action": "Planner assigns the sole changeover technician to Line 1 first based on order size."
        },
        {
          "phase": 2,
          "decision_point": true,
          "facts_available_before_decision": [
            "Line 3 alarm has occurred twice in the past hour with no confirmed cause",
            "Line 3 is the only line with open capacity to absorb overflow from Line 1 or Line 2 if either falls behind",
            "Operator reports the alarm 'usually clears itself'",
            "Time remaining in shift is under 5 hours"
          ],
          "new_information_after_decision": [
            "Line 3 continues running without further stoppage for the next hour",
            "A third, smaller order (Order C) is later found to depend on Line 3 output, which was not checked before the decision"
          ],
          "alternatives": [
            "Pause Line 3 briefly to have maintenance investigate the alarm before committing it as overflow capacity",
            "Continue running Line 3 as-is and treat it as available overflow capacity for Order A or B",
            "Request a quick root-cause check from the on-call technician while continuing production"
          ],
          "intended_action": "Planner accepts the operator's informal assessment, commits Line 3 as overflow capacity for whichever line falls behind, and moves on to the next fire without checking whether any other order or downstream constraint depends on Line 3 output within the shift."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "QA has not yet confirmed release status on the prior batch sitting in the Line 2 output buffer",
            "Order B requires units from that buffer plus new production to meet full quantity",
            "QA lead is off-site and reachable only by phone with intermittent response time"
          ],
          "new_information_after_decision": [
            "QA calls back 40 minutes later confirming the batch passed, but flags a labeling discrepancy that requires rework on a subset of units"
          ],
          "alternatives": [
            "Wait for QA confirmation before committing buffer units to the Order B shipment plan",
            "Provisionally include buffer units in the shipment plan and adjust if QA flags an issue",
            "Exclude buffer units entirely and rely only on new production, accepting a lower initial fill rate"
          ],
          "intended_action": "Planner provisionally includes the buffer units in the Order B plan pending QA confirmation."
        },
        {
          "phase": 4,
          "decision_point": true,
          "facts_available_before_decision": [
            "Rework from the labeling discrepancy will consume 20 minutes of Line 2 time",
            "Ship cutoff for both orders is now 90 minutes away",
            "Overtime authorization has come through but adds cost",
            "Order A is tracking to complete on time; Order B is at risk"
          ],
          "new_information_after_decision": [
            "Order B ships 12 minutes past the cutoff after carrier coordination; Order A ships on time"
          ],
          "alternatives": [
            "Pull additional labor onto Order B rework via overtime to protect the cutoff",
            "Accept a partial shipment for Order B and expedite the remainder next shift",
            "Renegotiate the cutoff time directly with the Order B account manager"
          ],
          "intended_action": "Planner authorizes overtime labor for rework and coordinates directly with the carrier to extend the pickup window."
        }
      ],
      "probe_plan": {
        "opening": [
          "Walk me through what a normal shift looks like before this incident started.",
          "What was your primary objective when you learned about the late delivery?"
        ],
        "timeline_reconstruction": [
          "What did you know at the moment the component arrived late?",
          "What happened right after you made the technician assignment call?",
          "When did the Line 3 alarm first come to your attention relative to other events?",
          "Walk me through what you knew about the QA hold status at each point in the afternoon."
        ],
        "decision_point_probes": [
          "What information did you have available when you assigned the technician?",
          "What other options did you consider before committing Line 3 as overflow capacity?",
          "Did you check whether any other orders depended on Line 3 before making that call?",
          "What made you decide to include the buffer units before QA confirmed the batch?",
          "How did you decide between overtime, partial shipment, and renegotiating the cutoff?"
        ],
        "time_pressure": [
          "How much time did you feel you had to make each of these calls?",
          "Did the time pressure change how much information you gathered before deciding?"
        ],
        "uncertainty": [
          "What were you most unsure about during the Line 3 decision?",
          "How confident were you that the buffer units would pass QA?"
        ],
        "prior_experience": [
          "Have you handled a similar late-delivery situation before? How did that shape your approach here?",
          "Has the Line 3 alarm come up in past shifts?"
        ],
        "closing_hypotheticals": [
          "If you had known Order C depended on Line 3, would you have handled that decision differently?",
          "If you'd had an extra 15 minutes before the technician assignment, would anything have changed?",
          "Looking back, is there a point where you wish you'd gathered more information before deciding?"
        ]
      },
      "occurrence_embedding_plan_internal": [
        {
          "instance_id": "br_01",
          "bias": "Bounded Rationality",
          "decision_point": 2,
          "mechanism": "Under time pressure and multiple concurrent demands, the planner accepts the first workable option (operator's informal 'it usually clears itself' assessment) and commits Line 3 as overflow capacity without searching for or checking readily available information about other order dependencies on Line 3, because fully verifying all downstream implications exceeds the practical time and attention available in the moment.",
          "affected_reasoning_operation": "Evidence search and option evaluation prior to committing a resource",
          "evidence_available_at_time": [
            "Operator's informal, unverified claim that the alarm usually clears itself",
            "Order C's dependency on Line 3 output was discoverable in the scheduling system but not checked",
            "Under 5 hours remained in the shift with two other live decision threads open"
          ],
          "required_textual_manifestation": "The planner should explicitly state that they moved on to the next issue after accepting the operator's assessment, and should acknowledge (when probed) that they did not check whether other orders relied on Line 3 output, framing this as driven by the volume of concurrent issues rather than the information being unavailable.",
          "plausible_nonbias_interpretation": "The planner reasonably trusted an experienced operator's real-time judgment about equipment behavior, which is a legitimate use of frontline expertise under time constraints.",
          "strength": "subtle",
          "do_not_make_explicit": [
            "bounded rationality",
            "satisficing",
            "limited search",
            "cognitive limits",
            "any named cognitive bias term"
          ]
        }
      ],
      "control_specification": {
        "paired_scenario_id": null,
        "features_to_match": [],
        "features_to_remove_or_change": [],
        "ambiguity_boundary": "Not applicable; scenario is biased condition with no paired control in this batch."
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
        "Confirm exactly one Bounded Rationality instance appears, located at decision point 2, and no other decision point contains an independently identifiable instance of the same bias.",
        "Confirm the interview narrative reaches 1,215-1,485 words without repeating the bias manifestation as a summary or restated example elsewhere.",
        "Confirm the operator's 'it usually clears itself' claim and the planner's failure to check Order C dependency are both present as concrete textual evidence supporting br_01.",
        "Confirm decision points 1, 3, and 4 contain no intentional bias instances and are resolved via plausible domain reasoning (order-size prioritization, provisional planning under uncertainty, overtime/logistics trade-off).",
        "Confirm closing hypothetical about Order C directly probes br_01 without naming the bias.",
        "Confirm exactly four decision points exist and each has at least two alternatives listed.",
        "Confirm no bias labels, definitions, or psychological terminology appear anywhere in probe plan or timeline text intended for the public interview."
      ]
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "biased",
      "exact_occurrence_manifest": [
        {
          "bias": "Bounded Rationality",
          "occurrences": 1,
          "mechanism_constraint": null
        }
      ],
      "target_bias_names": [
        "Bounded Rationality"
      ],
      "requested_occurrence_count_for_each_bias": [
        {
          "bias": "Bounded Rationality",
          "requested_occurrences": 1
        }
      ],
      "planned_instance_ids": [
        {
          "instance_id": "br_01",
          "bias": "Bounded Rationality"
        }
      ],
      "intended_decision_points": [
        {
          "instance_id": "br_01",
          "bias": "Bounded Rationality",
          "decision_point": 2
        }
      ],
      "intended_mechanisms": [
        {
          "instance_id": "br_01",
          "bias": "Bounded Rationality",
          "mechanism": "Acceptance of the first satisfactory option (operator's informal reassurance) under multi-threaded time pressure, foregoing a readily available check of Order C's dependency on Line 3 output, because exhaustive verification exceeded practical time and attentional capacity in the moment.",
          "affected_reasoning_operation": "Evidence search and option evaluation prior to resource commitment",
          "evidence_source": "Operator's verbal assessment of the Line 3 alarm; scheduling system data on Order C dependency (available but unchecked)",
          "distinctiveness_requirement": "This is the only planned instance of Bounded Rationality; no other decision point may contain a second independently identifiable manifestation of incomplete search, satisficing, or capacity-limited evaluation attributable to this bias."
        }
      ],
      "intended_strength": [
        {
          "instance_id": "br_01",
          "bias": "Bounded Rationality",
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
      "scenario_id": "IP_Biased_1",
      "domain_id": "IP",
      "total_requested_occurrences": 1,
      "total_planned_occurrences": 1,
      "allocation_rule_used": "Single occurrence assigned to the decision point offering the strongest mechanism fit (multi-threaded time pressure with a readily available but unchecked cross-dependency), consistent with rules 2 and 3 of automatic decision-point assignment; no splitting required since occurrences = 1.",
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
          "segment_id": "dp_01_technician_assignment",
          "speaker": "Participant",
          "segment_type": "decision_episode",
          "raw_interview_anchor": "In the moment I went with unit count — Order A first — partly because that's our default rule when picking between two rush jobs.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The planner considered the tighter packaging slot and selected Order A using an explicit production rule; the generation specification treats this as plausible domain reasoning, not an intentional bias instance."
        },
        {
          "segment_id": "dp_02_line3_alarm_overflow",
          "speaker": "Participant",
          "segment_type": "decision_episode",
          "raw_interview_anchor": "I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "br_01"
          ],
          "ground_truth_rationale": "This is the planned Bounded Rationality instance: under concurrent demands, the planner accepted the first workable assessment and did not check the readily available Order C dependency before committing Line 3."
        },
        {
          "segment_id": "dp_03_qa_buffer_plan",
          "speaker": "Participant",
          "segment_type": "decision_episode",
          "raw_interview_anchor": "I decided to provisionally build the buffer units into the Order B plan rather than wait, because waiting with no ETA on a callback risked losing time I couldn't get back.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The planner made a reversible provisional plan under uncertain QA timing and explicitly planned to adjust if QA flagged an issue; this is treated as reasonable operational planning."
        },
        {
          "segment_id": "dp_04_rework_shipment",
          "speaker": "Participant",
          "segment_type": "decision_episode",
          "raw_interview_anchor": "Overtime plus talking to the carrier directly gave me a shot at getting the full order out with minimal disruption, even shipping a few minutes past official cutoff.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The planner explicitly weighed overtime, partial shipment, and renegotiation, then made a documented cost and customer-service trade-off; the generation specification does not mark this as biased."
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
      "analysis_scope_note": "Conservative mechanism-first review. One attentional/cognitive narrowing occurrence met the identification threshold; two plausible mechanisms were recorded as candidates because the evidence was insufficient under the required standard."
    },
    "identified_bias_summary": [
      {
        "bias_label": "cognitive tunneling",
        "identified_occurrence_count": 1
      }
    ],
    "identified_occurrences": [
      {
        "occurrence_id": "obs_001",
        "classification_status": "identified",
        "confidence": "moderate",
        "bias_label": "cognitive tunneling",
        "alternative_labels": ["attentional tunneling", "tunnel vision", "attentional narrowing"],
        "taxonomy_status": "established_label",
        "bias_definition": "A cognitive/perceptual pattern in which attention becomes locked onto a salient task or goal while task-relevant peripheral information is not processed or checked, especially under high workload or time pressure.",
        "attributed_to_speaker": "Participant",
        "evidence_speaker": "Participant",
        "decision_episode_label": "Line 3 overflow-capacity decision after intermittent alarm report",
        "decision_point_description": "When the Line 3 intermittent alarm was reported, the participant decided to treat Line 3 as available overflow capacity without checking what else depended on Line 3 output.",
        "affected_reasoning_operation": "Attention allocation and situation assessment under concurrent task demands",
        "bias_specific_mechanism": "Under time pressure and competing demands, attention narrowed to the two salient orders (Order A and Order B), so available schedule information about Line 3 was not attended to or searched for.",
        "manifestation_in_interview": "The participant accepted the operator's benign alarm read, immediately treated Line 3 as available overflow, and did not cross-reference the schedule; he later acknowledged that his focus was entirely on Orders A and B and that Order C had been missed.",
        "effect_on_reasoning_or_decision": "He committed to a Line 3 overflow-capacity plan without checking for other dependencies; this later produced an 'oh, right' realization that Order C also needed Line 3 output that shift.",
        "interview_evidence": [
          {
            "speaker": "Participant",
            "verbatim_quote": "I decided to just treat Line 3 as available overflow capacity if Line 1 or Line 2 fell behind, and moved on to the next issue.",
            "evidence_explanation": "This shows that the Line 3 decision was made quickly and was incorporated into the plan without further schedule investigation."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "Honestly, no. I didn't check. My focus was entirely on Order A and Order B — those were the two fires in front of me — so I didn't cross-reference the schedule for anything else running through Line 3.",
            "evidence_explanation": "This is the core affirmative evidence of attentional narrowing: the participant explicitly names the two salient demands that captured his attention and states that this focus prevented him from checking Line 3 schedule dependencies."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "It turned out a smaller order, Order C, also needed Line 3 output that same shift, but I didn't find that out until later. I wasn't ignoring it on purpose, it just wasn't on my radar with everything else going on.",
            "evidence_explanation": "This confirms that the missed dependency was not intentional neglect but a consequence of the attentional focus in the moment."
          }
        ],
        "correction_or_counterevidence": "The participant later recognized the Line 3 call as the decision he would revisit: he said it was the one place 'where a little more digging would have given me a fuller picture before I committed the line,' and that with knowledge of Order C he likely would have taken two minutes to check the schedule. No debiasing action occurred before the decision.",
        "retrieved_corpus_support_available": false,
        "corpus_support_note": "The provided task context did not include retrieved corpus passages for this occurrence; the label 'cognitive tunneling' and its mechanism are assigned from general cognitive-science/human-factors knowledge rather than from retrieved corpus evidence.",
        "corpus_evidence": []
      }
    ],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "availability heuristic",
        "alternative_labels": ["availability bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Line 3 alarm risk assessment and overflow decision",
        "supporting_interview_quote": "The operator told me the alarm had come up before and 'usually clears itself' — an intermittent sensor fault we've seen a handful of times, nothing that's ever caused a real stoppage in his experience.",
        "plausible_mechanism": "The easily recalled pattern of past alarms clearing without a stoppage may have made a benign interpretation more cognitively available, reducing the perceived need to investigate the alarm or check the schedule before using Line 3 as overflow.",
        "why_not_identified": "The evidence is consistent with the availability heuristic, but the participant was also relying on an operator's specific operational experience under explicit time pressure, so the mechanism was not sufficiently separable from ordinary context during the interview."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "plan continuation bias",
        "alternative_labels": ["get-there-itis", "escalation of commitment"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Final rework and shipment decision for Order B",
        "supporting_interview_quote": "Partial shipment felt like a worse customer experience than a slightly late full shipment, and renegotiating the cutoff was a last resort I wanted to avoid if I could still make it work operationally. Overtime plus talking to the carrier directly gave me a shot at getting the full order out with minimal disruption, even shipping a few minutes past official cutoff.",
        "plausible_mechanism": "The participant preserved the original full-shipment goal despite accumulating schedule pressure and additional rework, which may reflect plan continuation tendency rather than full reevaluation of the partial-shipment or renegotiation options.",
        "why_not_identified": "The transcript shows an explicit comparison of alternatives and a flexible operational adjustment rather than non-rational persistence; therefore the biased mechanism was not affirmatively evidenced."
      }
    ],
    "no_supported_biases_found": false,
    "limitations": [
      "No retrieved corpus passages were supplied in the task context, so corpus grounding was unavailable and labels rely on general knowledge with disclosure.",
      "The transcript is a retrospective account, so the analysis is limited to the participant's reported reasoning rather than direct observation of the decisions.",
      "Speaker labels were present and unambiguous in this transcript."
    ]
  }
</RAG_ANALYSIS_OUTPUT>



<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Biased_1_Sonnet_off",
  "interview_id": "IP_Biased_1",
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
