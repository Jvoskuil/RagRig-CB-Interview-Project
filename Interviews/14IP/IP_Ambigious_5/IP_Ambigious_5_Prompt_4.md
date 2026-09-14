You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for sitting down with me. This is a cognitive task analysis interview — I want to understand how you actually worked through a specific production problem, including what you knew at each point and why you chose what you did. There are no right answers I'm grading you against. Okay to start?

Participant: Sure, no problem. I've got a decent example — the Line 3 flash issue before our Meridian shipment a few weeks back.

Interviewer: Great, let's use that. Can you describe the overall situation and what you were trying to accomplish?

Participant: We had a 72-hour window to ship a Meridian order off Line 3 — interior clips, tight tolerances. Partway through a night shift, scrap jumped from about 1.8% to 6.4%, mostly flash, some short shots. My goal was to get us back under 2% without missing the ship date and without a full shutdown, since that needs VP sign-off and we didn't have time for that process anyway.

Interviewer: What were the first signs something was wrong?

Participant: Quality flagged the scrap numbers, and the SPC chart showed cavity pressure drifting starting mid-shift. That drift range is one of those things that's ambiguous on its own — we've seen similar magnitudes tied to humidity issues before, but also to early tooling wear. So it didn't point cleanly in one direction.

Interviewer: Did anything from past experience come to mind?

Participant: We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying. But we'd since put in a new dehumidifier, so I honestly wasn't sure how comparable that case even was anymore. It could easily have been a red herring.

Interviewer: So what did you do with that uncertainty?

Participant: I didn't want to bet the sequencing on either guess, so I had two techs pull humidity logs and tooling wear data at the same time — they'd take roughly the same amount of time either way, so there wasn't a good reason to prioritize one over the other.

Interviewer: What came back?

Participant: Humidity logs were normal. Tooling data showed moderate wear had built up. So the wear side turned out to be the real thread, but I couldn't have known that going in — it really could have gone either way based on what we had.

Interviewer: Let's reconstruct the next couple of days. What happened once wear was confirmed?

Participant: That's decision point two. Wear was real, but the reading was right on the line — borderline between our threshold for a simple hold-pressure adjustment and the threshold for a full insert swap. My tooling lead and one of the shift supervisors actually disagreed about which side of that line we were on.

Interviewer: How did you resolve that?

Participant: We had a press-down window open right then, shared with two other product runs, and it wouldn't come around again for five days. A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap.

Interviewer: Did that resolve things?

Participant: Partially. Scrap improved but didn't fully get back to baseline. Could mean the wear diagnosis was right but incomplete, or that there's a second factor we haven't isolated. I genuinely don't know which.

Interviewer: Take me to the third point — the call with the sister plant.

Participant: Right, this was day two, when my quality engineer was out sick, so I had less support than usual. I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match.

Interviewer: What did you know about how well it would apply to your line specifically?

Participant: My engineer had partially validated it against our resin lot before going out sick, but hadn't finished testing it against our specific cavity geometry. Corporate quality said results across the network looked promising but not conclusive yet.

Interviewer: So what did you decide?

Participant: I adopted it based on the partial validation we already had. I'll be honest, it could reasonably have gone the other way — waiting for full geometry testing, or rolling out a more conservative version first. I weighed the incomplete testing against the shipment clock and made a call I can defend, but I wouldn't say it was obviously the right one.

Interviewer: What happened after?

Participant: Short-term, flash defects dropped. Then two shifts later we got a new warping issue on some parts, cause not yet clear. Might be related to the cooling change, might not.

Interviewer: Last decision point — the rollout call.

Participant: Right. By the final stretch, our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability. Corporate quality asked if we should roll the fix to Lines 4 and 6.

Interviewer: What made that decision hard?

Participant: Lines 4 and 6 have different tooling age profiles than Line 3, so I couldn't just assume the fix would transfer cleanly either way. Given the mixed trend and those differences, I didn't think a full rollout to both lines was justified yet, but sitting on it entirely wasn't really an option with the deadline bearing down.

Interviewer: So what did you approve?

Participant: A limited pilot on one line with extra monitoring, rather than pushing it to both. I said as much to corporate — that the data didn't support going all-in yet, but doing nothing wasn't realistic either.

Interviewer: What came of the pilot?

Participant: Initial improvement, then a new tooling alarm showed up on that line that we hadn't seen before. A fuller week-long review later suggested the underlying wear issue was only partly addressed.

Interviewer: What information would have made these calls easier?

Participant: Faster wear measurements at decision two, and full geometry validation before decision three. Those were the two spots where I felt like I was deciding on incomplete information out of necessity, not preference.

Interviewer: If the last shift's numbers had come in worse instead of better, would decision four have gone differently?

Participant: Possibly less generous — maybe I'd have held off on even the pilot. But given how mixed the broader trend already was, I think I was already treating that last shift as one data point, not the whole answer.

Interviewer: Anything you'd do differently if this happened again?

Participant: Build in a standing arrangement for a second wear reading that doesn't cost us the press-down window, and push corporate for full geometry validation timelines before protocols spread across plants. Otherwise, honestly, most of these calls I'd probably make the same way again given the same constraints.

Interviewer: This has been really helpful, thank you.

Participant: Anytime.
}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Bandwagon effect",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; sister-plant adoption rate must not be the stated primary justification for the protocol-adoption decision."
      },
      {
        "bias": "Recency effect",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; the most recent shift's data must not be disproportionately weighted over the full multi-day trend in the rollout decision."
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; no unqualified certainty claim about full root-cause resolution may be made at the rollout decision."
      },
      {
        "bias": "Availability Heuristic",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; the Line 5 vivid-failure narrative must not be the stated primary justification for the fix-selection decision."
      },
      {
        "bias": "Anchoring Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not be instantiated; the six-month-old prior incident must not fix the initial diagnostic hypothesis or determine inquiry order."
      }
    ],
    "target_bias_names": [
      "Bandwagon effect",
      "Recency effect",
      "Overconfidence Bias",
      "Availability Heuristic",
      "Anchoring Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bandwagon effect", "requested_occurrences": 0 },
      { "bias": "Recency effect", "requested_occurrences": 0 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 0 },
      { "bias": "Availability Heuristic", "requested_occurrences": 0 },
      { "bias": "Anchoring Bias", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IP_Biased_5",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Ambigious_5",
    "domain_id": "IP",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; this is a zero-instance ambiguous control. All four decision points are constructed with genuinely underdetermined evidence (parallel-checking under equal plausibility, disputed borderline wear readings, partial cross-geometry validation, and mixed multi-day trends) so that reasonable non-biased judgment remains plausible throughout, without instantiating any of the five named target biases.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Operational objective (restore scrap rate under 2% before Meridian shipment)",
      "Setting, stakeholders, and organizational constraints",
      "Sequence and narrative role of the four decision points",
      "Technical vocabulary and domain terminology",
      "Overall difficulty, time pressure, and emotional tone",
      "Probe structure and coverage areas"
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
