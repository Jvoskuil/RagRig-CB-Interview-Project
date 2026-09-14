You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time. Just to confirm, this conversation is voluntary and for internal review of decision-making, not a formal chart audit. Okay to proceed?

Participant: Yeah, that's fine.

Interviewer: Can you set the scene—what was going on in the department that evening?

Participant: It was a Thursday night, pretty rough. We had four boarders in hallway beds waiting on inpatient rooms, so our effective capacity was well below normal. I was covering two other acute patients—a possible stroke and a kid with a fracture—when this chest pain patient came in. My second-year resident saw him first and then brought me in.

Interviewer: What was your first impression once you got involved?

Participant: 52-year-old man, generally healthy, pleuritic chest pain that was worse with deep breaths. Vitals were reassuring, sat 97%, heart rate 88. On exam I found reproducible tenderness over the chest wall, which does suggest something musculoskeletal, and he told me he'd been moving furniture two days earlier. That's a coherent story by itself. But he also mentioned, almost in passing, a 10-hour flight home from a trip about a week before, and a mild calf ache nobody had actually examined yet.

Interviewer: How did you weigh those pieces against each other?

Participant: The chest wall tenderness was a legitimate finding, so I wasn't going to dismiss it, but the flight and the calf comment gave me pause. Immobility plus a leg symptom is exactly the combination you don't want to explain away just because there's a tidier story sitting right in front of you. So I told the resident we'd hold off on a final impression until we actually looked at the leg directly.

Interviewer: What happened after that?

Participant: About twenty minutes later, the nurse rechecked him and confirmed mild swelling in the left calf, matching what he'd described. Around the same time, the resident came back with the D-dimer result—it had already been sent per our chest pain protocol—and it was mildly elevated, just above the assay cutoff.

Interviewer: Walk me through your thinking once you had that result.

Participant: A borderline D-dimer doesn't mean much on its own; it depends on the pretest probability going in. With the calf swelling now confirmed, I sat with the resident and we recalculated the Wells score properly, incorporating the leg finding this time rather than just the original picture. That pushed him into a range where imaging felt genuinely warranted, not just a reaction to one number.

Interviewer: How much did the scanner queue or bed pressure factor into that?

Participant: It was there in the background—40-minute queue behind trauma, charge nurse pushing to free up beds—but I didn't let that skip the reassessment step. I wanted the score redone first. Once that supported imaging, the practical pressure just meant asking radiology to prioritize him within their existing queue.

Interviewer: Tell me about the conversation regarding Dr. B's earlier patient.

Participant: While we were waiting on the CTPA, the charge nurse mentioned Dr. B had a similar-looking patient the week before—same kind of pleuritic pain—and discharged him without imaging. She said the patient did fine afterward.

Interviewer: What was your reaction to hearing that?

Participant: Honestly, my first thought was that I didn't know enough to judge it either way. Did he do a formal Wells score? Was it PERC-negative? A good outcome doesn't tell you whether the underlying reasoning was sound—some borderline calls work out fine by chance. I asked the resident to pull the chart before forming any real opinion.

Interviewer: What did you find?

Participant: Dr. B had documented a formal low-risk Wells score and a negative PERC before discharging that patient. So there was actual structure behind the decision, not just a guess that happened to land well.

Interviewer: Did that change your view?

Participant: It confirmed what I suspected—that it was a reasonable, defensible call given what he knew. If it had gone badly instead, with the same documented workup, I'd still call it reasonable. The outcome doesn't really tell you much about the quality of the reasoning behind it.

Interviewer: Let's get to the end of your shift. What was the situation with your patient by then?

Participant: PE was ruled out on the CTPA, though it picked up a small lung nodule needing outpatient follow-up, and he'd had a mild contrast reaction that took about 45 minutes to settle. By the time all that resolved, he was stable, but the visit had gotten more complicated than expected. The hospitalist I called wasn't eager to admit someone with a negative PE workup, and the patient and his wife were anxious to leave. Handoff was closing in.

Interviewer: How did you decide between admitting and discharging?

Participant: I genuinely went back and forth. Part of the pull toward admission was that the visit had been eventful—the reaction, the nodule—but eventful isn't the same as unsafe. Clinically, admission wouldn't have changed anything overnight; the nodule needed outpatient pulmonology, not inpatient care. I discharged him with a follow-up scheduled within the week and clear return precautions, but I told the resident honestly it could have gone either way.

Interviewer: What tipped it toward discharge in the end?

Participant: Mostly that nothing about his overnight risk profile had changed, and we had a real follow-up plan arranged quickly. The boarding pressure was present in the background, but I don't think it drove the decision. If anything, I spent more time on that disposition than I'd have liked given how busy we were.

Interviewer: What information, if it had been available earlier, would have changed how you handled the D-dimer result?

Participant: If the calf swelling had been documented at triage instead of found later, I probably would have gone straight to a formal risk score without the intermediate step of waiting on the nurse's recheck. It would have saved some time, though I don't think it would have changed the ultimate decision to image him.

Interviewer: If the department had been quiet that night, would you have handled things differently?

Participant: Not fundamentally—I still would have wanted the leg exam and the recalculated score before deciding on imaging. Busy or not, that step felt necessary once the calf came into the picture.

Interviewer: And if you'd learned about Dr. B's Wells score at the same time as the outcome, rather than afterward, would your reaction have been different?

Participant: No, I think I'd have asked the same question regardless of order—what did he actually know when he made the call. The outcome was almost beside the point for me.

Interviewer: Looking back, is there a moment you'd have handled differently?

Participant: Maybe I could have pushed radiology harder given how backed up we were. But on the clinical reasoning itself, I wouldn't change much. The disposition at the end is probably where I sat longest and still feel least certain—it was a genuinely close call, not an obvious one.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HC_Vocab_Control_3",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Emergency Medicine Attending Physician (community hospital, ~8 years post-residency experience)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Overnight Chest Pain Disposition (Vocabulary-Matched Control)",
    "scenario_summary_internal": "An ED attending physician manages a 52-year-old patient with pleuritic chest pain during a boarded, high-volume evening shift, mirroring the vocabulary, actors, constraints, and decision structure of the paired biased scenario. In this version, the attending integrates the flight/calf-ache cue into a broadened differential rather than closing on musculoskeletal strain alone, reassesses risk formally before ordering imaging, evaluates a colleague's earlier decision by the information that colleague actually had, and reaches a genuinely uncertain final disposition. No intended bias instances are embedded.",
    "occupational_realism": {
      "objective": "Correctly diagnose and safely disposition a patient with atypical chest pain while managing ED overcrowding and competing patient demands during a single evening shift.",
      "setting": "Emergency department of a mid-sized community hospital; evening shift with boarding patients, one CT scanner shared across the department, a covering resident, and a charge nurse coordinating flow.",
      "constraints": [
        "ED is at capacity with admitted patients boarding in hallway beds",
        "Single CT scanner shared with trauma and stroke protocols",
        "Attending is covering two acute patients simultaneously",
        "Family at bedside pressing for a rapid answer",
        "End-of-shift handoff deadline in two hours"
      ],
      "stakeholders": [
        "52-year-old patient with pleuritic chest pain",
        "Emergency medicine attending physician (interviewee)",
        "Second-year emergency medicine resident",
        "Charge nurse",
        "Radiology technologist",
        "Dr. B, a colleague from the prior week's shift",
        "On-call hospitalist"
      ],
      "technical_terms_to_use": [
        "pleuritic chest pain",
        "Wells score",
        "PERC rule",
        "D-dimer",
        "pretest probability",
        "CT pulmonary angiography (CTPA)",
        "costochondritis",
        "disposition",
        "hospitalist admission",
        "contrast reaction"
      ],
      "technical_terms_to_avoid": [
        "premature closure",
        "action bias",
        "outcome bias",
        "anchoring",
        "cognitive bias",
        "heuristic",
        "confirmation bias",
        "hindsight bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Reproducible chest wall tenderness on palpation",
          "History of moving furniture two days prior",
          "Mild pleuritic pain, no leg swelling noted on brief inspection",
          "O2 saturation 97%, heart rate 88",
          "Patient mentions a 10-hour flight home from a trip one week earlier",
          "Patient offhandedly mentions a mild calf ache, not formally examined"
        ],
        "new_information_after_decision": [
          "Nurse rechecks the patient later and confirms mild left calf swelling, consistent with the earlier verbal complaint"
        ],
        "alternatives": [
          "Settle on musculoskeletal strain as the working diagnosis based on the tenderness finding alone",
          "Fold the flight history and calf ache into an expanded differential and examine the leg directly before committing to a single explanation"
        ],
        "intended_action": "Attending notes the tenderness is suggestive of a musculoskeletal cause but flags the flight and calf complaint as worth a direct leg exam, and defers a final impression until that exam is done."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Resident has already drawn a D-dimer per department protocol",
          "D-dimer returns mildly elevated, just above the assay cutoff",
          "Patient's calculated pretest probability remains low-to-moderate given exam findings",
          "CT scanner has a 40-minute queue with trauma priority",
          "Charge nurse is pushing to clear beds for boarding admissions",
          "Two hours remain before shift handoff"
        ],
        "new_information_after_decision": [
          "CTPA is negative for pulmonary embolism",
          "Scan incidentally reveals a small indeterminate lung nodule requiring outpatient follow-up",
          "Patient has a mild contrast reaction requiring monitoring, delaying disposition by 45 minutes"
        ],
        "alternatives": [
          "Order an emergent CTPA immediately given the elevated D-dimer",
          "Recalculate the Wells/PERC risk formally with the new calf finding before deciding whether imaging changes management"
        ],
        "intended_action": "Attending redoes the risk score with the resident, factoring in the calf swelling, and concludes the updated pretest probability still warrants imaging, so orders the CTPA on that basis rather than skipping the reassessment."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Charge nurse mentions that Dr. B discharged a similarly presenting patient the prior week without ordering imaging",
          "Attending is told that patient later did well with no adverse event",
          "Attending has no direct knowledge yet of what specific findings, risk scores, or conversation Dr. B had with that patient at the time",
          "Attending is mid-shift, multitasking on the current CTPA workup"
        ],
        "new_information_after_decision": [
          "Resident confirms Dr. B had documented a formal low-risk Wells score and PERC-negative status before discharging that patient"
        ],
        "alternatives": [
          "Withhold judgment on Dr. B's decision until learning what information and risk stratification Dr. B actually used",
          "Judge Dr. B's decision primarily by how the case turned out"
        ],
        "intended_action": "Attending says it's hard to know if Dr. B's call was sound without knowing what workup was documented, and asks the resident to check the chart before forming an opinion."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "CTPA negative for PE",
          "Incidental lung nodule needs outpatient follow-up",
          "Patient recovered from mild contrast reaction, currently stable",
          "Hospitalist is reachable but reluctant to admit a patient with a negative PE workup",
          "Shift handoff is imminent",
          "Patient and family are anxious and requesting to go home"
        ],
        "new_information_after_decision": [
          "Patient is scheduled for outpatient pulmonology follow-up within one week",
          "No further acute events during the remainder of the visit"
        ],
        "alternatives": [
          "Admit briefly for observation given the eventful workup and contrast reaction",
          "Discharge home with structured follow-up instructions and safety-netting"
        ],
        "intended_action": "Attending weighs the residual clinical uncertainty, boarding pressure, and follow-up feasibility, and reaches a disposition decision without a predetermined or reflexive preference for either admitting or discharging."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what was going on in the department when this patient arrived.",
        "What was your first impression of the patient's presentation?"
      ],
      "timeline_reconstruction": [
        "What happened right after you completed the initial exam?",
        "What did you learn between ordering the D-dimer and getting the result back?",
        "How did the conversation about Dr. B's earlier patient come up during your shift?",
        "What was the sequence of events after the CTPA came back?"
      ],
      "decision_point_probes": [
        "What made you want to examine the leg directly rather than settle on the chest wall finding alone?",
        "What alternative explanations did you keep open at that point, and why?",
        "What led you to recheck the risk score before deciding on the CTPA?",
        "How much did the scanner queue and bed pressure factor into that decision?",
        "When you thought about Dr. B's decision, what information were you waiting to confirm before forming a view?",
        "Would your assessment of Dr. B's decision have changed if the outcome had been different but the documented reasoning stayed the same?",
        "How did you weigh admission versus discharge for the final disposition?"
      ],
      "goals_and_alternatives": [
        "What were you trying to accomplish at each stage—speed, certainty, or safety?",
        "What was the next-best alternative you didn't choose at each decision point?"
      ],
      "decision_basis_and_experience": [
        "What past cases, if any, were you drawing on during this shift?",
        "How confident were you in each decision at the time you made it, versus now?"
      ],
      "time_pressure_and_uncertainty": [
        "How much did the two-hour handoff deadline shape your choices?",
        "Where did you feel most uncertain during this case?"
      ],
      "closing_hypotheticals": [
        "If the department had been quiet that night, would you have handled the D-dimer result differently?",
        "If you'd learned about Dr. B's Wells score before hearing about the outcome, would your reaction have been different?",
        "Looking back, is there a point where you'd have paused longer before deciding?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "HC_Biased_3",
      "features_to_match": [
        "Domain vocabulary (Wells score, PERC, D-dimer, CTPA, costochondritis, disposition, hospitalist admission, contrast reaction)",
        "Setting and constraints (ED overcrowding, single scanner, boarding pressure, handoff deadline)",
        "Actors (attending, resident, charge nurse, radiology tech, Dr. B, hospitalist)",
        "Emotional tone (time-pressured, mildly anxious family, professional uncertainty)",
        "Exact four-decision-point structure and sequencing",
        "Difficulty level (challenging) and narrative complexity"
      ],
      "features_to_remove_or_change": [
        "Early closure on musculoskeletal strain without examining the calf",
        "Ordering CTPA without first reassessing risk score",
        "Judging Dr. B's decision primarily by outcome before learning the process",
        "Any framing that resolves ambiguity through reflexive action or premature diagnostic settlement"
      ],
      "ambiguity_boundary": "Genuine clinical uncertainty (borderline D-dimer, incidental nodule, disposition trade-off) is preserved, but every decision is supported by an explicit, reasonable evidentiary or process-based justification rather than by a shortcut pattern matching a named bias."
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
      "Exactly 4 decision points present, matching the paired biased scenario's phase structure",
      "Zero intended bias instances embedded anywhere in the interview",
      "All vocabulary, actors, constraints, and emotional tone match HC_Biased_3",
      "Each decision point shows balanced consideration of at least two alternatives with a stated, reasonable justification",
      "No bias labels, definitions, or psychological explanations appear in probe plan or timeline text",
      "Word count target 1,350 (range 1,215-1,485) achievable given matched narrative density to the paired scenario",
      "Consequences at each decision point (calf swelling, incidental nodule, contrast reaction, Wells-score confirmation) remain genuinely uncertain and do not mechanically prove sound or unsound reasoning"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Premature Closure",
        "occurrences": 0,
        "mechanism_constraint": "Not to be embedded; control condition overrides any nonzero input count."
      },
      {
        "bias": "Outcome Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not to be embedded; control condition overrides any nonzero input count."
      },
      {
        "bias": "Action Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not to be embedded; control condition overrides any nonzero input count."
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
        "requested_occurrences": 0
      },
      {
        "bias": "Outcome Bias",
        "requested_occurrences": 0
      },
      {
        "bias": "Action Bias",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "HC_Biased_3",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Vocab_Control_3",
    "domain_id": "HC",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: vocabulary_control forces zero intended instances of all named target biases regardless of the caller-supplied manifest, which here identifies the paired target bias set (Premature Closure, Outcome Bias, Action Bias) rather than a nonzero request for this condition.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Setting, constraints, and time pressure profile",
      "Actor roster and roles",
      "Emotional tone",
      "Four-decision-point structure and sequencing",
      "Difficulty level"
    ],
    "generation_warnings": [
      "Caller-supplied manifest listed occurrences of 1 for each of three biases, matching the paired biased scenario's manifest; per condition rules for vocabulary_control, this was treated as the target bias identification for pairing purposes only, and all occurrences were overridden to 0 for this control scenario."
    ]
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_differential_reasoning",
        "raw_interview_anchor": "Reproducible chest wall tenderness suggested a musculoskeletal cause, but the flight and calf-ache history remained relevant.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant considers competing explanations rather than settling on the first coherent account."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_and_deferred_commitment",
        "raw_interview_anchor": "The flight and calf comment gave me pause, so the participant deferred a final impression until the leg was examined directly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly delays commitment pending a targeted examination."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "formal_risk_reassessment",
        "raw_interview_anchor": "A borderline D-dimer depended on pretest probability, so the participant and resident recalculated the Wells score before imaging.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The imaging decision is based on formal reassessment rather than the isolated test result."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "resource_allocation_reasoning",
        "raw_interview_anchor": "The scanner queue and bed pressure did not skip reassessment; after the score supported imaging, radiology was asked to prioritize him within the queue.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Operational pressure affects prioritization but is not described as overriding clinical reasoning."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "deferred_colleague_evaluation",
        "raw_interview_anchor": "The participant did not know enough to judge Dr. B and asked the resident to pull the chart before forming an opinion.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant withholds judgment until contemporaneous decision information is available."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "process_over_outcome_evaluation",
        "raw_interview_anchor": "After finding a formal low-risk Wells score and negative PERC, the participant called Dr. B's decision reasonable and said a different outcome would not change that assessment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant evaluates the colleague's reasoning by available process information rather than outcome."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "disposition_tradeoff_reasoning",
        "raw_interview_anchor": "The participant weighed the eventful visit against actual overnight safety, arranged follow-up and precautions, and discharged while acknowledging uncertainty.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Admission and discharge are both considered, with a stated clinical rationale and residual uncertainty."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "disposition_basis_and_pressure_assessment",
        "raw_interview_anchor": "The overnight risk profile had not changed and follow-up was arranged; boarding pressure was present but not considered the driver.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant distinguishes relevant disposition evidence from background operational pressure."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "counterfactual_process_reasoning",
        "raw_interview_anchor": "Earlier documentation of calf swelling would have prompted a formal score sooner but would not have changed the decision to image.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The counterfactual changes timing of the process, not the ultimate clinical choice."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "counterfactual_stability_reasoning",
        "raw_interview_anchor": "A quiet department would not have changed the need for the leg exam and recalculated score.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states that the key reassessment step was invariant to workload."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "order_invariance_reasoning",
        "raw_interview_anchor": "Learning Dr. B's Wells score at the same time as the outcome would not have changed the question of what he knew when deciding.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly rejects outcome-based revision of the evaluation."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "retrospective_resource_reflection",
        "raw_interview_anchor": "The participant might have pushed radiology harder, but would not change the clinical reasoning.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive reflection on a possible operational improvement, not a bias manifestation."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "uncertainty_assessment",
        "raw_interview_anchor": "The participant identified final disposition as the least certain point and described it as a genuine close call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Acknowledged uncertainty and balanced tradeoffs do not constitute a hidden bias instance."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Objective review of the participant's recounted reasoning for affirmative, mechanism-level evidence of cognitive biases. No confirmed bias occurrence met the threshold; one candidate pattern was noted but not identified as an occurrence."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Outcome bias",
      "alternative_labels": [
        "Outcome effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Charge nurse (as reported by the Participant)",
      "possible_decision_episode_label": "Evaluation of Dr. B's earlier similar chest pain discharge",
      "supporting_interview_quote": "While we were waiting on the CTPA, the charge nurse mentioned Dr. B had a similar-looking patient the week before—same kind of pleuritic pain—and discharged him without imaging. She said the patient did fine afterward.",
      "plausible_mechanism": "The charge nurse may have implicitly evaluated the earlier discharge as appropriate because of the good outcome, rather than by examining the documented reasoning or risk stratification.",
      "why_not_identified": "The transcript provides only a secondhand report of the charge nurse's statement and no affirmative evidence that the charge nurse actually based a judgment or decision on the favorable outcome. The participant immediately questioned the evidentiary value of the outcome and reviewed documentation before forming an opinion."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "Analysis is based on a brief self-reported interview rather than direct observation of real-time cognition.",
    "The participant shows substantial evidence of deliberate debiasing and reflective reasoning; absence of detected biases does not imply perfect decision-making.",
    "Only biases with affirmative mechanism-level evidence in the transcript were eligible for identification."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Vocab_Control_3_Gemini_on",
  "interview_id": "HC_Vocab_Control_3",
  "system_prompt_id": "Gemini",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
