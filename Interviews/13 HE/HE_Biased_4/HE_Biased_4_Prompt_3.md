You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{**Interviewer:** Thanks for making time this week. Just to confirm, this is a voluntary conversation about your recent work verifying the fire engineering package on the tower project—I'll be asking about a specific sequence of decisions, and there's no need to reference anything confidential like commercial terms. That work for you?

**Participant:** Sure, that's fine. I led the performance-based design verification on the 42-story mixed-use tower—office floors, residential above, and an assembly space at podium level. My job was to close out the fire strategy sign-off before the developer's occupancy certificate deadline.

**Interviewer:** Can you give me a general account of what happened in that final stretch?

**Participant:** It was a compressed week. We had four things converging: a late glazing substitution from the contractor, a smoke-control model that came back borderline, a punch list that wasn't fully closed, and a final egress run we needed clean before submission. Normally these would be spaced out, but the contract had liquidated damages tied to the occupancy date, so everything landed at once. The contractor proposed swapping the specified glazing for a cheaper product from another supplier—call them Vendor B—because the original product had a lead-time problem. Around the same time, our CFD smoke model for the atrium showed a visibility result at the escape stair door that was right at the edge of the tenability threshold. Then, with about two inspection days left, our QA reviewer flagged some open punch-list items across cladding fire-stopping, stair pressurization, and signage. And finally, we had to finalize the egress modeling parameters before submitting to building control.

**Interviewer:** Let's reconstruct that in order. What came first?

**Participant:** The glazing issue surfaced first, maybe ten days out. Vendor B sent their technical bulletin, and their rep followed up by email restating the same fire resistance figure, and then I found the same number again in their product brochure. The CFD result came in a few days later, right when we were prepping for fan commissioning. The punch-list conversation happened after that, once the QA reviewer did a walk-through. The egress modeling was the last piece, done in the final two days before submission.

**Interviewer:** Let's take the glazing decision first. What did you have in front of you?

**Participant:** The original spec had a UL-tested 90-minute integrity rating, properly documented. Vendor B's material said their product also achieved "90 minutes, independently verified." I saw that phrase in their bulletin, then again in the cover email, then again in their brochure.

**Interviewer:** What made you comfortable with that?

**Participant:** Honestly, seeing it stated the same way three times across three different documents gave me a level of confidence I probably wouldn't have had from just one. It felt corroborated—like it wasn't just marketing spin, because the same number kept showing up consistently.

**Interviewer:** Did you look at whether those three statements were drawing on the same underlying test?

**Participant:** Not at that stage, no. It didn't occur to me to check whether the bulletin, the email, and the brochure were all citing the same lab report versus separate testing. Building control asked for the raw report later, and that's when we found the mounting configuration in the original test didn't match our as-installed detail, which meant we needed a compatibility assessment. At the time, though, I provisionally accepted the substitution on the basis that it was consistently documented.

**Interviewer:** Moving to the CFD result—what were the options there?

**Participant:** The model showed visibility at the stair door getting close to the threshold around the six-minute mark. Our QA reviewer recommended re-running it with a revised HVAC shutdown sequence, which would've added about five working days. We had four days to the deadline. Fan commissioning was next on the critical path.

**Interviewer:** What did you decide, and why?

**Participant:** I authorized the commissioning to proceed. We were losing days, and holding the whole phase for a re-run felt like it would stall the entire program right when we needed to keep moving. I treated the re-run as something that could happen in parallel rather than as a gate before the next milestone.

**Interviewer:** Was there a technical basis for treating it as non-blocking, or was it mainly about the schedule?

**Participant:** If I'm honest, it was mostly about not wanting the project to stand still. The commissioning itself wasn't destructive, so proceeding felt like the safer, more productive choice compared to just waiting around for numbers we already suspected might come back tight. The re-run did eventually show the margin was narrower under a slightly different shutdown assumption, but by then commissioning had already passed its initial functional tests.

**Interviewer:** Let's talk about the punch-list reprioritization. What was on the list at that point?

**Participant:** Cladding fire-stopping, a pressurization deficiency on one of the lift-shaft fan doors, and some egress signage items. Two inspection days left.

**Interviewer:** How did you decide where to spend those two days?

**Participant:** There'd been that apartment-tower fire overseas about two weeks earlier—cladding-related, and the footage was everywhere. It stuck with me. Even though our cladding and compartmentation system is different and already well-documented, I put the remaining time into re-inspecting the cladding fire-stopping.

**Interviewer:** What about the pressurization fan-door deficiency?

**Participant:** It got pushed down the list. It had already been logged, so it felt like something we understood and could revisit later. The cladding felt like the one I needed to be extra sure about after watching that. In hindsight, a follow-up visit found the fan-door issue was more significant than we'd initially logged, and the cladding re-inspection didn't turn up anything new.

**Interviewer:** Did you use the standard risk matrix to rank those items?

**Participant:** Not formally at that point. It was more of a judgment call based on what felt most urgent to check again.

**Interviewer:** Last decision point—the egress modeling parameters.

**Participant:** Right, this was in the final two days. The software's default library has pre-movement times and flow rates calibrated for generic office occupancy. Our building's mixed-use—office, residential, assembly—so the population isn't quite the same. A colleague flagged that we actually had project-specific pre-movement survey data, plus some comparable mixed-use studies, that could refine those numbers.

**Interviewer:** Did you use that data?

**Participant:** We didn't, in the end. Recalibrating with the survey data would've meant extra runs and QA time we didn't have. The defaults are the standard starting point in that software, so I kept them for the final compliance run. I flagged in my notes that the calibration population wasn't a perfect match, but the run passed the required threshold, so we submitted it as is.

**Interviewer:** If recalibrating had taken less effort, would you have used the survey data instead?

**Participant:** Probably, yes. It wasn't that I thought the defaults were more accurate—it was more that changing them under that timeline felt like an unnecessary complication.

**Interviewer:** Looking back across all four decisions, what would have changed your approach on the glazing, if anything?

**Participant:** If the 90-minute claim had come from one document instead of three, I think I'd have pushed harder for the raw report before accepting it. Something about seeing it repeated made it feel more settled than it actually was.

**Interviewer:** And if there'd been no deadline pressure at all that week?

**Participant:** The CFD re-run probably would've been a hard hold point rather than something running in parallel. Without the schedule squeeze, I don't think I'd have authorized commissioning ahead of it.

**Interviewer:** Last one—if that overseas fire hadn't been in the news right before your punch-list decision, do you think the priority would have looked different?

**Participant:** Possibly. I'd like to think I'd have gone with the risk matrix from the start. But I can't fully separate how much of that reallocation was the news versus genuine caution.

**Interviewer:** That's a helpful place to stop. Thanks for walking through it in this much detail.

**Participant:** No problem. It's useful to go back over it, honestly.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusion of Truth effect",
        "occurrences": 1,
        "mechanism_constraint": "Repetition of an identical unverified claim across multiple documents from a single underlying source, mistaken for independent corroboration."
      },
      {
        "bias": "Action bias",
        "occurrences": 1,
        "mechanism_constraint": "Preference for proceeding with an active step over pausing/waiting, justified primarily by the value of acting rather than by risk analysis."
      },
      {
        "bias": "Affect Bias",
        "occurrences": 1,
        "mechanism_constraint": "Risk prioritization driven by emotional reaction to a vivid, unrelated recent event rather than new technical evidence."
      },
      {
        "bias": "Default bias",
        "occurrences": 1,
        "mechanism_constraint": "Retention of pre-set software parameters over an available, more representative alternative, justified by effort/status-quo rather than technical superiority."
      }
    ],
    "target_bias_names": [
      "Illusion of Truth effect",
      "Action bias",
      "Affect Bias",
      "Default bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Illusion of Truth effect", "requested_occurrences": 1 },
      { "bias": "Action bias", "requested_occurrences": 1 },
      { "bias": "Affect Bias", "requested_occurrences": 1 },
      { "bias": "Default bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect" },
      { "instance_id": "he4_ab_01", "bias": "Action bias" },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias" },
      { "instance_id": "he4_db_01", "bias": "Default bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect", "decision_point": 1 },
      { "instance_id": "he4_ab_01", "bias": "Action bias", "decision_point": 2 },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias", "decision_point": 3 },
      { "instance_id": "he4_db_01", "bias": "Default bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "he4_iot_01",
        "bias": "Illusion of Truth effect",
        "mechanism": "Repeated exposure to the same claim across three vendor documents traced to one underlying test increases perceived credibility without independent verification.",
        "affected_reasoning_operation": "Evaluation of source credibility / evidence weighting",
        "evidence_source": "Vendor B's spec sheet, cover email, and marketing brochure, all citing the same '90-minute, independently verified' claim",
        "distinctiveness_requirement": "Must be tied to decision point 1's glazing substitution evaluation only; not restated in later decision points."
      },
      {
        "instance_id": "he4_ab_01",
        "bias": "Action bias",
        "mechanism": "Preference for authorizing an active commissioning step over waiting for a recommended re-run, justified by the value of maintaining momentum rather than analysis of the borderline CFD result.",
        "affected_reasoning_operation": "Action-versus-inaction choice under schedule pressure and uncertainty",
        "evidence_source": "Preliminary CFD visibility result and QA's re-run recommendation at decision point 2",
        "distinctiveness_requirement": "Must be tied to the fan-commissioning authorization only; not conflated with the cladding-reprioritization decision in point 3."
      },
      {
        "instance_id": "he4_afb_01",
        "bias": "Affect Bias",
        "mechanism": "Emotional salience of a vivid, unrelated recent high-rise fire shifts inspection-time allocation toward the emotionally resonant cladding system over the technically more urgent pressurization deficiency.",
        "affected_reasoning_operation": "Risk-based prioritization of remaining QA punch-list items",
        "evidence_source": "News coverage of the unrelated fire and the pre-existing pressurization fan-door deficiency log at decision point 3",
        "distinctiveness_requirement": "Must be tied to punch-list reallocation only; must not be justified by new technical cladding evidence."
      },
      {
        "instance_id": "he4_db_01",
        "bias": "Default bias",
        "mechanism": "Retention of software's generic-office default occupant parameters over available project-specific survey data, justified by effort/status-quo rather than technical fit.",
        "affected_reasoning_operation": "Selection of model input parameters for the final egress compliance run",
        "evidence_source": "Software default library and colleague's flagged project-specific survey/comparable-building data at decision point 4",
        "distinctiveness_requirement": "Must be tied to the final egress-modeling run only; must not reuse action-bias or illusion-of-truth reasoning."
      }
    ],
    "intended_strength": [
      { "instance_id": "he4_iot_01", "bias": "Illusion of Truth effect", "strength": "moderate" },
      { "instance_id": "he4_ab_01", "bias": "Action bias", "strength": "moderate" },
      { "instance_id": "he4_afb_01", "bias": "Affect Bias", "strength": "moderate" },
      { "instance_id": "he4_db_01", "bias": "Default bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Biased_4",
    "domain_id": "HE",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism: illusion of truth at the documentary-evidence evaluation (point 1), action bias at the schedule-pressure go/no-go choice (point 2), affect bias at the risk-prioritization choice following a vivid external event (point 3), and default bias at the modeling-parameter selection (point 4). No bias shares a decision point, so no additional evidence-source separation was required.",
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
