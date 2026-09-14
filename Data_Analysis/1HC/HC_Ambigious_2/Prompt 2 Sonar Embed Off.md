You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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

<EVALUATION_SEGMENT_MAP>
"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "care_goal",
        "raw_interview_anchor": "To sort out the new finding properly and get her home with a plan that actually made sense given everything else going on with her, not just the one issue.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicit care objective integrating the full clinical situation; no hidden bias occurrence."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_interpretation",
        "raw_interview_anchor": "The admission ECG showed persistent atrial fibrillation... So we didn't actually know if this was a mechanical trip or something with a cardiac or orthostatic component that nobody had chased down.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Balances stroke risk, bleeding risk, renal information, and unresolved fall etiology as clinical evidence."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "action_rationale",
        "raw_interview_anchor": "Given that gap, I asked for a fall-risk assessment and held off committing to a start date until we had more to go on... the literature doesn't give a clean threshold for a case like this.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Deferral is explicitly tied to incomplete diagnostic information and genuine clinical uncertainty."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_verification",
        "raw_interview_anchor": "I didn't have the other patient's details memorized, so I asked the resident to pull what was available before I answered her... which changes the picture substantially.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Verifies a salient comparator instead of treating an anecdote as patient-specific evidence."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_weighting",
        "raw_interview_anchor": "The CHA2DS2-VASc and HAS-BLED numbers hadn't moved — they still leaned toward treating... I asked for one more renal function check before finalizing a dose.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Acknowledges treatment-favoring scores while seeking current dose-relevant renal information."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "discharge_decision",
        "raw_interview_anchor": "She wasn't on anticoagulation yet, so it wasn't drug-related, but the renal result still hadn't come back. I finalized the discharge without starting treatment and arranged outpatient follow-up.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The pending renal result is identified as the decision determinant; the bruise is expressly treated as irrelevant."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "decision_interpretation",
        "raw_interview_anchor": "The lightheadedness before the fall... starting anticoagulation without understanding it felt premature. But I'll be honest, it's a judgment call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explains treatment hesitation through an unresolved possible cause of the fall and acknowledges reasonable disagreement."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "alternatives_and_choice",
        "raw_interview_anchor": "Start the DOAC right away given the score, defer until the lightheadedness was evaluated, or start a reduced empirical dose... mainly because the history felt incomplete rather than because I thought waiting was inherently safer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Considers alternatives and rejects an inaction-based rationale; no omission-bias mechanism is present."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "communication_choice",
        "raw_interview_anchor": "Give the daughter an accurate answer instead of a reassuring guess... I had the resident check before we talked further.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Chooses verification before communicating a clinical comparison."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "tradeoff_rationale",
        "raw_interview_anchor": "It pushed the conversation back a day... But answering her with an unverified comparison seemed worse than the delay.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly weighs communication delay against the risk of giving unsupported information."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "dose_rationale",
        "raw_interview_anchor": "Her creatinine on admission was borderline, and dosing a DOAC on stale numbers... didn't sit right with me. Someone could reasonably argue the scores already justified starting and adjusting later if needed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Uses current renal data for dosing while acknowledging a reasonable alternative."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "experience_based_reasoning",
        "raw_interview_anchor": "Something like it, yes — dosing decisions where the renal number is borderline. It usually comes down to how much runway you have before discharge, and here we had very little.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Connects prior experience to available time without asserting a biased rule."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "evidence_relevance",
        "raw_interview_anchor": "It didn't really change anything clinically since she wasn't on the drug yet. The bigger factor was still the pending renal result.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly rejects an unrelated bruise as confirmatory evidence and identifies the relevant factor."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "Probably, yes — a clear low score would have resolved a lot of the hesitation at the first decision point.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Narrow counterfactual about how clearer fall-risk information would affect the decision."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "Possibly the family conversation would have gone faster, but I don't think it would have changed the actual treatment timing much — the renal question was separate.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Separates the communication effect of comparator details from the independent renal-treatment question."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "retrospective_guidance",
        "raw_interview_anchor": "Chase down unexplained symptoms before they get labeled as routine falls, and don't assume a story about another patient applies to yours without checking the details.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Generalizes evidence-checking lessons and explicitly endorses avoiding unsupported comparison."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative mechanism-first review of the interview for cognitive biases. No retrieved scientific-paper passages were supplied, so candidate bias labels rely on general cognitive-science knowledge rather than corpus support."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Omission bias",
      "alternative_labels": ["Inaction bias", "Status quo bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Discharge decision to withhold anticoagulation despite CHA2DS2-VASc 4 and HAS-BLED 2 favoring treatment",
      "supporting_interview_quote": "On day four, right before discharge, she had a small bruise where blood was drawn. She wasn't on anticoagulation yet, so it wasn't drug-related, but the renal result still hadn't come back. I finalized the discharge without starting treatment and arranged outpatient follow-up, which ended up being three weeks out rather than the two we'd hoped for.",
      "plausible_mechanism": "A preference could be operating in which harm from commission, such as starting anticoagulation and causing bleeding, is treated as more concerning than harm from omission, such as withholding anticoagulation and leaving stroke risk untreated.",
      "why_not_identified": "The transcript does not affirmatively demonstrate a preference for inaction as a cognitive mechanism; the participant offers clinical reasons for deferring treatment—unexplained presyncope before a fall, borderline fall risk, and pending renal function—and explicitly states waiting was not felt to be inherently safer."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Ambiguity aversion",
      "alternative_labels": ["Uncertainty aversion"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial decision to defer anticoagulation start date after new atrial fibrillation diagnosis",
      "supporting_interview_quote": "I went with deferring the start date, mainly because the history felt incomplete rather than because I thought waiting was inherently safer.",
      "plausible_mechanism": "The participant may have favored delaying treatment because the clinical picture contained ambiguous or missing information, a pattern consistent with ambiguity aversion in which decision-makers avoid options with uncertain risks.",
      "why_not_identified": "The interview shows ordinary clinical uncertainty and a reasonable attempt to obtain missing information before acting; it does not clearly show that the participant disproportionately avoided ambiguity relative to known stroke risk."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Response to recent bleeding-complication case on the ward",
      "supporting_interview_quote": "On day two, one of the nurses mentioned that a patient down the hall had a bleeding complication on anticoagulation the month before. My patient's daughter had heard about it and asked me directly how similar the situations were. I didn't have the other patient's details memorized, so I asked the resident to pull what was available before I answered her — turned out that patient had notably worse renal clearance and was also on an antiplatelet, which changes the picture substantially.",
      "plausible_mechanism": "A recent, emotionally salient bleeding event could make anticoagulation-related bleeding more mentally available and thereby distort risk perception, even if the participant ultimately sought more information.",
      "why_not_identified": "The participant appears to recognize the comparison risk, checks objective details, and distinguishes the other patient's situation; there is no affirmative evidence that the salient bleeding case influenced the treatment timing or discharge decision."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "No retrieved scientific-paper passages were provided; candidate labels are based on general cognitive-science knowledge rather than corpus-derived definitions or diagnostic criteria.",
    "The transcript contains substantial clinical uncertainty, information gathering, and risk balancing; those features alone are not classified as cognitive biases under the requested conservative standard.",
    "No positive bias occurrence was identified because the participant did not clearly display a bias-specific mechanism affecting reasoning or action; the stated deferrals were tied to incomplete history, borderline fall risk, and pending renal function."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Ambigious_2_Sonar_off",
  "interview_id": "HC_Ambigious_2",
  "system_prompt_id": "Sonar",
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
