You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "AV_Biased_7",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Continuing Airworthiness Manager (CAMO)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Recurring Hydraulic Leak Report",
    "scenario_summary_internal": "A CAMO manager at a regional airline oversees continuing airworthiness for a fleet of turboprops. A recurring but historically minor hydraulic seepage finding on one aircraft resurfaces during a pre-lease-return inspection window, coinciding with heavy schedule pressure and an experienced line engineer's reassurance. The manager must decide how to classify, defer, or escalate the finding across four sequential decisions, ultimately releasing the aircraft to service before a full root-cause investigation is closed out.",
    "occupational_realism": {
      "objective": "Determine airworthiness disposition of a recurring hydraulic seepage finding on a leased turboprop before a contractual lease-return deadline, while maintaining fleet dispatch reliability.",
      "setting": "Regional airline CAMO office and hangar line maintenance, mid-size fleet, third-party MRO involvement, lease-return inspection window with a fixed deadline in five days.",
      "constraints": [
        "Contractual lease-return deadline in five days with financial penalty for delay",
        "Limited hangar slot availability shared with two other aircraft",
        "MRO third-party engineering support only available for two more days",
        "Minimum equipment list and deferred defect procedures must be followed",
        "Regulatory reporting obligations for recurring defects"
      ],
      "stakeholders": [
        "CAMO Manager (interviewee)",
        "Line Maintenance Engineer (experienced, 22 years)",
        "Quality/Airworthiness Review Board",
        "Lessor's technical representative",
        "Fleet operations/scheduling manager"
      ],
      "technical_terms_to_use": [
        "MEL (Minimum Equipment List)",
        "deferred defect",
        "hydraulic seepage vs. leakage classification",
        "root cause analysis",
        "airworthiness directive",
        "reliability program trend data",
        "borescope inspection",
        "release to service"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "cognitive error",
        "psychological terminology"
      ],
      "timeline": [
        {
          "phase": 1,
          "decision_point": true,
          "facts_available_before_decision": [
            "Routine borescope and visual inspection flags hydraulic seepage at a fitting previously logged twice in the past 8 months",
            "Reliability trend data shows seepage rate within MEL tolerance historically",
            "Lease-return deadline is five days away"
          ],
          "new_information_after_decision": [
            "Line engineer notes the seepage pattern looks 'the same as always' and recommends standard wipe-and-monitor procedure",
            "No immediate escalation to Quality is made"
          ],
          "alternatives": [
            "Classify as routine recurring seepage and defer per MEL",
            "Escalate immediately for expanded inspection given recurrence"
          ],
          "intended_action": "Manager accepts the recurring classification and defers further action, treating the third occurrence as consistent with the prior benign pattern."
        },
        {
          "phase": 2,
          "decision_point": true,
          "facts_available_before_decision": [
            "Line engineer, citing decades of experience, states this fitting type 'never fails badly, it just seeps'",
            "No formal fault-tree or updated root cause analysis has been run for this tail number",
            "Hangar slot pressure is increasing"
          ],
          "new_information_after_decision": [
            "Manager defers ordering a full fault-tree analysis, relying on the engineer's judgment as sufficient technical basis",
            "A junior engineer's suggestion to pull torque and seal specs is not followed up"
          ],
          "alternatives": [
            "Commission a fault-tree/root cause analysis before further disposition",
            "Rely on the experienced engineer's field judgment and proceed to interim clearance"
          ],
          "intended_action": "Manager treats the engineer's confident assessment as equivalent to a validated technical finding and proceeds without independent analysis."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "Reliability program report (auto-generated trend dashboard) shows a green status indicator for this defect category fleet-wide",
            "The dashboard's green rating is based on fleet-average data, not this specific tail number's recurrence pattern",
            "Two hangar days remain before MRO support departs"
          ],
          "new_information_after_decision": [
            "Manager cites the dashboard's green status in the disposition memo as primary justification for continued airworthiness",
            "No manual cross-check of tail-specific history against the fleet-average calculation is performed"
          ],
          "alternatives": [
            "Treat the dashboard's green indicator as one input requiring manual verification against tail-specific history",
            "Accept the automated trend status as sufficient standalone justification for release"
          ],
          "intended_action": "Manager defers to the automated reliability dashboard output as authoritative without checking whether it accounts for the specific aircraft's repeat pattern."
        },
        {
          "phase": 4,
          "decision_point": true,
          "facts_available_before_decision": [
            "Deadline is now two days away; MRO engineering support has left",
            "No new defect has appeared since the last inspection, and the seepage measurement is technically within tolerance",
            "Manager has never seen this specific fitting fail catastrophically at this airline in 15 years"
          ],
          "new_information_after_decision": [
            "Aircraft is released to service and returned to the lessor on schedule",
            "A follow-up borescope inspection recommendation for the next check interval is noted but not made mandatory before dispatch"
          ],
          "alternatives": [
            "Release the aircraft on schedule based on current tolerance readings and past benign history",
            "Request a short deadline extension from the lessor to complete a mandatory root cause closure first"
          ],
          "intended_action": "Manager releases the aircraft on schedule, confident that because no serious failure has occurred before, none will occur now, without recognizing the deadline pressure's influence on that confidence."
        }
      ]
    },
    "probe_plan": {
      "opening": [
        "Can you walk me through what this aircraft's maintenance history looked like going into this inspection cycle?",
        "What was your primary objective during this five-day window?"
      ],
      "timeline_reconstruction": [
        "What specific data or reports did you review before each disposition decision?",
        "Who did you consult, and what did they tell you?",
        "What changed in the information you had between the first and last decision?"
      ],
      "decision_point_probes": [
        "At the point of the third seepage finding, what made you classify it the way you did?",
        "When the line engineer gave his assessment, what independent verification, if any, did you seek?",
        "How did you interpret the reliability dashboard's status indicator, and did you check what data it was built from?",
        "What made you confident enough to release the aircraft at the final deadline?"
      ],
      "decision_basis_and_alternatives": [
        "What alternative actions did you consider at each stage, and why were they set aside?",
        "Looking back, what other explanations could account for the recurring seepage pattern?"
      ],
      "prior_experience_and_time_pressure": [
        "How did your past experience with this fitting type shape your read of the situation?",
        "How much did the lease-return deadline weigh on your decisions at each stage?"
      ],
      "uncertainty_and_hypotheticals": [
        "What was your level of certainty at each decision point, on reflection?",
        "If the deadline had been three weeks out instead of five days, would any decision have changed?",
        "If a different engineer, with less seniority, had given the same assessment, would you have weighed it differently?"
      ],
      "closing_hypotheticals": [
        "If you had to make this same disposition decision again today, what would you do differently, if anything?",
        "What would have needed to be different in the data for you to escalate at the first decision point?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "AV7_apo_01",
        "bias": "Apophenia or Correlation Bias",
        "decision_point": 1,
        "mechanism": "Manager perceives the third seepage occurrence as confirming a stable, meaningful pattern ('consistent with prior benign behavior') from only two prior data points, treating recurrence itself as evidence of harmlessness rather than as an unresolved trend needing investigation.",
        "affected_reasoning_operation": "Pattern classification from limited historical data",
        "evidence_available_at_time": [
          "Two prior seepage logs in 8 months",
          "Reliability trend data showing tolerance-range values"
        ],
        "required_textual_manifestation": "Manager explicitly states the third finding 'fits the pattern we've seen before' and treats that perceived pattern as itself justifying deferral, without acknowledging the small sample size.",
        "plausible_nonbias_interpretation": "MEL procedures may legitimately permit deferral for seepage within tolerance regardless of recurrence count.",
        "strength": "subtle",
        "do_not_make_explicit": ["pattern recognition fallacy", "correlation vs causation", "small sample size"]
      },
      {
        "instance_id": "AV7_aut_01",
        "bias": "Automaticity or Automation Bias",
        "decision_point": 3,
        "mechanism": "Manager accepts the automated reliability dashboard's green/fleet-average status as authoritative justification without manually verifying it reflects this tail number's specific recurrence history.",
        "affected_reasoning_operation": "Evidence weighting and verification of automated output",
        "evidence_available_at_time": [
          "Dashboard green status indicator",
          "Underlying fleet-average (not tail-specific) data basis"
        ],
        "required_textual_manifestation": "Manager cites the dashboard status in the disposition memo as primary justification and does not describe checking whether it accounted for this aircraft's specific repeat pattern.",
        "plausible_nonbias_interpretation": "The dashboard may be a validated, approved tool that management is procedurally entitled to rely on.",
        "strength": "moderate",
        "do_not_make_explicit": ["automation reliance", "verification failure"]
      },
      {
        "instance_id": "AV7_bbs_01",
        "bias": "Bias Blind Spot",
        "decision_point": 4,
        "mechanism": "When asked how deadline pressure influenced the decision, manager acknowledges pressure exists generally in the industry but asserts their own final release decision was purely technical and unaffected by the deadline, despite describing timeline strain throughout the account.",
        "affected_reasoning_operation": "Self-assessment of one's own decision influences during a probe response",
        "evidence_available_at_time": [
          "Manager's own prior statements about escalating schedule pressure",
          "Explicit probe question about deadline influence"
        ],
        "required_textual_manifestation": "Manager states something like 'other managers might rush under deadline pressure, but I based this strictly on the numbers' immediately after having described the tightening schedule as a factor in earlier decisions.",
        "plausible_nonbias_interpretation": "The manager could genuinely have compartmentalized schedule awareness from the technical judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["blind spot", "self versus others asymmetry"]
      },
      {
        "instance_id": "AV7_norm_01",
        "bias": "Normalcy Bias",
        "decision_point": 2,
        "mechanism": "Manager assumes the situation will continue behaving as it always has ('it just seeps, never fails badly') and does not seriously entertain that a departure from the established pattern is possible, despite no root cause analysis ever being performed.",
        "affected_reasoning_operation": "Risk projection under uncertainty",
        "evidence_available_at_time": [
          "Absence of a formal root cause or fault-tree analysis for this tail number",
          "Engineer's characterization of the fitting type's typical behavior"
        ],
        "required_textual_manifestation": "Manager repeats an assumption of continuity ('it's always behaved this way, so it will keep behaving this way') as sufficient basis to skip deeper analysis.",
        "plausible_nonbias_interpretation": "Fitting-type behavior may be well documented industry-wide as low-risk, making continuity a reasonable technical assumption.",
        "strength": "subtle",
        "do_not_make_explicit": ["normalcy", "assumption of continuity"]
      },
      {
        "instance_id": "AV7_exp_01",
        "bias": "Experience Bias or Trusting expert intuition",
        "decision_point": 2,
        "mechanism": "Manager substitutes the senior line engineer's confident field intuition for a structured technical analysis (fault-tree/root cause), treating years of experience as sufficient evidentiary weight to bypass the junior engineer's suggested spec check.",
        "affected_reasoning_operation": "Evidence source selection and weighting",
        "evidence_available_at_time": [
          "Senior engineer's 22 years of experience and confident verbal assessment",
          "Junior engineer's unaddressed suggestion to pull torque/seal specifications"
        ],
        "required_textual_manifestation": "Manager explains deferring to the senior engineer's judgment specifically because of his tenure, and states the junior engineer's suggestion was not pursued as a result.",
        "plausible_nonbias_interpretation": "Deferring to the most experienced technician on a routine finding is a standard and often appropriate practice in maintenance operations.",
        "strength": "moderate",
        "do_not_make_explicit": ["expert intuition substitution", "seniority weighting"]
      },
      {
        "instance_id": "AV7_iov_01",
        "bias": "Illusion of Validity",
        "decision_point": 3,
        "mechanism": "Manager expresses high subjective confidence in the disposition memo's conclusion because the dashboard output and the engineer's assessment 'lined up consistently,' treating this internal consistency as proof of accuracy despite neither source having been independently validated against tail-specific data.",
        "affected_reasoning_operation": "Confidence calibration based on convergence of unverified sources",
        "evidence_available_at_time": [
          "Dashboard green status",
          "Engineer's verbal reassurance",
          "Absence of independent tail-specific verification"
        ],
        "required_textual_manifestation": "Manager states confidence was high specifically because 'everything pointed the same direction,' without noting that the sources shared the same underlying gap in tail-specific verification.",
        "plausible_nonbias_interpretation": "Convergent evidence from multiple independent sources can legitimately increase confidence when the sources are genuinely independent.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of validity", "false convergence"]
      },
      {
        "instance_id": "AV7_opt_01",
        "bias": "Optimism Bias",
        "decision_point": 4,
        "mechanism": "Manager releases the aircraft believing failure is unlikely specifically for this aircraft because of 15 years of personal experience without a catastrophic failure, projecting a favorable outcome for this specific case despite the unresolved investigation, rather than assessing base-rate risk neutrally.",
        "affected_reasoning_operation": "Outcome probability estimation under time pressure",
        "evidence_available_at_time": [
          "15-year personal failure-free history with this fitting type",
          "Unclosed root cause investigation status",
          "Two-day remaining deadline"
        ],
        "required_textual_manifestation": "Manager states confidence that 'this one will be fine' based on personal failure-free history, framing the specific release decision as low-risk without referencing the still-open investigation status.",
        "plausible_nonbias_interpretation": "A genuinely low base rate of failure for this fitting type could justify proceeding even without a closed investigation.",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "base rate neglect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition scenario with no paired control specified."
    },
    "counterfactual_specification": {
      "causal_variable": "Availability of a completed root cause / fault-tree analysis before the final release decision",
      "original_state": "No formal root cause analysis is performed; disposition relies on recurrence pattern, senior engineer intuition, and dashboard trend status",
      "counterfactual_state": "A completed fault-tree analysis is available before the final decision, providing an independently validated technical basis",
      "variables_to_hold_constant": [
        "Lease-return deadline and schedule pressure",
        "Aircraft type and defect history",
        "Personnel involved and their stated experience levels",
        "Reliability dashboard output and its underlying data basis"
      ],
      "expected_causal_difference": "With a validated fault-tree analysis available, the manager's confidence in the final release decision would rest on independently verified evidence rather than on convergent but unverified sources, altering the basis (though not necessarily the outcome) of the illusion-of-validity and experience-bias-driven decisions.",
      "causal_test_question": "Does the presence of an independently validated root cause analysis change how the manager weighs expert intuition and dashboard convergence when reaching the final release decision?"
    },
    "generation_checks": [
      "Exactly 7 biases requested, each with occurrences=1, totaling 7 planned instances",
      "Each instance assigned to a distinct decision point or distinct evidence/reasoning operation within a shared decision point",
      "No more than two instances of any bias share a decision point (max observed: 2, at decision points 2 and 3)",
      "Decision points 2 and 3 each host two distinct-bias instances with different evidence sources (engineer intuition vs. junior suggestion at DP2; dashboard vs. engineer convergence at DP3)",
      "No bias terminology, labels, or explanations appear in probe plan or timeline",
      "Target word count 1,350 (range 1,215-1,485) is achievable given 4 decision points, 7 embedded instances, and probe plan scope without repetitive exposition",
      "Consequences (on-time release, no immediate failure) do not mechanically prove or disprove bias presence"
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
