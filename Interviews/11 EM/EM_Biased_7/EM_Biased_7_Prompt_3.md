You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this conversation being recorded and used for after-action training purposes, not for any personnel evaluation.

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Can you tell me your role and what you were responsible for when this incident started?

Participant: I'm the Situation Unit Analyst for the county EOC. My job during an activation is to build and maintain the Common Operating Picture — pulling in field reports, sensor data, weather, whatever's coming in — and turning that into something the Branch Directors and the EOC Director can actually make calls from. That night I was covering both the flood side and keeping an eye on the fire branch, since Ridge Fire was still active and eating into our smoke-camera and aerial coverage.

Interviewer: Walk me through how the incident began.

Participant: It started with a notice from the Twin Forks Reservoir Authority around 9 PM. They said they were doing a controlled precautionary release ahead of the storm cell that was coming in — basically getting ahead of it so the reservoir wouldn't be over capacity when the rain hit. Our downstream gauges at that point were showing a gradual rise, nothing dramatic. The duty hydrologist was tied up on another call and wasn't going to be free for at least ninety minutes, so I didn't have anyone to sanity-check the numbers against. Our flood Branch Director, who's been doing this about twenty years, looked at the same notice and said this was a routine pattern, that he'd seen the reservoir do exactly this kind of release two or three times before.

Interviewer: What did you decide to do with that information?

Participant: I recommended we go with a monitor-and-prepare advisory rather than jump straight to a warning for Sector 7. The operator's language was pretty clearly framed as precautionary — they used the word "controlled" a couple times — and combined with the Director's read that this looked routine, it felt like the proportionate response. I remember thinking, if this were really an emergency release they wouldn't be calling it precautionary.

Interviewer: Did you consider verifying that independently before finalizing the advisory?

Participant: I thought about it, but with the hydrologist unavailable and the Director being pretty confident, it seemed like it would just slow things down without adding much. He's the one who signs off on tier decisions normally, and I trusted his read given how long he's been doing this.

Interviewer: What happened next?

Participant: About ninety minutes later the gauges spiked hard — much faster than the operator's language had implied. The release turned out to be a lot bigger than "controlled precautionary" suggested. That's when things started moving fast.

Interviewer: Let's talk about the resource request that followed. What was happening at that point?

Participant: Our field liaison started getting scattered water-rescue calls, but only in two sub-neighborhoods — small numbers, really consistent with a standard tier-1 response. At the same time I was hearing fire dispatch chatter using radio codes that sounded almost identical to what we used during the 2018 flash flood two counties over, the one with multiple fatalities. I'd helped coordinate the tier-3 mobilization on that one.

Interviewer: How did that connection affect your recommendation?

Participant: Honestly, it hit me pretty hard. I remember thinking, this feels like 2018 again, and I didn't want to be caught understaffed like we almost were back then. So I recommended a full tier-3 mobilization — extra swift-water teams, extra staging — even though the actual call volume we had in front of us was only tier-1 level.

Interviewer: Did the current data support tier-3 on its own?

Participant: Not really, no. If you just looked at the confirmed calls, tier-1 would've covered it. But that memory was loud in my head.

Interviewer: What ended up happening with those resources?

Participant: The rescue calls plateaued at basically tier-1 volume. So we had tier-3 assets sitting partly idle for a few hours, which the fire branch wasn't thrilled about since they needed some of that same equipment.

Interviewer: Let's move to the evacuation zone decision. What information did you have at that stage?

Participant: This was the rough part. Six of our eight stream gauges were down — the repeater got knocked out by Ridge Fire smoke interference — so I only had two gauges reporting, and both were showing a sharp rise over about twenty minutes. Around the same time, videos of flooding at one intersection started circulating on social media and a regional news account picked it up and ran with it.

Interviewer: How did you put that together into a recommendation?

Participant: I built out a flood-extent map using the two gauges plus that footage, and honestly, it all fit together really cleanly — the trend line, the video, the timing. It told a clear, coherent story, and I felt confident recommending we expand the evacuation to the whole multi-sector watershed area rather than just the sub-zones next to those two gauges.

Interviewer: Did you weigh how much of the watershed those two gauges actually represented?

Participant: I mean, two out of eight isn't the full picture, but they were both moving in the same direction, so I took that as a strong enough signal for the whole area. Getting people out ahead of a flood is better than being late, so I leaned toward the wider expansion.

Interviewer: What came out of that afterward?

Participant: Once the backup gauges came back online later that night, it turned out two of the newly evacuated sub-zones never actually exceeded minor flood stage. So the expansion was broader than what materialized, though obviously nobody could've known that for certain in the moment.

Interviewer: Let's go to the hot-wash review. What was discussed there?

Participant: We went back over the original advisory decision — the one from the start of the night — now that we knew how bad it actually got. Reading the operator's notice again, with everything we now know, it seemed like the signs were pretty clearly there. The scale of what happened felt like it should have been obvious from that notice alone.

Interviewer: When you say "obvious," obvious based on what was known that night, or knowing how it turned out?

Participant: Looking back at it now, it just reads differently. Knowing what happened after, the wording in that notice looks like it was underselling things pretty clearly.

Interviewer: If the operator's notice had used different language that night — less "controlled," more urgent — do you think your initial recommendation would have changed?

Participant: Probably, yeah. If it had said something like "emergency release" instead of "precautionary," I think I'd have pushed harder for a warning tier instead of an advisory, regardless of what the Director's initial read was.

Interviewer: And if all eight gauges had stayed online through the evacuation decision, would that have changed things?

Participant: I'd like to think I'd have waited for a fuller picture instead of leaning as hard on those two data points and the footage. With full coverage I probably wouldn't have needed the video to fill in the gaps at all.

Interviewer: Looking back across the whole night, how do you separate what you actually knew in the moment from what became clear afterward?

Participant: It's harder than it sounds. In the moment you're working with partial data and you're making the best call you can with what's in front of you. It's only once you have the full outcome that certain things start looking like they should have been flagged earlier — but I try to remind myself that clarity came from hindsight, not from anything I necessarily missed in real time.

Interviewer: That's a good place to stop. Thanks for walking through this in detail.

Participant: Sure, happy to help however this gets used.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Illusion of Validity", "occurrences": 1, "mechanism_constraint": "Confidence must derive from narrative coherence of a thin-evidence flood map, not from accurate calibration."},
      {"bias": "Insensitivity to sample size", "occurrences": 1, "mechanism_constraint": "Must involve extrapolation from 2-of-8 gauges to a broader watershed conclusion."},
      {"bias": "Authority Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to deference based on the Branch Director's seniority/title, not independent verification."},
      {"bias": "Availability Bias", "occurrences": 2, "mechanism_constraint": "Each instance must use a distinct evidence source: (1) personal institutional memory of a past event, (2) vivid circulated media footage."},
      {"bias": "Framing Effect", "occurrences": 1, "mechanism_constraint": "Must be tied to the dam operator's specific wording ('controlled precautionary release') shaping the tier decision."},
      {"bias": "Hindsight bias", "occurrences": 1, "mechanism_constraint": "Must occur only in the Phase 4 retrospective hot-wash review, using outcome knowledge to judge foreseeability."}
    ],
    "target_bias_names": [
      "Illusion of Validity",
      "Insensitivity to sample size",
      "Authority Bias",
      "Availability Bias",
      "Framing Effect",
      "Hindsight bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Illusion of Validity", "requested_occurrences": 1},
      {"bias": "Insensitivity to sample size", "requested_occurrences": 1},
      {"bias": "Authority Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 2},
      {"bias": "Framing Effect", "requested_occurrences": 1},
      {"bias": "Hindsight bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Framing Effect"},
      {"instance_id": "cb_02", "bias": "Authority Bias"},
      {"instance_id": "cb_03", "bias": "Availability Bias"},
      {"instance_id": "cb_04", "bias": "Insensitivity to sample size"},
      {"instance_id": "cb_05", "bias": "Availability Bias"},
      {"instance_id": "cb_06", "bias": "Illusion of Validity"},
      {"instance_id": "cb_07", "bias": "Hindsight bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Framing Effect", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Authority Bias", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Availability Bias", "decision_point": 2},
      {"instance_id": "cb_04", "bias": "Insensitivity to sample size", "decision_point": 3},
      {"instance_id": "cb_05", "bias": "Availability Bias", "decision_point": 3},
      {"instance_id": "cb_06", "bias": "Illusion of Validity", "decision_point": 3},
      {"instance_id": "cb_07", "bias": "Hindsight bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Framing Effect",
        "mechanism": "Threat-tier choice driven by the dam operator's positively-valenced wording rather than gauge trend analysis.",
        "affected_reasoning_operation": "Threat-tier classification",
        "evidence_source": "Dam operator release notice text",
        "distinctiveness_requirement": "Sole instance of Framing Effect; must not overlap with cb_02's authority-based mechanism even though co-located at decision point 1."
      },
      {
        "instance_id": "cb_02",
        "bias": "Authority Bias",
        "mechanism": "Deference to Branch Director's seniority/title in lieu of independent verification.",
        "affected_reasoning_operation": "Evidence weighting / authorization deference",
        "evidence_source": "Branch Director's verbal assurance",
        "distinctiveness_requirement": "Sole instance of Authority Bias; distinguished from cb_01 by relying on person-based credibility rather than message wording."
      },
      {
        "instance_id": "cb_03",
        "bias": "Availability Bias",
        "mechanism": "Resource sizing driven by vivid recall of the 2018 mass-casualty event triggered by superficial radio-code similarity.",
        "affected_reasoning_operation": "Resource-need estimation",
        "evidence_source": "Analyst's personal/institutional memory of a prior incident",
        "distinctiveness_requirement": "First of two Availability Bias instances; uses internally-recalled past-event memory as evidence source, distinct from cb_05's externally-sourced media footage."
      },
      {
        "instance_id": "cb_04",
        "bias": "Insensitivity to sample size",
        "mechanism": "Treating a 2-of-8 gauge sample as sufficient basis for a watershed-wide conclusion.",
        "affected_reasoning_operation": "Statistical/spatial extrapolation",
        "evidence_source": "Two functioning stream gauges out of eight",
        "distinctiveness_requirement": "Sole instance; distinguished from cb_06 (illusion of validity) by focusing on sample-size neglect rather than overall narrative-coherence confidence."
      },
      {
        "instance_id": "cb_05",
        "bias": "Availability Bias",
        "mechanism": "Perceived severity/scope inflated by vivid, widely circulated social-media footage of one flooded location.",
        "affected_reasoning_operation": "Severity/scope estimation",
        "evidence_source": "Viral social-media/news footage",
        "distinctiveness_requirement": "Second of two Availability Bias instances; uses externally-sourced viral media as evidence, distinct from cb_03's internally-recalled memory, and occurs at a different decision point."
      },
      {
        "instance_id": "cb_06",
        "bias": "Illusion of Validity",
        "mechanism": "High subjective confidence attributed to the internal coherence of the flood-extent map rather than its actual evidentiary reliability.",
        "affected_reasoning_operation": "Confidence calibration in predictive model",
        "evidence_source": "Self-assembled flood-extent map from gauges and footage",
        "distinctiveness_requirement": "Sole instance; distinguished from cb_04 by addressing confidence/coherence rather than sample-size neglect per se."
      },
      {
        "instance_id": "cb_07",
        "bias": "Hindsight bias",
        "mechanism": "Retrospective claim that the escalation was 'obvious' from Phase 1 information, using now-known outcome to judge past foreseeability.",
        "affected_reasoning_operation": "Retrospective causal attribution",
        "evidence_source": "Re-read of original dam notice combined with full outcome knowledge",
        "distinctiveness_requirement": "Sole instance; confined strictly to the Phase 4 retrospective decision point, must not appear in earlier decision points or closing hypotheticals."
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Framing Effect", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Authority Bias", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Availability Bias", "strength": "moderate"},
      {"instance_id": "cb_04", "bias": "Insensitivity to sample size", "strength": "moderate"},
      {"instance_id": "cb_05", "bias": "Availability Bias", "strength": "subtle"},
      {"instance_id": "cb_06", "bias": "Illusion of Validity", "strength": "moderate"},
      {"instance_id": "cb_07", "bias": "Hindsight bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Biased_7",
    "domain_id": "EM",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across 4 decision points by mechanism fit and narrative realism: decision point 1 hosts framing/authority (message-framing and hierarchical trust both operate on the same initial classification act via different evidentiary channels); decision point 2 hosts one availability instance tied to internally recalled memory; decision point 3 hosts sample-size neglect, the second availability instance (externally-sourced media), and illusion of validity (confidence in the resulting synthesis), each addressing a distinct reasoning operation on distinct evidence; decision point 4 hosts hindsight bias exclusively, isolated to the retrospective review act. No bias exceeds two occurrences at any single decision point, and the two Availability Bias instances use fully independent evidence sources and occur at different decision points per the distinctiveness rule.",
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
