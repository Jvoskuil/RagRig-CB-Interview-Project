<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through a specific project, not whether the outcome was good or bad. Everything you share stays with the research team, and you can skip anything you'd rather not discuss. Sound okay?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role and give me a general sense of the project we're going to talk about?

Participant: Sure, I'm a UX designer on the product team at an analytics SaaS company. Back in Q4 we had a six-week window to redesign our onboarding wizard before a big client renewal review. Leadership wanted to see a real bump in activation rate going into that meeting, so there was a lot riding on it.

Interviewer: What made this project different from a routine update?

Participant: Normally we'd have more runway — like a full quarter. This one was compressed, and the budget for outside help was capped, so every dollar and every hour had to be justified. Engineering could only give us maybe one and a half people. It was tight.

Interviewer: Walk me through how it unfolded, from the start.

Participant: So the first thing on my plate was research. We knew the wizard's drop-off was concentrated in three flows, and I needed outside eyes on it fast. I got three vendor proposals in the same week. One was a cheap self-serve platform, six grand, five sessions, but basically no synthesis — you get raw recordings and that's it. Then there were two full-service options: one at twenty-one thousand for ten sessions with a written synthesis, and another at twenty-three for twelve sessions plus dashboard integration and two follow-up rounds. I ended up going with the twenty-three thousand one.

Interviewer: What tipped it that direction?

Participant: Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. For two grand more you got two more sessions, the dashboard hookup, and follow-ups baked in. The middle option just looked like a worse version of the top one at almost the same price. It felt like an easy call.

Interviewer: Did you look closely at whether the cheaper self-serve option would've covered what you actually needed?

Participant: I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from.

Interviewer: Got it. What happened after you picked that vendor?

Participant: The findings were usable, but we later realized two of the twelve sessions basically repeated data we already had internally. And the dashboard integration they promised only half worked at delivery, so I had to patch a lot of that manually anyway.

Interviewer: Let's move to the next stage. What came after research?

Participant: We needed a contractor to build the actual micro-interactions for the new flow — transitions, progress indicators, that kind of thing. Two candidates were shortlisted. One, let's call him Candidate X, had done flagship interaction work at a pretty well-known unicorn startup — gorgeous portfolio. The other, Candidate Y, had a less flashy portfolio but included actual test scripts, metrics, iteration logs, the whole documented process.

Interviewer: What made you choose between them?

Participant: I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. It seemed like a safe bet given where he'd come from.

Interviewer: Did you verify that documentation and communication piece directly — maybe ask for writing samples or how he'd handled testing on past projects?

Participant: Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall.

Interviewer: How did that play out?

Participant: The micro-interactions themselves were beautiful. But he skipped documenting the reasoning behind two key transitions, and when the Head of Design asked for the testing basis, there wasn't really anything to show her.

Interviewer: Let's talk about the third stage — the personalization engine.

Participant: Right, so in parallel we were running a small test on the rules engine — about a hundred forty users — and I'd manually adjusted two of the onboarding rule weights that same week. The activation numbers on the dashboard ticked up right after.

Interviewer: What did you make of that?

Participant: I took it as a sign the adjustments were working. I went to the Data lead and asked to expand my manual tuning authority so I could keep pushing on it before the renewal review.

Interviewer: Was there anything at the time that complicated that read?

Participant: She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver.

Interviewer: What happened the following week?

Participant: The uptick partly reversed once the email campaign ended, and she noted the causal driver was still unconfirmed. So it's genuinely unclear how much of that first bump was actually the rule changes.

Interviewer: Last stage — tell me about the legacy component decision.

Participant: We'd spent three sprints customizing our old step-wizard component to fit the new flow. Then engineering flagged an accessibility defect and a rendering performance issue, and said a newer modular framework would fix both in about a sprint.

Interviewer: What did you decide?

Participant: I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us.

Interviewer: Setting aside the sprints already spent, how did the one-sprint migration estimate compare on its own terms to continuing?

Participant: If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built.

Interviewer: What ended up happening with that component?

Participant: The accessibility issue surfaced again during the pre-renewal QA pass, and by then the migration would've cost more than the original estimate because we'd layered on even more customization in the meantime.

Interviewer: If Vendor B had been priced the same as Vendor C, would you have chosen differently?

Participant: Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all.

Interviewer: If Candidate Y's portfolio had come from a more recognizable company, would the hiring call have gone differently?

Participant: Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have.

Interviewer: And if the significance threshold had been strictly enforced before you could act on the rules engine data?

Participant: I'd have waited, or at least run the isolated test first. I just didn't want to lose the momentum.

Interviewer: Last one — if none of the three sprints had already gone into the legacy component, would you still have kept it?

Participant: No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back.

Interviewer: This has been really useful. Thank you for being so candid about where things were uncertain.

Participant: Of course — it's easier to see some of this clearly now than it was in the middle of the sprint.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IS_Biased_4",
  "domain_id": "IS",
  "domain": "Information Systems, Human-Computer Interaction, and Interaction Design",
  "role": "UX/Product Designer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Onboarding Wizard Overhaul",
    "scenario_summary_internal": "A UX/Product Designer at a mid-size B2B SaaS analytics company leads a six-week redesign of a multi-step onboarding wizard ahead of a major client renewal review. Across the sprint the designer must select a usability-research vendor, choose a contractor to build key micro-interactions, decide whether to expand an automated personalization engine based on early dashboard signals, and decide whether to keep customizing a legacy wizard component or migrate to a new modular framework. Each decision is made under time pressure with incomplete evidence and competing stakeholder goals.",
    "occupational_realism": {
      "objective": "Redesign the onboarding wizard to reduce first-week drop-off before the Q4 enterprise renewal review, without exceeding the discretionary research/contractor budget or slipping the six-week sprint window.",
      "setting": "Mid-size B2B SaaS analytics company; cross-functional Product & Design team operating under a hard external deadline tied to a client renewal cycle.",
      "constraints": [
        "Six-week sprint window fixed by the renewal review date",
        "Capped discretionary budget for external research and contractor work",
        "Engineering capacity limited to 1.5 FTE for the sprint",
        "Design-system governance expects reuse of existing components where feasible",
        "Leadership expects a quantifiable activation-rate improvement to present at the review"
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
          "Scope only requires validating three wizard flows, which Vendor A's session count could plausibly cover"
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
        "intended_action": "Designer selects Vendor C, justifying the choice mainly by contrasting it favorably against Vendor B rather than independently assessing whether the smaller Vendor A package would have met the actual research need."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two contract interaction designers are shortlisted: Candidate X (portfolio featuring flagship work at a well-known unicorn startup, limited documented research process) and Candidate Y (less prominent portfolio, but includes documented usability test scripts, metrics, and iteration logs)",
          "The task requires rigorous micro-interaction testing and clear stakeholder documentation, not visual polish alone",
          "Contractor budget allows only one hire for the sprint"
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
        "intended_action": "Designer hires Candidate X, extending assumed competence in research rigor and stakeholder communication from the strength of the visible portfolio, without verifying those specific capabilities."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "An automated personalization rules engine is running a small-sample A/B test (n=140) that shows activation rate ticking upward during the same week the designer manually adjusted two onboarding rule weights",
          "The Data/Analytics Lead notes the sample size is below the pre-registered threshold for statistical significance",
          "No isolated causal test separating the manual rule changes from other concurrent factors (e.g., a marketing email send) has been run"
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
        "intended_action": "Designer requests expanded manual control over the personalization rules engine, treating the early upward tick as evidence that their specific adjustments are steering the outcome."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The team has spent three sprints customizing the legacy 'step-wizard' design-system component to fit the new onboarding flow",
          "Engineering flags that the legacy component has a known accessibility defect and a rendering performance issue that a newer modular framework would resolve in roughly one sprint",
          "Migrating now would discard the three sprints of legacy customization work already completed"
        ],
        "alternatives": [
          "Migrate to the modular framework now, absorbing the one-sprint rebuild cost",
          "Continue customizing the legacy component to preserve the work already invested",
          "Freeze scope and ship with known defects, revisiting the framework question after the renewal review"
        ],
        "new_information_after_decision": [
          "The legacy component's accessibility defect is flagged during the pre-renewal QA pass",
          "Engineering estimates the eventual migration will now cost more than the original one-sprint estimate due to further customization layered on top"
        ],
        "intended_action": "Designer argues to continue customizing the legacy component, citing the three sprints already invested as a primary reason to avoid switching, despite the engineering evidence favoring migration."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were trying to accomplish with the onboarding wizard redesign and why it mattered for this particular sprint.",
        "What made this project different from a routine design update?"
      ],
      "timeline_reconstruction": [
        "Take me from the moment the vendor proposals arrived through to the final QA pass before the renewal review.",
        "What information did you have at each stage, and what changed once you acted on it?"
      ],
      "decision_point_probes": [
        "What specifically made Vendor C stand out compared to the other two proposals, and what would you have needed to see to justify the smaller package instead?",
        "What evidence did you use to judge Candidate X's fit for this specific task, beyond the portfolio itself?",
        "What told you the activation uptick was tied to your manual rule adjustments rather than something else happening that week?",
        "What weighed most heavily in your decision to keep customizing the legacy component rather than migrate?"
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
        "How much did the six-week deadline affect how quickly you settled on an option?"
      ],
      "uncertainty": [
        "What did you still not know when you committed to each choice?",
        "Looking back, where was the evidence thinnest?"
      ],
      "closing_hypotheticals": [
        "If Vendor B had been priced the same as Vendor C, would your choice have changed?",
        "If Candidate Y's portfolio had come from a more recognizable company, would you have hired differently?",
        "If the sample size requirement had been enforced before you acted, what would you have done instead?",
        "If none of the three sprints had already gone into the legacy component, would you still have chosen to keep it?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect",
        "decision_point": 1,
        "mechanism": "An intermediate option (Vendor B) is priced close to the target option (Vendor C) but offers strictly less value, making Vendor C appear to be the obviously superior deal relative to Vendor B, which pulls attention away from independently assessing whether the cheaper Vendor A package actually matched the research scope.",
        "affected_reasoning_operation": "Comparative evaluation of vendor proposals; option selection under a fixed budget ceiling",
        "evidence_available_at_time": [
          "Three vendor price/feature tables including the near-identical Vendor B/C pricing gap",
          "Actual project scope requiring only three flows tested, which Vendor A could plausibly cover"
        ],
        "required_textual_manifestation": "The designer explains the choice of Vendor C primarily in terms of how much better it looks next to Vendor B ('for barely more than B, C gives you so much more'), without separately justifying why Vendor A's smaller package was insufficient.",
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
        "mechanism": "A strong, salient positive attribute (prestigious portfolio brand) causes the designer to infer unrelated positive qualities (research rigor, documentation discipline, stakeholder communication) without direct evidence for those specific qualities.",
        "affected_reasoning_operation": "Candidate competency assessment across multiple unverified dimensions based on one salient cue",
        "evidence_available_at_time": [
          "Candidate X's portfolio emphasizing visual work from a well-known company",
          "Candidate Y's portfolio containing documented test scripts and metrics",
          "Task requirements explicitly needing rigorous testing and documentation"
        ],
        "required_textual_manifestation": "The designer describes choosing Candidate X by extending trust from the impressive portfolio brand to assumed strengths in documentation and communication that were never directly evaluated.",
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
        "mechanism": "The designer overattributes a small, statistically underpowered upward trend to their own specific manual adjustments, overestimating personal causal influence over a system with concurrent confounding factors and no isolated causal test.",
        "affected_reasoning_operation": "Causal attribution of an observed metric change to a self-initiated action, under acknowledged low statistical power",
        "evidence_available_at_time": [
          "Small-sample dashboard trend (n=140, below significance threshold)",
          "Analytics Lead's explicit flag about insufficient sample size",
          "Absence of an isolated test separating manual rule changes from the concurrent marketing send"
        ],
        "required_textual_manifestation": "The designer requests expanded manual control, framing the uptick as evidence that their specific rule adjustments are working, despite the flagged sample-size and confound issues.",
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
        "mechanism": "The decision to continue customizing the legacy component is driven primarily by the magnitude of effort already invested (three sprints) rather than by a forward-looking comparison of remaining costs and benefits, even though engineering evidence favors migration.",
        "affected_reasoning_operation": "Forward-looking cost-benefit weighing of continuing versus abandoning a partially completed investment",
        "evidence_available_at_time": [
          "Three sprints of prior customization effort on the legacy component",
          "Engineering estimate that migration would take roughly one sprint and resolve known defects",
          "Known accessibility and performance defects in the legacy component"
        ],
        "required_textual_manifestation": "The designer cites the three sprints already spent as a central justification for continuing with the legacy component, rather than weighing the one-sprint migration estimate and defect risks on their own merits.",
        "plausible_nonbias_interpretation": "The designer might reasonably believe the migration estimate is unreliable or that switching introduces its own unquantified risks close to the renewal deadline.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "sunk cost",
          "prior investment fallacy",
          "any naming of the bias mechanism"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control variant."
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
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Exactly one instance of each of the four named biases is planned, mapped one-to-one to a distinct decision point.",
      "No bias label, definition, or psychological explanation is to appear in the public interview text.",
      "Each occurrence has a distinct evidence trace and a plausible non-bias alternative explanation.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points with probes, without repetitive exposition.",
      "Consequences described after each decision point do not mechanically confirm or deny whether the decision was biased.",
      "Technical vocabulary list avoids all bias-name terms to prevent label leakage."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
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
        "mechanism": "Selection of the target vendor option is driven by favorable contrast against a similarly priced but inferior intermediate option, rather than independent assessment of the cheapest sufficient option.",
        "affected_reasoning_operation": "Comparative evaluation of vendor proposals under budget constraint",
        "evidence_source": "Vendor price/feature comparison table; project scope documentation",
        "distinctiveness_requirement": "Must involve a three-option price/value contrast structure unique to this decision point; not reducible to a simple cost-only preference."
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "mechanism": "A single salient positive attribute (portfolio brand prestige) is used to infer unrelated positive qualities (documentation rigor, communication skill) without direct supporting evidence.",
        "affected_reasoning_operation": "Multi-dimensional competency assessment based on one visible cue",
        "evidence_source": "Candidate portfolios; task requirement specification for documentation and rigor",
        "distinctiveness_requirement": "Must involve generalization from one attribute to unrelated, unverified attributes; not reducible to a simple preference for the flashier portfolio."
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control",
        "mechanism": "Overattribution of an observed metric change to the designer's own specific manual action, despite acknowledged insufficient statistical power and unresolved confounding factors.",
        "affected_reasoning_operation": "Causal attribution under uncertainty and low sample size",
        "evidence_source": "A/B dashboard trend data; Analytics Lead's sample-size flag; concurrent marketing-send confound",
        "distinctiveness_requirement": "Must involve explicit disregard of a flagged statistical limitation in favor of self-attributed causal influence; not reducible to general overconfidence."
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias",
        "mechanism": "Continuation of a design approach is justified primarily by the magnitude of prior invested effort rather than a forward-looking comparison of remaining costs and benefits.",
        "affected_reasoning_operation": "Forward-looking continuation-versus-abandonment cost-benefit judgment",
        "evidence_source": "Sprint investment history; engineering migration-cost and defect-resolution estimate",
        "distinctiveness_requirement": "Must explicitly cite prior invested effort as the stated justification for continuation despite forward-looking evidence favoring the alternative; not reducible to general risk-aversion."
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
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IS_Biased_4",
    "domain_id": "IS",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point chosen for mechanism fit and narrative realism (Decoy effect -> vendor procurement comparison; Halo effect -> contractor competency inference; Illusion of control -> causal attribution of an ambiguous metric trend; Sunk Cost Bias -> continuation-vs-migration judgment on prior invested effort). No decision point hosts more than one bias instance, and no bias occurrence count required splitting across decision points.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
        "raw_interview_anchor": "Participant: Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. ... the contrast between the other two was just so stark that it became the frame I was working from.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant lets the near-priced inferior full-service option frame the choice of Vendor C and does not independently assess whether Vendor A meets the three-flow scope."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "contractor_selection_reasoning",
        "raw_interview_anchor": "Participant: I went with Candidate X. ... if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. ... I looked at the visual work and sort of assumed the rest would follow.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "The participant generalizes prestige and visual polish to unverified documentation and communication abilities, despite Candidate Y's directly relevant process evidence."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "rules_engine_causal_interpretation",
        "raw_interview_anchor": "Participant: The activation numbers on the dashboard ticked up right after. I took it as a sign the adjustments were working. ... I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The participant attributes an underpowered, confounded uptick to their own manual rule changes and acts on that attribution despite the Data lead's warning."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "post_test_uncertainty_update",
        "raw_interview_anchor": "Participant: The uptick partly reversed once the email campaign ended, and she noted the causal driver was still unconfirmed. So it's genuinely unclear how much of that first bump was actually the rule changes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a later uncertainty update that acknowledges reversal and unresolved causality; it contains no hidden manifested bias instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "legacy_component_continuation_reasoning",
        "raw_interview_anchor": "Participant: I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away ... The one-sprint number was probably a better bet purely on cost and risk.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "Past effort is used to justify continuation even though the forward-looking one-sprint migration estimate is better on cost and risk and resolves known defects."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
