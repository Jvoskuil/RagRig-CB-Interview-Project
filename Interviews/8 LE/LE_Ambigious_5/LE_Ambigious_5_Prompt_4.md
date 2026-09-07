You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time. This is a voluntary session for internal research on how IA reviews get worked, not a disciplinary matter. You can decline any question. Good with that?

Participant: Sure, that's fine.

Interviewer: Can you tell me your role and experience with complaint reviews?

Participant: Internal Affairs investigator, about five years. I handle use-of-force complaints mostly, some policy violations.

Interviewer: Walk me through the case.

Participant: Traffic stop on Cedar Street, expired registration, ended with a takedown. The driver, Mr. Alvarez, alleges excessive force by Officer Marquez, came away with a wrist fracture. Marquez's report says Alvarez became resistant and pulled his arm away, necessitating the takedown. His partner, Officer Chen, corroborates that. Marquez has nine years in, two prior complaints, both closed unfounded. Alvarez has two prior arrests, one for resisting.

Interviewer: What was your initial read on credibility before you'd seen any footage?

Participant: Genuinely unresolved. Two competing accounts, both plausible on their face, and I didn't have enough yet to prefer one.

Interviewer: What did you do first when you opened the file?

Participant: Requested background on both sides—Alvarez's arrest history and Marquez's disciplinary and training file. Alvarez's record came back within a day, since it's just a records-system pull. Marquez's full file took almost a week because it required a request through the union rep and a records custodian. So for several days I had a fuller picture of one side than the other, which I noted explicitly in my log as a limitation, not a conclusion.

Interviewer: Did that timing gap affect how you approached the rest of the review?

Participant: I tried not to let it. I flagged it as an open item—"complainant background received, officer background pending"—so anyone reading the file later would know the record was uneven at that point, not that I'd already decided anything based on it. Dispatch audio later confirmed it was a routine stop, not flagged high-risk. Medical report confirmed the fracture but didn't tell me which account caused it.

Interviewer: Let's go to the footage.

Participant: Eighteen minutes, with a forty-second gap right after initial contact—his camera didn't reactivate cleanly. Early part is calm, verbal exchange, some de-escalation language from Marquez. Final ninety seconds: Alvarez pulls his arm back, Marquez takes him down.

Interviewer: How did you weigh the earlier footage against that final sequence?

Participant: Honestly, I couldn't fully resolve it on the first pass. The takedown is obviously central since that's where the injury happened, but the gap sits right before the point where things start escalating, and I don't know what's in it. I logged both segments as carrying weight and noted the gap as a limiting factor on any proportionality conclusion I might draw. I didn't want to lock in a read before the consultant weighed in.

Interviewer: What came out of the consultant review?

Participant: A slowed-frame audio pass caught Marquez raising his voice and stepping closer about three minutes before the takedown. The consultant said it's relevant context but not dispositive on its own—doesn't resolve whether the final force was proportionate, just adds texture.

Interviewer: How did that sit with you?

Participant: It complicated things more than it clarified them, if I'm honest. It's the kind of detail that could support either read, depending on what else you believe about the encounter.

Interviewer: Tell me about the case conference.

Participant: Day six. Me, the sergeant, two peer investigators. The sergeant supervised Marquez for three years, said something like "he's generally solid, but I wasn't in the car, so take that for what it's worth." One of the other investigators raised the forty-second gap, said it needed to be addressed before we went further.

Interviewer: How did the room handle that?

Participant: We actually sat with it. There wasn't a quick consensus—two of us thought the gap was potentially significant given the timing relative to the escalation audio, one thought Chen's corroboration and the visible resisting motion carried it regardless. We didn't resolve that disagreement in the room. I logged the dissenting view by name in the case file and noted the preliminary summary as tentative pending the gap issue.

Interviewer: Did the sergeant's history with Marquez shape the discussion?

Participant: It was mentioned, and it's fair to say it's not nothing—people listen when a three-year supervisor speaks. But he qualified it himself, and the discussion kept coming back to what was and wasn't on the tape rather than settling on his character read. I can't say for certain it had zero influence, but I also can't point to a moment where it overrode the evidentiary discussion.

Interviewer: What happened with the eyewitness on day ten?

Participant: A civilian witness we'd had trouble reaching finally called back. She said Marquez was "aggressive from the start," which cuts against how I'd been characterizing the early footage. That came two days after I'd sent the Deputy Chief a preliminary note—explicitly marked tentative, pending the gap and the consultant review.

Interviewer: How did you weigh her statement against what you already had?

Participant: We ran a supplemental check—she had an unobstructed view but was about thirty-five feet out, evening light. I weighed that against the footage on its own terms: is a thirty-five-foot, unobstructed view enough to outweigh eighteen minutes of direct recording? I didn't think it fully was, but I also didn't think it was nothing, especially given the earlier escalation audio the consultant had flagged. I ended up revising the briefing language to reflect that the finding remained more open than the initial note suggested, rather than either adopting her account outright or setting it aside.

Interviewer: Did the fact that you'd already briefed command shape how you handled her statement?

Participant: Command asked whether the preliminary note still held, and I told them it needed updating. It wasn't comfortable revising something I'd already sent up, but the distance and lighting were the actual basis for how much weight I gave her account—not really about protecting what I'd said earlier. I'd rather have gotten it right than tidy.

Interviewer: What's the part of this case you're least confident about?

Participant: The forty-second gap, still. I don't know what happened in it, and I don't know how much that should move the needle either way.

Interviewer: If the eyewitness statement had come in on day two instead of day ten, would your review have gone differently?

Participant: Possibly. I'd have had it earlier alongside the footage instead of layering it onto a note I'd already sent, though I think I'd have weighed it the same way on the merits—distance and view, not timing.

Interviewer: If you'd been the only reviewer, without the case conference, same finding?

Participant: Hard to say. I might have sat with the gap even longer alone. The conference didn't rush me toward a view, but group discussion does move differently than solo review.

Interviewer: Anything you'd sequence differently next time?

Participant: I'd push to get officer background files moving faster at intake, so that gap doesn't sit open as long. Otherwise, I think the uncertainty here was mostly the case itself, not how I worked it.

Interviewer: Appreciate you walking through it.}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      { "bias": "Cognitive dissonance", "occurrences": 0, "mechanism_constraint": "No post-commitment reconciliation of a prior communicated position may be embedded; any evidence revision must be explicitly reasoned on reliability grounds." },
      { "bias": "Recency Effects", "occurrences": 0, "mechanism_constraint": "No disproportionate weighting of the most-recently-reviewed footage segment or most-recently-obtained testimony due to temporal position may be embedded." },
      { "bias": "Groupthink", "occurrences": 0, "mechanism_constraint": "No rapid unchallenged consensus formation with unpursued dissent may be embedded; dissent must be explicitly logged." },
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "occurrences": 0, "mechanism_constraint": "No unequal verification effort applied to the complainant versus the officer may be embedded; any asymmetry must be resource-driven and explicitly flagged as incomplete." }
    ],
    "target_bias_names": [
      "Cognitive dissonance",
      "Recency Effects",
      "Groupthink",
      "Confirmation Bias and Asymmetrical skepticism"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Cognitive dissonance", "requested_occurrences": 0 },
      { "bias": "Recency Effects", "requested_occurrences": 0 },
      { "bias": "Groupthink", "requested_occurrences": 0 },
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "LE_Biased_5",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Ambigious_5",
    "domain_id": "LE",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, which mandates zero intended occurrences of every bias named in the paired manifest regardless of the nonzero counts supplied in the caller's input manifest. The supplied manifest ([Cognitive dissonance:1, Recency Effects:2, Groupthink:1, Confirmation Bias and Asymmetrical skepticism:1]) is treated as identifying the paired target-bias set from LE_Biased_5 for exclusion purposes only, not as an occurrence count to embed.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and role (Internal Affairs Investigator, municipal PD)",
      "Core incident facts (Cedar Street expired-registration stop, takedown, wrist fracture)",
      "All named actors and their prior histories",
      "The 40-second BWC gap",
      "The 14-day deadline and 48-hour briefing window",
      "The day-10 eyewitness statement and 35-foot viewing distance",
      "Four-decision-point structure and approximate word count",
      "Technical vocabulary and difficulty level"
    ],
    "generation_warnings": [
      "The caller's input manifest for this scenario specifies nonzero occurrence counts (1, 2, 1, 1) identical to the paired biased scenario LE_Biased_5, which conflicts with the ambiguous_control condition rule requiring zero intended occurrences of all named target biases. Per the CONDITION RULES, the condition value governs: this specification implements zero intended occurrences for every listed bias and repurposes the supplied manifest solely as the definition of the paired target-bias set to be avoided, not as an embedding instruction. The dataset controller should confirm this interpretation before validation."
    ]
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
