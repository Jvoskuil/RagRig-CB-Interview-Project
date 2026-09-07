You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IS_Biased_6",
  "domain_id": "IS",
  "domain": "Information Systems, Human-Computer Interaction, and Interaction Design",
  "role": "Software Architect",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Portal Modernization: Anchors, Trends, and Sunk Costs",
    "scenario_summary_internal": "A software architect leads a six-month modernization of a customer-facing enterprise portal, covering both interaction-design overhaul and backend re-architecture from monolith toward microservices. The interview reconstructs four chronological decision points: an early vendor cost/timeline estimate that anchors later planning, a usability-test review during which the architect selectively weighs feedback on a navigation pattern he championed, a joint moment where industry-trend adoption and a single dramatic incident distort both the architecture-pattern choice and the beta-result assessment, and a late-stage moment where sunk investment drives continued commitment while a security-mandated authentication change triggers resistance rooted in the fact of being told what to do rather than the substance of the mandate.",
    "occupational_realism": {
      "objective": "Deliver a modernized, scalable, and usable customer portal (new interaction model + re-architected backend) within a fixed 6-month window and budget envelope.",
      "setting": "Mid-size financial-services company modernizing its customer self-service portal; cross-functional team including UX researchers, backend engineers, a security/compliance team, and an external vendor.",
      "constraints": [
        "Fixed 6-month delivery deadline tied to a regulatory reporting change",
        "Capped budget approved by finance based on an early estimate",
        "Legacy monolith with tight coupling to a core banking system",
        "Limited usability-testing sample size and time window",
        "Security team has independent authority to mandate authentication architecture",
        "Executive visibility after a public demo incident"
      ],
      "stakeholders": [
        "Software Architect (interviewee)",
        "External framework/migration vendor",
        "UX research lead",
        "Backend engineering team",
        "Security and compliance team",
        "Executive sponsor",
        "Beta customer cohort"
      ],
      "technical_terms_to_use": [
        "microservices decomposition",
        "monolith refactor",
        "navigation model",
        "usability testing",
        "authentication architecture",
        "service-level rollout",
        "beta cohort",
        "technical debt",
        "API gateway",
        "interaction pattern"
      ],
      "technical_terms_to_avoid": [
        "anchoring bias",
        "confirmation bias",
        "herding",
        "irrational escalation",
        "negativity bias",
        "reactance",
        "cognitive bias",
        "heuristic error"
      ],
      "constraints_note": "No named-bias vocabulary or psychological framing may appear in the public interview; only behavior and reasoning traces."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor scoping call produces a rough order-of-magnitude quote and timeline for the front-end migration",
          "No detailed technical estimate yet exists from the internal team",
          "Finance requests a budget number within one week"
        ],
        "new_information_after_decision": [
          "Internal engineering later produces a detailed estimate roughly 40% higher than the vendor's ballpark",
          "Some scope items were not covered in the original quote"
        ],
        "alternatives": [
          "Submit the vendor's ballpark number as the working budget baseline",
          "Wait two more weeks for a detailed internal estimate before submitting any budget number",
          "Submit a range with explicit uncertainty caveats instead of a point estimate"
        ],
        "intended_action": "Architect submits the vendor's ballpark figure as the working baseline and anchors subsequent budget conversations to it."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Usability test with 10 beta users on the new navigation model the architect designed",
          "6 of 10 users report confusion navigating between the new dashboard and account sections",
          "4 of 10 users complete tasks quickly and give positive comments",
          "UX researcher's written summary flags the navigation confusion as the top issue"
        ],
        "new_information_after_decision": [
          "A follow-up round with a different cohort shows the confusion issue persists at similar rates",
          "The architect's presentation to stakeholders emphasizes the positive comments and task-completion speed"
        ],
        "alternatives": [
          "Treat the navigation confusion as the primary finding requiring redesign",
          "Present a balanced summary weighting both confused and successful users equally",
          "Highlight the positive results and characterize the confusion as user-training gaps"
        ],
        "intended_action": "Architect frames the mixed results around the positive comments, seeks out additional favorable quotes from the transcripts, and characterizes the confusion reports as isolated onboarding issues."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Team debate: monolith refactor (lower risk, slower scalability gains) vs. microservices decomposition (higher risk, matches recent conference case studies from three peer financial firms)",
          "Beta rollout metrics: 92% of transactions complete successfully across the pilot week",
          "One beta session ends in a visible crash during a live demo in front of the executive sponsor",
          "Backend team's internal risk memo notes migration risk is 'moderate, manageable with phased rollout'"
        ],
        "new_information_after_decision": [
          "Two additional peer-company case studies later reveal significant post-migration incident rates not mentioned in the original talks",
          "A deeper log review shows the demo crash stemmed from a one-off test-environment misconfiguration, not the underlying architecture"
        ],
        "alternatives": [
          "Choose microservices decomposition citing industry adoption and proceed",
          "Choose the monolith refactor path as lower risk given the existing coupling",
          "Request a structured risk/benefit comparison before committing"
        ],
        "intended_action": "Architect recommends microservices decomposition partly because peer firms are adopting it, and separately treats the single demo crash as decisive evidence of fragility, overriding the 92% success metric in the internal risk framing presented to the executive sponsor."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Four months into the microservices migration, integration bugs have delayed two of five planned service cutovers",
          "A third-party monitoring report shows rising latency and two customer-facing outages tied to the new service mesh",
          "Security team formally mandates switching the authentication architecture to a centralized identity provider, citing a compliance finding",
          "Remaining budget and timeline are tight; abandoning the migration would require reverting several already-cutover services"
        ],
        "new_information_after_decision": [
          "A post-mortem later shows the compliance finding was valid and unrelated to the architect's preferred authentication approach",
          "Continuing the migration without adjustment leads to a further slipped cutover date"
        ],
        "alternatives": [
          "Continue the current migration plan and authentication approach as originally scoped, pushing timeline",
          "Pause and reassess the microservices migration given the accumulating negative signals",
          "Adopt the security team's mandated identity-provider architecture as specified",
          "Propose an alternative authentication design that meets the compliance finding differently, mainly to avoid simply complying"
        ],
        "intended_action": "Architect commits further resources to complete the migration as planned despite the negative signals, and separately pushes back on the security mandate by proposing an alternative primarily because the change was imposed rather than because of a substantive technical objection."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe the portal modernization project and your role in it.",
        "What was the original objective and timeline when the project started?"
      ],
      "timeline_reconstruction": [
        "Walk me through how the budget number was first established.",
        "What happened during the usability testing round?",
        "How was the decision between monolith refactor and microservices decomposition made?",
        "What happened after the security team's mandate arrived?"
      ],
      "decision_point_probes": [
        "What information did you have available at the moment you set the budget baseline?",
        "What made you weight some usability comments more than others?",
        "What role did other companies' architecture choices play in your recommendation?",
        "How did the demo crash affect your read of the beta metrics compared to the success rate?",
        "What made you decide to keep investing in the migration despite the delays?",
        "What was your first reaction to the security team's mandate, and why?"
      ],
      "cues_and_sources": [
        "What sources of information did you rely on most at each stage?",
        "Were there sources you discounted or didn't revisit?"
      ],
      "goals_and_alternatives": [
        "What alternatives did you consider at each decision point and why did you rule them out?",
        "Did competing goals (budget, timeline, usability, compliance) ever conflict?"
      ],
      "prior_experience": [
        "Had you handled a similar migration or usability tradeoff before?",
        "Did past projects influence how you read the peer-company case studies?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure did you feel at each stage?",
        "How confident were you in the numbers and metrics at the time versus later?"
      ],
      "closing_hypotheticals": [
        "If the vendor's early quote had never been mentioned, would the budget conversation have gone differently?",
        "If the demo crash hadn't happened in front of the executive sponsor, would your risk framing have changed?",
        "If the security mandate had come as a suggestion instead of a directive, would your response have differed?",
        "Looking back, what would you do differently at each of these four moments?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "anch_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Vendor's early ballpark quote/timeline, offered before detailed technical scoping existed, is adopted as the working budget baseline and subsequent conversations are framed relative to it rather than to the later, more accurate internal estimate.",
        "affected_reasoning_operation": "Numeric/quantitative estimation and budget-baseline setting",
        "evidence_available_at_time": [
          "Vendor's rough order-of-magnitude quote and timeline",
          "Finance's one-week deadline for a budget number",
          "Absence of a detailed internal estimate"
        ],
        "required_textual_manifestation": "Architect explicitly reports submitting the vendor figure as the baseline and later describes the 40%-higher internal estimate as an overrun relative to that baseline rather than as the more accurate number.",
        "plausible_nonbias_interpretation": "Under a hard one-week deadline, using the only available number is a reasonable stopgap heuristic rather than a cognitive distortion.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "first number bias"]
      },
      {
        "instance_id": "conf_01",
        "bias": "Confirmation Bias",
        "decision_point": 2,
        "mechanism": "Given mixed usability-test results (6/10 negative, 4/10 positive), the architect selectively revisits transcripts to surface additional favorable quotes and reframes the majority negative finding as an onboarding gap rather than a design flaw, without applying the same scrutiny to the positive comments.",
        "affected_reasoning_operation": "Evidence weighting and selective evidence retrieval during synthesis of mixed data",
        "evidence_available_at_time": [
          "Usability test transcripts with a majority reporting navigation confusion",
          "UX researcher's written summary naming navigation confusion as the top issue",
          "A minority of positive task-completion comments"
        ],
        "required_textual_manifestation": "Architect describes going back to find more positive quotes and characterizing the majority negative finding as isolated or training-related, without describing equivalent scrutiny applied to the positive minority.",
        "plausible_nonbias_interpretation": "Distinguishing genuine design flaws from onboarding gaps is a legitimate diagnostic judgment a senior architect might reasonably make.",
        "strength": "moderate",
        "do_not_make_explicit": ["confirmation", "cherry-picking", "selective evidence"]
      },
      {
        "instance_id": "herd_01",
        "bias": "Herding",
        "decision_point": 3,
        "mechanism": "The recommendation for microservices decomposition is partly justified by reference to peer-company conference case studies and industry adoption trends, independent of the internal risk memo's own moderate-risk assessment.",
        "affected_reasoning_operation": "Option evaluation and justification of a technical architecture choice",
        "evidence_available_at_time": [
          "Three peer-firm conference case studies on microservices adoption",
          "Internal backend team's risk memo characterizing risk as moderate and phasing-manageable",
          "Existing monolith coupling constraints"
        ],
        "required_textual_manifestation": "Architect names peer-company adoption as a factor in the recommendation, distinct from and in addition to the internal technical risk assessment.",
        "plausible_nonbias_interpretation": "Learning from peers who have solved similar coupling problems is a legitimate form of technology due diligence.",
        "strength": "subtle",
        "do_not_make_explicit": ["herding", "bandwagon", "social proof"]
      },
      {
        "instance_id": "neg_01",
        "bias": "Negativity Bias",
        "decision_point": 3,
        "mechanism": "A single visible demo crash in front of the executive sponsor is treated as decisive evidence of architectural fragility, overriding the 92% pilot-week success rate in the risk framing presented upward.",
        "affected_reasoning_operation": "Aggregation and weighting of outcome evidence when forming a risk narrative",
        "evidence_available_at_time": [
          "92% successful transaction rate across the pilot week",
          "One demo crash witnessed by the executive sponsor",
          "No log analysis yet available on the crash's cause"
        ],
        "required_textual_manifestation": "Architect's account of the risk framing gives the single crash outsized narrative weight relative to the aggregate success rate when describing what shaped the executive-facing risk assessment.",
        "plausible_nonbias_interpretation": "A visible failure in front of leadership is legitimately more consequential politically and reputationally, independent of its statistical frequency.",
        "strength": "moderate",
        "do_not_make_explicit": ["negativity bias", "overweighting negative", "salience"]
      },
      {
        "instance_id": "esc_01",
        "bias": "Irrational Escalation",
        "decision_point": 4,
        "mechanism": "Despite delayed cutovers, rising latency, and two customer-facing outages, the architect commits further resources to complete the migration as originally scoped, citing the sunk work of already-cutover services rather than a forward-looking reassessment of remaining costs and benefits.",
        "affected_reasoning_operation": "Continuation/commitment decision under negative feedback",
        "evidence_available_at_time": [
          "Two of five planned cutovers delayed",
          "Third-party monitoring report showing rising latency and two outages",
          "Already-cutover services that would require reversion if the plan changed"
        ],
        "required_textual_manifestation": "Architect explicitly reasons that reverting the already-migrated services would waste the completed work, and uses that as a stated reason to continue rather than independently reassessing remaining risk and benefit.",
        "plausible_nonbias_interpretation": "Reversion costs are a legitimate switching-cost consideration in any staged migration decision.",
        "strength": "moderate",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment", "irrational escalation"]
      },
      {
        "instance_id": "react_01",
        "bias": "Reactance",
        "decision_point": 4,
        "mechanism": "Upon receiving the security team's mandate to adopt a centralized identity provider, the architect's stated primary objection centers on the fact that the change was imposed as a directive, and an alternative design is proposed mainly to preserve autonomy rather than from a distinct technical concern with the mandated approach.",
        "affected_reasoning_operation": "Response to an externally imposed constraint on a prior decision",
        "evidence_available_at_time": [
          "Security team's formal mandate citing a compliance finding",
          "Architect's prior authentication design already partially implemented",
          "No technical evaluation yet performed comparing the two approaches"
        ],
        "required_textual_manifestation": "Architect's account of the reaction foregrounds being told what to do as the trigger for pushback, with the alternative proposal framed as a way to retain control over the design rather than as a response to a specific technical shortcoming of the mandated approach.",
        "plausible_nonbias_interpretation": "Architects reasonably scrutinize externally imposed mandates for unintended technical side effects before complying.",
        "strength": "subtle",
        "do_not_make_explicit": ["reactance", "psychological reactance", "resistance to control"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control scenario supplied."
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
      "Exactly 4 decision points present, each with at least two plausible alternatives.",
      "Exactly 6 bias instances planned, one per manifest entry, matching requested counts exactly.",
      "No decision point contains two instances of the same bias.",
      "Decision points 3 and 4 each host two distinct biases, with distinct evidence sources and reasoning operations documented per instance.",
      "No bias vocabulary, labels, or psychological explanations appear in probe_plan or timeline text intended for the public interview.",
      "Target word count 1,350 (acceptable range 1,215-1,485) achievable given 4 decision points with moderate probe depth and no repetitive exposition.",
      "Each occurrence has a plausible non-bias interpretation to prevent mechanical proof of bias from outcomes alone."
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
