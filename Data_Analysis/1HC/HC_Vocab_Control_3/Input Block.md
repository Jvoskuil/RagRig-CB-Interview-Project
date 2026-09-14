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
[ontology-free RAG JSON output]
</RAG_ANALYSIS_OUTPUT>
