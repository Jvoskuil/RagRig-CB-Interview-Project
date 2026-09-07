You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "NP_Vocab_Control_7",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Process Control Operator (Chemical/Petrochemical Refinery)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Reactor Feed Heater Temperature Excursion During Night-to-Day Shift Handover (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A control-room operator at a petrochemical refinery's catalytic reforming unit encounters a developing high-temperature/high-pressure excursion on the reactor feed heater train during a shift handover under production-throughput pressure. The operator methodically cross-checks the alarm against corroborating trend data, weighs both recent and older log evidence, adapts the routine feed-increase procedure to the abnormal conditions, tests candidate diagnostic hypotheses against available discriminating signals, and selects a corrective action after comparing the available checklist options against the closing regeneration window. The scenario mirrors the paired biased scenario's setting, actors, constraints, and decision structure, but every decision is supported by balanced consideration of available evidence and alternatives.",
    "occupational_realism": {
      "objective": "Diagnose and correct an abnormal thermal/pressure trend on the reforming unit's feed heater and lead reactor before it threatens catalyst integrity or triggers an automatic unit trip, while minimizing unplanned production loss ahead of a scheduled regeneration outage.",
      "setting": "Central control room of a catalytic reforming unit at a mid-size petrochemical refinery, day-to-night shift transition, DCS (distributed control system) console with trend screens, alarm annunciator panel, radio contact with outside field operators.",
      "constraints": [
        "Production target tied to a narrow regeneration outage window in 6 hours",
        "Limited outside operator availability for field verification during shift change",
        "Alarm system has a known history of nuisance/false alarms on this specific sensor loop",
        "Time pressure to resolve the trend before board handover documentation is due",
        "No direct real-time catalyst bed temperature profile, only proxy sensors"
      ],
      "stakeholders": [
        "Incoming day-shift Process Control Operator (interviewee)",
        "Outgoing night-shift operator",
        "Field operator",
        "Unit shift supervisor",
        "Process engineer on call"
      ],
      "technical_terms_to_use": [
        "reactor feed heater",
        "catalytic reforming unit",
        "DCS trend screen",
        "high-temperature alarm setpoint",
        "catalyst bed",
        "compressor surge",
        "regeneration window",
        "annunciator panel",
        "board operator log"
      ],
      "technical_terms_to_avail": [],
      "technical_terms_to_avoid": [
        "nuclear reactor",
        "radiation",
        "containment breach",
        "core meltdown"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "High-temperature alarm activates on reactor feed heater outlet",
          "Operator log shows this same alarm has triggered 11 times in the past month, all resolved as instrument drift",
          "A slower, less visually prominent pressure-differential trend on an adjacent screen has begun a gradual rise over the last 2 hours"
        ],
        "new_information_after_decision": [
          "Field operator confirms outlet thermocouple reading is accurate, not drifting",
          "Pressure-differential trend is already noted as a corroborating factor when the alarm is addressed"
        ],
        "alternatives": [
          "Acknowledge and silence alarm as likely nuisance based on history, continue monitoring",
          "Dispatch field operator immediately to verify heater outlet temperature independently",
          "Cross-check the pressure-differential trend alongside the alarm before deciding"
        ],
        "intended_action": "Operator pulls up the pressure-differential trend alongside the alarm before acknowledging, notes that the two together are less consistent with a pure nuisance trip than prior isolated occurrences, and dispatches the field operator to verify the thermocouple independently while continuing to monitor both trends."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Night-shift handover report describes 'stable, unremarkable' readings for the last 4 hours",
          "Board operator log (older entries, several days back) shows a slow upward drift in feed heater duty that was flagged but not resolved",
          "Production schedule calls for a feed rate increase to meet output target before the regeneration window"
        ],
        "new_information_after_decision": [
          "Feed rate increase proceeds at a reduced initial ramp with closer monitoring of outlet temperature",
          "Field operator reports unusual heat shimmer near the heater firebox during walkdown"
        ],
        "alternatives": [
          "Proceed with the standard feed-rate increase sequence used for routine handovers",
          "Delay the increase and review the multi-day trend log before acting",
          "Consult the process engineer before adjusting feed rate"
        ],
        "intended_action": "Operator reviews the older drift note against the current handover report, confirms with the night operator whether the drift had actually been corrected or simply stopped appearing in recent readings, and proceeds with a modified, closer-monitored version of the feed-increase sequence rather than the unmodified routine steps."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Combined alarm and shimmer observations could resemble a compressor surge event handled 18 months ago on a similar unit",
          "A separate, more dramatic feed heater tube-rupture incident from about 2 years ago at this same refinery is well known and often discussed in shift briefings",
          "Current instrumentation shows temperature and pressure trending abnormally but does not show the vibration signature that accompanied the earlier compressor surge"
        ],
        "new_information_after_decision": [
          "Heater-specific diagnostic data is gathered and does not match either historical precedent closely",
          "Process engineer confirms that neither the surge vibration signature nor tube-rupture-specific markers are present"
        ],
        "alternatives": [
          "Apply the diagnostic and response template from the prior compressor surge event",
          "Treat the situation as a fresh case and gather heater-specific data before selecting a diagnostic path",
          "Request an independent instrument check to compare against both remembered precedents"
        ],
        "intended_action": "Operator treats the current symptom pattern as a fresh case, checks explicitly for the compressor's vibration signature and the tube-rupture-specific markers before drawing any parallel, and requests an independent instrument check when neither historical signature is confirmed."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Regeneration window closes in under 90 minutes",
          "Temperature and pressure trends continue to climb but have not yet reached automatic trip setpoints",
          "Process engineer is reachable but a full consultation would take 20-30 minutes",
          "Board checklist offers a short list of standard corrective actions for heater excursions"
        ],
        "new_information_after_decision": [
          "The selected corrective action, chosen after a brief comparison of the checklist options, stabilizes the trend and addresses more of the underlying condition than a first-available choice would have",
          "Post-incident review confirms the comparison was reasonable given the time available"
        ],
        "alternatives": [
          "Select the first standard corrective action on the checklist that appears workable",
          "Pause production and conduct a full diagnostic review before acting",
          "Escalate immediately to the process engineer and wait for full guidance"
        ],
        "intended_action": "Operator quickly compares the two or three most relevant checklist options against the available diagnostic data, selects the option best matched to the observed pattern rather than simply the first one listed, and briefs the process engineer concurrently by radio while implementing the action."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you were doing when the alarm first activated?",
        "What was your initial read on the situation?"
      ],
      "timeline_reconstruction": [
        "What happened right after you addressed the alarm?",
        "Walk me through the shift handover conversation and what stood out to you.",
        "What did you notice during the field walkdown report?",
        "What happened as the regeneration window approached?"
      ],
      "decision_point_probes": [
        "What information did you have available at that moment?",
        "What alternatives did you consider, and why did you rule them out?",
        "What made you settle on that particular course of action?",
        "How did your past experience with similar situations factor into this decision?",
        "How much time pressure did you feel, and how did that affect your choice?",
        "How confident were you in your read of the situation at the time?"
      ],
      "closing_hypotheticals": [
        "If the alarm history had been different, would you have responded the same way?",
        "If you had had more time before the regeneration window, what would you have done differently?",
        "Looking back, is there a moment where a different piece of information would have changed your decision?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "NP_Biased_7",
      "features_to_match": [
        "Domain vocabulary (reactor feed heater, catalytic reforming unit, DCS trend screen, annunciator panel, compressor surge, regeneration window, board operator log)",
        "Setting: central control room, day-to-night shift handover, same stakeholders",
        "Structure: exactly 4 decision points in the same chronological sequence and phase order",
        "Difficulty: same operational complexity and moderate ambiguity of underlying cause",
        "Actors: incoming operator, outgoing night operator, field operator, shift supervisor, process engineer",
        "Emotional tone: measured, procedural, mild time pressure escalating across the incident",
        "Same 6-hour regeneration-window constraint and same closing 90-minute final decision window",
        "Same surface incident facts: alarm history, pressure-differential trend, handover report, older drift note, heat shimmer, compressor-surge and tube-rupture precedents, closing checklist decision"
      ],
      "features_to_remove_or_change": [
        "Remove reliance on recalled alarm frequency alone as sufficient grounds for judgment; replace with active cross-checking of the pressure trend before acknowledging",
        "Remove automatic, unmodified execution of the routine feed-increase sequence; replace with a deliberate, adapted response given the abnormal precursor conditions",
        "Remove attention capture by the alarm's prominence alone; replace with explicit joint review of both the alarm and the quieter trend",
        "Remove unweighted discounting of the older drift note due to its age; replace with an explicit check of whether the drift had actually resolved",
        "Remove uncritical template transfer from the prior surge event; replace with an explicit check for the differentiating vibration signature before acting",
        "Remove overweighting of the vivid tube-rupture precedent; replace with an evidence-based comparison against current diagnostic markers",
        "Remove selection of the first workable checklist option without comparison; replace with a brief but real comparison of the top candidate options before choosing"
      ],
      "ambiguity_boundary": "The underlying cause of the excursion remains genuinely uncertain throughout the interview, and the final corrective action's completeness is not fully confirmed until after the interview period, but every decision shown is supported by an active, reasonably thorough evidence-weighing process rather than by a shortcut in reasoning."
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
      "Confirm exactly 4 decision points are present in the timeline, matching the paired scenario's phase structure",
      "Confirm zero intended instances of Availability Bias, Recency Bias, Habit Intrusion, Salience Bias, Similarity Bias, and Bounded Rationality appear anywhere in the interview",
      "Confirm domain vocabulary, setting, stakeholders, constraints, and emotional tone match the paired biased scenario",
      "Confirm each decision point offers at least two plausible alternatives and shows evidence of balanced consideration",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm final interview length falls within 1,215-1,485 words",
      "Confirm consequences described do not mechanically prove decisions were unbiased, preserving genuine uncertainty about root cause",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text",
      "Confirm the operator's reasoning at each decision point reflects active cross-checking, adaptation, or comparison rather than shortcut-driven judgment"
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
