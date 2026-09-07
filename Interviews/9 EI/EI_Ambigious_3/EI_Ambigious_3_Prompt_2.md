You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EI_Ambigious_3",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "Special Education Caseworker / IEP Coordinator",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Interim Placement for a Mid-Year IEP Transfer (Ambiguous Control)",
    "scenario_summary_internal": "An IEP Coordinator processes a mid-year transfer student arriving from an out-of-district specialized program, completing an interim placement within a 10-school-day compliance window. The reasoning at each decision point is genuinely underdetermined: caution, deferral, and cautious wording are each supported by plausible non-bias justifications (individualized documentation, fixed scheduling constraints, safety-relevant uncertainty) rather than by group-based generalization, short-term discounting, or disproportionate negative colorization. No named bias is intentionally instantiated.",
    "occupational_realism": {
      "objective": "Determine a compliant interim IEP placement, present levels of performance, and service minutes for a transferring student within the statutory timeline, using the best available evidence.",
      "setting": "Public elementary school special education department, mid-year transfer, 10-school-day interim placement mandate",
      "constraints": [
        "10-school-day statutory deadline for interim placement determination",
        "Caseload of 42 active IEP students",
        "School psychologist has a 3-week testing backlog",
        "Incomplete transfer records arriving in stages from sending program",
        "Parent expects a placement decision at the interim meeting",
        "Principal wants minimal disruption to general education scheduling"
      ],
      "stakeholders": [
        "IEP Coordinator (interviewee)",
        "General education classroom teacher",
        "Instructional paraprofessional",
        "School psychologist",
        "Parent/guardian",
        "Sending program liaison",
        "Building principal"
      ],
      "technical_terms_to_use": [
        "interim placement",
        "present levels of performance (PLOP)",
        "functional behavior assessment (FBA)",
        "behavior intervention plan (BIP)",
        "least restrictive environment (LRE)",
        "service minutes",
        "related services",
        "eligibility category",
        "compliance timeline",
        "reevaluation"
      ],
      "technical_terms_to_avoid": [
        "group attribution error",
        "present bias",
        "horn effect",
        "halo effect",
        "stereotype",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Transfer summary sheet identifies sending program as a specialized placement for students with significant emotional/behavioral disabilities",
          "The student's own prior IEP excerpt documents an individualized FBA/BIP written 18 months ago for aggression",
          "Full cumulative file has not yet arrived from the sending program",
          "Coordinator has handled several prior transfers, some from this program and some from others, with mixed outcomes"
        ],
        "new_information_after_decision": [
          "Full records arrive later showing the BIP was successfully faded out and the student had 9 incident-free months before transfer"
        ],
        "alternatives": [
          "Flag the case for additional behavioral observation before finalizing an inclusion-heavy interim schedule, citing the student's own documented history",
          "Proceed directly toward a full-inclusion interim schedule and revisit supports only if new concerns emerge"
        ],
        "intended_action": "Coordinator recommends building in a short observation period before finalizing the interim schedule, citing the student's own prior FBA/BIP documentation; it remains genuinely unclear from the record whether this caution is anchored to the individual student's own file or is generally influenced by the reputation of the sending program, since both were part of the same intake conversation."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Existing cognitive/academic testing is over 2 years old and due for reevaluation",
          "School psychologist's earliest testing slot is 3 weeks out",
          "Interim placement decision is due in 10 school days",
          "Caseload workload is already at capacity"
        ],
        "new_information_after_decision": [
          "Weeks later, the classroom teacher reports some accommodations need adjustment; a scheduled check-in already anticipated this possibility"
        ],
        "alternatives": [
          "Request an expedited or partial testing slot and build a short bridge plan with a defined near-term follow-up",
          "Use existing data for the interim IEP and schedule a specific, dated check-in shortly after the meeting to reassess accommodations"
        ],
        "intended_action": "Coordinator uses existing testing data for the interim IEP but schedules a concrete, dated follow-up review within a few weeks; it is genuinely ambiguous whether the choice reflects a considered judgment that the psychologist's backlog made expedited testing infeasible, or a general tendency to prefer the more immediately available option, since both interpretations fit the visible facts equally well."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Paraprofessional reports one specific outburst during a classroom transition",
          "Two separate teacher check-ins describe consistently positive peer interactions",
          "Work samples show reading performance above grade level",
          "Coordinator has only briefly observed the classroom in person"
        ],
        "new_information_after_decision": [
          "Additional peer and teacher feedback collected afterward continues to show strong academic engagement, roughly consistent with the balanced present-levels description"
        ],
        "alternatives": [
          "Write present levels giving comparable weight to the transition incident, the positive peer reports, and the academic work samples",
          "Emphasize the transition incident more heavily than the other three data points when describing overall functioning"
        ],
        "intended_action": "Coordinator drafts present levels that mention the transition incident alongside the academic and social strengths, using cautious language about transitions specifically without extending that caution into blanket statements about academic or social functioning; whether the resulting tone still reads as slightly more guarded than the underlying data strictly requires remains genuinely open to interpretation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "All records, testing history, and observation notes collected to date",
          "Parent is present and expects a service-minutes decision at the interim meeting",
          "Principal has flagged general-education scheduling constraints"
        ],
        "new_information_after_decision": [
          "Parent requests a follow-up review in 6 weeks to confirm the service minutes are adequate"
        ],
        "alternatives": [
          "Propose full inclusion with consultative behavior support",
          "Propose partial pull-out for targeted skill instruction"
        ],
        "intended_action": "Coordinator finalizes service minutes and LRE recommendation using a documented rationale drawn from the assembled record; this decision point is intentionally left evidence-balanced and is not a site of any intended ambiguity manipulation beyond ordinary domain judgment."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and caseload at the time of this case?",
        "What was the operational goal for this student's interim placement?"
      ],
      "timeline_reconstruction": [
        "Walk me through what happened, in order, from the transfer notice to the interim meeting.",
        "What information did you have at each stage, and what arrived later?"
      ],
      "decision_point_probes": [
        "What cues stood out to you at this point in the case?",
        "What information sources did you rely on, and which were unavailable?",
        "What were you trying to accomplish with this particular decision?",
        "What alternatives did you consider, and why did you choose the one you did?",
        "What was the basis for that decision?",
        "Had you handled a similar situation before, and did that shape your approach?",
        "How much time pressure were you under at this point?",
        "How confident were you in the information you had?",
        "If a key fact had been different, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If the student had transferred from a different, less specialized program, would your approach have been the same?",
        "If the psychologist had immediate testing availability, would you have made the same choice about reassessment?",
        "If the paraprofessional's report hadn't come in, how might the present levels have read differently?",
        "If the compliance timeline had been longer, what would you have done differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "EI_Biased_3",
      "features_to_match": [
        "Same domain vocabulary (interim placement, PLOP, FBA/BIP, LRE, service minutes, compliance timeline, reevaluation)",
        "Same stakeholders and staging (parent, teacher, paraprofessional, psychologist, principal, sending program liaison)",
        "Same four-decision-point structure and narrative sequence (records/history review, reassessment scheduling, incident interpretation, final placement)",
        "Same constraints (10-day timeline, 42-student caseload, 3-week psychologist backlog)",
        "Same target word count and difficulty level",
        "Same emotional tone: professional, time-pressured, cautious"
      ],
      "features_to_remove_or_change": [
        "Remove framing that ties the interim lean to the sending program's general population rather than the student's own documented file",
        "Remove explicit acknowledgment that a future cost is being knowingly discounted in favor of an easier immediate option",
        "Remove disproportionate extension of a single negative incident into unrelated academic/social characterizations",
        "Add a concrete, dated follow-up mechanism at decision point 2 to keep the deferral defensible rather than clearly discount-driven",
        "Balance the present-levels narrative at decision point 3 so cautious language is scoped to the transition context rather than generalized"
      ],
      "ambiguity_boundary": "Each of the first three decision points must remain genuinely undecidable between a bias-consistent reading and a legitimate, individualized, resource-constrained reading: (1) the observation-period recommendation is grounded in the student's own FBA/BIP record, but the intake conversation also surfaces program reputation, so the causal driver of caution is not textually resolvable; (2) the reassessment deferral is paired with a concrete dated check-in, making it consistent with reasonable compliance-driven sequencing rather than clearly short-term discounting; (3) the present-levels caution is explicitly scoped to transitions rather than generalized, but a reader could still perceive a mild tonal shift, keeping the degree of generalization ambiguous rather than absent or blatant. No sentence may contain a clean, unambiguous tell that isolates a single causal mechanism as the sole explanation."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable in ambiguous_control condition (no counterfactual requested)",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly 4 decision points present, matching the paired biased scenario's structure",
      "No named bias is intentionally instantiated at any decision point",
      "Each of decision points 1-3 supports at least two plausible readings (individualized/legitimate vs. group- or discount- or generalization-consistent) without resolving which applies",
      "Decision point 4 remains a balanced, evidence-driven judgment with no ambiguity manipulation",
      "No bias labels, definitions, or explanations appear in probes or narrative",
      "Vocabulary, stakeholders, constraints, and word count match the paired biased scenario EI_Biased_3",
      "Target word count 1,350 (range 1,215-1,485) achievable given 4 decision points, probe plan, and ambiguity design without repetitive exposition"
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
