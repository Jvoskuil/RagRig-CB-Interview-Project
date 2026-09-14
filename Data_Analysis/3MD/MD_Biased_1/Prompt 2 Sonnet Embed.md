You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through the District X attack tempo assessment, not in grading the outcome. Nothing here goes in your file, and you can decline any question. That work for you?

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Great. Can you start by telling me your role and what pulled you into this particular assessment?

Participant: I'm the all-source analyst supporting the battalion S2 for District X. I own the SIGACTS tracking and the weekly INTSUM injects for that sector. It came onto my desk because we had a sharp jump in attack reporting and the S2 wanted an assessment fast, since command was already asking questions.

Interviewer: What was the overall objective you were working toward?

Participant: Figure out what was driving the attack numbers, recommend a response, and eventually judge whether that response worked — because the commander needed something concrete for a regional brief and for deciding where to put checkpoint resources next.

Interviewer: Walk me through the incident from the start.

Participant: Sure. For about a month, District X was running maybe three attacks a week — small-arms harassment, the occasional IED. Pretty steady. Then in week five we got eleven. That's not a small bump, that's the highest number in our whole dataset for that district. Around the same time, HUMINT was reporting a local festival that was drawing large crowds, some chatter about a resupplied weapons cache, and a tribal land dispute that had flared up. None of that was fully confirmed, but it was in the reporting. I had to decide what to recommend for that week's INTSUM with command already pushing for an answer.

Interviewer: What did you land on?

Participant: I recommended we not overreact with a full cordon-and-search — we didn't have solid targeting yet — but we did push more ISR onto two suspected cache routes and stood up a limited checkpoint pilot in the highest-traffic area. That felt like the right middle ground: do something, but don't commit to a big posture change before we knew if week five was a one-off or the start of a real trend.

Interviewer: What made you choose that over the other options?

Participant: Mainly time pressure and thin confirmation. We only had eight weeks of data total for that district, so I didn't want to overcorrect off one bad week. But I also couldn't just sit on it with command asking for something in the INTSUM. The pilot checkpoint let us act without betting the whole resourcing plan on one spike.

Interviewer: Okay — what happened after the pilot went in?

Participant: S3 liked it enough to expand it battalion-wide starting week six. That became Operation Steady Watch — full checkpoint posture across the district's main routes. Week six came in at six attacks, better than five but still elevated. Then week seven dropped to three, week eight to four. Basically back to where we'd been before the spike.

Interviewer: At that point, did anything else come in about what else might have changed?

Participant: Yeah, HUMINT caught up a bit. The festival had ended by week six. The tribal dispute got mediated by local elders around the same time. And there were reports the cache that got resupplied before week five had largely been expended in whatever activity drove that spike. So there were a few things resolving in parallel with Steady Watch going in.

Interviewer: Your supervisor then asked you for a causal read on that. What did you tell them?

Participant: I told them Steady Watch was working. The numbers backed it up — we went from eleven down to three and four within two weeks of putting checkpoints on the main routes. That's a big swing, and it lined up with when we increased presence. I flagged the other stuff — the festival ending, the dispute settling — but I treated those as secondary color, not the main driver. The posture change was the biggest, most visible thing we'd done, and the timing fit.

Interviewer: When you were weighing that, did you consider what the numbers might have done without Steady Watch at all?

Participant: Not in much depth, honestly. I noted the other factors existed, but I didn't really sit down and ask how much of that drop would've happened on its own just because week five was such an extreme outlier to begin with. The checkpoint explanation was the one command wanted and the one I had the clearest evidence trail for — increased presence, fewer incidents. It felt like a clean story.

Interviewer: That assessment then fed into a District Y decision. Tell me about that.

Participant: Right, the commander wanted to know if we should extend Steady Watch to District Y. District Y had its own spike — hit nine in week four — then eased down to five or six afterward, no posture change over there. Given what I'd just seen in District X, I recommended rolling Steady Watch out to District Y too, expecting a similar sharp drop.

Interviewer: Did you weigh the alternative of running a separate cause analysis for District Y first?

Participant: I considered it, but time was short and District X felt like a validated model at that point — we'd just seen checkpoints turn a spike around. The Y handler did mention their spike had a different, still-unresolved driver, which I noted, but I leaned on the District X result as the stronger signal for what to do next.

Interviewer: Last decision point — the forecast for the commander's brief.

Participant: With the brief three days out and only two weeks of post-implementation data, I presented a forecast of continued low attack tempo, three to four a week, framed as Steady Watch holding. I could have given a wider range and flagged that two weeks isn't much of a track record, but the trend line looked clean and the commander wanted something decisive for the brief, not a hedge.

Interviewer: If the tribal dispute hadn't been resolved that week, would your Steady Watch conclusion have looked different to you?

Participant: Probably, yeah. If that dispute had still been active and attacks still dropped, I'd have been much more confident it was the checkpoints. With it resolved right alongside our posture change, I probably should have leaned harder into how much of that drop those other threads accounted for on their own.

Interviewer: And if District Y's spike had also faded without any posture change at all?

Participant: That would've made me second-guess the District X read pretty quickly — it'd suggest spikes like that just settle down on their own sometimes, checkpoints or not.

Interviewer: Anything about the week-five spike itself you'd weigh differently now?

Participant: Maybe how extreme it was compared to everything before it. Eleven against a baseline of three is a huge jump, and huge jumps like that don't usually stay huge. I focused on what we did in response rather than on how unusual that single week was to begin with.

</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Biased_1",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Intelligence Analyst (All-Source)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Sector Nightfall: Attack Tempo Assessment After Operation Steady Watch",
    "scenario_summary_internal": "An all-source intelligence analyst tracks weekly attack counts (IED and small-arms incidents) in District X over eight weeks. A baseline of roughly three attacks per week produces an anomalous spike to eleven attacks in week five, driven by a convergence of transient local factors (a religious festival drawing crowds, a resupplied weapons cache, and a flaring tribal land dispute). In week six, command implements a new checkpoint posture, Operation Steady Watch, partly on the analyst's recommendation. In weeks seven and eight, attack counts fall back to near-baseline levels (roughly three to four per week) as the transient factors resolve on their own. The analyst credits Steady Watch as the primary cause of the decline without weighing the likelihood that an extreme statistical outlier would revert toward the mean regardless of the intervention. This belief then shapes a resourcing recommendation for a neighboring district and a confident forecast to the battalion commander.",
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
        "outlier correction"
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
          "Analyst's assessment is forwarded to S3 and the company commander as the basis for sustaining the posture",
          "Commander requests the same posture be evaluated for District Y"
        ],
        "alternatives": [
          "Attribute the weeks 7-8 decline primarily to Steady Watch's deterrent effect",
          "Attribute the decline to the resolution of the transient local factors (festival, cache depletion, dispute mediation) that had converged in week 5, treating the extreme spike as an unusual peak likely to subside regardless of the checkpoint posture",
          "Withhold a firm causal judgment and request two more weeks of data before attributing cause"
        ],
        "intended_action": "Analyst concludes that Steady Watch is the primary driver of the decline, citing the magnitude of the drop as evidence of the posture's effectiveness, without weighing that week 5 was an extreme deviation from an established ~3/week baseline that the transient confounders alone would plausibly have reversed."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "District Y has its own eight-week SIGACTS history with a similar baseline (~2-3/week) and one anomalous spike to 9 in week 4, followed by a partial decline to 5-6 in subsequent weeks without any posture change",
          "Commander wants a resourcing recommendation: extend Steady Watch to District Y or hold current ISR allocation",
          "Analyst's District X assessment (from phase 2) is the primary input available"
        ],
        "new_information_after_decision": [
          "S3 begins provisioning checkpoint materials for District Y based on the recommendation",
          "District Y HUMINT source handler flags that District Y's spike had a different, still-unresolved local driver"
        ],
        "alternatives": [
          "Recommend replicating Steady Watch in District Y, expecting a comparable sharp decline based on the District X result",
          "Recommend a separate baseline and cause analysis for District Y before committing checkpoint resources",
          "Recommend reallocating resources to HUMINT source development in District Y instead of a checkpoint posture"
        ],
        "intended_action": "Analyst recommends extending Steady Watch to District Y, treating the District X outcome as a validated model of checkpoint effectiveness."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two consecutive weeks (7-8) of low attack counts in District X following Steady Watch implementation",
          "Command brief scheduled in three days requiring a forward-looking assessment",
          "No additional District X SIGACTS data beyond week 8 is yet available"
        ],
        "new_information_after_decision": [
          "Commander approves sustained Steady Watch funding for the following quarter based on the forecast",
          "Analyst is tasked to monitor for any deviation from the forecast in subsequent INTSUMs"
        ],
        "alternatives": [
          "Forecast continued low attack tempo (3-4/week) as a direct extrapolation of the two-week decline",
          "Present a wider forecast range with explicit uncertainty, noting the limited data window and possibility of tempo rising back toward or above baseline",
          "Defer any quantitative forecast and request an extended observation period before the brief"
        ],
        "intended_action": "Analyst presents a confident forecast of sustained low attack tempo to the commander, framed as the expected continuation of Steady Watch's demonstrated effect."
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
        "When you saw the decline in weeks 7-8, what evidence did you use to explain it, and what other explanations did you consider or set aside?",
        "What made you confident enough in the District X result to recommend the same approach for District Y?",
        "How did you decide what to tell the commander about future attack tempo, and what would have changed that forecast?"
      ],
      "closing_hypotheticals": [
        "If the tribal dispute had not been resolved that week, would your assessment of Steady Watch's effect have changed?",
        "If District Y's spike had also declined without any posture change, how would that have affected your confidence in the District X conclusion?",
        "Looking back, is there anything about the week-5 spike itself, apart from the checkpoint posture, that you'd weigh differently now?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "decision_point": 2,
        "mechanism": "Analyst observes an extreme, transient-factor-driven outlier (week 5 spike) followed by a decline back toward the established baseline, and attributes the full decline to a deliberate intervention (Steady Watch) without considering that an extreme deviation was statistically likely to revert toward the mean independent of the intervention.",
        "affected_reasoning_operation": "Causal attribution of an observed trend change following an extreme data point",
        "evidence_available_at_time": [
          "Eight weeks of SIGACTS data showing a ~3/week baseline, a single spike to 11 in week 5, and a decline to 3-4 in weeks 7-8",
          "HUMINT confirmation that the festival ended, the tribal dispute was mediated, and the resupplied cache was reportedly expended around the time of the spike",
          "Timing coincidence between Steady Watch implementation (week 6) and the observed decline (weeks 7-8)"
        ],
        "required_textual_manifestation": "The analyst explicitly credits Steady Watch as the primary or sole cause of the magnitude of the decline, references the size of the drop as proof of effectiveness, and does not raise the possibility that the extreme week-5 value itself made a reversion toward baseline likely regardless of the checkpoint posture, even though the resolved transient factors are mentioned only in passing or dismissed as secondary.",
        "plausible_nonbias_interpretation": "Steady Watch may indeed have had a genuine deterrent effect, and an analyst reasonably weighing checkpoint interdiction reports alongside the timing correlation could arrive at a similar conclusion through ordinary (non-biased) causal inference if they had also explicitly weighed and ruled out the alternative explanation.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "regression to the mean",
          "statistical regression",
          "mean reversion",
          "outlier correction",
          "base rate"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no paired control scenario specified for this generation run."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence versus absence of resolvable transient confounding factors (festival, cache depletion, tribal dispute mediation) coinciding with the week-5 attack spike",
      "original_state": "Transient local factors were present during the week-5 spike and resolved naturally by weeks 7-8, meaning the decline was overdetermined by both the intervention and natural reversion of an extreme outlier",
      "counterfactual_state": "No transient confounding factors are present; the week-5 spike reflects a genuine, sustained escalation in insurgent capability with no natural reason to revert, isolating whether Steady Watch alone can still produce a comparable decline",
      "variables_to_hold_constant": [
        "Baseline attack rate in weeks 1-4",
        "Timing of Steady Watch implementation (week 6)",
        "Magnitude and timing of the week-5 spike",
        "Analyst identity, role, and reporting cadence",
        "Command pressure and INTSUM deadline structure"
      ],
      "expected_causal_difference": "In the counterfactual, a sustained decline following Steady Watch would provide stronger, less confounded evidence of intervention effectiveness, whereas in the original scenario the decline is ambiguous between intervention effect and natural reversion of an extreme outlier.",
      "causal_test_question": "Does the presence of resolvable transient confounders during the spike change how confidently the decline can be attributed to Steady Watch versus natural reversion?"
    },
    "generation_checks": [
      "Confirm exactly four decision points exist, each with at least two alternatives.",
      "Confirm exactly one instance of 'Failure to recognize regression to the mean' is planned, located at decision point 2.",
      "Confirm decision points 1, 3, and 4 do not independently reproduce the same bias mechanism through new evidence-processing acts.",
      "Confirm bias terminology and explanations are excluded from the public interview text.",
      "Confirm total interview length falls within 1,215-1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm consequences described (sustained low tempo, resource extension to District Y) do not mechanically prove or disprove whether the week-5 to week-8 attribution was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Failure to recognize regression to the mean",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Failure to recognize regression to the mean"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Failure to recognize regression to the mean",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "mechanism": "Attributing the full magnitude of a post-outlier decline to a deliberate intervention (Steady Watch) while disregarding the statistical likelihood that an extreme deviation (week-5 spike) would revert toward the established baseline independent of that intervention.",
        "affected_reasoning_operation": "Causal attribution of trend change following an extreme data point",
        "evidence_source": "SIGACTS weekly attack counts (weeks 1-8) combined with HUMINT reporting on resolution of transient local factors coincident with the spike",
        "distinctiveness_requirement": "This is the only planned instance; no other decision point may independently manifest the same evidence-processing failure (ignoring outlier-driven reversion) with new evidence sources or moments."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "rtm_01",
        "bias": "Failure to recognize regression to the mean",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence versus absence of resolvable transient confounding factors coincident with the week-5 attack spike",
      "original_state": "Transient factors (festival, cache depletion, tribal dispute mediation) present and naturally resolved by weeks 7-8",
      "changed_state": "No transient confounding factors; spike reflects sustained capability escalation with no natural reason to revert",
      "variables_to_hold_constant": [
        "Baseline attack rate weeks 1-4",
        "Timing of Steady Watch implementation",
        "Magnitude and timing of week-5 spike",
        "Analyst identity and reporting cadence",
        "Command pressure and INTSUM deadline"
      ]
    },
    "scenario_id": "MD_Biased_1",
    "domain_id": "MD",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the clearest mechanism fit: the causal-attribution judgment made immediately after an extreme SIGACTS outlier reverts toward baseline, where transient confounders provide a documentable alternative explanation the analyst can be shown to underweight. Decision points 1, 3, and 4 were deliberately kept free of independent regression-to-the-mean evidence-processing acts to avoid double-counting the single requested instance.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Baseline attack rate weeks 1-4",
      "Timing of Steady Watch implementation",
      "Magnitude and timing of week-5 spike",
      "Analyst identity and reporting cadence",
      "Command pressure and INTSUM deadline"
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
        "segment_type": "choice_and_action_rationale",
        "raw_interview_anchor": "I recommended we not overreact with a full cordon-and-search ... we did push more ISR onto two suspected cache routes and stood up a limited checkpoint pilot.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Measured response rationale based on limited confirmation and uncertainty."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_and_action_rationale",
        "raw_interview_anchor": "Mainly time pressure and thin confirmation. We only had eight weeks of data total ... I didn't want to overcorrect off one bad week.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains a cautious response to sparse data and command pressure."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "causal_attribution_and_alternative_explanation_weighting",
        "raw_interview_anchor": "I told them Steady Watch was working. The numbers backed it up ... That's a big swing ... I treated those as secondary color ... I didn't really sit down and ask how much of that drop would've happened on its own just because week five was such an extreme outlier.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rtm_01"
        ],
        "ground_truth_rationale": "The participant attributes the decline primarily to Steady Watch while failing to consider natural reversion after an extreme spike."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "resource_allocation_recommendation",
        "raw_interview_anchor": "Given what I'd just seen in District X, I recommended rolling Steady Watch out to District Y too, expecting a similar sharp drop.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden manifest contains no independent instance at this downstream decision point."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "alternative_analysis_and_decision_rationale",
        "raw_interview_anchor": "I considered it, but time was short and District X felt like a validated model ... The Y handler did mention their spike had a different, still-unresolved driver.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification excludes an independent hidden instance here."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "forecast_and_communication_choice",
        "raw_interview_anchor": "I presented a forecast of continued low attack tempo ... I could have given a wider range ... but the trend line looked clean and the commander wanted something decisive.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "No separate hidden bias instance is planned for this forecast decision."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "retrospective_reasoning_reflection",
        "raw_interview_anchor": "Eleven against a baseline of three is a huge jump, and huge jumps like that don't usually stay huge. I focused on what we did in response rather than on how unusual that single week was.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This retrospective reflection is not a second hidden occurrence."
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
      "analysis_scope_note": "Analyzed the full CTA transcript for affirmatively evidenced cognitive, perceptual, memory, motivational, affective, social-influence, and group-decision biases. The participant consistently distinguished competing causal explanations, expressed uncertainty about the checkpoint effect, resisted pressure for a clean narrative, used limited and reversible decisions under data constraints, and explicitly considered counterfactual evidence. No bias-specific mechanism was sufficiently evidenced in the transcript."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [],
    "no_supported_biases_found": true,
    "limitations": [
      "Single-interview transcript; biases not manifested in verbal reasoning cannot be ruled out.",
      "Retrieved corpus passages were not applied because no identified occurrence met the evidentiary standard.",
      "The interviewer included retrospective counterfactual questions, but the participant's responses showed explicit uncertainty and alternative consideration rather than a bias-specific mechanism."
    ]
  }
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Biased_1_Sonnet_on",
  "interview_id": "MD_Biased_1",
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
