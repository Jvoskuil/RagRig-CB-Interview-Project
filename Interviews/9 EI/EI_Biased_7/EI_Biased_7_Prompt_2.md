You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EI_Biased_7",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "Academic Department Chair (Higher Education)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Capstone Realignment and Adjunct Renewal Decision",
    "scenario_summary_internal": "A department chair must decide, within a compressed renewal-and-accreditation window, whether to renew a longtime adjunct instructor's contract, how to interpret a cluster of section-specific student complaints against a backdrop of a heated faculty-meeting exchange, whether to reallocate a teaching line toward a curriculum-committee-favored elective, and how to finalize and justify the renewal decision to the Dean under a tight staffing deadline. The chair works from partial evaluation data, mixed peer-observation reports, an external accreditation review, and personal recollections of prior interactions with the instructor.",
    "occupational_realism": {
      "objective": "Decide whether to renew the adjunct instructor's teaching contract and how to allocate a contested teaching line, while meeting an HR deadline and an accreditation self-study deadline.",
      "setting": "A mid-sized university's Communications Department during the final three weeks before fall-semester staffing decisions are due, overlapping with an ongoing accreditation self-study and a curriculum committee review cycle.",
      "constraints": [
        "48-hour HR deadline for submitting the adjunct renewal list",
        "Only two of four current-semester course sections have complete student evaluations at decision time",
        "No vetted replacement instructor is available within three weeks of the final decision",
        "Curriculum committee has a two-year-old standing narrative favoring 'capstone modernization'",
        "Chair carries a full teaching and service load alongside administrative duties"
      ],
      "stakeholders": [
        "Adjunct instructor under renewal review",
        "Complaining students in one section",
        "Curriculum committee (senior faculty)",
        "Dean's office / HR",
        "External accreditation reviewer",
        "Teaching assistants and peer observers"
      ],
      "technical_terms_to_use": [
        "student evaluations of teaching (SET)",
        "adjunct renewal cycle",
        "curriculum committee",
        "capstone course",
        "credit-hour allocation",
        "peer observation memo",
        "accreditation self-study",
        "teaching line",
        "learning outcomes",
        "cohort pathway program"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "rationalization",
        "attribution error",
        "confirmation",
        "cognitive shortcut",
        "in-group/out-group",
        "anchoring",
        "present bias",
        "egocentric"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Instructor's SET scores for the prior three years averaged 4.6/5",
          "Current-semester scores available for only 2 of 4 sections, averaging 3.9/5",
          "HR requires the renewal list within 48 hours",
          "Accreditation self-study deadline overlaps the same week"
        ],
        "new_information_after_decision": [
          "The remaining two sections' evaluations arrive a week later showing a further drop to 3.6/5",
          "A batch of student complaint emails surfaces from one of the already-reported sections"
        ],
        "alternatives": [
          "Request an extension from HR to review all four sections before deciding",
          "Approve renewal now based on the multi-year historical trend and partial current data"
        ],
        "intended_action": "Chair approves renewal quickly using the multi-year average and available partial data, treating the missing sections as unlikely to change the picture given time pressure."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Five students from one section sent complaint emails citing disorganized lectures and unfair grading",
          "The same instructor pushed back sharply on a proposed grading-rubric change at a recent faculty meeting",
          "The complaining students are drawn mostly from a newly admitted transfer-pathway cohort",
          "The instructor's other three sections show no complaints this term"
        ],
        "new_information_after_decision": [
          "A peer-observation memo describing the instructor's classroom management as 'adequate but inconsistent' is filed",
          "An external accreditation reviewer's report describes the same instructor's observed session as 'well-structured and responsive'"
        ],
        "alternatives": [
          "Treat the complaints as specific to one section's dynamics and gather additional targeted input",
          "Interpret the complaints as confirming a broader decline in the instructor's overall teaching quality and attitude"
        ],
        "intended_action": "Chair reads the section-specific complaints through the lens of the tense faculty-meeting exchange and separately concludes the pathway cohort is characteristically more vocal, without seeking section-specific clarification."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Curriculum committee has spent two years building a case for 'modernizing' the capstone course",
          "A senior faculty member has proposed reallocating the adjunct's teaching line to a new elective",
          "Enrollment data for the existing capstone actually grew 8% year over year",
          "The mixed peer-observation memo and the positive accreditation report are both now on file"
        ],
        "new_information_after_decision": [
          "A budget analyst later notes the enrollment growth was not factored into the committee's recommendation memo",
          "The accreditation reviewer's report is filed without further departmental follow-up"
        ],
        "alternatives": [
          "Commission a fresh, data-driven review of capstone enrollment and outcomes before deciding on reallocation",
          "Approve the reallocation because it aligns with the committee's established modernization narrative, treating the enrollment growth and positive accreditation note as exceptions"
        ],
        "intended_action": "Chair endorses the reallocation, weaving the complaint pattern, the meeting exchange, and the committee's prior narrative into a single consistent story of decline, while reading the mixed peer memo as confirming that story and setting aside the more positive accreditation report as less informed."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The HR paperwork deadline is three weeks out with no vetted replacement instructor identified",
          "Historical record shows three years of strong performance prior to this term",
          "The chair has had two personal one-on-one meetings with the instructor this term, both described by the chair as 'defensive in tone'",
          "TA feedback and peer-observation notes exist but were not central to the chair's prior deliberations"
        ],
        "new_information_after_decision": [
          "The Dean asks for a one-paragraph justification memo before finalizing the non-renewal",
          "A colleague later notes the memo relies heavily on the chair's own meeting impressions rather than the fuller evidence file"
        ],
        "alternatives": [
          "Extend the contract short-term while completing a fuller multi-source review over the semester",
          "Issue immediate non-renewal to resolve the situation before the deadline, despite lacking a replacement"
        ],
        "intended_action": "Chair opts for immediate non-renewal to close out the pressing scheduling question, and drafts the justification memo primarily around personal recollections of the two tense meetings rather than the broader evidence file."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were responsible for deciding that term.",
        "What made this renewal cycle different from previous ones?"
      ],
      "timeline_reconstruction": [
        "What did you know at the point you first had to act, and what arrived later?",
        "Which pieces of information came in before versus after each decision?"
      ],
      "decision_point_probes": [
        "What cues made you lean one way at that point?",
        "What information sources did you rely on, and which did you set aside?",
        "What was your goal at that specific moment?",
        "What alternatives did you consider, and why did you rule them out?",
        "What was the deciding factor in the end?",
        "Had you handled a similar situation before? How did that shape this one?",
        "How much time pressure were you under right then?",
        "How confident were you in the data you had at that point?"
      ],
      "closing_hypotheticals": [
        "If the missing evaluation data had arrived before your first decision, would anything have changed?",
        "If the complaint emails had come from a different group of students, would you have read them differently?",
        "If the accreditation report had arrived before the committee meeting, would the outcome have changed?",
        "If you had a replacement instructor already lined up, would your final decision have been different?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Bounded Rationality",
        "decision_point": 1,
        "mechanism": "Chair satisfices under time pressure, relying on the multi-year average and readily available partial data instead of pursuing complete current-term evidence.",
        "affected_reasoning_operation": "Evidence-sufficiency judgment before a renewal decision",
        "evidence_available_at_time": [
          "Three-year historical SET average of 4.6",
          "Partial current-term SET average of 3.9 from 2 of 4 sections",
          "48-hour HR deadline"
        ],
        "required_textual_manifestation": "Chair explicitly justifies acting on partial/historical data because of time and workload constraints rather than seeking the missing sections.",
        "plausible_nonbias_interpretation": "A reasonable manager may legitimately act on the best available data under a hard deadline; this must be distinguished by the chair not even attempting a quick check (e.g., a phone call) that was feasible within the window.",
        "strength": "subtle",
        "do_not_make_explicit": ["bounded rationality", "satisficing", "cognitive load"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Horn Effect",
        "decision_point": 2,
        "mechanism": "A single negative interaction (the heated rubric-meeting exchange) spreads to color the chair's interpretation of unrelated complaint emails about the instructor's classroom conduct.",
        "affected_reasoning_operation": "Cross-domain trait inference from one negative data point to unrelated performance dimensions",
        "evidence_available_at_time": [
          "The instructor's pushback at the faculty meeting on the rubric proposal",
          "Complaint emails describing lecture organization and grading fairness",
          "No prior link established between the meeting exchange and the complaints"
        ],
        "required_textual_manifestation": "Chair connects the meeting tone to a broader judgment about the instructor's classroom competence without independent evidence linking the two.",
        "plausible_nonbias_interpretation": "The instructor's general disposition that term could independently affect both the meeting and the classroom; this must be distinguished by the chair drawing the link without seeking classroom-specific verification.",
        "strength": "subtle",
        "do_not_make_explicit": ["horn effect", "halo", "trait generalization"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Group attribution error",
        "decision_point": 2,
        "mechanism": "Chair attributes the complaint pattern to a perceived characteristic of the students' admission cohort rather than to section- or instructor-specific factors.",
        "affected_reasoning_operation": "Causal attribution of an observed behavior pattern to group membership",
        "evidence_available_at_time": [
          "Roster composition showing most complainants are from a transfer-pathway cohort",
          "No comparative data on complaint rates from that cohort in other courses"
        ],
        "required_textual_manifestation": "Chair reasons that this cohort 'tends to be more vocal' as a general trait, using cohort membership as the explanation rather than checking the specific course context.",
        "plausible_nonbias_interpretation": "Cohort-level patterns can sometimes reflect genuine programmatic differences; this must be distinguished by the chair not checking whether the same cohort behaves similarly in other courses before attributing the complaints to group character.",
        "strength": "moderate",
        "do_not_make_explicit": ["group attribution error", "stereotype", "cohort generalization"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 3,
        "mechanism": "Chair integrates the complaint pattern, the meeting exchange, and the committee's pre-existing modernization narrative into one internally consistent story of decline, while the contrary enrollment-growth figure is not addressed within that story.",
        "affected_reasoning_operation": "Narrative construction and selective integration of favorable-fitting facts into a decision rationale",
        "evidence_available_at_time": [
          "Two-year-old committee narrative favoring capstone modernization",
          "8% year-over-year enrollment growth in the existing capstone",
          "Prior complaint and meeting evidence already in hand"
        ],
        "required_textual_manifestation": "Chair presents a single fluent justification for reallocation that folds in the complaints and meeting tension but never addresses the enrollment growth figure within that justification.",
        "plausible_nonbias_interpretation": "A coherent case for change can be legitimate; this must be distinguished by the enrollment data being available and relevant but conspicuously absent from an otherwise thorough-sounding rationale.",
        "strength": "moderate",
        "do_not_make_explicit": ["coherence-based reasoning", "rationalization", "narrative fit"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Biased Assimilation",
        "decision_point": 3,
        "mechanism": "Chair interprets the ambiguous peer-observation memo as confirming decline while discounting the more positive external accreditation report as less credible, despite both being similarly authoritative evidence types.",
        "affected_reasoning_operation": "Evaluation of ambiguous or mixed-quality evidence against a prior-held belief",
        "evidence_available_at_time": [
          "Peer-observation memo describing classroom management as 'adequate but inconsistent'",
          "External accreditation report describing the observed session as 'well-structured and responsive'"
        ],
        "required_textual_manifestation": "Chair treats the mixed memo's ambiguity as supporting the decline narrative while explaining away the positive report (e.g., 'the reviewer only saw one session').",
        "plausible_nonbias_interpretation": "Different observers can reasonably see different things in a single session; this must be distinguished by the chair applying a stricter credibility standard specifically to the report that conflicts with the emerging narrative.",
        "strength": "subtle",
        "do_not_make_explicit": ["biased assimilation", "motivated evidence evaluation", "prior belief"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Present Bias",
        "decision_point": 4,
        "mechanism": "Chair prioritizes immediate resolution of the staffing ambiguity (issuing non-renewal now) over the larger, more distant cost of scrambling to cover the course without a vetted replacement.",
        "affected_reasoning_operation": "Intertemporal trade-off between short-term relief and longer-term departmental cost",
        "evidence_available_at_time": [
          "Three-week HR deadline",
          "No replacement instructor identified",
          "Option to extend the contract short-term while completing a fuller review"
        ],
        "required_textual_manifestation": "Chair explicitly favors closing the question now to relieve the immediate pressure, acknowledging but downweighting the coverage risk this creates for the fall term.",
        "plausible_nonbias_interpretation": "Deadlines sometimes genuinely force immediate closure; this must be distinguished by the chair having a viable short-term-extension alternative available and choosing immediate closure primarily for relief from present discomfort rather than for a substantive reason tied to that alternative's costs.",
        "strength": "subtle",
        "do_not_make_explicit": ["present bias", "temporal discounting", "immediate gratification"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Egocentric bias",
        "decision_point": 4,
        "mechanism": "When drafting the justification memo, chair recalls and foregrounds personal one-on-one interactions with the instructor as the central evidence, discounting TA feedback and peer-observation notes that were also available.",
        "affected_reasoning_operation": "Memory retrieval and evidence weighting during justification construction",
        "evidence_available_at_time": [
          "Chair's own recollection of two meetings described as 'defensive in tone'",
          "TA feedback and peer-observation notes on file but not previously central to deliberation"
        ],
        "required_textual_manifestation": "Chair's memo draft leans on 'in my meetings with him' as the primary basis, with other stakeholder input mentioned only in passing or omitted.",
        "plausible_nonbias_interpretation": "Direct personal observation can be legitimately weighty evidence; this must be distinguished by the chair not reconciling this account with the more complete evidence file already available before finalizing the memo's emphasis.",
        "strength": "subtle",
        "do_not_make_explicit": ["egocentric bias", "self-referential recall", "personal salience"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition scenario with no paired control specified in this request."
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
      "Confirm exactly 4 decision points, each with at least two plausible alternatives.",
      "Confirm exactly 7 total planned bias instances, one per manifest entry.",
      "Confirm no decision point contains more than two instances of the same bias.",
      "Confirm decision point 2 and 3 each host two distinct biases with separated evidence sources.",
      "Confirm no bias name, definition, or psychological label appears in probes or narrative text.",
      "Confirm word count target of 1,350 (range 1,215–1,485) is achievable given four decision points and probe density without repetitive exposition.",
      "Confirm each instance has a plausible non-bias explanation distinguishable from the biased manifestation.",
      "Confirm consequences described (e.g., replacement staffing outcome, accreditation follow-up) do not mechanically confirm or refute whether decisions were biased."
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
