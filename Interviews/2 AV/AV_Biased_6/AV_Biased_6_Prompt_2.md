You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "AV_Biased_6",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Flight Dispatcher / Flight Operations Officer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "JFK–LIS Overnight Dispatch: Fog Trend, MEL Constraint, and Late Diversion Call",
    "scenario_summary_internal": "A flight dispatcher plans and monitors an overnight transatlantic flight (JFK to Lisbon, widebody twin) during a period of developing coastal fog at the destination, compounded by a deferred APU (MEL) item that limits ground-power options at the planned alternate. The dispatcher's initial fuel/alternate release is built around an early-morning TAF, and subsequent judgments during the flight are progressively shaped by that initial figure and by a preference for information confirming the original plan, culminating in a late top-of-descent decision to continue toward Lisbon rather than divert early.",
    "occupational_realism": {
      "objective": "Produce a compliant, safe, and operationally efficient dispatch release for an overnight JFK–LIS flight, and monitor/support the flight through changing destination weather and an aircraft maintenance limitation.",
      "setting": "Airline dispatch operations center, overnight shift, dispatcher responsible for release preparation, oceanic routing coordination, and real-time flight-watch monitoring via ACARS/weather feeds.",
      "constraints": [
        "APU inoperative (MEL item) limits electrical/air-conditioning options at alternate without ground power unit availability",
        "Fog trend forecast for Lisbon (LIS) with TAF amendments issued over several hours",
        "Alternate airport (Porto, OPO) has limited ground-power/GPU support after midnight local",
        "North Atlantic oceanic track fuel and reroute constraints limit late track changes",
        "Crew duty-time limits create pressure to avoid extended holding or diversion delay",
        "Company on-time performance and fuel-cost targets create implicit efficiency pressure"
      ],
      "stakeholders": [
        "Flight Dispatcher / Flight Operations Officer (interviewee)",
        "Captain and First Officer of the flight",
        "Duty Manager / Operations Control Center supervisor",
        "Meteorology desk / contract weather provider",
        "Ground handling agent at Porto (alternate)",
        "Maintenance control (regarding MEL APU item)"
      ],
      "technical_terms_to_use": [
        "TAF/METAR", "dispatch release", "MEL (Minimum Equipment List)", "alternate minima", "fuel reserve", "oceanic track message", "top of descent", "GPU (ground power unit)", "trend forecast", "holding fuel", "diversion", "flight watch"
      ],
      "technical_terms_to_avoid": [
        "anchoring", "confirmation bias", "plan continuation bias", "substitution bias", "information bias", "subjectivity", "cognitive bias", "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "0300Z TAF for LIS showing marginal visibility improving by ETA",
          "APU MEL item requiring GPU at any diversion airport",
          "Porto (OPO) listed as primary alternate with GPU available until 0500 local",
          "Standard fuel policy requires alternate + reserve + contingency fuel"
        ],
        "new_information_after_decision": [
          "Later TAF amendment (issued after release) shows fog onset earlier than first forecast"
        ],
        "alternatives": [
          "Release with minimum required alternate/contingency fuel based on the early TAF",
          "Add extra fuel and/or select a second alternate with round-the-clock GPU support given fog risk profile"
        ],
        "intended_action": "Dispatcher finalizes release using the early TAF figure and standard fuel policy, treating that number as the reference point for the remainder of the flight-watch."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Amended TAF showing fog onset two hours earlier than original forecast",
          "One meteorology model run still shows improving trend consistent with original plan",
          "Another model run and a pilot report (PIREP) from an earlier arrival suggest faster deterioration"
        ],
        "new_information_after_decision": [
          "Crew reports LIS tower now broadcasting reduced visibility procedures"
        ],
        "alternatives": [
          "Weight the deteriorating model run and PIREP equally or more heavily and revise fuel/alternate guidance",
          "Continue relying on the improving model run that matches the original release"
        ],
        "intended_action": "Dispatcher relays a flight-watch update that emphasizes the forecast consistent with the original plan and characterizes the conflicting data as less reliable."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Crew requests a fresh risk assessment for continuing versus early diversion planning",
          "Available data: extended satellite loop imagery, additional METARs from nearby stations, current fuel state, GPU availability window at Porto",
          "The core operational question is whether overall approach/diversion risk at LIS is acceptable given the MEL constraint"
        ],
        "new_information_after_decision": [
          "Porto ground handling confirms GPU cutoff time is earlier than previously logged"
        ],
        "alternatives": [
          "Directly assess whether visibility/ceiling and GPU-window risk together support continuing to LIS",
          "Answer a narrower, easier-to-verify question (fuel sufficiency) and treat that as resolving the broader risk question"
        ],
        "intended_action": "Dispatcher reviews the extended imagery in detail, treats the added volume of data as reassuring without it changing the diagnostic picture, and responds to the crew's broader risk question mainly in terms of fuel sufficiency."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Near top of descent, LIS visibility now near alternate minima and trending down",
          "GPU window at Porto closing within the diversion flight-time margin",
          "Crew asks dispatcher for a clear recommendation: continue approach sequence or divert now"
        ],
        "new_information_after_decision": [
          "LIS visibility drops briefly below landing minima before recovering, requiring a short hold",
          "Post-flight the dispatcher logs the event summary for the operations file"
        ],
        "alternatives": [
          "Recommend diverting to Porto immediately while the GPU window remains open",
          "Recommend continuing the approach sequence to LIS as originally planned"
        ],
        "intended_action": "Dispatcher recommends continuing to LIS, consistent with the original release plan, and later records the weather judgment in the operations log as a settled fact rather than as a judgment made under uncertainty."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this flight and shift looked like before anything unusual happened?",
        "What was your main objective when you built the original release?"
      ],
      "timeline_reconstruction": [
        "What information did you have in front of you at each stage, in order?",
        "When did new weather or maintenance information arrive, and how did you first react to it?"
      ],
      "decision_point_probes": [
        "What sources did you weigh most heavily at that point, and why?",
        "What alternatives did you consider, and what made you choose the one you did?",
        "How confident were you in that call at the time, and what would have changed your mind?",
        "Looking back, was there any information you set aside or treated as less important?"
      ],
      "closing_hypotheticals": [
        "If the PIREP had come in before you finalized the release, would anything have changed?",
        "If the GPU cutoff time had been flagged an hour earlier, what would you have done differently?",
        "How would you describe the level of certainty behind your final recommendation to someone reviewing the file later?",
        "What would you tell a newer dispatcher to watch for in a situation like this?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "AV6_anchor_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Dispatcher fixes the fuel/alternate figure to the earliest available TAF and continues to use that figure as the reference baseline even as later information becomes available, rather than treating it as a provisional starting estimate",
        "affected_reasoning_operation": "Initial numerical/risk estimate formation and its persistence as a reference point",
        "evidence_available_at_time": ["0300Z TAF for LIS", "standard fuel policy minimums", "APU MEL constraint"],
        "required_textual_manifestation": "Dispatcher explicitly states the release fuel/alternate figure was set from the early TAF and that later checks were framed as confirming or adjusting that same number rather than as fresh, independent assessments",
        "plausible_nonbias_interpretation": "Using the earliest official TAF is standard, policy-compliant dispatch practice and does not by itself indicate anchoring",
        "strength": "subtle",
        "do_not_make_explicit": ["anchoring", "reference point", "cognitive bias"]
      },
      {
        "instance_id": "AV6_confirm_01",
        "bias": "Confirmation Bias",
        "decision_point": 2,
        "mechanism": "When two conflicting data sources (an improving model run vs. a deteriorating model run plus PIREP) appear, dispatcher gives more credence and airtime to the source matching the original plan and discounts the contradictory PIREP/model as less reliable without an equivalent evidentiary basis for that judgment",
        "affected_reasoning_operation": "Evaluation and weighting of conflicting evidence during an update",
        "evidence_available_at_time": ["amended TAF", "two conflicting meteorology model runs", "PIREP from an earlier arrival"],
        "required_textual_manifestation": "Dispatcher describes relaying the update to the crew in a way that foregrounds the improving-trend model and frames the PIREP/deteriorating run as an outlier, without citing a specific technical reason the PIREP was less credible",
        "plausible_nonbias_interpretation": "Model runs do genuinely vary in skill and a dispatcher reasonably favoring the higher-resolution or more recent model is a legitimate meteorological judgment",
        "strength": "moderate",
        "do_not_make_explicit": ["confirmation bias", "selective weighting", "motivated reasoning"]
      },
      {
        "instance_id": "AV6_infobias_01",
        "bias": "Information bias",
        "decision_point": 3,
        "mechanism": "Dispatcher seeks out and reviews an extended volume of supplementary data (extended satellite loop, extra METARs) believing more data collection itself increases decision quality, even though the additional data does not change the diagnostic picture or alter the eventual recommendation",
        "affected_reasoning_operation": "Evidence-gathering and perceived value of additional information prior to acting",
        "evidence_available_at_time": ["extended satellite imagery loop", "additional nearby METARs", "current fuel state", "GPU availability window"],
        "required_textual_manifestation": "Dispatcher recounts spending meaningful time reviewing the extra imagery/METARs and describes feeling more confident afterward, while the actual content of that additional review is acknowledged (in hindsight) not to have changed the assessment",
        "plausible_nonbias_interpretation": "Reviewing more current weather data before an approach-risk judgment is a reasonable due-diligence step regardless of outcome",
        "strength": "subtle",
        "do_not_make_explicit": ["information bias", "value of information", "illusion of thoroughness"]
      },
      {
        "instance_id": "AV6_substitution_01",
        "bias": "Substitution bias",
        "decision_point": 3,
        "mechanism": "In response to the crew's harder question (is the overall continue/divert risk acceptable given weather trend and the GPU/MEL constraint), the dispatcher substitutes and answers a narrower, easier-to-evaluate question (is there enough fuel reserve) and treats that answer as resolving the original question",
        "affected_reasoning_operation": "Question interpretation and answer substitution when responding to a complex risk query",
        "evidence_available_at_time": ["current fuel state", "reserve/contingency fuel policy", "GPU cutoff time", "visibility trend at LIS"],
        "required_textual_manifestation": "Dispatcher's account of the reply to the crew centers on fuel sufficiency figures as the basis for reassurance, without separately addressing the visibility/GPU-window risk that was actually asked about",
        "plausible_nonbias_interpretation": "Fuel state is a necessary and legitimate input to any diversion decision, so citing it is not inherently improper",
        "strength": "moderate",
        "do_not_make_explicit": ["substitution bias", "easier question", "attribute substitution"]
      },
      {
        "instance_id": "AV6_plancont_01",
        "bias": "Plan Continuation",
        "decision_point": 4,
        "mechanism": "Despite visibility trending toward/below alternate minima and a closing GPU window, dispatcher recommends continuing the original LIS approach plan rather than triggering an early diversion, giving disproportionate weight to sticking with the original release plan as conditions worsen",
        "affected_reasoning_operation": "Final go/continue vs. divert recommendation under worsening real-time conditions",
        "evidence_available_at_time": ["current LIS visibility trend near minima", "closing Porto GPU window", "remaining fuel/time margin", "original release plan"],
        "required_textual_manifestation": "Dispatcher explains recommending continuation to LIS at top of descent by referring back to the original plan and release assumptions rather than re-deriving the decision fresh from the current trend and GPU-window data",
        "plausible_nonbias_interpretation": "Continuing may have been the objectively correct call given the fuel and time margins actually available, independent of any attachment to the original plan",
        "strength": "moderate",
        "do_not_make_explicit": ["plan continuation", "sunk cost", "escalation of commitment"]
      },
      {
        "instance_id": "AV6_omitsubj_01",
        "bias": "Omitting subjectivity",
        "decision_point": 4,
        "mechanism": "In the post-event operations log, dispatcher records the weather/continue judgment as a settled, objective fact ('conditions were acceptable for continuation') without flagging that it was a judgment call made under uncertain and conflicting information",
        "affected_reasoning_operation": "Retrospective documentation and communication of a judgment made under uncertainty",
        "evidence_available_at_time": ["the dispatcher's own real-time uncertainty during decision point 4", "conflicting weather trend data", "final log entry drafted after the flight landed"],
        "required_textual_manifestation": "Dispatcher describes writing or having written the log summary in definitive terms ('the decision was straightforward,' 'conditions supported continuing') rather than noting the uncertainty and conflicting signals present at the time",
        "plausible_nonbias_interpretation": "Operational logs are often written concisely and directive language may just reflect standard reporting style rather than concealment of uncertainty",
        "strength": "subtle",
        "do_not_make_explicit": ["omitting subjectivity", "false objectivity", "uncertainty concealment"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for this condition; no paired control scenario was supplied."
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
      "Confirm exactly 4 decision points appear in the timeline and interview.",
      "Confirm each of the 6 named biases has exactly 1 embedded instance with a unique instance_id.",
      "Confirm decision point 3 and 4 each carry two distinct biases from different mechanism families, with no bias repeated at the same decision point.",
      "Confirm no bias name, definition, or explicit psychological label appears in the public interview text.",
      "Confirm each instance has an available plausible non-bias explanation preserved in the interview's ambiguity.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm final consequences (brief hold, safe landing) do not mechanically confirm or refute whether any decision was biased.",
      "Confirm total word count target of 1,350 (range 1,215-1,485) is achievable without repeating any single bias instance in multiple places."
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
