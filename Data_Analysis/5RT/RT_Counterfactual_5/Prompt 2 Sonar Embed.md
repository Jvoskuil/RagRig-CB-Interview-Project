You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time for this. Just to confirm, this is a routine debrief — I want to walk through a specific job you handled, how you made the calls you made, what information you had at each point. Nothing here is about assigning fault. Can you tell me your role?

**Participant:** Sure. I'm a Maintenance-of-Way Supervisor, I run a panel tie gang on the secondary main. I've got about eleven years in track maintenance, six as a supervisor. I handle scoping, scheduling, crew assignment, coordination with dispatch and the roadmaster on outage windows.

**Interviewer:** Good. Tell me about the incident you flagged for this conversation.

**Participant:** We had an ultrasonic rail flaw car come through and flag a detail fracture indication at mile post 47.3 — that's a curve on the secondary main. Dispatch gave us a 60-hour track window to get in there, pull the bad rail, do tie renewal on the segment, get it tamped and squared, and get the slow order lifted before a contracted freight customer's holiday surge started. There was a penalty clause in that contract tied to when the slow order came off, so timing mattered a lot to the regional office.

**Interviewer:** What was your main objective going in?

**Participant:** Get it done safe, get it done in the window. Those two things are supposed to line up, but this one had some tension in it — rain was forecast within about 48 hours, which cuts into ballast curing time, and we only had one tamper and one ballast regulator, shared with the gang working the adjacent territory. So there wasn't a lot of slack.

**Interviewer:** Walk me through what happened, start to finish.

**Participant:** The flaw car report came in on a Tuesday morning. Our last full inspection on that curve was about two weeks old, and it had rated the ties as fair, some deterioration noted, nothing urgent. I used our standard production rate for a 500-foot renewal — so many ties an hour with a full crew — and built a 60-hour schedule off that, plus the fair rating. We mobilized that afternoon.

Once we started pulling ties Wednesday morning, the count came in higher than what I'd planned for — more of them were rotted through than the fair rating suggested. So the roadmaster, two of our inspectors, and my foreman got together that afternoon to talk about how to handle the revised scope inside the same window. The foreman pitched running an extra tamper pass and cutting ballast dwell time to make up the lost hours. One of the inspectors mentioned a similar-looking curve we'd worked three years back that came in light on tie count too, and it held up fine long-term. That gave the room some confidence, and we went with the faster method.

By Thursday's mid-course check-in with the regional engineering manager, we were still behind where the revised plan said we should be, though some segments were actually ahead of pace. I gave him my read on the status. Then Friday morning, six hours before the freight window opened, we hadn't gotten the geometry car through yet — only manual gauge checks — and I had to decide whether to hold the slow order or lift it.

**Interviewer:** Let's go back to Tuesday. What made you comfortable locking in that 60-hour schedule off the fair rating and the standard rate table?

**Participant:** Honestly, the fair rating was the most recent data point I had, and the production table's what we use on every job like this — it's not something I second-guess unless there's a specific reason to. There is a longer defect history on that segment in our system, going back five years, that tracks flaw growth over time. I didn't pull it. At the time it felt like it'd just slow down getting the crew mobilized, and the two-week-old inspection seemed current enough to plan against.

**Interviewer:** Did anything about the flaw car flag itself suggest looking further back?

**Participant:** Looking back, probably. A detail fracture indication at that specific location wasn't the first flag we'd had there, I found out later. But at the time, I treated it as a standalone event and scoped it like a typical renewal.

**Interviewer:** When the tie count came back high on Wednesday, how did the group land on the faster method?

**Participant:** We talked through it for maybe twenty minutes. Nobody walked in pushing hard either way — my foreman had a proposal, the inspectors had questions about dwell time and compaction. But once the prior curve came up, the one that "always held up fine" with a lighter tie count, the room's mood shifted. By the end, everybody was more on board with running fast than any one of us had been at the start of that meeting.

**Interviewer:** Was that prior curve comparable in other respects — soil, drainage?

**Participant:** Not exactly, no. Our site report from the day before had actually flagged the subgrade drainage at 47.3 as worse than typical for that district. Nobody brought that back up once the other curve got mentioned. It just didn't come up again.

**Interviewer:** On Thursday's status call, how did you frame things for the regional manager?

**Participant:** I told him we'd had a late ballast delivery and lost some hours to a rain delay overnight, which was true, both happened. For the segments that were tracking on pace, I credited the crew's execution and the call to add the extra tamper pass. He signed off on keeping the existing timeline.

**Interviewer:** Did the original scope estimate come up as a factor in the slippage?

**Participant:** Not really, no. I didn't bring it up in that call. In hindsight it probably belonged in the conversation, since the tie count coming in high was part of why we were behind in the first place.

**Interviewer:** Friday morning — six hours out from the window opening, geometry car not through yet. What went into that call?

**Participant:** The penalty clause was the thing sitting heaviest on me at that point. Missing that window meant a real financial hit to the region, and I didn't want to be the reason for that. I knew the geometry car would give us a continuous read across the whole segment that manual checks just can't match, but with that loss already sitting right in front of us and the verification still open-ended, avoiding the hit was what drove the call more than anything else. We'd done manual gauge spot-checks across the segment and they came back clean, and I'd set up extra hand-inspection rounds plus a pilot train running the curve at reduced speed before we opened it to normal traffic. The roadmaster pointed out that the hand rounds and the pilot train wouldn't give us the same continuous profile the car would, but I figured between what we already had and those extra rounds, we'd catch anything that mattered. Between those, I felt like we had the risk covered well enough to lift the slow order without waiting on the geometry car.

**Interviewer:** What was the alternative you weighed against that?

**Participant:** Holding the slow order until the geometry car actually ran it, even if that meant eating the penalty. We talked about it briefly with the roadmaster, but the inspection rounds and the pilot train felt like enough of a safety net that we didn't need to wait.

**Interviewer:** What happened with the geometry car pass?

**Participant:** It ran the next day and came back within tolerance. So the track was fine. But I'll say that doesn't necessarily tell you whether lifting it early that morning was the right call or just the way it worked out.

**Interviewer:** If you'd had that five-year defect history in hand on Tuesday, what do you think would've changed?

**Participant:** Probably the initial schedule. If I'd seen recurring flaw growth at that spot, I'd have scoped it heavier from the start instead of finding out mid-job.

**Interviewer:** If the contract penalty hadn't existed, would Friday's decision have gone differently?

**Participant:** I think I'd have been more willing to just wait for the geometry car. It wasn't the only factor, but it was a big part of why six hours felt urgent instead of just cautious.

**Interviewer:** Last one — if a different inspector had been in that Wednesday meeting, someone without that prior-curve story, do you think the method decision changes?

**Participant:** Maybe. That story didn't have hard data behind it, just a memory of how a similar-looking job turned out. Take it out of the room and the conversation might've stayed more cautious. Hard to say for sure.

**Interviewer:** That's helpful. Thanks for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Biased_7",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Maintenance-of-Way Supervisor / Track Maintenance Supervisor",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Curve MP 47.3 Tie Renewal Under Holiday Freight Deadline",
    "scenario_summary_internal": "A Maintenance-of-Way Supervisor manages an emergency tie and rail renewal at a curve (MP 47.3) flagged by an ultrasonic rail-flaw detection car, within a fixed 60-hour track window before a contracted holiday freight surge. Across four chronological decision points—initial scoping/scheduling, team method-selection briefing, a mid-course progress call, and the final go/no-go on lifting the slow order—the supervisor makes judgments under schedule pressure, incomplete inspection data, group dynamics, and contractual penalty exposure. The narrative embeds exactly seven distinct, independently identifiable bias instances (one each of Group Polarization, Ostrich Effect, Self-serving Bias, Planning Fallacy, Loss Aversion, Experience Bias, and Illusion of Control) without naming or explaining any bias, and without the outcome mechanically confirming whether any decision was in fact biased.",
    "occupational_realism": {
      "objective": "Complete emergency tie and rail renewal on a curve segment (MP 47.3) before a contracted holiday freight embargo lifts, while meeting FRA Track Safety Standards and hours-of-service limits.",
      "setting": "Class 1 freight railroad, single main track curve, 500-linear-foot renewal zone, 60-hour authorized track window, secondary main line with a contracted freight customer penalty clause tied to slow-order removal timing.",
      "constraints": [
        "Fixed 60-hour track outage window before holiday freight surge begins",
        "Limited availability of tamper and ballast regulator equipment (shared with adjacent gang)",
        "Contracted freight customer penalty clause for missed slow-order-removal deadline",
        "Forecast rain within 48 hours reducing ballast compaction/curing time",
        "Hours-of-service limits capping crew work periods",
        "FRA-mandated post-work geometry car pass (or documented manual verification) required before restoring authorized speed"
      ],
      "stakeholders": [
        "Track Maintenance Supervisor (interviewee)",
        "Roadmaster",
        "Track inspector(s)",
        "Chief Train Dispatcher",
        "Regional Engineering Manager",
        "Contracted freight customer operations liaison",
        "Tie gang foreman and crew"
      ],
      "technical_terms_to_use": [
        "slow order",
        "tie renewal",
        "tamping",
        "ballast regulator",
        "ultrasonic rail flaw detection",
        "gauge",
        "cross-level",
        "superelevation",
        "FRA Track Safety Standards Class",
        "geometry car",
        "hours of service",
        "embargo",
        "spot replacement",
        "panel tie gang",
        "dwell time"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias",
        "groupthink",
        "psychological terminology of any kind"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Ultrasonic rail flaw detection car flagged a detail fracture indication at MP 47.3",
          "Most recent track inspection report (two weeks old) rated tie condition as 'fair, some deterioration'",
          "Dispatch authorized a 60-hour track outage window",
          "Weather forecast showed rain arriving within 48 hours",
          "A five-year defect-growth history file for this location existed in the maintenance system but had not yet been pulled"
        ],
        "new_information_after_decision": [
          "Once ties were pulled, more required replacement than the standard production-rate estimate assumed",
          "The unreviewed five-year defect file (obtained later) showed recurring flaw growth at this exact location consistent with a larger needed scope"
        ],
        "alternatives": [
          "Pull the full five-year defect-growth history before finalizing scope and duration",
          "Proceed with the standard 500-foot production-rate table and the two-week-old fair-condition rating"
        ],
        "intended_action": "Supervisor sets an initial 60-hour schedule using standard production rates and the fair-condition rating, without requesting the extended defect history, and commits to a best-case tie-pulling duration."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Revised tie count came in higher than the phase-1 estimate",
          "Roadmaster, two track inspectors, and the foreman convened to discuss method",
          "Foreman proposed accelerating via an extra tamper pass and reduced ballast dwell time to protect the schedule",
          "One inspector recalled a curve segment from three years prior that 'always held up fine' with fewer ties replaced",
          "Phase-1 report had noted this curve's subgrade drainage as poorer than typical"
        ],
        "new_information_after_decision": [
          "Drainage conditions at MP 47.3 differed materially from the recalled prior site, which had well-drained subgrade"
        ],
        "alternatives": [
          "Adopt a more conservative method with slower dwell time and an added geometry check before advancing",
          "Endorse the foreman's accelerated method, citing the prior similar-seeming curve as reassurance"
        ],
        "intended_action": "The group collectively endorses the accelerated method with more confidence than any individual voiced beforehand, partly on the strength of the recalled prior curve's track record."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Overall progress was behind the (already revised) schedule despite the accelerated method",
          "Some sub-segments were on pace; others were behind",
          "A scheduled mid-course status call with the Regional Engineering Manager was due"
        ],
        "new_information_after_decision": [
          "Regional Engineering Manager approved continuing the existing timeline without adjustment, unaware that the original scope estimate itself had contributed to the slippage"
        ],
        "alternatives": [
          "Give a status summary that attributes both the delays and the on-pace segments to a mix of factors, including the initial scope estimate",
          "Attribute delays mainly to weather and a late ballast delivery while crediting the on-pace segments to crew skill and his own scheduling calls"
        ],
        "intended_action": "Supervisor delivers the second explanatory narrative to the Regional Engineering Manager."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Contracted freight window was set to open in six hours",
          "The FRA-required geometry car pass had not yet been completed; only manual spot gauge checks had been done",
          "Supervisor had scheduled extra hand-inspection rounds and a slow-rolling pilot train as compensating measures",
          "Contract penalty clause would trigger if the slow order remained past the window opening"
        ],
        "new_information_after_decision": [
          "The geometry car pass, completed a day later, showed the track within tolerance"
        ],
        "alternatives": [
          "Hold the slow order until the geometry car pass is complete, even if it costs the freight window",
          "Lift the slow order now, relying on manual checks plus extra inspection rounds as compensating control"
        ],
        "intended_action": "Supervisor authorizes early removal of the slow order ahead of the geometry car pass, framing the decision around avoiding the contractual penalty and expressing confidence that the added inspection rounds give him sufficient control over residual risk."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role and responsibilities on this job.",
        "Walk me through what this incident was and why it came up.",
        "What was your main objective going into this window?"
      ],
      "timeline_reconstruction": [
        "Take me through what happened first, in order, from the flaw detection report to the final restoration of speed.",
        "Who else was involved at each stage, and what did they contribute?",
        "What information did you have at each point, and where did it come from?"
      ],
      "decision_point_probes": [
        "At the scheduling stage, what cues told you the standard production estimate would hold? What made you decide whether or not to pull additional history on this location?",
        "During the team briefing, how did the group arrive at the accelerated method? What weight did the earlier similar curve carry in that discussion?",
        "On the mid-course call, how did you explain the schedule status? What factors did you emphasize and why?",
        "On the final go/no-go, what alternatives did you weigh regarding the geometry car pass versus lifting the slow order? What made you confident the extra inspection rounds were enough?",
        "What was your basis for each of these calls at the time you made them?",
        "How much time pressure did you feel at each stage, and how did that shape what you considered?",
        "How certain were you about the track condition and the schedule at each point?",
        "Had you handled anything similar before? How did that shape your read of this situation?"
      ],
      "closing_hypotheticals": [
        "If the freight contract penalty hadn't existed, would the final decision have gone differently?",
        "If you'd had the five-year defect history in hand at the outset, what might you have done differently?",
        "If a different crew or a different inspector had been in that briefing, do you think the method decision would have changed?",
        "Looking back, what would you want to know sooner next time a similar flaw indication comes in?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "rt7_01",
        "bias": "Ostrich Effect",
        "decision_point": 1,
        "mechanism": "Supervisor avoids pulling the available five-year defect-growth history that could reveal a larger true scope, preferring to proceed on the more favorable two-week-old 'fair' rating.",
        "affected_reasoning_operation": "Evidence-selection / information-seeking before scope commitment",
        "evidence_available_at_time": [
          "Ultrasonic flaw flag at MP 47.3",
          "Two-week-old inspection rating of 'fair, some deterioration'",
          "Existence of an accessible five-year defect-growth file, not yet retrieved"
        ],
        "required_textual_manifestation": "Supervisor explicitly states he relied on the standard rating and production table and did not request the extended defect file before locking the schedule.",
        "plausible_nonbias_interpretation": "Time constraints made pulling extra records seem unnecessary for a routine-looking scope decision.",
        "strength": "subtle",
        "do_not_make_explicit": ["ostrich effect", "avoidance", "information avoidance"]
      },
      {
        "instance_id": "rt7_02",
        "bias": "Planning Fallacy",
        "decision_point": 1,
        "mechanism": "Supervisor commits to a best-case, standard-production-rate duration estimate for tie replacement without adjusting for site-specific deterioration signals already in hand.",
        "affected_reasoning_operation": "Duration/scope estimation and schedule commitment",
        "evidence_available_at_time": [
          "Standard 500-ft production rate table",
          "Fair-condition tie rating with 'some deterioration' noted",
          "60-hour authorized window"
        ],
        "required_textual_manifestation": "Supervisor describes setting the 60-hour schedule based on the typical rate table, expressing confidence the job would fit that window despite the deterioration note.",
        "plausible_nonbias_interpretation": "Using a standard planning table is normal practice absent stronger contrary evidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "underestimation"]
      },
      {
        "instance_id": "rt7_03",
        "bias": "Group Polarization",
        "decision_point": 2,
        "mechanism": "The briefing group collectively adopts the accelerated method with greater confidence and less caution than individual members expressed before the discussion began.",
        "affected_reasoning_operation": "Collective risk judgment and method selection",
        "evidence_available_at_time": [
          "Foreman's acceleration proposal",
          "Revised, higher tie count",
          "Individual pre-discussion hesitations (implied) about pace"
        ],
        "required_textual_manifestation": "Supervisor recounts that after the group talked it through, everyone ended up more confident in the fast method than they'd been walking in.",
        "plausible_nonbias_interpretation": "Group discussion surfaced legitimate reassuring information that justified more confidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["group polarization", "risky shift"]
      },
      {
        "instance_id": "rt7_04",
        "bias": "Experience Bias",
        "decision_point": 2,
        "mechanism": "An inspector's recollection of a superficially similar curve from three years earlier is used to judge current risk, without accounting for the documented drainage difference at the current site.",
        "affected_reasoning_operation": "Analogical retrieval and risk assessment for method selection",
        "evidence_available_at_time": [
          "Recollection of prior curve's good long-term performance",
          "Phase-1 report noting poorer subgrade drainage at MP 47.3"
        ],
        "required_textual_manifestation": "Supervisor mentions the inspector's reference to the earlier curve as a reason the group felt reassured about the faster method, without connecting it back to the drainage difference.",
        "plausible_nonbias_interpretation": "Drawing on past comparable cases is a legitimate and often necessary part of field judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["experience bias", "overgeneralization from past cases"]
      },
      {
        "instance_id": "rt7_05",
        "bias": "Self-serving Bias",
        "decision_point": 3,
        "mechanism": "In the same status call, the supervisor attributes schedule slippage to external causes (weather, vendor delivery) while attributing on-pace segments to his own scheduling decisions and crew skill, omitting the earlier scope-estimation choice as a contributing factor.",
        "affected_reasoning_operation": "Causal attribution of outcomes during status reporting",
        "evidence_available_at_time": [
          "Mixed progress: some segments on pace, others behind",
          "Known contributing factors: weather delay, late ballast delivery, and the phase-1 scope/duration estimate"
        ],
        "required_textual_manifestation": "Supervisor's account of the mid-course call splits credit and blame along self-favoring lines for the same overall result.",
        "plausible_nonbias_interpretation": "Weather and vendor delays were genuinely real and worth reporting as factors.",
        "strength": "subtle",
        "do_not_make_explicit": ["self-serving bias", "external attribution for failure"]
      },
      {
        "instance_id": "rt7_06",
        "bias": "Loss Aversion or Loss Framing effect",
        "decision_point": 4,
        "mechanism": "The final decision is framed predominantly around avoiding the contractual penalty ('cannot afford to lose the window') rather than balancing it against the safety margin gained by waiting for the geometry car pass.",
        "affected_reasoning_operation": "Weighing of gains versus losses in the final go/no-go choice",
        "evidence_available_at_time": [
          "Six hours until contracted freight window opens",
          "Penalty clause for missing the window",
          "Geometry car pass incomplete; only manual checks done"
        ],
        "required_textual_manifestation": "Supervisor's explanation of the final call centers on the cost of losing the window more than on the value of the still-missing verification.",
        "plausible_nonbias_interpretation": "Contractual penalties are a legitimate operational consideration in any go/no-go call.",
        "strength": "subtle",
        "do_not_make_explicit": ["loss aversion", "loss framing"]
      },
      {
        "instance_id": "rt7_07",
        "bias": "Illusion of Control",
        "decision_point": 4,
        "mechanism": "Supervisor overestimates his ability to manage the residual risk of an incomplete geometry car pass through added hand-inspection rounds and a slow-rolling pilot train, treating these compensating measures as more determinative of safety outcome than they can support.",
        "affected_reasoning_operation": "Risk-control judgment underlying the final authorization",
        "evidence_available_at_time": [
          "Planned extra inspection rounds and pilot train",
          "Manual gauge spot-checks only, no completed geometry car pass"
        ],
        "required_textual_manifestation": "Supervisor expresses confidence that the extra inspection measures are enough to cover for the missing geometry car verification.",
        "plausible_nonbias_interpretation": "Compensating inspection measures are a standard and sometimes sufficient practice before full verification.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of control", "overconfidence in mitigation"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": null
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
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Exactly seven bias instances are planned, one per manifest entry, with no substitutions or additions.",
      "No decision point contains more than two instances of the same bias (all instances here are of different biases within their decision points).",
      "Instances rt7_03 and rt7_04 share decision point 2 but rely on distinct evidence sources and reasoning operations (group risk-shift vs. analogical recall).",
      "Instances rt7_06 and rt7_07 share decision point 4 but rely on distinct reasoning operations (loss-weighted framing vs. control-overestimation) and distinct evidence.",
      "No bias name, definition, or psychological explanation will appear in the public interview text.",
      "Consequences (post-decision information) do not mechanically confirm or refute whether any decision was biased.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points, opening, timeline reconstruction, and closing hypotheticals without repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Group Polarization", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Ostrich Effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Self-serving Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Planning Fallacy", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Loss Aversion or Loss Framing effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Experience Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Illusion of Control", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Group Polarization",
      "Ostrich Effect",
      "Self-serving Bias",
      "Planning Fallacy",
      "Loss Aversion or Loss Framing effect",
      "Experience Bias",
      "Illusion of Control"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Group Polarization", "requested_occurrences": 1 },
      { "bias": "Ostrich Effect", "requested_occurrences": 1 },
      { "bias": "Self-serving Bias", "requested_occurrences": 1 },
      { "bias": "Planning Fallacy", "requested_occurrences": 1 },
      { "bias": "Loss Aversion or Loss Framing effect", "requested_occurrences": 1 },
      { "bias": "Experience Bias", "requested_occurrences": 1 },
      { "bias": "Illusion of Control", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "rt7_01", "bias": "Ostrich Effect" },
      { "instance_id": "rt7_02", "bias": "Planning Fallacy" },
      { "instance_id": "rt7_03", "bias": "Group Polarization" },
      { "instance_id": "rt7_04", "bias": "Experience Bias" },
      { "instance_id": "rt7_05", "bias": "Self-serving Bias" },
      { "instance_id": "rt7_06", "bias": "Loss Aversion or Loss Framing effect" },
      { "instance_id": "rt7_07", "bias": "Illusion of Control" }
    ],
    "intended_decision_points": [
      { "instance_id": "rt7_01", "bias": "Ostrich Effect", "decision_point": 1 },
      { "instance_id": "rt7_02", "bias": "Planning Fallacy", "decision_point": 1 },
      { "instance_id": "rt7_03", "bias": "Group Polarization", "decision_point": 2 },
      { "instance_id": "rt7_04", "bias": "Experience Bias", "decision_point": 2 },
      { "instance_id": "rt7_05", "bias": "Self-serving Bias", "decision_point": 3 },
      { "instance_id": "rt7_06", "bias": "Loss Aversion or Loss Framing effect", "decision_point": 4 },
      { "instance_id": "rt7_07", "bias": "Illusion of Control", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "rt7_01",
        "bias": "Ostrich Effect",
        "mechanism": "Avoids retrieving accessible five-year defect-growth history that could reveal a larger true scope, proceeding instead on the more favorable existing rating.",
        "affected_reasoning_operation": "Evidence-selection before scope commitment",
        "evidence_source": "Existing accessible defect-growth file vs. two-week-old fair rating",
        "distinctiveness_requirement": "Distinct from rt7_02 by operating on information-seeking/avoidance rather than duration estimation."
      },
      {
        "instance_id": "rt7_02",
        "bias": "Planning Fallacy",
        "mechanism": "Commits to a best-case standard production-rate duration despite an available deterioration signal, without adjustment.",
        "affected_reasoning_operation": "Duration/scope estimation and schedule commitment",
        "evidence_source": "Standard production rate table vs. 'fair, some deterioration' rating",
        "distinctiveness_requirement": "Distinct from rt7_01 by concerning time estimation rather than information avoidance, same decision point but different reasoning operation."
      },
      {
        "instance_id": "rt7_03",
        "bias": "Group Polarization",
        "mechanism": "Collective discussion produces greater confidence in the risky/accelerated method than individuals held beforehand.",
        "affected_reasoning_operation": "Collective risk judgment during method selection",
        "evidence_source": "Foreman's acceleration proposal and group discussion dynamic",
        "distinctiveness_requirement": "Distinct from rt7_04 by concerning group-level confidence shift, not individual analogical recall."
      },
      {
        "instance_id": "rt7_04",
        "bias": "Experience Bias",
        "mechanism": "Recollection of a superficially similar past curve is used to judge current risk without accounting for a documented drainage difference.",
        "affected_reasoning_operation": "Analogical retrieval feeding risk assessment",
        "evidence_source": "Inspector's recollection of prior curve vs. phase-1 drainage note",
        "distinctiveness_requirement": "Distinct from rt7_03 by concerning an individual's memory-based analogy rather than group confidence dynamics."
      },
      {
        "instance_id": "rt7_05",
        "bias": "Self-serving Bias",
        "mechanism": "Attributes slippage to external causes while attributing on-pace progress to own decisions/crew skill within the same report.",
        "affected_reasoning_operation": "Causal attribution during status reporting",
        "evidence_source": "Mixed progress data reported to Regional Engineering Manager",
        "distinctiveness_requirement": "Unique to decision point 3; no other instance addresses causal attribution of mixed outcomes."
      },
      {
        "instance_id": "rt7_06",
        "bias": "Loss Aversion or Loss Framing effect",
        "mechanism": "Final decision is framed around avoiding the contractual penalty more heavily than around the safety margin from waiting for verification.",
        "affected_reasoning_operation": "Gain/loss weighting in the final go/no-go choice",
        "evidence_source": "Penalty clause and six-hour window vs. incomplete geometry car pass",
        "distinctiveness_requirement": "Distinct from rt7_07 by concerning the framing/weighting of the choice itself, not confidence in mitigation capability."
      },
      {
        "instance_id": "rt7_07",
        "bias": "Illusion of Control",
        "mechanism": "Overestimates ability of added hand-inspection rounds and pilot train to substitute for a completed geometry car pass.",
        "affected_reasoning_operation": "Risk-control judgment underlying final authorization",
        "evidence_source": "Planned compensating inspection measures vs. absence of completed formal verification",
        "distinctiveness_requirement": "Distinct from rt7_06 by concerning perceived mitigation efficacy, not the loss/gain framing of the decision."
      }
    ],
    "intended_strength": [
      { "instance_id": "rt7_01", "bias": "Ostrich Effect", "strength": "subtle" },
      { "instance_id": "rt7_02", "bias": "Planning Fallacy", "strength": "subtle" },
      { "instance_id": "rt7_03", "bias": "Group Polarization", "strength": "subtle" },
      { "instance_id": "rt7_04", "bias": "Experience Bias", "strength": "subtle" },
      { "instance_id": "rt7_05", "bias": "Self-serving Bias", "strength": "subtle" },
      { "instance_id": "rt7_06", "bias": "Loss Aversion or Loss Framing effect", "strength": "subtle" },
      { "instance_id": "rt7_07", "bias": "Illusion of Control", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "RT_Biased_7",
    "domain_id": "RT",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across decision points by mechanism fit and narrative realism: DP1 (Ostrich Effect, Planning Fallacy) at initial scoping/scheduling; DP2 (Group Polarization, Experience Bias) at the team method-selection briefing, kept distinct via group-level vs. individual-memory mechanisms; DP3 (Self-serving Bias) at the mid-course attribution report; DP4 (Loss Aversion, Illusion of Control) at the final go/no-go, kept distinct via decision-framing vs. mitigation-confidence mechanisms. No decision point holds more than two instances of any single bias, and no bias appears at more than its requested count.",
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
          "segment_type": "objective_and_operational_constraints",
          "raw_interview_anchor": "Get it done safe, get it done in the window. Those two things are supposed to line up, but this one had some tension in it — rain was forecast within about 48 hours, which cuts into ballast curing time, and we only had one tamper and one ballast regulator, shared with the gang working the adjacent territory. So there wasn't a lot of slack.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant balances safety and schedule while identifying real weather and equipment constraints; this is ordinary operational framing."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "duration_and_scope_estimation",
          "raw_interview_anchor": "I used our standard production rate for a 500-foot renewal — so many ties an hour with a full crew — and built a 60-hour schedule off that, plus the fair rating. We mobilized that afternoon.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rt7_02"
          ],
          "ground_truth_rationale": "The supervisor commits to the standard-rate duration without adjusting for the deterioration signal, expressing the hidden Planning Fallacy."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "analogical_case_use_in_method_selection",
          "raw_interview_anchor": "One of the inspectors mentioned a similar-looking curve we'd worked three years back that came in light on tie count too, and it held up fine long-term. That gave the room some confidence, and we went with the faster method.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rt7_04"
          ],
          "ground_truth_rationale": "The prior curve's favorable result reassures the group. Later, the participant says MP 47.3's drainage was worse and the contrary report was not revisited, establishing the hidden Experience Bias in this decision."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "evidence_selection_before_scope_commitment",
          "raw_interview_anchor": "Honestly, the fair rating was the most recent data point I had, and the production table's what we use on every job like this — it's not something I second-guess unless there's a specific reason to. There is a longer defect history on that segment in our system, going back five years, that tracks flaw growth over time. I didn't pull it. At the time it felt like it'd just slow down getting the crew mobilized, and the two-week-old inspection seemed current enough to plan against.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rt7_01"
          ],
          "ground_truth_rationale": "The accessible five-year history was not retrieved before commitment, and the supervisor preferred the recent rating. This is the hidden Ostrich Effect."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "collective_risk_judgment",
          "raw_interview_anchor": "By the end, everybody was more on board with running fast than any one of us had been at the start of that meeting.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rt7_03"
          ],
          "ground_truth_rationale": "The group's confidence in the accelerated method increased beyond members' initial positions during discussion, expressing Group Polarization."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "causal_attribution_in_status_reporting",
          "raw_interview_anchor": "I told him we'd had a late ballast delivery and lost some hours to a rain delay overnight, which was true, both happened. For the segments that were tracking on pace, I credited the crew's execution and the call to add the extra tamper pass. He signed off on keeping the existing timeline.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rt7_05"
          ],
          "ground_truth_rationale": "The report attributes slippage to external causes, credits progress to crew execution and the participant's choices, and omits the initial scope estimate. The later admission confirms that estimate contributed to slippage."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "gain_loss_weighting_in_go_no_go",
          "raw_interview_anchor": "The penalty clause was the thing sitting heaviest on me at that point. Missing that window meant a real financial hit to the region, and I didn't want to be the reason for that. I knew the geometry car would give us a continuous read across the whole segment that manual checks just can't match, but with that loss already sitting right in front of us and the verification still open-ended, avoiding the hit was what drove the call more than anything else.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rt7_06"
          ],
          "ground_truth_rationale": "The participant centers the choice on avoiding the contract penalty despite knowing the higher-fidelity verification remained incomplete, expressing Loss Aversion/Loss Framing."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "risk_control_judgment",
          "raw_interview_anchor": "We'd done manual gauge spot-checks across the segment and they came back clean, and I'd set up extra hand-inspection rounds plus a pilot train running the curve at reduced speed before we opened it to normal traffic. The roadmaster pointed out that the hand rounds and the pilot train wouldn't give us the same continuous profile the car would, but I figured between what we already had and those extra rounds, we'd catch anything that mattered. Between those, I felt like we had the risk covered well enough to lift the slow order without waiting on the geometry car.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rt7_07"
          ],
          "ground_truth_rationale": "The supervisor treats the checks as sufficient substitutes for the missing profile despite a warning that they are not equivalent, expressing Illusion of Control. The composite RAG finding is assigned to the separate penalty-weighting segment under one-to-one matching."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "post_decision_outcome_assessment",
          "raw_interview_anchor": "It ran the next day and came back within tolerance. So the track was fine. But I'll say that doesn't necessarily tell you whether lifting it early that morning was the right call or just the way it worked out.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant separates the favorable outcome from the quality of the earlier decision; this is sound retrospective reasoning."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of one interview transcript for cognitive biases in project decision-making. Only bias-specific mechanisms with affirmative interview evidence are reported."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Hindsight bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Loss aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Optimism bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Ostrich effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value or piece of information when forming judgments, with insufficient adjustment from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Setting the baseline schedule duration for the interlocking replacement project",
      "decision_point_description": "Choosing between the contractor's aggressive 24-month estimate and peer agency data of 28-34 months.",
      "affected_reasoning_operation": "Schedule estimation and judgment under uncertainty",
      "bias_specific_mechanism": "The participant anchored on the contractor's initial best-case proposal and adjusted insufficiently away from it, discounting the peer agency base-rate data as soft or not directly comparable.",
      "manifestation_in_interview": "The participant reported leaning harder on the contractor's numbers and adopting 24 months despite peer agencies typically taking 28 to 34 months.",
      "effect_on_reasoning_or_decision": "The project baseline was set at 24 months, below the peer-agency range, creating an aggressive external target that later shaped schedule decisions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The contractor's proposal assumed efficient crew productivity — their best-case numbers. We also had data from peer agencies that had done similar interlocking swaps, running 28 to 34 months typically.",
          "evidence_explanation": "This establishes two sources of evidence: an aggressive inside estimate and a peer-derived range indicating longer typical durations."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned harder on the contractor's numbers. The peer projects weren't identical — different vendors, different corridor layouts — so the comparison felt soft. We went with 24 months.",
          "evidence_explanation": "The participant discounts the peer evidence and settles on the contractor's initial estimate, consistent with insufficient adjustment from the available anchor."
        }
      ],
      "correction_or_counterevidence": "The peer projects were not identical, so discounting them could have some legitimate basis. Leadership pressure for visible progress may also have influenced the schedule, though it does not fully explain leaning on best-case contractor numbers.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support was available for anchoring bias from Rastogi et al. (2022).",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022)",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The passage supports the anchoring-and-adjustment heuristic, in which an initial value influences a judgment and adjustment from that value is often insufficient.",
          "relevance_to_this_occurrence": "The participant similarly used the contractor's initial 24-month estimate as the focal reference and under-adjusted away from peer data that suggested a longer schedule."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Optimism bias",
      "alternative_labels": ["Unrealistic optimism"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overestimate the probability of positive outcomes and underestimate the probability of negative outcomes, especially for one's own plans or projects.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deciding whether to add contingency for the flagged utility-tolerance segment",
      "decision_point_description": "Deciding between dedicated contingency time and budget for the uncertain utility segment versus relying on standard field verification.",
      "affected_reasoning_operation": "Risk assessment under uncertainty",
      "bias_specific_mechanism": "The participant minimized a live uncertainty signal by treating the tolerance note as resolved through routine process, while also acknowledging that verification would occur only after mobilization inside the possession window.",
      "manifestation_in_interview": "The participant did not add contingency and rated the risk low, saying the uncertainty did not need separate budget.",
      "effect_on_reasoning_or_decision": "The uncertain segment remained an unprovisioned risk, and the later conduit conflict caused a work stand-down on that segment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Field crews verify positions as a matter of course before they dig in any segment, so it felt like that tolerance note was already covered by standard practice.",
          "evidence_explanation": "The participant interpreted the residual uncertainty as already managed by a routine process, even though the tolerance note described a specific positional uncertainty."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew that verification would really only confirm the actual position once we were mobilized inside that possession window — so if something was off, we'd find out on the clock, not ahead of it — but that still felt like enough to keep the segment on plan. Two feet isn't a huge miss, and I didn't see it as something that needed separate budget.",
          "evidence_explanation": "This shows the participant knew the verification was not an early warning, yet still downplayed the likelihood and impact of the flagged uncertainty."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Our risk register logged it as low residual risk once the survey came back. We treated the tolerance note as basically resolved by process, not as an open risk.",
          "evidence_explanation": "The risk was reclassified as low and closed rather than treated as an open item requiring contingency, consistent with optimistic risk minimization."
        }
      ],
      "correction_or_counterevidence": "Commissioning the updated survey was an appropriate review step, and field verification may have been a legitimate control in many segments. A two-foot tolerance could reasonably be judged as manageable; the current analysis is retrospective and the bias inference is indirect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically addressed optimism bias; the label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Hindsight bias",
      "alternative_labels": ["Knew-it-all-along effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overestimate one's ability to have predicted an outcome after it has already occurred.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Retrospective assessment of whether the conduit conflict was foreseeable",
      "decision_point_description": "Answering whether the utility conflict could have been anticipated after the outcome was known.",
      "affected_reasoning_operation": "Retrospective probability and foreseeability judgment",
      "bias_specific_mechanism": "Outcome knowledge inflated the perceived predictability of the conduit conflict, making the uncertain survey segment seem evidently likely in retrospect.",
      "manifestation_in_interview": "The participant said that in hindsight it was almost obvious that something would be slightly off in the flagged segment.",
      "effect_on_reasoning_or_decision": "The participant's retrospective evaluation overstated how foreseeable the conflict had been before the event, even though the risk had been rated low at the time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the survey told us that segment was uncertain. So in hindsight, of course something was going to be slightly off there — it's almost obvious once you say it that way.",
          "evidence_explanation": "The participant's statement is a direct expression of hindsight bias: the outcome now feels predictable because the segment was known to be uncertain."
        }
      ],
      "correction_or_counterevidence": "The participant used the phrase 'in hindsight,' which shows some awareness that the obviousness is retrospective rather than necessarily apparent at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically addressed hindsight bias; the label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Ostrich effect",
      "alternative_labels": ["Information avoidance"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to avoid or delay processing negative information, thereby ignoring potentially important signals.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reviewing and escalating the contractor risk report",
      "decision_point_description": "Deciding how deeply to review and escalate a risk report projecting 6 percent cost overrun and four weeks of schedule impact.",
      "affected_reasoning_operation": "Risk information processing and escalation decision",
      "bias_specific_mechanism": "The participant avoided detailed engagement with threatening cost and schedule information, reading only the executive summary, delegating analysis without a real readout, and not escalating during the review window.",
      "manifestation_in_interview": "The participant described not wanting to sit with the numbers and not asking for a real readout on the detailed analysis.",
      "effect_on_reasoning_or_decision": "The negative risk information was not promptly brought into focus or escalated, and the impact later increased before the issue was formally addressed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Those numbers weren't something I wanted to sit with heading into board season, honestly — reviewing and pushing that forward before the next monitoring cycle gave us anything better felt premature.",
          "evidence_explanation": "This reveals motivated avoidance of uncomfortable cost and schedule information rather than a purely procedural decision to defer."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I read the executive summary, delegated the detailed analysis to one of my leads without asking for a real readout on what it actually showed, and told the team to keep monitoring. I didn't escalate to the grant administrator during that window.",
          "evidence_explanation": "The participant's shallow processing of the report and lack of escalation are behavioral indicators of avoiding the negative information."
        }
      ],
      "correction_or_counterevidence": "The participant had competing demands from quarterly board preparation and a five-day review window, so delegation and reliance on the executive summary may partly reflect ordinary resource constraints. The issue was eventually brought into focus and discussed with the grant side.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically addressed the ostrich effect or information avoidance; the label is drawn from general behavioral-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Loss aversion",
      "alternative_labels": ["Framing effect", "Reference dependence"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to weigh losses relative to one's current reference point more heavily than equivalent gains.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Systems integration testing scope decision near the grant deadline",
      "decision_point_description": "Choosing between an eight-week standard testing protocol and a compressed five-week protocol with $4 million in secured funding at risk.",
      "affected_reasoning_operation": "Tradeoff decision under risk and framing of gains versus losses",
      "bias_specific_mechanism": "The participant valued the $4 million as money already possessed, so avoiding its loss felt weightier than the equivalent potential gain would have felt, leading to compression of testing scope.",
      "manifestation_in_interview": "The participant stated that losing already-secured money felt different from failing to gain the same amount, and confirmed the call would likely have differed if the $4 million were framed as a potential gain.",
      "effect_on_reasoning_or_decision": "The participant chose the compressed five-week testing window despite a solid engineering case for the full eight-week protocol.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We couldn't afford to lose $4 million that was already ours. That was the deciding factor, even though the engineering lead's case for the full protocol was solid.",
          "evidence_explanation": "The decision was driven by avoidance of losing secured money, not by a neutral comparison of testing risks and schedule requirements."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If it were more like a bonus on the table instead of something already secured, I think we hold the full eight weeks. Losing money we already had in hand felt different from missing out on the same amount.",
          "evidence_explanation": "This directly compares equivalent gains and losses and shows asymmetric weighting consistent with loss aversion and reference dependence."
        }
      ],
      "correction_or_counterevidence": "The funding loss risk was real and substantial, and the system ultimately passed commissioning within the compressed window. However, the participant's own counterfactual response indicates the decision would have differed under an equivalent gain frame.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically addressed loss aversion; the label is drawn from general behavioral-economics and cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective interview and therefore depends on self-reported reasoning.",
    "Some occurrences rely on general cognitive-science or behavioral-economics labels because retrieved corpus support was unavailable.",
    "Project decisions were made under real schedule, funding, and operational constraints; some judgments may reflect legitimate tradeoffs rather than bias.",
    "The optimism-bias occurrence is low confidence because the decision to rely on standard field verification may have been reasonable at the time.",
    "Corpus support was available only for anchoring bias; the other identified labels were not directly supported by the retrieved passages."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Counterfactual_5_Sonar_on",
  "interview_id": "RT_Counterfactual_5",
  "system_prompt_id": "Sonar",
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
