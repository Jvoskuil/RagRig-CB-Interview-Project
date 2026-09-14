You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": [
        "Interviewer",
        "Participant"
      ],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "The transcript was evaluated for affirmative, mechanism-grounded cognitive-bias occurrences. No retrieved scientific corpus passages were supplied in the RAG context; therefore, no corpus-supported classifications are asserted."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [],
    "no_supported_biases_found": true,
    "limitations": [
      "No retrieved bias corpus was available, so all analysis is based on the transcript alone.",
      "The transcript is a retrospective first-person account; the analysis is limited to reported reasoning rather than direct observation of cognition.",
      "The participant's reported decisions show active cross-checking, contingency planning, and updating in response to new information, which does not meet the conservative threshold for an affirmative cognitive-bias occurrence."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Vocab_Control_1_Gemini_off",
  "interview_id": "MO_Vocab_Control_1",
  "system_prompt_id": "Gemini",
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
