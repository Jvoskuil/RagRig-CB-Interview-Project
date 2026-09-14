You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "CS_Biased_7",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Chief Information Security Officer (CISO)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Anomalous Login and the Threat-Intel Renewal",
    "scenario_summary_internal": "Elena Voss, CISO of a mid-size fintech (NorthGate Financial), is midway through the annual security-vendor budget cycle when a SOC analyst flags an anomalous privileged login on a payments-adjacent host. Elena must triage the alert, decide whether to renew the incumbent threat-intel/EDR vendor or run a competitive RFP, decide how aggressively to contain the suspected intrusion given revenue-impact framing from the CFO, and finally decide how to reallocate the annual security budget after the incident is closed. The scenario is designed to surface anchoring on automated severity scores and legacy budget figures, narrow vendor consideration due to habitual sourcing, attentional narrowing onto the flagged host, overconfidence in a hastily built monitoring script, loss-framed reluctance to isolate a revenue-generating segment, and attachment to the incumbent vendor relationship.",
    "occupational_realism": {
      "objective": "Detect, triage, and contain a suspected credential-based intrusion while making a concurrent annual vendor-renewal and budget decision without disrupting payment operations.",
      "setting": "Mid-size fintech company (NorthGate Financial, ~450 employees) processing card and ACH payments; SOC operates with a 6-person team; annual security budget cycle overlaps with a live security alert.",
      "constraints": [
        "Board-mandated deadline to finalize next fiscal year's security vendor contracts within the week",
        "Payments processing segment cannot be taken fully offline without significant revenue and SLA penalty exposure",
        "SOC team is short-staffed due to one analyst on leave",
        "Existing EDR/threat-intel vendor contract auto-renews unless canceled within 5 business days",
        "Regulatory expectation (PCI DSS) to document incident response decisions and rationale"
      ],
      "stakeholders": [
        "Elena Voss, CISO (interview subject)",
        "SOC Lead Analyst",
        "CFO",
        "VP of Payments Operations",
        "Incumbent EDR/Threat-Intel Vendor Account Manager",
        "External Incident Response Retainer Firm"
      ],
      "technical_terms_to_use": [
        "SIEM", "EDR", "SOC", "lateral movement", "privileged access", "IOC", "playbook",
        "containment", "network segmentation", "MFA", "threat intelligence feed", "RFP",
        "MTTR", "SOAR", "vendor risk assessment", "credential stuffing", "tabletop exercise",
        "risk appetite", "board reporting", "CVE"
      ],
      "technical_terms_to_avoid": [
        "anchoring", "anchor", "endowment effect", "sunk cost", "illusion of control",
        "loss aversion", "loss framing", "selective attention", "inattentional blindness",
        "limited alternatives bias", "cognitive bias", "heuristic", "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "SOC's SIEM auto-classified the login anomaly as 'Medium' severity based on a default risk-scoring model",
          "The flagged host is a jump server used by a payments engineer",
          "A second, lower-priority alert fired nine minutes earlier on an adjacent authentication server but was not opened",
          "SOC analyst is handling both alerts alone due to short staffing"
        ],
        "new_information_after_decision": [
          "The adjacent authentication server alert, once reviewed hours later, is found to share the same source IP range as the jump-server anomaly",
          "The automated 'Medium' score did not account for the privileged nature of the account involved"
        ],
        "alternatives": [
          "Escalate immediately to full incident response and open both alerts jointly",
          "Accept the automated 'Medium' classification and schedule standard next-business-day follow-up",
          "Request the analyst correlate all authentication alerts from the same time window before deciding severity"
        ],
        "intended_action": "Elena defers to the SIEM's default 'Medium' score and directs the SOC analyst to focus solely on the flagged jump server, without requesting a broader correlation sweep of concurrent alerts."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The incumbent EDR/threat-intel vendor contract must be renewed or canceled within 5 business days",
          "NorthGate has used this vendor for six years and Elena's team built custom detection rules and dashboards on top of it",
          "Two peer fintech CISOs, contacted informally, mentioned they also use the same vendor or its closest competitor",
          "No formal RFP has been issued this cycle; procurement flagged that three other vendors offer comparable EDR/threat-intel bundles"
        ],
        "new_information_after_decision": [
          "A newer entrant vendor, not considered, later publishes a case study showing faster detection times for the same attack pattern involved in this incident",
          "Procurement notes the renewal was signed without a comparative bid on file"
        ],
        "alternatives": [
          "Run a short competitive RFP against at least one vendor outside the two informally referenced by peers",
          "Renew the incumbent vendor because of the custom integrations and team familiarity",
          "Request a 90-day contract extension to allow time for a proper market scan"
        ],
        "intended_action": "Elena renews the incumbent vendor, citing the effort already invested in custom dashboards and rules, and limits her comparison to the vendor and the one competitor her peers happened to mention."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Correlated logs now show lateral movement attempts from the compromised jump-server account toward the payments database segment",
          "Elena's team wrote a quick monitoring script overnight to watch for further movement from that account",
          "The CFO states that isolating the payments segment for containment will cause a guaranteed processing outage costing an estimated $180,000 in same-day transaction fees",
          "The external IR retainer firm recommends full segment isolation pending forensic review; there is no confirmed evidence yet that isolation would fully stop the threat"
        ],
        "new_information_after_decision": [
          "Two hours after the decision, the compromised account is used to access a second internal system that the monitoring script did not cover",
          "Forensics later determines the attacker had already exfiltrated a small dataset before the monitoring script was deployed"
        ],
        "alternatives": [
          "Isolate the payments segment fully as the IR retainer recommends, accepting the guaranteed short-term revenue impact",
          "Rely on the newly written monitoring script and targeted account lockout instead of full isolation",
          "Isolate only the specific subnet touched so far while keeping broader payments processing online"
        ],
        "intended_action": "Elena chooses to rely on the overnight monitoring script and a targeted account lockout rather than full segment isolation, treating the script as sufficient coverage and treating the CFO's framing of a 'guaranteed' revenue loss as decisive against isolation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The incident is now contained; a post-incident budget review is due to the board in three days",
          "A remediation project (privileged-access segmentation) was scoped 18 months ago with a cost estimate of $240,000, never funded",
          "Current vendor quotes for the same scope, gathered this week, range from $310,000 to $340,000 due to inflation and expanded scope",
          "The board has asked for a single recommended remediation budget figure"
        ],
        "new_information_after_decision": [
          "Procurement flags that the submitted budget figure is below every current vendor quote received this week",
          "The finance team later notes the original $240,000 estimate excluded cloud components added to the environment since it was scoped"
        ],
        "alternatives": [
          "Recommend a budget based on the current vendor quotes gathered this week",
          "Recommend the original $240,000 figure with a modest contingency",
          "Commission a fresh, narrow-scope estimate before submitting any number to the board"
        ],
        "intended_action": "Elena recommends a remediation budget close to the original 18-month-old $240,000 estimate, treating it as the reasonable baseline and only lightly adjusting it upward despite current quotes running well above that figure."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through your role and responsibilities as CISO at NorthGate Financial.",
        "Describe, in your own words, the incident you're about to walk me through and what the overall objective was."
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from the first alert to the incident being closed, in the order they happened.",
        "At each stage, what did you know, and when did you learn it?"
      ],
      "decision_point_probes": [
        "What cues in the alert or dashboard drew your attention first, and what, if anything, competed for your attention at that moment?",
        "What information sources did you consult before making this call, and were there sources you didn't check?",
        "What alternatives did you consider at this point, and why did you rule the others out?",
        "What was the main basis for your decision here?",
        "Had you handled a similar situation before, and did that experience shape this decision?",
        "How much time pressure were you under when you made this call?",
        "How confident were you in the information you were acting on, and what was still uncertain?",
        "If you'd had an extra day or an extra analyst, would this decision have gone differently?"
      ],
      "closing_hypotheticals": [
        "If the SIEM hadn't pre-scored the alert's severity, do you think your initial response would have changed?",
        "If procurement had required a formal RFP regardless of timeline, how might the vendor decision have gone?",
        "If the CFO had not quantified the outage cost, would the containment call have been different?",
        "Looking back, what would you tell a CISO facing the same budget-review deadline with an 18-month-old cost estimate on file?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Adjustment and anchoring",
        "decision_point": 1,
        "mechanism": "Elena adopts the SIEM's automatically generated 'Medium' severity score as the reference point and makes only a minor upward adjustment in urgency, rather than independently assessing severity from the underlying evidence (privileged account, jump-server role).",
        "affected_reasoning_operation": "Initial severity/urgency estimation",
        "evidence_available_at_time": [
          "Automated 'Medium' severity score from SIEM",
          "Knowledge that the account is privileged and tied to payments infrastructure"
        ],
        "required_textual_manifestation": "Elena explicitly references the automated score as her starting point and describes adjusting her own urgency assessment only slightly from it, despite having independent reasons (privileged account) to weight it higher.",
        "plausible_nonbias_interpretation": "Trusting a validated automated triage tool could be a reasonable efficiency practice under staffing constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "reference point", "bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 1,
        "mechanism": "Having locked onto the flagged jump server as the object of concern, Elena directs the analyst to focus exclusively there, causing the concurrent, related alert on the adjacent authentication server to go unexamined until much later.",
        "affected_reasoning_operation": "Evidence-selection / scope-setting for investigation",
        "evidence_available_at_time": [
          "A second alert on an adjacent authentication server that fired nine minutes earlier",
          "Single analyst available to review both alerts"
        ],
        "required_textual_manifestation": "Elena describes narrowing the analyst's focus to the jump server without mentioning the second alert as something she asked to be checked in parallel; the connection is only made much later.",
        "plausible_nonbias_interpretation": "With one analyst and limited time, focusing on the most concrete alert first is a defensible triage sequencing choice.",
        "strength": "moderate",
        "do_not_make_explicit": ["selective attention", "inattentional blindness", "missed", "overlooked"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "decision_point": 2,
        "mechanism": "Elena overvalues the incumbent vendor relationship because of the custom dashboards and detection rules her team has already built on it, treating that built-up investment as making the incumbent inherently more valuable than a comparable alternative would be if evaluated fresh.",
        "affected_reasoning_operation": "Vendor valuation / renewal justification",
        "evidence_available_at_time": [
          "Six years of custom rules and dashboards built on the incumbent platform",
          "Three other vendors flagged by procurement as offering comparable bundles"
        ],
        "required_textual_manifestation": "Elena cites the team's built investment in the incumbent's platform as the primary reason to keep it, without separately establishing that the incumbent's current capability outperforms the alternatives on their own merits.",
        "plausible_nonbias_interpretation": "Switching costs and integration risk are legitimate factors in vendor retention decisions.",
        "strength": "subtle",
        "do_not_make_explicit": ["endowment", "sunk cost", "overvalue"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Exposure to limited alternatives",
        "decision_point": 2,
        "mechanism": "Elena restricts her comparison set to the incumbent and the single competitor mentioned informally by peer CISOs, never engaging procurement's list of three other qualified vendors, so the renewal decision is made against an artificially narrow option set.",
        "affected_reasoning_operation": "Alternative-generation for vendor decision",
        "evidence_available_at_time": [
          "Procurement's list of three vendors offering comparable bundles",
          "Informal peer mentions of one alternative vendor"
        ],
        "required_textual_manifestation": "Elena describes her comparison as being between the incumbent and 'the vendor a couple of peers use,' without describing having reviewed procurement's broader vendor list.",
        "plausible_nonbias_interpretation": "Relying on trusted peer recommendations can be an efficient, low-risk way to shortlist vendors under time pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["limited alternatives", "narrow options", "restricted search"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Illusion of control",
        "decision_point": 3,
        "mechanism": "Elena treats the overnight, hastily built monitoring script as providing reliable coverage of the compromised account's activity, expressing confidence in containment through that script despite it being untested and narrow in scope relative to the actual threat surface.",
        "affected_reasoning_operation": "Confidence assessment of a self-implemented containment measure",
        "evidence_available_at_time": [
          "A monitoring script built overnight by the team, not independently tested",
          "IR retainer firm's recommendation for full segment isolation pending forensic review"
        ],
        "required_textual_manifestation": "Elena describes feeling that the script 'had it covered' or gave her team the visibility they needed, in place of full isolation, without qualifying its actual tested scope.",
        "plausible_nonbias_interpretation": "Deploying a rapid custom monitoring measure while avoiding a costly full isolation is a legitimate proportional-response strategy under uncertainty.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control", "overconfidence", "false sense of coverage"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Loss Framing",
        "decision_point": 3,
        "mechanism": "The CFO's presentation of the isolation option as a 'guaranteed' $180,000 loss, versus an uncertain security benefit, leads Elena to weight the certain financial loss far more heavily than the uncertain security gain, tilting her decision away from isolation.",
        "affected_reasoning_operation": "Risk-tradeoff evaluation between certain cost and uncertain benefit",
        "evidence_available_at_time": [
          "CFO's framing of isolation as a guaranteed $180,000 same-day loss",
          "IR retainer's recommendation, framed only in terms of risk reduction, not quantified certainty"
        ],
        "required_textual_manifestation": "Elena explicitly recalls the CFO's 'guaranteed loss' framing as the decisive factor tipping her away from isolation, contrasted with the less concretely stated security benefit.",
        "plausible_nonbias_interpretation": "Weighing a certain, quantified operational cost against an unquantified security benefit is a standard part of risk-based decision-making.",
        "strength": "subtle",
        "do_not_make_explicit": ["loss framing", "framing effect", "certain loss versus uncertain gain"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Adjustment and anchoring",
        "decision_point": 4,
        "mechanism": "Elena starts from the 18-month-old $240,000 remediation estimate and makes only a modest upward adjustment for the board recommendation, rather than re-deriving the figure from this week's actual vendor quotes, which all exceed that adjusted figure.",
        "affected_reasoning_operation": "Budget-figure estimation for board recommendation",
        "evidence_available_at_time": [
          "18-month-old remediation cost estimate of $240,000",
          "Current vendor quotes ranging from $310,000-$340,000"
        ],
        "required_textual_manifestation": "Elena describes taking the old estimate as her starting figure and nudging it up 'a bit' for the board, rather than basing the recommendation on the range of current quotes she has in hand.",
        "plausible_nonbias_interpretation": "Using a prior internal estimate as a starting point for continuity in board reporting can be a reasonable practice absent stronger signals to deviate.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "stale estimate", "starting point"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this generation is the primary 'biased' condition with no paired control specified in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence and salience of the SIEM's automated severity pre-score at the moment of initial triage (autoselected as the highest-leverage single causal lever, given its downstream role in anchoring cb_01 and its narrative connection to attention allocation in cb_02)",
      "original_state": "The SIEM displays a default automated 'Medium' severity score to Elena before she reviews underlying evidence",
      "counterfactual_state": "The SIEM displays raw event data without a pre-computed severity score, requiring Elena to derive urgency independently",
      "variables_to_hold_constant": [
        "Company profile and staffing levels",
        "Incident type and technical details (privileged jump-server compromise, lateral movement pattern)",
        "Vendor renewal deadline and budget-cycle timing",
        "CFO's revenue-impact framing at decision point 3",
        "Decision count and sequence (4 decision points, same order)",
        "Word count target and interview structure"
      ],
      "expected_causal_difference": "Without a displayed pre-score, Elena would be expected to derive severity from the privileged-account context directly, plausibly increasing early escalation and reducing the delay in correlating the second alert.",
      "causal_test_question": "Does removing the automated severity pre-score change the CISO's initial escalation urgency and the speed of alert correlation, independent of all other incident facts?"
    },
    "generation_checks": [
      "Exactly 7 total occurrence instances planned, matching the sum of the manifest (2+1+1+1+1+1=7)",
      "Adjustment and anchoring instances (cb_01, cb_07) are placed at different decision points with distinct evidence sources (automated severity score vs. legacy budget estimate)",
      "Decision points 1, 2, and 3 each host two distinct biases with different reasoning operations and evidence sources, satisfying the shared-decision-point distinctiveness rule",
      "No decision point hosts more than two instances of any single bias",
      "No bias names, definitions, or explanations appear in planned interview text; only behavioral manifestations are specified",
      "Each instance has a plausible non-bias interpretation to avoid mechanical bias-proof consequences",
      "Exactly four decision points are planned, each with at least three alternatives",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Narrative content across 4 phases is scoped to fit within 1,215-1,485 words without repetitive exposition"
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
