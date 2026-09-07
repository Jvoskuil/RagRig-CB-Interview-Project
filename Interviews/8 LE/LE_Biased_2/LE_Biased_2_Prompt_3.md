You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I just want to confirm—this is a routine case-review interview, we're reconstructing your reasoning on a specific case, and it's fine to speak candidly since this isn't a disciplinary review. Sound good?

Participant: Sure, that's fine. I've done these debriefs before.

Interviewer: Great. Can you tell me a bit about your role and how this case landed on your desk?

Participant: I'm a latent print examiner, been doing casework about nine years. This one came through as a burglary submission—pry bar recovered from a residential break-in, latent lifted off the metal surface, plus a known print card for a suspect already booked. Standard comparison request, but they wanted it fast, ahead of a bail hearing.

Interviewer: Walk me through how the case actually came in—what did you know before you looked at the print itself?

Participant: The detective dropped the evidence off personally, which doesn't always happen. He mentioned, kind of in passing, that the suspect had already confessed and had two prior burglary convictions. I remember thinking, okay, that's helpful context, but my job is still to look at the ridges. I logged it in, noted his comments in the file, and got started. We don't have a strict blind-review setup here—some labs do, we don't—so it's normal for that kind of information to come with the evidence.

Interviewer: Did you consider handling the intake differently, given what he told you?

Participant: I thought about it for a second. I could've asked someone else to look at it fresh, or flagged it to my supervisor since he'd shared outcome information. But honestly, with the turnaround we had, that would've meant a delay we didn't have room for, and it's not like the confession changes what's on the pry bar. I proceeded normally.

Interviewer: Let's reconstruct the timeline. What was the physical state of the latent when you got into the analysis?

Participant: Partial print, fair amount of smudging, and there was a distorted region around the periphery—looked like it picked up texture from the tool grip itself, which throws off the ridge flow. The core area, though, was clean. Ten minutiae in that clear zone, no question about it.

Interviewer: And after you drafted your preliminary read?

Participant: I wrote it up, sent it to verification. Then the verifying examiner came back with a flag on that same peripheral area—didn't see it the way I did. That's when I had to reconcile things before the report went out.

Interviewer: Let's slow down on the comparison itself. When you got to that distorted peripheral region, what were you actually looking at, and how did you land on your read?

Participant: The ten minutiae in the clear zone were enough on their own, honestly—textbook sufficiency. The peripheral area was rougher, ridge flow was broken up by the distortion. I went back and forth on it. But when I lined it up against the known card, the flow direction seemed to pick back up in a way that fit the suspect's print. I remember thinking, given everything else pointing his way—he'd already admitted to it—this piece just confirmed what was already lining up. So I folded it into the individualization call as consistent rather than calling it indeterminate.

Interviewer: What alternatives were on the table at that point?

Participant: I could've treated that region as indeterminate and rested the conclusion purely on the ten clear minutiae—which honestly would've been sufficient by itself. Or I could've called for better imaging before committing either way. Those were both live options.

Interviewer: What would you say tipped you toward reading it as consistent rather than going with one of those?

Participant: The pattern looked plausible to me. I won't pretend the case context wasn't in my head at that point—it's hard to fully compartmentalize once you've heard something like that. But I also want to be clear, the ridge flow genuinely looked continuous to me in that section.

Interviewer: Moving to the verification step—what did you send over, and did you weigh other options?

Participant: I sent the full worksheet with my conclusion attached, along with the images. I could've sent just the images without my determination, let the verifier come in blind. We only had one other qualified examiner available that day, and with the clock running on the bail hearing, I went with the standard route—full packet, conclusion included.

Interviewer: Any hesitation there?

Participant: A little. Blind verification is theoretically cleaner, I know that. But it's not our default practice, and slowing things down to arrange it felt like more friction than the situation called for.

Interviewer: Let's talk about the discrepancy. The verifying examiner flagged that same peripheral region differently than you did. What went through your mind?

Participant: My first reaction was, okay, this is the distorted area, that's exactly the kind of spot where two examiners can read things differently. The ten core minutiae weren't in dispute—she agreed on those. So I looked at the discrepancy again and thought about what could explain it without it actually being a mismatch. Tool-surface texture causing pressure variance in that specific region made sense to me, and it's a documented thing that happens with textured surfaces like pry bars. I wrote that into the file as the explanation and kept the individualization conclusion standing.

Interviewer: Did you consider downgrading the conclusion instead?

Participant: I thought about calling it inconclusive until we could get a better lift or additional processing. That was on the table. But the ten minutiae were solid regardless, the deadline was same-day, and the distortion explanation accounted for what she was seeing without requiring me to throw out the whole determination.

Interviewer: What else, besides distortion, could have explained what she saw?

Participant: Could've genuinely been a non-matching area—maybe that region just doesn't belong to the same source. I didn't rule that out entirely, but it felt less likely to me once I had the distortion explanation in hand.

Interviewer: How confident were you in that peripheral read, if you had to put a number on it?

Participant: Maybe a six or seven out of ten on its own. But paired with the ten minutiae, I felt solid on the overall call.

Interviewer: Has this kind of distortion situation come up before in your casework?

Participant: Yeah, textured tool surfaces are a known headache. Usually if the core detail's strong, we don't let a rough edge area derail things.

Interviewer: Last few questions. If the detective had never mentioned the confession or the priors, do you think your read of that ambiguous region would've gone differently?

Participant: Possibly. I'd like to think I'd have called it the same way, but I can't say for certain the extra confidence wasn't doing some work there.

Interviewer: If the verifier's discrepancy had come up before you drafted your conclusion instead of after, would things have gone differently?

Participant: Maybe. Seeing it flagged first might've made me treat that region as indeterminate from the start rather than reconciling it after the fact.

Interviewer: What would you change if you had this case again with no deadline?

Participant: I'd probably request a fresh lift or enhanced imaging on that peripheral area before committing to anything, and maybe ask for a blind second look. Not because I think the outcome was wrong, but because that region deserved more room than we gave it that day.

Interviewer: Appreciate the candor. That's everything I need.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Contextual Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as case-outcome information (confession/priors) influencing resolution of a genuinely ambiguous print feature during comparison, not as a general statement of belief in guilt."
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a post-hoc explanation constructed to preserve a pre-existing conclusion after disconfirming verifier feedback, not as a routine technical judgment offered independent of the prior conclusion."
      }
    ],
    "target_bias_names": [
      "Contextual Bias",
      "Coherence-based reasoning or Rationalisation"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Contextual Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias"
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "decision_point": 2
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "mechanism": "Extraneous confession/prior-record information received pre-analysis shifts interpretation of an ambiguous peripheral ridge region toward a match-consistent reading, absent independent print-based justification for that specific resolution.",
        "affected_reasoning_operation": "Evaluation/interpretation of ambiguous perceptual evidence during Comparison/Evaluation",
        "evidence_source": "Detective's unsolicited case-outcome remarks retained during analysis of the distorted peripheral ridge area",
        "distinctiveness_requirement": "Distinct from coh_01: occurs at the analysis/comparison stage on ambiguous perceptual data, before any conclusion has been challenged, and is driven by pre-analysis extraneous information rather than by defending an already-stated conclusion against disconfirming feedback."
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "After the verifying examiner flags a discrepancy, the examiner generates a distortion-based explanation that renders the discrepancy compatible with the already-fixed individualization conclusion, rather than treating it as evidence warranting downgrade.",
        "affected_reasoning_operation": "Evaluation of disconfirming evidence and belief updating during final report reconciliation",
        "evidence_source": "Verifying examiner's independent discrepancy flag on the peripheral ridge region, evaluated against the pre-existing draft conclusion",
        "distinctiveness_requirement": "Distinct from ctx_01: occurs post-conclusion, triggered by external disconfirming feedback from a second examiner, and operates through explanatory construction to preserve coherence with a prior commitment rather than through initial ambiguous-evidence interpretation."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "strength": "moderate"
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence versus absence of unsolicited case-outcome information at intake",
      "original_state": "Detective volunteers confession and prior-record information before analysis begins",
      "changed_state": "Case submitted blind, with no outcome information disclosed to the examiner",
      "variables_to_hold_constant": [
        "Print quality and distortion pattern",
        "Number and clarity of minutiae",
        "Deadline pressure",
        "Verification routing and staffing availability",
        "Verifier's discrepancy finding at phase 4"
      ]
    },
    "scenario_id": "LE_Biased_2",
    "domain_id": "LE",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias, each assigned to the decision point offering the best mechanism fit and narrative realism: Contextual Bias at the initial ambiguous-comparison decision (phase 2), where pre-analysis case information most plausibly biases perceptual interpretation; Coherence-based reasoning/Rationalisation at the final report-reconciliation decision (phase 4), where disconfirming verifier feedback most plausibly triggers a conclusion-preserving explanation. Decision points were kept distinct (no shared decision point) to maximize independent identifiability and avoid overlap between mechanisms.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Print quality and distortion pattern",
      "Number and clarity of minutiae",
      "Deadline pressure",
      "Staffing and verification availability",
      "Verifier's discrepancy finding"
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
