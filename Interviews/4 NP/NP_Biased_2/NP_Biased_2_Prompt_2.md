You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "NP_Biased_2",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Chemistry Technician / Radiochemistry Laboratory Technician",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Anomalous Iodine Peak During RCS Grab Sample Analysis",
    "scenario_summary_internal": "A radiochemistry technician performing a routine reactor coolant system (RCS) grab sample and gamma spectroscopy count detects an unexpected I-131 photopeak. The technician must decide how urgently to treat the reading, whether to attribute it to a fuel cladding defect versus an instrument or sampling artifact, whether to escalate to the shift supervisor, and how to set final corrective sampling frequency and root-cause attribution. A vivid fuel-leak event from a prior outage and a superficially similar spectral signature from an unrelated past case create two distinct opportunities for biased reasoning embedded in an otherwise technically plausible, nonroutine incident.",
    "occupational_realism": {
      "objective": "Correctly determine the source of an elevated I-131 activity reading in an RCS coolant sample, take proportionate corrective action, and report results within technical specification reporting timelines without triggering unwarranted plant conservative actions or missing a genuine fuel defect indication.",
      "setting": "Radiochemistry laboratory adjacent to the reactor building of a pressurized water reactor plant, during a backshift with reduced staffing; sample drawn from the RCS hot leg via the sampling panel and analyzed on a high-purity germanium (HPGe) gamma spectroscopy system.",
      "constraints": [
        "Reduced backshift staffing means the shift supervisor is not immediately on the lab floor",
        "Technical specifications require timely reporting of coolant activity trending outside normal band",
        "Reactor is at 100% power with limited tolerance for unnecessary conservative power reduction",
        "HPGe detector was recently recalibrated after a maintenance outage, introducing residual uncertainty about instrument drift",
        "Sample turnaround time is limited before the next scheduled surveillance sample supersedes it"
      ],
      "stakeholders": [
        "Radiochemistry technician (primary actor)",
        "Shift supervisor / control room",
        "Reactor engineering (fuel performance)",
        "Instrumentation and controls (I&C) technician",
        "Chemistry supervisor (day shift, on-call)"
      ],
      "technical_terms_to_use": [
        "RCS grab sample",
        "gamma spectroscopy",
        "HPGe detector",
        "I-131 photopeak",
        "dose equivalent iodine (DEI)",
        "fuel cladding defect",
        "letdown line",
        "background count",
        "technical specification limit",
        "cross-contamination",
        "counting geometry",
        "efficiency calibration"
      ],
      "technical_terms_to_avoid": [
        "salience",
        "similarity heuristic",
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
          "HPGe spectrum shows an I-131 photopeak roughly 3x the prior week's trend",
          "Detector was recalibrated two days earlier after maintenance",
          "Plant is at steady 100% power with no recent transients logged",
          "Technician personally handled a confirmed fuel-defect event with a similar-looking iodine spike during the previous refueling outage cycle"
        ],
        "new_information_after_decision": [
          "A repeat count on the same sample shows a slightly different peak ratio than the first count",
          "No corresponding change in reactor power or letdown flow is logged for this shift"
        ],
        "alternatives": [
          "Treat the reading as a likely early fuel-defect indicator and initiate expedited confirmatory sampling",
          "Treat the reading as routine statistical variation pending a second count",
          "Suspect an instrument or calibration artifact given the recent recalibration and check detector background first"
        ],
        "intended_action": "Technician leans strongly toward the fuel-defect interpretation, prioritizing it over the calibration-artifact possibility"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The current spectrum's peak shape and secondary Cs-137 ratio superficially resemble a spectrum from an unrelated prior case involving a resin intrusion in the letdown demineralizer",
          "No sample has yet been drawn from the demineralizer effluent to confirm or rule out that pathway",
          "The RCS sample and the demineralizer effluent sample are drawn from different points in the system with different expected activity signatures"
        ],
        "new_information_after_decision": [
          "The demineralizer effluent sample, once drawn, shows a different Cs-137-to-I-131 ratio than the RCS sample",
          "I&C reports no open work orders on the RCS sample panel valves"
        ],
        "alternatives": [
          "Attribute the RCS reading to the same root cause as the earlier demineralizer resin-intrusion case based on the resemblance of the spectral pattern",
          "Treat the resemblance as coincidental and independently trace the RCS sample's activity pathway",
          "Request an independent split-sample count by a second technician before attributing cause"
        ],
        "intended_action": "Technician attributes the RCS activity to a resin-intrusion-type cause because the spectrum looks like the earlier case, without independently verifying the pathway"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two counts now show a consistent, real I-131 elevation above the recalibration uncertainty band",
          "Shift supervisor has not yet been formally notified; only informal discussion has occurred",
          "Technical specification reporting window is narrowing",
          "Reactor engineering has not yet been consulted on fuel performance trending"
        ],
        "new_information_after_decision": [
          "Shift supervisor requests a formal written activity trend report and asks whether a power reduction is being recommended",
          "Reactor engineering asks for the last three surveillance data points for comparison"
        ],
        "alternatives": [
          "Escalate immediately to the shift supervisor with a preliminary fuel-defect call",
          "Continue independent verification (extended count, split sample) before escalating",
          "Consult reactor engineering informally before making any formal call"
        ],
        "intended_action": "Technician escalates with a specific causal framing already fixed in mind"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "All confirmatory data (repeat count, split sample, demineralizer sample) are now available",
          "Reactor engineering's fuel-performance model gives a probabilistic, not definitive, assessment",
          "Final report must specify recommended sampling frequency and root-cause attribution"
        ],
        "new_information_after_decision": [
          "Follow-up trending over the next 24 hours either confirms or fails to confirm the initial attribution",
          "Chemistry supervisor reviews the report the next morning"
        ],
        "alternatives": [
          "Finalize the report with a single, confident root-cause attribution and a fixed sampling frequency",
          "Finalize the report with a ranked set of plausible causes and a conservative increased-frequency sampling plan pending further data",
          "Request an extended surveillance period before finalizing any attribution"
        ],
        "intended_action": "Technician finalizes attribution and sampling recommendation, closing out the incident record"
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe what you were doing when you first noticed the anomalous reading.",
        "What was your role and what were you responsible for deciding that shift?"
      ],
      "timeline_reconstruction": [
        "Walk me through what you saw on the spectrum first, second, and third counts.",
        "What information did you have before each decision, and what changed afterward?",
        "Who else was involved at each stage, and when did you bring them in?"
      ],
      "decision_point_probes": [
        "What specifically drew your attention to the fuel-defect explanation first? (cues)",
        "What other information sources could you have checked before settling on that view? (information sources)",
        "What were you trying to accomplish at that moment—speed, certainty, or something else? (goals)",
        "What alternatives did you consider, and why did you rule them out? (alternatives)",
        "What was the deciding factor that tipped you toward the demineralizer resin-intrusion explanation? (decision basis)",
        "Had you seen a similar spectrum before? How did that prior experience shape your read this time? (prior experience)",
        "How much time pressure did you feel at each stage? (time pressure)",
        "How confident were you in the attribution at the time versus after the confirmatory data came in? (uncertainty)"
      ],
      "closing_hypotheticals": [
        "If the recalibration had happened a month earlier instead of two days earlier, would your first read have changed?",
        "If you had drawn the demineralizer sample before forming any theory about the RCS reading, do you think your conclusion would have differed?",
        "Looking back, what would you tell a newer technician to check before letting a past case guide the current one?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "decision_point": 1,
        "mechanism": "The technician's personal, vivid, emotionally memorable involvement in a prior confirmed fuel-defect event during the last outage causes that explanation to dominate the interpretation of the current ambiguous I-131 peak, overweighting it relative to the equally or more plausible instrument-recalibration-artifact explanation.",
        "affected_reasoning_operation": "Initial hypothesis generation and weighting under the first data point (first spectrum count)",
        "evidence_available_at_time": [
          "Recalibration occurred two days prior, an objectively relevant competing explanation",
          "No power or flow transient logged",
          "Technician's own memorable prior fuel-defect experience from the last outage"
        ],
        "required_textual_manifestation": "Technician's narration should explicitly reference how strongly the memory of the prior fuel-defect event colored the first read, and should show the recalibration-artifact explanation being mentioned but under-weighted or considered only briefly before moving on.",
        "plausible_nonbias_interpretation": "A technician could reasonably prioritize the fuel-defect hypothesis first simply because it is the higher-consequence possibility requiring prompt verification, independent of how memorable the prior event was.",
        "strength": "subtle",
        "do_not_make_explicit": ["salience", "memorable", "cognitive bias", "vivid recall bias"]
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "decision_point": 2,
        "mechanism": "The technician attributes the RCS sample's elevated activity to the same root cause as an unrelated prior demineralizer resin-intrusion case purely because the gamma spectrum's peak shape and secondary ratio superficially resemble that earlier case, without verifying that the sampling point, system pathway, or other distinguishing features actually support a common cause.",
        "affected_reasoning_operation": "Causal attribution and evidence-selection act during cross-check with a second sample source",
        "evidence_available_at_time": [
          "Superficial resemblance of spectral peak shape and Cs-137:I-131 ratio to the prior demineralizer case",
          "No demineralizer effluent sample has yet been drawn to confirm the pathway",
          "The RCS and demineralizer sample points are physically and functionally distinct"
        ],
        "required_textual_manifestation": "Technician's narration should show the attribution being made or strongly favored on the basis of the spectra 'looking like' the earlier case, before the confirmatory demineralizer sample is drawn, with the distinguishing sampling-point difference mentioned but not treated as decisive.",
        "plausible_nonbias_interpretation": "A technician might reasonably use a known prior pattern as a starting hypothesis to guide efficient troubleshooting, provided it is promptly checked against confirmatory data rather than treated as established.",
        "strength": "subtle",
        "do_not_make_explicit": ["similarity heuristic", "pattern matching bias", "cognitive bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for biased condition; no control scenario is being generated in this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Autoselected: presence versus absence of the technician's prior personal involvement in the earlier confirmed fuel-defect event and the earlier demineralizer resin-intrusion case (i.e., whether the technician has direct memorable experience with both precedent cases or is instead encountering both pattern types for the first time via written records only)",
      "original_state": "Technician personally experienced both prior cases firsthand and recalls them vividly",
      "counterfactual_state": "Technician has only read summary records of both prior cases secondhand, with no personal vivid memory",
      "variables_to_hold_constant": [
        "Reactor power level and operating conditions",
        "Timing and sequence of the spectrum counts and confirmatory samples",
        "Staffing level and reporting deadlines",
        "Final confirmatory data outcomes"
      ],
      "expected_causal_difference": "Without vivid firsthand recall, the technician would be expected to weight the recalibration-artifact and independent-pathway explanations more evenly at decision points 1 and 2, reducing the strength of both the salience-driven and similarity-driven attributions.",
      "causal_test_question": "Does removing the technician's personal, memorable firsthand experience with the two precedent cases reduce the degree to which the initial spectrum reading and the cross-check attribution are driven by memorability and surface resemblance rather than by systematically weighted evidence?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present in the timeline",
      "Confirm exactly one Salience Bias instance is embedded, located at decision point 1",
      "Confirm exactly one Similarity Bias instance is embedded, located at decision point 2",
      "Confirm no bias labels or psychological terminology appear in probe or timeline text intended for the public interview",
      "Confirm each decision point offers at least two plausible alternatives",
      "Confirm consequences described do not mechanically prove bias presence (e.g., outcome is not stated as simply 'wrong' or 'right')",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points, probe plan breadth, and two bias manifestations"
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
