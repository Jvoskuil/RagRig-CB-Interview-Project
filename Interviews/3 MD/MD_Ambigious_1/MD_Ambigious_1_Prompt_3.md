You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for sitting down with me. This is a cognitive task analysis debrief — I want to understand how you reasoned through the District X attack tempo assessment, not evaluate whether the outcome was right. Nothing here affects your record, and you can skip anything. Sound okay?

Participant: Sure, that's fine.

Interviewer: Can you tell me your role and how this landed on your desk?

Participant: I'm the all-source analyst covering District X for the battalion S2. It came to me because SIGACTS showed a sharp jump in attacks and command wanted an assessment fast for the weekly INTSUM.

Interviewer: What was the objective as you understood it?

Participant: Figure out what was driving the numbers, recommend a response, and later judge whether that response actually worked, since the commander needed something concrete for a regional brief and for deciding where checkpoint resources should go next.

Interviewer: Walk me through the incident from the start.

Participant: For about a month, District X was steady — roughly three attacks a week, small-arms harassment, occasional IED. Then week five came in at eleven. That's the highest we'd seen in the whole dataset. Around the same time, HUMINT was reporting a local festival drawing big crowds, chatter about a resupplied weapons cache, and a tribal land dispute that had flared up. None of it was fully confirmed, but it was all sitting in the reporting at once. I had to give command something for that week's INTSUM.

Interviewer: What did you recommend?

Participant: I didn't want to jump straight to a cordon-and-search without solid targeting, so I pushed more ISR onto two suspected cache routes and stood up a limited checkpoint pilot in the busiest corridor. It felt like the right middle ground — do something, but don't commit the whole posture before knowing if week five was a real trend or a one-off.

Interviewer: What drove that choice over the alternatives?

Participant: Mostly the thin data. Eight weeks total isn't much to build a trend on, and I didn't want to overcommit resources off one bad week. But sitting on it wasn't an option either, with command already asking questions. The pilot let us act without locking in a bigger resourcing decision.

Interviewer: What happened after the pilot went in?

Participant: S3 liked it enough to expand it battalion-wide in week six — that became Operation Steady Watch. Week six came in at six, still elevated but down from eleven. Week seven dropped to three, week eight to four. Basically back near where we'd been before the spike.

Interviewer: Did anything else come in around that time?

Participant: Yeah. HUMINT caught up — the festival had ended by week six, the tribal dispute got mediated by local elders, and there were reports the resupplied cache had largely been used up in whatever drove the spike. So a few things were resolving in the same window as Steady Watch going in.

Interviewer: Your supervisor asked for a causal read for the command brief. What did you actually tell them?

Participant: Honestly, I told them I couldn't cleanly separate the two explanations. The timing fit Steady Watch — presence went up, attacks went down. But the timing also fit the festival ending and the dispute settling. Both stories explain the same numbers. With only eight weeks of data and all three of those things resolving in roughly the same stretch, I didn't think I had enough to say confidently which one was doing the work, or how much of each. I flagged the checkpoint effect as plausible but unconfirmed and recommended we keep watching before treating it as proven.

Interviewer: Was there pressure to just pick one explanation for the brief?

Participant: Some. Command likes a clean narrative, and "the checkpoints worked" is a better line than "we're not sure yet." But I've been burned before recommending something off two data points that didn't hold up, so I'd rather flag the uncertainty than overstate it.

Interviewer: That fed into a District Y question. Tell me about that.

Participant: Right, the commander wanted to know if we should roll Steady Watch out to District Y too. District Y had its own spike — hit nine in week four, eased to five or six after, no posture change over there. Given that I wasn't confident about what actually drove District X's drop, I didn't want to treat that result as a proven model. Plus the District Y handler flagged that their spike had a different, still-unresolved driver — not the same mix of factors we'd seen in District X.

Interviewer: So what did you recommend?

Participant: I recommended holding off on committing checkpoint materials and doing a short standalone look at District Y first, since its situation wasn't a clean match for what we'd just seen. S3 agreed to wait rather than provision resources immediately.

Interviewer: And the forecast for the commander's brief — what did you present?

Participant: With the brief three days out and only two weeks of data past the implementation, I gave a range rather than a single number. I told the commander the tempo could hold near three to four a week, but that we hadn't isolated what was actually driving the drop, and that four more weeks would tell us a lot more than two. He wasn't thrilled with the hedge, but he approved continued funding with a review point built in rather than an open-ended commitment.

Interviewer: If the tribal dispute hadn't been resolved that week, would your read have changed?

Participant: Probably would've made me more comfortable crediting Steady Watch, yeah — one less competing explanation sitting on top of the same data.

Interviewer: And if District Y's spike had also faded without any posture change there?

Participant: That would've made me want even more data before trusting the District X story, since it'd suggest spikes can settle on their own regardless of what we do.

Interviewer: Anything about how the data came together that week you'd want to see differently?

Participant: I'd want a longer baseline before the spike, and I'd want the local reporting on the festival, the cache, and the dispute nailed down earlier instead of confirmed after the fact. Getting that timing right sooner would have made it a lot easier to say what actually moved the numbers instead of leaving it open the way we did.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Failure to recognize regression to the mean",
        "occurrences": 0,
        "mechanism_constraint": "Must not be intentionally embedded; phase-2 reasoning must remain genuinely underdetermined between checkpoint effect and natural resolution of transient factors, without either dismissing the reversion-relevant evidence or naming/defining the bias."
      }
    ],
    "target_bias_names": [
      "Failure to recognize regression to the mean"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Failure to recognize regression to the mean",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MD_Biased_1",
    "counterfactual_variable": {
      "name": "Presence versus absence of resolvable transient confounding factors coincident with the week-5 attack spike",
      "original_state": "Transient factors (festival, cache depletion, tribal dispute mediation) present and naturally resolved by weeks 7-8, keeping the cause of the decline ambiguous",
      "changed_state": "No transient confounding factors; spike reflects sustained escalation with no independent reason to subside",
      "variables_to_hold_constant": [
        "Baseline attack rate weeks 1-4",
        "Timing of Steady Watch implementation",
        "Magnitude and timing of week-5 spike",
        "Analyst identity and reporting cadence",
        "Command pressure and INTSUM deadline"
      ]
    },
    "scenario_id": "MD_Ambigious_1",
    "domain_id": "MD",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; this is a zero-occurrence ambiguous control paired with MD_Biased_1. The single decision point that carries the bias mechanism in the paired scenario (phase 2, causal attribution of the weeks 7-8 decline) is deliberately rewritten here as an explicitly unresolved, dual-explanation judgment rather than a confident single-cause attribution, and this rewrite is not counted as a bias instance.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Setting, stakeholders, and operational constraints",
      "SIGACTS trajectory (baseline, week-5 spike, weeks 7-8 decline)",
      "Four decision-point structure and alternative sets",
      "District Y comparison and forecast-to-commander closing decision",
      "Interview length target and emotional tone"
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
