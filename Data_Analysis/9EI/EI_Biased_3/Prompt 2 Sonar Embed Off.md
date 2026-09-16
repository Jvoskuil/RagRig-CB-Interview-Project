You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Before we begin, do I have your consent to discuss a past case in a way that does not identify the student, family, school, or sending program?

Participant: Yes, that is fine.

Interviewer: Please describe your role at the time.

Participant: I was the special education caseworker and IEP Coordinator for an elementary building. I carried about 42 active IEPs, coordinated meetings, drafted present levels of performance, tracked compliance timelines, and worked with the school psychologist and classroom teams when a student transferred in. This case involved a student who arrived mid-year from an out-of-district specialized program. We had ten school days to establish an interim placement and services.

Interviewer: What was the main objective?

Participant: We needed a legally compliant interim IEP that gave the student access to instruction right away, identified an appropriate least restrictive environment, and gave the classroom team enough structure to begin. The challenge was that the records came in pieces. The parent expected a real decision at the interim meeting, but we did not yet have a full picture.

Interviewer: Walk me through what happened from the transfer notice to the meeting.

Participant: The registrar notified us late on a Thursday that the student would start the following Monday. The transfer summary said the student came from a program serving students with significant emotional and behavioral needs. We had a short IEP excerpt, an eligibility category, and a reference to a functional behavior assessment and behavior intervention plan from about 18 months earlier. The full cumulative file had not arrived.

On the first day, I met briefly with the parent, the classroom teacher, and the principal. The parent described the student as bright and said the previous year had gone much better. The classroom teacher was open to inclusion but was worried about bringing in a student with an unknown behavioral history during the middle of the year. The principal was focused on getting a schedule in place without repeatedly moving students or staff.

I asked the sending program for records and contacted our school psychologist about testing. The old cognitive and academic assessments were already more than two years old. In the meantime, the student attended general education with support from an instructional paraprofessional during transitions and less structured periods.

During the first week, most reports were fairly calm. Then the paraprofessional described an outburst during a transition from recess to writing. That became part of what I had to synthesize for the interim IEP. We held the meeting near the end of the ten-day window. By then we had more records, but not updated testing, and there were still limits on how much direct observation I had completed.

Interviewer: At the beginning, what information did you have, and what arrived later?

Participant: Initially, I had the transfer summary, the short IEP excerpt, the old FBA/BIP reference, and my conversations with the parent and school staff. Later, the fuller records showed that the BIP had been faded out in the sending setting and that the student had gone roughly nine months without a documented behavioral incident. That was important context, but it arrived after I had already started forming an interim placement view.

Interviewer: Let’s go back to your first key decision. What did you decide before the full records arrived?

Participant: I decided to prepare the team for a more supported interim placement rather than begin with full inclusion as the likely recommendation. I did not make a final placement decision that day, but I was leaning toward partial pull-out and more structured adult support.

Interviewer: What cues stood out?

Participant: The sending program stood out. In my experience, students transferring from that program often needed a fairly high level of behavioral structure when they first arrived. The reference to prior aggression and an FBA/BIP reinforced that. We had received several transfers from there over the years, and they generally did not transition smoothly into a fully general education schedule immediately.

Interviewer: What alternatives did you consider?

Participant: One option was to hold off on any placement lean until the full individualized file came through and simply use temporary supports. Another was to begin planning for a structured setting so we would not be caught unprepared at the meeting. I chose the second approach because the timeline was short, and it seemed safer to have that option built into the draft schedule.

Interviewer: How confident were you?

Participant: Moderately confident, not completely. I knew the summary was incomplete. But I felt that the program history told me something meaningful about the kind of supports we might need at the start. If the student had come from a less specialized setting, I think I would have been more comfortable starting with a full-inclusion assumption while we gathered data.

Interviewer: What information would have changed that initial lean?

Participant: Current behavior data, recent progress notes, evidence that the BIP was no longer active, and a detailed description of how the student handled general education classes. Once the fuller record showed the long incident-free period, I had to adjust my thinking. Still, by then the structured option was already the frame I had brought into our early planning conversations.

Interviewer: What was the next decision point?

Participant: The reevaluation question. The existing testing was stale, and the student’s prior goals did not give us a current academic profile. Our school psychologist was booked for about three weeks, which was beyond the interim timeline.

Interviewer: What did you do?

Participant: I wrote the interim plan using the old testing, existing goals, classroom information, and generic accommodations rather than trying to force an expedited assessment process. I deferred the full reevaluation discussion to the annual review period.

Interviewer: What alternatives were available?

Participant: I could have asked the psychologist to see whether there was an emergency opening, requested brief curriculum-based measures, or built a more explicit bridge plan with a reassessment date soon after the interim meeting. That would have meant coordinating another set of forms, getting teacher input quickly, and trying to rearrange a schedule that was already tight.

Interviewer: Why did you choose to defer it?

Participant: Frankly, I was trying to get a compliant interim IEP done without creating another moving part. We had ten days, I had a full caseload, and the psychologist had no visible opening. The old data were not ideal, but they were usable enough to put services in place. I told myself we could revisit testing at the annual review.

Interviewer: Did you expect the old data might create a problem before then?

Participant: Yes. I knew there was a good chance the accommodations would need adjustment once the teacher had more academic data. The student’s work samples already suggested the old profile might not fit perfectly. But requesting a special process immediately felt like it would slow everything down, and I wanted the team to leave the meeting with something settled.

Interviewer: What happened afterward?

Participant: A few weeks later, the classroom teacher said the accommodations were mismatched. The student was reading above grade level but struggled with some written-output demands that the old plan did not capture well. We ultimately needed updated testing anyway. In retrospect, an earlier bridge assessment might have made the interim plan more precise.

Interviewer: Let’s move to the present levels. What information did you have at that point?

Participant: I had two teacher check-ins saying the student was generally polite with peers and participated when prompted. I had reading work samples that were stronger than expected. I also had the paraprofessional’s report of the recess-to-writing transition. The student reportedly yelled, pushed materials off a desk, and needed about ten minutes with adult support before returning to class. I had only observed briefly myself, so that report was vivid because it was the most detailed account of a difficult moment.

Interviewer: What did you decide when drafting the PLOP?

Participant: I wrote that the student’s behavioral regulation could interfere with consistent classroom engagement and peer interactions, and I recommended transition support and check-ins. I also described the student as needing substantial adult prompting to remain productively engaged.

Interviewer: What alternatives did you consider?

Participant: I could have written a more separated description: strong reading performance, generally positive peer interactions based on teacher reports, and one transition incident requiring follow-up data. Or I could write a broader concern statement so the receiving team would understand that the student might be harder to support than the work samples alone suggested.

Interviewer: What was your reasoning?

Participant: That transition episode concerned me. When a student has an outburst during a routine shift in the day, it can affect more than the transition itself. I worried that the same difficulty would show up in group work, independent work, and peer situations, even though the teacher check-ins had been positive. I did not want the team to read “above-grade-level reading” and underestimate the level of support the student might need.

Interviewer: Did later information affect that view?

Participant: Yes. We gathered more feedback, and it consistently showed that the student was engaged academically and got along with peers most of the time. The classroom team still wanted transition supports, which made sense, but my initial wording was broader than the later evidence supported.

Interviewer: What was the final decision at the interim meeting?

Participant: We had to determine service minutes and the LRE. I presented two options: full inclusion with consultative behavioral support, or partial pull-out for targeted support while the team collected more data. By that point, I reviewed the attendance information, classroom schedule, teacher input, parent input, work samples, the transition incident, and the records that had arrived.

Interviewer: What did the team choose?

Participant: We chose partial pull-out for a limited portion of the day, focused on writing organization and transition support, with general education for the rest of the schedule. The parent preferred keeping the student with peers as much as possible, and the teacher could support that schedule. The principal’s scheduling concern was real, but it was not the deciding factor. We documented why the service minutes were temporary and set a review point.

Interviewer: What did you learn after that decision?

Participant: The parent asked for a follow-up review in six weeks. That was appropriate. It gave us a chance to look at actual classroom data rather than treating the interim decision as permanent.

Interviewer: If the psychologist had immediate testing availability, would you have approached the reassessment decision differently?

Participant: Yes. I would have requested updated testing right away and probably written more individualized accommodations from the beginning.

Interviewer: If the paraprofessional’s report had not come in, how might the PLOP have read differently?

Participant: I likely would have emphasized the positive classroom information and the reading strengths more clearly, while noting that we still needed direct observations of transitions.

Interviewer: And if the compliance timeline had been longer?

Participant: I would have waited for the full records, gathered more observations, and convened with a more complete set of current data before making the interim placement recommendation.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Biased_3",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "Special Education Caseworker / IEP Coordinator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Interim Placement for a Mid-Year IEP Transfer",
    "scenario_summary_internal": "An IEP Coordinator must process a mid-year transfer student arriving from an out-of-district specialized behavioral program, complete an interim placement within a mandatory 10-school-day compliance window, and draft present levels and services with incomplete records, a testing backlog, and a single vivid behavioral incident report from a paraprofessional, while balancing caseload pressure against individualized decision-making.",
    "occupational_realism": {
      "objective": "Determine a compliant interim IEP placement, present levels of performance, and service minutes for a transferring student within the statutory timeline, using the best available evidence.",
      "setting": "Public elementary school special education department, mid-year transfer, 10-school-day interim placement mandate",
      "constraints": [
        "10-school-day statutory deadline for interim placement determination",
        "Caseload of 42 active IEP students",
        "School psychologist has a 3-week testing backlog",
        "Incomplete transfer records arriving in stages from sending program",
        "Parent expects a placement decision at the interim meeting",
        "Principal wants minimal disruption to general education scheduling"
      ],
      "stakeholders": [
        "IEP Coordinator (interviewee)",
        "General education classroom teacher",
        "Instructional paraprofessional",
        "School psychologist",
        "Parent/guardian",
        "Sending program liaison",
        "Building principal"
      ],
      "technical_terms_to_use": [
        "interim placement",
        "present levels of performance (PLOP)",
        "functional behavior assessment (FBA)",
        "behavior intervention plan (BIP)",
        "least restrictive environment (LRE)",
        "service minutes",
        "related services",
        "eligibility category",
        "compliance timeline",
        "reevaluation"
      ],
      "technical_terms_to_avoid": [
        "group attribution error",
        "present bias",
        "horn effect",
        "halo effect",
        "stereotype",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Transfer summary sheet identifies sending program as a specialized placement for students with significant emotional/behavioral disabilities",
          "Prior IEP excerpt mentions an FBA/BIP written 18 months ago for aggression",
          "Full cumulative file has not yet arrived from the sending program",
          "Coordinator has prior familiarity with several other students who transferred from the same sending program"
        ],
        "new_information_after_decision": [
          "Full records arrive later showing the BIP was successfully faded out and the student had 9 incident-free months before transfer"
        ],
        "alternatives": [
          "Withhold any interim placement lean until the full individualized file arrives",
          "Form an initial interim placement lean based on the general profile of students typically served by the sending program"
        ],
        "intended_action": "Coordinator leans toward recommending a more restrictive interim placement based on a general impression of the sending program's population, ahead of receiving the student's individualized data."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Existing cognitive/academic testing is over 2 years old and due for reevaluation",
          "School psychologist's earliest testing slot is 3 weeks out",
          "Interim placement decision is due in 10 school days",
          "Caseload workload is already at capacity"
        ],
        "new_information_after_decision": [
          "Weeks later, the classroom teacher reports the accommodations do not match the student's current academic profile, and updated testing turns out to be necessary regardless"
        ],
        "alternatives": [
          "Request expedited or temporary testing accommodations and build a short bridge plan while assessment is pending",
          "Skip requesting new testing now, write the interim IEP entirely from old data and generic classroom accommodations, and defer full reassessment to the annual review months later"
        ],
        "intended_action": "Coordinator chooses the lower-effort immediate option, writing the interim plan from outdated data and pushing reassessment far into the future, discounting the near-term cost of delayed information."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Paraprofessional reports one specific outburst during a classroom transition",
          "Two separate teacher check-ins describe consistently positive peer interactions",
          "Work samples show reading performance above grade level",
          "Coordinator has only briefly observed the classroom in person"
        ],
        "new_information_after_decision": [
          "Additional peer and teacher feedback collected afterward consistently shows strong academic engagement, at odds with the coordinator's broader write-up"
        ],
        "alternatives": [
          "Weigh the single outburst alongside the broader academic and social evidence when drafting present levels",
          "Let the one vivid negative incident generalize into the overall description of the student's academic engagement and social skills"
        ],
        "intended_action": "Coordinator drafts present levels that extend the behavioral concern from the single incident into an overall more negative characterization of the student's academic and social functioning."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "All records, testing history, and observation notes collected to date",
          "Parent is present and expects a service-minutes decision at the interim meeting",
          "Principal has flagged general-education scheduling constraints"
        ],
        "new_information_after_decision": [
          "Parent requests a follow-up review in 6 weeks to confirm the service minutes are adequate"
        ],
        "alternatives": [
          "Propose full inclusion with consultative behavior support",
          "Propose partial pull-out for targeted skill instruction"
        ],
        "intended_action": "Coordinator finalizes service minutes and LRE recommendation using a documented rationale drawn from the assembled record, without introducing a new bias mechanism at this decision point."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and caseload at the time of this case?",
        "What was the operational goal for this student's interim placement?"
      ],
      "timeline_reconstruction": [
        "Walk me through what happened, in order, from the transfer notice to the interim meeting.",
        "What information did you have at each stage, and what arrived later?"
      ],
      "decision_point_probes": [
        "What cues stood out to you at this point in the case?",
        "What information sources did you rely on, and which were unavailable?",
        "What were you trying to accomplish with this particular decision?",
        "What alternatives did you consider, and why did you choose the one you did?",
        "What was the basis for that decision?",
        "Had you handled a similar situation before, and did that shape your approach?",
        "How much time pressure were you under at this point?",
        "How confident were you in the information you had?",
        "If a key fact had been different, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If the student had transferred from a different, less specialized program, would your interim lean have been the same?",
        "If the psychologist had immediate testing availability, would you have made the same choice about reassessment?",
        "If the paraprofessional's report hadn't come in, how might the present levels have read differently?",
        "If the compliance timeline had been longer, what would you have done differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "gae_01",
        "bias": "Group attribution error",
        "decision_point": 1,
        "mechanism": "Generalizing the assumed dispositional profile of students from a specific sending program onto this individual student before individualized records arrive",
        "affected_reasoning_operation": "Initial placement inference from partial group-identifying information",
        "evidence_available_at_time": [
          "Transfer summary naming the sending program's population type",
          "An 18-month-old FBA/BIP reference",
          "Coordinator's prior experience with other transfers from the same program"
        ],
        "required_textual_manifestation": "Coordinator explicitly frames the initial placement lean in terms of what students from that program are generally like, rather than in terms of this student's individual, current data",
        "plausible_nonbias_interpretation": "Using base-rate information from a known feeder program as a reasonable starting prior while awaiting individualized records",
        "strength": "subtle",
        "do_not_make_explicit": ["group attribution error", "stereotype", "bias"]
      },
      {
        "instance_id": "pb_01",
        "bias": "Present Bias",
        "decision_point": 2,
        "mechanism": "Choosing the lower-effort immediate path (skip requesting testing) over a modest present cost that would avoid a larger, foreseeable near-term cost (mismatched accommodations)",
        "affected_reasoning_operation": "Trade-off between an immediate scheduling/paperwork cost and a foreseeable future information cost",
        "evidence_available_at_time": [
          "Outdated testing data known to be stale",
          "3-week psychologist backlog",
          "10-day compliance deadline",
          "Existing caseload workload"
        ],
        "required_textual_manifestation": "Coordinator states a preference for the easier immediate option and explicitly defers the reassessment need to a distant future point despite acknowledging it will likely be needed sooner",
        "plausible_nonbias_interpretation": "A legitimate short-term compliance necessity given a genuinely fixed statutory deadline and no faster testing option",
        "strength": "subtle",
        "do_not_make_explicit": ["present bias", "discounting", "bias"]
      },
      {
        "instance_id": "he_01",
        "bias": "Horn Effect",
        "decision_point": 3,
        "mechanism": "One vivid negative behavioral incident colors the overall characterization of unrelated academic and social attributes",
        "affected_reasoning_operation": "Synthesis of mixed evidence into an overall present-levels characterization",
        "evidence_available_at_time": [
          "Single paraprofessional-reported outburst during a transition",
          "Two teacher check-ins describing positive peer interactions",
          "Work samples showing above-grade-level reading"
        ],
        "required_textual_manifestation": "Coordinator's description of the student's academic engagement and social skills becomes generally more negative immediately after recounting the outburst, without citing academic or social evidence that would justify the shift",
        "plausible_nonbias_interpretation": "Reasonable caution about safety-relevant behavior temporarily taking priority in a present-levels narrative",
        "strength": "moderate",
        "do_not_make_explicit": ["horn effect", "halo effect", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control condition."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable in biased condition (no counterfactual requested)",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly 4 decision points present, decision point 4 contains no intended bias instance",
      "Exactly 1 Group attribution error instance placed at decision point 1",
      "Exactly 1 Present Bias instance placed at decision point 2",
      "Exactly 1 Horn Effect instance placed at decision point 3",
      "No bias labels, definitions, or explanations appear in probes or narrative",
      "Each instance has a distinct evidence trace and decision moment",
      "Target word count 1,350 (range 1,215-1,485) achievable given 4 decision points, probe plan, and 3 embedded instances without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Group attribution error",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as generalization from sending-program group identity to individual student prior to individualized data arrival"
      },
      {
        "bias": "Present Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as trading a modest present effort cost for a foreseeable, acknowledged near-term future cost"
      },
      {
        "bias": "Horn Effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a single negative incident coloring unrelated academic/social characterization without supporting evidence"
      }
    ],
    "target_bias_names": [
      "Group attribution error",
      "Present Bias",
      "Horn Effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Group attribution error", "requested_occurrences": 1 },
      { "bias": "Present Bias", "requested_occurrences": 1 },
      { "bias": "Horn Effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "gae_01", "bias": "Group attribution error" },
      { "instance_id": "pb_01", "bias": "Present Bias" },
      { "instance_id": "he_01", "bias": "Horn Effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "gae_01", "bias": "Group attribution error", "decision_point": 1 },
      { "instance_id": "pb_01", "bias": "Present Bias", "decision_point": 2 },
      { "instance_id": "he_01", "bias": "Horn Effect", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "gae_01",
        "bias": "Group attribution error",
        "mechanism": "Generalizing assumed group disposition (sending program population) onto an individual student ahead of individualized evidence",
        "affected_reasoning_operation": "Initial placement inference from group-identifying information",
        "evidence_source": "Transfer summary sheet and prior experience with the sending program, absent full individualized records",
        "distinctiveness_requirement": "Must be the only instance in the interview where a placement or capability judgment is drawn from group/program identity rather than individual data"
      },
      {
        "instance_id": "pb_01",
        "bias": "Present Bias",
        "mechanism": "Overweighting an immediate effort/scheduling cost relative to an acknowledged, larger near-term future cost of delayed information",
        "affected_reasoning_operation": "Cost-benefit trade-off between present effort and future informational adequacy",
        "evidence_source": "Testing backlog, compliance deadline, and caseload workload data",
        "distinctiveness_requirement": "Must be the only instance where a foreseeable future cost is explicitly acknowledged yet discounted in favor of the easier immediate path"
      },
      {
        "instance_id": "he_01",
        "bias": "Horn Effect",
        "mechanism": "A single vivid negative behavioral data point generalizes into an unsupported, broader negative characterization of unrelated attributes",
        "affected_reasoning_operation": "Synthesis of mixed evidence into an overall present-levels narrative",
        "evidence_source": "Paraprofessional's single incident report contrasted with teacher check-ins and academic work samples",
        "distinctiveness_requirement": "Must be the only instance where an isolated negative data point measurably shifts characterization of unrelated (academic/social) attributes without supporting evidence"
      }
    ],
    "intended_strength": [
      { "instance_id": "gae_01", "bias": "Group attribution error", "strength": "subtle" },
      { "instance_id": "pb_01", "bias": "Present Bias", "strength": "subtle" },
      { "instance_id": "he_01", "bias": "Horn Effect", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Biased_3",
    "domain_id": "EI",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1, 2, 3) chosen for best mechanism fit and narrative realism; decision point 4 intentionally left neutral to satisfy the required 4-decision-point structure without adding unrequested bias instances.",
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
          "segment_id": "DP1_INITIAL_PLACEMENT",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "The sending program stood out. In my experience, students transferring from that program often needed a fairly high level of behavioral structure when they first arrived.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gae_01"
          ],
          "ground_truth_rationale": "The coordinator generalized the assumed profile of students from the sending program to this individual before individualized records arrived, matching Group attribution error."
        },
        {
          "segment_id": "DP2_REEVALUATION",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "I was trying to get a compliant interim IEP done without creating another moving part. ... I told myself we could revisit testing at the annual review.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "pb_01"
          ],
          "ground_truth_rationale": "The coordinator chose the easier immediate path despite stale data and an acknowledged foreseeable near-term cost from delayed information, matching Present Bias."
        },
        {
          "segment_id": "DP3_PRESENT_LEVELS",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "that report was vivid because it was the most detailed account of a difficult moment ... I worried that the same difficulty would show up in group work, independent work, and peer situations",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "he_01"
          ],
          "ground_truth_rationale": "A single vivid negative incident generalized into an unsupported broader characterization of unrelated academic and social functioning, matching Horn Effect."
        },
        {
          "segment_id": "DP4_FINAL_PLACEMENT",
          "speaker": "Participant",
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "We documented why the service minutes were temporary and set a review point.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The final service-minutes and LRE decision is described as a documented whole-record judgment with no additional hidden bias instance."
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
    "analysis_scope_note": "Single interview transcript analyzed for cognitive biases in the participant's case-reasoning decisions. No retrieved scientific-paper corpus passages were supplied, so bias labels are drawn from general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "premature closure",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment heuristic", "diagnostic anchoring"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information and to make insufficient adjustments from that anchor when later information becomes available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Early interim placement planning before full records arrived",
      "decision_point_description": "Formation of a preliminary placement lean after receiving the transfer summary but before the full individualized record arrived.",
      "affected_reasoning_operation": "Initial placement recommendation and framing of early planning conversations",
      "bias_specific_mechanism": "The transfer summary, specialized-program label, prior aggression reference, and old FBA/BIP served as an initial anchor. Later records showing a faded BIP and long incident-free period were acknowledged, but the participant reported that the structured-placement option remained the frame already brought into early planning.",
      "manifestation_in_interview": "The participant leaned toward partial pull-out and structured adult support before the full record arrived. After fuller records arrived, he adjusted his thinking but said the structured option was already the frame for early planning conversations.",
      "effect_on_reasoning_or_decision": "The early placement frame was formed around a more supported placement, making full inclusion less central as an initial planning assumption.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I decided to prepare the team for a more supported interim placement rather than begin with full inclusion as the likely recommendation. I did not make a final placement decision that day, but I was leaning toward partial pull-out and more structured adult support.",
          "evidence_explanation": "Shows an early placement lean based on incomplete initial information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Later, the fuller records showed that the BIP had been faded out in the sending setting and that the student had gone roughly nine months without a documented behavioral incident. That was important context, but it arrived after I had already started forming an interim placement view.",
          "evidence_explanation": "Indicates that important contradictory information arrived only after the initial placement view had begun forming."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once the fuller record showed the long incident-free period, I had to adjust my thinking. Still, by then the structured option was already the frame I had brought into our early planning conversations.",
          "evidence_explanation": "Explicitly describes the persistence of the early frame despite later information, consistent with insufficient adjustment from an anchor."
        }
      ],
      "correction_or_counterevidence": "The participant did not make a final placement decision at that time, considered waiting for the full individualized file, recognized the summary was incomplete, and later adjusted his thinking. The initial precaution could also reflect a reasonable safety-oriented default under uncertainty.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "premature closure",
      "alternative_labels": ["need for closure", "premature diagnostic closure"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to accept a conclusion or plan before gathering sufficient current information because of a desire for closure or a settled decision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deferring reevaluation and using old testing and generic accommodations",
      "decision_point_description": "Decision not to seek expedited assessment or a bridge reassessment, and instead to defer reevaluation to the annual review.",
      "affected_reasoning_operation": "Information-gathering and individualization of the interim IEP",
      "bias_specific_mechanism": "The participant recognized that the old testing likely did not match current academic functioning, but avoided additional assessment steps because they felt like they would slow the process. He wanted the team to leave with a settled plan, which truncated further information search before the interim plan was written.",
      "manifestation_in_interview": "Despite knowing the old profile might not fit, the participant used old testing and generic accommodations rather than requesting brief curriculum-based measures, checking for an emergency assessment opening, or building an early reassessment bridge.",
      "effect_on_reasoning_or_decision": "The interim plan used less individualized accommodations, which were later found to be mismatched and required updated testing anyway.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I could have asked the psychologist to see whether there was an emergency opening, requested brief curriculum-based measures, or built a more explicit bridge plan with a reassessment date soon after the interim meeting. That would have meant coordinating another set of forms, getting teacher input quickly, and trying to rearrange a schedule that was already tight.",
          "evidence_explanation": "Shows that alternatives for gathering more current information were considered but set aside."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew there was a good chance the accommodations would need adjustment once the teacher had more academic data. The student’s work samples already suggested the old profile might not fit perfectly. But requesting a special process immediately felt like it would slow everything down, and I wanted the team to leave the meeting with something settled.",
          "evidence_explanation": "Demonstrates a preference for closure and a settled meeting over gathering more individually accurate current data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Frankly, I was trying to get a compliant interim IEP done without creating another moving part. We had ten days, I had a full caseload, and the psychologist had no visible opening. The old data were not ideal, but they were usable enough to put services in place. I told myself we could revisit testing at the annual review.",
          "evidence_explanation": "Indicates that the information search was ended in favor of a workable current plan, with revisit deferred."
        }
      ],
      "correction_or_counterevidence": "There were real structural constraints: a ten-day timeline, a full caseload, and no visible psychologist opening. Deferral may partly reflect reasonable satisficing under workload and time pressure rather than a purely bias-driven process.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judgments of frequency, probability, or general importance are influenced by how easily instances come to mind; vivid, detailed, or emotionally salient events are more mentally available and can be overweighed.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Drafting present levels of performance and behavior-related recommendations",
      "decision_point_description": "Synthesis of positive teacher check-ins, stronger-than-expected reading samples, and one detailed transition outburst into the PLOP.",
      "affected_reasoning_operation": "Assessment of the student's overall behavioral regulation and support needs",
      "bias_specific_mechanism": "A single vivid, detailed negative transition report was more available than the more general positive teacher check-ins and academic work samples. The participant overgeneralized that salient incident to group work, independent work, and peer situations.",
      "manifestation_in_interview": "The participant wrote broad behavioral concern language and described the student as needing substantial adult prompting to remain productively engaged, even though teacher check-ins had been positive and reading work samples were stronger than expected.",
      "effect_on_reasoning_or_decision": "The PLOP overstated behavioral concerns relative to later evidence and underweighted positive classroom and academic information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I had only observed briefly myself, so that report was vivid because it was the most detailed account of a difficult moment.",
          "evidence_explanation": "Indicates that the negative transition incident was especially salient and available in memory."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I wrote that the student’s behavioral regulation could interfere with consistent classroom engagement and peer interactions, and I recommended transition support and check-ins. I also described the student as needing substantial adult prompting to remain productively engaged.",
          "evidence_explanation": "Shows broad conclusions drawn from limited behavioral evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When a student has an outburst during a routine shift in the day, it can affect more than the transition itself. I worried that the same difficulty would show up in group work, independent work, and peer situations, even though the teacher check-ins had been positive.",
          "evidence_explanation": "Demonstrates overgeneralization from one salient episode while positive teacher check-ins were available."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We gathered more feedback, and it consistently showed that the student was engaged academically and got along with peers most of the time. The classroom team still wanted transition supports, which made sense, but my initial wording was broader than the later evidence supported.",
          "evidence_explanation": "Later evidence did not support the broad initial wording, consistent with availability-driven overweighing of the vivid incident."
        }
      ],
      "correction_or_counterevidence": "The transition incident was real, and transition support was later still considered useful. The participant had only limited direct observation and only two teacher check-ins, so some caution was reasonable.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was not available; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No RAG corpus passages were provided, so bias labels and mechanisms rely on general cognitive-science knowledge rather than retrieved scientific support.",
    "The interview is retrospective self-report and may be affected by memory or hindsight; the analysis is based on the participant's described reasoning rather than objective records.",
    "Several decisions occurred under real time, caseload, and information constraints, so some reasoning may reflect reasonable satisficing or precautionary judgment rather than bias.",
    "Findings were kept conservative and mechanism-first; ambiguous or alternative explanations were treated as lowering confidence rather than excluding findings."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Biased_3_Sonar_off",
  "interview_id": "EI_Biased_3",
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
