You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "AV_Biased_5",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Director of Maintenance (DOM)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Intermittent Hydraulic Caution Light Ahead of Holiday Peak Schedule",
    "scenario_summary_internal": "A regional airline DOM manages a recurring, intermittently-clearing Hydraulic System B caution light on an E175 across a five-day window while under pressure to keep the aircraft flying into a holiday traffic peak. The DOM downplays an early worsening trend, defers to an informally-consulted OEM rep and a superficially similar past case over his own senior engineer's request for full fault isolation, continues an incremental repair path partly because of hours/parts already invested once a real leak is found, and finally certifies return-to-service on ground-only data with more certainty than the evidence supports.",
    "occupational_realism": {
      "objective": "Restore the aircraft to safe, dispatch-reliable service while meeting a schedule commitment for an upcoming holiday travel peak.",
      "setting": "Line maintenance hangar at a regional carrier's base station, over a five-day period involving three flight days and two ground/troubleshooting days.",
      "constraints": [
        "Holiday peak schedule requiring the aircraft back in rotation within days",
        "Limited hangar slot availability and competing aircraft needing the same bay",
        "Parts lead time for hydraulic components",
        "Pressure from VP of Operations on dispatch reliability metrics",
        "Limited access to OEM engineering support beyond an informally present field rep",
        "No dedicated test-flight crew available same-day as final repair"
      ],
      "stakeholders": [
        "Director of Maintenance (interviewee)",
        "Senior avionics/hydraulics engineer (line maintenance)",
        "OEM field technical representative",
        "VP of Operations",
        "Scheduling/Ops control",
        "Line pilots reporting the squawks",
        "Quality assurance / RTS signoff authority"
      ],
      "technical_terms_to_use": [
        "MEL (Minimum Equipment List)",
        "CND (could not duplicate)",
        "BITE test",
        "Hydraulic System B",
        "non-routine card",
        "fault isolation manual (FIM)",
        "accumulator",
        "pump seal residue",
        "leak check",
        "return to service (RTS)",
        "squawk",
        "test flight",
        "service bulletin"
      ],
      "technical_terms_to_avoid": [
        "optimism bias",
        "authority bias",
        "sunk cost fallacy",
        "representativeness heuristic",
        "overconfidence bias",
        "cognitive bias",
        "heuristic",
        "confirmation",
        "anchoring"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three pilot writeups over two weeks of momentary Hydraulic System B caution light, each cleared as CND on ground BITE test",
          "No fluid loss or visible leakage found on any inspection",
          "Aircraft has continued flying on schedule with no MEL restriction",
          "Duration of the caution light has crept up slightly across the three events (roughly 2, 3, then 5 seconds)"
        ],
        "new_information_after_decision": [
          "A fourth occurrence the next day with the light lasting about 12 seconds",
          "Crew also notes a brief speed brake anomaly during that same flight"
        ],
        "alternatives": [
          "Ground the aircraft for extended fault isolation (pump pressure decay test) before the holiday peak",
          "Sign off as an intermittent nuisance and continue dispatch under monitoring, deferring deep troubleshooting to the next scheduled check"
        ],
        "intended_action": "DOM authorizes continued dispatch with informal monitoring rather than immediate deep troubleshooting."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Fourth, longer-duration caution light event plus a speed brake anomaly",
          "Senior line engineer requests a full fault isolation procedure per the FIM",
          "OEM field rep, present at the hangar for an unrelated aircraft, is asked informally for a read on the symptom pattern",
          "OEM rep recalls a service bulletin describing a benign software/BITE quirk on another operator's fleet with similar symptoms",
          "A team member recalls a prior in-house case with a hydraulic caution light that resolved after a simple reset"
        ],
        "new_information_after_decision": [
          "BITE reset performed; aircraft flies two clean cycles",
          "A cursory pump seal inspection during a later task turns up small fluid residue not previously documented"
        ],
        "alternatives": [
          "Ground the aircraft for the senior engineer's proposed full isolation procedure",
          "Accept the OEM rep's informal read and the recalled prior case, reset BITE, and clear the aircraft to continue flying"
        ],
        "intended_action": "DOM overrides the senior engineer's isolation request, accepts the OEM rep's casual assessment and the recalled similar case, and clears the aircraft after a reset."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pump seal residue confirmed on inspection, a new finding not present in the earlier CND checks",
          "14 labor hours and several replaced components (accumulator, sensor) already invested in the prior troubleshooting path",
          "The incremental component-swap plan is nearly complete; only the seal remains to be addressed",
          "Full hydraulic pump replacement would require additional downtime and parts not yet on hand"
        ],
        "new_information_after_decision": [
          "Seal is replaced; ground leak check passes",
          "Static ground test shows no further visible residue"
        ],
        "alternatives": [
          "Escalate to a full hydraulic pump teardown/replacement given the new leak evidence",
          "Continue the already-planned incremental path and replace only the seal"
        ],
        "intended_action": "DOM approves the seal-only fix and declines full pump replacement, citing the work and parts already committed to the current path."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Ground leak check passed after seal replacement",
          "Static test shows no residue, but no post-repair test flight has been performed",
          "No test-flight crew available same day; aircraft is needed for an afternoon departure into the holiday peak",
          "History of three prior CND events and one earlier misdiagnosis of the same general system on this tail"
        ],
        "new_information_after_decision": [
          "Aircraft is dispatched on the scheduled flight",
          "Outcome of the flight is not yet known at the time of the interview"
        ],
        "alternatives": [
          "Require a test flight or extended ground run before certifying return to service",
          "Certify return to service immediately based on ground-only data"
        ],
        "intended_action": "DOM signs the RTS certification expressing high confidence the issue is resolved, based on ground test data alone."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what this aircraft's hydraulic issue looked like when you first became aware of it.",
        "What was your role in this event day to day?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you learn at each step?",
        "What changed between the first CND write-up and the fourth event?",
        "Who did you talk to as this unfolded, and what did each of them tell you?"
      ],
      "decision_point_probes": [
        "At the point you decided to keep flying it after the third write-up, what specific information made you comfortable with that?",
        "When the OEM rep gave his read, how much weight did that carry compared to your own engineer's request, and why?",
        "Once the seal residue turned up, what made you stick with the seal-only plan rather than escalating?",
        "When you signed the RTS certification, what evidence were you relying on, and how sure were you it would hold?"
      ],
      "information_sources": [
        "What sources of information did you trust most during this event, and why?",
        "Was there any data you didn't look at or didn't request? Why not?"
      ],
      "goals_and_alternatives": [
        "What other options did you consider at each stage, and why did you rule them out?",
        "How did the schedule pressure factor into which option you picked?"
      ],
      "decision_basis": [
        "If you had to justify this decision to a regulator afterward, what would you point to?",
        "How confident were you at each stage, on a scale of 1-10, and what moved that number?"
      ],
      "prior_experience": [
        "Had you seen anything like this before? How did that history shape your read of this case?"
      ],
      "time_pressure_and_uncertainty": [
        "How much did the holiday schedule weigh on your timeline for these decisions?",
        "What were you still uncertain about when you made the final call?"
      ],
      "closing_hypotheticals": [
        "If the OEM rep hadn't been on-site that day, what do you think you would have done differently?",
        "If the seal residue had shown up before the component swaps instead of after, would your approach have changed?",
        "Looking back, is there a point where you'd make a different call with the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ob_01",
        "bias": "Optimism Bias",
        "decision_point": 1,
        "mechanism": "DOM interprets an increasing-duration trend across three intermittent events as unlikely to worsen or recur meaningfully, favoring continued dispatch over deeper investigation.",
        "affected_reasoning_operation": "Risk/trend projection from repeated CND events",
        "evidence_available_at_time": [
          "Three CND write-ups with slightly increasing caution-light duration",
          "No fluid loss found on inspection"
        ],
        "required_textual_manifestation": "DOM states or implies expectation that the issue will likely resolve itself or stay minor, despite the visible upward trend in duration, and chooses monitoring over isolation.",
        "plausible_nonbias_interpretation": "A reasonable read that CND-with-no-fluid-loss findings genuinely support low urgency under MEL policy.",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "trend denial", "risk underestimation"]
      },
      {
        "instance_id": "ab_01",
        "bias": "Authority Bias",
        "decision_point": 2,
        "mechanism": "DOM gives disproportionate weight to the informally-offered opinion of the OEM field rep (present for an unrelated task) over the formal, procedure-based recommendation of his own senior engineer.",
        "affected_reasoning_operation": "Weighting of competing expert recommendations",
        "evidence_available_at_time": [
          "OEM rep's casual, unofficial verbal assessment referencing a different fleet's bulletin",
          "Senior engineer's formal request to run the FIM fault isolation procedure"
        ],
        "required_textual_manifestation": "DOM explains overriding or setting aside the senior engineer's request because the OEM rep's title/affiliation carried more weight, without evaluating whether the rep's informal opinion was actually procedurally grounded for this case.",
        "plausible_nonbias_interpretation": "OEM reps do carry specialized fleet-wide knowledge, so deferring to one is often reasonable practice.",
        "strength": "moderate",
        "do_not_make_explicit": ["authority bias", "deference to titles", "status-based weighting"]
      },
      {
        "instance_id": "rh_01",
        "bias": "Representativeness Heuristic",
        "decision_point": 2,
        "mechanism": "Team matches the current symptom set (caution light + hydraulic system) to a superficially similar prior in-house case and infers the same root cause and fix, without checking dissimilar underlying details (different flight-hour history, different component batch, no borescope check).",
        "affected_reasoning_operation": "Case-pattern matching / categorical inference from surface similarity",
        "evidence_available_at_time": [
          "Recalled prior case file involving a hydraulic caution light resolved by reset",
          "Absence of comparison on flight hours, component batch, or physical inspection depth between the two cases"
        ],
        "required_textual_manifestation": "DOM or team member cites the prior case as reason to expect the same resolution, without probing whether the underlying mechanism actually matches.",
        "plausible_nonbias_interpretation": "Drawing on past maintenance history is a legitimate diagnostic starting point in troubleshooting.",
        "strength": "moderate",
        "do_not_make_explicit": ["representativeness heuristic", "base rate neglect", "surface similarity"]
      },
      {
        "instance_id": "scf_01",
        "bias": "Sunk Cost Fallacy",
        "decision_point": 3,
        "mechanism": "DOM continues the incremental component-replacement plan primarily because of labor hours and parts already spent, discounting the new leak evidence that arguably warrants escalation to full pump replacement.",
        "affected_reasoning_operation": "Cost-based justification for continuing a diagnostic path versus updating on new evidence",
        "evidence_available_at_time": [
          "14 labor hours and multiple replaced components already committed",
          "Newly discovered pump seal residue not accounted for in the original plan"
        ],
        "required_textual_manifestation": "DOM references the hours/parts already invested as a reason to finish the current plan rather than escalate, in a way that is tied to past investment rather than the new evidence.",
        "plausible_nonbias_interpretation": "Completing an almost-finished diagnostic path before escalating can be a legitimate efficiency judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment", "past investment justification"]
      },
      {
        "instance_id": "ocb_01",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "DOM certifies RTS with a stated or implied high degree of certainty that the fix has resolved the issue, exceeding what ground-only test data (no test flight, prior CND/misdiagnosis history) can support.",
        "affected_reasoning_operation": "Calibration of confidence in a decision against the actual strength of supporting evidence",
        "evidence_available_at_time": [
          "Passed ground leak check and clean static test",
          "No post-repair test flight",
          "History of three prior CND events and one earlier misdiagnosis of the same system"
        ],
        "required_textual_manifestation": "DOM expresses strong certainty ('confident this is resolved') in the RTS decision without qualifying that the fix has not been flight-verified.",
        "plausible_nonbias_interpretation": "Ground-based leak checks are an accepted, standard basis for RTS decisions in many maintenance contexts.",
        "strength": "moderate",
        "do_not_make_explicit": ["overconfidence bias", "miscalibration", "unverified certainty"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition, no paired control generated in this specification."
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
      "Exactly 4 decision points are defined in the timeline",
      "Exactly 5 total bias instances planned, matching the manifest total",
      "No two instances of the same bias occur; each named bias has exactly 1 occurrence as requested",
      "Decision point 2 carries two distinct biases (authority, representativeness) with clearly separate evidence sources",
      "No bias labels, definitions, or psychological terminology appear in probe_plan or timeline content intended for the public interview",
      "Each occurrence has a documented plausible non-bias interpretation",
      "Consequences described (test-flight-free RTS, unresolved final outcome) do not mechanically confirm or deny bias",
      "Target word count 1,215-1,485 achievable given 4 decision points with probes and chronological narrative"
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
