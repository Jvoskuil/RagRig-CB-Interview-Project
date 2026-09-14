You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time. This is a voluntary debrief reconstructing your decision-making on a specific fire support mission—not an evaluation for any board. You can decline any question. Good to proceed?

Participant: Sure, happy to walk through it.

Interviewer: Can you describe your role and the mission?

Participant: I was the FSO attached to the company for a daylight clearing operation. We had an 82mm mortar team that had been harassing our forward positions, and intel flagged a possible staging compound near a village on the north edge of the objective. My job was coordinating mortars, then CAS, then artillery, to clear both threats before the company crossed the line of departure. Objective was simple enough on paper—suppress the mortar team, clear the compound, don't hit friendlies or the village.

Interviewer: What made this mission nonroutine?

Participant: We had a fairly generous window that day, about ninety minutes before the company needed to cross the line, so time wasn't the crunch it sometimes is. But ammo for the 81s was still limited from earlier use, comms between me and FSCC kept dropping intermittently, the compound was close enough to friendly squads to be danger-close, and the only real-time read on the compound came from a single ISR feed with no second source.

Interviewer: Walk me through the sequence as it happened.

Participant: First was the mortar mission against the mortar position. Adjustment round one landed short. Round two, also short. Section chief checked the gun-line data once, said no fault found. We still had most of the ninety minutes ahead of us at that point. Around the same time, I had two conflicting reports on the staging activity—battalion JTAC had one grid, the partner-force liaison next to us had a grid about three hundred meters off. Then CAS checked in for the compound piece, and last was the ISR cue on the compound right before the artillery mission.

Interviewer: Let's take the mortar rounds first. What was the decision?

Participant: Two rounds down, both short, section chief's one check came back clean. I had time to have them do a full re-lay from scratch—level, deflection, the works—or just fire the next adjustment round and see what happened.

Interviewer: What did you decide?

Participant: Fired again. Two shorts in a row, felt like we were due for one on target.

Interviewer: You mentioned you had close to ninety minutes at that point. Did the time available factor into the call?

Participant: Not really, if I'm honest. I had plenty of time to stop and have them recheck everything properly. I just didn't feel like it was necessary—the pattern read as random scatter that would correct itself.

Interviewer: What happened with that third round?

Participant: Also short. Turned out later there was a leveling error on the gun, unrelated to the first two misses. We caught it on a fourth check.

Interviewer: If the section chief had reported a confirmed fault after the first miss, would your third-round call have changed?

Participant: Yes, immediately—I'd have stopped for the recheck. Without a flagged fault, I read it as scatter that would sort itself out.

Interviewer: Now the grid discrepancy. What did you have?

Participant: Battalion JTAC, same battalion as me, called Grid A for the staging activity. Around the same time, the partner-force liaison called Grid B, roughly three hundred meters off, similar confidence in both reports. Nothing on paper that clearly outranked the other.

Interviewer: How did you resolve it, given you had time to check both?

Participant: I went with Grid A. It came through our own FSCC net, format I was used to, source I'd worked with the whole deployment. I did have the time to cross-check Grid B properly—there wasn't really anything stopping me—I just leaned toward our own channel.

Interviewer: Did anything come of Grid B later?

Participant: Follow-on recon picked up some indicators there too. Wasn't nothing. We just didn't chase it down at the time.

Interviewer: If the partner-force liaison's report had come through your own channel instead, would you have weighted it the same as Grid A?

Participant: Probably would've given it more credit. Hard to explain exactly why, but hearing it through your own net makes it feel more solid, even without a concrete reason the information itself was better.

Interviewer: Let's cover the CAS run. What was the situation?

Participant: Pilot on station, ready for a danger-close run near the compound. We'd run several strikes with this squadron over the deployment, all clean, standard margins. This time friendly-squad positioning put us tighter than usual, and we'd had comms dropouts with the lead squad in the minutes before.

Interviewer: What were your options, given the window you had?

Participant: I could've widened the margin or delayed for a stable comms check—we had plenty of time to do that without missing the assault—or cleared it with the tighter margin as-is.

Interviewer: What did you choose?

Participant: Cleared it hot with the tighter margin. This squadron had been reliable every time, so I expected the same result.

Interviewer: What happened with comms during the final attack heading confirmation?

Participant: Dropped again for about ten seconds. Came back before the pilot needed the call, so it worked out, but closer than I'd like looking back, especially since I had the time to just wait it out.

Interviewer: If this had been the squadron's first-ever danger-close run with you, would you have set the same margin?

Participant: No, I'd have wanted the wider margin and a cleaner comms check. The track record with them is what made the tighter margin feel acceptable.

Interviewer: Last one—the artillery mission on the compound.

Participant: Right before we committed the 155s, the ISR feed flagged one cue, "possible enemy activity" at the compound. That sector had been quiet the whole deployment, mostly normal village pattern-of-life, and that sensor had a track record of throwing false hits in that terrain.

Interviewer: What were the alternatives, given you had time to spare?

Participant: Get a second source to confirm, since the area had been so quiet, or approve the mission off the one cue. We genuinely had time for the first option that day.

Interviewer: What did you decide?

Participant: I approved it off the single cue. It matched what we were looking for, so I went with it.

Interviewer: What did the post-strike assessment show?

Participant: Mixed—some indicators of prior enemy presence, some signs it might've been unoccupied by then. Inconclusive.

Interviewer: If the sector had a recent history of confirmed enemy activity, would that one cue have been enough on its own?

Participant: Probably would've felt about the same either way—I was focused on the cue itself more than the sector's overall track record.

Interviewer: Across all four decisions, how did having that extra time affect your process?

Participant: Honestly, less than I'd have expected. I used some of it—double-checked timing on the CAS brief, confirmed the 9-line details—but on the calls that mattered most, I don't think the extra time changed how I read the situation.

Interviewer: Anything you'd do differently?

Participant: Maybe push for that mortar recheck early since I clearly had the time for it, and get a second look at the compound cue rather than moving straight to the artillery mission. Given how much time we actually had, I probably could have afforded to slow down more than I did.

Interviewer: Thanks for the detail—that's very helpful.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Counterfactual_4",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Fire Support Officer (FSO) / Joint Fires Observer",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Danger-Close, More Time: Fire Support Coordination Under an Extended Assault Window",
    "scenario_summary_internal": "A counterfactual of MD_Biased_4 in which the same FSO/JFO, same unit, same mortar/CAS/artillery sequence, and same four fire-support decisions occur, but the company has a 90-minute window before crossing the line of departure instead of 30 minutes. All other material facts (ammunition limits, comms degradation, danger-close geometry, civilian presence, single-sensor ISR reliability, and the same four decisions) are held constant, isolating the causal effect of reduced time pressure on whether the same reasoning patterns still appear.",
    "occupational_realism": {
      "objective": "Suppress/destroy an enemy 82mm mortar team harassing the company's forward positions and clear a suspected staging compound before the assault window closes, without fratricide or civilian casualties.",
      "setting": "Daylight combined-arms clearing operation; company commander and FSO co-located at a forward command post; battalion Fire Support Coordination Center (FSCC), a CAS aircraft on station, and an adjacent partner-force unit all in the fires network. The company has a 90-minute window before crossing the line of departure, rather than the tighter window in the paired scenario.",
      "constraints": [
        "Limited 81mm mortar ammunition remaining for adjustment rounds",
        "90-minute window before the company must cross the line of departure",
        "Intermittent radio/data-link degradation between FSCC and forward observers",
        "Danger-close proximity of friendly squads to the target compound",
        "Possible civilian presence in the adjacent village",
        "Single organic ISR feed with known intermittent false-positive history"
      ],
      "stakeholders": [
        "Company commander",
        "Fire Support Officer / Joint Fires Observer (interviewee)",
        "Battalion FSCC watch officer",
        "Mortar section chief",
        "CAS pilot on station",
        "Adjacent partner-force liaison officer",
        "ISR/sensor analyst"
      ],
      "technical_terms_to_use": [
        "adjust fire",
        "danger close",
        "CDE (collateral damage estimate)",
        "9-line brief",
        "grid coordinate",
        "FSCC",
        "positive identification (PID)",
        "final attack heading",
        "cleared hot"
      ],
      "technical_terms_to_avoid": [
        "gambler's fallacy",
        "optimism bias",
        "in-group bias",
        "base rate",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two successive 81mm adjustment rounds have landed short of the mortar position",
          "Mortar section reports gun-line data checked once, no fault found",
          "Roughly 90 minutes remain before the assault window closes, leaving ample time for a recheck"
        ],
        "new_information_after_decision": [
          "Third round result (on or off target) is learned only after firing",
          "A later data check reveals a leveling error unrelated to prior rounds"
        ],
        "alternatives": [
          "Order a full re-lay and data recheck of the gun line before firing again",
          "Fire the next adjustment round immediately, expecting the miss streak to end"
        ],
        "intended_action": "FSO authorizes firing another adjustment round without a full re-lay, reasoning that after two misses a hit is 'due', even though the extended window would have comfortably allowed a recheck first."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Battalion JTAC (same service) reports the enemy staging point at Grid A",
          "Adjacent partner-force liaison independently reports enemy activity at Grid B, roughly 300m away",
          "Both reports carry similar confidence caveats; the extended window leaves time to cross-check both before acting"
        ],
        "new_information_after_decision": [
          "Follow-on reconnaissance shows some indicators near Grid B as well as Grid A"
        ],
        "alternatives": [
          "Request cross-verification of both grids before committing fires",
          "Prioritize the battalion JTAC's grid because it comes through the FSO's own chain"
        ],
        "intended_action": "FSO weights the battalion JTAC's coordinate more heavily than the partner-force report largely because it originates from his own unit's channel, despite having time available to verify both."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "CAS pilot is ready for a danger-close run near friendly positions",
          "The last several CAS strikes with this squadron were executed cleanly with standard margins",
          "Current friendly-troop proximity is tighter than the squadron's usual margin, and communications with the lead squad have had brief dropouts; the extended window would allow a delay to reset comms without missing the assault"
        ],
        "new_information_after_decision": [
          "Communications with the lead squad drop out again during the final attack heading confirmation"
        ],
        "alternatives": [
          "Widen the safety margin or delay the run pending a stable communications check",
          "Proceed with the tighter margin, expecting it to go as smoothly as the recent strikes"
        ],
        "intended_action": "FSO clears the CAS run with the tight margin, expecting the outcome to match the string of recent successful strikes, even though the longer window removed most of the time pressure to skip the delay."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The sole ISR sensor flags a single 'possible enemy activity' cue at the suspected compound",
          "The sector has historically been quiet with routine civilian pattern-of-life",
          "The specific sensor type has a known history of false positives in this terrain; the extended window leaves time to request a second confirming source"
        ],
        "new_information_after_decision": [
          "Post-strike assessment of what was actually present at the compound"
        ],
        "alternatives": [
          "Request a second confirming source given the sector's normally low enemy-activity rate",
          "Approve the artillery mission on the single sensor cue alone"
        ],
        "intended_action": "FSO approves the fire mission based on the one sensor cue, without factoring in how rarely this sector produces genuine enemy activity or how often this sensor errs, despite having time to seek confirmation."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe the mission and your role that day?",
        "What was the operational objective at the start of the clearing operation?"
      ],
      "timeline_reconstruction": [
        "Walk me through the sequence of fire missions in the order they happened.",
        "What information did you have at each stage, and what changed afterward?"
      ],
      "decision_point_probes": [
        "What cues made you decide to fire again without a full re-lay, given how much time you had?",
        "How did you weigh the battalion JTAC's grid against the partner-force liaison's grid?",
        "What made you comfortable clearing the CAS run with a tighter margin than usual?",
        "How did the sector's history factor into your decision to approve the artillery mission on one sensor cue?",
        "What information sources did you rely on most at each point, and why?",
        "With as much time as you had that day, how did that affect your process at each decision?",
        "How confident were you in each call, and what would have changed your mind?",
        "Looking back, what would you do differently if you replayed each decision?"
      ],
      "closing_hypotheticals": [
        "If the mortar section had reported a confirmed fault after the first miss, would your third-round decision have changed?",
        "If the partner-force liaison's report had come through your own chain instead, would you have weighted it differently?",
        "If this had been the squadron's first-ever danger-close run with you, would you have set the same margin?",
        "If the sector had a recent history of confirmed enemy activity, would one sensor cue have been enough for you?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "gf_01",
        "bias": "Gamblers Fallacy",
        "decision_point": 1,
        "mechanism": "Treating independent artillery/mortar rounds as part of a self-correcting streak, expecting a hit because prior rounds missed, despite ample time available for a recheck",
        "affected_reasoning_operation": "Probabilistic inference about an upcoming independent event",
        "evidence_available_at_time": [
          "Two prior adjustment rounds landed short",
          "No confirmed fault yet identified in the gun line",
          "90-minute window leaves ample time for a full re-lay"
        ],
        "required_textual_manifestation": "FSO explicitly reasons that because the last two rounds missed, the next one is likely to hit, rather than ordering a data recheck, even though time was not the binding constraint",
        "plausible_nonbias_interpretation": "The FSO may have simply trusted the section chief's single check as sufficient without needing time pressure as a justification",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "streak", "independent probability"]
      },
      {
        "instance_id": "ig_01",
        "bias": "Ingroup Preference bias or In-group bias",
        "decision_point": 2,
        "mechanism": "Discounting an equally credible report because it originates from an outside unit rather than the FSO's own chain, despite time available to cross-verify",
        "affected_reasoning_operation": "Weighting and integration of two competing evidence sources",
        "evidence_available_at_time": [
          "Battalion JTAC (same service/unit) reports Grid A",
          "Partner-force liaison reports Grid B with similar confidence caveats",
          "Extended window permits verification of both grids"
        ],
        "required_textual_manifestation": "FSO states or implies that the battalion JTAC's grid was trusted more simply because it came through his own unit's channel",
        "plausible_nonbias_interpretation": "The battalion JTAC's report may have used a more familiar reporting format that was easier to verify quickly",
        "strength": "subtle",
        "do_not_make_explicit": ["in-group", "own unit trust", "outgroup discount"]
      },
      {
        "instance_id": "ob_01",
        "bias": "Optimism bias",
        "decision_point": 3,
        "mechanism": "Underestimating the risk of a tighter-than-usual danger-close margin because recent strikes with the same squadron succeeded, despite time available to delay for a comms reset",
        "affected_reasoning_operation": "Risk assessment and forecasting of mission outcome",
        "evidence_available_at_time": [
          "Recent history of clean CAS strikes with this squadron",
          "Current margin tighter than normal and comms dropouts with lead squad",
          "Extended window allows a delay without missing the assault"
        ],
        "required_textual_manifestation": "FSO expresses confidence the run would go fine like the recent strikes, despite the tighter margin and comms issue and despite having time to wait",
        "plausible_nonbias_interpretation": "The squadron's demonstrated proficiency was a legitimate factor supporting a calculated risk decision",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "unrealistic confidence", "overestimate success odds"]
      },
      {
        "instance_id": "brn_01",
        "bias": "Base-rate neglect",
        "decision_point": 4,
        "mechanism": "Approving fires on a single sensor cue while ignoring the sector's low historical enemy-activity rate and the sensor's known false-positive rate, despite time available to seek a second source",
        "affected_reasoning_operation": "Updating a target-identification judgment given prior probability and current evidence",
        "evidence_available_at_time": [
          "Single 'possible enemy activity' sensor cue",
          "Sector's historically low/quiet enemy-activity pattern",
          "Sensor's known history of false positives in this terrain",
          "Extended window allows time to request confirmation"
        ],
        "required_textual_manifestation": "FSO approves the mission based mainly on the cue without weighing how rarely this sector or sensor type produces genuine hits, even though time was not the binding constraint",
        "plausible_nonbias_interpretation": "The FSO may have judged the cue's specificity as strong enough evidence on its own merits, independent of available time",
        "strength": "subtle",
        "do_not_make_explicit": ["base rate", "prior probability", "false positive rate"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "MD_Biased_4",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a counterfactual variant, not a vocabulary or ambiguous control."
    },
    "counterfactual_specification": {
      "causal_variable": "Duration of the pre-assault time window (time-pressure level) before the company crosses the line of departure",
      "original_state": "30-minute window before the assault, framed throughout MD_Biased_4 as a binding time constraint on all four decisions",
      "counterfactual_state": "90-minute window before the assault, removing time pressure as a plausible binding constraint while all other facts, actors, evidence, and decision alternatives remain the same",
      "variables_to_hold_constant": [
        "Ammunition limitations for the 81mm mortar section",
        "Intermittent radio/data-link degradation between FSCC and forward observers",
        "Danger-close proximity of friendly squads to the target compound",
        "Possible civilian presence in the adjacent village",
        "Single organic ISR feed with known false-positive history",
        "Identity and roles of all stakeholders",
        "The four decisions, their alternatives, and their sequence",
        "The mechanisms and strength of all four embedded reasoning patterns"
      ],
      "expected_causal_difference": "With time pressure substantially reduced, the same reasoning patterns observed in MD_Biased_4 should be harder to justify purely as rational time-constrained trade-offs, isolating whether the patterns persist independent of urgency",
      "causal_test_question": "Do the same four decisions and reasoning patterns still occur when the FSO has ample time to recheck data, cross-verify sources, delay for comms stability, and seek a second confirming source, rather than being forced by a tight window?"
    },
    "generation_checks": [
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Each of the four manifest biases is embedded exactly once, at a distinct decision point, matching the paired scenario's instance structure.",
      "No bias labels, definitions, or psychological terminology appear in probes or narrative.",
      "Each instance has an available plausible non-bias explanation to avoid mechanical proof of bias.",
      "Only the time-window/time-pressure variable is changed relative to MD_Biased_4; all other material facts, actors, and constraints are held constant.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points, probe coverage, and chronological narrative without repetitive exposition.",
      "Consequences described (round results, strike outcomes, post-strike assessment) do not confirm or deny bias presence mechanically."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Gamblers Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must involve reasoning about an upcoming independent artillery/mortar round based on prior round outcomes, under reduced time pressure"
      },
      {
        "bias": "Ingroup Preference bias or In-group bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve differential weighting of two evidence sources based on unit affiliation rather than evidentiary quality, under reduced time pressure"
      },
      {
        "bias": "Optimism bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve underestimating risk of a specific mission element based on a recent favorable track record, under reduced time pressure"
      },
      {
        "bias": "Base-rate neglect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve disregarding sector-level or sensor-level prior probability in favor of a single specific cue, under reduced time pressure"
      }
    ],
    "target_bias_names": [
      "Gamblers Fallacy",
      "Ingroup Preference bias or In-group bias",
      "Optimism bias",
      "Base-rate neglect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Gamblers Fallacy", "requested_occurrences": 1 },
      { "bias": "Ingroup Preference bias or In-group bias", "requested_occurrences": 1 },
      { "bias": "Optimism bias", "requested_occurrences": 1 },
      { "bias": "Base-rate neglect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy" },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias" },
      { "instance_id": "ob_01", "bias": "Optimism bias" },
      { "instance_id": "brn_01", "bias": "Base-rate neglect" }
    ],
    "intended_decision_points": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy", "decision_point": 1 },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias", "decision_point": 2 },
      { "instance_id": "ob_01", "bias": "Optimism bias", "decision_point": 3 },
      { "instance_id": "brn_01", "bias": "Base-rate neglect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "gf_01",
        "bias": "Gamblers Fallacy",
        "mechanism": "Belief that an independent fire-mission outcome is 'due' to succeed after consecutive misses, rather than treating each round independently, now without the time-pressure alibi",
        "affected_reasoning_operation": "Probabilistic forecasting of an independent event",
        "evidence_source": "Sequence of two prior adjustment-round outcomes plus explicit availability of a 90-minute window",
        "distinctiveness_requirement": "Only bias-relevant instance tied to sequential round outcomes; must not overlap with any other instance's evidence; differs from MD_Biased_4's gf_01 only in the removed time-pressure justification"
      },
      {
        "instance_id": "ig_01",
        "bias": "Ingroup Preference bias or In-group bias",
        "mechanism": "Preferential trust in a report because it originates from the observer's own unit/service rather than on evidentiary merit, now with time available to verify both sources",
        "affected_reasoning_operation": "Comparative weighting of two competing target-location reports",
        "evidence_source": "Battalion JTAC report vs. partner-force liaison report, plus explicit availability of verification time",
        "distinctiveness_requirement": "Only instance involving cross-unit evidence comparison; distinct evidence source and decision point from gf_01; differs from paired scenario only in removed time constraint"
      },
      {
        "instance_id": "ob_01",
        "bias": "Optimism bias",
        "mechanism": "Underweighting risk indicators (tight margin, comms dropout) because of a recent favorable track record with the same asset, now with time available to delay for a comms reset",
        "affected_reasoning_operation": "Forward-looking risk/outcome forecasting for a danger-close CAS run",
        "evidence_source": "Recent squadron strike history plus current margin/comms conditions plus explicit availability of delay time",
        "distinctiveness_requirement": "Only instance concerning forecast confidence about mission execution risk; independent of ig_01 and brn_01 evidence; differs from paired scenario only in removed time constraint"
      },
      {
        "instance_id": "brn_01",
        "bias": "Base-rate neglect",
        "mechanism": "Approving action based on one specific-case cue while ignoring known low prior probability of true positives in this sector/sensor combination, now with time available to seek confirmation",
        "affected_reasoning_operation": "Belief updating on target identification given prior probability and single-case evidence",
        "evidence_source": "Sector activity history and sensor false-positive history vs. single sensor cue, plus explicit availability of confirmation time",
        "distinctiveness_requirement": "Only instance involving prior-probability neglect in target identification; final decision point; differs from paired scenario only in removed time constraint"
      }
    ],
    "paired_scenario_id": "MD_Biased_4",
    "counterfactual_variable": {
      "name": "Duration of the pre-assault time window (time-pressure level)",
      "original_state": "30-minute window before the company crosses the line of departure",
      "changed_state": "90-minute window before the company crosses the line of departure",
      "variables_to_hold_constant": [
        "Ammunition limitations for the 81mm mortar section",
        "Intermittent radio/data-link degradation between FSCC and forward observers",
        "Danger-close proximity of friendly squads to the target compound",
        "Possible civilian presence in the adjacent village",
        "Single organic ISR feed with known false-positive history",
        "Identity and roles of all stakeholders",
        "The four decisions, their alternatives, and their sequence",
        "The mechanisms and strength of all four embedded reasoning patterns"
      ]
    },
    "scenario_id": "MD_Counterfactual_4",
    "domain_id": "MD",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias assigned to a distinct decision point, mirroring the 1:1 decision-point mapping used in MD_Biased_4, selected for mechanism fit and narrative realism per rules 1-4; no decision point hosts more than one instance of any bias; only the time-window variable was altered relative to the paired scenario.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Ammunition limitations for the 81mm mortar section",
      "Intermittent radio/data-link degradation between FSCC and forward observers",
      "Danger-close proximity of friendly squads to the target compound",
      "Possible civilian presence in the adjacent village",
      "Single organic ISR feed with known false-positive history",
      "Identity and roles of all stakeholders",
      "The four decisions, their alternatives, and their sequence",
      "The mechanisms and strength of all four embedded reasoning patterns"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first evaluation of four mission decision episodes described during debrief: mortar adjustment rounds, grid discrepancy resolution, danger-close CAS clearance, and artillery mission approval on an ISR cue."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Base-rate neglect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Expectation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Gambler's fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Ingroup bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Gambler's fallacy",
      "alternative_labels": ["Monte Carlo fallacy", "negative recency bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The belief that a run of independent events makes the opposite outcome more likely because random sequences are expected to balance out.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Mortar adjustment round decision",
      "decision_point_description": "Whether to fire the next adjustment round or order a full re-lay after two short rounds and a single no-fault gun-line check.",
      "affected_reasoning_operation": "Prediction of the next mortar round's point of impact",
      "bias_specific_mechanism": "Negative recency based on the representativeness heuristic: the participant interpreted two consecutive short impacts as a sequence that would self-correct, making a hit feel 'due' without an identified fault or change in physical conditions.",
      "manifestation_in_interview": "The participant fired the third adjustment round rather than using available time for a full re-lay, explicitly stating the prior two shorts made an on-target round feel due.",
      "effect_on_reasoning_or_decision": "The third round was fired without additional verification and also landed short; a subsequent check later found a leveling error.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Fired again. Two shorts in a row, felt like we were due for one on target.",
          "evidence_explanation": "This directly articulates the gambler's fallacy: inferring a future hit was more likely because of the prior streak of shorts."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, if I'm honest. I had plenty of time to stop and have them recheck everything properly. I just didn't feel like it was necessary—the pattern read as random scatter that would correct itself.",
          "evidence_explanation": "Shows the decision was not driven by resource constraints or an identified mechanical fault, but by an erroneous belief that random scatter would self-correct."
        }
      ],
      "correction_or_counterevidence": "The third round also landed short; a later fourth check identified a leveling error. The counterevidence arrived after the biased decision had already affected the firing choice.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved passages did not include gambler's fallacy or related negative recency/representativeness material; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Ingroup bias",
      "alternative_labels": ["source bias", "familiarity heuristic", "channel bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to assign greater credibility or weight to information from one's own group, organization, or familiar source, independent of objective information quality.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Grid discrepancy resolution",
      "decision_point_description": "Choosing whether to act on Grid A from battalion JTAC or cross-check/act on Grid B from the partner-force liaison.",
      "affected_reasoning_operation": "Source credibility assessment and evidence weighting between conflicting grid reports",
      "bias_specific_mechanism": "Familiarity and shared organizational source made the battalion JTAC report feel more reliable without any concrete evidence that its information was better than the partner-force report.",
      "manifestation_in_interview": "The participant selected Grid A despite having time to cross-check Grid B, explicitly attributing the choice to the report's own-channel source and familiar format.",
      "effect_on_reasoning_or_decision": "Grid A was treated as actionable and Grid B was not pursued; follow-on reconnaissance later found indicators at Grid B.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with Grid A. It came through our own FSCC net, format I was used to, source I'd worked with the whole deployment. I did have the time to cross-check Grid B properly—there wasn't really anything stopping me—I just leaned toward our own channel.",
          "evidence_explanation": "The participant describes source familiarity, not information quality, as the reason for choosing Grid A."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably would've given it more credit. Hard to explain exactly why, but hearing it through your own net makes it feel more solid, even without a concrete reason the information itself was better.",
          "evidence_explanation": "This counterfactual acknowledgement isolates the source/channel heuristic and rules out the content as the driver."
        }
      ],
      "correction_or_counterevidence": "Follow-on reconnaissance picked up some indicators at Grid B, but the evidence is not conclusive; the key point is that the weighting occurred before any confirmatory information.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved passages did not contain ingroup bias or source-based credibility bias material; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Expectation bias",
      "alternative_labels": ["overconfidence effect", "complacency", "false sense of normality"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for strong prior expectations about a system or person's performance to shape risk perception and underweight current disconfirming or hazardous cues.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "CAS danger-close clearance decision",
      "decision_point_description": "Whether to clear the CAS run with the tighter danger-close margin as-is, or widen the margin/delay for stable comms.",
      "affected_reasoning_operation": "Risk estimation and risk acceptance for close air support",
      "bias_specific_mechanism": "The squadron's prior clean record generated a strong expectation of another clean run; the participant underweighted current situation-specific risk factors such as tighter friendly positioning and recent comms dropouts.",
      "manifestation_in_interview": "The participant cleared the strike hot with the tighter margin rather than using available time to widen or wait for a stable comms check, explicitly citing the squadron's track record.",
      "effect_on_reasoning_or_decision": "The strike was cleared with a tighter margin; comms dropped again during final attack heading confirmation, producing a closer-than-planned sequence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Cleared it hot with the tighter margin. This squadron had been reliable every time, so I expected the same result.",
          "evidence_explanation": "Shows the decision was driven by an expectation of repeat performance rather than a current risk assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, I'd have wanted the wider margin and a cleaner comms check. The track record with them is what made the tighter margin feel acceptable.",
          "evidence_explanation": "Confirms that the track record, not current mission conditions, lowered the perceived risk."
        }
      ],
      "correction_or_counterevidence": "Comms dropped again for about ten seconds during final attack heading confirmation; the outcome was still safe but the participant acknowledged it was closer than desired and he had time to wait.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor document identifies expectation as a common cognitive bias in aviation incidents, but the fragment does not provide a full operational definition.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation",
          "mechanism_supported_by_source": "The retrieved source identifies expectation as one of the common cognitive biases in aviation incident reports, though the excerpt provides label-level support rather than a detailed mechanism definition.",
          "relevance_to_this_occurrence": "Supports the label 'Expectation bias' for the participant's reliance on prior squadron reliability to expect a safe result despite current tighter margins and comms dropouts."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Base-rate neglect",
      "alternative_labels": ["base-rate fallacy", "prior probability neglect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to underweight or ignore base-rate or historical frequency information when making probabilistic or diagnostic judgments about a specific case.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Artillery mission on compound (single ISR cue)",
      "decision_point_description": "Whether to obtain a second source to confirm the ISR cue or approve the 155 mission on the single cue.",
      "affected_reasoning_operation": "Diagnostic/probabilistic evaluation of the ISR cue's validity",
      "bias_specific_mechanism": "The participant explicitly recognized the low prior probability of enemy activity in the sector and the sensor's high false-hit history, but reported focusing on the single cue itself rather than the base-rate information.",
      "manifestation_in_interview": "Approved the mission off a single cue despite acknowledging the quiet sector and false-hit-prone sensor.",
      "effect_on_reasoning_or_decision": "Artillery was committed to the compound without a second source; post-strike assessment was mixed and inconclusive.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That sector had been quiet the whole deployment, mostly normal village pattern-of-life, and that sensor had a track record of throwing false hits in that terrain.",
          "evidence_explanation": "Participant possessed and could articulate relevant base-rate information that should have reduced confidence in the cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably would've felt about the same either way—I was focused on the cue itself more than the sector's overall track record.",
          "evidence_explanation": "This directly states the core base-rate neglect mechanism: the case-specific cue dominated the base-rate and historical track record."
        }
      ],
      "correction_or_counterevidence": "Post-strike assessment was mixed, with some indicators of prior enemy presence but also signs the compound may have been unoccupied by then; the outcome does not negate the base-rate neglect at the time of assessment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved passages did not include base-rate neglect or base-rate fallacy material; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["confirmatory information processing", "selective information processing"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information that confirms one's preexisting beliefs or operational expectations while underweighting disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Artillery mission on compound (single ISR cue)",
      "decision_point_description": "Whether to obtain a second source to confirm the ISR cue or approve the 155 mission on the single cue.",
      "affected_reasoning_operation": "Evaluation of a hypothesis-consistent intelligence cue",
      "bias_specific_mechanism": "The participant treated the ISR cue as sufficient because it matched the operational search objective rather than evaluating its reliability or seeking disconfirmation.",
      "manifestation_in_interview": "Approved the artillery mission on a single 'possible enemy activity' cue, explicitly citing the match with the objective.",
      "effect_on_reasoning_or_decision": "The mission was approved without a second source; post-strike assessment was inconclusive.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I approved it off the single cue. It matched what we were looking for, so I went with it.",
          "evidence_explanation": "The phrase 'matched what we were looking for' demonstrates confirmatory evidence processing: hypothesis fit, not corroboration, drove the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Get a second source to confirm, since the area had been so quiet, or approve the mission off the one cue. We genuinely had time for the first option that day.",
          "evidence_explanation": "Indicates a disconfirming/corroborating option was available and feasible, making the confirmatory shortcut more clearly a bias rather than a constraint."
        }
      ],
      "correction_or_counterevidence": "Post-strike assessment was mixed and inconclusive; the decision was made before that information was available.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved O'Connor document identifies confirmation as a common cognitive bias in aviation incidents, though the fragment does not provide a detailed definition.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation",
          "mechanism_supported_by_source": "The retrieved source identifies confirmation as one of the common cognitive biases in aviation incident reports, though the excerpt provides label-level support rather than a detailed mechanism definition.",
          "relevance_to_this_occurrence": "Supports the label 'Confirmation bias' for the participant's acceptance of a single ISR cue because it matched the search objective."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus passages are fragmentary; some classifications rely on established cognitive-science knowledge where corpus support was unavailable.",
    "The analysis uses a single self-reported debrief transcript without independent outcome data or direct observation of the original decisions.",
    "Some decisions occurred under military operational context and may include professional heuristics that are not fully separable from bias based solely on transcript evidence."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Counterfactual_4_Gemini_on",
  "interview_id": "MD_Counterfactual_4",
  "system_prompt_id": "Gemini",
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
