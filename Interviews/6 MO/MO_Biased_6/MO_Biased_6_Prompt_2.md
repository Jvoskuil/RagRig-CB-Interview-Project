You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MO_Biased_6",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Port Captain / Terminal Operations Manager",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Gusting Crosswind Berthing and Discharge of MV Nordic Star",
    "scenario_summary_internal": "A Port Captain manages the berthing, pilotage, and STS crane discharge of a container vessel as a forecast wind system deteriorates through the day. Schedule pressure from a tight tidal window and an incoming next vessel push the captain and team toward continuing with the original plan despite escalating wind data, favorable framing of transit risk, quiet team consensus, and confidence in personal and crew capability that outruns the marginal instrument readings. No accident occurs, but a near-miss fender contact and an automatic crane wind-alarm event punctuate the shift, leaving the soundness of the underlying judgments genuinely debatable.",
    "occupational_realism": {
      "objective": "Safely berth MV Nordic Star within its tidal window and complete scheduled STS crane discharge before the berth must be vacated for the next vessel.",
      "setting": "Container terminal Operations Control Center and quayside, single shift from 06:00 morning weather bulletin through afternoon cargo discharge.",
      "constraints": [
        "Tidal window for berthing closes at 14:00",
        "Next vessel scheduled to occupy the same berth at 18:00, creating knock-on schedule pressure",
        "STS crane OEM soft-limit guidance recommends operational review above 25 knots sustained / 32 knots gusting",
        "Only two tugs and one duty pilot available for the shift",
        "Charter party laytime clock is running, creating commercial pressure to avoid delay"
      ],
      "stakeholders": [
        "Port Captain (interviewee)",
        "Duty Pilot",
        "Two Shift Supervisors",
        "Terminal Operations Director",
        "Vessel Master, MV Nordic Star",
        "Junior Operations Engineer (crane systems)",
        "Port Meteorological Service"
      ],
      "technical_terms_to_use": [
        "STS (ship-to-shore) crane",
        "gust factor",
        "wind limit envelope",
        "pilotage",
        "tug assist",
        "berth window",
        "laytime",
        "anemometer reading",
        "bollard pull",
        "wind alarm trip"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "anchoring",
        "framing",
        "groupthink",
        "overconfidence",
        "heuristic",
        "cognitive",
        "status quo"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Berthing plan approved the previous evening based on a 20-knot wind forecast",
          "06:00 weather bulletin revises gusts to 28 knots, trending toward 32 knots by afternoon",
          "Tidal window closes at 14:00; next vessel occupies berth at 18:00"
        ],
        "new_information_after_decision": [
          "By midday, sustained gusts confirmed at 27 knots with a continuing rising trend"
        ],
        "alternatives": [
          "Proceed with the previously published berthing plan unchanged",
          "Request a revised wind risk assessment and consider shifting the berthing window earlier",
          "Delay berthing pending a clearer forecast"
        ],
        "intended_action": "Proceed with the original plan, treating the updated bulletin as within the range already anticipated."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pilot's operational log: 18 of last 20 similar-condition transits completed without incident",
          "STS crane manufacturer envelope allows operations up to 30 knots sustained gusts",
          "Vessel has bow thruster; two tugs available"
        ],
        "new_information_after_decision": [
          "Transit completed but with a near-miss fender contact during final approach due to a gust"
        ],
        "alternatives": [
          "Proceed with pilotage as planned, citing the high historical success rate",
          "Request additional tug support and a reduced speed profile",
          "Postpone the transit until wind eases"
        ],
        "intended_action": "Proceed with pilotage, endorsing the plan based on the favorable success statistic and personal past experience."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "OEM soft-limit guidance recommends pausing for review above 25 knots sustained / 32 knots gusting",
          "Two supervisors privately expressed concern to each other before the meeting",
          "Captain outlines a plan to proceed with a reduced lift rate"
        ],
        "new_information_after_decision": [
          "A gust spike later triggers the automatic crane wind alarm, requiring temporary suspension"
        ],
        "alternatives": [
          "Proceed with reduced-rate lifting as proposed",
          "Pause operations until anemometer readings stabilize",
          "Formally escalate the concern to the Terminal Operations Director for a second opinion"
        ],
        "intended_action": "Team reaches quick unanimous agreement to proceed; meeting closes without recorded objection."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Automatic wind alarm has reset after a brief gust spike",
          "Anemometer shows 24 knots sustained but fluctuating near the alarm threshold",
          "Junior operations engineer recommends waiting 30 minutes for confirmed stabilization",
          "Next vessel's imminent arrival creates renewed schedule pressure"
        ],
        "new_information_after_decision": [
          "Cargo discharge completes with only a minor delay and no further alarm trips"
        ],
        "alternatives": [
          "Resume immediately, trusting crane operators to manage fluctuating winds",
          "Wait for the stabilization window recommended by the engineer",
          "Request updated meteorological confirmation before resuming"
        ],
        "intended_action": "Resume immediately, citing confidence in operator skill despite fluctuating readings."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were responsible for on this shift.",
        "What was the operational objective when the shift began?"
      ],
      "timeline_reconstruction": [
        "What did the 06:00 weather bulletin show compared to the previous evening's plan?",
        "What happened during the pilotage of MV Nordic Star?",
        "What was discussed in the operations meeting before discharge began?",
        "What happened after the wind alarm tripped?"
      ],
      "decision_point_probes": [
        "What cues told you the original plan still made sense (or didn't)?",
        "What information sources did you rely on at each point, and how much weight did you give each?",
        "What goals were you weighing against each other?",
        "What alternatives did you consider, and why did you rule them out?",
        "What was the basis for your final call at each stage?",
        "How did your past experience with similar wind conditions shape your thinking?",
        "How much time pressure did you feel, and how did that affect the decision?",
        "How confident were you in your assessment at the time, versus in hindsight?",
        "What was still uncertain when you made the call?"
      ],
      "closing_hypotheticals": [
        "If the 06:00 bulletin had shown 32 knots instead of 28, would your initial decision have changed?",
        "If the pilot had framed the transit as a '1 in 20 chance of incident,' would you have proceeded the same way?",
        "If a supervisor had voiced an objection in the meeting, do you think the outcome would have changed?",
        "If the junior engineer's 30-minute wait had been enforced, what do you think would have been different?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Status Quo Bias",
        "decision_point": 1,
        "mechanism": "Preference for retaining the pre-existing, already-approved berthing plan despite updated wind information that would normally warrant reassessment.",
        "affected_reasoning_operation": "Plan revision / threshold for triggering re-evaluation",
        "evidence_available_at_time": [
          "Previous evening's 20-knot forecast and approved plan",
          "06:00 bulletin showing rising trend to 28 knots"
        ],
        "required_textual_manifestation": "Captain notes the plan was 'already agreed' and sees no reason to reopen it, treating the new bulletin as not warranting a fresh review.",
        "plausible_nonbias_interpretation": "A reasonable operational preference for stability, avoiding unnecessary disruption until a clearer confirmed trend emerges.",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo", "resistance to change", "default option"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Continued reference to the original 20-knot figure when interpreting the significance of the new 28-32 knot bulletin, insufficiently adjusting the risk estimate.",
        "affected_reasoning_operation": "Numerical risk estimation and updating in light of new evidence",
        "evidence_available_at_time": [
          "Initial planning forecast of 20 knots",
          "Updated bulletin trending 28 to 32 knots"
        ],
        "required_textual_manifestation": "Captain frames the new reading relative to the original number ('still not far off what we planned for') rather than evaluating it on its own terms.",
        "plausible_nonbias_interpretation": "Cautious, incremental interpretation of a single updated bulletin pending confirmation of the trend.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "initial estimate bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Framing Bias",
        "decision_point": 2,
        "mechanism": "Risk information presented and accepted in a positively framed form ('95% of similar transits succeed') rather than an equivalent negative frame, shifting the decision toward proceeding.",
        "affected_reasoning_operation": "Risk evaluation from a probabilistic statement",
        "evidence_available_at_time": [
          "Pilot's log showing 18 of 20 prior similar transits succeeded"
        ],
        "required_textual_manifestation": "Captain repeats and leans on the success-rate phrasing as the central justification for proceeding, without independently restating the failure rate.",
        "plausible_nonbias_interpretation": "Reasonably trusting an experienced pilot's aggregated operational data.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "positive frame", "negative frame"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Overconfidence Bias",
        "decision_point": 2,
        "mechanism": "Excessive confidence in personal past experience handling similar wind conditions, overriding the need for added margin (extra tug, reduced speed).",
        "affected_reasoning_operation": "Self-assessed capability judgment used to justify proceeding",
        "evidence_available_at_time": [
          "Captain's personal recollection of past similar transits"
        ],
        "required_textual_manifestation": "Captain states something like 'I've handled winds like this dozens of times, I know how the vessel will behave,' offered as sufficient justification without acknowledging residual uncertainty.",
        "plausible_nonbias_interpretation": "Legitimate expertise reasonably informing judgment under uncertainty.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence", "miscalibration"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "Team converges quickly on the captain's proposed plan without surfacing pre-existing private reservations, prioritizing apparent consensus over voiced dissent.",
        "affected_reasoning_operation": "Collective judgment aggregation and suppression of dissent",
        "evidence_available_at_time": [
          "Two supervisors' private concerns expressed to each other before the meeting",
          "Rapid, unopposed agreement in the meeting itself"
        ],
        "required_textual_manifestation": "Captain recalls 'everyone was on board, nobody objected,' while the narrative separately reveals supervisors had reservations they did not raise in the room.",
        "plausible_nonbias_interpretation": "Genuine shared professional confidence producing fast, real agreement.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "consensus pressure", "dissent suppression"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Overestimation of the crane operators' collective ability to manage fluctuating, near-threshold wind readings immediately after an alarm event, dismissing a cautious wait recommendation.",
        "affected_reasoning_operation": "Predictive judgment about team/operator performance under uncertainty",
        "evidence_available_at_time": [
          "Junior engineer's recommendation to wait 30 minutes",
          "Fluctuating anemometer readings near the alarm threshold"
        ],
        "required_textual_manifestation": "Captain justifies immediate resumption by citing confidence in the operators' skill, without citing new confirming data to counter the engineer's caution.",
        "plausible_nonbias_interpretation": "Operators may genuinely be skilled enough that the extra wait was unnecessary given marginal readings.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence", "team competence bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition and no paired control is specified in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable for this biased-condition generation task.",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Exactly 6 total bias instances planned across 5 named biases, matching the manifest",
      "Exactly 4 decision points, each with at least two plausible alternatives",
      "No decision point contains more than two instances of the same bias",
      "cb_01 and cb_02 share decision point 1 but use distinct evidence sources (approved plan vs. numeric forecast) and distinct reasoning operations",
      "cb_04 and cb_06 are both Overconfidence Bias but differ in decision point, evidence source, and target of confidence (self vs. team)",
      "No bias term, definition, or explicit psychological label appears in probe or timeline text intended for the public interview",
      "Consequences (near-miss, alarm trip, minor delay) do not conclusively prove any decision was biased",
      "Target interview length 1,350 words (acceptable 1,215-1,485) is achievable given 4 decision points with concise probe-driven answers"
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
