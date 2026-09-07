You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IS_Ambigious_1",
  "domain_id": "IS",
  "domain": "Information Systems, human-computer interaction, and interaction design",
  "role": "Product Manager (Digital Platform)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "The Onboarding Wizard Decision at CollabHub (Ambiguous Control)",
    "scenario_summary_internal": "A PM at CollabHub, a mid-size B2B collaboration platform, investigates a 32% drop-off at the account-setup step of the signup funnel ahead of a Q3 board review. The incident mirrors the paired scenario's structure, actors, constraints, and four decision points, but decision point 2 is written so that the choice between building an AI-guided setup wizard and fixing a payment-field issue remains genuinely underdetermined: the PM weighs a small, unstable internal cohort signal against a strategic feature-parity consideration raised by Sales, and the record leaves multiple reasonable readings of the decision open without any evidence-weighting pattern that privileges adoption prevalence itself.",
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
        "irrational",
        "everyone is doing it"
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
          "Sales director reports that two active enterprise deals specifically asked about guided onboarding during demos",
          "Internal sample size for the affected cohort is small (approximately 140 users) and not yet statistically stable"
        ],
        "new_information_after_decision": [
          "Engineering estimates the wizard will take three sprints to build",
          "A follow-up analytics review (after the decision) shows the payment-field friction persists independent of the wizard concept"
        ],
        "alternatives": [
          "Build the AI-guided setup wizard raised in the deal conversations",
          "Run a targeted fix on the payment-field step identified in internal cohort data",
          "Run a small controlled A/B test comparing a wizard concept against a payment-field fix before committing engineering resources"
        ],
        "intended_action": "PM commits to building the wizard, citing a mix of the specific deal-related requests and reservations about the small internal sample, while leaving open whether the payment-field signal would have been prioritized under different sales circumstances."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Engineering lead confirms building the wizard requires reallocating two engineers from the bug-fix backlog for three sprints",
          "Backlog contains several unresolved defects reported by enterprise customers",
          "Sales director requests wizard prioritization to support two active deals"
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
        "At what point did the sales conversations enter your thinking?",
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
        "If the deal-related requests hadn't come up, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If you had two more weeks before the board review, what would you have done differently?",
        "If the payment-field signal had come from a larger sample, would that have changed your decision at that stage?",
        "Looking back, what would you tell a peer PM facing a similar mix of signals?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "IS_Biased_1",
      "features_to_match": [
        "Domain vocabulary (onboarding funnel, activation rate, cohort analysis, drop-off step, SSO, funnel instrumentation, canary release, sprint capacity, feature parity, heatmap analytics)",
        "Narrative structure and chronology (diagnosis, redesign-approach choice, staffing allocation, launch decision)",
        "Actor set (PM, VP of Product, Engineering lead, data analyst, UX researcher, Sales director, external peer PMs)",
        "Difficulty level (moderate) and emotional tone (time-pressured but professional)",
        "Exactly four decision points with at least two plausible alternatives each",
        "Consequences that remain inconclusive about whether decision point 2 was well-founded"
      ],
      "features_to_remove_or_change": [
        "Remove the explicit framing where adoption prevalence among competitors and peer PMs is cited as the primary justification for the wizard decision",
        "Replace the industry-Slack-group adoption-prevalence narrative with a concrete, deal-specific sales request as one of two co-equal considerations",
        "Ensure the internal cohort signal (payment-field friction) is acknowledged with comparable weight to the external consideration, so no single evidence source dominates the stated rationale"
      ],
      "ambiguity_boundary": "The decision at phase 2 must remain genuinely underdetermined: a reader should be able to interpret it either as a reasonable strategic bet motivated by specific, named deal risk, or as an instance of insufficient weight given to a small but concrete internal signal, without the interview supplying evidence that adoption prevalence, competitor volume, or peer conformity was the operative justification. No wording may state or imply that the wizard was chosen because 'others are doing it' or because of the sheer number of competitors/peers adopting the pattern; the PM's stated reasons must reference specific, individuated business facts (two named deals) rather than aggregate popularity."
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
      "Zero intentional Herding instances planned anywhere in the interview, including decision point 2",
      "Decision point 2 reasoning references two specific named deals rather than aggregate competitor/peer adoption volume, preserving ambiguity without instantiating the target bias",
      "No bias vocabulary appears in probe_plan or timeline text",
      "All four decision points retain at least two plausible alternatives and inconclusive consequences",
      "Structure, actor set, vocabulary, and difficulty match paired scenario IS_Biased_1",
      "Word count target 1,350 (range 1,215-1,485) achievable given 4 decision points with moderate probe depth and no embedded bias instance"
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
