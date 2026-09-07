You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MD_Vocab_Control_5",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Battalion Operations Officer (S3)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Route BLUE Crossing: Balanced Bridge Reclassification Response",
    "scenario_summary_internal": "A mechanized infantry battalion S3 must secure a river crossing (Route BLUE) within a compressed timeline to enable brigade's follow-on attack. The same operational sequence as the paired incident occurs — an atypical enemy scout sighting, a brigade-directed continuation of the axis, a staff planning session addressing a new bridge-classification report, and a post-incident after-action interview — but at each point the participant and staff engage in balanced, evidence-weighed reasoning: information is actively sought, escalated, debated, or calibrated rather than defaulted, deferred, or suppressed. The crossing still encounters a partial bridge complication and enemy contact, but the account emphasizes genuine deliberation rather than any systematic reasoning shortcut.",
    "occupational_realism": {
      "objective": "Secure and hold Route BLUE river crossing to enable brigade's main-effort attack within a 48-hour window.",
      "setting": "Contested border corridor, mechanized infantry battalion task force, deteriorating weather, degraded FM/digital comms reliability.",
      "constraints": [
        "Single bridging asset (MGB) with limited engineer float capacity",
        "48-hour brigade timeline tied to a synchronized main-effort attack",
        "Intermittent SATCOM/FM comms degrading real-time intel updates",
        "Only one alternate ford, unrehearsed and unreconned in daylight",
        "Limited ISR assets already tasked to brigade's main effort"
      ],
      "stakeholders": [
        "Battalion Commander",
        "S3 (interviewee)",
        "S2 (Intelligence Officer)",
        "Battalion Engineer Officer",
        "Brigade S3",
        "Company Commanders (Route BLUE lead element)"
      ],
      "technical_terms_to_use": [
        "axis of advance",
        "movement to contact",
        "bridge classification",
        "reconnaissance-in-force",
        "main effort",
        "branch plan",
        "MGB (Mobile Gap-Crossing Bridge)",
        "named area of interest (NAI)",
        "template",
        "commander's critical information requirement (CCIR)"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "groupthink",
        "hindsight",
        "authority bias",
        "status quo bias",
        "representativeness"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "S2 reports enemy scout vehicles observed at an atypical location relative to the templated company defensive belt",
          "Prior three months of pattern-of-life data show enemy reconnaissance consistently screening from ridge NAI 12",
          "Weather forecast shows a closing window for aerial ISR support"
        ],
        "new_information_after_decision": [
          "A follow-up ground patrol later reports enemy dismounts moving toward the river crossing itself, not the ridge",
          "S2's retasked ISR request is partially filled before the weather window closes, giving an updated but incomplete picture"
        ],
        "alternatives": [
          "Request ISR retasking specifically to check whether the sighting represents a deviation from the known enemy template",
          "Proceed with the existing reconnaissance-in-force plan on the assumption the sighting is a normal variant of the known company defense template",
          "Split the difference: continue current planning while requesting a partial ISR look at the deviation before the window closes"
        ],
        "intended_action": "S3 weighs the location deviation explicitly against the pattern baseline, discusses it with S2, and authorizes a partial ISR retasking before the weather window closes, adjusting the reconnaissance plan's assumptions accordingly."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Brigade S3 directs continuation on Axis BLUE per the original brigade order, citing the synchronized attack timeline",
          "Battalion engineer has flagged a preliminary concern about bridge load capacity pending a full classification survey",
          "Battalion S3 has raised the bridge concern informally but has not yet received a written response from brigade"
        ],
        "new_information_after_decision": [
          "Brigade agrees to expedite the bridge classification survey in parallel with continued movement, rather than halting or ignoring the concern",
          "Engineer officer completes a fuller bridge classification on the accelerated timeline brigade approved"
        ],
        "alternatives": [
          "Formally request a short delay pending full bridge classification before committing heavy vehicles",
          "Comply with brigade's direction to continue on Axis BLUE without raising further conditions",
          "Continue movement while formally escalating the bridge concern and requesting an expedited classification survey as a parallel effort"
        ],
        "intended_action": "S3 formally escalates the bridge concern to brigade rather than dropping it informally, and negotiates an expedited classification survey to run in parallel with continued movement, balancing the synchronization requirement against the unresolved technical risk."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engineer officer presents a bridge classification report suggesting overweight risk for the battalion's heaviest vehicles",
          "The crossing plan has already been briefed to brigade and rehearsed by lead companies",
          "One company commander raises a concern about sequencing heavy vehicles and it is discussed openly in the session",
          "The alternate ford exists but has not been reconned in current water conditions"
        ],
        "new_information_after_decision": [
          "The staff adopts a modified vehicle sequencing plan that reduces peak load on the bridge while keeping the rehearsed route",
          "The alternate ford is later found passable, which becomes a documented branch option rather than an untested fallback"
        ],
        "alternatives": [
          "Reroute the battalion's heavy vehicles to the alternate ford despite the added reconnaissance and rehearsal burden",
          "Retain the original bridge crossing plan unchanged",
          "Retain the bridge crossing route but resequence vehicle order and stagger loads to mitigate the classified overweight risk"
        ],
        "intended_action": "The staff debates the report openly, weighs the sequencing mitigation against a full reroute, and adopts a modified sequencing plan that addresses the load concern while documenting the alternate ford as a formal branch option."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The crossing attempt encounters a bridge complication under a heavy vehicle and near-simultaneous enemy contact from dismounts near the crossing site",
          "The battalion executes the pre-identified branch plan to secure the site and complete the crossing via the alternate ford",
          "The interview occurs after the operation, during a formal after-action review"
        ],
        "new_information_after_decision": [
          "Casualty and equipment loss reports are finalized",
          "S2 compiles a consolidated timeline showing the scout sighting, the bridge report, and the contact, for the after-action review"
        ],
        "alternatives": [
          "Describe the sequence of events and decisions as they appeared at each point in time, acknowledging what was and was not knowable",
          "Characterize the enemy activity and bridge risk as having been clearly foreseeable indicators of the eventual outcome"
        ],
        "intended_action": "During the interview, the S3 gives a calibrated account distinguishing what was known at each point from what only became clear afterward, without overstating how predictable the outcome was from the earlier information."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through the overall mission and your role as S3 during this operation?",
        "What was the operational objective for Route BLUE, and why did it matter to brigade's plan?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through the sequence of reports you received from S2 and the engineer officer.",
        "When did brigade's directive on Axis BLUE come in, and what did you know before that call?"
      ],
      "decision_point_probes": [
        "What cues made you decide to request additional ISR on the scout sighting?",
        "What sources of information did you weigh most heavily when deciding how to handle the recon plan?",
        "When brigade directed continuation on Axis BLUE, what alternatives did you consider, and why did you choose the one you did?",
        "During the planning session, how did the staff resolve the disagreement or concern about the bridge report?",
        "What was your basis for adopting the sequencing mitigation rather than a full reroute or no change at all?"
      ],
      "cues_and_information_sources": [
        "What specific data or reports drove each of your calls?",
        "How reliable did you consider the engineer's preliminary bridge assessment versus the fuller classification?"
      ],
      "goals_and_alternatives": [
        "What competing goals were you balancing at each decision point?",
        "What other courses of action did you or the staff consider but set aside?"
      ],
      "prior_experience": [
        "Had you encountered a similar enemy templated defense before, and how did that shape your read of the situation?",
        "Has your battalion faced a similar bridge or crossing constraint on past operations?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure were you under at each of these points?",
        "What were you most uncertain about, and how did that uncertainty affect your decision?"
      ],
      "closing_hypotheticals": [
        "If you had less time before the crossing, what would you have had to change?",
        "Looking back, what do you think the early indicators tell you about how predictable the outcome was?",
        "If the alternate ford had been reconned earlier, how might the planning session have gone differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MD_Biased_5",
      "features_to_match": [
        "Domain vocabulary (axis of advance, bridge classification, reconnaissance-in-force, MGB, NAI, branch plan, CCIR, template)",
        "Four-decision-point structure mirroring the paired scenario's phases (scout sighting, brigade directive, bridge-report planning session, after-action reflection)",
        "Same actors and roles (S3 interviewee, S2, battalion engineer, brigade S3, company commanders)",
        "Same operational setting, constraints (single MGB, weather-limited ISR, 48-hour synchronization window, unreconned alternate ford)",
        "Same emotional tone: professional, reflective, moderate time pressure, no dramatization",
        "Same approximate difficulty and interview length/format (semi-structured CTA with opening, timeline reconstruction, four decision points, closing hypotheticals)"
      ],
      "features_to_remove_or_change": [
        "Remove template-neglect framing at decision point 1; replace with active reassessment and partial ISR retasking",
        "Remove source-weighted deference at decision point 2; replace with formal escalation and negotiated parallel classification",
        "Remove suppressed-dissent and incumbent-anchored framing at decision point 3; replace with open debate and a mitigation-based resolution",
        "Remove retrospective overstatement of foreseeability at decision point 4; replace with a calibrated, uncertainty-preserving account"
      ],
      "ambiguity_boundary": "The scenario may retain genuine operational uncertainty (e.g., incomplete ISR confirmation, unresolved water conditions at the ford) as long as the participant's reasoning process at each decision point demonstrates active weighing of alternatives and evidence rather than any systematic shortcut; no named bias should be inferable from the reasoning pattern."
    },
    "counterfactual_specification": {
      "causal_variable": "not_applicable",
      "original_state": "not_applicable",
      "counterfactual_state": "not_applicable",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "not_applicable",
      "causal_test_question": "not_applicable"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, mirroring the paired biased scenario's structure and vocabulary.",
      "Zero intended bias instances are embedded; each decision point shows explicit weighing of at least two alternatives with genuine evidence-based resolution.",
      "No bias labels, definitions, or psychological terminology appear anywhere in the planned interview text.",
      "Decision point 1 shows active retasking/reassessment rather than template-based dismissal of the location deviation.",
      "Decision point 2 shows formal escalation and negotiated parallel action rather than deference driven primarily by hierarchical source.",
      "Decision point 3 shows open debate and a mitigation-based resolution rather than rapid unchallenged convergence or incumbent-anchored preference.",
      "Decision point 4 shows a calibrated retrospective account that explicitly distinguishes real-time uncertainty from post-outcome clarity.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given 4 decision points and matched probe density without repetitive exposition."
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
