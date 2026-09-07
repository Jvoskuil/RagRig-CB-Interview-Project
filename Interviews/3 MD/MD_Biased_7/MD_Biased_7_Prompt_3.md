You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary cognitive task analysis, not an evaluation of your conduct — I'm interested in how you actually thought through the decisions, not whether they were right. Can you tell me your role on this operation?

Participant: Sure. I was the troop commander — overall lead for the assault force, responsible for the go/no-go call, movement decisions, and the breach plan. I had a partnered host-nation commando element attached for this one too.

Interviewer: Good. Let's start broad — walk me through the mission from tasking to your final report.

Participant: We got tasked against a facilitator, code name Zaytun, believed to be co-located with a weapons cache in a compound out in a valley we'd worked before. We had about six hours from tasking to launch, which is tight but not unusual. SIGINT had a phone associated with his network pinging inside the compound two nights before. We planned a foot infil from an offset LZ, about forty-five minutes in, breach, clear, exploit, exfil by helicopter. We'd hit that valley twice before with good results — both times we got confirmed HVTs with almost no collateral issues, so there was a comfort level with the terrain and the pattern.

Interviewer: What information did you have going into the launch decision specifically?

Participant: The SIGINT hit, which the analyst flagged as moderate confidence, not high — he was clear about that. We also had a note from our host-nation liaison that the compound was a known family residence, kids present during the day. That came in maybe two hours before the brief. And obviously the track record from the last two ops in that valley.

Interviewer: How did you weigh the liaison's report against the SIGINT?

Participant: Honestly, it didn't move the needle much for me. The SIGINT was the thing that put the target in that building, and the two prior ops had built a lot of confidence that when we get a hit like that in that valley, it pans out. The family-residence note felt like background texture rather than something that should change the plan — it wasn't tied to a specific threat, more of a general caution. I didn't feel like I needed a specific reason to set it aside, it just didn't carry the same weight as the geolocation.

Interviewer: What other options did you consider at that point?

Participant: Really it came down to launch or delay twenty-four hours for another collection pass. Delaying risked losing the target if he moved. There was technically a lower-signature surveillance-only option on paper, but that's not really how we use this troop — we're not built for that mission set, so it didn't get serious airtime in the room.

Interviewer: Let's move to the infiltration route. What were you working with?

Participant: The route crossed a wadi that, for me personally, is loaded — we took a hard contact there about eight months earlier, sharp firefight, guys got hurt. There was a slower alternate route that avoided it. But we'd also had three straight quiet insertions through that general area over the past couple months.

Interviewer: How did those two things — the old firefight and the recent quiet crossings — factor into your choice?

Participant: Both were in my head, if I'm honest. The firefight sticks with you in a way that current reporting doesn't always match — when I pictured that wadi, I pictured tracer fire, not a calm crossing, even though nothing in the current threat picture pointed to that. At the same time, we'd had three clean runs through there recently, and there's a pull toward thinking the run continues, or conversely that we were "due." I went with the wadi route mostly on that combination rather than waiting on updated route-specific intel.

Interviewer: Did you request anything to resolve that uncertainty before deciding?

Participant: Not specifically for the route. Time was a factor — we were already tight against the assault window.

Interviewer: What happened as a result?

Participant: We crossed clean, no contact, but we came out about four minutes behind timeline, which compressed everything downstream.

Interviewer: Let's go to the breach decision. What were the options there?

Participant: Rear wall or front gate. Rear wall we'd rehearsed extensively in training — I could run that sequence in my head start to finish, exactly how the team would flow through. Front gate was less rehearsed, though our engineer actually assessed it as structurally simpler to get through. The liaison flagged movement near the front gate suggesting people were awake there.

Interviewer: What about the rear wall — was there any comparable read on activity?

Participant: Team 1, my own guys, called the rear wall clean. The host-nation commandos, separately, reported ambiguous movement near that same wall. Two different reads on the same spot.

Interviewer: How did you resolve that conflict?

Participant: I went with Team 1's call. That's the read I trusted — they're my organic element, I know how they call things, I know their standards. The commandos' report was vaguer anyway, "possible movement," nothing concrete. Between that and being able to see exactly how the rear-wall entry would go from all the rehearsals, the front gate never really competed for my attention.

Interviewer: What happened at the breach?

Participant: We went in the rear wall. Found a non-combatant right near the breach point, had to pause the whole assault element to sort that out. Wasn't dangerous, but it cost us time we didn't have a lot of.

Interviewer: Last decision point — the extraction. What was the situation?

Participant: One of my guys took a leg injury during that pause. Medic called it stable but said we needed to get him out within the window. Primary LZ was a twenty-minute movement through ground where our ISR coverage had gaps — the UAS had been intermittent all night because of weather. The casevac bird had a narrow fuel window.

Interviewer: What made you choose the primary LZ over the alternatives?

Participant: We'd used that exact exfil sequence successfully the last two times we'd operated in that valley — same LZ, same general flow. It had worked clean both times, so I had a lot of confidence going into it. There was a closer casevac point off the approved list, and we could've held for a dedicated casevac asset instead of the standard bird, but both of those added complexity or delay I didn't think we needed given how smoothly things had gone before.

Interviewer: Did the casualty or the ISR gaps change your risk calculus at all?

Participant: Not as much as maybe they should have, looking back. I was leaning heavily on "this has worked twice," and I don't think I fully re-weighted for the fact that this time we had a man down and less coverage than we'd had before.

Interviewer: What actually happened?

Participant: We made it to the primary LZ without incident, but we landed right at the edge of the bird's fuel window, so the load was rushed. It worked out, but it was tighter than it needed to be.

Interviewer: If the liaison's family-residence report had come from your own intelligence shop instead of the host-nation side, would that have changed your launch decision?

Participant: Probably would have gotten more scrutiny, yeah. I can't say for certain it flips the decision, but it would've sat differently with me.

Interviewer: If you hadn't had that earlier firefight in the wadi, do you think you'd have picked the same route?

Participant: Maybe. Without that memory pulling at me, I might have given the alternate route a fairer look on its own merits instead of it competing against a gut feeling either way.

Interviewer: Looking back, what would you tell a junior team leader about reading a sequence like this — quiet, then contested, then quiet again?

Participant: I'd say don't let a streak, in either direction, do your thinking for you, and don't assume today's team call is more solid than someone else's just because it's your own guys. Weigh the actual report, not who it came from.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Negative Rejection Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as discounting a dissenting/unfavorable liaison report at the intel-validation decision point."},
      {"bias": "Retrievability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as vivid past-event memory disproportionately shaping current route risk assessment."},
      {"bias": "Search set Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as an artificially narrowed set of considered courses of action at the launch decision."},
      {"bias": "Imaginability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as ease of mentally simulating a rehearsed breach inflating confidence in that option."},
      {"bias": "Gamblers Fallacy", "occurrences": 1, "mechanism_constraint": "Must manifest as treating a recent run of independent quiet insertions as predictive of the current crossing's odds."},
      {"bias": "Ingroup Preference bias or In-group bias", "occurrences": 1, "mechanism_constraint": "Must manifest as favoring the organic team's report over the host-nation commandos' report at the same breach point based on affiliation."},
      {"bias": "Optimism bias", "occurrences": 1, "mechanism_constraint": "Must manifest as underestimating compounded exfil risk based on past personal success with the same sequence."}
    ],
    "target_bias_names": [
      "Negative Rejection Bias",
      "Retrievability Bias",
      "Search set Bias",
      "Imaginability Bias",
      "Gamblers Fallacy",
      "Ingroup Preference bias or In-group bias",
      "Optimism bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Negative Rejection Bias", "requested_occurrences": 1},
      {"bias": "Retrievability Bias", "requested_occurrences": 1},
      {"bias": "Search set Bias", "requested_occurrences": 1},
      {"bias": "Imaginability Bias", "requested_occurrences": 1},
      {"bias": "Gamblers Fallacy", "requested_occurrences": 1},
      {"bias": "Ingroup Preference bias or In-group bias", "requested_occurrences": 1},
      {"bias": "Optimism bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "MD7_01", "bias": "Negative Rejection Bias"},
      {"instance_id": "MD7_02", "bias": "Search set Bias"},
      {"instance_id": "MD7_03", "bias": "Retrievability Bias"},
      {"instance_id": "MD7_04", "bias": "Gamblers Fallacy"},
      {"instance_id": "MD7_05", "bias": "Imaginability Bias"},
      {"instance_id": "MD7_06", "bias": "Ingroup Preference bias or In-group bias"},
      {"instance_id": "MD7_07", "bias": "Optimism bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "MD7_01", "bias": "Negative Rejection Bias", "decision_point": 1},
      {"instance_id": "MD7_02", "bias": "Search set Bias", "decision_point": 1},
      {"instance_id": "MD7_03", "bias": "Retrievability Bias", "decision_point": 2},
      {"instance_id": "MD7_04", "bias": "Gamblers Fallacy", "decision_point": 2},
      {"instance_id": "MD7_05", "bias": "Imaginability Bias", "decision_point": 3},
      {"instance_id": "MD7_06", "bias": "Ingroup Preference bias or In-group bias", "decision_point": 3},
      {"instance_id": "MD7_07", "bias": "Optimism bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MD7_01",
        "bias": "Negative Rejection Bias",
        "mechanism": "Discounting the host-nation liaison's unfavorable, dissenting report on family residence/children because it conflicts with the desired go decision.",
        "affected_reasoning_operation": "Evidence-selection / weighting of disconfirming information",
        "evidence_source": "Host-nation liaison field report",
        "distinctiveness_requirement": "Distinct from MD7_02 (option-generation narrowing) and from MD7_06 (which involves comparative source trust rather than rejection of unfavorable content)."
      },
      {
        "instance_id": "MD7_02",
        "bias": "Search set Bias",
        "mechanism": "Failing to seriously generate or consider the surveillance-only downgrade option, restricting alternatives to the habitual go/delay pair.",
        "affected_reasoning_operation": "Generation of alternative courses of action",
        "evidence_source": "Troop standard operating repertoire / mission tasking framework",
        "distinctiveness_requirement": "Distinct from MD7_01: this instance concerns the range of options generated, not the weighting of a specific piece of disconfirming evidence."
      },
      {
        "instance_id": "MD7_03",
        "bias": "Retrievability Bias",
        "mechanism": "An emotionally vivid firefight memory from eight months prior dominates route risk assessment over current, less memorable threat reporting.",
        "affected_reasoning_operation": "Recall-based risk weighting",
        "evidence_source": "Commander's personal memory of a prior firefight at the same location",
        "distinctiveness_requirement": "Distinct from MD7_04: this instance concerns vividness/salience of a single memorable event, not a sequence-based probability judgment."
      },
      {
        "instance_id": "MD7_04",
        "bias": "Gamblers Fallacy",
        "mechanism": "Treating a recent independent sequence of quiet insertions as informative about the probability of contact on the current, unrelated crossing.",
        "affected_reasoning_operation": "Sequential probability judgment",
        "evidence_source": "Record of three prior insertions in the same general area over two months",
        "distinctiveness_requirement": "Distinct from MD7_03: this instance concerns a run of outcomes treated as altering future independent odds, not the salience of one vivid event."
      },
      {
        "instance_id": "MD7_05",
        "bias": "Imaginability Bias",
        "mechanism": "Ease of mentally simulating the well-rehearsed rear-wall breach inflates its perceived success probability relative to the front gate.",
        "affected_reasoning_operation": "Success-probability estimation via mental simulation ease",
        "evidence_source": "Rehearsal history for the rear-wall breach sequence",
        "distinctiveness_requirement": "Distinct from MD7_06: this instance concerns confidence derived from rehearsal-driven visualization, not comparative trust between two reporting sources."
      },
      {
        "instance_id": "MD7_06",
        "bias": "Ingroup Preference bias or In-group bias",
        "mechanism": "At the identical rear-wall breach point, the organic team's report is trusted over the host-nation commandos' ambiguous report due to team affiliation rather than evidentiary merit.",
        "affected_reasoning_operation": "Cross-source evidence weighting",
        "evidence_source": "Team 1 (organic) 'clean' call versus host-nation commando ambiguous-movement report",
        "distinctiveness_requirement": "Distinct from MD7_05: this instance concerns differential trust across two competing reports on the same location, not visualization-driven confidence in one option."
      },
      {
        "instance_id": "MD7_07",
        "bias": "Optimism bias",
        "mechanism": "Confidence in the primary exfil route is projected forward from two prior successes without adjusting for the current casualty and ISR gap, underestimating compounded risk.",
        "affected_reasoning_operation": "Forward risk projection",
        "evidence_source": "Track record of two prior successful exfils using the same sequence",
        "distinctiveness_requirement": "Sole instance at decision point 4; distinguished from all others by occurring at the final extraction phase and concerning self-referential risk projection rather than evidence weighting."
      }
    ],
    "intended_strength": [
      {"instance_id": "MD7_01", "bias": "Negative Rejection Bias", "strength": "subtle"},
      {"instance_id": "MD7_02", "bias": "Search set Bias", "strength": "subtle"},
      {"instance_id": "MD7_03", "bias": "Retrievability Bias", "strength": "subtle"},
      {"instance_id": "MD7_04", "bias": "Gamblers Fallacy", "strength": "moderate"},
      {"instance_id": "MD7_05", "bias": "Imaginability Bias", "strength": "subtle"},
      {"instance_id": "MD7_06", "bias": "Ingroup Preference bias or In-group bias", "strength": "moderate"},
      {"instance_id": "MD7_07", "bias": "Optimism bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Biased_7",
    "domain_id": "MD",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across the 4 decision points by mechanism fit and narrative realism: DP1 (intel validation) received Negative Rejection Bias and Search set Bias since both concern pre-launch evidence/option handling; DP2 (infiltration) received Retrievability Bias and Gamblers Fallacy since both concern route-risk judgment under a stream of prior experience; DP3 (assault/breach) received Imaginability Bias and Ingroup Preference bias since both concern breach-point confidence at the same physical decision moment but via distinct mechanisms (visualization vs. source trust) and distinct evidence sources; DP4 (extraction) received the sole remaining bias, Optimism bias, fitting the forward-risk-projection nature of the exfil decision. No decision point received more than two instances, and co-located instances (DP1, DP3) were required to use distinct evidence sources and reasoning operations per the exact-occurrence rules.",
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
