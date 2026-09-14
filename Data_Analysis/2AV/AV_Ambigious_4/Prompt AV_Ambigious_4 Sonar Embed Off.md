You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down for this. Same as before — this is a confidential debrief for training research, not a personnel review. I'll ask you to walk through a specific check ride in detail. Okay to go ahead?

Participant: Sure. This one was a Line Check, OPC cycle, on a senior widebody captain — very experienced, long time on type. I was up front as the TRE.

Interviewer: What was the flight meant to accomplish, and what was your role?

Participant: Standard revenue sector. I'm there to evaluate his technical handling and CRM for the recurrent check, intervening only if there's a safety need. First officer was PM.

Interviewer: Take me through what happened, from the start.

Participant: Before we got out to the aircraft, I looked at the tech log. One prior flight had logged an ADIRU 2 advisory — it cleared on its own in flight. Maintenance inspected it on the ground, couldn't confirm a fault on their test, but they went ahead and replaced a connector they suspected as a precaution. So it wasn't a clean bill of health exactly — more like "we think we found it, but we're not certain." We talked about that briefly during the walk-around. Departure was normal. Climbing through about FL250 we got a caution — an IRS align caution, not the same wording as the previous flight's advisory — and it cleared in maybe ten seconds. No checklist auto-triggered. Later in cruise, a different thing came up entirely — nothing to do with the ADIRU. The captain was working a minor non-normal checklist for an unrelated caution, and there was a verification step in it that takes a while and doesn't affect safety of flight. He told the FO he'd hold that one and come back to it once things settled down, which he did later in cruise. Everything else on the flight was uneventful. Normal approach and landing.

Interviewer: What happened after landing?

Participant: I wrote the report, graded the performance. A colleague — another TRE — looked at it and asked whether I'd have graded the deferred checklist item the same way with a different crew pairing. I told him honestly I wasn't sure. A few days later maintenance said the replaced connector had been seated correctly and they couldn't tie it definitively to either the first flight's advisory or ours. So the picture's still not fully closed.

Interviewer: Let's go back to the tech log discussion before departure. What went through your mind?

Participant: There were two things pulling in different directions. On one hand, maintenance had physically done something — replaced a part — not just signed a form. That counts for something. On the other hand, their own test didn't confirm a fault, so the replacement was really a guess about what might have caused it. I raised that with the captain — that we were accepting the aircraft on the strength of an educated guess, not a confirmed fix.

Interviewer: Did you consider asking maintenance control for more before departure?

Participant: I thought about asking whether they'd tested the replaced connector under load, not just visually. I didn't end up asking. Partly schedule, partly that it felt like it might not have changed anything practical — if they said yes, fine, if they said no, we'd probably still have gone. So there wasn't a single clean reason either way.

Interviewer: What would have had to be different for you to hold the flight?

Participant: Honestly, I go back and forth on that. If the write-up had said "fault confirmed, unresolved," that's different. What we had was murkier — inspected, not confirmed, acted on anyway. I can see an argument for going and an argument for waiting.

Interviewer: Move to the climb, when the caution came up. Walk me through that.

Participant: The caution came up, cleared in about ten seconds, no checklist triggered. I remember specifically noting to the captain that this wasn't the same wording as the previous flight's write-up — different system behavior, not obviously connected. That mattered to me because I didn't want either of us assuming it was "the same thing again" when it might not be.

Interviewer: What alternative did you weigh?

Participant: Leveling off to watch a couple more parameters before continuing. I considered it. In the end the absence of a checklist trigger carried more weight, but I wouldn't say it was an easy call — an ADIRU-adjacent caution always has some amount of "we don't fully know what's behind this" to it, regardless of how it presents.

Interviewer: How confident were you in that read at the time?

Participant: Moderately. Not fully confident, not dismissive either. I flagged the uncertainty out loud rather than treating it as settled.

Interviewer: Now cruise, when the captain deferred that checklist step. How did you evaluate that?

Participant: He explained his reasoning to the FO — the item doesn't affect flight safety, he'd come back to it, and he did. The checklist itself allows some latitude on sequencing non-critical items. So there's a real basis for calling that acceptable. At the same time, a stricter reading of the manual might say any deferral should be flagged differently regardless of the rationale. I noted both readings in the report rather than picking one as obviously correct.

Interviewer: If a newer captain had made the identical call, would you have graded it the same?

Participant: I've genuinely thought about that and I don't have a settled answer. Possibly yes, because the rationale and outcome would be identical. Possibly not, if I'd want to see more explicit checklist referencing from someone earlier in their career. I can argue it either way.

Interviewer: Last one — the peer's question afterward about whether your standard would hold for a different crew pairing. How did you respond?

Participant: I told him it was a fair question and I wasn't sure. I've had mixed views on this myself across different checks — sometimes I think the standard should be identical regardless of who's flying, other times I think context legitimately matters. I suggested we bring it up at the next standardization meeting rather than me just deciding it on the spot.

Interviewer: Is there anything that would have changed your mind on any of these calls?

Participant: If the connector issue had turned out to be confirmed and unresolved, the dispatch call looks different in hindsight. If the deferred checklist item had caused any downstream problem, that grading looks different too. But neither of those things happened, so I'm left without a clean answer on which reading was right.

Interviewer: Last question — if you ran this same flight again with the same information, what would you do differently?

Participant: I might ask maintenance control the load-test question next time, mostly for the record. Beyond that, I honestly don't know that I'd change the calls themselves. I can see reasonable people landing on either side of each one.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Ambigious_4",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Check Airman / Type Rating Instructor (TRI/TRE)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "ADIRU Advisory During Line Check: A Check Airman's Judgment Under Genuine Uncertainty",
    "scenario_summary_internal": "A veteran Type Rating Examiner (TRE) conducts a scheduled Line Check/OPC on a senior widebody captain during a revenue flight. A previously logged, ambiguously-resolved ADIRU advisory resurfaces briefly during climb and again in a different form during cruise, forcing the TRE to make four judgment calls under incomplete information: accepting the aircraft at dispatch, responding to a transient advisory in climb, grading the captain's handling of a minor procedural deviation in cruise, and interpreting a peer's question about his own process during debrief. Each decision is genuinely underdetermined - defensible on multiple grounds - and the eventual maintenance finding does not resolve which considerations actually drove the TRE's reasoning at the time.",
    "occupational_realism": {
      "objective": "Complete a scheduled Line Check / Operator Proficiency Check (OPC) on a type-rated captain while maintaining safe operation of the aircraft, correctly grading crew performance, and responding appropriately to an emergent avionics advisory.",
      "setting": "Flight deck of a twin-aisle commercial aircraft during a scheduled passenger revenue flight, TRE occupying the observer/jump seat with check-ride authority, captain as Pilot Flying under evaluation, first officer as Pilot Monitoring.",
      "constraints": [
        "Fixed check-ride syllabus with limited time to complete required evaluation items",
        "Dispatch reliability and schedule pressure from operations control",
        "MEL (Minimum Equipment List) sign-off already completed by maintenance before the flight",
        "TRE must both observe and simultaneously grade CRM and technical performance",
        "Limited real-time diagnostic data on an intermittent avionics advisory",
        "Passengers and revenue schedule create incentive to avoid unnecessary diversion or turnback"
      ],
      "stakeholders": [
        "Type Rating Examiner (TRE) / Check Airman",
        "Line Captain under evaluation",
        "First Officer (Pilot Monitoring)",
        "Maintenance Control",
        "Operations Control / Dispatch",
        "Fellow Check Airman (peer, post-flight)"
      ],
      "technical_terms_to_use": [
        "ADIRU", "advisory", "EICAS", "QRH", "MEL", "OPC", "Line Check",
        "CRM", "cross-check", "non-normal checklist", "tech log", "PF/PM",
        "V1", "memory items", "dispatch release"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias", "heuristic", "anchoring", "overconfidence",
        "blind spot", "normalcy bias", "illusion of validity", "expert intuition bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tech log shows one prior flight with an ADIRU 2 advisory that cleared during flight",
          "Maintenance inspected the unit, found no fault confirmed on ground test, but preemptively replaced a suspect connector as a precaution",
          "Aircraft is on schedule with a full passenger load"
        ],
        "new_information_after_decision": [
          "A different, milder advisory (a brief IRS align caution, not the same ADIRU miscompare) appears during climb in Phase 2"
        ],
        "alternatives": [
          "Accept the aircraft as dispatched, treating the preventive part replacement as adequate closure",
          "Request confirmation from maintenance control that the replaced connector was tested under load before departure"
        ],
        "intended_action": "TRE and captain discuss the tech log entry and the preventive part replacement, weigh both the maintenance action taken and the schedule pressure, and decide to accept dispatch, with the TRE noting both supporting and countervailing considerations aloud rather than settling the matter on a single rationale."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Brief IRS align caution appears on EICAS during climb through FL250 and clears within about ten seconds",
          "No non-normal checklist is triggered by the system",
          "TRE is aware the previous flight's ADIRU advisory was a different symptom, not identical to this one"
        ],
        "new_information_after_decision": [
          "In cruise, the captain later encounters a distinct, unrelated minor procedural choice point rather than a recurrence of the same advisory"
        ],
        "alternatives": [
          "Continue the climb, noting the advisory did not match the exact prior symptom and did not trigger a checklist",
          "Level off briefly to monitor additional parameters before continuing, given that any ADIRU-related caution carries some irreducible uncertainty"
        ],
        "intended_action": "TRE recommends continuing the climb while explicitly flagging to the captain that the current advisory is not the same as the previous flight's, and that the decision rests on the absence of a checklist trigger and on operational judgment under an uncertain, only partially analogous situation."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "In cruise, the captain skips a non-critical, time-consuming verification step in a minor non-normal checklist for an unrelated caution, citing that the item does not affect flight safety and can be completed later",
          "The captain explains the reasoning to the first officer, who agrees but notes it should be documented",
          "The item is completed later in cruise once workload decreases"
        ],
        "new_information_after_decision": [
          "The checklist item is completed without incident before descent, and no adverse effect is observed"
        ],
        "alternatives": [
          "Grade the deviation as an acceptable, explained prioritization decision consistent with published guidance on sequencing non-critical items",
          "Grade the deviation as a procedural nonconformance requiring debrief, regardless of the stated rationale or eventual completion"
        ],
        "intended_action": "TRE grades the captain's handling as satisfactory, citing both the captain's explicit verbal rationale to the crew and the checklist's own allowance for deferring non-critical items, while also noting in the report that a stricter reading of the manual could support a different grade."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Flight lands uneventfully; TRE begins writing the check report",
          "A fellow TRE, reviewing the report informally, asks whether the grading standard applied would have been the same for a different crew pairing",
          "TRE has handled similar deferred-item situations before, with mixed views on the correct standard"
        ],
        "new_information_after_decision": [
          "Maintenance later finds the replaced connector was seated correctly and cannot conclusively link it to either advisory, leaving the underlying cause only partially explained"
        ],
        "alternatives": [
          "Tell the peer that the same standard would likely apply regardless of crew pairing, while acknowledging the question is fair and worth documenting more explicitly next time",
          "Tell the peer that crew pairing probably does affect how such judgment calls get made, without specifying whether that is appropriate or not"
        ],
        "intended_action": "TRE responds to the peer's question with genuine uncertainty, acknowledging that he isn't fully sure whether his grading standard would transfer identically to a different crew, and proposes discussing it further at the next check-airman standardization meeting rather than resolving the question himself."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this flight was supposed to accomplish and your role in it?",
        "What was your initial impression of the aircraft and crew before departure?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you notice at each stage of the flight?",
        "What information did you have in front of you at each point, and where did it come from?",
        "What changed between what you expected and what actually occurred?"
      ],
      "decision_point_probes": [
        "What cues led you to accept/continue/grade the situation the way you did at this point?",
        "What information sources did you rely on, and were there others you could have consulted?",
        "What were you trying to achieve at that moment, and did that goal compete with anything else?",
        "What alternatives did you consider, and why did you weigh them the way you did?",
        "What was the basis for your decision — was there a single deciding factor or several?",
        "Had you seen something like this before, and how did that shape your response?",
        "How much time pressure did you feel, and did that affect how you gathered information?",
        "How confident were you in your read of the situation at the time, versus in hindsight?",
        "If the information had been slightly different, or if a different pilot had been flying, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If you had to do this flight again with the same information, what would you do differently, if anything?",
        "If a less experienced captain had made the same call in Phase 3, would you have graded it the same?",
        "How do you think other check airmen might have handled the same sequence of events?",
        "What would it take to convince you that one of your calls that day should have gone the other way?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "AV_Biased_4",
      "features_to_match": [
        "Domain (aviation), role (Check Airman/TRE), setting (Line Check/OPC on a senior widebody captain)",
        "Four-decision-point structure covering dispatch acceptance, in-flight advisory response, evaluative grading, and post-flight reflection",
        "Technical vocabulary set (ADIRU, EICAS, QRH, MEL, tech log, CRM, cross-check)",
        "Stakeholder roster (TRE, captain, first officer, maintenance control, ops control, peer TRE)",
        "Emotional tone (measured, professional, reflective) and difficulty level (challenging)",
        "Approximate word count and dialogue format"
      ],
      "features_to_remove_or_change": [
        "Remove the repeated identical self-clearing pattern used as a predictive basis (replaced with a non-identical, only partially analogous advisory)",
        "Remove the seniority-substitutes-for-verification grading rationale (replaced with a dual-rationale grading tied to explicit crew communication and published checklist allowance)",
        "Remove the categorical self-exemption from a peer's critique (replaced with genuine, unresolved uncertainty about whether the standard would transfer to a different crew)",
        "Remove the dispatch-history-as-proof-of-safety reasoning (replaced with an explicit acknowledgment of both supporting and countervailing considerations)"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined: the textual evidence must support at least two plausible readings (a defensible operational judgment and a less careful one) without the interview supplying a clear marker that tips the reasoning into any of the four target mechanisms. The TRE's language should include explicit hedges, acknowledgment of counterarguments, or open questions at each decision point, rather than a confident, single-basis justification of the kind used in the paired biased scenario."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable; no counterfactual condition requested for this generation.",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly 4 decision points present, matching the paired biased scenario's structure",
      "Each decision point offers at least two plausible alternatives with genuine ambiguity",
      "No decision point contains a confident, single-basis justification matching any of the four target bias mechanisms",
      "No bias labels, definitions, or psychological terminology appear in probes or narrative",
      "Consequences (successful landing, inconclusive maintenance finding) leave open multiple interpretations of each decision",
      "Target word count 1,215-1,485 words achievable given 4 timeline phases plus probe responses without repetitive exposition",
      "Zero intended instances of Bias Blind Spot, Normalcy Bias, Experience Bias or Trusting expert intuition, and Illusion of validity are embedded"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Bias Blind Spot",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Normalcy Bias",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Experience Bias or Trusting expert intuition",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 0,
        "mechanism_constraint": "Not applicable; zero occurrences required for this control condition."
      }
    ],
    "target_bias_names": [
      "Bias Blind Spot",
      "Normalcy Bias",
      "Experience Bias or Trusting expert intuition",
      "Illusion of validity"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bias Blind Spot", "requested_occurrences": 0 },
      { "bias": "Normalcy Bias", "requested_occurrences": 0 },
      { "bias": "Experience Bias or Trusting expert intuition", "requested_occurrences": 0 },
      { "bias": "Illusion of validity", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "AV_Biased_4",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Ambigious_4",
    "domain_id": "AV",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, so no bias instances are planned. Decision points are instead structured to mirror the paired biased scenario's mechanism-fit locations (dispatch acceptance, in-flight advisory response, evaluative grading, post-flight reflection) while each is written to remain genuinely underdetermined between a defensible judgment and a less careful one, without resolving into any target bias mechanism.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and role (aviation, Check Airman/TRE)",
      "Setting (Line Check/OPC on a senior widebody captain, revenue flight)",
      "Four-decision-point structure and ordering",
      "Stakeholder roster and interaction pattern",
      "Technical vocabulary level and terminology set",
      "Difficulty level (challenging) and approximate word count",
      "Dialogue format and emotional tone"
    ],
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
        "segment_type": "role_and_intervention_rationale",
        "raw_interview_anchor": "Standard revenue sector. I'm there to evaluate his technical handling and CRM for the recurrent check, intervening only if there's a safety need.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Defines the participant's evaluation objective and intervention threshold; no hidden bias instance is planned in this zero-bias control."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "dispatch_evidence_weighting",
        "raw_interview_anchor": "There were two things pulling in different directions. On one hand, maintenance had physically done something — replaced a part — not just signed a form. That counts for something. On the other hand, their own test didn't confirm a fault, so the replacement was really a guess about what might have caused it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly weighs supporting and countervailing evidence; the control specification requires no bias instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "maintenance_information_choice",
        "raw_interview_anchor": "I thought about asking whether they'd tested the replaced connector under load, not just visually. I didn't end up asking. Partly schedule, partly that it felt like it might not have changed anything practical — if they said yes, fine, if they said no, we'd probably still have gone.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explains a contemplated information-gathering action and competing practical considerations without a hidden bias mechanism."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "dispatch_threshold_reflection",
        "raw_interview_anchor": "Honestly, I go back and forth on that. If the write-up had said 'fault confirmed, unresolved,' that's different. What we had was murkier — inspected, not confirmed, acted on anyway. I can see an argument for going and an argument for waiting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States a conditional threshold and preserves competing interpretations; no hidden instance exists."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "climb_symptom_differentiation",
        "raw_interview_anchor": "I remember specifically noting to the captain that this wasn't the same wording as the previous flight's write-up — different system behavior, not obviously connected. That mattered to me because I didn't want either of us assuming it was 'the same thing again' when it might not be.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Distinguishes current and prior symptoms and guards against an unsupported assumption; no hidden bias instance is planned."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "climb_action_choice",
        "raw_interview_anchor": "Leveling off to watch a couple more parameters before continuing. I considered it. In the end the absence of a checklist trigger carried more weight, but I wouldn't say it was an easy call — an ADIRU-adjacent caution always has some amount of 'we don't fully know what's behind this' to it, regardless of how it presents.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Weighs an alternative against checklist evidence while retaining uncertainty; candidate cand_001 localizes here but the hidden control has no positive instance."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "confidence_and_communication",
        "raw_interview_anchor": "Moderately. Not fully confident, not dismissive either. I flagged the uncertainty out loud rather than treating it as settled.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Expresses calibrated confidence and an uncertainty disclosure; no hidden instance."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "checkride_grading_rationale",
        "raw_interview_anchor": "He explained his reasoning to the FO — the item doesn't affect flight safety, he'd come back to it, and he did. The checklist itself allows some latitude on sequencing non-critical items. So there's a real basis for calling that acceptable. At the same time, a stricter reading of the manual might say any deferral should be flagged differently regardless of the rationale. I noted both readings in the report rather than picking one as obviously correct.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Gives a dual-basis evaluation and records the stricter alternative; no hidden bias occurrence is present."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "seniority_counterfactual",
        "raw_interview_anchor": "I've genuinely thought about that and I don't have a settled answer. Possibly yes, because the rationale and outcome would be identical. Possibly not, if I'd want to see more explicit checklist referencing from someone earlier in their career. I can argue it either way.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Considers whether seniority would alter grading but does not endorse a distortion; candidate cand_002 localizes here and remains a false alarm at the candidate threshold."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "peer_challenge_response",
        "raw_interview_anchor": "I told him it was a fair question and I wasn't sure. I've had mixed views on this myself across different checks — sometimes I think the standard should be identical regardless of who's flying, other times I think context legitimately matters. I suggested we bring it up at the next standardization meeting rather than me just deciding it on the spot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Responds to a process challenge by acknowledging uncertainty and escalating for standardization; no hidden instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "outcome_counterfactual_reflection",
        "raw_interview_anchor": "If the connector issue had turned out to be confirmed and unresolved, the dispatch call looks different in hindsight. If the deferred checklist item had caused any downstream problem, that grading looks different too. But neither of those things happened, so I'm left without a clean answer on which reading was right.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly frames adverse outcomes as counterfactual and withholds a definitive conclusion; candidate cand_003 localizes here but no hidden instance exists."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "repeat_flight_change_choice",
        "raw_interview_anchor": "I might ask maintenance control the load-test question next time, mostly for the record. Beyond that, I honestly don't know that I'd change the calls themselves. I can see reasonable people landing on either side of each one.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Identifies a modest process change while preserving ambiguity about the substantive calls; no hidden instance."
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
    "analysis_scope_note": "No retrieved scientific-paper corpus passages were supplied. The analysis therefore uses a conservative, mechanism-first standard based on general cognitive-science knowledge, and no identified occurrence has retrieved corpus support."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "outcome bias",
      "alternative_labels": [
        "outcome-dependent evaluation",
        "resulting bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-flight evaluation of the captain's deferred checklist item",
      "supporting_interview_quote": "If the deferred checklist item had caused any downstream problem, that grading looks different too. But neither of those things happened, so I'm left without a clean answer on which reading was right.",
      "plausible_mechanism": "Evaluating the quality of the captain's decision to defer a non-critical checklist step partly by the downstream outcome rather than solely by the decision process, information available at the time, and the operative checklist authority.",
      "why_not_identified": "The statement is a hypothetical counterfactual about what would have changed the participant's view, not affirmative evidence that the actual grading was based on outcome. The participant also reports recording both readings rather than selecting one as obviously correct."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "halo effect",
      "alternative_labels": [
        "experience-based leniency",
        "reputation-based leniency"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Consideration of whether the captain's experience affected grading of the deferred checklist item",
      "supporting_interview_quote": "I've genuinely thought about that and I don't have a settled answer. Possibly yes, because the rationale and outcome would be identical. Possibly not, if I'd want to see more explicit checklist referencing from someone earlier in their career. I can argue it either way.",
      "plausible_mechanism": "A senior captain's extensive experience and long time on type could favorably influence the evaluator's judgment of the same action that might be graded more strictly for a junior pilot.",
      "why_not_identified": "The participant does not report actually grading differently by crew seniority or experience. He explicitly states uncertainty and brings the issue to standardization rather than endorsing a differential standard."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "No retrieved scientific-paper corpus was provided, so no identified occurrence could be grounded in retrieved support.",
    "The interview contains substantial reflective and debiasing language, so absence of identified occurrences does not imply definitive absence of all biased cognition.",
    "Candidate biases are included where a bias mechanism was plausible but lacked sufficient affirmative evidence for identification even at low confidence."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Ambigious_4_Sonar_off",
  "interview_id": "AV_Ambigious_4",
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
