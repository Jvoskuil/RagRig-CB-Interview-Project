"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "I'm a reliability engineer in Maintenance Control. Part of my job is tracking repetitive write-ups across the fleet and deciding when something needs a formal corrective action versus routine monitoring.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Role-based decision criteria are stated without a hidden bias mechanism."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "Three in that short a window is unusual, though our fleet-wide removal rate for that valve was still inside the OEM's published MTBUR, so nothing yet told me this was a fleet problem. It looked like it could just be a stubborn individual aircraft.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant weighs local recurrence against fleet-wide reliability data without an intended distortion."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "I opened a focused review on 738 and put a flag on it so I'd get pinged if anything similar turned up elsewhere.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The monitoring action is proportionate to the evidence and preserves escalation if new evidence appears."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "Line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility of an intermittent fault that ground checks weren't catching.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A reported test limitation leads to a plausible alternative explanation, not a hidden bias."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "I pulled the two tails' component histories together and found they shared the same valve batch lot number. That was the first real thread.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant actively seeks cross-case evidence and identifies a traceable common factor."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "Company policy discourages repeated MEL carryover on the same defect ... doing it leg after leg on the same fault is a flag in itself.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Policy and repeated-defect risk are used as relevant decision inputs."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "Grounding both outright felt like more than the evidence supported at that point, so I set a one-leg maximum MEL carryover on both tails and opened a formal root-cause investigation tied to the lot number.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant chooses an interim restriction calibrated to available evidence and opens an investigation."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "The vendor quality engineer confirmed the lot had a documented seal-material change about six months earlier — that's a traceable, real candidate cause.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Documented vendor evidence is treated as a candidate cause, not as conclusive proof."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "The degradation pattern wasn't clean. It was consistent with the seal-material change, but it also overlapped with a separate supplier nonconformance ... and that nonconformance would have implied a wider set of affected valves than just this lot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Ambiguous evidence is explicitly recognized as supporting two live causal explanations."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "If I went with just the vendor documentation and the ambiguous teardown, I'd be guessing at which of the two explanations was actually driving the failures — and that guess would directly change how many valves I'd be asking to replace.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant identifies unresolved uncertainty and its direct consequence for corrective-action scope."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "An external metallurgical lab could run a composition assay that would distinguish the two, but their turnaround was about three weeks, which meant blowing through the RCB deadline before I'd have an answer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant weighs a decision-relevant evidence source against a known timing cost."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "I sent it out. I genuinely didn't know which cause was correct, and the two answers led to different-sized corrective actions. Submitting on the original timeline would have meant picking one interpretation without being able to defend it ... I'd rather take the deadline hit than write a scope I couldn't justify.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The assay is commissioned because unresolved evidence could change the recommendation, despite the deadline cost."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "If it had come back pointing at the broader nonconformance instead of the seal-material change, I'd have had to widen the replacement scope ... That's a materially different corrective action request, so the result wasn't just confirmatory.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly states how the test result could alter the action."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "It slipped to submit-pending-lab-results. When the assay came back, it identified the seal-material change as the actual cause and ruled out the other nonconformance. So the lot-bounded scope held up, but I didn't know that going in.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant distinguishes subsequent confirmation from information available before the decision."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "What I had in hand was a specific, bounded problem: one vendor lot, identifiable serial ranges, and now a cause that was no longer ambiguous. I wrote the corrective action request to replace valves from that lot specifically — not a fleet-wide swap, and not deferring to wait on the OEM's broader review.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The final recommendation follows confirmed, bounded evidence while separating the longer-term design review."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "Because a fleet-wide replacement would pull serviceable, unaffected valves for no reliability benefit — that's cost and downtime without a justified reason. Once the assay confirmed the mechanism, the evidence supported exactly that lot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains why the scope is limited to the evidence-supported lot."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "reasoning",
        "raw_interview_anchor": "I don't think I'd change the decision to get the assay — the ambiguity was real, and guessing wrong on scope would have been worse than being late. But I might push harder next time to get the lab to prioritize a case like this, or find out earlier whether a faster partial test could resolve just the scope question.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The retrospective improvement concerns process speed, while affirming a decision-relevant evidence choice."
      }
    ]
  }
