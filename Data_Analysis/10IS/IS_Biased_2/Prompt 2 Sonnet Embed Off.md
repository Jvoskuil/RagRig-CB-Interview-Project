You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a cognitive task analysis session—I'll be asking about a specific incident you worked through, and I'd like your candid recollection of how you reasoned through it, not a polished after-the-fact summary. Everything stays anonymized. Is that okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me your role and what you were responsible for during this incident?

Participant: I lead a five-person team on our internal analytics platform—basically the tooling our support organization uses to look up customer accounts, usage history, that kind of thing. I own delivery for that dashboard and I report into the VP of Engineering. During this period I was accountable for keeping the platform stable and also for a demo we had coming up for leadership.

Interviewer: Can you walk me through what first alerted you to a problem?

Participant: Load times on the dashboard started creeping up—support tickets came in complaining pages were taking six, seven seconds instead of two. Over about two weeks it basically tripled. We hadn't touched much in that subsystem recently except our caching layer, which we'd built in-house—we call it QuickCache—about eight months earlier.

Interviewer: What did you do first?

Participant: I had two real options—run broad instrumentation across the whole stack to be safe, or go straight at QuickCache since it was the most recent change and the timing lined up. We were also getting pressure from the support lead because tickets kept climbing, so I didn't want to spend a week doing exhaustive profiling everywhere. I told the team to profile QuickCache specifically first, since it was the most likely suspect given the timing, and if that came back clean we'd widen the net.

Interviewer: What came out of that?

Participant: Profiling confirmed QuickCache was adding real latency under high load—invalidation was firing more than it should, forcing extra database round-trips. It also surfaced a separate, unrelated issue: a missing index on one of the support tables. Neither of those was hugely surprising, but it did mean two independent things needed fixing, not one.

Interviewer: How did the investigation affect team workload?

Participant: Priya, who originally built QuickCache, took point on diagnosing the invalidation logic. Dev, one of our other senior engineers, has also worked deep in that code. Everyone else picked up the index fix and other tickets. That's roughly how the two weeks split.

Interviewer: Let's step through it chronologically. After profiling confirmed the QuickCache issue, what was the next major decision?

Participant: That's where it got harder. QuickCache had taken us about eight months to build and stabilize—three separate patch rounds just to get it production-ready in the first place. Priya was adamant we were close, that one more targeted patch to the invalidation logic would fix it. On the other hand, there's a mature Redis-backed option out there that could probably replace QuickCache in about a sprint, with a track record we could actually point to.

Interviewer: What did you decide?

Participant: I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up. I figured one more focused patch, with the team that knows it best, would get us there.

Interviewer: What information did you rely on most heavily for that call?

Participant: Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily.

Interviewer: What happened after that decision?

Participant: The patch only bought us about fifteen percent improvement. Not enough to hit the demo deadline. And the extra sprint stretched the team thin on top of everything else going on.

Interviewer: Third decision point—who owned the urgent fix at that stage?

Participant: Right, so at this point we're down to days, not weeks. Dev has the deepest knowledge of QuickCache internals, but Dev had also been at the center of a production outage about three weeks earlier—a rushed deploy under pressure that caused a real incident, though the postmortem showed it was handled well and fixed fast. Marcus was the other option; he's been solid but has missed several deadlines over the past year, nothing dramatic, just a slower, steadier pattern of slipping.

Interviewer: What did you decide, and why?

Participant: I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet.

Interviewer: How did that play out?

Participant: Handoff was messy—Dev had context Marcus didn't, so there was friction getting him up to speed, and the fix took longer than it would have with Dev leading it outright.

Interviewer: Looking back, how did you weigh Dev's eighteen months of strong delivery against that one incident?

Participant: I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either.

Interviewer: With three days left before the demo, what did you decide about reporting status?

Participant: Latency was better but not fully resolved. I could've asked to push the demo, shipped quietly and hoped nobody noticed the remaining lag, or just told leadership straight where things stood. I went with transparency—laid out what was fixed, what wasn't, and proposed a follow-up sprint with monitoring in place. They accepted that.

Interviewer: What was the reasoning behind choosing that option over delaying the demo?

Participant: Delaying felt like it would cost more politically than it would gain technically—the partial fix was real progress, and monitoring would catch anything that slipped. Hiding it wasn't really on the table once I thought about it seriously.

Interviewer: If you'd had the profiling data suggesting a structural rework earlier, would that have changed your patch-versus-switch decision?

Participant: Possibly. If I'd seen it that clearly before committing the extra sprint, I might have pushed harder for the parallel evaluation option instead.

Interviewer: If Dev's outage had happened a year earlier rather than three weeks before this decision, would you have assigned the fix differently?

Participant: Probably, yeah. With more distance from it, I likely would have just given it to him outright given his familiarity with the system.

Interviewer: Anything you'd tell a peer facing a similar in-house-build-versus-alternative call?

Participant: Try to separate how much you've already put into something from what it's actually going to cost you going forward. Easier said than done when your team's pride and expertise are wrapped up in it.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IS_Biased_2",
  "domain_id": "IS",
  "domain": "Information Systems, human-computer interaction, and interaction design",
  "role": "Software Engineering Team Lead",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The QuickCache Crossroads",
    "scenario_summary_internal": "A software engineering team lead must resolve a worsening performance problem in an internal support-operations dashboard before a quarterly leadership demo. The in-house caching layer the team built eight months ago ('QuickCache') is implicated. Over four chronological decision points, the lead triages the problem, decides how to respond to QuickCache's failure (continue investing vs. switch to a mature alternative), decides who should own the urgent fix given a team member's recent outage, and finally decides how to report status to leadership. The narrative embeds exactly one irrational-escalation instance (continued investment in QuickCache driven by prior sunk effort rather than forward-looking value) and exactly one negativity-bias instance (a single recent, vivid outage disproportionately shaping a personnel-risk judgment despite a strong overall track record).",
    "occupational_realism": {
      "objective": "Restore acceptable dashboard latency for the customer-support platform before a quarterly leadership demo, while managing team capacity and reputational risk.",
      "setting": "Mid-size SaaS company; internal analytics/support-ops platform team of five engineers reporting to the interviewee; two-week sprint window before a board-facing product demo.",
      "constraints": [
        "Hard deadline: leadership demo in two weeks, later compressed to three days",
        "Limited budget for new third-party tooling this quarter",
        "Team morale strained after a recent production incident",
        "Partial diagnostic visibility; full root-cause data arrives incrementally",
        "Only two engineers available with relevant caching-layer familiarity"
      ],
      "stakeholders": [
        "Team lead (interviewee)",
        "VP of Engineering",
        "Priya (senior engineer, original QuickCache designer)",
        "Dev (engineer involved in a recent production outage)",
        "Marcus (engineer with a longer history of missed deadlines)",
        "Product manager",
        "Customer support lead"
      ],
      "technical_terms_to_use": [
        "caching layer",
        "cache invalidation",
        "latency",
        "profiling",
        "technical debt",
        "incident postmortem",
        "feature flag",
        "on-call rotation",
        "rollback",
        "load testing"
      ],
      "technical_terms_to_avoid": [
        "sunk cost fallacy",
        "escalation of commitment",
        "negativity bias",
        "recency effect",
        "cognitive bias",
        "irrational escalation",
        "confirmation bias",
        "anchoring"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dashboard load times have tripled over two weeks",
          "Customer-support tickets about slow load are rising",
          "QuickCache was the last major change deployed to this subsystem",
          "No full-stack profiling has been run yet"
        ],
        "new_information_after_decision": [
          "Profiling confirms QuickCache adds latency under high load",
          "Profiling also surfaces an unrelated missing database index"
        ],
        "alternatives": [
          "Run full-stack instrumentation before attributing cause to any component",
          "Focus investigation narrowly on QuickCache since it was the most recent change",
          "Escalate immediately to the infrastructure team to check shared resource contention"
        ],
        "intended_action": "Lead orders targeted profiling of QuickCache based on the timing correlation with its deployment, a reasonable diagnostic narrowing rather than a biased inference; no intended bias instance at this phase."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "QuickCache took roughly eight months and three prior patch cycles to build and stabilize",
          "Each prior patch produced only marginal, temporary latency improvement",
          "A mature open-source Redis-backed alternative could replace QuickCache in about one sprint with known reliability characteristics",
          "Priya, who designed QuickCache, argues the team is 'nearly there' and one more patch will resolve it",
          "Leadership previously praised QuickCache publicly as strategic in-house IP"
        ],
        "new_information_after_decision": [
          "The additional patch yields only a 15% improvement, insufficient to meet the demo deadline",
          "Remaining timeline to a durable fix is now uncertain",
          "Team morale is further strained by the extended effort"
        ],
        "alternatives": [
          "Commit another sprint to further optimize QuickCache's invalidation logic",
          "Abandon QuickCache and migrate to the Redis-backed alternative",
          "Run both solutions in parallel behind a feature flag to compare before committing"
        ],
        "intended_action": "Lead commits an additional sprint to further patching QuickCache, citing the months of engineering time and specialized internal expertise already invested and a reluctance to 'waste' that work, even though the profiling data points toward a structural redesign rather than an incremental patch, and the alternative has a clearer risk profile."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dev had a production outage three weeks ago, traced to a rushed deploy under time pressure; the postmortem showed prompt, effective remediation and process fixes",
          "Dev otherwise has eighteen months of consistently strong reviews and on-time delivery, and the deepest working knowledge of QuickCache internals",
          "Marcus has a longer pattern of several missed deadlines over the past year, with no single dramatic incident",
          "The urgent fix requires deep QuickCache familiarity and must be delivered within days"
        ],
        "new_information_after_decision": [
          "Reassigning ownership away from Dev creates friction and confusion during handoff",
          "The fix takes longer than planned because the assigned engineer is less familiar with QuickCache internals"
        ],
        "alternatives": [
          "Assign the critical fix to Dev given his QuickCache expertise",
          "Assign the fix to Marcus to reduce load on Dev after the recent incident",
          "Pair Dev and Marcus so responsibility and risk are shared"
        ],
        "intended_action": "Lead sidelines Dev from the critical fix and assigns it to Marcus, weighting the vivid recent outage heavily against Dev despite his strong eighteen-month record and the incident's well-documented resolution, while treating Marcus's more diffuse pattern of missed deadlines as less concerning because it lacks a single salient episode."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The demo is three days away",
          "The fix is only partially effective; latency is improved but not fully resolved",
          "Leadership expects a status update ahead of the demo"
        ],
        "new_information_after_decision": [
          "Leadership accepts the partial-fix plan with monitoring",
          "A follow-up sprint is scheduled to complete the redesign"
        ],
        "alternatives": [
          "Present a transparent status update with a mitigation and monitoring plan",
          "Request a delay of the demo until the fix is complete",
          "Ship the partial fix silently without flagging remaining risk"
        ],
        "intended_action": "Lead presents a transparent status update proposing to ship the partial improvement with monitoring and a scheduled follow-up sprint, a defensible trade-off given the constraints; no intended bias instance at this phase."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first alerted you to a problem with the dashboard?",
        "What was your role and what were you responsible for delivering?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did QuickCache come into the picture?",
        "How did the team's workload and staffing shift over the two weeks?"
      ],
      "decision_point_probes": [
        "What cues made you focus on that particular explanation at the time?",
        "What information sources did you rely on for that decision, and were there others you didn't use?",
        "What were you ultimately trying to achieve when you made that call?",
        "What other options did you consider, and why did you rule them out?",
        "What was the main basis for the decision you made?",
        "Had you faced a similar situation before, and did that experience shape your choice?",
        "How much time pressure were you under at that point?",
        "How confident were you in the information you had when you decided?",
        "If you'd had more time or different information, would you have chosen differently?"
      ],
      "closing_hypotheticals": [
        "If QuickCache had been a vendor product instead of something your team built, would your approach have differed?",
        "If Dev's outage had happened a year earlier instead of three weeks before this decision, would you have assigned the fix differently?",
        "Looking back, what would you tell a peer facing a similar in-house-versus-alternative decision?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "decision_point": 2,
        "mechanism": "Continued commitment to further investment in QuickCache is justified primarily by the amount of time, effort, and internal expertise already sunk into it, rather than by a forward-looking comparison of expected cost, risk, and benefit against the available alternative.",
        "affected_reasoning_operation": "Resource-allocation decision under uncertainty; weighting of prior investment against prospective outcomes",
        "evidence_available_at_time": [
          "Eight months and three prior patch cycles already invested in QuickCache",
          "Prior patches produced only marginal, temporary gains",
          "A lower-risk, faster alternative exists with known reliability",
          "Profiling data suggests a structural redesign, not a patch, is needed"
        ],
        "required_textual_manifestation": "The lead's stated rationale for choosing another patch cycle explicitly invokes the time/effort already spent or the team's specialized expertise as a reason to continue, rather than citing a forward-looking comparison showing the patch path is expected to outperform switching.",
        "plausible_nonbias_interpretation": "The lead could defensibly argue that in-house control, avoided vendor dependency, or long-term customization benefits outweigh switching costs, provided that reasoning rests on those forward-looking benefits rather than on the sunk months already spent.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "sunk cost",
          "escalation of commitment",
          "irrational escalation",
          "any explicit bias label"
        ]
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "decision_point": 3,
        "mechanism": "A single vivid, recent negative event (Dev's outage) is given disproportionate weight in a personnel-risk judgment relative to a larger, more diffuse body of both positive (Dev's eighteen-month record) and comparably negative (Marcus's repeated missed deadlines) evidence.",
        "affected_reasoning_operation": "Risk assessment and task-assignment judgment based on weighting of historical performance evidence",
        "evidence_available_at_time": [
          "Postmortem showing the outage was promptly and effectively remediated",
          "Eighteen months of consistently strong performance reviews for Dev",
          "Marcus's pattern of several missed deadlines over the past year",
          "Dev has the deepest technical familiarity with QuickCache"
        ],
        "required_textual_manifestation": "The lead's explanation for reassigning the task centers on the vividness or recency of Dev's single incident, while explicitly or implicitly discounting Marcus's more numerous but less salient shortfalls, without citing a specific unresolved skill or trust gap tied to the outage.",
        "plausible_nonbias_interpretation": "The lead could defensibly argue caution is warranted after any recent incident before assigning a mission-critical task, provided that reasoning is grounded in a specific, still-unresolved capability concern rather than the sheer salience of one recent event.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "negativity bias",
          "recency effect",
          "availability heuristic",
          "any explicit bias label"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition interview, not a control."
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
      "Confirm exactly one Irrational Escalation instance appears, located at decision point 2, tied to the QuickCache patch-vs-switch choice.",
      "Confirm exactly one Negativity Bias instance appears, located at decision point 3, tied to the Dev-vs-Marcus assignment choice.",
      "Confirm decision points 1 and 4 contain no intentionally embedded instances of either named bias.",
      "Confirm no bias labels, definitions, or psychological terminology appear anywhere in the public interview text.",
      "Confirm each embedded instance includes both the biased rationale and a plausible non-bias alternative reading, without resolving which applies.",
      "Confirm the interview contains exactly four decision points, each with at least two alternatives, pre-decision facts, and post-decision new information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count falls within 1,215-1,485 words without repetitive exposition padding.",
      "Confirm consequences described do not mechanically prove or disprove whether either decision was biased."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Irrational Escalation",
        "occurrences": 1,
        "mechanism_constraint": "Must be justified via prior sunk time/effort/expertise, not forward-looking cost-benefit reasoning"
      },
      {
        "bias": "Negativity Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must involve disproportionate weight on one vivid recent negative event versus a larger body of mixed/positive evidence"
      }
    ],
    "target_bias_names": [
      "Irrational Escalation",
      "Negativity Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Irrational Escalation",
        "requested_occurrences": 1
      },
      {
        "bias": "Negativity Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "decision_point": 2
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "mechanism": "Continued investment decision justified by prior sunk effort (eight months, three patch cycles, internal expertise) rather than forward-looking expected value of the alternative solution",
        "affected_reasoning_operation": "Resource-allocation choice under uncertainty",
        "evidence_source": "History of QuickCache development effort and prior patch outcomes versus profiling-based redesign recommendation",
        "distinctiveness_requirement": "Single instance at decision point 2 only; must not be repeated as a restated example, follow-up probe answer, or outcome explanation elsewhere in the interview"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "mechanism": "Disproportionate weight given to one recent, vivid negative event (Dev's outage) relative to a longer positive track record and a comparably negative but less salient pattern from another engineer (Marcus's missed deadlines)",
        "affected_reasoning_operation": "Personnel-risk assessment feeding a task-assignment decision",
        "evidence_source": "Incident postmortem and eighteen-month performance history for Dev, contrasted with Marcus's deadline record",
        "distinctiveness_requirement": "Single instance at decision point 3 only; must not be repeated as a restated example, follow-up probe answer, or outcome explanation elsewhere in the interview"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ie_01",
        "bias": "Irrational Escalation",
        "strength": "subtle"
      },
      {
        "instance_id": "nb_01",
        "bias": "Negativity Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IS_Biased_2",
    "domain_id": "IS",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences were spread across distinct decision points (Irrational Escalation at decision point 2, Negativity Bias at decision point 3) chosen for mechanism fit and narrative realism within a single continuous incident; decision points 1 and 4 were kept clean to avoid unintended bias density and to preserve plausible non-bias explanations at every decision point.",
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
          "segment_type": "diagnostic_choice_and_rationale",
          "raw_interview_anchor": "I told the team to profile QuickCache specifically first, since it was the most likely suspect given the timing, and if that came back clean we'd widen the net.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The targeted profiling choice is a reasonable diagnostic narrowing based on deployment timing; no hidden bias instance is manifested."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "resource_allocation_choice_and_rationale",
          "raw_interview_anchor": "I committed another sprint to patching QuickCache. We'd put so much into that system—Priya and Dev both have deep expertise in it... Ripping it out after all that felt like it would waste the specialized knowledge we'd built up.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ie_01"
          ],
          "ground_truth_rationale": "The decision to continue patching is justified primarily by sunk engineering effort, specialized expertise, and reluctance to waste prior investment rather than by a forward-looking comparison with the mature alternative."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "personnel_assignment_choice_and_rationale",
          "raw_interview_anchor": "I pulled Dev off primary ownership and gave it to Marcus, with Dev supporting in a reduced capacity. The outage was still fresh... Marcus hadn't had an incident like that, so it felt like the safer bet.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "nb_01"
          ],
          "ground_truth_rationale": "A single vivid recent outage is given disproportionate weight over Dev's strong eighteen-month record and Marcus's more diffuse pattern of missed deadlines."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "status_communication_choice_and_rationale",
          "raw_interview_anchor": "I went with transparency—laid out what was fixed, what wasn't, and proposed a follow-up sprint with monitoring in place.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Transparent status reporting with mitigation and monitoring is the specified defensible, non-biased choice."
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
    "analysis_scope_note": "Analysis covers only affirmative, transcript-evidenced reasoning episodes. No retrieved corpus passages were supplied in this task, so bias labels and mechanisms rely on established cognitive-science knowledge with disclosure in each occurrence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue a course of action or investment based on the time, money, or effort already committed, even when current evidence favors a different course, rather than evaluating primarily prospective costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Commitment to another QuickCache patch rather than switching to a Redis-backed alternative",
      "decision_point_description": "After profiling identified QuickCache latency and suggested structural rework, the participant chose to invest another sprint in patching QuickCache instead of replacing it, citing sunk engineering effort and team expertise.",
      "affected_reasoning_operation": "Choice between continuing an in-house system and switching to a mature alternative under schedule pressure",
      "bias_specific_mechanism": "Escalation of commitment/sunk cost: the participant weighted prior engineering investments and the desire not to waste accumulated expertise more heavily than forward-looking profiling evidence that the invalidation architecture needed structural rethinking.",
      "manifestation_in_interview": "The participant explicitly stated that profiling data suggested the invalidation architecture needed rethinking, but that he nevertheless weighed the history and sunk engineering time heavily, and chose another patch partly because replacing QuickCache felt like wasting the specialized knowledge the team had built.",
      "effect_on_reasoning_or_decision": "It produced continuation of QuickCache for another sprint despite evidence favoring a more substantial change, leading to only about a fifteen percent improvement, continued team strain, and insufficient progress for the demo.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd put so much into that system—Priya and Dev both have deep expertise in it, and honestly, leadership had held it up before as an example of us building smart in-house tooling instead of just buying everything. Ripping it out after all that felt like it would waste the specialized knowledge we'd built up.",
          "evidence_explanation": "This directly shows the participant treating previously invested effort, expertise, and reputational validation as a reason to continue rather than assessing forward-looking costs and benefits."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly Priya's read on how close the fix was, plus the fact that we'd already sunk so much engineering time into getting QuickCache stable. The profiling data actually suggested the invalidation architecture itself needed rethinking, not just a tweak, but I weighed the history we had with the system pretty heavily.",
          "evidence_explanation": "This explicitly acknowledges that the participant gave heavy weight to sunk engineering time and system history even though current profiling evidence pointed toward structural rework."
        }
      ],
      "correction_or_counterevidence": "The participant did possess profiling data suggesting structural rework rather than a minor tweak, and later said he might have pushed for a parallel evaluation if he had seen that evidence clearly before committing. However, this did not alter the allocation at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in this task. The label and mechanism are assigned from established cognitive-science knowledge and the transcript evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "recency bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging likelihood or risk based on how easily instances come to mind, causing recent, vivid, or emotionally salient events to influence probability or risk estimates disproportionately.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Assignment of urgent QuickCache fix to Marcus instead of Dev under deadline",
      "decision_point_description": "With days remaining, the participant chose Marcus as primary owner despite Dev's deeper QuickCache knowledge, because Dev's recent production outage was salient; Marcus's slower deadline pattern lacked a similarly vivid recent episode.",
      "affected_reasoning_operation": "Risk assessment and assignment of critical engineering ownership under time pressure",
      "bias_specific_mechanism": "Availability heuristic: a recent, emotionally vivid production outage was easily recalled and therefore overweighted as evidence of future risk, while a less vivid but objective pattern of missed deadlines was underweighted.",
      "manifestation_in_interview": "The participant explicitly described the recent outage as the thing sitting in front of him when making the assignment decision, while Marcus's slower deadline record did not feel as urgent even though the participant said it was objectively relevant.",
      "effect_on_reasoning_or_decision": "It led to assigning a less experienced engineer to the urgent fix, producing a messier handoff and a longer fix than if Dev had led; the participant's forward-looking risk judgment was distorted by event salience rather than a balanced review of track records.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The outage was still fresh, and putting Dev front and center on another high-stakes fix right after that felt like more risk than I wanted heading into a leadership demo. Marcus hadn't had an incident like that, so it felt like the safer bet.",
          "evidence_explanation": "This shows the freshness and vividness of Dev's recent outage driving the participant's risk perception, rather than a systematic evaluation of Dev's overall performance and expertise."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mean, I knew his track record was good overall. But that outage was the thing sitting right in front of me when I had to make the call. Marcus's slower pattern didn't have a moment like that attached to it, so it didn't feel as urgent, even though objectively his deadline record isn't great either.",
          "evidence_explanation": "This directly contrasts an easily recalled salient incident with a more diagnostic but less vivid record, demonstrating availability as the operative mechanism."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged Dev's overall track record was good and that Marcus's deadline record was objectively problematic. He also later indicated that more temporal distance from the outage would likely have changed the assignment. These points do not undo the availability-driven assignment at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in this task. The label and mechanism are assigned from established cognitive-science knowledge and the transcript evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied; corpus evidence is empty and labels rest on general cognitive-science knowledge.",
    "The interview is a retrospective self-report, so the analysis is limited to the participant's account and exact transcript statements."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Biased_2_Sonnet_off",
  "interview_id": "IS_Biased_2",
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
