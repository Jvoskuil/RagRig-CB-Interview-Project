You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MU_Vocab_Control_2",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Geotechnical Engineer / Ground Control Specialist",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Roof Fall Precursor at the 4200 Panel Development Face (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A geotechnical engineer at an underground metal mine is called in after a contractor crew reports minor rib spalling and unusual dust puffing near a development face advancing toward a known fault splay. Over roughly 14 hours, the engineer works through the same four decisions as the paired biased scenario — continue mucking, use a convergence model to justify finishing the round, decide on supplemental support in an adjacent heading, and decide whether to permit entry after a crack appears — but at each point weighs the same evidence types (prior incident history, model track record, schedule pressure, monitoring gaps) in a balanced way, explicitly considering situational/geological explanations alongside crew-technique explanations and explicitly qualifying the convergence model's applicability. The incident still culminates in a contained roof fall in the adjacent bolted heading, but the participant's reasoning at no point relies on an unexamined dispositional attribution or unadjusted confidence in the model.",
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
          "The engineer authorizes continued mucking and a visual-only inspection after weighing both the 3800 comparison and the missing local monitoring as open, unresolved factors",
          "Scaling crew finds slightly larger loose slabs than initially described"
        ],
        "alternatives": [
          "Halt all work at the face pending a full geotechnical inspection",
          "Allow mucking to continue with a visual-only check by the shift boss",
          "Restrict access to a buffer zone and reroute the round sequence"
        ],
        "intended_action": "Engineer authorizes continued mucking with a visual check, explicitly noting that the 3800 comparison is only a partial analogy, that the current operator's technique is one relevant but not dispositive factor, and that the missing extensometer data is a real gap that will need to be closed before further judgments are made."
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
          "The engineer runs the in-house convergence prediction model using nearby (but not adjacent) station data and treats the low-displacement forecast as one input among several, explicitly discounting it for the acknowledged domain mismatch",
          "The ground control technician's caveat about calibration domain is incorporated into a more conservative reading of the forecast, and the engineer sets a specific condition (a follow-up scaling check) before relying on it further"
        ],
        "alternatives": [
          "Delay the model output's use until a representative extensometer is reinstalled near the face",
          "Treat the fracture pattern as an independent red flag requiring a stop regardless of model output",
          "Rely on the convergence model's forecast, adjusted downward for domain mismatch, to justify proceeding with the round under a defined follow-up check"
        ],
        "intended_action": "Engineer uses the convergence model's forecast as a qualified, partial input, explicitly reduces confidence in it because of the acknowledged rock-mass domain mismatch, and pairs the decision to proceed with a concrete follow-up condition rather than treating the model output as sufficient on its own."
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
          "Engineer defers a full support upgrade but orders a targeted scaling and spot-bolt check specifically because the second location of spalling is new information that was not covered by the earlier forecast",
          "A ground crack becomes visible along a bolt row in the adjacent heading two hours later"
        ],
        "alternatives": [
          "Order immediate supplemental bolting and mesh in the adjacent heading",
          "Defer additional support pending the next scheduled inspection",
          "Install spot bolts only at the fracture location while deferring full mesh and bolting"
        ],
        "intended_action": "Engineer treats the appearance of spalling in a second location as new evidence that revises, rather than merely extends, the earlier assessment, and responds with a scoped intermediate action (spot bolting and a scaling check) rather than either dismissing the new location or fully deferring based on the earlier forecast."
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
          "Engineer treats the new crack as a materially different signal from the earlier spalling, explicitly declines to extend the earlier forecast to cover it, and authorizes only a restricted, technician-accompanied inspection entry rather than routine access",
          "A larger roof fall occurs in the adjacent bolted section shortly after entry, though no injuries result because the crew evacuates in time following an unrelated alarm"
        ],
        "alternatives": [
          "Deny entry until convergence monitoring is restored and re-evaluated",
          "Allow a restricted, technician-accompanied inspection entry pending re-evaluation",
          "Require full re-support of the heading before any personnel access"
        ],
        "intended_action": "Engineer authorizes a restricted inspection entry while explicitly treating the crack as an open, unresolved question rather than as confirmation of the earlier benign account, balancing the technician's evacuation recommendation against the narrow inspection need."
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
        "How did you weigh the 3800 comparison against the missing extensometer data?",
        "How did you decide how much weight to give the convergence model's forecast?",
        "What was the technician's concern about the model, and how did you incorporate it?",
        "What led you to order a spot check rather than either a full upgrade or a full deferral in the adjacent heading?",
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
        "If the 3800 investigation had reached a different conclusion about its cause, do you think you'd have read the spalling differently?",
        "Looking back, what would you do differently if a similar sequence of reports came in again?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MU_Biased_2",
      "features_to_match": [
        "Underground hard-rock mining domain vocabulary (rib spalling, convergence monitoring, fault splay, extensometer, cut cycle, scaling, bolt pattern)",
        "Same setting, stakeholders, and role (geotechnical engineer / ground control specialist)",
        "Same four-decision-point structure and same chronological incident skeleton (initial spalling report, model-informed round completion, adjacent-heading support decision, crack/entry decision)",
        "Same emotional tone: measured, professionally reflective, mildly self-critical in hindsight",
        "Same difficulty level and same underlying uncertainty sources (offline extensometer, imprecise fault-splay location, model domain mismatch, schedule pressure)",
        "Same eventual outcome (contained roof fall with no injuries due to an unrelated alarm)",
        "Same probe categories and similar probe wording where possible"
      ],
      "features_to_remove_or_change": [
        "Remove the dispositional, analogy-driven causal attribution of the current spalling to operator technique at decision point 1; replace with explicit, balanced weighing of situational and dispositional explanations",
        "Remove the unadjusted confidence in the convergence model's forecast at decision point 2; replace with an explicit downward adjustment for the acknowledged domain mismatch and a defined follow-up condition",
        "Remove the carry-forward reuse of the operator-technique frame at decision point 3; replace with treatment of the second spalling location as revising evidence",
        "Remove the treatment of the crack as confirming prior benign surface behavior at decision point 4; replace with explicit treatment of the crack as an open, unresolved signal"
      ],
      "ambiguity_boundary": "Not applicable; this is a vocabulary_control condition designed to hold domain content constant while removing all intended bias mechanisms. Genuine occupational uncertainty (imprecise fault-splay location, monitoring gaps, model domain mismatch) is retained, but the participant's reasoning must not exhibit an unexamined dispositional attribution or unadjusted confidence in a validity source at any decision point."
    },
    "counterfactual_specification": {
      "causal_variable": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "counterfactual_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "NOT_APPLICABLE",
      "causal_test_question": "NOT_APPLICABLE"
    },
    "generation_checks": [
      "Confirm zero intended instances of Attribution Bias and zero intended instances of Illusion of validity are embedded anywhere in the interview",
      "Confirm domain vocabulary, setting, stakeholders, role, and four-decision-point structure match the paired biased scenario MU_Biased_2",
      "Confirm each decision point includes explicit, balanced consideration of at least two candidate explanations (dispositional/technique vs. situational/geological; model confidence vs. model limitation) rather than an unexamined default",
      "Confirm no bias terminology or psychological labels appear in probes or narrative",
      "Confirm four decision points each have at least two alternatives and pre/post decision information",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and probe density",
      "Confirm the final roof-fall outcome is retained without being used to prove or disprove the quality of any decision",
      "Confirm the participant's tone, difficulty level, and emotional register match the paired biased scenario as closely as vocabulary_control requires"
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
