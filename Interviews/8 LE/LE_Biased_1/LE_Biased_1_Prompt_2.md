You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Biased_1",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Patrol Officer (Field Response)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Late-Night Welfare Check at the Shuttered Strip Mall",
    "scenario_summary_internal": "A patrol officer responds to a dispatch call about a person loitering near a row of closed businesses after hours. Over the course of the stop, the officer must decide how to approach, whether to pat down, whether to detain, and how to resolve the encounter. The subject turns out to be a delivery driver waiting for a late shift-change contact. One subtle feature-positive-effect instance is embedded at the pat-down decision point: the officer weights the presence of a jacket-pocket bulge heavily toward 'weapon' while failing to give commensurate weight to the equally diagnostic absence of any nervous or evasive behavior, which would logically offset the suspicion if absence-of-cue were weighted the same as presence-of-cue.",
    "occupational_realism": {
      "objective": "Determine whether a person loitering near closed businesses after hours poses a safety or criminal risk, resolve the stop safely and lawfully, and decide on appropriate action (release, further investigation, or arrest).",
      "setting": "Suburban strip mall, closed for the night, dim parking lot lighting, single officer on patrol, backup 6 minutes out",
      "constraints": [
        "Officer is alone until backup arrives",
        "Poor lighting limits visual assessment",
        "Dispatch information is secondhand and vague ('subject acting suspicious')",
        "Department policy requires reasonable suspicion before a pat-down",
        "Time pressure: officer must decide quickly whether the situation is escalating"
      ],
      "stakeholders": [
        "Patrol officer",
        "Subject (delivery driver)",
        "Dispatch/911 caller (anonymous, not present)",
        "Backup officer (arrives late)",
        "Store owner association (indirect, property concerns)"
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
          "Dispatch call: anonymous caller reported a person 'loitering suspiciously' near closed stores",
          "No description of clothing, weapon, or specific behavior provided",
          "Time is 1:40 a.m., area has had recent break-ins"
        ],
        "new_information_after_decision": [
          "On arrival, officer sees one male standing near a parked car outside a closed electronics store, looking at his phone"
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
          "Subject explains he is a delivery driver waiting for a store employee to accept a late shipment",
          "Officer notices a visible bulge in the subject's jacket pocket",
          "Subject shows no shaking, no avoidance of eye contact, no attempt to move away, no change in breathing or speech pattern"
        ],
        "new_information_after_decision": [
          "Pat-down reveals the bulge is a rolled-up invoice clipboard and a phone charger, not a weapon"
        ],
        "alternatives": [
          "Conduct a pat-down based on the pocket bulge alone",
          "Ask the subject to voluntarily show pocket contents without a pat-down",
          "Continue the conversation and reassess after a few more questions"
        ],
        "intended_action": "Officer performs a pat-down, citing the pocket bulge as the primary basis for reasonable suspicion, without weighing the calm, non-evasive demeanor as an offsetting factor."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pat-down is clean; no weapon or contraband found",
          "Subject's ID matches a valid driver's license and a delivery company badge",
          "Backup officer has not yet arrived",
          "Subject's story about waiting for a store contact has not been independently confirmed"
        ],
        "new_information_after_decision": [
          "Dispatch confirms the delivery company has an active late-night account with the electronics store"
        ],
        "alternatives": [
          "Detain the subject further pending dispatch confirmation",
          "Release the subject pending a callback from dispatch",
          "Escort the subject to the store entrance to verify in person"
        ],
        "intended_action": "Officer requests dispatch confirmation while keeping the subject at the scene, without further escalation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch confirms the delivery account and expected late-night drop-off",
          "No further evidence of wrongdoing",
          "Store employee arrives moments later to accept the shipment"
        ],
        "new_information_after_decision": [
          "Encounter concludes without arrest; officer files a field report noting the stop"
        ],
        "alternatives": [
          "Release the subject with no further action",
          "Issue a formal warning or citation for loitering",
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
        "Were there any signs that suggested he wasn't a threat? How did those factor in?",
        "What made you decide to hold him at the scene rather than release him right away?",
        "What led you to close out the stop the way you did?"
      ],
      "information_sources": [
        "How much weight did you give the dispatch call versus what you observed yourself?",
        "Did the subject's explanation change how you viewed the bulge in his pocket?"
      ],
      "goals": [
        "What were you trying to accomplish at each stage of the stop?"
      ],
      "alternatives": [
        "What else could you have done instead of the pat-down?",
        "Could you have verified his story before conducting the pat-down?"
      ],
      "decision_basis": [
        "What single piece of information most drove your pat-down decision?"
      ],
      "prior_experience": [
        "Has a similar bulge or object turned out to be a weapon in past stops?"
      ],
      "time_pressure": [
        "How much did being alone, without backup, affect your pace of decisions?"
      ],
      "uncertainty": [
        "At what point were you most unsure about whether this was a real threat?"
      ],
      "closing_hypotheticals": [
        "If the subject had been visibly nervous instead of calm, would that have changed your decision?",
        "If there had been no bulge but the same calm demeanor, would you still have patted him down?",
        "Looking back, is there anything you'd weigh differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect",
        "decision_point": 2,
        "mechanism": "Officer's suspicion judgment is driven predominantly by the presence of a salient, discrete cue (visible pocket bulge) while the presence of an equally diagnostic countervailing cue (the absence of nervous, evasive, or agitated behavior) is not given proportional weight in the same judgment, even though a logically calibrated assessment would treat the absence of expected 'guilty' behavior as informative in the opposite direction.",
        "affected_reasoning_operation": "Weighting and integration of positive versus absent cues in a real-time risk assessment",
        "evidence_available_at_time": [
          "Visible bulge in jacket pocket",
          "Subject calm, coherent, cooperative, maintains eye contact",
          "No shaking, no avoidance, no change in breathing or speech",
          "Subject's coherent explanation for presence at the location"
        ],
        "required_textual_manifestation": "In describing the pat-down decision, the officer should explicitly cite the pocket bulge as the deciding factor ('that's what made me act') while, when probed about the calm demeanor, describing it as merely 'not really factoring in' or 'not something I weighed much,' revealing asymmetric weighting between the presence cue and the absence cue.",
        "plausible_nonbias_interpretation": "An unseen object in a pocket is an objectively higher officer-safety risk than calm demeanor is a safety reassurance, so weighting the bulge more heavily could reflect a justified officer-safety heuristic rather than a bias.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Do not name 'feature positive effect' or any bias term",
          "Do not have the officer explicitly reason about 'presence versus absence' in abstract terms",
          "Do not have the officer state the demeanor was irrelevant in a way that reads as a deliberate policy statement rather than a natural recollection"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": "presence_vs_absence_weighting_of_pocket_bulge_cue",
      "original_state": "Officer treats the visible pocket bulge as the dominant, near-sufficient basis for the pat-down decision.",
      "counterfactual_state": "Officer weighs the absence of nervous/evasive behavior as equally informative, integrating both presence and absence cues before deciding on the pat-down.",
      "variables_to_hold_constant": [
        "Time of night and lighting conditions",
        "Dispatch call content and vagueness",
        "Subject's actual identity, behavior, and explanation",
        "Absence of backup during the initial stop",
        "Outcome that the bulge is not a weapon"
      ],
      "expected_causal_difference": "If cues were weighted symmetrically, the officer would more likely delay or forgo the pat-down pending further verification, since the calm demeanor would offset the ambiguous bulge.",
      "causal_test_question": "Would the officer have proceeded to a pat-down at that exact moment if the calm demeanor had been given equal evidentiary weight to the pocket bulge?"
    },
    "generation_checks": [
      "Exactly one Feature positive effect instance planned, assigned to decision point 2 only",
      "No bias terminology appears in probe_plan or timeline",
      "Four decision points present, each with at least two alternatives",
      "Word count target 1,350 (range 1,215-1,485) achievable given four decision points and probe set without repetitive exposition",
      "Consequences (clean pat-down, confirmed delivery account) do not mechanically prove or disprove bias presence",
      "No unrequested bias intentionally embedded elsewhere in timeline or probes"
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
