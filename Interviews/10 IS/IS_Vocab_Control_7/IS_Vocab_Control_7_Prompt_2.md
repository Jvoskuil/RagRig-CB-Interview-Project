You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IS_Vocab_Control_7",
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
