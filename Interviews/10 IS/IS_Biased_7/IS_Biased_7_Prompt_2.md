You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IS_Biased_7",
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
