You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "RT_Ambigious_2",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Signal Maintainer / Signal Technician",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Intermittent Signal Drop at the Marlow Interlocking",
    "scenario_summary_internal": "A signal maintainer is called out to an interlocking after crews report a signal intermittently displaying a more restrictive aspect than expected. Test readings are inconsistent across cycles, weather conditions complicate root-cause attribution, and the maintainer must sequence four decisions about testing, component replacement, and restoring the signal to service before the next traffic window, all under incomplete and genuinely ambiguous diagnostic information.",
    "occupational_realism": {
      "objective": "Diagnose and resolve an intermittent signal malfunction at an interlocking and restore reliable, safe operation before the next scheduled traffic window, without unnecessarily extending the out-of-service period.",
      "setting": "Evening call-out to the Marlow interlocking on a secondary main line; damp weather following an earlier rain shower; one signal maintainer on site with phone access to a signal supervisor.",
      "constraints": [
        "The interlocking must be either fully restored or protected by a manual block/flag arrangement before the next scheduled train movement",
        "Test equipment readings vary somewhat between successive test cycles, some within tolerance and some marginal",
        "Damp conditions from earlier rain could plausibly affect insulation resistance readings on aging wiring",
        "A relay cabinet component is old enough to be a plausible failure point but shows no definitive fault indication",
        "Limited overtime authorization; extending the call-out past a certain point requires supervisor approval"
      ],
      "stakeholders": [
        "Signal maintainer (interviewee)",
        "Signal supervisor (phone contact)",
        "Train dispatcher for the territory",
        "Track crew who reported the original anomaly",
        "Next scheduled train crew"
      ],
      "technical_terms_to_use": [
        "track circuit",
        "relay cabinet",
        "insulation resistance test",
        "signal aspect",
        "interlocking",
        "block occupancy",
        "megger reading",
        "manual block protection"
      ],
      "technical_terms_to_avoid": [
        "zero-risk bias",
        "ambiguity aversion",
        "cognitive bias",
        "heuristic",
        "known versus unknown probability"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Track crew reports the signal dropped to a more restrictive aspect twice during their shift, then returned to normal on its own",
          "No fault code was logged at the interlocking cabinet",
          "The signal has shown no prior history of similar reports in maintenance records"
        ],
        "new_information_after_decision": [
          "Initial visual inspection of the relay cabinet shows no obvious physical damage or moisture intrusion"
        ],
        "alternatives": [
          "Begin immediate bench testing of the suspect track circuit and relay before drawing conclusions",
          "Observe the signal through one or two more operating cycles before opening the cabinet, to see if the pattern repeats"
        ],
        "intended_action": "Maintainer opts to begin testing immediately rather than waiting for further occurrences, citing the need to have a diagnosis before the next scheduled train movement."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Insulation resistance readings across three test cycles come back inconsistent: two within normal tolerance, one marginally low",
          "Wiring in the cabinet is original to a 15-year-old installation",
          "No single component shows a readable, unambiguous fault"
        ],
        "new_information_after_decision": [
          "A fourth test cycle, run after additional drying time, returns a normal reading"
        ],
        "alternatives": [
          "Replace the aging relay and suspect wiring segment now, using the marginal reading as justification",
          "Continue monitoring across additional test cycles and hold replacement until a clearer pattern emerges"
        ],
        "intended_action": "Maintainer chooses to run additional test cycles rather than replace the component immediately, reasoning that a single marginal reading amid otherwise normal ones does not yet point clearly to the wiring versus a transient moisture effect."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The marginal reading occurred shortly after an earlier rain shower, and the cabinet gasket shows minor wear",
          "Drying and cleaning the cabinet connections is a lower-cost, faster interim step",
          "A full wiring segment replacement would take significantly longer and use limited overtime hours"
        ],
        "new_information_after_decision": [
          "Readings remain stable after drying and cleaning, through two more monitored cycles"
        ],
        "alternatives": [
          "Dry, clean, and reseal the cabinet connections as an interim measure and monitor for recurrence",
          "Proceed directly to full replacement of the wiring segment despite the added time and cost"
        ],
        "intended_action": "Maintainer selects the drying-and-resealing approach, noting that the timing correlation with the rain shower offers a plausible, lower-cost explanation that has not yet been ruled out."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Readings have been stable for two consecutive cycles since the interim repair",
          "The next scheduled train movement is approaching, and manual block protection would need to be arranged if the signal is not restored",
          "Root cause remains unconfirmed as either resolved moisture intrusion or a coincidentally quiet marginal wiring issue"
        ],
        "new_information_after_decision": [
          "The signal operates normally through the next several movements without further incident that shift"
        ],
        "alternatives": [
          "Restore the signal to automatic service, given two stable readings, and schedule a follow-up inspection",
          "Keep the signal under manual block protection for the remainder of the shift and reassess in daylight"
        ],
        "intended_action": "Maintainer restores the signal to automatic service after weighing the stable recent readings against the cost of extended manual protection, while flagging the unresolved uncertainty for a follow-up inspection."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and what the call-out looked like when you arrived?",
        "What was your main objective going into this job?"
      ],
      "timeline_reconstruction": [
        "What did you find when you first got to the cabinet, and what did you do right after?",
        "What new information came in after each step that you didn't have going in?"
      ],
      "decision_point_probes": [
        "What options did you weigh at that point, and what made you lean one way?",
        "What specific reading or observation mattered most to you there?",
        "How much time pressure were you under at that moment?",
        "How sure were you about what was actually causing the issue?",
        "Had you seen a similar pattern before, and did that shape your call?"
      ],
      "closing_hypotheticals": [
        "If the marginal reading had shown up again on that fourth test, would you have done something different?",
        "If the overtime authorization had been open-ended, would that have changed your approach?",
        "Looking back, is there a point where you'd want more information before deciding, even now?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "RT_Biased_2",
      "features_to_match": [
        "Four decision points with at least two plausible alternatives each",
        "Subtle difficulty level and comparable narrative complexity",
        "Single frontline technical operator managing incomplete information under moderate time pressure",
        "Similar occupational register, sentence rhythm, and interview probe structure",
        "Comparable proportion of neutral, well-justified reasoning versus open uncertainty",
        "Consequences that do not conclusively prove any decision right or wrong"
      ],
      "features_to_remove_or_change": [
        "Remove the disproportionate risk-elimination framing used in the paired scenario's routing decision",
        "Remove the ambiguity-driven default-to-known-protocol framing used in the paired scenario's hazard-report decision",
        "Change role from dispatcher to signal maintainer and change the operational domain from train movement sequencing to signal/track-circuit diagnostics",
        "Change the specific incident type from multi-train corridor management to single-site fault diagnosis"
      ],
      "ambiguity_boundary": "Genuine diagnostic ambiguity is preserved throughout (inconsistent test readings, an unconfirmed root cause, and a correlation with weather that is plausible but not proven). The maintainer's reasoning at each point remains explicable by ordinary evidence-weighing, cost-benefit judgment, or conservative safety practice, with no point where a described preference is disproportionate to the evidence or driven specifically by discomfort with unspecified information as its stated cause."
    },
    "counterfactual_specification": {
      "causal_variable": "Recent weather exposure of the relay cabinet (dry versus recently rained-on)",
      "original_state": "The marginal insulation reading occurs shortly after a rain shower, with a worn cabinet gasket offering a plausible moisture-related explanation",
      "counterfactual_state": "The same marginal reading occurs during a stretch of consistently dry weather with no recent precipitation, removing the moisture explanation as a candidate cause",
      "variables_to_hold_constant": [
        "The pattern of inconsistent test readings across cycles",
        "The age and condition of the wiring and relay",
        "The interim drying-and-resealing decision structure",
        "The end-of-shift restoration decision and its timing pressure"
      ],
      "expected_causal_difference": "Without the weather-based explanation available, the maintainer's choice between interim measures and full replacement would need to rest on a different justification, which would help distinguish whether the original decision was driven by the specific moisture evidence or by a more general reluctance to commit to a costlier repair.",
      "causal_test_question": "Does removing the plausible weather explanation for the marginal reading change whether the maintainer chooses an interim fix or a full component replacement?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present in the timeline",
      "Confirm no named-bias mechanism from the manifest is intentionally embedded at any decision point",
      "Confirm each decision point contains genuine, textually supported ambiguity with at least one plausible non-bias explanation already built into the surrounding facts",
      "Confirm technical vocabulary and narrative complexity are comparable to the paired scenario RT_Biased_2",
      "Confirm no bias terminology or psychological labels appear in interview text",
      "Confirm each decision point offers at least two plausible alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm final word count falls between 1215 and 1485 words",
      "Confirm consequences described do not conclusively prove any decision correct, incorrect, or biased"
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
