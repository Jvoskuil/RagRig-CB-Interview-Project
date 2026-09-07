You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm looking to understand how you actually reasoned through the feedwater heater trend during the ascension test, not to evaluate your performance. Everything stays de-identified for training and procedure review purposes. Sound okay?

Participant: Yeah, that's fine. I figured this was coming after the work order got written up.

Interviewer: Good, let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend?

Participant: Sure. We were about three hours into the ascension test, sitting around 90 percent power, working toward the dispatch commitment at end of shift. I was at the controls, doing my normal rounds on the trend recorders, and I caught that heater 1B outlet temperature had crept up about three degrees over maybe twenty minutes. Train 1A was steady, no issue there. No alarm, nothing outside our Tech Spec limit. My first thought honestly was, "here we go again" — we'd had a calibration deviation on that exact sensor last cycle, logged and closed out. So I figured that was probably it.

Interviewer: What was going through your head at that point, in terms of goals and pressures?

Participant: Main thing was getting to a hundred percent within the dispatch window — we had about two hours of slack at that point. I wasn't in a panic, but I was aware the schedule mattered. And with the calibration history sitting right there in my head, the drift didn't feel like something new. It felt like the same story playing out again.

Interviewer: Let's reconstruct the timeline a bit before we get into the decisions themselves. After you first noticed the drift, what happened next?

Participant: I logged it as consistent with the prior calibration pattern and kept going with the ascension sequence. About fifteen minutes later the trend was still creeping, still shallow, still inside limits. Then a bit after that — maybe forty minutes in total — a maintenance tech doing an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. Shortly after that call, the trend recorder actually started flattening out as we approached the final ascension step.

Interviewer: Okay, let's go through this decision by decision. First one: when you saw that initial drift, what alternatives did you actually consider?

Participant: There were really two options. Either treat it as the same calibration issue from last cycle and just keep trending, or treat it as something new and call for an independent instrument check, maybe get I&C down there. I went with the first.

Interviewer: What made you settle on that one?

Participant: The pattern matched what we'd seen before — small, slow rise, no other train affected, no alarm. When something lines up that cleanly with a known cause, it's hard not to read it that way. I didn't really see a strong reason to go pull I&C off what they were doing for something that already had an explanation on file.

Interviewer: Did you consider what it would take to rule that explanation out?

Participant: Not really, no. I suppose I could've asked for a quick independent check on the sensor loop, but at the time it seemed like it would've been overkill given what I was looking at. I didn't go back and check whether the specific signature we saw last cycle — the way that fault crept in — actually matched what I was seeing on 1B. I just saw "same sensor, same shape" and moved on, since I was already treating it as the same event.

Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available where you could've briefed the STA before continuing. What went into that call?

Participant: The STA was right there, actually, just hadn't said anything to him yet about it. I remember thinking it "felt manageable" — the number was moving, but slowly, and we still had margin to the limit and time in the schedule. I didn't sit down and work through the hold-point criteria formally, if I'm honest. It was more of a quick gut check — this looks like the same thing, we've got room, let's keep the momentum going and I'll mention it at the next shift briefing.

Interviewer: Was the dispatch window part of that calculation?

Participant: A little, yeah. Stopping to formally brief would've meant slowing the pace, and I didn't feel like the data demanded that yet.

Interviewer: Right after that, the technician's infrared call came in. Walk me through how you weighed that against what you were seeing on the trend recorder.

Participant: That's the one I've gone back and forth on since. His reading suggested localized heating, which is a bit different from what a simple sensor drift would look like. But my trend recorder was showing this nice smooth rise, exactly the shape I associated with the calibration issue. I had that graph in front of me continuously — I'd been watching it for almost an hour. His reading was a single handheld measurement, called in over the radio, and once the call ended I honestly wasn't holding it in my head the same way — my eyes kept going back to the display in front of me, not to what he'd said.

Interviewer: How did you end up weighting the two?

Participant: I leaned toward the trend data. Partly because it was the instrument I trust for that parameter, and partly because, honestly, he doesn't spend his day reading control room trends the way we do — his experience is more hands-on with the equipment itself, not with interpreting these signatures. I figured his reading was probably picking up ambient heat or an inconsistent scan angle, something like that. I didn't ask him to take a second scan or check his baseline before writing it off, but I also didn't stop to double-check my own read of the trend line the same way — I just logged his call as likely noise from the handheld device rather than something that changed my read on the situation.

Interviewer: Did anything about that reasoning give you pause?

Participant: A little, yeah. He's not wrong about heat exchangers — that's literally his specialty, probably more relevant to shell heating than what I look at day to day. But in the moment, my trend line just felt like the stronger evidence, and honestly there's something about hearing it from another operator — someone who sees the plant the way we see it in here — that would've landed differently than a radio call from the field, even with the same words.

Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed rather than hold?

Participant: At that point I had the flattening trend, which fit with the calibration story settling back down, plus the history from last cycle. Time was getting tighter on the dispatch commitment too. I didn't loop back to the technician's earlier call at that point — my attention was on the ascension step itself and whether the number in front of me supported moving forward. Given what I was looking at right then, it seemed like enough to go.

Interviewer: Did you consider requesting a hold for independent verification before that step?

Participant: I thought about it briefly, but between the schedule and what the trend was showing, it didn't seem necessary at the time.

Interviewer: How much uncertainty did you feel across all of this?

Participant: Some, especially after the tech's call. But nothing that crossed into "this violates a limit" territory, so it stayed more like background noise than something driving the decisions.

Interviewer: Let's close with a couple of hypotheticals. If that infrared call had come from another licensed operator instead of a maintenance tech, do you think you'd have weighed it differently?

Participant: Probably, yeah. I think I'd have taken it more seriously right away rather than filing it as likely noise.

Interviewer: And if the trend had kept climbing instead of flattening near the final step?

Participant: Then I think I would've held and called the STA in properly. The flattening is honestly what let me feel okay proceeding.

Interviewer: Last one — looking back, is there a point where, with the same information you had, you might've made a different call?

Participant: Maybe the second one. I could've just briefed the STA early and let him weigh in, even without hard evidence something was wrong. It wouldn't have cost us much time, and it would've gotten another set of eyes on it before things went further.

Interviewer: That's helpful, thank you. I think that covers everything I needed.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias",
        "occurrences": 2,
        "mechanism_constraint": "One instance at initial ambiguous-evidence interpretation (decision point 1); one instance at discounting new disconfirming field evidence (decision point 3). Must use distinct evidence sources."
      },
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Expressed as a non-systematic, satisficing escalation decision at decision point 2, not as an outcome failure."
      },
      {
        "bias": "Salience Bias",
        "occurrences": 1,
        "mechanism_constraint": "Expressed as overweighting the visually prominent trend recorder over a verbally reported field observation at decision point 3."
      },
      {
        "bias": "Similarity Bias",
        "occurrences": 1,
        "mechanism_constraint": "Expressed as discounting a source based on dissimilar role/background rather than content, at decision point 3."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": "Expressed as an incomplete-information final integrative decision under time/cognitive constraints at decision point 4."
      }
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Imperfect Rationality",
      "Salience Bias",
      "Similarity Bias",
      "Bounded Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confirmation Bias", "requested_occurrences": 2 },
      { "bias": "Imperfect Rationality", "requested_occurrences": 1 },
      { "bias": "Salience Bias", "requested_occurrences": 1 },
      { "bias": "Similarity Bias", "requested_occurrences": 1 },
      { "bias": "Bounded Rationality", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias" },
      { "instance_id": "cb_02", "bias": "Confirmation Bias" },
      { "instance_id": "ir_01", "bias": "Imperfect Rationality" },
      { "instance_id": "sb_01", "bias": "Salience Bias" },
      { "instance_id": "sim_01", "bias": "Similarity Bias" },
      { "instance_id": "br_01", "bias": "Bounded Rationality" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Confirmation Bias", "decision_point": 3 },
      { "instance_id": "ir_01", "bias": "Imperfect Rationality", "decision_point": 2 },
      { "instance_id": "sb_01", "bias": "Salience Bias", "decision_point": 3 },
      { "instance_id": "sim_01", "bias": "Similarity Bias", "decision_point": 3 },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective interpretation of ambiguous drift as matching a known prior-cycle belief, without seeking disconfirming checks",
        "affected_reasoning_operation": "Initial hypothesis selection",
        "evidence_source": "trend recorder drift plus prior-cycle calibration log",
        "distinctiveness_requirement": "Occurs at initial evidence interpretation before any conflicting data exists; distinct from cb_02 which involves discounting new conflicting data"
      },
      {
        "instance_id": "cb_02",
        "bias": "Confirmation Bias",
        "mechanism": "Reinterpreting new disconfirming field evidence (infrared reading) as noise to preserve the pre-existing calibration-drift belief",
        "affected_reasoning_operation": "Belief updating in response to new conflicting evidence",
        "evidence_source": "technician's infrared handheld reading",
        "distinctiveness_requirement": "Occurs after new disconfirming evidence arrives, at a different decision point and evidence source than cb_01"
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Non-exhaustive, satisficing weighing of escalation criteria under time and information constraints, rather than systematic evaluation",
        "affected_reasoning_operation": "Escalation/deferral decision-making",
        "evidence_source": "trend continuation, hold-point procedure, dispatch schedule",
        "distinctiveness_requirement": "Distinct from bounded rationality instance (br_01) by focusing on the escalation judgment process itself rather than integration of multiple data sources at the final step"
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "mechanism": "Overweighting the continuously visible trend graph relative to a verbally reported one-time field observation",
        "affected_reasoning_operation": "Evidence source weighting",
        "evidence_source": "trend recorder display versus radioed verbal report",
        "distinctiveness_requirement": "Distinct from cb_02 by focusing on visual prominence/attention capture rather than belief-preservation motive"
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "mechanism": "Discounting technician's report based on dissimilarity of role/training rather than content of the observation",
        "affected_reasoning_operation": "Source credibility assessment",
        "evidence_source": "technician's background/role as stated in the report",
        "distinctiveness_requirement": "Distinct from sb_01 and cb_02 by grounding the discounting in source identity/similarity rather than evidence format or belief consistency"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Using a limited subset of available information for the final go decision due to cognitive/time constraints, without revisiting unresolved uncertainty",
        "affected_reasoning_operation": "Final integrative go/no-go judgment",
        "evidence_source": "flattening trend, prior precedent, unresolved technician report",
        "distinctiveness_requirement": "Distinct from ir_01 by occurring at the final integrative decision point and reflecting information-processing capacity limits rather than escalation-judgment style"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "ir_01", "bias": "Imperfect Rationality", "strength": "subtle" },
      { "instance_id": "sb_01", "bias": "Salience Bias", "strength": "subtle" },
      { "instance_id": "sim_01", "bias": "Similarity Bias", "strength": "subtle" },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_6",
    "domain_id": "NP",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across 4 decision points by mechanism fit: decision point 1 received one confirmation-bias instance (initial interpretation); decision point 2 received the imperfect-rationality instance (escalation judgment); decision point 3 received three instances (second confirmation-bias occurrence, salience bias, similarity bias), each tied to a distinct evidence source or reasoning operation (belief-preservation vs. visual prominence vs. source-identity discounting) per the multi-occurrence-per-point rule; decision point 4 received the bounded-rationality instance (final integrative judgment). No bias exceeded two instances at a single decision point, and no two instances at the same decision point shared an evidence source or reasoning operation.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": [
      "Decision point 3 carries three distinct bias instances (cb_02, sb_01, sim_01) to satisfy mechanism-fit requirements, since the technician-report conflict is the most natural location for confirmation, salience, and similarity biases to jointly manifest through different evidence-processing routes; each instance is documented with a distinct evidence source and reasoning operation to preserve independent identifiability and avoid redundancy."
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
