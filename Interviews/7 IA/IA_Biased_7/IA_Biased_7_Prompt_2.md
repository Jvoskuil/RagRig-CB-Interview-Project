You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IA_Biased_7",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Human Intelligence (HUMINT) Collection Manager/Reports Officer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Walk-In and the Deadline: Procurement Network Reporting Under Pressure",
    "scenario_summary_internal": "A HUMINT Collection Manager/Reports Officer at a forward station receives an unvetted walk-in source claiming knowledge of an imminent illicit dual-use technology shipment tied to a procurement network the station has tracked for months. With a senior-level policy briefing due within 36 hours, the officer must triage the source, reconcile the claim against existing multi-source reporting, draft a time-sensitive product, and respond to a senior officer's push to disseminate before all discrepancies are resolved.",
    "occupational_realism": {
      "objective": "Determine whether the walk-in's claim about an imminent shipment is credible enough to redirect collection resources and to include in a policy-relevant intelligence product before a fixed briefing deadline.",
      "setting": "A regional HUMINT station supporting a task force on dual-use technology proliferation, operating under normal reporting cadence but facing an unscheduled walk-in contact and an externally fixed briefing deadline.",
      "constraints": [
        "36-hour window before a senior policymaker briefing",
        "Limited independent means to vet the walk-in source's access and motivation in the time available",
        "Competing tasking requirements on the same technical collection assets",
        "Partial, sometimes contradictory reporting streams (existing HUMINT network, technical collection, open-source)",
        "Pressure from a senior officer to produce an actionable product quickly"
      ],
      "stakeholders": [
        "The reports officer/collection manager (interviewee)",
        "The walk-in source",
        "An established sub-source network being run for months on the same target",
        "A senior reports officer/branch chief pushing for rapid dissemination",
        "Technical collection analysts providing a partially contradictory data stream",
        "The policy audience awaiting the briefing"
      ],
      "technical_terms_to_use": [
        "walk-in",
        "source validation",
        "collection tasking",
        "corroboration",
        "access and placement",
        "product turnaround",
        "confidence level",
        "dissemination",
        "sub-source",
        "reporting stream"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "cognitive bias",
        "heuristic",
        "anchoring",
        "framing effect",
        "authority bias",
        "wishful thinking",
        "belief bias",
        "selective attention",
        "planning fallacy"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Walk-in arrives unannounced claiming direct knowledge of an imminent shipment",
          "Walk-in presents a handwritten manifest fragment and a photo of a shipping container",
          "No independent vetting of the walk-in's stated access has yet occurred",
          "The station has spent months building a hypothesis about this same procurement network"
        ],
        "new_information_after_decision": [
          "Initial debrief notes are drafted describing the walk-in as consistent with the existing network hypothesis",
          "A request is submitted to expedite validation of the walk-in's documents"
        ],
        "alternatives": [
          "Treat the walk-in as an unvetted, uncorroborated contact requiring full standard validation before any tasking action",
          "Treat the material as strongly consistent with the prior network hypothesis and move directly to tasking",
          "Defer any assessment for 24 hours pending basic document authentication"
        ],
        "intended_action": "Officer interprets the ambiguous handwriting and container photo as clearly matching the network's known shipping pattern, and separately reflects that the timing is 'a stroke of luck' because it would validate months of otherwise inconclusive effort."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Existing sub-source reporting from the tracked network is ambiguous about shipment timing",
          "Technical collection has flagged activity at a different port than the one named by the walk-in",
          "The walk-in claims a prior logistics role that would explain access, but this claim is unverified",
          "A colleague raises the technical-collection discrepancy in a coordination call"
        ],
        "new_information_after_decision": [
          "The report draft cites the walk-in and sub-source material prominently; the technical-collection discrepancy is mentioned only in a footnote",
          "The colleague's concern is logged but not incorporated into the main assessment"
        ],
        "alternatives": [
          "Weigh the technical-collection discrepancy and the walk-in's account with comparable rigor before drafting",
          "Give primary weight to the reporting that matches the established network hypothesis and treat the discrepancy as secondary",
          "Pause the draft until the port discrepancy is reconciled"
        ],
        "intended_action": "Officer reasons that because the walk-in's claimed logistics background makes the story 'the kind of thing a real insider would know,' the account must be substantially true, and continues to emphasize corroborating threads while the contradicting technical-collection item receives minimal analytic attention."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Briefing deadline is 14 hours away",
          "The estimate of shipment timing carries meaningful residual uncertainty",
          "Two ways exist to describe the same confidence level to the policy audience",
          "Historical timelines for similar validation-and-tasking sequences typically take longer than initially planned"
        ],
        "new_information_after_decision": [
          "The draft language is finalized using an urgency-emphasizing framing of the uncertain timeline",
          "A follow-on tasking and source-meeting schedule is set assuming compressed timeframes"
        ],
        "alternatives": [
          "Present the uncertainty in terms of what is not yet known and what could invalidate the assessment",
          "Present the same uncertainty by emphasizing the probability that the network will act imminently",
          "Build follow-on tasking timelines around historical validation durations rather than the shortest plausible case"
        ],
        "intended_action": "Officer chooses wording that foregrounds the chance of imminent action rather than the chance of no action, and separately schedules follow-on source meetings and validation steps on a compressed timeline that assumes best-case availability of interpreters, safehouses, and sub-source cooperation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The branch chief reviews the draft and states a preference to disseminate immediately given the deadline",
          "Unresolved discrepancies between the walk-in account and technical collection remain",
          "The officer has previously seen the branch chief's calls prove correct in ambiguous situations",
          "Standard practice allows officers to request additional caveat language or a short delay"
        ],
        "new_information_after_decision": [
          "The product is disseminated substantially as the branch chief directed, with limited additional caveat language",
          "Post-dissemination feedback later notes that the shipment timing in the product did not match subsequent observed activity"
        ],
        "alternatives": [
          "Request an additional short delay or stronger caveat language before dissemination, independent of the branch chief's preference",
          "Defer to the branch chief's judgment on timing and caveat strength without independently re-examining the unresolved discrepancy",
          "Escalate the unresolved discrepancy to a separate technical-collection reviewer before finalizing"
        ],
        "intended_action": "Officer defers to the branch chief's stated preference for immediate dissemination with minimal caveats, treating the chief's seniority and past track record as sufficient reason not to press the unresolved technical-collection discrepancy further."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this incident began and what your role was?",
        "What was your primary objective when the walk-in first made contact?"
      ],
      "timeline_reconstruction": [
        "What happened right after the walk-in presented the documents?",
        "How did the coordination call with your colleague unfold?",
        "What did you do between receiving the technical-collection flag and finalizing the draft?",
        "Walk me through the final hours before dissemination."
      ],
      "decision_point_probes": [
        "What specific cues in the documents led you to your initial read of the walk-in's credibility?",
        "What information sources did you weigh most heavily when drafting the assessment, and why?",
        "What alternatives did you consider for describing the uncertainty in the report?",
        "What was your basis for setting the follow-on meeting and validation timeline?",
        "How much time pressure did you feel at each stage, and how did that affect what you focused on?",
        "What was your prior experience with similar walk-ins or with this network telling you?",
        "How did you factor in the branch chief's preference versus your own independent read of the discrepancy?"
      ],
      "closing_hypotheticals": [
        "If the technical-collection discrepancy had been flagged earlier, do you think your draft would have looked different?",
        "If the branch chief had not expressed a preference, would you have handled the caveat language differently?",
        "Looking back, is there a point where you'd have wanted more time regardless of the deadline?",
        "If this walk-in situation happened again, what would you want to have available before the first assessment?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Perceptual Bias",
        "decision_point": 1,
        "mechanism": "Officer perceives ambiguous physical evidence (handwriting fragment, container photo) as clearly matching a pre-existing mental template of the network's shipping pattern, when the evidence is genuinely ambiguous.",
        "affected_reasoning_operation": "Interpretation of raw sensory/documentary evidence",
        "evidence_available_at_time": ["Handwritten manifest fragment", "Photo of a shipping container", "Months-old network hypothesis"],
        "required_textual_manifestation": "Officer describes the manifest and photo as 'clearly' or 'obviously' matching the known pattern despite the material being generic or degraded enough to admit other readings.",
        "plausible_nonbias_interpretation": "The officer has genuine domain expertise recognizing a real pattern match.",
        "strength": "moderate",
        "do_not_make_explicit": ["perceptual bias", "pattern recognition error", "cognitive bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Wishful Thinking",
        "decision_point": 1,
        "mechanism": "Officer's desire for the walk-in to be genuine, because it would validate months of otherwise inconclusive collection effort, inflates the officer's confidence in the source's veracity beyond what the initial evidence supports.",
        "affected_reasoning_operation": "Confidence estimation about source veracity",
        "evidence_available_at_time": ["No independent vetting yet completed", "Months of inconclusive prior effort on the same target"],
        "required_textual_manifestation": "Officer explicitly links personal relief or hope ('finally,' 'a stroke of luck') to an unearned boost in confidence about the walk-in, distinct from the perceptual read of the documents.",
        "plausible_nonbias_interpretation": "The officer is simply expressing normal professional satisfaction without altering the actual assessment.",
        "strength": "moderate",
        "do_not_make_explicit": ["wishful thinking", "desirability bias", "motivated reasoning"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Belief bias",
        "decision_point": 2,
        "mechanism": "Officer judges the logical soundness of the walk-in's explanatory account (claimed logistics access explaining knowledge) based on whether the conclusion is one the officer already believes, rather than on the actual validity of the inference chain.",
        "affected_reasoning_operation": "Evaluation of an explanatory argument's logical validity",
        "evidence_available_at_time": ["Walk-in's unverified claim of a prior logistics role", "General plausibility of such a role explaining access"],
        "required_textual_manifestation": "Officer states or implies that because the conclusion (source is credible) fits what was already believed about the network, the argument for access must be sound, without separately testing the argument's logical structure.",
        "plausible_nonbias_interpretation": "The officer is using reasonable professional judgment about plausible cover stories.",
        "strength": "subtle",
        "do_not_make_explicit": ["belief bias", "syllogistic reasoning error"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias",
        "decision_point": 2,
        "mechanism": "During multi-source review, the officer disproportionately attends to and elaborates on evidence corroborating the network hypothesis while relegating a genuinely contradicting technical-collection item to minimal treatment.",
        "affected_reasoning_operation": "Evidence weighting and selection during report drafting",
        "evidence_available_at_time": ["Corroborating sub-source reporting", "Technical-collection flag naming a different port", "Colleague's verbal concern in coordination call"],
        "required_textual_manifestation": "Officer describes giving the corroborating material prominent treatment in the draft and the contradicting technical item only a footnote or passing mention, without a stated evidentiary reason for the disparity.",
        "plausible_nonbias_interpretation": "The corroborating reporting may genuinely be higher quality or more current than the technical flag.",
        "strength": "moderate",
        "do_not_make_explicit": ["selective attention", "biased evidence weighting", "confirmation"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Framing effects",
        "decision_point": 3,
        "mechanism": "Officer chooses to phrase an uncertain probability estimate in terms emphasizing the likelihood of imminent action rather than the mathematically equivalent likelihood of no action, shifting the perceived urgency of the same underlying uncertainty.",
        "affected_reasoning_operation": "Presentation/communication of a probabilistic judgment",
        "evidence_available_at_time": ["Genuinely uncertain shipment timing estimate", "Two equivalent ways to phrase the same probability"],
        "required_textual_manifestation": "Officer explicitly recalls choosing wording that stresses the chance the network 'will act imminently' over wording stressing the chance it 'will not act soon,' for the same underlying estimate.",
        "plausible_nonbias_interpretation": "Policy audiences conventionally prefer action-oriented framing regardless of underlying probability.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "loss/gain framing"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Planning fallacy",
        "decision_point": 3,
        "mechanism": "Officer sets follow-on validation and source-meeting timelines based on a best-case scenario, ignoring the station's own historical pattern in which similar validation sequences have taken longer.",
        "affected_reasoning_operation": "Prediction of task duration for follow-on tasking",
        "evidence_available_at_time": ["Historical precedent that similar validation sequences run longer than planned", "Immediate deadline pressure"],
        "required_textual_manifestation": "Officer describes scheduling follow-on meetings and validation steps assuming interpreters, safehouses, and sub-source cooperation will all be available on the shortest plausible timeline, without adjusting for known historical delays.",
        "plausible_nonbias_interpretation": "The compressed timeline may be a deliberate stretch target rather than a genuine duration estimate.",
        "strength": "moderate",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "underestimation"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Authority Bias or Authority Obedience",
        "decision_point": 4,
        "mechanism": "Officer defers to the branch chief's stated preference for immediate dissemination with minimal caveats primarily because of the chief's seniority and past track record, rather than independently re-weighing the unresolved technical-collection discrepancy.",
        "affected_reasoning_operation": "Final decision on caveat strength and dissemination timing",
        "evidence_available_at_time": ["Branch chief's explicit preference for immediate dissemination", "Unresolved discrepancy from decision point 2", "Standing option to request delay or stronger caveats"],
        "required_textual_manifestation": "Officer states that the chief's seniority or past record of being right was the deciding factor for not pressing the discrepancy further, distinct from an independent evaluation of the evidence.",
        "plausible_nonbias_interpretation": "Organizational hierarchy reasonably assigns final call authority to the branch chief regardless of the officer's personal view.",
        "strength": "moderate",
        "do_not_make_explicit": ["authority bias", "obedience", "deference"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no control pairing requested."
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
      "Confirm exactly 4 decision points are present and numbered 1-4.",
      "Confirm each of the 7 named biases appears exactly once, tied to the specified decision point and instance ID.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm each instance has a plausible non-bias explanation available in context.",
      "Confirm decision points 1, 2, and 3 each carry two distinct instances that use different evidence sources or reasoning operations, per the co-location rule.",
      "Confirm final word count falls between 1,215 and 1,485 words, target 1,350.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm consequences described (e.g., mismatched shipment timing) do not mechanically prove bias presence."
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
