You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the border-sector traffic assessment from last month, purely for how you approached the analysis. Nothing here goes in your file.

Participant: Sure, no problem. That one's still fresh anyway.

Interviewer: Good. Can you give me your role in the fusion cell and what your objective was that day?

Participant: I'm the SIGINT desk analyst for that regional cell. My job that day was to turn a raw traffic spike into a confidence-graded assessment for the fusion cell lead—basically, tell him whether what we were seeing near the Sector 7 logistics hub was something operational or just noise.

Interviewer: Take me through the incident from the top.

Participant: Around 0700 the automated system flagged a jump in encrypted burst traffic near the Sector 7 hub—well above baseline, and Sector 7 is normally quiet outside scheduled rotations. About the same time, Sector 4 showed a smaller bump too, but that's a different area entirely, no obvious connection. I had a hard deadline: the lead wanted a briefing in six hours. My linguists were already sitting on an eight-hour backlog from other tasking, so I knew from the jump I wasn't going to get everything translated.

Interviewer: What did you know before you made any calls?

Participant: Just the signal signature data—volume, timing, burst patterns—and the historical baseline for both sectors. No content yet. Sector 7's hub has strategic weight, it's tied to a known logistics node in the order of battle, so a spike there gets attention regardless. Sector 4's pattern was actually less typical, statistically, but there was no obvious link to anything sensitive.

Interviewer: So what did you do with your linguist hours?

Participant: I pushed almost all three available hours to Sector 7 and queued Sector 4 for later. The alternative was splitting time evenly, or even flipping it and doing Sector 4 first because its pattern was more unusual. But given the deadline, I couldn't do both properly, and Sector 7's hub mattered more if something real was happening there.

Interviewer: What came back from that first batch of translation?

Participant: A mix. Some convoy-movement language, some resupply terms, and two coded phrases that weren't in our standard glossary. Also some fairly mundane rotation talk. It wasn't clean either way.

Interviewer: How did you interpret that mix?

Participant: I started drafting a working note. My instinct was that convoy references plus burst traffic plus unexplained code phrases fit a pattern I'd want to flag—an emerging logistics buildup ahead of some posture change. I laid it out step by step: the signal surge, then the convoy chatter, then the coded terms as probable concealment for something they didn't want plain-language. Writing it out that way, it held together. It read like a coherent sequence, and honestly, once I had it typed up in that form, I felt more confident it was the right read than when I'd started.

Interviewer: Was there anything at that point that argued the other way?

Participant: The exercise calendar showed a rotation window that plausibly overlapped, and no imagery corroboration had come in yet. I noted the rotation possibility in the draft, but I led with the buildup framing because it explained more of the pieces at once—the convoy talk, the burst pattern, and the coded phrases all fit under one story, whereas the rotation explanation left the coded phrases dangling.

Interviewer: Did anything come in afterward that touched that account?

Participant: Yes—a later intercept had maintenance-cycle terminology in it, which cuts somewhat against the buildup idea. And one of those two coded phrases turned out to be in a maintenance-schedule glossary, not anything to do with offensive posture. That came in after I'd already built the note around the buildup framing.

Interviewer: Let's move to sourcing. You had two corroborating options—walk me through that.

Participant: Right, I had an open-source digest, well-written, clearly formatted, forecasting regional tension in a way that lined up with what I already had drafted. And I had an IMINT report on vehicle dispersal at the hub—more directly relevant to the actual location, but dense, heavy on sensor jargon, and I only had time to fully absorb one of them before the deadline. The IMINT analyst wasn't reachable for a quick walk-through either.

Interviewer: What tipped it toward the digest?

Participant: Time, mostly. The digest was quick to read and slotted right into the write-up I already had going—it reinforced the framing without extra work parsing sensor terminology I'd have needed help interpreting anyway. It read so cleanly and confidently that its regional forecast felt like it applied straight to Sector 7, more than I could really back up just from what was on the page. The IMINT report would've taken longer to properly digest and I wasn't fully confident I was reading the dispersal imagery correctly on my own.

Interviewer: Did you consider weighting them evenly, or leaning on IMINT instead?

Participant: I considered it. IMINT is sensor-based and specific to that hub, so on paper it's the stronger source. But given the time I had, citing the source I could actually process well and confidently seemed like the more responsible choice than citing something I might misread under pressure.

Interviewer: What did you learn about those sources afterward?

Participant: After the briefing, going back through the IMINT report more carefully, the dispersal pattern was actually just as consistent with a maintenance stand-down as with a buildup. And the digest, it turned out, was drawing on general regional reporting that didn't specifically tie back to Sector 7 at all.

Interviewer: Now the final call—how did you land on your confidence level for the briefing?

Participant: I had twenty minutes before I had to walk in. I had a buildup narrative, partial open-source support, and this unresolved contradiction with the maintenance terminology. I considered going high confidence, but the contradiction made that feel wrong. Low confidence felt like it undersold the pattern I was seeing. So I went moderate—buildup assessment, explicitly flagged the maintenance-terminology contradiction, and recommended a follow-up collection tasking to resolve it.

Interviewer: How did the lead respond?

Participant: He took the moderate framing at face value and tasked the follow-up collection, which was really the right outcome regardless of which way the underlying truth eventually goes.

Interviewer: And has that follow-up traffic settled it either way?

Participant: Not really. Two days on, the new traffic is still genuinely mixed. It hasn't confirmed the buildup and it hasn't ruled it out either.

Interviewer: If you'd had one more linguist-hour before the briefing, what would you have done differently?

Participant: Probably gone back to that second coded phrase earlier rather than letting it sit unresolved in the draft. It might have surfaced the maintenance angle sooner.

Interviewer: If the IMINT report had been your only corroborating option, how do you think your assessment would have looked?

Participant: Honestly, I think I'd have spent more time forcing myself through the sensor detail, and the ambiguity in the dispersal pattern might have shown up in my write-up earlier instead of after the fact. I might have hedged more going into the briefing.

Interviewer: Looking back, is there a point in this you'd want to revisit?

Participant: Probably the moment I locked in the buildup framing in the working note. It wasn't wrong to consider it, but I built it out pretty fully before I'd seen the maintenance-terminology intercept, and once it was written that clearly, it was hard to hold as loosely as I probably should have.

Interviewer: That's helpful. I think that covers everything I need.

Participant: Glad to walk through it.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Explanation bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as confidence increase from narrative construction itself, not from new evidence"
      },
      {
        "bias": "Fluency effects",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as source preference driven by ease of reading/processing rather than sourcing strength or relevance"
      }
    ],
    "target_bias_names": [
      "Explanation bias",
      "Fluency effects"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Explanation bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Fluency effects",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias"
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias",
        "decision_point": 2
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias",
        "mechanism": "Constructing a coherent, detailed causal narrative from partial intercepts increases the analyst's confidence in that narrative, independent of new supporting evidence",
        "affected_reasoning_operation": "Hypothesis generation and confidence calibration",
        "evidence_source": "Partial translated intercepts (rotation terminology plus two unclear coded phrases) and overlapping exercise calendar",
        "distinctiveness_requirement": "Distinct from fe_01 in decision point, evidence type (intercept translation vs. open-source/IMINT corroboration), and reasoning operation (narrative construction vs. source selection)"
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects",
        "mechanism": "Ease of reading the open-source digest is mistaken for a proxy of its reliability or relevance relative to the denser IMINT report",
        "affected_reasoning_operation": "Source selection and evidentiary weighting for corroboration",
        "evidence_source": "Open-source news digest versus dense IMINT vehicle-dispersal report",
        "distinctiveness_requirement": "Distinct from eb_01 in decision point, evidence type, and reasoning operation (source weighting vs. narrative generation)"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias",
        "strength": "subtle"
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects",
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
    "scenario_id": "IA_Biased_2",
    "domain_id": "IA",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias assigned to a distinct decision point (explanation bias at decision point 2, fluency effects at decision point 3) selected for mechanism fit: explanation bias fits the narrative-construction moment after partial translation, fluency effects fits the corroborating-source selection moment; decision points 1 and 4 were kept free of intended bias instances to preserve narrative realism and avoid over-concentration.",
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
