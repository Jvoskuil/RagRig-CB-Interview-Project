You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "CS_Vocab_Control_5",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Vulnerability Management Analyst",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Legacy Order Gateway CVE — Vocabulary-Matched Control",
    "scenario_summary_internal": "A vulnerability management analyst at a mid-size retail-fintech firm discovers a critical, exploit-in-the-wild remote code execution CVE affecting an internet-facing legacy order-processing gateway. Over roughly 96 hours, the analyst triages severity and urgency, chooses a mitigation path under a partial change freeze, decides between a self-built detection script and a vendor SIEM correlation rule, and closes out residual risk on the ticket before an internal SLA deadline. This version mirrors the paired biased scenario's setting, stakeholders, vocabulary, decision count, and emotional tone, but every decision is resolved through balanced, evenly-weighted, well-documented reasoning with no intended cognitive-bias instances.",
    "occupational_realism": {
      "objective": "Triage, mitigate, and close out a critical CVE on an internet-facing legacy order-processing system within the organization's 30-day critical-remediation SLA, without causing unplanned downtime to a revenue-generating platform.",
      "setting": "Vulnerability Management function inside the SOC of a mid-size retail-fintech company running hybrid on-prem/cloud infrastructure; a partial year-end change freeze is approaching in 10 days.",
      "constraints": [
        "Legacy order-processing gateway cannot be patched without vendor coordination and a scheduled maintenance window",
        "Approaching change freeze limits available patch windows",
        "Analyst is simultaneously handling two other open high-severity tickets",
        "Internal policy sets a 30-day SLA for critical CVE remediation",
        "App owner resists downtime due to peak sales period",
        "Limited SOC staffing means the analyst owns triage, mitigation design, and closure end-to-end"
      ],
      "stakeholders": [
        "Vulnerability Management Analyst (interviewee)",
        "CISO",
        "IT Operations Manager",
        "Legacy application owner",
        "Compliance/GRC officer",
        "SOC threat intel lead"
      ],
      "technical_terms_to_use": [
        "CVSS score",
        "exploit-in-the-wild",
        "WAF virtual patch",
        "compensating control",
        "residual risk",
        "SIEM correlation rule",
        "change advisory board (CAB)",
        "asset criticality tier",
        "patch window",
        "threat intel feed",
        "SLA remediation clock"
      ],
      "technical_terms_to_avoid": [
        "loss framing",
        "endowment effect",
        "illusion of control",
        "recency bias",
        "selective attention",
        "inattentional blindness",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Threat intel feed flags a new CVE (CVSS 9.8) with confirmed exploitation in the wild affecting the gateway's web framework version",
          "Asset is tagged Tier-1 criticality (internet-facing, processes customer orders)",
          "Standard patch cycle would apply the fix in 21 days; emergency escalation would require pulling the app owner into an off-cycle CAB session tomorrow"
        ],
        "new_information_after_decision": [
          "App owner reports the emergency CAB slot was granted, but only a 2-hour window is available, insufficient for full regression testing"
        ],
        "alternatives": [
          "Escalate immediately to emergency CAB and push for an off-cycle patch",
          "Route the CVE into the standard 21-day patch cycle with interim monitoring",
          "Request a compensating control now and defer the patch decision until more exploit data arrives"
        ],
        "intended_action": "Analyst escalates to emergency CAB after producing a short comparison that weighs the probability-adjusted exposure of waiting 21 days against the operational disruption cost of an off-cycle patch attempt, citing both the exploit-in-the-wild status and the short regression-testing window as factors pulling in opposite directions before recommending escalation."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Emergency patch window is too short for full regression testing, so a WAF virtual patch (rule blocking the known exploit request pattern) is proposed as an interim compensating control",
          "SOC dashboard shows a spike in requests matching the known CVE payload signature",
          "Same dashboard also shows an unrelated but visible anomaly: a burst of unusual outbound DNS queries from the gateway host, unconnected in the ticket to the CVE signature"
        ],
        "new_information_after_decision": [
          "The parallel DNS investigation determines the anomaly traces to a previously known internal monitoring job that had been recently reconfigured, unrelated to the CVE, and closes without further action"
        ],
        "alternatives": [
          "Deploy the WAF rule and continue monitoring only the known exploit-pattern signature",
          "Deploy the WAF rule and also open a parallel investigation into the outbound DNS anomaly",
          "Delay the WAF rule until both the exploit pattern and the DNS anomaly are jointly investigated"
        ],
        "intended_action": "Analyst deploys the WAF rule and, in the same ticket update, opens a separate low-priority task to investigate the DNS anomaly, reasoning that both are visible in the same monitoring view and each deserves independent documentation even though only one is tied to the active CVE."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor SIEM correlation rule for this CVE family becomes available, offering broader coverage (multiple payload variants) with lower maintenance overhead",
          "Analyst has a self-written detection script (built six months earlier) that only covers the single payload variant seen so far",
          "IT Ops manager suggests retiring the script in favor of the vendor rule to standardize detection across the team"
        ],
        "new_information_after_decision": [
          "A week later, a slightly different payload variant appears in logs and is correctly flagged by the vendor rule, confirming the coverage gap that had been identified in advance"
        ],
        "alternatives": [
          "Replace the self-written script with the vendor correlation rule",
          "Run both in parallel for a transition period",
          "Keep the self-written script as primary and treat the vendor rule as optional backup"
        ],
        "intended_action": "Analyst compares the two tools on documented coverage (number of payload variants detected) and maintenance overhead, and decides to run both in parallel for a transition period so that neither tool's known limitations create a detection gap while the team evaluates a permanent standard."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "SLA remediation clock is at day 27 of 30; full vendor patch is still not deployed, only the WAF rule and both detection tools are active",
          "Residual risk assessment requires weighing patch coverage gaps, the now-resolved DNS anomaly, and the current dual-tool detection coverage",
          "Compliance/GRC officer requests a documented risk position before the SLA deadline"
        ],
        "new_information_after_decision": [
          "One month later, a post-incident audit confirms the compensating controls and dual detection coverage held, though the underlying vendor patch is still pending a rescheduled maintenance window"
        ],
        "alternatives": [
          "Close the ticket as adequately mitigated based on current compensating controls",
          "Extend the SLA and request additional resources to fully resolve the patch",
          "Escalate residual risk formally to the CISO for a risk-acceptance decision"
        ],
        "intended_action": "Analyst compiles the outstanding items (unpatched root cause, dual-tool coverage status, resolved DNS finding) into a residual risk summary and escalates it to the CISO for a formal risk-acceptance decision rather than closing the ticket outright, explicitly basing the recommendation on the documented gaps rather than on any single recent event."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how you first became aware of this vulnerability and what your initial objective was.",
        "What was your role in this incident from start to finish?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events in the order they happened.",
        "What information did you have at each point, and what changed afterward?",
        "Were there other tickets or priorities competing for your attention during this period?"
      ],
      "decision_point_probes": [
        "What factors did you weigh when deciding between the standard patch cycle and emergency escalation?",
        "What information sources did you rely on when choosing the WAF rule and handling the DNS anomaly?",
        "What was your goal in how you tracked the DNS anomaly alongside the CVE ticket?",
        "What alternatives did you consider before deciding how to handle the script versus the vendor rule?",
        "What was the main basis for your decision at closure time?",
        "Had you handled a similar situation before, and did that experience shape any of these decisions?",
        "How much time pressure did you feel at each of these moments?",
        "How confident were you that the compensating controls addressed the risk, and what informed that confidence?",
        "If you had had another week before the SLA deadline, would you have made any of these decisions differently?"
      ],
      "closing_hypotheticals": [
        "If the vendor SIEM rule hadn't existed at all during this incident, how would that have changed your detection approach?",
        "If the DNS anomaly had turned out to be related to the CVE, would that have changed how you sequenced your investigation?",
        "Looking back, is there a point where you think additional information would have changed your decision?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "CS_Biased_5",
      "features_to_match": [
        "Domain vocabulary (CVSS score, exploit-in-the-wild, WAF virtual patch, compensating control, residual risk, SIEM correlation rule, CAB, asset criticality tier, patch window, threat intel feed, SLA remediation clock)",
        "Overall incident structure and four-decision-point sequence",
        "Difficulty and subtlety of reasoning required to interpret answers",
        "Actors and stakeholders (CISO, IT Ops manager, app owner, Compliance/GRC officer, threat intel lead)",
        "Emotional tone (measured professional urgency, time pressure, competing priorities)",
        "Decision count (exactly four) and general narrative arc from triage to closure"
      ],
      "features_to_remove_or_change": [
        "Replace loss-centered escalation justification with an evenly-weighted probability/disruption comparison",
        "Replace attention lock on the exploit signature with parallel, evenly-documented handling of both the signature and the DNS anomaly",
        "Replace ownership-based tool retention with a coverage-and-overhead-based parallel-run decision",
        "Replace personal-control confidence and recency-driven urgency at closure with a documented, escalation-based risk position independent of any single recent event"
      ],
      "ambiguity_boundary": "Reasoning must remain balanced and well-justified rather than artificially neutral; alternatives should be genuinely weighed with documented criteria, and outcomes should not be uniformly positive, but no decision should be resolved through the mechanisms defined for the five target biases."
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
      "Exactly four decision points are defined, each with at least two alternatives, matching the paired biased scenario's structure",
      "Zero intended bias instances are planned across all five named biases",
      "Domain vocabulary, stakeholders, constraints, and decision sequence match the paired scenario CS_Biased_5",
      "No bias name, definition, or psychological label appears anywhere in the specification content intended for the public interview",
      "Each decision point offers a balanced, evidence-based resolution with documented criteria rather than an artificially neutral or contradictory account",
      "Probe plan retains the same coverage categories (cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, hypotheticals) as the paired scenario, reworded to avoid presupposing biased reasoning",
      "Consequences described (DNS anomaly resolution, vendor rule catching a new variant, audit confirming controls held) remain plausible and do not mechanically prove absence of bias, preserving natural narrative variation",
      "Scenario content and terminology are sufficient to support a 1,215-1,485 word interview without repetitive exposition"
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
