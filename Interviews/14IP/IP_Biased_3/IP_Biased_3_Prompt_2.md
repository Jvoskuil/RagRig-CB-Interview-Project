You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Biased_3",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Environmental/Safety Compliance Officer (Manufacturing Plant)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Fenceline Alarm: VOC Exceedance Investigation at the Solvent Recovery Unit",
    "scenario_summary_internal": "A specialty chemicals plant's Solvent Recovery Unit (SRU) in Building 3 triggers a VOC sensor alarm coinciding with a community odor complaint. The Environmental/Safety Compliance Officer must triage the alarm, decide how aggressively to investigate, construct a causal narrative for the incident, and determine whether/how to report to the state agency, all under production-deadline and budget pressure and against a backdrop of recent sensor false positives and a recently publicized valve-failure incident at a sister plant.",
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
          "Field team's handheld VOC readings are elevated but ambiguous relative to the initial hypothesis"
        ],
        "alternatives": [
          "Classify the alarm as probable sensor drift and schedule routine recalibration during day shift",
          "Treat the alarm as a potential real release and immediately dispatch a field team with protocol-level urgency"
        ],
        "intended_action": "Officer forms an initial 'probably drift' judgment from a brief review of the alarm log before other evidence arrives, and this first impression frames how subsequent, more ambiguous field data is interpreted."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary field VOC readings fall in a 'grey zone' near but not conclusively over the permit limit",
          "Production is mid-batch; a partial shutdown for full testing would cost roughly $40,000/day",
          "A full CEM data pull and independent lab confirmation could reveal a reportable exceedance requiring self-report within 24 hours"
        ],
        "new_information_after_decision": [
          "Two days later, a contractor reviewing an unrelated maintenance log flags a data logger showing sustained high VOC readings during the alarm window"
        ],
        "alternatives": [
          "Request an immediate full CEM data download and independent lab confirmation before proceeding",
          "Defer deeper analysis, citing inconclusive grey-zone readings, and proceed with routine recalibration and continued monitoring"
        ],
        "intended_action": "Officer defers requesting the full CEM dataset and confirmatory lab testing, citing workload and inconclusiveness, thereby avoiding the analysis most likely to confirm a reportable exceedance."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three-year maintenance log shows gasket seep is the statistically most common cause of past minor VOC events at this site",
          "Officer attended a corporate webinar two weeks earlier detailing a dramatic valve failure at a sister plant in Ohio that caused a $2M fine and local news coverage",
          "No teardown or physical inspection of the SRU valve or gaskets has yet occurred"
        ],
        "new_information_after_decision": [
          "Maintenance teardown later reveals a worn gasket seal, not a valve failure"
        ],
        "alternatives": [
          "Prioritize investigating gasket seep as the most likely cause based on site history",
          "Frame the initial investigation and draft incident report around a valve-failure scenario resembling the Ohio incident"
        ],
        "intended_action": "Officer's causal narrative for the draft report disproportionately features the vivid, recently recalled Ohio valve-failure scenario, directing inspection resources toward the valve before the statistically more probable gasket cause is checked."
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
        "intended_action": "Officer weighs the two calculation methodologies and permit language on their merits; this decision point is left free of intended bias instrumentation so it functions as a genuine, undetermined judgment call."
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
        "What cues made you initially lean toward sensor drift rather than a real release?",
        "What information sources did you consult before deciding whether to pull the full CEM dataset, and which did you set aside?",
        "What alternatives did you consider when drafting the incident narrative, and why did the Ohio incident come to mind?",
        "What was your basis for choosing an exceedance calculation methodology, and how did the permit deadline factor in?",
        "How much time pressure did you feel at each of these moments, and how did that shape what evidence you gathered?",
        "How confident were you in your interpretation at each stage, and what would have made you less confident?"
      ],
      "closing_hypotheticals": [
        "If the sensor drift history hadn't existed, would your initial triage have gone differently?",
        "If you'd had an extra analyst that week, would you have pulled the full CEM data sooner?",
        "If you hadn't attended the corporate webinar about the Ohio incident, do you think your investigation would have started elsewhere?",
        "Looking back, what single piece of information, if available earlier, would have most changed your approach?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "decision_point": 1,
        "mechanism": "The officer's first plausible explanation (sensor drift, formed from a brief alarm-log review) is given outsized weight and colors interpretation of the ambiguous field readings that arrive afterward, rather than those later readings being weighed on their own merits.",
        "affected_reasoning_operation": "Initial hypothesis formation and subsequent evidence interpretation",
        "evidence_available_at_time": [
          "Alarm log showing recent drift-related false positives",
          "No complaints yet logged",
          "Absence of confirmatory field data at the moment of triage"
        ],
        "required_textual_manifestation": "Officer explicitly states the drift explanation was adopted within minutes of the alarm and that later ambiguous field readings were read through that initial lens ('I already figured it was probably drift again, so...') rather than assessed independently.",
        "plausible_nonbias_interpretation": "Given a genuine base rate of two prior false alarms in one month, treating drift as the leading hypothesis is a reasonable, experience-based heuristic, not necessarily bias.",
        "strength": "subtle",
        "do_not_make_explicit": ["primacy effect", "anchoring", "first impression bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Ostrich effect",
        "decision_point": 2,
        "mechanism": "Officer avoids requesting the full CEM data pull and lab confirmation specifically because that information is likely to confirm a costly, reportable exceedance, choosing inconclusive grey-zone readings as sufficient grounds to defer.",
        "affected_reasoning_operation": "Evidence-seeking / information avoidance under threat of unwelcome confirmation",
        "evidence_available_at_time": [
          "Grey-zone field VOC readings",
          "Awareness that a full CEM download could reveal a reportable exceedance",
          "Known cost of partial shutdown (~$40,000/day) and reporting consequences"
        ],
        "required_textual_manifestation": "Officer acknowledges knowing the full data pull was the appropriate next step but describes consciously delaying it, citing workload or inconclusiveness, in a way that reveals awareness the deferral was tied to not wanting to find a problem.",
        "plausible_nonbias_interpretation": "With a short-staffed team and a genuinely ambiguous reading, deferring a resource-intensive full analysis pending a second checkpoint could reflect ordinary prioritization under workload constraints.",
        "strength": "moderate",
        "do_not_make_explicit": ["ostrich effect", "information avoidance", "willful blindness"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Imaginability Bias",
        "decision_point": 3,
        "mechanism": "Officer's causal narrative construction is disproportionately shaped by the vivid, recently recalled Ohio valve-failure incident rather than by the statistically more common gasket-seep cause documented in three years of maintenance logs.",
        "affected_reasoning_operation": "Causal attribution / hypothesis prioritization for the draft incident report",
        "evidence_available_at_time": [
          "Three-year maintenance log showing gasket seep as the most frequent past cause",
          "Recent, vivid recollection of a dramatic sister-plant valve failure from a corporate webinar",
          "No physical inspection yet performed"
        ],
        "required_textual_manifestation": "Officer explains that the Ohio incident came to mind readily and shaped the initial framing of the report and inspection priorities, described in terms that emphasize how memorable/vivid that comparison was, ahead of statistically grounded reasoning.",
        "plausible_nonbias_interpretation": "Investigating the valve first could be justified as prudent worst-case-first triage given catastrophic consequences, independent of vividness.",
        "strength": "subtle",
        "do_not_make_explicit": ["imaginability bias", "availability heuristic", "vividness effect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no paired control scenario is specified for this generation task."
    },
    "counterfactual_specification": {
      "causal_variable": "Officer's recent exposure to the vivid sister-plant (Ohio) valve-failure narrative prior to the incident (autoselected as the causal variable best suited to a future counterfactual pairing; inactive for the current 'biased' condition)",
      "original_state": "Officer attended a corporate webinar two weeks before the incident describing a dramatic, costly valve failure at a sister plant",
      "counterfactual_state": "Officer had no recent exposure to any vivid comparable incident narrative before the SRU alarm",
      "variables_to_hold_constant": [
        "Sensor alarm timing and drift history",
        "Community odor complaint",
        "Production deadline and shutdown cost figures",
        "Maintenance log base rates for gasket seep vs. valve failure",
        "Number and sequencing of decision points"
      ],
      "expected_causal_difference": "Without the vivid Ohio exposure, the officer's causal narrative at decision point 3 would be expected to default to the statistically dominant gasket-seep hypothesis rather than the valve-failure hypothesis.",
      "causal_test_question": "Does removing the officer's recent exposure to a vivid comparable incident change which cause is prioritized in the initial causal narrative at decision point 3?"
    },
    "generation_checks": [
      "Confirm exactly one instance each of Primacy Effect, Ostrich effect, and Imaginability Bias appears, tied to decision points 1, 2, and 3 respectively.",
      "Confirm decision point 4 contains no intended bias instrumentation.",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text.",
      "Confirm each instance has a distinct evidentiary basis and reasoning operation from the others.",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and probe coverage without repetitive exposition.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm consequences at each decision point do not mechanically prove bias (e.g., the gasket cause being correct does not itself prove the Ohio-narrative emphasis was biased)."
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
