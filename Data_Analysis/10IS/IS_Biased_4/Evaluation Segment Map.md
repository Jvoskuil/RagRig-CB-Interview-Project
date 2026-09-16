"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "vendor_selection_reasoning",
        "raw_interview_anchor": "Participant: Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. ... the contrast between the other two was just so stark that it became the frame I was working from.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant lets the near-priced inferior full-service option frame the choice of Vendor C and does not independently assess whether Vendor A meets the three-flow scope."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "contractor_selection_reasoning",
        "raw_interview_anchor": "Participant: I went with Candidate X. ... if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. ... I looked at the visual work and sort of assumed the rest would follow.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "The participant generalizes prestige and visual polish to unverified documentation and communication abilities, despite Candidate Y's directly relevant process evidence."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "rules_engine_causal_interpretation",
        "raw_interview_anchor": "Participant: The activation numbers on the dashboard ticked up right after. I took it as a sign the adjustments were working. ... I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The participant attributes an underpowered, confounded uptick to their own manual rule changes and acts on that attribution despite the Data lead's warning."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "post_test_uncertainty_update",
        "raw_interview_anchor": "Participant: The uptick partly reversed once the email campaign ended, and she noted the causal driver was still unconfirmed. So it's genuinely unclear how much of that first bump was actually the rule changes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a later uncertainty update that acknowledges reversal and unresolved causality; it contains no hidden manifested bias instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "legacy_component_continuation_reasoning",
        "raw_interview_anchor": "Participant: I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away ... The one-sprint number was probably a better bet purely on cost and risk.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "Past effort is used to justify continuation even though the forward-looking one-sprint migration estimate is better on cost and risk and resolves known defects."
      }
    ]
  }
