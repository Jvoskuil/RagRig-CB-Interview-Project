You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MU_Biased_7",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Underground Mine Manager / Assistant Mine Manager",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Elevated Microseismicity Near Stope 14 East During a Behind-Schedule Production Push",
    "scenario_summary_internal": "An Assistant Mine Manager at a deep underground hard-rock mine must decide how to respond to a sequence of elevated microseismic events near an active stope while production is behind schedule. Ground control monitoring, a proprietary seismic hazard-rating model, shift-crew reports, and the manager's own recent experience with a similar 'false alarm' event all feed into four sequential decisions spanning roughly one shift-and-a-half, ending with a decision to proceed with a scheduled blast despite unresolved warning signs.",
    "occupational_realism": {
      "objective": "Maintain safe ground conditions in Stope 14 East while meeting a tightening weekly ore-production target, without triggering an unnecessary work stoppage.",
      "setting": "A deep underground hard-rock (gold/base-metal analog) mine, 950m level, active stoping area with a real-time microseismic monitoring array and a contracted geotechnical engineering team providing periodic hazard ratings.",
      "constraints": [
        "Production schedule is two days behind target for the month",
        "Geotechnical engineer is only on-site two days per week; remote support is used the rest of the time",
        "Evacuating or re-supporting the stope costs 12-18 hours of lost production",
        "Seismic monitoring array has known blind spots near intersections and old workings",
        "Shift crew morale and trust in management is affected by perceived overreaction to false alarms"
      ],
      "stakeholders": [
        "Assistant Mine Manager (interviewee)",
        "Shift supervisor on Stope 14 East",
        "Contract geotechnical engineer",
        "Production superintendent",
        "Underground crew (drill and blast team)"
      ],
      "technical_terms_to_use": [
        "microseismic event",
        "seismic hazard rating",
        "ground support plan",
        "stope",
        "shotcrete",
        "rockburst potential",
        "re-entry protocol",
        "blast clearance",
        "strain energy",
        "fall of ground (FOG)"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "status quo bias",
        "illusion of validity",
        "overconfidence bias",
        "availability bias",
        "heuristic",
        "cognitive bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Microseismic array logs three moderate-magnitude events near Stope 14 East overnight, above the 30-day baseline",
          "The existing ground support plan for the stope was approved four months ago and has not been revised since",
          "Production is two days behind schedule for the month",
          "No visible ground damage reported by night shift"
        ],
        "new_information_after_decision": [
          "Day shift crew enters Stope 14 East and begins scheduled drilling without additional ground inspection",
          "A minor loose rock is scaled off a rib wall mid-shift, logged as routine"
        ],
        "alternatives": [
          "Continue operations under the existing ground support plan as approved",
          "Pause entry and request an unscheduled ground control inspection before crew entry",
          "Reduce crew numbers in the stope while inspection is pending"
        ],
        "intended_action": "Continue operations under the existing, unrevised ground support plan"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The remote geotechnical model returns a numeric seismic hazard rating of 2.3 on a 5-point scale for the affected zone, labeled 'moderate but manageable'",
          "The manager recalls a similar rating and event cluster six weeks earlier near Stope 9 that resolved without incident",
          "The monitoring array has a documented blind spot near the intersection adjacent to Stope 14 East",
          "The geotechnical engineer is off-site until the following day"
        ],
        "new_information_after_decision": [
          "Blast clearance is granted for the afternoon round based on the hazard rating",
          "A second, larger microseismic event is logged two hours after the rating was issued, outside the model's confidence interval"
        ],
        "alternatives": [
          "Accept the 2.3 rating as sufficient basis to proceed with the planned blast",
          "Request an updated rating incorporating the array's known blind spot before authorizing the blast",
          "Delay the blast until the geotechnical engineer returns on-site"
        ],
        "intended_action": "Accept the numeric hazard rating and authorize the afternoon blast, citing the earlier Stope 9 experience as reassurance"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Following the blast, shotcrete on one rib shows new hairline cracking, reported by the shift supervisor as concerning",
          "A junior geotechnical inspector emails a cautionary note recommending re-support before further blasting",
          "Two other crew members separately describe the cracking as 'typical settling after a blast'",
          "Historical logs show a comparable crack pattern in Stope 9 that did not precede a fall of ground"
        ],
        "new_information_after_decision": [
          "The manager forwards only the crew's 'typical settling' assessments to the production superintendent",
          "The junior inspector's cautionary note is filed but not escalated or discussed on the shift call"
        ],
        "alternatives": [
          "Treat the cracking as inconclusive and commission an independent structural check before continuing",
          "Weigh the junior inspector's recommendation equally against crew observations",
          "Proceed on the basis that crew observations and the Stope 9 precedent are sufficient"
        ],
        "intended_action": "Proceed with the production plan, emphasizing crew reassurance and downplaying the inspector's caution"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Sensor lag on one array node delays confirmation of ground movement magnitude for the next scheduled blast",
          "A small unplanned rock fall (no injuries) occurs near the stope access drift shortly before the decision window",
          "The manager has 20 years of underground experience and has personally overseen similar rock falls without escalation",
          "Production superintendent is pressing for the blast to proceed to hit the monthly target"
        ],
        "new_information_after_decision": [
          "The blast proceeds as scheduled; ground conditions remain stable through the shift",
          "A post-shift review is scheduled but the underlying ground support plan is not revised"
        ],
        "alternatives": [
          "Authorize the blast based on personal judgment and past experience with similar rock falls",
          "Suspend the blast pending confirmed sensor data",
          "Escalate to the geotechnical engineer for a fresh independent assessment"
        ],
        "intended_action": "Authorize the blast, expressing high confidence in personal judgment despite the sensor lag and interpreting the rock fall as further confirmation that conditions are stable"
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what was happening in Stope 14 East that shift?",
        "What was your main objective going into that decision window?"
      ],
      "timeline_reconstruction": [
        "What did you know at the moment you decided to continue under the existing ground support plan?",
        "Walk me through what happened right after the hazard rating came in.",
        "What did the shift supervisor and the junior inspector each tell you, and in what order?",
        "What information arrived after the blast that changed or didn't change your view?"
      ],
      "decision_point_probes": [
        "What alternatives did you consider before continuing operations under the existing plan?",
        "How much weight did the numeric hazard rating carry in your decision, and why?",
        "How did you decide which reports to pass along to the superintendent?",
        "What made you confident enough to authorize the final blast despite the sensor lag?"
      ],
      "goals": [
        "What were you trying to balance between safety and production that day?"
      ],
      "information_sources": [
        "Which sources of information did you trust most in that shift, and why?"
      ],
      "alternatives": [
        "Looking back, what other options were realistically available at each of those points?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision at each step?"
      ],
      "prior_experience": [
        "Did anything from your past experience underground shape how you read these signals?"
      ],
      "time_pressure": [
        "How much did the production schedule affect the pace of your decisions?"
      ],
      "uncertainty": [
        "Where did you feel most uncertain, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the geotechnical engineer had been on-site the whole time, would anything have changed?",
        "If the hazard rating had come back at 3.5 instead of 2.3, what would you have done differently?",
        "Looking back, would you make the same call on continuing under the existing ground support plan?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "sqb_01",
        "bias": "Status quo bias",
        "decision_point": 1,
        "mechanism": "Manager defaults to the existing, unrevised ground support plan despite new seismic evidence, treating the cost/effort of deviation as decisive without directly weighing the new risk information",
        "affected_reasoning_operation": "Option evaluation under a default anchor",
        "evidence_available_at_time": [
          "Three above-baseline microseismic events overnight",
          "Ground support plan unrevised for four months",
          "Production two days behind schedule"
        ],
        "required_textual_manifestation": "Manager states or implies that changing the approved plan felt unnecessary/disruptive and that continuing as planned was the natural choice, without describing a substantive comparison of the new seismic data against the plan's original assumptions",
        "plausible_nonbias_interpretation": "The manager reasonably judged the plan still valid based on the absence of visible damage",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "default effect", "anchoring to existing plan"]
      },
      {
        "instance_id": "iv_01",
        "bias": "Illusion of validity",
        "decision_point": 2,
        "mechanism": "Manager treats the precise numeric hazard rating (2.3) as a reliable, well-calibrated predictor of localized risk despite the model's known blind spot and lack of site-specific validation",
        "affected_reasoning_operation": "Confidence calibration in a quantitative model output",
        "evidence_available_at_time": [
          "Numeric hazard rating of 2.3 labeled 'moderate but manageable'",
          "Known monitoring blind spot near the adjacent intersection",
          "Geotechnical engineer off-site"
        ],
        "required_textual_manifestation": "Manager describes treating the specific numeric rating as strong, decisive evidence of manageable risk, without acknowledging the model's blind-spot limitation as reducing confidence",
        "plausible_nonbias_interpretation": "The rating came from a credentialed remote model and represented the best available quantitative input at the time",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "model limitations", "false precision"]
      },
      {
        "instance_id": "iv_02",
        "bias": "Illusion of validity",
        "decision_point": 3,
        "mechanism": "Manager infers strong predictive confidence from the apparent coherence between the new crack pattern and a past Stope 9 case, treating narrative similarity as proof the pattern is benign rather than as one uncertain data point",
        "affected_reasoning_operation": "Pattern-matching against historical case as validation",
        "evidence_available_at_time": [
          "New hairline cracking in shotcrete",
          "Historical log of comparable Stope 9 crack pattern that resolved without a fall of ground",
          "Junior inspector's cautionary note"
        ],
        "required_textual_manifestation": "Manager expresses that because the crack pattern 'matched' Stope 9's history, this made the current situation predictable/understood, without noting how different one prior case is as a basis for confidence",
        "plausible_nonbias_interpretation": "Drawing on relevant precedent is a legitimate part of experienced judgment in ground control",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "pattern coherence", "overgeneralization from one case"]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3,
        "mechanism": "Manager selectively forwards crew accounts that support the 'normal settling' hypothesis while filing away, without escalation, the junior inspector's dissenting recommendation",
        "affected_reasoning_operation": "Selective evidence transmission/weighting",
        "evidence_available_at_time": [
          "Two crew accounts describing cracking as typical settling",
          "Junior inspector's cautionary email recommending re-support"
        ],
        "required_textual_manifestation": "Manager describes choosing to pass along the reassuring crew reports to the superintendent while not raising or discussing the inspector's note on the shift call",
        "plausible_nonbias_interpretation": "Crew observations from people physically present may reasonably be weighted alongside a remote junior inspector's note",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "selective reporting", "cherry-picking evidence"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Confirmation Bias",
        "decision_point": 4,
        "mechanism": "Manager interprets an ambiguous, minor rock fall as further confirmation that ground conditions are stable, rather than as an update that should increase caution given the pending sensor data gap",
        "affected_reasoning_operation": "Interpretation of ambiguous new evidence relative to a prior belief",
        "evidence_available_at_time": [
          "Small unplanned rock fall near stope access drift",
          "Sensor lag delaying confirmed ground movement magnitude",
          "Prior belief that conditions were manageable"
        ],
        "required_textual_manifestation": "Manager frames the rock fall as consistent with/expected under the 'stable conditions' view rather than treating it as new evidence warranting reassessment, distinct from cb_01's evidence-selection act",
        "plausible_nonbias_interpretation": "Minor rock falls are common and can reasonably be treated as routine background risk",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "belief-consistent interpretation", "biased assimilation"]
      },
      {
        "instance_id": "ob_01",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Manager expresses high personal certainty in the decision to authorize the blast, citing 20 years of experience, while the objective uncertainty (sensor lag, unresolved crack report, superintendent pressure) remains substantial and unaddressed",
        "affected_reasoning_operation": "Self-assessed confidence in a judgment under incomplete information",
        "evidence_available_at_time": [
          "Sensor lag preventing confirmed data",
          "20 years of personal underground experience",
          "Production pressure from superintendent"
        ],
        "required_textual_manifestation": "Manager states strong personal certainty that the call was correct and downplays the significance of the missing sensor confirmation, without qualifying the confidence level against the actual gaps in evidence",
        "plausible_nonbias_interpretation": "Extensive experience is a legitimate basis for professional judgment under uncertainty",
        "strength": "moderate",
        "do_not_make_explicit": ["overconfidence bias", "miscalibrated certainty", "experience-based overconfidence"]
      },
      {
        "instance_id": "ab_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "Manager judges current risk as low primarily because a vivid, easily recalled recent event (Stope 9, six weeks earlier) resolved without incident, rather than referencing base-rate statistics on seismic-event escalation",
        "affected_reasoning_operation": "Risk judgment via recall of a salient prior instance",
        "evidence_available_at_time": [
          "Memory of the Stope 9 event cluster six weeks earlier",
          "Absence of readily recalled base-rate data on escalation frequency"
        ],
        "required_textual_manifestation": "Manager explains reassurance about the current rating mainly by referencing how the Stope 9 case turned out, without citing broader statistics or a wider sample of past events",
        "plausible_nonbias_interpretation": "Recent, directly relevant experience is often a reasonable input to operational judgment",
        "strength": "subtle",
        "do_not_make_explicit": ["availability bias", "recency effect", "salience of recalled event"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, no paired control is being generated in this specification"
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
      "Confirm exactly 7 total bias instances are embedded: 1 status quo, 2 illusion of validity, 2 confirmation bias, 1 overconfidence, 1 availability",
      "Confirm exactly 4 decision points, each with at least two plausible alternatives",
      "Confirm no bias-name vocabulary or explicit psychological labels appear in the interview text",
      "Confirm each instance has a distinct evidence trace and decision moment distinguishing it from any other instance of the same bias",
      "Confirm interview draft falls between 1,215 and 1,485 words, targeting 1,350",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm consequences described (stable shift outcome) do not mechanically prove or disprove bias presence",
      "Confirm no unrequested bias (e.g., anchoring, sunk cost) is intentionally embedded"
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
