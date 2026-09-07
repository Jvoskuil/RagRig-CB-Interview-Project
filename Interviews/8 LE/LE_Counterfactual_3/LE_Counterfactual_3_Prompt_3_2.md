You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. This is for our case-review research file — I'll ask you to walk through your decision-making on the Riverside apartment case, and it's fine to say you don't recall something exactly. Okay to start?

Participant: Sure, go ahead.

Interviewer: Can you start with your role and how the case came to you?

Participant: I was lead detective, my partner and I caught it together after patrol secured the scene. Apartment homicide, young woman, found by a coworker who came by when she missed a shift. We split canvass and paperwork like usual.

Interviewer: Walk me through the scene.

Participant: No forced entry, deadbolt engaged from inside. That tells you something — either she let someone in, or it's somebody with access. Pulled her phone, found a breakup with her ex about three weeks back, some heated texts, and he had a prior domestic disturbance call at that same address, maybe eight months earlier. Scene damage was mostly contained to the bedroom. Between the lock, the texts, and his history, that's where my attention went first. We also swabbed the scene and pushed it to an expedited lab track — there was already some media interest building, so we had a faster turnaround than usual, maybe a day instead of two or three.

Interviewer: What was the objective at that stage?

Participant: Get a working theory solid enough to direct the canvass without locking in before we had more to go on. Same clock as always — witness memory starts fading fast, and if it is someone connected to her, you don't want to give them time to get comfortable or leave town.

Interviewer: Let's reconstruct the timeline.

Participant: Day one, scene work, the ex's history surfaces, swabs go out on the expedited track. Overnight, the lab actually gets back to us — negative, no DNA match to him at the scene. Day two morning, we walk into the unit briefing already knowing that. Alibi still has a two-hour gap at that point. Day three, a second witness closes that gap, and we finally sit down properly with the rear-entrance witness, who gives us a much sharper description — turns out to match a guy with a burglary record in that block. Day four, we're drafting the referral for the DA liaison.

Interviewer: First decision point — naming the ex as primary on day one, before any lab results.

Participant: Right, nothing back yet at that point. We could've waited on forensics and the full canvass, or treated the rear-entrance sighting as equally weighted from the start. I named him primary anyway — the domestic history, the breakup timing, the locked door, that's a pattern worth acting on with the manpower we had. The rear entrance was just one line from a passerby at that stage, nothing to build resources around yet.

Interviewer: What made that combination feel strong enough to commit to over waiting?

Participant: Mostly experience. You don't get to split resources evenly on day one, so you go where the documented history points. That felt like a defensible use of the shift.

Interviewer: Second decision point — the unit briefing, and this time you already had the negative DNA result in hand.

Participant: Right, that's the part that made that morning different. We walk in already knowing the swab didn't match him. My partner still laid out the domestic-call history pretty forcefully, made the case that the DNA gap didn't mean much on its own. One of the junior guys raised the rear-entrance lead again, said it was worth a real look given the negative result, but it didn't get much traction — people moved on to warrant logistics for the ex fairly quickly. By the end of that meeting the case log still had him as primary, and nobody was formally assigned to run down the loitering report.

Interviewer: How did you square keeping him primary with a negative result already sitting in front of the room?

Participant: I didn't see it as ignoring it. The domestic history and the locked door were still unexplained either way, and everyone in the room seemed to land in the same place once my partner made the case — the DNA on its own didn't feel like it outweighed that. Reopening it right then would've meant pulling someone off the warrant work we were already moving on, and with the room settled, that didn't feel like the priority.

Interviewer: Was there a point where the negative result almost changed the direction of that meeting?

Participant: Briefly, when the junior detective brought it up. But once my partner and the lieutenant seemed comfortable holding the line, it didn't really get pushed further.

Interviewer: Third decision point — day three, alibi closes and the rear-entrance description sharpens.

Participant: That was the harder morning. Second witness closes the two-hour gap completely, and the rear-entrance guy's description gets a lot more specific — matches someone with a burglary record nearby. I still didn't shift the primary theory. The DNA was already a known factor by then, so it wasn't new information exactly — what was new was the alibi and the detailed description, and I kept coming back to the fact that it wasn't enough to undo what we'd already built around him, even though I could see it was chipping away at the case in a way the DNA result alone hadn't. On their own, without independent corroboration, I didn't treat them as decisive enough to flip the case. I logged the alternative as secondary and kept digging on our end.

Interviewer: What was the basis for treating the closed alibi and the new description as not yet decisive?

Participant: One witness closing a gap and one detailed description aren't the same as physical evidence tying someone to the scene. The domestic history was still sitting there unaddressed if it wasn't him. I didn't want to swing the whole case on two pieces of testimony without corroboration.

Interviewer: Fourth decision point — drafting the referral memo.

Participant: By day four we had two live threads: the ex, thinner now, and the burglary-record guy, whose statement was the freshest and most detailed thing in the file. When I wrote the summary for the DA liaison, that statement got the most space and read as the strongest piece on the page, more than the older scene notes or the original canvass material.

Interviewer: What gave it that weight in the writing itself?

Participant: Partly the detail — clearer description, better timing. But honestly, it was also just the last substantial thing that had come in before I sat down to write, so it was what was fresh in my head. I hadn't gone back and stacked it against the earlier material for corroboration, it just carried into the draft that way. The DA liaison ended up asking for supplemental work before filing on either of them.

Interviewer: If the DNA result had come back after the briefing instead of before it, do you think the meeting would have gone differently?

Participant: Possibly. Walking in without that result already known, the room might have leaned harder into the domestic history with less friction, since there'd have been nothing to explain away yet. Having it already on the table at least got it mentioned, even if it didn't change the outcome much.

Interviewer: Had you seen a case before where a negative result early on still didn't shift the team's direction?

Participant: A couple times, yeah. It's usually a reminder to keep digging on the alternative rather than treating one result as the final word either way.

Interviewer: Looking back, is there a moment you'd want to redo?

Participant: Probably assigning someone concretely to the rear-entrance lead right at that second briefing, once the negative result was already in the room. That felt like the moment a small procedural step could've changed the pace of everything after it.

Interviewer: Anything else you'd want on record about how the case moved through those points?

Participant: Just that nothing felt reckless in the moment. Every step had something behind it. It's only looking at the whole thing end to end now that the gaps stand out more.

Interviewer: That's a good place to stop. Thanks for going through it in this detail.
}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Cognitive dissonance",
        "occurrences": 1,
        "mechanism_constraint": "must be triggered by the alibi closure and detailed alternative description at decision point 3, not by the DNA result itself, since the DNA result is already known by that point"
      },
      {
        "bias": "Recency Effects",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Groupthink",
        "occurrences": 1,
        "mechanism_constraint": "must occur at decision point 2 with the negative DNA result already known in the room at the time of convergence"
      }
    ],
    "target_bias_names": ["Cognitive dissonance", "Recency Effects", "Groupthink"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Cognitive dissonance", "requested_occurrences": 1 },
      { "bias": "Recency Effects", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "gt_01", "bias": "Groupthink" },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance" },
      { "instance_id": "re_01", "bias": "Recency Effects" }
    ],
    "intended_decision_points": [
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 2 },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "decision_point": 3 },
      { "instance_id": "re_01", "bias": "Recency Effects", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Team converges on retaining the ex-boyfriend as primary suspect despite an already-known negative DNA result, without assigning independent verification of the dissenting rear-entrance lead",
        "affected_reasoning_operation": "collective decision adoption and dissent evaluation",
        "evidence_source": "briefing discussion occurring after the DNA result is already in hand; partner's continued support; junior detective's dissenting mention",
        "distinctiveness_requirement": "must occur at decision point 2, distinct from the individual-level reconciliation at decision point 3 (cd_01) and the weighting behavior at decision point 4 (re_01); the disconfirming DNA evidence must already be present in the room rather than arriving afterward, distinguishing this instance from the paired biased scenario's version"
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "mechanism": "Reinterpreting the closed alibi gap and the newly detailed alternative-suspect statement as insufficient to override the already-committed theory, while treating the earlier-known negative DNA result as settled rather than reopening it",
        "affected_reasoning_operation": "evidence reconciliation and theory revision",
        "evidence_source": "closed alibi statement and detailed alternative-suspect description at decision point 3",
        "distinctiveness_requirement": "must occur at decision point 3 and must be triggered by the alibi closure and detailed statement, not by the DNA result, since the DNA result was already processed collectively at decision point 2 in this counterfactual variant"
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "mechanism": "Disproportionate weighting of the most recently obtained witness statement over earlier comparable evidence when drafting the referral summary, tied partly to recency of acquisition",
        "affected_reasoning_operation": "evidence weighting and summary drafting",
        "evidence_source": "most recent witness description versus earlier canvass statements and scene notes",
        "distinctiveness_requirement": "must occur during final referral drafting at decision point 4, tied specifically to recency of acquisition rather than theory commitment or group consensus, unchanged in character from the paired biased scenario"
      }
    ],
    "intended_strength": [
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "strength": "subtle" },
      { "instance_id": "re_01", "bias": "Recency Effects", "strength": "subtle" }
    ],
    "paired_scenario_id": "LE_Biased_3",
    "counterfactual_variable": {
      "name": "timing of the forensic DNA result relative to the unit briefing",
      "original_state": "Negative DNA result returns on day three, after the day-two unit briefing has already formalized the ex-boyfriend as primary suspect (LE_Biased_3).",
      "changed_state": "Negative DNA result returns before the day-two unit briefing via an expedited lab track, so the team already knows the result when it converges on the ex-boyfriend as primary suspect.",
      "variables_to_hold_constant": [
        "victim, scene facts, and locked-door context",
        "ex-boyfriend's domestic-call history and breakup timeline",
        "rear-entrance witness and eventual detailed description matching a burglary-record individual",
        "personnel present (partner detective, lieutenant, junior detective, DA liaison)",
        "four-decision-point structure and overall chronology length",
        "the three targeted bias instances and their general character",
        "referral drafting process and DA liaison's request for supplemental work"
      ]
    },
    "scenario_id": "LE_Counterfactual_3",
    "domain_id": "LE",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per bias, reallocated relative to the paired scenario to accommodate the shifted timing of the DNA result: groupthink remains at decision point 2 but now incorporates the already-known negative result as the disconfirming evidence present at the moment of convergence; cognitive dissonance shifts its trigger evidence to the alibi closure and detailed alternative description at decision point 3, since the DNA result is no longer novel at that point; recency effects remains unchanged at decision point 4. Decision point 1 held bias-free as a neutral anchor, matching the paired scenario.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "victim, scene facts, and locked-door context",
      "ex-boyfriend's domestic-call history and breakup timeline",
      "rear-entrance witness and eventual detailed description matching a burglary-record individual",
      "personnel present (partner detective, lieutenant, junior detective, DA liaison)",
      "four-decision-point structure and overall chronology length",
      "the three targeted bias instances and their general character",
      "referral drafting process and DA liaison's request for supplemental work",
      "target word count range (1,215-1,485 words)"
    ],
    "generation_warnings": [
      "Shifting the DNA result earlier necessarily changes the evidentiary content available at decision point 2 (it now includes a negative forensic result) and at decision point 3 (which no longer includes a fresh negative DNA shock). This is an intended consequence of the single causal-variable change and does not constitute a second uncontrolled variable, but validators should confirm that no second unrelated fact (e.g., personnel, tone, or unrelated timeline length) was altered when auditing causal minimality."
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
