<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. Before we start, just to confirm—this is a confidential debrief for our internal process-improvement study, not part of any disciplinary or compliance record. Is that okay with you?

Participant: Yes, that's fine. I've done these before.

Interviewer: Great. Can you tell me your role and what your responsibilities were during this incident?

Participant: I'm the Environmental/Safety Compliance Officer at the plant. I own air permit compliance for the whole site, including the Solvent Recovery Unit in Building 3. During this event my job was to figure out what actually happened, decide what needed to be reported to the state, and keep production moving if I could justify it.

Interviewer: Walk me through what happened, starting from the beginning.

Participant: Sure. It started at 6:40 in the morning—a VOC sensor near the SRU tripped above the action threshold. Nothing else had happened yet, no complaints, nothing. We'd had two drift-related false alarms on that same sensor array in the past month, so that was fresh in my mind. My first read was that it was probably drift again. About half an hour later, before I'd done much else, the hotline got a call from someone near the fenceline complaining about a chemical smell. That obviously raised the stakes, so I sent a technician out with a handheld VOC meter. The readings he brought back were elevated, but not dramatically—kind of a grey zone, not clearly over the permit limit. We were also mid-batch on a large customer order due in two days, so a shutdown wasn't something anyone wanted to trigger without good reason. I decided to hold off on pulling the full continuous emissions monitoring data and just kept an eye on it with recalibration scheduled. That stayed the plan for about two days, until a contractor doing unrelated maintenance work noticed a data logger showing sustained high readings during that exact window. That's when I really dug in. I pulled the maintenance history, and separately, I was thinking about a valve failure that happened at our sister plant in Ohio—I'd just seen a corporate webinar on it two weeks earlier, big fine, made the local news. So initially my draft notes on the incident leaned toward a valve issue. Eventually the teardown showed it was actually a worn gasket seal, which is honestly the most common cause we've had here over the last few years. Once that was confirmed, I had to decide how to calculate the emissions and whether it crossed into reportable territory, given the permit's 24-hour notification clock and our production deadline.

Interviewer: Let's reconstruct that timeline a bit more precisely. What did you do in the first thirty minutes after the alarm?

Participant: I checked the alarm log, saw the drift history, and made a quick call that we'd treat it as probable drift and schedule recalibration for later in the shift. I didn't dispatch the field team immediately—that came after the odor complaint.

Interviewer: And between the odor complaint and the teardown, what new information came in, and when?

Participant: The field readings came in that same morning—inconclusive, as I said. Then nothing new for about two days until the contractor flagged the data logger. That's really what forced a fuller investigation.

Interviewer: When did the teardown findings become available relative to your draft report?

Participant: The teardown happened after I'd already started drafting my incident summary and had briefed the plant manager verbally on what I thought we were dealing with.

Interviewer: Let's go back to that very first decision—treating the alarm as probable drift. What cues drove that?

Participant: Mainly the history. We'd had two false alarms in a month from that same array, so drift felt like the obvious explanation. It was the first thing that made sense, and honestly once I had that in my head, the readings the technician brought back later didn't strike me as clearly contradicting it—they were ambiguous enough that I read them as consistent with drift rather than as a red flag on their own.

Interviewer: Did you consider the possibility of a real release before the odor complaint came in?

Participant: Not seriously, no. There was no other reason to at that point.

Interviewer: What information sources did you consult before deciding whether to pull the full CEM dataset, and which did you set aside?

Participant: I looked at the handheld readings and the recent drift history. I didn't pull the full continuous emissions monitoring data at that stage. I knew that was the more thorough option—it would have given us a much clearer picture—but our analyst time is tight, we're basically a two-person team, and a full data pull plus lab confirmation would have taken hours we didn't have with the production deadline looming. If it had come back showing an exceedance, we'd have been on a 24-hour reporting clock, which would have complicated the week considerably. So I told myself the grey-zone readings weren't conclusive enough to justify pulling everyone off other work yet.

Interviewer: What alternatives did you consider when drafting the incident narrative, and why did the Ohio incident come to mind?

Participant: I thought about gasket seep, which is genuinely our most common issue based on the maintenance log—three years of data point that way. But the Ohio valve failure was just very present for me. I'd sat through that whole webinar, seen the numbers, the fine, the news coverage. So when I started framing the draft report and thinking about where to send the inspection team first, the valve scenario is what I wrote down and what I asked maintenance to check first, even before the gasket line was inspected.

Interviewer: What was your basis for choosing the exceedance calculation methodology at the end?

Participant: Once the gasket was confirmed, I had two methodologies I could reasonably apply, and they gave different exceedance outcomes. I went through the permit language and the historical way we'd calculated similar events, and picked the one I felt was most defensible given how our last few audits went.

Interviewer: How much time pressure did you feel at each of these moments?

Participant: Constant, honestly. The production deadline was hanging over almost every decision, from the initial triage to whether to escalate.

Interviewer: How confident were you in your interpretation at each stage, and what would have made you less confident?

Participant: Early on, fairly confident it was drift—maybe too confident, looking back. By the time the data logger turned up, I was much less sure of anything. If the field readings that first morning had been sharper, either clearly high or clearly normal, that would have changed how much weight I put on the drift explanation.

Interviewer: If the sensor drift history hadn't existed, would your initial triage have gone differently?

Participant: Probably. Without that history I think I'd have dispatched the field team right away instead of waiting.

Interviewer: If you hadn't attended the webinar about the Ohio incident, do you think your investigation would have started elsewhere?

Participant: That's a fair question. I'd like to think the maintenance log would have driven it regardless, but I honestly can't rule out that the webinar shaped where I looked first.

Interviewer: Looking back, what single piece of information, if available earlier, would have most changed your approach?

Participant: The data logger readings from that first day. If I'd seen those immediately instead of two days later, I think the whole sequence would have moved faster and with less back-and-forth.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Biased_3",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Environmental/Safety Compliance Officer (Manufacturing Plant)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Fenceline Alarm: VOC Exceedance Investigation at the Solvent Recovery Unit",
    "scenario_summary_internal": "A specialty chemicals plant's Solvent Recovery Unit (SRU) in Building 3 triggers a VOC sensor alarm coinciding with a community odor complaint. The Environmental/Safety Compliance Officer must triage the alarm, decide how aggressively to investigate, construct a causal narrative for the incident, and determine whether/how to report to the state agency, all under production-deadline and budget pressure and against a backdrop of recent sensor false positives and a recently publicized valve-failure incident at a sister plant.",
    "occupational_realism": {
      "objective": "Determine the true cause of the anomalous VOC reading and odor complaint, decide on corrective action, and satisfy Title V air permit reporting obligations without triggering an unnecessary production shutdown.",
      "setting": "Mid-size specialty chemicals/coatings manufacturing plant; Building 3 houses the Solvent Recovery Unit (SRU) subject to a state Title V air permit with VOC concentration and mass-emission limits and fenceline monitoring.",
      "constraints": [
        "Large customer production order due in 48 hours",
        "Environmental team is short-staffed (officer plus one part-time technician)",
        "Full CEM data pull and independent lab confirmation take analyst hours and may delay production",
        "Permit requires self-report of confirmed exceedances within 24 hours",
        "Corporate is mid-renewal on the Title V permit and sensitive to regulatory attention",
        "Sensor array has a documented history of drift-related false alarms in the past month"
      ],
      "stakeholders": [
        "Plant Manager",
        "Production Supervisor",
        "Corporate EHS Director",
        "Maintenance Technician",
        "State Environmental Agency inspector",
        "Local residents near the fenceline"
      ],
      "technical_terms_to_use": [
        "VOC (volatile organic compound)",
        "action threshold",
        "fenceline monitoring",
        "continuous emissions monitoring (CEM)",
        "Title V permit",
        "self-report",
        "reportable exceedance",
        "solvent recovery unit (SRU)",
        "sensor drift/recalibration",
        "gasket seep",
        "corrective action plan"
      ],
      "technical_terms_to_avoid": [
        "primacy effect",
        "ostrich effect",
        "imaginability bias",
        "cognitive bias",
        "anchoring",
        "availability heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "VOC sensor near SRU triggers alarm above action threshold at 6:40am",
          "Sensor array drifted twice in the past month causing false positives",
          "No community complaints yet logged at time of alarm"
        ],
        "new_information_after_decision": [
          "Community hotline receives an odor complaint near the fenceline at 7:15am",
          "Field team's handheld VOC readings are elevated but ambiguous relative to the initial hypothesis"
        ],
        "alternatives": [
          "Classify the alarm as probable sensor drift and schedule routine recalibration during day shift",
          "Treat the alarm as a potential real release and immediately dispatch a field team with protocol-level urgency"
        ],
        "intended_action": "Officer forms an initial 'probably drift' judgment from a brief review of the alarm log before other evidence arrives, and this first impression frames how subsequent, more ambiguous field data is interpreted."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary field VOC readings fall in a 'grey zone' near but not conclusively over the permit limit",
          "Production is mid-batch; a partial shutdown for full testing would cost roughly $40,000/day",
          "A full CEM data pull and independent lab confirmation could reveal a reportable exceedance requiring self-report within 24 hours"
        ],
        "new_information_after_decision": [
          "Two days later, a contractor reviewing an unrelated maintenance log flags a data logger showing sustained high VOC readings during the alarm window"
        ],
        "alternatives": [
          "Request an immediate full CEM data download and independent lab confirmation before proceeding",
          "Defer deeper analysis, citing inconclusive grey-zone readings, and proceed with routine recalibration and continued monitoring"
        ],
        "intended_action": "Officer defers requesting the full CEM dataset and confirmatory lab testing, citing workload and inconclusiveness, thereby avoiding the analysis most likely to confirm a reportable exceedance."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three-year maintenance log shows gasket seep is the statistically most common cause of past minor VOC events at this site",
          "Officer attended a corporate webinar two weeks earlier detailing a dramatic valve failure at a sister plant in Ohio that caused a $2M fine and local news coverage",
          "No teardown or physical inspection of the SRU valve or gaskets has yet occurred"
        ],
        "new_information_after_decision": [
          "Maintenance teardown later reveals a worn gasket seal, not a valve failure"
        ],
        "alternatives": [
          "Prioritize investigating gasket seep as the most likely cause based on site history",
          "Frame the initial investigation and draft incident report around a valve-failure scenario resembling the Ohio incident"
        ],
        "intended_action": "Officer's causal narrative for the draft report disproportionately features the vivid, recently recalled Ohio valve-failure scenario, directing inspection resources toward the valve before the statistically more probable gasket cause is checked."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Gasket seal wear is confirmed as the physical cause",
          "Cumulative emissions data now available, with exceedance status depending on which calculation methodology is applied",
          "Permit requires notification within 24 hours of a confirmed exceedance",
          "Production order deadline is two days away"
        ],
        "new_information_after_decision": [
          "Outcome (whether the agency ultimately cites the plant, and whether repair timing avoided further release) is learned only after the officer's decision"
        ],
        "alternatives": [
          "Apply the conservative exceedance calculation, self-report immediately, and recommend temporary SRU shutdown for repair",
          "Apply a less conservative calculation methodology that keeps reported emissions under threshold, avoid mandatory reporting, and schedule repair during the next planned maintenance window"
        ],
        "intended_action": "Officer weighs the two calculation methodologies and permit language on their merits; this decision point is left free of intended bias instrumentation so it functions as a genuine, undetermined judgment call."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew and what your objective was when the alarm first came in.",
        "What was your role and responsibility once the sensor alarm and the odor complaint both surfaced?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do in the first 30 minutes?",
        "What new information came in over the following two days, and when did you learn it?",
        "At what point did the maintenance teardown findings become available?"
      ],
      "decision_point_probes": [
        "What cues made you initially lean toward sensor drift rather than a real release?",
        "What information sources did you consult before deciding whether to pull the full CEM dataset, and which did you set aside?",
        "What alternatives did you consider when drafting the incident narrative, and why did the Ohio incident come to mind?",
        "What was your basis for choosing an exceedance calculation methodology, and how did the permit deadline factor in?",
        "How much time pressure did you feel at each of these moments, and how did that shape what evidence you gathered?",
        "How confident were you in your interpretation at each stage, and what would have made you less confident?"
      ],
      "closing_hypotheticals": [
        "If the sensor drift history hadn't existed, would your initial triage have gone differently?",
        "If you'd had an extra analyst that week, would you have pulled the full CEM data sooner?",
        "If you hadn't attended the corporate webinar about the Ohio incident, do you think your investigation would have started elsewhere?",
        "Looking back, what single piece of information, if available earlier, would have most changed your approach?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "decision_point": 1,
        "mechanism": "The officer's first plausible explanation (sensor drift, formed from a brief alarm-log review) is given outsized weight and colors interpretation of the ambiguous field readings that arrive afterward, rather than those later readings being weighed on their own merits.",
        "affected_reasoning_operation": "Initial hypothesis formation and subsequent evidence interpretation",
        "evidence_available_at_time": [
          "Alarm log showing recent drift-related false positives",
          "No complaints yet logged",
          "Absence of confirmatory field data at the moment of triage"
        ],
        "required_textual_manifestation": "Officer explicitly states the drift explanation was adopted within minutes of the alarm and that later ambiguous field readings were read through that initial lens ('I already figured it was probably drift again, so...') rather than assessed independently.",
        "plausible_nonbias_interpretation": "Given a genuine base rate of two prior false alarms in one month, treating drift as the leading hypothesis is a reasonable, experience-based heuristic, not necessarily bias.",
        "strength": "subtle",
        "do_not_make_explicit": ["primacy effect", "anchoring", "first impression bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Ostrich effect",
        "decision_point": 2,
        "mechanism": "Officer avoids requesting the full CEM data pull and lab confirmation specifically because that information is likely to confirm a costly, reportable exceedance, choosing inconclusive grey-zone readings as sufficient grounds to defer.",
        "affected_reasoning_operation": "Evidence-seeking / information avoidance under threat of unwelcome confirmation",
        "evidence_available_at_time": [
          "Grey-zone field VOC readings",
          "Awareness that a full CEM download could reveal a reportable exceedance",
          "Known cost of partial shutdown (~$40,000/day) and reporting consequences"
        ],
        "required_textual_manifestation": "Officer acknowledges knowing the full data pull was the appropriate next step but describes consciously delaying it, citing workload or inconclusiveness, in a way that reveals awareness the deferral was tied to not wanting to find a problem.",
        "plausible_nonbias_interpretation": "With a short-staffed team and a genuinely ambiguous reading, deferring a resource-intensive full analysis pending a second checkpoint could reflect ordinary prioritization under workload constraints.",
        "strength": "moderate",
        "do_not_make_explicit": ["ostrich effect", "information avoidance", "willful blindness"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Imaginability Bias",
        "decision_point": 3,
        "mechanism": "Officer's causal narrative construction is disproportionately shaped by the vivid, recently recalled Ohio valve-failure incident rather than by the statistically more common gasket-seep cause documented in three years of maintenance logs.",
        "affected_reasoning_operation": "Causal attribution / hypothesis prioritization for the draft incident report",
        "evidence_available_at_time": [
          "Three-year maintenance log showing gasket seep as the most frequent past cause",
          "Recent, vivid recollection of a dramatic sister-plant valve failure from a corporate webinar",
          "No physical inspection yet performed"
        ],
        "required_textual_manifestation": "Officer explains that the Ohio incident came to mind readily and shaped the initial framing of the report and inspection priorities, described in terms that emphasize how memorable/vivid that comparison was, ahead of statistically grounded reasoning.",
        "plausible_nonbias_interpretation": "Investigating the valve first could be justified as prudent worst-case-first triage given catastrophic consequences, independent of vividness.",
        "strength": "subtle",
        "do_not_make_explicit": ["imaginability bias", "availability heuristic", "vividness effect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no paired control scenario is specified for this generation task."
    },
    "counterfactual_specification": {
      "causal_variable": "Officer's recent exposure to the vivid sister-plant (Ohio) valve-failure narrative prior to the incident (autoselected as the causal variable best suited to a future counterfactual pairing; inactive for the current 'biased' condition)",
      "original_state": "Officer attended a corporate webinar two weeks before the incident describing a dramatic, costly valve failure at a sister plant",
      "counterfactual_state": "Officer had no recent exposure to any vivid comparable incident narrative before the SRU alarm",
      "variables_to_hold_constant": [
        "Sensor alarm timing and drift history",
        "Community odor complaint",
        "Production deadline and shutdown cost figures",
        "Maintenance log base rates for gasket seep vs. valve failure",
        "Number and sequencing of decision points"
      ],
      "expected_causal_difference": "Without the vivid Ohio exposure, the officer's causal narrative at decision point 3 would be expected to default to the statistically dominant gasket-seep hypothesis rather than the valve-failure hypothesis.",
      "causal_test_question": "Does removing the officer's recent exposure to a vivid comparable incident change which cause is prioritized in the initial causal narrative at decision point 3?"
    },
    "generation_checks": [
      "Confirm exactly one instance each of Primacy Effect, Ostrich effect, and Imaginability Bias appears, tied to decision points 1, 2, and 3 respectively.",
      "Confirm decision point 4 contains no intended bias instrumentation.",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text.",
      "Confirm each instance has a distinct evidentiary basis and reasoning operation from the others.",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and probe coverage without repetitive exposition.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm consequences at each decision point do not mechanically prove bias (e.g., the gasket cause being correct does not itself prove the Ohio-narrative emphasis was biased)."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Imaginability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as disproportionate causal-narrative weighting toward a vivid, recently recalled comparable incident over a statistically dominant base-rate cause, at decision point 3 only."
      },
      {
        "bias": "Ostrich effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as conscious deferral of an information-gathering step (full CEM pull/lab confirmation) motivated by avoidance of an unwelcome confirmatory finding, at decision point 2 only."
      },
      {
        "bias": "Primacy Effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an early-formed hypothesis anchoring interpretation of subsequently received, more ambiguous evidence, at decision point 1 only."
      }
    ],
    "target_bias_names": ["Imaginability Bias", "Ostrich effect", "Primacy Effect"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Imaginability Bias", "requested_occurrences": 1 },
      { "bias": "Ostrich effect", "requested_occurrences": 1 },
      { "bias": "Primacy Effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Primacy Effect" },
      { "instance_id": "cb_02", "bias": "Ostrich effect" },
      { "instance_id": "cb_03", "bias": "Imaginability Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Ostrich effect", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Imaginability Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "mechanism": "Early alarm-log-based drift hypothesis anchors interpretation of subsequent ambiguous field readings",
        "affected_reasoning_operation": "Initial hypothesis formation / subsequent evidence interpretation",
        "evidence_source": "Alarm log and sensor drift history reviewed within minutes of the alarm",
        "distinctiveness_requirement": "Distinct from cb_03 by occurring at first evidence encounter (drift history) rather than at narrative construction from a recalled external incident"
      },
      {
        "instance_id": "cb_02",
        "bias": "Ostrich effect",
        "mechanism": "Deliberate deferral of full CEM data pull/lab confirmation to avoid confirming a costly reportable exceedance",
        "affected_reasoning_operation": "Information-seeking behavior under threat of unwelcome confirmation",
        "evidence_source": "Grey-zone field VOC readings and known cost/reporting consequences of a confirmed exceedance",
        "distinctiveness_requirement": "Distinct from cb_01 and cb_03 in involving active avoidance of an available information-gathering action rather than misweighting evidence already in hand"
      },
      {
        "instance_id": "cb_03",
        "bias": "Imaginability Bias",
        "mechanism": "Vivid, recently recalled sister-plant valve-failure incident disproportionately shapes causal attribution over the statistically dominant gasket-seep base rate",
        "affected_reasoning_operation": "Causal attribution / hypothesis prioritization for incident narrative",
        "evidence_source": "Three-year maintenance log base rates versus recalled corporate webinar narrative",
        "distinctiveness_requirement": "Distinct from cb_01 by involving retrieval of an external, emotionally vivid memory to override base-rate statistical evidence, rather than anchoring on the first internally generated hypothesis"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Ostrich effect", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Imaginability Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Officer's recent exposure to a vivid comparable incident narrative (Ohio sister-plant valve failure) prior to causal-narrative construction",
      "original_state": "Officer attended a corporate webinar two weeks before the incident describing the Ohio valve failure",
      "changed_state": "Officer had no recent exposure to any vivid comparable incident narrative",
      "variables_to_hold_constant": [
        "Sensor alarm timing and drift history",
        "Community odor complaint",
        "Production deadline and shutdown cost figures",
        "Maintenance log base rates for gasket seep vs. valve failure",
        "Number and sequencing of decision points",
        "Difficulty level and word count target"
      ]
    },
    "scenario_id": "IP_Biased_3",
    "domain_id": "IP",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1, 2, 3) selected for mechanism fit and narrative realism; decision point 4 deliberately left free of intended bias instrumentation to serve as an undetermined control judgment within the same interview.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Setting, actors, and stakeholder roles",
      "Four-decision-point structure",
      "Difficulty level (challenging)",
      "Emotional tone and time-pressure framing",
      "Target word count range (1,215-1,485)"
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
        "segment_type": "role_and_objective",
        "raw_interview_anchor": "I own air permit compliance for the whole site... figure out what actually happened, decide what needed to be reported to the state, and keep production moving if I could justify it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states role responsibilities and operational objectives without a manifested hidden bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_hypothesis_and_evidence_interpretation",
        "raw_interview_anchor": "My first read was that it was probably drift again... once I had that in my head... I read them as consistent with drift rather than as a red flag on their own.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "The early drift hypothesis is explicitly described as shaping interpretation of later ambiguous handheld readings, matching the Primacy Effect instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "operational_constraint_and_shutdown_tradeoff",
        "raw_interview_anchor": "The readings he brought back were elevated, but not dramatically... We were also mid-batch on a large customer order due in two days, so a shutdown wasn't something anyone wanted to trigger without good reason.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This expresses ambiguous evidence and legitimate production constraints, but does not by itself establish a hidden bias mechanism."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "information_seeking_and_deferral",
        "raw_interview_anchor": "I decided to hold off on pulling the full continuous emissions monitoring data... If it had come back showing an exceedance, we'd have been on a 24-hour reporting clock... So I told myself the grey-zone readings weren't conclusive enough.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "The participant acknowledges the more diagnostic step and links deferral partly to the unwelcome reporting consequence, matching the Ostrich effect instance."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "causal_narrative_and_inspection_prioritization",
        "raw_interview_anchor": "Gasket seep... is genuinely our most common issue... But the Ohio valve failure was just very present for me... the valve scenario is what I wrote down and what I asked maintenance to check first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "A vivid recent valve-failure narrative displaced the statistically common gasket explanation in the initial causal framing, matching Imaginability Bias."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "reporting_methodology_decision",
        "raw_interview_anchor": "Once the gasket was confirmed, I had two methodologies I could reasonably apply... picked the one I felt was most defensible given how our last few audits went.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification deliberately leaves decision point 4 as an undetermined judgment call without intended bias instrumentation."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "retrospective_uncertainty_and_decision_calibration",
        "raw_interview_anchor": "Early on, fairly confident it was drift—maybe too confident... If the field readings that first morning had been sharper... that would have changed how much weight I put on the drift explanation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is retrospective confidence calibration and a counterfactual about evidence sharpness; it does not introduce a separate hidden instance."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
