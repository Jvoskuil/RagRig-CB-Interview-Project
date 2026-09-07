You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for sitting down with me. As discussed, this is a routine after-action cognitive task analysis, not an investigation — I want to understand how you processed information during the Ridge Road sortie, not evaluate whether calls were right or wrong. You okay to proceed on that basis?

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

Participant: Briefly, yeah, but the ambush sortie was the one that jumped to mind fastest, and with the clock running I went with that read.

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
}}
- Hidden generation specification: {{"hidden_validation_specification": {
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
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "MD_Biased_6_Ridge_Road",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Military intelligence, surveillance, and reconnaissance (ISR) cognitive task analysis",
    "role": "MQ-9 sensor operator",
    "objective": "Maintain surveillance of Ridge Road and a secondary named area of interest, identify possible logistics/cache activity, assess ambiguous personnel and vehicle cues, and provide operational recommendations under weather and fuel constraints.",
    "incident_type": "Ambiguous ISR threat assessment involving a stopped pickup, unidentified long objects, historical activity logs, and a final strike-prioritization recommendation.",
    "confidence": 0.98
  },
  "structure_audit": {
    "estimated_word_count": 1455,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "The participant assessed a pickup stopped at a culvert as a probable resupply touch.",
        "evidence_before": [
          "A pickup with a tarped bed stopped at the culvert for about six minutes.",
          "IR showed one warm engine block.",
          "No weapons, unloading, or personnel grouping were observed.",
          "A weapons cache linked to a truck had been found at the same crossing two weeks earlier."
        ],
        "evidence_after": [
          "The truck departed.",
          "No further activity occurred at the culvert during the sortie.",
          "The eventual explanation was farming-family activity related to an irrigation dispute."
        ],
        "goals_constraints": [
          "Determine whether activity fit a logistics or cache profile.",
          "Operate under intermittent haze and degraded EO coverage.",
          "Allocate sensor attention between Ridge Road and the secondary NAI."
        ],
        "alternatives": [
          "Log the vehicle as routine traffic.",
          "Hold the camera longer before characterizing the event.",
          "Request historical comparison while withholding a threat characterization."
        ],
        "decision_basis": "The prior cache at the same physical crossing was treated as the dominant basis for an initial probable-resupply assessment despite weak current imagery.",
        "time_pressure": "No explicit immediate deadline is stated at this point, although the operator was managing a broader surveillance mission.",
        "uncertainty": "High: the current observation showed only a brief vehicle stop and no direct cache or transfer evidence."
      },
      {
        "id": 2,
        "summary": "The participant categorized long objects carried by three individuals as probable weapons and recommended escalated surveillance.",
        "evidence_before": [
          "Haze required IR-only observation.",
          "The objects could have been rifles, tools, or pipe.",
          "A commander requested an initial read within two minutes.",
          "A vivid earlier sortie involving three people and an ambush came readily to mind."
        ],
        "evidence_after": [
          "A later wide-angle pass suggested farm equipment near the field.",
          "The people were later identified as members of a local farming family."
        ],
        "goals_constraints": [
          "Provide a rapid initial threat characterization.",
          "Maintain surveillance under degraded sensor resolution.",
          "Avoid missing a possible armed threat."
        ],
        "alternatives": [
          "Describe the objects as ambiguous.",
          "Request another angle before making a weapons call.",
          "Treat tools or irrigation pipe as equally live hypotheses."
        ],
        "decision_basis": "The most salient prior ambush memory drove the rapid weapons categorization.",
        "time_pressure": "A two-minute commander request materially constrained the assessment.",
        "uncertainty": "High: IR resolution was insufficient to distinguish rifles from non-hostile long objects."
      },
      {
        "id": 3,
        "summary": "The participant treated recent vehicle activity as a reliable predictor of next-day indirect fire.",
        "evidence_before": [
          "The MIC reported that four of the last five nights with vehicle activity near Ridge Road were followed by indirect-fire spikes the next day.",
          "The participant had personally logged the apparent relationship over five nights.",
          "The commander asked whether the night's activity predicted an attack the following day."
        ],
        "evidence_after": [
          "No indirect-fire event occurred the next day.",
          "The participant acknowledged not seeking nights with vehicle activity but no later fire, or fire without preceding vehicle activity."
        ],
        "goals_constraints": [
          "Provide a near-term predictive judgment for command.",
          "Interpret limited historical logs quickly.",
          "Communicate operationally useful confidence under uncertainty."
        ],
        "alternatives": [
          "State that the pattern is preliminary and non-predictive.",
          "Review both confirming and disconfirming log cells.",
          "Distinguish co-occurrence from a demonstrated causal or predictive mechanism."
        ],
        "decision_basis": "The participant relied on a small recent coincidence streak and selectively reviewed matching observations.",
        "time_pressure": "The exact deadline is not stated, but the review occurred during the sortie and before the final fuel-constrained recommendation.",
        "uncertainty": "High: the dataset was small, the denominator and comparison cases were not reviewed, and no causal mechanism linking vehicle activity to fire was observed."
      },
      {
        "id": 4,
        "summary": "The participant gave high confidence that the compound should be prioritized for a strike package.",
        "evidence_before": [
          "The compound had been quiet for about 40 minutes.",
          "A wide-angle pass suggested farm tools rather than weapons.",
          "The participant's earlier vehicle, object, and pattern assessments had been incorporated into the overall impression.",
          "The participant cited more than 200 sorties in the sector and a strong personal cache-site track record."
        ],
        "evidence_after": [
          "A daytime follow-up sortie found no cache or weapons.",
          "The participant later said the farm-tools cue should have carried more weight."
        ],
        "goals_constraints": [
          "Provide JTAC a final confidence call for strike prioritization.",
          "Operate with approximately 20 minutes before bingo fuel.",
          "Make a recommendation despite incomplete visual confirmation."
        ],
        "alternatives": [
          "Recommend holding off pending more collection.",
          "Give low or qualified confidence.",
          "Prioritize the disconfirming farm-tools cue and prolonged inactivity."
        ],
        "decision_basis": "The participant elevated self-assessed track record and holistic intuition above ambiguous and disconfirming current evidence.",
        "time_pressure": "Bingo fuel was approaching and JTAC requested a final confidence assessment.",
        "uncertainty": "High: no weapons or cache were directly observed, the compound was inactive, and later imagery suggested an innocent explanation."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "AN_01",
      "bias": "Anchoring Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "“Honestly, the location did most of the work... given it was the same crossing, I treated it as a probable resupply touch and wanted that comparison front and center before I'd even really processed the fresh footage.”",
      "evidence_location": "Decision-point-1 reconstruction, participant response to what specifically drove the truck assessment.",
      "mechanism": "A specific historical cache incident at the same culvert supplied an initial reference point that pulled the participant's threat estimate toward resupply activity before fresh, weakly diagnostic footage had been processed.",
      "strength": "strong",
      "confidence": 0.96,
      "plausible_nonbias_explanation": "Location history can be a legitimate ISR cue. Here, however, the participant explicitly says that location history did most of the work and was foregrounded before reviewing current footage, while the current evidence was limited to a short stop with no observed unloading or weapons.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, truck-at-culvert assessment.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The same-location prior cache history",
          "The weak current visual evidence",
          "The participant's statement that historical comparison was prioritized before fresh-footage processing"
        ],
        "avoid_creating": [
          "Do not add separate historical examples that would turn the episode into availability bias rather than spatial anchoring.",
          "Do not make the location history objectively dispositive through added corroborating transfer or weapons evidence."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "AV_01",
      "bias": "Availability Bias",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 2,
      "supporting_quote": "“What came to mind was a sortie a few months back — a group of three, similar setup, turned into an ambush. That one's stuck with me pretty vividly. So I called the objects as probable weapons.”",
      "evidence_location": "Decision-point-2 object-identification account and follow-up probe on the tool or irrigation-pipe alternative.",
      "mechanism": "The participant's rapid category judgment was influenced by an especially vivid and easily recalled prior ambush episode. The text establishes salience and reliance, but does not establish the relevant base rate of non-hostile long objects or show that the recalled episode displaced known frequency information.",
      "strength": "moderate",
      "confidence": 0.79,
      "plausible_nonbias_explanation": "Under a two-minute deadline, degraded IR imagery, and a potentially armed group, recognition-primed use of a similar prior incident can be justified expertise or risk management. A bad outcome alone does not make it availability bias.",
      "additional_evidence_needed": "A subtle indication that ordinary non-hostile explanations were more frequent or were known from routine sector experience, yet the participant did not retrieve or weight that frequency information because the ambush memory was more vivid.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_evidence_addition",
        "location": "Decision point 2, immediately after the participant says the earlier ambush was the first event that came to mind.",
        "current_defect": "The interview demonstrates vivid-memory reliance but not the required contrast between salience and a less memorable relevant base rate. The episode therefore remains potentially consistent with an appropriate rapid expert analogy.",
        "minimal_change_instruction": "Add one restrained participant statement or probe response establishing that similar long objects on this route were usually farm tools or irrigation pipe in routine reviews, but that the participant did not bring those routine cases to mind and instead let the memorable ambush determine the initial weapons call. Keep the statement focused on memory retrieval and weighting, not on hindsight or the later benign outcome.",
        "preserve": [
          "The two-minute commander request",
          "IR-only ambiguity",
          "The vivid earlier ambush memory",
          "The participant's brief consideration of tools or pipe",
          "The existing decision-point sequence"
        ],
        "avoid_creating": [
          "Do not add a second anchoring episode based on a location or prior report.",
          "Do not portray the participant as ignoring a direct visual identification of tools.",
          "Do not add a second independent availability instance at the final recommendation."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "IC_01",
      "bias": "Illusory Correlation",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "“The MIC showed me four of the last five nights lining up — vehicle activity, then fire the next day... I told the commander I thought it was a reliable indicator.”",
      "evidence_location": "Decision-point-3 response to the commander's question about predicting next-day attack activity.",
      "mechanism": "The participant inferred that two co-occurring event types formed a reliable predictive relationship from a small set of coincidence nights, without observing or articulating a mechanism connecting vehicle activity to later indirect fire.",
      "strength": "moderate",
      "confidence": 0.87,
      "plausible_nonbias_explanation": "Vehicle activity could genuinely be a predictive operational cue if supported by a broader validated intelligence model, a known logistics-to-fire mechanism, or properly characterized base rates. None is provided here, and the participant elevates the co-occurrence itself into a reliable indicator.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, predictive claim about vehicle activity and next-day fire.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The distinction between co-occurrence and a demonstrated mechanism",
          "The participant's reliable-indicator claim",
          "The separate log-search and streak-extrapolation evidence"
        ],
        "avoid_creating": [
          "Do not add a real intelligence mechanism that would validate the inference.",
          "Do not merge this claim with the separate selective-search or regression-to-the-mean mechanisms."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "CB_01",
      "bias": "Confirmation Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "“I mostly had the MIC bring up the nights that matched what I already remembered seeing. I didn't specifically go looking for nights with activity but no fire afterward, or fire without activity beforehand.”",
      "evidence_location": "Decision-point-3 follow-up on how the participant reviewed the log data.",
      "mechanism": "The participant selectively retrieved confirming cells from the available sortie-log dataset while not seeking disconfirming cells that could test the recalled pattern.",
      "strength": "strong",
      "confidence": 0.97,
      "plausible_nonbias_explanation": "A time-limited review can legitimately begin with apparently relevant observations. The explicit statement that matching nights were selected because they fit what the participant already remembered, combined with failure to inspect contrary cells, supports confirmation bias rather than merely incomplete analysis.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, MIC log-review discussion.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The MIC as the log source",
          "The distinction between confirming and disconfirming log cells",
          "The participant's remembered-pattern framing"
        ],
        "avoid_creating": [
          "Do not make the logs unavailable, because that would shift the explanation to missing information.",
          "Do not add an explicit causal mechanism for the vehicle/fire relationship."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "FRM_01",
      "bias": "Failure to recognize regression to the mean",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "“If anything it made me more confident. Five nights running with that connection felt like a real pattern taking shape, not a fluke. I told the commander I expected it to hold again the next day.”",
      "evidence_location": "Decision-point-3 follow-up specifically probing whether the unusually high streak affected confidence.",
      "mechanism": "The participant treated an unusually strong short-term run as evidence that the high rate would persist, rather than considering that an extreme recent streak may normalize in subsequent observations.",
      "strength": "moderate",
      "confidence": 0.88,
      "plausible_nonbias_explanation": "A recent streak can rationally increase confidence if it reflects a stable, independently validated change in adversary behavior. The interview supplies neither a stable mechanism nor a sufficiently characterized longer-term data series, and the participant expressly rejects the possibility that the run is a fluke.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, streak-confidence probe.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The explicit unusually-high-streak prompt",
          "The participant's increased confidence because of the streak",
          "The future-oriented expectation that the pattern would hold"
        ],
        "avoid_creating": [
          "Do not add longer-term base-rate data showing a stable pattern.",
          "Do not collapse this occurrence into confirmation bias by focusing on the log search process rather than future extrapolation."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "OC_01",
      "bias": "Overconfidence Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 4,
      "supporting_quote": "“I've flown over two hundred sorties in that sector and I've got a solid track record calling cache sites correctly. I gave it high confidence for prioritization...” and “My own track record, honestly. I trusted my read of the pattern over the whole night more than any one frame of video.”",
      "evidence_location": "Decision-point-4 final-recommendation account and probe asking for the single most important evidence.",
      "mechanism": "The participant issued a high-confidence strike-prioritization recommendation by relying on self-assessed prior accuracy and overall intuitive pattern recognition while underweighting 40 minutes of inactivity and imagery suggesting farm tools.",
      "strength": "strong",
      "confidence": 0.96,
      "plausible_nonbias_explanation": "Experience can appropriately inform confidence where individual frames are ambiguous. The bias is supported because the participant explicitly ranks personal track record above contemporaneous disconfirming evidence and later acknowledges that the farm-tools cue should have changed the recommendation.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 4, final compound-prioritization recommendation.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The high-confidence recommendation",
          "The self-reported track record as its justification",
          "The quiet compound and farm-tools cue as current disconfirming evidence",
          "The fuel constraint"
        ],
        "avoid_creating": [
          "Do not make the recommendation unsupported solely because it was wrong in hindsight.",
          "Do not add a second confidence statement at earlier decision points that could create an extra overconfidence occurrence."
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Overconfidence Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Availability Bias",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    },
    {
      "bias": "Anchoring Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Confirmation Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Failure to recognize regression to the mean",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Illusory Correlation",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Representativeness heuristic",
      "decision_point": 2,
      "supporting_quote": "“A group of three, similar setup, turned into an ambush... So I called the objects as probable weapons.”",
      "mechanism": "The participant may have judged the ambiguous current group to be threatening because it superficially resembled a prior ambush configuration.",
      "confidence": 0.48,
      "status": "weak",
      "plausible_nonbias_explanation": "This is better explained by the intended availability mechanism because the account emphasizes vivid recall rather than a claimed prototypical resemblance rule. Time pressure and degraded imagery also support a non-bias recognition-primed explanation.",
      "revision_recommendation": "remove_or_neutralize"
    },
    {
      "bias": "Premature closure",
      "decision_point": 1,
      "supporting_quote": "“The location match made me want to get the historical data moving right away rather than just sitting on it.”",
      "mechanism": "The participant may have moved prematurely toward a resupply interpretation before collecting further current imagery.",
      "confidence": 0.42,
      "status": "weak",
      "plausible_nonbias_explanation": "The participant requested the old report rather than terminating collection, and no final closure at this moment is clearly established. The behavior is adequately captured by anchoring and should not be counted independently.",
      "revision_recommendation": "remove_or_neutralize"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "The haze-driven switch from EO to IR.",
      "location": "Initial incident account and decision point 2.",
      "why_not_bias": "This is a sensor and environmental constraint that directly reduces object-identification resolution. It explains uncertainty but does not itself establish distorted reasoning."
    },
    {
      "cue": "The commander's two-minute request.",
      "location": "Decision point 2.",
      "why_not_bias": "Time pressure can make a quick decision understandable and can increase reliance on recognition, but time pressure is not itself a cognitive bias."
    },
    {
      "cue": "Approaching bingo fuel and JTAC's request for a final call.",
      "location": "Decision point 4.",
      "why_not_bias": "Fuel and operational-tasking constraints are legitimate organizational conditions. They do not independently prove overconfidence, escalation, or any other bias."
    },
    {
      "cue": "The eventual farming-family explanation and absence of next-day fire.",
      "location": "Outcome account.",
      "why_not_bias": "An incorrect or unfavorable outcome does not establish that the original reasoning was biased. The bias findings depend on the stated reasoning processes before the outcome was known."
    },
    {
      "cue": "The participant's more than 200 sorties of sector experience.",
      "location": "Decision point 4.",
      "why_not_bias": "Experience can be valid expertise. It becomes evidence of overconfidence here only because the participant explicitly gives it more weight than contemporaneous contradictory observations."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "Vehicle activity near Ridge Road predicts next-day indirect fire.",
        "speaker": "Participant",
        "basis_offered": "Four of five recent nights reportedly had vehicle activity followed by fire the next day, reinforced by the participant's personal recollection.",
        "mechanism_observed": "None. No logistics, command-and-control, targeting, or temporal-operational pathway is identified."
      },
      {
        "claim": "The prior cache at the culvert affected the participant's initial truck assessment.",
        "speaker": "Participant",
        "basis_offered": "The participant states that without the prior cache history, the truck likely would have been logged as routine traffic.",
        "mechanism_observed": "The historical event supplied a salient spatial reference point that changed initial evidence weighting."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "The participant treats a limited sequence of temporal co-occurrences as a reliable predictor without examining false positives, false negatives, denominators, alternative common causes, or a connecting mechanism.",
        "affected_decision_point": 3,
        "assessment": "High"
      },
      {
        "risk": "The four-of-five rate is presented without a defined observation window, baseline fire frequency, vehicle-activity prevalence, or verification that the observations are independent.",
        "affected_decision_point": 3,
        "assessment": "High"
      }
    ],
    "counterfactual_present": true,
    "changed_variable": "Presence versus absence of the prior cache incident at the same culvert crossing.",
    "held_constant": [
      "The observed truck stop and its duration",
      "Weather and sensor conditions",
      "Mission setting and participant role",
      "The participant's stated decision task",
      "The remaining sortie chronology"
    ],
    "causal_coherence": "strong",
    "explanation": "The principal counterfactual probe is appropriately diagnostic: it changes the intended anchor-history variable while preserving the current truck observation, and the participant reports a different initial classification. The later hypothetical probes concerning the remembered ambush and first-night experience are also useful diagnostic probes, but they should not be treated as outcome counterfactuals or as evidence that the original scenario itself changed."
  },
  "quality_scores": {
    "occupational_realism": 88,
    "cta_fidelity": 91,
    "bias_separability": 86,
    "bias_subtlety": 82,
    "control_fidelity": 100,
    "counterfactual_fidelity": 88,
    "narrative_coherence": 92,
    "naturalness": 87,
    "hidden_label_integrity": 85,
    "overall_quality": 88
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 5,
    "requested_occurrence_total": 6,
    "missing_occurrence_total": 1,
    "accidental_occurrence_total": 0,
    "priority": "low",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Retain exactly four decision points and the existing order: truck assessment, ambiguous-object assessment, log-pattern assessment, and final compound recommendation.",
      "Preserve the distinction at decision point 3 between evidence selection (confirmation bias), causal/predictive inference (illusory correlation), and projection of an extreme short-run rate (failure to recognize regression to the mean).",
      "Do not use the later farming-family outcome as the primary proof of any cognitive bias.",
      "Preserve the specified counterfactual variable of prior cache history at the culvert and do not add a second causal change to that probe.",
      "Repair only the availability episode; no broad regeneration is needed."
    ],
    "revision_order": [
      {
        "instance_id": "AV_01",
        "action": "Add a minimal base-rate-versus-salience cue to the existing object-identification dialogue so that vivid recall, rather than justified rapid expertise alone, independently explains the weapons categorization."
      }
    ]
  },
  "failure_flags": [
    {
      "flag": "availability_base_rate_not_explicit",
      "severity": "moderate",
      "description": "The intended availability mechanism requires reliance on a vivid prior incident rather than a relevant base rate, but the interview establishes the vivid incident without establishing the non-hostile base rate that was displaced."
    }
  ]
}}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
