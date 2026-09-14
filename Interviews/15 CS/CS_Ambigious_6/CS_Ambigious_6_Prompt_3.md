You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay?

Participant: Sure, that's fine.

Interviewer: Can you tell me a bit about your role?

Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also work through our open findings backlog for compliance reporting, and I sit in on the weekly risk review with application owners.

Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened.

Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. There'd also been some industry news about a breach at another company the week before, though that wasn't really something I was thinking about directly when this came in — just background noise on the security channels, the kind of thing that's always circulating.

Interviewer: When the new CVE came in, what did you do first?

Participant: I read through the advisory, checked the CVSS score and the exposure — internet-facing, no compensating control in front of it, no WAF rule that would catch this pattern — and decided it needed to jump ahead of the backlog. The database finding is serious on paper, but at that point I didn't have a confirmed exploit path for it, just the privilege configuration itself and how long it had been sitting there. So it came down to weighing a confirmed critical exposure against an older, structurally risky one without fresh evidence of active exploitability.

Interviewer: How confident were you in that call?

Participant: Reasonably, but not completely. If I'd had time to pull a fresh risk assessment on the database server that morning, it's possible that would've changed the ordering. I didn't have that luxury, and honestly both items had a legitimate claim to going first.

Interviewer: Where did you route the new CVE?

Participant: Into our standard remediation workflow, tagged toward the web-facing application team, since it touches a customer-facing API and that team handles most of our external-facing patch coordination. It turned out to be more specifically an authentication-bypass issue in the API gateway rather than a typical injection bug, which meant a slightly different exploit chain than I'd first assumed, but the initial routing wasn't far off and the handoff to the right owner happened within the same day.

Interviewer: Walk me through what happened next, later that day.

Participant: While I was cross-referencing the CVE against our asset inventory, the SIEM threw an alert — "privilege escalation, low confidence" — on an internal host. I pulled up the log entry, saw a lateral-movement timestamp that looked a little off from the usual pattern, and there was also an outbound traffic flag on the same host in the same view.

Interviewer: What did you do with that?

Participant: I looked at both — the timestamp and the outbound entry — but neither one on its own had enough corroborating detail to justify pulling away from the CVE triage right then. No matching indicator from the threat intel feed, no other host showing similar activity, nothing in the ticket history suggesting a known campaign. I made a note to loop back once the CVE work was further along and kept going.

Interviewer: Two days later that outbound entry turned out to be linked to an actual low-level compromise. Looking back, do you read that decision differently?

Participant: It's hard to say. Given what I had at the time — a low-confidence label and a somewhat unusual but unconfirmed pattern — I don't think escalating immediately was obviously the right call either. It could've gone either way with the same information in front of me. I've seen similar-looking situations resolve as nothing more than a test process before, and I've also seen them turn out to matter, so I don't think this one particular case tells me much either way about how I generally handle it.

Interviewer: Let's talk about the change window request.

Participant: Patching the API gateway meant an emergency change window during business hours, about twenty minutes of disruption to customer transactions. IT ops needed a written justification to approve that instead of waiting for the weekend cycle.

Interviewer: What went into the justification?

Participant: I put in both the EPSS number — moderate probability, not exceptional — and what the exposure meant in practical terms: the contract implications, the audit angle, and the disruption window itself. I didn't deliberately lead with one over the other, honestly. It read as a fairly standard risk memo, the same format I use for most emergency requests.

Interviewer: Which part do you think actually got it approved?

Participant: I genuinely don't know. IT ops doesn't usually explain which line convinced them. Could've been the score, could've been the business language, could've been that the ask was only for twenty minutes rather than a longer outage. I couldn't tell you with confidence which one mattered most.

Interviewer: Did anything happen afterward that would clarify that?

Participant: Not really. No exploitation was observed against that CVE in the following week, but that doesn't tell me whether the request was overstated or exactly right — we patched it, so there was nothing left to observe either way. It's genuinely inconclusive from where I sit.

Interviewer: Last decision point — scoping which systems got patched.

Participant: The scanner's default view showed two hosts with the matching vulnerable library. Given the deadline, I scoped the ticket to those two, but I also flagged a follow-up sweep of the broader asset inventory for the next week, since I know that default view doesn't always capture everything depending on how assets are tagged in different categories.

Interviewer: One of three additional hosts under a different category turned out to still have the vulnerable library a week later.

Participant: Right, and that's a fair miss. I did build in the follow-up step, it just didn't happen fast enough given everything else on my plate that week. Whether a full manual cross-check up front versus a scheduled follow-up was the better trade-off given the deadline — I go back and forth on that even now.

Interviewer: If you'd had more time before the deadline, would any of these have gone differently?

Participant: Maybe the database server would've gotten a proper fresh look instead of being compared mostly on paper. And I might've pushed the manual inventory check earlier instead of scheduling it after the ticket closed. Hard to know for sure without actually having had that time.

Interviewer: If the scanner had shown five hosts instead of two, would scoping have changed?

Participant: I'd have patched what was in front of me either way, so probably not much different in terms of process — the follow-up sweep would just have had a shorter list left to check afterward.

Interviewer: Looking back, is there anything you'd weigh differently now?

Participant: Maybe how much weight I gave the SIEM alert without a corroborating signal. Not sure I'd act differently even now with the same information, but it's the one I think about.

Interviewer: If you had to write the change-window justification again, would you present it differently?

Participant: Possibly lead more with the numbers and less with the business language, just to see if it changes anything. I don't have strong evidence either framing actually mattered to the outcome.

Interviewer: That's really helpful, thank you for walking through it in detail.

Participant: No problem, glad to help.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      { "bias": "Recency", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Availability Frequency", "occurrences": 0, "mechanism_constraint": "ease of recall of one category over that of another leading to the selection of that category even if the other category is a better fit." },
      { "bias": "Exposure to limited alternatives", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Loss Framing", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 0, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Recency",
      "Availability Frequency",
      "Exposure to limited alternatives",
      "Loss Framing",
      "Selective Attention Bias or Inattentional Blindness"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Recency", "requested_occurrences": 0 },
      { "bias": "Availability Frequency", "requested_occurrences": 0 },
      { "bias": "Exposure to limited alternatives", "requested_occurrences": 0 },
      { "bias": "Loss Framing", "requested_occurrences": 0 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "CS_Biased_6",
    "counterfactual_variable": {
      "name": "Not applicable in this condition",
      "original_state": "Not applicable",
      "changed_state": "Not applicable",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "Analyst role, staffing, and tooling"
      ]
    },
    "scenario_id": "CS_Ambigious_6",
    "domain_id": "CS",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "No occurrences requested; ambiguous_control condition requires zero intended instances of all named target biases. Decision points were instead constructed to preserve genuine ambiguity and plausible non-bias justifications at each of the four decision points, mirroring the structural positions used for bias instances in the paired biased scenario (CS_Biased_6) without instantiating any bias mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "CVE technical details and CVSS score",
      "Backlog composition and the older database finding",
      "48-hour compliance deadline",
      "Analyst role, staffing, and tooling",
      "Four-decision-point structure and domain vocabulary matching CS_Biased_6"
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
