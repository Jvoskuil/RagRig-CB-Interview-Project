"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "initial evidence interpretation and urgency",
        "raw_interview_anchor": "My first reaction was 'there it is again' ... the seepage rate was within MEL tolerance historically ... we were also five days from a contractual deadline ... I wanted to move quickly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Eligible rationale about initial reaction, tolerance history, and urgency, but not itself a complete hidden manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "pattern classification and deferral choice",
        "raw_interview_anchor": "Once I saw the third one lined up with the first two, it read to me as confirmation ... I deferred it under MEL rather than pulling it into an unscheduled inspection.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_apo_01"
        ],
        "ground_truth_rationale": "The participant treats a third recurrence as a meaningful benign pattern and uses that perceived pattern to justify deferral."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "expert evidence weighting and risk continuity judgment",
        "raw_interview_anchor": "Tomas ... says it's the same seepage pattern ... this fitting type 'just seeps, it doesn't fail badly' ... that carries weight ... the junior engineer's torque and seal check felt like duplicating effort.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_norm_01",
          "AV7_exp_01"
        ],
        "ground_truth_rationale": "The same decision episode contains both the continuity assumption about benign fitting behavior and tenure-based substitution of expert judgment for structured analysis."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "automated evidence acceptance",
        "raw_interview_anchor": "Green status for that defect category, fleet-wide ... I referenced it directly in the disposition memo ... I didn't dig into the calculation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_aut_01"
        ],
        "ground_truth_rationale": "The fleet-average dashboard is accepted as authoritative without checking tail-specific recurrence coverage."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "confidence calibration from source convergence",
        "raw_interview_anchor": "Between the dashboard and Tomas's read, everything was pointing the same direction ... it felt like two independent checks agreeing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_iov_01"
        ],
        "ground_truth_rationale": "Confidence is increased by apparent convergence of sources that were not independently validated against the tail-specific history."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "release authorization and follow-up choice",
        "raw_interview_anchor": "MRO's engineering support had already left ... the seepage was still within tolerance ... I authorized release to service ... flagged a borescope recheck ... but didn't make it mandatory before dispatch.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an eligible release rationale, but the hidden manifestations are mapped to the later self-assessment and aircraft-specific outcome projection."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "self-assessment of deadline influence",
        "raw_interview_anchor": "Other managers might let a deadline push them into a call they're not comfortable with. I don't think that happened here ... the schedule was in the background ... I don't experience it as something that colors my technical judgment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_bbs_01"
        ],
        "ground_truth_rationale": "The participant generalizes susceptibility to deadline pressure to other managers while exempting the own final technical judgment."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "case-specific outcome probability judgment",
        "raw_interview_anchor": "Fifteen years at this airline, and I've never seen this exact fitting fail badly on any tail. That history made me comfortable that this one would be fine, even with the root cause investigation still technically open.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV7_opt_01"
        ],
        "ground_truth_rationale": "Failure-free personal history is projected onto this unresolved aircraft-specific case as confidence in a favorable outcome."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "retrospective process correction",
        "raw_interview_anchor": "I'd probably push harder for that fault-tree analysis ... not treat the recurrence pattern alone as settling the question ... a smooth return ... doesn't really tell us whether the process behind it was solid.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective correction is eligible context but is not credited as a contemporaneous hidden manifestation."
      }
    ]
  }
