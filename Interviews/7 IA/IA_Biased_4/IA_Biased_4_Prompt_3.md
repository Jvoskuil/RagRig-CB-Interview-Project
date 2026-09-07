You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal case-review and training purposes only, and I'll be asking you to walk me through a specific case in detail. You're free to skip anything you're not comfortable discussing. Can you first tell me your role and how long you've been doing this kind of work?

Participant: Sure. I'm a financial crime intelligence analyst on the FIU team, been here about six years, mostly focused on trade finance and sanctions-related typologies. Before that I did two years in transaction monitoring.

Interviewer: Great, thanks. I want to focus on a specific case — the Meridian Trading matter. Can you walk me through how it first came to your attention and what you were trying to accomplish?

Participant: Right, so this came in through an automated alert — three invoices from Meridian Trading LLC with quantity and value mismatches, which is a classic flag for trade-based money laundering. My objective was straightforward on paper: figure out whether this was probable sanctions evasion and, if so, get a defensible escalation to compliance and law enforcement before the filing window closed. We had ten business days from the alert.

Interviewer: What did the alert batch actually contain?

Participant: A cluster of counterparties. Meridian was the obvious one — the ultimate beneficial owner shared a registered agent with a company from a case I'd worked about eighteen months earlier, which had ended in a successful sanctions-evasion referral. There was also a separate counterparty in the same batch, a logistics firm, that didn't match anything I recognized. And it was a heavy week — alert volume across the team was well above average, so I needed to move efficiently.

Interviewer: Let's reconstruct the sequence. What did you do right after opening the alert?

Participant: I scoped the review. Given the registered-agent overlap with the prior case, I focused my initial workup on Meridian and its immediate corporate web — pulling registry filings, past KYC refresh notes, that kind of thing. The logistics counterparty I noted but set aside as lower priority since it didn't fit any typology I'd seen before.

Interviewer: What specifically made you decide to scope it that way rather than, say, broadly across everyone in the batch?

Participant: Honestly, the registered-agent match jumped out immediately. That pattern had been reliable before — same agent, similar shell structure, same region. With the volume we were under that week, I didn't feel I had the bandwidth to give equal weight to an entity that had no connection to anything I'd seen. I did glance at the logistics firm's file, but there was nothing that screamed "look here," so I moved on.

Interviewer: Did you consider requesting broader automated screening before locking in that scope?

Participant: I thought about it, but that would've added a day or two, and the Meridian angle felt like the more productive use of time.

Interviewer: What happened with the logistics counterparty afterward?

Participant: A few days later it showed an unusual same-day wire pattern — nothing I'd examined at that point. My team lead actually asked why it wasn't in my initial scoping note. I didn't have a great answer beyond "it didn't fit the pattern I was chasing."

Interviewer: Let's move to the vendor report. Walk me through what happened when that arrived.

Participant: About three days in, our OSINT vendor sent a report concluding Meridian was highly likely tied to the sanctioned end-user. Their argument traced a chain of corporate registry links. The bottom line matched exactly what I already suspected from the registered-agent overlap, so it felt like strong corroboration.

Interviewer: Did anyone raise concerns about the report?

Participant: One of our junior analysts flagged that a step in the vendor's chain — where they treated two similarly named entities as the same legal entity — hadn't been independently verified. I remember thinking that was a fair point to note, but it read to me as a technicality rather than something that undercut the conclusion, since the overall picture fit so well with what I was already building.

Interviewer: What made you weight the report the way you did?

Participant: The conclusion aligned with my working theory, and the vendor has a decent track record. I treated the alignment itself as a kind of confirmation. I didn't go back and independently re-verify that specific entity-matching step before folding the report into the case file.

Interviewer: What did you later learn about that?

Participant: A document pull afterward showed the two entities were actually legally distinct, different beneficial owners entirely. Compliance counsel asked directly what independent verification had been done on that claim, and I had to admit — not much, beyond the vendor's own chain.

Interviewer: Let's talk about the correspondent bank. What was the situation there?

Participant: We'd requested SWIFT records — MT202 and MT103 messages — to confirm the fund flow to the suspected end-user. That correspondent bank, in a secondary jurisdiction, is notoriously slow; historically those requests take twelve to fifteen business days. We were six days from the filing deadline with nothing back yet, no confirmation timeline in writing.

Interviewer: What did you decide to do about the escalation while waiting?

Participant: I held off drafting it. I figured the records would probably come through in time — I wanted the file to be complete with that corroborating piece rather than submit something with a gap in it.

Interviewer: What gave you that expectation, given the track record you mentioned?

Participant: Honestly, more that I wanted it to land that way. Nothing had actually changed with the correspondent bank's typical pace. On day six they came back and said it'd be another ten days.

Interviewer: What happened to the case file at that point?

Participant: My team lead pointed out there wasn't a contingency escalation path drafted, so we were now scrambling.

Interviewer: Let's cover the last piece — the time estimate for remaining work.

Participant: With reconciliation, narrative drafting, and compliance sign-off left, I estimated two business days. I walked through the sequence assuming everything went smoothly — no rework.

Interviewer: How does that estimate compare to similar cases?

Participant: Comparable cross-border verification cases have typically run five to seven days. I didn't really reference that when I made the call, and I still had two other active cases pulling at me.

Interviewer: What happened once you started?

Participant: Reconciliation turned up a discrepancy that needed a follow-up query — cost an extra day. Sign-off took longer too, over a routine question I hadn't anticipated.

Interviewer: Looking back across all four points, what were you least certain about at the time?

Participant: Probably the entity-matching step and whether the records would actually show up. Those felt like the shakiest parts, even while I was moving forward on them.

Interviewer: A couple of hypotheticals. If the logistics counterparty had been flagged as high-risk from the start, how would your approach have changed?

Participant: I'd have split my attention much earlier and probably caught the wire pattern days sooner.

Interviewer: And if you'd known upfront the correspondent bank would take fifteen days?

Participant: I would have drafted a conditional escalation immediately rather than waiting.

Interviewer: Last one — if a colleague had reviewed your time estimate before you committed to it, what do you think they'd have flagged?

Participant: The base rate, probably, and the fact that I was already stretched across two other cases. Fair critique.

Interviewer: That's really helpful, thank you.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Wishful Thinking",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an unsupported expectation of a favorable outcome (records arriving in time) with no confirming evidence and contrary historical base rate."
      },
      {
        "bias": "Belief bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as accepting an argument's conclusion because it matches prior belief, while failing to evaluate the argument's logical/evidentiary validity despite an explicit flag."
      },
      {
        "bias": "Selective Attention Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as attention allocation driven by pattern familiarity, with a non-matching but relevant entity deprioritized without independent evaluation."
      },
      {
        "bias": "Planning fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a time estimate derived from a best-case task sequence that disregards known historical base rates and competing demands."
      }
    ],
    "target_bias_names": [
      "Wishful Thinking",
      "Belief bias",
      "Selective Attention Bias",
      "Planning fallacy"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Wishful Thinking", "requested_occurrences": 1 },
      { "bias": "Belief bias", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias", "requested_occurrences": 1 },
      { "bias": "Planning fallacy", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias" },
      { "instance_id": "bb_01", "bias": "Belief bias" },
      { "instance_id": "wt_01", "bias": "Wishful Thinking" },
      { "instance_id": "pf_01", "bias": "Planning fallacy" }
    ],
    "intended_decision_points": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias", "decision_point": 1 },
      { "instance_id": "bb_01", "bias": "Belief bias", "decision_point": 2 },
      { "instance_id": "wt_01", "bias": "Wishful Thinking", "decision_point": 3 },
      { "instance_id": "pf_01", "bias": "Planning fallacy", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sab_01",
        "bias": "Selective Attention Bias",
        "mechanism": "Attention allocated to pattern-matching entity (shared registered agent), non-matching relevant entity deprioritized without independent risk evaluation",
        "affected_reasoning_operation": "Evidence-selection / initial scoping",
        "evidence_source": "Alert batch metadata: registered-agent match vs. unrelated logistics counterparty",
        "distinctiveness_requirement": "Must be tied to the scoping act at intake, distinct in evidence source and moment from the belief-bias instance at decision point 2, which concerns argument evaluation rather than attention allocation."
      },
      {
        "instance_id": "bb_01",
        "bias": "Belief bias",
        "mechanism": "Conclusion-driven acceptance of vendor argument despite unverified premise flagged by a colleague",
        "affected_reasoning_operation": "Argument evaluation / evidence weighting",
        "evidence_source": "OSINT vendor report and colleague's flag on entity-matching validity",
        "distinctiveness_requirement": "Distinct reasoning operation (validity assessment of an argument) and evidence source (vendor report) from the attention-allocation act in decision point 1."
      },
      {
        "instance_id": "wt_01",
        "bias": "Wishful Thinking",
        "mechanism": "Unsupported expectation that outstanding records arrive in time, contrary to historical turnaround data, driving a delay in contingency drafting",
        "affected_reasoning_operation": "Prediction / risk forecasting",
        "evidence_source": "Correspondent bank historical turnaround record and absence of confirmation",
        "distinctiveness_requirement": "Distinct from bb_01 and sab_01 in that it concerns forecasting a future event under uncertainty rather than evaluating past evidence or allocating attention."
      },
      {
        "instance_id": "pf_01",
        "bias": "Planning fallacy",
        "mechanism": "Best-case task-sequence estimate ignoring historical base rate and competing caseload",
        "affected_reasoning_operation": "Time/effort estimation",
        "evidence_source": "Historical base rate for comparable cases and current competing case list",
        "distinctiveness_requirement": "Distinct from wt_01 in that it concerns a self-generated task-duration estimate rather than an expectation about an external party's action."
      }
    ],
    "intended_strength": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias", "strength": "subtle" },
      { "instance_id": "bb_01", "bias": "Belief bias", "strength": "moderate" },
      { "instance_id": "wt_01", "bias": "Wishful Thinking", "strength": "moderate" },
      { "instance_id": "pf_01", "bias": "Planning fallacy", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_4",
    "domain_id": "IA",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias assigned to a distinct decision point (1:1 mapping across the 4 decision points), chosen for mechanism fit: attention/scoping at intake (DP1), argument evaluation of external evidence (DP2), forecasting under uncertainty (DP3), and self-estimation of task duration (DP4). No bias shares a decision point, so the 'two occurrences at one decision point' distinctiveness rule was not triggered.",
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
