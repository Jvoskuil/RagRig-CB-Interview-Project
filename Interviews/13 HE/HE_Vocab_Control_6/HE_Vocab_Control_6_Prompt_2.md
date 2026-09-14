You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HE_Vocab_Control_6",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Building/Fire Code Official (Plan Review and Permitting)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Meridian Tower Atrium Retrofit: Balanced Plan Review and Occupancy Decision",
    "scenario_summary_internal": "A municipal Building/Fire Code Official handles the adaptive-reuse permit for Meridian Tower, a 22-story former office building being converted to mixed-use residential/commercial with a large central atrium. The atrium geometry cannot meet prescriptive smoke-control provisions, so the design team submits a performance-based alternative. The official evaluates the alternative design on its technical merits, selects a commissioning/verification protocol by weighing fit against defensibility, responds to a small cluster of fire-door deficiencies discovered during construction with appropriately calibrated statistical reasoning, and decides whether to grant temporary occupancy before full fire-alarm/smoke-control integration testing is complete by explicitly weighing case-specific risk data. A minor trash-chute fire late in construction (contained by sprinklers, no injuries) prompts a retrospective review that remains evidentially grounded in what was actually known beforehand.",
    "occupational_realism": {
      "objective": "Ensure the Meridian Tower conversion meets life-safety code requirements for smoke control, fire-rated separations, and alarm integration while managing statutory review deadlines and the developer's financing-driven schedule.",
      "setting": "Municipal Building & Fire Department, plan review and permitting division; site visits to a 22-story adaptive-reuse construction project during active build-out.",
      "constraints": [
        "30-day statutory plan review deadline",
        "Department staffing shortage limiting time for independent technical review",
        "No budget authorized for third-party peer review on this project",
        "Developer financing deadline tied to a move-in date",
        "City council pressure to expedite housing supply projects",
        "Ongoing active construction limiting full-building inspection access"
      ],
      "stakeholders": [
        "Plan review official (interviewee)",
        "Fire protection engineer of record (Halkirk & Vance engineering firm)",
        "General contractor",
        "Developer/project owner",
        "Building official supervisor",
        "Construction inspector colleague",
        "Future building occupants"
      ],
      "technical_terms_to_use": [
        "performance-based design",
        "alternative means and methods",
        "smoke control system",
        "CFD modeling",
        "commissioning/acceptance testing",
        "fire-rated door assembly",
        "integration testing",
        "equivalent level of safety",
        "temporary certificate of occupancy"
      ],
      "technical_terms_to_avoid": [
        "clustering illusion",
        "base-rate neglect",
        "optimism bias",
        "ambiguity effect",
        "authority bias",
        "hindsight bias",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Halkirk & Vance submitted a CFD-based performance design for the atrium smoke control system because the geometry does not meet prescriptive NFPA 92/IBC atrium provisions",
          "Halkirk & Vance is a nationally recognized regional fire-engineering firm with dozens of previously approved performance-based designs",
          "A neighboring jurisdiction approved a similar atrium design from the same firm the prior year",
          "No budget was authorized for an independent third-party peer review of the CFD assumptions"
        ],
        "new_information_after_decision": [
          "The official identified a specific input assumption (stack-effect behavior under partial door-open conditions) that warranted direct clarification from the design team before conditions were finalized"
        ],
        "alternatives": [
          "Approve the alternative design based on the firm's documentation with standard conditions",
          "Request a targeted written clarification of the specific stack-effect assumption from the design team before approval, without commissioning a full external peer review",
          "Require a full independent third-party peer review of the CFD assumptions before approval, adding roughly three weeks to the review"
        ],
        "intended_action": "Approve the performance-based design only after requesting and receiving a written clarification of the specific CFD assumption most relevant to occupant egress, balancing review-time constraints against a targeted technical check rather than either blanket deference or a full external review."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two candidate commissioning/acceptance test protocols were submitted for the smoke control system",
          "Option A is a newer risk-informed acceptance protocol whose pass/fail thresholds are only partially and qualitatively defined in current guidance",
          "Option B is a traditional prescriptive visual smoke test with clearly defined binary pass/fail criteria but known lower sensitivity to certain atrium failure modes",
          "Available technical guidance suggests Option A is better matched to this atrium's specific risk profile"
        ],
        "new_information_after_decision": [
          "The permit conditions specify Option A as the primary commissioning protocol, supplemented with defined interim checkpoints to make the qualitative thresholds auditable"
        ],
        "alternatives": [
          "Require Option A alone, accepting the administrative burden of qualitative thresholds",
          "Require Option B alone, accepting weaker sensitivity to relevant failure modes",
          "Require Option A supplemented with defined interim checkpoints and documentation standards to make its criteria auditable"
        ],
        "intended_action": "Select Option A as the primary protocol because it better matches the atrium's risk profile, while adding documented interim checkpoints so the qualitative thresholds remain defensible for enforcement purposes."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Inspection reports show fire-rated door deficiencies on floors 8, 11, and 14 out of 22",
          "Floor assignments to installation crews were rotated randomly across the building, not fixed by floor",
          "3 deficiencies were found among roughly 150 doors inspected so far, a rate consistent with typical random defect rates on comparable projects",
          "The three flagged floors are non-contiguous"
        ],
        "new_information_after_decision": [
          "A building-wide random sample inspection is completed and finds a defect rate consistent with the original three floors, indicating no floor-specific concentration"
        ],
        "alternatives": [
          "Treat the three-floor pattern as evidence of a localized crew or workmanship problem and concentrate follow-up inspection there",
          "Recognize the sample size is too small to indicate a systemic pattern and continue the originally planned random-sample inspection across all floors"
        ],
        "intended_action": "Continue the originally planned random-sample inspection across all floors, explicitly noting that three deficiencies among 150 doors with randomly rotated crews is within the range expected from ordinary variation and does not by itself indicate a localized cause."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Full fire-alarm and smoke-control integration testing is scheduled in three weeks",
          "The developer requests a temporary certificate of occupancy for completed lower floors, citing a financing deadline",
          "This general contractor's overall track record on other city projects has been favorable",
          "The department's own five-year inspection data show a roughly 15% integration-test failure/rework rate for atrium smoke-control systems citywide",
          "A colleague mentions that a nearby, similar building recently received early partial occupancy without incident"
        ],
        "new_information_after_decision": [
          "A minor trash-chute fire occurs during the remaining construction period; sprinklers contain it, no injuries occur, and the smoke migration pattern is later found consistent with the trash-chute enclosure rather than a defect in the atrium system"
        ],
        "alternatives": [
          "Grant temporary occupancy for completed lower floors with monitoring conditions, pending full integration testing",
          "Deny temporary occupancy and require full integration testing to be completed and passed before any occupancy is granted",
          "Grant a narrowly conditioned occupancy limited to floors served by fire-rated separations independent of the untested atrium smoke system"
        ],
        "intended_action": "Grant a narrowly conditioned temporary occupancy limited to floors that do not rely on the untested atrium smoke system, explicitly citing the citywide 15% integration-test rework rate as the reason for withholding broader occupancy despite the contractor's favorable general record and the nearby building's outcome."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role in the Meridian Tower conversion project and what made it nonroutine?",
        "What was your primary objective when you first received the atrium smoke control alternative-compliance submittal?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you know at that point?",
        "What new information came in after each major decision you made?",
        "Were there moments where the sequence of events surprised you?"
      ],
      "decision_point_probes": [
        "What specific evidence or documents did you rely on when approving the atrium smoke control design, and what made you ask for further clarification?",
        "What alternatives did you consider before choosing the commissioning protocol, and what tipped the balance?",
        "When the door deficiencies came in on floors 8, 11, and 14, how did you decide whether that pattern was meaningful?",
        "What made you confident about the scope of the temporary occupancy decision, and what information shaped where you drew the line?",
        "How much time pressure did you feel at each of these points, and how did that affect what you checked versus what you took on trust?",
        "What did you consider the biggest source of uncertainty at each decision, and how did you resolve it?"
      ],
      "closing_hypotheticals": [
        "If the third-party peer review budget had been available from the start, would your initial approval have gone differently?",
        "Looking back at your original approval of the atrium design, how do you now see the decision given what happened with the trash-chute fire?",
        "If you had to make the temporary occupancy call again with the same information you had then, what would you do differently, if anything?",
        "What would you tell a newer plan reviewer to watch for in a similar performance-based design submittal?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "HE_Biased_6",
      "features_to_match": [
        "Domain vocabulary (performance-based design, CFD modeling, commissioning/acceptance testing, fire-rated door assembly, integration testing, temporary certificate of occupancy)",
        "Occupational setting, stakeholders, and role of the interviewee",
        "Four-decision-point structure and topical sequence (design approval, commissioning protocol, door-deficiency response, temporary occupancy)",
        "Difficulty level and narrative complexity",
        "Emotional tone (measured, professional, moderate pressure)",
        "Overall word count and dialogue format"
      ],
      "features_to_remove_or_change": [
        "Remove reliance on firm reputation as a substitute for technical verification at Decision Point 1",
        "Remove selection of a protocol primarily for criterion clarity over technical fit at Decision Point 2",
        "Remove inference of a systemic localized cause from a small random sample at Decision Point 3",
        "Remove reliance on general contractor reputation as the basis for confidence in an untested system at Decision Point 4",
        "Remove discounting of the citywide base rate in favor of an anecdote at Decision Point 4",
        "Remove retrospective claims of foreseeability inconsistent with what was actually known at the time of the original decision"
      ],
      "ambiguity_boundary": "Genuine technical trade-offs (e.g., qualitative thresholds versus binary criteria, small-sample inspection data, competing schedule pressures) may remain visible and undetermined in places, but every decision must be accompanied by an evidence-consistent, non-biased justification, and no decision may rely on the mechanisms described in features_to_remove_or_change."
    },
    "counterfactual_specification": {
      "causal_variable": "engineering_firm_reputation (autoselected candidate retained for consistency with the paired biased scenario; not applied in this vocabulary_control generation)",
      "original_state": "Design submitted and stamped by a nationally recognized, previously-approved fire protection engineering firm (Halkirk & Vance)",
      "counterfactual_state": "Not applicable in this generation run; condition is vocabulary_control, not counterfactual",
      "variables_to_hold_constant": [
        "Atrium geometry and code non-conformance",
        "Statutory review timeline and staffing constraints",
        "Developer schedule pressure",
        "All four decision points and their topical sequence"
      ],
      "expected_causal_difference": "Not applicable: no causal manipulation is performed in this control condition.",
      "causal_test_question": "Not applicable in this generation run."
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Zero intended instances of all six named biases are embedded, consistent with the vocabulary_control condition rule overriding the input manifest's occurrence counts.",
      "Each decision point includes an evidence-consistent, non-biased justification that mirrors the topical structure of HE_Biased_6 without reusing its biased mechanisms.",
      "Domain vocabulary, actors, setting, difficulty, and decision-count match HE_Biased_6.",
      "Bias names, definitions, and psychological terminology are excluded from all public-facing timeline, probe, and dialogue content.",
      "Word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points with moderate-depth probes without repetitive exposition.",
      "Consequences (minor contained fire, no injuries) do not mechanically confirm or deny whether any specific decision was correct or incorrect.",
      "No accidental instance of Clustering illusion, Probability neglect/Base-Rate Neglect, Optimism bias, Ambiguity effect, Authority Bias, or Hindsight bias is introduced anywhere in the timeline or probes."
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
