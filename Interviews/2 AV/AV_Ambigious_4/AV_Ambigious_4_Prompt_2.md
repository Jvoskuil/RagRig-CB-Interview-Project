You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "AV_Ambigious_4",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Check Airman / Type Rating Instructor (TRI/TRE)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "ADIRU Advisory During Line Check: A Check Airman's Judgment Under Genuine Uncertainty",
    "scenario_summary_internal": "A veteran Type Rating Examiner (TRE) conducts a scheduled Line Check/OPC on a senior widebody captain during a revenue flight. A previously logged, ambiguously-resolved ADIRU advisory resurfaces briefly during climb and again in a different form during cruise, forcing the TRE to make four judgment calls under incomplete information: accepting the aircraft at dispatch, responding to a transient advisory in climb, grading the captain's handling of a minor procedural deviation in cruise, and interpreting a peer's question about his own process during debrief. Each decision is genuinely underdetermined - defensible on multiple grounds - and the eventual maintenance finding does not resolve which considerations actually drove the TRE's reasoning at the time.",
    "occupational_realism": {
      "objective": "Complete a scheduled Line Check / Operator Proficiency Check (OPC) on a type-rated captain while maintaining safe operation of the aircraft, correctly grading crew performance, and responding appropriately to an emergent avionics advisory.",
      "setting": "Flight deck of a twin-aisle commercial aircraft during a scheduled passenger revenue flight, TRE occupying the observer/jump seat with check-ride authority, captain as Pilot Flying under evaluation, first officer as Pilot Monitoring.",
      "constraints": [
        "Fixed check-ride syllabus with limited time to complete required evaluation items",
        "Dispatch reliability and schedule pressure from operations control",
        "MEL (Minimum Equipment List) sign-off already completed by maintenance before the flight",
        "TRE must both observe and simultaneously grade CRM and technical performance",
        "Limited real-time diagnostic data on an intermittent avionics advisory",
        "Passengers and revenue schedule create incentive to avoid unnecessary diversion or turnback"
      ],
      "stakeholders": [
        "Type Rating Examiner (TRE) / Check Airman",
        "Line Captain under evaluation",
        "First Officer (Pilot Monitoring)",
        "Maintenance Control",
        "Operations Control / Dispatch",
        "Fellow Check Airman (peer, post-flight)"
      ],
      "technical_terms_to_use": [
        "ADIRU", "advisory", "EICAS", "QRH", "MEL", "OPC", "Line Check",
        "CRM", "cross-check", "non-normal checklist", "tech log", "PF/PM",
        "V1", "memory items", "dispatch release"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias", "heuristic", "anchoring", "overconfidence",
        "blind spot", "normalcy bias", "illusion of validity", "expert intuition bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tech log shows one prior flight with an ADIRU 2 advisory that cleared during flight",
          "Maintenance inspected the unit, found no fault confirmed on ground test, but preemptively replaced a suspect connector as a precaution",
          "Aircraft is on schedule with a full passenger load"
        ],
        "new_information_after_decision": [
          "A different, milder advisory (a brief IRS align caution, not the same ADIRU miscompare) appears during climb in Phase 2"
        ],
        "alternatives": [
          "Accept the aircraft as dispatched, treating the preventive part replacement as adequate closure",
          "Request confirmation from maintenance control that the replaced connector was tested under load before departure"
        ],
        "intended_action": "TRE and captain discuss the tech log entry and the preventive part replacement, weigh both the maintenance action taken and the schedule pressure, and decide to accept dispatch, with the TRE noting both supporting and countervailing considerations aloud rather than settling the matter on a single rationale."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Brief IRS align caution appears on EICAS during climb through FL250 and clears within about ten seconds",
          "No non-normal checklist is triggered by the system",
          "TRE is aware the previous flight's ADIRU advisory was a different symptom, not identical to this one"
        ],
        "new_information_after_decision": [
          "In cruise, the captain later encounters a distinct, unrelated minor procedural choice point rather than a recurrence of the same advisory"
        ],
        "alternatives": [
          "Continue the climb, noting the advisory did not match the exact prior symptom and did not trigger a checklist",
          "Level off briefly to monitor additional parameters before continuing, given that any ADIRU-related caution carries some irreducible uncertainty"
        ],
        "intended_action": "TRE recommends continuing the climb while explicitly flagging to the captain that the current advisory is not the same as the previous flight's, and that the decision rests on the absence of a checklist trigger and on operational judgment under an uncertain, only partially analogous situation."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "In cruise, the captain skips a non-critical, time-consuming verification step in a minor non-normal checklist for an unrelated caution, citing that the item does not affect flight safety and can be completed later",
          "The captain explains the reasoning to the first officer, who agrees but notes it should be documented",
          "The item is completed later in cruise once workload decreases"
        ],
        "new_information_after_decision": [
          "The checklist item is completed without incident before descent, and no adverse effect is observed"
        ],
        "alternatives": [
          "Grade the deviation as an acceptable, explained prioritization decision consistent with published guidance on sequencing non-critical items",
          "Grade the deviation as a procedural nonconformance requiring debrief, regardless of the stated rationale or eventual completion"
        ],
        "intended_action": "TRE grades the captain's handling as satisfactory, citing both the captain's explicit verbal rationale to the crew and the checklist's own allowance for deferring non-critical items, while also noting in the report that a stricter reading of the manual could support a different grade."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Flight lands uneventfully; TRE begins writing the check report",
          "A fellow TRE, reviewing the report informally, asks whether the grading standard applied would have been the same for a different crew pairing",
          "TRE has handled similar deferred-item situations before, with mixed views on the correct standard"
        ],
        "new_information_after_decision": [
          "Maintenance later finds the replaced connector was seated correctly and cannot conclusively link it to either advisory, leaving the underlying cause only partially explained"
        ],
        "alternatives": [
          "Tell the peer that the same standard would likely apply regardless of crew pairing, while acknowledging the question is fair and worth documenting more explicitly next time",
          "Tell the peer that crew pairing probably does affect how such judgment calls get made, without specifying whether that is appropriate or not"
        ],
        "intended_action": "TRE responds to the peer's question with genuine uncertainty, acknowledging that he isn't fully sure whether his grading standard would transfer identically to a different crew, and proposes discussing it further at the next check-airman standardization meeting rather than resolving the question himself."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this flight was supposed to accomplish and your role in it?",
        "What was your initial impression of the aircraft and crew before departure?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you notice at each stage of the flight?",
        "What information did you have in front of you at each point, and where did it come from?",
        "What changed between what you expected and what actually occurred?"
      ],
      "decision_point_probes": [
        "What cues led you to accept/continue/grade the situation the way you did at this point?",
        "What information sources did you rely on, and were there others you could have consulted?",
        "What were you trying to achieve at that moment, and did that goal compete with anything else?",
        "What alternatives did you consider, and why did you weigh them the way you did?",
        "What was the basis for your decision — was there a single deciding factor or several?",
        "Had you seen something like this before, and how did that shape your response?",
        "How much time pressure did you feel, and did that affect how you gathered information?",
        "How confident were you in your read of the situation at the time, versus in hindsight?",
        "If the information had been slightly different, or if a different pilot had been flying, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If you had to do this flight again with the same information, what would you do differently, if anything?",
        "If a less experienced captain had made the same call in Phase 3, would you have graded it the same?",
        "How do you think other check airmen might have handled the same sequence of events?",
        "What would it take to convince you that one of your calls that day should have gone the other way?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "AV_Biased_4",
      "features_to_match": [
        "Domain (aviation), role (Check Airman/TRE), setting (Line Check/OPC on a senior widebody captain)",
        "Four-decision-point structure covering dispatch acceptance, in-flight advisory response, evaluative grading, and post-flight reflection",
        "Technical vocabulary set (ADIRU, EICAS, QRH, MEL, tech log, CRM, cross-check)",
        "Stakeholder roster (TRE, captain, first officer, maintenance control, ops control, peer TRE)",
        "Emotional tone (measured, professional, reflective) and difficulty level (challenging)",
        "Approximate word count and dialogue format"
      ],
      "features_to_remove_or_change": [
        "Remove the repeated identical self-clearing pattern used as a predictive basis (replaced with a non-identical, only partially analogous advisory)",
        "Remove the seniority-substitutes-for-verification grading rationale (replaced with a dual-rationale grading tied to explicit crew communication and published checklist allowance)",
        "Remove the categorical self-exemption from a peer's critique (replaced with genuine, unresolved uncertainty about whether the standard would transfer to a different crew)",
        "Remove the dispatch-history-as-proof-of-safety reasoning (replaced with an explicit acknowledgment of both supporting and countervailing considerations)"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined: the textual evidence must support at least two plausible readings (a defensible operational judgment and a less careful one) without the interview supplying a clear marker that tips the reasoning into any of the four target mechanisms. The TRE's language should include explicit hedges, acknowledgment of counterarguments, or open questions at each decision point, rather than a confident, single-basis justification of the kind used in the paired biased scenario."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable; no counterfactual condition requested for this generation.",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly 4 decision points present, matching the paired biased scenario's structure",
      "Each decision point offers at least two plausible alternatives with genuine ambiguity",
      "No decision point contains a confident, single-basis justification matching any of the four target bias mechanisms",
      "No bias labels, definitions, or psychological terminology appear in probes or narrative",
      "Consequences (successful landing, inconclusive maintenance finding) leave open multiple interpretations of each decision",
      "Target word count 1,215-1,485 words achievable given 4 timeline phases plus probe responses without repetitive exposition",
      "Zero intended instances of Bias Blind Spot, Normalcy Bias, Experience Bias or Trusting expert intuition, and Illusion of validity are embedded"
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
