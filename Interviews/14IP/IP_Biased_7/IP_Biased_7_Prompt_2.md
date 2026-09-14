You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Biased_7",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Process/Manufacturing Engineer (Process Selection)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Anodizing Line Micro-Pitting: Root-Cause Diagnosis and Process Certification Decision",
    "scenario_summary_internal": "A process engineer at a Tier-1 automotive parts manufacturer investigates intermittent micro-pitting defects on aluminum brackets produced on a newly commissioned anodizing line, under a 10-day deadline to certify the corrected process before a customer PPAP audit. The engineer must diagnose root cause, select a corrective dosing technology, validate trial batches, and make a final certification recommendation, all under time and cost pressure with incomplete, ambiguous, and sequentially-arriving evidence.",
    "occupational_realism": {
      "objective": "Diagnose the cause of intermittent micro-pitting on anodized aluminum brackets and certify a corrected surface-treatment process in time for a customer PPAP submission.",
      "setting": "Surface-treatment department of a Tier-1 automotive components plant; newly commissioned anodizing line with rectifier, temperature-controlled bath, and chemical dosing system; 10 working days before customer audit.",
      "constraints": [
        "10-day deadline before customer PPAP audit",
        "Limited capacity for full trial batches due to cost of scrap aluminum stock",
        "Cross-shift handoffs (day/night) with inconsistent logging practices",
        "Corporate pressure not to delay a customer product launch",
        "Only one qualified quality lab technician available for SPC data review"
      ],
      "stakeholders": [
        "Plant manager",
        "Quality manager",
        "Night-shift line operator",
        "Day-shift line operator",
        "Chemical dosing vendor representative",
        "Customer supplier quality engineer (SQE)",
        "Process engineer at sister plant"
      ],
      "technical_terms_to_use": [
        "anodizing",
        "rectifier",
        "bath chemistry",
        "dwell time",
        "PPAP",
        "SPC",
        "Cpk",
        "dosing system",
        "chiller",
        "coil certification",
        "micro-pitting",
        "DOE",
        "sister plant",
        "trial lot"
      ],
      "technical_terms_to_avoid": [
        "primacy effect",
        "anchoring",
        "fundamental attribution",
        "gambler's fallacy",
        "illusion of control",
        "ambiguity aversion",
        "bandwagon effect",
        "recency effect",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Night-shift operator's handoff note attributing pitting to an overnight bath temperature spike, received first thing on day one",
          "Unreviewed rectifier calibration logs from the past two weeks",
          "Unreviewed incoming aluminum coil chemistry certificates",
          "A defect-rate comparison report showing day-shift batches had a higher pitting rate than night-shift batches"
        ],
        "new_information_after_decision": [
          "Chiller repaired and bath temperature stabilized within one day",
          "Micro-pitting recurs at a reduced but nonzero rate, suggesting temperature was not the sole cause"
        ],
        "alternatives": [
          "Prioritize chiller repair and temperature control as the primary corrective action",
          "Investigate rectifier calibration drift first",
          "Review incoming coil chemistry certificates first",
          "Commission a multi-factor DOE across temperature, rectifier output, and material chemistry before acting"
        ],
        "intended_action": "Engineer focuses corrective resources on the bath temperature/chiller system and cites day-shift operator competency as a contributing factor, deferring rectifier and material reviews."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Residual low-rate pitting persists after temperature correction",
          "Vendor A offers an automated dosing control retrofit already installed at three sister plants, with mixed results reported at one of them",
          "Vendor B offers a newer inline sensor-based dosing system with a stronger published spec sheet but only one reference installation and incomplete documentation",
          "Informal calls with sister-plant engineers describing general satisfaction with Vendor A"
        ],
        "new_information_after_decision": [
          "Vendor A retrofit installed within three days",
          "Initial trial batches show a marked drop in defect rate"
        ],
        "alternatives": [
          "Select Vendor A's established multi-plant dosing retrofit",
          "Select Vendor B's newer sensor-based dosing system",
          "Run a small parallel trial of both systems before committing",
          "Delay a technology decision and continue manual dosing adjustments"
        ],
        "intended_action": "Engineer selects Vendor A primarily because it is already used at multiple sister plants, and explicitly rules out Vendor B due to its incomplete documentation despite its stronger spec sheet."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "First two post-retrofit batches still show minor pitting",
          "Next five consecutive batches come back clean after the engineer makes manual rectifier voltage adjustments between runs",
          "Bath chemistry was also replenished on a routine schedule during this same window",
          "Full SPC sample size is still below the minimum recommended for capability confirmation"
        ],
        "new_information_after_decision": [
          "A later independent quality audit finds the process capability index (Cpk) is only marginally within specification, not fully stable"
        ],
        "alternatives": [
          "Declare the process stable based on the five-batch clean streak and proceed toward certification",
          "Run the full recommended SPC sample size before drawing conclusions",
          "Attribute the improvement to the two initial bad batches being an isolated fluke unlikely to recur",
          "Commission a short confirmatory DOE isolating voltage adjustment from chemistry replenishment"
        ],
        "intended_action": "Engineer proceeds toward certification testing without the full SPC sample, crediting personal mid-run voltage adjustments for the clean streak and treating the earlier bad batches as now behind a run of 'owed' good outcomes."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Full trial-lot dataset spans two weeks and shows real variability across early lots",
          "The final validation lot, run the day before the deadline, comes back completely clean",
          "Customer SQE requires a sign-off memo within 24 hours",
          "Marginal Cpk finding from the independent audit is available but was filed separately from the sign-off packet"
        ],
        "new_information_after_decision": [
          "Process is certified and PPAP is submitted on schedule; longer-term field performance remains unknown at the time of the interview"
        ],
        "alternatives": [
          "Certify the process based heavily on the clean final lot",
          "Base the certification decision on the full two-week trial dataset including earlier variability",
          "Request a short deadline extension for a complete statistical review",
          "Issue a conditional certification pending additional monitoring"
        ],
        "intended_action": "Engineer signs off on certification, emphasizing the final clean lot in the memo and giving comparatively little weight to the earlier variability documented across the full trial period."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what happened when you were first assigned to investigate the micro-pitting issue.",
        "What was your overall objective going into this investigation?"
      ],
      "timeline_reconstruction": [
        "What information did you have on day one, and what came in later?",
        "How did the investigation unfold from the initial report to the final certification decision?",
        "What changed in your understanding as new data arrived?"
      ],
      "decision_point_probes": [
        "At that point, what alternatives did you consider, and why did you choose the one you did?",
        "What evidence or cues were you weighing most heavily at that moment?",
        "Who or what influenced your thinking at this stage?",
        "How confident were you at the time, and what would have changed your mind?",
        "Was there time pressure affecting this particular decision?"
      ],
      "closing_hypotheticals": [
        "If you had reviewed the rectifier calibration logs before the operator's report, do you think your investigation would have gone differently?",
        "If the final validation lot had shown pitting instead of a clean result, how would that have changed your certification decision?",
        "Looking back, is there anything about how you weighed the evidence that you'd do differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "decision_point": 1,
        "mechanism": "The engineer gives disproportionate investigative weight to the first explanation received (night-shift operator's temperature-spike report) and organizes subsequent inquiry around confirming it, deferring review of rectifier and material data that arrived later.",
        "affected_reasoning_operation": "Hypothesis prioritization at the start of a diagnostic investigation",
        "evidence_available_at_time": [
          "Night-shift operator's handoff note (received first)",
          "Unreviewed rectifier calibration logs",
          "Unreviewed coil chemistry certificates"
        ],
        "required_textual_manifestation": "Engineer explicitly states that the temperature explanation 'made sense right away' or was the natural starting point because it was the first thing reported, and describes deferring the rectifier/material checks as a result.",
        "plausible_nonbias_interpretation": "Temperature control is a common and easily testable first suspect in anodizing defects, so starting there could reflect a reasonable triage heuristic rather than order-driven weighting.",
        "strength": "subtle",
        "do_not_make_explicit": ["primacy", "anchoring", "first impression bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Fundamental Attribution Bias",
        "decision_point": 1,
        "mechanism": "The engineer explains a defect-rate difference between shifts by attributing it to the day-shift operator's personal carelessness or insufficient skill, rather than considering situational factors like equipment condition, bath chemistry drift, or handoff documentation quality.",
        "affected_reasoning_operation": "Causal attribution of a performance difference between personnel",
        "evidence_available_at_time": [
          "Defect-rate comparison report showing day-shift batches had higher pitting rates than night-shift batches"
        ],
        "required_textual_manifestation": "Engineer characterizes the day-shift operator as careless, inattentive, or less capable when explaining the defect-rate gap, without weighing equipment or process-condition explanations for the same data.",
        "plausible_nonbias_interpretation": "If the day-shift operator genuinely had less experience or documented training gaps, personal-factor attribution could be a reasonable read of the same evidence.",
        "strength": "subtle",
        "do_not_make_explicit": ["fundamental attribution error", "dispositional vs situational"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Ambiguity effect",
        "decision_point": 2,
        "mechanism": "The engineer avoids Vendor B's sensor-based dosing system specifically because its documentation is incomplete or unclear, even though its published specifications are stronger, preferring the more thoroughly documented but less proven-in-context option.",
        "affected_reasoning_operation": "Option elimination under incomplete information",
        "evidence_available_at_time": [
          "Vendor B's published spec sheet (favorable) and incomplete installation documentation (unfavorable clarity)"
        ],
        "required_textual_manifestation": "Engineer states that Vendor B was ruled out mainly because 'we didn't have enough clarity on how it performs' or similar, despite acknowledging its stronger specs.",
        "plausible_nonbias_interpretation": "Avoiding a poorly documented system before a customer audit could reflect legitimate risk management rather than aversion to ambiguity itself.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity aversion", "uncertainty avoidance"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "decision_point": 2,
        "mechanism": "The engineer selects Vendor A largely because it is already used at three sister plants and informally endorsed by peer engineers, despite one of those plants reporting mixed results, rather than basing the choice on independent technical evaluation.",
        "affected_reasoning_operation": "Vendor selection weighting based on peer adoption prevalence",
        "evidence_available_at_time": [
          "Informal calls with sister-plant engineers describing general satisfaction with Vendor A",
          "Knowledge that one sister plant had mixed results with Vendor A"
        ],
        "required_textual_manifestation": "Engineer justifies the choice with language like 'everyone else is running it' or 'three plants already use it,' downplaying the mixed-result data point.",
        "plausible_nonbias_interpretation": "Wide internal adoption can be a legitimate proxy for supportability and spare-parts availability, independent of peer-conformity pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon", "social proof", "conformity"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Gambler's Fallacy",
        "decision_point": 3,
        "mechanism": "The engineer or team reasons that after two defective batches, the process was statistically 'due' for a run of good batches, treating sequential independent batch outcomes as if they were anti-correlated.",
        "affected_reasoning_operation": "Probabilistic interpretation of a sequence of batch outcomes",
        "evidence_available_at_time": [
          "Batch outcome log showing two defective batches followed by five clean batches"
        ],
        "required_textual_manifestation": "Engineer explicitly frames the clean streak as the process having been 'due' for good results or the bad batches as making a further bad batch unlikely, rather than treating each batch as an independent trial.",
        "plausible_nonbias_interpretation": "A genuine underlying cause (e.g., dosing retrofit taking effect) could independently explain an improving trend, without any probabilistic reasoning error.",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "due for a win", "law of averages"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Illusion of control",
        "decision_point": 3,
        "mechanism": "The engineer attributes the clean batch streak primarily to their own manual mid-run rectifier voltage adjustments, overestimating personal control over an outcome also plausibly explained by a routine bath chemistry replenishment occurring in the same window.",
        "affected_reasoning_operation": "Causal credit assignment for a process outcome involving both personal action and an uncontrolled concurrent factor",
        "evidence_available_at_time": [
          "Engineer's own process-log annotations documenting manual voltage adjustments",
          "Record of a routine bath chemistry replenishment occurring in the same period"
        ],
        "required_textual_manifestation": "Engineer states confidence that their manual tuning is what stabilized the process, without acknowledging the concurrent chemistry replenishment as an alternative explanation.",
        "plausible_nonbias_interpretation": "Manual voltage tuning is a legitimate corrective action in anodizing and could genuinely have contributed to the improvement.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control", "overestimating personal influence"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Recency effect",
        "decision_point": 4,
        "mechanism": "In the final certification sign-off, the engineer gives disproportionate weight to the most recently produced validation lot (completely clean) over the fuller two-week trial dataset that documented earlier variability.",
        "affected_reasoning_operation": "Evidence weighting in a final go/no-go certification judgment",
        "evidence_available_at_time": [
          "Full two-week trial-lot dataset showing earlier variability",
          "Final validation lot results (clean), produced immediately before the deadline"
        ],
        "required_textual_manifestation": "Engineer's sign-off reasoning emphasizes the final clean lot as the deciding factor, with the earlier variability mentioned only in passing or filed separately.",
        "plausible_nonbias_interpretation": "The most recent lot could legitimately be the most representative of the corrected process state, making recency-weighting a defensible engineering judgment rather than an error.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "recency bias", "last impression"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', no paired control is generated under this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Order in which diagnostic evidence sources were reviewed at the start of the investigation",
      "original_state": "Night-shift operator's temperature-spike report is received and reviewed first, before rectifier calibration logs or coil chemistry certificates.",
      "counterfactual_state": "Rectifier calibration logs are reviewed first, before the operator's temperature-spike report or coil chemistry certificates.",
      "variables_to_hold_constant": [
        "Underlying true root cause(s) of the micro-pitting defect",
        "Deadline pressure and PPAP audit timing",
        "Vendor options and their documentation quality",
        "Batch outcome sequence during trial runs",
        "Personnel and stakeholder roles"
      ],
      "expected_causal_difference": "If rectifier data is reviewed first, the engineer's initial hypothesis prioritization at Decision Point 1 should anchor on rectifier calibration rather than bath temperature, testing whether order of evidence receipt (rather than the content of the operator's report) drives the initial hypothesis weighting.",
      "causal_test_question": "Does changing which evidence source is encountered first at the start of the investigation change which root-cause hypothesis the engineer prioritizes, holding all other facts constant?"
    },
    "generation_checks": [
      "Confirm exactly four decision points are present, each with at least two plausible alternatives.",
      "Confirm exactly one instance each of Primacy Effect, Fundamental Attribution Bias, Gambler's Fallacy, Illusion of control, Ambiguity effect, Bandwagon effect, and Recency effect is embedded, with no repetitions or additional unrequested bias instances.",
      "Confirm no bias name, definition, or psychological label appears anywhere in the public interview text.",
      "Confirm each embedded instance is textually distinguishable from a neutral, justified, or expertise-based explanation.",
      "Confirm instances sharing a decision point (cb_01/cb_02, cb_03/cb_04, cb_05/cb_06) each rely on distinct evidence sources or reasoning operations.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm final word count falls between 1,215 and 1,485 words without repetitive exposition.",
      "Confirm consequences described do not mechanically prove or disprove whether any decision was biased."
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
