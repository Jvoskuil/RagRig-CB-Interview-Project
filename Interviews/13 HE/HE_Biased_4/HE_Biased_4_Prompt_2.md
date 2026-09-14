You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HE_Biased_4",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Structural Fire Engineer (Performance-Based Design)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Atrium Tower Occupancy Signoff Under Schedule Pressure",
    "scenario_summary_internal": "A structural fire engineer leading performance-based design (PBD) verification for a 42-story mixed-use tower must close out four remaining compliance items before the developer's occupancy certificate deadline: a late substitute-glazing test report, a borderline smoke-control CFD result requiring re-modeling, a QA punch-list reprioritization occurring two weeks after a widely publicized high-rise fire elsewhere, and a final egress-modeling run using software default occupant parameters. Each decision is made under time and commercial pressure, with plausible technical justifications available at every step.",
    "occupational_realism": {
      "objective": "Complete and sign off the fire engineering verification package (glazing fire resistance, smoke control performance, compartmentation QA, egress modeling) so the developer can obtain the occupancy certificate on schedule.",
      "setting": "Fire engineering consultancy office and construction site of a 42-story mixed-use (office/residential/assembly) tower in final commissioning phase, four days before a contractual occupancy deadline.",
      "constraints": [
        "Hard occupancy certificate deadline set by developer contract with liquidated-damages exposure",
        "Independent QA reviewer flags open items requiring further verification",
        "Limited remaining site-access days for punch-list inspections",
        "Substitute glazing product proposed late by contractor for cost/lead-time reasons",
        "Modeling software licensed with generic default occupant-behavior libraries not calibrated to this occupancy mix"
      ],
      "stakeholders": [
        "Lead structural fire engineer (interviewee)",
        "Independent QA/peer reviewer",
        "Developer's project director",
        "General contractor",
        "Glazing subcontractor and Vendor B (substitute glazing supplier)",
        "Building control/approving authority"
      ],
      "technical_terms_to_use": [
        "performance-based design (PBD)",
        "fire resistance rating",
        "integrity and insulation criteria",
        "CFD smoke modeling",
        "tenability criteria / visibility threshold",
        "compartmentation",
        "cladding fire-stopping",
        "stair pressurization",
        "pre-movement time",
        "egress/evacuation modeling",
        "punch list",
        "commissioning"
      ],
      "technical_terms_to_avoid": [
        "illusion of truth",
        "action bias",
        "affect bias",
        "default bias",
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Original glazing spec was approved with a UL/EN test report showing 90-minute integrity rating",
          "Contractor proposes a substitute product from Vendor B for cost and lead-time reasons",
          "Vendor B's technical bulletin, cover email, and marketing brochure each state '90 minutes, independently verified' fire resistance",
          "The underlying test referenced in all three documents used a different mounting/frame configuration than the project's installation detail"
        ],
        "new_information_after_decision": [
          "Building control later requests the raw test report and mounting schedule for the substitute product",
          "The raw report shows the mounting configuration differs from the as-installed detail, requiring a compatibility assessment"
        ],
        "alternatives": [
          "Request the raw underlying test report and mounting schedule before accepting the substitution",
          "Commission an independent verification test or engineering judgment memo for the as-installed configuration",
          "Provisionally accept the substitution based on the consistency of the vendor's repeated claims"
        ],
        "intended_action": "Engineer provisionally accepts the substitute glazing, citing that the 90-minute rating appears 'consistently documented across multiple vendor sources.'"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary smoke-control CFD model shows borderline visibility at the escape-stair door at approximately six minutes",
          "Independent QA review recommends re-running the model with a revised HVAC shutdown sequence, adding five working days",
          "Occupancy certificate deadline is four days away",
          "Fan commissioning is the next scheduled construction milestone and is on the critical path"
        ],
        "new_information_after_decision": [
          "Fan commissioning proceeds and passes initial functional tests",
          "The revised CFD re-run, completed later than planned, shows the visibility margin was narrower than assumed under a different plausible shutdown sequence"
        ],
        "alternatives": [
          "Pause the commissioning phase and wait for the revised CFD re-run before proceeding",
          "Authorize fan commissioning to proceed now while treating the re-run as a parallel, non-blocking check",
          "Implement an interim mechanical mitigation and hold the next milestone pending re-run results"
        ],
        "intended_action": "Engineer authorizes fan commissioning to proceed immediately 'to keep the program moving,' without making the re-run result a hold point for the next milestone."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A widely reported apartment-tower fire in another country, involving dramatic cladding-fire footage, occurred two weeks earlier",
          "This building uses a different cladding and compartmentation system with adequate prior documentation",
          "Remaining QA punch list includes open items across cladding fire-stopping, lift-shaft pressurization (unresolved fan-door deficiency), and egress signage",
          "Only two inspection days remain before signoff"
        ],
        "new_information_after_decision": [
          "The pressurization fan-door deficiency is later found during a follow-up visit to be more significant than initially logged",
          "The cladding re-inspection finds no new deficiencies beyond what was already documented"
        ],
        "alternatives": [
          "Rank the remaining punch-list items using the project's standard risk/probability matrix",
          "Reallocate the final two inspection days toward cladding-related items ahead of the pressurization deficiency",
          "Split the remaining time evenly across all three open item categories"
        ],
        "intended_action": "Engineer reallocates the final two inspection days to re-inspect cladding fire-stopping, deprioritizing the pressurization fan-door deficiency."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Egress-modeling software ships with default pre-movement time and flow-rate parameters calibrated for a generic office occupancy",
          "This building has a mixed-use occupancy (office, residential, assembly) with a different demographic and behavioral profile",
          "A colleague flags that project-specific pre-movement survey data and comparable mixed-use building studies are available",
          "Substituting project-specific values requires additional recalibration effort before the deadline"
        ],
        "new_information_after_decision": [
          "The compliance run using default parameters passes the required egress time threshold with limited margin",
          "A later audit note observes the default library's behavioral assumptions were developed for a different occupancy type"
        ],
        "alternatives": [
          "Substitute the project-specific survey-based pre-movement values into the model",
          "Blend the default values with a partial adjustment based on the available survey data",
          "Retain the software's default parameters for the final compliance run with a documented justification"
        ],
        "intended_action": "Engineer retains the software's default pre-movement and flow parameters for the final compliance run rather than substituting the available project-specific data."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role in signing off this tower's fire engineering package?",
        "What was the overall objective in the final week before the occupancy deadline?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what triggered the glazing substitution request?",
        "Walk me through the sequence of events between the CFD result and the fan commissioning decision.",
        "How did the punch-list reprioritization unfold over those final two days?",
        "When did the egress-modeling parameter question come up relative to the other decisions?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you when you decided to accept the substitute glazing?",
        "What made the vendor's documentation convincing at that point?",
        "What alternatives did you consider before authorizing fan commissioning to proceed?",
        "How did you weigh the five-day delay against the borderline CFD result?",
        "What led you to prioritize the cladding re-inspection over the pressurization deficiency?",
        "How did the recent tower fire in the news factor into that prioritization, if at all?",
        "Why did you keep the software's default pre-movement parameters for the final run?",
        "Was the project-specific survey data considered, and if so, how?"
      ],
      "closing_hypotheticals": [
        "If the vendor documentation had come from a single source instead of three, would you have handled it differently?",
        "If there had been no deadline pressure, would the CFD re-run have been a hold point?",
        "If the fire in the news had not occurred, would the punch-list priority have been different?",
        "If recalibrating the egress model had taken less effort, would you have used the survey data?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "he4_iot_01",
        "bias": "Illusion of Truth effect",
        "decision_point": 1,
        "mechanism": "Repeated exposure to the same '90-minute, independently verified' claim across three separate vendor documents (spec sheet, email, brochure) increases the engineer's subjective sense of its credibility, even though all three repetitions trace back to a single underlying test with a differing mounting configuration.",
        "affected_reasoning_operation": "Evaluation of source credibility / evidence weighting for a technical claim",
        "evidence_available_at_time": [
          "Three vendor documents repeating an identical fire-resistance claim",
          "No independent second test or raw report yet obtained",
          "A mounting-configuration discrepancy that is discoverable but not yet checked"
        ],
        "required_textual_manifestation": "The interviewee should explicitly attribute their increased confidence to the claim being 'documented consistently' or 'repeated across multiple sources,' rather than to independent verification, and should not mention checking whether the sources shared a common underlying test.",
        "plausible_nonbias_interpretation": "A reasonable engineer might treat multiple corroborating vendor documents as a legitimate (if incomplete) form of triangulation under time pressure, without this reflecting a truth-illusion effect.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "illusion of truth",
          "repetition effect",
          "familiarity breeds belief"
        ]
      },
      {
        "instance_id": "he4_ab_01",
        "bias": "Action bias",
        "decision_point": 2,
        "mechanism": "Faced with a borderline, uncertain CFD result and a recommended pause, the engineer favors authorizing an active step (proceeding with fan commissioning) over the passive/waiting alternative, framing forward motion itself as risk-reducing regardless of the analytic case for waiting.",
        "affected_reasoning_operation": "Choice between action and inaction under time pressure and uncertainty",
        "evidence_available_at_time": [
          "Borderline visibility margin in preliminary CFD results",
          "A specific QA recommendation to re-run the model before the next milestone",
          "A four-day deadline creating pressure to keep the schedule moving"
        ],
        "required_textual_manifestation": "The interviewee should justify authorizing commissioning primarily in terms of 'needing to do something' or 'keeping momentum,' rather than through a risk-based justification for why proceeding without the re-run was analytically sound.",
        "plausible_nonbias_interpretation": "Proceeding with a non-destructive commissioning step in parallel with a re-run could be a legitimate schedule-risk management strategy, not necessarily a bias.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "action bias",
          "bias toward action",
          "omission versus commission"
        ]
      },
      {
        "instance_id": "he4_afb_01",
        "bias": "Affect Bias",
        "decision_point": 3,
        "mechanism": "The emotionally vivid recent cladding-fire disaster elsewhere increases the perceived risk salience of cladding fire-stopping on this project, causing the engineer to reallocate scarce inspection time toward the emotionally resonant system rather than toward the item with an already-documented, arguably more severe technical deficiency (the pressurization fan-door issue).",
        "affected_reasoning_operation": "Risk prioritization / resource allocation across competing open QA items",
        "evidence_available_at_time": [
          "News coverage of an unrelated but emotionally striking high-rise fire two weeks prior",
          "An already-logged, unresolved pressurization fan-door deficiency",
          "No updated technical data suggesting this building's cladding risk had actually increased"
        ],
        "required_textual_manifestation": "The interviewee's explanation for reprioritizing toward cladding should reference the emotional impact or vividness of the recent fire (e.g., feeling it was 'too close for comfort' or wanting to be 'extra sure' after seeing it), rather than new technical evidence about this building's cladding.",
        "plausible_nonbias_interpretation": "Increased public and regulatory scrutiny of cladding after a major incident could be a legitimate, defensible reason to revisit cladding documentation, independent of any emotional reaction.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "affect bias",
          "emotional salience",
          "availability from vivid recent event"
        ]
      },
      {
        "instance_id": "he4_db_01",
        "bias": "Default bias",
        "decision_point": 4,
        "mechanism": "The engineer retains the modeling software's pre-set occupant-behavior parameters for the final compliance run rather than substituting available project-specific data, favoring the path requiring no active change over an equally or more available alternative.",
        "affected_reasoning_operation": "Selection of model input parameters / choice between status-quo default and available alternative data",
        "evidence_available_at_time": [
          "Software default pre-movement and flow-rate parameters calibrated for generic office occupancy",
          "Availability of project-specific survey data and comparable mixed-use building studies, flagged by a colleague",
          "Awareness that this building's occupancy mix differs from the office-calibrated default"
        ],
        "required_textual_manifestation": "The interviewee should explain keeping the default values in terms of it being the standard/pre-set path or requiring less effort to change, while acknowledging the mismatch between the default's calibration population and the actual occupancy mix, without providing a substantive technical justification for why the default was actually more appropriate.",
        "plausible_nonbias_interpretation": "If the software vendor's default had been independently validated for mixed-use buildings, retaining it could be a legitimate, evidence-based choice rather than a default bias.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "default bias",
          "status quo",
          "path of least resistance"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition and no paired control scenario ID was supplied."
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
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Exactly one intended bias instance is embedded per decision point, matching the manifest total of four.",
      "No bias name, definition, or psychological label appears in the planned public interview text.",
      "Each occurrence has a distinct evidence trace, decision point, and plausible non-bias interpretation.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Planned content supports a 1,215-1,485 word interview without repetitive exposition.",
      "Consequences described do not mechanically prove or disprove bias presence."
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
