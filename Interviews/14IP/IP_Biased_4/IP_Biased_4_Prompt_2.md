You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Biased_4",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Maintenance Reliability Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Recurring Bearing Failures on Feedwater Pump P-204",
    "scenario_summary_internal": "A maintenance reliability engineer investigates the third bearing failure in five months on a critical boiler feedwater pump (P-204) inside a tight 48-hour outage window. The engineer must determine the root cause of the latest failure, decide whether extra interim monitoring is warranted before the pump returns to service, choose between a specialist-led laser alignment and a personally performed manual alignment, and select between a well-known legacy bearing part and a newer OEM-upgraded bearing housing with less field history. The narrative embeds one instance each of Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, and Ambiguity Effect at four distinct decision points, with consequences left genuinely ambiguous so no single decision is proven biased by outcome alone.",
    "occupational_realism": {
      "objective": "Diagnose the cause of a recurring bearing failure on a critical feedwater pump and select a repair and monitoring strategy that returns the pump to reliable service before the outage window closes.",
      "setting": "A continuous-process industrial plant (e.g., chemical or power generation) with a centralized reliability engineering function, a 48-hour scheduled outage window, and limited access to OEM technical support.",
      "constraints": [
        "48-hour outage window before production demands full pump output",
        "OEM technical representative and laser alignment specialist have limited availability",
        "Corporate pressure to minimize unplanned downtime and repair cost",
        "Recent budget-driven change to lubrication interval (3 to 4 months)",
        "Staffing shortage limiting who can perform diagnostics",
        "Multiple other rotating assets competing for reliability team attention"
      ],
      "stakeholders": [
        "Reliability Engineer (interviewee)",
        "Marco, junior maintenance technician who performed the prior PM",
        "Plant Maintenance Manager",
        "Production Supervisor",
        "OEM technical representative",
        "Vibration analysis specialist"
      ],
      "technical_terms_to_use": [
        "bearing housing",
        "vibration spectrum",
        "alignment tolerance",
        "MTBF",
        "lubrication interval",
        "root cause failure analysis (RCFA)",
        "condition-based maintenance (CBM)",
        "OEM spec sheet",
        "shaft misalignment",
        "thermal growth",
        "laser alignment",
        "locknut torque"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "cognitive",
        "psychological",
        "fallacy",
        "attribution error",
        "illusion",
        "ambiguity aversion"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "P-204 bearing has failed a third time in five months, each roughly 5-6 weeks apart",
          "Vibration data from the failure is ambiguous, showing both thermal and mechanical signatures",
          "Marco performed the most recent preventive maintenance six weeks earlier and used a slightly different locknut tightening sequence than his predecessor",
          "The lubrication interval was changed from 3 to 4 months two quarters ago as a cost-saving measure",
          "The two prior failures were handled by different technicians using the standard sequence"
        ],
        "new_information_after_decision": [
          "Later records show technicians on all three failures followed varying but plant-approved procedures, and all three failures occurred under the same extended lubrication interval"
        ],
        "alternatives": [
          "Attribute the failure primarily to Marco's specific installation technique",
          "Broaden the investigation to situational/systemic factors such as the lubrication interval change, bearing batch quality, or ambient heat load"
        ],
        "intended_action": "The engineer concludes the failure was mainly caused by Marco's personal carelessness/inexperience, citing his nonstandard tightening sequence, while giving comparatively little weight to the recently changed lubrication interval that applied across all three failures."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three consecutive bearing failures have occurred at roughly similar intervals",
          "Failure interval data shows no statistical dependency between successive events; each failure has been linked to a distinct proximate condition (heat, lubrication, installation variance)",
          "An interim inspection or additional monitoring during the next run would require extending the outage window by several hours"
        ],
        "new_information_after_decision": [
          "The pump completes the next run without incident, which is consistent with both a genuine improvement and simple chance given the small sample size"
        ],
        "alternatives": [
          "Proceed with the standard run schedule without added monitoring, reasoning that the run is 'due' to succeed after three failures",
          "Add interim vibration checks or a shortened run interval given the still-unresolved root cause"
        ],
        "intended_action": "The engineer decides against extra monitoring, remarking that after three failures in a row the pump is 'bound to run clean this time,' despite the lack of any causal link between the independent failure events."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The vibration analyst recommends a specialist-led laser alignment given persistent uncertainty about whether misalignment or thermal growth is driving the failures",
          "The laser alignment specialist and tool are not available for 24 hours, which threatens the outage window",
          "The engineer has personally performed manual dial-indicator alignments on similar pumps in the past with generally acceptable results",
          "Industry alignment tolerances for this pump class have tightened since the engineer's manual technique was last validated"
        ],
        "new_information_after_decision": [
          "The manual alignment falls within the older, looser tolerance band the engineer used to judge success, though it is unclear whether it meets the newer tighter tolerance now recommended for this bearing type"
        ],
        "alternatives": [
          "Wait 24 hours for the specialist and laser tool to get a more precise alignment reading",
          "Perform the alignment manually himself using dial indicators and feel, to keep the outage on schedule"
        ],
        "intended_action": "The engineer chooses to personally perform the manual alignment, stating that his years of hands-on experience mean he can 'feel' when it's right, effectively believing his personal skill can reliably control the alignment outcome despite the unresolved diagnostic uncertainty about whether misalignment is even the dominant failure driver."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The legacy bearing part has a well-documented failure pattern: predictable but recurring failures roughly every 5-6 weeks under current conditions",
          "The OEM's newer sealed-bearing housing has limited field data, with only vague vendor claims of 'improved reliability' and no specific failure-rate figures for this application",
          "The OEM upgrade costs more and would require a minor housing modification within the outage window",
          "Both options are available for installation within the remaining outage time"
        ],
        "new_information_after_decision": [
          "The reordered legacy bearing installs without incident during the outage, but its long-term failure pattern remains statistically unresolved based on this single data point"
        ],
        "alternatives": [
          "Install the OEM's upgraded sealed-bearing housing despite the lack of specific failure-rate data",
          "Reorder the same legacy bearing part because its failure behavior, while poor, is at least well known"
        ],
        "intended_action": "The engineer selects the legacy bearing part, explicitly citing the lack of concrete failure-rate numbers for the OEM upgrade as the reason to avoid it, even though the legacy part's known failure history is itself clearly unsatisfactory."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first told you something was wrong with P-204 this time?",
        "What was your overall goal when you started this investigation?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did you bring in other people, like Marco or the vibration analyst?",
        "What information came in after each step that changed your thinking?"
      ],
      "decision_point_probes": [
        "What cues made you settle on that explanation for the failure?",
        "What information sources did you rely on most at that moment, and which did you set aside?",
        "What were you trying to achieve or protect when you made that call?",
        "What other options did you consider, and why did you rule them out?",
        "What was the main basis for your final decision at that point?",
        "Has something like this come up before in your experience, and how did that shape your thinking here?",
        "How much time pressure were you under when you made that call?",
        "How confident were you in the information you had at that moment?",
        "If you'd had more time or different data, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If the lubrication interval had never been changed, do you think the outcome would have been different?",
        "If the OEM had provided specific failure-rate numbers for the new bearing, would that have changed your choice?",
        "Looking back, is there a point where you'd handle things differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "IP_Biased_4_FAB_01",
        "bias": "Fundamental Attribution Bias",
        "decision_point": 1,
        "mechanism": "Engineer attributes the bearing failure primarily to Marco's personal disposition (carelessness, inexperience) rather than to the situational factor common to all three failures (the extended lubrication interval).",
        "affected_reasoning_operation": "Causal attribution during root cause diagnosis",
        "evidence_available_at_time": [
          "Marco's nonstandard tightening sequence",
          "Recently changed lubrication interval applying to all three failures",
          "Ambiguous vibration signature"
        ],
        "required_textual_manifestation": "The engineer explicitly links the failure to Marco's individual technique/character while giving minimal or dismissive weight to the shared situational factor, despite having the interval-change data available at the time.",
        "plausible_nonbias_interpretation": "It is reasonable domain practice to review the most recent technician's work first when a failure follows shortly after a PM.",
        "strength": "subtle",
        "do_not_make_explicit": ["fundamental attribution bias", "dispositional vs situational", "attribution error"]
      },
      {
        "instance_id": "IP_Biased_4_GF_01",
        "bias": "Gambler's Fallacy",
        "decision_point": 2,
        "mechanism": "Engineer reasons that because three independent failures have occurred in a row, the next run is 'due' to succeed, treating statistically independent failure events as if they were sequentially dependent.",
        "affected_reasoning_operation": "Prediction of future equipment reliability based on recent outcome streak",
        "evidence_available_at_time": [
          "Three consecutive failures at similar intervals",
          "Data showing each failure has a distinct proximate cause (no dependency between events)"
        ],
        "required_textual_manifestation": "The engineer states or implies that the recent run of failures makes a clean run more likely now, and uses this reasoning to justify skipping added monitoring.",
        "plausible_nonbias_interpretation": "Declining to add monitoring could be justified purely by outage-time constraints rather than a belief in a 'streak' correcting itself.",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "independent events", "law of small numbers"]
      },
      {
        "instance_id": "IP_Biased_4_IOC_01",
        "bias": "Illusion of control",
        "decision_point": 3,
        "mechanism": "Engineer overestimates his personal ability to achieve a correct alignment by feel/experience, treating a diagnostically uncertain, partly random outcome as primarily within his personal control.",
        "affected_reasoning_operation": "Decision on repair method and confidence in personally controlling the outcome",
        "evidence_available_at_time": [
          "Specialist recommendation for laser alignment",
          "Tightened industry tolerance standards since the engineer's technique was last validated",
          "Unresolved uncertainty about whether misalignment is even the dominant failure driver"
        ],
        "required_textual_manifestation": "The engineer expresses confidence that personal skill/experience will ensure a correct outcome ('I can feel when it's right') despite acknowledging the underlying diagnostic uncertainty and tighter tolerances.",
        "plausible_nonbias_interpretation": "Choosing the faster manual method could be a reasonable time-pressure tradeoff rather than overconfidence in personal control.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of control", "overconfidence", "personal control bias"]
      },
      {
        "instance_id": "IP_Biased_4_AE_01",
        "bias": "Ambiguity effect",
        "decision_point": 4,
        "mechanism": "Engineer avoids the OEM upgraded bearing option specifically because its success probability is unknown/ambiguous, choosing the legacy part whose failure probability is known even though it is clearly worse.",
        "affected_reasoning_operation": "Choice between two repair options under differing levels of probability information",
        "evidence_available_at_time": [
          "Legacy part's well-documented ~5-6 week recurring failure pattern",
          "OEM upgrade's vague reliability claims without specific failure-rate data"
        ],
        "required_textual_manifestation": "The engineer explicitly cites the lack of concrete numbers for the OEM option as the deciding reason to avoid it, in favor of the known-but-poor legacy option.",
        "plausible_nonbias_interpretation": "Sticking with the legacy part could be justified by cost or by genuine skepticism of unverified vendor marketing claims rather than aversion to ambiguity itself.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity effect", "ambiguity aversion", "known vs unknown probability"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for this biased-condition specification; no paired control scenario was supplied."
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
      "Confirm exactly one instance each of Fundamental Attribution Bias, Gambler's Fallacy, Illusion of Control, and Ambiguity Effect, none repeated or paraphrased elsewhere.",
      "Confirm exactly four decision points, each with at least two plausible alternatives.",
      "Confirm no bias names, definitions, or psychological terminology appear in the interview text.",
      "Confirm each decision point includes probes for cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and at least one hypothetical.",
      "Confirm consequences after each decision remain ambiguous and do not mechanically prove bias or correctness.",
      "Confirm final interview word count falls between 1,215 and 1,485 words, targeting 1,350.",
      "Confirm each occurrence has a distinct evidence source and reasoning operation distinguishing it from the others."
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
