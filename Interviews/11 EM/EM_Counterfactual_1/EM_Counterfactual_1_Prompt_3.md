You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm — you're okay with us discussing this incident in detail for training-development purposes, and we can pause anytime?

Participant: Yes, that's fine. Happy to go through it.

Interviewer: Can you tell me your role and what you were supposed to be doing that day?

Participant: I'm a Training Officer with the county EM office. That day I was controlling a full-scale exercise — a shelter-in-place and evacuation drill at our EOC and one of our public shelters. My job was running injects and evaluating the shelter and liaison teams.

Interviewer: What actually happened?

Participant: About ninety minutes in, we got a scripted comms-disruption inject. Almost right after, a real weather alert came through — a fast-moving winter storm, faster than what we'd built the drill around. A couple of field reports came in that I couldn't immediately place as scripted or real. So I paused the exercise and checked actual weather data before doing anything else. That confirmed it — a real tower failure, and roads closing faster than forecast.

Interviewer: What led you to stop and verify rather than continue running the drill?

Participant: The timing didn't fit our script, and the reports didn't match the inject list. I've run enough of these to recognize when something's off-script, and I didn't want to keep feeding scenario content into what might already be real.

Interviewer: What happened next?

Participant: Shortly after, two liaison officers arrived for the scheduled shift handoff at the shelter. Neither had worked that specific site before. This time, though, I actually had a bit of breathing room — maybe twenty-five minutes before I needed to turn to the transportation side, since the bus situation hadn't come up yet. So I sat with them, gave them the rundown — told them to run the usual Zone C protocol, muster at the standard point, same as always — and then went to check on road conditions.

Interviewer: What happened after that handoff?

Participant: About forty minutes later, during a headcount, we found a group had been sent to the old west muster point — we'd relocated that about a year ago. Separately, a volunteer coordinator asked me directly what "Zone C protocol" even referred to. So the same kind of mix-up happened, even though I'd had more time with them than I usually get in situations like this.

Interviewer: Let's go through this step by step. First, the decision to pause the exercise — what did you actually have in front of you at that moment?

Participant: The scripted inject text, the live weather alert, and two ambiguous field reports. No confirmation yet of a real failure — that came after.

Interviewer: What alternatives did you weigh?

Participant: Keep running the drill and treat it as scripted, or stop and verify against real data. I verified. Worst case, I lose a few minutes of drill time; best case, I catch a real problem early.

Interviewer: Now the liaison handoff. You said you had more time than usual there. What did you know about these two officers going in?

Participant: I knew they were new to this shelter specifically. I didn't ask about their broader background — I assumed liaison officers generally pick up our zone conventions fast, since it's not unusual across our sites.

Interviewer: You had roughly twenty-five minutes and no immediate competing task. What did you do with that time?

Participant: Some of it went to double-checking the transportation numbers with the section chief, even though I didn't strictly need to yet. With the liaisons, I gave them the same rundown I always give — "usual Zone C protocol," "standard muster point." I didn't really stretch it out into something longer.

Interviewer: Given that you weren't rushed, what made you choose the short version anyway?

Participant: Honestly, it didn't occur to me that it needed to be longer. Those terms are just how I refer to things day to day — they don't register as shorthand to me, they register as the actual names. Having the extra time didn't change how I framed it, because I wasn't treating it as an abbreviated version of anything.

Interviewer: Did you check what they already knew before briefing them?

Participant: No. I could have asked directly — "have you worked this layout before, do you know where the current muster point is" — and I had time to do that. I just didn't think to.

Interviewer: What would have changed your approach there?

Participant: If either of them had flagged that they were unfamiliar, I'd have walked them through it properly. Neither volunteered that, and I didn't ask.

Interviewer: Let's move to the transportation decision. What was the situation?

Participant: Two buses, three sites requesting transport, and the section chief flagged fuel and driver-hour limits. One sector's roads were closing faster than the others per the county updates.

Interviewer: What options did you consider?

Participant: Split the buses evenly across all three, or prioritize the fastest-closing sector first. I prioritized that sector.

Interviewer: Why that option?

Participant: Splitting evenly felt fair on paper, but it risked stranding people at the site about to become unreachable. Prioritizing by closure risk meant a longer wait elsewhere, but nobody got cut off entirely.

Interviewer: How did that play out?

Participant: The prioritized site cleared in time. One other site had a longer wait — inconvenient, but they got transport once the first run finished, no injuries.

Interviewer: Last decision point — handing off to the Incident Commander. What was competing for your attention?

Participant: The IC arrived to take over the real incident, the exercise evaluators still expected a formal debrief, and parts of the shelter were still running on the arrangement from the earlier handoff.

Interviewer: What did you consider doing?

Participant: Run the debrief and real command informally in parallel, or fully suspend the exercise and do a proper handoff. I suspended it and gave the IC a written status briefing instead of just talking him through it.

Interviewer: Why written, given you had some time pressure again at that point?

Participant: Verbal is faster, but I've seen details get lost that way, especially with comms already degraded. Writing it down gave him something to check against rather than relying on what he remembered hearing.

Interviewer: Did the earlier muster-point mix-up influence that choice?

Participant: A bit, in hindsight. I think I was more deliberate about not leaving room for gaps after seeing what happened with the liaison briefing.

Interviewer: Given that you actually had time available during that briefing, what do you think would have changed if you'd used it differently — say, walking through the zone map from scratch?

Participant: Probably would have caught the muster point issue immediately. It wasn't that I didn't have the minutes for it. I just didn't reframe the conversation as something that needed more than the usual rundown.

Interviewer: If the storm had hit an hour later, would your resource decisions have changed?

Participant: The bus prioritization logic would hold regardless. It might have given me even more slack before the transportation piece, but based on what happened here, I'm not sure that alone would've changed how I briefed the liaisons.

Interviewer: What would you tell a less experienced officer in a similar spot?

Participant: Don't assume the title comes with the knowledge. It's tempting to think "liaison officer" means someone already knows your terms, but that depends entirely on which site they've actually worked. Time isn't always the reason things get skipped — sometimes you just don't think to check.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Curse of Knowledge",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Curse of Knowledge"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Curse of Knowledge",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "mechanism": "Expert briefer assumes newly rotated, less-informed liaison officers share the same tacit facility-specific knowledge and terminology, resulting in an under-explained shift-handoff briefing, persisting even when time pressure is removed as a confound.",
        "affected_reasoning_operation": "Content selection and calibration during a briefing when time is not a binding constraint",
        "evidence_source": "Training Officer's stated rationale for briefing content and use of available time, contrasted with liaison officers' subsequent confusion/misdirection",
        "distinctiveness_requirement": "Must be distinguishable from the base scenario's time-pressure-confounded instance by explicitly showing the same abbreviated briefing occurs even with ample uncommitted time, isolating the knowledge-assumption mechanism from a time-economization explanation."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": "EM_Biased_1",
    "counterfactual_variable": {
      "name": "Amount of time available for the shift-handoff briefing before the next competing task",
      "original_state": "Approximately ten minutes available, under acute time pressure from the pending transportation task",
      "changed_state": "Approximately twenty-five minutes available, with no immediate competing task",
      "variables_to_hold_constant": [
        "Storm timeline and severity",
        "Liaison officers' identity, role, and experience level",
        "Transportation resource constraints and phase 3 decision reasoning",
        "Phase 1 and phase 4 decisions and reasoning",
        "Shorthand terminology used and downstream misdirection consequence"
      ]
    },
    "scenario_id": "EM_Counterfactual_1",
    "domain_id": "EM",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence retained at decision point 2 (shift-handoff briefing), matching the base scenario's assignment, since the counterfactual condition requires implementing the identical manifest while varying exactly one causal factor (available briefing time) rather than the bias's decision-point placement.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Storm timeline and severity",
      "Liaison officers' identity, role, and experience level",
      "Transportation resource constraints and phase 3 decision reasoning",
      "Phase 1 and phase 4 decisions and reasoning",
      "Shorthand terminology used and downstream misdirection consequence"
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
