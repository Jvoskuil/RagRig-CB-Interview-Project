You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time to talk through this. Before we start, I want to confirm you're comfortable having this incident discussed for training-development purposes, and that we can pause or skip anything you'd rather not detail.

Participant: Yeah, that's fine. This one's worth talking through anyway.

Interviewer: Good. Can you start by telling me who you are in this context and roughly what your role was supposed to be that day?

Participant: I'm a Training Officer for the county EM office. That day I was the exercise controller for a full-scale drill — a shelter-in-place and evacuation scenario at our county EOC and one of our affiliated public shelters. My job was to run injects, coordinate the simulated agencies, and evaluate how the shelter team and liaison staff performed under the exercise conditions.

Interviewer: And what actually happened?

Participant: About ninety minutes in, we got a report of a comms disruption. It was scripted — one of our injects — so at first I treated it that way. But almost immediately after, a real weather alert came through on my phone, a fast-moving winter storm, much faster than the forecast we'd built the exercise around. A couple of field reports started coming in that were ambiguous — I genuinely couldn't tell if they were part of the exercise or real conditions. So I paused the drill and checked the actual weather service data before doing anything else. That confirmed it: we had a real tower failure, not a scripted one, and roads were closing faster than forecast.

Interviewer: What made you decide to stop and verify rather than keep running the exercise?

Participant: Because the timing was too coincidental, and the reports didn't match our inject script. I've run enough of these to know when something's off-script. I didn't want to keep injecting scenario content into what might already be a real event.

Interviewer: Once you confirmed it was real, walk me through what happened next.

Participant: Right after that, two liaison officers arrived to relieve the exercise-shift shelter team — this was a scheduled shift handoff, storm or no storm. Neither of them had worked this particular shelter before. I had maybe ten minutes to brief them before I needed to shift attention to transportation, because we had buses that needed redirecting before roads closed. So I gave them a fast rundown — told them to run the usual Zone C protocol, muster the evacuees at the standard point, same as always. Then I moved on.

Interviewer: What happened after that handoff?

Participant: Maybe forty minutes later, during a headcount, it turned out a group of evacuees had been sent to the old west muster point instead of the current one — we'd changed that location about a year ago. And separately, one of the volunteer coordinators asked me point-blank what "Zone C protocol" even meant. That's when I realized the handoff hadn't landed the way I thought it had.

Interviewer: Let's slow down and go through this stage by stage. Starting with that first decision — pausing the exercise. What information did you have in front of you at that exact moment?

Participant: I had the scripted inject text, the live weather alert on my phone, and two unclear field radio reports. I didn't have direct confirmation of a real tower failure yet — that came after.

Interviewer: What alternatives did you weigh?

Participant: Either keep running the drill and treat the comms report as part of the script, or stop and check real data first. I chose to verify. If I'd been wrong, I'd have wasted a few minutes on a real drill for nothing. Given the mismatch in timing, that felt like the safer bet.

Interviewer: Fair enough. Now the liaison handoff — decision point two. What did you actually know about these two officers beforehand?

Participant: I knew they were newly rotated onto this shelter assignment. I didn't know their full experience level, but I assumed they'd have some baseline familiarity with our layout conventions, since that's fairly standard across our shelters.

Interviewer: When you gave them the shorthand briefing — "usual Zone C protocol," "standard muster point" — what did you assume they already understood?

Participant: Honestly, I assumed those terms would be self-explanatory to anyone who'd been through liaison training. I use them every day, so they don't feel like shorthand to me — they feel like the actual name of the thing. I wasn't thinking about it as skipping steps. It felt more like a normal handoff.

Interviewer: What alternative was available to you at that moment?

Participant: I could have walked them through the zone map and muster locations from scratch. That would've taken maybe five more minutes.

Interviewer: What made you choose the shorter version?

Participant: Time, mostly. I had buses to deal with. But if I'm honest, it wasn't purely a time trade-off — I didn't really stop to ask myself whether "the usual protocol" meant anything to them. It's just what I'd say to anyone on my team.

Interviewer: What would have changed your approach at that point?

Participant: If one of them had said upfront, "I've never worked this site," I probably would have slowed down. Neither of them said that, and I didn't ask.

Interviewer: Let's move to the transportation decision. What was the situation there?

Participant: Two buses available, three sites requesting transport, and the transportation chief flagged fuel and driver-hour limits. One sector's roads were closing noticeably faster than the others based on the county road updates.

Interviewer: What options did you consider?

Participant: Split the buses evenly across all three sites, or prioritize the site with the fastest-closing road first. I went with prioritizing that site.

Interviewer: Why that option over splitting evenly?

Participant: Splitting evenly sounded fair, but it risked stranding people at the site that was about to become unreachable. Prioritizing by road-closure risk meant we might delay the other two sites a bit, but nobody would get physically cut off.

Interviewer: How did that play out?

Participant: The prioritized site cleared in time. One of the other sites had a longer wait than we'd have liked, but nothing dangerous — they got transport once the first run was done.

Interviewer: Last decision point — the handoff to the Incident Commander. What was competing for your attention at that stage?

Participant: The IC had arrived to take over the real incident, but the exercise evaluators were still expecting a formal debrief, and some of the shelter arrangements were still running on the ad hoc setup from the earlier handoff.

Interviewer: What did you consider doing?

Participant: I could've tried to run the exercise debrief and real command informally side by side, or fully suspend the exercise and hand off command properly. I suspended it and gave the IC a written status briefing instead of just talking him through it.

Interviewer: Why written over verbal, given the time pressure?

Participant: Verbal felt faster, but I've seen handoffs get garbled that way, especially when comms are already degraded. Writing it down meant he had something to refer back to, and there was less chance of him missing something the way the liaison officers had earlier.

Interviewer: That's an interesting connection — did that earlier mix-up shape this choice?

Participant: A little, yeah. Not consciously at the time, but looking back, I think I was more careful here because of what happened with the muster point.

Interviewer: If you could redo the liaison briefing, what would you change?

Participant: I'd probably ask them directly what they already knew instead of assuming based on their role title. I think I treated "liaison officer" as if it came with a fixed set of knowledge attached, when really it depends a lot on which site they'd worked before.

Interviewer: And if the storm had hit an hour later, would any of your resource decisions have changed?

Participant: Probably not the bus prioritization — that logic holds regardless of timing. But I might have had more slack to do a fuller handoff briefing, which could have avoided the muster point confusion entirely.

Interviewer: Last one — what would you tell a less experienced officer stepping into a similar transition?

Participant: Don't assume shorthand travels with the title. Just because someone's qualified to be a liaison doesn't mean they've internalized your particular shelter's layout. It costs you almost nothing to check, and it can cost a lot if you don't.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "EM_Biased_1",
    "domain_id": "EM",
    "domain": "Emergency Management and Civil Protection",
    "role": "Emergency Management Training Officer",
    "condition": "biased",
    "generation_specification": {
      "scenario_title_internal": "Exercise-to-Real Transition During Winter Storm Shelter Handoff",
      "scenario_summary_internal": "An Emergency Management Training Officer is running a full-scale interagency training exercise simulating a shelter-in-place/evacuation scenario at a county EOC when a genuine winter storm knocks out primary communications and forces an unplanned mid-exercise transition to real incident coordination. The officer must decide whether to pause the drill, brief newly rotated liaison staff on shelter operations mid-transition, reallocate transportation resources under time pressure, and decide how to hand off command to the arriving on-call Incident Commander. Because the officer has run this shelter protocol dozens of times, they brief less-experienced liaison staff during the shift handoff using internal shorthand and assumed background knowledge, without recognizing that the newly arrived staff lack the same operational familiarity (Curse of Knowledge).",
      "occupational_realism": {
        "objective": "Maintain safe, coordinated shelter operations and evacuation transport during an unplanned transition from a training exercise to a real weather emergency, while handing off command smoothly to an incoming Incident Commander.",
        "setting": "County Emergency Operations Center (EOC) and an affiliated public shelter, during a scheduled full-scale training exercise that is overtaken by an actual severe winter storm causing communications outages and road closures.",
        "constraints": [
          "Primary radio and phone lines degraded by storm damage",
          "Newly rotated shelter liaison staff and volunteer coordinators unfamiliar with facility-specific procedures",
          "Limited transport assets shared between exercise injects and real evacuee movement",
          "Hard deadline before roads become impassable",
          "Ambiguity about which reports are scripted exercise injects versus real conditions"
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
        ],
        "timeline": []
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
            "Storm conditions require an immediate handoff briefing with limited time"
          ],
          "new_information_after_decision": [
            "The new liaison officers later misdirect evacuees to the wrong muster point during a subsequent headcount",
            "A volunteer coordinator asks what 'Zone C protocol' means partway through the shift"
          ],
          "alternatives": [
            "Give a full walkthrough briefing covering zone layout, muster points, and terminology from first principles",
            "Give a brief handoff referencing established shorthand ('the usual Zone C protocol,' 'muster at the standard point'), assuming the new liaisons already understand shelter layout and terms"
          ],
          "intended_action": "Training Officer gives the abbreviated handoff briefing using internal shorthand, assuming the incoming liaison officers share the same background familiarity with shelter procedures."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "Two buses are available; three sites are requesting transport",
            "Road closures are worsening in one sector faster than another",
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
          "When you briefed the new liaison officers, what did you assume they already knew?",
          "What alternatives did you consider for allocating the buses, and why did you rule the others out?",
          "How did you decide it was time to formally hand off to the Incident Commander?"
        ],
        "closing_hypotheticals": [
          "If you had more time, what would you have done differently in the liaison handoff?",
          "If the storm had hit an hour later, would your resource decisions have changed?",
          "Looking back, what would you tell a less experienced officer to watch for in a similar transition?"
        ]
      },
      "occurrence_embedding_plan_internal": [
        {
          "instance_id": "ck_01",
          "bias": "Curse of Knowledge",
          "decision_point": 2,
          "mechanism": "Expert briefer with years of familiarity with facility-specific shorthand assumes newly rotated liaison staff share the same tacit operational knowledge, and therefore omits explanatory detail that would be obvious in hindsight to be necessary for novices.",
          "affected_reasoning_operation": "Communication/briefing content selection under time pressure",
          "evidence_available_at_time": [
            "Liaison officers are newly rotated in and have not previously worked this shelter",
            "Time pressure from the storm limits briefing length",
            "Training Officer has years of routine familiarity with zone/muster terminology"
          ],
          "required_textual_manifestation": "The Training Officer describes giving the handoff briefing in abbreviated shorthand ('the usual Zone C protocol,' 'muster at the standard point') and, when asked in a probe what the new liaisons knew beforehand, reveals an assumption that they would recognize these terms without further explanation; the interview later notes a liaison officer's confusion or misdirection stemming from that gap.",
          "plausible_nonbias_interpretation": "The officer might simply have been rushed by genuine time pressure and reasonably economized language, without any assumption about shared knowledge -- this must be distinguishable by the officer's explicit assumption that the terms were 'standard' or 'obvious' rather than a deliberate, reasoned trade-off acknowledging the liaisons' inexperience.",
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
        "paired_scenario_id": null,
        "features_to_match": [],
        "features_to_remove_or_change": [],
        "ambiguity_boundary": "Not applicable: condition is 'biased' with no paired control scenario specified in this request."
      },
      "counterfactual_specification": {
        "causal_variable": "Whether the Training Officer explicitly explained shelter zone/muster terminology during the shift-handoff briefing versus relying on shorthand assuming shared knowledge",
        "original_state": "Training Officer uses shorthand terminology assuming liaison officers already understand it (as embedded in this scenario)",
        "counterfactual_state": "Training Officer gives a full explanatory briefing covering zone layout and muster-point terminology from first principles",
        "variables_to_hold_constant": [
          "Storm timeline and severity",
          "Identity and experience level of the incoming liaison officers",
          "Transportation resource constraints",
          "Sequence and content of the other three decision points"
        ],
        "expected_causal_difference": "A fuller briefing would likely reduce or eliminate the later muster-point misdirection, without necessarily changing decisions at the other three decision points.",
        "causal_test_question": "Autoselected candidate for a possible future counterfactual pairing; not implemented in this 'biased' condition instance since no paired scenario was requested."
      },
      "generation_checks": [
        "Exactly one Curse of Knowledge instance planned, matching manifest occurrence count of 1",
        "Instance assigned to decision point 2, distinct from the other three decision points which contain no intended bias instances",
        "No bias labels or psychological terminology will appear in the public interview text",
        "Interview scoped to fit 1,215-1,485 word range across 4 decision points with proportionate probe coverage",
        "Plausible non-bias explanation documented for the single instance to prevent mechanical over-attribution",
        "No paired control or counterfactual scenario is being generated under this request; specification fields for those are populated as null/autoselected placeholders only"
      ]
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "biased",
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
          "mechanism": "Expert briefer assumes newly rotated, less-informed liaison officers share the same tacit facility-specific knowledge and terminology, resulting in an under-explained shift-handoff briefing.",
          "affected_reasoning_operation": "Content selection and calibration during time-pressured briefing/communication",
          "evidence_source": "Training Officer's stated rationale for briefing content, contrasted with liaison officers' subsequent confusion/misdirection",
          "distinctiveness_requirement": "Must be distinguishable from simple time-pressure economization by showing the officer treats the shorthand as self-evidently understood rather than as a deliberate, acknowledged trade-off given the liaisons' inexperience."
        }
      ],
      "intended_strength": [
        {
          "instance_id": "ck_01",
          "bias": "Curse of Knowledge",
          "strength": "moderate"
        }
      ],
      "paired_scenario_id": null,
      "counterfactual_variable": {
        "name": "Explicitness of terminology explanation during liaison handoff briefing",
        "original_state": "Shorthand briefing assuming shared knowledge",
        "changed_state": "Fully explanatory briefing covering terminology from first principles",
        "variables_to_hold_constant": [
          "Storm timeline and severity",
          "Liaison officers' experience level",
          "Transportation constraints",
          "Content of decision points 1, 3, and 4"
        ]
      },
      "scenario_id": "EM_Biased_1",
      "domain_id": "EM",
      "total_requested_occurrences": 1,
      "total_planned_occurrences": 1,
      "allocation_rule_used": "Single occurrence assigned to the decision point (shift-handoff briefing, phase 2) offering the strongest mechanism fit for Curse of Knowledge in this domain, given the Training Officer's long-standing familiarity with shelter terminology versus the incoming liaison officers' inexperience; no splitting across decision points was needed since only one occurrence was requested.",
      "control_zero_bias_requirement": false,
      "variables_to_hold_constant": [
        "Storm timeline and severity",
        "Liaison officers' experience level",
        "Transportation constraints",
        "Sequence and content of decision points 1, 3, and 4"
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
        "segment_type": "initial_interpretation",
        "raw_interview_anchor": "The participant initially treated the comms disruption as a scripted exercise inject.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A provisional classification based on the exercise script; it was immediately questioned and verified rather than allowed to distort action."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "verification_choice",
        "raw_interview_anchor": "The participant paused the drill and checked actual weather-service data after the alert and ambiguous reports.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant selected external verification in response to conflicting evidence; this is non-biased evidence checking."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "The timing and mismatch with the inject script led the participant to stop injecting scenario content into a possible real event.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The stated rationale weighs timing and evidence mismatch and does not instantiate the hidden bias."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "communication_choice",
        "raw_interview_anchor": "The participant gave newly arrived liaison officers a fast handoff using ‘usual Zone C protocol’ and ‘standard point’ shorthand before shifting to transportation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is the selected communication action, while the defining shared-knowledge assumption is expressed more narrowly in seg_007."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "retrospective_causal_attribution",
        "raw_interview_anchor": "The participant describes the later wrong muster point and the volunteer’s confusion about Zone C protocol.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is outcome and retrospective recognition of a communication failure, not a separate hidden occurrence."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "audience_assumption_context",
        "raw_interview_anchor": "The participant knew the officers were newly rotated, lacked full experience information, and assumed baseline familiarity with shelter conventions.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This supplies contextual evidence for the primary manifestation but is not treated as a separately mapped occurrence."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "communication_reasoning",
        "raw_interview_anchor": "The participant says the terms felt self-explanatory because they used them every day and did not stop to consider whether the incoming staff understood them.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["ck_01"],
        "ground_truth_rationale": "This is the narrowest primary manifestation of Curse of Knowledge: expert familiarity makes site-specific shorthand feel transparently understood by less-familiar recipients."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "alternative_consideration",
        "raw_interview_anchor": "The participant identifies a full zone-map and muster-location walkthrough as an available alternative.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "An alternative is acknowledged, but this span does not itself contain the hidden mechanism."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "The participant cites time pressure but also admits not asking whether the shorthand meant anything to the recipients.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This reinforces the primary mechanism but is not separately mapped to avoid duplicating the single hidden occurrence."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "The participant says they would have slowed down if an officer had disclosed never working the site, while acknowledging they did not ask.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is retrospective counterfactual reasoning about a corrective cue, not a second bias instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "resource_allocation_choice",
        "raw_interview_anchor": "With two buses and three requesting sites, the participant chose to prioritize the site facing the fastest-closing roads.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The resource-allocation choice follows the stated road-closure risk and is not a hidden bias instance."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "resource_allocation_rationale",
        "raw_interview_anchor": "The participant rejects even splitting because it could strand people, accepting delay for other sites to avoid physical cutoff.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an explicit risk-based trade-off supported by available road information."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "command_handoff_choice",
        "raw_interview_anchor": "The participant suspended the exercise, transferred the real incident to the arriving Incident Commander, and provided a written status briefing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant chose a formal handoff rather than running exercise and real command in parallel; no hidden instance is assigned here."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "handoff_format_rationale",
        "raw_interview_anchor": "The participant preferred written over verbal transfer because degraded communications could cause information to be missed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a documented communication-reliability rationale, not the hidden expert-knowledge mechanism."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "retrospective_influence",
        "raw_interview_anchor": "The participant says the earlier muster-point mix-up made them more careful with the later Incident Commander handoff.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective explanation of learning from an earlier event, not a hidden bias instance."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "corrective_reflection",
        "raw_interview_anchor": "If redoing the liaison briefing, the participant would ask what staff already knew instead of inferring knowledge from their role title.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a corrective reflection and contains the candidate representativeness interpretation, but it is not a separate hidden instance."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "The participant predicts bus prioritization would remain unchanged with later storm timing, while a fuller handoff might have prevented confusion.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a counterfactual comparison of operational decisions, not an additional bias occurrence."
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
    "analysis_scope_note": "Conservative mechanism-first analysis of the participant's stated reasoning and decisions; only affirmative, bias-specific mechanism evidence is classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Curse of knowledge",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Curse of knowledge",
      "alternative_labels": ["False consensus effect", "Illusion of transparency", "Egocentric bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency of informed individuals to overestimate the degree to which others share their knowledge and to fail to adequately imagine a less-informed perspective.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Liaison handoff briefing during transition from exercise to real incident",
      "decision_point_description": "The participant had to decide whether to give newly arrived liaison officers a rapid shorthand briefing or a fuller site-specific orientation.",
      "affected_reasoning_operation": "Audience design and perspective-taking in emergency communication",
      "bias_specific_mechanism": "Using his own daily familiarity with site-specific terms as an automatic baseline, the participant failed to discount privileged knowledge when estimating what the new officers would understand.",
      "manifestation_in_interview": "The participant briefed two newly arrived liaison officers using shorthand such as 'usual Zone C protocol' and 'standard muster point' under time pressure, treating those terms as self-evident and later acknowledging they felt like the actual names of the things rather than shorthand.",
      "effect_on_reasoning_or_decision": "The handoff landed as routine and self-explanatory rather than as a site-specific orientation. This contributed to evacuees being sent to the old west muster point and a volunteer coordinator later asking what 'Zone C protocol' meant.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "So I gave them a fast rundown — told them to run the usual Zone C protocol, muster the evacuees at the standard point, same as always. Then I moved on.",
          "evidence_explanation": "This shows the communication decision: site-specific procedures were delivered as familiar shorthand without checking whether the new officers shared that site-specific knowledge."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I assumed those terms would be self-explanatory to anyone who'd been through liaison training. I use them every day, so they don't feel like shorthand to me — they feel like the actual name of the thing. I wasn't thinking about it as skipping steps. It felt more like a normal handoff.",
          "evidence_explanation": "Directly articulates the curse-of-knowledge mechanism: his own everyday familiarity made the labels feel transparent and routine, so he did not adjust for listeners who lacked that familiarity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe forty minutes later, during a headcount, it turned out a group of evacuees had been sent to the old west muster point instead of the current one — we'd changed that location about a year ago. And separately, one of the volunteer coordinators asked me point-blank what 'Zone C protocol' even meant. That's when I realized the handoff hadn't landed the way I thought it had.",
          "evidence_explanation": "Demonstrates the material effect of the communication failure on shelter operations and the participant's later recognition that the shared-knowledge assumption was incorrect."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized the problem and said he would ask officers directly what they already knew instead of assuming based on their role title. He also used a written status briefing for the Incident Commander specifically to reduce the chance of the same kind of garbled handoff.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly supported the curse-of-knowledge mechanism; this label is applied from established cognitive-science knowledge, not from the provided retrieval corpus.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": ["Category-based inference", "Stereotyping"],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which a judgment about an individual or event is based on similarity to a category prototype, often without adequately adjusting for variability or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Liaison handoff briefing during transition from exercise to real incident",
      "decision_point_description": "The participant had to assess the incoming liaison officers' likely familiarity with the specific shelter site and its procedures before deciding how much orientation to provide.",
      "affected_reasoning_operation": "Judgment of individual knowledge based on role category",
      "bias_specific_mechanism": "The participant inferred individual site-specific knowledge from the officers' role title and standard training category, assuming that being a liaison officer carried a fixed set of knowledge even though actual familiarity depended on which site they had worked.",
      "manifestation_in_interview": "Although the participant knew the two officers were newly rotated onto this shelter assignment and did not know their experience level, he assumed they would have baseline familiarity with layout conventions because that was fairly standard across shelters.",
      "effect_on_reasoning_or_decision": "The category-based assumption reinforced the decision not to conduct a fuller site-specific orientation or ask what the officers already knew, contributing to the same handoff miscommunication.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew they were newly rotated onto this shelter assignment. I didn't know their full experience level, but I assumed they'd have some baseline familiarity with our layout conventions, since that's fairly standard across our shelters.",
          "evidence_explanation": "Shows an inference from category or standard-practice information to the specific individuals, despite lacking individual experience information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I treated 'liaison officer' as if it came with a fixed set of knowledge attached, when really it depends a lot on which site they'd worked before.",
          "evidence_explanation": "Explicit retrospective recognition of the representativeness mechanism: using the role category as a proxy for site-specific knowledge."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If one of them had said upfront, 'I've never worked this site,' I probably would have slowed down. Neither of them said that, and I didn't ask.",
          "evidence_explanation": "Demonstrates that the participant relied on the absence of disconfirming information rather than actively verifying individual knowledge, consistent with category-based inference."
        }
      ],
      "correction_or_counterevidence": "The participant later said he should have asked directly what they already knew instead of assuming based on their role title, indicating recognition of the category-based inference.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly supported the representativeness heuristic mechanism in this communication context; this label is applied from established cognitive-science knowledge, not from the provided retrieval corpus.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Availability heuristic",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Handoff to Incident Commander",
      "supporting_interview_quote": "Verbal felt faster, but I've seen handoffs get garbled that way, especially when comms are already degraded. Writing it down meant he had something to refer back to, and there was less chance of him missing something the way the liaison officers had earlier.",
      "plausible_mechanism": "The recent liaison-handoff failure may have been salient and increased the participant's estimated probability of a similar failure during the Incident Commander handoff.",
      "why_not_identified": "The transcript frames this as a deliberate corrective action based on relevant recent experience rather than as a distorted estimate or adverse effect; there is insufficient affirmative evidence that the reasoning was biased rather than adaptive."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus did not contain passages directly addressing curse of knowledge or representativeness heuristic, so those classifications rely on established cognitive-science labels rather than retrieval support.",
    "The analysis is based on a single participant self-report; the liaison officers' actual knowledge and internal states were not directly observed.",
    "The two identified biases are tightly interwoven in one handoff episode and may be interacting rather than fully independent."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Biased_1_Sonnet_on",
  "interview_id": "EM_Biased_1",
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
