"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "weather_expectation_context",
        "raw_interview_anchor": "Destination has a known fog problem in the early morning — radiation fog that usually burns off by mid-morning.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A general weather expectation is stated as context, but no hidden bias instance is manifested in this scene-setting statement."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "dispatch_review_and_forecast_assessment",
        "raw_interview_anchor": "The release showed the destination TAF with fog down to a half mile visibility starting around 0500, improving to three miles by 0900. Our ETA was 0845... Dispatch had us at minimum contract fuel plus standard contingency... I'd flown into that airport probably a dozen times with similar fog setups, so the pattern was familiar to me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This establishes the information and prior experience available before the fuel decision; it does not by itself contain a hidden bias manifestation."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "predeparture_weather_read",
        "raw_interview_anchor": "Honestly, I felt fine about it. The forecast lined up with what I'd typically seen there — fog clears out once the sun gets some angle on it. Nothing about the release stood out as unusual.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an expectation assessment, but the hidden manifest does not allocate an occurrence to this opening read and the statement alone does not establish the required mechanism."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "fuel_acceptance_basis",
        "raw_interview_anchor": "It was really just what the release called for. Dispatch runs the numbers, and if they don't flag anything extra, that's usually a good signal it's a normal day. I didn't see a reason to second-guess it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["os_01"],
        "ground_truth_rationale": "The captain frames the fuel decision as purely objective/procedural while omitting the material role of his experience-based confidence that the fog would improve."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "additional_fuel_tradeoff",
        "raw_interview_anchor": "I thought about it briefly — my first officer actually mentioned the improvement time was pretty close to our ETA, not a lot of cushion. But the release was within limits, and asking for extra fuel when the paperwork already supports the flight can slow things down at the gate. We had a full connection bank behind us. I went with what was filed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a separate operational tradeoff rationale involving gate delay, connections, and procedural limits; it is not the narrow hidden self-report mechanism for Omitting Subjectivity."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "forecast_clearance_expectation",
        "raw_interview_anchor": "Half mile visibility overnight, improving to three miles by 0900. I expected it to be lifting by the time we got there, based on how that pattern usually goes at that field.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This states the expectation underlying the scenario, but not the required retrospective framing of the fuel decision as purely procedural."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "enroute_plan_continuation",
        "raw_interview_anchor": "Since dispatch wasn't changing the release, and the delay didn't seem dramatic yet, we kept proceeding toward the field and started working the descent.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The manifest reserves the Plan Continuation instance for the distinct pre-approach decision at decision point 3; this earlier response is a separate, non-target episode despite being a plausible related prediction."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "enroute_alternative_rejection",
        "raw_interview_anchor": "We could've asked for holding fuel proactively, or had dispatch start building an early diversion picture. We didn't do either — it felt premature at that point, since one lagging METAR isn't necessarily a trend.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is the same distinct decision-point-2 episode and is negative under the exhaustive hidden manifest; it cannot be credited as the planned decision-point-3 occurrence."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "preapproach_evidence_assessment",
        "raw_interview_anchor": "Tower told us the last two aircraft in landed fine, but a third had just gone missed. Looking at the last few METARs, one had ticked up slightly and then the next held flat — not really a clear trend either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This reports the mixed evidence available before the approach; the hidden instance is mapped to the subsequent choice to continue rather than to this evidence description alone."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "approach_continuation_decision",
        "raw_interview_anchor": "We could have diverted straight to the alternate right then instead of shooting the approach. But two of the three recent arrivals had gotten in, and the forecast had always called for improvement by our arrival window, so I expected we'd break out. We briefed it as a normal approach and continued. We noted it, but it didn't really shift the plan. We were still within minimums, legally fine to try, and the overall picture matched what we'd expected going in.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["pc_01"],
        "ground_truth_rationale": "The captain continues the original approach plan despite the go-around report and flattening trend, giving disproportionate weight to the earlier forecast and successful arrivals."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "missed_approach_action",
        "raw_interview_anchor": "We didn't get the visual references we needed, so we went missed. Fuel after that put us close to the point where we needed to commit to the alternate.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a procedural response to the failed approach and fuel state, not an additional hidden bias instance."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "postmissedapproach_situation_assessment",
        "raw_interview_anchor": "Everything got a lot more concrete. Fuel was no longer theoretical — I had a hard number and a hard decision. ATIS still showed the same visibility as before, no real improvement. The alternate was reporting clear skies and we had comfortable fuel to get there, and ops confirmed ground handling was ready for us.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The captain independently reassesses the changed fuel and weather state; the hidden specification explicitly requires this later reasoning to resolve independently."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "diversion_choice",
        "raw_interview_anchor": "Try one more approach at the destination since we were still technically legal, or commit to the alternate now while we had solid reserves. I ran the fuel numbers again independently rather than assuming we'd get in this time, and it was clear the smarter move was to divert.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The captain independently recomputes fuel and selects the alternate; this is explicitly non-target reasoning in the hidden validation."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "diversion_decision_basis",
        "raw_interview_anchor": "The fuel math, plain and simple. There wasn't a strong reason to think a second attempt would go differently, and I didn't want to erode our margins further chasing it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This reinforces the independent post-missed-approach fuel rationale and does not add a hidden instance."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "closing_retrospective_adjustment",
        "raw_interview_anchor": "I'd probably push a little harder for extra fuel given how tight that improvement window was relative to our ETA, and maybe ask dispatch for a firmer trend picture before committing to the approach rather than the destination. But nothing that happened was outside normal limits at any single point — it was more about the margins tightening up as we went.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a hindsight reflection and proposed future adjustment; the hidden validation says closing hypotheticals do not introduce additional bias instances."
      }
    ]
  }
