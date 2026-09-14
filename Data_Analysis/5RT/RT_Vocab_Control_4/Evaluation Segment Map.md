"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "objective_and_tradeoff",
        "raw_interview_anchor": "Keep the operation safe, but also be realistic about the schedule. We had Q-119, one of our priority intermodal trains, due through that territory later in the day, and there's a contractual on-time window — past two hours late and we take a penalty. On top of that we had a cold front coming that night, about a 25-degree drop, which matters for rail integrity on continuous welded rail. So I'm weighing the defect information against the operational picture, not just one or the other.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly weighs safety, schedule, and cold-weather context; no distorted weighting is manifested."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "I pulled the defect history for that curve. There'd been small flaws there before, mostly on bolted rail nearby, that had stayed flat and never developed into anything. But what stood out this time wasn't just the 4-millimeter reading, it was the rate — doubling in three weeks is faster than anything in that log. I treated that rate as the key new piece of information. Instead of keeping the standard two-week retest, I moved it to an elevated-monitor status with a one-week retest.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The faster growth is treated as new decision-relevant evidence and leads to proportionate retesting, per the control specification."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_threshold_reasoning",
        "raw_interview_anchor": "Two millimeters isn't much on its own, but the speed of the change is what a static reading doesn't tell you. If it had gone from 2 to 2.5, I'd probably have left the interval alone. Doubling in three weeks felt like something that needed a closer look sooner.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains a rate-based evidentiary threshold, not a bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_weighting",
        "raw_interview_anchor": "The two readings, the inspector's comparison to the historical log, the current 60 mile-an-hour track class rating, and his statement that the rate was faster than what we'd typically seen. Nothing pointed to imminent failure, but the trend was enough to justify tightening the interval.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Absence of imminent-failure evidence is distinguished from a trend that justifies a shorter retest."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "I've handled a lot of flaw reports over the years, and my instinct was that this looked like ones that had resolved fine. But the inspector's point about the CWR and tonnage was legitimate — those aren't small distinctions, especially with the cold snap coming. So rather than going with full track speed because it reminded me of past cases, or swinging all the way to a full slow order, I put a targeted, moderate speed restriction on that curve specifically, to hold until the one-week retest.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Experience is weighed against relevant case differences and does not override them. Candidate cand_001's quotation is valid here, but the complete reasoning negates a manifested experience or representativeness bias."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "alternative_comparison",
        "raw_interview_anchor": "Full track speed leaned too much on pattern-matching without accounting for the differences the inspector raised. A full slow order across the segment felt heavier than the data supported — we didn't have evidence of anything beyond the flagged growth rate. The moderate restriction on just that curve matched the actual risk picture.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Both extremes are rejected for stated evidentiary reasons; the selected restriction is proportionate."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "group_decision_rationale",
        "raw_interview_anchor": "It didn't move much, honestly. We talked through the restriction already in place, the penalty exposure if we held the train, and the retest timeline, and the road foreman asked partway through whether the restriction we had was enough given the CWR concern. We talked that through for a minute before agreeing to release under the existing restriction rather than removing it. The call ran close to fifteen minutes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The group reviews relevant factors and an explicit concern before reaching a position consistent with initial views. Candidate cand_002 quotes this segment, but stable consensus alone does not show anchoring."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "group_convergence_reflection",
        "raw_interview_anchor": "Not really. Nobody argued for pulling the restriction, and nobody argued for a full reroute either. We landed close to where people already were.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant describes a non-extreme result consistent with starting positions; no polarization or groupthink is manifested."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "response_to_new_cue",
        "raw_interview_anchor": "A following local crew radioed in an unusual sound at the wheel-rail interface near that stretch — no visible damage, nothing measurable. That triggered a debrief before shift change.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A debrief is initiated in response to an unusual report despite no measurable damage."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "meeting_inclusion_decision",
        "raw_interview_anchor": "Myself, the trainmaster, and the chief dispatcher initially. Our assistant engineer from track engineering asked to join to raise concerns about the classification and the speed decision. The meeting was originally set for fifteen minutes before shift change, but the chief dispatcher pushed it back to bring him in once we heard he wanted to weigh in.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The schedule is adjusted to include an engineering voice, rather than excluding dissent."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "debrief_evidence_and_followup",
        "raw_interview_anchor": "We went through the wheel-rail sound — the read was that it was probably unrelated, likely debris or a joint bar, but nobody stated that with certainty. We confirmed we'd keep the interim restriction in place until the retest, and we logged his specific concerns to revisit at that retest rather than closing them out.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The attribution remains explicitly uncertain and concerns are recorded for later review."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "dissent_handling",
        "raw_interview_anchor": "A bit. He wasn't fully convinced the sound was unrelated, and he wanted the retest moved up further. We didn't move the date, but we agreed to note his concern formally and treat it as open rather than resolved.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Disagreement is retained as an open issue, not erased by apparent consensus."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "alternative_comparison",
        "raw_interview_anchor": "Closing it out quickly without him, which is basically what almost happened before the schedule got adjusted. Or escalating straight to the chief engineer that same day. We didn't think escalation was warranted yet, but documenting it as open with a defined follow-up felt like the right middle ground.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant compares exclusion and immediate escalation and chooses documented follow-up."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "time_pressure_reflection",
        "raw_interview_anchor": "The release call and the debrief were the tightest, tied to the two-hour window and the shift change. The morning classification had more room — that was mainly me and the inspector working through the numbers.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A descriptive assessment of pressure across decision points; pressure alone is not a bias."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "If it had stayed at two weeks, we'd have been relying longer on a single fast-growth data point without a closer check, which is part of why I didn't want to leave it standard.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains the shorter retest using evidence available at the decision."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "Maybe the discussion would have taken a bit longer, but I don't think the restriction itself would have changed much, since we'd already built it in based on his earlier input about the CWR and tonnage.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The engineer's relevant input had already informed the restriction; the hypothetical does not indicate dissent suppression."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "retrospective_process_reflection",
        "raw_interview_anchor": "I'd have looped him in before the meeting was even scheduled, rather than adjusting on the fly once he asked.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This proposes a process improvement for earlier inclusion."
      },
      {
        "segment_id": "seg_018",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "Probably similar, since the restriction came out of the specific data points rather than familiarity with the location. I might have leaned on the inspector's judgment even more, since I wouldn't have my own history with that curve to cross-check against.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hypothetical prioritizes specific data and inspector judgment over familiarity."
      }
    ]
  }
