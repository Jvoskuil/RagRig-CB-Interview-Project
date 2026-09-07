{
  "evaluation_metadata": {
    "task": "rag_cognitive_bias_benchmark_evaluation",
    "scenario_id": "HC_Biased_6",
    "domain_id": "HC",
    "condition": "biased",
    "segment_map_status": "generated_not_prevalidated",
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
      "details": "The identified_bias_summary reports five identified occurrences, matching the five objects in identified_occurrences. The stated candidate count also matches the single object in candidate_biases."
    },
    "evaluation_limitations": [
      "No prevalidated evaluation segment map was supplied, so the segment map was generated from the raw interview and hidden specification before RAG-output adjudication.",
      "The raw interview is retrospective self-report, although the required mechanisms are unusually explicit and therefore support localization and mechanism assessment.",
      "No actual retrieved corpus passages, source chunks, or retrieval logs were supplied; corpus-support fields can be audited only for internal consistency, not factual retrieval fidelity."
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
      "localization_basis": "obs_001 uses an exact quote from this segment and accurately localizes the recent, vivid comparison case and reduced review of case-specific evidence.",
      "adjudication_note": "The RAG detected biased reasoning at the correct segment, but the predicted Availability Bias label is a near-neighbor rather than the hidden Recency Bias target."
    },
    {
      "segment_id": "seg_002",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "amb_01"
      ],
      "rag_identified_occurrence_ids": [],
      "rag_detected_bias_in_segment": false,
      "sdt_outcome": "miss",
      "localization_basis": "The only related RAG item is candidate cand_001; candidates are excluded from primary segment-level detection metrics.",
      "adjudication_note": "The RAG recognized the relevant text as a candidate for Premature Closure but did not identify the hidden Ambiguity Bias occurrence."
    },
    {
      "segment_id": "seg_003",
      "ground_truth_status": "negative",
      "ground_truth_instance_ids": [],
      "rag_identified_occurrence_ids": [],
      "rag_detected_bias_in_segment": false,
      "sdt_outcome": "correct_rejection",
      "localization_basis": "No RAG identified occurrence localizes to this corrective-review statement.",
      "adjudication_note": "No false alarm occurred in this non-biased reasoning segment."
    },
    {
      "segment_id": "seg_004",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "sunk_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_002"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_002 quotes, \"Twenty hours felt like too much to walk away from without one more push,\" which exactly matches the segment's primary evidence.",
      "adjudication_note": "The RAG correctly detects and localizes the past-investment rationale."
    },
    {
      "segment_id": "seg_005",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "fram_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_003"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_003 quotes the participant's statement that the \"losing a fifth\" framing stuck with him and altered what he perceived the decision to involve.",
      "adjudication_note": "The RAG correctly detects and localizes the loss-framing mechanism."
    },
    {
      "segment_id": "seg_006",
      "ground_truth_status": "negative",
      "ground_truth_instance_ids": [],
      "rag_identified_occurrence_ids": [],
      "rag_detected_bias_in_segment": false,
      "sdt_outcome": "correct_rejection",
      "localization_basis": "No RAG identified occurrence localizes to the retrospective outcome statement.",
      "adjudication_note": "The RAG does not improperly treat the eventual failure of reconciliation as independent proof of bias."
    },
    {
      "segment_id": "seg_007",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "rep_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_004"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_004 quotes the prototype-versus-objective-criteria contrast from this exact segment.",
      "adjudication_note": "The RAG correctly detects and localizes the profile-resemblance mechanism."
    },
    {
      "segment_id": "seg_008",
      "ground_truth_status": "positive",
      "ground_truth_instance_ids": [
        "band_01"
      ],
      "rag_identified_occurrence_ids": [
        "obs_005"
      ],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit",
      "localization_basis": "obs_005 quotes the participant's explicit reliance on other sites' adoption and failure to seek validation evidence.",
      "adjudication_note": "The RAG correctly detects and localizes peer-majority-driven adoption."
    },
    {
      "segment_id": "seg_009",
      "ground_truth_status": "negative",
      "ground_truth_instance_ids": [],
      "rag_identified_occurrence_ids": [],
      "rag_detected_bias_in_segment": false,
      "sdt_outcome": "correct_rejection",
      "localization_basis": "The statement is adjacent confirmation of the seg_008 rationale, but no separate RAG occurrence is localized here.",
      "adjudication_note": "No false alarm occurred in this non-distinct post-decision explanatory segment."
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
      "matched_rag_occurrence_id": null,
      "rag_predicted_bias_name": null,
      "rag_confidence": null,
      "label_match_type": "no_prediction",
      "localization_match_type": "no_prediction",
      "mechanism_overlap": "no_prediction",
      "affected_reasoning_operation_match": "not_assessable",
      "primary_instance_outcome": "false_negative",
      "secondary_diagnostic_outcome": "candidate_only_near_miss",
      "mechanism_overlap_explanation": "No RAG identified occurrence targets this hidden instance. Candidate cand_001 substantially overlaps the underlying category-avoidance mechanism but uses Premature Closure rather than the target Ambiguity Bias label and is excluded from primary scoring.",
      "evidence_fidelity_assessment": "No identified RAG evidence is available for this instance. The candidate's supporting quote is exact and valid.",
      "adjudication_note": "Miss in strict primary scoring because the RAG did not promote any correct Ambiguity Bias identification."
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
      "mechanism_overlap_explanation": "The RAG accurately describes excessive influence of a recent, vivid comparison case and the resulting underweighting of the participant's own record. However, Availability Bias is not an approved alias for the hidden Recency Bias target under the benchmark's strict label rules.",
      "evidence_fidelity_assessment": "Both RAG quotations are exact raw-interview quotations, correctly attributed to the Participant, and directly support the recent-case weighting mechanism.",
      "adjudication_note": "The segment is correctly detected, but strict instance credit is denied because the canonical label is a near-neighbor rather than the specified Recency Bias construct."
    },
    {
      "hidden_instance_id": "sunk_01",
      "hidden_canonical_bias_name": "Sunk Costs Bias",
      "hidden_decision_or_episode": "Participant 07 reconciliation after a new dosing-record discrepancy",
      "hidden_mechanism": "Continued investment is justified by hours already spent rather than by forward-looking resolvability of the new discrepancy.",
      "hidden_affected_reasoning_operation": "Continue or discontinue resource-allocation decision",
      "hidden_evidence_source": "Approximately twenty hours already logged on Participant 07 reconciliation",
      "matched_rag_occurrence_id": "obs_002",
      "rag_predicted_bias_name": "Sunk Costs Bias",
      "rag_confidence": "high",
      "label_match_type": "exact_canonical_match",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "true_positive",
      "secondary_diagnostic_outcome": "exact_instance_match",
      "mechanism_overlap_explanation": "The RAG identifies the prior twenty-hour investment as the operative reason for continued effort and correctly contrasts that rationale with a prospective expected-value assessment.",
      "evidence_fidelity_assessment": "The RAG quotes are exact, correctly attributed, and include the decisive statement that twenty hours felt too substantial to abandon.",
      "adjudication_note": "Exact strict instance-level match."
    },
    {
      "hidden_instance_id": "fram_01",
      "hidden_canonical_bias_name": "Framing Effect",
      "hidden_decision_or_episode": "Participant 07 reconciliation after the Site Director email",
      "hidden_mechanism": "The continuation decision is shaped by the Site Director's loss-framed description of losing a fifth of the evaluable population, independently of the hours-invested rationale.",
      "hidden_affected_reasoning_operation": "Option evaluation under loss-framed versus gain-framed description",
      "hidden_evidence_source": "Site Director email describing the alternative as losing a fifth of the evaluable per-protocol population",
      "matched_rag_occurrence_id": "obs_003",
      "rag_predicted_bias_name": "Loss/gain Framing effect",
      "rag_confidence": "high",
      "label_match_type": "approved_alias_match",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "true_positive",
      "secondary_diagnostic_outcome": "approved_alias_match",
      "mechanism_overlap_explanation": "Loss/gain Framing effect is an established wording variant of Framing Effect. The RAG separately identifies the loss wording, its added psychological weight, and the counterfactual acknowledgement that a different framing could have changed the decision.",
      "evidence_fidelity_assessment": "All three RAG quotations are exact, correctly attributed, and directly support the distinct loss-framing mechanism.",
      "adjudication_note": "Exact instance-level hit through an approved alias mapping."
    },
    {
      "hidden_instance_id": "rep_01",
      "hidden_canonical_bias_name": "Representativeness",
      "hidden_decision_or_episode": "New referral screening prioritization",
      "hidden_mechanism": "Eligibility likelihood is judged by resemblance to the typical older, comorbid enrollee profile rather than by written objective eligibility criteria.",
      "hidden_affected_reasoning_operation": "Prioritization and likelihood judgment against a category prototype",
      "hidden_evidence_source": "Referral profile compared with objective protocol inclusion and exclusion criteria",
      "matched_rag_occurrence_id": "obs_004",
      "rag_predicted_bias_name": "Representativeness",
      "rag_confidence": "high",
      "label_match_type": "exact_canonical_match",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "true_positive",
      "secondary_diagnostic_outcome": "exact_instance_match",
      "mechanism_overlap_explanation": "The RAG captures each defining element: prototype mismatch, objective criteria unrelated to that prototype, and deprioritization based on perceived poor fit.",
      "evidence_fidelity_assessment": "The RAG's cited statements are exact, correctly attributed, and directly establish the profile-resemblance reasoning.",
      "adjudication_note": "Exact strict instance-level match."
    },
    {
      "hidden_instance_id": "band_01",
      "hidden_canonical_bias_name": "Bandwagon effect",
      "hidden_decision_or_episode": "Source data verification method change before interim lock",
      "hidden_mechanism": "An unverified shortcut is adopted primarily because most peer sites have adopted it, without independent validation.",
      "hidden_affected_reasoning_operation": "Process-adoption decision under peer-majority influence",
      "hidden_evidence_source": "Multi-site coordinator-call disclosures, absence of shortcut validation data, and current method's clean audit history",
      "matched_rag_occurrence_id": "obs_005",
      "rag_predicted_bias_name": "Bandwagon effect",
      "rag_confidence": "high",
      "label_match_type": "exact_canonical_match",
      "localization_match_type": "exact_quote_match",
      "mechanism_overlap": "full_mechanism_match",
      "affected_reasoning_operation_match": "full",
      "primary_instance_outcome": "true_positive",
      "secondary_diagnostic_outcome": "exact_instance_match",
      "mechanism_overlap_explanation": "The RAG identifies majority adoption as the central driver, notes the absence of error-rate validation, and states that social proof substituted for independent evaluation.",
      "evidence_fidelity_assessment": "The RAG quotations are exact, correctly attributed, and directly support the peer-adoption rationale and lack of validation.",
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
      "why_not_an_exact_match": "The RAG fully captures the recent-case overweighting mechanism in the correct segment, but Availability Bias is a related construct rather than an approved established alias for the hidden Recency Bias label."
    }
  ],
  "candidate_analysis": {
    "candidate_count": 1,
    "candidates": [
      {
        "candidate_id": "cand_001",
        "proposed_bias_name": "Premature Closure",
        "localized_segment_id": "seg_002",
        "best_related_hidden_instance_id": "amb_01",
        "quote_validity": "valid",
        "would_match_if_promoted": false,
        "candidate_assessment": "candidate_near_miss",
        "details": "The quote is exact and correctly localized to the participant's rejection of the \"possibly related\" category. Its mechanism substantially overlaps the hidden Ambiguity Bias instance because it identifies avoidance of unresolved uncertainty and early closure. However, Premature Closure is not an approved alias for Ambiguity Bias under the strict benchmark ontology, and the candidate emphasizes workload reduction as an alternative interpretation."
      }
    ]
  },
  "segment_level_metrics": {
    "all_identified_confidence_levels": {
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
    }
  },
  "instance_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_exact_matches": 4,
      "false_negatives_misses": 2,
      "false_positives": 1,
      "precision": 0.8,
      "recall": 0.6667,
      "f1": 0.7273,
      "exact_occurrence_match_rate": 0.6667,
      "occurrence_count_match_rate": 0.8333
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
      "false_positives": 1,
      "precision": 0.8,
      "recall": 0.6667,
      "f1": 0.7273,
      "exact_occurrence_match_rate": 0.6667,
      "occurrence_count_match_rate": 0.8333
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
    }
  ],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 1,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_mapping_count": 1,
    "near_neighbor_prediction_count": 1,
    "outside_ontology_prediction_count": 0,
    "candidate_count": 1,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 1
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 5,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "Each identified occurrence includes corpus-support fields and explicitly states that no retrieved scientific corpus passages were provided. The field retrieved_corpus_support_available is set to true despite the accompanying disclosure that no actual corpus evidence exists, which is semantically awkward but not a fabricated citation claim. No retrieval logs, passages, source chunks, or citations were supplied for independent fidelity verification."
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 6,
    "rag_total_identified_occurrences": 5,
    "rag_total_candidate_biases": 1,
    "segment_level_primary_result": "Strong segment-level detection: 5 of 6 positive reasoning segments were detected, with no false alarms across 3 generated negative segments. Segment-level precision was 1.0000, recall was 0.8333, and F1 was 0.9091.",
    "instance_level_primary_result": "Strict instance-level performance was 4 exact matches out of 6 hidden instances, with 1 unmatched identified prediction and 2 misses. Instance-level precision was 0.8000, recall was 0.6667, and F1 was 0.7273.",
    "main_failure_modes": [
      "The RAG classified the hidden Recency Bias occurrence as Availability Bias. The mechanism and location were correct, but the label is a near-neighbor rather than an approved canonical match.",
      "The RAG did not identify Ambiguity Bias. It treated the relevant category-avoidance statement as a Premature Closure candidate, which is a useful near miss but does not count as an identified target under strict scoring.",
      "The RAG's stated five-occurrence total underdetects the six-occurrence hidden manifest by one occurrence."
    ],
    "main_strengths": [
      "All four exact primary matches use valid, exact participant quotations and correctly identify the relevant decision episode.",
      "The RAG cleanly distinguishes the Participant 07 sunk-cost mechanism from the independent loss-framing mechanism.",
      "The RAG correctly identifies representativeness and bandwagon effect with the required contrast against objective criteria or independent validation evidence.",
      "The RAG does not generate unsupported extra bias findings in generated ground-truth-negative reasoning segments."
    ],
    "benchmark_interpretation": "The system is highly effective at locating biased reasoning and accurately classifies four of the six planned instances. Its principal weakness is ontology-level discrimination among closely related memory-based constructs and between ambiguity avoidance and premature closure. The candidate handling shows partial recognition of the omitted ambiguity mechanism, but the benchmark's strict policy correctly withholds primary credit until the target construct is identified with the appropriate label."
  }
}
