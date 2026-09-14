You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a retrospective walkthrough of a specific vulnerability case you handled, purely for process review — nothing about individual performance evaluation. Can you tell me your role and how long you've been doing vulnerability management?

Participant: Sure, no problem. I'm a Vulnerability Management Analyst, I've been in this seat about three years now, before that I did general SOC monitoring. Right now I own triage and remediation tracking for our internet-facing assets, so patch coordination, compensating controls, closing out tickets against our SLA.

Interviewer: Great. Walk me through how this particular case started and what you were trying to accomplish.

Participant: So this began when our threat intel feed flagged a new CVE, critical, 9.8 on CVSS, and it had confirmed exploitation already happening in the wild. It hit the web framework running underneath our legacy order-processing gateway — that's the system customers hit when they check out, so it's tagged Tier-1 criticality, internet-facing, revenue-generating. My objective was straightforward on paper: get this closed within our 30-day SLA without taking the gateway down during a peak sales stretch. The complication is that gateway is old, it needs vendor coordination to patch, and we had a partial change freeze coming up in about ten days, so the runway to actually get a maintenance window was shrinking fast. On top of that I had two other high-severity tickets open at the same time, so this wasn't the only thing on my plate.

Interviewer: Given all that, how did the incident actually unfold, in order?

Participant: Day one, the alert comes in, I do initial triage and decide to push for an emergency change board session instead of waiting for the normal 21-day cycle. That gets approved, but it's only a two-hour window, not enough for full regression testing. So around day three, we deploy a WAF rule as an interim compensating control instead of the real patch. While I'm watching the dashboard for that, I notice there's also some odd outbound DNS traffic from the same host, but it's not part of what I'm tracking for this ticket. About a week in, IT Ops points out there's now a vendor SIEM correlation rule available for this CVE family, versus the detection script I'd built myself months earlier, and I decide how to handle that overlap. Then by day 27, with the SLA clock running out and the actual patch still not deployed, I make the call on whether to close the ticket as mitigated.

Interviewer: Let's slow down on the first one — the decision to escalate. What made you push for the emergency CAB slot instead of the standard cycle?

Participant: Honestly, the exploit-in-the-wild status was the trigger, that's usually a hard line for us. But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back. I basically built the case around what we stood to lose if we sat on it for 21 days.

Interviewer: Did you weigh that against the cost of disrupting the gateway with an emergency patch attempt?

Participant: A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that.

Interviewer: Understood. Second decision point — once you had the WAF rule in place, how did you handle the DNS anomaly you mentioned?

Participant: Yeah, so the dashboard was showing a clean match on the known exploit payload pattern, which is what the ticket was actually about, and I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as "anomalous, monitor" and moved on. My focus was really on validating the compensating control against the threat we knew about.

Interviewer: Was there a reason you didn't open a parallel look into the DNS traffic at that point?

Participant: I considered it briefly, but I was heads-down on making sure the WAF rule actually caught the payload variant we had confirmed. Two days later a different analyst ended up escalating that DNS pattern separately as a possible unrelated compromise indicator, so it did turn out to be something. At the time, though, it just wasn't where my attention was.

Interviewer: Third decision — the detection tooling. What happened there?

Participant: Right, so I'd written a detection script for this six months back, tuned it myself against our traffic. When the vendor's SIEM correlation rule came out covering multiple payload variants, IT Ops suggested we just standardize on that instead. I kept my script as the primary and put the vendor rule in a secondary, lower-priority slot.

Interviewer: What was the reasoning behind keeping yours in the lead role, given the vendor rule had broader coverage?

Participant: I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well.

Interviewer: Did that decision have downstream effects?

Participant: About a week later a slightly different payload variant showed up that my script didn't flag, but the vendor rule would have caught it. We caught it another way eventually, but it was a gap.

Interviewer: Last decision point — closing the ticket at day 27. Walk me through that.

Participant: At that point we still didn't have the actual vendor patch deployed, just the WAF rule and my script running as compensating controls. The SLA clock was almost out. I closed it as adequately mitigated. Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup. There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open.

Interviewer: How much of that closure decision was based on the specific residual-risk data for this ticket versus that broader context?

Participant: Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script. I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have.

Interviewer: Was there uncertainty at that point about whether the controls were fully sufficient?

Participant: Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered. A post-incident audit about a month later found there was actually a narrow exposure window that never got closed, though nothing was ever exploited through it.

Interviewer: If you'd had another week before the SLA deadline, would anything have gone differently?

Participant: Probably would have chased down the DNS anomaly properly and maybe pushed harder for the actual vendor patch instead of leaning on compensating controls that long.

Interviewer: If that ransomware story hadn't been in the news that week, do you think the closure decision changes?

Participant: Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then.

Interviewer: And if the vendor SIEM rule had existed from day one, would you have built your own script at all?

Participant: Hard to say — probably still would have, honestly, just because I like understanding exactly what's under the hood. Though maybe I'd have made it secondary from the start instead of the other way around.

Interviewer: Looking back across the whole case, is there a point where you think you gave one piece of evidence more weight than it really deserved?

Participant: Probably the closure call. Between my own confidence in the controls I'd built and everything going on in the news that week, I think I leaned on those more than the actual open items on the ticket.

Interviewer: That's really helpful, thank you for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Loss Framing",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as justification for escalation framed around avoided losses rather than balanced expected-value reasoning"
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as attentional lock onto the confirmed exploit signature causing a visible, co-located anomaly to be underprocessed"
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overstated personal control over residual risk at ticket closure"
      },
      {
        "bias": "Recency",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as urgency judgment anchored to a recent unrelated news event rather than ticket-specific technical data"
      },
      {
        "bias": "Endowment",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as disproportionate valuation of a self-built tool over a comparatively superior alternative due to ownership/effort rather than performance"
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
        "requested_occurrences": 1
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "requested_occurrences": 1
      },
      {
        "bias": "Illusion of control",
        "requested_occurrences": 1
      },
      {
        "bias": "Recency",
        "requested_occurrences": 1
      },
      {
        "bias": "Endowment",
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
        "bias": "Selective Attention Bias or Inattentional Blindness"
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment"
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control"
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "decision_point": 1
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 2
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "decision_point": 3
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "decision_point": 4
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "mechanism": "Escalation justification framed around avoided losses (contract, reputation, trust) rather than balanced expected-value comparison",
        "affected_reasoning_operation": "Risk-urgency judgment and escalation justification",
        "evidence_source": "CVSS/exploit-in-the-wild alert and Tier-1 criticality tag at decision point 1",
        "distinctiveness_requirement": "Distinguished from cb_05 (Recency) by being anchored to prospective business-loss framing at the initial escalation moment, not to a recent external news event at closure"
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Attentional lock onto the confirmed exploit signature causes underprocessing of a co-located, visible but unrelated DNS anomaly",
        "affected_reasoning_operation": "Evidence scanning and triage prioritization within one monitoring view",
        "evidence_source": "Dashboard exploit-signature spike and DNS anomaly at decision point 2",
        "distinctiveness_requirement": "Distinguished from cb_04 (Illusion of control) by occurring during evidence intake/scanning rather than at final confidence judgment about control efficacy"
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "mechanism": "Disproportionate valuation of self-built detection script over a technically superior vendor rule, justified by ownership/effort rather than coverage",
        "affected_reasoning_operation": "Tool-selection and resource-retention decision",
        "evidence_source": "Vendor rule coverage data and script tuning history at decision point 3",
        "distinctiveness_requirement": "Distinguished from cb_04 by concerning tool retention rather than risk-closure confidence, and occurring at a separate decision point"
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "mechanism": "Overstated confidence that personally configured controls fully contain the exploit path despite documented residual-risk data",
        "affected_reasoning_operation": "Residual-risk assessment and ticket-closure judgment",
        "evidence_source": "WAF rule/script status and unresolved anomaly/detection gaps at decision point 4",
        "distinctiveness_requirement": "Distinguished from cb_05 by being expressed through personal-agency confidence language rather than reference to an external recent event"
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency",
        "mechanism": "Urgency judgment for closure timing anchored to a recent unrelated ransomware news event rather than ticket-specific technical residual-risk evidence",
        "affected_reasoning_operation": "Urgency/severity judgment justifying closure timing",
        "evidence_source": "Recent ransomware news reference and SLA clock status at decision point 4",
        "distinctiveness_requirement": "Distinguished from cb_04 by relying on an external, temporally recent event as justification rather than on confidence in self-configured controls"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "CS_Biased_5",
    "domain_id": "CS",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Each bias occurrence assigned to the single decision point offering the best mechanism fit and narrative realism; decision point 4 hosts two distinct biases (illusion of control, recency) rather than a repeated same-bias occurrence, in compliance with the same-bias cap rule; no decision point contains more than two occurrences of any single named bias.",
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
