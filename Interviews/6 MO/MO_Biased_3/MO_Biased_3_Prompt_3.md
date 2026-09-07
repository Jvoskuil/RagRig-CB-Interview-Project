You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a review of decision-making processes during watch operations, not for any disciplinary purpose. Is that okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me a bit about your role and what you were responsible for monitoring that evening?

Participant: Sure. I was on console for the approach channel, so my job was traffic separation through the narrows — sequencing inbound and outbound vessels, keeping an eye on anything that didn't fit the normal pattern, and coordinating with pilots on larger transits. That evening we had a crude tanker inbound under pilotage, and it was right around dusk, so visibility was starting to get patchy with some fog banks rolling through. My main objective was just making sure the tanker had a clean run through the bend within its tidal window, since that channel doesn't give you much room to maneuver once you're committed.

Interviewer: Okay. Walk me through what happened, from when things started to become unusual.

Participant: About forty minutes before the tanker was due at the bend, I picked up a small contact near there — slow track, kind of wandering. AIS class B tagged it as a local fishing vessel, one that's licensed to work that area, so my first read was that it was probably setting or hauling gear. That's a pretty common sight in that spot, especially in the evening. The radar was showing some inconsistent course data on it, near-zero speed at some points, but with the sea state kicking up a bit of clutter, small-target tracking isn't always clean, so I didn't put much weight on that at first. No distress call, nothing on the radio suggesting trouble, so I logged it as routine and kept my main attention on the tanker's progress.

Interviewer: What happened after that?

Participant: About ten minutes later I noticed the track had drifted a bit further toward the centerline than I'd expect from a boat working gear in that area, and there was a short burst on the radio from around that frequency, but it was garbled — couldn't make out any content. Around then my shift supervisor came on for handover and looked at the display with me. He'd worked that stretch for years and said straight off that this looked typical for that vessel, that he'd seen this exact drift pattern before with boats working that bend. My colleague on the next console glanced over and mentioned the track looked a little off to her, but didn't push it further, and we moved on with finishing the handover log. Then, as the tanker got closer to the tidal cutoff, the supervisor turned to me and framed it as, essentially, are we going to lose the tide window over this or not. I proceeded with the transit as scheduled. Afterward, once the tanker had cleared and things settled, we found the fishing vessel was completely stationary and not answering hails, so I put out a general advisory. Turned out later it had a fouled propeller and needed a tow.

Interviewer: Let's reconstruct that a bit more carefully. Starting with your very first read on the contact — what specific cues led you to call it routine fishing activity?

Participant: Mainly the AIS tag. It came up as a class B unit registered to a fishing vessel we see in that area fairly often, so that matched what I'd expect to see there at that hour. I did notice the COG data wasn't fully consistent with active maneuvering, but I chalked that up to the clutter — that channel gets noisy on radar with any chop, and small targets bounce around in the plot all the time.

Interviewer: Did you go back and check the COG pattern again once you'd made that initial call?

Participant: Not specifically, no. Once I had a plausible explanation for it, my attention went back to the tanker's progress, since that was the higher-priority track at that point.

Interviewer: What alternatives did you consider at that moment?

Participant: I could have hailed the vessel directly on VHF to check status, or just flagged it for tighter radar tracking without contacting them. I didn't do either right away — with no distress call and the AIS type matching, it didn't seem urgent enough to prioritize over the tanker sequencing.

Interviewer: Moving to the handover — tell me more about that conversation with your supervisor and colleague.

Participant: He came on, looked at the plot, and said it looked like the same pattern he'd seen from that boat before — kind of a lazy drift while gear's out. He said it with a lot of confidence, and honestly that matched my own initial read too, so it didn't feel like there was much to question. My colleague said something like "that track looks a little odd" but didn't really elaborate, and nobody asked her to say more. We closed out the handover log with a "no action required" note on that contact.

Interviewer: Did anyone suggest getting an independent re-plot or double-checking the radar data before finalizing that note?

Participant: No, not really. It felt like a fairly settled read at that point, given his experience with that specific vessel.

Interviewer: When the tanker was about fifteen minutes from the bend, how did the decision to proceed take shape?

Participant: That's when my supervisor turned it into a scheduling question — asked whether holding for this would cost us the tide window. Once he framed it that way, the conversation was mostly about whether the delay was worth it, since missing that window would push the tanker's transit back a full cycle. Holding to confirm the fishing vessel's status would almost certainly have meant losing the window.

Interviewer: Was there a point where you weighed the safety margin on its own, separate from the schedule question?

Participant: I think I mostly folded it into the same conversation — the tide window was the thing driving the urgency, so that's the lens I was looking at it through. In hindsight I can see how that shaped which options felt realistic.

Interviewer: What alternatives were on the table there?

Participant: Holding the tanker outside the channel, advising the pilot to slow down and open up the CPA a bit while still proceeding, or just going ahead as scheduled. I went with proceeding as scheduled, given the tide constraint.

Interviewer: And the final decision, after the tanker had cleared and the fishing vessel was found stationary and not responding — how did you land on issuing the advisory?

Participant: At that point the immediate encounter was already resolved, but there was another inbound vessel due within the hour, so I weighed that residual risk against the fact that the current situation had cleared without incident. I decided the advisory was worth it given the upcoming traffic, even though nothing bad had actually happened yet.

Interviewer: How much time pressure did you feel across these decisions?

Participant: The tide window created real pressure during that middle stretch. The final advisory call felt calmer, more like a standard judgment call with time to think it through.

Interviewer: If you'd gotten a clean, confirmed COG reading right at the start, would anything have changed?

Participant: Probably — if it had clearly shown no active movement at all, I likely would've tried to raise them on the radio much earlier instead of letting it ride.

Interviewer: Looking back, if your colleague had pushed harder on that "looks odd" comment, do you think it would have changed the outcome?

Participant: Possibly. If she'd said more specifically what she was seeing, it might have prompted another look at the plot before we closed the handover.

Interviewer: And if the tide-window question had been framed differently — say, purely as a safety check rather than a scheduling one — do you think you'd have weighed the options differently?

Participant: That's a fair point. I might have leaned more toward slowing the pilot down or holding briefly, if the conversation had started from the risk side rather than the schedule side.

Interviewer: Anything you'd want to do differently if this came up again?

Participant: I'd probably push for a direct radio check earlier, before letting an initial read sit unchallenged for too long.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as selective reliance on the AIS vessel-type tag while dismissing/ignoring the conflicting radar COG/SOG trend at decision point 1 only."
      },
      {
        "bias": "Framing Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as the operator's reasoning being anchored to the supervisor's schedule/tide-window framing rather than an independent safety-margin framing, at decision point 3 only."
      },
      {
        "bias": "Groupthink",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as rapid team convergence on the supervisor's assessment with suppression/non-escalation of the second operator's dissenting observation, at decision point 2 only."
      }
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Framing Bias",
      "Groupthink"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confirmation Bias", "requested_occurrences": 1 },
      { "bias": "Framing Bias", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias" },
      { "instance_id": "gt_01", "bias": "Groupthink" },
      { "instance_id": "fb_01", "bias": "Framing Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1 },
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 2 },
      { "instance_id": "fb_01", "bias": "Framing Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective reliance on AIS vessel-type tag as confirming evidence while conflicting radar COG/SOG data is noted but not investigated",
        "affected_reasoning_operation": "Evidence selection and weighting during initial contact classification",
        "evidence_source": "AIS class B tag vs. radar COG/SOG track",
        "distinctiveness_requirement": "Must be the only confirmation-bias-coded moment in the transcript; distinguished from gt_01 and fb_01 by occurring solely within the solo classification act at decision point 1, before any team discussion or framing occurs."
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Rapid team convergence on supervisor's confident prior assessment; dissenting observation from second operator is voiced but not escalated or independently verified",
        "affected_reasoning_operation": "Team-level consensus formation and suppression of dissent during handover",
        "evidence_source": "Supervisor's verbal assessment and second operator's brief drift-trend observation",
        "distinctiveness_requirement": "Must be the only groupthink-coded moment, located specifically in the multi-person handover conversation at decision point 2, distinct from the solo reasoning in cb_01 and the schedule-framed trade-off in fb_01."
      },
      {
        "instance_id": "fb_01",
        "bias": "Framing Bias",
        "mechanism": "Operator's evaluation of reroute-vs-proceed alternatives is anchored to the supervisor's delay-cost framing rather than an independently stated safety-margin framing",
        "affected_reasoning_operation": "Option evaluation and trade-off weighting at the reroute decision",
        "evidence_source": "Supervisor's delay-framed question and tidal transit window constraint",
        "distinctiveness_requirement": "Must be the only framing-bias-coded moment, located specifically at the reroute-vs-proceed trade-off in decision point 3, distinct from the earlier classification (cb_01) and the handover consensus (gt_01)."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "fb_01", "bias": "Framing Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Timing of independent verification of the fishing vessel's status",
      "original_state": "Verification deferred until after the tanker transits the bend",
      "changed_state": "Verification attempted immediately at decision point 1",
      "variables_to_hold_constant": [
        "Channel geometry and tidal window",
        "Weather and visibility conditions",
        "Presence and timing of shift handover",
        "Tanker's original schedule and pilotage arrangement",
        "Fishing vessel's actual mechanical failure (fouled propeller)"
      ]
    },
    "scenario_id": "MO_Biased_3",
    "domain_id": "MO",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Automatic allocation: each bias assigned to the single distinct decision point offering the best mechanism fit and narrative realism (Confirmation Bias -> solo initial classification at DP1; Groupthink -> multi-person handover discussion at DP2; Framing Bias -> reroute trade-off evaluation at DP3), with no bias sharing a decision point and DP4 left intentionally neutral.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Channel geometry and tidal window",
      "Weather and visibility conditions",
      "Cast of stakeholders (operator, supervisor, second operator, pilot, fishing vessel master)",
      "Sequence and number of decision points (4)",
      "Outcome facts (fouled propeller, minor tanker delay, no collision)"
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
