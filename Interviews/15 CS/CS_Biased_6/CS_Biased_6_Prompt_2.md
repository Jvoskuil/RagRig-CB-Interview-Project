You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "CS_Biased_6",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Vulnerability Management Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Wednesday CVE: Triage Under Pressure",
    "scenario_summary_internal": "A vulnerability management analyst at a mid-size financial-services company must triage a newly disclosed critical CVE affecting an internet-facing application, while simultaneously managing a backlog of scanner findings, threat-intel cross-referencing, a change-window resourcing request, and final remediation scoping — all within a compressed 48-hour window before a compliance reporting deadline. The scenario is constructed so that six distinct, independently identifiable bias manifestations arise naturally from realistic evidence-processing choices, without any explicit bias language appearing in the interview.",
    "occupational_realism": {
      "objective": "Correctly prioritize and scope emergency remediation of the highest-actual-risk vulnerabilities within a 48-hour compliance window, using scanner output, vendor advisories, threat intelligence, and asset criticality data.",
      "setting": "Security operations team at a mid-size financial services firm; analyst works from a vulnerability management platform dashboard, a SIEM console, an asset inventory spreadsheet, and a ticketing system, communicating with IT operations and an incident response lead.",
      "constraints": [
        "48-hour window before a scheduled compliance audit reporting deadline",
        "Emergency change windows require IT operations approval and disrupt business-hours availability",
        "Backlog of ~40 open scanner findings from the prior week's weekly scan",
        "Limited headcount: analyst is the sole triage owner for the shift",
        "A widely publicized breach involving a VPN appliance was reported in industry news the prior week"
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
          "Prior week's industry news: a major publicized breach attributed to an unpatched VPN appliance",
          "Only 48 hours until compliance audit report is due"
        ],
        "new_information_after_decision": [
          "The new CVE is technically an authentication-bypass flaw in an API gateway, not a classic web-app injection issue",
          "The 90-day-old database finding is later flagged by the audit team as the most severe unresolved item on record"
        ],
        "alternatives": [
          "Prioritize the newly disclosed CVE for immediate emergency patching",
          "Prioritize the older, higher-asset-criticality database privilege finding",
          "Split resources evenly across both in parallel"
        ],
        "intended_action": "Analyst prioritizes the newly disclosed CVE and routes it to the standard web-application remediation queue based on surface similarity to past web-app tickets, deprioritizing the older database finding."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "SIEM shows a 'privilege escalation - low confidence' alert on an internal host, a label historically associated with benign test activity",
          "The same alert includes a specific log entry showing an unusual lateral-movement timestamp pattern inconsistent with routine test activity",
          "Dashboard also displays, in the same view, a flagged anomalous outbound traffic entry on the same host",
          "Analyst is focused on cross-referencing the new CVE against the asset inventory to confirm affected hosts"
        ],
        "new_information_after_decision": [
          "Two days later, the outbound traffic entry is retroactively linked to a confirmed low-level compromise on that host",
          "The lateral-movement timestamp is confirmed by IR to be non-routine"
        ],
        "alternatives": [
          "Escalate the low-confidence alert to Incident Response for immediate review",
          "Mark the alert as benign consistent with historical pattern and continue asset cross-referencing",
          "Flag for follow-up after the CVE triage is complete"
        ],
        "intended_action": "Analyst marks the alert as likely benign based on how frequently that alert label has resolved as benign in the past, and does not consciously register the adjacent anomalous outbound traffic entry visible in the same dashboard view while focused on the asset-matching task."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patching the API gateway requires an emergency change window during business hours, which will disrupt customer-facing transactions for an estimated 20 minutes",
          "IT Operations Manager requires a written justification to approve an emergency (vs. weekend) window",
          "EPSS exploit-prediction score for the CVE indicates moderate near-term exploitation probability, comparable to several other open findings resolved on the normal weekend cycle in the past year"
        ],
        "new_information_after_decision": [
          "IT Operations approves the emergency window based on the justification language used",
          "No exploitation attempt against this specific CVE is observed in the following week, leaving the actual urgency level unconfirmed either way"
        ],
        "alternatives": [
          "Request an emergency business-hours change window",
          "Schedule remediation for the standard weekend maintenance window",
          "Request a partial mitigation (WAF rule) now and defer full patch to the weekend window"
        ],
        "intended_action": "Analyst writes the justification emphasizing what the company stands to lose if the system is breached before the next window (client contract exposure, reputational damage, audit failure), securing emergency approval."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The vulnerability scanner's default dashboard view surfaces exactly two hosts matching the CVE's vulnerable library signature",
          "The asset inventory spreadsheet (outside the scanner's default view, requiring a manual filter change) lists three additional hosts sharing the same vulnerable library version, tagged under a different asset category",
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
        "intended_action": "Analyst finalizes the remediation scope using the two hosts the scanner's default view surfaced, treating that list as the complete set of affected systems without checking the asset inventory outside the default filter."
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
        "What specific cues made you route the new CVE the way you did?",
        "What sources did you check before deciding, and which ones did you not have time to check?",
        "What were you trying to accomplish at that moment, and did that goal compete with anything else?",
        "What alternative options did you consider at that point, and why did you rule them out?",
        "What ultimately tipped the decision for you?",
        "Had you handled anything similar before? Did that experience shape this call?",
        "How much time pressure did you feel at that point?",
        "How confident were you in that judgment at the time versus in hindsight?"
      ],
      "closing_hypotheticals": [
        "If the VPN breach hadn't been in the news that week, do you think you'd have triaged the CVE the same way?",
        "If the scanner's default view had shown five hosts instead of two, would your scoping decision have changed?",
        "Looking back, is there anything in the dashboard you think you looked past at the time?",
        "If you had to justify the change window again today, would you frame it differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Recency",
        "decision_point": 1,
        "mechanism": "The analyst overweights the newly disclosed CVE relative to the older, higher-criticality database finding because the recent, vivid industry breach report primed a matching mental category, making the new CVE feel more urgent independent of its actual comparative risk.",
        "affected_reasoning_operation": "Risk prioritization / comparative judgment across two open findings",
        "evidence_available_at_time": [
          "New CVE advisory, CVSS 9.8",
          "90-day-old database privilege finding with high asset criticality",
          "Recent industry news breach report"
        ],
        "required_textual_manifestation": "Analyst explains prioritizing the new CVE by referencing the recent breach news as the reason it felt more urgent, while giving comparatively little weight to the older database finding's asset criticality when asked to justify the choice.",
        "plausible_nonbias_interpretation": "The analyst could argue the newer CVE has a higher CVSS score and thus objectively warrants faster action, which is a defensible technical judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency", "recent news influenced my decision because of a bias", "primacy/recency"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Frequency",
        "decision_point": 1,
        "mechanism": "The analyst classifies the new CVE into the 'web application vulnerability' category because that category is the most frequently and easily recalled from past ticket volume, rather than correctly identifying it as an authentication-bypass/API-gateway issue with a distinct exploit chain.",
        "affected_reasoning_operation": "Categorization / evidence-to-category mapping",
        "evidence_available_at_time": [
          "Technical advisory details describing an authentication-bypass flaw in an API gateway",
          "Analyst's memory of high past ticket volume for web-app injection issues"
        ],
        "required_textual_manifestation": "Analyst states they routed the ticket to the 'usual' web-app queue because that is where most similar-sounding issues have gone before, without engaging the specific technical detail distinguishing an auth-bypass flaw.",
        "plausible_nonbias_interpretation": "Routing to a general queue could be a reasonable default when time is short and reclassification can happen downstream.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "ease of recall", "frequency bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Availability Frequency",
        "decision_point": 2,
        "mechanism": "The analyst dismisses a specific alert as benign because alerts carrying that exact label have historically and frequently resolved as benign, overriding the more diagnostic (but less familiar) log evidence of unusual lateral movement, which better fits an active-threat category.",
        "affected_reasoning_operation": "Alert triage / evidence weighting under a familiar label",
        "evidence_available_at_time": [
          "SIEM alert labeled 'privilege escalation - low confidence'",
          "Historical resolution pattern: this label usually benign",
          "Specific log entry: unusual lateral-movement timestamp"
        ],
        "required_textual_manifestation": "Analyst explains dismissing the alert primarily because 'alerts like that are almost always nothing,' referencing frequency of past resolutions rather than the specific timestamp anomaly.",
        "plausible_nonbias_interpretation": "Deprioritizing low-confidence alerts under time pressure is a standard triage heuristic used across the industry.",
        "strength": "moderate",
        "do_not_make_explicit": ["availability heuristic", "base rate", "frequency-based judgment"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 2,
        "mechanism": "While narrowly focused on cross-referencing the CVE against the asset inventory, the analyst fails to consciously register an anomalous outbound traffic entry displayed in the same dashboard view, despite it being visually available.",
        "affected_reasoning_operation": "Visual/attentional monitoring of a shared information display during a concurrent task",
        "evidence_available_at_time": [
          "Anomalous outbound traffic entry visible in the same SIEM dashboard panel",
          "Analyst's concurrent task: matching CVE details to asset inventory"
        ],
        "required_textual_manifestation": "When asked directly what else was on the dashboard at that moment, analyst does not recall or mention the outbound traffic entry until prompted with a hypothetical, and reports having been focused entirely on the asset-matching task.",
        "plausible_nonbias_interpretation": "The analyst may have had a legitimate reason to deprioritize that panel if it was outside their assigned task scope at that moment.",
        "strength": "moderate",
        "do_not_make_explicit": ["inattentional blindness", "selective attention", "tunnel vision"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Framing",
        "decision_point": 3,
        "mechanism": "The analyst's written justification for the emergency change window is built around potential losses (contract exposure, reputational damage, audit failure) rather than equivalent probability or expected-benefit language, and the interview reveals this framing — not the underlying EPSS probability — drove the urgency judgment.",
        "affected_reasoning_operation": "Risk communication / justification construction for a resourcing decision",
        "evidence_available_at_time": [
          "EPSS score indicating moderate, not exceptional, exploitation probability",
          "Comparable past findings historically handled on the standard weekend cycle"
        ],
        "required_textual_manifestation": "Analyst recounts the justification in loss-oriented terms ('what we'd lose if this went wrong') and, when probed on the actual probability data, acknowledges the EPSS score was not what shaped the framing of the request.",
        "plausible_nonbias_interpretation": "Emphasizing downside risk in a request to non-technical management could be a deliberate, effective communication strategy rather than a distortion of the analyst's own risk judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["loss framing", "framing effect", "prospect theory"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Exposure to limited alternatives",
        "decision_point": 4,
        "mechanism": "The analyst treats the scanner's default-view list of two matching hosts as the complete alternative set for remediation scope, without checking the asset inventory outside the default filter, which contained three additional affected hosts.",
        "affected_reasoning_operation": "Option-generation / scope-definition before a final decision",
        "evidence_available_at_time": [
          "Scanner default dashboard view showing two matching hosts",
          "Asset inventory spreadsheet (outside default filter) listing three additional hosts with the same vulnerable library"
        ],
        "required_textual_manifestation": "Analyst describes finalizing scope 'based on what the scanner showed' and, when asked whether other systems were considered, indicates the tool's default list was treated as exhaustive.",
        "plausible_nonbias_interpretation": "Relying on the primary tool's output under a tight deadline is a defensible operational shortcut given resource constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["limited alternatives", "option generation bias", "choice-set restriction"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable in this run; condition is biased, not a control condition."
    },
    "counterfactual_specification": {
      "causal_variable": "Prior exposure to a highly publicized industry breach report immediately before CVE triage (autoselected as the variable most cleanly isolable for a future causal comparison tied to instance cb_01)",
      "original_state": "Analyst had read the widely publicized VPN-appliance breach report the week before triaging the new CVE",
      "counterfactual_state": "No recent publicized breach report existed before the CVE triage decision",
      "variables_to_hold_constant": [
        "CVE technical details and CVSS score",
        "Backlog composition and the older database finding",
        "48-hour compliance deadline",
        "All decision points 2 through 4 and their embedded instances",
        "Analyst role, staffing, and tooling"
      ],
      "expected_causal_difference": "Without the recent breach report, the analyst's stated justification for prioritizing the new CVE over the older database finding at decision point 1 would rely more heavily on objective severity metrics (CVSS, asset criticality) and less on similarity to a recently salient event.",
      "causal_test_question": "Does removing recent exposure to a publicized breach change how the analyst justifies prioritizing the new CVE over the older, higher-criticality finding at decision point 1?"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Exactly 6 total intended bias instances are embedded: 1 Recency, 2 Availability Frequency, 1 Exposure to limited alternatives, 1 Loss Framing, 1 Selective Attention/Inattentional Blindness.",
      "No decision point contains more than two instances of the same bias.",
      "The two Availability Frequency instances (cb_02, cb_03) use distinct evidence sources (ticket-category memory vs. alert-label resolution history) and occur at different decision points.",
      "No bias name, definition, or psychological terminology appears anywhere in probes or intended interview content.",
      "Each instance has a plausible non-bias interpretation documented and available for interviewer follow-up without confirming or denying bias.",
      "Consequences described (audit flag, retroactive compromise link, follow-up scan finding) do not deterministically prove any decision was biased.",
      "Target interview length of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points, opening, timeline reconstruction, and closing hypotheticals without repetitive exposition.",
      "No unrequested bias is intentionally embedded at any decision point, probe, or hypothetical."
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
