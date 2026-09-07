You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, is it okay if I record this conversation for internal research on curriculum decision-making, with everything used in de-identified form?

Participant: Sure, that's fine.

Interviewer: Can you tell me about your role and what this particular adoption cycle involved?

Participant: I've served on the district curriculum committee for about five years, representing middle school math. Last fall, after sixth-grade state scores dropped eight points district-wide, the superintendent's office asked us to run a full adoption cycle for a new K-8 math curriculum. This time we actually had twelve weeks instead of the usual six, since the state calendar shifted and gave us extra room. Everyone was glad for the breathing space, honestly — most of us still teach or run buildings full-time.

Interviewer: Walk me through how the review actually started.

Participant: Three publishers submitted proposals — Curriculum A, B, and C. Each had a standards-alignment matrix, sample units, vendor support materials, the usual package. With twelve weeks, we had every intention of giving all three a genuinely deep look before narrowing anything down. But right around when the proposals landed, two of our members came back from a regional math conference where a neighboring district presented on their experience adopting Curriculum B. They were enthusiastic — said it fixed their pacing issues. Our people came back energized, and even with all that extra runway, our first working session ended up centered on B. A and C got more of a checklist pass.

Interviewer: Given you had twelve weeks instead of six, was there a reason A and C didn't get the same depth early on?

Participant: That's the part I keep turning over. There wasn't really a scheduling reason. We had time. It's just that once people were talking about what the neighboring district found, B became the thing everyone wanted to dig into first. We told ourselves we'd circle back to A and C properly, and we had the calendar to do it.

Interviewer: Did you?

Participant: Eventually, yes — around scoring, we went back to Curriculum A's proposal, and it actually had a stronger differentiated-instruction plan than B's. But by then, even weeks into a much longer process, the conversation was still framed as "is this good enough to make us reconsider B," instead of just asking how strong A was standing on its own.

Interviewer: Let's move to the vendor meeting. What happened there?

Participant: That was maybe three weeks in, so still plenty of runway left — something like nine weeks to go. Curriculum B's rep brought in committee members from other districts using it. One of them told a really vivid story about a struggling classroom that turned around within a semester. I still remember the details clearly. Somewhere in that same meeting, someone mentioned a statistical pilot report from a comparable district, covering multiple schools over a full year. I barely registered that part.

Interviewer: You had time to go get that report right away. What happened instead?

Participant: I kept meaning to. It sat on my list for weeks. The story was just more vivid — a real teacher, real kids, a real unit. The report was two sentences and some numbers I didn't have in front of me. It wasn't until we were close to final scoring that anyone actually pulled the report up. When we did, it showed mixed results across schools, not the clean win the anecdote suggested. But by then my sense of B's promise was already pretty locked in.

Interviewer: Did the extra time change how you weighed the testimonials versus the report?

Participant: Honestly, not as much as it should have. The testimonials felt like they confirmed what we already believed from the conference, so they didn't feel like they needed more scrutiny. The report felt like something to get to eventually rather than something urgent, even though nothing was stopping us from pulling it the same week.

Interviewer: Let's talk about the pilot. What happened when concerns came up?

Participant: We ran a three-week pilot of Curriculum B in two schools. About halfway through, one of the pilot teachers flagged pacing problems in a unit — said the sequencing didn't match how her students were actually progressing. By that point most of the committee had already spoken favorably about B in earlier meetings. We still had several weeks before the deadline, so there wasn't really an urgent reason to rush past it.

Interviewer: How was the concern handled?

Participant: It got mentioned, acknowledged, and the conversation moved along toward agreement fairly quickly anyway. We didn't send anyone to observe the second pilot classroom, even though we had the calendar space to do that easily. We just nodded and kept going. I found out afterward that one member had reservations that day but didn't voice them, given how the room felt.

Interviewer: Did that pacing issue end up mattering?

Participant: It did. A second classroom hit the same snag during full rollout. So the concern was real. It just didn't get a real hearing when it came up, even with time on our side.

Interviewer: Last decision point — final scoring. How did that go?

Participant: Everyone submitted rubric scores across five criteria for all three curricula. When the chair compiled them, Curriculum A had an odd split on differentiated-instruction support — two very high scores, two very low. B's scores were tighter across the board. The chair still needed one composite number per curriculum for the board memo, even though the memo wasn't due for weeks. The scores just got averaged straight across, split included. Once that single number came back, it read as a settled, middling score for A, and nobody suggested pulling it apart to see what was underneath.

Interviewer: Was the disagreement on Curriculum A discussed before combining the numbers?

Participant: Not really, even with all that time available. It went into the spreadsheet like everything else. It was only afterward, when someone asked why A's differentiation score looked so unremarkable despite that split, that we found out the two low scorers hadn't reviewed the differentiation appendix, while the two high scorers had. The average wasn't really consensus — it was masking a difference in how much people had actually read.

Interviewer: Did the board notice?

Participant: They asked. Why a criterion with that much internal disagreement got reported as one clean number. We didn't have a great answer beyond "that's how we compile scores."

Interviewer: Stepping back — with twelve weeks instead of six, did scheduling actually drive how quickly things moved?

Participant: Less than I expected, if I'm honest. We had room to slow down at almost every point, and mostly didn't use it. The pacing concern is the one that sits with me. Nobody was acting in bad faith. B just already felt like the likely outcome by the time real friction showed up, deadline or no deadline.

Interviewer: If the pacing concern had surfaced earlier, would the outcome have changed?

Participant: Possibly. Before people's minds were as made up, I think it would've gotten a more serious look, regardless of how much calendar time was left.

Interviewer: And if the neighboring district hadn't mentioned Curriculum B at that conference at all?

Participant: I've wondered that. I think A and C would've gotten a more even start from day one. B's materials were genuinely solid, so it might still have won out. But the early spotlight wouldn't have been there from the beginning.

Interviewer: If you had the scoring step to redo, even with no deadline pressure, would you handle the split differently?

Participant: Yes. I'd flag any criterion with a wide spread and ask why before folding it into one number. The spread itself was telling us something. Averaging it away just erased that, and having extra weeks available didn't stop us from doing it anyway.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "Elevation of a curriculum based on external district enthusiasm/popularity signal rather than independent evidence review, persisting despite absence of scheduling pressure to justify uneven review" },
      { "bias": "Groupthink", "occurrences": 1, "mechanism_constraint": "Suppression of dissenting pilot-teacher feedback under majority preference, with a member's unvoiced reservation, occurring despite ample remaining time before the deadline" },
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Overweighting a vivid single-classroom anecdote over a less memorable statistical report, despite ample time available to retrieve the report promptly" },
      { "bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "Evaluating subsequent curricula relative to an early-formed frontrunner reference point, persisting despite extended review time" },
      { "bias": "Confirmation bias", "occurrences": 1, "mechanism_constraint": "Readily accepting supporting testimonials while delaying retrieval of potentially disconfirming statistical data, despite no scheduling barrier to prompt retrieval" },
      { "bias": "Averaging Bias", "occurrences": 1, "mechanism_constraint": "Averaging widely divergent rubric scores into a single composite without investigating the disagreement, despite no imminent scheduling emergency" }
    ],
    "target_bias_names": [
      "Bandwagon effect",
      "Groupthink",
      "Availability Bias",
      "Anchoring Bias",
      "Confirmation bias",
      "Averaging Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 },
      { "bias": "Availability Bias", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 },
      { "bias": "Confirmation bias", "requested_occurrences": 1 },
      { "bias": "Averaging Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cfbw_01", "bias": "Bandwagon effect" },
      { "instance_id": "cfgt_01", "bias": "Groupthink" },
      { "instance_id": "cfav_01", "bias": "Availability Bias" },
      { "instance_id": "cfan_01", "bias": "Anchoring Bias" },
      { "instance_id": "cfcf_01", "bias": "Confirmation bias" },
      { "instance_id": "cfavg_01", "bias": "Averaging Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cfbw_01", "bias": "Bandwagon effect", "decision_point": 1 },
      { "instance_id": "cfgt_01", "bias": "Groupthink", "decision_point": 3 },
      { "instance_id": "cfav_01", "bias": "Availability Bias", "decision_point": 2 },
      { "instance_id": "cfan_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "cfcf_01", "bias": "Confirmation bias", "decision_point": 2 },
      { "instance_id": "cfavg_01", "bias": "Averaging Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cfbw_01",
        "bias": "Bandwagon effect",
        "mechanism": "Shortlisting attention allocated to Curriculum B based on secondhand reports of another district's enthusiasm rather than substantive independent review, unchanged despite a doubled review window",
        "affected_reasoning_operation": "Initial evidence-selection / shortlisting judgment",
        "evidence_source": "Conference report of neighboring district's reception of Curriculum B",
        "distinctiveness_requirement": "Occurs at the shortlisting moment before any committee-generated evidence exists; distinct from cfan_01's later comparative evaluation of already-shortlisted options"
      },
      {
        "instance_id": "cfgt_01",
        "bias": "Groupthink",
        "mechanism": "Committee suppresses full airing of a dissenting pilot teacher's pacing concern under pre-existing majority preference, moving to apparent consensus despite ample remaining weeks before the deadline",
        "affected_reasoning_operation": "Group deliberation / dissent evaluation before consensus decision",
        "evidence_source": "Pilot teacher's mid-pilot pacing report and the unvoiced reservation of one committee member",
        "distinctiveness_requirement": "Distinct from cfcf_01 in that it concerns suppression of an internal dissenting voice within a group deliberation moment, not selective external evidence-seeking"
      },
      {
        "instance_id": "cfav_01",
        "bias": "Availability Bias",
        "mechanism": "A vivid single-classroom anecdote is recalled and weighted more heavily in confidence-formation than a less memorable statistical report from the same meeting, despite ample time to retrieve the report promptly",
        "affected_reasoning_operation": "Recall and weighting of evidence for confidence formation",
        "evidence_source": "Vendor meeting anecdote vs. comparable-district statistical pilot report",
        "distinctiveness_requirement": "Distinct from cfcf_01: concerns differential recall/salience of two pieces of evidence encountered simultaneously, not selective retrieval based on prior preference"
      },
      {
        "instance_id": "cfan_01",
        "bias": "Anchoring Bias",
        "mechanism": "Early-formed frontrunner status of Curriculum B persists as an implicit reference point against which subsequently reviewed options are measured, unchanged by additional available review time",
        "affected_reasoning_operation": "Comparative evaluation of new evidence relative to an established reference point",
        "evidence_source": "Curriculum A's differentiation plan, reviewed and judged relative to Curriculum B's presumptive lead",
        "distinctiveness_requirement": "Occurs during later comparative evaluation, distinct from cfbw_01's earlier shortlisting-attention moment at the same decision point"
      },
      {
        "instance_id": "cfcf_01",
        "bias": "Confirmation bias",
        "mechanism": "Committee members readily accept testimonials consistent with existing favorable view of Curriculum B while deprioritizing retrieval of a statistical report that could complicate that view, despite no scheduling barrier to prompt retrieval",
        "affected_reasoning_operation": "Selective evidence-seeking and evidence-acceptance following an existing preference",
        "evidence_source": "Vendor testimonials (accepted readily) vs. comparable-district statistical report (retrieval delayed)",
        "distinctiveness_requirement": "Distinct from cfav_01: concerns motivated prioritization of evidence-seeking effort based on prior preference, not passive differential memorability"
      },
      {
        "instance_id": "cfavg_01",
        "bias": "Averaging Bias",
        "mechanism": "Chair combines widely divergent individual rubric scores into a single composite without investigating the underlying disagreement, treating the mean as settled despite no imminent scheduling emergency",
        "affected_reasoning_operation": "Aggregation of conflicting quantitative judgments into a summary decision metric",
        "evidence_source": "Individual rubric scores on the differentiation-support criterion for Curriculum A",
        "distinctiveness_requirement": "Sole aggregation-stage occurrence; not related to any other instance's evidence source"
      }
    ],
    "intended_strength": [
      { "instance_id": "cfbw_01", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "cfgt_01", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "cfav_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "cfan_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cfcf_01", "bias": "Confirmation bias", "strength": "subtle" },
      { "instance_id": "cfavg_01", "bias": "Averaging Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": "EI_Biased_6",
    "counterfactual_variable": {
      "name": "Length of the committee's adoption-cycle deadline",
      "original_state": "Six-week hard deadline creating acute schedule pressure throughout the process",
      "changed_state": "Twelve-week deadline (doubled review window), substantially reducing acute schedule pressure at each decision point",
      "variables_to_hold_constant": [
        "The three publisher proposals and their content",
        "The neighboring district's conference testimony about Curriculum B",
        "The vendor stakeholder meeting, anecdote, and statistical report",
        "The pilot structure, pacing concern, and its later recurrence",
        "The final rubric-scoring process and the two-high/two-low split on Curriculum A",
        "Committee composition and the board's eventual questions",
        "The four-decision-point narrative structure and sequence of events"
      ]
    },
    "scenario_id": "EI_Counterfactual_6",
    "domain_id": "EI",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences mirror EI_Biased_6's allocation exactly (decision points 1 and 2 each host two biases at distinct moments/evidence sources; decision points 3 and 4 each host one bias), since the counterfactual condition requires holding the bias-embedding structure constant while varying only the deadline-length causal variable. No decision point holds more than two instances of the same bias (each bias occurs only once total). Assignment prioritized mechanism-context fit identically to the paired scenario: bandwagon and anchoring both relate to initial/comparative shortlisting judgments (decision point 1) but target distinct moments; availability and confirmation both relate to processing the same vendor-meeting evidence (decision point 2) but target distinct cognitive operations; groupthink fits the group-consensus moment (decision point 3); averaging bias fits the numerical aggregation moment (decision point 4).",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "The three publisher proposals and their content",
      "The neighboring district's conference testimony about Curriculum B",
      "The vendor stakeholder meeting, anecdote, and statistical report",
      "The pilot structure, pacing concern, and its later recurrence",
      "The final rubric-scoring process and the two-high/two-low split on Curriculum A",
      "Committee composition and the board's eventual questions",
      "The four-decision-point narrative structure and sequence of events"
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
