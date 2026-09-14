You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief on the elevated I-131 reading you caught during the backshift a couple weeks ago — nothing punitive, I just want to understand how you worked through it. Can I get your role and shift context first?

Participant: Sure. I'm a radiochemistry tech, second shift lead on backshift when it happened. Reduced crew that night — just me and one other tech in the lab, supervisor was in the control room, not on the floor.

Interviewer: Good. Walk me through what happened from the top.

Participant: I was running a routine RCS grab sample, standard surveillance, hot leg sample through the panel, straight into the HPGe for the count. When I pulled the spectrum, the I-131 photopeak was way up — something like three times the trend from the week before. First thing that jumped to mind was the fuel-defect event we had last outage. I was on shift for that one too, actually caught the original spike, so I remembered exactly what that spectrum looked like, and this one had a similar shape to it. My gut said we might have a cladding defect starting.

Interviewer: What else was going on around that reading, technically?

Participant: A few things. The detector had just come back from a recalibration two days before — routine, after some maintenance work. So there was some residual uncertainty baked in there, we hadn't fully re-baselined the efficiency curve yet. Power was steady at 100%, no transients logged, letdown flow was normal. So nothing on the plant side jumped out as an obvious driver.

Interviewer: Given the recalibration was so recent, did that register as a competing explanation?

Participant: It crossed my mind, yeah. I noted it in my head — "detector was just touched, keep that in your back pocket." But honestly the fuel-defect angle felt like the more urgent thing to chase down first, because I'd lived through that exact scenario before and knew how fast it can escalate if you sit on it. So I ran with that as my working theory and figured I'd circle back to the calibration question if the fuel-defect leads didn't pan out.

Interviewer: What did you do next?

Participant: I set up a repeat count on the same sample to confirm the peak wasn't a fluke, and while that was running I started looking at secondary indicators — the Cs-137 ratio, background counts, counting geometry, that kind of thing.

Interviewer: What came out of the repeat count?

Participant: Ratio shifted slightly from the first count, not hugely, but enough that I filed it as "real signal, not noise." No corresponding power or flow change logged for the shift either, which kept the plant-transient explanation off the table.

Interviewer: That's decision point one, roughly — leaning into the fuel-defect read early. Let's move to what happened after that repeat count.

Participant: Right, so once I had a second data point, I started comparing the shape of this spectrum — the peak shape and that Cs-137 ratio — against stuff I'd seen before. And it actually reminded me a lot of a case from maybe eighteen months back, a resin intrusion event in the letdown demineralizer. Different system, different sample point, but the spectral signature had that same kind of look to it. So I started leaning toward calling it a resin-intrusion-type issue rather than purely a fuel defect.

Interviewer: Had you drawn a demineralizer effluent sample at that point to check?

Participant: Not yet, no. That sample takes a bit longer to pull and process, so I was going off the resemblance of the two spectra while that was in queue. It looked enough like the old case that I figured we were probably looking at the same kind of root cause, even though I hadn't confirmed the pathway yet.

Interviewer: What made the resemblance persuasive versus, say, waiting for the demineralizer sample first?

Participant: Time, mostly. We had a reporting window closing on us, and I wanted to have some working hypothesis in hand rather than nothing. The two sample points are physically different — I knew that — but the pattern match felt strong enough that I didn't push hard to verify the pathway before forming the call.

Interviewer: What did the demineralizer sample eventually show?

Participant: Different Cs-137 to I-131 ratio than the RCS sample, actually. And I&C confirmed no open work orders on the RCS panel valves, so cross-contamination through hardware wasn't it either. That complicated things a bit.

Interviewer: Let's talk about the escalation decision — point three. Once you had two consistent counts showing a real elevation, what did you do?

Participant: I went to the shift supervisor with a preliminary call. I told him I thought we were looking at an early fuel-defect indicator, possibly compounded by something upstream, and that I wanted to keep sampling frequency up. I'd already formed that framing in my head from the earlier steps, so that's the story I brought him.

Interviewer: Did you consider looping in reactor engineering before that formal notification?

Participant: I thought about it, but the tech spec clock was ticking and I didn't want to sit on the report. Supervisor asked right away whether I was recommending a power reduction, and reactor engineering wanted the last three surveillance points for comparison, so it kicked off a bigger conversation than I'd expected.

Interviewer: And the fourth point — finalizing the report?

Participant: By then I had the repeat count, the split sample, and the demineralizer result all in hand. Reactor engineering's fuel-performance model came back probabilistic, not a clean yes-or-no. I ended up writing the report with a ranked list of possible causes rather than pinning it to one thing, and recommended bumping up the sampling frequency for the next 24 hours instead of locking in a single root cause right away.

Interviewer: What tipped you toward the ranked approach instead of a single definitive call?

Participant: Honestly, by that point the data wasn't clean enough to be confident in one explanation. The demineralizer ratio didn't match, the valve work orders were clear, and the model wasn't definitive either. Given how the earlier assumptions hadn't fully held up, I didn't want to overcommit the final write-up.

Interviewer: Looking back, what would've changed your first read, at the very start?

Participant: If I hadn't been the one who caught that fuel-defect spike last outage, I might not have jumped there first. I might have given the recalibration explanation more weight right out of the gate instead of parking it.

Interviewer: And if you'd pulled the demineralizer sample before forming any theory at all?

Participant: I think I'd have held off longer before connecting it to that old resin-intrusion case. The pattern match was persuasive in the moment, but it turned out not to hold up once the actual pathway data came in.

Interviewer: Last one — what would you tell a newer tech about using past cases to read a new spectrum?

Participant: I'd say a prior case can point you somewhere to look, but don't let it stand in for confirming the actual pathway. Get the second sample before you commit to the story, not after.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Biased_2",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Chemistry Technician / Radiochemistry Laboratory Technician",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Anomalous Iodine Peak During RCS Grab Sample Analysis",
    "scenario_summary_internal": "A radiochemistry technician performing a routine reactor coolant system (RCS) grab sample and gamma spectroscopy count detects an unexpected I-131 photopeak. The technician must decide how urgently to treat the reading, whether to attribute it to a fuel cladding defect versus an instrument or sampling artifact, whether to escalate to the shift supervisor, and how to set final corrective sampling frequency and root-cause attribution. A vivid fuel-leak event from a prior outage and a superficially similar spectral signature from an unrelated past case create two distinct opportunities for biased reasoning embedded in an otherwise technically plausible, nonroutine incident.",
    "occupational_realism": {
      "objective": "Correctly determine the source of an elevated I-131 activity reading in an RCS coolant sample, take proportionate corrective action, and report results within technical specification reporting timelines without triggering unwarranted plant conservative actions or missing a genuine fuel defect indication.",
      "setting": "Radiochemistry laboratory adjacent to the reactor building of a pressurized water reactor plant, during a backshift with reduced staffing; sample drawn from the RCS hot leg via the sampling panel and analyzed on a high-purity germanium (HPGe) gamma spectroscopy system.",
      "constraints": [
        "Reduced backshift staffing means the shift supervisor is not immediately on the lab floor",
        "Technical specifications require timely reporting of coolant activity trending outside normal band",
        "Reactor is at 100% power with limited tolerance for unnecessary conservative power reduction",
        "HPGe detector was recently recalibrated after a maintenance outage, introducing residual uncertainty about instrument drift",
        "Sample turnaround time is limited before the next scheduled surveillance sample supersedes it"
      ],
      "stakeholders": [
        "Radiochemistry technician (primary actor)",
        "Shift supervisor / control room",
        "Reactor engineering (fuel performance)",
        "Instrumentation and controls (I&C) technician",
        "Chemistry supervisor (day shift, on-call)"
      ],
      "technical_terms_to_use": [
        "RCS grab sample",
        "gamma spectroscopy",
        "HPGe detector",
        "I-131 photopeak",
        "dose equivalent iodine (DEI)",
        "fuel cladding defect",
        "letdown line",
        "background count",
        "technical specification limit",
        "cross-contamination",
        "counting geometry",
        "efficiency calibration"
      ],
      "technical_terms_to_avoid": [
        "salience",
        "similarity heuristic",
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
          "HPGe spectrum shows an I-131 photopeak roughly 3x the prior week's trend",
          "Detector was recalibrated two days earlier after maintenance",
          "Plant is at steady 100% power with no recent transients logged",
          "Technician personally handled a confirmed fuel-defect event with a similar-looking iodine spike during the previous refueling outage cycle"
        ],
        "new_information_after_decision": [
          "A repeat count on the same sample shows a slightly different peak ratio than the first count",
          "No corresponding change in reactor power or letdown flow is logged for this shift"
        ],
        "alternatives": [
          "Treat the reading as a likely early fuel-defect indicator and initiate expedited confirmatory sampling",
          "Treat the reading as routine statistical variation pending a second count",
          "Suspect an instrument or calibration artifact given the recent recalibration and check detector background first"
        ],
        "intended_action": "Technician leans strongly toward the fuel-defect interpretation, prioritizing it over the calibration-artifact possibility"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The current spectrum's peak shape and secondary Cs-137 ratio superficially resemble a spectrum from an unrelated prior case involving a resin intrusion in the letdown demineralizer",
          "No sample has yet been drawn from the demineralizer effluent to confirm or rule out that pathway",
          "The RCS sample and the demineralizer effluent sample are drawn from different points in the system with different expected activity signatures"
        ],
        "new_information_after_decision": [
          "The demineralizer effluent sample, once drawn, shows a different Cs-137-to-I-131 ratio than the RCS sample",
          "I&C reports no open work orders on the RCS sample panel valves"
        ],
        "alternatives": [
          "Attribute the RCS reading to the same root cause as the earlier demineralizer resin-intrusion case based on the resemblance of the spectral pattern",
          "Treat the resemblance as coincidental and independently trace the RCS sample's activity pathway",
          "Request an independent split-sample count by a second technician before attributing cause"
        ],
        "intended_action": "Technician attributes the RCS activity to a resin-intrusion-type cause because the spectrum looks like the earlier case, without independently verifying the pathway"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two counts now show a consistent, real I-131 elevation above the recalibration uncertainty band",
          "Shift supervisor has not yet been formally notified; only informal discussion has occurred",
          "Technical specification reporting window is narrowing",
          "Reactor engineering has not yet been consulted on fuel performance trending"
        ],
        "new_information_after_decision": [
          "Shift supervisor requests a formal written activity trend report and asks whether a power reduction is being recommended",
          "Reactor engineering asks for the last three surveillance data points for comparison"
        ],
        "alternatives": [
          "Escalate immediately to the shift supervisor with a preliminary fuel-defect call",
          "Continue independent verification (extended count, split sample) before escalating",
          "Consult reactor engineering informally before making any formal call"
        ],
        "intended_action": "Technician escalates with a specific causal framing already fixed in mind"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "All confirmatory data (repeat count, split sample, demineralizer sample) are now available",
          "Reactor engineering's fuel-performance model gives a probabilistic, not definitive, assessment",
          "Final report must specify recommended sampling frequency and root-cause attribution"
        ],
        "new_information_after_decision": [
          "Follow-up trending over the next 24 hours either confirms or fails to confirm the initial attribution",
          "Chemistry supervisor reviews the report the next morning"
        ],
        "alternatives": [
          "Finalize the report with a single, confident root-cause attribution and a fixed sampling frequency",
          "Finalize the report with a ranked set of plausible causes and a conservative increased-frequency sampling plan pending further data",
          "Request an extended surveillance period before finalizing any attribution"
        ],
        "intended_action": "Technician finalizes attribution and sampling recommendation, closing out the incident record"
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe what you were doing when you first noticed the anomalous reading.",
        "What was your role and what were you responsible for deciding that shift?"
      ],
      "timeline_reconstruction": [
        "Walk me through what you saw on the spectrum first, second, and third counts.",
        "What information did you have before each decision, and what changed afterward?",
        "Who else was involved at each stage, and when did you bring them in?"
      ],
      "decision_point_probes": [
        "What specifically drew your attention to the fuel-defect explanation first? (cues)",
        "What other information sources could you have checked before settling on that view? (information sources)",
        "What were you trying to accomplish at that moment—speed, certainty, or something else? (goals)",
        "What alternatives did you consider, and why did you rule them out? (alternatives)",
        "What was the deciding factor that tipped you toward the demineralizer resin-intrusion explanation? (decision basis)",
        "Had you seen a similar spectrum before? How did that prior experience shape your read this time? (prior experience)",
        "How much time pressure did you feel at each stage? (time pressure)",
        "How confident were you in the attribution at the time versus after the confirmatory data came in? (uncertainty)"
      ],
      "closing_hypotheticals": [
        "If the recalibration had happened a month earlier instead of two days earlier, would your first read have changed?",
        "If you had drawn the demineralizer sample before forming any theory about the RCS reading, do you think your conclusion would have differed?",
        "Looking back, what would you tell a newer technician to check before letting a past case guide the current one?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "decision_point": 1,
        "mechanism": "The technician's personal, vivid, emotionally memorable involvement in a prior confirmed fuel-defect event during the last outage causes that explanation to dominate the interpretation of the current ambiguous I-131 peak, overweighting it relative to the equally or more plausible instrument-recalibration-artifact explanation.",
        "affected_reasoning_operation": "Initial hypothesis generation and weighting under the first data point (first spectrum count)",
        "evidence_available_at_time": [
          "Recalibration occurred two days prior, an objectively relevant competing explanation",
          "No power or flow transient logged",
          "Technician's own memorable prior fuel-defect experience from the last outage"
        ],
        "required_textual_manifestation": "Technician's narration should explicitly reference how strongly the memory of the prior fuel-defect event colored the first read, and should show the recalibration-artifact explanation being mentioned but under-weighted or considered only briefly before moving on.",
        "plausible_nonbias_interpretation": "A technician could reasonably prioritize the fuel-defect hypothesis first simply because it is the higher-consequence possibility requiring prompt verification, independent of how memorable the prior event was.",
        "strength": "subtle",
        "do_not_make_explicit": ["salience", "memorable", "cognitive bias", "vivid recall bias"]
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "decision_point": 2,
        "mechanism": "The technician attributes the RCS sample's elevated activity to the same root cause as an unrelated prior demineralizer resin-intrusion case purely because the gamma spectrum's peak shape and secondary ratio superficially resemble that earlier case, without verifying that the sampling point, system pathway, or other distinguishing features actually support a common cause.",
        "affected_reasoning_operation": "Causal attribution and evidence-selection act during cross-check with a second sample source",
        "evidence_available_at_time": [
          "Superficial resemblance of spectral peak shape and Cs-137:I-131 ratio to the prior demineralizer case",
          "No demineralizer effluent sample has yet been drawn to confirm the pathway",
          "The RCS and demineralizer sample points are physically and functionally distinct"
        ],
        "required_textual_manifestation": "Technician's narration should show the attribution being made or strongly favored on the basis of the spectra 'looking like' the earlier case, before the confirmatory demineralizer sample is drawn, with the distinguishing sampling-point difference mentioned but not treated as decisive.",
        "plausible_nonbias_interpretation": "A technician might reasonably use a known prior pattern as a starting hypothesis to guide efficient troubleshooting, provided it is promptly checked against confirmatory data rather than treated as established.",
        "strength": "subtle",
        "do_not_make_explicit": ["similarity heuristic", "pattern matching bias", "cognitive bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for biased condition; no control scenario is being generated in this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Autoselected: presence versus absence of the technician's prior personal involvement in the earlier confirmed fuel-defect event and the earlier demineralizer resin-intrusion case (i.e., whether the technician has direct memorable experience with both precedent cases or is instead encountering both pattern types for the first time via written records only)",
      "original_state": "Technician personally experienced both prior cases firsthand and recalls them vividly",
      "counterfactual_state": "Technician has only read summary records of both prior cases secondhand, with no personal vivid memory",
      "variables_to_hold_constant": [
        "Reactor power level and operating conditions",
        "Timing and sequence of the spectrum counts and confirmatory samples",
        "Staffing level and reporting deadlines",
        "Final confirmatory data outcomes"
      ],
      "expected_causal_difference": "Without vivid firsthand recall, the technician would be expected to weight the recalibration-artifact and independent-pathway explanations more evenly at decision points 1 and 2, reducing the strength of both the salience-driven and similarity-driven attributions.",
      "causal_test_question": "Does removing the technician's personal, memorable firsthand experience with the two precedent cases reduce the degree to which the initial spectrum reading and the cross-check attribution are driven by memorability and surface resemblance rather than by systematically weighted evidence?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present in the timeline",
      "Confirm exactly one Salience Bias instance is embedded, located at decision point 1",
      "Confirm exactly one Similarity Bias instance is embedded, located at decision point 2",
      "Confirm no bias labels or psychological terminology appear in probe or timeline text intended for the public interview",
      "Confirm each decision point offers at least two plausible alternatives",
      "Confirm consequences described do not mechanically prove bias presence (e.g., outcome is not stated as simply 'wrong' or 'right')",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points, probe plan breadth, and two bias manifestations"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Salience Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overweighting a vivid, personally memorable prior fuel-defect event relative to an objectively relevant competing explanation (recent recalibration) at the first data point."
      },
      {
        "bias": "Similarity Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as causal attribution based on superficial spectral resemblance to an unrelated prior case, made or strongly favored before confirmatory pathway evidence is obtained."
      }
    ],
    "target_bias_names": ["Salience Bias", "Similarity Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Salience Bias", "requested_occurrences": 1},
      {"bias": "Similarity Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "sb_01", "bias": "Salience Bias"},
      {"instance_id": "sim_01", "bias": "Similarity Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "sb_01", "bias": "Salience Bias", "decision_point": 1},
      {"instance_id": "sim_01", "bias": "Similarity Bias", "decision_point": 2}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "mechanism": "Overweighting a vivid, personally memorable prior fuel-defect event during initial hypothesis formation, at the expense of the objectively relevant recalibration-artifact explanation",
        "affected_reasoning_operation": "Initial hypothesis generation and weighting from first spectrum count",
        "evidence_source": "Technician's autobiographical memory of prior outage fuel-defect event versus the logged recalibration date",
        "distinctiveness_requirement": "Must be tied specifically to the memorability/vividness of a past personal event overriding an objectively available competing cue, not to mere pattern resemblance (which is reserved for the Similarity Bias instance)"
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "mechanism": "Causal attribution driven by superficial resemblance between the current spectrum and an unrelated prior case's spectrum, prior to obtaining confirmatory pathway-specific evidence",
        "affected_reasoning_operation": "Evidence-selection and causal-attribution act during the demineralizer cross-check",
        "evidence_source": "Visual/quantitative resemblance of peak shape and isotopic ratio between current RCS sample and prior unrelated demineralizer case, versus the un-obtained demineralizer effluent sample",
        "distinctiveness_requirement": "Must be tied specifically to surface pattern resemblance between two different physical sampling contexts, not to personal memorability of either case (reserved for the Salience Bias instance) and must occur at a distinct decision point and evidence source from sb_01"
      }
    ],
    "intended_strength": [
      {"instance_id": "sb_01", "bias": "Salience Bias", "strength": "subtle"},
      {"instance_id": "sim_01", "bias": "Similarity Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Technician's firsthand vivid experience with precedent cases (autoselected)",
      "original_state": "Technician personally experienced both precedent cases and recalls them vividly",
      "changed_state": "Technician knows both precedent cases only from secondhand written records, without vivid personal recall",
      "variables_to_hold_constant": [
        "Reactor power level and operating conditions",
        "Timing and sequence of spectrum counts and confirmatory samples",
        "Staffing level and reporting deadlines",
        "Final confirmatory data outcomes"
      ]
    },
    "scenario_id": "NP_Biased_2",
    "domain_id": "NP",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread across distinct decision points (Salience Bias at decision point 1, Similarity Bias at decision point 2) per mechanism fit: Salience Bias fits the earliest ambiguous-cue interpretation moment; Similarity Bias fits the subsequent cross-source causal-attribution moment. No decision point received more than one instance of any single bias, satisfying the max-two-per-point rule trivially since each bias has only one occurrence.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Reactor power level and operating conditions",
      "Timing and sequence of spectrum counts and confirmatory samples",
      "Staffing level and reporting deadlines",
      "Final confirmatory data outcomes"
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
          "segment_type": "initial_hypothesis_weighting",
          "raw_interview_anchor": "I-131 peak interpreted through the prior fuel-defect event while the recent recalibration explanation was acknowledged but parked.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sb_01"
          ],
          "ground_truth_rationale": "The participant explicitly overweighted a personally experienced prior fuel-defect event relative to the objectively relevant recent recalibration."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "confirmatory_evidence_interpretation",
          "raw_interview_anchor": "The repeat count was treated as a real signal rather than noise, with plant-transient explanations deprioritized.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is evidence interpretation and exclusion of a plant-transient explanation, without a hidden manifested bias instance."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "pattern_based_causal_attribution",
          "raw_interview_anchor": "The current spectrum was treated as a resin-intrusion-type issue because it resembled an older case before pathway confirmation.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sim_01"
          ],
          "ground_truth_rationale": "The participant favored a causal attribution from superficial spectral resemblance despite distinct sample points and absent pathway confirmation."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "counterevidence_interpretation",
          "raw_interview_anchor": "The mismatched demineralizer ratio and absence of valve work orders were recognized as complications.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant incorporated counterevidence; this segment contains no hidden target instance."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "escalation_framing",
          "raw_interview_anchor": "The supervisor was given a preliminary early-fuel-defect framing while reporting urgency shaped the escalation timing.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden manifest contains no anchoring instance at the escalation point."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "final_reporting_decision",
          "raw_interview_anchor": "The final report used ranked causes and increased sampling because the evidence was not definitive.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant updated toward uncertainty and a ranked report; no hidden target instance is located here."
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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis covers the participant's reasoning during the elevated I-131 episode, including initial hypothesis generation, weighting of competing explanations, pattern matching to prior cases, escalation, and final reporting."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and Adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability Heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness Heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability Heuristic",
      "alternative_labels": [
        "availability bias",
        "availability"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to judge the likelihood or diagnostic relevance of an event based on how easily similar instances come to mind, especially personally salient or recent experiences.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial interpretation of the elevated I-131 spectrum",
      "decision_point_description": "Generating an initial working hypothesis for the elevated I-131 reading before repeat counting or pathway confirmation.",
      "affected_reasoning_operation": "Initial diagnostic hypothesis generation",
      "bias_specific_mechanism": "A prior personally experienced fuel-defect spike was highly available in memory, and that ease of recall shaped the participant's early judgment that the new spectrum indicated a possible cladding defect.",
      "manifestation_in_interview": "The participant immediately linked the current elevated I-131 peak to the fuel-defect event from the last outage, stating that he had personally caught the original spike and remembered the spectrum shape, which made the fuel-defect explanation jump to mind.",
      "effect_on_reasoning_or_decision": "The easy retrieval of the prior fuel-defect episode produced an early gut call toward a cladding defect and made it the initial working theory before competing explanations were systematically evaluated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "First thing that jumped to mind was the fuel-defect event we had last outage. I was on shift for that one too, actually caught the original spike, so I remembered exactly what that spectrum looked like, and this one had a similar shape to it. My gut said we might have a cladding defect starting.",
          "evidence_explanation": "The participant explicitly attributes the fuel-defect hypothesis to having personally experienced and remembered a prior similar event, which is the hallmark availability mechanism: salient, easily recalled instances guiding initial judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I hadn't been the one who caught that fuel-defect spike last outage, I might not have jumped there first. I might have given the recalibration explanation more weight right out of the gate instead of parking it.",
          "evidence_explanation": "This retrospective statement reinforces that the personal availability of the prior fuel-defect event biased the initial weighting of explanations, rather than a neutral assessment of the current evidence."
        }
      ],
      "correction_or_counterevidence": "The participant later used a ranked list of possible causes and acknowledged that his personal history may have influenced the first read. However, the availability-driven hypothesis was already formed and guided early actions before that correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The label and mechanism derive from general cognitive-science knowledge; the retrieved corpus did not directly support the availability heuristic label for this occurrence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring and Adjustment",
      "alternative_labels": [
        "anchoring bias",
        "anchoring and insufficient adjustment",
        "diagnostic anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to rely heavily on an initial value, hypothesis, or impression and to make insufficient adjustments from that anchor when later information or competing explanations become available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Weighting the recent detector recalibration against the fuel-defect hypothesis",
      "decision_point_description": "Deciding how much weight to give the recent detector recalibration as a competing explanation while forming the early working theory.",
      "affected_reasoning_operation": "Weighting of competing explanations and adjustment from an initial hypothesis",
      "bias_specific_mechanism": "The early fuel-defect interpretation served as an anchor; the participant acknowledged the recalibration explanation but explicitly parked it and continued from the fuel-defect framing rather than adjusting the initial diagnosis proportionally.",
      "manifestation_in_interview": "The participant noted the detector had just been recalibrated and there was residual uncertainty, but treated the fuel-defect angle as more urgent and deferred the calibration explanation. This initial framing later carried into the escalation narrative.",
      "effect_on_reasoning_or_decision": "The recalibration explanation was underweighted relative to the initial fuel-defect anchor, and the anchored framing persisted into the preliminary report to the shift supervisor.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I noted it in my head — 'detector was just touched, keep that in your back pocket.' But honestly the fuel-defect angle felt like the more urgent thing to chase down first, because I'd lived through that exact scenario before and knew how fast it can escalate if you sit on it. So I ran with that as my working theory and figured I'd circle back to the calibration question if the fuel-defect leads didn't pan out.",
          "evidence_explanation": "The participant explicitly forms an initial hypothesis and sets aside a plausible competing explanation rather than adjusting the diagnosis to account for it, consistent with insufficient adjustment from an anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I told him I thought we were looking at an early fuel-defect indicator, possibly compounded by something upstream, and that I wanted to keep sampling frequency up. I'd already formed that framing in my head from the earlier steps, so that's the story I brought him.",
          "evidence_explanation": "The earlier fuel-defect anchor continued to shape the escalation message, showing that the initial frame was not sufficiently revised before being communicated."
        }
      ],
      "correction_or_counterevidence": "The participant did consciously note the recalibration as an alternative and ultimately avoided overcommitting in the final report. However, the anchor still affected early prioritization and escalation framing.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus material on anchoring and adjustment in engineering contexts was used to support this occurrence.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "Initial values or hypotheses serve as anchors, and subsequent adjustments from the anchor are typically insufficient.",
          "relevance_to_this_occurrence": "The participant's early fuel-defect hypothesis functioned as an initial answer; the recalibration alternative was acknowledged but parked, indicating insufficient adjustment from that initial diagnostic anchor."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Representativeness Heuristic",
      "alternative_labels": [
        "representativeness bias",
        "representativeness"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to judge the probability that a current case belongs to a particular category based on resemblance to a typical or remembered case, while underweighting base rates and pathway-specific information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Inferring a resin-intrusion root cause from spectral resemblance",
      "decision_point_description": "Deciding whether the current spectrum represented a resin-intrusion-type issue before demineralizer effluent sample confirmation.",
      "affected_reasoning_operation": "Inference of root-cause category from pattern resemblance",
      "bias_specific_mechanism": "The participant judged the likelihood of a resin-intrusion event primarily from the visual resemblance between the current spectrum and a remembered prior case, even though the sample points and system pathways were different and not yet confirmed.",
      "manifestation_in_interview": "After the repeat count, the participant compared the spectrum to an eighteen-month-old resin intrusion case, noted the strong resemblance, and began leaning toward that same root cause despite acknowledging the physical sample source differences and lack of confirmatory demineralizer data.",
      "effect_on_reasoning_or_decision": "The resemblance-based match created a provisional root-cause call before confirmatory pathway evidence, influencing the participant's provisional diagnosis without waiting for the demineralizer sample.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "And it actually reminded me a lot of a case from maybe eighteen months back, a resin intrusion event in the letdown demineralizer. Different system, different sample point, but the spectral signature had that same kind of look to it. So I started leaning toward calling it a resin-intrusion-type issue rather than purely a fuel defect.",
          "evidence_explanation": "The participant explicitly states that similarity to a remembered case, rather than confirmed pathway data, shifted his diagnosis toward resin intrusion, which is the core representativeness mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It looked enough like the old case that I figured we were probably looking at the same kind of root cause, even though I hadn't confirmed the pathway yet.",
          "evidence_explanation": "This quote directly links the resemblance judgment to a probability inference about the root cause, despite the absence of confirmatory pathway evidence."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that the sample points differed, and the eventual demineralizer sample showed a different Cs-137 to I-131 ratio. The final report used a ranked list rather than a single resemblance-based cause.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The label and mechanism derive from general cognitive-science knowledge; the retrieved corpus did not directly support the representativeness heuristic label for this occurrence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a single retrospective self-report from one participant; inference of cognitive mechanisms is based on verbal descriptions rather than direct observation or controlled comparison.",
    "Retrieved corpus support was limited and mainly provided directly relevant support for anchoring and adjustment; availability and representativeness labels rely on general cognitive-science knowledge.",
    "Some reasoning occurred under time pressure and with limited information; these structural conditions are not themselves treated as biases unless a distinct mechanism was evidenced.",
    "No experimental baseline or normative benchmark is available from the transcript, so classification is based on affirmative mechanism evidence only."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Biased_2_Sonar_on",
  "interview_id": "NP_Biased_2",
  "system_prompt_id": "Sonar",
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
