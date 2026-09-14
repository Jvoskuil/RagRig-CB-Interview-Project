You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. As explained, this is a confidential debrief to understand the reasoning behind decisions during the cargo transfer alongside the platform last month — not a disciplinary review. Anything you share helps refine our procedures. Are you comfortable proceeding?

Participant: Yes, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by describing your role on that job?

Participant: I was the DPO on watch, running station-keeping in DP2 mode while we did a scheduled cargo transfer — deck cargo and some bulk — to the platform. Normally that's a fairly routine job. We hold position off the leg, crane operator on the platform takes the lifts off our deck, and we just maintain the watch circle until it's done.

Interviewer: And what made this particular job different, if anything?

Participant: Weather was closing in faster than the forecast suggested first thing that morning. We had maybe a four-hour window before significant wave height would push past the platform crane's operating limit. So there was a bit more time pressure than usual, but nothing outside normal parameters when we started.

Interviewer: Take me through what happened, from approach onward.

Participant: On final approach, I noticed a discrepancy between the HPR and one of the DGPS units — about 1.8 meters. DGPS1 and DGPS2 were agreeing closely with each other, and the system had auto-weighted those two into the primary solution, showing green across the board. HPR didn't have any maintenance flag against it, but given the other two were lined up, I read the HPR number as the odd one out and carried on with the approach. We got alongside, started the transfer, cargo went smoothly for the first several lifts. About halfway through — call it 55% of the load transferred — Thruster 3 threw a yellow caution, reduced power availability. Consequence analysis still showed adequate capability, so I kept going in the same configuration. Superintendent called in around then too, just a reminder about the transit schedule afterward. Later, on the second-to-last lift, there was a wind shift that changed the footprint plot recommendation. I was heads-down on the crane boom position at that point, watching the load come across, and I didn't clock the footprint change until the Master mentioned the vessel's attitude had shifted. Checked afterward — the indicator had been sitting there on the secondary screen the whole time. Then for the last lift, OIM asked if we could finish or wanted to stand off. I told him we were maybe eight to ten minutes out, so we pushed on. Partway through that final lift our separation from the leg closed up more than I expected, and we ended up suspending early and backing off to a safer distance. No contact, no loss of position beyond the watch circle, but closer than I'd have liked.

Interviewer: Let's reconstruct that in order. What were you actually monitoring at each stage?

Participant: Early on, reference systems and the DP status page — standard for closing distance. Once we were alongside and lifting, my attention split between the crane display, thruster status, and periodic checks of the environmental trend. As the job went on, honestly, more of my attention shifted toward the crane display than the DP overview, especially in that last third.

Interviewer: Let's go back to the reference discrepancy. Walk me through your decision process there.

Participant: DGPS1 and DGPS2 agreed within normal tolerance, HPR was off by 1.8 meters, no fault logged on it. Two out of three lined up, and once I'd settled on the DGPS pair as the good solution, I didn't see much point going back into the HPR trace since it was just going to keep disagreeing with a picture I'd already accepted. So I proceeded on that basis.

Interviewer: Did you do anything to independently check which reference was actually correct, beyond the system's selection?

Participant: Not really — the pairing agreed and the status was green, so I didn't dig into the raw HPR trace further at that point. In hindsight the offset was a multipath effect from being close to the structure, so HPR wasn't actually wrong, but at the time the two-out-of-three read as good enough.

Interviewer: What would have made you look harder at that discrepancy?

Participant: If the DGPS units had disagreed with each other too, I'd have stopped and manually cross-checked before closing in. It was really the agreement between the two that settled it for me.

Interviewer: Now the thruster caution at the halfway point — what went into staying in the same mode?

Participant: The consequence analysis still showed us within capability, so procedurally there wasn't a hard requirement to change anything. We'd already gotten through a bit more than half the cargo, and the weather window was closing, so stopping to reassess felt like it would cost us more than it bought us at that stage.

Interviewer: Did you consider switching to a more conservative setup — tightening the watch circle, adjusting reference weighting — rather than continuing exactly as before?

Participant: Not actively, no. It wasn't red, so it didn't really register as something requiring a change in how we were running things. We'd been in that configuration all shift and it had been fine.

Interviewer: Move to the final lift and the footprint change. What was pulling your attention at that point?

Participant: The crane boom, almost entirely. That's the highest-consequence thing to watch during an active lift — if the load swings or the boom's position goes wrong, that's an immediate hazard. Checking the footprint plot is normally part of the scan during a lift like that, and the co-operator was on the bridge and could have picked it up, but with only one lift left I figured it was quick enough that it didn't need pulling him off what he was doing to specifically watch environmental trends. The footprint indicator itself is a visual cue only, no audible alarm tied to it, so it's easy for it to sit there unnoticed if you're not specifically glancing over.

Interviewer: What would have changed that — would delegating the environmental watch to your co-operator have helped?

Participant: Probably, yes. We didn't explicitly split that responsibility during the lift. In hindsight that would have been the more robust setup.

Interviewer: Last one — the OIM's question about finishing the final lift. What did you weigh in your answer?

Participant: Mainly the time — eight to ten minutes to complete it, and the equipment status hadn't escalated past caution level. So I told him we were good to finish rather than framing it around how much margin we actually had left, which by that point had narrowed more than I'd tracked.

Interviewer: At that moment, did you actually have the separation and capability numbers available to answer in terms of margin instead of time, or was that information harder to pull together?

Participant: It was there if I'd called it up — separation, remaining thrust reserve, all on the DP overview. But the eight-to-ten-minute figure was just quicker and more concrete to give the OIM, and once I'd framed it that way in my head, finishing felt like the obvious answer. If I'd led with the margin number instead, I think it would have looked like a less comfortable call.

Interviewer: Looking back at that sequence overall, do you think there were earlier indications of how close things got at the end?

Participant: Looking back, yes — the reference offset and the thruster caution together were quietly eating into our margin the whole time, and honestly it feels like it should have been fairly obvious that was building toward something. In the moment, though, neither one individually crossed a threshold that flagged it.

Interviewer: If you were advising a newer DPO going into a similar job, what would you tell them to watch for?

Participant: Don't let a green status or a majority agreement between references close the door on checking the outlier. And separate out who's watching the environmental picture versus the load, especially late in a job when you're tired and task-focused.

Interviewer: Anything you'd do differently if this came up again?

Participant: I'd probably reassess capability actively at the first caution rather than just confirming it was still within limits, and frame those late-stage go/no-go calls around remaining margin rather than remaining minutes. Otherwise the job itself was manageable — we just let a few small things ride longer than we should have.

Interviewer: That's really helpful detail. Thank you for walking through it so thoroughly.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MO_Biased_7",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Dynamic Positioning Operator (Offshore Support Vessel)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Reference Drift During Cargo Transfer at North Sea Platform",
    "scenario_summary_internal": "A DPO aboard a DP2-class offshore support vessel is conducting a scheduled cargo transfer alongside a fixed platform under a closing weather window. A reference-system discrepancy appears early in the approach, is resolved in a way that favors the DPO's initial mental model, and is never fully re-examined. As the transfer proceeds, a thruster caution and worsening wind trend compete with schedule pressure and sunk time already invested in the operation. A crane-boom fixation causes a late wind-shift cue to be under-weighted. Near the end of the job, the decision to finish the last lift versus suspend operations is framed around minutes remaining rather than proximity risk, and the vessel experiences a controlled but uncomfortably close approach toward the platform before operations are suspended. No collision or DP loss of position beyond safe limits occurs, so the incident is a near-miss learning event rather than a casualty, keeping outcome information ambiguous as evidence of bias.",
    "occupational_realism": {
      "objective": "Complete a scheduled cargo transfer of deck cargo and bulk material from the OSV to a fixed offshore platform under DP2 station-keeping, within a forecast weather window, without breaching safe approach distance or DP capability limits.",
      "setting": "North Sea fixed platform, DP2-class offshore support vessel on standby/cargo-transfer duty, daylight, forecast deteriorating sea state (rising from 2.5m to 3.5m Hs) over a 4-hour window, cargo crane operations alongside the platform leg.",
      "constraints": [
        "Closing weather window before conditions exceed platform crane operating limits",
        "Limited remaining vessel time on charter before transit to next location",
        "DP2 redundancy requirement (loss of one reference system must not compromise position-keeping)",
        "Crew fatigue from an extended shift",
        "Communication lag between crane operator, platform OIM, and bridge team"
      ],
      "stakeholders": [
        "Dynamic Positioning Operator (interviewee)",
        "Master / DP2 co-operator",
        "Platform Installation Manager (OIM)",
        "Crane operator",
        "Vessel superintendent (shore-based, schedule pressure)"
      ],
      "technical_terms_to_use": [
        "DP2 redundancy concept",
        "reference system (DGPS, HPR, laser/Fanbeam)",
        "footprint plot",
        "consequence analysis",
        "thruster caution alarm",
        "green/yellow/red DP status",
        "safe working envelope",
        "watch circle",
        "weather window"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "automation bias",
        "inattentional blindness",
        "hindsight bias",
        "sunk cost",
        "status quo bias",
        "framing effect",
        "any explicit bias or heuristic terminology"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "DGPS1 and HPR show a 1.8m position discrepancy during final approach",
          "DGPS2 agrees closely with DGPS1",
          "DP system auto-selected DGPS1/DGPS2 as the weighted reference pair, showing overall GREEN status",
          "No maintenance flag currently logged against HPR"
        ],
        "new_information_after_decision": [
          "HPR later shown to have a valid multipath-related offset consistent with proximity to the platform structure",
          "The discrepancy trend continues but stays within the DP2 alert threshold at this stage"
        ],
        "alternatives": [
          "Accept the DP system's auto-weighted reference pair and proceed with approach",
          "Manually down-weight or flag HPR pending a deeper cross-check before closing distance"
        ],
        "intended_action": "DPO accepts the two agreeing GPS references as sufficient confirmation, treats the HPR reading as the outlier without further independent cross-check, and proceeds with the approach relying on the system's GREEN status."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Approximately 55% of cargo has been transferred; two lifts remain",
          "Thruster 3 shows a yellow caution for reduced power availability",
          "DP consequence analysis still shows adequate capability with the caution active",
          "Weather forecast confirms Hs will exceed platform crane limits within roughly 70 minutes"
        ],
        "new_information_after_decision": [
          "Thruster 3 caution persists at a stable but unresolved severity through the remaining transfer",
          "The vessel superintendent radios a reminder about the tight onward transit schedule"
        ],
        "alternatives": [
          "Suspend the transfer, move to a safe standby distance, and reassess DP capability before continuing",
          "Switch to a more conservative operating mode (e.g., reduce reference reliance, tighten watch circle) while continuing at reduced pace",
          "Continue the transfer at the current pace and mode on the basis that DP2 capability is still nominally sufficient"
        ],
        "intended_action": "DPO continues cargo transfer in the existing DP Auto configuration at the existing pace, citing the completed portion of the job and the closing weather window, without adjusting mode or reassessing the operating plan in light of the new caution."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "DPO's attention is concentrated on the crane boom position display during the final lift",
          "A new wind-shift alert changes the vessel's heading/footprint recommendation on the DP plot",
          "The environmental sensor trend line has shifted for roughly 90 seconds prior to the lift's completion",
          "No audible alarm accompanies the footprint plot change, only a visual indicator"
        ],
        "new_information_after_decision": [
          "The wind shift is confirmed moments later by the Master, who notices the vessel's heel/attitude change",
          "The footprint plot indicator had been visually available the entire time on a secondary screen"
        ],
        "alternatives": [
          "Periodically scan the DP footprint and environmental displays independently of crane progress",
          "Delegate footprint/environmental monitoring explicitly to the co-operator during the final lift",
          "Remain focused primarily on the crane boom display until the lift is landed"
        ],
        "intended_action": "DPO remains focused on the crane boom display through the final lift and does not register the footprint plot change until prompted by the Master, despite the indicator being visible on a secondary screen."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "One final, smaller lift remains, estimated at 8-10 minutes",
          "Wind and swell have increased since Phase 3, narrowing the safe working envelope",
          "Thruster 3 caution and the earlier reference discrepancy are both still present but not escalated to red/alarm status",
          "OIM asks whether the vessel can finish the last lift or should stand off"
        ],
        "new_information_after_decision": [
          "The vessel's separation from the platform decreases more than expected during the final maneuvering, prompting an early suspension of the lift",
          "Post-event review shows the combination of reduced thruster margin and reference offset had been narrowing the safe envelope for some time"
        ],
        "alternatives": [
          "Suspend the final lift now and move to standby distance given the narrowing envelope",
          "Complete the final lift on the basis that only a few minutes remain and equipment is still within nominal status"
        ],
        "intended_action": "DPO frames the decision to the OIM around the short remaining time needed to finish ('just a few more minutes') rather than around the shrinking safety margin, and elects to proceed with the final lift before conditions force an early suspension."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role and responsibilities during this cargo transfer operation.",
        "Walk me through what a routine transfer alongside this platform normally looks like."
      ],
      "timeline_reconstruction": [
        "Take me through the operation from approach to the final lift, in the order things happened.",
        "What were you monitoring at each stage, and how did that change as the job progressed?"
      ],
      "decision_point_probes": [
        "At the point where the reference systems disagreed, what information did you use to decide which was correct?",
        "What made you comfortable continuing the transfer once the thruster caution appeared?",
        "What were you focused on during the final lift, and how did you become aware of the wind shift?",
        "When the OIM asked about finishing the last lift, what factors did you weigh in your answer?",
        "What alternatives did you consider at each of these points, and why did you rule them out?"
      ],
      "closing_hypotheticals": [
        "If the HPR discrepancy had appeared without the GPS agreement, would your approach have differed?",
        "Looking back, do you think there were earlier indications of the eventual close approach to the platform?",
        "If you were advising a newer DPO facing a similar sequence, what would you tell them to watch for?",
        "What, if anything, would you do differently if this situation arose again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 1,
        "mechanism": "DPO treats agreement between DGPS1 and DGPS2 as sufficient confirmation of position accuracy and interprets the conflicting HPR reading as the erroneous outlier without seeking disconfirming or independent cross-check evidence",
        "affected_reasoning_operation": "evidence-selection and evidence-weighting during reference validation",
        "evidence_available_at_time": [
          "1.8m discrepancy between HPR and the DGPS pair",
          "No prior maintenance flag on HPR",
          "DP system GREEN status based on auto-selected weighting"
        ],
        "required_textual_manifestation": "DPO explains the decision by citing only the two agreeing sources and dismissing HPR without describing any independent verification step",
        "plausible_nonbias_interpretation": "Two-out-of-three agreement is a legitimate operational heuristic under time pressure, so the choice could reflect ordinary reliance on majority-reference logic rather than biased evidence selection",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "cherry-picking", "selective evidence"]
      },
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "decision_point": 1,
        "mechanism": "DPO defers to the DP system's automatically weighted reference selection and overall GREEN status as sufficient justification to proceed, without independently interpreting the raw discrepancy data",
        "affected_reasoning_operation": "trust calibration between automated system output and independent manual judgment",
        "evidence_available_at_time": [
          "DP system auto-weighting output showing GREEN",
          "Raw discrepancy data visible on the reference system page",
          "DPO's own training on manual reference validation"
        ],
        "required_textual_manifestation": "DPO's stated justification centers on the system's status indicator itself rather than an independent manual assessment of the raw data",
        "plausible_nonbias_interpretation": "Trusting a certified DP system's automated consequence analysis is standard practice and consistent with the vessel's approved operating procedures",
        "strength": "subtle",
        "do_not_make_explicit": ["automation bias", "over-reliance on automation"]
      },
      {
        "instance_id": "hb_01",
        "bias": "Hindsight Bias",
        "decision_point": 1,
        "mechanism": "When asked retrospectively about early warning signs, DPO overstates how foreseeable the reference discrepancy's significance was at the time, framing it as something that 'should have been obvious' despite it appearing marginal and within tolerance in the moment",
        "affected_reasoning_operation": "retrospective probability/foreseeability judgment during closing reflection on the Phase 1 decision",
        "evidence_available_at_time": [
          "Contemporaneous discrepancy was within the DP2 alert threshold, not flagged as abnormal at the time",
          "Later review confirmed the discrepancy was linked to platform-proximity multipath, learned only after the event"
        ],
        "required_textual_manifestation": "In response to a closing hypothetical, DPO states the discrepancy pattern was clearly indicative of trouble, in stronger terms than the contemporaneous alert status supports",
        "plausible_nonbias_interpretation": "An experienced operator may legitimately recognize a pattern in hindsight that genuinely was subtly present, without this reflecting distorted memory of foreseeability",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "creeping determinism", "knew-it-all-along"]
      },
      {
        "instance_id": "sc_01",
        "bias": "Sunk cost bias",
        "decision_point": 2,
        "mechanism": "DPO's justification for continuing the transfer emphasizes the proportion of cargo already transferred and time already invested, rather than a forward-looking reassessment of current DP capability and risk given the new thruster caution",
        "affected_reasoning_operation": "cost-weighting in the continue-versus-suspend decision",
        "evidence_available_at_time": [
          "~55% of cargo already transferred",
          "Thruster 3 yellow caution newly active",
          "Consequence analysis still nominally adequate"
        ],
        "required_textual_manifestation": "DPO explicitly references the completed portion of work or elapsed effort as a reason to continue, alongside or instead of a fresh capability assessment",
        "plausible_nonbias_interpretation": "Completing a partially finished lift sequence can be operationally preferable to a partial suspend-and-resume cycle, independent of any sunk-cost reasoning",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment"]
      },
      {
        "instance_id": "sq_01",
        "bias": "Status Quo Bias",
        "decision_point": 2,
        "mechanism": "DPO retains the existing DP Auto configuration and pace after the thruster caution rather than actively considering a more conservative mode change, treating the current setup as the default that need not be revisited absent a red alarm",
        "affected_reasoning_operation": "option-generation and default-preservation when a new caution condition arises",
        "evidence_available_at_time": [
          "Thruster 3 caution active but not escalated to red",
          "Available mode/pace adjustment options were procedurally accessible",
          "No requirement mandated staying in the current configuration"
        ],
        "required_textual_manifestation": "DPO's account shows no active comparison of mode-change alternatives; the current configuration is preserved by default rather than by a stated reason to prefer it",
        "plausible_nonbias_interpretation": "Maintaining a stable, previously validated configuration during an active lift can be a deliberate stability-preserving choice rather than a default bias",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "default preservation", "inertia"]
      },
      {
        "instance_id": "sa_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 3,
        "mechanism": "DPO's sustained visual and cognitive focus on the crane boom display during the final lift causes a visually-available footprint plot change (wind-shift indicator) to go unnoticed until an external party points it out",
        "affected_reasoning_operation": "perceptual monitoring and attentional allocation across competing displays",
        "evidence_available_at_time": [
          "Footprint plot indicator change visible on secondary screen for ~90 seconds",
          "No audible alarm accompanying the visual change",
          "Crane boom display requiring continuous visual tracking during the lift"
        ],
        "required_textual_manifestation": "DPO states or implies they did not register the footprint change until the Master mentioned it, despite the indicator having been visible the whole time",
        "plausible_nonbias_interpretation": "Reasonable task prioritization during an active lift can justify concentrated attention on the crane display as the higher-priority task in that moment",
        "strength": "moderate",
        "do_not_make_explicit": ["inattentional blindness", "selective attention", "tunnel vision"]
      },
      {
        "instance_id": "fb_01",
        "bias": "Framing Bias",
        "decision_point": 4,
        "mechanism": "The decision to proceed with the final lift is verbally and cognitively framed by the DPO around the small amount of time remaining ('just a few more minutes') rather than around the narrowing safety envelope, shaping the choice toward continuation",
        "affected_reasoning_operation": "decision framing in the continue-versus-suspend judgment communicated to the OIM",
        "evidence_available_at_time": [
          "Estimated 8-10 minutes to complete final lift",
          "Narrowing safe working envelope from combined thruster and reference conditions",
          "OIM's direct question inviting either frame of response"
        ],
        "required_textual_manifestation": "DPO's stated rationale to the OIM foregrounds remaining time/completion rather than the margin/risk trend, even though both pieces of information were available",
        "plausible_nonbias_interpretation": "Time-to-completion is a legitimate operational factor in a suspend/continue decision and can reasonably be mentioned without indicating biased framing",
        "strength": "subtle",
        "do_not_make_explicit": ["framing bias", "gain framing", "loss framing"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for this biased-condition scenario; no paired control is specified in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable - no counterfactual condition requested",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points, each with at least two plausible alternatives",
      "Confirm exactly 7 planned bias instances, one per manifest entry",
      "Confirm no bias terminology, labels, or explanations appear in the public interview text",
      "Confirm each instance has a distinct evidence trace and decision point per the internal embedding plan",
      "Confirm final word count falls between 1,215 and 1,485 words",
      "Confirm consequences described (near-approach, suspension) do not mechanically prove any decision was biased",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as reliance on agreeing DGPS pair to dismiss conflicting HPR reading without independent cross-check"},
      {"bias": "Automation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as deference to DP system's auto-weighted GREEN status over independent manual interpretation of raw discrepancy data"},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "occurrences": 1, "mechanism_constraint": "Must manifest as failure to notice a visually-available footprint/environmental cue due to sustained focus on the crane display"},
      {"bias": "Hindsight Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as retrospective overstatement of foreseeability of the Phase 1 reference discrepancy during closing reflection"},
      {"bias": "Sunk cost bias", "occurrences": 1, "mechanism_constraint": "Must manifest as justification for continuing based on cargo/time already invested rather than forward-looking capability reassessment"},
      {"bias": "Status Quo Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as default preservation of current DP mode/pace without active comparison of mode-change alternatives"},
      {"bias": "Framing Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as decision rationale framed around remaining time rather than narrowing safety margin"}
    ],
    "target_bias_names": [
      "Confirmation Bias",
      "Automation Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Hindsight Bias",
      "Sunk cost bias",
      "Status Quo Bias",
      "Framing Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Confirmation Bias", "requested_occurrences": 1},
      {"bias": "Automation Bias", "requested_occurrences": 1},
      {"bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1},
      {"bias": "Hindsight Bias", "requested_occurrences": 1},
      {"bias": "Sunk cost bias", "requested_occurrences": 1},
      {"bias": "Status Quo Bias", "requested_occurrences": 1},
      {"bias": "Framing Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias"},
      {"instance_id": "ab_01", "bias": "Automation Bias"},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness"},
      {"instance_id": "hb_01", "bias": "Hindsight Bias"},
      {"instance_id": "sc_01", "bias": "Sunk cost bias"},
      {"instance_id": "sq_01", "bias": "Status Quo Bias"},
      {"instance_id": "fb_01", "bias": "Framing Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1},
      {"instance_id": "ab_01", "bias": "Automation Bias", "decision_point": 1},
      {"instance_id": "hb_01", "bias": "Hindsight Bias", "decision_point": 1},
      {"instance_id": "sc_01", "bias": "Sunk cost bias", "decision_point": 2},
      {"instance_id": "sq_01", "bias": "Status Quo Bias", "decision_point": 2},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 3},
      {"instance_id": "fb_01", "bias": "Framing Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective reliance on the two agreeing GPS references to confirm the preferred position estimate, dismissing the conflicting HPR reading as the outlier without independent verification",
        "affected_reasoning_operation": "evidence-selection and weighting during reference validation",
        "evidence_source": "Reference system comparison data (DGPS1, DGPS2, HPR) at Phase 1",
        "distinctiveness_requirement": "Must be distinguished from ab_01 by focusing on the DPO's own evidence-selection reasoning rather than on deference to the automated system status indicator"
      },
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "mechanism": "Deference to the DP system's automated reference-weighting and GREEN status as sufficient justification, bypassing independent manual interpretation of the underlying raw data",
        "affected_reasoning_operation": "trust calibration between automated output and manual judgment",
        "evidence_source": "DP system status indicator and auto-weighting output at Phase 1",
        "distinctiveness_requirement": "Must be distinguished from cb_01 by centering on trust in the system's output itself, not on the DPO's own selective interpretation of raw discrepancy data"
      },
      {
        "instance_id": "hb_01",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospective overstatement, during closing reflection, of how foreseeable the Phase 1 discrepancy's significance was, exceeding what the contemporaneous alert status supported",
        "affected_reasoning_operation": "retrospective foreseeability judgment elicited by closing hypothetical probe",
        "evidence_source": "DPO's closing-probe response compared against the contemporaneous Phase 1 alert status",
        "distinctiveness_requirement": "Must occur only in the closing reflective probe tied to the Phase 1 event, not as a repeated commentary elsewhere in the interview"
      },
      {
        "instance_id": "sc_01",
        "bias": "Sunk cost bias",
        "mechanism": "Justification for continuing the transfer that foregrounds cargo and time already invested rather than a forward-looking reassessment of DP capability given the new thruster caution",
        "affected_reasoning_operation": "cost-weighting in the continue-versus-suspend judgment",
        "evidence_source": "Phase 2 cargo-completion status and elapsed operation time",
        "distinctiveness_requirement": "Must be distinguished from sq_01 by explicit reference to invested cost/effort as the stated reason, rather than default preservation of the operating mode without any stated cost rationale"
      },
      {
        "instance_id": "sq_01",
        "bias": "Status Quo Bias",
        "mechanism": "Retention of the existing DP Auto configuration and operating pace after the thruster caution, without active comparison of a more conservative mode as an alternative",
        "affected_reasoning_operation": "option-generation and default-preservation when a new caution condition arises",
        "evidence_source": "Phase 2 mode/configuration status and absence of considered alternatives in DPO's account",
        "distinctiveness_requirement": "Must be distinguished from sc_01 by the absence of an invested-cost rationale; the defining feature is default retention of configuration, not a cost-based justification"
      },
      {
        "instance_id": "sa_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Sustained attentional focus on the crane boom display causes a visually-available footprint/wind-shift indicator change to go unnoticed until pointed out externally",
        "affected_reasoning_operation": "perceptual monitoring and attentional allocation across competing displays",
        "evidence_source": "Phase 3 footprint plot indicator timeline versus DPO's attention account",
        "distinctiveness_requirement": "Unique to Phase 3; concerns failure to perceive available information, not failure to act on already-perceived information"
      },
      {
        "instance_id": "fb_01",
        "bias": "Framing Bias",
        "mechanism": "The continue/suspend rationale communicated to the OIM is framed around remaining completion time rather than the narrowing safety margin, despite both being available",
        "affected_reasoning_operation": "decision framing in the final continue-versus-suspend response to a direct query",
        "evidence_source": "Phase 4 DPO response to the OIM's query, compared against available margin data",
        "distinctiveness_requirement": "Unique to Phase 4; concerns how the decision is framed/communicated, not the underlying cost or default-preservation reasoning captured by sc_01/sq_01"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle"},
      {"instance_id": "ab_01", "bias": "Automation Bias", "strength": "subtle"},
      {"instance_id": "hb_01", "bias": "Hindsight Bias", "strength": "subtle"},
      {"instance_id": "sc_01", "bias": "Sunk cost bias", "strength": "subtle"},
      {"instance_id": "sq_01", "bias": "Status Quo Bias", "strength": "subtle"},
      {"instance_id": "sa_01", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate"},
      {"instance_id": "fb_01", "bias": "Framing Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "N/A",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MO_Biased_7",
    "domain_id": "MO",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across distinct decision points by mechanism fit and narrative realism: Phase 1 (reference discrepancy) hosts confirmation bias, automation bias, and hindsight bias as three distinct reasoning operations (evidence-selection, automation trust, retrospective foreseeability); Phase 2 (continue transfer under thruster caution) hosts sunk cost and status quo as distinct rationale types (cost-based vs. default-based); Phase 3 (final lift) hosts selective attention/inattentional blindness as the sole attentional-mechanism fit; Phase 4 (final continue/suspend decision) hosts framing bias as the sole communication-framing fit. No bias exceeds two occurrences at a single decision point, and no two co-located instances share an evidence source or reasoning operation.",
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
          "segment_type": "reference-validation decision",
          "raw_interview_anchor": "\"Two out of three lined up... I didn't see much point going back into the HPR trace\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01",
            "ab_01"
          ],
          "ground_truth_rationale": "The participant selects the agreeing DGPS pair, dismisses the conflicting HPR reading without independent checking, and cites green/auto-weighted system status."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "continue-versus-reassess decision",
          "raw_interview_anchor": "\"We'd already gotten through a bit more than half the cargo... stopping to reassess felt like it would cost us more\" / \"It wasn't red... We'd been in that configuration all shift\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sc_01",
            "sq_01"
          ],
          "ground_truth_rationale": "Continuation is justified with completed cargo and closing time, while no conservative mode alternative is actively compared."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "attention and monitoring allocation",
          "raw_interview_anchor": "\"The crane boom, almost entirely... I didn't clock the footprint change until the Master mentioned\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sa_01"
          ],
          "ground_truth_rationale": "Sustained crane-display focus leaves a visible environmental cue unnoticed; delegation was not explicitly assigned."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "final-lift communication and go/no-go decision",
          "raw_interview_anchor": "\"Mainly the time — eight to ten minutes... rather than framing it around how much margin\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "fb_01"
          ],
          "ground_truth_rationale": "The response to the OIM foregrounds remaining minutes over the narrowing margin despite available margin data."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "retrospective foreseeability judgment",
          "raw_interview_anchor": "\"Looking back... it feels like it should have been fairly obvious\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "hb_01"
          ],
          "ground_truth_rationale": "After the close approach, the participant says the buildup should have been obvious while acknowledging no individual threshold was crossed."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "initial operational appraisal",
          "raw_interview_anchor": "\"There was a bit more time pressure than usual, but nothing outside normal parameters\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is an operational appraisal of conditions without a hidden bias manifestation."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "monitoring-plan description",
          "raw_interview_anchor": "\"My attention split between the crane display, thruster status, and periodic checks... more ... toward the crane display\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A general description of monitoring allocation before the final-lift miss; it does not itself express one of the hidden instances."
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
    "analysis_scope_note": "Single confidential debrief transcript analyzed for bias-specific reasoning mechanisms. No retrieved scientific-paper corpus passages were supplied in this session; labels rely on general cognitive-science/human-factors knowledge rather than retrieved corpus evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Attentional tunneling",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Hindsight bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Confirmatory search", "Myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's prior beliefs or decisions while underweighting or avoiding disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final-approach reference-system discrepancy resolution",
      "decision_point_description": "Whether to treat the DGPS pair as the trustworthy reference and continue the approach without further investigating the HPR outlier.",
      "affected_reasoning_operation": "Evidence evaluation and reference-system selection",
      "bias_specific_mechanism": "The participant formed an early interpretation that the agreeing DGPS pair was the good solution. He then avoided re-examining the HPR trace because it would conflict with the accepted picture, thereby treating the outlier as wrong rather than checking which reference was actually degraded.",
      "manifestation_in_interview": "The participant described reading the HPR as the odd one out, accepting the DGPS pair, and then not seeing much point in going back into the HPR trace because it would keep disagreeing with the solution he had already accepted.",
      "effect_on_reasoning_or_decision": "The unverified majority reference was accepted, reducing the chance of detecting that HPR may have been valid and that the DGPS pair could have been affected by multipath. The participant proceeded with the approach on that basis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "DGPS1 and DGPS2 were agreeing closely with each other, and the system had auto-weighted those two into the primary solution, showing green across the board. HPR didn't have any maintenance flag against it, but given the other two were lined up, I read the HPR number as the odd one out and carried on with the approach.",
          "evidence_explanation": "This shows the early acceptance of the DGPS pairing as the good reference because it formed a confirming majority."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Two out of three lined up, and once I'd settled on the DGPS pair as the good solution, I didn't see much point going back into the HPR trace since it was just going to keep disagreeing with a picture I'd already accepted.",
          "evidence_explanation": "This is a explicit statement of avoiding information that could disconfirm the accepted solution, which is the core mechanism of confirmation bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really — the pairing agreed and the status was green, so I didn't dig into the raw HPR trace further at that point.",
          "evidence_explanation": "The participant confirms he did not independently test the initial interpretation, relying instead on the solution that was already consistent with his conclusion."
        }
      ],
      "correction_or_counterevidence": "A two-out-of-three voting heuristic and a green system status can be reasonable operational bases in the moment, and no HPR maintenance flag was logged. The bias lies less in using the majority than in avoiding a check that might have disconfirmed the accepted solution.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this session; the label and mechanism are assigned from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Plan continuation bias",
      "alternative_labels": ["Get-there-itis", "Plan continuation error"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to continue an original plan or course of action even when cues suggest that conditions have changed or that reassessment may be warranted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Mid-transfer response to Thruster 3 yellow caution",
      "decision_point_description": "Whether to continue in the same DP configuration after a thruster caution versus actively reassessing or shifting to a more conservative setup.",
      "affected_reasoning_operation": "Risk assessment and operational go/continue decision",
      "bias_specific_mechanism": "The original plan and current configuration served as the reference point. The participant did not actively consider a more conservative setup because the caution had not escalated to red and the configuration had been fine all shift. Progress and the closing weather window made reassessment feel more costly than continuing.",
      "manifestation_in_interview": "The participant reported that after the yellow caution he kept the same configuration, did not actively consider changing it, and rationalized continuation partly by the amount of cargo already transferred and the shrinking weather window.",
      "effect_on_reasoning_or_decision": "The caution did not trigger a deliberate re-evaluation of configuration or watch circle, which may have allowed small degradations to continue accumulating without active review.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Thruster 3 threw a yellow caution, reduced power availability. Consequence analysis still showed adequate capability, so I kept going in the same configuration.",
          "evidence_explanation": "The participant continued the existing plan after a changed system-status cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd already gotten through a bit more than half the cargo, and the weather window was closing, so stopping to reassess felt like it would cost us more than it bought us at that stage.",
          "evidence_explanation": "This shows plan-continuation pressure from progress and time pressure rather than a decision driven primarily by an active re-evaluation of remaining margin."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not actively, no. It wasn't red, so it didn't really register as something requiring a change in how we were running things. We'd been in that configuration all shift and it had been fine.",
          "evidence_explanation": "The participant treats the absence of a red alarm and prior uninterrupted performance as sufficient reason not to consider a more conservative alternative."
        }
      ],
      "correction_or_counterevidence": "Counterevidence is substantial: consequence analysis showed adequate capability, no hard procedural requirement existed, and operational time pressure was real. These factors could make the same decision defensible without invoking bias, so this occurrence is reported at low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this session; the label and mechanism are assigned from general cognitive-science/human-factors knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Attentional tunneling",
      "alternative_labels": ["Cognitive tunneling", "Inattentional narrowing"],
      "taxonomy_status": "established_label",
      "bias_definition": "Narrowing of attention onto a salient task or display at the expense of detecting other relevant, potentially critical information in the environment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Second-to-last lift footprint recommendation change",
      "decision_point_description": "Monitoring allocation during an active crane lift after a wind shift changed the footprint plot recommendation.",
      "affected_reasoning_operation": "Attention allocation and environmental monitoring",
      "bias_specific_mechanism": "Attentional resources were concentrated almost entirely on the crane boom as the highest-consequence element of the active lift. The footprint indicator, a visual-only cue on the secondary screen, was not sampled and no explicit delegation of environmental scanning to the co-operator was made.",
      "manifestation_in_interview": "The participant stated his attention was on the crane boom almost entirely, did not notice the footprint change until the Master mentioned the vessel's attitude shift, and found afterward that the indicator had been sitting on the secondary screen the whole time.",
      "effect_on_reasoning_or_decision": "The changed footprint recommendation was missed during a safety-critical lift, contributing to an unexpected attitude shift and later closer-than-expected separation from the leg.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The crane boom, almost entirely.",
          "evidence_explanation": "This directly states the extreme narrowing of attention during the lift."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't clock the footprint change until the Master mentioned the vessel's attitude had shifted. Checked afterward — the indicator had been sitting there on the secondary screen the whole time.",
          "evidence_explanation": "This confirms that a relevant environmental indicator was available but not sampled due to the narrowed attention."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The footprint indicator itself is a visual cue only, no audible alarm tied to it, so it's easy for it to sit there unnoticed if you're not specifically glancing over.",
          "evidence_explanation": "The participant identifies a display-design factor that made the narrowed attention consequential, but the cognitive mechanism remains attentional tunneling rather than alarm absence alone."
        }
      ],
      "correction_or_counterevidence": "There are contributing non-bias factors: the footprint indicator had no audible alarm, and attending to the crane boom is a safety-critical task during an active lift. However, the participant's own account shows that a normally relevant scan item was omitted because attention was absorbed elsewhere.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this session; the label and mechanism are assigned from general cognitive-science/human-factors knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Framing effect",
      "alternative_labels": ["Narrow framing", "Attribute framing"],
      "taxonomy_status": "established_label",
      "bias_definition": "A change in judgment or decision when the same information is represented or emphasized in different ways; here, framing the decision around time remaining rather than remaining safety margin led to a more favorable go decision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final-lift go/no-go response to OIM",
      "decision_point_description": "Whether to finish the final lift or stand off when the OIM asked for the participant's call.",
      "affected_reasoning_operation": "Risk judgment and communication of a go/no-go recommendation",
      "bias_specific_mechanism": "The participant internally represented the decision in terms of a concrete time-to-complete figure rather than remaining safety margin. Once the decision was framed around time remaining, finishing felt like the obvious answer, and the margin frame appeared less comfortable.",
      "manifestation_in_interview": "The participant said he told the OIM they were good to finish based on eight to ten minutes remaining, and he explicitly contrasted that with how the call would have looked if he had framed it around remaining margin.",
      "effect_on_reasoning_or_decision": "The participant recommended finishing without fully tracking or weighing the narrowed margin. Partway through the final lift, separation closed up more than expected and the operation was suspended early.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mainly the time — eight to ten minutes to complete it, and the equipment status hadn't escalated past caution level. So I told him we were good to finish rather than framing it around how much margin we actually had left, which by that point had narrowed more than I'd tracked.",
          "evidence_explanation": "This states that the go/no-go answer was organized around time remaining instead of available safety margin."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But the eight-to-ten-minute figure was just quicker and more concrete to give the OIM, and once I'd framed it that way in my head, finishing felt like the obvious answer. If I'd led with the margin number instead, I think it would have looked like a less comfortable call.",
          "evidence_explanation": "The participant directly links the chosen frame to the decision feeling obvious, indicating that the representation of the decision influenced the judgment."
        }
      ],
      "correction_or_counterevidence": "Time remaining and equipment status were relevant operational inputs, and the system had not escalated beyond caution level. The framing effect inference is based on the participant's own contrast between the time frame and the margin frame rather than on external manipulation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this session; the label and mechanism are assigned from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Hindsight bias",
      "alternative_labels": ["Knew-it-all-along effect", "Retrospective predictability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive past events as having been more predictable or obvious after the outcome is known than they were at the time.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Retrospective debrief assessment of warning signs after near-miss",
      "decision_point_description": null,
      "affected_reasoning_operation": "Retrospective predictability judgment",
      "bias_specific_mechanism": "After knowing the near-miss outcome, the participant judged that the accumulating reference offset and thruster caution should have been fairly obvious. This overestimates the foreseeability of the degraded margin relative to the in-the-moment cues, which he also acknowledged did not individually cross a threshold.",
      "manifestation_in_interview": "The participant said that looking back the signs were quietly eating into the margin and that it should have been fairly obvious, while noting that in the moment neither one individually crossed a threshold that flagged it.",
      "effect_on_reasoning_or_decision": "The retrospective judgment may distort how predictable the event was and could influence debrief conclusions, procedural recommendations, and assessments of the participant's earlier decisions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, yes — the reference offset and the thruster caution together were quietly eating into our margin the whole time, and honestly it feels like it should have been fairly obvious that was building toward something. In the moment, though, neither one individually crossed a threshold that flagged it.",
          "evidence_explanation": "The phrase 'should have been fairly obvious' is a classic hindsight marker when paired with the later-known outcome. The participant simultaneously acknowledges real-time ambiguity, which is why this is rated moderate rather than high."
        }
      ],
      "correction_or_counterevidence": "The participant immediately qualifies the retrospective claim by noting that neither cue individually crossed a threshold in real time, showing partial awareness of the limited foreseeability at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this session; the label and mechanism are assigned from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper corpus was supplied for this analysis, so bias labels and mechanisms rely on general cognitive-science/human-factors knowledge rather than retrieved corpus evidence.",
    "The analysis is based on a single self-reported debrief narrative without independent objective data, benchmark conditions, or real-time sensor records.",
    "Some occurrences, especially plan continuation bias, have strong competing non-bias explanations such as valid procedural thresholds, time pressure, and adequate consequence analysis.",
    "The framing effect and hindsight bias findings are based on retrospective self-report and may not capture the exact in-the-moment cognitive processes.",
    "The analysis is conservative but cannot establish causal effects on operational outcomes from the interview alone."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Biased_7_Sonar_off",
  "interview_id": "MO_Biased_7",
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
