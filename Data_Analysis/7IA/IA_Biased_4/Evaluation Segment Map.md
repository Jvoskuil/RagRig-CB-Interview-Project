"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "goal_setting",
        "raw_interview_anchor": "My objective was straightforward on paper: figure out whether this was probable sanctions evasion and, if so, get a defensible escalation to compliance and law enforcement before the filing window closed. We had ten business days from the alert.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Goal and deadline; no target bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "contextual_assessment",
        "raw_interview_anchor": "Meridian was the obvious one — the ultimate beneficial owner shared a registered agent with a company from a case I'd worked about eighteen months earlier, which had ended in a successful sanctions-evasion referral. There was also a separate counterparty in the same batch, a logistics firm, that didn't match anything I recognized. And it was a heavy week — alert volume across the team was well above average, so I needed to move efficiently.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Risk cues and workload are stated before allocation of attention."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "initial_scope_choice",
        "raw_interview_anchor": "I scoped the review. Given the registered-agent overlap with the prior case, I focused my initial workup on Meridian and its immediate corporate web — pulling registry filings, past KYC refresh notes, that kind of thing. The logistics counterparty I noted but set aside as lower priority since it didn't fit any typology I'd seen before.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sab_01"
        ],
        "ground_truth_rationale": "Familiar-pattern-driven scoping deprioritizes a relevant entity without independent assessment."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "scope_rationale",
        "raw_interview_anchor": "Honestly, the registered-agent match jumped out immediately. That pattern had been reliable before — same agent, similar shell structure, same region. With the volume we were under that week, I didn't feel I had the bandwidth to give equal weight to an entity that had no connection to anything I'd seen. I did glance at the logistics firm's file, but there was nothing that screamed 'look here,' so I moved on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sab_01"
        ],
        "ground_truth_rationale": "Explicit pattern-based attention allocation and failure to assess the non-matching counterparty; primary location."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "screening_resource_choice",
        "raw_interview_anchor": "I thought about it, but that would've added a day or two, and the Meridian angle felt like the more productive use of time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sab_01"
        ],
        "ground_truth_rationale": "Declining broader screening continues the familiar-pattern concentration."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "retrospective_scope_explanation",
        "raw_interview_anchor": "A few days later it showed an unusual same-day wire pattern — nothing I'd examined at that point. My team lead actually asked why it wasn't in my initial scoping note. I didn't have a great answer beyond 'it didn't fit the pattern I was chasing.'",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sab_01"
        ],
        "ground_truth_rationale": "The participant retrospectively confirms the same pattern-driven omission."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "vendor_evidence_weighting",
        "raw_interview_anchor": "About three days in, our OSINT vendor sent a report concluding Meridian was highly likely tied to the sanctioned end-user. Their argument traced a chain of corporate registry links. The bottom line matched exactly what I already suspected from the registered-agent overlap, so it felt like strong corroboration.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "bb_01"
        ],
        "ground_truth_rationale": "Agreement with prior suspicion is treated as corroboration."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "disconfirming_evidence_assessment",
        "raw_interview_anchor": "One of our junior analysts flagged that a step in the vendor's chain — where they treated two similarly named entities as the same legal entity — hadn't been independently verified. I remember thinking that was a fair point to note, but it read to me as a technicality rather than something that undercut the conclusion, since the overall picture fit so well with what I was already building.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "bb_01"
        ],
        "ground_truth_rationale": "The flagged validity issue is discounted because the conclusion fits."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "argument_verification",
        "raw_interview_anchor": "The conclusion aligned with my working theory, and the vendor has a decent track record. I treated the alignment itself as a kind of confirmation. I didn't go back and independently re-verify that specific entity-matching step before folding the report into the case file.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "bb_01"
        ],
        "ground_truth_rationale": "Explicit conclusion-driven acceptance and failure to verify the disputed premise."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "post_decision_correction",
        "raw_interview_anchor": "A document pull afterward showed the two entities were actually legally distinct, different beneficial owners entirely. Compliance counsel asked directly what independent verification had been done on that claim, and I had to admit — not much, beyond the vendor's own chain.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Hindsight correction after the decision, not a new biased judgment."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "external_timing_assessment",
        "raw_interview_anchor": "We'd requested SWIFT records — MT202 and MT103 messages — to confirm the fund flow to the suspected end-user. That correspondent bank, in a secondary jurisdiction, is notoriously slow; historically those requests take twelve to fifteen business days. We were six days from the filing deadline with nothing back yet, no confirmation timeline in writing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Adverse historical turnaround and remaining time are stated before the forecast."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "favorable_forecast_and_action",
        "raw_interview_anchor": "I held off drafting it. I figured the records would probably come through in time — I wanted the file to be complete with that corroborating piece rather than submit something with a gap in it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "wt_01"
        ],
        "ground_truth_rationale": "Desired completeness drives unsupported favorable prediction and delay."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "forecast_basis_reflection",
        "raw_interview_anchor": "Honestly, more that I wanted it to land that way. Nothing had actually changed with the correspondent bank's typical pace. On day six they came back and said it'd be another ten days.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "wt_01"
        ],
        "ground_truth_rationale": "Confirms desire, not evidence, drove the forecast."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "inside_view_estimate",
        "raw_interview_anchor": "With reconciliation, narrative drafting, and compliance sign-off left, I estimated two business days. I walked through the sequence assuming everything went smoothly — no rework.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "pf_01"
        ],
        "ground_truth_rationale": "Best-case sequence and no rework underpin the estimate."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "base_rate_workload_reflection",
        "raw_interview_anchor": "Comparable cross-border verification cases have typically run five to seven days. I didn't really reference that when I made the call, and I still had two other active cases pulling at me.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "pf_01"
        ],
        "ground_truth_rationale": "Base rate and competing workload were not incorporated."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "uncertainty_assessment",
        "raw_interview_anchor": "Probably the entity-matching step and whether the records would actually show up. Those felt like the shakiest parts, even while I was moving forward on them.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective uncertainty alone is not a target bias."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "estimate_review",
        "raw_interview_anchor": "The base rate, probably, and the fact that I was already stretched across two other cases. Fair critique.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Prompted hindsight recognition, not a new instance."
      }
    ]
  }
