You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time. Before we start, do you consent to discussing this incident for the interview?

Participant: Yes, go ahead.

Interviewer: Could you describe your role and the situation we'll be talking through?

Participant: I'm a Product Manager on the onboarding team at CollabHub. We're a B2B collaboration platform, mostly self-serve signups with some sales-assisted accounts that go through the same flow. About five weeks before a board review, we saw a jump in abandonment at account setup, and I had to figure out what to do about it without blowing up the sprint plan or the roadmap we'd already committed to.

Interviewer: What first alerted you to it?

Participant: Our weekly funnel dashboard. Drop-off at account setup increased 32% over three weeks, which was unusual because upstream traffic and acquisition numbers hadn't shifted. At that stage the dashboard only broke things down at a fairly coarse level, so I could see something had changed but not exactly where in the flow people were leaving. The VP of Product wanted an explanation fast because activation rate is one of the numbers the board tracks closely. Sales was also getting questions in a couple of active deals about whether we had more guided setup options, since that had come up in demos. Engineering had a full sprint already, mostly enterprise bug fixes.

Interviewer: What was your objective at that point?

Participant: Immediate goal was to understand the cause well enough to act. Longer term, protect activation rate and have something credible to show the board, without pulling engineering off commitments that mattered to existing customers.

Interviewer: Walk me through what happened, roughly in order.

Participant: First few days were spent figuring out whether the dashboard number was even reliable, then narrowing down where in the funnel people were dropping. Once we had a clearer signal, I had to decide how to respond — that's the piece that took the most judgment. After that came a staffing call, since the response required engineering time we didn't really have spare. Then, closer to the board date, there was a launch decision under time pressure with incomplete testing.

Interviewer: Let's start with the first decision — how you investigated.

Participant: Right. I had the 32% increase, no user feedback yet, and a note from our analyst that payment-step instrumentation was incomplete. Options were: commission proper interviews, which research said would take two weeks to get sessions running; do a fast internal analytics and heatmap pass; or scan what competitors were doing for quick context. I went with the analytics pass plus a light competitor scan, and deferred interviews. Five weeks isn't much runway once you add design, build, QA, and release, so waiting two weeks just for interviews to start felt like too much of the budget gone before we even had a direction.

Interviewer: Any downside to skipping interviews at that stage?

Participant: Sure — analytics tells you where people drop, not always why. I flagged that trade-off to the team and kept research on standby in case the data stayed ambiguous.

Interviewer: What came out of that analysis?

Participant: The sharper signal was abandonment right after the payment-detail field, concentrated in a newer account subgroup — about 140 users. Small, and the cohort had only existed a month, so I wasn't fully confident it was stable. The heatmaps showed some repeated field edits around payment, but because instrumentation there was incomplete, I couldn't tell if that was a validation error or people just backing out.

Interviewer: That brings us to the second decision — choosing how to respond.

Participant: This was the harder one. I had two things in front of me. On one side, the payment-field signal, real but statistically thin. On the other, our Sales director told me two active enterprise deals had specifically asked, during demos, whether we had a more guided setup experience — not a general market comment, two named accounts with real revenue attached. Around the same time I'd noticed a few competitors had shipped something similar, but that wasn't really what drove the call for me.

Interviewer: What did drive it?

Participant: Honestly, it was close. The deal-specific requests gave me something concrete to point to — an actual account, an actual objection in a sales cycle — whereas the internal cohort data, while suggestive, was small enough that I didn't want to bet three sprints on it alone. I decided to build the guided setup wizard, partly because of those two deals, partly because I wasn't confident the payment-field fix alone would move the number given how thin the sample was. I'll be honest, if I look back at it, I'm not entirely sure I weighted that correctly — it's possible a more targeted fix would have addressed the real problem faster, or it's possible the deal risk was the right thing to prioritize. I don't think the data gave a clean answer either way.

Interviewer: Did you consider testing both directions before committing?

Participant: Our analyst suggested a small controlled comparison — one version fixing payment fields, another adding limited guidance — before committing engineering time. I didn't go that route because it would have delayed a decision the deals needed answered, and because I felt the payment data alone wasn't strong enough to anchor the whole response.

Interviewer: If those two deals hadn't come up, would you have decided differently?

Participant: Probably, yes. Without that pressure I think I'd have leaned toward the payment-field fix first and treated broader onboarding changes as a separate, later initiative.

Interviewer: Third decision — staffing.

Participant: Building the wizard meant pulling two engineers off the bug backlog for three sprints. That backlog had real enterprise-reported defects sitting in it. Sales wanted the wizard ready to reference in the two deals. I chose full reallocation rather than splitting time or delaying, because a split effort usually means both things ship late and half-tested, in my experience.

Interviewer: What followed?

Participant: Two of those backlog tickets escalated in severity while the engineers were reassigned. Not an outage, but real friction for those customers. Wizard build stayed on schedule. Follow-up analytics also showed the payment-field friction hadn't changed, which wasn't surprising since we hadn't touched that code.

Interviewer: Fourth decision — the launch itself.

Participant: Four days before the board meeting, QA had only done partial regression testing, the canary group was too small to read cleanly, and payment abandonment was unchanged. Options were full launch, a longer 10% canary, or a one-week delay for better testing and instrumentation. I chose full launch. A longer canary wouldn't have given us clean results in time, and delaying meant showing up to the board with a plan instead of something shipped. Engineering and QA weren't thrilled, but agreed the risk was manageable with monitoring and a rollback ready.

Interviewer: What were the results?

Participant: No statistically meaningful change in activation rate versus the prior month, and support tickets kept mentioning the payment step. Not a disaster, but not the fix either. We shifted focus afterward to a proper look at the payment validation and getting the instrumentation gap closed.

Interviewer: With two more weeks before the board review, what would you change?

Participant: I'd have run that controlled comparison the analyst proposed, and probably gotten a handful of user sessions from the affected cohort before committing three sprints anywhere.

Interviewer: What information would have made the second decision clearer at the time?

Participant: A larger, stable sample showing payment friction was the dominant cause, or direct evidence from users about why they stopped there. Either would have given me more to weigh against the deal pressure.

Interviewer: And if the payment-field data had come from a larger cohort?

Participant: I think it would have carried more weight against the deal requests. Hard to say for certain — it's the kind of call where reasonable people could have gone either way with what we actually had.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "IS_Ambigious_1",
    "domain_id": "IS",
    "domain": "Information Systems, human-computer interaction, and interaction design",
    "role": "Product Manager (Digital Platform)",
    "condition": "ambiguous_control",
    "generation_specification": {
      "scenario_title_internal": "The Onboarding Wizard Decision at CollabHub (Ambiguous Control)",
      "scenario_summary_internal": "A PM at CollabHub, a mid-size B2B collaboration platform, investigates a 32% drop-off at the account-setup step of the signup funnel ahead of a Q3 board review. The incident mirrors the paired scenario's structure, actors, constraints, and four decision points, but decision point 2 is written so that the choice between building an AI-guided setup wizard and fixing a payment-field issue remains genuinely underdetermined: the PM weighs a small, unstable internal cohort signal against a strategic feature-parity consideration raised by Sales, and the record leaves multiple reasonable readings of the decision open without any evidence-weighting pattern that privileges adoption prevalence itself.",
      "occupational_realism": {
        "objective": "Diagnose and reduce a sudden increase in signup-funnel drop-off before the quarterly board review, without destabilizing the sprint roadmap.",
        "setting": "Mid-size B2B SaaS collaboration platform, in-house product team, four-week sprint window, distributed team using shared analytics dashboards and a cross-company PM Slack community.",
        "constraints": [
          "Board review in five weeks",
          "Limited engineering capacity shared with a bug-fix backlog",
          "Small internal user-research team with a two-week interview lead time",
          "Incomplete instrumentation on the payment step of the funnel",
          "Pressure from sales leadership citing competitor feature parity"
        ],
        "stakeholders": [
          "Product Manager (protagonist)",
          "VP of Product",
          "Engineering lead",
          "Data analyst",
          "UX researcher",
          "Sales director",
          "External peer PMs in industry Slack community"
        ],
        "technical_terms_to_use": [
          "onboarding funnel",
          "activation rate",
          "cohort analysis",
          "drop-off step",
          "SSO",
          "funnel instrumentation",
          "canary release",
          "sprint capacity",
          "feature parity",
          "heatmap analytics"
        ],
        "technical_terms_to_avoid": [
          "herding",
          "bandwagon effect",
          "social proof",
          "conformity bias",
          "peer pressure",
          "groupthink",
          "cognitive bias",
          "irrational",
          "everyone is doing it"
        ]
      },
      "timeline": [
        {
          "phase": 1,
          "decision_point": true,
          "facts_available_before_decision": [
            "Weekly dashboard shows a 32% drop-off increase at the account-setup step over three weeks",
            "No qualitative user feedback yet collected",
            "Data analyst flags that instrumentation on the payment sub-step is incomplete"
          ],
          "new_information_after_decision": [
            "Funnel analytics show elevated abandonment specifically after the payment-detail field, not the initial account fields",
            "A quick competitor teardown reveals three peers have shipped new onboarding patterns in the last month"
          ],
          "alternatives": [
            "Commission a two-week qualitative user-interview study",
            "Run an internal funnel/heatmap analytics deep dive this week",
            "Skim publicly available competitor teardown reports for quick signal"
          ],
          "intended_action": "PM combines a rapid internal analytics review with a light competitor scan, deferring formal interviews due to the board timeline."
        },
        {
          "phase": 2,
          "decision_point": true,
          "facts_available_before_decision": [
            "Internal cohort data suggests the sharpest abandonment occurs right after the payment-detail field, in a subgroup added last month",
            "Three named competitor platforms have shipped an 'AI-guided setup wizard' pattern within the last six weeks",
            "Sales director reports that two active enterprise deals specifically asked about guided onboarding during demos",
            "Internal sample size for the affected cohort is small (approximately 140 users) and not yet statistically stable"
          ],
          "new_information_after_decision": [
            "Engineering estimates the wizard will take three sprints to build",
            "A follow-up analytics review (after the decision) shows the payment-field friction persists independent of the wizard concept"
          ],
          "alternatives": [
            "Build the AI-guided setup wizard raised in the deal conversations",
            "Run a targeted fix on the payment-field step identified in internal cohort data",
            "Run a small controlled A/B test comparing a wizard concept against a payment-field fix before committing engineering resources"
          ],
          "intended_action": "PM commits to building the wizard, citing a mix of the specific deal-related requests and reservations about the small internal sample, while leaving open whether the payment-field signal would have been prioritized under different sales circumstances."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "Engineering lead confirms building the wizard requires reallocating two engineers from the bug-fix backlog for three sprints",
            "Backlog contains several unresolved defects reported by enterprise customers",
            "Sales director requests wizard prioritization to support two active deals"
          ],
          "new_information_after_decision": [
            "Two enterprise bug tickets escalate in severity during the reallocation window",
            "Engineering reports the wizard build is on schedule but payment-field code is untouched"
          ],
          "alternatives": [
            "Fully reallocate engineers to the wizard build",
            "Split capacity between a partial wizard build and the payment-field fix",
            "Delay the wizard and prioritize the escalating backlog defects"
          ],
          "intended_action": "PM authorizes full reallocation to the wizard build, deferring the backlog defects and the payment-field fix."
        },
        {
          "phase": 4,
          "decision_point": true,
          "facts_available_before_decision": [
            "QA has completed only partial regression testing due to compressed schedule",
            "Board review is in four days",
            "Early canary metrics on the wizard are inconclusive due to low traffic",
            "Payment-field abandonment metric has not moved"
          ],
          "new_information_after_decision": [
            "Post-launch activation rate shows no statistically significant change versus the prior month",
            "Support tickets mention continued difficulty at the payment step"
          ],
          "alternatives": [
            "Launch the wizard to 100% of new signups before the board review",
            "Launch to a 10% canary cohort and monitor for one more week",
            "Delay launch one week to complete regression testing and add payment-field instrumentation"
          ],
          "intended_action": "PM launches to 100% of new signups ahead of the board review, accepting the incomplete regression testing."
        }
      ],
      "probe_plan": {
        "opening": [
          "Can you walk me through what first alerted you to the onboarding problem?",
          "What was your primary objective when you started looking into this?"
        ],
        "timeline_reconstruction": [
          "What happened first, and what did you look at next?",
          "At what point did the sales conversations enter your thinking?",
          "How did the internal cohort data evolve as you worked through this?"
        ],
        "decision_point_probes": [
          "What information did you have in front of you at that moment?",
          "What sources did you weigh most heavily, and why?",
          "What alternatives did you consider, and why did you rule them out?",
          "What was your goal at that specific point in the process?",
          "Had you handled a similar situation before? How did that shape this decision?",
          "How much time pressure did you feel at that point?",
          "How confident were you in the data you had?",
          "If the deal-related requests hadn't come up, would you have decided differently?"
        ],
        "closing_hypotheticals": [
          "If you had two more weeks before the board review, what would you have done differently?",
          "If the payment-field signal had come from a larger sample, would that have changed your decision at that stage?",
          "Looking back, what would you tell a peer PM facing a similar mix of signals?"
        ]
      },
      "occurrence_embedding_plan_internal": [],
      "control_specification": {
        "paired_scenario_id": "IS_Biased_1",
        "features_to_match": [
          "Domain vocabulary (onboarding funnel, activation rate, cohort analysis, drop-off step, SSO, funnel instrumentation, canary release, sprint capacity, feature parity, heatmap analytics)",
          "Narrative structure and chronology (diagnosis, redesign-approach choice, staffing allocation, launch decision)",
          "Actor set (PM, VP of Product, Engineering lead, data analyst, UX researcher, Sales director, external peer PMs)",
          "Difficulty level (moderate) and emotional tone (time-pressured but professional)",
          "Exactly four decision points with at least two plausible alternatives each",
          "Consequences that remain inconclusive about whether decision point 2 was well-founded"
        ],
        "features_to_remove_or_change": [
          "Remove the explicit framing where adoption prevalence among competitors and peer PMs is cited as the primary justification for the wizard decision",
          "Replace the industry-Slack-group adoption-prevalence narrative with a concrete, deal-specific sales request as one of two co-equal considerations",
          "Ensure the internal cohort signal (payment-field friction) is acknowledged with comparable weight to the external consideration, so no single evidence source dominates the stated rationale"
        ],
        "ambiguity_boundary": "The decision at phase 2 must remain genuinely underdetermined: a reader should be able to interpret it either as a reasonable strategic bet motivated by specific, named deal risk, or as an instance of insufficient weight given to a small but concrete internal signal, without the interview supplying evidence that adoption prevalence, competitor volume, or peer conformity was the operative justification. No wording may state or imply that the wizard was chosen because 'others are doing it' or because of the sheer number of competitors/peers adopting the pattern; the PM's stated reasons must reference specific, individuated business facts (two named deals) rather than aggregate popularity."
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
        "Zero intentional Herding instances planned anywhere in the interview, including decision point 2",
        "Decision point 2 reasoning references two specific named deals rather than aggregate competitor/peer adoption volume, preserving ambiguity without instantiating the target bias",
        "No bias vocabulary appears in probe_plan or timeline text",
        "All four decision points retain at least two plausible alternatives and inconclusive consequences",
        "Structure, actor set, vocabulary, and difficulty match paired scenario IS_Biased_1",
        "Word count target 1,350 (range 1,215-1,485) achievable given 4 decision points with moderate probe depth and no embedded bias instance"
      ]
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "ambiguous_control",
      "exact_occurrence_manifest": [
        {
          "bias": "Herding",
          "occurrences": 0,
          "mechanism_constraint": "Must not be intentionally instantiated; decision point 2 must rely on individuated, named deal facts rather than aggregate adoption-prevalence framing."
        }
      ],
      "target_bias_names": [
        "Herding"
      ],
      "requested_occurrence_count_for_each_bias": [
        {
          "bias": "Herding",
          "requested_occurrences": 0
        }
      ],
      "planned_instance_ids": [],
      "intended_decision_points": [],
      "intended_mechanisms": [],
      "intended_strength": [],
      "paired_scenario_id": "IS_Biased_1",
      "counterfactual_variable": {
        "name": null,
        "original_state": null,
        "changed_state": null,
        "variables_to_hold_constant": []
      },
      "scenario_id": "IS_Ambigious_1",
      "domain_id": "IS",
      "total_requested_occurrences": 0,
      "total_planned_occurrences": 0,
      "allocation_rule_used": "Not applicable; manifest requests zero occurrences of the paired target bias (Herding), so no allocation across decision points was performed. Decision point 2 was instead rewritten to preserve narrative ambiguity by substituting individuated deal-specific evidence for the aggregate adoption-prevalence framing used in the paired biased scenario, per the ambiguous_control condition rules.",
      "control_zero_bias_requirement": true,
      "variables_to_hold_constant": [
        "Domain (Information Systems / HCI / interaction design)",
        "Role (Product Manager, Digital Platform)",
        "Scenario premise (CollabHub onboarding funnel drop-off before Q3 board review)",
        "Four decision points and their sequencing",
        "Actor set and stakeholder roles",
        "Technical vocabulary and difficulty level (moderate)",
        "Overall word count target and range",
        "Inconclusive consequence pattern at each decision point"
      ],
      "generation_warnings": [
        "Input specified counterfactual_variable as 'AUTOSELECT', but condition is 'ambiguous_control' (not 'counterfactual'), so no counterfactual variable was selected; counterfactual_specification and counterfactual_variable fields are set to null to avoid fabricating an unrequested experimental factor.",
        "Because this is a control paired against IS_Biased_1, decision point 2 was deliberately rewritten (deal-specific facts replacing aggregate adoption-prevalence framing) to preserve genuine ambiguity while matching structure; this substitution is a control-fidelity requirement, not an unintended bias instance."
      ]
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
          "segment_type": "investigation_choice",
          "raw_interview_anchor": "I went with the analytics pass plus a light competitor scan, and deferred interviews.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden manifest requests zero Herding occurrences and no other intentional bias instance is present."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "tradeoff_and_contingency",
          "raw_interview_anchor": "Analytics tells you where people drop, not always why. I flagged that trade-off to the team and kept research on standby.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant explicitly recognizes the limitation of the selected evidence and retains a fallback research option; the hidden zero-bias manifest has no instance here."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "evidence_interpretation",
          "raw_interview_anchor": "The sharper signal was abandonment right after the payment-detail field, concentrated in a newer account subgroup — about 140 users.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a qualified interpretation of incomplete cohort and heatmap evidence, not an intentionally embedded hidden bias instance."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "response_selection",
          "raw_interview_anchor": "The deal-specific requests gave me something concrete to point to ... I decided to build the guided setup wizard.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Decision point 2 was deliberately rewritten to use two named deal requests and a small internal cohort signal, preserving ambiguity without instantiating Herding or another hidden target."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "experiment_rejection",
          "raw_interview_anchor": "I didn't go that route because it would have delayed a decision the deals needed answered, and because I felt the payment data alone wasn't strong enough.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant explains why a controlled comparison was rejected; no hidden occurrence is planned in this control interview."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "resource_allocation",
          "raw_interview_anchor": "I chose full reallocation rather than splitting time or delaying, because a split effort usually means both things ship late and half-tested.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a stated staffing trade-off with a plausible operational rationale and no hidden bias instance."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "launch_decision",
          "raw_interview_anchor": "I chose full launch. A longer canary wouldn't have given us clean results in time, and delaying meant showing up to the board with a plan instead of something shipped.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The launch decision is intentionally non-diagnostic in the hidden control manifest; time pressure and a risk trade-off do not establish a hidden bias."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "post_launch_action",
          "raw_interview_anchor": "We shifted focus afterward to a proper look at the payment validation and getting the instrumentation gap closed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a corrective follow-up action based on post-launch evidence; the hidden manifest contains no planned instance."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": ["Interviewer", "Participant"],
      "retrieved_corpus_support_used": true,
      "analysis_scope_note": "Conservative, mechanism-first review of the CTA transcript for affirmative evidence of bias-specific mechanisms; time pressure, resource constraints, and ordinary uncertainty were treated as competing explanations unless a distinct cognitive mechanism was present."
    },
    "identified_bias_summary": [
      {
        "bias_label": "plan continuation bias",
        "identified_occurrence_count": 1
      }
    ],
    "identified_occurrences": [
      {
        "occurrence_id": "obs_001",
        "classification_status": "identified",
        "confidence": "low",
        "bias_label": "plan continuation bias",
        "alternative_labels": ["get-there-itis", "plan continuation error"],
        "taxonomy_status": "established_label",
        "bias_definition": "A cognitive bias in which a person continues with an established plan or course of action despite new or accumulating cues that the plan should be revised, delayed, or abandoned.",
        "attributed_to_speaker": "Participant",
        "evidence_speaker": "Participant",
        "decision_episode_label": "Launch decision under time pressure before board review",
        "decision_point_description": "Four days before the board review, with only partial regression testing, an unreadable canary, and unchanged payment abandonment, the participant selected full launch over a longer 10% canary or a one-week delay for better testing and instrumentation.",
        "affected_reasoning_operation": "Deciding whether to launch the guided setup wizard despite unresolved validation evidence",
        "bias_specific_mechanism": "Plan continuation bias: the participant continued the existing launch course despite cues that delayed or limited launch was warranted, including partial regression testing, a canary group too small to read cleanly, and payment-step friction unchanged, with the stated reason that delay would mean showing up to the board without something shipped.",
        "manifestation_in_interview": "The participant explicitly lists the unresolved testing and evidence signals and then chooses full launch rather than revising the plan.",
        "effect_on_reasoning_or_decision": "The decision led to a full launch that produced no statistically meaningful activation improvement and did not address the payment-step issue; a more cautious delay or longer canary was rejected.",
        "interview_evidence": [
          {
            "speaker": "Participant",
            "verbatim_quote": "Four days before the board meeting, QA had only done partial regression testing, the canary group was too small to read cleanly, and payment abandonment was unchanged. Options were full launch, a longer 10% canary, or a one-week delay for better testing and instrumentation. I chose full launch.",
            "evidence_explanation": "This quote establishes the presence of cues suggesting caution and the selection of the plan-continuation option, full launch."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "A longer canary wouldn't have given us clean results in time, and delaying meant showing up to the board with a plan instead of something shipped.",
            "evidence_explanation": "This quote shows the commitment to the existing launch timeline and board-facing progress, rather than revisiting the plan in light of unresolved validation evidence."
          }
        ],
        "correction_or_counterevidence": "Engineering and QA reportedly judged the risk manageable with monitoring and rollback readiness, and the launch did not result in an outage; the decision may also reflect legitimate time pressure and board-related organizational incentives rather than a purely cognitive bias.",
        "retrieved_corpus_support_available": true,
        "corpus_support_note": "The retrieved corpus names plan continuation bias as a common operational cognitive bias, but provides limited definitional detail; therefore the definition and mechanism explanation draw on general cognitive-science knowledge.",
        "corpus_evidence": [
          {
            "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
            "paper_title": null,
            "authors": null,
            "publication_year": null,
            "retrieved_passage_or_finding": "confirmation, expectation, and plan continuation , and in some cases multiple biases",
            "mechanism_supported_by_source": "The source identifies plan continuation as one of the common cognitive biases in operational incidents, supporting the use of an established label rather than a novel one.",
            "relevance_to_this_occurrence": "The launch decision shows a similar operational pattern of continuing a planned course despite unresolved cues."
          }
        ]
      }
    ],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "availability heuristic",
        "alternative_labels": ["salience bias", "vividness bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Choosing guided setup wizard versus targeted payment-field fix",
        "supporting_interview_quote": "The deal-specific requests gave me something concrete to point to — an actual account, an actual objection in a sales cycle — whereas the internal cohort data, while suggestive, was small enough that I didn't want to bet three sprints on it alone.",
        "plausible_mechanism": "Availability/salience: two recent, concrete enterprise-deal objections were more vivid and accessible than the abstract internal cohort data, potentially leading to disproportionate weighting of the deal anecdotes in prioritization.",
        "why_not_identified": "The transcript supports that the deal requests influenced the decision, but it does not clearly demonstrate that ease of recall or vividness, rather than legitimate revenue/account risk, produced the weighting; the participant himself notes the data were ambiguous and that deal risk may have been the right priority."
      }
    ],
    "no_supported_biases_found": false,
    "limitations": [
      "Launch decision has a substantial competing non-bias explanation from time pressure and board-related organizational incentives, limiting confidence in the plan-continuation classification.",
      "Retrieved corpus coverage for plan continuation bias is sparse and mostly names the bias rather than providing a detailed mechanism.",
      "The transcript is self-reported and retrospective, so some reasoning is reconstructed rather than directly observed."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Ambigious_1_Sonnet_on",
  "interview_id": "IS_Ambigious_1",
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
