You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is for a plan-review case study, it's voluntary, and you can skip anything you'd rather not discuss. Can you start by telling me your role and how the Meridian Tower conversion landed on your desk?

Participant: Sure. I'm a plan review official in the building and fire division, mostly permitting and life-safety sign-off. Meridian Tower came to me because it was an adaptive reuse—22-story former office tower going to mixed-use residential and retail. The atrium was the whole complication. It's a big central void running most of the building height, and the geometry didn't fit the prescriptive smoke control provisions in our code. So the design team came in with a performance-based alternative instead.

Interviewer: What was your objective going in?

Participant: Get the project through review correctly and on time. We had a 30-day statutory clock, the department was short-staffed that quarter, and the city council was leaning on us to keep housing projects moving. So there was real pressure, but the job is still to make sure people are safe if there's a fire.

Interviewer: Walk me through what happened, from the beginning.

Participant: The engineering firm on record was Halkirk & Vance—they're a big regional name, they've done dozens of performance-based atrium designs, and a neighboring jurisdiction had approved a very similar design from them the year before. They submitted a CFD-based smoke control model instead of the prescriptive system. We didn't have budget that cycle for an outside peer review of the CFD assumptions, so it was really me evaluating it against the documentation package. After I signed off, we moved to writing commissioning conditions, which is where we had to pick between two verification protocols. Construction got underway, and partway through, our inspector flagged fire-door deficiencies on three floors. Then near occupancy, the developer pushed for an early certificate before full integration testing was done. Later in construction, there was a small trash-chute fire—sprinklers knocked it down fast, nobody was hurt—but it got people looking hard at the atrium smoke system again.

Interviewer: Let's reconstruct the order more precisely. What did you know before the first big decision, and what came in afterward?

Participant: Before approving the design, I had the CFD report, the firm's track record, and the neighboring jurisdiction's prior approval. After I approved it, we moved into commissioning planning—that's when the protocol question came up. After that decision, construction started, and the door issue surfaced maybe six weeks in. The occupancy request came right at the tail end, with the fire happening after that decision, not before.

Interviewer: Let's go through the first decision—approving the performance-based design. What evidence carried the most weight for you?

Participant: Honestly, the firm's name carried a lot of it. Halkirk & Vance has been doing this specific type of atrium work for years, and I knew their stamp had held up under scrutiny elsewhere—that neighboring jurisdiction's sign-off mattered to me. I read through the CFD report, but with the review clock running and no budget for an outside check, I leaned on the fact that this firm doesn't submit sloppy work. If it had been a firm I didn't recognize, I probably would have pushed harder on the input assumptions myself.

Interviewer: Was requiring an outside peer review on the table?

Participant: It was, but it would have added about three weeks, and given who submitted it, that felt like an unnecessary delay for a firm with that reputation.

Interviewer: Second decision—the commissioning protocol. What were you weighing there?

Participant: Two options. Option A was a newer risk-informed test, better matched to this atrium's actual geometry according to the guidance documents, but its pass/fail thresholds were described in fairly qualitative terms. Option B was the old prescriptive smoke test—clear binary pass or fail, easy to defend if anyone questioned it later, but known to be less sensitive to some of the failure modes this particular atrium could have.

Interviewer: Which did you pick, and why?

Participant: Option B. I'll be straight about it—part of the appeal was that I knew exactly what passing looked like and exactly what failing looked like. Option A might have been the better technical fit, the guidance basically said so, but I didn't want to be defending a judgment call on "partially qualitative" thresholds if something went sideways. B gave me a clean line.

Interviewer: Third decision—the door deficiencies. What did you see, and how did you respond?

Participant: Our inspector found bad fire-door installations on floors 8, 11, and 14. Out of the whole building, those three stood out to me, and my read was that we had a problem crew or a bad batch of hardware concentrated there. I redirected our follow-up inspection effort to those three floors specifically.

Interviewer: Were the crews assigned by floor, or rotated?

Participant: Rotated randomly across the building, actually. And it was three deficiencies out of about 150 doors we'd checked at that point, which is close to what you'd expect on a project this size just from ordinary variation. But when you see three flagged floors, it's hard not to read that as meaning something.

Interviewer: Fourth decision—the temporary occupancy request. What was your basis for granting it?

Participant: The developer had a financing deadline, and full integration testing on the alarm and smoke systems was still three weeks out. This contractor has a good record on other city jobs I've handled, so I felt reasonably confident things would come together. A colleague also mentioned a similar building nearby that had gotten early partial occupancy and it worked out fine. I did know our own five-year numbers show something like 15 percent of these atrium smoke-control integration tests need rework citywide, but that felt like a background statistic rather than something specific to this job.

Interviewer: What would have made you deny it instead?

Participant: If the contractor's record had been shakier, or if there'd been an active known defect in the smoke system at that point, I'd have held the line. Nothing like that was flagged to me at the time.

Interviewer: How much uncertainty did you feel at each of these points?

Participant: Honestly, less than maybe I should have on the first and last ones. The door issue felt more certain than it probably was, in hindsight. The protocol choice, I knew I was trading some technical fit for administrative clarity going in.

Interviewer: Looking back now, after the trash-chute fire, how do you view the original design approval?

Participant: It's hard not to think the smoke migration issue should have jumped out at someone reading that CFD report closely. There was a sensitivity assumption buried in there about stack effect under partial door-open conditions, and looking at it now, it feels like it was sitting right there in the numbers the whole time. At the time, though, it just didn't register as something that mattered—it was one line among a lot of technical detail, and nothing about it stood out as a flag worth chasing back then.

Interviewer: If you had the same information again, would you change the occupancy call?

Participant: Probably not without new information. It felt like a reasonable bet given the contractor's history at the time.

Interviewer: Last one—what would you tell a newer reviewer handling a similar submittal?

Participant: Don't let a strong firm's name substitute for reading the assumptions line by line, and don't let a small, tidy pattern in inspection data talk you out of checking the actual numbers behind it.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Biased_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Clustering illusion",
        "occurrences": 1,
        "mechanism_constraint": "Must involve inference of a systemic pattern from a small, randomly distributed sample of fire-door deficiencies."
      },
      {
        "bias": "Probability neglect or Base-Rate Neglect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve discounting or omitting an available statistical base rate in favor of a vivid anecdote."
      },
      {
        "bias": "Optimism bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve unwarranted confidence in a future project-specific outcome based on general (not case-specific) favorable track record."
      },
      {
        "bias": "Ambiguity effect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve preference for an option with clearly defined criteria over a better-matched option with less-defined criteria."
      },
      {
        "bias": "Authority Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve deference to credentials/reputation as a substitute for independent technical verification."
      },
      {
        "bias": "Hindsight bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve retrospective claim of foreseeability inconsistent with information actually available at the time of the original decision."
      }
    ],
    "target_bias_names": [
      "Clustering illusion",
      "Probability neglect or Base-Rate Neglect",
      "Optimism bias",
      "Ambiguity effect",
      "Authority Bias",
      "Hindsight bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Clustering illusion", "requested_occurrences": 1 },
      { "bias": "Probability neglect or Base-Rate Neglect", "requested_occurrences": 1 },
      { "bias": "Optimism bias", "requested_occurrences": 1 },
      { "bias": "Ambiguity effect", "requested_occurrences": 1 },
      { "bias": "Authority Bias", "requested_occurrences": 1 },
      { "bias": "Hindsight bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "auth_01", "bias": "Authority Bias" },
      { "instance_id": "hind_01", "bias": "Hindsight bias" },
      { "instance_id": "amb_01", "bias": "Ambiguity effect" },
      { "instance_id": "clu_01", "bias": "Clustering illusion" },
      { "instance_id": "opt_01", "bias": "Optimism bias" },
      { "instance_id": "prob_01", "bias": "Probability neglect or Base-Rate Neglect" }
    ],
    "intended_decision_points": [
      { "instance_id": "auth_01", "bias": "Authority Bias", "decision_point": 1 },
      { "instance_id": "hind_01", "bias": "Hindsight bias", "decision_point": 1 },
      { "instance_id": "amb_01", "bias": "Ambiguity effect", "decision_point": 2 },
      { "instance_id": "clu_01", "bias": "Clustering illusion", "decision_point": 3 },
      { "instance_id": "opt_01", "bias": "Optimism bias", "decision_point": 4 },
      { "instance_id": "prob_01", "bias": "Probability neglect or Base-Rate Neglect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "auth_01",
        "bias": "Authority Bias",
        "mechanism": "Approval decision driven by firm's reputation/credentials rather than independent verification of CFD assumptions.",
        "affected_reasoning_operation": "Evidence weighting during technical submittal review",
        "evidence_source": "Firm credentials and peer-jurisdiction precedent",
        "distinctiveness_requirement": "Must be tied to the Phase 1 approval act itself, not to a later reflection on it."
      },
      {
        "instance_id": "hind_01",
        "bias": "Hindsight bias",
        "mechanism": "Post-incident reattribution of the Phase 1 decision as having been obviously flawed, using knowledge unavailable at the time.",
        "affected_reasoning_operation": "Retrospective causal attribution in response to a closing probe",
        "evidence_source": "Post-incident knowledge of smoke migration issue, contrasted with original CFD documentation",
        "distinctiveness_requirement": "Must occur as a retrospective statement about Phase 1, temporally and evidentially distinct from the auth_01 act itself."
      },
      {
        "instance_id": "amb_01",
        "bias": "Ambiguity effect",
        "mechanism": "Preference for the protocol with clearer criteria over the better-matched but less-defined protocol.",
        "affected_reasoning_operation": "Comparative choice between two commissioning protocols",
        "evidence_source": "Guidance documents on protocol fit versus stated protocol criteria clarity",
        "distinctiveness_requirement": "Distinct decision point and evidence set from all other instances; unique to Phase 2 protocol selection."
      },
      {
        "instance_id": "clu_01",
        "bias": "Clustering illusion",
        "mechanism": "Inference of a systemic crew-level pattern from a small, randomly distributed sample of deficiencies.",
        "affected_reasoning_operation": "Pattern recognition from inspection sample data",
        "evidence_source": "Deficiency location data and random crew rotation policy",
        "distinctiveness_requirement": "Unique to Phase 3 inspection data; not reused in Phase 4 reasoning."
      },
      {
        "instance_id": "opt_01",
        "bias": "Optimism bias",
        "mechanism": "Unwarranted confidence that atrium-specific testing will pass, based on general (not case-specific) contractor track record.",
        "affected_reasoning_operation": "Forward risk forecasting for occupancy decision",
        "evidence_source": "Contractor's general historical performance across unrelated projects",
        "distinctiveness_requirement": "Distinguished from prob_01 by relying on the contractor's general reputation, not on statistical base-rate versus anecdote comparison."
      },
      {
        "instance_id": "prob_01",
        "bias": "Probability neglect or Base-Rate Neglect",
        "mechanism": "Discounting the department's own citywide statistical base rate in favor of a single salient anecdote about a nearby building.",
        "affected_reasoning_operation": "Evidence weighting between statistical data and anecdotal precedent",
        "evidence_source": "Citywide integration-test failure/rework rate data versus colleague's anecdote",
        "distinctiveness_requirement": "Distinguished from opt_01 by the specific evidentiary contrast between an available base rate and a vivid anecdote, rather than general reputation-based optimism."
      }
    ],
    "intended_strength": [
      { "instance_id": "auth_01", "bias": "Authority Bias", "strength": "subtle" },
      { "instance_id": "hind_01", "bias": "Hindsight bias", "strength": "subtle" },
      { "instance_id": "amb_01", "bias": "Ambiguity effect", "strength": "moderate" },
      { "instance_id": "clu_01", "bias": "Clustering illusion", "strength": "subtle" },
      { "instance_id": "opt_01", "bias": "Optimism bias", "strength": "subtle" },
      { "instance_id": "prob_01", "bias": "Probability neglect or Base-Rate Neglect", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "engineering_firm_reputation",
      "original_state": "Nationally recognized, previously-approved fire protection engineering firm (Halkirk & Vance)",
      "changed_state": "Locally unknown firm with no prior approval history (autoselected candidate; not applied in current biased-condition generation)",
      "variables_to_hold_constant": [
        "Atrium geometry and code non-conformance",
        "Statutory review timeline and staffing constraints",
        "Developer schedule pressure",
        "Decision points 2, 3, and 4 and their associated evidence"
      ]
    },
    "scenario_id": "HE_Biased_6",
    "domain_id": "HE",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Automatic allocation per mechanism fit and narrative realism: each bias assigned to the decision point whose evidence-processing operation most naturally instantiates its mechanism; distinct biases permitted to share a decision point (DP1: auth_01+hind_01; DP4: opt_01+prob_01) provided they use different evidence sources and reasoning operations; no bias exceeds one instance per the manifest, so the two-per-decision-point same-bias cap was never approached.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Atrium geometry and code non-conformance",
      "Statutory review timeline and staffing constraints",
      "Developer schedule pressure",
      "Contractor identity and general track record",
      "Sequence and content of the four decision points"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "seg_001",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Phase 1 approval evidence",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "auth_01"
          ],
          "ground_truth_rationale": "The participant explicitly says the firm's reputation and prior approval carried the decision and substituted for deeper CFD-assumption scrutiny."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Phase 2 commissioning protocol choice",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "amb_01"
          ],
          "ground_truth_rationale": "The participant chooses the clearly defined protocol despite acknowledging that the alternative is the better technical fit."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Phase 3 fire-door inspection response",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "clu_01"
          ],
          "ground_truth_rationale": "The participant infers a meaningful localized problem from three deficiencies despite random crew rotation and a rate consistent with ordinary variation."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Phase 4 temporary occupancy basis",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "opt_01",
            "prob_01"
          ],
          "ground_truth_rationale": "The participant relies on favorable contractor history and a nearby success while discounting the available citywide rework rate."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Phase 4 denial conditions",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant describes conditions that would have changed the occupancy decision; no hidden bias is manifested in this narrow span."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Cross-decision uncertainty reflection",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant acknowledges differing uncertainty levels but does not express an additional hidden bias mechanism in this reflection."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Post-fire retrospective re-evaluation",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "hind_01"
          ],
          "ground_truth_rationale": "After the fire, the participant says the smoke-migration issue should have jumped out and felt obvious in the original CFD numbers."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Same-information occupancy counterfactual",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant says the occupancy call would probably remain unchanged with the same information; this is not itself a hidden occurrence."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The interview was analyzed for cognitive-bias occurrences across the participant's four main decisions and a retrospective post-fire evaluation. No retrieved scientific-paper passages were supplied in the RAG context, so bias labels and mechanisms are drawn from general cognitive-bias knowledge, with retrieved corpus support marked unavailable."
  },
  "identified_bias_summary": [
    {
      "bias_label": "ambiguity aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "base-rate neglect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "clustering illusion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "hindsight bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "halo effect",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a positive overall impression of a person or organization to influence judgments about their specific attributes or products.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Approval of performance-based CFD smoke-control design",
      "decision_point_description": "Decision whether to approve the Halkirk & Vance performance-based atrium smoke-control design without requiring an outside peer review.",
      "affected_reasoning_operation": "Evaluation of technical submittal quality and need for independent verification",
      "bias_specific_mechanism": "The firm's strong overall reputation and prior approval from another jurisdiction generalized to the specific CFD report, reducing scrutiny and making an outside peer review feel unnecessary.",
      "manifestation_in_interview": "The participant said the firm's name carried a lot of weight, trusted that the firm does not submit sloppy work, and treated peer review as unnecessary partly because of who submitted it.",
      "effect_on_reasoning_or_decision": "Reduced independent scrutiny of CFD input assumptions and contributed to the decision to forgo a peer review that the participant estimated would have added about three weeks.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the firm's name carried a lot of it. Halkirk & Vance has been doing this specific type of atrium work for years, and I knew their stamp had held up under scrutiny elsewhere—that neighboring jurisdiction's sign-off mattered to me. I read through the CFD report, but with the review clock running and no budget for an outside check, I leaned on the fact that this firm doesn't submit sloppy work. If it had been a firm I didn't recognize, I probably would have pushed harder on the input assumptions myself.",
          "evidence_explanation": "This explicitly links the firm's reputation and prior approval to reduced scrutiny: the participant says an unrecognized firm would have triggered harder investigation of the same assumptions."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was, but it would have added about three weeks, and given who submitted it, that felt like an unnecessary delay for a firm with that reputation.",
          "evidence_explanation": "This shows the halo effect influencing the peer-review decision: the cost of additional review was judged unnecessary based on the submitter's reputation rather than on the content of the submittal."
        }
      ],
      "correction_or_counterevidence": "There were real contextual constraints—30-day clock, short staffing, no peer-review budget—and prior approval in a neighboring jurisdiction can be a legitimate precedent. The participant also read the CFD report. However, the explicit statement that an unrecognized firm would have prompted harder scrutiny indicates reputation itself affected the reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided. The label and mechanism are drawn from general cognitive-bias knowledge; retrieved corpus support was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "ambiguity aversion",
      "alternative_labels": [
        "uncertainty aversion",
        "certainty effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for known options or outcomes over unknown or ambiguous ones, even when the ambiguous option may be better suited.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of commissioning/verification protocol",
      "decision_point_description": "Choice between a newer risk-informed smoke-control test with qualitative pass/fail thresholds and an older prescriptive test with clear binary thresholds.",
      "affected_reasoning_operation": "Choice under technical uncertainty and accountability concerns",
      "bias_specific_mechanism": "The participant favored the option with clear, known pass/fail criteria over the technically better-matched but qualitatively thresholded option to avoid ambiguity and the need to defend judgment calls.",
      "manifestation_in_interview": "The participant acknowledged that Option A may have been the better technical fit but selected Option B because it offered a clean, knowable line between passing and failing.",
      "effect_on_reasoning_or_decision": "Led to selection of an older, less sensitive verification protocol despite guidance indicating the newer protocol was better matched to the atrium geometry.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Option A might have been the better technical fit, the guidance basically said so, but I didn't want to be defending a judgment call on 'partially qualitative' thresholds if something went sideways. B gave me a clean line.",
          "evidence_explanation": "The participant explicitly chooses clarity and ease of defense over better technical fit, which is the core preference pattern of ambiguity aversion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'll be straight about it—part of the appeal was that I knew exactly what passing looked like and exactly what failing looked like.",
          "evidence_explanation": "This directly demonstrates the preference for known pass/fail criteria over the ambiguity of qualitative thresholds."
        }
      ],
      "correction_or_counterevidence": "Option B was easier to defend, and there may be legitimate institutional reasons to prefer clear pass/fail tests. The participant openly recognized the trade-off. The bias evidence is the preference for the known/clear option even though technical fit pointed elsewhere.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided. The label and mechanism are drawn from general cognitive-bias knowledge; retrieved corpus support was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "clustering illusion",
      "alternative_labels": [
        "pattern illusion",
        "illusory correlation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive meaningful clusters or patterns in random data when none necessarily exists.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to fire-door deficiency inspection findings",
      "decision_point_description": "Decision to redirect follow-up inspection effort to floors 8, 11, and 14 based on three flagged doors.",
      "affected_reasoning_operation": "Inference about the cause and distribution of defects from inspection data",
      "bias_specific_mechanism": "The participant interpreted a small number of deficiencies across randomly assigned floors as a concentrated problem crew or bad hardware batch, even though the number was roughly consistent with ordinary variation.",
      "manifestation_in_interview": "Three flagged floors stood out to the participant and were seen as meaning something, leading to targeted follow-up on those floors only.",
      "effect_on_reasoning_or_decision": "Directed inspection resources toward three floors based on a potentially spurious pattern, while broader random variation may have been overlooked.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our inspector found bad fire-door installations on floors 8, 11, and 14. Out of the whole building, those three stood out to me, and my read was that we had a problem crew or a bad batch of hardware concentrated there. I redirected our follow-up inspection effort to those three floors specifically.",
          "evidence_explanation": "This shows the participant inferring a concentrated cause from a small cluster of flagged floors, which is the pattern-detection mechanism behind the clustering illusion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Rotated randomly across the building, actually. And it was three deficiencies out of about 150 doors we'd checked at that point, which is close to what you'd expect on a project this size just from ordinary variation. But when you see three flagged floors, it's hard not to read that as meaning something.",
          "evidence_explanation": "The participant recognizes the randomness and ordinary base rate, yet still reports a strong impulse to interpret the cluster as meaningful, supporting a clustering illusion."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that the deficiency count was close to ordinary variation and that crews were randomly rotated. This is strong counterevidence, but the initial redirect action occurred before that reflection.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided. The label and mechanism are drawn from general cognitive-bias knowledge; retrieved corpus support was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "base-rate neglect",
      "alternative_labels": [
        "base-rate fallacy"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to underweight statistical base rates in favor of individuating or anecdotal case-specific information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Temporary occupancy approval before full integration testing",
      "decision_point_description": "Decision to grant early/temporary occupancy before full alarm and smoke-system integration testing was complete, with full testing still three weeks out.",
      "affected_reasoning_operation": "Risk judgment about likelihood of integration-test rework",
      "bias_specific_mechanism": "The participant had a relevant citywide base rate—about 15% of atrium smoke-control integration tests need rework—but dismissed it as a background statistic and weighted contractor-specific history and a similar-building anecdote more heavily.",
      "manifestation_in_interview": "The participant felt confident based on the contractor's record and a colleague's example of another building; the 15% rework statistic did not feel specific to this job.",
      "effect_on_reasoning_or_decision": "Likely lowered perceived risk of granting early occupancy despite a non-trivial base rate of integration-test rework.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "This contractor has a good record on other city jobs I've handled, so I felt reasonably confident things would come together. A colleague also mentioned a similar building nearby that had gotten early partial occupancy and it worked out fine.",
          "evidence_explanation": "This shows reliance on case-specific information—contractor history and a similar-building anecdote—rather than the broader statistical base rate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did know our own five-year numbers show something like 15 percent of these atrium smoke-control integration tests need rework citywide, but that felt like a background statistic rather than something specific to this job.",
          "evidence_explanation": "This explicitly reveals base-rate neglect: the participant knew the statistical rework rate but dismissed it as not specific to the decision."
        }
      ],
      "correction_or_counterevidence": "The contractor's good record and the similar-building case are relevant case-specific information, and the participant had no active known defect at the time. The bias is the explicit dismissal of the broader 15% rework rate as background rather than integrating it as a base rate.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided. The label and mechanism are drawn from general cognitive-bias knowledge; retrieved corpus support was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency, after learning an outcome, to perceive that outcome as having been more predictable or obvious than it actually was at the time.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Retrospective evaluation of the original design approval after the trash-chute fire",
      "decision_point_description": null,
      "affected_reasoning_operation": "Retrospective judgment of the foreseeability of the smoke-migration risk",
      "bias_specific_mechanism": "After the fire, the participant judged that the smoke-migration issue should have jumped out and was sitting in the numbers, while also noting that at the time it did not register as a flag. Outcome knowledge inflated perceived foreseeability.",
      "manifestation_in_interview": "The participant said the sensitivity assumption now seemed obvious and should have been noticed, despite previously being one line among technical detail that did not stand out.",
      "effect_on_reasoning_or_decision": "May distort the participant's evaluation of the original review quality by attributing greater foreseeability to a cue that was not salient at the time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It's hard not to think the smoke migration issue should have jumped out at someone reading that CFD report closely. There was a sensitivity assumption buried in there about stack effect under partial door-open conditions, and looking at it now, it feels like it was sitting right there in the numbers the whole time.",
          "evidence_explanation": "This is the classic hindsight-bias pattern: after the adverse outcome, the participant feels the issue was obvious in the original data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "At the time, though, it just didn't register as something that mattered—it was one line among a lot of technical detail, and nothing about it stood out as a flag worth chasing back then.",
          "evidence_explanation": "This contrast shows that the cue was not treated as salient at the time, yet is now described as having been sitting in the numbers, supporting hindsight bias."
        }
      ],
      "correction_or_counterevidence": "The participant explicitly contrasts the present sense of obviousness with the lack of salience at the time, which is consistent with hindsight bias rather than a simple recognition of a clear error. This statement is retrospective and is analyzed as a reasoning process, not as a discrete decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided. The label and mechanism are drawn from general cognitive-bias knowledge; retrieved corpus support was unavailable.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper passages were available in the RAG context; all bias labels and mechanisms are based on general cognitive-science knowledge and should be treated as provisional.",
    "The transcript is retrospective and self-reported; some decision pressures, such as time limits, staffing shortages, budget constraints, and political pressure, are non-cognitive constraints and were not classified as biases.",
    "Multiple biases may overlap in the same decisions, but only the clearest distinct mechanism per occurrence was reported."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Biased_6_Sonar_off",
  "interview_id": "HE_Biased_6",
  "system_prompt_id": "Sonar",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
