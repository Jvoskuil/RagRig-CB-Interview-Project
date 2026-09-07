You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HC_Biased_4",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Hospital Medicine Attending Physician (Internal Medicine Hospitalist)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Overnight-to-Morning Handoff: Managing a Suspected Sepsis Admission",
    "scenario_summary_internal": "An internal medicine hospitalist takes over care of a 68-year-old patient admitted overnight with fever, tachycardia, and borderline hypotension of unclear source. Across a single shift, the attending must decide how aggressively to work up the source of infection, which empiric antibiotic order set to select, how to configure ongoing monitoring orders, and how to interpret new culture data during multidisciplinary rounds. The case is nonroutine because the initial presentation is ambiguous (could be urinary, pulmonary, or skin/soft-tissue source) and institutional tools (EHR order sets, prior clinical experience, team handoff framing) shape the physician's reasoning in ways that are individually defensible but cumulatively distort the diagnostic and treatment path.",
    "occupational_realism": {
      "objective": "Correctly identify the infectious source and select an appropriately targeted, resource-proportionate treatment and monitoring plan within the first 24 hours of admission.",
      "setting": "Inpatient general medicine ward at a mid-sized community teaching hospital during a normal weekday, transitioning from night-shift coverage to day-shift attending rounds.",
      "constraints": [
        "Limited time before morning multidisciplinary rounds",
        "Incomplete overnight culture and imaging data",
        "EHR order sets with pre-configured default durations and tiered antibiotic bundles",
        "Need to balance antibiotic stewardship against risk of undertreating a potentially severe infection",
        "Competing demand from ED for bed turnover pressuring quick disposition decisions"
      ],
      "stakeholders": [
        "Attending hospitalist",
        "Overnight resident (handoff author)",
        "Bedside nurse",
        "Infectious disease consultant (available by page)",
        "Patient and family"
      ],
      "technical_terms_to_use": [
        "empiric antibiotic coverage",
        "pretest probability",
        "source control",
        "SIRS criteria",
        "telemetry order",
        "de-escalation",
        "differential diagnosis"
      ],
      "technical_terms_to_avoid": [
        "affect heuristic",
        "decoy effect",
        "default bias",
        "primacy bias",
        "cognitive bias",
        "anchoring"
      ],
      "excluded_themes": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient: 68-year-old male, fever 38.9C, HR 112, BP 98/62, mild confusion overnight",
          "No clear localizing symptoms yet; overnight labs show mild leukocytosis",
          "Attending recalls a recent case from three weeks prior where a similarly presenting patient was under-worked-up and later found to have rapidly progressive necrotizing fasciitis with a poor outcome"
        ],
        "new_information_after_decision": [
          "CT imaging is ordered emergently; results return three hours later showing no soft-tissue or abdominal source",
          "Urinalysis pending at time of decision"
        ],
        "alternatives": [
          "Order a stepwise, symptom-guided workup starting with basic labs and urinalysis before advanced imaging",
          "Order immediate broad cross-sectional imaging (CT torso) despite low localizing findings",
          "Defer imaging until vital sign trend and initial labs clarify severity"
        ],
        "intended_action": "Attending orders immediate CT imaging, citing a strong personal reaction tied to the recent adverse case rather than the patient's actual presenting probability of a soft-tissue emergency."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Blood and urine cultures pending, no organism identified yet",
          "EHR sepsis order set presents three empiric antibiotic bundles: (A) narrow-spectrum single-agent, (B) broad-spectrum dual-agent 'standard bundle', (C) broad-spectrum triple-agent 'extended bundle' with similar cost to (B) but broader, less-targeted coverage and higher toxicity risk with no clear added benefit for this presentation",
          "Patient hemodynamically stable, SIRS criteria met but not meeting severe sepsis threshold"
        ],
        "new_information_after_decision": [
          "Pharmacy flags the extended bundle as rarely indicated for this severity level",
          "ID consultant later notes bundle (B) was reasonable but confirms bundle (A) would likely have sufficed given stability"
        ],
        "alternatives": [
          "Select bundle (A), narrow-spectrum monotherapy consistent with stable presentation",
          "Select bundle (B), broad-spectrum dual-agent 'standard' bundle",
          "Select bundle (C), broad-spectrum triple-agent extended bundle"
        ],
        "intended_action": "Attending selects bundle (B), reasoning that it looks like the moderate, sensible middle option relative to the two bracketing choices, without independently re-deriving the appropriate spectrum from the patient's actual severity."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient stabilizing, HR now 88, BP 118/74, mentation clear",
          "EHR admission order set auto-populates a pre-checked 5-day continuous telemetry order and a pre-checked indwelling urinary catheter continuation order as part of the standard sepsis pathway",
          "Nursing flags that patient is ambulating well and catheter may no longer be indicated"
        ],
        "new_information_after_decision": [
          "Case management later notes prolonged catheter use is a known driver of hospital-acquired infection risk and length of stay",
          "Telemetry data over the next two days shows no arrhythmia events"
        ],
        "alternatives": [
          "Actively reassess and shorten telemetry duration and discontinue the catheter based on current clinical status",
          "Accept the pre-populated 5-day telemetry and catheter continuation orders as configured in the order set",
          "Escalate monitoring further out of caution"
        ],
        "intended_action": "Attending signs off on the pre-checked telemetry and catheter orders without modification, treating the order-set default as the appropriate plan rather than re-evaluating necessity given the patient's improved status."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Overnight resident's handoff note and initial verbal presentation at rounds framed the case as 'likely urosepsis' based on early urinalysis showing mild pyuria",
          "New morning data: urine culture is now finalized and shows no significant bacterial growth; blood culture is flagged preliminarily positive with gram-positive cocci in clusters, more consistent with a skin or line-related source",
          "Team discussion at rounds begins with, and largely stays anchored to, the urosepsis framing introduced first"
        ],
        "new_information_after_decision": [
          "Repeat blood cultures and skin/IV site examination two hours later reveal a peripheral IV site with local erythema, supporting a catheter-related bacteremia source",
          "Antibiotic coverage is later adjusted to target the newly identified source"
        ],
        "alternatives": [
          "Re-open the differential fully in light of the negative urine culture and positive blood culture morphology",
          "Continue treating the case primarily as urosepsis, the diagnosis introduced at the start of rounds, with only minor adjustments",
          "Request an infectious disease consult before finalizing the working diagnosis"
        ],
        "intended_action": "The team, including the attending, continues to frame ongoing management around the urosepsis diagnosis first proposed at the start of rounds, giving that initial framing more weight in discussion than the newer culture data that arrived later in the same conversation."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how you first learned about this patient and what your initial impression was.",
        "What was your role in this case, and what were you responsible for deciding?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you know at that point?",
        "What new information came in over the course of the shift, and when?",
        "How did the picture change between your first assessment and rounds?"
      ],
      "decision_point_probes": [
        "What made you decide to order imaging right away rather than wait for basic labs?",
        "How did you weigh the three antibiotic bundle options in the order set?",
        "Did you actively reconsider the telemetry and catheter orders, or did you leave them as they came up?",
        "When the new culture data came in, how did that change the working diagnosis discussed at rounds?"
      ],
      "goals_and_alternatives": [
        "What other options did you consider at each step, and why did you rule them out?",
        "What were you ultimately trying to balance or protect against in this case?"
      ],
      "decision_basis": [
        "What specific piece of information or experience most influenced your choice?",
        "Was there anything from a past case that came to mind while managing this one?"
      ],
      "prior_experience_time_pressure_uncertainty": [
        "How much time pressure did you feel at each stage?",
        "Where did you feel most uncertain, and how did you handle that uncertainty?",
        "Has a similar case shaped how you approach patients like this?"
      ],
      "closing_hypotheticals": [
        "If the order set had presented the antibiotic options differently, do you think you'd have chosen differently?",
        "If the urine culture result had come back before the team discussion started, would the conversation have gone differently?",
        "Looking back, is there a point where you'd handle things differently with the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ah_01",
        "bias": "Affect Heuristic",
        "decision_point": 1,
        "mechanism": "Emotional residue from a recent, vivid adverse outcome (necrotizing fasciitis case) drives an elevated subjective risk judgment that overrides the low objective pretest probability suggested by the current patient's presentation, leading to a decision framed around feeling rather than probability.",
        "affected_reasoning_operation": "Risk estimation / diagnostic prioritization",
        "evidence_available_at_time": [
          "Non-specific fever and tachycardia without localizing soft-tissue findings",
          "Recollection of a recent unrelated case with a bad outcome"
        ],
        "required_textual_manifestation": "The physician explicitly links the urgency of the imaging decision to how the recent case made them feel ('I didn't want to miss it again' or equivalent) rather than to specific exam findings in the current patient.",
        "plausible_nonbias_interpretation": "Ordering early imaging could be framed as reasonable defensive/cautious practice given diagnostic uncertainty.",
        "strength": "subtle",
        "do_not_make_explicit": ["affect heuristic", "emotional bias", "cognitive bias"]
      },
      {
        "instance_id": "de_01",
        "bias": "Decoy Effect",
        "decision_point": 2,
        "mechanism": "The presence of a dominated 'extended bundle' option (broader coverage, similar cost, no added benefit, higher toxicity) makes the 'standard bundle' appear to be the sensible middle ground, pulling the choice toward it independent of an independent severity-based assessment.",
        "affected_reasoning_operation": "Option evaluation among asymmetric choice set",
        "evidence_available_at_time": [
          "Three EHU bundles: narrow monotherapy, standard dual-agent, extended triple-agent",
          "Patient's actual stability level supporting narrower coverage"
        ],
        "required_textual_manifestation": "The physician's stated rationale references the bundle's position relative to the other two options ('it seemed like the reasonable one in the middle') rather than an independent clinical derivation of required spectrum.",
        "plausible_nonbias_interpretation": "Choosing the standard bundle could be explained as adherence to common institutional practice patterns for sepsis rule-outs.",
        "strength": "subtle",
        "do_not_make_explicit": ["decoy effect", "asymmetric dominance"]
      },
      {
        "instance_id": "db_01",
        "bias": "Default Bias",
        "decision_point": 3,
        "mechanism": "The pre-checked telemetry and catheter continuation settings in the EHR order set are accepted without active reassessment, even though the patient's improved clinical status would support discontinuation or shortening.",
        "affected_reasoning_operation": "Order confirmation / status-quo evaluation",
        "evidence_available_at_time": [
          "Improved vital signs and mentation",
          "Nursing flag suggesting catheter may no longer be needed",
          "Pre-populated 5-day telemetry/catheter defaults in the order set"
        ],
        "required_textual_manifestation": "The physician describes signing off on the orders as configured, without describing an active re-evaluation step despite acknowledging the patient's improvement.",
        "plausible_nonbias_interpretation": "Leaving the standard pathway in place could be explained as reasonable adherence to a validated sepsis protocol pending full stabilization.",
        "strength": "subtle",
        "do_not_make_explicit": ["default bias", "status quo bias"]
      },
      {
        "instance_id": "pb_01",
        "bias": "Primacy Bias",
        "decision_point": 4,
        "mechanism": "The diagnostic framing ('likely urosepsis') introduced first at the start of rounds continues to anchor the team's discussion and management even after later-arriving culture data (negative urine culture, gram-positive blood culture) supports reconsidering the source.",
        "affected_reasoning_operation": "Belief updating / differential diagnosis revision",
        "evidence_available_at_time": [
          "Initial verbal framing of 'likely urosepsis' at start of rounds",
          "Newly returned urine culture (no significant growth)",
          "Newly returned blood culture morphology (gram-positive cocci in clusters)"
        ],
        "required_textual_manifestation": "The physician's account shows the team's discussion continuing to center on the urosepsis framing even while narrating the arrival of culture data that runs counter to it, before only later shifting focus.",
        "plausible_nonbias_interpretation": "Continuing to treat urosepsis as a working diagnosis briefly could be explained as reasonable caution against overreacting to a single preliminary culture result.",
        "strength": "subtle",
        "do_not_make_explicit": ["primacy bias", "anchoring", "first information effect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": "AUTOSELECT — not applicable, no counterfactual condition requested",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and none are merged or split.",
      "Confirm each of the 4 planned bias instances appears exactly once, at its assigned decision point, with no repetition elsewhere.",
      "Confirm no bias name, definition, or psychological label appears in the interview text.",
      "Confirm each decision point includes at least two plausible alternatives and both pre- and post-decision information.",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count falls between 1,215 and 1,485 words.",
      "Confirm consequences described do not conclusively prove or disprove bias presence (outcomes remain ambiguous as to causation)."
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
