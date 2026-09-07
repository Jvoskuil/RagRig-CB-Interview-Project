You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "RT_Biased_3",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Yardmaster / Rail Yard Supervisor",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Night Shift Hump Yard Congestion and Suspected Hot Bearing",
    "scenario_summary_internal": "During a night shift with only one working hump lead (the other closed for signal maintenance) and a carman shortage aggravated by a storm, the yardmaster must classify and release a mixed freight train to meet a customer SLA connection window. A prior-shift switch list gives an initial car-count and ready-time estimate. A wheel-bearing hot-box detector flags a car in the cut at a borderline reading, evoking memory of a derailment three weeks earlier at the same yard caused by an overheated bearing. The yardmaster forms a working hypothesis that a specific car has a coupler/mechanical defect and selectively weighs subsequent carman reports before making a final dispatch call under time pressure.",
    "occupational_realism": {
      "objective": "Classify and safely dispatch an inbound mixed freight cut through the hump yard in time to meet an outbound connection with a contractual SLA penalty, without compromising mechanical safety.",
      "setting": "Class I railroad classification (hump) yard control tower, night shift, moderate rain reducing visibility, one of two hump leads closed for signal maintenance.",
      "constraints": [
        "Only one working hump lead available",
        "Carman crew reduced by two due to storm callouts",
        "Outbound connection deadline with customer SLA penalty",
        "Wet rail reducing retarder braking predictability",
        "Prior-shift paperwork handed off verbally during a rushed relief briefing"
      ],
      "stakeholders": [
        "Yardmaster (interviewee)",
        "Relief yardmaster (prior shift)",
        "Two carmen (car inspectors)",
        "Hump conductor / switchman crew",
        "Train dispatcher (network control)",
        "Customer service desk (SLA owner)"
      ],
      "technical_terms_to_use": [
        "hump lead",
        "bad order",
        "switch list",
        "hot-box detector",
        "knuckle",
        "retarder",
        "cut of cars",
        "bowl track",
        "consist",
        "SLA connection window"
      ],
      "technical_terms_to_avoid": [
        "anchoring effect",
        "availability heuristic",
        "confirmation bias",
        "cognitive bias",
        "heuristic",
        "base rate"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Prior shift's switch list states 38 cars, estimated classification-complete by 2200",
          "Relief briefing was rushed due to shift-change storm delays",
          "Inbound train reported running 40 minutes late by the road crew"
        ],
        "new_information_after_decision": [
          "Actual car count on arrival is 41, three more than the switch list indicated",
          "Storm has slowed retarder cycle times, extending classification beyond normal pace"
        ],
        "alternatives": [
          "Recalculate the ready-time estimate from scratch using current car count and observed retarder cycle speed",
          "Keep the 2200 target from the switch list and only make minor mental adjustments",
          "Request an updated estimate directly from the hump conductor before committing to a target"
        ],
        "intended_action": "Yardmaster keeps the 2200 figure as the working target, adjusting only slightly despite the higher car count and slower cycle time."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Hot-box detector flags car GATX 88213 at a borderline temperature reading, within tolerance but elevated",
          "Detector history at this location has produced false positives in wet weather",
          "Three weeks earlier, an overheated bearing on a similar car caused a derailment at this yard"
        ],
        "new_information_after_decision": [
          "A full cut-pull inspection of eleven cars is ordered, consuming crew time already short due to storm callouts",
          "The carman assigned reports the reading is consistent with normal wet-rail sensor variance"
        ],
        "alternatives": [
          "Flag only the single indicated car for a standard visual and manual temperature check per procedure",
          "Pull the entire eleven-car cut for inspection out of caution",
          "Continue classification and reassess the detector reading at the next scheduled pass"
        ],
        "intended_action": "Yardmaster orders the full cut pulled for inspection, citing the earlier derailment, well beyond what the borderline reading and detector history would typically warrant."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Carman A reports a hairline mark near the coupler knuckle on GATX 88213, unrelated to the bearing alarm",
          "Carman B, inspecting the same car independently, reports no defect found and clears the car",
          "A paperwork discrepancy shows GATX 88213 was flagged for a minor repair two inspection cycles ago, now closed"
        ],
        "new_information_after_decision": [
          "Yardmaster logs the car as suspect and requests a third inspection pass, delaying the cut further",
          "Carman B's clearance is not recorded in the shift log as a factor in the decision"
        ],
        "alternatives": [
          "Weigh both carmen's reports equally and default to the standard resolution procedure for conflicting inspections",
          "Accept Carman B's clearance since it followed the same protocol and timeframe as Carman A's mark",
          "Escalate the conflicting reports to the car foreman for an independent tie-breaking inspection"
        ],
        "intended_action": "Yardmaster treats Carman A's hairline-mark report and the old repair-history entry as confirming a defect, while discounting Carman B's clearance as insufficiently thorough."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Classification is now running roughly 55 minutes behind the original target",
          "The SLA connection window closes in 40 minutes",
          "GATX 88213 has been set aside pending the third inspection pass; the rest of the cut is ready"
        ],
        "new_information_after_decision": [
          "Dispatcher confirms the outbound train can depart without GATX 88213, incurring a partial rather than full SLA penalty",
          "The third inspection later clears GATX 88213 with no defect found"
        ],
        "alternatives": [
          "Hold the entire train until GATX 88213's status is resolved",
          "Set out GATX 88213 and dispatch the remainder of the cut to partially meet the SLA window",
          "Request a short extension from the dispatcher to complete the third inspection before departure"
        ],
        "intended_action": "Yardmaster sets out GATX 88213 and dispatches the rest of the train, a judgment call balanced against genuine competing constraints rather than a biased inference."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this shift's objective was and what made it nonroutine?",
        "What information did you have at the very start of the shift, and where did it come from?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events in the order they happened.",
        "At each stage, what changed compared to what you expected going in?"
      ],
      "decision_point_probes": [
        "What options did you consider at that moment, and why did you choose the one you did?",
        "What specific piece of information most influenced that call?",
        "Did anything from earlier in the shift, or from past experience, shape how you read this situation?",
        "How did you weigh the different reports or data points you received?",
        "Looking back, was there information you didn't use as much as you could have?"
      ],
      "closing_hypotheticals": [
        "If the hot-box detector had never triggered, how do you think the shift would have gone?",
        "If Carman B's clearance had come in before Carman A's report, would that have changed your decision?",
        "How much did the earlier derailment weigh on you during this shift, if at all?",
        "If you had to make the same set of decisions again tomorrow, what would you do differently, if anything?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "an_01",
        "bias": "Anchoring Effect",
        "decision_point": 1,
        "mechanism": "Initial numeric/time estimate from the prior shift's switch list (2200 ready-time, 38 cars) is insufficiently adjusted despite new, materially different information (41 cars, slower retarder cycling in the rain).",
        "affected_reasoning_operation": "Estimation and revision of a target completion time under new evidence",
        "evidence_available_at_time": [
          "Switch list stating 38 cars / 2200 target",
          "Actual arrival count of 41 cars",
          "Observed slower retarder cycle time due to wet rail"
        ],
        "required_textual_manifestation": "Yardmaster explicitly references sticking with the 2200 figure or making only a small mental tweak to it, rather than recalculating from the new car count and cycle speed.",
        "plausible_nonbias_interpretation": "Could be read as reasonable trust in a handoff estimate from an experienced relief yardmaster under time pressure.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "anchoring",
          "initial estimate bias",
          "insufficient adjustment"
        ]
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "The vivid, emotionally salient memory of a recent derailment caused by an overheated bearing disproportionately drives the probability/severity assessment of a borderline, statistically unremarkable hot-box reading, overriding the known false-positive rate of the detector in wet conditions.",
        "affected_reasoning_operation": "Risk assessment and response-scaling to a sensor alert",
        "evidence_available_at_time": [
          "Borderline hot-box detector reading",
          "Known history of false positives at this detector location in wet weather",
          "Recent memory of a derailment three weeks earlier involving a similar defect"
        ],
        "required_textual_manifestation": "Yardmaster's stated rationale for pulling the full eleven-car cut explicitly invokes the recent derailment memory as the driving reason, disproportionate to the borderline/ordinary nature of the reading.",
        "plausible_nonbias_interpretation": "Could be read as appropriately cautious safety margin-setting by an experienced supervisor.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "availability bias",
          "recency of memory",
          "salience"
        ]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3,
        "mechanism": "After forming a working hypothesis that the car is defective, the yardmaster selectively weights Carman A's ambiguous mark and an unrelated closed repair-history entry as corroborating evidence, while discounting Carman B's independent clearance that followed the same protocol.",
        "affected_reasoning_operation": "Evaluation and integration of conflicting evidence sources against a pre-existing hypothesis",
        "evidence_available_at_time": [
          "Carman A's report of a hairline mark near the knuckle",
          "Carman B's independent clearance finding no defect",
          "A closed, unrelated repair-history entry for the same car"
        ],
        "required_textual_manifestation": "Yardmaster explains treating Carman A's report and the old repair note as confirming the suspicion while characterizing Carman B's clearance as less credible or incomplete, without a stated procedural justification for the asymmetry.",
        "plausible_nonbias_interpretation": "Could be read as a defensible safety-first tie-breaking judgment favoring the more cautious of two conflicting reports.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "confirmation bias",
          "selective weighting",
          "discounting disconfirming evidence"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased', not a control condition."
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
      "Exactly 4 decision points are present, each with at least two alternatives.",
      "Exactly 3 intended bias instances planned (an_01, av_01, cb_01), matching the manifest total of 3.",
      "Each bias instance occupies its own decision point (1, 2, 3 respectively); decision point 4 is deliberately bias-free to serve as a genuine multi-constraint trade-off.",
      "No bias labels or psychological terminology appear in technical_terms_to_use, probe_plan, or timeline entries.",
      "Each instance has a plausible non-bias interpretation to avoid mechanically proving bias from outcome alone.",
      "Target word count (1,215-1,485 words) is achievable given 4 decision points with moderate probe depth and no repetitive exposition.",
      "Consequences (SLA penalty avoided partially, GATX 88213 later cleared) do not conclusively prove any decision was biased."
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
