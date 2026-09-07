You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Before we start, do I have your consent to talk through a past case, keeping identifying details out of it?

Participant: Yes, that's fine.

Interviewer: Can you describe your role and caseload at the time?

Participant: I was the IEP Coordinator for an elementary building, managing about 42 active IEPs. My job included coordinating interim placements for transfers, writing present levels, tracking related services, and making sure we stayed inside compliance timelines. This case was a mid-year transfer, so we had ten school days to get an interim placement in place.

Interviewer: What was the goal for this student specifically?

Participant: To get a legally sound interim IEP finished quickly, with a placement, present levels, and service minutes that actually reflected the student, not just a generic starting point. The tricky part was that our information came in pieces, and we had real scheduling limits on both testing and staff time.

Interviewer: Tell me what happened, from the transfer notice onward.

Participant: We got notice on a Thursday that the student would start Monday, coming from an out-of-district program that serves students with significant emotional and behavioral needs. The paperwork we had immediately was a transfer summary and a short IEP excerpt. That excerpt referenced a functional behavior assessment and behavior intervention plan written about a year and a half earlier for aggression. The full cumulative file hadn't arrived yet.

I met with the parent, the classroom teacher, and the principal early that first week. The parent said the student had done well recently and was looking forward to a normal schedule. The teacher was willing to include the student but wanted some structure in place before diving into a full schedule, partly because of the FBA/BIP reference and partly, I think, because any new student mid-year creates some uncertainty regardless of background. The principal wanted whatever we set up to be stable, not something we'd be rearranging every other week.

I reached out to the sending program for the rest of the file and contacted our school psychologist about testing, since the existing academic and cognitive testing was over two years old. The psychologist's soonest opening was about three weeks out, past our ten-day deadline. During the first week, the student did fine in most settings, with a paraprofessional supporting transitions. Then, toward the end of the first week, the paraprofessional reported one incident during the shift from recess to writing time. That report became part of what I had to work with when I sat down to write the present levels for the interim meeting, which we held near the end of the ten-day window.

Interviewer: What did you know going in, and what came later?

Participant: Going in, I had the transfer summary, the short IEP excerpt, and the FBA/BIP reference specific to this student. I didn't yet have the full behavioral history, attendance record, or recent progress notes. Later, when the complete file arrived, it showed the plan had been faded out and the student had gone about nine months without a documented incident before the transfer. That context came in after I'd already started shaping my initial thinking about the case.

Interviewer: Let's start with that first decision. Before the full file came in, what did you decide?

Participant: I recommended we build in a short observation window before locking in a fully open interim schedule. I didn't want to finalize a heavily inclusive schedule the very first week without seeing the student in our building first.

Interviewer: What led you there?

Participant: Mainly the student's own FBA/BIP reference. That's documentation specific to this student, not a general assumption. At the same time, that conversation with the teacher and principal also touched on the kind of program the student was coming from, so I can't fully separate how much of my caution was strictly about this student's file versus the general sense that transfers from more structured programs sometimes need an adjustment period. Both things were sitting in my head at the same time.

Interviewer: What alternatives did you weigh?

Participant: Either flag the case for a brief observation period, or move straight into a full-inclusion interim schedule and only add supports if problems came up. I went with the observation window because it felt like the safer starting point given what we knew, even though I recognize a different reading is that I'd have leaned that way for any transfer with that program history in the file, individual documentation or not.

Interviewer: What would have made you comfortable skipping that step?

Participant: If I'd had the full file up front showing the long incident-free stretch, I probably would have gone straight into a fuller schedule from day one.

Interviewer: Second decision point: the reevaluation question.

Participant: Right. The existing testing was old, but the psychologist had no opening inside our ten-day window. I decided to write the interim IEP from the existing data and set a specific check-in date a few weeks out to revisit accommodations once we had more classroom information.

Interviewer: Why that option over pushing for an expedited slot?

Participant: There genuinely wasn't a faster testing option available, so using current data with a scheduled follow-up seemed reasonable. I'll admit I'm not entirely sure whether I'd have pushed harder for an earlier slot if one had existed, or whether the follow-up date was just a comfortable way to move forward without more phone calls that week. Both explanations feel plausible to me looking back.

Interviewer: What happened with that plan?

Participant: The scheduled check-in caught a mismatch in the accommodations a few weeks later, which is part of why we'd built the follow-up in to begin with.

Interviewer: Third decision point, the present levels write-up. What did you have to work with?

Participant: The paraprofessional's report of one transition incident, two teacher check-ins describing good peer interactions, and reading work samples above grade level. I'd only briefly observed the classroom myself.

Interviewer: How did you write it?

Participant: I included the transition incident specifically in the context of transitions, and separately described the peer interactions and reading performance as strengths. I tried not to let the incident bleed into how I described the rest of the day.

Interviewer: Do you think the tone came out even-handed?

Participant: Mostly, yes. Though rereading it later, there might be a slightly more cautious note running through the whole thing than the data alone would demand. I honestly can't tell if that's from the incident specifically or just how I write present levels in general when there's any behavioral history in the file.

Interviewer: Final decision point, the placement and service minutes.

Participant: By the meeting, I had the fuller record, the check-in schedule, the present levels, and input from the parent and teacher. I proposed partial pull-out time for transition support and writing organization, with general education for the rest of the day. The parent preferred keeping the student with peers as much as possible, which fit with what the teacher could support.

Interviewer: How was that decision reached?

Participant: It came from weighing the record as a whole, not any single piece. The parent asked for a follow-up review in six weeks, which we agreed to.

Interviewer: If the psychologist had had an immediate opening, would the reassessment decision have gone differently?

Participant: Probably. I'd have likely requested it right away rather than leaning on the older data with a later check-in.

Interviewer: If the paraprofessional's report hadn't come in, would the present levels have read differently?

Participant: Maybe slightly less cautious in tone, though I think the transition supports would still have come up given the program history in the file.

Interviewer: And with a longer compliance timeline?

Participant: I'd have waited for the complete file and done more observation before drafting anything.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Group attribution error",
        "occurrences": 0,
        "mechanism_constraint": "Control implementation: zero intended instances; decision point 1 must remain genuinely ambiguous between individualized and group-based causal readings without resolving toward either."
      },
      {
        "bias": "Present Bias",
        "occurrences": 0,
        "mechanism_constraint": "Control implementation: zero intended instances; decision point 2 must include a dated follow-up mechanism that keeps the deferral defensible on legitimate grounds."
      },
      {
        "bias": "Horn Effect",
        "occurrences": 0,
        "mechanism_constraint": "Control implementation: zero intended instances; decision point 3 caution must be scoped to the transition context rather than generalized to unrelated attributes."
      }
    ],
    "target_bias_names": [
      "Group attribution error",
      "Present Bias",
      "Horn Effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Group attribution error", "requested_occurrences": 0 },
      { "bias": "Present Bias", "requested_occurrences": 0 },
      { "bias": "Horn Effect", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "EI_Biased_3",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Ambigious_3",
    "domain_id": "EI",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: ambiguous_control condition requires zero intended bias instances for all target biases inherited from the paired scenario's manifest; no decision-point allocation of bias instances was performed. Ambiguity was instead distributed across decision points 1-3 by design, each engineered to support at least two plausible causal readings without resolving toward a bias-consistent interpretation.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Stakeholder roster and roles",
      "Four-decision-point narrative structure and sequence",
      "Operational constraints (10-day timeline, caseload size, psychologist backlog)",
      "Target word count and difficulty level",
      "Emotional tone and time pressure"
    ],
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
