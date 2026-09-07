You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for joining me. This is being recorded for an internal reliability-process review, not a personnel evaluation — we're just trying to understand how these calls actually get made. Okay to proceed?

Participant: Sure, no problem.

Interviewer: Can you tell me your role and how this case came across your desk?

Participant: I'm a reliability engineer in Maintenance Control. Part of my job is tracking repetitive write-ups across the fleet and deciding when something needs a formal corrective action versus routine monitoring. This one started when tail 738 logged a third APU bleed air valve write-up inside 45 flight days. The first two had closed out as operational check normal — no parts replaced — which is common; a lot of these clear on the bench and never come back.

Interviewer: Walk me through the incident from the start.

Participant: The third write-up on 738 is what caught my attention. Three in that short a window is unusual, though our fleet-wide removal rate for that valve was still inside the OEM's published MTBUR, so nothing yet told me this was a fleet problem. It looked like it could just be a stubborn individual aircraft. I opened a focused review on 738 and put a flag on it so I'd get pinged if anything similar turned up elsewhere. Two days later it did — tail 712 logged a lower-severity version of the same complaint. Line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility of an intermittent fault that ground checks weren't catching. I pulled the two tails' component histories together and found they shared the same valve batch lot number. That was the first real thread.

Interviewer: What did you do with the lot-number connection?

Participant: Company policy discourages repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had an in-flight consequence; both were caught on the ground. Grounding both outright felt like more than the evidence supported at that point, so I set a one-leg maximum MEL carryover on both tails and opened a formal root-cause investigation tied to the lot number.

Interviewer: What came out of that investigation?

Participant: The vendor quality engineer confirmed the lot had a documented seal-material change about six months earlier — that's a traceable, real candidate cause. But when I got the in-house teardown back on the valve pulled from 738, the degradation pattern wasn't clean. It was consistent with the seal-material change, but it also overlapped with a separate supplier nonconformance that had been logged against an earlier serial range — and that nonconformance would have implied a wider set of affected valves than just this lot.

Interviewer: That sounds like it complicated things. What were you weighing at that point?

Participant: Right, this is before I finalized anything for the board. I had ten days to the RCB deadline. If I went with just the vendor documentation and the ambiguous teardown, I'd be guessing at which of the two explanations was actually driving the failures — and that guess would directly change how many valves I'd be asking to replace. One candidate pointed at a single lot; the other pointed at a broader serial range. An external metallurgical lab could run a composition assay that would distinguish the two, but their turnaround was about three weeks, which meant blowing through the RCB deadline before I'd have an answer.

Interviewer: What did you decide?

Participant: I sent it out. I genuinely didn't know which cause was correct, and the two answers led to different-sized corrective actions. Submitting on the original timeline would have meant picking one interpretation without being able to defend it if someone on the board asked why I ruled out the other nonconformance. I'd rather take the deadline hit than write a scope I couldn't justify.

Interviewer: At the time, was there anything that assay could tell you that would actually change your recommendation?

Participant: Yes — directly. If it had come back pointing at the broader nonconformance instead of the seal-material change, I'd have had to widen the replacement scope well beyond this one lot, potentially into aircraft that hadn't shown any symptoms yet. That's a materially different corrective action request, so the result wasn't just confirmatory. It was the thing that would tell me which request to write.

Interviewer: What happened with the deadline?

Participant: We missed the RCB cycle. It slipped to submit-pending-lab-results. When the assay came back, it identified the seal-material change as the actual cause and ruled out the other nonconformance. So the lot-bounded scope held up, but I didn't know that going in.

Interviewer: Take me to the final decision — what you actually recommended.

Participant: Once the assay settled which mechanism was operating, the OEM tech rep also raised a broader design review of the seal specification generally, as a longer-term item. That's a slower, separate track. What I had in hand was a specific, bounded problem: one vendor lot, identifiable serial ranges, and now a cause that was no longer ambiguous. I wrote the corrective action request to replace valves from that lot specifically — not a fleet-wide swap, and not deferring to wait on the OEM's broader review.

Interviewer: Why bounded to the lot rather than fleet-wide?

Participant: Because a fleet-wide replacement would pull serviceable, unaffected valves for no reliability benefit — that's cost and downtime without a justified reason. Once the assay confirmed the mechanism, the evidence supported exactly that lot, so that's what I scoped the action to.

Interviewer: What happened after submission?

Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review is still running separately, unrelated to this specific corrective action.

Interviewer: Looking back, is there a point you'd handle differently?

Participant: Honestly, I keep coming back to the deadline slip. I don't think I'd change the decision to get the assay — the ambiguity was real, and guessing wrong on scope would have been worse than being late. But I might push harder next time to get the lab to prioritize a case like this, or find out earlier whether a faster partial test could resolve just the scope question without needing the full three-week turnaround.

Interviewer: If the teardown result hadn't been ambiguous — if it had clearly pointed to just the seal-material change from the start — would you still have sent it out?

Participant: Probably not on the same timeline. If the in-house evidence had cleanly ruled out the other nonconformance, there wouldn't have been a live scope question left to answer, and I'd have likely submitted on the original ten days.

Interviewer: And if this exact pattern showed up on a different fleet type — same kind of ambiguity, same deadline pressure — would you send it out again?

Participant: Yes, if there were genuinely two live explanations with different-sized consequences. That's really the test I'd apply — whether the result could actually change what I'd recommend, not just make the file feel more complete.

Interviewer: That's a good place to stop. Thanks for walking through it in this much detail.

Participant: Happy to help — glad it was useful.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Information bias",
        "occurrences": 0,
        "mechanism_constraint": "Per vocabulary_control condition rules, zero intended instances must be implemented regardless of the caller-supplied manifest value of 1; the evidence-selection decision (decision point 3) must instead be written so the external assay is genuinely decision-relevant (capable of changing corrective-action scope), removing the mechanism entirely rather than weakening it."
      }
    ],
    "target_bias_names": [
      "Information bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Information bias",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "AV_Biased_1",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Vocab_Control_1",
    "domain_id": "AV",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is vocabulary_control, which requires zero intended instances of all named biases regardless of the input occurrence manifest. The caller-supplied manifest value of 1 for Information bias is overridden to 0 per CONDITION RULES; the decision point that hosted the bias mechanism in the paired scenario (decision point 3, evidence-selection prior to corrective-action recommendation) is retained structurally but rewritten so the same evidence-selection act is fully decision-relevant and non-biased, preserving vocabulary, structure, and decision count parity with AV_Biased_1.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and role (Aviation Maintenance Planner / Reliability Engineer, regional airline MCC)",
      "Fleet size, affected tail count, and RCB deadline (10 days)",
      "Full technical vocabulary list used in AV_Biased_1",
      "Four-decision-point structure and its ordering (triage, interim restriction, evidence-selection, final corrective-action scope)",
      "Actor roster (line maintenance supervisor, OEM technical representative, vendor quality engineer, flight operations scheduling manager)",
      "Emotional tone/register and difficulty level",
      "Absence of any acute in-flight safety event"
    ],
    "generation_warnings": [
      "The input occurrence manifest specified 1 occurrence of Information bias, but the vocabulary_control condition mandates zero intended instances of all named biases; this specification overrides the manifest count to 0 for the public interview as required by CONDITION RULES, and this override is recorded here rather than silently applied without documentation."
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
