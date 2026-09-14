You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Biased_6",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Production Planning and Control (PPC) Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Press 3 Vibration Advisory and the Coil-Steel Delay",
    "scenario_summary_internal": "A PPC analyst at a mid-size automotive stamping plant manages the weekly production schedule across three lines feeding downstream assembly plants. Two nonroutine disruptions surface almost simultaneously: (1) maintenance issues a low-priority vibration advisory on Press 3, a machine the analyst had just relied on for extra weekend capacity, and (2) the primary coil-steel supplier reports a shipment delay. The analyst must decide how to allocate press capacity, how to respond to the supplier delay, whether/when to escalate risk to the plant manager, and how to finalize the committed schedule as new information arrives. The incident is realistic, nonroutine, and does not mechanically resolve in a way that proves any single decision was biased.",
    "occupational_realism": {
      "objective": "Meet the weekly shipment commitment to three downstream assembly plants without exceeding safe equipment operating limits or unplanned downtime, while managing a raw-material supply disruption.",
      "setting": "Stamping and sub-assembly plant producing steel brackets on three hydraulic presses (Press 1, 2, 3), running a rolling 5-day production schedule reviewed every Monday and Thursday.",
      "constraints": [
        "Fixed weekly shipment commitments to three downstream assembly customers with contractual penalty clauses for late delivery",
        "Only one qualified backup coil-steel supplier, with longer lead time and higher unit cost",
        "Press 3 is the only press currently tooled for the high-volume bracket variant needed this week",
        "Maintenance advisories are logged in a separate CMMS system not directly integrated with the scheduling dashboard",
        "Analyst has authority to adjust intra-week allocation but must escalate any capacity risk above a defined threshold to the plant manager"
      ],
      "stakeholders": [
        "PPC Analyst (interviewee)",
        "Plant Manager",
        "Maintenance Technician / Reliability Engineer",
        "Primary coil-steel supplier account representative",
        "Downstream assembly plant schedulers (three plants)"
      ],
      "technical_terms_to_use": [
        "capacity allocation",
        "master production schedule",
        "vibration advisory",
        "lead time",
        "safety stock",
        "throughput report",
        "escalation threshold",
        "CMMS log",
        "coil-steel allocation",
        "tooling changeover"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "bounded rationality",
        "correlation bias",
        "conservatism bias",
        "imaginability bias",
        "ostrich effect",
        "heuristic",
        "cognitive bias",
        "availability heuristic",
        "anchoring"
      ],
      "excluded_themes_note": "None specified by caller."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Press 3 produced above-target output in last week's throughput report",
          "Maintenance has logged a low-priority vibration advisory on Press 3 in the CMMS (not shown on scheduling dashboard)",
          "Weekend demand surge requires additional capacity beyond Press 1 and 2 combined",
          "Press 3 is the only press currently tooled for the required bracket variant"
        ],
        "new_information_after_decision": [
          "Maintenance technician mentions in passing that the advisory recommends a follow-up inspection within two weeks",
          "Press 3 completes the weekend run without incident, but reliability engineer notes the trend is 'worth watching'"
        ],
        "alternatives": [
          "Allocate the extra weekend batch to Press 3 as planned",
          "Split the batch between Press 1 (retooled temporarily) and a reduced Press 3 run",
          "Delay part of the batch to the following week and negotiate with the downstream plant"
        ],
        "intended_action": "Analyst allocates the full extra batch to Press 3, citing last week's strong throughput report as the deciding evidence."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Primary coil-steel supplier reports a 4-day shipment delay",
          "Supplier's account rep cites 'internal allocation constraints' as the cause",
          "Analyst recalls two prior delays from this same supplier, both occurring in late December and late June",
          "Current delay falls in early September, outside those prior windows",
          "A backup supplier is available with a 9-day lead time and 15% higher cost"
        ],
        "new_information_after_decision": [
          "Supplier later clarifies the real cause is a shortage of a specific steel grade, unrelated to seasonal patterns",
          "Backup supplier's shorter-lead option was available but was not evaluated in detail before the decision"
        ],
        "alternatives": [
          "Wait for the primary supplier's delayed shipment without ordering backup stock",
          "Place a partial backup order to cover the shortfall while waiting on the primary shipment",
          "Fully switch the week's coil-steel order to the backup supplier"
        ],
        "intended_action": "Analyst decides to wait for the primary shipment, reasoning that the delay pattern matches prior seasonal delays and will self-resolve, and picks the first available backup contact without comparing other backup options."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Reliability engineer sends an updated CMMS note indicating Press 3 vibration levels have risen slightly since the weekend run",
          "The full vibration trend log (available on request) shows a gradual upward trend over three weeks",
          "Analyst recalls a dramatic Press 1 fire incident from two years ago as the primary mental reference point for 'serious press failure'",
          "Escalation policy requires notifying the plant manager if any press shows a sustained reliability concern"
        ],
        "new_information_after_decision": [
          "Plant manager later asks why the vibration trend log was not reviewed before the schedule was finalized",
          "Maintenance confirms the gradual trend, if unaddressed, typically precedes bearing wear rather than sudden failure"
        ],
        "alternatives": [
          "Pull the full vibration trend log and escalate to the plant manager immediately",
          "Wait for the scheduled bi-weekly maintenance review before deciding whether to escalate",
          "Ask the reliability engineer for a same-day informal opinion instead of the full log"
        ],
        "intended_action": "Analyst does not pull the full trend log, judges the situation as low-risk because it doesn't resemble the vivid Press 1 fire scenario, and defers escalation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Updated engineering assessment (received the morning of schedule finalization) states Press 3 vibration has moved from 'monitor' to 'elevated concern' status",
          "Original schedule already commits Press 3 to a full run through Friday",
          "Downstream plants have been told the schedule is confirmed",
          "Reallocating now would require a partial tooling changeover on Press 1, costing several hours"
        ],
        "new_information_after_decision": [
          "Press 3 completes the week without failure, but the reliability engineer files a formal recommendation for reduced loading next cycle",
          "Downstream plants receive shipments on time this cycle"
        ],
        "alternatives": [
          "Keep the original schedule with only a minor reduction in Press 3's Friday run",
          "Reallocate the remaining Press 3 volume to Press 1 despite the changeover cost",
          "Split remaining volume between Press 1 and Press 3 and shorten the shift on Press 3"
        ],
        "intended_action": "Analyst makes only a minor adjustment to Press 3's Friday run, keeping most of the original schedule despite the elevated-concern status, treating the earlier throughput-based judgment as still largely valid."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what happened that week, from when you first noticed the disruption to when the schedule was finalized.",
        "What was your main objective during this incident?"
      ],
      "timeline_reconstruction": [
        "What information did you have in hand at the very start, before any decisions were made?",
        "At what point did you learn about the vibration advisory, and how did that information reach you?",
        "When did you first hear about the supplier delay, and what was your first reaction?"
      ],
      "decision_point_probes": [
        "What alternatives did you consider before allocating the weekend batch, and why did you choose the one you did?",
        "What made last week's throughput report feel like the most relevant piece of information at that moment?",
        "How did you interpret the pattern of past supplier delays when deciding whether to order backup stock?",
        "What led you to compare this delay to the December and June delays specifically?",
        "When the vibration trend note came in, what determined whether you pulled the full log or not?",
        "What situation were you picturing when you assessed how serious the vibration issue might be?",
        "When the elevated-concern status arrived, how did you weigh it against the schedule you'd already committed to?",
        "What would have had to be different in that updated assessment for you to change the schedule more significantly?"
      ],
      "closing_hypotheticals": [
        "If the vibration advisory had appeared directly on your scheduling dashboard instead of only in the CMMS, do you think your initial allocation decision would have changed?",
        "If you'd had unlimited time that week, is there anything you would have checked differently?",
        "Looking back, what's one thing about how information reached you that you'd want changed for next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 1,
        "mechanism": "Analyst selectively weights the throughput report (confirming Press 3 is reliable) as decisive evidence while downplaying the CMMS vibration advisory (disconfirming evidence) that was available at the same time.",
        "affected_reasoning_operation": "Evidence selection and weighting during capacity allocation",
        "evidence_available_at_time": [
          "Last week's throughput report showing above-target Press 3 output",
          "Existing CMMS vibration advisory on Press 3"
        ],
        "required_textual_manifestation": "The analyst explicitly cites the throughput report as the reason for the allocation and either omits or minimizes the advisory when asked what other information was available.",
        "plausible_nonbias_interpretation": "The advisory was genuinely low-priority and throughput data is a legitimate, standard basis for near-term capacity decisions.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "cherry-picking", "selective evidence"]
      },
      {
        "instance_id": "co_01",
        "bias": "Correlation bias",
        "decision_point": 2,
        "mechanism": "Analyst infers that the current delay shares the same cause as two prior delays because they superficially co-occur with 'supplier delay' events, without verifying the actual causal reason, which later turns out to be unrelated.",
        "affected_reasoning_operation": "Causal attribution of the current disruption based on pattern-matching to past events",
        "evidence_available_at_time": [
          "Two prior supplier delays in December and June, previously attributed to seasonal demand",
          "Current delay's stated cause: 'internal allocation constraints' (no seasonal reference)"
        ],
        "required_textual_manifestation": "The analyst explains the decision to wait by referencing the past delay pattern as if it explains the current one, despite the current delay occurring at a different time of year and having a different stated cause.",
        "plausible_nonbias_interpretation": "Past experience with the same supplier is a reasonable input into scheduling risk, even if imperfect.",
        "strength": "subtle",
        "do_not_make_explicit": ["correlation bias", "spurious correlation", "pattern-matching error"]
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 2,
        "mechanism": "Under time pressure, analyst selects the first minimally acceptable backup-supplier contact rather than evaluating available alternatives on lead time, cost, and quality, satisficing instead of optimizing.",
        "affected_reasoning_operation": "Alternative generation and evaluation for backup sourcing",
        "evidence_available_at_time": [
          "One known backup supplier contact with 9-day lead time and known cost premium",
          "Time constraint: schedule must be finalized before end of day"
        ],
        "required_textual_manifestation": "The analyst describes picking the backup contact quickly without comparing it to other sourcing options, citing time pressure or familiarity rather than a comparative evaluation.",
        "plausible_nonbias_interpretation": "With only one qualified backup supplier realistically available, minimal comparison may be a justified use of limited time.",
        "strength": "subtle",
        "do_not_make_explicit": ["bounded rationality", "satisficing", "cognitive limits"]
      },
      {
        "instance_id": "oe_01",
        "bias": "Ostrich effect",
        "decision_point": 3,
        "mechanism": "Analyst avoids requesting the full vibration trend log after receiving the update note, thereby avoiding exposure to information that might force an unwelcome rescheduling decision.",
        "affected_reasoning_operation": "Information-seeking / avoidance behavior in response to a risk signal",
        "evidence_available_at_time": [
          "Update note indicating vibration levels rose slightly",
          "Full trend log available on request but not yet reviewed"
        ],
        "required_textual_manifestation": "The analyst explains not pulling the full log, giving a reason (busy, waiting for the regular review cycle) that functions as avoidance of potentially schedule-disrupting information.",
        "plausible_nonbias_interpretation": "Deferring to the scheduled bi-weekly maintenance review could be a legitimate adherence to established process.",
        "strength": "subtle",
        "do_not_make_explicit": ["ostrich effect", "information avoidance", "willful ignorance"]
      },
      {
        "instance_id": "im_01",
        "bias": "Imaginability Bias",
        "decision_point": 3,
        "mechanism": "Analyst judges the severity of the current risk by comparing it to a vivid, easily recalled past event (the Press 1 fire) rather than the actual gradual vibration trend, which is harder to picture and therefore underweighted.",
        "affected_reasoning_operation": "Risk assessment / probability judgment for escalation",
        "evidence_available_at_time": [
          "Memory of a dramatic Press 1 fire incident two years prior",
          "Gradual, non-dramatic three-week vibration trend on Press 3"
        ],
        "required_textual_manifestation": "The analyst explicitly references the past dramatic incident as the mental benchmark for 'serious' and concludes the current situation doesn't match it, therefore isn't urgent.",
        "plausible_nonbias_interpretation": "Referencing a known severe failure mode as a benchmark for urgency could be a reasonable, if imperfect, use of experience.",
        "strength": "subtle",
        "do_not_make_explicit": ["imaginability bias", "availability heuristic", "vividness effect"]
      },
      {
        "instance_id": "cv_01",
        "bias": "Conservatism Bias",
        "decision_point": 4,
        "mechanism": "Upon receiving the updated 'elevated concern' engineering assessment, analyst makes only a minor adjustment to the schedule, underweighting the new information relative to the prior belief formed at decision point 1 that Press 3 was reliable.",
        "affected_reasoning_operation": "Belief updating in response to new evidence during final schedule commitment",
        "evidence_available_at_time": [
          "New engineering status change from 'monitor' to 'elevated concern'",
          "Prior belief anchored on last week's throughput report and weekend run without incident"
        ],
        "required_textual_manifestation": "The analyst describes making only a small tweak to the Friday run and explains the reasoning by referring back to the earlier positive throughput evidence rather than substantially revising the plan in light of the new status.",
        "plausible_nonbias_interpretation": "Given sunk costs (tooling, downstream commitments), a measured rather than drastic change could be a legitimate operational trade-off.",
        "strength": "subtle",
        "do_not_make_explicit": ["conservatism bias", "underweighting new evidence", "anchoring on prior belief"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' with no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": "Visibility of the Press 3 maintenance advisory within the scheduling workflow (autoselected as the most theoretically interesting single-variable change for a future counterfactual pairing)",
      "original_state": "Vibration advisory logged only in the separate CMMS system, not surfaced on the scheduling dashboard the analyst uses for capacity allocation",
      "counterfactual_state": "Vibration advisory surfaced directly and prominently within the scheduling dashboard at the moment of the decision point 1 allocation",
      "variables_to_hold_constant": [
        "Weekend demand surge and required batch size",
        "Press 3 tooling exclusivity for the bracket variant",
        "Supplier delay timing and stated cause",
        "Escalation policy and threshold",
        "All stakeholder identities and roles"
      ],
      "expected_causal_difference": "With the advisory surfaced prominently, the confirmation-bias pattern at decision point 1 (cb_01) should be harder to sustain, since the disconfirming evidence would be immediately co-located with the confirming throughput data rather than requiring a separate lookup.",
      "causal_test_question": "Does making the vibration advisory equally visible as the throughput report at the point of allocation change whether the analyst selectively weights confirming evidence over disconfirming evidence?"
    },
    "generation_checks": [
      "Exactly 4 decision points are defined, each with at least two plausible alternatives.",
      "Exactly one instance planned per bias per manifest: Confirmation Bias, Bounded Rationality, Correlation bias, Conservatism Bias, Imaginability Bias, Ostrich effect.",
      "No decision point contains more than one instance of the same named bias.",
      "Decision point 2 and decision point 3 each host two distinct biases with clearly separated evidence sources and reasoning operations, not repetitions of the same thought.",
      "No bias labels, definitions, or psychological terminology are to appear in the public interview text.",
      "Consequences described (no press failure, on-time shipments) do not confirm or refute whether any decision was biased.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given 4 decision points with probes, without relying on repetitive exposition.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes."
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
