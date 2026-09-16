"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "goal-setting rationale",
        "raw_interview_anchor": "Mainly to see if we could shortcut months of remediation work by adopting something pre-built and compliant, given the clock we were on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A deadline-driven goal and reasonable motivation for evaluating outside tooling; it does not itself express one of the hidden bias mechanisms."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial pilot-scope decision",
        "raw_interview_anchor": "After that call I told my VP I thought we should move fast and pilot the full token set across both squads rather than cherry-picking pieces, because the overall quality bar felt high enough that a narrower test seemed like it'd just slow us down.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "The participant generalized the vivid, polished demo's overall evaluative frame to the full library before independently reviewing it, matching the hidden Priming effect instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "cross-attribute quality inference",
        "raw_interview_anchor": "Not directly, no — we hadn't run our own contrast checks yet. But the accordion was so well executed, and given the awards and the fact that two competitors already ship with it, I figured the token layer was probably in similarly good shape.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "A positive impression of the accordion and vendor reputation was used to infer the quality of unverified contrast and elevation tokens, matching Halo effect."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "licensing-tier comparison",
        "raw_interview_anchor": "Mostly that Team was a bad deal — you're paying almost Enterprise money for a fraction of the components and worse support. Enterprise looked obviously better sitting next to that.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "Enterprise was made disproportionately attractive by comparison with the unattractive Team tier rather than by an independent value calculation, matching Decoy effect."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "rollout timeline and control judgment",
        "raw_interview_anchor": "I set four weeks. Aggressive, but I was going to be hands-on managing the integration personally, syncing daily with both squads. Not formally, no. I figured with me driving it closely day to day, we'd make it work regardless of their existing release calendars.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_04"],
        "ground_truth_rationale": "The participant attributed success of an aggressive timeline to personal oversight despite unconfirmed, uncontrolled squad calendars, matching Illusion of control."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective feasibility assessment",
        "raw_interview_anchor": "Honestly, just asking each squad lead directly, before I set the date, whether four weeks fit their existing commitments. I asked them to work toward it rather than asking if it was feasible first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a hindsight account of information-gathering that would have improved the timeline decision. The hidden instance is mapped to the contemporaneous control judgment; hindsight alone is not separately credited."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "audit discrepancy interpretation",
        "raw_interview_anchor": "My instinct was that these were implementation-specific edge cases — maybe our theming layer interacting oddly with their defaults — rather than the library itself being non-compliant, since the vendor's own documentation states AA compliance. Part of why that explanation felt like the natural one to reach for first was that I'd already told the VP and both squad leads LumenKit would solve most of our contrast problems out of the box, so ‘it's our theming, not their tokens’ sat better with what I'd already said than the alternative did.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_05"],
        "ground_truth_rationale": "The audit findings were reinterpreted in a way that preserved consistency with the participant's earlier public endorsement, matching Cognitive Dissonance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "continue-versus-revert decision",
        "raw_interview_anchor": "We'd already put in over forty engineering hours customizing the tokens to fit our theming, so I decided we should keep refining rather than pause or fall back to legacy. Partly that reverting would mean writing off the hours we'd already put in. It felt more efficient to push through and fix what remained than to start over on a path we already knew worked.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_06"],
        "ground_truth_rationale": "Previously invested engineering hours were used as a reason to continue rather than evaluate the remaining options on forward-looking costs and benefits, matching Sunk Cost Bias."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "final rollout recommendation",
        "raw_interview_anchor": "I recommended continuing largely as we had it, with LumenKit tokens and all, rather than switching to the hybrid setup. Even with the hybrid's technical case being reasonably strong, sticking with what we already had running felt like the safer, known quantity this close to the deadline — everyone on both squads already understood how the current setup behaved, and that familiarity mattered more to me in the moment than moving to an arrangement that was objectively cleaner but still new to the team.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_07"],
        "ground_truth_rationale": "The current implementation was preferred for familiarity and continuity even though the hybrid plan was acknowledged as objectively cleaner, matching Status Quo Bias."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "retrospective closing assessment",
        "raw_interview_anchor": "I'd keep the urgency and the willingness to bring in outside tooling under deadline pressure — that part was right. I'd change how early I locked in public commitments about what the library would solve, and I'd get squad confirmation on timelines before setting them rather than after.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A retrospective account of lessons learned and corrective actions; it does not add a new hidden occurrence."
      }
    ]
  }
