You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "RT_Vocab_Control_4",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Division Superintendent / Operations Manager",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Milepost 214 Rail Flaw and the Q-119 Release Decision (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A division superintendent manages the same evolving situation as the paired biased scenario: an ultrasonic test flags a growing internal rail flaw on a curve near milepost 214 just as a winter cold front approaches and a high-priority intermodal train (Q-119) is due through the territory. Over several hours, the superintendent interprets updated defect data, decides whether to impose a slow order, consults with a small operations group by conference call about releasing Q-119, and runs a post-incident debrief after a minor wheel-rail anomaly is reported downstream. Unlike the paired scenario, every decision in this version is supported by proportionate evidence-weighting, explicit consideration of contextual differences, a group discussion that converges without amplifying individual positions into an extreme, and a debrief that includes the dissenting engineering voice and revisits open questions. The scenario is designed to match the biased scenario's domain vocabulary, structure, actors, emotional tone, and decision count while containing zero intended instances of any named bias.",
    "occupational_realism": {
      "objective": "Maintain safe train operations across the subdivision while minimizing unnecessary delay to a contractual priority intermodal service during a developing rail-defect and weather situation.",
      "setting": "Division dispatch office and territory covering a 90-mile freight subdivision with a curved, high-tonnage segment near milepost 214, during a forecast overnight temperature drop of 25°F.",
      "constraints": [
        "Only one qualified track inspector available for re-testing before Q-119's scheduled window",
        "Contractual on-time performance penalty if Q-119 is delayed beyond a two-hour window",
        "Falling temperatures increase risk of rail contraction breaks in continuous welded rail (CWR)",
        "Limited extra-board crew availability for a potential reroute",
        "Communication only by phone/radio conference call, no in-person meeting possible before the decision window closes"
      ],
      "stakeholders": [
        "Division Superintendent (interviewee)",
        "Track Inspector",
        "Chief Dispatcher",
        "Trainmaster",
        "Road Foreman of Engines",
        "Assistant Engineer (track engineering)",
        "Intermodal customer service desk"
      ],
      "technical_terms_to_use": [
        "ultrasonic rail flaw detection",
        "continuous welded rail (CWR)",
        "slow order",
        "FRA Track Safety Standards / track class",
        "wheel-rail interface",
        "cold weather rail break risk",
        "extra board crew",
        "priority intermodal train",
        "on-time performance (OTP) metric",
        "defect growth rate"
      ],
      "technical_terms_to_avoid": [
        "conservatism bias",
        "experience bias",
        "group polarization",
        "groupthink",
        "anchoring",
        "cognitive bias",
        "heuristic",
        "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Morning ultrasonic test flags a 4mm internal transverse defect near milepost 214, previously logged at 2mm three weeks earlier",
          "Track is currently classified for 60 mph freight operation",
          "Historical defect log shows this curve has had similar small flaws in the past that stabilized without incident",
          "Overnight low forecast to drop 25°F by evening"
        ],
        "new_information_after_decision": [
          "Track inspector notes the growth rate (2mm to 4mm in three weeks) is faster than the prior flaws referenced in the log",
          "Superintendent reclassifies the defect to an elevated-monitor status and moves the retest interval up to one week rather than the standard two, citing the faster growth rate as the deciding factor"
        ],
        "alternatives": [
          "Retain the standard 'monitor, retest in two weeks' classification per historical pattern",
          "Move to an elevated-monitor status with a shortened one-week retest given the faster growth rate",
          "Request emergency inspection support from an adjoining division"
        ],
        "intended_action": "Superintendent explicitly treats the faster growth rate as new, decision-relevant information and proportionately tightens the retest interval, without over- or under-reacting to the single data point."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Track inspector raises concern that this segment is CWR laid five years ago, unlike the bolted-rail segments where most prior 'stabilized' flaws were found",
          "Current tonnage on the curve has increased roughly 15% year-over-year",
          "Superintendent has handled dozens of similar-looking flaw reports over a 20-year career on this subdivision",
          "One-week retest interval from decision point 1 is now in effect"
        ],
        "new_information_after_decision": [
          "Superintendent weighs the recalled past cases against the inspector's stated CWR and tonnage distinctions and concludes the differences are material enough to warrant a temporary, targeted response",
          "Decision is made to impose a modest interim speed restriction for the curve until the one-week retest, rather than either full track speed or a blanket slow order"
        ],
        "alternatives": [
          "Keep full track speed based on similarity to past resolved cases",
          "Impose a full slow order across the segment pending retest",
          "Impose a targeted, moderate interim speed restriction reflecting the CWR/tonnage distinctions while awaiting the retest"
        ],
        "intended_action": "Superintendent uses personal experience as one input among several, explicitly reasons about why the current case differs from prior ones (construction type, tonnage, timing), and selects a proportionate middle option rather than defaulting to the remembered pattern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief Dispatcher, Trainmaster, and Road Foreman join a short conference call to decide whether to release Q-119 through milepost 214 under the interim restriction, hold it for a reroute, or seek further data",
          "Individually, each participant has expressed mild caution beforehand: Trainmaster texted 'probably fine but a little nervous,' Road Foreman said 'leaning toward yes but wouldn't mind a slow order'",
          "The customer service desk has flagged the two-hour delay penalty as a live financial consequence"
        ],
        "new_information_after_decision": [
          "During the call, participants raise and weigh the interim restriction already in place, the penalty exposure, and the one-week retest timeline, and the group settles on releasing Q-119 under the existing interim restriction rather than adopting a more extreme position in either direction",
          "The call runs about fifteen minutes and includes at least one explicit question about whether the restriction is sufficient before consensus is reached"
        ],
        "alternatives": [
          "Release Q-119 under the interim restriction already in place",
          "Remove the restriction and release at full track speed",
          "Hold Q-119 for a reroute via the adjoining subdivision"
        ],
        "intended_action": "The group discussion converges on a position that is consistent with, rather than more extreme than, the individual pre-call positions, incorporating the existing interim restriction and explicit verification before reaching consensus."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "After Q-119 passes under the interim restriction, a following local crew reports a minor unusual wheel-rail sound near milepost 214 but no measurable damage",
          "Assistant Engineer, not on the earlier call, requests to join the debrief to raise concerns about the defect classification and speed decision",
          "Debrief meeting is scheduled for 15 minutes before shift change but is extended by the Chief Dispatcher once the Assistant Engineer's request is relayed"
        ],
        "new_information_after_decision": [
          "The debrief group, including the Assistant Engineer, discusses the wheel-rail sound alongside the interim restriction and the upcoming one-week retest, and agrees to keep the restriction in place and confirm the retest date rather than closing the matter outright",
          "Minutes record the Assistant Engineer's concern as logged and scheduled for follow-up at the retest, alongside the provisional read that the sound was likely unrelated"
        ],
        "alternatives": [
          "Close the debrief quickly without including the Assistant Engineer's input",
          "Extend the debrief to include the Assistant Engineer's concerns and confirm the retest and restriction plan, as occurred",
          "Escalate immediately to the chief engineer for an independent review"
        ],
        "intended_action": "The debrief group extends the meeting to incorporate a dissenting perspective, documents open questions rather than declaring closure, and ties the outcome to the already-scheduled retest rather than treating the quick agreement as proof the process was fully resolved."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what first came to your attention that morning regarding milepost 214.",
        "What was your overall objective for the shift once the flaw report came in?"
      ],
      "timeline_reconstruction": [
        "What happened right after the ultrasonic test results came in?",
        "What led up to the conference call about Q-119?",
        "What happened between the call ending and the debrief meeting?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you when you decided on the retest interval?",
        "How did you weigh what you'd seen before against what was different about this case?",
        "How did the group's view compare with where people started before the call?",
        "What was discussed in the debrief, and how was the Assistant Engineer's input handled?",
        "What alternatives did you weigh at each of these points, and why did you rule the others out?",
        "How much time pressure did you feel at each of these moments?",
        "How certain were you about the defect's growth rate at the time you made the classification?"
      ],
      "closing_hypotheticals": [
        "If the retest interval had stayed at two weeks instead of one, would anything about your classification have changed?",
        "If the Assistant Engineer had been on the original conference call, do you think the release decision would have gone differently?",
        "Looking back, is there anything about the debrief you'd have wanted to handle differently given the time constraints?",
        "If this same flaw had appeared on a curve you hadn't worked before, would your approach have changed?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "RT_Biased_4",
      "features_to_match": [
        "Domain vocabulary: ultrasonic rail flaw detection, CWR, slow order, track class, wheel-rail interface, cold weather rail break risk, extra board crew, priority intermodal train, OTP metric, defect growth rate",
        "Setting: 90-mile subdivision, milepost 214 curve, overnight 25°F cold snap, Q-119 priority intermodal train",
        "Actors: Division Superintendent (interviewee), Track Inspector, Chief Dispatcher, Trainmaster, Road Foreman, Assistant Engineer, customer service desk",
        "Structure: four decision points in the same chronological order (classification, speed/slow-order decision, group release call, post-incident debrief)",
        "Difficulty: moderate, with genuine competing goals (safety vs. on-time performance vs. cost of delay)",
        "Emotional tone: measured, professional, mild background pressure without dramatization",
        "Decision count: exactly four, matching the paired scenario"
      ],
      "features_to_remove_or_change": [
        "Replace under-adjustment of the initial classification with an explicit, proportionate tightening of the retest interval in response to the new growth-rate evidence",
        "Replace over-reliance on personally recalled cases with an explicit weighing of experience against stated contextual differences (CWR, tonnage) and a proportionate middle-ground action",
        "Replace the group's shift to a more extreme release position with a group discussion that converges on a position consistent with individual pre-call views and includes explicit verification",
        "Replace the debrief's rapid, dissent-excluding closure with an extended debrief that includes the dissenting stakeholder and documents open follow-up items"
      ],
      "ambiguity_boundary": "Not applicable for population of intended bias instances: this is a zero-bias vocabulary control. Genuine domain uncertainty (e.g., whether the wheel-rail sound is related to the flaw) may remain unresolved, but no reasoning pattern should manifest a named bias mechanism."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable: condition is 'vocabulary_control', not 'counterfactual'; no counterfactual variable is instantiated for this generation.",
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly four decision points are present, each with at least two plausible alternatives, mirroring the paired scenario's structure.",
      "Zero named-bias instances are intentionally embedded anywhere in the interview.",
      "Domain vocabulary, setting, actors, decision count, and emotional tone match the paired biased scenario (RT_Biased_4).",
      "Each decision point shows evidence-proportionate reasoning: new evidence is weighed and acted on, experience is checked against contextual differences, group discussion does not amplify individual positions, and dissent is incorporated rather than excluded.",
      "Consequences (minor wheel-rail sound, no measurable damage) remain genuinely ambiguous and do not mechanically prove the process was correct or incorrect.",
      "No bias name, definition, or psychological label appears anywhere in the interview.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable via four decision-point narrations plus probes without repetitive exposition.",
      "Technical vocabulary reflects rail operations terminology consistent with a Division Superintendent role, matching the paired scenario's technical_terms_to_use list."
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
