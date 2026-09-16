"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial_triage_reasoning",
        "raw_interview_anchor": "At 6:40 in the morning ... I sent a technician out with a handheld meter right away rather than waiting to see if anything else developed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant treats sensor drift as relevant background but seeks independent field confirmation before classifying the alarm; the hidden zero-bias manifest contains no instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "monitoring_and_cem_timing_reasoning",
        "raw_interview_anchor": "The handheld readings came back elevated but in a grey zone ... schedule a full continuous emissions monitoring pull within a short, defined window rather than letting it drift indefinitely or shutting down that same morning.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant weighs ambiguous evidence, shutdown cost, production timing, and a defined monitoring plan; the hidden zero-bias manifest contains no instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "physical_inspection_target_reasoning",
        "raw_interview_anchor": "I pulled the three-year maintenance history ... I prioritized the gasket line based on the site's own history, and separately scheduled a quick, low-cost check of the valve as a precaution.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly prioritizes the local base rate and labels the valve check as a severity-based precaution; the hidden zero-bias manifest contains no instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "emissions_calculation_decision_setup",
        "raw_interview_anchor": "From there I had to decide how to calculate cumulative emissions, since the outcome affected whether we crossed into reportable territory under our 24-hour notification clock.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This introduces a genuine methodology and reporting decision without expressing a hidden bias mechanism."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "initial_triage_followup_reasoning",
        "raw_interview_anchor": "I looked at the alarm log, noted the drift history, but didn't stop there—I dispatched the technician immediately to get independent field data rather than waiting to see if the alarm cleared on its own.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The follow-up gives an explicit evidence-gathering rationale and contains no hidden bias instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "hypothesis_testing_reasoning",
        "raw_interview_anchor": "The drift history was real, and it made drift a reasonable starting hypothesis, but two false alarms in a month isn't the same as certainty ... test the hypothesis rather than just assume it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant distinguishes a plausible hypothesis from certainty and describes active testing; the hidden manifest is zero-bias."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "cem_timing_evidence_weighting",
        "raw_interview_anchor": "I looked at the grey-zone handheld readings, the cost of a partial shutdown ... we tightened our interim sampling and locked in a specific date for the full pull.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant articulates a bounded workload-and-risk trade-off rather than avoidance of confirmatory data."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "inspection_alternatives_reasoning",
        "raw_interview_anchor": "The maintenance log made the gasket the statistically obvious first stop ... I added a quick valve check as a low-cost precaution, but I was explicit with the team that the log, not the Ohio story, was driving where we started.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant separates likelihood from severity and gives the local maintenance history priority; no hidden instance is present."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "calculation_methodology_reasoning",
        "raw_interview_anchor": "I compared both calculation approaches against the permit language and how we'd handled similar situations in past audits, and picked the one that held up best under that precedent.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The methodology is selected using permit language and audit precedent; the phase-four decision is intentionally undetermined and bias-free."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "calculation_verification_reasoning",
        "raw_interview_anchor": "I logged which specific permit clause it fell under and cross-checked the calculation window against the actual alarm and logger timestamps before finalizing anything.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant makes the calculation traceable to dated evidence and does not express a hidden bias mechanism."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "time_pressure_reasoning",
        "raw_interview_anchor": "It was there throughout ... it mostly meant we had to be efficient about sequencing rather than skipping analysis.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Time pressure is explicitly described as affecting efficiency and sequencing, not as a hidden bias instance."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "confidence_and_uncertainty_reasoning",
        "raw_interview_anchor": "Early on, moderate confidence at best—drift was plausible but unproven ... Clearer field readings on day one would have resolved a lot of that uncertainty sooner.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant reports calibrated uncertainty and identifies what evidence would have changed confidence; no hidden instance is present."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "drift_counterfactual_reasoning",
        "raw_interview_anchor": "If the sensor drift history hadn't existed, I still would have wanted field confirmation before classifying anything.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The counterfactual supports robust evidence-seeking and does not instantiate a hidden bias."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "Ohio_counterfactual_reasoning",
        "raw_interview_anchor": "If you hadn't known about the Ohio incident, do you think your inspection order would have been different? ... I don't think so. The maintenance log was doing the real work there.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant says the salient incident did not drive inspection order; the hidden control manifest contains no bias instance."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "information_value_counterfactual_reasoning",
        "raw_interview_anchor": "The data logger readings from day one ... would have let us move to the teardown that much sooner.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant identifies earlier evidence that would have changed timing, without expressing a hidden bias mechanism."
      }
    ]
  }
