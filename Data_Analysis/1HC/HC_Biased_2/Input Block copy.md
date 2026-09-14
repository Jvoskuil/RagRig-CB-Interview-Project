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
[optional prevalidated segment map; may be absent, empty, null, or invalid]
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[ontology-free RAG JSON output]
</RAG_ANALYSIS_OUTPUT>
