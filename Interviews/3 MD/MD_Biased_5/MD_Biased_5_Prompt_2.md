You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MD_Biased_5",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Battalion Operations Officer (S3)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Route BLUE Crossing: Delayed Bridge Reclassification Incident",
    "scenario_summary_internal": "A mechanized infantry battalion S3 must secure a river crossing (Route BLUE) within a compressed timeline to enable brigade's follow-on attack. Ambiguous enemy reconnaissance activity, a brigade-directed continuation of the original axis, and a staff planning session that converges too quickly on the existing crossing plan (despite a new engineer bridge-classification report) precede a crossing attempt that encounters partial bridge failure and enemy contact. The post-incident CTA interview captures the S3's chronological account and reflections.",
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
          "S2 flags the deviation as worth re-tasking ISR, but battalion has already committed to the original recon plan"
        ],
        "alternatives": [
          "Request additional ISR retasking to confirm whether the scout sighting represents a deviation from the known enemy template before finalizing the reconnaissance-in-force plan",
          "Proceed with the existing reconnaissance-in-force plan on the assumption the sighting is a normal variant of the known company defense template"
        ],
        "intended_action": "S3 treats the atypical sighting as consistent with the familiar enemy template and proceeds with the unmodified reconnaissance plan."
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
          "Engineer officer completes a fuller bridge classification later than planned, after the crossing plan is already locked in with brigade",
          "Brigade acknowledges the concern only after the battalion has already committed forces to the axis"
        ],
        "alternatives": [
          "Push back to brigade requesting a short delay to complete bridge reinforcement or reconnoiter the alternate ford before committing heavy vehicles",
          "Comply with brigade's direction to continue on Axis BLUE without altering the crossing timeline, given the synchronized attack requirement"
        ],
        "intended_action": "S3 defers to brigade's directive to continue on the original axis largely because brigade has prioritized timeline over the unresolved bridge concern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engineer officer presents a bridge classification report suggesting overweight risk for the battalion's heaviest vehicles",
          "The crossing plan has already been briefed to brigade and rehearsed by lead companies",
          "Staff members raise the report but no one proposes rerouting before the commander's planning session ends",
          "The alternate ford exists but has not been reconned in current water conditions"
        ],
        "new_information_after_decision": [
          "Post-session, one company commander privately notes he had reservations about the bridge but did not voice them in the session",
          "The alternate ford is later found passable, but only after the crossing attempt has already begun"
        ],
        "alternatives": [
          "Reroute the battalion's heavy vehicles to the alternate ford despite the added reconnaissance and rehearsal burden",
          "Retain the original bridge crossing plan on the grounds that it is already rehearsed, briefed to brigade, and requires no further coordination"
        ],
        "intended_action": "The staff converges quickly on retaining the existing bridge crossing plan; the session ends with unanimous, largely unchallenged agreement despite the unresolved load-capacity concern."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The crossing attempt results in a partial bridge failure under a heavy vehicle and near-simultaneous enemy contact from dismounts near the crossing site",
          "The battalion executes a hasty branch plan to secure the site and complete the crossing via the alternate ford",
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
        "intended_action": "During the interview, the S3 characterizes the earlier scout sighting as an obvious warning sign of the ambush, asserting the outcome was foreseeable given what 'was clearly there all along.'"
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
        "What cues made you interpret the scout sighting the way you did?",
        "What sources of information did you weigh most heavily when deciding whether to continue the recon plan?",
        "When brigade directed continuation on Axis BLUE, what alternatives did you consider, and why did you choose the one you did?",
        "During the planning session, how did the staff resolve the disagreement or concern about the bridge report?",
        "What was your basis for keeping the original crossing plan rather than rerouting?"
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
        "If you had more time before the crossing, what would you have done differently?",
        "Looking back, what do you think the early indicators tell you about how predictable the outcome was?",
        "If the alternate ford had been reconned earlier, how might the planning session have gone differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "MD5_b01",
        "bias": "Representativeness Heuristic",
        "decision_point": 1,
        "mechanism": "S3 classifies the atypical scout sighting as belonging to the familiar enemy company-defense template based on surface similarity to past patterns, rather than weighing the specific locational deviation.",
        "affected_reasoning_operation": "Categorization of new evidence against a prior mental template",
        "evidence_available_at_time": [
          "Atypical scout vehicle location relative to templated defensive belt",
          "Three months of consistent pattern-of-life data showing screening from NAI 12"
        ],
        "required_textual_manifestation": "S3 explicitly states the sighting was treated as a normal variant of the known template and that this is why no plan modification or ISR retasking was requested.",
        "plausible_nonbias_interpretation": "Given limited ISR availability and a tight timeline, relying on a well-validated template could be framed as a reasonable economy-of-effort judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["representativeness", "heuristic", "template bias"]
      },
      {
        "instance_id": "MD5_b02",
        "bias": "Authority Bias or Higher-level prioritization Bias",
        "decision_point": 2,
        "mechanism": "S3 defers to brigade's directive to continue on Axis BLUE primarily because it originates from a higher headquarters, muting his own unresolved concern about bridge capacity rather than escalating it formally.",
        "affected_reasoning_operation": "Weighting of directive source over unresolved technical risk in a go/no-go judgment",
        "evidence_available_at_time": [
          "Brigade S3's verbal directive citing the synchronized attack timeline",
          "Battalion engineer's informal, unresolved concern about bridge load capacity"
        ],
        "required_textual_manifestation": "S3 states that he complied with brigade's directive largely because it came from brigade and the timeline was fixed, without describing an independent risk-weighing process.",
        "plausible_nonbias_interpretation": "Time-sensitive synchronization with a brigade main effort is a legitimate reason to prioritize compliance with a higher headquarters' timeline.",
        "strength": "moderate",
        "do_not_make_explicit": ["authority bias", "deference", "higher-level prioritization"]
      },
      {
        "instance_id": "MD5_b03",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "The staff planning session converges rapidly on retaining the existing plan with no one voicing dissent aloud, even though at least one company commander privately held reservations, indicating suppressed disagreement rather than genuine consensus.",
        "affected_reasoning_operation": "Group decision convergence and dissent suppression during collective evaluation of the bridge report",
        "evidence_available_at_time": [
          "Engineer's bridge classification report indicating overweight risk",
          "Staff members' brief mention of the report followed by no further challenge"
        ],
        "required_textual_manifestation": "S3 describes the session as reaching quick, unanimous agreement to keep the plan, and separately notes (or a probe reveals) that a company commander had unspoken reservations he did not raise.",
        "plausible_nonbias_interpretation": "A team with strong rapport and shared understanding may genuinely and legitimately agree quickly without any suppressed dissent.",
        "strength": "moderate",
        "do_not_make_explicit": ["groupthink", "consensus pressure", "suppressed dissent"]
      },
      {
        "instance_id": "MD5_b04",
        "bias": "Status Quo Bias",
        "decision_point": 3,
        "mechanism": "The staff retains the original bridge crossing plan primarily because it is already rehearsed and briefed to brigade, treating the effort already invested in the existing plan as a reason to avoid the alternate ford rather than independently evaluating the new load-capacity evidence.",
        "affected_reasoning_operation": "Selection between two crossing options, anchored on the default (already-committed) plan",
        "evidence_available_at_time": [
          "The alternate ford as an unreconned but available option",
          "The fact that the existing plan was already rehearsed and briefed to brigade"
        ],
        "required_textual_manifestation": "S3 explains the choice to keep the original plan by referencing the rehearsal and brigade briefing already completed, rather than the risk data itself, as the deciding factor.",
        "plausible_nonbias_interpretation": "Avoiding an unreconned ford under time pressure could be a legitimate risk-mitigation choice independent of any default preference.",
        "strength": "moderate",
        "do_not_make_explicit": ["status quo bias", "default option", "sunk cost of rehearsal"]
      },
      {
        "instance_id": "MD5_b05",
        "bias": "Hindsight Bias",
        "decision_point": 4,
        "mechanism": "During the after-action interview, S3 characterizes the earlier scout sighting as an obvious, foreseeable warning of the ambush, overstating how predictable the outcome was given what was actually known at the time.",
        "affected_reasoning_operation": "Retrospective reconstruction of prior uncertainty into perceived foreseeability",
        "evidence_available_at_time": [
          "Consolidated after-action timeline showing the scout sighting, bridge report, and eventual contact",
          "S3's own prior account (decision point 1) describing the sighting as ambiguous at the time"
        ],
        "required_textual_manifestation": "S3 states in the interview that the sighting 'was clearly there all along' or equivalent, implying the outcome was obvious in advance, contrasting with his earlier real-time uncertainty.",
        "plausible_nonbias_interpretation": "With full knowledge of the eventual contact, it is reasonable to note the sighting was relevant in retrospect without claiming it was obviously predictive at the time.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "foreseeability", "retrospective distortion"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no paired control scenario specified for this generation (condition = biased)."
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
      "Exactly 4 decision points are present in the timeline.",
      "Exactly 5 total bias instances are planned, matching the manifest sum (1 each for 5 biases).",
      "No decision point contains more than one instance of the same bias.",
      "Decision point 3 contains two distinct biases (Groupthink, Status Quo Bias) with separated evidence sources (dissent suppression vs. rehearsal/briefing investment).",
      "No bias labels, definitions, or psychological terminology appear in the technical_terms_to_use list or planned interview text.",
      "Each occurrence has a distinct evidence trace and a plausible non-bias explanation.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given 4 decision points and probe density without repetitive exposition."
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
