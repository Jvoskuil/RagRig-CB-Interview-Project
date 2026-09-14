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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
