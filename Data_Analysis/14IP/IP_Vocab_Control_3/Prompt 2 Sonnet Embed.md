You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": ["Interviewer", "Participant"],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Analyzed the full transcript for affirmative evidence of bias-specific mechanisms. The participant described several heuristic risks but engaged in hypothesis testing, base-rate use, cost-risk balancing, and explicit checks. No bias occurrence met the conservative identification standard."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Availability heuristic",
        "alternative_labels": ["Availability bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Selection of physical inspection targets after the contractor flagged the data logger",
        "supporting_interview_quote": "The Ohio case was in the back of my mind because the consequences there were so severe, so I added a quick valve check as a low-cost precaution, but I was explicit with the team that the log, not the Ohio story, was driving where we started.",
        "plausible_mechanism": "A recent, vivid, high-consequence valve failure at a sister plant could increase the mental availability of valve failure, raising perceived salience or likelihood enough to prompt an additional precautionary valve check even though the site's three-year maintenance history favored gasket seep.",
        "why_not_identified": "The participant explicitly recognized the potential influence of the dramatic Ohio case, used the local maintenance history as the primary basis for the inspection decision, and described the valve check as a low-cost precaution. No affirmative evidence shows the available case distorted the primary reasoning or outcome."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "Plan continuation bias",
        "alternative_labels": ["Get-there-itis", "Plan continuation error"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Decision to continue operations with interim monitoring rather than immediate shutdown after grey-zone handheld readings",
        "supporting_interview_quote": "We were also mid-batch on a large customer order due in two days, so an unnecessary shutdown wasn't something anyone wanted. I talked it through with the production supervisor and we agreed to tighten our sampling interval and schedule a full continuous emissions monitoring pull within a short, defined window rather than letting it drift indefinitely or shutting down that same morning.",
        "plausible_mechanism": "Commitment to the existing production plan and the desire to avoid an unnecessary shutdown may have biased interpretation of ambiguous grey-zone readings toward continuing operations.",
        "why_not_identified": "The transcript shows active risk management—tightened sampling, a defined full data pull, consultation with the production supervisor—and no distortion or neglect of the ambiguous readings. Production deadline and cost considerations are structural/incentive factors rather than affirmative evidence of a distinct plan-continuation cognitive mechanism."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "Retrieved corpus passages were sparse and partially truncated, limiting formal source anchoring.",
      "The interview contains explicit self-regulatory and debiasing statements, so plausible heuristic influences could not be affirmatively tied to a biased reasoning outcome.",
      "No speaker or transcript feature allowed confident attribution of a bias-specific mechanism to any identified decision."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IP_Vocab_Control_3_Sonnet_on",
  "interview_id": "IP_Vocab_Control_3",
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
