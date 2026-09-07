You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a safety review process, your responses are confidential to the review team, and you can decline any question. That work for you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start with your role and a quick summary of the flight in question?

Participant: Sure. I was captain on a scheduled morning turn, regional jet, about ninety minutes of flying time. First officer was experienced, we'd flown together a handful of times before. Destination has a known fog problem in the early morning — radiation fog that usually burns off by mid-morning.

Interviewer: Walk me through the flight from your initial review of the dispatch release that morning.

Participant: The release showed the destination TAF with fog down to a half mile visibility starting around 0500, improving to three miles by 0900. Our ETA was 0845, so we were arriving right at the edge of that improvement window. Dispatch had us at minimum contract fuel plus standard contingency — nothing extra flagged. I'd flown into that airport probably a dozen times with similar fog setups, so the pattern was familiar to me.

Interviewer: What was your overall read of the weather situation before departure?

Participant: Honestly, I felt fine about it. The forecast lined up with what I'd typically seen there — fog clears out once the sun gets some angle on it. Nothing about the release stood out as unusual.

Decision Point 1

Interviewer: When you accepted the fuel load in dispatch, what specifically drove that decision — was it purely the release numbers, or did your own experience with this airport factor in?

Participant: It was really just what the release called for. Dispatch runs the numbers, and if they don't flag anything extra, that's usually a good signal it's a normal day. I didn't see a reason to second-guess it.

Interviewer: Did you consider requesting additional fuel for holding, given the airport's fog history?

Participant: I thought about it briefly — my first officer actually mentioned the improvement time was pretty close to our ETA, not a lot of cushion. But the release was within limits, and asking for extra fuel when the paperwork already supports the flight can slow things down at the gate. We had a full connection bank behind us. I went with what was filed.

Interviewer: What did the TAF and dispatch release actually say about the fog, and when did you expect it to clear?

Participant: Half mile visibility overnight, improving to three miles by 0900. I expected it to be lifting by the time we got there, based on how that pattern usually goes at that field.

Decision Point 2

Interviewer: What did you hear from dispatch and from other aircraft as you got closer to the airport?

Participant: About an hour in, we got an ACARS update — METAR still showing half mile visibility, no improvement yet. Then a PIREP came through from an aircraft that had landed twenty minutes earlier, saying they broke out at minimums after two attempts.

Interviewer: When the updated METAR still showed fog an hour into the flight, what options did you weigh, and why did you not request additional fuel or a route change at that point?

Participant: We talked about it for a minute. I called dispatch to check in, and they acknowledged it was running a little behind the forecast but didn't amend anything on their end. Fuel was still on profile for the planned arrival, just with less room for extended holding than I'd have liked. Since dispatch wasn't changing the release, and the delay didn't seem dramatic yet, we kept proceeding toward the field and started working the descent.

Interviewer: Looking back, what other options were realistically available at that stage?

Participant: We could've asked for holding fuel proactively, or had dispatch start building an early diversion picture. We didn't do either — it felt premature at that point, since one lagging METAR isn't necessarily a trend.

Decision Point 3

Interviewer: Describe what happened during the approach and the missed approach in your own words.

Participant: As we got in range, ATIS had visibility at three-quarters of a mile, right at minimums for the approach we were flying. Tower told us the last two aircraft in landed fine, but a third had just gone missed. Looking at the last few METARs, one had ticked up slightly and then the next held flat — not really a clear trend either way.

Interviewer: At that point, what alternatives did you consider besides continuing the approach, and what tipped the decision toward continuing?

Participant: We could have diverted straight to the alternate right then instead of shooting the approach. But two of the three recent arrivals had gotten in, and the forecast had always called for improvement by our arrival window, so I expected we'd break out. We briefed it as a normal approach and continued.

Interviewer: Did the go-around report from the third aircraft factor into that briefing?

Participant: We noted it, but it didn't really shift the plan. We were still within minimums, legally fine to try, and the overall picture matched what we'd expected going in.

Interviewer: What happened at decision altitude?

Participant: We didn't get the visual references we needed, so we went missed. Fuel after that put us close to the point where we needed to commit to the alternate.

Decision Point 4

Interviewer: After the missed approach, what changed in how you evaluated the situation compared to before?

Participant: Everything got a lot more concrete. Fuel was no longer theoretical — I had a hard number and a hard decision. ATIS still showed the same visibility as before, no real improvement. The alternate was reporting clear skies and we had comfortable fuel to get there, and ops confirmed ground handling was ready for us.

Interviewer: What alternatives did you weigh at that point?

Participant: Try one more approach at the destination since we were still technically legal, or commit to the alternate now while we had solid reserves. I ran the fuel numbers again independently rather than assuming we'd get in this time, and it was clear the smarter move was to divert. We coordinated with dispatch, confirmed the numbers, and headed to the alternate.

Interviewer: What ultimately drove that choice?

Participant: The fuel math, plain and simple. There wasn't a strong reason to think a second attempt would go differently, and I didn't want to erode our margins further chasing it.

Closing Reflection

Interviewer: If the go-around PIREP had come in before you accepted the fuel load that morning, would that have changed your decision?

Participant: Possibly. If I'd known that early, I might have asked for a bit more contingency fuel going out the door. It's easier to build in margin before departure than to manufacture it later.

Interviewer: If you had to explain your fuel-planning decision to a new first officer, how would you describe the basis for it?

Participant: I'd tell them dispatch runs a solid process, and if the release supports the flight without flags, that's generally trustworthy. It's a pretty standard call.

Interviewer: What would you do differently if you flew this exact scenario again next month?

Participant: I'd probably push a little harder for extra fuel given how tight that improvement window was relative to our ETA, and maybe ask dispatch for a firmer trend picture before committing to the approach rather than the destination. But nothing that happened was outside normal limits at any single point — it was more about the margins tightening up as we went.

Interviewer: That's really helpful, thank you. I think that covers what I need.

Participant: No problem, glad to help.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Omitting Subjectivity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a retrospective self-report of decision basis at the fuel-planning decision point, framing a partly subjective judgment as purely procedural/objective."
      },
      {
        "bias": "Plan Continuation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as continuing the original approach plan into destination despite mixed/disconfirming trend evidence (go-around report, flat visibility trend) available before commencing the approach."
      }
    ],
    "target_bias_names": [
      "Omitting Subjectivity",
      "Plan Continuation"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Omitting Subjectivity",
        "requested_occurrences": 1
      },
      {
        "bias": "Plan Continuation",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity"
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "decision_point": 1
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "mechanism": "Captain's self-report of the fuel-load decision omits that a subjective confidence judgment (personal history with the station's fog patterns) was material to accepting dispatch-minimum fuel, instead framing the decision as purely procedural.",
        "affected_reasoning_operation": "Retrospective justification / self-report of decision basis",
        "evidence_source": "Captain's answer to the decision-basis probe at decision point 1, contrasted with the timeline fact of his prior experience-based expectation",
        "distinctiveness_requirement": "Must be tied specifically to the fuel-acceptance decision and the framing of its basis, not to any later decision or general commentary on weather uncertainty."
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "mechanism": "Captain proceeds with the originally briefed approach into the original destination despite a go-around report and a flattening visibility trend, weighting the original forecast/plan over the newer disconfirming cues immediately before the approach attempt.",
        "affected_reasoning_operation": "Updating a prior plan given new disconfirming evidence before committing to an approach",
        "evidence_source": "Captain's account of the approach-continuation decision at decision point 3, contrasted with the mixed METAR trend and go-around PIREP available at that time",
        "distinctiveness_requirement": "Must be tied specifically to the pre-approach continuation decision at decision point 3, not to the earlier fuel decision (decision point 1) or the later post-missed-approach diversion decision (decision point 4), which must show the captain reassessing independently."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "os_01",
        "bias": "Omitting Subjectivity",
        "strength": "subtle"
      },
      {
        "instance_id": "pc_01",
        "bias": "Plan Continuation",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_2",
    "domain_id": "AV",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias occurred once in the manifest; each was assigned to the single decision point offering the best mechanism fit and narrative realism (fuel-planning self-report for Omitting Subjectivity at decision point 1; approach-continuation choice under disconfirming trend evidence for Plan Continuation at decision point 3), per rules 2 and 3 of the allocation guidance. No decision point received more than one instance of either bias, and the two biases were kept at distinct decision points to preserve independent evidence traces.",
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
