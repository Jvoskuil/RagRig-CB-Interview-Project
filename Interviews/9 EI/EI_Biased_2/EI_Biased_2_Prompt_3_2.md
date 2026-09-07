You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is for our instructional practice research and will be handled confidentially. Can you start by telling me your role and how the Bridge Literacy pilot came about?

Participant: Sure. I'm the Curriculum Coordinator for K-5, and I also run our instructional coaching cycle across the elementary buildings. I brought Bridge Literacy in after seeing it presented at a state conference last spring. It's a structured literacy approach, more explicit phonics sequencing than what we'd been using. I pitched it to the superintendent, and we set it up as a trimester pilot in six classrooms across our two elementary schools.

Interviewer: And what were you trying to accomplish with the checkpoint review you did partway through?

Participant: The board needed a scale-up recommendation before the next budget cycle, so I had to look at the trimester oral reading fluency benchmark data, figure out if the pilot was working, and decide what to tell the finance committee. There's real competition for dollars — the math intervention team wants the same PD budget — so whatever I brought needed to be solid.

Interviewer: Walk me through what happened when the data actually came in.

Participant: The literacy specialist sent me the classroom-level fluency results in early February. Three classrooms were clearly above the expected growth rate, three were flat or just mixed. My first reaction was — okay, this is a real pilot, we're going to have variation. But when I looked closer at the three flat classrooms, I noticed the testing had happened on different days at the two schools because of a scheduling conflict. That felt like something worth flagging. I asked the specialist to check whether that timing gap could explain the flat results.

Interviewer: Did you look at the testing conditions in the classrooms that showed gains too?

Participant: Not in the same way, no. Those looked like the program was doing what we hoped, so I didn't feel the same urgency to dig into how the testing was administered there. In hindsight, the scheduling issue technically applied across the whole window, not just to certain rooms, but at the time my attention went to the classrooms where the results didn't match what I expected.

Interviewer: What did you learn afterward?

Participant: The specialist came back about a week later and said the testing conditions were actually pretty similar across all six classrooms — the day-to-day difference wasn't significant. And separately, one of the flat classrooms had unusually high absenteeism that same week, which probably mattered more than timing.

Interviewer: When you were deciding how much scrutiny to apply, what alternatives did you consider?

Participant: I could have treated all six the same way from the start — same level of questioning regardless of outcome. Or waited for the specialist to audit everything before drawing any conclusions. I didn't do either of those first. I went straight to questioning the ones that weren't showing growth.

Interviewer: Let's move to the board meeting prep. What did that involve?

Participant: I had fifteen minutes on the agenda, and the math team was presenting right after me. I had the six-classroom fluency numbers plus a walkthrough-observation log the specialist and I had been keeping. I decided to bring a highlights slide with the aggregate trend line rather than all six classrooms individually — mostly a time issue, honestly. Fifteen minutes isn't enough to walk through six separate data profiles and still leave room for questions.

Interviewer: Any consequence from that choice?

Participant: One board member asked for classroom-by-classroom detail I hadn't included. I had the numbers on hand, just not on the slide, so I was able to answer, but it did mean I was talking through figures I hadn't rehearsed presenting.

Interviewer: Around the same time, you had PD feedback to review. What did that look like?

Participant: Five of six pilot teachers filled out a survey after the coaching session, rated it helpful or very helpful. One comment mentioned the pacing guide felt rushed for lower-performing students. It's a small sample and it was voluntary, so I noted that caveat when I summarized it — I didn't want to present five responses as if that settled anything about how teachers overall felt.

Interviewer: Did you follow up on the one teacher who didn't respond?

Participant: Not right away. The specialist later mentioned that two of the non-responses were actually invitations that went to teachers in the flat classrooms, which made me wonder if we were mostly hearing from teachers who were already seeing good results. I flagged that as a limitation rather than treating the survey as fully representative.

Interviewer: Let's get to the recommendation memo. How did you explain the fluency gains?

Participant: The aggregate number was a modest net gain across all six classrooms. I'd been doing biweekly coaching visits in four of the six rooms all trimester — modeling lessons, giving feedback, that kind of thing. When I wrote the memo, I framed the gains as largely a product of that coaching cycle, and I recommended that if we scale up, we'd need to replicate that same coaching frequency districtwide, which means adding coaching staff.

Interviewer: What about the two classrooms that improved without your direct coaching visits?

Participant: They did show gains too, yes. I mentioned the new decodable-text materials and the smaller class sizes in a line or two, but the core of the recommendation centered on the coaching model, since that's the piece I could speak to most directly and the piece I think drove the results I was seeing week to week.

Interviewer: A board member raised that point later, is that right?

Participant: Right, someone pointed out afterward that the two non-visited classrooms also improved, and asked how that fit with a coaching-centered explanation. I said we'd need more study to fully untangle it, but I still think the coaching cycle was the biggest lever.

Interviewer: What would have needed to be different for you to weight materials or class size more heavily in that memo?

Participant: Probably if I'd had the detailed classroom-by-classroom comparison — matching each room's growth to whether I'd coached it, plus the materials and class-size notes — pulled together before I drafted, instead of after I'd already sent the memo in. I had the aggregate fluency numbers going into the writing, but that side-by-side breakdown didn't come together until later. I was writing under deadline, and the coaching piece was what I had the most direct visibility into.

Interviewer: If someone else had gotten these same results without your involvement, how do you think you'd have explained the gains?

Participant: That's fair to ask. I'd probably have looked harder at the materials and class-size differences if I weren't the one who ran the coaching. I don't think I was ignoring those factors on purpose, but they weren't the first thing I reached for.

Interviewer: And if the classrooms that struggled had been the ones you were personally coaching, do you think you'd have scrutinized the testing conditions the same way?

Participant: Probably not as much, no. I think I'd have wanted an explanation either way, but I might not have gone looking for one as quickly if the numbers had gone the way I expected from the start.

Interviewer: Looking back, what would you do differently if you ran this checkpoint again?

Participant: I'd ask the specialist to review testing conditions across every classroom at the same time, before I form an impression of which ones look right. And I'd probably pull together the full classroom-by-classroom comparison before I draft the causal explanation in the memo, not partway through.

Interviewer: That's really helpful context. Thank you for walking through this in detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Biased Assimilation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as asymmetric methodological scrutiny of disconfirming vs. confirming classroom data at decision point 1"
      },
      {
        "bias": "Egocentric bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overattribution of shared outcome to coordinator's personal coaching contribution at decision point 4"
      }
    ],
    "target_bias_names": [
      "Biased Assimilation",
      "Egocentric bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Biased Assimilation",
        "requested_occurrences": 1
      },
      {
        "bias": "Egocentric bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation"
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation",
        "decision_point": 1
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation",
        "mechanism": "Asymmetric methodological scrutiny applied to disconfirming classroom fluency data relative to confirming data, driven by prior favorable belief in the program",
        "affected_reasoning_operation": "Evidence evaluation / evidentiary weighting",
        "evidence_source": "Trimester oral reading fluency benchmark results across six classrooms plus testing-schedule discrepancy note",
        "distinctiveness_requirement": "Only occurrence of this bias; must occur at decision point 1 and must not be repeated as a summary or restated elsewhere in the interview"
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias",
        "mechanism": "Overweighting of own coaching involvement as the primary cause of a multi-factor outcome, underweighting co-occurring factors and disconfirming detail about non-visited classrooms",
        "affected_reasoning_operation": "Causal attribution",
        "evidence_source": "Aggregate fluency gain data, classroom-level coaching-visit records, materials and class-size differences across pilot classrooms",
        "distinctiveness_requirement": "Only occurrence of this bias; must occur at decision point 4 and must not be repeated as a restated causal claim elsewhere in the interview"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation",
        "strength": "subtle"
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias",
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
    "scenario_id": "EI_Biased_2",
    "domain_id": "EI",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread across distinct decision points (DP1 for Biased Assimilation, DP4 for Egocentric bias) based on mechanism fit: DP1 involves initial evidence evaluation of mixed pilot data, well-suited to asymmetric-scrutiny assimilation; DP4 involves final causal attribution of outcomes, well-suited to self-referential overweighting. DP2 and DP3 retained as neutral decision points to preserve narrative realism and avoid overloading any single phase with bias content.",
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
