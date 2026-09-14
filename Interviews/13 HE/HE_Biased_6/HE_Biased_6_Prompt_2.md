You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HE_Biased_6",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Building/Fire Code Official (Plan Review and Permitting)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Meridian Tower Atrium Retrofit: Plan Review and Occupancy Decision",
    "scenario_summary_internal": "A municipal Building/Fire Code Official handles the adaptive-reuse permit for Meridian Tower, a 22-story former office building being converted to mixed-use residential/commercial with a large central atrium. The atrium geometry cannot meet prescriptive smoke-control provisions, so the design team submits a performance-based alternative. The official must approve the alternative design, select a commissioning/verification protocol, respond to a cluster of fire-door deficiencies discovered during construction, and decide whether to grant temporary occupancy before full fire-alarm/smoke-control integration testing is complete. A minor trash-chute fire late in construction (contained by sprinklers, no injuries) prompts a retrospective review of the original design approval.",
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
          "The approval was issued with standard commissioning conditions but without independent verification of the CFD input assumptions"
        ],
        "alternatives": [
          "Approve the alternative design based on the firm's documentation, prior approvals, and reputation, with standard conditions",
          "Require an independent third-party peer review of the CFD assumptions before approval, adding roughly three weeks to the review"
        ],
        "intended_action": "Approve the performance-based design with standard conditions, leaning heavily on the engineering firm's credentials and prior track record rather than independently probing the CFD assumptions."
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
          "The permit conditions specify Option B as the required commissioning protocol"
        ],
        "alternatives": [
          "Require Option A, the risk-informed protocol better matched to the atrium's risk profile despite less crisply defined thresholds",
          "Require Option B, the traditional protocol with clear binary criteria despite weaker sensitivity to relevant failure modes",
          "Require both protocols be run in sequence"
        ],
        "intended_action": "Select Option B for the permit conditions primarily because its acceptance criteria are unambiguous, even though guidance indicates Option A is the better technical match for this design."
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
          "Inspection resources are redirected toward the three flagged floors and away from a planned random sample of the remaining floors"
        ],
        "alternatives": [
          "Treat the three-floor pattern as evidence of a localized crew or workmanship problem and concentrate follow-up inspection there",
          "Recognize the sample size is too small to indicate a systemic pattern and continue the originally planned random-sample inspection across all floors"
        ],
        "intended_action": "Conclude that a specific crew or floor grouping is responsible for a workmanship problem and concentrate follow-up inspection on floors 8, 11, and 14, even though the observed deficiency rate is consistent with ordinary random variation."
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
          "A minor trash-chute fire occurs during the remaining construction period; sprinklers contain it, no injuries occur, but smoke migration patterns raise questions about the atrium smoke system's readiness"
        ],
        "alternatives": [
          "Grant temporary occupancy for completed lower floors with monitoring conditions, pending full integration testing",
          "Deny temporary occupancy and require full integration testing to be completed and passed before any occupancy is granted"
        ],
        "intended_action": "Grant temporary occupancy with monitoring conditions, expecting the remaining testing will succeed based on the contractor's general track record and the nearby building's outcome, rather than the department's own citywide failure-rate data."
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
        "What specific evidence or documents did you rely on when approving the atrium smoke control design?",
        "What alternatives did you consider before choosing the commissioning protocol, and what tipped the balance?",
        "When the door deficiencies came in on floors 8, 11, and 14, what made you treat them as connected rather than coincidental?",
        "What made you confident the temporary occupancy decision would work out before full integration testing was complete?",
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
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "auth_01",
        "bias": "Authority Bias",
        "decision_point": 1,
        "mechanism": "Official's approval decision is driven substantially by the design firm's national reputation and prior approvals rather than independent scrutiny of the CFD modeling assumptions.",
        "affected_reasoning_operation": "Evidence weighting during technical evaluation of a submittal",
        "evidence_available_at_time": [
          "Firm's credentials and history of approved designs",
          "Peer jurisdiction's approval of a similar design from the same firm",
          "No independent peer review was commissioned"
        ],
        "required_textual_manifestation": "The official explicitly cites the firm's reputation, credentials, or prior approvals as a primary reason for approving without independently probing the CFD assumptions.",
        "plausible_nonbias_interpretation": "Deferring to a well-credentialed, previously reliable engineering firm under review-time constraints could be read as a reasonable resource-allocation judgment rather than bias.",
        "strength": "subtle",
        "do_not_make_explicit": ["authority bias", "deference", "credential-based reasoning"]
      },
      {
        "instance_id": "hind_01",
        "bias": "Hindsight bias",
        "decision_point": 1,
        "mechanism": "After the trash-chute fire, the official retrospectively characterizes the atrium design's inadequacy as having been obvious at the time of approval, despite the original CFD documentation appearing adequate given prior peer-jurisdiction approvals.",
        "affected_reasoning_operation": "Retrospective causal attribution and memory reconstruction of a past decision's foreseeability",
        "evidence_available_at_time": [
          "Original CFD report and peer-jurisdiction precedent (available at time of Phase 1 decision)",
          "Post-incident knowledge of smoke migration issues (available only later, informing the retrospective probe)"
        ],
        "required_textual_manifestation": "In response to a closing hypothetical/reflection probe about the original approval, the official states the design's shortcomings 'should have been obvious' or similar, reinterpreting the original decision using information only available after the incident.",
        "plausible_nonbias_interpretation": "A genuinely overlooked technical flaw that a careful post-incident audit later reveals would not itself be biased; it becomes an instance only if the official claims foreseeability inconsistent with what was actually knowable at the time.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "creeping determinism", "I knew it all along"]
      },
      {
        "instance_id": "amb_01",
        "bias": "Ambiguity effect",
        "decision_point": 2,
        "mechanism": "Official favors the commissioning protocol with clearly defined pass/fail criteria over the protocol better matched to the atrium's actual risk profile, because the better-matched option's thresholds are less precisely defined.",
        "affected_reasoning_operation": "Choice between two evidence-based options under differing degrees of defined criteria",
        "evidence_available_at_time": [
          "Option A: risk-informed protocol, better technical fit, partially qualitative thresholds",
          "Option B: traditional protocol, clear binary criteria, weaker sensitivity to relevant failure modes",
          "Guidance documents indicating Option A's suitability for this atrium"
        ],
        "required_textual_manifestation": "The official states a preference for the protocol with clear, unambiguous criteria specifically because it is easier to defend or apply, despite acknowledging the other option's better technical fit.",
        "plausible_nonbias_interpretation": "Choosing a protocol with well-established, defensible criteria for enforcement purposes could be a legitimate administrative preference rather than bias.",
        "strength": "moderate",
        "do_not_make_explicit": ["ambiguity effect", "ambiguity aversion", "uncertainty avoidance"]
      },
      {
        "instance_id": "clu_01",
        "bias": "Clustering illusion",
        "decision_point": 3,
        "mechanism": "Official interprets three door deficiencies on non-contiguous, randomly assigned floors as evidence of a systemic, localized crew problem, despite the rate being consistent with expected random variation.",
        "affected_reasoning_operation": "Pattern recognition and inference from a small sample of inspection data",
        "evidence_available_at_time": [
          "Deficiency locations (floors 8, 11, 14)",
          "Random crew rotation policy across floors",
          "Overall deficiency rate (~3 of 150 doors) consistent with typical random defect rates"
        ],
        "required_textual_manifestation": "The official describes the three-floor pattern as meaningful or non-coincidental and redirects inspection resources specifically toward those floors based on that inferred pattern.",
        "plausible_nonbias_interpretation": "Targeting inspection where problems were actually found is a defensible triage approach; it becomes an instance only if the stated rationale is that the floors form a meaningful pattern rather than simply 'these are the floors with known issues.'",
        "strength": "subtle",
        "do_not_make_explicit": ["clustering illusion", "pattern in randomness", "small-sample inference"]
      },
      {
        "instance_id": "opt_01",
        "bias": "Optimism bias",
        "decision_point": 4,
        "mechanism": "Official expects the remaining integration testing will succeed mainly because this contractor's general track record has been good, downplaying the specific technical risk profile of this atrium's smoke-control system.",
        "affected_reasoning_operation": "Risk forecasting for an uncompleted, project-specific technical outcome",
        "evidence_available_at_time": [
          "Contractor's favorable general track record on unrelated projects",
          "Unresolved status of atrium-specific integration testing",
          "Known open questions about smoke control commissioning raised earlier in the project"
        ],
        "required_textual_manifestation": "The official expresses confident expectation that the testing will pass, grounded in the contractor's general reliability rather than atrium-specific technical evidence.",
        "plausible_nonbias_interpretation": "Relying on a contractor's track record is a legitimate, though partial, risk signal; it becomes an instance only if it displaces attention from atrium-specific risk factors already known to the official.",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "overconfidence", "unrealistic expectation"]
      },
      {
        "instance_id": "prob_01",
        "bias": "Probability neglect or Base-Rate Neglect",
        "decision_point": 4,
        "mechanism": "Official weighs a single vivid anecdote about a nearby building's successful early occupancy more heavily than the department's own citywide base rate of ~15% integration-test failure/rework for atrium smoke-control systems.",
        "affected_reasoning_operation": "Evidence weighting between a salient anecdote and an available statistical base rate",
        "evidence_available_at_time": [
          "Colleague's anecdote about a nearby building's successful early partial occupancy",
          "Department's own five-year data showing ~15% integration-test failure/rework rate citywide"
        ],
        "required_textual_manifestation": "The official cites the nearby building's outcome as a reason for confidence while the citywide failure-rate statistic is mentioned but not factored into the stated reasoning.",
        "plausible_nonbias_interpretation": "Anecdotal precedent can be a legitimate contextual data point; it becomes an instance only if the official's stated reasoning omits or discounts the more representative statistical base rate that was available.",
        "strength": "moderate",
        "do_not_make_explicit": ["base-rate neglect", "probability neglect", "anecdote versus statistics"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario was supplied for this generation run."
    },
    "counterfactual_specification": {
      "causal_variable": "engineering_firm_reputation (autoselected candidate for a future paired counterfactual run; not applied in this biased-condition generation)",
      "original_state": "Design submitted and stamped by a nationally recognized, previously-approved fire protection engineering firm (Halkirk & Vance)",
      "counterfactual_state": "Identical CFD-based design submitted and stamped by a small, locally unknown firm with no prior approvals in any jurisdiction",
      "variables_to_hold_constant": [
        "Atrium geometry and code non-conformance",
        "Statutory review timeline and staffing constraints",
        "Developer schedule pressure",
        "All other decision points (2, 3, 4) and their evidence"
      ],
      "expected_causal_difference": "If a future counterfactual pairing is generated using this variable, Authority Bias instance auth_01 should not manifest in that condition because the credibility-based deference cue would be absent, isolating the causal contribution of firm reputation to the Phase 1 approval decision.",
      "causal_test_question": "Does removing the engineering firm's high-authority reputation change whether the official independently scrutinizes the CFD assumptions before approving the alternative design?"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Each of the 6 requested biases has exactly one planned instance, matching the manifest.",
      "No decision point contains more than two instances of the same bias.",
      "auth_01 and hind_01 share decision point 1 but are distinct biases with distinct evidence sources (technical credential deference vs. post-incident retrospective reattribution).",
      "opt_01 and prob_01 share decision point 4 but are distinct biases with distinct evidence sources (general contractor track record vs. specific citywide statistical base rate).",
      "Bias names, definitions, and psychological terminology are excluded from all public-facing timeline, probe, and dialogue content.",
      "Word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points with moderate-depth probes without repetitive exposition.",
      "Consequences (minor contained fire, no injuries) do not mechanically confirm or deny whether any specific decision was biased."
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
