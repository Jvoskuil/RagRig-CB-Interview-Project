You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HC_Biased_1",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Emergency Department Attending Physician",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Atypical Chest Complaint in a Patient with an Anxiety History",
    "scenario_summary_internal": "During a busy night shift, an ED attending evaluates a returning patient with a well-documented history of panic-attack-related ED visits who now presents with chest tightness and dyspnea. The physician must decide how to triage, interpret ambiguous vital signs, respond to a new symptom (calf tenderness), and determine disposition, all while a prior diagnostic pattern from the chart shapes early clinical framing.",
    "occupational_realism": {
      "objective": "Accurately triage, diagnose, and disposition a patient with an atypical presentation while maintaining ED throughput under high patient volume.",
      "setting": "Urban hospital emergency department, overnight shift, moderate-to-high patient census, limited monitored bed availability.",
      "constraints": [
        "High patient volume with pressure to keep wait times low",
        "Limited monitored beds and portable monitoring equipment",
        "Patient chart contains five prior ED visits coded as panic attacks",
        "On-call cardiology and radiology have variable response times overnight",
        "Nursing staff stretched across multiple acute patients simultaneously"
      ],
      "stakeholders": [
        "ED attending physician",
        "Triage nurse",
        "Patient",
        "On-call cardiologist",
        "Radiology technician"
      ],
      "technical_terms_to_use": [
        "triage acuity",
        "ECG",
        "troponin",
        "D-dimer",
        "Wells score",
        "sinus tachycardia",
        "SpO2",
        "chief complaint",
        "chest CT angiography",
        "disposition"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "expectation",
        "cognitive",
        "prior probability",
        "anchoring",
        "confirmation"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief complaint: chest tightness and shortness of breath",
          "Chart shows five prior ED visits over 18 months, all discharged with panic attack diagnosis",
          "Mild diaphoresis noted by triage nurse",
          "Patient appears anxious, speaking rapidly"
        ],
        "new_information_after_decision": [
          "ECG obtained within protocol window shows sinus tachycardia, no ST changes",
          "Initial vitals: HR 108, BP 128/82, RR 22, SpO2 94% on room air"
        ],
        "alternatives": [
          "Assign standard chest-pain protocol acuity requiring immediate ECG regardless of history",
          "Assign lower acuity based on anxiety history and revisit after brief observation"
        ],
        "intended_action": "Physician follows standard chest-pain protocol and orders an ECG, while mentally noting the patient's extensive anxiety-visit history as context for the encounter."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "ECG: sinus tachycardia, no acute ischemic changes",
          "HR 108, SpO2 94% on room air, mild diaphoresis persists",
          "Patient reports this 'feels like her usual attacks but a little different'",
          "Chart-driven framing of recurrent panic attacks established from Phase 1"
        ],
        "new_information_after_decision": [
          "Anxiolytic administered; patient's HR drops modestly to 100 after 20 minutes",
          "SpO2 remains at 94-95% despite reported symptomatic improvement"
        ],
        "alternatives": [
          "Order D-dimer and chest CT angiography to evaluate for pulmonary embolism given tachycardia and hypoxia",
          "Attribute tachycardia and mild desaturation to hyperventilation from anxiety and proceed with anxiolytic plus reassessment"
        ],
        "intended_action": "Physician interprets the borderline tachycardia and desaturation as consistent with a typical anxiety episode based on the patient's documented pattern, defers D-dimer/CT, and orders an anxiolytic with a plan to reassess."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient newly reports left calf tenderness and mild swelling, onset over the past two days",
          "SpO2 still 94-95% despite anxiolytic",
          "No prior mention of leg symptoms in chart"
        ],
        "new_information_after_decision": [
          "Wells score calculated as moderate-risk",
          "D-dimer sent, elevated; chest CT angiography ordered"
        ],
        "alternatives": [
          "Pursue DVT/PE workup via Wells score, D-dimer, and imaging given the new, chart-inconsistent symptom",
          "Attribute calf tenderness to muscle tension from prolonged anxious guarding and continue anxiety-focused management"
        ],
        "intended_action": "Physician treats the new calf symptom as inconsistent with the anxiety pattern and initiates a formal DVT/PE workup, overriding the earlier symptom framing."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "D-dimer elevated, chest CT pending",
          "Patient clinically stable but SpO2 still borderline",
          "Cardiology unavailable for immediate consult; radiology read expected in 45 minutes",
          "ED census rising, pressure to clear bed"
        ],
        "new_information_after_decision": [
          "CT angiography results become available after disposition decision is made",
          "Cardiology consult note added retrospectively"
        ],
        "alternatives": [
          "Hold patient in ED on monitored bed pending CT results before any disposition",
          "Admit to observation unit proactively given moderate Wells score and elevated D-dimer, without waiting for imaging"
        ],
        "intended_action": "Physician elects to hold the patient in a monitored ED bed pending imaging results rather than deciding disposition prematurely, given persisting uncertainty."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this patient first came to your attention.",
        "What was your initial impression when you reviewed the chart?"
      ],
      "timeline_reconstruction": [
        "What happened right after triage assigned an acuity level?",
        "Talk me through the sequence of tests you ordered and when.",
        "When did the calf symptom come up, and how did that change things?"
      ],
      "decision_point_probes": [
        "What specific information made you decide to follow the chest-pain protocol at triage?",
        "When you saw the tachycardia and SpO2 reading, what went through your mind about what it meant?",
        "What made the calf tenderness stand out to you compared to the earlier presentation?",
        "What factors led you to hold the patient rather than decide on disposition right away?"
      ],
      "cues": [
        "What specific vital sign or comment from the patient caught your attention at each step?"
      ],
      "information_sources": [
        "How much did the prior ED visit history influence how you read the current vitals?",
        "Did you consult any colleagues before ordering or deferring tests?"
      ],
      "goals": [
        "What were you trying to balance between speed and thoroughness that night?"
      ],
      "alternatives": [
        "What other explanation did you consider for the tachycardia and desaturation at the time?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision toward reassessment rather than immediate imaging?"
      ],
      "prior_experience": [
        "Have you seen this patient's pattern of visits before, and how did that shape your read of this case?"
      ],
      "time_pressure": [
        "How busy was the department at that point, and did that affect your pace of workup?"
      ],
      "uncertainty": [
        "At what point did you feel least confident about the diagnosis, and why?"
      ],
      "closing_hypotheticals": [
        "If the calf symptom hadn't come up, do you think the workup would have gone differently?",
        "If this had been a first-time visitor with no chart history, would your initial read of the vitals have been different?",
        "Looking back, is there a point where you'd handle the ambiguous vitals differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "eb_01",
        "bias": "Expectation Bias",
        "decision_point": 2,
        "mechanism": "The physician interprets ambiguous, borderline vital signs (tachycardia, mild hypoxia) through the lens of the expected diagnosis formed from chart history (recurrent panic attacks), leading to under-weighting of an alternative explanation (pulmonary embolism) and deferral of confirmatory testing.",
        "affected_reasoning_operation": "Interpretation and weighting of physiological evidence against a pre-formed diagnostic expectation",
        "evidence_available_at_time": [
          "Five prior ED visits coded as panic attacks",
          "HR 108, SpO2 94% room air",
          "Patient's own comment that the episode 'feels like her usual attacks but a little different'",
          "No ischemic ECG changes"
        ],
        "required_textual_manifestation": "The physician explicitly frames the tachycardia and desaturation as fitting the patient's known pattern ('this looks like her usual anxiety picture') and chooses anxiolytic plus reassessment over D-dimer/CT despite values falling outside a typical uncomplicated panic-attack range.",
        "plausible_nonbias_interpretation": "A reasonable clinician could argue this reflects appropriate stewardship of limited overnight resources and legitimate reliance on a strong, well-documented diagnostic base rate for this specific patient.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "expectation bias",
          "anchoring",
          "confirmation bias",
          "any named cognitive-bias label or definition"
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
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly one Expectation Bias instance planned, assigned to decision point 2 only.",
      "Decision point 1 (triage/protocol adherence) and decision point 3 (calf symptom escalation) are written as protocol-consistent or evidence-updating actions, not additional bias instances.",
      "Decision point 4 (holding for imaging) reflects uncertainty tolerance, not bias.",
      "No bias labels, definitions, or explanatory psychological language appear in probes or narrative.",
      "Word count target 1,350 (range 1,215-1,485) achievable given four decision points and probe set without repetitive exposition.",
      "Consequences (elevated D-dimer, pending CT) do not mechanically confirm or refute whether decision point 2 was biased."
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
