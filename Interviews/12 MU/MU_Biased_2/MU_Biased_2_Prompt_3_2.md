You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{**Interviewer:** Thanks for making time for this. Just to confirm, this is a voluntary debrief for our internal learning review, not a disciplinary process — anything you share helps us understand decision-making under uncertainty, not to assign blame. Can you start by telling me your role and what you were responsible for during this incident?

**Participant:** Sure. I'm the ground control specialist for the site — geotech engineer by training. I cover support design, monitoring interpretation, and sign-off on ground conditions for active headings. During this shift I was working from the surface office but on call for anything flagged at the 4200 development face and the adjacent bolted heading next to it.

**Interviewer:** Good. Before we get into specifics, can you give me a general account of what happened, start to finish?

**Participant:** It started with a call from the shift boss — minor rib spalling near the 4200 face, right after a blast, with a bit of dust puffing off the wall. Nobody was hurt, the crew actually paused on their own, which I give them credit for. Our extensometer near that face had been down for about two days — the bolting rig had knocked the cable loose — so I didn't have fresh convergence numbers for that specific spot. I authorized them to keep mucking with a visual check, because honestly this looked a lot like something we'd seen at the 3800 panel about six months back, where the cause turned out to be the operator undercutting too aggressively on the bottom of the round.

A bit later the scaling crew called in with bigger slabs than first described, plus a hairline fracture pattern we hadn't logged before. We're roughly fifteen to twenty meters from a mapped fault splay there, though the exact position is fuzzy — exploration drilling only gives you so much. I ran our convergence model using the nearest working stations, which weren't right at the face, and it came back with a low displacement forecast. That gave me enough to let the round finish.

After the round, spalling showed up in the adjacent bolted heading too. The shift boss asked if we should mesh and bolt before the next rotation, and the mine manager reminded me that would blow our weekly advance number. I held off. A couple hours later a crack opened along a bolt row in that heading. Technician wanted an immediate evacuation. I let a short monitored entry happen instead. Not long after, we had a larger fall in that section. No one was hurt — an unrelated alarm actually cleared people out just before it happened — but it could have gone differently.

**Interviewer:** Let's reconstruct the timeline a bit more precisely. What exactly did you know at the moment of that first call?

**Participant:** Just the spalling, the dust, no injuries, crew stopped on their own initiative. And that our monitoring near that face was blind because of the extensometer outage.

**Interviewer:** And after the scaling crew's second report?

**Participant:** That's when the picture got more complicated — bigger slabs, a fracture pattern, and the fault splay proximity became more relevant in my head.

**Interviewer:** When did you first pull up the convergence model output, and what did you do with it?

**Participant:** Right after that second report. I wanted something more than visual judgment before letting the round finish.

**Interviewer:** Walk me through the gap between finishing the round and the evacuation call.

**Participant:** Round finished, spalling in the adjacent heading came up, I deferred the support order, then the crack appeared maybe two hours later, and the technician pushed for evacuation almost immediately after that.

**Interviewer:** Let's go through the first decision — authorizing continued mucking. What alternatives did you weigh?

**Participant:** I could've stopped everything for a full inspection, or restricted a buffer zone and resequenced the round. I chose the visual-check option.

**Interviewer:** What made the 3800 comparison feel relevant enough to lean on here?

**Participant:** The symptoms looked similar — spalling right after a blast cycle. At 3800 we'd traced that to the operator undercutting on the bottom of the round, and once that case was in my head, my first read here was that we were probably looking at something similar — a shallow, crew-induced spall out of the cut or cleanup sequence, not necessarily anything structural. I didn't actually have anything from this round confirming that; it was more that the 3800 case gave me a ready-made explanation to reach for.

**Interviewer:** Did the missing extensometer data factor into that judgment?

**Participant:** Honestly, less than it should have. Once I'd settled on the crew-sequence explanation, the monitoring gap felt like a secondary concern rather than something that should have pushed me toward taking the geological angle more seriously.

**Interviewer:** Second decision — using the convergence model output to justify finishing the round. How did you decide it applied here?

**Participant:** That model's been solid for us — it called ground behavior accurately on a panel we ran last year. So when it came back low-displacement, I trusted that read.

**Interviewer:** The technician mentioned a calibration concern. Can you describe that?

**Participant:** She said the model was built on data from a different rock mass domain and might not transfer well this close to the fault splay. I heard her, but between the track record and the schedule pressure, I went with the output as it stood.

**Interviewer:** Third decision — deferring the supplemental support order. What was the basis?

**Participant:** The model's forecast was still sitting there as stable, so nothing had come in that reset the picture I already had. I treated it as the same authorization carrying forward from the face decision, rather than reopening the question, and the manager had flagged the schedule impact on top of that. I was planning to revisit support once we had updated readings from that heading.

**Interviewer:** What would have changed that decision?

**Participant:** Fresh convergence readings right at that heading, honestly. Or if the crack had shown up before I made the call instead of after.

**Interviewer:** Fourth decision — allowing the brief entry after the crack appeared. What was your reasoning?

**Participant:** I didn't have a fresh geotechnical read on the crack itself — nobody had run a new assessment specific to it — so I was essentially still operating inside the decision I'd made earlier in the shift. Given the timeline we were on, I opted for a short, monitored entry instead of a full lockout, treating it as a controlled check on an open question rather than something I'd already settled one way or the other.

**Interviewer:** How much did time pressure factor into that specific call?

**Participant:** A fair amount. The next crew was due within the hour, and stopping everything again would have meant a second schedule hit in one shift.

**Interviewer:** Looking back, if the extensometer had been working the entire time, do you think your decisions would have gone differently?

**Participant:** Probably, at least at the first and third points. Real numbers instead of an analogy might have shifted things earlier.

**Interviewer:** And if the 3800 investigation had reached a different conclusion at the time — say it had been traced to unanticipated stress redistribution near a geological structure instead of the operator's undercutting, with everything else about that case the same — do you think you'd have read this situation differently, given the same monitoring outage and schedule pressure you actually had?

**Participant:** Probably, yeah. If that case had taught me to expect a geological cause behind those symptoms, I think I'd have leaned harder on the fault-splay possibility from the first report, instead of defaulting to a crew-sequence explanation, even with the same blind spot on the extensometer and the same push to keep the round moving.

**Interviewer:** Last one — what would you do differently if a similar sequence came in again?

**Participant:** Push harder to get monitoring restored before trusting any model output, and probably treat a new fracture pattern as its own signal rather than folding it into a story that already made sense to me.

**Interviewer:** That's really helpful detail. Thanks for walking through it so openly.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Attribution Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dispositional (operator-technique) causal attribution of current spalling, anchored to a prior analogous incident attribution, over situational (ground-stress) attribution, at decision point 1 only."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overconfidence in the convergence model's forecast based on past track record, despite acknowledged domain mismatch, at decision point 2 only."
      }
    ],
    "target_bias_names": ["Attribution Bias", "Illusion of validity"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Illusion of validity", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "attr_01", "bias": "Attribution Bias" },
      { "instance_id": "iov_01", "bias": "Illusion of validity" }
    ],
    "intended_decision_points": [
      { "instance_id": "attr_01", "bias": "Attribution Bias", "decision_point": 1 },
      { "instance_id": "iov_01", "bias": "Illusion of validity", "decision_point": 2 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "mechanism": "Dispositional (operator-error) causal attribution of ambiguous ground behavior, anchored to a prior analogous case the engineer personally attributed to operator error, over situational (geological) attribution",
        "affected_reasoning_operation": "Causal attribution under incomplete evidence at the point of authorizing continued mucking",
        "evidence_source": "Shift boss's spalling/dust report combined with the engineer's own prior 3800 incident report",
        "distinctiveness_requirement": "Must be the only instance of dispositional-over-situational causal misattribution in the interview; must occur at decision point 1 and not be repeated in later decision points, probes, or the closing hypotheticals as a separate instance."
      },
      {
        "instance_id": "iov_01",
        "bias": "Illusion of validity",
        "mechanism": "Confidence in a predictive model's output derived from its past track record and internal coherence, unadjusted for an acknowledged domain mismatch (different rock mass calibration) and sparse current data",
        "affected_reasoning_operation": "Confidence calibration when interpreting the convergence model's forecast at decision point 2",
        "evidence_source": "Convergence model output using non-adjacent station data, plus technician's verbal domain-mismatch caveat",
        "distinctiveness_requirement": "Must be the only instance of unwarranted forecast confidence in the interview; occurs at decision point 2; later reliance on the same stale model output at decision points 3 and 4 must be narrated as a consequence of this single occurrence, not as additional independent instances."
      }
    ],
    "intended_strength": [
      { "instance_id": "attr_01", "bias": "Attribution Bias", "strength": "subtle" },
      { "instance_id": "iov_01", "bias": "Illusion of validity", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Causal framing of the engineer's prior 3800 incident attribution (operator error vs. ground stress)",
      "original_state": "Attributed to operator's aggressive undercutting technique",
      "changed_state": "Attributed to unanticipated stress redistribution near a geological structure",
      "variables_to_hold_constant": [
        "Production schedule pressure",
        "Extensometer outage near the 4200 face",
        "Convergence model's domain mismatch",
        "Sequence and content of the four decision points",
        "Scaling crew and technician reports",
        "Final roof fall outcome"
      ]
    },
    "scenario_id": "MU_Biased_2",
    "domain_id": "MU",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias assigned to a distinct decision point (attribution bias at decision point 1, illusion of validity at decision point 2) based on mechanism fit: attribution bias fits the earliest causal-interpretation moment, illusion of validity fits the model-reliance moment; subsequent decision points (3 and 4) narrate downstream consequences of these same two instances without introducing new independent instances.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Production schedule pressure",
      "Extensometer outage near the 4200 face",
      "Convergence model's domain mismatch",
      "Sequence and content of the four decision points",
      "Scaling crew and technician reports",
      "Final roof fall outcome"
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
