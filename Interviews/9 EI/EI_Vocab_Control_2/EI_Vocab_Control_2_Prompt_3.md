You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. This is for our instructional practice research and will be kept confidential. Can you start by telling me your role and how the Bridge Literacy pilot came about?

Participant: Sure. I'm the Curriculum Coordinator for K-5, and I also run our instructional coaching cycle across the elementary buildings. I brought Bridge Literacy in after seeing it presented at a state conference last spring. It's a structured literacy approach, more explicit phonics sequencing than what we'd been using. I pitched it to the superintendent, and we set it up as a trimester pilot in six classrooms across our two elementary schools.

Interviewer: And what were you trying to accomplish with the checkpoint review you did partway through?

Participant: The board needed a scale-up recommendation before the next budget cycle, so I had to look at the trimester oral reading fluency benchmark data, figure out if the pilot was working, and decide what to tell the finance committee. There's real competition for dollars — the math intervention team wants the same PD budget — so whatever I brought needed to hold up under questions.

Interviewer: Walk me through what happened when the data actually came in.

Participant: The literacy specialist sent me the classroom-level fluency results in early February. Three classrooms were clearly above the expected growth rate, three were flat or mixed. Before I drew any conclusions, I asked her to check something that had been bothering me — the two schools had administered the benchmark on different days because of a scheduling conflict, and I wanted to know whether that gap could be distorting results anywhere, not just in the classrooms that happened to come in flat.

Interviewer: Why did you want it checked across all six rather than just the ones that looked off?

Participant: Because the scheduling issue wasn't specific to any classroom — it applied to the testing window generally. If I only went looking for problems in the rooms with disappointing numbers, I'd have no way of knowing whether the same issue was quietly present in the rooms that looked fine. It seemed like the only fair way to trust the comparison.

Interviewer: What did you learn afterward?

Participant: The specialist came back about a week later and said testing conditions were actually pretty similar across all six classrooms — the day-to-day difference wasn't significant. Separately, she found that one flat classroom had unusually high absenteeism that same week, which probably explained more of that particular result than timing did.

Interviewer: What alternatives did you weigh before deciding how to handle the review?

Participant: I could have just accepted the gain classrooms and focused all my attention on explaining away the flat ones. Or waited entirely until a full audit was done before forming any impression. I went with checking everything at once instead, mostly because I didn't want to end up defending a number in front of the board that I hadn't actually stress-tested.

Interviewer: Let's move to the board meeting prep. What did that involve?

Participant: I had fifteen minutes on the agenda, and the math team was presenting right after me. I had the full six-classroom data set plus a walkthrough-observation log the specialist and I had been keeping. I decided to bring a highlights slide with the aggregate trend line rather than all six classrooms individually — mostly a time issue. Fifteen minutes isn't enough to walk through six separate data profiles and still leave room for questions.

Interviewer: Any consequence from that choice?

Participant: One board member asked for classroom-by-classroom detail I hadn't put on the slide. I had it on hand, just not formatted for presentation, so I was able to answer, but I was working from memory a bit more than I'd have liked.

Interviewer: Around the same time, you had PD feedback to review. What did that look like?

Participant: Five of six pilot teachers filled out a survey after the coaching session, rated it helpful or very helpful. One comment mentioned the pacing guide felt rushed for lower-performing students. It's a small sample and it was voluntary, so I noted that caveat when I summarized it — I didn't want to present five responses as if that settled anything about how teachers overall felt.

Interviewer: Did you follow up on the teacher who didn't respond?

Participant: Not immediately. The specialist later mentioned the one non-response was from a teacher in a flat classroom, which made me wonder whether we were hearing a slightly rosier picture than the full group would give. I flagged that as a limitation in the write-up rather than treating the survey as representative.

Interviewer: Let's get to the recommendation memo. How did you explain the fluency gains?

Participant: The aggregate number was a modest net gain across all six classrooms. I'd been doing biweekly coaching visits in four of the six rooms, and those classrooms also had new decodable-text materials and, in a couple of cases, smaller class sizes than our typical rosters. When I wrote the memo, I tried to lay out all of that together rather than pointing to one piece — coaching, materials, and class size were all present at the same time in the classrooms that improved most.

Interviewer: What about the two classrooms that improved without your direct coaching visits?

Participant: That was actually one of the more useful data points. Those two rooms had the new materials too, and one of them had a smaller roster, so it suggested the materials and class-size piece might be doing real work independent of coaching. I included that in the memo as a reason to be cautious about crediting coaching alone.

Interviewer: A board member raised a related point, is that right?

Participant: Right, someone asked directly how those two classrooms improved without my visits. I said that was exactly why I was recommending a staged approach — bring in the materials and coaching together in a next round, but track classrooms with and without direct coaching support separately so we can actually see what's carrying the result before committing to a full districtwide coaching build-out.

Interviewer: What would have needed to be different for you to weight one factor more heavily than the others?

Participant: Probably a design where coaching, materials, and class size weren't all bundled together in the same rooms. Right now they move together, so I don't think the data lets anyone single one out with confidence. I said as much in the memo.

Interviewer: If someone else had gotten these same results without your involvement, how do you think they'd have explained the gains?

Participant: Probably about the same way I did — pointing at materials, class size, and coaching together, since all three were present. I don't think my being the one running the coaching changes what the data can and can't support.

Interviewer: And if the classrooms that struggled had been the ones you were personally coaching, do you think your review process would have looked any different?

Participant: I don't think so. I'd still have wanted the testing conditions checked everywhere before drawing conclusions — that part wasn't really about which rooms I was in.

Interviewer: Looking back, what would you do differently if you ran this checkpoint again?

Participant: I'd try to get the specialist's testing-condition review done earlier, before the board deadline was quite so close, so I'm not doing that verification under quite as much time pressure. And if we run another round of the pilot, I'd try to stagger which classrooms get coaching versus materials only, so the next causal story isn't as tangled as this one.

Interviewer: That's really helpful context. Thank you for walking through this in detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Biased Assimilation",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended occurrences; coordinator must apply uniform scrutiny to all classroom data regardless of outcome direction"
      },
      {
        "bias": "Egocentric bias",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended occurrences; coordinator must distribute causal credit across multiple contributing factors without centering personal contribution"
      }
    ],
    "target_bias_names": [
      "Biased Assimilation",
      "Egocentric bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Biased Assimilation",
        "requested_occurrences": 0
      },
      {
        "bias": "Egocentric bias",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "EI_Biased_2",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Vocab_Control_2",
    "domain_id": "EI",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control condition mandates zero intended instances of all named target biases regardless of any manifest occurrence counts supplied by the caller. The caller-supplied manifest (1 occurrence each of Biased Assimilation and Egocentric bias) is overridden to zero per the condition rules for vocabulary_control, and this override is recorded in generation_warnings.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Six-classroom, two-school pilot structure and trimester timeline",
      "Stakeholder roster and role of the Curriculum Coordinator",
      "Four-decision-point narrative structure and sequence",
      "Budget-competition, board-time, and testing-schedule constraints",
      "Emotional tone and overall narrative complexity",
      "Approximate interview length and probe category coverage"
    ],
    "generation_warnings": [
      "The input manifest for this request specified 1 occurrence each of Biased Assimilation and Egocentric bias; per the CONDITION RULES, vocabulary_control requires zero intended instances of all named target biases. The manifest occurrence counts were overridden to zero to comply with the control condition, and this override is documented here rather than silently applied."
    ]
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
