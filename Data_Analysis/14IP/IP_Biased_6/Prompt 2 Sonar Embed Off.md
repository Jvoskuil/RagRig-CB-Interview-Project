You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on how you handled scheduling decisions during that disruption a few weeks back — Press 3 and the coil-steel delay. Nothing you say here affects performance review, I just want to understand how you actually worked through it. Sound okay?

Participant: Sure, happy to walk through it. It was a fairly full week.

Interviewer: Can you start by telling me who you are and what your role was during this incident?

Participant: I'm the PPC analyst for the stamping shop — I own the rolling five-day schedule across Press 1, 2, and 3, and I coordinate with the three downstream assembly plants that pull from us. That week my job was basically to keep the master schedule intact despite two things going sideways at once.

Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened?

Participant: It started Monday morning. We had a weekend demand surge from one of the assembly plants — they needed an extra batch of the high-volume bracket variant, and Press 3 is the only press currently tooled for that part. I pulled up last week's throughput report and Press 3 had actually run above target, so capacity-wise it looked like the obvious answer. Before I locked anything in, I did get a short heads-up line from the scheduling assistant saying Press 3 had an open vibration advisory — not the full CMMS entry, just a flag. It read as low-priority, and set against how strong the throughput numbers were, it didn't seem like something that should change the call. So I allocated the full extra batch to Press 3.

Then Tuesday, our coil-steel supplier called in a four-day delay. Their rep mentioned "internal allocation constraints," which didn't mean much to me at the time. I've dealt with this supplier for a while — they've had two delays before, both around late December and late June, and both times it sorted itself out within a week without us needing backup stock. Their delays always seem to cluster around certain stretches for them, so I read the timing itself as the real signal — the "internal allocation constraints" line sounded like their usual wording, not something new. So I figured this would follow the same pattern. I did reach out to our backup supplier contact just to have something in reserve, but honestly I called the first person on my list rather than shopping around — we were already stretched that day.

By Thursday, the reliability engineer sent an update saying Press 3's vibration had ticked up slightly since the weekend run. There's a full trend log you can pull that shows three weeks of data, but I didn't open it. Partly because things were moving fast, partly because the number itself wasn't dramatic — nothing like the Press 1 incident a couple years back, which is the kind of thing that jumps to mind when I think "serious press problem." This felt more like background noise.

Then Friday morning, right before I finalized the week's schedule, engineering upgraded Press 3 from "monitor" to "elevated concern." When I asked what that actually meant, the engineer said it reflected a real increase in loading risk, not just a status update on paper. At that point the schedule was basically locked — downstream plants already had confirmation — and shifting the remaining volume to Press 1 would have meant a partial changeover costing several hours. I trimmed Friday's Press 3 run a bit but kept the plan mostly as it was.

Interviewer: Let's reconstruct that timeline a bit more precisely. What did you actually have in front of you Monday morning, before you made the allocation call?

Participant: The throughput report from the prior week, the demand surge notice from the assembly plant, the fact that Press 3 was the only tooled option, and that brief note flagging the vibration advisory. The full CMMS detail wasn't something I pulled up — I just had the short flag.

Interviewer: And the vibration advisory — how did that information reach you in more detail?

Participant: The maintenance tech mentioned more of it in passing, after the allocation was already set, saying there'd be a follow-up inspection recommended within two weeks. It wasn't presented as urgent even then.

Interviewer: When did you first hear about the supplier delay, and what was your first reaction?

Participant: Tuesday, from their account rep directly. My first thought was, "this looks like the same thing that happened in December and June."

Interviewer: Let's go back to the Monday allocation decision. What alternatives did you actually weigh?

Participant: I considered splitting the batch — running part on a temporarily retooled Press 1 and a reduced run on Press 3 — or pushing part of the order to the following week. But the changeover cost and the tight timeline made Press 3 alone the cleanest option.

Interviewer: What made the throughput report feel like the deciding piece of evidence, given you also had that vibration flag?

Participant: It was recent, it was concrete, and it directly answered the question I was asking — can Press 3 handle more volume. The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.

Interviewer: On the supplier delay — walk me through the reasoning that led you to wait rather than order backup stock right away.

Participant: The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution — to me the timing itself was the tell, more than anything they actually said. Their rep's line about "internal allocation constraints" sounded like the kind of thing they always say around these stretches, so it didn't register as pointing to anything different this time.

Interviewer: And the choice of backup contact — what determined which supplier you called?

Participant: Honestly, it's the one I already had a relationship with. I didn't compare lead times or pricing against other options that morning — there wasn't a clean window to do that kind of comparison shopping with everything else going on.

Interviewer: Thursday's vibration note — what determined whether you pulled the full trend log? Do you think opening it would have changed what you had to do that day?

Participant: I had the update in front of me, and I made a call not to dig further right then. If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving. The bi-weekly review was close enough that it felt fine to let it sit until then.

Interviewer: What situation were you picturing when you assessed how serious it might be?

Participant: If I'm honest, I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says "press failure." This didn't look anything like that, so it didn't register as urgent.

Interviewer: Friday, when the status moved to "elevated concern" — how did you weigh that against the schedule you'd already committed to?

Participant: At that point we were locked in with the downstream plants, and a full reallocation meant hours of changeover we didn't have room for. Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had. I trimmed the Friday run slightly rather than overhauling the plan.

Interviewer: What would have had to be different in that assessment for you to change the schedule more substantially?

Participant: Probably if the language had been stronger — something like an explicit downtime risk instead of "elevated concern" — or if it had come earlier in the week when I had more room to maneuver.

Interviewer: What actually happened with Press 3 and the shipments that week?

Participant: Press 3 finished the week without failing. The reliability engineer did file a formal recommendation to reduce loading next cycle. Shipments went out on time to all three plants.

Interviewer: If that Monday flag had appeared directly inside your scheduling dashboard instead of arriving as a separate message from the scheduling assistant, do you think the allocation decision would have gone differently?

Participant: Possibly. If it had been sitting right there next to the throughput numbers instead of coming in as a separate note, I think I'd have paused longer on it instead of leaning mainly on the report.

Interviewer: If you'd had unlimited time that week, is there anything you'd have checked differently?

Participant: I'd have pulled the full trend log Thursday instead of going off the single update, and I probably would have called around to compare backup suppliers instead of just going with who I knew.

Interviewer: Last one — looking back, what's one thing about how information reached you that you'd want changed?

Participant: Honestly, just having the maintenance advisories show up in full where I'm already doing my scheduling. Right now I mostly get a quick flag and have to go looking for the rest, and that week, I didn't.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Biased_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as selective weighting of confirming throughput evidence over disconfirming advisory evidence at decision point 1."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as satisficing/time-constrained alternative selection at decision point 2, distinct from the correlation-bias instance at the same decision point."
      },
      {
        "bias": "Correlation bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as causal misattribution based on superficial temporal pattern-matching to prior unrelated delays, at decision point 2."
      },
      {
        "bias": "Conservatism Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as underweighting new elevated-concern evidence relative to a previously formed belief, at decision point 4."
      },
      {
        "bias": "Imaginability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as risk judgment anchored on ease of recalling a vivid past incident rather than the actual gradual trend data, at decision point 3."
      },
      {
        "bias": "Ostrich effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as avoidance of requesting/reviewing available risk-relevant information (full vibration trend log), at decision point 3, distinct evidence source from the imaginability-bias instance."
      }
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Bounded Rationality",
      "Correlation bias",
      "Conservatism Bias",
      "Imaginability Bias",
      "Ostrich effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confirmation Bias", "requested_occurrences": 1 },
      { "bias": "Bounded Rationality", "requested_occurrences": 1 },
      { "bias": "Correlation bias", "requested_occurrences": 1 },
      { "bias": "Conservatism Bias", "requested_occurrences": 1 },
      { "bias": "Imaginability Bias", "requested_occurrences": 1 },
      { "bias": "Ostrich effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias" },
      { "instance_id": "br_01", "bias": "Bounded Rationality" },
      { "instance_id": "co_01", "bias": "Correlation bias" },
      { "instance_id": "cv_01", "bias": "Conservatism Bias" },
      { "instance_id": "im_01", "bias": "Imaginability Bias" },
      { "instance_id": "oe_01", "bias": "Ostrich effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1 },
      { "instance_id": "co_01", "bias": "Correlation bias", "decision_point": 2 },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 2 },
      { "instance_id": "oe_01", "bias": "Ostrich effect", "decision_point": 3 },
      { "instance_id": "im_01", "bias": "Imaginability Bias", "decision_point": 3 },
      { "instance_id": "cv_01", "bias": "Conservatism Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective weighting of confirming throughput data over disconfirming vibration advisory during capacity allocation",
        "affected_reasoning_operation": "Evidence selection and weighting",
        "evidence_source": "Weekly throughput report vs. CMMS vibration advisory",
        "distinctiveness_requirement": "Unique in involving allocation-stage evidence weighting; not repeated at any other decision point"
      },
      {
        "instance_id": "co_01",
        "bias": "Correlation bias",
        "mechanism": "Causal misattribution of current delay to a seasonal pattern observed in unrelated past delays",
        "affected_reasoning_operation": "Causal attribution based on temporal pattern-matching",
        "evidence_source": "Two historical seasonal delay events vs. current supplier's stated non-seasonal cause",
        "distinctiveness_requirement": "Distinct from br_01 at the same decision point: this instance concerns causal reasoning about delay origin, not alternative selection"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Satisficing selection of the first acceptable backup-supplier option under time pressure without comparative evaluation",
        "affected_reasoning_operation": "Alternative generation and evaluation for sourcing decision",
        "evidence_source": "Single known backup supplier contact vs. unexplored alternative sourcing options",
        "distinctiveness_requirement": "Distinct from co_01: concerns choice among alternatives, not causal explanation of the delay"
      },
      {
        "instance_id": "oe_01",
        "bias": "Ostrich effect",
        "mechanism": "Avoidance of requesting the full vibration trend log to prevent exposure to information that could force rescheduling",
        "affected_reasoning_operation": "Information-seeking/avoidance behavior",
        "evidence_source": "Available but unrequested full trend log",
        "distinctiveness_requirement": "Distinct from im_01 at the same decision point: this instance concerns active avoidance of an information source, not a memory-based risk judgment"
      },
      {
        "instance_id": "im_01",
        "bias": "Imaginability Bias",
        "mechanism": "Risk severity judgment anchored on vividness of a recalled past dramatic incident rather than actual gradual trend data",
        "affected_reasoning_operation": "Probability/severity judgment for escalation",
        "evidence_source": "Recalled Press 1 fire incident vs. gradual three-week vibration trend",
        "distinctiveness_requirement": "Distinct from oe_01: this instance concerns a memory-based comparison heuristic, not an information-avoidance act"
      },
      {
        "instance_id": "cv_01",
        "bias": "Conservatism Bias",
        "mechanism": "Underweighting of new 'elevated concern' status relative to previously formed belief that Press 3 is reliable",
        "affected_reasoning_operation": "Belief updating during final schedule commitment",
        "evidence_source": "New engineering status change vs. prior throughput-based belief from decision point 1",
        "distinctiveness_requirement": "Unique to decision point 4; references but does not duplicate the cb_01 evidence base"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "strength": "subtle" },
      { "instance_id": "co_01", "bias": "Correlation bias", "strength": "subtle" },
      { "instance_id": "cv_01", "bias": "Conservatism Bias", "strength": "subtle" },
      { "instance_id": "im_01", "bias": "Imaginability Bias", "strength": "subtle" },
      { "instance_id": "oe_01", "bias": "Ostrich effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Visibility of Press 3 maintenance advisory in the scheduling workflow",
      "original_state": "Advisory logged only in CMMS, separate from the scheduling dashboard",
      "changed_state": "Advisory surfaced prominently within the scheduling dashboard at the point of allocation",
      "variables_to_hold_constant": [
        "Weekend demand surge and required batch size",
        "Press 3 tooling exclusivity",
        "Supplier delay timing and stated cause",
        "Escalation policy and threshold",
        "All stakeholder identities and roles"
      ]
    },
    "scenario_id": "IP_Biased_6",
    "domain_id": "IP",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Automatic allocation: occurrences spread across 4 decision points, no bias repeated within a decision point, co-located biases at decision points 2 and 3 assigned distinct evidence sources and reasoning operations per mechanism-fit and narrative realism (rules 1-4 of allocation policy).",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Weekend demand surge and required batch size",
      "Press 3 tooling exclusivity for the bracket variant",
      "Supplier delay timing and stated cause",
      "Escalation policy and threshold",
      "All stakeholder identities and roles"
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
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "The throughput report just carried more weight for me.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "Selective weighting of confirming throughput evidence over the disconfirming vibration advisory during the Press 3 allocation."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "causal_attribution",
          "raw_interview_anchor": "The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "co_01"
          ],
          "ground_truth_rationale": "The current supplier delay was causally attributed to a superficial temporal pattern observed in prior delays."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "alternative_selection",
          "raw_interview_anchor": "I called the first person on my list rather than shopping around.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "br_01"
          ],
          "ground_truth_rationale": "The first acceptable backup-supplier option was selected without comparative evaluation under time pressure."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "information_avoidance",
          "raw_interview_anchor": "Pulling three weeks of data might have shown a clearer upward line ... and that could have meant reworking Friday's plan.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "oe_01"
          ],
          "ground_truth_rationale": "The available vibration trend log was not reviewed partly because it might have forced rescheduling."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "severity_assessment",
          "raw_interview_anchor": "I was thinking of the Press 1 fire from a couple years ago ... This didn't look anything like that, so it didn't register as urgent.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "im_01"
          ],
          "ground_truth_rationale": "Risk severity was judged against the vivid recalled fire rather than the gradual vibration trend."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "belief_updating",
          "raw_interview_anchor": "The earlier data ... still felt like the more solid read ... so I didn't weight the new label as heavily.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cv_01"
          ],
          "ground_truth_rationale": "New elevated-concern evidence was underweighted relative to the previously formed throughput-based belief."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The transcript was analyzed for bias-specific reasoning mechanisms in the participant's scheduling decisions during a production disruption. No retrieved scientific-paper passages were available in the context, so bias labels rely on established cognitive-science terminology from general knowledge and all corpus_evidence arrays are empty."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "ostrich effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive heuristic in which the judged probability or expected outcome of an event is based on its resemblance to a known category or remembered past instance, often while underweighting more diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Tuesday supplier-delay prediction",
      "decision_point_description": "Whether to order backup stock immediately after hearing about the coil-steel supplier's four-day delay",
      "affected_reasoning_operation": "Prediction of supplier-delay resolution and backup-stock decision",
      "bias_specific_mechanism": "The participant treated similarity to two prior supplier delays as the main signal for the current delay's likely resolution, interpreting the timing as 'the real signal' and dismissing the specific 'internal allocation constraints' message as usual wording.",
      "manifestation_in_interview": "The participant said his first thought was that the current delay looked like the same thing that happened in December and June, and later explained that the timing pattern, not the supplier's stated reason, drove his expectation.",
      "effect_on_reasoning_or_decision": "He expected the delay to resolve within a week as in the recalled cases and did not immediately order backup stock; he only contacted a familiar backup contact for reserve.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was, 'this looks like the same thing that happened in December and June.'",
          "evidence_explanation": "This explicit first thought shows he categorized the new event by resemblance to past instances before considering the supplier's specific message."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution — to me the timing itself was the tell, more than anything they actually said. Their rep's line about 'internal allocation constraints' sounded like the kind of thing they always say around these stretches, so it didn't register as pointing to anything different this time.",
          "evidence_explanation": "The participant says timing similarity was weighted more than current diagnostic information; this is the representativeness heuristic mechanism."
        }
      ],
      "correction_or_counterevidence": "He did reach out to a backup supplier contact as a reserve, but this did not involve comparing alternatives or ordering backup stock immediately.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; the label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which the perceived likelihood, severity, or importance of an event is influenced by how easily a relevant example comes to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Thursday vibration-risk assessment",
      "decision_point_description": "Whether to treat the Thursday Press 3 vibration update as a serious risk requiring immediate investigation",
      "affected_reasoning_operation": "Assessment of press-failure risk from vibration data",
      "bias_specific_mechanism": "The participant used the easily recalled, dramatic Press 1 fire as the reference point for what a serious press problem looks like. Because the current vibration signal did not resemble that salient memory, he judged it as non-urgent background noise rather than examining the trend.",
      "manifestation_in_interview": "He explicitly says the Press 1 fire is the reference point that comes to mind for 'press failure' and that the current signal didn't look like that, so it didn't register as urgent.",
      "effect_on_reasoning_or_decision": "This comparison contributed to not pulling the full trend log Thursday and not escalating the vibration signal as urgent.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "partly because the number itself wasn't dramatic — nothing like the Press 1 incident a couple years back, which is the kind of thing that jumps to mind when I think 'serious press problem.' This felt more like background noise.",
          "evidence_explanation": "The ease and salience of the Press 1 memory supplies the comparison standard and leads to dismissing the current signal as background noise."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says 'press failure.' This didn't look anything like that, so it didn't register as urgent.",
          "evidence_explanation": "He directly attributes his urgency judgment to the recall of a dramatic prior event, which is the availability heuristic mechanism."
        }
      ],
      "correction_or_counterevidence": "The vibration signal was only slightly elevated at that point, so a less urgent interpretation may also have been reasonable.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; the label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "ostrich effect",
      "alternative_labels": [
        "motivated information avoidance",
        "willful blindness"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A motivated tendency to avoid attending to information that may be threatening or may require an undesired change in behavior.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Thursday decision not to open full trend log",
      "decision_point_description": "Whether to pull the three-week Press 3 vibration trend log after the Thursday update",
      "affected_reasoning_operation": "Information search and monitoring decision",
      "bias_specific_mechanism": "Motivated avoidance of potentially decision-useful information: the participant reports that part of the reason for not opening the trend log was that it might reveal a clearer upward line, which could require reworking Friday's plan.",
      "manifestation_in_interview": "He says 'If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line' and that this could have meant reworking the schedule.",
      "effect_on_reasoning_or_decision": "He chose not to pull the full trend log and let the issue sit until the bi-weekly review.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I had the update in front of me, and I made a call not to dig further right then. If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving. The bi-weekly review was close enough that it felt fine to let it sit until then.",
          "evidence_explanation": "The participant explicitly identifies a motivation to avoid seeing data that might force an unwanted plan change, which is the core mechanism of information avoidance."
        }
      ],
      "correction_or_counterevidence": "He also cited time pressure and the small magnitude of the single-number update; the bi-weekly review was near.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; the label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and insufficient adjustment",
        "conservatism bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to rely too heavily on an initial value, belief, or plan and to make insufficient adjustments when new information arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Friday schedule decision after elevated-concern status",
      "decision_point_description": "Whether to substantially rework the nearly locked schedule after engineering upgraded Press 3 to 'elevated concern'",
      "affected_reasoning_operation": "Integration of new risk information into an existing schedule commitment",
      "bias_specific_mechanism": "The existing schedule and earlier favorable throughput data served as an anchor. When the risk label escalated, the participant did not fully adjust his plan; he weighted the earlier data and committed schedule more heavily than the new risk signal and made only a small trim.",
      "manifestation_in_interview": "He says the earlier data still felt like 'the more solid read' and that he didn't weight the new label as heavily as what he already had.",
      "effect_on_reasoning_or_decision": "He kept the plan mostly intact and only trimmed Friday's Press 3 run, rather than substantively reallocating or overhauling the plan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we were locked in with the downstream plants, and a full reallocation meant hours of changeover we didn't have room for. Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had. I trimmed the Friday run slightly rather than overhauling the plan.",
          "evidence_explanation": "The participant anchored on the committed schedule and earlier favorable throughput data, making only a small adjustment despite the new elevated-concern signal."
        }
      ],
      "correction_or_counterevidence": "Changeover costs and downstream commitments were real logistical factors, and Press 3 ultimately finished the week without failing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; the label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "familiarity heuristic",
      "alternative_labels": [
        "status quo bias",
        "default bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Tuesday backup supplier selection",
      "supporting_interview_quote": "Honestly, it's the one I already had a relationship with. I didn't compare lead times or pricing against other options that morning — there wasn't a clean window to do that kind of comparison shopping with everything else going on.",
      "plausible_mechanism": "Reliance on the existing supplier relationship may reflect a familiarity or default preference, reducing search for possibly better alternatives.",
      "why_not_identified": "The statement also attributes the lack of comparison to time pressure and situational constraints; it does not clearly show that familiarity distorted perceived lead time, price, or quality."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": [
        "selective evidence weighting"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Monday Press 3 allocation decision",
      "supporting_interview_quote": "The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.",
      "plausible_mechanism": "The strong throughput report may have been favored because it supported the preferred clean allocation, while the vibration flag was discounted.",
      "why_not_identified": "The reasoning can be explained as normal evidence weighting: the flag was explicitly low-priority and vague, and the participant considered alternatives and recognized changeover costs. There is insufficient affirmative evidence that the interpretation was motivated by a desire to confirm Press 3 capacity."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper corpus passages were available in the provided context, so all bias labels and definitions derive from general cognitive-science knowledge.",
    "The transcript is a retrospective self-report and may rationalize decisions after the fact.",
    "Some reasoning may be legitimate given operational constraints such as changeover costs, locked downstream commitments, and time pressure.",
    "Several plausible biases may interact, and assigning one primary label per occurrence required isolating the most distinct bias-specific mechanism."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Biased_6_Sonar_off",
  "interview_id": "IP_Biased_6",
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
