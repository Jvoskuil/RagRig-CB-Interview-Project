You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IA_Biased_4",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Financial Crime/Threat Intelligence Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Meridian Trade Network: Suspected Sanctions Evasion via Layered Shell Invoicing",
    "scenario_summary_internal": "A financial crime intelligence analyst at a mid-size bank's FIU receives an automated alert flagging a cluster of trade-finance transactions linked to a Central Asian trading company suspected of routing goods for a sanctioned end-user. The analyst must triage the alert, evaluate a corroborating tip from an external intelligence vendor, decide whether to wait for outstanding correspondent-bank records before escalating, and estimate how long full verification will take before a regulatory reporting deadline. The case echoes a prior, successfully prosecuted sanctions-evasion typology the analyst worked on eighteen months earlier, creating fertile ground for pattern-driven reasoning errors under time pressure.",
    "occupational_realism": {
      "objective": "Determine whether the Meridian trade-finance activity constitutes probable sanctions evasion and produce a timely, defensible intelligence escalation to compliance/law enforcement before the regulatory filing window closes.",
      "setting": "Financial Intelligence Unit (FIU) of a mid-size international bank, hybrid remote/office work, coordinating with correspondent banks, an external OSINT vendor, and internal compliance counsel.",
      "constraints": [
        "10-business-day regulatory filing deadline from initial alert",
        "Correspondent bank in a secondary jurisdiction is slow to respond to information requests",
        "Analyst is simultaneously covering two other active cases",
        "Escalating a false positive damages a profitable corporate relationship and analyst credibility",
        "Underreporting risks regulatory penalty and reputational harm"
      ],
      "stakeholders": [
        "Financial Crime/Threat Intelligence Analyst (interviewee)",
        "FIU team lead",
        "Compliance counsel",
        "External OSINT/intelligence vendor",
        "Correspondent bank compliance liaison",
        "Relationship manager for the corporate client"
      ],
      "technical_terms_to_use": [
        "trade-based money laundering (TBML)",
        "correspondent banking",
        "sanctions typology",
        "beneficial ownership",
        "SAR/STR filing",
        "invoice mismatch",
        "know-your-customer (KYC) refresh",
        "escalation window"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "wishful thinking",
        "belief bias",
        "selective attention",
        "planning fallacy",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Automated alert flags three invoices from Meridian Trading LLC with quantity/value mismatches",
          "Meridian's ultimate beneficial owner shares a registered agent with a company from a 2024 sanctions-evasion case the analyst worked",
          "A separate counterparty in the same batch operates in an unrelated logistics sector with no prior typology match",
          "Alert volume this week is above average across the team"
        ],
        "new_information_after_decision": [
          "The unrelated logistics counterparty later shows an unusual same-day wire pattern that goes unexamined",
          "Team lead asks why the logistics counterparty wasn't included in the initial scoping note"
        ],
        "alternatives": [
          "Scope the review narrowly around the shell-company/registered-agent pattern matching the prior case",
          "Scope the review broadly across all flagged counterparties regardless of typology fit",
          "Request additional automated screening before committing to a scope"
        ],
        "intended_action": "Analyst scopes the case narrowly around entities matching the prior sanctions-evasion typology and sets aside the unrelated logistics counterparty as low priority."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "External OSINT vendor sends a report arguing Meridian is 'highly likely' tied to the sanctioned end-user",
          "The vendor's supporting argument relies on a chain of corporate registry links that has a logical gap: it assumes two similarly-named entities are identical without independent confirmation",
          "The report's bottom-line conclusion matches the analyst's working theory from Phase 1",
          "A junior analyst on the team flags that the entity-matching step in the vendor's argument is unverified"
        ],
        "new_information_after_decision": [
          "A later document pull shows the two similarly-named entities are in fact legally distinct with different beneficial owners",
          "Compliance counsel asks what independent verification was done on the vendor's entity-matching claim"
        ],
        "alternatives": [
          "Accept the vendor's conclusion because it fits the suspected sanctions-evasion narrative and proceed",
          "Independently verify the entity-matching step before weighting the report's conclusion",
          "Request a second vendor opinion to cross-check the argument's validity"
        ],
        "intended_action": "Analyst accepts the vendor's conclusion as probative because it aligns with the working theory, without separately assessing whether the argument's internal logic (the entity-matching step) actually holds."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Correspondent bank has not yet returned requested SWIFT MT202/MT103 records confirming fund flow to the suspected end-user",
          "Prior similar requests to this correspondent bank have taken 12-15 business days on average",
          "Filing deadline is 6 business days away",
          "No written confirmation exists that the records will arrive in time"
        ],
        "new_information_after_decision": [
          "On day 6, the correspondent bank confirms records will take another 10 business days",
          "Team lead notes the case file was left without a contingency escalation path"
        ],
        "alternatives": [
          "Proceed on the assumption the records will arrive before the deadline and delay drafting the escalation",
          "Draft a conditional escalation now that does not depend on the pending records, with a plan to supplement if records arrive",
          "Immediately request an extension from compliance given known correspondent-bank delays"
        ],
        "intended_action": "Analyst delays drafting the escalation, expecting the outstanding SWIFT records will arrive in time despite no confirmation and a track record of slower turnaround."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Remaining verification tasks include: reconciling three invoice sets, drafting the narrative, and obtaining compliance sign-off",
          "Historical average time for comparable cases with cross-border verification has been 5-7 business days",
          "Analyst estimates the remaining work at 2 business days based on the best-case sequence with no rework",
          "Two other active cases still require partial attention this week"
        ],
        "new_information_after_decision": [
          "Invoice reconciliation surfaces a discrepancy requiring a follow-up query, consuming an extra day",
          "Compliance sign-off takes longer than expected due to a routine but unanticipated question"
        ],
        "alternatives": [
          "Plan the remaining timeline using the best-case, no-rework scenario",
          "Plan the remaining timeline using historical base rates for comparable cases",
          "Build in an explicit buffer for likely follow-up queries and competing case demands"
        ],
        "intended_action": "Analyst commits to a 2-day completion estimate based on the best-case task sequence, without adjusting for historical base rates or known competing demands."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this case first came to your attention?",
        "What was your overall objective once you saw the alert?"
      ],
      "timeline_reconstruction": [
        "What happened right after you opened the alert?",
        "Walk me through what you did once the OSINT vendor's report arrived.",
        "What happened while you were waiting on the correspondent bank?",
        "How did you plan out the remaining work before the deadline?"
      ],
      "decision_point_probes": [
        "What specific cues made you decide to scope the case the way you did?",
        "What sources of information did you weigh most heavily when reading the vendor's report, and why?",
        "What told you the outstanding records would or wouldn't arrive in time?",
        "How did you arrive at your time estimate for the remaining tasks?",
        "What alternatives did you consider at each of those points, and why did you rule them out?",
        "Looking back, what was your basis for that decision at the time?"
      ],
      "decision_basis": [
        "What made you confident in that call at the time?",
        "Did anything give you pause before you committed to that course of action?"
      ],
      "prior_experience": [
        "Had you handled a similar case before? How did that shape your approach here?"
      ],
      "time_pressure": [
        "How much did the deadline affect how you approached each step?"
      ],
      "uncertainty": [
        "What were you least certain about at each of these points?"
      ],
      "closing_hypotheticals": [
        "If the unrelated logistics counterparty had been flagged as high-risk from the start, how would your approach have changed?",
        "If the vendor's report had reached the opposite conclusion, how would you have responded?",
        "If you'd known upfront the correspondent bank would take 15 days, what would you have done differently?",
        "If a colleague had reviewed your time estimate before you committed to it, what do you think they would have flagged?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "sab_01",
        "bias": "Selective Attention Bias",
        "decision_point": 1,
        "mechanism": "Analyst allocates review attention to entities matching a familiar registered-agent pattern from a prior case, while the unrelated logistics counterparty in the same alert batch is deprioritized without any substantive risk assessment, purely because it does not match the salient prior pattern.",
        "affected_reasoning_operation": "Evidence-selection / initial scoping of investigation",
        "evidence_available_at_time": [
          "Shared registered agent between Meridian and a prior sanctions-evasion case",
          "Unrelated logistics counterparty present in the same alert batch with no typology link",
          "Above-average alert volume creating pressure to triage quickly"
        ],
        "required_textual_manifestation": "Analyst explains narrowing the scope specifically because of the registered-agent match, and separately acknowledges the logistics counterparty was set aside without being evaluated on its own merits, only realizing its relevance after a later unusual wire pattern surfaces.",
        "plausible_nonbias_interpretation": "Prioritizing entities with a known typology match under time pressure could be read as reasonable triage efficiency rather than a reasoning error.",
        "strength": "subtle",
        "do_not_make_explicit": ["selective attention", "bias", "tunnel vision"]
      },
      {
        "instance_id": "bb_01",
        "bias": "Belief bias",
        "decision_point": 2,
        "mechanism": "Analyst evaluates the OSINT vendor's argument as sound primarily because its conclusion matches the analyst's pre-existing suspicion about Meridian, without independently checking whether the argument's key premise (the entity-matching step) is actually valid, despite a colleague flagging the gap.",
        "affected_reasoning_operation": "Argument evaluation / evidence weighting",
        "evidence_available_at_time": [
          "Vendor report conclusion aligning with analyst's working theory",
          "An unverified logical step in the vendor's argument (assumed entity identity)",
          "A junior colleague's explicit flag of the unverified step"
        ],
        "required_textual_manifestation": "Analyst describes accepting the report's conclusion as strong evidence because it 'made sense' given what was already suspected, while treating the colleague's concern about the unverified entity-matching step as a minor procedural note rather than a reason to re-examine the argument's validity.",
        "plausible_nonbias_interpretation": "Trusting a vendor report that aligns with independently formed suspicion could be framed as reasonable convergent-evidence reasoning rather than a validity error.",
        "strength": "moderate",
        "do_not_make_explicit": ["belief bias", "logical validity", "cognitive bias"]
      },
      {
        "instance_id": "wt_01",
        "bias": "Wishful Thinking",
        "decision_point": 3,
        "mechanism": "Analyst delays drafting the escalation and continues to expect the outstanding correspondent-bank records will arrive before the deadline, despite having no confirmation of this and possessing historical data showing this correspondent typically takes longer than the time remaining.",
        "affected_reasoning_operation": "Prediction / risk forecasting under uncertainty",
        "evidence_available_at_time": [
          "No written confirmation that records will arrive within the remaining window",
          "Historical average turnaround from this correspondent bank exceeding the time remaining",
          "Desire to complete the case cleanly with full corroboration"
        ],
        "required_textual_manifestation": "Analyst states a belief that the records would 'probably come through in time' or similar, explicitly tied to wanting a complete file rather than to any evidence the timeline had improved, and delays contingency drafting on that basis.",
        "plausible_nonbias_interpretation": "Waiting for corroborating records before escalating could be framed as a legitimate preference for evidentiary completeness rather than an unwarranted expectation.",
        "strength": "moderate",
        "do_not_make_explicit": ["wishful thinking", "optimism bias", "cognitive bias"]
      },
      {
        "instance_id": "pf_01",
        "bias": "Planning fallacy",
        "decision_point": 4,
        "mechanism": "Analyst estimates the remaining workload using a best-case, no-rework task sequence, disregarding known historical base rates for comparable cross-border verification cases and the presence of competing case demands, resulting in an estimate substantially shorter than typical completion times.",
        "affected_reasoning_operation": "Time/effort estimation for task completion",
        "evidence_available_at_time": [
          "Historical base rate of 5-7 business days for comparable verification cases",
          "Two other active cases still requiring partial attention",
          "A best-case task sequence with no anticipated rework"
        ],
        "required_textual_manifestation": "Analyst explains arriving at a 2-day estimate by walking through the ideal task sequence, without referencing or adjusting for the historical base rate or the competing caseload, and this estimate is later overtaken by an unanticipated reconciliation query and slower sign-off.",
        "plausible_nonbias_interpretation": "Estimating based on the planned task sequence could be seen as standard project scoping rather than a systematic underestimation error.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "cognitive bias", "underestimation"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, no control pairing requested."
    },
    "counterfactual_specification": {
      "causal_variable": "not_applicable",
      "original_state": "not_applicable",
      "counterfactual_state": "not_applicable",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "not_applicable",
      "causal_test_question": "not_applicable"
    },
    "generation_checks": [
      "Exactly 4 decision points planned, one per manifest bias, no bias sharing a decision point.",
      "Exactly one instance per bias per manifest (1x Wishful Thinking, 1x Belief bias, 1x Selective Attention Bias, 1x Planning fallacy) = 4 total instances.",
      "No bias labels, definitions, or psychological terminology to appear in the public interview.",
      "Each instance has a distinct evidence trace and a plausible non-bias interpretation to avoid mechanical proof of bias.",
      "Target interview length 1,350 words (acceptable range 1,215-1,485) achievable via 4 decision points with moderate probe density and no repetitive exposition.",
      "Consequences at each decision point are realistic and do not deterministically confirm bias (e.g., logistics counterparty pattern, entity mismatch discovery, correspondent delay, reconciliation query) — all plausible independent of bias status.",
      "Technical vocabulary list ensures domain realism; avoid-list ensures no leakage of bias terminology."
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
