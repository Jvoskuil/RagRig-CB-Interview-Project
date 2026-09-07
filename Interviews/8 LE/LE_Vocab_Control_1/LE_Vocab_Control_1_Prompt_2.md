You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Vocab_Control_1",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Patrol Officer (Field Response)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Late-Night Vehicle Check at the Closed Loading Dock",
    "scenario_summary_internal": "A patrol officer responds to a dispatch call about a parked vehicle idling near a closed distribution warehouse after hours. Over the course of the stop, the officer must decide how to approach, whether to conduct a pat-down, whether to detain, and how to resolve the encounter. The subject turns out to be a contracted maintenance technician waiting for a site manager to grant after-hours access. This is a vocabulary- and structure-matched control paired with LE_Biased_1: same domain, role, setting type, decision count, technical vocabulary, and emotional tone, but with zero intended cognitive-bias instances. All cue integration in the pat-down decision is written to reflect balanced, proportionate weighting of both present and absent cues, with no asymmetric treatment embedded.",
    "occupational_realism": {
      "objective": "Determine whether a person near a closed commercial facility after hours poses a safety or criminal risk, resolve the stop safely and lawfully, and decide on appropriate action (release, further investigation, or arrest).",
      "setting": "Suburban distribution warehouse loading dock, closed for the night, dim exterior lighting, single officer on patrol, backup several minutes out",
      "constraints": [
        "Officer is alone until backup arrives",
        "Limited lighting restricts visual assessment",
        "Dispatch information is secondhand and vague ('vehicle idling suspiciously')",
        "Department policy requires reasonable suspicion before a pat-down",
        "Time pressure: officer must decide quickly whether the situation is escalating"
      ],
      "stakeholders": [
        "Patrol officer",
        "Subject (contracted maintenance technician)",
        "Dispatch/911 caller (anonymous, not present)",
        "Backup officer (arrives later)",
        "Warehouse site manager (indirect, property concerns)"
      ],
      "technical_terms_to_use": [
        "reasonable suspicion",
        "Terry stop",
        "pat-down",
        "field interview",
        "officer safety",
        "totality of the circumstances"
      ],
      "technical_terms_to_avoid": [
        "feature positive effect",
        "cognitive bias",
        "salience bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch call: anonymous caller reported a vehicle 'idling suspiciously' near a closed warehouse loading dock",
          "No description of the vehicle, occupants, or specific behavior provided",
          "Time is 2:05 a.m., area has had recent cargo theft incidents"
        ],
        "new_information_after_decision": [
          "On arrival, officer sees one man standing beside a parked pickup truck near the loading dock, checking a clipboard"
        ],
        "alternatives": [
          "Approach directly and initiate contact immediately",
          "Observe from a distance first to assess behavior before approaching",
          "Call dispatch for more details before acting"
        ],
        "intended_action": "Officer parks at a distance and briefly observes before approaching on foot."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Subject is calm, makes eye contact, answers initial questions coherently",
          "Subject explains he is a contracted HVAC technician waiting for the site manager to grant after-hours access for a scheduled repair",
          "Officer notices a visible bulge in the subject's coat pocket",
          "Subject shows no shaking, no avoidance of eye contact, no attempt to move away, no change in breathing or speech pattern"
        ],
        "new_information_after_decision": [
          "Pat-down reveals the bulge is a folded work order and a multimeter, not a weapon"
        ],
        "alternatives": [
          "Ask the subject to voluntarily show pocket contents without a pat-down",
          "Conduct a pat-down after weighing both the pocket bulge and the subject's calm, cooperative demeanor together",
          "Continue the conversation and reassess after a few more questions"
        ],
        "intended_action": "Officer weighs the pocket bulge alongside the subject's calm, cooperative demeanor and consistent paperwork, and decides a brief pat-down is still warranted given the unidentified object, while explicitly noting the calm demeanor as a factor that tempers but does not eliminate the concern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pat-down is clean; no weapon or contraband found",
          "Subject's ID matches a valid driver's license and a contractor badge",
          "Backup officer has not yet arrived",
          "Subject's story about waiting for the site manager has not been independently confirmed"
        ],
        "new_information_after_decision": [
          "Dispatch confirms the HVAC contractor has an active work order with the warehouse for that night"
        ],
        "alternatives": [
          "Detain the subject further pending dispatch confirmation",
          "Release the subject pending a callback from dispatch",
          "Escort the subject to the site office to verify in person"
        ],
        "intended_action": "Officer requests dispatch confirmation while keeping the subject at the scene, without further escalation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch confirms the active work order and expected after-hours repair",
          "No further evidence of wrongdoing",
          "Site manager arrives moments later to grant access"
        ],
        "new_information_after_decision": [
          "Encounter concludes without arrest; officer files a field report noting the stop"
        ],
        "alternatives": [
          "Release the subject with no further action",
          "Issue a formal warning or citation for trespassing",
          "Request the subject leave the area immediately as a precaution"
        ],
        "intended_action": "Officer releases the subject and documents the stop as resolved."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew before you arrived on scene.",
        "What was your initial read of the situation when you pulled up?"
      ],
      "timeline_reconstruction": [
        "What did you notice first when you approached the subject?",
        "What happened between your initial observation and the pat-down decision?",
        "What did dispatch tell you, and when?"
      ],
      "decision_point_probes": [
        "What specifically made you decide to pat him down at that point?",
        "How did the calm demeanor and the pocket bulge factor together into that call?",
        "What made you decide to hold him at the scene rather than release him right away?",
        "What led you to close out the stop the way you did?"
      ],
      "information_sources": [
        "How much weight did you give the dispatch call versus what you observed yourself?",
        "Did the subject's explanation change how you viewed the bulge in his pocket?"
      ],
      "closing_hypotheticals": [
        "If the subject had been visibly nervous instead of calm, would that have changed your decision?",
        "If there had been no bulge but the same calm demeanor, would you still have patted him down?",
        "Looking back, is there anything you'd weigh differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "LE_Biased_1",
      "features_to_match": [
        "Domain vocabulary (reasonable suspicion, Terry stop, pat-down, field interview, officer safety, totality of the circumstances)",
        "Structure: four decision points in the same sequence (observe/approach, pat-down decision, continued-detention decision, release decision)",
        "Difficulty and subtlety of reasoning presented",
        "Actor roles: solo patrol officer, cooperative subject with a work-related explanation, anonymous caller, delayed backup, third-party corroborator",
        "Emotional tone: measured, procedural, mildly tense due to solitude and ambiguity",
        "Overall decision count and probe categories"
      ],
      "features_to_remove_or_change": [
        "Underlying incident specifics (warehouse loading dock instead of strip mall, HVAC technician instead of delivery driver)",
        "The asymmetric cue-weighting mechanism at the pat-down decision, replaced with explicit balanced consideration of both the pocket bulge and the calm demeanor",
        "Object found in pocket (work order and multimeter instead of invoice clipboard and charger)"
      ],
      "ambiguity_boundary": "Reasoning may remain genuinely uncertain (e.g., unconfirmed story, unidentified object) but must not include the intended asymmetric presence/absence cue-weighting pattern reserved for the biased condition."
    },
    "counterfactual_specification": {
      "causal_variable": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "counterfactual_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "NOT_APPLICABLE",
      "causal_test_question": "NOT_APPLICABLE"
    },
    "generation_checks": [
      "Zero Feature positive effect instances embedded; pat-down decision explicitly integrates both the bulge and the calm demeanor as joint, proportionate factors",
      "No bias terminology appears in probe_plan or timeline",
      "Four decision points present, each with at least two alternatives",
      "Word count target 1,350 (range 1,215-1,485) achievable given four decision points and probe set without repetitive exposition",
      "Vocabulary, structure, actor roles, and emotional tone matched to LE_Biased_1",
      "Underlying incident specifics changed sufficiently to avoid duplication while preserving parallel structure",
      "No unrequested bias intentionally embedded anywhere in timeline or probes"
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
