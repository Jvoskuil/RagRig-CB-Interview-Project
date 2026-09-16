You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Single-participant confidential debrief transcript reviewed for cognitive biases in reasoning and decision-making; the attributed reasoner is the Participant unless otherwise noted."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["biased assimilation", "selective interpretation"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to search for, weigh, interpret, or recall information in ways that support an existing belief or hypothesis, while insufficiently considering or discounting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial VOC alarm triage and interpretation of follow-up handheld readings",
      "decision_point_description": "Deciding whether to treat the alarm as probable drift and how to interpret the subsequent ambiguous handheld VOC readings.",
      "affected_reasoning_operation": "Hypothesis formation and evidence interpretation",
      "bias_specific_mechanism": "A recent history of false alarms made the drift explanation highly accessible and preferred; after that hypothesis was formed, ambiguous field readings were assimilated as consistent with drift rather than treated as neutral or potentially disconfirming.",
      "manifestation_in_interview": "The Participant reported that drift felt like the obvious explanation from the outset and that, once that explanation was in place, the later grey-zone handheld readings were interpreted as supporting drift rather than as a red flag.",
      "effect_on_reasoning_or_decision": "The initial alarm was not escalated with immediate field dispatch, and the later ambiguous readings did not substantially shift the Participant's working diagnosis toward further investigation at that stage.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd had two drift-related false alarms on that same sensor array in the past month, so that was fresh in my mind. My first read was that it was probably drift again.",
          "evidence_explanation": "This establishes that the initial hypothesis was formed quickly from recent memory of false alarms before other information was gathered."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I checked the alarm log, saw the drift history, and made a quick call that we'd treat it as probable drift and schedule recalibration for later in the shift. I didn't dispatch the field team immediately—that came after the odor complaint.",
          "evidence_explanation": "This shows the initial drift interpretation directly affected an early operational decision: delaying field deployment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once I had that in my head, the readings the technician brought back later didn't strike me as clearly contradicting it—they were ambiguous enough that I read them as consistent with drift rather than as a red flag on their own.",
          "evidence_explanation": "This is the core confirmation mechanism: ambiguous evidence was interpreted through the existing drift hypothesis rather than treated as a reason to reconsider it."
        }
      ],
      "correction_or_counterevidence": "Past false alarms on the same sensor array made the drift hypothesis plausible, so the initial interpretation was not necessarily unreasonable. The Participant later reopened the investigation and accepted the teardown result, and he also said sharper field readings would have changed how much weight he placed on the drift explanation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were available in the analysis context; the label and mechanism are drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments, probability estimates, or attention allocations are influenced by how easily examples come to mind, such as recent, vivid, or emotionally salient events, rather than by more systematic or base-rate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Incident-cause hypothesis generation and initial inspection priority after fuller investigation was triggered",
      "decision_point_description": "Deciding which failure mode to prioritize in the draft incident narrative and maintenance inspection after the data logger indicated sustained high readings.",
      "affected_reasoning_operation": "Hypothesis generation, causal priority judgment, and allocation of inspection attention",
      "bias_specific_mechanism": "A recent, vivid, emotionally salient example from a corporate webinar—the Ohio valve failure with a large fine and local news coverage—was highly available in memory; this salience influenced the Participant to prioritize the valve hypothesis over the locally more common gasket-seal failure despite the maintenance history.",
      "manifestation_in_interview": "The Participant acknowledged considering gasket seep as the most common local cause but said the Ohio valve failure was 'just very present' due to recent exposure; he then wrote the valve scenario into the draft report and asked maintenance to check it first.",
      "effect_on_reasoning_or_decision": "The initial draft incident notes leaned toward a valve issue, and maintenance inspection resources were directed first toward the valve rather than the gasket; the eventual teardown identified a worn gasket seal.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about gasket seep, which is genuinely our most common issue based on the maintenance log—three years of data point that way. But the Ohio valve failure was just very present for me. I'd sat through that whole webinar, seen the numbers, the fine, the news coverage.",
          "evidence_explanation": "This directly contrasts the local base-rate information with the recent, vivid example, and identifies the felt accessibility of the Ohio valve failure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So when I started framing the draft report and thinking about where to send the inspection team first, the valve scenario is what I wrote down and what I asked maintenance to check first, even before the gasket line was inspected.",
          "evidence_explanation": "This shows the availability-driven hypothesis translated into an actual priority decision: valve inspection before gasket inspection."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I honestly can't rule out that the webinar shaped where I looked first.",
          "evidence_explanation": "This is an explicit, self-aware uncertainty by the Participant that the webinar exposure influenced the initial direction of the investigation."
        }
      ],
      "correction_or_counterevidence": "The Participant did consider the local maintenance history indicating gasket seep was most common, and the subsequent teardown result was accepted and used as the basis for final emissions assessment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were available in the analysis context; the label and mechanism are drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "motivated reasoning",
      "alternative_labels": ["directional information avoidance", "motivated skepticism"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision not to pull the full continuous emissions monitoring data after inconclusive handheld readings",
      "supporting_interview_quote": "If it had come back showing an exceedance, we'd have been on a 24-hour reporting clock, which would have complicated the week considerably. So I told myself the grey-zone readings weren't conclusive enough to justify pulling everyone off other work yet.",
      "plausible_mechanism": "The Participant had outcome-relevant incentives to avoid confirming a reportable exceedance because of the reporting clock and production deadline; this may have led to motivated information avoidance or a stricter, motivated threshold for seeking disconfirming data.",
      "why_not_identified": "The transcript also supplies substantial non-bias explanations—resource constraints, a two-person analyst team, production time pressure, and ordinary uncertainty about grey-zone readings—so a distinct motivated-reasoning mechanism is plausible but not affirmatively separated from these structural and legitimate constraints."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper corpus was provided in the analysis context, so bias labels and mechanisms rely on general cognitive-science knowledge rather than on the specified RAG corpus.",
    "The transcript is self-reported and retrospective; classification therefore depends on the Participant's descriptions of reasoning, not on direct behavioral or process data.",
    "Several decisions occurred under resource constraints and production pressure, which can provide non-bias explanations for otherwise bias-like behavior."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Biased_3_Sonar_off",
  "interview_id": "IP_Biased_3",
  "system_prompt_id": "Sonar",
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
