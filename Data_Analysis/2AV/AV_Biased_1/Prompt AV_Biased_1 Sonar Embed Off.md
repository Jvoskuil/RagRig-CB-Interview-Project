You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for an internal reliability-process review, not a safety investigation into you personally — we're trying to understand how these calls actually get made in practice. That okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me your role and how this particular case landed on your desk?

Participant: Sure. I'm a reliability engineer in Maintenance Control. Part of my job is watching for repetitive write-ups across the fleet and deciding when something crosses from "normal noise" into something that needs a formal corrective action. This one came up because tail 738 logged a third APU bleed air valve write-up inside 45 flight days. Two earlier ones had been closed out as operational check normal, no parts changed, which is pretty typical — a lot of these clear on the bench.

Interviewer: Walk me through the incident from the beginning, in your own words.

Participant: So the third write-up on 738 is what actually got my attention, because three in that short a window is unusual even though our fleet-wide removal rate for that valve was still sitting inside the OEM's published MTBUR. Nothing screamed "fleet problem" yet — it looked like it could just be a stubborn individual aircraft. I opened a focused review on that tail rather than calling it a fleet issue outright, and I put a flag on it so I'd get pinged if anything similar showed up elsewhere. Two days later it did — tail 712 logged a lower-severity version of basically the same complaint. That's when line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility we had an intermittent fault that ground checks weren't catching. At that point I pulled the two tails' component histories together and found they shared the same valve batch lot number. That felt like a real thread to pull.

Interviewer: What did you do with that lot-number connection?

Participant: Company policy is we don't like repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had had an actual in-flight consequence; both faults were caught on the ground. So grounding both outright felt like more than the evidence supported at that point. I put an interim restriction on — one leg of MEL carryover maximum, then it has to be addressed — on both tails, and opened a formal root-cause investigation tied to that lot number.

Interviewer: What came back from that investigation?

Participant: The vendor quality engineer confirmed that lot had a documented seal-material change about six months earlier. That's a real, traceable cause — not a guess. And our in-house teardown of the valve we'd pulled off 738 showed seal degradation that was consistent with exactly that material change. So by that point I had two independent lines — vendor documentation and physical teardown — pointing at the same thing.

Interviewer: Let's slow down on that moment, because I want to understand what happened next. What were you weighing?

Participant: Right, so this is the part before I finalized anything for the Reliability Control Board. I had ten days to the RCB deadline. The vendor's lot documentation and our own teardown already lined up on the seal material as the cause, and honestly I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had.

Interviewer: And what did you decide?

Participant: I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result. I think I just wanted a third, fully independent source in the file alongside the vendor's own account of their material, so the package read as more thorough when it went to the board. I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway.

Interviewer: At the time you sent it out, was there anything the assay could tell you that would have changed which corrective action you recommended?

Participant: Not really, no. The recommendation was already written in my head — vendor records and physical teardown agreed, and that's what the corrective action request was going to be built on either way. I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself.

Interviewer: What happened with the deadline?

Participant: We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results, even though the recommendation itself wasn't really pending on anything. When the assay results did eventually land, they confirmed the same seal-material change the vendor had already told us about — nothing new in it.

Interviewer: Let's move to the final decision — what you actually recommended once everything was in.

Participant: Once the root cause was locked down, the OEM tech rep raised the idea of a broader design review of the valve seal spec generally, as a longer-term option. But that's a slow, separate track. What I had in front of me was a specific, bounded problem: one vendor lot, identifiable serial ranges. I wrote the corrective action request to replace valves from that lot specifically, not a fleet-wide swap of every valve regardless of lot, and not just deferring to wait on the OEM's broader review.

Interviewer: Why bounded to the lot rather than fleet-wide?

Participant: Because a fleet-wide replacement would have pulled serviceable, unaffected valves for no reason — that's cost and downtime with no reliability benefit. The evidence pointed specifically at that lot, so that's what I scoped the action to.

Interviewer: What happened after you submitted it?

Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review got pushed into a separate long-term study, which is still open as far as I know.

Interviewer: Looking back at the whole sequence — is there a point where, with hindsight, you'd handle it differently?

Participant: The one thing I go back and forth on is the external lab. I already knew the recommendation wasn't going to move based on what it found — I'd have submitted the same lot-based request either way. Knowing that now, I probably should have just submitted on the original ten-day timeline using the vendor and teardown evidence and let the RCB approve on that, rather than holding the whole submission for a test that was only ever going to restate what I already had.

Interviewer: If the assay had come back showing something different from the vendor's account — a different degradation mechanism, say — what would you have done?

Participant: I'd have flagged it and opened a separate follow-up investigation into whether the lot-based campaign needed a second look. But that would've come after the fact — I wasn't planning to hold up this submission on that possibility, since I'd already committed to the lot-based recommendation before the assay went out.

Interviewer: And if this exact pattern showed up again on a different fleet type — same lot-based signature, same timeline pressure — would you send it out for independent lab work again?

Participant: Probably not on the same timeline, honestly. I think I'd ask myself earlier on whether the extra data was likely to change the recommendation I'd already reached or just make the file look better, and weigh that against the deadline more explicitly than I did this time.

Interviewer: That's a good place to stop. Thanks for the detail — this is exactly the kind of reconstruction we needed.

Participant: No problem. Happy to follow up if anything else comes to mind.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Biased_1",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Aviation Maintenance Planner / Reliability Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Recurring APU Bleed Valve Fault: Fleet Reliability Escalation",
    "scenario_summary_internal": "A reliability engineer at a regional airline's MCC (Maintenance Control Center) investigates a third recurring write-up of an APU (Auxiliary Power Unit) bleed air valve fault on the same tail number within 45 flight days. The engineer must decide whether to escalate to a fleet-wide inspection campaign, what interim operational restriction to apply, what additional evidence to commission before recommending a corrective action, and what final corrective action (component redesign vs. procedural revision) to submit to the Reliability Control Board. The narrative embeds one instance of information bias at the evidence-selection decision point: the engineer commissions a costly, schedule-delaying data-gathering exercise that cannot change the already-justified decision, driven by a belief that 'more data is always safer,' rather than because the data is decision-relevant.",
    "occupational_realism": {
      "objective": "Determine whether the recurring APU bleed valve fault represents an isolated maintenance issue or a fleet-wide airworthiness risk, and select a corrective action before the next scheduled Reliability Control Board (RCB) meeting.",
      "setting": "Regional airline Maintenance Control Center (MCC), reviewing tail-number defect history, fleet reliability reports, and vendor teardown data under a 10-day deadline before the RCB meeting.",
      "constraints": [
        "10 calendar days until mandatory RCB submission deadline",
        "Aircraft on revenue schedule; AOG (aircraft on ground) grounding has direct revenue and crew-scheduling cost",
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
          "Fleet-wide removal rate for this valve is within OEM-published MTBUR (mean time between unscheduled removals)"
        ],
        "new_information_after_decision": [
          "A second tail (train 712) logs a similar, lower-severity write-up two days later",
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
          "No safety event (in-flight consequence) has occurred; both faults were caught on ground checks"
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
          "Vendor-confirmed seal-material change is a documented, sufficient candidate root cause consistent with both write-ups",
          "In-house teardown of the removed valve from tail 738 already shows seal degradation consistent with the material change",
          "External metallurgical lab could provide an independent composition assay, but has a 3-week lead time that would exceed the RCB deadline"
        ],
        "new_information_after_decision": [
          "The RCB deadline passes with the corrective-action recommendation still pending vendor lab results",
          "The eventual metallurgical assay (received after the deadline) confirms exactly the seal-material change already identified by the vendor, adding no new decision-relevant detail"
        ],
        "alternatives": [
          "Proceed to a corrective-action recommendation using the existing in-house teardown and vendor lot documentation, which are already sufficient to identify the seal-material cause",
          "Commission the external metallurgical assay before finalizing any recommendation, delaying the RCB submission past its deadline",
          "Request a limited peer review of the existing teardown photos as a faster, decision-relevant supplement"
        ],
        "intended_action": "Engineer commissions the full external metallurgical assay before finalizing the recommendation, reasoning that having independent composition data will make the eventual RCB submission 'more thorough and defensible,' even though the existing vendor and in-house evidence already sufficiently establishes the same seal-material cause and the assay cannot alter which corrective action is warranted."
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
        "Take me through the sequence between confirming the seal-material lead and drafting your corrective action recommendation."
      ],
      "decision_point_probes": [
        "At the point you opened the focused review, what alternatives did you weigh before deciding not to declare a full fleet campaign yet?",
        "When you set the interim MEL restriction, what made a one-leg limit feel like the right balance versus grounding outright?",
        "Once the vendor confirmed the seal-material change, what more, if anything, did you feel you needed before recommending action, and why?",
        "Walk me through why you chose a lot-bounded replacement over a full fleet-wide swap or waiting for the OEM's design review."
      ],
      "goals_and_alternatives": [
        "What competing goals were you balancing between schedule reliability and thoroughness of the investigation?",
        "Were there alternative evidence sources you considered but didn't pursue at each stage?"
      ],
      "closing_hypotheticals": [
        "If the metallurgical assay had come back showing something different from the vendor's explanation, how would that have changed your recommendation?",
        "If you'd had the assay results in hand before the RCB deadline, would your final recommendation have been any different from what you actually submitted?",
        "Looking back, what would you do differently if a similar recurring write-up showed up on another fleet type?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "decision_point": 3,
        "mechanism": "Engineer seeks additional confirmatory data (external metallurgical assay) that cannot alter the corrective-action decision, motivated by a belief that more data inherently improves decision quality or defensibility, rather than by the data's actual decision relevance.",
        "affected_reasoning_operation": "Evidence-sufficiency assessment and evidence-selection prior to a root-cause conclusion",
        "evidence_available_at_time": [
          "Vendor-confirmed documented seal-material lot change",
          "In-house teardown results already consistent with that same cause",
          "Known 3-week lab lead time that would breach the RCB deadline"
        ],
        "required_textual_manifestation": "The engineer explicitly acknowledges the existing evidence already points to the seal-material cause, yet still commissions the external assay 'to be thorough' or 'more defensible,' and afterward confirms the assay added no new decision-relevant finding.",
        "plausible_nonbias_interpretation": "A cautious engineer might reasonably want independent verification before a fleet-wide safety recommendation, which could look prudent rather than biased if not explicitly tied to the deadline and lack of decision impact.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "information bias",
          "cognitive bias",
          "the idea that more information was sought without regard to usefulness"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition scenario with no paired control requested."
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
      "Confirm exactly four decision points are present in the narrative, each with at least two plausible alternatives.",
      "Confirm the single information-bias instance appears only at decision point 3 and nowhere else in the interview.",
      "Confirm the interview never uses the terms 'information bias,' 'cognitive bias,' or any bias taxonomy language.",
      "Confirm the assay's eventual result is described as adding no new decision-relevant information, distinguishing the instance from a merely cautious, justified verification step.",
      "Confirm total word count falls between 1,215 and 1,485 words, target 1,350.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm consequences (RCB approval, no further in-service events) do not themselves prove or disprove that the assay request was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Information bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as seeking additional data that cannot change the pending corrective-action decision, motivated by a belief that more information improves decision quality/defensibility rather than by actual decision relevance."
      }
    ],
    "target_bias_names": [
      "Information bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Information bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "mechanism": "Commissioning a costly, schedule-delaying external metallurgical assay that duplicates already-sufficient vendor and in-house evidence, pursued because more information is assumed to be inherently valuable/defensible rather than because it can change the corrective-action recommendation.",
        "affected_reasoning_operation": "Evidence-sufficiency assessment prior to finalizing a root-cause-based recommendation",
        "evidence_source": "External metallurgical assay request vs. existing vendor lot documentation and in-house teardown results",
        "distinctiveness_requirement": "Single instance only; must not be echoed as a second, differently-worded instance at any other decision point, probe, or hypothetical."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_1",
    "domain_id": "AV",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point (phase 3, evidence-selection prior to corrective-action recommendation) offering the best mechanism fit for information bias, where sufficient decision-relevant evidence already existed and additional information-seeking could not alter the outcome; no split across multiple points was needed since occurrences = 1.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
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
        "segment_type": "role_and_threshold_reasoning",
        "raw_interview_anchor": "Monitoring repetitive write-ups and deciding when a case crosses from normal noise into formal corrective action.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive decision criterion without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_escalation_reasoning",
        "raw_interview_anchor": "The third write-up was unusual, but fleet-wide removal remained within MTBUR; the participant opened a focused review rather than declaring a fleet issue.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Evidence-weighted escalation decision without a hidden bias."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_integration",
        "raw_interview_anchor": "A second tail showed a similar complaint; difficult bench testing suggested an intermittent fault, and both tails shared a valve lot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Working-hypothesis update from new evidence without a hidden bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "interim_action_rationale",
        "raw_interview_anchor": "Repeated MEL carryover was a flag, but grounding was unsupported by the evidence; the participant imposed a one-leg MEL limit and opened an investigation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Balanced operational restriction without a hidden bias."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "root_cause_evidence_assessment",
        "raw_interview_anchor": "Vendor documentation and in-house teardown both pointed to the same seal-material cause.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Assessment of convergent existing evidence before the assay decision."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "evidence_selection_and_submission_timing",
        "raw_interview_anchor": "The participant already regarded lot-bounded replacement as settled, nevertheless commissioned a three-week external assay for thoroughness, and held the submission despite knowing the assay could not change the recommendation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["ib_01"],
        "ground_truth_rationale": "The sole hidden Information bias instance: non-decision-relevant additional data was sought for reassurance or perceived thoroughness, causing a deadline miss."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "final_corrective_action_rationale",
        "raw_interview_anchor": "The participant chose replacement limited to the identified vendor lot rather than a fleet-wide swap or deferral.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Scope selection followed lot-specific evidence."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_reasoning",
        "raw_interview_anchor": "In hindsight, the participant said the lot-based request should have been submitted on the original timeline without waiting for the assay.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Retrospective reconsideration of the already mapped occurrence, not a second occurrence."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "counterfactual_follow_up_reasoning",
        "raw_interview_anchor": "A different assay result would have triggered a follow-up investigation, not delayed the original submission.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Counterfactual response without an additional bias instance."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "prospective_process_reasoning",
        "raw_interview_anchor": "For a future case, the participant would ask whether extra data could change the recommendation or merely improve the file.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Prospective process adjustment without a new manifested occurrence."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis of a reliability engineer's self-reported reasoning during an APU bleed air valve corrective-action decision, focusing on the decision to obtain an external lab assay after already settling on a lot-based replacement recommendation."
  },
  "identified_bias_summary": [
    {
      "bias_label": "information bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "information bias",
      "alternative_labels": [
        "non-instrumental information seeking",
        "over-testing bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek or acquire information even when it cannot affect the decision or action at issue, often because the additional information provides reassurance or perceived thoroughness rather than instrumental decision value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to send the APU bleed air valve for an external lab assay after already deciding the corrective action and before the RCB deadline.",
      "decision_point_description": "Whether to send the valve sample to an external metallurgical lab for an independent composition assay despite having vendor lot documentation and an in-house teardown that already supported the lot-bounded replacement recommendation.",
      "affected_reasoning_operation": "Information acquisition and testing decision prior to finalizing the Reliability Control Board submission.",
      "bias_specific_mechanism": "The participant sought an additional independent test even though he explicitly stated that the result would not change his recommendation; the test was pursued for reassurance and file completeness rather than for information that could alter the action.",
      "manifestation_in_interview": "The participant sent the valve for an external three-week assay while knowing it would cause the RCB deadline to be missed and while stating that the lot-based replacement recommendation was already settled regardless of what the assay would show.",
      "effect_on_reasoning_or_decision": "The final recommendation was delayed beyond the RCB deadline even though the decision itself was not pending on the external result; the assay ultimately confirmed existing findings and did not change the corrective action.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The vendor's lot documentation and our own teardown already lined up on the seal material as the cause, and honestly I'd already decided in my own head that the corrective action was going to be a lot-bounded replacement — that part felt settled. But there was still an option to send the valve out to an external metallurgical lab for an independent composition assay, on top of what I already had.",
          "evidence_explanation": "This shows the participant had already made the substantive recommendation decision before ordering the external assay, framing the assay as additional rather than decision-determining."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I sent it out anyway. I'd basically landed on the lot-based replacement regardless of what came back — I wasn't holding the recommendation open pending that result. I think I just wanted a third, fully independent source in the file alongside the vendor's own account of their material, so the package read as more thorough when it went to the board. I knew the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back, and I sent it anyway.",
          "evidence_explanation": "This is the core evidence: he ordered information that he knew would not change the recommendation, would delay the decision, and was sought mainly for perceived thoroughness and reassurance."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The recommendation was already written in my head — vendor records and physical teardown agreed, and that's what the corrective action request was going to be built on either way. I think I was after the reassurance of having one more test in the folder more than anything that would've moved the decision itself.",
          "evidence_explanation": "This directly states that the additional test was not intended to move the decision, distinguishing non-instrumental information seeking from ordinary decision-support evidence gathering."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized with hindsight that he likely should have submitted on the original timeline and let the RCB decide using the vendor and teardown evidence. He also stated that if the assay had shown a different degradation mechanism, he would have opened a separate follow-up investigation, suggesting he was not closed to disconfirming evidence, but that such information would not have changed the already-settled current recommendation. The extra test could arguably be justified as risk management or board-facing thoroughness, but the participant's own account indicates it was non-instrumental for the decision itself.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper corpus passages were available in the provided context. The label 'information bias' is applied from established cognitive-science knowledge; retrieved corpus support was unavailable.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided, so the analysis relies on general cognitive-science knowledge rather than retrieved scientific sources.",
    "The transcript is a single self-report reconstruction and may not fully capture the participant's real-time reasoning or organizational factors."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Biased_1_Sonar_off",
  "interview_id": "AV_Biased_1",
  "system_prompt_id": "Sonar",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
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
