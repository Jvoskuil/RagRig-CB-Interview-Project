You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MU_Biased_6",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Mine Safety/Health & Safety Officer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Strata Noise Escalation in Stope 14-East",
    "scenario_summary_internal": "A Health & Safety Officer (HSO) at an underground hard-rock mine responds to a report of intermittent cracking/popping noise in the back (roof) of Stope 14-East during dayshift. Over several hours the HSO must weigh verbal reports, instrument telemetry (extensometer displacement, microseismic event counts), a veteran supervisor's informal read of the situation, and a widely publicized rockburst at a sister mine two months earlier, against production pressure to keep the stope running. A minor rock spall (no injuries) occurs later in the shift, prompting a post-event review and incident report in which the HSO must explain the escalation and assign contributing causes.",
    "occupational_realism": {
      "objective": "Determine, at four successive points during the shift, whether Stope 14-East can safely continue production or must be restricted/evacuated, and afterward produce an accurate incident account of a minor rock-spall event.",
      "setting": "Underground hard-rock mine, approximately 900m depth, longhole stoping method, instrumented with extensometers and a microseismic monitoring array; remote geotechnical engineer on-call, production quota deadline mid-shift.",
      "constraints": [
        "Production quota pressure from mine manager to avoid unnecessary stoppages",
        "Limited real-time geotechnical staff presence (engineer off-site, reachable by radio/phone only)",
        "Ground Control Management Plan (GCMP) specifies rate-of-change and event-count thresholds for escalation, not just absolute readings",
        "Two-month-old widely publicized rockburst at a sister operation still fresh in workforce/industry consciousness",
        "Shift-change occurring mid-incident, creating handover risk",
        "Time pressure: decisions must be made within minutes of each new data point"
      ],
      "stakeholders": [
        "Health & Safety Officer (HSO, protagonist)",
        "Veteran shift supervisor (22 years underground experience)",
        "Remote geotechnical engineer (on-call)",
        "Mine manager (production accountability)",
        "Ventilation/monitoring technician",
        "Miners working in Stope 14-East"
      ],
      "technical_terms_to_use": [
        "back (roof)",
        "extensometer",
        "microseismic event count",
        "displacement rate",
        "Ground Control Management Plan (GCMP)",
        "stope",
        "spall",
        "hang-up",
        "escalation threshold",
        "ground support"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "availability",
        "narrative fallacy",
        "attribution error",
        "confirmation",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Verbal report at 06:40 from a miner of intermittent cracking/popping sounds in the back of Stope 14-East",
          "No automated alarm triggered yet from the microseismic array",
          "Two months earlier, a rockburst at a sister mine (same ore body region) caused significant disruption and was widely covered in trade press and internal safety bulletins",
          "Production schedule requires Stope 14-East output today to meet weekly quota"
        ],
        "new_information_after_decision": [
          "Instrument technician confirms no alarm state at time of report",
          "Mine manager asks for an ETA on resuming full production"
        ],
        "alternatives": [
          "Immediately evacuate and halt work in Stope 14-East pending full geotechnical assessment",
          "Allow continued work with enhanced monitoring and a designated escape route review",
          "Request only an instrument check before deciding, without restricting access"
        ],
        "intended_action": "HSO orders enhanced monitoring and limited access rather than full evacuation, treating the verbal report as a high-probability precursor to a rockburst-type event, drawing heavily on the vivid recent sister-mine incident rather than current instrument state."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "05:00 baseline extensometer reading: 0.2mm displacement, logged as normal",
          "09:40 updated extensometer reading: 0.6mm displacement, a threefold increase over roughly 3 hours",
          "GCMP specifies escalation is triggered by displacement rate-of-change, not solely by absolute magnitude",
          "Ventilation technician confirms no other anomalies (gas, temperature) at this time"
        ],
        "new_information_after_decision": [
          "Microseismic technician reports event count for the shift is trending upward",
          "Mine manager reiterates production timeline"
        ],
        "alternatives": [
          "Treat the displacement trend as within acceptable range relative to the morning baseline and continue normal operations",
          "Recalculate against the GCMP rate-of-change threshold and restrict access pending geotechnical sign-off",
          "Order immediate reinstallation of additional ground support before any further work"
        ],
        "intended_action": "HSO judges the 0.6mm reading as still 'normal' because it is compared against the initial 0.2mm baseline rather than evaluated against the GCMP's rate-of-change escalation threshold, and authorizes continued limited work."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Veteran shift supervisor (22 years) recalls similar popping sounds from 2009 that resolved without incident and voices confidence the current situation is 'nothing'",
          "Microseismic event count has now reached 6 events/hour, at the GCMP's stated escalation flag of 5 events/hour",
          "A hairline crack (approx. 1mm width) was photographed and logged as insignificant the previous week in the same panel",
          "Geotechnical engineer has not yet called back"
        ],
        "new_information_after_decision": [
          "Engineer eventually calls back and requests the day's full event-count log",
          "A second, wider crack is noticed near the original hairline crack location"
        ],
        "alternatives": [
          "Follow the GCMP microseismic threshold and restrict the stope pending engineer review",
          "Defer to the supervisor's experiential read and permit continued limited access",
          "Split the difference: reduce crew size but keep the stope open"
        ],
        "intended_action": "HSO permits continued limited access, weighting the supervisor's tenure-based recollection of a past, unrelated event as strong evidence the current situation is benign, and separately evaluates today's crack photos against last week's 1mm reference rather than against the newly reached microseismic threshold."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "A minor rock spall occurred in Stope 14-East at 13:15; no injuries, minor equipment damage",
          "Overnight temperature had dropped several degrees before the shift",
          "Shift change occurred approximately 90 minutes before the spall",
          "Blasting in an adjacent panel had occurred the previous week",
          "GCMP escalation protocol required a documented engineer sign-off before continued access after the 6 events/hour flag, which had not been completed"
        ],
        "new_information_after_decision": [
          "Incident report is submitted to the mine manager and regulator liaison",
          "Geotechnical engineer's later analysis notes multiple plausible contributing factors, none confirmed as dominant"
        ],
        "alternatives": [
          "Report the spall as resulting from a specific, well-defined causal chain (temperature drop plus shift-change vigilance lapse plus prior blasting)",
          "Report the event as multifactorial with several unresolved contributing conditions",
          "Attribute the escalation primarily to systemic gaps in escalation follow-through rather than to any single factor or individual"
        ],
        "intended_action": "HSO writes an incident narrative that links the temperature drop, shift change, and prior blasting into a single coherent causal story, and assigns primary responsibility for the escalation to the on-shift miner's delayed reporting rather than to the unresolved GCMP sign-off gap."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were doing when you first heard about the noise in Stope 14-East.",
        "What was your overall objective during this shift?"
      ],
      "timeline_reconstruction": [
        "What happened right after the 06:40 report came in?",
        "What did the extensometer readings show at each check, and when did you see them?",
        "When did you speak with the shift supervisor, and what did that conversation cover?",
        "Walk me through what happened between the 09:40 reading and the spall at 13:15."
      ],
      "decision_point_probes": [
        "At 06:40, what information sources did you weigh, and how did you weigh them against each other?",
        "What alternatives did you consider before deciding on enhanced monitoring instead of evacuation?",
        "When you compared the 09:40 reading to the morning baseline, what made you conclude it was still acceptable?",
        "How did the supervisor's comments from 2009 factor into your access decision?",
        "How did you compare today's crack photos to last week's reading, and why?",
        "What alternatives to permitting continued access did you consider at that point?",
        "In writing the incident report, how did you decide which factors to include as causes?",
        "How did you decide where responsibility for the escalation belonged?"
      ],
      "closing_hypotheticals": [
        "If the sister-mine rockburst two months ago had never happened, do you think your first decision would have been different?",
        "If the GCMP's rate-of-change threshold had been displayed automatically alongside the raw reading, would your second decision have changed?",
        "If a less experienced supervisor had made the same comment, would you have weighted it the same way?",
        "Looking back, what would you tell a new HSO to watch for in a similar shift?",
        "How confident are you, in hindsight, that the causes you listed in the report are the real causes?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 1,
        "mechanism": "Ease of recall of a vivid, recent, widely publicized rockburst at a sister mine inflates perceived likelihood/severity of the current ambiguous auditory report, independent of current instrument data.",
        "affected_reasoning_operation": "Risk-likelihood estimation from an initial verbal cue",
        "evidence_available_at_time": [
          "Verbal report of intermittent cracking sounds",
          "No active alarm state",
          "Recollection of the sister-mine rockburst two months prior"
        ],
        "required_textual_manifestation": "HSO explicitly references the sister-mine event as the reason the noise felt urgent, disproportionate to what current instrumentation indicated.",
        "plausible_nonbias_interpretation": "A cautious safety officer reasonably erring toward caution given any recent industry incident, regardless of recall vividness.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability", "recall", "vividness", "bias"]
      },
      {
        "instance_id": "exp_01",
        "bias": "Experience Bias",
        "decision_point": 3,
        "mechanism": "Overweighting the supervisor's general tenure/seniority as validating evidence, without verifying that the supervisor's 2009 recollection actually shares the relevant geological or instrumentation conditions with today's situation.",
        "affected_reasoning_operation": "Credibility weighting of an informal expert opinion versus current threshold data",
        "evidence_available_at_time": [
          "Supervisor's verbal recollection of a 2009 event",
          "Current microseismic event count at the GCMP flag threshold",
          "No documented similarity check between 2009 conditions and today's panel"
        ],
        "required_textual_manifestation": "HSO cites the supervisor's years of experience as the primary reason for trusting the 'it's nothing' assessment, without probing whether the 2009 case matches today's specific conditions.",
        "plausible_nonbias_interpretation": "Reasonably valuing frontline tacit knowledge as one legitimate input among several.",
        "strength": "subtle",
        "do_not_make_explicit": ["experience bias", "seniority heuristic", "bias"]
      },
      {
        "instance_id": "anc_01",
        "bias": "Anchoring Bias",
        "decision_point": 2,
        "mechanism": "The initial 05:00 baseline extensometer reading serves as a reference point against which the later reading is judged 'still normal,' rather than applying the GCMP's rate-of-change threshold.",
        "affected_reasoning_operation": "Comparative evaluation of updated instrument data against a fixed initial reference",
        "evidence_available_at_time": [
          "05:00 baseline reading (0.2mm)",
          "09:40 updated reading (0.6mm)",
          "GCMP rate-of-change escalation criterion"
        ],
        "required_textual_manifestation": "HSO frames the 0.6mm reading relative to the 0.2mm baseline ('still low compared to this morning') instead of relative to the rate-of-change rule.",
        "plausible_nonbias_interpretation": "A reasonable simplification when a formal rate-of-change calculation is not immediately at hand.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "reference point", "bias"]
      },
      {
        "instance_id": "anc_02",
        "bias": "Anchoring Bias",
        "decision_point": 3,
        "mechanism": "The prior week's 1mm hairline crack photograph serves as the reference point for judging today's crack severity, displacing attention from the newly reached microseismic event-count threshold, a distinct evidence source and reasoning moment from anc_01's instrument-baseline anchor.",
        "affected_reasoning_operation": "Visual/photographic comparison of crack evidence against a prior fixed reference rather than integrating a separate concurrent data stream",
        "evidence_available_at_time": [
          "Photograph and log entry of last week's 1mm hairline crack, deemed insignificant",
          "Today's crack photos",
          "Microseismic event count reaching the 5 events/hour flag (now at 6)"
        ],
        "required_textual_manifestation": "HSO explicitly compares today's crack to last week's photo ('about the same as what we saw before') rather than cross-referencing the microseismic threshold that had just been reached.",
        "plausible_nonbias_interpretation": "Using recent, directly comparable visual history as a reasonable check when photographic baselines are readily available.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "reference photo", "bias"]
      },
      {
        "instance_id": "narr_01",
        "bias": "Narrative Fallacy",
        "decision_point": 4,
        "mechanism": "Post-hoc construction of a single coherent causal chain (temperature drop, shift change, prior blasting) that feels satisfying and complete, overstating the certainty of causal linkage among factors whose individual contribution is unverified.",
        "affected_reasoning_operation": "Causal reconstruction and incident narrative-writing after the outcome is known",
        "evidence_available_at_time": [
          "Overnight temperature drop",
          "Shift-change timing",
          "Prior week's blasting in an adjacent panel",
          "Engineer's later note that multiple factors are plausible but none confirmed dominant"
        ],
        "required_textual_manifestation": "HSO's report presents the three factors as a tidy, sequential explanation of 'why it happened,' with confident causal language despite unresolved uncertainty.",
        "plausible_nonbias_interpretation": "A reasonable attempt to summarize a complex event for a report audience that expects a clear explanation.",
        "strength": "subtle",
        "do_not_make_explicit": ["narrative fallacy", "coherence", "storytelling", "bias"]
      },
      {
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "decision_point": 4,
        "mechanism": "Primary responsibility for the escalation is assigned to the on-shift miner's individual delay in reporting, rather than to the systemic gap of the missing GCMP-required engineer sign-off after the event-count flag was reached.",
        "affected_reasoning_operation": "Causal attribution of responsibility between individual actor and systemic/process factors",
        "evidence_available_at_time": [
          "Miner's reporting timeline",
          "GCMP requirement for engineer sign-off after reaching the 6 events/hour flag, which was not completed",
          "Shift-change handover timing"
        ],
        "required_textual_manifestation": "HSO's report language centers on the miner 'should have flagged it sooner' as the leading explanation, while treating the missing sign-off step as a secondary or procedural footnote.",
        "plausible_nonbias_interpretation": "Individual vigilance genuinely is one legitimate contributing factor worth noting in any incident report.",
        "strength": "subtle",
        "do_not_make_explicit": ["attribution bias", "fundamental attribution", "systemic vs individual", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' with no paired control scenario supplied."
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
      "Confirm exactly 4 decision points, each with at least two plausible alternatives.",
      "Confirm exactly 6 total bias instances embedded: 1 Availability, 1 Experience, 2 Anchoring (at distinct decision points 2 and 3, distinct evidence sources), 1 Narrative Fallacy, 1 Attribution.",
      "Confirm no bias terminology, labels, or psychological explanations appear in probe language or intended answers.",
      "Confirm each instance has a plausible non-bias interpretation available to the validator.",
      "Confirm the two Anchoring instances use different evidence sources (extensometer baseline vs. crack photograph) and different decision points.",
      "Confirm interview draft target is 1,350 words (acceptable range 1,215-1,485) and can be reached without repeating bias-relevant content across probes.",
      "Confirm consequences (minor spall, no injuries) do not mechanically prove any decision was biased."
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
