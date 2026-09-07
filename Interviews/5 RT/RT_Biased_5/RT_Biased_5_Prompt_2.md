You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "RT_Biased_5",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Project Manager / Capital Projects Manager (Rail Infrastructure)",
  "condition": "biased_counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Corridor Interlocking Replacement: Schedule, Survey, and Grant-Deadline Pressure",
    "scenario_summary_internal": "A regional rail agency Capital Projects Manager oversees a design-build replacement of an aging interlocking/signaling system on a busy commuter corridor, funded in part by a federal infrastructure grant with a hard obligation deadline. The PM sets an aggressive baseline schedule, elects to skip an updated utility survey in favor of relying on active oversight processes, later underreacts to a contractor risk report flagging cost/schedule overrun after an unmapped utility strike, and finally compresses systems-integration testing to protect grant funding as the deadline nears. The interview reconstructs these four decisions retrospectively.",
    "occupational_realism": {
      "objective": "Deliver a signal/interlocking replacement on a commuter rail corridor on schedule and within the federal grant's obligation window, while maintaining safety-critical testing standards.",
      "setting": "Mid-size regional commuter rail agency; design-build capital project; corridor with active revenue service requiring possession/outage windows for construction.",
      "constraints": [
        "Fixed federal grant obligation deadline with risk of partial defunding on slippage",
        "Limited track possession/outage windows shared with revenue operations",
        "Fixed-price design-build contract with limited change-order flexibility",
        "Aging, incompletely documented underground utility infrastructure in the corridor",
        "PM's competing obligations to board reporting, grant compliance officer, and field operations"
      ],
      "stakeholders": [
        "Capital Projects Manager (interviewee)",
        "Design-build contractor project manager",
        "Agency chief engineer",
        "Signal/systems integration engineering lead",
        "Grants and compliance officer",
        "Rail operations/dispatch department",
        "Third-party utility owners",
        "Federal grant administrator"
      ],
      "technical_terms_to_use": [
        "interlocking replacement",
        "signal cutover",
        "positive train control (PTC) interface",
        "utility conduit conflict",
        "geotechnical/utility survey",
        "fixed-price design-build contract",
        "systems integration testing",
        "possession window",
        "change order",
        "risk register",
        "grant obligation deadline",
        "commissioning protocol"
      ],
      "technical_terms_to_avoid": [
        "aviation-specific terminology",
        "maritime terminology",
        "unrelated software engineering jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Grant obligation deadline is 30 months from project initiation",
          "Comparable interlocking replacement projects at peer agencies took 28-34 months historically",
          "Contractor's proposal assumes best-case crew productivity rates",
          "Agency leadership wants visible grant utilization progress reported to the board"
        ],
        "new_information_after_decision": [
          "Actual crew productivity later trails the plan, consistent with the historical range the PM had access to at baseline"
        ],
        "alternatives": [
          "Adopt an aggressive 24-month baseline schedule to build political margin",
          "Adopt a 30-month baseline schedule anchored to historical analogous project durations"
        ],
        "intended_action": "PM selects the aggressive 24-month schedule, anchoring on the contractor's best-case estimate and discounting historical overrun patterns on comparable projects."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Existing utility maps for the corridor are over five years old",
          "Contractor flags several unmapped conduit locations near the planned bore path",
          "An updated survey would cost $150K and add three weeks to baseline",
          "PM has established a weekly risk-review and change-order tracking process"
        ],
        "new_information_after_decision": [
          "Mid-construction, crews strike an unmapped high-voltage utility duct, triggering a multi-week safety stand-down"
        ],
        "alternatives": [
          "Commission an updated utility/geotechnical survey before finalizing the fixed-price schedule",
          "Proceed on existing maps, relying on the weekly risk-review cadence to catch and manage conflicts as they surface"
        ],
        "intended_action": "PM proceeds without the survey, judging that active weekly oversight and change-order discipline will let the team manage unknown conditions as they arise."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Contractor delivers a 40-page risk/cost report following the utility strike, projecting a 12% cost overrun and 10-week delay",
          "Report requires PM sign-off within five business days",
          "PM's calendar is consumed by quarterly board preparation"
        ],
        "new_information_after_decision": [
          "Overrun risk compounds over the following weeks, eventually requiring formal escalation and a deadline-renegotiation request to the grant administrator"
        ],
        "alternatives": [
          "Block dedicated time to fully review the report and convene a risk workshop with the engineering lead",
          "Skim the executive summary, delegate detailed review, and continue the existing reporting cadence without escalating"
        ],
        "intended_action": "PM defers detailed engagement with the report's underlying analysis, tells the team to 'keep monitoring,' and does not escalate to leadership or the grant administrator at this stage."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Six weeks remain before the grant obligation deadline",
          "Systems integration testing normally requires an eight-week protocol",
          "Signal engineering lead recommends the full eight-week test window",
          "Grants officer states a milestone slip risks roughly $4M in partial defunding"
        ],
        "new_information_after_decision": [
          "Testing completes within the compressed window and the system passes, but with fewer redundant verification cycles; funding is preserved but long-term reliability implications are not yet known at interview time"
        ],
        "alternatives": [
          "Request a formal deadline extension from the grant administrator while completing the full eight-week protocol",
          "Compress testing to five weeks, cutting some redundant verification cycles, to preserve the funding"
        ],
        "intended_action": "PM frames the decision around not losing the $4M and compresses the testing timeline, prioritizing funding preservation over the engineering team's full recommended protocol."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role on this project and what the corridor interlocking replacement was meant to achieve.",
        "What made this project nonroutine compared to prior capital projects you've managed?"
      ],
      "timeline_reconstruction": [
        "Walk me through the project chronologically from initiation to commissioning.",
        "What cues or signals prompted you to move from one phase to the next?",
        "At what point did you first sense the project might not go as planned?"
      ],
      "decision_point_probes": [
        "What information did you have available when you set the baseline schedule, and how did you weigh it?",
        "What alternatives did you consider for the utility survey question, and why did you choose the path you did?",
        "When the contractor's risk report came in, what was your process for reviewing it and deciding next steps?",
        "How did you weigh the testing protocol recommendation against the grant deadline pressure?",
        "How much time pressure did you feel at each of these moments, and how did that affect your options?",
        "What was your level of uncertainty at each decision, and how did you handle it?",
        "Had you faced a similar situation before? How did that experience shape your choice this time?"
      ],
      "closing_hypotheticals": [
        "If you had unlimited budget and time for the utility survey, would you have decided differently?",
        "If the grant deadline had been flexible, would your testing decision have changed?",
        "Looking back, was the utility strike something the team could have anticipated at the time?",
        "What would you tell a peer facing a similar fixed-price, fixed-deadline project?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "decision_point": 1,
        "mechanism": "PM anchors the baseline schedule on the contractor's best-case productivity estimate while discounting the distribution of durations from comparable historical projects that were available to them at the time.",
        "affected_reasoning_operation": "Estimation/forecasting of project duration",
        "evidence_available_at_time": [
          "Contractor's optimistic productivity-based proposal",
          "Historical duration range (28-34 months) from peer agency projects"
        ],
        "required_textual_manifestation": "PM explains choosing the 24-month schedule primarily by citing the contractor's proposal and board pressure, while acknowledging but setting aside the historical range as 'not really comparable to our team.'",
        "plausible_nonbias_interpretation": "PM could argue the peer projects had different scope or team composition, making the shorter estimate a reasonable domain judgment rather than a forecasting error.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "underestimation bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Control",
        "decision_point": 2,
        "mechanism": "PM substitutes confidence in an active management process (weekly risk reviews, change-order tracking) for actually reducing the underlying informational uncertainty (outdated utility maps), treating procedural oversight as equivalent to control over physical/ground conditions.",
        "affected_reasoning_operation": "Risk evaluation and decision to accept incomplete information",
        "evidence_available_at_time": [
          "Outdated utility maps (5+ years old)",
          "Contractor flag of unmapped conduit locations",
          "Existence of PM's weekly risk-review process"
        ],
        "required_textual_manifestation": "PM states that skipping the survey was acceptable because 'we track everything weekly and would catch issues fast,' framing internal process rigor as sufficient to manage an external, unknown physical condition.",
        "plausible_nonbias_interpretation": "PM could argue that time and cost tradeoffs justified accepting the survey gap as a calculated, budget-conscious risk rather than an overestimate of control.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control", "overconfidence in process"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Hindsight Bias",
        "decision_point": 2,
        "mechanism": "In a retrospective probe about the utility strike, PM recalls the conflict as having been 'clearly predictable' given the corridor's age, which is inconsistent with the team's contemporaneous risk register that had rated the utility conflict as low likelihood at the time of the decision.",
        "affected_reasoning_operation": "Retrospective causal attribution / memory reconstruction of past uncertainty",
        "evidence_available_at_time": [
          "Contemporaneous risk register entry rating utility conflict as low likelihood",
          "Post-hoc knowledge of the actual utility strike outcome"
        ],
        "required_textual_manifestation": "When asked to reflect on the strike, PM says something like 'looking back, it was obvious this corridor was going to have hidden utilities—we should have seen it coming,' contradicting the low-likelihood rating the team itself assigned beforehand.",
        "plausible_nonbias_interpretation": "PM could be expressing legitimate updated risk literacy for future projects rather than misremembering the foreseeability of the specific outcome.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "creeping determinism"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Ostrich Effect",
        "decision_point": 3,
        "mechanism": "Facing a detailed adverse risk/cost report, PM avoids engaging with its underlying data (skims summary, delegates without follow-up, does not escalate) rather than confronting the unfavorable information directly, despite having the time-bounded sign-off obligation.",
        "affected_reasoning_operation": "Information-seeking and evidence engagement under threat of unfavorable news",
        "evidence_available_at_time": [
          "40-page contractor risk/cost report projecting 12% overrun and 10-week delay",
          "Five-business-day sign-off window",
          "PM's own calendar constraints"
        ],
        "required_textual_manifestation": "PM describes skimming only the executive summary, delegating the detailed review without following up, and telling the team to 'keep monitoring' instead of opening the full analysis or escalating, despite recognizing the report's seriousness.",
        "plausible_nonbias_interpretation": "PM could argue that delegation was a legitimate time-management choice given competing board-reporting duties, not avoidance of bad news.",
        "strength": "moderate",
        "do_not_make_explicit": ["ostrich effect", "avoidance of negative information"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Aversion or Loss Framing effect",
        "decision_point": 4,
        "mechanism": "PM frames the testing-schedule decision predominantly around avoiding the loss of the $4M in grant funding rather than symmetrically weighing the safety/reliability value of the full test protocol, producing a choice that overweights the framed loss relative to the foregone verification benefit.",
        "affected_reasoning_operation": "Tradeoff evaluation between funding risk and safety/reliability protocol completeness",
        "evidence_available_at_time": [
          "Grants officer's statement that a slip risks ~$4M defunding",
          "Signal engineering lead's recommendation for the full eight-week protocol",
          "Six weeks remaining before the deadline"
        ],
        "required_textual_manifestation": "PM explicitly states the decision was driven by 'we couldn't afford to lose that $4M' and describes compressing testing to preserve funding, giving comparatively little explicit weight to the engineering lead's full-protocol rationale.",
        "plausible_nonbias_interpretation": "PM could argue the compressed protocol still met minimum safety-certification requirements, making this a defensible resource-constrained engineering tradeoff rather than a framing-driven distortion.",
        "strength": "moderate",
        "do_not_make_explicit": ["loss aversion", "loss framing", "prospect theory"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the biased_counterfactual condition, not a control."
    },
    "counterfactual_specification": {
      "causal_variable": "Whether the Capital Projects Manager commissioned an updated utility/geotechnical survey before finalizing the fixed-price baseline schedule",
      "original_state": "Survey requested/considered but not commissioned; baseline schedule and fixed-price contract finalized using outdated (5+ year old) utility maps",
      "counterfactual_state": "PM proceeds to skip the survey entirely, relying on the weekly risk-review/change-order process to manage unmapped-utility risk as it surfaces, rather than resolving the uncertainty upfront",
      "variables_to_hold_constant": [
        "Grant obligation deadline (30 months) and $4M defunding risk",
        "Contractor identity and fixed-price contract structure",
        "Agency staffing and PM's role/authority",
        "Corridor location and general utility-age profile",
        "Occurrence of the eventual utility strike and downstream schedule/cost impacts"
      ],
      "expected_causal_difference": "Skipping the survey (versus commissioning it) removes the three-week/$ 150K upfront cost but leaves the unmapped-conduit risk unresolved, causally enabling the mid-construction utility strike, the subsequent risk-report avoidance at decision point 3, and the funding-driven testing compression at decision point 4.",
      "causal_test_question": "Would the mid-construction utility strike, the cost/schedule overrun, and the compressed testing decision have occurred if the PM had commissioned the updated utility survey before finalizing the baseline schedule?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and each has at least two plausible alternatives.",
      "Confirm each of the 5 planned instances is tied to a single, identifiable decision/inference/probe response with distinguishable evidence.",
      "Confirm no bias term, definition, or explicit psychological label appears in the drafted interview text.",
      "Confirm cb_02 and cb_03 at decision point 2 use different reasoning operations (in-the-moment risk evaluation vs. retrospective causal attribution) and different evidence traces.",
      "Confirm word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points, probe plan, and 5 embedded instances without repetitive exposition.",
      "Confirm consequences at each decision point are consistent with either a biased or a reasonable-judgment account (non-mechanical proof of bias).",
      "Confirm the counterfactual variable holds all other material facts constant and changes only the survey-commissioning decision."
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
