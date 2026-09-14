You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "CS_Ambigious_6",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Vulnerability Management Analyst",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "The Wednesday CVE: Triage Under Pressure (Ambiguous Control)",
    "scenario_summary_internal": "A vulnerability management analyst at a mid-size financial-services company must triage a newly disclosed critical CVE affecting an internet-facing application, while simultaneously managing a backlog of scanner findings, a low-confidence SIEM alert, a change-window resourcing request, and final remediation scoping, all within a compressed 48-hour compliance window. The scenario mirrors CS_Biased_6 in domain, role, structure, vocabulary, actors, and decision count, but every decision is constructed to be genuinely underdetermined: each has a plausible, defensible non-bias justification and insufficient information for an observer to conclude any specific distorted reasoning process occurred. No named bias mechanism is intentionally instantiated.",
    "occupational_realism": {
      "objective": "Correctly prioritize and scope emergency remediation of the highest-actual-risk vulnerabilities within a 48-hour compliance window, using scanner output, vendor advisories, threat intelligence, and asset criticality data.",
      "setting": "Security operations team at a mid-size financial services firm; analyst works from a vulnerability management platform dashboard, a SIEM console, an asset inventory spreadsheet, and a ticketing system, communicating with IT operations and an incident response lead.",
      "constraints": [
        "48-hour window before a scheduled compliance audit reporting deadline",
        "Emergency change windows require IT operations approval and disrupt business-hours availability",
        "Backlog of ~40 open scanner findings from the prior week's weekly scan",
        "Limited headcount: analyst is the sole triage owner for the shift",
        "General awareness of an industry breach reported the prior week, mentioned only as ambient context, not as a stated reason for any specific choice"
      ],
      "stakeholders": [
        "Vulnerability Management Analyst (interviewee)",
        "IT Operations Manager (approves change windows)",
        "Incident Response Lead (receives escalations)",
        "Compliance/Audit team (deadline owner)",
        "Application owners for affected systems"
      ],
      "technical_terms_to_use": [
        "CVE", "CVSS", "EPSS", "RCE", "SIEM", "asset inventory", "patch management", "change window", "remediation SLA", "vulnerability scanner", "threat intel feed", "privilege escalation", "lateral movement", "exploit chain", "authentication bypass"
      ],
      "technical_terms_to_avoid": [
        "recency bias", "availability heuristic", "framing effect", "inattentional blindness", "selective attention bias", "cognitive bias", "anchoring", "limited alternatives bias", "heuristic", "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor advisory just published: new CVE, CVSS 9.8, remote code execution, affects an internet-facing authentication API",
          "Backlog of ~40 open findings from last week's scan, including an unpatched database server with excessive service-account privileges, open for 90+ days",
          "General industry awareness of an unrelated breach reported the prior week, not directly discussed as a decision factor",
          "Only 48 hours until compliance audit report is due"
        ],
        "new_information_after_decision": [
          "The new CVE is technically an authentication-bypass flaw in an API gateway, confirmed after deeper review",
          "The database finding is later flagged by the audit team as a severe unresolved item, though its exploitability had not been independently reassessed at triage time"
        ],
        "alternatives": [
          "Prioritize the newly disclosed CVE for immediate emergency patching",
          "Prioritize the older, higher-asset-criticality database privilege finding",
          "Split resources evenly across both in parallel"
        ],
        "intended_action": "Analyst prioritizes the newly disclosed CVE, citing its CVSS score, internet-facing exposure, and the absence of any existing compensating control, while noting the database finding lacks a similarly confirmed exploit path at that time — a judgment call between two legitimately serious but differently characterized risks."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "SIEM shows a 'privilege escalation - low confidence' alert on an internal host",
          "The alert includes a log entry showing a somewhat unusual lateral-movement timestamp",
          "Dashboard also displays an anomalous outbound traffic entry on the same host, which the analyst reviews alongside the alert",
          "Analyst is concurrently cross-referencing the new CVE against the asset inventory"
        ],
        "new_information_after_decision": [
          "Two days later, the outbound traffic entry is retroactively linked to a confirmed low-level compromise on that host",
          "IR later notes the lateral-movement timestamp was non-routine, though corroborating indicators were sparse at the time"
        ],
        "alternatives": [
          "Escalate the low-confidence alert to Incident Response for immediate review",
          "Note both the alert and the outbound traffic entry but continue asset cross-referencing given no corroborating indicator of compromise",
          "Flag for follow-up after the CVE triage is complete"
        ],
        "intended_action": "Analyst reviews both the alert and the adjacent outbound traffic entry, judges that neither individually meets the threshold for interrupting the CVE triage given the available corroborating evidence, and defers full investigation — a defensible call given genuinely limited diagnostic detail at the time, with no stated reliance on how often the alert label has resolved historically."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patching the API gateway requires an emergency change window during business hours, disrupting customer-facing transactions for an estimated 20 minutes",
          "IT Operations Manager requires a written justification to approve an emergency (vs. weekend) window",
          "EPSS score indicates moderate near-term exploitation probability, comparable to several other findings resolved on the normal weekend cycle in the past year"
        ],
        "new_information_after_decision": [
          "IT Operations approves the emergency window",
          "No exploitation attempt against this specific CVE is observed in the following week, leaving the actual urgency level unconfirmed either way"
        ],
        "alternatives": [
          "Request an emergency business-hours change window",
          "Schedule remediation for the standard weekend maintenance window",
          "Request a partial mitigation (WAF rule) now and defer full patch to the weekend window"
        ],
        "intended_action": "Analyst's justification presents both the EPSS estimate and the potential business consequences together without a stated preference for one framing over the other, and the interview does not establish which factor was actually decisive — a genuinely ambiguous resourcing judgment."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The vulnerability scanner's default dashboard view surfaces exactly two hosts matching the CVE's vulnerable library signature",
          "The asset inventory spreadsheet, outside the scanner's default view, lists three additional hosts sharing the same vulnerable library version under a different asset category",
          "Time remaining before the audit deadline is limited"
        ],
        "new_information_after_decision": [
          "One week later, one of the three unscoped hosts is found still running the vulnerable library during a follow-up audit scan"
        ],
        "alternatives": [
          "Scope remediation to the two hosts shown in the scanner's default view",
          "Manually cross-reference the full asset inventory to identify all affected hosts before finalizing scope",
          "Scope the two known hosts now and schedule a follow-up sweep for additional hosts"
        ],
        "intended_action": "Analyst scopes to the two hosts shown by the scanner and separately schedules a follow-up sweep of the broader inventory given time constraints, a partial-verification compromise whose adequacy is genuinely debatable rather than a clear case of treating one source as exhaustive."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what a typical shift looks like for you as a vulnerability management analyst.",
        "What was the first thing you noticed when this incident began?"
      ],
      "timeline_reconstruction": [
        "Can you walk me through, in order, everything that happened from the moment the CVE advisory came in?",
        "What were you looking at on your screen at each stage?",
        "What information did you have at each point, and what came in later?"
      ],
      "decision_point_probes": [
        "What specific cues made you decide the way you did?",
        "What sources did you check before deciding, and which ones did you not have time to check?",
        "What were you trying to accomplish at that moment, and did that goal compete with anything else?",
        "What alternative options did you consider at that point, and why did you rule them out?",
        "What ultimately tipped the decision for you?",
        "Had you handled anything similar before? Did that experience shape this call?",
        "How much time pressure did you feel at that point?",
        "How confident were you in that judgment at the time versus in hindsight?"
      ],
      "closing_hypotheticals": [
        "If you'd had more time before the deadline, would you have approached any of these differently?",
        "If the scanner's default view had shown five hosts instead of two, would your scoping decision have changed?",
        "Looking back, is there anything you think you weighed differently than you would today?",
        "If you had to write the change-window justification again, would you present it differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "CS_Biased_6",
      "features_to_match": [
        "Domain, role, setting, and stakeholder set",
        "Four-decision-point structure and chronology",
        "Same operational objective, constraints, and 48-hour deadline",
        "Same technical vocabulary and tool set (scanner, SIEM, asset inventory, EPSS, CVSS)",
        "Same surface incident type: new critical CVE, low-confidence SIEM alert, change-window request, host-scoping decision",
        "Comparable difficulty and emotional tone (time pressure, professional composure)"
      ],
      "features_to_remove_or_change": [
        "Remove explicit attribution of urgency to a recently salient breach story",
        "Remove explicit statement that a frequently recalled ticket category or alert-label history displaced consideration of a better-fitting category",
        "Remove explicit statement that an available visual cue went completely unregistered due to narrow attentional focus",
        "Remove explicit statement that loss-oriented language, rather than probability data, drove the urgency judgment",
        "Remove explicit statement that a single tool's default output was treated as an exhaustive alternative set without any partial verification"
      ],
      "ambiguity_boundary": "Each decision point must retain at least one genuinely plausible non-bias justification and at least one detail that leaves the analyst's actual reasoning basis underdetermined, without the interview explicitly resolving which factor was decisive. The ambiguity must arise from realistically incomplete information and reasonable trade-offs, not from artificial vagueness or contradictory statements."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable for this run (ambiguous_control condition); autoselected placeholder retained for structural consistency with the paired biased scenario: prior exposure to a highly publicized industry breach report immediately before CVE triage",
      "original_state": "Not activated in this condition",
      "counterfactual_state": "Not activated in this condition",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "Analyst role, staffing, and tooling"
      ],
      "expected_causal_difference": "Not applicable; no causal manipulation is performed in this condition.",
      "causal_test_question": "Not applicable; this run is not a counterfactual condition."
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Zero intended bias instances are embedded for Recency, Availability Frequency, Exposure to limited alternatives, Loss Framing, and Selective Attention/Inattentional Blindness.",
      "Each decision point includes a genuinely plausible non-bias justification and leaves the analyst's decisive reasoning basis underdetermined.",
      "No bias name, definition, or psychological terminology appears anywhere in probes or intended interview content.",
      "Vocabulary, structure, decision count, actors, setting, and difficulty match CS_Biased_6 as required for a paired control.",
      "Consequences described (audit flag, retroactive compromise link, follow-up scan finding) do not deterministically prove any decision was biased or unbiased.",
      "Target interview length of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points, opening, timeline reconstruction, and closing hypotheticals without repetitive exposition.",
      "No named-bias mechanism from the manifest is intentionally instantiated at any decision point, probe, or hypothetical.",
      "Ambiguity is achieved through realistic informational incompleteness, not exaggerated contradiction or suspiciously neutral phrasing."
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
