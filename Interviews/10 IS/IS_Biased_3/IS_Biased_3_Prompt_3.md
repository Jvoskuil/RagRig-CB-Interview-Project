You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal research-practice review, and I'll be asking you to walk me through a specific project in detail. You can skip anything you're not comfortable discussing. Can you start by telling me your role and how long you've been doing UX research here?

Participant: Sure. I'm a UX researcher on the productivity tools team, been here about four years. Most of my work is usability testing and discovery research feeding into our quarterly release cycles.

Interviewer: Great. I want to focus on the Smart Suggestions study. Can you walk me through how that project came about?

Participant: So Smart Suggestions is a recommendation feature — it watches what you're doing in the app and surfaces contextual actions. It came to me already pretty far along. Our VP had seen a competitor demo and decided we were building it. My brief wasn't "should we ship this," it was "help us ship it right." That framing came directly from him, almost word for word, in the kickoff.

Interviewer: How did that framing affect how you approached the study?

Participant: Honestly, it put me in a slightly defensive posture. The original plan I'd sketched was pretty lean — five moderated sessions, look at task completion and basic usability heuristics, done in a week. But hearing "this is happening regardless" made me not want to just rubber-stamp something. So before I even looked at the budget, I decided to add an unmoderated diary study on top of the moderated sessions, specifically to give people more room to surface friction over time, not just in a single session.

Interviewer: What did you know at that point that made you confident the expansion was the right call?

Participant: I had some prior data — a similar recommendation pattern we shipped in another product line got mixed reactions, so I knew these features aren't automatically loved. That backed up the diary study idea. But if I'm being fully honest, part of it was wanting to make sure the study had enough teeth that it couldn't just be waved through.

Interviewer: Did anyone push back on the expanded scope?

Participant: Research ops flagged that moderated sessions plus a diary cohort would eat most of our remaining budget. And engineering said the diary study would push the readout back a week. I considered just keeping the original five-session plan, and I also thought about pausing to renegotiate the study's purpose with the VP directly. In the end I went with the expanded version anyway.

Interviewer: Let's move to the discussion guide. What happened there?

Participant: Our PM shared a transcript from an earlier internal demo — a stakeholder said something like "this feels like it reads my mind." She sent it to me before I'd finalized the guide and said, "make sure the guide can capture moments like this." At that point my draft was pretty neutral — open prompts about task completion, satisfaction, that kind of thing.

Interviewer: What did you do with that transcript?

Participant: I went back through the guide and revised a couple of probes to more closely echo that framing — things like asking participants to describe moments where the suggestion "anticipated" what they needed. I thought I was just sharpening vague questions with a concrete example. Screener criteria were still being locked down around the same time, so there was a lot happening at once.

Interviewer: Did you consider leaving the original wording as-is?

Participant: Yeah, that was one option. Another was asking her to hold off sharing examples until after I'd locked the guide. I didn't do either. I finalized the revised version.

Interviewer: What happened once sessions started?

Participant: Two of the pilot participants used almost identical language to that transcript — "it's like it knows what I want." Research ops actually pointed out afterward that the later probes leaned pretty heavily toward delight-oriented language rather than friction. I hadn't really clocked that until she said it.

Interviewer: Let's talk about synthesis. What did the fuller pilot data look like?

Participant: Once we had ten moderated sessions plus the diary entries, it was mixed. Four sessions had real frustration — suggestions popping up mid-task, interrupting flow. Three were clearly positive. The diary entries kept circling back to timing as an issue.

Interviewer: How did you approach coding that?

Participant: This is where it got complicated. I'd given the steering committee an informal update about two weeks earlier — after just the first couple of sessions — saying early signs looked promising. So when the frustration cluster showed up, I coded it separately, as edge cases tied to atypical workflows, rather than merging it with the positive theme into one "mixed reception" finding.

Interviewer: What made atypical workflows the right explanation, in your view at the time?

Participant: Some of those users did have unusual task patterns — multi-window setups, non-standard shortcuts. So there was a real basis for it. But when a second researcher sat in on the affinity mapping and asked why we weren't just calling it "mixed reception" outright, I remember thinking that would be a harder story to tell after already saying things looked promising. That consideration was in my head when I made the call.

Interviewer: Was pausing for more sessions ever on the table?

Participant: Briefly. Engineering was also asking whether the timing complaints were serious enough to change the rollout configuration, and we didn't have time to run more sessions before the readout, so I moved forward with the edge-case framing.

Interviewer: Walk me through the final recommendation.

Participant: The synthesis doc described the feature as largely positive with a small caveat about timing. Engineering wanted one of three things: ship as-is, ship with a timing adjustment, or delay for redesign. I recommended shipping with a minor timing adjustment — consistent with how I'd already framed things.

Interviewer: How did the readout go?

Participant: The steering committee approved it, asked for a follow-up study post-launch. The VP thanked me for "confirming the direction was right all along." That phrase stuck with me a bit.

Interviewer: What information, if you'd had it earlier, might have changed any of these decisions?

Participant: If I'd had the full ten-session data set before I ever spoke informally to the committee, I might have described the early signal more cautiously. Not giving that update at all would have removed a constraint I was working around later.

Interviewer: If the product manager hadn't shared that transcript before you finalized the guide, do you think the probes would have looked different?

Participant: Probably. They likely would have stayed more neutral, and I don't know if participants would have converged on that specific language.

Interviewer: Looking back, is there anything about the process you'd reconsider?

Participant: I think I'd separate the informal updates from the analysis phase more strictly — maybe not report anything upward until coding was finalized. And I'd want a second pass on the guide before sharing any example transcripts, just to keep those inputs from bleeding into the wording. The frustration data was real; I just wonder now whether "edge case" was the cleanest read of it or the most convenient one at the time.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Reactance",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as scope expansion in direct response to a mandate framed as non-negotiable, not as generic dislike of the feature."
      },
      {
        "bias": "Priming effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as instrument (discussion guide) wording shift following exposure to a specific example, prior to and independent of actual pilot data."
      },
      {
        "bias": "Cognitive Dissonance",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as reinterpretation of contradicting data specifically to preserve consistency with a prior public statement, not as generic optimism."
      }
    ],
    "target_bias_names": ["Reactance", "Priming effect", "Cognitive Dissonance"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Reactance", "requested_occurrences": 1},
      {"bias": "Priming effect", "requested_occurrences": 1},
      {"bias": "Cognitive Dissonance", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Reactance"},
      {"instance_id": "cb_02", "bias": "Priming effect"},
      {"instance_id": "cb_03", "bias": "Cognitive Dissonance"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Reactance", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Priming effect", "decision_point": 2},
      {"instance_id": "cb_03", "bias": "Cognitive Dissonance", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Reactance",
        "mechanism": "Scope expansion asserted in direct response to a mandate framed as removing the researcher's discretion over the study's purpose.",
        "affected_reasoning_operation": "Scope-setting under perceived constraint on research freedom",
        "evidence_source": "VP's mandate framing plus researcher's stated rationale for adding the diary study",
        "distinctiveness_requirement": "Must be tied explicitly to the mandate framing, not to methodological necessity alone."
      },
      {
        "instance_id": "cb_02",
        "bias": "Priming effect",
        "mechanism": "Guide-wording revision following exposure to a specific enthusiastic example transcript shared immediately before finalization.",
        "affected_reasoning_operation": "Instrument design / probe wording selection",
        "evidence_source": "Product manager's shared transcript and resulting probe revisions, plus later echoed participant language",
        "distinctiveness_requirement": "Must occur before pilot data collection and be traceable to the shared example, distinct from cb_03's data-synthesis-stage mechanism."
      },
      {
        "instance_id": "cb_03",
        "bias": "Cognitive Dissonance",
        "mechanism": "Reclassification of contradicting frustration data as 'edge cases' specifically to remain consistent with an earlier public 'promising' statement.",
        "affected_reasoning_operation": "Data synthesis and thematic categorization",
        "evidence_source": "Mixed pilot session data plus researcher's prior informal steering-committee update",
        "distinctiveness_requirement": "Must occur at data-synthesis stage and be motivated by consistency with a prior public commitment, distinct from cb_01's mandate-driven and cb_02's instrument-driven mechanisms."
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Reactance", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Priming effect", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Cognitive Dissonance", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IS_Biased_3",
    "domain_id": "IS",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Each bias assigned to a distinct decision point (1, 2, 3) based on mechanism fit and narrative realism: reactance at the mandate-driven scope decision, priming at the instrument-design decision, cognitive dissonance at the data-synthesis decision. Decision point 4 intentionally left free of new intended instances. No bias shares a decision point, so no sub-allocation of evidence sources within a single decision point was required.",
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
