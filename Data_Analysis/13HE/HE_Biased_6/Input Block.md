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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
