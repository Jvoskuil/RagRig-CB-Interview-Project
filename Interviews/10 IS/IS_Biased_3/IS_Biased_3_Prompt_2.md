You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IS_Biased_3",
  "domain_id": "IS",
  "domain": "Information Systems, Human-Computer Interaction, and Interaction Design",
  "role": "UX Researcher",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Smart Suggestions Mandate: A Contested Usability Study",
    "scenario_summary_internal": "A UX Researcher at a mid-size software company is asked to validate a 'Smart Suggestions' recommendation feature that leadership has already decided to ship, ostensibly to gather supporting evidence rather than to test feasibility. The researcher must scope a mixed-methods study (moderated sessions, screener, diary study), design a discussion guide under influence from a product manager's framing example, synthesize pilot data that partially contradicts an earlier informal endorsement, and finally decide what to recommend to a steering committee. The narrative traces four sequential decisions from kickoff to final readout, embedding one instance each of reactance, priming effect, and cognitive dissonance without naming or explaining them.",
    "occupational_realism": {
      "objective": "Determine whether the mandated 'Smart Suggestions' feature is usable and beneficial enough to justify its planned rollout scope, and produce an evidence-based recommendation for the steering committee.",
      "setting": "Enterprise software company, UX research team embedded in a product organization, six-week research sprint ahead of a quarterly release train.",
      "constraints": [
        "Leadership has already approved the feature for release; the study's stated purpose is to inform rollout configuration, not go/no-go.",
        "Limited recruiting budget allows only 10 moderated sessions plus a small unmoderated diary cohort.",
        "Three-week timeline before the steering committee readout.",
        "Product manager wants findings to support a specific interaction pattern already prototyped.",
        "Researcher gave an informal positive update to the steering committee after an earlier exploratory session."
      ],
      "stakeholders": [
        "UX Researcher (participant of the interview)",
        "Product Manager for Smart Suggestions",
        "Engineering lead",
        "VP of Product (mandate source)",
        "Research operations coordinator",
        "Pilot cohort end users"
      ],
      "technical_terms_to_use": [
        "discussion guide",
        "screener",
        "moderated session",
        "unmoderated diary study",
        "think-aloud protocol",
        "affinity mapping",
        "thematic synthesis",
        "pilot cohort",
        "north-star metric",
        "steering committee readout",
        "rollout configuration",
        "usability heuristic"
      ],
      "technical_terms_to_avoid": [
        "reactance",
        "priming",
        "priming effect",
        "cognitive dissonance",
        "confirmation bias",
        "anchoring",
        "psychological bias",
        "cognitive bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "VP frames the Smart Suggestions feature as 'happening regardless' and says the study should 'make sure we ship it right.'",
          "Original research plan called for a lightweight 5-session moderated study.",
          "Researcher has prior data suggesting mixed reactions to similar recommendation UI patterns in another product line."
        ],
        "new_information_after_decision": [
          "Research ops flags that the expanded scope (moderated sessions plus a diary study) will consume most of the remaining budget.",
          "Engineering lead notes the extra diary study will delay the readout by one week."
        ],
        "alternatives": [
          "Keep the original lightweight 5-session moderated plan focused on usability of the current prototype.",
          "Expand scope to add an unmoderated diary study explicitly aimed at surfacing friction and negative reactions.",
          "Propose a short pause to renegotiate the study's purpose with the VP before proceeding."
        ],
        "intended_action": "Researcher expands the study scope to add the diary study, framing it internally as 'being thorough' in response to being told the outcome was predetermined."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Product manager shares a transcript excerpt from an earlier internal demo where a stakeholder reacted enthusiastically ('this feels like it reads my mind') and asks the researcher to 'make sure the guide can capture moments like this.'",
          "Draft discussion guide has neutral, open-ended prompts about task completion and satisfaction.",
          "Screener criteria are still being finalized."
        ],
        "new_information_after_decision": [
          "Two pilot participants use language nearly identical to the shared transcript when describing the feature.",
          "Research ops coordinator notes the guide's later probes lean toward eliciting delight-oriented language rather than friction."
        ],
        "alternatives": [
          "Finalize the discussion guide using only the original neutral, task-based prompts.",
          "Revise several probes to explicitly invite comparisons to the shared 'mind-reading' example.",
          "Ask the product manager not to share example reactions until after guide finalization."
        ],
        "intended_action": "Researcher revises specific probes to more closely echo the language and framing of the shared example transcript before finalizing the guide."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Researcher gave an informal update to the steering committee two weeks earlier stating early signs 'looked promising.'",
          "Pilot data now includes four sessions with clear frustration around unwanted suggestions interrupting workflow, alongside three sessions with positive reactions.",
          "Diary study entries show a recurring complaint about suggestion timing."
        ],
        "new_information_after_decision": [
          "Affinity mapping session with a second researcher flags that the frustration theme is being coded separately from the positive theme rather than merged into a single 'mixed reception' finding.",
          "Engineering lead asks whether the timing complaints are severe enough to change the rollout configuration."
        ],
        "alternatives": [
          "Code the frustration and positive reactions as a single, integrated 'mixed reception' theme reflecting the full pilot cohort.",
          "Treat the frustration sessions as isolated edge cases tied to atypical user workflows, preserving the earlier promising narrative.",
          "Pause synthesis and request additional pilot sessions to clarify the split before drawing conclusions."
        ],
        "intended_action": "Researcher characterizes the frustration sessions as edge cases attributable to unusual workflows, preserving consistency with the earlier informal 'promising' update to the steering committee."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Synthesis document frames the feature as largely positive with a small, edge-case caveat about suggestion timing.",
          "Steering committee readout is scheduled in two days.",
          "Engineering lead has asked for a clear recommendation: ship as-is, ship with timing adjustments, or delay for redesign."
        ],
        "new_information_after_decision": [
          "Steering committee approves shipping with a minor timing adjustment and asks for a follow-up study after launch.",
          "VP thanks the researcher for 'confirming the direction was right all along.'"
        ],
        "alternatives": [
          "Recommend shipping as-is with no configuration changes.",
          "Recommend shipping with a specific timing adjustment addressing the friction theme.",
          "Recommend a short delay to redesign the suggestion-timing logic before any rollout."
        ],
        "intended_action": "Researcher recommends shipping with a minor timing adjustment, consistent with the synthesis framing established in phase 3."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this research project came about?",
        "What was your understanding of the study's purpose when it was first assigned to you?"
      ],
      "timeline_reconstruction": [
        "What happened right after the VP described the feature as already decided?",
        "Walk me through how the discussion guide came together before the pilot sessions.",
        "What did the pilot data look like once sessions started coming in?",
        "How did you move from the synthesized findings to the final recommendation?"
      ],
      "decision_point_probes": [
        "What information did you have at the moment you decided to expand the study scope?",
        "What alternatives did you consider besides adding the diary study?",
        "When the product manager shared that transcript, how did it affect how you finalized the guide?",
        "What made you decide to revise those specific probes rather than leave the original wording?",
        "When you saw the frustration sessions, what made you categorize them the way you did?",
        "How did your earlier update to the steering committee factor into how you framed the findings?",
        "What ultimately tipped your final recommendation toward a timing adjustment rather than shipping as-is or delaying?"
      ],
      "cues": [
        "What specific words or reactions from participants or stakeholders stood out to you at each stage?"
      ],
      "information_sources": [
        "Which sources of information did you rely on most heavily at each decision point, and which did you set aside?"
      ],
      "goals": [
        "At each stage, whose goals were you trying to satisfy, and did that shift over time?"
      ],
      "alternatives": [
        "Looking back, what other paths could you have taken at each decision point?"
      ],
      "decision_basis": [
        "What ultimately justified each choice you made, in your own words?"
      ],
      "prior_experience": [
        "Did anything from past projects shape how you approached this one?"
      ],
      "time_pressure": [
        "How much did the timeline affect your choices at each stage?"
      ],
      "uncertainty": [
        "Where did you feel least certain about what the data was telling you?"
      ],
      "closing_hypotheticals": [
        "If the VP had never framed the feature as already decided, do you think your study scope would have looked different?",
        "If the product manager hadn't shared that transcript before the guide was finalized, would your probes have been worded differently?",
        "If you hadn't given that earlier 'promising' update to the steering committee, do you think you'd have coded the frustration sessions the same way?",
        "Looking back, is there anything about your final recommendation you'd reconsider?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Reactance",
        "decision_point": 1,
        "mechanism": "Being told the outcome (ship the feature) was non-negotiable triggers an assertive counter-response: the researcher unilaterally expands scope beyond what the research question requires, partly to reassert professional autonomy against the perceived restriction on the study's purpose.",
        "affected_reasoning_operation": "Scope-setting decision under a perceived constraint on research freedom",
        "evidence_available_at_time": [
          "VP's framing that the feature is 'happening regardless'",
          "Original lightweight 5-session plan already fit the research question",
          "Budget and timeline constraints flagged by research ops"
        ],
        "required_textual_manifestation": "Researcher explicitly links the scope expansion to the feeling of being told what the outcome should be, using language like 'wanted to make sure we weren't just rubber-stamping it' before naming budget/timeline tradeoffs.",
        "plausible_nonbias_interpretation": "A diary study is a legitimate methodological addition to capture longitudinal friction that moderated sessions alone might miss.",
        "strength": "subtle",
        "do_not_make_explicit": ["reactance", "psychological reactance", "asserting autonomy", "resisting mandate"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Priming effect",
        "decision_point": 2,
        "mechanism": "Exposure to the product manager's enthusiastic example transcript, presented immediately before guide finalization, shapes the wording and emphasis of subsequent probes toward eliciting similar delight-oriented language, independent of the guide's original neutral design intent.",
        "affected_reasoning_operation": "Instrument design / probe wording selection",
        "evidence_available_at_time": [
          "Shared transcript excerpt with specific 'mind-reading' phrasing",
          "Original neutral, task-based draft guide",
          "Research ops note about guide balance before finalization"
        ],
        "required_textual_manifestation": "Researcher describes revising 'a couple of probes' to more closely mirror the shared example's phrasing, and later notes participants used near-identical language, without recognizing the guide itself invited that language.",
        "plausible_nonbias_interpretation": "Incorporating a concrete example of positive engagement is a reasonable way to sharpen vague probes and ensure the guide can capture strong reactions if they occur.",
        "strength": "subtle",
        "do_not_make_explicit": ["priming", "priming effect", "anchoring on example", "unconscious influence"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Cognitive Dissonance",
        "decision_point": 3,
        "mechanism": "Having earlier publicly stated to the steering committee that results 'looked promising,' the researcher encounters contradicting frustration data and resolves the inconsistency by reinterpreting the negative sessions as atypical edge cases rather than integrating them into the overall finding, preserving consistency with the prior public commitment.",
        "affected_reasoning_operation": "Data synthesis and thematic categorization",
        "evidence_available_at_time": [
          "Four sessions showing clear frustration with suggestion timing",
          "Three sessions showing positive reactions",
          "Diary study entries repeating the timing complaint",
          "Researcher's own prior informal 'promising' statement to the steering committee"
        ],
        "required_textual_manifestation": "Researcher justifies separating frustration sessions as 'atypical workflows' specifically by referencing the need for the findings to line up with what was already told to the steering committee, rather than purely on data grounds.",
        "plausible_nonbias_interpretation": "Some usability studies do find that friction clusters around specific workflow types, making an edge-case categorization a legitimate analytical choice.",
        "strength": "subtle",
        "do_not_make_explicit": ["cognitive dissonance", "reducing dissonance", "rationalization", "consistency motive"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', not a control condition."
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
      "Exactly four decision points are present, each with at least two alternatives, prior facts, and post-decision information.",
      "Exactly one instance each of Reactance, Priming effect, and Cognitive Dissonance is embedded, at decision points 1, 2, and 3 respectively.",
      "Decision point 4 contains no new intended bias instance; it reflects downstream consequences only.",
      "No bias names, definitions, or explanations appear in probe wording or intended interview content.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and closing hypotheticals.",
      "Each occurrence has a distinct evidence trace, decision point, and plausible non-bias interpretation, satisfying the instance independence rule.",
      "Target length of 1,350 words (range 1,215-1,485) is achievable given four decision points with moderate probe depth and no repetitive exposition."
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
