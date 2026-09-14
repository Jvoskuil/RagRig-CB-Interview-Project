You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MU_Biased_5",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Mine Planning Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Panel 5 Extraction Sequencing Under Seismic Uncertainty",
    "scenario_summary_internal": "A mine planning engineer at an underground hard-rock metal mine must decide whether to proceed with a scheduled transition from Panel 4 to Panel 5 sublevel stoping after an overnight seismic event and rising convergence readings near the panel 4 abutment. Production targets for the quarter are behind, the geotechnical team's report is preliminary, and the engineer must reconcile a numerical stability model, prior experience with a superficially similar panel, a minor fall-of-ground incident report, and pressure from the mine manager to keep the blast schedule intact. The narrative follows the engineer from the morning planning meeting through the shift-end review, culminating in a go/no-go call on firing the next stope ring.",
    "occupational_realism": {
      "objective": "Decide how to sequence and support the Panel 5 stope extraction while managing an emerging ground-stability concern without derailing the quarterly production schedule.",
      "setting": "Underground sublevel stoping operation, hard-rock base-metal mine, transition between Panel 4 (near completion) and Panel 5 (next scheduled panel), during a single 24-hour period spanning night shift alert through day shift planning decision.",
      "constraints": [
        "Quarterly production target is already 6% behind plan",
        "Geotechnical team has only preliminary seismic and convergence data, full analysis will take 48 hours",
        "Ground support crew and drill jumbo are scheduled and costly to remobilize if delayed",
        "Mine manager is pushing to maintain the blast cycle",
        "Panel 5 stability model was calibrated using data from Panel 3, not Panel 5's actual rock mass"
      ],
      "stakeholders": [
        "Mine Planning Engineer (interviewee)",
        "Chief Geotechnical Engineer",
        "Mine Manager",
        "Underground Shift Supervisor",
        "Ground Support Contractor",
        "Equipment Operator involved in fall-of-ground incident"
      ],
      "technical_terms_to_use": [
        "sublevel stoping",
        "convergence monitoring",
        "factor of safety (FOS)",
        "seismic event magnitude",
        "abutment stress",
        "fall of ground (FOG)",
        "ground support design",
        "stope firing schedule",
        "rock mass rating (RMR)",
        "extraction sequence"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation",
        "psychological terminology of any kind"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Overnight seismic monitoring recorded a magnitude event near the Panel 4 abutment",
          "Convergence readings in Panel 4 rose modestly above the trailing 30-day average",
          "The original firing schedule calls for Panel 5's first ring to be drilled and loaded this shift",
          "Geotechnical team requests 48 hours to complete a full review"
        ],
        "new_information_after_decision": [
          "Drilling proceeds on the original schedule",
          "A shift supervisor later flags unusual jointing patterns in the Panel 5 heading not previously logged"
        ],
        "alternatives": [
          "Proceed with the existing firing schedule as planned pending the geotech review",
          "Pause the schedule and wait for the 48-hour geotechnical review",
          "Proceed but reduce the ring advance rate as an interim precaution"
        ],
        "intended_action": "Engineer authorizes continuation of the existing schedule, treating the seismic reading as within normal operating variation because that has always been the standing procedure."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Panel 5's rock mass exhibits some visual similarities to Panel 3, which the engineer personally designed support for two years earlier",
          "Panel 3's support design performed well with no major incidents",
          "Panel 5's exploration drilling data shows different joint orientation and a fault splay not present in Panel 3",
          "Ground support contractor asks whether to use the Panel 3 pattern or commission a new design"
        ],
        "new_information_after_decision": [
          "Support pattern from Panel 3 is specified for Panel 5",
          "A geotechnical technician later notes the joint sets in Panel 5 are oriented closer to the fault splay than anything encountered in Panel 3"
        ],
        "alternatives": [
          "Reuse the Panel 3 support pattern given its past success",
          "Commission a new site-specific support design based on Panel 5's actual exploration data",
          "Request an independent geotechnical review before specifying support"
        ],
        "intended_action": "Engineer specifies the Panel 3 support pattern for Panel 5, citing personal past success with that pattern as sufficient justification."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A minor fall of ground occurs in the Panel 5 heading, injuring no one but damaging a loader bucket",
          "Incident report notes the loader was positioned under an unsupported back at the time",
          "Ground conditions log shows the affected section had elevated joint density flagged the previous shift",
          "Equipment operator states he followed the marked safe-operating zone"
        ],
        "new_information_after_decision": [
          "Incident is logged primarily as an operator positioning error",
          "A later scaling inspection finds loose ground beyond the marked zone, consistent with the joint density flag"
        ],
        "alternatives": [
          "Attribute the incident primarily to operator positioning error",
          "Attribute the incident primarily to unaddressed ground conditions flagged the prior shift",
          "Treat the cause as undetermined pending a joint investigation"
        ],
        "intended_action": "Engineer attributes the fall of ground mainly to the operator's positioning decision rather than to the previously flagged ground conditions."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Updated stability model returns a Panel 5 factor of safety of 1.42, calculated using Panel 3 calibration parameters",
          "Field scaling crew reports intermittent minor spalling not reflected in the model inputs",
          "Mine manager requests final go/no-go confirmation to fire the next ring",
          "Chief geotechnical engineer's full 48-hour review is still twelve hours from completion"
        ],
        "new_information_after_decision": [
          "Ring is fired on schedule",
          "Post-blast inspection finds greater-than-modeled fracturing near the fault splay, prompting an unplanned support upgrade"
        ],
        "alternatives": [
          "Approve firing based on the model's calculated factor of safety",
          "Delay firing until the geotechnical review is complete",
          "Approve firing with additional interim scaling and monitoring as a condition"
        ],
        "intended_action": "Engineer approves firing, treating the model's 1.42 factor of safety as a precise and sufficient basis while also expressing personal confidence in his ability to manage any ground issues that arise."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role in the Panel 4 to Panel 5 transition.",
        "Walk me through what a typical shift handover looked like before this incident."
      ],
      "timeline_reconstruction": [
        "What did you know when you first heard about the overnight seismic event?",
        "What happened between the seismic alert and the decision to specify support for Panel 5?",
        "Take me through the sequence of events around the fall-of-ground incident.",
        "What information did you have right before authorizing the final ring firing?"
      ],
      "decision_point_probes": [
        "What cues told you the seismic reading was or wasn't a concern?",
        "What sources of information did you weigh most heavily when choosing the support pattern, and why?",
        "What alternatives did you consider before deciding what caused the fall of ground?",
        "What was your basis for approving the firing given the outstanding geotechnical review?",
        "Had you handled a similar situation before? How did that shape your decision this time?",
        "How much time pressure did you feel at each of these moments?",
        "How confident were you in each decision at the time you made it?",
        "What would you have needed to see to decide differently?"
      ],
      "closing_hypotheticals": [
        "If the geotechnical review had come back before you had to decide, what might you have done differently?",
        "If Panel 5 had shown no visual similarity to Panel 3, would your support decision have changed?",
        "Looking back, what single piece of information, if available earlier, would have most changed your approach?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Status quo bias",
        "decision_point": 1,
        "mechanism": "Engineer defaults to continuing the pre-existing firing schedule despite a new seismic signal, treating deviation from the established plan as requiring more justification than continuation of the plan.",
        "affected_reasoning_operation": "Evaluation of whether to change an existing operational plan in light of new monitoring data",
        "evidence_available_at_time": [
          "Seismic event overnight near Panel 4 abutment",
          "Convergence readings modestly above trailing average",
          "Geotech team's request for 48-hour review window"
        ],
        "required_textual_manifestation": "Engineer explains continuing the schedule primarily by reference to it being the established procedure or the way things have always been run, rather than a fresh risk-based justification for that specific reading.",
        "plausible_nonbias_interpretation": "The reading may genuinely fall within normal operating variation and continuing could be a defensible engineering judgment based on threshold criteria.",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "default bias", "inertia"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Experience Bias",
        "decision_point": 2,
        "mechanism": "Engineer generalizes a personally successful past support design from Panel 3 to Panel 5 based on surface similarity, discounting Panel 5's distinct exploration data showing different joint orientation and a fault splay.",
        "affected_reasoning_operation": "Transfer of a prior solution to a new case based on recalled personal success rather than re-evaluation of case-specific evidence",
        "evidence_available_at_time": [
          "Panel 3 support pattern history and personal design authorship",
          "Panel 5 exploration drilling data showing different joint orientation and fault splay",
          "Contractor's request for confirmation of pattern choice"
        ],
        "required_textual_manifestation": "Engineer justifies reusing the Panel 3 pattern mainly by citing personal past success with it, without independently weighing the differing exploration data for Panel 5.",
        "plausible_nonbias_interpretation": "Reusing a proven design could be a reasonable efficiency measure if the engineer believed the differences were immaterial to support requirements.",
        "strength": "moderate",
        "do_not_make_explicit": ["experience bias", "overgeneralization", "past success bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Attribution Bias",
        "decision_point": 3,
        "mechanism": "Engineer attributes the fall-of-ground incident predominantly to the equipment operator's positioning choice (a dispositional/behavioral cause) while underweighting the previously logged ground-condition flag (a situational cause).",
        "affected_reasoning_operation": "Causal attribution of an adverse event to person versus situation given conflicting evidence",
        "evidence_available_at_time": [
          "Incident report noting operator positioning under an unsupported back",
          "Ground conditions log flagging elevated joint density the previous shift",
          "Operator's statement that he followed the marked safe-operating zone"
        ],
        "required_textual_manifestation": "Engineer's account of the incident foregrounds the operator's positioning decision as the primary cause and treats the joint density flag as a secondary or incidental detail, despite both being available at the time.",
        "plausible_nonbias_interpretation": "The operator may indeed have deviated from the marked zone, making a behavior-focused explanation a legitimate partial account.",
        "strength": "subtle",
        "do_not_make_explicit": ["attribution bias", "fundamental attribution error", "blame"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of validity",
        "decision_point": 4,
        "mechanism": "Engineer treats the model-derived factor of safety (1.42) as a precise and reliable indicator of ground stability, despite it being calculated from Panel 3 calibration parameters and conflicting with fresh field spalling observations.",
        "affected_reasoning_operation": "Weighting of a quantitative model output versus qualitative field observation when forming a confidence judgment about ground stability",
        "evidence_available_at_time": [
          "Stability model output of FOS 1.42 using Panel 3 calibration parameters",
          "Field scaling crew reports of intermittent minor spalling not reflected in model inputs",
          "Outstanding geotechnical review not yet complete"
        ],
        "required_textual_manifestation": "Engineer describes the numerical FOS value as a firm basis for the go decision, referencing its precision or specificity, while treating the field spalling reports as not requiring a revision of that judgment.",
        "plausible_nonbias_interpretation": "A calculated FOS above 1.0 is a legitimate standard industry threshold, so relying on it could reflect a reasonable, if incomplete, decision rule.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "false precision", "model overreliance"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Engineer expresses high personal confidence in his own ability to manage or respond to any ground issues that might arise after firing, distinct from and in addition to his reliance on the model output itself.",
        "affected_reasoning_operation": "Self-assessment of personal capability to control or mitigate uncertain future outcomes",
        "evidence_available_at_time": [
          "Personal track record of managing prior ground-support issues",
          "Outstanding uncertainty in the geotechnical review",
          "Mine manager's request for a firm go/no-go answer"
        ],
        "required_textual_manifestation": "Engineer states confidence in his personal capacity to handle whatever ground issues emerge, framed as a reason to proceed, separate from the model's numerical output.",
        "plausible_nonbias_interpretation": "Confidence grounded in genuine relevant experience and contingency planning could be a legitimate professional judgment rather than miscalibration.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence bias", "miscalibration", "self-assessment error"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the biased-condition scenario with no paired control specified in this generation cycle."
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
      "Confirm exactly four decision points exist and each has at least two plausible alternatives.",
      "Confirm each of the five requested biases has exactly one embedded instance with a unique instance_id.",
      "Confirm decision point 4 hosts two distinct instances (cb_04, cb_05) with different evidence sources (model output vs. self-assessed capability) and different reasoning operations.",
      "Confirm no bias label, definition, or psychological term appears in the planned interview text.",
      "Confirm each occurrence includes a plausible non-bias interpretation to avoid mechanical proof of bias.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm projected interview length falls between 1,215 and 1,485 words without repetitive exposition.",
      "Confirm technical vocabulary matches underground hard-rock mining and mine planning terminology throughout."
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
