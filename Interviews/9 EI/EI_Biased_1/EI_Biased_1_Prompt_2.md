You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EI_Biased_1",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
