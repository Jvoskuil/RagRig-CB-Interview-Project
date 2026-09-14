You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MU_Biased_4",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Mine Ventilation Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Return Airway CO Spike After the 14 Level Blast",
    "scenario_summary_internal": "A mine ventilation engineer must interpret an unexpected carbon monoxide (CO) spike detected at a return-airway gas monitoring station shortly after a scheduled production blast on 14 Level. Under pressure from mine planning to restore ore-haulage on schedule, the engineer must decide whether the reading reflects normal blast-fume clearance or a genuine hazard, whether to hold re-entry, what alarm threshold to apply going forward, and how to close out the incident. The scenario is designed to surface four distinct reasoning failures without ever naming them.",
    "occupational_realism": {
      "objective": "Determine the cause of an anomalous CO reading at a return-airway gas station following a production blast, decide on re-entry and ventilation-on-demand (VOD) settings, and close out the shift incident report without compromising worker safety or the haulage schedule.",
      "setting": "A underground decline gold mine operating a ventilation-on-demand system across multiple levels, approximately 900 m below surface, with auxiliary fans supporting active stopes and a primary fan system exhausting through the return airway network.",
      "constraints": [
        "Blast clearance protocol requires confirmed safe atmosphere before re-entry",
        "Mine planning is pushing to resume load-haul-dump (LHD) ore movement within the shift to meet a weekly tonnage target",
        "Only one handheld multi-gas detector is available on-site for cross-check during the relevant window",
        "The gas monitoring station has a documented history of dust-related interference near a recently shotcreted junction",
        "Diesel LHD fleet was idling near the loading point during the relevant period, a known but modest CO contributor",
        "Commissioning-era alarm thresholds were set five years ago under different depth and fleet conditions"
      ],
      "stakeholders": [
        "Mine Ventilation Engineer (interviewee)",
        "Shift Boss",
        "Underground Gas Monitoring Technician",
        "Mine Planning Superintendent",
        "LHD Operators",
        "Mine Safety Officer"
      ],
      "technical_terms_to_use": [
        "return airway", "gas monitoring station", "ventilation-on-demand (VOD)", "blast clearance time",
        "re-entry protocol", "primary fan", "auxiliary fan", "parts per million (ppm)",
        "diesel particulate matter (DPM)", "load-haul-dump (LHD)", "regulator door", "baseline survey",
        "commissioning report", "handheld multi-gas detector", "shotcrete curing", "telemetry log"
      ],
      "technical_terms_to_avoid": [
        "specific national regulatory agency names",
        "specific real mine or company names",
        "brand names of sensor manufacturers"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Gas station GS-14R shows CO at 280 ppm, roughly 30 minutes after scheduled blast clearance time, against a historical post-blast baseline under 50 ppm",
          "The engineer has flagged GS-14R twice in the past three months for suspected dust-induced drift near a newly shotcreted junction",
          "A technician's handheld multi-gas detector taken at the return airway independently reads 190 ppm at roughly the same time",
          "No maintenance ticket has yet confirmed a sensor fault on GS-14R this shift"
        ],
        "new_information_after_decision": [
          "Re-entry proceeds on schedule based on the sensor-fault call",
          "The handheld reading is logged but not escalated for independent recalibration",
          "CO levels are later found to have genuinely elevated over baseline, though not to hazardous concentration"
        ],
        "alternatives": [
          "Treat the sensor reading as likely erroneous based on prior drift history and proceed with re-entry",
          "Cross-validate with the handheld reading and delay re-entry pending a second confirmatory reading",
          "Request immediate recalibration check before making any re-entry call"
        ],
        "intended_action": "Engineer concludes the GS-14R reading is a probable false spike, drawing primarily on past instances that fit this belief while discounting the corroborating handheld reading."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Re-entry has been approved but the shift boss asks whether personnel should hold at the refuge chamber a few extra minutes as a precaution",
          "Fume-clearance delays of this type are the far more common explanation for transient post-blast CO elevation at this mine",
          "The engineer recently discussed, in a safety meeting, a widely reported underground mine fire fatality from another operation with vivid detail about smoke and delayed detection",
          "No smoke, heat, or secondary gas (e.g., elevated CO2 trend) indicators are present at 14 Level"
        ],
        "new_information_after_decision": [
          "Personnel are held for an additional 15 minutes and a full fire-response protocol is partially activated",
          "No fire indicators materialize; the delay is later attributed to normal fume clearance lag from a slightly longer-than-usual round"
        ],
        "alternatives": [
          "Hold personnel and partially activate fire-response protocol given the memorable prior incident",
          "Proceed with standard fume-clearance wait time consistent with the more common explanation",
          "Request a bleeder raise check for smoke/heat before deciding"
        ],
        "intended_action": "Engineer weighs the probability of a fire scenario heavily based on the vividness and recency of a remembered case rather than the base rate of ordinary fume-clearance delays at this mine."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The Mine Planning Superintendent asks whether the CO auto-cutoff setpoint for GS-14R should be revised before resuming full LHD movement",
          "The original commissioning report, written five years ago at a shallower working depth and with a smaller diesel fleet, recommended a 100 ppm auto-cutoff threshold",
          "Recent baseline surveys under current depth and fleet conditions show ambient CO trending noticeably higher than at commissioning",
          "No formal re-baselining of the auto-cutoff has occurred since fleet expansion two years ago"
        ],
        "new_information_after_decision": [
          "The 100 ppm threshold is retained with only a minor adjustment",
          "Over subsequent shifts, the auto-cutoff trips more frequently during normal diesel-heavy periods, prompting operational friction"
        ],
        "alternatives": [
          "Retain the original commissioning threshold with minor adjustment",
          "Commission a fresh baseline survey and recalculate the threshold from current conditions",
          "Set an interim conservative threshold pending full re-survey"
        ],
        "intended_action": "Engineer's revised threshold stays close to the original commissioning figure, treating it as the natural starting point despite new baseline data indicating conditions have materially changed."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The Safety Officer requests a short closing narrative for the incident report before production resumes fully",
          "Three loosely related facts are on record: the sensor's known drift history, the idling LHD fleet near the loading point, and the longer-than-usual blast round",
          "No single confirmed causal test (e.g., isolating the sensor, then isolating the LHD fleet) was performed to separate these factors",
          "Mine planning is waiting on report closure to greenlight full-shift resumption"
        ],
        "new_information_after_decision": [
          "The incident is closed with a single coherent explanation combining sensor drift, idling diesel fleet, and round length",
          "No follow-up investigation is scheduled to test which factor, if any, was primarily responsible"
        ],
        "alternatives": [
          "Close the report with a single tidy combined explanation covering all observed facts",
          "Close the report listing multiple unresolved candidate explanations without asserting a single causal chain",
          "Defer closure pending a targeted follow-up test isolating each candidate cause"
        ],
        "intended_action": "Engineer assembles the loosely connected facts into one smooth, satisfying causal story for the report, even though no single fact was tested against the others."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were doing when the GS-14R reading first came to your attention.",
        "What was your role and responsibility at that point in the shift?"
      ],
      "timeline_reconstruction": [
        "What happened right after you saw the 280 ppm reading?",
        "What did the shift boss and technician do while you were assessing the situation?",
        "How did the situation evolve from the initial reading to the final incident closure?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you at that moment?",
        "What sources did you check, and which ones did you not check?",
        "What alternatives did you consider before deciding?",
        "What ultimately tipped your decision one way rather than another?",
        "Had you seen anything like this before, and did that affect how you read the situation?"
      ],
      "closing_hypotheticals": [
        "If the handheld reading had shown a much higher number, would your call have changed?",
        "If you'd had time for a full re-baseline survey before setting the threshold, would you have set it differently?",
        "Looking back, is there another explanation for the spike that fits the same facts equally well?",
        "How much of your decision was shaped by the time pressure from mine planning that day?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 1,
        "mechanism": "Engineer selectively weights the prior drift history of GS-14R as confirming evidence for a sensor-fault hypothesis while discounting the corroborating handheld reading that would disconfirm it",
        "affected_reasoning_operation": "evidence weighting and evidence selection during hazard interpretation",
        "evidence_available_at_time": [
          "Two prior drift flags on GS-14R in the past three months",
          "Independent handheld reading of 190 ppm at roughly the same time",
          "No confirmed maintenance fault ticket yet"
        ],
        "required_textual_manifestation": "Interviewee explains reaching the sensor-fault conclusion primarily by citing the prior flags, while explicitly or implicitly setting aside or minimizing the handheld corroboration without a stated technical reason for doing so",
        "plausible_nonbias_interpretation": "A reasonable engineer familiar with a sensor's documented drift history might legitimately give it more weight than an ambiguous handheld cross-check",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "cherry-picking", "selective evidence"]
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "Engineer estimates the likelihood of a fire scenario based on the vividness and memorability of a recently discussed fatal incident elsewhere rather than the actual base rate of fume-clearance delays at this mine",
        "affected_reasoning_operation": "probability estimation / risk judgment under uncertainty",
        "evidence_available_at_time": [
          "Absence of smoke, heat, or secondary gas trend indicators at 14 Level",
          "Recent vivid discussion of an unrelated fatal mine fire",
          "Historical frequency of fume-clearance delays being the common explanation at this site"
        ],
        "required_textual_manifestation": "Interviewee references the memorable prior fire case as a reason for escalating caution, in a way that outweighs the locally available base-rate evidence pointing toward a mundane explanation",
        "plausible_nonbias_interpretation": "Erring toward caution near any fire-adjacent possibility is a defensible safety-first heuristic even without statistical grounding",
        "strength": "subtle",
        "do_not_make_explicit": ["availability bias", "vividness", "recency effect"]
      },
      {
        "instance_id": "an_01",
        "bias": "Anchoring Bias",
        "decision_point": 3,
        "mechanism": "Engineer's revised auto-cutoff threshold remains close to the original five-year-old commissioning figure despite new baseline data indicating that current depth and fleet conditions warrant a materially different starting point",
        "affected_reasoning_operation": "numerical estimation / threshold-setting adjustment",
        "evidence_available_at_time": [
          "Original commissioning report threshold of 100 ppm from five years prior",
          "Recent baseline surveys showing higher ambient CO under current depth and fleet",
          "No re-baselining performed since fleet expansion two years ago"
        ],
        "required_textual_manifestation": "Interviewee describes adjusting the threshold only slightly from the original figure, treating the commissioning number as the natural reference point rather than recalculating from current baseline data",
        "plausible_nonbias_interpretation": "Preserving continuity with an established, previously-approved threshold can be a reasonable conservative default absent a formal re-survey mandate",
        "strength": "moderate",
        "do_not_make_explicit": ["anchoring bias", "insufficient adjustment", "reference point"]
      },
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "decision_point": 4,
        "mechanism": "Engineer constructs one smooth, internally consistent causal story linking sensor drift, idling diesel fleet, and round length to close the incident report, despite no single test isolating which factor actually caused the spike",
        "affected_reasoning_operation": "causal attribution / retrospective sense-making",
        "evidence_available_at_time": [
          "Sensor drift history",
          "Idling LHD fleet near the loading point",
          "Longer-than-usual blast round",
          "No isolating test performed among these candidate causes"
        ],
        "required_textual_manifestation": "Interviewee narrates the incident closure as a single coherent chain of cause and effect connecting all three facts, expressing confidence in this combined story despite the lack of a discriminating test",
        "plausible_nonbias_interpretation": "Synthesizing multiple contributing factors into one closing account is normal incident-report practice when time is limited and no single cause is provably dominant",
        "strength": "subtle",
        "do_not_make_explicit": ["narrative fallacy", "coherence over truth", "storytelling"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario was supplied for this generation."
    },
    "counterfactual_specification": {
      "causal_variable": "Availability of a second corroborating handheld gas reading before the Decision Point 1 sensor-fault call",
      "original_state": "Only one handheld cross-check reading (190 ppm) was available and was discounted relative to sensor drift history",
      "counterfactual_state": "A second independent handheld reading, taken from a different location in the return airway, is also available and corroborates elevated CO before the sensor-fault call is made",
      "variables_to_hold_constant": [
        "Blast timing and clearance schedule",
        "Mine planning's production pressure",
        "Prior drift history of GS-14R",
        "Subsequent decision points 2 through 4 and their available facts"
      ],
      "expected_causal_difference": "With stronger corroborating evidence available, a less-biased reasoner would be less likely to dismiss the readings as sensor fault at Decision Point 1, which could alter downstream caution levels at Decision Point 2",
      "causal_test_question": "Does adding a second corroborating handheld reading before the sensor-fault call reduce the confirmation-driven dismissal observed in the biased condition?"
    },
    "generation_checks": [
      "Exactly four decision points are present, one per named bias, with no bias assigned to more than one decision point",
      "Each of the four manifest biases has exactly one planned instance, matching occurrences=1 for each",
      "No bias labels, definitions, or explicit psychological terminology will appear in the public interview text",
      "Each instance has a distinct evidence trace and reasoning operation, preventing conflation across instances",
      "Consequences described (minor threshold friction, no fire, tidy report closure) do not mechanically prove or disprove bias, preserving interpretive ambiguity for the validator",
      "Word count target of 1,350 (range 1,215-1,485) is achievable given four decision points with probes, without requiring repetitive exposition",
      "Technical vocabulary list is sufficient to sustain occupational realism without needing invented jargon"
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
