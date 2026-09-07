You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for an internal reliability-process review, not a safety investigation into you personally — we're trying to understand how these calls actually get made in practice. That okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me your role and how this particular case landed on your desk?

Participant: Sure. I'm a reliability engineer in Maintenance Control. Part of my job is watching for repetitive write-ups across the fleet and deciding when something crosses from "normal noise" into something that needs a formal corrective action. This one came up because tail 738 logged a third APU bleed air valve write-up inside 45 flight days. Two earlier ones had been closed out as operational check normal, no parts changed, which is pretty typical — a lot of these clear on the bench.

Interviewer: Walk me through the incident from the beginning, in your own words.

Participant: So the third write-up on 738 is what actually got my attention, because three in that short a window is unusual even though our fleet-wide removal rate for that valve was still sitting inside the OEM's published MTBUR. Nothing screamed "fleet problem" yet — it looked like it could just be a stubborn individual aircraft. I opened a focused review on that tail rather than calling it a fleet issue outright, and I put a flag on it so I'd get pinged if anything similar showed up elsewhere. Two days later it did — tail 712 logged a lower-severity version of basically the same complaint. That's when line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility we had an intermittent fault that ground checks weren't catching. At that point I pulled the two tails' component histories together and found they shared the same valve batch lot number. That felt like a real thread to pull.

Interviewer: What did you do with that lot-number connection?

Participant: Company policy is we don't like repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had had an actual in-flight consequence; both faults were caught on the ground. So grounding both outright felt like more than the evidence supported at that point. I put an interim restriction on — one leg of MEL carryover maximum, then it has to be addressed — on both tails, and opened a formal root-cause investigation tied to that lot number.

Interviewer: What came back from that investigation?

Participant: The vendor quality engineer confirmed that lot had a documented seal-material change about six months earlier. That's a real, traceable cause — not a guess. And our in-house teardown of the valve we'd pulled off 738 showed seal degradation that was consistent with exactly that material change. So by that point I had two independent lines — vendor documentation and physical teardown — pointing at the same thing.

Interviewer: Let's slow down on that moment, because I want to understand what happened next. What were you weighing?

Participant: Right, so this is the part before I finalized anything for the Reliability Control Board. I had ten days to the RCB deadline. The existing evidence — the vendor's lot documentation plus our own teardown — already lined up on the seal material as the cause. Technically that was enough to write the corrective action request. But there was also an option to send the valve out to an external metallurgical lab for an independent composition assay, which would be a fully independent third data point rather than relying on the vendor's own account of their material.

Interviewer: And what did you decide?

Participant: I sent it out. I wanted the submission to be as solid as possible — this is a corrective action request that could turn into a fleet campaign, and I didn't want to hand the board something that was only two-thirds independently verified. Having a truly outside lab confirm it felt like it would make the whole package more defensible, even knowing the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back.

Interviewer: At the time you sent it out, was there anything the assay could tell you that would have changed which corrective action you recommended?

Participant: Honestly... probably not the underlying conclusion. The seal-material story was already coherent — vendor records and physical teardown agreed. I think I was thinking more about the strength of the case than whether the case would actually change.

Interviewer: What happened with the deadline?

Participant: We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results. When the assay results did eventually land, they confirmed the same seal-material change the vendor had already told us about — nothing new in it.

Interviewer: Let's move to the final decision — what you actually recommended once everything was in.

Participant: Once the root cause was locked down, the OEM tech rep raised the idea of a broader design review of the valve seal spec generally, as a longer-term option. But that's a slow, separate track. What I had in front of me was a specific, bounded problem: one vendor lot, identifiable serial ranges. I wrote the corrective action request to replace valves from that lot specifically, not a fleet-wide swap of every valve regardless of lot, and not just deferring to wait on the OEM's broader review.

Interviewer: Why bounded to the lot rather than fleet-wide?

Participant: Because a fleet-wide replacement would have pulled serviceable, unaffected valves for no reason — that's cost and downtime with no reliability benefit. The evidence pointed specifically at that lot, so that's what I scoped the action to.

Interviewer: What happened after you submitted it?

Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review got pushed into a separate long-term study, which is still open as far as I know.

Interviewer: Looking back at the whole sequence — is there a point where, with hindsight, you'd handle it differently?

Participant: The one thing I go back and forth on is the external lab. If I'd known going in that it would just restate what we already had, I might have submitted on the original ten-day timeline and let the RCB approve based on the vendor and teardown evidence alone. I don't think it was wrong to want outside confirmation — this becomes a fleet-level safety call, and I'd rather be too careful than not careful enough. But I'll admit, looking at it now, I'm not sure that extra data point actually changed anything I ended up recommending.

Interviewer: If the assay had come back showing something different from the vendor's account — a different degradation mechanism, say — what would you have done?

Participant: Then it would've mattered a lot, and I'd have had to go back and possibly widen the scope beyond that one lot. That's part of why it felt worth doing at the time.

Interviewer: And if this exact pattern showed up again on a different fleet type — same lot-based signature, same timeline pressure — would you send it out for independent lab work again?

Participant: Probably, yeah, if the timing allowed it. Though I think I'd ask myself earlier on whether the extra data was likely to change the recommendation or just make me feel better about it, and weigh that against the deadline more explicitly than I did this time.

Interviewer: That's a good place to stop. Thanks for the detail — this is exactly the kind of reconstruction we needed.

Participant: No problem. Happy to follow up if anything else comes to mind.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Information bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as seeking additional data that cannot change the pending corrective-action decision, motivated by a belief that more information improves decision quality/defensibility rather than by actual decision relevance."
      }
    ],
    "target_bias_names": [
      "Information bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Information bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "mechanism": "Commissioning a costly, schedule-delaying external metallurgical assay that duplicates already-sufficient vendor and in-house evidence, pursued because more information is assumed to be inherently valuable/defensible rather than because it can change the corrective-action recommendation.",
        "affected_reasoning_operation": "Evidence-sufficiency assessment prior to finalizing a root-cause-based recommendation",
        "evidence_source": "External metallurgical assay request vs. existing vendor lot documentation and in-house teardown results",
        "distinctiveness_requirement": "Single instance only; must not be echoed as a second, differently-worded instance at any other decision point, probe, or hypothetical."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_1",
    "domain_id": "AV",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point (phase 3, evidence-selection prior to corrective-action recommendation) offering the best mechanism fit for information bias, where sufficient decision-relevant evidence already existed and additional information-seeking could not alter the outcome; no split across multiple points was needed since occurrences = 1.",
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
