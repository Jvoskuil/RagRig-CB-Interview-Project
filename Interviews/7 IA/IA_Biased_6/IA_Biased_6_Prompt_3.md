You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. You can skip anything you're not comfortable sharing. Can you tell me your role and how long you've been doing it?

Participant: Sure. I'm a threat intelligence analyst on the SOC team, been in this seat about four years, mostly financial services environments. My job during shift is triage, attribution, and hunt scoping when something looks like it's more than commodity noise.

Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared?

Participant: It was maybe two hours into an overnight shift. EDR kicked out a cluster of alerts on a trading-support server — not the trading engine itself, but a box that feeds reporting data to it. The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing.

Interviewer: What was your primary objective at that point?

Participant: Get through the queue, keep the shift moving, and not waste the incident response lead's time on something that turns out to be benign. We only had about three hours left in the shift, and I wanted whatever I handed off to be solid, not a guess.

Interviewer: Take me through what happened next, chronologically.

Participant: So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet. About forty minutes later, a follow-up alert showed an outbound connection from that same host to an IP I didn't recognize. That's when I actually opened the case properly. I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me. Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway. Then I pulled a vendor bulletin that had just come in — the vendor portal access was closing soon, so I read it quickly. It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that. Near the end of shift, I had to write up a containment recommendation for the IR lead, and I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of "possibly" and "unclear."

Interviewer: Let's slow down and go through each of those decisions one at a time. First one — the initial Low-severity alert. What cues were you weighing right then?

Participant: Mainly the auto-triage score and my own memory of that server generating false alarms before. No unusual business disruption was reported either, which reinforced it felt routine.

Interviewer: What made you decide to defer the manual log pull rather than doing it right away?

Participant: Time, mostly. The score was Low, I had precedent that Low from that host usually meant nothing, and pulling raw logs is a real time cost. It felt like a reasonable use of triage priority rather than checking every single alert by hand.

Interviewer: Did you consider escalating to the IR lead first instead?

Participant: I thought about it, but that seemed like overkill for a Low score with no other signal at that point. In hindsight, I probably could've spent the fifteen minutes given how the next forty minutes went, but at the time it didn't seem to justify interrupting anyone.

Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for assigning GreyFalcon?

Participant: The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in.

Interviewer: You mentioned the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure. How did that factor in?

Participant: It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.

Interviewer: And the HR database access attempt — GreyFalcon has typically gone after trading or financial data in your prior tracking. How did you read that mismatch?

Participant: My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly. So it didn't strike me as inconsistent with the group, more like an opportunistic pivot they'd make if they were being efficient about it.

Interviewer: Did you weigh that explanation against the possibility that it wasn't GreyFalcon at all?

Participant: Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.

Interviewer: Let's talk about the hunt scope decision, once the vendor bulletin came in. Walk me through how you decided what to include.

Participant: The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources.

Interviewer: The bulletin listed two file-hash IOCs last — how much did those factor into the scope?

Participant: Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.

Interviewer: Was there consideration of scoping broadly across all five IOCs regardless of order?

Participant: There was, briefly — business owners wanted it narrow anyway to avoid downtime on trading-adjacent systems, so narrow scope aligned with what they wanted too. That made it easier to just go with the scope that already made sense to me.

Interviewer: Last decision point — the containment recommendation. You mentioned leaning on the vendor bulletin over a colleague's notes. What drove that?

Participant: Time pressure, for one — I needed something to hand the IR lead within the hour. But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — "possibly," "unclear if," that kind of thing. The vendor version gave me something concrete to act on.

Interviewer: Did you compare the actual evidence underlying each source, separate from how they were written?

Participant: Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.

Interviewer: How confident were you overall in the final recommendation you handed off?

Participant: Reasonably confident, maybe seven out of ten. Enough uncertainty that I flagged it as needing follow-up validation next shift, but I felt the containment steps were defensible given what I had.

Interviewer: Looking back across the shift, if you'd pulled the raw logs immediately in phase one instead of deferring, how do you think things would've unfolded differently?

Participant: I might have caught the odd outbound connection sooner, maybe before the vendor window closed, which could've changed how much I leaned on that bulletin later. Hard to say for certain.

Interviewer: If the vendor bulletin had listed its IOCs in reverse order, hash-based ones first, do you think your scoping would have changed?

Participant: Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope.

Interviewer: Is there a point in this sequence where you'd want a second analyst's independent read before proceeding?

Participant: Probably the attribution step. That's where I moved fastest from one piece of strong evidence to a full working theory, and a second set of eyes might have pushed back on the infrastructure mismatch or the HR access pattern before I built the rest of the shift around it.

Interviewer: That's helpful, thank you. I think that covers what I need.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Confimation Bias", "occurrences": 1, "mechanism_constraint": "Selective weighting of registry-key IOC over discordant C2 infrastructure pattern during attribution." },
      { "bias": "Complacency Bias", "occurrences": 1, "mechanism_constraint": "Deferred manual verification due to trust in automated EDR severity scoring." },
      { "bias": "Explanation bias", "occurrences": 1, "mechanism_constraint": "Scope decision justified by narrative coherence rather than independent testing of alternative explanation." },
      { "bias": "Fluency effects", "occurrences": 1, "mechanism_constraint": "Preference for polished vendor bulletin over hedged internal notes based on presentation, not evidentiary rigor." },
      { "bias": "Mirror Imaging Bias", "occurrences": 1, "mechanism_constraint": "Adversary target-selection interpreted via analyst's own strategic logic rather than tested against alternative adversary motivations." },
      { "bias": "Order effects", "occurrences": 1, "mechanism_constraint": "Scope decision disproportionately shaped by first-listed IOC in vendor bulletin." }
    ],
    "target_bias_names": [
      "Confimation Bias", "Complacency Bias", "Explanation bias", "Fluency effects", "Mirror Imaging Bias", "Order effects"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confimation Bias", "requested_occurrences": 1 },
      { "bias": "Complacency Bias", "requested_occurrences": 1 },
      { "bias": "Explanation bias", "requested_occurrences": 1 },
      { "bias": "Fluency effects", "requested_occurrences": 1 },
      { "bias": "Mirror Imaging Bias", "requested_occurrences": 1 },
      { "bias": "Order effects", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cp_01", "bias": "Complacency Bias" },
      { "instance_id": "cb_01", "bias": "Confimation Bias" },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias" },
      { "instance_id": "ex_01", "bias": "Explanation bias" },
      { "instance_id": "oe_01", "bias": "Order effects" },
      { "instance_id": "fl_01", "bias": "Fluency effects" }
    ],
    "intended_decision_points": [
      { "instance_id": "cp_01", "bias": "Complacency Bias", "decision_point": 1 },
      { "instance_id": "cb_01", "bias": "Confimation Bias", "decision_point": 2 },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias", "decision_point": 2 },
      { "instance_id": "ex_01", "bias": "Explanation bias", "decision_point": 3 },
      { "instance_id": "oe_01", "bias": "Order effects", "decision_point": 3 },
      { "instance_id": "fl_01", "bias": "Fluency effects", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cp_01",
        "bias": "Complacency Bias",
        "mechanism": "Trust in automated EDR triage score substitutes for independent manual log verification despite available time.",
        "affected_reasoning_operation": "Verification/evidence-gathering decision",
        "evidence_source": "EDR auto-triage severity score vs. available raw logs",
        "distinctiveness_requirement": "Only complacency instance; tied uniquely to automated tool trust at DP1, distinct from all other instances by decision point and evidence source."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confimation Bias",
        "mechanism": "Registry-key IOC match is treated as confirming evidence for GreyFalcon attribution while the discordant C2 registration pattern is not actively sought or weighted.",
        "affected_reasoning_operation": "Evidence weighting during attribution",
        "evidence_source": "Registry-key artifact match vs. C2 domain registration pattern",
        "distinctiveness_requirement": "Distinct from mi_01 (same DP2) by evidence source: cb_01 uses IOC-matching evidence; mi_01 uses target-selection telemetry and adversary-intent reasoning."
      },
      {
        "instance_id": "mi_01",
        "bias": "Mirror Imaging Bias",
        "mechanism": "Adversary's HR-database target selection is explained via the analyst's own strategic logic ('what I would do to maximize leverage') rather than by testing alternative adversary motivations against GreyFalcon's documented historical pattern.",
        "affected_reasoning_operation": "Inference about adversary intent",
        "evidence_source": "Internal telemetry on HR database access attempt vs. GreyFalcon's historical targeting pattern",
        "distinctiveness_requirement": "Distinct from cb_01 by reasoning operation (intent inference vs. attribution-evidence weighting) though sharing DP2."
      },
      {
        "instance_id": "ex_01",
        "bias": "Explanation bias",
        "mechanism": "Scope decision is justified by the internal coherence of the pre-existing GreyFalcon narrative rather than by independently comparing it against an equally plausible alternative explanation.",
        "affected_reasoning_operation": "Scope-determination reasoning via narrative integration",
        "evidence_source": "Working attribution narrative vs. alternative commodity-malware/insider-misconfiguration explanation",
        "distinctiveness_requirement": "Distinct from oe_01 (same DP3) by mechanism: ex_01 is about narrative-coherence justification, not IOC list ordering."
      },
      {
        "instance_id": "oe_01",
        "bias": "Order effects",
        "mechanism": "The fixed listing order of the vendor bulletin's five IOCs (dramatic signature first) disproportionately shapes the scope decision toward the first-listed item over later, more diagnostic hashes.",
        "affected_reasoning_operation": "Weighting of listed evidence items during scope selection",
        "evidence_source": "Vendor bulletin IOC list order",
        "distinctiveness_requirement": "Distinct from ex_01 by reasoning operation: positional weighting of a list vs. narrative-fit justification, though both occur at DP3."
      },
      {
        "instance_id": "fl_01",
        "bias": "Fluency effects",
        "mechanism": "Confident, polished presentation of the vendor bulletin is treated as an indicator of reliability relative to hedged internal notes, independent of underlying evidentiary rigor.",
        "affected_reasoning_operation": "Source-credibility weighting during containment recommendation",
        "evidence_source": "Vendor bulletin presentation quality vs. internal analyst's hedged raw notes",
        "distinctiveness_requirement": "Only fluency instance; uniquely tied to DP4 containment decision and presentation-based credibility judgment."
      }
    ],
    "intended_strength": [
      { "instance_id": "cp_01", "bias": "Complacency Bias", "strength": "subtle" },
      { "instance_id": "cb_01", "bias": "Confimation Bias", "strength": "subtle" },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias", "strength": "subtle" },
      { "instance_id": "ex_01", "bias": "Explanation bias", "strength": "subtle" },
      { "instance_id": "oe_01", "bias": "Order effects", "strength": "subtle" },
      { "instance_id": "fl_01", "bias": "Fluency effects", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_6",
    "domain_id": "IA",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences spread across 4 decision points respecting mechanism fit: DP1=1 (Complacency), DP2=2 (Confirmation, Mirror Imaging; distinguished by evidence source and reasoning operation), DP3=2 (Explanation bias, Order effects; distinguished by mechanism), DP4=1 (Fluency effects). No decision point received more than two instances, and no two instances of the same bias were assigned, satisfying the manifest's per-bias count of 1 each.",
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
