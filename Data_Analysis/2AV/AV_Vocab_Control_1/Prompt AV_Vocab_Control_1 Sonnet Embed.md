You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for joining me. This is being recorded for an internal reliability-process review, not a personnel evaluation — we're just trying to understand how these calls actually get made. Okay to proceed?

Participant: Sure, no problem.

Interviewer: Can you tell me your role and how this case came across your desk?

Participant: I'm a reliability engineer in Maintenance Control. Part of my job is tracking repetitive write-ups across the fleet and deciding when something needs a formal corrective action versus routine monitoring. This one started when tail 738 logged a third APU bleed air valve write-up inside 45 flight days. The first two had closed out as operational check normal — no parts replaced — which is common; a lot of these clear on the bench and never come back.

Interviewer: Walk me through the incident from the start.

Participant: The third write-up on 738 is what caught my attention. Three in that short a window is unusual, though our fleet-wide removal rate for that valve was still inside the OEM's published MTBUR, so nothing yet told me this was a fleet problem. It looked like it could just be a stubborn individual aircraft. I opened a focused review on 738 and put a flag on it so I'd get pinged if anything similar turned up elsewhere. Two days later it did — tail 712 logged a lower-severity version of the same complaint. Line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility of an intermittent fault that ground checks weren't catching. I pulled the two tails' component histories together and found they shared the same valve batch lot number. That was the first real thread.

Interviewer: What did you do with the lot-number connection?

Participant: Company policy discourages repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had an in-flight consequence; both were caught on the ground. Grounding both outright felt like more than the evidence supported at that point, so I set a one-leg maximum MEL carryover on both tails and opened a formal root-cause investigation tied to the lot number.

Interviewer: What came out of that investigation?

Participant: The vendor quality engineer confirmed the lot had a documented seal-material change about six months earlier — that's a traceable, real candidate cause. But when I got the in-house teardown back on the valve pulled from 738, the degradation pattern wasn't clean. It was consistent with the seal-material change, but it also overlapped with a separate supplier nonconformance that had been logged against an earlier serial range — and that nonconformance would have implied a wider set of affected valves than just this lot.

Interviewer: That sounds like it complicated things. What were you weighing at that point?

Participant: Right, this is before I finalized anything for the board. I had ten days to the RCB deadline. If I went with just the vendor documentation and the ambiguous teardown, I'd be guessing at which of the two explanations was actually driving the failures — and that guess would directly change how many valves I'd be asking to replace. One candidate pointed at a single lot; the other pointed at a broader serial range. An external metallurgical lab could run a composition assay that would distinguish the two, but their turnaround was about three weeks, which meant blowing through the RCB deadline before I'd have an answer.

Interviewer: What did you decide?

Participant: I sent it out. I genuinely didn't know which cause was correct, and the two answers led to different-sized corrective actions. Submitting on the original timeline would have meant picking one interpretation without being able to defend it if someone on the board asked why I ruled out the other nonconformance. I'd rather take the deadline hit than write a scope I couldn't justify.

Interviewer: At the time, was there anything that assay could tell you that would actually change your recommendation?

Participant: Yes — directly. If it had come back pointing at the broader nonconformance instead of the seal-material change, I'd have had to widen the replacement scope well beyond this one lot, potentially into aircraft that hadn't shown any symptoms yet. That's a materially different corrective action request, so the result wasn't just confirmatory. It was the thing that would tell me which request to write.

Interviewer: What happened with the deadline?

Participant: We missed the RCB cycle. It slipped to submit-pending-lab-results. When the assay came back, it identified the seal-material change as the actual cause and ruled out the other nonconformance. So the lot-bounded scope held up, but I didn't know that going in.

Interviewer: Take me to the final decision — what you actually recommended.

Participant: Once the assay settled which mechanism was operating, the OEM tech rep also raised a broader design review of the seal specification generally, as a longer-term item. That's a slower, separate track. What I had in hand was a specific, bounded problem: one vendor lot, identifiable serial ranges, and now a cause that was no longer ambiguous. I wrote the corrective action request to replace valves from that lot specifically — not a fleet-wide swap, and not deferring to wait on the OEM's broader review.

Interviewer: Why bounded to the lot rather than fleet-wide?

Participant: Because a fleet-wide replacement would pull serviceable, unaffected valves for no reliability benefit — that's cost and downtime without a justified reason. Once the assay confirmed the mechanism, the evidence supported exactly that lot, so that's what I scoped the action to.

Interviewer: What happened after submission?

Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review is still running separately, unrelated to this specific corrective action.

Interviewer: Looking back, is there a point you'd handle differently?

Participant: Honestly, I keep coming back to the deadline slip. I don't think I'd change the decision to get the assay — the ambiguity was real, and guessing wrong on scope would have been worse than being late. But I might push harder next time to get the lab to prioritize a case like this, or find out earlier whether a faster partial test could resolve just the scope question without needing the full three-week turnaround.

Interviewer: If the teardown result hadn't been ambiguous — if it had clearly pointed to just the seal-material change from the start — would you still have sent it out?

Participant: Probably not on the same timeline. If the in-house evidence had cleanly ruled out the other nonconformance, there wouldn't have been a live scope question left to answer, and I'd have likely submitted on the original ten days.

Interviewer: And if this exact pattern showed up on a different fleet type — same kind of ambiguity, same deadline pressure — would you send it out again?

Participant: Yes, if there were genuinely two live explanations with different-sized consequences. That's really the test I'd apply — whether the result could actually change what I'd recommend, not just make the file feel more complete.

Interviewer: That's a good place to stop. Thanks for walking through it in this much detail.

Participant: Happy to help — glad it was useful.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Vocab_Control_1",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Aviation Maintenance Planner / Reliability Engineer",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Recurring APU Bleed Valve Fault: Fleet Reliability Escalation (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A reliability engineer at a regional airline's MCC investigates a third recurring write-up of an APU bleed air valve fault on the same tail number within 45 flight days, matching the paired scenario's setting, actors, terminology, and four-decision-point structure. Unlike the paired biased scenario, every decision-including the evidence-selection decision before the corrective-action recommendation-is supported by evidence that is genuinely decision-relevant at the time it is gathered. No instance of information bias, or any other named bias, is intentionally embedded.",
    "occupational_realism": {
      "objective": "Determine whether the recurring APU bleed valve fault represents an isolated maintenance issue or a fleet-wide airworthiness risk, and select a corrective action before the next scheduled Reliability Control Board (RCB) meeting.",
      "setting": "Regional airline Maintenance Control Center (MCC), reviewing tail-number defect history, fleet reliability reports, and vendor teardown data under a 10-day deadline before the RCB meeting.",
      "constraints": [
        "10 calendar days until mandatory RCB submission deadline",
        "Aircraft on revenue schedule; AOG grounding has direct revenue and crew-scheduling cost",
        "Limited in-house metallurgical/vendor teardown capacity, requiring external lab scheduling with lead time",
        "Regulatory reporting obligation if fault is classified as an unsafe condition (potential Airworthiness Directive trigger)",
        "Fleet has 24 aircraft; only 3 have logged this specific bleed valve write-up"
      ],
      "stakeholders": [
        "Reliability Control Board (RCB) chair",
        "Line maintenance supervisor",
        "OEM technical representative",
        "Flight operations scheduling manager",
        "Component vendor quality engineer"
      ],
      "technical_terms_to_use": [
        "APU bleed air valve",
        "repetitive write-up",
        "MEL (Minimum Equipment List)",
        "teardown analysis",
        "Reliability Control Board",
        "component removal rate",
        "no-fault-found (NFF)",
        "corrective action request",
        "fleet campaign",
        "interim operational restriction"
      ],
      "technical_terms_to_avoid": [
        "information bias",
        "cognitive bias",
        "anchoring",
        "confirmation bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tail 738 has logged three bleed valve write-ups in 45 flight days",
          "Two prior write-ups were closed as 'operational check normal' with no part replacement",
          "Fleet-wide removal rate for this valve is within OEM-published MTBUR"
        ],
        "new_information_after_decision": [
          "A second tail (712) logs a similar, lower-severity write-up two days later",
          "Line maintenance reports the valve is difficult to bench-test, raising suspicion of an intermittent fault masked by ground testing"
        ],
        "alternatives": [
          "Treat as isolated tail-specific issue; monitor via routine trend report",
          "Escalate immediately to a two-aircraft focused reliability review",
          "Request OEM service bulletin history before deciding severity classification"
        ],
        "intended_action": "Engineer opens a focused reliability review on tail 738 and flags tail 712 for monitoring, without yet declaring a fleet campaign."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Focused review confirms both tails share the same valve batch lot number",
          "MEL allows dispatch with the APU inoperative under defined conditions, but company policy discourages repeated MEL carryover",
          "No safety event has occurred; both faults were caught on ground checks"
        ],
        "new_information_after_decision": [
          "Vendor quality engineer confirms the batch lot had a documented seal-material change six months prior",
          "Line maintenance requests clarity on how long the interim restriction will remain in effect, citing crew-scheduling friction"
        ],
        "alternatives": [
          "Apply an interim operational restriction (no MEL carryover beyond one flight leg) pending root cause",
          "Allow normal MEL dispatch to continue while root cause investigation proceeds in parallel",
          "Ground both tails immediately pending full inspection"
        ],
        "intended_action": "Engineer applies the interim one-leg MEL restriction on both affected tails and opens a formal root-cause investigation referencing the seal-material lot change."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor-confirmed seal-material change is a documented candidate root cause consistent with both write-ups",
          "In-house teardown of the removed valve from tail 738 shows seal degradation, but the degradation pattern is ambiguous between the reported material change and a second, previously logged supplier nonconformance affecting an overlapping serial range",
          "External metallurgical lab could provide an independent composition assay distinguishing the two candidate causes, but has a 3-week lead time that would exceed the RCB deadline"
        ],
        "new_information_after_decision": [
          "The RCB deadline passes with the corrective-action recommendation still pending lab results",
          "The assay identifies the seal-material change as the operative cause and rules out the second nonconformance, which would have implied a wider serial range for replacement"
        ],
        "alternatives": [
          "Proceed to a corrective-action recommendation using only the vendor lot documentation and ambiguous in-house teardown",
          "Commission the external metallurgical assay before finalizing any recommendation, delaying the RCB submission past its deadline",
          "Request a limited peer review of the existing teardown photos as a faster substitute"
        ],
        "intended_action": "Engineer commissions the external metallurgical assay before finalizing the recommendation because the in-house teardown cannot yet distinguish between two candidate causes that imply different replacement scopes, and the assay result is capable of changing which valves the corrective action covers."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Confirmed root cause: seal-material change in a specific vendor lot, affecting a known, boundable set of valves",
          "Corrective action request drafted by engineer names the affected lot and recommends valve replacement across that lot only",
          "OEM technical representative suggests a broader design review of the valve seal specification as a longer-term option"
        ],
        "new_information_after_decision": [
          "RCB approves the lot-based replacement campaign; no further in-service events occur on the affected tails after replacement",
          "The broader OEM design review is deferred pending a separate long-term reliability study"
        ],
        "alternatives": [
          "Recommend a bounded corrective action limited to the affected vendor lot",
          "Recommend a full fleet-wide valve replacement regardless of lot",
          "Recommend deferring any hardware change pending the OEM's broader design review"
        ],
        "intended_action": "Engineer submits a lot-bounded corrective action request to the RCB, which is approved and closes the investigation."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this recurring bleed valve write-up first came to your attention.",
        "What was your initial read on whether this was a single-aircraft issue or something bigger?"
      ],
      "timeline_reconstruction": [
        "After the second tail showed a similar fault, what changed in how you were tracking this?",
        "When did the vendor lot-number information come in, and how did that shift your view of the root cause?",
        "Take me through the sequence between the ambiguous teardown finding and drafting your corrective action recommendation."
      ],
      "decision_point_probes": [
        "At the point you opened the focused review, what alternatives did you weigh before deciding not to declare a full fleet campaign yet?",
        "When you set the interim MEL restriction, what made a one-leg limit feel like the right balance versus grounding outright?",
        "Once the teardown result came back ambiguous, what made you decide the external assay was necessary rather than proceeding on what you had?",
        "Walk me through why you chose a lot-bounded replacement over a full fleet-wide swap or waiting for the OEM's design review."
      ],
      "goals_and_alternatives": [
        "What competing goals were you balancing between schedule reliability and thoroughness of the investigation?",
        "Were there alternative evidence sources you considered but didn't pursue at each stage?"
      ],
      "closing_hypotheticals": [
        "If the teardown result hadn't been ambiguous, would you still have sent the valve out for an external assay?",
        "If you'd had the assay results in hand before the RCB deadline, would your final recommendation have looked any different from what you actually submitted?",
        "Looking back, what would you do differently if a similar recurring write-up showed up on another fleet type?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "AV_Biased_1",
      "features_to_match": [
        "Domain vocabulary: APU bleed air valve, repetitive write-up, MEL, teardown analysis, RCB, component removal rate, NFF, corrective action request, fleet campaign, interim operational restriction",
        "Setting: regional airline MCC, 10-day RCB deadline, 24-aircraft fleet, 3 affected tails",
        "Actors: reliability engineer participant, line maintenance supervisor, OEM technical representative, vendor quality engineer, flight operations scheduling manager",
        "Structure: identical four-decision-point sequence (triage/escalation, interim operational restriction, evidence-selection before corrective action, final corrective-action scope)",
        "Difficulty and emotional tone: same time pressure, same measured/professional register, same absence of acute safety event",
        "Decision count: exactly four"
      ],
      "features_to_remove_or_change": [
        "The in-house teardown finding is written as genuinely ambiguous between two candidate causes with different replacement-scope implications, rather than already sufficient and merely confirmatory",
        "The external assay is reframed as capable of changing the corrective action's scope (ruling in or out a second candidate nonconformance), so commissioning it is decision-relevant rather than merely reassurance-seeking",
        "The participant's stated rationale for the assay cites an unresolved scope question rather than a desire for a third confirmatory source once the conclusion was already reached"
      ],
      "ambiguity_boundary": "Not applicable; this is a vocabulary_control condition with zero intended bias instances, not an ambiguous_control condition."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly four decision points are present, matching the paired scenario's structure.",
      "Confirm zero intended instances of information bias, or any other named bias, appear anywhere in the interview.",
      "Confirm the decision-point-3 evidence-selection act is written so the external assay is explicitly capable of changing the corrective action's scope, distinguishing it from the paired biased scenario's decision-irrelevant assay request.",
      "Confirm domain vocabulary, actors, setting, time pressure, and emotional register match the paired scenario AV_Biased_1.",
      "Confirm total word count falls between 1,215 and 1,485 words, target 1,350.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm no accidental bias-like pattern (e.g., unjustified evidence-seeking, selective evidence weighting) is introduced at any decision point.",
      "Confirm consequences (RCB approval, no further in-service events) do not themselves imply any bias judgment."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Information bias",
        "occurrences": 0,
        "mechanism_constraint": "Per vocabulary_control condition rules, zero intended instances must be implemented regardless of the caller-supplied manifest value of 1; the evidence-selection decision (decision point 3) must instead be written so the external assay is genuinely decision-relevant (capable of changing corrective-action scope), removing the mechanism entirely rather than weakening it."
      }
    ],
    "target_bias_names": [
      "Information bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Information bias",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "AV_Biased_1",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Vocab_Control_1",
    "domain_id": "AV",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is vocabulary_control, which requires zero intended instances of all named biases regardless of the input occurrence manifest. The caller-supplied manifest value of 1 for Information bias is overridden to 0 per CONDITION RULES; the decision point that hosted the bias mechanism in the paired scenario (decision point 3, evidence-selection prior to corrective-action recommendation) is retained structurally but rewritten so the same evidence-selection act is fully decision-relevant and non-biased, preserving vocabulary, structure, and decision count parity with AV_Biased_1.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and role (Aviation Maintenance Planner / Reliability Engineer, regional airline MCC)",
      "Fleet size, affected tail count, and RCB deadline (10 days)",
      "Full technical vocabulary list used in AV_Biased_1",
      "Four-decision-point structure and its ordering (triage, interim restriction, evidence-selection, final corrective-action scope)",
      "Actor roster (line maintenance supervisor, OEM technical representative, vendor quality engineer, flight operations scheduling manager)",
      "Emotional tone/register and difficulty level",
      "Absence of any acute in-flight safety event"
    ],
    "generation_warnings": [
      "The input occurrence manifest specified 1 occurrence of Information bias, but the vocabulary_control condition mandates zero intended instances of all named biases; this specification overrides the manifest count to 0 for the public interview as required by CONDITION RULES, and this override is recorded here rather than silently applied without documentation."
    ]
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
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
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative, mechanism-first review of the interview for affirmatively evidenced bias-specific reasoning effects; the participant's explicit debiasing statements and corrections were treated as counterevidence rather than as bias occurrences."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [],
  "no_supported_biases_found": true,
  "limitations": [
    "The transcript contains several explicit debiasing statements: the participant suspended a potentially anchoring musculoskeletal story, requested Dr. B's documented workup before judging the earlier discharge, and rejected visit eventfulness as an admission driver. These possible influences did not meet the conservative threshold for an identified bias occurrence.",
    "The analysis is limited to verbalized reasoning in the transcript and cannot exclude unexpressed implicit or automatic biases.",
    "Retrieved corpus support was not used because no identified bias occurrence required grounding."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Vocab_Control_1_Sonnet_on",
  "interview_id": "AV_Vocab_Control_1",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
