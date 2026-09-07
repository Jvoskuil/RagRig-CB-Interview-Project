You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. Just to confirm, this is a routine debrief about a watchkeeping incident during your last strait transit — nothing punitive, and it's fine to speak candidly about how you worked through it. Can you tell me your role and roughly how long you've been standing bridge watches?

Participant: Sure. I'm second officer, been sailing as OOW for about four years now, mostly on container ships this size. That night I had the 0000 to 0400 watch on our own, with one AB as lookout. We were transiting the strait, which is always busy — crossing traffic, fishing boats, the usual squally weather this time of year.

Interviewer: Can you walk me through what happened that night, from the start of the watch?

Participant: When I took over, ARPA already had five targets acquired, nothing alarming — CPAs all comfortable. VHF chatter mentioned fishing activity ahead, and the forecast had squalls coming through, visibility dropping under a mile at times. Passage plan had us holding course into the next TSS leg, so early on it was just normal monitoring — checking the plot, cross-referencing with a visual sweep every few minutes since I know some of these wooden boats don't paint well on radar. That's actually how we caught the first one — the lookout spotted a small boat visually at about three miles before ARPA ever picked it up. Its light was dim, flickering, hard to get a steady bearing on at first.

Interviewer: What did you do once that boat was sighted?

Participant: We kept watching it. It was converging, but slowly, and ARPA still wasn't holding a firm track — weak return, in and out. I logged it mentally as one to watch rather than something urgent.

Interviewer: Let's go through the timeline a bit more before we get into specifics. After that first sighting, what came next?

Participant: The boat kept closing, down to about two miles. Around the same time we hit a squall band — visibility dropped, and radar showed a loose cluster of three or four more small contacts near the next waypoint. That waypoint rang a bell because there'd been a bulletin from the office a couple weeks back about a near-miss with a fishing cluster right around there, in fog, very similar setup. On top of that, a bulk carrier showed up on the starboard bow, CPA tightening. So for a while I had three things going at once. Eventually the bulk carrier needed a real course adjustment, and the fishing cluster passed wider than I expected. Nothing hit, watch ended, I briefed the master and handed over.

Interviewer: Let's go back to that first boat at three miles. What alternatives did you weigh?

Participant: Honestly it was between letting the ARPA scan handle prioritization since nothing was flagged, or doing extra manual sweeps myself. I went with splitting attention — mostly trusting the system's target list but throwing in visual checks specifically because I've been burned before by small wooden hulls not showing up well. That's standard practice for me in these waters.

Interviewer: And when the boat closed to two miles, still without ARPA elevating it — what happened at that point?

Participant: That one I keep turning over. The lookout said the boat seemed to be zigzagging, not settling into a track you could plot cleanly, which usually would make me nervous. But ARPA's overall ranking still had nothing above the alarm threshold — none of the five original targets or this one had crossed into the alert zone. Two VHF calls to it got no answer. I decided to keep monitoring rather than take early avoiding action, mainly because the system wasn't telling me anything was critical yet and I didn't want to make an unnecessary alteration inside the TSS lane over a contact the system itself hadn't escalated.

Interviewer: What would have changed that decision for you?

Participant: If the ARPA alarm had actually tripped on it, I'd have gone straight to manual plotting and probably altered early. As it was, the numbers on the display weren't backing up what the lookout was describing, so I leaned on the display.

Interviewer: How much time pressure did you feel at that point?

Participant: Not extreme, maybe ten, fifteen minutes before it would've mattered. Enough room to keep watching, is how it felt.

Interviewer: Let's move to the squall and the cluster near the waypoint. What drove your read of the danger there?

Participant: That one hit me fast. Visibility dropped, this loose cluster showed up right at the spot from the bulletin, and my first thought honestly was "this is the same setup as that near-miss." That report had been pretty vivid — fog, fishing boats, a ship that barely missed hitting one. So I started orienting my planning toward the cluster, working out an evasive course for it, getting the lookout focused that direction.

Interviewer: How did that compare with how you handled the bulk carrier at the same time?

Participant: The bulk carrier was actually the one with the tightening CPA on the numbers — inside a mile and closing. I noticed it, but for a bit my attention was more on the cluster because that scenario felt like the one about to go wrong. It wasn't until a little later that I really focused back on the bulk carrier's plot and realized that was the one needing the firmer action.

Interviewer: What was your sense of the cluster's actual plotted risk at the time, separate from the bulletin?

Participant: Looking back, the spacing and drift on the cluster weren't actually showing a fast closing rate yet. It was more that the situation reminded me strongly of that report.

Interviewer: If there'd been no bulletin about a similar incident, do you think you'd have split your attention differently?

Participant: Probably, yeah. Without that in my head, I think the bulk carrier's numbers would've grabbed me first, since objectively that was the tighter CPA.

Interviewer: Last decision point — after both situations resolved, you briefed the master. How did you decide what to recommend?

Participant: Both contacts passed clear, no drama, so I could've just logged it as routine. But given how much fishing activity we'd seen, and one more area coming up with reported fishing boats, I recommended posting an extra lookout for the rest of the transit. Felt like the sensible call based on what we'd actually observed that watch, not tied to any one incident.

Interviewer: Had you seen a comparable multi-contact situation before this?

Participant: A few times, though usually not three things converging together like that. Normally it's one contact at a time.

Interviewer: Looking back, what are you most uncertain about?

Participant: Whether I gave the first boat too much benefit of the doubt because the system wasn't flagging it. And whether I'd have caught the bulk carrier sooner if that bulletin hadn't been sitting in the back of my mind.

Interviewer: If you faced this same combination again, what would you do differently?

Participant: I'd probably force myself to independently plot any contact the lookout flags as behaving oddly, regardless of what the ranking shows. And I'd try to rank contacts by their actual numbers first before letting any one of them feel more urgent just because it resembles something I'd heard about.

Interviewer: That's helpful, thank you. I think that covers what I needed.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Automation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as deference to ARPA's aggregate risk ranking over a conflicting independent lookout report, at Decision Point 2 only."
      },
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as risk estimation anchored to a vividly recalled prior incident rather than current plotted data, at Decision Point 3 only."
      }
    ],
    "target_bias_names": ["Automation Bias", "Availability Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Automation Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "ab_01", "bias": "Automation Bias"},
      {"instance_id": "av_01", "bias": "Availability Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "ab_01", "bias": "Automation Bias", "decision_point": 2},
      {"instance_id": "av_01", "bias": "Availability Bias", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "mechanism": "Deference to ARPA's aggregate target-ranking output over a conflicting independent visual/lookout signal, delaying escalation to manual plotting or avoidance action.",
        "affected_reasoning_operation": "Risk prioritization / escalation decision",
        "evidence_source": "ARPA target list and alarm threshold vs. lookout's visual report of erratic small-craft movement",
        "distinctiveness_requirement": "Must be textually distinct from av_01 by involving system-output deference rather than recalled-incident salience, and must occur only at Decision Point 2."
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Risk probability estimate for the fishing cluster driven by ease of recall and vividness of a recent bulletin incident rather than current plotted spacing/closing-rate data, causing temporary under-attention to the bulk carrier's tightening CPA.",
        "affected_reasoning_operation": "Probability estimation and attention allocation across concurrent contacts",
        "evidence_source": "Recalled bulletin narrative vs. current radar plot of fishing cluster and bulk carrier CPA/TCPA",
        "distinctiveness_requirement": "Must be textually distinct from ab_01 by involving recalled-incident salience rather than system-output deference, and must occur only at Decision Point 3."
      }
    ],
    "intended_strength": [
      {"instance_id": "ab_01", "bias": "Automation Bias", "strength": "moderate"},
      {"instance_id": "av_01", "bias": "Availability Bias", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence/vividness of the recent safety-bulletin near-miss narrative (autoselected; not activated under the biased condition)",
      "original_state": "Bulletin exists and is vivid/recently discussed",
      "changed_state": "not_applicable_condition_is_biased",
      "variables_to_hold_constant": [
        "Vessel type and passage route",
        "Weather sequence",
        "Contact kinematics",
        "Watch composition",
        "Decision count and structure"
      ]
    },
    "scenario_id": "MO_Biased_2",
    "domain_id": "MO",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread one-per-bias across two distinct decision points (2 and 3), chosen for mechanism fit: Automation Bias tied to system-output deference during active target tracking, Availability Bias tied to recalled-incident salience during a spatially/thematically matching hazard (fishing cluster near the bulletin's waypoint). Decision Points 1 and 4 left free of intentional bias instances to preserve narrative realism and avoid over-saturation.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vessel type, route, and TSS constraints",
      "Weather/squall sequence",
      "Number and identity of contacts (fishing boat, fishing cluster, bulk carrier)",
      "Watch composition (single OOW plus lookout, Master on standby)",
      "Four-decision-point structure and probe set"
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
