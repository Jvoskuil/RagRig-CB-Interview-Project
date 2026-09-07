You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IA_Biased_1",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "All-Source Intelligence Analyst (Strategic)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Steady State: Reassessing a Long-Dormant Border Garrison",
    "scenario_summary_internal": "A senior strategic all-source analyst has monitored a foreign border garrison for three years under a standing assessment of 'low activity, defensive posture only.' New multi-INT indicators (satellite imagery showing engineering equipment, a signals intercept referencing 'phase two,' and a liaison report of unusual night convoys) begin arriving over a two-week period. The analyst must decide whether to escalate, reframe, or fold the new data into the existing steady-state narrative before a quarterly strategic warning board. The incident tests whether long-standing threat assessments are re-examined with appropriate rigor when disconfirming evidence begins to accumulate, or whether the existing 'nothing changes here' judgment is preserved through reduced vigilance and routinized handling of new inputs.",
    "occupational_realism": {
      "objective": "Determine whether the garrison's new activity indicators warrant an upgraded threat assessment and formal warning notification before the quarterly board, without triggering an unnecessary alert fatigue cycle.",
      "setting": "A strategic intelligence fusion cell supporting a regional command, three years into monitoring a border garrison previously assessed as low-threat and defensively postured.",
      "constraints": [
        "Quarterly warning board convenes in 10 days; assessment must be finalized 48 hours prior",
        "Collection assets are shared across higher-priority theaters, limiting tasking flexibility",
        "Analyst carries a portfolio of six other accounts alongside this one",
        "Liaison reporting from the partner service has a mixed reliability history",
        "Prior three annual assessments all concluded 'no material change'"
      ],
      "stakeholders": [
        "Strategic all-source analyst (interviewee)",
        "Branch chief responsible for the quarterly warning board briefing",
        "Imagery analyst providing the engineering-activity report",
        "SIGINT analyst flagging the 'phase two' intercept",
        "Partner-nation liaison officer reporting convoy activity",
        "Regional command watch officer"
      ],
      "technical_terms_to_use": [
        "steady-state assessment",
        "indications and warning (I&W)",
        "multi-INT fusion",
        "collection tasking",
        "confidence level",
        "warning board",
        "baseline deviation",
        "analytic line"
      ],
      "technical_terms_to_avoid": [
        "complacency bias",
        "cognitive bias",
        "anchoring",
        "status quo bias",
        "normalcy bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three consecutive annual assessments rated the garrison as low-activity, defensive-only",
          "New satellite imagery shows earth-moving equipment and new foundation work near a previously inactive motor pool",
          "No prior imagery anomalies had been reported in over 18 months"
        ],
        "new_information_after_decision": [
          "The imagery analyst's report is logged as a routine update rather than a baseline-deviation flag",
          "No follow-on collection is tasked against the site for another 10 days"
        ],
        "alternatives": [
          "Task immediate follow-on imagery collection to confirm whether construction indicates a capability change",
          "Log the report as a minor update consistent with the existing steady-state judgment and revisit at the next scheduled review",
          "Flag the discrepancy to the branch chief for an out-of-cycle discussion"
        ],
        "intended_action": "Analyst logs the new construction activity as a routine update within the existing steady-state file, citing three years of consistent low-activity assessments, and does not escalate or retask collection."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "SIGINT intercept references an unidentified 'phase two' in a garrison communications channel",
          "The garrison's communications patterns have otherwise matched historical baselines",
          "The SIGINT analyst requests analytic input on whether 'phase two' should be treated as a new indicator"
        ],
        "new_information_after_decision": [
          "The intercept is filed under the existing account without a new indicator code",
          "No cross-reference is made against the earlier imagery report from Phase 1"
        ],
        "alternatives": [
          "Cross-reference the intercept against the recent imagery findings to test for a converging pattern",
          "Request additional SIGINT collection to clarify the meaning of 'phase two'",
          "Treat the intercept as ambiguous background noise consistent with historical low-threat communications"
        ],
        "intended_action": "Analyst characterizes the intercept as ambiguous and non-actionable, consistent with the garrison's historical communications pattern, without cross-referencing it against the imagery indicator from Phase 1."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Partner-nation liaison reports unusual night convoy movements near the garrison over three consecutive nights",
          "Liaison service has a mixed reliability history, with roughly 60% of past reports corroborated",
          "The branch chief asks the analyst for a preliminary read ahead of the warning board"
        ],
        "new_information_after_decision": [
          "The convoy report is annotated as 'uncorroborated, consistent with liaison's historical noise level'",
          "The analyst does not request independent verification against available overhead assets"
        ],
        "alternatives": [
          "Request tasking of an independent collection asset to verify or refute the convoy reporting",
          "Weight the convoy report cautiously but flag it as a data point requiring resolution before the board",
          "Discount the report primarily on the basis of the liaison's historical reliability record"
        ],
        "intended_action": "Analyst discounts the convoy reporting largely on the liaison's historical reliability record, without independently verifying it, and does not integrate it with the imagery and SIGINT indicators already on file."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "All three indicators (construction, intercept, convoys) are now visible together in the case file for the first time as the analyst drafts the warning board summary",
          "The branch chief expects a recommendation: sustain the existing assessment or propose an upgrade",
          "Time remaining before the assessment is due: approximately 48 hours"
        ],
        "new_information_after_decision": [
          "The warning board accepts the sustained low-activity judgment with minor caveats noted for future monitoring",
          "Three weeks later, additional reporting suggests the garrison's posture may have changed, prompting a retrospective review of the quarterly assessment"
        ],
        "alternatives": [
          "Synthesize the three indicators as a potential converging pattern and recommend an upgraded confidence level or formal warning",
          "Sustain the existing steady-state judgment with a caveat noting the indicators for future monitoring",
          "Request a short extension to task confirmatory collection before finalizing the recommendation"
        ],
        "intended_action": "Analyst sustains the existing steady-state judgment for the warning board, treating each indicator individually as within historical noise levels rather than synthesizing them as a potential converging signal, citing the multi-year track record of stability as the primary basis for confidence."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how you first became involved in monitoring this garrison account?",
        "What was your understanding of the account's threat status going into this period?"
      ],
      "timeline_reconstruction": [
        "Walk me through, in order, how each new piece of reporting came in over the two-week period.",
        "At what point did you first see the imagery, the intercept, and the convoy reporting?",
        "How did each report get logged or routed once it arrived?"
      ],
      "decision_point_probes": [
        "What specific cues in the imagery report stood out to you, if any?",
        "What sources did you consult before deciding how to characterize the intercept?",
        "What alternatives did you consider for handling the convoy reporting?",
        "What was your main basis for the recommendation you brought to the warning board?",
        "How much time pressure did you feel at each of these points?",
        "How confident were you in each judgment at the time you made it?",
        "What prior experience with this account shaped how you interpreted the new reporting?"
      ],
      "closing_hypotheticals": [
        "If the imagery report had arrived without the account's three-year track record behind it, how might you have handled it differently?",
        "If you had unlimited collection assets, what would you have tasked differently across this period?",
        "Looking back, what would you tell a junior analyst about how to handle a long-running low-threat account when new indicators start to appear?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Complacency Bias",
        "decision_point": 4,
        "mechanism": "Analyst relies on the multi-year track record of a stable, low-threat judgment as the primary justification for sustaining the existing assessment, treating newly converging multi-INT indicators as individually explainable rather than triggering a full re-evaluation of vigilance or verification effort at the synthesis stage.",
        "affected_reasoning_operation": "Evidence synthesis and confidence calibration at the point of final judgment formation",
        "evidence_available_at_time": [
          "Imagery indicator of new construction from Phase 1",
          "SIGINT 'phase two' intercept from Phase 2",
          "Liaison convoy reporting from Phase 3",
          "Three years of prior steady-state assessments"
        ],
        "required_textual_manifestation": "In responding to the closing decision-point probe, the analyst should explicitly cite the account's long track record of stability as the reason for not escalating verification effort, while acknowledging the three indicators were seen together for the first time without prompting a corresponding increase in scrutiny.",
        "plausible_nonbias_interpretation": "The analyst could reasonably conclude that each indicator was individually weak and that base-rate stability legitimately supports a cautious, non-alarmist recommendation given resource constraints.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "complacency",
          "cognitive bias",
          "vigilance decrement",
          "reduced scrutiny due to routine"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario requested for this generation."
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
      "Confirm the interview contains exactly four decision points, each with at least two plausible alternatives.",
      "Confirm exactly one Complacency Bias instance is embedded, located at decision point 4, with no repetition or reinforcement of the same judgment elsewhere.",
      "Confirm decision points 1-3 contain plausible, non-bias-labeled analyst reasoning that sets up the evidentiary basis for the Phase 4 instance without themselves being scored as bias instances.",
      "Confirm no bias terminology, labels, or psychological explanations appear anywhere in the interview text.",
      "Confirm total word count falls between 1,215 and 1,485 words, targeting 1,350.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm the outcome (retrospective review three weeks later) does not mechanically confirm or deny whether the Phase 4 judgment was biased."
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
