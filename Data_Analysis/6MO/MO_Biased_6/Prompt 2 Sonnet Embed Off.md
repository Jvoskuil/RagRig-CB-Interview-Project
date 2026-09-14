You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm this is a voluntary conversation about a specific shift you managed, purely to understand your decision-making process. Nothing here is about assigning fault. Are you comfortable with that, and can you tell me your role?

Participant: Sure. I'm the Port Captain — vessel scheduling, pilotage coordination, and final sign-off on berthing and cargo operations when conditions get marginal. Nine years in this role, terminal operations before that.

Interviewer: Great. I'd like you to walk me through a shift that stands out — the one involving the Nordic Star, with the wind system that came through. Can you give me the overall account first, start to finish?

Participant: Sure. We had the Nordic Star scheduled to berth that morning. The plan had been signed off the night before based on a 20-knot forecast, which is well within our normal envelope. When I came in around six, the updated bulletin had gusts revised up to 28, trending toward 32 by afternoon. We also had a hard tidal window closing at two, and the next vessel was booked into that same berth at six that evening, so there wasn't a lot of slack. I looked at the numbers and decided to keep the plan as it was — the shift had already been briefed, tugs were assigned, the pilot was standing by, and reopening it would have meant restructuring the whole day for a bulletin that could easily soften by midday. Around noon it firmed up at 27 knots and climbing, so it wasn't a one-off spike.

The pilotage went ahead early afternoon. Our pilot had done a lot of transits in similar conditions — I want to say 18 of the last 20 in that wind range went through clean. Crane manufacturer envelope allows up to 30 knots sustained, so we still had margin on paper. I've personally taken vessels through worse crosswinds, so between the pilot's numbers and my own read of it, we went ahead as planned rather than pulling in an extra tug or slowing the approach. It got the vessel alongside, but there was a gust right at the final approach that pushed the bow toward the fendering — no contact damage, but it was closer than anyone wanted.

Then we moved into discharge. In the pre-lift meeting I laid out a plan to run the STS cranes at a reduced lift rate given the wind. That got agreed on quickly, no real pushback, and we started. Partway through, a gust spiked hard enough to trip the automatic wind alarm on one crane, so we had to pause. After it reset, the readings were bouncing around 24 knots but not settling, and one of our engineers wanted thirty minutes before restarting. I made the call to resume based on the operators we had on the cranes — very experienced team — and we finished the discharge with only a short delay.

Interviewer: Let's slow down and rebuild that timeline piece by piece. What exactly changed between the evening plan and the six a.m. bulletin?

Participant: The evening plan used a 20-knot forecast. The morning bulletin bumped that to 28 gusting, trending toward 32 later. It wasn't a small revision.

Interviewer: And after the pilotage, what new information came in?

Participant: The near-miss on the fender got logged, and I had a conversation with the pilot afterward about the gust timing on final approach.

Interviewer: What happened structurally after the operations meeting, before the alarm tripped?

Participant: We'd started reduced-rate lifting, everything looked normal for maybe forty minutes, then the spike came through and the crane's own safety system shut it down.

Interviewer: And once it reset?

Participant: Readings were fluctuating in the low-to-mid twenties, not stable, and that's when the engineer flagged waiting.

Interviewer: Let's go back to that first call, keeping the original plan after the six a.m. bulletin. What told you the plan still held?

Participant: Mostly that everything was already in motion — tugs booked, pilot briefed, berth confirmed. The forecast had moved, but forecasts move around this time of year, and 28 with a trend to 32 didn't feel like a different situation than the 20 we'd planned for, more like a variation on it. Reopening the schedule for a bulletin update felt like more disruption than the number justified.

Interviewer: What alternatives did you actually consider at that point?

Participant: I could've asked for a fresh risk assessment, pushed the berthing earlier to beat the trend, or delayed and eaten the tidal window. Delay meant missing the window entirely, and reassessment would've eaten into the same time we needed to berth.

Interviewer: How much of that decision was about the number itself versus the fact the plan already existed?

Participant: Honestly, probably both. But I keep coming back to — it wasn't 40 knots, it was still in the range we'd already built the plan around.

Interviewer: Moving to the pilotage decision. What was the deciding factor there?

Participant: The pilot's track record in that wind band, and the crane envelope still having margin. And frankly, I've been through plenty of crosswind approaches myself over the years, so I had a good feel for what the vessel could handle. The wind we were actually seeing that afternoon was gustier and more variable than what I usually deal with, but since I'd handled worse steady crosswinds before, I didn't think that gustiness changed much about how the approach would go.

Interviewer: Did you weigh the alternative of adding a tug or slowing the approach?

Participant: We talked about it briefly. But with 18 out of 20 similar transits going clean, and my own read of the conditions, it didn't seem necessary to add that complexity.

Interviewer: If someone had put it to you as one in twenty transits having a problem, rather than eighteen out of twenty succeeding, would that have changed anything?

Participant: I don't think I really thought about it that way at the time. Put like that it sounds worse, but it's the same numbers.

Interviewer: Let's talk about the pre-lift meeting. How did the team land on proceeding with reduced-rate lifting?

Participant: I presented the plan, and it was agreed pretty fast. Nobody raised an objection in the room.

Interviewer: Did you learn anything afterward about how people actually felt going in?

Participant: Later on, yeah — I found out two of the supervisors had talked between themselves beforehand and had some reservations about lifting so close to the soft limit. Neither of them said anything when I laid it out.

Interviewer: Any read on why that didn't come up in the meeting itself?

Participant: Hard to say. Maybe they figured I'd already made the call. Maybe they agreed once they heard the reduced-rate plan. It moved quickly either way.

Interviewer: Did either of them say afterward what specifically held them back from raising it in the room?

Participant: One of them mentioned it in passing — once I'd laid out the reduced-rate plan and it got nodded through that fast, it felt like reopening it would mean being the one who stalled the discharge, so they let it go rather than push back.

Interviewer: Last decision point — resuming after the alarm reset. Walk me through that call.

Participant: The engineer wanted thirty minutes to be sure the readings settled. I looked at the crew running the cranes — very capable, some of the most experienced operators we've got — and decided we could resume and they'd manage the fluctuation fine. We also had the next vessel coming in, so there was real pressure to get moving again.

Interviewer: Was there anything in the readings themselves that supported resuming immediately, versus waiting the thirty minutes?

Participant: Not really new data, no. The numbers hadn't stabilized, they were still bouncing. It came down to trusting the operators to handle it.

Interviewer: How confident were you in each of these calls at the time, compared to now?

Participant: At the time, fairly confident — you make these calls constantly and mostly they're fine. Looking back, the fender near-miss and the alarm trip make me want to sit with the numbers a bit longer next time rather than lean so much on how things usually go.

Interviewer: Last couple of hypotheticals. If the six a.m. bulletin had shown 32 knots outright instead of 28 trending toward it, would your first decision have gone differently?

Participant: Probably, yeah. Something clearly outside the range we planned for would've triggered a real reassessment.

Interviewer: And if the supervisor who had reservations had spoken up in that meeting?

Participant: I'd like to think we'd have paused to talk it through properly. It's possible the plan would've held anyway, but at least it would've been tested.

Interviewer: Appreciate you walking through that in detail.

Participant: No problem.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MO_Biased_6",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Port Captain / Terminal Operations Manager",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Gusting Crosswind Berthing and Discharge of MV Nordic Star",
    "scenario_summary_internal": "A Port Captain manages the berthing, pilotage, and STS crane discharge of a container vessel as a forecast wind system deteriorates through the day. Schedule pressure from a tight tidal window and an incoming next vessel push the captain and team toward continuing with the original plan despite escalating wind data, favorable framing of transit risk, quiet team consensus, and confidence in personal and crew capability that outruns the marginal instrument readings. No accident occurs, but a near-miss fender contact and an automatic crane wind-alarm event punctuate the shift, leaving the soundness of the underlying judgments genuinely debatable.",
    "occupational_realism": {
      "objective": "Safely berth MV Nordic Star within its tidal window and complete scheduled STS crane discharge before the berth must be vacated for the next vessel.",
      "setting": "Container terminal Operations Control Center and quayside, single shift from 06:00 morning weather bulletin through afternoon cargo discharge.",
      "constraints": [
        "Tidal window for berthing closes at 14:00",
        "Next vessel scheduled to occupy the same berth at 18:00, creating knock-on schedule pressure",
        "STS crane OEM soft-limit guidance recommends operational review above 25 knots sustained / 32 knots gusting",
        "Only two tugs and one duty pilot available for the shift",
        "Charter party laytime clock is running, creating commercial pressure to avoid delay"
      ],
      "stakeholders": [
        "Port Captain (interviewee)",
        "Duty Pilot",
        "Two Shift Supervisors",
        "Terminal Operations Director",
        "Vessel Master, MV Nordic Star",
        "Junior Operations Engineer (crane systems)",
        "Port Meteorological Service"
      ],
      "technical_terms_to_use": [
        "STS (ship-to-shore) crane",
        "gust factor",
        "wind limit envelope",
        "pilotage",
        "tug assist",
        "berth window",
        "laytime",
        "anemometer reading",
        "bollard pull",
        "wind alarm trip"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "anchoring",
        "framing",
        "groupthink",
        "overconfidence",
        "heuristic",
        "cognitive",
        "status quo"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Berthing plan approved the previous evening based on a 20-knot wind forecast",
          "06:00 weather bulletin revises gusts to 28 knots, trending toward 32 knots by afternoon",
          "Tidal window closes at 14:00; next vessel occupies berth at 18:00"
        ],
        "new_information_after_decision": [
          "By midday, sustained gusts confirmed at 27 knots with a continuing rising trend"
        ],
        "alternatives": [
          "Proceed with the previously published berthing plan unchanged",
          "Request a revised wind risk assessment and consider shifting the berthing window earlier",
          "Delay berthing pending a clearer forecast"
        ],
        "intended_action": "Proceed with the original plan, treating the updated bulletin as within the range already anticipated."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pilot's operational log: 18 of last 20 similar-condition transits completed without incident",
          "STS crane manufacturer envelope allows operations up to 30 knots sustained gusts",
          "Vessel has bow thruster; two tugs available"
        ],
        "new_information_after_decision": [
          "Transit completed but with a near-miss fender contact during final approach due to a gust"
        ],
        "alternatives": [
          "Proceed with pilotage as planned, citing the high historical success rate",
          "Request additional tug support and a reduced speed profile",
          "Postpone the transit until wind eases"
        ],
        "intended_action": "Proceed with pilotage, endorsing the plan based on the favorable success statistic and personal past experience."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "OEM soft-limit guidance recommends pausing for review above 25 knots sustained / 32 knots gusting",
          "Two supervisors privately expressed concern to each other before the meeting",
          "Captain outlines a plan to proceed with a reduced lift rate"
        ],
        "new_information_after_decision": [
          "A gust spike later triggers the automatic crane wind alarm, requiring temporary suspension"
        ],
        "alternatives": [
          "Proceed with reduced-rate lifting as proposed",
          "Pause operations until anemometer readings stabilize",
          "Formally escalate the concern to the Terminal Operations Director for a second opinion"
        ],
        "intended_action": "Team reaches quick unanimous agreement to proceed; meeting closes without recorded objection."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Automatic wind alarm has reset after a brief gust spike",
          "Anemometer shows 24 knots sustained but fluctuating near the alarm threshold",
          "Junior operations engineer recommends waiting 30 minutes for confirmed stabilization",
          "Next vessel's imminent arrival creates renewed schedule pressure"
        ],
        "new_information_after_decision": [
          "Cargo discharge completes with only a minor delay and no further alarm trips"
        ],
        "alternatives": [
          "Resume immediately, trusting crane operators to manage fluctuating winds",
          "Wait for the stabilization window recommended by the engineer",
          "Request updated meteorological confirmation before resuming"
        ],
        "intended_action": "Resume immediately, citing confidence in operator skill despite fluctuating readings."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were responsible for on this shift.",
        "What was the operational objective when the shift began?"
      ],
      "timeline_reconstruction": [
        "What did the 06:00 weather bulletin show compared to the previous evening's plan?",
        "What happened during the pilotage of MV Nordic Star?",
        "What was discussed in the operations meeting before discharge began?",
        "What happened after the wind alarm tripped?"
      ],
      "decision_point_probes": [
        "What cues told you the original plan still made sense (or didn't)?",
        "What information sources did you rely on at each point, and how much weight did you give each?",
        "What goals were you weighing against each other?",
        "What alternatives did you consider, and why did you rule them out?",
        "What was the basis for your final call at each stage?",
        "How did your past experience with similar wind conditions shape your thinking?",
        "How much time pressure did you feel, and how did that affect the decision?",
        "How confident were you in your assessment at the time, versus in hindsight?",
        "What was still uncertain when you made the call?"
      ],
      "closing_hypotheticals": [
        "If the 06:00 bulletin had shown 32 knots instead of 28, would your initial decision have changed?",
        "If the pilot had framed the transit as a '1 in 20 chance of incident,' would you have proceeded the same way?",
        "If a supervisor had voiced an objection in the meeting, do you think the outcome would have changed?",
        "If the junior engineer's 30-minute wait had been enforced, what do you think would have been different?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Status Quo Bias",
        "decision_point": 1,
        "mechanism": "Preference for retaining the pre-existing, already-approved berthing plan despite updated wind information that would normally warrant reassessment.",
        "affected_reasoning_operation": "Plan revision / threshold for triggering re-evaluation",
        "evidence_available_at_time": [
          "Previous evening's 20-knot forecast and approved plan",
          "06:00 bulletin showing rising trend to 28 knots"
        ],
        "required_textual_manifestation": "Captain notes the plan was 'already agreed' and sees no reason to reopen it, treating the new bulletin as not warranting a fresh review.",
        "plausible_nonbias_interpretation": "A reasonable operational preference for stability, avoiding unnecessary disruption until a clearer confirmed trend emerges.",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo", "resistance to change", "default option"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Continued reference to the original 20-knot figure when interpreting the significance of the new 28-32 knot bulletin, insufficiently adjusting the risk estimate.",
        "affected_reasoning_operation": "Numerical risk estimation and updating in light of new evidence",
        "evidence_available_at_time": [
          "Initial planning forecast of 20 knots",
          "Updated bulletin trending 28 to 32 knots"
        ],
        "required_textual_manifestation": "Captain frames the new reading relative to the original number ('still not far off what we planned for') rather than evaluating it on its own terms.",
        "plausible_nonbias_interpretation": "Cautious, incremental interpretation of a single updated bulletin pending confirmation of the trend.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "initial estimate bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Framing Bias",
        "decision_point": 2,
        "mechanism": "Risk information presented and accepted in a positively framed form ('95% of similar transits succeed') rather than an equivalent negative frame, shifting the decision toward proceeding.",
        "affected_reasoning_operation": "Risk evaluation from a probabilistic statement",
        "evidence_available_at_time": [
          "Pilot's log showing 18 of 20 prior similar transits succeeded"
        ],
        "required_textual_manifestation": "Captain repeats and leans on the success-rate phrasing as the central justification for proceeding, without independently restating the failure rate.",
        "plausible_nonbias_interpretation": "Reasonably trusting an experienced pilot's aggregated operational data.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "positive frame", "negative frame"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Overconfidence Bias",
        "decision_point": 2,
        "mechanism": "Excessive confidence in personal past experience handling similar wind conditions, overriding the need for added margin (extra tug, reduced speed).",
        "affected_reasoning_operation": "Self-assessed capability judgment used to justify proceeding",
        "evidence_available_at_time": [
          "Captain's personal recollection of past similar transits"
        ],
        "required_textual_manifestation": "Captain states something like 'I've handled winds like this dozens of times, I know how the vessel will behave,' offered as sufficient justification without acknowledging residual uncertainty.",
        "plausible_nonbias_interpretation": "Legitimate expertise reasonably informing judgment under uncertainty.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence", "miscalibration"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "Team converges quickly on the captain's proposed plan without surfacing pre-existing private reservations, prioritizing apparent consensus over voiced dissent.",
        "affected_reasoning_operation": "Collective judgment aggregation and suppression of dissent",
        "evidence_available_at_time": [
          "Two supervisors' private concerns expressed to each other before the meeting",
          "Rapid, unopposed agreement in the meeting itself"
        ],
        "required_textual_manifestation": "Captain recalls 'everyone was on board, nobody objected,' while the narrative separately reveals supervisors had reservations they did not raise in the room.",
        "plausible_nonbias_interpretation": "Genuine shared professional confidence producing fast, real agreement.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "consensus pressure", "dissent suppression"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Overestimation of the crane operators' collective ability to manage fluctuating, near-threshold wind readings immediately after an alarm event, dismissing a cautious wait recommendation.",
        "affected_reasoning_operation": "Predictive judgment about team/operator performance under uncertainty",
        "evidence_available_at_time": [
          "Junior engineer's recommendation to wait 30 minutes",
          "Fluctuating anemometer readings near the alarm threshold"
        ],
        "required_textual_manifestation": "Captain justifies immediate resumption by citing confidence in the operators' skill, without citing new confirming data to counter the engineer's caution.",
        "plausible_nonbias_interpretation": "Operators may genuinely be skilled enough that the extra wait was unnecessary given marginal readings.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence", "team competence bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition and no paired control is specified in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable for this biased-condition generation task.",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Exactly 6 total bias instances planned across 5 named biases, matching the manifest",
      "Exactly 4 decision points, each with at least two plausible alternatives",
      "No decision point contains more than two instances of the same bias",
      "cb_01 and cb_02 share decision point 1 but use distinct evidence sources (approved plan vs. numeric forecast) and distinct reasoning operations",
      "cb_04 and cb_06 are both Overconfidence Bias but differ in decision point, evidence source, and target of confidence (self vs. team)",
      "No bias term, definition, or explicit psychological label appears in probe or timeline text intended for the public interview",
      "Consequences (near-miss, alarm trip, minor delay) do not conclusively prove any decision was biased",
      "Target interview length 1,350 words (acceptable 1,215-1,485) is achievable given 4 decision points with concise probe-driven answers"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Status Quo Bias", "occurrences": 1, "mechanism_constraint": "Retention of pre-approved berthing plan despite updated wind bulletin" },
      { "bias": "Framing Bias", "occurrences": 1, "mechanism_constraint": "Acceptance of positively framed success-rate statistic over equivalent negative frame" },
      { "bias": "Groupthink", "occurrences": 1, "mechanism_constraint": "Rapid unopposed team consensus despite pre-existing private dissent" },
      { "bias": "Overconfidence Bias", "occurrences": 2, "mechanism_constraint": "One instance self-referential (personal experience), one instance team-referential (operator competence judgment), at distinct decision points" },
      { "bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "Insufficient adjustment away from initial 20-knot forecast figure" }
    ],
    "target_bias_names": ["Status Quo Bias", "Framing Bias", "Groupthink", "Overconfidence Bias", "Anchoring Bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Status Quo Bias", "requested_occurrences": 1 },
      { "bias": "Framing Bias", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 2 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias" },
      { "instance_id": "cb_02", "bias": "Anchoring Bias" },
      { "instance_id": "cb_03", "bias": "Framing Bias" },
      { "instance_id": "cb_04", "bias": "Overconfidence Bias" },
      { "instance_id": "cb_05", "bias": "Groupthink" },
      { "instance_id": "cb_06", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "cb_03", "bias": "Framing Bias", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Overconfidence Bias", "decision_point": 2 },
      { "instance_id": "cb_05", "bias": "Groupthink", "decision_point": 3 },
      { "instance_id": "cb_06", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Status Quo Bias",
        "mechanism": "Preference for retaining the pre-approved plan despite updated risk information",
        "affected_reasoning_operation": "Plan revision threshold",
        "evidence_source": "Prior-evening approved plan vs. 06:00 bulletin",
        "distinctiveness_requirement": "Distinguished from cb_02 by concerning whether to reopen the plan at all, not the numerical interpretation of the wind figure"
      },
      {
        "instance_id": "cb_02",
        "bias": "Anchoring Bias",
        "mechanism": "Insufficient adjustment of risk estimate away from the original 20-knot figure",
        "affected_reasoning_operation": "Numerical risk updating",
        "evidence_source": "Original 20-knot forecast vs. updated 28-32 knot bulletin",
        "distinctiveness_requirement": "Distinguished from cb_01 by focusing on the numeric anchor used in risk estimation rather than the decision to keep the existing plan"
      },
      {
        "instance_id": "cb_03",
        "bias": "Framing Bias",
        "mechanism": "Acceptance of a positively framed success statistic driving the transit decision",
        "affected_reasoning_operation": "Risk evaluation from probabilistic statement",
        "evidence_source": "Pilot's log of prior transit success rate",
        "distinctiveness_requirement": "Distinguished from cb_04 by being about how the statistic was presented/received, not about the captain's own experiential confidence"
      },
      {
        "instance_id": "cb_04",
        "bias": "Overconfidence Bias",
        "mechanism": "Excessive confidence in personal past experience with similar wind conditions",
        "affected_reasoning_operation": "Self-assessed capability judgment",
        "evidence_source": "Captain's own recollection of prior similar transits",
        "distinctiveness_requirement": "Distinguished from cb_06 by being self-referential and occurring at the pilotage decision, not the post-alarm resumption decision"
      },
      {
        "instance_id": "cb_05",
        "bias": "Groupthink",
        "mechanism": "Rapid unopposed consensus despite pre-existing unvoiced supervisor concerns",
        "affected_reasoning_operation": "Collective judgment aggregation / dissent suppression",
        "evidence_source": "Supervisors' private pre-meeting concerns vs. meeting outcome",
        "distinctiveness_requirement": "Sole groupthink instance; no repetition elsewhere in the interview"
      },
      {
        "instance_id": "cb_06",
        "bias": "Overconfidence Bias",
        "mechanism": "Overestimation of crane operators' ability to manage fluctuating near-threshold readings",
        "affected_reasoning_operation": "Predictive judgment about team performance under uncertainty",
        "evidence_source": "Junior engineer's wait recommendation vs. fluctuating anemometer readings",
        "distinctiveness_requirement": "Distinguished from cb_04 by being team-referential and occurring at the post-alarm resumption decision, not the pilotage decision"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Framing Bias", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Overconfidence Bias", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "cb_06", "bias": "Overconfidence Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MO_Biased_6",
    "domain_id": "MO",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across all 4 decision points, prioritizing mechanism fit and narrative realism: decision point 1 carries Status Quo and Anchoring (distinct evidence sources and reasoning operations); decision point 2 carries Framing and one Overconfidence instance (distinct mechanisms: statistic framing vs. self-experience); decision point 3 carries the sole Groupthink instance; decision point 4 carries the second Overconfidence instance (team-referential, distinct from decision point 2's self-referential instance). No decision point exceeds two instances of the same bias.",
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
        "segment_type": "initial plan-retention rationale",
        "raw_interview_anchor": "I looked at the numbers and decided to keep the plan as it was — the shift had already been briefed, tugs were assigned, the pilot was standing by, and reopening it would have meant restructuring the whole day for a bulletin that could easily soften by midday.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The pre-approved plan and its prior commitments dominated the response to materially worsened wind information; this is the hidden plan-retention instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial pilotage statistic rationale",
        "raw_interview_anchor": "Our pilot had done a lot of transits in similar conditions — I want to say 18 of the last 20 in that wind range went through clean. Crane manufacturer envelope allows up to 30 knots sustained, so we still had margin on paper.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The favorable success-rate presentation is part of the decision basis for proceeding, matching the hidden positive-frame instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "initial self-experience rationale",
        "raw_interview_anchor": "I've personally taken vessels through worse crosswinds, so between the pilot's numbers and my own read of it, we went ahead as planned rather than pulling in an extra tug or slowing the approach.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "Personal past experience is used to support proceeding without added margin, matching the self-referential overconfidence instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "pre-lift consensus report",
        "raw_interview_anchor": "In the pre-lift meeting I laid out a plan to run the STS cranes at a reduced lift rate given the wind. That got agreed on quickly, no real pushback, and we started.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_05"
        ],
        "ground_truth_rationale": "Rapid unopposed agreement is one part of the groupthink instance; the later report establishes that reservations already existed."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "initial post-alarm restart rationale",
        "raw_interview_anchor": "After it reset, the readings were bouncing around 24 knots but not settling, and one of our engineers wanted thirty minutes before restarting. I made the call to resume based on the operators we had on the cranes — very experienced team.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_06"
        ],
        "ground_truth_rationale": "The captain favors immediate restart based on operator capability despite unstable readings and a wait recommendation, matching the team-referential overconfidence instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "plan-revision reasoning",
        "raw_interview_anchor": "Mostly that everything was already in motion — tugs booked, pilot briefed, berth confirmed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "Prior commitments and the existing plan are explicitly treated as reasons against reopening the plan."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "numeric forecast updating",
        "raw_interview_anchor": "The forecast had moved, but forecasts move around this time of year, and 28 with a trend to 32 didn't feel like a different situation than the 20 we'd planned for, more like a variation on it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "The new forecast is evaluated relative to the initial 20-knot figure rather than independently, matching the hidden anchoring instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "alternative and constraint assessment",
        "raw_interview_anchor": "I could've asked for a fresh risk assessment, pushed the berthing earlier to beat the trend, or delayed and eaten the tidal window. Delay meant missing the window entirely, and reassessment would've eaten into the same time we needed to berth.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant weighs operational alternatives and timing constraints; no hidden bias mechanism is manifested in this span."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "plan-range rationale",
        "raw_interview_anchor": "Honestly, probably both. But I keep coming back to — it wasn't 40 knots, it was still in the range we'd already built the plan around.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The existing plan's range remains the basis for retaining it after the update, a repeated manifestation of the plan-retention instance."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "self-experience comparison",
        "raw_interview_anchor": "The wind we were actually seeing that afternoon was gustier and more variable than what I usually deal with, but since I'd handled worse steady crosswinds before, I didn't think that gustiness changed much about how the approach would go.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "The captain discounts a relevant difference in current conditions based on confidence from personal experience, matching the self-referential overconfidence instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "pilot success-rate decision rationale",
        "raw_interview_anchor": "We talked about it briefly. But with 18 out of 20 similar transits going clean, and my own read of the conditions, it didn't seem necessary to add that complexity.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The positive success-rate form is explicitly used to reject additional tug or speed margin, matching the hidden framing instance."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "speculative explanation of silence",
        "raw_interview_anchor": "Hard to say. Maybe they figured I'd already made the call. Maybe they agreed once they heard the reduced-rate plan. It moved quickly either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an uncertain retrospective explanation, not itself evidence that a bias mechanism was adopted."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "withheld dissent mechanism",
        "raw_interview_anchor": "One of them mentioned it in passing — once I'd laid out the reduced-rate plan and it got nodded through that fast, it felt like reopening it would mean being the one who stalled the discharge, so they let it go rather than push back.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_05"
        ],
        "ground_truth_rationale": "A supervisor's pre-existing concern was withheld because challenging apparent consensus carried a social and operational cost, matching the hidden groupthink instance."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "post-alarm operator-confidence rationale",
        "raw_interview_anchor": "The engineer wanted thirty minutes to be sure the readings settled. I looked at the crew running the cranes — very capable, some of the most experienced operators we've got — and decided we could resume and they'd manage the fluctuation fine. We also had the next vessel coming in, so there was real pressure to get moving again.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_06"
        ],
        "ground_truth_rationale": "The captain predicts the operators can manage near-threshold fluctuation and discounts the engineer's wait recommendation, matching the hidden team-referential overconfidence instance."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "no-new-data restart justification",
        "raw_interview_anchor": "Not really new data, no. The numbers hadn't stabilized, they were still bouncing. It came down to trusting the operators to handle it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_06"
        ],
        "ground_truth_rationale": "The captain confirms no new stabilizing evidence and rests the restart decision on trust in operator performance, matching the same hidden instance."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "hindsight reflection",
        "raw_interview_anchor": "At the time, fairly confident — you make these calls constantly and mostly they're fine. Looking back, the fender near-miss and the alarm trip make me want to sit with the numbers a bit longer next time rather than lean so much on how things usually go.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is hindsight learning after consequences and is not a separate hidden in-time bias instance."
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
    "analysis_scope_note": "No retrieved corpus passages were supplied; bias labels and mechanisms are based on established cognitive-science concepts applied to transcript evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "groupthink",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring effect",
      "alternative_labels": ["anchoring and adjustment heuristic", "reference dependence"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias where an initial value or reference point exerts disproportionate influence on later judgments, leading to insufficient adjustment.",
      "attributed_to_speaker": "Participant (Port Captain)",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting the 06:00 wind forecast update",
      "decision_point_description": "After receiving the updated 28-gusting-32 forecast, judging whether the new numbers represented a meaningful departure from the 20-knot plan.",
      "affected_reasoning_operation": "Risk perception and forecast interpretation",
      "bias_specific_mechanism": "The original 20-knot plan/forecast served as an anchor, so the participant interpreted the revised 28-32 knot figures as a variation of the original plan rather than a meaningfully different risk sign.",
      "manifestation_in_interview": "The participant frames the increased wind as not a different situation but more like a variation, and later says it was still in the range they had already built the plan around, even though he admits the revision was not small.",
      "effect_on_reasoning_or_decision": "Reduced the perceived severity of the forecast change and contributed to proceeding without a fresh risk assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The evening plan used a 20-knot forecast. The morning bulletin bumped that to 28 gusting, trending toward 32 later. It wasn't a small revision.",
          "evidence_explanation": "Confirms the original reference point and that the change was materially significant, making the later assimilation to the original plan diagnostic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The forecast had moved, but forecasts move around this time of year, and 28 with a trend to 32 didn't feel like a different situation than the 20 we'd planned for, more like a variation on it.",
          "evidence_explanation": "Directly demonstrates insufficient adjustment from the original 20-knot reference point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, probably both. But I keep coming back to — it wasn't 40 knots, it was still in the range we'd already built the plan around.",
          "evidence_explanation": "Evaluates the updated forecast against the original plan's category rather than fully reassessing its trend."
        }
      ],
      "correction_or_counterevidence": "The participant did name alternatives and said an outright 32-knot bulletin would probably have triggered a real reassessment, suggesting some sensitivity to a more extreme departure from the anchor.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "status quo bias",
      "alternative_labels": ["plan continuation bias", "default bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for the current state of affairs, with change from an existing plan perceived as more costly or risky than is warranted.",
      "attributed_to_speaker": "Participant (Port Captain)",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Choosing to retain the original berthing plan",
      "decision_point_description": "After the updated forecast, deciding whether to keep the original plan or reopen the schedule and risk assessment.",
      "affected_reasoning_operation": "Plan continuation decision",
      "bias_specific_mechanism": "The already-mobilized plan was treated as the default, and departing from it was framed mainly as costly disruption rather than weighed against the increased wind risk.",
      "manifestation_in_interview": "The participant repeatedly emphasizes that the plan was already in motion and that reopening it would disrupt the day, treating the forecast change as insufficient to justify that disruption.",
      "effect_on_reasoning_or_decision": "He kept the original plan despite the revised forecast and hard tidal window, moving directly toward pilotage.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly that everything was already in motion — tugs booked, pilot briefed, berth confirmed. The forecast had moved, but forecasts move around this time of year, and 28 with a trend to 32 didn't feel like a different situation than the 20 we'd planned for, more like a variation on it. Reopening the schedule for a bulletin update felt like more disruption than the number justified.",
          "evidence_explanation": "Shows the existing plan was treated as the default and change was evaluated primarily as disruption."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I could've asked for a fresh risk assessment, pushed the berthing earlier to beat the trend, or delayed and eaten the tidal window. Delay meant missing the window entirely, and reassessment would've eaten into the same time we needed to berth.",
          "evidence_explanation": "Alternatives were framed mainly in terms of cost to the current plan rather than updated risk."
        }
      ],
      "correction_or_counterevidence": "The participant considered specific alternatives and said an outright 32-knot forecast would probably have triggered a reassessment, indicating the status quo preference was not absolute.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["overconfidence effect", "representativeness heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging likelihood by how easily salient instances come to mind rather than by relevant base rates or current conditions.",
      "attributed_to_speaker": "Participant (Port Captain)",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pilotage go/no-go under gusty crosswind",
      "decision_point_description": "Deciding whether to proceed with pilotage as planned, add an extra tug, or slow the approach.",
      "affected_reasoning_operation": "Risk judgment and probability of incident",
      "bias_specific_mechanism": "The participant relied on the availability of the pilot's 18/20 clean transits and his own memorable past success in worse steady crosswinds, while discounting the current gust variability he explicitly acknowledged.",
      "manifestation_in_interview": "He noted the current wind was gustier and more variable than his prior experience, but concluded that because he had handled worse steady crosswinds, gustiness would not change the approach.",
      "effect_on_reasoning_or_decision": "He proceeded without adding an extra tug or slowing the approach; the final approach produced a near-miss at the fendering.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The pilot's track record in that wind band, and the crane envelope still having margin. And frankly, I've been through plenty of crosswind approaches myself over the years, so I had a good feel for what the vessel could handle. The wind we were actually seeing that afternoon was gustier and more variable than what I usually deal with, but since I'd handled worse steady crosswinds before, I didn't think that gustiness changed much about how the approach would go.",
          "evidence_explanation": "Directly demonstrates use of salient prior instances to discount currently observed gust variability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We talked about it briefly. But with 18 out of 20 similar transits going clean, and my own read of the conditions, it didn't seem necessary to add that complexity.",
          "evidence_explanation": "Shows statistically thin but salient success instances drove the no-added-tug decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I don't think I really thought about it that way at the time. Put like that it sounds worse, but it's the same numbers.",
          "evidence_explanation": "Reveals he had not adopted a formal risk/failure framing, consistent with instance-based intuitive reuse."
        }
      ],
      "correction_or_counterevidence": "The pilot's success rate and crane envelope margin were legitimate operational inputs; the retrospective acknowledgment that the one-in-twenty framing sounds worse is a partial recognition, not an in-the-moment correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "groupthink",
      "alternative_labels": ["self-censorship", "illusion of unanimity", "false consensus effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A group decision-making pattern in which the desire for cohesion or unanimity leads to suppression of dissent and insufficient appraisal of alternatives.",
      "attributed_to_speaker": "Two supervisors at the pre-lift meeting (reported by Participant)",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Supervisors withholding reservations during reduced-rate lifting plan",
      "decision_point_description": "During the pre-lift meeting when the reduced-rate lifting plan was presented and quickly accepted.",
      "affected_reasoning_operation": "Dissent expression and group communication",
      "bias_specific_mechanism": "Self-censorship driven by perceived rapid consensus; one supervisor felt that reopening after the plan was nodded through would make him the person stalling discharge.",
      "manifestation_in_interview": "No objections were raised in the room despite private prior reservations; the participant only later learned of the reservations.",
      "effect_on_reasoning_or_decision": "Reservations about lifting near the soft limit were not raised, so the plan was adopted quickly without testing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I presented the plan, and it was agreed pretty fast. Nobody raised an objection in the room.",
          "evidence_explanation": "Establishes the surface appearance of unanimity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Later on, yeah — I found out two of the supervisors had talked between themselves beforehand and had some reservations about lifting so close to the soft limit. Neither of them said anything when I laid it out.",
          "evidence_explanation": "Shows disagreement existed but was not voiced."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "One of them mentioned it in passing — once I'd laid out the reduced-rate plan and it got nodded through that fast, it felt like reopening it would mean being the one who stalled the discharge, so they let it go rather than push back.",
          "evidence_explanation": "Direct mechanism of self-censorship under perceived group consensus and social cost."
        }
      ],
      "correction_or_counterevidence": "No immediate correction occurred in the meeting; the participant learned afterward and reflected that a voiced dissent might have prompted a fuller discussion.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "halo effect",
      "alternative_labels": ["overconfidence effect", "expertise heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias where a general positive impression of a person or group influences judgments about their specific abilities in an unrelated or only loosely related domain.",
      "attributed_to_speaker": "Participant (Port Captain)",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Resuming crane operations after wind alarm reset",
      "decision_point_description": "After the automatic alarm reset with unstable 24-knot readings, deciding whether to resume immediately or wait 30 minutes as the engineer suggested.",
      "affected_reasoning_operation": "Prediction of operator performance under unstable conditions",
      "bias_specific_mechanism": "The participant inferred that because crane operators were very capable and some of the most experienced, they would manage current unpredictable fluctuations despite no new stabilizing data and the engineer's caution.",
      "manifestation_in_interview": "He explicitly says there was no new data and the numbers had not stabilized; the decision came down to trusting operator experience.",
      "effect_on_reasoning_or_decision": "He resumed immediately instead of waiting, completing discharge with only a short delay but under conditions the engineer had flagged.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The engineer wanted thirty minutes to be sure the readings settled. I looked at the crew running the cranes — very capable, some of the most experienced operators we've got — and decided we could resume and they'd manage the fluctuation fine.",
          "evidence_explanation": "Shows a global evaluation of operator quality used to resolve a specific fluctuating-wind safety judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really new data, no. The numbers hadn't stabilized, they were still bouncing. It came down to trusting the operators to handle it.",
          "evidence_explanation": "Confirms the decision was based on trait-like trust rather than changed condition data."
        }
      ],
      "correction_or_counterevidence": "Operator experience may be a legitimate operational consideration, and pressure from the next vessel was also present; this competing explanation lowers confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided, so corpus evidence is unavailable and labels rely on general cognitive-science knowledge.",
    "The supervisor/groupthink occurrence is based on participant-reported secondhand information rather than the supervisors' own speech.",
    "The halo-effect occurrence is lower confidence because experience-based trust can also be a legitimate operational judgment."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Biased_6_Sonnet_off",
  "interview_id": "MO_Biased_6",
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
