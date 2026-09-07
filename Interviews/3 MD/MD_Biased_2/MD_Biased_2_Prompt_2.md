You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MD_Biased_2",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Military Police Investigator / Criminal Investigations Division (CID) Special Agent",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Motor Pool Fuel Theft Investigation",
    "scenario_summary_internal": "A CID Special Agent investigates a series of fuel and equipment thefts from a garrison motor pool. The agent must decide which personnel to focus on, how to weigh conflicting witness statements, whether to pursue a forensic lead versus a behavioral pattern, and how to close out the case. The scenario embeds one Illusory Correlation instance (agent perceives a spurious link between a soldier's off-duty conduct/appearance and theft likelihood) and one Negative Rejection Bias instance (agent discounts or dismisses a data point/witness account because it contradicts an already-forming narrative, effectively 'rejecting' disconfirming information as unreliable).",
    "occupational_realism": {
      "objective": "Identify and build a prosecutable case against the individual(s) responsible for repeated fuel and small-equipment theft from the installation motor pool over a six-week period.",
      "setting": "U.S. Army garrison motor pool and adjacent CID field office, mid-size installation, investigation conducted over 10 days",
      "constraints": [
        "Limited surveillance camera coverage (only two of six bays covered)",
        "Rotating duty rosters make timeline reconstruction difficult",
        "Command pressure to close the case before an upcoming inspection",
        "Chain-of-custody requirements for physical evidence (fuel logs, key sign-out sheets)",
        "Limited agent bandwidth—single agent handling primary interviews"
      ],
      "stakeholders": [
        "CID Special Agent (interviewee)",
        "Motor pool NCOIC",
        "Battalion Commander",
        "Suspected junior enlisted soldiers",
        "Night-shift dispatcher",
        "Provost Marshal's Office"
      ],
      "technical_terms_to_use": [
        "chain of custody",
        "key control log",
        "duty roster",
        "sworn statement",
        "probable cause",
        "motor pool NCOIC",
        "fuel reconciliation report",
        "CID case file"
      ],
      "technical_terms_to_avoid": [
        "illusory correlation",
        "negative rejection bias",
        "cognitive bias",
        "confirmation bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Fuel reconciliation report shows discrepancies on nights when three specific soldiers were on shift",
          "No direct camera footage of theft in progress",
          "Motor pool NCOIC mentions one soldier, PFC Doyle, has tattoos and rides a motorcycle off-post"
        ],
        "new_information_after_decision": [
          "Doyle's shift attendance actually overlaps with only 2 of 5 theft dates",
          "Two other soldiers with no distinguishing off-duty traits also had matching shifts"
        ],
        "alternatives": [
          "Prioritize Doyle for initial interview based on the NCOIC's remark and appearance",
          "Build an unbiased shift-overlap matrix across all personnel before selecting an initial interviewee"
        ],
        "intended_action": "Agent selects Doyle as the primary early suspect, associating his off-duty appearance/lifestyle with elevated theft likelihood, ahead of full data review"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Key control log shows irregular sign-outs on two of the theft nights",
          "Fuel truck odometer logs show inconsistent mileage",
          "No fingerprint evidence recovered from fuel caps"
        ],
        "new_information_after_decision": [
          "Odometer inconsistency is later explained by a documented maintenance test drive, unrelated to theft"
        ],
        "alternatives": [
          "Treat the odometer discrepancy as inconclusive until corroborated",
          "Treat the odometer discrepancy as strong corroboration of the working theory"
        ],
        "intended_action": "Agent treats the ambiguous odometer data as supporting evidence without ruling out the routine maintenance explanation"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Night-shift dispatcher provides a sworn statement that Doyle was on the phone with her the entire suspected theft window on one date",
          "Dispatcher has a clean record and no known relationship to Doyle beyond professional contact",
          "Statement directly contradicts the emerging case narrative"
        ],
        "new_information_after_decision": [
          "Phone records later obtained independently corroborate the dispatcher's account"
        ],
        "alternatives": [
          "Formally document and weigh the dispatcher's alibi statement as potentially exculpatory",
          "Characterize the dispatcher's statement as unreliable or possibly coordinated, and deprioritize it in the case file"
        ],
        "intended_action": "Agent discounts the dispatcher's disconfirming statement, framing it as suspect or unreliable rather than integrating it into the evidentiary picture"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Command is pressing for case closure before the upcoming command inspection",
          "Evidence remains circumstantial; no direct forensic or eyewitness link to any one individual",
          "A fourth soldier with unremarkable duty history has an unexplained fuel-card transaction anomaly"
        ],
        "new_information_after_decision": [
          "Case is referred to the Provost Marshal's Office with a recommendation, pending further investigation"
        ],
        "alternatives": [
          "Expand the investigation to fully vet the fourth soldier's anomaly before recommending action",
          "Close out the investigation focusing on the original suspect to meet the command timeline"
        ],
        "intended_action": "Agent recommends closing the investigative focus on the original suspect track to meet the inspection deadline"
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this case first came to your attention?",
        "What was your operational objective when you opened the investigation?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did you form your first working theory of who was responsible?",
        "What information did you have in hand at each stage?"
      ],
      "decision_point_probes": [
        "What specifically drew your attention to that individual at that point?",
        "What alternatives did you consider before proceeding?",
        "How did you weigh the odometer discrepancy against other possible explanations?",
        "How did you handle the dispatcher's statement when it came in?",
        "What made you trust or distrust that source of information?",
        "Walk me through your reasoning for closing out the investigative focus when you did."
      ],
      "prior_experience": [
        "Had you seen a similar theft pattern in past cases?",
        "Did prior investigations shape how you approached this one?"
      ],
      "time_pressure_and_uncertainty": [
        "How much pressure did you feel from command to close this quickly?",
        "At what points did you feel most uncertain about the direction of the case?"
      ],
      "closing_hypotheticals": [
        "If the dispatcher's alibi had come in earlier, would it have changed your approach?",
        "If command had not been pushing for a deadline, what would you have done differently?",
        "Looking back, is there a point where you'd revisit your reasoning?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ic_01",
        "bias": "Illusory Correlation",
        "decision_point": 1,
        "mechanism": "Agent perceives a spurious statistical link between a salient but irrelevant trait (off-duty appearance/motorcycle lifestyle) and theft likelihood, prioritizing this individual for early scrutiny despite shift-overlap data not uniquely implicating him",
        "affected_reasoning_operation": "Suspect prioritization / initial hypothesis formation from distinctive-but-irrelevant cue paired with rare event",
        "evidence_available_at_time": [
          "NCOIC's remark about Doyle's tattoos and motorcycle",
          "Incomplete shift-overlap matrix showing partial, non-unique overlap"
        ],
        "required_textual_manifestation": "Agent explicitly cites Doyle's distinctive off-duty traits as a reason for suspicion before completing a full comparison of all personnel's shift overlaps",
        "plausible_nonbias_interpretation": "Using a memorable personnel detail as a starting point for interviews is a normal triage step when time is limited",
        "strength": "subtle",
        "do_not_make_explicit": ["illusory correlation", "stereotype", "bias", "spurious"]
      },
      {
        "instance_id": "nrb_01",
        "bias": "Negative Rejection Bias",
        "decision_point": 3,
        "mechanism": "Agent discounts a credible, disconfirming witness statement (dispatcher's alibi) by attributing unreliability or ulterior motive to the source, rather than weighing it on its evidentiary merits, because it conflicts with the developing case narrative",
        "affected_reasoning_operation": "Evidence evaluation / source credibility assessment for disconfirming information",
        "evidence_available_at_time": [
          "Dispatcher's sworn statement with no known conflict of interest",
          "Prior investigative narrative already centered on Doyle"
        ],
        "required_textual_manifestation": "Agent characterizes the dispatcher's statement as potentially coordinated or unreliable without a factual basis for that suspicion, and deprioritizes it relative to the existing theory",
        "plausible_nonbias_interpretation": "Investigators routinely scrutinize alibi statements for coordination or bias, especially between coworkers",
        "strength": "subtle",
        "do_not_make_explicit": ["negative rejection bias", "disconfirmation", "bias", "dismissal"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "NONE",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control variant"
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
      "Confirm exactly one Illusory Correlation instance and one Negative Rejection Bias instance are embedded, each at a distinct decision point (1 and 3)",
      "Confirm no bias labels or psychological terminology appear in the interview text",
      "Confirm exactly four decision points, each with at least two alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm word count falls between 1215 and 1485 words",
      "Confirm consequences at each decision point do not definitively prove bias or its absence",
      "Confirm plausible non-bias explanations remain available for both embedded instances"
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
