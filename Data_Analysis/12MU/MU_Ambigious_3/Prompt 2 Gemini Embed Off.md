You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. This is a routine interview to reconstruct how you approached a specific blast round — it's not an evaluation of your performance, and everything stays with the study team. Okay to go ahead?

Participant: Sure, no problem.

Interviewer: Can you tell me about your role and what this round involved?

Participant: I'm the drill and blast engineer for the lower sublevels — I own the pattern design, sign off on charging, and coordinate with geology and ventilation before anything fires. This was a production round in Panel 14, sublevel open stope, about 450 meters down, right next to the service shaft, so vibration control is always part of the picture. Goal was simple on paper: fire on schedule, hit fragmentation targets for the mill, stay under our PPV limits near the shaft.

Interviewer: What was the situation going in?

Participant: We were a shift behind and the mill was low on feed, so there was real pressure to keep moving. A couple days out, geology mapped a minor fault trace crossing about a third of the panel, with some moisture along it. Not alarming on its own, but new enough that I didn't want to just wave it off either. A full geotechnical resurvey would've eaten the whole shift, which we didn't have, so I had the crew run a limited spot-check on a handful of holes near the trace instead — a middle option between doing nothing and doing everything.

Interviewer: Walk me through what happened as drilling and charging progressed.

Participant: The spot-check came back clean on the three holes we tested, but it didn't cover the entire fault-affected stretch — I was upfront with the crew about that limitation. Once full drilling wrapped, a few more holes near the trace logged wet, including two just outside where we'd spot-checked. The explosives technician flagged those specific holes and suggested decking them with emulsion instead of running full ANFO columns. I went with that for the flagged holes only, keeping ANFO for the rest of the panel — partly on his data, partly because I'd handled similar wet ground before without major issues. Then, while loading, one more hole outside the original flagged list turned up borderline wet too, which we hadn't caught. On timing, our two vibration sensors near the shaft disagreed a bit — one comfortably under limit, the other borderline — and the vendor guidance didn't clearly say which one to trust for our geometry. I went with the more conservative longer-interval sequence given that mismatch. After firing, the fault-zone section came out with some overbreak and coarser fragmentation, vibration stayed under limit on both sensors but with less margin than usual, and no complaints came in.

Interviewer: Let's go back to the pattern decision specifically. What was driving the choice to spot-check rather than resurvey or just proceed?

Participant: Honestly, it was a resource call as much as anything. A full resurvey was the safer option in theory, but it would've blown the schedule entirely, and the pattern's history in that ground gave me some confidence it probably wasn't a major issue. The spot-check felt like a reasonable middle ground — get some current data without stopping everything.

Interviewer: Did the fact that it only covered part of the zone concern you at the time?

Participant: A bit, yeah. I flagged it to the crew supervisor as a known gap, not something I was fully comfortable with, but I judged it acceptable given the time we had.

Interviewer: On the charging decision — how did you land on the mixed approach rather than going one way or the other?

Participant: The technician's data pointed pretty specifically at certain holes, and I didn't have a strong reason to extend that to the whole panel. At the same time, I've seen wet ground behave both ways — sometimes it's nothing, sometimes it needs real adjustment — so I wasn't relying purely on his numbers or purely on my own read. It felt like combining both was the more defensible call.

Interviewer: Did you consider treating the whole panel more conservatively given the borderline hole that turned up later?

Participant: In hindsight, sure, but at the time it hadn't been discovered yet — that came up during loading, after the charging plan was already largely set.

Interviewer: Moving to the timing call — the two sensors disagreeing seems like a genuinely tricky spot. How did you work through that?

Participant: It was tricky. Neither sensor was clearly wrong, and the vendor's guidance didn't settle it for our specific layout. I talked it through with the safety officer, and we agreed the conservative reading deserved more weight given we couldn't fully explain the gap between the two. So we went with the longer interval, accepting a bit less fragmentation efficiency for a wider vibration margin.

Interviewer: Was there time pressure to just default to the standard sequence instead?

Participant: A little, but not enough to skip that conversation. It felt like the kind of disagreement worth pausing on for ten minutes.

Interviewer: Last one — after the round, how did you approach explaining the overbreak to the mine manager?

Participant: That one I genuinely couldn't resolve on the spot. It looked similar to a fault-zone overbreak pattern I'd seen at a previous site, but this round also had real gaps — the spot-check didn't cover everything, and the charging was mixed rather than uniform. Either factor could explain what we saw, maybe both together. I told the manager that rather than picking one story, and asked the geologist to review the current instrumentation before we changed anything for the next round.

Interviewer: Was there pressure to give a cleaner answer than that?

Participant: A little — he wanted something actionable — but I didn't think I could honestly narrow it down yet without more review.

Interviewer: If the spot-check had covered the entire fault-affected zone, do you think the outcome would have been different?

Participant: Possibly. We might have caught those additional wet holes earlier and adjusted the charging more broadly. I can't say for certain it would've changed the overbreak, but it would've closed one of the gaps we're now unsure about.

Interviewer: And if the two vibration sensors had agreed with each other?

Participant: That would've made the timing call much simpler — less deliberation, less uncertainty about which reading to trust.

Interviewer: Looking back, is there a specific piece of information that could have resolved the overbreak question one way or the other?

Participant: Full coverage on the geotechnical side, honestly. Right now we've got two plausible explanations sitting side by side, and neither the deviation survey nor my own experience is enough on its own to settle which one mattered more.

Interviewer: That's a really thorough walkthrough — thank you.

Participant: Happy to clarify anything further if it helps.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Ambigious_3",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Drill and Blast Engineer",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Panel 14 Fault-Zone Production Round (Ambiguous Reasoning Variant)",
    "scenario_summary_internal": "A drill and blast engineer manages the same Panel 14 production round context as the paired biased scenario - a newly mapped minor fault trace, schedule pressure from low mill feed, and vibration-sensitive shaft infrastructure - but at each decision point the engineer visibly weighs competing considerations, takes partial or hedged actions, and encounters genuinely equivocal outcomes. The reasoning is deliberately underdetermined: plausible non-bias explanations (limited resources, real trade-offs, incomplete but reasonably interpreted data) are always available alongside any resemblance to the target biases, and no decision is written to unambiguously instantiate experience bias, status quo bias, or overconfidence bias.",
    "occupational_realism": {
      "objective": "Design and fire a safe, on-schedule production blast round in Panel 14 that meets fragmentation and mill-feed targets despite a newly identified geological anomaly.",
      "setting": "Underground metal mine using sublevel open stoping, mid-shift production blasting cycle, Panel 14 approximately 450m below surface, ore body adjacent to a ventilation raise and a service shaft requiring strict vibration control.",
      "constraints": [
        "Mill is running low on ore feed, creating schedule pressure to fire the round on time",
        "Vibration (PPV) limits apply near the shaft and ventilation infrastructure",
        "A geologist has newly mapped a minor fault trace with localized moisture crossing part of the panel",
        "Blast crew and explosives technician have limited authority to override the engineer's design",
        "Explosives cost and inventory (ANFO vs emulsion) affect charging choices",
        "Two years of stable production history exist for the standard pattern used in adjacent panels",
        "Only a partial geotechnical spot-check, not a full survey, is feasible within the shift"
      ],
      "stakeholders": [
        "Drill and Blast Engineer (interviewee)",
        "Mine Geologist",
        "Blast Crew Supervisor",
        "Explosives Technician (vendor representative)",
        "Mine Manager",
        "Ventilation and Safety Officer"
      ],
      "technical_terms_to_use": [
        "burden and spacing",
        "powder factor",
        "stemming",
        "delay timing / initiation sequence",
        "fragmentation",
        "overbreak",
        "fly-rock",
        "blasthole deviation survey",
        "decking",
        "ANFO",
        "emulsion explosive",
        "PPV (peak particle velocity)",
        "fault trace",
        "sublevel stoping",
        "mill feed"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias",
        "overconfidence",
        "status quo bias",
        "experience bias"
      ],
      "constraints_note": "No domain constraints or excluded themes were specified by the caller."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Geologist's updated fracture map shows a minor fault trace crossing roughly one-third of Panel 14, with a noted moisture seep",
          "The current pattern (burden 2.7m x spacing 3.1m) has performed well in three adjacent panels over two years",
          "Mill feed is low and production is one shift behind schedule",
          "A full geotechnical resurvey would take a full shift; a limited spot-check of a few holes is feasible within an hour"
        ],
        "new_information_after_decision": [
          "The spot-check on three holes near the trace comes back within normal tolerance, but does not cover the full fault-affected zone",
          "Two holes just outside the spot-checked area later log as wet"
        ],
        "alternatives": [
          "Proceed with the standard pattern unmodified",
          "Commission a full geotechnical resurvey before finalizing the pattern",
          "Run a limited spot-check on a subset of holes near the trace and adjust only if it flags a problem"
        ],
        "intended_action": "The engineer selects the limited spot-check option, explicitly weighing the cost of a full resurvey against the schedule pressure and the pattern's track record, and proceeds with the standard pattern after the partial check comes back clear, while acknowledging it did not cover the whole fault-affected section."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Blasthole logs show a few wet holes and mild deviation readings near the fault trace, including two outside the earlier spot-check zone",
          "The explosives technician recommends decking and emulsion substitution for the specific flagged holes, not the whole panel",
          "The engineer has used fully columned ANFO successfully in similar-looking ground before, but also recalls one case where wet ground required adjustment",
          "Substituting emulsion for only the flagged holes costs modest additional time and inventory"
        ],
        "new_information_after_decision": [
          "The flagged holes are decked with emulsion as recommended; the rest of the panel is charged with standard ANFO",
          "One additional hole not on the original flagged list also turns out to be borderline wet, discovered only during loading"
        ],
        "alternatives": [
          "Adopt the technician's recommendation for the specifically flagged holes only",
          "Charge the entire panel uniformly with standard ANFO",
          "Charge the entire panel with emulsion as a precaution"
        ],
        "intended_action": "The engineer adopts a middle-ground approach, decking and substituting emulsion only in the holes flagged by the survey, explicitly citing both the technician's data and past experience with similar ground as joint inputs, while acknowledging that the survey may not have caught every borderline hole."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Seismic/PPV monitoring near the shaft shows readings that are elevated but within limit on one sensor and borderline on a second sensor with a different offset",
          "Two delay-timing options are available: the standard mine-wide sequence, or a longer-interval sequence recommended for infrastructure protection",
          "The two sensors give somewhat inconsistent readings, and the vibration vendor's guidance does not fully resolve which sensor is more representative for this geometry"
        ],
        "new_information_after_decision": [
          "The fired round keeps both sensors within limit, though the second sensor remains closer to threshold than the first",
          "No complaints are recorded, but the vibration margin is narrower than on comparable past rounds"
        ],
        "alternatives": [
          "Use the standard mine-wide delay sequence based on the first sensor's reading",
          "Adopt the longer-interval sequence based on the more conservative second sensor's reading",
          "Request a third monitoring point before deciding"
        ],
        "intended_action": "The engineer discusses the conflicting sensor readings with the safety officer, chooses the longer-interval sequence as the more conservative option given the ambiguity, and documents that the discrepancy between sensors was not fully resolved before firing."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Post-blast survey shows localized overbreak and coarser fragmentation concentrated near the fault-affected section, including areas both inside and outside the original spot-check zone",
          "Current round's deviation survey, moisture logs, and vibration data are available for review",
          "The engineer recalls a broadly similar overbreak pattern from a previous mine, but also notes this round had incomplete survey coverage and a mixed charging approach",
          "The mine manager wants a preliminary explanation before a formal review can be scheduled"
        ],
        "new_information_after_decision": [
          "The engineer flags multiple plausible contributing factors to the manager rather than a single cause",
          "The geologist agrees to review the current round's instrumentation data before any design change is finalized"
        ],
        "alternatives": [
          "Attribute the outcome primarily to the same fault-zone pattern seen at a previous mine",
          "Attribute the outcome primarily to the incomplete spot-check coverage and mixed charging approach specific to this round",
          "Present both explanations as unresolved pending further review and hold off on a firm recommendation"
        ],
        "intended_action": "The engineer explicitly lays out both the prior-experience pattern and the current round's specific data gaps as competing explanations, declines to commit to a single cause, and recommends waiting for the geologist's review before changing the next round's design."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role in planning the Panel 14 production round?",
        "What was the operational objective for this particular round?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you know at that point?",
        "What new information came in as drilling and charging progressed?",
        "How did the sequence of events unfold from pattern approval through firing?"
      ],
      "decision_point_probes": [
        "What cues or signals stood out to you at that moment?",
        "What information sources did you rely on for that decision?",
        "What were you trying to achieve with that choice?",
        "What alternatives did you consider, and why did you rule them out?",
        "What was the main basis for the decision you made?",
        "Had you handled a similar situation before? How did that shape your thinking, if at all?",
        "How much time pressure were you under when you made that call?",
        "How confident were you in the ground conditions or data at that point?"
      ],
      "closing_hypotheticals": [
        "If the spot-check had covered the whole fault-affected zone, do you think the outcome would have been different?",
        "If the two vibration sensors had agreed with each other, would the timing decision have been easier?",
        "Looking back, is there a piece of information that could have resolved the overbreak question either way?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MU_Biased_3",
      "features_to_match": [
        "Domain and role (drill and blast engineer, sublevel stoping mine)",
        "Setting: Panel 14, fault trace, mill feed pressure, shaft vibration constraints",
        "Four decision points in the same narrative order and general topic (pattern, charging, timing, post-blast diagnosis)",
        "Technical vocabulary and terminology set",
        "Stakeholders and their roles",
        "Overall word count target and probe structure",
        "Emotional tone (measured, professional, mild time pressure)"
      ],
      "features_to_remove_or_change": [
        "Replace single-track-record justification for the pattern decision with an explicit partial-verification action",
        "Replace outright override of the technician's recommendation with a partial, jointly-reasoned adoption",
        "Introduce genuinely conflicting sensor data at the vibration decision rather than a single clean data source",
        "Replace confident single-cause post-blast attribution with an explicit, unresolved multi-cause account"
      ],
      "ambiguity_boundary": "Reasoning must remain genuinely underdetermined: the engineer's choices are defensible given real resource and information constraints, and no answer should allow a validator to cleanly attribute the outcome to reliance on past success alone, resistance to changing an established approach, or unwarranted confidence in personal judgment over available data. Any resemblance to those patterns must be counterbalanced within the same answer by an explicit acknowledgment of the data's limits or by genuine, described deliberation."
    },
    "counterfactual_specification": {
      "causal_variable": "NONE",
      "original_state": "NONE",
      "counterfactual_state": "NONE",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "NONE",
      "causal_test_question": "NONE"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points appear, matching the paired scenario's topical structure.",
      "Confirm zero intentional instances of Experience Bias, Status quo bias, or Overconfidence Bias appear anywhere in the interview.",
      "Confirm each decision point includes an explicit acknowledgment of data limits, genuine trade-off deliberation, or a hedged/partial action that blocks a clean bias attribution.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the interview text.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals for each decision point.",
      "Confirm final word count falls within 1,215-1,485 words.",
      "Confirm consequences (overbreak, narrow vibration margin) remain genuinely ambiguous as to cause, consistent with multiple competing explanations presented in Phase 4."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Experience Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; any reference to prior experience must be explicitly counterbalanced by consideration of current, case-specific data within the same answer."
      },
      {
        "bias": "Status quo bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; the pattern decision must include a genuine verification action rather than pure retention of the existing approach on track-record grounds alone."
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; the charging decision must show joint reliance on both technician data and experience, with an explicit acknowledgment of data limits, rather than an unexamined override."
      }
    ],
    "target_bias_names": ["Experience Bias", "Status quo bias", "Overconfidence Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Experience Bias", "requested_occurrences": 0},
      {"bias": "Status quo bias", "requested_occurrences": 0},
      {"bias": "Overconfidence Bias", "requested_occurrences": 0}
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MU_Biased_3",
    "counterfactual_variable": {
      "name": "NONE",
      "original_state": "NONE",
      "changed_state": "NONE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Ambigious_3",
    "domain_id": "MU",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: zero occurrences were requested for this control condition. No decision-point allocation was performed for any target bias; each of the four decision points was instead designed with explicit hedging, partial actions, or multi-cause reasoning to preserve genuine ambiguity while matching the paired scenario's topical structure.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain (Mining and underground industrial operations) and role (Drill and Blast Engineer)",
      "Panel 14 setting, fault trace premise, mill feed schedule pressure, shaft vibration constraints",
      "Four decision points addressing pattern design, charging design, timing/vibration control, and post-blast diagnosis",
      "Stakeholder roster and their functional roles",
      "Technical vocabulary set and difficulty level (subtle)",
      "Target word count and probe-plan structure",
      "Overall emotional tone and narrative pacing"
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
        "segment_type": "pattern_decision_rationale",
        "raw_interview_anchor": "A full resurvey was the safer option in theory, but it would've blown the schedule entirely, and the pattern's history in that ground gave me some confidence it probably wasn't a major issue. The spot-check felt like a reasonable middle ground — get some current data without stopping everything.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The engineer makes a resource-constrained pattern decision, performs a limited verification action, and acknowledges the coverage gap; the hidden manifest specifies zero instances."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "charging_decision_rationale",
        "raw_interview_anchor": "The technician's data pointed pretty specifically at certain holes, and I didn't have a strong reason to extend that to the whole panel. At the same time, I've seen wet ground behave both ways — sometimes it's nothing, sometimes it needs real adjustment — so I wasn't relying purely on his numbers or purely on my own read. It felt like combining both was the more defensible call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The mixed charging choice jointly weighs technician data and prior experience while explicitly rejecting reliance on either source alone; the hidden manifest specifies zero instances."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "timing_decision_rationale",
        "raw_interview_anchor": "Neither sensor was clearly wrong, and the vendor's guidance didn't settle it for our specific layout. I talked it through with the safety officer, and we agreed the conservative reading deserved more weight given we couldn't fully explain the gap between the two. So we went with the longer interval, accepting a bit less fragmentation efficiency for a wider vibration margin.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The engineer resolves conflicting measurements through consultation and conservative risk management, with an explicit trade-off; no hidden bias instance is present."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "post_blast_causal_diagnosis",
        "raw_interview_anchor": "It looked similar to a fault-zone overbreak pattern I'd seen at a previous site, but this round also had real gaps — the spot-check didn't cover everything, and the charging was mixed rather than uniform. Either factor could explain what we saw, maybe both together. I told the manager that rather than picking one story, and asked the geologist to review the current instrumentation before we changed anything for the next round.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The engineer presents competing explanations, declines premature causal closure, and defers design changes pending review; no hidden bias instance is present."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "Possibly. We might have caught those additional wet holes earlier and adjusted the charging more broadly. I can't say for certain it would've changed the overbreak, but it would've closed one of the gaps we're now unsure about.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant gives a qualified counterfactual prediction and explicitly preserves uncertainty; no hidden bias instance is present."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "counterfactual_prediction",
        "raw_interview_anchor": "That would've made the timing call much simpler — less deliberation, less uncertainty about which reading to trust.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant describes how agreeing measurements would reduce uncertainty without attributing a bias; no hidden bias instance is present."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "information_gap_diagnosis",
        "raw_interview_anchor": "Full coverage on the geotechnical side, honestly. Right now we've got two plausible explanations sitting side by side, and neither the deviation survey nor my own experience is enough on its own to settle which one mattered more.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant identifies the information needed to resolve competing causal explanations and rejects single-source certainty; no hidden bias instance is present."
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
      "analysis_scope_note": "Evaluated the participant's retrospective reasoning for affirmative evidence of cognitive bias. No retrieved corpus passages were supplied in the prompt, so no corpus evidence could be cited."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Insensitivity to sample size",
        "alternative_labels": [
          "Law of small numbers",
          "Belief in the law of small numbers"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Geotechnical inspection scope after fault trace identification",
        "supporting_interview_quote": "The spot-check came back clean on the three holes we tested, but it didn't cover the entire fault-affected stretch — I was upfront with the crew about that limitation.",
        "plausible_mechanism": "A small, non-representative clean sample may have been used to support confidence that the fault-affected zone was unlikely to be a major issue.",
        "why_not_identified": "The participant explicitly acknowledged the limited coverage and selected it as a resource-constrained middle option; there is no affirmative evidence that the three-hole sample was treated as statistically representative or sufficient to eliminate risk."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "Availability heuristic",
        "alternative_labels": [
          "Ease-of-recall heuristic"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Charging decision for wet holes near fault trace",
        "supporting_interview_quote": "I went with that for the flagged holes only, keeping ANFO for the rest of the panel — partly on his data, partly because I'd handled similar wet ground before without major issues.",
        "plausible_mechanism": "Readily recalled prior experiences with wet ground may have disproportionately influenced risk estimates for the current panel.",
        "why_not_identified": "The prior experience was cited as only one factor alongside the explosives technician's data, and the transcript does not show that recall of prior instances overwhelmed current evidence or materially distorted the decision."
      },
      {
        "candidate_id": "cand_003",
        "classification_status": "candidate",
        "proposed_bias_label": "Overconfidence bias",
        "alternative_labels": [
          "Overprecision"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Initial pattern risk assessment",
        "supporting_interview_quote": "A full resurvey was the safer option in theory, but it would've blown the schedule entirely, and the pattern's history in that ground gave me some confidence it probably wasn't a major issue.",
        "plausible_mechanism": "The participant may have assigned greater confidence to a low-risk estimate than was warranted by the available historical and spot-check data.",
        "why_not_identified": "The confidence is expressed in qualified terms and was accompanied by additional data collection, so there is no objective calibration evidence or outcome measure in the transcript to establish overconfidence."
      },
      {
        "candidate_id": "cand_004",
        "classification_status": "candidate",
        "proposed_bias_label": "Plan continuation bias",
        "alternative_labels": [
          "Get-there-itis",
          "Continuation bias"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Decision to proceed with schedule rather than full geotechnical resurvey",
        "supporting_interview_quote": "A full geotechnical resurvey would've eaten the whole shift, which we didn't have, so I had the crew run a limited spot-check on a handful of holes near the trace instead — a middle option between doing nothing and doing everything.",
        "plausible_mechanism": "Schedule pressure may have created a preference to continue the original firing plan despite new fault-trace information.",
        "why_not_identified": "The participant did not ignore new information; he modified the plan with a spot-check and later adjusted charging. The transcript does not show an irrational continuation of the original plan."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No retrieved corpus passages were supplied, so corpus_evidence could not be populated and retrieved_corpus_support_used is false.",
      "The analysis is based on retrospective self-report; it cannot directly observe implicit or group decision processes.",
      "The transcript does not include objective calibration data, probabilistic base rates, or independent outcome measures needed to detect overconfidence, base-rate neglect, or selection biases.",
      "Several plausible heuristics were noted as candidates rather than identified occurrences because the evidence did not affirmatively demonstrate a distorting influence."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Ambigious_3_Gemini_off",
  "interview_id": "MU_Ambigious_3",
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
