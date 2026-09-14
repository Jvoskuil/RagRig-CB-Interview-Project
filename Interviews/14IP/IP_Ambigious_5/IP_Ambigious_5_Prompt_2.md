You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Ambigious_5",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Plant/Industrial Production Manager",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "The Line 3 Flash Defect Spike Before the Meridian Shipment (Ambiguous Variant)",
    "scenario_summary_internal": "A plant manager at a mid-size injection molding facility must diagnose and correct a sudden rise in flash/short-shot defects on Line 3 in the four days before a large customer (Meridian Automotive) shipment deadline. The manager faces the same operational objective, constraints, stakeholders, and four decision points as the paired biased scenario (IP_Biased_5), but at each decision point the available evidence is genuinely incomplete or conflicting, so the manager's choices remain defensible under multiple reasonable interpretations. No decision is driven by a fixed prior anchor, vivid recall, social consensus, recency-weighting, or miscalibrated certainty; each choice reflects reasonable, resource-constrained judgment under authentic uncertainty.",
    "occupational_realism": {
      "objective": "Restore Line 3 output to spec-compliant quality (scrap rate back under 2%) in time to fulfill the Meridian shipment without triggering a full line shutdown or missing the ship date.",
      "setting": "A 24/7 mid-size automotive-parts injection molding plant running three shifts, with a quality lab, a maintenance/tooling team, and a corporate quality network linking four sister plants.",
      "constraints": [
        "72-hour window before the Meridian shipment must ship",
        "Limited access to the sister plant's full defect log, only a summary shared in a call",
        "Tooling change requires a scheduled press-down window shared with two other product runs",
        "Quality engineer is out sick during the second day, reducing statistical support",
        "Corporate directive discourages full-line shutdowns without VP sign-off"
      ],
      "stakeholders": [
        "Plant/Industrial Production Manager (interviewee)",
        "Shift supervisors (Shift A, B, C)",
        "Quality engineer",
        "Tooling/maintenance lead",
        "Sister-plant production manager (peer)",
        "Corporate quality director",
        "Meridian Automotive account representative"
      ],
      "technical_terms_to_use": [
        "flash defect",
        "short shot",
        "cycle time",
        "scrap rate",
        "mold cavity pressure",
        "resin lot",
        "tooling wear",
        "SPC chart",
        "press-down window",
        "hold pressure"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "anchoring",
        "availability heuristic",
        "bandwagon",
        "overconfidence",
        "recency effect",
        "heuristic",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Scrap rate on Line 3 jumped from 1.8% to 6.4% over the last 12-hour shift",
          "SPC chart shows a cavity-pressure drift starting mid-shift, but the drift magnitude is within a range that has previously been linked to both humidity and early-stage tooling wear",
          "A similar defect pattern six months earlier was traced to humidity, but that plant configuration has since changed (new dehumidifier installed), making direct comparison uncertain",
          "Tooling wear data has not yet been pulled and would take roughly the same time to retrieve as humidity logs"
        ],
        "new_information_after_decision": [
          "Humidity logs come back normal",
          "Tooling wear data, pulled shortly after, shows moderate wear accumulation"
        ],
        "alternatives": [
          "Check humidity/drying conditions first, given the historical precedent",
          "Check tooling wear first, given the equally plausible connection to pressure drift",
          "Request both checks be run in parallel using two available technicians"
        ],
        "intended_action": "Manager decides to run the humidity check and the tooling-wear pull in parallel using two available technicians, explicitly noting that either cause is plausible and that sequencing one before the other could not be justified from the data alone; both come back within a similar timeframe."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tooling wear confirmed as a contributing factor; wear severity readings are borderline between the plant's threshold for a minor hold-pressure adjustment and the threshold for a full insert swap",
          "Two candidate fixes exist: incremental hold-pressure adjustment (lower risk, slower to validate) or a full mold-insert swap (faster perceived fix, requires press-down window)",
          "The tooling lead and the shift supervisor disagree on whether the wear reading is closer to the adjustment threshold or the swap threshold",
          "The press-down window, if used now, will not be available again for five days"
        ],
        "new_information_after_decision": [
          "The insert swap is completed within the available press-down window",
          "Early results show partial improvement but scrap rate does not fully return to baseline, which is consistent with either an correctly-diagnosed-but-incomplete fix or a secondary contributing factor not yet identified"
        ],
        "alternatives": [
          "Choose the insert swap now, given the closing press-down window and borderline wear reading",
          "Choose the incremental hold-pressure adjustment and monitor over several cycles, accepting slower validation",
          "Request a second wear measurement to resolve the disagreement before deciding, at the cost of losing the press-down window"
        ],
        "intended_action": "Manager weighs the disagreement between the tooling lead and shift supervisor, notes that the window will close before a second measurement could realistically change the threshold classification, and selects the insert swap primarily citing the closing window and the borderline reading rather than a settled diagnosis."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A call with the sister-plant manager reveals that three of the four sister plants adopted a cooling-time reduction protocol, but two of those three plants run a different resin lot and slightly different cavity geometry than Line 3",
          "The plant's own quality engineer has partially validated the protocol against Line 3's resin lot but has not completed testing against the specific cavity geometry due to being out sick part of the day",
          "Corporate quality director notes the protocol is showing promising but not yet conclusive results network-wide"
        ],
        "new_information_after_decision": [
          "Applying the cooling-time reduction produces a short-term drop in flash defects",
          "A new, unrelated warping issue emerges on a subset of parts two shifts later, with cause not yet determined"
        ],
        "alternatives": [
          "Adopt the cooling-time reduction protocol based on the partial validation already completed",
          "Wait for the quality engineer to complete geometry-specific validation before adopting",
          "Adopt a modified, more conservative version of the protocol pending full validation"
        ],
        "intended_action": "Manager adopts the protocol after the partial validation, explicitly weighing the incomplete geometry testing against the shipment deadline, and acknowledges in the account that the decision could reasonably have gone either way given the partial data."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The most recent shift (last 8 hours) shows scrap rate down to 1.5%, the best reading in four days",
          "The full four-day trend, including the warping issue from phase 3, is more mixed and shows only 2.9% average improvement with unresolved variability",
          "Meridian shipment must be finalized within hours, and the corporate quality director is asking whether the fix should be rolled out to Lines 4 and 6",
          "Lines 4 and 6 have different tooling age profiles than Line 3, making direct extrapolation uncertain in either direction"
        ],
        "new_information_after_decision": [
          "Lines 4 and 6 initially show improvement, but one line later reports a new tooling alarm not previously seen",
          "A fuller week-long data review shows the underlying wear-related root cause was only partially addressed"
        ],
        "alternatives": [
          "Approve immediate rollout to Lines 4 and 6, citing the deadline and the latest positive shift",
          "Request one more full day of Line 3 data across all shifts before recommending rollout",
          "Approve a limited pilot rollout to one additional line with added monitoring"
        ],
        "intended_action": "Manager approves a limited pilot rollout to one line with added monitoring rather than a full rollout to both lines, explicitly stating that the mixed four-day trend and differing tooling profiles on Lines 4 and 6 made a full rollout premature, while also noting the deadline pressure made some rollout decision unavoidable."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first indicated something was wrong on Line 3?",
        "What was your primary objective when you were first notified?"
      ],
      "timeline_reconstruction": [
        "What happened right after you were told about the scrap rate spike?",
        "Walk me through the sequence of checks, calls, and decisions over the four days.",
        "What information came in after each major decision, and how did it change things?"
      ],
      "decision_point_probes": [
        "At that moment, what options did you consider, and why did you rule the others out?",
        "What evidence or past experience were you drawing on when you made that call?",
        "Who else was involved, and how much did their input shape your decision?",
        "Looking back, what information did you have available that you didn't use, or used less than others?",
        "What information would have changed your decision at that point?"
      ],
      "closing_hypotheticals": [
        "If the sister plants had not shared their protocol, would your approach have been different?",
        "If the last shift's numbers had looked worse instead of better, would you have made the same rollout call?",
        "What would you do differently if a similar defect spike happened again next quarter?",
        "How much uncertainty did you feel you were operating under at each stage, in hindsight?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "IP_Biased_5",
      "features_to_match": [
        "Same operational objective, setting, constraints, and stakeholders as IP_Biased_5",
        "Same four decision points in the same sequence and narrative role (diagnosis, fix selection, protocol adoption, rollout decision)",
        "Same technical vocabulary and level of domain detail",
        "Same overall difficulty, emotional tone, and time pressure",
        "Same probe structure and coverage (cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, hypotheticals)"
      ],
      "features_to_remove_or_change": [
        "Remove the fixed anchor to the six-month-old humidity case; introduce a changed plant configuration that makes the historical parallel genuinely uncertain",
        "Remove the vivid Line 5 insert-failure narrative as the stated justification; replace with a borderline, disputed wear-severity reading as the actual point of ambiguity",
        "Remove sister-plant adoption rate as the primary stated justification; replace with partial, resin-lot-specific validation as the actual basis, with acknowledged incomplete geometry testing",
        "Remove disproportionate weighting of the single best recent shift; replace with explicit acknowledgment of the mixed four-day trend shaping a more conservative pilot decision",
        "Remove stated high certainty of full resolution; replace with an explicit, reasoned hedge (partial pilot rather than full rollout) that reflects genuine uncertainty rather than overclaiming"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined by the evidence provided (borderline thresholds, disputed readings, partial validation, mixed trends) such that a reasonable manager could have chosen any of the listed alternatives, and the participant's own account should acknowledge the uncertainty rather than resolve it artificially. No decision may be resolved via a fixed prior anchor, vivid-memory justification, majority-adoption justification, single-data-point weighting, or unqualified certainty claims, since these would constitute unintended instances of the named target biases."
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
      "Verify zero intended bias instances of Bandwagon effect, Recency effect, Overconfidence Bias, Availability Heuristic, and Anchoring Bias are embedded anywhere in the narrative, probes, or hypotheticals.",
      "Verify each of the four decision points contains genuine ambiguity (borderline data, disputed readings, partial validation, or mixed trends) with at least two plausible alternatives.",
      "Verify no decision is resolved via a fixed prior anchor, vivid recollection, majority-adoption justification, single-data-point overweighting, or unqualified certainty, since these would constitute unrequested bias instances.",
      "Verify the scenario matches IP_Biased_5 in objective, setting, constraints, stakeholders, decision count, vocabulary, and difficulty.",
      "Verify no bias name, definition, or psychological label appears anywhere in the text.",
      "Verify consequences at each decision point remain consistent with reasonable judgment under uncertainty, not proof of a correct or incorrect bias-free process.",
      "Verify total narrative length target of 1,350 words (range 1,215-1,485) is achievable without repetitive exposition.",
      "Verify probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes, including at least one 'what information would have changed the decision' probe and one 'what if a key feature had been different' probe."
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
