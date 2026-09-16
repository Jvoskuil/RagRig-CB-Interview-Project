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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
