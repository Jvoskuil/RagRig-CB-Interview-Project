You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. As discussed, this is a routine after-action cognitive task analysis, not an investigation — I want to understand how you processed information during the Ridge Road sortie, not evaluate whether calls were right or wrong. You okay to proceed on that basis?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Can you start with your role that night and what the mission objective was?

Participant: I was the sensor operator on an MQ-9 orbit, tail end of an eight-hour shift. Objective was continuous coverage of Ridge Road, a known resupply corridor near the border, plus a secondary NAI about a klick east. We were watching for vehicle movement, personnel patterns, anything that fit a logistics or cache profile. Weather was rough — haze rolling in and out, so EO was in and out and I was leaning on IR a lot more than usual.

Interviewer: Give me the incident account in your own words — what happened, roughly in order.

Participant: Around 0140 a pickup with a tarped bed stopped at the culvert crossing on Ridge Road. That crossing's not random to me — we'd found a weapons cache linked to a truck at that exact spot about two weeks earlier. So when I saw it stop there, that history was right at the front of my mind. IR showed one warm engine block, no visible weapons, no personnel grouping yet. Truck sat for about six minutes, then left without anybody unloading anything I could see. Nothing more happened at the culvert for the rest of the sortie.

About twenty minutes later the haze got bad enough I switched fully to IR, and I picked up three individuals moving toward a compound maybe 400 meters from the truck stop, carrying long objects — could've been rifles, could've been tools or pipe, IR doesn't give you that resolution. Commander wanted an initial read inside two minutes, so I called it. Later, a wider-angle pass showed what looked like farm equipment near a field close to the compound, and nobody moved back toward the truck or culvert after that.

Then the MIC pulled sortie logs showing that four of the last five nights with vehicle activity near Ridge Road, we'd seen an indirect-fire spike the next day. Commander asked point-blank whether tonight predicted an attack tomorrow. Toward the end, fuel was getting close to bingo, maybe twenty minutes of coverage left, compound had been quiet for about forty minutes, and JTAC wanted a final confidence call on whether to prioritize the compound for a strike package.

Interviewer: Let's rebuild that timeline a bit more precisely. What came first — the sensor cue or the historical context?

Participant: Sensor cue first, always. I saw the truck stop, and within maybe ten seconds I was already thinking about the cache incident. It's the same physical location, so that connection was immediate.

Interviewer: And the order of the other three calls — vehicle sighting, log review, final recommendation?

Participant: Right, in that sequence. Vehicle sighting happened, I gave the weapons read on the personnel, then the MIC did the log pull maybe forty minutes later, and the final compound recommendation came right near bingo fuel, so that was the last call of the night.

Interviewer: Let's go through each of those four moments. Starting with the truck at the culvert — what specifically drove your assessment?

Participant: Honestly, the location did most of the work. I told the MIC to pull the old cache report so we could line it up against tonight. The current picture on its own — one truck, six minutes, nothing offloaded — wasn't much. But given it was the same crossing, I treated it as a probable resupply touch and wanted that comparison front and center before I'd even really processed the fresh footage.

Interviewer: What alternatives did you weigh at that point?

Participant: I could've just logged it as routine traffic, or held the camera longer before deciding anything. I considered holding longer, but the location match made me want to get the historical data moving right away rather than just sitting on it.

Interviewer: Moving to the three individuals with long objects — walk me through that call.

Participant: Two-minute window from the commander, haze had killed my EO, so I'm working IR-only with soft resolution on the objects. What came to mind was a sortie a few months back — a group of three, similar setup, turned into an ambush. That one's stuck with me pretty vividly. So I called the objects as probable weapons and recommended escalating surveillance.

Interviewer: Did you consider the tool or irrigation-pipe possibility before that call?

Participant: Briefly, yeah, but the ambush sortie was the one that jumped to mind fastest, and with the clock running I went with that read. Looking back on it, most of the times we've had people carrying long objects out that stretch of road, it's turned out to be farm tools or irrigation pipe — that's actually the more common thing we log on routine passes. But none of those ordinary cases came to mind for me in the moment; the ambush sortie was just the one that surfaced fastest, so that's what shaped the call.

Interviewer: Third decision point — the log pattern and the commander's question about predicting tomorrow's attack.

Participant: The MIC showed me four of the last five nights lining up — vehicle activity, then fire the next day. That's a pretty strong hit rate from where I sat, and this was the fifth night in a row I'd personally logged it happening. I told the commander I thought it was a reliable indicator.

Interviewer: How did you review the log data itself — did you look at nights that didn't fit the pattern?

Participant: I mostly had the MIC bring up the nights that matched what I already remembered seeing. I didn't specifically go looking for nights with activity but no fire afterward, or fire without activity beforehand. Wasn't really the focus at the time.

Interviewer: And the fact that it was an unusually high streak — four of five — did that factor into how confident you were it would hold?

Participant: If anything it made me more confident. Five nights running with that connection felt like a real pattern taking shape, not a fluke. I told the commander I expected it to hold again the next day.

Interviewer: Last decision point — the final call on the compound with fuel running low.

Participant: JTAC wanted a confidence level for prioritizing it. Compound had been quiet forty minutes, and that wide pass earlier suggested farm tools, not weapons. But I've flown over two hundred sorties in that sector and I've got a solid track record calling cache sites correctly. I gave it high confidence for prioritization based on that experience, plus everything else from the night stacked together.

Interviewer: What's the single piece of evidence that mattered most in that final call?

Participant: My own track record, honestly. I trusted my read of the pattern over the whole night more than any one frame of video.

Interviewer: What actually happened afterward, at each of these points?

Participant: The truck never came back, no cache activity there rest of the shift. Follow-up daytime sortie two days later found nothing at the compound — no cache, no weapons. Turned out the truck and the personnel belonged to a local farming family with an irrigation dispute on that field. And there was no fire event the next day despite the streak.

Interviewer: If the fuel clock and the commander's two-minute request hadn't been there, would you have handled the objects call differently?

Participant: Maybe. I might have pushed for another angle before committing to a read. Time pressure definitely pushed me toward the fastest match I had in memory.

Interviewer: Hypothetically — if that culvert had no history with you, no prior cache, would your first read of the truck have been the same?

Participant: Probably would've logged it as routine and moved on. The history at that spot is what pulled my attention that hard.

Interviewer: If you had no memory of that earlier ambush sortie, would you have described the long objects the same way?

Participant: Probably would've called it ambiguous and asked for another pass rather than committing to weapons.

Interviewer: And if this had been your very first night ever watching this stretch of road, would you have called the vehicle-activity pattern predictive?

Participant: No, I don't think five data points would've meant much to me without having personally watched it build over those nights.

Interviewer: Last one — looking back, what single piece of evidence, weighted differently, would have changed your final recommendation on the compound?

Participant: The wide-angle pass showing farm tools. If I'd let that carry more weight against my own track record, I probably would've recommended holding off rather than prioritizing it.

Interviewer: This has been really useful. Thanks for the detail.

Participant: No problem.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Biased_6",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Unmanned Aircraft System (UAS) Operator / Sensor Operator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Ridge Road Convoy Watch",
    "scenario_summary_internal": "A UAS sensor operator flying an ISR mission over a contested border route is tasked with monitoring a suspected insurgent logistics corridor. Over a multi-hour shift, the operator must decide whether to reposition sensors, escalate a possible hostile vehicle sighting, request strike authorization support, and interpret a pattern of nighttime movement, under time pressure, degraded weather, and fatigue. The scenario is built to elicit six distinct cognitive biases across four decision points without ever naming or explaining them.",
    "occupational_realism": {
      "objective": "Maintain continuous ISR coverage of a suspected insurgent resupply route ('Ridge Road') and provide timely, accurate threat assessments to the ground force commander while conserving fuel/loiter time and avoiding misidentification of civilian traffic.",
      "setting": "MQ-9-class UAS orbiting at medium altitude over a mountainous border corridor at night and into dawn twilight, operator working from a ground control station with a sensor operator seat, full-motion video (FMV), infrared (IR), and a chat-based intelligence feed (mIRC-style).",
      "constraints": [
        "Limited remaining loiter time before fuel bingo forces RTB",
        "Intermittent weather (haze/low cloud) degrading EO sensor performance, forcing reliance on IR",
        "Restrictive rules of engagement requiring positive identification before any strike recommendation",
        "Single sensor operator covering two areas of interest simultaneously",
        "Fatigue from an extended 8-hour shift near its end",
        "Communication lag with the Joint Terminal Attack Controller (JTAC) and ground commander"
      ],
      "stakeholders": [
        "UAS Sensor Operator (interviewee)",
        "UAS Pilot (aircraft control)",
        "Mission Intelligence Coordinator (MIC)",
        "Ground force commander",
        "JTAC",
        "Squadron intelligence analyst reviewing prior sorties"
      ],
      "technical_terms_to_use": [
        "loiter time",
        "positive identification (PID)",
        "pattern of life",
        "full-motion video (FMV)",
        "IR/EO sensor ball",
        "named area of interest (NAI)",
        "bingo fuel",
        "chat feed",
        "JTAC",
        "danger close"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "anchoring",
        "availability heuristic",
        "overconfidence",
        "illusory correlation",
        "regression to the mean",
        "cognitive bias",
        "heuristic"
      ],
      "timeline": [],
      "probe_plan": {},
      "occurrence_embedding_plan_internal": [],
      "control_specification": {},
      "counterfactual_specification": {},
      "generation_checks": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "A single pickup truck with a tarped bed stopped near a known culvert crossing on Ridge Road at 0140 local",
          "Two weeks earlier, a similar truck at the same crossing was later linked to a weapons cache",
          "No radio chatter or grouping of personnel observed yet",
          "IR signature shows one warm engine block, no visible weapons"
        ],
        "new_information_after_decision": [
          "The truck departs after 6 minutes without unloading anything visible",
          "No cache or personnel activity is subsequently detected at that location for the rest of the sortie"
        ],
        "alternatives": [
          "Flag the truck as a high-priority resupply indicator and request the MIC cross-check against the prior cache incident",
          "Log it as routine traffic and continue scanning the broader NAI without elevating priority",
          "Split attention and hold the camera on the truck for an extended dwell before deciding"
        ],
        "intended_action": "Operator immediately treats the stop as a probable resupply event because it happened at the same culvert crossing as the earlier cache discovery, requesting the MIC pull that old report as the primary comparison point."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Weather haze has degraded EO; operator switches to IR",
          "A cluster of three individuals is seen moving toward a compound roughly 400m from the truck stop",
          "The individuals are carrying long objects that could be tools, weapons, or irrigation pipe",
          "Ground force commander asks for an initial read within two minutes"
        ],
        "new_information_after_decision": [
          "A wider-angle pass later shows one individual carrying what appears to be farming equipment near a field",
          "No further movement toward the truck or culvert is observed"
        ],
        "alternatives": [
          "Report the long objects as likely weapons consistent with the earlier resupply read, and recommend continued surveillance escalation",
          "Report the sighting as ambiguous and request additional dwell time or a different sensor angle before characterizing the objects",
          "Cross-check against known agricultural patterns in the area before characterizing the objects"
        ],
        "intended_action": "Operator reports the long objects as probable weapons, drawing on the vivid, easily recalled memory of a recent sortie where a similar three-person group turned out to be an ambush team, while downplaying the less memorable majority of prior sorties where such groups were farmers."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "MIC pulls up sortie logs showing that on 4 of the last 5 nights, vehicle activity near Ridge Road coincided with a spike in indirect fire reports the following day",
          "Tonight's truck-and-personnel activity is the fifth such coincidence the operator has personally logged",
          "No causal link (e.g., cache movement, weapons handoff) has ever been directly observed connecting the traffic to the fire events",
          "Ground commander asks whether tonight's activity predicts an attack tomorrow"
        ],
        "new_information_after_decision": [
          "Squadron intelligence later notes that indirect fire incidents in the area occur on an irregular but frequent baseline schedule regardless of vehicle activity",
          "The following day sees no indirect fire event despite tonight's activity"
        ],
        "alternatives": [
          "Tell the commander the vehicle activity pattern is a reliable predictive indicator of next-day attacks based on the personally observed correlation",
          "Tell the commander the sample is too small and the correlation may be coincidental, recommending it not be treated as predictive without further analysis",
          "Request the intelligence cell run a formal frequency analysis before characterizing any relationship"
        ],
        "intended_action": "Operator asserts that the vehicle activity is a strong, reliable warning indicator for next-day attacks, treating the two co-occurring but likely unrelated event streams as causally linked because they have appeared together several times."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Fuel is approaching bingo, giving roughly 20 minutes of remaining coverage",
          "The compound shows no further suspicious activity for the last 40 minutes",
          "The operator has flown over 200 sorties in this sector and has a strong personal track record of correctly flagging cache sites",
          "JTAC asks for a final confidence assessment on whether the compound should be prioritized for a follow-up strike package"
        ],
        "new_information_after_decision": [
          "A follow-up daytime sortie two days later finds no cache, weapons, or suspicious material at the compound",
          "The truck and personnel are later identified through separate reporting as belonging to a local farming family with a documented irrigation dispute at that field"
        ],
        "alternatives": [
          "Recommend high-confidence prioritization of the compound based on personal experience and the night's combined observations",
          "Recommend a moderate-confidence assessment pending daylight follow-up and additional corroboration before any strike package is built",
          "Recommend deprioritizing the compound and reallocating remaining loiter time to other NAIs"
        ],
        "intended_action": "Operator gives a high-confidence recommendation to prioritize the compound for a strike package, citing personal experience and strong track record as sufficient basis, without adequately weighing the ambiguity of the visual evidence or the negative information from the wider-angle pass."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role and the objective of that sortie?",
        "What was the overall tactical picture on Ridge Road that night?"
      ],
      "timeline_reconstruction": [
        "What did you see first, and what did you do immediately after?",
        "Walk me through the order in which information came in from the sensor feed, the MIC, and the ground commander.",
        "What happened right after each of your four key calls?"
      ],
      "decision_point_probes": [
        "What specific cues on the screen made you characterize the truck stop the way you did?",
        "What sources did you use to compare tonight's activity to prior incidents?",
        "What alternatives did you consider before reporting the long objects as weapons?",
        "Why did the earlier cache incident feel relevant to this stop?",
        "How did you decide the vehicle-activity pattern was predictive of next-day attacks?",
        "What made you confident enough to recommend prioritizing the compound?"
      ],
      "goals": [
        "What were you personally trying to achieve with each report you gave?",
        "How did competing priorities (fuel, dual-NAI coverage) shape what you focused on?"
      ],
      "alternatives": [
        "What other explanations did you consider at each point, and why did you set them aside?"
      ],
      "decision_basis": [
        "What single piece of evidence mattered most to your call, and why?"
      ],
      "prior_experience": [
        "How did past sorties or past incidents at this location influence your read of tonight's activity?"
      ],
      "time_pressure": [
        "How did the fuel clock and the commander's request for a quick answer affect how carefully you weighed the evidence?"
      ],
      "uncertainty": [
        "At each point, how confident were you, and what would have changed that confidence?"
      ],
      "closing_hypotheticals": [
        "If the truck had stopped at a different, unfamiliar location, would your initial read have been different?",
        "If you had no memory of the prior ambush sortie, would you have described the long objects the same way?",
        "If this had been your first night ever watching Ridge Road, would you have called the vehicle-activity pattern predictive?",
        "Looking back, what single piece of evidence, if weighted differently, would have changed your final recommendation?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "AN_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Operator's assessment of the truck stop is anchored to the specific prior cache incident at the same culvert, causing the initial estimate of threat probability to be pulled toward that one reference point rather than updated proportionally to the actually weak current evidence (single vehicle, brief stop, no unloading).",
        "affected_reasoning_operation": "Initial probability estimation / evidence weighting at first sighting",
        "evidence_available_at_time": [
          "Truck stopped 6 minutes, no visible unloading",
          "IR shows one warm engine, no weapons visible",
          "Location matches site of a cache found two weeks prior"
        ],
        "required_textual_manifestation": "Operator explicitly frames the current stop primarily in terms of matching the old cache location, requesting the old report as the main comparison rather than weighing the weak fresh evidence on its own terms.",
        "plausible_nonbias_interpretation": "Checking a location's history is a reasonable investigative step given limited real-time cues.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "reference point", "bias"]
      },
      {
        "instance_id": "AV_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "Operator characterizes ambiguous long objects as weapons because a vivid, recent, and emotionally salient ambush memory comes to mind easily, while the more numerous but less memorable instances of similar groups being farmers are not retrieved or weighted.",
        "affected_reasoning_operation": "Category judgment / recall-based probability estimation for object identification",
        "evidence_available_at_time": [
          "Three individuals moving with long objects toward a compound",
          "IR-only imagery due to haze, ambiguous shape resolution",
          "Two-minute window to give an initial read to the ground commander"
        ],
        "required_textual_manifestation": "Operator explains the weapons call by referencing how memorable/recent the ambush sortie was, without mentioning the base rate of similar groups being non-hostile.",
        "plausible_nonbias_interpretation": "Under time pressure with degraded imagery, defaulting to a cautious threat read is a standard risk-averse heuristic.",
        "strength": "moderate",
        "do_not_make_explicit": ["availability heuristic", "vivid memory", "bias"]
      },
      {
        "instance_id": "IC_01",
        "bias": "Illusory Correlation",
        "decision_point": 3,
        "mechanism": "Operator infers a causal/predictive relationship between nighttime vehicle activity and next-day indirect fire based on a small number of personally observed co-occurrences, without evidence of an actual causal mechanism connecting them or accounting for the base rate of fire events.",
        "affected_reasoning_operation": "Causal attribution / pattern inference from personally logged co-occurrences",
        "evidence_available_at_time": [
          "4 of last 5 nights with vehicle activity coincided with next-day fire reports",
          "No observed handoff, cache movement, or communication linking the two event types",
          "Commander requests a predictive judgment"
        ],
        "required_textual_manifestation": "Operator asserts the vehicle-activity/attack link as reliable based on the personally noticed co-occurrence count, without citing any mechanism connecting the two, and without considering the small sample or baseline attack frequency.",
        "plausible_nonbias_interpretation": "Pattern-of-life analysis based on repeated field observation is a legitimate part of ISR tradecraft.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusory correlation", "base rate", "spurious", "bias"]
      },
      {
        "instance_id": "CB_01",
        "bias": "Confirmation Bias",
        "decision_point": 3,
        "mechanism": "When reviewing the MIC's sortie logs, the operator selectively emphasizes the nights that fit the vehicle-activity/attack narrative (4 of 5) and does not seek out or weight nights with vehicle activity but no subsequent attack, or attacks with no preceding activity, which would test the claimed relationship.",
        "affected_reasoning_operation": "Evidence selection / hypothesis testing when reviewing historical logs",
        "evidence_available_at_time": [
          "MIC-provided sortie logs spanning multiple nights",
          "Operator's own recollection of which nights 'fit' the pattern",
          "Availability of disconfirming nights in the same log set, unexamined"
        ],
        "required_textual_manifestation": "Operator describes pulling and citing only the confirming nights from the log while not mentioning or checking the disconfirming cases, when asked how they reviewed the data.",
        "plausible_nonbias_interpretation": "Time constraints during a live mission can limit how exhaustively logs are reviewed.",
        "strength": "moderate",
        "do_not_make_explicit": ["confirmation bias", "disconfirming evidence", "selective search"]
      },
      {
        "instance_id": "FRM_01",
        "bias": "Failure to recognize regression to the mean",
        "decision_point": 3,
        "mechanism": "Operator treats the unusually high recent coincidence rate (4 of 5 nights) between vehicle activity and fire events as a stable, durable pattern, without recognizing that an unusually high streak is likely to be followed by a return toward the area's normal, lower baseline coincidence rate.",
        "affected_reasoning_operation": "Trend extrapolation / prediction from a short recent streak",
        "evidence_available_at_time": [
          "Recent short streak of 4-of-5 coincidences, described as unusually high",
          "No mention of the longer-run historical baseline rate of coincidence",
          "Commander's request for a next-day prediction"
        ],
        "required_textual_manifestation": "Operator projects that the current high streak will likely continue into tomorrow, without acknowledging that such a strong short-term streak may simply be an unusual cluster likely to normalize.",
        "plausible_nonbias_interpretation": "Recent operational tempo can genuinely shift and persist, so recency weighting is not always wrong.",
        "strength": "subtle",
        "do_not_make_explicit": ["regression to the mean", "streak", "normalize", "bias"]
      },
      {
        "instance_id": "OC_01",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Operator gives a high-confidence strike-priority recommendation based primarily on personal track record and experience, without proportionally discounting confidence for the genuinely ambiguous and partly disconfirming visual evidence (wide-angle farming-tool view, 40 minutes of no further activity).",
        "affected_reasoning_operation": "Confidence calibration when issuing a final recommendation under uncertainty",
        "evidence_available_at_time": [
          "40 minutes of no further suspicious activity at the compound",
          "Earlier wide-angle pass suggesting farming equipment, not weapons",
          "Operator's 200+ prior sorties and strong personal track record",
          "JTAC requesting a final confidence assessment"
        ],
        "required_textual_manifestation": "Operator states high confidence in the strike-priority recommendation, citing personal experience/track record as the main justification, while giving limited weight to the ambiguous and partly contradicting visual evidence gathered later in the sortie.",
        "plausible_nonbias_interpretation": "Experienced operators legitimately develop calibrated intuition that can outperform naive analysis.",
        "strength": "moderate",
        "do_not_make_explicit": ["overconfidence", "miscalibration", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control generated in this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence of prior cache incident at the same culvert location (anchor-establishing history)",
      "original_state": "A cache was found at the same culvert crossing two weeks prior, giving the operator a salient historical anchor",
      "counterfactual_state": "No prior cache incident exists at this location; the culvert crossing has no notable history",
      "variables_to_hold_constant": [
        "Weather and sensor degradation conditions",
        "Fuel/loiter constraints",
        "Number and timing of decision points",
        "Ground commander and JTAC requests",
        "Final outcome facts (farming family, no cache found)"
      ],
      "expected_causal_difference": "Without the prior cache anchor, the operator's initial threat estimate at decision point 1 should be lower and less fixed, potentially reducing the strength of the anchoring-driven framing that carries into later decisions.",
      "causal_test_question": "Does removing the prior cache incident at this location change how strongly the operator anchors the initial threat assessment to that single historical reference point?"
    },
    "generation_checks": [
      "Exactly 4 decision points present, each with at least two alternatives.",
      "Exactly 6 bias instances planned, one per manifest entry, each with a unique instance_id.",
      "No bias term, definition, or explanation appears in probe plan or timeline text.",
      "Each instance tied to a distinct evidence source, decision point, or reasoning operation from other instances of the same bias where applicable (only Confirmation Bias and Illusory Correlation and Failure to recognize regression to the mean share decision point 3, each using distinct evidence-processing operations).",
      "Consequences (farming family identity, no cache found, no next-day attack) are revealed only after decisions and do not mechanically label any decision as biased or correct.",
      "Target word count 1,350 achievable via chronological narrative plus probe responses without repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Overconfidence Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as miscalibrated confidence in a final recommendation despite disconfirming/ambiguous evidence, justified via personal track record."},
      {"bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as reliance on a vivid, easily recalled prior incident rather than base rate of similar events."},
      {"bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as initial estimate pulled toward a specific historical reference point at first sighting."},
      {"bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as selective retrieval/citation of confirming log evidence while omitting disconfirming evidence in the same dataset."},
      {"bias": "Failure to recognize regression to the mean", "occurrences": 1, "mechanism_constraint": "Must manifest as extrapolating an unusually high short-term streak forward without acknowledging likely normalization."},
      {"bias": "Illusory Correlation", "occurrences": 1, "mechanism_constraint": "Must manifest as inferring a causal/predictive link between two co-occurring event types absent any observed mechanism."}
    ],
    "target_bias_names": [
      "Overconfidence Bias",
      "Availability Bias",
      "Anchoring Bias",
      "Confirmation Bias",
      "Failure to recognize regression to the mean",
      "Illusory Correlation"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Overconfidence Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 1},
      {"bias": "Anchoring Bias", "requested_occurrences": 1},
      {"bias": "Confirmation Bias", "requested_occurrences": 1},
      {"bias": "Failure to recognize regression to the mean", "requested_occurrences": 1},
      {"bias": "Illusory Correlation", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "AN_01", "bias": "Anchoring Bias"},
      {"instance_id": "AV_01", "bias": "Availability Bias"},
      {"instance_id": "IC_01", "bias": "Illusory Correlation"},
      {"instance_id": "CB_01", "bias": "Confirmation Bias"},
      {"instance_id": "FRM_01", "bias": "Failure to recognize regression to the mean"},
      {"instance_id": "OC_01", "bias": "Overconfidence Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "AN_01", "bias": "Anchoring Bias", "decision_point": 1},
      {"instance_id": "AV_01", "bias": "Availability Bias", "decision_point": 2},
      {"instance_id": "IC_01", "bias": "Illusory Correlation", "decision_point": 3},
      {"instance_id": "CB_01", "bias": "Confirmation Bias", "decision_point": 3},
      {"instance_id": "FRM_01", "bias": "Failure to recognize regression to the mean", "decision_point": 3},
      {"instance_id": "OC_01", "bias": "Overconfidence Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "AN_01",
        "bias": "Anchoring Bias",
        "mechanism": "Initial threat estimate pulled toward a specific prior cache incident at the same location rather than the weak fresh visual evidence.",
        "affected_reasoning_operation": "Initial probability estimation at first sighting",
        "evidence_source": "Historical incident report for the same culvert crossing",
        "distinctiveness_requirement": "Occurs uniquely at decision point 1, tied to spatial/location anchoring, distinct from all other instances."
      },
      {
        "instance_id": "AV_01",
        "bias": "Availability Bias",
        "mechanism": "Weapons categorization driven by ease of recall of a vivid recent ambush memory, ignoring less memorable non-hostile base rate.",
        "affected_reasoning_operation": "Category judgment for ambiguous long objects",
        "evidence_source": "Recalled memory of a prior ambush sortie vs. current IR imagery",
        "distinctiveness_requirement": "Occurs uniquely at decision point 2, tied to memory salience, distinct from anchoring's location-based mechanism."
      },
      {
        "instance_id": "IC_01",
        "bias": "Illusory Correlation",
        "mechanism": "Causal/predictive link inferred between vehicle activity and next-day fire events from co-occurrence alone, no observed mechanism.",
        "affected_reasoning_operation": "Causal attribution from personally logged co-occurrences",
        "evidence_source": "Operator's personal count of coincidence nights",
        "distinctiveness_requirement": "Focuses on the causal/predictive claim itself, distinct from CB_01's evidence-selection process and FRM_01's trend-extrapolation focus."
      },
      {
        "instance_id": "CB_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective citation of confirming nights from MIC logs while disconfirming nights in the same log set are not sought or weighted.",
        "affected_reasoning_operation": "Evidence selection during historical log review",
        "evidence_source": "MIC-provided multi-night sortie logs",
        "distinctiveness_requirement": "Focuses on the search/retrieval process over the log data, distinct from IC_01's causal inference and FRM_01's streak-extrapolation."
      },
      {
        "instance_id": "FRM_01",
        "bias": "Failure to recognize regression to the mean",
        "mechanism": "Unusually high short-term coincidence streak extrapolated forward as a stable predictor without acknowledging likely normalization.",
        "affected_reasoning_operation": "Trend extrapolation / prediction from a short recent streak",
        "evidence_source": "The 4-of-5-night streak statistic itself",
        "distinctiveness_requirement": "Focuses on the streak's future trajectory, distinct from IC_01's causal-link claim and CB_01's evidence-search behavior, though co-located at decision point 3."
      },
      {
        "instance_id": "OC_01",
        "bias": "Overconfidence Bias",
        "mechanism": "High-confidence final recommendation issued based on personal track record, underweighting ambiguous/disconfirming late-sortie visual evidence.",
        "affected_reasoning_operation": "Confidence calibration for final recommendation",
        "evidence_source": "Operator's self-reported track record and 40 minutes of null activity plus farming-tool visual cue",
        "distinctiveness_requirement": "Occurs uniquely at decision point 4, focused on confidence calibration rather than initial categorization or causal inference."
      }
    ],
    "intended_strength": [
      {"instance_id": "AN_01", "bias": "Anchoring Bias", "strength": "subtle"},
      {"instance_id": "AV_01", "bias": "Availability Bias", "strength": "moderate"},
      {"instance_id": "IC_01", "bias": "Illusory Correlation", "strength": "subtle"},
      {"instance_id": "CB_01", "bias": "Confirmation Bias", "strength": "moderate"},
      {"instance_id": "FRM_01", "bias": "Failure to recognize regression to the mean", "strength": "subtle"},
      {"instance_id": "OC_01", "bias": "Overconfidence Bias", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence of prior cache incident at the culvert crossing (anchor history)",
      "original_state": "A cache was found at the same culvert crossing two weeks prior, serving as a salient anchor",
      "changed_state": "No prior cache incident exists at this location",
      "variables_to_hold_constant": [
        "Weather/sensor degradation",
        "Fuel/loiter constraints",
        "Decision point structure and count",
        "Commander/JTAC request timing",
        "Final ground-truth outcome facts"
      ]
    },
    "scenario_id": "MD_Biased_6",
    "domain_id": "MD",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Automatic assignment per mechanism fit and narrative realism: each bias assigned to the decision point where its cognitive mechanism most naturally arises (initial sighting for anchoring, ambiguous object ID for availability, historical pattern review for confirmation/illusory correlation/regression-failure, final recommendation for overconfidence). Three distinct biases co-located at decision point 3 use different evidence sources and reasoning operations (log-search behavior vs. causal inference vs. trend extrapolation) per rule 4.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Weather/sensor degradation conditions",
      "Fuel/loiter constraints",
      "Decision point count and sequencing",
      "Stakeholder roles and requests",
      "Final outcome/ground-truth facts"
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
        "segment_type": "initial threat assessment and evidence weighting",
        "raw_interview_anchor": "The current picture on its own ... wasn't much. But given it was the same crossing, I treated it as a probable resupply touch and wanted that comparison front and center before I'd even really processed the fresh footage.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["AN_01"],
        "ground_truth_rationale": "The initial truck assessment is pulled toward the prior cache incident at the same location rather than the weak current evidence."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "alternative assessment and monitoring choice",
        "raw_interview_anchor": "I could've just logged it as routine traffic, or held the camera longer before deciding anything.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an explicit consideration of reasonable alternatives without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "ambiguous object classification",
        "raw_interview_anchor": "The ambush sortie was the one that jumped to mind fastest ... most of the times ... it's turned out to be farm tools or irrigation pipe ... that's what shaped the call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["AV_01"],
        "ground_truth_rationale": "A vivid ambush memory drives the weapons classification while more common benign cases are not retrieved or weighted."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "causal and predictive pattern inference",
        "raw_interview_anchor": "That's a pretty strong hit rate from where I sat ... I told the commander I thought it was a reliable indicator.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["IC_01"],
        "ground_truth_rationale": "The participant treats co-occurring vehicle activity and next-day fire as a reliable predictive relationship without an observed causal mechanism."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "historical evidence search and selection",
        "raw_interview_anchor": "I mostly had the MIC bring up the nights that matched what I already remembered seeing. I didn't specifically go looking for nights with activity but no fire afterward, or fire without activity beforehand.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["CB_01"],
        "ground_truth_rationale": "The participant explicitly describes retrieving confirming cases while omitting disconfirming cases from the same log set."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "short-streak extrapolation",
        "raw_interview_anchor": "Five nights running with that connection felt like a real pattern taking shape, not a fluke. I told the commander I expected it to hold again the next day.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["FRM_01"],
        "ground_truth_rationale": "An unusually high short-term streak is projected forward as durable without acknowledging likely normalization."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "final confidence calibration and recommendation",
        "raw_interview_anchor": "I've flown over two hundred sorties ... I've got a solid track record ... I gave it high confidence for prioritization ... My own track record, honestly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["OC_01"],
        "ground_truth_rationale": "The participant gives a high-confidence strike-priority recommendation mainly from personal track record while underweighting contradictory visual and null-activity evidence."
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
    "analysis_scope_note": "Analysis covers four reasoning/decision episodes described by the participant: the truck stop at the culvert, the interpretation of three people carrying long objects, the vehicle-activity/fire-pattern log review, and the final compound prioritization call."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or importance of an event by the ease with which salient examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Truck stop at culvert crossing",
      "decision_point_description": "Whether the pickup at the culvert was a probable resupply touch or routine traffic",
      "affected_reasoning_operation": "Initial classification and probability judgment of an ambiguous vehicle stop",
      "bias_specific_mechanism": "A highly salient prior cache event at the same physical location was immediately retrieved and dominated the participant's inference, causing the ambiguous current observation to be treated as matching that prior example.",
      "manifestation_in_interview": "The participant said the prior cache history was 'right at the front of my mind' and that the location did most of the assessment work before the fresh footage had been fully processed.",
      "effect_on_reasoning_or_decision": "The participant treated a low-information truck stop as a probable resupply touch and initiated a historical cache-report comparison rather than logging it as routine or simply holding the camera longer.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That crossing's not random to me — we'd found a weapons cache linked to a truck at that exact spot about two weeks earlier. So when I saw it stop there, that history was right at the front of my mind.",
          "evidence_explanation": "This shows a salient past event was immediately available and shaped the initial interpretation of the current cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the location did most of the work. I told the MIC to pull the old cache report so we could line it up against tonight. The current picture on its own — one truck, six minutes, nothing offloaded — wasn't much. But given it was the same crossing, I treated it as a probable resupply touch and wanted that comparison front and center before I'd even really processed the fresh footage.",
          "evidence_explanation": "The participant explicitly says the current evidence was weak, but the easily recalled historical case drove the classification and subsequent information request."
        }
      ],
      "correction_or_counterevidence": "The participant noted that he could have logged it as routine traffic or held the camera longer, and he acknowledged the current picture on its own was weak. Later follow-up indicated the truck belonged to a farming family and no cache activity occurred.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derives from general knowledge; retrieved corpus support for the availability heuristic was not available in the supplied passages.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or importance of an event by the ease with which salient examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Three individuals carrying long objects",
      "decision_point_description": "Whether the long objects were probable weapons or tools/pipe",
      "affected_reasoning_operation": "Interpretation of ambiguous long objects under time pressure",
      "bias_specific_mechanism": "A vivid past ambush memory came to mind most easily and served as the primary basis for judging ambiguous objects, while less accessible ordinary examples such as farm tools or irrigation pipe received little weight.",
      "manifestation_in_interview": "The participant said the earlier ambush sortie was 'stuck with me pretty vividly' and was 'the one that surfaced fastest,' even though he later acknowledged that tools and irrigation pipe were more common in routine logs.",
      "effect_on_reasoning_or_decision": "The participant classified the ambiguous objects as probable weapons and recommended escalated surveillance rather than calling the image ambiguous or requesting another pass.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "What came to mind was a sortie a few months back — a group of three, similar setup, turned into an ambush. That one's stuck with me pretty vividly. So I called the objects as probable weapons and recommended escalating surveillance.",
          "evidence_explanation": "The vivid and easily recalled ambush memory directly shaped the weapons interpretation of an ambiguous sensor image."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Briefly, yeah, but the ambush sortie was the one that jumped to mind fastest, and with the clock running I went with that read. Looking back on it, most of the times we've had people carrying long objects out that stretch of road, it's turned out to be farm tools or irrigation pipe — that's actually the more common thing we log on routine passes. But none of those ordinary cases came to mind for me in the moment; the ambush sortie was just the one that surfaced fastest, so that's what shaped the call.",
          "evidence_explanation": "This demonstrates the availability mechanism: the most accessible memory, not the most diagnostic or representative base rate, drove the judgment under time pressure."
        }
      ],
      "correction_or_counterevidence": "The participant briefly considered the tool or irrigation-pipe possibility before the call, and in retrospect recognized that ordinary cases were more common but did not surface in the moment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derives from general knowledge; retrieved corpus support for the availability heuristic was not available in the supplied passages.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory search", "selective exposure"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's pre-existing beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Log-pattern review and next-day attack prediction",
      "decision_point_description": "Commander's question whether tonight predicted an attack tomorrow",
      "affected_reasoning_operation": "Evaluation of the predictive relationship between vehicle activity and next-day indirect fire",
      "bias_specific_mechanism": "The participant directed the log review toward nights that matched his existing belief about vehicle activity predicting next-day fire, and did not seek or examine nonconforming cases, thereby selectively strengthening that belief.",
      "manifestation_in_interview": "The participant stated that he mostly had the MIC bring up nights that matched what he already remembered seeing and did not look for nights with activity but no fire, or fire without activity.",
      "effect_on_reasoning_or_decision": "The participant overestimated the reliability of the four-of-five pattern and told the commander he expected the relationship to hold again the next day.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I mostly had the MIC bring up the nights that matched what I already remembered seeing. I didn't specifically go looking for nights with activity but no fire afterward, or fire without activity beforehand. Wasn't really the focus at the time.",
          "evidence_explanation": "This is direct evidence of selective information search: the participant sought confirmatory cases and omitted disconfirming possibilities."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The MIC showed me four of the last five nights lining up — vehicle activity, then fire the next day. That's a pretty strong hit rate from where I sat, and this was the fifth night in a row I'd personally logged it happening. I told the commander I thought it was a reliable indicator.",
          "evidence_explanation": "The participant treated only the matching pattern as a reliable indicator without considering the missing base rates or nonmatches."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If anything it made me more confident. Five nights running with that connection felt like a real pattern taking shape, not a fluke. I told the commander I expected it to hold again the next day.",
          "evidence_explanation": "The selected streak increased subjective confidence, showing how confirmatory focus strengthened the predictive conclusion."
        }
      ],
      "correction_or_counterevidence": "The four-of-five pattern was objectively present and could plausibly support a predictive relationship from the participant's operational perspective. However, the participant did not examine nonmatching nights, and no real-time correction occurred. The next day produced no fire event.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The confirmation-bias label is supported in general terms by the retrieved cockpit-bias source, which identifies confirmation bias as a common cognitive bias in aviation incidents.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The report identifies confirmation, expectation, and plan continuation among the most common cognitive biases in cockpit incidents.",
          "mechanism_supported_by_source": "The source supports the presence and aviation relevance of confirmation bias, though it does not provide a formal mechanism definition.",
          "relevance_to_this_occurrence": "This occurrence involved selective review of nights fitting the participant's existing belief about vehicle activity predicting next-day indirect fire, consistent with confirmation bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence effect",
      "alternative_labels": ["overconfidence bias", "overprecision"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to hold subjective confidence in one's judgments that is greater than the available evidence supports, often based on perceived experience or expertise.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final compound prioritization call near bingo fuel",
      "decision_point_description": "JTAC's request for a final confidence call on whether to prioritize the compound",
      "affected_reasoning_operation": "Final confidence recommendation under uncertainty",
      "bias_specific_mechanism": "The participant relied on a self-assessed track record and the evening's accumulated pattern as a global confidence cue, allowing it to outweigh specific current disconfirming imagery such as the farm-tool pass and the compound's prolonged quiet period.",
      "manifestation_in_interview": "The participant said he gave high confidence based on his experience and solid track record, and that he trusted his read of the pattern over any single video frame.",
      "effect_on_reasoning_or_decision": "The participant gave high confidence for prioritizing the compound instead of recommending restraint or holding off despite the ambiguous-to-disconfirming current sensor evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But I've flown over two hundred sorties in that sector and I've got a solid track record calling cache sites correctly. I gave it high confidence for prioritization based on that experience, plus everything else from the night stacked together.",
          "evidence_explanation": "The participant used self-perceived track record and experience as the dominant basis for a high-confidence call, even though current evidence was weak or contradictory."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My own track record, honestly. I trusted my read of the pattern over the whole night more than any one frame of video.",
          "evidence_explanation": "This shows the participant prioritized an internal confidence narrative over the specific sensor evidence available at the decision point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The wide-angle pass showing farm tools. If I'd let that carry more weight against my own track record, I probably would've recommended holding off rather than prioritizing it.",
          "evidence_explanation": "The participant identified the underweighted contradictory evidence, supporting the inference that confidence was driven more by self-assessment than by the current picture."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the compound had been quiet for forty minutes and the wide-angle pass suggested farm tools. Later follow-up found no cache or weapons at the compound.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derives from general knowledge; retrieved corpus support for the overconfidence effect was not available in the supplied passages.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single after-action self-report and therefore relies on the participant's retrospective descriptions of his reasoning.",
    "Retrieved corpus support was available for confirmation bias only; availability heuristic and overconfidence effect labels derive from general knowledge because the supplied passages did not contain adequate formal support for those labels.",
    "Outcome information was used only as context and counterevidence, not as the basis for identifying bias.",
    "The interview does not provide independent calibration data to directly assess overconfidence; that occurrence is therefore rated moderate.",
    "The retrieved cockpit source is used only to support the relevance of confirmation bias in aviation decision-making, not as a formal diagnostic definition."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Biased_6_Sonar_on",
  "interview_id": "MD_Biased_6",
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
