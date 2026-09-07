You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operational learning file, not a disciplinary review — you can decline any question. Can you state your role and how long you've been in it?

Participant: Sure. I'm shift captain on nights, been supervising underground crews about nine years, this site for four. Before that I was a ground control tech, so I came up through that side.

Interviewer: Good. Let's start broad — walk me through what you knew at the start of the shift, before anything unusual happened.

Participant: Standard handover. Day shift left a note that there'd been a small seismic event overnight near Panel 3, magnitude around 1.1, logged as minor, within normal range for that ground. They also flagged some wet ground near the access drift — more seepage than usual, nothing alarming on its own. Production schedule had us blasting Panel 3 within the first couple hours, and mucking and haulage after that. That was the plan.

Interviewer: What was the main objective for the night?

Participant: Keep Panel 3 on schedule. We were behind for the week, so there was some pressure from the surface to not lose another shift. Safety first, obviously, but the blast cycle was already tight.

Interviewer: Take me through the incident itself, in order.

Participant: Okay. First couple hours were the blast — I authorized it after the ground control tech did a visual pass, no visible loose rock, so we went ahead as scheduled. Didn't call for an instrumented convergence check, just a visual scaling look, because the seismic event had been small and logged as normal range. Blast went fine, mucking started.

A while after that, microseismic monitoring started showing a cluster of small events near the panel next to our old mined-out area — not bigger events, just more of them, more frequent. Haul trucks run a road that passes under part of that adjacent panel, so I had to decide whether to keep hauling that route. Ventilation was reading normal across the circuit, no gas issues reported, so I let haulage continue as-is.

About fifteen minutes after trucks started moving again, a methane sensor near that haul intersection logged a brief spike, then went back to baseline. Ventilation officer logged it as transient, no recurrence, didn't think much of it at the time — that kind of blip happens.

Then we got the fall of ground. Small one, near the haul intersection, damaged a section of mesh, no injuries, but it needed re-support before we could keep running trucks through there.

Interviewer: When that happened, what did you think was going on?

Participant: Honestly, by that point it felt pretty clear. You had the seismic event overnight, the wet ground, then the seismic cluster building up near the old workings, plus the blast vibration from our own cycle — it all lined up. Stress transfer off the old mined-out panel, aggravated by the water getting into the joints and then our blast adding vibration on top. Once you saw it laid out like that, it made sense — it was almost the story you'd expect given that ground history.

Interviewer: And the methane spike from earlier?

Participant: That I set aside. It didn't fit with a ground stability event — different system, different sensor, and it hadn't recurred. Ventilation had already called it transient. I didn't loop back on it specifically once we had a ground explanation that accounted for everything else.

Interviewer: Let's go back through each decision point one at a time. Starting with the blast authorization — what alternatives did you weigh?

Participant: Three options really. Go ahead with just the visual check, delay and call for an instrumented geotech inspection, or go ahead but scale back charge size and add scaling time as a buffer. I went with the first. The seismic event was classified minor, the tech didn't see loose rock, and we were already behind schedule.

Interviewer: What cues mattered most there?

Participant: The classification on the seismic log, mostly. "Minor, within normal range" carries weight — that's the geotech team's own threshold, not something I'm second-guessing casually.

Interviewer: Any uncertainty at that point?

Participant: Some. The wet ground note nagged at me a little, but on its own it's common enough that shift.

Interviewer: Second decision — continuing haulage under the adjacent panel despite the seismic cluster.

Participant: I considered rerouting the trucks, or halting until the geotech engineer looked at the cluster. But it was frequency increasing, not magnitude — that pattern is something I've seen before near old workings settling out. Ventilation was clean. Given the schedule pressure, I let it continue.

Interviewer: Whose input did you lean on there, and whose didn't you seek?

Participant: Leaned on the ventilation officer's readings. Didn't call the on-call geotech engineer — he's not on-site overnight, and I judged the cluster wasn't urgent enough to wake him for.

Interviewer: Third — the fall of ground and the remediation decision. What alternatives existed?

Participant: I could've treated the cause as undetermined and ordered an instrumented investigation of both the ground and the gas anomaly before deciding on re-support. Or gotten the geotech engineer's real-time input before committing to any explanation. Instead I went with the stress-transfer account and had the crew re-support directly on that basis.

Interviewer: What made that explanation feel solid enough to act on without waiting for engineering input?

Participant: It tied together everything we'd seen that night in one line — the timing worked, the location worked, the mechanism was one I understood from my ground control days. When it clicks together that cleanly, you don't feel like you're guessing anymore.

Interviewer: Did anything not fit that account?

Participant: The methane spike, technically. But it was a single blip, different monitoring system, already logged as transient. It didn't feel like it belonged in the same picture as a ground support issue.

Interviewer: Fourth decision — resuming production after re-support.

Participant: Re-support was done, no new seismic or gas readings since the FOG, and we were losing more schedule the longer we sat. I could've resumed limited production with continued monitoring, or suspended the panel until formal sign-off. I resumed full production. The explanation held together and the repair was solid, so I didn't see a reason to hold back further.

Interviewer: How confident were you in the cause at that point, on reflection?

Participant: Pretty confident in the moment. Looking back, I'll admit the geotech engineer wanted the raw seismic and gas data before he'd sign off on it as the definitive cause — he mentioned it could also be a localized joint failure or even sensor drift, unrelated to the stress-transfer idea entirely.

Interviewer: What information, if you'd had it earlier, might have changed your read?

Participant: Probably the engineer's data review itself, before we committed to re-support. If that had flagged the methane sensor as a calibration issue right away, or ruled out joint failure, I'd have felt more sure. Without it, I was working off what fit together in front of me.

Interviewer: If the methane spike had recurred a second time that night, would that have changed anything?

Participant: Yeah, I think so. A repeat would've been harder to wave off as unrelated. One blip is easy to set aside; two starts looking like its own problem.

Interviewer: Looking back, what part of your explanation are you least sure about now?

Participant: Whether the stress transfer story was really the whole cause, or just the part that was easiest to see. The pieces fit together well enough that I didn't push hard on what didn't fit.

Interviewer: What would you tell a newer supervisor facing a similar sequence?

Participant: That a clean-sounding explanation isn't the same as a confirmed one — get the data checked even when the story already feels complete.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Narrative Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a post-hoc fluent causal chain linking prior disparate signals into one coherent, high-confidence explanation at decision point 3, with the discordant methane reading dismissed rather than investigated."
      }
    ],
    "target_bias_names": ["Narrative Fallacy"],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Narrative Fallacy",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Post-hoc construction of a single coherent causal chain (seismic event + wet ground + adjacent seismic cluster + blast vibration) explaining the FOG, expressed with unwarranted confidence and completeness, while the discordant methane spike is excluded from the story without genuine investigation.",
        "affected_reasoning_operation": "Retrospective causal attribution / explanation construction",
        "evidence_source": "Cross-phase synthesis of seismic log, ground condition note, microseismic cluster data, blast schedule, and the phase-2 methane sensor spike",
        "distinctiveness_requirement": "Only instance of this bias in the interview; must not be duplicated via restated examples, the phase 4 resumption decision, or the closing hypotheticals — those turns may reference the same explanation but must not introduce a new independently identifiable manifestation."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "changed_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_1",
    "domain_id": "MU",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point (phase 3) offering the strongest mechanism fit and narrative realism — the moment a multi-signal incident (FOG) demands causal explanation under time and production pressure, immediately after a discordant data point (methane spike) has been introduced in phase 2 but left unresolved.",
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
