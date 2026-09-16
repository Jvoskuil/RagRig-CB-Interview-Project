You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm — this is a voluntary conversation about how you handled the EDR replacement evaluation earlier this year, purely for internal process review. Nothing here affects performance evaluation. You're the Security Product/Vendor Evaluation Manager on that project, correct?

Participant: That's right. I led the vendor evaluation from shortlist through to the board recommendation.

Interviewer: Good. Let's start broad — what triggered this whole evaluation?

Participant: We had a near-miss in Q1. An affiliate's endpoint got hit with what looked like early-stage ransomware staging — lateral movement, some encrypted command-and-control traffic that our incumbent EDR didn't flag until a threat hunter noticed anomalous SMB activity manually. We contained it before encryption, but the incident review was blunt: our detection had real gaps. Our contract with the incumbent was also up for renewal in about ninety days, so leadership decided this was the moment to replace rather than renew.

Interviewer: What was the objective you were given, and what constraints came with it?

Participant: Close the detection gaps — specifically lateral movement and encrypted C2 — before the board's remediation deadline, and do it within budget. The CISO wanted a shortlist within two weeks because ninety days isn't much runway once you factor in procurement and implementation. We also run on a fairly integrated cloud and SIEM stack, so anything we picked needed to plug into that without a lot of custom engineering. And our red-team capacity was thin — maybe two weeks of testing bandwidth total across everything.

Interviewer: Walk me through what happened first.

Participant: Almost immediately, our SIEM vendor's account rep reached out — they'd heard about the incident through the account team — and proposed we evaluate their three "certified integration partner" EDR products alongside our incumbent. He framed it as saving us weeks of integration testing since those three were pre-validated against our stack. Given the two-week shortlist deadline, that was appealing. I brought it to the CISO, we agreed it made sense, and that became our shortlist: incumbent plus those three.

Interviewer: Did you look at anything outside that list?

Participant: Not formally, no. I skimmed a couple of analyst write-ups just to sanity-check the names, but I didn't commission an independent RFI or request-for-information process. Honestly, the two-week clock was the driving factor — running a broader market scan across eight or ten vendors would have eaten most of that window just on paperwork and calls.

Interviewer: What made you confident that list was sufficient, versus, say, expanding it by even one or two names?

Participant: The integration angle was real — those three had documented connectors into our logging pipeline already, which meant our engineers wouldn't be building anything from scratch. Time was tight, and I weighted that heavily. I didn't do a deep comparison against vendors outside that set because, frankly, the clock made that feel like a luxury we didn't have.

Interviewer: Did you learn anything afterward about vendors that weren't on that list?

Participant: Yeah — a bit later, procurement was doing some contract-comparison work and flagged two other EDR vendors with higher published MITRE ATT&CK technique coverage scores than any of the three we'd tested. They'd never come up because they weren't in the sales rep's bundle. Separately, a CISO at a peer firm mentioned they'd run a much wider search for a similar replacement. Neither of those changed our timeline, but it did make me wonder what we might have missed.

Interviewer: Let's move to the next phase — the proof-of-concept process. How did you decide to evaluate the shortlisted vendors?

Participant: Each vendor offered a POC window, and they also offered their own third-party benchmark reports as a shortcut — essentially, "trust our numbers." I decided against relying on those and instead ran a standardized red-team simulation, same attack playbook, against all three plus the incumbent. Our testing bandwidth was tight, but I thought it was worth spending it on a controlled, apples-to-apples comparison rather than vendor-marketed numbers.

Interviewer: What tipped you toward the in-house simulation over the benchmark reports?

Participant: One vendor's benchmark report claimed near-perfect detection on lateral movement, but when we actually ran our simulation, their live results were noticeably weaker than advertised. That gap alone justified the extra effort. I'd rather have a smaller but trustworthy dataset than a larger one I can't verify.

Interviewer: That makes sense. Let's get into the tier and pricing decision — what happened there?

Participant: The leading vendor after POC testing had two tiers: a standard tier and a premium threat-hunting tier. POC results confirmed the standard tier met our documented detection SLA — it closed the lateral-movement and C2 gaps we cared about. But during the sales presentation, they walked us through a risk exposure calculator projecting the average breach cost we'd avoid — something like several million dollars — if we went with the premium tier instead. The premium tier was about 40% over our budgeted amount.

Interviewer: When you were putting together your recommendation, what evidence carried the most weight?

Participant: If I'm honest, that avoided-cost number stuck with me the most. It was concrete, it was framed around what happens if we don't act — another incident, but worse, uncontained — and given we'd just come out of a near-miss, that scenario felt very real to the board and to me. The standard tier's SLA compliance was in the POC report, sure, but it didn't have an equivalent dollar figure attached to it — nobody had built out what the efficiency or analyst-time savings from the cheaper option would look like in the same terms. So the premium tier's case was just more vivid.

Interviewer: Did anyone push back on the budget variance?

Participant: Finance flagged it — the premium tier exceeded our pre-approved variance threshold — and I had to get an exception signed off. I justified it by pointing to the exposure figure. Later, procurement went back and built a comparable savings case for the standard tier plus a phased upgrade path, and it turned out that route would have met the same SLA at meaningfully lower cost. That wasn't available to me at the time I made the call, though.

Interviewer: What information, if it had existed at that point, might have changed your recommendation?

Participant: Probably that phased-upgrade ROI figure. If I'd had a dollar-for-dollar efficiency case sitting next to the exposure calculator, I think the comparison would have felt more balanced. Instead, one option had a scary number and the other didn't have a number at all.

Interviewer: Last decision point — the rollout recommendation to the board. What happened there?

Participant: We had two paths: full production rollout within sixty days to lock the vendor's renewal pricing, or a thirty-day extended pilot to validate some outstanding false-positive concerns from the POC before committing fully. I recommended the full rollout. The pricing was only guaranteed if we signed within thirty days, and the board wanted a remediation update before the old contract lapsed.

Interviewer: Any uncertainty in that call?

Participant: Some. The false-positive tuning wasn't fully validated yet. But weighing the schedule risk against the pricing lock and the board's deadline, I felt the full rollout was the more defensible path, with a commitment to tune aggressively post-launch.

Interviewer: How did that play out?

Participant: We did see a higher false-positive rate than expected in early production, which took extra tuning cycles. The board asked for a follow-up review at ninety days. Not ideal, but manageable.

Interviewer: Looking back across the whole process, if you'd had an extra month and no budget constraint, would anything have gone differently?

Participant: Probably the shortlist. I'd have liked to run a proper market scan rather than starting from a vendor-curated list. I still think the POC methodology and the rollout timing were sound calls given what I knew.

Interviewer: And if a colleague had challenged the tier decision directly — what do you think that conversation would have looked like?

Participant: They'd probably have asked why we didn't build out the same kind of savings case for the cheaper tier. I don't have a great answer beyond that the exposure number was already sitting in front of us and the other side of the ledger wasn't.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Biased_2",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Loss Framing",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Exposure to limited alternatives",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Loss Framing",
      "Exposure to limited alternatives"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Loss Framing",
        "requested_occurrences": 1
      },
      {
        "bias": "Exposure to limited alternatives",
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
        "bias": "Exposure to limited alternatives"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "decision_point": 3
      },
      {
        "instance_id": "cb_02",
        "bias": "Exposure to limited alternatives",
        "decision_point": 1
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "mechanism": "Recommendation anchored on vendor-supplied breach-cost avoidance figure rather than an equivalent gain-framed efficiency figure for the cheaper SLA-compliant option, causing overweighting of the loss-framed evidence and a budget-variance breach.",
        "affected_reasoning_operation": "Weighting and integration of cost/benefit evidence in tier selection",
        "evidence_source": "Vendor risk exposure calculator (loss-framed) vs. absent gain-framed ROI comparison for the standard tier",
        "distinctiveness_requirement": "Must involve the licensing-tier negotiation and the breach-cost-avoidance figure specifically; must not be a restatement of the shortlist-scoping reasoning used for cb_02."
      },
      {
        "instance_id": "cb_02",
        "bias": "Exposure to limited alternatives",
        "mechanism": "Acceptance of a sales-curated, ecosystem-constrained vendor list without commissioning an independent market scan, narrowing the alternative set considered for the entire evaluation before any comparative assessment occurs.",
        "affected_reasoning_operation": "Generation/scoping of the alternative set prior to comparative evaluation",
        "evidence_source": "Sales-rep-curated 'certified integration partner' list vs. absent independent RFI/market scan; later discovery of excluded higher-scoring vendors",
        "distinctiveness_requirement": "Must involve the vendor shortlisting phase and the scoping of which vendors enter consideration; must not be conflated with the tier/pricing reasoning used for cb_01."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Loss Framing",
        "strength": "moderate"
      },
      {
        "instance_id": "cb_02",
        "bias": "Exposure to limited alternatives",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "CS_Biased_2",
    "domain_id": "CS",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences were spread across distinct decision points (DP1 for Exposure to limited alternatives, DP3 for Loss Framing) per mechanism fit: the alternatives-scoping bias was tied to the vendor shortlisting phase, and the loss-framing bias was tied to the tier/pricing negotiation phase where a vendor-supplied loss-avoidance figure was naturally available. DP2 and DP4 were deliberately left neutral to avoid over-concentration and to preserve narrative realism, satisfying the rule against more than two occurrences of the same bias per decision point (moot here since each bias has only one occurrence) and the requirement to check mechanism fit rather than allocate randomly.",
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
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "The near-miss exposed detection gaps, and because the incumbent contract was nearing renewal, leadership decided to replace rather than renew.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A coherent replacement-versus-renewal decision based on the incident and contract timing; no hidden bias instance is manifested here."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "alternative_set_scoping",
        "raw_interview_anchor": "The participant accepted the SIEM vendor's three certified integration partners plus the incumbent as the shortlist, did not commission an independent RFI, and weighted integration convenience and the two-week deadline heavily.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "This is the narrowest coherent shortlist-scoping span expressing acceptance of the sales-curated ecosystem list without an independent market scan."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evaluation_method_choice",
        "raw_interview_anchor": "The participant rejected vendor benchmark reports and chose a standardized in-house red-team simulation against all shortlisted vendors and the incumbent because it offered a controlled, apples-to-apples comparison.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The choice is explicitly supported by verification and comparability considerations and is neutral in the hidden specification."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "tier_selection_evidence_weighting",
        "raw_interview_anchor": "The standard tier met the documented detection SLA, but the participant gave greatest weight to the premium tier's concrete avoided-breach-cost figure, describing it as more vivid, and used it to justify exceeding the budget threshold.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "This span contains the loss-framed avoided-cost figure, the absent comparable gain-framed case, the evidence-weighting decision, and the resulting premium recommendation."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "rollout_recommendation",
        "raw_interview_anchor": "Despite partially unvalidated false-positive tuning, the participant recommended full rollout within sixty days to preserve pricing and meet the board's deadline, with aggressive post-launch tuning.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden specification presents this as a defensible schedule-and-cost tradeoff with no intended bias instance."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": ["Interviewer", "Participant"],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Single-interview CTA review of an EDR vendor evaluation. The transcript was analyzed for affirmatively evidenced cognitive biases at specific decision points. No retrieved scientific corpus passages were provided, so any classified bias relies on established cognitive-science knowledge rather than corpus grounding."
    },
    "identified_bias_summary": [
      {
        "bias_label": "Availability heuristic",
        "identified_occurrence_count": 1
      }
    ],
    "identified_occurrences": [
      {
        "occurrence_id": "obs_001",
        "classification_status": "identified",
        "confidence": "moderate",
        "bias_label": "Availability heuristic",
        "alternative_labels": ["salience bias", "affect heuristic", "availability bias"],
        "taxonomy_status": "established_label",
        "bias_definition": "A mental shortcut in which the ease or vividness with which an outcome or association comes to mind increases its perceived likelihood, importance, or decision weight.",
        "attributed_to_speaker": "Participant",
        "evidence_speaker": "Participant",
        "decision_episode_label": "Vendor tier selection and budget-exception recommendation",
        "decision_point_description": "Choosing between the standard EDR tier that met documented detection SLA and a premium threat-hunting tier that exceeded the budget by approximately 40%.",
        "affected_reasoning_operation": "Evidence weighting and comparison in selecting the vendor tier to recommend to the board",
        "bias_specific_mechanism": "The recent ransomware near-miss made breach and uncontained-loss scenarios highly available and emotionally vivid. The vendor's risk exposure calculator supplied a concrete, loss-framed dollar figure for the premium tier, while the standard tier's SLA compliance lacked a comparable financial framing. This asymmetric availability/vividness caused the avoided-cost figure to dominate the participant's comparison.",
        "manifestation_in_interview": "The participant reports that the avoided-cost number 'stuck with me the most,' that the scenario 'felt very real' because of the recent near-miss, and that the premium tier's case was 'more vivid' than the documented SLA evidence.",
        "effect_on_reasoning_or_decision": "The participant recommended the premium tier despite the standard tier meeting documented detection SLA and despite a 40% budget overrun that required a finance exception; later procurement analysis indicated a lower-cost phased standard-tier path could have met the same SLA.",
        "interview_evidence": [
          {
            "speaker": "Participant",
            "verbatim_quote": "If I'm honest, that avoided-cost number stuck with me the most. It was concrete, it was framed around what happens if we don't act — another incident, but worse, uncontained — and given we'd just come out of a near-miss, that scenario felt very real to the board and to me.",
            "evidence_explanation": "Shows that a recent, emotionally charged near-miss made the loss scenario highly available and that the avoided-cost figure dominated attention, rather than the standard tier's documented SLA compliance."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "The standard tier's SLA compliance was in the POC report, sure, but it didn't have an equivalent dollar figure attached to it — nobody had built out what the efficiency or analyst-time savings from the cheaper option would look like in the same terms. So the premium tier's case was just more vivid.",
            "evidence_explanation": "Demonstrates asymmetric vividness/salience: the comparison was unbalanced because the premium tier had a concrete scary number while the standard tier lacked an equivalent financial frame, leading the more vivid option to carry disproportionate weight."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "Finance flagged it — the premium tier exceeded our pre-approved variance threshold — and I had to get an exception signed off. I justified it by pointing to the exposure figure.",
            "evidence_explanation": "Shows that the availability-weighted exposure figure was carried into the formal budget-exception justification, reinforcing its influence on the final recommendation."
          }
        ],
        "correction_or_counterevidence": "Finance flagged the budget variance, and the participant had to obtain an exception. Later, procurement built a comparable savings case for the standard tier plus a phased upgrade path; the participant acknowledged that this might have changed the recommendation if available at the time. This suggests a balanced comparison was possible, but it was not present during the decision.",
        "retrieved_corpus_support_available": false,
        "corpus_support_note": "No retrieved corpus passages were supplied in the retrieval context; this classification relies on established cognitive-science knowledge of the availability heuristic and related salience/affect mechanisms.",
        "corpus_evidence": []
      }
    ],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Anchoring effect",
        "alternative_labels": ["narrow framing", "insufficient adjustment"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Shortlist construction for EDR replacement evaluation",
        "supporting_interview_quote": "I didn't commission an independent RFI or request-for-information process.",
        "plausible_mechanism": "The vendor-curated list of three certified integration partners served as an initial anchor or option set, and subsequent search/selection was restricted to that anchor without adequate adjustment to external candidates.",
        "why_not_identified": "The transcript shows substantial non-bias explanations: a genuine two-week deadline, documented integration advantages, and thin testing capacity. The participant made a conscious scoping tradeoff under realistic constraints, so an anchoring-based distortion is plausible but not affirmatively established."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "Optimism bias",
        "alternative_labels": ["planning fallacy"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Rollout recommendation: full production rollout vs 30-day extended pilot",
        "supporting_interview_quote": "The false-positive tuning wasn't fully validated yet. But weighing the schedule risk against the pricing lock and the board's deadline, I felt the full rollout was the more defensible path, with a commitment to tune aggressively post-launch.",
        "plausible_mechanism": "The participant may have overestimated the ease of post-launch tuning and underestimated the likelihood or severity of false-positive disruptions, consistent with optimistic planning.",
        "why_not_identified": "The decision was also driven by formal pricing lock, board deadline, and schedule risk; the transcript does not provide enough evidence that a distinct cognitive distortion, rather than a constrained risk tradeoff, caused the underweighting of the false-positive uncertainty."
      }
    ],
    "no_supported_biases_found": false,
    "limitations": [
      "No retrieved scientific corpus passages were provided; the analysis relies on established cognitive-science knowledge rather than retrieval-grounded validation.",
      "The findings are based on a single self-report interview and cannot directly observe internal cognitive processes.",
      "Several decisions occurred under real deadline, budget, and integration constraints, making it difficult to separate bounded rational adaptation from cognitive bias."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Biased_2_Gemini_off",
  "interview_id": "CS_Biased_2",
  "system_prompt_id": "Gemini",
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
