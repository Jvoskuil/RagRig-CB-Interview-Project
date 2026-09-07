You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{**Interviewer:** Thanks for making time for this. Just to confirm, this is a voluntary debrief for our internal learning review, not a disciplinary process — anything you share helps us understand decision-making under uncertainty, not to assign blame. Can you start by telling me your role and what you were responsible for during this incident?

**Participant:** Sure. I'm the ground control specialist for the site — geotech engineer by training. I cover support design, monitoring interpretation, and sign-off on ground conditions for active headings. During this shift I was working from the surface office but on call for anything flagged at the 4200 development face and the adjacent bolted heading next to it.

**Interviewer:** Good. Before we get into specifics, can you give me a general account of what happened, start to finish?

**Participant:** It started with a call from the shift boss — minor rib spalling near the 4200 face, right after a blast, with a bit of dust puffing off the wall. Nobody was hurt, the crew paused on their own. Our extensometer near that face had been down for about two days — the bolting rig had knocked the cable loose — so I didn't have fresh convergence numbers for that specific spot. That gap mattered to me; I flagged it as something we'd need to close before I could really trust any read on that area. I also had the 3800 panel in the back of my mind — a similar-looking spalling event about six months earlier that we'd traced to aggressive undercutting by the operator at the time. But I didn't want to lean on that too hard, since one analogy from a different crew and a different round doesn't tell you much about stress conditions here. I authorized continued mucking with a visual check, treating both the operator-technique angle and the possibility of something geological as open questions.

A bit later the scaling crew called in bigger slabs than first described, plus a hairline fracture pattern we hadn't logged. We're roughly fifteen to twenty meters from a mapped fault splay there, though the exact position is fuzzy. I ran our convergence model using the nearest working stations, which weren't right at the face. It came back with a low displacement forecast, but the technician reminded me the model's calibration came from a different rock mass domain, so I didn't take the number at face value — I discounted it and tied continuing the round to a specific follow-up scaling check afterward.

After the round, spalling showed up in the adjacent bolted heading too. The shift boss asked about mesh and bolts before the next rotation, and the mine manager flagged the schedule hit. I treated the second location as new information rather than just an extension of what I already believed, so I ordered spot bolts at the fracture and a targeted scaling check instead of either a full upgrade or a full deferral. A couple hours later a crack opened along a bolt row. The technician wanted immediate evacuation. I authorized a restricted, technician-accompanied entry instead of routine access, since I didn't think the crack could just be read as more of the same. Not long after, we had a larger fall in that section. No one was hurt — an unrelated alarm cleared people out just before it happened — but it could have gone differently.

**Interviewer:** Let's reconstruct the timeline a bit more precisely. What exactly did you know at the moment of that first call?

**Participant:** Just the spalling, the dust, no injuries, crew stopped on their own. And that our monitoring near that face was blind because of the extensometer outage — that was very much on my mind, not something I set aside.

**Interviewer:** And after the scaling crew's second report?

**Participant:** That's when the picture got more complicated — bigger slabs, a fracture pattern, and the fault splay proximity became more relevant. It pushed me to actually run the model rather than rely on judgment alone.

**Interviewer:** When did you first pull up the convergence model output, and what did you do with it?

**Participant:** Right after that second report. I wanted a second line of evidence, but I went in already expecting to have to adjust for the domain mismatch.

**Interviewer:** Walk me through the gap between finishing the round and the evacuation call.

**Participant:** Round finished, spalling in the adjacent heading came up, I ordered the spot check rather than closing the question either way, then the crack appeared maybe two hours later, and the technician pushed for evacuation almost immediately after that.

**Interviewer:** Let's go through the first decision — authorizing continued mucking. What alternatives did you weigh?

**Participant:** Stopping everything for a full inspection, or restricting a buffer zone and resequencing the round. I went with the visual-check option, but I didn't treat it as a closed case.

**Interviewer:** How did you weigh the 3800 comparison against the missing extensometer data?

**Participant:** I tried to hold both at once. The 3800 case gave me one plausible read, but the missing monitoring meant I genuinely didn't know what the ground was doing locally, and I didn't want that gap to just disappear because I had a tidier story available. I made a point of telling the shift boss I wanted that extensometer back online as soon as the rig work allowed.

**Interviewer:** Second decision — using the convergence model output to justify finishing the round. How did you decide how much weight to give it?

**Participant:** Given the domain mismatch the technician flagged, I didn't treat the low-displacement number as decisive on its own — more as one data point that shifted my confidence somewhat, conditional on a scaling check afterward. If that check had come back worse, I'd have stopped regardless of what the model said.

**Interviewer:** What was the technician's concern, specifically, and how did you incorporate it?

**Participant:** She said the model's calibration came from a different rock mass domain and might not transfer well this close to the fault splay. I built that into how much I let the forecast move my decision — I leaned on it less than I would have on a panel where I trusted the calibration fit.

**Interviewer:** Third decision — the adjacent heading. What led you to the spot-check option rather than a full upgrade or a full deferral?

**Participant:** The new location mattered to me — it wasn't just the same spalling showing up again, it was a second area behaving in a way the earlier forecast hadn't covered. A full deferral felt like ignoring that; a full upgrade felt premature without more specific data on where the fracture actually was. The spot bolts and scaling check were a way to act on the new information without overcommitting either direction.

**Interviewer:** What would have changed that decision?

**Participant:** Fresh convergence readings right at that heading, or if the crack had shown up before I made the call instead of after.

**Interviewer:** Fourth decision — allowing entry after the crack appeared. What was your reasoning?

**Participant:** The model hadn't been rerun with the crack data, so I didn't extend the earlier forecast to cover it — that felt like a different question. I authorized a restricted entry with the technician present rather than routine access, treating the crack as something we still needed to understand rather than something already explained by what we'd seen at the face.

**Interviewer:** How much did time pressure factor into that specific call?

**Participant:** A fair amount. The next crew was due within the hour, and a full lockout would have meant a second schedule hit in one shift. That pressure was real, but it's why I restricted the entry rather than just clearing it outright.

**Interviewer:** Looking back, if the extensometer had been working the entire time, do you think your decisions would have gone differently?

**Participant:** Probably at the first and third points especially. Real numbers instead of partial analogies and adjusted model output would have given me something firmer to act on earlier.

**Interviewer:** And if the 3800 investigation had reached a different conclusion — say it had been traced to stress redistribution near a geological structure instead of operator technique — do you think you'd have read this situation differently?

**Participant:** Maybe somewhat, but I'd hope I'd still have tried to treat it as one data point rather than the deciding factor, given how different the local conditions were here.

**Interviewer:** Last one — what would you do differently if a similar sequence came in again?

**Participant:** Push even harder to get monitoring restored before any round decision, and probably formalize the follow-up conditions I attach to model output, rather than keeping them informal in my own head.

**Interviewer:** That's really helpful detail. Thanks for walking through it so openly.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Attribution Bias",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended instances. Decision point 1 reasoning must explicitly balance dispositional (operator-technique) and situational (ground-stress) explanations rather than defaulting to either without examination."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended instances. Decision point 2 reasoning must explicitly discount the convergence model's forecast for the acknowledged domain mismatch and attach a concrete follow-up condition rather than treating the forecast as sufficient on its own."
      }
    ],
    "target_bias_names": ["Attribution Bias", "Illusion of validity"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Attribution Bias", "requested_occurrences": 0 },
      { "bias": "Illusion of validity", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MU_Biased_2",
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "changed_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Vocab_Control_2",
    "domain_id": "MU",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "No occurrences allocated. Vocabulary-control condition requires zero intended instances of both named biases at all four decision points; the paired biased scenario's decision-point structure, evidence types, and vocabulary are matched while the reasoning at each decision point is rewritten to explicitly weigh competing explanations and explicitly qualify model confidence, removing the mechanisms that would otherwise instantiate the target biases.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Underground hard-rock mining setting and role (geotechnical engineer / ground control specialist)",
      "Stakeholder set (shift boss, contractor operator, mine manager, ground control technician)",
      "Four-decision-point chronological structure and incident skeleton",
      "Production schedule pressure and its narrative placement",
      "Extensometer outage near the 4200 face",
      "Fault splay proximity and positional uncertainty",
      "Convergence model's domain mismatch as a known, acknowledged fact",
      "Prior 3800 incident as a referenced case with the same stated operator-undercutting cause",
      "Final roof fall outcome and the unrelated-alarm evacuation detail",
      "Probe categories and approximate probe density",
      "Target word count and difficulty level"
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
