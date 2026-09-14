You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations research file — nothing here goes into a disciplinary record, and you can decline any question. Are you good to proceed?

**Participant:** Yeah, that's fine. I figured I'd get a call about this run eventually.

**Interviewer:** Can you start by telling me your role and roughly what a normal night looks like on this route?

**Participant:** Sure. I'm the engineer, so I'm running the power, handling speed and braking, working the radio with the dispatcher. I've had this territory for about eleven years now. It's single track most of the way, so timing matters — you've got meets scheduled at sidings, and if you're late getting into the hole, you can back up traffic for an hour or more. That night I had a loaded manifest train, mixed freight, heading toward a meet at a siding we needed to clear before an opposing train showed up.

**Interviewer:** Walk me through what happened that night, from the top.

**Participant:** Everything was normal to start. Light rain, some fog building up later, but nothing unusual for that time of year. We were running close to on time. About forty minutes in, we passed a wayside detector and got the automated call — hot bearing alarm, didn't specify which axle exactly, just flagged the train. Now, that particular detector, I want to say it's given us grief before. I know of at least two times in the last six months it flagged something in wet weather that turned out to be nothing — sensor drift, is what maintenance called it. So when I heard the alarm, my first thought was, here we go again, same detector, same kind of weather.

**Interviewer:** What did you do at that point?

**Participant:** I looked for anything from the cab — smoke, sparks, smell — didn't see or smell a thing. Told the dispatcher we copied the alarm, and honestly, I treated it as almost certainly another false trip. I kept the train moving at track speed.

**Interviewer:** Did you consider asking the dispatcher or the car department to check which car or axle had triggered it?

**Participant:** I could have. The information's usually gettable if you push for it. I just didn't think it would've changed anything in the moment — no visible symptoms, detector's flaky in the rain, so I didn't request the breakdown. Dispatcher didn't have it handy either when I asked in passing.

**Interviewer:** Let's move ahead. What happened as you approached the meet window?

**Participant:** So now I'm coming up on the point where I either need to get moving to make the siding in time, or I lose the slot and sit. No further alarms since the first one. My normal practice on this run, when nothing's confirmed wrong, is to just keep the plan as built — that's what I did. I kept us on the standing plan, didn't change speed or add a stop.

**Interviewer:** Was there anything else going on around that time?

**Participant:** The conductor mentioned the ride felt a little rough through one stretch, but he chalked it up to rail joints — we've got some known joint conditions in that section, nothing new. I did have him do a rolling check from his side window at the next spot where visibility was decent, just to cover myself on that first alarm. Didn't see anything.

**Interviewer:** Why the rolling check specifically, rather than, say, slowing down more broadly or calling the car department?

**Participant:** It felt like the right-sized response. It let me say I'd actually looked at something, rather than just sitting on the alarm and hoping. Once he told me there was no smoke, no sparks, nothing glowing on that car, I figured whatever the immediate danger was, it was covered — even though, strictly speaking, the original alarm itself was never actually resolved one way or the other. Slowing the whole train down or getting into it with the car department over the radio — that's a bigger step, and I didn't think the situation called for it yet.

**Interviewer:** Did you make the meet?

**Participant:** Yeah, cleared it with a few minutes to spare.

**Interviewer:** Then the second detector came into play. Tell me about that.

**Participant:** About twenty-two miles further on, second detector, independent from the first, flags a hot bearing alarm again — and this one specified roughly the same car position as before. Fog's thicker by then. Around the same time, dispatcher radios that the corridor's on-time numbers have been under review this month, so there's that in the back of my mind too.

**Interviewer:** How did you interpret the second alarm?

**Participant:** Honestly, I leaned on what I've seen over the years. In eleven years running this territory, almost every hot-box call from these wet-weather detectors has turned out to be nothing. So two alarms from detectors with that reputation — to me that still read as consistent with the pattern I already knew, not as something new and urgent. I didn't weight it much differently than the first one.

**Interviewer:** What did you decide to do?

**Participant:** Kept going to the next station stop rather than calling for an inspection right then.

**Interviewer:** Looking back, why do you think you didn't stop after that second alarm?

**Participant:** If I'm honest, I felt kind of boxed in that night — the dispatcher had just brought up the on-time scrutiny, and a full walking inspection eats twenty, thirty minutes easy, plus coordination, and on top of that these detectors just aren't reliable in this weather, that's well known on this line. Between the schedule sitting on me and detectors that cry wolf, it didn't feel like there was much room to do anything different. I guess if I really think about it, I did also just go with my own read that it probably wasn't anything, and I didn't push back on that read the way I maybe could have.

**Interviewer:** What happened next?

**Participant:** About eight miles past that second alarm, conductor calls up and says he's smelling something acrid from the trailing end of the train. That got my attention right away.

**Interviewer:** What did you do?

**Participant:** Made an emergency radio call to the dispatcher, requested an unscheduled stop immediately.

**Interviewer:** At that point, what was going through your mind — what made you decide to stop when you did?

**Participant:** The smell, mainly. That's a real, physical thing happening right then, not an automated call that might be a sensor glitch. That's what pushed me to stop.

**Interviewer:** By the time the smell came in, had the two earlier alarms already sort of faded from your mind, just because they'd happened a while back?

**Participant:** Yeah, honestly, kind of. They were still in there somewhere, but they'd happened miles ago at that point and nothing had come of them yet, so they weren't really front and center anymore. The smell was just what was right in front of me at that moment.

**Interviewer:** How much did the two earlier alarms factor into that decision, compared to the smell?

**Participant:** They were there, sure, in the back of my head. But honestly the smell is what did it. The alarms were a ways back by then, and like I said, they hadn't led anywhere before.

**Interviewer:** What did the inspection find?

**Participant:** Car department found an overheated wheel bearing on the flagged car — hadn't failed, but it needed to be set out right there. Turned out it had actually been logged as a watch item at the previous terminal, but that flag never got relayed to us.

**Interviewer:** If the second detector hadn't gone off at all, do you think you'd have handled the rest of the trip differently?

**Participant:** Probably not that differently, honestly. Without a second alarm, I likely would've just kept going the same way I did after the first one, until something more obvious showed up.

**Interviewer:** Looking back now, how would you weigh the two alarms against the smell, in terms of what actually mattered?

**Participant:** I still think the smell was the deciding piece. The alarms gave some warning, I'll grant that, but they'd cried wolf enough times before that I didn't put much stock in them until there was something undeniable.

**Interviewer:** If schedule pressure hadn't been part of the picture that night, do you think your decisions after the second alarm would have gone differently?

**Participant:** Maybe. Without the on-time conversation with the dispatcher sitting there, I might've been quicker to call for a look. But that pressure was real, and it's a normal part of the job on this territory.

**Interviewer:** Anything else you'd want a fresh crew to know if they saw this same pattern of alarms come up?

**Participant:** Just that these detectors do throw false alarms in wet weather, so I get why people read it that way. But I'd tell them two hits on the same car position is worth more than we probably gave it credit for that night.

**Interviewer:** That's helpful. I think that covers what I need — thanks for walking through it in this much detail.

**Participant:** No problem. Glad it didn't end up worse than a set-out.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Biased_6",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Locomotive Engineer / Train Driver",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Second Detector: A Hot-Box Alarm on the Overnight Manifest Run",
    "scenario_summary_internal": "A locomotive engineer operating a loaded freight manifest train on an overnight run receives an intermittent hot-bearing (hot-box) detector alarm from a wayside defect detector. Weather is deteriorating (fog, light rain), the train is on a tight schedule to clear a single-track siding before an opposing train's meet window, and the engineer has a history of false alarms from that particular detector. Over the course of four decision points, the engineer must decide how to interpret the initial alarm, whether to maintain the operating plan, how to weigh a second confirming detector alarm further down the line, and when/whether to make an emergency stop for a hands-on inspection before a wheel or bearing failure could cause a derailment.",
    "occupational_realism": {
      "objective": "Move the loaded manifest train safely and on schedule to clear the single-track siding before the opposing train's meet window, while responding appropriately to wayside defect detector alerts indicating a possible hot bearing or overheated wheel.",
      "setting": "Overnight freight operation on a single-track mainline with automated wayside hot-box/hot-wheel detectors spaced roughly 20-25 miles apart, deteriorating weather (fog and light rain), radio dispatch contact intermittent due to terrain.",
      "constraints": [
        "Single-track territory with a scheduled meet at a siding; a delay risks fouling the meet window and holding the opposing train.",
        "Detector at milepost in question has a documented history of intermittent false alarms in wet weather.",
        "Limited visibility from the cab due to fog and rain reduces the value of a rolling visual inspection.",
        "Full emergency stop for a walking inspection requires roughly 20-30 minutes and radio coordination with the dispatcher.",
        "Crew consists of the engineer and one conductor; only the conductor can perform the trackside walking inspection."
      ],
      "stakeholders": [
        "Train dispatcher (rail traffic control)",
        "Conductor (train crew)",
        "Opposing train crew awaiting the meet",
        "Mechanical/car department (bearing and wheel maintenance)",
        "Railroad safety and compliance office"
      ],
      "technical_terms_to_use": [
        "hot-box detector",
        "wayside defect detector (WDD)",
        "hot bearing/hot wheel alarm",
        "restricted speed",
        "train dispatcher / rail traffic control",
        "meet point / siding",
        "consist",
        "axle count / car placement",
        "emergency application",
        "walking inspection"
      ],
      "technical_terms_to_avoid": [
        "positive train control override codes",
        "specific proprietary detector brand names",
        "signal aspect terminology beyond basic stop/proceed/restricted"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Automated radio message reports a hot bearing/hot wheel alarm on an unspecified axle as the train passes a wayside detector.",
          "This particular detector has triggered at least two known false alarms in the past six months, both attributed to wet-weather sensor drift.",
          "Current weather is light rain; conditions match the profile of prior false alarms.",
          "The train is running roughly on time toward the meet window."
        ],
        "new_information_after_decision": [
          "No visible smoke, sparks, or odor detected from the cab during the alarm segment.",
          "The dispatcher acknowledges the alarm but has no additional detector history immediately on hand."
        ],
        "alternatives": [
          "Treat the alarm as indeterminate, reduce speed, and request the dispatcher check the axle/car count and any maintenance flags before proceeding further.",
          "Treat the alarm as a likely false positive given detector history and continue at authorized track speed without further verification.",
          "Stop immediately and hold for a full walking inspection before proceeding at all."
        ],
        "intended_action": "The engineer classifies the alarm as almost certainly a false positive based on the detector's prior track record and continues at track speed without requesting axle-level confirmation from the dispatcher or car department."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The train is now approaching the point where it must either accelerate to make the meet window on schedule or lose the slot and hold at a prior siding.",
          "No further alarms have occurred since milepost of the first detector.",
          "The engineer's normal practice on this run is to maintain the standard operating plan absent a confirmed defect."
        ],
        "new_information_after_decision": [
          "The conductor mentions, in passing, having felt a slightly rougher ride on one section of track, but attributes it to known rail joint conditions.",
          "The train clears the meet window with a few minutes to spare."
        ],
        "alternatives": [
          "Deviate from the standard plan by ordering a brief speed reduction and a rolling visual check from the conductor's side window at the next favorable location, even without a new alarm.",
          "Continue with the standing operating plan exactly as before, treating the absence of further alarms as sufficient reassurance.",
          "Contact the car department directly to ask whether the specific axle/car has any open maintenance history before proceeding to the next detector."
        ],
        "intended_action": "The engineer defaults to the standing operating plan without modification, and separately elects to satisfy any residual concern by having the conductor perform only a quick rolling visual check of that one car at the next opportunity, rather than addressing the broader uncertainty about the axle's condition at speed."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A second, independent wayside detector approximately 22 miles further down the line also flags a hot bearing/hot wheel alarm, this time specifying the same general car position as the first alarm.",
          "Weather has worsened slightly; fog now limits visibility further.",
          "The dispatcher radios that the railroad's on-time performance metrics for this corridor have been under scrutiny this month.",
          "The engineer recalls that in over a decade of service, almost every hot-box alarm on this route from wet-weather-prone detectors turned out to be a false alarm."
        ],
        "new_information_after_decision": [
          "The train proceeds for another 8 miles before the conductor reports smelling something acrid from the trailing end of the train.",
          "An emergency radio call is made to the dispatcher requesting an unscheduled stop."
        ],
        "alternatives": [
          "Treat the second alarm at the same car position as materially new evidence warranting an immediate stop and walking inspection, regardless of schedule pressure.",
          "Continue to the next station stop, reasoning that two alarms from historically unreliable detectors do not yet outweigh a decade of mostly false positives on this line.",
          "Request the dispatcher hold a following train and arrange for a mobile mechanical inspector to meet the train at the next crossing."
        ],
        "intended_action": "The engineer continues to the next station stop, treating the second alarm as consistent with his long-standing belief that this route's detectors are unreliable, and later attributes the delay in stopping to the dispatcher's schedule pressure and detector unreliability rather than to his own read of the second alarm."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The conductor's report of an acrid smell is the most recent and most vivid piece of information available.",
          "Two prior wayside detector alarms had already flagged the same general car position earlier in the trip.",
          "The train is now past the meet window, so schedule pressure has eased somewhat.",
          "An emergency stop at this point will require a full mechanical inspection before the train can resume."
        ],
        "new_information_after_decision": [
          "The walking inspection finds an overheated wheel bearing on the flagged car, short of failure but requiring the car to be set out.",
          "The car department confirms the bearing had been logged as a watch item at the previous terminal but the flag had not been relayed to the crew."
        ],
        "alternatives": [
          "Order an immediate emergency stop based primarily on the smell just reported, treating it as the decisive signal.",
          "Order an immediate stop based on the cumulative pattern of both detector alarms plus the smell, treating all three as equally weighted evidence.",
          "Request a rolling reduction to restricted speed while continuing toward the next inspection point rather than stopping outright."
        ],
        "intended_action": "The engineer orders an emergency stop, and in the closing interview probes, explains the decision primarily by reference to the smell just reported, giving comparatively little weight in his account to the two earlier detector alarms that had occurred well before."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you were doing and what the operating plan was at the start of this trip?",
        "What was your role and what information sources did you normally rely on during a run like this?"
      ],
      "timeline_reconstruction": [
        "What happened right after the first detector alarm sounded?",
        "What did you do between the first and second detector alarms?",
        "Walk me through what happened once the conductor reported the smell."
      ],
      "decision_point_probes": [
        "At the point of the first alarm, what information did you have, and what did you do with it?",
        "Why did you decide to keep to the standard plan after the first alarm rather than change anything?",
        "When the second alarm came in at the same car position, how did that change or not change your thinking?",
        "What ultimately made you decide to stop the train when you did?",
        "Were there other options you considered at each of these points, and why did you rule them out?"
      ],
      "closing_hypotheticals": [
        "If the second detector had not gone off, do you think you would have handled things differently?",
        "Looking back, how much weight do you think each piece of information deserved in your decision to stop?",
        "If schedule pressure had not been a factor, would your decisions have changed?",
        "How did your past experience with this detector shape how you read the alarms this time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ur_01",
        "bias": "Uncertainty Rejection Bias",
        "decision_point": 1,
        "mechanism": "Engineer resolves the ambiguous, intermittent nature of the first alarm by prematurely committing to a single confident classification (false positive) rather than tolerating the genuine uncertainty and seeking confirming information.",
        "affected_reasoning_operation": "Interpretation of ambiguous sensor evidence",
        "evidence_available_at_time": [
          "Automated alarm with no axle-level detail",
          "Detector's known history of false alarms in wet weather",
          "No visible smoke/sparks from the cab"
        ],
        "required_textual_manifestation": "Engineer explicitly states he treated the alarm as 'almost certainly' a false positive rather than as unresolved, and did not request axle/car confirmation despite it being available from the dispatcher.",
        "plausible_nonbias_interpretation": "A reasonable engineer could deprioritize an axle-confirmation request if operationally it would not have changed the immediate action and no visible symptoms were present.",
        "strength": "subtle",
        "do_not_make_explicit": ["uncertainty rejection", "ambiguity intolerance", "premature closure"]
      },
      {
        "instance_id": "sq_01",
        "bias": "Status quo bias",
        "decision_point": 2,
        "mechanism": "Engineer defaults to the pre-existing standard operating plan without modification, treating the absence of new alarms as sufficient reason to change nothing, even though the operative context (an unresolved earlier alarm) had shifted.",
        "affected_reasoning_operation": "Selection among competing operating plans",
        "evidence_available_at_time": [
          "Unresolved first alarm",
          "Conductor's comment about a rougher ride",
          "Approaching meet window on the standing schedule"
        ],
        "required_textual_manifestation": "Engineer states he kept to 'the plan exactly as before' and treated deviation as something requiring a new alarm, rather than treating the unresolved first alarm as reason enough to adjust.",
        "plausible_nonbias_interpretation": "Sticking to an established, previously safe plan is a legitimate default when no new confirming evidence has appeared.",
        "strength": "subtle",
        "do_not_make_explicit": ["default option", "status quo", "inertia"]
      },
      {
        "instance_id": "zr_01",
        "bias": "Zero-Risk Bias",
        "decision_point": 2,
        "mechanism": "Engineer chooses a narrow, fully-containable action (a quick rolling visual check of one car) that gives a feeling of eliminating a specific worry, while leaving the larger and more consequential residual risk (operating an unverified axle at full track speed) unaddressed.",
        "affected_reasoning_operation": "Evaluation of risk-mitigation options",
        "evidence_available_at_time": [
          "Unresolved first alarm",
          "Availability of a rolling visual check versus a full speed/inspection change",
          "Time pressure from the meet window"
        ],
        "required_textual_manifestation": "Engineer describes satisfying his concern specifically through the small rolling visual check rather than addressing the broader speed/verification risk, framing the small action as resolving the issue.",
        "plausible_nonbias_interpretation": "A rolling visual check is a normal, low-cost first step that many engineers would take given limited alternatives at speed.",
        "strength": "moderate",
        "do_not_make_explicit": ["zero risk", "risk elimination versus risk reduction"]
      },
      {
        "instance_id": "cs_01",
        "bias": "Conservatism Bias",
        "decision_point": 3,
        "mechanism": "Engineer underweights the new, more specific and confirming second detector alarm at the same car position, updating his belief only marginally from his strong prior (a decade of mostly false alarms) rather than shifting substantially toward the new evidence.",
        "affected_reasoning_operation": "Belief updating in response to new confirming evidence",
        "evidence_available_at_time": [
          "Second independent detector alarm at the same car position",
          "A decade of personal experience with mostly false alarms on this route",
          "Worsening weather/visibility"
        ],
        "required_textual_manifestation": "Engineer explicitly compares the new alarm to his long history of false alarms and describes continuing largely unchanged in belief and action despite the second, more specific alarm.",
        "plausible_nonbias_interpretation": "Placing substantial weight on a long, personally observed track record is a defensible use of experience-based judgment.",
        "strength": "moderate",
        "do_not_make_explicit": ["conservatism", "insufficient belief updating", "anchoring on prior"]
      },
      {
        "instance_id": "ss_01",
        "bias": "Self-serving Bias",
        "decision_point": 3,
        "mechanism": "When explaining why he did not stop sooner after the second alarm, the engineer attributes the delay to external factors (dispatcher schedule pressure, detector unreliability) rather than to his own interpretation of the evidence, protecting his own competence narrative.",
        "affected_reasoning_operation": "Causal attribution for a suboptimal delay",
        "evidence_available_at_time": [
          "Dispatcher's comment about on-time performance scrutiny",
          "Engineer's own decision not to stop after the second alarm",
          "Detector's prior unreliability"
        ],
        "required_textual_manifestation": "In the decision-basis or hypothetical probe response, the engineer credits schedule pressure and detector unreliability for the delay, without acknowledging his own read of the second alarm as a contributing factor.",
        "plausible_nonbias_interpretation": "Schedule pressure and known detector unreliability are genuine contextual factors that legitimately influenced the situation.",
        "strength": "subtle",
        "do_not_make_explicit": ["self-serving", "external attribution", "ego protection"]
      },
      {
        "instance_id": "re_01",
        "bias": "Recency effect",
        "decision_point": 4,
        "mechanism": "When asked what drove the final stop decision, the engineer's account gives outsized weight to the most recently received cue (the conductor's report of a smell) and comparatively little weight to the two earlier detector alarms that were temporally more distant, despite all three being relevant evidence.",
        "affected_reasoning_operation": "Retrospective weighting of cues in explaining a decision",
        "evidence_available_at_time": [
          "Conductor's just-reported acrid smell",
          "First detector alarm (temporally distant)",
          "Second detector alarm (temporally distant)"
        ],
        "required_textual_manifestation": "In the closing probe about what 'ultimately made' him stop, the engineer's explanation centers on the smell and mentions the two earlier alarms only briefly or as background, not as co-equal drivers.",
        "plausible_nonbias_interpretation": "A strong, unambiguous sensory cue like a smell is legitimately a more decisive trigger for an emergency stop than an earlier ambiguous automated alarm.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "recency-weighted recall"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable to this biased-condition scenario."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable (no counterfactual condition requested for this scenario ID)",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable",
      "causal_test_question": "Not applicable"
    },
    "generation_checks": [
      "Confirm exactly 6 intended bias instances are embedded, one per manifest entry, with no duplicates or substitutions.",
      "Confirm exactly 4 decision points, each with at least two plausible alternatives.",
      "Confirm no decision point contains two instances of the same named bias.",
      "Confirm each instance has a distinct evidence source or reasoning operation from any other instance of a different bias sharing its decision point.",
      "Confirm bias labels, definitions, or explicit psychological terminology are absent from the public interview text.",
      "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given the timeline and probe density.",
      "Confirm consequences described (bearing found overheated but not failed) do not mechanically prove or disprove bias, preserving interpretive ambiguity for validators."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Recency effect",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Self-serving Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Status quo bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Uncertainty Rejection Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Zero-Risk Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Conservatism Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Recency effect",
      "Self-serving Bias",
      "Status quo bias",
      "Uncertainty Rejection Bias",
      "Zero-Risk Bias",
      "Conservatism Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Recency effect", "requested_occurrences": 1 },
      { "bias": "Self-serving Bias", "requested_occurrences": 1 },
      { "bias": "Status quo bias", "requested_occurrences": 1 },
      { "bias": "Uncertainty Rejection Bias", "requested_occurrences": 1 },
      { "bias": "Zero-Risk Bias", "requested_occurrences": 1 },
      { "bias": "Conservatism Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "ur_01", "bias": "Uncertainty Rejection Bias" },
      { "instance_id": "sq_01", "bias": "Status quo bias" },
      { "instance_id": "zr_01", "bias": "Zero-Risk Bias" },
      { "instance_id": "cs_01", "bias": "Conservatism Bias" },
      { "instance_id": "ss_01", "bias": "Self-serving Bias" },
      { "instance_id": "re_01", "bias": "Recency effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "ur_01", "bias": "Uncertainty Rejection Bias", "decision_point": 1 },
      { "instance_id": "sq_01", "bias": "Status quo bias", "decision_point": 2 },
      { "instance_id": "zr_01", "bias": "Zero-Risk Bias", "decision_point": 2 },
      { "instance_id": "cs_01", "bias": "Conservatism Bias", "decision_point": 3 },
      { "instance_id": "ss_01", "bias": "Self-serving Bias", "decision_point": 3 },
      { "instance_id": "re_01", "bias": "Recency effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ur_01",
        "bias": "Uncertainty Rejection Bias",
        "mechanism": "Premature resolution of ambiguous alarm evidence into a confident false-positive classification without seeking available confirming information.",
        "affected_reasoning_operation": "Interpretation of ambiguous sensor evidence",
        "evidence_source": "First wayside detector alarm plus detector history",
        "distinctiveness_requirement": "Must be tied specifically to the unresolved, ambiguous status of the first alarm at decision point 1, not to any later confirmed or repeated alarm."
      },
      {
        "instance_id": "sq_01",
        "bias": "Status quo bias",
        "mechanism": "Default preference for the pre-existing standard operating plan over any plan modification, absent a change requirement being self-imposed.",
        "affected_reasoning_operation": "Selection among competing operating plans",
        "evidence_source": "Standing operating plan and schedule at decision point 2",
        "distinctiveness_requirement": "Must concern the choice to keep the overall plan unchanged, distinct from the separate zero-risk-motivated micro-action (zr_01) evaluated at the same decision point."
      },
      {
        "instance_id": "zr_01",
        "bias": "Zero-Risk Bias",
        "mechanism": "Preference for a small action that feels like it fully eliminates a narrow risk, over a larger action that would more meaningfully reduce overall residual risk.",
        "affected_reasoning_operation": "Evaluation of risk-mitigation options",
        "evidence_source": "Choice between rolling visual check versus broader speed/verification change at decision point 2",
        "distinctiveness_requirement": "Must concern the risk-mitigation option evaluation specifically, distinct from the plan-continuation reasoning captured by sq_01."
      },
      {
        "instance_id": "cs_01",
        "bias": "Conservatism Bias",
        "mechanism": "Insufficient updating of belief toward new, more specific confirming evidence (second alarm at same car) relative to a long-held prior belief.",
        "affected_reasoning_operation": "Belief updating in response to new confirming evidence",
        "evidence_source": "Second wayside detector alarm at decision point 3",
        "distinctiveness_requirement": "Must be expressed as an evidence-weighting/belief-update failure, distinct from the causal-attribution reasoning captured by ss_01 at the same decision point."
      },
      {
        "instance_id": "ss_01",
        "bias": "Self-serving Bias",
        "mechanism": "Attribution of the delay in stopping to external factors (schedule pressure, detector unreliability) rather than to the engineer's own evidentiary judgment.",
        "affected_reasoning_operation": "Causal attribution for a suboptimal delay",
        "evidence_source": "Dispatcher's schedule-pressure comment at decision point 3",
        "distinctiveness_requirement": "Must be expressed as an attribution-of-cause statement, distinct from the evidence-weighting failure captured by cs_01 at the same decision point."
      },
      {
        "instance_id": "re_01",
        "bias": "Recency effect",
        "mechanism": "Overweighting of the most recently received cue (smell report) relative to earlier, temporally distant cues (two detector alarms) when retrospectively explaining the final decision.",
        "affected_reasoning_operation": "Retrospective weighting of cues in explaining a decision",
        "evidence_source": "Conductor's smell report versus two earlier detector alarms at decision point 4",
        "distinctiveness_requirement": "Must be located in the retrospective explanation probe at decision point 4, not in the earlier decision points where the alarms first occurred."
      }
    ],
    "intended_strength": [
      { "instance_id": "ur_01", "bias": "Uncertainty Rejection Bias", "strength": "subtle" },
      { "instance_id": "sq_01", "bias": "Status quo bias", "strength": "subtle" },
      { "instance_id": "zr_01", "bias": "Zero-Risk Bias", "strength": "moderate" },
      { "instance_id": "cs_01", "bias": "Conservatism Bias", "strength": "moderate" },
      { "instance_id": "ss_01", "bias": "Self-serving Bias", "strength": "subtle" },
      { "instance_id": "re_01", "bias": "Recency effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "RT_Biased_6",
    "domain_id": "RT",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Automatic allocation: one instance per manifest bias, spread across 4 decision points by mechanism fit and narrative chronology; decision points 2 and 3 each host two distinct biases with clearly separated evidence sources and reasoning operations, per rules 1-4 of the allocation guidance.",
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
          "segment_type": "decision_point_1_alarm_interpretation",
          "raw_interview_anchor": "I treated it as almost certainly another false trip. I kept the train moving at track speed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ur_01"
          ],
          "ground_truth_rationale": "The first alarm is prematurely resolved as a false positive despite genuine ambiguity."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_point_2_plan_continuation",
          "raw_interview_anchor": "My normal practice on this run, when nothing's confirmed wrong, is to just keep the plan as built - that's what I did. I kept us on the standing plan, didn't change speed or add a stop.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sq_01"
          ],
          "ground_truth_rationale": "The standing plan is retained despite the unresolved alarm."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "decision_point_2_risk_mitigation_choice",
          "raw_interview_anchor": "It felt like the right-sized response. It let me say I'd actually looked at something... Once he told me there was no smoke, no sparks, nothing glowing on that car, I figured whatever the immediate danger was, it was covered.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "zr_01"
          ],
          "ground_truth_rationale": "A narrow rolling check is treated as covering the immediate risk while larger residual risk remains."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_point_3_second_alarm_evidence_weighting",
          "raw_interview_anchor": "So two alarms from detectors with that reputation - to me that still read as consistent with the pattern I already knew, not as something new and urgent. I didn't weight it much differently than the first one.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cs_01"
          ],
          "ground_truth_rationale": "The second independent same-position alarm receives insufficient updating relative to the false-alarm prior."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "decision_point_3_causal_attribution",
          "raw_interview_anchor": "I felt kind of boxed in that night - the dispatcher had just brought up the on-time scrutiny... Between the schedule sitting on me and detectors that cry wolf, it didn't feel like there was much room to do anything different.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ss_01"
          ],
          "ground_truth_rationale": "The delay is attributed to external pressure and detector unreliability."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "decision_point_4_retrospective_cue_weighting",
          "raw_interview_anchor": "They were still in there somewhere, but they'd happened miles ago at that point and nothing had come of them yet, so they weren't really front and center anymore. The smell was just what was right in front of me at that moment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "re_01"
          ],
          "ground_truth_rationale": "The recent smell is overweighted over the two earlier alarms."
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
    "analysis_scope_note": "Conservative mechanism-first analysis. Only bias-specific mechanisms affirmatively evidenced in the Participant's reasoning are reported; interviewer questions and retrospective outcome information are not treated as bias evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Expectation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Expectation bias",
      "alternative_labels": [
        "Confirmation bias",
        "Selective perception"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive or interpret a situation as matching a pre-existing expectation, giving insufficient weight to conflicting cues.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of hot-bearing detector alarms",
      "decision_point_description": "After the second independent detector flagged a hot bearing at roughly the same car position, he classified it as another likely false alarm rather than as corroborating evidence.",
      "affected_reasoning_operation": "Interpretation of automated warning cues under uncertainty",
      "bias_specific_mechanism": "A pre-existing expectancy that wet-weather detector alarms are false alarms caused the Participant to encode the second independent same-car alarm as fitting the known false-alarm pattern and to underweight its novelty and corroborative value.",
      "manifestation_in_interview": "The Participant described the first alarm as 'same detector, same kind of weather' and said the two alarms still read as consistent with the pattern he already knew rather than as something new and urgent.",
      "effect_on_reasoning_or_decision": "He maintained track speed and did not request inspection after the first or second alarm, delaying detection until a physical smell appeared.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I know of at least two times in the last six months it flagged something in wet weather that turned out to be nothing — sensor drift, is what maintenance called it. So when I heard the alarm, my first thought was, here we go again, same detector, same kind of weather.",
          "evidence_explanation": "Shows the expectancy was activated by the first alarm and shaped his initial interpretation before further investigation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In eleven years running this territory, almost every hot-box call from these wet-weather detectors has turned out to be nothing. So two alarms from detectors with that reputation — to me that still read as consistent with the pattern I already knew, not as something new and urgent.",
          "evidence_explanation": "Shows the same expectancy persisted and dominated interpretation of the second independent alarm, which should have been treated as partly disconfirming the false-alarm hypothesis."
        }
      ],
      "correction_or_counterevidence": "He did request a rolling visual check after the first alarm and later made an emergency stop once a physical smell appeared; however, the intervening interpretation of the alarms was still shaped by the prior false-alarm expectation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The report outlines that the expectation bias  outweighed other available conflicting cues.",
          "mechanism_supported_by_source": "The passage identifies expectation bias as operating when a pre-existing expectation outweighs conflicting cues.",
          "relevance_to_this_occurrence": "It supports classifying the Participant's interpretation of the alarms as expectation bias because his prior expectation of unreliable wet-weather detectors outweighed the conflicting new alarm evidence."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Get-there-itis",
        "Continuation bias",
        "Plan continuation error"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an original course of action or plan despite new or accumulating evidence indicating that the plan should be revised or reconsidered.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to continue the planned movement rather than stop or inspect after detector alarms",
      "decision_point_description": "After the first and again after the second corroborating hot-bearing alarm, he kept the train moving under the original plan instead of stopping or requesting an inspection.",
      "affected_reasoning_operation": "Plan revision versus plan persistence under anomalous cues",
      "bias_specific_mechanism": "The existing plan of maintaining track speed and making the meet was treated as the default; anomalous cues from the first and second alarms did not lead to plan revision, and schedule pressure reinforced staying on the original plan.",
      "manifestation_in_interview": "He explicitly stated that his normal practice when nothing is confirmed wrong is to keep the plan as built, and after the second alarm he kept going to the next station stop rather than calling for an inspection.",
      "effect_on_reasoning_or_decision": "The train continued at speed after both warnings, delaying an inspection until a physical smell was noticed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I kept the train moving at track speed.",
          "evidence_explanation": "Shows the initial decision to continue the plan after the first alarm."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My normal practice on this run, when nothing's confirmed wrong, is to just keep the plan as built — that's what I did. I kept us on the standing plan, didn't change speed or add a stop.",
          "evidence_explanation": "Shows explicit reliance on the standing plan as the default response to unresolved abnormalities."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Kept going to the next station stop rather than calling for an inspection right then.",
          "evidence_explanation": "Shows persistence with the original plan after the second independent alarm made the abnormality harder to dismiss."
        }
      ],
      "correction_or_counterevidence": "He did request a rolling visual check and eventually made an emergency stop when the smell provided a strong physical cue; however, the earlier decisions after the alarms reflect the continuation bias.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Research carried out by Boeing  accidents be tween 2011 of accidents during the same period. during the final phases of flight evidence to support this finding. This  continuation bias, in that it appears to occur in frequently during runway excursions on landing, after longer duties and at the latter stages of flight.",
          "mechanism_supported_by_source": "The passage links plan continuation bias to persisting with the original plan during later phases of flight despite emerging risk.",
          "relevance_to_this_occurrence": "Supports the classification because the Participant persisted with his original rail movement plan after accumulating hot-bearing alarm cues and schedule pressure."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory information-seeking"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, attend to, or interpret information in ways that confirm one's existing hypothesis, while giving insufficient weight to information that could falsify it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Rolling visual check after first hot-bearing alarm",
      "decision_point_description": "He used a brief rolling visual check for smoke and sparks and treated its negative result as covering the unresolved hot-bearing alarm.",
      "affected_reasoning_operation": "Verification and interpretation of safety-critical diagnostic information",
      "bias_specific_mechanism": "He sought and overweighted visible signs that would confirm his false-alarm hypothesis, such as the absence of smoke, sparks, or glow, and interpreted that absence as sufficient evidence of safety even though the automated alarm was not resolved and an internal bearing condition could remain undetected visually.",
      "manifestation_in_interview": "He described the rolling check as 'right-sized' and as letting him say he had actually looked at something, then concluded the immediate danger was covered even though the original alarm was never resolved.",
      "effect_on_reasoning_or_decision": "It reinforced the choice to continue without further slowing or inspection by providing a subjective sense that the alarm had been checked adequately.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I did have him do a rolling check from his side window at the next spot where visibility was decent, just to cover myself on that first alarm.",
          "evidence_explanation": "Shows the check was motivated by confirming the preferred false-alarm account rather than by a falsifying diagnostic test."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once he told me there was no smoke, no sparks, nothing glowing on that car, I figured whatever the immediate danger was, it was covered — even though, strictly speaking, the original alarm itself was never actually resolved one way or the other.",
          "evidence_explanation": "Demonstrates that absence of visible external signs was weighted as sufficient to disconfirm a hot-bearing alarm despite the alarm remaining unresolved."
        }
      ],
      "correction_or_counterevidence": "The Participant immediately acknowledged that the original alarm had not been resolved, which means he retained metacognitive awareness, but this did not prevent the confirmation-based conclusion from affecting the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage provided a mechanism-level account of confirmation bias; the label is applied from widely established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring and adjustment heuristic",
        "Insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial assessment and to adjust insufficiently from it in response to new evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reassessment after second independent detector alarm",
      "decision_point_description": "When the second independent detector flagged a hot bearing at roughly the same car position, he did not materially revise his initial false-alarm assessment.",
      "affected_reasoning_operation": "Updating a prior diagnosis or probability judgment with new evidence",
      "bias_specific_mechanism": "The initial assessment of the first alarm as 'almost certainly another false trip' served as an anchor; a later independent detector alarm at roughly the same car position was treated as insufficient reason to adjust that initial assessment.",
      "manifestation_in_interview": "The Participant stated that after the first alarm he treated it as 'almost certainly another false trip,' and after the second independent alarm he 'didn't weight it much differently than the first one.'",
      "effect_on_reasoning_or_decision": "He kept going to the next station stop rather than calling for an inspection, because the second alarm was not treated as materially increasing the likelihood of a real hot bearing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I treated it as almost certainly another false trip.",
          "evidence_explanation": "States the initial anchor after the first alarm."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't weight it much differently than the first one.",
          "evidence_explanation": "Shows insufficient adjustment after the second independent alarm."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did also just go with my own read that it probably wasn't anything, and I didn't push back on that read the way I maybe could have.",
          "evidence_explanation": "Metacognitive acknowledgement that he retained the initial read and did not force reconsideration."
        }
      ],
      "correction_or_counterevidence": "He ultimately made an emergency stop after the smell, and in the debrief acknowledged that two hits on the same car position was worth more than he gave it credit for; this recognition came after the decision, not as an adjustment at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Anchoring and Adjustment  The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.” Although the phenomenon was initially described in  of anchoring on initial values when arriving at num estimates, the results have been found to hold in m general cases.",
          "mechanism_supported_by_source": "The passage describes the anchoring-and-adjustment heuristic: estimates are based on an initial answer and later adjustments are typically insufficient, and the phenomenon generalizes beyond purely numeric estimates.",
          "relevance_to_this_occurrence": "Supports the classification of the Participant's failure to materially update his initial false-alarm assessment after the second independent alarm."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Recency effect",
      "alternative_labels": [
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to stop after acrid smell rather than after earlier alarms",
      "supporting_interview_quote": "They were still in there somewhere, but they'd happened miles ago at that point and nothing had come of them yet, so they weren't really front and center anymore. The smell was just what was right in front of me at that moment.",
      "plausible_mechanism": "The more recent and physically salient smell cue may have disproportionately dominated his decision to stop while the earlier alarms were recalled as less important.",
      "why_not_identified": "The smell was an objectively strong and diagnostic signal, and the decision to stop was appropriate; the transcript does not clearly show that recency or availability distorted reasoning rather than reflecting rational cue weighting."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved passages were sparse and partially corrupted; corpus support was used only where it specifically addressed the mechanism.",
    "The analysis is based on a retrospective single-participant account; some statements may include post-hoc rationalization.",
    "Some related mechanisms, such as availability, recency, and normalcy, were considered but did not meet the threshold for identified occurrences."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Biased_6_Sonnet_on",
  "interview_id": "RT_Biased_6",
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
