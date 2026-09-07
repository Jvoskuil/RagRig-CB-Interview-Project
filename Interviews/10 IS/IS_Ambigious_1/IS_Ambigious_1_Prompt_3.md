You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time. Before we start, do you consent to discussing this incident for the interview?

Participant: Yes, go ahead.

Interviewer: Could you describe your role and the situation we'll be talking through?

Participant: I'm a Product Manager on the onboarding team at CollabHub. We're a B2B collaboration platform, mostly self-serve signups with some sales-assisted accounts that go through the same flow. About five weeks before a board review, we saw a jump in abandonment at account setup, and I had to figure out what to do about it without blowing up the sprint plan or the roadmap we'd already committed to.

Interviewer: What first alerted you to it?

Participant: Our weekly funnel dashboard. Drop-off at account setup increased 32% over three weeks, which was unusual because upstream traffic and acquisition numbers hadn't shifted. At that stage the dashboard only broke things down at a fairly coarse level, so I could see something had changed but not exactly where in the flow people were leaving. The VP of Product wanted an explanation fast because activation rate is one of the numbers the board tracks closely. Sales was also getting questions in a couple of active deals about whether we had more guided setup options, since that had come up in demos. Engineering had a full sprint already, mostly enterprise bug fixes.

Interviewer: What was your objective at that point?

Participant: Immediate goal was to understand the cause well enough to act. Longer term, protect activation rate and have something credible to show the board, without pulling engineering off commitments that mattered to existing customers.

Interviewer: Walk me through what happened, roughly in order.

Participant: First few days were spent figuring out whether the dashboard number was even reliable, then narrowing down where in the funnel people were dropping. Once we had a clearer signal, I had to decide how to respond — that's the piece that took the most judgment. After that came a staffing call, since the response required engineering time we didn't really have spare. Then, closer to the board date, there was a launch decision under time pressure with incomplete testing.

Interviewer: Let's start with the first decision — how you investigated.

Participant: Right. I had the 32% increase, no user feedback yet, and a note from our analyst that payment-step instrumentation was incomplete. Options were: commission proper interviews, which research said would take two weeks to get sessions running; do a fast internal analytics and heatmap pass; or scan what competitors were doing for quick context. I went with the analytics pass plus a light competitor scan, and deferred interviews. Five weeks isn't much runway once you add design, build, QA, and release, so waiting two weeks just for interviews to start felt like too much of the budget gone before we even had a direction.

Interviewer: Any downside to skipping interviews at that stage?

Participant: Sure — analytics tells you where people drop, not always why. I flagged that trade-off to the team and kept research on standby in case the data stayed ambiguous.

Interviewer: What came out of that analysis?

Participant: The sharper signal was abandonment right after the payment-detail field, concentrated in a newer account subgroup — about 140 users. Small, and the cohort had only existed a month, so I wasn't fully confident it was stable. The heatmaps showed some repeated field edits around payment, but because instrumentation there was incomplete, I couldn't tell if that was a validation error or people just backing out.

Interviewer: That brings us to the second decision — choosing how to respond.

Participant: This was the harder one. I had two things in front of me. On one side, the payment-field signal, real but statistically thin. On the other, our Sales director told me two active enterprise deals had specifically asked, during demos, whether we had a more guided setup experience — not a general market comment, two named accounts with real revenue attached. Around the same time I'd noticed a few competitors had shipped something similar, but that wasn't really what drove the call for me.

Interviewer: What did drive it?

Participant: Honestly, it was close. The deal-specific requests gave me something concrete to point to — an actual account, an actual objection in a sales cycle — whereas the internal cohort data, while suggestive, was small enough that I didn't want to bet three sprints on it alone. I decided to build the guided setup wizard, partly because of those two deals, partly because I wasn't confident the payment-field fix alone would move the number given how thin the sample was. I'll be honest, if I look back at it, I'm not entirely sure I weighted that correctly — it's possible a more targeted fix would have addressed the real problem faster, or it's possible the deal risk was the right thing to prioritize. I don't think the data gave a clean answer either way.

Interviewer: Did you consider testing both directions before committing?

Participant: Our analyst suggested a small controlled comparison — one version fixing payment fields, another adding limited guidance — before committing engineering time. I didn't go that route because it would have delayed a decision the deals needed answered, and because I felt the payment data alone wasn't strong enough to anchor the whole response.

Interviewer: If those two deals hadn't come up, would you have decided differently?

Participant: Probably, yes. Without that pressure I think I'd have leaned toward the payment-field fix first and treated broader onboarding changes as a separate, later initiative.

Interviewer: Third decision — staffing.

Participant: Building the wizard meant pulling two engineers off the bug backlog for three sprints. That backlog had real enterprise-reported defects sitting in it. Sales wanted the wizard ready to reference in the two deals. I chose full reallocation rather than splitting time or delaying, because a split effort usually means both things ship late and half-tested, in my experience.

Interviewer: What followed?

Participant: Two of those backlog tickets escalated in severity while the engineers were reassigned. Not an outage, but real friction for those customers. Wizard build stayed on schedule. Follow-up analytics also showed the payment-field friction hadn't changed, which wasn't surprising since we hadn't touched that code.

Interviewer: Fourth decision — the launch itself.

Participant: Four days before the board meeting, QA had only done partial regression testing, the canary group was too small to read cleanly, and payment abandonment was unchanged. Options were full launch, a longer 10% canary, or a one-week delay for better testing and instrumentation. I chose full launch. A longer canary wouldn't have given us clean results in time, and delaying meant showing up to the board with a plan instead of something shipped. Engineering and QA weren't thrilled, but agreed the risk was manageable with monitoring and a rollback ready.

Interviewer: What were the results?

Participant: No statistically meaningful change in activation rate versus the prior month, and support tickets kept mentioning the payment step. Not a disaster, but not the fix either. We shifted focus afterward to a proper look at the payment validation and getting the instrumentation gap closed.

Interviewer: With two more weeks before the board review, what would you change?

Participant: I'd have run that controlled comparison the analyst proposed, and probably gotten a handful of user sessions from the affected cohort before committing three sprints anywhere.

Interviewer: What information would have made the second decision clearer at the time?

Participant: A larger, stable sample showing payment friction was the dominant cause, or direct evidence from users about why they stopped there. Either would have given me more to weigh against the deal pressure.

Interviewer: And if the payment-field data had come from a larger cohort?

Participant: I think it would have carried more weight against the deal requests. Hard to say for certain — it's the kind of call where reasonable people could have gone either way with what we actually had.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Herding",
        "occurrences": 0,
        "mechanism_constraint": "Must not be intentionally instantiated; decision point 2 must rely on individuated, named deal facts rather than aggregate adoption-prevalence framing."
      }
    ],
    "target_bias_names": [
      "Herding"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Herding",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IS_Biased_1",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IS_Ambigious_1",
    "domain_id": "IS",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; manifest requests zero occurrences of the paired target bias (Herding), so no allocation across decision points was performed. Decision point 2 was instead rewritten to preserve narrative ambiguity by substituting individuated deal-specific evidence for the aggregate adoption-prevalence framing used in the paired biased scenario, per the ambiguous_control condition rules.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain (Information Systems / HCI / interaction design)",
      "Role (Product Manager, Digital Platform)",
      "Scenario premise (CollabHub onboarding funnel drop-off before Q3 board review)",
      "Four decision points and their sequencing",
      "Actor set and stakeholder roles",
      "Technical vocabulary and difficulty level (moderate)",
      "Overall word count target and range",
      "Inconclusive consequence pattern at each decision point"
    ],
    "generation_warnings": [
      "Input specified counterfactual_variable as 'AUTOSELECT', but condition is 'ambiguous_control' (not 'counterfactual'), so no counterfactual variable was selected; counterfactual_specification and counterfactual_variable fields are set to null to avoid fabricating an unrequested experimental factor.",
      "Because this is a control paired against IS_Biased_1, decision point 2 was deliberately rewritten (deal-specific facts replacing aggregate adoption-prevalence framing) to preserve genuine ambiguity while matching structure; this substitution is a control-fidelity requirement, not an unintended bias instance."
    ]
  }}}

The hidden specification may include:
- condition;
- exact occurrence manifest;
- target bias names;
- requested occurrence count for each bias;
- planned instance IDs;
- intended decision points;
- intended mechanisms;
- intended strength;
- paired scenario ID;
- counterfactual variable.

Do not treat the hidden specification as evidence that a bias exists. It is a test plan only. The interview text is the evidence. If the specification and interview conflict, report the conflict.

CORE OCCURRENCE DEFINITIONS

A supported occurrence requires all of the following:
1. A distinct decision, inference, evidence-selection act, memory retrieval, prediction, causal attribution, or response to a probe.
2. Evidence showing how the participant processed, weighted, ignored, recalled, interpreted, or updated information.
3. A mechanism consistent with the named bias.
4. Enough context to distinguish the mechanism from a justified domain judgment or an ordinary mistake.

A single occurrence may span several adjacent sentences or one answer turn. Do not count repeated wording about the same reasoning episode as multiple occurrences. Count two occurrences separately only when they have distinct evidence traces, decision moments, evidence sources, or reasoning operations.

VALIDATION TASKS

1. Identify the domain, participant role, operational objective, and incident type.
2. Reconstruct the chronology and identify the decision points. Report whether exactly four decision points are present.
3. For every target bias in the hidden occurrence manifest, independently assess each requested occurrence.
4. Identify additional candidate biases not present in the target manifest.
5. Identify apparent bias cues that should not be labeled as bias.
6. Audit causal claims and counterfactual logic.
7. Evaluate interview quality and control fidelity.
8. Produce precise revision guidance when the interview does not satisfy its occurrence requirements.

FOR EACH REQUESTED OCCURRENCE, CLASSIFY IT AS ONE OF:

- supported: a distinct, textually supported instance is present;
- weak: a possible instance is present, but evidence or mechanism is insufficient;
- absent: no defensible instance is present;
- merged: the intended instance appears to be indistinguishable from another intended occurrence of the
  same bias or from another bias;
- accidental: an unintended instance appears outside the planned occurrence map;
- misclassified: the text supports a different bias or a non-bias explanation instead.

REVISION PRINCIPLES

If a requested occurrence is absent, weak, merged, or misclassified:
- Do not recommend simply repeating the bias label.
- Do not recommend adding an obvious textbook explanation.
- Specify the minimum local narrative or dialogue change needed to make that occurrence independently identifiable.
- Preserve the occupational setting, participant role, chronology, vocabulary, approximate length, and other intended bias occurrences.
- Do not create a new occurrence elsewhere merely to compensate.
- Do not strengthen every occurrence. Revise only the affected occurrence unless the evidence shows a broader structural problem.
- If strengthening the missing occurrence would make the interview too obvious, recommend a subtle evidence change rather than explicit labeling.
- If the requested occurrence is not plausible in the scenario, recommend changing the scenario or the target occurrence manifest rather than forcing implausible behavior.
- For controls, never recommend adding a target bias. If a control contains a defensible bias, recommend neutralizing or replacing the relevant reasoning episode.
- For a counterfactual, preserve the original and changed causal variables and do not introduce a second causal change while repairing bias evidence.

REVISION TYPES

Use one or more of these revision types:
- `none`: occurrence is adequately supported;
- `local_evidence_addition`: add or alter one cue, evidence source, or participant response;
- `local_reasoning_revision`: revise how the participant interprets or weighs evidence;
- `probe_revision`: change an interviewer question or hypothetical so the existing reasoning becomes independently observable;
- `decision_point_revision`: revise one decision point while preserving the rest;
- `remove_accidental_occurrence`: neutralize an unintended additional manifestation;
- `separate_merged_occurrences`: make two intended episodes distinct;
- `reclassify_bias`: change the target label or mechanism because the current label is not defensible;
- `scenario_revision`: revise the occupational situation because the requested occurrence is implausible.

REVISION SPECIFICITY

Each revision recommendation must include:
- the affected instance ID or `additional_candidate`;
- decision point and approximate turn or paragraph location;
- current status;
- evidence currently present, or `none`;
- precise defect;
- recommended revision type;
- minimal change instruction;
- what must remain unchanged;
- a warning against creating additional unintended occurrences;
- expected post-revision status.

Do not rewrite the complete interview. Provide revision instructions only. The generation system will apply
the instructions in a separate revision step.

OUTPUT

Return valid JSON only:
{
  "validator_version": "2.0",
  "interview_id": "...",
  "condition": "biased|vocabulary_control|ambiguous_control|counterfactual|unknown",
  "domain_assessment": {
    "domain": "...",
    "role": "...",
    "objective": "...",
    "incident_type": "...",
    "confidence": 0
  },
  "structure_audit": {
    "estimated_word_count": 0,
    "within_target_range": true,
    "decision_point_count": 0,
    "decision_points": [
      {
        "id": 1,
        "summary": "...",
        "evidence_before": [],
        "evidence_after": [],
        "goals_constraints": [],
        "alternatives": [],
        "decision_basis": "...",
        "time_pressure": "...",
        "uncertainty": "..."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "...",
      "bias": "...",
      "requested_occurrences_for_bias": 0,
      "status": "supported|weak|absent|merged|accidental|misclassified",
      "decision_point": 1,
      "supporting_quote": "...",
      "evidence_location": "...",
      "mechanism": "...",
      "strength": "absent|weak|moderate|strong",
      "confidence": 0,
      "plausible_nonbias_explanation": "...",
      "additional_evidence_needed": "...",
      "revision_needed": true,
      "revision": {
        "revision_type": "none|local_evidence_addition|local_reasoning_revision|probe_revision|decision_point_revision|remove_accidental_occurrence|separate_merged_occurrences|reclassify_bias|scenario_revision",
        "location": "...",
        "current_defect": "...",
        "minimal_change_instruction": "...",
        "preserve": [],
        "avoid_creating": [],
        "expected_post_revision_status": "supported|weak|absent|merged|accidental|misclassified"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "...",
      "requested_count": 0,
      "supported_count": 0,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "...",
      "decision_point": 1,
      "supporting_quote": "...",
      "mechanism": "...",
      "confidence": 0,
      "status": "candidate|supported|weak|rejected",
      "plausible_nonbias_explanation": "...",
      "revision_recommendation": "none|remove_or_neutralize|consider_adding_to_manifest"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "...",
      "location": "...",
      "why_not_bias": "..."
    }
  ],
  "causal_audit": {
    "causal_claims": [],
    "correlation_causation_risks": [],
    "counterfactual_present": false,
    "changed_variable": "...",
    "held_constant": [],
    "causal_coherence": "not_applicable|weak|moderate|strong",
    "explanation": "..."
  },
  "quality_scores": {
    "occupational_realism": 0,
    "cta_fidelity": 0,
    "bias_separability": 0,
    "bias_subtlety": 0,
    "control_fidelity": 0,
    "counterfactual_fidelity": 0,
    "narrative_coherence": 0,
    "naturalness": 0,
    "hidden_label_integrity": 0,
    "overall_quality": 0
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 0,
    "requested_occurrence_total": 0,
    "missing_occurrence_total": 0,
    "accidental_occurrence_total": 0,
    "priority": "none|low|medium|high|reject",
    "recommended_action": "accept|revise|regenerate|reject",
    "global_revision_constraints": [],
    "revision_order": []
  },
  "failure_flags": []
}

COUNTING RULES FOR THE SUMMARY
- `supported_occurrence_total` counts only occurrences with status `supported`.
- `missing_occurrence_total` counts `weak`, `absent`, `merged`, and `misclassified` requested occurrences.
- `accidental_occurrence_total` counts unintended instances that should be removed or separately labeled.
- Set `recommended_action` to `accept` only when all requested occurrences are supported, no unacceptable accidental occurrences exist, and quality is adequate.
- Set it to `revise` when local changes can repair the interview without changing the scenario.
- Set it to `regenerate` when the scenario, decision structure, or several occurrences are fundamentally unsuitable.
- Set it to `reject` for severe incoherence, contaminated controls, or unrepairable causal confounding.

Return JSON only. Do not return a revised interview.
