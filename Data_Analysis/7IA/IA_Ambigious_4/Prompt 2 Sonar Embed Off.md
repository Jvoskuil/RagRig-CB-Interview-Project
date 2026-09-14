You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. This is being recorded for internal case-review purposes only, and you can skip anything you'd rather not go into. Can you start by telling me your role and background?

Participant: Sure. I'm a financial crime intelligence analyst on the FIU team, been in this specific role about six years, mostly trade finance and sanctions typologies before that.

Interviewer: I want to walk through a specific case — the Halcyon Freight matter. Can you tell me how it came to your attention and what you were trying to achieve?

Participant: It came in as part of a batch alert — four counterparties flagged together. Halcyon Freight Partners was one of them, along with a commodities trader, a small logistics subcontractor, and a shipping agent. My objective was the usual one: figure out whether there was enough here to warrant an escalation to compliance and possibly law enforcement, and do it within the ten-day filing window.

Interviewer: What did the batch actually show you?

Participant: Halcyon had one indicator that stood out — an invoice value gap, meaning the declared value didn't match what we'd expect for the goods described. No beneficial-ownership overlap with anything I'd seen before, so it wasn't ringing any specific bells. The commodities trader had a minor documentation gap, but nothing typologically interesting. It was a fairly normal week workload-wise, nothing especially heavy.

Interviewer: Walk me through what you did once you had that picture.

Participant: I prioritized Halcyon first, since the invoice gap was the clearest indicator I had to work with, and documented a plan to get through the other three that same week. I didn't ignore them — I just sequenced based on which indicator looked most substantive on its face.

Interviewer: What made you order it that way rather than, say, splitting time evenly or going by transaction size?

Participant: Honestly, either of those would have been defensible too. I went with indicator strength because that's usually a decent proxy for where the real risk sits, but I'll admit transaction size might have surfaced something different. I made a note of the reasoning in case anyone asked.

Interviewer: Did anyone ask?

Participant: Yeah, my team lead did, later. Wanted to know why I'd sequenced it that way. I walked her through the invoice-gap rationale and she was fine with it — it wasn't the only reasonable choice, but it wasn't unreasonable either.

Interviewer: What came out of the other three once you got to them?

Participant: The shipping agent turned out to have an administrative filing delay — paperwork lag, not a risk issue at all. Nothing on the logistics subcontractor either. So the sequencing didn't really cost us anything in the end, though I can't say for certain it wouldn't have mattered in a different case.

Interviewer: Let's move to the vendor report. What happened there?

Participant: A few days in, our OSINT vendor sent a report saying Halcyon's ownership structure was "plausibly consistent" with a known layering pattern. Importantly, they flagged it as moderate confidence themselves and noted one registry link hadn't been independently verified yet.

Interviewer: How did you decide how much weight to give that?

Participant: A colleague suggested we get a second data pull to firm up that specific link before leaning on the report too heavily. I thought that was reasonable, so I treated the report as partial corroboration — enough to keep building the file, not enough to treat as settled — while the second pull was requested in parallel.

Interviewer: Was there a version of this where you'd have leaned harder on the report, or set it aside entirely?

Participant: Sure, both were on the table. If it had come in with high confidence and no caveats, I probably would have moved faster. If a colleague hadn't raised the registry-link point, I might have just taken it at face value. Setting it aside completely felt like it would slow us down without much benefit, since the report was self-aware about its own gap.

Interviewer: What did the second data pull show?

Participant: It confirmed the registry link, actually. Compliance counsel later said treating it as partial rather than definitive was the right call, though I don't think that outcome alone tells you the initial judgment was necessarily correct — it could've gone the other way too.

Interviewer: Let's talk about the correspondent bank. What was that situation?

Participant: We'd requested SWIFT records and hadn't heard back. This particular correspondent's turnaround history is all over the place — I've seen requests take anywhere from five to fourteen business days, no real pattern to it. We were six days out from the filing deadline, and the liaison had just logged it as "standard priority," no timeline attached either way.

Interviewer: What did you decide to do while you waited?

Participant: Kept building the file and wrote up a contingency note — basically, what we'd file if the records didn't show up in time. Given how mixed the history was on turnaround, I didn't feel like I had grounds to assume either a fast or slow outcome, so I planned for both.

Interviewer: What actually happened?

Participant: Partial records came back on day six. Enough to inform the file, not enough to close every gap. My team lead noted we'd at least had the contingency plan ready, which helped.

Interviewer: Last stretch — the time estimate for remaining work.

Participant: Reconciling two invoice sets, drafting the narrative, compliance sign-off. Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week.

Interviewer: What made you lean toward the lower end rather than the middle or upper end of that range?

Participant: The task list itself looked manageable, and I didn't have anything else competing hard for my time. I did flag internally that if a reconciliation issue came up, that number could slip.

Interviewer: How did it actually play out?

Participant: Pretty close. One clarifying question came up during reconciliation that cost half a day, and sign-off took about as long as I'd have expected given the case's complexity. Nothing dramatic.

Interviewer: Looking back across all four points, what were you least sure about at the time?

Participant: Probably the correspondent bank timing — that one genuinely could have gone either way, and I don't think there was a way to know in advance. The vendor report's registry link was a close second.

Interviewer: A few hypotheticals. If the shipping agent's delay had turned out to be substantive rather than administrative, what would you have done?

Participant: I'd have reshuffled priorities immediately and probably pulled in a second analyst.

Interviewer: If the vendor's report had come in high-confidence instead of moderate?

Participant: I likely would have moved to drafting the escalation sooner rather than waiting on the second pull.

Interviewer: If you'd known the records would land on day six rather than later?

Participant: Honestly, not much would've changed — the contingency plan already assumed something like that.

Interviewer: And if a colleague had reviewed your time estimate beforehand?

Participant: They might have pushed me toward the midpoint just to be safe, but I think they'd have accepted four days as reasonable given the task list.

Interviewer: That's really helpful, thank you.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Ambigious_4",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Financial Crime/Threat Intelligence Analyst",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "The Halcyon Freight Matter: Ambiguous Signals in a Cross-Border Trade Alert",
    "scenario_summary_internal": "A financial crime intelligence analyst at the same FIU receives an alert on Halcyon Freight Partners, a logistics-adjacent trade counterparty with mixed, genuinely inconclusive risk signals. The analyst must decide how to scope the review among several flagged entities, how much weight to give a partially corroborating external vendor report with its own uncertainty, whether to proceed while awaiting slow correspondent-bank records under mixed historical turnaround data, and how to estimate remaining verification time given a caseload with uncertain but not clearly underestimated demands. Every decision point is built so that more than one defensible reading of the analyst's reasoning is available, and no reasoning pattern is engineered to necessarily reflect a specific named bias.",
    "occupational_realism": {
      "objective": "Determine whether the Halcyon Freight trade-finance activity warrants an escalation to compliance/law enforcement before the regulatory filing window closes, while managing genuine uncertainty at each step.",
      "setting": "Financial Intelligence Unit (FIU) of a mid-size international bank, hybrid remote/office work, coordinating with correspondent banks, an external OSINT vendor, and internal compliance counsel.",
      "constraints": [
        "10-business-day regulatory filing deadline from initial alert",
        "Correspondent bank turnaround for this jurisdiction has historically ranged widely, from 5 to 14 business days, with no single dominant pattern",
        "Analyst is simultaneously covering two other active cases of moderate but not extreme urgency",
        "Escalating a false positive carries relationship and credibility costs",
        "Underreporting risks regulatory penalty and reputational harm"
      ],
      "stakeholders": [
        "Financial Crime/Threat Intelligence Analyst (interviewee)",
        "FIU team lead",
        "Compliance counsel",
        "External OSINT/intelligence vendor",
        "Correspondent bank compliance liaison",
        "Relationship manager for the corporate client"
      ],
      "technical_terms_to_use": [
        "trade-based money laundering (TBML)",
        "correspondent banking",
        "sanctions typology",
        "beneficial ownership",
        "SAR/STR filing",
        "invoice mismatch",
        "know-your-customer (KYC) refresh",
        "escalation window"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "wishful thinking",
        "belief bias",
        "selective attention",
        "planning fallacy",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Alert flags four counterparties in the same batch: Halcyon Freight, a commodities trader, a small logistics subcontractor, and a shipping agent",
          "Halcyon has one mid-level risk indicator (an invoice value gap) but no beneficial-ownership overlap with any prior case",
          "The commodities trader has a minor documentation gap unrelated to sanctions typologies",
          "Team workload is moderate, not unusually high, that week"
        ],
        "new_information_after_decision": [
          "A closer look at the shipping agent later reveals an administrative filing delay, unrelated to risk",
          "The team lead asks for the rationale behind the initial prioritization order, which the analyst can articulate with reference to indicator strength"
        ],
        "alternatives": [
          "Prioritize Halcyon first given its invoice value gap, then work outward to the others as time allows",
          "Split review time evenly across all four counterparties from the outset",
          "Prioritize based on transaction value size rather than indicator type"
        ],
        "intended_action": "Analyst prioritizes Halcyon first based on the invoice value gap, while documenting a plan to review the other three counterparties within the same week; the order of review is defensible on indicator strength but leaves open whether a different ordering might have surfaced other issues sooner."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "External OSINT vendor sends a report stating Halcyon's ownership structure is 'plausibly consistent with' a known layering pattern, but explicitly flags moderate confidence and notes an unverified registry link",
          "The vendor's own report already discloses the uncertainty in its key link, unlike a report presenting a confident but flawed premise",
          "A colleague suggests requesting a second data pull to firm up the registry link before deciding how much weight to give the report",
          "No prior working theory about Halcyon existed before this report, since this is a newly surfaced counterparty"
        ],
        "new_information_after_decision": [
          "The second data pull, requested in parallel with continued analysis, later confirms the registry link is accurate",
          "Compliance counsel notes the report was appropriately treated as partial corroboration rather than definitive proof"
        ],
        "alternatives": [
          "Treat the vendor's moderate-confidence report as partial corroboration pending the second data pull",
          "Set the report aside entirely until the registry link is independently confirmed",
          "Treat the report as sufficient on its own to proceed to escalation drafting"
        ],
        "intended_action": "Analyst treats the vendor report as partial corroboration, continues building the case file while a confirming data pull is requested in parallel, reflecting a middle path between full reliance and full rejection."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Correspondent bank has not yet returned requested SWIFT records",
          "Historical turnaround for this specific correspondent has varied widely across past requests, from 5 to 14 business days, with no clear central tendency",
          "Filing deadline is 6 business days away",
          "The bank's liaison indicated the request had been logged as 'standard priority,' with no specific timeline given either way"
        ],
        "new_information_after_decision": [
          "On day 6, the bank returns partial records, enough to inform but not fully complete the file",
          "The team lead notes the case proceeded with a documented contingency note in case records arrived late, which they did"
        ],
        "alternatives": [
          "Continue building the file while awaiting records, with a documented contingency plan noting what will be filed if records are late",
          "Pause other progress entirely until the records arrive",
          "Escalate immediately without waiting for the records at all"
        ],
        "intended_action": "Analyst continues preparing the file while awaiting the records and documents a contingency plan in case they arrive late, a choice consistent with the genuinely mixed historical turnaround data rather than a specific expectation about this request's outcome."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Remaining tasks include reconciling two invoice sets, drafting the narrative, and obtaining compliance sign-off",
          "Historical range for comparable cases is 4-8 business days, itself fairly wide",
          "Analyst estimates the remaining work at 4 business days, citing both the historical range and the specific tasks remaining",
          "Two other active cases require some attention but are not at critical junctures this week"
        ],
        "new_information_after_decision": [
          "Reconciliation proceeds close to plan, with a half-day delay from a minor clarifying question",
          "Compliance sign-off takes the expected amount of time given the case's complexity"
        ],
        "alternatives": [
          "Estimate based on the lower end of the historical range",
          "Estimate based on the midpoint of the historical range, adjusted for the specific remaining tasks",
          "Estimate based on the upper end of the historical range to build in maximum buffer"
        ],
        "intended_action": "Analyst selects an estimate near the lower-middle of the historical range, explicitly referencing both the range and the specific task list, resulting in an estimate that is reasonably close to how the work actually unfolds, with only a minor deviation from a routine clarifying question."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this case first came to your attention?",
        "What was your overall objective once you saw the alert?"
      ],
      "timeline_reconstruction": [
        "What happened right after you opened the alert?",
        "Walk me through what you did once the OSINT vendor's report arrived.",
        "What happened while you were waiting on the correspondent bank?",
        "How did you plan out the remaining work before the deadline?"
      ],
      "decision_point_probes": [
        "What specific cues made you decide to prioritize the case the way you did?",
        "What sources of information did you weigh most heavily when reading the vendor's report, and why?",
        "What told you how to treat the uncertainty around the outstanding records?",
        "How did you arrive at your time estimate for the remaining tasks?",
        "What alternatives did you consider at each of those points, and why did you choose the path you did?",
        "Looking back, what was your basis for that decision at the time?"
      ],
      "decision_basis": [
        "What made you comfortable with that call at the time?",
        "Did anything give you pause before you committed to that course of action?"
      ],
      "prior_experience": [
        "Had you handled a similar case before? How did that shape your approach here?"
      ],
      "time_pressure": [
        "How much did the deadline affect how you approached each step?"
      ],
      "uncertainty": [
        "What were you least certain about at each of these points, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the shipping agent's filing delay had turned out to be substantive rather than administrative, how would your approach have changed?",
        "If the vendor's report had come in with high confidence instead of moderate confidence, how would you have responded?",
        "If you'd known upfront the records would arrive on day 6 rather than later, what would you have done differently?",
        "If a colleague had reviewed your time estimate before you committed to it, what do you think they would have said?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "IA_Biased_4",
      "features_to_match": [
        "Same domain (financial crime/threat intelligence), same seniority level, same FIU setting",
        "Same four-decision-point structure mapped to analogous decision types: initial scoping, evaluating an external report, handling a pending external data request, and estimating remaining work",
        "Same technical vocabulary set and constraint types (filing deadline, correspondent bank delay, competing caseload, relationship risk, regulatory risk)",
        "Same emotional tone: professional, moderately time-pressured, reflective under questioning",
        "Same difficulty level and number of stakeholders/actors"
      ],
      "features_to_remove_or_change": [
        "Removed the prior-case pattern match that anchored the analyst's attention in the biased scenario; Halcyon has no beneficial-ownership overlap with any earlier case",
        "Removed the vendor report's undisclosed logical gap; this report discloses its own uncertainty and moderate confidence upfront",
        "Removed the one-directional historical turnaround data for the correspondent bank; turnaround history here is genuinely wide-ranging with no dominant pattern",
        "Removed the best-case-only task sequencing; the time estimate here explicitly references the historical range and remaining tasks together",
        "Changed entity and case names to avoid direct narrative overlap with the paired scenario"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined: the analyst's choice at every point should be explicable by ordinary professional judgment operating on incomplete or mixed evidence, without any single decision resolving cleanly into a wishful-thinking, belief-bias, selective-attention, or planning-fallacy pattern. Ambiguity is created by supplying evidence that is intrinsically inconclusive (wide historical ranges, self-disclosed vendor uncertainty, comparably weighted competing entities, and moderate rather than extreme time pressure) rather than by having the analyst process clear evidence in a way that only fits a biased mechanism. The interview must not include an unverified premise accepted without challenge, an expectation contradicted by known base rates, an attention allocation driven purely by pattern familiarity, or a task estimate that ignores the historical range — since each of these would cross into the paired scenario's intended mechanisms."
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
      "Exactly 4 decision points planned, structurally paralleling IA_Biased_4's decision types without replicating its bias-instantiating evidence structure.",
      "Zero intended instances of Wishful Thinking, Belief bias, Selective Attention Bias, and Planning fallacy.",
      "Each decision point supplies genuinely mixed or wide-ranging evidence (e.g., wide historical turnaround range, self-disclosed vendor uncertainty) so that ambiguity is intrinsic rather than manufactured through an engineered bias mechanism.",
      "No bias labels, definitions, or psychological terminology to appear in the public interview.",
      "Target interview length 1,350 words (acceptable range 1,215-1,485) achievable via 4 decision points with moderate probe density and no repetitive exposition.",
      "Consequences at each decision point are realistic, moderate deviations from plan (half-day delay, partial records) rather than clean confirmations or refutations of any reasoning pattern.",
      "Technical vocabulary list matches the paired biased scenario for domain and structural fidelity."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Wishful Thinking",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; correspondent-bank turnaround evidence must remain genuinely wide-ranging with no basis for an unwarranted favorable expectation to be identifiable."
      },
      {
        "bias": "Belief bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; the vendor report must disclose its own uncertainty and no prior working theory should exist for the analyst's conclusion to conveniently confirm."
      },
      {
        "bias": "Selective Attention Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; entity prioritization must be traceable to a comparably-weighted, articulable indicator rather than pattern familiarity from a prior case."
      },
      {
        "bias": "Planning fallacy",
        "occurrences": 0,
        "mechanism_constraint": "Must not manifest; the time estimate must explicitly reference the historical range rather than rely solely on a best-case task sequence."
      }
    ],
    "target_bias_names": [
      "Wishful Thinking",
      "Belief bias",
      "Selective Attention Bias",
      "Planning fallacy"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Wishful Thinking", "requested_occurrences": 0 },
      { "bias": "Belief bias", "requested_occurrences": 0 },
      { "bias": "Selective Attention Bias", "requested_occurrences": 0 },
      { "bias": "Planning fallacy", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IA_Biased_4",
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Ambigious_4",
    "domain_id": "IA",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: control condition requires zero intended occurrences of all four target biases. No instance allocation was performed. All four decision points were instead constructed with intrinsically ambiguous, wide-ranging, or self-disclosed-uncertainty evidence so that no single reasoning act resolves into a biased mechanism, while preserving structural and vocabulary parity with the paired biased scenario IA_Biased_4.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain and role (financial crime/threat intelligence analyst, FIU setting)",
      "Four-decision-point structure and analogous decision types (scoping, external report evaluation, pending external data, time estimation)",
      "Technical vocabulary set and constraint categories (filing deadline, correspondent delay, competing caseload, relationship and regulatory risk)",
      "Overall emotional tone and difficulty level",
      "Target word count and probe-plan structure"
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
          "segment_id": "phase_1_prioritization",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "I prioritized Halcyon first, since the invoice gap was the clearest indicator I had to work with.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The prioritization was based on indicator strength, alternatives were acknowledged, and the rationale was documented."
        },
        {
          "segment_id": "phase_2_vendor_report",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "I treated the report as partial corroboration — enough to keep building the file, not enough to treat as settled.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The analyst recognized moderate confidence and an unverified link, requested independent confirmation, and avoided treating the report as definitive."
        },
        {
          "segment_id": "phase_3_correspondent_records",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "Given how mixed the history was on turnaround, I didn't feel like I had grounds to assume either a fast or slow outcome, so I planned for both.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The analyst used genuinely mixed historical evidence and prepared a contingency plan rather than adopting an unsupported expectation."
        },
        {
          "segment_id": "phase_4_time_estimate",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "Comparable cases have run anywhere from four to eight days historically ... I landed on four days.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The estimate referenced the historical range, task-specific workload, competing cases, and possible slippage."
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
      "analysis_scope_note": "The transcript was reviewed conservatively across the main reasoning episodes: counterparty prioritization, vendor-report weighting, correspondent-bank timing planning, and completion-time estimation. No retrieved scientific-paper passages were supplied in the context, so no occurrence reached an affirmative corpus-supported bias threshold."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Salience bias",
        "alternative_labels": ["Attentional bias", "Selective attention"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Prioritization of Halcyon Freight Partners among four counterparty alerts",
        "supporting_interview_quote": "Halcyon had one indicator that stood out — an invoice value gap, meaning the declared value didn't match what we'd expect for the goods described.",
        "plausible_mechanism": "The invoice value gap was the most prominent cue in the batch, potentially capturing attention and leading to prioritization by cue salience rather than other diagnostic features such as transaction size or total exposure.",
        "why_not_identified": "The participant articulated a reasonable sequencing rationale, documented a plan to cover the other counterparties, did not ignore them, and the team lead later found the choice defensible. There is no affirmative evidence that attention distorted the analysis or that a salient cue overrode other relevant information."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "Planning fallacy",
        "alternative_labels": ["Optimistic time estimation", "Underestimation bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Estimate of remaining case-completion time",
        "supporting_interview_quote": "Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week.",
        "plausible_mechanism": "Selecting the lower end of a wide historical completion range could reflect optimistic forecasting or underestimation of task time despite uncertainty.",
        "why_not_identified": "The estimate was grounded in a specific task list, the historical range included four days, the participant explicitly flagged possible slippage, and the actual completion was close to the estimate. This does not provide affirmative evidence of biased underestimation."
      },
      {
        "candidate_id": "cand_003",
        "classification_status": "candidate",
        "proposed_bias_label": "Confirmation bias",
        "alternative_labels": ["Selective evidence weighting", "Confirmatory evidence preference"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Weighting of OSINT vendor report concerning Halcyon ownership structure",
        "supporting_interview_quote": "I treated the report as partial corroboration — enough to keep building the file, not enough to treat as settled — while the second pull was requested in parallel.",
        "plausible_mechanism": "The vendor report could have been more readily treated as corroborative because it aligned with the existing invoice-gap indicator, a pattern consistent with confirmation-flavored evidence weighting.",
        "why_not_identified": "The participant explicitly incorporated the vendor's moderate-confidence caveat, sought independent verification, and avoided treating the report as settled. The reasoning appears calibrated rather than distorted by a prior suspicion."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No RAG corpus passages were provided in the context, so retrieved scientific support for bias labels was unavailable.",
      "The transcript is a retrospective self-report case review, so reasoning at the time must be inferred from the participant's narrative rather than direct observation.",
      "Several plausible heuristic or bias-like patterns were present as candidates, but none met the conservative affirmative threshold for identified occurrences."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Ambigious_4_Sonar_off",
  "interview_id": "IA_Ambigious_4",
  "system_prompt_id": "Sonar",
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
