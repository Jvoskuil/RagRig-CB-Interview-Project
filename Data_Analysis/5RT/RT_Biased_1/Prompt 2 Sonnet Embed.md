You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. Just to confirm before we start — this is a routine cognitive task analysis interview, not an investigation. Nothing you say here goes into a disciplinary file, and you can decline any question. Comfortable to proceed?

Participant: Yeah, that's fine, happy to go through it.

Interviewer: Great. Can you tell me your role and how long you've been controlling this branch?

Participant: I'm a Rail Traffic Controller, six years on this desk, mostly overnight and weekend turns. I cover the Falcon Bank branch pretty regularly — it's single line, absolute block working, so only one train in the section at a time.

Interviewer: And what's a normal possession handback look like on a section like that?

Participant: Gang foreman calls in on the trackside telephone, confirms the line's clear of personnel and equipment, I log the time, and then it's back to normal working. Nothing unusual about that part.

Interviewer: Walk me through what actually happened that night.

Participant: Handback came through at 23:40, all routine. I had 6M42, a freight, sitting at the entry signal waiting for the road, and 2T19, a passenger service, running about eighteen minutes late further up the line. Objective was simple enough — get 6M42 through Falcon Bank and get 2T19 back on time without anyone sitting in a queue longer than they needed to. Shortly after the handback, the track circuit for the section showed occupied for about four seconds, then cleared. It did that twice in ten minutes. Light rain had just started.

Interviewer: What went through your mind when you saw that?

Participant: Honestly, my first thought was "here we go again." That circuit's had three nuisance trips in the last eight months, all rain or leaf-fall related, all logged. So I looked at it and thought, that's the same signature — short blip, self-clears, no correlation with anything physically on the track. It fit the pattern well enough that I didn't feel I needed to chase it further.

Interviewer: What alternatives did you actually have at that point?

Participant: I could've rung the foreman again on the trackside phone to get him to re-walk it, or got the on-call technician out to test the circuit, or gone to pilotman working as a precaution. All were on the table.

Interviewer: What made you choose to just proceed?

Participant: The pattern, mostly. Three prior trips, same weather trigger, same short duration. It read like the circuit doing its usual thing. Calling the foreman back would've meant holding 6M42 another ten, fifteen minutes for what I was fairly confident was nothing, and pilotman working is even longer than that to arrange. Once I had it slotted into that nuisance-trip bucket in my head, verifying it didn't feel like it was really adding anything — I'd already accounted for it, if that makes sense.

Interviewer: How confident would you say you were, on reflection, that it was genuinely just the nuisance trip and not something else?

Participant: At the time, quite confident — enough that I didn't feel the need to build in a check. Looking back, I suppose I treated it as basically closed rather than just "probably fine but still open." I gave 6M42 the road.

Interviewer: What happened next?

Participant: 6M42 entered the section, and for a few minutes everything was quiet — no more flickers, so it looked like a good call at that point. Then the foreman came back on the radio to do his readback, confirming the gang and equipment were fully clear, but the transmission was garbled by static. I caught "clear" and something like "trolley," but it wasn't a full clean readback.

Interviewer: What were your options there?

Participant: Accept it as good enough since the formal handback had already happened before that call, try to re-raise him for a clean repeat, or ring my supervisor to get a second opinion on whether a partial transmission was adequate.

Interviewer: Which did you go with, and why?

Participant: I logged it as adequate. The handback itself was already formally done and clean at 23:40 — this was just the follow-up readback, and the gang was already moving off to their next job, so re-contacting wasn't straightforward. No rule had actually been broken; the section was already possession-free by the book. It felt like a reasonable judgment call given what I had, not a great one, but reasonable.

Interviewer: Then what?

Participant: Weather got worse. Rain picked up, and a junction signal further along — separate from Falcon Bank — started throwing intermittent signal failure warnings. 2T19 was approaching that junction and needed a routing call within a couple of minutes.

Interviewer: What were you weighing there?

Participant: Send it through on the affected signal relying on backup indication and the driver's caution, divert it onto the loop line which adds six minutes, or hold it at the previous station until the fault's diagnosed. Meanwhile 6M42 was still moving through Falcon Bank fine, no further anomalies.

Interviewer: What did you decide?

Participant: I sent 2T19 round the loop. That signal issue felt different in character — a live "failure" warning rather than a short clean blip — and I didn't have any history on that particular fault to lean on, so I wasn't willing to trust backup indication on an unfamiliar problem. Six minutes felt like a cheap price for not gambling on something I hadn't seen before.

Interviewer: Interesting that you treated that one differently to the Falcon Bank flicker.

Participant: Yeah — I didn't have a pattern to fall back on there, so holding back felt like the safer default. Turned out to be an unrelated relay fault, nothing to do with Falcon Bank at all, but I didn't know that at the time.

Interviewer: What happened after that?

Participant: The Falcon Bank circuit flickered again — same kind of brief occupied indication — but this time 6M42 was confirmed still inside the section. I finally got hold of the on-call technician, who told me the circuit's wiring has a known moisture-sensitivity problem that's never been fully run down. Driver of 6M42 reported nothing unusual, normal progress, no obstruction visible. And 2T19 was closing in behind, having rejoined the main line off the loop.

Interviewer: What options did you have at that point?

Participant: Carry on as normal and let 2T19 follow into Falcon Bank once clear, treating the second flicker the same way as the first. Suspend normal working and go to pilotman working for everything through that section until it's properly looked at. Or hold 2T19 short and get the technician to physically inspect before anything else moves.

Interviewer: What did you choose?

Participant: I went to pilotman working. Once the technician mentioned there was an actual unresolved wiring issue behind it, the flicker stopped feeling like the same closed case from earlier — it felt like there was something real and undiagnosed sitting underneath it, so I wanted a person physically controlling movement rather than relying on the circuit again.

Interviewer: Suppose everything else that night had stayed exactly the same — the weather, the maintenance log, the garbled readback, the junction fault, and how the wiring issue eventually turned out — but at that very first flicker you'd taken thirty seconds to ring the foreman back on the trackside phone before giving 6M42 the road. Do you think that changes anything about how you'd have gone into the rest of the night?

Participant: Probably, yeah. I still think the pattern would've weighed heavily either way — three prior trips is three prior trips. But if I'd made that one extra call and gotten a clean confirmation, I'd have gone into the rest of the shift with something on record rather than just my own read of the log. It wouldn't have changed the facts on the ground, but it might've meant I wasn't relying quite so much on the pattern doing all the work by itself.

Interviewer: Looking back, what would you change about the initial decision?

Participant: I'd probably still weigh the history heavily, but I think I'd want some cheap independent check alongside it rather than letting the pattern alone close the question. A quick call doesn't cost that much against holding a train.

Interviewer: What would need to change, procedurally, for you to verify faster next time?

Participant: Direct line to the technician's diagnostic panel instead of routing through the on-call rota — that delay probably shaped a couple of my later calls too.

Interviewer: Last one — how do you think a colleague would've handled that first flicker?

Participant: Honestly, most of the desk would've read it the same way I did. That log is well known on our shift. Whether that's the right instinct or not, I couldn't tell you for certain — nothing went wrong that night, but I know that doesn't prove it was the right call either.

Interviewer: That's a good place to stop. Thanks for your time.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Biased_1",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Rail Traffic Controller / Train Dispatcher",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Falcon Bank Nuisance Trip",
    "scenario_summary_internal": "Overnight, a Rail Traffic Controller manages handback of a single-track branch section (Falcon Bank) from engineering possession to traffic. An intermittent track circuit occupancy indication appears shortly after handback. The controller, drawing on a history of nuisance trips on this same circuit caused by rain and leaf-fall, treats the ambiguous indication as resolved/explained rather than genuinely uncertain, and authorizes a freight train into the section without independent verification. Subsequent events (a garbled foreman readback, worsening weather affecting a passenger train's routing, and a recurrence of the anomaly once the freight train is already in the section) force the controller through three further decisions, none of which mechanically prove whether the original call was biased or simply an unlucky but reasonable judgment.",
    "occupational_realism": {
      "objective": "Safely resume normal train working on a single-line branch after an engineering possession, minimizing delay to a following freight and a late-running passenger service while preserving safe separation between trains.",
      "setting": "A regional signalling control center overseeing a rural single-track branch (Falcon Bank block section) during the 23:30-01:00 overnight window, immediately after an engineering gang has handed back possession.",
      "constraints": [
        "Single line section with no parallel track for overtaking or bidirectional running",
        "Only one train may occupy the block section at a time under normal absolute block rules",
        "Worsening rain forecast affecting signal and track circuit reliability",
        "A late-running passenger service (2T19) needs to traverse the same section within the hour",
        "Pilotman working is available but takes 12-15 minutes to arrange and further delays both trains",
        "Trackside telephone confirmation from the gang foreman is the only independent verification method besides pilotman working",
        "Controller is solo on shift with a supervisor reachable only by phone"
      ],
      "stakeholders": [
        "Rail Traffic Controller (interviewee)",
        "Engineering gang foreman (possession handback)",
        "Freight train driver (6M42)",
        "Passenger train driver/guard (2T19)",
        "Signalling maintenance technician (on-call)",
        "Shift supervisor"
      ],
      "technical_terms_to_use": [
        "track circuit",
        "block section",
        "absolute block working",
        "possession handback",
        "single line working",
        "pilotman",
        "trackside telephone",
        "nuisance trip",
        "right of time",
        "signal box/control panel",
        "occupied/clear indication"
      ],
      "technical_terms_to_avoid": [
        "PTC (positive train control, US-specific)",
        "CTC (centralized traffic control, US-specific)",
        "generic 'red light' language without block terminology"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engineering gang foreman handed back Falcon Bank section as clear at 23:40",
          "Track circuit briefly displayed 'occupied' for approximately 4 seconds, then cleared, twice within 10 minutes",
          "Maintenance log shows three prior nuisance trips on this same circuit over the past 8 months, all attributed to rain ingress or leaf-fall on the rail",
          "Light rain has just begun in the area",
          "Freight 6M42 is standing ready at the section's entry signal awaiting authority to proceed"
        ],
        "alternatives": [
          "Authorize 6M42 to enter under normal absolute block working, treating the flickers as a known nuisance-trip pattern",
          "Call the gang foreman on the trackside telephone to reconfirm the line is physically clear before authorizing any movement",
          "Request the on-call signalling technician to inspect or test the circuit before resuming normal working",
          "Implement single line working with a pilotman as a precaution until the circuit behavior is explained"
        ],
        "intended_action": "Controller classifies the intermittent indication as a familiar nuisance trip based on the maintenance log pattern and authorizes 6M42 into the section without further verification.",
        "new_information_after_decision": [
          "6M42 departs and enters Falcon Bank section under normal working",
          "No further track circuit flicker is observed for several minutes afterward, giving the appearance the call was correct"
        ]
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "6M42 is now inside the block section",
          "Gang foreman's radio readback confirming all personnel and equipment clear was partially garbled by static, audible words include 'clear' and 'trolley' but the phrase is incomplete",
          "Foreman is not immediately reachable again as the gang has begun moving to their next worksite",
          "No rule violation has occurred yet; possession was formally handed back before the transmission"
        ],
        "alternatives": [
          "Accept the partial readback as sufficient given the formal handback already received",
          "Halt further movements and attempt to re-contact the foreman for a full readback before allowing 2T19 to approach",
          "Escalate to the shift supervisor for a second opinion on whether the partial transmission is adequate"
        ],
        "intended_action": "Controller logs the partial transmission as adequate confirmation and proceeds with normal planning for 2T19's approach, reasoning that the earlier formal handback already covers clearance.",
        "new_information_after_decision": []
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Rain has intensified; a separate signal at the branch junction is reporting intermittent 'signal failure' warnings unrelated to Falcon Bank",
          "2T19 (passenger, running 18 minutes late) is approaching the junction and needs a routing decision within the next few minutes",
          "An alternate loop line adds 6 minutes to 2T19's journey but avoids the affected junction signal entirely",
          "6M42 is still progressing through Falcon Bank with no further anomalies reported"
        ],
        "alternatives": [
          "Route 2T19 via the affected junction signal, relying on backup indication and driver caution",
          "Divert 2T19 via the alternate loop line to avoid the junction signal issue entirely",
          "Hold 2T19 at the previous station until the junction signal issue is diagnosed"
        ],
        "intended_action": "Controller diverts 2T19 via the loop line as a precaution, accepting the schedule delay to avoid relying on the unreliable junction signal.",
        "new_information_after_decision": [
          "2T19 proceeds via the loop with an additional 6-minute delay",
          "Junction signal issue is later found to be a separate, unrelated relay fault"
        ]
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The Falcon Bank track circuit flickers again, this time while 6M42 is confirmed to still be inside the section",
          "The on-call signalling technician, now reached, states the circuit's wiring has a known moisture-sensitivity issue that has not yet been fully diagnosed",
          "6M42's driver reports no visual obstruction and normal progress",
          "2T19 is now close behind on the same route, having rejoined the main line after the loop diversion"
        ],
        "alternatives": [
          "Continue normal working and allow 2T19 to follow 6M42 into Falcon Bank once clear, treating the second flicker as confirmation of the same known nuisance pattern",
          "Suspend normal working and implement single line working with a pilotman for all further movements through Falcon Bank until the fault is properly diagnosed",
          "Hold 2T19 short of the section and request the technician physically inspect the circuit before any further movement"
        ],
        "intended_action": "Controller implements single line working with a pilotman for 2T19 and future movements, while documenting the recurring flicker for the maintenance team.",
        "new_information_after_decision": [
          "Technician later confirms a genuine intermittent short in the track circuit cabling, aggravated by rain, consistent with but not identical to the earlier nuisance-trip pattern",
          "No safety incident occurred, but the fault is flagged for priority repair"
        ]
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what a normal possession handback looks like on a section like Falcon Bank?",
        "What was your overall objective that night, given the freight and the late passenger service?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from the handback at 23:40 through to the pilotman working decision.",
        "At what point did you first notice something unusual with the track circuit?",
        "What did you know about this circuit's history before that night?"
      ],
      "decision_point_probes": [
        "At the moment the flicker first appeared, what cues made you interpret it the way you did?",
        "What information sources did you have available, and which ones did you use or not use?",
        "What were you trying to achieve at that moment, and what alternatives did you consider?",
        "What was the basis for choosing to proceed rather than verify independently?",
        "Had you seen this kind of situation before, and how did that experience shape your response?",
        "How much time pressure did you feel you were under when you made that call?",
        "How confident were you that the indication was genuinely a nuisance trip versus something else?",
        "If the maintenance log had shown no prior nuisance trips on this circuit, would you have acted differently?"
      ],
      "closing_hypotheticals": [
        "If you could redo the initial decision with the benefit of hindsight, what would you change?",
        "What would need to be different about the tools or procedures for you to verify ambiguous indications faster?",
        "How do you think other controllers on your team would have handled the same flicker?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias",
        "decision_point": 1,
        "mechanism": "Controller encounters a genuinely ambiguous, intermittent signal (4-second occupancy flicker) and, rather than tolerating or investigating the uncertainty, forcibly resolves it into a certain, familiar category (past nuisance trips) that requires no further action, then acts on that resolved certainty without seeking the available independent verification.",
        "affected_reasoning_operation": "Evidence interpretation and decision to seek (or forgo) verification under ambiguity",
        "evidence_available_at_time": [
          "Intermittent 4-second occupied indication occurring twice in 10 minutes",
          "Maintenance log of three prior similar nuisance trips linked to rain/leaf-fall",
          "Onset of light rain at the same time",
          "Availability of trackside telephone confirmation and pilotman working as verification options"
        ],
        "required_textual_manifestation": "The controller's account should explicitly state that the flicker was treated as 'basically explained' or 'not worth chasing further' because of the prior pattern, and should describe skipping the telephone/pilotman verification step specifically because the uncertainty felt already resolved by the pattern-match, not because verification was impossible or procedurally unnecessary.",
        "plausible_nonbias_interpretation": "A controller could reasonably use base-rate pattern-matching from maintenance history as a legitimate operational heuristic under time pressure, especially if verification always takes 12-15 minutes and causes further delay; this alone would not indicate bias unless the account shows the controller treating residual uncertainty as fully eliminated rather than merely reduced.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "Do not name 'uncertainty rejection bias' or any bias term",
          "Do not have the controller say 'I ignored the uncertainty' in clinical/psychological language",
          "Do not have the narrator or interviewer label the reasoning as flawed"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no control scenario requested for this generation pass."
    },
    "counterfactual_specification": {
      "causal_variable": "Whether the controller sought independent verification (trackside telephone confirmation) of the intermittent track circuit indication before authorizing 6M42 into Falcon Bank",
      "original_state": "Controller does not seek verification; treats the flicker as an explained nuisance trip and authorizes movement immediately",
      "counterfactual_state": "Controller calls the trackside telephone to reconfirm the gang has fully cleared the section before authorizing movement, delaying 6M42 by several minutes but obtaining direct confirmation",
      "variables_to_hold_constant": [
        "Weather onset and progression",
        "Maintenance log history of the circuit",
        "Timing and content of the garbled foreman readback",
        "Junction signal fault affecting 2T19",
        "Final technician diagnosis of the genuine intermittent short"
      ],
      "expected_causal_difference": "In the counterfactual, the controller's later decisions (partial readback acceptance, loop diversion, final pilotman decision) would likely be made with a documented verification step already on record, altering how the recurring flicker in phase 4 is interpreted (as an escalation of a partly-verified issue rather than a repeat of an unverified assumption), but consequences would remain non-diagnostic of bias absent this manipulation.",
      "causal_test_question": "Does explicitly seeking trackside verification at decision point 1 change how confidently the controller commits to the nuisance-trip interpretation in decision point 4, independent of the eventual outcome?"
    },
    "generation_checks": [
      "Exactly one instance of Uncertainty Rejection Bias is planned, at decision point 1 only",
      "No other decision point contains an intentional instance of the named bias",
      "Decision points 2 and 3 use different reasoning failures (partial-information acceptance, precautionary diversion) that must not be coded as instances of the named bias",
      "Word count target of 1,350 (range 1,215-1,485) is achievable given four decision points with probes and one embedded bias instance, without repetitive exposition",
      "Consequences at each decision point are ambiguous with respect to whether the decision was well- or poorly-founded",
      "Technical vocabulary matches UK/Commonwealth-style single-line block working terminology consistently"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Uncertainty Rejection Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as premature resolution of a genuinely ambiguous/intermittent signal into a falsely certain category (pattern-matched to prior nuisance trips), coupled with forgoing an available verification action, rather than mere risk tolerance or time-pressure heuristic use alone."
      }
    ],
    "target_bias_names": [
      "Uncertainty Rejection Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Uncertainty Rejection Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias",
        "decision_point": 1
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias",
        "mechanism": "Forcible resolution of an ambiguous intermittent track circuit indication into a familiar, certain category (nuisance trip) based on maintenance history pattern-match, followed by forgoing available independent verification (trackside telephone or pilotman working) that would have addressed the residual uncertainty.",
        "affected_reasoning_operation": "Evidence interpretation under ambiguity and the decision to seek versus forgo verification",
        "evidence_source": "Maintenance log of prior nuisance trips combined with the live intermittent occupancy indication and onset of rain",
        "distinctiveness_requirement": "This is the only planned instance of this bias; it must be textually and causally distinct from the phase 2 partial-readback acceptance and phase 3 precautionary diversion, which are governed by different reasoning operations (acceptance of incomplete confirmation; risk-averse rerouting) and must not be coded as additional bias instances."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ub_01",
        "bias": "Uncertainty Rejection Bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Whether independent trackside verification was sought before authorizing movement into Falcon Bank",
      "original_state": "No verification sought; flicker treated as explained nuisance trip",
      "changed_state": "Verification sought via trackside telephone before authorizing movement",
      "variables_to_hold_constant": [
        "Weather onset and progression",
        "Maintenance log history of the circuit",
        "Garbled foreman readback content and timing",
        "Junction signal fault affecting 2T19",
        "Final technician diagnosis of the genuine intermittent short"
      ]
    },
    "scenario_id": "RT_Biased_1",
    "domain_id": "RT",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the strongest mechanism fit (ambiguous evidence requiring interpretation and a verification-seeking choice), per rule 2 of the allocation guidance; no spreading was needed since only one occurrence was requested.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Weather onset and progression",
      "Maintenance log history of the circuit",
      "Garbled foreman readback content and timing",
      "Junction signal fault affecting 2T19",
      "Final technician diagnosis of the genuine intermittent short"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {"segment_id":"seg_001","speaker":"Participant","segment_type":"evidence_interpretation","raw_interview_anchor":"Honestly, my first thought was 'here we go again.' That circuit's had three nuisance trips in the last eight months, all rain or leaf-fall related, all logged. So I looked at it and thought, that's the same signature — short blip, self-clears, no correlation with anything physically on the track. It fit the pattern well enough that I didn't feel I needed to chase it further.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"Prior-history pattern matching alone is a plausible operational cue; the target requires explicit premature closure of residual uncertainty and suppression of verification, which is most directly expressed later in seg_003."},
        {"segment_id":"seg_002","speaker":"Participant","segment_type":"resource_and_delay_tradeoff","raw_interview_anchor":"Calling the foreman back would've meant holding 6M42 another ten, fifteen minutes for what I was fairly confident was nothing, and pilotman working is even longer than that to arrange.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"A distinct delay-cost rationale. Time pressure or a legitimate operational tradeoff alone is explicitly a plausible non-bias interpretation."},
        {"segment_id":"seg_003","speaker":"Participant","segment_type":"uncertainty_resolution_and_verification_choice","raw_interview_anchor":"Once I had it slotted into that nuisance-trip bucket in my head, verifying it didn't feel like it was really adding anything — I'd already accounted for it, if that makes sense.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["ub_01"],"ground_truth_rationale":"Narrowest explicit manifestation: ambiguous evidence is forced into a familiar, effectively settled category and independent verification feels unnecessary."},
        {"segment_id":"seg_004","speaker":"Participant","segment_type":"retrospective_confidence_reflection","raw_interview_anchor":"At the time, quite confident — enough that I didn't feel the need to build in a check. Looking back, I suppose I treated it as basically closed rather than just 'probably fine but still open.' I gave 6M42 the road.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"An eligible retrospective restatement of the same unique decision, not a separate planned occurrence; ub_01 is mapped to its more specific contemporaneous rationale in seg_003."},
        {"segment_id":"seg_005","speaker":"Participant","segment_type":"partial_readback_acceptance","raw_interview_anchor":"I logged it as adequate. The handback itself was already formally done and clean at 23:40 — this was just the follow-up readback, and the gang was already moving off to their next job, so re-contacting wasn't straightforward. No rule had actually been broken; the section was already possession-free by the book. It felt like a reasonable judgment call given what I had, not a great one, but reasonable.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"A separate phase-2 procedural-status judgment. Hidden validation explicitly excludes this partial-readback episode from the target; formal handback was already complete."},
        {"segment_id":"seg_006","speaker":"Participant","segment_type":"precautionary_routing_decision","raw_interview_anchor":"That signal issue felt different in character — a live 'failure' warning rather than a short clean blip — and I didn't have any history on that particular fault to lean on, so I wasn't willing to trust backup indication on an unfamiliar problem. Six minutes felt like a cheap price for not gambling on something I hadn't seen before.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"A distinct precautionary phase-3 decision about an unfamiliar junction signal fault, not the target bias."},
        {"segment_id":"seg_007","speaker":"Participant","segment_type":"escalation_decision","raw_interview_anchor":"Once the technician mentioned there was an actual unresolved wiring issue behind it, the flicker stopped feeling like the same closed case from earlier — it felt like there was something real and undiagnosed sitting underneath it, so I wanted a person physically controlling movement rather than relying on the circuit again.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The later pilotman escalation follows new information; hidden validation says this is not another target instance."},
        {"segment_id":"seg_008","speaker":"Participant","segment_type":"counterfactual_reasoning","raw_interview_anchor":"But if I'd made that one extra call and gotten a clean confirmation, I'd have gone into the rest of the shift with something on record rather than just my own read of the log. It wouldn't have changed the facts on the ground, but it might've meant I wasn't relying quite so much on the pattern doing all the work by itself.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"An adopted retrospective hypothetical, not another contemporaneous manifestation."},
        {"segment_id":"seg_009","speaker":"Participant","segment_type":"hindsight_improvement_reflection","raw_interview_anchor":"I'd probably still weigh the history heavily, but I think I'd want some cheap independent check alongside it rather than letting the pattern alone close the question. A quick call doesn't cost that much against holding a train.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"A retrospective desired-practice statement, not a second occurrence."},
        {"segment_id":"seg_010","speaker":"Participant","segment_type":"procedural_resource_rationale","raw_interview_anchor":"Direct line to the technician's diagnostic panel instead of routing through the on-call rota — that delay probably shaped a couple of my later calls too.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"An explanation of how diagnostic access delays affected later calls, not a target manifestation."},
        {"segment_id":"seg_011","speaker":"Participant","segment_type":"colleague_prediction_and_outcome_caution","raw_interview_anchor":"Honestly, most of the desk would've read it the same way I did. That log is well known on our shift. Whether that's the right instinct or not, I couldn't tell you for certain — nothing went wrong that night, but I know that doesn't prove it was the right call either.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"A qualified colleague prediction and explicit caution against inferring correctness from an uneventful outcome; no additional target instance."}
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Focused on reasoning episodes reported by the rail traffic controller for evidence of bias-specific mechanisms; no experimental condition or expected bias count was assumed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["expectation bias", "normalcy bias", "selective information processing"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial track-circuit flicker after possession handback",
      "decision_point_description": "Deciding whether to treat a brief track-circuit occupied indication as a known nuisance trip and give 6M42 the road, or to verify via the foreman, on-call technician, or pilotman working.",
      "affected_reasoning_operation": "Interpretation of an ambiguous track-circuit occupancy signal and decision whether to seek independent verification.",
      "bias_specific_mechanism": "The controller's prior expectation from three similar nuisance trips biased his interpretation of the flicker as the same known fault; this prematurely closed the diagnostic question and suppressed verification of a cheap alternative.",
      "manifestation_in_interview": "The controller describes initially thinking 'here we go again', matching the flicker to the prior nuisance-trip pattern, and then treating it as already accounted for rather than still open.",
      "effect_on_reasoning_or_decision": "He gave 6M42 the road without independent verification. Later, when the technician reported an actual unresolved wiring issue, he changed to pilotman working, showing the initial closed assessment had been less secure than he treated it.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was 'here we go again.' That circuit's had three nuisance trips in the last eight months, all rain or leaf-fall related, all logged. So I looked at it and thought, that's the same signature — short blip, self-clears, no correlation with anything physically on the track. It fit the pattern well enough that I didn't feel I needed to chase it further.",
          "evidence_explanation": "This shows the participant used prior nuisance-trip history to interpret the current ambiguous circuit indication as the same known signature, reducing the felt need for further verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once I had it slotted into that nuisance-trip bucket in my head, verifying it didn't feel like it was really adding anything — I'd already accounted for it, if that makes sense.",
          "evidence_explanation": "This is an explicit report of premature closure: the conclusion was treated as already settled, so verification seemed redundant."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I suppose I treated it as basically closed rather than just 'probably fine but still open.' I gave 6M42 the road.",
          "evidence_explanation": "The participant himself distinguishes between a still-open possibility and the closed judgment he actually used, connecting the biased reasoning to the decision to give the train the road."
        }
      ],
      "correction_or_counterevidence": "Later, the on-call technician reported a known unresolved moisture-sensitivity wiring problem; the participant then suspended normal working and went to pilotman working. The participant also reflected that a cheap independent check at the first flicker would have been better.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor document provides topical support that confirmation/expectation biases occur in operational incidents and can create a false sense of normality; the formal definition of confirmation bias relies on general cognitive-science knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, ... plan continuation ... false sense of normality",
          "mechanism_supported_by_source": "The document identifies confirmation and expectation as common cognitive biases in operational incidents and describes a false sense of normality, supporting the classification of the controller's pattern-based acceptance as a confirmation/expectation mechanism.",
          "relevance_to_this_occurrence": "The participant treated an abnormal track-circuit indication as normal because it matched prior nuisance trips, paralleling the operational false sense of normality described in the source."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "expectation bias",
      "alternative_labels": ["confirmation bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Acceptance of garbled possession follow-up readback",
      "supporting_interview_quote": "I caught 'clear' and something like 'trolley,' but it wasn't a full clean readback.",
      "plausible_mechanism": "The clean formal handback at 23:40 may have created an expectation that the follow-up readback was clear, leading the controller to accept the expected word 'clear' in a garbled transmission as adequate without seeking a clean repeat.",
      "why_not_identified": "The participant's stated reason was primarily procedural: the formal handback was already complete and no rule had been broken. A bias-specific mechanism is plausible but not affirmatively evidenced enough to count as an identified occurrence."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial decision to give 6M42 the road despite track-circuit anomaly",
      "supporting_interview_quote": "Calling the foreman back would've meant holding 6M42 another ten, fifteen minutes for what I was fairly confident was nothing, and pilotman working is even longer than that to arrange.",
      "plausible_mechanism": "The original goal of getting 6M42 through Falcon Bank and keeping 2T19 on time may have created pressure to continue with the planned movement rather than interrupting it for a verification check after an ambiguous signal.",
      "why_not_identified": "The participant's primary stated reason was the prior nuisance-trip pattern rather than plan continuation; delay avoidance was a secondary consideration and may reflect ordinary operational prioritization rather than a distinct bias mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on a retrospective self-report; the participant may rationalize decisions after the fact.",
    "Retrieved corpus passages were topically relevant but some were fragmented, so formal bias definitions partly draw on general cognitive-science knowledge.",
    "The transcript includes only the participant's account, so external validation of perceived signal characteristics or procedural requirements was not available."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Biased_1_Sonnet_on",
  "interview_id": "RT_Biased_1",
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
