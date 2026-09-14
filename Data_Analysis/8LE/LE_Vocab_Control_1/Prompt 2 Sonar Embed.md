You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. This is being recorded for a training-review case study, your name won't be attached to the write-up, and you can skip anything you'd rather not answer. That work for you?

Participant: Yeah, that's fine. I've sat through a few of these for the sergeant's after-action reviews before.

Interviewer: Good. What's your role, and how long have you been doing patrol work?

Participant: Patrol officer, field response, seven years now. Nights mostly the last three.

Interviewer: Let's start with the incident. Walk me through it from the top.

Participant: Sure. About 2:05 in the morning, dispatch got an anonymous call about a vehicle idling suspiciously near the loading dock at the distribution warehouse off Route 12. Caller didn't give a vehicle description, nothing about occupants, no specifics at all. That area's had a run of cargo theft the last couple months, so it's a place we keep an eye on anyway. I was closest unit, backup was a few minutes out. I rolled up, parked back a bit instead of pulling right up on the dock, and watched for a minute. Saw one guy standing next to a parked pickup truck near the dock, looking at a clipboard. Nothing dramatic—no forced entry, no tools out, nothing urgent-looking.

Interviewer: What made you hold back and observe instead of approaching right away?

Participant: Habit, really. If somebody's actually up to something, walking straight up tips them off before you get a read on them. He wasn't doing anything that needed immediate action, so there wasn't a reason to rush it.

Interviewer: Okay, so you approach. What happens next?

Participant: I get out, identify myself, ask what he's doing there. He's calm, looks right at me, answers straight away—says he's a contracted HVAC tech waiting on the site manager to let him in for a scheduled after-hours repair. Shows me a contractor badge clipped to his jacket, hands over his license without me asking twice. While we're talking I notice a bulge in his coat pocket, kind of squared off, hard to tell what it is.

Interviewer: What did you do with that?

Participant: I asked him to keep his hands visible while I thought it through. He's calm, cooperative, story's consistent, paperwork on the clipboard lines up with an HVAC job—that all counts for something. But I still don't know what's in that pocket, and an unidentified object at two in the morning, alone, isn't something I can just wave off because the guy seems relaxed. So I weighed it as: the demeanor and the story lower the odds it's a problem, but they don't rule it out, and the bulge is still an open question either way. Ended up doing a brief pat-down, but I told him why—said something like, "you seem fine, but I've got to check this."

Interviewer: Let's build the full timeline before we go decision by decision. What happened after the pat-down?

Participant: Clean. Bulge was a folded work order and a multimeter. No weapon. His story still wasn't independently confirmed though, and backup hadn't shown up yet, so I had him stay put while dispatch checked whether the HVAC company actually had a work order with that warehouse for that night. Came back a few minutes later—yes, active account, scheduled after-hours repair, all legitimate. Site manager showed up right around then to let him in. I released him, wrote up the field contact, noted the pat-down and why, and that was it.

Interviewer: Let's go through it decision by decision. First: choosing to observe before approaching. What alternatives did you weigh?

Participant: I could've walked right up, or called dispatch back for more detail first. Calling back didn't seem worth it—the caller hadn't given much to work with anyway. Watching first gets me information without giving up the advantage of him not knowing I'm there yet.

Interviewer: Second—the pat-down decision. How did the calm demeanor and the pocket bulge actually factor together into that call?

Participant: Pretty directly, honestly. The demeanor mattered—if he'd been jumpy or wouldn't look at me, I'd have treated the bulge as a lot more urgent and probably backed off to wait for backup before getting that close. Since he was calm and the story checked out on its face, that brought my concern down some. But it didn't erase it, because none of that tells me what's actually in his pocket. So both things were in the mix—the calm cuts one way, the unidentified object cuts the other, and I made the call knowing neither one fully resolved the other.

Interviewer: Did the subject's explanation change how you saw the bulge?

Participant: Some. Once he mentioned the work order and the multimeter before I even patted him down, I had a guess what it probably was. But "probably" isn't the same as confirmed, so I still checked.

Interviewer: If he'd been visibly nervous instead of calm, would that have changed things?

Participant: Yeah, I'd have been quicker to create distance and wait on backup rather than getting in close for a pat-down solo. Nervousness plus an unknown object is a different risk picture than calm plus an unknown object.

Interviewer: And if there'd been no bulge at all, same calm demeanor, same story?

Participant: Then there's nothing physical to check. It'd just be a field interview, verify the story, and let him go once it holds up.

Interviewer: Third decision point—after the pat-down's clean, you keep him at the scene instead of releasing him right away. Why?

Participant: The story wasn't verified yet. Badge and ID looked legit, but I've seen contractor badges that were expired or from a job somebody didn't actually have anymore. Backup still hadn't arrived. Holding him a few extra minutes for dispatch to confirm the work order felt like the reasonable middle ground—not cutting him loose on an unconfirmed story, but not treating him like a suspect either.

Interviewer: Did you consider escorting him to the site office instead?

Participant: Thought about it, but the office was locked, nobody there to answer. Waiting on dispatch and the site manager made more sense than walking him around the property in the dark.

Interviewer: Fourth—closing it out. Why release with no citation instead of a trespassing warning?

Participant: Once dispatch confirmed the work order and the site manager showed up right after, there wasn't a factual basis left for a citation. He had a legitimate reason to be there, and it held up. Writing him up at that point would've just been penalizing him for being at his own job site.

Interviewer: What single piece of information, if it had come in earlier, would have changed how you handled this?

Participant: Honestly, if dispatch had been able to confirm the work order before I even got out of the car, most of this would've been a formality. The whole thing hinged on not having that confirmation up front.

Interviewer: How much did being alone without backup shape your pace?

Participant: Some. I moved a little more carefully closing distance, and I was more inclined to resolve the pocket question myself rather than just let it sit unanswered while I waited.

Interviewer: Looking back, is there anything you'd weigh differently next time?

Participant: Not really. I think I got the balance about right—gave the calm and the story their due, but didn't let them talk me out of checking something I genuinely couldn't identify. That's about as fair as you can be with limited information at two in the morning.

Interviewer: That's helpful, thank you. I think that covers everything I need.

Participant: No problem. Glad it worked out clean for him.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Vocab_Control_1",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Patrol Officer (Field Response)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Late-Night Vehicle Check at the Closed Loading Dock",
    "scenario_summary_internal": "A patrol officer responds to a dispatch call about a parked vehicle idling near a closed distribution warehouse after hours. Over the course of the stop, the officer must decide how to approach, whether to conduct a pat-down, whether to detain, and how to resolve the encounter. The subject turns out to be a contracted maintenance technician waiting for a site manager to grant after-hours access. This is a vocabulary- and structure-matched control paired with LE_Biased_1: same domain, role, setting type, decision count, technical vocabulary, and emotional tone, but with zero intended cognitive-bias instances. All cue integration in the pat-down decision is written to reflect balanced, proportionate weighting of both present and absent cues, with no asymmetric treatment embedded.",
    "occupational_realism": {
      "objective": "Determine whether a person near a closed commercial facility after hours poses a safety or criminal risk, resolve the stop safely and lawfully, and decide on appropriate action (release, further investigation, or arrest).",
      "setting": "Suburban distribution warehouse loading dock, closed for the night, dim exterior lighting, single officer on patrol, backup several minutes out",
      "constraints": [
        "Officer is alone until backup arrives",
        "Limited lighting restricts visual assessment",
        "Dispatch information is secondhand and vague ('vehicle idling suspiciously')",
        "Department policy requires reasonable suspicion before a pat-down",
        "Time pressure: officer must decide quickly whether the situation is escalating"
      ],
      "stakeholders": [
        "Patrol officer",
        "Subject (contracted maintenance technician)",
        "Dispatch/911 caller (anonymous, not present)",
        "Backup officer (arrives later)",
        "Warehouse site manager (indirect, property concerns)"
      ],
      "technical_terms_to_use": [
        "reasonable suspicion",
        "Terry stop",
        "pat-down",
        "field interview",
        "officer safety",
        "totality of the circumstances"
      ],
      "technical_terms_to_avoid": [
        "feature positive effect",
        "cognitive bias",
        "salience bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch call: anonymous caller reported a vehicle 'idling suspiciously' near a closed warehouse loading dock",
          "No description of the vehicle, occupants, or specific behavior provided",
          "Time is 2:05 a.m., area has had recent cargo theft incidents"
        ],
        "new_information_after_decision": [
          "On arrival, officer sees one man standing beside a parked pickup truck near the loading dock, checking a clipboard"
        ],
        "alternatives": [
          "Approach directly and initiate contact immediately",
          "Observe from a distance first to assess behavior before approaching",
          "Call dispatch for more details before acting"
        ],
        "intended_action": "Officer parks at a distance and briefly observes before approaching on foot."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Subject is calm, makes eye contact, answers initial questions coherently",
          "Subject explains he is a contracted HVAC technician waiting for the site manager to grant after-hours access for a scheduled repair",
          "Officer notices a visible bulge in the subject's coat pocket",
          "Subject shows no shaking, no avoidance of eye contact, no attempt to move away, no change in breathing or speech pattern"
        ],
        "new_information_after_decision": [
          "Pat-down reveals the bulge is a folded work order and a multimeter, not a weapon"
        ],
        "alternatives": [
          "Ask the subject to voluntarily show pocket contents without a pat-down",
          "Conduct a pat-down after weighing both the pocket bulge and the subject's calm, cooperative demeanor together",
          "Continue the conversation and reassess after a few more questions"
        ],
        "intended_action": "Officer weighs the pocket bulge alongside the subject's calm, cooperative demeanor and consistent paperwork, and decides a brief pat-down is still warranted given the unidentified object, while explicitly noting the calm demeanor as a factor that tempers but does not eliminate the concern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pat-down is clean; no weapon or contraband found",
          "Subject's ID matches a valid driver's license and a contractor badge",
          "Backup officer has not yet arrived",
          "Subject's story about waiting for the site manager has not been independently confirmed"
        ],
        "new_information_after_decision": [
          "Dispatch confirms the HVAC contractor has an active work order with the warehouse for that night"
        ],
        "alternatives": [
          "Detain the subject further pending dispatch confirmation",
          "Release the subject pending a callback from dispatch",
          "Escort the subject to the site office to verify in person"
        ],
        "intended_action": "Officer requests dispatch confirmation while keeping the subject at the scene, without further escalation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch confirms the active work order and expected after-hours repair",
          "No further evidence of wrongdoing",
          "Site manager arrives moments later to grant access"
        ],
        "new_information_after_decision": [
          "Encounter concludes without arrest; officer files a field report noting the stop"
        ],
        "alternatives": [
          "Release the subject with no further action",
          "Issue a formal warning or citation for trespassing",
          "Request the subject leave the area immediately as a precaution"
        ],
        "intended_action": "Officer releases the subject and documents the stop as resolved."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew before you arrived on scene.",
        "What was your initial read of the situation when you pulled up?"
      ],
      "timeline_reconstruction": [
        "What did you notice first when you approached the subject?",
        "What happened between your initial observation and the pat-down decision?",
        "What did dispatch tell you, and when?"
      ],
      "decision_point_probes": [
        "What specifically made you decide to pat him down at that point?",
        "How did the calm demeanor and the pocket bulge factor together into that call?",
        "What made you decide to hold him at the scene rather than release him right away?",
        "What led you to close out the stop the way you did?"
      ],
      "information_sources": [
        "How much weight did you give the dispatch call versus what you observed yourself?",
        "Did the subject's explanation change how you viewed the bulge in his pocket?"
      ],
      "closing_hypotheticals": [
        "If the subject had been visibly nervous instead of calm, would that have changed your decision?",
        "If there had been no bulge but the same calm demeanor, would you still have patted him down?",
        "Looking back, is there anything you'd weigh differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "LE_Biased_1",
      "features_to_match": [
        "Domain vocabulary (reasonable suspicion, Terry stop, pat-down, field interview, officer safety, totality of the circumstances)",
        "Structure: four decision points in the same sequence (observe/approach, pat-down decision, continued-detention decision, release decision)",
        "Difficulty and subtlety of reasoning presented",
        "Actor roles: solo patrol officer, cooperative subject with a work-related explanation, anonymous caller, delayed backup, third-party corroborator",
        "Emotional tone: measured, procedural, mildly tense due to solitude and ambiguity",
        "Overall decision count and probe categories"
      ],
      "features_to_remove_or_change": [
        "Underlying incident specifics (warehouse loading dock instead of strip mall, HVAC technician instead of delivery driver)",
        "The asymmetric cue-weighting mechanism at the pat-down decision, replaced with explicit balanced consideration of both the pocket bulge and the calm demeanor",
        "Object found in pocket (work order and multimeter instead of invoice clipboard and charger)"
      ],
      "ambiguity_boundary": "Reasoning may remain genuinely uncertain (e.g., unconfirmed story, unidentified object) but must not include the intended asymmetric presence/absence cue-weighting pattern reserved for the biased condition."
    },
    "counterfactual_specification": {
      "causal_variable": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "counterfactual_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "NOT_APPLICABLE",
      "causal_test_question": "NOT_APPLICABLE"
    },
    "generation_checks": [
      "Zero Feature positive effect instances embedded; pat-down decision explicitly integrates both the bulge and the calm demeanor as joint, proportionate factors",
      "No bias terminology appears in probe_plan or timeline",
      "Four decision points present, each with at least two alternatives",
      "Word count target 1,350 (range 1,215-1,485) achievable given four decision points and probe set without repetitive exposition",
      "Vocabulary, structure, actor roles, and emotional tone matched to LE_Biased_1",
      "Underlying incident specifics changed sufficiently to avoid duplication while preserving parallel structure",
      "No unrequested bias intentionally embedded anywhere in timeline or probes"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Feature positive effect",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended instances required by vocabulary_control condition rules, overriding the caller-supplied manifest value of 1; the pat-down decision must instead show explicit, proportionate joint weighting of the present cue (pocket bulge) and the absent cue (lack of nervous/evasive behavior)."
      }
    ],
    "target_bias_names": ["Feature positive effect"],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Feature positive effect",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "LE_Biased_1",
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "changed_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Vocab_Control_1",
    "domain_id": "LE",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control condition mandates zero intended occurrences of all named target biases per condition rules, regardless of caller-supplied manifest value.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology set",
      "Four-decision-point structure and sequence",
      "Actor roles and stakeholder set",
      "Emotional tone and difficulty level",
      "Probe category coverage (cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, hypotheticals)"
    ],
    "generation_warnings": [
      "The caller-supplied exact-occurrence manifest specified 1 occurrence of Feature positive effect, but condition rules for vocabulary_control require zero intended instances of all named target biases. This specification overrides the manifest count to 0 in accordance with the CONDITION RULES section, and documents the override here for audit purposes rather than silently reducing an occurrence count under the biased condition rules."
    ]
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "LE_Vocab_Control_1_DP1",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Choosing to observe before approaching: the officer briefly watches from a distance because the call is vague, the area has recent cargo theft, and immediate action is not required.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden validation requires zero Feature positive effect instances; the officer proportionately weighs the vague call, recent theft context, and observed behavior."
        },
        {
          "segment_id": "LE_Vocab_Control_1_DP2",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Pat-down decision: the officer weighs the calm, cooperative demeanor and consistent paperwork against the still-unidentified pocket bulge, then performs a brief pat-down.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden validation requires zero Feature positive effect instances; the officer explicitly integrates the present bulge and absent nervous or evasive cues as joint, proportionate factors."
        },
        {
          "segment_id": "LE_Vocab_Control_1_DP3",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Continued detention decision: after a clean pat-down, the officer keeps the subject at the scene briefly while dispatch verifies the unconfirmed work-order story.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden validation requires zero Feature positive effect instances; the officer uses unresolved verification and delayed backup to choose a limited, non-escalatory hold."
        },
        {
          "segment_id": "LE_Vocab_Control_1_DP4",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "Release decision: after dispatch confirms the work order and the site manager arrives, the officer releases the subject and documents the field contact.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden validation requires zero Feature positive effect instances; once corroboration removes the factual basis for enforcement, the officer releases the subject."
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
      "analysis_scope_note": "Analyzed a single patrol incident after-action interview for affirmative evidence of bias-specific mechanisms affecting the officer's reasoning or decisions. The participant describes observation, approach, pat-down, detention for verification, and release decisions. No identified occurrence met the conservative mechanism-first threshold, so no corpus passage was used for an occurrence-level label."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [],
    "no_supported_biases_found": true,
    "limitations": [
      "The analysis relies on retrospective self-report rather than direct observation of real-time cognition.",
      "The participant provides explicit counterfactual reasoning and weight-balancing, which reduces inferential evidence of bias but does not rule out unmeasured cognitive bias.",
      "Retrieved corpus passages address aviation, fire evacuation, automation, search, usability, and cybersecurity contexts; none provided a directly applicable field-policing decision case.",
      "Hypothetical questions in the interview were not treated as evidence that the speaker held a bias.",
      "No affirmative bias-specific mechanism was identified, so retrieved_corpus_support_used is false."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Vocab_Control_1_Sonar_on",
  "interview_id": "LE_Vocab_Control_1",
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
