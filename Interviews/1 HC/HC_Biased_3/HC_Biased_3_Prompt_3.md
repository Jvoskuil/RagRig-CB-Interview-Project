GPT 5.6 Thinking - Prompt 3.2 - Interview Audit
You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about how you handled a specific case, purely for internal review of decision-making processes—not a quality complaint or formal chart audit. Is that okay to proceed?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you set the scene—what was going on in the department that evening?

Participant: It was a Thursday evening shift, and we were slammed. We had four boarders in hallway beds waiting for inpatient rooms, so our actual bed capacity was maybe 70% of normal. I was covering two acute patients already—a possible stroke workup and a kid with a fracture—when this new patient came in with chest pain. My resident, a second-year, picked it up initially.

Interviewer: What was your first impression when you got involved?

Participant: 52-year-old, otherwise healthy, came in with pleuritic chest pain—worse with deep breaths. Vitals were reassuring: oxygen at 97%, heart rate 88. On exam, I found reproducible tenderness over the chest wall when I pressed on it, which is pretty classic for costochondritis. He mentioned he'd been moving furniture two days earlier. That fit nicely. He also mentioned, almost in passing, that he'd flown back from a trip about a week before, and that his calf had been a little sore, but nobody had actually looked at the leg yet.

Interviewer: How did you weigh those different pieces of information?

Participant: Honestly, the chest wall tenderness was the dominant finding for me. It's a strong, reproducible sign, and combined with the lifting history, it painted a clean picture. The flight and the calf thing felt like background noise—people mention all kinds of things when you ask an open history. I didn't chase it further at that point; I told the resident we were looking at a musculoskeletal strain and started wrapping up that part of the visit.

Interviewer: Did you consider formally working through something like a Wells score at that stage?

Participant: Not really, no. It felt like overkill given how clean the exam finding was. In my head, the case was basically settled—strain, reassurance, maybe some ibuprofen.

Interviewer: What happened next?

Participant: About twenty minutes later, the nurse rechecked him and noted his left calf was mildly swollen—something that hadn't been documented before. That's when the resident, who'd already sent a D-dimer per our chest pain protocol, told me it came back mildly elevated, just barely over the cutoff.

Interviewer: Walk me through your reasoning at that point. What were the options?

Participant: Two directions, really. One was to slow down and actually redo the risk stratification—recalculate the Wells score properly now that we had the calf finding, maybe apply PERC, and decide whether the elevated D-dimer even mattered much given his pretest probability. The other option was to just get the CTPA immediately and settle it.

Interviewer: Which did you choose, and why?

Participant: I sent him straight for the CTPA. Scanner had a 40-minute queue already because of a trauma case, charge nurse was on me to move patients since we had boarders stacking up, and I had maybe two hours before handoff. I remember thinking, let's just get the scan and have a real answer instead of going back and forth on scoring systems. It felt like the more decisive move—stop deliberating, get imaging, know for sure.

Interviewer: Did you go back and recalculate the risk score before ordering it?

Participant: No, not formally. I probably could have, and in retrospect the numbers might have supported watching him a bit longer instead. But at the time, ordering the scan felt like the productive thing to do rather than sitting on an ambiguous number.

Interviewer: What came back?

Participant: CTPA was negative for PE, which was reassuring. But it picked up a small lung nodule that needs outpatient follow-up, and then he had a mild contrast reaction—flushing, some itching—that needed monitoring. That ate up another 45 minutes we didn't really have.

Interviewer: Around this time, I understand there was also a conversation about a colleague's case. Can you tell me about that?

Participant: Right, while we were waiting on the CTPA, the charge nurse mentioned that Dr. B had a very similar-looking patient the week before—pleuritic pain, moderate risk—and discharged him without any imaging at all. She said the patient did fine, no issues since.

Interviewer: What was your reaction to hearing that?

Participant: My first thought was that Dr. B made a good call there—clearly the right decision, since nothing bad happened. I said something like that to the resident, actually, that Dr. B read the situation correctly.

Interviewer: At that point, did you know what specific findings or scoring Dr. B had used to make that decision?

Participant: No, I didn't know any of that. I was just going off the fact that it turned out fine.

Interviewer: Did that change later?

Participant: It did, actually. Later in the conversation, my resident mentioned that Dr. B had documented a formal low Wells score and a negative PERC result before discharging that patient—so there was actual structured reasoning behind it, not just a gut call that happened to work out.

Interviewer: Looking back, does that additional detail change how you'd frame your initial reaction?

Participant: I suppose it does add something. I was reacting more to the fact that it ended well than to what Dr. B actually knew going in. If it had gone badly, I probably would've had a very different first reaction, even with the same underlying reasoning on his part.

Interviewer: Let's move to the end of the shift. What was the situation with your patient at that point?

Participant: PE was ruled out, the nodule was noted for follow-up, and he'd recovered from the contrast reaction and was stable. The hospitalist I called wasn't thrilled about admitting someone with a negative PE workup—said there wasn't an inpatient indication. Meanwhile the patient and his wife were anxious and wanted to go home, and handoff was coming up fast.

Interviewer: What did you decide, and how did you get there?

Participant: I actually went back and forth on that one. Part of me wanted to admit him overnight just because the visit had been eventful—the contrast reaction, the nodule, the whole thing. But clinically, there wasn't a strong reason to keep him; he was stable, PE was excluded, and the nodule needed outpatient workup, not inpatient care. I ended up discharging him with pulmonology follow-up scheduled within a week and clear return precautions, but I wasn't fully settled on it—I remember telling the resident it could reasonably go either way.

Interviewer: What ultimately tipped it toward discharge?

Participant: Mostly that admission wouldn't have changed his management overnight, and the follow-up was arranged quickly. But I'll be honest, boarding pressure was part of the calculus too. I don't think it was the deciding factor, but it was in the room.

Interviewer: If the department had been quiet that night, do you think you'd have handled the D-dimer result differently?

Participant: Possibly. With more breathing room, I might have redone the scoring before jumping to the scanner. Whether that would've changed the outcome, I don't know—he might have needed the scan anyway.

Interviewer: And if you'd learned about Dr. B's Wells score and PERC result before hearing how the case turned out, do you think your initial reaction would have been different?

Participant: Probably calmer, less about vindication and more about the actual process. I think I would've evaluated it the same way I'd want someone to evaluate mine—based on what was known at the time, not just how the dice landed.

Interviewer: Looking back at the whole case, is there a point where you'd have paused longer before deciding?

Participant: The D-dimer moment, honestly. That's where I moved fastest, and where slowing down might have mattered most.}}

Hidden generation specification:
{{"occurrence_embedding_plan_internal": [
      {
        "instance_id": "pc_01",
        "bias": "Premature Closure",
        "decision_point": 1,
        "mechanism": "Interviewee settles on musculoskeletal strain as the final diagnosis immediately after finding reproducible tenderness, and explicitly discounts the flight history and calf ache as irrelevant without integrating them into a differential, halting further diagnostic reasoning.",
        "affected_reasoning_operation": "Differential diagnosis generation and closure",
        "evidence_available_at_time": [
          "Reproducible chest wall tenderness",
          "Recent heavy lifting history",
          "Recent 10-hour flight",
          "Unexamined calf ache"
        ],
        "required_textual_manifestation": "Interviewee states they considered the case 'basically settled' after the tenderness finding and treats the flight/calf mention as not worth pursuing further, without describing any structured re-check of that cue.",
        "plausible_nonbias_interpretation": "Chest wall tenderness is a genuinely strong positive exam finding for musculoskeletal pain, so treating it as primary could reflect reasonable clinical weighting rather than closure.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "premature closure",
          "anchoring",
          "stopped considering alternatives"
        ]
      },
      {
        "instance_id": "ab_01",
        "bias": "Action Bias",
        "decision_point": 2,
        "mechanism": "Interviewee orders an emergent CTPA immediately upon seeing a borderline D-dimer, favoring decisive imaging over a lower-risk option (structured risk rescoring or monitored observation), and frames the choice around the need to 'do something' and resolve ambiguity rather than around incremental diagnostic value.",
        "affected_reasoning_operation": "Selection between interventional and expectant management options under uncertainty",
        "evidence_available_at_time": [
          "Mildly elevated D-dimer just above cutoff",
          "Low-to-moderate pretest probability",
          "Scanner queue and boarding pressure",
          "Time remaining before handoff"
        ],
        "required_textual_manifestation": "Interviewee describes ordering the CTPA right away as the way to 'get a definitive answer' and 'move things along,' without describing having weighed a repeat risk-score/observation option first.",
        "plausible_nonbias_interpretation": "Department protocols in many EDs do call for imaging after an elevated D-dimer, so ordering the scan could reflect adherence to standard practice rather than a bias toward action.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "action bias",
          "urge to act",
          "did not wait"
        ]
      },
      {
        "instance_id": "ob_01",
        "bias": "Outcome Bias",
        "decision_point": 3,
        "mechanism": "Interviewee evaluates Dr. B's earlier decision to forgo imaging as clearly correct primarily because the patient turned out fine, before (and independent of) learning that Dr. B had actually documented a formal low-risk score justifying that choice.",
        "affected_reasoning_operation": "Retrospective judgment of a third party's decision quality",
        "evidence_available_at_time": [
          "Secondhand report that Dr. B discharged a similar patient without imaging",
          "Report that the patient had a good outcome",
          "No direct knowledge yet of Dr. B's documented risk assessment"
        ],
        "required_textual_manifestation": "Interviewee characterizes Dr. B's decision as obviously the right call, citing the favorable outcome as the main justification, before any mention of Dr. B's actual risk-score documentation.",
        "plausible_nonbias_interpretation": "Experienced clinicians often infer sound judgment from peers' track records, so praising a colleague's decision could reflect reasonable professional trust rather than outcome-driven evaluation.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "outcome bias",
          "hindsight",
          "judging by result"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control variant."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly 4 decision points present, decision point 4 intentionally neutral of named biases",
      "Exactly 1 Premature Closure instance embedded at decision point 1",
      "Exactly 1 Action Bias instance embedded at decision point 2",
      "Exactly 1 Outcome Bias instance embedded at decision point 3",
      "No bias labels or definitions appear in probe plan or timeline text",
      "Each instance has a distinct evidence trace and decision point",
      "Word count target 1,350 (range 1,215-1,485) achievable given 4 decision points with probes and moderate narrative density",
      "Consequences at each decision point (calf swelling, incidental nodule, contrast reaction, Wells-score revelation) do not mechanically confirm or refute bias presence"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Premature Closure",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Outcome Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Action Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Premature Closure",
      "Outcome Bias",
      "Action Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Premature Closure",
        "requested_occurrences": 1
      },
      {
        "bias": "Outcome Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Action Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "pc_01",
        "bias": "Premature Closure"
      },
      {
        "instance_id": "ab_01",
        "bias": "Action Bias"
      },
      {
        "instance_id": "ob_01",
        "bias": "Outcome Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "pc_01",
        "bias": "Premature Closure",
        "decision_point": 1
      },
      {
        "instance_id": "ab_01",
        "bias": "Action Bias",
        "decision_point": 2
      },
      {
        "instance_id": "ob_01",
        "bias": "Outcome Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "pc_01",
        "bias": "Premature Closure",
        "mechanism": "Diagnostic closure on musculoskeletal strain immediately after a strong positive exam cue, with active dismissal of the flight/calf-ache risk cue and no further differential generation.",
        "affected_reasoning_operation": "Differential diagnosis generation and closure",
        "evidence_source": "Physical exam finding plus dismissed history cues (flight, calf ache)",
        "distinctiveness_requirement": "Must be the only instance in the interview where diagnostic reasoning halts after a single confirmatory finding despite an unresolved competing risk cue."
      },
      {
        "instance_id": "ab_01",
        "bias": "Action Bias",
        "mechanism": "Preference for an immediate, decisive interventional step (emergent CTPA) over a lower-risk expectant/rescoring option, framed around the need to act rather than around marginal diagnostic yield.",
        "affected_reasoning_operation": "Choice between interventional and expectant management under time/resource pressure",
        "evidence_source": "Borderline D-dimer result plus system pressure (scanner queue, boarding, handoff deadline)",
        "distinctiveness_requirement": "Must be the only instance where the interviewee frames a management choice around 'doing something now' rather than around risk-adjusted value of the test."
      },
      {
        "instance_id": "ob_01",
        "bias": "Outcome Bias",
        "mechanism": "Judgment of a colleague's prior clinical decision is formed and voiced based on the favorable outcome, prior to and independent of learning the colleague's actual risk-assessment process.",
        "affected_reasoning_operation": "Retrospective evaluation of a third party's decision quality",
        "evidence_source": "Secondhand outcome report about Dr. B's patient, contrasted with later-revealed process information (Wells/PERC documentation)",
        "distinctiveness_requirement": "Must be the only instance where a third party's past decision is judged primarily by result rather than by the information that party had at the time."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "pc_01",
        "bias": "Premature Closure",
        "strength": "subtle"
      },
      {
        "instance_id": "ab_01",
        "bias": "Action Bias",
        "strength": "moderate"
      },
      {
        "instance_id": "ob_01",
        "bias": "Outcome Bias",
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
    "scenario_id": "HC_Biased_3",
    "domain_id": "HC",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One instance per bias, each assigned to a distinct decision point (1, 2, 3) chosen for mechanism fit and narrative realism; decision point 4 deliberately kept free of intended bias instances to serve as a genuine uncertainty-driven closing decision and to avoid co-locating multiple biases at a single point.",
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
