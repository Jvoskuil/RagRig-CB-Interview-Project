You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative, mechanism-first review of the interview for decision-making biases. One perspective-taking bias was identified in the liaison handoff episode."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Curse of knowledge",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Curse of knowledge",
      "alternative_labels": ["curse of expertise", "false consensus effect", "illusion of transparency"],
      "taxonomy_status": "established_label",
      "bias_definition": "The curse of knowledge is the cognitive bias whereby a person who possesses knowledge, expertise, or routinized familiarity with a topic fails to accurately reconstruct the perspective of someone who lacks that knowledge, causing them to overestimate the clarity, understandability, or sharedness of their communication.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Liaison shift handoff briefing at the public shelter",
      "decision_point_description": "Choosing how to brief two liaison officers who were new to the specific shelter, with roughly twenty-five minutes available and no immediate competing task.",
      "affected_reasoning_operation": "Perspective-taking and communication calibration; assessment of audience prior knowledge; selection of briefing depth and terminology",
      "bias_specific_mechanism": "The participant's fluent, routinized knowledge of site-specific protocol and muster point language made those local terms feel transparent and self-evident. This reduced the felt need to elicit or verify the incoming officers' knowledge, so he defaulted to the usual abbreviated briefing and failed to adjust for their unfamiliarity, despite knowing they had not worked that site before.",
      "manifestation_in_interview": "During the handoff, the participant told two new-to-site liaison officers to 'run the usual Zone C protocol, muster at the standard point, same as always' without checking whether they understood those references. Later, a group was found sent to the old west muster point, and a volunteer coordinator asked what 'Zone C protocol' referred to.",
      "effect_on_reasoning_or_decision": "The briefing transmitted labels and local references that the recipients could not correctly map to current locations or protocols, resulting in a group mustering at the old west muster point and apparent confusion about a key term. Extra time did not trigger a more thorough briefing because the participant experienced his shorthand as explicit, self-evident names.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew they were new to this shelter specifically. I didn't ask about their broader background — I assumed liaison officers generally pick up our zone conventions fast, since it's not unusual across our sites.",
          "evidence_explanation": "This shows the participant knew the officers lacked site-specific experience but nevertheless relied on an assumption about their shared knowledge rather than checking what they actually knew."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. I could have asked directly — 'have you worked this layout before, do you know where the current muster point is' — and I had time to do that. I just didn't think to.",
          "evidence_explanation": "This directly demonstrates the failure to verify audience knowledge despite available time, supporting an egocentric default rather than a resource constraint."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, it didn't occur to me that it needed to be longer. Those terms are just how I refer to things day to day — they don't register as shorthand to me, they register as the actual names. Having the extra time didn't change how I framed it, because I wasn't treating it as an abbreviated version of anything.",
          "evidence_explanation": "This is a hallmark of the curse of knowledge: the participant experienced his compressed local terminology as literal and transparent, so the audience's missing perspective did not become salient."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized the problem and articulated the lesson that one should not assume a title brings knowledge of local terms. However, this recognition occurred after the miscommunication had already affected the muster point. The available time, knowledge that the officers were new to the site, and absence of an immediate competing task reduce plausible non-bias explanations such as time compression or routine professional behavior under pressure.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The retrieved corpus did not include passages defining or validating the curse of knowledge or closely related perspective-taking biases. This classification relies on established cognitive-science knowledge; retrieved corpus support was unavailable for this specific bias.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring and adjustment",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Liaison shift handoff briefing",
      "supporting_interview_quote": "With the liaisons, I gave them the same rundown I always give — 'usual Zone C protocol,' 'standard muster point.' I didn't really stretch it out into something longer.",
      "plausible_mechanism": "The participant may have anchored on his usual briefing routine and made insufficient adjustments for the two officers' unfamiliarity, a pattern consistent with anchoring-and-adjustment as described in the retrieved corpus.",
      "why_not_identified": "The evidence is more directly explained by a curse-of-knowledge perspective-taking failure: the core distortion is not a numeric or initial-value estimate, but an egocentric assumption about shared knowledge. The anchor-like use of the same rundown is suggestive but insufficient to establish an anchoring-specific mechanism over the primary perspective-taking bias."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passage addressed the identified curse-of-knowledge bias directly; classification relies on general cognitive-science taxonomy.",
    "The transcript is a single participant self-report, so some mental processes are inferred from verbal testimony rather than direct observation.",
    "Routine professional shorthand and resource constraints were considered and were not classified as biases unless combined with affirmative evidence of a distinct cognitive distortion."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Counterfactual_1_Gemini_on",
  "interview_id": "EM_Counterfactual_1",
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
