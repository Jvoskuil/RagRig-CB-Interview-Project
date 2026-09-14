You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "CS_Biased_1",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Security Architect",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Segmentation Framework Decision",
    "scenario_summary_internal": "A Security Architect at a mid-size fintech must remediate findings from an external penetration test that flags weaknesses in a Zero Trust micro-segmentation framework the architect personally designed and built three years earlier. A vendor-managed ZTNA/SASE platform is available as an alternative remediation path. Across four decision points (triage of findings, remediation option selection, rollout/testing approach, and escalation/reporting to leadership), the architect must weigh the in-house framework's continued viability against a comparably capable vendor alternative, under time pressure from a compliance deadline. At decision point 2, the architect exhibits endowment bias: overvaluing the self-built framework relative to its objective remediation cost and risk profile, and demanding a higher burden of proof from the vendor alternative than from the incumbent system.",
    "occupational_realism": {
      "objective": "Remediate a critical pentest finding regarding lateral-movement exposure in the network segmentation layer before a regulatory compliance deadline, while minimizing operational disruption and preserving the integrity of the broader Zero Trust program.",
      "setting": "Mid-size fintech company, internal security architecture team, six weeks before an annual SOC 2 / regulatory audit window, following a third-party penetration test.",
      "constraints": [
        "Compliance deadline in six weeks",
        "Limited engineering headcount available for remediation work",
        "Vendor procurement and security review adds lead time",
        "Existing framework is deeply integrated with internal CI/CD and identity systems",
        "Budget approval required for any new vendor spend",
        "Leadership expects a remediation plan, not just a diagnosis"
      ],
      "stakeholders": [
        "Security Architect (interviewee)",
        "CISO",
        "Penetration testing vendor",
        "Platform engineering lead",
        "Compliance/audit manager",
        "ZTNA vendor sales engineer"
      ],
      "technical_terms_to_use": [
        "micro-segmentation",
        "lateral movement",
        "Zero Trust Network Access (ZTNA)",
        "policy enforcement point",
        "identity-aware proxy",
        "attack surface",
        "compensating control",
        "remediation SLA"
      ],
      "technical_terms_to_avoid": [
        "endowment effect",
        "cognitive bias",
        "sunk cost",
        "loss aversion",
        "ownership bias"
      ],
      "excluded_themes": "NONE"
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pentest report lists three findings: segmentation gap, stale service-account credentials, incomplete log retention",
          "Only one finding is marked 'critical severity'",
          "Compliance deadline is six weeks out"
        ],
        "new_information_after_decision": [
          "Deeper triage reveals the segmentation gap allows lateral movement between two previously 'isolated' trust zones",
          "Platform engineering confirms limited bandwidth to fix all three findings in parallel"
        ],
        "alternatives": [
          "Prioritize the segmentation finding first as highest business risk",
          "Prioritize credential rotation first as fastest to close",
          "Run all three remediations in parallel with reduced depth on each"
        ],
        "intended_action": "Architect selects the segmentation finding as top priority based on severity and lateral-movement risk."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "In-house segmentation framework was designed and implemented by the architect three years prior",
          "A vendor ZTNA/SASE platform is available that independent benchmarks and the pentest vendor suggest would close the same gap with less custom engineering",
          "Fixing the in-house framework requires an estimated four weeks of engineering effort with residual uncertainty about coverage",
          "Vendor platform requires a security review and migration plan estimated at three weeks, with vendor-provided coverage guarantees"
        ],
        "new_information_after_decision": [
          "The chosen remediation path is presented to the CISO as the recommended fix",
          "Platform engineering raises concerns about integration effort that were not fully weighted in the original comparison"
        ],
        "alternatives": [
          "Patch and extend the in-house framework to close the gap",
          "Migrate the affected segment to the vendor ZTNA platform",
          "Deploy a temporary compensating control while evaluating both options further"
        ],
        "intended_action": "Architect chooses to patch and extend the in-house framework, citing familiarity and control, while applying a stricter evidentiary standard to the vendor option than to the in-house one. [ENDOWMENT BIAS INSTANCE cb_01]"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patched framework is ready for testing",
          "Two testing approaches are available: narrow pilot on one trust zone, or full rollout across all affected zones",
          "Compliance deadline is now four weeks away"
        ],
        "new_information_after_decision": [
          "Pilot or rollout surfaces an edge case where a legacy service bypasses the new policy enforcement point",
          "Platform engineering flags additional remediation time needed"
        ],
        "alternatives": [
          "Run a narrow pilot first, then expand if successful",
          "Roll out to all affected zones simultaneously to save time",
          "Stage rollout by risk tier over two weeks"
        ],
        "intended_action": "Architect selects a staged rollout by risk tier to balance validation confidence against the compressed timeline."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Staged rollout has closed the original lateral-movement path but the legacy-service edge case remains partially unresolved",
          "Compliance deadline is two weeks away",
          "CISO needs a status report for the audit committee"
        ],
        "new_information_after_decision": [
          "Audit committee accepts the report with a follow-up remediation item",
          "The unresolved edge case is scheduled for a subsequent sprint"
        ],
        "alternatives": [
          "Report the finding as fully remediated",
          "Report as substantially remediated with a documented compensating control and follow-up date",
          "Request a deadline extension pending full closure"
        ],
        "intended_action": "Architect reports the finding as substantially remediated with a documented compensating control and a committed follow-up date."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what triggered this incident and what your role was.",
        "What was your overall objective when you first reviewed the pentest report?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did the segmentation finding become the focus?",
        "What information did you have at each stage, and what changed afterward?"
      ],
      "decision_point_probes": [
        "What cues or evidence stood out to you when triaging the three findings?",
        "What information sources did you consult when comparing the in-house framework to the vendor platform?",
        "What alternatives did you consider at that point, and why did you rule the others out?",
        "What was the basis for your decision to extend the in-house framework rather than migrate?",
        "Had you evaluated vendor ZTNA platforms before? How did that prior experience factor in?",
        "How much time pressure did you feel at each stage, and how did that affect your evaluation?",
        "How confident were you in the coverage estimate for each remediation option?",
        "During the rollout decision, what made you choose a staged approach over a full rollout?",
        "When reporting to the audit committee, what led you to characterize the finding as 'substantially remediated'?"
      ],
      "closing_hypotheticals": [
        "If a different engineer had originally built the segmentation framework, do you think the remediation choice would have unfolded differently?",
        "If the vendor platform had been proposed as a replacement for someone else's system rather than your own, would your evaluation criteria have changed?",
        "Looking back, what would you do differently if you faced this same choice again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Endowment",
        "decision_point": 2,
        "mechanism": "The architect assigns disproportionately higher value to the in-house segmentation framework because they personally designed and built it, applying a stricter evidentiary bar to the vendor alternative than to the incumbent system despite comparable or superior objective indicators for the vendor option.",
        "affected_reasoning_operation": "Comparative evaluation and weighting of two remediation alternatives (in-house patch vs. vendor migration)",
        "evidence_available_at_time": [
          "Independent benchmarks and pentest vendor commentary favoring the vendor ZTNA platform's coverage guarantees",
          "Estimated engineering effort: 4 weeks (in-house) vs. 3 weeks (vendor) with vendor-provided coverage guarantees",
          "Architect's personal authorship of the in-house framework three years prior"
        ],
        "required_textual_manifestation": "The architect explicitly favors extending their own framework, citing 'knowing exactly how it works' and control over the code, while describing the vendor option's guarantees as unproven or requiring more validation than the self-built system received, without citing a comparable objective risk analysis for the in-house option.",
        "plausible_nonbias_interpretation": "Familiarity with an internally maintained system can legitimately reduce integration risk and operational uncertainty, which is a defensible engineering rationale independent of authorship attachment.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "endowment effect",
          "bias",
          "ownership attachment",
          "sunk cost"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": "Authorship of the incumbent segmentation framework (self-built vs. built by a different, now-departed engineer)",
      "original_state": "Architect personally designed and built the in-house segmentation framework being evaluated for remediation.",
      "counterfactual_state": "The in-house segmentation framework was originally built by a different, now-departed engineer, and the interviewee is only its current maintainer.",
      "variables_to_hold_constant": [
        "Pentest findings and severity ratings",
        "Compliance deadline and timeline pressure",
        "Vendor platform capabilities and cost estimates",
        "Staffing and engineering bandwidth constraints",
        "Rollout and reporting decisions at phases 1, 3, and 4"
      ],
      "expected_causal_difference": "Without personal authorship, the architect is expected to apply a symmetric evidentiary standard to both remediation options, reducing or eliminating the endowment-driven preference for the in-house framework observed at decision point 2.",
      "causal_test_question": "Does removing personal authorship of the incumbent system change the relative weighting applied to the in-house vs. vendor remediation options at decision point 2?"
    },
    "generation_checks": [
      "Exactly one endowment bias instance planned, matching manifest occurrences=1",
      "Endowment instance assigned to decision point 2 only, per automatic allocation since no allowed_decision_points was specified",
      "No bias labels, definitions, or psychological terms appear in probe_plan or timeline text intended for the public interview",
      "Four decision points defined, each with at least two alternatives",
      "Consequences at each decision point are ambiguous as to whether the decision was correct, avoiding mechanical proof of bias",
      "Target word count 1,350 (acceptable range 1,215-1,485) achievable given four decision points with proportionate probe depth",
      "No unrequested bias types intentionally embedded in any phase"
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
