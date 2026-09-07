You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Biased_5",
  "domain_id": "EM",
  "domain": "Emergency management and Civil Protection",
  "role": "Incident Commander (Structural Fire/Hazmat Response)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Riverside Industrial Park: Structural Fire with Concealed Chemical Storage",
    "scenario_summary_internal": "An Incident Commander responds to a reported small trash fire at a mixed-use industrial building (auto-parts retail front, rear warehouse storing unlabeled solvent/chemical drums). Over roughly 40 minutes, the incident escalates from a routine knockdown to a multi-company hazmat-involved structural fire with an uncertain chemical identity, a shifting wind threatening a nearby residential block, and a partially searched structure. The interview reconstructs four sequential decisions the IC made under time pressure, incomplete information, and social/organizational pressure from arriving mutual aid officers.",
    "occupational_realism": {
      "objective": "Achieve life safety for occupants and crews, contain the fire, prevent an uncontrolled chemical release, and protect nearby exposures while resources build up on scene.",
      "setting": "Early evening, single-story industrial park unit with a retail auto-parts storefront and an attached rear warehouse used for solvent and chemical storage; residential block approximately 200m downwind; intermittent radio/dispatch reliability.",
      "constraints": [
        "Only two engines, one truck, and one battalion chief on scene at initial size-up",
        "Original dispatch information described the incident as a small exterior trash fire",
        "Chemical storage manifest for the rear warehouse is incomplete and partially fire-damaged",
        "Wind direction shifts mid-incident toward a residential area",
        "Night manager/occupant is present but shaken and gives inconsistent statements",
        "Search team fatigue increases after 30+ minutes of interior operations",
        "Mutual aid battalion chief arrives and begins directing perimeter decisions alongside the IC"
      ],
      "stakeholders": [
        "Incident Commander (interviewee)",
        "First-arriving engine company officer",
        "Hazmat technician assigned to identify chemical contents",
        "Mutual aid battalion chief",
        "Interior search team",
        "Night shift facility manager/occupant",
        "Dispatch center"
      ],
      "technical_terms_to_use": [
        "size-up",
        "offensive strategy",
        "defensive strategy",
        "NFPA 704 placard",
        "exposure",
        "isolation perimeter",
        "PPE level",
        "IDLH",
        "staging area",
        "unified command",
        "personnel accountability report (PAR)",
        "decon corridor",
        "Emergency Response Guidebook (ERG)"
      ],
      "technical_terms_to_avoid": [
        "anchoring",
        "confirmation bias",
        "framing effect",
        "bandwagon effect",
        "hindsight bias",
        "cognitive bias",
        "heuristic",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch reported 'small trash fire, rear alley' with no mention of chemical storage",
          "Light-to-moderate smoke column visible from the street on arrival",
          "No prior incident history at this address in dispatch notes"
        ],
        "new_information_after_decision": [
          "Heavier smoke and a chemical odor detected once the first crew reaches the rear of the building",
          "Visible drums are discovered stacked against the rear wall, some showing fire exposure"
        ],
        "alternatives": [
          "Commit a single attack line immediately for a quick knockdown consistent with the dispatched call type",
          "Hold the initial line at a defensive stand-off distance and complete a full 360-degree size-up, including the rear of the structure, before committing"
        ],
        "intended_action": "The IC commits the first-arriving crew to an offensive quick-knockdown attack based on the dispatched description, without confirming rear-of-building conditions first."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "A partially obscured NFPA diamond is visible on one drum; some hazard numbers are unreadable due to rust and fire damage",
          "The hazmat technician's preliminary read suggests a common solvent (consistent with items normally sold in the retail front)",
          "The night manager states, inconsistently, that 'something different' is stored in that section of the warehouse"
        ],
        "new_information_after_decision": [
          "A second, fully intact placard is later located on an adjacent drum showing a different hazard class than initially assumed",
          "The manifest fragment recovered from an office file cabinet does not match the assumed solvent"
        ],
        "alternatives": [
          "Pause PPE and tactical decisions until the placard and manifest can be independently cross-checked against the ERG",
          "Proceed with the preliminary solvent identification and select PPE/extinguishing agent consistent with that assumption"
        ],
        "intended_action": "The IC and hazmat technician treat the ambiguous placard reading as consistent with the assumed common solvent, discount the occupant's contradicting statement as unreliable, and proceed with PPE and foam selection built around that assumption."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The first-arriving officer set an initial 150-meter isolation perimeter before wind data was considered",
          "Multiple mutual aid units and the arriving battalion chief have already begun operating and staging based on the 150-meter line",
          "Wind direction has begun shifting toward the residential block, though the shift is not yet fully confirmed"
        ],
        "new_information_after_decision": [
          "Wind shift is confirmed by a later weather update",
          "Air monitoring near the edge of the established perimeter shows readings close to the action threshold, prompting a last-minute perimeter adjustment"
        ],
        "alternatives": [
          "Independently recalculate the isolation distance using current wind data and the ERG guidance for the (still-uncertain) chemical",
          "Adopt the perimeter already agreed upon by the first-arriving officer and endorsed by the incoming battalion chief and other units"
        ],
        "intended_action": "Despite personal uncertainty about whether 150 meters is sufficient given the wind shift, the IC defers to the perimeter already accepted and reinforced by multiple arriving officers rather than independently recalculating it."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Interior search team reports approximately 90% of the structure has been cleared",
          "The remaining unsearched area is a small storage room adjacent to the drum stack",
          "Crew fatigue is visibly increasing after more than 30 minutes of interior work",
          "Chemical identity and drum integrity in that area remain unresolved"
        ],
        "new_information_after_decision": [
          "The final room is found empty of occupants",
          "One drum in that room is later found to be slightly leaking, increasing the exposure that occurred during the extended interior operation"
        ],
        "alternatives": [
          "Withdraw interior crews to defensive/exterior operations given the unresolved chemical risk near the final search area",
          "Send the search team back in to finish clearing the last 10% of the structure quickly"
        ],
        "intended_action": "After the battalion chief frames the choice as 'not wasting the search already completed' rather than as 'entering an unresolved chemical risk area,' the IC authorizes the crew to re-enter and complete the search."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how the call came in and what you knew before you arrived on scene.",
        "What was your overall objective for this incident once you pulled up?"
      ],
      "timeline_reconstruction": [
        "Talk me through what happened, step by step, from arrival to the point crews began interior operations.",
        "At what point did the situation change from what dispatch had described?",
        "What information came in that you didn't have when you first arrived?"
      ],
      "decision_point_probes": [
        "What options did you consider at that point, and why did you choose the one you did?",
        "What specific information were you relying on when you made that call?",
        "Was anyone else's input or agreement part of how you settled on that course of action?",
        "How confident were you in that information at the time, and what would have changed your mind?",
        "How much time pressure were you under when you made that decision?",
        "Had you handled a situation like this before, and did that experience shape your choice?"
      ],
      "closing_hypotheticals": [
        "If you had known earlier what the placard and manifest actually showed, would you have done anything differently?",
        "Looking back now, does anything about how the incident unfolded seem like it should have been obvious at the time?",
        "If the wind hadn't shifted, do you think the perimeter decision would have turned out differently?",
        "What would you tell a newer commander to watch for in a similar call?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "anchor_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Initial strategy commitment is pulled toward the dispatch-provided description ('small trash fire') rather than being adjusted to match the moderate smoke column actually observed on arrival.",
        "affected_reasoning_operation": "Initial size-up and strategy selection (offensive vs. defensive/full assessment)",
        "evidence_available_at_time": [
          "Dispatch description of a small exterior trash fire",
          "Visible moderate smoke column from the street",
          "No stated information yet about rear warehouse contents"
        ],
        "required_textual_manifestation": "IC explicitly references the dispatched call type as the primary basis for committing the initial attack line, and only mentions the smoke column as a secondary or dismissed detail, without describing an independent re-assessment before committing.",
        "plausible_nonbias_interpretation": "A fast offensive knockdown on a small reported fire is a standard, experience-based tactical default; committing quickly could simply reflect efficient triage rather than an anchored estimate.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "initial estimate bias", "adjustment failure"]
      },
      {
        "instance_id": "hindsight_01",
        "bias": "Hindsight bias",
        "decision_point": 1,
        "mechanism": "During retrospective reflection on the same initial strategy decision, the IC characterizes the eventual escalation as something that 'should have been obvious' from the smoke conditions, overstating the foreseeability of the outcome relative to what was actually knowable at the time of the decision.",
        "affected_reasoning_operation": "Retrospective evaluation/causal judgment of a past decision's foreseeability, distinct from the real-time strategy selection itself",
        "evidence_available_at_time": [
          "Outcome knowledge available only at interview time: drums, hazmat escalation, eventual perimeter and search complications",
          "Contemporaneous information that was actually available before phase 1's decision (dispatch call type, limited smoke view)"
        ],
        "required_textual_manifestation": "In response to a closing hypothetical probe, the IC states in substance that the escalation 'should have been obvious' or 'was really there to see' from the early smoke conditions, without acknowledging that this information was not equally clear before the outcome was known.",
        "plausible_nonbias_interpretation": "Experienced commanders often identify genuine early warning signs in retrospect; noting a missed cue could reflect accurate professional learning rather than distorted foreseeability judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight", "foreseeability", "knew-it-all-along", "outcome knowledge distortion"]
      },
      {
        "instance_id": "confirm_01",
        "bias": "Confirmation Bias",
        "decision_point": 2,
        "mechanism": "The ambiguous placard and manifest fragment are interpreted as supporting the initially guessed solvent, while the occupant's contradicting statement is actively discounted rather than weighed as disconfirming evidence.",
        "affected_reasoning_operation": "Evidence weighting and hazard identification during PPE/agent selection",
        "evidence_available_at_time": [
          "Partially obscured NFPA placard consistent with, but not conclusive of, the assumed solvent",
          "Occupant statement suggesting a different chemical is stored in that section",
          "Hazmat technician's preliminary read favoring the common solvent"
        ],
        "required_textual_manifestation": "IC describes treating the unclear placard reading as confirming the initial guess and explicitly gives a reason for setting aside or downplaying the occupant's contrary statement (e.g., citing the occupant's shaken state) rather than seeking independent verification.",
        "plausible_nonbias_interpretation": "Occupant statements during active emergencies are often unreliable, so discounting one contradicting account could reflect sound risk-based judgment rather than selective evidence use.",
        "strength": "moderate",
        "do_not_make_explicit": ["confirmation bias", "selective evidence", "disconfirming evidence", "motivated reasoning"]
      },
      {
        "instance_id": "bandwagon_01",
        "bias": "Bandwagon effect",
        "decision_point": 3,
        "mechanism": "The IC adopts the perimeter distance already set and reinforced by multiple other officers and the mutual aid battalion chief, despite privately holding doubts about its sufficiency given the shifting wind, rather than independently recalculating it.",
        "affected_reasoning_operation": "Perimeter/isolation-distance decision under converging peer agreement",
        "evidence_available_at_time": [
          "150-meter perimeter already established by the first-arriving officer",
          "Multiple additional units and the mutual aid battalion chief operating consistently with that line",
          "Early, not-yet-confirmed indication of a wind shift toward the residential block"
        ],
        "required_textual_manifestation": "IC states that other units and the battalion chief were already operating on the existing perimeter and describes going along with it, while separately acknowledging personal uncertainty about whether the distance was adequate given the wind.",
        "plausible_nonbias_interpretation": "Maintaining a single established perimeter avoids conflicting instructions and confusion across multiple companies, so preserving it could reflect legitimate incident-command coordination rather than social conformity.",
        "strength": "moderate",
        "do_not_make_explicit": ["bandwagon", "social proof", "conformity", "peer pressure"]
      },
      {
        "instance_id": "framing_01",
        "bias": "Framing Effect",
        "decision_point": 4,
        "mechanism": "The decision to re-enter and finish the search is driven by the battalion chief's presentation of the choice as avoiding wasted effort ('not wasting the search already completed') rather than as accepting continued exposure to an unresolved chemical risk; the same factual choice, framed around loss-of-effort, shifts the IC toward the risk-tolerant option.",
        "affected_reasoning_operation": "Risk-based go/no-go decision on completing interior search",
        "evidence_available_at_time": [
          "90% of the structure already cleared",
          "Remaining area adjacent to unresolved drum stack",
          "Battalion chief's verbal framing emphasizing completed effort over remaining risk",
          "Visible crew fatigue"
        ],
        "required_textual_manifestation": "IC recounts the battalion chief's specific framing of the remaining decision (effort-already-invested framing) as a stated reason for authorizing re-entry, rather than independently weighing the unresolved chemical risk on its own terms.",
        "plausible_nonbias_interpretation": "Completing a nearly finished search to confirm no occupants remain is a defensible life-safety priority independent of how the choice was phrased.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "loss framing", "sunk cost of effort", "gain/loss frame"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', no paired control scenario supplied."
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
      "Each decision point includes information available before the decision and new information learned afterward.",
      "Exactly five intended bias instances are planned, one per manifest entry, matching the exact-occurrence rules.",
      "No bias names, definitions, or psychological terminology appear in the planned public interview content.",
      "anchor_01 and hindsight_01 share decision point 1 but involve distinct reasoning operations (real-time estimation vs. retrospective foreseeability judgment) and distinct evidence traces.",
      "Each occurrence has a documented plausible non-bias interpretation to prevent mechanical bias attribution from outcomes.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals as required.",
      "Target interview length of 1,350 words (range 1,215-1,485) is achievable given four decision points and five embedded instances without repetitive exposition."
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
