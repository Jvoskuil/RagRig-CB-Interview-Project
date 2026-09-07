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

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analyzed the participant's retrospective description of clinical reasoning during one ED case. No experimental condition or hidden metadata was assumed. Retrieved scientific-paper passages were not supplied, so classification rests on interview evidence and conceptual definitions."
  },
  "identified_bias_summary": [
    {
      "canonical_bias_name": "Anchoring Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Confirmation Bias",
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
      "bias_definition": "Anchoring bias occurs when an initial piece of information or an early diagnostic impression disproportionately influences subsequent judgment, with insufficient adjustment away from that anchor in light of new or discordant information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-ECG/vitals interpretation and initial decision not to order D-dimer/CT immediately",
      "decision_point_description": "Whether to escalate to D-dimer and CT angiogram immediately versus give an anxiolytic and reassess after borderline tachycardia and 94% oxygen saturation.",
      "affected_reasoning_operation": "Interpretation of borderline vital signs and diagnostic probability; decision about escalation of chest-pain/dyspnea workup.",
      "bias_specific_mechanism": "The patient's chart history of five prior panic-attack discharges served as an early diagnostic anchor. The participant interpreted the current borderline tachycardia and desaturation as consistent with that anchor and adjusted insufficiently away from it despite objective findings that he later said would have nagged at him in a first-time patient.",
      "manifestation_in_interview": "The participant recognized the patient from five prior anxiety-related visits, interpreted her heart rate and saturation as consistent with her usual picture, and later stated that the prior visits made the borderline read feel more settled than it would have otherwise.",
      "effect_on_reasoning_or_decision": "The initial workup was not escalated to D-dimer and CT after the ECG and borderline vitals; the participant instead gave an anxiolytic and planned reassessment, delaying the D-dimer/CT until new calf symptoms emerged.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "the second I pulled up her chart I recognized the name. Five visits in the last year and a half, every single one worked up and discharged as a panic attack.",
          "evidence_explanation": "Establishes the early diagnostic anchor from prior psychiatric history before the current borderline findings were interpreted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My read at the time was that this looked like her usual picture — a bit worse than baseline maybe, but hyperventilation and anxiety can absolutely drive a sat down a couple points and push the heart rate up.",
          "evidence_explanation": "Shows the current objective findings being interpreted through the prior anxiety anchor rather than as independent evidence requiring escalation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But I think having five prior visits with the same complaint made a borderline read feel more settled than it might have with a first-time patient.",
          "evidence_explanation": "Explicit self-report that the prior history anchor reduced uncertainty about a borderline presentation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without five prior visits backing up the anxiety story, I think that combination of tachycardia and hypoxia would have nagged at me more, and I might have gone for the D-dimer sooner rather than waiting on the reassessment.",
          "evidence_explanation": "Counterfactual statement directly linking the anchor to the decision not to order D-dimer earlier."
        }
      ],
      "correction_or_counterevidence": "The participant initially obtained a timely ECG under chest pain protocol despite the psychiatric history. The anchor was later disrupted by the new report of calf tenderness/swelling, after which he calculated a Wells score, sent a D-dimer, and ordered CT angiography.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the classification is based on the interview evidence and the standard mechanism of anchoring bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "canonical_bias_name": "Confirmation Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Confirmation bias is the tendency to search for, interpret, favor, and recall information in ways that confirm or support one's existing beliefs or hypotheses while giving insufficient weight to disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of the patient's statement that the episode felt 'a little different' and of borderline objective findings",
      "decision_point_description": "Whether to treat the patient's report and borderline vitals as still consistent with the anxiety diagnosis or as signals that the working diagnosis might be insufficient.",
      "affected_reasoning_operation": "Interpretation of a disconfirming patient statement and ambiguous clinical findings; assessment of fit with the existing anxiety hypothesis.",
      "bias_specific_mechanism": "The participant favored the existing anxiety hypothesis when processing ambiguous evidence. He acknowledged that the patient's 'a little different' statement should have been explored further and characterized the abnormal vitals as only borderline, thereby minimizing disconfirming cues.",
      "manifestation_in_interview": "The participant heard the patient say the episode was 'a little different' but still read the presentation as her usual picture, and described the numbers as not dramatically abnormal, allowing the anxiety framing to remain dominant.",
      "effect_on_reasoning_or_decision": "Reinforced the decision to delay D-dimer/CT and treat with an anxiolytic first, because ambiguous or mildly disconfirming information was absorbed into the existing anxiety explanation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "She tells me this feels like her usual attacks, 'but a little different,' which in hindsight I probably should have sat with longer.",
          "evidence_explanation": "Identifies a disconfirming cue in the patient's own report that was not fully explored at the time."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The numbers weren't dramatically abnormal, they were borderline.",
          "evidence_explanation": "Shows ambiguous objective findings being interpreted in a way that minimized concern under the existing anxiety hypothesis."
        }
      ],
      "correction_or_counterevidence": "Later, when the patient reported left calf tenderness and swelling, the participant recognized this as not fitting the pattern, avoided explaining it away, calculated a Wells score, sent a D-dimer, and ordered CT angiography.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the classification is based on the interview evidence and the standard mechanism of confirmation bias.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_name": "Hindsight Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Retrospective evaluation of the earlier decision to delay D-dimer/CT",
      "supporting_interview_quote": "I'd probably weigh the sats a little more heavily on their own, independent of what the history seemed to be telling me. The numbers were real regardless of what her chart said.",
      "plausible_mechanism": "After learning of the calf tenderness and elevated D-dimer, the participant may now view the earlier borderline SpO2 and tachycardia as more clearly warranting earlier escalation than they appeared at the time.",
      "why_not_identified": "The interview does not clearly show the participant now believes the outcome was predictable in advance or that he 'knew it all along'; the statements could reflect ordinary reflective learning rather than a distorted retrospective judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were available, so corpus support for identified occurrences is absent and classification relies on interview evidence and standard bias definitions.",
    "The interview is a retrospective self-report, so the reasoning described may be filtered by memory and later reflection.",
    "The final clinical outcome is not fully specified beyond an elevated D-dimer and pending CT, limiting outcome-related bias assessment."
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
