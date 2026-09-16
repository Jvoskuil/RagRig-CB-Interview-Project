You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Blind to experimental condition and benchmark hypothesis. The transcript was evaluated strictly for affirmatively evidenced cognitive bias mechanisms in the participant's reasoning and decisions. Professional heuristics, time pressure, and bounded rational adaptations were considered as alternative explanations."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive shortcut in which judgments of frequency, probability, or risk are influenced by the ease with which relevant instances or outcomes are brought to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Pre-firing pattern design after geology fault flag",
      "decision_point_description": "Whether to modify the standard blast pattern or obtain additional geotechnical verification after geology flagged a minor fault trace in part of the panel.",
      "affected_reasoning_operation": "Risk estimation and pattern design decision",
      "bias_specific_mechanism": "The participant's risk estimate was dominated by readily recalled past firings of the same pattern in ground he treated as similar. These accessible successful outcomes became a substitute for examining the specific risk introduced by the current fault trace, reducing his felt need to seek geotechnical verification or alter the pattern.",
      "manifestation_in_interview": "The participant retained the standard 2.7 by 3.1 burden and spacing pattern rather than redesigning it; he considered additional geotechnical verification briefly but judged it unjustified based primarily on the pattern's track record.",
      "effect_on_reasoning_or_decision": "The decision preserved the standard pattern and only added minor stemming adjustment as a hedge, leaving the fault-corridor design essentially unchanged without current site-specific verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly time and track record. That pattern's fired dozens of rounds in similar ground without a hiccup, so redesigning burden and spacing for a fault trace that geology themselves called minor felt like it would cost us a day we didn't have, for a problem that historically hasn't caused us grief in that rock.",
          "evidence_explanation": "This shows the participant's risk judgment was anchored to a mentally available sample of successful prior rounds rather than to the specific fault-related risk signal."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It came up briefly, yeah. But honestly, given how well that pattern's performed, I didn't see it as justified. We tightened the stemming slightly on that side as a small hedge, but kept the design essentially as-is.",
          "evidence_explanation": "This demonstrates that the accessible record of prior performance directly suppressed further information-seeking and design change."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. Without that history to lean on, I'd likely have wanted the extra geotech pass before committing.",
          "evidence_explanation": "This counterfactual statement reinforces that the history of prior rounds, rather than current fault-specific information, was the dominant factor in the pattern decision."
        }
      ],
      "correction_or_counterevidence": "Geology had classified the structure as 'minor,' schedule and mill-feed pressure created a legitimate incentive to avoid delay, and the participant added a stemming hedge. These factors mean the reliance on history may have been partially bounded-rational rather than purely biased, which is why confidence is low.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context. The classification relies on established general cognitive-science knowledge of the availability heuristic rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive shortcut in which judgments of frequency, probability, or risk are influenced by the ease with which relevant instances or outcomes are brought to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Charging decision for wet and deviated blast holes",
      "decision_point_description": "Whether to accept the explosives technician's recommendation to deck the affected holes and use emulsion, or to proceed with the standard full ANFO charge across the panel.",
      "affected_reasoning_operation": "Risk assessment and charging method decision",
      "bias_specific_mechanism": "When the current holes were flagged as wet and deviated, the participant retrieved vivid remembered instances in which similar-looking holes had been charged with full ANFO columns and produced acceptable outcomes. The ease and concreteness of those recollections substituted for analysis of the specific moisture, deviation, and ground-control readings in the current round.",
      "manifestation_in_interview": "The participant rejected the technician's decking and emulsion recommendation and instructed the crew to run the standard full ANFO charge as planned.",
      "effect_on_reasoning_or_decision": "The affected fault-section holes were charged with the standard ANFO column rather than being decked or weighted more conservatively, despite the technician's specific warning.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've charged plenty of holes that looked like that — a bit wet, slightly off on deviation — and it's never been a real problem when the surrounding rock was competent. I've used full ANFO columns in ground that looked rougher than this and it worked out fine, so I told the crew we'd run it as planned.",
          "evidence_explanation": "This is a direct expression of the availability heuristic: remembered past successes with similar-looking holes dominated the participant's judgment of the current risk."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not in detail, no. I'd seen the technician's note and I trusted my read of the situation from experience more than I felt I needed to re-pull the log line by line.",
          "evidence_explanation": "This demonstrates that the participant substituted his experience-based read for the current hole-specific data, which is the operational distortion produced by the availability heuristic."
        }
      ],
      "correction_or_counterevidence": "The alternative of decking and emulsion would have consumed firing-window time, and using accumulated operational experience is often a legitimate expert heuristic. However, the participant's decision was made without detailed examination of the specific deviation or moisture readings, reducing the extent to which this can be considered purely rational expert judgment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context. The classification relies on established general cognitive-science knowledge of the availability heuristic rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": ["representativeness bias", "representative heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive shortcut in which probability, causal category membership, or similarity is judged by the degree to which a case resembles a prototype or remembered example, often at the expense of specific diagnostic data.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-blast diagnosis of overbreak and coarse fragmentation",
      "decision_point_description": "Determining the cause of overbreak and coarse fragmentation in the fault section and recommending corrective action to the mine manager.",
      "affected_reasoning_operation": "Causal attribution and corrective recommendation",
      "bias_specific_mechanism": "The participant judged the current post-blast outcome by its similarity to a single remembered panel from a different site. Because the surface features looked alike—localized fault and overbreak signature—he transferred the prior site's causal story and remedy to the present case without initially testing that analogy against the current round's own deviation, moisture, or instrumentation data.",
      "manifestation_in_interview": "The participant recommended tightening the pattern and adjusting timing through the fault corridor based on a remembered prior panel, while not closely reviewing this round's logs or bringing geology in before the recommendation.",
      "effect_on_reasoning_or_decision": "The causal explanation and corrective action were imported from a prior incident, and the current round's specific data were not used to confirm or falsify the analogy before the recommendation went forward.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It reminded me a lot of a panel I worked years ago at a different site — same kind of localized fault, same overbreak signature. There, the fix was tightening the pattern and adjusting timing specifically through that corridor, and it worked well. So that's what I recommended here.",
          "evidence_explanation": "This shows a similarity-based transfer from a remembered prior case as the primary basis for diagnosis and recommendation, which is the core operation of the representativeness heuristic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not closely — the pattern matched what I'd seen before closely enough that I was fairly confident in the read.",
          "evidence_explanation": "This confirms that perceived similarity to the prior case, rather than current log analysis, drove the diagnosis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd pulled this round's own logs first, side by side with the old site's data, instead of going mostly off memory — that might've told a different story. I'm not sure it would have, but I didn't really test it that way.",
          "evidence_explanation": "The participant's own reflection indicates that the similarity-based diagnosis was not tested against current data, supporting the presence of the representativeness heuristic."
        }
      ],
      "correction_or_counterevidence": "The participant framed the recommendation as an actionable immediate response for the mine manager, and analogy to prior experienced ground conditions can be a legitimate expert diagnostic strategy. He also acknowledged geology review was a likely next step, suggesting the diagnosis was not entirely closed.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context. The classification relies on established general cognitive-science knowledge of the representativeness heuristic rather than retrieved evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence effect",
      "alternative_labels": ["overconfidence bias", "overprecision"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Pre-firing pattern design after geology fault flag",
      "supporting_interview_quote": "But honestly, given how well that pattern's performed, I didn't see it as justified.",
      "plausible_mechanism": "Repeated success with the standard pattern may have produced an inflated subjective confidence that it would accommodate the fault trace, reducing the perceived need for further verification.",
      "why_not_identified": "The available transcript evidence more directly supports an availability heuristic mechanism, and a distinct miscalibrated probability estimate is not sufficiently separable from that availability effect in this episode."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": ["myside bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-blast diagnosis of overbreak and coarse fragmentation",
      "supporting_interview_quote": "Not closely — the pattern matched what I'd seen before closely enough that I was fairly confident in the read.",
      "plausible_mechanism": "The participant may have favored the prior old-site diagnosis and failed to seek out current log data that could disconfirm the analogy.",
      "why_not_identified": "The transcript does not clearly show an active search for confirmatory evidence or biased weighting of mixed evidence; the diagnostic shortcut is better explained by the representativeness heuristic."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific passages were supplied in the RAG retrieval context, so corpus support fields are empty and classification relies on established general cognitive-science knowledge rather than retrieved evidence.",
    "The interview captures self-reported reasoning, which may reflect post-hoc rationalization rather than perfectly accurate online cognitive processing.",
    "Several decisions also have legitimate professional, operational, and time-pressure explanations, so confidence levels are moderate or low rather than high."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Biased_3_Gemini_off",
  "interview_id": "MU_Biased_3",
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
