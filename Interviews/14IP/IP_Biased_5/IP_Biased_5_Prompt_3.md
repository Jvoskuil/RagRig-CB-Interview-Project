You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time today. This is a cognitive task analysis interview — I'm just trying to understand how you actually worked through a real production issue, step by step, including what you knew at each point and how you decided what to do. Nothing here is evaluative of you personally, and I may ask you to reconstruct things in detail even if they seem obvious. Sound okay?

Participant: Sure, happy to walk through it. I've got a good one — the Line 3 flash issue before the Meridian shipment a few weeks back.

Interviewer: Perfect. Before we get into the decisions, can you just describe the incident overall — what was the situation and what were you trying to achieve?

Participant: We run three shifts on Line 3, automotive interior clips for Meridian, and we had a 72-hour window to hit a shipment. Partway through a night shift, our scrap rate jumped from about 1.8% up to 6.4%, mostly flash defects, a few short shots mixed in. My objective was straightforward on paper — get quality back under 2% without blowing the ship date and without a full shutdown, since corporate wants VP sign-off for that and we didn't have time to chase approvals.

Interviewer: What were the first signs something was wrong?

Participant: Quality flagged the scrap numbers at shift change, and when I pulled the SPC chart, you could see cavity pressure had started drifting mid-shift. That's usually a decent early indicator. Honestly, my first thought was, this looks almost identical to something we had about six months ago — same symptom pattern, flash showing up in the same cavities. That time it turned out to be ambient humidity messing with resin drying before it hit the hopper.

Interviewer: So walk me through what you did with that first.

Participant: I told the team to re-check drying conditions and humidity logs first, since that's what fixed it last time. We had pressure data sitting right there that could've pointed us toward tooling, but I wanted to rule out humidity given how closely it matched the prior case. In hindsight, tooling wear was already flagged as a possibility by the tooling lead, but I didn't prioritize pulling that data until humidity came back clean.

Interviewer: What did you learn once the humidity results came in?

Participant: They were normal, well within range, so that ruled it out. That's when the tooling lead came back and said the mold had racked up wear cycles since the last inspection — more than we'd expected. So we lost a bit of time chasing the humidity angle before we got to the actual contributing factor.

Interviewer: If you'd had the pressure and wear data side by side from the start, would you have sequenced it differently?

Participant: Possibly. I think if I hadn't had that six-month-old case so fresh in mind, I might have pulled wear data in parallel instead of after.

Interviewer: Let's move to the fix itself. Once wear was confirmed, what were your options?

Participant: Wear was moderate, not severe. We had two real options — an incremental hold-pressure adjustment, which is lower risk but takes longer to validate, or a full mold-insert swap, which is more disruptive but felt like the more thorough fix. We had a press-down window shared with two other product runs, so timing was tight either way.

Interviewer: What tipped you toward the insert swap?

Participant: Honestly, the Line 5 situation from a few months back was still very much on everyone's mind — that insert failure caused a two-day shutdown and we did a whole plant-wide debrief on it. Nobody wanted a repeat of that. When I was weighing the two options, that case kept coming up in my head, and I think it pushed me toward the swap more than a strict comparison of our current wear severity against the threshold where a swap is actually warranted.

Interviewer: Did you compare the wear numbers to your swap criteria directly?

Participant: Not as rigorously as I probably should have, no. I made the call fairly quickly given the press-down window was closing.

Interviewer: What happened after the swap?

Participant: It got done inside the window, which was good. But results were partial — scrap improved but didn't fully get back to baseline, so there was still something unresolved.

Interviewer: Let's go to the third point — the sister-plant call.

Participant: Right, around day two our quality engineer was out sick, so I had less statistical support than I wanted. I got on a call with a peer manager at one of our sister plants, and he mentioned three of our four sister plants had already adopted an aggressive cooling-time reduction protocol for similar flash problems. Corporate quality was also framing it as becoming the standard approach across the network.

Interviewer: What did you decide?

Participant: I adopted it. Three out of four plants using something gave me a lot of confidence it would work here too, and with the engineer out, I didn't have someone in-house to run a full validation against our specific resin lot and cavity geometry before rolling it out.

Interviewer: Did you consider waiting for that validation, or a modified version?

Participant: I did think about a more conservative version, yeah, but given how many plants were already on it, it seemed like the lower-risk path was just to go with what was already proven out there rather than reinvent it locally.

Interviewer: What came out of that?

Participant: Short-term, flash defects dropped, which felt like a win. But two shifts later we started seeing a new warping issue on a subset of parts that hadn't shown up before.

Interviewer: Let's get to the final decision — the rollout call.

Participant: Right, so by the time Meridian's deadline was closing in, our most recent shift — the last eight hours — showed scrap down to 1.5%, best number we'd seen in four days. Corporate quality asked whether we should roll the fix out to Lines 4 and 6 as well.

Interviewer: What was your reasoning?

Participant: Given that shift's numbers, I felt good that we'd nailed it. I told corporate I was confident the root cause was resolved and approved rollout to both lines.

Interviewer: How did that stack up against the full four-day trend?

Participant: The broader trend was messier — more like 2.9% average, some variability, plus the warping thing from the day before. But that last shift felt like real proof it had turned a corner, so that's what I leaned on when I made the call.

Interviewer: Did the warping incident factor into your confidence level at that point?

Participant: Less than it probably should have, looking back. I was focused on getting a clean answer to corporate fast.

Interviewer: What happened with the rollout?

Participant: Lines 4 and 6 looked fine initially, but one of them later threw a tooling alarm we hadn't seen before. And a fuller week-long review afterward showed the wear-related root cause was only partly addressed, not fully resolved like I'd said.

Interviewer: If the last shift's numbers had come in worse instead of better, do you think you'd have made the same call?

Participant: No, honestly, probably not — I think that reading was a big part of why I felt ready to greenlight it.

Interviewer: What would you do differently if this happened again?

Participant: Pull wear and pressure data in parallel from the start instead of chasing the familiar explanation first. And probably wait for a full trend view, not just the best shift, before telling corporate we were done.

Interviewer: This has been really useful — thank you for walking through it in this much detail.

Participant: No problem, happy to help.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Bandwagon effect",
        "occurrences": 1,
        "mechanism_constraint": "Must be driven by sister-plant/network adoption pressure preceding local validation, at decision point 3."
      },
      {
        "bias": "Recency effect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve overweighting the most recent shift's data relative to the fuller multi-day trend, at decision point 4."
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve stated certainty exceeding what available mixed evidence supports, at decision point 4, distinct from the recency-weighting mechanism."
      },
      {
        "bias": "Availability Heuristic",
        "occurrences": 1,
        "mechanism_constraint": "Must be driven by vividness/memorability of the Line 5 insert failure rather than objective wear-severity data, at decision point 2."
      },
      {
        "bias": "Anchoring Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must be driven by surface similarity to a prior six-month-old incident shaping initial hypothesis and inquiry order, at decision point 1."
      }
    ],
    "target_bias_names": [
      "Bandwagon effect",
      "Recency effect",
      "Overconfidence Bias",
      "Availability Heuristic",
      "Anchoring Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Recency effect", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 },
      { "bias": "Availability Heuristic", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias" },
      { "instance_id": "cb_02", "bias": "Availability Heuristic" },
      { "instance_id": "cb_03", "bias": "Bandwagon effect" },
      { "instance_id": "cb_04", "bias": "Recency effect" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Availability Heuristic", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Bandwagon effect", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Recency effect", "decision_point": 4 },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Anchoring Bias",
        "mechanism": "Initial diagnosis fixed on surface similarity to a six-month-old prior incident, shaping inquiry order ahead of available tooling-wear data.",
        "affected_reasoning_operation": "Initial hypothesis formation and information-gathering sequencing",
        "evidence_source": "SPC pressure data and prior incident record",
        "distinctiveness_requirement": "Only intended anchoring instance; occurs at decision point 1 only."
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Heuristic",
        "mechanism": "Fix selection driven by vividness/recency of the Line 5 insert failure narrative rather than current wear-severity data comparison.",
        "affected_reasoning_operation": "Option evaluation and justification for corrective action",
        "evidence_source": "Staff recollection of Line 5 debrief vs. current wear-severity data",
        "distinctiveness_requirement": "Only intended availability instance; occurs at decision point 2 only; distinct from recency effect at decision point 4, which concerns weighting of sequential performance data, not memorability of a past event."
      },
      {
        "instance_id": "cb_03",
        "bias": "Bandwagon effect",
        "mechanism": "Protocol adoption driven by sister-plant/network consensus ahead of local, line-specific validation.",
        "affected_reasoning_operation": "Selection of corrective standard under social/organizational consensus",
        "evidence_source": "Peer manager report of sister-plant adoption and corporate framing",
        "distinctiveness_requirement": "Only intended bandwagon instance; occurs at decision point 3 only."
      },
      {
        "instance_id": "cb_04",
        "bias": "Recency effect",
        "mechanism": "Rollout judgment disproportionately weighted toward the most recent shift's numbers versus the fuller multi-day trend.",
        "affected_reasoning_operation": "Weighting of sequential performance data in forming a resolution judgment",
        "evidence_source": "Most recent shift data vs. four-day trend data",
        "distinctiveness_requirement": "Only intended recency instance; occurs at decision point 4; distinct from overconfidence instance (cb_05), which concerns certainty calibration rather than data-weighting order."
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "mechanism": "Stated certainty of full resolution and rollout approval exceeds what mixed multi-line, multi-day evidence supports.",
        "affected_reasoning_operation": "Confidence calibration in causal judgment and generalization decision",
        "evidence_source": "Partial-improvement and warping signals from phases 2-3 vs. stated certainty",
        "distinctiveness_requirement": "Only intended overconfidence instance; occurs at decision point 4; distinct from recency instance (cb_04) via focus on certainty level rather than data-weighting mechanism."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Availability Heuristic", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Bandwagon effect", "strength": "moderate" },
      { "instance_id": "cb_04", "bias": "Recency effect", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Biased_5",
    "domain_id": "IP",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across four decision points by mechanism fit and narrative realism: one bias per decision point at DP1-DP3, and two distinct biases (Recency effect, Overconfidence Bias) co-located at DP4 using different evidence sources and reasoning operations (data-weighting order vs. certainty calibration), consistent with the no-more-than-two-per-point and distinct-evidence-source rules.",
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
