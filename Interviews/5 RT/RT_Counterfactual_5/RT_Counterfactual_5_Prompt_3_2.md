You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time. Before we start, I want to confirm you're okay with me recording this for internal process-improvement purposes, and that we can talk candidly about a project that didn't go entirely to plan.

Participant: Sure, no problem. It's a good one to talk through.

Interviewer: Can you describe your role and what the project was meant to accomplish?

Participant: I'm the capital projects manager for a corridor interlocking replacement — swapping out an aging interlocking and signal system on one of our busiest commuter segments, integrating it with our PTC interface. Federal grant money covered a good chunk of it, so we had a fixed obligation deadline. Miss it, and part of that funding is at risk.

Interviewer: What made this project different from others you'd run?

Participant: Live revenue service running through the work zone, so limited possession windows at night and weekends. A fixed-price design-build contract, which makes change orders painful. And that federal clock running the whole time.

Interviewer: Walk me through what happened, start to finish.

Participant: We set a baseline schedule and budget up front. During early design we had a utility-survey question — the corridor's underground records were old — and we decided to commission an updated survey before locking the schedule. That survey came back mostly clean, but it flagged one segment where the position data had a stated tolerance, meaning the utility was there but not pinned down precisely. We handled that finding a certain way. Mid-construction, crews still hit a conduit conflict in that exact segment, and we had a shorter safety stand-down than you'd get from a totally unknown strike, but a stand-down all the same. Contractor followed with a risk report on the cost and schedule impact. Then near the end we had to decide how to run systems integration testing against the deadline. We got through commissioning, the system passed, and we hit the funding deadline, but it was tight.

Interviewer: Let's start with the baseline schedule. What information did you have?

Participant: The contractor's proposal assumed efficient crew productivity — their best-case numbers. We also had data from peer agencies that had done similar interlocking swaps, running 28 to 34 months typically. Leadership wanted visible progress against the grant, so there was pressure to commit to something aggressive.

Interviewer: How did you weigh those two data points?

Participant: I leaned harder on the contractor's numbers. The peer projects weren't identical — different vendors, different corridor layouts — so the comparison felt soft. We went with 24 months.

Interviewer: Once the survey added three weeks up front, how did that affect the schedule?

Participant: We didn't push the overall target out. We absorbed those three weeks by tightening later construction phases so the external date stayed at 24 months.

Interviewer: Let's go to the survey itself. What did the results tell you, and what did you do with them?

Participant: Utility maps had been over five years old, so we commissioned the updated survey — about $150,000 and three weeks. It came back solid overall, but one segment near the bore path came with a stated tolerance, something like two feet of uncertainty on exact position, because the underlying municipal records for that block were poor to begin with.

Interviewer: What were your options once you saw that tolerance note?

Participant: We could fund extra contingency time and budget specifically for that segment, or rely on our normal process — weekly risk reviews plus the field crew's verification work during excavation — to handle it as it came up.

Interviewer: Which way did you go, and why?

Participant: We didn't add contingency. Field crews verify positions as a matter of course before they dig in any segment, so it felt like that tolerance note was already covered by standard practice. I knew that verification would really only confirm the actual position once we were mobilized inside that possession window — so if something was off, we'd find out on the clock, not ahead of it — but that still felt like enough to keep the segment on plan. Two feet isn't a huge miss, and I didn't see it as something that needed separate budget.

Interviewer: What happened once construction reached that segment?

Participant: Crews still caught a conduit edge that was outside where the drawing showed it, inside that same flagged area. Shorter stand-down than a full unknown-utility strike would cause — a few days, not weeks — but it did stop work on that segment.

Interviewer: Looking back on that now, how foreseeable does it feel?

Participant: Honestly, the survey told us that segment was uncertain. So in hindsight, of course something was going to be slightly off there — it's almost obvious once you say it that way.

Interviewer: At the time, though, how was that segment actually rated?

Participant: Our risk register logged it as low residual risk once the survey came back. We treated the tolerance note as basically resolved by process, not as an open risk.

Interviewer: Let's move to the contractor's risk report. What did that process look like?

Participant: It came in projecting around a 6 percent cost overrun and about four weeks of schedule impact from the segment conflict. Those numbers weren't something I wanted to sit with heading into board season, honestly — reviewing and pushing that forward before the next monitoring cycle gave us anything better felt premature. I had five business days to sign off, and that same week I was buried in quarterly board prep.

Interviewer: How did you handle the review given that?

Participant: I read the executive summary, delegated the detailed analysis to one of my leads without asking for a real readout on what it actually showed, and told the team to keep monitoring. I didn't escalate to the grant administrator during that window.

Interviewer: Did the picture change in the following weeks?

Participant: It crept up a bit before we brought it into focus and eventually asked the grant side for a smaller schedule accommodation than we would have needed with a full unmapped strike.

Interviewer: Now the testing decision near the end. What was the situation?

Participant: Six weeks left before the grant deadline. Standard systems integration testing runs eight weeks. Our engineering lead wanted the full eight, no shortcuts. Grants officer was clear that missing the milestone risked about $4 million of funding we already had secured.

Interviewer: What alternatives did you weigh?

Participant: Request a formal extension and keep the full eight weeks, or compress to five weeks, trimming some redundant verification cycles, to hit the date.

Interviewer: How did you land on compressing it?

Participant: We couldn't afford to lose $4 million that was already ours. That was the deciding factor, even though the engineering lead's case for the full protocol was solid.

Interviewer: If that $4 million had instead been potential new funding you could gain by finishing on time, rather than money you already had, would the call have gone differently?

Participant: Probably, yeah. If it were more like a bonus on the table instead of something already secured, I think we hold the full eight weeks. Losing money we already had in hand felt different from missing out on the same amount.

Interviewer: How did testing play out?

Participant: Finished in the compressed window, system passed, we hit the deadline and kept the funding. Whether the trimmed verification cycles matter down the line, I honestly don't know yet.

Interviewer: What additional information about that tolerance zone would have changed your decision not to add contingency?

Participant: If the survey firm had given us a tighter confidence range, or flagged that segment as a priority-verify area rather than routine, I think we'd have budgeted differently.

Interviewer: Looking back, was the conflict something the team could have anticipated?

Participant: The information was there. We just read the tolerance note as already handled rather than as a live risk.

Interviewer: What would you tell a peer facing a similar project?

Participant: Get your survey done early, but don't stop there — treat any flagged uncertainty as an open item with its own budget line, not something your normal process automatically covers. And build real slack against the funding clock before you're forced into testing-scope decisions at the end.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Hindsight Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Illusion of Control", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Loss Aversion or Loss Framing effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Ostrich Effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Planning Fallacy", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Hindsight Bias",
      "Illusion of Control",
      "Loss Aversion or Loss Framing effect",
      "Ostrich Effect",
      "Planning Fallacy"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Hindsight Bias", "requested_occurrences": 1 },
      { "bias": "Illusion of Control", "requested_occurrences": 1 },
      { "bias": "Loss Aversion or Loss Framing effect", "requested_occurrences": 1 },
      { "bias": "Ostrich Effect", "requested_occurrences": 1 },
      { "bias": "Planning Fallacy", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy" },
      { "instance_id": "cb_02", "bias": "Illusion of Control" },
      { "instance_id": "cb_03", "bias": "Hindsight Bias" },
      { "instance_id": "cb_04", "bias": "Ostrich Effect" },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Illusion of Control", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Hindsight Bias", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Ostrich Effect", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "mechanism": "Anchoring baseline schedule on contractor's best-case estimate while discounting available historical duration data, and later absorbing added survey time via phase compression rather than revising the external target.",
        "affected_reasoning_operation": "Duration estimation/forecasting",
        "evidence_source": "Contractor proposal vs. historical peer-agency project durations",
        "distinctiveness_requirement": "Occurs at initiation/baseline-setting; involves forward-looking forecasting, not the in-the-moment resource-allocation judgment at decision point 2 or the retrospective judgment tied to it."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Control",
        "mechanism": "Treating routine field-inspection/verification practice as sufficient to resolve an explicitly quantified residual position-tolerance uncertainty in the survey, rather than allocating contingency for it.",
        "affected_reasoning_operation": "Risk evaluation and resource allocation in response to a qualified (not absent) data source at the moment of the survey decision",
        "evidence_source": "Survey report's stated tolerance finding vs. PM's description of relying on field-verification process",
        "distinctiveness_requirement": "Occurs in-the-moment at the post-survey resource-allocation decision, distinct from the later retrospective recall at the same decision point (cb_03)."
      },
      {
        "instance_id": "cb_03",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively characterizing the tolerance-zone conflict as obviously foreseeable because the survey flagged it, inconsistent with the team's contemporaneous low-residual-risk rating for that segment.",
        "affected_reasoning_operation": "Post-hoc causal attribution / memory reconstruction in response to a reflection probe",
        "evidence_source": "Contemporaneous risk-register rating vs. post-outcome recollection",
        "distinctiveness_requirement": "Occurs only in a later reflective probe response about decision point 2's outcome, not in the original in-the-moment decision (cb_02)."
      },
      {
        "instance_id": "cb_04",
        "bias": "Ostrich Effect",
        "mechanism": "Avoiding direct engagement with an unfavorable, quantified risk/cost report because the figures are unwelcome, by skimming the summary, delegating without requesting a substantive readout, and not escalating within the required review window.",
        "affected_reasoning_operation": "Information engagement/evidence-seeking under threat of unfavorable news",
        "evidence_source": "Contractor's risk/cost report and PM's described review behavior, including an explicit statement that the figures were unwelcome ahead of board season",
        "distinctiveness_requirement": "Confined to decision point 3's report-handling behavior; not a repetition of cb_02's resource-allocation judgment or cb_01's forecasting."
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Aversion or Loss Framing effect",
        "mechanism": "Framing the testing-schedule tradeoff around avoiding loss of already-secured funding, with an explicit equivalent-gain probe response showing the decision would likely differ if the same amount were an unrealized upside.",
        "affected_reasoning_operation": "Tradeoff evaluation between funding risk and protocol completeness",
        "evidence_source": "Grants officer's loss framing, engineering lead's full-protocol recommendation, and PM's response to the equivalent-gain probe",
        "distinctiveness_requirement": "Occurs at the final decision point only, tied to explicit loss-framed language and the gain-framing contrast, distinct from all prior instances."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Illusion of Control", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Hindsight Bias", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Ostrich Effect", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect", "strength": "moderate" }
    ],
    "paired_scenario_id": "RT_Biased_5",
    "counterfactual_variable": {
      "name": "Commissioning of an updated utility/geotechnical survey before finalizing the fixed-price baseline schedule",
      "original_state": "Not commissioned in the paired scenario (RT_Biased_5); baseline finalized using outdated utility maps",
      "changed_state": "Commissioned in this scenario; survey identifies most utility locations but reports a stated position tolerance in one segment, which the PM manages via field-verification process rather than added contingency",
      "variables_to_hold_constant": [
        "30-month grant obligation deadline and ~$4M defunding risk",
        "Contractor identity and fixed-price contract terms",
        "PM's role, authority, and team composition",
        "Corridor location and utility-age profile",
        "Occurrence of a utility-related disruption at decision point 2, at reduced magnitude",
        "Presence of the contractor risk report and testing-compression decision at decision points 3 and 4"
      ]
    },
    "scenario_id": "RT_Counterfactual_5",
    "domain_id": "RT",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points with mechanism-fit prioritization; decision point 2 hosts two distinct biases (Illusion of Control at the moment of the post-survey resource-allocation decision, Hindsight Bias in a later reflective probe about that decision's outcome), using different reasoning operations and evidence sources, mirroring the paired scenario's allocation while adapting the evidence content to the changed causal variable.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "30-month grant obligation deadline and ~$4M defunding risk",
      "Contractor identity and fixed-price contract terms",
      "PM's role, authority, and team composition",
      "Corridor location and utility-age profile",
      "Occurrence of a utility-related disruption at decision point 2, at reduced magnitude",
      "Presence of the contractor risk report and testing-compression decision at decision points 3 and 4"
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
