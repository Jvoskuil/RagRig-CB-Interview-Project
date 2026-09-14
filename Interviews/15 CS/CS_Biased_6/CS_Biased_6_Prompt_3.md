You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm — this is for internal process research, not a performance review, and you can decline to answer anything. Okay?

Participant: Yeah, that's fine.

Interviewer: Can you tell me a bit about your role?

Participant: I'm a vulnerability management analyst on the security operations team. I triage scanner findings, vendor advisories, coordinate patch timelines with IT ops, and escalate anything that looks like active exploitation to incident response. I also chase our open findings backlog for compliance reporting.

Interviewer: Let's talk about the CVE that came in a few weeks back. Walk me through what happened.

Participant: It was mid-morning when a vendor advisory landed — a new CVE, CVSS 9.8, remote code execution, affecting our internet-facing authentication API. At the same time I had roughly forty open findings from the previous week's scan sitting in my queue, with forty-eight hours until our compliance audit report was due. One backlog item was an unpatched database server with excessive service-account privileges, open ninety-plus days. And the week before, there'd been a big breach in the news — a VPN appliance that hadn't been patched — it caused a mess for that company and was all over our internal Slack.

Interviewer: When the new CVE came in, what did you do first?

Participant: My gut reaction was, this is the one — a brand-new critical CVE on an internet-facing system, exactly the profile of what just happened elsewhere. I moved it to the top of the queue and started routing it into our standard remediation workflow. The database finding stayed where it was.

Interviewer: Where did the routing go?

Participant: Into our web-application remediation queue — that's where the bulk of public-facing CVEs usually land, and the team that normally handles this volume, so it goes there almost automatically.

Interviewer: Did you look closely at the advisory's technical detail before routing it?

Participant: I skimmed it — saw "authentication," saw "internet-facing," saw the CVSS score, and that was enough to know it needed to move fast. I didn't dig into the exploit chain right away because time was tight.

Interviewer: Later you found it wasn't quite a standard web-app issue?

Participant: Right — it turned out to be an authentication bypass in the API gateway, a different exploit path than the injection-style stuff that queue usually handles. It got redirected eventually, but that cost some time.

Interviewer: Going back to that first decision — the new CVE and the ninety-day-old database finding were competing for urgency. What made the new one win?

Participant: Honestly, it felt more urgent. The breach story from the week before was fresh, a business like ours hit through an unpatched internet-facing system. This CVE matched that shape almost exactly. The database finding is bad on paper — high privileges, old — but nothing new had happened with it, so it didn't have the same pull.

Interviewer: If you'd ranked them purely on asset criticality and exposure, independent of the news, how would that have gone?

Participant: The database server probably deserved more attention than I gave it. It ended up flagged by the audit team afterward as our most severe open item. But at the time, the CVE felt like the more pressing thing.

Interviewer: Later that day you were cross-referencing the CVE against the asset inventory when something else came up.

Participant: Yeah, while going host by host through the inventory, the SIEM threw an alert — "privilege escalation, low confidence" — on an internal box. That label comes up a lot, and in my experience it's almost always nothing, some test script or scheduled job tripping a rule. I saw the same label I've seen a hundred times and moved on.

Interviewer: Was there anything specific in that alert that stood out?

Participant: There was a log entry with a lateral-movement timestamp that was a little unusual. I registered it existed, but I was heads-down trying to finish the asset match, so I didn't stop to dig in.

Interviewer: Was there anything else on that dashboard view at the time?

Participant: [pause] I'd have to think about that. I was really focused on the inventory cross-reference right then.

Interviewer: There was an anomalous outbound traffic entry flagged on that same host, visible in the same panel. Do you recall it?

Participant: I don't specifically remember it. I was scrolling through host records, not scanning that side panel. It's possible it was there and I just didn't register it — my attention was on matching CVE-affected assets, not general alert triage.

Interviewer: That entry was later linked to a confirmed low-level compromise on that host. Does that change how you see the decision to move past the alert?

Participant: It's easy to say now I should've stopped. At the time, given how often that label turns out to be routine, continuing with the task in front of me felt reasonable. I didn't have a strong signal telling me to drop what I was doing.

Interviewer: Let's talk about the change window request. What went into that?

Participant: IT ops needed written justification to approve an emergency window during business hours instead of the weekend cycle, since patching would disrupt customer transactions for about twenty minutes. I wrote it emphasizing what we stood to lose — client contract exposure, reputational fallout, risk of an audit finding if we didn't move fast.

Interviewer: What did the exploitation data actually say?

Participant: The EPSS score put it at moderate probability, comparable to a handful of things we've handled on the normal weekend schedule over the past year. Not in the exceptional range.

Interviewer: So the justification leaned more on what the company could lose than on that probability figure?

Participant: Yeah, fair point. I framed it around the downside because that's what gets a fast yes from leadership. The EPSS number wasn't really what drove how I wrote it up.

Interviewer: Did it work?

Participant: It did — they approved the window. Though nothing was actually observed exploiting that CVE the following week, so it's hard to say in hindsight whether the urgency was fully warranted.

Interviewer: Last decision point — finalizing which systems to patch.

Participant: The scanner's dashboard, in its default view, showed exactly two hosts matching the vulnerable library signature. Given the deadline, I used that list to scope the ticket and closed it out.

Interviewer: Did you check the asset inventory outside that default view?

Participant: Not at that point. The scanner's list is usually what we work from day to day, so I treated it as the full picture.

Interviewer: There were actually three more hosts with the same vulnerable library, tagged under a different asset category, visible in the inventory with a manual filter change.

Participant: One of those turned up still vulnerable in the follow-up audit scan a week later. A manual cross-check would have caught it, but with the clock running down, the scanner's output was what I had in front of me and it looked complete.

Interviewer: If the VPN breach hadn't been in the news that week, would you have triaged the CVE the same way?

Participant: Possibly not with the same urgency. Hard to fully separate, but that story was fresh, and I think it shaped how fast I moved past the database finding.

Interviewer: If the scanner had surfaced five hosts instead of two, would scoping have gone differently?

Participant: Probably — I'd have just patched whatever the tool showed me. I wasn't second-guessing whether the list was complete.

Interviewer: Anything you'd flag differently now?

Participant: The outbound traffic entry, for sure. And maybe relying less on how an alert label has resolved in the past versus what's specifically in front of me each time.

Interviewer: If you had to write that justification again today, would you frame it differently?

Participant: I might lead with the actual numbers instead of the worst-case story. Though the worst-case framing is usually what gets things approved quickly around here.

Interviewer: That's really helpful, thank you.

Participant: No problem, happy to help.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Recency", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Availability Frequency", "occurrences": 2, "mechanism_constraint": "ease of recall of one category over that of another leading to the selection of that category even if the other category is a better fit." },
      { "bias": "Exposure to limited alternatives", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Loss Framing", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Recency",
      "Availability Frequency",
      "Exposure to limited alternatives",
      "Loss Framing",
      "Selective Attention Bias or Inattentional Blindness"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Recency", "requested_occurrences": 1 },
      { "bias": "Availability Frequency", "requested_occurrences": 2 },
      { "bias": "Exposure to limited alternatives", "requested_occurrences": 1 },
      { "bias": "Loss Framing", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Recency" },
      { "instance_id": "cb_02", "bias": "Availability Frequency" },
      { "instance_id": "cb_03", "bias": "Availability Frequency" },
      { "instance_id": "cb_04", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "cb_05", "bias": "Loss Framing" },
      { "instance_id": "cb_06", "bias": "Exposure to limited alternatives" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Recency", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Availability Frequency", "decision_point": 1 },
      { "instance_id": "cb_03", "bias": "Availability Frequency", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 2 },
      { "instance_id": "cb_05", "bias": "Loss Framing", "decision_point": 3 },
      { "instance_id": "cb_06", "bias": "Exposure to limited alternatives", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Recency",
        "mechanism": "Recent, vivid industry breach report primes a matching mental category, causing the newly disclosed CVE to be judged more urgent than an objectively higher-criticality older finding.",
        "affected_reasoning_operation": "Comparative risk prioritization across two open findings",
        "evidence_source": "Industry breach news report from the prior week vs. 90-day-old database finding",
        "distinctiveness_requirement": "Must be tied specifically to temporal recency of the news event, not to category frequency (distinguishes from cb_02/cb_03) or to attentional failure (distinguishes from cb_04)."
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Frequency",
        "mechanism": "High historical frequency of 'web app vulnerability' tickets makes that category easiest to recall, causing miscategorization of a technically distinct authentication-bypass CVE.",
        "affected_reasoning_operation": "Categorization / evidence-to-category mapping at intake",
        "evidence_source": "Analyst's recalled ticket-volume history for web-app injection issues",
        "distinctiveness_requirement": "Occurs at decision point 1 during initial categorization, using ticket-volume memory as the evidence source; must differ from cb_03's alert-label-history evidence source and decision point."
      },
      {
        "instance_id": "cb_03",
        "bias": "Availability Frequency",
        "mechanism": "Frequent historical benign resolution of a specific SIEM alert label makes 'benign' the easiest-recalled outcome for that label, overriding specific diagnostic log evidence pointing to an active-threat category.",
        "affected_reasoning_operation": "Alert triage / evidence weighting under a familiar label",
        "evidence_source": "Historical resolution-rate memory for the 'privilege escalation - low confidence' alert label",
        "distinctiveness_requirement": "Occurs at decision point 2 during alert disposition, using alert-label resolution-history as the evidence source; must differ from cb_02's decision point and evidence source, and must not be a restatement of cb_04's attentional failure."
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Narrow attentional focus on the asset-matching task causes failure to consciously register a visually available anomalous outbound traffic entry in the same dashboard panel.",
        "affected_reasoning_operation": "Visual monitoring of a shared information display during a concurrent primary task",
        "evidence_source": "Anomalous outbound traffic entry present in the same SIEM dashboard view",
        "distinctiveness_requirement": "Must manifest as failure to notice/report an available visual cue during a concurrent task, distinct from cb_03's memory-based category judgment about an alert the analyst did actively process."
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Framing",
        "mechanism": "Justification for urgency is constructed around potential losses (contract, reputation, audit) rather than equivalent probability data (EPSS score), and this framing—not the underlying probability—drives the urgency judgment communicated to management.",
        "affected_reasoning_operation": "Risk communication / justification construction for a resourcing request",
        "evidence_source": "EPSS exploitation-probability score vs. loss-oriented language used in the written justification",
        "distinctiveness_requirement": "Must be located in the construction/communication of the change-window justification at decision point 3, separate from the prioritization judgment at decision point 1 (cb_01)."
      },
      {
        "instance_id": "cb_06",
        "bias": "Exposure to limited alternatives",
        "mechanism": "The scanner's default-view host list is treated as the complete and exhaustive set of remediation alternatives, without checking the asset inventory outside the default filter that contained additional affected hosts.",
        "affected_reasoning_operation": "Option-generation / scope-definition prior to a final scoping decision",
        "evidence_source": "Scanner default dashboard view vs. asset inventory spreadsheet requiring a manual filter change",
        "distinctiveness_requirement": "Must be located at the final scoping decision (decision point 4) and concern the completeness of the option set itself, not category judgment (cb_02/cb_03) or attentional failure (cb_04)."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Recency", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Availability Frequency", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Availability Frequency", "strength": "moderate" },
      { "instance_id": "cb_04", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Loss Framing", "strength": "subtle" },
      { "instance_id": "cb_06", "bias": "Exposure to limited alternatives", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Prior exposure to a highly publicized industry breach report immediately before CVE triage",
      "original_state": "Analyst had read the publicized VPN-appliance breach report the week before triage",
      "changed_state": "No recent publicized breach report existed before triage",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "Decision points 2 through 4 and their embedded instances",
        "Analyst role, staffing, and tooling"
      ]
    },
    "scenario_id": "CS_Biased_6",
    "domain_id": "CS",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Automatic assignment per mechanism fit and narrative realism: occurrences spread across distinct decision points wherever possible; the two Availability Frequency occurrences were placed at different decision points (1 and 2) using distinct evidence sources (ticket-volume memory vs. alert-label resolution history) to satisfy the distinctiveness requirement; no decision point received more than two instances of any single bias.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "CVE technical details and CVSS score",
      "Backlog composition and the older database finding",
      "48-hour compliance deadline",
      "Analyst role, staffing, and tooling"
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
