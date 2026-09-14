You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MU_Ambigious_3",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Drill and Blast Engineer",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Panel 14 Fault-Zone Production Round (Ambiguous Reasoning Variant)",
    "scenario_summary_internal": "A drill and blast engineer manages the same Panel 14 production round context as the paired biased scenario - a newly mapped minor fault trace, schedule pressure from low mill feed, and vibration-sensitive shaft infrastructure - but at each decision point the engineer visibly weighs competing considerations, takes partial or hedged actions, and encounters genuinely equivocal outcomes. The reasoning is deliberately underdetermined: plausible non-bias explanations (limited resources, real trade-offs, incomplete but reasonably interpreted data) are always available alongside any resemblance to the target biases, and no decision is written to unambiguously instantiate experience bias, status quo bias, or overconfidence bias.",
    "occupational_realism": {
      "objective": "Design and fire a safe, on-schedule production blast round in Panel 14 that meets fragmentation and mill-feed targets despite a newly identified geological anomaly.",
      "setting": "Underground metal mine using sublevel open stoping, mid-shift production blasting cycle, Panel 14 approximately 450m below surface, ore body adjacent to a ventilation raise and a service shaft requiring strict vibration control.",
      "constraints": [
        "Mill is running low on ore feed, creating schedule pressure to fire the round on time",
        "Vibration (PPV) limits apply near the shaft and ventilation infrastructure",
        "A geologist has newly mapped a minor fault trace with localized moisture crossing part of the panel",
        "Blast crew and explosives technician have limited authority to override the engineer's design",
        "Explosives cost and inventory (ANFO vs emulsion) affect charging choices",
        "Two years of stable production history exist for the standard pattern used in adjacent panels",
        "Only a partial geotechnical spot-check, not a full survey, is feasible within the shift"
      ],
      "stakeholders": [
        "Drill and Blast Engineer (interviewee)",
        "Mine Geologist",
        "Blast Crew Supervisor",
        "Explosives Technician (vendor representative)",
        "Mine Manager",
        "Ventilation and Safety Officer"
      ],
      "technical_terms_to_use": [
        "burden and spacing",
        "powder factor",
        "stemming",
        "delay timing / initiation sequence",
        "fragmentation",
        "overbreak",
        "fly-rock",
        "blasthole deviation survey",
        "decking",
        "ANFO",
        "emulsion explosive",
        "PPV (peak particle velocity)",
        "fault trace",
        "sublevel stoping",
        "mill feed"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias",
        "overconfidence",
        "status quo bias",
        "experience bias"
      ],
      "constraints_note": "No domain constraints or excluded themes were specified by the caller."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Geologist's updated fracture map shows a minor fault trace crossing roughly one-third of Panel 14, with a noted moisture seep",
          "The current pattern (burden 2.7m x spacing 3.1m) has performed well in three adjacent panels over two years",
          "Mill feed is low and production is one shift behind schedule",
          "A full geotechnical resurvey would take a full shift; a limited spot-check of a few holes is feasible within an hour"
        ],
        "new_information_after_decision": [
          "The spot-check on three holes near the trace comes back within normal tolerance, but does not cover the full fault-affected zone",
          "Two holes just outside the spot-checked area later log as wet"
        ],
        "alternatives": [
          "Proceed with the standard pattern unmodified",
          "Commission a full geotechnical resurvey before finalizing the pattern",
          "Run a limited spot-check on a subset of holes near the trace and adjust only if it flags a problem"
        ],
        "intended_action": "The engineer selects the limited spot-check option, explicitly weighing the cost of a full resurvey against the schedule pressure and the pattern's track record, and proceeds with the standard pattern after the partial check comes back clear, while acknowledging it did not cover the whole fault-affected section."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Blasthole logs show a few wet holes and mild deviation readings near the fault trace, including two outside the earlier spot-check zone",
          "The explosives technician recommends decking and emulsion substitution for the specific flagged holes, not the whole panel",
          "The engineer has used fully columned ANFO successfully in similar-looking ground before, but also recalls one case where wet ground required adjustment",
          "Substituting emulsion for only the flagged holes costs modest additional time and inventory"
        ],
        "new_information_after_decision": [
          "The flagged holes are decked with emulsion as recommended; the rest of the panel is charged with standard ANFO",
          "One additional hole not on the original flagged list also turns out to be borderline wet, discovered only during loading"
        ],
        "alternatives": [
          "Adopt the technician's recommendation for the specifically flagged holes only",
          "Charge the entire panel uniformly with standard ANFO",
          "Charge the entire panel with emulsion as a precaution"
        ],
        "intended_action": "The engineer adopts a middle-ground approach, decking and substituting emulsion only in the holes flagged by the survey, explicitly citing both the technician's data and past experience with similar ground as joint inputs, while acknowledging that the survey may not have caught every borderline hole."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Seismic/PPV monitoring near the shaft shows readings that are elevated but within limit on one sensor and borderline on a second sensor with a different offset",
          "Two delay-timing options are available: the standard mine-wide sequence, or a longer-interval sequence recommended for infrastructure protection",
          "The two sensors give somewhat inconsistent readings, and the vibration vendor's guidance does not fully resolve which sensor is more representative for this geometry"
        ],
        "new_information_after_decision": [
          "The fired round keeps both sensors within limit, though the second sensor remains closer to threshold than the first",
          "No complaints are recorded, but the vibration margin is narrower than on comparable past rounds"
        ],
        "alternatives": [
          "Use the standard mine-wide delay sequence based on the first sensor's reading",
          "Adopt the longer-interval sequence based on the more conservative second sensor's reading",
          "Request a third monitoring point before deciding"
        ],
        "intended_action": "The engineer discusses the conflicting sensor readings with the safety officer, chooses the longer-interval sequence as the more conservative option given the ambiguity, and documents that the discrepancy between sensors was not fully resolved before firing."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Post-blast survey shows localized overbreak and coarser fragmentation concentrated near the fault-affected section, including areas both inside and outside the original spot-check zone",
          "Current round's deviation survey, moisture logs, and vibration data are available for review",
          "The engineer recalls a broadly similar overbreak pattern from a previous mine, but also notes this round had incomplete survey coverage and a mixed charging approach",
          "The mine manager wants a preliminary explanation before a formal review can be scheduled"
        ],
        "new_information_after_decision": [
          "The engineer flags multiple plausible contributing factors to the manager rather than a single cause",
          "The geologist agrees to review the current round's instrumentation data before any design change is finalized"
        ],
        "alternatives": [
          "Attribute the outcome primarily to the same fault-zone pattern seen at a previous mine",
          "Attribute the outcome primarily to the incomplete spot-check coverage and mixed charging approach specific to this round",
          "Present both explanations as unresolved pending further review and hold off on a firm recommendation"
        ],
        "intended_action": "The engineer explicitly lays out both the prior-experience pattern and the current round's specific data gaps as competing explanations, declines to commit to a single cause, and recommends waiting for the geologist's review before changing the next round's design."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role in planning the Panel 14 production round?",
        "What was the operational objective for this particular round?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you know at that point?",
        "What new information came in as drilling and charging progressed?",
        "How did the sequence of events unfold from pattern approval through firing?"
      ],
      "decision_point_probes": [
        "What cues or signals stood out to you at that moment?",
        "What information sources did you rely on for that decision?",
        "What were you trying to achieve with that choice?",
        "What alternatives did you consider, and why did you rule them out?",
        "What was the main basis for the decision you made?",
        "Had you handled a similar situation before? How did that shape your thinking, if at all?",
        "How much time pressure were you under when you made that call?",
        "How confident were you in the ground conditions or data at that point?"
      ],
      "closing_hypotheticals": [
        "If the spot-check had covered the whole fault-affected zone, do you think the outcome would have been different?",
        "If the two vibration sensors had agreed with each other, would the timing decision have been easier?",
        "Looking back, is there a piece of information that could have resolved the overbreak question either way?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MU_Biased_3",
      "features_to_match": [
        "Domain and role (drill and blast engineer, sublevel stoping mine)",
        "Setting: Panel 14, fault trace, mill feed pressure, shaft vibration constraints",
        "Four decision points in the same narrative order and general topic (pattern, charging, timing, post-blast diagnosis)",
        "Technical vocabulary and terminology set",
        "Stakeholders and their roles",
        "Overall word count target and probe structure",
        "Emotional tone (measured, professional, mild time pressure)"
      ],
      "features_to_remove_or_change": [
        "Replace single-track-record justification for the pattern decision with an explicit partial-verification action",
        "Replace outright override of the technician's recommendation with a partial, jointly-reasoned adoption",
        "Introduce genuinely conflicting sensor data at the vibration decision rather than a single clean data source",
        "Replace confident single-cause post-blast attribution with an explicit, unresolved multi-cause account"
      ],
      "ambiguity_boundary": "Reasoning must remain genuinely underdetermined: the engineer's choices are defensible given real resource and information constraints, and no answer should allow a validator to cleanly attribute the outcome to reliance on past success alone, resistance to changing an established approach, or unwarranted confidence in personal judgment over available data. Any resemblance to those patterns must be counterbalanced within the same answer by an explicit acknowledgment of the data's limits or by genuine, described deliberation."
    },
    "counterfactual_specification": {
      "causal_variable": "NONE",
      "original_state": "NONE",
      "counterfactual_state": "NONE",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "NONE",
      "causal_test_question": "NONE"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points appear, matching the paired scenario's topical structure.",
      "Confirm zero intentional instances of Experience Bias, Status quo bias, or Overconfidence Bias appear anywhere in the interview.",
      "Confirm each decision point includes an explicit acknowledgment of data limits, genuine trade-off deliberation, or a hedged/partial action that blocks a clean bias attribution.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the interview text.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals for each decision point.",
      "Confirm final word count falls within 1,215-1,485 words.",
      "Confirm consequences (overbreak, narrow vibration margin) remain genuinely ambiguous as to cause, consistent with multiple competing explanations presented in Phase 4."
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
