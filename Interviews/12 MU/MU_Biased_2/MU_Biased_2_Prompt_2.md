You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MU_Biased_2",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Geotechnical Engineer / Ground Control Specialist",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Roof Fall Precursor at the 4200 Panel Development Face",
    "scenario_summary_internal": "A geotechnical engineer at an underground metal mine is called in after a contractor crew reports minor rib spalling and unusual dust puffing near a development face that is advancing toward a known fault splay. Over roughly 14 hours, the engineer must decide whether to halt advance, reduce the cut cycle, order additional support, or clear the crew to continue, while balancing production targets, a previous incident he personally investigated (which he attributes largely to a specific junior operator's error rather than ground conditions), and an in-house convergence model he trusts because it performed well on a past, structurally different panel. The incident culminates in a larger, contained roof fall in an adjacent bolted section after the engineer clears the area based on the model's benign forecast, requiring the interview to probe how prior causal attributions and confidence in the model shaped four sequential decisions.",
    "occupational_realism": {
      "objective": "Determine whether the 4200 development face and adjacent bolted heading can continue safely under current ground behavior, or require support upgrades, re-sequencing, or evacuation, while maintaining the shift's advance schedule.",
      "setting": "Underground hard-rock mine, sublevel development heading approaching a mapped fault splay; mixed contractor and mine-employed crew; engineer works from a surface geotech office with intermittent underground inspection visits.",
      "constraints": [
        "Production schedule requires the 4200 face to advance a full round before shift change",
        "Fault splay location is only approximately known from exploration drilling, not fully delineated",
        "Convergence monitoring points near the face have gaps due to recent bolt installation disturbing extensometers",
        "Contractor crew reports are relayed through a shift boss, introducing communication lag",
        "A prior incident report the engineer authored six months earlier attributed a rib failure at a different panel primarily to an operator's aggressive undercutting rather than ground stress"
      ],
      "stakeholders": [
        "Geotechnical Engineer (interviewee)",
        "Shift Boss overseeing the 4200 crew",
        "Contractor drill-and-blast operator",
        "Mine Manager tracking weekly advance targets",
        "Ground control technician monitoring extensometers and convergence stations"
      ],
      "technical_terms_to_use": [
        "rib spalling",
        "convergence monitoring",
        "fault splay",
        "extensometer",
        "ground support density",
        "cut cycle",
        "stress redistribution",
        "scaling",
        "bolt pattern",
        "development face"
      ],
      "technical_terms_to_avoid": [
        "attribution bias",
        "illusion of validity",
        "cognitive bias",
        "heuristic",
        "confirmation",
        "overconfidence"
      ],
      "excluded_themes": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Shift boss reports minor rib spalling and a dust puff near the 4200 face after the last blast",
          "No injuries; crew paused work voluntarily",
          "Extensometer near the face has been offline for two days due to bolt rig interference",
          "Six months earlier, a similar-sounding rib spalling event at Panel 3800 was attributed in the engineer's report to an operator's aggressive undercutting technique"
        ],
        "new_information_after_decision": [
          "The engineer authorizes continued mucking and a visual-only inspection rather than an immediate stop, reasoning that the current crew is more careful than the 3800 operator was",
          "Scaling crew finds slightly larger loose slabs than initially described"
        ],
        "alternatives": [
          "Halt all work at the face pending a full geotechnical inspection",
          "Allow mucking to continue with a visual-only check by the shift boss",
          "Restrict access to a buffer zone and reroute the round sequence"
        ],
        "intended_action": "Engineer authorizes continued mucking based partly on his belief that the current operator's careful technique makes ground-condition causes less likely, given his prior attribution of a similar event to operator error rather than geology."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Scaling crew reports larger-than-expected loose slabs and a hairline fracture pattern not previously logged",
          "Geological mapping shows the face is within 15-20 meters of the projected fault splay, with real position uncertain",
          "No updated convergence data is available due to the offline extensometer"
        ],
        "new_information_after_decision": [
          "The engineer runs the in-house convergence prediction model using nearby (but not adjacent) station data and interprets its low-displacement forecast as confirming stable ground",
          "The ground control technician notes verbally that the model was calibrated on a different rock mass domain but is overruled by the schedule pressure"
        ],
        "alternatives": [
          "Delay the model output's use until a representative extensometer is reinstalled near the face",
          "Treat the fracture pattern as an independent red flag requiring a stop regardless of model output",
          "Rely on the convergence model's forecast to justify proceeding with the round"
        ],
        "intended_action": "Engineer places high confidence in the convergence model's benign forecast and uses it to justify proceeding, because the model performed accurately during a past panel he considers analogous, without adjusting for the model's untested fit to the current fault-proximal domain."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Round is completed; minor further spalling observed in the adjacent bolted heading, not just the development face",
          "Shift boss asks whether additional bolting or mesh should be ordered before the next crew rotation",
          "Mine Manager flags that ordering additional support will push the weekly advance behind target"
        ],
        "new_information_after_decision": [
          "Engineer defers additional support, citing the model's stable forecast and his assessment that the spalling pattern resembles the 3800 incident's operator-driven cause rather than a stress-related one",
          "A ground crack becomes visible along a bolt row in the adjacent heading two hours later"
        ],
        "alternatives": [
          "Order immediate supplemental bolting and mesh in the adjacent heading",
          "Defer additional support pending the next scheduled inspection",
          "Split the difference: install spot bolts only at the fracture location"
        ],
        "intended_action": "Engineer defers the supplemental support order, again attributing the spalling to crew technique rather than reconsidering the ground-stress explanation, and treating the model's earlier reassurance as sufficient basis for confidence."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Visible crack has propagated along the bolt row; ground control technician requests immediate evacuation of the adjacent heading",
          "Model forecast has not been rerun with the new crack data because no new convergence readings exist",
          "Next crew is due to enter the heading within the hour"
        ],
        "new_information_after_decision": [
          "Engineer clears personnel to enter for a brief inspection based on the model's last (unrevised) forecast, believing the crack is a surface phenomenon consistent with the earlier operator-driven interpretation",
          "A larger roof fall occurs in the adjacent bolted section shortly after entry, though no injuries result because the crew evacuates in time following an unrelated alarm"
        ],
        "alternatives": [
          "Deny entry until convergence monitoring is restored and re-evaluated",
          "Allow a brief, monitored inspection entry as the engineer decided",
          "Require full re-support of the heading before any personnel access"
        ],
        "intended_action": "Engineer authorizes entry based on continued trust in the outdated model output and a persistent framing of the spalling as behavior-driven, setting up the final incident without directly proving the reasoning was flawed."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first drew your attention to the 4200 face that shift?",
        "What was your role and what were you responsible for deciding at that point?"
      ],
      "timeline_reconstruction": [
        "What did you know at the moment the shift boss first called in the spalling report?",
        "What changed in your understanding after the scaling crew's second report?",
        "When did you first look at the convergence model output, and what did you do with it?",
        "Take me through the hours between the round completion and the final evacuation."
      ],
      "decision_point_probes": [
        "What alternatives did you consider before authorizing continued mucking after the first report?",
        "What made you confident the spalling pattern was similar to the 3800 incident?",
        "How did you decide the convergence model's forecast was applicable to this location?",
        "What was the technician's concern about the model, and how did you weigh it?",
        "What led you to defer the supplemental support order in the adjacent heading?",
        "What information would have changed your decision to allow entry after the crack appeared?"
      ],
      "prior_experience_probes": [
        "How did the 3800 panel incident shape how you read this situation?",
        "Have you used this convergence model in similar fault-proximal conditions before?"
      ],
      "uncertainty_and_time_pressure_probes": [
        "How much uncertainty did you feel about the fault splay's exact location, and how did that factor in?",
        "How much did the production schedule weigh on your decisions that shift?"
      ],
      "closing_hypotheticals": [
        "If the extensometer near the face had been working the whole time, would your decisions have changed?",
        "If the 3800 incident had never happened, do you think you would have read the spalling differently?",
        "Looking back, what would you do differently if a similar sequence of reports came in again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "decision_point": 1,
        "mechanism": "Engineer attributes the cause of the current spalling event to operator technique/behavior (dispositional cause), by analogy to a past incident he personally attributed to operator error, rather than attributing it to situational/geological factors (stress redistribution near the fault splay) despite comparable surface cues.",
        "affected_reasoning_operation": "Causal attribution of an observed anomaly (rib spalling, dust puff) under incomplete evidence",
        "evidence_available_at_time": [
          "Minor rib spalling and dust puff reported by shift boss",
          "Extensometer offline, no ground-stress data available",
          "Engineer's own prior report attributing a similar-sounding event to operator's aggressive undercutting"
        ],
        "required_textual_manifestation": "In answering why he allowed mucking to continue, the engineer explicitly reasons that the current operator's more careful technique makes the spalling less concerning, drawing a direct comparison to the 3800 operator he blamed previously, without weighing the missing ground-stress data as an alternative cause.",
        "plausible_nonbias_interpretation": "A reasonable engineer might legitimately consider operator technique as one relevant factor among several, especially if the current operator has a known careful track record.",
        "strength": "subtle",
        "do_not_make_explicit": ["attribution bias", "dispositional", "situational", "bias"]
      },
      {
        "instance_id": "iov_01",
        "bias": "Illusion of validity",
        "decision_point": 2,
        "mechanism": "Engineer expresses high confidence in the convergence model's benign forecast based on its past accuracy on a structurally different panel, treating internal consistency of the model's output (and his fluency in reading it) as a signal of predictive validity, without accounting for the model's poor fit to the current fault-proximal, data-sparse domain.",
        "affected_reasoning_operation": "Confidence calibration when interpreting a quantitative forecast under known model-domain mismatch",
        "evidence_available_at_time": [
          "Convergence model output showing low predicted displacement using non-adjacent station data",
          "Ground control technician's verbal caveat that the model was calibrated on a different rock mass domain",
          "Model's strong track record on a past, structurally different panel"
        ],
        "required_textual_manifestation": "The engineer describes trusting the model's forecast strongly enough to justify proceeding, citing its past reliability, while the technician's domain-mismatch caveat is acknowledged but not treated as reducing his confidence in the current prediction.",
        "plausible_nonbias_interpretation": "Relying on a validated in-house model with a track record could be a reasonable engineering judgment call under time pressure and data scarcity.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "overconfidence", "calibration", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control specified in this generation cycle."
    },
    "counterfactual_specification": {
      "causal_variable": "Whether the engineer's prior 3800 incident report attributed the earlier failure to operator error versus ground stress",
      "original_state": "Engineer's prior report attributed the 3800 rib failure primarily to operator's aggressive undercutting technique",
      "counterfactual_state": "Engineer's prior report attributed the 3800 rib failure primarily to unanticipated stress redistribution near a geological structure",
      "variables_to_hold_constant": [
        "Production schedule pressure",
        "Extensometer outage near the 4200 face",
        "Convergence model's domain mismatch",
        "Sequence and content of the four decision points",
        "Scaling crew and technician reports",
        "Final roof fall outcome"
      ],
      "expected_causal_difference": "With a situational prior attribution, the engineer would more readily treat the current spalling as a possible ground-stress signal, likely triggering earlier support upgrades or evacuation rather than deferral.",
      "causal_test_question": "Does changing the causal framing of the engineer's prior incident report (operator error vs. ground stress) alter his interpretation of the current spalling and his willingness to trust the convergence model?"
    },
    "generation_checks": [
      "Confirm exactly one Attribution Bias instance and one Illusion of validity instance are embedded, each at a distinct decision point",
      "Confirm no bias terminology or psychological labels appear in probes or narrative",
      "Confirm four decision points each have at least two alternatives and pre/post decision information",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and probe density",
      "Confirm consequences (final roof fall) do not explicitly confirm or deny whether reasoning was biased",
      "Confirm plausible non-bias explanations exist for both embedded instances"
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
