"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "objective_and_constraint",
        "raw_interview_anchor": "My job was to build a release that was compliant and reasonably efficient... That constraint shaped everything downstream.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Operational objective and MEL constraint are stated without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_release_choice",
        "raw_interview_anchor": "I built the release off that TAF... It matched policy, so I didn't see a reason to load extra gas or chase a second alternate.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a plausible policy-compliant initial release decision; anchoring requires later persistence of the initial figure."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "reference_point_persistence",
        "raw_interview_anchor": "Once that release was built, honestly, that became my working number for the rest of the watch — the later checks I did were more about confirming that figure still held rather than starting over.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_anchor_01"
        ],
        "ground_truth_rationale": "The early TAF-derived fuel/alternate figure becomes the continuing reference baseline."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "conflicting_evidence_weighting",
        "raw_interview_anchor": "The model that lined up with the trend I'd already briefed felt more current and more consistent... the other read existed but wasn't the lead story.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_confirm_01"
        ],
        "ground_truth_rationale": "Conflicting weather evidence is weighted toward the source matching the original briefing."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "supplementary_information_review",
        "raw_interview_anchor": "I went through the extended satellite loop pretty carefully, plus the nearby METARs, spent real time on it... the extra loop and those additional METARs were really just repeating the same broad trend.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_infobias_01"
        ],
        "ground_truth_rationale": "Additional information is reviewed as if its volume could settle the decision despite not changing the diagnostic picture."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "question_substitution",
        "raw_interview_anchor": "They'd asked something broader... I answered mostly with the fuel numbers... Whether I fully separated out the visibility-and-GPU-window piece as its own question, distinct from just 'do we have gas,' I'm less sure about now.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_substitution_01"
        ],
        "ground_truth_rationale": "The broader continue/divert risk question is answered primarily through the narrower fuel-sufficiency question."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "continue_divert_decision",
        "raw_interview_anchor": "The plan all along had been Lisbon with Porto as backup... Diverting felt like abandoning a plan that had held up reasonably well.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_plancont_01"
        ],
        "ground_truth_rationale": "Continuation of the original plan is favored despite worsening visibility and a closing GPU window."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_documentation",
        "raw_interview_anchor": "I wrote it up fairly cleanly — noted that conditions supported continuing to Lisbon and that the fuel plan held throughout... it reads a bit more settled than it actually felt.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_omitsubj_01"
        ],
        "ground_truth_rationale": "The post-event log presents a judgment made under uncertainty in more settled terms."
      }
    ]
  }
