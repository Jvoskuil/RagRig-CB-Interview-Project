You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Before we begin, do you consent to taking part in this interview? I’m interested in a specific work incident and how you made decisions as it unfolded, rather than in evaluating the outcome.

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

Participant: I think I would have been more willing to make the smaller, targeted payment change first. The market context made the broader redesign feel urgent in a way that the internal data alone did not.}}

Hidden generation specification:
{{"hidden_validation_specification": {
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
  }}}

The hidden specification may include:
- condition;
- exact occurrence manifest;
- target bias names;
- requested occurrence count for each bias;
- planned instance IDs;
- intended decision points;
- intended mechanisms;
- intended strength;
- paired scenario ID;
- counterfactual variable.

Do not treat the hidden specification as evidence that a bias exists. It is a test plan only. The interview text is the evidence. If the specification and interview conflict, report the conflict.

CORE OCCURRENCE DEFINITIONS

A supported occurrence requires all of the following:
1. A distinct decision, inference, evidence-selection act, memory retrieval, prediction, causal attribution, or response to a probe.
2. Evidence showing how the participant processed, weighted, ignored, recalled, interpreted, or updated information.
3. A mechanism consistent with the named bias.
4. Enough context to distinguish the mechanism from a justified domain judgment or an ordinary mistake.

A single occurrence may span several adjacent sentences or one answer turn. Do not count repeated wording about the same reasoning episode as multiple occurrences. Count two occurrences separately only when they have distinct evidence traces, decision moments, evidence sources, or reasoning operations.

VALIDATION TASKS

1. Identify the domain, participant role, operational objective, and incident type.
2. Reconstruct the chronology and identify the decision points. Report whether exactly four decision points are present.
3. For every target bias in the hidden occurrence manifest, independently assess each requested occurrence.
4. Identify additional candidate biases not present in the target manifest.
5. Identify apparent bias cues that should not be labeled as bias.
6. Audit causal claims and counterfactual logic.
7. Evaluate interview quality and control fidelity.
8. Produce precise revision guidance when the interview does not satisfy its occurrence requirements.

FOR EACH REQUESTED OCCURRENCE, CLASSIFY IT AS ONE OF:

- supported: a distinct, textually supported instance is present;
- weak: a possible instance is present, but evidence or mechanism is insufficient;
- absent: no defensible instance is present;
- merged: the intended instance appears to be indistinguishable from another intended occurrence of the
  same bias or from another bias;
- accidental: an unintended instance appears outside the planned occurrence map;
- misclassified: the text supports a different bias or a non-bias explanation instead.

REVISION PRINCIPLES

If a requested occurrence is absent, weak, merged, or misclassified:
- Do not recommend simply repeating the bias label.
- Do not recommend adding an obvious textbook explanation.
- Specify the minimum local narrative or dialogue change needed to make that occurrence independently identifiable.
- Preserve the occupational setting, participant role, chronology, vocabulary, approximate length, and other intended bias occurrences.
- Do not create a new occurrence elsewhere merely to compensate.
- Do not strengthen every occurrence. Revise only the affected occurrence unless the evidence shows a broader structural problem.
- If strengthening the missing occurrence would make the interview too obvious, recommend a subtle evidence change rather than explicit labeling.
- If the requested occurrence is not plausible in the scenario, recommend changing the scenario or the target occurrence manifest rather than forcing implausible behavior.
- For controls, never recommend adding a target bias. If a control contains a defensible bias, recommend neutralizing or replacing the relevant reasoning episode.
- For a counterfactual, preserve the original and changed causal variables and do not introduce a second causal change while repairing bias evidence.

REVISION TYPES

Use one or more of these revision types:
- `none`: occurrence is adequately supported;
- `local_evidence_addition`: add or alter one cue, evidence source, or participant response;
- `local_reasoning_revision`: revise how the participant interprets or weighs evidence;
- `probe_revision`: change an interviewer question or hypothetical so the existing reasoning becomes independently observable;
- `decision_point_revision`: revise one decision point while preserving the rest;
- `remove_accidental_occurrence`: neutralize an unintended additional manifestation;
- `separate_merged_occurrences`: make two intended episodes distinct;
- `reclassify_bias`: change the target label or mechanism because the current label is not defensible;
- `scenario_revision`: revise the occupational situation because the requested occurrence is implausible.

REVISION SPECIFICITY

Each revision recommendation must include:
- the affected instance ID or `additional_candidate`;
- decision point and approximate turn or paragraph location;
- current status;
- evidence currently present, or `none`;
- precise defect;
- recommended revision type;
- minimal change instruction;
- what must remain unchanged;
- a warning against creating additional unintended occurrences;
- expected post-revision status.

Do not rewrite the complete interview. Provide revision instructions only. The generation system will apply
the instructions in a separate revision step.

OUTPUT

Return valid JSON only:
{
  "validator_version": "2.0",
  "interview_id": "...",
  "condition": "biased|vocabulary_control|ambiguous_control|counterfactual|unknown",
  "domain_assessment": {
    "domain": "...",
    "role": "...",
    "objective": "...",
    "incident_type": "...",
    "confidence": 0
  },
  "structure_audit": {
    "estimated_word_count": 0,
    "within_target_range": true,
    "decision_point_count": 0,
    "decision_points": [
      {
        "id": 1,
        "summary": "...",
        "evidence_before": [],
        "evidence_after": [],
        "goals_constraints": [],
        "alternatives": [],
        "decision_basis": "...",
        "time_pressure": "...",
        "uncertainty": "..."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "...",
      "bias": "...",
      "requested_occurrences_for_bias": 0,
      "status": "supported|weak|absent|merged|accidental|misclassified",
      "decision_point": 1,
      "supporting_quote": "...",
      "evidence_location": "...",
      "mechanism": "...",
      "strength": "absent|weak|moderate|strong",
      "confidence": 0,
      "plausible_nonbias_explanation": "...",
      "additional_evidence_needed": "...",
      "revision_needed": true,
      "revision": {
        "revision_type": "none|local_evidence_addition|local_reasoning_revision|probe_revision|decision_point_revision|remove_accidental_occurrence|separate_merged_occurrences|reclassify_bias|scenario_revision",
        "location": "...",
        "current_defect": "...",
        "minimal_change_instruction": "...",
        "preserve": [],
        "avoid_creating": [],
        "expected_post_revision_status": "supported|weak|absent|merged|accidental|misclassified"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "...",
      "requested_count": 0,
      "supported_count": 0,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "...",
      "decision_point": 1,
      "supporting_quote": "...",
      "mechanism": "...",
      "confidence": 0,
      "status": "candidate|supported|weak|rejected",
      "plausible_nonbias_explanation": "...",
      "revision_recommendation": "none|remove_or_neutralize|consider_adding_to_manifest"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "...",
      "location": "...",
      "why_not_bias": "..."
    }
  ],
  "causal_audit": {
    "causal_claims": [],
    "correlation_causation_risks": [],
    "counterfactual_present": false,
    "changed_variable": "...",
    "held_constant": [],
    "causal_coherence": "not_applicable|weak|moderate|strong",
    "explanation": "..."
  },
  "quality_scores": {
    "occupational_realism": 0,
    "cta_fidelity": 0,
    "bias_separability": 0,
    "bias_subtlety": 0,
    "control_fidelity": 0,
    "counterfactual_fidelity": 0,
    "narrative_coherence": 0,
    "naturalness": 0,
    "hidden_label_integrity": 0,
    "overall_quality": 0
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 0,
    "requested_occurrence_total": 0,
    "missing_occurrence_total": 0,
    "accidental_occurrence_total": 0,
    "priority": "none|low|medium|high|reject",
    "recommended_action": "accept|revise|regenerate|reject",
    "global_revision_constraints": [],
    "revision_order": []
  },
  "failure_flags": []
}

COUNTING RULES FOR THE SUMMARY
- `supported_occurrence_total` counts only occurrences with status `supported`.
- `missing_occurrence_total` counts `weak`, `absent`, `merged`, and `misclassified` requested occurrences.
- `accidental_occurrence_total` counts unintended instances that should be removed or separately labeled.
- Set `recommended_action` to `accept` only when all requested occurrences are supported, no unacceptable accidental occurrences exist, and quality is adequate.
- Set it to `revise` when local changes can repair the interview without changing the scenario.
- Set it to `regenerate` when the scenario, decision structure, or several occurrences are fundamentally unsuitable.
- Set it to `reject` for severe incoherence, contaminated controls, or unrepairable causal confounding.

Return JSON only. Do not return a revised interview.
