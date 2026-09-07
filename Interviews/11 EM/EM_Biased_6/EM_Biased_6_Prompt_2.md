You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Biased_6",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Emergency Preparedness Curriculum Designer / Exercise Planner",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Riverbend Rising: Designing the Levee-Failure Full-Scale Exercise",
    "scenario_summary_internal": "A county Emergency Preparedness Curriculum Designer is assigned to build a HSEEP-compliant full-scale exercise (FSE) and companion training curriculum simulating a levee failure and flash-flood evacuation, to be delivered in 10 weeks ahead of the seasonal flood-risk window. The designer must scope the build timeline, decide how severe the simulated hazard should be, choose which training injects to prioritize under production time limits, and decide how much explanatory detail to put in the Controller-Evaluator handbook for partner agencies with less specialized background. The narrative follows the design process from initial scoping through post-exercise debrief, without ever stating whether the final exercise 'worked,' so that consequences do not mechanically prove bias.",
    "occupational_realism": {
      "objective": "Design and deliver a full-scale flood/levee-failure exercise and an accompanying evaluator training curriculum within a fixed 10-week window, satisfying HSEEP documentation standards and validating EOC decision-making capability.",
      "setting": "County Office of Emergency Management, coordinating with the Army Corps of Engineers, a regional Emergency Operations Center, a school district, and municipal police/fire partners.",
      "constraints": [
        "10-week fixed deadline tied to seasonal flood-risk window",
        "Solo designer with reduced staff support compared to prior exercise cycles",
        "New Army Corps dam-break hydrology data must be incorporated",
        "Partner agencies vary widely in technical flood-response background",
        "Limited production budget for training materials",
        "HSEEP documentation and after-action reporting requirements"
      ],
      "stakeholders": [
        "Curriculum Designer / Exercise Planner (interviewee)",
        "County Emergency Management Director",
        "Army Corps of Engineers hydrology liaison",
        "Regional EOC watch commanders",
        "Partner-agency Controller-Evaluators (police, school district, fire)",
        "Local advisory committee / elected stakeholders"
      ],
      "technical_terms_to_use": [
        "HSEEP",
        "full-scale exercise (FSE)",
        "Controller-Evaluator handbook",
        "Exercise Evaluation Guide (EEG)",
        "inject",
        "after-action report (AAR)",
        "levee overtopping",
        "stream gauge",
        "evacuation zone"
      ],
      "technical_terms_to_avoid": [
        "explicit bias names (e.g., 'planning fallacy', 'normality bias')",
        "psychological or cognitive-science terminology",
        "meta-commentary about bias or heuristics"
      ],
      "timeline": [
        {
          "phase": 1,
          "decision_point": true,
          "facts_available_before_decision": [
            "Prior comparable exercise (2019) took 6 weeks with two staff and reused an existing scenario shell",
            "Current project scope adds a new levee-failure module and coordination across three agencies",
            "Designer is now working largely solo",
            "Deadline is fixed at 10 weeks"
          ],
          "new_information_after_decision": [
            "Building the custom levee-failure module and coordinating three agencies' inputs takes substantially longer than the legacy template did",
            "Mid-project status check shows the schedule has already slipped by two weeks"
          ],
          "alternatives": [
            "Build a new scenario module from the updated dam-break data with an explicit contingency buffer",
            "Reuse the familiar legacy exercise template and compress the new hydrology content into the existing schedule"
          ],
          "intended_action": "Adopt the compressed timeline based on the prior exercise's duration, treating the added scope and reduced staffing as absorbable within the same schedule."
        },
        {
          "phase": 2,
          "decision_point": true,
          "facts_available_before_decision": [
            "Updated Army Corps modeling shows increased catastrophic dam-failure risk",
            "Local advisory committee notes the area has not seen flooding at that severity in over 40 years",
            "A peer planner's exercise from another county was recently criticized in an AAR review for an unrealistic, watered-down scenario",
            "Designer participates in reviewing that peer's after-action findings"
          ],
          "new_information_after_decision": [
            "During execution, evaluators report the scenario's peak severity feels routine and does not sufficiently stress EOC escalation procedures",
            "Advisory committee later acknowledges the hydrology data was more alarming than the exercise conveyed"
          ],
          "alternatives": [
            "Retain the catastrophic dam-failure inject supported by updated Army Corps modeling",
            "Scale the exercise down to a historically typical flood severity that matches community expectations"
          ],
          "intended_action": "Scale the severity toward the historically familiar flood level, while separately concluding in the peer-review discussion that the reviewed exercise's flaws reflect a planning weakness unlikely to affect the designer's own work."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "Production time only allows full development of one inject category before the deadline",
            "Available options include annotated photo/video clips of levee overtopping and plain data packages (stream gauge readouts, GIS flow-rate shapefiles)",
            "Photo/video injects are more time-consuming to produce but are recalled easily in past post-exercise surveys",
            "Data packages are less visually engaging but carry the specific quantitative detail EOC staff need for modeling decisions"
          ],
          "new_information_after_decision": [
            "Post-exercise survey shows participants vividly remember the photo/video injects",
            "Several EOC participants could not translate the visual injects into correct evacuation-zone or resource decisions because the specific flow-rate data was underdeveloped"
          ],
          "alternatives": [
            "Prioritize photo/video injects for memorability and emotional engagement",
            "Prioritize data-rich technical injects that support precise operational decisions"
          ],
          "intended_action": "Prioritize the photo/video injects, allocating most remaining production time to visual material on the reasoning that it will be a more effective training tool."
        },
        {
          "phase": 4,
          "decision_point": true,
          "facts_available_before_decision": [
            "Designer has 15 years of hydrology/EM background and has used the same shorthand terms and scoring conventions across many prior exercises",
            "Partner-agency evaluators (school district, police) have limited specialized flood-response training",
            "Time remaining before the deadline is short",
            "A glossary/explanatory appendix would add production time but has been requested informally in past AAR feedback"
          ],
          "new_information_after_decision": [
            "During the exercise, several partner-agency evaluators misapply the scoring rubric because shorthand terms and acronyms were not explained",
            "Resulting AAR data from those evaluators is inconsistent with EOC-side evaluator data"
          ],
          "alternatives": [
            "Add a glossary and expanded explanation of specialized terms and scoring conventions for less-experienced evaluators",
            "Keep the Controller-Evaluator handbook concise using standard practitioner shorthand to save production time"
          ],
          "intended_action": "Keep the handbook concise in standard practitioner shorthand, treating the terminology and scoring logic as self-evident to all evaluators."
        }
      ]
    },
    "probe_plan": {
      "opening": [
        "Describe the assignment and what a successful outcome would have looked like.",
        "What was your overall objective when you started designing this exercise?"
      ],
      "timeline_reconstruction": [
        "Walk me through how the project unfolded from initial scoping to the exercise day.",
        "What did you know at each stage, and what changed as you learned more?"
      ],
      "decision_point_probes": [
        "What information did you have available at the moment you made this decision?",
        "What alternatives did you consider, and why did you choose the one you did?",
        "What in your prior experience shaped how you approached this?",
        "How much time pressure did you feel at this point, and how did that affect your choice?",
        "How confident were you in that decision at the time, and how confident are you now?",
        "What sources of information did you rely on most, and were any downweighted or set aside?"
      ],
      "closing_hypotheticals": [
        "If you had had two more weeks, what would you have done differently?",
        "If a completely new planner had taken over halfway through, what might they have done differently at each stage?",
        "Looking back, is there a point where you'd make a different call knowing what you know now?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "decision_point": 1,
        "mechanism": "Designer anchors the new project's timeline estimate on a past, smaller-scope project's completion time, without adjusting for added complexity (three-agency coordination, new hydrology module) or reduced staffing.",
        "affected_reasoning_operation": "Duration/effort estimation for project scoping",
        "evidence_available_at_time": [
          "2019 exercise took 6 weeks with two staff and a reused scenario shell",
          "Current project has expanded scope (new module, three-agency coordination) and reduced staffing (solo)",
          "Deadline is fixed at 10 weeks"
        ],
        "required_textual_manifestation": "Designer states the belief that the build can be completed in roughly the same time as the prior, smaller project, without acknowledging the added scope or reduced staffing as reasons for a longer estimate.",
        "plausible_nonbias_interpretation": "The designer may have reasonably assumed some efficiencies from having done a similar project before, and simply prioritized starting quickly over front-loaded planning.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "underestimation bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Mere Exposure",
        "decision_point": 1,
        "mechanism": "Designer favors the previously used scenario template/format over a newly recommended modular design, citing comfort/familiarity with the old structure rather than an evidence-based comparison of the two options' training value.",
        "affected_reasoning_operation": "Selection among design-format alternatives",
        "evidence_available_at_time": [
          "Legacy template has been used in the past three exercise cycles",
          "A newer modular design format was suggested by stakeholders as potentially more effective",
          "No formal comparative data on training outcomes between the two formats was reviewed"
        ],
        "required_textual_manifestation": "Designer expresses a preference for the familiar template phrased in terms of comfort or ease of use, without citing evidence that it produces better training outcomes than the alternative format.",
        "plausible_nonbias_interpretation": "The designer could be making a legitimate efficiency trade-off, since a known format reduces production risk under a tight deadline.",
        "strength": "subtle",
        "do_not_make_explicit": ["mere exposure effect", "familiarity bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Normality Bias",
        "decision_point": 2,
        "mechanism": "Designer scales back the simulated hazard severity toward the community's recent historical experience (no severe flood in 40 years) despite updated hydrology data showing increased catastrophic risk, treating the absence of recent occurrence as evidence the worst case is unlikely to matter for training purposes.",
        "affected_reasoning_operation": "Risk-severity calibration for scenario design based on updated hazard data vs. recent historical experience",
        "evidence_available_at_time": [
          "Updated Army Corps modeling indicates increased catastrophic dam-failure risk",
          "Advisory committee notes no comparable flood severity has occurred locally in over 40 years",
          "HSEEP guidance calls for exercises to test capability gaps, not just familiar scenarios"
        ],
        "required_textual_manifestation": "Designer justifies reducing the hazard severity mainly by referencing the community's lack of recent experience with such an event, rather than by a documented capability or resource limitation.",
        "plausible_nonbias_interpretation": "The designer might have legitimately scaled down severity to keep the exercise achievable for evaluators with limited training maturity.",
        "strength": "subtle",
        "do_not_make_explicit": ["normalcy bias", "normality bias", "it can't happen here"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Bias Blind Spot",
        "decision_point": 2,
        "mechanism": "While reviewing a peer planner's criticized exercise design in an after-action discussion, the designer attributes the peer's shortcomings to a planning weakness specific to that peer, while expressing confidence that their own concurrent design choices are objective and free of similar influence, without applying the same scrutiny to their own process.",
        "affected_reasoning_operation": "Self-versus-other evaluation of susceptibility to design distortion during peer AAR review",
        "evidence_available_at_time": [
          "Peer's exercise was criticized in an AAR for being unrealistically mild",
          "Designer is simultaneously making a related severity-scaling decision on their own exercise",
          "No independent review of the designer's own scenario severity has occurred at this point"
        ],
        "required_textual_manifestation": "Designer comments on the peer's design flaw as a planning shortcoming unlikely to occur in their own work, without applying comparable self-scrutiny to their concurrent severity decision.",
        "plausible_nonbias_interpretation": "The designer may simply have more direct knowledge of their own safeguards and processes than of the peer's, making the differential judgment reasonable rather than a systematic blind spot.",
        "strength": "subtle",
        "do_not_make_explicit": ["bias blind spot", "naive realism", "third-person effect"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Picture Superiority",
        "decision_point": 3,
        "mechanism": "Designer allocates the majority of limited remaining production time to photo/video injects on the basis that visual material is more memorable, over data-rich technical injects that carry the specific quantitative information needed for correct operational decisions.",
        "affected_reasoning_operation": "Resource allocation among competing training-material formats under time constraint",
        "evidence_available_at_time": [
          "Photo/video injects of levee overtopping are more time-consuming to produce but recalled vividly in past surveys",
          "Data packages (stream gauge readouts, GIS shapefiles) carry specific operational detail but are less visually engaging",
          "Only one inject category can be fully developed given remaining time"
        ],
        "required_textual_manifestation": "Designer justifies prioritizing the visual injects primarily by their memorability or engagement value, rather than by their relevance to the specific operational decisions evaluators need to practice.",
        "plausible_nonbias_interpretation": "The designer may have reasonably judged that visual injects better sustain participant engagement across a long exercise day, which is itself a legitimate training design goal.",
        "strength": "subtle",
        "do_not_make_explicit": ["picture superiority effect", "visual memorability bias"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Curse of Knowledge",
        "decision_point": 4,
        "mechanism": "Designer, drawing on 15 years of specialized hydrology/EM background, drafts the Controller-Evaluator handbook using standard practitioner shorthand and acronyms without added explanation, assuming this level of detail is self-evident to all evaluators including those from partner agencies with far less specialized background.",
        "affected_reasoning_operation": "Calibration of explanatory detail for an audience with different background knowledge",
        "evidence_available_at_time": [
          "Designer has extensive specialized background and has used the same shorthand across many prior exercises",
          "Partner-agency evaluators (school district, police) have limited specialized flood-response training",
          "Past AAR feedback had informally requested clearer explanations for non-specialist evaluators"
        ],
        "required_textual_manifestation": "Designer describes deciding to keep the handbook concise in specialist shorthand, reasoning that the terms and scoring logic are obvious or standard, without adjusting for the partner evaluators' different background.",
        "plausible_nonbias_interpretation": "The designer may have made a legitimate time-management trade-off, judging that a glossary was a lower priority than finishing other deliverables before the deadline.",
        "strength": "subtle",
        "do_not_make_explicit": ["curse of knowledge", "expert blind spot"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' with no paired control in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable in this condition; field retained for schema completeness only.",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points appear in the timeline, each with at least two plausible alternatives.",
      "Confirm all 6 planned instances (cb_01 through cb_06) are represented once each, with no additional unintended instances of the same 6 biases elsewhere in the narrative, probes, or hypotheticals.",
      "Confirm no bias names, definitions, or psychological terminology appear in the public-facing interview text.",
      "Confirm consequences described after each decision point are ambiguous as to whether the decision was biased (i.e., plausible non-bias explanations remain available).",
      "Confirm total word count target is 1,350 words, within the 1,215–1,485 acceptable range, achieved without repetitive exposition.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm decision points 1 and 2 each carry two distinct-bias instances with clearly separated evidence traces and reasoning operations, per the instance independence rule.",
      "Confirm decision points 3 and 4 each carry exactly one bias instance."
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
