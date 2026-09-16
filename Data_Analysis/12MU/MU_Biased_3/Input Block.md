<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — we're reconstructing how you approached a specific blast round, not evaluating performance. Everything you share stays with the study team. Comfortable to proceed?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me a bit about your role and what this particular round involved?

Participant: I'm the drill and blast engineer for the lower sublevels, so I design the pattern, sign off on charging, and coordinate with the geology and ventilation teams before anything gets fired. This one was a production round in Panel 14 — sublevel open stope, about 450 meters down, right next to the service shaft and a ventilation raise, so vibration control matters there. The objective was straightforward: get the round fired on schedule, keep fragmentation good enough for the mill, and stay inside our PPV limits near the shaft.

Interviewer: What was the situation going in?

Participant: We were already a shift behind, and the mill was low on feed, so there was pressure to keep things moving. A couple of days before, geology flagged a minor fault trace crossing maybe a third of the panel, with a bit of moisture along it. Nothing dramatic — geologists flag structure fairly often in that area. We'd been running the same pattern, 2.7 by 3.1 burden and spacing, in three adjacent panels for about two years without issues, so that was the baseline I was working from.

Interviewer: Walk me through what happened once drilling started.

Participant: Drilling went ahead on the standard layout. A handful of holes near the fault trace came back wet, and the deviation survey showed a few of them drifting more than we'd normally tolerate. The crew mentioned the ground felt a bit looser in that section, but it went into the shift log as a routine note, nothing flagged for follow-up. Once charging started, our explosives tech looked at those readings and suggested decking the affected holes and swapping to emulsion for the wet ones instead of running full ANFO columns. I decided to stick with the standard charge across the panel. We fired on the planned timing, adjusted for the shaft-side sensitivity, and afterward the muck pile in that fault section came out coarser than expected, with some overbreak. No safety issues, vibration stayed under limit, but the fragmentation in that corner wasn't what we wanted.

Interviewer: Let's go back through this step by step. First, the pattern decision — once geology handed you that fracture map, what were you actually weighing?

Participant: Mostly time and track record. That pattern's fired dozens of rounds in similar ground without a hiccup, so redesigning burden and spacing for a fault trace that geology themselves called minor felt like it would cost us a day we didn't have, for a problem that historically hasn't caused us grief in that rock.

Interviewer: Did you consider getting additional geotech verification before finalizing it?

Participant: It came up briefly, yeah. But honestly, given how well that pattern's performed, I didn't see it as justified. We tightened the stemming slightly on that side as a small hedge, but kept the design essentially as-is.

Interviewer: What would it have taken for you to actually pause and reverify?

Participant: Probably if geology had called it a major structure, or if we'd seen it show up on more than one panel survey. A single minor trace with a track record like ours behind it didn't feel like enough to slow down for.

Interviewer: Moving to charging — the technician raised a specific concern about the flagged holes. What went through your mind there?

Participant: I've charged plenty of holes that looked like that — a bit wet, slightly off on deviation — and it's never been a real problem when the surrounding rock was competent. I've used full ANFO columns in ground that looked rougher than this and it worked out fine, so I told the crew we'd run it as planned.

Interviewer: Did you go back through the specific deviation numbers or moisture readings for those holes before making that call?

Participant: Not in detail, no. I'd seen the technician's note and I trusted my read of the situation from experience more than I felt I needed to re-pull the log line by line.

Interviewer: What alternatives were on the table at that point?

Participant: Decking with emulsion in the wet holes, like he suggested, or pushing the charging back to resurvey first. Both were doable, just would've eaten into the firing window.

Interviewer: Third decision — the timing and vibration question near the shaft. How did you approach that?

Participant: That one I spent more time on, actually. The monitoring vendor had recommended a longer delay interval for rounds close to sensitive infrastructure, and our live PPV readings were creeping toward the limit on the comparable round before. I compared the fragmentation trade-off against the vibration risk directly and went with the longer sequence on the shaft-facing side. It cost us a bit on fragmentation there, but it kept us clearly under limit.

Interviewer: What made that one feel more resolved than the others?

Participant: We had current numbers right in front of us — actual PPV readings, not just a general sense of things. Easier to make a clean call when the data's that immediate.

Interviewer: Last one — after the round, you had overbreak and coarse fragmentation in the fault section. How did you explain that to yourself and to the mine manager?

Participant: It reminded me a lot of a panel I worked years ago at a different site — same kind of localized fault, same overbreak signature. There, the fix was tightening the pattern and adjusting timing specifically through that corridor, and it worked well. So that's what I recommended here.

Interviewer: Did you look back at this round's own deviation survey or moisture logs as part of that diagnosis?

Participant: Not closely — the pattern matched what I'd seen before closely enough that I was fairly confident in the read.

Interviewer: Was geology brought in to review the current instrumentation before that recommendation went forward?

Participant: Not yet, no. That's probably a next step, but I wanted to give the manager something actionable in the moment.

Interviewer: If the deviation survey had shown something you hadn't seen before, would your charging decision have gone differently?

Participant: Possibly — if it was unfamiliar, I'd have wanted the technician to walk me through it properly rather than just going with my gut.

Interviewer: And if this had been your first round in this panel rather than one of many, do you think the pattern decision changes?

Participant: Probably, yeah. Without that history to lean on, I'd likely have wanted the extra geotech pass before committing.

Interviewer: Last one — looking back, is there a point where different information might have changed how you diagnosed the overbreak?

Participant: If I'd pulled this round's own logs first, side by side with the old site's data, instead of going mostly off memory — that might've told a different story. I'm not sure it would have, but I didn't really test it that way.

Interviewer: That's really helpful, thank you. I think we've got a solid picture of the whole sequence.

Participant: No problem, happy to clarify anything further if it's useful.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Biased_3",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Drill and Blast Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Panel 14 Fault-Zone Production Round",
    "scenario_summary_internal": "An underground drill and blast engineer must design and execute a production blast round in Panel 14 of a sublevel stoping operation after geology reports a newly mapped minor fault trace and localized wet ground crossing the panel, while the mill is running low on feed and schedule pressure is high. The engineer must decide whether to modify the established blast pattern, how to charge holes that log anomalies near the fault, how to manage vibration/timing near shaft infrastructure, and how to interpret an imperfect blast outcome afterward. The incident is designed so that a status-quo pattern decision, an overconfident charging override, and an experience-driven post-blast attribution can each occur naturally without being flagged as errors by the narrative or by outcome framing.",
    "occupational_realism": {
      "objective": "Design and fire a safe, on-schedule production blast round in Panel 14 that meets fragmentation and mill-feed targets despite a newly identified geological anomaly.",
      "setting": "Underground metal mine using sublevel open stoping, mid-shift production blasting cycle, Panel 14 approximately 450m below surface, ore body adjacent to a ventilation raise and a service shaft requiring strict vibration control.",
      "constraints": [
        "Mill is running low on ore feed, creating schedule pressure to fire the round on time",
        "Vibration (PPV) limits apply near the shaft and ventilation infrastructure",
        "A geologist has newly mapped a minor fault trace with localized moisture crossing part of the panel",
        "Blast crew and explosives technician have limited authority to override the engineer's design",
        "Explosives cost and inventory (ANFO vs emulsion) affect charging choices",
        "Two years of stable production history exist for the standard pattern used in adjacent panels"
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
          "The current pattern (burden 2.7m x spacing 3.1m) has been used successfully in three adjacent panels over two years",
          "Mill feed is low and production is one shift behind schedule",
          "No additional geotechnical drilling has been ordered for this panel"
        ],
        "new_information_after_decision": [
          "Several blastholes drilled near the mapped fault log as wet and show minor deviation beyond normal tolerance",
          "The drill crew mentions the ground 'felt looser' in that section but logs it as a routine note"
        ],
        "alternatives": [
          "Proceed with the standard, previously successful burden/spacing pattern, adjusting only stemming slightly",
          "Commission a short geotechnical verification pass before finalizing the pattern",
          "Reduce the round size and treat the fault-affected section as a separate, smaller test round"
        ],
        "intended_action": "The engineer approves the standard pattern with only a minor stemming adjustment, citing the pattern's long track record in the mine, and does not commission further geotechnical verification of the fault trace before drilling proceeds."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Blasthole logs show several wet holes and deviation readings above normal near the fault trace",
          "The explosives technician recommends decking the affected holes and substituting emulsion for the wet sections instead of a fully columned ANFO charge",
          "The engineer has successfully used fully columned ANFO charges in visually similar ground on past rounds",
          "Firing window is fixed to align with the shift's ventilation clearance schedule"
        ],
        "new_information_after_decision": [
          "The charge is loaded as fully columned ANFO across most of the panel, including several of the flagged holes",
          "The technician notes the deviation survey again at loading but does not escalate further once the engineer confirms the plan"
        ],
        "alternatives": [
          "Accept the technician's recommendation to deck and switch to emulsion in the flagged holes",
          "Proceed with the standard fully columned ANFO charge across the panel",
          "Delay charging to re-survey the flagged holes before deciding"
        ],
        "intended_action": "The engineer overrides the technician's recommendation, reassures the crew based on past success with similar-looking ground, and proceeds with the standard fully columned ANFO charge without re-examining the updated deviation and moisture logs in detail."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Seismic/PPV monitoring near the shaft shows readings approaching but not exceeding the vibration limit on the previous comparable round",
          "Two delay-timing options are available: the standard sequence used mine-wide, or a longer-interval sequence recommended by the vibration monitoring vendor for rounds near sensitive infrastructure",
          "Longer delays would modestly reduce fragmentation efficiency but lower peak vibration"
        ],
        "new_information_after_decision": [
          "The chosen delay sequence keeps vibration within limits and fragmentation within an acceptable range",
          "No complaints or exceedances are recorded near the shaft after firing"
        ],
        "alternatives": [
          "Use the standard mine-wide delay sequence",
          "Adopt the longer-interval sequence recommended for infrastructure protection",
          "Split the round into two smaller fired sequences"
        ],
        "intended_action": "The engineer reviews the current monitoring data directly, weighs the fragmentation-versus-vibration trade-off on its merits, and selects the longer-interval sequence near the shaft-facing section. This decision point is deliberately left free of intended bias instances."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Post-blast survey shows localized overbreak and coarser-than-expected fragmentation concentrated in the fault-affected section",
          "A minor, within-limit vibration spike was recorded near the shaft during that section's firing",
          "Current round's deviation survey and moisture logs from Phase 1 and 2 are available for review",
          "The engineer previously worked at another mine where similar overbreak patterns near fault zones were common and were resolved with a specific standard fix"
        ],
        "new_information_after_decision": [
          "The mine manager asks for a brief explanation and a recommendation for the next round's design",
          "The geologist has not yet been asked to formally review the current round's instrumentation data"
        ],
        "alternatives": [
          "Recommend a formal site-specific investigation using the current round's deviation and moisture data before changing the design",
          "Attribute the outcome to the same fault-zone pattern seen at a previous mine and apply that mine's standard fix directly",
          "Escalate the section's data to the geotechnical engineer for independent review before next round's design is set"
        ],
        "intended_action": "The engineer explains the overbreak by drawing on the similar-looking pattern from a previous mine and recommends applying that prior fix for the next round, without first incorporating the current round's own deviation survey and moisture readings into the diagnosis."
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
        "Had you handled a similar situation before? How did that shape your thinking?",
        "How much time pressure were you under when you made that call?",
        "How confident were you in the ground conditions or data at that point?"
      ],
      "closing_hypotheticals": [
        "If the deviation survey had shown even more pronounced anomalies, would you have made the same charging decision?",
        "If this had been your first round in this panel rather than your hundredth, would your pattern decision have differed?",
        "Looking back, is there a point where a different data source might have changed your diagnosis of the overbreak?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_02",
        "bias": "Status quo bias",
        "decision_point": 1,
        "mechanism": "Preference for the existing, previously validated blast pattern over adapting to new geotechnical information, justified by the pattern's track record rather than by evaluating the fault trace on its own merits",
        "affected_reasoning_operation": "Evidence-selection and decision act: whether to redesign burden/spacing given the new fault-trace report",
        "evidence_available_at_time": [
          "Geologist's updated fracture map with fault trace and moisture note",
          "Two-year successful history of the standard pattern in adjacent panels",
          "Schedule pressure from low mill feed"
        ],
        "required_textual_manifestation": "The engineer explicitly cites the pattern's established track record as the main reason to keep it essentially unchanged, rather than weighing the new fault-trace data on its own terms, while acknowledging the new information exists.",
        "plausible_nonbias_interpretation": "A reasonable engineer might legitimately judge that a minor fault trace does not warrant redesign given strong historical performance and time constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "bias", "heuristic"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Overconfidence Bias",
        "decision_point": 2,
        "mechanism": "Overriding a specific technical recommendation (decking/emulsion substitution) based on generalized confidence from past experience with similar-looking ground, without re-checking the specific updated deviation and moisture data available at that moment",
        "affected_reasoning_operation": "Decision act: charge design and acceptance/rejection of the technician's recommendation",
        "evidence_available_at_time": [
          "Explosives technician's recommendation to deck and substitute emulsion in flagged holes",
          "Updated deviation survey and moisture logs for the flagged holes",
          "Engineer's personal history of successful fully columned ANFO charges in visually similar ground"
        ],
        "required_textual_manifestation": "The engineer describes overriding the technician's recommendation with confident reassurance based on personal track record, and does not describe re-examining the specific updated hole data before deciding.",
        "plausible_nonbias_interpretation": "The engineer may have genuinely and correctly judged the deviation readings as within an acceptable range based on legitimate technical criteria not fully articulated in the interview.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence bias", "bias", "miscalibration"]
      },
      {
        "instance_id": "cb_01",
        "bias": "Experience Bias",
        "decision_point": 4,
        "mechanism": "Attributing the post-blast overbreak outcome primarily to a remembered pattern from a previous mine site, and recommending that prior fix, while not incorporating the current round's own site-specific deviation and moisture data into the diagnosis",
        "affected_reasoning_operation": "Causal attribution and recommendation act: diagnosing the cause of overbreak and proposing next-round design changes",
        "evidence_available_at_time": [
          "Post-blast survey showing localized overbreak and coarse fragmentation in the fault-affected section",
          "Current round's deviation survey and moisture logs from Phases 1 and 2",
          "Engineer's recollection of a similar-looking overbreak pattern and fix from a previous mine"
        ],
        "required_textual_manifestation": "The engineer explains the cause and proposed fix mainly by reference to the prior mine's similar situation, without describing an examination of the current round's own instrumentation data as part of that diagnosis.",
        "plausible_nonbias_interpretation": "Pattern-matching to prior fault-zone incidents is a legitimate and often efficient diagnostic heuristic in blast engineering, especially under time constraints before a formal review.",
        "strength": "subtle",
        "do_not_make_explicit": ["experience bias", "bias", "overgeneralization"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "NONE",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is a biased-condition scenario with no paired control specified."
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
      "Confirm exactly 4 decision points appear, with Decision Point 3 free of intended bias instances.",
      "Confirm exactly one instance each of Experience Bias, Status quo bias, and Overconfidence Bias appears, at the assigned decision points only.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the interview text.",
      "Confirm each instance has a plausible non-bias interpretation available in the surrounding narrative.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals for each decision point.",
      "Confirm final word count falls within 1,215-1,485 words.",
      "Confirm consequences (overbreak, vibration spike) do not explicitly confirm or deny bias, remaining consistent with routine operational variance."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Experience Bias",
        "occurrences": 1,
        "mechanism_constraint": "Manifest only as post-blast causal attribution to a remembered prior-mine pattern, discounting current site-specific instrumentation"
      },
      {
        "bias": "Status quo bias",
        "occurrences": 1,
        "mechanism_constraint": "Manifest only as retention of the established blast pattern against new geotechnical information at Decision Point 1"
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": "Manifest only as overriding a specific technician recommendation on charging without re-verifying updated hole data"
      }
    ],
    "target_bias_names": ["Experience Bias", "Status quo bias", "Overconfidence Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Experience Bias", "requested_occurrences": 1},
      {"bias": "Status quo bias", "requested_occurrences": 1},
      {"bias": "Overconfidence Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_02", "bias": "Status quo bias"},
      {"instance_id": "cb_03", "bias": "Overconfidence Bias"},
      {"instance_id": "cb_01", "bias": "Experience Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_02", "bias": "Status quo bias", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Overconfidence Bias", "decision_point": 2},
      {"instance_id": "cb_01", "bias": "Experience Bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_02",
        "bias": "Status quo bias",
        "mechanism": "Retaining the established burden/spacing pattern over adapting to a newly mapped fault trace, on grounds of historical track record",
        "affected_reasoning_operation": "Evidence-selection and decision act on pattern redesign",
        "evidence_source": "Geologist's updated fracture map versus two-year pattern performance history",
        "distinctiveness_requirement": "Must be tied specifically to the pattern-retention decision at Decision Point 1, not repeated as a general attitude elsewhere"
      },
      {
        "instance_id": "cb_03",
        "bias": "Overconfidence Bias",
        "mechanism": "Overriding technician's decking/emulsion recommendation based on generalized personal track record rather than re-checking specific updated hole data",
        "affected_reasoning_operation": "Charge-design decision act and evaluation of technician's recommendation",
        "evidence_source": "Updated deviation survey and moisture logs versus engineer's personal experience with similar-looking ground",
        "distinctiveness_requirement": "Must be tied specifically to the charging override at Decision Point 2, distinct in evidence source and moment from the Decision Point 1 pattern decision"
      },
      {
        "instance_id": "cb_01",
        "bias": "Experience Bias",
        "mechanism": "Attributing post-blast overbreak to a remembered prior-mine pattern and recommending its fix without incorporating current round's own instrumentation data",
        "affected_reasoning_operation": "Causal attribution and recommendation act during post-blast evaluation",
        "evidence_source": "Post-blast survey and current round's deviation/moisture logs versus recollection of a prior mine's similar incident",
        "distinctiveness_requirement": "Must be tied specifically to the Decision Point 4 diagnosis/recommendation act, distinct in timing and evidence from the Decision Point 1 and 2 instances"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_02", "bias": "Status quo bias", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Overconfidence Bias", "strength": "subtle"},
      {"instance_id": "cb_01", "bias": "Experience Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": "NONE",
    "counterfactual_variable": {
      "name": "NONE",
      "original_state": "NONE",
      "changed_state": "NONE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Biased_3",
    "domain_id": "MU",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences distributed one-per-bias across three of the four decision points, chosen for mechanism fit: Status quo bias at the pattern-approval decision (DP1), Overconfidence Bias at the charging-override decision (DP2), and Experience Bias at the post-blast causal-attribution decision (DP4). Decision Point 3 (vibration/timing) was deliberately left bias-free to preserve narrative realism and avoid bias clustering, since no manifest entry required more than one occurrence for any bias.",
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
        "segment_type": "objective_and_constraint_prioritization",
        "raw_interview_anchor": "The objective was straightforward: get the round fired on schedule, keep fragmentation good enough for the mill, and stay inside our PPV limits near the shaft.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This states operational objectives and constraints without expressing a hidden bias mechanism."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "pattern_design_decision",
        "raw_interview_anchor": "Mostly time and track record. That pattern's fired dozens of rounds in similar ground without a hiccup, so redesigning burden and spacing for a fault trace that geology themselves called minor felt like it would cost us a day we didn't have.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "The participant retains the established burden-and-spacing pattern despite new fault-trace information, relying on its historical track record."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "charging_method_decision",
        "raw_interview_anchor": "I've used full ANFO columns in ground that looked rougher than this and it worked out fine, so I told the crew we'd run it as planned.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The participant overrides the technician's decking and emulsion recommendation based on generalized prior experience without rechecking current hole data."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "timing_and_vibration_decision",
        "raw_interview_anchor": "I compared the fragmentation trade-off against the vibration risk directly and went with the longer sequence on the shaft-facing side.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The decision explicitly weighs current PPV data against fragmentation trade-offs and has no hidden manifest instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "data_based_decision_justification",
        "raw_interview_anchor": "We had current numbers right in front of us — actual PPV readings, not just a general sense of things.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a data-based explanation for why the timing decision felt resolved and contains no hidden bias instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "post_blast_causal_diagnosis",
        "raw_interview_anchor": "It reminded me a lot of a panel I worked years ago at a different site — same kind of localized fault, same overbreak signature. There, the fix was tightening the pattern and adjusting timing specifically through that corridor, and it worked well. So that's what I recommended here.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant attributes the outcome to a remembered prior-mine pattern and recommends its fix without first incorporating current instrumentation."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
