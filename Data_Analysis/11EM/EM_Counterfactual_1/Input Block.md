<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm — you're okay with us discussing this incident in detail for training-development purposes, and we can pause anytime?

Participant: Yes, that's fine. Happy to go through it.

Interviewer: Can you tell me your role and what you were supposed to be doing that day?

Participant: I'm a Training Officer with the county EM office. That day I was controlling a full-scale exercise — a shelter-in-place and evacuation drill at our EOC and one of our public shelters. My job was running injects and evaluating the shelter and liaison teams.

Interviewer: What actually happened?

Participant: About ninety minutes in, we got a scripted comms-disruption inject. Almost right after, a real weather alert came through — a fast-moving winter storm, faster than what we'd built the drill around. A couple of field reports came in that I couldn't immediately place as scripted or real. So I paused the exercise and checked actual weather data before doing anything else. That confirmed it — a real tower failure, and roads closing faster than forecast.

Interviewer: What led you to stop and verify rather than continue running the drill?

Participant: The timing didn't fit our script, and the reports didn't match the inject list. I've run enough of these to recognize when something's off-script, and I didn't want to keep feeding scenario content into what might already be real.

Interviewer: What happened next?

Participant: Shortly after, two liaison officers arrived for the scheduled shift handoff at the shelter. Neither had worked that specific site before. This time, though, I actually had a bit of breathing room — maybe twenty-five minutes before I needed to turn to the transportation side, since the bus situation hadn't come up yet. So I sat with them, gave them the rundown — told them to run the usual Zone C protocol, muster at the standard point, same as always — and then went to check on road conditions.

Interviewer: What happened after that handoff?

Participant: About forty minutes later, during a headcount, we found a group had been sent to the old west muster point — we'd relocated that about a year ago. Separately, a volunteer coordinator asked me directly what "Zone C protocol" even referred to. So the same kind of mix-up happened, even though I'd had more time with them than I usually get in situations like this.

Interviewer: Let's go through this step by step. First, the decision to pause the exercise — what did you actually have in front of you at that moment?

Participant: The scripted inject text, the live weather alert, and two ambiguous field reports. No confirmation yet of a real failure — that came after.

Interviewer: What alternatives did you weigh?

Participant: Keep running the drill and treat it as scripted, or stop and verify against real data. I verified. Worst case, I lose a few minutes of drill time; best case, I catch a real problem early.

Interviewer: Now the liaison handoff. You said you had more time than usual there. What did you know about these two officers going in?

Participant: I knew they were new to this shelter specifically. I didn't ask about their broader background — I assumed liaison officers generally pick up our zone conventions fast, since it's not unusual across our sites.

Interviewer: You had roughly twenty-five minutes and no immediate competing task. What did you do with that time?

Participant: Some of it went to double-checking the transportation numbers with the section chief, even though I didn't strictly need to yet. With the liaisons, I gave them the same rundown I always give — "usual Zone C protocol," "standard muster point." I didn't really stretch it out into something longer.

Interviewer: Given that you weren't rushed, what made you choose the short version anyway?

Participant: Honestly, it didn't occur to me that it needed to be longer. Those terms are just how I refer to things day to day — they don't register as shorthand to me, they register as the actual names. Having the extra time didn't change how I framed it, because I wasn't treating it as an abbreviated version of anything.

Interviewer: Did you check what they already knew before briefing them?

Participant: No. I could have asked directly — "have you worked this layout before, do you know where the current muster point is" — and I had time to do that. I just didn't think to.

Interviewer: What would have changed your approach there?

Participant: If either of them had flagged that they were unfamiliar, I'd have walked them through it properly. Neither volunteered that, and I didn't ask.

Interviewer: Let's move to the transportation decision. What was the situation?

Participant: Two buses, three sites requesting transport, and the section chief flagged fuel and driver-hour limits. One sector's roads were closing faster than the others per the county updates.

Interviewer: What options did you consider?

Participant: Split the buses evenly across all three, or prioritize the fastest-closing sector first. I prioritized that sector.

Interviewer: Why that option?

Participant: Splitting evenly felt fair on paper, but it risked stranding people at the site about to become unreachable. Prioritizing by closure risk meant a longer wait elsewhere, but nobody got cut off entirely.

Interviewer: How did that play out?

Participant: The prioritized site cleared in time. One other site had a longer wait — inconvenient, but they got transport once the first run finished, no injuries.

Interviewer: Last decision point — handing off to the Incident Commander. What was competing for your attention?

Participant: The IC arrived to take over the real incident, the exercise evaluators still expected a formal debrief, and parts of the shelter were still running on the arrangement from the earlier handoff.

Interviewer: What did you consider doing?

Participant: Run the debrief and real command informally in parallel, or fully suspend the exercise and do a proper handoff. I suspended it and gave the IC a written status briefing instead of just talking him through it.

Interviewer: Why written, given you had some time pressure again at that point?

Participant: Verbal is faster, but I've seen details get lost that way, especially with comms already degraded. Writing it down gave him something to check against rather than relying on what he remembered hearing.

Interviewer: Did the earlier muster-point mix-up influence that choice?

Participant: A bit, in hindsight. I think I was more deliberate about not leaving room for gaps after seeing what happened with the liaison briefing.

Interviewer: Given that you actually had time available during that briefing, what do you think would have changed if you'd used it differently — say, walking through the zone map from scratch?

Participant: Probably would have caught the muster point issue immediately. It wasn't that I didn't have the minutes for it. I just didn't reframe the conversation as something that needed more than the usual rundown.

Interviewer: If the storm had hit an hour later, would your resource decisions have changed?

Participant: The bus prioritization logic would hold regardless. It might have given me even more slack before the transportation piece, but based on what happened here, I'm not sure that alone would've changed how I briefed the liaisons.

Interviewer: What would you tell a less experienced officer in a similar spot?

Participant: Don't assume the title comes with the knowledge. It's tempting to think "liaison officer" means someone already knows your terms, but that depends entirely on which site they've actually worked. Time isn't always the reason things get skipped — sometimes you just don't think to check.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Counterfactual_1",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Emergency Management Training Officer",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Exercise-to-Real Transition During Winter Storm Shelter Handoff (Time-Pressure Isolated Variant)",
    "scenario_summary_internal": "This is a counterfactual variant of EM_Biased_1. The same Training Officer manages the same exercise-to-real transition, the same storm, and the same newly rotated liaison officers, but the single causal variable that is changed is the amount of time available before the shift-handoff briefing: instead of roughly ten minutes under acute time pressure, the officer has about twenty-five minutes with no immediate competing task. All other material facts, including the storm timeline, staffing, transportation constraints, and the fourth decision point, are held constant. The officer still gives the abbreviated, shorthand handoff briefing assuming the new liaison officers share the same background familiarity with shelter zone and muster-point terminology, and the same downstream misdirection occurs. This isolates the assumption-of-shared-knowledge mechanism from the alternative explanation that the shorthand briefing was purely a time-constrained economization (Curse of Knowledge).",
    "occupational_realism": {
      "objective": "Maintain safe, coordinated shelter operations and evacuation transport during an unplanned transition from a training exercise to a real weather emergency, while handing off command smoothly to an incoming Incident Commander.",
      "setting": "County Emergency Operations Center (EOC) and an affiliated public shelter, during a scheduled full-scale training exercise that is overtaken by an actual severe winter storm causing communications outages and road closures.",
      "constraints": [
        "Primary radio and phone lines degraded by storm damage",
        "Newly rotated shelter liaison staff and volunteer coordinators unfamiliar with facility-specific procedures",
        "Limited transport assets shared between exercise injects and real evacuee movement",
        "Hard deadline before roads become impassable",
        "Ambiguity about which reports are scripted exercise injects versus real conditions",
        "Unlike the paired base scenario, the officer has approximately twenty-five minutes available before the next competing task, rather than roughly ten"
      ],
      "stakeholders": [
        "Emergency Management Training Officer (protagonist)",
        "Newly rotated shelter liaison officers",
        "Volunteer shelter coordinators",
        "Transportation/logistics section chief",
        "Incoming on-call Incident Commander",
        "Exercise evaluators/controllers"
      ],
      "technical_terms_to_use": [
        "shelter-in-place",
        "muster point",
        "liaison officer",
        "incident action plan",
        "shift handoff",
        "transportation section",
        "unified command"
      ],
      "technical_terms_to_avoid": [
        "highly specialized ICS position titles beyond liaison/section chief",
        "hazmat-specific technical jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Scripted exercise inject reports a minor comms disruption",
          "Actual weather service warning shows a fast-moving winter storm approaching",
          "Some field reports arriving are unclear whether they are scripted or real"
        ],
        "new_information_after_decision": [
          "Confirmation that a real communications tower failure has occurred, distinct from any scripted inject",
          "Reports that some roads are already closing faster than forecast"
        ],
        "alternatives": [
          "Continue the exercise as scripted and treat the comms report as an inject",
          "Pause the exercise to verify against real weather data before proceeding"
        ],
        "intended_action": "Training Officer decides to pause the exercise and verify conditions against real-time weather reporting before continuing."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two newly rotated liaison officers have just arrived to relieve the exercise-shift shelter team",
          "The shelter has an internal zone and muster-point system the Training Officer has used for years",
          "Unlike the base scenario, no immediate competing task is pending; the officer has roughly twenty-five minutes before needing to turn to transportation matters"
        ],
        "new_information_after_decision": [
          "The new liaison officers later misdirect evacuees to the wrong muster point during a subsequent headcount, despite the extra briefing time",
          "A volunteer coordinator asks what 'Zone C protocol' means partway through the shift"
        ],
        "alternatives": [
          "Use the available time to give a full walkthrough briefing covering zone layout, muster points, and terminology from first principles",
          "Give a brief handoff referencing established shorthand ('the usual Zone C protocol,' 'muster at the standard point'), assuming the new liaisons already understand shelter layout and terms, even though more time was available"
        ],
        "intended_action": "Training Officer gives the same abbreviated handoff briefing using internal shorthand, assuming the incoming liaison officers share the same background familiarity with shelter procedures, despite having ample uncommitted time to explain more fully."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two buses are available; three sites are requesting transport",
          "Road closures are worsening in one sector faster than others",
          "Transportation section chief flags fuel and driver-hours constraints"
        ],
        "new_information_after_decision": [
          "The prioritized site clears successfully before road closure",
          "One deprioritized site experiences a delay that increases evacuee wait time but is later resolved without injury"
        ],
        "alternatives": [
          "Split remaining transport evenly across all three requesting sites",
          "Prioritize the site facing the fastest-closing road access first"
        ],
        "intended_action": "Training Officer directs the transportation section to prioritize the site with the fastest-closing road access."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "An on-call Incident Commander has arrived to formally take over the real incident",
          "The exercise evaluators are still expecting a formal exercise debrief",
          "Some shelter operations are still using ad hoc handoff arrangements from phase 2"
        ],
        "new_information_after_decision": [
          "The Incident Commander requests a full written status briefing rather than a verbal summary",
          "The exercise is formally suspended and reclassified as a real activation"
        ],
        "alternatives": [
          "Continue running both the exercise debrief and real incident command informally in parallel",
          "Fully suspend the exercise, transfer command authority formally to the Incident Commander, and issue a written status briefing"
        ],
        "intended_action": "Training Officer formally suspends the exercise and transfers command to the Incident Commander with a written status briefing."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what was happening right before you realized this was becoming a real incident?",
        "What was your role supposed to be that day, and how did it change?"
      ],
      "timeline_reconstruction": [
        "What information did you have at each point, and where did it come from?",
        "What happened right after each of your major decisions?",
        "Were there moments where it was unclear whether something was scripted or real?"
      ],
      "decision_point_probes": [
        "What cues told you this was a real event rather than an exercise inject?",
        "You mentioned you had some time before turning to transportation — what did you decide to do with it during the liaison briefing?",
        "What alternatives did you consider for allocating the buses, and why did you rule the others out?",
        "How did you decide it was time to formally hand off to the Incident Commander?"
      ],
      "closing_hypotheticals": [
        "Given that you actually had time available for the liaison briefing, what would have changed had you used it differently?",
        "If the storm had hit an hour later, would your resource decisions have changed?",
        "Looking back, what would you tell a less experienced officer to watch for in a similar transition?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "decision_point": 2,
        "mechanism": "Expert briefer with years of familiarity with facility-specific shorthand assumes newly rotated liaison staff share the same tacit operational knowledge, and therefore omits explanatory detail, even when ample uncommitted time is available to explain more fully.",
        "affected_reasoning_operation": "Communication/briefing content selection when time pressure is not a binding constraint",
        "evidence_available_at_time": [
          "Liaison officers are newly rotated in and have not previously worked this shelter",
          "Approximately twenty-five minutes are available with no immediate competing task",
          "Training Officer has years of routine familiarity with zone/muster terminology"
        ],
        "required_textual_manifestation": "The Training Officer describes having available time before the next task, yet still delivers the handoff briefing in abbreviated shorthand ('the usual Zone C protocol,' 'muster at the standard point'); when probed about what was done with the extra time, the officer reveals the shorthand was used because the terms felt self-evidently understood, not because of a deliberate time trade-off; the same downstream misdirection and terminology-confusion consequence occurs.",
        "plausible_nonbias_interpretation": "The officer might describe the shorthand as simply their normal communication style with any liaison officer, independent of actual understanding, which could be read as a habitual register rather than a knowledge-assumption failure -- this must be distinguished by the officer's explicit acknowledgment, under probing, that they did not check what the liaisons already knew despite having time to do so.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "curse of knowledge",
          "assumed shared knowledge",
          "cognitive bias",
          "hindsight bias",
          "egocentric communication bias"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "EM_Biased_1",
      "features_to_match": [
        "Storm severity and general timeline",
        "Identity, role, and experience level of the liaison officers",
        "Transportation resource constraints and the phase 3 decision",
        "Phase 1 and phase 4 decisions and reasoning",
        "Use of the same shorthand terminology ('Zone C protocol', 'standard muster point')",
        "The downstream misdirection consequence at the shelter"
      ],
      "features_to_remove_or_change": [
        "Amount of time available before the shift-handoff briefing (changed from ~10 minutes under acute time pressure to ~25 minutes with no immediate competing task)"
      ],
      "ambiguity_boundary": "Not applicable as a control; this is a counterfactual variant, not a zero-bias control. The manifest still requires exactly one Curse of Knowledge instance."
    },
    "counterfactual_specification": {
      "causal_variable": "Amount of time available for the shift-handoff briefing before the Training Officer had to move to a competing task",
      "original_state": "In EM_Biased_1, only about ten minutes were available before the officer needed to turn to transportation duties, creating acute time pressure during the liaison briefing.",
      "counterfactual_state": "In this variant, about twenty-five minutes are available with no immediate competing task, removing acute time pressure as a plausible sole explanation for the abbreviated briefing.",
      "variables_to_hold_constant": [
        "Storm timeline and severity",
        "Liaison officers' identity, role, and experience level",
        "Transportation resource constraints and phase 3 reasoning",
        "Phase 1 and phase 4 decisions and reasoning",
        "The specific shorthand terms used and the downstream misdirection consequence"
      ],
      "expected_causal_difference": "Because the officer still gives the same abbreviated briefing despite having ample time, the interview should make it harder to attribute the communication gap to time pressure alone, strengthening the inference that the gap stems from an assumption that the liaison officers already shared the officer's background knowledge.",
      "causal_test_question": "Does removing acute time pressure change whether the Training Officer gives a fuller explanatory briefing, or does the abbreviated, assumption-laden briefing persist regardless of available time?"
    },
    "generation_checks": [
      "Exactly one Curse of Knowledge instance planned, matching manifest occurrence count of 1, consistent with counterfactual condition rules requiring the manifest to still be implemented",
      "Instance assigned to decision point 2, distinct from the other three decision points which contain no intended bias instances",
      "Only one causal variable changed relative to EM_Biased_1: time available before the liaison briefing",
      "All other material facts, actors, and the phase 3 and phase 4 decisions held constant relative to the base scenario",
      "No bias labels or psychological terminology will appear in the public interview text",
      "Interview scoped to fit 1,215-1,485 word range across 4 decision points with proportionate probe coverage",
      "Plausible non-bias explanation (habitual communication register) documented for the single instance to prevent mechanical over-attribution",
      "Downstream consequence (misdirection) preserved from the base scenario to keep the causal comparison clean"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Curse of Knowledge",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Curse of Knowledge"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Curse of Knowledge",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "mechanism": "Expert briefer assumes newly rotated, less-informed liaison officers share the same tacit facility-specific knowledge and terminology, resulting in an under-explained shift-handoff briefing, persisting even when time pressure is removed as a confound.",
        "affected_reasoning_operation": "Content selection and calibration during a briefing when time is not a binding constraint",
        "evidence_source": "Training Officer's stated rationale for briefing content and use of available time, contrasted with liaison officers' subsequent confusion/misdirection",
        "distinctiveness_requirement": "Must be distinguishable from the base scenario's time-pressure-confounded instance by explicitly showing the same abbreviated briefing occurs even with ample uncommitted time, isolating the knowledge-assumption mechanism from a time-economization explanation."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": "EM_Biased_1",
    "counterfactual_variable": {
      "name": "Amount of time available for the shift-handoff briefing before the next competing task",
      "original_state": "Approximately ten minutes available, under acute time pressure from the pending transportation task",
      "changed_state": "Approximately twenty-five minutes available, with no immediate competing task",
      "variables_to_hold_constant": [
        "Storm timeline and severity",
        "Liaison officers' identity, role, and experience level",
        "Transportation resource constraints and phase 3 decision reasoning",
        "Phase 1 and phase 4 decisions and reasoning",
        "Shorthand terminology used and downstream misdirection consequence"
      ]
    },
    "scenario_id": "EM_Counterfactual_1",
    "domain_id": "EM",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence retained at decision point 2 (shift-handoff briefing), matching the base scenario's assignment, since the counterfactual condition requires implementing the identical manifest while varying exactly one causal factor (available briefing time) rather than the bias's decision-point placement.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Storm timeline and severity",
      "Liaison officers' identity, role, and experience level",
      "Transportation resource constraints and phase 3 decision reasoning",
      "Phase 1 and phase 4 decisions and reasoning",
      "Shorthand terminology used and downstream misdirection consequence"
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
        "segment_type": "decision_point_1_reasoning",
        "raw_interview_anchor": "Pausing the exercise and checking actual weather data after a scripted communications-disruption inject coincided with a real weather alert and ambiguous field reports.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "No hidden bias is assigned to decision point 1. The participant recognizes that reports do not fit the script and verifies real-time conditions before acting."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_point_2_reasoning",
        "raw_interview_anchor": "Giving newly rotated liaison officers the abbreviated instructions “usual Zone C protocol” and “standard muster point,” while assuming those local terms were self-explanatory despite having ample time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ck_01"
        ],
        "ground_truth_rationale": "Curse of Knowledge: the experienced briefer relies on facility-specific shorthand and assumes newly rotated liaisons share tacit operational knowledge; subsequent wrong-muster-point direction and terminology confusion support the mechanism."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_point_3_reasoning",
        "raw_interview_anchor": "Prioritizing the site facing the fastest-closing road access with two buses instead of splitting transport evenly across three sites.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "No hidden bias is assigned to decision point 3. The participant explicitly weighs closure risk and transport constraints to avoid stranding evacuees."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_point_4_reasoning",
        "raw_interview_anchor": "Suspending the exercise and transferring command to the Incident Commander with a written status briefing during degraded communications.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "No hidden bias is assigned to decision point 4. The written handoff is a deliberate reliability choice under degraded communications."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
