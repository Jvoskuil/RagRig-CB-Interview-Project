You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for sitting down for this. Same as before — this is a confidential debrief for training research, not a personnel review. I'll ask you to walk through a specific check ride in detail. Okay to go ahead?

Participant: Sure. This one was a Line Check, OPC cycle, on a senior widebody captain — very experienced, long time on type. I was up front as the TRE.

Interviewer: What was the flight meant to accomplish, and what was your role?

Participant: Standard revenue sector. I'm there to evaluate his technical handling and CRM for the recurrent check, intervening only if there's a safety need. First officer was PM.

Interviewer: Take me through what happened, from the start.

Participant: Before we got out to the aircraft, I looked at the tech log. One prior flight had logged an ADIRU 2 advisory — it cleared on its own in flight. Maintenance inspected it on the ground, couldn't confirm a fault on their test, but they went ahead and replaced a connector they suspected as a precaution. So it wasn't a clean bill of health exactly — more like "we think we found it, but we're not certain." We talked about that briefly during the walk-around. Departure was normal. Climbing through about FL250 we got a caution — an IRS align caution, not the same wording as the previous flight's advisory — and it cleared in maybe ten seconds. No checklist auto-triggered. Later in cruise, a different thing came up entirely — nothing to do with the ADIRU. The captain was working a minor non-normal checklist for an unrelated caution, and there was a verification step in it that takes a while and doesn't affect safety of flight. He told the FO he'd hold that one and come back to it once things settled down, which he did later in cruise. Everything else on the flight was uneventful. Normal approach and landing.

Interviewer: What happened after landing?

Participant: I wrote the report, graded the performance. A colleague — another TRE — looked at it and asked whether I'd have graded the deferred checklist item the same way with a different crew pairing. I told him honestly I wasn't sure. A few days later maintenance said the replaced connector had been seated correctly and they couldn't tie it definitively to either the first flight's advisory or ours. So the picture's still not fully closed.

Interviewer: Let's go back to the tech log discussion before departure. What went through your mind?

Participant: There were two things pulling in different directions. On one hand, maintenance had physically done something — replaced a part — not just signed a form. That counts for something. On the other hand, their own test didn't confirm a fault, so the replacement was really a guess about what might have caused it. I raised that with the captain — that we were accepting the aircraft on the strength of an educated guess, not a confirmed fix.

Interviewer: Did you consider asking maintenance control for more before departure?

Participant: I thought about asking whether they'd tested the replaced connector under load, not just visually. I didn't end up asking. Partly schedule, partly that it felt like it might not have changed anything practical — if they said yes, fine, if they said no, we'd probably still have gone. So there wasn't a single clean reason either way.

Interviewer: What would have had to be different for you to hold the flight?

Participant: Honestly, I go back and forth on that. If the write-up had said "fault confirmed, unresolved," that's different. What we had was murkier — inspected, not confirmed, acted on anyway. I can see an argument for going and an argument for waiting.

Interviewer: Move to the climb, when the caution came up. Walk me through that.

Participant: The caution came up, cleared in about ten seconds, no checklist triggered. I remember specifically noting to the captain that this wasn't the same wording as the previous flight's write-up — different system behavior, not obviously connected. That mattered to me because I didn't want either of us assuming it was "the same thing again" when it might not be.

Interviewer: What alternative did you weigh?

Participant: Leveling off to watch a couple more parameters before continuing. I considered it. In the end the absence of a checklist trigger carried more weight, but I wouldn't say it was an easy call — an ADIRU-adjacent caution always has some amount of "we don't fully know what's behind this" to it, regardless of how it presents.

Interviewer: How confident were you in that read at the time?

Participant: Moderately. Not fully confident, not dismissive either. I flagged the uncertainty out loud rather than treating it as settled.

Interviewer: Now cruise, when the captain deferred that checklist step. How did you evaluate that?

Participant: He explained his reasoning to the FO — the item doesn't affect flight safety, he'd come back to it, and he did. The checklist itself allows some latitude on sequencing non-critical items. So there's a real basis for calling that acceptable. At the same time, a stricter reading of the manual might say any deferral should be flagged differently regardless of the rationale. I noted both readings in the report rather than picking one as obviously correct.

Interviewer: If a newer captain had made the identical call, would you have graded it the same?

Participant: I've genuinely thought about that and I don't have a settled answer. Possibly yes, because the rationale and outcome would be identical. Possibly not, if I'd want to see more explicit checklist referencing from someone earlier in their career. I can argue it either way.

Interviewer: Last one — the peer's question afterward about whether your standard would hold for a different crew pairing. How did you respond?

Participant: I told him it was a fair question and I wasn't sure. I've had mixed views on this myself across different checks — sometimes I think the standard should be identical regardless of who's flying, other times I think context legitimately matters. I suggested we bring it up at the next standardization meeting rather than me just deciding it on the spot.

Interviewer: Is there anything that would have changed your mind on any of these calls?

Participant: If the connector issue had turned out to be confirmed and unresolved, the dispatch call looks different in hindsight. If the deferred checklist item had caused any downstream problem, that grading looks different too. But neither of those things happened, so I'm left without a clean answer on which reading was right.

Interviewer: Last question — if you ran this same flight again with the same information, what would you do differently?

Participant: I might ask maintenance control the load-test question next time, mostly for the record. Beyond that, I honestly don't know that I'd change the calls themselves. I can see reasonable people landing on either side of each one.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Bias Blind Spot",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Normalcy Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Experience Bias or Trusting expert intuition",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      }
    ],
    "target_bias_names": [
      "Bias Blind Spot",
      "Normalcy Bias",
      "Experience Bias or Trusting expert intuition",
      "Illusion of validity"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bias Blind Spot", "requested_occurrences": 0 },
      { "bias": "Normalcy Bias", "requested_occurrences": 0 },
      { "bias": "Experience Bias or Trusting expert intuition", "requested_occurrences": 0 },
      { "bias": "Illusion of validity", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "AV_Biased_4",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Ambigious_4",
    "domain_id": "AV",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, so no bias instances are planned. Decision points are instead structured to mirror the paired biased scenario's mechanism-fit locations (dispatch acceptance, in-flight advisory response, evaluative grading, post-flight reflection) while each is written to remain genuinely underdetermined between a defensible judgment and a less careful one, without resolving into any target bias mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and role (aviation, Check Airman/TRE)",
      "Setting (Line Check/OPC on a senior widebody captain, revenue flight)",
      "Four-decision-point structure and ordering",
      "Stakeholder roster and interaction pattern",
      "Technical vocabulary level and terminology set",
      "Difficulty level (challenging) and approximate word count",
      "Dialogue format and emotional tone"
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
