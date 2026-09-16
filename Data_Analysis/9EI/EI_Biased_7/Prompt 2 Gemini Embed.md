You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a confidential discussion about how you approached a specific staffing decision last term — nothing you say here goes into any personnel file, and you can decline to answer anything. That work for you?

Participant: Yes, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me your role and what you were responsible for deciding during that period?

Participant: I chair the Communications Department. Every spring we run the adjunct renewal cycle — deciding which non-tenure-track instructors get contracts for the following fall. That term it landed right on top of our accreditation self-study, plus the curriculum committee was finishing a two-year review of our capstone sequence. So I had three processes converging in about a month, all needing sign-off from me.

Interviewer: What made this cycle different from previous ones?

Participant: Normally renewal is routine — you look at the evaluation trend, check for any complaints, and move on. This time one of our longer-tenured adjuncts, who'd taught the intro public speaking sequence for years with strong numbers, had a rockier semester. And it collided with the committee wanting to repurpose his teaching line for a new elective. So instead of one clean decision, it turned into four separate calls over about six weeks.

Interviewer: Let's get the whole account first, and then we'll go back through it step by step. What happened?

Participant: HR gave us 48 hours to submit the renewal list, which is tight, but it's not unusual — everyone's juggling the self-study at the same time. This instructor had three straight years averaging 4.6 out of 5 on his teaching evaluations, so on paper he was one of our strongest adjuncts. Only two of his four sections had scores in yet, and those were down to 3.9. I had to decide whether to hold the list for the missing two sections or go with what I had.

A week after I submitted him for renewal, the other two sections came in lower still — 3.6 average — and around the same time I got a batch of complaint emails, five students, all from one section, saying his lectures felt disorganized and his grading was inconsistent. That same week he'd pushed back pretty hard on a rubric change I'd proposed at a faculty meeting — raised his voice a bit, which isn't like him. I looked at the roster for the complaining section and noticed most of those students had come in through our new transfer-pathway cohort. Meanwhile his other three sections had zero complaints.

Then the curriculum committee, which had been building toward "modernizing" the capstone for two years, proposed folding his line into a new elective a senior colleague wanted to launch. I had a peer-observation memo calling his classroom management "adequate but inconsistent," and around the same time an external accreditation reviewer who'd sat in on one of his sessions wrote that it was "well-structured and responsive." I ended up backing the reallocation.

Finally, three weeks before the HR deadline, with no replacement lined up, I had to decide renew or not. I'd had two one-on-one meetings with him that term and both felt defensive on his end. I went with non-renewal and had to write the Dean a short memo justifying it.

Interviewer: Let's reconstruct the order precisely. What did you know before you made the first call, versus what came in afterward?

Participant: Before: the three-year average, the two-section partial data, the deadline. After: the other two sections' scores, and separately, the complaint batch. The meeting blow-up and the roster detail came in around the same window as the complaints. The peer memo and the accreditation report landed close together, right before the committee vote. And the "defensive" meetings happened gradually across the term, so by the time of the final decision that impression was already fully formed in my head.

Interviewer: On that first decision — submitting him for renewal with only half the current-term data — walk me through your reasoning.

Participant: The deadline was real, 48 hours, and I had the self-study eating the rest of my week. Three years at 4.6 is a strong track record, and 3.9 on two sections isn't alarming by itself — it's still solidly good. My read was that the missing two sections were unlikely to change the overall picture much, so I submitted him.

Interviewer: Did you consider asking for even a short extension, or checking in with the instructor or students directly before the deadline?

Participant: I thought about emailing HR for two more days, yeah. I didn't, mostly because I assumed it wouldn't move the needle — his history was so consistent. In hindsight I could have just called the two sections' students directly, that would've taken twenty minutes, but with the self-study deadline stacked on top I didn't prioritize it.

Interviewer: When the complaints and the meeting incident arrived close together, how did you interpret them?

Participant: Honestly, the meeting was fresh in my mind — he'd been unusually sharp with me, out of character — and when the complaint emails came in days later describing "disorganized" and "unfair," it read to me like confirmation that something had shifted with him generally, not just in one classroom. I didn't have anything connecting the meeting tone to his actual teaching that term, but it felt like part of the same pattern.

Interviewer: Separately, you mentioned the roster composition. How did that factor in?

Participant: Right — when I saw most of the complainants were from the transfer-pathway cohort, my sense was that group tends to be more vocal about grading generally, so I weighted the complaints a bit less as a reflection of his teaching specifically. I didn't actually check whether that cohort files more complaints in other courses; it was more of an impression from prior semesters.

Interviewer: What alternative did you rule out there?

Participant: I could have gone section by section, talked to a TA, looked at whether other instructors teaching that same cohort saw similar patterns. I didn't do that before forming my view.

Interviewer: Move to the committee decision on the teaching line. What tipped you toward reallocation?

Participant: The committee had been pushing capstone modernization for two years, and by that point I had the complaints, the meeting tension, and now a peer memo calling his management "inconsistent." It all fit together into a fairly clear story — declining performance, aligned with a change the department already wanted to make. The accreditation reviewer's report was more positive, but reviewers usually only see one session, so I gave that less weight. Actually, if I'm honest, the peer memo came from a single sit-in too — one class period — but I read "inconsistent" as more representative of what was really going on, since it lined up with what I was already hearing from the complaints.

Interviewer: The enrollment numbers for the capstone had actually grown 8% that year. Did that come up in your reasoning?

Participant: It's in the file, but no, I didn't really fold it into the recommendation. The narrative we were building was about quality and modernization, not enrollment, so it didn't feel central at the time.

Interviewer: Last decision point — the final renewal call under the three-week deadline, with no replacement identified. What drove that?

Participant: There was a real cost to leaving it unresolved — HR needed an answer, and dragging it out would've meant scrambling even harder later. I could have extended him short-term while we did a fuller review, but I wanted the question closed so I could focus on the self-study. When I wrote the memo to the Dean, I mostly drew on my two meetings with him — I'd sat across from him myself both times, and that felt like a more reliable read on where he really stood than notes filtered through a TA or a peer observer who'd only caught one class. So that's what I led with.

Interviewer: How confident were you in that final call, on a gut level?

Participant: Moderately. I knew the file had more in it than what I used, but I trusted my own sense of him over those secondhand accounts, so I didn't go back and weigh the TA or peer material more heavily.

Interviewer: A couple of hypotheticals. If the missing two sections' scores had been available before your first decision, would anything have changed?

Participant: Possibly — if I'd seen 3.6 upfront instead of after, I might have paused the renewal rather than approving it outright.

Interviewer: If the accreditation report had reached the committee before the vote instead of after, do you think the outcome shifts?

Participant: Maybe. It might have at least prompted a conversation instead of being filed quietly.

Interviewer: And if you'd had a vetted replacement ready to go, would the final decision have looked different?

Participant: I think I still lean non-renewal given everything by that point, but I probably would've extended him for a term instead of cutting it off right there. The absence of a replacement pushed me toward closing it out faster than I might have otherwise.

Interviewer: That's really helpful — thank you for walking through all of that in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Biased_7",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Horn Effect",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Present Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Group attribution error",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Egocentric bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Biased Assimilation",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Coherence-based reasoning or Rationalisation",
      "Bounded Rationality",
      "Horn Effect",
      "Present Bias",
      "Group attribution error",
      "Egocentric bias",
      "Biased Assimilation"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Coherence-based reasoning or Rationalisation", "requested_occurrences": 1 },
      { "bias": "Bounded Rationality", "requested_occurrences": 1 },
      { "bias": "Horn Effect", "requested_occurrences": 1 },
      { "bias": "Present Bias", "requested_occurrences": 1 },
      { "bias": "Group attribution error", "requested_occurrences": 1 },
      { "bias": "Egocentric bias", "requested_occurrences": 1 },
      { "bias": "Biased Assimilation", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Bounded Rationality" },
      { "instance_id": "cb_02", "bias": "Horn Effect" },
      { "instance_id": "cb_03", "bias": "Group attribution error" },
      { "instance_id": "cb_04", "bias": "Coherence-based reasoning or Rationalisation" },
      { "instance_id": "cb_05", "bias": "Biased Assimilation" },
      { "instance_id": "cb_06", "bias": "Present Bias" },
      { "instance_id": "cb_07", "bias": "Egocentric bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Bounded Rationality", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Horn Effect", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Group attribution error", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Coherence-based reasoning or Rationalisation", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Biased Assimilation", "decision_point": 3 },
      { "instance_id": "cb_06", "bias": "Present Bias", "decision_point": 4 },
      { "instance_id": "cb_07", "bias": "Egocentric bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Bounded Rationality",
        "mechanism": "Satisficing on partial/historical data under deadline pressure instead of seeking complete current evaluation data.",
        "affected_reasoning_operation": "Evidence-sufficiency judgment before renewal decision",
        "evidence_source": "Historical SET average and partial current-term SET data",
        "distinctiveness_requirement": "Must be the only instance involving deadline-driven curtailment of data-gathering effort at decision point 1."
      },
      {
        "instance_id": "cb_02",
        "bias": "Horn Effect",
        "mechanism": "Negative meeting exchange spreads to color interpretation of unrelated classroom complaints.",
        "affected_reasoning_operation": "Cross-domain trait inference from one negative event",
        "evidence_source": "Faculty-meeting rubric exchange and complaint emails",
        "distinctiveness_requirement": "Must involve the meeting-to-classroom trait spillover, distinct from cb_03's cohort-based attribution at the same decision point."
      },
      {
        "instance_id": "cb_03",
        "bias": "Group attribution error",
        "mechanism": "Complaint pattern attributed to a perceived trait of the students' admission cohort rather than section-specific factors.",
        "affected_reasoning_operation": "Causal attribution of observed behavior to group membership",
        "evidence_source": "Roster composition data on complainants' cohort membership",
        "distinctiveness_requirement": "Must use cohort-roster evidence, distinct from cb_02's meeting-exchange evidence at the same decision point."
      },
      {
        "instance_id": "cb_04",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "Facts assembled into one fluent decline narrative that omits the contrary enrollment-growth figure.",
        "affected_reasoning_operation": "Narrative construction and selective integration of decision rationale",
        "evidence_source": "Committee's modernization narrative plus complaint and meeting history",
        "distinctiveness_requirement": "Must center on overall narrative construction and omission of enrollment data, distinct from cb_05's evaluation of the two written reports."
      },
      {
        "instance_id": "cb_05",
        "bias": "Biased Assimilation",
        "mechanism": "Mixed peer memo read as confirmatory; positive accreditation report discounted via stricter credibility standard.",
        "affected_reasoning_operation": "Evaluation of ambiguous/mixed evidence against a prior-held belief",
        "evidence_source": "Peer-observation memo and external accreditation report",
        "distinctiveness_requirement": "Must center on differential credibility standards applied to two specific written reports, distinct from cb_04's broader narrative construction."
      },
      {
        "instance_id": "cb_06",
        "bias": "Present Bias",
        "mechanism": "Immediate closure of the staffing question prioritized over the larger deferred cost of unstaffed course coverage.",
        "affected_reasoning_operation": "Intertemporal trade-off between short-term relief and long-term cost",
        "evidence_source": "HR deadline and absence of a vetted replacement instructor",
        "distinctiveness_requirement": "Must be the only instance involving a time-discounting trade-off between immediate relief and deferred departmental cost."
      },
      {
        "instance_id": "cb_07",
        "bias": "Egocentric bias",
        "mechanism": "Personal meeting recollections foregrounded as central evidence in the justification memo, discounting other stakeholder input.",
        "affected_reasoning_operation": "Memory retrieval and evidence weighting during justification drafting",
        "evidence_source": "Chair's own recollection of two personal meetings",
        "distinctiveness_requirement": "Must be the only instance involving self-referential weighting of personally experienced interactions over third-party evidence (TA/peer notes)."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Bounded Rationality", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Horn Effect", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Group attribution error", "strength": "moderate" },
      { "instance_id": "cb_04", "bias": "Coherence-based reasoning or Rationalisation", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Biased Assimilation", "strength": "subtle" },
      { "instance_id": "cb_06", "bias": "Present Bias", "strength": "subtle" },
      { "instance_id": "cb_07", "bias": "Egocentric bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Biased_7",
    "domain_id": "EI",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across all 4 decision points with mechanism-fit prioritization; decision points 2 and 3 each host two distinct biases separated by independent evidence sources (roster composition vs. meeting exchange; narrative construction vs. differential report credibility) per Rule 4 of the allocation rules; no single bias exceeds one occurrence at any decision point, satisfying the manifest's occurrences=1 for every bias.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis relied exclusively on the interview transcript; retrieved passages were used only for construct validation. Two confirmation-bias episodes were affirmatively identified. Other plausible mechanisms were logged as candidates because the transcript evidence was insufficient under conservative diagnostic standards."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 2
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "biased assimilation",
        "myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's prior beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting student complaints in context of recent faculty meeting",
      "decision_point_description": "Deciding whether the complaint emails and the faculty-meeting incident reflected a general decline in teaching performance.",
      "affected_reasoning_operation": "Evidence interpretation and pattern perception",
      "bias_specific_mechanism": "An affectively salient but teaching-unrelated interpersonal event, the faculty-meeting blow-up, was treated as a confirming datapoint for the hypothesis that the instructor had declined generally, despite no established link between meeting tone and classroom performance.",
      "manifestation_in_interview": "The participant described the complaint emails as confirmation that something had shifted with the instructor generally, while also acknowledging there was no evidence connecting the meeting tone to teaching.",
      "effect_on_reasoning_or_decision": "It strengthened a negative impression of the instructor, which later fed into weighting of other evidence and the reallocation/non-renewal trajectory.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the meeting was fresh in my mind — he'd been unusually sharp with me, out of character — and when the complaint emails came in days later describing 'disorganized' and 'unfair,' it read to me like confirmation that something had shifted with him generally, not just in one classroom. I didn't have anything connecting the meeting tone to his actual teaching that term, but it felt like part of the same pattern.",
          "evidence_explanation": "This quote explicitly documents an interpretive distortion: the participant used an unrelated interpersonal event as confirmatory evidence for a teaching-decline hypothesis, while simultaneously admitting the absence of a factual connection. That is a direct manifestation of confirmation bias in evidence interpretation."
        }
      ],
      "correction_or_counterevidence": "He immediately noted the absence of evidence connecting the meeting tone to teaching, but this recognition did not prevent the confirmation interpretation from shaping his impression.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Hallihan et al. passage provides general support for the confirmation bias construct, though from a design-reasoning context rather than personnel decision-making.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "These results closely replicate the findings from earlier experiments on confirmation bias (Wason, 1968) but with a situation more relevant to design.",
          "mechanism_supported_by_source": "Confirmation bias as a tendency to seek or evaluate evidence in ways that confirm pre-existing beliefs.",
          "relevance_to_this_occurrence": "The participant interpreted ambiguous complaint information as confirming a negative conclusion derived from an unrelated meeting, consistent with confirmation bias."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "biased assimilation",
        "selective evaluation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's prior beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluating peer-observation and accreditation reviewer evidence for teaching-line reallocation",
      "decision_point_description": "Backing the curriculum committee's proposal to fold the adjunct's teaching line into a new elective.",
      "affected_reasoning_operation": "Evidence weighting and assessment of source reliability",
      "bias_specific_mechanism": "Asymmetric discounting of a positive external observation relative to a negative peer observation, despite both relying on single-session observations, because the negative report cohered with an already-formed decline narrative.",
      "manifestation_in_interview": "He acknowledged that both reports came from single class visits, but treated the positive accreditation report as less diagnostic while treating the negative peer memo as more representative because it lined up with prior complaints.",
      "effect_on_reasoning_or_decision": "Facilitated endorsement of reallocation by reinforcing a coherent negative narrative and reducing the influence of potentially contradictory positive evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The committee had been pushing capstone modernization for two years, and by that point I had the complaints, the meeting tension, and now a peer memo calling his management 'inconsistent.' It all fit together into a fairly clear story — declining performance, aligned with a change the department already wanted to make. The accreditation reviewer's report was more positive, but reviewers usually only see one session, so I gave that less weight. Actually, if I'm honest, the peer memo came from a single sit-in too — one class period — but I read 'inconsistent' as more representative of what was really going on, since it lined up with what I was already hearing from the complaints.",
          "evidence_explanation": "This quote explicitly documents asymmetric evaluation of two structurally similar sources based on consistency with a prior belief. The participant even catches himself acknowledging the double standard, which is strong evidence of confirmation bias in evidence weighting."
        }
      ],
      "correction_or_counterevidence": "He briefly recognized the double standard, but this recognition did not alter how he weighted the reports in the decision.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Hallihan et al. passage provides general support for the confirmation bias construct, though from a design-reasoning context rather than personnel decision-making.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "These results closely replicate the findings from earlier experiments on confirmation bias (Wason, 1968) but with a situation more relevant to design.",
          "mechanism_supported_by_source": "Confirmation bias as a tendency to seek or evaluate evidence in ways that confirm pre-existing beliefs.",
          "relevance_to_this_occurrence": "The participant discounted positive evidence and favored negative evidence based on consistency with a pre-existing decline narrative, consistent with confirmation bias."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial renewal decision with partial current-term evaluation data",
      "supporting_interview_quote": "I thought about emailing HR for two more days, yeah. I didn't, mostly because I assumed it wouldn't move the needle — his history was so consistent.",
      "plausible_mechanism": "Anchoring on the 4.6 three-year average and insufficiently adjusting to the lower 3.9 current sections when predicting missing scores; time pressure may have amplified reliance on the anchor.",
      "why_not_identified": "Incomplete information, deadline pressure, and a legitimate track record provide a plausible non-bias explanation; the transcript does not clearly demonstrate a distinct anchoring distortion rather than ordinary decision-making under uncertainty."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "representativeness heuristic",
      "alternative_labels": [
        "availability heuristic"
      ],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Weighting student complaints by transfer-pathway cohort membership",
      "supporting_interview_quote": "when I saw most of the complainants were from the transfer-pathway cohort, my sense was that group tends to be more vocal about grading generally, so I weighted the complaints a bit less as a reflection of his teaching specifically. I didn't actually check whether that cohort files more complaints in other courses; it was more of an impression from prior semesters.",
      "plausible_mechanism": "Using a group-level impression retrieved from memory to discount specific complaint evidence without checking base rates, consistent with representativeness or availability heuristics.",
      "why_not_identified": "The transcript does not establish that the impression was inaccurate or that the discounting distorted the decision; it may be a legitimate use of past knowledge, and no comparative base rates were examined."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence effect",
      "alternative_labels": [
        "illusion of validity",
        "egocentric evidence weighting"
      ],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final non-renewal memo and reliance on personal meetings",
      "supporting_interview_quote": "I knew the file had more in it than what I used, but I trusted my own sense of him over those secondhand accounts, so I didn't go back and weigh the TA or peer material more heavily.",
      "plausible_mechanism": "Overweighting direct personal impressions relative to documented observations and self-assessed reliability, potentially inflated by the availability or vividness of face-to-face meetings.",
      "why_not_identified": "Direct personal interaction can legitimately provide richer information than secondhand reports; the transcript reports moderate confidence rather than explicit overconfidence, so there is insufficient evidence of a distinct bias mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a self-report; verbal rationalizations may not fully capture internal cognitive mechanisms.",
    "Retrieved corpus support was limited to confirmation bias; other plausible mechanisms are logged as candidates and require additional evidence.",
    "No outcome information was used to impute bias; all classifications rely on reasoning available at the time and explicit testimony.",
    "The analysis uses a conservative threshold, so some plausible but ambiguous heuristic patterns were not counted as identified occurrences."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Biased_7_Gemini_on",
  "interview_id": "EI_Biased_7",
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
