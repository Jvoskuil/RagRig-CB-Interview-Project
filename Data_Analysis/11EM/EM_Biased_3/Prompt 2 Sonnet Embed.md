You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary cognitive task analysis interview about your handling of the Millbrook Creek flash flood event. I'll ask you to walk me through what happened, and I may pause to dig into specific decisions. Nothing you say here is used for discipline or performance review. Can you state your role for the record?

Participant: Sure. I'm the county's emergency manager, been in the role about nine years, and I oversee EOC activation, evacuation orders, and shelter coordination for the whole county, but Millbrook Creek is one of our higher-attention areas because of the mobile home park down there.

Interviewer: Good. Before we get into specifics, give me the general shape of the incident.

Participant: It started as a fairly normal night shift. We had a flash flood watch come in from the National Weather Service for a storm system that was moving slower than usual and carrying a lot of moisture. The duty forecaster actually called me directly, which isn't standard for a watch-level product, and mentioned the storm structure looked different from what we typically see. I noted it, but Millbrook Creek has a long track record of handling these watches fine. Fifteen years of data at that gauge, and it's never gone past minor nuisance flooding on any watch I've been part of. So I kept us at routine monitoring rather than activating the EOC. A couple hours later, radar rainfall estimates blew past the watch threshold, and the gauge started climbing faster than anything I'd seen there before. NWS upgraded to a warning. From there we had to evacuate the mobile home park, manage two shelters with uneven capacity, and eventually request mutual aid. We got through it without any deaths, but there was a close call with a transport vehicle on the access road right as it was closing.

Interviewer: Let's reconstruct the timeline in a bit more detail. What information did you have at each stage, and where did it come from?

Participant: Initially it was NWS products plus the forecaster's call, and our own gauge telemetry, which was reading normal. About two hours in, we got updated radar rainfall totals from the regional office, and that's when the gauge began rising sharply. Once the warning was issued, our field liaison at the mobile home park confirmed water was already approaching the lowest units. After the evacuation was underway, Public Works reported the access road was narrowing due to runoff, and that's when the shelter and mutual aid pieces came into play.

Interviewer: Let's go through the decisions one at a time, starting with that initial watch. What alternatives did you consider before deciding to hold at routine monitoring?

Participant: I could've activated the EOC to Level 2 right when the watch came in, gotten resources pre-positioned. I also could've just called the forecaster back and asked more questions before deciding anything. But activating the EOC has real costs — staff overtime, pulling people off other duties — and I didn't want to cry wolf again after we'd done that twice last year on systems that fizzled. Given that gauge has never done anything but minor overflow on a watch, I made the call to hold at routine monitoring and wait for an actual warning before committing resources.

Interviewer: The forecaster flagged this one as structurally different. How did that factor into your decision?

Participant: I heard it, and I noted it, but honestly what carried more weight for me was the track record. That gauge just doesn't misbehave. I've watched a dozen watches come and go there with nothing to show for it, so a watch alone wasn't enough to move me off routine monitoring.

Interviewer: Moving to the evacuation decision once the warning came in. What alternatives did you weigh there?

Participant: We could evacuate with contingency time built in and pre-stage extra transport before ordering it, or issue a partial shelter-in-place for upper units and just pull the ground floor first. I chose to order a full evacuation, and I built the timeline off our fastest previous evacuation of that same park, which was under 90 minutes.

Interviewer: How did you arrive at that specific estimate?

Participant: We'd done it before in daylight with full staffing and it went under 90 minutes, so that was my benchmark. In hindsight, this time was nighttime, we had a skeleton crew until the EOC ramped up, and a chunk of those residents don't have their own vehicles, so it needs door-to-door contact. It ended up taking over three hours, and the shuttle buses from Public Works arrived later than I'd planned for. That gap surprised me at the time, honestly.

Interviewer: What made three hours surprising, given those differences were known going in?

Participant: I suppose I anchored on the best version of that evacuation rather than really adjusting for what was different this time. The information was there — nighttime, staffing, no-vehicle households — I just didn't weight it heavily enough when I set the timeline.

Interviewer: Let's talk about the shelter and mutual aid decision. What were the alternatives?

Participant: We could submit the mutual aid request immediately alongside the shelter routing calls, or split evacuees evenly across both shelters regardless of real-time numbers, or wait on mutual aid until we had firmer capacity data. I routed most evacuees to shelter A based on our initial capacity numbers and held off on mutual aid until we could confirm the picture more fully.

Interviewer: What happened as a result?

Participant: Shelter B actually filled up faster than shelter A because of how people were routed in from the road closures, and by the time we submitted mutual aid, the access road had already closed, so those resources arrived too late to help with the routing problem directly.

Interviewer: Was there information available at that point that could have changed the routing or timing decision?

Participant: The Red Cross coordinator had flagged that shelter B would need extra staff for overflow, and Public Works said the road might close within the hour. I had both of those inputs before I made the call. I was leaning on the initial capacity assumptions more than the live warnings coming in.

Interviewer: Let's move to the after-action review. Walk me through that discussion.

Participant: The panel was going through the timeline, and there was some pointed conversation about the Sheriff's watch commander, who had pushed back internally when the watch first came in, arguing it probably wasn't going to amount to much. People in the room were fairly critical of that, saying he let the historical pattern cloud his judgment on a night when the forecaster was explicitly saying this one was different.

Interviewer: How did you see your own role in that same conversation?

Participant: I felt for him, but I also think there's a difference — he was pushing back without really engaging with the forecaster's call, whereas I did hear it and made a judgment based on the full track record we had. My escalation timing and the evacuation plan were built on real experience with that location, so I'd characterize my decisions as sound given what I knew at each point.

Interviewer: Looking at your own decision log next to his account, do you see any similarities in the pattern?

Participant: I mean, on paper the timing gap looks similar, and I did build the evacuation estimate off a best-case prior run. But I still think context matters — I was managing a lot more moving pieces than he was, so I'd hesitate to put us in the same category.

Interviewer: Last few questions. If the storm had behaved like a typical watch-level event, what would you have done differently?

Participant: Probably nothing — routine monitoring would've been the right call, and we'd have avoided the overtime and disruption. That's part of why the decision felt reasonable going in.

Interviewer: If you'd had unlimited staffing from the very start, what would change about the evacuation?

Participant: I'd have pre-staged the shuttle buses and had more people for door-to-door contact from minute one, which probably closes most of that three-hour gap.

Interviewer: What would you tell a newer emergency manager to watch for in a similar situation?

Participant: Trust the data, but don't dismiss a forecaster who's willing to pick up the phone on something that's usually just a form letter. That's not something they do casually.

Interviewer: Thank you, this has been very helpful.

Participant: Happy to help. Hope it's useful for the next one of these we run into.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Biased_3",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Local Emergency Manager (County/Municipal Level)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Millbrook Creek Flash Flood Escalation",
    "scenario_summary_internal": "A county emergency manager responsible for a river-valley jurisdiction with a documented history of minor, manageable flooding must respond to a rapidly evolving flash flood threat driven by an atypical, slow-moving convective storm cell. The manager must decide when to escalate monitoring, whether and when to order evacuation of a low-lying mobile home community, how to allocate limited shelter and staffing resources under a compressed timeline, and how to frame the response afterward during an after-action review. The scenario is designed to elicit one instance each of Normality Bias (underweighting an atypical threat signal because of a benign local flood history), Planning Fallacy (underestimating time and resource needs for evacuation logistics based on best-case past performance), and Bias Blind Spot (recognizing bias in a colleague's judgment while failing to recognize an analogous pattern in one's own reasoning during reflective probing).",
    "occupational_realism": {
      "objective": "Protect life safety in the Millbrook Creek floodplain by making timely, well-resourced evacuation and resource-allocation decisions during a fast-developing flash flood event.",
      "setting": "County Office of Emergency Management, Emergency Operations Center (EOC), and field liaison with county sheriff, public works, and a regional Red Cross chapter during a 14-hour flash flood event.",
      "constraints": [
        "Limited EOC staffing (skeleton night shift until escalation)",
        "Single road access/egress for the Millbrook Mobile Home Park",
        "State mutual aid resources require 4-6 hour lead time to mobilize",
        "Shelter capacity limited to two designated sites with partial ADA accessibility",
        "Historical gauge data shows only minor, non-damaging overflow events at this location for 15 years",
        "Forecast uncertainty regarding storm cell movement and rainfall totals"
      ],
      "stakeholders": [
        "County Emergency Manager (interviewee)",
        "Sheriff's Office watch commander",
        "Public Works director",
        "Red Cross regional coordinator",
        "Mobile home park residents",
        "National Weather Service (NWS) forecaster",
        "County Board liaison"
      ],
      "technical_terms_to_use": [
        "flash flood watch/warning",
        "EOC activation level",
        "gauge height",
        "evacuation order vs. advisory",
        "mutual aid request",
        "shelter-in-place",
        "after-action review (AAR)"
      ],
      "technical_terms_to_avoid": [
        "normalcy bias",
        "planning fallacy",
        "bias blind spot",
        "cognitive bias",
        "heuristic",
        "anchoring",
        "overconfidence bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "NWS issues a flash flood watch citing an unusually slow-moving, high-precipitable-water storm cell",
          "Gauge at Millbrook Creek is at normal seasonal level",
          "Fifteen years of records show only minor, non-damaging overflow at this gauge during comparable watches",
          "Duty forecaster verbally flags this event as atypical in structure"
        ],
        "new_information_after_decision": [
          "Radar-estimated rainfall totals exceed the watch threshold within two hours",
          "Gauge begins rising faster than any prior watch-level event on record"
        ],
        "alternatives": [
          "Activate EOC to Level 2 and pre-position resources immediately",
          "Maintain routine monitoring and wait for a warning (not just a watch) before escalating",
          "Request an informal check-in call with NWS forecaster before deciding"
        ],
        "intended_action": "Maintain routine monitoring, citing the area's consistent history of manageable events, and defer formal escalation until a warning is issued."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Gauge has now crossed the warning threshold; NWS upgrades to a flash flood warning",
          "Millbrook Mobile Home Park (140 residents, single-road egress) sits in the most exposed zone",
          "Past voluntary evacuations of this park have been completed in under 90 minutes",
          "Current event involves nighttime conditions and a portion of residents without vehicles"
        ],
        "new_information_after_decision": [
          "Actual evacuation notification and loading takes over three hours due to door-to-door contact needs and one blocked access point",
          "Shuttle buses requested from Public Works arrive later than estimated"
        ],
        "alternatives": [
          "Order evacuation with a timeline built on the fastest prior comparable evacuation",
          "Order evacuation with contingency buffer time and pre-stage additional transport before ordering",
          "Issue a shelter-in-place advisory for upper units, evacuate only ground-level units first"
        ],
        "intended_action": "Order full evacuation using a timeline modeled on the fastest previous evacuation of the same park, without adding contingency time for nighttime conditions or reduced staffing."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two designated shelters have uneven capacity; one is nearing its limit",
          "Red Cross coordinator flags that overflow routing to shelter B will require additional staff not yet on site",
          "Public Works reports the access road may close within the hour due to rising water",
          "Mutual aid request has not yet been formally submitted"
        ],
        "new_information_after_decision": [
          "Shelter B reaches capacity faster than shelter A due to uneven routing",
          "Mutual aid resources arrive after the access road has already closed"
        ],
        "alternatives": [
          "Submit the mutual aid request immediately alongside shelter routing decisions",
          "Delay mutual aid request until shelter capacity data is fully confirmed",
          "Split resources evenly between shelters regardless of real-time capacity reports"
        ],
        "intended_action": "Route evacuees primarily to shelter A based on initial capacity assumptions, and delay the mutual aid request pending further confirmation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Event concludes with no fatalities but a near-miss when the access road closed with a transport vehicle still en route",
          "After-action review is being conducted; a Sheriff's Office colleague is criticized in the room for having doubted the initial watch severity",
          "Interviewer asks the emergency manager to reflect on decision quality across the event",
          "Manager has direct visibility into their own decision log from phases 1-3"
        ],
        "new_information_after_decision": [
          "AAR panel later flags the same monitoring-escalation lag in the manager's own timeline that was criticized in the colleague's account",
          "Documentation shows the manager's evacuation and shelter estimates also relied on best-case historical benchmarks"
        ],
        "alternatives": [
          "Acknowledge that one's own escalation and estimation judgments may share the same pattern being criticized in the colleague",
          "Attribute the colleague's hesitation to a personal or situational shortcoming distinct from one's own decision-making",
          "Request a structured, criteria-based comparison of both decision timelines before drawing conclusions"
        ],
        "intended_action": "Critique the colleague's initial hesitation as a personal misjudgment while describing one's own escalation and estimation decisions as sound and well-reasoned given the information at the time."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first caught your attention about this event?",
        "What was your role and objective at the very start of the shift?"
      ],
      "timeline_reconstruction": [
        "What information did you have at each stage, and where did it come from?",
        "What changed between the watch and the warning, and when did you learn it?",
        "Walk me through what happened at the mobile home park step by step."
      ],
      "decision_point_probes": [
        "What alternatives did you consider before deciding to hold at routine monitoring?",
        "How did you arrive at the evacuation timeline estimate?",
        "What made you choose shelter A as the primary routing destination?",
        "How did you weigh the mutual aid timing decision against road-closure risk?"
      ],
      "closing_hypotheticals": [
        "If the storm had behaved exactly like a typical prior event, what would you have done differently, if anything?",
        "Looking back at the after-action discussion, do you see anything in your own decisions that mirrors what was raised about your colleague?",
        "If you had unlimited staffing from the outset, what would you change about the evacuation plan?",
        "What would you tell a newer emergency manager to watch for in a similar event next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "nb_01",
        "bias": "Normality Bias",
        "decision_point": 1,
        "mechanism": "Manager discounts an explicit forecaster warning that the storm is atypical, instead anchoring the threat assessment to fifteen years of benign local outcomes at the same gauge.",
        "affected_reasoning_operation": "Risk assessment / threat classification under initial ambiguous evidence",
        "evidence_available_at_time": [
          "NWS flash flood watch citing atypical storm structure",
          "Direct verbal flag from duty forecaster that the event differs from past patterns",
          "Fifteen-year benign outcome history at the gauge"
        ],
        "required_textual_manifestation": "Manager explicitly justifies delaying escalation by referencing the gauge's consistent past behavior, without addressing the forecaster's specific atypicality flag.",
        "plausible_nonbias_interpretation": "Resource-conscious managers reasonably avoid over-escalating on every watch given staffing costs and false-alarm fatigue.",
        "strength": "subtle",
        "do_not_make_explicit": ["normalcy bias", "base rate", "historical bias", "cognitive bias"]
      },
      {
        "instance_id": "pf_01",
        "bias": "Planning Fallacy",
        "decision_point": 2,
        "mechanism": "Evacuation timeline is built from the single fastest historical evacuation of the same park, ignoring known complicating factors present in this event (nighttime, reduced staffing, no-vehicle residents) that were absent in the reference case.",
        "affected_reasoning_operation": "Duration/resource estimation for a multi-step logistics task",
        "evidence_available_at_time": [
          "Prior evacuation records showing a 90-minute best case",
          "Known nighttime conditions and partial lack of resident vehicles",
          "Single-road egress constraint"
        ],
        "required_textual_manifestation": "Manager states the evacuation was planned around the fastest prior completion time without incorporating adjustments for the differing conditions, and expresses surprise when the real duration triples.",
        "plausible_nonbias_interpretation": "Using a recent successful precedent as a planning baseline is a common and often reasonable heuristic when time is short.",
        "strength": "moderate",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "reference class", "underestimation bias"]
      },
      {
        "instance_id": "bbs_01",
        "bias": "Bias Blind Spot",
        "decision_point": 4,
        "mechanism": "During the after-action reflection, the manager readily identifies a judgment flaw (hesitation despite a warning) in a colleague's account but does not recognize the same pattern of discounting atypical evidence and using best-case estimates in their own documented decisions from the same event.",
        "affected_reasoning_operation": "Self-referential judgment evaluation during retrospective causal attribution",
        "evidence_available_at_time": [
          "Colleague's criticized hesitation described in the AAR discussion",
          "Manager's own decision log from phases 1-3, directly accessible in the same review",
          "AAR panel's later note that both timelines show a similar escalation lag"
        ],
        "required_textual_manifestation": "Manager critiques the colleague's judgment in specific terms while describing their own analogous decisions as sound and appropriately reasoned, despite having the same information available for self-comparison.",
        "plausible_nonbias_interpretation": "It is reasonable to believe one had more context or better justification for a decision than an outside observer initially credits.",
        "strength": "subtle",
        "do_not_make_explicit": ["bias blind spot", "self-serving bias", "third-person bias", "meta-bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario is specified for this generation request."
    },
    "counterfactual_specification": {
      "causal_variable": "Lead time between forecaster's atypicality flag and formal EOC escalation decision",
      "original_state": "Manager defers escalation until a formal warning is issued, roughly two hours after the atypicality flag and rainfall exceedance",
      "counterfactual_state": "Manager escalates EOC activation immediately upon receiving the forecaster's atypicality flag, prior to formal warning issuance",
      "variables_to_hold_constant": [
        "Storm behavior and rainfall totals",
        "Mobile home park population and access constraints",
        "Shelter capacity and staffing availability",
        "Mutual aid lead time requirements",
        "After-action review structure and participants"
      ],
      "expected_causal_difference": "Earlier escalation would likely compress the evacuation and shelter-routing timeline, reducing the near-miss at the access road, and would provide a direct causal contrast for isolating the effect of the Normality Bias instance at decision point 1.",
      "causal_test_question": "Would earlier EOC escalation, holding storm behavior and population constant, have prevented the downstream evacuation and routing time pressure observed in the biased condition?"
    },
    "generation_checks": [
      "Confirm interview draft falls between 1,215 and 1,485 words",
      "Confirm exactly 4 decision points are present and clearly demarcated",
      "Confirm each of nb_01, pf_01, bbs_01 appears exactly once with sufficient evidence trace",
      "Confirm no bias name, definition, or psychological label appears in interview text",
      "Confirm each decision point offers at least two plausible alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm consequences described do not mechanically prove bias presence",
      "Confirm no unintended additional instance of any named bias is introduced in probes, hypotheticals, or summaries"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Bias Blind Spot",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as self/other asymmetry during retrospective reflection, not as a general statement about bias existing in others."
      },
      {
        "bias": "Normality Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as discounting an explicit atypicality signal in favor of historical base-rate outcomes at the initial threat-assessment decision."
      },
      {
        "bias": "Planning Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as duration/resource estimation anchored to a best-case precedent while ignoring known differing conditions."
      }
    ],
    "target_bias_names": ["Bias Blind Spot", "Normality Bias", "Planning Fallacy"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Bias Blind Spot", "requested_occurrences": 1},
      {"bias": "Normality Bias", "requested_occurrences": 1},
      {"bias": "Planning Fallacy", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "nb_01", "bias": "Normality Bias"},
      {"instance_id": "pf_01", "bias": "Planning Fallacy"},
      {"instance_id": "bbs_01", "bias": "Bias Blind Spot"}
    ],
    "intended_decision_points": [
      {"instance_id": "nb_01", "bias": "Normality Bias", "decision_point": 1},
      {"instance_id": "pf_01", "bias": "Planning Fallacy", "decision_point": 2},
      {"instance_id": "bbs_01", "bias": "Bias Blind Spot", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "nb_01",
        "bias": "Normality Bias",
        "mechanism": "Discounting an explicit forecaster atypicality flag by anchoring on fifteen years of benign gauge history",
        "affected_reasoning_operation": "Initial threat classification under ambiguous but flagged evidence",
        "evidence_source": "NWS flash flood watch text and duty forecaster verbal flag versus historical gauge record",
        "distinctiveness_requirement": "Unique to decision point 1; must not be repeated as a restated justification at later decision points."
      },
      {
        "instance_id": "pf_01",
        "bias": "Planning Fallacy",
        "mechanism": "Anchoring evacuation duration estimate to the single fastest historical precedent while omitting known aggravating conditions present in the current event",
        "affected_reasoning_operation": "Time/resource estimation for evacuation logistics",
        "evidence_source": "Prior evacuation completion-time record versus current nighttime/staffing/vehicle-access conditions",
        "distinctiveness_requirement": "Unique to decision point 2; distinct evidence (logistics timing) from the threat-classification evidence used in nb_01."
      },
      {
        "instance_id": "bbs_01",
        "bias": "Bias Blind Spot",
        "mechanism": "Recognizing a judgment flaw in a colleague's decision while failing to apply the same evaluative standard to one's own analogous decisions from the same event",
        "affected_reasoning_operation": "Retrospective self-evaluation during after-action causal attribution",
        "evidence_source": "AAR colleague critique versus manager's own decision log covering phases 1-3",
        "distinctiveness_requirement": "Unique to decision point 4; occurs only during reflective/self-referential probing, not during real-time decisions."
      }
    ],
    "intended_strength": [
      {"instance_id": "nb_01", "bias": "Normality Bias", "strength": "subtle"},
      {"instance_id": "pf_01", "bias": "Planning Fallacy", "strength": "moderate"},
      {"instance_id": "bbs_01", "bias": "Bias Blind Spot", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Lead time between forecaster's atypicality flag and formal EOC escalation decision",
      "original_state": "Escalation deferred until formal warning issuance (~2 hours after atypicality flag)",
      "changed_state": "Escalation triggered immediately upon receiving atypicality flag, prior to formal warning",
      "variables_to_hold_constant": [
        "Storm behavior and rainfall totals",
        "Mobile home park population and access constraints",
        "Shelter capacity and staffing availability",
        "Mutual aid lead time requirements",
        "After-action review structure and participants"
      ]
    },
    "scenario_id": "EM_Biased_3",
    "domain_id": "EM",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Each bias assigned to a distinct decision point selected for mechanism fit and narrative realism: Normality Bias to the initial ambiguous-threat decision (point 1), Planning Fallacy to the resource/time estimation decision (point 2), and Bias Blind Spot to the reflective after-action decision (point 4), leaving point 3 as a neutral/control decision point with no intended bias instance.",
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
          "segment_type": "initial threat assessment and escalation decision",
          "raw_interview_anchor": "Initial flash flood watch discussion: the participant cites fifteen years of benign gauge history, downweights the duty forecaster's atypicality call, and keeps the EOC at routine monitoring.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["nb_01"],
          "ground_truth_rationale": "The participant discounts an explicit atypicality signal in favor of historical benign outcomes at the initial threat-assessment decision."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "evacuation duration estimation and plan selection",
          "raw_interview_anchor": "Evacuation discussion: the participant bases the timeline on the fastest prior evacuation and later acknowledges insufficient adjustment for nighttime conditions, skeleton staffing, and residents without vehicles.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["pf_01"],
          "ground_truth_rationale": "The participant uses a best-case precedent for duration estimation while failing to incorporate known aggravating conditions."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "shelter routing decision",
          "raw_interview_anchor": "Shelter and mutual-aid discussion: the participant routes most evacuees to shelter A based on initial capacity numbers despite live overflow warnings.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Decision point 3 is a neutral/control point in the hidden manifest; the occurrence manifest is exhaustive."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "mutual aid timing decision",
          "raw_interview_anchor": "Shelter and mutual-aid discussion: the participant delays the mutual-aid request until capacity is confirmed despite the reported risk that the access road may close within the hour.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a substantive resource-timing rationale but no hidden bias instance is assigned to decision point 3."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "after-action attribution of colleague judgment",
          "raw_interview_anchor": "After-action review discussion: the participant characterizes the Sheriff's watch commander's reliance on the historical pattern as a judgment failure.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The colleague critique alone is not the hidden Bias Blind Spot occurrence; the occurrence requires the subsequent self/other asymmetry."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "retrospective self-comparison and causal attribution",
          "raw_interview_anchor": "After-action self-comparison: the participant acknowledges a similar timing gap and best-case estimate in their own decisions but still describes their own decisions as sound and declines to place them in the same category as the colleague.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["bbs_01"],
          "ground_truth_rationale": "The participant applies a critical standard to the colleague while resisting the same interpretation for analogous decisions in their own decision log."
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
    "analysis_scope_note": "Analyzed the transcript for affirmatively evidenced cognitive bias mechanisms only. Retrieved corpus passages were used to ground normalcy bias and anchoring bias; bias blind spot is identified from general cognitive-science knowledge because retrieval did not contain a supporting passage."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "Bias blind spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Normalcy bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Normalcy bias",
      "alternative_labels": ["Threat underestimation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to disbelieve or disregard a threat by viewing the situation as normal or routine despite anomalous or warning cues.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial flash flood watch monitoring decision",
      "decision_point_description": "The participant considered whether to activate the EOC or remain at routine monitoring after a flash flood watch and a direct forecaster call that stated the storm structure looked different.",
      "affected_reasoning_operation": "Threat/severity assessment and emergency activation decision",
      "bias_specific_mechanism": "The participant underweighted a live, unusual threat cue from the forecaster and over-relied on the gauge's long benign history, leading him to perceive the situation as normal despite the explicit warning.",
      "manifestation_in_interview": "He acknowledges the forecaster called directly and said the storm structure looked different, but repeatedly cites the gauge's 15-year track record and states 'that gauge just doesn't misbehave', keeping the response at routine monitoring.",
      "effect_on_reasoning_or_decision": "The EOC was not activated and resources were not pre-positioned during the watch phase; the unusual storm was treated as a routine watch-level event.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The duty forecaster actually called me directly, which isn't standard for a watch-level product, and mentioned the storm structure looked different from what we typically see. I noted it, but Millbrook Creek has a long track record of handling these watches fine. Fifteen years of data at that gauge, and it's never gone past minor nuisance flooding on any watch I've been part of. So I kept us at routine monitoring rather than activating the EOC.",
          "evidence_explanation": "This shows an anomalous forecaster cue was acknowledged but overridden by the historical pattern, causing a routine response."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I heard it, and I noted it, but honestly what carried more weight for me was the track record. That gauge just doesn't misbehave.",
          "evidence_explanation": "This explicitly states that the historical track record outweighed the current threat-specific information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't want to cry wolf again after we'd done that twice last year on systems that fizzled.",
          "evidence_explanation": "This shows prior false-alarm outcomes reinforced the default assumption of normality rather than focusing on current differences."
        }
      ],
      "correction_or_counterevidence": "The participant did notice and record the forecaster's call, and later advised a newer emergency manager not to dismiss a forecaster who picks up the phone. However, no contemporaneous correction altered the watch-phase decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The Kinsey et al. source directly defines normalcy bias in emergency threat appraisal and was used as retrieval grounding.",
      "corpus_evidence": [
        {
          "source_identifier": "Kinsey Cognitive Biases Within Decision Making During Fire Evacuations.pdf",
          "paper_title": "Cognitive Biases Within Decision Making During Fire Evacuations",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Normalcy bias is the phenomenon where people disbelieve or disregard the threat altogether—thinking that nothing is happening that places them at risk. In the former case, individuals believe that 'nothing unusual is happening'.",
          "mechanism_supported_by_source": "The source defines normalcy bias as disregarding threat and believing nothing unusual is happening, which is the same mechanism shown by the participant's reliance on the gauge's benign history.",
          "relevance_to_this_occurrence": "The participant treated the forecaster's 'different' signal as insufficient to change a routine watch response because the gauge 'just doesn't misbehave', matching the source-defined normalcy bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value or prior example when making an estimate, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evacuation timeline estimate for Millbrook Creek mobile home park",
      "decision_point_description": "When ordering a full evacuation, the participant estimated the time required using the fastest previous evacuation of the same park as the baseline.",
      "affected_reasoning_operation": "Duration/timeline estimation for evacuation planning",
      "bias_specific_mechanism": "Anchoring and insufficient adjustment: he used the under-90-minute previous daylight, fully staffed evacuation as an anchor and failed to sufficiently adjust for nighttime conditions, skeleton staffing, and no-vehicle households.",
      "manifestation_in_interview": "The participant states he built the timeline from the fastest previous evacuation and later explicitly says he 'anchored on the best version' and did not sufficiently weight the known differences.",
      "effect_on_reasoning_or_decision": "The evacuation timeline was underestimated; the operation took over three hours instead of under 90 minutes, and shuttle buses arrived later than planned, contributing to a close call on the access road.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I chose to order a full evacuation, and I built the timeline off our fastest previous evacuation of that same park, which was under 90 minutes.",
          "evidence_explanation": "This establishes the best-case previous evacuation as the anchor for the new timeline."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd done it before in daylight with full staffing and it went under 90 minutes, so that was my benchmark.",
          "evidence_explanation": "This shows the anchor was known to come from materially different conditions but was still used as the reference point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I suppose I anchored on the best version of that evacuation rather than really adjusting for what was different this time. The information was there — nighttime, staffing, no-vehicle households — I just didn't weight it heavily enough when I set the timeline.",
          "evidence_explanation": "This is an explicit self-report of the anchoring-and-adjustment mechanism and insufficient adjustment."
        }
      ],
      "correction_or_counterevidence": "The participant identifies the anchoring in the interview, but only as a later retrospective acknowledgment after the operational delay had occurred.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The Rastogi et al. source supports the anchoring-and-adjustment heuristic and its effect on insufficient adjustment from an anchor.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source documents the anchoring-and-adjustment heuristic: decision makers tend to adjust insufficiently from an anchor without adequate time or effort.",
          "relevance_to_this_occurrence": "The participant's best-case previous evacuation served as the anchor, and he insufficiently adjusted for changed operational conditions."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment heuristic", "Insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on initial information or assumptions and to adjust insufficiently in response to new, discrepant information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Shelter routing and mutual aid request timing",
      "decision_point_description": "After evacuation began, the participant decided to route most evacuees to shelter A and to delay mutual aid until the capacity picture was clearer.",
      "affected_reasoning_operation": "Resource allocation and timing of mutual aid request under evolving information",
      "bias_specific_mechanism": "The participant anchored on the initial shelter capacity numbers and resource assumptions, underweighting live warnings from Red Cross and Public Works that were inconsistent with those initial assumptions.",
      "manifestation_in_interview": "He reports routing based on initial capacity numbers and holding mutual aid, then acknowledges he had the Red Cross and Public Works warnings before the decision but was 'leaning on the initial capacity assumptions more than the live warnings'.",
      "effect_on_reasoning_or_decision": "Shelter B filled faster than expected, mutual aid was requested too late, and the access road closed before those resources could help with the routing problem.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I routed most evacuees to shelter A based on our initial capacity numbers and held off on mutual aid until we could confirm the picture more fully.",
          "evidence_explanation": "This identifies the initial capacity numbers as the anchor and shows the delay was maintained pending confirmatory data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The Red Cross coordinator had flagged that shelter B would need extra staff for overflow, and Public Works said the road might close within the hour. I had both of those inputs before I made the call. I was leaning on the initial capacity assumptions more than the live warnings coming in.",
          "evidence_explanation": "This explicitly acknowledges discrepant live warnings were available and were underweighted relative to the initial assumptions."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction occurred. Waiting for firmer capacity data could in isolation reflect ordinary uncertainty, but the statement that he leaned on initial assumptions more than live warnings provides affirmative evidence of anchoring.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The same Rastogi et al. retrieval supports the anchoring-and-adjustment mechanism; no emergency-management-specific source was available.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports the anchoring-and-adjustment heuristic: initial information can function as an anchor and adjustment away from it is often insufficient.",
          "relevance_to_this_occurrence": "The participant's initial shelter capacity assumptions served as an anchor, and live warnings were not sufficiently weighted to adjust the routing and mutual aid decisions."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Bias blind spot",
      "alternative_labels": ["Self-serving bias", "Blind spot bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases in others more readily than in oneself, or to believe one is less susceptible to biased reasoning.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "After-action review comparative self-assessment",
      "decision_point_description": "During the after-action review, the participant compared his own watch-phase and evacuation reasoning with the sheriff's watch commander's pushback.",
      "affected_reasoning_operation": "Comparative self-evaluation and attribution of decision quality",
      "bias_specific_mechanism": "Motivated asymmetry in bias detection: the participant endorsed the view that the sheriff's commander let historical pattern cloud his judgment, but resisted applying the same category to his own similar use of track record and best-case prior run.",
      "manifestation_in_interview": "He acknowledges the timing gap looks similar and that he used a best-case prior run, but says 'context matters' and he would 'hesitate to put us in the same category'.",
      "effect_on_reasoning_or_decision": "The participant maintained a favorable assessment of his own decisions and reduced the likelihood that he would fully encode his own comparable pattern as bias.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "People in the room were fairly critical of that, saying he let the historical pattern cloud his judgment on a night when the forecaster was explicitly saying this one was different.",
          "evidence_explanation": "This establishes a readily accepted bias attribution for another person's historical-pattern reliance."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I felt for him, but I also think there's a difference — he was pushing back without really engaging with the forecaster's call, whereas I did hear it and made a judgment based on the full track record we had. My escalation timing and the evacuation plan were built on real experience with that location, so I'd characterize my decisions as sound given what I knew at each point.",
          "evidence_explanation": "The participant frames his own similar track-record reliance as sound judgment and identifies a differentiating factor, despite the earlier evidence that track record outweighed the forecaster's warning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mean, on paper the timing gap looks similar, and I did build the evacuation estimate off a best-case prior run. But I still think context matters — I was managing a lot more moving pieces than he was, so I'd hesitate to put us in the same category.",
          "evidence_explanation": "This is an explicit acknowledgment of similarity followed by resistance to placing himself in the same biased category."
        }
      ],
      "correction_or_counterevidence": "His later advice not to dismiss a forecaster who calls personally shows some insight into the initial watch decision, but it does not directly correct the after-action asymmetry in self-assessment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly supports bias blind spot or self-serving bias; this label rests on general cognitive-science knowledge rather than retrieved corpus evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Some retrieved passages contain OCR errors, and source metadata for the Kinsey document were incomplete.",
    "The bias blind spot finding is low confidence because the participant identifies a possible legitimate distinction between his engagement with the forecaster and the sheriff's watch commander's pushback.",
    "The shelter and mutual aid decision could also reflect ordinary uncertainty or a risk-avoidant preference to wait for firm data, but the explicit statement about leaning on initial assumptions supports an anchoring interpretation."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Biased_3_Sonnet_on",
  "interview_id": "EM_Biased_3",
  "system_prompt_id": "Sonnet",
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
