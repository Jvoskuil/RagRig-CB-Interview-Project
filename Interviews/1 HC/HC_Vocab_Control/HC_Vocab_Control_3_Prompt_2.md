You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HC_Vocab_Control_3",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Emergency Medicine Attending Physician (community hospital, ~8 years post-residency experience)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Overnight Chest Pain Disposition (Vocabulary-Matched Control)",
    "scenario_summary_internal": "An ED attending physician manages a 52-year-old patient with pleuritic chest pain during a boarded, high-volume evening shift, mirroring the vocabulary, actors, constraints, and decision structure of the paired biased scenario. In this version, the attending integrates the flight/calf-ache cue into a broadened differential rather than closing on musculoskeletal strain alone, reassesses risk formally before ordering imaging, evaluates a colleague's earlier decision by the information that colleague actually had, and reaches a genuinely uncertain final disposition. No intended bias instances are embedded.",
    "occupational_realism": {
      "objective": "Correctly diagnose and safely disposition a patient with atypical chest pain while managing ED overcrowding and competing patient demands during a single evening shift.",
      "setting": "Emergency department of a mid-sized community hospital; evening shift with boarding patients, one CT scanner shared across the department, a covering resident, and a charge nurse coordinating flow.",
      "constraints": [
        "ED is at capacity with admitted patients boarding in hallway beds",
        "Single CT scanner shared with trauma and stroke protocols",
        "Attending is covering two acute patients simultaneously",
        "Family at bedside pressing for a rapid answer",
        "End-of-shift handoff deadline in two hours"
      ],
      "stakeholders": [
        "52-year-old patient with pleuritic chest pain",
        "Emergency medicine attending physician (interviewee)",
        "Second-year emergency medicine resident",
        "Charge nurse",
        "Radiology technologist",
        "Dr. B, a colleague from the prior week's shift",
        "On-call hospitalist"
      ],
      "technical_terms_to_use": [
        "pleuritic chest pain",
        "Wells score",
        "PERC rule",
        "D-dimer",
        "pretest probability",
        "CT pulmonary angiography (CTPA)",
        "costochondritis",
        "disposition",
        "hospitalist admission",
        "contrast reaction"
      ],
      "technical_terms_to_avoid": [
        "premature closure",
        "action bias",
        "outcome bias",
        "anchoring",
        "cognitive bias",
        "heuristic",
        "confirmation bias",
        "hindsight bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Reproducible chest wall tenderness on palpation",
          "History of moving furniture two days prior",
          "Mild pleuritic pain, no leg swelling noted on brief inspection",
          "O2 saturation 97%, heart rate 88",
          "Patient mentions a 10-hour flight home from a trip one week earlier",
          "Patient offhandedly mentions a mild calf ache, not formally examined"
        ],
        "new_information_after_decision": [
          "Nurse rechecks the patient later and confirms mild left calf swelling, consistent with the earlier verbal complaint"
        ],
        "alternatives": [
          "Settle on musculoskeletal strain as the working diagnosis based on the tenderness finding alone",
          "Fold the flight history and calf ache into an expanded differential and examine the leg directly before committing to a single explanation"
        ],
        "intended_action": "Attending notes the tenderness is suggestive of a musculoskeletal cause but flags the flight and calf complaint as worth a direct leg exam, and defers a final impression until that exam is done."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Resident has already drawn a D-dimer per department protocol",
          "D-dimer returns mildly elevated, just above the assay cutoff",
          "Patient's calculated pretest probability remains low-to-moderate given exam findings",
          "CT scanner has a 40-minute queue with trauma priority",
          "Charge nurse is pushing to clear beds for boarding admissions",
          "Two hours remain before shift handoff"
        ],
        "new_information_after_decision": [
          "CTPA is negative for pulmonary embolism",
          "Scan incidentally reveals a small indeterminate lung nodule requiring outpatient follow-up",
          "Patient has a mild contrast reaction requiring monitoring, delaying disposition by 45 minutes"
        ],
        "alternatives": [
          "Order an emergent CTPA immediately given the elevated D-dimer",
          "Recalculate the Wells/PERC risk formally with the new calf finding before deciding whether imaging changes management"
        ],
        "intended_action": "Attending redoes the risk score with the resident, factoring in the calf swelling, and concludes the updated pretest probability still warrants imaging, so orders the CTPA on that basis rather than skipping the reassessment."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Charge nurse mentions that Dr. B discharged a similarly presenting patient the prior week without ordering imaging",
          "Attending is told that patient later did well with no adverse event",
          "Attending has no direct knowledge yet of what specific findings, risk scores, or conversation Dr. B had with that patient at the time",
          "Attending is mid-shift, multitasking on the current CTPA workup"
        ],
        "new_information_after_decision": [
          "Resident confirms Dr. B had documented a formal low-risk Wells score and PERC-negative status before discharging that patient"
        ],
        "alternatives": [
          "Withhold judgment on Dr. B's decision until learning what information and risk stratification Dr. B actually used",
          "Judge Dr. B's decision primarily by how the case turned out"
        ],
        "intended_action": "Attending says it's hard to know if Dr. B's call was sound without knowing what workup was documented, and asks the resident to check the chart before forming an opinion."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "CTPA negative for PE",
          "Incidental lung nodule needs outpatient follow-up",
          "Patient recovered from mild contrast reaction, currently stable",
          "Hospitalist is reachable but reluctant to admit a patient with a negative PE workup",
          "Shift handoff is imminent",
          "Patient and family are anxious and requesting to go home"
        ],
        "new_information_after_decision": [
          "Patient is scheduled for outpatient pulmonology follow-up within one week",
          "No further acute events during the remainder of the visit"
        ],
        "alternatives": [
          "Admit briefly for observation given the eventful workup and contrast reaction",
          "Discharge home with structured follow-up instructions and safety-netting"
        ],
        "intended_action": "Attending weighs the residual clinical uncertainty, boarding pressure, and follow-up feasibility, and reaches a disposition decision without a predetermined or reflexive preference for either admitting or discharging."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what was going on in the department when this patient arrived.",
        "What was your first impression of the patient's presentation?"
      ],
      "timeline_reconstruction": [
        "What happened right after you completed the initial exam?",
        "What did you learn between ordering the D-dimer and getting the result back?",
        "How did the conversation about Dr. B's earlier patient come up during your shift?",
        "What was the sequence of events after the CTPA came back?"
      ],
      "decision_point_probes": [
        "What made you want to examine the leg directly rather than settle on the chest wall finding alone?",
        "What alternative explanations did you keep open at that point, and why?",
        "What led you to recheck the risk score before deciding on the CTPA?",
        "How much did the scanner queue and bed pressure factor into that decision?",
        "When you thought about Dr. B's decision, what information were you waiting to confirm before forming a view?",
        "Would your assessment of Dr. B's decision have changed if the outcome had been different but the documented reasoning stayed the same?",
        "How did you weigh admission versus discharge for the final disposition?"
      ],
      "goals_and_alternatives": [
        "What were you trying to accomplish at each stage—speed, certainty, or safety?",
        "What was the next-best alternative you didn't choose at each decision point?"
      ],
      "decision_basis_and_experience": [
        "What past cases, if any, were you drawing on during this shift?",
        "How confident were you in each decision at the time you made it, versus now?"
      ],
      "time_pressure_and_uncertainty": [
        "How much did the two-hour handoff deadline shape your choices?",
        "Where did you feel most uncertain during this case?"
      ],
      "closing_hypotheticals": [
        "If the department had been quiet that night, would you have handled the D-dimer result differently?",
        "If you'd learned about Dr. B's Wells score before hearing about the outcome, would your reaction have been different?",
        "Looking back, is there a point where you'd have paused longer before deciding?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "HC_Biased_3",
      "features_to_match": [
        "Domain vocabulary (Wells score, PERC, D-dimer, CTPA, costochondritis, disposition, hospitalist admission, contrast reaction)",
        "Setting and constraints (ED overcrowding, single scanner, boarding pressure, handoff deadline)",
        "Actors (attending, resident, charge nurse, radiology tech, Dr. B, hospitalist)",
        "Emotional tone (time-pressured, mildly anxious family, professional uncertainty)",
        "Exact four-decision-point structure and sequencing",
        "Difficulty level (challenging) and narrative complexity"
      ],
      "features_to_remove_or_change": [
        "Early closure on musculoskeletal strain without examining the calf",
        "Ordering CTPA without first reassessing risk score",
        "Judging Dr. B's decision primarily by outcome before learning the process",
        "Any framing that resolves ambiguity through reflexive action or premature diagnostic settlement"
      ],
      "ambiguity_boundary": "Genuine clinical uncertainty (borderline D-dimer, incidental nodule, disposition trade-off) is preserved, but every decision is supported by an explicit, reasonable evidentiary or process-based justification rather than by a shortcut pattern matching a named bias."
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
      "Exactly 4 decision points present, matching the paired biased scenario's phase structure",
      "Zero intended bias instances embedded anywhere in the interview",
      "All vocabulary, actors, constraints, and emotional tone match HC_Biased_3",
      "Each decision point shows balanced consideration of at least two alternatives with a stated, reasonable justification",
      "No bias labels, definitions, or psychological explanations appear in probe plan or timeline text",
      "Word count target 1,350 (range 1,215-1,485) achievable given matched narrative density to the paired scenario",
      "Consequences at each decision point (calf swelling, incidental nodule, contrast reaction, Wells-score confirmation) remain genuinely uncertain and do not mechanically prove sound or unsound reasoning"
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
