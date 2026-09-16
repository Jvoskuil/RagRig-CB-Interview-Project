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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
