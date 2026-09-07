You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MD_Biased_4",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Fire Support Officer (FSO) / Joint Fires Observer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Danger-Close: Fire Support Coordination During a Company Clearing Operation",
    "scenario_summary_internal": "An FSO/JFO attached to an infantry company during a daylight clearing operation must coordinate mortar, CAS, and artillery fires against an enemy mortar team and a suspected staging compound near a populated area. Ammunition, time before the assault window closes, degraded comms, and proximity to friendly troops and civilians force four sequential fire-support decisions under pressure.",
    "occupational_realism": {
      "objective": "Suppress/destroy an enemy 82mm mortar team harassing the company's forward positions and clear a suspected staging compound before the assault window closes, without fratricide or civilian casualties.",
      "setting": "Daylight combined-arms clearing operation; company commander and FSO co-located at a forward command post; battalion Fire Support Coordination Center (FSCC), a CAS aircraft on station, and an adjacent partner-force unit all in the fires network.",
      "constraints": [
        "Limited 81mm mortar ammunition remaining for adjustment rounds",
        "30-minute window before the company must cross the line of departure",
        "Intermittent radio/data-link degradation between FSCC and forward observers",
        "Danger-close proximity of friendly squads to the target compound",
        "Possible civilian presence in the adjacent village",
        "Single organic ISR feed with known intermittent false-positive history"
      ],
      "stakeholders": [
        "Company commander",
        "Fire Support Officer / Joint Fires Observer (interviewee)",
        "Battalion FSCC watch officer",
        "Mortar section chief",
        "CAS pilot on station",
        "Adjacent partner-force liaison officer",
        "ISR/sensor analyst"
      ],
      "technical_terms_to_use": [
        "adjust fire",
        "danger close",
        "CDE (collateral damage estimate)",
        "9-line brief",
        "grid coordinate",
        "FSCC",
        "positive identification (PID)",
        "final attack heading",
        "cleared hot"
      ],
      "technical_terms_to_avoid": [
        "gambler's fallacy",
        "optimism bias",
        "in-group bias",
        "base rate",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two successive 81mm adjustment rounds have landed short of the mortar position",
          "Mortar section reports gun-line data checked once, no fault found",
          "Time remaining before assault window is closing"
        ],
        "new_information_after_decision": [
          "Third round result (on or off target) is learned only after firing",
          "A later data check reveals a leveling error unrelated to prior rounds"
        ],
        "alternatives": [
          "Order a full re-lay and data recheck of the gun line before firing again",
          "Fire the next adjustment round immediately, expecting the miss streak to end"
        ],
        "intended_action": "FSO authorizes firing another adjustment round without a full re-lay, reasoning that after two misses a hit is 'due'."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Battalion JTAC (same service) reports the enemy staging point at Grid A",
          "Adjacent partner-force liaison independently reports enemy activity at Grid B, roughly 300m away",
          "Both reports carry similar confidence caveats"
        ],
        "new_information_after_decision": [
          "Follow-on reconnaissance shows some indicators near Grid B as well as Grid A"
        ],
        "alternatives": [
          "Request cross-verification of both grids before committing fires",
          "Prioritize the battalion JTAC's grid because it comes through the FSO's own chain"
        ],
        "intended_action": "FSO weights the battalion JTAC's coordinate more heavily than the partner-force report largely because it originates from his own unit's channel."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "CAS pilot is ready for a danger-close run near friendly positions",
          "The last several CAS strikes with this squadron were executed cleanly with standard margins",
          "Current friendly-troop proximity is tighter than the squadron's usual margin, and communications with the lead squad have had brief dropouts"
        ],
        "new_information_after_decision": [
          "Communications with the lead squad drop out again during the final attack heading confirmation"
        ],
        "alternatives": [
          "Widen the safety margin or delay the run pending a stable communications check",
          "Proceed with the tighter margin, expecting it to go as smoothly as the recent strikes"
        ],
        "intended_action": "FSO clears the CAS run with the tight margin, expecting the outcome to match the string of recent successful strikes."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The sole ISR sensor flags a single 'possible enemy activity' cue at the suspected compound",
          "The sector has historically been quiet with routine civilian pattern-of-life",
          "The specific sensor type has a known history of false positives in this terrain"
        ],
        "new_information_after_decision": [
          "Post-strike assessment of what was actually present at the compound"
        ],
        "alternatives": [
          "Request a second confirming source given the sector's normally low enemy-activity rate",
          "Approve the artillery mission on the single sensor cue alone"
        ],
        "intended_action": "FSO approves the fire mission based on the one sensor cue, without factoring in how rarely this sector produces genuine enemy activity or how often this sensor errs."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe the mission and your role that day?",
        "What was the operational objective at the start of the clearing operation?"
      ],
      "timeline_reconstruction": [
        "Walk me through the sequence of fire missions in the order they happened.",
        "What information did you have at each stage, and what changed afterward?"
      ],
      "decision_point_probes": [
        "What cues made you decide to fire again without a full re-lay?",
        "How did you weigh the battalion JTAC's grid against the partner-force liaison's grid?",
        "What made you comfortable clearing the CAS run with a tighter margin than usual?",
        "How did the sector's history factor into your decision to approve the artillery mission on one sensor cue?",
        "What information sources did you rely on most at each point, and why?",
        "How much time pressure did you feel at each decision, and how did it affect your process?",
        "How confident were you in each call, and what would have changed your mind?",
        "Looking back, what would you do differently if you replayed each decision?"
      ],
      "closing_hypotheticals": [
        "If the mortar section had reported a confirmed fault after the first miss, would your third-round decision have changed?",
        "If the partner-force liaison's report had come through your own chain instead, would you have weighted it differently?",
        "If this had been the squadron's first-ever danger-close run with you, would you have set the same margin?",
        "If the sector had a recent history of confirmed enemy activity, would one sensor cue have been enough for you?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "gf_01",
        "bias": "Gamblers Fallacy",
        "decision_point": 1,
        "mechanism": "Treating independent artillery/mortar rounds as part of a self-correcting streak, expecting a hit because prior rounds missed",
        "affected_reasoning_operation": "Probabilistic inference about an upcoming independent event",
        "evidence_available_at_time": [
          "Two prior adjustment rounds landed short",
          "No confirmed fault yet identified in the gun line"
        ],
        "required_textual_manifestation": "FSO explicitly reasons that because the last two rounds missed, the next one is likely to hit, rather than ordering a data recheck",
        "plausible_nonbias_interpretation": "Time pressure before the assault window justified skipping a re-lay check as an acceptable risk trade-off",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "streak", "independent probability"]
      },
      {
        "instance_id": "ig_01",
        "bias": "Ingroup Preference bias or In-group bias",
        "decision_point": 2,
        "mechanism": "Discounting an equally credible report because it originates from an outside unit rather than the FSO's own chain",
        "affected_reasoning_operation": "Weighting and integration of two competing evidence sources",
        "evidence_available_at_time": [
          "Battalion JTAC (same service/unit) reports Grid A",
          "Partner-force liaison reports Grid B with similar confidence caveats"
        ],
        "required_textual_manifestation": "FSO states or implies that the battalion JTAC's grid was trusted more simply because it came through his own unit's channel",
        "plausible_nonbias_interpretation": "The battalion JTAC's report may have used a more familiar reporting format that was easier to verify quickly",
        "strength": "subtle",
        "do_not_make_explicit": ["in-group", "own unit trust", "outgroup discount"]
      },
      {
        "instance_id": "ob_01",
        "bias": "Optimism bias",
        "decision_point": 3,
        "mechanism": "Underestimating the risk of a tighter-than-usual danger-close margin because recent strikes with the same squadron succeeded",
        "affected_reasoning_operation": "Risk assessment and forecasting of mission outcome",
        "evidence_available_at_time": [
          "Recent history of clean CAS strikes with this squadron",
          "Current margin tighter than normal and comms dropouts with lead squad"
        ],
        "required_textual_manifestation": "FSO expresses confidence the run would go fine like the recent strikes, despite the tighter margin and comms issue",
        "plausible_nonbias_interpretation": "The squadron's demonstrated proficiency was a legitimate factor supporting a calculated risk decision",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "unrealistic confidence", "overestimate success odds"]
      },
      {
        "instance_id": "brn_01",
        "bias": "Base-rate neglect",
        "decision_point": 4,
        "mechanism": "Approving fires on a single sensor cue while ignoring the sector's low historical enemy-activity rate and the sensor's known false-positive rate",
        "affected_reasoning_operation": "Updating a target-identification judgment given prior probability and current evidence",
        "evidence_available_at_time": [
          "Single 'possible enemy activity' sensor cue",
          "Sector's historically low/quiet enemy-activity pattern",
          "Sensor's known history of false positives in this terrain"
        ],
        "required_textual_manifestation": "FSO approves the mission based mainly on the cue without weighing how rarely this sector or sensor type produces genuine hits",
        "plausible_nonbias_interpretation": "Time pressure before the assault window made a single strong cue an acceptable basis for action given mission urgency",
        "strength": "subtle",
        "do_not_make_explicit": ["base rate", "prior probability", "false positive rate"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control requested."
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
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Each of the four manifest biases is embedded exactly once, at a distinct decision point.",
      "No bias labels, definitions, or psychological terminology appear in probes or narrative.",
      "Each instance has an available plausible non-bias explanation to avoid mechanical proof of bias.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points, probe coverage, and chronological narrative without repetitive exposition.",
      "Consequences described (round results, strike outcomes, post-strike assessment) do not confirm or deny bias presence mechanically."
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
