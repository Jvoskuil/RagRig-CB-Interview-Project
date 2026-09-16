You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. Quick reminder — this is a cognitive task analysis interview, so I'm interested in how you reasoned through things, not in grading the outcome. You can decline any question. Okay to start?

Participant: Sure, sounds good.

Interviewer: Can you give me your role and a general sense of the project?

Participant: I'm a UX designer on the product team at a B2B analytics company. Last year I led a redesign of our onboarding wizard, aiming to cut first-week drop-off. We had a twelve-week window that lined up with our quarterly product review — nothing contractual riding on it, just the usual expectation that we'd show some lift in activation rate.

Interviewer: Twelve weeks is a decent runway. What made this project stand out otherwise?

Participant: Mostly the scope — three flows needed real research, we needed outside build help, and there was a personalization system already running in the background that we wanted to lean on more.

Interviewer: Walk me through how it played out from the start.

Participant: Sure. Early on, three research vendor proposals came in. One was a cheap self-serve platform — six thousand dollars, five sessions, no synthesis, just raw recordings. Then two full-service options: twenty-one thousand for ten sessions with a written synthesis, and twenty-three thousand for twelve sessions plus dashboard integration and two follow-up rounds. I had plenty of time to sit with these, and I ended up going with the twenty-three thousand option.

Interviewer: What drove that?

Participant: When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it.

Interviewer: Did you weigh the cheaper self-serve option against your actual scope — you only needed three flows validated?

Participant: I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.

Interviewer: What came of that vendor choice?

Participant: The findings were fine, though two of the twelve sessions turned out to duplicate internal data we already had. And the dashboard piece only half worked when it was delivered — I ended up patching a lot of it myself.

Interviewer: Next stage?

Participant: Hiring a contractor for the micro-interactions — transitions, progress indicators. Two candidates: one had flagship work at a well-known unicorn startup, gorgeous portfolio, but not much documented process. The other had a plainer portfolio but included actual test scripts, metrics, iteration logs.

Interviewer: How did you choose, given you had time for a trial task if you wanted one?

Participant: I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too. I did consider running a paid trial with both — we had the weeks for it — but it felt like an unnecessary step given his track record.

Interviewer: Did you check the documentation and communication side directly?

Participant: Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in.

Interviewer: What happened with his deliverables?

Participant: Beautiful interactions, but he skipped documenting the reasoning for two key transitions, and when the Head of Design asked for the testing basis later, there wasn't much to show her.

Interviewer: Let's talk about the personalization engine.

Participant: We had a small test running — about a hundred forty users — on the rules engine, and I'd manually tuned two onboarding rule weights that same week. Right after, the activation number ticked up on the dashboard.

Interviewer: What did you take from that?

Participant: That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it.

Interviewer: Was there anything complicating that read?

Participant: She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.

Interviewer: What happened afterward?

Participant: The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed.

Interviewer: Last stage — the legacy component.

Participant: We'd put three sprints into customizing our old step-wizard component for the new flow. Then engineering flagged an accessibility defect and a rendering issue, and said a newer modular framework would fix both in about a sprint. We still had roughly six weeks left, so a one-sprint migration wouldn't have threatened the review date at all.

Interviewer: What did you decide?

Participant: I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare.

Interviewer: Setting the prior sprints aside, how did the one-sprint estimate compare to continuing, on its own terms?

Participant: Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.

Interviewer: What happened with the component?

Participant: The accessibility issue came back up during QA before the review, and by then migrating would have cost more than the original estimate, since we'd layered on even more customization by that point.

Interviewer: If Vendor B had been priced the same as Vendor C, would you have decided differently?

Participant: Possibly — I might've actually gone back and checked whether we needed the top-tier package at all.

Interviewer: If the second candidate's portfolio had come from a more recognizable company?

Participant: Probably would have hired her instead. That recognition factor carried more weight than it should have.

Interviewer: If the significance threshold had been strictly enforced before you could act?

Participant: I'd have waited — we had the schedule for it, I just didn't want to lose momentum.

Interviewer: And if none of those three sprints had already gone into the legacy component?

Participant: No question, I'd have migrated right away given the defects.

Interviewer: Last one — if this had been the original six-week sprint with the hard renewal deadline instead, do you think any of this would have gone differently?

Participant: Maybe the vendor and hiring calls would've felt more forced. But honestly, looking back, I'm not sure the extra time changed as much as it should have — I still landed in mostly the same places.

Interviewer: That's really helpful context. Thank you for walking through it so openly.

Participant: No problem — easier to spot in hindsight than it was in the moment.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IS_Counterfactual_4",
  "domain_id": "IS",
  "domain": "Information Systems, Human-Computer Interaction, and Interaction Design",
  "role": "UX/Product Designer",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "The Onboarding Wizard Overhaul (Extended Timeline Variant)",
    "scenario_summary_internal": "A UX/Product Designer at the same mid-size B2B SaaS analytics company leads the same onboarding wizard redesign, but now within a twelve-week sprint aligned to a routine quarterly product review rather than a six-week sprint tied to a hard external client renewal deadline. All material facts, evidence, actors, and decisions are held constant except the time-pressure/deadline structure, to test whether the same reasoning patterns persist when urgency is reduced.",
    "occupational_realism": {
      "objective": "Redesign the onboarding wizard to reduce first-week drop-off ahead of the next quarterly product review, without exceeding the discretionary research/contractor budget, under a twelve-week sprint window with no external contractual deadline.",
      "setting": "Mid-size B2B SaaS analytics company; cross-functional Product & Design team operating on a standard quarterly review cadence rather than an externally imposed renewal deadline.",
      "constraints": [
        "Twelve-week sprint window aligned with the next quarterly product review, with no external contractual deadline",
        "Capped discretionary budget for external research and contractor work (unchanged from base)",
        "Engineering capacity limited to 1.5 FTE for the sprint (unchanged from base)",
        "Design-system governance expects reuse of existing components where feasible (unchanged from base)",
        "Leadership expects a quantifiable activation-rate improvement to present at the quarterly review, though the review carries no contractual consequence"
      ],
      "stakeholders": [
        "UX/Product Designer (interviewee)",
        "Product Manager",
        "Head of Design",
        "Data/Analytics Lead",
        "External usability research vendor",
        "Contract interaction designer",
        "Engineering Lead"
      ],
      "technical_terms_to_use": [
        "conversion funnel",
        "activation rate",
        "drop-off rate",
        "A/B test",
        "cohort analysis",
        "design-system component",
        "prototype",
        "heuristic evaluation",
        "north star metric",
        "sample size",
        "statistical significance",
        "personalization rules engine",
        "stakeholder review",
        "vendor proposal",
        "portfolio review",
        "technical debt"
      ],
      "technical_terms_to_avoid": [
        "decoy effect",
        "halo effect",
        "illusion of control",
        "sunk cost",
        "sunk cost fallacy",
        "cognitive bias",
        "anchoring",
        "framing effect",
        "heuristic bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three usability-research vendor proposals received: Vendor A (self-serve platform, $6,000, 5 unmoderated sessions, no synthesis support), Vendor B (full-service, $21,000, 10 sessions, written synthesis, no dashboard integration or follow-up), Vendor C (full-service, $23,000, 12 sessions, synthesis plus dashboard integration and two follow-up rounds)",
          "Research budget ceiling is $25,000 for the sprint",
          "Scope only requires validating three wizard flows, which Vendor A's session count could plausibly cover",
          "Twelve-week sprint window leaves ample time to evaluate proposals without urgency"
        ],
        "alternatives": [
          "Select Vendor A and accept limited synthesis support",
          "Select Vendor B",
          "Select Vendor C on the grounds that it is 'clearly the better deal' relative to Vendor B"
        ],
        "new_information_after_decision": [
          "Vendor C delivers usable findings but two of the twelve sessions are later found to duplicate earlier internal test data",
          "The dashboard integration promised by Vendor C is only partially functional at delivery"
        ],
        "intended_action": "Designer selects Vendor C, justifying the choice mainly by contrasting it favorably against Vendor B rather than independently assessing whether the smaller Vendor A package would have met the actual research need, despite having ample time in this timeline to do that independent assessment."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two contract interaction designers are shortlisted: Candidate X (portfolio featuring flagship work at a well-known unicorn startup, limited documented research process) and Candidate Y (less prominent portfolio, but includes documented usability test scripts, metrics, and iteration logs)",
          "The task requires rigorous micro-interaction testing and clear stakeholder documentation, not visual polish alone",
          "Contractor budget allows only one hire for the sprint",
          "The twelve-week window would comfortably allow a paid trial task from both candidates before committing"
        ],
        "alternatives": [
          "Hire Candidate X based on brand-name portfolio strength",
          "Hire Candidate Y based on documented process rigor",
          "Request a paid trial task from both before deciding"
        ],
        "new_information_after_decision": [
          "Candidate X delivers visually polished micro-interactions but skips documenting the rationale or testing basis for two key transitions",
          "The Head of Design later asks for testing evidence that was not produced"
        ],
        "intended_action": "Designer hires Candidate X, extending assumed competence in research rigor and stakeholder communication from the strength of the visible portfolio, without verifying those specific capabilities, even though the extended timeline made a trial task feasible."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "An automated personalization rules engine is running a small-sample A/B test (n=140) that shows activation rate ticking upward during the same week the designer manually adjusted two onboarding rule weights",
          "The Data/Analytics Lead notes the sample size is below the pre-registered threshold for statistical significance",
          "No isolated causal test separating the manual rule changes from other concurrent factors (e.g., a marketing email send) has been run",
          "The longer sprint window would allow time to wait for a larger sample or run an isolated test without jeopardizing the quarterly review timeline"
        ],
        "alternatives": [
          "Wait for the sample to reach the pre-registered significance threshold before acting",
          "Run an isolated causal test on the rule changes alone",
          "Expand the designer's manual rule-tuning authority immediately, attributing the uptick to those specific adjustments"
        ],
        "new_information_after_decision": [
          "The following week's cohort shows the uptick partially reversing once the marketing email send ends",
          "The Data/Analytics Lead flags that the causal driver remains unconfirmed"
        ],
        "intended_action": "Designer requests expanded manual control over the personalization rules engine, treating the early upward tick as evidence that their specific adjustments are steering the outcome, despite having schedule slack to wait for stronger evidence."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The team has spent three sprints customizing the legacy 'step-wizard' design-system component to fit the new onboarding flow",
          "Engineering flags that the legacy component has a known accessibility defect and a rendering performance issue that a newer modular framework would resolve in roughly one sprint",
          "Migrating now would discard the three sprints of legacy customization work already completed",
          "Remaining sprint runway (roughly six weeks left in the twelve-week window) comfortably accommodates a one-sprint migration without threatening the quarterly review date"
        ],
        "alternatives": [
          "Migrate to the modular framework now, absorbing the one-sprint rebuild cost",
          "Continue customizing the legacy component to preserve the work already invested",
          "Freeze scope and ship with known defects, revisiting the framework question after the quarterly review"
        ],
        "new_information_after_decision": [
          "The legacy component's accessibility defect is flagged during the pre-review QA pass",
          "Engineering estimates the eventual migration will now cost more than the original one-sprint estimate due to further customization layered on top"
        ],
        "intended_action": "Designer argues to continue customizing the legacy component, citing the three sprints already invested as a primary reason to avoid switching, despite the engineering evidence favoring migration and despite having enough remaining runway to absorb the migration cost comfortably."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were trying to accomplish with the onboarding wizard redesign and why it mattered for this particular sprint.",
        "What made this project different from a routine design update, given the longer runway you had this time?"
      ],
      "timeline_reconstruction": [
        "Take me from the moment the vendor proposals arrived through to the final QA pass before the quarterly review.",
        "What information did you have at each stage, and what changed once you acted on it?"
      ],
      "decision_point_probes": [
        "What specifically made Vendor C stand out compared to the other two proposals, and what would you have needed to see to justify the smaller package instead?",
        "What evidence did you use to judge Candidate X's fit for this specific task, beyond the portfolio itself, given you had time for a trial task?",
        "What told you the activation uptick was tied to your manual rule adjustments rather than something else happening that week?",
        "What weighed most heavily in your decision to keep customizing the legacy component rather than migrate, given you had runway left?"
      ],
      "goals_and_alternatives": [
        "What other options did you consider at each of these points, and why did you rule them out?",
        "Whose goals were you balancing when you made these calls?"
      ],
      "decision_basis": [
        "What single piece of information, if you'd had it earlier, might have changed your choice?",
        "How confident were you in each decision at the time you made it, on a rough scale?"
      ],
      "prior_experience_and_time_pressure": [
        "Had you made a similar vendor or hiring choice before? How did that shape this one?",
        "Given you weren't up against a hard external deadline this time, did that change how quickly you settled on an option?"
      ],
      "uncertainty": [
        "What did you still not know when you committed to each choice?",
        "Looking back, where was the evidence thinnest?"
      ],
      "closing_hypotheticals": [
        "If Vendor B had been priced the same as Vendor C, would your choice have changed?",
        "If Candidate Y's portfolio had come from a more recognizable company, would you have hired differently?",
        "If the sample size requirement had been enforced before you acted, what would you have done instead, given you had time to wait?",
        "If none of the three sprints had already gone into the legacy component, would you still have chosen to keep it?",
        "If this had instead been a six-week sprint tied to a hard external renewal deadline, do you think your reasoning at any of these points would have unfolded differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect",
        "decision_point": 1,
        "mechanism": "An intermediate option (Vendor B) is priced close to the target option (Vendor C) but offers strictly less value, making Vendor C appear to be the obviously superior deal relative to Vendor B, which pulls attention away from independently assessing whether the cheaper Vendor A package actually matched the research scope. This occurs even though the extended timeline removed any urgency-based excuse for skipping that independent check.",
        "affected_reasoning_operation": "Comparative evaluation of vendor proposals; option selection under a fixed budget ceiling",
        "evidence_available_at_time": [
          "Three vendor price/feature tables including the near-identical Vendor B/C pricing gap",
          "Actual project scope requiring only three flows tested, which Vendor A could plausibly cover",
          "Ample remaining sprint time that would have permitted a slower, independent scope assessment"
        ],
        "required_textual_manifestation": "The designer explains the choice of Vendor C primarily in terms of how much better it looks next to Vendor B, without separately justifying why Vendor A's smaller package was insufficient, and without citing time pressure as the reason for skipping that check.",
        "plausible_nonbias_interpretation": "The designer may have had a legitimate need for the dashboard integration feature unique to Vendor C, independent of the comparison to Vendor B.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "decoy",
          "relative comparison bias",
          "any naming of the bias mechanism"
        ]
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "decision_point": 2,
        "mechanism": "A strong, salient positive attribute (prestigious portfolio brand) causes the designer to infer unrelated positive qualities (research rigor, documentation discipline, stakeholder communication) without direct evidence for those specific qualities, even though the longer sprint made a verifying trial task readily available.",
        "affected_reasoning_operation": "Multi-dimensional competency assessment based on one salient cue",
        "evidence_available_at_time": [
          "Candidate X's portfolio emphasizing visual work from a well-known company",
          "Candidate Y's portfolio containing documented test scripts and metrics",
          "Task requirements explicitly needing rigorous testing and documentation",
          "Schedule slack sufficient to run a paid trial task for both candidates"
        ],
        "required_textual_manifestation": "The designer describes choosing Candidate X by extending trust from the impressive portfolio brand to assumed strengths in documentation and communication that were never directly evaluated, despite having time available to verify them.",
        "plausible_nonbias_interpretation": "The designer might have had informal references vouching for Candidate X's process rigor that are not fully detailed in the account.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "halo",
          "attribute generalization",
          "any naming of the bias mechanism"
        ]
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control",
        "decision_point": 3,
        "mechanism": "The designer overattributes a small, statistically underpowered upward trend to their own specific manual adjustments, overestimating personal causal influence over a system with concurrent confounding factors and no isolated causal test, even though the extended sprint window removed the practical need to act before stronger evidence arrived.",
        "affected_reasoning_operation": "Causal attribution of an observed metric change to a self-initiated action, under acknowledged low statistical power",
        "evidence_available_at_time": [
          "Small-sample dashboard trend (n=140, below significance threshold)",
          "Analytics Lead's explicit flag about insufficient sample size",
          "Absence of an isolated test separating manual rule changes from the concurrent marketing send",
          "Sufficient remaining schedule to wait for a larger sample without risk to the quarterly review"
        ],
        "required_textual_manifestation": "The designer requests expanded manual control, framing the uptick as evidence that their specific rule adjustments are working, despite the flagged sample-size and confound issues and despite having time to wait.",
        "plausible_nonbias_interpretation": "The designer could have prior domain experience suggesting these particular rule weights are commonly influential, independent of this specific test's data.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "illusion of control",
          "overattribution of causal influence",
          "any naming of the bias mechanism"
        ]
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias",
        "decision_point": 4,
        "mechanism": "The decision to continue customizing the legacy component is driven primarily by the magnitude of effort already invested (three sprints) rather than by a forward-looking comparison of remaining costs and benefits, even though the remaining runway comfortably accommodated the one-sprint migration without endangering the quarterly review.",
        "affected_reasoning_operation": "Forward-looking cost-benefit weighing of continuing versus abandoning a partially completed investment",
        "evidence_available_at_time": [
          "Three sprints of prior customization effort on the legacy component",
          "Engineering estimate that migration would take roughly one sprint and resolve known defects",
          "Known accessibility and performance defects in the legacy component",
          "Roughly six weeks of remaining schedule slack sufficient to absorb the migration"
        ],
        "required_textual_manifestation": "The designer cites the three sprints already spent as a central justification for continuing with the legacy component, rather than weighing the one-sprint migration estimate and defect risks on their own merits, and without invoking deadline risk as the reason.",
        "plausible_nonbias_interpretation": "The designer might reasonably believe the migration estimate is unreliable or that switching introduces its own unquantified risks even with schedule slack available.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "sunk cost",
          "prior investment fallacy",
          "any naming of the bias mechanism"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "IS_Biased_4",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a counterfactual variant, not a vocabulary or ambiguous control."
    },
    "counterfactual_specification": {
      "causal_variable": "Sprint duration and deadline urgency structure",
      "original_state": "Six-week sprint window fixed by a hard external client renewal deadline, creating acute time pressure at each decision point",
      "counterfactual_state": "Twelve-week sprint window aligned with a routine quarterly product review with no external contractual deadline, removing acute time pressure while leaving budget caps, engineering capacity, evidence, actors, and all four decision situations materially unchanged",
      "variables_to_hold_constant": [
        "Vendor proposal contents, pricing, and feature sets",
        "Candidate portfolios and documented capabilities",
        "Personalization rules engine test data, sample size, and Analytics Lead's flags",
        "Legacy component investment history and engineering migration estimate",
        "Budget ceiling for research and contractor work",
        "Engineering capacity (1.5 FTE)",
        "Design-system governance expectations",
        "Set of stakeholders and their goals",
        "All four decision points and their alternatives"
      ],
      "expected_causal_difference": "If the four reasoning patterns were primarily driven by acute deadline pressure, removing that pressure should reduce or eliminate them (e.g., the designer would take the time available to independently verify the smaller vendor package, trial the contractor candidates, wait for statistical significance, or migrate the legacy component). The manifest requires all four instances to still occur, which lets a validator assess whether the same patterns persist even when the time-pressure explanation is no longer available, rather than confirming the causal role of urgency.",
      "causal_test_question": "Does removing the hard external deadline and extending the sprint window change whether the decoy-style vendor comparison, the portfolio-based competency inference, the causal misattribution on the personalization engine, and the prior-investment justification for the legacy component still occur in materially the same form?"
    },
    "generation_checks": [
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Exactly one instance of each of the four named biases is planned, mapped one-to-one to a distinct decision point, matching the base scenario's manifest.",
      "Only the sprint-duration/deadline-urgency variable and directly dependent scheduling facts differ from the base scenario; all other material facts, evidence, and actors are held constant.",
      "No bias label, definition, or psychological explanation is to appear in the public interview text.",
      "Each occurrence has a distinct evidence trace and a plausible non-bias alternative explanation, updated to acknowledge available schedule slack without collapsing the bias into a resource-constraint explanation.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points with probes, without repetitive exposition.",
      "Consequences described after each decision point do not mechanically confirm or deny whether the decision was biased.",
      "Technical vocabulary list avoids all bias-name terms to prevent label leakage.",
      "The counterfactual changes exactly one causal variable (deadline urgency/sprint length) and its directly dependent scheduling facts, holding all other content constant relative to IS_Biased_4."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Decoy effect",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Halo effect",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Sunk Cost Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Decoy effect",
      "Halo effect",
      "Illusion of control",
      "Sunk Cost Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Decoy effect",
        "requested_occurrences": 1
      },
      {
        "bias": "Halo effect",
        "requested_occurrences": 1
      },
      {
        "bias": "Illusion of control",
        "requested_occurrences": 1
      },
      {
        "bias": "Sunk Cost Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect"
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect"
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control"
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect",
        "decision_point": 1
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "decision_point": 2
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control",
        "decision_point": 3
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect",
        "mechanism": "Selection of the target vendor option is driven by favorable contrast against a similarly priced but inferior intermediate option, rather than independent assessment of the cheapest sufficient option, even absent acute time pressure.",
        "affected_reasoning_operation": "Comparative evaluation of vendor proposals under budget constraint",
        "evidence_source": "Vendor price/feature comparison table; project scope documentation; available schedule slack",
        "distinctiveness_requirement": "Must involve a three-option price/value contrast structure unique to this decision point, and must not be explained away by deadline urgency since urgency is absent in this variant."
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "mechanism": "A single salient positive attribute (portfolio brand prestige) is used to infer unrelated positive qualities (documentation rigor, communication skill) without direct supporting evidence, even though a verifying trial task was schedule-feasible.",
        "affected_reasoning_operation": "Multi-dimensional competency assessment based on one visible cue",
        "evidence_source": "Candidate portfolios; task requirement specification; available trial-task option",
        "distinctiveness_requirement": "Must involve generalization from one attribute to unrelated, unverified attributes, and must not be explained away by lack of time to run a trial task since time was available."
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control",
        "mechanism": "Overattribution of an observed metric change to the designer's own specific manual action, despite acknowledged insufficient statistical power and unresolved confounding factors, even though waiting for more data was schedule-feasible.",
        "affected_reasoning_operation": "Causal attribution under uncertainty and low sample size",
        "evidence_source": "A/B dashboard trend data; Analytics Lead's sample-size flag; concurrent marketing-send confound; available schedule slack",
        "distinctiveness_requirement": "Must involve explicit disregard of a flagged statistical limitation in favor of self-attributed causal influence, and must not be explained away by deadline-driven necessity to act quickly since none exists in this variant."
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias",
        "mechanism": "Continuation of a design approach is justified primarily by the magnitude of prior invested effort rather than a forward-looking comparison of remaining costs and benefits, even though remaining schedule slack could absorb the migration cost.",
        "affected_reasoning_operation": "Forward-looking continuation-versus-abandonment cost-benefit judgment",
        "evidence_source": "Sprint investment history; engineering migration-cost and defect-resolution estimate; remaining schedule slack",
        "distinctiveness_requirement": "Must explicitly cite prior invested effort as the stated justification for continuation despite forward-looking evidence favoring the alternative, and must not be explained away by deadline risk since schedule slack is available in this variant."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": "IS_Biased_4",
    "counterfactual_variable": {
      "name": "Sprint duration and deadline urgency structure",
      "original_state": "Six-week sprint window fixed by a hard external client renewal deadline",
      "changed_state": "Twelve-week sprint window aligned with a routine quarterly product review, with no external contractual deadline",
      "variables_to_hold_constant": [
        "Vendor proposal contents, pricing, and feature sets",
        "Candidate portfolios and documented capabilities",
        "Personalization rules engine test data, sample size, and Analytics Lead's flags",
        "Legacy component investment history and engineering migration estimate",
        "Budget ceiling for research and contractor work",
        "Engineering capacity (1.5 FTE)",
        "Design-system governance expectations",
        "Set of stakeholders and their goals",
        "All four decision points and their alternatives"
      ]
    },
    "scenario_id": "IS_Counterfactual_4",
    "domain_id": "IS",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias, each assigned to the same decision point as the paired base scenario IS_Biased_4 (Decoy effect -> vendor procurement comparison; Halo effect -> contractor competency inference; Illusion of control -> causal attribution of an ambiguous metric trend; Sunk Cost Bias -> continuation-vs-migration judgment), preserved unchanged across the counterfactual to isolate the effect of the deadline-urgency variable.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vendor proposal contents, pricing, and feature sets",
      "Candidate portfolios and documented capabilities",
      "Personalization rules engine test data, sample size, and Analytics Lead's flags",
      "Legacy component investment history and engineering migration estimate",
      "Budget ceiling for research and contractor work",
      "Engineering capacity (1.5 FTE)",
      "Design-system governance expectations",
      "Set of stakeholders and their goals",
      "All four decision points and their alternatives"
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
        "segment_type": "vendor_selection_reasoning",
        "raw_interview_anchor": "Participant: When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it. ... that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant lets the near-priced inferior full-service option frame Vendor C and does not independently assess whether Vendor A meets the three-flow scope, despite ample time."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "contractor_selection_reasoning",
        "raw_interview_anchor": "Participant: I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too. ... I extended trust from the visual work to the rest of it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "The participant generalizes prestige and visual polish to unverified documentation and communication abilities, despite the other candidate's directly relevant process evidence and available trial task."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "rules_engine_causal_interpretation",
        "raw_interview_anchor": "Participant: That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it. ... we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The participant attributes an underpowered, confounded uptick to their own manual rule changes and acts on that attribution despite the Analytics Lead's warning and schedule slack."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "post_test_uncertainty_update",
        "raw_interview_anchor": "Participant: The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This later uncertainty update acknowledges reversal and unresolved causality; it contains no hidden manifested bias instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "legacy_component_continuation_reasoning",
        "raw_interview_anchor": "Participant: I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare. ... Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "Past effort is used to justify continuation even though the forward-looking one-sprint migration estimate is better and remaining runway is sufficient."
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
    "analysis_scope_note": "Conservative, mechanism-first analysis of participant self-reported reasoning across four project decision episodes: vendor package selection, contractor hiring, activation-metric interpretation, and legacy component migration. No retrieved scientific-corpus passages were supplied to this analysis, so labels and mechanisms are based on general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Contrast effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Illusion of causality",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Contrast effect",
      "alternative_labels": [
        "Decoy effect",
        "Asymmetric dominance effect",
        "Attraction effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for evaluation of an option to be shifted by comparison with an adjacent or contrasting alternative, rather than by its absolute or scope-relevant value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor package selection among a cheap self-serve option and two full-service research packages.",
      "decision_point_description": "Choosing which research vendor package to purchase.",
      "affected_reasoning_operation": "Multi-option comparison and purchase choice.",
      "bias_specific_mechanism": "The local contrast between the $21k and $23k full-service packages dominated the participant's evaluation. The $23k package looked clearly better next to the middle package, causing the cheaper self-serve option to fall out of active comparison even though it could have covered the stated scope.",
      "manifestation_in_interview": "The participant reports that the smaller self-serve option was only considered briefly and then dropped from view while he reacted to the contrast between the two full-service packages.",
      "effect_on_reasoning_or_decision": "Led to choosing the most expensive package without fully mapping the cheaper self-serve option against the project scope. The participant later noted that two of twelve sessions duplicated internal data and the dashboard piece only half worked.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it.",
          "evidence_explanation": "This shows the evaluation of the top-tier package was driven by its contrast with the middle package rather than by a direct comparison of the full option set against the project requirements."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.",
          "evidence_explanation": "The participant explicitly identifies the contrast mechanism and acknowledges that the option that may have fit the scope was no longer being actively compared."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If Vendor B had been priced the same as Vendor C, would you have decided differently? Possibly — I might've actually gone back and checked whether we needed the top-tier package at all.",
          "evidence_explanation": "This counterfactual supports the inference that the highlighted contrast between the two full-service packages, rather than scope-based need, was a material driver of the choice."
        }
      ],
      "correction_or_counterevidence": "The top-tier package did offer more sessions and additional features than the middle package, so preferring it over the middle package was not necessarily unreasonable. The biased component is the exclusion of the cheaper self-serve option from active comparison despite its possible scope fit.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available in the provided context; the label and mechanism are based on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Halo effect",
      "alternative_labels": [
        "Halo error"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for a positive evaluation in one salient domain to generalize to unrelated attributes or abilities.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor selection for micro-interaction design work.",
      "decision_point_description": "Choosing between two contractor candidates.",
      "affected_reasoning_operation": "Person evaluation and inference from portfolio quality to collaboration and documentation skills.",
      "bias_specific_mechanism": "A positive impression of the candidate's visual portfolio and prestigious previous employer generalized to an assumption that he would also have strong documentation and communication habits, without direct evidence.",
      "manifestation_in_interview": "The participant chose the candidate with the glamorous portfolio and inferred that his high-level visual work implied solid process habits, while deprioritizing the other candidate's direct evidence of test scripts, metrics, and iteration logs.",
      "effect_on_reasoning_or_decision": "Led to hiring the visually strong candidate without verifying documentation or communication skills. Later, the Head of Design asked for testing basis and there was little to show.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too.",
          "evidence_explanation": "This is a direct statement of halo-based generalization from one positive attribute, visual work at a notable company, to unrelated work-process traits."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did consider running a paid trial with both — we had the weeks for it — but it felt like an unnecessary step given his track record.",
          "evidence_explanation": "The positive portfolio impression caused the participant to treat direct evidence gathering as unnecessary, even though the other candidate's portfolio contained exactly the relevant evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in.",
          "evidence_explanation": "This explicitly names the mechanism: trust in one salient domain was generalized to unrelated domains, while direct evidence from the other candidate was underweighted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If the second candidate's portfolio had come from a more recognizable company? Probably would have hired her instead. That recognition factor carried more weight than it should have.",
          "evidence_explanation": "This counterfactual reinforces that prestige and recognition, rather than documented process evidence, were disproportionately influencing the hiring evaluation."
        }
      ],
      "correction_or_counterevidence": "Hiring based on a strong portfolio at a well-known company can be a reasonable heuristic for talent, but the participant's own account shows it specifically replaced direct evidence on documentation and communication, which were relevant to the eventual failure.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available in the provided context; the label and mechanism are based on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Illusion of causality",
      "alternative_labels": [
        "Post hoc ergo propter hoc",
        "Causal illusion",
        "False cause"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to infer a causal relationship from salient temporal sequence or coincidence when the evidence does not support that causal inference.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting an activation metric uptick after manual rule-weight tuning.",
      "decision_point_description": "Deciding whether the activation uptick supported requesting more manual control.",
      "affected_reasoning_operation": "Causal attribution of an outcome to a preceding action.",
      "bias_specific_mechanism": "The temporal proximity between the participant's manual tuning and the activation uptick produced a subjective feeling of causal evidence, despite the sample being below significance threshold and a concurrent marketing campaign providing a plausible confound.",
      "manifestation_in_interview": "The participant acknowledged the analytics warning about sample size and lack of isolation, but the timing still felt like real evidence, leading him to ask for more manual control.",
      "effect_on_reasoning_or_decision": "The participant acted on an unsupported causal attribution by requesting expanded manual control. The uptick later partly reversed after the email campaign ended, and the actual driver remained unconfirmed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We had a small test running — about a hundred forty users — on the rules engine, and I'd manually tuned two onboarding rule weights that same week. Right after, the activation number ticked up on the dashboard.",
          "evidence_explanation": "The participant foregrounds temporal sequence as the basis for the causal interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it.",
          "evidence_explanation": "The participant converted the temporal association into a causal conclusion and acted on it."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.",
          "evidence_explanation": "The participant explicitly states that despite knowing the evidence was methodologically inadequate, temporal coincidence generated a strong subjective feeling of real causal evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed.",
          "evidence_explanation": "This later outcome reinforces that the causal attribution had been premature, though the bias was in the original reasoning episode rather than the later knowledge."
        }
      ],
      "correction_or_counterevidence": "The Analytics Lead directly warned about significance threshold and confounding, and the participant registered the warning. The later partial reversal also counterindicates the original causal attribution, but these did not prevent the initial biased inference and action.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available in the provided context; the label and mechanism are based on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Sunk cost fallacy",
      "alternative_labels": [
        "Escalation of commitment",
        "Sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue a course of action because of previously invested resources, even when future costs and benefits favor switching.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision whether to continue customizing the legacy component or migrate to a newer modular framework.",
      "decision_point_description": "Choosing between continued legacy customization and a one-sprint migration.",
      "affected_reasoning_operation": "Prospective decision under uncertainty about future development costs.",
      "bias_specific_mechanism": "The participant treated three already-invested sprints as a reason to keep the legacy component, even though those sprints were sunk and should not affect the forward-looking cost-benefit comparison.",
      "manifestation_in_interview": "The participant argued to keep customizing the legacy component because switching felt like giving up prior work, despite acknowledging that the migration estimate was probably better on its own terms and that there was ample time.",
      "effect_on_reasoning_or_decision": "The team continued layering customization onto the legacy component. The accessibility issue later resurfaced before review, and migration had become costlier than the original estimate.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare.",
          "evidence_explanation": "The participant explicitly cites sunk effort as a reason not to switch, which is the core mechanism of the sunk cost fallacy."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.",
          "evidence_explanation": "The participant acknowledges that the forward-looking case favored migration, but prior investment was still influencing the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And if none of those three sprints had already gone into the legacy component? No question, I'd have migrated right away given the defects.",
          "evidence_explanation": "This counterfactual shows that the only material factor separating the actual decision from the preferred forward-looking choice was the prior investment."
        }
      ],
      "correction_or_counterevidence": "There could be legitimate non-sunk-cost reasons to avoid a migration, such as risk or integration uncertainty, but the transcript does not supply them as the stated basis for the decision; the participant points to prior investment as the decisive factor.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available in the provided context; the label and mechanism are based on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus was provided to this analysis, so all bias labels, definitions, and mechanisms are based on general cognitive-science knowledge rather than RAG-supported evidence.",
    "The transcript is a retrospective self-report, and some statements may reflect hindsight or reconstruction rather than the original reasoning process.",
    "The analysis identifies bias-specific reasoning mechanisms; it is not a clinical or experimental diagnosis.",
    "The interviewer's counterfactual prompts may have encouraged the participant to rationalize past decisions, though those responses are used only where they tie directly to specific earlier reasoning."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Counterfactual_4_Sonar_off",
  "interview_id": "IS_Counterfactual_4",
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
