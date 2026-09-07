You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MO_Biased_5",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Chief Engineer (Marine Engineering)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Turbocharger Bearing Degradation Under Tide-Window Pressure",
    "scenario_summary_internal": "A Chief Engineer aboard a mid-size bulk carrier, three weeks after a costly main-engine turbocharger overhaul, encounters an emerging turbocharger bearing fault during a transit with a fixed tide-restricted berth deadline. Early ambiguous vibration/temperature signals are downplayed partly because the unit was just overhauled and the schedule is tight; automated monitoring readouts are trusted over manual sampling; a secondary fuel-filter differential-pressure cue is deprioritized while attention is fixed on the turbocharger; and after a partial bearing failure, the engineer presses on with a jury-rigged fix rather than diverting, again invoking the overhaul investment and lost troubleshooting time. In post-incident reflection, the engineer reconstructs the earliest signal as having been obviously predictive of failure.",
    "occupational_realism": {
      "objective": "Maintain safe propulsion while meeting a fixed tide-restricted berth window at the discharge port, managing an emerging turbocharger anomaly without unnecessary schedule loss following a recent expensive overhaul.",
      "setting": "Engine room and bridge of a geared bulk carrier, mid-ocean transit, approximately 30 hours from a port with a narrow tidal berthing window; main engine turbocharger overhauled three weeks earlier at significant cost and owner scrutiny.",
      "constraints": [
        "Fixed tide-restricted berth slot with no flexible arrival window",
        "Recent high-cost turbocharger overhaul under owner/technical-superintendent scrutiny",
        "Limited onboard spare parts (partial bearing kit only)",
        "Reduced engine room manning for continuous manual sampling",
        "Weather window closing behind the vessel, discouraging backtracking",
        "Fuel consumption targets tied to charter party terms"
      ],
      "stakeholders": [
        "Chief Engineer",
        "Second Engineer",
        "Master",
        "Technical Superintendent (shore)",
        "Class surveyor (post-incident)",
        "Port agent / charterer schedule coordinator"
      ],
      "technical_terms_to_use": [
        "turbocharger bearing",
        "exhaust gas temperature",
        "scavenge air pressure",
        "differential pressure",
        "lube oil sample",
        "jury rig",
        "load reduction",
        "class survey",
        "tide window",
        "engine monitoring system alarm"
      ],
      "technical_terms_to_avoid": [
        "sunk cost",
        "automation bias",
        "inattentional blindness",
        "hindsight bias",
        "cognitive bias",
        "heuristic",
        "confirmation"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Turbocharger overhaul completed 3 weeks prior at high cost, closely tracked by owners",
          "Minor elevated vibration and exhaust gas temperature deviation on one unit, within nominal alarm band",
          "Fixed tide-restricted berth window roughly 30 hours out",
          "No prior similar fault history on this specific turbocharger since overhaul"
        ],
        "new_information_after_decision": [
          "Readings stabilize temporarily, giving short-term reassurance",
          "No alarm is triggered in the following hours"
        ],
        "alternatives": [
          "Reduce load and inspect the turbocharger promptly",
          "Continue at full sea speed while monitoring the trend"
        ],
        "intended_action": "Continue at full sea speed, reasoning that a unit just overhauled at cost could not plausibly already be failing, and that stopping now would waste the overhaul investment and jeopardize the tide window."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engine monitoring system reports all turbocharger parameters back within green band",
          "No manual lube oil sample or bearing inspection has been taken since the initial deviation",
          "Second Engineer available to take a manual sample if requested",
          "Time pressure from the approaching tide window remains"
        ],
        "new_information_after_decision": [
          "System continues reporting nominal values for several hours with no new alarms",
          "Underlying bearing wear continues undetected beneath system thresholds"
        ],
        "alternatives": [
          "Order a manual lube oil sample and visual bearing check despite the clear system readout",
          "Accept the automated system readout as sufficient and proceed without manual verification"
        ],
        "intended_action": "Accept the automated monitoring system's clear readout as sufficient confirmation and forgo the manual sample, deferring inspection to the next scheduled maintenance."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief Engineer is closely watching the turbocharger dashboard given earlier concern",
          "Second Engineer reports during rounds that fuel filter differential pressure has risen moderately",
          "No abnormal fuel consumption or combustion symptoms observed yet",
          "Turbocharger readings remain the primary focus of attention at this moment"
        ],
        "new_information_after_decision": [
          "The fuel filter differential pressure rise turns out to be unrelated to any developing fault and resolves on its own",
          "No connection is later found between the filter reading and the turbocharger issue"
        ],
        "alternatives": [
          "Pause turbocharger monitoring briefly to investigate the fuel filter differential pressure rise",
          "Continue focused turbocharger monitoring and defer the fuel filter check to routine maintenance"
        ],
        "intended_action": "Continue focused turbocharger monitoring and defer the fuel filter differential pressure check, briefly acknowledging the Second Engineer's report without engaging with it."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Turbocharger exhibits a sudden exhaust temperature spike and audible vibration consistent with partial bearing failure",
          "Approximately 10 hours remain before the tide window closes",
          "Only a partial bearing repair kit is available onboard",
          "Significant time and money have already been invested in the recent overhaul and in troubleshooting so far",
          "Nearest port capable of proper repair would require diverting and missing the tide window"
        ],
        "new_information_after_decision": [
          "The jury-rigged fix holds at reduced load long enough to reach berth, but with continued risk of further degradation",
          "Class surveyor later confirms the bearing damage had been progressing for some time before the spike"
        ],
        "alternatives": [
          "Reduce to a safe minimal load and divert to the nearest port for a proper repair, missing the tide window",
          "Jury-rig a temporary fix and continue at reduced but still meaningful load to reach the original berth on schedule"
        ],
        "intended_action": "Jury-rig a temporary fix and press on at reduced load to preserve the overhaul investment and the time already spent troubleshooting, reaching berth on schedule rather than diverting."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe the voyage and the operational objective at the time this incident began.",
        "What was your role and what were you responsible for monitoring during this transit?"
      ],
      "timeline_reconstruction": [
        "Walk me through what happened from the first sign of trouble to the eventual repair.",
        "What did you observe first, and in what order did subsequent signals appear?"
      ],
      "decision_point_probes": [
        "At the point you first noticed the elevated vibration and temperature, what information did you have, and what alternatives did you weigh?",
        "When the monitoring system showed parameters back in the green band, what made you decide a manual check was or was not necessary?",
        "When the fuel filter differential pressure was reported, how did you decide where to direct your attention?",
        "When the bearing partially failed with limited time before the tide window, what options did you consider, and what tipped your decision?",
        "What prior experience with turbochargers or overhauls influenced how you read these signals?",
        "How much time pressure did you feel at each of these moments, and how did it factor into your decisions?",
        "How confident were you in the readings at each stage, and how did that confidence change?"
      ],
      "closing_hypotheticals": [
        "Looking back, how would you characterize the earliest vibration reading now that you know how things turned out?",
        "If the overhaul had not just been completed, do you think you would have responded differently to the first signal?",
        "If there had been no tide window deadline, would your decision at the point of partial failure have changed?",
        "What would you tell a junior engineer to watch for differently, based on this experience?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "MO5_SC_01",
        "bias": "Sunk cost bias",
        "decision_point": 1,
        "mechanism": "Reluctance to reduce load or inspect because the recent, costly overhaul is treated as evidence the unit cannot be failing, and stopping now would appear to waste that investment.",
        "affected_reasoning_operation": "Weighting of prior investment in the decision to continue vs. inspect",
        "evidence_available_at_time": [
          "Overhaul completed 3 weeks earlier at high cost",
          "Mildly elevated but in-band vibration/temperature readings",
          "Tide window approaching"
        ],
        "required_textual_manifestation": "Engineer explicitly links the decision to continue at full speed to the recency/cost of the overhaul rather than to the actual readings alone.",
        "plausible_nonbias_interpretation": "A reasonable engineer could judge mildly in-band readings as not yet warranting action, independent of overhaul cost.",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "investment bias", "loss aversion"]
      },
      {
        "instance_id": "MO5_AB_01",
        "bias": "Automation Bias",
        "decision_point": 2,
        "mechanism": "Treating the automated monitoring system's green-band readout as sufficient confirmation, foregoing an available and low-cost manual verification step.",
        "affected_reasoning_operation": "Evidence sufficiency judgment / verification-seeking behavior",
        "evidence_available_at_time": [
          "Automated system reporting nominal values",
          "No new alarms",
          "Second Engineer available to take manual sample"
        ],
        "required_textual_manifestation": "Engineer states that the system reading itself was treated as the deciding factor for not manually checking, despite the earlier anomaly.",
        "plausible_nonbias_interpretation": "Trusting a properly functioning, class-approved monitoring system is a legitimate operational default under normal circumstances.",
        "strength": "moderate",
        "do_not_make_explicit": ["automation bias", "over-reliance on automation"]
      },
      {
        "instance_id": "MO5_SA_01",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 3,
        "mechanism": "Attention narrowly fixed on the turbocharger dashboard causes the fuel filter differential pressure report to be acknowledged but not cognitively processed as an action-relevant cue.",
        "affected_reasoning_operation": "Attention allocation and cue registration among competing signals",
        "evidence_available_at_time": [
          "Turbocharger readings under active close monitoring",
          "Second Engineer's verbal report of rising fuel filter differential pressure"
        ],
        "required_textual_manifestation": "Engineer's account shows the filter report being briefly noted then set aside without engaging its implications, explicitly tied to the turbocharger being the focus at that moment.",
        "plausible_nonbias_interpretation": "Prioritizing an already-flagged system over an unconfirmed, isolated reading can be a defensible triage choice under workload constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["inattentional blindness", "selective attention", "tunnel vision"]
      },
      {
        "instance_id": "MO5_SC_02",
        "bias": "Sunk cost bias",
        "decision_point": 4,
        "mechanism": "Choosing to press on with a jury-rig rather than divert, justified by reference to the overhaul cost and the time already spent troubleshooting rather than solely by the present risk of continued operation.",
        "affected_reasoning_operation": "Weighting of prior time/cost investment in the choice between diverting and continuing",
        "evidence_available_at_time": [
          "Partial bearing failure signals (temperature spike, vibration)",
          "Limited spare parts kit",
          "Time and money already spent on overhaul and troubleshooting",
          "Tide window closing in ~10 hours"
        ],
        "required_textual_manifestation": "Engineer explicitly cites the money/time already spent as a reason to continue rather than basing the decision solely on the present state of the bearing and available repair capability.",
        "plausible_nonbias_interpretation": "Diverting has real, independent costs (missed tide window, charter penalties) that could justify pressing on regardless of prior investment.",
        "strength": "moderate",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment"]
      },
      {
        "instance_id": "MO5_HB_01",
        "bias": "Hindsight Bias",
        "decision_point": 4,
        "mechanism": "In retrospective reflection, the engineer recasts the ambiguous initial vibration/temperature signal as having been obviously predictive of the eventual failure, once the outcome is known.",
        "affected_reasoning_operation": "Retrospective causal attribution and memory reconstruction of the original signal's clarity",
        "evidence_available_at_time": [
          "Knowledge of the eventual bearing failure outcome",
          "Recollection of the phase-1 vibration/temperature reading, which was in-band at the time"
        ],
        "required_textual_manifestation": "In response to a closing hypothetical/reflection probe, the engineer describes the earliest signal as something that 'should have been obvious' or 'clearly meant trouble,' inconsistent with how it was actually treated as in-band at the time.",
        "plausible_nonbias_interpretation": "With full information, some signals genuinely are clearer in retrospect without any biased reconstruction of one's past confidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "creeping determinism", "knew-it-all-along"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; no control scenario requested for this generation."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence vs. absence of the fixed tide-restricted berth deadline (schedule time pressure)",
      "original_state": "A fixed tide-restricted berth window roughly 30 hours out creates continuous schedule pressure throughout the incident.",
      "counterfactual_state": "No tide restriction; the vessel has a flexible arrival window with no binding schedule deadline.",
      "variables_to_hold_constant": [
        "Turbocharger fault progression and physical failure mechanics",
        "Recent overhaul history and cost",
        "Crew composition and roles",
        "Automated monitoring system behavior",
        "Fuel filter differential pressure event"
      ],
      "expected_causal_difference": "Removing the schedule deadline should reduce or eliminate the schedule-linked pressing-on decision at decision point 4 and weaken the framing of decision point 1, if those instances are genuinely driven by time pressure rather than by the overhaul investment alone.",
      "causal_test_question": "Absent a fixed tide window, would the Chief Engineer still have chosen to jury-rig and continue rather than divert once the bearing partially failed?"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Exactly 5 total bias instances are planned, matching the manifest sum (2+1+1+1).",
      "No decision point hosts more than two instances of the same bias.",
      "Decision point 4 hosts two different biases (sunk cost, hindsight) via distinct reasoning operations and evidence sources.",
      "No bias-labeling or psychological terminology is scheduled to appear in the public interview.",
      "Each instance has a plausible non-bias explanation to avoid mechanical proof of bias from outcome alone.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points plus opening/closing probes without repetitive exposition."
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
