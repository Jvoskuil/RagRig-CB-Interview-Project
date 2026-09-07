You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. This is being recorded for a training-review case study, your name won't be attached to the write-up, and you can skip anything you'd rather not answer. That work for you?

Participant: Yeah, that's fine. I've sat through a few of these for the sergeant's after-action reviews before.

Interviewer: Good. What's your role, and how long have you been doing patrol work?

Participant: Patrol officer, field response, seven years now. Nights mostly the last three.

Interviewer: Let's start with the incident. Walk me through it from the top.

Participant: Sure. About 2:05 in the morning, dispatch got an anonymous call about a vehicle idling suspiciously near the loading dock at the distribution warehouse off Route 12. Caller didn't give a vehicle description, nothing about occupants, no specifics at all. That area's had a run of cargo theft the last couple months, so it's a place we keep an eye on anyway. I was closest unit, backup was a few minutes out. I rolled up, parked back a bit instead of pulling right up on the dock, and watched for a minute. Saw one guy standing next to a parked pickup truck near the dock, looking at a clipboard. Nothing dramatic—no forced entry, no tools out, nothing urgent-looking.

Interviewer: What made you hold back and observe instead of approaching right away?

Participant: Habit, really. If somebody's actually up to something, walking straight up tips them off before you get a read on them. He wasn't doing anything that needed immediate action, so there wasn't a reason to rush it.

Interviewer: Okay, so you approach. What happens next?

Participant: I get out, identify myself, ask what he's doing there. He's calm, looks right at me, answers straight away—says he's a contracted HVAC tech waiting on the site manager to let him in for a scheduled after-hours repair. Shows me a contractor badge clipped to his jacket, hands over his license without me asking twice. While we're talking I notice a bulge in his coat pocket, kind of squared off, hard to tell what it is.

Interviewer: What did you do with that?

Participant: I asked him to keep his hands visible while I thought it through. He's calm, cooperative, story's consistent, paperwork on the clipboard lines up with an HVAC job—that all counts for something. But I still don't know what's in that pocket, and an unidentified object at two in the morning, alone, isn't something I can just wave off because the guy seems relaxed. So I weighed it as: the demeanor and the story lower the odds it's a problem, but they don't rule it out, and the bulge is still an open question either way. Ended up doing a brief pat-down, but I told him why—said something like, "you seem fine, but I've got to check this."

Interviewer: Let's build the full timeline before we go decision by decision. What happened after the pat-down?

Participant: Clean. Bulge was a folded work order and a multimeter. No weapon. His story still wasn't independently confirmed though, and backup hadn't shown up yet, so I had him stay put while dispatch checked whether the HVAC company actually had a work order with that warehouse for that night. Came back a few minutes later—yes, active account, scheduled after-hours repair, all legitimate. Site manager showed up right around then to let him in. I released him, wrote up the field contact, noted the pat-down and why, and that was it.

Interviewer: Let's go through it decision by decision. First: choosing to observe before approaching. What alternatives did you weigh?

Participant: I could've walked right up, or called dispatch back for more detail first. Calling back didn't seem worth it—the caller hadn't given much to work with anyway. Watching first gets me information without giving up the advantage of him not knowing I'm there yet.

Interviewer: Second—the pat-down decision. How did the calm demeanor and the pocket bulge actually factor together into that call?

Participant: Pretty directly, honestly. The demeanor mattered—if he'd been jumpy or wouldn't look at me, I'd have treated the bulge as a lot more urgent and probably backed off to wait for backup before getting that close. Since he was calm and the story checked out on its face, that brought my concern down some. But it didn't erase it, because none of that tells me what's actually in his pocket. So both things were in the mix—the calm cuts one way, the unidentified object cuts the other, and I made the call knowing neither one fully resolved the other.

Interviewer: Did the subject's explanation change how you saw the bulge?

Participant: Some. Once he mentioned the work order and the multimeter before I even patted him down, I had a guess what it probably was. But "probably" isn't the same as confirmed, so I still checked.

Interviewer: If he'd been visibly nervous instead of calm, would that have changed things?

Participant: Yeah, I'd have been quicker to create distance and wait on backup rather than getting in close for a pat-down solo. Nervousness plus an unknown object is a different risk picture than calm plus an unknown object.

Interviewer: And if there'd been no bulge at all, same calm demeanor, same story?

Participant: Then there's nothing physical to check. It'd just be a field interview, verify the story, and let him go once it holds up.

Interviewer: Third decision point—after the pat-down's clean, you keep him at the scene instead of releasing him right away. Why?

Participant: The story wasn't verified yet. Badge and ID looked legit, but I've seen contractor badges that were expired or from a job somebody didn't actually have anymore. Backup still hadn't arrived. Holding him a few extra minutes for dispatch to confirm the work order felt like the reasonable middle ground—not cutting him loose on an unconfirmed story, but not treating him like a suspect either.

Interviewer: Did you consider escorting him to the site office instead?

Participant: Thought about it, but the office was locked, nobody there to answer. Waiting on dispatch and the site manager made more sense than walking him around the property in the dark.

Interviewer: Fourth—closing it out. Why release with no citation instead of a trespassing warning?

Participant: Once dispatch confirmed the work order and the site manager showed up right after, there wasn't a factual basis left for a citation. He had a legitimate reason to be there, and it held up. Writing him up at that point would've just been penalizing him for being at his own job site.

Interviewer: What single piece of information, if it had come in earlier, would have changed how you handled this?

Participant: Honestly, if dispatch had been able to confirm the work order before I even got out of the car, most of this would've been a formality. The whole thing hinged on not having that confirmation up front.

Interviewer: How much did being alone without backup shape your pace?

Participant: Some. I moved a little more carefully closing distance, and I was more inclined to resolve the pocket question myself rather than just let it sit unanswered while I waited.

Interviewer: Looking back, is there anything you'd weigh differently next time?

Participant: Not really. I think I got the balance about right—gave the calm and the story their due, but didn't let them talk me out of checking something I genuinely couldn't identify. That's about as fair as you can be with limited information at two in the morning.

Interviewer: That's helpful, thank you. I think that covers everything I need.

Participant: No problem. Glad it worked out clean for him.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Feature positive effect",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended instances required by vocabulary_control condition rules, overriding the caller-supplied manifest value of 1; the pat-down decision must instead show explicit, proportionate joint weighting of the present cue (pocket bulge) and the absent cue (lack of nervous/evasive behavior)."
      }
    ],
    "target_bias_names": ["Feature positive effect"],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Feature positive effect",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "LE_Biased_1",
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "changed_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Vocab_Control_1",
    "domain_id": "LE",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control condition mandates zero intended occurrences of all named target biases per condition rules, regardless of caller-supplied manifest value.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology set",
      "Four-decision-point structure and sequence",
      "Actor roles and stakeholder set",
      "Emotional tone and difficulty level",
      "Probe category coverage (cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, hypotheticals)"
    ],
    "generation_warnings": [
      "The caller-supplied exact-occurrence manifest specified 1 occurrence of Feature positive effect, but condition rules for vocabulary_control require zero intended instances of all named target biases. This specification overrides the manifest count to 0 in accordance with the CONDITION RULES section, and documents the override here for audit purposes rather than silently reducing an occurrence count under the biased condition rules."
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
