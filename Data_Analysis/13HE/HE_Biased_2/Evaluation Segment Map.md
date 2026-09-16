"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "The panel breaker had visually severe heat damage, that's true. But honestly, what really settled it for me was that this whole setup ... reminded me hard of a case I worked maybe four years back ... So when I saw this layout, my gut said panel, and I went with the panel side first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["inst_01"],
        "ground_truth_rationale": "The participant gives a remembered prior case more weight than a balanced comparison of present panel and fryer evidence when sequencing excavation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_reconstruction",
        "raw_interview_anchor": "She said she smelled an electrical, burning-plastic odor about twenty minutes before she saw flame—and she also mentioned catching a flicker, like a spark, near where the panel is ... That's a strong data point pointing at the panel.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["inst_02"],
        "ground_truth_rationale": "The participant confidently integrates a panel-consistent flicker detail into the tenant's account even though the earlier documented account contained smell only; the inconsistency is later acknowledged."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "resource_allocation_decision",
        "raw_interview_anchor": "The utility inspector had given me an informal, not-yet-written read that leaned panel. I weighed that against the fryer component's condition ... I picked the panel breaker. ... Clear independent radiating burn patterns from the appliance itself. It wasn't a toss-up, but it wasn't locked in either.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification defines this as a genuinely ambiguous, resource-constrained retention decision without an additional named-bias instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "final_classification_decision",
        "raw_interview_anchor": "I went conditional—panel fault primary, fryer malfunction as a documented secondary possibility. A hard determinate call felt premature since the fryer possibility wasn't eliminated, and 'undetermined' felt like it undersold the direction the pattern evidence and the inspector's preliminary read were pointing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification defines this as a deadline-driven classification choice that documents residual uncertainty without an additional named-bias instance."
      }
    ]
  }
