You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — we're reconstructing how you approached a specific blast round, not evaluating performance. Everything you share stays with the study team. Comfortable to proceed?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me a bit about your role and what this particular round involved?

Participant: I'm the drill and blast engineer for the lower sublevels, so I design the pattern, sign off on charging, and coordinate with the geology and ventilation teams before anything gets fired. This one was a production round in Panel 14 — sublevel open stope, about 450 meters down, right next to the service shaft and a ventilation raise, so vibration control matters there. The objective was straightforward: get the round fired on schedule, keep fragmentation good enough for the mill, and stay inside our PPV limits near the shaft.

Interviewer: What was the situation going in?

Participant: We were already a shift behind, and the mill was low on feed, so there was pressure to keep things moving. A couple of days before, geology flagged a minor fault trace crossing maybe a third of the panel, with a bit of moisture along it. Nothing dramatic — geologists flag structure fairly often in that area. We'd been running the same pattern, 2.7 by 3.1 burden and spacing, in three adjacent panels for about two years without issues, so that was the baseline I was working from.

Interviewer: Walk me through what happened once drilling started.

Participant: Drilling went ahead on the standard layout. A handful of holes near the fault trace came back wet, and the deviation survey showed a few of them drifting more than we'd normally tolerate. The crew mentioned the ground felt a bit looser in that section, but it went into the shift log as a routine note, nothing flagged for follow-up. Once charging started, our explosives tech looked at those readings and suggested decking the affected holes and swapping to emulsion for the wet ones instead of running full ANFO columns. I decided to stick with the standard charge across the panel. We fired on the planned timing, adjusted for the shaft-side sensitivity, and afterward the muck pile in that fault section came out coarser than expected, with some overbreak. No safety issues, vibration stayed under limit, but the fragmentation in that corner wasn't what we wanted.

Interviewer: Let's go back through this step by step. First, the pattern decision — once geology handed you that fracture map, what were you actually weighing?

Participant: Mostly time and track record. That pattern's fired dozens of rounds in similar ground without a hiccup, so redesigning burden and spacing for a fault trace that geology themselves called minor felt like it would cost us a day we didn't have, for a problem that historically hasn't caused us grief in that rock.

Interviewer: Did you consider getting additional geotech verification before finalizing it?

Participant: It came up briefly, yeah. But honestly, given how well that pattern's performed, I didn't see it as justified. We tightened the stemming slightly on that side as a small hedge, but kept the design essentially as-is.

Interviewer: What would it have taken for you to actually pause and reverify?

Participant: Probably if geology had called it a major structure, or if we'd seen it show up on more than one panel survey. A single minor trace with a track record like ours behind it didn't feel like enough to slow down for.

Interviewer: Moving to charging — the technician raised a specific concern about the flagged holes. What went through your mind there?

Participant: I've charged plenty of holes that looked like that — a bit wet, slightly off on deviation — and it's never been a real problem when the surrounding rock was competent. I've used full ANFO columns in ground that looked rougher than this and it worked out fine, so I told the crew we'd run it as planned.

Interviewer: Did you go back through the specific deviation numbers or moisture readings for those holes before making that call?

Participant: Not in detail, no. I'd seen the technician's note and I trusted my read of the situation from experience more than I felt I needed to re-pull the log line by line.

Interviewer: What alternatives were on the table at that point?

Participant: Decking with emulsion in the wet holes, like he suggested, or pushing the charging back to resurvey first. Both were doable, just would've eaten into the firing window.

Interviewer: Third decision — the timing and vibration question near the shaft. How did you approach that?

Participant: That one I spent more time on, actually. The monitoring vendor had recommended a longer delay interval for rounds close to sensitive infrastructure, and our live PPV readings were creeping toward the limit on the comparable round before. I compared the fragmentation trade-off against the vibration risk directly and went with the longer sequence on the shaft-facing side. It cost us a bit on fragmentation there, but it kept us clearly under limit.

Interviewer: What made that one feel more resolved than the others?

Participant: We had current numbers right in front of us — actual PPV readings, not just a general sense of things. Easier to make a clean call when the data's that immediate.

Interviewer: Last one — after the round, you had overbreak and coarse fragmentation in the fault section. How did you explain that to yourself and to the mine manager?

Participant: It reminded me a lot of a panel I worked years ago at a different site — same kind of localized fault, same overbreak signature. There, the fix was tightening the pattern and adjusting timing specifically through that corridor, and it worked well. So that's what I recommended here.

Interviewer: Did you look back at this round's own deviation survey or moisture logs as part of that diagnosis?

Participant: Not closely — the pattern matched what I'd seen before closely enough that I was fairly confident in the read.

Interviewer: Was geology brought in to review the current instrumentation before that recommendation went forward?

Participant: Not yet, no. That's probably a next step, but I wanted to give the manager something actionable in the moment.

Interviewer: If the deviation survey had shown something you hadn't seen before, would your charging decision have gone differently?

Participant: Possibly — if it was unfamiliar, I'd have wanted the technician to walk me through it properly rather than just going with my gut.

Interviewer: And if this had been your first round in this panel rather than one of many, do you think the pattern decision changes?

Participant: Probably, yeah. Without that history to lean on, I'd likely have wanted the extra geotech pass before committing.

Interviewer: Last one — looking back, is there a point where different information might have changed how you diagnosed the overbreak?

Participant: If I'd pulled this round's own logs first, side by side with the old site's data, instead of going mostly off memory — that might've told a different story. I'm not sure it would have, but I didn't really test it that way.

Interviewer: That's really helpful, thank you. I think we've got a solid picture of the whole sequence.

Participant: No problem, happy to clarify anything further if it's useful.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Experience Bias",
        "occurrences": 1,
        "mechanism_constraint": "Manifest only as post-blast causal attribution to a remembered prior-mine pattern, discounting current site-specific instrumentation"
      },
      {
        "bias": "Status quo bias",
        "occurrences": 1,
        "mechanism_constraint": "Manifest only as retention of the established blast pattern against new geotechnical information at Decision Point 1"
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": "Manifest only as overriding a specific technician recommendation on charging without re-verifying updated hole data"
      }
    ],
    "target_bias_names": ["Experience Bias", "Status quo bias", "Overconfidence Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Experience Bias", "requested_occurrences": 1},
      {"bias": "Status quo bias", "requested_occurrences": 1},
      {"bias": "Overconfidence Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_02", "bias": "Status quo bias"},
      {"instance_id": "cb_03", "bias": "Overconfidence Bias"},
      {"instance_id": "cb_01", "bias": "Experience Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_02", "bias": "Status quo bias", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Overconfidence Bias", "decision_point": 2},
      {"instance_id": "cb_01", "bias": "Experience Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_02",
        "bias": "Status quo bias",
        "mechanism": "Retaining the established burden/spacing pattern over adapting to a newly mapped fault trace, on grounds of historical track record",
        "affected_reasoning_operation": "Evidence-selection and decision act on pattern redesign",
        "evidence_source": "Geologist's updated fracture map versus two-year pattern performance history",
        "distinctiveness_requirement": "Must be tied specifically to the pattern-retention decision at Decision Point 1, not repeated as a general attitude elsewhere"
      },
      {
        "instance_id": "cb_03",
        "bias": "Overconfidence Bias",
        "mechanism": "Overriding technician's decking/emulsion recommendation based on generalized personal track record rather than re-checking specific updated hole data",
        "affected_reasoning_operation": "Charge-design decision act and evaluation of technician's recommendation",
        "evidence_source": "Updated deviation survey and moisture logs versus engineer's personal experience with similar-looking ground",
        "distinctiveness_requirement": "Must be tied specifically to the charging override at Decision Point 2, distinct in evidence source and moment from the Decision Point 1 pattern decision"
      },
      {
        "instance_id": "cb_01",
        "bias": "Experience Bias",
        "mechanism": "Attributing post-blast overbreak to a remembered prior-mine pattern and recommending its fix without incorporating current round's own instrumentation data",
        "affected_reasoning_operation": "Causal attribution and recommendation act during post-blast evaluation",
        "evidence_source": "Post-blast survey and current round's deviation/moisture logs versus recollection of a prior mine's similar incident",
        "distinctiveness_requirement": "Must be tied specifically to the Decision Point 4 diagnosis/recommendation act, distinct in timing and evidence from the Decision Point 1 and 2 instances"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_02", "bias": "Status quo bias", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Overconfidence Bias", "strength": "subtle"},
      {"instance_id": "cb_01", "bias": "Experience Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": "NONE",
    "counterfactual_variable": {
      "name": "NONE",
      "original_state": "NONE",
      "changed_state": "NONE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_3",
    "domain_id": "MU",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences distributed one-per-bias across three of the four decision points, chosen for mechanism fit: Status quo bias at the pattern-approval decision (DP1), Overconfidence Bias at the charging-override decision (DP2), and Experience Bias at the post-blast causal-attribution decision (DP4). Decision Point 3 (vibration/timing) was deliberately left bias-free to preserve narrative realism and avoid bias clustering, since no manifest entry required more than one occurrence for any bias.",
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
