You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm — this is a voluntary conversation about how you handled the EDR replacement evaluation earlier this year, purely for internal process review. Nothing here affects performance evaluation. You're the Security Product/Vendor Evaluation Manager on that project, correct?

Participant: That's right. I led the vendor evaluation from shortlist through to the board recommendation.

Interviewer: Good. Let's start broad — what triggered this whole evaluation?

Participant: We had a near-miss in Q1. An affiliate's endpoint got hit with what looked like early-stage ransomware staging — lateral movement, some encrypted command-and-control traffic that our incumbent EDR didn't flag until a threat hunter noticed anomalous SMB activity manually. We contained it before encryption, but the incident review was blunt: our detection had real gaps. Our contract with the incumbent was also up for renewal in about ninety days, so leadership decided this was the moment to replace rather than renew.

Interviewer: What was the objective you were given, and what constraints came with it?

Participant: Close the detection gaps — specifically lateral movement and encrypted C2 — before the board's remediation deadline, and do it within budget. The CISO wanted a shortlist within two weeks because ninety days isn't much runway once you factor in procurement and implementation. We also run on a fairly integrated cloud and SIEM stack, so anything we picked needed to plug into that without a lot of custom engineering. And our red-team capacity was thin — maybe two weeks of testing bandwidth total across everything.

Interviewer: Walk me through what happened first.

Participant: Almost immediately, our SIEM vendor's account rep reached out — they'd heard about the incident through the account team — and proposed we evaluate their three "certified integration partner" EDR products alongside our incumbent. He framed it as saving us weeks of integration testing since those three were pre-validated against our stack. Given the two-week shortlist deadline, that was appealing. I brought it to the CISO, we agreed it made sense, and that became our shortlist: incumbent plus those three.

Interviewer: Did you look at anything outside that list?

Participant: Not formally, no. I skimmed a couple of analyst write-ups just to sanity-check the names, but I didn't commission an independent RFI or request-for-information process. Honestly, the two-week clock was the driving factor — running a broader market scan across eight or ten vendors would have eaten most of that window just on paperwork and calls.

Interviewer: What made you confident that list was sufficient, versus, say, expanding it by even one or two names?

Participant: The integration angle was real — those three had documented connectors into our logging pipeline already, which meant our engineers wouldn't be building anything from scratch. Time was tight, and I weighted that heavily. I didn't do a deep comparison against vendors outside that set because, frankly, the clock made that feel like a luxury we didn't have.

Interviewer: Did you learn anything afterward about vendors that weren't on that list?

Participant: Yeah — a bit later, procurement was doing some contract-comparison work and flagged two other EDR vendors with higher published MITRE ATT&CK technique coverage scores than any of the three we'd tested. They'd never come up because they weren't in the sales rep's bundle. Separately, a CISO at a peer firm mentioned they'd run a much wider search for a similar replacement. Neither of those changed our timeline, but it did make me wonder what we might have missed.

Interviewer: Let's move to the next phase — the proof-of-concept process. How did you decide to evaluate the shortlisted vendors?

Participant: Each vendor offered a POC window, and they also offered their own third-party benchmark reports as a shortcut — essentially, "trust our numbers." I decided against relying on those and instead ran a standardized red-team simulation, same attack playbook, against all three plus the incumbent. Our testing bandwidth was tight, but I thought it was worth spending it on a controlled, apples-to-apples comparison rather than vendor-marketed numbers.

Interviewer: What tipped you toward the in-house simulation over the benchmark reports?

Participant: One vendor's benchmark report claimed near-perfect detection on lateral movement, but when we actually ran our simulation, their live results were noticeably weaker than advertised. That gap alone justified the extra effort. I'd rather have a smaller but trustworthy dataset than a larger one I can't verify.

Interviewer: That makes sense. Let's get into the tier and pricing decision — what happened there?

Participant: The leading vendor after POC testing had two tiers: a standard tier and a premium threat-hunting tier. POC results confirmed the standard tier met our documented detection SLA — it closed the lateral-movement and C2 gaps we cared about. But during the sales presentation, they walked us through a risk exposure calculator projecting the average breach cost we'd avoid — something like several million dollars — if we went with the premium tier instead. The premium tier was about 40% over our budgeted amount.

Interviewer: When you were putting together your recommendation, what evidence carried the most weight?

Participant: If I'm honest, that avoided-cost number stuck with me the most. It was concrete, it was framed around what happens if we don't act — another incident, but worse, uncontained — and given we'd just come out of a near-miss, that scenario felt very real to the board and to me. The standard tier's SLA compliance was in the POC report, sure, but it didn't have an equivalent dollar figure attached to it — nobody had built out what the efficiency or analyst-time savings from the cheaper option would look like in the same terms. So the premium tier's case was just more vivid.

Interviewer: Did anyone push back on the budget variance?

Participant: Finance flagged it — the premium tier exceeded our pre-approved variance threshold — and I had to get an exception signed off. I justified it by pointing to the exposure figure. Later, procurement went back and built a comparable savings case for the standard tier plus a phased upgrade path, and it turned out that route would have met the same SLA at meaningfully lower cost. That wasn't available to me at the time I made the call, though.

Interviewer: What information, if it had existed at that point, might have changed your recommendation?

Participant: Probably that phased-upgrade ROI figure. If I'd had a dollar-for-dollar efficiency case sitting next to the exposure calculator, I think the comparison would have felt more balanced. Instead, one option had a scary number and the other didn't have a number at all.

Interviewer: Last decision point — the rollout recommendation to the board. What happened there?

Participant: We had two paths: full production rollout within sixty days to lock the vendor's renewal pricing, or a thirty-day extended pilot to validate some outstanding false-positive concerns from the POC before committing fully. I recommended the full rollout. The pricing was only guaranteed if we signed within thirty days, and the board wanted a remediation update before the old contract lapsed.

Interviewer: Any uncertainty in that call?

Participant: Some. The false-positive tuning wasn't fully validated yet. But weighing the schedule risk against the pricing lock and the board's deadline, I felt the full rollout was the more defensible path, with a commitment to tune aggressively post-launch.

Interviewer: How did that play out?

Participant: We did see a higher false-positive rate than expected in early production, which took extra tuning cycles. The board asked for a follow-up review at ninety days. Not ideal, but manageable.

Interviewer: Looking back across the whole process, if you'd had an extra month and no budget constraint, would anything have gone differently?

Participant: Probably the shortlist. I'd have liked to run a proper market scan rather than starting from a vendor-curated list. I still think the POC methodology and the rollout timing were sound calls given what I knew.

Interviewer: And if a colleague had challenged the tier decision directly — what do you think that conversation would have looked like?

Participant: They'd probably have asked why we didn't build out the same kind of savings case for the cheaper tier. I don't have a great answer beyond that the exposure number was already sitting in front of us and the other side of the ledger wasn't.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Loss Framing",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Exposure to limited alternatives",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Loss Framing",
      "Exposure to limited alternatives"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Loss Framing",
        "requested_occurrences": 1
      },
      {
        "bias": "Exposure to limited alternatives",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing"
      },
      {
        "instance_id": "cb_02",
        "bias": "Exposure to limited alternatives"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "decision_point": 3
      },
      {
        "instance_id": "cb_02",
        "bias": "Exposure to limited alternatives",
        "decision_point": 1
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "mechanism": "Recommendation anchored on vendor-supplied breach-cost avoidance figure rather than an equivalent gain-framed efficiency figure for the cheaper SLA-compliant option, causing overweighting of the loss-framed evidence and a budget-variance breach.",
        "affected_reasoning_operation": "Weighting and integration of cost/benefit evidence in tier selection",
        "evidence_source": "Vendor risk exposure calculator (loss-framed) vs. absent gain-framed ROI comparison for the standard tier",
        "distinctiveness_requirement": "Must involve the licensing-tier negotiation and the breach-cost-avoidance figure specifically; must not be a restatement of the shortlist-scoping reasoning used for cb_02."
      },
      {
        "instance_id": "cb_02",
        "bias": "Exposure to limited alternatives",
        "mechanism": "Acceptance of a sales-curated, ecosystem-constrained vendor list without commissioning an independent market scan, narrowing the alternative set considered for the entire evaluation before any comparative assessment occurs.",
        "affected_reasoning_operation": "Generation/scoping of the alternative set prior to comparative evaluation",
        "evidence_source": "Sales-rep-curated 'certified integration partner' list vs. absent independent RFI/market scan; later discovery of excluded higher-scoring vendors",
        "distinctiveness_requirement": "Must involve the vendor shortlisting phase and the scoping of which vendors enter consideration; must not be conflated with the tier/pricing reasoning used for cb_01."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "strength": "moderate"
      },
      {
        "instance_id": "cb_02",
        "bias": "Exposure to limited alternatives",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "CS_Biased_2",
    "domain_id": "CS",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences were spread across distinct decision points (DP1 for Exposure to limited alternatives, DP3 for Loss Framing) per mechanism fit: the alternatives-scoping bias was tied to the vendor shortlisting phase, and the loss-framing bias was tied to the tier/pricing negotiation phase where a vendor-supplied loss-avoidance figure was naturally available. DP2 and DP4 were deliberately left neutral to avoid over-concentration and to preserve narrative realism, satisfying the rule against more than two occurrences of the same bias per decision point (moot here since each bias has only one occurrence) and the requirement to check mechanism fit rather than allocate randomly.",
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
