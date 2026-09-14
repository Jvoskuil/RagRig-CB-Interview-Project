You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "CS_Biased_5",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Vulnerability Management Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Legacy Order Gateway CVE",
    "scenario_summary_internal": "A vulnerability management analyst at a mid-size retail-fintech firm discovers a critical, exploit-in-the-wild remote code execution CVE affecting an internet-facing legacy order-processing gateway. Over roughly 96 hours, the analyst must triage severity and urgency, choose a mitigation path under a partial change freeze, decide between a self-built detection script and a vendor SIEM correlation rule, and finally close out residual risk on the ticket before an internal SLA deadline, all while competing tickets, a recent unrelated ransomware headline, and personal ownership of prior tooling shape the reasoning.",
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
        "intended_action": "Analyst escalates to emergency CAB, justifying urgency primarily by describing what the company stands to lose (contract, reputation, customer trust) if a breach occurs, rather than weighing the probability-adjusted exposure evenly against the disruption cost of emergency patching."
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
          "Two days later, the outbound DNS anomaly recurs and is escalated separately by a different analyst as a possible unrelated compromise indicator"
        ],
        "alternatives": [
          "Deploy the WAF rule and continue monitoring only the known exploit-pattern signature",
          "Deploy the WAF rule and also open a parallel investigation into the outbound DNS anomaly",
          "Delay the WAF rule until both the exploit pattern and the DNS anomaly are jointly investigated"
        ],
        "intended_action": "Analyst deploys the WAF rule and documents the ticket almost entirely around the matched exploit signature, mentioning the DNS anomaly only in passing without following up, because attention is locked onto confirming the known indicator."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor SIEM correlation rule for this CVE family becomes available, offering broader coverage (multiple payload variants) with lower maintenance overhead",
          "Analyst has a self-written detection script (built six months earlier) that only covers the single payload variant seen so far but that the analyst has tuned and trusts",
          "IT Ops manager suggests retiring the script in favor of the vendor rule to standardize detection across the team"
        ],
        "new_information_after_decision": [
          "A week later, a slightly different payload variant appears in logs that the self-written script does not flag but the vendor rule would have caught"
        ],
        "alternatives": [
          "Replace the self-written script with the vendor correlation rule",
          "Run both in parallel for a transition period",
          "Keep the self-written script as primary and treat the vendor rule as optional backup"
        ],
        "intended_action": "Analyst keeps the self-written script as the primary detection mechanism, citing familiarity and past tuning effort, and assigns the vendor rule a secondary, lower-priority role despite acknowledging its broader technical coverage."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "SLA remediation clock is at day 27 of 30; full vendor patch is still not deployed, only the WAF rule and self-written script are active",
          "A major, unrelated ransomware attack on another company hit national news three days ago, dominating recent SOC team discussion",
          "Residual risk assessment requires weighing patch coverage gaps, the DNS anomaly left unresolved from phase 2, and detection gaps left from phase 3"
        ],
        "new_information_after_decision": [
          "One month later, a post-incident audit finds the compensating controls left a narrow but real exposure window that was never closed, though no confirmed breach occurred"
        ],
        "alternatives": [
          "Close the ticket as adequately mitigated based on current compensating controls",
          "Extend the SLA and request additional resources to fully resolve the patch and open anomalies",
          "Escalate residual risk formally to the CISO for a risk-acceptance decision"
        ],
        "intended_action": "Analyst closes the ticket as adequately mitigated, expressing confidence that the controls they personally configured have the exploit path fully contained, while also citing the recent ransomware headline as the main justification for why this particular closure decision feels urgent and high-stakes, more than the technical residual-risk data on file supports."
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
        "What cues told you this needed emergency escalation rather than the standard cycle?",
        "What information sources did you rely on when choosing the WAF rule over other options?",
        "What was your goal when you decided to keep the outbound DNS anomaly separate from the CVE ticket?",
        "What alternatives did you consider before deciding between your script and the vendor rule?",
        "What was the main basis for your decision to close the ticket when you did?",
        "Had you handled a similar situation before, and did that experience shape this decision?",
        "How much time pressure did you feel at each of these moments?",
        "How confident were you that the compensating controls fully addressed the risk, and why?",
        "If you had had another week before the SLA deadline, would you have made any of these decisions differently?"
      ],
      "closing_hypotheticals": [
        "If the ransomware news story hadn't been in the headlines that week, do you think your closure decision would have changed?",
        "If the vendor SIEM rule had existed from day one, would you have built your own script at all?",
        "Looking back, is there a point where you think you weighted some piece of evidence more heavily than it deserved?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "decision_point": 1,
        "mechanism": "Justification for emergency escalation is framed almost entirely around what will be lost (contract, reputation, trust) if a breach occurs, rather than a balanced probability-weighted comparison of expected loss versus disruption cost of emergency patching.",
        "affected_reasoning_operation": "Risk-urgency judgment and escalation justification",
        "evidence_available_at_time": [
          "CVSS 9.8 exploit-in-the-wild alert",
          "Tier-1 asset criticality tag",
          "Two competing timeline options (21-day cycle vs emergency CAB)"
        ],
        "required_textual_manifestation": "The analyst's stated rationale for escalating should center on avoided losses (what the company stands to lose) rather than an evenly weighted cost-benefit statement, without ever naming the framing explicitly.",
        "plausible_nonbias_interpretation": "Emphasizing worst-case business impact could simply reflect appropriate business-risk communication to get executive buy-in for urgency.",
        "strength": "subtle",
        "do_not_make_explicit": ["loss framing", "framing effect", "bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 2,
        "mechanism": "Attention is fully absorbed by the confirmed exploit-signature match, causing a visibly logged but unrelated anomaly (outbound DNS spike) to be noted only in passing and not investigated, despite being available in the same dashboard view.",
        "affected_reasoning_operation": "Evidence scanning and triage prioritization within a single monitoring view",
        "evidence_available_at_time": [
          "Dashboard showing exploit-pattern signature spike",
          "Same dashboard showing an unrelated outbound DNS anomaly"
        ],
        "required_textual_manifestation": "The interview should show the analyst describing detailed engagement with the exploit-signature data while only briefly and dismissively mentioning the DNS anomaly as noted but not pursued.",
        "plausible_nonbias_interpretation": "Prioritizing the confirmed, ticket-relevant signature over an ambiguous anomaly could reflect reasonable triage discipline under time pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["selective attention", "inattentional blindness", "tunnel vision"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "decision_point": 3,
        "mechanism": "The analyst assigns disproportionate value to a self-built detection script relative to its objective technical coverage, resisting replacement by a broader vendor rule mainly because of ownership and prior tuning investment rather than comparative performance.",
        "affected_reasoning_operation": "Tool-selection and resource-retention decision",
        "evidence_available_at_time": [
          "Vendor correlation rule covering multiple payload variants",
          "Self-written script covering only one known variant",
          "IT Ops recommendation to standardize on the vendor rule"
        ],
        "required_textual_manifestation": "The analyst should explicitly justify keeping their own script as primary using ownership/familiarity language (built it, tuned it, trust it) rather than a coverage-based technical argument, while still acknowledging the vendor rule's broader coverage.",
        "plausible_nonbias_interpretation": "Preferring a well-understood, already-tuned tool could reflect reasonable operational caution about switching detection tooling mid-incident.",
        "strength": "subtle",
        "do_not_make_explicit": ["endowment effect", "ownership bias", "sunk cost"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "decision_point": 4,
        "mechanism": "The analyst expresses confidence that controls they personally configured have fully contained the exploit path, overstating personal control over a residual risk that independent audit later shows was not fully closed.",
        "affected_reasoning_operation": "Residual-risk assessment and ticket-closure judgment",
        "evidence_available_at_time": [
          "WAF rule and self-written script currently active",
          "Unresolved DNS anomaly and detection gap from earlier phases",
          "No confirmed exploitation of the residual gap yet"
        ],
        "required_textual_manifestation": "The analyst should state confidence that the exploit path is fully contained because of controls they personally set up, using personal-agency language, without qualifying this with documented residual-risk data.",
        "plausible_nonbias_interpretation": "Confidence in one's own configured controls could reflect legitimate professional assurance based on direct familiarity with the mitigation.",
        "strength": "subtle",
        "do_not_make_explicit": ["illusion of control", "overconfidence", "bias"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency",
        "decision_point": 4,
        "mechanism": "The analyst's stated urgency and justification for the closure decision is disproportionately anchored to a recent, unrelated ransomware headline rather than the specific technical residual-risk evidence on this ticket.",
        "affected_reasoning_operation": "Urgency/severity judgment used to justify the closure timing",
        "evidence_available_at_time": [
          "Recent unrelated ransomware news story from three days earlier",
          "SLA clock at day 27 of 30",
          "Technical residual-risk data (patch gap, unresolved anomaly, detection gap)"
        ],
        "required_textual_manifestation": "The analyst should reference the recent ransomware news as a significant reason the decision felt urgent, in a way that is separable from and additional to the loss-framing justification in decision point 1.",
        "plausible_nonbias_interpretation": "Citing a recent industry incident could be a legitimate way of communicating heightened threat-landscape awareness to stakeholders.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency bias", "availability heuristic", "anchoring"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased and no paired control scenario was supplied."
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
      "Exactly four decision points are defined, each with at least two alternatives",
      "Each of the five requested biases has exactly one planned instance, each tied to a distinct decision point and evidence source",
      "Decision point 4 hosts two different biases (illusion of control, recency) rather than two occurrences of the same bias, satisfying the same-bias cap rule",
      "No bias name, definition, or psychological label appears in technical_terms_to_use or intended interview content",
      "Each occurrence has a plausible non-bias interpretation to avoid mechanical proof of bias from outcome alone",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Consequences described (DNS anomaly escalation, payload variant miss, audit finding) do not conclusively prove bias, preserving interpretive ambiguity",
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
