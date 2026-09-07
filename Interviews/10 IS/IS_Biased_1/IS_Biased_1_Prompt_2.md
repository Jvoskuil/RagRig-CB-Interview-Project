You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IS_Biased_1",
  "domain_id": "IS",
  "domain": "Information Systems, human-computer interaction, and interaction design",
  "role": "Product Manager (Digital Platform)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Onboarding Wizard Decision at CollabHub",
    "scenario_summary_internal": "A PM at a mid-size B2B collaboration-software platform (CollabHub) investigates a 32% drop-off at the account-setup step of the signup funnel ahead of a Q3 board review. Across four chronological decision points, the PM diagnoses the problem, chooses a redesign approach, allocates scarce engineering resources, and makes a launch call under time pressure. At decision point 2, the PM adopts an 'AI-guided setup wizard' pattern primarily because several visible competitor platforms and peer PMs in an industry Slack group have rapidly adopted it, discounting internal cohort data pointing to a different friction source (a payment-field issue), consistent with herding.",
    "occupational_realism": {
      "objective": "Diagnose and reduce a sudden increase in signup-funnel drop-off before the quarterly board review, without destabilizing the sprint roadmap.",
      "setting": "Mid-size B2B SaaS collaboration platform, in-house product team, four-week sprint window, distributed team using shared analytics dashboards and a cross-company PM Slack community.",
      "constraints": [
        "Board review in five weeks",
        "Limited engineering capacity shared with a bug-fix backlog",
        "Small internal user-research team with a two-week interview lead time",
        "Incomplete instrumentation on the payment step of the funnel",
        "Pressure from sales leadership citing competitor feature parity"
      ],
      "stakeholders": [
        "Product Manager (protagonist)",
        "VP of Product",
        "Engineering lead",
        "Data analyst",
        "UX researcher",
        "Sales director",
        "External peer PMs in industry Slack community"
      ],
      "technical_terms_to_use": [
        "onboarding funnel",
        "activation rate",
        "cohort analysis",
        "drop-off step",
        "SSO",
        "funnel instrumentation",
        "canary release",
        "sprint capacity",
        "feature parity",
        "heatmap analytics"
      ],
      "technical_terms_to_avoid": [
        "herding",
        "bandwagon effect",
        "social proof",
        "conformity bias",
        "peer pressure",
        "groupthink",
        "cognitive bias",
        "irrational"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Weekly dashboard shows a 32% drop-off increase at the account-setup step over three weeks",
          "No qualitative user feedback yet collected",
          "Data analyst flags that instrumentation on the payment sub-step is incomplete"
        ],
        "new_information_after_decision": [
          "Funnel analytics show elevated abandonment specifically after the payment-detail field, not the initial account fields",
          "A quick competitor teardown reveals three peers have shipped new onboarding patterns in the last month"
        ],
        "alternatives": [
          "Commission a two-week qualitative user-interview study",
          "Run an internal funnel/heatmap analytics deep dive this week",
          "Skim publicly available competitor teardown reports for quick signal"
        ],
        "intended_action": "PM combines a rapid internal analytics review with a light competitor scan, deferring formal interviews due to the board timeline."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Internal cohort data suggests the sharpest abandonment occurs right after the payment-detail field, in a subgroup added last month",
          "Three named competitor platforms have shipped an 'AI-guided setup wizard' pattern within the last six weeks",
          "An industry analyst newsletter and the PM's cross-company Slack group report that 'most top SaaS onboarding flows now use guided AI wizards'",
          "Internal sample size for the affected cohort is small (approximately 140 users) and not yet statistically stable"
        ],
        "new_information_after_decision": [
          "Engineering estimates the wizard will take three sprints to build",
          "A follow-up analytics review (after the decision) shows the payment-field friction persists independent of the wizard concept"
        ],
        "alternatives": [
          "Build the AI-guided setup wizard adopted by competitors",
          "Run a targeted fix on the payment-field step identified in internal cohort data",
          "Run a small controlled A/B test comparing a wizard concept against a payment-field fix before committing engineering resources"
        ],
        "intended_action": "PM commits to building the AI-guided wizard, citing rapid competitor and peer-community adoption as the primary justification, while treating the internal payment-field signal as secondary."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engineering lead confirms building the wizard requires reallocating two engineers from the bug-fix backlog for three sprints",
          "Backlog contains several unresolved defects reported by enterprise customers",
          "Sales director requests wizard prioritization to match competitor demos in active deals"
        ],
        "new_information_after_decision": [
          "Two enterprise bug tickets escalate in severity during the reallocation window",
          "Engineering reports the wizard build is on schedule but payment-field code is untouched"
        ],
        "alternatives": [
          "Fully reallocate engineers to the wizard build",
          "Split capacity between a partial wizard build and the payment-field fix",
          "Delay the wizard and prioritize the escalating backlog defects"
        ],
        "intended_action": "PM authorizes full reallocation to the wizard build, deferring the backlog defects and the payment-field fix."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "QA has completed only partial regression testing due to compressed schedule",
          "Board review is in four days",
          "Early canary metrics on the wizard are inconclusive due to low traffic",
          "Payment-field abandonment metric has not moved"
        ],
        "new_information_after_decision": [
          "Post-launch activation rate shows no statistically significant change versus the prior month",
          "Support tickets mention continued difficulty at the payment step"
        ],
        "alternatives": [
          "Launch the wizard to 100% of new signups before the board review",
          "Launch to a 10% canary cohort and monitor for one more week",
          "Delay launch one week to complete regression testing and add payment-field instrumentation"
        ],
        "intended_action": "PM launches to 100% of new signups ahead of the board review, accepting the incomplete regression testing."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first alerted you to the onboarding problem?",
        "What was your primary objective when you started looking into this?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you look at next?",
        "At what point did competitor activity enter your thinking?",
        "How did the internal cohort data evolve as you worked through this?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you at that moment?",
        "What sources did you weigh most heavily, and why?",
        "What alternatives did you consider, and why did you rule them out?",
        "What was your goal at that specific point in the process?",
        "Had you handled a similar situation before? How did that shape this decision?",
        "How much time pressure did you feel at that point?",
        "How confident were you in the data you had?",
        "If the competitor activity hadn't been visible to you, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If you had two more weeks before the board review, what would you have done differently?",
        "If the payment-field signal had come from a larger sample, would that have changed your decision at that stage?",
        "Looking back, what would you tell a peer PM facing a similar signal about a competitor trend?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "herd_01",
        "bias": "Herding",
        "decision_point": 2,
        "mechanism": "PM selects the onboarding redesign approach primarily on the basis that multiple competitors and peer PMs have rapidly adopted the same pattern, treating adoption prevalence itself as the main evidentiary signal, and downweighting an available internal cohort signal that points to a different root cause.",
        "affected_reasoning_operation": "evidence weighting during redesign-approach selection",
        "evidence_available_at_time": [
          "Internal cohort data indicating payment-field friction",
          "Small, statistically unstable internal sample (~140 users)",
          "Three competitor platforms shipping an AI-guided wizard within six weeks",
          "Industry Slack group and analyst newsletter framing wizard adoption as near-universal among top SaaS platforms"
        ],
        "required_textual_manifestation": "The PM explicitly cites 'everyone else is doing this now' / peer and competitor adoption volume as the deciding factor for choosing the wizard, while acknowledging but setting aside the payment-field signal, without independently testing the wizard concept against the internal data before committing resources.",
        "plausible_nonbias_interpretation": "Could be read as a defensible strategic bet on feature parity for sales reasons, or as a rational response to a genuinely small and unreliable internal sample — the interview must include enough detail (e.g., PM's own words prioritizing adoption prevalence over the specific cohort signal) to distinguish it from this reasonable alternative.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "herding",
          "bandwagon",
          "social proof",
          "conformity",
          "everyone is doing it therefore correct"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' and no paired control scenario was supplied."
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
      "Exactly one Herding instance planned, assigned to decision point 2 only",
      "No bias vocabulary appears in probe_plan or timeline text",
      "Decision points 1, 3, and 4 contain no intentional bias instances",
      "Internal cohort signal (payment-field friction) is present before and remains unresolved after the biased decision, enabling a non-bias interpretation to also be plausible",
      "Word count target 1,350 (range 1,215-1,485) achievable given 4 decision points with moderate probe depth and one embedded instance",
      "Technical-terms-to-avoid list checked against all planned decision-point language"
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
