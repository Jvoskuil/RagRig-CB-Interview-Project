You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and you're comfortable speaking openly about how the decisions unfolded?

Participant: Yes, that's fine. I've done these debriefs before after audits.

Interviewer: Great. Can you start by telling me your role and a bit about the situation we're discussing?

Participant: I'm the Continuing Airworthiness Manager for our turboprop fleet. This one involved a lease-return aircraft — we had five days to get it back to the lessor in contract condition, and during the pre-return borescope inspection, the hangar crew flagged hydraulic seepage at a fitting that had already come up twice in the prior eight months.

Interviewer: What was going through your mind when that finding came in?

Participant: Honestly, my first reaction was "there it is again." We'd seen this fitting seep before, logged it, and it never went anywhere. The reliability trend data showed the seepage rate was within MEL tolerance historically, so nothing about the number itself was alarming. But we were also five days from a contractual deadline with financial penalties attached, so I wanted to move quickly.

Interviewer: Walk me through what happened next, chronologically.

Participant: Sure. Day one, the borescope finding comes in. I pull up the maintenance history, see the two prior logs, and my line engineer — Tomas, he's been with us over twenty years — takes a look and says it's the same seepage pattern we've always seen. Day two, we're deciding how to formally classify it. Tomas is confident it's cosmetic, says this fitting type "just seeps, it doesn't fail badly." Day three, I pull the reliability dashboard for a broader read before writing the disposition memo. Day four and five, we're finalizing release paperwork against the clock, because MRO's engineering support was only contracted through day three.

Interviewer: Let's go back to that first day. What exactly made you comfortable classifying it as routine rather than escalating for expanded inspection?

Participant: The recurrence itself, honestly. Two prior instances, same location, same profile — it fit the pattern we'd already established for this aircraft. Once I saw the third one lined up with the first two, it read to me as confirmation that this was just how this particular fitting behaves, not something new developing. So I deferred it under MEL rather than pulling it into an unscheduled inspection.

Interviewer: Did you consider that three data points over eight months might not be enough to establish a real pattern?

Participant: I mean — in hindsight, sure, three isn't a huge number. But in the moment it felt consistent enough. It wasn't like the readings were random or inconsistent with each other.

Interviewer: What alternative did you weigh at that point?

Participant: The other option was escalating to Quality immediately for an expanded inspection. I set that aside because nothing in the numbers themselves crossed a threshold — it was really the shape of the recurrence that drove my read, not the raw values.

Interviewer: Moving to day two — Tomas's assessment. What was your process for validating what he told you?

Participant: Tomas has been doing this longer than almost anyone on my team. When he said this fitting type doesn't fail catastrophically, just seeps, that carries weight. We didn't commission a fault-tree analysis at that point — partly hangar time, partly that his read seemed like sufficient technical grounds on its own.

Interviewer: Was there a dissenting view from anyone else?

Participant: There was, actually. One of our junior engineers suggested we pull the torque and seal specs to check whether something in the installation had drifted. I didn't follow up on that. It felt like duplicating effort when Tomas had already given a clear read.

Interviewer: What would it have taken for you to pursue the junior engineer's suggestion instead?

Participant: Probably if Tomas himself had seemed less certain, or if the seepage rate had ticked up rather than stayed flat. As it was, his confidence made the spec check feel unnecessary.

Interviewer: Let's talk about day three, the reliability dashboard. What did that show you?

Participant: Green status for that defect category, fleet-wide. That was reassuring — I referenced it directly in the disposition memo as supporting evidence for continued airworthiness.

Interviewer: Did you check whether that green rating accounted for this tail number's specific recurrence history, or whether it was a fleet-average figure?

Participant: I didn't dig into the calculation, no. It's an approved tool, it's what we use for these calls day to day. Between the dashboard and Tomas's read, everything was pointing the same direction, so that consistency across sources gave me a fair amount of confidence in the memo's conclusion.

Interviewer: When you say "everything pointing the same direction" — did you consider that the dashboard and Tomas's assessment might share the same blind spot rather than genuinely corroborating each other?

Participant: That's a fair question. I didn't frame it that way at the time. It felt like two independent checks agreeing, which is usually a good sign.

Interviewer: Let's move to the final decision — releasing the aircraft. What was the state of play by day four?

Participant: MRO's engineering support had already left, deadline was two days out, and the seepage was still within tolerance with no new defect. I authorized release to service and we returned the aircraft on schedule. I did flag a borescope recheck for the next inspection interval, but didn't make it mandatory before dispatch.

Interviewer: How much did the two-day deadline weigh on that call?

Participant: Some, sure — everyone in this industry feels the schedule. But I want to be clear, my release decision itself was based on the tolerance readings and history, not the clock. Other managers might let a deadline push them into a call they're not comfortable with. I don't think that happened here.

Interviewer: You mentioned earlier that hangar pressure and the departing MRO support were very much on your mind through days two and three. How does that square with the release decision being unaffected by timing?

Participant: I see what you're asking. I suppose the schedule was in the background the whole way through — I just don't experience it as something that colors my technical judgment specifically at the end.

Interviewer: What gave you confidence specifically in this aircraft, as opposed to the fitting type generally?

Participant: Fifteen years at this airline, and I've never seen this exact fitting fail badly on any tail. That history made me comfortable that this one would be fine, even with the root cause investigation still technically open.

Interviewer: If the deadline had been three weeks out instead of five days, would anything have gone differently?

Participant: Probably. I likely would have let the fault-tree analysis run to completion before finalizing the memo, rather than resting on Tomas's read and the dashboard.

Interviewer: And if a less senior engineer had given you the same "it just seeps" assessment — would you have weighed it the same way?

Participant: Probably not as heavily. Tomas's tenure is a big part of why that carried the weight it did.

Interviewer: Looking back, what would you do differently if this situation happened again tomorrow?

Participant: I'd probably push harder for that fault-tree analysis before finalizing the disposition, and maybe not treat the recurrence pattern alone as settling the question so early. But I still think the outcome — a clean return with no failure — supports that the underlying judgment wasn't unreasonable.

Interviewer: That's helpful context. Thank you for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Apophenia or Correlation Bias", "occurrences": 1, "mechanism_constraint": "Recurrence-as-pattern inference from limited sample"},
      {"bias": "Automaticity or Automation Bias", "occurrences": 1, "mechanism_constraint": "Unverified reliance on automated dashboard output"},
      {"bias": "Bias Blind Spot", "occurrences": 1, "mechanism_constraint": "Self-exemption from deadline pressure acknowledged generally in others"},
      {"bias": "Normalcy Bias", "occurrences": 1, "mechanism_constraint": "Assumption of behavioral continuity absent formal analysis"},
      {"bias": "Experience Bias or Trusting expert intuition", "occurrences": 1, "mechanism_constraint": "Seniority-based deference overriding structured analysis"},
      {"bias": "Illusion of Validity", "occurrences": 1, "mechanism_constraint": "Confidence from convergence of non-independent unverified sources"},
      {"bias": "Optimism Bias", "occurrences": 1, "mechanism_constraint": "Personal failure-free history projected onto specific unresolved case"}
    ],
    "target_bias_names": [
      "Apophenia or Correlation Bias",
      "Automaticity or Automation Bias",
      "Bias Blind Spot",
      "Normalcy Bias",
      "Experience Bias or Trusting expert intuition",
      "Illusion of Validity",
      "Optimism Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Apophenia or Correlation Bias", "requested_occurrences": 1},
      {"bias": "Automaticity or Automation Bias", "requested_occurrences": 1},
      {"bias": "Bias Blind Spot", "requested_occurrences": 1},
      {"bias": "Normalcy Bias", "requested_occurrences": 1},
      {"bias": "Experience Bias or Trusting expert intuition", "requested_occurrences": 1},
      {"bias": "Illusion of Validity", "requested_occurrences": 1},
      {"bias": "Optimism Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "AV7_apo_01", "bias": "Apophenia or Correlation Bias"},
      {"instance_id": "AV7_aut_01", "bias": "Automaticity or Automation Bias"},
      {"instance_id": "AV7_bbs_01", "bias": "Bias Blind Spot"},
      {"instance_id": "AV7_norm_01", "bias": "Normalcy Bias"},
      {"instance_id": "AV7_exp_01", "bias": "Experience Bias or Trusting expert intuition"},
      {"instance_id": "AV7_iov_01", "bias": "Illusion of Validity"},
      {"instance_id": "AV7_opt_01", "bias": "Optimism Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "AV7_apo_01", "bias": "Apophenia or Correlation Bias", "decision_point": 1},
      {"instance_id": "AV7_aut_01", "bias": "Automaticity or Automation Bias", "decision_point": 3},
      {"instance_id": "AV7_bbs_01", "bias": "Bias Blind Spot", "decision_point": 4},
      {"instance_id": "AV7_norm_01", "bias": "Normalcy Bias", "decision_point": 2},
      {"instance_id": "AV7_exp_01", "bias": "Experience Bias or Trusting expert intuition", "decision_point": 2},
      {"instance_id": "AV7_iov_01", "bias": "Illusion of Validity", "decision_point": 3},
      {"instance_id": "AV7_opt_01", "bias": "Optimism Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "AV7_apo_01",
        "bias": "Apophenia or Correlation Bias",
        "mechanism": "Treating third recurrence as confirming a meaningful stable pattern from a two-point history, using perceived pattern itself as justification for deferral",
        "affected_reasoning_operation": "Pattern classification from limited historical data",
        "evidence_source": "Two prior seepage logs plus current third finding",
        "distinctiveness_requirement": "Distinct from normalcy bias (AV7_norm_01) because this instance concerns inferring a causal/meaningful pattern from sparse data at intake, not assuming future continuity of an established norm at a later stage"
      },
      {
        "instance_id": "AV7_aut_01",
        "bias": "Automaticity or Automation Bias",
        "mechanism": "Accepting automated dashboard's fleet-average green status as authoritative without manual verification against tail-specific data",
        "affected_reasoning_operation": "Evidence weighting and verification of automated tool output",
        "evidence_source": "Reliability dashboard status indicator",
        "distinctiveness_requirement": "Distinct from illusion of validity (AV7_iov_01) because this instance is specifically about deferring to an automated system's output rather than about confidence arising from convergence of multiple sources"
      },
      {
        "instance_id": "AV7_bbs_01",
        "bias": "Bias Blind Spot",
        "mechanism": "Acknowledging deadline pressure affects others generally while denying it affected own final technical judgment, despite prior self-description of schedule strain",
        "affected_reasoning_operation": "Self-assessment during probe response about one's own decision influences",
        "evidence_source": "Manager's own probe response contrasted with earlier timeline statements",
        "distinctiveness_requirement": "Distinct from optimism bias (AV7_opt_01) because this instance concerns asymmetric self-perception of susceptibility to pressure, not projection of favorable outcome probability"
      },
      {
        "instance_id": "AV7_norm_01",
        "bias": "Normalcy Bias",
        "mechanism": "Assuming continued benign behavior of the fitting because it has always behaved that way, without seeking analysis that could reveal a departure from the pattern",
        "affected_reasoning_operation": "Risk projection under uncertainty at mid-timeline decision",
        "evidence_source": "Engineer's characterization of typical fitting behavior; absence of fault-tree analysis",
        "distinctiveness_requirement": "Distinct from experience bias (AV7_exp_01) at same decision point because this instance is the manager's own risk-continuity assumption, while AV7_exp_01 is the manager's deference to the engineer's authority/tenure as evidentiary substitute"
      },
      {
        "instance_id": "AV7_exp_01",
        "bias": "Experience Bias or Trusting expert intuition",
        "mechanism": "Substituting senior engineer's tenure-based confident intuition for structured fault-tree analysis, bypassing junior engineer's spec-check suggestion",
        "affected_reasoning_operation": "Evidence source selection and weighting based on perceived authority",
        "evidence_source": "Senior engineer's verbal assessment vs. junior engineer's unaddressed suggestion",
        "distinctiveness_requirement": "Distinct from normalcy bias (AV7_norm_01) at same decision point: this instance is about source authority/credibility weighting, not about assumed continuity of pattern"
      },
      {
        "instance_id": "AV7_iov_01",
        "bias": "Illusion of Validity",
        "mechanism": "High confidence in the disposition memo attributed to apparent consistency between dashboard status and engineer's reassurance, both of which share the same unverified data gap",
        "affected_reasoning_operation": "Confidence calibration based on convergence of unverified sources",
        "evidence_source": "Dashboard status plus engineer's verbal reassurance",
        "distinctiveness_requirement": "Distinct from automation bias (AV7_aut_01) at same decision point: this instance concerns confidence from perceived convergence across sources, not reliance on the automated source alone"
      },
      {
        "instance_id": "AV7_opt_01",
        "bias": "Optimism Bias",
        "mechanism": "Projecting favorable outcome for this specific aircraft based on personal 15-year failure-free history, disregarding the still-open investigation status",
        "affected_reasoning_operation": "Outcome probability estimation under time pressure at final decision",
        "evidence_source": "Personal historical experience; unresolved root cause investigation status",
        "distinctiveness_requirement": "Distinct from bias blind spot (AV7_bbs_01) at same decision point: this instance concerns favorable-outcome projection for the specific case, not self-exemption from a general susceptibility to pressure"
      }
    ],
    "intended_strength": [
      {"instance_id": "AV7_apo_01", "bias": "Apophenia or Correlation Bias", "strength": "subtle"},
      {"instance_id": "AV7_aut_01", "bias": "Automaticity or Automation Bias", "strength": "moderate"},
      {"instance_id": "AV7_bbs_01", "bias": "Bias Blind Spot", "strength": "subtle"},
      {"instance_id": "AV7_norm_01", "bias": "Normalcy Bias", "strength": "subtle"},
      {"instance_id": "AV7_exp_01", "bias": "Experience Bias or Trusting expert intuition", "strength": "moderate"},
      {"instance_id": "AV7_iov_01", "bias": "Illusion of Validity", "strength": "subtle"},
      {"instance_id": "AV7_opt_01", "bias": "Optimism Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of a completed root cause / fault-tree analysis before final release decision",
      "original_state": "No formal root cause analysis performed before release",
      "changed_state": "Completed fault-tree analysis available before release",
      "variables_to_hold_constant": [
        "Lease-return deadline and schedule pressure",
        "Aircraft type and defect history",
        "Personnel involved and stated experience levels",
        "Reliability dashboard output and its underlying data basis"
      ]
    },
    "scenario_id": "AV_Biased_7",
    "domain_id": "AV",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Automatic assignment per mechanism fit and narrative realism: one instance per decision point 1 and 4 respectively (single-bias focus), two distinct-bias instances each sharing decision points 2 and 3 (each pair using different evidence sources and reasoning operations per instance independence rule); no bias exceeds one occurrence; no decision point hosts more than two total bias instances.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Lease-return deadline and schedule pressure",
      "Aircraft type and defect history",
      "Personnel involved and stated experience levels",
      "Reliability dashboard output and its underlying data basis"
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
