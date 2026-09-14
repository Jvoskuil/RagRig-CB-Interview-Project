You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary cognitive task analysis, not an evaluation of your conduct — I'm interested in how you actually thought through the decisions, not whether they were right. Can you tell me your role on this operation?

Participant: Sure. I was the troop commander — overall lead for the assault force, responsible for the go/no-go call, movement decisions, and the breach plan. I had a partnered host-nation commando element attached for this one too.

Interviewer: Good. Let's start broad — walk me through the mission from tasking to your final report.

Participant: We got tasked against a facilitator, code name Zaytun, believed to be co-located with a weapons cache in a compound out in a valley we'd worked before. We had about six hours from tasking to launch, which is tight but not unusual. SIGINT had a phone associated with his network pinging inside the compound two nights before. We planned a foot infil from an offset LZ, about forty-five minutes in, breach, clear, exploit, exfil by helicopter. We'd hit that valley twice before with good results — both times we got confirmed HVTs with almost no collateral issues, so there was a comfort level with the terrain and the pattern.

Interviewer: What information did you have going into the launch decision specifically?

Participant: The SIGINT hit, which the analyst flagged as moderate confidence, not high — he was clear about that. We also had a note from our host-nation liaison that the compound was a known family residence, kids present during the day. That came in maybe two hours before the brief. And obviously the track record from the last two ops in that valley.

Interviewer: How did you weigh the liaison's report against the SIGINT?

Participant: Honestly, it didn't move the needle much for me. The SIGINT was the thing that put the target in that building, and the two prior ops had built a lot of confidence that when we get a hit like that in that valley, it pans out. The family-residence note felt like background texture rather than something that should change the plan — it wasn't tied to a specific threat, more of a general caution. I didn't feel like I needed a specific reason to set it aside, it just didn't carry the same weight as the geolocation.

Interviewer: What other options did you consider at that point?

Participant: Really it came down to launch or delay twenty-four hours for another collection pass. Delaying risked losing the target if he moved. There was technically a lower-signature surveillance-only option on paper — the host-nation element had eyes-capable personnel and our supporting ISR asset could have sustained a watch, so it wasn't off the table for lack of means. But that's not really how we use this troop — we're not built for that mission set, and when a tasking like this comes in, the room just defaults to figuring out how to assault it, so the surveillance option didn't get serious airtime.

Interviewer: Let's move to the infiltration route. What were you working with?

Participant: The route crossed a wadi that, for me personally, is loaded — we took a hard contact there about eight months earlier, sharp firefight, guys got hurt. There was a slower alternate route that avoided it. But we'd also had three straight quiet insertions through that general area over the past couple months.

Interviewer: How did those two things — the old firefight and the recent quiet crossings — factor into your choice?

Participant: Both were in my head, if I'm honest. The firefight sticks with you in a way that current reporting doesn't always match — when I pictured that wadi, I pictured tracer fire, not a calm crossing, even though nothing in the current threat picture pointed to that. At the same time, we'd had three clean runs through there recently, and there's a pull toward thinking the run continues, or conversely that we were "due." I went with the wadi route mostly on that combination rather than waiting on updated route-specific intel.

Interviewer: Did you request anything to resolve that uncertainty before deciding?

Participant: Not specifically for the route. Time was a factor — we were already tight against the assault window.

Interviewer: What happened as a result?

Participant: We crossed clean, no contact, but we came out about four minutes behind timeline, which compressed everything downstream.

Interviewer: Let's go to the breach decision. What were the options there?

Participant: Rear wall or front gate. Rear wall we'd rehearsed extensively in training — I could run that sequence in my head start to finish, exactly how the team would flow through. Because I could see every step of it, it felt less likely to go wrong than the front gate, even though I didn't actually have a current read showing the rear wall was any safer than the gate — that was just a feeling from how clearly I could picture it. Front gate was less rehearsed, though our engineer actually assessed it as structurally simpler to get through. The liaison flagged movement near the front gate suggesting people were awake there.

Interviewer: What about the rear wall — was there any comparable read on activity?

Participant: Team 1, my own guys, called the rear wall clean. The host-nation commandos, separately, reported ambiguous movement near that same wall. Two different reads on the same spot.

Interviewer: How did you resolve that conflict?

Participant: I went with Team 1's call. That's the read I trusted — they're my organic element, I know how they call things, I know their standards. The commandos' report was vaguer anyway, "possible movement," nothing concrete. Between that and being able to see exactly how the rear-wall entry would go from all the rehearsals, the front gate never really competed for my attention.

Interviewer: If the commandos' report had carried the same level of specificity as Team 1's — same level of certainty, just from them instead — would you have weighted it the same way?

Participant: Probably not, if I'm being straight about it. Even if it came in just as clean and specific, I think I'd still lean toward Team 1's version first, just because it's our own call. It's not that I'd ignore the commandos, but there's a trust that builds with your own guys that I don't have with an attached element yet, regardless of how the report reads.

Interviewer: What happened at the breach?

Participant: We went in the rear wall. Found a non-combatant right near the breach point, had to pause the whole assault element to sort that out. Wasn't dangerous, but it cost us time we didn't have a lot of.

Interviewer: Last decision point — the extraction. What was the situation?

Participant: One of my guys took a leg injury during that pause. Medic called it stable but said we needed to get him out within the window. Primary LZ was a twenty-minute movement through ground where our ISR coverage had gaps — the UAS had been intermittent all night because of weather. The casevac bird had a narrow fuel window.

Interviewer: What made you choose the primary LZ over the alternatives?

Participant: We'd used that exact exfil sequence successfully the last two times we'd operated in that valley — same LZ, same general flow. It had worked clean both times, so I had a lot of confidence going into it. There was a closer casevac point off the approved list, and we could've held for a dedicated casevac asset instead of the standard bird, but both of those added complexity or delay I didn't think we needed given how smoothly things had gone before.

Interviewer: Did the casualty or the ISR gaps change your risk calculus at all?

Participant: Not as much as maybe they should have, looking back. I was leaning heavily on "this has worked twice," and I don't think I fully re-weighted for the fact that this time we had a man down and less coverage than we'd had before.

Interviewer: What actually happened?

Participant: We made it to the primary LZ without incident, but we landed right at the edge of the bird's fuel window, so the load was rushed. It worked out, but it was tighter than it needed to be.

Interviewer: If the family-residence report had come in with a specific time window and independent corroboration instead of a general caveat, would that have changed your launch decision?

Participant: Probably, yeah. If it had pinned down that people would definitely be inside during the assault window, and it wasn't just a single uncorroborated note, I think that gets weighed a lot more seriously against the SIGINT. It was the vagueness and lack of a second source that let me set it aside as easily as I did.

Interviewer: If you hadn't had that earlier firefight in the wadi, do you think you'd have picked the same route?

Participant: Maybe. Without that memory pulling at me, I might have given the alternate route a fairer look on its own merits instead of it competing against a gut feeling either way.

Interviewer: Looking back, what would you tell a junior team leader about reading a sequence like this — quiet, then contested, then quiet again?

Participant: I'd say don't let a streak, in either direction, do your thinking for you, and don't assume today's team call is more solid than someone else's just because it's your own guys. Weigh the actual report, not who it came from.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Biased_7",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Special Operations Forces (SOF) Team Leader / Troop Commander",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Operation Nightfall Anvil: HVT Raid on Compound Zaytun",
    "scenario_summary_internal": "A SOF Troop Commander leads a partnered direct-action raid against a suspected high-value target (HVT) compound in a semi-permissive rural valley. The mission unfolds across intel validation, infiltration, assault/breach, and casualty-evacuation/extraction phases. Ambiguous signals intelligence, a partnered host-nation element, prior contact history in the valley, and time-compressed decision windows create realistic openings for seven distinct cognitive biases without any explicit bias language appearing in the interview.",
    "occupational_realism": {
      "objective": "Capture or kill a mid-tier facilitator (HVT 'Zaytun') believed to be co-located with a weapons cache in a rural compound, while minimizing civilian and partner-force casualties and preserving follow-on exploitation of the site.",
      "setting": "Nighttime partnered direct-action raid, rural valley compound, 45-minute infiltration by foot from a helicopter offset landing zone, host-nation commando element attached to the troop.",
      "constraints": [
        "Compressed planning window (6 hours from tasking to launch)",
        "Partnered host-nation force with separate reporting chain and caveats",
        "Single collection asset (UAS) with intermittent coverage due to weather",
        "Prior contact history in the valley from two earlier operations",
        "Limited exfil helicopter windows tied to fuel and threat envelope",
        "Rules of engagement requiring positive identification before use of force"
      ],
      "stakeholders": [
        "Troop Commander (interviewee)",
        "Assault element leads (Team 1 and Team 2)",
        "Host-nation commando liaison officer",
        "Joint Operations Center (JOC) watch officer",
        "Intelligence support team / all-source analyst",
        "Medic / casualty evacuation lead"
      ],
      "technical_terms_to_use": [
        "HVT", "PID (positive identification)", "infil/exfil", "breach point",
        "SIGINT", "pattern-of-life", "casevac", "offset LZ", "troop", "assault element",
        "host-nation force (HNF)", "JOC", "ISR", "compromise authority"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias", "heuristic", "confirmation", "anchoring", "availability",
        "in-group bias", "optimism bias", "gambler's fallacy", "psychological terminology"
      ],
      "timeline_narrative_notes": "Chronological, first-person retrospective account structured around the four decision points, interspersed with probe-driven elaboration rather than a dry after-action report."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "SIGINT hit placing a phone associated with Zaytun's network inside the compound two nights prior",
          "A dissenting field report from the host-nation liaison noting the compound is also a known family residence with children present during the day",
          "Prior two operations in the same valley yielded confirmed HVTs with minimal collateral incidents",
          "Analyst caveat that phone geolocation confidence is 'moderate, not high'"
        ],
        "new_information_after_decision": [
          "UAS coverage during infil shows more vehicle activity at the compound than pattern-of-life models predicted"
        ],
        "alternatives": [
          "Launch the raid as tasked on the SIGINT hit",
          "Delay 24 hours to request a second collection pass to resolve the family-residence report",
          "Downgrade to a lower-signature surveillance-only tasking"
        ],
        "intended_action": "Troop Commander approves launch, treating the liaison's dissenting report as not worth reweighting the plan."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Infiltration route crosses a wadi that was the site of a sharp firefight on a mission eight months earlier, vividly remembered by the Commander",
          "Current mission has had three consecutive quiet insertions in the same general area over the past two months",
          "Route brief includes a less-traveled but slower alternate path avoiding the wadi"
        ],
        "new_information_after_decision": [
          "The team crosses without contact, but arrives four minutes behind the assault timeline"
        ],
        "alternatives": [
          "Take the wadi route because 'it's due for a quiet crossing' given the recent run of quiet insertions",
          "Take the wadi route while treating the earlier firefight as the dominant reference point for danger, overriding current threat reporting",
          "Take the slower alternate route to avoid the historically contested chokepoint"
        ],
        "intended_action": "Commander selects the wadi route, reasoning partly from the vivid firefight memory and partly from the recent run of uneventful crossings, rather than from current threat data."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two viable breach points: a rear wall (rehearsed extensively in training, easy to visualize executing cleanly) and a front gate (less rehearsed, structurally simpler per the engineer's assessment)",
          "Host-nation liaison flags movement near the front gate suggesting occupants are awake",
          "Team 1 (organic SOF element) reports the rear wall is 'clean,' while the host-nation commandos report ambiguous movement near the rear wall too"
        ],
        "new_information_after_decision": [
          "Breach proceeds at the rear wall; a non-combatant is found inside near the breach point, requiring an unplanned pause"
        ],
        "alternatives": [
          "Breach the rear wall because the team can vividly picture the rehearsed sequence unfolding smoothly",
          "Breach the front gate based on the engineer's structural assessment and the liaison's movement report",
          "Hold and request updated ISR before committing to either breach point"
        ],
        "intended_action": "Commander commits to the rear-wall breach, favoring the organic team's 'clean' call over the host-nation commandos' ambiguous movement report at the same location, and because the rehearsed scenario is easier to picture succeeding."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "A team member sustains a leg injury during the pause at the rear wall; medic assesses it as stable but requiring evacuation within the operational window",
          "Primary exfil LZ requires a 20-minute movement through terrain with unresolved ISR gaps",
          "Casevac helicopter has a narrow fuel-driven window; Commander has personally executed this exact exfil sequence successfully on the two prior valley operations"
        ],
        "new_information_after_decision": [
          "The movement to the primary LZ proceeds without incident, but arrives at the edge of the helicopter's fuel window, forcing a rushed load"
        ],
        "alternatives": [
          "Proceed to the primary LZ on the assumption that, like the last two operations, exfil will go smoothly",
          "Request an alternate, closer casevac point despite it being outside the pre-cleared LZ list",
          "Hold in place and request a dedicated casevac asset rather than the standard exfil bird"
        ],
        "intended_action": "Commander proceeds to the primary LZ, underestimating the risk of the ISR-gapped movement and fuel-window compression because the same sequence had worked cleanly the previous two times."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through the mission from tasking to your final report.",
        "What was your role and what were you responsible for deciding?"
      ],
      "timeline_reconstruction": [
        "What information did you have at each stage, and where did it come from?",
        "What changed between the plan and what you actually encountered on the ground?"
      ],
      "decision_point_probes": [
        "At the point you approved launch, what made the liaison's report less influential than the SIGINT hit?",
        "When choosing the infiltration route, what past experiences or recent patterns came to mind, and how did they weigh against current reporting?",
        "At the breach decision, whose read on the situation did you trust more, and why?",
        "When selecting the exfil approach, what made you confident in the primary LZ despite the ISR gaps?"
      ],
      "goals_and_alternatives": [
        "What other options did you consider at each of those moments, and why were they set aside?"
      ],
      "decision_basis": [
        "What single piece of information, if any, tipped the decision one way?"
      ],
      "prior_experience": [
        "How did earlier operations in this valley shape what you expected this time?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time did you have to weigh these options, and how confident were you in the information at the time?"
      ],
      "closing_hypotheticals": [
        "If the host-nation liaison's report had come from your own team instead, would that have changed your launch decision?",
        "If you had not had the earlier firefight in that wadi, would you have chosen the same infiltration route?",
        "Looking back, what would you tell a junior team leader to watch for in a similar sequence of quiet, then contested, then quiet operations?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "MD7_01",
        "bias": "Negative Rejection Bias",
        "decision_point": 1,
        "mechanism": "Commander discounts the host-nation liaison's dissenting, unfavorable report (family residence, children present) specifically because it conflicts with the desired go decision, rather than evaluating it on its evidentiary merits.",
        "affected_reasoning_operation": "Evidence-selection / weighting of disconfirming information",
        "evidence_available_at_time": [
          "SIGINT hit with moderate confidence",
          "Liaison report flagging family residence and children",
          "Two prior successful valley operations"
        ],
        "required_textual_manifestation": "Commander explicitly recalls receiving the liaison's report and describes setting it aside because it did not fit the picture built from the SIGINT hit, without citing a specific evidentiary reason for rejecting it.",
        "plausible_nonbias_interpretation": "The liaison's report could reasonably be judged lower-reliability due to caveated host-nation reporting standards.",
        "strength": "subtle",
        "do_not_make_explicit": ["negative rejection bias", "dismissal", "disconfirming evidence"]
      },
      {
        "instance_id": "MD7_02",
        "bias": "Search set Bias",
        "decision_point": 1,
        "mechanism": "Commander's consideration of response options is narrowed to launch-as-tasked versus delay, without the surveillance-only downgrade option being seriously entertained, because that option falls outside the troop's habitual repertoire of responses.",
        "affected_reasoning_operation": "Generation of alternative courses of action",
        "evidence_available_at_time": [
          "Standard troop playbook of go/no-go/delay options",
          "Analyst caveat on geolocation confidence"
        ],
        "required_textual_manifestation": "When asked what other options existed, Commander names only launch or delay, treating the surveillance-only option as not a real alternative in this kind of tasking.",
        "plausible_nonbias_interpretation": "Surveillance-only taskings may genuinely fall outside the troop's mandate for this mission type.",
        "strength": "subtle",
        "do_not_make_explicit": ["search set bias", "narrow option generation"]
      },
      {
        "instance_id": "MD7_03",
        "bias": "Retrievability Bias",
        "decision_point": 2,
        "mechanism": "The vivid, personally memorable firefight from eight months earlier at the same wadi disproportionately shapes the Commander's route risk assessment relative to the less memorable but more current threat picture.",
        "affected_reasoning_operation": "Recall and weighting of prior experience for risk assessment",
        "evidence_available_at_time": [
          "Memory of an intense firefight at the wadi eight months prior",
          "Current route brief noting the wadi as a known chokepoint",
          "Absence of recent contact reports at the wadi"
        ],
        "required_textual_manifestation": "Commander describes the wadi decision by referencing how vividly he remembers that earlier firefight, and how that memory colored his sense of the route's danger more than current reporting did.",
        "plausible_nonbias_interpretation": "Route familiarity from a past engagement is a legitimate input to tactical planning.",
        "strength": "subtle",
        "do_not_make_explicit": ["retrievability bias", "vivid memory", "availability of memory"]
      },
      {
        "instance_id": "MD7_04",
        "bias": "Gamblers Fallacy",
        "decision_point": 2,
        "mechanism": "Commander treats the recent string of three uneventful insertions as increasing the likelihood that this crossing will also be quiet, or alternatively as making contact 'due,' rather than assessing the route on independent current conditions.",
        "affected_reasoning_operation": "Probability judgment from a sequence of past independent events",
        "evidence_available_at_time": [
          "Three consecutive quiet insertions in the same general area over two months",
          "No new intelligence specifically indicating this crossing's risk"
        ],
        "required_textual_manifestation": "Commander explains reasoning that, given how many quiet crossings there had recently been in that area, this one felt either overdue for contact or safely likely to stay quiet, framing the run of past outcomes as informative about this specific crossing's odds.",
        "plausible_nonbias_interpretation": "A recent pattern of quiet insertions could reflect a genuine, currently valid reduction in enemy activity in that corridor.",
        "strength": "moderate",
        "do_not_make_explicit": ["gambler's fallacy", "streak", "due for contact"]
      },
      {
        "instance_id": "MD7_05",
        "bias": "Imaginability Bias",
        "decision_point": 3,
        "mechanism": "The rear-wall breach is favored because the extensively rehearsed sequence is easy to picture executing cleanly, inflating the Commander's confidence in its success relative to the less-rehearsed front-gate option, independent of the actual structural or threat assessments.",
        "affected_reasoning_operation": "Probability/success estimation based on ease of mental simulation",
        "evidence_available_at_time": [
          "Extensive rehearsal history on the rear-wall breach sequence",
          "Engineer's assessment that the front gate is structurally simpler",
          "Liaison report of movement near the front gate"
        ],
        "required_textual_manifestation": "Commander describes being able to 'see exactly how it would go' at the rear wall because of the rehearsals, and lets that clarity of mental picture tip the choice over the front-gate option.",
        "plausible_nonbias_interpretation": "Rehearsal genuinely improves execution reliability, so preferring a well-rehearsed breach point is a defensible tactical choice.",
        "strength": "subtle",
        "do_not_make_explicit": ["imaginability bias", "ease of imagining", "mental simulation"]
      },
      {
        "instance_id": "MD7_06",
        "bias": "Ingroup Preference bias or In-group bias",
        "decision_point": 3,
        "mechanism": "At the same rear-wall breach point, the Commander weights the organic SOF team's 'clean' call over the host-nation commandos' ambiguous movement report at that identical location, based on team affiliation rather than the comparative reliability of the two reports.",
        "affected_reasoning_operation": "Cross-source evidence weighting at a shared decision moment",
        "evidence_available_at_time": [
          "Team 1 (organic) report: rear wall is 'clean'",
          "Host-nation commando report: ambiguous movement near the same rear wall"
        ],
        "required_textual_manifestation": "Commander explains trusting Team 1's call over the host-nation commandos' report specifically because it came from his own team, without offering an independent evidentiary reason the organic report was more reliable.",
        "plausible_nonbias_interpretation": "Organic teams may have better training standardization, making their reports genuinely more reliable in this Commander's experience.",
        "strength": "moderate",
        "do_not_make_explicit": ["in-group bias", "own team", "outgroup", "favoritism"]
      },
      {
        "instance_id": "MD7_07",
        "bias": "Optimism bias",
        "decision_point": 4,
        "mechanism": "Commander underestimates the compounded risk of an ISR-gapped movement plus a fuel-constrained exfil window because the identical sequence succeeded on the two prior valley operations, projecting a personally favorable outcome despite objectively worse conditions (casualty aboard, gap in coverage).",
        "affected_reasoning_operation": "Forward risk projection for a planned course of action",
        "evidence_available_at_time": [
          "Two prior successful uses of the same exfil sequence",
          "Unresolved ISR gaps on the current movement path",
          "Narrow fuel-driven casevac window with an injured team member"
        ],
        "required_textual_manifestation": "Commander states confidence that the exfil would go as smoothly as the previous two times, without adjusting that confidence for the added casualty and the current ISR gap.",
        "plausible_nonbias_interpretation": "Confidence built on a real track record of successful execution of the same sequence is a legitimate basis for a plan.",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "overconfidence", "underestimating risk"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control."
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
      "Exactly 4 decision points present, each with at least two plausible alternatives.",
      "Exactly 7 total intended bias instances, one per manifest entry, no bias repeated beyond its requested count.",
      "No two instances at the same decision point (DP1: 2, DP2: 2, DP3: 2, DP4: 1) share the same evidence source or reasoning moment.",
      "No bias terminology, labels, or definitions appear in probes or narrative content.",
      "Each instance has a plausible non-bias explanation documented to prevent mechanical outcome-based scoring.",
      "Target word count 1,350 (range 1,215-1,485) achievable given 4 decision points with moderate probe density and no repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Negative Rejection Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as discounting a dissenting/unfavorable liaison report at the intel-validation decision point."},
      {"bias": "Retrievability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as vivid past-event memory disproportionately shaping current route risk assessment."},
      {"bias": "Search set Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as an artificially narrowed set of considered courses of action at the launch decision."},
      {"bias": "Imaginability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as ease of mentally simulating a rehearsed breach inflating confidence in that option."},
      {"bias": "Gamblers Fallacy", "occurrences": 1, "mechanism_constraint": "Must manifest as treating a recent run of independent quiet insertions as predictive of the current crossing's odds."},
      {"bias": "Ingroup Preference bias or In-group bias", "occurrences": 1, "mechanism_constraint": "Must manifest as favoring the organic team's report over the host-nation commandos' report at the same breach point based on affiliation."},
      {"bias": "Optimism bias", "occurrences": 1, "mechanism_constraint": "Must manifest as underestimating compounded exfil risk based on past personal success with the same sequence."}
    ],
    "target_bias_names": [
      "Negative Rejection Bias",
      "Retrievability Bias",
      "Search set Bias",
      "Imaginability Bias",
      "Gamblers Fallacy",
      "Ingroup Preference bias or In-group bias",
      "Optimism bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Negative Rejection Bias", "requested_occurrences": 1},
      {"bias": "Retrievability Bias", "requested_occurrences": 1},
      {"bias": "Search set Bias", "requested_occurrences": 1},
      {"bias": "Imaginability Bias", "requested_occurrences": 1},
      {"bias": "Gamblers Fallacy", "requested_occurrences": 1},
      {"bias": "Ingroup Preference bias or In-group bias", "requested_occurrences": 1},
      {"bias": "Optimism bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "MD7_01", "bias": "Negative Rejection Bias"},
      {"instance_id": "MD7_02", "bias": "Search set Bias"},
      {"instance_id": "MD7_03", "bias": "Retrievability Bias"},
      {"instance_id": "MD7_04", "bias": "Gamblers Fallacy"},
      {"instance_id": "MD7_05", "bias": "Imaginability Bias"},
      {"instance_id": "MD7_06", "bias": "Ingroup Preference bias or In-group bias"},
      {"instance_id": "MD7_07", "bias": "Optimism bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "MD7_01", "bias": "Negative Rejection Bias", "decision_point": 1},
      {"instance_id": "MD7_02", "bias": "Search set Bias", "decision_point": 1},
      {"instance_id": "MD7_03", "bias": "Retrievability Bias", "decision_point": 2},
      {"instance_id": "MD7_04", "bias": "Gamblers Fallacy", "decision_point": 2},
      {"instance_id": "MD7_05", "bias": "Imaginability Bias", "decision_point": 3},
      {"instance_id": "MD7_06", "bias": "Ingroup Preference bias or In-group bias", "decision_point": 3},
      {"instance_id": "MD7_07", "bias": "Optimism bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MD7_01",
        "bias": "Negative Rejection Bias",
        "mechanism": "Discounting the host-nation liaison's unfavorable, dissenting report on family residence/children because it conflicts with the desired go decision.",
        "affected_reasoning_operation": "Evidence-selection / weighting of disconfirming information",
        "evidence_source": "Host-nation liaison field report",
        "distinctiveness_requirement": "Distinct from MD7_02 (option-generation narrowing) and from MD7_06 (which involves comparative source trust rather than rejection of unfavorable content)."
      },
      {
        "instance_id": "MD7_02",
        "bias": "Search set Bias",
        "mechanism": "Failing to seriously generate or consider the surveillance-only downgrade option, restricting alternatives to the habitual go/delay pair.",
        "affected_reasoning_operation": "Generation of alternative courses of action",
        "evidence_source": "Troop standard operating repertoire / mission tasking framework",
        "distinctiveness_requirement": "Distinct from MD7_01: this instance concerns the range of options generated, not the weighting of a specific piece of disconfirming evidence."
      },
      {
        "instance_id": "MD7_03",
        "bias": "Retrievability Bias",
        "mechanism": "An emotionally vivid firefight memory from eight months prior dominates route risk assessment over current, less memorable threat reporting.",
        "affected_reasoning_operation": "Recall-based risk weighting",
        "evidence_source": "Commander's personal memory of a prior firefight at the same location",
        "distinctiveness_requirement": "Distinct from MD7_04: this instance concerns vividness/salience of a single memorable event, not a sequence-based probability judgment."
      },
      {
        "instance_id": "MD7_04",
        "bias": "Gamblers Fallacy",
        "mechanism": "Treating a recent independent sequence of quiet insertions as informative about the probability of contact on the current, unrelated crossing.",
        "affected_reasoning_operation": "Sequential probability judgment",
        "evidence_source": "Record of three prior insertions in the same general area over two months",
        "distinctiveness_requirement": "Distinct from MD7_03: this instance concerns a run of outcomes treated as altering future independent odds, not the salience of one vivid event."
      },
      {
        "instance_id": "MD7_05",
        "bias": "Imaginability Bias",
        "mechanism": "Ease of mentally simulating the well-rehearsed rear-wall breach inflates its perceived success probability relative to the front gate.",
        "affected_reasoning_operation": "Success-probability estimation via mental simulation ease",
        "evidence_source": "Rehearsal history for the rear-wall breach sequence",
        "distinctiveness_requirement": "Distinct from MD7_06: this instance concerns confidence derived from rehearsal-driven visualization, not comparative trust between two reporting sources."
      },
      {
        "instance_id": "MD7_06",
        "bias": "Ingroup Preference bias or In-group bias",
        "mechanism": "At the identical rear-wall breach point, the organic team's report is trusted over the host-nation commandos' ambiguous report due to team affiliation rather than evidentiary merit.",
        "affected_reasoning_operation": "Cross-source evidence weighting",
        "evidence_source": "Team 1 (organic) 'clean' call versus host-nation commando ambiguous-movement report",
        "distinctiveness_requirement": "Distinct from MD7_05: this instance concerns differential trust across two competing reports on the same location, not visualization-driven confidence in one option."
      },
      {
        "instance_id": "MD7_07",
        "bias": "Optimism bias",
        "mechanism": "Confidence in the primary exfil route is projected forward from two prior successes without adjusting for the current casualty and ISR gap, underestimating compounded risk.",
        "affected_reasoning_operation": "Forward risk projection",
        "evidence_source": "Track record of two prior successful exfils using the same sequence",
        "distinctiveness_requirement": "Sole instance at decision point 4; distinguished from all others by occurring at the final extraction phase and concerning self-referential risk projection rather than evidence weighting."
      }
    ],
    "intended_strength": [
      {"instance_id": "MD7_01", "bias": "Negative Rejection Bias", "strength": "subtle"},
      {"instance_id": "MD7_02", "bias": "Search set Bias", "strength": "subtle"},
      {"instance_id": "MD7_03", "bias": "Retrievability Bias", "strength": "subtle"},
      {"instance_id": "MD7_04", "bias": "Gamblers Fallacy", "strength": "moderate"},
      {"instance_id": "MD7_05", "bias": "Imaginability Bias", "strength": "subtle"},
      {"instance_id": "MD7_06", "bias": "Ingroup Preference bias or In-group bias", "strength": "moderate"},
      {"instance_id": "MD7_07", "bias": "Optimism bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Biased_7",
    "domain_id": "MD",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across the 4 decision points by mechanism fit and narrative realism: DP1 (intel validation) received Negative Rejection Bias and Search set Bias since both concern pre-launch evidence/option handling; DP2 (infiltration) received Retrievability Bias and Gamblers Fallacy since both concern route-risk judgment under a stream of prior experience; DP3 (assault/breach) received Imaginability Bias and Ingroup Preference bias since both concern breach-point confidence at the same physical decision moment but via distinct mechanisms (visualization vs. source trust) and distinct evidence sources; DP4 (extraction) received the sole remaining bias, Optimism bias, fitting the forward-risk-projection nature of the exfil decision. No decision point received more than two instances, and co-located instances (DP1, DP3) were required to use distinct evidence sources and reasoning operations per the exact-occurrence rules.",
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
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "launch evidence weighting",
        "raw_interview_anchor": "Honestly, it didn't move the needle much for me ... it just didn't carry the same weight as the geolocation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["MD7_01"],
        "ground_truth_rationale": "The participant discounts the unfavorable family-residence report because it does not fit the go decision built around the SIGINT hit, without a specific evidentiary reason."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "alternative generation",
        "raw_interview_anchor": "Really it came down to launch or delay twenty-four hours ... the surveillance option didn't get serious airtime.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["MD7_02"],
        "ground_truth_rationale": "The response narrows the course-of-action set to launch or delay and treats an available surveillance-only option as outside the real repertoire because the troop defaults to assaulting the tasking."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "route risk assessment",
        "raw_interview_anchor": "The firefight sticks with you ... when I pictured that wadi, I pictured tracer fire, not a calm crossing, even though nothing in the current threat picture pointed to that.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["MD7_03"],
        "ground_truth_rationale": "A vivid personal firefight memory disproportionately shapes current route-risk assessment over the current threat picture."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "sequence-based route judgment",
        "raw_interview_anchor": "At the same time, we'd had three clean runs through there recently ... I went with the wadi route mostly on that combination rather than waiting on updated route-specific intel.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["MD7_04"],
        "ground_truth_rationale": "The participant treats the recent run of quiet crossings as relevant to whether contact will continue or is due, rather than evaluating the current crossing independently."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "information-seeking decision",
        "raw_interview_anchor": "Not specifically for the route. Time was a factor — we were already tight against the assault window.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a separate decision not to request route-specific clarification; the stated time constraint is a plausible non-bias explanation and is not itself a hidden target instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "breach option probability judgment",
        "raw_interview_anchor": "Rear wall we'd rehearsed extensively in training ... it felt less likely to go wrong than the front gate, even though I didn't actually have a current read showing the rear wall was any safer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["MD7_05"],
        "ground_truth_rationale": "Ease of mentally simulating the rehearsed rear-wall sequence is treated as evidence of lower failure risk despite comparative structural and activity information favoring consideration of the gate."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "conflicting-source resolution",
        "raw_interview_anchor": "I went with Team 1's call ... they're my organic element ... the front gate never really competed for my attention.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["MD7_06"],
        "ground_truth_rationale": "The participant favors the organic team's report over the host-nation report at the same location based on affiliation and built-in trust, in addition to the report-specific difference in vagueness."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "initial extraction option rationale",
        "raw_interview_anchor": "We'd used that exact exfil sequence successfully the last two times ... both of those added complexity or delay I didn't think we needed.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Prior success and avoiding added complexity are stated as the initial rationale, but this span alone does not explicitly show failure to adjust for the current casualty and ISR gap; the hidden mechanism is localized to the subsequent reweighting reflection."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "extraction risk reassessment",
        "raw_interview_anchor": "Not as much as maybe they should have, looking back ... I don't think I fully re-weighted for the fact that this time we had a man down and less coverage than we'd had before.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["MD7_07"],
        "ground_truth_rationale": "The participant explicitly acknowledges projecting confidence from two prior successes without sufficiently adjusting for worse current conditions, which is the hidden optimism mechanism."
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
    "analysis_scope_note": "Analysis of a single interview transcript for cognitive bias occurrences. No retrieved scientific-paper corpus passages were provided, so labels use established general cognitive-science knowledge and corpus support is explicitly marked unavailable."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability_heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation_bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "fluency_heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "ingroup_bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence_effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "status_quo_bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "confirmation_bias",
      "alternative_labels": [
        "myside_bias",
        "congeniality_bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, or recall information in ways that confirm one's pre-existing beliefs or hypotheses, while giving disproportionately little weight to disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Launch go/no-go: weighing SIGINT and family-residence report",
      "decision_point_description": "Go/no-go launch decision after receiving moderate-confidence SIGINT geolocation and a host-nation family-residence caution.",
      "affected_reasoning_operation": "Weighing conflicting intelligence in the launch decision",
      "bias_specific_mechanism": "The initial geolocation hypothesis from SIGINT and two prior successful operations formed a strong expectancy. The family-residence report was treated as background texture and dismissed without a specific reason, so disconfirming information was not weighted on its evidential content but on its consistency with the existing assault plan.",
      "manifestation_in_interview": "The participant explicitly describes not needing a specific reason to set aside the family-residence note and says it did not carry the same weight as the geolocation.",
      "effect_on_reasoning_or_decision": "The civilian-risk information did not materially affect the launch calculation, and the existing target picture remained dominant.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The SIGINT was the thing that put the target in that building, and the two prior ops had built a lot of confidence that when we get a hit like that in that valley, it pans out. The family-residence note felt like background texture rather than something that should change the plan — it wasn't tied to a specific threat, more of a general caution. I didn't feel like I needed a specific reason to set it aside, it just didn't carry the same weight as the geolocation.",
          "evidence_explanation": "The existing target hypothesis and prior successes are weighted heavily, while the disconfirming family-residence caution is minimized without a specific reason; this is the asymmetrical weighting characteristic of confirmation bias."
        }
      ],
      "correction_or_counterevidence": "The participant later said a specific and independently corroborated family-residence report would have been weighed more seriously, suggesting information quality was also relevant; the actual report was vague and uncorroborated.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "status_quo_bias",
      "alternative_labels": [
        "default_bias",
        "default_option_bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A preference for the current or default course of action over alternatives, even when alternatives may be feasible or potentially preferable.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Launch go/no-go: option consideration",
      "decision_point_description": "Choosing among immediate assault, 24-hour delay for collection, or lower-signature surveillance-only option.",
      "affected_reasoning_operation": "Option generation and consideration during the launch decision",
      "bias_specific_mechanism": "The assault approach was the unit's default template; the surveillance-only option was not rejected through explicit feasibility weighing but was excluded because the room defaulted to assault. The existing standard dominated the option set.",
      "manifestation_in_interview": "The participant says the surveillance option did not get serious airtime because the room defaults to assault.",
      "effect_on_reasoning_or_decision": "The decision space was narrowed to launch or delay rather than seriously considering a lower-signature surveillance option.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was technically a lower-signature surveillance-only option on paper — the host-nation element had eyes-capable personnel and our supporting ISR asset could have sustained a watch, so it wasn't off the table for lack of means. But that's not really how we use this troop — we're not built for that mission set, and when a tasking like this comes in, the room just defaults to figuring out how to assault it, so the surveillance option didn't get serious airtime.",
          "evidence_explanation": "A feasible alternative was not actively compared; the explanation describes a default to the assault template rather than an explicit rejection of surveillance on its merits."
        }
      ],
      "correction_or_counterevidence": "The participant also cites unit role and mission set as reasons, and time was tight, so the preference may partly reflect legitimate structural or logistical constraints rather than pure default bias.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability_heuristic",
      "alternative_labels": [
        "affect_heuristic",
        "salience_effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which people judge likelihood or risk by the ease with which instances come to mind; salient or emotional memories are disproportionately available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Infiltration route selection",
      "decision_point_description": "Choosing between the wadi route and a slower alternate route.",
      "affected_reasoning_operation": "Risk perception and route choice under uncertainty",
      "bias_specific_mechanism": "The earlier firefight in the same wadi was salient and emotionally evocative, so it dominated mental imagery and route risk assessment, even though current threat reporting did not support that risk.",
      "manifestation_in_interview": "The participant says he pictured tracer fire rather than a calm crossing when thinking about the wadi, even though the current threat picture did not point to that.",
      "effect_on_reasoning_or_decision": "He selected the wadi route on that felt risk picture rather than waiting on updated route-specific intelligence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The firefight sticks with you in a way that current reporting doesn't always match — when I pictured that wadi, I pictured tracer fire, not a calm crossing, even though nothing in the current threat picture pointed to that.",
          "evidence_explanation": "The vivid, salient memory of the earlier firefight dominates route risk perception over current reporting, which is the availability/affect mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with the wadi route mostly on that combination rather than waiting on updated route-specific intel.",
          "evidence_explanation": "The participant explicitly states the memory-driven combination influenced the route choice."
        }
      ],
      "correction_or_counterevidence": "There had also been three recent quiet insertions and no current specific threat, so the route choice was not wholly unsupported; the bias is that the old firefight memory pulled more than current reporting warranted.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "fluency_heuristic",
      "alternative_labels": [
        "processing_fluency_effect",
        "ease_of_processing_bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The mental shortcut whereby subjective ease of processing or imagining an action is used as a cue to lower risk and higher success likelihood.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Breach point selection",
      "decision_point_description": "Choosing between rear-wall and front-gate breach.",
      "affected_reasoning_operation": "Breach option risk assessment and selection",
      "bias_specific_mechanism": "The rear-wall sequence was extensively rehearsed and could be mentally simulated step-by-step. The felt ease of that simulation was treated as evidence that the rear wall was less likely to go wrong, despite absence of current intelligence on the rear wall and an engineer assessment favoring the front gate for structural simplicity.",
      "manifestation_in_interview": "The participant says the feeling from how clearly he could picture the rear-wall sequence made it feel less likely to go wrong.",
      "effect_on_reasoning_or_decision": "The rear wall was selected partly because rehearsed fluency made it feel safer, and the front gate never really competed for attention.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Rear wall we'd rehearsed extensively in training — I could run that sequence in my head start to finish, exactly how the team would flow through. Because I could see every step of it, it felt less likely to go wrong than the front gate, even though I didn't actually have a current read showing the rear wall was any safer than the gate — that was just a feeling from how clearly I could picture it.",
          "evidence_explanation": "The ease of mentally simulating the rehearsed rear-wall plan was treated as diagnostic of safety and low failure risk, despite the absence of current intelligence; this is fluency used as a heuristic."
        }
      ],
      "correction_or_counterevidence": "There was also Team 1's clean report on the rear wall, and the front gate was less rehearsed, so some preference for a rehearsed plan may be operationally rational; however, the specific statement identifies fluency from rehearsals rather than current-read risk as the mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "ingroup_bias",
      "alternative_labels": [
        "ingroup_favoritism",
        "own_group_bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to favor or trust members of one's own group over others and to evaluate their information as more credible regardless of content.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Resolution of conflicting breach-point activity reports",
      "decision_point_description": "Deciding whether the rear wall was clear given conflicting Team 1 and host-nation commando reports.",
      "affected_reasoning_operation": "Source credibility assessment",
      "bias_specific_mechanism": "The decision to accept Team 1's report over the host-nation commandos' report was driven by group membership and organic-unit trust rather than by a purely content-based comparison. The participant said he would still lean toward Team 1 even if the commando report were equally specific.",
      "manifestation_in_interview": "The participant explicitly acknowledges he would weight his own unit's call first 'just because it's our own call.'",
      "effect_on_reasoning_or_decision": "The conflicting rear-wall ambiguity was resolved in favor of Team 1, contributing to the decision to use the rear wall.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with Team 1's call. That's the read I trusted — they're my organic element, I know how they call things, I know their standards. The commandos' report was vaguer anyway, 'possible movement,' nothing concrete.",
          "evidence_explanation": "The participant resolves the conflict partly by invoking who provided the report, not only the report content."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Even if it came in just as clean and specific, I think I'd still lean toward Team 1's version first, just because it's our own call. It's not that I'd ignore the commandos, but there's a trust that builds with your own guys that I don't have with an attached element yet, regardless of how the report reads.",
          "evidence_explanation": "This counterfactual statement shows group membership, rather than report quality, would still influence the credibility judgment."
        }
      ],
      "correction_or_counterevidence": "The commandos' actual report was less specific, so a content-based preference was also available; the bias is most directly evidenced by his counterfactual statement about equal specificity.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "overconfidence_effect",
      "alternative_labels": [
        "overconfidence_bias",
        "miscalibration_effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A miscalibration in which subjective confidence in a decision or prediction is higher than warranted by available evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Extraction LZ and casevac asset selection",
      "decision_point_description": "Choosing primary LZ over closer casevac point/dedicated casevac asset under casualty and ISR gaps.",
      "affected_reasoning_operation": "Extraction risk and confidence assessment",
      "bias_specific_mechanism": "Two prior clean uses of the exact exfil sequence produced strong confidence and a heavy reliance on 'this has worked twice'; current changed conditions, including a casualty and reduced ISR coverage, were not fully re-weighted.",
      "manifestation_in_interview": "The participant states he had a lot of confidence from two prior successes and did not fully re-weight for the fact that this time there was a man down and less coverage.",
      "effect_on_reasoning_or_decision": "Primary LZ was selected and alternatives were dismissed, leading to a rushed load at the edge of the fuel window.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd used that exact exfil sequence successfully the last two times we'd operated in that valley — same LZ, same general flow. It had worked clean both times, so I had a lot of confidence going into it.",
          "evidence_explanation": "A two-instance history of success produced high confidence in the exfil plan."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I was leaning heavily on 'this has worked twice,' and I don't think I fully re-weighted for the fact that this time we had a man down and less coverage than we'd had before.",
          "evidence_explanation": "The participant then identifies the miscalibration: confidence from previous success outweighed changed current circumstances."
        }
      ],
      "correction_or_counterevidence": "The primary LZ had succeeded before and was the standard option, and the alternatives added complexity or delay; the bias-specific evidence is the retrospective acknowledgment of insufficient re-weighting.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable; the label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "gambler's_fallacy",
      "alternative_labels": [
        "hot_hand_fallacy",
        "recency_bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Route selection after three quiet insertions",
      "supporting_interview_quote": "At the same time, we'd had three clean runs through there recently, and there's a pull toward thinking the run continues, or conversely that we were 'due.' I went with the wadi route mostly on that combination rather than waiting on updated route-specific intel.",
      "plausible_mechanism": "A sequence of prior quiet crossings may have been treated as predictive either that the quiet streak would continue or that a negative event was more likely, rather than using current route-specific intelligence.",
      "why_not_identified": "The participant describes both streak-continuation and being 'due' pulls but does not specify which of those mechanisms drove the choice; therefore it remains an unresolved candidate rather than an identified occurrence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-paper corpus passages were available for this analysis, so all bias labels and mechanisms are based on general cognitive-science knowledge rather than corpus support.",
    "The analysis relies solely on the participant's self-report; it cannot establish ground truth, actual probabilities, or the full contextual constraints of the operational decisions.",
    "Some identified occurrences, especially low-confidence confirmation-bias and moderate-confidence status-quo-bias findings, are subject to plausible non-bias explanations such as information quality, time pressure, unit capability, or legitimate use of prior experience."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Biased_7_Sonar_off",
  "interview_id": "MD_Biased_7",
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
