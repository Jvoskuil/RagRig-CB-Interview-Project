You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HE_Biased_6",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Emergency Response/Incident Commander (Industrial Fire Brigade)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Tank Farm Solvent Fire — Offensive Commitment Under Escalating Thermal Warning",
    "scenario_summary_internal": "An industrial fire brigade Incident Commander responds to a fire in a four-tank solvent storage/blending area at a chemical processing site. The IC initially frames the event as a routine, contained tank fire similar to one handled successfully years earlier, commits an offensive foam attack, and progressively resists tactical reassessment as new hazmat, structural, and thermal data accumulate, while command-post and mutual-aid social dynamics reinforce continuation of the original plan until a final withdrawal-timing decision.",
    "occupational_realism": {
      "objective": "Extinguish or control the tank fire and prevent catastrophic tank shell failure while protecting brigade personnel and adjacent production assets, without a mechanically 'wrong' outcome revealing bias.",
      "setting": "Onsite industrial fire brigade responding to a fire in a bunded above-ground storage tank (AST) farm at a chemical processing/solvent blending facility, with municipal mutual aid engine companies supporting on a shared radio net.",
      "constraints": [
        "Limited initial information on exact tank contents pending hazmat/manifest confirmation",
        "Light, variable wind affecting smoke and vapor dispersion",
        "Personnel and hoselines already committed to close-quarters positions",
        "Time pressure from rising shell temperature indicators",
        "Multiple radio channels with municipal mutual aid officers weighing in",
        "Command post staffed by IC, safety officer, and hazmat/structural specialist"
      ],
      "stakeholders": [
        "Incident Commander (interviewee)",
        "Plant control room operator",
        "Hazmat technician",
        "Structural/process safety engineer",
        "Safety officer at command post",
        "Municipal mutual aid engine company officers",
        "Interior attack crews"
      ],
      "technical_terms_to_use": [
        "defensive perimeter",
        "master stream/monitor",
        "shell temperature indicator",
        "exposure protection",
        "incident action plan (IAP)",
        "bunded area",
        "radiant heat",
        "foam concentrate",
        "exclusion zone",
        "size-up"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "groupthink",
        "sunk cost",
        "framing"
      ],
      "excluded_themes": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch report describes a 'contained flammable liquid tank fire' with dark smoke",
          "IC's visual size-up shows a smoke column resembling a tank fire he successfully controlled with offensive foam attack three years earlier",
          "Tank farm manifest not yet confirmed; four tanks present with differing contents",
          "Wind light and variable"
        ],
        "new_information_after_decision": [
          "Hazmat technician arrives and reports the specific burning tank holds a more volatile solvent mixture than the one from the earlier incident the IC recalled"
        ],
        "alternatives": [
          "Launch immediate offensive foam attack with exposure protection lines while confirming contents",
          "Establish a defensive stand-off perimeter and hold attack until tank contents and manifest are verified"
        ],
        "intended_action": "IC commits crews to an offensive attack, treating the fire as functionally identical to the earlier successful incident and accepting the dispatcher's 'contained' characterization as the operative risk frame."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Thermal imaging and shell temperature alarms show a rising trend on the burning tank",
          "Two crews and hoselines already positioned within 15 meters under the original plan",
          "IAP has been reviewed only once, at the initial size-up"
        ],
        "new_information_after_decision": [
          "Structural/hazmat specialist flags an accelerating temperature trend on the adjacent (second) tank as a possible early warning sign"
        ],
        "alternatives": [
          "Withdraw interior crews to a defensive perimeter and switch to unmanned monitor streams",
          "Continue current offensive positions and reinforce with an additional foam line"
        ],
        "intended_action": "IC keeps crews in their committed interior positions and reinforces rather than withdrawing, without formally revisiting the IAP against the new alarm data."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Multiple municipal mutual-aid officers on the shared radio net voice support for continuing the interior foam attack",
          "Safety officer at the command post raises a verbal concern about exposure risk to interior crews",
          "Command post discussion is brief; no formal risk re-assessment log is opened"
        ],
        "new_information_after_decision": [
          "A relief crew reports visible bulging or vibration on the adjacent tank shell"
        ],
        "alternatives": [
          "Escalate to full site evacuation and adopt a defensive-only stance",
          "Maintain the current offensive plan, consistent with the on-net consensus"
        ],
        "intended_action": "IC affirms continuation of the offensive plan based on the audible agreement of multiple mutual-aid officers, and the command post reaches quick unanimous agreement without substantively engaging the safety officer's objection."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "A 20-minute instrument trend log shows a steady, repeatedly radioed rise in shell temperature on the adjacent tank",
          "A spotter's single, most recent verbal report states the tank 'looks stable now' based on a brief visual check"
        ],
        "new_information_after_decision": [
          "Outcome is ambiguous: the tank vents without catastrophic failure, but post-incident review cannot cleanly attribute this to the timing decision"
        ],
        "alternatives": [
          "Order immediate full withdrawal based on the sustained instrument trend",
          "Delay the withdrawal order, weighting the spotter's latest verbal update"
        ],
        "intended_action": "IC delays the withdrawal order, giving the most recent single verbal report more practical weight than the accumulated instrument trend data."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you saw and were told as you arrived on scene.",
        "What was your primary objective when you took command?"
      ],
      "timeline_reconstruction": [
        "What happened right after your initial strategy decision, phase by phase?",
        "At what points did new information arrive, and from which source?",
        "How did your read of the situation change (or not change) as the incident progressed?"
      ],
      "decision_point_probes": [
        "What options did you consider at that moment, and why did you choose the one you did?",
        "What specific cues or reports drove that call?",
        "Had you seen a similar situation before, and did that influence you here?",
        "How much time pressure did you feel at that point?",
        "How confident were you in the information you were acting on?",
        "Did anyone on scene or on the radio express a different view, and how was that handled?"
      ],
      "closing_hypotheticals": [
        "If the hazmat report had come in before you committed crews, would your initial call have differed?",
        "If the mutual-aid officers on the net had been silent or split, would phase three have gone differently?",
        "Looking back, what single piece of information do you wish had carried more weight at the end?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "rh_01",
        "bias": "Representative heuristic",
        "decision_point": 1,
        "mechanism": "IC classifies the current fire as belonging to the same category as a prior successfully-resolved tank fire based on superficial visual similarity (smoke color/column shape), overriding the need to verify base-rate-relevant differences (contents, tank design).",
        "affected_reasoning_operation": "Situation classification / analogical categorization prior to strategy selection",
        "evidence_available_at_time": ["Visual smoke column resembling a prior incident", "Unconfirmed tank contents manifest"],
        "required_textual_manifestation": "IC explicitly links the current smoke/appearance to the specific earlier fire and treats that resemblance as sufficient basis for applying the same offensive tactic, before contents are confirmed.",
        "plausible_nonbias_interpretation": "Experienced pattern-based size-up is a legitimate, trained skill; using prior experience is not inherently biased.",
        "strength": "subtle",
        "do_not_make_explicit": ["representative heuristic", "base rate", "pattern-matching bias"]
      },
      {
        "instance_id": "fr_01",
        "bias": "Framing effect",
        "decision_point": 1,
        "mechanism": "The dispatcher's verbal label 'contained flammable liquid tank fire' anchors the IC's risk framing toward a low-severity, manageable-event schema, shaping the offensive/defensive choice independently of the visual and manifest ambiguity.",
        "affected_reasoning_operation": "Initial risk framing / threat categorization from a verbal report",
        "evidence_available_at_time": ["Dispatch radio language describing the event as 'contained'"],
        "required_textual_manifestation": "IC recalls the dispatcher's specific wording and describes treating it as an accurate characterization of severity that shaped the choice of an offensive posture.",
        "plausible_nonbias_interpretation": "Dispatch information is a normal, necessary input to size-up and reasonably guides initial posture.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "anchoring on wording"]
      },
      {
        "instance_id": "sc_01",
        "bias": "Sunk cost bias",
        "decision_point": 2,
        "mechanism": "IC's decision to keep crews in committed interior positions is justified partly by reference to resources already deployed (crews, hoselines) rather than solely by the current risk data.",
        "affected_reasoning_operation": "Resource-continuation decision under new alarm data",
        "evidence_available_at_time": ["Two crews and hoselines already positioned within 15m", "Rising shell temperature alarm"],
        "required_textual_manifestation": "IC references the existing commitment of crews/hoselines as a reason to continue and reinforce rather than withdraw, in response to the new thermal data.",
        "plausible_nonbias_interpretation": "Repositioning committed crews has real operational cost and risk, so caution about immediate withdrawal can be a reasonable tactical judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment"]
      },
      {
        "instance_id": "sq_01",
        "bias": "Status quo bias",
        "decision_point": 2,
        "mechanism": "The command team continues the original IAP without formally revisiting it against the new alarm data, defaulting to 'no change' absent an explicit prompt to reassess, distinct from the resource-justification reasoning of sc_01.",
        "affected_reasoning_operation": "Plan-maintenance decision / failure to trigger IAP re-evaluation",
        "evidence_available_at_time": ["IAP reviewed only once at initial size-up", "New structural/hazmat flag on adjacent tank"],
        "required_textual_manifestation": "IC describes not reopening or formally reassessing the IAP despite the new specialist flag, treating the original plan as the default absent a strong forcing event.",
        "plausible_nonbias_interpretation": "Continuous re-planning during active suppression can itself be disruptive; sticking with a plan can reflect disciplined execution.",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "default option", "inertia"]
      },
      {
        "instance_id": "bw_01",
        "bias": "Bandwagon Effect",
        "decision_point": 3,
        "mechanism": "IC weights the tactical judgment of continuing the offensive attack more heavily because multiple mutual-aid officers on the shared radio net vocally support it, treating the number of agreeing voices as evidence of correctness.",
        "affected_reasoning_operation": "Evidence-selection / social-proof-driven inference from radio traffic",
        "evidence_available_at_time": ["Multiple mutual-aid officers voicing agreement on the net"],
        "required_textual_manifestation": "IC cites the fact that several other officers agreed on the radio as a reason reinforcing the continuation decision, separate from the command-post internal dynamics.",
        "plausible_nonbias_interpretation": "Peer officers' input is a legitimate collaborative input in multi-agency incidents.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon effect", "social proof", "peer consensus bias"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "Within the internal command post, the safety officer's dissenting concern is raised but not substantively engaged, and the small command team reaches rapid unanimous agreement, reflecting suppressed dissent and an illusion of unanimity distinct from the external radio-based bw_01 dynamic.",
        "affected_reasoning_operation": "Internal group deliberation / dissent handling in the command post",
        "evidence_available_at_time": ["Safety officer's verbal exposure-risk concern at the command post", "Absence of a formal risk re-assessment log"],
        "required_textual_manifestation": "IC describes the command post's brief internal discussion in which the safety officer's concern is acknowledged but not pursued, and the team quickly aligns on continuing.",
        "plausible_nonbias_interpretation": "Efficient, decisive command-post communication is valued during active incidents and can look similar to suppressed dissent without being biased.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "illusion of unanimity", "self-censorship"]
      },
      {
        "instance_id": "mr_01",
        "bias": "Modality effect or Recency effect",
        "decision_point": 4,
        "mechanism": "IC gives disproportionate practical weight to the single most recently received verbal report ('looks stable now') relative to a 20-minute, repeatedly radioed instrument trend showing a steady temperature rise, when timing the withdrawal order.",
        "affected_reasoning_operation": "Final evidence-weighting / withdrawal-timing decision",
        "evidence_available_at_time": ["20-minute logged instrument trend of rising shell temperature", "Single most recent spotter verbal report of apparent stability"],
        "required_textual_manifestation": "IC explains delaying the withdrawal call by referencing the latest verbal update as more decisive than the accumulated trend data leading up to it.",
        "plausible_nonbias_interpretation": "A trained visual spotter's real-time report is a legitimate, sometimes more current, data point than a lagging instrument trend.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "modality effect", "most recent information bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable — condition is 'biased', not a control condition."
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
      "Confirm exactly 4 decision points are present in the timeline",
      "Confirm each of the 7 instance IDs maps to exactly one decision point and one distinct evidence source",
      "Confirm decision points 1, 2, and 3 each carry exactly two instances with clearly distinct evidence sources or reasoning operations, and decision point 4 carries exactly one",
      "Confirm no bias term, definition, or explicit psychological label appears in any interviewee-facing text",
      "Confirm each instance has a plausible non-bias interpretation available in the narrative",
      "Confirm consequences at the end (tank vents without catastrophic failure) do not mechanically prove or disprove any bias",
      "Confirm total word count target of 1,350 (range 1,215–1,485) is achievable given 4 decision points, probes, and 7 non-repetitive instance manifestations"
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
