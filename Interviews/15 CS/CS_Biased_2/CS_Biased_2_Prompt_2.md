You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "CS_Biased_2",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Security Product/Vendor Evaluation Manager",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "EDR Replacement Evaluation After a Near-Miss Ransomware Incident",
    "scenario_summary_internal": "A Security Product/Vendor Evaluation Manager at a mid-sized financial services firm must select a replacement Endpoint Detection and Response (EDR) platform within a 90-day contract-expiry window, following a near-miss ransomware incident that exposed detection gaps in the incumbent tool. The manager scopes a vendor shortlist, defines POC evaluation methodology, negotiates a licensing tier under budget pressure using vendor-supplied loss-avoidance figures, and makes a final go/no-go rollout recommendation to the board. Two decision points carry intentionally embedded biases (limited-alternative exposure during shortlisting; loss framing during tier negotiation); the other two decision points are handled through ordinary, defensible domain judgment.",
    "occupational_realism": {
      "objective": "Select and contract a replacement EDR/XDR platform that closes detection gaps identified after a near-miss ransomware event, within budget and before the incumbent contract lapses.",
      "setting": "Mid-sized financial services firm, in-house security team, cross-functional evaluation involving the CISO, procurement, finance, and the vendor evaluation manager; 90-day timeline; post-incident scrutiny from the board.",
      "constraints": [
        "Incumbent EDR contract expires in 90 days",
        "Board-mandated post-incident remediation deadline",
        "Fixed annual security tooling budget with finance sign-off required for overages",
        "Existing SIEM/cloud ecosystem creates integration preferences",
        "Limited internal red-team bandwidth for proof-of-concept testing",
        "Regulatory expectation (financial services) to document a defensible selection rationale"
      ],
      "stakeholders": [
        "Security Product/Vendor Evaluation Manager (interviewee)",
        "CISO",
        "Procurement lead",
        "Finance/budget owner",
        "Vendor sales engineers (shortlisted vendors)",
        "Board risk committee"
      ],
      "technical_terms_to_use": [
        "EDR/XDR",
        "MITRE ATT&CK coverage",
        "proof-of-concept (POC)",
        "detection SLA",
        "threat-hunting tier",
        "risk exposure calculator",
        "red-team simulation",
        "renewal window"
      ],
      "technical_terms_to_avoid": [
        "loss framing",
        "limited alternatives bias",
        "cognitive bias",
        "anchoring",
        "heuristic",
        "availability bias"
      ],
      "timeline": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Incumbent EDR contract expires in 90 days",
          "Incident review flagged specific detection gaps (lateral movement, encrypted C2 traffic)",
          "CISO wants a shortlist finalized within two weeks",
          "The firm's SIEM and cloud logging stack is built around one major ecosystem vendor",
          "A sales rep from that ecosystem vendor has proposed a bundled evaluation of three 'certified integration partner' EDR products plus the incumbent"
        ],
        "new_information_after_decision": [
          "Procurement later finds two additional EDR vendors with higher published MITRE ATT&CK technique coverage scores that were never included in the pre-screened list",
          "A peer firm's CISO mentions in passing that they evaluated a broader field of vendors for a similar replacement"
        ],
        "alternatives": [
          "Commission an independent RFI/market scan covering 8-10 EDR vendors including non-integrated options",
          "Restrict the shortlist to the incumbent plus three 'certified integration partner' vendors suggested by the existing ecosystem sales rep, citing time pressure and integration convenience"
        ],
        "intended_action": "Manager adopts the pre-screened, ecosystem-constrained shortlist and does not commission an independent market scan, treating integration convenience and speed as sufficient justification for narrowing the vendor field before any capability comparison occurs."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Shortlisted vendors have each offered a POC window",
          "Internal red-team bandwidth is limited to two weeks of testing capacity",
          "Vendors have offered their own third-party benchmark reports as an alternative to in-house testing",
          "Detection SLA requirements from the incident review are documented"
        ],
        "new_information_after_decision": [
          "The chosen POC methodology surfaces meaningful performance differences between the shortlisted vendors, feeding into phase 3 negotiations",
          "One vendor's live-simulation results diverge from its own benchmark report"
        ],
        "alternatives": [
          "Run a standardized in-house red-team simulation against all shortlisted vendors using the same attack playbook",
          "Rely primarily on vendor-supplied third-party benchmark reports supplemented by reference calls"
        ],
        "intended_action": "Manager chooses the standardized in-house red-team simulation as the primary evaluation method, a defensible methodological judgment given limited but sufficient testing bandwidth; no intended bias is embedded at this decision point."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "POC results show the leading vendor's standard tier meets the documented detection SLA",
          "The vendor's premium threat-hunting tier costs 40% above the budgeted amount, per finance",
          "The vendor's sales presentation includes a 'risk exposure calculator' projecting an average breach-cost avoidance figure (e.g., dollars saved by preventing a hypothetical future breach) if the premium tier is purchased",
          "No comparable efficiency/productivity-gain figure was prepared for the standard tier plus a phased upgrade path"
        ],
        "new_information_after_decision": [
          "Procurement later reconstructs a gain-framed ROI case (productivity and analyst-time savings) for the standard tier plus phased upgrade and finds it would meet the same detection SLA at materially lower cost",
          "Finance notes the premium-tier decision exceeded the pre-approved budget variance threshold"
        ],
        "alternatives": [
          "Select the standard tier, which POC results confirm meets the documented detection SLA, and defer advanced threat-hunting features to a phase-2 upgrade",
          "Select the premium tier, justified primarily by the vendor's breach-cost-avoidance projection, despite exceeding the pre-approved budget variance"
        ],
        "intended_action": "Manager recommends the premium tier, weighting the vendor's avoided-loss projection heavily in the recommendation memo while the standard tier's demonstrated SLA compliance and a comparable gain-framed efficiency case receive comparatively little analytic attention."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Board risk committee wants a remediation update before the incumbent contract lapses",
          "Implementation team estimates 45-60 days for a full rollout versus a shorter timeline for a partial pilot",
          "Some POC findings (e.g., alert-tuning false-positive rate) remain only partially validated",
          "Renewal pricing from the selected vendor is guaranteed only if signed within 30 days"
        ],
        "new_information_after_decision": [
          "Rollout proceeds; early production alerts show a higher-than-expected false-positive rate that requires additional tuning",
          "Board asks for a follow-up review of tuning progress at the 90-day mark"
        ],
        "alternatives": [
          "Recommend full production rollout within 60 days to lock in guaranteed renewal pricing",
          "Recommend a 30-day extended pilot with phased rollout to validate outstanding false-positive concerns before full commitment"
        ],
        "intended_action": "Manager recommends the full 60-day rollout to preserve pricing terms and meet the board's remediation timeline; this is presented as a defensible schedule-and-cost tradeoff and carries no intended bias instance."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what triggered this EDR replacement evaluation.",
        "What was your primary objective going into this process, and what constraints were you working under?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "How did the vendor shortlist come together, and who was involved?",
        "What did the POC process look like once the shortlist was set?",
        "How did the tier and pricing conversation unfold?",
        "What led to the final rollout recommendation?"
      ],
      "decision_point_probes": [
        "At the point you finalized the shortlist, what other options did you consider, and why were they included or excluded?",
        "What made the standardized red-team simulation preferable to relying on vendor benchmark reports?",
        "When you compared tiers, what evidence carried the most weight in your recommendation?",
        "What made you confident the full rollout timeline was the right call versus an extended pilot?"
      ],
      "decision_basis": [
        "What specific evidence or figures did you rely on most heavily at each step?",
        "Was there information you set aside or judged less relevant, and why?"
      ],
      "prior_experience": [
        "Had you run a vendor evaluation like this before? How did that shape your approach here?"
      ],
      "time_pressure_and_uncertainty": [
        "Where did time pressure most affect how thoroughly you could evaluate options?",
        "Where were you least certain, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If you'd had an extra month with no budget constraint, would anything have gone differently?",
        "If a colleague had pushed back on the shortlist or the tier choice, how do you think that conversation would have gone?",
        "Looking back, is there a point where a different framing of the evidence might have changed your recommendation?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "decision_point": 3,
        "mechanism": "The recommendation is anchored on a vendor-supplied loss-avoidance figure (projected breach cost avoided) rather than an equivalently constructed gain-framed figure (efficiency/productivity savings) for the cheaper option that met the same SLA, causing the manager to overweight the loss-framed evidence and exceed the approved budget variance.",
        "affected_reasoning_operation": "Weighting and integration of cost/benefit evidence when recommending a licensing tier",
        "evidence_available_at_time": [
          "POC results showing the standard tier meets the documented detection SLA",
          "Vendor's risk exposure calculator projecting breach-cost avoidance from the premium tier",
          "Finance's note that the premium tier exceeds pre-approved budget variance",
          "Absence of an equivalent gain-framed (efficiency/ROI) figure for the standard tier"
        ],
        "required_textual_manifestation": "The interviewee explicitly recalls being most persuaded by the avoided-loss/breach-cost figure and gives comparatively little independent weight to the standard tier's confirmed SLA compliance or to any efficiency-gain reasoning, while acknowledging the budget overage.",
        "plausible_nonbias_interpretation": "A risk-averse but reasonable manager might legitimately prioritize downside protection in a regulated financial-services context, especially post-incident, without this reflecting a framing effect.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "loss framing",
          "framing effect",
          "cognitive bias",
          "reference point",
          "prospect theory"
        ]
      },
      {
        "instance_id": "cb_02",
        "bias": "Exposure to limited alternatives",
        "decision_point": 1,
        "mechanism": "The manager accepts a pre-screened, ecosystem-constrained vendor list (incumbent plus three 'certified integration partners') proposed by a sales-affiliated source and does not commission an independent, broader market scan, so the entire downstream evaluation operates over a narrowed alternative set never benchmarked against excluded vendors with stronger published coverage scores.",
        "affected_reasoning_operation": "Generation and scoping of the alternative set prior to comparative evaluation",
        "evidence_available_at_time": [
          "90-day contract expiry timeline",
          "CISO's two-week shortlist deadline",
          "Sales-rep-curated list of three 'certified integration partner' vendors plus incumbent",
          "No independent RFI or market scan commissioned"
        ],
        "required_textual_manifestation": "The interviewee describes finalizing the shortlist from the sales-curated, integration-partner list and justifies this primarily by time pressure and integration convenience, without describing any independent search for alternatives outside that list; later learns of excluded vendors with stronger coverage scores.",
        "plausible_nonbias_interpretation": "Given a genuine two-week deadline and real integration costs, narrowing to ecosystem-compatible vendors could be a defensible, resource-constrained triage decision rather than a biased restriction of alternatives.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "limited alternatives",
          "restricted choice set",
          "cognitive bias",
          "narrow framing",
          "consideration set"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the biased condition with no paired control scenario supplied."
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
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Exactly one Loss Framing instance is planned, at decision point 3, distinct evidence trace (vendor loss-avoidance calculator vs. absent gain-framed comparison).",
      "Exactly one Exposure to limited alternatives instance is planned, at decision point 1, distinct evidence trace (sales-curated shortlist vs. absent independent market scan).",
      "Decision points 2 and 4 are deliberately kept neutral/defensible with no intended bias instances.",
      "No bias labels, definitions, or psychological terminology are to appear in the public interview.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and closing hypotheticals.",
      "Consequences described (false-positive rate uptick, budget overage, discovery of excluded vendors) do not mechanically prove bias; each has a plausible non-bias explanation.",
      "Target length 1,350 words (range 1,215-1,485) is achievable without repetitive exposition given two embedded instances and two neutral decision points."
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
