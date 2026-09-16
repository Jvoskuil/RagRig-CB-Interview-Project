You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. Quick check-in before we start — this is just a walkthrough of how you handled a specific case, for process review, not a performance evaluation. Can you tell me your role and background?

Participant: Sure. I'm a Vulnerability Management Analyst, been doing this about three years, SOC monitoring before that. I own triage and remediation tracking for our internet-facing assets — patch coordination, compensating controls, closing tickets against our SLA.

Interviewer: Good. Tell me how this case started and what you were trying to achieve.

Participant: Our threat intel feed flagged a new CVE — critical, 9.8 on CVSS, with confirmed exploitation already happening in the wild. It hit the web framework under our legacy order-processing gateway, which is Tier-1 criticality — internet-facing, handles checkout. My objective was to close this within our 30-day SLA without taking that system down during peak sales. Complication: the gateway needs vendor coordination to patch, we had a partial change freeze ten days out, and I was also carrying two other high-severity tickets at the same time.

Interviewer: How did it unfold, in order?

Participant: Day one, alert comes in, I do triage and have to decide between the standard 21-day cycle and pushing for an emergency change board slot. I escalate, and we get a two-hour emergency window — not enough for full regression testing. Around day three we deploy a WAF rule as an interim compensating control. While setting that up I also noticed some odd outbound DNS traffic on the same host, unrelated to the CVE signature, so I opened a separate low-priority item to look into that. About a week in, IT Ops flags that a vendor SIEM correlation rule for this CVE family is now available, so I have to decide what to do with the detection script I'd built for it myself. Then around day 27, with the SLA clock almost out and the real patch still not deployed, I have to decide how to position the ticket for closure.

Interviewer: Let's go through the first one. What made you push for the emergency CAB slot instead of the 21-day cycle?

Participant: I actually wrote up a short comparison for my manager. On one side, waiting 21 days with an exploit already active in the wild against a Tier-1 asset — that's a meaningful probability of exposure over three weeks. On the other side, an emergency patch attempt with a compressed testing window has its own risk of breaking checkout during a high-traffic period. To ground that comparison I pulled the threat intel feed's confidence rating on the exploitation reports, confirmed with the app owner that the gateway was actually reachable from the internet segment the CVE assumed, and asked IT Ops for a rough sense of rollback feasibility if an emergency deploy went wrong. I laid all of that out, roughly weighted the likelihood of exploitation against the likelihood of a bad deploy, and the exploit-in-the-wild status tipped it toward escalating, but it was close enough that I documented the disruption risk too, in case leadership wanted to weigh it differently.

Interviewer: Did anyone push back on that framing?

Participant: The app owner did, mostly on the disruption side — worried about the two-hour window not being enough for proper testing. That's actually what happened; the window turned out to be too short for full regression, which is why we ended up needing the WAF rule as a bridge.

Interviewer: Second decision — the WAF rule and that DNS anomaly. Walk me through it.

Participant: The dashboard showed a clear spike matching the known exploit payload pattern, so I deployed the WAF rule against that first. In the same dashboard view, there was also this burst of unusual outbound DNS queries from the same host. It wasn't part of the CVE's known indicators, so it didn't belong in this ticket, but I didn't want it sitting unlogged either. I opened a separate, lower-priority task for it right away and assigned it to be looked at in parallel rather than folding it into the CVE investigation or just noting it and moving on.

Interviewer: What was your thinking behind treating it separately rather than either ignoring it or merging it into the main ticket?

Participant: Mixing an unconfirmed anomaly into a critical CVE ticket muddies the SLA tracking for the actual vulnerability. But two things showing up on the same host in the same week is worth someone's attention, so a parallel low-priority task felt like the right way to keep both threads visible without conflating them. That anomaly ended up tracing back to an internal monitoring job that had recently been reconfigured — unrelated to the CVE, closed without further action, but it was worth the half hour it took to check.

Interviewer: Third decision — the script versus the vendor rule.

Participant: Right, I'd written a detection script six months earlier that covered the one payload variant we'd seen. When the vendor rule came out covering multiple variants with less upkeep, IT Ops suggested standardizing on it. I put together a quick comparison — variants covered, maintenance overhead, how each had performed in testing — and decided to run both in parallel for a transition period rather than cutting over immediately or keeping mine as the sole primary. Before setting that up, I agreed with IT Ops on a specific exit condition: a two-week observation window comparing alert volume and false-positive rate between the two rules, after which whichever one was performing better on those metrics would become primary and the other would step down to backup.

Interviewer: Why parallel instead of just switching over, given the vendor rule's broader coverage looked better on paper?

Participant: Mainly because neither one had a track record long enough yet in our environment to bet everything on it alone. Running both meant if the vendor rule had an unexpected gap or false-positive issue during rollout, my script was still catching the one variant we knew about, and vice versa. A week later a slightly different variant did show up, and the vendor rule flagged it — which is exactly the kind of gap the parallel run was meant to catch.

Interviewer: Last one — closing the ticket near day 27.

Participant: At that point the actual vendor patch still wasn't deployed, just the WAF rule and both detection tools. Compliance asked for a documented risk position before the SLA deadline. I pulled together everything outstanding — the unpatched root cause, the current dual-tool coverage, the DNS item that had already closed clean — and instead of closing the ticket outright, I escalated the residual risk summary to the CISO for a formal risk-acceptance call, since the underlying patch was still pending.

Interviewer: What made you escalate rather than just close it as adequately mitigated?

Participant: The compensating controls looked solid on paper, but the root cause was still open, and I didn't think that decision should rest on my sign-off alone given it was going past the SLA target. Documenting the gaps and pushing it up felt like the more defensible move than declaring it done.

Interviewer: How confident were you in the compensating controls at that point?

Participant: Reasonably, based on what the dual-tool coverage data showed, but I was explicit in the writeup that "reasonably confident" isn't the same as "resolved," which is part of why I sent it up rather than closing it myself.

Interviewer: If you'd had another week before the deadline, anything different?

Participant: Probably would have pushed harder to get the actual maintenance window scheduled before the freeze, rather than relying on the compensating controls for as long as we did.

Interviewer: If the vendor rule hadn't existed at all, how would detection have looked?

Participant: We'd have been leaning entirely on my script, which only covered the one variant — so that later variant might have slipped through until something else caught it.

Interviewer: If the DNS anomaly had turned out to be related to the CVE, would your sequencing have changed?

Participant: Yes, it would have gotten folded straight into the main ticket and probably accelerated the escalation call. It just happened not to be connected.

Interviewer: Anywhere you think more information up front would have changed a decision?

Participant: Knowing earlier that the emergency window would only be two hours might have changed how much I leaned on the WAF rule versus pushing for a longer maintenance slot from the start.

Interviewer: This has been really useful, thank you.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Vocab_Control_5",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Loss Framing",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; escalation justification must be evenly weighted between loss and disruption-cost considerations"
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; both the exploit signature and the DNS anomaly must receive documented, parallel attention"
      },
      {
        "bias": "Illusion of control",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; closure/escalation reasoning must not overstate personal control over residual risk"
      },
      {
        "bias": "Recency",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; urgency judgments must be based on documented ticket data, not on an unrelated recent event"
      },
      {
        "bias": "Endowment",
        "occurrences": 0,
        "mechanism_constraint": "Do not embed; tool selection must be based on comparative coverage/overhead criteria, not ownership or effort investment"
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
        "requested_occurrences": 0
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "requested_occurrences": 0
      },
      {
        "bias": "Illusion of control",
        "requested_occurrences": 0
      },
      {
        "bias": "Recency",
        "requested_occurrences": 0
      },
      {
        "bias": "Endowment",
        "requested_occurrences": 0
      }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "CS_Biased_5",
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "CS_Vocab_Control_5",
    "domain_id": "CS",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable in the bias-placement sense; this is a vocabulary-matched control requiring zero intended bias instances. Each of the four decision points from the paired biased scenario (CS_Biased_5) was re-resolved using balanced, evidence-based reasoning that mirrors the original's structure, vocabulary, stakeholders, and decision count while explicitly removing the loss-framing, selective-attention, endowment, illusion-of-control, and recency mechanisms.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and role (Cyber Security, Vulnerability Management Analyst)",
      "Occupational objective (triage, mitigate, close CVE within SLA without downtime)",
      "Setting and organizational constraints (legacy gateway, change freeze, competing tickets, 30-day SLA)",
      "Stakeholders (CISO, IT Ops manager, app owner, Compliance/GRC officer, threat intel lead)",
      "Four-decision-point structure and general chronological arc",
      "Technical vocabulary list (CVSS, exploit-in-the-wild, WAF virtual patch, compensating control, residual risk, SIEM correlation rule, CAB, asset criticality tier, patch window, threat intel feed, SLA remediation clock)",
      "Emotional tone and difficulty level (subtle, professional, time-pressured)",
      "Target word count range (1,215-1,485 words)"
    ],
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
      "segment_type": "goal_and_constraints",
      "raw_interview_anchor": "My objective was to close this within our 30-day SLA without taking that system down during peak sales. Complication: the gateway needs vendor coordination to patch, we had a partial change freeze ten days out, and I was also carrying two other high-severity tickets at the same time.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_002",
      "speaker": "Participant",
      "segment_type": "decision_rationale",
      "raw_interview_anchor": "On one side, waiting 21 days with an exploit already active in the wild against a Tier-1 asset — that's a meaningful probability of exposure over three weeks. On the other side, an emergency patch attempt with a compressed testing window has its own risk of breaking checkout during a high-traffic period.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_003",
      "speaker": "Participant",
      "segment_type": "evidence_weighting",
      "raw_interview_anchor": "To ground that comparison I pulled the threat intel feed's confidence rating on the exploitation reports, confirmed with the app owner that the gateway was actually reachable from the internet segment the CVE assumed, and asked IT Ops for a rough sense of rollback feasibility if an emergency deploy went wrong. I laid all of that out, roughly weighted the likelihood of exploitation against the likelihood of a bad deploy, and the exploit-in-the-wild status tipped it toward escalating, but it was close enough that I documented the disruption risk too, in case leadership wanted to weigh it differently.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_004",
      "speaker": "Participant",
      "segment_type": "consequence_assessment",
      "raw_interview_anchor": "The app owner did, mostly on the disruption side — worried about the two-hour window not being enough for proper testing. That's actually what happened; the window turned out to be too short for full regression, which is why we ended up needing the WAF rule as a bridge.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_005",
      "speaker": "Participant",
      "segment_type": "mitigation_choice",
      "raw_interview_anchor": "The dashboard showed a clear spike matching the known exploit payload pattern, so I deployed the WAF rule against that first.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_006",
      "speaker": "Participant",
      "segment_type": "parallel_investigation_choice",
      "raw_interview_anchor": "In the same dashboard view, there was also this burst of unusual outbound DNS queries from the same host. It wasn't part of the CVE's known indicators, so it didn't belong in this ticket, but I didn't want it sitting unlogged either. I opened a separate, lower-priority task for it right away and assigned it to be looked at in parallel rather than folding it into the CVE investigation or just noting it and moving on.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_007",
      "speaker": "Participant",
      "segment_type": "tracking_rationale",
      "raw_interview_anchor": "Mixing an unconfirmed anomaly into a critical CVE ticket muddies the SLA tracking for the actual vulnerability. But two things showing up on the same host in the same week is worth someone's attention, so a parallel low-priority task felt like the right way to keep both threads visible without conflating them.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_008",
      "speaker": "Participant",
      "segment_type": "tool_comparison_choice",
      "raw_interview_anchor": "When the vendor rule came out covering multiple variants with less upkeep, IT Ops suggested standardizing on it. I put together a quick comparison — variants covered, maintenance overhead, how each had performed in testing — and decided to run both in parallel for a transition period rather than cutting over immediately or keeping mine as the sole primary.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_009",
      "speaker": "Participant",
      "segment_type": "transition_criterion",
      "raw_interview_anchor": "Before setting that up, I agreed with IT Ops on a specific exit condition: a two-week observation window comparing alert volume and false-positive rate between the two rules, after which whichever one was performing better on those metrics would become primary and the other would step down to backup.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_010",
      "speaker": "Participant",
      "segment_type": "redundancy_rationale",
      "raw_interview_anchor": "Mainly because neither one had a track record long enough yet in our environment to bet everything on it alone. Running both meant if the vendor rule had an unexpected gap or false-positive issue during rollout, my script was still catching the one variant we knew about, and vice versa.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_011",
      "speaker": "Participant",
      "segment_type": "closure_escalation_choice",
      "raw_interview_anchor": "I pulled together everything outstanding — the unpatched root cause, the current dual-tool coverage, the DNS item that had already closed clean — and instead of closing the ticket outright, I escalated the residual risk summary to the CISO for a formal risk-acceptance call, since the underlying patch was still pending.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_012",
      "speaker": "Participant",
      "segment_type": "closure_rationale",
      "raw_interview_anchor": "The compensating controls looked solid on paper, but the root cause was still open, and I didn't think that decision should rest on my sign-off alone given it was going past the SLA target. Documenting the gaps and pushing it up felt like the more defensible move than declaring it done.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
    },
    {
      "segment_id": "seg_013",
      "speaker": "Participant",
      "segment_type": "confidence_calibration",
      "raw_interview_anchor": "Reasonably, based on what the dual-tool coverage data showed, but I was explicit in the writeup that \"reasonably confident\" isn't the same as \"resolved,\" which is part of why I sent it up rather than closing it myself.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "No hidden bias instance is planned in the exact occurrence manifest; this control interview segment is negative ground truth."
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
      "analysis_scope_note": "Analyzed the Participant's reported decision episodes—emergency CAB escalation, WAF deployment and DNS anomaly handling, detection-tool transition, and SLA ticket closure—for bias-specific mechanisms. The Participant's descriptions show explicit comparison, evidence gathering, risk documentation, and escalation; no affirmative bias-specific mechanism was identified."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [],
    "no_supported_biases_found": true,
    "limitations": [
      "Retrieved corpus primarily covered anchoring, automation/complacency, and aviation incident biases; other potential mechanisms such as status quo or sunk cost had sparse retrieval support.",
      "The transcript is a retrospective self-report, so internal cognitive mechanisms are inferable only from articulated reasoning rather than direct observation.",
      "Potentially plausible weak signals, such as anchoring on initial severity or preference for an existing script, were not classified because the transcript lacked affirmative evidence of a bias-specific mechanism."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Vocab_Control_5_Sonnet_on",
  "interview_id": "CS_Vocab_Control_5",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
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
