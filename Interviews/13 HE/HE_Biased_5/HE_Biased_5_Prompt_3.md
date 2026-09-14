You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{**Interviewer:** Thanks for taking the time. Just to confirm — this is a cognitive task analysis interview, it's confidential, and I'll be asking you to reconstruct a specific incident in detail. There's no evaluation of your performance here, just your reasoning process. Can you start by telling me your role and roughly when this happened?

**Participant:** Sure. I'm a process safety engineer at the site — I cover the batch nitration unit among others. This was about four months ago, night shift transition. I'd just come on when the trend started.

**Interviewer:** Good. Before we get into the sequence, what was the operational objective that shift?

**Participant:** Straightforward — get the batch through its exothermic hold step cleanly and into the next unit operation without deviation, so we could hand off a clean batch at shift change. Nothing unusual planned.

**Interviewer:** Walk me through what first drew your attention to the reactor.

**Participant:** The DCS trend. Pressure was running about eight percent above the expected curve for that stage of the hold. Temperature was fine, right in band, which is usually the first thing you check because if temperature's climbing too you're thinking runaway. It wasn't. So it read more like an instrumentation quirk than a reaction problem, at least on the surface.

**Interviewer:** What did you do with that information?

**Participant:** Well, by the time I'd pulled up the trend, the shift supervisor and two operators were already standing around the panel talking about it. And honestly, that conversation shaped things a lot. Someone said "this looks like the same thing we saw in March," and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier. I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure. We'd had two prior deviations like this, both chalked up to sensor drift, no incident either time. That history was doing a lot of work in the room.

**Interviewer:** So what was the actual decision at that point — stop the batch, escalate, or continue?

**Participant:** Continue monitoring. We didn't interrupt. Looking back, the alternative was to call an emergency hold pending manual inspection, or escalate straight to the on-call plant manager. I didn't push for either. The shared read in the room was "probably the same sensor issue," and that's the frame I went with.

**Interviewer:** What happened next?

**Participant:** Pressure kept climbing, slowly, over about twenty minutes. Eventually the relief valve lifted — you could hear it, a distinct pop — and then pressure fell back and reseated. No release beyond the relief line, nobody hurt. But at that point we genuinely didn't know if the batch chemistry itself was compromised.

**Interviewer:** How did you move from "we had a relief lift" to a root cause?

**Participant:** I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion. A full instrument and kinetics review would've taken three to four hours, and that would blow past shift changeover, so there was real pressure to land on something workable.

**Interviewer:** Did anything about this batch differ from the two prior "drift" events?

**Participant:** Yeah, actually — this batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily. It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review.

**Interviewer:** How confident were you in that diagnosis at the time?

**Participant:** Fairly confident, honestly. I've been on this unit a long time, I've seen this signature before. It felt like a case I recognized rather than a case I needed to dig into further.

**Interviewer:** What did you learn afterward that touched on that conclusion?

**Participant:** A partial calibration spot-check later showed the transmitter was actually within tolerance. That undercuts the drift explanation somewhat. And nobody had gone back and independently reviewed the new catalyst lot's exotherm profile. So the diagnosis I'd settled on quickly was never really closed out on the chemistry side.

**Interviewer:** Let's move to the mitigation decision. What options were in front of you?

**Participant:** The external relief-system contractor reviewed the incident and came back with a data package showing our existing relief system had a narrower margin than we'd assumed, specifically for this catalyst lot. Their recommendation was to add an automated high-pressure interlock trip before restart. It's a system with a decent track record at two comparable plants. The alternative was keeping our current manual response procedure, which has run for years here without failure.

**Interviewer:** What did you decide?

**Participant:** I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet. Our manual process, whatever its limits, was a known quantity.

**Interviewer:** How did you weigh the contractor's margin data against that operational familiarity?

**Participant:** I didn't dismiss the margin data, I just — I think I gave more weight to the fact that the interlock was unproven here specifically, on our unit, with our people. The margin reduction was real on paper, but it hadn't caused an actual failure yet either. The known system winning out over the new one felt like the safer bet.

**Interviewer:** Any information afterward relevant to that call?

**Participant:** The plant manager pointed out later that adding the interlock then would've cost about one shift of downtime, versus none for keeping status quo. And no further excursions happened for the rest of the campaign, so we never really got a clean test of whether the interlock would've mattered.

**Interviewer:** Take me into the MOC meeting. Who was there and what was the disagreement?

**Participant:** Myself, the senior process safety engineer — he was on the original commissioning team for this unit, well known across the plant for a strong safety record — and the contractor. The senior engineer backed my sensor-drift read, said it matched his experience with the unit over the years. The contractor's written analysis flagged the catalyst-lot kinetics as an open gap and recommended keeping the MOC open until that was resolved. No new data had come in since the calibration check.

**Interviewer:** How did you resolve that?

**Participant:** I sided with the senior engineer's view. He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site. And frankly, his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it. The contractor's point was on paper, but it felt like an outside read compared to someone who's actually run this unit for fifteen years.

**Interviewer:** What happened after the MOC closed?

**Participant:** We restarted without the kinetics review. Production since then hasn't clearly proven or disproven that call either way.

**Interviewer:** Looking back across the shift, where did time pressure weigh most heavily?

**Participant:** Definitely the root cause call and the MOC closure — both had that shift-changeover clock running, and neither had a hard deadline forcing an answer, but it felt like there was one.

**Interviewer:** If the contractor's report had arrived before the control-room discussion instead of after, do you think the outcome changes?

**Participant:** Possibly. If that margin data had been sitting on the table before everyone converged on "probably fine," it might have slowed the room down. Order mattered more than I'd like to admit.

**Interviewer:** If a less senior colleague had proposed the sensor-drift explanation in that MOC meeting, would you have accepted it as readily?

**Participant:** Probably not with the same confidence, no.

**Interviewer:** What would you do differently with a similar deviation on a new catalyst lot?

**Participant:** Flag the lot change explicitly, early, before pattern-matching to prior events — treat it as its own case rather than assuming it inherits the old explanation.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Group Polarization",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via observable shift toward group extremity in a collective monitoring decision, not individual reasoning alone"
      },
      {
        "bias": "Dunning-Kruger effect or Illusion of understanding",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via overconfident causal conclusion drawn from incomplete pattern-matching, ignoring a known unknown (new catalyst lot)"
      },
      {
        "bias": "Risk aversion bias",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via disproportionate weighting of unfamiliar-change risk over documented status-quo risk in a mitigation choice"
      },
      {
        "bias": "In-group bias",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via crediting an in-house colleague's view due to team affiliation rather than technical content"
      },
      {
        "bias": "Halo effect",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via transferring general reputation to credibility of a specific unverified technical claim"
      }
    ],
    "target_bias_names": [
      "Group Polarization",
      "Dunning-Kruger effect or Illusion of understanding",
      "Risk aversion bias",
      "In-group bias",
      "Halo effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Group Polarization", "requested_occurrences": 1 },
      { "bias": "Dunning-Kruger effect or Illusion of understanding", "requested_occurrences": 1 },
      { "bias": "Risk aversion bias", "requested_occurrences": 1 },
      { "bias": "In-group bias", "requested_occurrences": 1 },
      { "bias": "Halo effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "gp_01", "bias": "Group Polarization" },
      { "instance_id": "dk_01", "bias": "Dunning-Kruger effect or Illusion of understanding" },
      { "instance_id": "ra_01", "bias": "Risk aversion bias" },
      { "instance_id": "ig_01", "bias": "In-group bias" },
      { "instance_id": "he_01", "bias": "Halo effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "gp_01", "bias": "Group Polarization", "decision_point": 1 },
      { "instance_id": "dk_01", "bias": "Dunning-Kruger effect or Illusion of understanding", "decision_point": 2 },
      { "instance_id": "ra_01", "bias": "Risk aversion bias", "decision_point": 3 },
      { "instance_id": "ig_01", "bias": "In-group bias", "decision_point": 4 },
      { "instance_id": "he_01", "bias": "Halo effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "gp_01",
        "bias": "Group Polarization",
        "mechanism": "Collective discussion in the control room shifts the group's confidence toward a more extreme benign judgment than any individual initially held, driving continued monitoring instead of an independent interrupt",
        "affected_reasoning_operation": "Group risk judgment formation before interrupt/continue decision",
        "evidence_source": "Informal control-room discussion among supervisor, operators, and engineer",
        "distinctiveness_requirement": "Only instance of this bias; occurs at decision point 1 via group discussion dynamics, not individual cognition"
      },
      {
        "instance_id": "dk_01",
        "bias": "Dunning-Kruger effect or Illusion of understanding",
        "mechanism": "Confident causal conclusion drawn from superficial pattern match to prior events, unaware that the new catalyst lot places the current situation outside prior experience",
        "affected_reasoning_operation": "Causal attribution / root cause conclusion under incomplete data",
        "evidence_source": "Two prior 'drift' precedents plus new, unreviewed catalyst-lot variable",
        "distinctiveness_requirement": "Only instance of this bias; occurs at decision point 2 as an individual diagnostic judgment, distinct in evidence and operation from gp_01"
      },
      {
        "instance_id": "ra_01",
        "bias": "Risk aversion bias",
        "mechanism": "Disproportionate weight given to the unfamiliar risk of a new interlock relative to the better-documented margin-reduction risk of the status quo procedure",
        "affected_reasoning_operation": "Mitigation option selection under asymmetric gain/loss framing",
        "evidence_source": "Contractor's margin analysis versus unit's manual-procedure track record",
        "distinctiveness_requirement": "Only instance of this bias; occurs at decision point 3, involving a change-versus-status-quo choice distinct from prior decision points"
      },
      {
        "instance_id": "ig_01",
        "bias": "In-group bias",
        "mechanism": "Crediting a colleague's conclusion because of shared team membership, discounting an outsider's written technical objection",
        "affected_reasoning_operation": "Evidence-source weighting during MOC technical disagreement",
        "evidence_source": "Senior colleague's verbal agreement citing team tenure",
        "distinctiveness_requirement": "Shares decision point 4 with he_01 but uses a distinct evidence source (team-affiliation statement) and reasoning operation (source-of-origin weighting) rather than trait-based credibility transfer"
      },
      {
        "instance_id": "he_01",
        "bias": "Halo effect",
        "mechanism": "General reputation for safety performance is used to validate an unrelated, specific, unverified technical claim about catalyst-lot kinetics",
        "affected_reasoning_operation": "Credibility transfer from general trait to specific claim",
        "evidence_source": "Senior colleague's plant-wide reputation record",
        "distinctiveness_requirement": "Shares decision point 4 with ig_01 but uses a distinct evidence source (reputation record) and reasoning operation (trait-to-claim generalization) rather than group-affiliation weighting"
      }
    ],
    "intended_strength": [
      { "instance_id": "gp_01", "bias": "Group Polarization", "strength": "subtle" },
      { "instance_id": "dk_01", "bias": "Dunning-Kruger effect or Illusion of understanding", "strength": "moderate" },
      { "instance_id": "ra_01", "bias": "Risk aversion bias", "strength": "subtle" },
      { "instance_id": "ig_01", "bias": "In-group bias", "strength": "subtle" },
      { "instance_id": "he_01", "bias": "Halo effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Biased_5",
    "domain_id": "HE",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points by mechanism fit and narrative realism: one bias per decision point at DP1-DP3; DP4 hosts two biases (In-group bias and Halo effect) because the MOC closure moment naturally involves both source-affiliation weighting and reputation-based credibility transfer, kept distinct via separate evidence sources and reasoning operations per co-location rule (max two per decision point, no more than two of the same bias anywhere).",
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
