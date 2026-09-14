You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'll ask you to walk me through a specific incident in detail, and there are no right or wrong answers. Everything's for internal learning purposes. Can you tell me your current role and how long you've been in it?

Participant: Sure. I'm the ventilation engineer for the underground section — mainly responsible for the primary and auxiliary fan systems, the VOD setup, and gas monitoring across the active levels. I've been in this role about six years, underground ventilation for closer to eleven overall.

Interviewer: Good. Let's start with the incident itself. What happened?

Participant: This was during a shift where we had a scheduled production blast on 14 Level. Standard round, nothing unusual planned. About thirty minutes after blast clearance time, one of our gas stations — GS-14R, out in the return airway — started reading CO at 280 ppm. Baseline after a blast like that is usually under 50 ppm once the primary fan's had time to clear it. So that number stood out immediately.

Interviewer: What went through your mind when you saw that?

Participant: Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again. I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience.

Interviewer: Was there any other information available to you at that point?

Participant: Yes — the gas monitoring technician had taken a handheld multi-gas detector reading out at the return airway around the same time, and that came back at 190 ppm. Lower than the station reading, but still well above baseline. No maintenance ticket had confirmed a fault on GS-14R yet either — that hadn't been checked this shift.

Interviewer: How did you weigh those two numbers against each other?

Participant: I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.

Interviewer: Did you consider getting a second confirmatory reading, or requesting a recalibration check before deciding?

Participant: I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward.

Interviewer: What happened next?

Participant: Re-entry went ahead. About twenty minutes later, the shift boss called me — one of the crew wanted to hold at the refuge chamber a few extra minutes before heading further in, just as a precaution. Nothing specific triggering it, more a gut feeling.

Interviewer: What was your reasoning at that point?

Participant: That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.

Interviewer: Was there anything in the data at that point pointing toward fire specifically?

Participant: Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger.

Interviewer: How did that play out?

Participant: No fire indicators ever showed up. We eventually put it down to a longer-than-usual round that took a bit more time to clear than normal. The fifteen-minute hold turned out to be unnecessary, though nobody complained about the extra caution.

Interviewer: Let's move to the threshold question. What came up there?

Participant: Later that shift, the mine planning superintendent asked whether we should revise the CO auto-cutoff setpoint on GS-14R before ramping the LHD fleet back up fully. Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now.

Interviewer: Did you have newer data available?

Participant: We did, and it was actually pretty usable. The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous. A couple of us had even talked informally about a materially higher interim figure being more realistic given those numbers. We hadn't done a formal re-baseline since the fleet expanded two years ago, but the recent surveys were solid enough to work from for an interim call.

Interviewer: What did you decide?

Participant: I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested.

Interviewer: How did that work out afterward?

Participant: Not great, if I'm honest. Over the following shifts the auto-cutoff started tripping more often during normal diesel-heavy periods — nothing hazardous, just operational friction, alarms going off during routine LHD movement. We've since talked about doing the full re-baseline properly.

Interviewer: Last decision point — the incident closeout. Walk me through that.

Participant: The safety officer wanted a closing narrative before full production resumed. By that point we had three things on the table: the sensor's drift history, the LHD fleet idling near the loading point during the relevant window, and the fact that the round itself ran a bit long. None of those had been tested individually — we hadn't isolated the sensor alone, or the fleet alone, to see which one actually explained the spike.

Interviewer: How did you write it up?

Participant: I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure. Mine planning was waiting on that closure to greenlight full resumption, so I didn't push for a separate follow-up test.

Interviewer: Looking back, is there another explanation that fits those same facts just as well?

Participant: In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from.

Interviewer: If the handheld reading that morning had come back much higher than the station reading, would your first call have changed?

Participant: Probably, yes. If it had matched or exceeded the station number, I'd have taken it more seriously as a real hazard rather than sensor noise.

Interviewer: And if you'd had time to run a full re-baseline before setting the threshold?

Participant: I'd have set it higher, most likely, based on the newer survey data. Time was the constraint there, not confidence in the old number.

Interviewer: How much would you say the schedule pressure from mine planning shaped your decisions that day?

Participant: More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Narrative Fallacy", "occurrences": 1, "mechanism_constraint": "Must occur only at final incident-closure decision as a single overconfident causal synthesis of three loosely related, untested facts" },
      { "bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "Must occur only at initial sensor-reading interpretation via selective weighting of drift history over corroborating handheld data" },
      { "bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "Must occur only at threshold-setting decision via insufficient adjustment from the original commissioning figure" },
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Must occur only at the re-entry/hold decision via overweighting a vivid remembered fire case over local base rates" }
    ],
    "target_bias_names": ["Narrative Fallacy", "Confirmation Bias", "Anchoring Bias", "Availability Bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Narrative Fallacy", "requested_occurrences": 1 },
      { "bias": "Confirmation Bias", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 },
      { "bias": "Availability Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias" },
      { "instance_id": "av_01", "bias": "Availability Bias" },
      { "instance_id": "an_01", "bias": "Anchoring Bias" },
      { "instance_id": "nf_01", "bias": "Narrative Fallacy" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1 },
      { "instance_id": "av_01", "bias": "Availability Bias", "decision_point": 2 },
      { "instance_id": "an_01", "bias": "Anchoring Bias", "decision_point": 3 },
      { "instance_id": "nf_01", "bias": "Narrative Fallacy", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective weighting of prior sensor-drift history as confirming evidence while discounting an independent corroborating handheld reading",
        "affected_reasoning_operation": "evidence weighting and selection during hazard interpretation",
        "evidence_source": "GS-14R drift history vs. handheld multi-gas detector reading",
        "distinctiveness_requirement": "Must be tied specifically to the sensor-fault interpretation at Decision Point 1; must not overlap with the threshold-anchoring reasoning at Decision Point 3"
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Overweighting a vivid, memorable prior fire incident relative to the actual base rate of mundane fume-clearance delays at this mine",
        "affected_reasoning_operation": "probability estimation under uncertainty",
        "evidence_source": "Recalled fatal fire case vs. absence of local smoke/heat/secondary-gas indicators",
        "distinctiveness_requirement": "Must be tied to the re-entry/hold judgment at Decision Point 2; must not be reused as the causal narrative at Decision Point 4"
      },
      {
        "instance_id": "an_01",
        "bias": "Anchoring Bias",
        "mechanism": "Insufficient adjustment of the CO auto-cutoff threshold away from a five-year-old commissioning figure despite new baseline data",
        "affected_reasoning_operation": "numerical threshold estimation and adjustment",
        "evidence_source": "Original commissioning report (100 ppm) vs. recent baseline survey data under current depth/fleet conditions",
        "distinctiveness_requirement": "Must be confined to the threshold-setting decision at Decision Point 3; distinct from the sensor-fault evidence weighting at Decision Point 1"
      },
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Construction of one coherent, satisfying causal chain linking sensor drift, idling diesel fleet, and round length without any test isolating the true cause",
        "affected_reasoning_operation": "retrospective causal attribution / incident-report synthesis",
        "evidence_source": "Three untested candidate causes combined into a single closing account",
        "distinctiveness_requirement": "Must occur only at final report closure (Decision Point 4); must not restate or repeat the Decision Point 1 sensor-fault reasoning"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "an_01", "bias": "Anchoring Bias", "strength": "moderate" },
      { "instance_id": "nf_01", "bias": "Narrative Fallacy", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of a second corroborating handheld gas reading before the Decision Point 1 sensor-fault call",
      "original_state": "Only one handheld cross-check reading available and discounted",
      "changed_state": "A second independent, spatially distinct handheld reading corroborates elevated CO before the sensor-fault call",
      "variables_to_hold_constant": [
        "Blast timing and clearance schedule",
        "Mine planning production pressure",
        "GS-14R prior drift history",
        "Facts available at Decision Points 2 through 4"
      ]
    },
    "scenario_id": "MU_Biased_4",
    "domain_id": "MU",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point selected for best mechanism fit and narrative realism (mechanism-fit-first allocation, no bias sharing a decision point with another bias or with itself)",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Occupational setting (underground decline gold mine, VOD system)",
      "Four-decision-point structure",
      "Moderate difficulty level",
      "Word count target of 1,350 (range 1,215-1,485)"
    ],
    "generation_warnings": [
      "No manifest-fulfillment problems identified: all four requested occurrences (one each) are plausibly and distinctly embeddable within the four planned decision points without repetition or overlap.",
      "The counterfactual_specification field was populated via AUTOSELECT for potential future pairing/testing purposes only; it is not activated under the current 'biased' condition and should not be interpreted as an executed counterfactual for this scenario_id."
    ]
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
