You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on a process event from your shift — I'll ask you to walk me through what happened and how you made a few of the calls along the way. Nothing here goes into your personnel file, it's for improving our SPC response process. Sound okay?

Participant: Sure, no problem. Happy to walk through it.

Interviewer: Great. Can you start by telling me what your role was that day and what first drew your attention to the control chart?

Participant: I'm the QA analyst covering statistical process control for the turning cell that makes the automotive shafts. I was watching the Xbar-R chart for outer diameter like normal, two subgroups an hour from the automated gauge. I noticed three subgroup means in a row creeping upward, and the most recent one landed in the warning zone — inside two sigma, not over the UCL yet. Range chart was still flat, so whatever was happening wasn't blowing up part-to-part variability, just shifting the average.

Interviewer: What was going through your mind at that point?

Participant: Honestly, at 62% through the shift's quota, my first instinct was not to panic. A single warning-zone point isn't automatically an assignable cause under the Western Electric rules — you need a pattern. But three rising points is a pattern worth respecting. Nothing had been logged yet, no maintenance, no material change, so I didn't have an obvious explanation.

Interviewer: Walk me through what happened next, chronologically.

Participant: I tightened up sampling instead of pulling the trigger on a full stop. I figured if it was real, the next subgroup would confirm it, and if it was noise, extra samples would show it settling back down. Sure enough, the next subgroup crossed the UCL outright. I did a manual spot check with a hand micrometer to rule out a gauge artifact, and it matched the automated reading, so I knew it was real.

Interviewer: At that first decision point, what alternatives did you weigh, and why did you choose to increase sampling rather than halt immediately?

Participant: I could have shut it down right there, or just logged it and kept going. Stopping the line on one warning-zone point felt premature — that costs us 45 minutes of changeover time we might not need, and we're still trying to hit quota. Ignoring it felt reckless given the trend. Increasing sampling was the middle path — get more data fast without committing to downtime.

Interviewer: Once you confirmed the out-of-control signal, what did you look at to figure out the cause?

Participant: I pulled up everything I had access to in real time. The shop floor temperature log showed about a three-degree rise over the same two-hour window as the drift. The material lot traveler — which lags real time by about an hour — showed a new lot had been loaded roughly ninety minutes before the drift started. I hadn't checked the tool wear sensor yet at that point. I also mentioned to our process engineer what I was seeing, and he said temperature swings had caused drift on that machine before.

Interviewer: Given both the temperature rise and the new lot were roughly time-aligned with the drift, what made you lean toward temperature as the explanation?

Participant: The timing just lined up so cleanly — the temperature started climbing and almost immediately the dimension started walking. And the engineer's comment reinforced it, since he'd seen that pattern before on this exact machine. Pulling a hardness sample on the new lot would have meant sending it to the lab and waiting, and honestly the temperature story felt like it explained things well enough that I didn't prioritize that test at the time.

Interviewer: Did you do anything to directly check the lot hypothesis before moving forward?

Participant: Not at that point, no. I noted it in my log as a secondary possibility, but I put my attention on documenting the temperature correlation and kept monitoring under that assumption.

Interviewer: Let's move to the next stretch of the shift. What came in after that?

Participant: The tool wear sensor data finally came through. It showed cumulative cutting distance at 78% of rated tool life. That surprised me a little because I'd been thinking of that insert as basically new — we'd swapped it two days earlier, and two-day-old tools don't usually burn through life that fast. But there it was. And the drift direction, diameter trending undersize, is a classic tool wear signature on that machine.

Interviewer: How did that sensor reading change your thinking about the tool?

Participant: It definitely registered as a data point I couldn't dismiss. But my mental model going in was that this tool was recently serviced and shouldn't be a major factor yet, and that's a hard thing to fully shake in the moment. I had ninety minutes left in the shift and changeover was coming up, so stopping for a full tool change felt like a big move to make off one sensor reading, even a striking one.

Interviewer: So what did you decide to do?

Participant: I made a small in-process offset adjustment to compensate for the drift and kept running, planning to keep a close eye on the next few subgroups rather than pulling the tool right away.

Interviewer: Looking back, what alternatives did you consider there, and why didn't the offset feel like enough given what the sensor showed?

Participant: I considered halting for a tool change outright, and I considered just running it out unchanged since the tool was "recently serviced." The offset felt like a reasonable middle ground given the time pressure — I wasn't fully dismissing the wear reading, I was just not ready to treat it as the whole story yet.

Interviewer: What happened after that adjustment?

Participant: The next sample still trended toward the lower spec limit, so the offset wasn't holding. Then shift changeover happened, and the incoming night operator mentioned the tool had sounded different in the last hour — a cue I obviously didn't have access to until after the handoff.

Interviewer: Bring me to the end of the shift. What did the final data show, and what did you decide?

Participant: By the end, several parts were near or slightly under the lower spec limit. The wear sensor was up to 91%. Cpk for the last two hours had dropped from 1.42 to 1.05, which is a real capability hit. At that point I recommended an immediate tool change, a temporary update to the control chart center line, and I filed a deviation report covering the affected parts.

Interviewer: What tipped you fully toward that recommendation?

Participant: The Cpk drop was the clincher, honestly, combined with the wear number climbing another thirteen points in a short window. That's not marginal anymore, that's a tool that's clearly done. And with parts sitting near spec limits, a deviation report was required regardless of what I concluded about the cause.

Interviewer: What happened after the tool change?

Participant: It resolved it. The next shift's dimensions went right back to the historical baseline. And when the lab result on that new material lot finally came back, the hardness was within spec after all — so that wasn't a factor.

Interviewer: If the tool wear data had been available an hour earlier, do you think it would have changed your call at the offset-adjustment point?

Participant: Possibly. If I'd seen 78% that much earlier with more of the shift left, I might have leaned toward the tool change sooner rather than the offset. The compressed time at the end made a bigger intervention feel less appealing.

Interviewer: And if the lot hardness test had come back out of spec instead?

Participant: Then I'd have had two live explanations instead of one, and I probably would have had to test them against each other more directly instead of settling on temperature early.

Interviewer: Anything you'd do differently in how you weighed the temperature information against the lot information?

Participant: In hindsight, I could have pulled that lot sample earlier instead of waiting — it wouldn't have cost much time, and it would have closed off one hypothesis instead of leaving it as an unexamined footnote.

Interviewer: Last one — how much did the approaching shift changeover and time pressure shape your decisions overall?

Participant: Quite a bit, especially at the tool wear point. Knowing changeover was close made me want to avoid committing to a full stop until the evidence was overwhelming, which is part of why I went with the smaller offset first instead of pulling the tool right when the sensor data came in.

Interviewer: That's really helpful, thank you for walking through all of that in detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Correlation bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as causal attribution from temporal co-occurrence (temperature vs. dimension drift) while an equally available alternative (material lot) is not tested with equivalent rigor"
      },
      {
        "bias": "Conservatism Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as insufficient belief revision toward tool wear despite strong new quantitative sensor evidence, anchored to an earlier 'tool recently replaced' assumption"
      }
    ],
    "target_bias_names": [
      "Correlation bias",
      "Conservatism Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Correlation bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Conservatism Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "decision_point": 2
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "mechanism": "Causal inference drawn from temporal co-movement of temperature and dimensional drift, with a comparably available material-lot explanation left untested at the same rigor level",
        "affected_reasoning_operation": "Causal attribution and evidence-selection during root-cause hypothesis formation",
        "evidence_source": "Temperature log and material lot traveler, both available within the same investigative window",
        "distinctiveness_requirement": "This is the only planned correlation-bias instance; it must not be repeated as a second independent occurrence elsewhere (e.g., decision point 4's closure of the lot hypothesis is an outcome explanation, not a second instance)"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "mechanism": "Underweighting of new tool-wear sensor evidence (78% of rated life) relative to a prior belief ('tool recently replaced, unlikely worn'), resulting in a corrective action smaller than the updated evidence would justify",
        "affected_reasoning_operation": "Belief updating and proportionality of response magnitude to new evidence at decision point 3",
        "evidence_source": "Tool wear sensor reading and prior stated assumption about tool age",
        "distinctiveness_requirement": "This is the only planned conservatism-bias instance; the eventual full tool change at decision point 4 is a separate, later, adequately-revised decision and must not be coded as a second conservatism instance"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "strength": "moderate"
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Biased_2",
    "domain_id": "IP",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (2 and 3) chosen for mechanism fit: correlation bias fits the root-cause hypothesis-formation decision where two co-varying evidence sources exist; conservatism bias fits the halt/continue decision where new quantitative evidence updates a previously stated prior belief. No bias shares a decision point with another instance of itself, so the same-decision-point differentiation rule was not triggered.",
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
