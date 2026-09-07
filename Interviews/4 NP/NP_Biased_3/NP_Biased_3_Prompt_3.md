You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about your decision-making during the last refueling outage, not a performance review. Everything you share is for process improvement. Can you tell me your role and roughly how long you've been doing outage coordination?

Participant: Sure, happy to walk through it. I'm the maintenance planner and outage coordinator for the unit — been doing this specific role about six years, plus four years as a planner before that. My main job during the outage is to sequence work orders against the critical path, allocate craft-hours, and make sure everything closes out before we hit the mode change hold points.

Interviewer: What made this particular outage stand out from a routine one?

Participant: Honestly, the sheer volume — we had around 140 concurrent work orders competing for a fixed 21-day window, and craft-hours were tighter than usual because two contractor crews got pulled to another site mid-cycle. So there was a lot of juggling. The item that ended up taking more of my attention than I expected was FW-IV-204, one of our feedwater isolation valves.

Interviewer: Take me through the sequence of events, from initial scoping to final return to service.

Participant: At the start of scoping, FW-IV-204 had a minor packing weep — nothing new, it had shown up in two prior outage condition reports, both closed as acceptable-as-found. No trend showing it was getting worse. But right around scoping, I'd just heard a pretty detailed account from a colleague about a similar valve at a sister unit that failed and caused a multi-day slip to their critical path. That story was fresh in my head when I built the priority list. I bumped FW-IV-204 up to top-tier priority for rework. Then, once we got into execution, craft-hours were running thin one afternoon and I had to lock in a crew configuration fast for the valve job — Outage Manager wanted it settled within the hour. I went with the first configuration that cleared the minimum schedule and safety requirements. Later in the outage, during post-maintenance testing, we saw a mild vibration anomaly on the pump bearing right next to FW-IV-204. My first thought was residual misalignment from the rework we'd just done. I pulled vibration data that fit that theory, we closed it out, and eventually got system engineer concurrence and did the walkdown before returning the unit to service.

Interviewer: Let's slow down and reconstruct the timeline in more detail. When exactly did FW-IV-204 first come onto your radar for this outage?

Participant: Right at the outset of scoping, maybe day one or two of pre-outage planning. It was already on the work list from the prior cycle's CR, so it wasn't a surprise. What changed was how I ranked it relative to everything else.

Interviewer: And the vibration anomaly — when did that surface relative to the valve work?

Participant: That was maybe day fourteen, after the valve rework was already complete and we were running post-maintenance functional tests on the adjacent feedwater pump.

Interviewer: Let's go through each of those decision points one at a time. First — the priority ranking. What information did you actually have in front of you when you made that call?

Participant: I had the two prior CRs, both closed, no adverse trend on leak rate. I also had the backlog of other work orders, some with comparable or even higher CR severity ratings. Objectively, on paper, FW-IV-204 wasn't the most urgent thing on the list.

Interviewer: So what tipped it to top-tier?

Participant: The sister-unit story, honestly. It was detailed — apparently their valve packing failed catastrophically enough to slip their whole schedule by several days, and it involved almost the exact same valve type. That stuck with me. I remember thinking, we don't want to be the ones explaining a multi-day slip because we treated this as routine. So I moved it up.

Interviewer: Did you go back and re-check the trend data before finalizing that ranking?

Participant: No, not really. I had the CR history in mind from having reviewed it originally, but I didn't pull updated numbers specifically to test whether the concern was warranted. It felt like the kind of thing where the downside of being wrong was bad enough that I didn't need to.

Interviewer: Understood. Second decision point — the crew configuration under the tight craft-hour window. Walk me through that.

Participant: We were maybe two-thirds through the day's craft-hour budget, and I had several configurations that would technically work — different mixes of overtime, different sequencing with other jobs. The Outage Manager wanted a decision inside the hour to protect the critical path. I looked at the first configuration that met minimum schedule and safety requirements, confirmed it cleared those bars, and locked it in.

Interviewer: Did you consider comparing the other options more fully?

Participant: I thought about it, but comparing all the variables — overtime cost, fatigue limits, downstream sequencing — for three or four configurations would have eaten time I didn't have. So I went with what worked and moved to the next fire.

Interviewer: What happened as a result?

Participant: It created a minor sequencing conflict later with an unrelated pump job — nothing that blew the schedule, but craft had to shuffle around it. When we reviewed it afterward, there was a configuration that would have avoided that friction. Marginally better, not dramatically.

Interviewer: Third decision point — the vibration anomaly. What was your first working theory?

Participant: Residual misalignment from the valve rework. It made sense sequentially — we'd just had hands in that area, and a little post-maintenance vibration isn't unheard of.

Interviewer: What data did you pull to check that theory?

Participant: I asked for the immediate vibration readings from the test run, the ones that would show whether the signature matched a misalignment pattern. They looked consistent with that, so I documented the anomaly as resolved on that basis.

Interviewer: Was there other data available that you didn't request at that point?

Participant: In hindsight, yes. There was a lubrication log entry for that bearing that existed in the system at the time. I didn't pull it because the misalignment explanation already fit what I was seeing, and I didn't feel a need to widen the search once I had a reading that matched.

Interviewer: What about the full trend history for that bearing?

Participant: Also didn't pull that at the time. The system engineer reviewed it later, after the fact.

Interviewer: Last decision point — the final return-to-service call. What was your basis for concurring?

Participant: By that point, all the CRs on the valve and the adjacent pump were formally closed, the system engineer had given written concurrence, and I did the walkdown myself with operations. Given the sign-offs and what I observed directly during the walkdown, I concurred with return to service. I did weigh the earlier vibration discussion against that documentation, but everything on paper and everything I saw in the field lined up, so I didn't see a basis to hold it further.

Interviewer: Did you consider requesting extra monitoring time before mode change?

Participant: I did think about it briefly, given the anomaly earlier in the outage, but with the engineering concurrence and a clean walkdown, holding the unit longer without a specific technical reason didn't seem justified.

Interviewer: How much time pressure were you under across these decisions, generally?

Participant: Constant, honestly, but it spiked hardest around the crew assignment call — that was the one hour deadline. The priority ranking and the vibration call had a bit more breathing room, even if it didn't always feel that way in the moment.

Interviewer: If the lubrication log had been sitting on your desk when the vibration anomaly came up, do you think it would have changed your review?

Participant: Possibly. If it had shown something inconsistent with misalignment, I probably would have widened the investigation. It just wasn't something I went looking for at the time.

Interviewer: Looking back, is there a point where a different call on FW-IV-204's priority might have changed how things unfolded?

Participant: Maybe. If I'd ranked it purely on the documented trend, it might have sat lower in the queue, and I'd have had more craft-hours free for other jobs earlier. Hard to say if that changes anything meaningfully, since the valve work itself went fine.

Interviewer: Anything you'd tell a newer planner based on this outage?

Participant: Mainly to keep coming back to the actual trend data, even when a recent story or a tight clock makes a different path feel more urgent. It's not that those instincts are wrong, just that they're easy to lean on more than the numbers warrant.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overweighting a vivid recalled sister-unit incident over flat local trend data during priority ranking."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as satisficing crew-configuration selection under time/cognitive constraint rather than exhaustive comparison."
      },
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as selective evidence request/review consistent with an existing working theory, omitting available disconfirming sources."
      }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Bounded Rationality",
      "Confirmation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Availability Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Bounded Rationality",
        "requested_occurrences": 1
      },
      {
        "bias": "Confirmation Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias",
        "decision_point": 1
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 2
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias",
        "mechanism": "Recall vividness of a memorable sister-unit valve failure inflates perceived risk of local, statistically unremarkable valve issue, overriding documented trend data during priority ranking.",
        "affected_reasoning_operation": "Risk/priority ranking of competing outage work orders",
        "evidence_source": "Verbal/recalled sister-unit incident vs. documented local CR trend data",
        "distinctiveness_requirement": "Only occurrence of Availability Bias in the interview; must not be repeated at other decision points or in hypotheticals."
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Time- and capacity-constrained selection of the first satisfactory crew configuration instead of continued search for an optimal one.",
        "affected_reasoning_operation": "Resource/crew allocation under schedule constraint",
        "evidence_source": "Craft-hour budget status and multiple feasible but uncompared crew configurations",
        "distinctiveness_requirement": "Only occurrence of Bounded Rationality in the interview; distinct decision point and reasoning operation from the other two instances."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective solicitation and interpretation of vibration data consistent with a pre-formed misalignment theory, while not requesting available disconfirming lubrication/trend records.",
        "affected_reasoning_operation": "Evidence selection and interpretation during anomaly investigation",
        "evidence_source": "Post-maintenance vibration readings vs. unrequested lubrication log and full trend history",
        "distinctiveness_requirement": "Only occurrence of Confirmation Bias in the interview; occurs at decision point 3 only, not reintroduced at decision point 4's return-to-service judgment."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias",
        "strength": "subtle"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_3",
    "domain_id": "NP",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1, 2, 3) selected for best mechanism fit and narrative realism; decision point 4 reserved as a neutral, non-biased judgment call to provide contrast and prevent unintended bias clustering.",
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
