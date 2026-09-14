You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for training purposes — we're reviewing your decision-making during the Kestrel Subdivision shift, not evaluating your performance. Is that alright with you?

Participant: Sure, no problem. I've done a few of these before.

Interviewer: Great. Can you start by telling me your role and what the board looked like that evening?

Participant: I was the sole dispatcher covering the Kestrel Sub, about 40 miles of single track for most of it. We had a maintenance possession scheduled from 6:40 to roughly 7:30 for tamping work near milepost 214, plus a mixed traffic evening — a manifest freight headed east and an intercity passenger train that was already running about 22 minutes behind schedule with a connection downstream. My main priority was keeping things moving safely through that one possession window without letting the passenger delay balloon further.

Interviewer: Walk me through how the incident actually unfolded.

Participant: About twenty minutes into my shift, the wayside hot-box detector near milepost 198 flagged the freight train — an axle bearing reading slightly above baseline, but well under the threshold that triggers an automatic stop. No abnormal noise reported by the crew, nothing visual. Not long after that, I started working the sequencing problem for the passenger train getting through the work zone at 214. Then, while I was juggling that, the foreman on-site radioed in something about a possible person near the right-of-way — the transmission was choppy, in and out, so I didn't get a clean picture of where exactly or how many. And near the tail end of the possession, the foreman asked for a 12-minute extension to finish the tamping work properly.

Interviewer: So four distinct things landed on you in a fairly short window.

Participant: Pretty much back to back, yeah. That's a normal night on that line, honestly — it's just a matter of which order you deal with them and what you're willing to let sit for a minute.

Interviewer: Let's reconstruct the order. What came first, and what did you do right after?

Participant: The hot-box alert came first. I checked the reading against the threshold table — it was elevated, but not near the automatic-stop number. The next detector was about 8 miles up the line. I authorized the crew to proceed at restricted speed to that next detector rather than stopping cold on the single track, since stopping there would've blocked everything behind it, including the passenger train's approach to the work zone. When the next reading came back, the temperature had actually stabilized rather than climbed, so that resolved fairly cleanly.

Interviewer: What was going through your mind when you made that call?

Participant: The number was below the mandatory stop point, so procedurally I had room to make that judgment. Stopping a train on that single track for a hands-on inspection is a big deal — it doesn't just hold up that train, it backs up the whole corridor behind it. Given no other symptoms from the crew, restricted speed to the next detector felt like the appropriate middle ground. I've made calls like that before and they've resolved fine most of the time.

Interviewer: How confident were you at that moment?

Participant: Reasonably. Not certain — you're never fully certain with a bearing reading — but confident enough given the threshold and the lack of other symptoms.

Interviewer: Let's move to the passenger train and the work zone. What were your options there?

Participant: Two real options. One, hold the passenger train for a short window — maybe four or five minutes — while the crew paused work, and let it through under standard flag protection, which is the setup they use routinely at that site. Two, reroute it entirely onto the alternate line, which avoids the work zone altogether but adds about 25 minutes and forces me to realign two other train slots later in the evening.

Interviewer: Which did you choose, and why?

Participant: I sent it around on the alternate line. I just didn't want that train anywhere near an active work zone that evening — I wanted it completely clear of that whole area rather than threading it through on a flag. Even though the flagging setup there is the standard one they use all the time, I'd rather eat the schedule hit than have any interaction with the work zone at all.

Interviewer: Was there something specific about that flag protection that made you distrust it?

Participant: Not really anything specific to that crew — it's the same setup used all over the subdivision. I think I just weighed it as, if I reroute, that risk is off the table entirely, full stop. The delay is a known, manageable cost. I didn't sit there and compare exactly how much risk the flagged window actually removes versus how much schedule damage the reroute causes — it was more that avoiding the zone altogether felt like the safer place to land.

Interviewer: Did the 25-minute cost and the two realigned slots factor into that comparison?

Participant: They were in the back of my mind, but honestly, once I decided I wanted the train out of that zone entirely, the size of the delay became secondary. It's not that I ignored it, I just didn't weigh it against how small the actual exposure through a flagged window normally is.

Interviewer: Let's go to the trespasser report. What did you actually hear?

Participant: It was garbled — "possible person near the right-of-way," something like that, no confirmed location, no headcount, and I couldn't tell if they'd already moved off or not. Reception near that stretch is spotty.

Interviewer: What were your options at that point?

Participant: Realistically both options started with getting a precaution in place right away — you don't leave a train unprotected on a report like that no matter which way you go next. So it was really a question of which precaution. I could issue the standard subdivision-wide restriction — ten minutes of restricted speed through the whole general area — which is the routine call for reports like this. Or I could put a shorter restriction on just the immediate approach while the foreman tried a callback, and then either lift it early or extend it once I actually knew what we were dealing with.

Interviewer: Which did you go with?

Participant: I went with the full ten-minute restriction across the whole area. It's the protocol I know — fixed length, fixed scope, everyone on the radio understands exactly what it means and when it ends. The tailored version might've actually cost the queued trains less time if the callback had come back clean, but I couldn't tell you up front how long that would run or how far the restriction would need to extend, so it felt like the harder thing to commit to in the moment.

Interviewer: Did you weigh what the report might actually mean — say, that it could be nothing, or could be something more serious than the standard protocol addresses — against the tailored option?

Participant: Not really as a probability question, no. It wasn't that I sat down and worked out how likely it was to be nothing versus something worse. It was more that the fixed protocol had a shape I could describe to everyone right away, and the tailored version was open-ended until the callback came through, so I defaulted to the one with the known edges.

Interviewer: Last decision — the possession extension.

Participant: The foreman asked for 12 more minutes to finish the tamping properly. I had two trains queued behind the work zone at that point. I granted it. Denying it risked leaving the work incomplete, which usually means scheduling a whole new possession later in the week — more disruption overall. The queued trains absorbed a modest additional delay, but the crew finished clean.

Interviewer: How did you land on that one?

Participant: That was more of a straightforward cost comparison — a short, bounded extension now versus a bigger disruption later. Fairly routine call.

Interviewer: If the detector reading had been just a bit higher, would your first decision have changed?

Participant: Yes, definitely — if it had been near the stop threshold I'd have held the train for a physical inspection, no question.

Interviewer: And if the foreman's report had come through clearly instead of garbled — say, confirmed as one person who'd already left the area?

Participant: If I'd had that, I probably would've gone with the tailored, shorter restriction from the start instead of the full ten-minute call. Knowing the person was already clear would've given me something definite to scope the response around, instead of having to lean on the fixed protocol just because it was the one thing I could describe with certainty in the moment.

Interviewer: Looking back, is there anything you'd handle differently with the same information you had at the time?

Participant: Maybe on the reroute — I might spend a bit more time actually comparing what the flagged window really costs in risk versus what the full reroute costs in delay, rather than just leaning toward whichever option felt more completely clear of the zone. But overall, given what I knew in the moment, I'd probably make the same calls again.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Biased_2",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Rail Traffic Controller / Train Dispatcher",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Borderline Hot-Box Alarm and Work-Zone Reroute on the Kestrel Subdivision",
    "scenario_summary_internal": "A rail traffic controller manages a single-track corridor during an evening shift with a scheduled maintenance possession, a freight train that triggers a marginal wayside hot-box detector alert, a delayed passenger train needing to pass through an active work zone, and an ambiguous radio report of a possible trespasser near the work site. The controller must sequence four decisions under time pressure and incomplete information, balancing throughput, safety, and crew/possession constraints.",
    "occupational_realism": {
      "objective": "Maintain safe, on-time movement of freight and passenger traffic through a single-track corridor with an active maintenance possession, while responding appropriately to an equipment alarm and an ambiguous safety report.",
      "setting": "Evening shift, regional rail traffic control center, single dispatcher covering a 40-mile subdivision with one active track maintenance window and mixed freight/passenger traffic.",
      "constraints": [
        "Only one main track available through the work zone during the possession window",
        "Wayside hot-box detector gives a borderline (not clearly critical) temperature reading",
        "Passenger train is already running 22 minutes late with downstream connection commitments",
        "Track crew has a fixed possession end time before the next train movement is authorized",
        "Radio coverage near the work site is intermittent, limiting real-time clarification"
      ],
      "stakeholders": [
        "Rail traffic controller (interviewee)",
        "Freight train crew (engineer and conductor)",
        "Passenger train crew and dispatcher liaison",
        "Track maintenance foreman and work crew",
        "Regional operations manager (on-call)"
      ],
      "technical_terms_to_use": [
        "hot-box detector",
        "wayside defect detector",
        "possession/track warrant",
        "slow order",
        "block signal territory",
        "flag protection",
        "train dispatcher authority",
        "restricted speed"
      ],
      "technical_terms_to_avoid": [
        "zero-risk bias",
        "ambiguity aversion",
        "cognitive bias",
        "heuristic",
        "known versus unknown probability"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Wayside detector reports axle temperature slightly above baseline but below the automatic stop threshold",
          "Freight train is 8 miles from the next detector location",
          "No unusual noise or vibration reported by the crew"
        ],
        "new_information_after_decision": [
          "Next detector reading shows temperature has stabilized, not increased further"
        ],
        "alternatives": [
          "Instruct the freight train to proceed to the next detector at restricted speed for confirmation",
          "Stop the train immediately for a hands-on inspection, holding up the single track"
        ],
        "intended_action": "Controller allows the freight train to proceed at reduced speed to the next detector rather than stopping it immediately, based on the reading being below the mandatory-stop threshold."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Work zone occupies the single main track for another 35 minutes",
          "Passenger train can either wait for a short window between crew tasks (minor, well-defined delay) or be rerouted onto a longer alternate line that avoids the work zone entirely",
          "The short-window option requires standard flag protection already in place and used routinely at this site",
          "The reroute adds 25 minutes and requires realigning two other train slots"
        ],
        "alternatives": [
          "Hold passenger train for the brief flagged window through the work zone under standard protection",
          "Reroute passenger train onto the longer alternate line to avoid the work zone entirely"
        ],
        "intended_action": "Controller chooses the longer reroute to eliminate any interaction with the work zone entirely, even though the flagged-window option carries only a small, well-managed residual risk and causes far less network disruption."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Track foreman radios a brief, partially garbled report of a 'possible person near the right-of-way' close to the work site",
          "No confirmation of exact location, number of people, or whether they left the area",
          "A known, previously used protocol exists: reduce approaching trains to restricted speed through the general area for 10 minutes as a standard precaution",
          "An alternative exists: request the foreman attempt a direct callback for a clearer picture before issuing any speed instruction, delaying the decision by several minutes"
        ],
        "alternatives": [
          "Issue the standard restricted-speed instruction for the area immediately, treating the report as the known/routine trespasser protocol",
          "Delay action and attempt to get a clarified, specific report from the foreman before deciding on any speed restriction"
        ],
        "intended_action": "Controller favors the familiar, well-defined restricted-speed protocol over waiting for clarification, even though the vague report could plausibly indicate something requiring a different response, because the ambiguous option feels harder to act on than the known routine."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Track foreman requests a 12-minute possession extension to finish tamping work",
          "Two trains are queued behind the work zone awaiting clearance",
          "Denying the extension risks incomplete work needing a follow-up possession later in the week"
        ],
        "new_information_after_decision": [
          "Extension is granted; both queued trains experience additional minor delay",
          "Foreman completes work without further incident"
        ],
        "alternatives": [
          "Grant the 12-minute extension and hold queued traffic",
          "Deny the extension and require the crew to clear the track on schedule, deferring remaining work"
        ],
        "intended_action": "Controller grants the extension after weighing crew safety, work completeness, and downstream schedule impact."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what was happening on your board that evening before the detector alert came in.",
        "What was your overall priority at the start of the shift?"
      ],
      "timeline_reconstruction": [
        "What did you see or hear first, and what did you do immediately after?",
        "What information came in after each decision that you didn't have beforehand?"
      ],
      "decision_point_probes": [
        "What options did you consider at that point, and why did you rule the others out?",
        "What specific piece of information tipped your decision one way or the other?",
        "How much time pressure did you feel at that moment?",
        "How confident were you in the information you had, and what was still unclear?",
        "Had you handled a similar situation before, and did that shape your choice here?"
      ],
      "closing_hypotheticals": [
        "If the detector reading had been just slightly higher, would your first decision have changed?",
        "If the foreman's report had come through clearly instead of garbled, do you think you'd have responded differently?",
        "Looking back, is there a point where you'd handle things differently with the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "zrb_01",
        "bias": "Zero-Risk Bias",
        "decision_point": 2,
        "mechanism": "Controller disproportionately values eliminating a small, already well-controlled residual risk (brief flagged passage through the work zone) entirely, choosing a costly full reroute over a modest reduction of risk via standard, routinely effective flag protection.",
        "affected_reasoning_operation": "Risk-cost tradeoff weighting during route selection",
        "evidence_available_at_time": [
          "Flag protection at the work zone is described as standard and already in place",
          "The reroute imposes a much larger, quantifiable network cost (25 extra minutes, two realigned slots) than the residual risk it removes"
        ],
        "required_textual_manifestation": "Controller explicitly justifies the reroute by wanting to avoid the work zone 'completely' or 'entirely,' rather than comparing the magnitude of risk reduction to the delay cost, and does not weigh the flagged-window option's already-low residual risk against its much smaller disruption.",
        "plausible_nonbias_interpretation": "A controller could reasonably prefer the reroute simply due to unfamiliarity with that specific work crew's flagging reliability, which would be a legitimate risk judgment rather than bias.",
        "strength": "subtle",
        "do_not_make_explicit": ["zero-risk", "risk elimination", "disproportionate", "bias"]
      },
      {
        "instance_id": "ae_01",
        "bias": "Ambiguity effect",
        "decision_point": 3,
        "mechanism": "Controller prefers the familiar, well-specified restricted-speed protocol (known probability/known procedure) over seeking clarification of the ambiguous trespasser report, even though the vague report could call for a different, better-fitted response; the preference is driven by the report's ambiguity itself rather than a comparison of expected outcomes.",
        "affected_reasoning_operation": "Choice between two response options under differing degrees of information ambiguity",
        "evidence_available_at_time": [
          "The foreman's report is described as brief and partially garbled, with no confirmed location or number of people",
          "A callback for clarification is available as an option but described as taking 'several minutes longer'"
        ],
        "required_textual_manifestation": "Controller states a preference for the standard protocol specifically because the alternative (waiting for clarification) feels uncertain or hard to act on, rather than because the standard protocol was independently judged to be the better response to this specific report.",
        "plausible_nonbias_interpretation": "A controller could reasonably favor immediate restricted speed simply because safety protocol requires erring toward caution regardless of report clarity, which would be a justified default rather than an ambiguity-driven preference.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity effect", "known versus unknown probability", "aversion", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no paired control scenario was requested for this generation."
    },
    "counterfactual_specification": {
      "causal_variable": "Clarity of the trespasser report received from the track foreman",
      "original_state": "Report is brief, partially garbled, with no confirmed location or headcount",
      "counterfactual_state": "Report is clear and specific, confirming a single person who has already left the right-of-way",
      "variables_to_hold_constant": [
        "Hot-box detector event and outcome",
        "Work zone reroute decision and its network cost",
        "Possession extension request and grant",
        "Overall shift timing and traffic volume"
      ],
      "expected_causal_difference": "With a clear report, the controller would be expected to select a response proportionate to the confirmed, low-risk situation rather than defaulting to the standard restricted-speed protocol out of discomfort with ambiguity, isolating whether the choice was driven by report ambiguity versus genuine safety judgment.",
      "causal_test_question": "Does the controller's response to the trespasser report change when the same underlying risk level is communicated with full clarity instead of ambiguity?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present in the timeline",
      "Confirm decision points 1 and 4 contain no intentionally embedded named-bias instances",
      "Confirm zrb_01 appears only at decision point 2 and is not repeated in probes or hypotheticals",
      "Confirm ae_01 appears only at decision point 3 and is not repeated in probes or hypotheticals",
      "Confirm no bias terminology or psychological labels appear in interview text",
      "Confirm each decision point offers at least two plausible alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm final word count falls between 1215 and 1485 words",
      "Confirm consequences described do not conclusively prove either decision was biased or correct"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Zero-Risk Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as disproportionate preference for eliminating a small, already well-controlled risk entirely over a cost-comparable partial risk reduction"
      },
      {
        "bias": "Ambiguity effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as preference for a known/well-specified option over an ambiguous one driven by the ambiguity itself, not by an independent risk comparison"
      }
    ],
    "target_bias_names": ["Zero-Risk Bias", "Ambiguity effect"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Zero-Risk Bias", "requested_occurrences": 1 },
      { "bias": "Ambiguity effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "zrb_01", "bias": "Zero-Risk Bias" },
      { "instance_id": "ae_01", "bias": "Ambiguity effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "zrb_01", "bias": "Zero-Risk Bias", "decision_point": 2 },
      { "instance_id": "ae_01", "bias": "Ambiguity effect", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "zrb_01",
        "bias": "Zero-Risk Bias",
        "mechanism": "Disproportionate weighting of eliminating a small residual risk to zero over accepting a modest, well-protected risk with far lower disruption cost",
        "affected_reasoning_operation": "Risk-cost tradeoff weighting during route selection",
        "evidence_source": "Comparison between flagged-window protection adequacy and the magnitude of reroute-induced network delay",
        "distinctiveness_requirement": "Must involve the work-zone reroute decision specifically and the framing of 'complete avoidance' rather than proportional risk reduction; must not overlap with decision point 3's reasoning about ambiguity"
      },
      {
        "instance_id": "ae_01",
        "bias": "Ambiguity effect",
        "mechanism": "Preference for a familiar, fully specified protocol over an ambiguous report-driven judgment call, motivated by discomfort with unknown probability rather than a substantive risk comparison",
        "affected_reasoning_operation": "Choice between two response options differing in information ambiguity",
        "evidence_source": "The garbled, unconfirmed nature of the foreman's trespasser report versus the fully defined standard protocol",
        "distinctiveness_requirement": "Must involve the trespasser-report decision specifically and hinge on the report's ambiguity as the driver of choice; must not overlap with decision point 2's cost-based reasoning"
      }
    ],
    "intended_strength": [
      { "instance_id": "zrb_01", "bias": "Zero-Risk Bias", "strength": "subtle" },
      { "instance_id": "ae_01", "bias": "Ambiguity effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Clarity of the trespasser report received from the track foreman",
      "original_state": "Brief, partially garbled report with no confirmed location or headcount",
      "changed_state": "Clear, specific report confirming a single person who has already left the right-of-way",
      "variables_to_hold_constant": [
        "Hot-box detector event and outcome",
        "Work zone reroute decision and its network cost",
        "Possession extension request and grant",
        "Overall shift timing and traffic volume"
      ]
    },
    "scenario_id": "RT_Biased_2",
    "domain_id": "RT",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias assigned to a distinct decision point (2 and 3 respectively) chosen for mechanism fit and narrative realism; decision points 1 and 4 held neutral to avoid unintended bias instances; no bias shares a decision point, so intra-point distinctiveness rules were not needed.",
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
          "segment_type": "priority_setting",
          "raw_interview_anchor": "“My main priority was keeping things moving safely through that one possession window without letting the passenger delay balloon further.”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A reasonable operating goal; neither hidden mechanism is manifested."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "hot_box_disposition_rationale",
          "raw_interview_anchor": "“The number was below the mandatory stop point… Given no other symptoms from the crew, restricted speed to the next detector felt like the appropriate middle ground. I've made calls like that before and they've resolved fine most of the time.”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The action rests on threshold and symptom evidence; prior success does not establish availability-based distortion."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "confidence_assessment",
          "raw_interview_anchor": "“Reasonably. Not certain… but confident enough given the threshold and the lack of other symptoms.”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Calibrated confidence tied to available evidence."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "work_zone_reroute_reasoning",
          "raw_interview_anchor": "“I sent it around… I wanted it completely clear… rather than threading it through on a flag”; “risk is off the table entirely… I didn't… compare exactly how much risk… versus… schedule damage”; “I didn't weigh it against how small the actual exposure… normally is.”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "zrb_01"
          ],
          "ground_truth_rationale": "One coherent route-selection episode across follow-up probes: complete avoidance of small managed exposure dominates known delay without proportional comparison."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "baseline_precaution_reasoning",
          "raw_interview_anchor": "“Both options started with getting a precaution in place right away — you don't leave a train unprotected… So it was really a question of which precaution.”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Safety baseline shared by both options; it does not express the hidden preference for the known option."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "trespasser_response_selection",
          "raw_interview_anchor": "“I went with the full ten-minute restriction… fixed length, fixed scope… the tailored version… harder… to commit to”; “I didn't… work out how likely… It was more that the fixed protocol had a shape… so I defaulted to the one with the known edges.”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ae_01"
          ],
          "ground_truth_rationale": "The actual response preference is driven by the tailored option's ambiguity, not by a probability comparison."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "possession_extension_cost_tradeoff",
          "raw_interview_anchor": "“I granted it. Denying it risked leaving the work incomplete… more disruption overall. The queued trains absorbed a modest additional delay…”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Bounded cost comparison; the generation spec designates this decision neutral."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "hot_box_threshold_counterfactual",
          "raw_interview_anchor": "“If it had been near the stop threshold I'd have held the train for a physical inspection, no question.”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Conditional response to changed facts, not a hidden instance."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "trespasser_clarity_counterfactual",
          "raw_interview_anchor": "“Knowing the person was already clear would've given me something definite to scope the response around… lean on the fixed protocol… certainty in the moment.”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Counterfactual supports the causal role of clarity but is not an additional at-time instance."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "retrospective_route_reflection",
          "raw_interview_anchor": "“I might spend a bit more time actually comparing what the flagged window really costs in risk versus what the full reroute costs in delay…”",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Hindsight reflection on the mapped route decision, not a second manifested occurrence."
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
    "analysis_scope_note": "The transcript was analyzed for affirmative evidence of cognitive/perceptual/memory/motivational/social/group decision biases in the participant's reported decisions. No retrieved corpus passages were supplied, so any named labels rely on general cognitive-science knowledge and no retrieved citations are available."
  },
  "identified_bias_summary": [
    {
      "bias_label": "ambiguity aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "zero-risk bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "zero-risk bias",
      "alternative_labels": [
        "certainty effect",
        "risk elimination preference"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to prefer an option that eliminates a risk entirely over options that merely reduce it, even when the risk-reducing option is routine or objectively less costly.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Passenger train routing around active work zone",
      "decision_point_description": "Choice between holding the passenger train for a short flagged movement through the work zone versus rerouting onto the alternate line with a 25-minute delay and two downstream slot realignments.",
      "affected_reasoning_operation": "Risk evaluation and option selection under a safety-versus-delay trade-off",
      "bias_specific_mechanism": "Preference for completely removing the active-work-zone risk rather than reducing it through the standard flagged movement, without comparing the marginal risk reduction of the flagged window to the marginal schedule cost of the reroute.",
      "manifestation_in_interview": "The participant framed the reroute as taking the risk off the table entirely and described the standard flagged alternative as less attractive even though he acknowledged the flagging setup was routine. He reported not comparing the actual risk reduction to the delay cost and instead leaning toward the option that felt completely clear of the zone.",
      "effect_on_reasoning_or_decision": "The decision produced a full reroute with a known 25-minute delay and two downstream slot realignments, bypassing a lower-delay option the participant himself described as a routine flagging setup.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I sent it around on the alternate line. I just didn't want that train anywhere near an active work zone that evening — I wanted it completely clear of that whole area rather than threading it through on a flag.",
          "evidence_explanation": "This shows a preference for total separation from the hazard over a partial but standard exposure, rather than weighing the actual residual risk of the flagged option."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I just weighed it as, if I reroute, that risk is off the table entirely, full stop.",
          "evidence_explanation": "The participant explicitly treats the reroute as complete risk elimination, which is the core mechanism of zero-risk bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't sit there and compare exactly how much risk the flagged window actually removes versus how much schedule damage the reroute causes — it was more that avoiding the zone altogether felt like the safer place to land.",
          "evidence_explanation": "This demonstrates the absence of a marginal risk-reduction versus marginal cost comparison and reliance on the feeling of complete avoidance."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "once I decided I wanted the train out of that zone entirely, the size of the delay became secondary. It's not that I ignored it, I just didn't weigh it against how small the actual exposure through a flagged window normally is.",
          "evidence_explanation": "This shows that the preference for zero exposure made a large known delay secondary, which is a characteristic effect of zero-risk bias."
        }
      ],
      "correction_or_counterevidence": "At the time, the participant denied any specific concern about the flag protection crew or setup. In later reflection he said he might compare the flagged window's actual risk reduction against the full reroute delay more explicitly, but that reflection occurred after the decision and did not alter the original choice.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were available in the analysis input; the label 'zero-risk bias' is assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "ambiguity aversion",
      "alternative_labels": [
        "aversion to ambiguous options",
        "preference for known risk"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to prefer options with known parameters or known probabilities over options with uncertain or ambiguous parameters, even when the ambiguous option may have a better expected outcome.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Trespasser report precaution selection",
      "decision_point_description": "Choice between a fixed ten-minute subdivision-wide restricted-speed order and a shorter or more narrowly scoped restriction while waiting for a clarifying callback from the foreman.",
      "affected_reasoning_operation": "Selection of protective action under uncertainty about report details and train-delay trade-offs",
      "bias_specific_mechanism": "Avoidance of the tailored option because its duration, scope, and possible extension were unknown until a callback, leading to default selection of the fixed protocol with known temporal and geographic boundaries despite likely greater train delay.",
      "manifestation_in_interview": "The participant described the tailored option as open-ended and therefore harder to commit to, and stated that he did not treat the likelihood that the report was benign or serious as a probability question. He defaulted to the fixed protocol because it had a clear shape and known edges.",
      "effect_on_reasoning_or_decision": "The participant imposed a full ten-minute subdivision-wide restriction rather than a potentially shorter and narrower restriction, accepting more delay to queued trains because the standard protocol had known boundaries.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The tailored version might've actually cost the queued trains less time if the callback had come back clean, but I couldn't tell you up front how long that would run or how far the restriction would need to extend, so it felt like the harder thing to commit to in the moment.",
          "evidence_explanation": "This explicitly acknowledges that the ambiguous option could have been lower-cost but was avoided because its parameters were unknown."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It wasn't that I sat down and worked out how likely it was to be nothing versus something worse. It was more that the fixed protocol had a shape I could describe to everyone right away, and the tailored version was open-ended until the callback came through, so I defaulted to the one with the known edges.",
          "evidence_explanation": "This directly contrasts the known-boundary standard protocol with the open-ended tailored option and shows the selection was driven by ambiguity avoidance, not probability-based expected-cost reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really as a probability question, no.",
          "evidence_explanation": "In response to a direct question about whether he weighed the probabilities of the report being benign or serious, the participant confirms that he did not engage in probabilistic comparison."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction or debiasing action occurred. In a later counterfactual, the participant said that if the foreman's report had clearly confirmed one person already left the area, he probably would have chosen the tailored shorter restriction, which supports the interpretation that ambiguity about the report drove the original choice.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were available in the analysis input; the label 'ambiguity aversion' is assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "normalcy bias",
      "alternative_labels": [
        "availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Hot-box detector response after elevated bearing reading",
      "supporting_interview_quote": "I've made calls like that before and they've resolved fine most of the time.",
      "plausible_mechanism": "The participant may have underestimated the current elevated bearing reading because similar past events resolved without incident, or because benign outcomes were more available in memory.",
      "why_not_identified": "The decision was explicitly anchored to the mandatory threshold table and the absence of other crew-reported symptoms, and the participant said a near-threshold reading would have led to a physical inspection. The recall statement is suggestive but does not provide sufficient affirmative evidence that a bias mechanism materially affected the hot-box decision."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided to the analyzer, so corpus_evidence arrays are empty and named labels rely on general cognitive-science knowledge.",
    "The analysis is based solely on the participant's self-reported reasoning and may not capture all internal cognitive processes."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Biased_2_Sonnet_off",
  "interview_id": "RT_Biased_2",
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
