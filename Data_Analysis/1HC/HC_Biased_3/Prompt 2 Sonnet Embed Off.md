You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about how you handled a specific case, purely for internal review of decision-making processes—not a quality complaint or formal chart audit. Is that okay to proceed?

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

Participant: The D-dimer moment, honestly. That's where I moved fastest, and where slowing down might have mattered most.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HC_Biased_3",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Emergency Medicine Attending Physician (community hospital, ~8 years post-residency experience)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Overnight Chest Pain Disposition",
    "scenario_summary_internal": "An ED attending physician manages a 52-year-old patient with pleuritic chest pain during a boarded, high-volume evening shift. The attending anchors early on a musculoskeletal explanation despite a modest pulmonary-embolism risk cue, later orders an aggressive confirmatory scan under throughput pressure rather than tolerating a period of risk-stratified observation, and separately evaluates a colleague's earlier similar case largely through the lens of how that case turned out rather than the information available to the colleague at the time. The shift closes with a genuinely uncertain, non-biased disposition decision for the index patient.",
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
          "Nurse rechecks the patient later and notes mild left calf swelling not previously documented"
        ],
        "alternatives": [
          "Settle on musculoskeletal strain as the working diagnosis and move to closing the chart",
          "Treat the flight history and calf ache as active cues warranting continued differential consideration (e.g., formal Wells scoring) before settling on a diagnosis"
        ],
        "intended_action": "Attending documents musculoskeletal strain as the likely explanation based on reproducible tenderness, treats the flight history and calf ache as incidental noise, and stops generating alternative explanations."
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
          "Order an emergent CTPA immediately to resolve the question definitively",
          "Use the borderline D-dimer with a formal risk score (e.g., repeat Wells/PERC assessment or a period of monitored observation) before deciding whether imaging is truly necessary"
        ],
        "intended_action": "Attending orders the emergent CTPA right away, framed as the decisive move to 'get an answer' under time pressure, rather than first completing a structured risk reassessment that might have supported observation."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Charge nurse mentions that Dr. B discharged a similarly presenting patient the prior week without ordering imaging",
          "Attending is told that patient later did well with no adverse event",
          "Attending has no direct knowledge of what specific findings, risk scores, or conversation Dr. B had with that patient at the time",
          "Attending is mid-shift, multitasking on the current CTPA workup"
        ],
        "new_information_after_decision": [
          "Later in conversation, the resident notes that Dr. B had in fact documented a formal low-risk Wells score and PERC-negative status before discharging that patient"
        ],
        "alternatives": [
          "Judge Dr. B's decision quality based on the information and reasoning Dr. B actually had available at the time",
          "Judge Dr. B's decision quality primarily by how the case turned out"
        ],
        "intended_action": "Attending remarks that Dr. B's choice to forgo imaging was clearly the right call, justifying that judgment mainly by pointing to the patient's uneventful outcome rather than asking what information or risk stratification Dr. B had used."
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
        "What specific findings led you to settle on musculoskeletal strain at that point?",
        "What alternative explanations did you consider, and why did you set them aside?",
        "What made you decide to move straight to CTPA rather than reassess risk first?",
        "How much did the scanner queue and bed pressure factor into that decision?",
        "When you evaluated Dr. B's decision, what information were you basing that judgment on?",
        "Would your assessment of Dr. B's decision have changed if you'd known the Wells score details upfront?",
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
    "occurrence_embedding_plan_internal": [
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
    "generation_warnings": []
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
        "segment_type": "initial_diagnostic_interpretation",
        "raw_interview_anchor": "Reproducible tenderness was described as classic for costochondritis, and the furniture-moving history was said to fit.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a plausible initial clinical interpretation without the required hidden-bias manifestation by itself."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "diagnostic_evidence_weighting_and_closure",
        "raw_interview_anchor": "The chest wall tenderness was the dominant finding; the flight and calf symptom felt like background noise; the participant did not chase it further and considered the case basically settled.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "pc_01"
        ],
        "ground_truth_rationale": "The participant settles on a musculoskeletal explanation after a salient finding, dismisses unresolved PE-risk cues, and stops further differential consideration."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "alternative_management_analysis",
        "raw_interview_anchor": "The participant described either redoing risk stratification with Wells/PERC or obtaining CTPA immediately.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly articulates competing options and their relevant diagnostic implications; the bias manifestation occurs in the subsequent choice rationale."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "immediate_action_choice_and_resource_allocation",
        "raw_interview_anchor": "The participant sent the patient straight for CTPA, citing the queue, boarding pressure, handoff deadline, and the desire to get a real answer and make the decisive move.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ab_01"
        ],
        "ground_truth_rationale": "The participant favors immediate imaging over rescoring or observation and frames the decision around decisiveness and resolving ambiguity under pressure."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "test_consequence_assessment",
        "raw_interview_anchor": "The negative CTPA was reassuring, but the incidental nodule and mild contrast reaction required follow-up and monitoring and consumed additional time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an assessment of consequences after the decision, not an intended hidden bias instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective_third_party_decision_evaluation",
        "raw_interview_anchor": "Dr. B's decision was initially called clearly right because nothing bad happened; the participant later acknowledged reacting to the good outcome rather than what Dr. B knew going in.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ob_01"
        ],
        "ground_truth_rationale": "The initial evaluation of Dr. B's decision is based primarily on the favorable outcome before process information is known, with later reflection confirming that mechanism."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "final_disposition_reasoning",
        "raw_interview_anchor": "The participant went back and forth about admission versus discharge, then discharged because the patient was stable, PE was excluded, outpatient follow-up was arranged, and admission would not change overnight management.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The disposition decision is explicitly uncertain, clinically reasoned, and intentionally neutral in the hidden specification."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_uncertainty_reflection",
        "raw_interview_anchor": "The participant identified the D-dimer moment as the point where they moved fastest and might have paused longer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective reflection on uncertainty and pacing, not a separate hidden instance."
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
    "analysis_scope_note": "Analyzed as a self-contained CTA interview; no experimental condition, manipulation, or intended bias count was assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "action_bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "anchoring_bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "outcome_bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring_bias",
      "alternative_labels": [
        "premature_closure",
        "diagnostic_momentum"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information or initial diagnostic impression and to insufficiently adjust subsequent judgments in light of new or contradictory information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial assessment of a patient with pleuritic chest pain and possible PE",
      "decision_point_description": "After reproducing chest wall tenderness and hearing lifting history, forming a working diagnosis and deciding whether to pursue PE risk factors or formal risk scoring.",
      "affected_reasoning_operation": "Diagnostic hypothesis generation and information weighting",
      "bias_specific_mechanism": "Anchoring on a salient, easily available exam finding (reproducible chest wall tenderness) and compatible history caused the participant to downgrade PE-relevant cues (recent flight, sore calf) as background noise and accept a musculoskeletal diagnosis prematurely.",
      "manifestation_in_interview": "The participant described the chest wall tenderness as the dominant finding and the flight/calf information as background noise; he said the case was basically settled and began communicating a strain diagnosis to the resident without formal Wells scoring.",
      "effect_on_reasoning_or_decision": "The participant stopped pursuing PE risk assessment at that point, told the resident the case was a musculoskeletal strain, and began wrapping up that portion of the visit.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "the chest wall tenderness was the dominant finding for me. It's a strong, reproducible sign, and combined with the lifting history, it painted a clean picture. The flight and the calf thing felt like background noise—people mention all kinds of things when you ask an open history. I didn't chase it further at that point; I told the resident we were looking at a musculoskeletal strain and started wrapping up that part of the visit.",
          "evidence_explanation": "This quote shows the participant treating the initial diagnostic impression as a clean picture and explicitly downgrading PE-relevant information, which is the anchoring mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. It felt like overkill given how clean the exam finding was.",
          "evidence_explanation": "This shows the anchor suppressing formal risk stratification; the initial benign impression was used as sufficient reason not to pursue a structured PE workup."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In my head, the case was basically settled—strain, reassurance, maybe some ibuprofen.",
          "evidence_explanation": "This is an explicit statement of premature closure based on the anchored diagnosis."
        }
      ],
      "correction_or_counterevidence": "A chest-pain protocol D-dimer sent by the resident later surfaced PE risk after the secondary finding of calf swelling, serving as an external check on the initial diagnostic impression; however, it did not prevent the initial anchored assessment and communication to the resident.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the analysis context; the label is assigned from established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "action_bias",
      "alternative_labels": [
        "commission_bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to favor taking action over inaction or further deliberation, especially under uncertainty or pressure, even when a more measured strategy may be indicated.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to elevated D-dimer after calf swelling was noted",
      "decision_point_description": "Choosing between formally recalculating risk (Wells/PERC) before deciding whether to image and proceeding directly to CTPA.",
      "affected_reasoning_operation": "Clinical decision selection under uncertainty",
      "bias_specific_mechanism": "Under time pressure and diagnostic ambiguity, the participant framed immediate imaging as a decisive, productive action and framed further risk scoring as unproductive deliberation, leading to a preference for action over more measured assessment.",
      "manifestation_in_interview": "The participant described ordering CTPA immediately, explicitly saying it felt like the more decisive move and that action was productive compared with sitting on an ambiguous number.",
      "effect_on_reasoning_or_decision": "He ordered CTPA without recalculating the Wells score or applying PERC; this led to definitive imaging and its downstream consequences, including an incidental nodule and contrast reaction.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I sent him straight for the CTPA.",
          "evidence_explanation": "This is the direct statement of the action chosen without the formal risk recalculation he had just described as the alternative."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking, let's just get the scan and have a real answer instead of going back and forth on scoring systems. It felt like the more decisive move—stop deliberating, get imaging, know for sure.",
          "evidence_explanation": "This reveals a preference for immediate action to resolve uncertainty rather than choosing based on a structured risk estimate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not formally. I probably could have, and in retrospect the numbers might have supported watching him a bit longer instead. But at the time, ordering the scan felt like the productive thing to do rather than sitting on an ambiguous number.",
          "evidence_explanation": "He explicitly frames action as productive and further deliberation as merely sitting on ambiguity, which is consistent with action bias rather than a process-driven choice."
        }
      ],
      "correction_or_counterevidence": "A competing non-bias explanation is that immediate CTPA was clinically reasonable after newly documented calf swelling and a positive D-dimer. The participant also later acknowledged that with more time he might have redone the scoring, but this reflection did not occur before the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the analysis context; the label is assigned from established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "outcome_bias",
      "alternative_labels": [
        "result_bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the quality of a decision primarily by its eventual outcome rather than by the reasoning and information available at the time of the decision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of Dr. B's similar case described by the charge nurse",
      "decision_point_description": "Upon hearing that Dr. B discharged a similar patient without imaging and the patient did well, forming an immediate judgment about whether Dr. B's decision was correct.",
      "affected_reasoning_operation": "Retrospective judgment of another clinician's decision quality",
      "bias_specific_mechanism": "The participant used the favorable outcome (the patient did fine) as evidence that Dr. B's decision was correct, rather than the quality of the decision process or the information available at the time.",
      "manifestation_in_interview": "The participant stated Dr. B made the right decision because nothing bad happened, acknowledged he did not know the process details, and later recognized that a bad outcome would have changed his first reaction despite the same underlying reasoning.",
      "effect_on_reasoning_or_decision": "The participant communicated to the resident that Dr. B read the situation correctly, endorsing the decision based on outcome rather than process.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was that Dr. B made a good call there—clearly the right decision, since nothing bad happened. I said something like that to the resident, actually, that Dr. B read the situation correctly.",
          "evidence_explanation": "The stated reason for judging the call correct is the favorable outcome, not the decision process, which is the signature of outcome bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, I didn't know any of that. I was just going off the fact that it turned out fine.",
          "evidence_explanation": "Direct admission that the outcome, not process information, drove the evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I was reacting more to the fact that it ended well than to what Dr. B actually knew going in. If it had gone badly, I probably would've had a very different first reaction, even with the same underlying reasoning on his part.",
          "evidence_explanation": "The participant explicitly recognizes that his evaluation would reverse with a bad outcome, which demonstrates the outcome-based mechanism."
        }
      ],
      "correction_or_counterevidence": "Later in the conversation the resident reported that Dr. B had documented a low Wells score and negative PERC before discharging, providing process-based support for the decision. The participant acknowledged this added information, but it did not erase the initial outcome-driven evaluation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the analysis context; the label is assigned from established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "availability_heuristic",
      "alternative_labels": [
        "affect_heuristic",
        "salience_bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Disposition decision after negative PE workup and contrast reaction",
      "supporting_interview_quote": "Part of me wanted to admit him overnight just because the visit had been eventful—the contrast reaction, the nodule, the whole thing.",
      "plausible_mechanism": "Salient, recent events in the visit (contrast reaction and incidental nodule) may have made overnight admission feel more necessary than clinical factors supported.",
      "why_not_identified": "The participant explicitly recognized this as a non-clinical pull and ultimately discharged the patient with arranged outpatient follow-up; there is no affirmative evidence that this thought materially changed the final disposition decision."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied in the task context, so all bias labels rely on general cognitive-science knowledge rather than corpus-grounded evidence.",
    "The analysis is based on the participant's retrospective self-report rather than direct observation of the clinical episode."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Biased_3_Sonnet_off",
  "interview_id": "HC_Biased_3",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
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
