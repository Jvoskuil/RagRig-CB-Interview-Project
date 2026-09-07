You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Biased_7",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Emergency Operations Center (EOC) Situation Unit Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Twin Forks Flash Flood and Ridge Fire Smoke Incident",
    "scenario_summary_internal": "Over a 14-hour operational period, a Situation Unit Analyst at a county EOC manages the Common Operating Picture during a compound event: an unplanned high-volume release from Twin Forks Reservoir coincides with a monsoonal storm cell and reduced aerial/sensor visibility from active Ridge Fire smoke. The analyst must classify the threat and decide on public warning tier, mobilize rescue resources, decide on evacuation zone expansion using degraded sensor coverage, and later participate in a hot-wash review of the initial decision after the outcome is known.",
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
        "tier-1/tier-3 mobilization",
        "advisory vs. warning tier",
        "watershed sub-zone",
        "hot-wash review",
        "swift-water rescue asset"
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
          "Dam operator notice describes the release as a 'controlled precautionary release to manage reservoir levels ahead of the storm system'",
          "Downstream gauge readings show a gradual, modest level rise consistent with routine operations",
          "Duty hydrologist is unavailable for independent verification",
          "The flood Branch Director, a respected 20-year veteran, states this pattern 'is routine, we've seen this before'"
        ],
        "alternatives": [
          "Issue an immediate evacuation warning for low-lying Sector 7",
          "Issue a lower-tier 'monitor and prepare' advisory only",
          "Hold any public messaging pending independent hydrological verification"
        ],
        "intended_action": "Analyst adopts the advisory-only tier, deferring to the Branch Director's framing and the dam operator's characterization without requesting independent verification.",
        "new_information_after_decision": [
          "Within 90 minutes, gauge levels exceed the warning threshold rapidly",
          "The release volume was substantially larger than the 'controlled' framing implied"
        ]
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Field liaison reports scattered water-rescue calls in two sub-neighborhoods, consistent with tier-1 staffing",
          "Fire dispatch chatter uses radio codes similar to those from a widely publicized 2018 neighboring-county mass-casualty flash flood the analyst helped coordinate",
          "No new gauge or rainfall data has arrived since the last COP update"
        ],
        "alternatives": [
          "Request a standard tier-1 rescue package matching current confirmed calls",
          "Request a large tier-3 mobilization sized to match the recalled 2018 event",
          "Hold current staffing and reassess in 30 minutes"
        ],
        "intended_action": "Analyst requests tier-3 mobilization, sized to the vividly remembered 2018 event rather than the smaller confirmed current call volume.",
        "new_information_after_decision": [
          "Actual rescue calls plateau at a volume consistent with tier-1 need",
          "Tier-3 assets are partly idle, straining resources needed elsewhere for the fire branch"
        ]
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Only 2 of 8 planned stream gauges are transmitting; the rest are offline due to smoke-damaged repeaters",
          "Both reporting gauges show a sharp rise over a 20-minute window",
          "Social media videos of flooding at one visually dramatic intersection are circulating widely and being amplified by a regional news account",
          "The analyst's projected flood-extent map, built from the two gauges plus the viral footage, appears internally coherent and is presented with high confidence"
        ],
        "alternatives": [
          "Expand evacuation to the entire multi-sector watershed area based on the two gauges and viral footage",
          "Expand evacuation only to sub-zones adjacent to the two reporting gauges pending more data",
          "Request emergency deployment of backup gauge readings or aerial confirmation before expanding"
        ],
        "intended_action": "Analyst expands the evacuation order to the full multi-sector watershed area, expressing strong confidence in the derived flood map despite thin, unrepresentative sensor coverage.",
        "new_information_after_decision": [
          "Backup gauges are restored later and show two of the newly evacuated sub-zones never exceeded minor flood stage"
        ]
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The event has stabilized; full outcome data (major flooding, evacuations, resource strain) is now known",
          "EOC leadership convenes a hot-wash review of the Phase 1 advisory-only decision",
          "The dam operator's original notice wording is being re-read in light of what is now known"
        ],
        "alternatives": [
          "Conclude the original advisory decision was a clear, foreseeable error given 'obvious' warning signs in the notice",
          "Evaluate the Phase 1 decision using only the information that was available at that time",
          "Defer judgment pending full data reconciliation"
        ],
        "intended_action": "Analyst states the escalation 'should have been obvious' from the dam notice wording alone, reconstructing the earlier decision as clearly negligent in light of the now-known outcome.",
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
        "Whose input carried the most weight in that decision, and why?",
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
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Framing Effect",
        "decision_point": 1,
        "mechanism": "The dam operator's positively-valenced characterization ('controlled precautionary release') shapes the analyst's threat classification more than the underlying gauge data would independently warrant.",
        "affected_reasoning_operation": "Threat-tier classification / risk categorization",
        "evidence_available_at_time": [
          "Dam operator notice text framed as routine/controlled",
          "Modest gradual gauge rise",
          "No independent hydrological verification yet obtained"
        ],
        "required_textual_manifestation": "Analyst explicitly references the operator's wording ('controlled,' 'precautionary') as the basis for choosing the lower advisory tier, rather than citing independent gauge trend analysis.",
        "plausible_nonbias_interpretation": "Given genuinely limited gradual gauge rise, an advisory tier could be a reasonable proportional response absent framing influence.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "wording bias", "anchoring on language"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Authority Bias",
        "decision_point": 1,
        "mechanism": "Analyst defers to the Branch Director's confident verbal assessment ('this is routine, we've seen this before') on the basis of the Director's seniority/title rather than independent verification of current data.",
        "affected_reasoning_operation": "Evidence weighting / deference in decision authorization",
        "evidence_available_at_time": [
          "Branch Director's verbal assurance, delivered with confidence and citing tenure",
          "Absence of the duty hydrologist to independently confirm"
        ],
        "required_textual_manifestation": "Analyst names the Director's experience/seniority as the specific reason for not seeking further verification before finalizing the advisory tier.",
        "plausible_nonbias_interpretation": "Trusting an experienced supervisor under time pressure is a normal chain-of-command heuristic in EOC operations.",
        "strength": "subtle",
        "do_not_make_explicit": ["authority bias", "deference to hierarchy", "credential-based trust"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "A vivid, personally salient memory of the 2018 mass-casualty flash flood (triggered by superficially similar radio codes) is used to size the current resource request instead of the actual current call volume.",
        "affected_reasoning_operation": "Resource-need estimation / prediction of rescue demand",
        "evidence_available_at_time": [
          "Current confirmed rescue calls limited to two sub-neighborhoods (tier-1 consistent)",
          "Radio chatter superficially resembling the 2018 event's codes",
          "No new gauge or rainfall data since last update"
        ],
        "required_textual_manifestation": "Analyst explicitly attributes the tier-3 mobilization request to the memory of the 2018 event ('this reminded me of...') rather than to current call-volume data.",
        "plausible_nonbias_interpretation": "Erring toward a larger mobilization could be framed as a defensible precautionary safety margin.",
        "strength": "moderate",
        "do_not_make_explicit": ["availability bias", "vivid memory", "recency/salience of recall"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Insensitivity to sample size",
        "decision_point": 3,
        "mechanism": "Analyst extrapolates a watershed-wide flood extent from only two of eight gauges (a small, non-representative sample) as though it were as reliable as full-network coverage.",
        "affected_reasoning_operation": "Statistical/spatial extrapolation from sensor data to a broader geographic conclusion",
        "evidence_available_at_time": [
          "Only 2 of 8 stream gauges transmitting",
          "Sharp 20-minute rise at those two gauges",
          "Six gauges offline with unknown readings"
        ],
        "required_textual_manifestation": "Analyst treats the two-gauge trend as sufficient basis for a full multi-sector watershed conclusion without qualifying the limited coverage.",
        "plausible_nonbias_interpretation": "Acting on partial data under time pressure is a defensible precautionary approach in life-safety contexts.",
        "strength": "moderate",
        "do_not_make_explicit": ["insensitivity to sample size", "small-sample extrapolation", "statistical representativeness"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Availability Bias",
        "decision_point": 3,
        "mechanism": "Widely circulated, emotionally vivid social-media/news footage of one dramatic flooded intersection disproportionately elevates the analyst's perceived severity and geographic scope of the flood, distinct from the earlier institutional-memory-based recall in cb_03.",
        "affected_reasoning_operation": "Severity/scope estimation from media salience rather than systematic sensor coverage",
        "evidence_available_at_time": [
          "Viral video/footage of one dramatic flooded intersection",
          "Amplification by a regional news account",
          "Sparse underlying gauge network"
        ],
        "required_textual_manifestation": "Analyst cites the viral footage's vividness or reach as adding confidence to expanding the evacuation zone, separate from and additional to the two-gauge data point.",
        "plausible_nonbias_interpretation": "Incorporating public-facing visual reports as a supplementary corroborating source is a legitimate multi-source verification practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability bias", "media salience", "vividness effect"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Illusion of Validity",
        "decision_point": 3,
        "mechanism": "Analyst expresses high subjective confidence in the internally coherent flood-extent map despite the map being built on thin, unrepresentative evidence; the coherence of the narrative substitutes for its actual predictive reliability.",
        "affected_reasoning_operation": "Confidence calibration in a predictive/inferential model",
        "evidence_available_at_time": [
          "Internally consistent flood-extent map assembled from two gauges and viral footage",
          "No cross-validation against the six offline gauges or aerial confirmation"
        ],
        "required_textual_manifestation": "Analyst describes feeling confident the map 'told a clear story' or 'all fit together,' explicitly linking that coherence to confidence in accuracy, despite acknowledging the thin data underlying it.",
        "plausible_nonbias_interpretation": "Producing a best-available operational picture under time constraints is standard EOC practice, and expressed confidence could reflect professional decisiveness rather than miscalibration.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "overconfidence from coherence", "narrative fallacy"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Hindsight bias",
        "decision_point": 4,
        "mechanism": "Knowing the eventual severe outcome, the analyst reconstructs the Phase 1 decision as having had 'obvious' warning signs, overestimating how foreseeable the escalation was from the information actually available at the time.",
        "affected_reasoning_operation": "Retrospective causal attribution / reconstruction of past decision quality",
        "evidence_available_at_time": [
          "Now-known full outcome data (major flooding, evacuations, resource strain)",
          "Re-reading of the original dam notice wording with outcome knowledge"
        ],
        "required_textual_manifestation": "Analyst states the escalation 'should have been obvious' from the original notice alone, without acknowledging that this judgment depends on information only available after the fact.",
        "plausible_nonbias_interpretation": "A genuinely reasonable after-action critique could identify real process gaps without inflating their foreseeability at the time.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "outcome knowledge distorting judgment", "creeping determinism"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition primary generation, no paired control specified in this call."
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
      "Confirm exactly 7 total bias instances are embedded: 1 Illusion of Validity, 1 Insensitivity to sample size, 1 Authority Bias, 2 Availability Bias, 1 Framing Effect, 1 Hindsight bias.",
      "Confirm no bias name, definition, or psychological label appears in the public interview text.",
      "Confirm the two Availability Bias instances (cb_03, cb_05) use distinct evidence sources (institutional memory of a past event vs. viral social-media footage) and occur at different decision points.",
      "Confirm decision point 3 contains three distinct bias instances (cb_04, cb_05, cb_06) with non-overlapping mechanisms and no repeated bias.",
      "Confirm each instance has a plausible non-bias explanation present in context so the bias is inferable, not asserted.",
      "Confirm hindsight bias (cb_07) is expressed only in the Phase 4 retrospective decision point and not leaked into earlier decision points or closing hypotheticals.",
      "Confirm total interview length falls within 1,215-1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals as required.",
      "Confirm consequences described do not mechanically prove bias (i.e., bad outcomes are shown as possible under both biased and non-biased reasoning)."
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
