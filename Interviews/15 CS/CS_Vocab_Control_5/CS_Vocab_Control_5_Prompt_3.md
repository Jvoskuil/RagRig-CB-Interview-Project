You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. Quick check-in before we start — this is just a walkthrough of how you handled a specific case, for process review, not a performance evaluation. Can you tell me your role and background?

Participant: Sure. I'm a Vulnerability Management Analyst, been doing this about three years, SOC monitoring before that. I own triage and remediation tracking for our internet-facing assets — patch coordination, compensating controls, closing tickets against our SLA.

Interviewer: Good. Tell me how this case started and what you were trying to achieve.

Participant: Our threat intel feed flagged a new CVE — critical, 9.8 on CVSS, with confirmed exploitation already happening in the wild. It hit the web framework under our legacy order-processing gateway, which is Tier-1 criticality — internet-facing, handles checkout. My objective was to close this within our 30-day SLA without taking that system down during peak sales. Complication: the gateway needs vendor coordination to patch, we had a partial change freeze ten days out, and I was also carrying two other high-severity tickets at the same time.

Interviewer: How did it unfold, in order?

Participant: Day one, alert comes in, I do triage and have to decide between the standard 21-day cycle and pushing for an emergency change board slot. I escalate, and we get a two-hour emergency window — not enough for full regression testing. Around day three we deploy a WAF rule as an interim compensating control. While setting that up I also noticed some odd outbound DNS traffic on the same host, unrelated to the CVE signature, so I opened a separate low-priority item to look into that. About a week in, IT Ops flags that a vendor SIEM correlation rule for this CVE family is now available, so I have to decide what to do with the detection script I'd built for it myself. Then around day 27, with the SLA clock almost out and the real patch still not deployed, I have to decide how to position the ticket for closure.

Interviewer: Let's go through the first one. What made you push for the emergency CAB slot instead of the 21-day cycle?

Participant: I actually wrote up a short comparison for my manager. On one side, waiting 21 days with an exploit already active in the wild against a Tier-1 asset — that's a meaningful probability of exposure over three weeks. On the other side, an emergency patch attempt with a compressed testing window has its own risk of breaking checkout during a high-traffic period. I laid both out, roughly weighted the likelihood of exploitation against the likelihood of a bad deploy, and the exploit-in-the-wild status tipped it toward escalating, but it was close enough that I documented the disruption risk too, in case leadership wanted to weigh it differently.

Interviewer: Did anyone push back on that framing?

Participant: The app owner did, mostly on the disruption side — worried about the two-hour window not being enough for proper testing. That's actually what happened; the window turned out to be too short for full regression, which is why we ended up needing the WAF rule as a bridge.

Interviewer: Second decision — the WAF rule and that DNS anomaly. Walk me through it.

Participant: The dashboard showed a clear spike matching the known exploit payload pattern, so I deployed the WAF rule against that first. In the same dashboard view, there was also this burst of unusual outbound DNS queries from the same host. It wasn't part of the CVE's known indicators, so it didn't belong in this ticket, but I didn't want it sitting unlogged either. I opened a separate, lower-priority task for it right away and assigned it to be looked at in parallel rather than folding it into the CVE investigation or just noting it and moving on.

Interviewer: What was your thinking behind treating it separately rather than either ignoring it or merging it into the main ticket?

Participant: Mixing an unconfirmed anomaly into a critical CVE ticket muddies the SLA tracking for the actual vulnerability. But two things showing up on the same host in the same week is worth someone's attention, so a parallel low-priority task felt like the right way to keep both threads visible without conflating them. That anomaly ended up tracing back to an internal monitoring job that had recently been reconfigured — unrelated to the CVE, closed without further action, but it was worth the half hour it took to check.

Interviewer: Third decision — the script versus the vendor rule.

Participant: Right, I'd written a detection script six months earlier that covered the one payload variant we'd seen. When the vendor rule came out covering multiple variants with less upkeep, IT Ops suggested standardizing on it. I put together a quick comparison — variants covered, maintenance overhead, how each had performed in testing — and decided to run both in parallel for a transition period rather than cutting over immediately or keeping mine as the sole primary.

Interviewer: Why parallel instead of just switching over, given the vendor rule's broader coverage looked better on paper?

Participant: Mainly because neither one had a track record long enough yet in our environment to bet everything on it alone. Running both meant if the vendor rule had an unexpected gap or false-positive issue during rollout, my script was still catching the one variant we knew about, and vice versa. A week later a slightly different variant did show up, and the vendor rule flagged it — which is exactly the kind of gap the parallel run was meant to catch.

Interviewer: Last one — closing the ticket near day 27.

Participant: At that point the actual vendor patch still wasn't deployed, just the WAF rule and both detection tools. Compliance asked for a documented risk position before the SLA deadline. I pulled together everything outstanding — the unpatched root cause, the current dual-tool coverage, the DNS item that had already closed clean — and instead of closing the ticket outright, I escalated the residual risk summary to the CISO for a formal risk-acceptance call, since the underlying patch was still pending.

Interviewer: What made you escalate rather than just close it as adequately mitigated?

Participant: The compensating controls looked solid on paper, but the root cause was still open, and I didn't think that decision should rest on my sign-off alone given it was going past the SLA target. Documenting the gaps and pushing it up felt like the more defensible move than declaring it done.

Interviewer: How confident were you in the compensating controls at that point?

Participant: Reasonably, based on what the dual-tool coverage data showed, but I was explicit in the writeup that "reasonably confident" isn't the same as "resolved," which is part of why I sent it up rather than closing it myself.

Interviewer: If you'd had another week before the deadline, anything different?

Participant: Probably would have pushed harder to get the actual maintenance window scheduled before the freeze, rather than relying on the compensating controls for as long as we did.

Interviewer: If the vendor rule hadn't existed at all, how would detection have looked?

Participant: We'd have been leaning entirely on my script, which only covered the one variant — so that later variant might have slipped through until something else caught it.

Interviewer: If the DNS anomaly had turned out to be related to the CVE, would your sequencing have changed?

Participant: Yes, it would have gotten folded straight into the main ticket and probably accelerated the escalation call. It just happened not to be connected.

Interviewer: Anywhere you think more information up front would have changed a decision?

Participant: Knowing earlier that the emergency window would only be two hours might have changed how much I leaned on the WAF rule versus pushing for a longer maintenance slot from the start.

Interviewer: This has been really useful, thank you.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Loss Framing",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; escalation justification must be evenly weighted between loss and disruption-cost considerations"
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; both the exploit signature and the DNS anomaly must receive documented, parallel attention"
      },
      {
        "bias": "Illusion of control",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; closure/escalation reasoning must not overstate personal control over residual risk"
      },
      {
        "bias": "Recency",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; urgency judgments must be based on documented ticket data, not on an unrelated recent event"
      },
      {
        "bias": "Endowment",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; tool selection must be based on comparative coverage/overhead criteria, not ownership or effort investment"
      }
    ],
    "target_bias_names": [
      "Loss Framing",
      "Selective Attention Bias or Inattentional Blindness",
      "Illusion of control",
      "Recency",
      "Endowment"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Loss Framing",
        "requested_occurrences": 0
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "requested_occurrences": 0
      },
      {
        "bias": "Illusion of control",
        "requested_occurrences": 0
      },
      {
        "bias": "Recency",
        "requested_occurrences": 0
      },
      {
        "bias": "Endowment",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "CS_Biased_5",
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "CS_Vocab_Control_5",
    "domain_id": "CS",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable in the bias-placement sense; this is a vocabulary-matched control requiring zero intended bias instances. Each of the four decision points from the paired biased scenario (CS_Biased_5) was re-resolved using balanced, evidence-based reasoning that mirrors the original's structure, vocabulary, stakeholders, and decision count while explicitly removing the loss-framing, selective-attention, endowment, illusion-of-control, and recency mechanisms.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and role (Cyber Security, Vulnerability Management Analyst)",
      "Occupational objective (triage, mitigate, close CVE within SLA without downtime)",
      "Setting and organizational constraints (legacy gateway, change freeze, competing tickets, 30-day SLA)",
      "Stakeholders (CISO, IT Ops manager, app owner, Compliance/GRC officer, threat intel lead)",
      "Four-decision-point structure and general chronological arc",
      "Technical vocabulary list (CVSS, exploit-in-the-wild, WAF virtual patch, compensating control, residual risk, SIEM correlation rule, CAB, asset criticality tier, patch window, threat intel feed, SLA remediation clock)",
      "Emotional tone and difficulty level (subtle, professional, time-pressured)",
      "Target word count range (1,215-1,485 words)"
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
