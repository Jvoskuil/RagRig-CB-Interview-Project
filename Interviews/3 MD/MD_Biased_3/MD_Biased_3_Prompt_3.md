You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a cognitive task analysis study, not for any evaluation of your performance or record. You can decline to answer anything. Are you okay to proceed?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role and what your responsibilities were that night?

Participant: I was the Battle Captain on the night shift at the JOC, so I'm the watch officer responsible for the common operational picture, coordinating sensor and ISR tasking, and making the call on escalation — QRF alerts, higher headquarters notifications, that kind of thing. That night we were short an intel analyst, so the S2 shop was thinner than usual, and we only had one UAV available for the whole sector.

Interviewer: Walk me through what happened, starting from the first indication something was off.

Participant: Around 0215 a perimeter sensor near NAI-7, up on the northern boundary, logged a motion alert. Single sensor, no visual confirmation, and the weather that night — some ground fog — was already degrading sensor reliability. We didn't have any HUMINT or SIGINT corroborating it yet. Normally that's the kind of thing you'd log and keep an eye on. But I'll be honest, that specific sensor and that specific stretch of perimeter rang a bell for me. About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away.

Interviewer: What exactly about the current alert reminded you of that earlier incident?

Participant: Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way.

Interviewer: Okay. What happened next?

Participant: I had the S2 analyst start pulling historical activity for the sector while I looked at tasking the UAV. That's where things got tight, because we only had the one asset and there were competing requests elsewhere in the sector that night.

Interviewer: Let's stay on that first call for a second — classifying the alert as elevated. What alternatives did you consider?

Participant: I could've left it routine and waited for more data, or reached out to the adjacent unit for corroboration before deciding priority. Comms with them were spotty that night, intermittent SATCOM, so that would've cost time. I went with elevating it based on what I already knew.

Interviewer: How confident were you in that classification at the time?

Participant: Moderately. I didn't have hard evidence, just the pattern match in my head to the earlier event.

Interviewer: Understood. So then you moved to the ISR tasking decision — walk me through that.

Participant: Right, with only one UAV, I had to justify diverting it to NAI-7 over the other requests. To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first.

Interviewer: Were there other sources you could have checked?

Participant: Sure, there's the adjacent-unit SIGACT log and a sector-wide pattern-of-life database that tracks things like livestock movement and civilian traffic patterns near the perimeter. Both were accessible that night despite the comms issue — the pattern-of-life database is stored locally, actually.

Interviewer: Did you look at those before tasking the UAV?

Participant: No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later.

Interviewer: What made you stick with just the own-sector feed?

Participant: Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes.

Interviewer: What did the UAV feed show once it arrived on station?

Participant: Ambiguous thermal signatures. Could've been a small dismounted element, could've been livestock — genuinely hard to tell from the imagery alone. No weapons visible, no confirmed hostile indicators.

Interviewer: What did you do with that information?

Participant: I put the QRF on 15-minute alert status.

Interviewer: What alternatives were on the table at that point?

Participant: I could've held the current posture and requested more UAV dwell time to get a clearer picture, or asked the adjacent unit to send a ground patrol to verify visually before touching QRF readiness at all.

Interviewer: What tipped you toward alerting QRF instead of those options?

Participant: We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time.

Interviewer: Did the thermal evidence itself favor the ambush interpretation over livestock?

Participant: Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other.

Interviewer: What happened after QRF went to alert status?

Participant: Additional analyst review came back later and assessed the signatures as most consistent with livestock movement, based on movement speed and clustering patterns. QRF was never launched, just held at readiness.

Interviewer: How did you handle the final reporting for shift change?

Participant: I wrote it up as a genuinely mixed picture — noted the initial elevation, the QRF alert, and then the follow-up analyst assessment leaning non-hostile. I didn't want to call it a clean false alarm because the imagery was ambiguous enough that I couldn't rule out the dismounted-element read. I also didn't want to overstate it as an ongoing threat given what the analyst found. Higher headquarters ended up asking for a follow-up clarification the next day, which is pretty normal for anything left open like that.

Interviewer: Was there a point where you considered recommending a sensor review for NAI-7 instead?

Participant: I mentioned it as a secondary note, since that spot generates a fair number of ambiguous alerts, but I didn't want to bury the main SITREP under an infrastructure recommendation when the operational question was still open.

Interviewer: Stepping back — if the alert had come in during a quiet stretch with no recent similar incident in your memory, do you think you'd have classified it the same way?

Participant: Probably not as quickly to elevated. I think I'd have waited for the S2 pull before deciding priority.

Interviewer: If you'd checked the adjacent-unit and pattern-of-life data first, before your own-sector feed, do you think the tasking decision changes?

Participant: The UAV probably still goes to NAI-7 — that part of the call felt justified regardless. But I think how I framed the justification would've been different, maybe more grounded in actual cross-referenced history instead of just what was in front of me.

Interviewer: And if you hadn't run that ambush rehearsal in training recently, would you have read the thermal imagery differently?

Participant: Yeah, I think so. Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way.

Interviewer: Last question — looking back with everything you know now, what would you change?

Participant: Honestly, probably slow down at each of those first three points and force myself to check the wider data before trusting my first read. None of the individual calls were unreasonable given what I had in front of me, but I can see now where I leaned on what came to mind fastest instead of what was actually available.

Interviewer: That's really helpful. Thanks for walking through it in that much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Retrievability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as reliance on an easily-recalled recent personal precedent rather than base-rate or matching-signature reasoning" },
      { "bias": "Search set Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as restricting information search to the habitual/familiar repository while equally accessible alternative sources go unconsulted" },
      { "bias": "Imaginability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as a vividly imaginable rehearsed scenario inflating perceived probability over an equally evidenced but less vivid alternative" }
    ],
    "target_bias_names": ["Retrievability Bias", "Search set Bias", "Imaginability Bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Retrievability Bias", "requested_occurrences": 1 },
      { "bias": "Search set Bias", "requested_occurrences": 1 },
      { "bias": "Imaginability Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias" },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias" },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias", "decision_point": 1 },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias", "decision_point": 2 },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MD3_retr_01",
        "bias": "Retrievability Bias",
        "mechanism": "Ease of recalling a recent, salient infiltration precedent inflates perceived likelihood of the current ambiguous alert being a genuine threat",
        "affected_reasoning_operation": "Initial priority classification of an ambiguous sensor alert",
        "evidence_source": "Officer's own recollection of a prior incident, contrasted with the actual (weaker) evidentiary content of the current alert",
        "distinctiveness_requirement": "Must be tied specifically to memory recall driving classification, not to search-source restriction (MD3_ss_01) or to imagined future scenarios (MD3_im_01)"
      },
      {
        "instance_id": "MD3_ss_01",
        "bias": "Search set Bias",
        "mechanism": "Restriction of the information search to the habitual own-sector repository skews the evidentiary basis for ISR tasking despite equally available alternative repositories",
        "affected_reasoning_operation": "Evidence-gathering/source-selection prior to ISR tasking",
        "evidence_source": "Comparison between the repository actually consulted (own-sector SIGINT) and the repositories available but not consulted (adjacent-unit logs, pattern-of-life database)",
        "distinctiveness_requirement": "Must be tied specifically to which sources were queried, not to memory retrieval (MD3_retr_01) or to vividness of imagined outcomes (MD3_im_01)"
      },
      {
        "instance_id": "MD3_im_01",
        "bias": "Imaginability Bias",
        "mechanism": "A vividly rehearsed ambush scenario is easier to mentally simulate than the equally evidenced mundane alternative, inflating its perceived probability and driving QRF escalation",
        "affected_reasoning_operation": "Risk assessment and QRF readiness decision based on ambiguous thermal imagery",
        "evidence_source": "Officer's account of the mental scenario constructed from recent training, contrasted with the genuinely ambiguous thermal evidence",
        "distinctiveness_requirement": "Must be tied specifically to vividness/ease of mental simulation of an outcome, not to memory of a past real event (MD3_retr_01) or to which information sources were searched (MD3_ss_01)"
      }
    ],
    "intended_strength": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias", "strength": "subtle" },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias", "strength": "subtle" },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of adjacent-unit and pattern-of-life data at ISR tasking time",
      "original_state": "Officer consults only own-sector SIGINT summaries",
      "changed_state": "Officer's workflow automatically surfaces adjacent-unit and pattern-of-life data alongside own-sector summaries",
      "variables_to_hold_constant": [
        "Initial sensor alert content and ambiguity",
        "Single available ISR asset",
        "Time pressure and staffing shortfall",
        "Subsequent QRF and reporting decisions",
        "Personnel and stakeholders involved"
      ]
    },
    "scenario_id": "MD_Biased_3",
    "domain_id": "MD",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences spread across distinct decision points (1, 2, 3) per mechanism fit and narrative realism; decision point 4 reserved as bias-free reporting/closure phase; no bias assigned to more than one decision point; no two occurrences share a decision point so no cross-evidence-source separation was required.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Initial sensor alert content and ambiguity",
      "Single available ISR asset",
      "Time pressure and staffing shortfall",
      "Personnel and stakeholders involved",
      "Overall four-decision-point structure"
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
