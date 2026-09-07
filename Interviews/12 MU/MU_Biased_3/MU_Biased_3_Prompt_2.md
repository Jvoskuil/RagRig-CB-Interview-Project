You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MU_Biased_3",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Drill and Blast Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Panel 14 Fault-Zone Production Round",
    "scenario_summary_internal": "An underground drill and blast engineer must design and execute a production blast round in Panel 14 of a sublevel stoping operation after geology reports a newly mapped minor fault trace and localized wet ground crossing the panel, while the mill is running low on feed and schedule pressure is high. The engineer must decide whether to modify the established blast pattern, how to charge holes that log anomalies near the fault, how to manage vibration/timing near shaft infrastructure, and how to interpret an imperfect blast outcome afterward. The incident is designed so that a status-quo pattern decision, an overconfident charging override, and an experience-driven post-blast attribution can each occur naturally without being flagged as errors by the narrative or by outcome framing.",
    "occupational_realism": {
      "objective": "Design and fire a safe, on-schedule production blast round in Panel 14 that meets fragmentation and mill-feed targets despite a newly identified geological anomaly.",
      "setting": "Underground metal mine using sublevel open stoping, mid-shift production blasting cycle, Panel 14 approximately 450m below surface, ore body adjacent to a ventilation raise and a service shaft requiring strict vibration control.",
      "constraints": [
        "Mill is running low on ore feed, creating schedule pressure to fire the round on time",
        "Vibration (PPV) limits apply near the shaft and ventilation infrastructure",
        "A geologist has newly mapped a minor fault trace with localized moisture crossing part of the panel",
        "Blast crew and explosives technician have limited authority to override the engineer's design",
        "Explosives cost and inventory (ANFO vs emulsion) affect charging choices",
        "Two years of stable production history exist for the standard pattern used in adjacent panels"
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
          "The current pattern (burden 2.7m x spacing 3.1m) has been used successfully in three adjacent panels over two years",
          "Mill feed is low and production is one shift behind schedule",
          "No additional geotechnical drilling has been ordered for this panel"
        ],
        "new_information_after_decision": [
          "Several blastholes drilled near the mapped fault log as wet and show minor deviation beyond normal tolerance",
          "The drill crew mentions the ground 'felt looser' in that section but logs it as a routine note"
        ],
        "alternatives": [
          "Proceed with the standard, previously successful burden/spacing pattern, adjusting only stemming slightly",
          "Commission a short geotechnical verification pass before finalizing the pattern",
          "Reduce the round size and treat the fault-affected section as a separate, smaller test round"
        ],
        "intended_action": "The engineer approves the standard pattern with only a minor stemming adjustment, citing the pattern's long track record in the mine, and does not commission further geotechnical verification of the fault trace before drilling proceeds."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Blasthole logs show several wet holes and deviation readings above normal near the fault trace",
          "The explosives technician recommends decking the affected holes and substituting emulsion for the wet sections instead of a fully columned ANFO charge",
          "The engineer has successfully used fully columned ANFO charges in visually similar ground on past rounds",
          "Firing window is fixed to align with the shift's ventilation clearance schedule"
        ],
        "new_information_after_decision": [
          "The charge is loaded as fully columned ANFO across most of the panel, including several of the flagged holes",
          "The technician notes the deviation survey again at loading but does not escalate further once the engineer confirms the plan"
        ],
        "alternatives": [
          "Accept the technician's recommendation to deck and switch to emulsion in the flagged holes",
          "Proceed with the standard fully columned ANFO charge across the panel",
          "Delay charging to re-survey the flagged holes before deciding"
        ],
        "intended_action": "The engineer overrides the technician's recommendation, reassures the crew based on past success with similar-looking ground, and proceeds with the standard fully columned ANFO charge without re-examining the updated deviation and moisture logs in detail."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Seismic/PPV monitoring near the shaft shows readings approaching but not exceeding the vibration limit on the previous comparable round",
          "Two delay-timing options are available: the standard sequence used mine-wide, or a longer-interval sequence recommended by the vibration monitoring vendor for rounds near sensitive infrastructure",
          "Longer delays would modestly reduce fragmentation efficiency but lower peak vibration"
        ],
        "new_information_after_decision": [
          "The chosen delay sequence keeps vibration within limits and fragmentation within an acceptable range",
          "No complaints or exceedances are recorded near the shaft after firing"
        ],
        "alternatives": [
          "Use the standard mine-wide delay sequence",
          "Adopt the longer-interval sequence recommended for infrastructure protection",
          "Split the round into two smaller fired sequences"
        ],
        "intended_action": "The engineer reviews the current monitoring data directly, weighs the fragmentation-versus-vibration trade-off on its merits, and selects the longer-interval sequence near the shaft-facing section. This decision point is deliberately left free of intended bias instances."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Post-blast survey shows localized overbreak and coarser-than-expected fragmentation concentrated in the fault-affected section",
          "A minor, within-limit vibration spike was recorded near the shaft during that section's firing",
          "Current round's deviation survey and moisture logs from Phase 1 and 2 are available for review",
          "The engineer previously worked at another mine where similar overbreak patterns near fault zones were common and were resolved with a specific standard fix"
        ],
        "new_information_after_decision": [
          "The mine manager asks for a brief explanation and a recommendation for the next round's design",
          "The geologist has not yet been asked to formally review the current round's instrumentation data"
        ],
        "alternatives": [
          "Recommend a formal site-specific investigation using the current round's deviation and moisture data before changing the design",
          "Attribute the outcome to the same fault-zone pattern seen at a previous mine and apply that mine's standard fix directly",
          "Escalate the section's data to the geotechnical engineer for independent review before next round's design is set"
        ],
        "intended_action": "The engineer explains the overbreak by drawing on the similar-looking pattern from a previous mine and recommends applying that prior fix for the next round, without first incorporating the current round's own deviation survey and moisture readings into the diagnosis."
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
        "Had you handled a similar situation before? How did that shape your thinking?",
        "How much time pressure were you under when you made that call?",
        "How confident were you in the ground conditions or data at that point?"
      ],
      "closing_hypotheticals": [
        "If the deviation survey had shown even more pronounced anomalies, would you have made the same charging decision?",
        "If this had been your first round in this panel rather than your hundredth, would your pattern decision have differed?",
        "Looking back, is there a point where a different data source might have changed your diagnosis of the overbreak?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_02",
        "bias": "Status quo bias",
        "decision_point": 1,
        "mechanism": "Preference for the existing, previously validated blast pattern over adapting to new geotechnical information, justified by the pattern's track record rather than by evaluating the fault trace on its own merits",
        "affected_reasoning_operation": "Evidence-selection and decision act: whether to redesign burden/spacing given the new fault-trace report",
        "evidence_available_at_time": [
          "Geologist's updated fracture map with fault trace and moisture note",
          "Two-year successful history of the standard pattern in adjacent panels",
          "Schedule pressure from low mill feed"
        ],
        "required_textual_manifestation": "The engineer explicitly cites the pattern's established track record as the main reason to keep it essentially unchanged, rather than weighing the new fault-trace data on its own terms, while acknowledging the new information exists.",
        "plausible_nonbias_interpretation": "A reasonable engineer might legitimately judge that a minor fault trace does not warrant redesign given strong historical performance and time constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "bias", "heuristic"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Overconfidence Bias",
        "decision_point": 2,
        "mechanism": "Overriding a specific technical recommendation (decking/emulsion substitution) based on generalized confidence from past experience with similar-looking ground, without re-checking the specific updated deviation and moisture data available at that moment",
        "affected_reasoning_operation": "Decision act: charge design and acceptance/rejection of the technician's recommendation",
        "evidence_available_at_time": [
          "Explosives technician's recommendation to deck and substitute emulsion in flagged holes",
          "Updated deviation survey and moisture logs for the flagged holes",
          "Engineer's personal history of successful fully columned ANFO charges in visually similar ground"
        ],
        "required_textual_manifestation": "The engineer describes overriding the technician's recommendation with confident reassurance based on personal track record, and does not describe re-examining the specific updated hole data before deciding.",
        "plausible_nonbias_interpretation": "The engineer may have genuinely and correctly judged the deviation readings as within an acceptable range based on legitimate technical criteria not fully articulated in the interview.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence bias", "bias", "miscalibration"]
      },
      {
        "instance_id": "cb_01",
        "bias": "Experience Bias",
        "decision_point": 4,
        "mechanism": "Attributing the post-blast overbreak outcome primarily to a remembered pattern from a previous mine site, and recommending that prior fix, while not incorporating the current round's own site-specific deviation and moisture data into the diagnosis",
        "affected_reasoning_operation": "Causal attribution and recommendation act: diagnosing the cause of overbreak and proposing next-round design changes",
        "evidence_available_at_time": [
          "Post-blast survey showing localized overbreak and coarse fragmentation in the fault-affected section",
          "Current round's deviation survey and moisture logs from Phases 1 and 2",
          "Engineer's recollection of a similar-looking overbreak pattern and fix from a previous mine"
        ],
        "required_textual_manifestation": "The engineer explains the cause and proposed fix mainly by reference to the prior mine's similar situation, without describing an examination of the current round's own instrumentation data as part of that diagnosis.",
        "plausible_nonbias_interpretation": "Pattern-matching to prior fault-zone incidents is a legitimate and often efficient diagnostic heuristic in blast engineering, especially under time constraints before a formal review.",
        "strength": "subtle",
        "do_not_make_explicit": ["experience bias", "bias", "overgeneralization"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "NONE",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is a biased-condition scenario with no paired control specified."
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
      "Confirm exactly 4 decision points appear, with Decision Point 3 free of intended bias instances.",
      "Confirm exactly one instance each of Experience Bias, Status quo bias, and Overconfidence Bias appears, at the assigned decision points only.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the interview text.",
      "Confirm each instance has a plausible non-bias interpretation available in the surrounding narrative.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals for each decision point.",
      "Confirm final word count falls within 1,215-1,485 words.",
      "Confirm consequences (overbreak, vibration spike) do not explicitly confirm or deny bias, remaining consistent with routine operational variance."
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
