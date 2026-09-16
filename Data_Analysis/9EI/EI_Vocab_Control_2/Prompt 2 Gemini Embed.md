You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. This is for our instructional practice research and will be kept confidential. Can you start by telling me your role and how the Bridge Literacy pilot came about?

Participant: Sure. I'm the Curriculum Coordinator for K-5, and I also run our instructional coaching cycle across the elementary buildings. I brought Bridge Literacy in after seeing it presented at a state conference last spring. It's a structured literacy approach, more explicit phonics sequencing than what we'd been using. I pitched it to the superintendent, and we set it up as a trimester pilot in six classrooms across our two elementary schools.

Interviewer: And what were you trying to accomplish with the checkpoint review you did partway through?

Participant: The board needed a scale-up recommendation before the next budget cycle, so I had to look at the trimester oral reading fluency benchmark data, figure out if the pilot was working, and decide what to tell the finance committee. There's real competition for dollars — the math intervention team wants the same PD budget — so whatever I brought needed to hold up under questions.

Interviewer: Walk me through what happened when the data actually came in.

Participant: The literacy specialist sent me the classroom-level fluency results in early February. Three classrooms were clearly above the expected growth rate, three were flat or mixed. Before I drew any conclusions, I asked her to check something that had been bothering me — the two schools had administered the benchmark on different days because of a scheduling conflict, and I wanted to know whether that gap could be distorting results anywhere, not just in the classrooms that happened to come in flat.

Interviewer: Why did you want it checked across all six rather than just the ones that looked off?

Participant: Because the scheduling issue wasn't specific to any classroom — it applied to the testing window generally. If I only went looking for problems in the rooms with disappointing numbers, I'd have no way of knowing whether the same issue was quietly present in the rooms that looked fine. It seemed like the only fair way to trust the comparison.

Interviewer: What did you learn afterward?

Participant: The specialist came back about a week later and said testing conditions were actually pretty similar across all six classrooms — the day-to-day difference wasn't significant. Separately, she found that one flat classroom had unusually high absenteeism that same week, which probably explained more of that particular result than timing did.

Interviewer: What alternatives did you weigh before deciding how to handle the review?

Participant: I could have just accepted the gain classrooms and focused all my attention on explaining away the flat ones. Or waited entirely until a full audit was done before forming any impression. I went with checking everything at once instead, mostly because I didn't want to end up defending a number in front of the board that I hadn't actually stress-tested.

Interviewer: Let's move to the board meeting prep. What did that involve?

Participant: I had fifteen minutes on the agenda, and the math team was presenting right after me. I had the full six-classroom data set plus a walkthrough-observation log the specialist and I had been keeping. I decided to bring a highlights slide with the aggregate trend line rather than all six classrooms individually — mostly a time issue. Fifteen minutes isn't enough to walk through six separate data profiles and still leave room for questions.

Interviewer: Any consequence from that choice?

Participant: One board member asked for classroom-by-classroom detail I hadn't put on the slide. I had it on hand, just not formatted for presentation, so I was able to answer, but I was working from memory a bit more than I'd have liked.

Interviewer: Around the same time, you had PD feedback to review. What did that look like?

Participant: Five of six pilot teachers filled out a survey after the coaching session, rated it helpful or very helpful. One comment mentioned the pacing guide felt rushed for lower-performing students. It's a small sample and it was voluntary, so I noted that caveat when I summarized it — I didn't want to present five responses as if that settled anything about how teachers overall felt.

Interviewer: Did you follow up on the teacher who didn't respond?

Participant: Not immediately. The specialist later mentioned the one non-response was from a teacher in a flat classroom, which made me wonder whether we were hearing a slightly rosier picture than the full group would give. I flagged that as a limitation in the write-up rather than treating the survey as representative.

Interviewer: Let's get to the recommendation memo. How did you explain the fluency gains?

Participant: The aggregate number was a modest net gain across all six classrooms. I'd been doing biweekly coaching visits in four of the six rooms, and those classrooms also had new decodable-text materials and, in a couple of cases, smaller class sizes than our typical rosters. When I wrote the memo, I tried to lay out all of that together rather than pointing to one piece — coaching, materials, and class size were all present at the same time in the classrooms that improved most.

Interviewer: What about the two classrooms that improved without your direct coaching visits?

Participant: That was actually one of the more useful data points. Those two rooms had the new materials too, and one of them had a smaller roster, so it suggested the materials and class-size piece might be doing real work independent of coaching. I included that in the memo as a reason to be cautious about crediting coaching alone.

Interviewer: A board member raised a related point, is that right?

Participant: Right, someone asked directly how those two classrooms improved without my visits. I said that was exactly why I was recommending a staged approach — bring in the materials and coaching together in a next round, but track classrooms with and without direct coaching support separately so we can actually see what's carrying the result before committing to a full districtwide coaching build-out.

Interviewer: What would have needed to be different for you to weight one factor more heavily than the others?

Participant: Probably a design where coaching, materials, and class size weren't all bundled together in the same rooms. Right now they move together, so I don't think the data lets anyone single one out with confidence. I said as much in the memo.

Interviewer: If someone else had gotten these same results without your involvement, how do you think they'd have explained the gains?

Participant: Probably about the same way I did — pointing at materials, class size, and coaching together, since all three were present. I don't think my being the one running the coaching changes what the data can and can't support.

Interviewer: And if the classrooms that struggled had been the ones you were personally coaching, do you think your review process would have looked any different?

Participant: I don't think so. I'd still have wanted the testing conditions checked everywhere before drawing conclusions — that part wasn't really about which rooms I was in.

Interviewer: Looking back, what would you do differently if you ran this checkpoint again?

Participant: I'd try to get the specialist's testing-condition review done earlier, before the board deadline was quite so close, so I'm not doing that verification under quite as much time pressure. And if we run another round of the pilot, I'd try to stagger which classrooms get coaching versus materials only, so the next causal story isn't as tangled as this one.

Interviewer: That's really helpful context. Thank you for walking through this in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Vocab_Control_2",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "Curriculum Coordinator / Instructional Coach",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Bridge Literacy Pilot: Balanced Mid-Year Review (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A district Curriculum Coordinator who introduced a new structured-literacy pilot ('Bridge Literacy Program') across six elementary classrooms conducts a trimester checkpoint review to decide whether to recommend district-wide scale-up. The pilot data are mixed, mirroring the paired scenario's domain, actors, constraints, and decision structure, but the coordinator applies consistent evidentiary scrutiny across all classrooms and distributes causal credit for observed gains across multiple contributing factors rather than centering her own coaching role.",
    "occupational_realism": {
      "objective": "Decide whether to recommend district-wide scale-up of the Bridge Literacy Program to the board finance committee, using one trimester of pilot data.",
      "setting": "Mid-size K-5 public school district; six pilot classrooms across two elementary schools; single literacy specialist supporting the coordinator; upcoming board budget cycle with competing requests from a math-intervention initiative.",
      "constraints": [
        "Only one trimester of assessment data available before the funding decision deadline",
        "Limited PD and coaching budget must be split between literacy and math initiatives",
        "Pilot classrooms were not randomly assigned; some had smaller class sizes",
        "Board meeting agenda time is limited to 15 minutes for the literacy update",
        "Testing window differed slightly by school due to scheduling conflicts"
      ],
      "stakeholders": [
        "Superintendent",
        "Building principals",
        "Pilot classroom teachers",
        "District literacy specialist",
        "School board finance committee",
        "Parents of pilot students"
      ],
      "technical_terms_to_use": [
        "structured literacy",
        "oral reading fluency benchmark",
        "trimester pilot",
        "fidelity of implementation",
        "instructional coaching cycle",
        "walkthrough data",
        "baseline assessment",
        "tiered intervention",
        "scale-up recommendation",
        "PD session feedback"
      ],
      "technical_terms_to_avoid": [
        "biased assimilation",
        "egocentric bias",
        "confirmation bias",
        "self-serving attribution",
        "motivated reasoning",
        "cognitive bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Coordinator advocated for adopting Bridge Literacy after attending a conference session on it",
          "Three of six pilot classrooms show fluency gains at or above benchmark growth rate",
          "Three classrooms show flat or mixed fluency growth",
          "The literacy specialist flags that the two schools administered the benchmark on different days within the testing window"
        ],
        "new_information_after_decision": [
          "Literacy specialist confirms testing conditions were substantively similar across all six classrooms",
          "One 'flat' classroom's teacher reports high student absenteeism during the testing week"
        ],
        "alternatives": [
          "Apply the same level of testing-condition review to all six classrooms regardless of outcome direction",
          "Focus scrutiny only on the three non-gain classrooms",
          "Postpone any interpretation until the literacy specialist audits testing conditions in all six classrooms"
        ],
        "intended_action": "Coordinator asks the literacy specialist to review testing conditions across all six classrooms at the same time, treating the scheduling discrepancy as a data-quality question that could affect any classroom rather than one specific to the non-gain group."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Board meeting agenda allows 15 minutes for the literacy update",
          "Full data set includes both classroom-level fluency scores and a summary walkthrough-observation log",
          "Math-intervention team is also requesting agenda time and funding"
        ],
        "new_information_after_decision": [
          "A board member asks for classroom-level detail that wasn't included in the highlights-only slide"
        ],
        "alternatives": [
          "Bring the full six-classroom data set with methodology notes for transparency",
          "Bring a highlights-only summary emphasizing aggregate trend lines to fit the time slot",
          "Bring only the three gain-classroom results as illustrative case studies"
        ],
        "intended_action": "Coordinator selects a highlights-only summary slide to fit the fifteen-minute slot, while keeping the full classroom-by-classroom figures on hand to answer follow-up questions."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Post-PD survey returned by 5 of 6 pilot teachers rates the coaching cycle as 'helpful' or 'very helpful'",
          "One teacher's written comment notes the pacing guide felt rushed for lower-performing students",
          "Survey sample size is small and response was voluntary"
        ],
        "new_information_after_decision": [
          "Literacy specialist notes that the one non-responding invitation went to a teacher in a non-gain classroom"
        ],
        "alternatives": [
          "Report the survey results with an explicit caveat about small sample size and nonresponse",
          "Report the survey results as broadly representative of teacher sentiment without caveats",
          "Follow up individually with the non-responding teacher before drawing conclusions"
        ],
        "intended_action": "Coordinator reports the survey with an appropriate caveat about sample size and voluntary response, treating the result as suggestive rather than conclusive."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Aggregate pilot data show a modest net fluency gain across the six classrooms",
          "Pilot classrooms also benefited from smaller class sizes, new decodable-text materials, and varying teacher experience levels",
          "Coordinator personally conducted biweekly coaching visits in four of the six classrooms",
          "Budget committee requires a causal rationale to justify scale-up cost, including additional coaching staff"
        ],
        "new_information_after_decision": [
          "A board member asks how the two classrooms without coordinator visits also showed gains"
        ],
        "alternatives": [
          "Attribute the gains to a combination of factors: new materials, smaller class sizes, teacher effort, and coaching support",
          "Attribute the gains primarily to the frequency and quality of the coordinator's own coaching visits",
          "Withhold a causal attribution and recommend a controlled follow-up study before scaling"
        ],
        "intended_action": "Coordinator's recommendation memo describes the fluency gains as resulting from a combination of coaching, materials, and class-size factors, notes that two non-visited classrooms also improved, and recommends a staged scale-up that evaluates each contributing factor rather than assuming coaching alone explains the results."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how the Bridge Literacy pilot came about and your role in it.",
        "What was your objective going into the trimester checkpoint review?"
      ],
      "timeline_reconstruction": [
        "What did you see first when the trimester fluency data came in?",
        "What did you do after noticing the split between gain and non-gain classrooms?",
        "How did you decide what to present at the board meeting?",
        "Walk me through how you read the PD feedback survey results.",
        "How did you arrive at your final scale-up recommendation?"
      ],
      "decision_point_probes": [
        "What made you ask the specialist to check testing conditions across all six classrooms rather than just some?",
        "What information did you have about testing conditions in the gain classrooms at that point?",
        "Why did a highlights-only summary make sense for the board slot?",
        "How representative do you think the survey responses were of all six classrooms?",
        "What factors did you weigh when writing the causal explanation in the memo?",
        "How did you decide how much weight to give coaching versus other contributing factors?"
      ],
      "goals_and_alternatives": [
        "What other ways could you have weighed the classroom data?",
        "What would have changed your view of the testing-condition issue?",
        "What alternative explanations did you consider for the two non-visited classrooms improving?"
      ],
      "decision_basis_and_experience": [
        "Has something like this happened in a previous pilot you've run?",
        "What in your prior experience shaped how you read this data?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure were you under when preparing for the board meeting?",
        "What were you most uncertain about when writing the final recommendation?"
      ],
      "closing_hypotheticals": [
        "If the non-gain classrooms had been the ones you personally coached, do you think your review process would have looked any different?",
        "If someone else had gotten the same fluency results without your involvement, how would you have explained the gains?",
        "What would you do differently if you ran this checkpoint review again?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "EI_Biased_2",
      "features_to_match": [
        "Domain vocabulary (structured literacy, oral reading fluency benchmark, fidelity of implementation, instructional coaching cycle, walkthrough data, tiered intervention, scale-up recommendation)",
        "Six-classroom, two-school pilot structure with a trimester assessment window",
        "Same stakeholders: superintendent, principals, pilot teachers, literacy specialist, board finance committee",
        "Same four-decision-point sequence: mixed-data review, board presentation under time constraint, PD survey interpretation, causal-attribution memo",
        "Same constraints: budget competition with math intervention, 15-minute board slot, testing-schedule discrepancy, unequal class sizes",
        "Same emotional tone: measured, deadline-driven, professionally cautious",
        "Same probe categories and approximate interview length"
      ],
      "features_to_remove_or_change": [
        "Remove asymmetric methodological scrutiny of disconfirming versus confirming classroom data; apply uniform scrutiny across all six classrooms",
        "Remove overattribution of shared outcome gains to the coordinator's personal coaching involvement; distribute causal credit across coaching, materials, class size, and teacher factors",
        "Ensure the coordinator's reasoning at every decision point is explainable by legitimate time constraints, sampling caveats, or genuine uncertainty rather than a favorable prior belief or self-referential weighting"
      ],
      "ambiguity_boundary": "Not applicable in the strict ambiguous_control sense; this is a vocabulary-matched control requiring balanced, non-intentionally-biased reasoning rather than deliberately underdetermined reasoning."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm zero intended instances of Biased Assimilation and zero intended instances of Egocentric bias appear anywhere in the interview.",
      "Confirm decision point 1 shows uniform, outcome-independent scrutiny applied to both gain and non-gain classrooms.",
      "Confirm decision point 4 distributes causal credit for fluency gains across coaching, materials, class size, and teacher factors without centering the coordinator's personal contribution.",
      "Confirm decision points 2 and 3 mirror the paired scenario's neutral, defensible reasoning (time-constrained presentation choice; appropriately caveated survey interpretation).",
      "Confirm domain vocabulary, actors, constraints, tone, and four-decision-point structure match the paired scenario EI_Biased_2.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable without repetitive exposition.",
      "Confirm no bias labels, definitions, or psychological explanations appear in the interview text."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Biased Assimilation",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended occurrences; coordinator must apply uniform scrutiny to all classroom data regardless of outcome direction"
      },
      {
        "bias": "Egocentric bias",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended occurrences; coordinator must distribute causal credit across multiple contributing factors without centering personal contribution"
      }
    ],
    "target_bias_names": [
      "Biased Assimilation",
      "Egocentric bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Biased Assimilation",
        "requested_occurrences": 0
      },
      {
        "bias": "Egocentric bias",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "EI_Biased_2",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Vocab_Control_2",
    "domain_id": "EI",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control condition mandates zero intended instances of all named target biases regardless of any manifest occurrence counts supplied by the caller. The caller-supplied manifest (1 occurrence each of Biased Assimilation and Egocentric bias) is overridden to zero per the condition rules for vocabulary_control, and this override is recorded in generation_warnings.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Six-classroom, two-school pilot structure and trimester timeline",
      "Stakeholder roster and role of the Curriculum Coordinator",
      "Four-decision-point narrative structure and sequence",
      "Budget-competition, board-time, and testing-schedule constraints",
      "Emotional tone and overall narrative complexity",
      "Approximate interview length and probe category coverage"
    ],
    "generation_warnings": [
      "The input manifest for this request specified 1 occurrence each of Biased Assimilation and Egocentric bias; per the CONDITION RULES, vocabulary_control requires zero intended instances of all named target biases. The manifest occurrence counts were overridden to zero to comply with the control condition, and this override is documented here rather than silently applied."
    ]
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  null
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
      "analysis_scope_note": "Evaluated the full interview transcript for affirmatively demonstrated cognitive bias occurrences. The participant's described reasoning consistently included preemptive checks, alternative-cause consideration, and explicit disclosure of limitations; no distinct bias mechanism was demonstrated with sufficient evidence to be identified."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [],
    "no_supported_biases_found": true,
    "limitations": [
      "The analysis relies only on the participant's self-reported decision process; internal cognitive states are not directly observable.",
      "The participant's statements are largely retrospective and may be subject to self-presentation or memory limitations, but the transcript itself does not affirm a specific bias mechanism.",
      "Portions of the interview describe hypothetical counterfactuals or rejected decision alternatives; these were not treated as evidence of actual biased reasoning."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Vocab_Control_2_Gemini_on",
  "interview_id": "EI_Vocab_Control_2",
  "system_prompt_id": "Gemini",
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
