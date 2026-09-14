You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a safety review process, your responses are confidential to the review team, and you can decline any question. That work for you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start with your role and a quick summary of the flight in question?

Participant: Sure. I was captain on a scheduled morning turn, regional jet, about ninety minutes of flying time. First officer was experienced, we'd flown together a handful of times before. Destination has a known fog problem in the early morning — radiation fog that usually burns off by mid-morning.

Interviewer: Walk me through the flight from your initial review of the dispatch release that morning.

Participant: The release showed the destination TAF with fog down to a half mile visibility starting around 0500, improving to three miles by 0900. Our ETA was 0845, so we were arriving right at the edge of that improvement window. Dispatch had us at minimum contract fuel plus standard contingency — nothing extra flagged. I'd flown into that airport probably a dozen times with similar fog setups, so the pattern was familiar to me.

Interviewer: What was your overall read of the weather situation before departure?

Participant: Honestly, I felt fine about it. The forecast lined up with what I'd typically seen there — fog clears out once the sun gets some angle on it. Nothing about the release stood out as unusual.

Decision Point 1

Interviewer: When you accepted the fuel load in dispatch, what specifically drove that decision — was it purely the release numbers, or did your own experience with this airport factor in?

Participant: It was really just what the release called for. Dispatch runs the numbers, and if they don't flag anything extra, that's usually a good signal it's a normal day. I didn't see a reason to second-guess it.

Interviewer: Did you consider requesting additional fuel for holding, given the airport's fog history?

Participant: I thought about it briefly — my first officer actually mentioned the improvement time was pretty close to our ETA, not a lot of cushion. But the release was within limits, and asking for extra fuel when the paperwork already supports the flight can slow things down at the gate. We had a full connection bank behind us. I went with what was filed.

Interviewer: What did the TAF and dispatch release actually say about the fog, and when did you expect it to clear?

Participant: Half mile visibility overnight, improving to three miles by 0900. I expected it to be lifting by the time we got there, based on how that pattern usually goes at that field.

Decision Point 2

Interviewer: What did you hear from dispatch and from other aircraft as you got closer to the airport?

Participant: About an hour in, we got an ACARS update — METAR still showing half mile visibility, no improvement yet. Then a PIREP came through from an aircraft that had landed twenty minutes earlier, saying they broke out at minimums after two attempts.

Interviewer: When the updated METAR still showed fog an hour into the flight, what options did you weigh, and why did you not request additional fuel or a route change at that point?

Participant: We talked about it for a minute. I called dispatch to check in, and they acknowledged it was running a little behind the forecast but didn't amend anything on their end. Fuel was still on profile for the planned arrival, just with less room for extended holding than I'd have liked. Since dispatch wasn't changing the release, and the delay didn't seem dramatic yet, we kept proceeding toward the field and started working the descent.

Interviewer: Looking back, what other options were realistically available at that stage?

Participant: We could've asked for holding fuel proactively, or had dispatch start building an early diversion picture. We didn't do either — it felt premature at that point, since one lagging METAR isn't necessarily a trend.

Decision Point 3

Interviewer: Describe what happened during the approach and the missed approach in your own words.

Participant: As we got in range, ATIS had visibility at three-quarters of a mile, right at minimums for the approach we were flying. Tower told us the last two aircraft in landed fine, but a third had just gone missed. Looking at the last few METARs, one had ticked up slightly and then the next held flat — not really a clear trend either way.

Interviewer: At that point, what alternatives did you consider besides continuing the approach, and what tipped the decision toward continuing?

Participant: We could have diverted straight to the alternate right then instead of shooting the approach. But two of the three recent arrivals had gotten in, and the forecast had always called for improvement by our arrival window, so I expected we'd break out. We briefed it as a normal approach and continued.

Interviewer: Did the go-around report from the third aircraft factor into that briefing?

Participant: We noted it, but it didn't really shift the plan. We were still within minimums, legally fine to try, and the overall picture matched what we'd expected going in.

Interviewer: What happened at decision altitude?

Participant: We didn't get the visual references we needed, so we went missed. Fuel after that put us close to the point where we needed to commit to the alternate.

Decision Point 4

Interviewer: After the missed approach, what changed in how you evaluated the situation compared to before?

Participant: Everything got a lot more concrete. Fuel was no longer theoretical — I had a hard number and a hard decision. ATIS still showed the same visibility as before, no real improvement. The alternate was reporting clear skies and we had comfortable fuel to get there, and ops confirmed ground handling was ready for us.

Interviewer: What alternatives did you weigh at that point?

Participant: Try one more approach at the destination since we were still technically legal, or commit to the alternate now while we had solid reserves. I ran the fuel numbers again independently rather than assuming we'd get in this time, and it was clear the smarter move was to divert. We coordinated with dispatch, confirmed the numbers, and headed to the alternate.

Interviewer: What ultimately drove that choice?

Participant: The fuel math, plain and simple. There wasn't a strong reason to think a second attempt would go differently, and I didn't want to erode our margins further chasing it.

Closing Reflection

Interviewer: If the go-around PIREP had come in before you accepted the fuel load that morning, would that have changed your decision?

Participant: Possibly. If I'd known that early, I might have asked for a bit more contingency fuel going out the door. It's easier to build in margin before departure than to manufacture it later.

Interviewer: If you had to explain your fuel-planning decision to a new first officer, how would you describe the basis for it?

Participant: I'd tell them dispatch runs a solid process, and if the release supports the flight without flags, that's generally trustworthy. It's a pretty standard call.

Interviewer: What would you do differently if you flew this exact scenario again next month?

Participant: I'd probably push a little harder for extra fuel given how tight that improvement window was relative to our ETA, and maybe ask dispatch for a firmer trend picture before committing to the approach rather than the destination. But nothing that happened was outside normal limits at any single point — it was more about the margins tightening up as we went.

Interviewer: That's really helpful, thank you. I think that covers what I need.

Participant: No problem, glad to help.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Biased_2",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Airline Transport Pilot (ATP) – Scheduled Carrier",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Fog Burn-Off Expectation: Regional Jet Approach into Deteriorating Visibility",
    "scenario_summary_internal": "Captain of a scheduled regional jet flight plans fuel and reviews dispatch weather showing patchy morning fog at the destination forecast to burn off by arrival. En route, updated reports show the fog persisting longer than forecast. Approaching the airport, visibility hovers near approach minima with an ambiguous improving/worsening trend. The captain continues the approach expecting conditions to resolve as originally briefed, executes a missed approach, and must then decide whether to attempt a second approach or divert to the filed alternate with reduced fuel margins.",
    "occupational_realism": {
      "objective": "Complete a scheduled passenger flight safely and on time by making sound fuel, weather-diversion, and approach-continuation decisions under evolving, uncertain destination weather.",
      "setting": "Two-person crew, single-aisle regional jet, domestic scheduled carrier operation, morning departure with destination airport prone to radiation fog, dispatcher release under Part 121-style operational control.",
      "constraints": [
        "Fuel load is finite and each holding/diversion option trades against required reserves",
        "Dispatch release sets a filed alternate and minimum fuel figure that the crew can supplement but not unilaterally reduce",
        "Company on-time performance and connecting passenger loads create schedule pressure",
        "Weather trend information (METAR/TAF/PIREP) updates incrementally and is sometimes contradictory",
        "Approach minima are fixed by regulation and cannot be judgment-adjusted"
      ],
      "stakeholders": [
        "Captain (interviewee)",
        "First officer",
        "Company dispatcher",
        "Air traffic control",
        "Passengers with connections",
        "Destination station operations"
      ],
      "technical_terms_to_use": [
        "dispatch release",
        "TAF/METAR",
        "contingency fuel",
        "missed approach",
        "alternate minimums",
        "PIREP",
        "holding fuel",
        "decision altitude",
        "stabilized approach"
      ],
      "technical_terms_to_avoid": [
        "plan continuation bias",
        "omitting subjectivity",
        "confirmation bias",
        "anchoring",
        "cognitive bias",
        "heuristic"
      ],
      "notes": "Keep dialogue naturalistic; the captain should sound competent and procedurally fluent, not careless, so that bias manifestations remain subtle rather than obviously reckless."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch release shows destination TAF forecasting fog 0500-0800L improving to 3SM by 0900L, arrival ETA 0845L",
          "Dispatcher recommends minimum contractual fuel plus standard contingency, no extra fuel flagged",
          "Captain has flown into this airport during similar fog patterns roughly a dozen times before"
        ],
        "alternatives": [
          "Accept dispatch fuel as filed",
          "Request additional discretionary fuel for extended holding given fog history at this station"
        ],
        "new_information_after_decision": [
          "First officer notes the TAF's improvement time is close to the ETA, giving little margin",
          "Flight departs on schedule with dispatch-minimum fuel plus contingency only"
        ],
        "intended_action": "Captain accepts the dispatch fuel load, characterizing the choice as simply following the numbers on the release rather than a personal read of how reliably the fog would burn off on schedule."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "One hour into the flight, ACARS relay shows an updated METAR still reporting 1/2SM visibility in fog at the destination, no improvement yet",
          "A PIREP from an aircraft that landed 20 minutes ago reports breaking out at minimums after two attempts",
          "Fuel remaining is on profile for planned arrival but leaves reduced margin for extended holding"
        ],
        "alternatives": [
          "Contact dispatch to discuss holding fuel, rerouting, or early diversion planning",
          "Continue as planned, treating the delay in improvement as within normal variability"
        ],
        "new_information_after_decision": [
          "Dispatch acknowledges the slower improvement but does not amend the release",
          "Crew begins descent planning still targeting the original destination"
        ],
        "intended_action": "Crew briefly discusses the discrepancy, contacts dispatch for a status check, and proceeds toward the destination without requesting additional fuel or an alternate routing change."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Current ATIS reports visibility 3/4SM, at the published minimum for the approach in use",
          "Tower reports the last two aircraft landed without incident but a third just went around",
          "Trend over the last three METARs is mixed: one improved reading followed by one that held steady",
          "Fuel remaining supports one approach plus a missed approach and diversion to the filed alternate, with limited margin for a second attempt"
        ],
        "alternatives": [
          "Continue the approach as originally planned, expecting the forecast improvement to materialize as briefed",
          "Divert directly to the alternate before commencing the approach, preserving full fuel margin"
        ],
        "new_information_after_decision": [
          "The aircraft reaches decision altitude without acquiring the required visual references and executes a missed approach",
          "Fuel state after the missed approach is now closer to the point requiring a firm diversion decision"
        ],
        "intended_action": "Captain briefs and flies the approach as originally intended, citing the forecast improvement and the two successful landings ahead, and does not treat the mixed trend or the go-around report as grounds to divert before attempting the approach."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Post-missed-approach fuel is at or near the point requiring a diversion to remain within reserve requirements",
          "Current ATIS shows visibility unchanged from the prior approach",
          "Alternate airport reports clear conditions and is within comfortable fuel range if committed to now",
          "Company operations has confirmed ground handling availability at the alternate"
        ],
        "alternatives": [
          "Divert immediately to the filed alternate with adequate fuel reserves",
          "Request one more approach at the destination given the marginal-but-legal visibility report"
        ],
        "new_information_after_decision": [
          "Fuel and reserve calculations are confirmed with dispatch before the final approach or diversion",
          "Flight is completed to either the original destination or the alternate depending on the choice made"
        ],
        "intended_action": "Captain reassesses fuel state independently of the earlier expectation and diverts to the alternate, illustrating that the crew's judgment was not universally compromised and that the earlier continuation was a bounded, decision-specific lapse."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through the flight from your initial review of the dispatch release that morning.",
        "What was your overall read of the weather situation before departure?"
      ],
      "timeline_reconstruction": [
        "What did the TAF and dispatch release actually say about the fog, and when did you expect it to clear?",
        "What did you hear from dispatch and from other aircraft as you got closer to the airport?",
        "Describe what happened during the approach and the missed approach in your own words."
      ],
      "decision_point_probes": [
        "When you accepted the fuel load in dispatch, what specifically drove that decision — was it purely the release numbers, or did your own experience with this airport factor in?",
        "When the updated METAR still showed fog an hour into the flight, what options did you weigh, and why did you not request additional fuel or a route change at that point?",
        "At the point visibility was reported right at minimums with a mixed trend, what alternatives did you consider besides continuing the approach, and what tipped the decision toward continuing?",
        "After the missed approach, what changed in how you evaluated the situation compared to before the approach?"
      ],
      "goals_and_alternatives": [
        "What competing goals were you balancing — schedule, fuel conservation, passenger connections, safety margins?",
        "Looking back, what other options were realistically available to you at each stage?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure did you feel at each stage, and how did that affect how you gathered or used information?",
        "How confident were you in the forecast improvement, and how did that confidence level change over the flight?"
      ],
      "prior_experience": [
        "How has your past experience with fog at this airport shaped how you interpret forecasts there?"
      ],
      "closing_hypotheticals": [
        "If the PIREP reporting a go-around had come in before you accepted the fuel load, would that have changed your decision?",
        "If you had to explain your fuel-planning decision to a new first officer, how would you describe the basis for it?",
        "What would you do differently if you flew this exact scenario again next month?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "decision_point": 1,
        "mechanism": "When probed about the basis for accepting the dispatch fuel load, the captain describes the decision as simply following the objective release numbers/procedure, without acknowledging that the acceptance also rested on his own subjective confidence that the fog would burn off on the forecast schedule based on personal experience at that station.",
        "affected_reasoning_operation": "Retrospective justification / self-report of decision basis",
        "evidence_available_at_time": [
          "Dispatch release with TAF showing improvement forecast close to ETA",
          "Captain's personal history of roughly a dozen prior encounters with similar fog patterns at this station",
          "No explicit dispatcher flag recommending extra fuel"
        ],
        "required_textual_manifestation": "In response to the decision-basis probe, the captain states the fuel decision was 'straightforward, just what the release called for' or equivalent, while the timeline shows his experience-based read of the fog trend was actually doing real work in the acceptance — and this subjective input is not mentioned or flagged as such.",
        "plausible_nonbias_interpretation": "The captain may simply be summarizing a routine, low-friction decision because dispatch fuel figures are usually followed without much personal deliberation, not necessarily concealing a judgment call.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Any reference to 'subjectivity,' 'assumption,' or 'judgment call' as a labeled concept",
          "Any explicit admission that the objective framing was misleading"
        ]
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "decision_point": 3,
        "mechanism": "Despite mixed and non-confirming trend data (steady-to-worsening visibility, one aircraft going around) at the point where visibility sat right at minimums, the captain continues with the originally briefed plan of flying the approach to the original destination rather than treating the new evidence as grounds to divert before the attempt, giving disproportionate weight to the earlier forecast and the two successful landings.",
        "affected_reasoning_operation": "Updating a prior plan in light of new disconfirming evidence before committing to an approach",
        "evidence_available_at_time": [
          "ATIS visibility exactly at published minimum",
          "Mixed METAR trend (one improved reading, one flat reading)",
          "One aircraft executing a go-around shortly before, alongside two successful landings",
          "Reduced fuel margin for multiple attempts"
        ],
        "required_textual_manifestation": "The captain's account of the approach decision cites the original forecast and the earlier successful landings as the basis for proceeding, without weighing the go-around report or the flattening trend as a reason to divert before the approach attempt; the decision reads as continuation of the original plan rather than a fresh evaluation at that moment.",
        "plausible_nonbias_interpretation": "Continuing the approach was legal and within minima, and two of three recent aircraft landed successfully, so proceeding could reflect a reasonable probabilistic read of the situation rather than an unwillingness to abandon the plan.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Any reference to 'plan continuation,' 'sunk cost,' or 'commitment to the original plan' as a labeled concept",
          "Explicit admission that the go-around report was disregarded because of prior commitment"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control specified in this generation pass."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable for this condition (biased, no counterfactual requested)",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points, each with at least two plausible alternatives",
      "Confirm exactly one Omitting Subjectivity instance placed at decision point 1 and exactly one Plan Continuation instance placed at decision point 3",
      "Confirm no bias labels, definitions, or psychological terminology appear in interview text or probes",
      "Confirm decision point 4 shows fuel/diversion reasoning that resolves independently of the biased approach decision, so consequences do not mechanically prove bias",
      "Confirm word count target 1,350 (range 1,215-1,485) is achievable given four decision points plus probe answers without repetitive padding",
      "Confirm captain is portrayed as generally competent to keep bias manifestations subtle rather than overtly negligent",
      "Confirm closing hypotheticals do not introduce new bias instances beyond the two planned"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Omitting Subjectivity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a retrospective self-report of decision basis at the fuel-planning decision point, framing a partly subjective judgment as purely procedural/objective."
      },
      {
        "bias": "Plan Continuation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as continuing the original approach plan into destination despite mixed/disconfirming trend evidence (go-around report, flat visibility trend) available before commencing the approach."
      }
    ],
    "target_bias_names": [
      "Omitting Subjectivity",
      "Plan Continuation"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Omitting Subjectivity",
        "requested_occurrences": 1
      },
      {
        "bias": "Plan Continuation",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity"
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "decision_point": 1
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "mechanism": "Captain's self-report of the fuel-load decision omits that a subjective confidence judgment (personal history with the station's fog patterns) was material to accepting dispatch-minimum fuel, instead framing the decision as purely procedural.",
        "affected_reasoning_operation": "Retrospective justification / self-report of decision basis",
        "evidence_source": "Captain's answer to the decision-basis probe at decision point 1, contrasted with the timeline fact of his prior experience-based expectation",
        "distinctiveness_requirement": "Must be tied specifically to the fuel-acceptance decision and the framing of its basis, not to any later decision or general commentary on weather uncertainty."
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "mechanism": "Captain proceeds with the originally briefed approach into the original destination despite a go-around report and a flattening visibility trend, weighting the original forecast/plan over the newer disconfirming cues immediately before the approach attempt.",
        "affected_reasoning_operation": "Updating a prior plan given new disconfirming evidence before committing to an approach",
        "evidence_source": "Captain's account of the approach-continuation decision at decision point 3, contrasted with the mixed METAR trend and go-around PIREP available at that time",
        "distinctiveness_requirement": "Must be tied specifically to the pre-approach continuation decision at decision point 3, not to the earlier fuel decision (decision point 1) or the later post-missed-approach diversion decision (decision point 4), which must show the captain reassessing independently."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "strength": "subtle"
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_2",
    "domain_id": "AV",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias occurred once in the manifest; each was assigned to the single decision point offering the best mechanism fit and narrative realism (fuel-planning self-report for Omitting Subjectivity at decision point 1; approach-continuation choice under disconfirming trend evidence for Plan Continuation at decision point 3), per rules 2 and 3 of the allocation guidance. No decision point received more than one instance of either bias, and the two biases were kept at distinct decision points to preserve independent evidence traces.",
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
    "analysis_scope_note": "Analyzed the interview transcript for affirmatively evidenced cognitive biases. No retrieved scientific corpus passages were supplied, so classifications are grounded in the transcript and established cognitive-science knowledge rather than task-specific retrieval evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation_bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan_continuation_bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "plan_continuation_bias",
      "alternative_labels": [
        "get-there-itis",
        "plan continuation error"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to persist with an existing plan despite new information indicating that the plan's assumptions or margins are weakening.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "In-flight response to updated METAR and PIREP",
      "decision_point_description": "Whether to request additional holding fuel or begin building a diversion picture after the updated METAR and PIREP indicated fog was persisting.",
      "affected_reasoning_operation": "Risk reassessment and contingency triggering under updated weather evidence",
      "bias_specific_mechanism": "The participant retained the original dispatch plan as the default and continued toward the destination because the update was not seen as dramatic and because no external party amended the plan. This persistence narrowed margins rather than triggering proactive contingency action.",
      "manifestation_in_interview": "After the ACARS METAR still showed half-mile visibility and a PIREP reported a landing after two attempts at minimums, the participant considered proactive holding fuel and early diversion but decided to continue toward the field.",
      "effect_on_reasoning_or_decision": "The decision reduced proactive margin-building and preserved the original arrival plan despite weakening weather information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We talked about it for a minute. I called dispatch to check in, and they acknowledged it was running a little behind the forecast but didn't amend anything on their end. Fuel was still on profile for the planned arrival, just with less room for extended holding than I'd have liked. Since dispatch wasn't changing the release, and the delay didn't seem dramatic yet, we kept proceeding toward the field and started working the descent.",
          "evidence_explanation": "The participant explicitly acknowledges updated weather information but keeps the original plan in place, partly because the release was not externally amended and the deviation did not yet feel large."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We could've asked for holding fuel proactively, or had dispatch start building an early diversion picture. We didn't do either — it felt premature at that point, since one lagging METAR isn't necessarily a trend.",
          "evidence_explanation": "This identifies viable alternatives that were not taken because the emerging trend was treated as premature, consistent with persistence in the original plan."
        }
      ],
      "correction_or_counterevidence": "A single lagging METAR was not necessarily a definitive trend, fuel was on profile, and continuing was legally permitted. The behavior is also partly ordinary decision-making under uncertainty, so the occurrence is coded at low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context; the label and mechanism are assigned from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "confirmation_bias",
      "alternative_labels": [
        "expectation bias",
        "confirmatory bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's existing expectations or beliefs.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Approach briefing and decision to continue after ATIS and tower reports",
      "decision_point_description": "Whether to continue the approach or divert to the alternate after ATIS showed visibility at minimums and the tower reported two recent landings and one missed approach.",
      "affected_reasoning_operation": "Interpretation of mixed arrival evidence and probability of successful approach",
      "bias_specific_mechanism": "The participant treated the two recent successful landings and the forecast improvement as confirmatory of the expected breakout, while the recent missed approach was acknowledged but not allowed to shift the interpretation. Ambiguous evidence was assimilated into the original expectation.",
      "manifestation_in_interview": "The participant selected and weighted information consistent with the prior expectation that fog would clear at the destination and concluded that the overall picture matched what was expected, despite one of the last three arrivals going missed.",
      "effect_on_reasoning_or_decision": "The approach was briefed and flown as normal rather than diverting, preserving the original plan and reducing the likelihood of a proactive diversion decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We could have diverted straight to the alternate right then instead of shooting the approach. But two of the three recent arrivals had gotten in, and the forecast had always called for improvement by our arrival window, so I expected we'd break out. We briefed it as a normal approach and continued.",
          "evidence_explanation": "This shows confirmation-oriented weighting: the two successes and the forecast changed the interpretation of the destination's viability, while the miss from the third aircraft did not shift the plan."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We noted it, but it didn't really shift the plan. We were still within minimums, legally fine to try, and the overall picture matched what we'd expected going in.",
          "evidence_explanation": "The explicit statement that the overall picture matched prior expectation despite mixed evidence is a direct example of confirmatory assimilation."
        }
      ],
      "correction_or_counterevidence": "The decision was legally within minimums, two of three recent arrivals had landed successfully, and the forecast had called for improvement; therefore a non-bias explanation is plausible. The go-around report was acknowledged but not treated as a dominating trend, so this is coded at low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context; the label and mechanism are assigned from established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "normalcy_bias",
      "alternative_labels": [
        "optimism_bias",
        "overconfidence_effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial acceptance of dispatch fuel load",
      "supporting_interview_quote": "Honestly, I felt fine about it. The forecast lined up with what I'd typically seen there — fog clears out once the sun gets some angle on it. Nothing about the release stood out as unusual.",
      "plausible_mechanism": "Familiarity with a typical fog pattern may have led to an expectation that the normal improvement would recur, reducing concern about the tight margin between the improvement time and ETA.",
      "why_not_identified": "The forecast and dispatch release supported the plan, and there was no contradictory evidence at that early point. The reasoning is plausibly legitimate use of domain experience and standard operational practice rather than a clearly evidenced cognitive distortion."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus was supplied; labeling relies on established cognitive-science knowledge rather than task-specific retrieval evidence.",
    "The transcript is retrospective and self-reported, so occurrences are based on the participant's account rather than direct observation of cockpit behavior.",
    "Low-confidence findings are included because the evidence is affirmative but accompanied by plausible non-bias explanations."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Biased_2_Gemini_off",
  "interview_id": "AV_Biased_2",
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
