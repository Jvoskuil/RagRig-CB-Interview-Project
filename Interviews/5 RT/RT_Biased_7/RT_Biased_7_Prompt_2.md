You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "RT_Biased_7",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Maintenance-of-Way Supervisor / Track Maintenance Supervisor",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Curve MP 47.3 Tie Renewal Under Holiday Freight Deadline",
    "scenario_summary_internal": "A Maintenance-of-Way Supervisor manages an emergency tie and rail renewal at a curve (MP 47.3) flagged by an ultrasonic rail-flaw detection car, within a fixed 60-hour track window before a contracted holiday freight surge. Across four chronological decision points—initial scoping/scheduling, team method-selection briefing, a mid-course progress call, and the final go/no-go on lifting the slow order—the supervisor makes judgments under schedule pressure, incomplete inspection data, group dynamics, and contractual penalty exposure. The narrative embeds exactly seven distinct, independently identifiable bias instances (one each of Group Polarization, Ostrich Effect, Self-serving Bias, Planning Fallacy, Loss Aversion, Experience Bias, and Illusion of Control) without naming or explaining any bias, and without the outcome mechanically confirming whether any decision was in fact biased.",
    "occupational_realism": {
      "objective": "Complete emergency tie and rail renewal on a curve segment (MP 47.3) before a contracted holiday freight embargo lifts, while meeting FRA Track Safety Standards and hours-of-service limits.",
      "setting": "Class 1 freight railroad, single main track curve, 500-linear-foot renewal zone, 60-hour authorized track window, secondary main line with a contracted freight customer penalty clause tied to slow-order removal timing.",
      "constraints": [
        "Fixed 60-hour track outage window before holiday freight surge begins",
        "Limited availability of tamper and ballast regulator equipment (shared with adjacent gang)",
        "Contracted freight customer penalty clause for missed slow-order-removal deadline",
        "Forecast rain within 48 hours reducing ballast compaction/curing time",
        "Hours-of-service limits capping crew work periods",
        "FRA-mandated post-work geometry car pass (or documented manual verification) required before restoring authorized speed"
      ],
      "stakeholders": [
        "Track Maintenance Supervisor (interviewee)",
        "Roadmaster",
        "Track inspector(s)",
        "Chief Train Dispatcher",
        "Regional Engineering Manager",
        "Contracted freight customer operations liaison",
        "Tie gang foreman and crew"
      ],
      "technical_terms_to_use": [
        "slow order",
        "tie renewal",
        "tamping",
        "ballast regulator",
        "ultrasonic rail flaw detection",
        "gauge",
        "cross-level",
        "superelevation",
        "FRA Track Safety Standards Class",
        "geometry car",
        "hours of service",
        "embargo",
        "spot replacement",
        "panel tie gang",
        "dwell time"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias",
        "groupthink",
        "psychological terminology of any kind"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Ultrasonic rail flaw detection car flagged a detail fracture indication at MP 47.3",
          "Most recent track inspection report (two weeks old) rated tie condition as 'fair, some deterioration'",
          "Dispatch authorized a 60-hour track outage window",
          "Weather forecast showed rain arriving within 48 hours",
          "A five-year defect-growth history file for this location existed in the maintenance system but had not yet been pulled"
        ],
        "new_information_after_decision": [
          "Once ties were pulled, more required replacement than the standard production-rate estimate assumed",
          "The unreviewed five-year defect file (obtained later) showed recurring flaw growth at this exact location consistent with a larger needed scope"
        ],
        "alternatives": [
          "Pull the full five-year defect-growth history before finalizing scope and duration",
          "Proceed with the standard 500-foot production-rate table and the two-week-old fair-condition rating"
        ],
        "intended_action": "Supervisor sets an initial 60-hour schedule using standard production rates and the fair-condition rating, without requesting the extended defect history, and commits to a best-case tie-pulling duration."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Revised tie count came in higher than the phase-1 estimate",
          "Roadmaster, two track inspectors, and the foreman convened to discuss method",
          "Foreman proposed accelerating via an extra tamper pass and reduced ballast dwell time to protect the schedule",
          "One inspector recalled a curve segment from three years prior that 'always held up fine' with fewer ties replaced",
          "Phase-1 report had noted this curve's subgrade drainage as poorer than typical"
        ],
        "new_information_after_decision": [
          "Drainage conditions at MP 47.3 differed materially from the recalled prior site, which had well-drained subgrade"
        ],
        "alternatives": [
          "Adopt a more conservative method with slower dwell time and an added geometry check before advancing",
          "Endorse the foreman's accelerated method, citing the prior similar-seeming curve as reassurance"
        ],
        "intended_action": "The group collectively endorses the accelerated method with more confidence than any individual voiced beforehand, partly on the strength of the recalled prior curve's track record."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Overall progress was behind the (already revised) schedule despite the accelerated method",
          "Some sub-segments were on pace; others were behind",
          "A scheduled mid-course status call with the Regional Engineering Manager was due"
        ],
        "new_information_after_decision": [
          "Regional Engineering Manager approved continuing the existing timeline without adjustment, unaware that the original scope estimate itself had contributed to the slippage"
        ],
        "alternatives": [
          "Give a status summary that attributes both the delays and the on-pace segments to a mix of factors, including the initial scope estimate",
          "Attribute delays mainly to weather and a late ballast delivery while crediting the on-pace segments to crew skill and his own scheduling calls"
        ],
        "intended_action": "Supervisor delivers the second explanatory narrative to the Regional Engineering Manager."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Contracted freight window was set to open in six hours",
          "The FRA-required geometry car pass had not yet been completed; only manual spot gauge checks had been done",
          "Supervisor had scheduled extra hand-inspection rounds and a slow-rolling pilot train as compensating measures",
          "Contract penalty clause would trigger if the slow order remained past the window opening"
        ],
        "new_information_after_decision": [
          "The geometry car pass, completed a day later, showed the track within tolerance"
        ],
        "alternatives": [
          "Hold the slow order until the geometry car pass is complete, even if it costs the freight window",
          "Lift the slow order now, relying on manual checks plus extra inspection rounds as compensating control"
        ],
        "intended_action": "Supervisor authorizes early removal of the slow order ahead of the geometry car pass, framing the decision around avoiding the contractual penalty and expressing confidence that the added inspection rounds give him sufficient control over residual risk."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role and responsibilities on this job.",
        "Walk me through what this incident was and why it came up.",
        "What was your main objective going into this window?"
      ],
      "timeline_reconstruction": [
        "Take me through what happened first, in order, from the flaw detection report to the final restoration of speed.",
        "Who else was involved at each stage, and what did they contribute?",
        "What information did you have at each point, and where did it come from?"
      ],
      "decision_point_probes": [
        "At the scheduling stage, what cues told you the standard production estimate would hold? What made you decide whether or not to pull additional history on this location?",
        "During the team briefing, how did the group arrive at the accelerated method? What weight did the earlier similar curve carry in that discussion?",
        "On the mid-course call, how did you explain the schedule status? What factors did you emphasize and why?",
        "On the final go/no-go, what alternatives did you weigh regarding the geometry car pass versus lifting the slow order? What made you confident the extra inspection rounds were enough?",
        "What was your basis for each of these calls at the time you made them?",
        "How much time pressure did you feel at each stage, and how did that shape what you considered?",
        "How certain were you about the track condition and the schedule at each point?",
        "Had you handled anything similar before? How did that shape your read of this situation?"
      ],
      "closing_hypotheticals": [
        "If the freight contract penalty hadn't existed, would the final decision have gone differently?",
        "If you'd had the five-year defect history in hand at the outset, what might you have done differently?",
        "If a different crew or a different inspector had been in that briefing, do you think the method decision would have changed?",
        "Looking back, what would you want to know sooner next time a similar flaw indication comes in?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "rt7_01",
        "bias": "Ostrich Effect",
        "decision_point": 1,
        "mechanism": "Supervisor avoids pulling the available five-year defect-growth history that could reveal a larger true scope, preferring to proceed on the more favorable two-week-old 'fair' rating.",
        "affected_reasoning_operation": "Evidence-selection / information-seeking before scope commitment",
        "evidence_available_at_time": [
          "Ultrasonic flaw flag at MP 47.3",
          "Two-week-old inspection rating of 'fair, some deterioration'",
          "Existence of an accessible five-year defect-growth file, not yet retrieved"
        ],
        "required_textual_manifestation": "Supervisor explicitly states he relied on the standard rating and production table and did not request the extended defect file before locking the schedule.",
        "plausible_nonbias_interpretation": "Time constraints made pulling extra records seem unnecessary for a routine-looking scope decision.",
        "strength": "subtle",
        "do_not_make_explicit": ["ostrich effect", "avoidance", "information avoidance"]
      },
      {
        "instance_id": "rt7_02",
        "bias": "Planning Fallacy",
        "decision_point": 1,
        "mechanism": "Supervisor commits to a best-case, standard-production-rate duration estimate for tie replacement without adjusting for site-specific deterioration signals already in hand.",
        "affected_reasoning_operation": "Duration/scope estimation and schedule commitment",
        "evidence_available_at_time": [
          "Standard 500-ft production rate table",
          "Fair-condition tie rating with 'some deterioration' noted",
          "60-hour authorized window"
        ],
        "required_textual_manifestation": "Supervisor describes setting the 60-hour schedule based on the typical rate table, expressing confidence the job would fit that window despite the deterioration note.",
        "plausible_nonbias_interpretation": "Using a standard planning table is normal practice absent stronger contrary evidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "underestimation"]
      },
      {
        "instance_id": "rt7_03",
        "bias": "Group Polarization",
        "decision_point": 2,
        "mechanism": "The briefing group collectively adopts the accelerated method with greater confidence and less caution than individual members expressed before the discussion began.",
        "affected_reasoning_operation": "Collective risk judgment and method selection",
        "evidence_available_at_time": [
          "Foreman's acceleration proposal",
          "Revised, higher tie count",
          "Individual pre-discussion hesitations (implied) about pace"
        ],
        "required_textual_manifestation": "Supervisor recounts that after the group talked it through, everyone ended up more confident in the fast method than they'd been walking in.",
        "plausible_nonbias_interpretation": "Group discussion surfaced legitimate reassuring information that justified more confidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["group polarization", "risky shift"]
      },
      {
        "instance_id": "rt7_04",
        "bias": "Experience Bias",
        "decision_point": 2,
        "mechanism": "An inspector's recollection of a superficially similar curve from three years earlier is used to judge current risk, without accounting for the documented drainage difference at the current site.",
        "affected_reasoning_operation": "Analogical retrieval and risk assessment for method selection",
        "evidence_available_at_time": [
          "Recollection of prior curve's good long-term performance",
          "Phase-1 report noting poorer subgrade drainage at MP 47.3"
        ],
        "required_textual_manifestation": "Supervisor mentions the inspector's reference to the earlier curve as a reason the group felt reassured about the faster method, without connecting it back to the drainage difference.",
        "plausible_nonbias_interpretation": "Drawing on past comparable cases is a legitimate and often necessary part of field judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["experience bias", "overgeneralization from past cases"]
      },
      {
        "instance_id": "rt7_05",
        "bias": "Self-serving Bias",
        "decision_point": 3,
        "mechanism": "In the same status call, the supervisor attributes schedule slippage to external causes (weather, vendor delivery) while attributing on-pace segments to his own scheduling decisions and crew skill, omitting the earlier scope-estimation choice as a contributing factor.",
        "affected_reasoning_operation": "Causal attribution of outcomes during status reporting",
        "evidence_available_at_time": [
          "Mixed progress: some segments on pace, others behind",
          "Known contributing factors: weather delay, late ballast delivery, and the phase-1 scope/duration estimate"
        ],
        "required_textual_manifestation": "Supervisor's account of the mid-course call splits credit and blame along self-favoring lines for the same overall result.",
        "plausible_nonbias_interpretation": "Weather and vendor delays were genuinely real and worth reporting as factors.",
        "strength": "subtle",
        "do_not_make_explicit": ["self-serving bias", "external attribution for failure"]
      },
      {
        "instance_id": "rt7_06",
        "bias": "Loss Aversion or Loss Framing effect",
        "decision_point": 4,
        "mechanism": "The final decision is framed predominantly around avoiding the contractual penalty ('cannot afford to lose the window') rather than balancing it against the safety margin gained by waiting for the geometry car pass.",
        "affected_reasoning_operation": "Weighing of gains versus losses in the final go/no-go choice",
        "evidence_available_at_time": [
          "Six hours until contracted freight window opens",
          "Penalty clause for missing the window",
          "Geometry car pass incomplete; only manual checks done"
        ],
        "required_textual_manifestation": "Supervisor's explanation of the final call centers on the cost of losing the window more than on the value of the still-missing verification.",
        "plausible_nonbias_interpretation": "Contractual penalties are a legitimate operational consideration in any go/no-go call.",
        "strength": "subtle",
        "do_not_make_explicit": ["loss aversion", "loss framing"]
      },
      {
        "instance_id": "rt7_07",
        "bias": "Illusion of Control",
        "decision_point": 4,
        "mechanism": "Supervisor overestimates his ability to manage the residual risk of an incomplete geometry car pass through added hand-inspection rounds and a slow-rolling pilot train, treating these compensating measures as more determinative of safety outcome than they can support.",
        "affected_reasoning_operation": "Risk-control judgment underlying the final authorization",
        "evidence_available_at_time": [
          "Planned extra inspection rounds and pilot train",
          "Manual gauge spot-checks only, no completed geometry car pass"
        ],
        "required_textual_manifestation": "Supervisor expresses confidence that the extra inspection measures are enough to cover for the missing geometry car verification.",
        "plausible_nonbias_interpretation": "Compensating inspection measures are a standard and sometimes sufficient practice before full verification.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of control", "overconfidence in mitigation"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": null
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
      "Exactly seven bias instances are planned, one per manifest entry, with no substitutions or additions.",
      "No decision point contains more than two instances of the same bias (all instances here are of different biases within their decision points).",
      "Instances rt7_03 and rt7_04 share decision point 2 but rely on distinct evidence sources and reasoning operations (group risk-shift vs. analogical recall).",
      "Instances rt7_06 and rt7_07 share decision point 4 but rely on distinct reasoning operations (loss-weighted framing vs. control-overestimation) and distinct evidence.",
      "No bias name, definition, or psychological explanation will appear in the public interview text.",
      "Consequences (post-decision information) do not mechanically confirm or refute whether any decision was biased.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points, opening, timeline reconstruction, and closing hypotheticals without repetitive exposition."
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
