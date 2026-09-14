You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. This is a cognitive task analysis debrief — I want to understand how you reasoned through the District X attack tempo assessment, not evaluate whether the outcome was right. Nothing here affects your record, and you can skip anything. Sound okay?

Participant: Sure, that's fine.

Interviewer: Can you tell me your role and how this landed on your desk?

Participant: I'm the all-source analyst covering District X for the battalion S2. It came to me because SIGACTS showed a sharp jump in attacks and command wanted an assessment fast for the weekly INTSUM.

Interviewer: What was the objective as you understood it?

Participant: Figure out what was driving the numbers, recommend a response, and later judge whether that response actually worked, since the commander needed something concrete for a regional brief and for deciding where checkpoint resources should go next.

Interviewer: Walk me through the incident from the start.

Participant: For about a month, District X was steady — roughly three attacks a week, small-arms harassment, occasional IED. Then week five came in at eleven. That's the highest we'd seen in the whole dataset. Around the same time, HUMINT was reporting a local festival drawing big crowds, chatter about a resupplied weapons cache, and a tribal land dispute that had flared up. None of it was fully confirmed, but it was all sitting in the reporting at once. I had to give command something for that week's INTSUM.

Interviewer: What did you recommend?

Participant: I didn't want to jump straight to a cordon-and-search without solid targeting, so I pushed more ISR onto two suspected cache routes and stood up a limited checkpoint pilot in the busiest corridor. It felt like the right middle ground — do something, but don't commit the whole posture before knowing if week five was a real trend or a one-off.

Interviewer: What drove that choice over the alternatives?

Participant: Mostly the thin data. Eight weeks total isn't much to build a trend on, and I didn't want to overcommit resources off one bad week. But sitting on it wasn't an option either, with command already asking questions. The pilot let us act without locking in a bigger resourcing decision.

Interviewer: What happened after the pilot went in?

Participant: S3 liked it enough to expand it battalion-wide in week six — that became Operation Steady Watch. Week six came in at six, still elevated but down from eleven. Week seven dropped to three, week eight to four. Basically back near where we'd been before the spike.

Interviewer: Did anything else come in around that time?

Participant: Yeah. HUMINT caught up — the festival had ended by week six, the tribal dispute got mediated by local elders, and there were reports the resupplied cache had largely been used up in whatever drove the spike. So a few things were resolving in the same window as Steady Watch going in.

Interviewer: Your supervisor asked for a causal read for the command brief. What did you actually tell them?

Participant: Honestly, I told them I couldn't cleanly separate the two explanations. The timing fit Steady Watch — presence went up, attacks went down. But the timing also fit the festival ending and the dispute settling. Both stories explain the same numbers. With only eight weeks of data and all three of those things resolving in roughly the same stretch, I didn't think I had enough to say confidently which one was doing the work, or how much of each. I flagged the checkpoint effect as plausible but unconfirmed and recommended we keep watching before treating it as proven.

Interviewer: Was there pressure to just pick one explanation for the brief?

Participant: Some. Command likes a clean narrative, and "the checkpoints worked" is a better line than "we're not sure yet." But I've been burned before recommending something off two data points that didn't hold up, so I'd rather flag the uncertainty than overstate it.

Interviewer: That fed into a District Y question. Tell me about that.

Participant: Right, the commander wanted to know if we should roll Steady Watch out to District Y too. District Y had its own spike — hit nine in week four, eased to five or six after, no posture change over there. Given that I wasn't confident about what actually drove District X's drop, I didn't want to treat that result as a proven model. Plus the District Y handler flagged that their spike had a different, still-unresolved driver — not the same mix of factors we'd seen in District X.

Interviewer: So what did you recommend?

Participant: I recommended holding off on committing checkpoint materials and doing a short standalone look at District Y first, since its situation wasn't a clean match for what we'd just seen. S3 agreed to wait rather than provision resources immediately.

Interviewer: And the forecast for the commander's brief — what did you present?

Participant: With the brief three days out and only two weeks of data past the implementation, I gave a range rather than a single number. I told the commander the tempo could hold near three to four a week, but that we hadn't isolated what was actually driving the drop, and that four more weeks would tell us a lot more than two. He wasn't thrilled with the hedge, but he approved continued funding with a review point built in rather than an open-ended commitment.

Interviewer: If the tribal dispute hadn't been resolved that week, would your read have changed?

Participant: Probably would've made me more comfortable crediting Steady Watch, yeah — one less competing explanation sitting on top of the same data.

Interviewer: And if District Y's spike had also faded without any posture change there?

Participant: That would've made me want even more data before trusting the District X story, since it'd suggest spikes can settle on their own regardless of what we do.

Interviewer: Anything about how the data came together that week you'd want to see differently?

Participant: I'd want a longer baseline before the spike, and I'd want the local reporting on the festival, the cache, and the dispute nailed down earlier instead of confirmed after the fact. Getting that timing right sooner would have made it a lot easier to say what actually moved the numbers instead of leaving it open the way we did.

</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Ambigious_1",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Intelligence Analyst (All-Source)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Sector Nightfall: Attack Tempo Assessment After Operation Steady Watch (Ambiguous Control)",
    "scenario_summary_internal": "An all-source intelligence analyst tracks weekly attack counts (IED and small-arms incidents) in District X over eight weeks. A baseline of roughly three attacks per week produces an anomalous spike to eleven attacks in week five, coinciding with a local festival, a resupplied weapons cache, and a flaring tribal land dispute. In week six, command implements a new checkpoint posture, Operation Steady Watch, partly on the analyst's recommendation. In weeks seven and eight, attack counts fall back to near-baseline levels. Unlike the paired scenario, the analyst here explicitly weighs both the checkpoint posture and the resolution of the transient local factors as plausible contributors, cannot fully disentangle them with the data available, and presents the causal picture as genuinely undetermined rather than settling confidently on either explanation. The same downstream resourcing and forecasting decisions occur, but they proceed from acknowledged uncertainty rather than from a confident single-cause narrative.",
    "occupational_realism": {
      "objective": "Determine whether Operation Steady Watch is causing the observed decline in attack tempo in District X and produce a resourcing and forecasting recommendation for the battalion S2 and commander.",
      "setting": "Battalion S2 all-source intelligence cell on a forward operating base supporting counterinsurgency operations in a contested rural district, working from SIGACTS databases, UAV/ISR feeds, and HUMINT source reporting under a weekly INTSUM production cycle.",
      "constraints": [
        "Limited UAV/ISR collection hours must be allocated between District X and District Y",
        "Weekly INTSUM deadline compresses analytic turnaround time",
        "Command pressure for a demonstrable 'win' narrative ahead of a regional assessment brief",
        "HUMINT source access in District X is intermittent and unverified",
        "Only eight weeks of SIGACTS data exist for the district, limiting historical baseline depth"
      ],
      "stakeholders": [
        "Battalion S2 (senior analyst, supervisor)",
        "Company commander responsible for District X patrol posture",
        "District governor liaison officer",
        "HUMINT source handler",
        "S3 operations officer coordinating checkpoint resourcing"
      ],
      "technical_terms_to_use": [
        "SIGACTS",
        "attack tempo",
        "INTSUM",
        "ISR tasking",
        "checkpoint posture",
        "pattern-of-life",
        "indicators and warnings",
        "collection plan"
      ],
      "technical_terms_to_avoid": [
        "regression to the mean",
        "statistical regression",
        "mean reversion",
        "law of small numbers",
        "base rate fallacy",
        "cognitive bias",
        "outlier correction",
        "confounder",
        "causal inference"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Weeks 1-4 SIGACTS average roughly 3 attacks/week in District X, with one prior week reaching 5",
          "Week 5 SIGACTS jump to 11 attacks, the highest in the dataset",
          "Unconfirmed HUMINT reporting a local festival, a possible cache resupply, and a tribal land dispute all active in week 5",
          "Command is requesting an immediate assessment for the next INTSUM"
        ],
        "new_information_after_decision": [
          "S3 approves a limited checkpoint pilot (early version of what becomes Steady Watch) starting week 6",
          "ISR tasking is increased on two suspected cache routes"
        ],
        "alternatives": [
          "Recommend an immediate cordon-and-search operation against suspected cache sites",
          "Recommend increased ISR/HUMINT tasking only, withholding kinetic or posture changes until the pattern is confirmed over more weeks",
          "Recommend an immediate district-wide checkpoint posture change without waiting for confirmation"
        ],
        "intended_action": "Analyst recommends a measured response: expanded ISR tasking plus a limited checkpoint pilot, pending confirmation that week 5 is a genuine trend rather than a one-off spike."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Operation Steady Watch (full checkpoint posture) implemented battalion-wide in District X starting week 6",
          "Week 6 attacks drop to 6; weeks 7-8 drop further to 3 and 4 respectively",
          "HUMINT later confirms the festival ended, the tribal dispute was mediated by elders, and the resupplied cache was reportedly expended in week 5 operations",
          "Supervisor requests a causal assessment of Steady Watch's effectiveness for the command brief"
        ],
        "new_information_after_decision": [
          "Analyst's assessment, framed as inconclusive on single cause, is forwarded to S3 and the company commander with a recommendation to keep monitoring",
          "Commander asks whether the same posture should be evaluated for District Y despite the uncertainty"
        ],
        "alternatives": [
          "Attribute the weeks 7-8 decline primarily to Steady Watch's deterrent effect",
          "Attribute the decline primarily to the resolution of the transient local factors (festival, cache depletion, dispute mediation)",
          "Present the decline as consistent with either explanation, or some combination, without picking a dominant cause given the limited data"
        ],
        "intended_action": "Analyst tells the supervisor that both Steady Watch and the resolved local factors line up with the timing of the decline, that the eight-week dataset is too short and the confounding factors too concentrated in the same window to cleanly separate the two, and recommends treating the checkpoint effect as unconfirmed pending more data rather than asserting it as the driver."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "District Y has its own eight-week SIGACTS history with a similar baseline (~2-3/week) and one anomalous spike to 9 in week 4, followed by a partial decline to 5-6 in subsequent weeks without any posture change",
          "Commander wants a resourcing recommendation: extend Steady Watch to District Y or hold current ISR allocation",
          "Analyst's District X assessment (from phase 2), flagged as inconclusive, is the primary input available",
          "District Y HUMINT source handler reports a different, still-unresolved local driver behind District Y's spike"
        ],
        "new_information_after_decision": [
          "S3 holds off committing checkpoint materials to District Y pending a short standalone review",
          "District Y handler is tasked to pursue additional source reporting on the unresolved driver"
        ],
        "alternatives": [
          "Recommend replicating Steady Watch in District Y immediately, treating District X as a working model",
          "Recommend a separate baseline and cause analysis for District Y before committing checkpoint resources, given that District Y's spike had a different and unresolved driver",
          "Recommend reallocating resources to HUMINT source development in District Y instead of a checkpoint posture"
        ],
        "intended_action": "Analyst recommends against an immediate replication, citing the unresolved and different driver in District Y and the still-open causal question from District X, and instead proposes a short standalone review before committing checkpoint resources."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two consecutive weeks (7-8) of low attack counts in District X following Steady Watch implementation",
          "Command brief scheduled in three days requiring a forward-looking assessment",
          "No additional District X SIGACTS data beyond week 8 is yet available",
          "Analyst's phase 2 assessment already flagged the cause as unresolved"
        ],
        "new_information_after_decision": [
          "Commander approves continued Steady Watch funding for one more quarter with an explicit review checkpoint rather than an open-ended commitment",
          "Analyst is tasked to reassess after four additional weeks of data before any further resourcing decision"
        ],
        "alternatives": [
          "Forecast continued low attack tempo (3-4/week) as a direct extrapolation of the two-week decline",
          "Present a range with explicit uncertainty, noting the limited data window, the unresolved cause, and the possibility of tempo rising back toward or above baseline",
          "Defer any quantitative forecast and request an extended observation period before the brief"
        ],
        "intended_action": "Analyst presents a forecast range rather than a single point estimate, explicitly noting to the commander that the driver of the decline has not been isolated and that four more weeks of data are needed before treating the current tempo as the new normal."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what your role was in this assessment and what triggered your involvement.",
        "What was the operational objective you were trying to achieve with this analysis?"
      ],
      "timeline_reconstruction": [
        "Take me through the SIGACTS numbers week by week as you experienced them.",
        "What did you know about District X's attack pattern before week 5?",
        "When Steady Watch was implemented, what did you expect to happen to the numbers?"
      ],
      "decision_point_probes": [
        "At the week-5 spike, what alternatives did you consider before recommending a response, and why did you choose the one you did?",
        "When you saw the decline in weeks 7-8, what evidence did you use to explain it, and what made it hard to settle on a single explanation?",
        "What made you cautious about recommending the same approach for District Y?",
        "How did you decide what to tell the commander about future attack tempo, and what information would have let you commit to a firmer forecast?"
      ],
      "closing_hypotheticals": [
        "If the tribal dispute had not been resolved that week, would your read on Steady Watch have changed?",
        "If District Y's spike had also declined without any posture change, how would that have affected your confidence in the District X picture?",
        "Looking back, is there anything about how the data came together that week that you'd want to see differently before drawing a firmer conclusion?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MD_Biased_1",
      "features_to_match": [
        "Same domain vocabulary (SIGACTS, INTSUM, ISR tasking, checkpoint posture, pattern-of-life, indicators and warnings, collection plan)",
        "Same setting, stakeholders, and constraints",
        "Same eight-week attack-count trajectory (baseline ~3/week, week-5 spike to 11, decline to 3-4 in weeks 7-8)",
        "Same four decision points and same structural sequence of alternatives",
        "Same District Y comparison scenario and same forecast-to-commander closing decision",
        "Same emotional tone (measured, procedural, mild time pressure) and same interview length target"
      ],
      "features_to_remove_or_change": [
        "Remove the confident, single-cause attribution of the weeks 7-8 decline to Steady Watch",
        "Replace it with an explicit acknowledgment that the checkpoint posture and the resolved transient local factors are both plausible contributors and cannot be cleanly separated with the available data",
        "Adjust the District Y and forecast decisions so they proceed from stated uncertainty (holding off, requesting more data, presenting a range) rather than from a settled causal belief",
        "Remove any language that treats the magnitude of the decline itself as proof of the checkpoint's effect"
      ],
      "ambiguity_boundary": "The interview must leave the true cause of the weeks 7-8 decline genuinely underdetermined: the analyst notices and articulates both the checkpoint-effect explanation and the resolved-transient-factors explanation, treats the short data window and overlapping timing as a real obstacle to separating them, and makes downstream resourcing and forecasting choices that hedge against either explanation being wrong. This must read as reasonable analytic caution under thin data, not as an artificially neutral or evasive stance, and must not contain the specific failure of dismissing or omitting consideration of natural reversion after an extreme outlier."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence versus absence of resolvable transient confounding factors (festival, cache depletion, tribal dispute mediation) coinciding with the week-5 attack spike",
      "original_state": "Transient local factors were present during the week-5 spike and resolved naturally by weeks 7-8, so the decline is genuinely ambiguous between the checkpoint posture and natural resolution of those factors",
      "counterfactual_state": "No transient confounding factors are present; the week-5 spike reflects a sustained escalation with no independent reason to subside, which would let the checkpoint effect be assessed with less ambiguity",
      "variables_to_hold_constant": [
        "Baseline attack rate in weeks 1-4",
        "Timing of Steady Watch implementation (week 6)",
        "Magnitude and timing of the week-5 spike",
        "Analyst identity, role, and reporting cadence",
        "Command pressure and INTSUM deadline structure"
      ],
      "expected_causal_difference": "Removing the transient confounders would reduce the ambiguity in the phase-2 causal assessment, since there would be no competing natural-resolution explanation to weigh against the checkpoint posture.",
      "causal_test_question": "Does the presence of resolvable transient confounders during the spike change how confidently or ambiguously the decline can be attributed to Steady Watch?"
    },
    "generation_checks": [
      "Confirm exactly four decision points exist, each with at least two alternatives, mirroring MD_Biased_1's structure.",
      "Confirm zero intended instances of 'Failure to recognize regression to the mean' or any other named bias are embedded.",
      "Confirm the phase-2 causal assessment explicitly holds both explanations open rather than dismissing or omitting the natural-resolution explanation.",
      "Confirm bias terminology, definitions, and confounder/causal-inference jargon are excluded from the public interview text.",
      "Confirm total interview length falls within 1,215-1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals, matching the paired scenario's probe coverage.",
      "Confirm downstream consequences (District Y review, forecast range) reflect hedged reasoning rather than resolving or proving the phase-2 ambiguity."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Failure to recognize regression to the mean",
        "occurrences": 0,
        "mechanism_constraint": "Must not be intentionally embedded; phase-2 reasoning must remain genuinely underdetermined between checkpoint effect and natural resolution of transient factors, without either dismissing the reversion-relevant evidence or naming/defining the bias."
      }
    ],
    "target_bias_names": [
      "Failure to recognize regression to the mean"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Failure to recognize regression to the mean",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MD_Biased_1",
    "counterfactual_variable": {
      "name": "Presence versus absence of resolvable transient confounding factors coincident with the week-5 attack spike",
      "original_state": "Transient factors (festival, cache depletion, tribal dispute mediation) present and naturally resolved by weeks 7-8, keeping the cause of the decline ambiguous",
      "changed_state": "No transient confounding factors; spike reflects sustained escalation with no independent reason to subside",
      "variables_to_hold_constant": [
        "Baseline attack rate weeks 1-4",
        "Timing of Steady Watch implementation",
        "Magnitude and timing of week-5 spike",
        "Analyst identity and reporting cadence",
        "Command pressure and INTSUM deadline"
      ]
    },
    "scenario_id": "MD_Ambigious_1",
    "domain_id": "MD",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; this is a zero-occurrence ambiguous control paired with MD_Biased_1. The single decision point that carries the bias mechanism in the paired scenario (phase 2, causal attribution of the weeks 7-8 decline) is deliberately rewritten here as an explicitly unresolved, dual-explanation judgment rather than a confident single-cause attribution, and this rewrite is not counted as a bias instance.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Setting, stakeholders, and operational constraints",
      "SIGACTS trajectory (baseline, week-5 spike, weeks 7-8 decline)",
      "Four decision-point structure and alternative sets",
      "District Y comparison and forecast-to-commander closing decision",
      "Interview length target and emotional tone"
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
        "segment_type": "objective_statement",
        "raw_interview_anchor": "Figure out what was driving the numbers, recommend a response, and later judge whether that response actually worked...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "States the analytic objective and downstream decisions without a manifested hidden bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_response_choice",
        "raw_interview_anchor": "I didn't want to jump straight to a cordon-and-search without solid targeting, so I pushed more ISR onto two suspected cache routes and stood up a limited checkpoint pilot...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explains a measured operational choice based on targeting quality and proportional commitment."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "initial_response_rationale",
        "raw_interview_anchor": "Mostly the thin data. Eight weeks total isn't much to build a trend on... The pilot let us act without locking in a bigger resourcing decision.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Weights limited data and the need to act against the cost of overcommitment; no hidden instance is manifested."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "causal_assessment",
        "raw_interview_anchor": "Honestly, I told them I couldn't cleanly separate the two explanations... I flagged the checkpoint effect as plausible but unconfirmed and recommended we keep watching before treating it as proven.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Explicitly keeps the intervention and transient local explanations open and requests more evidence, matching the zero-bias control specification."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "communication_choice_under_pressure",
        "raw_interview_anchor": "Some. Command likes a clean narrative, and 'the checkpoints worked' is a better line than 'we're not sure yet.' But I've been burned before recommending something off two data points that didn't hold up, so I'd rather flag the uncertainty than overstate it.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Recognizes command pressure but rejects the preferred narrative and preserves uncertainty; this is not a manifested hidden bias."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "generalization_caution",
        "raw_interview_anchor": "Given that I wasn't confident about what actually drove District X's drop, I didn't want to treat that result as a proven model.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Declines to generalize from an unresolved District X causal account."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "cross_context_evidence_assessment",
        "raw_interview_anchor": "Plus the District Y handler flagged that their spike had a different, still-unresolved driver — not the same mix of factors we'd seen in District X.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Uses a material difference in local drivers to limit transfer of the District X result."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "resource_allocation_choice",
        "raw_interview_anchor": "I recommended holding off on committing checkpoint materials and doing a short standalone look at District Y first...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Chooses a separate review before committing resources because the evidence is not a clean match."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "forecast_and_commitment_choice",
        "raw_interview_anchor": "With the brief three days out and only two weeks of data past the implementation, I gave a range rather than a single number... He approved continued funding with a review point built in rather than an open-ended commitment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Uses a range, identifies unresolved causation and limited data, and supports a bounded commitment rather than overclaiming certainty."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "counterfactual_evidence_weighting",
        "raw_interview_anchor": "Probably would've made me more comfortable crediting Steady Watch, yeah — one less competing explanation sitting on top of the same data.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Hypothetically explains how removing a competing explanation would change confidence; it does not manifest the hidden bias."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "counterfactual_evidence_weighting",
        "raw_interview_anchor": "That would've made me want even more data before trusting the District X story, since it'd suggest spikes can settle on their own regardless of what we do.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Treats an untreated comparison decline as evidence against overconfidence in the intervention story."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "data_collection_improvement",
        "raw_interview_anchor": "I'd want a longer baseline before the spike, and I'd want the local reporting on the festival, the cache, and the dispute nailed down earlier...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Identifies concrete data and timing improvements needed for a firmer conclusion."
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
    "analysis_scope_note": "Analysis of the supplied debrief transcript only. No retrieved scientific-corpus passages were available in this session, so no bias labels are grounded in retrieval-based scientific support."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [],
  "no_supported_biases_found": true,
  "limitations": [
    "No retrieved scientific-paper corpus passages were available in this session; the analysis could not use retrieval-first scientific support and therefore relied on conservative application of general cognitive-bias taxonomy principles.",
    "The transcript contains substantial uncertainty-aware reasoning, explicit consideration of competing causal explanations, and resistance to a preferred narrative. Where the participant described pressure, caution, or prior negative experience, these were not classified as biases because no distinct bias-specific mechanism was affirmatively evidenced.",
    "Secondhand reports of S3 and commander decisions were not sufficient to attribute a bias occurrence to those individuals."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Ambigious_1_Sonar_off",
  "interview_id": "MD_Ambigious_1",
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
