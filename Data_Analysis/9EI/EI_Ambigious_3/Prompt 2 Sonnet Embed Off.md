You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Before we start, do I have your consent to talk through a past case, keeping identifying details out of it?

Participant: Yes, that's fine.

Interviewer: Can you describe your role and caseload at the time?

Participant: I was the IEP Coordinator for an elementary building, managing about 42 active IEPs. My job included coordinating interim placements for transfers, writing present levels, tracking related services, and making sure we stayed inside compliance timelines. This case was a mid-year transfer, so we had ten school days to get an interim placement in place.

Interviewer: What was the goal for this student specifically?

Participant: To get a legally sound interim IEP finished quickly, with a placement, present levels, and service minutes that actually reflected the student, not just a generic starting point. The tricky part was that our information came in pieces, and we had real scheduling limits on both testing and staff time.

Interviewer: Tell me what happened, from the transfer notice onward.

Participant: We got notice on a Thursday that the student would start Monday, coming from an out-of-district program that serves students with significant emotional and behavioral needs. The paperwork we had immediately was a transfer summary and a short IEP excerpt. That excerpt referenced a functional behavior assessment and behavior intervention plan written about a year and a half earlier for aggression. The full cumulative file hadn't arrived yet.

I met with the parent, the classroom teacher, and the principal early that first week. The parent said the student had done well recently and was looking forward to a normal schedule. The teacher was willing to include the student but wanted some structure in place before diving into a full schedule, partly because of the FBA/BIP reference and partly, I think, because any new student mid-year creates some uncertainty regardless of background. The principal wanted whatever we set up to be stable, not something we'd be rearranging every other week.

I reached out to the sending program for the rest of the file and contacted our school psychologist about testing, since the existing academic and cognitive testing was over two years old. The psychologist's soonest opening was about three weeks out, past our ten-day deadline. During the first week, the student did fine in most settings, with a paraprofessional supporting transitions. Then, toward the end of the first week, the paraprofessional reported one incident during the shift from recess to writing time. That report became part of what I had to work with when I sat down to write the present levels for the interim meeting, which we held near the end of the ten-day window.

Interviewer: What did you know going in, and what came later?

Participant: Going in, I had the transfer summary, the short IEP excerpt, and the FBA/BIP reference specific to this student. I didn't yet have the full behavioral history, attendance record, or recent progress notes. Later, when the complete file arrived, it showed the plan had been faded out and the student had gone about nine months without a documented incident before the transfer. That context came in after I'd already started shaping my initial thinking about the case.

Interviewer: Let's start with that first decision. Before the full file came in, what did you decide?

Participant: I recommended we build in a short observation window before locking in a fully open interim schedule. I didn't want to finalize a heavily inclusive schedule the very first week without seeing the student in our building first.

Interviewer: What led you there?

Participant: Mainly the student's own FBA/BIP reference. That's documentation specific to this student, not a general assumption. At the same time, that conversation with the teacher and principal also touched on the kind of program the student was coming from, so I can't fully separate how much of my caution was strictly about this student's file versus the general sense that transfers from more structured programs sometimes need an adjustment period. Both things were sitting in my head at the same time.

Interviewer: What alternatives did you weigh?

Participant: Either flag the case for a brief observation period, or move straight into a full-inclusion interim schedule and only add supports if problems came up. I went with the observation window because it felt like the safer starting point given what we knew, even though I recognize a different reading is that I'd have leaned that way for any transfer with that program history in the file, individual documentation or not.

Interviewer: What would have made you comfortable skipping that step?

Participant: If I'd had the full file up front showing the long incident-free stretch, I probably would have gone straight into a fuller schedule from day one.

Interviewer: Second decision point: the reevaluation question.

Participant: Right. The existing testing was old, but the psychologist had no opening inside our ten-day window. I decided to write the interim IEP from the existing data and set a specific check-in date a few weeks out to revisit accommodations once we had more classroom information.

Interviewer: Why that option over pushing for an expedited slot?

Participant: There genuinely wasn't a faster testing option available, so using current data with a scheduled follow-up seemed reasonable. I'll admit I'm not entirely sure whether I'd have pushed harder for an earlier slot if one had existed, or whether the follow-up date was just a comfortable way to move forward without more phone calls that week. Both explanations feel plausible to me looking back.

Interviewer: What happened with that plan?

Participant: The scheduled check-in caught a mismatch in the accommodations a few weeks later, which is part of why we'd built the follow-up in to begin with.

Interviewer: Third decision point, the present levels write-up. What did you have to work with?

Participant: The paraprofessional's report of one transition incident, two teacher check-ins describing good peer interactions, and reading work samples above grade level. I'd only briefly observed the classroom myself.

Interviewer: How did you write it?

Participant: I included the transition incident specifically in the context of transitions, and separately described the peer interactions and reading performance as strengths. I tried not to let the incident bleed into how I described the rest of the day.

Interviewer: Do you think the tone came out even-handed?

Participant: Mostly, yes. Though rereading it later, there might be a slightly more cautious note running through the whole thing than the data alone would demand. I honestly can't tell if that's from the incident specifically or just how I write present levels in general when there's any behavioral history in the file.

Interviewer: Final decision point, the placement and service minutes.

Participant: By the meeting, I had the fuller record, the check-in schedule, the present levels, and input from the parent and teacher. I proposed partial pull-out time for transition support and writing organization, with general education for the rest of the day. The parent preferred keeping the student with peers as much as possible, which fit with what the teacher could support.

Interviewer: How was that decision reached?

Participant: It came from weighing the record as a whole, not any single piece. The parent asked for a follow-up review in six weeks, which we agreed to.

Interviewer: If the psychologist had had an immediate opening, would the reassessment decision have gone differently?

Participant: Probably. I'd have likely requested it right away rather than leaning on the older data with a later check-in.

Interviewer: If the paraprofessional's report hadn't come in, would the present levels have read differently?

Participant: Maybe slightly less cautious in tone, though I think the transition supports would still have come up given the program history in the file.

Interviewer: And with a longer compliance timeline?

Participant: I'd have waited for the complete file and done more observation before drafting anything.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "EI_Ambigious_3",
    "domain_id": "EI",
    "domain": "Education and instructional work",
    "role": "Special Education Caseworker / IEP Coordinator",
    "condition": "ambiguous_control",
    "generation_specification": {
      "scenario_title_internal": "Interim Placement for a Mid-Year IEP Transfer (Ambiguous Control)",
      "scenario_summary_internal": "An IEP Coordinator processes a mid-year transfer student arriving from an out-of-district specialized program, completing an interim placement within a 10-school-day compliance window. The reasoning at each decision point is genuinely underdetermined: caution, deferral, and cautious wording are each supported by plausible non-bias justifications (individualized documentation, fixed scheduling constraints, safety-relevant uncertainty) rather than by group-based generalization, short-term discounting, or disproportionate negative colorization. No named bias is intentionally instantiated.",
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
            "The student's own prior IEP excerpt documents an individualized FBA/BIP written 18 months ago for aggression",
            "Full cumulative file has not yet arrived from the sending program",
            "Coordinator has handled several prior transfers, some from this program and some from others, with mixed outcomes"
          ],
          "new_information_after_decision": [
            "Full records arrive later showing the BIP was successfully faded out and the student had 9 incident-free months before transfer"
          ],
          "alternatives": [
            "Flag the case for additional behavioral observation before finalizing an inclusion-heavy interim schedule, citing the student's own documented history",
            "Proceed directly toward a full-inclusion interim schedule and revisit supports only if new concerns emerge"
          ],
          "intended_action": "Coordinator recommends building in a short observation period before finalizing the interim schedule, citing the student's own prior FBA/BIP documentation; it remains genuinely unclear from the record whether this caution is anchored to the individual student's own file or is generally influenced by the reputation of the sending program, since both were part of the same intake conversation."
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
            "Weeks later, the classroom teacher reports some accommodations need adjustment; a scheduled check-in already anticipated this possibility"
          ],
          "alternatives": [
            "Request an expedited or partial testing slot and build a short bridge plan with a defined near-term follow-up",
            "Use existing data for the interim IEP and schedule a specific, dated check-in shortly after the meeting to reassess accommodations"
          ],
          "intended_action": "Coordinator uses existing testing data for the interim IEP but schedules a concrete, dated follow-up review within a few weeks; it is genuinely ambiguous whether the choice reflects a considered judgment that the psychologist's backlog made expedited testing infeasible, or a general tendency to prefer the more immediately available option, since both interpretations fit the visible facts equally well."
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
            "Additional peer and teacher feedback collected afterward continues to show strong academic engagement, roughly consistent with the balanced present-levels description"
          ],
          "alternatives": [
            "Write present levels giving comparable weight to the transition incident, the positive peer reports, and the academic work samples",
            "Emphasize the transition incident more heavily than the other three data points when describing overall functioning"
          ],
          "intended_action": "Coordinator drafts present levels that mention the transition incident alongside the academic and social strengths, using cautious language about transitions specifically without extending that caution into blanket statements about academic or social functioning; whether the resulting tone still reads as slightly more guarded than the underlying data strictly requires remains genuinely open to interpretation."
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
          "intended_action": "Coordinator finalizes service minutes and LRE recommendation using a documented rationale drawn from the assembled record; this decision point is intentionally left evidence-balanced and is not a site of any intended ambiguity manipulation beyond ordinary domain judgment."
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
          "If the student had transferred from a different, less specialized program, would your approach have been the same?",
          "If the psychologist had immediate testing availability, would you have made the same choice about reassessment?",
          "If the paraprofessional's report hadn't come in, how might the present levels have read differently?",
          "If the compliance timeline had been longer, what would you have done differently?"
        ]
      },
      "occurrence_embedding_plan_internal": [],
      "control_specification": {
        "paired_scenario_id": "EI_Biased_3",
        "features_to_match": [
          "Same domain vocabulary (interim placement, PLOP, FBA/BIP, LRE, service minutes, compliance timeline, reevaluation)",
          "Same stakeholders and staging (parent, teacher, paraprofessional, psychologist, principal, sending program liaison)",
          "Same four-decision-point structure and narrative sequence (records/history review, reassessment scheduling, incident interpretation, final placement)",
          "Same constraints (10-day timeline, 42-student caseload, 3-week psychologist backlog)",
          "Same target word count and difficulty level",
          "Same emotional tone: professional, time-pressured, cautious"
        ],
        "features_to_remove_or_change": [
          "Remove framing that ties the interim lean to the sending program's general population rather than the student's own documented file",
          "Remove explicit acknowledgment that a future cost is being knowingly discounted in favor of an easier immediate option",
          "Remove disproportionate extension of a single negative incident into unrelated academic/social characterizations",
          "Add a concrete, dated follow-up mechanism at decision point 2 to keep the deferral defensible rather than clearly discount-driven",
          "Balance the present-levels narrative at decision point 3 so cautious language is scoped to the transition context rather than generalized"
        ],
        "ambiguity_boundary": "Each of the first three decision points must remain genuinely undecidable between a bias-consistent reading and a legitimate, individualized, resource-constrained reading: (1) the observation-period recommendation is grounded in the student's own FBA/BIP record, but the intake conversation also surfaces program reputation, so the causal driver of caution is not textually resolvable; (2) the reassessment deferral is paired with a concrete dated check-in, making it consistent with reasonable compliance-driven sequencing rather than clearly short-term discounting; (3) the present-levels caution is explicitly scoped to transitions rather than generalized, but a reader could still perceive a mild tonal shift, keeping the degree of generalization ambiguous rather than absent or blatant. No sentence may contain a clean, unambiguous tell that isolates a single causal mechanism as the sole explanation."
      },
      "counterfactual_specification": {
        "causal_variable": "Not applicable in ambiguous_control condition (no counterfactual requested)",
        "original_state": null,
        "counterfactual_state": null,
        "variables_to_hold_constant": [],
        "expected_causal_difference": null,
        "causal_test_question": null
      },
      "generation_checks": [
        "Exactly 4 decision points present, matching the paired biased scenario's structure",
        "No named bias is intentionally instantiated at any decision point",
        "Each of decision points 1-3 supports at least two plausible readings (individualized/legitimate vs. group- or discount- or generalization-consistent) without resolving which applies",
        "Decision point 4 remains a balanced, evidence-driven judgment with no ambiguity manipulation",
        "No bias labels, definitions, or explanations appear in probes or narrative",
        "Vocabulary, stakeholders, constraints, and word count match the paired biased scenario EI_Biased_3",
        "Target word count 1,350 (range 1,215-1,485) achievable given 4 decision points, probe plan, and ambiguity design without repetitive exposition"
      ]
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "ambiguous_control",
      "exact_occurrence_manifest": [
        {
          "bias": "Group attribution error",
          "occurrences": 0,
          "mechanism_constraint": "Control implementation: zero intended instances; decision point 1 must remain genuinely ambiguous between individualized and group-based causal readings without resolving toward either."
        },
        {
          "bias": "Present Bias",
          "occurrences": 0,
          "mechanism_constraint": "Control implementation: zero intended instances; decision point 2 must include a dated follow-up mechanism that keeps the deferral defensible on legitimate grounds."
        },
        {
          "bias": "Horn Effect",
          "occurrences": 0,
          "mechanism_constraint": "Control implementation: zero intended instances; decision point 3 caution must be scoped to the transition context rather than generalized to unrelated attributes."
        }
      ],
      "target_bias_names": [
        "Group attribution error",
        "Present Bias",
        "Horn Effect"
      ],
      "requested_occurrence_count_for_each_bias": [
        { "bias": "Group attribution error", "requested_occurrences": 0 },
        { "bias": "Present Bias", "requested_occurrences": 0 },
        { "bias": "Horn Effect", "requested_occurrences": 0 }
      ],
      "planned_instance_ids": [],
      "intended_decision_points": [],
      "intended_mechanisms": [],
      "intended_strength": [],
      "paired_scenario_id": "EI_Biased_3",
      "counterfactual_variable": {
        "name": null,
        "original_state": null,
        "changed_state": null,
        "variables_to_hold_constant": []
      },
      "scenario_id": "EI_Ambigious_3",
      "domain_id": "EI",
      "total_requested_occurrences": 0,
      "total_planned_occurrences": 0,
      "allocation_rule_used": "Not applicable: ambiguous_control condition requires zero intended bias instances for all target biases inherited from the paired scenario's manifest; no decision-point allocation of bias instances was performed. Ambiguity was instead distributed across decision points 1-3 by design, each engineered to support at least two plausible causal readings without resolving toward a bias-consistent interpretation.",
      "control_zero_bias_requirement": true,
      "variables_to_hold_constant": [
        "Domain vocabulary and technical terminology",
        "Stakeholder roster and roles",
        "Four-decision-point narrative structure and sequence",
        "Operational constraints (10-day timeline, caseload size, psychologist backlog)",
        "Target word count and difficulty level",
        "Emotional tone and time pressure"
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
        "segment_id": "DP1_INITIAL_PLACEMENT",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "I recommended we build in a short observation window before locking in a fully open interim schedule. Mainly the student's own FBA/BIP reference; I can't fully separate how much of my caution was strictly about this student's file versus the general sense that transfers from more structured programs sometimes need an adjustment period.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The exhaustive manifest assigns zero Group attribution error instances. Individualized FBA/BIP documentation and incomplete records provide a plausible non-bias basis, while the interview leaves category influence unresolved."
      },
      {
        "segment_id": "DP2_REEVALUATION",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "The psychologist had no opening inside our ten-day window. I decided to write the interim IEP from existing data and set a specific check-in date a few weeks out to revisit accommodations.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The exhaustive manifest assigns zero Present Bias instances. A fixed testing backlog, compliance deadline, and concrete follow-up support legitimate sequencing."
      },
      {
        "segment_id": "DP3_PRESENT_LEVELS",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "I included the transition incident specifically in the context of transitions, and separately described peer interactions and reading performance as strengths. Later, there might be a slightly more cautious note running through the whole thing than the data alone would demand.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The exhaustive manifest assigns zero Horn Effect instances. The incident is expressly contextualized and separated from strengths; uncertainty about a broader tone does not resolve toward a spillover distortion."
      },
      {
        "segment_id": "DP4_FINAL_PLACEMENT",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "It came from weighing the record as a whole, not any single piece. The parent asked for a follow-up review in six weeks, which we agreed to.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "No planned instance appears at the final placement decision; the participant describes a whole-record judgment with stakeholder input."
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
    "analysis_scope_note": "Only the CTA transcript was analyzed. No retrieved corpus passages were supplied, so bias labels and definitions reflect general cognitive-science knowledge rather than retrieved evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive heuristic in which judgments, especially judgments of risk or probability, are disproportionately influenced by information that is salient, emotionally charged, or easily brought to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interim placement schedule: observation window versus full-inclusion schedule",
      "decision_point_description": "Deciding whether to recommend a brief observation window before full inclusion or to move directly into a fuller interim schedule before the complete file arrived.",
      "affected_reasoning_operation": "Risk and safety judgment about the student's likely adjustment and need for initial structure",
      "bias_specific_mechanism": "The participant's caution was shaped by the most salient and easily available negative information: a years-old FBA/BIP reference for aggression and the sending program's behavioral reputation. These available risk cues appear to have outweighed the parent's current low-incident report in the early scheduling judgment.",
      "manifestation_in_interview": "The participant recommended a short observation window despite the parent saying the student had been doing well, and acknowledged that the old FBA/BIP reference and the program-history generalization were both mentally prominent at the same time.",
      "effect_on_reasoning_or_decision": "The initial interim schedule was shifted toward caution and structure rather than full inclusion; the participant stated that with the full record showing a long incident-free stretch, he probably would have moved directly into a fuller schedule.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The paperwork we had immediately was a transfer summary and a short IEP excerpt. That excerpt referenced a functional behavior assessment and behavior intervention plan written about a year and a half earlier for aggression. The full cumulative file hadn't arrived yet.",
          "evidence_explanation": "This establishes that the most negatively salient available information was an old FBA/BIP for aggression, which framed the initial risk judgment before fuller current information was available."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mainly the student's own FBA/BIP reference. That's documentation specific to this student, not a general assumption. At the same time, that conversation with the teacher and principal also touched on the kind of program the student was coming from, so I can't fully separate how much of my caution was strictly about this student's file versus the general sense that transfers from more structured programs sometimes need an adjustment period. Both things were sitting in my head at the same time.",
          "evidence_explanation": "The participant identifies two salient risk-related considerations that were mentally available during the decision, illustrating how easily recalled negative information about the student and program background influenced his caution."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'd had the full file up front showing the long incident-free stretch, I probably would have gone straight into a fuller schedule from day one.",
          "evidence_explanation": "This counterfactual indicates that the early restrictive judgment was driven by the available negative history rather than by a stable, evidence-based conclusion about the student, and that it would have been revised with fuller current information."
        }
      ],
      "correction_or_counterevidence": "A plausible non-bias explanation is that the observation window was a professionally reasonable precaution given incomplete information and a documented behavioral history. The participant also explicitly described the FBA/BIP as student-specific documentation. No explicit debiasing occurred at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were available in this analysis. The label 'availability heuristic' is applied from general cognitive-science knowledge rather than from retrieval.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "status quo bias",
      "alternative_labels": [
        "default bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Reevaluation timing: using existing data with a later check-in versus seeking expedited testing",
      "supporting_interview_quote": "I'll admit I'm not entirely sure whether I'd have pushed harder for an earlier slot if one had existed, or whether the follow-up date was just a comfortable way to move forward without more phone calls that week. Both explanations feel plausible to me looking back.",
      "plausible_mechanism": "The participant may have accepted the existing plan of using old data plus a later check-in partly to avoid additional effort or disruption, consistent with status quo or default bias.",
      "why_not_identified": "The transcript states that no faster testing option was available, so the decision may be fully explained by an external resource constraint. The participant's alternative explanation is retrospective speculation and is not affirmatively connected to the actual decision mechanism."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "negativity bias",
      "alternative_labels": [
        "horn effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Writing present levels for the interim IEP",
      "supporting_interview_quote": "Though rereading it later, there might be a slightly more cautious note running through the whole thing than the data alone would demand. I honestly can't tell if that's from the incident specifically or just how I write present levels in general when there’s any behavioral history in the file.",
      "plausible_mechanism": "A single negative transition incident may have broadened into a generally cautious tone across the present-levels write-up, giving negative information disproportionate influence over the positive peer and reading observations.",
      "why_not_identified": "The participant's language is explicitly tentative and he cannot distinguish this from his general professional writing style. There is insufficient affirmative evidence that the final present-levels description was actually distorted by the incident."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied, so scientific support for labels could not be drawn from retrieval.",
    "The transcript is retrospective self-report and may be filtered by memory, self-presentation, or hindsight.",
    "Some potentially bias-relevant statements are explicitly uncertain, limiting confidence in mechanism attribution."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Ambigious_3_Sonnet_off",
  "interview_id": "EI_Ambigious_3",
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
