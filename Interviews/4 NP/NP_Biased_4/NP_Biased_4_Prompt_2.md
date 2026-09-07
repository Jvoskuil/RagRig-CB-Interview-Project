You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "NP_Biased_4",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Field Operator / Equipment Operator (Nuclear)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Post-Maintenance AFW Train Realignment and Escalating Bearing Anomaly",
    "scenario_summary_internal": "A field operator returns Auxiliary Feedwater (AFW) Pump Train B to service following planned maintenance on a discharge check valve. During the post-maintenance walkdown, startup, and monitoring rounds, the operator must verify valve lineup against a modified procedure, interpret an elevated bearing temperature reading in light of a recent unrelated instrument glitch, triage multiple simultaneous abnormal cues of different vividness, and finally decide whether to continue running the train or initiate a trip and swap to the redundant train under time pressure before a required surveillance window closes.",
    "occupational_realism": {
      "objective": "Restore AFW Pump Train B to operable status after maintenance and complete required post-maintenance testing before the surveillance deadline, without introducing a plant transient or violating technical specifications.",
      "setting": "Nuclear power plant auxiliary building, AFW pump room, mid-shift during a scheduled maintenance outage window, field operator working with a control room operator via radio",
      "constraints": [
        "Fixed surveillance test window (Tech Spec LCO) closing in under two hours",
        "Radiological and industrial safety requirements limiting time in the pump room",
        "Only one other AFW train available as backup, creating pressure to avoid unnecessary trips",
        "Recent history of a nuisance/spurious alarm on a similar instrument loop",
        "Communication lag between field operator and control room during radio traffic congestion"
      ],
      "stakeholders": [
        "Field Operator (interviewee)",
        "Control Room Supervisor",
        "Maintenance technician who performed the check valve work",
        "Shift Technical Advisor",
        "Oncoming shift crew"
      ],
      "technical_terms_to_use": [
        "Auxiliary Feedwater (AFW)",
        "check valve",
        "valve lineup",
        "post-maintenance testing (PMT)",
        "bearing temperature",
        "vibration monitoring",
        "Tech Spec LCO",
        "surveillance window",
        "local control station",
        "trending",
        "RTD (resistance temperature detector)"
      ],
      "technical_terms_to_avoid": [
        "recency bias",
        "habit intrusion",
        "bounded rationality",
        "salience bias",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Standard AFW valve lineup checklist from the routine surveillance procedure",
          "A maintenance work order note stating an additional isolation valve was installed downstream of the check valve for the repair",
          "Verbal handover from the prior shift mentioning the valve change only in passing"
        ],
        "new_information_after_decision": [
          "The added isolation valve is found mid-lineup in a non-standard position",
          "Control room later confirms the valve should have been verified open per the updated work order attachment"
        ],
        "alternatives": [
          "Follow the familiar routine lineup sequence from memory as done hundreds of times before",
          "Stop and cross-check the current valve lineup against the specific post-maintenance work order attachment before proceeding"
        ],
        "intended_action": "Operator begins the lineup using the well-practiced routine sequence, walking past the new valve position without pausing to verify it against the modified paperwork."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Bearing temperature RTD reads slightly above normal band on pump start",
          "One week earlier, an unrelated RTD on a similar pump gave a false high reading traced to a wiring fault, later corrected",
          "Current trend data from the plant computer showing a slow but steady rise over the last 15 minutes is available on request"
        ],
        "new_information_after_decision": [
          "The trend data, if pulled, would show the rise is steeper and more sustained than the earlier false-alarm case",
          "Maintenance later confirms the RTD wiring on this pump was inspected and found intact, meaning the reading was likely real"
        ],
        "alternatives": [
          "Treat the elevated reading as most likely another instrument glitch similar to the recent case and continue monitoring informally",
          "Pull the full trend history and request an independent verification reading before proceeding further"
        ],
        "intended_action": "Operator attributes the reading primarily to the recently experienced false-alarm pattern and defers a full trend review, continuing the startup sequence."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A loud, intermittent mechanical knocking noise from the pump coupling area, clearly audible over the room's ambient noise",
          "A less noticeable but continuous upward drift in the bearing temperature trend visible only on the local gauge",
          "A faint, easily overlooked odor near the oil reservoir consistent with early seal degradation"
        ],
        "new_information_after_decision": [
          "The knocking noise is later attributed to a loose coupling guard, unrelated to the developing problem",
          "The bearing temperature and oil condition, once checked afterward, show the more diagnostic combination the operator initially set aside"
        ],
        "alternatives": [
          "Focus attention and the radio report on the loud knocking noise as the primary concern",
          "Systematically check all three cues (noise, temperature trend, odor) with equal weight before reporting anything"
        ],
        "intended_action": "Operator's attention and radio report to the control room center almost entirely on the loud knocking sound, mentioning the temperature and odor only briefly and without emphasis."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Surveillance window closing in under 30 minutes",
          "Partial, somewhat conflicting data on noise, temperature, and odor gathered across the shift",
          "Backup AFW train available but swapping trains requires additional coordination and paperwork",
          "Shift Technical Advisor available by radio but currently occupied with another issue"
        ],
        "new_information_after_decision": [
          "Post-event review shows a more complete data pull (full trend, vibration spectrum, oil sample) was feasible in the time available but was not fully pursued",
          "The train is later found to have degrading bearing lubrication requiring unplanned maintenance"
        ],
        "alternatives": [
          "Take the extra time to gather complete diagnostic data before deciding, even if it risks missing the surveillance window",
          "Make a quick judgment call based on the readily available partial information to keep the schedule on track"
        ],
        "intended_action": "Operator settles on a workable-enough combination of the partial cues gathered, decides to continue running the train to complete the surveillance on time, without exhaustively weighing all available diagnostic options."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you were asked to do at the start of this shift?",
        "What was your understanding of the operational goal before you began the lineup?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do immediately after?",
        "At what point did you first notice something might be different from a routine lineup or startup?",
        "How did the sequence of events unfold from the pump start to the final decision?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you at that moment?",
        "What alternatives did you consider before acting?",
        "Why did you choose that option over the other one?",
        "Had you handled a similar situation before? How did that shape your response?",
        "How much time pressure did you feel at that point?",
        "How confident were you in the information you were using?",
        "What sources of information did you check, and which ones did you not check?"
      ],
      "closing_hypotheticals": [
        "If the maintenance work order attachment had been handed to you directly instead of mentioned verbally, would anything have changed?",
        "If the earlier false-alarm instrument event had not happened the week before, would you have responded differently to the temperature reading?",
        "If the knocking noise had been quieter, do you think the temperature trend would have gotten more attention?",
        "Looking back, is there anything you would do differently with the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "decision_point": 1,
        "mechanism": "Operator executes the highly familiar, frequently-practiced routine valve lineup sequence from memory, and this overlearned pattern intrudes over the need to consult the modified, non-routine work order documentation for the newly added valve.",
        "affected_reasoning_operation": "Procedural execution / lineup verification",
        "evidence_available_at_time": [
          "Routine lineup checklist",
          "Work order note mentioning an added valve",
          "Brief verbal shift handover"
        ],
        "required_textual_manifestation": "Operator describes proceeding through the lineup 'the way I always do it' or similar, walking past or handling the new valve using the standard sequence rather than pausing to check the modified paperwork, later realizing the valve was not verified per the updated attachment.",
        "plausible_nonbias_interpretation": "The operator could argue the verbal handover was sufficient and time constraints justified relying on the standard sequence.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "habit intrusion",
          "automaticity",
          "overlearned behavior"
        ]
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "decision_point": 2,
        "mechanism": "Operator's interpretation of the elevated bearing temperature is disproportionately anchored on the most recently experienced similar event (last week's false-alarm RTD) rather than on the full available trend data or base rate of real versus spurious readings.",
        "affected_reasoning_operation": "Diagnostic interpretation of an instrument reading",
        "evidence_available_at_time": [
          "Current RTD reading slightly above normal",
          "Memory of last week's unrelated false-alarm RTD event",
          "Available but unpulled 15-minute trend data"
        ],
        "required_textual_manifestation": "Operator explicitly connects the current reading to the recent false-alarm case as the primary basis for downplaying it, without describing having reviewed the actual trend data at that time.",
        "plausible_nonbias_interpretation": "The operator could argue pattern-matching to a recent, verified false alarm was a reasonable time-saving judgment given workload.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "recency bias",
          "recent event weighting",
          "availability of memory"
        ]
      },
      {
        "instance_id": "sb_01",
        "bias": "Salience Bias",
        "decision_point": 3,
        "mechanism": "Operator's attention and reporting are captured disproportionately by the most perceptually vivid and attention-grabbing cue (loud knocking noise) while the less vivid but more diagnostically relevant cues (temperature trend, odor) receive minimal attention or reporting.",
        "affected_reasoning_operation": "Cue selection and triage / information reporting",
        "evidence_available_at_time": [
          "Loud intermittent knocking noise",
          "Continuous but visually subtle bearing temperature drift",
          "Faint oil odor"
        ],
        "required_textual_manifestation": "Operator's account of the radio report and personal focus centers heavily on the noise, with the temperature and odor mentioned only in passing or as an afterthought, despite all three being observable at the time.",
        "plausible_nonbias_interpretation": "The operator could argue the noise posed an immediate mechanical safety concern warranting priority attention.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "salience bias",
          "vividness",
          "attention capture"
        ]
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "decision_point": 4,
        "mechanism": "Under time pressure and incomplete information, the operator settles for a workable, 'good-enough' combination of partially gathered cues to reach a decision, rather than systematically pursuing available additional diagnostics (full trend, vibration spectrum, oil sample) that were feasible within the remaining time.",
        "affected_reasoning_operation": "Final go/no-go judgment integrating multiple partial evidence streams",
        "evidence_available_at_time": [
          "Partial, somewhat conflicting cues from noise, temperature, and odor",
          "Time remaining before surveillance window closes",
          "Availability of a backup train and of the Shift Technical Advisor"
        ],
        "required_textual_manifestation": "Operator describes stopping short of a full systematic evaluation of all available diagnostic options, instead combining the readily-at-hand partial information into a workable judgment to keep the train running and meet the schedule.",
        "plausible_nonbias_interpretation": "The operator could argue that pursuing every diagnostic option was operationally impractical given genuine time constraints.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "bounded rationality",
          "satisficing",
          "imperfect rationality"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control generated in this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Completeness of shift handover documentation regarding the added isolation valve and prior instrument trend history",
      "original_state": "Handover was verbal and incomplete; the work order attachment and full trend history were not proactively provided to the field operator",
      "counterfactual_state": "Handover includes the written work order attachment for the added valve and a printed trend summary for the RTD, both handed directly to the field operator before the lineup begins",
      "variables_to_hold_constant": [
        "Operational objective and surveillance deadline",
        "Personnel involved (same field operator, control room supervisor, maintenance technician)",
        "Physical plant conditions and equipment configuration",
        "Sequence of the four decision points",
        "Time pressure magnitude"
      ],
      "expected_causal_difference": "With complete documentation provided upfront, the habit-intrusion and recency-bias manifestations at decision points 1 and 2 would be expected to diminish, since the operator would have direct, salient documentary cues correcting reliance on routine memory and recent-event pattern-matching.",
      "causal_test_question": "Does providing complete written handover documentation (valve change order and trend summary) reduce reliance on routine memory and recent-event pattern-matching at the lineup and diagnostic-interpretation decision points?"
    },
    "generation_checks": [
      "Confirm exactly four decision points are present and sequential.",
      "Confirm exactly one instance each of Recency Bias, Habit Intrusion, Imperfect Rationality, and Salience Bias is embedded, each at a distinct decision point.",
      "Confirm the Habit Intrusion instance textually reflects the mechanism_constraint (familiar, frequently-occurring behavioral pattern).",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm each decision point offers at least two plausible alternatives with before/after information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 (acceptable 1,215–1,485) is achievable without repeating any single bias manifestation.",
      "Confirm consequences described do not deterministically prove any decision was biased."
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
