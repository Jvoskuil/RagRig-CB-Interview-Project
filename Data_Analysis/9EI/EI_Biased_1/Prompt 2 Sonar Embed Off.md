You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a workplace research project on how teachers make placement decisions, and you can decline to answer anything or stop at any point. Sound okay?

Participant: Yes, that's fine.

Interviewer: Great. Can you tell me a bit about your role and how long you've been teaching math here?

Participant: I've taught high school math for eleven years, the last six here. I mostly teach Algebra II and Geometry, and I'm usually the one who handles course placement questions when a student transfers in mid-year, since I know the sequencing best.

Interviewer: And walk me through, generally, what happens when a transfer student shows up without a complete academic record?

Participant: It varies. Sometimes the transcript is solid and we just slot them in. Other times, like this case, the transcript alone doesn't tell us enough, so we pull in a diagnostic test, maybe an observation, and go from there. The counselor coordinates logistics, but the placement call is mine, with my chair signing off.

Interviewer: Let's talk through the specific incident you had in mind. Can you give me the full account, start to finish?

Participant: Sure. A junior transferred in from out of state in early October. His transcript listed a "B+" in "Algebra II Honors," but the school wasn't one I recognized, and the counselor couldn't verify their grading scale or how rigorous that course actually was. We had about a week before the schedule locked, so I didn't have much runway. My first instinct was just to trust the transcript and drop him into Algebra II, but the ambiguity bothered me — I didn't want to either shortchange him with an easier class or set him up to fail in one that assumed skills he didn't have. So I asked my chair if we could hold off a few days and get a diagnostic test done, plus sit him in on one of my classes to see how he handled a formative assessment live. She agreed.

Interviewer: What happened next?

Participant: The diagnostic came back at the 72nd percentile against grade-level norms, which is solid. I also had his transcript GPA, which I converted to our 100-point scale as best I could — that conversion is always a little shaky since I don't actually know how their department curved things. Then I sat him in on a quiz during my third-period class, and he got a 78. On top of that, I had him fill out a short self-assessment where he rated his own algebra confidence, and he put himself at an 8 out of 10. So by the deadline I had four numbers in front of me.

Interviewer: How did you get from four numbers to a decision?

Participant: I converted everything to the same 100-point scale and averaged the four together. That gave me a composite right around 79, which cleared our department's cutoff of 75 for Algebra II placement, so I placed him there and my chair signed off on the figure.

Interviewer: Let's reconstruct the order things arrived in a bit more precisely. What came first?

Participant: The transcript came with his enrollment paperwork on day one. The diagnostic was scheduled for day three. The classroom observation happened day four, same day as the self-assessment survey, since I had him do both during that visit. I finalized everything by day five to make the deadline.

Interviewer: When each new piece came in, what did you do with it?

Participant: Mostly just logged it and waited until I had all four before doing anything with the numbers. I didn't want to prejudge based on one piece — that's actually why I asked for more data in the first place instead of just going with the transcript alone.

Interviewer: Going back to that first decision — holding off versus placing him immediately based on the transcript. What tipped you toward waiting?

Participant: The uncertainty around the prior school's rigor. A "B+" from a school I don't know isn't the same as a "B+" here. I've been burned before trusting an out-of-state label at face value, so I wanted more direct evidence before locking him in.

Interviewer: Once you had the diagnostic, transcript conversion, quiz grade, and self-report, which of those did you consider most important?

Participant: Honestly, I looked at them as four inputs into one number rather than ranking them. The goal was to get a composite score I could defend to my chair, something that wasn't just my gut feeling.

Interviewer: Did you consider treating any of them differently, given they came from pretty different sources?

Participant: I thought about it briefly, but averaging felt like the fairest way to combine them without me injecting extra subjectivity into which one mattered more. If I started picking and choosing weights, that's its own kind of judgment call, and I wanted the number to feel more objective than that.

Interviewer: Had you handled a composite score like this before?

Participant: A couple times, yes, and I've generally just averaged the available measures. It's quick, and it's easy to explain to a parent or administrator.

Interviewer: How much time pressure were you under at that point?

Participant: A fair amount — we were basically at the deadline day. I didn't have room to request another data point even if I'd wanted to.

Interviewer: How confident were you that all four numbers deserved equal footing in that calculation?

Participant: I didn't really stop to weigh that question at the time. I was focused on getting to a number that cleared or didn't clear the cutoff.

Interviewer: Moving to the third point — a few weeks in, he scored 55 on his first unit test, below the class median. What went through your mind?

Participant: That was concerning, but not alarming yet. His homework completion was strong and he still reported feeling confident. I've seen transfer students hit a rough patch adjusting to a new teacher's style and pacing before leveling out, so I didn't want to overreact to one test.

Interviewer: What alternatives did you weigh?

Participant: Move him down to standard track right away, or keep him in Algebra II with extra support and watch the trend. I chose the second option and set up twice-weekly tutoring.

Interviewer: What made you favor waiting over reassigning him immediately?

Participant: One test isn't the whole picture, and reassigning mid-quarter has real costs — transcript continuity, disruption, his own confidence. I wanted more evidence before making that call.

Interviewer: And the fourth point — end of quarter, he had a C-, with an upward trend the last three weeks. His parent asked in writing that he stay in Algebra II. What was your reasoning there?

Participant: The recent trend mattered a lot to me — it suggested the tutoring was working and he was catching up. The counselor also flagged that switching tracks mid-year could complicate his transcript. Combined with the parent's request, keeping him in with continued support seemed like the right call.

Interviewer: Looking back, is there anything you'd have wanted to know earlier that might have changed the placement decision?

Participant: Probably a second observation period. One 50-minute sit-in is a pretty thin slice of evidence, and I'd have liked a bit more before finalizing that composite number.

Interviewer: If the self-report survey had shown low confidence instead of high, do you think your composite score — and the placement — would have come out differently?

Participant: Yes, actually, since it was one of four numbers going into a straight average, a lower self-rating would have pulled the total down and possibly under the cutoff.

Interviewer: If only the diagnostic test had been available, without the other three measures, do you think you'd have placed him the same way?

Participant: Probably, since 72nd percentile alone is a reasonably strong signal. But I wouldn't have felt as comfortable relying on just one number for something this consequential.

Interviewer: Anything you'd do differently next time you face a similar composite decision?

Participant: I think I'd slow down and think harder about how the pieces relate to each other before just averaging them, especially when they're not really measuring the same thing with the same precision. At the time, though, it felt like the practical way to turn four different pieces of paper into one decision.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Biased_1",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "High School Classroom Teacher",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Composite Placement Decision for a Mid-Semester Transfer Student",
    "scenario_summary_internal": "A high school math teacher must place a newly transferred junior into either Algebra II or a lower track within a one-week scheduling deadline. Evidence arrives in stages: an ambiguous prior transcript, a standardized diagnostic test, a single classroom observation grade, and a student self-report confidence survey. At the composite-scoring decision point, the teacher combines these four inputs by simple unweighted averaging rather than weighting them according to their differing reliability, producing a placement score that appears objective but is not defensibly weighted. Later decision points involve genuine, non-biased uncertainty as the teacher monitors and adjusts support based on emerging performance data.",
    "occupational_realism": {
      "objective": "Determine an appropriate math course placement for a newly transferred junior using multiple imperfect information sources within a one-week scheduling deadline, then monitor and adjust the placement across the grading period.",
      "setting": "Suburban public high school; mid-semester transfer intake; math department scheduling process involving the classroom teacher, department chair, and school counselor.",
      "constraints": [
        "One-week deadline before the master schedule locks",
        "Prior school transcript uses an unfamiliar grading scale with no verified equivalency table",
        "No direct access to the student's previous teacher for verification",
        "Only one 50-minute period available for direct classroom observation before the deadline",
        "Department administrative process requires a single composite placement figure for chair sign-off",
        "Ongoing full course load limits time for individualized diagnostic follow-up"
      ],
      "stakeholders": [
        "Classroom teacher (participant)",
        "Department chair",
        "School counselor",
        "Transfer student",
        "Student's parent"
      ],
      "technical_terms_to_use": [
        "diagnostic assessment",
        "course placement",
        "composite score",
        "transcript equivalency",
        "formative assessment",
        "grading scale conversion",
        "unit assessment",
        "intervention support"
      ],
      "technical_terms_to_avoid": [
        "averaging bias",
        "cognitive bias",
        "equal-weighting fallacy",
        "weighting heuristic",
        "anchoring",
        "evidence reliability bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Transcript shows a 'B+' in 'Algebra II Honors' at prior school",
          "Counselor notes prior school's accreditation status and grading rigor are unverified",
          "Scheduling deadline is five school days away"
        ],
        "new_information_after_decision": [
          "Department chair agrees to delay final placement pending a diagnostic test and one classroom observation"
        ],
        "alternatives": [
          "Place the student directly into Algebra II based on the transcript label",
          "Hold placement pending additional diagnostic and observational data"
        ],
        "intended_action": "Teacher chooses to hold placement and request a diagnostic test plus a one-period observation before deciding, a reasonable data-gathering step with no intended bias."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Standardized diagnostic test result: 72nd percentile against grade-level norms (single reliable, normed instrument)",
          "Transcript-derived GPA-equivalent score converted to a 100-point scale (conversion reliability unverified)",
          "Single classroom observation quiz grade: 78% (one data point, unfamiliar content coverage)",
          "Student self-report survey: student rates own algebra confidence as 8/10",
          "Department cutoff for Algebra II placement: composite score of 75 or above"
        ],
        "new_information_after_decision": [
          "Department chair signs off on placement based on the reported composite figure",
          "Student is enrolled in Algebra II effective the following Monday"
        ],
        "alternatives": [
          "Weight the standardized diagnostic test more heavily than the self-report and single observation grade when forming the composite figure",
          "Average all four indicators with equal weight into one composite score",
          "Request one additional data point (e.g., a second observation) before finalizing the composite"
        ],
        "intended_action": "Teacher converts all four indicators to a comparable 100-point scale and takes a straight arithmetic mean, treating the standardized diagnostic, the transcript conversion, the single quiz grade, and the self-report rating as equally informative, then places the student based on this unweighted composite meeting the cutoff."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "First unit test score: 55%, below class median",
          "Homework completion rate: consistently high",
          "Student self-reports continued confidence and effort",
          "Two other transfer students in past years struggled initially before adjusting"
        ],
        "new_information_after_decision": [
          "Teacher arranges twice-weekly tutoring support and continues monitoring performance",
          "Student's participation and homework accuracy begin improving over the next two weeks"
        ],
        "alternatives": [
          "Recommend an immediate move to the standard-track math course",
          "Keep the student in Algebra II with added tutoring support while monitoring trend data"
        ],
        "intended_action": "Teacher opts to add support and monitor rather than move the student immediately, a defensible judgment call under genuine uncertainty about whether the low score reflects transition difficulty or a placement mismatch."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "End-of-quarter grade: C-, with an improving trend over the final three weeks",
          "Tutoring attendance was consistent",
          "Parent has requested in writing that the student remain in the advanced track",
          "Counselor flags that a mid-year track change could affect the student's transcript continuity"
        ],
        "new_information_after_decision": [
          "Student remains in Algebra II for the spring semester with continued support",
          "End-of-year outcome is not yet known at the time of the interview"
        ],
        "alternatives": [
          "Transition the student to the standard-track course for the spring semester",
          "Keep the student in Algebra II with continued tutoring support, citing the recent improving trend"
        ],
        "intended_action": "Teacher keeps the student in Algebra II based on the recent trend and parent input, a judgment consistent with reasonable weighting of recency and stakeholder input rather than any named bias."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role in placing transfer students mid-semester?",
        "What is the general process your department follows when a new student arrives without a complete record?"
      ],
      "timeline_reconstruction": [
        "What information did you have about this student when they first arrived?",
        "In what order did the diagnostic test, transcript, observation, and survey results come in?",
        "What did you do with each piece of information as it arrived?"
      ],
      "decision_point_probes": [
        "What cues in the transcript made you decide to hold off on immediate placement?",
        "Which information sources did you consider most important when computing the placement figure, and why?",
        "What was your goal when combining the diagnostic score, transcript conversion, quiz grade, and survey rating?",
        "What alternatives did you consider for how to combine these four pieces of information?",
        "What was the basis for choosing to combine them the way you did?",
        "Had you handled a similar composite-scoring situation before? How did that experience shape this decision?",
        "How much time pressure were you under when finalizing the composite score?",
        "How confident were you that each of the four inputs deserved equal weight?",
        "When the student struggled on the first unit test, what made you choose support over reassignment?",
        "What made you decide to keep the placement at the end of the quarter rather than transition the student?"
      ],
      "closing_hypotheticals": [
        "If only the diagnostic test result had been available, do you think your placement decision would have been different?",
        "If the self-report survey had shown low confidence instead of high confidence, would that have changed your composite figure?",
        "Looking back, would you handle the combination of evidence differently next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "decision_point": 2,
        "mechanism": "Combines four evidentiary inputs of markedly different reliability and comparability (a normed standardized test, an unverified transcript conversion, a single low-N classroom grade, and a subjective self-report) via simple unweighted arithmetic mean, treating all four as equally informative when forming the composite placement figure.",
        "affected_reasoning_operation": "Evidence integration/aggregation across heterogeneous sources when forming a single composite judgment",
        "evidence_available_at_time": [
          "Diagnostic percentile score (72nd percentile, normed instrument)",
          "Transcript-derived GPA-equivalent score (unverified conversion reliability)",
          "Single classroom observation quiz grade (78%, one data point)",
          "Self-report confidence rating (8/10, subjective and unverified)"
        ],
        "required_textual_manifestation": "Participant explicitly describes converting all four indicators to a comparable 100-point scale and computing a straight average to reach the composite figure, without articulating any rationale for differential weighting, and treats the resulting figure as an adequate basis for a placement decision against the department cutoff.",
        "plausible_nonbias_interpretation": "The department's administrative process nominally requires a single composite number, so producing one figure could be read as institutional compliance rather than a demonstrated failure to weight evidence; the instance is distinguishable only if the participant's own account shows no differentiation in how the four sources were treated despite their differing reliability.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "averaging bias",
          "unequal reliability",
          "weighting",
          "equal-weighting fallacy",
          "composite score bias",
          "evidence quality"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario requested for this generation pass."
    },
    "counterfactual_specification": {
      "causal_variable": "Availability of an explicit department weighting protocol at the composite-scoring decision point",
      "original_state": "No explicit guidance exists on how to weight the diagnostic test, transcript conversion, observation grade, and self-report; the teacher defaults to an unweighted average.",
      "counterfactual_state": "The department chair provides an explicit rubric instructing that the standardized diagnostic test should count for at least 50% of the composite, with the remaining sources weighted lower.",
      "variables_to_hold_constant": [
        "Student identity, transcript content, and diagnostic/observation/self-report values",
        "Scheduling deadline and time pressure",
        "Decision points 1, 3, and 4 and their outcomes",
        "Stakeholders and their roles",
        "Word count and interview structure"
      ],
      "expected_causal_difference": "With explicit weighting guidance present, the teacher would be expected to prioritize the standardized diagnostic over the less reliable sources, reducing or eliminating the unweighted-averaging manifestation at Decision Point 2.",
      "causal_test_question": "Does providing explicit weighting guidance at the composite-scoring step change whether the teacher combines evidence of differing reliability by simple averaging?"
    },
    "generation_checks": [
      "Confirm exactly one Averaging Bias instance is embedded, located at Decision Point 2 only.",
      "Confirm no bias name, definition, or psychological explanation appears anywhere in the public interview text.",
      "Confirm Decision Points 1, 3, and 4 contain no intentional instances of Averaging Bias or any other named bias.",
      "Confirm the interview contains exactly four decision points, each with at least two plausible alternatives.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm final word count falls within 1,215-1,485 words without repetitive exposition.",
      "Confirm consequences described (e.g., quarter grade trend) do not mechanically prove the composite-scoring decision was biased.",
      "Confirm the single Averaging Bias instance provides sufficient textual evidence (available inputs, integration method, absence of weighting rationale) for independent identification."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Averaging Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as unweighted arithmetic averaging of evidentiary inputs with materially different reliability/comparability, not as a stated preference or generic heuristic mention."
      }
    ],
    "target_bias_names": [
      "Averaging Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Averaging Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "mechanism": "Unweighted arithmetic averaging of four evidentiary inputs (standardized diagnostic percentile, unverified transcript conversion, single classroom quiz grade, subjective self-report) despite their differing reliability, producing a composite figure used directly for the placement decision.",
        "affected_reasoning_operation": "Evidence integration/aggregation across heterogeneous sources",
        "evidence_source": "Diagnostic test score, transcript-derived GPA equivalent, single observation quiz grade, self-report confidence survey",
        "distinctiveness_requirement": "The manifestation must show the participant applying equal weight to sources of visibly different reliability, with no stated differentiation rationale, distinguishing it from a merely incorrect but justified composite methodology."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of an explicit department weighting protocol at the composite-scoring decision point",
      "original_state": "No explicit weighting guidance exists; teacher defaults to unweighted averaging of the four inputs.",
      "changed_state": "Department chair provides an explicit rubric prioritizing the standardized diagnostic test (at least 50% weight) over the other three sources.",
      "variables_to_hold_constant": [
        "Student identity, transcript content, and diagnostic/observation/self-report values",
        "Scheduling deadline and time pressure",
        "Decision points 1, 3, and 4 and their outcomes",
        "Stakeholders and their roles",
        "Word count and interview structure"
      ]
    },
    "scenario_id": "EI_Biased_1",
    "domain_id": "EI",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single requested occurrence assigned to the decision point offering the clearest mechanism fit for Averaging Bias (composite scoring from heterogeneous evidence sources) and the greatest narrative realism within a high school placement workflow; remaining three decision points intentionally left free of any named bias per exact-occurrence rules.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Student identity, transcript content, and diagnostic/observation/self-report values",
      "Scheduling deadline and time pressure",
      "Decision points 1, 3, and 4 and their outcomes",
      "Stakeholders and their roles",
      "Word count and interview structure"
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
          "segment_id": "seg_dp1",
          "speaker": "Participant",
          "segment_type": "decision_point_1_initial_placement_hold",
          "raw_interview_anchor": "My first instinct was just to trust the transcript ... so I asked my chair if we could hold off a few days and get a diagnostic test done.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The teacher recognizes uncertainty in the transcript and deliberately gathers more evidence; the generation specification marks this as a reasonable, non-biased data-gathering decision."
        },
        {
          "segment_id": "seg_dp2",
          "speaker": "Participant",
          "segment_type": "decision_point_2_composite_placement_score",
          "raw_interview_anchor": "I converted everything to the same 100-point scale and averaged the four together. That gave me a composite right around 79, which cleared our department's cutoff of 75.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "avg_01"
          ],
          "ground_truth_rationale": "The teacher applies an unweighted arithmetic mean to heterogeneous inputs with materially different reliability and comparability, directly forming the placement decision."
        },
        {
          "segment_id": "seg_dp3",
          "speaker": "Participant",
          "segment_type": "decision_point_3_first_unit_test_monitoring",
          "raw_interview_anchor": "That was concerning, but not alarming yet ... I chose the second option and set up twice-weekly tutoring.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The teacher acknowledges the low score, considers reassignment, and chooses support while monitoring under genuine uncertainty; this is explicitly non-biased in the generation specification."
        },
        {
          "segment_id": "seg_dp4",
          "speaker": "Participant",
          "segment_type": "decision_point_4_quarter_end_retention",
          "raw_interview_anchor": "The recent trend mattered a lot to me ... keeping him in with continued support seemed like the right call.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Retention is supported by the improving trend, tutoring response, transcript continuity, and parent input; the specification treats this as a defensible judgment rather than a named bias."
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
    "analysis_scope_note": "Analysis of the participant's reported reasoning during a transfer-student math placement decision and later monitoring/reassessment decisions. No retrieved scientific-paper corpus passages were available in the input; labels are based on general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Illusion of validity",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Illusion of validity",
      "alternative_labels": [
        "Illusory validity",
        "Validity illusion"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overestimate the validity or predictive quality of a judgment, prediction, or composite score even when the underlying information has limited validity or reliability.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Composite-score placement decision for transfer student",
      "decision_point_description": "The participant converted transcript GPA, diagnostic percentile, classroom quiz score, and self-assessment confidence into a single 100-point average and used it against the department cutoff to make the Algebra II placement decision.",
      "affected_reasoning_operation": "Information integration, weighting of evidence, and threshold-based placement judgment",
      "bias_specific_mechanism": "The participant treated four heterogeneous and differentially valid indicators as equally informative and interchangeable in a single average, and interpreted the resulting number as objective and defensible rather than as a judgment-laden composite. He did not stop to examine whether all four deserved equal weight, even though the transcript conversion was acknowledged as shaky and the self-report was not an independent achievement measure.",
      "manifestation_in_interview": "The participant described averaging four educational measures to create a composite score. When asked whether all four deserved equal footing, he reported not weighing that question; he chose averaging because it felt fair and objective. In retrospect, he said he would think harder about how the pieces relate because they are not measuring the same thing with the same precision.",
      "effect_on_reasoning_or_decision": "The equal-weighted composite produced a score around 79, above the 75 cutoff, leading to Algebra II placement. The participant also acknowledged that a lower self-report score could have pulled the composite under the cutoff, showing that a subjective one-item measure had the same formal influence as the diagnostic test.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I converted everything to the same 100-point scale and averaged the four together. That gave me a composite right around 79, which cleared our department's cutoff of 75 for Algebra II placement, so I placed him there and my chair signed off on the figure.",
          "evidence_explanation": "Shows the actual decision rule: four indicators were converted to a common scale and averaged with equal weight, producing the placement threshold."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I looked at them as four inputs into one number rather than ranking them. The goal was to get a composite score I could defend to my chair, something that wasn't just my gut feeling.",
          "evidence_explanation": "Demonstrates that he treated the inputs as interchangeable contributors to a supposedly objective composite, rather than evaluating their differing validity or weighting them accordingly."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it briefly, but averaging felt like the fairest way to combine them without me injecting extra subjectivity into which one mattered more. If I started picking and choosing weights, that's its own kind of judgment call, and I wanted the number to feel more objective than that.",
          "evidence_explanation": "Shows the belief that unweighted averaging is more objective and fair, and that assigning weights would be subjective. This reflects overconfidence in the composite's validity despite the inputs' unequal measurement quality."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't really stop to weigh that question at the time. I was focused on getting to a number that cleared or didn't clear the cutoff.",
          "evidence_explanation": "Directly confirms he did not assess whether the four numbers deserved equal footing, which is the core information-weighting omission."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I'd slow down and think harder about how the pieces relate to each other before just averaging them, especially when they're not really measuring the same thing with the same precision. At the time, though, it felt like the practical way to turn four different pieces of paper into one decision.",
          "evidence_explanation": "Retrospective recognition that the equal-weight average combined measures of different meaning and precision, supporting the inference that the composite process had an illusory validity at the time."
        }
      ],
      "correction_or_counterevidence": "The participant did not act on his first instinct to rely solely on the transcript; he sought additional data before finalizing the placement. That shows some awareness of uncertainty, but it did not correct the later equal-weighting problem because the additional data were still averaged as if equally valid.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Status quo bias",
      "alternative_labels": [
        "Default bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to keep the student in Algebra II after low early performance and later parent request",
      "supporting_interview_quote": "One test isn't the whole picture, and reassigning mid-quarter has real costs — transcript continuity, disruption, his own confidence. I wanted more evidence before making that call.",
      "plausible_mechanism": "A preference for maintaining the current placement may have operated alongside legitimate practical considerations, making continuation feel safer than switching despite mixed initial evidence.",
      "why_not_identified": "The participant gave explicit, non-bias reasons for waiting, including avoiding overreaction to a single test and avoiding real mid-quarter disruption. The interview does not clearly show an exaggerated or irrational preference for the status quo beyond those considerations."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Recency bias",
      "alternative_labels": [
        "Recency effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "End-of-quarter decision to keep the student in Algebra II rather than move him down",
      "supporting_interview_quote": "The recent trend mattered a lot to me — it suggested the tutoring was working and he was catching up.",
      "plausible_mechanism": "The most recent three-week trend may have been weighted more heavily than the earlier low unit test and overall quarter performance when deciding to maintain placement.",
      "why_not_identified": "Recent trend can be a rational indicator of current learning trajectory, especially after intervention. The interview does not provide sufficient affirmative evidence that recency outweighed other relevant evidence disproportionately."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper corpus passages were provided, so labels and mechanisms rely on general cognitive-science knowledge rather than the requested RAG support.",
    "The analysis is based on a single self-reported interview; there are no independent records of the student's performance or the actual predictive validity of the four measures.",
    "The identification is conservative and does not classify the participant's caution, time pressure, or preference for more evidence as biases without a specific biased mechanism."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Biased_1_Sonar_off",
  "interview_id": "EI_Biased_1",
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
