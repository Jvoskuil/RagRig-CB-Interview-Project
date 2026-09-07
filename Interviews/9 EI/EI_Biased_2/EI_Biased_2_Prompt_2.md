You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EI_Biased_2",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "Curriculum Coordinator / Instructional Coach",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Bridge Literacy Pilot: Mid-Year Scale-Up Decision",
    "scenario_summary_internal": "A district Curriculum Coordinator who personally championed a new structured-literacy pilot ('Bridge Literacy Program') across six elementary classrooms must decide, at the trimester checkpoint, whether to recommend district-wide scale-up to the budget committee. Pilot fluency data are mixed: three classrooms show clear gains, three show flat or ambiguous results tied to disputed testing conditions. The coordinator must review the data, decide what to bring to a leadership meeting, interpret teacher PD feedback, and write a final recommendation memo attributing causes of the observed gains.",
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
          "Literacy specialist later confirms testing conditions were substantively similar across all six classrooms",
          "One 'flat' classroom's teacher reports high student absenteeism during the testing week"
        ],
        "alternatives": [
          "Treat all six classrooms' data with the same level of scrutiny and weigh gains and non-gains equally when judging program impact",
          "Apply closer methodological scrutiny to the three non-gain classrooms (questioning testing conditions, timing, absenteeism) while accepting the three gain classrooms' results largely at face value",
          "Postpone any interpretation until the literacy specialist audits testing conditions in all six classrooms"
        ],
        "intended_action": "Coordinator applies heavier methodological scrutiny to the disconfirming (non-gain) classrooms' data than to the confirming (gain) classrooms, citing testing-condition concerns only for the former."
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
        "intended_action": "Coordinator selects a highlights-only summary slide to fit the time constraint, a defensible time-management choice given the agenda limit."
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
          "Literacy specialist notes that two non-responding invitations went to teachers in the non-gain classrooms"
        ],
        "alternatives": [
          "Report the survey results with an explicit caveat about small sample size and nonresponse",
          "Report the survey results as broadly representative of teacher sentiment without caveats",
          "Follow up individually with non-responding teachers before drawing conclusions"
        ],
        "intended_action": "Coordinator reports the survey with an appropriate caveat about sample size, a reasonable and undistorted interpretive choice."
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
          "A board member later points out that the two classrooms without coordinator visits also showed gains"
        ],
        "alternatives": [
          "Attribute the gains to a combination of factors: new materials, smaller class sizes, teacher effort, and coaching support",
          "Attribute the gains primarily to the frequency and quality of the coordinator's own coaching visits, recommending scale-up centered on replicating her personal coaching model",
          "Withhold a causal attribution and recommend a controlled follow-up study before scaling"
        ],
        "intended_action": "Coordinator's recommendation memo frames the fluency gains as driven mainly by her own coaching involvement, proposing that scale-up success depends on replicating her personal coaching frequency, while giving comparatively little weight to materials, class size, or teacher factors."
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
        "What made you look more closely at the testing conditions in some classrooms but not others?",
        "What information did you have about testing conditions in the gain classrooms at that point?",
        "Why did a highlights-only summary make sense for the board slot?",
        "How representative do you think the survey responses were of all six classrooms?",
        "What other factors could explain the fluency gains besides coaching visits?",
        "How much of the gain would you attribute to your own coaching, versus other factors?"
      ],
      "goals_and_alternatives": [
        "What other ways could you have weighed the classroom data?",
        "What would you have needed to see to treat all six classrooms the same way?",
        "What alternative explanation did you consider for the two non-visited classrooms improving?"
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
        "If the non-gain classrooms had been the ones you personally coached, do you think your read of the testing-condition issue would have changed?",
        "If someone else had gotten the same fluency results without your involvement, how would you have explained the gains?",
        "What would you do differently if you ran this checkpoint review again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation",
        "decision_point": 1,
        "mechanism": "Evaluator applies asymmetric methodological scrutiny to evidence depending on whether it confirms or disconfirms a prior favorable belief about the intervention she championed",
        "affected_reasoning_operation": "Evidence evaluation / evidentiary weighting of classroom-level assessment data",
        "evidence_available_at_time": [
          "Three gain classrooms and three non-gain classrooms report from the same trimester assessment window",
          "A minor testing-schedule discrepancy flagged by the literacy specialist applying to the testing window broadly"
        ],
        "required_textual_manifestation": "Coordinator raises testing-condition and methodology concerns specifically about the non-gain classrooms while accepting the gain classrooms' results without similar scrutiny, in the same review conversation.",
        "plausible_nonbias_interpretation": "A reasonable evaluator might legitimately flag anomalies wherever they first noticed something odd, regardless of outcome direction.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Any reference to selective scrutiny being connected to her prior advocacy for the program",
          "Any labeling of the behavior as biased or unfair"
        ]
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias",
        "decision_point": 4,
        "mechanism": "Evaluator overweights her own personal contribution (coaching visits) as the causal driver of a shared outcome, underweighting other plausible contributing factors including two classrooms that improved without her direct involvement",
        "affected_reasoning_operation": "Causal attribution of an outcome with multiple plausible contributing factors",
        "evidence_available_at_time": [
          "Aggregate fluency gain across six classrooms",
          "New materials, smaller class size, and varying teacher experience present across classrooms",
          "Coordinator's own coaching visits occurred in four of six classrooms, not all six"
        ],
        "required_textual_manifestation": "In the recommendation memo/response, coordinator centers her own coaching frequency as the primary explanation for the gains and frames scale-up around replicating her personal involvement, while only briefly or dismissively noting materials, class size, or teacher factors.",
        "plausible_nonbias_interpretation": "A coach might reasonably highlight coaching as one contributing input among several without intending to overstate her personal causal role.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Any admission that she is overstating her role",
          "Any labeling of the behavior as self-serving or egocentric"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased with no paired control in this request."
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
      "Confirm exactly one Biased Assimilation instance (BA_01) and exactly one Egocentric bias instance (EB_01) are embedded, with no additional occurrences elsewhere in the timeline, probes, or hypotheticals.",
      "Confirm decision points 2 and 3 contain no intentionally embedded bias instances and reflect defensible, non-biased judgment calls.",
      "Confirm BA_01 evidence trace shows asymmetric scrutiny applied only to disconfirming classroom data at decision point 1.",
      "Confirm EB_01 evidence trace shows overweighting of personal coaching contribution relative to co-occurring factors at decision point 4, including the detail that two non-visited classrooms also improved.",
      "Confirm neither instance is labeled or explained using bias terminology in the interview text.",
      "Confirm the interview contains exactly four decision points, each with at least two plausible alternatives.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable without repeating either bias manifestation for padding.",
      "Confirm consequences described (e.g., board member's later question) do not conclusively prove or disprove bias, preserving ambiguity for the validator."
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
