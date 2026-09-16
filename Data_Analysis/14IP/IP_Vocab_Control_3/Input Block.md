<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a confidential process-improvement debrief, not part of any disciplinary record. Okay to proceed?

Participant: Yes, that's fine.

Interviewer: Can you describe your role and what you were responsible for during this incident?

Participant: I'm the Environmental/Safety Compliance Officer at the plant. I own air permit compliance site-wide, including the Solvent Recovery Unit in Building 3. My job here was to figure out what was actually happening, decide what needed to be reported under our Title V permit, and try to keep the production line moving if that could be justified.

Interviewer: Walk me through what happened.

Participant: At 6:40 in the morning, a VOC sensor near the SRU tripped above the action threshold. At that point there was nothing else—no complaints, no other data. We'd had two drift-related false alarms on that same sensor array in the past month, so I flagged that as relevant background, but I didn't want to just assume drift and move on. I sent a technician out with a handheld meter right away rather than waiting to see if anything else developed. About half an hour later, the hotline got a call about a chemical smell near the fenceline, which raised the stakes. The handheld readings came back elevated but in a grey zone—not clearly over the limit. We were also mid-batch on a large customer order due in two days, so an unnecessary shutdown wasn't something anyone wanted. I talked it through with the production supervisor and we agreed to tighten our sampling interval and schedule a full continuous emissions monitoring pull within a short, defined window rather than letting it drift indefinitely or shutting down that same morning. That held for about two days until a contractor doing unrelated maintenance work flagged a data logger showing sustained high readings during that exact alarm window. That's when we moved to a fuller investigation. I pulled the three-year maintenance history, which showed gasket seep as the most common cause of past VOC events here by a wide margin. I was also aware of a valve failure at our sister plant in Ohio a couple weeks earlier—big fine, local news, we'd covered it in a corporate webinar—but I didn't want that one dramatic case to drive where we looked first. I prioritized the gasket line based on the site's own history, and separately scheduled a quick, low-cost check of the valve as a precaution, given how bad a valve failure would be if it did happen. The teardown confirmed a worn gasket seal, consistent with our historical pattern. From there I had to decide how to calculate cumulative emissions, since the outcome affected whether we crossed into reportable territory under our 24-hour notification clock, with the production deadline two days out.

Interviewer: Let's reconstruct the timeline a bit more precisely. What did you do in the first thirty minutes?

Participant: I looked at the alarm log, noted the drift history, but didn't stop there—I dispatched the technician immediately to get independent field data rather than waiting to see if the alarm cleared on its own.

Interviewer: And between the odor complaint and the teardown?

Participant: The handheld readings came in that same morning. Then it was about two days of tighter monitoring until the contractor flagged the data logger, which is what triggered the deeper investigation.

Interviewer: When did the teardown findings come in relative to your reporting decision?

Participant: Right before. Once the gasket was confirmed, I moved straight into the emissions calculation question.

Interviewer: Going back to that first decision—how did you decide not to just classify it as drift outright?

Participant: The drift history was real, and it made drift a reasonable starting hypothesis, but two false alarms in a month isn't the same as certainty. I didn't want to commit to an explanation before I had any field data to check it against, so getting the technician out immediately felt like the right way to test the hypothesis rather than just assume it.

Interviewer: What information sources did you weigh before deciding on the CEM data pull, and how did you land on timing?

Participant: I looked at the grey-zone handheld readings, the cost of a partial shutdown—about $40,000 a day—and the fact that a full data pull would take real analyst hours we didn't have a lot of slack for. I talked to the production supervisor about the batch schedule. Rather than treating it as an all-or-nothing choice, we tightened the interim sampling and locked in a specific date for the full pull, so we weren't just sitting on ambiguous data indefinitely.

Interviewer: What alternatives did you weigh when deciding where to start the physical inspection?

Participant: Gasket seep versus the valve. The maintenance log made the gasket the statistically obvious first stop—it's what's caused nearly every minor event here for three years. The Ohio case was in the back of my mind because the consequences there were so severe, so I added a quick valve check as a low-cost precaution, but I was explicit with the team that the log, not the Ohio story, was driving where we started.

Interviewer: What was your basis for choosing the exceedance calculation methodology?

Participant: I compared both calculation approaches against the permit language and how we'd handled similar situations in past audits, and picked the one that held up best under that precedent.

Interviewer: Did you document how you verified that calculation against the event itself?

Participant: Yes—once I settled on the approach, I logged which specific permit clause it fell under and cross-checked the calculation window against the actual alarm and logger timestamps before finalizing anything, so the number we'd eventually report on was traceable back to dated evidence rather than just asserted after the fact.

Interviewer: How much time pressure did you feel at each stage?

Participant: It was there throughout, especially with the production deadline, but it didn't override any single step—it mostly meant we had to be efficient about sequencing rather than skipping analysis.

Interviewer: How confident were you at each stage, and what would have shifted that?

Participant: Early on, moderate confidence at best—drift was plausible but unproven. By the time the data logger turned up, confidence dropped further until the teardown gave us a physical answer. Clearer field readings on day one would have resolved a lot of that uncertainty sooner.

Interviewer: If the sensor drift history hadn't existed, would your initial response have gone differently?

Participant: Probably not dramatically—I still would have wanted field confirmation before classifying anything, though I might have dispatched with a bit more urgency from the start.

Interviewer: If you hadn't known about the Ohio incident, would your inspection order have changed?

Participant: Honestly, I don't think so. The maintenance log was doing the real work there; the Ohio case just justified adding a cheap secondary check.

Interviewer: Looking back, what single piece of information, if available earlier, would have most changed your approach?

Participant: The data logger readings from day one. Getting those immediately instead of two days later would have let us move to the teardown that much sooner.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IP_Vocab_Control_3",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Environmental/Safety Compliance Officer (Manufacturing Plant)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Fenceline Alarm: VOC Exceedance Investigation at the Solvent Recovery Unit (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A vocabulary- and structure-matched control paired to IP_Biased_3. The same specialty chemicals plant, same Solvent Recovery Unit (SRU) VOC sensor alarm, same odor complaint, same production deadline, and the same four decision points are preserved, but at every decision point the officer engages in balanced, evidence-proportionate reasoning: hypotheses are checked rather than anchored, potentially unwelcome data is sought rather than avoided, and causal attribution is weighted by base rates and severity rather than by vividness of a recalled incident. No named bias is intentionally instantiated.",
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
          "Field team's handheld VOC readings are elevated but not conclusively over the permit limit"
        ],
        "alternatives": [
          "Classify the alarm as probable sensor drift and schedule routine recalibration during day shift",
          "Treat the alarm as a potential real release and immediately dispatch a field team with protocol-level urgency"
        ],
        "intended_action": "Officer notes the drift history as a relevant base rate but withholds a firm classification, dispatching the field team promptly to gather independent confirming data before committing to either explanation, then updates the working assessment once the handheld readings and the odor complaint are both in hand."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary field VOC readings fall in a 'grey zone' near but not conclusively over the permit limit",
          "Production is mid-batch; a partial shutdown for full testing would cost roughly $40,000/day",
          "A full CEM data pull and independent lab confirmation could clarify whether the exceedance is reportable"
        ],
        "new_information_after_decision": [
          "Two days later, a contractor reviewing an unrelated maintenance log flags a data logger showing sustained high VOC readings during the alarm window"
        ],
        "alternatives": [
          "Request an immediate full CEM data download and independent lab confirmation before proceeding",
          "Continue near-term monitoring with tighter sampling intervals while scoping the cost and timing of a full data pull"
        ],
        "intended_action": "Officer weighs the analyst hours and shutdown cost against the risk of an undetected exceedance, consults the production supervisor on the batch timeline, and settles on a resourced middle path (tighter interim sampling plus a scheduled full data pull within a defined short window) rather than either open-ended deferral or immediate full escalation."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three-year maintenance log shows gasket seep is the statistically most common cause of past minor VOC events at this site",
          "Officer is aware of a valve failure at a sister plant in Ohio two weeks earlier, covered in a corporate webinar, that caused a $2M fine and local news coverage",
          "No teardown or physical inspection of the SRU valve or gaskets has yet occurred"
        ],
        "new_information_after_decision": [
          "Maintenance teardown later reveals a worn gasket seal, consistent with the statistically dominant site history"
        ],
        "alternatives": [
          "Prioritize investigating gasket seep as the most likely cause based on site history",
          "Inspect the valve first given the severity of the Ohio outcome, even though it is statistically less common at this site"
        ],
        "intended_action": "Officer explicitly states that the maintenance log's three-year pattern is the primary basis for prioritizing the gasket line first, while also scheduling a quick valve check as a low-cost precaution given the severity (not likelihood) of the Ohio scenario, documenting both the base-rate reasoning and the precautionary rationale side by side."
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
        "intended_action": "Officer weighs the two calculation methodologies and permit language on their merits, consulting precedent from prior audits, and reaches a defensible conclusion; this decision point remains a genuine, undetermined judgment call with no intended bias instrumentation, matching the base scenario."
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
        "What cues did you weigh when deciding how to classify the alarm, and how did you avoid over-relying on any one of them?",
        "What information sources did you consult before deciding on the CEM data pull, and how did you decide on timing?",
        "What alternatives did you consider when prioritizing which part of the unit to inspect first, and how did you weigh likelihood against severity?",
        "What was your basis for choosing the exceedance calculation methodology, and how did the permit deadline factor in?",
        "How much time pressure did you feel at each of these moments, and how did that shape what evidence you gathered?",
        "How confident were you in your interpretation at each stage, and what would have made you more or less confident?"
      ],
      "closing_hypotheticals": [
        "If the sensor drift history hadn't existed, would your initial triage have gone differently?",
        "If you'd had an extra analyst that week, would your CEM data timeline have changed?",
        "If you hadn't known about the Ohio incident, do you think your inspection order would have been different?",
        "Looking back, what single piece of information, if available earlier, would have most changed your approach?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "IP_Biased_3",
      "features_to_match": [
        "Setting: specialty chemicals/coatings plant, Building 3 SRU, Title V permit context",
        "Same stakeholders (Plant Manager, Production Supervisor, Corporate EHS Director, Maintenance Technician, state inspector, local residents)",
        "Same four-decision-point structure and sequencing",
        "Same constraints: production deadline, staffing shortage, cost of shutdown, 24-hour reporting clock, sensor drift history, Ohio webinar exposure",
        "Same technical vocabulary list and difficulty level",
        "Same emotional tone: time pressure, professional caution, incremental uncertainty resolution"
      ],
      "features_to_remove_or_change": [
        "Remove anchoring of the initial drift hypothesis; replace with prompt cross-checking before committing to a classification",
        "Remove avoidance-motivated deferral of the CEM data pull; replace with a resourced, workload-and-risk-based interim plan",
        "Remove disproportionate narrative weighting toward the vivid Ohio incident; replace with explicit base-rate-led prioritization plus a clearly labeled precautionary (severity-based) secondary check"
      ],
      "ambiguity_boundary": "Reasoning at each decision point may still involve genuine trade-offs and incomplete information, but the participant must articulate a proportionate, evidence-based rationale for each choice rather than exhibiting anchoring, avoidance, or vividness-driven attribution. Uncertainty is preserved through resource and timing trade-offs, not through undocumented reasoning shortcuts."
      },
    "counterfactual_specification": {
      "causal_variable": "Officer's recent exposure to the vivid sister-plant (Ohio) valve-failure narrative prior to the incident (autoselected for potential future counterfactual pairing; inactive for this vocabulary_control condition)",
      "original_state": "Officer is aware of the Ohio valve failure via a corporate webinar two weeks before the incident",
      "counterfactual_state": "Officer had no recent exposure to any vivid comparable incident narrative before the SRU alarm",
      "variables_to_hold_constant": [
        "Sensor alarm timing and drift history",
        "Community odor complaint",
        "Production deadline and shutdown cost figures",
        "Maintenance log base rates for gasket seep vs. valve failure",
        "Number and sequencing of decision points"
      ],
      "expected_causal_difference": "Not applicable in this condition; reasoning at decision point 3 is already base-rate led regardless of Ohio exposure, so removing the exposure would not be expected to change the prioritization in this control version.",
      "causal_test_question": "Not applicable; this field is retained only for potential future counterfactual pairing against IP_Biased_3, not for use in vocabulary_control validation."
    },
    "generation_checks": [
      "Confirm zero intended instances of Primacy Effect, Ostrich effect, and Imaginability Bias appear anywhere in the interview.",
      "Confirm all four decision points, stakeholders, constraints, and technical vocabulary match IP_Biased_3 in structure and complexity.",
      "Confirm each decision point shows explicit, proportionate reasoning that references available evidence rather than reasoning shortcuts resembling the named biases.",
      "Confirm the Ohio incident and drift-history details are present as background facts but are explicitly subordinated to base-rate/statistical reasoning rather than driving the outcome.",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text.",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and probe coverage without repetitive exposition.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm consequences at each decision point remain uncertain in advance and do not mechanically validate or invalidate any decision as biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Imaginability Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not appear; causal attribution at decision point 3 must be explicitly base-rate led with vivid-incident consideration clearly framed as a secondary, severity-based precaution rather than a driver of prioritization."
      },
      {
        "bias": "Ostrich effect",
        "occurrences": 0,
        "mechanism_constraint": "Must not appear; the CEM data pull decision at decision point 2 must show workload/risk-based reasoning, not avoidance of an unwelcome confirmatory finding."
      },
      {
        "bias": "Primacy Effect",
        "occurrences": 0,
        "mechanism_constraint": "Must not appear; the initial triage at decision point 1 must show active cross-checking before classification rather than anchoring on the first hypothesis."
      }
    ],
    "target_bias_names": ["Imaginability Bias", "Ostrich effect", "Primacy Effect"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Imaginability Bias", "requested_occurrences": 0 },
      { "bias": "Ostrich effect", "requested_occurrences": 0 },
      { "bias": "Primacy Effect", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IP_Biased_3",
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
    "scenario_id": "IP_Vocab_Control_3",
    "domain_id": "IP",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; per vocabulary_control condition rules, zero intended instances of all three named biases are planned. Domain vocabulary, structure, stakeholders, constraints, and four-decision-point sequencing are matched to the paired biased scenario IP_Biased_3, with each decision point rewritten to show proportionate, evidence-based reasoning in place of the biased mechanism it mirrors.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Setting, actors, and stakeholder roles",
      "Four-decision-point structure and sequencing",
      "Difficulty level (challenging)",
      "Emotional tone and time-pressure framing",
      "Technical vocabulary list",
      "Target word count range (1,215-1,485)",
      "Background facts: sensor drift history, Ohio webinar exposure, production deadline, staffing constraint"
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
        "segment_type": "initial_triage_reasoning",
        "raw_interview_anchor": "At 6:40 in the morning ... I sent a technician out with a handheld meter right away rather than waiting to see if anything else developed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant treats sensor drift as relevant background but seeks independent field confirmation before classifying the alarm; the hidden zero-bias manifest contains no instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "monitoring_and_cem_timing_reasoning",
        "raw_interview_anchor": "The handheld readings came back elevated but in a grey zone ... schedule a full continuous emissions monitoring pull within a short, defined window rather than letting it drift indefinitely or shutting down that same morning.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant weighs ambiguous evidence, shutdown cost, production timing, and a defined monitoring plan; the hidden zero-bias manifest contains no instance."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "physical_inspection_target_reasoning",
        "raw_interview_anchor": "I pulled the three-year maintenance history ... I prioritized the gasket line based on the site's own history, and separately scheduled a quick, low-cost check of the valve as a precaution.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly prioritizes the local base rate and labels the valve check as a severity-based precaution; the hidden zero-bias manifest contains no instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "emissions_calculation_decision_setup",
        "raw_interview_anchor": "From there I had to decide how to calculate cumulative emissions, since the outcome affected whether we crossed into reportable territory under our 24-hour notification clock.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This introduces a genuine methodology and reporting decision without expressing a hidden bias mechanism."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "initial_triage_followup_reasoning",
        "raw_interview_anchor": "I looked at the alarm log, noted the drift history, but didn't stop there—I dispatched the technician immediately to get independent field data rather than waiting to see if the alarm cleared on its own.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The follow-up gives an explicit evidence-gathering rationale and contains no hidden bias instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "hypothesis_testing_reasoning",
        "raw_interview_anchor": "The drift history was real, and it made drift a reasonable starting hypothesis, but two false alarms in a month isn't the same as certainty ... test the hypothesis rather than just assume it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant distinguishes a plausible hypothesis from certainty and describes active testing; the hidden manifest is zero-bias."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "cem_timing_evidence_weighting",
        "raw_interview_anchor": "I looked at the grey-zone handheld readings, the cost of a partial shutdown ... we tightened our interim sampling and locked in a specific date for the full pull.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant articulates a bounded workload-and-risk trade-off rather than avoidance of confirmatory data."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "inspection_alternatives_reasoning",
        "raw_interview_anchor": "The maintenance log made the gasket the statistically obvious first stop ... I added a quick valve check as a low-cost precaution, but I was explicit with the team that the log, not the Ohio story, was driving where we started.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant separates likelihood from severity and gives the local maintenance history priority; no hidden instance is present."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "calculation_methodology_reasoning",
        "raw_interview_anchor": "I compared both calculation approaches against the permit language and how we'd handled similar situations in past audits, and picked the one that held up best under that precedent.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The methodology is selected using permit language and audit precedent; the phase-four decision is intentionally undetermined and bias-free."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "calculation_verification_reasoning",
        "raw_interview_anchor": "I logged which specific permit clause it fell under and cross-checked the calculation window against the actual alarm and logger timestamps before finalizing anything.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant makes the calculation traceable to dated evidence and does not express a hidden bias mechanism."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "time_pressure_reasoning",
        "raw_interview_anchor": "It was there throughout ... it mostly meant we had to be efficient about sequencing rather than skipping analysis.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Time pressure is explicitly described as affecting efficiency and sequencing, not as a hidden bias instance."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "confidence_and_uncertainty_reasoning",
        "raw_interview_anchor": "Early on, moderate confidence at best—drift was plausible but unproven ... Clearer field readings on day one would have resolved a lot of that uncertainty sooner.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant reports calibrated uncertainty and identifies what evidence would have changed confidence; no hidden instance is present."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "drift_counterfactual_reasoning",
        "raw_interview_anchor": "If the sensor drift history hadn't existed, I still would have wanted field confirmation before classifying anything.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The counterfactual supports robust evidence-seeking and does not instantiate a hidden bias."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "Ohio_counterfactual_reasoning",
        "raw_interview_anchor": "If you hadn't known about the Ohio incident, do you think your inspection order would have been different? ... I don't think so. The maintenance log was doing the real work there.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant says the salient incident did not drive inspection order; the hidden control manifest contains no bias instance."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "information_value_counterfactual_reasoning",
        "raw_interview_anchor": "The data logger readings from day one ... would have let us move to the teardown that much sooner.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant identifies earlier evidence that would have changed timing, without expressing a hidden bias mechanism."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
