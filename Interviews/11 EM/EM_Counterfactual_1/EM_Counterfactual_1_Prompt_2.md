You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Counterfactual_1",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Emergency Management Training Officer",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Exercise-to-Real Transition During Winter Storm Shelter Handoff (Time-Pressure Isolated Variant)",
    "scenario_summary_internal": "This is a counterfactual variant of EM_Biased_1. The same Training Officer manages the same exercise-to-real transition, the same storm, and the same newly rotated liaison officers, but the single causal variable that is changed is the amount of time available before the shift-handoff briefing: instead of roughly ten minutes under acute time pressure, the officer has about twenty-five minutes with no immediate competing task. All other material facts, including the storm timeline, staffing, transportation constraints, and the fourth decision point, are held constant. The officer still gives the abbreviated, shorthand handoff briefing assuming the new liaison officers share the same background familiarity with shelter zone and muster-point terminology, and the same downstream misdirection occurs. This isolates the assumption-of-shared-knowledge mechanism from the alternative explanation that the shorthand briefing was purely a time-constrained economization (Curse of Knowledge).",
    "occupational_realism": {
      "objective": "Maintain safe, coordinated shelter operations and evacuation transport during an unplanned transition from a training exercise to a real weather emergency, while handing off command smoothly to an incoming Incident Commander.",
      "setting": "County Emergency Operations Center (EOC) and an affiliated public shelter, during a scheduled full-scale training exercise that is overtaken by an actual severe winter storm causing communications outages and road closures.",
      "constraints": [
        "Primary radio and phone lines degraded by storm damage",
        "Newly rotated shelter liaison staff and volunteer coordinators unfamiliar with facility-specific procedures",
        "Limited transport assets shared between exercise injects and real evacuee movement",
        "Hard deadline before roads become impassable",
        "Ambiguity about which reports are scripted exercise injects versus real conditions",
        "Unlike the paired base scenario, the officer has approximately twenty-five minutes available before the next competing task, rather than roughly ten"
      ],
      "stakeholders": [
        "Emergency Management Training Officer (protagonist)",
        "Newly rotated shelter liaison officers",
        "Volunteer shelter coordinators",
        "Transportation/logistics section chief",
        "Incoming on-call Incident Commander",
        "Exercise evaluators/controllers"
      ],
      "technical_terms_to_use": [
        "shelter-in-place",
        "muster point",
        "liaison officer",
        "incident action plan",
        "shift handoff",
        "transportation section",
        "unified command"
      ],
      "technical_terms_to_avoid": [
        "highly specialized ICS position titles beyond liaison/section chief",
        "hazmat-specific technical jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Scripted exercise inject reports a minor comms disruption",
          "Actual weather service warning shows a fast-moving winter storm approaching",
          "Some field reports arriving are unclear whether they are scripted or real"
        ],
        "new_information_after_decision": [
          "Confirmation that a real communications tower failure has occurred, distinct from any scripted inject",
          "Reports that some roads are already closing faster than forecast"
        ],
        "alternatives": [
          "Continue the exercise as scripted and treat the comms report as an inject",
          "Pause the exercise to verify against real weather data before proceeding"
        ],
        "intended_action": "Training Officer decides to pause the exercise and verify conditions against real-time weather reporting before continuing."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two newly rotated liaison officers have just arrived to relieve the exercise-shift shelter team",
          "The shelter has an internal zone and muster-point system the Training Officer has used for years",
          "Unlike the base scenario, no immediate competing task is pending; the officer has roughly twenty-five minutes before needing to turn to transportation matters"
        ],
        "new_information_after_decision": [
          "The new liaison officers later misdirect evacuees to the wrong muster point during a subsequent headcount, despite the extra briefing time",
          "A volunteer coordinator asks what 'Zone C protocol' means partway through the shift"
        ],
        "alternatives": [
          "Use the available time to give a full walkthrough briefing covering zone layout, muster points, and terminology from first principles",
          "Give a brief handoff referencing established shorthand ('the usual Zone C protocol,' 'muster at the standard point'), assuming the new liaisons already understand shelter layout and terms, even though more time was available"
        ],
        "intended_action": "Training Officer gives the same abbreviated handoff briefing using internal shorthand, assuming the incoming liaison officers share the same background familiarity with shelter procedures, despite having ample uncommitted time to explain more fully."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two buses are available; three sites are requesting transport",
          "Road closures are worsening in one sector faster than others",
          "Transportation section chief flags fuel and driver-hours constraints"
        ],
        "new_information_after_decision": [
          "The prioritized site clears successfully before road closure",
          "One deprioritized site experiences a delay that increases evacuee wait time but is later resolved without injury"
        ],
        "alternatives": [
          "Split remaining transport evenly across all three requesting sites",
          "Prioritize the site facing the fastest-closing road access first"
        ],
        "intended_action": "Training Officer directs the transportation section to prioritize the site with the fastest-closing road access."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "An on-call Incident Commander has arrived to formally take over the real incident",
          "The exercise evaluators are still expecting a formal exercise debrief",
          "Some shelter operations are still using ad hoc handoff arrangements from phase 2"
        ],
        "new_information_after_decision": [
          "The Incident Commander requests a full written status briefing rather than a verbal summary",
          "The exercise is formally suspended and reclassified as a real activation"
        ],
        "alternatives": [
          "Continue running both the exercise debrief and real incident command informally in parallel",
          "Fully suspend the exercise, transfer command authority formally to the Incident Commander, and issue a written status briefing"
        ],
        "intended_action": "Training Officer formally suspends the exercise and transfers command to the Incident Commander with a written status briefing."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what was happening right before you realized this was becoming a real incident?",
        "What was your role supposed to be that day, and how did it change?"
      ],
      "timeline_reconstruction": [
        "What information did you have at each point, and where did it come from?",
        "What happened right after each of your major decisions?",
        "Were there moments where it was unclear whether something was scripted or real?"
      ],
      "decision_point_probes": [
        "What cues told you this was a real event rather than an exercise inject?",
        "You mentioned you had some time before turning to transportation — what did you decide to do with it during the liaison briefing?",
        "What alternatives did you consider for allocating the buses, and why did you rule the others out?",
        "How did you decide it was time to formally hand off to the Incident Commander?"
      ],
      "closing_hypotheticals": [
        "Given that you actually had time available for the liaison briefing, what would have changed had you used it differently?",
        "If the storm had hit an hour later, would your resource decisions have changed?",
        "Looking back, what would you tell a less experienced officer to watch for in a similar transition?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "decision_point": 2,
        "mechanism": "Expert briefer with years of familiarity with facility-specific shorthand assumes newly rotated liaison staff share the same tacit operational knowledge, and therefore omits explanatory detail, even when ample uncommitted time is available to explain more fully.",
        "affected_reasoning_operation": "Communication/briefing content selection when time pressure is not a binding constraint",
        "evidence_available_at_time": [
          "Liaison officers are newly rotated in and have not previously worked this shelter",
          "Approximately twenty-five minutes are available with no immediate competing task",
          "Training Officer has years of routine familiarity with zone/muster terminology"
        ],
        "required_textual_manifestation": "The Training Officer describes having available time before the next task, yet still delivers the handoff briefing in abbreviated shorthand ('the usual Zone C protocol,' 'muster at the standard point'); when probed about what was done with the extra time, the officer reveals the shorthand was used because the terms felt self-evidently understood, not because of a deliberate time trade-off; the same downstream misdirection and terminology-confusion consequence occurs.",
        "plausible_nonbias_interpretation": "The officer might describe the shorthand as simply their normal communication style with any liaison officer, independent of actual understanding, which could be read as a habitual register rather than a knowledge-assumption failure -- this must be distinguished by the officer's explicit acknowledgment, under probing, that they did not check what the liaisons already knew despite having time to do so.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "curse of knowledge",
          "assumed shared knowledge",
          "cognitive bias",
          "hindsight bias",
          "egocentric communication bias"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "EM_Biased_1",
      "features_to_match": [
        "Storm severity and general timeline",
        "Identity, role, and experience level of the liaison officers",
        "Transportation resource constraints and the phase 3 decision",
        "Phase 1 and phase 4 decisions and reasoning",
        "Use of the same shorthand terminology ('Zone C protocol', 'standard muster point')",
        "The downstream misdirection consequence at the shelter"
      ],
      "features_to_remove_or_change": [
        "Amount of time available before the shift-handoff briefing (changed from ~10 minutes under acute time pressure to ~25 minutes with no immediate competing task)"
      ],
      "ambiguity_boundary": "Not applicable as a control; this is a counterfactual variant, not a zero-bias control. The manifest still requires exactly one Curse of Knowledge instance."
    },
    "counterfactual_specification": {
      "causal_variable": "Amount of time available for the shift-handoff briefing before the Training Officer had to move to a competing task",
      "original_state": "In EM_Biased_1, only about ten minutes were available before the officer needed to turn to transportation duties, creating acute time pressure during the liaison briefing.",
      "counterfactual_state": "In this variant, about twenty-five minutes are available with no immediate competing task, removing acute time pressure as a plausible sole explanation for the abbreviated briefing.",
      "variables_to_hold_constant": [
        "Storm timeline and severity",
        "Liaison officers' identity, role, and experience level",
        "Transportation resource constraints and phase 3 reasoning",
        "Phase 1 and phase 4 decisions and reasoning",
        "The specific shorthand terms used and the downstream misdirection consequence"
      ],
      "expected_causal_difference": "Because the officer still gives the same abbreviated briefing despite having ample time, the interview should make it harder to attribute the communication gap to time pressure alone, strengthening the inference that the gap stems from an assumption that the liaison officers already shared the officer's background knowledge.",
      "causal_test_question": "Does removing acute time pressure change whether the Training Officer gives a fuller explanatory briefing, or does the abbreviated, assumption-laden briefing persist regardless of available time?"
    },
    "generation_checks": [
      "Exactly one Curse of Knowledge instance planned, matching manifest occurrence count of 1, consistent with counterfactual condition rules requiring the manifest to still be implemented",
      "Instance assigned to decision point 2, distinct from the other three decision points which contain no intended bias instances",
      "Only one causal variable changed relative to EM_Biased_1: time available before the liaison briefing",
      "All other material facts, actors, and the phase 3 and phase 4 decisions held constant relative to the base scenario",
      "No bias labels or psychological terminology will appear in the public interview text",
      "Interview scoped to fit 1,215-1,485 word range across 4 decision points with proportionate probe coverage",
      "Plausible non-bias explanation (habitual communication register) documented for the single instance to prevent mechanical over-attribution",
      "Downstream consequence (misdirection) preserved from the base scenario to keep the causal comparison clean"
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
