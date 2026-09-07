You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "RT_Counterfactual_5",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Project Manager / Capital Projects Manager (Rail Infrastructure)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Corridor Interlocking Replacement: Schedule, Survey Commissioned, and Grant-Deadline Pressure (Counterfactual)",
    "scenario_summary_internal": "Paired counterfactual to RT_Biased_5. The Capital Projects Manager oversees the same design-build interlocking replacement on the same commuter corridor, under the same federal grant obligation deadline. The single causal variable changed is that the PM commissions an updated utility/geotechnical survey before finalizing the baseline schedule (rather than skipping it). The survey reduces but does not eliminate downstream risk: it flags one segment with a stated position tolerance rather than a fully unknown conduit. The PM still absorbs the added survey time by compressing later phases, still treats the survey's residual tolerance caveat as adequately managed by field inspection process rather than contingency, still underreacts to the contractor's subsequent risk report, and still compresses systems-integration testing under the funding deadline. All other material facts, actors, and the four-decision-point structure are held constant relative to RT_Biased_5.",
    "occupational_realism": {
      "objective": "Deliver a signal/interlocking replacement on a commuter rail corridor on schedule and within the federal grant's obligation window, while maintaining safety-critical testing standards.",
      "setting": "Mid-size regional commuter rail agency; design-build capital project; corridor with active revenue service requiring possession/outage windows for construction.",
      "constraints": [
        "Fixed federal grant obligation deadline with risk of partial defunding on slippage",
        "Limited track possession/outage windows shared with revenue operations",
        "Fixed-price design-build contract with limited change-order flexibility",
        "Aging corridor with a legacy utility survey that carries a stated position tolerance in at least one segment",
        "PM's competing obligations to board reporting, grant compliance officer, and field operations"
      ],
      "stakeholders": [
        "Capital Projects Manager (interviewee)",
        "Design-build contractor project manager",
        "Agency chief engineer",
        "Signal/systems integration engineering lead",
        "Grants and compliance officer",
        "Rail operations/dispatch department",
        "Utility survey firm",
        "Federal grant administrator"
      ],
      "technical_terms_to_use": [
        "interlocking replacement",
        "signal cutover",
        "positive train control (PTC) interface",
        "utility/geotechnical survey",
        "position tolerance zone",
        "pothole/field verification",
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
          "Actual crew productivity later trails the plan, consistent with the historical range the PM had access to at baseline",
          "The added survey time from phase 2 is absorbed by compressing later construction phases rather than extending the external target date"
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
          "Contractor flags several uncertain conduit locations near the planned bore path",
          "An updated survey would cost $150K and add three weeks to baseline",
          "PM has established a weekly risk-review and change-order tracking process"
        ],
        "new_information_after_decision": [
          "The commissioned survey identifies most conduit locations but reports a stated horizontal position tolerance of about two feet in one segment due to poor legacy municipal records",
          "PM's team treats the tolerance caveat as adequately covered by field verification during excavation rather than allocating contingency budget or schedule for that segment",
          "Mid-construction, crews still encounter a conduit conflict within the tolerance-flagged segment, triggering a shorter safety stand-down than an entirely unmapped strike would cause"
        ],
        "alternatives": [
          "Commission the updated survey and additionally fund contingency/extra field-verification time for any segment reported with position tolerance",
          "Commission the updated survey and rely on the existing weekly risk-review cadence and field crews to resolve any reported tolerance issues as they arise"
        ],
        "intended_action": "PM commissions the survey but, on seeing the tolerance caveat, elects not to add contingency budget or schedule for that segment, judging that inspection and field-verification practice already in place will resolve any residual placement uncertainty."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Contractor delivers a risk/cost report following the tolerance-zone conflict, projecting roughly a 6 percent cost overrun and about four weeks of schedule impact",
          "Report requires PM sign-off within five business days",
          "PM's calendar is consumed by quarterly board preparation"
        ],
        "new_information_after_decision": [
          "The overrun risk compounds modestly over the following weeks before it is escalated",
          "The agency later requests a smaller schedule accommodation from the grant administrator than in the fully unmapped-strike scenario"
        ],
        "alternatives": [
          "Block dedicated time to fully review the report and convene a risk workshop with the engineering lead",
          "Skim the executive summary, delegate detailed review, and continue the existing reporting cadence without escalating"
        ],
        "intended_action": "PM defers detailed engagement with the report's underlying analysis because the figures are unwelcome heading into board season, delegates review without requesting a substantive readout, and does not escalate to leadership or the grant administrator during the sign-off window."
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
        "intended_action": "PM frames the decision around not losing the already-secured $4M and compresses the testing timeline, indicating the choice would likely have gone the other way if the same amount had been an unrealized upside rather than funding already in hand."
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
        "Once you had the survey results, what did you do with the tolerance-zone finding?",
        "When the contractor's risk report came in, what was your process for reviewing it and deciding next steps?",
        "How did you weigh the testing protocol recommendation against the grant deadline pressure?",
        "How much time pressure did you feel at each of these moments, and how did that affect your options?",
        "What was your level of uncertainty at each decision, and how did you handle it?",
        "Had you faced a similar situation before? How did that experience shape your choice this time?"
      ],
      "closing_hypotheticals": [
        "What additional information about the tolerance zone would have changed your decision not to add contingency?",
        "If the $4 million had been an upside you might gain rather than funding you already had, would the testing decision have changed?",
        "Looking back, was the tolerance-zone conflict something the team could have anticipated at the time?",
        "What would you tell a peer facing a similar fixed-price, fixed-deadline project?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "decision_point": 1,
        "mechanism": "PM anchors the baseline schedule on the contractor's best-case productivity estimate while discounting the distribution of durations from comparable historical projects that were available at the time.",
        "affected_reasoning_operation": "Estimation/forecasting of project duration",
        "evidence_available_at_time": [
          "Contractor's optimistic productivity-based proposal",
          "Historical duration range (28-34 months) from peer agency projects"
        ],
        "required_textual_manifestation": "PM explains choosing the 24-month schedule primarily by citing the contractor's proposal and board pressure, while acknowledging but setting aside the historical range as not fully comparable, and later absorbs the survey's added three weeks by compressing later phases rather than revising the external target.",
        "plausible_nonbias_interpretation": "PM could argue the peer projects had different scope or team composition, making the shorter estimate a reasonable domain judgment rather than a forecasting error.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "underestimation bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Control",
        "decision_point": 2,
        "mechanism": "Having commissioned the survey, PM substitutes confidence in field-verification/inspection practice for actually reducing the residual, explicitly stated position-tolerance uncertainty in one segment, treating routine process as equivalent to control over an acknowledged data limitation.",
        "affected_reasoning_operation": "Risk evaluation and resource allocation in response to a qualified (not absent) data source",
        "evidence_available_at_time": [
          "Survey report showing most conduits located but one segment with a stated ~2-foot position tolerance",
          "Existence of PM's weekly risk-review and field-inspection process",
          "Availability of an option to fund contingency/extra field verification for that segment"
        ],
        "required_textual_manifestation": "PM states that the tolerance caveat did not warrant added contingency because field crews would verify positions during excavation as a matter of course, framing standard inspection practice as sufficient to resolve a known, quantified uncertainty rather than as one imperfect mitigation among others.",
        "plausible_nonbias_interpretation": "PM could argue that a two-foot tolerance is a minor, routine finding not warranting special budget, making the choice an ordinary risk-tolerance judgment rather than an overestimate of control.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control", "overconfidence in process"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Hindsight Bias",
        "decision_point": 2,
        "mechanism": "In a retrospective probe about the tolerance-zone conflict, PM recalls the conflict as obviously predictable given that the survey itself flagged the tolerance, which is inconsistent with the team's contemporaneous risk register that had rated that segment as low residual risk once surveyed.",
        "affected_reasoning_operation": "Retrospective causal attribution / memory reconstruction of past uncertainty",
        "evidence_available_at_time": [
          "Contemporaneous risk-register entry rating the tolerance-flagged segment as low residual risk",
          "Post-hoc knowledge of the actual conduit conflict"
        ],
        "required_textual_manifestation": "When asked to reflect on the conflict, PM says something like the survey literally told them that segment was uncertain, so of course something turned up there, which contradicts the low-residual-risk rating the team itself assigned after receiving the survey.",
        "plausible_nonbias_interpretation": "PM could be expressing legitimate updated risk literacy about tolerance zones for future projects rather than misremembering the foreseeability of this specific outcome.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "creeping determinism"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Ostrich Effect",
        "decision_point": 3,
        "mechanism": "Facing an unfavorable, quantified risk/cost report, PM avoids engaging with its underlying data because the figures are unwelcome ahead of board season, skims the summary, delegates without requesting a substantive readout, and does not escalate within the required review window.",
        "affected_reasoning_operation": "Information-seeking and evidence engagement under threat of unfavorable news",
        "evidence_available_at_time": [
          "Contractor risk/cost report projecting a 6 percent overrun and roughly four-week delay",
          "Five-business-day sign-off window",
          "PM's own calendar constraints"
        ],
        "required_textual_manifestation": "PM states that the figures were unwelcome enough that reviewing and escalating them before the next monitoring update felt premature, describes reading only the executive summary, delegating without requesting a detailed readout, and not escalating during the window.",
        "plausible_nonbias_interpretation": "PM could argue that delegation and awaiting the next monitoring cycle reflected legitimate workload triage given competing board-reporting duties, not avoidance of bad news.",
        "strength": "moderate",
        "do_not_make_explicit": ["ostrich effect", "avoidance of negative information"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Aversion or Loss Framing effect",
        "decision_point": 4,
        "mechanism": "PM frames the testing-schedule decision around avoiding the loss of already-secured $4M in grant funding, and when probed with an equivalent-gain framing, indicates the decision would likely differ if the same amount were an unrealized upside rather than funding already in hand, revealing asymmetric weighting rather than a symmetric cost-benefit calculation.",
        "affected_reasoning_operation": "Tradeoff evaluation between funding risk and safety/reliability protocol completeness",
        "evidence_available_at_time": [
          "Grants officer's statement that a slip risks ~$4M defunding of already-committed money",
          "Signal engineering lead's recommendation for the full eight-week protocol",
          "Six weeks remaining before the deadline"
        ],
        "required_textual_manifestation": "PM explicitly states the decision was driven by not wanting to lose funding already secured, and in response to a probe about an equivalent potential gain, states the full protocol would probably have been kept in that scenario, showing the loss framing rather than the dollar amount alone drove the choice.",
        "plausible_nonbias_interpretation": "PM could argue the compressed protocol still met minimum safety-certification requirements, making this a defensible resource-constrained engineering tradeoff rather than a framing-driven distortion.",
        "strength": "moderate",
        "do_not_make_explicit": ["loss aversion", "loss framing", "prospect theory"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "RT_Biased_5",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the counterfactual condition, not a zero-bias control."
    },
    "counterfactual_specification": {
      "causal_variable": "Whether the Capital Projects Manager commissions an updated utility/geotechnical survey before finalizing the fixed-price baseline schedule",
      "original_state": "In the paired scenario (RT_Biased_5), the survey is not commissioned; the schedule is finalized using outdated (5+ year old) utility maps",
      "counterfactual_state": "The survey is commissioned; it identifies most utility locations but reports a stated position tolerance in one segment, which the PM treats as adequately managed by field-verification practice rather than by allocating contingency",
      "variables_to_hold_constant": [
        "Grant obligation deadline (30 months) and $4M defunding risk",
        "Contractor identity and fixed-price contract structure",
        "Agency staffing and PM's role/authority",
        "Corridor location and general utility-age profile",
        "Occurrence of a utility-related disruption at decision point 2, though at reduced magnitude",
        "Presence of the contractor risk report at decision point 3 and the testing-compression decision at decision point 4"
      ],
      "expected_causal_difference": "Commissioning the survey reduces the severity of the mid-construction disruption (a shorter stand-down tied to a flagged tolerance zone rather than a fully unmapped strike) and correspondingly scales down the contractor's subsequent risk/cost report, but it does not eliminate the underlying risk-management gap, the report-handling avoidance, or the funding-driven testing compression, because those depend on separate decisions rather than on survey commissioning alone.",
      "causal_test_question": "Does commissioning the utility survey primarily change the magnitude and character of the downstream disruption, while leaving the risk-report handling and testing-compression decisions structurally similar to the paired scenario?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and each has at least two plausible alternatives.",
      "Confirm each of the 5 planned instances is tied to a single, identifiable decision/inference/probe response with distinguishable evidence.",
      "Confirm no bias term, definition, or explicit psychological label appears in the drafted interview text.",
      "Confirm cb_02 and cb_03 at decision point 2 use different reasoning operations (in-the-moment resource-allocation judgment vs. retrospective causal attribution) and different evidence traces.",
      "Confirm the survey is explicitly commissioned in this scenario and that this is the only material fact changed relative to RT_Biased_5's survey decision.",
      "Confirm the interview does not imply the survey deterministically prevented all disruption; only that it changed the disruption's severity and character.",
      "Confirm word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points, probe plan, and 5 embedded instances without repetitive exposition.",
      "Confirm consequences at each decision point are consistent with either a biased or a reasonable-judgment account (non-mechanical proof of bias).",
      "Confirm cb_04 and cb_05 include enough explicit contrast (threat-motivated deferral language; equivalent-gain probe and response) to be independently identifiable without naming the bias."
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
