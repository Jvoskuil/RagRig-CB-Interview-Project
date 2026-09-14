You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Biased_2",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Quality Assurance Analyst (Statistical Process Control)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Drifting Diameter: SPC Signal Investigation on a Precision Machining Line",
    "scenario_summary_internal": "A QA Analyst monitoring an Xbar-R control chart for a machined shaft's outer diameter notices a warning-zone signal. Over the course of a shift, the analyst must triage the signal, form a root-cause hypothesis among several candidate factors (tool wear, incoming material lot, ambient temperature, operator changeover), decide whether to halt the line or continue with in-process adjustment under time pressure, and finally choose a corrective/reporting action. The narrative embeds one correlation bias instance (treating a temperature-dimension co-movement as causal while not equally testing a competing lot-change explanation) and one conservatism bias instance (underweighting new tool-wear sensor evidence relative to a prior belief that the tool was 'recently serviced and unlikely to be worn').",
    "occupational_realism": {
      "objective": "Determine whether an observed shift in a critical dimensional measurement on a precision-machined part represents a true assignable-cause process shift requiring line stoppage and correction, or common-cause variation, while minimizing scrap and downtime.",
      "setting": "A CNC turning cell producing automotive shafts on a two-shift production schedule; QA Analyst monitors real-time SPC software (Xbar-R charts) from a quality office adjacent to the shop floor, with periodic gemba walks to the machine.",
      "constraints": [
        "Production quota for the shift must still be met if possible",
        "Halting the line triggers a formal deviation report and customer notification above a certain scrap threshold",
        "Tooling changeover takes 45 minutes and idles the cell",
        "Only two dimensional measurements per hour are available from the automated gauge, plus manual spot checks",
        "Material lot documentation lags real-time by roughly one hour",
        "Operator shift changeover occurred mid-investigation, creating a possible confound"
      ],
      "stakeholders": [
        "QA Analyst (protagonist)",
        "Line operator (day shift)",
        "Line operator (night shift, incoming)",
        "Process/manufacturing engineer",
        "Plant quality manager",
        "Incoming materials supplier quality contact"
      ],
      "technical_terms_to_use": [
        "Xbar-R chart",
        "upper control limit (UCL)",
        "warning zone / Western Electric rules",
        "assignable cause vs. common cause variation",
        "tool wear offset",
        "Cpk",
        "gauge R&R",
        "material lot traveler",
        "in-process adjustment",
        "deviation report"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "confirmation bias",
        "correlation bias",
        "conservatism bias",
        "heuristic",
        "anchoring",
        "base rate",
        "prior probability"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Xbar-R chart shows the last three subgroup means trending upward, with the most recent point inside the warning zone (between 2-sigma and 3-sigma) but not beyond the UCL",
          "Range chart remains in control, suggesting variability within subgroups is stable",
          "No maintenance or material change has been logged yet for this shift",
          "Production is 62% through the shift's quota"
        ],
        "new_information_after_decision": [
          "The following subgroup mean crosses the UCL outright, confirming an out-of-control signal",
          "A manual spot check confirms the automated gauge reading is not a measurement artifact"
        ],
        "alternatives": [
          "Treat the warning-zone point as common-cause noise and continue monitoring without intervention",
          "Immediately flag the signal as assignable-cause and begin a root-cause investigation",
          "Increase sampling frequency temporarily before deciding either way"
        ],
        "intended_action": "Analyst increases sampling frequency and flags the trend for investigation rather than halting, judged a reasonable moderate response"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Shop floor temperature log shows a 3°C rise over the same two-hour window as the dimensional drift",
          "A new material lot was received and loaded onto the line approximately 90 minutes before the drift began, per the (lagging) lot traveler",
          "Tool wear sensor has not yet been checked at this point",
          "Process engineer mentions temperature swings have 'caused drift before' on this machine"
        ],
        "new_information_after_decision": [
          "The lot traveler is later confirmed to show the new material lot has a hardness spec at the high end of the acceptable range, a plausible independent contributor",
          "Ambient temperature stabilizes on its own within the hour, and dimensions do not immediately return to baseline, weakening the temperature explanation retroactively"
        ],
        "alternatives": [
          "Attribute the drift primarily to the temperature rise given its clear time-alignment with the dimensional trend",
          "Treat the material lot change as an equally or more plausible cause and pull a sample for hardness/dimensional testing before concluding",
          "Hold both hypotheses open and request data on tool wear before assigning a root cause"
        ],
        "intended_action": "Analyst attributes the drift mainly to the temperature co-movement and deprioritizes the lot-change hypothesis without requesting the hardness sample test"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Analyst's working assumption, stated earlier in the shift, is that the tool was replaced two days ago and 'shouldn't be worn yet'",
          "Tool wear sensor data becomes available and shows cumulative cutting distance is already 78% of the rated tool life, well ahead of the expected pace for a two-day-old insert",
          "Dimensional drift direction (diameter trending toward undersize) is consistent with known tool wear signatures on this machine",
          "Time pressure is rising: only 90 minutes remain in the shift and shift changeover is approaching"
        ],
        "new_information_after_decision": [
          "A subsequent part sample shows the diameter continuing to trend toward the lower spec limit",
          "The incoming night-shift operator reports the tool 'sounded different' during the last hour, a cue available only after changeover"
        ],
        "alternatives": [
          "Revise the root-cause assessment substantially toward tool wear and halt the line for a tool change given the sensor reading",
          "Make a small in-process dimensional offset adjustment and continue running while monitoring closely",
          "Continue running unchanged for the remainder of the shift since the tool was 'recently serviced'"
        ],
        "intended_action": "Analyst makes only a small in-process offset adjustment and keeps running, revising the tool-wear likelihood only slightly despite the sensor reading, largely preserving the original 'tool shouldn't be worn' assessment"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "End-of-shift data shows several parts near or slightly below the lower specification limit",
          "Tool wear sensor now reads 91% of rated life",
          "Cpk calculated for the last two hours has dropped from 1.42 to 1.05",
          "A deviation report is required if any parts are confirmed out of spec"
        ],
        "new_information_after_decision": [
          "A full tool change resolves the drift on the next shift, and dimensions return to the historical baseline mean",
          "Retrospective review shows the material lot hardness was within spec after all, unrelated to the drift"
        ],
        "alternatives": [
          "Recommend an immediate tool change, update the control chart center line temporarily, and file a deviation report covering the affected parts",
          "Recommend only closer monitoring next shift without a tool change or deviation report",
          "Recommend a full process capability study before taking any corrective action"
        ],
        "intended_action": "Analyst recommends the tool change and deviation report, closing out the investigation with an accurate final root cause despite the earlier misweighting of evidence"
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first drew your attention to this control chart that shift?",
        "What was your overall objective when you started looking into the signal?"
      ],
      "timeline_reconstruction": [
        "What happened right after you noticed the warning-zone point?",
        "What information came in over the next couple of hours, and in what order?",
        "When did the tool wear sensor data become available relative to the temperature and lot information?"
      ],
      "decision_point_probes": [
        "At the point where you saw the warning-zone signal, what alternatives did you consider, and why did you choose to increase sampling rather than halt immediately?",
        "When you noticed the temperature rise lined up with the drift, what made that explanation feel more compelling than the material lot change? Did you test the lot hypothesis directly?",
        "Once the tool wear sensor showed 78% of rated life, how did that change your thinking about the tool being 'recently serviced'? What made you choose an offset adjustment over a tool change at that point?",
        "By the end of the shift, what evidence finally shifted your recommendation toward a tool change and deviation report?"
      ],
      "closing_hypotheticals": [
        "If the tool wear data had been available an hour earlier, do you think your decision at the halt/continue point would have changed?",
        "If the material lot hardness test had come back out of spec, how would that have affected your root-cause conclusion?",
        "Looking back, is there anything about how you weighed the temperature information versus the lot information that you'd do differently?",
        "How much did the approaching shift changeover and time pressure influence your decisions?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "corrbias_01",
        "bias": "Correlation bias",
        "decision_point": 2,
        "mechanism": "Analyst observes that ambient temperature rise and dimensional drift co-occur in time and infers a causal relationship, while a second plausible cause (new material lot) with comparable temporal proximity is not investigated with equivalent rigor (no hardness/dimensional sample pulled at the time)",
        "affected_reasoning_operation": "Causal attribution from an observed temporal correlation, evidence-selection favoring the co-varying signal over an equally available alternative",
        "evidence_available_at_time": [
          "Temperature log showing 3°C rise coincident with drift window",
          "Lagging material lot traveler showing a new lot loaded ~90 minutes prior",
          "Process engineer's remark that temperature has 'caused drift before'"
        ],
        "required_textual_manifestation": "The analyst explicitly cites the temperature-dimension timing alignment as the reason for favoring the temperature explanation, and explains not testing the lot hypothesis at that time (e.g., citing convenience, engineer's remark, or the lot data being harder to access) rather than citing a data-driven reason to rule out the lot",
        "plausible_nonbias_interpretation": "The engineer's stated history of temperature-related drift on this machine could be treated as legitimate domain expertise justifying a reasonable working hypothesis, not necessarily a bias",
        "strength": "moderate",
        "do_not_make_explicit": [
          "Do not name 'correlation bias'",
          "Do not have the analyst say 'correlation does not imply causation'",
          "Do not have the analyst explicitly acknowledge ignoring the lot hypothesis for no reason"
        ]
      },
      {
        "instance_id": "consbias_01",
        "bias": "Conservatism Bias",
        "decision_point": 3,
        "mechanism": "Analyst holds an initial belief that the tool is unlikely to be worn because it was replaced two days prior, and upon receiving strong new sensor evidence (78% of rated tool life already consumed) revises the corrective action only marginally (a small offset) rather than updating substantially toward a tool change",
        "affected_reasoning_operation": "Belief updating in response to new quantitative evidence; selection of corrective action magnitude relative to revised risk estimate",
        "evidence_available_at_time": [
          "Prior stated assumption: tool replaced two days ago, 'shouldn't be worn yet'",
          "Tool wear sensor reading: 78% of rated cutting life consumed",
          "Dimensional drift direction consistent with known tool wear signature",
          "Time pressure from approaching shift changeover"
        ],
        "required_textual_manifestation": "The analyst acknowledges the sensor reading as notable but explains choosing a small offset adjustment rather than a tool change by reiterating the earlier assumption that the tool is still relatively new, indicating the prior belief was not substantially revised despite the strength of the new data",
        "plausible_nonbias_interpretation": "Choosing a smaller intervention could be framed as a reasonable attempt to avoid unnecessary downtime under quota pressure, a legitimate operational trade-off rather than a bias",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Do not name 'conservatism bias'",
          "Do not have the analyst say they are 'sticking to their prior belief'",
          "Do not have the analyst state the sensor reading was ignored outright; the update must be present but insufficient"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for biased condition; no control scenario is being generated under this specification"
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
      "Confirm exactly one correlation bias instance and one conservatism bias instance are embedded, each mapped to a distinct decision point (2 and 3 respectively)",
      "Confirm no bias name, definition, or psychological label appears anywhere in the public interview text",
      "Confirm each of the four decision points contains at least two plausible alternatives and both pre- and post-decision information",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes",
      "Confirm word count falls between 1,215 and 1,485 words, targeting 1,350",
      "Confirm the final outcome (successful tool change and deviation report) does not retroactively prove either embedded bias occurred, since a competent non-biased analyst could have reached the same final action via a different reasoning path",
      "Confirm the material lot hardness result (in spec) is revealed only as background closure, not as an explicit confirmation that the earlier temperature attribution was biased",
      "Confirm no additional instances of correlation bias or conservatism bias are introduced at decision points 1 or 4"
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
