You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MO_Vocab_Control_1",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Harbor Pilot / Marine Pilot",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Falling Tide: Piloting MV Kalliopi to Berth 7 (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A harbor pilot boards a fully laden container vessel for the same time-critical river transit as the paired scenario, facing an identical sequence of operational pressures: a closing tidal window, a barge encroaching a channel bend, a delayed tug under rising wind, and a cross-current final approach. Unlike the paired biased scenario, the pilot's handling of the initial under-keel clearance question integrates the fresh echo sounder report and updated tide gauge data into a genuinely revised risk judgment, rather than treating the original tide-table figure as controlling. All other decision points, vocabulary, actors, constraints, and narrative tone match the paired scenario, with no intentional instance of anchoring bias or any other named bias.",
    "occupational_realism": {
      "objective": "Safely pilot the fully loaded 300m container vessel MV Kalliopi up a dredged river channel and berth her at Berth 7 within a closing tidal window, without grounding, collision, or missing the berth slot.",
      "setting": "A single-channel river approach to a major European container terminal, falling tide, moderate wind rising through the transit, one moored barge partially encroaching the channel near a bend, two tugs assigned with one delayed at the pilot station.",
      "constraints": [
        "Fully loaded draft of 14.2m against a channel with historically tight under-keel clearance (UKC)",
        "Tidal window for safe transit closing within roughly 90 minutes",
        "Only one tug immediately available; second tug delayed 20-30 minutes",
        "Bow thruster effectiveness reduced due to deep draft",
        "VTS and berth operator expecting on-schedule arrival to avoid missing the berth slot",
        "Rising wind forecast (15 kt gusting higher) during the transit window"
      ],
      "stakeholders": [
        "Harbor Pilot (interviewee)",
        "Vessel Master",
        "Vessel Traffic Service (VTS) controller",
        "Tug captains",
        "Berth/terminal operator",
        "Outbound pilot who provided the real-time sounding report"
      ],
      "technical_terms_to_use": [
        "under-keel clearance (UKC)",
        "tide table / tidal window",
        "echo sounder sweep",
        "squat effect",
        "conning position",
        "VTS clearance",
        "bow thruster",
        "tug made fast",
        "set and drift",
        "passage plan"
      ],
      "technical_terms_to_avoid": [
        "anchoring bias",
        "cognitive bias",
        "heuristic",
        "confirmation bias",
        "psychological priming"
      ],
      "constraints_note": "No excluded themes specified; standard maritime pilotage vocabulary applies throughout, matched to the paired scenario."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pre-arrival tide table figure emailed by port control giving predicted UKC of 1.2m at planned transit time",
          "Vessel's static draft survey confirming 14.2m loaded draft",
          "Standard passage plan built around the 1.2m UKC figure and a fixed transit start time"
        ],
        "new_information_after_decision": [
          "An outbound pilot's real-time echo sounder sweep near km 4 of the channel reports shoaling reducing actual clearance to approximately 0.7m",
          "Updated tide gauge readings show the tide rising more slowly than the table predicted"
        ],
        "alternatives": [
          "Proceed on the original schedule, treating the tide-table UKC figure as still valid",
          "Delay departure roughly 40 minutes to allow the tide to rise further before entering the shoal area",
          "Reduce transit speed and take a slightly longer route favoring the deeper side of the channel"
        ],
        "intended_action": "The pilot cross-checks the outbound pilot's sounding against the vessel's own echo sounder readings and the updated tide gauge trend, weighs the combined margin against the vessel's draft and squat allowance, and elects to reduce speed and shift toward the deeper side of the channel rather than holding the original timing unchanged."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "A barge is moored closer to the channel bend than charted, narrowing the safe passing width",
          "VTS reports the barge operator is slow to respond to move requests",
          "Vessel speed at the bend affects steering response and squat"
        ],
        "new_information_after_decision": [
          "The barge shifts slightly further into the channel due to wake from a passing workboat",
          "VTS confirms no other vessel traffic is currently approaching from downstream"
        ],
        "alternatives": [
          "Request VTS coordinate an emergency shift of the barge before proceeding",
          "Reduce speed and favor the opposite bank with a wider passing margin",
          "Hold position briefly until the barge situation is confirmed resolved"
        ],
        "intended_action": "The pilot reduces speed and adjusts the vessel's track to favor the wider side of the bend, reassessing continuously as new width and current information arrives."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Wind has increased to 15 kt gusting higher than forecast",
          "Only one tug is currently made fast; the second tug is still 20 minutes out",
          "The vessel's limited bow thruster effectiveness at this draft"
        ],
        "new_information_after_decision": [
          "A harbor tug not originally assigned becomes available nearby and can assist sooner than the delayed second tug",
          "Gust strength briefly exceeds initial forecast during the approach"
        ],
        "alternatives": [
          "Proceed toward the berth with only one tug made fast, relying on thruster and rudder",
          "Wait at a safe holding position for the second assigned tug",
          "Request the nearer, unassigned harbor tug to assist immediately"
        ],
        "intended_action": "The pilot requests the nearer harbor tug to assist promptly rather than waiting for the originally assigned but delayed tug, weighing wind risk against schedule pressure."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "A cross-current is pushing the vessel off the planned berthing line during final approach",
          "Two tugs are now made fast and available for correction",
          "Berth structure and neighboring vessel proximity limit room for error"
        ],
        "new_information_after_decision": [
          "The correction with tug and thruster input brings the vessel back onto line, but with reduced margin to the neighboring berth",
          "The berth operator confirms mooring lines can be run despite the tighter approach angle"
        ],
        "alternatives": [
          "Continue the current approach and correct with tug and thruster power",
          "Abort the approach and circle for a fresh attempt",
          "Request maximum tug power immediately rather than gradual correction"
        ],
        "intended_action": "The pilot orders a graduated tug and thruster correction to regain the berthing line rather than aborting, judged against the vessel's response and available room."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you knew about this transit before you even boarded the vessel?",
        "What made this passage feel nonroutine compared to a typical transit up this channel?"
      ],
      "timeline_reconstruction": [
        "What happened right after you boarded, in the order it happened?",
        "At what point did new information start coming in about channel conditions, wind, or tug availability?",
        "How did the situation evolve between boarding and final berthing?"
      ],
      "decision_point_probes": [
        "At the moment you confirmed the passage plan, what specific numbers or reports were you weighing?",
        "When the updated sounding report came in, how did you factor it against the earlier tide-table figure?",
        "What alternatives did you consider when the barge encroached on the channel, and why did you choose the one you did?",
        "When the second tug was delayed and wind picked up, what options did you weigh before requesting the nearer tug?",
        "During the final berthing correction, what made you choose to continue rather than abort the approach?",
        "How much time did you have to decide at each of these points?",
        "How confident were you in the information available at each decision, and why?"
      ],
      "closing_hypotheticals": [
        "If the echo sounder report had come in before you left the pilot station rather than mid-transit, would your initial timing decision have changed?",
        "If the second tug had arrived on time, would your approach through the bend or the berthing correction have gone differently?",
        "Looking back, is there anything you would have wanted to know sooner?",
        "What would you tell a less experienced pilot to watch for in a transit like this one?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MO_Biased_1",
      "features_to_match": [
        "Domain vocabulary (UKC, tide table, echo sounder sweep, squat effect, conning position, VTS clearance, bow thruster, tug made fast, set and drift, passage plan)",
        "Four-decision-point structure and sequence (clearance/timing, barge at bend, tug/wind shortage, cross-current berthing)",
        "Stakeholder roster (Master, VTS, tug captains, berth operator, outbound pilot)",
        "Difficulty level (challenging) and time-pressure profile at each decision point",
        "Emotional tone: measured, professional, mild tension without alarm",
        "Word count target and probe plan structure"
      ],
      "features_to_remove_or_change": [
        "The pilot's treatment of the initial tide-table figure: in the control, the pilot integrates the new sounding and tide gauge data into a revised judgment rather than holding the original figure as controlling",
        "Any language suggesting the original estimate was retained despite superseding evidence"
      ],
      "ambiguity_boundary": "The decision at phase 1 must remain genuinely uncertain and challenging (tight margins, imperfect cross-vessel comparability of the sounding) but must show visible integration of the new evidence into the final judgment, not mere retention of the initial figure."
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
      "Confirm zero intentional instances of anchoring bias or any other named bias appear anywhere in the interview.",
      "Confirm decision point 1 shows explicit integration of the fresh echo sounder report and tide gauge trend into the pilot's revised risk judgment, not retention of the original 1.2m figure as controlling.",
      "Confirm decision points 2, 3, and 4 remain structurally and vocabulary-matched to the paired biased scenario.",
      "Confirm technical vocabulary list matches the paired scenario's technical_terms_to_use.",
      "Confirm difficulty, actor roster, constraint set, and emotional tone match the paired scenario.",
      "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given four decision points and full probe coverage.",
      "Confirm each decision point offers at least two plausible, distinct alternatives.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm no bias-labeling or psychological vocabulary appears anywhere in the interview."
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
