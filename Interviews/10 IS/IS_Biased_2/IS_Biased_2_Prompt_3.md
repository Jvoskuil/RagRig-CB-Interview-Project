You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a cognitive task analysis session—I'll be asking about a specific incident you worked through, and I'd like your candid recollection of how you reasoned through it, not a polished after-the-fact summary. Everything stays anonymized. Is that okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me your role and what you were responsible for during this incident?

Participant: I lead a five-person team on our internal analytics platform—basically the tooling our support organization uses to look up customer accounts, usage history, that kind of thing. I own delivery for that dashboard and I report into the VP of Engineering. During this period I was accountable for keeping the platform stable and also for a demo we had coming up for leadership.

Interviewer: Can you walk me through what first alerted you to a problem?

Participant: Load times on the dashboard started creeping up—support tickets came in complaining pages were taking six, seven seconds instead of two. Over about two weeks it basically tripled. We hadn't touched much in that subsystem recently except our caching layer, which we'd built in-house—we call it QuickCache—about eight months earlier.

Interviewer: What did you do first?

Participant: I had two real options—run broad instrumentation across the whole stack to be safe, or go straight at QuickCache since it was the most recent change and the timing lined up. We were also getting pressure from the support lead because tickets kept climbing, so I didn't want to spend a week doing exhaustive profiling everywhere. I told the team to profile QuickCache specifically first, since it was the most likely suspect given the timing, and if that came back clean we'd widen the net.

Interviewer: What came out of that?

Participant: Profiling confirmed QuickCache was adding real latency under high load—invalidation was firing more than it should, forcing extra database round-trips. It also surfaced a separate, unrelated issue: a missing index on one of the support tables. Neither of those was hugely surprising, but it did mean two independent things needed fixing, not one.

Interviewer: How did the investigation affect team workload?

Participant: Priya, who originally built QuickCache, took point on diagnosing the invalidation logic. Dev, one of our other senior engineers, has also worked deep in that code. Everyone else picked up the index fix and other tickets. That's roughly how the two weeks split.

Interviewer: Let's step through it chronologically. After profiling confirmed the QuickCache issue, what was the next major decision?

Participant: That's where it got harder. QuickCache had taken us about eight months to build and stabilize—three separate patch rounds just to get it production-ready in the first place. Priya was adamant we were close, that one more targeted patch to the invalidation logic would fix it. On the other hand, there's a mature Redis-backed option out there that could probably replace QuickCache in about a sprint, with a track record we could actually point to.

Interviewer: What did you decide?

Participant: I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up. I figured one more focused patch, with the team that knows it best, would get us there.

Interviewer: What information did you rely on most heavily for that call?

Participant: Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily.

Interviewer: What happened after that decision?

Participant: The patch only bought us about fifteen percent improvement. Not enough to hit the demo deadline. And the extra sprint stretched the team thin on top of everything else going on.

Interviewer: Third decision point—who owned the urgent fix at that stage?

Participant: Right, so at this point we're down to days, not weeks. Dev has the deepest knowledge of QuickCache internals, but Dev had also been at the center of a production outage about three weeks earlier—a rushed deploy under pressure that caused a real incident, though the postmortem showed it was handled well and fixed fast. Marcus was the other option; he's been solid but has missed several deadlines over the past year, nothing dramatic, just a slower, steadier pattern of slipping.

Interviewer: What did you decide, and why?

Participant: I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet.

Interviewer: How did that play out?

Participant: Handoff was messy—Dev had context Marcus didn't, so there was friction getting him up to speed, and the fix took longer than it would have with Dev leading it outright.

Interviewer: Looking back, how did you weigh Dev's eighteen months of strong delivery against that one incident?

Participant: I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either.

Interviewer: With three days left before the demo, what did you decide about reporting status?

Participant: Latency was better but not fully resolved. I could've asked to push the demo, shipped quietly and hoped nobody noticed the remaining lag, or just told leadership straight where things stood. I went with transparency—laid out what was fixed, what wasn't, and proposed a follow-up sprint with monitoring in place. They accepted that.

Interviewer: What was the reasoning behind choosing that option over delaying the demo?

Participant: Delaying felt like it would cost more politically than it would gain technically—the partial fix was real progress, and monitoring would catch anything that slipped. Hiding it wasn't really on the table once I thought about it seriously.

Interviewer: If you'd had the profiling data suggesting a structural rework earlier, would that have changed your patch-versus-switch decision?

Participant: Possibly. If I'd seen it that clearly before committing the extra sprint, I might have pushed harder for the parallel evaluation option instead.

Interviewer: If Dev's outage had happened a year earlier rather than three weeks before this decision, would you have assigned the fix differently?

Participant: Probably, yeah. With more distance from it, I likely would have just given it to him outright given his familiarity with the system.

Interviewer: Anything you'd tell a peer facing a similar in-house-build-versus-alternative call?

Participant: Try to separate how much you've already put into something from what it's actually going to cost you going forward. Easier said than done when your team's pride and expertise are wrapped up in it.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Irrational Escalation",
        "occurrences": 1,
        "mechanism_constraint": "Must be justified via prior sunk time/effort/expertise, not forward-looking cost-benefit reasoning"
      },
      {
        "bias": "Negativity Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve disproportionate weight on one vivid recent negative event versus a larger body of mixed/positive evidence"
      }
    ],
    "target_bias_names": [
      "Irrational Escalation",
      "Negativity Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Irrational Escalation",
        "requested_occurrences": 1
      },
      {
        "bias": "Negativity Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "decision_point": 2
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "mechanism": "Continued investment decision justified by prior sunk effort (eight months, three patch cycles, internal expertise) rather than forward-looking expected value of the alternative solution",
        "affected_reasoning_operation": "Resource-allocation choice under uncertainty",
        "evidence_source": "History of QuickCache development effort and prior patch outcomes versus profiling-based redesign recommendation",
        "distinctiveness_requirement": "Single instance at decision point 2 only; must not be repeated as a restated example, follow-up probe answer, or outcome explanation elsewhere in the interview"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "mechanism": "Disproportionate weight given to one recent, vivid negative event (Dev's outage) relative to a longer positive track record and a comparably negative but less salient pattern from another engineer (Marcus's missed deadlines)",
        "affected_reasoning_operation": "Personnel-risk assessment feeding a task-assignment decision",
        "evidence_source": "Incident postmortem and eighteen-month performance history for Dev, contrasted with Marcus's deadline record",
        "distinctiveness_requirement": "Single instance at decision point 3 only; must not be repeated as a restated example, follow-up probe answer, or outcome explanation elsewhere in the interview"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "strength": "subtle"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
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
    "scenario_id": "IS_Biased_2",
    "domain_id": "IS",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences were spread across distinct decision points (Irrational Escalation at decision point 2, Negativity Bias at decision point 3) chosen for mechanism fit and narrative realism within a single continuous incident; decision points 1 and 4 were kept clean to avoid unintended bias density and to preserve plausible non-bias explanations at every decision point.",
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
