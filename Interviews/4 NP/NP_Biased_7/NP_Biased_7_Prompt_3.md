You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations learning file, not a disciplinary review — anything you share is for process improvement. Can you state your role and how long you've been on this unit?

Participant: Sure. I'm a process control operator on the catalytic reforming unit, been on this board for about six years, refinery for eleven. I run the DCS console during my shift — feed rates, heater duty, reactor temps, that kind of thing.

Interviewer: Good. Let's start broad — walk me through the incident from the beginning.

Participant: It started right at shift handover, early morning. I'd just sat down at the console when the high-temperature alarm came up on the feed heater outlet. Annunciator panel lit up red, audible tone too. Honestly, my first thought was "here we go again" — that specific alarm point has been a headache for a month. Log showed it, I want to say, eleven times in the past few weeks, and every single one turned out to be instrument drift on that thermocouple. So I acknowledged it, silenced the tone, and kept going with handover.

Interviewer: Did you check anything else at that point?

Participant: Not right away, no. I was focused on the panel itself — it's the loudest thing in the room when it goes off. There was actually a pressure-differential trend creeping up on one of the other screens, but it's a quieter kind of alarm, just a slow line drifting upward, no flashing, nothing urgent-looking. I didn't pull that screen up until later in the shift.

Interviewer: Okay, let's keep going chronologically. What happened during the handover conversation itself?

Participant: Night operator gave me the rundown — said the unit had been "stable, unremarkable" for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value. There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but that felt like old news at that point since the recent hours looked clean.

Interviewer: And then?

Participant: Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run.

Interviewer: What happened after the increase?

Participant: Outlet temperature climbed further than I expected. Then the field operator called in from a walkdown and mentioned some heat shimmer near the firebox — visually noticeable, he said, not normal. That's when it started feeling like more than a nuisance alarm.

Interviewer: Let's go back and unpack that first decision — acknowledging the alarm as nuisance. What information did you actually have in front of you at that moment?

Participant: The alarm itself, the log history showing repeat false trips, and that pressure trend I mentioned, which I hadn't really looked at yet.

Interviewer: What alternatives did you consider?

Participant: I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality.

Interviewer: How confident were you in that read?

Participant: Pretty confident, honestly. Maybe overconfident looking back. Eleven-for-eleven is a strong pattern in your head.

Interviewer: Moving to the feed increase decision — what alternatives were on the table?

Participant: I could've delayed the increase and gone back through the multi-day trend log, or looped in the process engineer before touching setpoints. Neither felt necessary given how clean the last few hours looked.

Interviewer: When you ran the sequence, were you consciously deciding it was the right call, or was it more automatic?

Participant: If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump.

Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind?

Participant: The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template. At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing.

Interviewer: Did the current data support either of those comparisons specifically?

Participant: Looking back, not entirely. The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach. And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.

Interviewer: What alternatives existed at that point?

Participant: I could've treated it as a new case entirely and pulled fresh heater-specific data before picking a diagnostic path, or requested an independent instrument check to test both of those past events against current readings. I did neither immediately.

Interviewer: Let's talk about the final decision, with the regeneration window closing in.

Participant: Under ninety minutes left. Temps and pressure still climbing but not at trip setpoints yet. I had the standard checklist for heater excursions, and I could've paused everything to escalate fully to the process engineer, but that's a twenty-to-thirty-minute conversation minimum, and the clock was working against us.

Interviewer: How did you decide?

Participant: I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast.

Interviewer: What was the outcome?

Participant: It did stabilize the immediate trend, which was the priority. Root cause wasn't fully addressed though — a later review flagged another corrective step on that same checklist that probably would've hit the underlying issue better. Wasn't wrong exactly, just not the most complete answer.

Interviewer: If the alarm's history had been different — say, no prior nuisance trips at all — would you have handled that first moment the same way?

Participant: No, honestly no. If that alarm had been clean before, I'd have jumped on the pressure trend immediately instead of treating it as background noise.

Interviewer: What single piece of information, if you'd had it earlier, would have changed the most for you?

Participant: Probably the pressure-differential trend, pulled up right alongside the alarm at the very start. That would've reframed the whole thing much sooner instead of it building quietly in the background.

Interviewer: And if you'd had more time before the regeneration window closed?

Participant: I'd have gone through more of the checklist options side by side, maybe gotten the engineer on the line even for ten minutes. It wasn't that I thought the first option was definitely best — it was available and it worked well enough given the clock.

Interviewer: Anything else stand out looking back?

Participant: Just that a lot of small, reasonable-feeling calls stacked up into something bigger than any one of them looked like at the time. Nothing felt like a wrong decision in the moment.

Interviewer: That's a good place to close. Thanks for walking through this in detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 2, "mechanism_constraint": null },
      { "bias": "Recency Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Habit Intrusion", "occurrences": 1, "mechanism_constraint": "human performance often can be captured by familiar behavioral patterns that occur so frequently in their experiences." },
      { "bias": "Salience Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Similarity Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Bounded Rationality", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Recency Bias",
      "Habit Intrusion",
      "Salience Bias",
      "Similarity Bias",
      "Bounded Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Availability Bias", "requested_occurrences": 2 },
      { "bias": "Recency Bias", "requested_occurrences": 1 },
      { "bias": "Habit Intrusion", "requested_occurrences": 1 },
      { "bias": "Salience Bias", "requested_occurrences": 1 },
      { "bias": "Similarity Bias", "requested_occurrences": 1 },
      { "bias": "Bounded Rationality", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "av_01", "bias": "Availability Bias" },
      { "instance_id": "av_02", "bias": "Availability Bias" },
      { "instance_id": "rec_01", "bias": "Recency Bias" },
      { "instance_id": "hab_01", "bias": "Habit Intrusion" },
      { "instance_id": "sal_01", "bias": "Salience Bias" },
      { "instance_id": "sim_01", "bias": "Similarity Bias" },
      { "instance_id": "br_01", "bias": "Bounded Rationality" }
    ],
    "intended_decision_points": [
      { "instance_id": "av_01", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "sal_01", "bias": "Salience Bias", "decision_point": 1 },
      { "instance_id": "rec_01", "bias": "Recency Bias", "decision_point": 2 },
      { "instance_id": "hab_01", "bias": "Habit Intrusion", "decision_point": 2 },
      { "instance_id": "sim_01", "bias": "Similarity Bias", "decision_point": 3 },
      { "instance_id": "av_02", "bias": "Availability Bias", "decision_point": 3 },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Probability of alarm being false judged via ease of recalling frequent past nuisance-alarm occurrences",
        "affected_reasoning_operation": "Probability estimation from recalled frequency",
        "evidence_source": "Alarm log showing 11 recent nuisance alarms",
        "distinctiveness_requirement": "Must be based on frequency-of-recall reasoning, distinct from av_02's vividness-of-recall reasoning"
      },
      {
        "instance_id": "sal_01",
        "bias": "Salience Bias",
        "mechanism": "Visually/audibly prominent alarm draws attention away from a less prominent but relevant pressure-differential trend",
        "affected_reasoning_operation": "Attention allocation across simultaneous evidence sources",
        "evidence_source": "Annunciator panel alarm vs. adjacent trend screen",
        "distinctiveness_requirement": "Must involve competing simultaneous evidence sources at the same decision point as av_01 but a different reasoning operation (attention allocation, not frequency-based probability judgment)"
      },
      {
        "instance_id": "rec_01",
        "bias": "Recency Bias",
        "mechanism": "Overweighting the most recent handover report of stability over older documented drift trend",
        "affected_reasoning_operation": "Weighting of sequential evidence in current-state judgment",
        "evidence_source": "Night-shift handover report vs. multi-day log drift entries",
        "distinctiveness_requirement": "Must center on temporal recency of information, not frequency or vividness"
      },
      {
        "instance_id": "hab_01",
        "bias": "Habit Intrusion",
        "mechanism": "Automatic execution of a frequently-practiced feed-increase sequence without adapting to abnormal precursor conditions",
        "affected_reasoning_operation": "Execution of a well-rehearsed action sequence under conditions requiring deviation",
        "evidence_source": "Standard operating sequence performed routinely",
        "distinctiveness_requirement": "Must manifest as an automatic behavioral pattern/slip, not a deliberate judgment error, per mechanism_constraint"
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "mechanism": "Diagnostic template from a superficially similar past compressor surge event applied despite a missing distinguishing signal",
        "affected_reasoning_operation": "Pattern-matching for diagnostic categorization",
        "evidence_source": "Memory of prior surge event vs. absence of vibration signature",
        "distinctiveness_requirement": "Must involve template transfer based on surface resemblance, distinct from av_02's likelihood judgment based on memorability"
      },
      {
        "instance_id": "av_02",
        "bias": "Availability Bias",
        "mechanism": "Likelihood of rare tube-rupture cause overestimated due to vividness/memorability of a widely discussed past incident",
        "affected_reasoning_operation": "Likelihood judgment driven by vividness of recall",
        "evidence_source": "Recollection of a two-year-old widely discussed incident",
        "distinctiveness_requirement": "Must be based on vividness-of-recall reasoning, distinct from av_01's frequency-of-recall reasoning, and occur at a different decision point"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Satisficing selection of the first workable checklist action under time and cognitive load constraints rather than exhaustive alternative evaluation",
        "affected_reasoning_operation": "Option generation and selection under constrained resources",
        "evidence_source": "Standard corrective-action checklist under closing time window",
        "distinctiveness_requirement": "Must reflect resource-constrained satisficing, not mere haste or a justified quick decision without evidence of skipped alternatives"
      }
    ],
    "intended_strength": [
      { "instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "sal_01", "bias": "Salience Bias", "strength": "subtle" },
      { "instance_id": "rec_01", "bias": "Recency Bias", "strength": "subtle" },
      { "instance_id": "hab_01", "bias": "Habit Intrusion", "strength": "moderate" },
      { "instance_id": "sim_01", "bias": "Similarity Bias", "strength": "subtle" },
      { "instance_id": "av_02", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_7",
    "domain_id": "NP",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across the 4 decision points by mechanism fit and narrative realism: decision point 1 hosts av_01 and sal_01 (distinct evidence sources: alarm-frequency log vs. competing trend screen); decision point 2 hosts rec_01 and hab_01 (distinct reasoning operations: temporal weighting vs. automatic action execution); decision point 3 hosts sim_01 and av_02 (distinct reasoning operations: pattern-matching template transfer vs. vividness-driven likelihood judgment, satisfying the same-bias distinctiveness rule for av_01/av_02 by using different evidence sources and different decision points); decision point 4 hosts br_01 alone under peak time pressure. No decision point exceeds two occurrences of any single bias.",
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
