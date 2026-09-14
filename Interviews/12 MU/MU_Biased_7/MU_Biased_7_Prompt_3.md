You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{**Interviewer:** Thanks for making time for this. Just to confirm, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the incident, not in second-guessing the outcome. Everything's confidential and used for training and research purposes only. You're an Assistant Mine Manager at the site, correct?

**Participant:** That's right. I've been in that role about three years, twenty years underground total, mostly hard rock.

**Interviewer:** Good. Let's start broad — can you walk me through what was happening in Stope 14 East during that shift?

**Participant:** Sure. We were running a stope on the 950 level, standard longhole retreat mining. We'd had three microseismic events overnight — moderate magnitude, above what the array normally logs for that block over a rolling thirty-day average. No visible damage reported by the night shift, though. At the same time, we were two days behind on the monthly tonnage target, so there was some pressure from the production side to keep things moving.

**Interviewer:** What was your main objective going into that morning?

**Participant:** Keep the crew safe, obviously, but also not create a stoppage we couldn't justify. We'd had false alarms before — events that looked concerning on paper but turned out to be nothing. You don't want to shut a stope every time the array blips, or the crew starts tuning out the real warnings.

**Interviewer:** Take me through what you actually decided that morning.

**Participant:** The ground support plan for that stope had been signed off about four months earlier, and nothing had changed structurally since then — no fall of ground, nothing visible. So my read was that the plan was still sound, and I didn't see a reason to hold the crew back. We had options — pause entry and get an unscheduled inspection, or drop crew numbers until someone looked at it — but honestly, revising an approved plan on the back of three events felt like more disruption than the situation called for. We let day shift go in and start drilling as scheduled.

**Interviewer:** Did anything happen during that shift that stood out?

**Participant:** A bit of loose rock came off a rib wall mid-shift. Crew scaled it down, logged it as routine. Nothing that changed my thinking at that point.

**Interviewer:** Let's move to later that day — you mentioned a hazard rating came in.

**Participant:** Yes, our geotech support is remote most of the week — the engineer's only on-site two days. The model came back with a 2.3 on their five-point scale, tagged "moderate but manageable." I also remembered we'd had almost the exact same rating and event cluster near Stope 9 about six weeks earlier, and that resolved completely fine, no incident. So between the number and that memory, I felt reasonably comfortable.

**Interviewer:** Were there other options at that point?

**Participant:** We could have asked for an updated rating that accounted for the blind spot near the intersection — the array doesn't read well there — or just held the blast until the engineer was back on-site the next day. But the 2.3 read as solid enough, and Stope 9 had gone fine under similar numbers, so I authorized the afternoon blast clearance.

**Interviewer:** How much weight did that number carry versus other considerations?

**Participant:** Probably more than I'd admit at the time. It's a clean, specific figure — 2.3 — and it's easy to anchor to something that concrete rather than sit with "we're not totally sure." And the Stope 9 comparison made it feel familiar, like we'd seen this movie before.

**Interviewer:** What happened after the blast was cleared?

**Participant:** About two hours later there was a second event, larger than the first three, and outside what the model's confidence range would have predicted.

**Interviewer:** Let's talk about what happened next — the cracking.

**Participant:** Right, after the blast, the shift supervisor flagged some hairline cracking in the shotcrete on one rib. Around the same time a junior inspector — one of the geotech contractor's people — sent an email recommending we re-support before doing any more blasting. But two other crew members separately told me it looked like typical post-blast settling, nothing unusual.

**Interviewer:** How did you weigh those two views?

**Participant:** I leaned toward the crew's read. We'd seen a very similar crack pattern in Stope 9 previously that never led anywhere. So when the reporting went up to the production superintendent, I passed along the crew's "typical settling" assessments. The inspector's note got filed — I didn't raise it on the shift call, mostly because it felt like it would just muddy a picture that already seemed clear enough from the people who were actually standing there.

**Interviewer:** Was there a version of that decision where the inspector's note carried equal weight?

**Participant:** Looking back, sure — we could have treated the cracking as inconclusive and brought in an independent check rather than leaning on precedent and the on-the-ground opinions. At the time it didn't feel necessary because the Stope 9 comparison made the pattern seem like something we already understood.

**Interviewer:** Let's get to the final decision point — the next scheduled blast.

**Participant:** Right before that decision, one of the array nodes had sensor lag, so we didn't have confirmed magnitude data for recent ground movement. Then a small rock fall happened near the access drift — no injuries, minor. The superintendent was pushing to keep the blast on schedule to hit the month-end number.

**Interviewer:** What went into your call there?

**Participant:** Honestly, that rock fall didn't worry me much. I've personally been through plenty of similar events over twenty years underground, and they almost never escalate. If anything, it read to me as consistent with what we'd already been seeing — minor settling, nothing structural. I authorized the blast.

**Interviewer:** Were you uncertain at all in that moment?

**Participant:** There was a gap, sure — we didn't have the sensor confirmation we'd normally want. But I was confident in the call. Twenty years gives you a feel for these things that a delayed sensor reading doesn't necessarily add to.

**Interviewer:** Could you have suspended the blast pending that data, or escalated to the engineer for a fresh look?

**Participant:** Both were on the table. I just didn't think either was warranted given how the shift had gone.

**Interviewer:** What happened afterward?

**Participant:** The blast went fine. Ground stayed stable through the rest of the shift. We did schedule a post-shift review, though the underlying ground support plan wasn't actually revised.

**Interviewer:** Stepping back — if the geotechnical engineer had been on-site the whole time rather than remote, would anything have gone differently?

**Participant:** Possibly. Having someone physically there to look at the cracking directly, rather than relying on an email and crew impressions, might have changed how that got weighted.

**Interviewer:** And if the hazard rating had come back at 3.5 instead of 2.3?

**Participant:** That would have stopped me. A 3.5 doesn't let you lean on a comfortable memory the way a 2.3 does.

**Interviewer:** Looking back, would you make the same call on continuing under the existing support plan that first morning?

**Participant:** I'd probably want more of a structured comparison next time — actually laying the new seismic readings against the plan's original assumptions, rather than just defaulting to "nothing's changed, so we haven't changed anything." At the time, though, it felt like the obvious choice.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Status quo bias", "occurrences": 1, "mechanism_constraint": "Defaulting to unrevised ground support plan despite new seismic evidence"},
      {"bias": "Illusion of validity", "occurrences": 2, "mechanism_constraint": "Overconfidence in numeric model precision (DP2) and in narrative case-pattern coherence (DP3)"},
      {"bias": "Confirmation Bias", "occurrences": 2, "mechanism_constraint": "Selective evidence transmission (DP3) and belief-consistent interpretation of ambiguous new evidence (DP4)"},
      {"bias": "Overconfidence Bias", "occurrences": 1, "mechanism_constraint": "Miscalibrated personal certainty despite unresolved sensor gap and dissenting input"},
      {"bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Risk judgment anchored to a single vivid recalled prior event rather than base rates"}
    ],
    "target_bias_names": [
      "Status quo bias",
      "Illusion of validity",
      "Confirmation Bias",
      "Overconfidence Bias",
      "Availability Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Status quo bias", "requested_occurrences": 1},
      {"bias": "Illusion of validity", "requested_occurrences": 2},
      {"bias": "Confirmation Bias", "requested_occurrences": 2},
      {"bias": "Overconfidence Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "sqb_01", "bias": "Status quo bias"},
      {"instance_id": "iv_01", "bias": "Illusion of validity"},
      {"instance_id": "iv_02", "bias": "Illusion of validity"},
      {"instance_id": "cb_01", "bias": "Confirmation Bias"},
      {"instance_id": "cb_02", "bias": "Confirmation Bias"},
      {"instance_id": "ob_01", "bias": "Overconfidence Bias"},
      {"instance_id": "ab_01", "bias": "Availability Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "sqb_01", "bias": "Status quo bias", "decision_point": 1},
      {"instance_id": "iv_01", "bias": "Illusion of validity", "decision_point": 2},
      {"instance_id": "ab_01", "bias": "Availability Bias", "decision_point": 2},
      {"instance_id": "iv_02", "bias": "Illusion of validity", "decision_point": 3},
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 3},
      {"instance_id": "cb_02", "bias": "Confirmation Bias", "decision_point": 4},
      {"instance_id": "ob_01", "bias": "Overconfidence Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sqb_01",
        "bias": "Status quo bias",
        "mechanism": "Default retention of existing ground support plan despite new seismic evidence, without substantive re-evaluation",
        "affected_reasoning_operation": "Option evaluation under a default anchor",
        "evidence_source": "Overnight microseismic logs vs. four-month-old approved plan",
        "distinctiveness_requirement": "Sole status quo instance; no other decision point may exhibit this mechanism"
      },
      {
        "instance_id": "iv_01",
        "bias": "Illusion of validity",
        "mechanism": "Overweighting precision of a numeric hazard rating despite known model blind spot",
        "affected_reasoning_operation": "Confidence calibration on quantitative model output",
        "evidence_source": "Remote geotechnical model's 2.3 rating",
        "distinctiveness_requirement": "Must be based on numeric/model precision, distinct from iv_02's case-pattern basis"
      },
      {
        "instance_id": "iv_02",
        "bias": "Illusion of validity",
        "mechanism": "Overweighting predictive confidence from apparent similarity to a single past case",
        "affected_reasoning_operation": "Pattern-matching against historical precedent as validation",
        "evidence_source": "Stope 9 historical crack-pattern log",
        "distinctiveness_requirement": "Must be based on case-pattern coherence, distinct from iv_01's numeric-model basis; different decision point"
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective forwarding of belief-consistent crew reports while sidelining a dissenting inspector note",
        "affected_reasoning_operation": "Selective evidence transmission/weighting",
        "evidence_source": "Crew verbal reports vs. junior inspector's email",
        "distinctiveness_requirement": "Must be an evidence-selection/transmission act, distinct from cb_02's interpretation act; different decision point"
      },
      {
        "instance_id": "cb_02",
        "bias": "Confirmation Bias",
        "mechanism": "Interpreting an ambiguous new event (rock fall) as confirming a prior belief rather than as reason to reassess",
        "affected_reasoning_operation": "Belief-consistent interpretation of ambiguous evidence",
        "evidence_source": "Minor rock fall near stope access drift",
        "distinctiveness_requirement": "Must be an interpretation act on new evidence, distinct from cb_01's selective-transmission act; different decision point"
      },
      {
        "instance_id": "ob_01",
        "bias": "Overconfidence Bias",
        "mechanism": "Expressed high personal certainty in judgment despite unresolved sensor gap and unaddressed dissent",
        "affected_reasoning_operation": "Self-assessed confidence calibration under incomplete information",
        "evidence_source": "Manager's stated certainty vs. sensor lag and prior unresolved cautionary note",
        "distinctiveness_requirement": "Sole overconfidence instance; must be framed as self-certainty, not evidence interpretation"
      },
      {
        "instance_id": "ab_01",
        "bias": "Availability Bias",
        "mechanism": "Risk judgment anchored to one vivid, easily recalled past event rather than base-rate data",
        "affected_reasoning_operation": "Risk judgment via recall salience",
        "evidence_source": "Recalled Stope 9 event from six weeks prior",
        "distinctiveness_requirement": "Sole availability instance; must be recall-driven, distinct from iv_02's case-pattern illusion-of-validity framing"
      }
    ],
    "intended_strength": [
      {"instance_id": "sqb_01", "bias": "Status quo bias", "strength": "subtle"},
      {"instance_id": "iv_01", "bias": "Illusion of validity", "strength": "moderate"},
      {"instance_id": "iv_02", "bias": "Illusion of validity", "strength": "moderate"},
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Confirmation Bias", "strength": "subtle"},
      {"instance_id": "ob_01", "bias": "Overconfidence Bias", "strength": "moderate"},
      {"instance_id": "ab_01", "bias": "Availability Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_7",
    "domain_id": "MU",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across decision points by mechanism fit and narrative realism: status quo bias placed solely at the initial anomaly-response decision (DP1); illusion of validity split between a numeric-model-trust manifestation (DP2) and a case-pattern-coherence manifestation (DP3) to ensure distinct evidence sources; confirmation bias split between a selective-transmission manifestation (DP3) and a belief-consistent-interpretation manifestation (DP4) to ensure distinct reasoning operations; overconfidence and availability bias each assigned a single instance at the decision points (DP4 and DP2 respectively) where personal certainty and recalled-precedent reasoning are most narratively plausible. No bias exceeds two occurrences at any single decision point, and no two occurrences of the same bias share both decision point and evidence source.",
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
