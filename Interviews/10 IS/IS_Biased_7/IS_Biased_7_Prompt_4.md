You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the LumenKit evaluation, not whether the outcome was "right." Everything you share stays in the design systems research archive. Sound okay?

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

Participant: My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. I didn't request an independent re-test of the vendor's out-of-box tokens without our theming applied to actually separate those two possibilities.

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

Participant: I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. We'd already built the governance docs, onboarding materials, and squad training around the current implementation, and switching structure again this close to the deadline felt like more disruption than it was worth, even with the hybrid's technical case being reasonably strong.

Interviewer: If the audit had surfaced in week one instead of week seven, do you think that would have changed how you weighed the hours already spent?

Participant: Probably — with less invested, reverting or pivoting to the hybrid would've felt like a much smaller loss.

Interviewer: If the vendor demo had opened with contrast-ratio data instead of the accordion, would your initial pilot decision have gone differently?

Participant: Possibly. If I'd seen the token-level numbers first, I might've scoped the pilot narrower before committing broadly.

Interviewer: If procurement had only offered two tiers instead of three, would Enterprise still have been the obvious pick?

Participant: Harder to say — I might have actually priced out Enterprise against our real component needs rather than against Team.

Interviewer: Last one — starting over today, what would you keep, and what would you change?

Participant: I'd keep the urgency and the willingness to bring in outside tooling under deadline pressure — that part was right. I'd change how early I locked in public commitments about what the library would solve, and I'd get squad confirmation on timelines before setting them rather than after.

Interviewer: This has been really useful. Thanks for being so candid about the reasoning, not just the outcome.

Participant: No problem — it's easier to see it laid out like this than it was living through it week to week.}}
- Hidden generation specification: {{"hidden_validation_specification": {
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
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "IS_Biased_7",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Enterprise design-systems procurement and accessibility-compliance implementation",
    "role": "Design systems lead managing a small platform design and engineering team",
    "objective": "Evaluate, license, and deploy an external component library quickly enough to help two customer-facing squads meet a WCAG 2.2 AA deadline.",
    "incident_type": "Time-pressured vendor evaluation and implementation decision in which an initially broad adoption plan encountered accessibility-audit failures and required a continuation, hybrid, or reversion decision.",
    "confidence": 0.98
  },
  "structure_audit": {
    "estimated_word_count": 1330,
    "within_target_range": true,
    "decision_point_count": 5,
    "decision_points": [
      {
        "id": 1,
        "summary": "Recommend a broad pilot of LumenKit's full token set across both squads after the vendor demo.",
        "evidence_before": [
          "A ten-week WCAG 2.2 AA compliance deadline.",
          "Known internal contrast and focus-state debt.",
          "A vendor demo focused heavily on a polished accordion component.",
          "Vendor claims of AA-compliant color defaults.",
          "Competitor adoption and industry recognition."
        ],
        "evidence_after": [
          "A three-week sandbox with a limited component set.",
          "Squad leads express interest but want pricing before committing engineering time."
        ],
        "goals_constraints": [
          "Avoid months of internal remediation work.",
          "Meet the accessibility deadline.",
          "Select an implementation approach under incomplete independent verification."
        ],
        "alternatives": [
          "Pilot the full token set broadly.",
          "Pilot selected components or tokens narrowly.",
          "Run independent contrast checks before committing to pilot scope.",
          "Continue remediation of the internal library."
        ],
        "decision_basis": "The participant generalized from the demo's perceived overall quality and inferred likely token quality from the accordion demonstration, vendor reputation, and compliance claims.",
        "time_pressure": "High; the organization had approximately ten weeks to achieve WCAG 2.2 AA coverage.",
        "uncertainty": "High; no independent contrast checks had been run and the sandbox did not yet establish token-level compliance."
      },
      {
        "id": 2,
        "summary": "Recommend the Enterprise licensing tier.",
        "evidence_before": [
          "Procurement required a recommendation within two weeks.",
          "Basic offered five components and no support.",
          "Team offered twelve components and limited support at a price close to Enterprise.",
          "Enterprise offered the full library and dedicated support."
        ],
        "evidence_after": [
          "Enterprise becomes the participant's tier recommendation."
        ],
        "goals_constraints": [
          "Obtain sufficient components and support.",
          "Make a procurement recommendation within the required window.",
          "Assess value despite no stated independent analysis of actual component needs or substitutes."
        ],
        "alternatives": [
          "Basic.",
          "Team.",
          "Enterprise.",
          "A scoped custom build or a needs-based alternative, which was not actually analyzed."
        ],
        "decision_basis": "The participant judged Enterprise primarily relative to the unattractive Team tier rather than through an isolated cost-benefit assessment against actual needs or substitutes.",
        "time_pressure": "Moderate to high; recommendation due within two weeks.",
        "uncertainty": "Moderate; actual component needs, implementation scope, and the economic comparison with custom remediation were not fully assessed."
      },
      {
        "id": 3,
        "summary": "Set a four-week rollout timeline before obtaining formal confirmation from the two dependent squads.",
        "evidence_before": [
          "The rollout required coordination with two dependent squads.",
          "The participant expected to manage integration personally and hold daily syncs.",
          "The squads' release calendars had not been formally confirmed."
        ],
        "evidence_after": [
          "One squad reports an unrelated release freeze that prevents the four-week window."
        ],
        "goals_constraints": [
          "Move implementation quickly enough to preserve the compliance schedule.",
          "Coordinate around external squad calendars and release constraints."
        ],
        "alternatives": [
          "Set the four-week deadline immediately.",
          "Ask squad leads whether four weeks was feasible before setting the date.",
          "Set a conditional or staged implementation timeline."
        ],
        "decision_basis": "The participant treated close personal oversight as sufficient to overcome unverified external calendar constraints.",
        "time_pressure": "High; the overall accessibility deadline constrained rollout duration.",
        "uncertainty": "High; dependent squad capacity and release-calendar restrictions were unverified."
      },
      {
        "id": 4,
        "summary": "Continue refining customized LumenKit tokens after the internal audit found contrast failures, rather than pause or revert to already-remediated legacy components.",
        "evidence_before": [
          "The internal audit found contrast-ratio failures in three of five tested components.",
          "The participant had publicly stated that LumenKit would solve most contrast problems out of the box.",
          "Vendor documentation stated that the library was AA compliant.",
          "More than forty engineering hours had already been spent customizing tokens.",
          "Legacy components already had remediated contrast values for the affected screens."
        ],
        "evidence_after": [
          "The participant continued refinement.",
          "The VP requested a written explanation for the compliance file.",
          "One squad lead independently reverted affected screens to legacy components."
        ],
        "goals_constraints": [
          "Resolve compliance failures before the deadline.",
          "Avoid losing prior implementation effort.",
          "Provide an auditable explanation for the compliance file."
        ],
        "alternatives": [
          "Continue refining LumenKit token customization.",
          "Pause and independently retest out-of-box tokens without theming.",
          "Revert affected screens to legacy components.",
          "Move to a hybrid implementation."
        ],
        "decision_basis": "The participant initially discounted audit findings as potentially implementation-specific and then explicitly justified continuation partly by prior engineering hours.",
        "time_pressure": "High; the audit occurred approximately seven weeks into a ten-week compliance window.",
        "uncertainty": "Moderate to high; the participant did not separate vendor-token defects from local theming interactions through an independent retest."
      },
      {
        "id": 5,
        "summary": "Recommend retaining LumenKit tokens and the largely current implementation rather than moving to the technically stronger hybrid arrangement.",
        "evidence_before": [
          "The hybrid option would preserve LumenKit layout and motion components while replacing problematic color and elevation tokens internally.",
          "The participant describes the hybrid option as arguably the cleanest technical fix.",
          "Governance documents, onboarding materials, and squad training had been built around the current implementation.",
          "The decision occurred three weeks before the deadline."
        ],
        "evidence_after": [
          "The participant recommends continuing largely as implemented, including LumenKit tokens."
        ],
        "goals_constraints": [
          "Meet the deadline.",
          "Resolve known token compliance problems.",
          "Avoid implementation disruption across squads."
        ],
        "alternatives": [
          "Expand the current LumenKit implementation organization-wide.",
          "Adopt the hybrid model.",
          "Revert fully to legacy."
        ],
        "decision_basis": "The participant privileges continuity of the existing arrangement and avoidance of near-term switching disruption over an option judged to address the identified technical problem more directly.",
        "time_pressure": "High; only three weeks remained before the compliance deadline.",
        "uncertainty": "Moderate; the practical switching burden is plausible, but the interview does not quantify whether it outweighed the hybrid option's compliance advantage."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "cb_01",
      "bias": "Priming effect",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "“After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down.”",
      "evidence_location": "Initial vendor-demo account, immediately after the description of a forty-minute accordion-focused demonstration.",
      "mechanism": "The vivid, highly positive opening demonstration establishes an overall evaluative frame for the vendor and makes broad adoption appear like the natural high-quality option before token-level compliance evidence is independently examined. The later probe—“If I'd seen the token-level numbers first, I might've scoped the pilot narrower”—provides direct retrospective evidence that presentation order affected the initial decision frame.",
      "strength": "moderate",
      "confidence": 0.79,
      "plausible_nonbias_explanation": "The broad pilot could partly reflect a rational response to an unusually short remediation deadline and a desire to evaluate system-level integration rather than isolated components.",
      "additional_evidence_needed": "No revision is required. If stronger causal identification were needed, the interview could elicit what evaluation criterion became salient after the accordion demonstration, but that is not necessary for moderate support.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, participant's explanation of why the full-token-set pilot was preferred.",
        "current_defect": "None material. The occurrence is distinguishable from the halo effect because it concerns broad evaluative framing and sequencing, while the halo occurrence concerns a specific inference about unverified contrast tokens.",
        "minimal_change_instruction": "Retain the existing account and the presentation-order counterfactual probe.",
        "preserve": [
          "The accordion-led demo order.",
          "The participant's broad-pilot recommendation.",
          "The separate explicit inference about contrast-token quality for cb_02."
        ],
        "avoid_creating": [
          "Do not add language that treats the vendor's fame or awards alone as the reason for the broad pilot; that would blur this occurrence with halo or social-proof reasoning.",
          "Do not add a second broad-pilot decision episode."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_02",
      "bias": "Halo effect",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "“But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape.”",
      "evidence_location": "Follow-up question about direct review of color and elevation tokens.",
      "mechanism": "The participant explicitly transfers a positive impression of demonstrated motion, keyboard handling, and graceful degradation, supplemented by favorable reputation cues, to an unrelated and unverified attribute: color and elevation token compliance.",
      "strength": "moderate",
      "confidence": 0.97,
      "plausible_nonbias_explanation": "Vendor-level quality consistency can be a reasonable preliminary prior, especially under time pressure; however, the participant acknowledges that no direct token review or contrast test occurred and uses the unrelated positive evidence as the basis for the inference.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, answer concerning unreviewed color and elevation tokens.",
        "current_defect": "None. The statement contains the required cross-attribute inference rather than merely a favorable general impression.",
        "minimal_change_instruction": "Retain the explicit contrast between the polished accordion and the unverified token layer.",
        "preserve": [
          "The absence of independent contrast testing.",
          "The distinction between the component's observed quality and token compliance.",
          "The separate presentation-order framing evidence for cb_01."
        ],
        "avoid_creating": [
          "Do not add evidence that the vendor supplied validated token test results before this inference; that would make the inference more justified and weaken the halo mechanism.",
          "Do not replace the participant's inference with a generic statement that the vendor seemed reputable."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_03",
      "bias": "Decoy effect",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "“Team was a bad deal—you’re paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that. I didn't really run Enterprise's cost against, say, a scoped custom build or against our actual component needs in isolation.”",
      "evidence_location": "Licensing-tier recommendation discussion.",
      "mechanism": "The Team tier functions as a relatively dominated middle option that increases the apparent attractiveness of Enterprise through local comparative contrast. The participant explicitly states that Enterprise looked compelling when positioned next to Team and was not evaluated independently against actual needs or external alternatives.",
      "strength": "moderate",
      "confidence": 0.94,
      "plausible_nonbias_explanation": "Enterprise may genuinely have been the best option because it included the full library and dedicated support at a small incremental price. The bias claim is supported because the participant identifies comparative contrast with Team, rather than an independent value analysis, as the primary decision basis.",
      "additional_evidence_needed": "None for a moderate occurrence. Evidence that Team was deliberately designed as a vendor sales decoy is not necessary to establish a decoy-like relative-choice mechanism in the participant's reasoning.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, participant's explanation of the Enterprise recommendation.",
        "current_defect": "None material. The reasoning explicitly references the inferior middle tier and disavows an isolated needs-based comparison.",
        "minimal_change_instruction": "Retain the phrase showing that Enterprise was judged 'sitting next to' Team and the omission of independent cost-benefit analysis.",
        "preserve": [
          "The three-tier structure.",
          "The procurement timing.",
          "The distinction from the rollout-timeline judgment."
        ],
        "avoid_creating": [
          "Do not add a fully quantified component-needs analysis that independently establishes Enterprise as optimal.",
          "Do not turn the episode into a generic anchoring account by removing the dominated Team tier."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_04",
      "bias": "Illusion of control",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "“I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars.”",
      "evidence_location": "Rollout-timeline discussion, following confirmation that dependent squads had not formally committed to the schedule.",
      "mechanism": "The participant attributes sufficient control over the outcome to personal oversight despite material, unconfirmed external dependencies—other squads' calendars and a release freeze—that the participant cannot personally control.",
      "strength": "strong",
      "confidence": 0.98,
      "plausible_nonbias_explanation": "Hands-on integration management can reduce coordination risk. It cannot reasonably guarantee that release freezes and squad capacity constraints will be overcome, especially when those constraints were not checked before setting the date.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, answer explaining the four-week timeline.",
        "current_defect": "None. The phrase 'regardless of their existing release calendars' directly identifies over-attribution of control over an external process.",
        "minimal_change_instruction": "Retain the unconfirmed dependency and the participant's confidence that personal daily management would make the schedule work.",
        "preserve": [
          "The separate procurement-tier decision as a distinct decision point.",
          "The subsequent discovery of the release freeze.",
          "The participant's role as active integration manager."
        ],
        "avoid_creating": [
          "Do not add evidence that the participant had authority to override release freezes or reallocate squad resources, because that would make the control attribution more realistic.",
          "Do not reframe the error solely as poor calendar checking; the unsupported control attribution is the necessary mechanism."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_05",
      "bias": "Cognitive Dissonance",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 4,
      "supporting_quote": "“My instinct was that these were implementation-specific edge cases—maybe our theming layer interacting oddly with their defaults—rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance.”",
      "evidence_location": "First interpretation of the internal accessibility-audit discrepancy.",
      "mechanism": "The text plausibly shows discounting disconfirming audit evidence through an implementation-specific explanation. However, it does not clearly establish that the reinterpretation served to preserve consistency with the participant's earlier public claim to the VP and squad leads, rather than being a potentially reasonable technical hypothesis based on the distinction between themed and out-of-box tokens.",
      "strength": "weak",
      "confidence": 0.68,
      "plausible_nonbias_explanation": "Theming layers can genuinely alter color relationships and contrast outcomes. Comparing an internal themed implementation with vendor documentation can rationally prompt a hypothesis that local implementation differs from the vendor's default configuration. The error is the failure to test that hypothesis, which alone is not cognitive dissonance.",
      "additional_evidence_needed": "A concise trace showing that the prior public endorsement made the implementation-specific interpretation more psychologically or evidentially attractive than the audit result. The trace should indicate motivated preservation of the earlier stance, not merely technical uncertainty.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_reasoning_revision",
        "location": "Decision point 4, immediately after the participant notes that the audit contradicted what had already been told to the VP and squad leads.",
        "current_defect": "The interview juxtaposes a prior public endorsement with an audit-discounting interpretation but does not make the belief-consistency link observable. The participant's explanation remains technically plausible and may instead reflect ordinary incomplete diagnostic work.",
        "minimal_change_instruction": "Add one subtle participant sentence indicating that, because the participant had already represented LumenKit as an out-of-the-box solution, the participant initially gave more weight to the 'our theming caused it' explanation than the audit's implication about the vendor tokens. Keep the participant's failure to request the independent out-of-box retest.",
        "preserve": [
          "The audit finding in three of five tested components.",
          "The vendor documentation's AA-compliance claim.",
          "The previously stated endorsement to the VP and squad leads.",
          "The separate forty-hours continuation rationale for cb_06."
        ],
        "avoid_creating": [
          "Do not state that the participant knew the vendor tokens were non-compliant and consciously concealed it.",
          "Do not use a textbook term such as 'cognitive dissonance.'",
          "Do not add prior-hours or document-rework reasoning to this answer; those belong to sunk cost and status quo episodes."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_06",
      "bias": "Sunk Cost Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 4,
      "supporting_quote": "“We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy.”",
      "evidence_location": "Post-audit continue-versus-revert decision, followed by the explanation that reverting would write off the hours already spent.",
      "mechanism": "The participant explicitly uses nonrecoverable past customization effort as a reason to continue the current path despite new adverse evidence and an available legacy fallback with remediated contrast values. This is backward-looking continuation reasoning rather than an analysis of incremental future costs and compliance probabilities.",
      "strength": "strong",
      "confidence": 0.98,
      "plausible_nonbias_explanation": "Prior work can contain reusable value and may lower the future cost of completing customization. Here, however, the participant specifically frames reversion as unattractive because it would write off prior hours, without supplying a forward-looking comparison that shows continued customization is cheaper, safer, or more likely to meet compliance.",
      "additional_evidence_needed": "None.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 4, participant's decision to continue refinement after the audit.",
        "current_defect": "None. The explicit reference to writing off already-spent hours supplies a distinct backward-looking mechanism.",
        "minimal_change_instruction": "Retain the forty-plus-hours reference, the available legacy fallback, and the participant's stated reluctance to write off invested effort.",
        "preserve": [
          "The audit's disconfirming evidence.",
          "The legacy components' remediated contrast values.",
          "The separate audit-interpretation episode for cb_05."
        ],
        "avoid_creating": [
          "Do not substitute a purely forward-looking engineering estimate for the invested-hours rationale.",
          "Do not repeat the same invested-effort rationale at the final hybrid decision; that would merge cb_06 with cb_07."
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_07",
      "bias": "Status Quo Bias",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 5,
      "supporting_quote": "“We'd already built the governance docs, onboarding materials, and squad training around the current implementation, and switching structure again this close to the deadline felt like more disruption than it was worth.”",
      "evidence_location": "Final rollout-selection discussion, after the hybrid option is described as arguably the cleanest fix.",
      "mechanism": "The participant favors the presently implemented LumenKit-token arrangement over a hybrid alternative that is assessed as technically stronger and preserves much of the existing layout and motion work. Nevertheless, the stated reason is primarily concrete switching disruption near a real deadline, including potentially legitimate retraining and governance rework, rather than a clearly disproportionate preference for the current arrangement simply because it is the default or familiar.",
      "strength": "weak",
      "confidence": 0.69,
      "plausible_nonbias_explanation": "With three weeks remaining, changing documentation, training, governance, and implementation structure could create material operational and compliance risk. The current statement may therefore reflect justified change-management risk management rather than status quo bias.",
      "additional_evidence_needed": "A limited comparison showing that the participant did not assess the hybrid transition burden against the hybrid's compliance benefit, or that the current structure felt safer primarily because it was already the working default even after the hybrid's transition work was shown manageable.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_reasoning_revision",
        "location": "Decision point 5, participant's explanation for rejecting the hybrid arrangement.",
        "current_defect": "The episode can be read as a justified deadline-sensitive switching-cost judgment. It also risks partial contamination by sunk-cost reasoning because governance documents, materials, and training are prior investments rather than pure continuity cues.",
        "minimal_change_instruction": "Retain the current implementation and the three-week deadline, but add one concise cue that the participant treated the existing arrangement as the safer default because the teams already knew it, while not comparing the manageable hybrid-transition steps with the hybrid's direct resolution of the token problem. Do not make past effort, document creation, or training expenditure the reason for retention.",
        "preserve": [
          "The hybrid option's technical advantage.",
          "The fact that hybrid retains LumenKit layout and motion components.",
          "The three alternatives and their chronology.",
          "The forty-hour sunk-cost episode at decision point 4."
        ],
        "avoid_creating": [
          "Do not add a second reference to hours already spent, writing off work, or recovering training investment.",
          "Do not portray hybrid as technically infeasible; that would eliminate the required preference against a comparably or better assessed alternative.",
          "Do not introduce a new public-commitment rationale, which would merge this episode with cb_05."
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Priming effect",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Cognitive Dissonance",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    },
    {
      "bias": "Decoy effect",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Halo effect",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Illusion of control",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Sunk Cost Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Status Quo Bias",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Social proof / bandwagon effect",
      "decision_point": 1,
      "supporting_quote": "“LumenKit came up because a couple of competitors use it and it's picked up some industry recognition.”",
      "mechanism": "Competitor adoption and industry recognition are presented as favorable cues that may increase perceived legitimacy of the vendor.",
      "confidence": 0.42,
      "status": "weak",
      "plausible_nonbias_explanation": "Competitor adoption and awards are reasonable vendor-screening signals. The interview does not clearly show that the participant's adoption decision was caused by imitation of competitors rather than by the demo, deadline, and perceived quality.",
      "revision_recommendation": "remove_or_neutralize"
    },
    {
      "bias": "Confirmation bias / selective evidence weighting",
      "decision_point": 4,
      "supporting_quote": "“My instinct was that these were implementation-specific edge cases ... since the vendor's own documentation states AA compliance. I didn't request an independent re-test.”",
      "mechanism": "The participant gives immediate weight to evidence consistent with prior expectations and does not seek the diagnostic test that could distinguish local-theming effects from vendor-token defects.",
      "confidence": 0.63,
      "status": "candidate",
      "plausible_nonbias_explanation": "The vendor documentation is relevant evidence and the local-theming explanation is technically plausible. The transcript does not establish a broader selective search pattern beyond this one missed diagnostic step.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Planning fallacy",
      "decision_point": 3,
      "supporting_quote": "“I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally.”",
      "mechanism": "The four-week estimate may underestimate external coordination constraints and release-calendar risk.",
      "confidence": 0.34,
      "status": "rejected",
      "plausible_nonbias_explanation": "There is no evidence about comparable rollout durations, base rates, task decomposition, or systematic underestimation. The stronger supported mechanism is the participant's claimed control over external schedules, not a general planning fallacy.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "The initial compliance deadline and urgency to find outside tooling.",
      "location": "Opening role and goal discussion.",
      "why_not_bias": "A ten-week WCAG deadline is an objective organizational constraint. Urgency can motivate a reasonable search for external tooling and does not, by itself, establish distorted judgment."
    },
    {
      "cue": "The participant had not run independent contrast checks before the initial broad-pilot recommendation.",
      "location": "Decision point 1.",
      "why_not_bias": "Missing verification is not itself a bias. It becomes relevant here only because the participant explicitly inferred unverified token quality from unrelated positive product and reputation cues."
    },
    {
      "cue": "One squad had an unrelated release freeze that prevented the planned schedule.",
      "location": "Decision point 3 aftermath.",
      "why_not_bias": "The release freeze is an external operational fact, not evidence of bias. It supports the context showing why the participant's asserted control was unwarranted."
    },
    {
      "cue": "The accessibility audit found contrast failures in three of five tested components.",
      "location": "Decision point 4.",
      "why_not_bias": "An unfavorable audit outcome does not prove any bias. Bias evidence comes from how the participant interpreted the audit and chose whether to test, continue, revert, or pivot."
    },
    {
      "cue": "The participant considered that local theming might interact with vendor defaults.",
      "location": "Decision point 4.",
      "why_not_bias": "This is a technically plausible causal hypothesis. Without a demonstrated motive to protect the earlier public claim, it should not automatically be labeled cognitive dissonance."
    },
    {
      "cue": "Near-deadline disruption associated with moving to a hybrid implementation.",
      "location": "Decision point 5.",
      "why_not_bias": "Documentation, training, governance, and implementation changes can create real operational risk. The present text is insufficient to distinguish fully between rational switching-cost management and status quo bias."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "The accordion-led demo framing affected the participant's initial pilot-scope decision.",
        "evidence": "The participant says the overall quality bar felt high enough to justify a broad pilot, then reports that seeing token-level contrast data first might have led to a narrower pilot.",
        "assessment": "Moderately supported as a self-reported causal account. It identifies a plausible ordering mechanism but remains retrospective and hypothetical."
      },
      {
        "claim": "The Enterprise tier appeared preferable because the Team tier was comparatively unattractive.",
        "evidence": "The participant says Enterprise looked obviously better next to Team and acknowledges not evaluating it against actual needs or a custom-build alternative.",
        "assessment": "Supported as a proximal comparative-evaluation account. The evidence does not establish that the vendor deliberately designed Team as a decoy, which is not required for the participant-level mechanism."
      },
      {
        "claim": "Personal oversight would make a four-week rollout work despite squad schedules.",
        "evidence": "The participant says daily management would make it work regardless of existing release calendars; a squad subsequently reports a release freeze.",
        "assessment": "The participant's predictive control claim is directly documented and falsified by a relevant unverified dependency. The incident does not prove all close management was ineffective, but it demonstrates the limits of the claimed control."
      },
      {
        "claim": "The audit failures were implementation-specific rather than attributable to vendor tokens.",
        "evidence": "The participant hypothesizes theming-layer interaction but does not request an independent out-of-box token retest.",
        "assessment": "Unsupported as a causal conclusion. It remains an untested alternative hypothesis, and the interview appropriately records the missing diagnostic step."
      },
      {
        "claim": "Continuing LumenKit refinement was more efficient than reverting.",
        "evidence": "The stated basis is that reverting would write off more than forty hours already invested.",
        "assessment": "Weak causal and economic justification. Past hours are unrecoverable and do not establish that incremental continued work is more efficient than legacy reversion or a hybrid approach."
      },
      {
        "claim": "The current implementation was less disruptive than the hybrid option.",
        "evidence": "Governance documents, onboarding materials, and training had already been created around the present arrangement.",
        "assessment": "Plausible but incompletely evaluated. The transcript does not compare the actual remaining transition work, compliance risk, and time-to-remediation across the current and hybrid options."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "Competitor adoption and industry awards are treated as cues of vendor quality.",
        "why_it_matters": "These signals may correlate with product quality but do not establish WCAG compliance of the specific color and elevation tokens used in the participant's themed implementation."
      },
      {
        "risk": "Vendor documentation asserting AA compliance is treated as evidence against the internal audit.",
        "why_it_matters": "The documentation and audit may concern different configurations, but neither source alone resolves whether the vendor's out-of-box tokens or local theming caused the failures. An unthemed independent retest is the needed discriminating evidence."
      },
      {
        "risk": "Prior engineering effort is treated as evidence that continuation is the efficient option.",
        "why_it_matters": "Past expenditure is not evidence about future incremental cost, technical feasibility, or the probability of meeting the compliance deadline."
      }
    ],
    "counterfactual_present": true,
    "changed_variable": "Vendor demo framing order: the observed account has the flagship accordion component preceding token-level contrast data; the probe asks whether token-level numbers appearing first would have changed pilot scope.",
    "held_constant": [
      "Compliance deadline.",
      "Licensing tier structure and pricing.",
      "Squad dependencies and release calendars.",
      "Audit timing and audit findings.",
      "Hours invested in customization."
    ],
    "causal_coherence": "moderate",
    "explanation": "The presentation-order counterfactual is cleanly specified in the interview and is aligned with the hidden counterfactual variable. The participant gives a directionally coherent response—narrower pilot scope may have resulted—but qualifies it as 'possibly' and does not explain precisely how the earlier information would have changed the evaluation criteria. This is appropriate for a retrospective CTA probe but supports only moderate causal confidence. The interview does not accidentally alter the deadline, vendor, pricing tiers, audit timing, squad dependencies, or invested hours in the counterfactual."
  },
  "quality_scores": {
    "occupational_realism": 92,
    "cta_fidelity": 88,
    "bias_separability": 76,
    "bias_subtlety": 89,
    "control_fidelity": 100,
    "counterfactual_fidelity": 84,
    "narrative_coherence": 91,
    "naturalness": 87,
    "hidden_label_integrity": 100,
    "overall_quality": 84
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 5,
    "requested_occurrence_total": 7,
    "missing_occurrence_total": 2,
    "accidental_occurrence_total": 0,
    "priority": "medium",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Preserve the design-systems, WCAG-compliance, vendor-procurement, and two-squad implementation setting.",
      "Preserve the chronology, including the accordion-led demo, procurement deadline, unconfirmed squad calendars, week-seven audit, forty-plus customization hours, and final three-week deadline.",
      "Do not convert technically plausible uncertainty about themed versus out-of-box tokens into a plainly irrational or knowingly deceptive claim.",
      "Keep cb_05 distinct from cb_06 by locating cognitive-dissonance evidence in interpretation of contradictory evidence and sunk-cost evidence in the separate continue-versus-abandon rationale.",
      "Keep cb_07 distinct from cb_06 by avoiding references to recouping prior hours, documents, or training investment as the reason to retain the current arrangement.",
      "Do not add a new target-bias episode to compensate for the structural mismatch between the hidden four-decision-point plan and the five distinct decisions actually narrated.",
      "Preserve the counterfactual's single changed variable: demo presentation order."
    ],
    "revision_order": [
      {
        "priority": 1,
        "affected_instance_id": "cb_05",
        "action": "Add a minimal belief-consistency cue linking the participant's initial audit interpretation to the earlier public endorsement, while retaining the technically plausible theming hypothesis and absent independent retest."
      },
      {
        "priority": 2,
        "affected_instance_id": "cb_07",
        "action": "Make default-continuity or familiarity, rather than prior invested artifacts or objectively assessed switching cost, the independently observable basis for resisting the hybrid option."
      },
      {
        "priority": 3,
        "affected_structure": "Decision-point map",
        "action": "Update the generation metadata or future allocation rule to recognize separate licensing and timeline decisions. The current interview contains five distinct decision moments, although the hidden plan allocates them as four."
      }
    ]
  },
  "failure_flags": [
    {
      "flag": "decision_point_count_conflict",
      "severity": "moderate",
      "detail": "The hidden specification states that occurrences are spread across four decision points, but the interview contains five behaviorally distinct decision moments: broad pilot scope, licensing-tier selection, rollout-timeline setting, post-audit continuation, and final rollout-model selection. Licensing and timeline setting occur in adjacent interview sections but involve different alternatives, constraints, reasoning operations, and outcomes."
    },
    {
      "flag": "cognitive_dissonance_underidentified",
      "severity": "moderate",
      "detail": "The audit-discounting account is compatible with cognitive dissonance but also with a reasonable untested technical hypothesis. The transcript needs a minimal observable link between the prior public endorsement and selective weighting of the implementation-specific explanation."
    },
    {
      "flag": "status_quo_bias_confounded_by_switching_cost",
      "severity": "moderate",
      "detail": "The final decision contains a plausible continuity preference, but documentation, onboarding, training, and a three-week deadline are real change-management considerations. The text does not yet demonstrate that the current arrangement was preferred disproportionately because it was the default or familiar."
    }
  ]
}}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
