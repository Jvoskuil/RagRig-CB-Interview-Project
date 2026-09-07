You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "AV_Biased_2",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
