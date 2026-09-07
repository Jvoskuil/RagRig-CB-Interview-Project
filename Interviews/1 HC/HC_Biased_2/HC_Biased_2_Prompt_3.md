You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a internal case review on decision-making during admissions, and that I can ask follow-up questions as we go.

Participant: Sure, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role on the team during this admission?

Participant: I was the attending on the general medicine service. I had a resident covering with me, and we picked up this patient on hospital day one after she came in for something unrelated and ended up with a new finding on her monitor.

Interviewer: And what was your overall goal for her care during the stay?

Participant: Mainly to get her diagnosis sorted out and make sure we sent her home with a safe, appropriate plan. She was 78, otherwise fairly independent, living with her daughter nearby.

Interviewer: Can you walk me through what happened, from the diagnosis to discharge?

Participant: She came in and the admission ECG showed she was in atrial fibrillation, which nobody had picked up before — persistent, not paroxysmal. That obviously changes the calculus for stroke prevention. Her CHA2DS2-VASc came out to 4, so her annual stroke risk if left untreated is meaningful. Her HAS-BLED was 2, which is moderate, not a red flag. Pharmacy checked and there were no interactions with the DOAC we'd typically use. But she'd had a fall about three weeks before admission — mechanical, tripped on a rug at home, no head strike, no fracture, fully worked up at the time. Still, when I saw "fall" in the history, that gave me pause about starting a blood thinner right away. I told the team we'd hold off and get a formal fall-risk assessment first before committing to anything.

Then on day two, one of the nurses mentioned, sort of in passing, that a patient two rooms down had died the previous month from a major GI bleed while on anticoagulation. Understandably, that got around the unit, and my patient's daughter had heard a version of it too. She was in the room a lot and got increasingly anxious every time anticoagulation came up. Clinically nothing had changed — no bleeding, no neuro symptoms — but I ended up ordering a head CT partly to have something concrete to reassure her with, even though it wasn't really indicated. That pushed our timeline back a day.

By day three the CT was normal, and physical therapy had cleared her fall risk as low with a walker. So on paper the numbers were now clearly in favor of starting treatment. I remember standing at the nurses' station with the resident and just picturing what it would be like if we started her on this drug and then she had a major bleed — the conversation with the daughter, explaining that decision, how that would sit with all of us. It felt like a heavier thing to carry than just not starting it. I told the resident we'd let the outpatient team pick it up after discharge.

Then on day four, right before discharge, she got a small bruise at her IV site — completely unrelated, she wasn't even on anticoagulation yet — but when I saw it, it just reinforced that we'd made the right call waiting. We finalized the discharge summary without a firm start plan, just a note to follow up as an outpatient.

Interviewer: Let's slow down and go through each of those moments. At the first point, right after diagnosis — what stood out to you most?

Participant: Honestly, the fall. Clinically I knew the scores favored treatment, but a recent fall in an older patient just registers as a flag. I didn't want to be the one who started a blood thinner and then she fell again and bled into her head.

Interviewer: What alternatives did you consider there?

Participant: We could have started the DOAC immediately since the scores supported it, or started a lower empirical dose. I chose to wait for a formal PT evaluation instead, even though the fall itself had already been worked up and looked mechanical.

Interviewer: What was the main basis for waiting rather than starting treatment that day?

Participant: I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number.

Interviewer: At the second point, with the daughter's anxiety and the CT — what were you trying to accomplish?

Participant: Mostly to de-escalate the family's fear so we could have a productive conversation. In hindsight, I could have just walked through her individual numbers with the daughter instead of ordering imaging that wasn't clinically indicated. But it felt like having a normal scan in hand would make the conversation easier.

Interviewer: How much time pressure did you feel making that call?

Participant: Some — we were already tight on discharge planning, and adding a CT meant another day. But I felt like skipping that step would leave the family conversation unresolved.

Interviewer: Move to the third point — after the CT came back normal and fall risk was cleared. What was going through your mind there?

Participant: That's the one I keep coming back to. The data at that point was pretty clean — low fall risk, normal imaging, scores favoring treatment. But I remember describing to the resident, almost involuntarily, this scenario of her bleeding on a drug I'd started, and how that would feel for a long time afterward, for the family and for me. It wasn't really about the probability anymore. I decided to leave it for the outpatient team.

Interviewer: What alternatives were on the table then?

Participant: Starting it right there before discharge, starting a lower dose with a firm two-week follow-up, or deferring entirely, which is what I did.

Interviewer: Had you handled a similar case before that shaped this decision?

Participant: Not directly with this patient, but the ward story about the other patient's bleed was fresh, and I think it colored how vividly I imagined the downside here.

Interviewer: At the fourth point, the bruise at discharge — how did that factor in?

Participant: It probably shouldn't have changed anything, since she wasn't even on the medication yet. But seeing a bruise right before we finalized the summary just felt like confirmation that waiting was reasonable. We sent her out with a follow-up appointment that ended up being three weeks out, later than the two-week window we'd wanted.

Interviewer: If the fall-risk assessment had come back before your first decision instead of after, would you have decided differently?

Participant: Probably, yes. If I'd had that clearance up front, I likely would have started treatment on day one instead of waiting.

Interviewer: If the other patient's bleeding event had never come up on the ward, do you think this admission would have gone differently?

Participant: It's hard to say for certain, but I think the family conversation would have been calmer, and maybe I wouldn't have gotten as fixated on the worst-case picture toward the end.

Interviewer: Looking back, what would you tell a colleague facing a similar case?

Participant: I'd say make sure the fall workup happens early, not as an afterthought, and try to separate the family's emotional reaction from the actual numbers in front of you. It's easy to let one vivid story anchor the whole decision, even when the data has already shifted.
}}

Hidden generation specification:
{{"hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Impact Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overestimation of the intensity/duration of imagined future emotional impact of a hypothetical bleeding event, not as a general fear statement."
      },
      {
        "bias": "Omission Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as explicit preference for inaction over action based on differential blame attribution, not as a generic caution statement."
      }
    ],
    "target_bias_names": ["Impact Bias", "Omission Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Impact Bias", "requested_occurrences": 1},
      {"bias": "Omission Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "om_01", "bias": "Omission Bias"},
      {"instance_id": "im_01", "bias": "Impact Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "om_01", "bias": "Omission Bias", "decision_point": 1},
      {"instance_id": "im_01", "bias": "Impact Bias", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "om_01",
        "bias": "Omission Bias",
        "mechanism": "Judging harm from action (prescribing anticoagulant) as more blameworthy than equivalent or greater harm from inaction (withholding), leading to deferral despite risk scores favoring treatment.",
        "affected_reasoning_operation": "Risk-benefit weighting and treatment-initiation choice at diagnosis",
        "evidence_source": "CHA2DS2-VASc/HAS-BLED scores and resident's risk comparison presented at decision point 1",
        "distinctiveness_requirement": "Must be tied to the initial diagnosis-stage decision and framed around act-vs-omission blame, distinct from im_01's forward-looking emotional forecasting at decision point 3."
      },
      {
        "instance_id": "im_01",
        "bias": "Impact Bias",
        "mechanism": "Overestimating the intensity and duration of imagined future emotional distress from a hypothetical bleeding event, causing this forecast to override updated quantitative risk data.",
        "affected_reasoning_operation": "Final pre-discharge treatment decision and prediction of future emotional consequences",
        "evidence_source": "Updated normal CT and fall-risk clarification plus recollection of the ward bleeding death, presented at decision point 3",
        "distinctiveness_requirement": "Must be tied to the discharge-stage decision and framed around vivid imagined future emotional impact, distinct from om_01's initial act-vs-omission blame framing."
      }
    ],
    "intended_strength": [
      {"instance_id": "om_01", "bias": "Omission Bias", "strength": "subtle"},
      {"instance_id": "im_01", "bias": "Impact Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Biased_2",
    "domain_id": "HC",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias assigned to a distinct decision point (Omission Bias at decision point 1, Impact Bias at decision point 3) selected for best mechanism fit and narrative realism; no decision point received more than one instance of any single bias; decision points 2 and 4 held neutral to avoid unintended bias concentration.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []}}

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
