<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. Just to confirm, you're okay with this being recorded for training analysis, no names attached?

Participant: Yes, that's fine.

Interviewer: Could you give me a quick sense of your background?

Participant: Sixteen years piloting on this river system, mostly deep-draft container and bulk carriers. I've taken vessels the size of the Kalliopi up to Berth 7 probably a hundred times.

Interviewer: Let's talk through this particular transit. What did you know before boarding?

Participant: It was a fully loaded container ship, about 300 meters, drawing 14.2 meters. Port control had sent the passage plan that morning built around the tide table, giving roughly 1.2 meters of under-keel clearance at our planned transit time. That's tight but workable for that stretch under normal conditions. We had a closing tidal window, maybe ninety minutes, two tugs assigned, and wind forecast around 15 knots picking up through the afternoon.

Interviewer: What made this one feel nonroutine?

Participant: A few things stacked up together. A barge was moored tighter to the bend than charted, one of our tugs got delayed at the pilot station, and the wind ended up running hotter than forecast. Individually those are manageable. Together, they meant I was reassessing constantly instead of just running the plan as written.

Interviewer: Walk me through what happened after you boarded.

Participant: I went up to the conning position, confirmed the plan with the master, checked the draft survey again, and we got underway close to schedule. Shortly after, an outbound pilot radioed a fresh echo sounder sweep from near kilometer four, reporting less water than expected, closer to 0.7 meters instead of the 1.2 we'd planned around. Around the same time, VTS mentioned the tide gauge was reading a slower rise than the table predicted.

Interviewer: How did things develop from there?

Participant: Approaching the bend, VTS told us the barge hadn't moved despite requests, so I adjusted our track. Then the wind picked up faster than forecast right as we were down to one tug made fast, with the second still twenty minutes out. Near the berth, a cross-current pushed us off line during final approach, and we corrected with the tugs we had by then.

Interviewer: Let's take these one at a time. Starting with the clearance question after the outbound pilot's report — what were you actually weighing?

Participant: I had the morning tide table figure, and now a fresh sounding plus a tide gauge trend running slower than predicted. I didn't want to just discount either one. I asked the master to run our own echo sounder sweep as we approached that stretch to see what we were actually reading under our own hull, since the outbound vessel's trim and draft weren't identical to ours. That came back closer to the outbound pilot's number than the original table, maybe 0.8 to 0.9 meters once I accounted for our squat at the speed we were making.

Interviewer: So how did that change your plan?

Participant: I cut speed to reduce squat and shifted our track toward the deeper water on the outer edge of that stretch. Combined, cutting speed and hugging the deeper line got our effective margin back to something I was comfortable with, without needing to blow the tidal window with a full delay.

Interviewer: Did you consider just holding the original timing, or delaying instead?

Participant: Both were on the table. Holding the original timing didn't sit right once we had two independent readings pointing the same direction. A full forty-minute delay was the safer extreme, but I judged that speed and track adjustment addressed the actual shortfall without sacrificing the window. It was closer than I like, honestly, maybe a six out of ten on confidence, but it was based on our own numbers, not just the forecast.

Interviewer: Moving to the barge near the bend, what options did you weigh?

Participant: Push VTS harder for an emergency move, slow down and favor the wider side, or hold position until it cleared. I went with slowing and shifting track because waiting would have eaten into the window we'd already tightened up, and pushing VTS wasn't going to move the barge fast enough anyway.

Interviewer: How much time did you have to decide?

Participant: A couple of minutes. Enough to make a deliberate call, not enough to sit and debate it.

Interviewer: Next, the tug situation with rising wind.

Participant: With only one tug fast and the second still well out, and gusts running above forecast, I didn't want to rely purely on the bow thruster given our draft. When I heard a harbor tug not originally assigned was nearby, I requested that one instead of waiting on our delayed second tug. Getting help sooner mattered more than sticking with the original assignment.

Interviewer: Was waiting ever seriously on the table?

Participant: Briefly, yes, but the wind was trending the wrong way, and bringing in help early felt like the safer bet.

Interviewer: And the final approach, with the cross-current?

Participant: By then both tugs were fast. I chose a graduated correction rather than aborting, applying tug and thruster power progressively and watching the response. If that hadn't taken hold quickly, I would have aborted and circled. It ended up tighter to the neighboring berth than I'd like, but within what the berth operator confirmed was workable.

Interviewer: What made continuing feel safer than aborting?

Participant: The initial response to tug power told me we had steerage and margin. That's really the deciding factor in the moment, how she responds to the first correction.

Interviewer: Looking back, if the echo sounder report had reached you before you even left the pilot station, would your approach have changed?

Participant: Possibly less improvisation involved. I'd have built the speed reduction and track shift into the plan from the start rather than adjusting mid-transit. The outcome likely would have been similar, just calculated earlier with more margin to plan around.

Interviewer: If the second tug had arrived on schedule, would the bend or the berthing approach have gone differently?

Participant: The bend, not much, that was about the barge and speed. The berthing correction might have felt less tight, since we'd have had both tugs from the start rather than bringing in a substitute.

Interviewer: Anything you'd have wanted to know sooner?

Participant: I'd have liked our own sounding data earlier rather than relying on someone else's reading first. That's really a sequencing issue, not a judgment one.

Interviewer: What would you tell a less experienced pilot about a transit like this?

Participant: Don't treat any single number, old or new, as final. Cross-check it against your own instruments when the margin is tight enough to matter, and build your track and speed decisions around what you can verify yourself.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "MO_Vocab_Control_1",
    "domain_id": "MO",
    "domain": "Maritime Operations",
    "role": "Harbor Pilot / Marine Pilot",
    "condition": "vocabulary_control",
    "generation_specification": {
      "scenario_title_internal": "The Falling Tide: Piloting MV Kalliopi to Berth 7 (Vocabulary-Matched Control)",
      "scenario_summary_internal": "A harbor pilot boards a fully laden container vessel for the same time-critical river transit as the paired scenario, facing an identical sequence of operational pressures: a closing tidal window, a barge encroaching a channel bend, a delayed tug under rising wind, and a cross-current final approach. Unlike the paired biased scenario, the pilot's handling of the initial under-keel clearance question integrates the fresh echo sounder report and updated tide gauge data into a genuinely revised risk judgment, rather than treating the original tide-table figure as controlling. All other decision points, vocabulary, actors, constraints, and narrative tone match the paired scenario, with no intentional instance of anchoring bias or any other named bias.",
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
        "constraints_note": "No excluded themes specified; standard maritime pilotage vocabulary applies throughout, matched to the paired scenario."
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
            "Proceed on the original schedule, treating the tide-table UKC figure as still valid",
            "Delay departure roughly 40 minutes to allow the tide to rise further before entering the shoal area",
            "Reduce transit speed and take a slightly longer route favoring the deeper side of the channel"
          ],
          "intended_action": "The pilot cross-checks the outbound pilot's sounding against the vessel's own echo sounder readings and the updated tide gauge trend, weighs the combined margin against the vessel's draft and squat allowance, and elects to reduce speed and shift toward the deeper side of the channel rather than holding the original timing unchanged."
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
          "Looking back, is there anything you would have wanted to know sooner?",
          "What would you tell a less experienced pilot to watch for in a transit like this one?"
        ]
      },
      "occurrence_embedding_plan_internal": [],
      "control_specification": {
        "paired_scenario_id": "MO_Biased_1",
        "features_to_match": [
          "Domain vocabulary (UKC, tide table, echo sounder sweep, squat effect, conning position, VTS clearance, bow thruster, tug made fast, set and drift, passage plan)",
          "Four-decision-point structure and sequence (clearance/timing, barge at bend, tug/wind shortage, cross-current berthing)",
          "Stakeholder roster (Master, VTS, tug captains, berth operator, outbound pilot)",
          "Difficulty level (challenging) and time-pressure profile at each decision point",
          "Emotional tone: measured, professional, mild tension without alarm",
          "Word count target and probe plan structure"
        ],
        "features_to_remove_or_change": [
          "The pilot's treatment of the initial tide-table figure: in the control, the pilot integrates the new sounding and tide gauge data into a revised judgment rather than holding the original figure as controlling",
          "Any language suggesting the original estimate was retained despite superseding evidence"
        ],
        "ambiguity_boundary": "The decision at phase 1 must remain genuinely uncertain and challenging (tight margins, imperfect cross-vessel comparability of the sounding) but must show visible integration of the new evidence into the final judgment, not mere retention of the initial figure."
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
        "Confirm zero intentional instances of anchoring bias or any other named bias appear anywhere in the interview.",
        "Confirm decision point 1 shows explicit integration of the fresh echo sounder report and tide gauge trend into the pilot's revised risk judgment, not retention of the original 1.2m figure as controlling.",
        "Confirm decision points 2, 3, and 4 remain structurally and vocabulary-matched to the paired biased scenario.",
        "Confirm technical vocabulary list matches the paired scenario's technical_terms_to_use.",
        "Confirm difficulty, actor roster, constraint set, and emotional tone match the paired scenario.",
        "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given four decision points and full probe coverage.",
        "Confirm each decision point offers at least two plausible, distinct alternatives.",
        "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
        "Confirm no bias-labeling or psychological vocabulary appears anywhere in the interview."
      ]
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "vocabulary_control",
      "exact_occurrence_manifest": [
        {
          "bias": "Anchoring Bias",
          "occurrences": 0,
          "mechanism_constraint": "No intentional anchoring-bias manifestation permitted; decision point 1 must show genuine integration of new evidence into a revised judgment."
        }
      ],
      "target_bias_names": [
        "Anchoring Bias"
      ],
      "requested_occurrence_count_for_each_bias": [
        {
          "bias": "Anchoring Bias",
          "requested_occurrences": 0
        }
      ],
      "planned_instance_ids": [],
      "intended_decision_points": [],
      "intended_mechanisms": [],
      "intended_strength": [],
      "paired_scenario_id": "MO_Biased_1",
      "counterfactual_variable": {
        "name": null,
        "original_state": null,
        "changed_state": null,
        "variables_to_hold_constant": []
      },
      "scenario_id": "MO_Vocab_Control_1",
      "domain_id": "MO",
      "total_requested_occurrences": 0,
      "total_planned_occurrences": 0,
      "allocation_rule_used": "Not applicable; vocabulary_control condition requires zero intended bias instances across all decision points, so no allocation was performed.",
      "control_zero_bias_requirement": true,
      "variables_to_hold_constant": [
        "Domain vocabulary and technical terminology",
        "Four-decision-point narrative structure and sequence",
        "Stakeholder roster and role functions",
        "Operational constraints (tidal window, draft, tug delay, wind forecast, barge encroachment, cross-current)",
        "Difficulty level (challenging)",
        "Emotional tone and pacing",
        "Target word count and probe plan categories"
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
        "segment_type": "risk_assessment",
        "raw_interview_anchor": "\"That's tight but workable for that stretch under normal conditions.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Initial UKC/timing assessment is an operational risk judgment; no hidden bias is manifested."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "situation_interpretation",
        "raw_interview_anchor": "\"Individually those are manageable. Together, they meant I was reassessing constantly instead of just running the plan as written.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Interprets stacked operational pressures and explains adaptive reassessment; no hidden bias."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_weighting",
        "raw_interview_anchor": "\"I didn't want to just discount either one. I asked the master to run our own echo sounder sweep... since the outbound vessel's trim and draft weren't identical to ours.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Explicitly seeks an independent cross-check and accounts for cross-vessel comparability; no hidden bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "action_rationale",
        "raw_interview_anchor": "\"I cut speed to reduce squat and shifted our track toward the deeper water... got our effective margin back to something I was comfortable with.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Links speed and track changes to the measured clearance margin; no hidden bias."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "alternative_evaluation",
        "raw_interview_anchor": "\"Holding the original timing didn't sit right once we had two independent readings pointing the same direction. A full forty-minute delay was the safer extreme, but I judged that speed and track adjustment addressed the actual shortfall.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Weighs competing options and updates the plan using convergent evidence; no hidden bias."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "uncertainty_assessment",
        "raw_interview_anchor": "\"It was closer than I like, honestly, maybe a six out of ten on confidence, but it was based on our own numbers, not just the forecast.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. States calibrated uncertainty and the evidential basis for the choice; no hidden bias."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "alternative_evaluation",
        "raw_interview_anchor": "\"Push VTS harder... slow down and favor the wider side, or hold position... I went with slowing and shifting track because waiting would have eaten into the window...\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Considers alternatives and selects a track/speed adjustment under time constraints; no hidden bias."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "resource_allocation_rationale",
        "raw_interview_anchor": "\"I didn't want to rely purely on the bow thruster... I requested that one instead of waiting on our delayed second tug. Getting help sooner mattered more than sticking with the original assignment.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Requests an available substitute resource based on wind and handling risk; no hidden bias."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "alternative_evaluation",
        "raw_interview_anchor": "\"Briefly, yes, but the wind was trending the wrong way, and bringing in help early felt like the safer bet.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Explains rejection of waiting using the worsening wind trend; no hidden bias."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "continue_or_abort_rationale",
        "raw_interview_anchor": "\"I chose a graduated correction rather than aborting, applying tug and thruster power progressively and watching the response.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Chooses a controlled correction with monitoring over an immediate abort; no hidden bias."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "contingency_criterion",
        "raw_interview_anchor": "\"If that hadn't taken hold quickly, I would have aborted and circled.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. States an explicit contingency and abort criterion; no hidden bias."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "causal_attribution",
        "raw_interview_anchor": "\"The initial response to tug power told me we had steerage and margin. That's really the deciding factor in the moment.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Uses observed response as the decisive operational signal; no hidden bias."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "counterfactual_planning",
        "raw_interview_anchor": "\"I'd have built the speed reduction and track shift into the plan from the start rather than adjusting mid-transit.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Counterfactual explains earlier planning integration of the same evidence; no hidden bias."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "counterfactual_evaluation",
        "raw_interview_anchor": "\"The berthing correction might have felt less tight, since we'd have had both tugs from the start rather than bringing in a substitute.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Counterfactually evaluates the effect of an on-time tug on berthing margin; no hidden bias."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "causal_attribution",
        "raw_interview_anchor": "\"I'd have liked our own sounding data earlier rather than relying on someone else's reading first. That's really a sequencing issue, not a judgment one.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden exact occurrence manifest requests zero Anchoring Bias occurrences; this is an eligible non-biased reasoning segment. Attributes the improvement opportunity to information sequencing and explicitly rejects a judgment explanation; no hidden bias."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
