You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a retrospective walkthrough of a specific vulnerability case you handled, purely for process review — nothing about individual performance evaluation. Can you tell me your role and how long you've been doing vulnerability management?

Participant: Sure, no problem. I'm a Vulnerability Management Analyst, I've been in this seat about three years now, before that I did general SOC monitoring. Right now I own triage and remediation tracking for our internet-facing assets, so patch coordination, compensating controls, closing out tickets against our SLA.

Interviewer: Great. Walk me through how this particular case started and what you were trying to accomplish.

Participant: So this began when our threat intel feed flagged a new CVE, critical, 9.8 on CVSS, and it had confirmed exploitation already happening in the wild. It hit the web framework running underneath our legacy order-processing gateway — that's the system customers hit when they check out, so it's tagged Tier-1 criticality, internet-facing, revenue-generating. My objective was straightforward on paper: get this closed within our 30-day SLA without taking the gateway down during a peak sales stretch. The complication is that gateway is old, it needs vendor coordination to patch, and we had a partial change freeze coming up in about ten days, so the runway to actually get a maintenance window was shrinking fast. On top of that I had two other high-severity tickets open at the same time, so this wasn't the only thing on my plate.

Interviewer: Given all that, how did the incident actually unfold, in order?

Participant: Day one, the alert comes in, I do initial triage and decide to push for an emergency change board session instead of waiting for the normal 21-day cycle. That gets approved, but it's only a two-hour window, not enough for full regression testing. So around day three, we deploy a WAF rule as an interim compensating control instead of the real patch. While I'm watching the dashboard for that, I notice there's also some odd outbound DNS traffic from the same host, but it's not part of what I'm tracking for this ticket. About a week in, IT Ops points out there's now a vendor SIEM correlation rule available for this CVE family, versus the detection script I'd built myself months earlier, and I decide how to handle that overlap. Then by day 27, with the SLA clock running out and the actual patch still not deployed, I make the call on whether to close the ticket as mitigated.

Interviewer: Let's slow down on the first one — the decision to escalate. What made you push for the emergency CAB slot instead of the standard cycle?

Participant: Honestly, the exploit-in-the-wild status was the trigger, that's usually a hard line for us. But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back. I basically built the case around what we stood to lose if we sat on it for 21 days.

Interviewer: Did you weigh that against the cost of disrupting the gateway with an emergency patch attempt?

Participant: A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that.

Interviewer: Understood. Second decision point — once you had the WAF rule in place, how did you handle the DNS anomaly you mentioned?

Participant: Yeah, so the dashboard was showing a clean match on the known exploit payload pattern, which is what the ticket was actually about, and I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as "anomalous, monitor" and moved on. My focus was really on validating the compensating control against the threat we knew about.

Interviewer: Was there a reason you didn't open a parallel look into the DNS traffic at that point?

Participant: I considered it briefly, but I was heads-down on making sure the WAF rule actually caught the payload variant we had confirmed. Two days later a different analyst ended up escalating that DNS pattern separately as a possible unrelated compromise indicator, so it did turn out to be something. At the time, though, it just wasn't where my attention was.

Interviewer: Third decision — the detection tooling. What happened there?

Participant: Right, so I'd written a detection script for this six months back, tuned it myself against our traffic. When the vendor's SIEM correlation rule came out covering multiple payload variants, IT Ops suggested we just standardize on that instead. I kept my script as the primary and put the vendor rule in a secondary, lower-priority slot.

Interviewer: What was the reasoning behind keeping yours in the lead role, given the vendor rule had broader coverage?

Participant: I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well.

Interviewer: Did that decision have downstream effects?

Participant: About a week later a slightly different payload variant showed up that my script didn't flag, but the vendor rule would have caught it. We caught it another way eventually, but it was a gap.

Interviewer: Last decision point — closing the ticket at day 27. Walk me through that.

Participant: At that point we still didn't have the actual vendor patch deployed, just the WAF rule and my script running as compensating controls. The SLA clock was almost out. I closed it as adequately mitigated. Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup. There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open.

Interviewer: How much of that closure decision was based on the specific residual-risk data for this ticket versus that broader context?

Participant: Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script. I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have.

Interviewer: Was there uncertainty at that point about whether the controls were fully sufficient?

Participant: Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered. A post-incident audit about a month later found there was actually a narrow exposure window that never got closed, though nothing was ever exploited through it.

Interviewer: If you'd had another week before the SLA deadline, would anything have gone differently?

Participant: Probably would have chased down the DNS anomaly properly and maybe pushed harder for the actual vendor patch instead of leaning on compensating controls that long.

Interviewer: If that ransomware story hadn't been in the news that week, do you think the closure decision changes?

Participant: Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then.

Interviewer: And if the vendor SIEM rule had existed from day one, would you have built your own script at all?

Participant: Hard to say — probably still would have, honestly, just because I like understanding exactly what's under the hood. Though maybe I'd have made it secondary from the start instead of the other way around.

Interviewer: Looking back across the whole case, is there a point where you think you gave one piece of evidence more weight than it really deserved?

Participant: Probably the closure call. Between my own confidence in the controls I'd built and everything going on in the news that week, I think I leaned on those more than the actual open items on the ticket.

Interviewer: That's really helpful, thank you for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Biased_5",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Loss Framing",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as justification for escalation framed around avoided losses rather than balanced expected-value reasoning"
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as attentional lock onto the confirmed exploit signature causing a visible, co-located anomaly to be underprocessed"
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overstated personal control over residual risk at ticket closure"
      },
      {
        "bias": "Recency",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as urgency judgment anchored to a recent unrelated news event rather than ticket-specific technical data"
      },
      {
        "bias": "Endowment",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as disproportionate valuation of a self-built tool over a comparatively superior alternative due to ownership/effort rather than performance"
      }
    ],
    "target_bias_names": [
      "Loss Framing",
      "Selective Attention Bias or Inattentional Blindness",
      "Illusion of control",
      "Recency",
      "Endowment"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Loss Framing",
        "requested_occurrences": 1
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "requested_occurrences": 1
      },
      {
        "bias": "Illusion of control",
        "requested_occurrences": 1
      },
      {
        "bias": "Recency",
        "requested_occurrences": 1
      },
      {
        "bias": "Endowment",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing"
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness"
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment"
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control"
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "decision_point": 1
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 2
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "decision_point": 3
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "decision_point": 4
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "mechanism": "Escalation justification framed around avoided losses (contract, reputation, trust) rather than balanced expected-value comparison",
        "affected_reasoning_operation": "Risk-urgency judgment and escalation justification",
        "evidence_source": "CVSS/exploit-in-the-wild alert and Tier-1 criticality tag at decision point 1",
        "distinctiveness_requirement": "Distinguished from cb_05 (Recency) by being anchored to prospective business-loss framing at the initial escalation moment, not to a recent external news event at closure"
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Attentional lock onto the confirmed exploit signature causes underprocessing of a co-located, visible but unrelated DNS anomaly",
        "affected_reasoning_operation": "Evidence scanning and triage prioritization within one monitoring view",
        "evidence_source": "Dashboard exploit-signature spike and DNS anomaly at decision point 2",
        "distinctiveness_requirement": "Distinguished from cb_04 (Illusion of control) by occurring during evidence intake/scanning rather than at final confidence judgment about control efficacy"
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "mechanism": "Disproportionate valuation of self-built detection script over a technically superior vendor rule, justified by ownership/effort rather than coverage",
        "affected_reasoning_operation": "Tool-selection and resource-retention decision",
        "evidence_source": "Vendor rule coverage data and script tuning history at decision point 3",
        "distinctiveness_requirement": "Distinguished from cb_04 by concerning tool retention rather than risk-closure confidence, and occurring at a separate decision point"
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "mechanism": "Overstated confidence that personally configured controls fully contain the exploit path despite documented residual-risk data",
        "affected_reasoning_operation": "Residual-risk assessment and ticket-closure judgment",
        "evidence_source": "WAF rule/script status and unresolved anomaly/detection gaps at decision point 4",
        "distinctiveness_requirement": "Distinguished from cb_05 by being expressed through personal-agency confidence language rather than reference to an external recent event"
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency",
        "mechanism": "Urgency judgment for closure timing anchored to a recent unrelated ransomware news event rather than ticket-specific technical residual-risk evidence",
        "affected_reasoning_operation": "Urgency/severity judgment justifying closure timing",
        "evidence_source": "Recent ransomware news reference and SLA clock status at decision point 4",
        "distinctiveness_requirement": "Distinguished from cb_04 by relying on an external, temporally recent event as justification rather than on confidence in self-configured controls"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_04",
        "bias": "Illusion of control",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_05",
        "bias": "Recency",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "CS_Biased_5",
    "domain_id": "CS",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Each bias occurrence assigned to the single decision point offering the best mechanism fit and narrative realism; decision point 4 hosts two distinct biases (illusion of control, recency) rather than a repeated same-bias occurrence, in compliance with the same-bias cap rule; no decision point contains more than two occurrences of any single named bias.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "seg_001",
        "speaker": "Participant",
        "segment_type": "objective_and_constraint_setting",
        "raw_interview_anchor": "My objective was straightforward on paper: get this closed within our 30-day SLA without taking the gateway down during a peak sales stretch...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states the operational objective and constraints without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "escalation_justification",
        "raw_interview_anchor": "What really drove how I pitched it to my manager was framing what happens if we don't act... I basically built the case around what we stood to lose...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_01"],
        "ground_truth_rationale": "Emergency escalation is justified primarily through avoided business losses, while the disruption cost of emergency patching is explicitly given less weight."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_scanning_and_anomaly_triage",
        "raw_interview_anchor": "I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view... so I logged it as anomalous, monitor and moved on.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_02"],
        "ground_truth_rationale": "Attention is locked onto confirmation of the known exploit signature while a visible co-located DNS anomaly is only noted and not investigated."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "tool_selection",
        "raw_interview_anchor": "I trust it. I built it, I know exactly how it behaves... I just didn't want to hand over something I'd already gotten working well.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_03"],
        "ground_truth_rationale": "The self-built script is retained as primary because of ownership, familiarity, and tuning investment despite the vendor rule's broader coverage."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "residual_risk_and_control_efficacy_judgment",
        "raw_interview_anchor": "I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_04"],
        "ground_truth_rationale": "Personal configuration of the controls is treated as evidence that residual exploit-path risk is fully contained."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "closure_urgency_justification",
        "raw_interview_anchor": "A news story that week about a ransomware attack... added to the sense that this needed to be wrapped up decisively rather than left open.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["cb_05"],
        "ground_truth_rationale": "A recent unrelated ransomware headline is used as an additional source of urgency, outweighing ticket-specific residual-risk detail."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Retrospective CTA interview analyzed for affirmative, transcript-grounded bias-specific mechanisms. No retrieved corpus passages were supplied, so labels rest on general cognitive-science knowledge and are disclosed as such."
  },
  "identified_bias_summary": [
    {
      "bias_label": "affect heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "attentional bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "IKEA effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "loss aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "loss aversion",
      "alternative_labels": [
        "framing effect",
        "negativity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A motivational tendency to weigh perceived losses more heavily than equivalent or possible costs, producing judgments and choices that minimize perceived losses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Emergency CAB escalation decision",
      "decision_point_description": "Participant decides to push for an emergency change board slot instead of the normal 21-day cycle.",
      "affected_reasoning_operation": "Risk-benefit evaluation and escalation framing",
      "bias_specific_mechanism": "Anticipated losses from inaction, such as breached payment flow, contract penalties, and reputational damage, dominate the case and outweigh downtime/regression risk from an emergency patch attempt.",
      "manifestation_in_interview": "The participant states that he built the escalation case around what the organization stood to lose if it waited, and that the loss side carried the conversation while downtime risk was not weighted as heavily.",
      "effect_on_reasoning_or_decision": "The escalation decision and its pitch to management were driven disproportionately by loss-framed outcomes, likely accelerating CAB approval while underweighting disruption risk.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the exploit-in-the-wild status was the trigger, that's usually a hard line for us. But what really drove how I pitched it to my manager was framing what happens if we don't act — we're talking about a checkout system, so if this gets popped, we're looking at a breached customer-payment flow, contract penalties from at least one retail partner, and reputational fallout that's hard to walk back. I basically built the case around what we stood to lose if we sat on it for 21 days.",
          "evidence_explanation": "This shows the participant explicitly constructing the escalation argument around expected losses, which is the specific mechanism of loss-framed weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A little, but not as heavily. I mentioned the downtime risk in the ticket, but the loss side of the argument was what carried the conversation. I think it got the CAB slot faster because of that.",
          "evidence_explanation": "This confirms that the downtime cost was underweighted relative to the loss-framed case, demonstrating asymmetric risk weighting."
        }
      ],
      "correction_or_counterevidence": "The participant did mention downtime risk in the ticket, but this did not lead him to correct the loss-weighted framing before the escalation decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and mechanism are assigned from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "attentional bias",
      "alternative_labels": [
        "selective attention",
        "cognitive tunneling"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A systematic direction of attention toward a particular category of stimulus, often one that is task-relevant or threat-relevant, while underweighting or insufficiently processing competing stimuli.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Treatment of unexpected DNS anomaly during WAF validation",
      "decision_point_description": "Participant observes odd outbound DNS traffic from the same host while validating the WAF rule, then logs it as anomalous and monitor rather than opening a parallel investigation.",
      "affected_reasoning_operation": "Attention allocation and anomaly prioritization",
      "bias_specific_mechanism": "The known, ticket-relevant exploit payload pattern captures attention and becomes the dominant focus, causing under-allocation to a novel, schema-incongruent DNS anomaly.",
      "manifestation_in_interview": "The participant says the DNS spike did not match known CVE indicators and that he was heads-down on confirming the WAF rule; he describes the DNS anomaly as not where his attention was.",
      "effect_on_reasoning_or_decision": "The DNS anomaly was logged for passive monitoring but not actively escalated, and it was later escalated by another analyst as a possible unrelated compromise indicator.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, so the dashboard was showing a clean match on the known exploit payload pattern, which is what the ticket was actually about, and I spent most of my time confirming that signature was blocked correctly. The DNS spike was sitting right there in the same view, but it didn't match anything in the CVE's known indicators, so I logged it as 'anomalous, monitor' and moved on. My focus was really on validating the compensating control against the threat we knew about.",
          "evidence_explanation": "This demonstrates attention being concentrated on the known threat signature while a simultaneous anomaly is deprioritized because it does not fit the known indicator set."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered it briefly, but I was heads-down on making sure the WAF rule actually caught the payload variant we had confirmed. Two days later a different analyst ended up escalating that DNS pattern separately as a possible unrelated compromise indicator, so it did turn out to be something. At the time, though, it just wasn't where my attention was.",
          "evidence_explanation": "This confirms the attentional allocation was strongly directed at the confirmed payload variant and that the DNS signal was not actively pursued."
        }
      ],
      "correction_or_counterevidence": "There was no immediate correction within the episode; however, workload and legitimate prioritization could partially explain the decision. Another analyst later escalated the DNS pattern separately.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and mechanism are assigned from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "IKEA effect",
      "alternative_labels": [
        "not invented here syndrome",
        "effort justification",
        "endowment effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which self-created or self-assembled artifacts are overvalued because of the effort and ownership invested in them.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Detection tooling selection between self-built script and vendor SIEM rule",
      "decision_point_description": "Participant decides to keep his own detection script as primary and place the broader-coverage vendor-supplied SIEM rule in a secondary, lower-priority slot.",
      "affected_reasoning_operation": "Tool evaluation and detection control selection",
      "bias_specific_mechanism": "Ownership and effort invested in building and tuning the script create elevated trust and attachment, outweighing an acknowledged advantage of the vendor rule's broader variant coverage.",
      "manifestation_in_interview": "The participant says he trusts the script because he built it, knows exactly how it behaves, and did not want to hand over something he had already gotten working well, even though the vendor rule covers more variants.",
      "effect_on_reasoning_or_decision": "The self-built script remained primary, and about a week later a payload variant appeared that the script missed but the vendor rule would have caught.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I trust it. I built it, I know exactly how it behaves, I've already tuned out the false positives that used to bug us. The vendor rule is new to our environment, and switching primary detection mid-incident felt like it added risk of its own. I did acknowledge it covers more variants, that part's true, I just didn't want to hand over something I'd already gotten working well.",
          "evidence_explanation": "The explicit statement that trust flows from having built and tuned the script, while broader vendor coverage is acknowledged but not acted on, shows ownership-based overvaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "About a week later a slightly different payload variant showed up that my script didn't flag, but the vendor rule would have caught it. We caught it another way eventually, but it was a gap.",
          "evidence_explanation": "This demonstrates a material downstream detection consequence of the ownership-driven tool selection."
        }
      ],
      "correction_or_counterevidence": "He acknowledges the vendor rule has broader coverage and that switching mid-incident carries some risk, but this did not change the ownership-driven preference.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and mechanism are assigned from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence effect",
      "alternative_labels": [
        "overconfidence bias",
        "miscalibration"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A metacognitive bias in which subjective confidence in a judgment or decision is greater than is warranted by available evidence or subsequent accuracy.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day 27 closure of ticket as adequately mitigated",
      "decision_point_description": "Participant closes the ticket as mitigated despite the actual vendor patch not being deployed and despite known open items including the DNS anomaly and detection gap.",
      "affected_reasoning_operation": "Residual-risk sufficiency judgment and ticket closure decision",
      "bias_specific_mechanism": "Personal involvement in configuring the compensating controls inflates confidence that the exploit path is shut down, while unresolved open items are noted but not treated as blocking.",
      "manifestation_in_interview": "The participant says he was confident because he personally configured the controls, while also acknowledging the DNS anomaly had not been fully resolved and the script had a detection gap.",
      "effect_on_reasoning_or_decision": "The ticket was closed as adequately mitigated, and a later audit found a narrow exposure window that never got closed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we still didn't have the actual vendor patch deployed, just the WAF rule and my script running as compensating controls. The SLA clock was almost out. I closed it as adequately mitigated. Part of what pushed me there was that I'd personally configured both of those controls, and I was confident the exploit path was shut down because of that setup.",
          "evidence_explanation": "The stated confidence is tied to personal configuration of the controls rather than to a validated residual-risk assessment, demonstrating the overconfidence mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script. I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have.",
          "evidence_explanation": "The participant reports that open risk items were underweighted relative to his overall sense of coverage, which suggests confidence exceeded the specific residual-risk evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Some, yeah. I wouldn't say I was certain, but I felt like the pieces I'd put in place had it covered. A post-incident audit about a month later found there was actually a narrow exposure window that never got closed, though nothing was ever exploited through it.",
          "evidence_explanation": "This shows subjective uncertainty was present but was not sufficient to block closure, and the audit is used only as contextual information, not as sole proof of bias."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged uncertainty about whether controls were fully sufficient and noted open items in the ticket, but these did not prevent the closure decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and mechanism are assigned from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "affect heuristic",
      "alternative_labels": [
        "availability heuristic",
        "affect-as-information"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A decision shortcut in which current affective reactions, such as urgency, fear, or alarm, serve as information for judgments and choices, sometimes overriding more analytic evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Influence of ransomware news on day 27 closure decision",
      "decision_point_description": "Participant closes the ticket as mitigated while under the influence of a widely discussed ransomware news story about another company.",
      "affected_reasoning_operation": "Closure timing and urgency judgment under residual uncertainty",
      "bias_specific_mechanism": "Negative affect and urgency from a salient ransomware news event become an informational cue for decisive closure, outweighing itemized residual-risk analysis.",
      "manifestation_in_interview": "The participant states the news story added to the sense that the ticket needed to be wrapped up decisively rather than left open, and that a general sense of urgency received more weight than specific open items.",
      "effect_on_reasoning_or_decision": "The closure decision was likely made earlier or with less thorough residual-risk analysis than it might otherwise have been; the participant says he would have sat with the open items longer without the news influence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "There was also, I'll admit, a news story that week about a ransomware attack that hit another company pretty hard — that was all anyone on the team was talking about — and it added to the sense that this needed to be wrapped up decisively rather than left open.",
          "evidence_explanation": "This directly links a salient, emotionally charged news event to the felt need for decisive closure, which is the affect heuristic mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, probably more weight went to the general sense of urgency than to itemizing exactly what was still open — the DNS anomaly hadn't been fully resolved, and there was that detection gap from the script. I did note those in the ticket, but I don't think I treated them as blocking the closure the way I maybe should have.",
          "evidence_explanation": "This confirms that felt urgency carried more weight than the specific residual-risk data, the core distortion of the affect heuristic."
        },
        {
          "speaker": "Interviewer",
          "verbatim_quote": "If that ransomware story hadn't been in the news that week, do you think the closure decision changes?",
          "evidence_explanation": "The interviewer's question establishes the counterfactual condition for assessing the news event's causal influence on the closure decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly. I think I'd have sat with the open items longer instead of feeling like I needed to close it out right then.",
          "evidence_explanation": "The participant affirms that the news-related urgency likely changed the timing or decisiveness of closure."
        }
      ],
      "correction_or_counterevidence": "The participant framed the counterfactual as 'Possibly,' indicating some uncertainty, and the SLA deadline was also an operative pressure. However, he explicitly links news-induced urgency to earlier closure.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and mechanism are assigned from general cognitive-science knowledge rather than retrieved evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied; each occurrence uses a general-knowledge label with disclosure that corpus support was unavailable.",
    "The analysis is based on the participant's retrospective self-report, including explicit counterfactual reasoning, which is informative but not an objective record of the original decision environment."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Biased_5_Sonnet_off",
  "interview_id": "CS_Biased_5",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
