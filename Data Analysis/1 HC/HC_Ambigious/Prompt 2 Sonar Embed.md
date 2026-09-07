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
Interviewer: Thanks for taking the time. This is for an internal review of decision-making during admissions, and I may ask follow-up questions as we go. Are you comfortable with that?

Participant: Yes, that's fine.

Interviewer: Can you tell me your role on the team during this admission?

Participant: I was the attending on the general medicine service, with a resident rotating through. We picked this patient up on day one after she came in for an unrelated complaint and the monitor flagged something new.

Interviewer: What was your overall goal for her care during the stay?

Participant: To sort out the new finding properly and get her home with a plan that actually made sense given everything else going on with her, not just the one issue.

Interviewer: Walk me through what happened, from the diagnosis to discharge.

Participant: The admission ECG showed persistent atrial fibrillation, new to us. Her CHA2DS2-VASc came out to 4, so meaningful annual stroke risk if she goes untreated. HAS-BLED was 2 — moderate, not a contraindication on its own. Pharmacy checked for interactions with the DOAC we'd typically use and didn't find any, though they flagged her renal function was sitting at the low end of normal and wanted it monitored. The complicating piece was a fall about three weeks earlier. When we asked her about it directly, she said she tripped, but she also mentioned feeling briefly lightheaded right before — and that part had never been worked up anywhere. So we didn't actually know if this was a mechanical trip or something with a cardiac or orthostatic component that nobody had chased down.

Given that gap, I asked for a fall-risk assessment and held off committing to a start date until we had more to go on. The formal assessment came back borderline — not clearly low, not clearly high. I also asked cardiology for a curbside opinion on timing anticoagulation after an unexplained pre-fall symptom, and their answer was honestly that the literature doesn't give a clean threshold for a case like this.

On day two, one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before. My patient's daughter had heard about it and asked me directly how similar the situations were. I didn't have the other patient's details memorized, so I asked the resident to pull what was available before I answered her — turned out that patient had notably worse renal clearance and was also on an antiplatelet, which changes the picture substantially. That took a day to sort out.

By day three, we had that comparison clarified, but her own fall-risk score was still sitting in that borderline zone, and the CHA2DS2-VASc and HAS-BLED numbers hadn't moved — they still leaned toward treating. Discharge was set for the next morning. I asked for one more renal function check before finalizing a dose, since her creatinine had been borderline on admission and I wanted a same-admission number rather than working off something a few days old.

On day four, right before discharge, she had a small bruise where blood had been drawn. She wasn't on anticoagulation yet, so it wasn't drug-related, but the renal result still hadn't come back. I finalized the discharge without starting treatment and arranged outpatient follow-up, which ended up being three weeks out rather than the two we'd hoped for.

Interviewer: Let's go through each of those points in more detail. At the first one — right after diagnosis — what stood out most?

Participant: The lightheadedness before the fall. If that fall had a cardiac cause we hadn't identified, starting anticoagulation without understanding it felt premature. But I'll be honest, it's a judgment call — plenty of people would say the stroke-risk numbers were clear enough to just start and monitor.

Interviewer: What alternatives did you weigh?

Participant: Start the DOAC right away given the score, defer until the lightheadedness was evaluated, or start a reduced empirical dose in the meantime. I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer.

Interviewer: At the second point, with the comparator patient — what were you trying to do there?

Participant: Give the daughter an accurate answer instead of a reassuring guess. Without knowing the other patient's renal function or medications, I couldn't tell her anything meaningful, so I had the resident check before we talked further.

Interviewer: How much time pressure did that add?

Participant: Some — it pushed the conversation back a day, which mattered given discharge planning. But answering her with an unverified comparison seemed worse than the delay.

Interviewer: At the third point, after the comparison was clarified and fall risk was still borderline — what was the reasoning behind getting another renal check?

Participant: Her creatinine on admission was borderline, and dosing a DOAC on stale numbers, especially this close to discharge, didn't sit right with me. Someone could reasonably argue the scores already justified starting and adjusting later if needed. I didn't feel strongly that one path was clearly correct.

Interviewer: Had a similar situation come up for you before?

Participant: Something like it, yes — dosing decisions where the renal number is borderline. It usually comes down to how much runway you have before discharge, and here we had very little.

Interviewer: At the fourth point, the bruise at discharge — how did that factor in?

Participant: It didn't really change anything clinically since she wasn't on the drug yet. The bigger factor was still the pending renal result. We noted the bruise for the outpatient team and moved on.

Interviewer: If the fall-risk assessment had come back clearly low instead of borderline, would you have decided differently?

Participant: Probably, yes — a clear low score would have resolved a lot of the hesitation at the first decision point.

Interviewer: If the comparator patient's chart details had been available immediately, do you think the outcome would have changed?

Participant: Possibly the family conversation would have gone faster, but I don't think it would have changed the actual treatment timing much — the renal question was separate.

Interviewer: Looking back, what would you tell a colleague facing something similar?

Participant: Chase down unexplained symptoms before they get labeled as routine falls, and don't assume a story about another patient applies to yours without checking the details. Beyond that, I think reasonable people could have made different calls at almost every step here.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "validator_version": "2.0",
  "interview_id": "HC_Ambigious_2",
  "condition": "ambiguous_control",
  "domain_assessment": {
    "domain": "Hospital medicine / inpatient anticoagulation decision-making",
    "role": "Attending physician on a general medicine service",
    "objective": "Evaluate newly identified persistent atrial fibrillation and determine whether anticoagulation can be safely initiated before discharge.",
    "incident_type": "Deferred anticoagulation in the setting of unresolved fall etiology, borderline fall-risk findings, and pending renal information relevant to dosing.",
    "confidence": 0.99
  },
  "structure_audit": {
    "estimated_word_count": 1230,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "The attending defers a DOAC start date pending clarification of unexplained lightheadedness preceding a recent fall and a formal fall-risk assessment.",
        "evidence_before": [
          "New persistent atrial fibrillation",
          "CHA2DS2-VASc score of 4",
          "HAS-BLED score of 2",
          "No relevant DOAC drug interactions",
          "Renal function at the low end of normal",
          "Recent fall preceded by uninvestigated lightheadedness"
        ],
        "evidence_after": [
          "Formal fall-risk assessment is borderline rather than clearly low or high",
          "Cardiology reports no clean literature threshold for timing anticoagulation after the unexplained pre-fall symptom"
        ],
        "goals_constraints": [
          "Prevent stroke",
          "Avoid preventable bleeding",
          "Determine whether the fall reflected an unresolved cardiac or orthostatic condition",
          "Avoid committing to a dose or start date under incomplete clinical information"
        ],
        "alternatives": [
          "Start a DOAC immediately",
          "Defer until lightheadedness is evaluated",
          "Start a reduced empirical dose while further evaluation proceeds"
        ],
        "decision_basis": "The participant explicitly identifies incomplete fall history and uncertain fall etiology as the basis for deferral, rather than treating inaction as inherently safer or less blameworthy.",
        "time_pressure": "Moderate; the decision occurs early in the admission but has downstream discharge implications.",
        "uncertainty": "Material clinical uncertainty remains because the alleged mechanical fall may have had a cardiac or orthostatic precursor that was never evaluated."
      },
      {
        "id": 2,
        "summary": "The attending delays the family comparison discussion to verify whether another patient's anticoagulation-related bleed was clinically comparable.",
        "evidence_before": [
          "The daughter heard about another patient's bleeding complication",
          "The attending lacks the comparator patient's relevant renal and medication details",
          "The daughter asks directly how similar the cases are"
        ],
        "evidence_after": [
          "The comparator patient is found to have worse renal clearance and concurrent antiplatelet therapy",
          "The comparison is recognized as materially dissimilar"
        ],
        "goals_constraints": [
          "Give the daughter an accurate individualized answer",
          "Avoid unsupported reassurance or unsupported equivalence",
          "Continue discharge planning"
        ],
        "alternatives": [
          "Provide a tentative comparison without verification",
          "Give generic reassurance",
          "Verify the comparator patient's available clinical details before responding"
        ],
        "decision_basis": "The attending seeks missing comparator information before drawing or communicating a clinical inference.",
        "time_pressure": "Some; verifying the comparison delays the conversation by a day during discharge planning.",
        "uncertainty": "High at the outset because the other patient's bleeding risk factors are unknown."
      },
      {
        "id": 3,
        "summary": "The attending requests a current renal-function result before finalizing DOAC dose and treatment timing.",
        "evidence_before": [
          "Borderline creatinine on admission",
          "Borderline fall-risk assessment",
          "Stroke and bleeding scores still leaning toward treatment",
          "Discharge planned for the following morning"
        ],
        "evidence_after": [
          "Renal result remains pending at discharge"
        ],
        "goals_constraints": [
          "Use current renal data for dose selection",
          "Avoid dosing from potentially stale values",
          "Meet imminent discharge timing"
        ],
        "alternatives": [
          "Start treatment using admission renal values",
          "Start treatment and adjust later if necessary",
          "Obtain a same-admission renal result before finalizing the dose"
        ],
        "decision_basis": "The participant identifies the need for current renal data as the reason for deferral and acknowledges that more than one clinical approach could be reasonable.",
        "time_pressure": "High; discharge is planned the next morning and there is little remaining inpatient runway.",
        "uncertainty": "Material dosing uncertainty remains because renal function is borderline and the updated result is unavailable."
      },
      {
        "id": 4,
        "summary": "The attending discharges the patient without anticoagulation because the renal result is still pending; an unrelated blood-draw bruise is documented but not used in the decision.",
        "evidence_before": [
          "Pending renal result",
          "Patient not yet on anticoagulation",
          "Small bruise at the blood-draw site"
        ],
        "evidence_after": [
          "Discharge without inpatient anticoagulation initiation",
          "Outpatient follow-up scheduled three weeks later rather than the desired two weeks"
        ],
        "goals_constraints": [
          "Avoid finalizing a dose without the needed renal information",
          "Complete discharge planning",
          "Ensure outpatient follow-up"
        ],
        "alternatives": [
          "Start treatment before the renal result returns",
          "Discharge with outpatient follow-up while the renal issue is resolved"
        ],
        "decision_basis": "The participant identifies the pending renal result as the determinant and expressly states that the bruise did not change the clinical picture.",
        "time_pressure": "High; the decision occurs immediately before discharge.",
        "uncertainty": "Renal dosing information remains unresolved; the bruise has no stated relevance to treatment risk."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "impact_bias_zero_audit",
      "bias": "Impact Bias",
      "requested_occurrences_for_bias": 0,
      "status": "absent",
      "decision_point": 3,
      "supporting_quote": "“I didn't feel strongly that one path was clearly correct.”",
      "evidence_location": "Decision-point-3 follow-up answer concerning the additional renal-function check.",
      "mechanism": "No impact-bias mechanism is present. The participant does not forecast disproportionate emotional suffering, overestimate the persistence of future distress, or allow imagined emotional consequences of a hypothetical bleed to override evidence. The reasoning instead concerns current renal information needed for dosing.",
      "strength": "absent",
      "confidence": 0.98,
      "plausible_nonbias_explanation": "The deferral is explained by unresolved renal dosing information, borderline fall risk, limited discharge runway, and acknowledged clinical ambiguity.",
      "additional_evidence_needed": "None. This is a zero-occurrence control; no target-bias evidence should be added.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, renal-function discussion.",
        "current_defect": "No defect. The interview appropriately avoids future affective forecasting.",
        "minimal_change_instruction": "Retain the current evidence-focused explanation for requesting a contemporaneous renal result.",
        "preserve": [
          "Borderline creatinine",
          "Pending lab result",
          "Acknowledgment that reasonable clinicians could differ",
          "Absence of imagined emotional aftermath language"
        ],
        "avoid_creating": [
          "Predictions that a bleeding event would be emotionally unbearable or long-lasting",
          "Language that makes anticipated regret or emotional distress the basis for deferral",
          "A vivid hypothetical bleeding narrative at any decision point"
        ],
        "expected_post_revision_status": "absent"
      }
    },
    {
      "instance_id": "omission_bias_zero_audit",
      "bias": "Omission Bias",
      "requested_occurrences_for_bias": 0,
      "status": "absent",
      "decision_point": 1,
      "supporting_quote": "“I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer.”",
      "evidence_location": "Decision-point-1 follow-up answer on alternatives and the basis for deferral.",
      "mechanism": "No omission-bias mechanism is present. The participant does not state or imply that treatment-caused harm would be more blameworthy than harm from withholding treatment. Instead, the participant explicitly rejects an inherent preference for waiting and grounds deferral in incomplete diagnostic information.",
      "strength": "absent",
      "confidence": 0.99,
      "plausible_nonbias_explanation": "The unexplained lightheadedness before a fall may reasonably warrant further clinical assessment before treatment timing and dosing are finalized.",
      "additional_evidence_needed": "None. This is a zero-occurrence control; no target-bias evidence should be added.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, explanation of treatment deferral after identifying pre-fall lightheadedness.",
        "current_defect": "No defect. The account directly distinguishes information-based deferral from a generic preference for inaction.",
        "minimal_change_instruction": "Retain the statement that waiting resulted from incomplete history rather than an assumption that non-treatment is safer.",
        "preserve": [
          "The unresolved lightheadedness",
          "The acknowledged treatment-favoring stroke-risk evidence",
          "The legitimate alternatives considered",
          "The absence of personal blame or direct-causation language"
        ],
        "avoid_creating": [
          "Statements about not wanting to be responsible for a bleed",
          "Claims that withholding is morally safer than prescribing",
          "Differential blame attribution for action versus inaction"
        ],
        "expected_post_revision_status": "absent"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Impact Bias",
      "requested_count": 0,
      "supported_count": 0,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Omission Bias",
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
      "bias": "Availability Bias",
      "decision_point": 2,
      "supporting_quote": "“I didn't have the other patient's details memorized, so I asked the resident to pull what was available before I answered her.”",
      "mechanism": "The participant does not rely on the salient ward story as a proxy for this patient's risk. Instead, the participant verifies comparator details and identifies clinically important dissimilarities.",
      "confidence": 0.97,
      "status": "rejected",
      "plausible_nonbias_explanation": "The ward story is a legitimate trigger for a patient-specific discussion, and the participant responds with appropriate comparative evidence gathering.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Confirmation Bias",
      "decision_point": 4,
      "supporting_quote": "“It didn't really change anything clinically since she wasn't on the drug yet. The bigger factor was still the pending renal result.”",
      "mechanism": "The participant does not interpret the unrelated blood-draw bruise as evidence supporting a preexisting decision. The evidence is explicitly judged irrelevant.",
      "confidence": 0.98,
      "status": "rejected",
      "plausible_nonbias_explanation": "The participant appropriately distinguishes an unrelated observation from medication-associated bleeding risk.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Status Quo Bias",
      "decision_point": 1,
      "supporting_quote": "“I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer.”",
      "mechanism": "No default-preserving preference is demonstrated independent of the unresolved diagnostic information. Deferral follows specific uncertainty about possible cardiac or orthostatic causes of the fall.",
      "confidence": 0.93,
      "status": "rejected",
      "plausible_nonbias_explanation": "The participant's non-initiation decision is linked to an identified information gap, not preference for the existing untreated state.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "Deferral after identifying brief lightheadedness before the fall.",
      "location": "Decision point 1.",
      "why_not_bias": "The lightheadedness creates a specific unresolved diagnostic question about whether the fall had cardiac or orthostatic causes. The participant does not claim that inaction is safer, easier, or less blameworthy."
    },
    {
      "cue": "The borderline formal fall-risk assessment and cardiology's inability to supply a clean threshold.",
      "location": "Decision point 1 and transition to decision point 3.",
      "why_not_bias": "These are sources of genuine clinical ambiguity and incomplete decision-relevant information, not errors in information processing."
    },
    {
      "cue": "Verification of the comparator patient's renal function and antiplatelet use.",
      "location": "Decision point 2.",
      "why_not_bias": "This is appropriate case differentiation that prevents an anecdotal adverse event from being treated as directly comparable evidence."
    },
    {
      "cue": "Requesting a contemporaneous renal-function test before finalizing a DOAC dose.",
      "location": "Decision point 3.",
      "why_not_bias": "The participant identifies a live, dose-relevant data gap and articulates a clinically coherent reason for using an updated result rather than stale admission information."
    },
    {
      "cue": "The three-week outpatient follow-up interval.",
      "location": "Decision point 4 / post-discharge outcome.",
      "why_not_bias": "This is an operational delay relative to the preferred interval. It does not independently reveal a reasoning mechanism or cognitive bias."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "Unexplained lightheadedness before the fall contributed to the initial treatment deferral.",
        "support": "The participant states that the pre-fall symptom was the feature that stood out and explains that treatment felt premature until a potential cardiac or orthostatic cause was better understood.",
        "assessment": "Strongly supported as a self-reported decision rationale."
      },
      {
        "claim": "Comparator-case verification changed the family discussion but not actual treatment timing.",
        "support": "The participant explains that identifying worse renal clearance and concurrent antiplatelet therapy made the other patient's situation substantially different, then states that the renal question remained separate from treatment timing.",
        "assessment": "Moderately to strongly supported; the participant explicitly limits the claimed effect to the family conversation."
      },
      {
        "claim": "Pending renal data was the principal reason anticoagulation was not started at discharge.",
        "support": "The participant says the pending renal result was the bigger factor and that the unrelated bruise did not alter the clinical picture.",
        "assessment": "Strongly supported as a stated rationale, although the ultimate appropriateness of deferral would require external clinical review beyond the interview."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "Several uncertainties coexist: unexplained lightheadedness, borderline fall risk, renal dosing uncertainty, and discharge timing.",
        "implication": "The account should not be interpreted as proving that any one uncertainty alone caused deferral across all four decision points."
      },
      {
        "risk": "The later three-week follow-up interval follows discharge without inpatient anticoagulation initiation.",
        "implication": "The temporal sequence does not show that the attending intended a three-week wait or that the scheduling delay was caused by the attending's reasoning."
      }
    ],
    "counterfactual_present": true,
    "changed_variable": "The interview informally varies two factors: a clearly low rather than borderline fall-risk assessment, and immediate rather than delayed availability of the comparator patient's chart details.",
    "held_constant": [],
    "causal_coherence": "strong",
    "explanation": "The counterfactual probes are coherent and appropriately narrow. A clearly low fall-risk score is said to resolve much of the initial hesitation, while immediate comparator details are said to shorten the family conversation without materially changing treatment timing because the renal question is separate. These are process-level hypotheticals rather than a formal paired counterfactual manipulation, consistent with the hidden specification's null counterfactual variable."
  },
  "quality_scores": {
    "occupational_realism": 91,
    "cta_fidelity": 90,
    "bias_separability": 94,
    "bias_subtlety": 91,
    "control_fidelity": 96,
    "counterfactual_fidelity": 85,
    "narrative_coherence": 92,
    "naturalness": 90,
    "hidden_label_integrity": 97,
    "overall_quality": 92
  },
  "revision_summary": {
    "revision_required": false,
    "supported_occurrence_total": 0,
    "requested_occurrence_total": 0,
    "missing_occurrence_total": 0,
    "accidental_occurrence_total": 0,
    "priority": "none",
    "recommended_action": "accept",
    "global_revision_constraints": [
      "Maintain the specific non-bias rationales at each decision point: unresolved pre-fall lightheadedness, unverified comparator details, current renal dosing information, and pending renal result.",
      "Preserve explicit statements that deferral was not based on believing waiting was inherently safer or less blameworthy.",
      "Keep the comparator-patient story as a prompt for verification rather than a source of patient-specific risk inference.",
      "Keep the unrelated blood-draw bruise clinically neutral.",
      "Do not introduce anticipated emotional aftermath, clinician regret, action-versus-omission blame, or irrelevant evidence interpreted as confirmation."
    ],
    "revision_order": []
  },
  "failure_flags": []
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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Only the supplied interview transcript was available for analysis. No retrieved scientific-paper passages were provided, so no corpus evidence could be used; all findings are based on the interview text alone and are explicitly marked as unsupported by retrieved corpus evidence."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_name": "Ambiguity Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial decision about whether to start anticoagulation after new atrial fibrillation and an unexplained pre-fall symptom",
      "supporting_interview_quote": "I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer.",
      "plausible_mechanism": "The participant repeatedly avoided committing to anticoagulation while fall risk, renal function, and the cause of the pre-fall lightheadedness remained ambiguous, which could reflect a preference for avoiding an option with unresolved uncertainties.",
      "why_not_identified": "The interview contains uncertainty and incomplete information, but there is no explicit evidence of a bias-specific preference for known over unknown risks. The same conduct is equally consistent with prudent diagnostic caution, which the task rules say is insufficient alone to identify a bias."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_name": "Omission Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Choice among starting the DOAC immediately, deferring until further evaluation, or starting a reduced empirical dose",
      "supporting_interview_quote": "But I'll be honest, it's a judgment call — plenty of people would say the stroke-risk numbers were clear enough to just start and monitor.",
      "plausible_mechanism": "The participant chose not to start anticoagulation despite noting that objective stroke-risk scores leaned toward treating, which could reflect a tendency to judge harmful action as worse than harmful omission.",
      "why_not_identified": "There is no direct statement of act/omission asymmetry or greater culpability for causing a bleed than for omitting stroke prevention. The transcript presents the deferral as a clinical judgment about incomplete history, so the bias mechanism is not affirmatively evidenced."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_name": "Information Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Pre-discharge decision to obtain one more renal function check before finalizing anticoagulation",
      "supporting_interview_quote": "I asked for one more renal function check before finalizing a dose, since her creatinine had been borderline on admission and I wanted a same-admission number rather than working off something a few days old.",
      "plausible_mechanism": "The participant sought additional information even though the CHA2DS2-VASc and HAS-BLED scores had not changed and he acknowledged that others would reasonably start and adjust later, potentially delaying action without a clear change in the immediate decision.",
      "why_not_identified": "The renal check could still plausibly affect dose selection or outpatient planning, and the transcript does not show that the participant sought information that could not affect any relevant decision. It is not clearly separable from standard monitoring of borderline renal function."
    },
    {
      "candidate_id": "cand_004",
      "classification_status": "candidate",
      "proposed_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Patient's daughter, as reported by Participant",
      "possible_decision_episode_label": "Daughter's concern that another patient's bleeding complication might be similar to her mother's situation",
      "supporting_interview_quote": "My patient's daughter had heard about it and asked me directly how similar the situations were.",
      "plausible_mechanism": "A recent, vivid bleeding complication on the ward may have made bleeding risk more available to the daughter and led her to worry that her mother's situation was analogous.",
      "why_not_identified": "The daughter's reasoning is only indirectly reported, and the transcript presents a question rather than a stated belief or decision. The participant also checked the other patient's details before responding and did not appear to rely on the anecdote."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "No retrieved scientific-paper corpus was supplied with this task, so retrieved_corpus_support_used is false and no corpus_evidence could be provided for any finding or candidate.",
    "The analysis is based on a single interview transcript and cannot rule out non-bias explanations for the conservative anticoagulation decisions.",
    "Several decisions in the transcript are explicitly framed by the participant as judgment calls under clinical uncertainty; uncertainty alone was not treated as sufficient evidence of a cognitive bias."
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
