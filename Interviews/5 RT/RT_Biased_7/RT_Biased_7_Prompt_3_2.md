You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{**Interviewer:** Thanks for making time for this. Just to confirm, this is a routine debrief — I want to walk through a specific job you handled, how you made the calls you made, what information you had at each point. Nothing here is about assigning fault. Can you tell me your role?

**Participant:** Sure. I'm a Maintenance-of-Way Supervisor, I run a panel tie gang on the secondary main. I've got about eleven years in track maintenance, six as a supervisor. I handle scoping, scheduling, crew assignment, coordination with dispatch and the roadmaster on outage windows.

**Interviewer:** Good. Tell me about the incident you flagged for this conversation.

**Participant:** We had an ultrasonic rail flaw car come through and flag a detail fracture indication at mile post 47.3 — that's a curve on the secondary main. Dispatch gave us a 60-hour track window to get in there, pull the bad rail, do tie renewal on the segment, get it tamped and squared, and get the slow order lifted before a contracted freight customer's holiday surge started. There was a penalty clause in that contract tied to when the slow order came off, so timing mattered a lot to the regional office.

**Interviewer:** What was your main objective going in?

**Participant:** Get it done safe, get it done in the window. Those two things are supposed to line up, but this one had some tension in it — rain was forecast within about 48 hours, which cuts into ballast curing time, and we only had one tamper and one ballast regulator, shared with the gang working the adjacent territory. So there wasn't a lot of slack.

**Interviewer:** Walk me through what happened, start to finish.

**Participant:** The flaw car report came in on a Tuesday morning. Our last full inspection on that curve was about two weeks old, and it had rated the ties as fair, some deterioration noted, nothing urgent. I used our standard production rate for a 500-foot renewal — so many ties an hour with a full crew — and built a 60-hour schedule off that, plus the fair rating. We mobilized that afternoon.

Once we started pulling ties Wednesday morning, the count came in higher than what I'd planned for — more of them were rotted through than the fair rating suggested. So the roadmaster, two of our inspectors, and my foreman got together that afternoon to talk about how to handle the revised scope inside the same window. The foreman pitched running an extra tamper pass and cutting ballast dwell time to make up the lost hours. One of the inspectors mentioned a similar-looking curve we'd worked three years back that came in light on tie count too, and it held up fine long-term. That gave the room some confidence, and we went with the faster method.

By Thursday's mid-course check-in with the regional engineering manager, we were still behind where the revised plan said we should be, though some segments were actually ahead of pace. I gave him my read on the status. Then Friday morning, six hours before the freight window opened, we hadn't gotten the geometry car through yet — only manual gauge checks — and I had to decide whether to hold the slow order or lift it.

**Interviewer:** Let's go back to Tuesday. What made you comfortable locking in that 60-hour schedule off the fair rating and the standard rate table?

**Participant:** Honestly, the fair rating was the most recent data point I had, and the production table's what we use on every job like this — it's not something I second-guess unless there's a specific reason to. There is a longer defect history on that segment in our system, going back five years, that tracks flaw growth over time. I didn't pull it. At the time it felt like it'd just slow down getting the crew mobilized, and the two-week-old inspection seemed current enough to plan against.

**Interviewer:** Did anything about the flaw car flag itself suggest looking further back?

**Participant:** Looking back, probably. A detail fracture indication at that specific location wasn't the first flag we'd had there, I found out later. But at the time, I treated it as a standalone event and scoped it like a typical renewal.

**Interviewer:** When the tie count came back high on Wednesday, how did the group land on the faster method?

**Participant:** We talked through it for maybe twenty minutes. Nobody walked in pushing hard either way — my foreman had a proposal, the inspectors had questions about dwell time and compaction. But once the prior curve came up, the one that "always held up fine" with a lighter tie count, the room's mood shifted. By the end, everybody was more on board with running fast than any one of us had been at the start of that meeting.

**Interviewer:** Was that prior curve comparable in other respects — soil, drainage?

**Participant:** Not exactly, no. Our site report from the day before had actually flagged the subgrade drainage at 47.3 as worse than typical for that district. Nobody brought that back up once the other curve got mentioned. It just didn't come up again.

**Interviewer:** On Thursday's status call, how did you frame things for the regional manager?

**Participant:** I told him we'd had a late ballast delivery and lost some hours to a rain delay overnight, which was true, both happened. For the segments that were tracking on pace, I credited the crew's execution and the call to add the extra tamper pass. He signed off on keeping the existing timeline.

**Interviewer:** Did the original scope estimate come up as a factor in the slippage?

**Participant:** Not really, no. I didn't bring it up in that call. In hindsight it probably belonged in the conversation, since the tie count coming in high was part of why we were behind in the first place.

**Interviewer:** Friday morning — six hours out from the window opening, geometry car not through yet. What went into that call?

**Participant:** The penalty clause was the thing sitting heaviest on me at that point. Missing that window meant a real financial hit to the region, and I didn't want to be the reason for that. I knew the geometry car would give us a continuous read across the whole segment that manual checks just can't match, but with that loss already sitting right in front of us and the verification still open-ended, avoiding the hit was what drove the call more than anything else. We'd done manual gauge spot-checks across the segment and they came back clean, and I'd set up extra hand-inspection rounds plus a pilot train running the curve at reduced speed before we opened it to normal traffic. The roadmaster pointed out that the hand rounds and the pilot train wouldn't give us the same continuous profile the car would, but I figured between what we already had and those extra rounds, we'd catch anything that mattered. Between those, I felt like we had the risk covered well enough to lift the slow order without waiting on the geometry car.

**Interviewer:** What was the alternative you weighed against that?

**Participant:** Holding the slow order until the geometry car actually ran it, even if that meant eating the penalty. We talked about it briefly with the roadmaster, but the inspection rounds and the pilot train felt like enough of a safety net that we didn't need to wait.

**Interviewer:** What happened with the geometry car pass?

**Participant:** It ran the next day and came back within tolerance. So the track was fine. But I'll say that doesn't necessarily tell you whether lifting it early that morning was the right call or just the way it worked out.

**Interviewer:** If you'd had that five-year defect history in hand on Tuesday, what do you think would've changed?

**Participant:** Probably the initial schedule. If I'd seen recurring flaw growth at that spot, I'd have scoped it heavier from the start instead of finding out mid-job.

**Interviewer:** If the contract penalty hadn't existed, would Friday's decision have gone differently?

**Participant:** I think I'd have been more willing to just wait for the geometry car. It wasn't the only factor, but it was a big part of why six hours felt urgent instead of just cautious.

**Interviewer:** Last one — if a different inspector had been in that Wednesday meeting, someone without that prior-curve story, do you think the method decision changes?

**Participant:** Maybe. That story didn't have hard data behind it, just a memory of how a similar-looking job turned out. Take it out of the room and the conversation might've stayed more cautious. Hard to say for sure.

**Interviewer:** That's helpful. Thanks for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Group Polarization", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Ostrich Effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Self-serving Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Planning Fallacy", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Loss Aversion or Loss Framing effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Experience Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Illusion of Control", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Group Polarization",
      "Ostrich Effect",
      "Self-serving Bias",
      "Planning Fallacy",
      "Loss Aversion or Loss Framing effect",
      "Experience Bias",
      "Illusion of Control"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Group Polarization", "requested_occurrences": 1 },
      { "bias": "Ostrich Effect", "requested_occurrences": 1 },
      { "bias": "Self-serving Bias", "requested_occurrences": 1 },
      { "bias": "Planning Fallacy", "requested_occurrences": 1 },
      { "bias": "Loss Aversion or Loss Framing effect", "requested_occurrences": 1 },
      { "bias": "Experience Bias", "requested_occurrences": 1 },
      { "bias": "Illusion of Control", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "rt7_01", "bias": "Ostrich Effect" },
      { "instance_id": "rt7_02", "bias": "Planning Fallacy" },
      { "instance_id": "rt7_03", "bias": "Group Polarization" },
      { "instance_id": "rt7_04", "bias": "Experience Bias" },
      { "instance_id": "rt7_05", "bias": "Self-serving Bias" },
      { "instance_id": "rt7_06", "bias": "Loss Aversion or Loss Framing effect" },
      { "instance_id": "rt7_07", "bias": "Illusion of Control" }
    ],
    "intended_decision_points": [
      { "instance_id": "rt7_01", "bias": "Ostrich Effect", "decision_point": 1 },
      { "instance_id": "rt7_02", "bias": "Planning Fallacy", "decision_point": 1 },
      { "instance_id": "rt7_03", "bias": "Group Polarization", "decision_point": 2 },
      { "instance_id": "rt7_04", "bias": "Experience Bias", "decision_point": 2 },
      { "instance_id": "rt7_05", "bias": "Self-serving Bias", "decision_point": 3 },
      { "instance_id": "rt7_06", "bias": "Loss Aversion or Loss Framing effect", "decision_point": 4 },
      { "instance_id": "rt7_07", "bias": "Illusion of Control", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "rt7_01",
        "bias": "Ostrich Effect",
        "mechanism": "Avoids retrieving accessible five-year defect-growth history that could reveal a larger true scope, proceeding instead on the more favorable existing rating.",
        "affected_reasoning_operation": "Evidence-selection before scope commitment",
        "evidence_source": "Existing accessible defect-growth file vs. two-week-old fair rating",
        "distinctiveness_requirement": "Distinct from rt7_02 by operating on information-seeking/avoidance rather than duration estimation."
      },
      {
        "instance_id": "rt7_02",
        "bias": "Planning Fallacy",
        "mechanism": "Commits to a best-case standard production-rate duration despite an available deterioration signal, without adjustment.",
        "affected_reasoning_operation": "Duration/scope estimation and schedule commitment",
        "evidence_source": "Standard production rate table vs. 'fair, some deterioration' rating",
        "distinctiveness_requirement": "Distinct from rt7_01 by concerning time estimation rather than information avoidance, same decision point but different reasoning operation."
      },
      {
        "instance_id": "rt7_03",
        "bias": "Group Polarization",
        "mechanism": "Collective discussion produces greater confidence in the risky/accelerated method than individuals held beforehand.",
        "affected_reasoning_operation": "Collective risk judgment during method selection",
        "evidence_source": "Foreman's acceleration proposal and group discussion dynamic",
        "distinctiveness_requirement": "Distinct from rt7_04 by concerning group-level confidence shift, not individual analogical recall."
      },
      {
        "instance_id": "rt7_04",
        "bias": "Experience Bias",
        "mechanism": "Recollection of a superficially similar past curve is used to judge current risk without accounting for a documented drainage difference.",
        "affected_reasoning_operation": "Analogical retrieval feeding risk assessment",
        "evidence_source": "Inspector's recollection of prior curve vs. phase-1 drainage note",
        "distinctiveness_requirement": "Distinct from rt7_03 by concerning an individual's memory-based analogy rather than group confidence dynamics."
      },
      {
        "instance_id": "rt7_05",
        "bias": "Self-serving Bias",
        "mechanism": "Attributes slippage to external causes while attributing on-pace progress to own decisions/crew skill within the same report.",
        "affected_reasoning_operation": "Causal attribution during status reporting",
        "evidence_source": "Mixed progress data reported to Regional Engineering Manager",
        "distinctiveness_requirement": "Unique to decision point 3; no other instance addresses causal attribution of mixed outcomes."
      },
      {
        "instance_id": "rt7_06",
        "bias": "Loss Aversion or Loss Framing effect",
        "mechanism": "Final decision is framed around avoiding the contractual penalty more heavily than around the safety margin from waiting for verification.",
        "affected_reasoning_operation": "Gain/loss weighting in the final go/no-go choice",
        "evidence_source": "Penalty clause and six-hour window vs. incomplete geometry car pass",
        "distinctiveness_requirement": "Distinct from rt7_07 by concerning the framing/weighting of the choice itself, not confidence in mitigation capability."
      },
      {
        "instance_id": "rt7_07",
        "bias": "Illusion of Control",
        "mechanism": "Overestimates ability of added hand-inspection rounds and pilot train to substitute for a completed geometry car pass.",
        "affected_reasoning_operation": "Risk-control judgment underlying final authorization",
        "evidence_source": "Planned compensating inspection measures vs. absence of completed formal verification",
        "distinctiveness_requirement": "Distinct from rt7_06 by concerning perceived mitigation efficacy, not the loss/gain framing of the decision."
      }
    ],
    "intended_strength": [
      { "instance_id": "rt7_01", "bias": "Ostrich Effect", "strength": "subtle" },
      { "instance_id": "rt7_02", "bias": "Planning Fallacy", "strength": "subtle" },
      { "instance_id": "rt7_03", "bias": "Group Polarization", "strength": "subtle" },
      { "instance_id": "rt7_04", "bias": "Experience Bias", "strength": "subtle" },
      { "instance_id": "rt7_05", "bias": "Self-serving Bias", "strength": "subtle" },
      { "instance_id": "rt7_06", "bias": "Loss Aversion or Loss Framing effect", "strength": "subtle" },
      { "instance_id": "rt7_07", "bias": "Illusion of Control", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "RT_Biased_7",
    "domain_id": "RT",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across decision points by mechanism fit and narrative realism: DP1 (Ostrich Effect, Planning Fallacy) at initial scoping/scheduling; DP2 (Group Polarization, Experience Bias) at the team method-selection briefing, kept distinct via group-level vs. individual-memory mechanisms; DP3 (Self-serving Bias) at the mid-course attribution report; DP4 (Loss Aversion, Illusion of Control) at the final go/no-go, kept distinct via decision-framing vs. mitigation-confidence mechanisms. No decision point holds more than two instances of any single bias, and no bias appears at more than its requested count.",
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
