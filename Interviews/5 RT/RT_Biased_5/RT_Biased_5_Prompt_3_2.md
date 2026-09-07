You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time. Before we start, I want to confirm you're okay with me recording this for internal process-improvement purposes, and that we can talk candidly about a project that didn't go entirely to plan.

Participant: Sure, that's fine. This one's still fresh for me anyway.

Interviewer: Can you describe your role and what the project was meant to accomplish?

Participant: I'm the capital projects manager for a corridor interlocking replacement — we were swapping out an aging interlocking and signal system on one of our busiest commuter segments, integrating it with our PTC interface. Federal grant money covered a good chunk of it, which meant a fixed obligation deadline. Miss it, and we risk losing part of the funding.

Interviewer: What made this project different from others you'd run?

Participant: The combination, really. Live revenue service running through the work zone, so we only had certain possession windows at night and weekends. A fixed-price design-build contract, so change orders were painful. And a hard federal clock ticking the whole time.

Interviewer: Walk me through what happened, start to finish.

Participant: We kicked off with a baseline schedule and budget. Then during early design we hit a scope question around underground utilities — old conduit, some of it undocumented. We made a call there and moved forward. Mid-construction, that came back to bite us: crews hit an unmapped high-voltage duct and we had a safety stand-down for a couple weeks. Contractor followed that up with a big risk report on cost and schedule impact. Then near the end, we had to decide how to handle systems integration testing with the deadline bearing down on us. We got through commissioning, the system passed, and we hit the funding deadline. But it was tighter than I'd like.

Interviewer: Let's go back to that baseline. What information did you have when you set the schedule?

Participant: The contractor's proposal assumed pretty efficient crew productivity — their best-case numbers. We also had data from a couple of peer agencies that had done similar interlocking swaps, and those ran 28 to 34 months typically. Leadership wanted to show the board real progress against the grant, so there was pressure to commit to something aggressive.

Interviewer: How did you weigh the contractor's numbers against those peer projects?

Participant: Honestly, I leaned on the contractor's proposal more. The peer projects weren't identical setups — different signal vendors, different corridor configurations — so I didn't think the comparison held up perfectly. We went with 24 months. I figured our team was sharper on execution than what those other durations reflected.

Interviewer: Did you revisit that historical range later, once things started slipping?

Participant: Yeah, once productivity started trailing plan, it looked a lot more like those other projects than I'd assumed going in.

Interviewer: Let's move to the utility question. What were you facing there, and what were your options?

Participant: Our utility maps for that stretch were over five years old, and the contractor flagged a few spots near the bore path where they weren't confident what was actually in the ground. We could pay for an updated survey — about $150,000 and three extra weeks — or proceed on the existing maps and manage anything that came up through our normal process.

Interviewer: What tipped it toward proceeding without the survey?

Participant: We have a solid weekly risk-review cadence, and a change-order tracking process that's pretty tight. I felt like if something came up, we'd catch it fast and deal with it through that mechanism rather than paying upfront to eliminate the uncertainty. It felt like an acceptable trade — spend the time and money there, or trust the oversight we already had running.

Interviewer: And what happened after that decision?

Participant: A few months into construction, crews struck a high-voltage duct that wasn't on any of our maps. Full stop on that segment for safety, about two weeks lost, plus the cost of the incident response and re-sequencing.

Interviewer: Looking back at that now, how foreseeable does it feel?

Participant: Honestly? In hindsight it feels almost obvious — that corridor's old, the utility ownership records were a mess, of course something was going to be down there that we didn't know about. It's the kind of thing you look at now and think, how did we not expect that.

Interviewer: At the time, though, how was that risk actually rated?

Participant: Our risk register had it logged as low likelihood. The team didn't flag it as a top concern going in.

Interviewer: Let's talk about the risk report the contractor sent after the strike. What did that process look like?

Participant: It was a substantial document — forty pages, laying out a projected 12 percent cost overrun and about ten weeks of schedule impact. Those numbers were bad enough that I didn't really want to carry them over to the grant side until the next monitoring cycle gave us something a little less ugly to bring forward. I had five business days to sign off. Problem was, that same week I was buried in quarterly board prep.

Interviewer: How did you handle the review given that?

Participant: I read the executive summary, delegated the detailed analysis to one of my leads, and told the team to keep monitoring things as they came in. I didn't ask my lead for a readout on what the detailed numbers actually showed, and I didn't loop in the grant administrator or escalate it up the chain at that point — I figured we'd get a clearer picture once the monitoring caught up.

Interviewer: Did the risk picture change in the following weeks?

Participant: It got worse before we brought it back into focus. We ended up escalating later and requesting a schedule accommodation from the grant side, which added its own headache.

Interviewer: Let's go to the testing decision near the end. What was the situation?

Participant: We had six weeks left before the grant obligation deadline. Standard systems integration testing protocol for this kind of interlocking work is eight weeks. Our signal engineering lead wanted the full eight weeks — no shortcuts. But the grants officer was clear that missing the milestone put around $4 million of funding at risk.

Interviewer: What alternatives did you consider?

Participant: We could ask the federal administrator for a formal extension and keep the full eight-week protocol, or compress testing to five weeks, trimming some of the redundant verification cycles, and hit the deadline as scheduled.

Interviewer: How did you land on compressing it?

Participant: We couldn't afford to lose that $4 million. That was really the driver. The engineering lead's case for the full protocol was sound, but against a funding number that size, protecting the grant took priority.

Interviewer: If the funding situation had been reversed — say that $4 million wasn't already secured, but finishing on time would have earned you an extra $4 million instead — do you think you'd have made the same call?

Participant: Probably not, honestly. If it were more like a bonus we might land versus something we already had in hand, I think we'd have leaned toward keeping the full eight weeks. Protecting money that was already ours felt different than chasing the same amount as upside.

Interviewer: How did the testing decision play out?

Participant: Testing finished in the compressed window, system passed, we hit the deadline and kept the funding. Whether those trimmed verification cycles matter down the road, I honestly don't know yet — too early to say.

Interviewer: If you'd had unlimited time and budget for that survey, would the utility decision have gone differently?

Participant: Probably, yeah — I'd have just paid for it and taken the three weeks. It wasn't that much money relative to the project.

Interviewer: If the grant deadline had had more flexibility, would the testing call have changed?

Participant: Almost certainly. Without that clock, I think we default straight to the full eight weeks, no debate.

Interviewer: What would you tell a peer walking into a similar fixed-price, fixed-deadline project?

Participant: Get your ground-truth data early, before you're locked into a schedule you can't easily unwind. And build in a real buffer against the funding clock so you're not making testing-scope decisions under that kind of pressure at the very end.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased_counterfactual",
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
        "mechanism": "Anchoring baseline schedule on contractor's best-case estimate while discounting available historical duration data from comparable projects.",
        "affected_reasoning_operation": "Duration estimation/forecasting",
        "evidence_source": "Contractor proposal vs. historical peer-agency project durations",
        "distinctiveness_requirement": "Occurs at initiation/baseline-setting; involves forward-looking forecasting, not retrospective judgment or risk-control belief."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Control",
        "mechanism": "Substituting confidence in an internal management process (weekly risk review) for actual reduction of external physical uncertainty (unmapped utilities).",
        "affected_reasoning_operation": "Risk evaluation under incomplete information at the moment of the survey decision",
        "evidence_source": "PM's own process description vs. outdated utility maps/flagged unknowns",
        "distinctiveness_requirement": "Occurs in-the-moment at the survey/schedule decision, distinct from the later retrospective recall at the same decision point (cb_03)."
      },
      {
        "instance_id": "cb_03",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively characterizing the utility conflict as obviously foreseeable, inconsistent with the team's contemporaneous low-likelihood risk rating.",
        "affected_reasoning_operation": "Post-hoc causal attribution / memory reconstruction in response to a reflection probe",
        "evidence_source": "Contemporaneous risk-register rating vs. post-outcome recollection",
        "distinctiveness_requirement": "Occurs only in a later reflective probe response about decision point 2's outcome, not in the original in-the-moment decision (cb_02)."
      },
      {
        "instance_id": "cb_04",
        "bias": "Ostrich Effect",
        "mechanism": "Avoiding direct engagement with an unfavorable, detailed risk/cost report by skimming, delegating without follow-up, and not escalating within the required review window.",
        "affected_reasoning_operation": "Information engagement/evidence-seeking under threat of unfavorable news",
        "evidence_source": "Contractor's 40-page risk/cost report and PM's review behavior",
        "distinctiveness_requirement": "Confined to decision point 3's report-handling behavior; not a repetition of cb_02's control belief or cb_01's forecasting."
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Aversion or Loss Framing effect",
        "mechanism": "Framing the testing-schedule tradeoff predominantly around avoiding the $4M funding loss rather than symmetrically weighing full-protocol safety/reliability value.",
        "affected_reasoning_operation": "Tradeoff evaluation between funding risk and protocol completeness",
        "evidence_source": "Grants officer's loss framing vs. engineering lead's full-protocol recommendation",
        "distinctiveness_requirement": "Occurs at the final decision point only, tied to explicit loss-framed language distinct from all prior instances."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Illusion of Control", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Hindsight Bias", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Ostrich Effect", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Commissioning of an updated utility/geotechnical survey before finalizing the fixed-price baseline schedule",
      "original_state": "Survey requested/considered but not commissioned prior to baseline finalization",
      "changed_state": "Survey skipped entirely; PM relies on active weekly risk-review process to manage unmapped-utility risk as it surfaces",
      "variables_to_hold_constant": [
        "30-month grant obligation deadline and ~$4M defunding risk",
        "Contractor identity and fixed-price contract terms",
        "PM's role, authority, and team composition",
        "Corridor location and utility-age profile",
        "Occurrence and timing of the eventual utility strike"
      ]
    },
    "scenario_id": "RT_Biased_5",
    "domain_id": "RT",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points with mechanism-fit prioritization; decision point 2 hosts two distinct biases (Illusion of Control at time of decision, Hindsight Bias in a later reflective probe about the same decision's outcome), using different reasoning operations and evidence sources as required when a decision point hosts more than one instance.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "30-month grant obligation deadline and ~$4M defunding risk",
      "Contractor identity and fixed-price contract terms",
      "PM's role, authority, and team composition",
      "Corridor location and utility-age profile",
      "Occurrence and timing of the eventual utility strike"
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
