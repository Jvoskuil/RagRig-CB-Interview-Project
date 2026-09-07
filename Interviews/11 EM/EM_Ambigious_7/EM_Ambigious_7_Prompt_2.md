You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Ambigious_7",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Emergency Operations Center (EOC) Situation Unit Analyst",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Twin Forks Flash Flood and Ridge Fire Smoke Incident (Ambiguous Control)",
    "scenario_summary_internal": "Over a 14-hour operational period, a Situation Unit Analyst at a county EOC manages the Common Operating Picture during a compound event: an unplanned high-volume release from Twin Forks Reservoir coincides with a monsoonal storm cell and reduced aerial/sensor visibility from active Ridge Fire smoke. The analyst classifies the threat and sets a warning tier, mobilizes rescue resources, decides on evacuation zone scope using degraded sensor coverage, and later participates in a hot-wash review of the initial decision. All four decisions are genuinely underdetermined by the available evidence, and the analyst's reasoning reflects reasonable, defensible judgment calls under uncertainty rather than any systematic distortion.",
    "occupational_realism": {
      "objective": "Maintain an accurate, timely Common Operating Picture and recommend warning/evacuation/resource decisions that protect life safety under degraded information conditions.",
      "setting": "County Emergency Operations Center, Situation Unit, during a compound flash-flood and wildfire-smoke incident affecting a river-adjacent residential sector (Sector 7-12 watershed).",
      "constraints": [
        "Two of eight stream gauges offline due to smoke-damaged repeater",
        "Duty hydrologist unavailable for first 90 minutes",
        "Aerial reconnaissance limited by wildfire smoke",
        "Dual-hazard workload competing for EOC attention (fire branch and flood branch)",
        "Public messaging must go through a single unified tone to avoid contradicting the dam operator's release notice"
      ],
      "stakeholders": [
        "Twin Forks Reservoir Authority dam operator",
        "EOC Branch Director (flood operations)",
        "Field liaison / incident commander at Sector 7",
        "Fire dispatch (Ridge Fire)",
        "Regional news/social media monitoring desk",
        "Downstream Sector 7-12 residents"
      ],
      "technical_terms_to_use": [
        "Common Operating Picture (COP)",
        "stream gauge threshold",
        "tier-1/tier-2/tier-3 mobilization",
        "advisory vs. warning tier",
        "watershed sub-zone",
        "hot-wash review",
        "swift-water rescue asset",
        "contingency radius protocol"
      ],
      "technical_terms_to_avoid": [
        "illusion of validity",
        "availability heuristic",
        "authority bias",
        "framing effect",
        "hindsight bias",
        "insensitivity to sample size",
        "any explicit cognitive-bias terminology or psychological jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dam operator notice describes the release using standard operational language that is genuinely open to more than one reading",
          "Downstream gauge readings show a gradual, modest level rise, not clearly diagnostic of eventual magnitude",
          "Duty hydrologist is unavailable for independent verification",
          "The flood Branch Director notes the pattern resembles prior releases, while also flagging that this storm cell's rainfall forecast is less certain than in past events"
        ],
        "alternatives": [
          "Issue an immediate evacuation warning for low-lying Sector 7",
          "Issue a lower-tier 'monitor and prepare' advisory only",
          "Hold any public messaging pending independent hydrological verification"
        ],
        "intended_action": "Analyst selects the advisory-only tier after weighing the gradual gauge trend, the Director's qualified read (routine pattern but uncertain storm forecast), and the operational cost of over-escalating, documenting the monitoring plan that would trigger an upgrade.",
        "new_information_after_decision": [
          "Within 90 minutes, gauge levels exceed the warning threshold rapidly",
          "The release volume was larger than the gradual early trend had suggested"
        ]
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Field liaison reports scattered water-rescue calls in two sub-neighborhoods, with an unclear trend line since call intervals are irregular",
          "Weather service updates the storm cell's projected duration upward by an uncertain margin",
          "No new gauge or rainfall data has arrived since the last COP update",
          "A neighboring jurisdiction's mutual-aid swift-water assets are available on a limited-time hold"
        ],
        "alternatives": [
          "Request a standard tier-1 rescue package matching current confirmed calls",
          "Request a staged tier-2 mobilization to preserve the mutual-aid hold window",
          "Request full tier-3 mobilization to cover a wide range of possible escalation paths"
        ],
        "intended_action": "Analyst requests a staged tier-2 mobilization, citing the irregular call trend, the extended storm duration estimate, and the closing mutual-aid window as jointly justifying a middle-tier request rather than either extreme.",
        "new_information_after_decision": [
          "Rescue calls plateau at a volume that, in hindsight, could have been served by either tier-1 or tier-2 staffing",
          "The mutual-aid assets are partially used, with some held in reserve for the remainder of the shift"
        ]
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Only 2 of 8 planned stream gauges are transmitting; the rest are offline due to smoke-damaged repeaters",
          "Both reporting gauges show a sharp rise over a 20-minute window",
          "The EOC's degraded-sensor contingency protocol specifies a default evacuation radius around any gauge exceeding threshold when network coverage falls below 50 percent",
          "Field spotters report localized street flooding near one of the two active gauges, with no reports yet from other sub-zones"
        ],
        "alternatives": [
          "Expand evacuation only to sub-zones adjacent to the two reporting gauges, per the contingency radius protocol",
          "Expand evacuation to the entire multi-sector watershed area as a wider precaution",
          "Request emergency deployment of backup gauge readings or aerial confirmation before expanding further"
        ],
        "intended_action": "Analyst applies the documented contingency radius protocol and expands evacuation to the zones adjacent to the two reporting gauges, explicitly noting that the protocol's radius is a policy compromise rather than a claim about actual conditions in unmonitored sub-zones.",
        "new_information_after_decision": [
          "Backup gauges are restored later and show that flooding in the adjacent zones matched the protocol's assumptions in some areas but not others"
        ]
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The event has stabilized; outcome data (moderate flooding, partial evacuations, staged resource use) is now known",
          "EOC leadership convenes a hot-wash review of the Phase 1 advisory-only decision",
          "The review uses a structured after-action template that separates 'information available at time of decision' from 'information available now'"
        ],
        "alternatives": [
          "Conclude the original advisory decision was reasonable given what was known, while noting specific data points that would have justified earlier escalation had they been available",
          "Conclude the original decision under-responded and should be revised in the SOP without fully separating hindsight knowledge from real-time knowledge",
          "Defer judgment pending a fuller data reconciliation across all four decision points"
        ],
        "intended_action": "Analyst walks through the after-action template point by point, explicitly separating what the gradual gauge trend and qualified Director comment supported at the time from what is now known, and reaches a mixed conclusion: some elements of the advisory choice look defensible in hindsight, others look like they could have been escalated sooner, without asserting that the outcome was clearly foreseeable from the outset.",
        "new_information_after_decision": []
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were responsible for when this incident began.",
        "What was your understanding of the operational objective at the start of your shift?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from the initial dam notice to the evacuation expansion.",
        "What information sources were feeding your Common Operating Picture at each stage?",
        "When did new information arrive relative to each decision you made?"
      ],
      "decision_point_probes": [
        "What cues stood out to you most at that moment, and why?",
        "What alternatives did you consider, and what ruled the others out?",
        "How did you weigh the different pieces of information you had at that point?",
        "How confident were you in the picture you had at the time, and what was that confidence based on?",
        "What role did time pressure play in how you weighed the available data?",
        "Had you handled a similar situation before? How did that prior experience shape your read of this one?",
        "How much uncertainty did you feel you were operating under at that point?"
      ],
      "closing_hypotheticals": [
        "If the dam operator's notice had used different wording, do you think your initial call would have changed?",
        "If all eight gauges had been online throughout, would the evacuation decision have gone differently?",
        "Looking back now, how do you separate what was knowable at the time from what became clear afterward?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "EM_Biased_7",
      "features_to_match": [
        "Domain vocabulary (COP, stream gauge threshold, tier-1/2/3 mobilization, advisory vs. warning tier, watershed sub-zone, hot-wash review, swift-water rescue asset)",
        "Same four-decision-point structure and chronology (threat classification, resource mobilization, evacuation scope, retrospective hot-wash)",
        "Same actors and stakeholders (dam operator, Branch Director, field liaison, fire dispatch, downstream residents)",
        "Same emotional tone: measured, professional, moderate time pressure",
        "Same moderate difficulty and degraded-information constraints (partial gauge outage, unavailable hydrologist, smoke-limited aerial recon)"
      ],
      "features_to_remove_or_change": [
        "Remove single-cause reliance on notice wording alone in Phase 1; replace with joint weighing of gradual trend and an explicitly qualified (not purely reassuring) Director comment",
        "Remove explicit reliance on a single vivid past-event memory as the stated driver of the Phase 2 resource tier; replace with multiple stated factors (call trend, forecast duration, mutual-aid window)",
        "Remove treatment of a 2-of-8 gauge sample as sufficient for a full watershed-wide inference in Phase 3; replace with an explicit, policy-based contingency radius applied consistently regardless of the sample-size question",
        "Remove narrative-coherence-driven overconfidence in Phase 3; replace with an explicit caveat that the protocol is a compromise, not a claim of certainty",
        "Remove outcome-driven 'should have been obvious' retrospective claim in Phase 4; replace with a structured, mixed after-action judgment that explicitly separates real-time and outcome knowledge throughout"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined: the analyst's choice should be explainable by legitimate, stated operational reasoning (protocol compliance, resource scarcity, forecast uncertainty, structured after-action method) such that a reasonable observer cannot confidently attribute the choice to any single named bias mechanism. Do not resolve the ambiguity by making the decision obviously correct or obviously erroneous, and do not insert cues that uniquely fit one of the six target bias mechanisms (reassuring wording as sole driver, authority-based deference as sole driver, single vivid memory as sole driver, small-sample overgeneralization stated as sufficient on its own, coherence-based overconfidence, or outcome-contaminated foreseeability claims)."
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
      "Confirm exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Confirm zero intended bias instances are embedded for any of the six target biases (Illusion of Validity, Insensitivity to sample size, Authority Bias, Availability Bias, Framing Effect, Hindsight bias).",
      "Confirm no bias name, definition, or psychological label appears in the public interview text.",
      "Confirm each decision point's reasoning is supported by an explicit, stated non-bias operational justification (protocol, resource constraint, forecast uncertainty, structured review method).",
      "Confirm Phase 1 does not rely solely on notice wording or solely on Director authority as the stated decisive factor; both must be present as one of several jointly weighed factors, none singularly determinative.",
      "Confirm Phase 2 does not attribute the tier choice to a single vivid recalled event; multiple stated factors must jointly justify the staged tier.",
      "Confirm Phase 3 does not treat the 2-of-8 gauge sample as self-evidently sufficient for the full watershed, and does not express coherence-based overconfidence; the protocol-compliance framing must carry the decision with an explicit uncertainty caveat.",
      "Confirm Phase 4 does not include an outcome-contaminated foreseeability claim; the structured after-action method must produce a genuinely mixed conclusion.",
      "Confirm total interview length falls within 1,215-1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals as required.",
      "Confirm consequences described remain ambiguous as to whether decisions were well- or poorly-calibrated, avoiding outcomes that mechanically prove or disprove reasoning quality."
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
