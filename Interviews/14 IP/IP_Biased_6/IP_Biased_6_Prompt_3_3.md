You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on how you handled scheduling decisions during that disruption a few weeks back — Press 3 and the coil-steel delay. Nothing you say here affects performance review, I just want to understand how you actually worked through it. Sound okay?

Participant: Sure, happy to walk through it. It was a fairly full week.

Interviewer: Can you start by telling me who you are and what your role was during this incident?

Participant: I'm the PPC analyst for the stamping shop — I own the rolling five-day schedule across Press 1, 2, and 3, and I coordinate with the three downstream assembly plants that pull from us. That week my job was basically to keep the master schedule intact despite two things going sideways at once.

Interviewer: Let's get the full account first, then we'll go back through it in detail. What happened?

Participant: It started Monday morning. We had a weekend demand surge from one of the assembly plants — they needed an extra batch of the high-volume bracket variant, and Press 3 is the only press currently tooled for that part. I pulled up last week's throughput report and Press 3 had actually run above target, so capacity-wise it looked like the obvious answer. Before I locked anything in, I did get a short heads-up line from the scheduling assistant saying Press 3 had an open vibration advisory — not the full CMMS entry, just a flag. It read as low-priority, and set against how strong the throughput numbers were, it didn't seem like something that should change the call. So I allocated the full extra batch to Press 3.

Then Tuesday, our coil-steel supplier called in a four-day delay. Their rep mentioned "internal allocation constraints," which didn't mean much to me at the time. I've dealt with this supplier for a while — they've had two delays before, both around late December and late June, and both times it sorted itself out within a week without us needing backup stock. Their delays always seem to cluster around certain stretches for them, so I read the timing itself as the real signal — the "internal allocation constraints" line sounded like their usual wording, not something new. So I figured this would follow the same pattern. I did reach out to our backup supplier contact just to have something in reserve, but honestly I called the first person on my list rather than shopping around — we were already stretched that day.

By Thursday, the reliability engineer sent an update saying Press 3's vibration had ticked up slightly since the weekend run. There's a full trend log you can pull that shows three weeks of data, but I didn't open it. Partly because things were moving fast, partly because the number itself wasn't dramatic — nothing like the Press 1 incident a couple years back, which is the kind of thing that jumps to mind when I think "serious press problem." This felt more like background noise.

Then Friday morning, right before I finalized the week's schedule, engineering upgraded Press 3 from "monitor" to "elevated concern." When I asked what that actually meant, the engineer said it reflected a real increase in loading risk, not just a status update on paper. At that point the schedule was basically locked — downstream plants already had confirmation — and shifting the remaining volume to Press 1 would have meant a partial changeover costing several hours. I trimmed Friday's Press 3 run a bit but kept the plan mostly as it was.

Interviewer: Let's reconstruct that timeline a bit more precisely. What did you actually have in front of you Monday morning, before you made the allocation call?

Participant: The throughput report from the prior week, the demand surge notice from the assembly plant, the fact that Press 3 was the only tooled option, and that brief note flagging the vibration advisory. The full CMMS detail wasn't something I pulled up — I just had the short flag.

Interviewer: And the vibration advisory — how did that information reach you in more detail?

Participant: The maintenance tech mentioned more of it in passing, after the allocation was already set, saying there'd be a follow-up inspection recommended within two weeks. It wasn't presented as urgent even then.

Interviewer: When did you first hear about the supplier delay, and what was your first reaction?

Participant: Tuesday, from their account rep directly. My first thought was, "this looks like the same thing that happened in December and June."

Interviewer: Let's go back to the Monday allocation decision. What alternatives did you actually weigh?

Participant: I considered splitting the batch — running part on a temporarily retooled Press 1 and a reduced run on Press 3 — or pushing part of the order to the following week. But the changeover cost and the tight timeline made Press 3 alone the cleanest option.

Interviewer: What made the throughput report feel like the deciding piece of evidence, given you also had that vibration flag?

Participant: It was recent, it was concrete, and it directly answered the question I was asking — can Press 3 handle more volume. The flag was there, but it was low-priority and vague next to a full week of solid output numbers, so the throughput report just carried more weight for me.

Interviewer: On the supplier delay — walk me through the reasoning that led you to wait rather than order backup stock right away.

Participant: The pattern matched what I'd seen twice before with this supplier, so I expected a similar resolution — to me the timing itself was the tell, more than anything they actually said. Their rep's line about "internal allocation constraints" sounded like the kind of thing they always say around these stretches, so it didn't register as pointing to anything different this time.

Interviewer: And the choice of backup contact — what determined which supplier you called?

Participant: Honestly, it's the one I already had a relationship with. I didn't compare lead times or pricing against other options that morning — there wasn't a clean window to do that kind of comparison shopping with everything else going on.

Interviewer: Thursday's vibration note — what determined whether you pulled the full trend log? Do you think opening it would have changed what you had to do that day?

Participant: I had the update in front of me, and I made a call not to dig further right then. If I'm honest, part of it was that pulling three weeks of data might have shown a clearer upward line than a single number did, and that could have meant reworking Friday's plan on top of everything else already moving. The bi-weekly review was close enough that it felt fine to let it sit until then.

Interviewer: What situation were you picturing when you assessed how serious it might be?

Participant: If I'm honest, I was thinking of the Press 1 fire from a couple years ago — that's the reference point that comes to mind when someone says "press failure." This didn't look anything like that, so it didn't register as urgent.

Interviewer: Friday, when the status moved to "elevated concern" — how did you weigh that against the schedule you'd already committed to?

Participant: At that point we were locked in with the downstream plants, and a full reallocation meant hours of changeover we didn't have room for. Even with the engineer telling me it reflected a real risk increase, the earlier data — the throughput numbers, the clean weekend run — still felt like the more solid read on how Press 3 actually performs, so I didn't weight the new label as heavily as what I already had. I trimmed the Friday run slightly rather than overhauling the plan.

Interviewer: What would have had to be different in that assessment for you to change the schedule more substantially?

Participant: Probably if the language had been stronger — something like an explicit downtime risk instead of "elevated concern" — or if it had come earlier in the week when I had more room to maneuver.

Interviewer: What actually happened with Press 3 and the shipments that week?

Participant: Press 3 finished the week without failing. The reliability engineer did file a formal recommendation to reduce loading next cycle. Shipments went out on time to all three plants.

Interviewer: If that Monday flag had appeared directly inside your scheduling dashboard instead of arriving as a separate message from the scheduling assistant, do you think the allocation decision would have gone differently?

Participant: Possibly. If it had been sitting right there next to the throughput numbers instead of coming in as a separate note, I think I'd have paused longer on it instead of leaning mainly on the report.

Interviewer: If you'd had unlimited time that week, is there anything you'd have checked differently?

Participant: I'd have pulled the full trend log Thursday instead of going off the single update, and I probably would have called around to compare backup suppliers instead of just going with who I knew.

Interviewer: Last one — looking back, what's one thing about how information reached you that you'd want changed?

Participant: Honestly, just having the maintenance advisories show up in full where I'm already doing my scheduling. Right now I mostly get a quick flag and have to go looking for the rest, and that week, I didn't.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as selective weighting of confirming throughput evidence over disconfirming advisory evidence at decision point 1."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as satisficing/time-constrained alternative selection at decision point 2, distinct from the correlation-bias instance at the same decision point."
      },
      {
        "bias": "Correlation bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as causal misattribution based on superficial temporal pattern-matching to prior unrelated delays, at decision point 2."
      },
      {
        "bias": "Conservatism Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as underweighting new elevated-concern evidence relative to a previously formed belief, at decision point 4."
      },
      {
        "bias": "Imaginability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as risk judgment anchored on ease of recalling a vivid past incident rather than the actual gradual trend data, at decision point 3."
      },
      {
        "bias": "Ostrich effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as avoidance of requesting/reviewing available risk-relevant information (full vibration trend log), at decision point 3, distinct evidence source from the imaginability-bias instance."
      }
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Bounded Rationality",
      "Correlation bias",
      "Conservatism Bias",
      "Imaginability Bias",
      "Ostrich effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confirmation Bias", "requested_occurrences": 1 },
      { "bias": "Bounded Rationality", "requested_occurrences": 1 },
      { "bias": "Correlation bias", "requested_occurrences": 1 },
      { "bias": "Conservatism Bias", "requested_occurrences": 1 },
      { "bias": "Imaginability Bias", "requested_occurrences": 1 },
      { "bias": "Ostrich effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias" },
      { "instance_id": "br_01", "bias": "Bounded Rationality" },
      { "instance_id": "co_01", "bias": "Correlation bias" },
      { "instance_id": "cv_01", "bias": "Conservatism Bias" },
      { "instance_id": "im_01", "bias": "Imaginability Bias" },
      { "instance_id": "oe_01", "bias": "Ostrich effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1 },
      { "instance_id": "co_01", "bias": "Correlation bias", "decision_point": 2 },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 2 },
      { "instance_id": "oe_01", "bias": "Ostrich effect", "decision_point": 3 },
      { "instance_id": "im_01", "bias": "Imaginability Bias", "decision_point": 3 },
      { "instance_id": "cv_01", "bias": "Conservatism Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective weighting of confirming throughput data over disconfirming vibration advisory during capacity allocation",
        "affected_reasoning_operation": "Evidence selection and weighting",
        "evidence_source": "Weekly throughput report vs. CMMS vibration advisory",
        "distinctiveness_requirement": "Unique in involving allocation-stage evidence weighting; not repeated at any other decision point"
      },
      {
        "instance_id": "co_01",
        "bias": "Correlation bias",
        "mechanism": "Causal misattribution of current delay to a seasonal pattern observed in unrelated past delays",
        "affected_reasoning_operation": "Causal attribution based on temporal pattern-matching",
        "evidence_source": "Two historical seasonal delay events vs. current supplier's stated non-seasonal cause",
        "distinctiveness_requirement": "Distinct from br_01 at the same decision point: this instance concerns causal reasoning about delay origin, not alternative selection"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Satisficing selection of the first acceptable backup-supplier option under time pressure without comparative evaluation",
        "affected_reasoning_operation": "Alternative generation and evaluation for sourcing decision",
        "evidence_source": "Single known backup supplier contact vs. unexplored alternative sourcing options",
        "distinctiveness_requirement": "Distinct from co_01: concerns choice among alternatives, not causal explanation of the delay"
      },
      {
        "instance_id": "oe_01",
        "bias": "Ostrich effect",
        "mechanism": "Avoidance of requesting the full vibration trend log to prevent exposure to information that could force rescheduling",
        "affected_reasoning_operation": "Information-seeking/avoidance behavior",
        "evidence_source": "Available but unrequested full trend log",
        "distinctiveness_requirement": "Distinct from im_01 at the same decision point: this instance concerns active avoidance of an information source, not a memory-based risk judgment"
      },
      {
        "instance_id": "im_01",
        "bias": "Imaginability Bias",
        "mechanism": "Risk severity judgment anchored on vividness of a recalled past dramatic incident rather than actual gradual trend data",
        "affected_reasoning_operation": "Probability/severity judgment for escalation",
        "evidence_source": "Recalled Press 1 fire incident vs. gradual three-week vibration trend",
        "distinctiveness_requirement": "Distinct from oe_01: this instance concerns a memory-based comparison heuristic, not an information-avoidance act"
      },
      {
        "instance_id": "cv_01",
        "bias": "Conservatism Bias",
        "mechanism": "Underweighting of new 'elevated concern' status relative to previously formed belief that Press 3 is reliable",
        "affected_reasoning_operation": "Belief updating during final schedule commitment",
        "evidence_source": "New engineering status change vs. prior throughput-based belief from decision point 1",
        "distinctiveness_requirement": "Unique to decision point 4; references but does not duplicate the cb_01 evidence base"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "strength": "subtle" },
      { "instance_id": "co_01", "bias": "Correlation bias", "strength": "subtle" },
      { "instance_id": "cv_01", "bias": "Conservatism Bias", "strength": "subtle" },
      { "instance_id": "im_01", "bias": "Imaginability Bias", "strength": "subtle" },
      { "instance_id": "oe_01", "bias": "Ostrich effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Visibility of Press 3 maintenance advisory in the scheduling workflow",
      "original_state": "Advisory logged only in CMMS, separate from the scheduling dashboard",
      "changed_state": "Advisory surfaced prominently within the scheduling dashboard at the point of allocation",
      "variables_to_hold_constant": [
        "Weekend demand surge and required batch size",
        "Press 3 tooling exclusivity",
        "Supplier delay timing and stated cause",
        "Escalation policy and threshold",
        "All stakeholder identities and roles"
      ]
    },
    "scenario_id": "IP_Biased_6",
    "domain_id": "IP",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Automatic allocation: occurrences spread across 4 decision points, no bias repeated within a decision point, co-located biases at decision points 2 and 3 assigned distinct evidence sources and reasoning operations per mechanism-fit and narrative realism (rules 1-4 of allocation policy).",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Weekend demand surge and required batch size",
      "Press 3 tooling exclusivity for the bracket variant",
      "Supplier delay timing and stated cause",
      "Escalation policy and threshold",
      "All stakeholder identities and roles"
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
