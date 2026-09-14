"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "care_goal",
        "raw_interview_anchor": "Mainly to get her diagnosis sorted out and make sure we sent her home with a safe, appropriate plan.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States the overall care objective without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_risk_assessment",
        "raw_interview_anchor": "Her CHA2DS2-VASc came out to 4... Her HAS-BLED was 2, which is moderate, not a red flag. Pharmacy checked and there were no interactions with the DOAC we'd typically use.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Accurately summarizes available quantitative risk and medication-interaction information."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "initial_treatment_deferral",
        "raw_interview_anchor": "Still, when I saw \"fall\" in the history, that gave me pause about starting a blood thinner right away... we'd hold off and get a formal fall-risk assessment first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Describes a clinically plausible precaution based on a recent fall but does not independently contain the required explicit act-versus-omission blame framing."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "family_reassurance_decision",
        "raw_interview_anchor": "Clinically nothing had changed... but I ended up ordering a head CT partly to have something concrete to reassure her with.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explains an anxiety-management and communication choice; no hidden target instance is assigned to this episode."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "updated_objective_assessment",
        "raw_interview_anchor": "By day three the CT was normal, and physical therapy had cleared her fall risk as low with a walker. So on paper the numbers were now clearly in favor of starting treatment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Records the updated evidence and its implication without the subsequent emotional forecast."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "final_emotional_forecast_and_deferral",
        "raw_interview_anchor": "I remember standing at the nurses' station... picturing what it would be like if we started her on this drug and then she had a major bleed... It felt like the kind of thing I'd still be replaying weeks later... That feeling seemed heavier to carry than just not starting it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "im_01"
        ],
        "ground_truth_rationale": "Contains the vivid forecast of intense and durable emotional consequences from a hypothetical bleed overriding the updated quantitative evidence."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "discharge_bruise_assessment",
        "raw_interview_anchor": "It didn't change anything about the plan; we finalized the discharge summary without a firm start plan.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly treats the bruise as unrelated and non-decisive."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "first_point_cue_assessment",
        "raw_interview_anchor": "Clinically I knew the scores favored treatment, but a recent fall in an older patient just registers as a flag.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Describes salience of the fall but does not by itself state differential blame for action versus inaction."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "first_point_alternatives",
        "raw_interview_anchor": "We could have started the DOAC immediately... or started a lower empirical dose. I chose to wait for a formal PT evaluation instead.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Lists alternatives and the selected precaution; the explicit blame-based rationale appears in the following segment."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "first_point_decision_basis",
        "raw_interview_anchor": "I suppose not wanting to be the direct cause of a bad outcome. Withholding felt like the more conservative option, even though I recognized the resident had pointed out the stroke risk reduction was the bigger number.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "om_01"
        ],
        "ground_truth_rationale": "Explicitly prefers withholding because prescribing would make the physician the direct cause of harm, despite recognizing that treatment had the larger numerical benefit."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "family_conversation_goal",
        "raw_interview_anchor": "Mostly to de-escalate the family's fear so we could have a productive conversation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States a communication goal without a target bias manifestation."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "time_pressure_assessment",
        "raw_interview_anchor": "We were already tight on discharge planning, and adding a CT meant another day. But I felt like skipping that step would leave the family conversation unresolved.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explains perceived communication pressure and does not instantiate either hidden target mechanism."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "third_point_reflection",
        "raw_interview_anchor": "The data at that point was pretty clean... I remember describing... this scenario of her bleeding on a drug I'd started... something that wouldn't really fade... It wasn't really about the probability anymore.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Corroborates the already mapped day-three instance but is not treated as a separate hidden occurrence."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "third_point_alternatives",
        "raw_interview_anchor": "Starting it right there before discharge, starting a lower dose with a firm two-week follow-up, or deferring entirely, which is what I did.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Lists alternatives and the choice without independently adding a new hidden instance."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "prior_experience_context",
        "raw_interview_anchor": "The ward story about the other patient's bleed was fresh in everyone's mind that week.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Provides contextual salience that supports a candidate availability interpretation but does not explicitly establish that mechanism."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "bruise_decision_context",
        "raw_interview_anchor": "It didn't really change the clinical picture, since she wasn't even on the medication yet. We noted it and moved on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly rejects the bruise as causally relevant."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "follow_up_constraint",
        "raw_interview_anchor": "We sent her out with a follow-up appointment that ended up being three weeks out, later than the two-week window we'd wanted.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States an operational consequence and follow-up constraint."
      },
      {
        "segment_id": "seg_018",
        "speaker": "Participant",
        "segment_type": "counterfactual_first_decision",
        "raw_interview_anchor": "If I'd had that clearance up front, I likely would have started treatment on day one instead of waiting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Counterfactual reflection about timing of information; it does not add a new hidden occurrence."
      },
      {
        "segment_id": "seg_019",
        "speaker": "Participant",
        "segment_type": "counterfactual_family_effect",
        "raw_interview_anchor": "If the other patient's bleeding event had never come up on the ward... I think the family conversation would have been calmer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Counterfactual communication reflection without a direct bias manifestation."
      },
      {
        "segment_id": "seg_020",
        "speaker": "Participant",
        "segment_type": "closing_debiasing_advice",
        "raw_interview_anchor": "Make sure the fall workup happens early... try to separate the family's emotional reaction from the actual numbers... It's easy to let the picture of a bad outcome sit with you well past the moment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective advice and debiasing reflection rather than a new decision-time instance."
      }
    ]
  }
