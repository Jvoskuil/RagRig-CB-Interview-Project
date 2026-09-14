You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HE_Biased_3",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Fire Protection System Designer (Sprinkler/Suppression Design Engineer)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Rack Storage Retrofit: Commodity Classification and Density Trade-offs Under Deadline",
    "scenario_summary_internal": "A fire protection design engineer is retained to design an automatic sprinkler retrofit for a third-party logistics (3PL) distribution warehouse that is converting part of its floor plan to high-piled rack storage for a new client tenant. The engineer must classify the stored commodity, select a hydraulic design density/K-factor combination, respond to the building owner's cost-reduction pressure during value engineering, and decide how rigorously to verify installation compliance before sign-off. The project is compressed into a three-week design window because the tenant's lease and stocking schedule are fixed. The engineer has worked with similar 3PL operators before and has an ongoing multi-project relationship with this building owner.",
    "occupational_realism": {
      "objective": "Design a code-compliant automatic sprinkler system for a new high-piled combustible storage racking layout inside an existing distribution warehouse, within a compressed schedule and a fixed retrofit budget.",
      "setting": "Existing 140,000 sq ft tilt-up concrete distribution warehouse being subdivided for a new 3PL tenant storing palletized retail goods on double-row selective rack up to 32 feet; retrofit must be designed, permitted, and installed before the tenant's lease start date.",
      "constraints": [
        "Three-week design turnaround before permit submission deadline",
        "Fixed retrofit budget set by the building owner before final commodity classification was confirmed",
        "Limited access to the tenant's actual SKU list before design must be finalized",
        "Ongoing multi-project relationship between the engineer's firm and the building owner",
        "Existing water supply and riser infrastructure sized for a prior, lower-hazard occupancy",
        "Local AHJ requires hydraulic calculations and a witnessed flow test before occupancy"
      ],
      "stakeholders": [
        "Fire Protection Design Engineer (interviewee)",
        "Building owner / developer",
        "Incoming 3PL tenant operations manager",
        "Sprinkler installation contractor",
        "Local Authority Having Jurisdiction (AHJ) plan reviewer",
        "Engineer's firm principal"
      ],
      "technical_terms_to_use": [
        "commodity classification",
        "high-piled storage",
        "design density/area curve",
        "in-rack sprinklers (IRAS)",
        "ESFR (early suppression fast response)",
        "hydraulic calculation",
        "K-factor",
        "value engineering",
        "witnessed flow test",
        "AHJ plan review"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias",
        "stereotype",
        "incentive bias",
        "satisficing"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tenant is a 3PL company similar in profile to two prior clients the engineer has designed for",
          "No finalized SKU or packaging list from the incoming tenant yet",
          "Building owner wants classification finalized quickly to lock the budget"
        ],
        "new_information_after_decision": [
          "Partial tenant inventory list later shows a meaningful share of exposed unexpanded plastics mixed with cartoned goods, closer to Class IV/plastics than assumed"
        ],
        "alternatives": [
          "Classify commodity based on general similarity to prior 3PL tenants' storage profile",
          "Require a preliminary SKU/packaging sample list from the tenant before finalizing classification",
          "Classify conservatively as worst-case plastics until tenant data is confirmed"
        ],
        "intended_action": "Engineer classifies the commodity as Class III based on its resemblance to two previous 3PL clients he has designed for, without requesting tenant-specific packaging data."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "NFPA design density/area curves for the assumed Class III classification and 32-ft rack height",
          "Multiple density/area combinations satisfy code minimums, some requiring additional in-rack sprinklers",
          "Schedule pressure to finalize hydraulic calculations for permit submission"
        ],
        "new_information_after_decision": [
          "AHJ plan reviewer later flags that the chosen density/area point is at the marginal edge of the applicable curve given the actual rack configuration"
        ],
        "alternatives": [
          "Select the first density/area point on the curve that meets the minimum code requirement for the assumed classification",
          "Evaluate multiple density/area combinations against the specific rack configuration and aisle widths before selecting",
          "Consult the sprinkler manufacturer's design guide for a configuration-specific recommendation"
        ],
        "intended_action": "Engineer selects the first tabulated density/area combination that technically satisfies the code minimum for the assumed classification, without comparing it against alternate points better suited to the specific rack geometry, in order to keep the calculation package on schedule."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Building owner requests a value-engineering pass to bring the design under the fixed retrofit budget",
          "In-rack sprinkler upgrade would add cost but reduce sensitivity to commodity classification uncertainty",
          "Engineer's firm has two additional retrofit projects pending with this same building owner"
        ],
        "new_information_after_decision": [
          "Removing the in-rack sprinkler allowance leaves the design with less margin against the commodity classification uncertainty identified in Phase 1"
        ],
        "alternatives": [
          "Recommend retaining the in-rack sprinkler allowance despite the added cost, citing classification uncertainty",
          "Recommend removing the in-rack sprinkler allowance to meet the owner's budget target",
          "Present both options with risk trade-offs and let the owner decide with full information"
        ],
        "intended_action": "Engineer recommends removing the in-rack sprinkler allowance to meet the owner's budget target, favoring the option likely to keep the ongoing multi-project relationship with the owner smooth, without fully surfacing the classification uncertainty risk in the recommendation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Contractor's certification paperwork shows the system installed per approved drawings",
          "AHJ requires a witnessed flow test before final sign-off",
          "Schedule pressure remains high as tenant move-in date approaches"
        ],
        "new_information_after_decision": [
          "Flow test performed under time pressure passes but at a value close to the required minimum, prompting a note for future monitoring"
        ],
        "alternatives": [
          "Proceed with a full witnessed flow test as required before sign-off",
          "Accept contractor certification alone and expedite paperwork to save time",
          "Schedule a partial test covering only the modified risers"
        ],
        "intended_action": "Engineer proceeds with the full witnessed flow test as required, despite time pressure, and documents the result before sign-off."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this retrofit project was for and what your role was?",
        "What made this particular design assignment more difficult than a routine sprinkler retrofit?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through how the commodity classification decision came about.",
        "What happened after the density/area selection was submitted for plan review?",
        "How did the value-engineering conversation with the building owner unfold?",
        "What happened during commissioning and sign-off?"
      ],
      "decision_point_probes": [
        "At the point you classified the commodity, what specific information did you have about this tenant's actual inventory?",
        "What other classification approaches did you consider, and why did you rule them out?",
        "When you selected the density/area combination, what alternatives were on the table and how did you compare them?",
        "What was your basis for choosing that particular design point over the others available?",
        "When the owner asked for value engineering, what options did you consider and how did you weigh them?",
        "How did your relationship with the building owner factor into how you presented the options?",
        "At commissioning, what made you decide on the level of testing you pursued?"
      ],
      "cues": [
        "What specific cues told you the commodity classification was appropriate?",
        "What cues, if any, suggested you should get more tenant-specific data before finalizing the design?"
      ],
      "information_sources": [
        "What sources of information did you rely on most heavily at each stage?",
        "Was there information you didn't seek out that, in hindsight, might have been available?"
      ],
      "goals": [
        "What were you personally trying to achieve or protect at each of these points?",
        "Were there competing goals between the schedule, the budget, and code compliance?"
      ],
      "alternatives": [
        "What other courses of action did you seriously consider at each decision point?",
        "Why didn't you pursue those alternatives?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision one way over another?",
        "How confident were you in that decision at the time you made it?"
      ],
      "prior_experience": [
        "How did your experience with similar past projects or clients shape your approach here?"
      ],
      "time_pressure": [
        "How did the compressed schedule affect how much time you spent on each decision?"
      ],
      "uncertainty": [
        "What were you most uncertain about at each stage, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If you had had the tenant's full SKU list before classifying the commodity, would you have done anything differently?",
        "If there had been no ongoing relationship with the building owner, would the value-engineering conversation have gone differently?",
        "Looking back, is there a point where you'd make a different call given the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "st_01",
        "bias": "Stereotyping",
        "decision_point": 1,
        "mechanism": "Engineer categorizes the incoming tenant's storage hazard based on surface similarity to a category of past clients (\"3PL operators like this always store cartoned goods\") rather than verifying tenant-specific inventory characteristics.",
        "affected_reasoning_operation": "Category-based inference substituting for case-specific evidence gathering during commodity classification",
        "evidence_available_at_time": [
          "No finalized SKU/packaging list from the tenant",
          "General resemblance of tenant type to two prior 3PL clients",
          "Owner pressure to finalize classification quickly"
        ],
        "required_textual_manifestation": "Interviewee explicitly attributes the classification choice to the tenant fitting the general pattern of prior 3PL clients ('this type of tenant is usually...') rather than to tenant-specific data, and does not request or wait for confirming inventory data before finalizing.",
        "plausible_nonbias_interpretation": "Using base rates from experience with similar occupancies is a legitimate engineering heuristic when time-constrained; the account must show the classification was treated as settled rather than provisional despite available means to verify it.",
        "strength": "subtle",
        "do_not_make_explicit": ["stereotyping", "generalization", "category bias", "assumption based on client type"]
      },
      {
        "instance_id": "sf_01",
        "bias": "Satisficing",
        "decision_point": 2,
        "mechanism": "Engineer accepts the first density/area combination that clears the minimum code threshold for the assumed classification instead of evaluating configuration-specific alternatives that could better match the actual rack geometry.",
        "affected_reasoning_operation": "Premature termination of the alternative-generation and comparison process during hydraulic design selection",
        "evidence_available_at_time": [
          "Multiple density/area curve points available for the assumed classification",
          "Rack height and aisle configuration data on hand",
          "Schedule pressure to submit hydraulic calculations for permit"
        ],
        "required_textual_manifestation": "Interviewee describes stopping at the first design point that 'met the minimum' without describing a comparison against other viable points or manufacturer guidance, framing the choice as sufficient rather than optimal, given the deadline.",
        "plausible_nonbias_interpretation": "Selecting a code-compliant minimum is a valid, common engineering practice under time constraints; the account must show the stopping point was driven by adequacy-seeking rather than a reasoned comparison against configuration-specific alternatives that were accessible.",
        "strength": "subtle",
        "do_not_make_explicit": ["satisficing", "settling", "good enough", "minimum viable"]
      },
      {
        "instance_id": "ib_01",
        "bias": "Incentive bias",
        "decision_point": 3,
        "mechanism": "Engineer's recommendation on removing the in-rack sprinkler allowance is shaped by the desire to preserve a smooth, ongoing multi-project relationship with the building owner, rather than by a neutral weighing of the classification-uncertainty risk this removal introduces.",
        "affected_reasoning_operation": "Selective emphasis and information-presentation during a risk-tradeoff recommendation to a client on whom future business depends",
        "evidence_available_at_time": [
          "Owner's budget constraint and request for value engineering",
          "Known classification uncertainty from Phase 1 not yet resolved",
          "Two additional pending projects with the same building owner"
        ],
        "required_textual_manifestation": "Interviewee acknowledges factoring in the ongoing relationship with the owner when deciding how to present the in-rack sprinkler trade-off, and describes downplaying or not fully surfacing the classification-uncertainty risk in the recommendation given to the owner.",
        "plausible_nonbias_interpretation": "Cost-conscious value engineering is a routine and legitimate part of design practice; the account must show the recommendation was tilted by the engineer's stake in the client relationship rather than purely by a neutral risk assessment.",
        "strength": "moderate",
        "do_not_make_explicit": ["incentive bias", "conflict of interest", "self-interest", "relationship preservation"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition scenario with no paired control specified in this request."
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
      "Confirm exactly 4 decision points appear in the timeline, with Decision Point 4 free of intentionally embedded named-bias instances.",
      "Confirm exactly one Stereotyping instance is embedded at Decision Point 1 only.",
      "Confirm exactly one Satisficing instance is embedded at Decision Point 2 only.",
      "Confirm exactly one Incentive bias instance is embedded at Decision Point 3 only.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm each decision point includes at least two plausible alternatives and both pre- and post-decision information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given the four decision points and probe density without repetitive exposition.",
      "Confirm consequences described (marginal flow test result, plan reviewer flag, unresolved classification uncertainty) do not mechanically prove any decision was biased."
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
