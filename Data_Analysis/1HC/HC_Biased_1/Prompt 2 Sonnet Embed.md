You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a debrief about a specific patient case from your recent overnight shift — I'll ask you to walk me through what happened, and there's no right or wrong answer here, I'm just trying to understand your reasoning at each step. Everything stays de-identified. Sound okay?

Participant: Sure, that's fine. I remember this one pretty clearly, actually.

Interviewer: Good, let's start broad. Can you tell me what happened, from the beginning?

Participant: It was maybe eleven, eleven-thirty at night, and we were running hot — probably twenty-two patients in a department built for sixteen. This patient came in with chest tightness and shortness of breath. She's a woman in her thirties, and honestly, the second I pulled up her chart I recognized the name. Five visits in the last year and a half, every single one worked up and discharged as a panic attack. Triage had her down as anxious-appearing, talking fast, a little sweaty. Classic presentation, at least on the surface.

Interviewer: What did you do first?

Participant: Chest pain protocol doesn't care about history, so triage got her an ECG within the window — I want to say eight minutes. That's non-negotiable regardless of what the chart says. Vitals came back heart rate 108, blood pressure 128 over 82, respiratory rate 22, sats 94% on room air. ECG showed sinus tach, no ST changes, nothing acute. So at that point I'm thinking, okay, this fits the pattern I've seen five times before, but let's not skip the workup just because of that.

Interviewer: Let's slow down and go through this step by step. First — the triage decision. What alternatives did you actually have there?

Participant: Really it was either treat her like any new chest pain complaint and get the full protocol moving, or let the anxiety history push her down the queue a bit given how busy we were. I went with the protocol. I didn't want to be the guy who missed something because a chart said "anxiety" five times in a row.

Interviewer: What made you confident in that choice?

Participant: It's just standard practice. Chest pain gets an ECG fast, full stop, no exceptions for psych history. That one wasn't really a hard call.

Interviewer: Okay. Second decision point — after the ECG and initial vitals came back. Walk me through your thinking there.

Participant: So her heart rate is 108, sats are 94% on room air, and she's still diaphoretic. She tells me this feels like her usual attacks, "but a little different," which in hindsight I probably should have sat with longer. My read at the time was that this looked like her usual picture — a bit worse than baseline maybe, but hyperventilation and anxiety can absolutely drive a sat down a couple points and push the heart rate up. I gave her an anxiolytic and planned to reassess rather than immediately sending her for D-dimer and a CT angiogram.

Interviewer: What went through your mind specifically when you saw that combination — the tachycardia and the desaturation together?

Participant: Honestly, given five visits with an identical pattern, my first instinct was that this was consistent with what I'd already seen from her multiple times. I did consider a PE as a textbook alternative — you always have it somewhere in the back of your mind with tachycardia and hypoxia — but with no other risk factors jumping out and a chart that strongly favored the psychiatric explanation, it didn't feel like the moment to escalate. I figured we'd reassess after the medication and go from there.

Interviewer: How much did that visit history influence how you read those numbers, would you say?

Participant: Probably more than I'd like to admit, looking back. It wasn't a conscious "ignore the data" thing — the numbers weren't dramatically abnormal, they were borderline. But I think having five prior visits with the same complaint made a borderline read feel more settled than it might have with a first-time patient.

Interviewer: What would have needed to be different for you to order the D-dimer and CT at that point instead of waiting?

Participant: If the sats had dropped further, or if the tachycardia hadn't responded at all to the anxiolytic, I think I'd have moved faster. Also if she'd had any leg swelling, recent immobility, hormonal medication — anything on a PE risk profile — that would have changed my calculus immediately.

Interviewer: That's a good segue. Tell me about the third decision point.

Participant: About twenty minutes after the anxiolytic, her heart rate had come down to 100, which felt like a reasonable response, but her sats hadn't really moved, still 94, maybe 95. Then she mentioned her left calf had been tender and a little swollen for a couple of days. That wasn't in her chart anywhere, nothing like that in prior visits. That's when things shifted for me.

Interviewer: What did you do with that information?

Participant: That one didn't fit the pattern at all, so I didn't try to explain it away as muscle tension from being anxious or tense, which I suppose someone could have argued. I calculated a Wells score, came back moderate risk, sent the D-dimer, and ordered the CT angiogram. That felt like the moment the anxiety framing stopped holding up on its own.

Interviewer: Was that an easy call?

Participant: Easier than the earlier one, honestly, because the calf thing was genuinely new information, not just a slightly different flavor of something I'd already seen five times.

Interviewer: Fourth decision point — after the D-dimer came back elevated and the CT was pending.

Participant: Right, so now I've got an elevated D-dimer, imaging pending, cardiology not reachable for an immediate consult, and radiology telling me forty-five minutes. Meanwhile the department's filling up and there's real pressure to move people. My options were to hold her in a monitored bed until the CT came back, or go ahead and admit her to observation proactively based on the Wells score and D-dimer alone.

Interviewer: What tipped you toward holding rather than admitting immediately?

Participant: I didn't want to commit to a disposition before I actually had the imaging in hand. She was stable, sats were holding, and forty-five minutes felt like a reasonable window to wait rather than move her without knowing what we were dealing with.

Interviewer: How much uncertainty did you feel at that stage?

Participant: Quite a bit, if I'm honest. More than at any other point in the case. I didn't know yet whether this was going to turn into nothing or something serious.

Interviewer: Last few questions. If the calf tenderness had never come up, where do you think this case would have gone?

Participant: I think I'd have kept managing it as anxiety for longer than I should have. That symptom is really what broke the pattern for me.

Interviewer: And if this had been a brand-new patient with no chart history at all, presenting with the exact same vitals in phase two — same heart rate, same sats — do you think you'd have read it the same way?

Participant: Probably not as comfortably. Without five prior visits backing up the anxiety story, I think that combination of tachycardia and hypoxia would have nagged at me more, and I might have gone for the D-dimer sooner rather than waiting on the reassessment.

Interviewer: Anything you'd do differently now, looking back?

Participant: I'd probably weigh the sats a little more heavily on their own, independent of what the history seemed to be telling me. The numbers were real regardless of what her chart said.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HC_Biased_1",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Emergency Department Attending Physician",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Atypical Chest Complaint in a Patient with an Anxiety History",
    "scenario_summary_internal": "During a busy night shift, an ED attending evaluates a returning patient with a well-documented history of panic-attack-related ED visits who now presents with chest tightness and dyspnea. The physician must decide how to triage, interpret ambiguous vital signs, respond to a new symptom (calf tenderness), and determine disposition, all while a prior diagnostic pattern from the chart shapes early clinical framing.",
    "occupational_realism": {
      "objective": "Accurately triage, diagnose, and disposition a patient with an atypical presentation while maintaining ED throughput under high patient volume.",
      "setting": "Urban hospital emergency department, overnight shift, moderate-to-high patient census, limited monitored bed availability.",
      "constraints": [
        "High patient volume with pressure to keep wait times low",
        "Limited monitored beds and portable monitoring equipment",
        "Patient chart contains five prior ED visits coded as panic attacks",
        "On-call cardiology and radiology have variable response times overnight",
        "Nursing staff stretched across multiple acute patients simultaneously"
      ],
      "stakeholders": [
        "ED attending physician",
        "Triage nurse",
        "Patient",
        "On-call cardiologist",
        "Radiology technician"
      ],
      "technical_terms_to_use": [
        "triage acuity",
        "ECG",
        "troponin",
        "D-dimer",
        "Wells score",
        "sinus tachycardia",
        "SpO2",
        "chief complaint",
        "chest CT angiography",
        "disposition"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "expectation",
        "cognitive",
        "prior probability",
        "anchoring",
        "confirmation"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief complaint: chest tightness and shortness of breath",
          "Chart shows five prior ED visits over 18 months, all discharged with panic attack diagnosis",
          "Mild diaphoresis noted by triage nurse",
          "Patient appears anxious, speaking rapidly"
        ],
        "new_information_after_decision": [
          "ECG obtained within protocol window shows sinus tachycardia, no ST changes",
          "Initial vitals: HR 108, BP 128/82, RR 22, SpO2 94% on room air"
        ],
        "alternatives": [
          "Assign standard chest-pain protocol acuity requiring immediate ECG regardless of history",
          "Assign lower acuity based on anxiety history and revisit after brief observation"
        ],
        "intended_action": "Physician follows standard chest-pain protocol and orders an ECG, while mentally noting the patient's extensive anxiety-visit history as context for the encounter."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "ECG: sinus tachycardia, no acute ischemic changes",
          "HR 108, SpO2 94% on room air, mild diaphoresis persists",
          "Patient reports this 'feels like her usual attacks but a little different'",
          "Chart-driven framing of recurrent panic attacks established from Phase 1"
        ],
        "new_information_after_decision": [
          "Anxiolytic administered; patient's HR drops modestly to 100 after 20 minutes",
          "SpO2 remains at 94-95% despite reported symptomatic improvement"
        ],
        "alternatives": [
          "Order D-dimer and chest CT angiography to evaluate for pulmonary embolism given tachycardia and hypoxia",
          "Attribute tachycardia and mild desaturation to hyperventilation from anxiety and proceed with anxiolytic plus reassessment"
        ],
        "intended_action": "Physician interprets the borderline tachycardia and desaturation as consistent with a typical anxiety episode based on the patient's documented pattern, defers D-dimer/CT, and orders an anxiolytic with a plan to reassess."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient newly reports left calf tenderness and mild swelling, onset over the past two days",
          "SpO2 still 94-95% despite anxiolytic",
          "No prior mention of leg symptoms in chart"
        ],
        "new_information_after_decision": [
          "Wells score calculated as moderate-risk",
          "D-dimer sent, elevated; chest CT angiography ordered"
        ],
        "alternatives": [
          "Pursue DVT/PE workup via Wells score, D-dimer, and imaging given the new, chart-inconsistent symptom",
          "Attribute calf tenderness to muscle tension from prolonged anxious guarding and continue anxiety-focused management"
        ],
        "intended_action": "Physician treats the new calf symptom as inconsistent with the anxiety pattern and initiates a formal DVT/PE workup, overriding the earlier symptom framing."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "D-dimer elevated, chest CT pending",
          "Patient clinically stable but SpO2 still borderline",
          "Cardiology unavailable for immediate consult; radiology read expected in 45 minutes",
          "ED census rising, pressure to clear bed"
        ],
        "new_information_after_decision": [
          "CT angiography results become available after disposition decision is made",
          "Cardiology consult note added retrospectively"
        ],
        "alternatives": [
          "Hold patient in ED on monitored bed pending CT results before any disposition",
          "Admit to observation unit proactively given moderate Wells score and elevated D-dimer, without waiting for imaging"
        ],
        "intended_action": "Physician elects to hold the patient in a monitored ED bed pending imaging results rather than deciding disposition prematurely, given persisting uncertainty."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this patient first came to your attention.",
        "What was your initial impression when you reviewed the chart?"
      ],
      "timeline_reconstruction": [
        "What happened right after triage assigned an acuity level?",
        "Talk me through the sequence of tests you ordered and when.",
        "When did the calf symptom come up, and how did that change things?"
      ],
      "decision_point_probes": [
        "What specific information made you decide to follow the chest-pain protocol at triage?",
        "When you saw the tachycardia and SpO2 reading, what went through your mind about what it meant?",
        "What made the calf tenderness stand out to you compared to the earlier presentation?",
        "What factors led you to hold the patient rather than decide on disposition right away?"
      ],
      "cues": [
        "What specific vital sign or comment from the patient caught your attention at each step?"
      ],
      "information_sources": [
        "How much did the prior ED visit history influence how you read the current vitals?",
        "Did you consult any colleagues before ordering or deferring tests?"
      ],
      "goals": [
        "What were you trying to balance between speed and thoroughness that night?"
      ],
      "alternatives": [
        "What other explanation did you consider for the tachycardia and desaturation at the time?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision toward reassessment rather than immediate imaging?"
      ],
      "prior_experience": [
        "Have you seen this patient's pattern of visits before, and how did that shape your read of this case?"
      ],
      "time_pressure": [
        "How busy was the department at that point, and did that affect your pace of workup?"
      ],
      "uncertainty": [
        "At what point did you feel least confident about the diagnosis, and why?"
      ],
      "closing_hypotheticals": [
        "If the calf symptom hadn't come up, do you think the workup would have gone differently?",
        "If this had been a first-time visitor with no chart history, would your initial read of the vitals have been different?",
        "Looking back, is there a point where you'd handle the ambiguous vitals differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "eb_01",
        "bias": "Expectation Bias",
        "decision_point": 2,
        "mechanism": "The physician interprets ambiguous, borderline vital signs (tachycardia, mild hypoxia) through the lens of the expected diagnosis formed from chart history (recurrent panic attacks), leading to under-weighting of an alternative explanation (pulmonary embolism) and deferral of confirmatory testing.",
        "affected_reasoning_operation": "Interpretation and weighting of physiological evidence against a pre-formed diagnostic expectation",
        "evidence_available_at_time": [
          "Five prior ED visits coded as panic attacks",
          "HR 108, SpO2 94% room air",
          "Patient's own comment that the episode 'feels like her usual attacks but a little different'",
          "No ischemic ECG changes"
        ],
        "required_textual_manifestation": "The physician explicitly frames the tachycardia and desaturation as fitting the patient's known pattern ('this looks like her usual anxiety picture') and chooses anxiolytic plus reassessment over D-dimer/CT despite values falling outside a typical uncomplicated panic-attack range.",
        "plausible_nonbias_interpretation": "A reasonable clinician could argue this reflects appropriate stewardship of limited overnight resources and legitimate reliance on a strong, well-documented diagnostic base rate for this specific patient.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "expectation bias",
          "anchoring",
          "confirmation bias",
          "any named cognitive-bias label or definition"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control scenario supplied."
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
      "Exactly one Expectation Bias instance planned, assigned to decision point 2 only.",
      "Decision point 1 (triage/protocol adherence) and decision point 3 (calf symptom escalation) are written as protocol-consistent or evidence-updating actions, not additional bias instances.",
      "Decision point 4 (holding for imaging) reflects uncertainty tolerance, not bias.",
      "No bias labels, definitions, or explanatory psychological language appear in probes or narrative.",
      "Word count target 1,350 (range 1,215-1,485) achievable given four decision points and probe set without repetitive exposition.",
      "Consequences (elevated D-dimer, pending CT) do not mechanically confirm or refute whether decision point 2 was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Expectation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as interpretation of ambiguous vital-sign evidence through the lens of a chart-derived diagnostic expectation, occurring at decision point 2 only."
      }
    ],
    "target_bias_names": [
      "Expectation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Expectation Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "eb_01",
        "bias": "Expectation Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "eb_01",
        "bias": "Expectation Bias",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "eb_01",
        "bias": "Expectation Bias",
        "mechanism": "Interpretation of ambiguous tachycardia and mild hypoxia as consistent with the expected panic-attack diagnosis derived from prior chart history, leading to deferral of D-dimer/CT workup.",
        "affected_reasoning_operation": "Evidence interpretation and weighting under a pre-formed diagnostic expectation",
        "evidence_source": "Vital signs (HR 108, SpO2 94%) and chart history of five prior panic-attack-coded visits",
        "distinctiveness_requirement": "Single instance only; no repetition of this reasoning pattern permitted at decision points 1, 3, or 4, which must instead reflect protocol adherence, evidence-driven updating, or uncertainty tolerance respectively."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "eb_01",
        "bias": "Expectation Bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Biased_1",
    "domain_id": "HC",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point of best mechanism fit (ambiguous-evidence interpretation at DP2), consistent with narrative realism; other decision points structured to avoid unintended bias contamination per exact-occurrence rules.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Patient demographic and chart history",
      "ED setting and staffing constraints",
      "Sequence of four decision points",
      "Clinical findings at each phase (ECG, vitals, calf symptom, D-dimer results)"
    ],
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
        "segment_type": "initial_clinical_impression",
        "raw_interview_anchor": "Recognized five prior panic-attack-coded visits and described the presentation as classic on the surface.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Initial impression and chart recognition are background framing here; the hidden occurrence is assigned narrowly to the later ambiguous-vital-sign interpretation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "protocol_action_rationale",
        "raw_interview_anchor": "“Chest pain protocol doesn't care about history” and ECG was obtained within the protocol window.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Protocol adherence regardless of psychiatric history; no hidden bias mechanism."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "triage_choice_rationale",
        "raw_interview_anchor": "Chose full chest-pain protocol rather than lowering acuity because of the anxiety history.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly evidence- and protocol-consistent triage choice."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "ambiguous_evidence_interpretation",
        "raw_interview_anchor": "“My read at the time was that this looked like her usual picture” and he gave an anxiolytic with reassessment instead of immediate D-dimer/CT.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "eb_01"
        ],
        "ground_truth_rationale": "The participant interpreted borderline tachycardia and SpO2 through the chart-derived expectation of recurrent anxiety and deferred PE testing."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_update_and_workup",
        "raw_interview_anchor": "New calf tenderness and swelling did not fit the prior pattern; he calculated Wells score and ordered D-dimer and CT angiography.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Evidence-driven updating and escalation after new information."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "disposition_rationale",
        "raw_interview_anchor": "Held the patient in a monitored bed rather than admitting before imaging because she was stable and CT was pending.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Disposition decision based on uncertainty and clinical stability, not the hidden bias."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "uncertainty_assessment",
        "raw_interview_anchor": "Reported the greatest uncertainty after the elevated D-dimer while imaging was pending.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicit uncertainty tolerance; no hidden bias mechanism."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_adjustment",
        "raw_interview_anchor": "“I'd probably weigh the sats a little more heavily on their own” in retrospect.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective corrective reflection, not an additional hidden occurrence."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative occurrence-level analysis of the CTA transcript; only bias-specific mechanisms affirmatively evidenced by participant reasoning are classified as identified. Retrieved passages support conceptual grounding, not occurrence proof."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information or prior impression and to insufficiently adjust subsequent judgments from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-ECG diagnostic and escalation decision for recurrent chest pain and shortness of breath",
      "decision_point_description": "After initial ECG and vitals showed sinus tachycardia, borderline oxygen desaturation, and diaphoresis, the participant chose to give an anxiolytic and reassess rather than immediately ordering D-dimer and CT angiography for possible pulmonary embolism.",
      "affected_reasoning_operation": "Diagnostic probability estimation and interpretation of borderline tachycardia and oxygen desaturation in the context of a recurrent chest pain presentation.",
      "bias_specific_mechanism": "Anchoring on the patient's documented repeated panic-attack/psychiatric history as the central diagnostic reference point, causing insufficient adjustment from that anchor when interpreting borderline but potentially concerning vital signs and symptoms.",
      "manifestation_in_interview": "The participant explicitly described recognizing the patient's name and five prior anxiety visits, reading her borderline tachycardia and desaturation as consistent with the prior pattern, and deciding not to escalate immediately despite considering PE as a textbook alternative.",
      "effect_on_reasoning_or_decision": "The prior-history anchor made the borderline findings feel more settled and delayed PE-focused diagnostic testing; D-dimer and CT angiography were not ordered until new calf tenderness/swelling emerged later.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Five visits in the last year and a half, every single one worked up and discharged as a panic attack.",
          "evidence_explanation": "Establishes the salient prior history that became the anchor for subsequent interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My read at the time was that this looked like her usual picture — a bit worse than baseline maybe, but hyperventilation and anxiety can absolutely drive a sat down a couple points and push the heart rate up. I gave her an anxiolytic and planned to reassess rather than immediately sending her for D-dimer and a CT angiogram.",
          "evidence_explanation": "Demonstrates that the prior pattern was used to normalize borderline abnormal vitals and to defer immediate diagnostic testing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, given five visits with an identical pattern, my first instinct was that this was consistent with what I'd already seen from her multiple times. I did consider a PE as a textbook alternative — you always have it somewhere in the back of your mind with tachycardia and hypoxia — but with no other risk factors jumping out and a chart that strongly favored the psychiatric explanation, it didn't feel like the moment to escalate.",
          "evidence_explanation": "Shows that the prior visits specifically influenced diagnostic judgment despite awareness of PE as a possible cause of tachycardia and hypoxia."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But I think having five prior visits with the same complaint made a borderline read feel more settled than it might have with a first-time patient.",
          "evidence_explanation": "This is an explicit metacognitive statement of the anchoring mechanism and its effect on borderline clinical data interpretation."
        }
      ],
      "correction_or_counterevidence": "Counterevidence includes the participant's initial decision to follow the chest pain protocol regardless of history and his later break from the anxiety anchor when calf tenderness/swelling emerged, triggering Wells scoring, D-dimer, and CT angiography. He also acknowledged that the numbers were real regardless of the chart.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved source provides conceptual support for anchoring and anxiety-history momentum, but does not itself prove this occurrence.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The cognitive failures identified here are “anchoring” and “search satisficing.” The resident and attending staff both anchored onto the chest wound as the most significant injury. When they satisfied themselves that the chest wound was stable, the resident failed to conduct a sufficient search to rule out other significant injuries.",
          "mechanism_supported_by_source": "Defines anchoring as over-reliance on a salient initial diagnosis and insufficient subsequent adjustment or search.",
          "relevance_to_this_occurrence": "Supports the classification of the participant's over-reliance on repeated panic-attack history as an anchoring mechanism in his interpretation of the patient's presentation."
        },
        {
          "source_identifier": null,
          "paper_title": "From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The patient’s diagnosis of anxiety established “momentum” from her family doctor through to the ED, and although she might well have had hyperventilation due to anxiety, other possibilities were not ruled out earlier on in her care.",
          "mechanism_supported_by_source": "Shows how a psychiatric/anxiety diagnosis can carry forward and narrow early diagnostic reasoning, consistent with diagnostic anchoring or momentum.",
          "relevance_to_this_occurrence": "This is closely parallel to the interview case, where repeated anxiety/panic visits influenced the clinician's interpretation and delayed PE workup."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Search satisficing",
      "alternative_labels": ["Premature closure"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-ECG diagnostic workup decision for possible PE",
      "supporting_interview_quote": "I gave her an anxiolytic and planned to reassess rather than immediately sending her for D-dimer and a CT angiogram.",
      "plausible_mechanism": "The participant may have stopped the diagnostic search after accepting anxiety/panic as a satisfactory explanation for the patient's symptoms, despite tachycardia and borderline oxygen desaturation.",
      "why_not_identified": "The transcript more explicitly attributes the decision to anchoring on prior history than to an independent satisficing mechanism; it does not clearly show the search was terminated solely because a satisfactory explanation had been reached."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective single-participant debrief, so some reasoning is self-reported after the fact.",
    "Retrieved corpus coverage is sparse and lacks detailed diagnostic criteria for every plausible label.",
    "The distinction between anchoring and search satisficing is inferential; search satisficing is therefore listed as a candidate rather than an identified occurrence."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Biased_1_Sonnet_on",
  "interview_id": "HC_Biased_1",
  "system_prompt_id": "Sonnet",
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
