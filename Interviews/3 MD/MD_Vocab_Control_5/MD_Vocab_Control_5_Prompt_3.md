You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. This is for the after-action cognitive review, not attribution of blame—I just want to understand how the decisions actually got made. Okay with you?

Participant: Sure, no problem.

Interviewer: Can you start with your role and what the mission was?

Participant: I'm the battalion S3 for the task force. Our mission was to secure and hold the Route BLUE crossing so brigade could push their main effort across within a 48-hour window. We had one Mobile Gap-Crossing Bridge, limited float capacity, and a weather forecast that was going to close our aerial ISR window at some point in that 48 hours. It mattered because if we didn't hold that crossing on schedule, brigade's synchronization slid.

Interviewer: Walk me through how the incident unfolded, start to finish.

Participant: About 48 hours out, S2 flagged enemy scout vehicles in a spot that didn't match what we'd been seeing—three months of pattern-of-life had them screening consistently off ridge NAI 12, and this sighting was lower, closer to the river. I sat down with S2 and we talked through whether that was just noise in the pattern or something worth checking. Given the ISR window was closing, we didn't want to burn the whole asset chasing one sighting, but we also didn't want to write it off, so we split it: kept the reconnaissance-in-force plan moving, but got a partial retasking in on that location before the window shut. It came back inconclusive—some thermal returns but nothing that confirmed intent either way.

About six hours later, brigade S3 called and directed us to continue on Axis BLUE per the original order, citing the synchronization requirement. At that point our engineer had flagged a preliminary concern about the bridge's load capacity, no full classification yet. Rather than just noting it and moving on, I put it in writing to brigade and asked for an expedited classification survey to run in parallel with our movement, so we wouldn't have to choose between the timeline and the risk. Brigade agreed to that.

Closer to execution, the engineer came back with the actual classification: overweight risk for our heaviest platforms. We had a planning session. One of the company commanders raised a concern about how we were sequencing the heavy vehicles across, and that turned into a real discussion—reroute to the alternate ford, keep the plan as is, or resequence and stagger the loads. We landed on resequencing, and flagged the ford as a documented branch option since it hadn't been reconned in current water conditions.

On execution day we still had a bridge complication under one of the heavier platforms, and almost simultaneously took contact from dismounts near the crossing site. We executed the branch plan, secured the site, and finished the crossing over the alternate ford.

Interviewer: Let's rebuild that timeline with what you knew at each point, not what you know now.

Participant: At H-48 I had the sighting and the pattern, nothing confirmed. After the partial retasking, I had an inconclusive picture—better than nothing, still not definitive. At H-30 I had brigade's directive plus an unconfirmed engineer concern, and by the time we committed we also had brigade's agreement to run the classification in parallel. At H-24 I had a confirmed overweight number and an open discussion about sequencing. At H-hour I had the complication and the contact at the same time.

Interviewer: Take me back to the scout sighting. What made you decide to get ISR eyes on it instead of just treating it as expected?

Participant: The location didn't fit. Three months of consistent behavior is a strong baseline, but a scout element showing up closer to the crossing than the ridge is a meaningful enough deviation that I didn't want to assume it away. At the same time, one sighting against three months of pattern isn't automatically a new threat either, so full ISR diversion felt like overcorrecting. The partial retasking let us get some confirmation without giving up the window entirely.

Interviewer: What would have made you commit the whole ISR effort to it instead of a partial look?

Participant: A second independent report—ground or signals—pointing at the same location. One sighting alone, I wasn't going to reallocate the whole asset off brigade's main effort for it.

Interviewer: When brigade directed continuation on Axis BLUE, what alternatives did you weigh?

Participant: I could've just complied and left the bridge concern where it was, or asked for an outright delay, or done what we did—continue moving while pushing the concern up formally and asking for the survey to run in parallel. A flat delay request wasn't going to land well without more than an informal flag, and just dropping it risked committing heavy vehicles blind. The parallel-track option let us keep the timeline while still getting a real number before we had to cross.

Interviewer: Did brigade push back on that at all?

Participant: A little—there was some back-and-forth on how fast the survey could realistically run, but they agreed to it once I put it in writing with the engineer's rationale attached.

Interviewer: Let's go to the planning session with the classification report. How did that discussion go?

Participant: The engineer laid out the overweight risk, and the company commander who'd be sequencing the heavy platforms raised it immediately as a real problem, not just a note-and-move-on item. We went through the reroute option, the ford's unreconned water conditions, and a resequencing option that would stagger loads to stay under the classified threshold. Resequencing won out because it addressed the actual number without adding the ford's unknowns on top of a tight clock. We still wrote the ford up as a formal branch option in case the bridge situation changed.

Interviewer: Was there any disagreement about that choice?

Participant: Some. A couple of staff members wanted to at least get a quick recon of the ford in daylight before ruling it out as primary. We didn't have time to do that and still make the window, so we tabled it as a branch rather than dropping it outright.

Interviewer: Now the crossing itself—what would have changed your decision at the planning session, looking back at what you knew then?

Participant: Honestly, more time to actually recon the ford would have mattered. If we'd had it validated as a live option instead of theoretical, the sequencing-versus-reroute conversation might have gone differently.

Interviewer: How do you assess the scout sighting now, knowing what happened at the crossing?

Participant: It's consistent with the enemy orienting toward the crossing rather than the ridge, but I wouldn't say it made the contact obvious at the time. The partial ISR look didn't confirm intent, and the location alone isn't proof—it's one data point that lines up better in hindsight than it did in isolation.

Interviewer: Last one—if the alternate ford had been reconned earlier, do you think the session goes differently?

Participant: Probably, yes. With a validated ford sitting next to the bridge option, the reroute becomes a real contender instead of a branch we noted and moved past. As it was, resequencing was the option we could actually execute on time.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Authority Bias or Higher-level prioritization Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; S3's compliance with brigade must be accompanied by formal escalation and negotiated parallel risk mitigation, not source-weighted deference."
      },
      {
        "bias": "Hindsight Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; retrospective account must explicitly preserve the real-time uncertainty that existed before the outcome was known."
      },
      {
        "bias": "Representativeness Heuristic",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; the location deviation from the enemy template must be actively investigated rather than discounted by categorical resemblance."
      },
      {
        "bias": "Status Quo Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; retention or modification of the crossing plan must be justified by explicit comparison of risk-mitigation options, not by incumbency alone."
      },
      {
        "bias": "Groupthink",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; any staff disagreement about the bridge report must be voiced and discussed openly rather than suppressed or self-censored."
      }
    ],
    "target_bias_names": [
      "Authority Bias or Higher-level prioritization Bias",
      "Hindsight Bias",
      "Representativeness Heuristic",
      "Status Quo Bias",
      "Groupthink"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Authority Bias or Higher-level prioritization Bias", "requested_occurrences": 0 },
      { "bias": "Hindsight Bias", "requested_occurrences": 0 },
      { "bias": "Representativeness Heuristic", "requested_occurrences": 0 },
      { "bias": "Status Quo Bias", "requested_occurrences": 0 },
      { "bias": "Groupthink", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MD_Biased_5",
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Vocab_Control_5",
    "domain_id": "MD",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: vocabulary_control condition requires zero intended instances of all named biases. Decision points are matched one-to-one to the paired biased scenario's four phases (scout sighting, brigade directive, bridge-report planning session, after-action reflection) for structural and vocabulary parity, with each phase's reasoning rewritten to demonstrate balanced, evidence-weighed deliberation instead of the paired scenario's intended bias mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Operational objective (secure Route BLUE crossing within 48-hour brigade synchronization window)",
      "Setting, constraints, and equipment (single MGB, weather-limited ISR, unreconned alternate ford)",
      "Actors and roles (S3, S2, battalion engineer, brigade S3, company commanders)",
      "Four-decision-point chronology and phase content (scout sighting, brigade directive, bridge-classification session, after-action review)",
      "Domain vocabulary and technical terminology",
      "Interview format, difficulty, and emotional tone",
      "Approximate target word count (1,350 words, range 1,215-1,485)"
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
