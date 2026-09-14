You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the turbocharger incident from your last contract, and that this is just for internal review purposes—nothing punitive.

Participant: Sure, no problem. Happy to go through it.

Interviewer: Can you set the scene for me—what vessel, what voyage, and what was your role at the time?

Participant: I was Chief Engineer on a geared bulk carrier, mid-size, about 55,000 deadweight. We were on a laden leg, roughly 30 hours out from the discharge port. My job was running the engine room day to day—main engine, auxiliaries, all the monitoring. We'd just come off a turbocharger overhaul on the main engine, done about three weeks prior at a yard stop. It wasn't cheap, and the office had been asking for updates on it, so it was very much front of mind.

Interviewer: Take me through what happened, from the first sign of trouble to how it eventually got resolved.

Participant: About two days into that leg, I noticed the exhaust gas temperature on one unit was running a touch high, and there was a bit more vibration on the turbocharger casing than I'd expect. Nothing alarming—still inside the normal band, no alarm triggered. Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul. I kept an eye on it rather than pulling back on load, because we had a tide-restricted berth waiting for us and reducing speed then would have put that window at risk. The readings actually settled down over the next few hours, so at the time it felt like the right call.

A day or so later, the monitoring system was showing everything back in the green—temperatures, scavenge air pressure, all nominal. I didn't have my second engineer pull a lube oil sample at that point. The system was telling me it was fine, and honestly that's what it's there for. We left it at that and planned to look at it properly at the next scheduled maintenance.

Then, maybe twelve hours before that, my second engineer had flagged during rounds that the fuel filter differential pressure had crept up a bit. I was pretty focused on the turbocharger numbers at that point given the earlier concern, so I told him to keep an eye on it and we'd deal with it later—there was no fuel consumption issue or anything on the combustion side, so it didn't feel urgent next to what I was already watching.

The real event came about ten hours before the tide window closed. We got a sudden exhaust temperature spike and a distinct knock-type vibration—clearly the bearing itself now, not just bedding in. At that point we were deep into it. We jury-rigged a fix, brought the load down, and pushed on to make berth rather than diverting.

Interviewer: Let's slow down and reconstruct that in order. What did you observe first, and how did things develop from there?

Participant: First was the mild vibration and temperature deviation, day two of the leg. Then it settled, then the system showed clean readings for a good stretch. The filter differential pressure note came in maybe a day and a half after that. Then the temperature spike and vibration event came about ten hours before we were due at the tide window. So there was a real gap—almost three days—between the first hint and the actual failure.

Interviewer: Going back to that first deviation—what information did you actually have, and what did you weigh?

Participant: I had the raw numbers, both inside the normal band, and I had the fact that this unit had just been fully overhauled. Those two things pulled in different directions a bit—on one hand you could say any deviation after a rebuild deserves a look, but on the other, we'd just paid to have that bearing and the running gear replaced, so a bearing problem three weeks later seemed like a stretch. I remember thinking it made more sense as running-in than as an actual fault. The alternative was to ease off and inspect right there, but with the tide window ahead, and given we'd just sunk real money and yard time into that unit, continuing and monitoring felt like the more reasonable read of the situation.

Interviewer: When the system showed everything back in the green band, what led you to skip the manual check?

Participant: Mainly that the system readout was clean across the board—no alarms, nothing trending badly. I had the option of pulling a sample; my second engineer wasn't tied up with anything else. But the system existed exactly to tell us this kind of thing, and it was telling me things were fine. Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying.

Interviewer: When the fuel filter report came in, how did you decide where to put your attention?

Participant: At that moment I was watching the turbocharger closely because of the earlier reading, so that's where my head was. The filter note got acknowledged—I told him we'd track it—but I didn't stop what I was doing to dig into it. There was no fuel or combustion symptom tied to it, so it didn't compete strongly for attention against what I already considered the open item.

Interviewer: When the bearing failed with the tide window ten hours out, what options did you consider, and what tipped it?

Participant: Two real options: reduce right down and divert to the nearest port for a proper repair, which would've cost us the tide window and probably several days, or jury-rig something at reduced load and make our original berth. We only had a partial bearing kit onboard, not a full replacement. What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig.

Interviewer: How much did time pressure factor in across these moments, and how confident were you at each stage?

Participant: The tide window was in the back of my mind at every one of these points, more so as we got closer to it. Early on I was fairly confident it was running-in. By the green-band reading I was quite confident there was nothing there. By the fuel filter note I wasn't worried at all—it seemed unrelated. By the failure itself, confidence obviously dropped, but by then options were also narrower.

Interviewer: What would have changed your decision at any of these points—what information was missing?

Participant: If the system had actually thrown an alarm at that first deviation, or if a manual sample early on had shown metal particulates, I'd have acted immediately. The instruments just never gave me that trigger until the spike itself.

Interviewer: Looking back now, how would you characterize that very first vibration reading?

Participant: Honestly, looking at it now, it was probably the bearing telling us something from the start—it seems fairly clear in hindsight that that was the early stage of the same failure, not bedding in at all.

Interviewer: If the overhaul hadn't just happened, do you think you'd have reacted differently to that first signal?

Participant: Probably, yes. Without the overhaul fresh in mind, an elevated reading like that might've gotten a closer look sooner rather than being read as settling-in.

Interviewer: And if there'd been no tide window at all—would the decision at the failure point have gone differently?

Participant: It's possible. Without that deadline pulling at me, diverting might have felt like a cleaner, more straightforward call rather than one that came with a schedule cost attached.

Interviewer: Last one—what would you tell a junior engineer to watch for differently, based on this?

Participant: I'd say don't let a recent repair make you assume a component's off the table for new problems, and don't let one system you're watching closely crowd out something else being reported to you, even if it seems minor at the time.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MO_Biased_5",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Chief Engineer (Marine Engineering)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Turbocharger Bearing Degradation Under Tide-Window Pressure",
    "scenario_summary_internal": "A Chief Engineer aboard a mid-size bulk carrier, three weeks after a costly main-engine turbocharger overhaul, encounters an emerging turbocharger bearing fault during a transit with a fixed tide-restricted berth deadline. Early ambiguous vibration/temperature signals are downplayed partly because the unit was just overhauled and the schedule is tight; automated monitoring readouts are trusted over manual sampling; a secondary fuel-filter differential-pressure cue is deprioritized while attention is fixed on the turbocharger; and after a partial bearing failure, the engineer presses on with a jury-rigged fix rather than diverting, again invoking the overhaul investment and lost troubleshooting time. In post-incident reflection, the engineer reconstructs the earliest signal as having been obviously predictive of failure.",
    "occupational_realism": {
      "objective": "Maintain safe propulsion while meeting a fixed tide-restricted berth window at the discharge port, managing an emerging turbocharger anomaly without unnecessary schedule loss following a recent expensive overhaul.",
      "setting": "Engine room and bridge of a geared bulk carrier, mid-ocean transit, approximately 30 hours from a port with a narrow tidal berthing window; main engine turbocharger overhauled three weeks earlier at significant cost and owner scrutiny.",
      "constraints": [
        "Fixed tide-restricted berth slot with no flexible arrival window",
        "Recent high-cost turbocharger overhaul under owner/technical-superintendent scrutiny",
        "Limited onboard spare parts (partial bearing kit only)",
        "Reduced engine room manning for continuous manual sampling",
        "Weather window closing behind the vessel, discouraging backtracking",
        "Fuel consumption targets tied to charter party terms"
      ],
      "stakeholders": [
        "Chief Engineer",
        "Second Engineer",
        "Master",
        "Technical Superintendent (shore)",
        "Class surveyor (post-incident)",
        "Port agent / charterer schedule coordinator"
      ],
      "technical_terms_to_use": [
        "turbocharger bearing",
        "exhaust gas temperature",
        "scavenge air pressure",
        "differential pressure",
        "lube oil sample",
        "jury rig",
        "load reduction",
        "class survey",
        "tide window",
        "engine monitoring system alarm"
      ],
      "technical_terms_to_avoid": [
        "sunk cost",
        "automation bias",
        "inattentional blindness",
        "hindsight bias",
        "cognitive bias",
        "heuristic",
        "confirmation"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Turbocharger overhaul completed 3 weeks prior at high cost, closely tracked by owners",
          "Minor elevated vibration and exhaust gas temperature deviation on one unit, within nominal alarm band",
          "Fixed tide-restricted berth window roughly 30 hours out",
          "No prior similar fault history on this specific turbocharger since overhaul"
        ],
        "new_information_after_decision": [
          "Readings stabilize temporarily, giving short-term reassurance",
          "No alarm is triggered in the following hours"
        ],
        "alternatives": [
          "Reduce load and inspect the turbocharger promptly",
          "Continue at full sea speed while monitoring the trend"
        ],
        "intended_action": "Continue at full sea speed, reasoning that a unit just overhauled at cost could not plausibly already be failing, and that stopping now would waste the overhaul investment and jeopardize the tide window."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engine monitoring system reports all turbocharger parameters back within green band",
          "No manual lube oil sample or bearing inspection has been taken since the initial deviation",
          "Second Engineer available to take a manual sample if requested",
          "Time pressure from the approaching tide window remains"
        ],
        "new_information_after_decision": [
          "System continues reporting nominal values for several hours with no new alarms",
          "Underlying bearing wear continues undetected beneath system thresholds"
        ],
        "alternatives": [
          "Order a manual lube oil sample and visual bearing check despite the clear system readout",
          "Accept the automated system readout as sufficient and proceed without manual verification"
        ],
        "intended_action": "Accept the automated monitoring system's clear readout as sufficient confirmation and forgo the manual sample, deferring inspection to the next scheduled maintenance."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief Engineer is closely watching the turbocharger dashboard given earlier concern",
          "Second Engineer reports during rounds that fuel filter differential pressure has risen moderately",
          "No abnormal fuel consumption or combustion symptoms observed yet",
          "Turbocharger readings remain the primary focus of attention at this moment"
        ],
        "new_information_after_decision": [
          "The fuel filter differential pressure rise turns out to be unrelated to any developing fault and resolves on its own",
          "No connection is later found between the filter reading and the turbocharger issue"
        ],
        "alternatives": [
          "Pause turbocharger monitoring briefly to investigate the fuel filter differential pressure rise",
          "Continue focused turbocharger monitoring and defer the fuel filter check to routine maintenance"
        ],
        "intended_action": "Continue focused turbocharger monitoring and defer the fuel filter differential pressure check, briefly acknowledging the Second Engineer's report without engaging with it."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Turbocharger exhibits a sudden exhaust temperature spike and audible vibration consistent with partial bearing failure",
          "Approximately 10 hours remain before the tide window closes",
          "Only a partial bearing repair kit is available onboard",
          "Significant time and money have already been invested in the recent overhaul and in troubleshooting so far",
          "Nearest port capable of proper repair would require diverting and missing the tide window"
        ],
        "new_information_after_decision": [
          "The jury-rigged fix holds at reduced load long enough to reach berth, but with continued risk of further degradation",
          "Class surveyor later confirms the bearing damage had been progressing for some time before the spike"
        ],
        "alternatives": [
          "Reduce to a safe minimal load and divert to the nearest port for a proper repair, missing the tide window",
          "Jury-rig a temporary fix and continue at reduced but still meaningful load to reach the original berth on schedule"
        ],
        "intended_action": "Jury-rig a temporary fix and press on at reduced load to preserve the overhaul investment and the time already spent troubleshooting, reaching berth on schedule rather than diverting."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe the voyage and the operational objective at the time this incident began.",
        "What was your role and what were you responsible for monitoring during this transit?"
      ],
      "timeline_reconstruction": [
        "Walk me through what happened from the first sign of trouble to the eventual repair.",
        "What did you observe first, and in what order did subsequent signals appear?"
      ],
      "decision_point_probes": [
        "At the point you first noticed the elevated vibration and temperature, what information did you have, and what alternatives did you weigh?",
        "When the monitoring system showed parameters back in the green band, what made you decide a manual check was or was not necessary?",
        "When the fuel filter differential pressure was reported, how did you decide where to direct your attention?",
        "When the bearing partially failed with limited time before the tide window, what options did you consider, and what tipped your decision?",
        "What prior experience with turbochargers or overhauls influenced how you read these signals?",
        "How much time pressure did you feel at each of these moments, and how did it factor into your decisions?",
        "How confident were you in the readings at each stage, and how did that confidence change?"
      ],
      "closing_hypotheticals": [
        "Looking back, how would you characterize the earliest vibration reading now that you know how things turned out?",
        "If the overhaul had not just been completed, do you think you would have responded differently to the first signal?",
        "If there had been no tide window deadline, would your decision at the point of partial failure have changed?",
        "What would you tell a junior engineer to watch for differently, based on this experience?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "MO5_SC_01",
        "bias": "Sunk cost bias",
        "decision_point": 1,
        "mechanism": "Reluctance to reduce load or inspect because the recent, costly overhaul is treated as evidence the unit cannot be failing, and stopping now would appear to waste that investment.",
        "affected_reasoning_operation": "Weighting of prior investment in the decision to continue vs. inspect",
        "evidence_available_at_time": [
          "Overhaul completed 3 weeks earlier at high cost",
          "Mildly elevated but in-band vibration/temperature readings",
          "Tide window approaching"
        ],
        "required_textual_manifestation": "Engineer explicitly links the decision to continue at full speed to the recency/cost of the overhaul rather than to the actual readings alone.",
        "plausible_nonbias_interpretation": "A reasonable engineer could judge mildly in-band readings as not yet warranting action, independent of overhaul cost.",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "investment bias", "loss aversion"]
      },
      {
        "instance_id": "MO5_AB_01",
        "bias": "Automation Bias",
        "decision_point": 2,
        "mechanism": "Treating the automated monitoring system's green-band readout as sufficient confirmation, foregoing an available and low-cost manual verification step.",
        "affected_reasoning_operation": "Evidence sufficiency judgment / verification-seeking behavior",
        "evidence_available_at_time": [
          "Automated system reporting nominal values",
          "No new alarms",
          "Second Engineer available to take manual sample"
        ],
        "required_textual_manifestation": "Engineer states that the system reading itself was treated as the deciding factor for not manually checking, despite the earlier anomaly.",
        "plausible_nonbias_interpretation": "Trusting a properly functioning, class-approved monitoring system is a legitimate operational default under normal circumstances.",
        "strength": "moderate",
        "do_not_make_explicit": ["automation bias", "over-reliance on automation"]
      },
      {
        "instance_id": "MO5_SA_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 3,
        "mechanism": "Attention narrowly fixed on the turbocharger dashboard causes the fuel filter differential pressure report to be acknowledged but not cognitively processed as an action-relevant cue.",
        "affected_reasoning_operation": "Attention allocation and cue registration among competing signals",
        "evidence_available_at_time": [
          "Turbocharger readings under active close monitoring",
          "Second Engineer's verbal report of rising fuel filter differential pressure"
        ],
        "required_textual_manifestation": "Engineer's account shows the filter report being briefly noted then set aside without engaging its implications, explicitly tied to the turbocharger being the focus at that moment.",
        "plausible_nonbias_interpretation": "Prioritizing an already-flagged system over an unconfirmed, isolated reading can be a defensible triage choice under workload constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["inattentional blindness", "selective attention", "tunnel vision"]
      },
      {
        "instance_id": "MO5_SC_02",
        "bias": "Sunk cost bias",
        "decision_point": 4,
        "mechanism": "Choosing to press on with a jury-rig rather than divert, justified by reference to the overhaul cost and the time already spent troubleshooting rather than solely by the present risk of continued operation.",
        "affected_reasoning_operation": "Weighting of prior time/cost investment in the choice between diverting and continuing",
        "evidence_available_at_time": [
          "Partial bearing failure signals (temperature spike, vibration)",
          "Limited spare parts kit",
          "Time and money already spent on overhaul and troubleshooting",
          "Tide window closing in ~10 hours"
        ],
        "required_textual_manifestation": "Engineer explicitly cites the money/time already spent as a reason to continue rather than basing the decision solely on the present state of the bearing and available repair capability.",
        "plausible_nonbias_interpretation": "Diverting has real, independent costs (missed tide window, charter penalties) that could justify pressing on regardless of prior investment.",
        "strength": "moderate",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment"]
      },
      {
        "instance_id": "MO5_HB_01",
        "bias": "Hindsight Bias",
        "decision_point": 4,
        "mechanism": "In retrospective reflection, the engineer recasts the ambiguous initial vibration/temperature signal as having been obviously predictive of the eventual failure, once the outcome is known.",
        "affected_reasoning_operation": "Retrospective causal attribution and memory reconstruction of the original signal's clarity",
        "evidence_available_at_time": [
          "Knowledge of the eventual bearing failure outcome",
          "Recollection of the phase-1 vibration/temperature reading, which was in-band at the time"
        ],
        "required_textual_manifestation": "In response to a closing hypothetical/reflection probe, the engineer describes the earliest signal as something that 'should have been obvious' or 'clearly meant trouble,' inconsistent with how it was actually treated as in-band at the time.",
        "plausible_nonbias_interpretation": "With full information, some signals genuinely are clearer in retrospect without any biased reconstruction of one's past confidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "creeping determinism", "knew-it-all-along"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no control scenario requested for this generation."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence vs. absence of the fixed tide-restricted berth deadline (schedule time pressure)",
      "original_state": "A fixed tide-restricted berth window roughly 30 hours out creates continuous schedule pressure throughout the incident.",
      "counterfactual_state": "No tide restriction; the vessel has a flexible arrival window with no binding schedule deadline.",
      "variables_to_hold_constant": [
        "Turbocharger fault progression and physical failure mechanics",
        "Recent overhaul history and cost",
        "Crew composition and roles",
        "Automated monitoring system behavior",
        "Fuel filter differential pressure event"
      ],
      "expected_causal_difference": "Removing the schedule deadline should reduce or eliminate the schedule-linked pressing-on decision at decision point 4 and weaken the framing of decision point 1, if those instances are genuinely driven by time pressure rather than by the overhaul investment alone.",
      "causal_test_question": "Absent a fixed tide window, would the Chief Engineer still have chosen to jury-rig and continue rather than divert once the bearing partially failed?"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Exactly 5 total bias instances are planned, matching the manifest sum (2+1+1+1).",
      "No decision point hosts more than two instances of the same bias.",
      "Decision point 4 hosts two different biases (sunk cost, hindsight) via distinct reasoning operations and evidence sources.",
      "No bias-labeling or psychological terminology is scheduled to appear in the public interview.",
      "Each instance has a plausible non-bias explanation to avoid mechanical proof of bias from outcome alone.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points plus opening/closing probes without repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Sunk cost bias",
        "occurrences": 2,
        "mechanism_constraint": "Must reference prior investment (overhaul cost and/or time already spent troubleshooting) as a stated reason for the decision, at two distinct decision points with distinct evidence."
      },
      {
        "bias": "Automation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must show reliance on automated monitoring readout as sufficient, in place of an available manual verification step."
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must show a competing cue being registered but not processed for action due to attentional focus elsewhere."
      },
      {
        "bias": "Hindsight Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must occur only in retrospective reflection/probe response, recasting an originally ambiguous signal as having been obviously predictive."
      }
    ],
    "target_bias_names": [
      "Sunk cost bias",
      "Automation Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Hindsight Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Sunk cost bias", "requested_occurrences": 2 },
      { "bias": "Automation Bias", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 },
      { "bias": "Hindsight Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias" },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias" },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias" },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias", "decision_point": 1 },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias", "decision_point": 2 },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 3 },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias", "decision_point": 4 },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MO5_SC_01",
        "bias": "Sunk cost bias",
        "mechanism": "Continuing at full speed because a recently, expensively overhauled unit is assumed unlikely to fail, treating the investment as evidence against the current reading.",
        "affected_reasoning_operation": "Weighting of prior investment in continue-vs-inspect decision",
        "evidence_source": "Overhaul cost/recency plus phase-1 vibration and temperature readings",
        "distinctiveness_requirement": "Distinct from MO5_SC_02 by decision point, by the specific evidence (initial ambiguous reading vs. active partial failure), and by the action considered (continuing without inspection vs. pressing on instead of diverting)."
      },
      {
        "instance_id": "MO5_AB_01",
        "bias": "Automation Bias",
        "mechanism": "Accepting the automated monitoring system's nominal readout as sufficient confirmation, forgoing available manual verification.",
        "affected_reasoning_operation": "Evidence-sufficiency judgment / verification-seeking",
        "evidence_source": "Automated system readout vs. availability of manual lube oil sample",
        "distinctiveness_requirement": "Sole instance of this bias; must not be repeated at any other decision point or probe."
      },
      {
        "instance_id": "MO5_SA_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Fixation on turbocharger dashboard causes the fuel filter differential pressure report to be noted but not processed as actionable.",
        "affected_reasoning_operation": "Attention allocation among competing simultaneous cues",
        "evidence_source": "Second Engineer's verbal report of rising fuel filter differential pressure during active turbocharger monitoring",
        "distinctiveness_requirement": "Sole instance of this bias; must not be repeated in later probes or the phase-4 crisis handling."
      },
      {
        "instance_id": "MO5_SC_02",
        "bias": "Sunk cost bias",
        "mechanism": "Choosing to jury-rig and continue toward the tide window rather than divert, citing prior time/cost investment rather than only present risk.",
        "affected_reasoning_operation": "Weighting of prior time/cost investment in divert-vs-continue decision",
        "evidence_source": "Partial bearing failure signals plus cumulative overhaul cost and troubleshooting time already spent",
        "distinctiveness_requirement": "Distinct from MO5_SC_01 by decision point, evidence (active failure vs. initial ambiguous signal), and the specific investment referenced (cumulative time+cost vs. overhaul recency alone)."
      },
      {
        "instance_id": "MO5_HB_01",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively recasting the ambiguous phase-1 signal as having been obviously predictive of failure, inconsistent with how it was treated at the time.",
        "affected_reasoning_operation": "Retrospective causal attribution / memory reconstruction",
        "evidence_source": "Closing hypothetical/reflection probe response referencing the phase-1 reading with outcome knowledge",
        "distinctiveness_requirement": "Occurs only in retrospective probe response tied to decision point 4's aftermath, not in the real-time decision itself; distinct reasoning operation from MO5_SC_02's forward-looking action choice."
      }
    ],
    "intended_strength": [
      { "instance_id": "MO5_SC_01", "bias": "Sunk cost bias", "strength": "subtle" },
      { "instance_id": "MO5_SC_02", "bias": "Sunk cost bias", "strength": "moderate" },
      { "instance_id": "MO5_AB_01", "bias": "Automation Bias", "strength": "moderate" },
      { "instance_id": "MO5_SA_01", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "subtle" },
      { "instance_id": "MO5_HB_01", "bias": "Hindsight Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence vs. absence of the fixed tide-restricted berth deadline (schedule time pressure)",
      "original_state": "A fixed tide-restricted berth window roughly 30 hours out creates continuous schedule pressure throughout the incident.",
      "changed_state": "No tide restriction; flexible arrival window with no binding schedule deadline.",
      "variables_to_hold_constant": [
        "Turbocharger fault progression and physical failure mechanics",
        "Recent overhaul history and cost",
        "Crew composition and roles",
        "Automated monitoring system behavior",
        "Fuel filter differential pressure event"
      ]
    },
    "scenario_id": "MO_Biased_5",
    "domain_id": "MO",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across distinct decision points where possible; sunk cost split across decision points 1 and 4 with distinct evidence and referenced investments; automation bias and selective attention each assigned to their single mechanism-fitting decision point (2 and 3 respectively); hindsight bias assigned to decision point 4's retrospective aftermath, sharing the decision point with the second sunk cost instance but differing in reasoning operation (forward action choice vs. retrospective causal attribution) and evidence source (real-time failure signals vs. outcome-informed recollection), per rule 4.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Turbocharger fault progression and physical failure mechanics",
      "Recent overhaul history and cost",
      "Crew composition and roles",
      "Automated monitoring system behavior",
      "Fuel filter differential pressure event"
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
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "First-deviation probe: raw readings were in-band, the unit had just been overhauled, and continuing while monitoring felt more reasonable than easing off and inspecting after the investment in the unit.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "MO5_SC_01"
          ],
          "ground_truth_rationale": "The participant links the continue-versus-inspect choice to the recent costly overhaul and time already invested, beyond the in-band readings alone."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Green-band probe: the monitoring readout was clean, a manual sample was available, and the participant regarded manual checking as merely confirming what the instruments already said.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "MO5_AB_01"
          ],
          "ground_truth_rationale": "The automated green-band readout was treated as sufficient confirmation in place of available manual verification."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Fuel-filter probe: attention remained on the turbocharger; the filter note was acknowledged but deferred because it lacked a fuel or combustion symptom.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "MO5_SA_01"
          ],
          "ground_truth_rationale": "A competing differential-pressure cue was registered but not processed for action because attention was fixed on the turbocharger."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Bearing-failure probe: after comparing diversion with a jury-rig, the participant said the overhaul cost and troubleshooting time already spent made diversion feel wasteful on top of the schedule hit.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "MO5_SC_02"
          ],
          "ground_truth_rationale": "The decision to continue at reduced load was justified by prior money and time investment rather than only the present risk and repair options."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "confidence_and_pressure_reasoning",
          "raw_interview_anchor": "Time-pressure and confidence response: confidence varied from running-in to no concern to reduced confidence at failure, while the tide window narrowed the options.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This explains confidence and operational pressure but does not independently manifest one of the hidden target mechanisms."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "evidence_threshold_reasoning",
          "raw_interview_anchor": "Missing-information response: an alarm or metal particulates in an early manual sample would have triggered action, but the instruments did not provide that trigger.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant identifies an evidence threshold that would have changed the decision; this is not itself a hidden bias occurrence."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "retrospective_reasoning",
          "raw_interview_anchor": "Looking-back reflection: the initial vibration was described as probably indicating the bearing problem from the start and fairly clear in hindsight, rather than bedding in.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "MO5_HB_01"
          ],
          "ground_truth_rationale": "After learning the outcome, the participant recasts the originally ambiguous in-band signal as clearly predictive of the failure."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "counterfactual_reasoning",
          "raw_interview_anchor": "No-tide-window counterfactual: without the deadline, diverting might have felt cleaner because it would not carry the same schedule cost.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a schedule-pressure counterfactual and does not by itself establish a hidden cognitive-bias instance."
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
    "analysis_scope_note": "Blind diagnostic evaluation of a single CTA interview transcript; only transcript statements are used as occurrence evidence, with no assumption of experimental condition or expected biases."
  },
  "identified_bias_summary": [
    {
      "bias_label": "automation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "expectation bias",
        "congeniality bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's existing beliefs or expectations.",
      "attributed_to_speaker": "Participant (Chief Engineer)",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of post-overhaul turbocharger temperature and vibration",
      "decision_point_description": "Whether to reduce speed/inspect or continue at load and monitor after the first elevated exhaust gas temperature and vibration readings.",
      "affected_reasoning_operation": "Interpretation of ambiguous sensor evidence and causal inference about the turbocharger condition",
      "bias_specific_mechanism": "The fresh overhaul created a strong prior expectation that the unit was healthy; the participant interpreted mildly abnormal readings as post-rebuild bedding-in and discounted the competing bearing-fault hypothesis despite the diagnostic uncertainty.",
      "manifestation_in_interview": "The participant states the overhaul made a bearing problem 'seem like a stretch' and that he read the signal as 'running-in rather than as an actual fault.' He later confirms that without the overhaul fresh in mind, the same reading likely would have been examined sooner.",
      "effect_on_reasoning_or_decision": "The interpretation reduced the perceived need for immediate manual inspection or speed reduction and led to continued monitoring while preserving the tide schedule.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given we'd literally just had that unit stripped and rebuilt, my first read was that it was probably just bedding in, maybe slightly different clearances after the overhaul.",
          "evidence_explanation": "This quote shows the recent-overhaul expectation being used to explain away an abnormal reading before disconfirming checks."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking it made more sense as running-in than as an actual fault.",
          "evidence_explanation": "This quote directly reveals selective interpretation of ambiguous evidence toward the prior expectation rather than neutrally weighing the fault hypothesis."
        }
      ],
      "correction_or_counterevidence": "The readings were still inside the normal band and no alarm had triggered, so some expectation of bedding-in after overhaul could be a legitimate engineering prior. However, the participant's counterfactual admission that the same signal would likely have been examined more closely absent the overhaul indicates the prior strongly shaped the interpretation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage in the supplied RAG context directly defines or supports this bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "automation bias",
      "alternative_labels": [
        "automation complacency",
        "automation overreliance"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overtrust automated system output and to fail to seek or act on additional independent information when the system appears nominal.",
      "attributed_to_speaker": "Participant (Chief Engineer)",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Green-band monitoring readings and omission of manual lube oil sample",
      "decision_point_description": "Whether to order a manual lube oil sample or other independent check after the monitoring system returned to green following an earlier anomaly.",
      "affected_reasoning_operation": "Evidence weighting and information-search/verification behavior",
      "bias_specific_mechanism": "The clean automated system readout was treated as sufficient proof of a healthy system, suppressing the decision to conduct an available independent check despite a recent unexplained anomaly. This overreliance on the monitoring system's green status reduced diagnostic vigilance.",
      "manifestation_in_interview": "The participant reports that he did not have the second engineer pull a lube oil sample and says the system was there to tell them this and was showing green; an additional manual check felt redundant.",
      "effect_on_reasoning_or_decision": "An early manual lube oil sample was skipped, removing a possible early detection opportunity for metal particulates and allowing the failure to progress unnoticed until the later spike.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have my second engineer pull a lube oil sample at that point. The system was telling me it was fine, and honestly that's what it's there for.",
          "evidence_explanation": "This shows automated system information was accepted as sufficient and displaced an available independent diagnostic action."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But the system existed exactly to tell us this kind of thing, and it was telling me things were fine. Doing a manual check on top of a clean system readout felt like it would've just confirmed what the instruments were already saying.",
          "evidence_explanation": "This quote demonstrates the overreliance mechanism: the clean instrument readout made independent verification seem unnecessary."
        }
      ],
      "correction_or_counterevidence": "Relying on monitoring instrumentation in the absence of alarms or adverse trends is a standard engineering practice, and there is no stated policy requiring manual sampling. Therefore the behavior could reflect ordinary professional reliance rather than a clear distortion; hence low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage in the supplied RAG context directly defines or supports this bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "sunk cost effect",
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to let already-invested and unrecoverable resources influence current decisions, even though only future costs and benefits should matter.",
      "attributed_to_speaker": "Participant (Chief Engineer)",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Failure decision between diverting for repair and jury-rigging to preserve the original berth",
      "decision_point_description": "Whether to reduce speed and divert to the nearest port for proper repair or to jury-rig at reduced load and make the tide-restricted berth after the bearing failure.",
      "affected_reasoning_operation": "Option evaluation and risk/benefit tradeoff under uncertainty",
      "bias_specific_mechanism": "The participant included past overhaul cost and prior troubleshooting time—both sunk costs—as decisional reasons for avoiding diversion. This distorted the current comparison by making diversion feel like wasting previous investment rather than assessing only future safety, repair, and schedule consequences.",
      "manifestation_in_interview": "The participant explicitly says what tipped the decision was that they had already put so much into the unit and diverting felt like it would waste all of that in addition to the schedule hit.",
      "effect_on_reasoning_or_decision": "The jury-rig option was selected partly to avoid psychological loss associated with prior investment, rather than purely on expected future consequences of repair versus delay.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "What tipped it, honestly, was that we'd already put so much into this unit—the overhaul cost, the time we'd already spent watching and troubleshooting it—and diverting felt like it would waste all of that on top of the schedule hit. So we went with the jury rig.",
          "evidence_explanation": "This is a direct statement of sunk-cost reasoning: past efforts and expenditures are treated as if they should be preserved in the current decision."
        }
      ],
      "correction_or_counterevidence": "The choice may also have had practical justifications: only a partial bearing kit was onboard, and a proper repair would have cost the tide window and several days. Nevertheless, the explicit invocation of past overhaul cost and prior time as decision-relevant is the hallmark of the sunk cost fallacy, so the occurrence is rated high confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage in the supplied RAG context directly defines or supports this bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis",
        "goal fixation"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant (Chief Engineer)",
      "possible_decision_episode_label": "Failure decision under tide-window pressure",
      "supporting_interview_quote": "It's possible. Without that deadline pulling at me, diverting might have felt like a cleaner, more straightforward call rather than one that came with a schedule cost attached.",
      "plausible_mechanism": "Commitment to the original tide-restricted berth and the looming deadline may have biased option evaluation toward preserving the original plan despite the bearing failure.",
      "why_not_identified": "The transcript shows a deliberate comparison of repair versus schedule costs and a load-reduction mitigation; this is insufficient to rule out a rational operational tradeoff under time constraints, so it is treated as a candidate rather than an identified occurrence."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "attentional bias",
      "alternative_labels": [
        "attentional tunneling",
        "cognitive tunneling"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant (Chief Engineer)",
      "possible_decision_episode_label": "Fuel filter differential pressure report",
      "supporting_interview_quote": "I was pretty focused on the turbocharger numbers at that point given the earlier concern, so I told him to keep an eye on it and we'd deal with it later—there was no fuel consumption issue or anything on the combustion side, so it didn't feel urgent next to what I was already watching.",
      "plausible_mechanism": "Selective attention to the previously flagged turbocharger may have reduced processing of the fuel filter report, crowding out a potentially separate fault cue.",
      "why_not_identified": "The fuel filter signal was diffuse, had no combustion-system corollary, and could reasonably be triaged as lower priority; there is no affirmative evidence that a bias-specific attentional distortion rather than ordinary task prioritization occurred."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant (Chief Engineer)",
      "possible_decision_episode_label": "Retrospective assessment of the initial vibration signal",
      "supporting_interview_quote": "Honestly, looking at it now, it was probably the bearing telling us something from the start—it seems fairly clear in hindsight that that was the early stage of the same failure, not bedding in at all.",
      "plausible_mechanism": "After knowing the subsequent failure, the participant may have reconstructed the initial signal as being more diagnostic than it was at the time.",
      "why_not_identified": "The participant explicitly frames the clarity as hindsight and does not claim he should have known in advance; this may be ordinary retrospective updating rather than biased memory reconstruction or overestimation of foreseeability."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were present in the supplied RAG context; therefore corpus_evidence arrays are empty and analysis_metadata.retrieved_corpus_support_used is false.",
    "The analysis is based on a single self-report interview, which may involve post-hoc reconstruction or self-presentation.",
    "Some observed behaviors plausibly overlap with legitimate operational heuristics, particularly reliance on automated monitoring and schedule-constrained decision-making."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Biased_5_Gemini_off",
  "interview_id": "MO_Biased_5",
  "system_prompt_id": "Gemini",
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
