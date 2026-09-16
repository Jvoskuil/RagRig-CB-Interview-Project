"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "objective_and_role_rationale",
        "raw_interview_anchor": "I was the Product Manager for onboarding at CollabHub... My responsibility was to identify a credible response quickly without derailing the sprint roadmap or putting enterprise customers at greater risk.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states the operational objective and constraints without a manifested hidden bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_investigation_action",
        "raw_interview_anchor": "At first, the dashboard only showed account setup as one broad stage... I asked our data analyst to investigate the funnel instrumentation and asked a designer to pull heatmap analytics.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The investigation actions are a reasonable response to an underspecified dashboard signal."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "objective_tradeoff",
        "raw_interview_anchor": "In the immediate sense, reduce abandonment and protect activation rate... We had to decide whether this was a narrow usability or payment issue, or evidence that our whole onboarding approach was behind where the market was going.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This frames competing product objectives and hypotheses but does not manifest the hidden instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "investigation_choice",
        "raw_interview_anchor": "I chose a rapid internal analytics review, supplemented by a light competitor scan, rather than immediately commissioning user interviews.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is decision point 1; the hidden manifest assigns no bias there."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_and_time_constraint",
        "raw_interview_anchor": "I had the 32% increase in the broad account-setup drop-off step, no fresh qualitative feedback, and a warning from the analyst that the payment sub-step had incomplete instrumentation... We had only five weeks until the board review.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "These are the evidence and timing constraints available before decision point 1."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "investigation_rationale",
        "raw_interview_anchor": "We needed a directional answer within days, not weeks... I documented that we were choosing speed over depth and asked Research to hold provisional time in case the data stayed unclear.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly documents a speed-versus-depth tradeoff and preserves a fallback research option."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "evidence_interpretation",
        "raw_interview_anchor": "The analyst narrowed the issue. Abandonment rose most clearly after payment details... So it was suggestive, but not statistically stable.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant appropriately characterizes a small, incompletely instrumented cohort signal as suggestive but unstable."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "market_signal_assessment",
        "raw_interview_anchor": "Once I was preparing options for the VP of Product. The competitor review showed three named platforms had shipped guided setup experiences... An industry newsletter was describing guided setup as something most leading SaaS onboarding flows were adopting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This records external context that became relevant; the hidden occurrence is mapped to the subsequent weighting-and-choice rationale."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "redesign_decision_framing",
        "raw_interview_anchor": "Whether to build an AI-guided setup wizard, focus on the payment-detail issue, or run a small A/B test of both directions before committing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This states the alternatives at decision point 2 without yet expressing the hidden mechanism."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "redesign_evidence_inventory",
        "raw_interview_anchor": "Internally, we had the payment-field signal, but it was from a small cohort... Externally, we had a much more visible pattern: competitors were changing their onboarding experiences...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant inventories competing evidence sources before explaining how they were weighted."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "biased_evidence_weighting_and_choice",
        "raw_interview_anchor": "I put more weight on the external pattern than I normally would have... I decided the AI-guided wizard was the better strategic move, and we would address the payment field within that broader redesign later.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "herd_01"
        ],
        "ground_truth_rationale": "This is the sole hidden instance: adoption prevalence among competitors and peer PMs is used as the primary basis for choosing the wizard while the internal payment signal is downweighted."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "test_rejection_rationale",
        "raw_interview_anchor": "I ruled it out because it would have taken design and engineering time without giving us a board-ready feature direction quickly. Also, I felt that waiting while the market moved would make us look late.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The manifest contains no additional occurrence at the A/B-test decision; the stated deadline and communication rationale remain a plausible non-bias explanation."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "I probably would have pushed harder for the payment-field experiment first. The external activity was a major reason I was comfortable making a larger commitment despite the uncertainty in our own data.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is corroborating counterfactual evidence for the mapped instance, not a separate hidden occurrence."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "resource_allocation_choice",
        "raw_interview_anchor": "I had to decide whether to fully reassign two engineers from the enterprise bug-fix backlog for three sprints, split their time... or delay the wizard and prioritize the backlog.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is decision point 3, which the hidden specification identifies as non-biased."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "resource_allocation_rationale",
        "raw_interview_anchor": "I authorized the full reallocation to the wizard... I accepted the bug-risk trade-off, with the engineering lead agreeing to triage only production-severity issues during the build.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The staffing decision is explained through capacity, feature completeness, board visibility, and an explicit risk mitigation."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "post_decision_evidence_review",
        "raw_interview_anchor": "Two enterprise tickets escalated during that period... The wizard build stayed on schedule. At the same time, a follow-up analytics review continued to show payment-field friction.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This reports consequences and persistent evidence without adding a hidden bias instance."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "launch_choice_and_evidence",
        "raw_interview_anchor": "Whether to release the wizard to all new signups before the board review, limit it to a 10% canary release, or wait another week for more regression testing and improved payment instrumentation... The board meeting was four days away.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is decision point 4 framing under technical and board-review constraints."
      },
      {
        "segment_id": "seg_018",
        "speaker": "Participant",
        "segment_type": "launch_rationale",
        "raw_interview_anchor": "A 10% canary would have been safer technically, but it would not produce enough usable operational evidence before the board meeting. Waiting another week would have improved testing, but it would also leave us presenting a plan rather than a shipped response.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden specification assigns no bias to decision point 4; the candidate escalation interpretation is not affirmatively supported."
      },
      {
        "segment_id": "seg_019",
        "speaker": "Participant",
        "segment_type": "outcome_assessment",
        "raw_interview_anchor": "The post-launch activation rate did not show a statistically significant change from the prior month... We then prioritized a focused review of payment validation and instrumentation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant assesses the launch outcome and redirects work toward the unresolved payment issue."
      },
      {
        "segment_id": "seg_020",
        "speaker": "Participant",
        "segment_type": "retrospective_alternative_plan",
        "raw_interview_anchor": "I would have run the controlled comparison and recruited several users from the new account cohort. I would also have kept the wizard in a limited canary longer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective improvement plan and not a new manifested occurrence."
      },
      {
        "segment_id": "seg_021",
        "speaker": "Participant",
        "segment_type": "decision_changing_evidence",
        "raw_interview_anchor": "A larger, stable cohort showing that payment details were clearly the dominant exit point would have changed it... If that evidence had been strong, I would have treated the payment fix as the immediate priority.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant identifies evidence that would have changed the redesign decision."
      },
      {
        "segment_id": "seg_022",
        "speaker": "Participant",
        "segment_type": "market_counterfactual",
        "raw_interview_anchor": "If the competitors had not introduced guided onboarding at that time... I think I would have been more willing to make the smaller, targeted payment change first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a counterfactual explanation of the earlier choice, not a second hidden instance."
      }
    ]
  }
