You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. As we discussed, this is a debrief to understand your reasoning during the Stope 14-East incident, not an audit of the outcome. Everything you share helps us understand how decisions get made in the field. You're comfortable proceeding?

Participant: Yeah, that's fine. I've done these debriefs before after other events. Happy to walk through it.

Interviewer: Great. Can you first tell me a bit about your role and what your objective was that shift?

Participant: I'm the Health and Safety Officer for the site, dayshift. My main job that day was routine — checks, permits, and keeping an eye on the ground conditions in the active stopes, including 14-East, which was mid-cycle in a longhole stope. We were also under a bit of pressure to hit weekly tonnage, so there was always that background tension between keeping things moving and not cutting corners.

Interviewer: Walk me through what happened when you first got word of the noise.

Participant: Around 06:40 one of the miners came up on radio saying he'd heard some cracking, almost like popping, in the back of 14-East. Intermittent, not constant. No alarm had gone off on the microseismic array at that point. Normally that would make me lean toward "let's just check it," but honestly, my mind went straight to what happened at our sister operation two months earlier — that rockburst that made the trade press and had everyone in the region talking. It wasn't identical conditions, but it was the same ore body region, and that event was still very much front of mind for the whole crew. So even without an alarm, I treated that report as something that could be heading toward a similar event, more than I think the instrument data alone would have justified.

Interviewer: What alternatives did you weigh at that point?

Participant: There were really three options — full evacuation and stop work pending a geotech look, allow work to continue with tighter monitoring and a reviewed escape route, or just get the instrument tech to check readings first without restricting anyone. I went with the middle option: enhanced monitoring, limited access, no full evacuation. Partly because the instruments weren't flagging anything, but I'll admit the sister-mine incident weighed heavily on how urgent it felt to me in the moment.

Interviewer: Let's move to later that morning — the extensometer readings.

Participant: Right, so the 05:00 baseline was 0.2mm, which is our normal quiet reading. At 09:40 the tech radioed that it had moved to 0.6mm. That's three times the baseline in about three hours. I looked at it and thought, well, compared to this morning it's still a small number, still sub-millimeter, nothing dramatic. I didn't go back and check it against the rate-of-change table in the GCMP, which is actually the correct way to assess it — that plan cares about how fast it's moving, not just where it sits relative to where it started. In hindsight I was comparing it to the wrong reference.

Interviewer: What made the baseline feel like the right comparison at the time?

Participant: It's just naturally what you have in front of you — you saw it at 0.2 that morning, now it's 0.6, and 0.6 still sounds low in absolute terms. Ventilation had nothing unusual either, no gas, no temperature anomaly, so there was nothing else pulling my attention toward the rate-of-change side of things.

Interviewer: Did anything else factor into that call?

Participant: The mine manager was also asking for a production ETA, so there was some pull to land on "we're fine" rather than dig deeper into the trend math right then.

Interviewer: Let's talk about the conversation with your shift supervisor.

Participant: That was maybe an hour later. He's got twenty-two years underground, most of it at this site. He mentioned he'd heard similar popping back in 2009, and it hadn't come to anything. He was pretty confident it was "nothing." Around that same time the microseismic count for the shift had actually climbed to six events an hour, which is right at — actually just over — the flag threshold in our plan. I didn't push hard on whether the 2009 case actually matched today's rock type, blast pattern, or depth. His track record is strong, so his read carried a lot of weight for me in that moment, maybe more than it should have on its own.

Interviewer: You also looked at a crack in the same panel. Can you describe that?

Participant: Yes — there was a hairline crack, about a millimeter wide, that had been photographed and logged the week before as insignificant. When I looked at today's crack, I compared it side-by-side with that old photo, and it looked about the same width to me, so I read it as "consistent with what we already know is fine." What I didn't do at that point was connect it back to the microseismic number that had just ticked over the threshold — I was judging the crack against the old photo rather than against the newer seismic data.

Interviewer: What alternatives did you consider before allowing continued access?

Participant: Follow the seismic threshold strictly and pull back until the engineer signed off, split the difference and reduce crew size, or trust the supervisor's read and keep going with limited crew. I went with limited access, mostly on the supervisor's confidence and my own read of that crack photo.

Interviewer: What happened next?

Participant: The engineer eventually called back wanting the full event log, and around then someone noticed a second, wider crack near the first one. Then at 13:15 we had a minor spall — no injuries, some equipment damage. Shift change had happened about ninety minutes before that.

Interviewer: When you wrote up the incident report, how did you decide what caused it?

Participant: Looking at everything together — the overnight temperature drop, the shift change happening not long before, and the blasting in the panel next door the prior week — it came together into a pretty clean story: cooling stresses plus the handover timing plus the residual vibration from that blast. It read as a coherent explanation, so that's what I put forward as the primary account, even though the engineer's later note said several factors were plausible and none could really be confirmed as the dominant cause.

Interviewer: And on responsibility — how did you frame that?

Participant: I focused mainly on the miner who first heard the sounds and didn't escalate again after the initial 06:40 report — I felt if he'd flagged it again once the popping continued, we might have caught it sooner. I did note the missing engineer sign-off after the six-events flag, but that came across more as a process footnote than as a central cause in the report.

Interviewer: If the sister-mine rockburst had never happened, do you think your first call would have gone differently?

Participant: Possibly. I think without that fresh in everyone's mind, I might have waited for the instrument tech's check before doing anything, rather than jumping to enhanced monitoring right away.

Interviewer: If the rate-of-change threshold had displayed automatically next to the raw reading, would the second decision have changed?

Participant: Probably, yeah. If it had flagged red rather than just showing a number, I don't think I'd have leaned on the morning comparison the way I did.

Interviewer: What would you tell a newer HSO to watch for in a similar shift?

Participant: To always check the plan's actual thresholds rather than trusting a gut comparison to whatever reading you saw earlier, and to weigh a senior person's read alongside the data, not instead of it.

Interviewer: Last one — how confident are you now that the causes you listed in the report are the real ones?

Participant: Honestly, less than I was when I wrote it. It felt tidy at the time, but there were a few threads I didn't fully chase down.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to recall of the specific sister-mine rockburst, not a generic caution statement." },
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
      { "instance_id": "av_01", "bias": "Availability Bias" },
      { "instance_id": "exp_01", "bias": "Experience Bias" },
      { "instance_id": "anc_01", "bias": "Anchoring Bias" },
      { "instance_id": "anc_02", "bias": "Anchoring Bias" },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy" },
      { "instance_id": "attr_01", "bias": "Attribution Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "av_01", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "anc_01", "bias": "Anchoring Bias", "decision_point": 2 },
      { "instance_id": "exp_01", "bias": "Experience Bias", "decision_point": 3 },
      { "instance_id": "anc_02", "bias": "Anchoring Bias", "decision_point": 3 },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy", "decision_point": 4 },
      { "instance_id": "attr_01", "bias": "Attribution Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Vivid recall of the recent sister-mine rockburst inflates the perceived likelihood of the current ambiguous noise report.",
        "affected_reasoning_operation": "Risk-likelihood estimation from a verbal cue",
        "evidence_source": "Memory of a widely publicized recent industry incident",
        "distinctiveness_requirement": "Occurs only at decision point 1, tied specifically to the sister-mine memory, not repeated later."
      },
      {
        "instance_id": "anc_01",
        "bias": "Anchoring Bias",
        "mechanism": "Morning baseline extensometer reading anchors judgment of the later reading as 'still normal' instead of applying the rate-of-change rule.",
        "affected_reasoning_operation": "Comparative evaluation of updated instrument data against fixed initial reference",
        "evidence_source": "Extensometer displacement readings (05:00 baseline vs. 09:40 update)",
        "distinctiveness_requirement": "Uses instrument telemetry evidence at decision point 2; distinct from anc_02's photographic evidence at decision point 3."
      },
      {
        "instance_id": "exp_01",
        "bias": "Experience Bias",
        "mechanism": "Supervisor's tenure is treated as sufficient validation of a benign read, without checking situational similarity to today's conditions.",
        "affected_reasoning_operation": "Credibility weighting of informal expert opinion vs. threshold data",
        "evidence_source": "Supervisor's verbal recollection of a 2009 event",
        "distinctiveness_requirement": "Occurs only at decision point 3, distinct reasoning operation (credibility weighting) from anc_02's evidence comparison at the same decision point."
      },
      {
        "instance_id": "anc_02",
        "bias": "Anchoring Bias",
        "mechanism": "Prior week's photographed hairline crack anchors judgment of today's crack severity, displacing attention from the newly reached microseismic threshold.",
        "affected_reasoning_operation": "Visual/photographic comparison against a prior fixed reference",
        "evidence_source": "Crack-width photographs (last week vs. today)",
        "distinctiveness_requirement": "Uses photographic evidence at decision point 3; distinct evidence type and moment from anc_01's instrument-baseline anchor at decision point 2."
      },
      {
        "instance_id": "narr_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Multiple loosely-related factors are woven into a single tidy causal chain in the post-event report, overstating certainty of the causal linkage.",
        "affected_reasoning_operation": "Post-hoc causal reconstruction for incident reporting",
        "evidence_source": "Temperature log, shift-change timing, prior blasting record",
        "distinctiveness_requirement": "Occurs only in the decision point 4 incident narrative, not in earlier probes or hypotheticals."
      },
      {
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "mechanism": "Escalation responsibility is assigned mainly to the on-shift miner's reporting delay rather than to the missing systemic GCMP sign-off step.",
        "affected_reasoning_operation": "Causal attribution of responsibility between individual and systemic factors",
        "evidence_source": "Miner reporting timeline vs. GCMP sign-off requirement",
        "distinctiveness_requirement": "Occurs only in the decision point 4 responsibility assessment, distinct reasoning operation from narr_01's causal-chain construction at the same decision point."
      }
    ],
    "intended_strength": [
      { "instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "exp_01", "bias": "Experience Bias", "strength": "subtle" },
      { "instance_id": "anc_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "anc_02", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "narr_01", "bias": "Narrative Fallacy", "strength": "subtle" },
      { "instance_id": "attr_01", "bias": "Attribution Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_6",
    "domain_id": "MU",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across the 4 decision points by mechanism fit and narrative realism: Availability Bias placed at the initial ambiguous-report decision (DP1) where recall of a recent vivid event is most plausible; Anchoring Bias split across DP2 (instrument baseline) and DP3 (photographic reference) using two distinct evidence sources to satisfy the same-decision-point distinctiveness rule; Experience Bias placed at DP3 alongside but reasoning-operation-distinct from the second Anchoring instance; Narrative Fallacy and Attribution Bias both placed at DP4 (post-event review) but targeting different reasoning operations (causal-chain construction vs. responsibility attribution). No bias exceeds two occurrences at a single decision point.",
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
