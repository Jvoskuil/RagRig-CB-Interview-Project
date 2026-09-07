You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for sitting down for this. This is a voluntary debrief for our operational learning file, not disciplinary. Can you tell me your role that shift and what the plan was?

Participant: Sure. I was Control Room Supervisor on dayshift. We were about five days past a refueling outage, running a scheduled ascension from 45 up to a 75 percent hold point. Standard evolution — controlled rod withdrawals, watching secondary parameters track along. Management wanted us at the hold point that day for a grid commitment, so there was a schedule to keep, but nothing forcing anyone's hand. Turnover wasn't a factor — I was only a few hours into the shift, still had most of it ahead of me.

Interviewer: What was your general read on plant status as the shift moved into the middle stretch?

Participant: Pretty routine. Ascensions like this usually throw a couple small things at you — nothing alarming, just things worth tracking. That's what happened here.

Interviewer: Walk me through the incident as it unfolded.

Participant: About two hours in, the reactor operator flagged that feedwater pump 1B's discharge pressure had a slow upward oscillation — vibration monitor ticking up too, still well within the normal band, no alarm. I had him log it and bump up the monitoring interval rather than pulling in the system engineer right away, since nothing was abnormal enough yet to justify an operability call. About forty minutes later, during a rod withdrawal, we got a brief blip in steam generator B's narrow range level — auto control caught it in seconds. Small thing, but two developing items at once gets your attention. I called our on-call reactor engineer, walked him through it, and he said it looked consistent with known control response at that power level. Level stayed stable after that.

Then, later in the shift, the pump vibration had crept up again — now sitting in the upper third of its normal band. Still no tech spec limit reached, no alarm. But it had been trending the same direction for a while, and I was pulling together materials for a surveillance test pre-brief due in about forty-five minutes, on top of the ascension schedule. I told the crew to keep it on the standard continue-and-monitor watch we use for that kind of trend, and we carried on toward the next hold point. During the pre-brief itself, the test coordinator asked an unrelated procedural question that happened to touch on the vibration item, and I mentioned it in passing without going into detail. About ninety minutes after that, the pump ended up on a formal close-monitoring action under a tech spec statement — the trend kept climbing. I pulled the historical comparison myself later that shift, once the pre-brief wrapped up.

Interviewer: Let's go through that in order. First, the pump reading forty minutes in — what informed logging it and increasing monitoring instead of calling the engineer immediately?

Participant: There wasn't much to react to yet — within the band, no real trend history to speak of. Calling the engineer for every early wobble creates noise. Tightening the interval was the right first move; escalate if it keeps climbing.

Interviewer: And the level blip — what made you check with the on-call engineer rather than rely on your own read?

Participant: Auto control handled it fine, so it wasn't urgent operationally. But two things trending at once during an ascension makes you want a second opinion, especially something with a control-system explanation I wanted verified rather than assumed.

Interviewer: Now the point where vibration crossed into the upper third of the band while you were assembling pre-brief materials. What options did you weigh, and what pushed you toward the standard response?

Participant: That's the one I've turned over the most. I had three things going — the pump, the pre-brief prep, and the ascension clock. The continue-and-monitor approach is what we've used for trends like this before, and it's worked, so that's the direction I went. Pulling the historical vibration comparison off the plant computer was something I could've done — the data was right there — but between the pre-brief materials and the schedule, it didn't feel necessary in that window. It wasn't that I decided the comparison was pointless, I just didn't work it in.

Interviewer: Did you consider holding the ascension until the engineer completed a documented review?

Participant: Briefly, but the trend hadn't broken any limit and the checklist response has covered similar-looking situations before. So I went with what I knew rather than stopping to build a fuller comparison right then.

Interviewer: How much did the upcoming pre-brief shape that, compared to if nothing else had been due?

Participant: Some. When you're building out pre-brief materials and tracking an ascension schedule at the same time, you lean on what's familiar instead of starting fresh on every item. If I'd had a totally open stretch, I probably would've poked at the historical data just out of curiosity. In hindsight, the rate of rise on that trend was a bit different from the earlier cases I was drawing on, but I didn't do the side-by-side to notice that at the time.

Interviewer: During the pre-brief, what determined how much you said about the vibration trend?

Participant: I mentioned it in passing when the coordinator's question happened to touch on it — kept it brief since it wasn't the topic of that meeting and it was already framed as a monitor-and-continue item in my head. I figured I'd circle back to it once we were done.

Interviewer: You mentioned pulling the historical comparison yourself afterward. What prompted that, given there was no handoff forcing your hand?

Participant: Once the pre-brief wrapped, it was one of the first things on my list — nobody was waiting on me to hand it off, but it had been nagging at me a bit. The comparison showed the rate of climb didn't quite match the earlier benign cases.

Interviewer: If nothing else had been competing for your attention at that moment on the ascension, would you have handled the vibration trend differently?

Participant: Probably would've pulled the comparison right then instead of after the pre-brief. Having one clear task instead of two changes what feels worth doing in the moment versus what can wait.

Interviewer: If that comparison data had been sitting in front of you right when the trend crossed into the upper third of the band, do you think it would have changed your decision?

Participant: Possibly. If it had shown the rate of rise was outside what we'd seen before, I'd have leaned toward holding rather than continuing. But at the time I was working off what had worked previously, not off that specific comparison.

Interviewer: What would you tell a newer supervisor about handling a trending-but-not-alarming parameter when something else, even something unrelated, is pulling at your attention?

Participant: That divided attention narrows what you actually look at, even without a handoff involved. The item that ends up mattering isn't always the one making noise — sometimes it's the one you've already decided you understand.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Imperfect Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Imperfect Rationality",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Under concurrent cognitive load from a non-handoff competing task (surveillance pre-brief preparation) and ascension schedule pressure, CRS selects a familiar 'good enough' checklist response over full evaluation of accessible comparative vibration trend data, satisficing rather than optimizing the continue/hold decision.",
        "affected_reasoning_operation": "Evidence integration and option evaluation prior to a continue/hold decision",
        "evidence_source": "Plant computer historical vibration trend library (accessible but not consulted) versus prior similar-event checklist experience",
        "distinctiveness_requirement": "Must show that full evaluation was feasible (data accessible) and consciously foregone in favor of a familiar heuristic response, and that this occurs even absent a handoff obligation, distinguishing it from mere reasonable time-constrained prioritization tied specifically to turnover."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ir_cf_01",
        "bias": "Imperfect Rationality",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": "NP_Biased_1",
    "counterfactual_variable": {
      "name": "Presence of an imminent shift-turnover handoff obligation at decision point 3",
      "original_state": "Shift turnover approaching in ~45 minutes, requiring the CRS to draft and finalize a turnover brief for the oncoming crew concurrently with monitoring the vibration trend.",
      "changed_state": "No shift turnover during this window (turnover ~4 hours away); CRS instead prepares a time-boxed pre-brief for an unrelated scheduled surveillance test due in ~45 minutes, producing an equivalent-magnitude competing-task deadline without a handoff obligation.",
      "variables_to_hold_constant": [
        "Feedwater pump 1B vibration trend magnitude and timing",
        "Steam generator level oscillation event and its resolution",
        "Ascension schedule and power hold-point timing",
        "Staffing levels and on-call engineer availability",
        "Accessibility of the plant computer historical trend library",
        "Alternatives available at all four decision points",
        "Imperfect Rationality occurrence count, decision point, mechanism, and strength"
      ]
    },
    "scenario_id": "NP_Counterfactual_1",
    "domain_id": "NP",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to decision point 3, identical to the paired base scenario NP_Biased_1, per allocation rules 2 and 3, to isolate the effect of the counterfactual causal variable while holding the bias mechanism, decision point, and strength constant.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Feedwater pump 1B vibration trend magnitude and timing",
      "Steam generator level oscillation event and its resolution",
      "Ascension schedule and power hold-point timing",
      "Staffing levels and on-call engineer availability",
      "Accessibility of the plant computer historical trend library",
      "Alternatives available at all four decision points",
      "Imperfect Rationality occurrence count (1), decision point (3), mechanism, and strength"
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
