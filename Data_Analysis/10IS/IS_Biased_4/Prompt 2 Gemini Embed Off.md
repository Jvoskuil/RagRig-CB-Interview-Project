You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative, mechanism-first evaluation of the participant's reported reasoning. No RAG retrieval context was supplied for this task; classifications rely on established general cognitive-science knowledge, and corpus_evidence fields are empty where no retrieval support was available."
  },
  "identified_bias_summary": [
    {
      "bias_label": "attraction effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "attraction effect",
      "alternative_labels": [
        "decoy effect",
        "asymmetric dominance effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A context-dependent preference shift in which an option perceived as clearly inferior to another option increases the attractiveness of the contrasting option, even if the selected option would not have been chosen on the basis of absolute requirements alone.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor selection for usability research",
      "decision_point_description": "Choosing among three vendor proposals: a $6k self-serve platform with five sessions and no synthesis, a $21k full-service option with ten sessions and synthesis, and a $23k full-service option with twelve sessions, dashboard integration, and two follow-up rounds.",
      "affected_reasoning_operation": "Option evaluation and vendor selection",
      "bias_specific_mechanism": "The middle $21k package was perceived as a much worse value than the $23k package because the top option offered more features for only $2k more. This stark contrast reframed the evaluation as a binary comparison between the two full-service packages and made the $23k package feel like an easy choice, causing the $6k self-serve option to drop out of the active decision frame even though it likely could have handled the three flows session-count-wise.",
      "manifestation_in_interview": "The participant reported that once the $21k and $23k options were placed side by side, the $23k option seemed obviously better and the self-serve option disappeared from consideration. The participant later acknowledged that without the price gap they would have looked harder at whether the top package was necessary.",
      "effect_on_reasoning_or_decision": "The evaluation was narrowed to two full-service packages, leading to selection of the $23k package while the lower-cost self-serve option was not seriously evaluated against actual research requirements.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. For two grand more you got two more sessions, the dashboard hookup, and follow-ups baked in. The middle option just looked like a worse version of the top one at almost the same price. It felt like an easy call.",
          "evidence_explanation": "This quote shows the decision was driven by the perceived dominance of the top option over the middle option rather than by a direct comparison of all three options against the project's actual needs."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from.",
          "evidence_explanation": "This directly describes the attraction-effect mechanism: the salient contrast between the full-service options narrowed the decision frame and excluded the self-serve option from consideration."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all.",
          "evidence_explanation": "This counterfactual supports the conclusion that the contextual price comparison, rather than an absolute requirements analysis, was the operative distorting factor."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that the self-serve option probably could have covered the three flows session-count-wise and that without the price gap they might have evaluated necessity more carefully. A non-bias explanation is that full-service synthesis may have been genuinely valuable under a compressed timeline; however, the participant's own description identifies the contrast frame rather than a requirements-based comparison as the operative mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for this classification; the label and mechanism rely on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "halo effect",
      "alternative_labels": [
        "prestige bias",
        "brand-name halo"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which a positive impression or salient strength in one dimension spreads to unrelated judgments about an individual's other attributes or competencies.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor selection for micro-interaction work",
      "decision_point_description": "Choosing between Candidate X, who had visually polished work from a well-known unicorn startup, and Candidate Y, whose portfolio was less flashy but included test scripts, metrics, and iteration logs.",
      "affected_reasoning_operation": "Personnel evaluation and hiring decision",
      "bias_specific_mechanism": "The visual polish and employer pedigree of Candidate X created a positive halo that led the participant to infer, without direct evidence, that Candidate X would also be rigorous in documentation, testing, and stakeholder communication. Candidate Y's directly documented process evidence was discounted because it lacked the same visual wow factor.",
      "manifestation_in_interview": "The participant chose Candidate X because of visual work and company reputation, then admitted assuming the documentation and communication strengths would follow. Candidate Y's portfolio had exactly the evidence needed, but it was perceived as less impressive overall because it lacked visual flash.",
      "effect_on_reasoning_or_decision": "Candidate X was selected despite the absence of verified documentation and testing process skills; later, Candidate X did not document the reasoning behind key transitions, leaving the participant without evidence to show the Head of Design.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. It seemed like a safe bet given where he'd come from.",
          "evidence_explanation": "This quote captures the halo mechanism: the participant inferred documentation and communication rigor from visual design quality and employer brand rather than from direct evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall.",
          "evidence_explanation": "This directly shows the biased inference from visual impression to unrelated job competencies and the undervaluing of the candidate with relevant evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have.",
          "evidence_explanation": "This admission confirms that brand recognition and visual prestige, rather than a balanced assessment of documented competencies, influenced the hiring decision."
        }
      ],
      "correction_or_counterevidence": "A non-bias explanation is that visual polish was a genuine requirement for the micro-interaction work, and Candidate X did deliver beautiful micro-interactions. However, the specific inference about documentation and communication was not verified and the participant later acknowledged that name recognition was overweighted.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for this classification; the label and mechanism rely on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "motivated reasoning",
        "myside bias",
        "illusory correlation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and weigh information in ways that confirm prior beliefs, expectations, or desired conclusions while discounting evidence that would disconfirm them.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting activation uptick after manual rule-weight changes",
      "decision_point_description": "Whether to attribute a dashboard activation uptick to the participant's recent manual rule-weight changes and expand manual tuning authority before pre-registered significance and isolation requirements were met.",
      "affected_reasoning_operation": "Causal inference from observational product-analytics data under statistical uncertainty",
      "bias_specific_mechanism": "After making manual rule adjustments, the participant interpreted a subsequent activation uptick as evidence that the adjustments were working. When the Data lead noted that the sample was below the pre-registered significance threshold and that a concurrent marketing email confounded causal attribution, the participant acknowledged but discounted these caveats because the timing appeared too clean. This selective weighting maintained the desired causal conclusion and motivated a request for expanded tuning authority.",
      "manifestation_in_interview": "The participant treated the uptick as a sign that the adjustments were working and sought to expand tuning authority. The Data lead provided methodological counterevidence, but the participant privileged the temporal association and later acknowledged not wanting to lose momentum.",
      "effect_on_reasoning_or_decision": "The participant requested expanded manual tuning authority prematurely. The next week the uptick partly reversed and the causal driver remained unconfirmed, indicating that the initial inference was not warranted by the available data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I took it as a sign the adjustments were working. I went to the Data lead and asked to expand my manual tuning authority so I could keep pushing on it before the renewal review.",
          "evidence_explanation": "This shows the participant accepted the uptick as confirmatory evidence for their own prior intervention and acted on that interpretation by seeking more authority."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver.",
          "evidence_explanation": "This directly demonstrates the biased evaluation of evidence: explicit statistical and confounding caveats were acknowledged but dismissed in favor of the preferred causal interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd have waited, or at least run the isolated test first. I just didn't want to lose the momentum.",
          "evidence_explanation": "This counterfactual supports the conclusion that the participant's action was influenced by a preferred conclusion and temporal momentum rather than by the methodological evidence."
        }
      ],
      "correction_or_counterevidence": "The Data lead provided explicit methodological counterevidence about sample size and confounding. The participant later acknowledged that the causal driver was unconfirmed. A non-bias factor is legitimate deadline pressure and a desire to maintain momentum; however, the reported dismissal of the methodological caveats supports a confirmatory distortion rather than a purely rational tradeoff.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for this classification; the label and mechanism rely on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue investing in a course of action because of already committed resources such as time, money, or effort, even when future prospects favor abandoning or changing course.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Legacy step-wizard component versus migration decision",
      "decision_point_description": "Whether to continue customizing the old step-wizard component after three sprints or migrate to a newer modular framework estimated to fix accessibility and rendering issues in about one sprint.",
      "affected_reasoning_operation": "Prospective cost/benefit decision under irrecoverable prior investment",
      "bias_specific_mechanism": "The participant's continued commitment to the legacy component was driven by the three sprints already spent. This prior investment was treated as a reason to keep customizing even though the participant's own prospective assessment favored migration on cost and risk grounds. The sunk cost was not recoverable, but it distorted the future-oriented decision.",
      "manifestation_in_interview": "The participant pushed to keep customizing the legacy component because restarting felt like throwing away the prior sprints. They later acknowledged that the one-sprint migration was probably a better bet purely on cost and risk, but the already spent work made it hard to let go.",
      "effect_on_reasoning_or_decision": "The team continued with the legacy component, layered on additional customization, and later faced the accessibility issue again during QA. By then, migration would have cost more than the original estimate.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us.",
          "evidence_explanation": "This quote shows that the irrecoverable investment of three sprints was used as a reason to continue the legacy path."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built.",
          "evidence_explanation": "This directly contrasts prospective cost/risk evaluation with the psychological pull of sunk costs, revealing that the prior investment distorted the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back.",
          "evidence_explanation": "This counterfactual isolates the causal role of sunk costs: absent the prior investment, the participant would have chosen migration immediately."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure could plausibly have made continued customization seem safer in the moment, but the participant explicitly stated that had no prior investment existed, the defects alone would have pushed them toward the new framework immediately. This supports the conclusion that unrecoverable sunk cost was the operative distorting factor.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available for this classification; the label and mechanism rely on established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "insensitivity to sample size",
      "alternative_labels": [
        "sample size neglect",
        "representativeness bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Interpreting activation uptick after manual rule-weight changes",
      "supporting_interview_quote": "She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore.",
      "plausible_mechanism": "The participant may have underweighted the low statistical reliability of the small sample and the confounded marketing campaign when making a causal inference from the activation uptick.",
      "why_not_identified": "The sample-size distortion is tightly coupled with the confirmatory interpretation already captured under confirmation bias, and the transcript does not provide an independent, separable decision or action attributable solely to sample-size neglect."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided for this analysis; all corpus_evidence fields are empty and retrieved_corpus_support_available is false for each occurrence.",
    "The analysis relies on a single interview transcript and the participant's retrospective self-report, which may be influenced by memory, self-presentation, or post-hoc reinterpretation.",
    "Some overlapping mechanisms, such as sample-size neglect in the rules-engine episode, are folded into a primary occurrence to avoid double-counting a single decision episode.",
    "The coding is conservative and mechanism-first; statements that merely reflect outcome disappointment or legitimate time-pressure tradeoffs were not classified as biases unless a distinct distortion mechanism was affirmatively evidenced."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Biased_4_Gemini_off",
  "interview_id": "IS_Biased_4",
  "system_prompt_id": "Gemini",
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
