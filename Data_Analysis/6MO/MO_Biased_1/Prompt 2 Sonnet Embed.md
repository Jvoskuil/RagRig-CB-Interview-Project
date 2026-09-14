You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable having this conversation recorded and used for training analysis purposes only, no names attached to the write-up.

Participant: Yeah, that's fine, I've done these debriefs before.

Interviewer: Great. Can you tell me a bit about your background as a harbor pilot?

Participant: Sixteen years piloting on this river system, mostly deep-draft container and bulk carriers. I've taken vessels the size of the Kalliopi up to Berth 7 probably a hundred times.

Interviewer: Let's talk about this particular transit. Can you walk me through what you knew before you even boarded?

Participant: Sure. It was a fully loaded container ship, about 300 meters, drawing 14.2 meters. Port control had sent over the passage plan that morning built around the tide table, which gave us roughly 1.2 meters of under-keel clearance at our planned transit time. That's tight, but it's within what we consider workable for that stretch. We had a closing tidal window, maybe ninety minutes to get up to the berth before the margin got too thin. Two tugs were assigned, wind was forecast around 15 knots picking up through the afternoon.

Interviewer: What made this one feel nonroutine compared to a typical run up that channel?

Participant: A few things stacked up. There was a barge moored tighter to the bend than charted, one of our tugs got delayed at the pilot station, and the wind ended up running a bit hotter than forecast. None of those alone would worry me much, but together they made it a transit where I was managing multiple moving pieces instead of just following the plan.

Interviewer: Let's reconstruct the sequence. What happened right after you boarded?

Participant: I went up to the conning position, confirmed the passage plan with the master, checked the draft survey again, and we started the transit close to the planned time. Not long after we got underway, an outbound pilot radioed in a fresh echo sounder sweep from near kilometer four, saying he was seeing less water than expected there, something closer to 0.7 meters of clearance instead of the 1.2 we'd planned around. Around the same time, VTS mentioned the tide gauge was reading a slightly slower rise than the table predicted.

Interviewer: How did that develop as you continued?

Participant: We kept going. Then approaching the bend, VTS told us the barge hadn't moved despite requests, so I had to adjust our track. After that, the wind picked up faster than forecast right as we were down to one tug made fast, with the second one still twenty minutes out. Near the berth, a cross-current pushed us off line during the final approach, and we had to correct with the tugs we had by then.

Interviewer: Let's go through each of those in turn. Starting with the clearance question after the outbound pilot's report — what were you weighing at that moment?

Participant: I had the morning tide table figure in hand, which I trust because it comes from the same source we use every day and it's usually solid. Then I had this one radio report from another pilot's sounding. My read was that a single sweep from someone else's vessel isn't necessarily apples to apples with our draft and trim, so I didn't see it as something that overrode the passage plan. The tide gauge lag was a few centimeters, not dramatic on its own.

Interviewer: What alternatives did you actually consider there?

Participant: Delaying about forty minutes to let the tide build more before we hit that stretch, or slowing down and shifting toward the deeper side of the channel. Both were on the table. I chose to hold our timing and proceed as planned, treating the 1.2 as still the number that mattered.

Interviewer: What made you settle on that instead of recalculating with the new sounding and the slower tide rise together?

Participant: Honestly, the original number felt like the anchor point for the whole plan, it had already been checked by port control, and one radio call didn't feel like enough to unwind that. In hindsight I probably could have asked for a second sounding or run our own check before committing, but at the time it felt like the tide table was the more reliable reference.

Interviewer: How confident were you in that judgment in the moment?

Participant: Reasonably confident, maybe seven out of ten. Not fully certain, but confident enough not to change course.

Interviewer: Moving to the barge near the bend — what options did you weigh there?

Participant: I could push VTS harder for an emergency move, slow down and favor the wider side, or hold position until it cleared. I went with slowing down and shifting track because waiting would have eaten into our tidal window, and pushing VTS wasn't going to get the barge moved fast enough anyway.

Interviewer: How much time did you have to decide?

Participant: A couple of minutes, maybe less. Enough to make a deliberate call but not to sit and debate it.

Interviewer: Next, the tug situation with rising wind. What was going through your mind?

Participant: With only one tug fast and the second still well out, and gusts running above forecast, I didn't like relying purely on the bow thruster given our draft. When I heard a harbor tug not originally assigned was nearby, I asked for that one instead of waiting on our delayed second tug. It came down to getting extra help sooner rather than sticking with the original assignment.

Interviewer: Was there a moment you considered just waiting it out?

Participant: Briefly, yes. But wind was trending the wrong direction, and I'd rather bring in help early than get caught short later.

Interviewer: And the final approach, with the cross-current pushing you off line?

Participant: By then we had both tugs fast. I chose a graduated correction rather than aborting, applying tug and thruster power progressively and watching how she responded. Aborting and circling was an option, but I judged we had enough room and control authority to correct in place.

Interviewer: What made continuing feel safer than aborting?

Participant: The response to the first pushes of tug power told me we had steerage and margin. If that correction hadn't taken hold quickly, I would have aborted. It ended up tighter to the neighboring berth than I'd like, but within what the berth operator confirmed was workable for mooring.

Interviewer: Looking back at the whole transit, if the echo sounder report had reached you before you left the pilot station instead of mid-transit, would your timing decision have gone differently?

Participant: Possibly. Getting it earlier, alongside the tide gauge lag, together rather than as two separate small inputs, might have pushed me toward the delay option. Mid-transit, each piece came in isolated and didn't feel like enough on its own to override a plan that was already running.

Interviewer: If the second tug had arrived on schedule, would the bend or berthing approach have gone differently?

Participant: The bend, not much, that was really about the barge and speed. The berthing correction might have felt less tight, since we'd have had both tugs earlier rather than picking up the harbor tug as a stand-in.

Interviewer: Is there a point where, in retrospect, you might have weighted new information more heavily?

Participant: Probably the clearance question early on. I leaned on the original figure because it had already been vetted, and I discounted the fresh sounding a bit more than I probably should have.

Interviewer: What would you tell a less experienced pilot to watch for in a transit like this?

Participant: Don't let the plan you walked in with carry more weight just because it came first. New readings, even partial ones, deserve a real second look, not just a quick mental check against what you already believe.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "MO_Biased_1",
    "domain_id": "MO",
    "domain": "Maritime Operations",
    "role": "Harbor Pilot / Marine Pilot",
    "condition": "biased",
    "generation_specification": {
      "scenario_title_internal": "The Falling Tide: Piloting MV Kalliopi to Berth 7",
      "scenario_summary_internal": "A harbor pilot boards a fully laden container vessel for a time-critical river transit during a narrowing tidal window. A pre-boarding tide-table estimate of under-keel clearance is treated as fixed truth even after fresher, more direct sounding data becomes available, subtly distorting the pilot's risk recalculation at the first decision point. Three further decision points (channel obstruction, tug shortage under rising wind, and a cross-current berthing approach) proceed as realistic, non-biased professional judgment calls, giving the interview narrative depth without adding further intended bias instances.",
      "occupational_realism": {
        "objective": "Safely pilot the fully loaded 300m container vessel MV Kalliopi up a dredged river channel and berth her at Berth 7 within a closing tidal window, without grounding, collision, or missing the berth slot.",
        "setting": "A single-channel river approach to a major European container terminal, falling tide, moderate wind rising through the transit, one moored barge partially encroaching the channel near a bend, two tugs assigned with one delayed at the pilot station.",
        "constraints": [
          "Fully loaded draft of 14.2m against a channel with historically tight under-keel clearance (UKC)",
          "Tidal window for safe transit closing within roughly 90 minutes",
          "Only one tug immediately available; second tug delayed 20-30 minutes",
          "Bow thruster effectiveness reduced due to deep draft",
          "VTS and berth operator expecting on-schedule arrival to avoid missing the berth slot",
          "Rising wind forecast (15 kt gusting higher) during the transit window"
        ],
        "stakeholders": [
          "Harbor Pilot (interviewee)",
          "Vessel Master",
          "Vessel Traffic Service (VTS) controller",
          "Tug captains",
          "Berth/terminal operator",
          "Outbound pilot who provided the real-time sounding report"
        ],
        "technical_terms_to_use": [
          "under-keel clearance (UKC)",
          "tide table / tidal window",
          "echo sounder sweep",
          "squat effect",
          "conning position",
          "VTS clearance",
          "bow thruster",
          "tug made fast",
          "set and drift",
          "passage plan"
        ],
        "technical_terms_to_avoid": [
          "anchoring bias",
          "cognitive bias",
          "heuristic",
          "confirmation bias",
          "psychological priming"
        ],
        "constraints_note": "No excluded themes specified; standard maritime pilotage vocabulary applies throughout."
      },
      "timeline": [
        {
          "phase": 1,
          "decision_point": true,
          "facts_available_before_decision": [
            "Pre-arrival tide table figure emailed by port control giving predicted UKC of 1.2m at planned transit time",
            "Vessel's static draft survey confirming 14.2m loaded draft",
            "Standard passage plan built around the 1.2m UKC figure and a fixed transit start time"
          ],
          "new_information_after_decision": [
            "An outbound pilot's real-time echo sounder sweep near km 4 of the channel reports shoaling reducing actual clearance to approximately 0.7m",
            "Updated tide gauge readings show the tide rising more slowly than the table predicted"
          ],
          "alternatives": [
            "Proceed on the original schedule, treating the tide-table UKC figure as the controlling number",
            "Delay departure roughly 40 minutes to allow the tide to rise further before entering the shoal area",
            "Reduce transit speed and take a slightly longer route favoring the deeper side of the channel"
          ],
          "intended_action": "The pilot proceeds on the original transit timing, referencing the earlier tide-table figure as reassurance and treating the new sounding report as likely conservative or not directly comparable, without recalculating the margin using the updated data."
        },
        {
          "phase": 2,
          "decision_point": true,
          "facts_available_before_decision": [
            "A barge is moored closer to the channel bend than charted, narrowing the safe passing width",
            "VTS reports the barge operator is slow to respond to move requests",
            "Vessel speed at the bend affects steering response and squat"
          ],
          "new_information_after_decision": [
            "The barge shifts slightly further into the channel due to wake from a passing workboat",
            "VTS confirms no other vessel traffic is currently approaching from downstream"
          ],
          "alternatives": [
            "Request VTS coordinate an emergency shift of the barge before proceeding",
            "Reduce speed and favor the opposite bank with a wider passing margin",
            "Hold position briefly until the barge situation is confirmed resolved"
          ],
          "intended_action": "The pilot reduces speed and adjusts the vessel's track to favor the wider side of the bend, reassessing continuously as new width and current information arrives."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "Wind has increased to 15 kt gusting higher than forecast",
            "Only one tug is currently made fast; the second tug is still 20 minutes out",
            "The vessel's limited bow thruster effectiveness at this draft"
          ],
          "new_information_after_decision": [
            "A harbor tug not originally assigned becomes available nearby and can assist sooner than the delayed second tug",
            "Gust strength briefly exceeds initial forecast during the approach"
          ],
          "alternatives": [
            "Proceed toward the berth with only one tug made fast, relying on thruster and rudder",
            "Wait at a safe holding position for the second assigned tug",
            "Request the nearer, unassigned harbor tug to assist immediately"
          ],
          "intended_action": "The pilot requests the nearer harbor tug to assist promptly rather than waiting for the originally assigned but delayed tug, weighing wind risk against schedule pressure."
        },
        {
          "phase": 4,
          "decision_point": true,
          "facts_available_before_decision": [
            "A cross-current is pushing the vessel off the planned berthing line during final approach",
            "Two tugs are now made fast and available for correction",
            "Berth structure and neighboring vessel proximity limit room for error"
          ],
          "new_information_after_decision": [
            "The correction with tug and thruster input brings the vessel back onto line, but with reduced margin to the neighboring berth",
            "The berth operator confirms mooring lines can be run despite the tighter approach angle"
          ],
          "alternatives": [
            "Continue the current approach and correct with tug and thruster power",
            "Abort the approach and circle for a fresh attempt",
            "Request maximum tug power immediately rather than gradual correction"
          ],
          "intended_action": "The pilot orders a graduated tug and thruster correction to regain the berthing line rather than aborting, judged against the vessel's response and available room."
        }
      ],
      "probe_plan": {
        "opening": [
          "Can you walk me through what you knew about this transit before you even boarded the vessel?",
          "What made this passage feel nonroutine compared to a typical transit up this channel?"
        ],
        "timeline_reconstruction": [
          "What happened right after you boarded, in the order it happened?",
          "At what point did new information start coming in about channel conditions, wind, or tug availability?",
          "How did the situation evolve between boarding and final berthing?"
        ],
        "decision_point_probes": [
          "At the moment you confirmed the passage plan, what specific numbers or reports were you weighing?",
          "When the updated sounding report came in, how did you factor it against the earlier tide-table figure?",
          "What alternatives did you consider when the barge encroached on the channel, and why did you choose the one you did?",
          "When the second tug was delayed and wind picked up, what options did you weigh before requesting the nearer tug?",
          "During the final berthing correction, what made you choose to continue rather than abort the approach?",
          "How much time did you have to decide at each of these points?",
          "How confident were you in the information available at each decision, and why?"
        ],
        "closing_hypotheticals": [
          "If the echo sounder report had come in before you left the pilot station rather than mid-transit, would your initial timing decision have changed?",
          "If the second tug had arrived on time, would your approach through the bend or the berthing correction have gone differently?",
          "Looking back, is there a point where you might have weighted the newer information more heavily?",
          "What would you tell a less experienced pilot to watch for in a transit like this one?"
        ]
      },
      "occurrence_embedding_plan_internal": [
        {
          "instance_id": "ab_01",
          "bias": "Anchoring Bias",
          "decision_point": 1,
          "mechanism": "The pilot's risk judgment anchors on the pre-boarding tide-table UKC figure (1.2m) and insufficiently adjusts this estimate after receiving a fresher, more direct echo sounder report indicating actual clearance closer to 0.7m, effectively treating the initial figure as the controlling reference despite superseding evidence.",
          "affected_reasoning_operation": "Quantitative risk-margin updating in light of new evidence",
          "evidence_available_at_time": [
            "Pre-arrival tide table email citing 1.2m predicted UKC",
            "Outbound pilot's real-time echo sounder sweep reporting reduced clearance near km 4",
            "Updated tide gauge readings showing slower-than-predicted rise"
          ],
          "required_textual_manifestation": "The pilot explicitly cites the original 1.2m figure as the basis for confidence, characterizes the new sounding as probably conservative or not fully comparable, and proceeds on the original timing without describing any recalculation of the margin using the new numbers.",
          "plausible_nonbias_interpretation": "The pilot could reasonably discount the new sounding as taken by a different vessel with a different draft profile, or trust the tide table as an institutionally verified source, making the choice a defensible professional judgment rather than a bias.",
          "strength": "moderate",
          "do_not_make_explicit": [
            "Do not name or define anchoring bias",
            "Do not have the pilot reflect explicitly on being 'anchored' to a number",
            "Do not have any other decision point reference the original 1.2m figure or repeat this reasoning pattern"
          ]
        }
      ],
      "control_specification": {
        "paired_scenario_id": null,
        "features_to_match": [],
        "features_to_remove_or_change": [],
        "ambiguity_boundary": "Not applicable; condition is 'biased', no paired control scenario supplied."
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
        "Confirm exactly one anchoring bias instance (ab_01) is embedded, located only at decision point 1.",
        "Confirm decision points 2, 3, and 4 contain no intentional anchoring-bias language or repeated reference to the original 1.2m UKC figure.",
        "Confirm the interview does not use the words 'bias', 'anchor' (in the psychological sense), or any bias-labeling language.",
        "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given four decision points, opening, timeline reconstruction, and closing hypothetical probes without repetitive exposition.",
        "Confirm each decision point offers at least two plausible, distinct alternatives.",
        "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
        "Confirm consequences described (tighter berthing margin, successful correction) do not mechanically prove or disprove whether decision 1 was biased.",
        "Confirm plausible non-bias interpretation for ab_01 is preserved as a legitimate alternative reading in the narrative."
      ]
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "biased",
      "exact_occurrence_manifest": [
        {
          "bias": "Anchoring Bias",
          "occurrences": 1,
          "mechanism_constraint": null
        }
      ],
      "target_bias_names": [
        "Anchoring Bias"
      ],
      "requested_occurrence_count_for_each_bias": [
        {
          "bias": "Anchoring Bias",
          "requested_occurrences": 1
        }
      ],
      "planned_instance_ids": [
        {
          "instance_id": "ab_01",
          "bias": "Anchoring Bias"
        }
      ],
      "intended_decision_points": [
        {
          "instance_id": "ab_01",
          "bias": "Anchoring Bias",
          "decision_point": 1
        }
      ],
      "intended_mechanisms": [
        {
          "instance_id": "ab_01",
          "bias": "Anchoring Bias",
          "mechanism": "Pilot's UKC risk estimate anchors on the pre-boarding tide-table figure (1.2m) and is insufficiently adjusted after a fresher, more direct echo sounder report suggests actual clearance near 0.7m.",
          "affected_reasoning_operation": "Quantitative risk-margin updating under new evidence",
          "evidence_source": "Pre-arrival tide table (initial anchor) vs. outbound pilot's real-time echo sounder sweep and updated tide gauge readings (disconfirming/updating evidence)",
          "distinctiveness_requirement": "Not applicable; only one instance requested, so no distinctiveness-from-sibling-instance requirement applies."
        }
      ],
      "intended_strength": [
        {
          "instance_id": "ab_01",
          "bias": "Anchoring Bias",
          "strength": "moderate"
        }
      ],
      "paired_scenario_id": null,
      "counterfactual_variable": {
        "name": null,
        "original_state": null,
        "changed_state": null,
        "variables_to_hold_constant": []
      },
      "scenario_id": "MO_Biased_1",
      "domain_id": "MO",
      "total_requested_occurrences": 1,
      "total_planned_occurrences": 1,
      "allocation_rule_used": "Single occurrence assigned to decision point 1 based on mechanism fit: anchoring bias requires an initial numeric estimate encountered early in the timeline (pre-boarding tide table figure) that persists despite later disconfirming evidence (real-time sounding), which is most narratively realistic at the first decision point rather than later points where the initiating anchor would already be stale or absent.",
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
        "segment_type": "environmental_assessment",
        "raw_interview_anchor": "The forecast weather was closing in a bit faster than the morning brief suggested. Roughly a four-hour window before sea state would exceed the platform crane’s limit. So there was schedule pressure, but nothing outside what we train for.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Interprets the weather window as schedule pressure while judging the conditions within training."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "reference_system_decision",
        "raw_interview_anchor": "On final approach I picked up a 1.7-meter discrepancy between HPR and the two DGPS units, which were agreeing with each other closely. The system had auto-weighted the DGPS pair and was showing green. I also remembered that HPR had an intermittent fault logged from a previous voyage — cleared, but never formally re-certified after that. Given that history, I treated the DGPS pair as the more trustworthy read and logged the discrepancy as unresolved rather than fully explained, and continued the approach.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The zero-instance manifest specifies a fault-history-based reliability rationale, preserved uncertainty, and no automation or confirmation mechanism."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "continuation_decision",
        "raw_interview_anchor": "About halfway — 55% of cargo across — Thruster 3 raised a yellow caution, reduced power available. Consequence analysis still showed adequate capability, but with less margin than we’d started with. I also knew that switching to a more conservative configuration at that point would cost us something like twenty to twenty-five minutes we didn’t have much room for against the weather window, so I weighed that against the capability numbers and kept going at the same pace.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The zero-instance manifest specifies a forward-looking comparison of consequence-analysis margin and time cost; cargo completion is not the stated basis."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "attention_and_workload_episode",
        "raw_interview_anchor": "On the second-to-last lift, there was a wind shift that changed the footprint recommendation on the DP plot. I was on the crane boom display at that point, which is standard procedure during an active lift, and my co-operator was mid-exchange on the radio confirming rigging for the next lift, so neither of us picked up the footprint change immediately.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The zero-instance manifest explains delayed registration through standard procedure and legitimate concurrent tasks."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "final_lift_decision",
        "raw_interview_anchor": "For the final lift, OIM asked whether we could finish or should stand off. I checked both the time estimate — eight to ten minutes — and the separation and capability readout, which still looked adequate for that duration, and told him we could finish. Partway through, our separation closed faster than either figure had suggested it would, and we suspended early and backed off.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The zero-instance manifest specifies that both time and margin were consulted; the later near-approach does not establish biased reasoning."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "monitoring_allocation_rationale",
        "raw_interview_anchor": "Early on, reference systems and DP status, which is standard for closing distance. Once we were alongside, it split across the crane display, thruster status, and periodic environmental checks. During the final lift specifically, the crane display gets priority per procedure, and whoever’s free on the bridge picks up secondary monitoring — that shifted around a bit depending on what else was happening at the time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explains procedure-based monitoring priorities and secondary-monitor allocation as workload changes."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "reference_evidence_weighting",
        "raw_interview_anchor": "DGPS1 and DGPS2 agreed tightly. HPR was off by 1.7 meters, and it had that fault history from a prior voyage — nothing currently logged against it, but nothing re-certifying it as fully sound either. Given a choice between two fresh, agreeing units and one with an open question mark over it, I leaned toward the DGPS pair. I didn’t call it settled — I noted it as something to keep an eye on rather than a solved problem.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. The participant cites underlying reference data and fault history, and keeps the discrepancy unresolved."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "diagnostic_pause_decision",
        "raw_interview_anchor": "I thought about it. It would have meant holding the approach for a few minutes with no clear guarantee it would tell us anything conclusive, since the fault history was intermittent by nature. I judged the DGPS agreement plus HPR’s own track record gave enough basis to proceed, but I’ll be honest, it wasn’t a fully closed question either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explicitly weighs a diagnostic pause against its uncertain value and preserves uncertainty."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "capability_time_tradeoff",
        "raw_interview_anchor": "The consequence analysis still cleared us, just with a smaller cushion than before. I also had a rough number for what a mode change would cost us time-wise against a window that was already tight. It came down to margin against time cost, and the margin figure won out. I can see an argument either way on that one.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explicitly states the comparison between capability margin and projected time cost."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "cargo_completion_influence",
        "raw_interview_anchor": "No — the cargo already across was just where we happened to be in the sequence, not something I weighed. The actual comparison was the consequence-analysis margin against the projected delay from reconfiguring, and the margin held up well enough to justify continuing at that point.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explicitly rejects completed cargo as a reason and restates the forward-looking trade-off."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "attention_allocation_explanation",
        "raw_interview_anchor": "Standard procedure has the crane display as priority during an active lift. My co-operator was tied up confirming rigging on the radio for the next lift, which is a legitimate concurrent task, not something either of us could have dropped without creating a different problem. So the footprint change sat for a short while before either of us caught it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Provides a procedure and concurrent-workload explanation for the missed cue."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "monitoring_reassignment_tradeoff",
        "raw_interview_anchor": "Possibly, but it would have meant interrupting a rigging confirmation that also affects safety on the next lift. It’s a genuine trade-off, not an obvious call either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Weighs reassignment against another safety-relevant task."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "final_lift_evidence_weighing",
        "raw_interview_anchor": "I looked at both numbers I had — time to finish and the current separation and capability readout — and both supported finishing at that moment. The margin just closed faster than either had indicated it would once we were actually maneuvering.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. States that both time and margin information informed the decision and attributes the outcome to faster-than-expected closure."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "conditional_decision_prediction",
        "raw_interview_anchor": "Probably, yes — if the readout itself had been less favorable I’d have told him to stand off. The issue wasn’t which number I used, it’s that the number moved faster than expected.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Conditionally predicts a different action if the readout were less favorable."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "retrospective_foreseeability_assessment",
        "raw_interview_anchor": "Honestly, I go back and forth on that. Individually, none of those things — the discrepancy, the caution, the workload split — crossed a line that demanded a different call. Whether they add up to something predictable in hindsight, or whether it just came together unluckily at the end, I’m genuinely not sure.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Explicitly remains uncertain about foreseeability rather than asserting the outcome was obvious."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "prospective_recheck_rationale",
        "raw_interview_anchor": "Maybe build in a fixed re-check of the margin figures rather than relying on the initial assessment holding steady. Otherwise I think the calls were reasonable given what was in front of me at each point.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest requests zero occurrences. Identifies a possible future re-check practice and explains it in light of changing margin."
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
      "retrieved_corpus_support_used": true,
      "analysis_scope_note": "Analysis restricted to affirmative transcript evidence of bias-specific mechanisms; operational risk-management choices and self-correcting decisions were not classified as bias."
    },
    "identified_bias_summary": [
      {
        "bias_label": "Anchoring bias",
        "identified_occurrence_count": 1
      }
    ],
    "identified_occurrences": [
      {
        "occurrence_id": "obs_001",
        "classification_status": "identified",
        "confidence": "high",
        "bias_label": "Anchoring bias",
        "alternative_labels": [
          "Anchoring and adjustment heuristic",
          "Anchoring effect"
        ],
        "taxonomy_status": "established_label",
        "bias_definition": "The tendency to rely too heavily on an initial value, or anchor, and to make insufficient adjustments from that anchor when later information is received.",
        "attributed_to_speaker": "Participant",
        "evidence_speaker": "Participant",
        "decision_episode_label": "Under-keel clearance decision after outbound pilot's echo sounder report",
        "decision_point_description": "After receiving an outbound pilot's echo sounder reading of approximately 0.7m clearance and a VTS tide gauge lag, the participant decided whether to delay, slow and shift track, or proceed on the original planned 1.2m clearance timing.",
        "affected_reasoning_operation": "Updating a numerical clearance estimate and choosing whether to revise transit timing in response to new field data.",
        "bias_specific_mechanism": "Insufficient adjustment from an initial, vetted plan value of 1.2m under-keel clearance. The original figure served as an anchor, and contradictory new information, the 0.7m sounding and slower tide rise, was treated as not enough to override it without recalculating.",
        "manifestation_in_interview": "The participant explicitly stated that the original 1.2m clearance figure felt like 'the anchor point for the whole plan' and continued to treat it as the operative number after the new sounding and tide information arrived.",
        "effect_on_reasoning_or_decision": "The participant chose to hold the original timing and proceed rather than delaying or slowing and shifting toward deeper water, giving less weight to the fresh sounding and tide gauge lag than he later indicated they deserved.",
        "interview_evidence": [
          {
            "speaker": "Participant",
            "verbatim_quote": "Honestly, the original number felt like the anchor point for the whole plan, it had already been checked by port control, and one radio call didn't feel like enough to unwind that.",
            "evidence_explanation": "This explicitly identifies the original clearance value as an anchor and shows that the new radio report was judged insufficient to dislodge it, which is the core anchoring-and-adjustment mechanism."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "I chose to hold our timing and proceed as planned, treating the 1.2 as still the number that mattered.",
            "evidence_explanation": "This shows that the anchor carried forward into the decision to proceed without revision, despite the contradictory echo sounder and tide gauge information."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "I leaned on the original figure because it had already been vetted, and I discounted the fresh sounding a bit more than I probably should have.",
            "evidence_explanation": "This retrospectively confirms that the initial vetted figure was over-weighted relative to the fresh sounding, directly evidencing insufficient adjustment."
          }
        ],
        "correction_or_counterevidence": "The participant did consider alternatives, including delaying about 40 minutes or slowing and shifting toward the deeper side, and offered a legitimate non-bias reason for caution about the radio report: a single sweep from another vessel may not match his vessel's draft and trim. He also retrospectively acknowledged that he may have underweighted the new sounding.",
        "retrieved_corpus_support_available": true,
        "corpus_support_note": "The retrieved corpus contains a passage explicitly describing anchoring and adjustment as making estimates from an initial value and then adjusting insufficiently from later information.",
        "corpus_evidence": [
          {
            "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
            "paper_title": null,
            "authors": null,
            "publication_year": null,
            "retrieved_passage_or_finding": "Anchoring and Adjustment  The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
            "mechanism_supported_by_source": "The source describes the anchoring-and-adjustment mechanism in which an initial answer anchors subsequent estimates and later information produces insufficient adjustment.",
            "relevance_to_this_occurrence": "This directly matches the participant's stated reliance on the original 1.2m clearance figure as an anchor and his decision not to override it from a single radio report, later acknowledging he discounted the fresh sounding more than he should have."
          }
        ]
      }
    ],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Plan continuation bias",
        "alternative_labels": [
          "Get-there-itis"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Overall transit continuation across accumulating risk cues",
        "supporting_interview_quote": "None of those alone would worry me much, but together they made it a transit where I was managing multiple moving pieces instead of just following the plan.",
        "plausible_mechanism": "Continuing with a pre-existing plan despite accumulating discrepant cues rather than reassessing the go/no-go decision.",
        "why_not_identified": "The transcript shows the participant actively considered alternatives and made explicit adjustments at each decision point; the clearest biased mechanism is anchoring on the initial clearance figure, not a general plan-continuation mechanism."
      }
    ],
    "no_supported_biases_found": false,
    "limitations": [
      "Single debrief self-report; no independent measurement of actual clearance, tide, or wind values.",
      "Retrieved corpus sources have sparse metadata and OCR-like truncation, limiting citation completeness.",
      "Classification is conservative and excludes operational risk-management choices that do not show affirmative bias-specific mechanisms."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Biased_1_Sonnet_on",
  "interview_id": "MO_Biased_1",
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
