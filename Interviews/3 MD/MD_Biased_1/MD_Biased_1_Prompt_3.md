You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the District X attack tempo assessment, not in grading the outcome. Nothing here goes in your file, and you can decline any question. That work for you?

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Great. Can you start by telling me your role and what pulled you into this particular assessment?

Participant: I'm the all-source analyst supporting the battalion S2 for District X. I own the SIGACTS tracking and the weekly INTSUM injects for that sector. It came onto my desk because we had a sharp jump in attack reporting and the S2 wanted an assessment fast, since command was already asking questions.

Interviewer: What was the overall objective you were working toward?

Participant: Figure out what was driving the attack numbers, recommend a response, and eventually judge whether that response worked — because the commander needed something concrete for a regional brief and for deciding where to put checkpoint resources next.

Interviewer: Walk me through the incident from the start.

Participant: Sure. For about a month, District X was running maybe three attacks a week — small-arms harassment, the occasional IED. Pretty steady. Then in week five we got eleven. That's not a small bump, that's the highest number in our whole dataset for that district. Around the same time, HUMINT was reporting a local festival that was drawing large crowds, some chatter about a resupplied weapons cache, and a tribal land dispute that had flared up. None of that was fully confirmed, but it was in the reporting. I had to decide what to recommend for that week's INTSUM with command already pushing for an answer.

Interviewer: What did you land on?

Participant: I recommended we not overreact with a full cordon-and-search — we didn't have solid targeting yet — but we did push more ISR onto two suspected cache routes and stood up a limited checkpoint pilot in the highest-traffic area. That felt like the right middle ground: do something, but don't commit to a big posture change before we knew if week five was a one-off or the start of a real trend.

Interviewer: What made you choose that over the other options?

Participant: Mainly time pressure and thin confirmation. We only had eight weeks of data total for that district, so I didn't want to overcorrect off one bad week. But I also couldn't just sit on it with command asking for something in the INTSUM. The pilot checkpoint let us act without betting the whole resourcing plan on one spike.

Interviewer: Okay — what happened after the pilot went in?

Participant: S3 liked it enough to expand it battalion-wide starting week six. That became Operation Steady Watch — full checkpoint posture across the district's main routes. Week six came in at six attacks, better than five but still elevated. Then week seven dropped to three, week eight to four. Basically back to where we'd been before the spike.

Interviewer: At that point, did anything else come in about what else might have changed?

Participant: Yeah, HUMINT caught up a bit. The festival had ended by week six. The tribal dispute got mediated by local elders around the same time. And there were reports the cache that got resupplied before week five had largely been expended in whatever activity drove that spike. So there were a few things resolving in parallel with Steady Watch going in.

Interviewer: Your supervisor then asked you for a causal read on that. What did you tell them?

Participant: I told them Steady Watch was working. The numbers backed it up — we went from eleven down to three and four within two weeks of putting checkpoints on the main routes. That's a big swing, and it lined up with when we increased presence. I flagged the other stuff — the festival ending, the dispute settling — but I treated those as secondary color, not the main driver. The posture change was the biggest, most visible thing we'd done, and the timing fit.

Interviewer: When you were weighing that, did you consider what the numbers might have done without Steady Watch at all?

Participant: Not in much depth, honestly. I noted the other factors existed, but I didn't really sit down and ask how much of that drop would've happened on its own just because week five was such an extreme outlier to begin with. The checkpoint explanation was the one command wanted and the one I had the clearest evidence trail for — increased presence, fewer incidents. It felt like a clean story.

Interviewer: That assessment then fed into a District Y decision. Tell me about that.

Participant: Right, the commander wanted to know if we should extend Steady Watch to District Y. District Y had its own spike — hit nine in week four — then eased down to five or six afterward, no posture change over there. Given what I'd just seen in District X, I recommended rolling Steady Watch out to District Y too, expecting a similar sharp drop.

Interviewer: Did you weigh the alternative of running a separate cause analysis for District Y first?

Participant: I considered it, but time was short and District X felt like a validated model at that point — we'd just seen checkpoints turn a spike around. The Y handler did mention their spike had a different, still-unresolved driver, which I noted, but I leaned on the District X result as the stronger signal for what to do next.

Interviewer: Last decision point — the forecast for the commander's brief.

Participant: With the brief three days out and only two weeks of post-implementation data, I presented a forecast of continued low attack tempo, three to four a week, framed as Steady Watch holding. I could have given a wider range and flagged that two weeks isn't much of a track record, but the trend line looked clean and the commander wanted something decisive for the brief, not a hedge.

Interviewer: If the tribal dispute hadn't been resolved that week, would your Steady Watch conclusion have looked different to you?

Participant: Probably, yeah. If that dispute had still been active and attacks still dropped, I'd have been much more confident it was the checkpoints. With it resolved right alongside our posture change, I probably should have leaned harder into how much of that drop those other threads accounted for on their own.

Interviewer: And if District Y's spike had also faded without any posture change at all?

Participant: That would've made me second-guess the District X read pretty quickly — it'd suggest spikes like that just settle down on their own sometimes, checkpoints or not.

Interviewer: Anything about the week-five spike itself you'd weigh differently now?

Participant: Maybe how extreme it was compared to everything before it. Eleven against a baseline of three is a huge jump, and huge jumps like that don't usually stay huge. I focused on what we did in response rather than on how unusual that single week was to begin with.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Failure to recognize regression to the mean",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Failure to recognize regression to the mean"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Failure to recognize regression to the mean",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "mechanism": "Attributing the full magnitude of a post-outlier decline to a deliberate intervention (Steady Watch) while disregarding the statistical likelihood that an extreme deviation (week-5 spike) would revert toward the established baseline independent of that intervention.",
        "affected_reasoning_operation": "Causal attribution of trend change following an extreme data point",
        "evidence_source": "SIGACTS weekly attack counts (weeks 1-8) combined with HUMINT reporting on resolution of transient local factors coincident with the spike",
        "distinctiveness_requirement": "This is the only planned instance; no other decision point may independently manifest the same evidence-processing failure (ignoring outlier-driven reversion) with new evidence sources or moments."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence versus absence of resolvable transient confounding factors coincident with the week-5 attack spike",
      "original_state": "Transient factors (festival, cache depletion, tribal dispute mediation) present and naturally resolved by weeks 7-8",
      "changed_state": "No transient confounding factors; spike reflects sustained capability escalation with no natural reason to revert",
      "variables_to_hold_constant": [
        "Baseline attack rate weeks 1-4",
        "Timing of Steady Watch implementation",
        "Magnitude and timing of week-5 spike",
        "Analyst identity and reporting cadence",
        "Command pressure and INTSUM deadline"
      ]
    },
    "scenario_id": "MD_Biased_1",
    "domain_id": "MD",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the clearest mechanism fit: the causal-attribution judgment made immediately after an extreme SIGACTS outlier reverts toward baseline, where transient confounders provide a documentable alternative explanation the analyst can be shown to underweight. Decision points 1, 3, and 4 were deliberately kept free of independent regression-to-the-mean evidence-processing acts to avoid double-counting the single requested instance.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Baseline attack rate weeks 1-4",
      "Timing of Steady Watch implementation",
      "Magnitude and timing of week-5 spike",
      "Analyst identity and reporting cadence",
      "Command pressure and INTSUM deadline"
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
