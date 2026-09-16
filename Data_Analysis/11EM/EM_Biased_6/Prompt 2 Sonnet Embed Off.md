You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine debrief for our exercise-design case-study library — I'll be asking about a specific project you led, how the decisions actually unfolded, not whether they were "right" in hindsight. Everything stays de-identified. Sound okay?

Participant: Sure, happy to walk through it. This is the Riverbend Rising full-scale exercise, right? That one's still pretty fresh for me.

Interviewer: Exactly. Can you start by describing the assignment and what success would've looked like?

Participant: I was handed the FSE build in early spring — simulate a levee failure and flash-flood evacuation, get it HSEEP-compliant, and use it to validate EOC escalation procedures before the seasonal flood window opened. Success meant a full exercise day, a usable Controller-Evaluator handbook, and an AAR that actually told the Director something new about our capability gaps.

Interviewer: Give me the incident account — how did the project actually go, start to finish?

Participant: We'd run something similar back in 2019 — smaller footprint, two of us on it, and we mostly reused an existing scenario shell. That one took about six weeks start to finish. This time I was solo, and the scope was bigger: a brand-new levee-failure module built off updated Army Corps dam-break modeling, plus coordination across the regional EOC, the school district, and municipal police and fire. Deadline was fixed at ten weeks because of the flood-risk calendar. I scoped the build assuming it'd track pretty close to the 2019 timeline — figured I knew the process well enough to move fast. About four weeks in, I was still building the custom hydrology module and waiting on sign-off from three different agencies, and a status check showed we'd already slipped two weeks. From there it became a scramble — severity calibration with the advisory committee, a fight over which training injects we could actually finish, and a last push on the handbook right up against the deadline.

Interviewer: Let's reconstruct that chronologically. What did you know at each stage, and what changed as you learned more?

Participant: At kickoff I had the 2019 numbers in my head and the new Corps data in hand, but I hadn't yet mapped out how much longer three-agency coordination would take versus one shell reused solo. Once the schedule slipped, I knew severity calibration and the advisory committee conversation were coming up next, and I could already tell we wouldn't have time to fully build every kind of training material — so the inject decision became a resource fight. By the time I got to the handbook, the clock was the dominant fact.

Interviewer: Let's slow down on the first real decision — scoping the build timeline. Walk me through it.

Participant: Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much. I remember telling the Director I could deliver in the same general window even though I was down to one person and building the hydrology piece essentially from scratch.

Interviewer: What made you confident the compressed schedule would hold?

Participant: Honestly, mostly that I'd done a version of this before and it worked out then. I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead.

Interviewer: What information would have changed that estimate?

Participant: If I'd actually broken out hours for three-agency sign-off separately instead of folding it into "coordination," I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up.

Interviewer: Still in that same phase — you also had a choice about which scenario format to build from. What drove that?

Participant: Yeah, there was a newer modular design format some of the stakeholders floated, supposedly better suited to multi-agency exercises. But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in.

Interviewer: Did you compare how the two formats actually performed for training outcomes?

Participant: Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure.

Interviewer: Let's move to the severity decision. What was on the table?

Participant: The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years. There was real pressure to keep the scenario grounded in something the community would find plausible.

Interviewer: How did you weigh the modeling against that history?

Participant: I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face.

Interviewer: Around that same time, you were part of an AAR review for a peer's exercise. What happened there?

Participant: Right, a planner in another county got flagged for an unrealistically mild scenario — didn't stress escalation procedures at all. In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time.

Interviewer: Did you apply the same scrutiny to your own severity choice that you applied to theirs?

Participant: Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard.

Interviewer: Third decision point — the training injects. What were the options?

Participant: We only had production time to fully build one category. Option one was photo and video clips of levee overtopping — dramatic, but slow to produce. Option two was the data packages — stream gauge readouts, GIS flow-rate shapefiles — less visually interesting but more specific for EOC modeling decisions.

Interviewer: Which did you prioritize, and why?

Participant: I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool.

Interviewer: Did you weigh how well each format supported the actual operational decisions evaluators would need to make?

Participant: Less than I probably should have, in retrospect. The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them.

Interviewer: Last decision point — the Controller-Evaluator handbook. What went into that?

Participant: I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary.

Interviewer: Was there any indication a glossary might be needed?

Participant: There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left.

Interviewer: Looking back across all four decisions — if you'd had two more weeks, what would you have done differently?

Participant: Probably built in a real contingency buffer up front instead of assuming the old timeline would hold, and maybe split production time more evenly between the visual and data injects.

Interviewer: And if a different planner had taken over halfway through?

Participant: They might have pushed harder on the severity call, given the modeling was pretty clear. And they might not have carried the same assumptions I had about what "obvious" means in the handbook, since they wouldn't have fifteen years of the same habits behind them.

Interviewer: Anything you'd flag as uncertain even now?

Participant: Whether the milder scenario actually undercut the escalation testing, or whether it was just a rough exercise day for other reasons — I genuinely don't know. Same with the handbook; the scoring inconsistencies could've come from a dozen things, not just the shorthand.

Interviewer: That's a good place to stop. Thanks for the detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Biased_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Planning Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Anchoring project timeline on a smaller prior project without adjusting for added scope/reduced staffing"
      },
      {
        "bias": "Normality Bias",
        "occurrences": 1,
        "mechanism_constraint": "Scaling down hazard severity based on lack of recent local occurrence despite updated risk data"
      },
      {
        "bias": "Bias Blind Spot",
        "occurrences": 1,
        "mechanism_constraint": "Judging a peer's design flaw as unlikely in own concurrent work without equivalent self-scrutiny"
      },
      {
        "bias": "Picture Superiority",
        "occurrences": 1,
        "mechanism_constraint": "Prioritizing visual injects over data-rich injects primarily for memorability rather than operational relevance"
      },
      {
        "bias": "Mere Exposure",
        "occurrences": 1,
        "mechanism_constraint": "Preferring a familiar prior template over a newly proposed format absent comparative evidence"
      },
      {
        "bias": "Curse of Knowledge",
        "occurrences": 1,
        "mechanism_constraint": "Assuming specialist shorthand is self-evident to less-experienced partner-agency evaluators"
      }
    ],
    "target_bias_names": [
      "Planning Fallacy",
      "Normality Bias",
      "Bias Blind Spot",
      "Picture Superiority",
      "Mere Exposure",
      "Curse of Knowledge"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Planning Fallacy", "requested_occurrences": 1},
      {"bias": "Normality Bias", "requested_occurrences": 1},
      {"bias": "Bias Blind Spot", "requested_occurrences": 1},
      {"bias": "Picture Superiority", "requested_occurrences": 1},
      {"bias": "Mere Exposure", "requested_occurrences": 1},
      {"bias": "Curse of Knowledge", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Planning Fallacy"},
      {"instance_id": "cb_02", "bias": "Mere Exposure"},
      {"instance_id": "cb_03", "bias": "Normality Bias"},
      {"instance_id": "cb_04", "bias": "Bias Blind Spot"},
      {"instance_id": "cb_05", "bias": "Picture Superiority"},
      {"instance_id": "cb_06", "bias": "Curse of Knowledge"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Planning Fallacy", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Mere Exposure", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Normality Bias", "decision_point": 2},
      {"instance_id": "cb_04", "bias": "Bias Blind Spot", "decision_point": 2},
      {"instance_id": "cb_05", "bias": "Picture Superiority", "decision_point": 3},
      {"instance_id": "cb_06", "bias": "Curse of Knowledge", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "mechanism": "Anchoring timeline estimate on smaller prior project duration without adjusting for added scope/reduced staffing",
        "affected_reasoning_operation": "Duration/effort estimation",
        "evidence_source": "Prior exercise duration record vs. current expanded scope facts",
        "distinctiveness_requirement": "Distinct from cb_02 (format preference) and cb_03 (severity calibration); concerns time estimation specifically"
      },
      {
        "instance_id": "cb_02",
        "bias": "Mere Exposure",
        "mechanism": "Preferring familiar legacy template over newly proposed format absent comparative evidence",
        "affected_reasoning_operation": "Selection among design-format alternatives",
        "evidence_source": "Repeated use of legacy template across three prior cycles vs. new modular proposal",
        "distinctiveness_requirement": "Distinct from cb_01; concerns format choice, not timeline estimation, though co-located at decision point 1"
      },
      {
        "instance_id": "cb_03",
        "bias": "Normality Bias",
        "mechanism": "Scaling hazard severity down based on absence of recent local occurrence despite updated risk modeling",
        "affected_reasoning_operation": "Risk-severity calibration",
        "evidence_source": "Army Corps updated modeling vs. advisory committee's historical-absence framing",
        "distinctiveness_requirement": "Distinct from cb_04; concerns hazard-severity judgment, not self/other evaluation, though co-located at decision point 2"
      },
      {
        "instance_id": "cb_04",
        "bias": "Bias Blind Spot",
        "mechanism": "Attributing peer's design flaw to peer-specific weakness while exempting own concurrent process from equivalent scrutiny",
        "affected_reasoning_operation": "Self-versus-other evaluation of susceptibility to distortion",
        "evidence_source": "Peer AAR criticism discussion vs. designer's own concurrent unreviewed decision",
        "distinctiveness_requirement": "Distinct from cb_03; concerns comparative self-assessment, not the severity decision itself"
      },
      {
        "instance_id": "cb_05",
        "bias": "Picture Superiority",
        "mechanism": "Prioritizing visual injects for memorability over data-rich injects needed for specific operational decisions",
        "affected_reasoning_operation": "Resource allocation among training-material formats",
        "evidence_source": "Past survey recall data on visual injects vs. operational relevance of data packages",
        "distinctiveness_requirement": "Sole instance at decision point 3; no co-located instance to distinguish from"
      },
      {
        "instance_id": "cb_06",
        "bias": "Curse of Knowledge",
        "mechanism": "Assuming specialist shorthand is self-evident to less-experienced partner-agency evaluators",
        "affected_reasoning_operation": "Calibration of explanatory detail for a mixed-background audience",
        "evidence_source": "Designer's own specialist background vs. partner evaluators' documented lower familiarity",
        "distinctiveness_requirement": "Sole instance at decision point 4; no co-located instance to distinguish from"
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Planning Fallacy", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Mere Exposure", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Normality Bias", "strength": "subtle"},
      {"instance_id": "cb_04", "bias": "Bias Blind Spot", "strength": "subtle"},
      {"instance_id": "cb_05", "bias": "Picture Superiority", "strength": "subtle"},
      {"instance_id": "cb_06", "bias": "Curse of Knowledge", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Biased_6",
    "domain_id": "EM",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences spread across 4 decision points (2,2,1,1) by mechanism fit and narrative realism; no bias repeated within a decision point; co-located instances (DP1: cb_01/cb_02; DP2: cb_03/cb_04) assigned distinct evidence sources and reasoning operations per instance independence rule.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_dp1_timeline",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Planning/scoping timeline: “I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant anchors the estimate on a smaller prior project and acknowledges only a small adjustment despite known added scope and reduced staffing."
      },
      {
        "segment_id": "seg_dp1_format",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Scenario format choice: “I went with the legacy template again — third cycle running it. It's the one I know... more comfortable to work in.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "The participant prefers the repeatedly used legacy format for familiarity and comfort without a formal comparison of training outcomes."
      },
      {
        "segment_id": "seg_dp2_severity",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Severity calibration: “I ended up scaling the peak severity down toward the more familiar flood level” because no comparable flood had occurred locally in forty years.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The participant lets the absence of recent local experience make the modeled catastrophic case feel abstract despite updated risk modeling."
      },
      {
        "segment_id": "seg_dp2_peer_review",
        "speaker": "Participant",
        "segment_type": "comparative_reasoning",
        "raw_interview_anchor": "Peer AAR review: the participant calls a peer's mild scenario a planning gap while saying he was not worried about the same problem in his own concurrent build.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "The participant explicitly says he did not apply the same scrutiny to his own concurrent severity reasoning."
      },
      {
        "segment_id": "seg_dp3_injects",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Training inject priority: “Past surveys showed people remember those vividly — I figured that made them the more effective training tool.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_05"
        ],
        "ground_truth_rationale": "The participant prioritizes visual injects for memorability over data-rich material carrying the quantitative detail needed for operational decisions."
      },
      {
        "segment_id": "seg_dp4_handbook",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Handbook detail: the participant keeps standard shorthand and no glossary because the terms feel standard, despite prior requests for clearer explanations.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_06"
        ],
        "ground_truth_rationale": "The participant treats specialist terminology as obvious to less-experienced partner evaluators."
      },
      {
        "segment_id": "seg_close_two_weeks",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "Two-week hypothetical: the participant says he would add contingency and split visual/data production more evenly.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective counterfactual, not an additional hidden occurrence."
      },
      {
        "segment_id": "seg_close_new_planner",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "New-planner hypothetical: the participant speculates about different severity scrutiny and handbook assumptions.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a hypothetical comparison and does not add a new decision occurrence."
      },
      {
        "segment_id": "seg_close_uncertainty",
        "speaker": "Participant",
        "segment_type": "uncertainty_reasoning",
        "raw_interview_anchor": "Uncertainty close: the participant says the exercise and handbook consequences could have had multiple causes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant reports uncertainty about consequences; no new bias occurrence is asserted."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis was restricted to affirmatively evidenced bias-specific mechanisms in the transcript. Structural constraints such as fixed deadline, solo staffing, and time pressure were not classified as biases unless a distinct cognitive mechanism was evident."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Bias blind spot",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Curse of knowledge",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Status quo bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Vividness bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring effect",
      "alternative_labels": ["Anchoring and adjustment", "Insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which an initial value or prior reference point exerts excessive influence on subsequent estimates, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Timeline scoping decision",
      "decision_point_description": "Setting and communicating the initial project timeline estimate to the Director.",
      "affected_reasoning_operation": "Duration estimation and schedule scoping",
      "bias_specific_mechanism": "The 2019 project served as an initial anchor: six weeks, two staff, and a reused shell. The participant adjusted only slightly for a larger, solo, custom-hydrology build with multi-agency sign-off, allowing the original anchor to dominate the estimate.",
      "manifestation_in_interview": "The participant explicitly treated the 2019 project as the baseline, adjusted little for the new module, and communicated the same general delivery window despite being solo and building a new hydrology module from scratch.",
      "effect_on_reasoning_or_decision": "Produced an overly compressed timeline estimate with no formal contingency buffer; the project had already slipped two weeks by the four-week status check.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right, so going in, I looked at the 2019 project — six weeks, two staff, reused shell — and treated that as roughly the baseline. I adjusted a little for the new module, but not by much.",
          "evidence_explanation": "This directly shows an initial anchor being adopted and only weakly adjusted despite material differences in scope and staffing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember telling the Director I could deliver in the same general window even though I was down to one person and building the hydrology piece essentially from scratch.",
          "evidence_explanation": "The discrepancy between the anchor-based estimate and the changed circumstances shows the anchor persisting into the communicated decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, mostly that I'd done a version of this before and it worked out then. I didn't build in a formal contingency buffer — I considered it, there was an option to pad the schedule for the new module, but I went with compressing the new content into the existing window instead.",
          "evidence_explanation": "The past success serves as the salient anchor and supplants explicit contingency planning, illustrating insufficient adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd actually broken out hours for three-agency sign-off separately instead of folding it into 'coordination,' I probably would've padded the schedule more. I didn't do that breakdown until after the slip showed up.",
          "evidence_explanation": "This retrospectively identifies the missing adjustment away from the anchor, confirming the mechanism was an undifferentiated use of the prior timeline."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction observed; the participant later acknowledged that breaking out sign-off hours would have changed the estimate.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the task context; the label and mechanism are applied from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Status quo bias",
      "alternative_labels": ["Default bias", "Familiarity bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for the current or pre-existing state that leads to under-evaluation of alternatives even when they may be better suited.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scenario format selection",
      "decision_point_description": "Choosing which exercise scenario format to build from.",
      "affected_reasoning_operation": "Choice of scenario design format",
      "bias_specific_mechanism": "The legacy template served as the existing reference state; the participant selected it because it was familiar and comfortable, without formally comparing training outcomes or suitability for multi-agency exercises.",
      "manifestation_in_interview": "The participant chose the legacy template again despite a newer modular design being floated as better suited to multi-agency exercises. He explained the choice through familiarity, speed, and comfort rather than comparative performance data.",
      "effect_on_reasoning_or_decision": "Continued use of the legacy template without evaluating whether the modular format would better support multi-agency training or exercise outcomes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, there was a newer modular design format some of the stakeholders floated, supposedly better suited to multi-agency exercises. But I went with the legacy template again — third cycle running it. It's the one I know, I can build it fast, and honestly it's just more comfortable to work in.",
          "evidence_explanation": "The preference for the current familiar template is explicit, and the absence of a performance-based rationale supports a status-quo mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not formally, no. I didn't have data in front of me showing the modular format trains better or worse. It was more that I know exactly where everything goes in the old structure.",
          "evidence_explanation": "The participant confirms the decision was not based on comparative outcome data but on familiarity with the existing structure."
        }
      ],
      "correction_or_counterevidence": "Countervailing contextual factor: time pressure made the familiar template faster, which could be a legitimate professional heuristic; however, the transcript also shows a comfort-based preference and no formal comparison of alternatives.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the task context; the label and mechanism are applied from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments of probability, frequency, or plausibility are influenced by how easily instances come to mind rather than by complete data.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Severity calibration decision",
      "decision_point_description": "Setting the peak flood-severity calibration for the exercise scenario.",
      "affected_reasoning_operation": "Plausibility judgment and severity calibration",
      "bias_specific_mechanism": "The absence of an easily recalled local catastrophic flood in over forty years made the modeled high-severity case feel abstract and implausible, leading the participant to scale severity down toward the more familiar flood level.",
      "manifestation_in_interview": "The participant acknowledged that the forty-year point shaped his thinking: because nobody had seen a catastrophic event locally, the severe modeled scenario felt abstract rather than something the EOC would actually face.",
      "effect_on_reasoning_or_decision": "Peak severity was scaled down toward the familiar flood level, potentially under-testing EOC escalation procedures relative to the updated Corps modeling.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The updated Corps modeling was pointing to a higher catastrophic dam-failure risk than we'd planned around before. But the advisory committee kept coming back to the fact that we haven't seen flooding at that severity locally in over forty years. There was real pressure to keep the scenario grounded in something the community would find plausible.",
          "evidence_explanation": "The contrast between model-based risk and the salience of local history shows availability of familiar flood levels entering the plausibility judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up scaling the peak severity down toward the more familiar flood level. The forty-year point came up a lot in that conversation, and it did shape my thinking — if nobody's seen anything like the catastrophic case, it felt like we were designing for something abstract rather than something the EOC would actually face.",
          "evidence_explanation": "This explicitly links the ease of recalling or failing to recall local flooding to the severity decision, demonstrating availability rather than a purely data-driven calibration."
        }
      ],
      "correction_or_counterevidence": "Plausible non-bias consideration: designing a scenario the community would find plausible is a legitimate exercise-design goal; however, the transcript shows the absence of locally recalled flooding influenced severity calibration beyond that concern.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the task context; the label and mechanism are applied from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Bias blind spot",
      "alternative_labels": ["Blind spot bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to recognize cognitive biases in others while failing to see the same biases in oneself.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Peer AAR review and self-scrutiny",
      "decision_point_description": "Assessing another planner's exercise scenario during the period when the participant's own severity choice was unresolved.",
      "affected_reasoning_operation": "Evaluation of another planner's scenario and self-monitoring",
      "bias_specific_mechanism": "The participant readily attributed a peer's unrealistically mild scenario to a planning gap, but did not apply the same scrutiny to his own concurrent severity reasoning, producing asymmetric bias detection.",
      "manifestation_in_interview": "During the peer AAR discussion, the participant judged the other planner as having a planning gap while explicitly not worrying that his own severity decision might be failing under the same standard.",
      "effect_on_reasoning_or_decision": "Reduced self-scrutiny of the participant's own severity calibration, allowing the same under-stressing pattern to persist unexamined in his own scenario.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "In that discussion I was pretty clear it looked like a planning gap on their end. I wasn't especially worried about the same thing happening with my build, even though I was mid-decision on my own severity call at that exact time.",
          "evidence_explanation": "This shows simultaneous detection of a planning gap in another person and lack of equivalent worry about the same issue in oneself, the definitional pattern of the bias blind spot."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not in that moment, no. I was more focused on what they'd missed than on double-checking my own reasoning against the same standard.",
          "evidence_explanation": "The participant confirms asymmetric scrutiny, ruling out the explanation that he had already applied the same standard to himself."
        }
      ],
      "correction_or_counterevidence": "No contemporaneous correction observed; later reflection acknowledged that a different planner might have pushed harder on the severity call given the modeling.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the task context; the label and mechanism are applied from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Vividness bias",
      "alternative_labels": ["Vividness effect", "Salience bias", "Availability heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overweight vivid, concrete, or salient information relative to abstract, statistical, or less salient information when making judgments or choices.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Training inject prioritization",
      "decision_point_description": "Deciding which inject category to fully build with limited production time.",
      "affected_reasoning_operation": "Prioritization of training inject production",
      "bias_specific_mechanism": "Photo and video products were more dramatic, concrete, and memorable than abstract data packages; the participant treated their vividness and recall as the primary proxy for training effectiveness, overweighting them relative to operational decision-support value.",
      "manifestation_in_interview": "The participant allocated most remaining production time to photo/video injects because past surveys showed people remember those vividly, while acknowledging he focused on impact and recall rather than whether the flow-rate specifics would be available when needed for EOC modeling decisions.",
      "effect_on_reasoning_or_decision": "Most production time went to photo/video injects, leaving the data packages for EOC modeling decisions comparatively underdeveloped.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Option one was photo and video clips of levee overtopping — dramatic, but slow to produce. Option two was the data packages — stream gauge readouts, GIS flow-rate shapefiles — less visually interesting but more specific for EOC modeling decisions.",
          "evidence_explanation": "The options are explicitly distinguished by vividness versus decision-specificity, setting up a vividness-based choice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I put most of the remaining time into the photo and video injects. Past surveys showed people remember those vividly — I figured that made them the more effective training tool.",
          "evidence_explanation": "The decision is justified by vivid recall, not by an analysis of which inject type best supported the evaluator decisions."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Less than I probably should have, in retrospect. The reasoning at the time was really centered on impact and recall, not on whether the flow-rate specifics would be there when people needed them.",
          "evidence_explanation": "This confirms that the weighting of impact and recall displaced the operational decision-support consideration."
        }
      ],
      "correction_or_counterevidence": "Countervailing consideration: prior survey evidence of vivid recall is not irrelevant to training effectiveness; however, the decision substantially favored recall and impact over operational decision needs without formal weighting.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the task context; the label and mechanism are applied from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Curse of knowledge",
      "alternative_labels": ["Expert blind spot"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which a knowledgeable person fails to account for another person's lack of background knowledge, assuming that jargon, shorthand, or concepts are as clear to others as they are to oneself.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Controller-Evaluator handbook development",
      "decision_point_description": "Deciding whether to include a glossary or clearer explanations in the Controller-Evaluator handbook.",
      "affected_reasoning_operation": "Communication design and assumption about evaluator knowledge",
      "bias_specific_mechanism": "The participant's 15 years of experience made his shorthand and scoring conventions feel standard and obvious, causing him to discount prior feedback that evaluators outside core emergency management needed clearer explanations.",
      "manifestation_in_interview": "Despite informal feedback in past AARs asking for clearer explanations, the participant kept the handbook concise without a glossary because the terms felt standard to him.",
      "effect_on_reasoning_or_decision": "The handbook remained concise without a glossary, likely contributing to scoring inconsistencies among evaluators without the same background.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've been doing this fifteen years, and I've used the same shorthand and scoring conventions across a lot of exercises. Time was short, so I kept the handbook concise — standard terminology, no glossary.",
          "evidence_explanation": "The participant's extensive experience is framed as a reason for assuming standard terminology, which is the foundation of curse of knowledge."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There'd been informal feedback in past AARs asking for clearer explanations for evaluators outside core EM, yeah. But the terms felt pretty standard to me, so I didn't prioritize adding that layer given how little time was left.",
          "evidence_explanation": "Past feedback directly contradicts the participant's assumption of shared understanding, yet he dismisses it because the terms felt standard to him, demonstrating the mechanism."
        }
      ],
      "correction_or_counterevidence": "Time pressure was a real constraint; nevertheless, prior feedback specifically requested clearer explanations for outside evaluators, and the participant's subjective sense of standardness drove the decision not to prioritize that layer.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the task context; the label and mechanism are applied from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied in the task context; all label assignments rely on general cognitive-science knowledge and explicit transcript evidence rather than retrieval.",
    "Speaker attribution is limited to the transcript labels 'Interviewer' and 'Participant'; some severity-calibration reasoning reflects the participant's report of advisory committee influence."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Biased_6_Sonnet_off",
  "interview_id": "EM_Biased_6",
  "system_prompt_id": "Sonnet",
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
