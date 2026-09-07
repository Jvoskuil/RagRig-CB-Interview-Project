You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Before we start, do I have your consent to talk through a past case, keeping identifying details out of it?

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

Participant: I'd have waited for the complete file and done more observation before drafting anything.}}
- Hidden generation specification: {{"hidden_validation_specification": {
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
  }}}
- Validation report: {{VALIDATION_REPORT}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
