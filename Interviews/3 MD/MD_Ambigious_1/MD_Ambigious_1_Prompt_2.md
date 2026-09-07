You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MD_Ambigious_1",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Intelligence Analyst (All-Source)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Sector Nightfall: Attack Tempo Assessment After Operation Steady Watch (Ambiguous Control)",
    "scenario_summary_internal": "An all-source intelligence analyst tracks weekly attack counts (IED and small-arms incidents) in District X over eight weeks. A baseline of roughly three attacks per week produces an anomalous spike to eleven attacks in week five, coinciding with a local festival, a resupplied weapons cache, and a flaring tribal land dispute. In week six, command implements a new checkpoint posture, Operation Steady Watch, partly on the analyst's recommendation. In weeks seven and eight, attack counts fall back to near-baseline levels. Unlike the paired scenario, the analyst here explicitly weighs both the checkpoint posture and the resolution of the transient local factors as plausible contributors, cannot fully disentangle them with the data available, and presents the causal picture as genuinely undetermined rather than settling confidently on either explanation. The same downstream resourcing and forecasting decisions occur, but they proceed from acknowledged uncertainty rather than from a confident single-cause narrative.",
    "occupational_realism": {
      "objective": "Determine whether Operation Steady Watch is causing the observed decline in attack tempo in District X and produce a resourcing and forecasting recommendation for the battalion S2 and commander.",
      "setting": "Battalion S2 all-source intelligence cell on a forward operating base supporting counterinsurgency operations in a contested rural district, working from SIGACTS databases, UAV/ISR feeds, and HUMINT source reporting under a weekly INTSUM production cycle.",
      "constraints": [
        "Limited UAV/ISR collection hours must be allocated between District X and District Y",
        "Weekly INTSUM deadline compresses analytic turnaround time",
        "Command pressure for a demonstrable 'win' narrative ahead of a regional assessment brief",
        "HUMINT source access in District X is intermittent and unverified",
        "Only eight weeks of SIGACTS data exist for the district, limiting historical baseline depth"
      ],
      "stakeholders": [
        "Battalion S2 (senior analyst, supervisor)",
        "Company commander responsible for District X patrol posture",
        "District governor liaison officer",
        "HUMINT source handler",
        "S3 operations officer coordinating checkpoint resourcing"
      ],
      "technical_terms_to_use": [
        "SIGACTS",
        "attack tempo",
        "INTSUM",
        "ISR tasking",
        "checkpoint posture",
        "pattern-of-life",
        "indicators and warnings",
        "collection plan"
      ],
      "technical_terms_to_avoid": [
        "regression to the mean",
        "statistical regression",
        "mean reversion",
        "law of small numbers",
        "base rate fallacy",
        "cognitive bias",
        "outlier correction",
        "confounder",
        "causal inference"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Weeks 1-4 SIGACTS average roughly 3 attacks/week in District X, with one prior week reaching 5",
          "Week 5 SIGACTS jump to 11 attacks, the highest in the dataset",
          "Unconfirmed HUMINT reporting a local festival, a possible cache resupply, and a tribal land dispute all active in week 5",
          "Command is requesting an immediate assessment for the next INTSUM"
        ],
        "new_information_after_decision": [
          "S3 approves a limited checkpoint pilot (early version of what becomes Steady Watch) starting week 6",
          "ISR tasking is increased on two suspected cache routes"
        ],
        "alternatives": [
          "Recommend an immediate cordon-and-search operation against suspected cache sites",
          "Recommend increased ISR/HUMINT tasking only, withholding kinetic or posture changes until the pattern is confirmed over more weeks",
          "Recommend an immediate district-wide checkpoint posture change without waiting for confirmation"
        ],
        "intended_action": "Analyst recommends a measured response: expanded ISR tasking plus a limited checkpoint pilot, pending confirmation that week 5 is a genuine trend rather than a one-off spike."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Operation Steady Watch (full checkpoint posture) implemented battalion-wide in District X starting week 6",
          "Week 6 attacks drop to 6; weeks 7-8 drop further to 3 and 4 respectively",
          "HUMINT later confirms the festival ended, the tribal dispute was mediated by elders, and the resupplied cache was reportedly expended in week 5 operations",
          "Supervisor requests a causal assessment of Steady Watch's effectiveness for the command brief"
        ],
        "new_information_after_decision": [
          "Analyst's assessment, framed as inconclusive on single cause, is forwarded to S3 and the company commander with a recommendation to keep monitoring",
          "Commander asks whether the same posture should be evaluated for District Y despite the uncertainty"
        ],
        "alternatives": [
          "Attribute the weeks 7-8 decline primarily to Steady Watch's deterrent effect",
          "Attribute the decline primarily to the resolution of the transient local factors (festival, cache depletion, dispute mediation)",
          "Present the decline as consistent with either explanation, or some combination, without picking a dominant cause given the limited data"
        ],
        "intended_action": "Analyst tells the supervisor that both Steady Watch and the resolved local factors line up with the timing of the decline, that the eight-week dataset is too short and the confounding factors too concentrated in the same window to cleanly separate the two, and recommends treating the checkpoint effect as unconfirmed pending more data rather than asserting it as the driver."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "District Y has its own eight-week SIGACTS history with a similar baseline (~2-3/week) and one anomalous spike to 9 in week 4, followed by a partial decline to 5-6 in subsequent weeks without any posture change",
          "Commander wants a resourcing recommendation: extend Steady Watch to District Y or hold current ISR allocation",
          "Analyst's District X assessment (from phase 2), flagged as inconclusive, is the primary input available",
          "District Y HUMINT source handler reports a different, still-unresolved local driver behind District Y's spike"
        ],
        "new_information_after_decision": [
          "S3 holds off committing checkpoint materials to District Y pending a short standalone review",
          "District Y handler is tasked to pursue additional source reporting on the unresolved driver"
        ],
        "alternatives": [
          "Recommend replicating Steady Watch in District Y immediately, treating District X as a working model",
          "Recommend a separate baseline and cause analysis for District Y before committing checkpoint resources, given that District Y's spike had a different and unresolved driver",
          "Recommend reallocating resources to HUMINT source development in District Y instead of a checkpoint posture"
        ],
        "intended_action": "Analyst recommends against an immediate replication, citing the unresolved and different driver in District Y and the still-open causal question from District X, and instead proposes a short standalone review before committing checkpoint resources."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two consecutive weeks (7-8) of low attack counts in District X following Steady Watch implementation",
          "Command brief scheduled in three days requiring a forward-looking assessment",
          "No additional District X SIGACTS data beyond week 8 is yet available",
          "Analyst's phase 2 assessment already flagged the cause as unresolved"
        ],
        "new_information_after_decision": [
          "Commander approves continued Steady Watch funding for one more quarter with an explicit review checkpoint rather than an open-ended commitment",
          "Analyst is tasked to reassess after four additional weeks of data before any further resourcing decision"
        ],
        "alternatives": [
          "Forecast continued low attack tempo (3-4/week) as a direct extrapolation of the two-week decline",
          "Present a range with explicit uncertainty, noting the limited data window, the unresolved cause, and the possibility of tempo rising back toward or above baseline",
          "Defer any quantitative forecast and request an extended observation period before the brief"
        ],
        "intended_action": "Analyst presents a forecast range rather than a single point estimate, explicitly noting to the commander that the driver of the decline has not been isolated and that four more weeks of data are needed before treating the current tempo as the new normal."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what your role was in this assessment and what triggered your involvement.",
        "What was the operational objective you were trying to achieve with this analysis?"
      ],
      "timeline_reconstruction": [
        "Take me through the SIGACTS numbers week by week as you experienced them.",
        "What did you know about District X's attack pattern before week 5?",
        "When Steady Watch was implemented, what did you expect to happen to the numbers?"
      ],
      "decision_point_probes": [
        "At the week-5 spike, what alternatives did you consider before recommending a response, and why did you choose the one you did?",
        "When you saw the decline in weeks 7-8, what evidence did you use to explain it, and what made it hard to settle on a single explanation?",
        "What made you cautious about recommending the same approach for District Y?",
        "How did you decide what to tell the commander about future attack tempo, and what information would have let you commit to a firmer forecast?"
      ],
      "closing_hypotheticals": [
        "If the tribal dispute had not been resolved that week, would your read on Steady Watch have changed?",
        "If District Y's spike had also declined without any posture change, how would that have affected your confidence in the District X picture?",
        "Looking back, is there anything about how the data came together that week that you'd want to see differently before drawing a firmer conclusion?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MD_Biased_1",
      "features_to_match": [
        "Same domain vocabulary (SIGACTS, INTSUM, ISR tasking, checkpoint posture, pattern-of-life, indicators and warnings, collection plan)",
        "Same setting, stakeholders, and constraints",
        "Same eight-week attack-count trajectory (baseline ~3/week, week-5 spike to 11, decline to 3-4 in weeks 7-8)",
        "Same four decision points and same structural sequence of alternatives",
        "Same District Y comparison scenario and same forecast-to-commander closing decision",
        "Same emotional tone (measured, procedural, mild time pressure) and same interview length target"
      ],
      "features_to_remove_or_change": [
        "Remove the confident, single-cause attribution of the weeks 7-8 decline to Steady Watch",
        "Replace it with an explicit acknowledgment that the checkpoint posture and the resolved transient local factors are both plausible contributors and cannot be cleanly separated with the available data",
        "Adjust the District Y and forecast decisions so they proceed from stated uncertainty (holding off, requesting more data, presenting a range) rather than from a settled causal belief",
        "Remove any language that treats the magnitude of the decline itself as proof of the checkpoint's effect"
      ],
      "ambiguity_boundary": "The interview must leave the true cause of the weeks 7-8 decline genuinely underdetermined: the analyst notices and articulates both the checkpoint-effect explanation and the resolved-transient-factors explanation, treats the short data window and overlapping timing as a real obstacle to separating them, and makes downstream resourcing and forecasting choices that hedge against either explanation being wrong. This must read as reasonable analytic caution under thin data, not as an artificially neutral or evasive stance, and must not contain the specific failure of dismissing or omitting consideration of natural reversion after an extreme outlier."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence versus absence of resolvable transient confounding factors (festival, cache depletion, tribal dispute mediation) coinciding with the week-5 attack spike",
      "original_state": "Transient local factors were present during the week-5 spike and resolved naturally by weeks 7-8, so the decline is genuinely ambiguous between the checkpoint posture and natural resolution of those factors",
      "counterfactual_state": "No transient confounding factors are present; the week-5 spike reflects a sustained escalation with no independent reason to subside, which would let the checkpoint effect be assessed with less ambiguity",
      "variables_to_hold_constant": [
        "Baseline attack rate in weeks 1-4",
        "Timing of Steady Watch implementation (week 6)",
        "Magnitude and timing of the week-5 spike",
        "Analyst identity, role, and reporting cadence",
        "Command pressure and INTSUM deadline structure"
      ],
      "expected_causal_difference": "Removing the transient confounders would reduce the ambiguity in the phase-2 causal assessment, since there would be no competing natural-resolution explanation to weigh against the checkpoint posture.",
      "causal_test_question": "Does the presence of resolvable transient confounders during the spike change how confidently or ambiguously the decline can be attributed to Steady Watch?"
    },
    "generation_checks": [
      "Confirm exactly four decision points exist, each with at least two alternatives, mirroring MD_Biased_1's structure.",
      "Confirm zero intended instances of 'Failure to recognize regression to the mean' or any other named bias are embedded.",
      "Confirm the phase-2 causal assessment explicitly holds both explanations open rather than dismissing or omitting the natural-resolution explanation.",
      "Confirm bias terminology, definitions, and confounder/causal-inference jargon are excluded from the public interview text.",
      "Confirm total interview length falls within 1,215-1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals, matching the paired scenario's probe coverage.",
      "Confirm downstream consequences (District Y review, forecast range) reflect hedged reasoning rather than resolving or proving the phase-2 ambiguity."
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
