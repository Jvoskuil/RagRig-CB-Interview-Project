You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm this is a routine debrief on your reasoning process during the Copper Creek event, not a performance review. Nothing here affects your evaluation. Are you okay proceeding on that basis?

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Great. Can you start by describing your role on the desk that shift?

Participant: I'm the meteorological hazard forecaster for the ESF-2/ESF-5 desk at the state EOC. My job is basically to translate NWS and SPC guidance into activation-level recommendations, warning products, and messaging calls for the counties in our basin. I coordinate with the WFO, the county EMs, and on multi-state events, with neighboring forecast desks.

Interviewer: Walk me through this particular incident from the start.

Participant: It started overnight with SPC flagging a marginal severe risk for the basin, low confidence, mostly because guidance was still sparse. By the 06Z cycle we only had four members of the convection-allowing ensemble finished — the rest were still running. Three of those four showed the cluster intensifying fast over the basin within about three hours. That got my attention because it lined up with what SPC's mesoscale discussion was hinting at, even though they were pretty upfront that confidence was low given how little guidance was in yet. I made the call to push an early watch-to-warning upgrade based on that signal rather than wait for the fuller 09Z set. A couple hours later, radar showed a hook-shaped reflectivity signature that looked almost identical to an event I'd forecasted successfully a couple seasons back — same kind of setup, similar CAPE and shear profile. I was fairly confident about the track and timing at that point. Then flash flood guidance started trending up in two of our sub-watersheds, and I wanted to escalate the EOC activation level and get swift-water teams moving, since they need about 45 minutes lead time. But the regional director called and told the desk to hold pending review. Later, on the interstate coordination call, most of the neighboring jurisdictions said they were holding their alert levels too, so we ended up staying at the same level even though our local numbers kept climbing. Flooding started in one of our communities about fifty minutes after that call ended.

Interviewer: Let's reconstruct the sequence a bit more precisely. What did you have in front of you at each stage, and what were you still waiting on?

Participant: At the start, just the partial ensemble and the SPC discussion — no radar-observed rotation or flood-guidance exceedance yet. Then the radar signature came in, which added a qualitative cue on top of the model data. After that, the guidance numbers started climbing, which was the first hard hydrologic evidence. And finally, the coordination call added the social layer — what everyone else on the basin was doing.

Interviewer: Let's go through the four moments where you had to make a call. First: the early upgrade decision. What were the alternatives you weighed?

Participant: I could've upgraded early, held until the 09Z cycle with the bigger ensemble, or done a limited advisory just for the highest-confidence sub-area. I went with the early upgrade.

Interviewer: What tipped it?

Participant: Three of the four members agreeing was a strong signal to me. When you get that kind of consistency across model runs, it usually means something real is going on with the pattern.

Interviewer: Did the size of that ensemble — four members — factor into how much weight you gave it?

Participant: Not really, no. I mean, agreement is agreement. If three separate runs are telling you the same intensification story, that's meaningful regardless of how many total members happened to finish by that hour.

Interviewer: And the SPC discussion's confidence language?

Participant: They noted it was low confidence because guidance was still limited, but I read that as boilerplate caution rather than something that should change how I weighted the signal itself.

Interviewer: Second decision — the radar signature and the track call. What made you settle on one track over maintaining both possibilities?

Participant: Honestly, the moment I saw that hook signature, it just clicked. I'd seen that exact shape develop the same way before, and it played out almost identically that time — same track, same timing window. I didn't feel like I needed to keep hedging between two tracks once I recognized the pattern.

Interviewer: Did you check that recognition against anything, like requesting the WFO's independent read before committing?

Participant: I didn't loop them in before committing, no. It felt clear enough on its own. Turned out the WFO desk was independently tracking a similar dual-track possibility, and the storm's actual path drifted a bit from what I'd called.

Interviewer: How confident were you in the moment, on a scale of how sure you'd normally be?

Participant: Pretty high, honestly — nine out of ten maybe. It looked so much like that prior case that I didn't see much reason to hedge.

Interviewer: Third decision point — the activation-level call after the director's instruction. What was your read going in?

Participant: My read was that guidance exceedance was climbing in two sub-watersheds and we should escalate and get swift-water teams moving given the lead time they need. Then the director called and said hold pending review, no new data attached to that, just a directive.

Interviewer: What did you do?

Participant: I held. He's the one with sign-off authority on activation level changes, so when he says hold, that's generally the end of the discussion on my end.

Interviewer: Was there a technical case for holding at that moment, independent of the instruction?

Participant: Not that I put together myself, no. I didn't really push back or lay out the counter-argument. He asked afterward for a written justification for the hold, and I had to go back and construct one after the fact.

Interviewer: Fourth decision — the coordination call and public messaging.

Participant: Going into that call, my own numbers favored escalating messaging and issuing a WEA. But three of the four neighboring jurisdictions said they were holding steady, and it just felt safer to stay aligned with that rather than break from the group on my own.

Interviewer: Even though your local guidance had worsened since the director's hold?

Participant: Right, it had ticked up further. But when the majority of the desks on the call are holding, going a different direction on your own feels like it needs more justification than staying with the group does.

Interviewer: What happened afterward?

Participant: Flooding started in one of our towns about fifty minutes later. One of the neighboring jurisdictions ended up escalating on their own shortly after, citing their local data.

Interviewer: If the fuller ensemble set had been available from the very start, do you think the early upgrade call would have gone differently?

Participant: Maybe — if the signal had been muddier across more members I might have waited. But I don't think I would have weighted it much differently than I did.

Interviewer: If the director's call hadn't come in at that third decision point, what would you have done?

Participant: I probably would have pushed the escalation through myself. It was really his instruction that changed my course there.

Interviewer: Looking back, with exactly the same information you had at each point, what would you do differently?

Participant: I'd probably slow down at the radar-signature moment and get a second set of eyes before locking onto one track. And on the coordination call, I'd try to separate what our own numbers were saying from what everyone else on the call was doing before deciding.

Interviewer: That's helpful. Thanks for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusion of Validity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as unwarranted near-certainty in track/timing derived from personal pattern recognition, not merely stating experience was useful."
      },
      {
        "bias": "Insensitivity to sample size",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as treating a very small ensemble set (4 members) as robust confirmatory evidence without caveat."
      },
      {
        "bias": "Authority Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as compliance justified by the director's rank/authority rather than by technical evidence accompanying the directive."
      },
      {
        "bias": "Bandwagon effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a shift in the forecaster's own decision to match peer-jurisdiction consensus despite worsening local evidence."
      }
    ],
    "target_bias_names": [
      "Illusion of Validity",
      "Insensitivity to sample size",
      "Authority Bias",
      "Bandwagon effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Illusion of Validity", "requested_occurrences": 1 },
      { "bias": "Insensitivity to sample size", "requested_occurrences": 1 },
      { "bias": "Authority Bias", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Insensitivity to sample size" },
      { "instance_id": "cb_02", "bias": "Illusion of Validity" },
      { "instance_id": "cb_03", "bias": "Authority Bias" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Insensitivity to sample size", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Illusion of Validity", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Authority Bias", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Insensitivity to sample size",
        "mechanism": "Overweighting agreement among only 4 ensemble members as statistically decisive without caveat",
        "affected_reasoning_operation": "Probability estimation from ensemble guidance",
        "evidence_source": "06Z convection-allowing ensemble (4 members) and SPC mesoscale discussion",
        "distinctiveness_requirement": "Distinct from cb_02 by operating on quantitative model-ensemble data rather than qualitative radar-signature pattern recognition."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Validity",
        "mechanism": "Expressing near-certainty in track/timing from a subjectively recognized radar signature lacking formal verification",
        "affected_reasoning_operation": "Subjective confidence calibration in track/timing forecast",
        "evidence_source": "Radar reflectivity pattern compared to a previously forecasted event",
        "distinctiveness_requirement": "Distinct from cb_01 by relying on personal pattern-recognition confidence rather than aggregated model-run agreement."
      },
      {
        "instance_id": "cb_03",
        "bias": "Authority Bias",
        "mechanism": "Deferring to the director's hold directive because of rank/authority rather than accompanying technical justification",
        "affected_reasoning_operation": "Integration of organizational directive versus own technical evidence",
        "evidence_source": "Director's phone directive plus concurrent flash-flood guidance exceedance data",
        "distinctiveness_requirement": "Distinct from cb_04 by involving a vertical, hierarchical directive from a single superior rather than horizontal peer consensus."
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "mechanism": "Shifting away from an independent inclination to escalate messaging to match the stated majority position of peer jurisdictions",
        "affected_reasoning_operation": "Revision of escalation/messaging decision based on peer consensus rather than local evidence trend",
        "evidence_source": "Interstate coordination call statements from neighboring jurisdictions plus local worsening guidance data",
        "distinctiveness_requirement": "Distinct from cb_03 by involving horizontal peer-agency consensus rather than a hierarchical directive."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Insensitivity to sample size", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Illusion of Validity", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Authority Bias", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence versus absence of the regional EOC director's hold directive at decision point 3",
      "original_state": "Director issues a hold directive without accompanying new technical evidence",
      "changed_state": "No directive issued; forecaster's decision rests solely on trending technical data",
      "variables_to_hold_constant": [
        "Storm evolution and meteorological data timeline",
        "Forecaster's role, seniority, and prior experience",
        "Coordination call composition and peer positions",
        "Resource constraints"
      ]
    },
    "scenario_id": "EM_Biased_4",
    "domain_id": "EM",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias, each assigned to a distinct decision point (DP1: Insensitivity to sample size on ensemble data; DP2: Illusion of Validity on radar pattern recognition; DP3: Authority Bias on hierarchical directive; DP4: Bandwagon effect on peer-agency consensus), selected for mechanism fit and chronological narrative realism. No decision point contains more than one instance of any single bias, and no two instances share an evidence source.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Storm characteristics and evolution",
      "Personnel roles and organizational structure",
      "Resource constraints and timing windows",
      "Basin geography and vulnerable-community locations"
    ],
    "generation_warnings": [
      "counterfactual_variable was autoselected per input instruction (AUTOSELECT) for documentation and future pairing purposes only; it is not activated under the current 'biased' condition and has no bearing on the exact-occurrence manifest for this scenario."
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
