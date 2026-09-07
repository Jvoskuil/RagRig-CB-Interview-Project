You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, just to confirm — this is a routine debrief for our operational learning file, not a disciplinary review, and you're free to skip anything you'd rather not detail. Can you tell me your role and how long you've been dispatching?

Participant: Sure, no problem. I'm a Flight Operations Officer, licensed dispatcher, coming up on nine years now, mostly widebody long-haul. I hold joint responsibility with the captain for the flight release, so I'm in it from planning through landing.

Interviewer: Good. Let's start broad — walk me through the flight and what your objective was going in.

Participant: This was an overnight JFK to Lisbon rotation, widebody twin. My job was to build a release that was compliant and reasonably efficient — right fuel, right alternate, nothing wasteful, but enough margin to cover the weather picture. Going into the shift I already knew the aircraft had an APU write-up, deferred under the MEL, so anywhere we might divert needed ground power support, not just a runway. That constraint shaped everything downstream.

Interviewer: What was the weather picture at that point?

Participant: The 0300Z TAF for Lisbon showed some morning visibility restriction, fairly typical coastal fog, but forecast to lift comfortably before our arrival window. Porto looked like the natural alternate — good runway, and their ground power unit was listed as available until 0500 local, which covered our arrival plus buffer. I built the release off that TAF: standard alternate fuel, contingency, reserve. It matched policy, so I didn't see a reason to load extra gas or chase a second alternate. I remember thinking the numbers were clean and moving on to the next release in the queue — it was a busy overnight bank.

Interviewer: Once the flight departed, how did things unfold?

Participant: Fairly normal until a few hours in. An amended TAF came through showing the fog setting in about two hours earlier than the original forecast had it. I pulled up the model guidance to sanity-check it. One run still showed the improving trend consistent with what I'd already briefed the crew. Another run, plus a PIREP from an aircraft that had landed there not long before, pointed to a slower burn-off, worse than forecast. Then later, closer to descent, the crew asked me directly for a fresh read on continue-versus-divert risk, and I answered that using the fuel picture. Finally at top of descent, with visibility sitting right at minima and the Porto GPU window closing, I gave a continue recommendation. There was a short hold near the bottom before it worked out, but we landed at Lisbon without further incident.

Interviewer: Let's rebuild that chronologically. What information did you have at each stage, in order?

Participant: Release time: early TAF, MEL constraint, alternate fuel policy. A couple hours later: amended TAF plus two competing model runs and a PIREP. Later still, maybe ninety minutes from arrival: extended satellite imagery, more METARs from stations around Lisbon, current fuel state, and updated word on the Porto GPU cutoff. Then at top of descent: live visibility trend, the closing GPU window, and the crew wanting a straight answer.

Interviewer: Let's take the first decision — building the release. What alternatives did you weigh?

Participant: Really it was between releasing on the minimum required fuel and alternate per the early TAF, or padding it — extra fuel, maybe a second alternate with round-the-clock power, given there was a fog signature in the picture at all.

Interviewer: What made you go with the minimum?

Participant: The TAF I had in front of me supported it, and Porto's GPU window comfortably covered our ETA. Once that release was built, honestly, that became my working number for the rest of the watch — the later checks I did were more about confirming that figure still held rather than starting over and asking whether a completely different fuel or alternate plan made more sense from scratch.

Interviewer: When the amended TAF and the conflicting model/PIREP data came in, how did you handle that?

Participant: I looked at both. The model that lined up with the trend I'd already briefed felt more current and more consistent with what we'd been seeing on other flights that shift, so I leaned on that one. The PIREP was useful, but a single pilot report felt like one data point against a fuller model picture, so I passed the update to the crew framed around the improving trend, noting the other read existed but wasn't the lead story.

Interviewer: Did you consider weighting the PIREP and the slower-recovery model more heavily?

Participant: I considered it, yeah. It just didn't feel like enough on its own to justify walking back guidance I'd already given the crew.

Interviewer: Move to the point where the crew asked for a fresh risk read. What did you do with the imagery and extra METARs?

Participant: I went through the extended satellite loop pretty carefully, plus the nearby METARs, spent real time on it. It gave me a fuller picture and I felt more settled afterward. Looking back, I think I was treating the sheer amount of data as if working through more of it would settle the call on its own — but the extra loop and those additional METARs were really just repeating the same broad trend I already had, and there wasn't a specific reading in any of them that was ever going to flip the recommendation one way or the other.

Interviewer: And how did you answer their risk question specifically?

Participant: They'd asked something broader — basically, is continuing to Lisbon versus setting up for Porto still the right call given the MEL and the visibility trend. I answered mostly with the fuel numbers — we had healthy reserves, well above minimums, comfortable margin to hold if needed. That's a real and necessary part of the answer. Whether I fully separated out the visibility-and-GPU-window piece as its own question, distinct from just "do we have gas," I'm less sure about now.

Interviewer: Last decision — top of descent, visibility near minima, GPU window closing. What tipped you to continue rather than divert?

Participant: The remaining fuel and time margin still looked workable, and the plan all along had been Lisbon with Porto as backup if things really fell apart. Diverting felt like abandoning a plan that had held up reasonably well to that point, and the numbers on paper still supported continuing. I recommended continue.

Interviewer: How confident were you at that moment?

Participant: Genuinely, moderately confident, not fully. There was real uncertainty in that visibility trend.

Interviewer: How did that get reflected afterward, say in the operations log?

Participant: I wrote it up fairly cleanly — noted that conditions supported continuing to Lisbon and that the fuel plan held throughout. Reading it back now, it reads a bit more settled than it actually felt in the moment.

Interviewer: If the PIREP and slower model had arrived before you finalized the release, would anything have changed?

Participant: Possibly the alternate fuel load, yes. Hard to say for certain.

Interviewer: If the GPU cutoff had been flagged an hour earlier than it was, what would you have done differently at top of descent?

Participant: That probably shifts the divert case earlier — that window was really the tightest constraint in the whole picture.

Interviewer: Anything you'd tell a newer dispatcher about a night like this?

Participant: Keep re-asking the actual question being asked, not just the easiest piece of it, and don't let your first number quietly become the only number you're checking against.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "must manifest as persistence of an early TAF-derived fuel/alternate figure as the ongoing reference point" },
      { "bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "must manifest as unequal weighting of two conflicting weather data sources favoring the one matching the original plan" },
      { "bias": "Information bias", "occurrences": 1, "mechanism_constraint": "must manifest as seeking/reviewing additional data believed to improve the decision despite not altering the diagnostic conclusion" },
      { "bias": "Omitting subjectivity", "occurrences": 1, "mechanism_constraint": "must manifest as retrospective documentation presenting a judgment call as settled objective fact" },
      { "bias": "Plan Continuation", "occurrences": 1, "mechanism_constraint": "must manifest as continuing the original plan despite worsening real-time indicators" },
      { "bias": "Substitution bias", "occurrences": 1, "mechanism_constraint": "must manifest as answering an easier substituted question (fuel sufficiency) in place of the harder asked question (overall continue/divert risk)" }
    ],
    "target_bias_names": ["Anchoring Bias", "Confirmation Bias", "Information bias", "Omitting subjectivity", "Plan Continuation", "Substitution bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Anchoring Bias", "requested_occurrences": 1 },
      { "bias": "Confirmation Bias", "requested_occurrences": 1 },
      { "bias": "Information bias", "requested_occurrences": 1 },
      { "bias": "Omitting subjectivity", "requested_occurrences": 1 },
      { "bias": "Plan Continuation", "requested_occurrences": 1 },
      { "bias": "Substitution bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "AV6_anchor_01", "bias": "Anchoring Bias" },
      { "instance_id": "AV6_confirm_01", "bias": "Confirmation Bias" },
      { "instance_id": "AV6_infobias_01", "bias": "Information bias" },
      { "instance_id": "AV6_substitution_01", "bias": "Substitution bias" },
      { "instance_id": "AV6_plancont_01", "bias": "Plan Continuation" },
      { "instance_id": "AV6_omitsubj_01", "bias": "Omitting subjectivity" }
    ],
    "intended_decision_points": [
      { "instance_id": "AV6_anchor_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "AV6_confirm_01", "bias": "Confirmation Bias", "decision_point": 2 },
      { "instance_id": "AV6_infobias_01", "bias": "Information bias", "decision_point": 3 },
      { "instance_id": "AV6_substitution_01", "bias": "Substitution bias", "decision_point": 3 },
      { "instance_id": "AV6_plancont_01", "bias": "Plan Continuation", "decision_point": 4 },
      { "instance_id": "AV6_omitsubj_01", "bias": "Omitting subjectivity", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "AV6_anchor_01",
        "bias": "Anchoring Bias",
        "mechanism": "Early TAF-derived fuel/alternate figure treated as fixed reference baseline for subsequent judgments",
        "affected_reasoning_operation": "Initial estimate formation and its persistence",
        "evidence_source": "0300Z TAF, fuel policy minimums",
        "distinctiveness_requirement": "Distinct from confirmation bias by involving no comparison of conflicting sources, only fixation on a single early figure"
      },
      {
        "instance_id": "AV6_confirm_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective emphasis on the weather model run matching original plan; discounting of contradictory PIREP/model without equivalent justification",
        "affected_reasoning_operation": "Evaluation and weighting of conflicting evidence",
        "evidence_source": "amended TAF, two conflicting model runs, PIREP",
        "distinctiveness_requirement": "Distinct from anchoring by requiring an explicit comparison between two conflicting sources rather than fixation on a single starting figure"
      },
      {
        "instance_id": "AV6_infobias_01",
        "bias": "Information bias",
        "mechanism": "Belief that gathering more data (extended satellite loop, extra METARs) itself improves decision quality despite no change to diagnostic conclusion",
        "affected_reasoning_operation": "Evidence-gathering behavior and perceived value of additional information",
        "evidence_source": "extended satellite imagery loop, additional METARs",
        "distinctiveness_requirement": "Distinct from confirmation bias by involving quantity/perceived value of information rather than selective favoring of one side of a conflict"
      },
      {
        "instance_id": "AV6_substitution_01",
        "bias": "Substitution bias",
        "mechanism": "Replacing a hard risk-assessment question with an easier fuel-sufficiency question and treating the easier answer as resolving the original question",
        "affected_reasoning_operation": "Question interpretation and answer substitution",
        "evidence_source": "current fuel state, reserve/contingency policy, GPU cutoff, visibility trend",
        "distinctiveness_requirement": "Distinct from information bias by involving a shift in the question being answered rather than volume of data reviewed; occurs in same decision point but different reasoning operation and evidence trace"
      },
      {
        "instance_id": "AV6_plancont_01",
        "bias": "Plan Continuation",
        "mechanism": "Disproportionate weight to original release plan when recommending continuation despite worsening real-time visibility/GPU-window data",
        "affected_reasoning_operation": "Final continue-vs-divert recommendation",
        "evidence_source": "current visibility trend, GPU window closing, original release plan",
        "distinctiveness_requirement": "Distinct from omitting subjectivity by occurring at the moment of the live decision itself, not in retrospective documentation"
      },
      {
        "instance_id": "AV6_omitsubj_01",
        "bias": "Omitting subjectivity",
        "mechanism": "Post-event log entry presents the continuation judgment as settled objective fact, omitting the uncertainty and conflicting signals present at decision time",
        "affected_reasoning_operation": "Retrospective documentation and communication of a judgment under uncertainty",
        "evidence_source": "dispatcher's real-time uncertainty, final log entry drafted after landing",
        "distinctiveness_requirement": "Distinct from plan continuation by occurring after the flight, in the documentation/reporting act, not the live recommendation"
      }
    ],
    "intended_strength": [
      { "instance_id": "AV6_anchor_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "AV6_confirm_01", "bias": "Confirmation Bias", "strength": "moderate" },
      { "instance_id": "AV6_infobias_01", "bias": "Information bias", "strength": "subtle" },
      { "instance_id": "AV6_substitution_01", "bias": "Substitution bias", "strength": "moderate" },
      { "instance_id": "AV6_plancont_01", "bias": "Plan Continuation", "strength": "moderate" },
      { "instance_id": "AV6_omitsubj_01", "bias": "Omitting subjectivity", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_6",
    "domain_id": "AV",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across the 4 required decision points by mechanism fit and narrative realism: 1 bias at decision point 1, 1 bias at decision point 2, 2 distinct biases (Information bias, Substitution bias) at decision point 3 using different evidence sources and reasoning operations, and 2 distinct biases (Plan Continuation, Omitting subjectivity) at decision point 4 separated by live-decision vs. retrospective-documentation moments. No bias repeated at the same decision point; each instance has a unique instance_id.",
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
