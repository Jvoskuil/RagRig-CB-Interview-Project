You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time. This is a voluntary session for internal research on how IA reviews get worked, not a disciplinary matter. You can decline any question. Good with that?

Participant: Sure, that's fine.

Interviewer: Can you tell me your role and experience with complaint reviews?

Participant: Internal Affairs investigator, about five years. I handle use-of-force complaints mostly, some policy violations.

Interviewer: Walk me through the case.

Participant: Traffic stop on Cedar Street, expired registration, ended with a takedown. The driver, Mr. Alvarez, alleges excessive force by Officer Marquez, came away with a wrist fracture. Marquez's report says Alvarez became resistant and pulled his arm away, necessitating the takedown. His partner, Officer Chen, corroborates that. Marquez has nine years in, two prior complaints, both closed unfounded. Alvarez has two prior arrests, one for resisting.

Interviewer: What was your initial read on credibility before you'd seen any footage?

Participant: Genuinely unresolved. Two competing accounts, both plausible on their face, and I didn't have enough yet to prefer one.

Interviewer: What did you do first when you opened the file?

Participant: Requested background on both sides—Alvarez's arrest history and Marquez's disciplinary and training file. Alvarez's record came back within a day, since it's just a records-system pull. Marquez's full file took almost a week because it required a request through the union rep and a records custodian. So for several days I had a fuller picture of one side than the other, which I noted explicitly in my log as a limitation, not a conclusion.

Interviewer: Did that timing gap affect how you approached the rest of the review?

Participant: I tried not to let it. I flagged it as an open item—"complainant background received, officer background pending"—so anyone reading the file later would know the record was uneven at that point, not that I'd already decided anything based on it. Dispatch audio later confirmed it was a routine stop, not flagged high-risk. Medical report confirmed the fracture but didn't tell me which account caused it.

Interviewer: Let's go to the footage.

Participant: Eighteen minutes, with a forty-second gap right after initial contact—his camera didn't reactivate cleanly. Early part is calm, verbal exchange, some de-escalation language from Marquez. Final ninety seconds: Alvarez pulls his arm back, Marquez takes him down.

Interviewer: How did you weigh the earlier footage against that final sequence?

Participant: Honestly, I couldn't fully resolve it on the first pass. The takedown is obviously central since that's where the injury happened, but the gap sits right before the point where things start escalating, and I don't know what's in it. I logged both segments as carrying weight and noted the gap as a limiting factor on any proportionality conclusion I might draw. I didn't want to lock in a read before the consultant weighed in.

Interviewer: What came out of the consultant review?

Participant: A slowed-frame audio pass caught Marquez raising his voice and stepping closer about three minutes before the takedown. The consultant said it's relevant context but not dispositive on its own—doesn't resolve whether the final force was proportionate, just adds texture.

Interviewer: How did that sit with you?

Participant: It complicated things more than it clarified them, if I'm honest. It's the kind of detail that could support either read, depending on what else you believe about the encounter.

Interviewer: Tell me about the case conference.

Participant: Day six. Me, the sergeant, two peer investigators. The sergeant supervised Marquez for three years, said something like "he's generally solid, but I wasn't in the car, so take that for what it's worth." One of the other investigators raised the forty-second gap, said it needed to be addressed before we went further.

Interviewer: How did the room handle that?

Participant: We actually sat with it. There wasn't a quick consensus—two of us thought the gap was potentially significant given the timing relative to the escalation audio, one thought Chen's corroboration and the visible resisting motion carried it regardless. We didn't resolve that disagreement in the room. I logged the dissenting view by name in the case file and noted the preliminary summary as tentative pending the gap issue.

Interviewer: Did the sergeant's history with Marquez shape the discussion?

Participant: It was mentioned, and it's fair to say it's not nothing—people listen when a three-year supervisor speaks. But he qualified it himself, and the discussion kept coming back to what was and wasn't on the tape rather than settling on his character read. I can't say for certain it had zero influence, but I also can't point to a moment where it overrode the evidentiary discussion.

Interviewer: What happened with the eyewitness on day ten?

Participant: A civilian witness we'd had trouble reaching finally called back. She said Marquez was "aggressive from the start," which cuts against how I'd been characterizing the early footage. That came two days after I'd sent the Deputy Chief a preliminary note—explicitly marked tentative, pending the gap and the consultant review.

Interviewer: How did you weigh her statement against what you already had?

Participant: We ran a supplemental check—she had an unobstructed view but was about thirty-five feet out, evening light. I weighed that against the footage on its own terms: is a thirty-five-foot, unobstructed view enough to outweigh eighteen minutes of direct recording? I didn't think it fully was, but I also didn't think it was nothing, especially given the earlier escalation audio the consultant had flagged. I ended up revising the briefing language to reflect that the finding remained more open than the initial note suggested, rather than either adopting her account outright or setting it aside.

Interviewer: Did the fact that you'd already briefed command shape how you handled her statement?

Participant: Command asked whether the preliminary note still held, and I told them it needed updating. It wasn't comfortable revising something I'd already sent up, but the distance and lighting were the actual basis for how much weight I gave her account—not really about protecting what I'd said earlier. I'd rather have gotten it right than tidy.

Interviewer: What's the part of this case you're least confident about?

Participant: The forty-second gap, still. I don't know what happened in it, and I don't know how much that should move the needle either way.

Interviewer: If the eyewitness statement had come in on day two instead of day ten, would your review have gone differently?

Participant: Possibly. I'd have had it earlier alongside the footage instead of layering it onto a note I'd already sent, though I think I'd have weighed it the same way on the merits—distance and view, not timing.

Interviewer: If you'd been the only reviewer, without the case conference, same finding?

Participant: Hard to say. I might have sat with the gap even longer alone. The conference didn't rush me toward a view, but group discussion does move differently than solo review.

Interviewer: Anything you'd sequence differently next time?

Participant: I'd push to get officer background files moving faster at intake, so that gap doesn't sit open as long. Otherwise, I think the uncertainty here was mostly the case itself, not how I worked it.

Interviewer: Appreciate you walking through it.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      { "bias": "Cognitive dissonance", "occurrences": 0, "mechanism_constraint": "No post-commitment reconciliation of a prior communicated position may be embedded; any evidence revision must be explicitly reasoned on reliability grounds." },
      { "bias": "Recency Effects", "occurrences": 0, "mechanism_constraint": "No disproportionate weighting of the most-recently-reviewed footage segment or most-recently-obtained testimony due to temporal position may be embedded." },
      { "bias": "Groupthink", "occurrences": 0, "mechanism_constraint": "No rapid unchallenged consensus formation with unpursued dissent may be embedded; dissent must be explicitly logged." },
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "occurrences": 0, "mechanism_constraint": "No unequal verification effort applied to the complainant versus the officer may be embedded; any asymmetry must be resource-driven and explicitly flagged as incomplete." }
    ],
    "target_bias_names": [
      "Cognitive dissonance",
      "Recency Effects",
      "Groupthink",
      "Confirmation Bias and Asymmetrical skepticism"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Cognitive dissonance", "requested_occurrences": 0 },
      { "bias": "Recency Effects", "requested_occurrences": 0 },
      { "bias": "Groupthink", "requested_occurrences": 0 },
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "LE_Biased_5",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Ambigious_5",
    "domain_id": "LE",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, which mandates zero intended occurrences of every bias named in the paired manifest regardless of the nonzero counts supplied in the caller's input manifest. The supplied manifest ([Cognitive dissonance:1, Recency Effects:2, Groupthink:1, Confirmation Bias and Asymmetrical skepticism:1]) is treated as identifying the paired target-bias set from LE_Biased_5 for exclusion purposes only, not as an occurrence count to embed.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and role (Internal Affairs Investigator, municipal PD)",
      "Core incident facts (Cedar Street expired-registration stop, takedown, wrist fracture)",
      "All named actors and their prior histories",
      "The 40-second BWC gap",
      "The 14-day deadline and 48-hour briefing window",
      "The day-10 eyewitness statement and 35-foot viewing distance",
      "Four-decision-point structure and approximate word count",
      "Technical vocabulary and difficulty level"
    ],
    "generation_warnings": [
      "The caller's input manifest for this scenario specifies nonzero occurrence counts (1, 2, 1, 1) identical to the paired biased scenario LE_Biased_5, which conflicts with the ambiguous_control condition rule requiring zero intended occurrences of all named target biases. Per the CONDITION RULES, the condition value governs: this specification implements zero intended occurrences for every listed bias and repurposes the supplied manifest solely as the definition of the paired target-bias set to be avoided, not as an embedding instruction. The dataset controller should confirm this interpretation before validation."
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
