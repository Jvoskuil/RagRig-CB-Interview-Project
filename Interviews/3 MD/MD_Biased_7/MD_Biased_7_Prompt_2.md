You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MD_Biased_7",
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
