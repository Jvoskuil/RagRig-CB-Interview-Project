You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time this week of all weeks. Before we start, this is just for our internal process-improvement review — I'll ask you to walk me through a recent stretch of work, and there's no wrong answer. That okay?

Participant: Sure, happy to. Lock week is a good time to talk about it, honestly, everything's still fresh.

Interviewer: Great. Can you remind me of your role and what was on your plate?

Participant: I'm the CRC for our site on the Phase III trial — the oncology drug study. I handle adverse event triage, case report form cleanup, and screening new referrals. That week we were seven days out from the interim data lock for the DSMB, so basically everything converged at once.

Interviewer: Walk me through what that week looked like.

Participant: Monday morning I got a lab flag on Participant 12 — an ALT elevation, elevated but not dramatically so, and the timeline relative to dosing wasn't clean. Could've been drug-related, could've been something else entirely, maybe even diet or an OTC medication he didn't mention. I had to assign a causality category for the AE report. Same day, I was also mid-reconciliation on Participant 07's case report forms — that one had been a slog for almost two weeks, lots of inconsistent entries between the source charts and the CRF. Then Wednesday a new referral came in for screening, and Thursday there was a multi-site coordinator call about verification procedures ahead of lock. So four distinct things, all against the same deadline.

Interviewer: Let's start with Participant 12. What did you have in front of you?

Participant: His ALT was elevated, but in a range where you genuinely can't tell just from the number whether it's the study drug. Our protocol has three buckets — related, possibly related, unrelated — for exactly this kind of situation. I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.

Interviewer: How did that shape the classification?

Participant: I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed.

Interviewer: What about the "possibly related" option?

Participant: Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But "possibly related" kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.

Interviewer: What happened after?

Participant: The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after.

Interviewer: Let's move to Participant 07.

Participant: That one's been painful. I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records. Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that.

Interviewer: What did you do with that discrepancy?

Participant: I kept going. Twenty hours felt like too much to walk away from without one more push. And honestly the "losing a fifth of our population" framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it.

Interviewer: Did you consider flagging it as a deviation instead?

Participant: I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.

Interviewer: How did it turn out?

Participant: The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later.

Interviewer: Let's talk about the new referral on Wednesday.

Participant: He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has.

Interviewer: What did you do with that instinct?

Participant: I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he "probably" wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.

Interviewer: What happened when you did screen him?

Participant: He met every inclusion criterion. Clean screen, no issues. Which doesn't tell you much either way about whether deprioritizing him was the right call — I just got lucky that lock week didn't cost us his enrollment.

Interviewer: Last one — the coordinator call about verification.

Participant: Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever.

Interviewer: What made you switch?

Participant: Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.

Interviewer: Any pushback since?

Participant: The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond "everyone else was doing it too."

Interviewer: If you could go back, what single piece of information would have changed any of these calls?

Participant: For Participant 12, if I'd pulled his full history first instead of after, I might not have leaned so hard on that other case. For the verification switch, actual error-rate data would've mattered — I just didn't have it and didn't chase it down in time.

Interviewer: What if that Monday meeting about the other participant's enzyme case had never come up?

Participant: I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind.

Interviewer: And if the Site Director's email had framed Participant 07 differently — say, just asking whether continued reconciliation was worth the time?

Participant: I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have.

Interviewer: Last one — if none of the other sites had mentioned switching methods on that call?

Participant: I probably would've stuck with what we had. It's passed every audit. There wasn't really a problem to solve, other than speed.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Ambiguity Bias", "occurrences": 1, "mechanism_constraint": "avoidance of an intermediate/uncertain causality category in favor of a more definite classification" },
      { "bias": "Sunk Costs Bias", "occurrences": 1, "mechanism_constraint": "continuation justified by hours already invested rather than forward-looking resolvability" },
      { "bias": "Representativeness", "occurrences": 1, "mechanism_constraint": "eligibility likelihood judged by resemblance to typical enrolled profile rather than written criteria" },
      { "bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "adoption of a practice because most peer sites have already adopted it, absent independent validation" },
      { "bias": "Framing Effect", "occurrences": 1, "mechanism_constraint": "decision swayed by loss-framed vs. gain-framed description of an equivalent outcome" },
      { "bias": "Recency Bias", "occurrences": 1, "mechanism_constraint": "overweighting the most recently encountered comparison case relative to fuller case history" }
    ],
    "target_bias_names": [
      "Ambiguity Bias",
      "Sunk Costs Bias",
      "Representativeness",
      "Bandwagon effect",
      "Framing Effect",
      "Recency Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Ambiguity Bias", "requested_occurrences": 1 },
      { "bias": "Sunk Costs Bias", "requested_occurrences": 1 },
      { "bias": "Representativeness", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Framing Effect", "requested_occurrences": 1 },
      { "bias": "Recency Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "amb_01", "bias": "Ambiguity Bias" },
      { "instance_id": "sunk_01", "bias": "Sunk Costs Bias" },
      { "instance_id": "rep_01", "bias": "Representativeness" },
      { "instance_id": "band_01", "bias": "Bandwagon effect" },
      { "instance_id": "fram_01", "bias": "Framing Effect" },
      { "instance_id": "rec_01", "bias": "Recency Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "amb_01", "bias": "Ambiguity Bias", "decision_point": 1 },
      { "instance_id": "rec_01", "bias": "Recency Bias", "decision_point": 1 },
      { "instance_id": "sunk_01", "bias": "Sunk Costs Bias", "decision_point": 2 },
      { "instance_id": "fram_01", "bias": "Framing Effect", "decision_point": 2 },
      { "instance_id": "rep_01", "bias": "Representativeness", "decision_point": 3 },
      { "instance_id": "band_01", "bias": "Bandwagon effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "amb_01",
        "bias": "Ambiguity Bias",
        "mechanism": "Avoids the genuinely uncertain 'possibly related' causality category, resolving discomfort with ambiguity by choosing a more definite label not fully supported by the evidence.",
        "affected_reasoning_operation": "Causality classification under probabilistic uncertainty",
        "evidence_source": "Participant 12 lab/AE record and protocol classification categories",
        "distinctiveness_requirement": "Must center on avoidance of the ambiguous category itself, not on comparison to another case (that is rec_01's mechanism)."
      },
      {
        "instance_id": "rec_01",
        "bias": "Recency Bias",
        "mechanism": "Overweights a recently discussed comparison case relative to Participant 12's own fuller medication/lab history when forming the causality judgment.",
        "affected_reasoning_operation": "Recall/weighting of comparison evidence",
        "evidence_source": "Team meeting discussion of a different recent case",
        "distinctiveness_requirement": "Must center on comparative overweighting of a recent case, not on category avoidance (that is amb_01's mechanism)."
      },
      {
        "instance_id": "sunk_01",
        "bias": "Sunk Costs Bias",
        "mechanism": "Justifies continued investment in Participant 07's reconciliation by reference to hours already spent rather than forward-looking resolvability of the new discrepancy.",
        "affected_reasoning_operation": "Continue/discontinue resource allocation decision",
        "evidence_source": "Internal hours-logged tracking for Participant 07",
        "distinctiveness_requirement": "Must center on past-cost justification, not on the framing language used by the Site Director (that is fram_01's mechanism)."
      },
      {
        "instance_id": "fram_01",
        "bias": "Framing Effect",
        "mechanism": "Decision to continue is shaped by the Site Director's loss-framed description of the outcome, independent of the sunk-cost reasoning.",
        "affected_reasoning_operation": "Option evaluation under loss- vs gain-framed description",
        "evidence_source": "Site Director's email framing",
        "distinctiveness_requirement": "Must center on reaction to the specific loss-framed wording, not on the hours-invested justification (that is sunk_01's mechanism)."
      },
      {
        "instance_id": "rep_01",
        "bias": "Representativeness",
        "mechanism": "Judges eligibility likelihood by resemblance to the typical enrolled profile rather than by the protocol's actual written criteria.",
        "affected_reasoning_operation": "Prioritization/likelihood judgment against a category prototype",
        "evidence_source": "New referral's demographic/clinical appearance vs. protocol criteria",
        "distinctiveness_requirement": "Must center on profile resemblance reasoning, distinguishable from any capacity/queue-based justification."
      },
      {
        "instance_id": "band_01",
        "bias": "Bandwagon effect",
        "mechanism": "Adopts an unverified verification shortcut primarily because most peer sites have already adopted it.",
        "affected_reasoning_operation": "Process-adoption decision under peer/majority influence",
        "evidence_source": "Multi-site coordinator call disclosures",
        "distinctiveness_requirement": "Must center on majority-adoption as the stated driver, not on independent efficiency analysis."
      }
    ],
    "intended_strength": [
      { "instance_id": "amb_01", "bias": "Ambiguity Bias", "strength": "subtle" },
      { "instance_id": "sunk_01", "bias": "Sunk Costs Bias", "strength": "subtle" },
      { "instance_id": "rep_01", "bias": "Representativeness", "strength": "subtle" },
      { "instance_id": "band_01", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "fram_01", "bias": "Framing Effect", "strength": "subtle" },
      { "instance_id": "rec_01", "bias": "Recency Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE_FOR_BIASED_CONDITION (autoselected candidate: presence vs. absence of multi-site coordinator call disclosure before Decision Point 4)",
      "original_state": "Coordinator call occurs and discloses peer sites' switch to the shortcut method",
      "changed_state": "No coordinator call occurs; CRC evaluates the method change without peer-disclosure",
      "variables_to_hold_constant": [
        "Interim lock deadline",
        "Participant 07 data discrepancy details",
        "Participant 12 AE facts",
        "New referral profile and eligibility outcome"
      ]
    },
    "scenario_id": "HC_Biased_6",
    "domain_id": "HC",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences spread across 4 decision points with a maximum of 2 per point (DP1: Ambiguity Bias + Recency Bias via distinct evidence sources and reasoning operations; DP2: Sunk Costs Bias + Framing Effect via distinct evidence sources and reasoning operations; DP3: Representativeness alone; DP4: Bandwagon effect alone), chosen for mechanism fit and narrative realism per rules 1-4.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
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
