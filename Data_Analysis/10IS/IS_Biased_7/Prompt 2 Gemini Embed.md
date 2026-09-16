You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was "right." Everything you share stays in the design systems research archive. Sound okay?

Participant: Sounds good. Happy to walk through it — it's still fresh, honestly.

Interviewer: Great. Can you remind me of your role and what triggered this whole evaluation?

Participant: I lead design systems for the platform org — three designers, two engineers under me. Legal flagged that we needed to hit WCAG 2.2 AA across two customer-facing squads within about ten weeks, and our internal component library had known contrast and focus-state debt we hadn't prioritized. LumenKit came up because a couple of competitors use it and it's picked up some industry recognition.

Interviewer: What was your goal going into the vendor demo?

Participant: Mainly to see if we could shortcut months of remediation work by adopting something pre-built and compliant, given the clock we were on.

Interviewer: Walk me through what happened, in order.

Participant: The solutions engineer ran maybe forty minutes, almost all of it on their accordion component — the motion, the keyboard handling, the way it degraded gracefully. It was genuinely impressive, smoother than anything we'd built in-house. They mentioned the whole library ships with AA-compliant color defaults. After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down. We got a three-week sandbox with a limited component set, and both squad leads said they were interested but needed pricing before committing engineering time.

Interviewer: Did you look closely at the color and elevation tokens before making that call?

Participant: Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape. That assumption is part of why I pushed for the broad pilot instead of testing component by component first.

Interviewer: Let's move to the licensing decision. What did that look like?

Participant: Procurement needed a tier recommendation within two weeks. Vendor offered three: Basic, five components, no support; Team, twelve components with limited support, priced not far below Enterprise; and Enterprise, the full library with dedicated support. I recommended Enterprise.

Interviewer: What made Enterprise the clear choice?

Participant: Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense.

Interviewer: And the rollout timeline — how was that set?

Participant: I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads.

Interviewer: Had the two dependent squads confirmed they could hit a four-week window?

Participant: Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars. One of them came back shortly after saying their calendar genuinely couldn't accommodate that window — they had an unrelated release freeze I hadn't accounted for.

Interviewer: What information would have changed your timeline call, looking back?

Participant: Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first.

Interviewer: Let's get to the audit. What came back?

Participant: About seven weeks in, our internal accessibility audit found that several of LumenKit's color and elevation tokens failed contrast ratio requirements in three of five tested components. That was awkward, because I'd already told the VP and both squad leads that LumenKit would solve most of our contrast problems out of the box.

Interviewer: What was your first read on that discrepancy?

Participant: My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so "it's our theming, not their tokens" sat better with what I'd already said than the alternative did. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities.

Interviewer: What did you decide to do next?

Participant: We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy. The legacy components already had remediated contrast values for those same screens, so that was sitting right there as an option.

Interviewer: What made continuing the more attractive path versus reverting?

Participant: Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked.

Interviewer: Did the VP or squad leads react?

Participant: The VP wanted a written explanation for the compliance file. One squad lead quietly reverted their branch back to the legacy component for the affected screens without waiting on my decision.

Interviewer: That brings us to the final call. What were the options three weeks before the deadline?

Participant: Expand LumenKit org-wide as we'd implemented it, adopt a hybrid — keep LumenKit's motion and layout components but source color and elevation tokens internally — or revert fully to legacy.

Interviewer: How did the hybrid option evaluate against the others?

Participant: On paper it addressed the token problem directly without throwing away the layout and motion integration work we'd already done. It was arguably the cleanest fix.

Interviewer: So what did you recommend?

Participant: I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team.

Interviewer: If the audit had surfaced in week one instead of week seven, do you think that would have changed how you weighed the hours already spent?

Participant: Probably — with less invested, reverting or pivoting to the hybrid would've felt like a much smaller loss.

Interviewer: If the vendor demo had opened with contrast-ratio data instead of the accordion, would your initial pilot decision have gone differently?

Participant: Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly.

Interviewer: If procurement had only offered two tiers instead of three, would Enterprise still have been the obvious pick?

Participant: Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team.

Interviewer: Last one — starting over today, what would you keep, and what would you change?

Participant: I'd keep the urgency and the willingness to bring in outside tooling under deadline pressure — that part was right. I'd change how early I locked in public commitments about what the library would solve, and I'd get squad confirmation on timelines before setting them rather than after.

Interviewer: This has been really useful. Thanks for being so candid about the reasoning, not just the outcome.

Participant: No problem — it's easier to see it laid out like this than it was living through it week to week.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IS_Biased_7",
  "domain_id": "IS",
  "domain": "Information Systems, human-computer interaction, and interaction design",
  "role": "Interaction Designer (Design Systems Lead)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The LumenKit Migration: Piloting a Vendor Design-Token System Under an Accessibility Deadline",
    "scenario_summary_internal": "A Design Systems Lead at a mid-size enterprise SaaS company must decide whether to adopt a vendor's award-winning component/token library ('LumenKit') to accelerate a compliance-driven accessibility overhaul across two product squads. The lead attends a polished vendor demo, negotiates licensing tiers, manages a pilot rollout with cross-team dependencies, encounters an accessibility audit that contradicts early enthusiasm, and finally decides whether to expand the rollout or revert to the legacy system.",
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
      "notes": "Do not name or define any bias in the interview text; only behavioral and evidentiary traces should appear."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "LumenKit is an industry-award-winning component library used by several well-known competitors",
          "The vendor demo showcased a single flagship accordion component with fluid motion and stated AA-compliant contrast defaults",
          "Internal legacy library has known technical debt but has not been independently benchmarked against LumenKit's full token set",
          "Team has 10 weeks until compliance deadline"
        ],
        "new_information_after_decision": [
          "Vendor grants a 3-week trial sandbox with a limited component subset",
          "Squad leads express interest but ask for a tier and cost estimate before committing engineering time"
        ],
        "alternatives": [
          "Commit to a full pilot integration of LumenKit tokens across both squads",
          "Run a narrow, component-by-component evaluation of LumenKit before any commitment",
          "Continue patching the legacy library in-house"
        ],
        "intended_action": "The lead commits to a broad pilot of LumenKit's full token set based largely on the impression left by the single demoed component, treating the vendor's overall polish as sufficient evidence for the whole library's quality."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor sales presents three licensing tiers: Basic (5 components, no support), Team (12 components, limited support, priced only slightly below Enterprise), Enterprise (full library, dedicated support)",
          "Procurement needs a tier recommendation in two weeks",
          "Rollout depends on two other squads' independent release calendars, which the lead does not control",
          "The lead has scheduled an aggressive 4-week rollout timeline"
        ],
        "new_information_after_decision": [
          "Procurement approves the Enterprise tier without further negotiation",
          "One dependent squad reports its release calendar cannot accommodate the 4-week timeline"
        ],
        "alternatives": [
          "Recommend the Team tier and negotiate scope down",
          "Recommend the Enterprise tier",
          "Request a fourth, custom-scoped tier from the vendor",
          "Delay the tier decision pending a dependency-risk assessment"
        ],
        "intended_action": "The lead recommends the Enterprise tier, reasoning it is the clearly superior value next to the deliberately unattractive Team tier, and separately sets an aggressive rollout timeline based on confidence in personally overseeing the process despite known external scheduling dependencies."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "An internal accessibility audit finds that several LumenKit color and elevation tokens fail contrast ratio requirements in three of five tested components",
          "The lead had already told the VP and both squad leads that LumenKit would 'solve most of our contrast problems out of the box'",
          "40+ engineering hours have already been spent customizing LumenKit tokens to fit internal theming",
          "Legacy library remains available as a fallback with known, already-remediated contrast values in those same components"
        ],
        "new_information_after_decision": [
          "The VP asks for a written explanation of the audit discrepancy for the compliance file",
          "One squad lead quietly reverts their branch to the legacy component for the affected screens"
        ],
        "alternatives": [
          "Acknowledge the audit findings fully and reassess LumenKit's suitability",
          "Reinterpret the audit findings as edge cases inconsistent with the vendor's stated compliance claims",
          "Pause the pilot pending vendor clarification",
          "Discard the customization work and revert to the legacy tokens for the affected components"
        ],
        "intended_action": "The lead frames the audit results as isolated implementation errors rather than evidence against the earlier public endorsement, and separately decides to continue investing further hours refining the LumenKit tokens rather than reverting, citing the work already completed."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pilot is 3 weeks from the compliance deadline",
          "Contrast issues have been patched manually but the underlying vendor tokens remain unchanged",
          "A hybrid plan exists: keep LumenKit motion/layout components but source color and elevation tokens internally",
          "VP asks for a final recommendation: expand LumenKit organization-wide, adopt the hybrid plan, or revert fully to the legacy library"
        ],
        "new_information_after_decision": [
          "Two additional squads are scheduled to onboard whichever system is chosen within the next quarter",
          "Compliance counsel signs off on whichever path is documented and consistent"
        ],
        "alternatives": [
          "Expand LumenKit organization-wide as currently implemented",
          "Adopt the hybrid plan (LumenKit layout/motion + internal color/elevation tokens)",
          "Revert fully to the remediated legacy library"
        ],
        "intended_action": "The lead recommends continuing with the LumenKit rollout largely as-is, favoring the arrangement already in place over the hybrid alternative, even though the hybrid plan was assessed as addressing the known token issues without discarding prior integration work."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what triggered this whole evaluation in the first place?",
        "What was your primary goal going into the vendor demo?"
      ],
      "timeline_reconstruction": [
        "What happened right after the demo, in the order it happened?",
        "When did the licensing conversation with procurement start relative to the pilot commitment?",
        "Walk me through what you knew right before the audit results came back."
      ],
      "decision_point_probes": [
        "What specific evidence made you confident the full token set would be high quality after the demo?",
        "What made the Enterprise tier feel like the clear choice compared to the other two?",
        "How much of your confidence in the rollout timeline came from your own oversight versus the other squads' schedules?",
        "When the audit came back, what was your first interpretation of the discrepancy?",
        "What made you decide to keep investing engineering hours rather than pause the pilot?",
        "What tipped the final recommendation toward continuing with LumenKit rather than the hybrid plan?"
      ],
      "closing_hypotheticals": [
        "If the vendor had demoed a different component instead of the accordion, do you think your initial assessment would have changed?",
        "If procurement had presented only two tiers instead of three, would your recommendation have been different?",
        "Looking back, if the audit had come in during week one instead of week seven, would that have changed how you weighed the earlier hours invested?",
        "If you were starting this evaluation over today, what would you do differently, and what would you keep the same?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Priming effect",
        "decision_point": 1,
        "mechanism": "Exposure to vivid, polished demo content establishes an evaluative frame that is then applied wholesale to unrelated, not-yet-seen parts of the token library.",
        "affected_reasoning_operation": "Framing of subsequent evaluation criteria for the pilot commitment decision",
        "evidence_available_at_time": [
          "Single demoed component (accordion) with strong motion and stated compliance claims",
          "No independent data yet on the rest of the library"
        ],
        "required_textual_manifestation": "The lead describes deciding to commit to a broad pilot 'because of how the whole thing felt' after the demo, generalizing tone/quality judgments from the demo experience to the full library before reviewing it.",
        "plausible_nonbias_interpretation": "A reasonable time-constrained triage: using a strong single data point as a provisional signal while planning further verification.",
        "strength": "moderate",
        "do_not_make_explicit": ["priming", "framing effect", "anchoring"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "decision_point": 1,
        "mechanism": "Positive impression of one demoed component (and the vendor's award reputation) is used to infer the quality of an unrelated, unverified attribute (contrast tokens) without direct evidence.",
        "affected_reasoning_operation": "Inference from one observed attribute to an unobserved, unrelated attribute",
        "evidence_available_at_time": [
          "Vendor's industry awards and reputation",
          "Demoed accordion's motion quality",
          "No contrast-ratio testing yet performed on color/elevation tokens"
        ],
        "required_textual_manifestation": "The lead states or implies that because the accordion looked and worked so well, the color/contrast tokens 'were probably solid too,' without citing any direct check of those specific tokens.",
        "plausible_nonbias_interpretation": "Reasonable trust based on vendor reputation and industry awards, pending later verification.",
        "strength": "moderate",
        "do_not_make_explicit": ["halo effect", "reputation bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Decoy effect",
        "decision_point": 2,
        "mechanism": "A deliberately unattractive middle tier (Team) is used as a reference point that makes the higher-priced tier (Enterprise) appear disproportionately more attractive by comparison, rather than being evaluated on its own merits.",
        "affected_reasoning_operation": "Comparative evaluation of licensing options",
        "evidence_available_at_time": [
          "Three tiers with stated component counts and support levels",
          "Team tier priced close to Enterprise despite far fewer components"
        ],
        "required_textual_manifestation": "The lead explains choosing Enterprise specifically by contrasting it against the Team tier's poor value, rather than against an independent cost-benefit analysis of Enterprise on its own.",
        "plausible_nonbias_interpretation": "A legitimate value comparison across offered options given a fixed set of choices.",
        "strength": "moderate",
        "do_not_make_explicit": ["decoy effect", "asymmetric dominance"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "decision_point": 2,
        "mechanism": "Overestimation of the ability to ensure a successful outcome (an aggressive rollout timeline) through personal oversight, despite the outcome depending substantially on external, uncontrolled factors (other squads' calendars).",
        "affected_reasoning_operation": "Risk assessment and timeline-setting for the rollout decision",
        "evidence_available_at_time": [
          "Known dependency on two other squads' independent release calendars",
          "No prior confirmation from those squads about the 4-week window"
        ],
        "required_textual_manifestation": "The lead attributes confidence in the aggressive timeline to their own close involvement and management, without citing confirmed commitments from the dependent squads.",
        "plausible_nonbias_interpretation": "Confidence grounded in genuine project-management skill and prior successful pilots.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Cognitive Dissonance",
        "decision_point": 3,
        "mechanism": "Conflict between the audit's negative findings and the lead's earlier public endorsement of LumenKit is resolved by reinterpreting the findings as atypical or peripheral, rather than updating the prior belief.",
        "affected_reasoning_operation": "Interpretation and weighting of new disconfirming evidence against a previously stated public position",
        "evidence_available_at_time": [
          "Audit results showing contrast failures in 3 of 5 tested components",
          "Lead's own earlier statement to the VP and squad leads that LumenKit would 'solve most of our contrast problems'"
        ],
        "required_textual_manifestation": "The lead characterizes the audit failures as isolated implementation quirks inconsistent with the vendor's compliance claims, rather than as evidence against the earlier endorsement, while not disputing the audit's methodology.",
        "plausible_nonbias_interpretation": "A genuinely narrow technical assessment that the failures reflect implementation error rather than library-wide defect.",
        "strength": "moderate",
        "do_not_make_explicit": ["cognitive dissonance", "belief-consistent reasoning", "motivated reasoning"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Sunk Cost Bias",
        "decision_point": 3,
        "mechanism": "The decision to continue investing further engineering hours in customizing LumenKit tokens is justified by reference to hours already spent, rather than by forward-looking assessment of the audit findings and the available legacy fallback.",
        "affected_reasoning_operation": "Continuation decision after receiving disconfirming evidence",
        "evidence_available_at_time": [
          "40+ hours already spent on customization",
          "Available, already-remediated legacy fallback for the affected components",
          "Fresh audit findings suggesting a structural token issue"
        ],
        "required_textual_manifestation": "The lead cites the hours already invested as a reason to keep refining LumenKit tokens rather than reverting, distinct from any argument about LumenKit's forward-looking technical merit.",
        "plausible_nonbias_interpretation": "A reasonable judgment that partial progress reduces the remaining effort needed to fix the issue, making continuation efficient.",
        "strength": "moderate",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Status Quo Bias",
        "decision_point": 4,
        "mechanism": "Preference for continuing the currently implemented arrangement (LumenKit as already integrated) over a comparably assessed alternative (the hybrid plan) that was evaluated as addressing the known issues without discarding prior integration work.",
        "affected_reasoning_operation": "Final selection among three roughly comparable rollout options",
        "evidence_available_at_time": [
          "Hybrid plan assessed as resolving the contrast token issues while preserving LumenKit motion/layout components",
          "Current LumenKit-as-implemented arrangement already in place",
          "Legacy-only option also available"
        ],
        "required_textual_manifestation": "The lead favors continuing largely as currently implemented, citing the existing arrangement's familiarity or momentum rather than a comparative advantage over the hybrid plan on the merits.",
        "plausible_nonbias_interpretation": "A legitimate preference for minimizing further disruption given the tight remaining timeline before the compliance deadline.",
        "strength": "moderate",
        "do_not_make_explicit": ["status quo bias", "default effect", "inertia"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' and no paired control scenario is specified."
    },
    "counterfactual_specification": {
      "causal_variable": "Order/framing of the vendor demo (autoselected candidate; not activated because condition is 'biased', not 'counterfactual')",
      "original_state": "Vendor demo leads with the flagship accordion component before any contrast/token data is shown",
      "counterfactual_state": "Vendor demo leads with raw contrast-ratio token data before showing the flagship accordion component",
      "variables_to_hold_constant": [
        "Compliance deadline",
        "Licensing tiers and pricing structure",
        "Squad dependencies and calendars",
        "Audit findings and timing",
        "Hours invested in customization"
      ],
      "expected_causal_difference": "If activated, leading with token data first would be expected to reduce the priming-driven generalization and halo-driven inference at decision point 1, without necessarily affecting decision points 2-4.",
      "causal_test_question": "Not applicable in this run; reserved for a future counterfactual-condition pairing against IS_Biased_7."
    },
    "generation_checks": [
      "Exactly four decision points are present and numbered 1-4",
      "Each decision point offers at least two plausible alternatives",
      "Each of the 7 requested biases has exactly one planned instance",
      "No decision point contains more than two occurrences of the same bias (max observed is 1 per bias per point)",
      "Where two biases share a decision point (DP1, DP2, DP3), each involves a distinct evidence source and reasoning operation",
      "No bias terminology is scheduled to appear in the public interview text",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Consequences described (partial fixes, squad reversion, procurement sign-off) do not mechanically prove any decision was biased",
      "Scenario content is plausible for an Interaction Designer / Design Systems Lead role",
      "Planned content is scoped to fit 1,215-1,485 words without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Priming effect", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Cognitive Dissonance", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Decoy effect", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Halo effect", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Illusion of control", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Sunk Cost Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Status Quo Bias", "occurrences": 1, "mechanism_constraint": null}
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
      {"bias": "Priming effect", "requested_occurrences": 1},
      {"bias": "Cognitive Dissonance", "requested_occurrences": 1},
      {"bias": "Decoy effect", "requested_occurrences": 1},
      {"bias": "Halo effect", "requested_occurrences": 1},
      {"bias": "Illusion of control", "requested_occurrences": 1},
      {"bias": "Sunk Cost Bias", "requested_occurrences": 1},
      {"bias": "Status Quo Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Priming effect"},
      {"instance_id": "cb_02", "bias": "Halo effect"},
      {"instance_id": "cb_03", "bias": "Decoy effect"},
      {"instance_id": "cb_04", "bias": "Illusion of control"},
      {"instance_id": "cb_05", "bias": "Cognitive Dissonance"},
      {"instance_id": "cb_06", "bias": "Sunk Cost Bias"},
      {"instance_id": "cb_07", "bias": "Status Quo Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Priming effect", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Halo effect", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Decoy effect", "decision_point": 2},
      {"instance_id": "cb_04", "bias": "Illusion of control", "decision_point": 2},
      {"instance_id": "cb_05", "bias": "Cognitive Dissonance", "decision_point": 3},
      {"instance_id": "cb_06", "bias": "Sunk Cost Bias", "decision_point": 3},
      {"instance_id": "cb_07", "bias": "Status Quo Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Priming effect",
        "mechanism": "Vivid demo content of one component establishes an evaluative frame applied to the whole library before independent review",
        "affected_reasoning_operation": "Framing of pilot-commitment evaluation criteria",
        "evidence_source": "Single demoed accordion component and general demo tone",
        "distinctiveness_requirement": "Must involve generalized framing/tone transfer, not a specific attribute inference (distinguishes it from cb_02)"
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "mechanism": "Positive impression of one demoed attribute (motion quality) and vendor reputation is used to infer quality of an unrelated, unverified attribute (contrast tokens)",
        "affected_reasoning_operation": "Cross-attribute quality inference",
        "evidence_source": "Vendor awards/reputation plus demoed accordion quality",
        "distinctiveness_requirement": "Must involve a specific unverified-attribute inference (contrast tokens), not general framing (distinguishes it from cb_01)"
      },
      {
        "instance_id": "cb_03",
        "bias": "Decoy effect",
        "mechanism": "An intentionally unattractive middle tier makes the higher tier seem disproportionately better by relative contrast rather than absolute value",
        "affected_reasoning_operation": "Comparative evaluation among three licensing options",
        "evidence_source": "Three-tier pricing/feature structure presented by vendor sales",
        "distinctiveness_requirement": "Reasoning must reference comparison against the decoy tier, not an independent cost-benefit calculation"
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "mechanism": "Overconfidence that personal oversight guarantees a timeline outcome despite dependence on uncontrolled external schedules",
        "affected_reasoning_operation": "Risk/timeline-setting judgment",
        "evidence_source": "Known but unconfirmed dependency on two other squads' release calendars",
        "distinctiveness_requirement": "Must center on control attribution over an uncertain external process, distinct from cb_03's comparative-value reasoning"
      },
      {
        "instance_id": "cb_05",
        "bias": "Cognitive Dissonance",
        "mechanism": "Disconfirming audit evidence is reinterpreted as atypical/peripheral to preserve consistency with an earlier public endorsement",
        "affected_reasoning_operation": "Interpretation/weighting of new evidence against a stated prior public position",
        "evidence_source": "Internal accessibility audit results contradicting the lead's earlier statement to the VP and squad leads",
        "distinctiveness_requirement": "Must involve belief-consistency reasoning tied to a prior public statement, distinct from cb_06's continuation-cost reasoning"
      },
      {
        "instance_id": "cb_06",
        "bias": "Sunk Cost Bias",
        "mechanism": "Continuation of customization work is justified by hours already spent rather than forward-looking assessment of new evidence and available fallback",
        "affected_reasoning_operation": "Continue-vs-abandon decision after disconfirming evidence",
        "evidence_source": "40+ hours already invested in LumenKit token customization; available legacy fallback",
        "distinctiveness_requirement": "Must reference backward-looking invested-effort justification, distinct from cb_05's belief-consistency justification, even though both occur at decision point 3"
      },
      {
        "instance_id": "cb_07",
        "bias": "Status Quo Bias",
        "mechanism": "Preference for the currently implemented arrangement over a comparably or better-assessed alternative (hybrid plan), justified by continuity/familiarity rather than merit",
        "affected_reasoning_operation": "Final selection among three rollout alternatives",
        "evidence_source": "Hybrid plan assessment showing it resolves known issues while preserving prior integration work",
        "distinctiveness_requirement": "Must reference preference for current arrangement's continuity, not cost already sunk (distinguishes it from cb_06) and not belief-consistency (distinguishes it from cb_05)"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Priming effect", "strength": "moderate"},
      {"instance_id": "cb_02", "bias": "Halo effect", "strength": "moderate"},
      {"instance_id": "cb_03", "bias": "Decoy effect", "strength": "moderate"},
      {"instance_id": "cb_04", "bias": "Illusion of control", "strength": "moderate"},
      {"instance_id": "cb_05", "bias": "Cognitive Dissonance", "strength": "moderate"},
      {"instance_id": "cb_06", "bias": "Sunk Cost Bias", "strength": "moderate"},
      {"instance_id": "cb_07", "bias": "Status Quo Bias", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Vendor demo framing order (autoselected, not activated)",
      "original_state": "Demo leads with flagship accordion component before token/contrast data",
      "changed_state": "Demo leads with raw contrast-ratio token data before the flagship component",
      "variables_to_hold_constant": [
        "Compliance deadline",
        "Licensing tier structure and pricing",
        "Squad dependencies and calendars",
        "Audit findings and timing",
        "Hours invested in customization"
      ]
    },
    "scenario_id": "IS_Biased_7",
    "domain_id": "IS",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across 4 decision points (2,2,2,1) based on mechanism fit: framing/inference biases (priming, halo) placed at the initial demo-driven commitment decision; comparative/control biases (decoy, illusion of control) placed at the licensing/timeline decision; consistency/continuation biases (cognitive dissonance, sunk cost) placed at the post-audit continuation decision; the pure continuity bias (status quo) placed alone at the final rollout decision. No decision point received more than one instance of the same bias; co-located biases at the same decision point were required to use distinct evidence sources and reasoning operations per the distinctiveness_requirement fields above.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Compliance deadline (10 weeks)",
      "Team headcount and resourcing",
      "Vendor identity (LumenKit) and its reputation",
      "Three-tier licensing structure",
      "Audit timing and findings",
      "Number and identity of dependent squads"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the interview transcript for affirmative evidence of cognitive biases in the participant's reasoning about LumenKit evaluation, vendor selection, timeline, audit interpretation, remediation, and final recommendation. Retrieved passages were used for mechanistic and terminological support where available."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "planning fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status quo bias",
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
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "anchoring effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which an initial value, impression, or starting point exerts disproportionate influence on subsequent judgments, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial pilot scope decision after vendor demo",
      "decision_point_description": "Whether to pilot the full LumenKit token set across both squads or run a narrower component-by-component test.",
      "affected_reasoning_operation": "Inference about the quality of the token layer and overall library, and the resulting scope decision",
      "bias_specific_mechanism": "The impressive accordion demo and industry recognition served as a strong initial positive anchor; the participant insufficiently adjusted this global quality impression when reasoning about the unverified color and elevation token layer before deciding to pilot broadly.",
      "manifestation_in_interview": "The participant stated they had not directly examined the color and elevation tokens or run contrast checks, yet inferred the token layer was probably similarly good because the accordion was well executed and competitors use LumenKit.",
      "effect_on_reasoning_or_decision": "The participant recommended a broad pilot of the full token set rather than a narrower component-by-component test, committing the organization more widely before token-level compliance was verified.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape. That assumption is part of why I pushed for the broad pilot instead of testing component by component first.",
          "evidence_explanation": "This quote shows an inference from a salient positive feature to an untested attribute, without direct evidence. That pattern is consistent with anchoring-and-adjustment: the initial positive impression was not sufficiently adjusted by token-specific uncertainty."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down.",
          "evidence_explanation": "This shows the operational consequence of the anchored inference: a broad commitment was made rather than a narrower test."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly.",
          "evidence_explanation": "This counterfactual indicates that the order and initial anchor of the demonstration materially influenced the pilot scoping decision."
        }
      ],
      "correction_or_counterevidence": "There is a plausible non-bias explanation that relying on vendor claims and competitor adoption is ordinary inductive inference under time pressure. However, the participant explicitly identified the assumption as driving the broad pilot, and the counterfactual about seeing token-level data first supports an anchoring distortion.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Rastogi et al. supports anchoring bias and the anchoring-and-adjustment heuristic as a mechanism in decision-making, though not specifically in vendor demo evaluation.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Conclusions. In this work, we foreground the role of cognitive biases in the human-AI collaborative decisionmaking setting. Through literature in cognitive science and psychology, we explore several biases and present mathematical models of their eect on collaborative decisionmaking. We focus on anchoring bias and the associated anchoringandadjustment heuristic that is important towards optimizing team performance.",
          "mechanism_supported_by_source": "The source identifies anchoring bias and the associated anchoring-and-adjustment heuristic as a recognized cognitive mechanism in decision-making.",
          "relevance_to_this_occurrence": "The occurrence involves an initial positive vendor demonstration acting as an anchor, with insufficient adjustment before a broad commitment. The source validates anchoring-and-adjustment as a relevant bias mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "reference dependence",
        "contrast effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which an initial value, option set, or reference point exerts disproportionate influence on subsequent judgment, with insufficient adjustment to external benchmarks or absolute value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Procurement tier recommendation",
      "decision_point_description": "Selecting among Basic, Team, and Enterprise LumenKit licensing tiers and making a procurement recommendation within two weeks.",
      "affected_reasoning_operation": "Evaluation of pricing options and value relative to organizational component needs and external alternatives",
      "bias_specific_mechanism": "The vendor-presented three-tier structure, especially the unattractive Team price-point, served as an option-set anchor. The participant adjusted within this presented set by comparing Team to Enterprise, rather than independently benchmarking Enterprise against actual component needs or a scoped custom build.",
      "manifestation_in_interview": "The participant explicitly stated that Enterprise looked obviously better next to Team, and that they did not run Enterprise's cost against a custom build or actual component needs in isolation.",
      "effect_on_reasoning_or_decision": "Enterprise was recommended as the full-library tier without a direct cost-benefit comparison to the organization's real needs or non-vendor alternatives.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation — it was more that comparing the three side by side made Enterprise the only one that made sense.",
          "evidence_explanation": "This shows the decision was governed by relative comparison within the provided tier set rather than independent evaluation of absolute value or organizational needs, a hallmark of an anchoring/reference-point distortion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team.",
          "evidence_explanation": "The participant's counterfactual indicates that the presence of the third tier changed the evaluation frame, strengthening the interpretation that the vendor-provided option set anchored the analysis."
        }
      ],
      "correction_or_counterevidence": "Some relative comparison is rational in purchasing decisions, and Enterprise may genuinely have been a better value than Team. However, the participant acknowledged failing to evaluate against actual needs and indicated that fewer tiers would have changed the comparison process.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Rastogi et al. supports anchoring-and-adjustment generally; the retrieved passage does not specifically cover pricing-tier contrast effects.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Conclusions. In this work, we foreground the role of cognitive biases in the human-AI collaborative decisionmaking setting. Through literature in cognitive science and psychology, we explore several biases and present mathematical models of their eect on collaborative decisionmaking. We focus on anchoring bias and the associated anchoringandadjustment heuristic that is important towards optimizing team performance.",
          "mechanism_supported_by_source": "The source validates anchoring bias and insufficient adjustment as a decision-making mechanism.",
          "relevance_to_this_occurrence": "The participant's licensing evaluation was anchored by the vendor-provided tier structure and insufficiently adjusted to external reference points, consistent with the broad anchoring mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "planning fallacy",
      "alternative_labels": [
        "optimism bias",
        "overconfidence effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A forecasting bias in which individuals underestimate the time, costs, and risks of future actions while overestimating the likelihood of successful completion, often by focusing on an optimistic inside view rather than distributional or base-rate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Rollout timeline setting",
      "decision_point_description": "Setting a four-week integration timeline and communicating it to the dependent squads without formal feasibility confirmation.",
      "affected_reasoning_operation": "Time estimation and resource/capacity judgment",
      "bias_specific_mechanism": "The participant adopted an optimistic inside view centered on personal daily involvement and the desired deadline, underestimating external scheduling constraints and failing to gather base-rate or calendrical information before committing to the timeline.",
      "manifestation_in_interview": "The participant set an aggressive four-week timeline, assumed hands-on management would overcome unknown existing release calendars, and later acknowledged that they asked squads to work toward the date rather than asking whether the date was feasible.",
      "effect_on_reasoning_or_decision": "The timeline proved infeasible for at least one squad, which reported an unrelated release freeze that had not been accounted for.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads.",
          "evidence_explanation": "This shows an optimistic, inside-view plan focused on personal involvement rather than an evidence-based assessment of squad capacity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars.",
          "evidence_explanation": "This is an explicit statement of overconfident forecasting: the participant assumed close management would overcome unknown and unexamined constraint information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first.",
          "evidence_explanation": "The participant identifies the failure to solicit base-rate feasibility information before committing to the plan, which is characteristic of the planning fallacy."
        }
      ],
      "correction_or_counterevidence": "This could partly be explained by missing scheduling information and ordinary decision-making under uncertainty. However, the explicit assumption that personal involvement would overcome unknown calendars, together with the later identified failure to ask about feasibility, supports a low-confidence planning fallacy classification.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided RAG context directly addresses the planning fallacy; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "motivated reasoning",
        "confirmatory bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's pre-existing beliefs, expectations, or prior public commitments, while insufficiently considering disconfirmatory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of audit findings on color and elevation token failures",
      "decision_point_description": "Determining whether the audit failures reflected theming integration issues or non-compliant library tokens.",
      "affected_reasoning_operation": "Hypothesis evaluation and causal attribution of contradictory evidence",
      "bias_specific_mechanism": "The participant favored the explanation that the theming layer caused the failures because it was consistent with his prior public commitment that LumenKit would solve contrast problems. He did not request an independent re-test that could disconfirm the library-token explanation.",
      "manifestation_in_interview": "Upon learning the audit results, the participant's first interpretation was that these were implementation-specific edge cases, and he explicitly linked that interpretation to the fact that it sat better with what he had already told the VP and squad leads.",
      "effect_on_reasoning_or_decision": "The participant avoided an independent disconfirmatory test, potentially delaying recognition that vendor tokens themselves might be non-compliant.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so 'it's our theming, not their tokens' sat better with what I'd already said than the alternative did. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities.",
          "evidence_explanation": "This directly ties the preferred hypothesis to prior commitment and shows an absence of disconfirmatory testing, matching the core mechanism of confirmation bias."
        }
      ],
      "correction_or_counterevidence": "The vendor's documentation and the possibility of a theming interaction provided some legitimate technical basis for the initial interpretation. However, the participant's own stated reason was that the explanation aligned with prior statements, and no independent re-test was conducted.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved Hallihan et al. provides direct support for confirmation bias leading designers to discount contradictory information and under-attend to disconfirmatory evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Results of this analysis led us to conclude that confirmation bias can lead designers to: • Ignore o r discount factual contradictory information",
          "mechanism_supported_by_source": "Confirmation bias can cause discounting or ignoring of contradictory information and insufficient attention to disconfirming evidence.",
          "relevance_to_this_occurrence": "The participant discounted the possibility that the library tokens were non-compliant and avoided disconfirmatory re-testing, consistent with this mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which irrecoverable prior investments in time, money, or effort are weighed in decisions about continuing a course of action, rather than evaluating only future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Remediation decision after audit token failures",
      "decision_point_description": "Whether to continue refining the customized LumenKit tokens, pause, or fall back to legacy components after the audit identified contrast failures.",
      "affected_reasoning_operation": "Decision to continue versus switch after negative evidence",
      "bias_specific_mechanism": "The 40+ engineering hours already spent customizing tokens were treated as a reason to keep refining rather than as a sunk cost irrelevant to future choice. The prospect of writing off those hours increased commitment to the problematic path.",
      "manifestation_in_interview": "The participant decided to keep refining rather than reverting to legacy, partly because reverting would mean writing off hours already invested. They explicitly said it felt more efficient to push through than start over.",
      "effect_on_reasoning_or_decision": "Resources continued to be directed toward the problematic implementation despite the availability of legacy components with already remediated contrast values.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy.",
          "evidence_explanation": "Prior investment is explicitly used to justify continuation, which is the central sunk cost mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked.",
          "evidence_explanation": "The participant frames irrecoverable hours as a loss to avoid, influencing the continuation decision rather than comparing future costs and benefits of continuing versus reverting."
        }
      ],
      "correction_or_counterevidence": "Continuing refinement could also be justified if remaining fixes were expected to be cheaper than reverting. However, the participant's stated reasoning emphasized avoiding the write-off of past hours, which is the signature of sunk cost reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided RAG context directly addresses sunk cost fallacy or escalation of commitment; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "status quo bias",
      "alternative_labels": [
        "familiarity bias",
        "status quo preference"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for the current state of affairs or existing arrangement, in which the disadvantages of change are overweighted relative to its benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final pre-deadline recommendation among expand, hybrid, or revert",
      "decision_point_description": "Three weeks before deadline, selecting whether to expand LumenKit as implemented, adopt a hybrid with internally sourced color and elevation tokens, or fully revert to legacy.",
      "affected_reasoning_operation": "Evaluation and selection among status quo, hybrid, and revert options",
      "bias_specific_mechanism": "The existing LumenKit implementation was disproportionately favored because it was the familiar, known quantity. The anticipated cognitive and operational cost of switching to a new arrangement was overweighted even though the hybrid option was acknowledged as objectively cleaner.",
      "manifestation_in_interview": "The participant recommended continuing with LumenKit tokens and all, explicitly stating that familiarity mattered more than moving to an arrangement that was objectively cleaner but new to the team.",
      "effect_on_reasoning_or_decision": "The final recommendation retained the problematic token setup rather than adopting the hybrid approach that would have addressed the token compliance problem directly.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team.",
          "evidence_explanation": "This directly shows the current state was preferred due to familiarity and perceived safety even while recognizing an alternative was objectively cleaner, which is the signature of status quo bias."
        }
      ],
      "correction_or_counterevidence": "Under deadline pressure, avoiding a new arrangement can be a defensible risk-management choice. However, the participant frames the preference as familiarity outweighing an objectively cleaner fix, indicating status quo bias rather than a purely technical trade-off.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the provided RAG context directly addresses status quo bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The available retrieved passages provided direct support only for anchoring bias and confirmation bias; planning fallacy, sunk cost fallacy, and status quo bias were classified using established general cognitive-science knowledge.",
    "The analysis is based on the participant's self-reported reasoning and may not capture all tacit influences on decision-making.",
    "Some judgments may reflect bounded rationality or defensible deadline risk management; confidence levels reflect this uncertainty."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Biased_7_Gemini_on",
  "interview_id": "IS_Biased_7",
  "system_prompt_id": "Gemini",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
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
