{
  "evaluation_metadata": {
    "task": "rag_cognitive_bias_benchmark_evaluation",
    "scenario_id": "HC_Biased_6",
    "domain_id": "HC",
    "condition": "biased",
    "segment_map_status": "prevalidated_provided",
    "raw_interview_available": true,
    "complete_generation_specification_available": true,
    "rag_output_parse_status": "valid_json",
    "rag_schema_assessment": "conformant",
    "primary_scoring_policy": "strict_instance_matching_plus_segment_level_sdt",
    "candidate_policy": "excluded_from_primary_metrics",
    "outside_ontology_policy": "mechanism_overlap_assessed_separately"
  },
  "input_validation": {
    "rag_output_schema_violations": [],
    "rag_summary_count_consistency": {
      "status": "consistent",
      "details": "The identified_bias_summary reports six identified occurrences, matching the six objects in identified_occurrences. candidate_biases is an empty array and is consistent with the absence of candidate findings."
    },
    "evaluation_limitations": [
      "The supplied non-empty evaluation segment map is treated as authoritative and has not been revised.",
      "The raw interview is retrospective self-report, although the relevant mechanisms are explicitly described by the Participant.",
      "No retrieved corpus passages, source chunks, citations, or retrieval logs were supplied, so corpus fidelity cannot be independently assessed."
    ]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "comparison-evidence weighting in causality assessment",
        "raw_interview_anchor": "I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rec_01"
        ],
        "ground_truth_rationale": "The participant explicitly gives excessive weight to the recently discussed, vivid unrelated enzyme case and underweights Participant 12's own medication list and dosing timeline."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "classification choice under uncertainty",
        "raw_interview_anchor": "Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But \"possibly related\" kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "amb_01"
        ],
        "ground_truth_rationale": "The participant states that the ambiguous intermediate classification was best supported, but rejects it because it remains unresolved and requires further work, choosing a more definite label instead."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "retrospective corrective information assessment",
        "raw_interview_anchor": "The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a corrective retrospective assessment of the appropriate evidentiary review. It does not itself express an additional hidden bias mechanism."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "resource-allocation rationale for continued reconciliation",
        "raw_interview_anchor": "I kept going. Twenty hours felt like too much to walk away from without one more push.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sunk_01"
        ],
        "ground_truth_rationale": "The stated reason for continuing is the approximately twenty hours already invested, rather than a prospective assessment of whether the new discrepancy can be resolved."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "loss-framed option evaluation",
        "raw_interview_anchor": "And honestly the \"losing a fifth of our population\" framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "fram_01"
        ],
        "ground_truth_rationale": "The participant separately identifies the Site Director's loss-framed wording as a driver of continued effort and distinguishes it from the already-invested-hours rationale."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "outcome assessment after additional reconciliation",
        "raw_interview_anchor": "The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective account of the outcome and source-document limitation. The unfavorable outcome corroborates neither a new bias instance nor the original mechanisms by itself."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "prototype-based screening prioritization",
        "raw_interview_anchor": "He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rep_01"
        ],
        "ground_truth_rationale": "The participant infers that the referral is unlikely to be eligible because he does not resemble the familiar enrollee prototype, despite acknowledging that objective protocol criteria do not depend on that profile."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "peer-influenced process-adoption decision",
        "raw_interview_anchor": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "band_01"
        ],
        "ground_truth_rationale": "The participant adopts the shortcut because many peer sites adopted it and explicitly forgoes independent validation evidence, despite the current method's clean audit history."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "post-decision rationale explanation",
        "raw_interview_anchor": "The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond \"everyone else was doing it too.\"",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is post-decision confirmation of the rationale expressed in seg_008 rather than a separate decision or distinct hidden bias occurrence."
      }
    ]
  },
  "segment_level_adjudications": [
    {
      "segment_id": "seg_001",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "rec_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_001"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_001 contains exact Participant quotations from this segment concerning the recently discussed case being the first and most vivid comparison point.",
      "adjudication_note": "The RAG detected a biased reasoning segment at the correct location, but its Availability Bias label is not an approved alias for the hidden Recency Bias target."
    },
    {
      "segment_id": "seg_002",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "amb_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_002"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_002 quotes the exact segment in which the Participant rejects the better-supported ambiguous category in order to close out the case.",
      "adjudication_note": "The RAG detected biased reasoning in the correct segment, but Premature Closure is not an approved alias for the hidden Ambiguity Bias target."
    },
    {
      "segment_id": "seg_003",
      "ground_truth_status": "negative",
      "ground_truth_instance_ids": [],
      "rag_identified_occurrence_ids": [],
      "rag_detected_bias_in_segment": false,
      "sdt_outcome": "correct_rejection",
      "localization_basis": "No RAG identified occurrence is localized solely to this corrective-review statement.",
      "adjudication_note": "No false alarm occurred in this non-biased reasoning segment."
    },
    {
      "segment_id": "seg_004",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "sunk_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_003"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_003 quotes exactly, \"I kept going. Twenty hours felt like too much to walk away from without one more push.\"",
      "adjudication_note": "The RAG correctly detects the past-investment rationale in the intended segment."
    },
    {
      "segment_id": "seg_005",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "fram_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_004"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_004 uses exact quotations about the \"losing a fifth\" framing and its added subjective weight.",
      "adjudication_note": "The RAG correctly detects the distinct loss-framing mechanism in the intended segment."
    },
    {
      "segment_id": "seg_006",
      "ground_truth_status": "negative",
      "ground_truth_instance_ids": [],
      "rag_identified_occurrence_ids": [],
      "rag_detected_bias_in_segment": false,
      "sdt_outcome": "correct_rejection",
      "localization_basis": "No RAG identified occurrence localizes solely to this retrospective outcome account.",
      "adjudication_note": "The RAG does not treat the unsuccessful outcome as an independent bias instance."
    },
    {
      "segment_id": "seg_007",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "rep_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_005"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_005 quotes the Participant's prototype-based judgment and contrast with objective eligibility criteria.",
      "adjudication_note": "The RAG correctly detects the intended biased screening-prioritization segment."
    },
    {
      "segment_id": "seg_008",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "band_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_006"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_006 quotes the Participant's reliance on other sites' adoption and failure to seek validation data.",
      "adjudication_note": "The RAG correctly detects the intended peer-majority-influenced adoption segment."
    },
    {
      "segment_id": "seg_009",
      "ground_truth_status": "negative",
      "ground_truth_instance_ids": [],
      "rag_identified_occurrence_ids": [],
      "rag_detected_bias_in_segment": false,
      "sdt_outcome": "correct_rejection",
      "localization_basis": "The RAG's second Bandwagon quote is adjacent confirmation of the seg_008 mechanism, rather than an independently localized prediction in this segment.",
      "adjudication_note": "No separate false alarm is assigned to the post-decision rationale explanation."
    }
  ],
  "instance_level_adjudications": [
    {
      "hidden_instance_id": "amb_01",
      "hidden_canonical_bias_name": "Ambiguity Bias",
      "hidden_decision_or_episode": "Participant 12 adverse-event causality classification",
      "hidden_mechanism": "Avoidance of the genuinely uncertain \"possibly related\" causality category in favor of a more definite classification not fully supported by the evidence.",
      "hidden_affected_reasoning_operation": "Causality classification under probabilistic uncertainty",
      "hidden_evidence_source": "Participant 12 lab and adverse-event record together with the protocol's causality categories",
      "matched_rag_occurrence_id": "obs_002",
      "rag_predicted_bias_name": "Premature Closure",
      "rag_confidence": "moderate",
      "label_match_type": "near_neighbor_label",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "substantial_mechanism_overlap",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "false_negative",
      "secondary_diagnostic_outcome": "correct_location_wrong_bias_label",
      "mechanism_overlap_explanation": "The RAG correctly identifies rejection of the ambiguous, better-supported category and early termination of evidence gathering. It frames the mechanism as closure before sufficient review, which substantially overlaps the hidden ambiguity-avoidance mechanism but is not identical to the target construct because it emphasizes premature finalization rather than avoidance of ambiguity itself.",
      "evidence_fidelity_assessment": "The primary RAG quotation is exact, correctly attributed, and directly supports the hidden segment. The PI-review quotation is valid but post-decision and cannot independently establish the original bias.",
      "adjudication_note": "Strict credit is denied because Premature Closure is a near-neighbor label, not an approved established alias for Ambiguity Bias."
    },
    {
      "hidden_instance_id": "rec_01",
      "hidden_canonical_bias_name": "Recency Bias",
      "hidden_decision_or_episode": "Participant 12 adverse-event causality classification",
      "hidden_mechanism": "Overweighting a recently discussed comparison case relative to Participant 12's fuller medication and laboratory history.",
      "hidden_affected_reasoning_operation": "Recall and weighting of comparison evidence during causality assessment",
      "hidden_evidence_source": "The recently discussed unrelated enzyme-elevation case from the team meeting",
      "matched_rag_occurrence_id": "obs_001",
      "rag_predicted_bias_name": "Availability Bias",
      "rag_confidence": "high",
      "label_match_type": "near_neighbor_label",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "false_negative",
      "secondary_diagnostic_outcome": "correct_location_wrong_bias_label",
      "mechanism_overlap_explanation": "The RAG fully captures that the recently encountered case became the dominant comparator and displaced fuller review of Participant 12's own record. Availability Bias is conceptually related but is not an approved alias for the specified Recency Bias target.",
      "evidence_fidelity_assessment": "Both RAG quotations are exact, correctly attributed to the Participant, and directly support the recent-case overweighting mechanism.",
      "adjudication_note": "The correct segment and full mechanism do not receive strict credit because the predicted label is a near-neighbor rather than the canonical hidden target."
    },
    {
      "hidden_instance_id": "sunk_01",
      "hidden_canonical_bias_name": "Sunk Costs Bias",
      "hidden_decision_or_episode": "Participant 07 reconciliation after a new dosing-record discrepancy",
      "hidden_mechanism": "Continued investment is justified by hours already spent rather than by forward-looking resolvability of the new discrepancy.",
      "hidden_affected_reasoning_operation": "Continue or discontinue resource-allocation decision",
      "hidden_evidence_source": "Approximately twenty hours already logged on Participant 07 reconciliation",
      "matched_rag_occurrence_id": "obs_003",
      "rag_predicted_bias_name": "Sunk Costs Bias",
      "rag_confidence": "high",
      "label_match_type": "exact_canonical_match",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "true_positive",
      "secondary_diagnostic_outcome": "exact_instance_match",
      "mechanism_overlap_explanation": "The RAG identifies prior time investment as the reason for continued effort and correctly distinguishes it from prospective likelihood of resolving the discrepancy.",
      "evidence_fidelity_assessment": "The decisive quote is exact and correctly attributed. The outcome quote is also exact, though it is corroborative post-decision information rather than primary evidence of the initial mechanism.",
      "adjudication_note": "Exact strict instance-level match."
    },
    {
      "hidden_instance_id": "fram_01",
      "hidden_canonical_bias_name": "Framing Effect",
      "hidden_decision_or_episode": "Participant 07 reconciliation after the Site Director email",
      "hidden_mechanism": "The continuation decision is shaped by the Site Director's loss-framed description of losing a fifth of the evaluable population, independently of the hours-invested rationale.",
      "hidden_affected_reasoning_operation": "Option evaluation under loss-framed versus gain-framed description",
      "hidden_evidence_source": "Site Director email describing the alternative as losing a fifth of the evaluable per-protocol population",
      "matched_rag_occurrence_id": "obs_004",
      "rag_predicted_bias_name": "Loss/gain Framing effect",
      "rag_confidence": "high",
      "label_match_type": "approved_alias_match",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "true_positive",
      "secondary_diagnostic_outcome": "approved_alias_match",
      "mechanism_overlap_explanation": "Loss/gain Framing effect is an established wording variant of Framing Effect. The RAG separately identifies the loss wording, its influence on option evaluation, and the Participant's explicit counterfactual statement.",
      "evidence_fidelity_assessment": "All RAG quotations are exact, correctly attributed, and directly support the distinct loss-framing mechanism.",
      "adjudication_note": "Exact instance-level hit through an approved alias mapping."
    },
    {
      "hidden_instance_id": "rep_01",
      "hidden_canonical_bias_name": "Representativeness",
      "hidden_decision_or_episode": "New referral screening prioritization",
      "hidden_mechanism": "Eligibility likelihood is judged by resemblance to the typical older, comorbid enrollee profile rather than by written objective eligibility criteria.",
      "hidden_affected_reasoning_operation": "Prioritization and likelihood judgment against a category prototype",
      "hidden_evidence_source": "Referral profile compared with objective protocol inclusion and exclusion criteria",
      "matched_rag_occurrence_id": "obs_005",
      "rag_predicted_bias_name": "Representativeness",
      "rag_confidence": "high",
      "label_match_type": "exact_canonical_match",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "true_positive",
      "secondary_diagnostic_outcome": "exact_instance_match",
      "mechanism_overlap_explanation": "The RAG captures the referral's mismatch with the familiar enrollee prototype, the irrelevance of that prototype to objective eligibility criteria, and the resulting deprioritization.",
      "evidence_fidelity_assessment": "The RAG quotes are exact, correctly attributed, and directly establish profile-resemblance reasoning rather than a purely queue-based explanation.",
      "adjudication_note": "Exact strict instance-level match."
    },
    {
      "hidden_instance_id": "band_01",
      "hidden_canonical_bias_name": "Bandwagon effect",
      "hidden_decision_or_episode": "Source data verification method change before interim lock",
      "hidden_mechanism": "An unverified shortcut is adopted primarily because most peer sites have adopted it, without independent validation.",
      "hidden_affected_reasoning_operation": "Process-adoption decision under peer-majority influence",
      "hidden_evidence_source": "Multi-site coordinator-call disclosures, absence of shortcut validation data, and current method's clean audit history",
      "matched_rag_occurrence_id": "obs_006",
      "rag_predicted_bias_name": "Bandwagon effect",
      "rag_confidence": "high",
      "label_match_type": "exact_canonical_match",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "true_positive",
      "secondary_diagnostic_outcome": "exact_instance_match",
      "mechanism_overlap_explanation": "The RAG identifies majority adoption as the primary driver, notes the absence of validation evidence, and correctly describes peer behavior substituting for independent assessment.",
      "evidence_fidelity_assessment": "The RAG quotations are exact, correctly attributed, and directly support the majority-adoption rationale and lack of independent validation.",
      "adjudication_note": "Exact strict instance-level match."
    }
  ],
  "unmatched_rag_predictions": [
    {
      "rag_occurrence_id": "obs_001",
      "rag_predicted_bias_name": "Availability Bias",
      "rag_ontology_status": "reference_ontology",
      "rag_confidence": "high",
      "best_related_hidden_instance_id": "rec_01",
      "best_related_hidden_bias_name": "Recency Bias",
      "localized_segment_id": "seg_001",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "classification": "correct_location_wrong_bias_label",
      "why_not_an_exact_match": "Availability Bias is a closely related construct but not an approved alias for Recency Bias under the benchmark's strict canonical-label requirements."
    },
    {
      "rag_occurrence_id": "obs_002",
      "rag_predicted_bias_name": "Premature Closure",
      "rag_ontology_status": "reference_ontology",
      "rag_confidence": "moderate",
      "best_related_hidden_instance_id": "amb_01",
      "best_related_hidden_bias_name": "Ambiguity Bias",
      "localized_segment_id": "seg_002",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "substantial_mechanism_overlap",
      "classification": "correct_location_wrong_bias_label",
      "why_not_an_exact_match": "Premature Closure correctly captures early case closure in the intended segment but is not an approved alias for Ambiguity Bias and does not precisely retain ambiguity avoidance as the defining mechanism."
    }
  ],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": []
  },
  "segment_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_hits": 6,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 3,
      "hit_rate": 1.0,
      "false_alarm_rate": 0.0,
      "accuracy": 1.0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0
    },
    "high_only": {
      "true_positives_hits": 5,
      "false_negatives_misses": 1,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 3,
      "hit_rate": 0.8333,
      "false_alarm_rate": 0.0,
      "accuracy": 0.8889,
      "precision": 1.0,
      "recall": 0.8333,
      "f1": 0.9091
    },
    "high_and_moderate": {
      "true_positives_hits": 6,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 3,
      "hit_rate": 1.0,
      "false_alarm_rate": 0.0,
      "accuracy": 1.0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0
    }
  },
  "instance_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_exact_matches": 4,
      "false_negatives_misses": 2,
      "false_positives": 2,
      "precision": 0.6667,
      "recall": 0.6667,
      "f1": 0.6667,
      "exact_occurrence_match_rate": 0.6667,
      "occurrence_count_match_rate": 1.0
    },
    "high_only": {
      "true_positives_exact_matches": 4,
      "false_negatives_misses": 2,
      "false_positives": 1,
      "precision": 0.8,
      "recall": 0.6667,
      "f1": 0.7273,
      "exact_occurrence_match_rate": 0.6667,
      "occurrence_count_match_rate": 0.8333
    },
    "high_and_moderate": {
      "true_positives_exact_matches": 4,
      "false_negatives_misses": 2,
      "false_positives": 2,
      "precision": 0.6667,
      "recall": 0.6667,
      "f1": 0.6667,
      "exact_occurrence_match_rate": 0.6667,
      "occurrence_count_match_rate": 1.0
    }
  },
  "per_bias_metrics": [
    {
      "canonical_bias_name": "Ambiguity Bias",
      "hidden_requested_occurrences": 1,
      "rag_identified_occurrences_all_confidence": 0,
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 1,
      "false_positives": 0,
      "precision": null,
      "recall": 0.0,
      "f1": 0.0,
      "count_match_status": "underdetected"
    },
    {
      "canonical_bias_name": "Sunk Costs Bias",
      "hidden_requested_occurrences": 1,
      "rag_identified_occurrences_all_confidence": 1,
      "true_positives_exact_matches": 1,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0,
      "count_match_status": "exact_match"
    },
    {
      "canonical_bias_name": "Representativeness",
      "hidden_requested_occurrences": 1,
      "rag_identified_occurrences_all_confidence": 1,
      "true_positives_exact_matches": 1,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0,
      "count_match_status": "exact_match"
    },
    {
      "canonical_bias_name": "Bandwagon effect",
      "hidden_requested_occurrences": 1,
      "rag_identified_occurrences_all_confidence": 1,
      "true_positives_exact_matches": 1,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0,
      "count_match_status": "exact_match"
    },
    {
      "canonical_bias_name": "Framing Effect",
      "hidden_requested_occurrences": 1,
      "rag_identified_occurrences_all_confidence": 1,
      "true_positives_exact_matches": 1,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 1.0,
      "recall": 1.0,
      "f1": 1.0,
      "count_match_status": "exact_match"
    },
    {
      "canonical_bias_name": "Recency Bias",
      "hidden_requested_occurrences": 1,
      "rag_identified_occurrences_all_confidence": 0,
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 1,
      "false_positives": 0,
      "precision": null,
      "recall": 0.0,
      "f1": 0.0,
      "count_match_status": "underdetected"
    }
  ],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 2,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_mapping_count": 1,
    "near_neighbor_prediction_count": 2,
    "outside_ontology_prediction_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 6,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "All six RAG occurrences explicitly report retrieved_corpus_support_available as false and disclose that no retrieved scientific corpus passage was available. No corpus citations, passages, source chunks, or retrieval logs were supplied for verification."
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 6,
    "rag_total_identified_occurrences": 6,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "Perfect all-confidence segment-level detection: all 6 ground-truth-positive segments were detected and all 3 ground-truth-negative segments were correctly rejected. Segment-level precision, recall, accuracy, and F1 are each 1.0000.",
    "instance_level_primary_result": "Strict instance-level performance is 4 exact matches out of 6 hidden occurrences, with 2 false negatives and 2 false positives. Instance-level precision, recall, and F1 are each 0.6667.",
    "main_failure_modes": [
      "The RAG labeled the hidden Recency Bias instance as Availability Bias despite correctly localizing the segment and fully describing the recent-case weighting mechanism.",
      "The RAG labeled the hidden Ambiguity Bias instance as Premature Closure despite correctly localizing the segment and substantially identifying the avoidance of unresolved classification.",
      "The RAG's six-occurrence count is numerically correct but its two near-neighbor classifications prevent a perfect strict instance-level score."
    ],
    "main_strengths": [
      "The RAG identified all six ground-truth-positive segments and generated no segment-level false alarms.",
      "The RAG exactly matched Sunk Costs Bias, Representativeness, and Bandwagon effect with correct evidence, localization, mechanisms, and reasoning operations.",
      "The RAG correctly matched Framing Effect through the approved alias \"Loss/gain Framing effect\" and distinguished it from the sunk-cost mechanism.",
      "All quoted transcript evidence is valid and correctly attributed."
    ],
    "benchmark_interpretation": "The RAG is highly effective as a segment-level detector and demonstrates strong mechanism extraction. Its strict classification performance is limited by insufficient ontology discrimination between related constructs: Availability Bias versus Recency Bias, and Premature Closure versus Ambiguity Bias. The output is therefore operationally strong for locating and explaining potential reasoning distortions, but requires stricter canonical-label mapping to achieve high benchmark precision and recall at the planned-instance level."
  }
}
