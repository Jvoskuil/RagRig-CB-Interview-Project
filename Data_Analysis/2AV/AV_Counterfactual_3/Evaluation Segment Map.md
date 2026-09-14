"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "context_reasoning",
        "raw_interview_anchor": "Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—it was just less time to work with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This explains operational compression caused by the shortened turnaround but does not itself contain a hidden bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The irregular machinery item was assigned to hold 3 by the automatic load instruction, and the participant issued the ALI as generated because the system had been reliable and time was short; follow-up confirms the available manual chart was not used.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "au_01"
        ],
        "ground_truth_rationale": "Decision point 1 contains the intended automation-bias mechanism: an automated output for atypical cargo was accepted without the situation-specific manual cross-check, with system reliability and schedule compression cited as reasons."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant cleared the 380-kilogram mail and six late bags in aft hold 5 after comparing total weight with three recent LMCs, without calculating the placement-specific index shift.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sub_01"
        ],
        "ground_truth_rationale": "Decision point 2 contains the intended substitution mechanism: aggregate weight similarity was used as an easier proxy for the harder placement-specific index calculation under time scarcity."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant inferred that the rotation was running tail-heavy from the ramp report and two prior aft-trim events, then shifted cargo forward beyond what the current flight's own index required.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ap_01"
        ],
        "ground_truth_rationale": "Decision point 3 contains the intended apophenia/correlation mechanism: a recurring causal pattern was inferred from two temporally adjacent events and used to override valid current-flight data."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The participant signed and released with a one-bag discrepancy after weighing delay risk against the possibility of a routine miscount; the discrepancy was later corrected without changing the W&B conclusion.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Decision point 4 is deliberately neutral and genuinely ambiguous. The participant made an explicit operational risk tradeoff, and either sign-off or a short hold was professionally defensible."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective_recommendation",
        "raw_interview_anchor": "The participant recommended pulling the manual chart for irregular cargo and keeping the current flight's numbers separate from prior flights unless a shared cause is known, while remaining uncertain about the LMC issue.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective recommendation and uncertainty statement, not an additional hidden occurrence."
      }
    ]
  }
