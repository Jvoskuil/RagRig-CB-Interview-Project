You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. As a reminder, this session is for the after-action cognitive review, not for attribution of blame—I just want to understand how decisions actually got made. That okay with you?

Participant: Yeah, that's fine. I've done these before.

Interviewer: Good. Can you start by giving me your role and what the mission was?

Participant: I'm the battalion S3 for the task force. Our mission was to secure and hold the Route BLUE crossing so brigade could push their main effort across within a 48-hour window. We had one Mobile Gap-Crossing Bridge, limited float capacity, and weather was closing in on our aerial ISR window. It mattered because if we didn't hold that crossing on schedule, brigade's whole synchronization plan slid.

Interviewer: Walk me through how the incident actually unfolded, start to finish.

Participant: Sure. About 48 hours out, S2 flagged enemy scout vehicles in a spot that didn't quite match what we'd been seeing—three months of pattern-of-life had them screening consistently off ridge NAI 12, and this sighting was lower, closer to the river. The vehicle types and rough timing matched what we'd tracked before, so it read to me like the same defensive template, and I didn't put much weight on the location itself. S2 actually noted that the river-side position wasn't really consistent with how that unit normally screened, but I still treated it as a variant of the pattern we knew rather than something that needed a second look. So we didn't request additional ISR retasking, we just kept the reconnaissance-in-force plan as built.

About six hours after that, brigade S3 called and directed us to continue on Axis BLUE per the original order, citing the synchronization requirement. At that point our engineer had already flagged a preliminary concern about the bridge's load capacity, but it wasn't a hard number yet—no full classification. I mentioned it to brigade informally but didn't push hard. If I'm honest, I thought the concern was enough to justify at least asking for a short pause to get the classification confirmed, but once brigade framed continuation as a synchronization requirement, raising that again felt like second-guessing a decision that had already been made.

Then closer to execution, the engineer came back with an actual classification report suggesting overweight risk for our heaviest vehicles. We had a planning session that same day. The plan was already rehearsed, already briefed up to brigade. The report got raised, a couple people nodded at it, but the discussion moved straight to what the plan already had going for it rather than to whether the risk itself changed anything, and nobody proposed rerouting. The session wrapped with everyone agreeing to keep the existing crossing plan.

Execution day, we had a partial bridge failure under one of the heavier platforms, and almost simultaneously took contact from dismounts near the crossing site. We ran the branch plan, secured the site, and finished the crossing over the alternate ford instead.

Interviewer: Let's slow down and rebuild that timeline with the information you had at each point, not what you know now.

Participant: Fair. At H-48, all I had was the scout sighting and the historical pattern. No confirmation either way on intent. At H-30 or so, I had brigade's directive plus an informal, unconfirmed engineer concern. At H-24, I had a real classification number and a rehearsed plan already in brigade's hands. At H-hour, I had the failure and the contact simultaneously.

Interviewer: Take me back to that first sighting. What made you read it as consistent with the known template rather than as something new?

Participant: The vehicle types matched, the timing matched roughly what we'd seen before, and three months of consistent behavior is a strong baseline. Even with S2 pointing out the location was a little off for that unit's normal screening, it still looked and moved like the same picture we'd been tracking, so I didn't treat the position as something that changed the category. If I chased every deviation with an ISR request, given how constrained our collection was, we'd never finalize anything.

Interviewer: Did you consider requesting retasking anyway, just to confirm?

Participant: S2 raised it as an option. I didn't prioritize it because the weather window for aerial support was closing and I didn't think the deviation was significant enough to justify pulling that asset off other priorities.

Interviewer: When the ground patrol later reported dismounts moving toward the crossing itself rather than the ridge, how did that land?

Participant: That's when S2 flagged it as worth another look. But we were already committed to the recon plan by then, so it didn't change what we'd built.

Interviewer: Move to brigade's call directing continuation on Axis BLUE. What alternatives did you weigh?

Participant: I could have pushed back and asked for a short delay to firm up the bridge picture or scout the alternate ford. Or I could comply and keep the timeline. I went with compliance.

Interviewer: What drove that choice specifically?

Participant: Brigade had already made the call, and it came with the synchronization argument attached. Honestly, the informal concern was probably enough on its own to justify asking for a short hold pending classification, but by the time brigade framed it as a fixed requirement, pushing that same point again felt like challenging a decision that was already settled above me. It felt like brigade owned that risk calculus at that point more than I did.

Interviewer: Did you get any pushback or written response from brigade on the bridge issue?

Participant: No, not before we committed.

Interviewer: Let's go to the planning session where the classification report came in. How did that discussion actually go?

Participant: It was quick. The engineer laid out the overweight risk, a couple of people acknowledged it, and then the conversation moved on to why the current plan was already solid rather than to what the new number actually meant for it. Nobody put a reroute on the table. We closed with agreement to keep the plan.

Interviewer: What was the reasoning for keeping the plan rather than shifting to the alternate ford?

Participant: Once the classification came in, the room still leaned on the fact that the plan was rehearsed and already briefed to brigade more than it leaned on the number itself. Rerouting would have meant reconning an unfamiliar ford in current water conditions, in daylight, with no rehearsal, and we didn't really stop to weigh a partial fix, like resequencing the heavier vehicles, against just keeping what we had.

Interviewer: Did anyone in the room actually voice disagreement with keeping the plan?

Participant: Not in the room, no. I found out afterward that one of the company commanders had reservations about the bridge but didn't say anything during the session.

Interviewer: Did he ever say why he stayed quiet?

Participant: He told me later that by the time the report came up, the room had already settled on keeping the plan, and he didn't want to be the one to reopen something that had already gone up to brigade.

Interviewer: Now the crossing itself. What would have changed your decision to keep the original plan, looking back at what you knew before execution?

Participant: A hard confirmed number earlier, or if someone had actually put the alternate ford proposal on the table instead of just the report sitting there. If we'd had even a day more, I think we'd have reconned the ford as a real branch option instead of a theoretical one.

Interviewer: How do you assess the scout sighting now, knowing what happened at the crossing?

Participant: Looking back, I think we should have caught more from that first report than we did. The river-side location was there in the original reporting, and given how it lines up with the patrol and the contact, we probably should have recognized the implication right then instead of waiting for later confirmation.

Interviewer: Last one—if the alternate ford had been reconned earlier, do you think the planning session goes differently?

Participant: Probably. If it had been a real, validated option sitting next to the bridge option, I think the report would have gotten more than a nod. As it stood, it was theoretical, so keeping the rehearsed plan felt like the lower-risk path in the room that day.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Authority Bias or Higher-level prioritization Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Hindsight Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Representativeness Heuristic",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Status Quo Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Groupthink",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Authority Bias or Higher-level prioritization Bias",
      "Hindsight Bias",
      "Representativeness Heuristic",
      "Status Quo Bias",
      "Groupthink"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Authority Bias or Higher-level prioritization Bias", "requested_occurrences": 1 },
      { "bias": "Hindsight Bias", "requested_occurrences": 1 },
      { "bias": "Representativeness Heuristic", "requested_occurrences": 1 },
      { "bias": "Status Quo Bias", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "MD5_b01", "bias": "Representativeness Heuristic" },
      { "instance_id": "MD5_b02", "bias": "Authority Bias or Higher-level prioritization Bias" },
      { "instance_id": "MD5_b03", "bias": "Groupthink" },
      { "instance_id": "MD5_b04", "bias": "Status Quo Bias" },
      { "instance_id": "MD5_b05", "bias": "Hindsight Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "MD5_b01", "bias": "Representativeness Heuristic", "decision_point": 1 },
      { "instance_id": "MD5_b02", "bias": "Authority Bias or Higher-level prioritization Bias", "decision_point": 2 },
      { "instance_id": "MD5_b03", "bias": "Groupthink", "decision_point": 3 },
      { "instance_id": "MD5_b04", "bias": "Status Quo Bias", "decision_point": 3 },
      { "instance_id": "MD5_b05", "bias": "Hindsight Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MD5_b01",
        "bias": "Representativeness Heuristic",
        "mechanism": "Classifying an atypical scout sighting as a normal variant of a familiar enemy template rather than weighing the specific deviation.",
        "affected_reasoning_operation": "Categorization of new evidence against prior template",
        "evidence_source": "S2 scout-sighting report vs. historical pattern-of-life data",
        "distinctiveness_requirement": "Occurs at DP1, involves categorical pattern-matching, distinct from all other instances by evidence type (intel pattern data) and reasoning operation (categorization, not deference or default preference)."
      },
      {
        "instance_id": "MD5_b02",
        "bias": "Authority Bias or Higher-level prioritization Bias",
        "mechanism": "Deferring to brigade's directive to continue the axis primarily because of its source (higher headquarters) rather than independent risk-weighing.",
        "affected_reasoning_operation": "Source-weighted compliance judgment overriding unresolved technical risk",
        "evidence_source": "Brigade S3 verbal directive vs. battalion engineer's informal risk flag",
        "distinctiveness_requirement": "Occurs at DP2, involves deference to hierarchical authority, distinct from DP1 (no external directive involved) and DP3 (no group consensus dynamic)."
      },
      {
        "instance_id": "MD5_b03",
        "bias": "Groupthink",
        "mechanism": "Rapid, unchallenged staff convergence on retaining the plan despite a company commander's private, unvoiced reservations.",
        "affected_reasoning_operation": "Suppressed dissent during collective evaluation",
        "evidence_source": "Staff session dynamics and company commander's private post-session comment",
        "distinctiveness_requirement": "Shares DP3 with MD5_b04 but is distinguished by focusing on group dissent suppression (social/interpersonal evidence: unvoiced commander reservation) rather than the plan-retention rationale itself."
      },
      {
        "instance_id": "MD5_b04",
        "bias": "Status Quo Bias",
        "mechanism": "Choosing to retain the original bridge crossing plan because it was already rehearsed and briefed, rather than because the risk evidence favored it.",
        "affected_reasoning_operation": "Default-anchored selection between two crossing options",
        "evidence_source": "Engineer bridge classification report vs. sunk investment in the rehearsed/briefed plan",
        "distinctiveness_requirement": "Shares DP3 with MD5_b03 but is distinguished by evidence source (rehearsal/briefing investment and risk-data comparison) rather than group dynamics; reflects individual/staff preference for the incumbent option, not suppressed dissent."
      },
      {
        "instance_id": "MD5_b05",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively describing the earlier scout sighting as an obvious, foreseeable warning of the ambush, overstating predictability relative to the real-time uncertainty documented earlier.",
        "affected_reasoning_operation": "Retrospective reconstruction of foreseeability",
        "evidence_source": "After-action consolidated timeline vs. S3's own earlier (DP1) account of ambiguity",
        "distinctiveness_requirement": "Occurs at DP4 during post-outcome reflection only; distinct from MD5_b01 because it concerns retrospective judgment of foreseeability, not real-time categorization."
      }
    ],
    "intended_strength": [
      { "instance_id": "MD5_b01", "bias": "Representativeness Heuristic", "strength": "subtle" },
      { "instance_id": "MD5_b02", "bias": "Authority Bias or Higher-level prioritization Bias", "strength": "moderate" },
      { "instance_id": "MD5_b03", "bias": "Groupthink", "strength": "moderate" },
      { "instance_id": "MD5_b04", "bias": "Status Quo Bias", "strength": "moderate" },
      { "instance_id": "MD5_b05", "bias": "Hindsight Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Biased_5",
    "domain_id": "MD",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Instances distributed across 4 decision points per mechanism fit and narrative realism: DP1 (Representativeness Heuristic - intel categorization), DP2 (Authority Bias - directive compliance), DP3 (Groupthink and Status Quo Bias - two distinct biases co-located with separated evidence sources: dissent suppression vs. rehearsal-anchored plan retention), DP4 (Hindsight Bias - post-outcome reflection). No single bias exceeds one occurrence per decision point; co-located DP3 instances differ in evidence source and reasoning operation per Instance Independence Rule.",
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
