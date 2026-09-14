You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal case-review and training purposes only, and I'll be asking you to walk me through a specific case in detail. You're free to skip anything you're not comfortable discussing. Can you first tell me your role and how long you've been doing this kind of work?

Participant: Sure. I'm a financial crime intelligence analyst on the FIU team, been here about six years, mostly focused on trade finance and sanctions-related typologies. Before that I did two years in transaction monitoring.

Interviewer: Great, thanks. I want to focus on a specific case — the Meridian Trading matter. Can you walk me through how it first came to your attention and what you were trying to accomplish?

Participant: Right, so this came in through an automated alert — three invoices from Meridian Trading LLC with quantity and value mismatches, which is a classic flag for trade-based money laundering. My objective was straightforward on paper: figure out whether this was probable sanctions evasion and, if so, get a defensible escalation to compliance and law enforcement before the filing window closed. We had ten business days from the alert.

Interviewer: What did the alert batch actually contain?

Participant: A cluster of counterparties. Meridian was the obvious one — the ultimate beneficial owner shared a registered agent with a company from a case I'd worked about eighteen months earlier, which had ended in a successful sanctions-evasion referral. There was also a separate counterparty in the same batch, a logistics firm, that didn't match anything I recognized. And it was a heavy week — alert volume across the team was well above average, so I needed to move efficiently.

Interviewer: Let's reconstruct the sequence. What did you do right after opening the alert?

Participant: I scoped the review. Given the registered-agent overlap with the prior case, I focused my initial workup on Meridian and its immediate corporate web — pulling registry filings, past KYC refresh notes, that kind of thing. The logistics counterparty I noted but set aside as lower priority since it didn't fit any typology I'd seen before.

Interviewer: What specifically made you decide to scope it that way rather than, say, broadly across everyone in the batch?

Participant: Honestly, the registered-agent match jumped out immediately. That pattern had been reliable before — same agent, similar shell structure, same region. With the volume we were under that week, I didn't feel I had the bandwidth to give equal weight to an entity that had no connection to anything I'd seen. I did glance at the logistics firm's file, but there was nothing that screamed "look here," so I moved on.

Interviewer: Did you consider requesting broader automated screening before locking in that scope?

Participant: I thought about it, but that would've added a day or two, and the Meridian angle felt like the more productive use of time.

Interviewer: What happened with the logistics counterparty afterward?

Participant: A few days later it showed an unusual same-day wire pattern — nothing I'd examined at that point. My team lead actually asked why it wasn't in my initial scoping note. I didn't have a great answer beyond "it didn't fit the pattern I was chasing."

Interviewer: Let's move to the vendor report. Walk me through what happened when that arrived.

Participant: About three days in, our OSINT vendor sent a report concluding Meridian was highly likely tied to the sanctioned end-user. Their argument traced a chain of corporate registry links. The bottom line matched exactly what I already suspected from the registered-agent overlap, so it felt like strong corroboration.

Interviewer: Did anyone raise concerns about the report?

Participant: One of our junior analysts flagged that a step in the vendor's chain — where they treated two similarly named entities as the same legal entity — hadn't been independently verified. I remember thinking that was a fair point to note, but it read to me as a technicality rather than something that undercut the conclusion, since the overall picture fit so well with what I was already building.

Interviewer: What made you weight the report the way you did?

Participant: The conclusion aligned with my working theory, and the vendor has a decent track record. I treated the alignment itself as a kind of confirmation. I didn't go back and independently re-verify that specific entity-matching step before folding the report into the case file.

Interviewer: What did you later learn about that?

Participant: A document pull afterward showed the two entities were actually legally distinct, different beneficial owners entirely. Compliance counsel asked directly what independent verification had been done on that claim, and I had to admit — not much, beyond the vendor's own chain.

Interviewer: Let's talk about the correspondent bank. What was the situation there?

Participant: We'd requested SWIFT records — MT202 and MT103 messages — to confirm the fund flow to the suspected end-user. That correspondent bank, in a secondary jurisdiction, is notoriously slow; historically those requests take twelve to fifteen business days. We were six days from the filing deadline with nothing back yet, no confirmation timeline in writing.

Interviewer: What did you decide to do about the escalation while waiting?

Participant: I held off drafting it. I figured the records would probably come through in time — I wanted the file to be complete with that corroborating piece rather than submit something with a gap in it.

Interviewer: What gave you that expectation, given the track record you mentioned?

Participant: Honestly, more that I wanted it to land that way. Nothing had actually changed with the correspondent bank's typical pace. On day six they came back and said it'd be another ten days.

Interviewer: What happened to the case file at that point?

Participant: My team lead pointed out there wasn't a contingency escalation path drafted, so we were now scrambling.

Interviewer: Let's cover the last piece — the time estimate for remaining work.

Participant: With reconciliation, narrative drafting, and compliance sign-off left, I estimated two business days. I walked through the sequence assuming everything went smoothly — no rework.

Interviewer: How does that estimate compare to similar cases?

Participant: Comparable cross-border verification cases have typically run five to seven days. I didn't really reference that when I made the call, and I still had two other active cases pulling at me.

Interviewer: What happened once you started?

Participant: Reconciliation turned up a discrepancy that needed a follow-up query — cost an extra day. Sign-off took longer too, over a routine question I hadn't anticipated.

Interviewer: Looking back across all four points, what were you least certain about at the time?

Participant: Probably the entity-matching step and whether the records would actually show up. Those felt like the shakiest parts, even while I was moving forward on them.

Interviewer: A couple of hypotheticals. If the logistics counterparty had been flagged as high-risk from the start, how would your approach have changed?

Participant: I'd have split my attention much earlier and probably caught the wire pattern days sooner.

Interviewer: And if you'd known upfront the correspondent bank would take fifteen days?

Participant: I would have drafted a conditional escalation immediately rather than waiting.

Interviewer: Last one — if a colleague had reviewed your time estimate before you committed to it, what do you think they'd have flagged?

Participant: The base rate, probably, and the fact that I was already stretched across two other cases. Fair critique.

Interviewer: That's really helpful, thank you.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Biased_4",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Financial Crime/Threat Intelligence Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Meridian Trade Network: Suspected Sanctions Evasion via Layered Shell Invoicing",
    "scenario_summary_internal": "A financial crime intelligence analyst at a mid-size bank's FIU receives an automated alert flagging a cluster of trade-finance transactions linked to a Central Asian trading company suspected of routing goods for a sanctioned end-user. The analyst must triage the alert, evaluate a corroborating tip from an external intelligence vendor, decide whether to wait for outstanding correspondent-bank records before escalating, and estimate how long full verification will take before a regulatory reporting deadline. The case echoes a prior, successfully prosecuted sanctions-evasion typology the analyst worked on eighteen months earlier, creating fertile ground for pattern-driven reasoning errors under time pressure.",
    "occupational_realism": {
      "objective": "Determine whether the Meridian trade-finance activity constitutes probable sanctions evasion and produce a timely, defensible intelligence escalation to compliance/law enforcement before the regulatory filing window closes.",
      "setting": "Financial Intelligence Unit (FIU) of a mid-size international bank, hybrid remote/office work, coordinating with correspondent banks, an external OSINT vendor, and internal compliance counsel.",
      "constraints": [
        "10-business-day regulatory filing deadline from initial alert",
        "Correspondent bank in a secondary jurisdiction is slow to respond to information requests",
        "Analyst is simultaneously covering two other active cases",
        "Escalating a false positive damages a profitable corporate relationship and analyst credibility",
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
          "Automated alert flags three invoices from Meridian Trading LLC with quantity/value mismatches",
          "Meridian's ultimate beneficial owner shares a registered agent with a company from a 2024 sanctions-evasion case the analyst worked",
          "A separate counterparty in the same batch operates in an unrelated logistics sector with no prior typology match",
          "Alert volume this week is above average across the team"
        ],
        "new_information_after_decision": [
          "The unrelated logistics counterparty later shows an unusual same-day wire pattern that goes unexamined",
          "Team lead asks why the logistics counterparty wasn't included in the initial scoping note"
        ],
        "alternatives": [
          "Scope the review narrowly around the shell-company/registered-agent pattern matching the prior case",
          "Scope the review broadly across all flagged counterparties regardless of typology fit",
          "Request additional automated screening before committing to a scope"
        ],
        "intended_action": "Analyst scopes the case narrowly around entities matching the prior sanctions-evasion typology and sets aside the unrelated logistics counterparty as low priority."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "External OSINT vendor sends a report arguing Meridian is 'highly likely' tied to the sanctioned end-user",
          "The vendor's supporting argument relies on a chain of corporate registry links that has a logical gap: it assumes two similarly-named entities are identical without independent confirmation",
          "The report's bottom-line conclusion matches the analyst's working theory from Phase 1",
          "A junior analyst on the team flags that the entity-matching step in the vendor's argument is unverified"
        ],
        "new_information_after_decision": [
          "A later document pull shows the two similarly-named entities are in fact legally distinct with different beneficial owners",
          "Compliance counsel asks what independent verification was done on the vendor's entity-matching claim"
        ],
        "alternatives": [
          "Accept the vendor's conclusion because it fits the suspected sanctions-evasion narrative and proceed",
          "Independently verify the entity-matching step before weighting the report's conclusion",
          "Request a second vendor opinion to cross-check the argument's validity"
        ],
        "intended_action": "Analyst accepts the vendor's conclusion as probative because it aligns with the working theory, without separately assessing whether the argument's internal logic (the entity-matching step) actually holds."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Correspondent bank has not yet returned requested SWIFT MT202/MT103 records confirming fund flow to the suspected end-user",
          "Prior similar requests to this correspondent bank have taken 12-15 business days on average",
          "Filing deadline is 6 business days away",
          "No written confirmation exists that the records will arrive in time"
        ],
        "new_information_after_decision": [
          "On day 6, the correspondent bank confirms records will take another 10 business days",
          "Team lead notes the case file was left without a contingency escalation path"
        ],
        "alternatives": [
          "Proceed on the assumption the records will arrive before the deadline and delay drafting the escalation",
          "Draft a conditional escalation now that does not depend on the pending records, with a plan to supplement if records arrive",
          "Immediately request an extension from compliance given known correspondent-bank delays"
        ],
        "intended_action": "Analyst delays drafting the escalation, expecting the outstanding SWIFT records will arrive in time despite no confirmation and a track record of slower turnaround."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Remaining verification tasks include: reconciling three invoice sets, drafting the narrative, and obtaining compliance sign-off",
          "Historical average time for comparable cases with cross-border verification has been 5-7 business days",
          "Analyst estimates the remaining work at 2 business days based on the best-case sequence with no rework",
          "Two other active cases still require partial attention this week"
        ],
        "new_information_after_decision": [
          "Invoice reconciliation surfaces a discrepancy requiring a follow-up query, consuming an extra day",
          "Compliance sign-off takes longer than expected due to a routine but unanticipated question"
        ],
        "alternatives": [
          "Plan the remaining timeline using the best-case, no-rework scenario",
          "Plan the remaining timeline using historical base rates for comparable cases",
          "Build in an explicit buffer for likely follow-up queries and competing case demands"
        ],
        "intended_action": "Analyst commits to a 2-day completion estimate based on the best-case task sequence, without adjusting for historical base rates or known competing demands."
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
        "What specific cues made you decide to scope the case the way you did?",
        "What sources of information did you weigh most heavily when reading the vendor's report, and why?",
        "What told you the outstanding records would or wouldn't arrive in time?",
        "How did you arrive at your time estimate for the remaining tasks?",
        "What alternatives did you consider at each of those points, and why did you rule them out?",
        "Looking back, what was your basis for that decision at the time?"
      ],
      "decision_basis": [
        "What made you confident in that call at the time?",
        "Did anything give you pause before you committed to that course of action?"
      ],
      "prior_experience": [
        "Had you handled a similar case before? How did that shape your approach here?"
      ],
      "time_pressure": [
        "How much did the deadline affect how you approached each step?"
      ],
      "uncertainty": [
        "What were you least certain about at each of these points?"
      ],
      "closing_hypotheticals": [
        "If the unrelated logistics counterparty had been flagged as high-risk from the start, how would your approach have changed?",
        "If the vendor's report had reached the opposite conclusion, how would you have responded?",
        "If you'd known upfront the correspondent bank would take 15 days, what would you have done differently?",
        "If a colleague had reviewed your time estimate before you committed to it, what do you think they would have flagged?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "sab_01",
        "bias": "Selective Attention Bias",
        "decision_point": 1,
        "mechanism": "Analyst allocates review attention to entities matching a familiar registered-agent pattern from a prior case, while the unrelated logistics counterparty in the same alert batch is deprioritized without any substantive risk assessment, purely because it does not match the salient prior pattern.",
        "affected_reasoning_operation": "Evidence-selection / initial scoping of investigation",
        "evidence_available_at_time": [
          "Shared registered agent between Meridian and a prior sanctions-evasion case",
          "Unrelated logistics counterparty present in the same alert batch with no typology link",
          "Above-average alert volume creating pressure to triage quickly"
        ],
        "required_textual_manifestation": "Analyst explains narrowing the scope specifically because of the registered-agent match, and separately acknowledges the logistics counterparty was set aside without being evaluated on its own merits, only realizing its relevance after a later unusual wire pattern surfaces.",
        "plausible_nonbias_interpretation": "Prioritizing entities with a known typology match under time pressure could be read as reasonable triage efficiency rather than a reasoning error.",
        "strength": "subtle",
        "do_not_make_explicit": ["selective attention", "bias", "tunnel vision"]
      },
      {
        "instance_id": "bb_01",
        "bias": "Belief bias",
        "decision_point": 2,
        "mechanism": "Analyst evaluates the OSINT vendor's argument as sound primarily because its conclusion matches the analyst's pre-existing suspicion about Meridian, without independently checking whether the argument's key premise (the entity-matching step) is actually valid, despite a colleague flagging the gap.",
        "affected_reasoning_operation": "Argument evaluation / evidence weighting",
        "evidence_available_at_time": [
          "Vendor report conclusion aligning with analyst's working theory",
          "An unverified logical step in the vendor's argument (assumed entity identity)",
          "A junior colleague's explicit flag of the unverified step"
        ],
        "required_textual_manifestation": "Analyst describes accepting the report's conclusion as strong evidence because it 'made sense' given what was already suspected, while treating the colleague's concern about the unverified entity-matching step as a minor procedural note rather than a reason to re-examine the argument's validity.",
        "plausible_nonbias_interpretation": "Trusting a vendor report that aligns with independently formed suspicion could be framed as reasonable convergent-evidence reasoning rather than a validity error.",
        "strength": "moderate",
        "do_not_make_explicit": ["belief bias", "logical validity", "cognitive bias"]
      },
      {
        "instance_id": "wt_01",
        "bias": "Wishful Thinking",
        "decision_point": 3,
        "mechanism": "Analyst delays drafting the escalation and continues to expect the outstanding correspondent-bank records will arrive before the deadline, despite having no confirmation of this and possessing historical data showing this correspondent typically takes longer than the time remaining.",
        "affected_reasoning_operation": "Prediction / risk forecasting under uncertainty",
        "evidence_available_at_time": [
          "No written confirmation that records will arrive within the remaining window",
          "Historical average turnaround from this correspondent bank exceeding the time remaining",
          "Desire to complete the case cleanly with full corroboration"
        ],
        "required_textual_manifestation": "Analyst states a belief that the records would 'probably come through in time' or similar, explicitly tied to wanting a complete file rather than to any evidence the timeline had improved, and delays contingency drafting on that basis.",
        "plausible_nonbias_interpretation": "Waiting for corroborating records before escalating could be framed as a legitimate preference for evidentiary completeness rather than an unwarranted expectation.",
        "strength": "moderate",
        "do_not_make_explicit": ["wishful thinking", "optimism bias", "cognitive bias"]
      },
      {
        "instance_id": "pf_01",
        "bias": "Planning fallacy",
        "decision_point": 4,
        "mechanism": "Analyst estimates the remaining workload using a best-case, no-rework task sequence, disregarding known historical base rates for comparable cross-border verification cases and the presence of competing case demands, resulting in an estimate substantially shorter than typical completion times.",
        "affected_reasoning_operation": "Time/effort estimation for task completion",
        "evidence_available_at_time": [
          "Historical base rate of 5-7 business days for comparable verification cases",
          "Two other active cases still requiring partial attention",
          "A best-case task sequence with no anticipated rework"
        ],
        "required_textual_manifestation": "Analyst explains arriving at a 2-day estimate by walking through the ideal task sequence, without referencing or adjusting for the historical base rate or the competing caseload, and this estimate is later overtaken by an unanticipated reconciliation query and slower sign-off.",
        "plausible_nonbias_interpretation": "Estimating based on the planned task sequence could be seen as standard project scoping rather than a systematic underestimation error.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "cognitive bias", "underestimation"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, no control pairing requested."
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
      "Exactly 4 decision points planned, one per manifest bias, no bias sharing a decision point.",
      "Exactly one instance per bias per manifest (1x Wishful Thinking, 1x Belief bias, 1x Selective Attention Bias, 1x Planning fallacy) = 4 total instances.",
      "No bias labels, definitions, or psychological terminology to appear in the public interview.",
      "Each instance has a distinct evidence trace and a plausible non-bias interpretation to avoid mechanical proof of bias.",
      "Target interview length 1,350 words (acceptable range 1,215-1,485) achievable via 4 decision points with moderate probe density and no repetitive exposition.",
      "Consequences at each decision point are realistic and do not deterministically confirm bias (e.g., logistics counterparty pattern, entity mismatch discovery, correspondent delay, reconciliation query) — all plausible independent of bias status.",
      "Technical vocabulary list ensures domain realism; avoid-list ensures no leakage of bias terminology."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Wishful Thinking",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an unsupported expectation of a favorable outcome (records arriving in time) with no confirming evidence and contrary historical base rate."
      },
      {
        "bias": "Belief bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as accepting an argument's conclusion because it matches prior belief, while failing to evaluate the argument's logical/evidentiary validity despite an explicit flag."
      },
      {
        "bias": "Selective Attention Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as attention allocation driven by pattern familiarity, with a non-matching but relevant entity deprioritized without independent evaluation."
      },
      {
        "bias": "Planning fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a time estimate derived from a best-case task sequence that disregards known historical base rates and competing demands."
      }
    ],
    "target_bias_names": [
      "Wishful Thinking",
      "Belief bias",
      "Selective Attention Bias",
      "Planning fallacy"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Wishful Thinking", "requested_occurrences": 1 },
      { "bias": "Belief bias", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias", "requested_occurrences": 1 },
      { "bias": "Planning fallacy", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias" },
      { "instance_id": "bb_01", "bias": "Belief bias" },
      { "instance_id": "wt_01", "bias": "Wishful Thinking" },
      { "instance_id": "pf_01", "bias": "Planning fallacy" }
    ],
    "intended_decision_points": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias", "decision_point": 1 },
      { "instance_id": "bb_01", "bias": "Belief bias", "decision_point": 2 },
      { "instance_id": "wt_01", "bias": "Wishful Thinking", "decision_point": 3 },
      { "instance_id": "pf_01", "bias": "Planning fallacy", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sab_01",
        "bias": "Selective Attention Bias",
        "mechanism": "Attention allocated to pattern-matching entity (shared registered agent), non-matching relevant entity deprioritized without independent risk evaluation",
        "affected_reasoning_operation": "Evidence-selection / initial scoping",
        "evidence_source": "Alert batch metadata: registered-agent match vs. unrelated logistics counterparty",
        "distinctiveness_requirement": "Must be tied to the scoping act at intake, distinct in evidence source and moment from the belief-bias instance at decision point 2, which concerns argument evaluation rather than attention allocation."
      },
      {
        "instance_id": "bb_01",
        "bias": "Belief bias",
        "mechanism": "Conclusion-driven acceptance of vendor argument despite unverified premise flagged by a colleague",
        "affected_reasoning_operation": "Argument evaluation / evidence weighting",
        "evidence_source": "OSINT vendor report and colleague's flag on entity-matching validity",
        "distinctiveness_requirement": "Distinct reasoning operation (validity assessment of an argument) and evidence source (vendor report) from the attention-allocation act in decision point 1."
      },
      {
        "instance_id": "wt_01",
        "bias": "Wishful Thinking",
        "mechanism": "Unsupported expectation that outstanding records arrive in time, contrary to historical turnaround data, driving a delay in contingency drafting",
        "affected_reasoning_operation": "Prediction / risk forecasting",
        "evidence_source": "Correspondent bank historical turnaround record and absence of confirmation",
        "distinctiveness_requirement": "Distinct from bb_01 and sab_01 in that it concerns forecasting a future event under uncertainty rather than evaluating past evidence or allocating attention."
      },
      {
        "instance_id": "pf_01",
        "bias": "Planning fallacy",
        "mechanism": "Best-case task-sequence estimate ignoring historical base rate and competing caseload",
        "affected_reasoning_operation": "Time/effort estimation",
        "evidence_source": "Historical base rate for comparable cases and current competing case list",
        "distinctiveness_requirement": "Distinct from wt_01 in that it concerns a self-generated task-duration estimate rather than an expectation about an external party's action."
      }
    ],
    "intended_strength": [
      { "instance_id": "sab_01", "bias": "Selective Attention Bias", "strength": "subtle" },
      { "instance_id": "bb_01", "bias": "Belief bias", "strength": "moderate" },
      { "instance_id": "wt_01", "bias": "Wishful Thinking", "strength": "moderate" },
      { "instance_id": "pf_01", "bias": "Planning fallacy", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_4",
    "domain_id": "IA",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias assigned to a distinct decision point (1:1 mapping across the 4 decision points), chosen for mechanism fit: attention/scoping at intake (DP1), argument evaluation of external evidence (DP2), forecasting under uncertainty (DP3), and self-estimation of task duration (DP4). No bias shares a decision point, so the 'two occurrences at one decision point' distinctiveness rule was not triggered.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the participant's case narrative for affirmative, mechanism-grounded cognitive bias occurrences; self-reported reasoning and decisions were treated as primary evidence, with retrieved passages used for taxonomy and mechanism validation."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "optimism bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "planning fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment", "insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial salient cue and to make insufficient adjustments from that anchor when forming subsequent judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial scoping of the Meridian Trading alert batch",
      "decision_point_description": "Deciding which counterparties in the alert batch to prioritize for detailed review",
      "affected_reasoning_operation": "Attention allocation and initial risk prioritization",
      "bias_specific_mechanism": "The registered-agent overlap with a prior successful case acted as a salient anchor; under heavy alert volume, the participant made an insufficient adjustment toward the logistics counterparty and treated it as low priority.",
      "manifestation_in_interview": "The participant focused initial workup on Meridian and its immediate corporate web while setting aside the logistics counterparty despite the broad alert batch.",
      "effect_on_reasoning_or_decision": "The logistics counterparty was not meaningfully examined in the initial scoping; a later unusual same-day wire pattern was missed and the team lead questioned the omission.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given the registered-agent overlap with the prior case, I focused my initial workup on Meridian and its immediate corporate web — pulling registry filings, past KYC refresh notes, that kind of thing. The logistics counterparty I noted but set aside as lower priority since it didn't fit any typology I'd seen before.",
          "evidence_explanation": "Shows that a single prior-case similarity anchored the initial scoping and led to prioritizing one entity while explicitly setting aside another."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the registered-agent match jumped out immediately. That pattern had been reliable before — same agent, similar shell structure, same region. With the volume we were under that week, I didn't feel I had the bandwidth to give equal weight to an entity that had no connection to anything I'd seen. I did glance at the logistics firm's file, but there was nothing that screamed 'look here,' so I moved on.",
          "evidence_explanation": "Demonstrates the salient anchor and insufficient adjustment under time pressure; a brief glance was not an adequate search for the logistics firm's risk."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My team lead actually asked why it wasn't in my initial scoping note. I didn't have a great answer beyond 'it didn't fit the pattern I was chasing.'",
          "evidence_explanation": "Indicates that the original scoping pattern persisted and the omission was later recognized as poorly justified."
        }
      ],
      "correction_or_counterevidence": "Team lead later questioned the omission. The participant's workload and the legitimate triage of a known typology provide a plausible non-bias explanation, but the salient anchor and insufficient adjustment are still evidenced.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The Rastogi et al. (2022) passage supports the anchoring-and-adjustment mechanism under time/resource constraints, although the transcript setting is not AI-assisted decision-making.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Anchoring-and-adjustment heuristic; adjustment away from an initial cue is resource-rational and time-dependent.",
          "relevance_to_this_occurrence": "Supports the mechanism that time/resource pressure can leave an actor anchored to an initial cue with insufficient adjustment, as described in the participant's initial scoping."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["myside bias", "selective evidence weighting"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, and weight evidence as confirming an existing hypothesis while discounting or failing to verify disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of the OSINT vendor report on Meridian",
      "decision_point_description": "Deciding whether to accept the vendor report's conclusion and whether to independently verify the disputed entity-matching step",
      "affected_reasoning_operation": "Evidence weighting and corroboration verification",
      "bias_specific_mechanism": "The vendor conclusion matched the participant's existing suspicion, so alignment itself was treated as confirmation; a junior analyst's disconfirming warning about the unverified entity-matching step was minimized as a technicality, and no independent verification was performed.",
      "manifestation_in_interview": "The participant folded the vendor report into the case file despite a specific unverified link; later document retrieval showed the entities were legally distinct.",
      "effect_on_reasoning_or_decision": "An unverified conclusion was incorporated into the case file, producing a later compliance challenge.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The bottom line matched exactly what I already suspected from the registered-agent overlap, so it felt like strong corroboration.",
          "evidence_explanation": "Shows that agreement with prior suspicion was treated as evidence of reliability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking that was a fair point to note, but it read to me as a technicality rather than something that undercut the conclusion, since the overall picture fit so well with what I was already building.",
          "evidence_explanation": "Demonstrates discounting of disconfirming evidence because it conflicted with the emerging case."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I treated the alignment itself as a kind of confirmation. I didn't go back and independently re-verify that specific entity-matching step before folding the report into the case file.",
          "evidence_explanation": "Explicitly states the confirmation mechanism and absence of verification."
        }
      ],
      "correction_or_counterevidence": "A junior analyst had already flagged the unverified entity-matching step. Later document pull showed the two entities were legally distinct; the bias influenced evidence weighting before the correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The Cook & Smallman (2008) passage supports confirmation bias in intelligence analysis, specifically selective prioritizing and weighting of evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2008",
          "retrieved_passage_or_finding": "The goals for this study were to document the extent of the conﬁrmation bias exhibited by ana- lysts working the initial steps of a problem. Results revealed no bias at as- sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias in selecting, prioritizing, and weighing evidence during intelligence analysis.",
          "relevance_to_this_occurrence": "The participant's selective weighting of the confirmatory vendor report and minimization of the conflicting entity-matching issue follow the same mechanism."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "optimism bias",
      "alternative_labels": ["wishful thinking", "desirability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overestimate the likelihood of favorable outcomes because desired outcomes influence subjective probability judgments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to wait for correspondent bank SWIFT records before drafting escalation",
      "decision_point_description": "Whether to draft the escalation immediately or hold for records from a historically slow correspondent bank",
      "affected_reasoning_operation": "Probability estimation and escalation timing",
      "bias_specific_mechanism": "The desired outcome—a complete case file and clean escalation—inflated the participant's subjective likelihood that requested records would arrive before the filing deadline, despite a known 12-15 day historical turnaround and only six days remaining.",
      "manifestation_in_interview": "The participant held off drafting the escalation based on the expectation that records would likely arrive; the bank then indicated another ten days.",
      "effect_on_reasoning_or_decision": "No contingency escalation path was drafted, creating later scramble when the records were delayed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I held off drafting it. I figured the records would probably come through in time — I wanted the file to be complete with that corroborating piece rather than submit something with a gap in it.",
          "evidence_explanation": "States that the wait decision was based on a favorable probability estimate tied to wanting a complete file."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, more that I wanted it to land that way. Nothing had actually changed with the correspondent bank's typical pace. On day six they came back and said it'd be another ten days.",
          "evidence_explanation": "Explicitly links the expectation to the desired outcome rather than changed evidence; subsequent bank response contradicted the favorable estimate."
        }
      ],
      "correction_or_counterevidence": "The team lead later flagged absence of a contingency escalation path; the bank's response disconfirmed the timely-arrival expectation. The biased expectation influenced decision before correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly addresses optimism bias or wishful thinking; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "planning fallacy",
      "alternative_labels": ["inside view", "optimistic time estimation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to underestimate task completion time by constructing an idealized step-by-step scenario while underweighting distributional information from comparable past tasks.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Estimation of remaining work time for Meridian case",
      "decision_point_description": "Estimating how many business days remained for reconciliation, narrative drafting, and compliance sign-off",
      "affected_reasoning_operation": "Time estimation and project planning",
      "bias_specific_mechanism": "The participant used an inside-view simulation that assumed no rework and did not reference comparable case base rates of five to seven days, despite also being stretched across other active cases.",
      "manifestation_in_interview": "The participant estimated two business days when comparable cases had historically taken five to seven days; reconciliation and sign-off extended beyond the estimate.",
      "effect_on_reasoning_or_decision": "The underestimation contributed to schedule slippage and further time pressure on the case.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "With reconciliation, narrative drafting, and compliance sign-off left, I estimated two business days. I walked through the sequence assuming everything went smoothly — no rework.",
          "evidence_explanation": "Demonstrates an inside-view, best-case scenario as the basis for the time estimate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Comparable cross-border verification cases have typically run five to seven days. I didn't really reference that when I made the call, and I still had two other active cases pulling at me.",
          "evidence_explanation": "Shows base-rate information was available but not used, a core planning-fallacy feature."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Reconciliation turned up a discrepancy that needed a follow-up query — cost an extra day. Sign-off took longer too, over a routine question I hadn't anticipated.",
          "evidence_explanation": "Documents that actual execution did not follow the smooth scenario and the estimate was too low."
        }
      ],
      "correction_or_counterevidence": "Actual task execution exceeded the estimate and the participant later acknowledged a colleague would likely flag the base rate. This was not corrected before the underestimation affected planning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly addresses planning fallacy; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial scoping of Meridian Trading alert batch",
      "supporting_interview_quote": "That pattern had been reliable before — same agent, similar shell structure, same region.",
      "plausible_mechanism": "Ease of recalling the prior successful case may have inflated subjective probability and drawn attention toward Meridian.",
      "why_not_identified": "The same evidence is already explained by an anchoring mechanism, and the transcript does not explicitly indicate recall ease as the operative distortion; therefore availability is treated as a plausible but unconfirmed candidate."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Analysis relies on a single retrospective self-report; post hoc rationalization cannot be fully excluded.",
    "Retrieved corpus support was OCR-noisy and directly covered only anchoring and confirmation bias; optimism bias and planning fallacy were classified using established cognitive-science knowledge.",
    "The evidence supports bias occurrence but does not rule out some contribution from legitimate triage and resource constraints, particularly in the initial scoping episode.",
    "No access to the underlying case file or independent documentation was available to verify decision inputs."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_4_Gemini_on",
  "interview_id": "IA_Biased_4",
  "system_prompt_id": "Gemini",
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
