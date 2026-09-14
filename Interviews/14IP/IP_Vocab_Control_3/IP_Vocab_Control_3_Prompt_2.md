You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Vocab_Control_3",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Environmental/Safety Compliance Officer (Manufacturing Plant)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Fenceline Alarm: VOC Exceedance Investigation at the Solvent Recovery Unit (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A vocabulary- and structure-matched control paired to IP_Biased_3. The same specialty chemicals plant, same Solvent Recovery Unit (SRU) VOC sensor alarm, same odor complaint, same production deadline, and the same four decision points are preserved, but at every decision point the officer engages in balanced, evidence-proportionate reasoning: hypotheses are checked rather than anchored, potentially unwelcome data is sought rather than avoided, and causal attribution is weighted by base rates and severity rather than by vividness of a recalled incident. No named bias is intentionally instantiated.",
    "occupational_realism": {
      "objective": "Determine the true cause of the anomalous VOC reading and odor complaint, decide on corrective action, and satisfy Title V air permit reporting obligations without triggering an unnecessary production shutdown.",
      "setting": "Mid-size specialty chemicals/coatings manufacturing plant; Building 3 houses the Solvent Recovery Unit (SRU) subject to a state Title V air permit with VOC concentration and mass-emission limits and fenceline monitoring.",
      "constraints": [
        "Large customer production order due in 48 hours",
        "Environmental team is short-staffed (officer plus one part-time technician)",
        "Full CEM data pull and independent lab confirmation take analyst hours and may delay production",
        "Permit requires self-report of confirmed exceedances within 24 hours",
        "Corporate is mid-renewal on the Title V permit and sensitive to regulatory attention",
        "Sensor array has a documented history of drift-related false alarms in the past month"
      ],
      "stakeholders": [
        "Plant Manager",
        "Production Supervisor",
        "Corporate EHS Director",
        "Maintenance Technician",
        "State Environmental Agency inspector",
        "Local residents near the fenceline"
      ],
      "technical_terms_to_use": [
        "VOC (volatile organic compound)",
        "action threshold",
        "fenceline monitoring",
        "continuous emissions monitoring (CEM)",
        "Title V permit",
        "self-report",
        "reportable exceedance",
        "solvent recovery unit (SRU)",
        "sensor drift/recalibration",
        "gasket seep",
        "corrective action plan"
      ],
      "technical_terms_to_avoid": [
        "primacy effect",
        "ostrich effect",
        "imaginability bias",
        "cognitive bias",
        "anchoring",
        "availability heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "VOC sensor near SRU triggers alarm above action threshold at 6:40am",
          "Sensor array drifted twice in the past month causing false positives",
          "No community complaints yet logged at time of alarm"
        ],
        "new_information_after_decision": [
          "Community hotline receives an odor complaint near the fenceline at 7:15am",
          "Field team's handheld VOC readings are elevated but not conclusively over the permit limit"
        ],
        "alternatives": [
          "Classify the alarm as probable sensor drift and schedule routine recalibration during day shift",
          "Treat the alarm as a potential real release and immediately dispatch a field team with protocol-level urgency"
        ],
        "intended_action": "Officer notes the drift history as a relevant base rate but withholds a firm classification, dispatching the field team promptly to gather independent confirming data before committing to either explanation, then updates the working assessment once the handheld readings and the odor complaint are both in hand."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary field VOC readings fall in a 'grey zone' near but not conclusively over the permit limit",
          "Production is mid-batch; a partial shutdown for full testing would cost roughly $40,000/day",
          "A full CEM data pull and independent lab confirmation could clarify whether the exceedance is reportable"
        ],
        "new_information_after_decision": [
          "Two days later, a contractor reviewing an unrelated maintenance log flags a data logger showing sustained high VOC readings during the alarm window"
        ],
        "alternatives": [
          "Request an immediate full CEM data download and independent lab confirmation before proceeding",
          "Continue near-term monitoring with tighter sampling intervals while scoping the cost and timing of a full data pull"
        ],
        "intended_action": "Officer weighs the analyst hours and shutdown cost against the risk of an undetected exceedance, consults the production supervisor on the batch timeline, and settles on a resourced middle path (tighter interim sampling plus a scheduled full data pull within a defined short window) rather than either open-ended deferral or immediate full escalation."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three-year maintenance log shows gasket seep is the statistically most common cause of past minor VOC events at this site",
          "Officer is aware of a valve failure at a sister plant in Ohio two weeks earlier, covered in a corporate webinar, that caused a $2M fine and local news coverage",
          "No teardown or physical inspection of the SRU valve or gaskets has yet occurred"
        ],
        "new_information_after_decision": [
          "Maintenance teardown later reveals a worn gasket seal, consistent with the statistically dominant site history"
        ],
        "alternatives": [
          "Prioritize investigating gasket seep as the most likely cause based on site history",
          "Inspect the valve first given the severity of the Ohio outcome, even though it is statistically less common at this site"
        ],
        "intended_action": "Officer explicitly states that the maintenance log's three-year pattern is the primary basis for prioritizing the gasket line first, while also scheduling a quick valve check as a low-cost precaution given the severity (not likelihood) of the Ohio scenario, documenting both the base-rate reasoning and the precautionary rationale side by side."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Gasket seal wear is confirmed as the physical cause",
          "Cumulative emissions data now available, with exceedance status depending on which calculation methodology is applied",
          "Permit requires notification within 24 hours of a confirmed exceedance",
          "Production order deadline is two days away"
        ],
        "new_information_after_decision": [
          "Outcome (whether the agency ultimately cites the plant, and whether repair timing avoided further release) is learned only after the officer's decision"
        ],
        "alternatives": [
          "Apply the conservative exceedance calculation, self-report immediately, and recommend temporary SRU shutdown for repair",
          "Apply a less conservative calculation methodology that keeps reported emissions under threshold, avoid mandatory reporting, and schedule repair during the next planned maintenance window"
        ],
        "intended_action": "Officer weighs the two calculation methodologies and permit language on their merits, consulting precedent from prior audits, and reaches a defensible conclusion; this decision point remains a genuine, undetermined judgment call with no intended bias instrumentation, matching the base scenario."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew and what your objective was when the alarm first came in.",
        "What was your role and responsibility once the sensor alarm and the odor complaint both surfaced?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do in the first 30 minutes?",
        "What new information came in over the following two days, and when did you learn it?",
        "At what point did the maintenance teardown findings become available?"
      ],
      "decision_point_probes": [
        "What cues did you weigh when deciding how to classify the alarm, and how did you avoid over-relying on any one of them?",
        "What information sources did you consult before deciding on the CEM data pull, and how did you decide on timing?",
        "What alternatives did you consider when prioritizing which part of the unit to inspect first, and how did you weigh likelihood against severity?",
        "What was your basis for choosing the exceedance calculation methodology, and how did the permit deadline factor in?",
        "How much time pressure did you feel at each of these moments, and how did that shape what evidence you gathered?",
        "How confident were you in your interpretation at each stage, and what would have made you more or less confident?"
      ],
      "closing_hypotheticals": [
        "If the sensor drift history hadn't existed, would your initial triage have gone differently?",
        "If you'd had an extra analyst that week, would your CEM data timeline have changed?",
        "If you hadn't known about the Ohio incident, do you think your inspection order would have been different?",
        "Looking back, what single piece of information, if available earlier, would have most changed your approach?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "IP_Biased_3",
      "features_to_match": [
        "Setting: specialty chemicals/coatings plant, Building 3 SRU, Title V permit context",
        "Same stakeholders (Plant Manager, Production Supervisor, Corporate EHS Director, Maintenance Technician, state inspector, local residents)",
        "Same four-decision-point structure and sequencing",
        "Same constraints: production deadline, staffing shortage, cost of shutdown, 24-hour reporting clock, sensor drift history, Ohio webinar exposure",
        "Same technical vocabulary list and difficulty level",
        "Same emotional tone: time pressure, professional caution, incremental uncertainty resolution"
      ],
      "features_to_remove_or_change": [
        "Remove anchoring of the initial drift hypothesis; replace with prompt cross-checking before committing to a classification",
        "Remove avoidance-motivated deferral of the CEM data pull; replace with a resourced, workload-and-risk-based interim plan",
        "Remove disproportionate narrative weighting toward the vivid Ohio incident; replace with explicit base-rate-led prioritization plus a clearly labeled precautionary (severity-based) secondary check"
      ],
      "ambiguity_boundary": "Reasoning at each decision point may still involve genuine trade-offs and incomplete information, but the participant must articulate a proportionate, evidence-based rationale for each choice rather than exhibiting anchoring, avoidance, or vividness-driven attribution. Uncertainty is preserved through resource and timing trade-offs, not through undocumented reasoning shortcuts."
      },
    "counterfactual_specification": {
      "causal_variable": "Officer's recent exposure to the vivid sister-plant (Ohio) valve-failure narrative prior to the incident (autoselected for potential future counterfactual pairing; inactive for this vocabulary_control condition)",
      "original_state": "Officer is aware of the Ohio valve failure via a corporate webinar two weeks before the incident",
      "counterfactual_state": "Officer had no recent exposure to any vivid comparable incident narrative before the SRU alarm",
      "variables_to_hold_constant": [
        "Sensor alarm timing and drift history",
        "Community odor complaint",
        "Production deadline and shutdown cost figures",
        "Maintenance log base rates for gasket seep vs. valve failure",
        "Number and sequencing of decision points"
      ],
      "expected_causal_difference": "Not applicable in this condition; reasoning at decision point 3 is already base-rate led regardless of Ohio exposure, so removing the exposure would not be expected to change the prioritization in this control version.",
      "causal_test_question": "Not applicable; this field is retained only for potential future counterfactual pairing against IP_Biased_3, not for use in vocabulary_control validation."
    },
    "generation_checks": [
      "Confirm zero intended instances of Primacy Effect, Ostrich effect, and Imaginability Bias appear anywhere in the interview.",
      "Confirm all four decision points, stakeholders, constraints, and technical vocabulary match IP_Biased_3 in structure and complexity.",
      "Confirm each decision point shows explicit, proportionate reasoning that references available evidence rather than reasoning shortcuts resembling the named biases.",
      "Confirm the Ohio incident and drift-history details are present as background facts but are explicitly subordinated to base-rate/statistical reasoning rather than driving the outcome.",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text.",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and probe coverage without repetitive exposition.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm consequences at each decision point remain uncertain in advance and do not mechanically validate or invalidate any decision as biased."
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
