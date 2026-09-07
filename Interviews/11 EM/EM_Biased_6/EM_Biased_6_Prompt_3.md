You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief for our exercise-design case-study library — I'll be asking about a specific project you led, how the decisions actually unfolded, not whether they were "right" in hindsight. Everything stays de-identified. Sound okay?

Participant: Sure, happy to walk through it. This is the Riverbend Rising full-scale exercise, right? That one's still pretty fresh for me.

Interviewer: Exactly. Can you start by describing the assignment and what success would've looked like?

Participant: I was handed the FSE build in early spring — simulate a levee failure and flash-flood evacuation, get it HSEEP-compliant, and use it to validate EOC escalation procedures before the seasonal flood window opened. Success meant a full exercise day, a usable Controller-Evaluator handbook, and an AAR that actually told the Director something new about our capability gaps.

Interviewer: Give me the incident account — how did the project actually go, start to finish?

Participant: We'd run something similar back in 2019 — smaller footprint, two of us on it, and we mostly reused an existing scenario shell. That one took about six weeks start to finish. This time I was solo, and the scope was bigger: a brand-new levee-failure module built off updated Army Corps dam-break modeling, plus coordination across the regional EOC, the school district, and municipal police and fire. Deadline was fixed at ten weeks because of the flood-risk calendar. I scoped the build assuming it'd track pretty close to the 2019 timeline — figured I knew the process well enough to move fast. About four weeks in, I was still building the custom hydrology module and waiting on sign-off from three different agencies, and a status check showed we'd already slipped two weeks. From there it became a scramble — severity calibration with the advisory committee, a fight over which training injects we could actually finish, and a last push on the handbook right up against the deadline.

Interviewer: Let's reconstruct that chronologically. What did you know at each stage, and what changed as you learned more?

Participant: At kickoff I had the 2019 numbers in my head and the new Corps data in hand, but I hadn't yet mapped out how much longer three-agency coordination would take versus one shell reused solo. Once the schedule slipped, I knew severity calibration and the advisory committee conversation were coming up next, and I could already tell we wouldn't have time to fully build every kind of training material — so the inject decision became a resource fight. By the time I got to the handbook, the clock was the dominant fact.

Interviewer: Let's slow down on the first real decision — scoping the build timeline. Walk me through it.

Participant: Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much. I remember telling the Director I could deliver in the same general window even though I was down to one person and building the hydrology piece essentially from scratch.

Interviewer: What made you confident the compressed schedule would hold?

Participant: Honestly, mostly that I'd done a version of this before and it worked out then. I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead.

Interviewer: What information would have changed that estimate?

Participant: If I'd actually broken out hours for three-agency sign-off separately instead of folding it into "coordination," I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up.

Interviewer: Still in that same phase — you also had a choice about which scenario format to build from. What drove that?

Participant: Yeah, there was a newer modular design format some of the stakeholders floated, supposedly better suited to multi-agency exercises. But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in.

Interviewer: Did you compare how the two formats actually performed for training outcomes?

Participant: Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure.

Interviewer: Let's move to the severity decision. What was on the table?

Participant: The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years. There was real pressure to keep the scenario grounded in something the community would find plausible.

Interviewer: How did you weigh the modeling against that history?

Participant: I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face.

Interviewer: Around that same time, you were part of an AAR review for a peer's exercise. What happened there?

Participant: Right, a planner in another county got flagged for an unrealistically mild scenario — didn't stress escalation procedures at all. In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time.

Interviewer: Did you apply the same scrutiny to your own severity choice that you applied to theirs?

Participant: Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard.

Interviewer: Third decision point — the training injects. What were the options?

Participant: We only had production time to fully build one category. Option one was photo and video clips of levee overtopping — dramatic, but slow to produce. Option two was the data packages — stream gauge readouts, GIS flow-rate shapefiles — less visually interesting but more specific for EOC modeling decisions.

Interviewer: Which did you prioritize, and why?

Participant: I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool.

Interviewer: Did you weigh how well each format supported the actual operational decisions evaluators would need to make?

Participant: Less than I probably should have, in retrospect. The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them.

Interviewer: Last decision point — the Controller-Evaluator handbook. What went into that?

Participant: I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary.

Interviewer: Was there any indication a glossary might be needed?

Participant: There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left.

Interviewer: Looking back across all four decisions — if you'd had two more weeks, what would you have done differently?

Participant: Probably built in a real contingency buffer up front instead of assuming the old timeline would hold, and maybe split production time more evenly between the visual and data injects.

Interviewer: And if a different planner had taken over halfway through?

Participant: They might have pushed harder on the severity call, given the modeling was pretty clear. And they might not have carried the same assumptions I had about what "obvious" means in the handbook, since they wouldn't have fifteen years of the same habits behind them.

Interviewer: Anything you'd flag as uncertain even now?

Participant: Whether the milder scenario actually undercut the escalation testing, or whether it was just a rough exercise day for other reasons — I genuinely don't know. Same with the handbook; the scoring inconsistencies could've come from a dozen things, not just the shorthand.

Interviewer: That's a good place to stop. Thanks for the detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Planning Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Anchoring project timeline on a smaller prior project without adjusting for added scope/reduced staffing"
      },
      {
        "bias": "Normality Bias",
        "occurrences": 1,
        "mechanism_constraint": "Scaling down hazard severity based on lack of recent local occurrence despite updated risk data"
      },
      {
        "bias": "Bias Blind Spot",
        "occurrences": 1,
        "mechanism_constraint": "Judging a peer's design flaw as unlikely in own concurrent work without equivalent self-scrutiny"
      },
      {
        "bias": "Picture Superiority",
        "occurrences": 1,
        "mechanism_constraint": "Prioritizing visual injects over data-rich injects primarily for memorability rather than operational relevance"
      },
      {
        "bias": "Mere Exposure",
        "occurrences": 1,
        "mechanism_constraint": "Preferring a familiar prior template over a newly proposed format absent comparative evidence"
      },
      {
        "bias": "Curse of Knowledge",
        "occurrences": 1,
        "mechanism_constraint": "Assuming specialist shorthand is self-evident to less-experienced partner-agency evaluators"
      }
    ],
    "target_bias_names": [
      "Planning Fallacy",
      "Normality Bias",
      "Bias Blind Spot",
      "Picture Superiority",
      "Mere Exposure",
      "Curse of Knowledge"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Planning Fallacy", "requested_occurrences": 1},
      {"bias": "Normality Bias", "requested_occurrences": 1},
      {"bias": "Bias Blind Spot", "requested_occurrences": 1},
      {"bias": "Picture Superiority", "requested_occurrences": 1},
      {"bias": "Mere Exposure", "requested_occurrences": 1},
      {"bias": "Curse of Knowledge", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Planning Fallacy"},
      {"instance_id": "cb_02", "bias": "Mere Exposure"},
      {"instance_id": "cb_03", "bias": "Normality Bias"},
      {"instance_id": "cb_04", "bias": "Bias Blind Spot"},
      {"instance_id": "cb_05", "bias": "Picture Superiority"},
      {"instance_id": "cb_06", "bias": "Curse of Knowledge"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Planning Fallacy", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Mere Exposure", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Normality Bias", "decision_point": 2},
      {"instance_id": "cb_04", "bias": "Bias Blind Spot", "decision_point": 2},
      {"instance_id": "cb_05", "bias": "Picture Superiority", "decision_point": 3},
      {"instance_id": "cb_06", "bias": "Curse of Knowledge", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "mechanism": "Anchoring timeline estimate on smaller prior project duration without adjusting for added scope/reduced staffing",
        "affected_reasoning_operation": "Duration/effort estimation",
        "evidence_source": "Prior exercise duration record vs. current expanded scope facts",
        "distinctiveness_requirement": "Distinct from cb_02 (format preference) and cb_03 (severity calibration); concerns time estimation specifically"
      },
      {
        "instance_id": "cb_02",
        "bias": "Mere Exposure",
        "mechanism": "Preferring familiar legacy template over newly proposed format absent comparative evidence",
        "affected_reasoning_operation": "Selection among design-format alternatives",
        "evidence_source": "Repeated use of legacy template across three prior cycles vs. new modular proposal",
        "distinctiveness_requirement": "Distinct from cb_01; concerns format choice, not timeline estimation, though co-located at decision point 1"
      },
      {
        "instance_id": "cb_03",
        "bias": "Normality Bias",
        "mechanism": "Scaling hazard severity down based on absence of recent local occurrence despite updated risk modeling",
        "affected_reasoning_operation": "Risk-severity calibration",
        "evidence_source": "Army Corps updated modeling vs. advisory committee's historical-absence framing",
        "distinctiveness_requirement": "Distinct from cb_04; concerns hazard-severity judgment, not self/other evaluation, though co-located at decision point 2"
      },
      {
        "instance_id": "cb_04",
        "bias": "Bias Blind Spot",
        "mechanism": "Attributing peer's design flaw to peer-specific weakness while exempting own concurrent process from equivalent scrutiny",
        "affected_reasoning_operation": "Self-versus-other evaluation of susceptibility to distortion",
        "evidence_source": "Peer AAR criticism discussion vs. designer's own concurrent unreviewed decision",
        "distinctiveness_requirement": "Distinct from cb_03; concerns comparative self-assessment, not the severity decision itself"
      },
      {
        "instance_id": "cb_05",
        "bias": "Picture Superiority",
        "mechanism": "Prioritizing visual injects for memorability over data-rich injects needed for specific operational decisions",
        "affected_reasoning_operation": "Resource allocation among training-material formats",
        "evidence_source": "Past survey recall data on visual injects vs. operational relevance of data packages",
        "distinctiveness_requirement": "Sole instance at decision point 3; no co-located instance to distinguish from"
      },
      {
        "instance_id": "cb_06",
        "bias": "Curse of Knowledge",
        "mechanism": "Assuming specialist shorthand is self-evident to less-experienced partner-agency evaluators",
        "affected_reasoning_operation": "Calibration of explanatory detail for a mixed-background audience",
        "evidence_source": "Designer's own specialist background vs. partner evaluators' documented lower familiarity",
        "distinctiveness_requirement": "Sole instance at decision point 4; no co-located instance to distinguish from"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Planning Fallacy", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Mere Exposure", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Normality Bias", "strength": "subtle"},
      {"instance_id": "cb_04", "bias": "Bias Blind Spot", "strength": "subtle"},
      {"instance_id": "cb_05", "bias": "Picture Superiority", "strength": "subtle"},
      {"instance_id": "cb_06", "bias": "Curse of Knowledge", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Biased_6",
    "domain_id": "EM",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences spread across 4 decision points (2,2,1,1) by mechanism fit and narrative realism; no bias repeated within a decision point; co-located instances (DP1: cb_01/cb_02; DP2: cb_03/cb_04) assigned distinct evidence sources and reasoning operations per instance independence rule.",
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
