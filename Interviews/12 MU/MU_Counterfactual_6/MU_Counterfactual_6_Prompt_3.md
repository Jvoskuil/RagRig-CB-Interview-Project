You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for sitting down with me. As before, this is about understanding your reasoning process during the Stope 14-East event, not evaluating the outcome. Alright to continue?

Participant: Yes, fine.

Interviewer: Can you set the scene — your role, and what you were working toward that shift?

Participant: I'm the Health and Safety Officer, dayshift. My job that day was mostly routine oversight of active headings, including Stope 14-East, a longhole stope. One thing that was a bit different from a typical week was that our tonnage target had just been reset to a weekly figure rather than a shift figure, so there wasn't the usual same-day scramble hanging over us. That gave us a bit more room to breathe on scheduling, in theory.

Interviewer: Walk me through what happened when you first heard about the noise.

Participant: Around 06:40 a miner radioed in saying he'd heard intermittent cracking, kind of a popping sound, in the back of 14-East. No alarm had tripped on the microseismic array at that point. Even with the weekly target giving us some slack, my first thought went straight to the rockburst at our sister operation two months back — that made the trade press, and it was still something everyone on site talked about. The conditions weren't identical, but same ore body region, and it was vivid enough that I treated the report as more likely to be heading toward something serious than the instruments alone would have suggested.

Interviewer: What alternatives did you weigh at that point?

Participant: Full evacuation and stop-work pending geotech, enhanced monitoring with limited access, or just getting the instrument tech to check readings first. I went with enhanced monitoring and limited access. The instruments weren't flagging anything, but that sister-mine memory carried a lot of weight for me regardless of what the schedule looked like that day.

Interviewer: Let's move to the extensometer readings later that morning.

Participant: The 05:00 baseline was 0.2mm, our normal quiet reading. By 09:40 it had moved to 0.6mm — three times the baseline in about three hours. I looked at that and thought, well, compared to this morning, it's still a small number. I didn't go back to the GCMP's rate-of-change table, which is actually how you're supposed to judge it — the plan cares about the speed of movement, not just where it sits against an earlier point. Looking back, I was using the wrong reference.

Interviewer: What information, if you'd had it in front of you right then, would have changed that call?

Participant: If the rate-of-change figure had been sitting right next to the raw number, I think I'd have caught it. As it was, all I had was two numbers from two different times, and comparing them felt natural.

Interviewer: Did the weekly target play into that decision at all?

Participant: Honestly, not much. There wasn't pressure to rush a call because production wasn't riding on that hour. It was more just how I read the two numbers side by side.

Interviewer: Tell me about the conversation with your shift supervisor.

Participant: About an hour later. He's got twenty-two years underground, most of it here. He mentioned hearing similar popping back in 2009 that came to nothing, and he was confident this was the same kind of thing. Around then the microseismic count for the shift had actually climbed to six events an hour, just over our flag threshold of five. I didn't really push on whether the 2009 case matched today's rock type or blast pattern. His track record carried a lot of weight for me in that moment.

Interviewer: You also looked at a crack in that panel — can you describe that?

Participant: There was a hairline crack, about a millimeter, photographed and logged the week before as insignificant. Today's crack looked about the same width to me, so I read it as consistent with what we already knew was fine. What I didn't do was connect it to the seismic count that had just crossed the threshold — I was judging the crack against the old photo instead of against the newer number.

Interviewer: What alternatives did you consider before allowing continued access?

Participant: Follow the seismic threshold strictly and hold the stope for engineer sign-off, reduce crew size as a middle path, or trust the supervisor's read and continue with limited crew. I went with limited access, mostly on his confidence and my own read of the crack photo.

Interviewer: Given that production wasn't due until end of week, did that change how you approached this call?

Participant: Not really — there wasn't an obvious reason to hurry one way or the other. It felt more like I was weighing the supervisor's experience and that photo comparison on their own terms.

Interviewer: What happened after that?

Participant: The engineer eventually called back wanting the full event log, and around the same time someone noticed a second, wider crack near the first. Then at 13:15 we had a minor spall — no injuries, some equipment damage. Shift change had happened about ninety minutes earlier.

Interviewer: When you wrote the incident report, how did you land on the causes?

Participant: Putting it together — the overnight temperature drop, the shift change not long before, and the blasting in the next panel the previous week — it read as a pretty clean explanation: cooling stress plus the handover timing plus residual vibration from that blast. That's what I put forward as the account, even though the engineer's later note said several factors were plausible and none could be confirmed as dominant.

Interviewer: And how did you frame responsibility?

Participant: I focused mainly on the miner who first reported the sounds and didn't flag it again once the popping continued — I felt if he'd called it in a second time, we might have caught it sooner. I did mention the missing engineer sign-off after the six-events flag, but it came across more as a process note than a central cause.

Interviewer: If the sister-mine rockburst had never happened, would your first call have gone differently?

Participant: Probably. Without that fresh in mind, I think I'd have waited on the instrument tech's check before doing anything.

Interviewer: If a less experienced supervisor had said the same thing about 2009, would you have weighted it the same way?

Participant: No, I don't think so. His years underground were a big part of why I trusted the read.

Interviewer: Last one — how confident are you now that the causes in the report were the real ones?

Participant: Less than when I wrote it. It felt like a complete picture at the time, but there were threads I didn't fully chase down.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to recall of the specific sister-mine rockburst, not a generic caution statement, and must be independent of the deadline variable." },
      { "bias": "Experience Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to overweighting supervisor tenure without verifying situational similarity." },
      { "bias": "Anchoring Bias", "occurrences": 2, "mechanism_constraint": "Each instance must reference a distinct evidence source (instrument baseline reading vs. crack photograph) at a distinct decision point." },
      { "bias": "Narrative Fallacy", "occurrences": 1, "mechanism_constraint": "Must occur only in the post-event causal explanation, not in earlier probes." },
      { "bias": "Attribution Bias", "occurrences": 1, "mechanism_constraint": "Must contrast individual worker blame against an identifiable systemic/process factor." }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Experience Bias",
      "Anchoring Bias",
      "Narrative Fallacy",
      "Attribution Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Availability Bias", "requested_occurrences": 1 },
      { "bias": "Experience Bias", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 2 },
      { "bias": "Narrative Fallacy", "requested_occurrences": 1 },
      { "bias": "Attribution Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cf_av_01", "bias": "Availability Bias" },
      { "instance_id": "cf_exp_01", "bias": "Experience Bias" },
      { "instance_id": "cf_anc_01", "bias": "Anchoring Bias" },
      { "instance_id": "cf_anc_02", "bias": "Anchoring Bias" },
      { "instance_id": "cf_narr_01", "bias": "Narrative Fallacy" },
      { "instance_id": "cf_attr_01", "bias": "Attribution Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cf_av_01", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "cf_anc_01", "bias": "Anchoring Bias", "decision_point": 2 },
      { "instance_id": "cf_exp_01", "bias": "Experience Bias", "decision_point": 3 },
      { "instance_id": "cf_anc_02", "bias": "Anchoring Bias", "decision_point": 3 },
      { "instance_id": "cf_narr_01", "bias": "Narrative Fallacy", "decision_point": 4 },
      { "instance_id": "cf_attr_01", "bias": "Attribution Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cf_av_01",
        "bias": "Availability Bias",
        "mechanism": "Vivid recall of the recent sister-mine rockburst inflates the perceived likelihood of the current ambiguous noise report, independent of deadline urgency.",
        "affected_reasoning_operation": "Risk-likelihood estimation from a verbal cue",
        "evidence_source": "Memory of a widely publicized recent industry incident",
        "distinctiveness_requirement": "Occurs only at decision point 1, tied specifically to the sister-mine memory, not repeated later."
      },
      {
        "instance_id": "cf_anc_01",
        "bias": "Anchoring Bias",
        "mechanism": "Morning baseline extensometer reading anchors judgment of the later reading as 'still normal' instead of applying the rate-of-change rule.",
        "affected_reasoning_operation": "Comparative evaluation of updated instrument data against fixed initial reference",
        "evidence_source": "Extensometer displacement readings (05:00 baseline vs. 09:40 update)",
        "distinctiveness_requirement": "Uses instrument telemetry evidence at decision point 2; distinct from cf_anc_02's photographic evidence at decision point 3."
      },
      {
        "instance_id": "cf_exp_01",
        "bias": "Experience Bias",
        "mechanism": "Supervisor's tenure is treated as sufficient validation of a benign read, without checking situational similarity to today's conditions.",
        "affected_reasoning_operation": "Credibility weighting of informal expert opinion vs. threshold data",
        "evidence_source": "Supervisor's verbal recollection of a 2009 event",
        "distinctiveness_requirement": "Occurs only at decision point 3, distinct reasoning operation (credibility weighting) from cf_anc_02's evidence comparison at the same decision point."
      },
      {
        "instance_id": "cf_anc_02",
        "bias": "Anchoring Bias",
        "mechanism": "Prior week's photographed hairline crack anchors judgment of today's crack severity, displacing attention from the newly reached microseismic threshold.",
        "affected_reasoning_operation": "Visual/photographic comparison against a prior fixed reference",
        "evidence_source": "Crack-width photographs (last week vs. today)",
        "distinctiveness_requirement": "Uses photographic evidence at decision point 3; distinct evidence type and moment from cf_anc_01's instrument-baseline anchor at decision point 2."
      },
      {
        "instance_id": "cf_narr_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Multiple loosely-related factors are woven into a single tidy causal chain in the post-event report, overstating certainty of the causal linkage, regardless of deadline pressure.",
        "affected_reasoning_operation": "Post-hoc causal reconstruction for incident reporting",
        "evidence_source": "Temperature log, shift-change timing, prior blasting record",
        "distinctiveness_requirement": "Occurs only in the decision point 4 incident narrative, not in earlier probes or hypotheticals."
      },
      {
        "instance_id": "cf_attr_01",
        "bias": "Attribution Bias",
        "mechanism": "Escalation responsibility is assigned mainly to the on-shift miner's reporting delay rather than to the missing systemic GCMP sign-off step.",
        "affected_reasoning_operation": "Causal attribution of responsibility between individual and systemic factors",
        "evidence_source": "Miner reporting timeline vs. GCMP sign-off requirement",
        "distinctiveness_requirement": "Occurs only in the decision point 4 responsibility assessment, distinct reasoning operation from cf_narr_01's causal-chain construction at the same decision point."
      }
    ],
    "intended_strength": [
      { "instance_id": "cf_av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "cf_exp_01", "bias": "Experience Bias", "strength": "subtle" },
      { "instance_id": "cf_anc_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cf_anc_02", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cf_narr_01", "bias": "Narrative Fallacy", "strength": "subtle" },
      { "instance_id": "cf_attr_01", "bias": "Attribution Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": "MU_Biased_6",
    "counterfactual_variable": {
      "name": "Timing/urgency of the production quota deadline",
      "original_state": "Tonnage from Stope 14-East due by end of the current dayshift (acute same-day pressure)",
      "changed_state": "Tonnage from Stope 14-East due by end of the week (relaxed schedule slack)",
      "variables_to_hold_constant": [
        "Instrument readings (extensometer baseline/update, microseismic counts)",
        "Sister-mine rockburst memory and timing",
        "Supervisor's tenure, 2009 recollection, and reassurance wording",
        "Hairline crack photograph and today's crack photos",
        "Spall event details (time, no injuries, equipment damage)",
        "Shift-change timing and prior-week blasting",
        "GCMP thresholds and the missing engineer sign-off",
        "The four decision points, their alternatives, and the six planned bias instances"
      ]
    },
    "scenario_id": "MU_Counterfactual_6",
    "domain_id": "MU",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrence allocation mirrors the paired biased scenario (MU_Biased_6) exactly in decision-point placement and mechanism, since the manifest and CTA structure are held constant under the counterfactual condition: Availability Bias at DP1 (sister-mine recall), Anchoring Bias split across DP2 (instrument baseline) and DP3 (photographic reference) using distinct evidence sources, Experience Bias at DP3 alongside but reasoning-operation-distinct from the second Anchoring instance, and Narrative Fallacy plus Attribution Bias both at DP4 but targeting different reasoning operations. The only altered element is the production-deadline causal variable, which does not itself drive any bias mechanism and is deliberately kept orthogonal to all six instances so the counterfactual isolates the deadline's causal effect on outcome/framing rather than on reasoning-pattern presence.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Instrument readings (extensometer baseline/update, microseismic counts)",
      "Sister-mine rockburst memory and timing",
      "Supervisor's tenure, 2009 recollection, and reassurance wording",
      "Hairline crack photograph and today's crack photos",
      "Spall event details (time, no injuries, equipment damage)",
      "Shift-change timing and prior-week blasting",
      "GCMP thresholds and the missing engineer sign-off",
      "The four decision points, their alternatives, and the six planned bias instances"
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
