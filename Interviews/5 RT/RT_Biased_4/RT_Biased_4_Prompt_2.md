You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"generation_specification": {
    "scenario_title_internal": "The Milepost 214 Rail Flaw and the Q-119 Release Decision",
    "scenario_summary_internal": "A division superintendent manages an evolving situation on a busy subdivision: an ultrasonic test flags a growing internal rail flaw on a curve near milepost 214 just as a winter cold front approaches and a high-priority intermodal train (Q-119) is due through the territory. Over several hours, the superintendent must interpret updated defect data, decide whether to impose a slow order, consult with a small operations group by conference call about releasing Q-119 at track speed, and finally run a post-incident debrief after a minor wheel-rail anomaly is reported downstream. The case is designed to elicit under-updating on new severity data, over-reliance on personal tenure with similar-looking past defects, a group discussion that pushes an initially moderate position toward a more extreme one, and a rapid, dissent-suppressing consensus in the closing meeting.",
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
          "Superintendent classifies the defect as 'monitor, retest in two weeks' consistent with past practice for similarly sized flaws"
        ],
        "alternatives": [
          "Classify defect as 'monitor' per historical pattern and schedule routine retest",
          "Immediately impose a slow order pending same-day retest given the elevated growth rate",
          "Request emergency inspection support from an adjoining division"
        ],
        "intended_action": "Superintendent adopts the 'monitor' classification, treating the new growth-rate figure as within the range of previously seen, self-resolving flaws, without adjusting the assessment to reflect that this defect is growing faster than prior cases."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Track inspector raises concern that this segment is CWR laid five years ago, unlike the bolted-rail segments where most prior 'stabilized' flaws were found",
          "Current tonnage on the curve has increased roughly 15% year-over-year",
          "Superintendent has handled dozens of similar-looking flaw reports over a 20-year career on this subdivision",
          "No slow order currently in effect"
        ],
        "new_information_after_decision": [
          "Superintendent recalls three specific past cases from memory where a flaw of similar visual size 'turned out fine' and decides this case will behave the same way",
          "Decision is made to hold off on a slow order and keep the curve at track speed pending the two-week retest"
        ],
        "alternatives": [
          "Impose an interim slow order given the CWR construction and higher tonnage, distinct from the bolted-rail precedents being recalled",
          "Keep track speed based on the reasoning that similar past flaws resolved without incident",
          "Split the difference: reduce speed only for identified defect-adjacent train movements"
        ],
        "intended_action": "Superintendent generalizes directly from remembered past incidents without accounting for the material differences (CWR vs bolted rail, higher tonnage, cold-weather timing) and keeps the segment at track speed."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief Dispatcher, Trainmaster, and Road Foreman join a short conference call to decide whether to release Q-119 through milepost 214 at track speed or hold it for a reroute",
          "Individually, each participant has expressed mild caution beforehand: Trainmaster texted 'probably fine but a little nervous,' Road Foreman said 'leaning toward yes but wouldn't mind a slow order'",
          "The customer service desk has flagged the two-hour delay penalty as a live financial consequence"
        ],
        "new_information_after_decision": [
          "During the call, participants reinforce each other's confidence, and the group lands on releasing Q-119 at full track speed with no slow order at all, more decisively than any individual had proposed beforehand",
          "The call ends in under six minutes with no dissent voiced"
        ],
        "alternatives": [
          "Release Q-119 at track speed as the group ultimately decided",
          "Release Q-119 with a temporary slow order through the milepost 214 curve only",
          "Hold Q-119 for a reroute via the adjoining subdivision"
        ],
        "intended_action": "The group discussion shifts the collective position toward a more extreme, more risk-tolerant decision (full track speed, no slow order) than the moderate caution any individual member expressed going into the call."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "After Q-119 passes, a following local crew reports a minor unusual wheel-rail sound near milepost 214 but no measurable damage",
          "Assistant Engineer, not on the earlier call, requests to join the debrief to raise concerns about the defect classification and speed decision",
          "Debrief meeting is scheduled for 15 minutes before shift change"
        ],
        "new_information_after_decision": [
          "The debrief group (Superintendent, Trainmaster, Chief Dispatcher) quickly agrees the wheel-rail sound was unrelated to the flaw and closes the meeting without inviting the Assistant Engineer or reviewing the retest timeline",
          "Minutes record unanimous agreement that 'the process worked as intended' with no dissenting view logged"
        ],
        "alternatives": [
          "Extend the debrief to include the Assistant Engineer's concerns and reassess the retest interval",
          "Quickly ratify the existing plan and close the meeting before shift change, as occurred",
          "Escalate to the chief engineer for an independent review of the defect classification"
        ],
        "intended_action": "The debrief group reaches rapid, unanimous closure, excludes a dissenting voice, and does not seriously entertain alternative explanations or a review of the classification decision, treating the quick consensus as confirmation that the process was sound."
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
        "What information did you have in front of you when you classified the defect as 'monitor'?",
        "What made you confident that this flaw would behave like the ones you recalled from earlier in your career?",
        "How did the group's view change, if at all, over the course of the conference call?",
        "What was discussed, or not discussed, in the debrief before it closed?",
        "What alternatives did you weigh at each of these points, and why did you rule the others out?",
        "How much time pressure did you feel at each of these moments?",
        "How certain were you about the defect's growth rate at the time you made the classification?"
      ],
      "closing_hypotheticals": [
        "If the retest interval had been one week instead of two, would anything about your classification have changed?",
        "If the Assistant Engineer had been on the original conference call, do you think the release decision would have gone differently?",
        "Looking back, is there a point where you'd have wanted a dissenting voice to speak up more forcefully?",
        "If this same flaw had appeared on a different curve you hadn't worked before, would your approach have changed?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Conservatism Bias",
        "decision_point": 1,
        "mechanism": "Superintendent under-adjusts the risk classification despite new quantitative evidence (doubled defect size, faster growth rate than prior cases) indicating the situation has materially worsened, retaining the prior 'monitor' belief instead of updating toward a more urgent classification.",
        "affected_reasoning_operation": "Belief updating in response to new diagnostic evidence",
        "evidence_available_at_time": [
          "Ultrasonic test result showing growth from 2mm to 4mm in three weeks",
          "Track inspector's verbal flag that this growth rate exceeds prior logged cases"
        ],
        "required_textual_manifestation": "Interviewee acknowledges the new, larger/faster reading but explains the classification stayed at 'monitor, retest in two weeks' essentially unchanged from the prior visit, treating the new number as not warranting a shift in urgency.",
        "plausible_nonbias_interpretation": "A defensible judgment that 4mm is still within an established retest-rather-than-immediate-action threshold under track safety standards.",
        "strength": "subtle",
        "do_not_make_explicit": ["conservatism", "underweighting new evidence", "belief updating"]
      },
      {
        "instance_id": "eb_01",
        "bias": "Experience Bias",
        "decision_point": 2,
        "mechanism": "Superintendent draws on personally recalled past cases with superficial similarity (visual flaw size) while discounting material contextual differences (CWR vs bolted rail, higher tonnage, cold-weather timing) that distinguish the current case from those precedents.",
        "affected_reasoning_operation": "Analogical retrieval and generalization from personal case memory",
        "evidence_available_at_time": [
          "Track inspector's statement that this segment is CWR, unlike prior stabilized-flaw segments",
          "15% year-over-year tonnage increase on the curve",
          "Superintendent's 20 years of personal experience with similarly sized flaws"
        ],
        "required_textual_manifestation": "Interviewee explicitly references three specific remembered past cases as the basis for expecting this flaw to resolve similarly, without addressing why the CWR/tonnage/season differences might make the analogy weaker.",
        "plausible_nonbias_interpretation": "Reasonable use of pattern recognition built from decades of tenure on the same physical territory.",
        "strength": "subtle",
        "do_not_make_explicit": ["experience bias", "overgeneralization", "pattern matching"]
      },
      {
        "instance_id": "gp_01",
        "bias": "Group Polarization",
        "decision_point": 3,
        "mechanism": "Individually moderate, mildly cautious pre-call positions from the Trainmaster and Road Foreman shift, through group discussion, toward a more extreme collective position (full track speed, zero slow order) than any individual endorsed beforehand.",
        "affected_reasoning_operation": "Collective risk-position formation through group discussion",
        "evidence_available_at_time": [
          "Trainmaster's pre-call text expressing mild nervousness",
          "Road Foreman's pre-call statement leaning toward release but open to a slow order",
          "Financial penalty information from the customer service desk raised during the call"
        ],
        "required_textual_manifestation": "Interviewee describes the call's outcome as more decisively pro-release than the individual sentiments going in, and notes the call was short and ended without any dissenting voice moderating the final position.",
        "plausible_nonbias_interpretation": "The group may have simply been persuaded by a genuinely strong operational case for release that emerged during discussion.",
        "strength": "moderate",
        "do_not_make_explicit": ["group polarization", "risky shift", "social amplification"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 4,
        "mechanism": "The debrief group reaches fast, unanimous closure, actively excludes a stakeholder with a known dissenting concern, and records an illusion of unanimity without examining alternative explanations for the wheel-rail sound or revisiting the classification/speed decisions.",
        "affected_reasoning_operation": "Group consensus formation and alternative-generation under time pressure",
        "evidence_available_at_time": [
          "Assistant Engineer's request to join the debrief to raise concerns",
          "Local crew's report of an unusual wheel-rail sound",
          "15-minute time window before shift change"
        ],
        "required_textual_manifestation": "Interviewee describes the debrief closing quickly with unanimous agreement that 'the process worked,' the Assistant Engineer not being included, and no alternative explanations or reconsideration of the retest timeline being discussed.",
        "plausible_nonbias_interpretation": "A legitimately quick meeting because the wheel-rail sound was, in fact, minor and unrelated, and shift-change timing genuinely limited discussion.",
        "strength": "moderate",
        "do_not_make_explicit": ["groupthink", "illusion of unanimity", "self-censorship", "dissent suppression"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario was supplied for this generation (paired/base scenario ID is NONE)."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable: condition is 'biased', not 'counterfactual'; no counterfactual variable was instantiated for this generation despite AUTOSELECT being permitted by input, since the condition field governs generation mode.",
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Each of the four manifest biases (Conservatism Bias, Experience Bias, Group Polarization, Groupthink) has exactly one planned instance, mapped to a distinct decision point.",
      "No bias name, definition, or psychological label appears in probes or narrative content.",
      "Each instance has a distinguishable evidence trail sufficient for independent identification without relying on outcome-based judgment.",
      "Consequences described (minor wheel-rail sound, no measurable damage) do not conclusively prove or disprove whether any decision was biased.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable via four decision-point narrations plus probes without repetitive exposition.",
      "Technical vocabulary reflects rail operations terminology consistent with a Division Superintendent role.",
      "Group-level biases (Group Polarization, Groupthink) are each given moderate strength to ensure sufficient multi-actor dialogue evidence within the word budget."
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
