You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Biased_1",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
