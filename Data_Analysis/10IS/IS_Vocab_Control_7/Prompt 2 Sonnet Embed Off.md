You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was "right." Everything stays in the design systems research archive. Sound okay?

Participant: Sure, happy to walk through it.

Interviewer: Can you remind me of your role and what triggered this whole evaluation?

Participant: I lead design systems for the platform org — three designers, two engineers under me. Legal flagged that we needed to hit WCAG 2.2 AA across two customer-facing squads within about ten weeks, and our internal component library had known contrast and focus-state debt. LumenKit came up because a couple of competitors use it and it's picked up some industry recognition.

Interviewer: What was your goal going into the vendor demo?

Participant: Mainly to see whether adopting something pre-built could shortcut months of remediation work, given the timeline.

Interviewer: Walk me through what happened, in order.

Participant: The solutions engineer ran about forty minutes, mostly on their accordion component — motion, keyboard handling, graceful degradation. Genuinely well done. They also said the library ships with AA-compliant color defaults. Rather than take that at face value, I asked for their contrast-ratio spec sheet on the core color and elevation tokens before deciding anything about pilot scope. When it came back, I noticed it only covered default, unthemed values — nothing about how those tokens would behave once we applied our own theming layer. That gap mattered, since our actual implementation would always be themed.

Interviewer: What did that lead you to do?

Participant: I scoped the pilot narrowly — just the token categories tied directly to our compliance gap, not the whole library — since the spec sheet couldn't tell me how the tokens would hold up once themed. We got a three-week sandbox limited to that smaller set. Both squad leads said they were interested but wanted pricing before committing engineering time.

Interviewer: Did anything push you toward a broader commitment at that point?

Participant: Not really. The demo was impressive, but impressive motion design on one component doesn't tell you much about contrast behavior on a different set of tokens, so I kept those separate in my head.

Interviewer: Let's move to licensing. What did that look like?

Participant: Procurement needed a recommendation in two weeks. Three tiers: Basic, five components, no support; Team, twelve components, limited support, priced not far below Enterprise; Enterprise, full library with dedicated support. I mapped what the narrow pilot actually needed against each tier's component list rather than just comparing the tiers to each other.

Interviewer: What did that comparison show?

Participant: Team actually covered our confirmed needs — the components we'd already scoped plus reasonable headroom for the second squad. Enterprise had things we weren't using yet. I recommended Team and flagged that we could revisit Enterprise later if adoption grew.

Interviewer: And the rollout timeline?

Participant: I hadn't set a date yet at that point. I asked both squad leads directly what their earliest realistic integration window was, given their existing release calendars, before committing to anything.

Interviewer: What did they say?

Participant: One could start in three weeks, the other in five. I set the rollout date to the later window rather than picking something in between and hoping it would work out.

Interviewer: What information would have changed that recommendation, looking back?

Participant: Honestly, not much — checking actual needs against the tier list and getting real calendar commitments from both squads is basically what I'd do again.

Interviewer: Let's get to the audit. What came back?

Participant: About seven weeks in, our internal accessibility audit found that several LumenKit color and elevation tokens failed contrast requirements in three of five tested components. I'd told the VP and both squad leads earlier that the defaults tested well in the initial spec review and pilot, but I'd also flagged at the time that full-scale testing was still pending.

Interviewer: What was your first move on the discrepancy?

Participant: I wanted to know whether the failure was in our theming layer or in the vendor's own default tokens, so I requested an independent retest of LumenKit's out-of-box tokens with no internal theming applied. I didn't want to guess at the cause.

Interviewer: What did the retest show?

Participant: It confirmed the failures originated in the vendor's default token values, not our theming. That was useful because it told us exactly which components needed to change.

Interviewer: What did you decide to do with that?

Participant: We'd put some engineering hours into customizing those tokens already, but once the retest pointed at the vendor defaults specifically, I reverted just the three affected components to our already-remediated legacy tokens and left the rest of the LumenKit components in place, since those had tested clean.

Interviewer: Did the VP or squad leads react?

Participant: The VP asked for a written explanation for the compliance file, which I could give directly from the retest data. Both squads were fine with the partial reversion once they saw which components were affected.

Interviewer: That brings us to the final call. What were the options three weeks before the deadline?

Participant: Expand LumenKit organization-wide, including the categories that had failed; adopt a hybrid — keep LumenKit's motion and layout components but source color and elevation tokens internally; or revert fully to legacy.

Interviewer: How did you weigh those?

Participant: The retest data was specific to color and elevation, not layout or motion, so a full revert seemed like it would throw away components that had actually tested fine. Full expansion seemed to reintroduce the exact risk we'd just found. The hybrid matched what the evidence actually showed — keep what tested clean, source internally what didn't.

Interviewer: So what did you recommend?

Participant: The hybrid. I documented the retest findings, the expected migration effort for each option, and the compliance risk if we expanded the failing categories anyway, and sent that to the VP and counsel before finalizing it.

Interviewer: If the audit had come in during week one instead of week seven, would your approach to the retest have changed?

Participant: Probably not the approach — I'd still want to isolate vendor tokens from theming before deciding anything. It might have just meant less customization work to unwind.

Interviewer: If the vendor's demo hadn't included that contrast-ratio spec sheet at all, do you think your initial pilot scope would have looked different?

Participant: I likely would have asked for one anyway before scoping anything broadly — a strong demo on one component isn't evidence about a different set of tokens.

Interviewer: If procurement had only offered two tiers instead of three, would Team still have been your pick?

Participant: Depends on what the two were, but I'd still have checked actual component needs against whatever was offered rather than picking based on how the options looked next to each other.

Interviewer: Starting over today, what would you keep, and what would you change?

Participant: I'd keep asking for direct evidence before scoping decisions and getting real commitments from the squads before setting dates. I'm not sure I'd change much — the one thing I'd tighten up is flagging the "pending full-scale testing" caveat more visibly in written updates, so it's not just something I remember saying.

Interviewer: This has been really useful. Thanks for walking through the reasoning in this much detail.

Participant: No problem — it's a good exercise to lay it out step by step like this.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IS_Vocab_Control_7",
  "domain_id": "IS",
  "domain": "Information Systems, human-computer interaction, and interaction design",
  "role": "Interaction Designer (Design Systems Lead)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The LumenKit Migration (Vocabulary-Matched Control): Evaluating a Vendor Design-Token System Under an Accessibility Deadline",
    "scenario_summary_internal": "A Design Systems Lead at a mid-size enterprise SaaS company evaluates whether to adopt a vendor's component/token library ('LumenKit') to accelerate a compliance-driven accessibility overhaul across two product squads. The lead runs a structured, verification-driven evaluation: reviewing both the vendor demo and independent token data before scoping a pilot, comparing licensing tiers against actual component needs, setting a rollout timeline pending squad confirmation, and reassessing the plan point-by-point after an accessibility audit before making a final rollout recommendation. This scenario matches the paired biased scenario's domain, actors, stakes, and decision structure but instantiates zero intended cognitive biases.",
    "occupational_realism": {
      "objective": "Decide whether and how to replace the legacy internal component library with a vendor design-token system to meet an upcoming WCAG 2.2 AA compliance deadline across two product squads.",
      "setting": "Mid-size enterprise SaaS company; centralized design systems team supporting 6 product squads; 10-week compliance deadline set by legal/procurement.",
      "constraints": [
        "Hard compliance deadline in 10 weeks",
        "Limited design systems team headcount (3 designers, 2 engineers)",
        "Dependent squads have their own release calendars",
        "Procurement requires a licensing-tier recommendation within 2 weeks",
        "No budget for a full custom-built replacement"
      ],
      "stakeholders": [
        "Design Systems Lead (interviewee)",
        "VP of Product Design",
        "Accessibility/Compliance counsel",
        "Two product squad leads (dependent teams)",
        "LumenKit vendor sales and solutions engineer",
        "Procurement manager"
      ],
      "technical_terms_to_use": [
        "design tokens",
        "component library",
        "contrast ratio",
        "WCAG 2.2 AA",
        "elevation/shadow tokens",
        "pilot rollout",
        "design system governance",
        "licensing tier",
        "accessibility audit",
        "component adoption rate"
      ],
      "technical_terms_to_avoid": [
        "priming",
        "cognitive dissonance",
        "decoy effect",
        "halo effect",
        "illusion of control",
        "sunk cost",
        "status quo bias",
        "any explicit bias terminology or psychological labels"
      ],
      "notes": "Match the paired scenario's vocabulary, stakeholders, deadline structure, and four-decision-point chronology. Every decision should be supported by evidence gathered at or before the decision, with alternatives weighed on comparable terms rather than through incidental contrasts or carried-over impressions."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "LumenKit is an industry-recognized component library used by several competitors",
          "The vendor demo showcased a flagship accordion component with fluid motion and stated AA-compliant contrast defaults",
          "The lead requested and received a short contrast-ratio spec sheet for LumenKit's core color and elevation tokens before the pilot-scoping decision",
          "Internal legacy library has known technical debt but has not been benchmarked against LumenKit's full token set",
          "Team has 10 weeks until compliance deadline"
        ],
        "new_information_after_decision": [
          "Vendor grants a 3-week trial sandbox limited to the components the lead selected for the narrow pilot",
          "Squad leads express interest but ask for a tier and cost estimate before committing engineering time"
        ],
        "alternatives": [
          "Run a narrow, component-by-component pilot starting with the token categories most relevant to the compliance gap",
          "Commit to a full pilot integration of LumenKit's entire token set across both squads immediately",
          "Continue patching the legacy library in-house"
        ],
        "intended_action": "The lead reviews the contrast-ratio spec sheet alongside the demo, identifies that the spec sheet covers only default (unthemed) values, and scopes the pilot narrowly to the token categories most relevant to the compliance gap pending further verification."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor sales presents three licensing tiers: Basic (5 components, no support), Team (12 components, limited support, priced not far below Enterprise), Enterprise (full library, dedicated support)",
          "Procurement needs a tier recommendation in two weeks",
          "The lead maps the narrow pilot's actual component needs against each tier's included component list",
          "Rollout depends on two other squads' independent release calendars",
          "The lead has not yet set a rollout date and asks both squad leads to state their earliest feasible integration window"
        ],
        "new_information_after_decision": [
          "Procurement approves the recommended tier after a short scope justification",
          "Both squads confirm distinct feasible windows; the lead sets the rollout date to the later of the two"
        ],
        "alternatives": [
          "Recommend the Basic tier",
          "Recommend the Team tier",
          "Recommend the Enterprise tier",
          "Request a custom-scoped tier limited to the confirmed component needs"
        ],
        "intended_action": "The lead recommends the tier that covers the confirmed component needs at the lowest cost after checking actual requirements against each tier's component list, and sets the rollout timeline to match the later of the two squads' confirmed feasible windows rather than an internally assumed date."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "An internal accessibility audit finds that several LumenKit color and elevation tokens fail contrast ratio requirements in three of five tested components",
          "The lead had told the VP and both squad leads that LumenKit's contrast defaults tested well in the initial spec review and pilot, with the caveat that full-scale testing was pending",
          "Some engineering hours have already been spent customizing LumenKit tokens to fit internal theming",
          "Legacy library remains available as a fallback with known, already-remediated contrast values in those same components"
        ],
        "new_information_after_decision": [
          "An independent retest of the vendor's out-of-box tokens (without internal theming) confirms the failures originate in the vendor's default token values, not the internal theming layer",
          "The VP requests a written explanation for the compliance file, which the lead provides based on the retest"
        ],
        "alternatives": [
          "Request an independent retest of the vendor's out-of-box tokens before deciding whether to continue, pause, or revert",
          "Continue customizing the current tokens without further testing",
          "Revert immediately to the legacy tokens for the affected components without testing further"
        ],
        "intended_action": "The lead requests the retest to distinguish a theming-layer problem from a vendor-token problem, and, once the retest confirms a vendor-token issue, revert the three affected components to the remediated legacy tokens while keeping the passing LumenKit components in place."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pilot is 3 weeks from the compliance deadline",
          "The three affected components have been reverted to remediated legacy tokens; the remaining LumenKit components passed testing",
          "A hybrid plan exists: keep LumenKit motion/layout components but source color and elevation tokens internally",
          "VP asks for a final recommendation: expand LumenKit organization-wide, adopt the hybrid plan, or revert fully to the legacy library"
        ],
        "new_information_after_decision": [
          "Two additional squads are scheduled to onboard whichever system is chosen within the next quarter",
          "Compliance counsel signs off on the documented, tested rationale for the chosen path"
        ],
        "alternatives": [
          "Expand LumenKit organization-wide, including the previously failing token categories",
          "Adopt the hybrid plan (LumenKit layout/motion + internal color/elevation tokens)",
          "Revert fully to the legacy library"
        ],
        "intended_action": "The lead recommends the hybrid plan, citing the retest evidence that the vendor's color and elevation tokens carry unresolved risk while the motion and layout components tested cleanly, and documents the expected migration effort and compliance risk for each option before finalizing the recommendation."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what triggered this whole evaluation in the first place?",
        "What was your primary goal going into the vendor demo?"
      ],
      "timeline_reconstruction": [
        "What happened right after the demo, in the order it happened?",
        "When did the licensing conversation with procurement start relative to the pilot-scoping decision?",
        "Walk me through what you knew right before the audit results came back."
      ],
      "decision_point_probes": [
        "What specific evidence determined how broad or narrow the initial pilot was?",
        "How did you compare the three licensing tiers against your actual component needs?",
        "How did you arrive at the rollout timeline, and what role did the squads' input play?",
        "When the audit came back, what steps did you take to figure out where the failure originated?",
        "What made you decide to request the retest rather than continuing or reverting outright?",
        "What tipped the final recommendation toward the hybrid plan rather than the other two options?"
      ],
      "closing_hypotheticals": [
        "If the vendor's demo had not included a contrast-ratio spec sheet, do you think your initial pilot scope would have looked different?",
        "If procurement had presented only two tiers instead of three, would your recommendation have been different?",
        "Looking back, if the audit had come in during week one instead of week seven, would your approach to the retest have changed?",
        "If you were starting this evaluation over today, what would you do differently, and what would you keep the same?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "IS_Biased_7",
      "features_to_match": [
        "Domain vocabulary (design tokens, contrast ratio, WCAG 2.2 AA, licensing tiers, accessibility audit, pilot rollout, design system governance)",
        "Same stakeholders and organizational structure",
        "Same compliance deadline (10 weeks) and same downstream 3-week final-decision window",
        "Same four-phase chronological structure: demo/pilot-scoping decision, licensing/timeline decision, post-audit continuation decision, final rollout-model decision",
        "Same emotional tone: time pressure, professional candor, retrospective reflection without dramatization",
        "Same difficulty level (moderate) and same number of decision points (4)",
        "Same closing hypothetical probe types (presentation order, tier count, audit timing, retrospective redo)"
      ],
      "features_to_remove_or_change": [
        "Remove unverified generalization from one demoed component to the full token set; replace with direct review of a contrast-ratio spec sheet before scoping the pilot",
        "Remove comparative-contrast tier reasoning; replace with a needs-based comparison of each tier's component list against confirmed requirements",
        "Remove unconfirmed personal-oversight timeline-setting; replace with a timeline set only after both squads confirm feasible windows",
        "Remove belief-consistency-driven discounting of audit evidence; replace with a diagnostic retest that distinguishes theming-layer from vendor-token causes",
        "Remove invested-hours-driven continuation rationale; replace with a decision to revert only the specifically failing components based on retest evidence",
        "Remove continuity/familiarity-driven preference for the status quo arrangement; replace with a final recommendation grounded in comparative retest and migration-effort evidence"
      ],
      "ambiguity_boundary": "Not applicable in the strict sense used for ambiguous_control; reasoning here should read as well-supported and evidence-checked at each step, though genuine occupational uncertainty (e.g., squad calendar limits, evolving audit results) is preserved as realistic context, not as a vehicle for any named bias."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable to this condition (vocabulary_control implements zero intended bias instances and is not a counterfactual pairing)",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable.",
      "causal_test_question": "Not applicable."
    },
    "generation_checks": [
      "Exactly four decision points are present and numbered 1-4",
      "Each decision point offers at least two plausible alternatives",
      "Zero named-bias instances are intentionally embedded anywhere in the timeline or probes",
      "Each decision is supported by evidence gathered at or before the decision point, with no unverified generalization, comparative-contrast-only reasoning, unconfirmed control attribution, belief-preserving reinterpretation, invested-cost-driven continuation, or continuity-only preference",
      "Vocabulary, stakeholders, deadline structure, and phase chronology match the paired biased scenario IS_Biased_7",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Consequences described (retest outcome, squad confirmations, counsel sign-off) follow logically from evidence-checked decisions rather than mechanically proving correctness",
      "Scenario content is plausible for an Interaction Designer / Design Systems Lead role",
      "Planned content is scoped to fit 1,215-1,485 words without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {"bias": "Priming effect", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Cognitive Dissonance", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Decoy effect", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Halo effect", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Illusion of control", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Sunk Cost Bias", "occurrences": 0, "mechanism_constraint": null},
      {"bias": "Status Quo Bias", "occurrences": 0, "mechanism_constraint": null}
    ],
    "target_bias_names": [
      "Priming effect",
      "Cognitive Dissonance",
      "Decoy effect",
      "Halo effect",
      "Illusion of control",
      "Sunk Cost Bias",
      "Status Quo Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Priming effect", "requested_occurrences": 0},
      {"bias": "Cognitive Dissonance", "requested_occurrences": 0},
      {"bias": "Decoy effect", "requested_occurrences": 0},
      {"bias": "Halo effect", "requested_occurrences": 0},
      {"bias": "Illusion of control", "requested_occurrences": 0},
      {"bias": "Sunk Cost Bias", "requested_occurrences": 0},
      {"bias": "Status Quo Bias", "requested_occurrences": 0}
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IS_Biased_7",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IS_Vocab_Control_7",
    "domain_id": "IS",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control requires zero intended occurrences of every named bias. Decision points were instead populated with evidence-checked, alternative-considered reasoning that mirrors the paired scenario's four-phase structure (demo/pilot-scoping, licensing/timeline, post-audit continuation, final rollout-model) without instantiating priming, halo, decoy, illusion of control, cognitive dissonance, sunk cost, or status quo mechanisms.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Compliance deadline (10 weeks) and final 3-week decision window",
      "Team headcount and resourcing",
      "Vendor identity (LumenKit) and its reputation",
      "Three-tier licensing structure",
      "Audit occurrence and general timing (~week seven)",
      "Number and identity of dependent squads",
      "Four-phase decision chronology and stakeholder set matched to IS_Biased_7"
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
          "segment_type": "goal_statement",
          "raw_interview_anchor": "Participant: Mainly to see whether adopting something pre-built could shortcut months of remediation work, given the timeline.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant states a time-constrained evaluation goal without a manifested cognitive-bias instance."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "evidence_review_and_scope_basis",
          "raw_interview_anchor": "Participant: Rather than take that at face value, I asked for their contrast-ratio spec sheet... it only covered default, unthemed values... our actual implementation would always be themed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant seeks direct evidence and identifies the limits of the available spec before deciding scope."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "pilot_scoping_decision",
          "raw_interview_anchor": "Participant: I scoped the pilot narrowly — just the token categories tied directly to our compliance gap... since the spec sheet could not tell me how the tokens would hold up once themed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The narrow pilot is explicitly tied to an evidence gap and the compliance need."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "evidence_separation",
          "raw_interview_anchor": "Participant: The demo was impressive, but impressive motion design on one component does not tell you much about contrast behavior on a different set of tokens, so I kept those separate in my head.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant explicitly separates component-level motion evidence from token contrast evidence."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "licensing_tier_decision",
          "raw_interview_anchor": "Participant: I mapped what the narrow pilot actually needed against each tier’s component list... Team actually covered our confirmed needs... I recommended Team.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The tier choice is based on confirmed component requirements and comparison against each tier."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "rollout_timeline_decision",
          "raw_interview_anchor": "Participant: I asked both squad leads directly what their earliest realistic integration window was... One could start in three weeks, the other in five. I set the rollout date to the later window.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The date is set from both squads’ stated feasible windows rather than an unsupported internal assumption."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "recommendation_reflection",
          "raw_interview_anchor": "Participant: Checking actual needs against the tier list and getting real calendar commitments from both squads is basically what I would do again.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant restates an evidence-based decision process; no bias instance is intended or manifested."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "audit_status_and_disclosure",
          "raw_interview_anchor": "Participant: I had told the VP and both squad leads earlier that the defaults tested well... but I had also flagged at the time that full-scale testing was still pending.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant reports both the preliminary result and its pending-testing caveat."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "diagnostic_retest_decision",
          "raw_interview_anchor": "Participant: I wanted to know whether the failure was in our theming layer or in the vendor’s own default tokens, so I requested an independent retest... I did not want to guess at the cause.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The retest is a diagnostic step to distinguish competing causal explanations."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "selective_reversion_decision",
          "raw_interview_anchor": "Participant: Once the retest pointed at the vendor defaults specifically, I reverted just the three affected components... and left the rest... in place, since those had tested clean.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant takes a selective action keyed to retest evidence and component-level test results."
        },
        {
          "segment_id": "seg_011",
          "speaker": "Participant",
          "segment_type": "final_option_comparison_and_recommendation",
          "raw_interview_anchor": "Participant: The hybrid matched what the evidence actually showed — keep what tested clean, source internally what did not... I documented the retest findings, expected migration effort, and compliance risk for each option.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The final recommendation compares alternatives using test evidence, migration effort, and compliance risk."
        },
        {
          "segment_id": "seg_012",
          "speaker": "Participant",
          "segment_type": "retrospective_improvement",
          "raw_interview_anchor": "Participant: I would keep asking for direct evidence... The one thing I would tighten up is flagging the pending full-scale testing caveat more visibly in written updates.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant identifies a communication improvement while retaining evidence-seeking practices."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": ["Interviewer", "Participant"],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Mechanism-first analysis of the provided CTA transcript only; no retrieved corpus passages were supplied to ground bias labels or mechanisms."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Bandwagon effect",
        "alternative_labels": ["Social proof heuristic"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Initial vendor consideration",
        "supporting_interview_quote": "LumenKit came up because a couple of competitors use it and it's picked up some industry recognition.",
        "plausible_mechanism": "Competitor adoption and industry recognition could make LumenKit seem more credible or lower-risk via social-proof/bandwagon heuristics rather than through independent evaluation of fit.",
        "why_not_identified": "The quoted statement explains only why LumenKit entered consideration; subsequent reasoning is explicitly evidence-driven, including requesting contrast-ratio specs, narrowing pilot scope to compliance-relevant tokens, mapping tier needs to actual requirements, and ordering independent retesting. There is no affirmative evidence that social proof influenced the evaluation or decision."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No retrieved corpus passages were provided, so corpus-supported labeling and mechanism grounding were unavailable.",
      "Analysis is based on the transcript as evidence; subtle implicit biases not manifested in reasoning or decisions would not be identified."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Vocab_Control_7_Sonnet_off",
  "interview_id": "IS_Vocab_Control_7",
  "system_prompt_id": "Sonnet",
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
