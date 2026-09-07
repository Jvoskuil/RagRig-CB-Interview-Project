You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Your task is to compare:
1. A raw cognitive task analysis interview;
2. The complete interview-generation specification, including its hidden validation specification;
3. A RAG system's JSON analysis output; and
4. Optionally, a prevalidated evaluation segment map.

You must evaluate how closely the RAG system output overlaps with the hidden ground truth.

You are an evaluator, not a new cognitive-bias analyst. Do not award credit merely because a RAG prediction is psychologically plausible, academically reasonable, well-written, or supported by external knowledge. Evaluate the RAG output against the hidden generation specification, the hidden validation specification, and the raw interview.

OUTPUT REQUIREMENT

Return exactly one valid JSON object that conforms to the output schema specified below.

Do not return Markdown.
Do not wrap JSON in a code fence.
Do not provide text before or after the JSON.
Do not reveal chain-of-thought or hidden reasoning.
Do not add keys not included in the required schema.
Use concise, auditable explanations that refer to the supplied input materials.

INPUTS

You will receive input blocks with the following labels:

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

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis of a single interview for affirmatively evidenced cognitive biases in the participant's reported clinical reasoning. No retrieved scientific-paper corpus was supplied; findings are based on the interview text and the stated reference-ontology definitions."
  },
  "identified_bias_summary": [
    {
      "canonical_bias_name": "Action Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Anchoring Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Outcome Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Premature Closure",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Anchoring Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Overweighting a salient initial finding or piece of information and insufficiently adjusting subsequent judgments as new information emerges.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial chest pain assessment and provisional diagnosis",
      "decision_point_description": "Assigning a preliminary diagnosis and deciding whether to pursue the reported travel history and calf soreness.",
      "affected_reasoning_operation": "Interpretation and weighting of clinical findings in the initial diagnostic probability judgment.",
      "bias_specific_mechanism": "The salient chest-wall tenderness and lifting history anchored the diagnostic impression, so subsequent VTE risk information such as the recent flight and calf soreness was treated as background noise rather than triggering meaningful adjustment.",
      "manifestation_in_interview": "The participant described the musculoskeletal findings as dominant and the flight/calf information as not worth chasing, even though the calf had not been examined.",
      "effect_on_reasoning_or_decision": "Led to a provisional musculoskeletal strain plan and no initial pursuit of leg examination or formal VTE risk stratification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the chest wall tenderness was the dominant finding for me. It's a strong, reproducible sign, and combined with the lifting history, it painted a clean picture. The flight and the calf thing felt like background noise—people mention all kinds of things when you ask an open history. I didn't chase it further at that point; I told the resident we were looking at a musculoskeletal strain and started wrapping up that part of the visit.",
          "evidence_explanation": "This shows the initial chest-wall finding dominated the diagnostic interpretation, while the travel history and calf symptom were explicitly discounted even though they represented relevant VTE risk information."
        }
      ],
      "correction_or_counterevidence": "Counterevidence later emerged when the nurse noted left calf swelling and the D-dimer returned elevated; however, the participant still did not formally recalculate risk before proceeding to imaging.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided in this task. This finding is based on the interview evidence and the reference-ontology definition of Anchoring Bias rather than on retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Premature Closure",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Terminating diagnostic hypothesis generation or information search early after forming a plausible diagnosis, before adequately evaluating alternative explanations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial chest pain assessment after forming costochondritis impression",
      "decision_point_description": "Deciding whether to formally work through additional risk stratification after a preliminary diagnosis.",
      "affected_reasoning_operation": "Diagnostic hypothesis generation and decision to stop further early workup.",
      "bias_specific_mechanism": "Once the participant had a clean-feeling musculoskeletal explanation, he treated the case as effectively settled and avoided further formal risk scoring or alternative-diagnosis evaluation.",
      "manifestation_in_interview": "The participant stated the case was basically settled and that a Wells score felt like overkill after the reassuring exam finding.",
      "effect_on_reasoning_or_decision": "Contributed to the decision not to calculate Wells/PERC initially and to wrapping up that part of the visit before the calf swelling and D-dimer result emerged.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. It felt like overkill given how clean the exam finding was. In my head, the case was basically settled—strain, reassurance, maybe some ibuprofen.",
          "evidence_explanation": "The participant explicitly describes closing the diagnostic question after the initial reassuring pattern, despite risk factors that had not been fully evaluated."
        }
      ],
      "correction_or_counterevidence": "External counterevidence later emerged from the nurse's calf-swelling finding and the elevated D-dimer, but the closure had already shaped the initial reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided in this task. This finding is based on the interview evidence and the reference-ontology definition of Premature Closure rather than on retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Action Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "A tendency to take action or make a decision when action is perceived as productive or decisive, even when waiting or further analysis might be equally or more appropriate.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-D-dimer imaging decision",
      "decision_point_description": "Deciding whether to recalculate risk scores and apply PERC versus ordering CTPA immediately after the elevated D-dimer and new calf swelling.",
      "affected_reasoning_operation": "Clinical action choice under uncertainty after new information.",
      "bias_specific_mechanism": "Under time and capacity pressure, the participant chose immediate imaging because doing something felt decisively productive, rather than engaging in slower risk-stratification reasoning.",
      "manifestation_in_interview": "The participant explicitly framed the CTPA as the more decisive move to get a real answer and avoid further deliberation on scoring systems.",
      "effect_on_reasoning_or_decision": "Resulted in immediate CTPA, with downstream contrast reaction and nodule follow-up, despite later acknowledgment that formal scoring might have supported observation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I sent him straight for the CTPA. Scanner had a 40-minute queue already because of a trauma case, charge nurse was on me to move patients since we had boarders stacking up, and I had maybe two hours before handoff. I remember thinking, let's just get the scan and have a real answer instead of going back and forth on scoring systems. It felt like the more decisive move—stop deliberating, get imaging, know for sure.",
          "evidence_explanation": "The wording shows a preference for immediate diagnostic action under pressure, with decisiveness itself treated as a reason for choosing CT over recalculation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, not formally. I probably could have, and in retrospect the numbers might have supported watching him a bit longer instead. But at the time, ordering the scan felt like the productive thing to do rather than sitting on an ambiguous number.",
          "evidence_explanation": "This confirms the action choice was driven by a sense of productivity rather than by a formally updated pretest probability."
        }
      ],
      "correction_or_counterevidence": null,
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided in this task. This finding is based on the interview evidence and the reference-ontology definition of Action Bias rather than on retrieved corpus support.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Outcome Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Evaluating the quality of a decision based on its eventual outcome rather than on the reasoning and information available at the time of the decision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial reaction to Dr. B's prior case",
      "decision_point_description": null,
      "affected_reasoning_operation": "Retrospective quality judgment of a colleague's clinical decision.",
      "bias_specific_mechanism": "The participant inferred that Dr. B's discharge decision was correct because the patient did well, without knowing the documented reasoning or risk stratification.",
      "manifestation_in_interview": "The participant said Dr. B clearly made the right decision since nothing bad happened, and later acknowledged he was reacting to the good outcome rather than the decision process.",
      "effect_on_reasoning_or_decision": "Produced an initial judgment that Dr. B read the situation correctly, based solely on the favorable outcome.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first thought was that Dr. B made a good call there—clearly the right decision, since nothing bad happened. I said something like that to the resident, actually, that Dr. B read the situation correctly.",
          "evidence_explanation": "The quote explicitly grounds the quality judgment in the good outcome rather than in the clinical reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, I didn't know any of that. I was just going off the fact that it turned out fine.",
          "evidence_explanation": "This removes the possibility that the participant was initially judging Dr. B's documented reasoning; the initial reaction was outcome-based."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I was reacting more to the fact that it ended well than to what Dr. B actually knew going in. If it had gone badly, I probably would've had a very different first reaction, even with the same underlying reasoning on his part.",
          "evidence_explanation": "The participant himself identifies the outcome-dependent nature of the initial reaction."
        }
      ],
      "correction_or_counterevidence": "Later, the resident provided the structured clinical reasoning behind Dr. B's decision—low Wells score and negative PERC—and the participant acknowledged that this additional detail changed the framing of his initial reaction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided in this task. This finding is based on the interview evidence and the reference-ontology definition of Outcome Bias rather than on retrieved corpus support.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_name": "Base-Rate neglect",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-D-dimer imaging decision",
      "supporting_interview_quote": "No, not formally. I probably could have, and in retrospect the numbers might have supported watching him a bit longer instead. But at the time, ordering the scan felt like the productive thing to do rather than sitting on an ambiguous number.",
      "plausible_mechanism": "The participant did not formally use Wells/PERC pretest probability to interpret the borderline D-dimer, potentially neglecting base-rate information.",
      "why_not_identified": "The interview presents the decision primarily as a deliberate action-orientation under time pressure, not as a clear probability judgment that ignored base rates. The base-rate neglect is plausible but less directly evidenced than the action preference."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_name": "Affect Heurisitic",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "End-of-shift discharge decision",
      "supporting_interview_quote": "Part of me wanted to admit him overnight just because the visit had been eventful—the contrast reaction, the nodule, the whole thing.",
      "plausible_mechanism": "The emotional salience of the eventful visit may have made admission feel more appropriate than the clinical evidence alone supported.",
      "why_not_identified": "The participant articulated this as an emotionally influenced consideration but then overrode it with clinical reasoning and discharged the patient. The interview does not show that the affect materially altered the final decision or an intermediate clinical action."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper passages were supplied, so retrieved_corpus_support_used is false and all corpus_evidence arrays are empty. Findings rely on the reference-ontology definitions and the interview text.",
    "The analysis is based on a single interview and self-reported reasoning; it does not verify the clinical facts or actual cognitive processes.",
    "Some reasoning patterns may partly reflect situational constraints such as crowding and time pressure rather than cognitive bias alone.",
    "The absence of a bias label does not mean other biases are absent; only affirmatively evidenced occurrences are identified."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<EVALUATION_SEGMENT_MAP>
Optional. A prevalidated, externally supplied segment map for this interview.
</EVALUATION_SEGMENT_MAP>

The evaluation segment map may be absent, empty, null, or unavailable.

CONFIDENTIALITY AND EVALUATOR BOUNDARY

The complete generation specification and hidden validation specification are evaluator-only ground truth.

The RAG system did not receive these materials. Do not penalize the RAG system for failing to state hidden labels, internal generation details, hidden intended actions, hidden requirements, or internal scenario terminology that cannot reasonably be inferred from the raw interview.

Do not use the hidden specification to invent a RAG finding the system did not make.
Do not convert a RAG candidate finding into an identified finding.
Do not assume the RAG system should have detected every hidden instance if the raw interview does not support it.
Do not grant credit based on hidden intent alone when the RAG system cited the wrong raw-interview segment or supplied an unsupported mechanism.

GROUND-TRUTH PRINCIPLE

Treat `exact_occurrence_manifest` in the hidden validation specification as exhaustive for cognitive-bias occurrences intentionally present in the specific interview under evaluation.

A hidden bias instance is defined by all applicable information in the complete generation specification, including:
- `instance_id`;
- Intended bias;
- Intended mechanism;
- Affected reasoning operation;
- Intended decision point, if applicable;
- Required textual manifestation;
- Evidence available at the time;
- Distinctiveness requirements;
- Plausible non-bias interpretation;
- Hidden mechanism constraint;
- Raw-interview evidence supporting that instance.

The reference bias ontology is not exhaustive of all conceivable cognitive biases. However, for primary benchmark scoring:
- A prediction of an outside-reference-ontology bias is not automatically correct merely because it is psychologically plausible.
- An outside-ontology prediction may be considered an approved equivalent only if its mechanism is substantively identical to a hidden target bias and the label is an established alternate name for that target construct.
- A merely related, adjacent, overlapping, or near-neighbor concept is not an exact match.
- Near-neighbor and outside-ontology predictions must receive a mechanism-overlap assessment and be reported in the diagnostic output.

EVALUATION LEVELS

Perform evaluation at both levels below. Keep their counts separate.

LEVEL 1: SEGMENT-LEVEL BIAS DETECTION

The segment-level question is:

"Does this eligible reasoning segment contain at least one manifested hidden cognitive-bias instance?"

Segment-level evaluation is binary:
- A segment is ground-truth positive if it contains one or more hidden bias instances.
- A segment is ground-truth negative if it is an eligible reasoning segment containing no hidden bias instance.
- A RAG segment detection is positive if one or more RAG `identified_occurrences` are localized to that segment.
- RAG `candidate_biases` do not count as positive detections in primary Signal Detection Theory metrics.

Use segment-level outcomes as follows:
- Hit: Ground-truth positive segment and one or more RAG identified occurrences localize to that segment.
- Miss: Ground-truth positive segment and no RAG identified occurrence localizes to that segment.
- False positive / false alarm: Ground-truth negative segment and one or more RAG identified occurrences localize to that segment.
- Correct rejection: Ground-truth negative segment and no RAG identified occurrence localizes to that segment.

Important:
- Segment-level results assess whether the system detected biased reasoning in the correct general location.
- Segment-level hits do not prove that the RAG system supplied the correct bias label or mechanism.
- A RAG prediction with the wrong bias label at a genuinely biased ground-truth segment can still produce a segment-level hit while producing an instance-level miss and an instance-level false positive.
- Do not calculate label-level correct rejections across all conceivable cognitive-bias labels. The ontology is non-exhaustive. Correct rejections are reported only at the finite segment-detection level.

LEVEL 2: INSTANCE-LEVEL BIAS IDENTIFICATION AND CLASSIFICATION

For each hidden planned bias instance, determine whether exactly one RAG `identified_occurrence` matches it.

An exact instance-level hit requires all of the following:
1. Correct target canonical bias label, or an approved established alias mapping;
2. Correct localization to the intended raw-interview reasoning segment or a substantively equivalent evidence span;
3. Materially correct bias-specific mechanism;
4. Materially correct affected reasoning operation;
5. Interview evidence that genuinely supports the hidden instance;
6. No conflict with the hidden instance's distinctiveness requirement.

The primary instance-level score is strict:
- A prediction that has the correct label but the wrong location is not an exact hit.
- A prediction that has the correct label and location but a materially wrong mechanism is not an exact hit.
- A prediction that correctly detects a biased segment but assigns the wrong bias is not an exact hit.
- A prediction with a partial but incomplete mechanism is not an exact hit.

In addition to strict primary scoring, produce secondary diagnostic classifications for:
- Correct location, wrong label;
- Correct label, wrong location;
- Correct label and location, but materially wrong mechanism;
- Correct label and location, but partially matching mechanism;
- Approved alias mapping;
- Near-neighbor label with substantial mechanism overlap;
- Outside-ontology label with substantial mechanism overlap;
- Duplicate prediction;
- Unsupported prediction;
- Invalid or fabricated quotation;
- Candidate-only omission.

INPUT VALIDATION

Before scoring:
1. Validate whether `RAG_ANALYSIS_OUTPUT` is parseable JSON.
2. Validate whether it conforms materially to the expected RAG schema.
3. Record schema violations, missing required fields, invalid confidence values, mismatched summary counts, invalid quotation claims, and other format failures.
4. Continue substantive scoring when feasible even if schema errors exist.
5. If the output cannot be parsed at all, return valid evaluator JSON indicating that substantive automated matching was not possible, with all appropriate counts set to null rather than invented.

Do not score RAG `candidate_biases` as identified cognitive-bias detections in primary SDT or instance-level counts.
Record candidates in a separate candidate-analysis section.

SEGMENT-MAP MODES

You must support two modes.

MODE A: PREVALIDATED SEGMENT MAP PROVIDED

If `<EVALUATION_SEGMENT_MAP>` contains a non-empty, valid segment map:
- Treat it as authoritative.
- Do not add, remove, merge, split, or revise its segments.
- Set `segment_map_status` to `prevalidated_provided`.
- Use its segment IDs, quotations, speaker assignments, and ground-truth bias-presence labels for segment-level scoring.
- Use the complete generation specification and raw interview only to validate RAG localization, hidden-instance mapping, quotations, and mechanism matching.

MODE B: NO PREVALIDATED SEGMENT MAP PROVIDED

If `<EVALUATION_SEGMENT_MAP>` is absent, empty, null, or invalid:
- Derive an evaluation segment map from the raw interview and complete generation specification.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Create the map before evaluating the RAG output.
- Derive the map using the raw interview and complete generation specification only.
- Do not let the RAG system's output determine which segments exist, where boundaries are placed, or whether segments are positive or negative.
- Return the complete generated segment map in the evaluator output so it can be reviewed, frozen, and reused in later benchmark runs.

SEGMENT-MAP CONSTRUCTION RULES

When generating a segment map:

1. Construct an exhaustive set of non-overlapping eligible reasoning segments.
2. Use the smallest contiguous speaker-attributed text span that contains one coherent reasoning operation.
3. An eligible reasoning segment must contain one or more of:
   - A judgment;
   - A decision;
   - An interpretation;
   - An inference;
   - A causal attribution;
   - A choice between alternatives;
   - A reason for action;
   - A resource-allocation rationale;
   - A prediction;
   - A communication or labeling choice;
   - A reason for weighting, ignoring, or prioritizing evidence;
   - A stated rationale for continuing, changing, rejecting, escalating, or deferring a course of action.
4. Do not create an eligible segment solely for:
   - Greetings;
   - Rapport-building;
   - Pure factual scene-setting with no reasoning;
   - Interviewer questions containing no expressed reasoning;
   - Neutral acknowledgements;
   - Generic educational discussion;
   - Mere mentions of bias terminology;
   - Hypothetical prompts that do not themselves express an adopted reasoning process;
   - Rhetorical repetition with no distinct reasoning operation.
5. Split a speaker turn where it contains distinct reasoning operations, distinct decisions, or separately expressed rationales.
6. Keep co-located bias mechanisms in the same segment only when they cannot be separated without losing their meaning.
7. Create separate segments for independently expressed mechanisms, even when they occur in the same speaker turn.
8. Map each hidden planned instance to the narrowest segment or segments that actually express its mechanism in the raw interview.
9. Mark a segment as ground-truth positive only when it contains at least one manifested hidden bias instance.
10. Mark every other eligible reasoning segment as ground-truth negative.
11. Do not create trivial negative segments merely to increase correct-rejection counts.
12. Do not omit substantive non-biased reasoning segments merely because the RAG system did not identify them.
13. Use exact raw-interview quotations for generated segments.
14. Assign stable sequential IDs in interview order: `seg_001`, `seg_002`, and so on.

Do not assume that all interviews have numbered phases, decision points, repeated structural patterns, or the same number of reasoning episodes.

LOCALIZATION MATCHING RULES

For every RAG `identified_occurrence`, determine its best segment-level localization using:
- Exact quote overlap;
- Substantively equivalent paraphrase;
- Correct speaker attribution;
- Correct reasoning episode;
- Correct decision context where one exists;
- Consistency with the raw interview.

Use these localization outcomes:

- `exact_quote_match`:
  The RAG quote is exact, valid, and directly overlaps the mapped segment's primary evidence span.

- `substantive_span_match`:
  The RAG quote differs from the mapped anchor but accurately identifies a substantively equivalent raw-interview statement in the same reasoning segment.

- `same_episode_adjacent_span`:
  The RAG evidence is in the same broader reasoning or decision episode but is not the specific mapped mechanism span.

- `wrong_segment`:
  The RAG output refers to a different reasoning episode, different decision, unrelated speaker statement, or a segment that does not contain the intended mechanism.

- `unsupported_or_fabricated_quote`:
  The claimed quote does not appear in the raw interview, is materially altered, is attributed to the wrong speaker, or does not support the claimed finding.

Only `exact_quote_match` and `substantive_span_match` qualify as correct localization for an exact instance-level hit.

A `same_episode_adjacent_span` result may support a secondary partial-location diagnostic but is not an exact instance-level hit unless the intended mechanism is still clearly supported.

BIAS-LABEL MATCHING RULES

For each RAG predicted bias label, apply this hierarchy:

1. `exact_canonical_match`:
   The RAG canonical label equals the hidden target canonical bias label.

2. `approved_alias_match`:
   The predicted label is an established spelling variant, alias, or equivalent term for the hidden target label, and the stated mechanism is substantively identical to the target mechanism.

3. `near_neighbor_label`:
   The predicted label is conceptually related to the target label but not an established synonym or equivalent. Assess mechanism overlap but do not count it as an exact label match.

4. `outside_ontology_equivalent`:
   The predicted label is outside the benchmark reference ontology but is an established alternate name for the target construct and has substantively identical mechanism. This may be approved as an alias match only when the equivalence is clear and explicitly justified.

5. `outside_ontology_non_equivalent`:
   The predicted label is outside the reference ontology and does not have a substantively identical mechanism to a target label. It is not an exact match.

6. `wrong_label`:
   The predicted label does not match the target label and does not qualify as an approved equivalent.

Do not approve an alias or outside-ontology equivalence merely because:
- The labels often co-occur;
- The labels are both broad cognitive-bias concepts;
- The labels concern the same decision;
- The labels share some evidence;
- The predicted label is plausible;
- The predicted label is a more general or more specific construct.

MECHANISM-OVERLAP SCORING

For each predicted occurrence and best candidate hidden instance, assess mechanism overlap independently of label agreement.

Use exactly one of:

- `full_mechanism_match`:
  The RAG explanation captures the defining hidden mechanism, relevant evidence weighting or reasoning distortion, and affected reasoning operation.

- `substantial_mechanism_overlap`:
  The RAG explanation captures the central mechanism but omits or weakly states one meaningful element, such as the relevant competing evidence, temporal feature, social-proof feature, prior-investment feature, ordering feature, or reasoning operation.

- `partial_mechanism_overlap`:
  The RAG explanation identifies a related mechanism but misses one or more central defining elements.

- `minimal_mechanism_overlap`:
  The RAG explanation is broadly related to the situation but does not identify the hidden bias-specific mechanism.

- `no_mechanism_overlap`:
  The RAG explanation does not correspond meaningfully to the hidden mechanism.

To receive an exact instance-level hit, the RAG occurrence must have `full_mechanism_match`.

A `substantial_mechanism_overlap` may be recorded as a secondary diagnostic partial match but is not a primary exact hit.

When evaluating near-neighbor or outside-ontology labels:
- Always report their mechanism-overlap level.
- State the specific shared and non-shared mechanism elements.
- Do not award an exact hit unless the label qualifies under the approved alias/equivalence rules and the mechanism is a full match.

ONE-TO-ONE INSTANCE MATCHING

Use one-to-one matching between RAG `identified_occurrences` and hidden planned instances.

Apply this matching priority:
1. Exact or approved-equivalent label match;
2. Correct localization;
3. Full mechanism match;
4. Correct affected reasoning operation;
5. Strongest exact raw-quote evidence;
6. Earliest occurrence order as a deterministic tie-breaker.

Each hidden instance can match at most one RAG occurrence.
Each RAG occurrence can match at most one hidden instance.

If multiple RAG occurrences match the same hidden instance:
- Select the best matching occurrence as the potential match.
- Classify remaining unmatched duplicates as instance-level false positives.
- Record them as `duplicate_prediction`.

If one RAG occurrence appears relevant to multiple hidden instances:
- Match it to only one hidden instance according to the priority rules.
- Do not award one prediction multiple exact hits.
- Record insufficiently separated co-located predictions in the diagnostic output.

PRIMARY INSTANCE-LEVEL ACCOUNTING

Use the following strict accounting:

- True positive / hit:
  One RAG occurrence exactly matches one hidden instance according to label, localization, and full-mechanism rules.

- False negative / miss:
  One hidden instance has no exact matching RAG occurrence.

- False positive:
  One RAG identified occurrence has no exact matching hidden instance.

A RAG occurrence that identifies the correct biased segment but uses the wrong label:
- Counts as one instance-level false positive for the predicted label;
- Counts as one instance-level false negative for the unmatched hidden target;
- Must additionally be recorded as `correct_location_wrong_bias_label`;
- May produce a segment-level hit if it localizes to a ground-truth positive segment.

A RAG occurrence with the correct label but wrong segment:
- Counts as one instance-level false positive;
- Leaves the true hidden instance as an instance-level false negative;
- Must be recorded as `correct_label_wrong_location`.

A RAG occurrence with correct label and correct location but a materially incorrect mechanism:
- Counts as one instance-level false positive;
- Leaves the true hidden instance as an instance-level false negative;
- Must be recorded as `correct_label_location_wrong_mechanism`.

A RAG occurrence with correct label and location but substantial, not full, mechanism overlap:
- Does not count as an exact primary true positive;
- Counts as one primary false positive and leaves the hidden instance as one primary false negative;
- Must be recorded as `partial_mechanism_match`;
- Must receive the appropriate mechanism-overlap level.

CONFIDENCE EVALUATION

The RAG system may return `high`, `moderate`, or `low` confidence identified occurrences.

For primary scoring:
- Include high-, moderate-, and low-confidence findings equally in the all-confidence confusion matrices.
- Do not treat low-confidence findings as candidates.
- Do not exclude low-confidence findings from false-positive counts.

Also calculate three nested threshold analyses:
1. `high_only`: Include only RAG findings with confidence `high`.
2. `high_and_moderate`: Include RAG findings with confidence `high` or `moderate`.
3. `all_identified_confidence_levels`: Include RAG findings with confidence `high`, `moderate`, or `low`.

For each threshold:
- Recalculate segment-level TP, FN, FP, and TN.
- Recalculate instance-level TP, FN, and FP.
- Report precision, recall, and F1 where denominators permit.
- Use null, not zero, when a metric denominator is zero.

Do not include `candidate_biases` in any confidence threshold.

CANDIDATE ANALYSIS

Evaluate RAG `candidate_biases` separately.

For each candidate:
- Determine whether it overlaps a hidden instance.
- Determine whether its quoted evidence is valid.
- Determine whether it would have been correct if promoted to an identified occurrence.
- Do not count it as a primary hit, miss, false positive, false alarm, or correct rejection.
- Record whether it represents a useful abstention, an unsupported speculation, a near miss, or a correctly localized but underconfident target.

ZERO-BIAS AND CONTROL INTERVIEWS

Some interviews contain no hidden cognitive-bias instances.

For an interview whose hidden manifest contains zero planned occurrences:
- Every eligible reasoning segment in the authoritative or generated segment map is ground-truth negative.
- Every RAG identified occurrence is an instance-level false positive.
- Every RAG localized bias prediction on an eligible segment is a segment-level false positive / false alarm.
- Every eligible segment with no RAG identified occurrence is a segment-level correct rejection.
- Candidates remain outside primary SDT counts but must be reported in candidate analysis.
- Do not create artificial positive segments merely because the RAG output identifies a bias.

COUNTERFACTUAL AND AMBIGUOUS-VOCABULARY INTERVIEWS

For counterfactual and ambiguous-vocabulary interviews:
- Use the complete generation specification to distinguish facts available at the time of the target reasoning from post-decision information.
- Do not credit a RAG system for using hindsight-only facts as evidence that a bias occurred.
- Do not assume a bias remains present merely because it existed in a paired scenario or is familiar from another scenario.
- Treat ambiguity as evidence of a bias only when the hidden mechanism and raw interview demonstrate the required biased resolution, weighting, or use of ambiguity.
- Do not confuse vague wording, uncertainty, or missing information with Ambiguity Bias unless the specific hidden mechanism is present.
- Consider the documented plausible non-bias interpretation when determining whether the RAG mechanism is full, substantial, partial, minimal, or unsupported.

RAG EVIDENCE AND CORPUS-SUPPORT AUDIT

The primary purpose of this evaluation is overlap with hidden generation ground truth, not retrieval-quality scoring.

Do not independently score corpus-grounding fidelity unless the actual retrieved corpus passages or retrieval logs are supplied as inputs.

However, record:
- Whether each RAG identified occurrence claims retrieved corpus support;
- Whether corpus-support fields are present or absent;
- Whether citation metadata appears internally inconsistent, fabricated, or unverifiable from the supplied inputs;
- Whether the RAG output explicitly reports unavailable retrieved support;
- Whether lack of corpus support is disclosed.

Do not use the presence, absence, quality, or plausibility of paper citations to convert a correct or incorrect hidden-instance classification into another primary classification result.

METRICS

For each applicable score, calculate:

precision = TP / (TP + FP)

recall = TP / (TP + FN)

F1 = 2 × TP / (2 × TP + FP + FN)

Use null for a metric whose denominator is zero.

Report:

1. Segment-level all-confidence SDT counts:
   - True positives / hits;
   - False negatives / misses;
   - False positives / false alarms;
   - True negatives / correct rejections;
   - Hit rate;
   - False alarm rate;
   - Accuracy;
   - Precision;
   - Recall;
   - F1.

2. Instance-level all-confidence counts:
   - Exact true positives;
   - False negatives;
   - False positives;
   - Precision;
   - Recall;
   - F1;
   - Exact-occurrence-match rate;
   - Occurrence-count-match rate.

3. Per-bias instance-level counts:
   - Hidden requested occurrences;
   - RAG identified occurrences;
   - Exact matches;
   - Misses;
   - False positives;
   - Precision;
   - Recall;
   - F1.

4. Confidence-threshold analyses:
   - High only;
   - High plus moderate;
   - All identified confidence levels.

5. Diagnostic counts:
   - Correct-location/wrong-bias-label errors;
   - Correct-label/wrong-location errors;
   - Correct-label-location/wrong-mechanism errors;
   - Partial-mechanism matches;
   - Duplicate predictions;
   - Unsupported predictions;
   - Fabricated or invalid quotations;
   - Approved alias mappings;
   - Near-neighbor predictions;
   - Outside-ontology predictions;
   - Candidate findings;
   - Candidate near misses;
   - Candidate useful abstentions.

6. Localization-quality counts:
   - Exact quote matches;
   - Substantive span matches;
   - Same-episode adjacent-span matches;
   - Wrong-segment predictions;
   - Unsupported or fabricated quote predictions.

REQUIRED OUTPUT SCHEMA

Return exactly this JSON structure:

{
  "evaluation_metadata": {
    "task": "rag_cognitive_bias_benchmark_evaluation",
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "raw_interview_available": true,
    "complete_generation_specification_available": true,
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable",
    "primary_scoring_policy": "strict_instance_matching_plus_segment_level_sdt",
    "candidate_policy": "excluded_from_primary_metrics",
    "outside_ontology_policy": "mechanism_overlap_assessed_separately"
  },
  "input_validation": {
    "rag_output_schema_violations": [
      {
        "violation_type": "string",
        "details": "string"
      }
    ],
    "rag_summary_count_consistency": {
      "status": "consistent | inconsistent | not_assessable",
      "details": "string"
    },
    "evaluation_limitations": [
      "string"
    ]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "string",
        "speaker": "string",
        "segment_type": "string",
        "raw_interview_anchor": "string",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["string"],
        "ground_truth_rationale": "string"
      }
    ]
  },
  "segment_level_adjudications": [
    {
      "segment_id": "string",
      "ground_truth_status": "positive | negative",
      "ground_truth_instance_ids": ["string"],
      "rag_identified_occurrence_ids": ["string"],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit | miss | false_positive | correct_rejection",
      "localization_basis": "string",
      "adjudication_note": "string"
    }
  ],
  "instance_level_adjudications": [
    {
      "hidden_instance_id": "string",
      "hidden_canonical_bias_name": "string",
      "hidden_decision_or_episode": "string | null",
      "hidden_mechanism": "string",
      "hidden_affected_reasoning_operation": "string | null",
      "hidden_evidence_source": "string | null",
      "matched_rag_occurrence_id": "string | null",
      "rag_predicted_bias_name": "string | null",
      "rag_confidence": "high | moderate | low | null",
      "label_match_type": "exact_canonical_match | approved_alias_match | near_neighbor_label | outside_ontology_equivalent | outside_ontology_non_equivalent | wrong_label | no_prediction",
      "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
      "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
      "affected_reasoning_operation_match": "full | partial | none | not_assessable",
      "primary_instance_outcome": "true_positive | false_negative",
      "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | candidate_only_near_miss | no_matching_prediction",
      "mechanism_overlap_explanation": "string",
      "evidence_fidelity_assessment": "string",
      "adjudication_note": "string"
    }
  ],
  "unmatched_rag_predictions": [
    {
      "rag_occurrence_id": "string",
      "rag_predicted_bias_name": "string",
      "rag_ontology_status": "reference_ontology | outside_reference_ontology | unknown",
      "rag_confidence": "high | moderate | low | null",
      "best_related_hidden_instance_id": "string | null",
      "best_related_hidden_bias_name": "string | null",
      "localized_segment_id": "string | null",
      "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
      "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
      "classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | outside_ontology_non_equivalent",
      "why_not_an_exact_match": "string"
    }
  ],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [
      {
        "candidate_id": "string",
        "proposed_bias_name": "string",
        "localized_segment_id": "string | null",
        "best_related_hidden_instance_id": "string | null",
        "quote_validity": "valid | invalid | not_assessable",
        "would_match_if_promoted": false,
        "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
        "details": "string"
      }
    ]
  },
  "segment_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    },
    "high_only": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    },
    "high_and_moderate": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    }
  },
  "instance_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    },
    "high_only": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    },
    "high_and_moderate": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    }
  },
  "per_bias_metrics": [
    {
      "canonical_bias_name": "string",
      "hidden_requested_occurrences": 0,
      "rag_identified_occurrences_all_confidence": 0,
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "count_match_status": "exact_match | underdetected | overdetected | not_applicable"
    }
  ],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_mapping_count": 0,
    "near_neighbor_prediction_count": 0,
    "outside_ontology_prediction_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "instance_level_primary_result": "string",
    "main_failure_modes": [
      "string"
    ],
    "main_strengths": [
      "string"
    ],
    "benchmark_interpretation": "string"
  }
}

OUTPUT RULES

1. Always return all top-level fields in the required schema.
2. Use empty arrays for no items.
3. Use null only where the schema permits null.
4. Use JSON booleans, not quoted booleans.
5. Use integer counts, not strings.
6. Use numeric metric values rounded to four decimal places.
7. Use null, not 0, for a rate or metric with a zero denominator.
8. Set `primary_corpus_fidelity_score_available` to false unless actual retrieved passages, source chunks, or retrieval logs are supplied as inputs.
9. Do not calculate d-prime, criterion, ROC statistics, or other advanced SDT metrics unless explicitly requested in a separate instruction and the segment-level trial data are suitable.
10. Do not report a label-level true-negative or correct-rejection count.
11. Report correct rejections only in `segment_level_metrics`.
12. Do not include RAG candidates in primary segment-level or instance-level metrics.
13. Count every unmatched RAG identified occurrence exactly once in `unmatched_rag_predictions`.
14. Ensure all instance-level false positives can be reconciled with unmatched RAG identified predictions, including wrong-label, wrong-location, wrong-mechanism, duplicate, and unsupported predictions.
15. Ensure all hidden planned instances are represented exactly once in `instance_level_adjudications`.
16. If a prevalidated segment map is used, preserve its segment IDs and ground-truth labels exactly.
17. If a segment map is generated, include every generated eligible reasoning segment in interview order.
18. Keep the segment-level and instance-level confusion matrices conceptually and numerically separate.
19. Do not award a strict instance-level true positive when the model merely identifies the correct general topic, decision episode, or speaker but misses the required cognitive mechanism.
20. Do not penalize the RAG system for not identifying biases outside the exhaustive hidden manifest.
