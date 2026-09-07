You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IS_Biased_2",
  "domain_id": "IS",
  "domain": "Information Systems, human-computer interaction, and interaction design",
  "role": "Software Engineering Team Lead",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The QuickCache Crossroads",
    "scenario_summary_internal": "A software engineering team lead must resolve a worsening performance problem in an internal support-operations dashboard before a quarterly leadership demo. The in-house caching layer the team built eight months ago ('QuickCache') is implicated. Over four chronological decision points, the lead triages the problem, decides how to respond to QuickCache's failure (continue investing vs. switch to a mature alternative), decides who should own the urgent fix given a team member's recent outage, and finally decides how to report status to leadership. The narrative embeds exactly one irrational-escalation instance (continued investment in QuickCache driven by prior sunk effort rather than forward-looking value) and exactly one negativity-bias instance (a single recent, vivid outage disproportionately shaping a personnel-risk judgment despite a strong overall track record).",
    "occupational_realism": {
      "objective": "Restore acceptable dashboard latency for the customer-support platform before a quarterly leadership demo, while managing team capacity and reputational risk.",
      "setting": "Mid-size SaaS company; internal analytics/support-ops platform team of five engineers reporting to the interviewee; two-week sprint window before a board-facing product demo.",
      "constraints": [
        "Hard deadline: leadership demo in two weeks, later compressed to three days",
        "Limited budget for new third-party tooling this quarter",
        "Team morale strained after a recent production incident",
        "Partial diagnostic visibility; full root-cause data arrives incrementally",
        "Only two engineers available with relevant caching-layer familiarity"
      ],
      "stakeholders": [
        "Team lead (interviewee)",
        "VP of Engineering",
        "Priya (senior engineer, original QuickCache designer)",
        "Dev (engineer involved in a recent production outage)",
        "Marcus (engineer with a longer history of missed deadlines)",
        "Product manager",
        "Customer support lead"
      ],
      "technical_terms_to_use": [
        "caching layer",
        "cache invalidation",
        "latency",
        "profiling",
        "technical debt",
        "incident postmortem",
        "feature flag",
        "on-call rotation",
        "rollback",
        "load testing"
      ],
      "technical_terms_to_avoid": [
        "sunk cost fallacy",
        "escalation of commitment",
        "negativity bias",
        "recency effect",
        "cognitive bias",
        "irrational escalation",
        "confirmation bias",
        "anchoring"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dashboard load times have tripled over two weeks",
          "Customer-support tickets about slow load are rising",
          "QuickCache was the last major change deployed to this subsystem",
          "No full-stack profiling has been run yet"
        ],
        "new_information_after_decision": [
          "Profiling confirms QuickCache adds latency under high load",
          "Profiling also surfaces an unrelated missing database index"
        ],
        "alternatives": [
          "Run full-stack instrumentation before attributing cause to any component",
          "Focus investigation narrowly on QuickCache since it was the most recent change",
          "Escalate immediately to the infrastructure team to check shared resource contention"
        ],
        "intended_action": "Lead orders targeted profiling of QuickCache based on the timing correlation with its deployment, a reasonable diagnostic narrowing rather than a biased inference; no intended bias instance at this phase."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "QuickCache took roughly eight months and three prior patch cycles to build and stabilize",
          "Each prior patch produced only marginal, temporary latency improvement",
          "A mature open-source Redis-backed alternative could replace QuickCache in about one sprint with known reliability characteristics",
          "Priya, who designed QuickCache, argues the team is 'nearly there' and one more patch will resolve it",
          "Leadership previously praised QuickCache publicly as strategic in-house IP"
        ],
        "new_information_after_decision": [
          "The additional patch yields only a 15% improvement, insufficient to meet the demo deadline",
          "Remaining timeline to a durable fix is now uncertain",
          "Team morale is further strained by the extended effort"
        ],
        "alternatives": [
          "Commit another sprint to further optimize QuickCache's invalidation logic",
          "Abandon QuickCache and migrate to the Redis-backed alternative",
          "Run both solutions in parallel behind a feature flag to compare before committing"
        ],
        "intended_action": "Lead commits an additional sprint to further patching QuickCache, citing the months of engineering time and specialized internal expertise already invested and a reluctance to 'waste' that work, even though the profiling data points toward a structural redesign rather than an incremental patch, and the alternative has a clearer risk profile."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dev had a production outage three weeks ago, traced to a rushed deploy under time pressure; the postmortem showed prompt, effective remediation and process fixes",
          "Dev otherwise has eighteen months of consistently strong reviews and on-time delivery, and the deepest working knowledge of QuickCache internals",
          "Marcus has a longer pattern of several missed deadlines over the past year, with no single dramatic incident",
          "The urgent fix requires deep QuickCache familiarity and must be delivered within days"
        ],
        "new_information_after_decision": [
          "Reassigning ownership away from Dev creates friction and confusion during handoff",
          "The fix takes longer than planned because the assigned engineer is less familiar with QuickCache internals"
        ],
        "alternatives": [
          "Assign the critical fix to Dev given his QuickCache expertise",
          "Assign the fix to Marcus to reduce load on Dev after the recent incident",
          "Pair Dev and Marcus so responsibility and risk are shared"
        ],
        "intended_action": "Lead sidelines Dev from the critical fix and assigns it to Marcus, weighting the vivid recent outage heavily against Dev despite his strong eighteen-month record and the incident's well-documented resolution, while treating Marcus's more diffuse pattern of missed deadlines as less concerning because it lacks a single salient episode."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The demo is three days away",
          "The fix is only partially effective; latency is improved but not fully resolved",
          "Leadership expects a status update ahead of the demo"
        ],
        "new_information_after_decision": [
          "Leadership accepts the partial-fix plan with monitoring",
          "A follow-up sprint is scheduled to complete the redesign"
        ],
        "alternatives": [
          "Present a transparent status update with a mitigation and monitoring plan",
          "Request a delay of the demo until the fix is complete",
          "Ship the partial fix silently without flagging remaining risk"
        ],
        "intended_action": "Lead presents a transparent status update proposing to ship the partial improvement with monitoring and a scheduled follow-up sprint, a defensible trade-off given the constraints; no intended bias instance at this phase."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first alerted you to a problem with the dashboard?",
        "What was your role and what were you responsible for delivering?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did QuickCache come into the picture?",
        "How did the team's workload and staffing shift over the two weeks?"
      ],
      "decision_point_probes": [
        "What cues made you focus on that particular explanation at the time?",
        "What information sources did you rely on for that decision, and were there others you didn't use?",
        "What were you ultimately trying to achieve when you made that call?",
        "What other options did you consider, and why did you rule them out?",
        "What was the main basis for the decision you made?",
        "Had you faced a similar situation before, and did that experience shape your choice?",
        "How much time pressure were you under at that point?",
        "How confident were you in the information you had when you decided?",
        "If you'd had more time or different information, would you have chosen differently?"
      ],
      "closing_hypotheticals": [
        "If QuickCache had been a vendor product instead of something your team built, would your approach have differed?",
        "If Dev's outage had happened a year earlier instead of three weeks before this decision, would you have assigned the fix differently?",
        "Looking back, what would you tell a peer facing a similar in-house-versus-alternative decision?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "decision_point": 2,
        "mechanism": "Continued commitment to further investment in QuickCache is justified primarily by the amount of time, effort, and internal expertise already sunk into it, rather than by a forward-looking comparison of expected cost, risk, and benefit against the available alternative.",
        "affected_reasoning_operation": "Resource-allocation decision under uncertainty; weighting of prior investment against prospective outcomes",
        "evidence_available_at_time": [
          "Eight months and three prior patch cycles already invested in QuickCache",
          "Prior patches produced only marginal, temporary gains",
          "A lower-risk, faster alternative exists with known reliability",
          "Profiling data suggests a structural redesign, not a patch, is needed"
        ],
        "required_textual_manifestation": "The lead's stated rationale for choosing another patch cycle explicitly invokes the time/effort already spent or the team's specialized expertise as a reason to continue, rather than citing a forward-looking comparison showing the patch path is expected to outperform switching.",
        "plausible_nonbias_interpretation": "The lead could defensibly argue that in-house control, avoided vendor dependency, or long-term customization benefits outweigh switching costs, provided that reasoning rests on those forward-looking benefits rather than on the sunk months already spent.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "sunk cost",
          "escalation of commitment",
          "irrational escalation",
          "any explicit bias label"
        ]
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "decision_point": 3,
        "mechanism": "A single vivid, recent negative event (Dev's outage) is given disproportionate weight in a personnel-risk judgment relative to a larger, more diffuse body of both positive (Dev's eighteen-month record) and comparably negative (Marcus's repeated missed deadlines) evidence.",
        "affected_reasoning_operation": "Risk assessment and task-assignment judgment based on weighting of historical performance evidence",
        "evidence_available_at_time": [
          "Postmortem showing the outage was promptly and effectively remediated",
          "Eighteen months of consistently strong performance reviews for Dev",
          "Marcus's pattern of several missed deadlines over the past year",
          "Dev has the deepest technical familiarity with QuickCache"
        ],
        "required_textual_manifestation": "The lead's explanation for reassigning the task centers on the vividness or recency of Dev's single incident, while explicitly or implicitly discounting Marcus's more numerous but less salient shortfalls, without citing a specific unresolved skill or trust gap tied to the outage.",
        "plausible_nonbias_interpretation": "The lead could defensibly argue caution is warranted after any recent incident before assigning a mission-critical task, provided that reasoning is grounded in a specific, still-unresolved capability concern rather than the sheer salience of one recent event.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "negativity bias",
          "recency effect",
          "availability heuristic",
          "any explicit bias label"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition interview, not a control."
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
      "Confirm exactly one Irrational Escalation instance appears, located at decision point 2, tied to the QuickCache patch-vs-switch choice.",
      "Confirm exactly one Negativity Bias instance appears, located at decision point 3, tied to the Dev-vs-Marcus assignment choice.",
      "Confirm decision points 1 and 4 contain no intentionally embedded instances of either named bias.",
      "Confirm no bias labels, definitions, or psychological terminology appear anywhere in the public interview text.",
      "Confirm each embedded instance includes both the biased rationale and a plausible non-bias alternative reading, without resolving which applies.",
      "Confirm the interview contains exactly four decision points, each with at least two alternatives, pre-decision facts, and post-decision new information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count falls within 1,215-1,485 words without repetitive exposition padding.",
      "Confirm consequences described do not mechanically prove or disprove whether either decision was biased."
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
