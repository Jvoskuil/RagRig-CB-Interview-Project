You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for sitting down for this. This is voluntary, and I'm interested in your reasoning process, not in re-grading your final report. Can you give me your role and background?

Participant: Sure. Certified fire investigator, IAAI-CFI, eleven years doing origin and cause, mostly commercial buildings. Six years on suppression before that.

Interviewer: Good. Tell me about the incident. What did you see and hear when you first arrived?

Participant: Two-story mixed-use building—café downstairs, apartment above. Fire was already knocked down. The rear of the ground floor, dry storage plus part of the kitchen, had a partial ceiling collapse. The electrical panel sat on the wall maybe eight feet from the fryer exhaust duct. Suppression crew said they hit heavy smoke logging before they even got through the back door, so it had clearly been burning a while in low oxygen before anyone noticed. That matters because ventilation-limited burning smears your pattern reading—you don't get one clean V-pattern pointing at a single spot. The whole back room was charred fairly evenly, top to bottom, which made the visual read genuinely hard.

Interviewer: What was your objective going in?

Participant: Defensible origin and cause, NFPA 921 methodology, systematic elimination of ignition sources, all documented well enough to survive insurer and possibly legal scrutiny. And we had the clock running—48 hours before the demolition permit kicked in.

Interviewer: Walk me through the sequence, start to finish.

Participant: Scene photography and assessment first. Then excavation, starting in the rear zone since that's where the damage was worst. Within that zone I had to pick which side to dig into first, panel or fryer. Then witness statements came in and I had to fold those into a timeline that didn't quite match the dispatch log. Then a hard resource call—only one component could go out for full lab testing before demolition. And finally the report had to go out with whatever I had, on deadline.

Interviewer: Let's take the excavation order first. What led you to start where you did?

Participant: The panel breaker had visually severe heat damage, that's true. But honestly, what really settled it for me was that this whole setup—panel right next to a grease-heavy kitchen zone, older wiring—reminded me hard of a case I worked maybe four years back where a corroded panel connection took out a similar back-of-house area. That case stuck with me. So when I saw this layout, my gut said panel, and I went with the panel side first.

Interviewer: Even though the fryer wiring showed comparable damage and that zone had a higher fuel load and heavier daily use?

Participant: Yeah, and if you'd asked me to lay it out purely on the numbers—damage severity, fuel load, use frequency—it's closer than I probably made it sound at the time. But it felt like the same shape of fire I'd already solved once, so panel got my attention first. I'll grant that's not purely evidence-driven; it's partly this one felt familiar.

Interviewer: Let's move to the witness accounts. What exactly did the tenant tell you?

Participant: She said she smelled an electrical, burning-plastic odor about twenty minutes before she saw flame—and she also mentioned catching a flicker, like a spark, near where the panel is, before the smell really set in. That's a strong data point pointing at the panel.

Interviewer: I want to check that against what you told me earlier, when we first logged her statement—you described it then as smell only, no visual detail. Can you help me reconcile that?

Participant: Huh. You're right, that's how I noted it initially—smell only. I'm... now second-guessing whether she actually said "flicker" to me directly, or whether that's something I pieced together afterward from the panel damage and just started saying it as if she'd told me. It's possible I filled that in without meaning to. I don't think I did it on purpose, but sitting here, I can't swear the flicker detail came from her and not from my own read of the scene.

Interviewer: That's helpful to flag. How did the employee's account factor in?

Participant: He said the fryer had been left on, unattended, longer than usual before closing. Neither his estimate nor the tenant's matched the 911 log precisely—people misjudge time under stress, that's normal. I logged both as provisional. I didn't have a strong basis to fully trust one over the other independent of physical evidence.

Interviewer: Third decision point—the lab retention call, since you could only send one component out.

Participant: Right, demolition was scheduled, budget only covered one full forensic workup. Panel breaker or fryer control assembly. The utility inspector had given me an informal, not-yet-written read that leaned panel. I weighed that against the fryer component's condition, which was also degradable enough to still be informative. I picked the panel breaker. I considered asking for a deadline extension to save both, but the insurer pushed back hard, and waiting risked losing both to further collapse anyway.

Interviewer: What would have made you send the fryer assembly instead?

Participant: Clear independent radiating burn patterns from the appliance itself. It wasn't a toss-up, but it wasn't locked in either.

Interviewer: Last point—the final classification under deadline.

Participant: With no new evidence coming and the clock out, I had three options: determinate finding, undetermined pending lab results, or a conditional finding naming both with relative likelihood. I went conditional—panel fault primary, fryer malfunction as a documented secondary possibility. A hard determinate call felt premature since the fryer possibility wasn't eliminated, and "undetermined" felt like it undersold the direction the pattern evidence and the inspector's preliminary read were pointing.

Interviewer: What single piece of missing evidence would have most changed your confidence?

Participant: Independent lab results on both components. Losing the fryer assembly to demolition is the one thing I'd redo—push harder for even partial preservation.

Interviewer: If the witness timestamps had matched the dispatch log exactly, would your timeline weighting have differed?

Participant: Probably, yeah—I'd have leaned into whichever account lined up and trusted it more as an anchor point instead of treating both as soft.

Interviewer: How much of your final call would you attribute to prior cases versus this case's own evidence?

Participant: I'd like to say it was mostly this case. Looking back at how I've described a couple of these steps to you, though, I think the prior case did more work in my head than I'd have said if you'd asked me that on day one—especially early on, before the excavation even really got going.

Interviewer: Anything you'd flag for someone reviewing this file cold?

Participant: That the ambiguity was real, and that at least one detail I reported to you about the tenant's statement needs to be double-checked against her actual recorded interview before it goes in the file as fact.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "False memory",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a confidently recalled perceptual detail attributed to a witness that contradicts the originally documented content of that witness's statement, surfaced during timeline reconstruction."
      },
      {
        "bias": "Familiarity bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as reliance on resemblance to a remembered prior case as a leading justification for an evidence-sequencing decision, outweighing present-case comparative evidence."
      }
    ],
    "target_bias_names": [
      "False memory",
      "Familiarity bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "False memory",
        "requested_occurrences": 1
      },
      {
        "bias": "Familiarity bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias"
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias",
        "decision_point": 1
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias",
        "mechanism": "Excavation-sequencing choice justified primarily by resemblance to a remembered prior panel-fire case rather than by present-case comparative evidence weight between panel and fryer zones.",
        "affected_reasoning_operation": "Evidence-weighting and prioritization for zone-excavation order",
        "evidence_source": "Comparative physical damage and fuel-load evidence between panel and fryer zones, contrasted with an autobiographically recalled prior case",
        "distinctiveness_requirement": "Must be identifiable as resemblance-driven justification outweighing present-case evidence, not merely a mention of relevant professional experience used to interpret current evidence."
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory",
        "mechanism": "Confident recall of a visual detail (flicker/spark) attributed to the tenant's statement during timeline reconstruction, contradicting the smell-only content of her originally documented statement established earlier in the interview.",
        "affected_reasoning_operation": "Memory retrieval and integration of witness evidence into the working timeline",
        "evidence_source": "Originally documented tenant statement (smell only) versus the participant's later recollection (smell plus visual flicker/spark)",
        "distinctiveness_requirement": "Must be identifiable as an added detail inconsistent with the earlier-established record, not a vague paraphrase or a reasonable inferential gloss on the same content."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias",
        "strength": "subtle"
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": "HE_Ambigious_2",
    "counterfactual_variable": {
      "name": "presence_of_remembered_similar_prior_case",
      "original_state": "Investigator has a readily available memory of a superficially similar prior panel-fire case at the time of the excavation-sequencing decision.",
      "changed_state": "Investigator has no such prior case readily in mind and relies solely on present-case comparative evidence.",
      "variables_to_hold_constant": [
        "Building layout and fire damage pattern",
        "Witness statements and their original content",
        "Resource and deadline constraints",
        "Component-retention and final-classification decisions"
      ]
    },
    "scenario_id": "HE_Biased_2",
    "domain_id": "HE",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias (occurrences=1) was assigned exactly one instance ID and placed at a distinct decision point selected for mechanism fit and narrative realism: familiarity bias at decision point 1 (zone-sequencing choice, where recollection of a similar prior case is a natural expert-judgment trigger point) and false memory at decision point 2 (witness-timeline reconstruction, where memory retrieval and integration of secondhand accounts is the operative reasoning act). No decision point received more than one instance of the same bias, satisfying the spread and mechanism-fit rules.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Building layout, fire damage pattern, and physical evidence distribution",
      "Four-decision-point structure and sequencing",
      "Stakeholder cast and dialogue tone",
      "Time-pressure and resource-constraint framing",
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
