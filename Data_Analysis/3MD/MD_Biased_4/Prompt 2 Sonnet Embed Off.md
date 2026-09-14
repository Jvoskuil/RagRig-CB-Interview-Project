You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. Just to confirm, this is a voluntary cognitive task analysis debrief—we're reconstructing your decision-making during a specific fire support mission, not evaluating performance for any board or investigation. You can decline any question. Comfortable proceeding?

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Great. Can you describe your role and the mission?

Participant: I was the FSO attached to the company during a daylight clearing operation. We had an enemy 82mm mortar team that had been harassing our forward positions for about two days, and intel flagged a possible staging compound near a village on the objective's north edge. My job was coordinating mortars, then CAS, then artillery, to clear both threats before the company crossed the line of departure. Objective was straightforward—suppress the mortar team, clear the compound, keep it clean for friendlies and the village.

Interviewer: What made this mission nonroutine?

Participant: Timeline was tight—we had about thirty minutes before the assault window closed, ammo for the 81s was limited since we'd already used a chunk of it earlier that morning, and comms between me and FSCC kept dropping in and out. Plus the compound was close enough to friendly squads that anything there was going to be danger-close. And the only real-time picture we had on the compound was one ISR feed, no second source.

Interviewer: Walk me through the sequence as it happened.

Participant: First mission was against the mortar position with the 81s. Fired an adjustment round, it landed short. Fired a second one, still short. Section chief checked the gun-line data once, said no fault found. Around that time, I also had two conflicting reports on where the staging activity actually was—our battalion JTAC had one grid, and the partner-force liaison next to us had a grid about three hundred meters off. Then CAS checked in for the compound piece, and finally we had that ISR cue on the compound itself right before the artillery mission.

Interviewer: Let's take these one at a time. Start with the mortar adjustment rounds.

Participant: Right, so two rounds down, both short. Section chief ran through the data once and didn't find anything wrong. At that point I had a decision—stop and have them do a full re-lay, checking level, deflection, everything from scratch, or fire the next adjustment round and see what happens.

Interviewer: What did you decide, and why?

Participant: I told them to fire again. Two shorts in a row, statistically we were about due to get one on target, and a full re-lay eats time we didn't have with the window closing.

Interviewer: What did that third round do?

Participant: Also landed short. Turned out later there was a leveling error on the gun that had nothing to do with the first two rounds—separate issue entirely. We caught it on the fourth check.

Interviewer: If the section chief had reported a confirmed fault after the first miss, would your third-round call have gone differently?

Participant: Probably, yeah. If there'd been a flagged fault I'd have stopped immediately for the recheck. Without one, I read the pattern as random scatter that would sort itself out on its own.

Interviewer: Let's move to the grid discrepancy. What information did you have?

Participant: Battalion JTAC—same battalion as me—called in Grid A for the staging activity. Almost at the same time, the partner-force liaison on our flank called Grid B, about three hundred meters away, similar confidence level in both reports, nothing that clearly outranked the other on paper.

Interviewer: How did you resolve that?

Participant: I went with Grid A, the JTAC's grid. It came through our own FSCC net, format I was used to, and honestly it's the source I'd worked with the whole deployment. The partner-force report came through a different relay and took longer to cross-check.

Interviewer: Did you request verification on Grid B?

Participant: Not before we acted on Grid A. Follow-on recon actually picked up some indicators near Grid B too, so it wasn't nothing—we just didn't chase it down at the time.

Interviewer: If the partner-force liaison's report had come through your own channel instead, do you think you'd have weighted it the same as Grid A?

Participant: Honestly, probably would've given it more credit. There's something about hearing it through your own net that makes it feel more solid, even if I can't point to a real reason the information itself was better.

Interviewer: Let's talk about the CAS run. What was the situation?

Participant: Pilot was on station, ready for a danger-close run supporting the compound clearance. We'd run several strikes with this same squadron over the deployment, all clean, standard margins, no issues. This time the friendly squad's position put us tighter than our usual margin, and we'd had a couple of comms dropouts with the lead squad in the minutes before.

Interviewer: What were your options?

Participant: Widen the margin, which meant delaying and possibly missing the window, or hold the comms until we got a stable check, versus just clearing it with the tighter margin we had.

Interviewer: What did you choose?

Participant: I cleared it hot with the tighter margin. This squadron had been reliable every time, so I expected it to go the same way.

Interviewer: What happened with comms during the final attack heading confirmation?

Participant: Dropped out again for about ten seconds. We got it back before the pilot needed the final call, so it worked out, but it was closer than I'd like on reflection.

Interviewer: If this had been the squadron's first-ever danger-close run with you, would you have set the same margin?

Participant: No. I'd have wanted the wider margin and a cleaner comms check. The history with them is what made the tighter margin feel acceptable.

Interviewer: Last decision point—the artillery mission on the compound.

Participant: Right before we committed the 155s, the ISR feed flagged one cue, "possible enemy activity" at the compound. That sector had been quiet the whole deployment, mostly normal village pattern-of-life, and that particular sensor had a track record of throwing false hits in that terrain.

Interviewer: What were the alternatives?

Participant: Get a second source to confirm before firing, given how quiet that area had been, or approve the mission off the one cue since the window was closing.

Interviewer: What did you decide?

Participant: I approved it off the single cue. We were inside the last few minutes before the assault, and the cue matched what we were looking for, so I went with it.

Interviewer: What did the post-strike assessment show?

Participant: Mixed. Some indicators of prior enemy presence, but also signs it might've been unoccupied by the time we fired. Inconclusive, honestly.

Interviewer: If the sector had a recent history of confirmed enemy activity, would that one cue have been enough on its own?

Participant: Probably would've felt the same either way at the time—I was focused on the cue itself, not really running the sector's track record against it.

Interviewer: Looking back across all four decisions, where do you think time pressure affected you most?

Participant: Probably the mortar rounds and the compound call—those felt the most rushed. The grid call and the CAS run felt more like judgment calls based on what I knew about the sources and the squadron.

Interviewer: Anything you'd do differently?

Participant: Maybe push harder for that re-lay check early, and get a second look at the compound cue. But given the clock we were working against, I think most FSOs would've made similar calls that day.

Interviewer: That's helpful. Thanks for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Biased_4",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Fire Support Officer (FSO) / Joint Fires Observer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Danger-Close: Fire Support Coordination During a Company Clearing Operation",
    "scenario_summary_internal": "An FSO/JFO attached to an infantry company during a daylight clearing operation must coordinate mortar, CAS, and artillery fires against an enemy mortar team and a suspected staging compound near a populated area. Ammunition, time before the assault window closes, degraded comms, and proximity to friendly troops and civilians force four sequential fire-support decisions under pressure.",
    "occupational_realism": {
      "objective": "Suppress/destroy an enemy 82mm mortar team harassing the company's forward positions and clear a suspected staging compound before the assault window closes, without fratricide or civilian casualties.",
      "setting": "Daylight combined-arms clearing operation; company commander and FSO co-located at a forward command post; battalion Fire Support Coordination Center (FSCC), a CAS aircraft on station, and an adjacent partner-force unit all in the fires network.",
      "constraints": [
        "Limited 81mm mortar ammunition remaining for adjustment rounds",
        "30-minute window before the company must cross the line of departure",
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
          "Time remaining before assault window is closing"
        ],
        "new_information_after_decision": [
          "Third round result (on or off target) is learned only after firing",
          "A later data check reveals a leveling error unrelated to prior rounds"
        ],
        "alternatives": [
          "Order a full re-lay and data recheck of the gun line before firing again",
          "Fire the next adjustment round immediately, expecting the miss streak to end"
        ],
        "intended_action": "FSO authorizes firing another adjustment round without a full re-lay, reasoning that after two misses a hit is 'due'."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Battalion JTAC (same service) reports the enemy staging point at Grid A",
          "Adjacent partner-force liaison independently reports enemy activity at Grid B, roughly 300m away",
          "Both reports carry similar confidence caveats"
        ],
        "new_information_after_decision": [
          "Follow-on reconnaissance shows some indicators near Grid B as well as Grid A"
        ],
        "alternatives": [
          "Request cross-verification of both grids before committing fires",
          "Prioritize the battalion JTAC's grid because it comes through the FSO's own chain"
        ],
        "intended_action": "FSO weights the battalion JTAC's coordinate more heavily than the partner-force report largely because it originates from his own unit's channel."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "CAS pilot is ready for a danger-close run near friendly positions",
          "The last several CAS strikes with this squadron were executed cleanly with standard margins",
          "Current friendly-troop proximity is tighter than the squadron's usual margin, and communications with the lead squad have had brief dropouts"
        ],
        "new_information_after_decision": [
          "Communications with the lead squad drop out again during the final attack heading confirmation"
        ],
        "alternatives": [
          "Widen the safety margin or delay the run pending a stable communications check",
          "Proceed with the tighter margin, expecting it to go as smoothly as the recent strikes"
        ],
        "intended_action": "FSO clears the CAS run with the tight margin, expecting the outcome to match the string of recent successful strikes."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The sole ISR sensor flags a single 'possible enemy activity' cue at the suspected compound",
          "The sector has historically been quiet with routine civilian pattern-of-life",
          "The specific sensor type has a known history of false positives in this terrain"
        ],
        "new_information_after_decision": [
          "Post-strike assessment of what was actually present at the compound"
        ],
        "alternatives": [
          "Request a second confirming source given the sector's normally low enemy-activity rate",
          "Approve the artillery mission on the single sensor cue alone"
        ],
        "intended_action": "FSO approves the fire mission based on the one sensor cue, without factoring in how rarely this sector produces genuine enemy activity or how often this sensor errs."
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
        "What cues made you decide to fire again without a full re-lay?",
        "How did you weigh the battalion JTAC's grid against the partner-force liaison's grid?",
        "What made you comfortable clearing the CAS run with a tighter margin than usual?",
        "How did the sector's history factor into your decision to approve the artillery mission on one sensor cue?",
        "What information sources did you rely on most at each point, and why?",
        "How much time pressure did you feel at each decision, and how did it affect your process?",
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
        "mechanism": "Treating independent artillery/mortar rounds as part of a self-correcting streak, expecting a hit because prior rounds missed",
        "affected_reasoning_operation": "Probabilistic inference about an upcoming independent event",
        "evidence_available_at_time": [
          "Two prior adjustment rounds landed short",
          "No confirmed fault yet identified in the gun line"
        ],
        "required_textual_manifestation": "FSO explicitly reasons that because the last two rounds missed, the next one is likely to hit, rather than ordering a data recheck",
        "plausible_nonbias_interpretation": "Time pressure before the assault window justified skipping a re-lay check as an acceptable risk trade-off",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "streak", "independent probability"]
      },
      {
        "instance_id": "ig_01",
        "bias": "Ingroup Preference bias or In-group bias",
        "decision_point": 2,
        "mechanism": "Discounting an equally credible report because it originates from an outside unit rather than the FSO's own chain",
        "affected_reasoning_operation": "Weighting and integration of two competing evidence sources",
        "evidence_available_at_time": [
          "Battalion JTAC (same service/unit) reports Grid A",
          "Partner-force liaison reports Grid B with similar confidence caveats"
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
        "mechanism": "Underestimating the risk of a tighter-than-usual danger-close margin because recent strikes with the same squadron succeeded",
        "affected_reasoning_operation": "Risk assessment and forecasting of mission outcome",
        "evidence_available_at_time": [
          "Recent history of clean CAS strikes with this squadron",
          "Current margin tighter than normal and comms dropouts with lead squad"
        ],
        "required_textual_manifestation": "FSO expresses confidence the run would go fine like the recent strikes, despite the tighter margin and comms issue",
        "plausible_nonbias_interpretation": "The squadron's demonstrated proficiency was a legitimate factor supporting a calculated risk decision",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "unrealistic confidence", "overestimate success odds"]
      },
      {
        "instance_id": "brn_01",
        "bias": "Base-rate neglect",
        "decision_point": 4,
        "mechanism": "Approving fires on a single sensor cue while ignoring the sector's low historical enemy-activity rate and the sensor's known false-positive rate",
        "affected_reasoning_operation": "Updating a target-identification judgment given prior probability and current evidence",
        "evidence_available_at_time": [
          "Single 'possible enemy activity' sensor cue",
          "Sector's historically low/quiet enemy-activity pattern",
          "Sensor's known history of false positives in this terrain"
        ],
        "required_textual_manifestation": "FSO approves the mission based mainly on the cue without weighing how rarely this sector or sensor type produces genuine hits",
        "plausible_nonbias_interpretation": "Time pressure before the assault window made a single strong cue an acceptable basis for action given mission urgency",
        "strength": "subtle",
        "do_not_make_explicit": ["base rate", "prior probability", "false positive rate"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control requested."
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
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Each of the four manifest biases is embedded exactly once, at a distinct decision point.",
      "No bias labels, definitions, or psychological terminology appear in probes or narrative.",
      "Each instance has an available plausible non-bias explanation to avoid mechanical proof of bias.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points, probe coverage, and chronological narrative without repetitive exposition.",
      "Consequences described (round results, strike outcomes, post-strike assessment) do not confirm or deny bias presence mechanically."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Gamblers Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must involve reasoning about an upcoming independent artillery/mortar round based on prior round outcomes"
      },
      {
        "bias": "Ingroup Preference bias or In-group bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve differential weighting of two evidence sources based on unit affiliation rather than evidentiary quality"
      },
      {
        "bias": "Optimism bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve underestimating risk of a specific mission element based on a recent favorable track record"
      },
      {
        "bias": "Base-rate neglect",
        "occurrences": 1,
        "mechanism_constraint": "Must involve disregarding sector-level or sensor-level prior probability in favor of a single specific cue"
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
        "mechanism": "Belief that an independent fire-mission outcome is 'due' to succeed after consecutive misses, rather than treating each round independently",
        "affected_reasoning_operation": "Probabilistic forecasting of an independent event",
        "evidence_source": "Sequence of two prior adjustment-round outcomes",
        "distinctiveness_requirement": "Only bias-relevant instance tied to sequential round outcomes; must not overlap with any other instance's evidence"
      },
      {
        "instance_id": "ig_01",
        "bias": "Ingroup Preference bias or In-group bias",
        "mechanism": "Preferential trust in a report because it originates from the observer's own unit/service rather than on evidentiary merit",
        "affected_reasoning_operation": "Comparative weighting of two competing target-location reports",
        "evidence_source": "Battalion JTAC report vs. partner-force liaison report",
        "distinctiveness_requirement": "Only instance involving cross-unit evidence comparison; distinct evidence source and decision point from gf_01"
      },
      {
        "instance_id": "ob_01",
        "bias": "Optimism bias",
        "mechanism": "Underweighting risk indicators (tight margin, comms dropout) because of a recent favorable track record with the same asset",
        "affected_reasoning_operation": "Forward-looking risk/outcome forecasting for a danger-close CAS run",
        "evidence_source": "Recent squadron strike history plus current margin/comms conditions",
        "distinctiveness_requirement": "Only instance concerning forecast confidence about mission execution risk; independent of ig_01 and brn_01 evidence"
      },
      {
        "instance_id": "brn_01",
        "bias": "Base-rate neglect",
        "mechanism": "Approving action based on one specific-case cue while ignoring known low prior probability of true positives in this sector/sensor combination",
        "affected_reasoning_operation": "Belief updating on target identification given prior probability and single-case evidence",
        "evidence_source": "Sector activity history and sensor false-positive history vs. single sensor cue",
        "distinctiveness_requirement": "Only instance involving prior-probability neglect in target identification; final decision point"
      }
    ],
    "intended_strength": [
      { "instance_id": "gf_01", "bias": "Gamblers Fallacy", "strength": "subtle" },
      { "instance_id": "ig_01", "bias": "Ingroup Preference bias or In-group bias", "strength": "subtle" },
      { "instance_id": "ob_01", "bias": "Optimism bias", "strength": "subtle" },
      { "instance_id": "brn_01", "bias": "Base-rate neglect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Biased_4",
    "domain_id": "MD",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism per rules 1-4; no decision point hosts more than one instance of any bias.",
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
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Mortar adjustment decision: 'Two shorts in a row, statistically we were about due to get one on target...' through '...random scatter that would sort itself out on its own.'",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gf_01"
        ],
        "ground_truth_rationale": "The participant expects the next independent round to succeed because the prior two rounds missed."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Grid discrepancy decision: 'I went with Grid A...' through '...makes it feel more solid, even if I can't point to a real reason the information itself was better.'",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ig_01"
        ],
        "ground_truth_rationale": "The participant preferentially weights the own-unit channel despite similar report quality."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "CAS decision: 'I cleared it hot with the tighter margin...' through '...The history with them is what made the tighter margin feel acceptable.'",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ob_01"
        ],
        "ground_truth_rationale": "Recent successful strikes with the squadron reduce perceived risk despite tighter margins and communication dropouts."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Artillery decision: 'I approved it off the single cue...' through '...I was focused on the cue itself, not really running the sector's track record against it.'",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "brn_01"
        ],
        "ground_truth_rationale": "The participant acts on one cue while disregarding the quiet sector history and known sensor false-positive history."
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
    "analysis_scope_note": "Strictly transcript-grounded classification; no retrieved corpus passages were supplied, so occurrence labels rely on established cognitive-science knowledge with disclosure."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "base-rate neglect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "gambler's fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "in-group bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "gambler's fallacy",
      "alternative_labels": ["negative recency bias", "Monte Carlo fallacy"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to believe that a departure from the long-run average will be corrected in the short run, so a repeated outcome makes the opposite outcome more likely.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Mortar adjustment round decision after two short impacts",
      "decision_point_description": "Whether to fire the next adjustment round or order a full re-lay/check after two short rounds and no reported gun-line fault.",
      "affected_reasoning_operation": "Probabilistic inference about artillery adjustment round accuracy",
      "bias_specific_mechanism": "Negative recency/self-correcting scatter belief: after two short rounds, the participant treated the next round as more likely to land on target because the pattern of misses seemed due to end.",
      "manifestation_in_interview": "After two short mortar rounds and a gun-line check with no fault found, the participant decided to fire again, explicitly saying the next round was statistically due to land on target.",
      "effect_on_reasoning_or_decision": "The third round was fired without a full re-lay or complete gun check; it also landed short, and a later check found a separate leveling error.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Two shorts in a row, statistically we were about due to get one on target, and a full re-lay eats time we didn't have with the window closing.",
          "evidence_explanation": "This directly states the gambler's fallacy mechanism: previous short rounds are treated as making a hit more likely, independent of any corrective action."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without one, I read the pattern as random scatter that would sort itself out on its own.",
          "evidence_explanation": "This further demonstrates the erroneous inference that the pattern of misses would self-correct without a mechanical intervention."
        }
      ],
      "correction_or_counterevidence": "The section chief checked the gun-line data once and found no fault; the participant said he would have stopped if a fault had been flagged. The eventual leveling error was discovered later, after the biased third-round decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was provided in the RAG context; this label is supplied from established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "in-group bias",
      "alternative_labels": ["ingroup favoritism", "source bias", "familiarity bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Favoring or assigning greater credibility to members of one's own group or familiar organizational channel over outgroup or external sources, independent of information quality.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Conflicting grid discrepancy resolution",
      "decision_point_description": "How to resolve conflicting staging-activity grids from the battalion JTAC and the partner-force liaison.",
      "affected_reasoning_operation": "Source credibility and information weighting",
      "bias_specific_mechanism": "Familiarity/own-group source elevation: the participant used channel familiarity and shared organizational identity as a proxy for trustworthiness, weighting the JTAC report more heavily despite similar confidence levels.",
      "manifestation_in_interview": "Faced with two equally credible reports, the participant selected Grid A because it came through his own FSCC net and from a source he had worked with throughout the deployment, rather than because of better informational content.",
      "effect_on_reasoning_or_decision": "Action was taken on Grid A while Grid B was not chased down at the time; follow-on reconnaissance later found indicators near Grid B.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with Grid A, the JTAC's grid. It came through our own FSCC net, format I was used to, and honestly it's the source I'd worked with the whole deployment.",
          "evidence_explanation": "The selection is explicitly based on the source's organizational channel and familiarity, not on the underlying information quality."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There's something about hearing it through your own net that makes it feel more solid, even if I can't point to a real reason the information itself was better.",
          "evidence_explanation": "The participant acknowledges that the feeling of credibility came from the channel rather than from the report's actual reliability, which is the mechanism of in-group/source bias."
        }
      ],
      "correction_or_counterevidence": "Follow-on recon later found indicators near Grid B, but this occurred after the decision to act on Grid A. The participant also recognized in the counterfactual that the partner-force report would have received more weight if it had arrived through his own channel.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was provided in the RAG context; this label is supplied from established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["overconfidence effect", "optimism bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood or risk of an event based on the ease with which relevant past examples come to mind, rather than on all current relevant information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Danger-close CAS clearance margin decision",
      "decision_point_description": "Whether to clear the CAS run hot with the current tight danger-close margin, widen the margin, or wait for a stable comms check.",
      "affected_reasoning_operation": "Risk assessment for close air support clearance",
      "bias_specific_mechanism": "Availability-driven risk estimate: several past clean runs with the same squadron were overused as evidence that the current tighter-margin run would also be safe, even though current risk factors differed.",
      "manifestation_in_interview": "The participant cleared the CAS run with the tighter margin because the squadron's prior clean history made the current increased risk feel acceptable; he said he would not have done so if it had been the squadron's first danger-close run with him.",
      "effect_on_reasoning_or_decision": "CAS was cleared hot with a tighter margin, and the final attack heading confirmation comms dropped out again for about ten seconds before recovering.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd run several strikes with this same squadron over the deployment, all clean, standard margins, no issues.",
          "evidence_explanation": "The participant uses a recall of prior clean outcomes as a risk-relevant sample, increasing the salience and ease of the clean-history heuristic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I cleared it hot with the tighter margin. This squadron had been reliable every time, so I expected it to go the same way.",
          "evidence_explanation": "The expectation that the current run would go the same way is based on available past outcomes rather than the current tighter margin and known comms problems."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The history with them is what made the tighter margin feel acceptable.",
          "evidence_explanation": "This isolates the role of availability of past clean runs in lowering perceived current risk."
        }
      ],
      "correction_or_counterevidence": "The participant reflected that comms dropped out again during the final confirmation and said it was closer than he would like, but no pre-decision correction occurred. A rational use of squadron reliability history is a plausible alternative explanation, so confidence is moderate.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was provided in the RAG context; this label is supplied from established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "base-rate neglect",
      "alternative_labels": ["base rate fallacy", "base-rate underweighting"],
      "taxonomy_status": "established_label",
      "bias_definition": "Evaluating a specific case by focusing on individuating information while ignoring or underweighting prior probabilities or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Artillery fire mission approval on compound cue",
      "decision_point_description": "Whether to approve the 155-mission on the single ISR cue or get a second source before firing.",
      "affected_reasoning_operation": "Decision to fire based on an ambiguous ISR cue",
      "bias_specific_mechanism": "Base-rate neglect: the participant had known prior probabilities indicating the cue was likely to be a false hit, but proceeded on the specific cue without integrating those base rates.",
      "manifestation_in_interview": "Despite knowing the sector had been quiet and the sensor had false-hit history in that terrain, the participant approved the artillery mission on one cue because the cue matched the target they were looking for.",
      "effect_on_reasoning_or_decision": "The artillery mission was approved on a single ambiguous cue; post-strike assessment was inconclusive about whether the compound was occupied at the time of the strike.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That sector had been quiet the whole deployment, mostly normal village pattern-of-life, and that particular sensor had a track record of throwing false hits in that terrain.",
          "evidence_explanation": "The participant identifies a low prior probability of enemy activity and the sensor's false-positive history, which should have lowered confidence in the single cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I approved it off the single cue. We were inside the last few minutes before the assault, and the cue matched what we were looking for, so I went with it.",
          "evidence_explanation": "The decision was made on the specific cue without a second source, showing that the individuating cue outweighed the known base rate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably would've felt the same either way at the time—I was focused on the cue itself, not really running the sector's track record against it.",
          "evidence_explanation": "This explicitly states that the sector's prior pattern was not integrated into the judgment, which is the core mechanism of base-rate neglect."
        }
      ],
      "correction_or_counterevidence": "Post-strike assessment was inconclusive, so the outcome does not confirm the decision was correct or incorrect. Time pressure was present, but the participant stated he would have focused on the cue itself regardless of the sector's history.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was provided in the RAG context; this label is supplied from established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided, so corpus-grounded support could not be checked; named labels are disclosed as general cognitive-science knowledge."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Biased_4_Sonnet_off",
  "interview_id": "MD_Biased_4",
  "system_prompt_id": "Sonnet",
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
