You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "NP_Biased_3",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Maintenance Planner / Outage Coordinator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Feedwater Isolation Valve Rework During a Refueling Outage",
    "scenario_summary_internal": "A maintenance planner/outage coordinator at a PWR station is scoping and executing a 21-day refueling outage. A recurring packing-leak issue on a feedwater isolation valve (FW-IV-204) must be scheduled alongside dozens of competing work orders under a fixed critical-path window. During execution, an unexpected vibration reading on a related pump bearing surfaces, and the coordinator must decide how to interpret it before clearing the system for startup. The narrative surfaces one vivid recalled incident from another unit that skews risk weighting (availability bias), a scoping/resourcing shortcut driven by cognitive and time load (bounded rationality), and a selective evidence-review pattern once a working theory forms about the vibration anomaly (confirmation bias). A fourth decision point (final return-to-service call) is written as a clean, non-biased judgment call to anchor the narrative and give a neutral contrast point.",
    "occupational_realism": {
      "objective": "Safely complete all critical-path maintenance and inspection work within the 21-day refueling outage window and return the unit to full power without exceeding the approved critical path or introducing latent equipment issues.",
      "setting": "Pressurized water reactor station; outage control center during a scheduled refueling outage; feedwater system and auxiliary building work areas.",
      "constraints": [
        "Fixed 21-day critical-path outage schedule with penalty exposure for schedule overrun",
        "Limited contractor craft-hours during the outage window",
        "Competing work orders across multiple systems requiring the same specialty crews (valve/rigging techs)",
        "Radiological and access control limiting work windows in certain areas",
        "Regulatory requirement to resolve open condition reports before mode change",
        "Coordinator responsible for prioritizing ~140 concurrent work orders with partial information on each"
      ],
      "stakeholders": [
        "Maintenance Planner/Outage Coordinator (interviewee)",
        "Outage Manager",
        "System Engineer for feedwater system",
        "Valve maintenance craft supervisor",
        "Operations shift manager",
        "Quality/condition report reviewer"
      ],
      "technical_terms_to_use": [
        "feedwater isolation valve (FW-IV-204)",
        "packing leak",
        "critical path",
        "work order backlog",
        "condition report (CR)",
        "bearing vibration trend",
        "return-to-service walkdown",
        "craft-hours allocation",
        "system engineer concurrence",
        "mode change hold point"
      ],
      "technical_terms_to_avoid": [
        "availability heuristic",
        "confirmation bias",
        "bounded rationality",
        "satisficing",
        "anchoring",
        "cognitive bias",
        "heuristic shortcut"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "FW-IV-204 has a known minor packing weep documented in two prior outage CRs, both closed as acceptable-as-found",
          "No trending data indicates worsening leak rate",
          "The coordinator recently heard a detailed account of a similar valve failure at a sister unit that caused a multi-day schedule slip"
        ],
        "new_information_after_decision": [
          "Craft supervisor notes the valve is functioning within spec but the packing job will consume more hours than budgeted",
          "Other queued work orders with equal or higher CR priority are pushed later in the schedule"
        ],
        "alternatives": [
          "Rank FW-IV-204 rework as top priority based on the vividly recalled sister-unit event",
          "Rank work orders strictly by documented CR severity and trend data, treating FW-IV-204 as routine",
          "Request updated trend data before assigning priority"
        ],
        "intended_action": "Coordinator elevates FW-IV-204 to top-tier priority, citing the memorable sister-unit failure more than the actual local trend data."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Craft-hour budget is nearly exhausted for the current outage day",
          "Multiple valid crew-assignment configurations exist, several requiring further comparison of overtime cost, fatigue rules, and sequencing",
          "Outage Manager wants a resourcing decision within the hour to hold the critical path"
        ],
        "new_information_after_decision": [
          "The chosen crew configuration works but creates a minor sequencing conflict with an unrelated pump job later in the shift",
          "A more thorough comparison, done later, shows a marginally better configuration existed"
        ],
        "alternatives": [
          "Run a full comparison of all feasible crew configurations against cost, fatigue, and sequencing before deciding",
          "Select the first crew configuration that meets minimum schedule and safety requirements and move on",
          "Defer the assignment decision to the next shift for a fuller review"
        ],
        "intended_action": "Coordinator picks the first workable crew configuration that clears the immediate constraints, given limited time and information-processing capacity, rather than continuing to search for the optimal configuration."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vibration monitoring shows a mild anomaly on the feedwater pump bearing adjacent to FW-IV-204 during post-maintenance testing",
          "Coordinator's working theory is that the anomaly is residual misalignment from the valve rework just completed",
          "System engineer has not yet reviewed the full vibration trend history for that bearing"
        ],
        "new_information_after_decision": [
          "A second vibration reading is taken 12 hours later and is ambiguous ",
          "The system engineer later notes an unrelated lubrication log entry that was available at the time but not requested"
        ],
        "alternatives": [
          "Pull the full bearing vibration trend history and lubrication records before attributing the anomaly to the valve rework",
          "Accept the misalignment theory, request only the specific data points that would confirm it, and proceed",
          "Treat the anomaly as unexplained and hold the item open pending independent engineering review"
        ],
        "intended_action": "Coordinator requests and reviews the vibration data segment that fits the misalignment theory, does not request the lubrication log or wider trend history, and documents the anomaly as resolved based on the theory-consistent data."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "All outstanding CRs on FW-IV-204 and the adjacent pump are formally closed",
          "System engineer has provided written concurrence for return to service",
          "Operations shift manager requests final walkdown confirmation before mode change"
        ],
        "new_information_after_decision": [
          "The unit returns to service and completes the walkdown without further anomalies",
          "A minor unrelated instrumentation drift is noted for tracking in the next outage, unrelated to the FW-IV-204 work"
        ],
        "alternatives": [
          "Concur with return to service based on completed walkdown and engineering sign-off",
          "Request an additional 24-hour monitoring period before mode change",
          "Escalate for independent review given the earlier vibration anomaly"
        ],
        "intended_action": "Coordinator conducts the walkdown, weighs the documented sign-offs against the earlier anomaly discussion, and concurs with return to service as a reasoned judgment call, without additional bias-driven distortion."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role during this outage and what your main objective was?",
        "What made this particular outage cycle stand out from a routine one?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from initial work scoping to final return to service.",
        "At what point did FW-IV-204 first come onto your radar for this outage?",
        "What happened after the vibration anomaly was first noticed?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you when you decided to prioritize FW-IV-204?",
        "Were there other work orders competing for the same priority ranking? How did you weigh them?",
        "How did you settle on the crew configuration you used for the valve rework?",
        "Did you consider comparing other resourcing options, and what stopped or allowed further comparison?",
        "When the vibration anomaly appeared, what was your first working theory about the cause?",
        "What data did you pull to check that theory, and what data did you not pull?",
        "What was your basis for signing off that the unit was ready to return to service?"
      ],
      "prior_experience": [
        "Have you dealt with a similar valve or vibration issue before? How did that shape your thinking here?",
        "Was there a past event, at this plant or elsewhere, that came to mind during this outage?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure were you under when making the crew assignment decision?",
        "How confident were you in the misalignment theory at the time, on a scale of your own judgment?",
        "Was there anything you were uncertain about but decided not to pursue further?"
      ],
      "closing_hypotheticals": [
        "If you had had more time before the crew assignment decision, would you have done anything differently?",
        "If the lubrication log had been in front of you when the vibration anomaly appeared, do you think it would have changed your review?",
        "Looking back, is there a point where a different prioritization of FW-IV-204 might have changed the outcome?",
        "What would you tell a newer planner to watch for in a similar situation?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "avail_01",
        "bias": "Availability Bias",
        "decision_point": 1,
        "mechanism": "Ease of recall of a vivid, recently-heard sister-unit valve failure inflates perceived probability/severity of a similar local issue, overriding the less memorable but more diagnostic local CR trend data.",
        "affected_reasoning_operation": "Risk/priority ranking of competing work orders during outage scoping",
        "evidence_available_at_time": [
          "Two prior CRs on FW-IV-204 closed as acceptable-as-found",
          "No adverse trend in packing leak rate",
          "Recently recounted sister-unit valve failure story circulating among staff"
        ],
        "required_textual_manifestation": "Coordinator explicitly cites the memorable sister-unit incident as the deciding factor for elevating FW-IV-204's priority, over the flat local trend data, without independently re-checking the trend numbers.",
        "plausible_nonbias_interpretation": "A cautious planner reasonably erring toward conservatism given any valve packing history, regardless of recall vividness.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "availability bias",
          "heuristic",
          "recall vividness",
          "cognitive bias"
        ]
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 2,
        "mechanism": "Under time pressure and limited capacity to evaluate all crew-configuration permutations, coordinator selects the first option clearing minimum constraints rather than continuing search toward an optimal allocation, consistent with satisficing under bounded cognitive/time resources.",
        "affected_reasoning_operation": "Resource/crew allocation decision-making under constraint",
        "evidence_available_at_time": [
          "Nearly exhausted craft-hour budget",
          "Multiple feasible crew configurations requiring comparison of cost, fatigue, sequencing",
          "One-hour deadline imposed by Outage Manager"
        ],
        "required_textual_manifestation": "Coordinator states they picked the first configuration that met minimum requirements 'to keep things moving' rather than comparing the remaining options, and only learns later a marginally better one existed.",
        "plausible_nonbias_interpretation": "A legitimate, expertise-based triage decision appropriate for real-time operational constraints where full optimization is infeasible.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "bounded rationality",
          "satisficing",
          "cognitive load",
          "heuristic shortcut"
        ]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 3,
        "mechanism": "Coordinator forms an early working theory (misalignment from valve rework) and selectively requests/reviews only the vibration data segment consistent with that theory, while not requesting the lubrication log or full trend history that could disconfirm or complicate it.",
        "affected_reasoning_operation": "Evidence selection and interpretation during anomaly investigation",
        "evidence_available_at_time": [
          "Mild vibration anomaly on adjacent pump bearing after valve rework",
          "Unrequested lubrication log entry existing in the record system",
          "Full bearing vibration trend history not yet pulled"
        ],
        "required_textual_manifestation": "Coordinator describes requesting only the specific vibration readings that fit the misalignment explanation, closing the item on that basis, and later acknowledging the lubrication log was available but not sought at the time.",
        "plausible_nonbias_interpretation": "A time-efficient, experience-based diagnostic shortcut focusing on the most likely proximate cause given the just-completed valve work.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "confirmation bias",
          "selective evidence",
          "disconfirming evidence",
          "cognitive bias"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control generated in this specification."
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
      "Confirm exactly 4 decision points are present in the timeline",
      "Confirm exactly 1 Availability Bias instance is embedded, located only at decision point 1",
      "Confirm exactly 1 Bounded Rationality instance is embedded, located only at decision point 2",
      "Confirm exactly 1 Confirmation Bias instance is embedded, located only at decision point 3",
      "Confirm decision point 4 contains no intentionally embedded named-bias instance",
      "Confirm no bias name, definition, or psychological label appears in interview text",
      "Confirm each instance has a plausible non-bias explanation present in probe answers",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points and probe plan density",
      "Confirm consequences at each decision point do not mechanically prove bias presence or absence"
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
