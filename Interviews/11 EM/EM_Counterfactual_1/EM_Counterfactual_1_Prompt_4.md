You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Just to confirm — you're okay with us discussing this incident in detail for training-development purposes, and we can pause anytime?

Participant: Yes, that's fine. Happy to go through it.

Interviewer: Can you tell me your role and what you were supposed to be doing that day?

Participant: I'm a Training Officer with the county EM office. That day I was controlling a full-scale exercise — a shelter-in-place and evacuation drill at our EOC and one of our public shelters. My job was running injects and evaluating the shelter and liaison teams.

Interviewer: What actually happened?

Participant: About ninety minutes in, we got a scripted comms-disruption inject. Almost right after, a real weather alert came through — a fast-moving winter storm, faster than what we'd built the drill around. A couple of field reports came in that I couldn't immediately place as scripted or real. So I paused the exercise and checked actual weather data before doing anything else. That confirmed it — a real tower failure, and roads closing faster than forecast.

Interviewer: What led you to stop and verify rather than continue running the drill?

Participant: The timing didn't fit our script, and the reports didn't match the inject list. I've run enough of these to recognize when something's off-script, and I didn't want to keep feeding scenario content into what might already be real.

Interviewer: What happened next?

Participant: Shortly after, two liaison officers arrived for the scheduled shift handoff at the shelter. Neither had worked that specific site before. This time, though, I actually had a bit of breathing room — maybe twenty-five minutes before I needed to turn to the transportation side, since the bus situation hadn't come up yet. So I sat with them, gave them the rundown — told them to run the usual Zone C protocol, muster at the standard point, same as always — and then went to check on road conditions.

Interviewer: What happened after that handoff?

Participant: About forty minutes later, during a headcount, we found a group had been sent to the old west muster point — we'd relocated that about a year ago. Separately, a volunteer coordinator asked me directly what "Zone C protocol" even referred to. So the same kind of mix-up happened, even though I'd had more time with them than I usually get in situations like this.

Interviewer: Let's go through this step by step. First, the decision to pause the exercise — what did you actually have in front of you at that moment?

Participant: The scripted inject text, the live weather alert, and two ambiguous field reports. No confirmation yet of a real failure — that came after.

Interviewer: What alternatives did you weigh?

Participant: Keep running the drill and treat it as scripted, or stop and verify against real data. I verified. Worst case, I lose a few minutes of drill time; best case, I catch a real problem early.

Interviewer: Now the liaison handoff. You said you had more time than usual there. What did you know about these two officers going in?

Participant: I knew they were new to this shelter specifically. I didn't ask about their broader background — I assumed liaison officers generally pick up our zone conventions fast, since it's not unusual across our sites.

Interviewer: You had roughly twenty-five minutes and no immediate competing task. What did you do with that time?

Participant: Some of it went to double-checking the transportation numbers with the section chief, even though I didn't strictly need to yet. With the liaisons, I gave them the same rundown I always give — "usual Zone C protocol," "standard muster point." I didn't really stretch it out into something longer.

Interviewer: Given that you weren't rushed, what made you choose the short version anyway?

Participant: Honestly, it didn't occur to me that it needed to be longer. Those terms are just how I refer to things day to day — they don't register as shorthand to me, they register as the actual names. Having the extra time didn't change how I framed it, because I wasn't treating it as an abbreviated version of anything.

Interviewer: Did you check what they already knew before briefing them?

Participant: No. I could have asked directly — "have you worked this layout before, do you know where the current muster point is" — and I had time to do that. I just didn't think to.

Interviewer: What would have changed your approach there?

Participant: If either of them had flagged that they were unfamiliar, I'd have walked them through it properly. Neither volunteered that, and I didn't ask.

Interviewer: Let's move to the transportation decision. What was the situation?

Participant: Two buses, three sites requesting transport, and the section chief flagged fuel and driver-hour limits. One sector's roads were closing faster than the others per the county updates.

Interviewer: What options did you consider?

Participant: Split the buses evenly across all three, or prioritize the fastest-closing sector first. I prioritized that sector.

Interviewer: Why that option?

Participant: Splitting evenly felt fair on paper, but it risked stranding people at the site about to become unreachable. Prioritizing by closure risk meant a longer wait elsewhere, but nobody got cut off entirely.

Interviewer: How did that play out?

Participant: The prioritized site cleared in time. One other site had a longer wait — inconvenient, but they got transport once the first run finished, no injuries.

Interviewer: Last decision point — handing off to the Incident Commander. What was competing for your attention?

Participant: The IC arrived to take over the real incident, the exercise evaluators still expected a formal debrief, and parts of the shelter were still running on the arrangement from the earlier handoff.

Interviewer: What did you consider doing?

Participant: Run the debrief and real command informally in parallel, or fully suspend the exercise and do a proper handoff. I suspended it and gave the IC a written status briefing instead of just talking him through it.

Interviewer: Why written, given you had some time pressure again at that point?

Participant: Verbal is faster, but I've seen details get lost that way, especially with comms already degraded. Writing it down gave him something to check against rather than relying on what he remembered hearing.

Interviewer: Did the earlier muster-point mix-up influence that choice?

Participant: A bit, in hindsight. I think I was more deliberate about not leaving room for gaps after seeing what happened with the liaison briefing.

Interviewer: Given that you actually had time available during that briefing, what do you think would have changed if you'd used it differently — say, walking through the zone map from scratch?

Participant: Probably would have caught the muster point issue immediately. It wasn't that I didn't have the minutes for it. I just didn't reframe the conversation as something that needed more than the usual rundown.

Interviewer: If the storm had hit an hour later, would your resource decisions have changed?

Participant: The bus prioritization logic would hold regardless. It might have given me even more slack before the transportation piece, but based on what happened here, I'm not sure that alone would've changed how I briefed the liaisons.

Interviewer: What would you tell a less experienced officer in a similar spot?

Participant: Don't assume the title comes with the knowledge. It's tempting to think "liaison officer" means someone already knows your terms, but that depends entirely on which site they've actually worked. Time isn't always the reason things get skipped — sometimes you just don't think to check.}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Curse of Knowledge",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Curse of Knowledge"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Curse of Knowledge",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "mechanism": "Expert briefer assumes newly rotated, less-informed liaison officers share the same tacit facility-specific knowledge and terminology, resulting in an under-explained shift-handoff briefing, persisting even when time pressure is removed as a confound.",
        "affected_reasoning_operation": "Content selection and calibration during a briefing when time is not a binding constraint",
        "evidence_source": "Training Officer's stated rationale for briefing content and use of available time, contrasted with liaison officers' subsequent confusion/misdirection",
        "distinctiveness_requirement": "Must be distinguishable from the base scenario's time-pressure-confounded instance by explicitly showing the same abbreviated briefing occurs even with ample uncommitted time, isolating the knowledge-assumption mechanism from a time-economization explanation."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ck_01",
        "bias": "Curse of Knowledge",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": "EM_Biased_1",
    "counterfactual_variable": {
      "name": "Amount of time available for the shift-handoff briefing before the next competing task",
      "original_state": "Approximately ten minutes available, under acute time pressure from the pending transportation task",
      "changed_state": "Approximately twenty-five minutes available, with no immediate competing task",
      "variables_to_hold_constant": [
        "Storm timeline and severity",
        "Liaison officers' identity, role, and experience level",
        "Transportation resource constraints and phase 3 decision reasoning",
        "Phase 1 and phase 4 decisions and reasoning",
        "Shorthand terminology used and downstream misdirection consequence"
      ]
    },
    "scenario_id": "EM_Counterfactual_1",
    "domain_id": "EM",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence retained at decision point 2 (shift-handoff briefing), matching the base scenario's assignment, since the counterfactual condition requires implementing the identical manifest while varying exactly one causal factor (available briefing time) rather than the bias's decision-point placement.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Storm timeline and severity",
      "Liaison officers' identity, role, and experience level",
      "Transportation resource constraints and phase 3 decision reasoning",
      "Phase 1 and phase 4 decisions and reasoning",
      "Shorthand terminology used and downstream misdirection consequence"
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
