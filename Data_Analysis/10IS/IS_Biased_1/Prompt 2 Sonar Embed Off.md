You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Before we begin, do you consent to taking part in this interview? I’m interested in a specific work incident and how you made decisions as it unfolded, rather than in evaluating the outcome.

Participant: Yes, that’s fine.

Interviewer: Could you briefly describe your role and the incident you’ll be discussing?

Participant: I was the Product Manager for onboarding at CollabHub, a B2B collaboration platform. We had self-serve signups, plus sales-assisted accounts that often began with the same flow. The incident was a noticeable increase in abandonment during account setup, about five weeks before our Q3 board review. My responsibility was to identify a credible response quickly without derailing the sprint roadmap or putting enterprise customers at greater risk.

Interviewer: What first alerted you to it?

Participant: Our weekly onboarding funnel dashboard showed that drop-off at account setup had increased 32% over three weeks. That was unusual because the top of the funnel was stable. Traffic, acquisition channels, and SSO usage had not changed enough to explain it. At first, the dashboard only showed account setup as one broad stage, so I could see the deterioration but not exactly where people were leaving.

We had a board narrative built around improving activation rate, so the timing mattered. The VP of Product wanted an explanation, Sales was already hearing feature-parity questions from prospects, and Engineering had a fairly full sprint with enterprise bug fixes. I asked our data analyst to investigate the funnel instrumentation and asked a designer to pull heatmap analytics. I also did a quick scan of competitors because I wanted to know whether there had been a shift in the market.

Interviewer: What was the overall objective you were working toward?

Participant: In the immediate sense, reduce abandonment and protect activation rate. More broadly, I needed a plan that was credible to the board and did not consume so much sprint capacity that we created problems elsewhere. We had to decide whether this was a narrow usability or payment issue, or evidence that our whole onboarding approach was behind where the market was going.

Interviewer: Walk me through the sequence after you saw the dashboard.

Participant: The first few days were mostly about separating the signal from the dashboard limitation. Then we got better detail from the analyst. The sharpest abandonment seemed to happen just after the payment-detail field, especially for a newer subgroup of accounts. In parallel, the competitor scan showed that three platforms we regularly encountered in deals had released some form of guided onboarding flow. That became a larger discussion in the product group. We then selected an approach, made a staffing decision, and finally had to decide whether to launch before the board review with incomplete testing.

Interviewer: At the outset, what did you decide to investigate first?

Participant: I chose a rapid internal analytics review, supplemented by a light competitor scan, rather than immediately commissioning user interviews.

Interviewer: What information did you have at that time?

Participant: I had the 32% increase in the broad account-setup drop-off step, no fresh qualitative feedback, and a warning from the analyst that the payment sub-step had incomplete instrumentation. The UX research team could have recruited interviews, but they estimated two weeks before we would have useful sessions. We had only five weeks until the board review, and any changes would still need design, engineering, QA, and a release window.

Interviewer: What alternatives did you consider?

Participant: The main alternatives were to start with formal customer interviews, to do a deeper funnel and heatmap analysis first, or to rely mostly on market research and competitor teardowns. We could also have done all three, but that would have spread a small team thin and still might not have produced a decision quickly.

Interviewer: Why did you choose the analytics route?

Participant: We needed a directional answer within days, not weeks. Analytics could tell us whether the issue was broadly distributed or concentrated in a specific step. The heatmaps could show hesitation, repeated field edits, or attempts to leave the page. I did not treat the competitor scan as a diagnosis; at that point it was context. Deferring interviews was a trade-off. I documented that we were choosing speed over depth and asked Research to hold provisional time in case the data stayed unclear.

Interviewer: What did you learn after that decision?

Participant: The analyst narrowed the issue. Abandonment rose most clearly after payment details, not when users named the workspace, invited teammates, or configured SSO. The affected cohort was only about 140 users, though, and it was a new account type introduced the previous month. So it was suggestive, but not statistically stable. The heatmaps showed some repeated edits around payment fields, but because instrumentation was incomplete, we could not reliably distinguish validation failures from people simply deciding not to continue.

Interviewer: When did competitor activity begin to matter more?

Participant: Once I was preparing options for the VP of Product. The competitor review showed three named platforms had shipped guided setup experiences in roughly six weeks. I also follow a cross-company product Slack group, and several PMs were sharing launch screenshots and implementation notes for AI-guided onboarding. An industry newsletter was describing guided setup as something most leading SaaS onboarding flows were adopting.

Interviewer: What was the next decision you had to make?

Participant: Whether to build an AI-guided setup wizard, focus on the payment-detail issue, or run a small A/B test of both directions before committing.

Interviewer: Describe the evidence in front of you.

Participant: Internally, we had the payment-field signal, but it was from a small cohort. The data did not show that a guided wizard would solve that specific issue. Externally, we had a much more visible pattern: competitors were changing their onboarding experiences, our sales director was hearing questions about whether we had comparable guidance, and peer PMs were treating these flows as the new baseline.

Interviewer: How did you weigh those sources?

Participant: I put more weight on the external pattern than I normally would have. My thinking was that if several direct competitors had invested in the same interaction pattern so quickly, there was probably something we were missing about expectations in the category. In the Slack discussions, it felt like every product team I recognized was moving toward guided setup. That made the wizard feel less like an experimental bet and more like the direction the category had already chosen.

The payment data was still important, but I saw it as potentially a local symptom. With only 140 users in that cohort and incomplete funnel instrumentation, I was reluctant to build the entire response around it. I decided the AI-guided wizard was the better strategic move, and we would address the payment field within that broader redesign later.

Interviewer: Did you consider running a controlled test before committing?

Participant: Yes. The analyst suggested a lightweight A/B test: one version simplifying payment details and another adding limited guided setup. That would have been cleaner from an evidence perspective. I ruled it out because it would have taken design and engineering time without giving us a board-ready feature direction quickly. Also, I felt that waiting while the market moved would make us look late.

Interviewer: If you had not seen the competitor releases or the discussions among peer PMs, would you have chosen the same option?

Participant: I probably would have pushed harder for the payment-field experiment first. The external activity was a major reason I was comfortable making a larger commitment despite the uncertainty in our own data.

Interviewer: Once you chose the wizard, what staffing decision followed?

Participant: I had to decide whether to fully reassign two engineers from the enterprise bug-fix backlog for three sprints, split their time between the wizard and a narrow payment-field fix, or delay the wizard and prioritize the backlog.

Interviewer: What were the competing goals then?

Participant: The engineering lead estimated three sprints for a usable wizard, including integration with account configuration and SSO routing. The backlog contained unresolved enterprise defects, some affecting permissions and notification behavior. Sales wanted the wizard in active deal demonstrations, while Engineering was concerned that splitting the work would make both efforts slow and difficult to test.

Interviewer: What did you decide, and why?

Participant: I authorized the full reallocation to the wizard. That was not an easy choice, but partial staffing would have produced a thin version of the feature and still would not have given us enough capacity to resolve the payment issue properly. Delaying the wizard would have protected the backlog, but it also meant we would have little concrete progress to show at the board review. I accepted the bug-risk trade-off, with the engineering lead agreeing to triage only production-severity issues during the build.

Interviewer: What happened afterward?

Participant: Two enterprise tickets escalated during that period. Neither became a platform outage, but account teams had to manage customer concerns. The wizard build stayed on schedule. At the same time, a follow-up analytics review continued to show payment-field friction. We had not changed that code path, so the result was not surprising, but it made clear that the redesign did not remove the immediate signal.

Interviewer: What was the final decision before launch?

Participant: Whether to release the wizard to all new signups before the board review, limit it to a 10% canary release, or wait another week for more regression testing and improved payment instrumentation.

Interviewer: What did you know at that point?

Participant: QA had completed partial regression testing. The canary had low traffic, so activation-rate results were inconclusive. We knew payment-field abandonment had not moved. The board meeting was four days away, and the release was functioning in the tested paths, but there were still gaps in edge-case coverage.

Interviewer: Why launch to all new signups?

Participant: I made a time-bounded product and communication decision. A 10% canary would have been safer technically, but it would not produce enough usable operational evidence before the board meeting. Waiting another week would have improved testing, but it would also leave us presenting a plan rather than a shipped response. I consulted the engineering lead and QA manager; both were uncomfortable but agreed the remaining risks were manageable if we staffed monitoring and had a rollback path.

Interviewer: What were the consequences?

Participant: The post-launch activation rate did not show a statistically significant change from the prior month. Support tickets still mentioned difficulty at the payment step. We did not have a major regression, which was important, but the wizard was not the immediate solution to the funnel problem. We then prioritized a focused review of payment validation and instrumentation.

Interviewer: If you had had two more weeks before the board review, what would you have done differently?

Participant: I would have run the controlled comparison and recruited several users from the new account cohort. I would also have kept the wizard in a limited canary longer. That would have given us a better answer about whether payment friction, onboarding complexity, or both were affecting activation.

Interviewer: What information would have changed your earlier redesign decision?

Participant: A larger, stable cohort showing that payment details were clearly the dominant exit point would have changed it. I also would have wanted session recordings or interview evidence showing why users stopped there. If that evidence had been strong, I would have treated the payment fix as the immediate priority and positioned the wizard as a separate longer-term initiative.

Interviewer: And if the competitors had not introduced guided onboarding at that time?

Participant: I think I would have been more willing to make the smaller, targeted payment change first. The market context made the broader redesign feel urgent in a way that the internal data alone did not.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "IS_Biased_1",
    "domain_id": "IS",
    "domain": "Information Systems, human-computer interaction, and interaction design",
    "role": "Product Manager (Digital Platform)",
    "condition": "biased",
    "generation_specification": {
      "scenario_title_internal": "The Onboarding Wizard Decision at CollabHub",
      "scenario_summary_internal": "A PM at a mid-size B2B collaboration-software platform (CollabHub) investigates a 32% drop-off at the account-setup step of the signup funnel ahead of a Q3 board review. Across four chronological decision points, the PM diagnoses the problem, chooses a redesign approach, allocates scarce engineering resources, and makes a launch call under time pressure. At decision point 2, the PM adopts an 'AI-guided setup wizard' pattern primarily because several visible competitor platforms and peer PMs in an industry Slack group have rapidly adopted it, discounting internal cohort data pointing to a different friction source (a payment-field issue), consistent with herding.",
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
          "irrational"
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
            "An industry analyst newsletter and the PM's cross-company Slack group report that 'most top SaaS onboarding flows now use guided AI wizards'",
            "Internal sample size for the affected cohort is small (approximately 140 users) and not yet statistically stable"
          ],
          "new_information_after_decision": [
            "Engineering estimates the wizard will take three sprints to build",
            "A follow-up analytics review (after the decision) shows the payment-field friction persists independent of the wizard concept"
          ],
          "alternatives": [
            "Build the AI-guided setup wizard adopted by competitors",
            "Run a targeted fix on the payment-field step identified in internal cohort data",
            "Run a small controlled A/B test comparing a wizard concept against a payment-field fix before committing engineering resources"
          ],
          "intended_action": "PM commits to building the AI-guided wizard, citing rapid competitor and peer-community adoption as the primary justification, while treating the internal payment-field signal as secondary."
        },
        {
          "phase": 3,
          "decision_point": true,
          "facts_available_before_decision": [
            "Engineering lead confirms building the wizard requires reallocating two engineers from the bug-fix backlog for three sprints",
            "Backlog contains several unresolved defects reported by enterprise customers",
            "Sales director requests wizard prioritization to match competitor demos in active deals"
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
          "At what point did competitor activity enter your thinking?",
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
          "If the competitor activity hadn't been visible to you, would you have decided differently?"
        ],
        "closing_hypotheticals": [
          "If you had two more weeks before the board review, what would you have done differently?",
          "If the payment-field signal had come from a larger sample, would that have changed your decision at that stage?",
          "Looking back, what would you tell a peer PM facing a similar signal about a competitor trend?"
        ]
      },
      "occurrence_embedding_plan_internal": [
        {
          "instance_id": "herd_01",
          "bias": "Herding",
          "decision_point": 2,
          "mechanism": "PM selects the onboarding redesign approach primarily on the basis that multiple competitors and peer PMs have rapidly adopted the same pattern, treating adoption prevalence itself as the main evidentiary signal, and downweighting an available internal cohort signal that points to a different root cause.",
          "affected_reasoning_operation": "evidence weighting during redesign-approach selection",
          "evidence_available_at_time": [
            "Internal cohort data indicating payment-field friction",
            "Small, statistically unstable internal sample (~140 users)",
            "Three competitor platforms shipping an AI-guided wizard within six weeks",
            "Industry Slack group and analyst newsletter framing wizard adoption as near-universal among top SaaS platforms"
          ],
          "required_textual_manifestation": "The PM explicitly cites 'everyone else is doing this now' / peer and competitor adoption volume as the deciding factor for choosing the wizard, while acknowledging but setting aside the payment-field signal, without independently testing the wizard concept against the internal data before committing resources.",
          "plausible_nonbias_interpretation": "Could be read as a defensible strategic bet on feature parity for sales reasons, or as a rational response to a genuinely small and unreliable internal sample — the interview must include enough detail (e.g., PM's own words prioritizing adoption prevalence over the specific cohort signal) to distinguish it from this reasonable alternative.",
          "strength": "moderate",
          "do_not_make_explicit": [
            "herding",
            "bandwagon",
            "social proof",
            "conformity",
            "everyone is doing it therefore correct"
          ]
        }
      ],
      "control_specification": {
        "paired_scenario_id": null,
        "features_to_match": [],
        "features_to_remove_or_change": [],
        "ambiguity_boundary": "Not applicable; condition is 'biased' and no paired control scenario was supplied."
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
        "Exactly one Herding instance planned, assigned to decision point 2 only",
        "No bias vocabulary appears in probe_plan or timeline text",
        "Decision points 1, 3, and 4 contain no intentional bias instances",
        "Internal cohort signal (payment-field friction) is present before and remains unresolved after the biased decision, enabling a non-bias interpretation to also be plausible",
        "Word count target 1,350 (range 1,215-1,485) achievable given 4 decision points with moderate probe depth and one embedded instance",
        "Technical-terms-to-avoid list checked against all planned decision-point language"
      ]
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "biased",
      "exact_occurrence_manifest": [
        {
          "bias": "Herding",
          "occurrences": 1,
          "mechanism_constraint": null
        }
      ],
      "target_bias_names": [
        "Herding"
      ],
      "requested_occurrence_count_for_each_bias": [
        {
          "bias": "Herding",
          "requested_occurrences": 1
        }
      ],
      "planned_instance_ids": [
        {
          "instance_id": "herd_01",
          "bias": "Herding"
        }
      ],
      "intended_decision_points": [
        {
          "instance_id": "herd_01",
          "bias": "Herding",
          "decision_point": 2
        }
      ],
      "intended_mechanisms": [
        {
          "instance_id": "herd_01",
          "bias": "Herding",
          "mechanism": "PM chooses the redesign approach mainly because of rapid, visible adoption of the same pattern by competitors and peer PMs, using adoption prevalence as the primary decision criterion instead of independently weighting the internal cohort evidence pointing to a distinct root cause.",
          "affected_reasoning_operation": "evidence weighting during redesign-approach selection",
          "evidence_source": "competitor teardown reports and industry Slack/analyst newsletter signaling widespread wizard adoption, contrasted with internal small-sample cohort data on payment-field friction",
          "distinctiveness_requirement": "Must be the only instance in the interview where adoption prevalence by external peers/competitors is used as the primary justification for a decision; no other decision point may reuse this justification pattern."
        }
      ],
      "intended_strength": [
        {
          "instance_id": "herd_01",
          "bias": "Herding",
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
      "scenario_id": "IS_Biased_1",
      "domain_id": "IS",
      "total_requested_occurrences": 1,
      "total_planned_occurrences": 1,
      "allocation_rule_used": "Single requested occurrence assigned to decision point 2 based on mechanism fit: a build-vs-fix redesign decision with salient, time-pressured market comparables is the most narratively realistic setting for herding in a PM context. Rules on splitting occurrences across decision points and using distinct evidence sources for co-located occurrences were not triggered because only one occurrence was requested.",
      "control_zero_bias_requirement": false,
      "variables_to_hold_constant": [],
      "generation_warnings": [
        "Input specified counterfactual_variable as 'AUTOSELECT', but condition is 'biased' (not 'counterfactual') and no paired/base scenario was supplied (paired scenario ID = NONE). No counterfactual variable was selected or embedded; counterfactual_specification and counterfactual_variable fields are set to null to avoid fabricating an unrequested experimental factor."
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
        "segment_type": "objective_and_role_rationale",
        "raw_interview_anchor": "I was the Product Manager for onboarding at CollabHub... My responsibility was to identify a credible response quickly without derailing the sprint roadmap or putting enterprise customers at greater risk.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states the operational objective and constraints without a manifested hidden bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_investigation_action",
        "raw_interview_anchor": "At first, the dashboard only showed account setup as one broad stage... I asked our data analyst to investigate the funnel instrumentation and asked a designer to pull heatmap analytics.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The investigation actions are a reasonable response to an underspecified dashboard signal."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "objective_tradeoff",
        "raw_interview_anchor": "In the immediate sense, reduce abandonment and protect activation rate... We had to decide whether this was a narrow usability or payment issue, or evidence that our whole onboarding approach was behind where the market was going.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This frames competing product objectives and hypotheses but does not manifest the hidden instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "investigation_choice",
        "raw_interview_anchor": "I chose a rapid internal analytics review, supplemented by a light competitor scan, rather than immediately commissioning user interviews.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is decision point 1; the hidden manifest assigns no bias there."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_and_time_constraint",
        "raw_interview_anchor": "I had the 32% increase in the broad account-setup drop-off step, no fresh qualitative feedback, and a warning from the analyst that the payment sub-step had incomplete instrumentation... We had only five weeks until the board review.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "These are the evidence and timing constraints available before decision point 1."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "investigation_rationale",
        "raw_interview_anchor": "We needed a directional answer within days, not weeks... I documented that we were choosing speed over depth and asked Research to hold provisional time in case the data stayed unclear.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly documents a speed-versus-depth tradeoff and preserves a fallback research option."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "evidence_interpretation",
        "raw_interview_anchor": "The analyst narrowed the issue. Abandonment rose most clearly after payment details... So it was suggestive, but not statistically stable.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant appropriately characterizes a small, incompletely instrumented cohort signal as suggestive but unstable."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "market_signal_assessment",
        "raw_interview_anchor": "Once I was preparing options for the VP of Product. The competitor review showed three named platforms had shipped guided setup experiences... An industry newsletter was describing guided setup as something most leading SaaS onboarding flows were adopting.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This records external context that became relevant; the hidden occurrence is mapped to the subsequent weighting-and-choice rationale."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "redesign_decision_framing",
        "raw_interview_anchor": "Whether to build an AI-guided setup wizard, focus on the payment-detail issue, or run a small A/B test of both directions before committing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This states the alternatives at decision point 2 without yet expressing the hidden mechanism."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "redesign_evidence_inventory",
        "raw_interview_anchor": "Internally, we had the payment-field signal, but it was from a small cohort... Externally, we had a much more visible pattern: competitors were changing their onboarding experiences...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant inventories competing evidence sources before explaining how they were weighted."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "biased_evidence_weighting_and_choice",
        "raw_interview_anchor": "I put more weight on the external pattern than I normally would have... I decided the AI-guided wizard was the better strategic move, and we would address the payment field within that broader redesign later.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "herd_01"
        ],
        "ground_truth_rationale": "This is the sole hidden instance: adoption prevalence among competitors and peer PMs is used as the primary basis for choosing the wizard while the internal payment signal is downweighted."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "test_rejection_rationale",
        "raw_interview_anchor": "I ruled it out because it would have taken design and engineering time without giving us a board-ready feature direction quickly. Also, I felt that waiting while the market moved would make us look late.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The manifest contains no additional occurrence at the A/B-test decision; the stated deadline and communication rationale remain a plausible non-bias explanation."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "counterfactual_reasoning",
        "raw_interview_anchor": "I probably would have pushed harder for the payment-field experiment first. The external activity was a major reason I was comfortable making a larger commitment despite the uncertainty in our own data.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is corroborating counterfactual evidence for the mapped instance, not a separate hidden occurrence."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "resource_allocation_choice",
        "raw_interview_anchor": "I had to decide whether to fully reassign two engineers from the enterprise bug-fix backlog for three sprints, split their time... or delay the wizard and prioritize the backlog.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is decision point 3, which the hidden specification identifies as non-biased."
      },
      {
        "segment_id": "seg_015",
        "speaker": "Participant",
        "segment_type": "resource_allocation_rationale",
        "raw_interview_anchor": "I authorized the full reallocation to the wizard... I accepted the bug-risk trade-off, with the engineering lead agreeing to triage only production-severity issues during the build.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The staffing decision is explained through capacity, feature completeness, board visibility, and an explicit risk mitigation."
      },
      {
        "segment_id": "seg_016",
        "speaker": "Participant",
        "segment_type": "post_decision_evidence_review",
        "raw_interview_anchor": "Two enterprise tickets escalated during that period... The wizard build stayed on schedule. At the same time, a follow-up analytics review continued to show payment-field friction.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This reports consequences and persistent evidence without adding a hidden bias instance."
      },
      {
        "segment_id": "seg_017",
        "speaker": "Participant",
        "segment_type": "launch_choice_and_evidence",
        "raw_interview_anchor": "Whether to release the wizard to all new signups before the board review, limit it to a 10% canary release, or wait another week for more regression testing and improved payment instrumentation... The board meeting was four days away.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is decision point 4 framing under technical and board-review constraints."
      },
      {
        "segment_id": "seg_018",
        "speaker": "Participant",
        "segment_type": "launch_rationale",
        "raw_interview_anchor": "A 10% canary would have been safer technically, but it would not produce enough usable operational evidence before the board meeting. Waiting another week would have improved testing, but it would also leave us presenting a plan rather than a shipped response.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The hidden specification assigns no bias to decision point 4; the candidate escalation interpretation is not affirmatively supported."
      },
      {
        "segment_id": "seg_019",
        "speaker": "Participant",
        "segment_type": "outcome_assessment",
        "raw_interview_anchor": "The post-launch activation rate did not show a statistically significant change from the prior month... We then prioritized a focused review of payment validation and instrumentation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant assesses the launch outcome and redirects work toward the unresolved payment issue."
      },
      {
        "segment_id": "seg_020",
        "speaker": "Participant",
        "segment_type": "retrospective_alternative_plan",
        "raw_interview_anchor": "I would have run the controlled comparison and recruited several users from the new account cohort. I would also have kept the wizard in a limited canary longer.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective improvement plan and not a new manifested occurrence."
      },
      {
        "segment_id": "seg_021",
        "speaker": "Participant",
        "segment_type": "decision_changing_evidence",
        "raw_interview_anchor": "A larger, stable cohort showing that payment details were clearly the dominant exit point would have changed it... If that evidence had been strong, I would have treated the payment fix as the immediate priority.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant identifies evidence that would have changed the redesign decision."
      },
      {
        "segment_id": "seg_022",
        "speaker": "Participant",
        "segment_type": "market_counterfactual",
        "raw_interview_anchor": "If the competitors had not introduced guided onboarding at that time... I think I would have been more willing to make the smaller, targeted payment change first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a counterfactual explanation of the earlier choice, not a second hidden instance."
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
      "analysis_scope_note": "Analyzed the participant's reasoning during the onboarding abandonment incident. No scientific-paper corpus passages were provided in the prompt; bias labels and mechanisms therefore rely on established cognitive-science knowledge."
    },
    "identified_bias_summary": [
      {
        "bias_label": "Bandwagon effect",
        "identified_occurrence_count": 1
      }
    ],
    "identified_occurrences": [
      {
        "occurrence_id": "obs_001",
        "classification_status": "identified",
        "confidence": "high",
        "bias_label": "Bandwagon effect",
        "alternative_labels": ["Social proof", "Herd behavior", "Information cascade"],
        "taxonomy_status": "established_label",
        "bias_definition": "The tendency to adopt a belief, course of action, or evaluation because many others are perceived to be adopting it, using social prevalence or visible adoption as a heuristic for correctness or urgency.",
        "attributed_to_speaker": "Participant",
        "evidence_speaker": "Participant",
        "decision_episode_label": "Choice of AI-guided setup wizard versus targeted payment-field fix or A/B test",
        "decision_point_description": "Deciding whether to build an AI-guided setup wizard, focus on the payment-detail issue, or run a small A/B test of both directions before committing.",
        "affected_reasoning_operation": "Weighing internal versus external evidence and selecting a product direction under uncertainty",
        "bias_specific_mechanism": "The participant inferred that guided onboarding was the correct or category-expected direction because several direct competitors and peer product teams were visibly moving toward it; this social-prevalence signal was weighted more heavily than weak internal evidence against the specific solution.",
        "manifestation_in_interview": "The participant explicitly says they gave more weight to the external pattern than normal and that visible competitor and peer adoption made the wizard feel like the direction the category had already chosen.",
        "effect_on_reasoning_or_decision": "The participant rejected the lower-risk A/B test and committed to the broader AI-guided wizard, even though internal data did not show that a guided wizard addressed the observed payment-step abandonment.",
        "interview_evidence": [
          {
            "speaker": "Participant",
            "verbatim_quote": "I put more weight on the external pattern than I normally would have. My thinking was that if several direct competitors had invested in the same interaction pattern so quickly, there was probably something we were missing about expectations in the category.",
            "evidence_explanation": "This directly states the social-proof mechanism: competitor adoption was treated as evidence of a category expectation, overriding the participant's usual weighing of external pattern evidence."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "In the Slack discussions, it felt like every product team I recognized was moving toward guided setup. That made the wizard feel less like an experimental bet and more like the direction the category had already chosen.",
            "evidence_explanation": "This shows visible peer adoption shaping the inference that the wizard was the safe or inevitable category direction rather than an uncertain experiment."
          },
          {
            "speaker": "Participant",
            "verbatim_quote": "I probably would have pushed harder for the payment-field experiment first. The external activity was a major reason I was comfortable making a larger commitment despite the uncertainty in our own data.",
            "evidence_explanation": "The participant's counterfactual confirms that the external social signal, not internal data, was the decisive reason for the larger commitment to the wizard."
          }
        ],
        "correction_or_counterevidence": "The participant did not ignore internal analytics entirely; the payment-cohort evidence was small and instrumentation was incomplete, so some discounting of that evidence was reasonable. The participant also documented the trade-off and planned to address payment later within the broader redesign.",
        "retrieved_corpus_support_available": false,
        "corpus_support_note": "Retrieved scientific-paper support was not available in the provided context. The bandwagon-effect label is applied from established cognitive-science knowledge.",
        "corpus_evidence": []
      }
    ],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Escalation of commitment",
        "alternative_labels": ["Sunk cost fallacy", "Commitment bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Final decision to launch the wizard to all new signups before board review despite incomplete testing and inconclusive canary",
        "supporting_interview_quote": "A 10% canary would have been safer technically, but it would not produce enough usable operational evidence before the board meeting. Waiting another week would have improved testing, but it would also leave us presenting a plan rather than a shipped response.",
        "plausible_mechanism": "After investing substantial resources and making a public commitment to the wizard, the participant may have continued toward full launch partly to justify the prior commitment rather than choosing the more cautious canary or delay options.",
        "why_not_identified": "The stated rationale is primarily time pressure and board communication, and the interview does not contain explicit sunk-cost reasoning such as 'we had already invested too much to stop now.' The safer inference is that this was a risky trade-off under organizational and deadline constraints rather than a clearly evinced biased escalation mechanism."
      }
    ],
    "no_supported_biases_found": false,
    "limitations": [
      "No retrieved scientific-paper corpus was provided in the prompt; bias labels rely on established cognitive-science knowledge rather than corpus support.",
      "The interview is a retrospective self-report, so the reasoning described may be reconstructed or self-presented after the outcome.",
      "Time pressure, board expectations, and organizational incentives are present in the decision context and can make it harder to distinguish bias from deliberate risk management or rational trade-offs."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Biased_1_Sonar_off",
  "interview_id": "IS_Biased_1",
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
