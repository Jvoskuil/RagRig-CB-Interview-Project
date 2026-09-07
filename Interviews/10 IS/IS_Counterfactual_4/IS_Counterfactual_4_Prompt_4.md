You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for sitting down with me. Quick reminder — this is a cognitive task analysis interview, so I'm interested in how you reasoned through things, not in grading the outcome. You can decline any question. Okay to start?

Participant: Sure, sounds good.

Interviewer: Can you give me your role and a general sense of the project?

Participant: I'm a UX designer on the product team at a B2B analytics company. Last year I led a redesign of our onboarding wizard, aiming to cut first-week drop-off. We had a twelve-week window that lined up with our quarterly product review — nothing contractual riding on it, just the usual expectation that we'd show some lift in activation rate.

Interviewer: Twelve weeks is a decent runway. What made this project stand out otherwise?

Participant: Mostly the scope — three flows needed real research, we needed outside build help, and there was a personalization system already running in the background that we wanted to lean on more.

Interviewer: Walk me through how it played out from the start.

Participant: Sure. Early on, three research vendor proposals came in. One was a cheap self-serve platform — six thousand dollars, five sessions, no synthesis, just raw recordings. Then two full-service options: twenty-one thousand for ten sessions with a written synthesis, and twenty-three thousand for twelve sessions plus dashboard integration and two follow-up rounds. I had plenty of time to sit with these, and I ended up going with the twenty-three thousand option.

Interviewer: What drove that?

Participant: When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it.

Interviewer: Did you weigh the cheaper self-serve option against your actual scope — you only needed three flows validated?

Participant: I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.

Interviewer: What came of that vendor choice?

Participant: The findings were fine, though two of the twelve sessions turned out to duplicate internal data we already had. And the dashboard piece only half worked when it was delivered — I ended up patching a lot of it myself.

Interviewer: Next stage?

Participant: Hiring a contractor for the micro-interactions — transitions, progress indicators. Two candidates: one had flagship work at a well-known unicorn startup, gorgeous portfolio, but not much documented process. The other had a plainer portfolio but included actual test scripts, metrics, iteration logs.

Interviewer: How did you choose, given you had time for a trial task if you wanted one?

Participant: I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too. I did consider running a paid trial with both — we had the weeks for it — but it felt like an unnecessary step given his track record.

Interviewer: Did you check the documentation and communication side directly?

Participant: Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in.

Interviewer: What happened with his deliverables?

Participant: Beautiful interactions, but he skipped documenting the reasoning for two key transitions, and when the Head of Design asked for the testing basis later, there wasn't much to show her.

Interviewer: Let's talk about the personalization engine.

Participant: We had a small test running — about a hundred forty users — on the rules engine, and I'd manually tuned two onboarding rule weights that same week. Right after, the activation number ticked up on the dashboard.

Interviewer: What did you take from that?

Participant: That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it.

Interviewer: Was there anything complicating that read?

Participant: She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.

Interviewer: What happened afterward?

Participant: The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed.

Interviewer: Last stage — the legacy component.

Participant: We'd put three sprints into customizing our old step-wizard component for the new flow. Then engineering flagged an accessibility defect and a rendering issue, and said a newer modular framework would fix both in about a sprint. We still had roughly six weeks left, so a one-sprint migration wouldn't have threatened the review date at all.

Interviewer: What did you decide?

Participant: I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare.

Interviewer: Setting the prior sprints aside, how did the one-sprint estimate compare to continuing, on its own terms?

Participant: Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.

Interviewer: What happened with the component?

Participant: The accessibility issue came back up during QA before the review, and by then migrating would have cost more than the original estimate, since we'd layered on even more customization by that point.

Interviewer: If Vendor B had been priced the same as Vendor C, would you have decided differently?

Participant: Possibly — I might've actually gone back and checked whether we needed the top-tier package at all.

Interviewer: If the second candidate's portfolio had come from a more recognizable company?

Participant: Probably would have hired her instead. That recognition factor carried more weight than it should have.

Interviewer: If the significance threshold had been strictly enforced before you could act?

Participant: I'd have waited — we had the schedule for it, I just didn't want to lose momentum.

Interviewer: And if none of those three sprints had already gone into the legacy component?

Participant: No question, I'd have migrated right away given the defects.

Interviewer: Last one — if this had been the original six-week sprint with the hard renewal deadline instead, do you think any of this would have gone differently?

Participant: Maybe the vendor and hiring calls would've felt more forced. But honestly, looking back, I'm not sure the extra time changed as much as it should have — I still landed in mostly the same places.

Interviewer: That's really helpful context. Thank you for walking through it so openly.

Participant: No problem — easier to spot in hindsight than it was in the moment.
}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Decoy effect",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Halo effect",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Sunk Cost Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Decoy effect",
      "Halo effect",
      "Illusion of control",
      "Sunk Cost Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Decoy effect",
        "requested_occurrences": 1
      },
      {
        "bias": "Halo effect",
        "requested_occurrences": 1
      },
      {
        "bias": "Illusion of control",
        "requested_occurrences": 1
      },
      {
        "bias": "Sunk Cost Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect"
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect"
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control"
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect",
        "decision_point": 1
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "decision_point": 2
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control",
        "decision_point": 3
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect",
        "mechanism": "Selection of the target vendor option is driven by favorable contrast against a similarly priced but inferior intermediate option, rather than independent assessment of the cheapest sufficient option, even absent acute time pressure.",
        "affected_reasoning_operation": "Comparative evaluation of vendor proposals under budget constraint",
        "evidence_source": "Vendor price/feature comparison table; project scope documentation; available schedule slack",
        "distinctiveness_requirement": "Must involve a three-option price/value contrast structure unique to this decision point, and must not be explained away by deadline urgency since urgency is absent in this variant."
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "mechanism": "A single salient positive attribute (portfolio brand prestige) is used to infer unrelated positive qualities (documentation rigor, communication skill) without direct supporting evidence, even though a verifying trial task was schedule-feasible.",
        "affected_reasoning_operation": "Multi-dimensional competency assessment based on one visible cue",
        "evidence_source": "Candidate portfolios; task requirement specification; available trial-task option",
        "distinctiveness_requirement": "Must involve generalization from one attribute to unrelated, unverified attributes, and must not be explained away by lack of time to run a trial task since time was available."
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control",
        "mechanism": "Overattribution of an observed metric change to the designer's own specific manual action, despite acknowledged insufficient statistical power and unresolved confounding factors, even though waiting for more data was schedule-feasible.",
        "affected_reasoning_operation": "Causal attribution under uncertainty and low sample size",
        "evidence_source": "A/B dashboard trend data; Analytics Lead's sample-size flag; concurrent marketing-send confound; available schedule slack",
        "distinctiveness_requirement": "Must involve explicit disregard of a flagged statistical limitation in favor of self-attributed causal influence, and must not be explained away by deadline-driven necessity to act quickly since none exists in this variant."
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias",
        "mechanism": "Continuation of a design approach is justified primarily by the magnitude of prior invested effort rather than a forward-looking comparison of remaining costs and benefits, even though remaining schedule slack could absorb the migration cost.",
        "affected_reasoning_operation": "Forward-looking continuation-versus-abandonment cost-benefit judgment",
        "evidence_source": "Sprint investment history; engineering migration-cost and defect-resolution estimate; remaining schedule slack",
        "distinctiveness_requirement": "Must explicitly cite prior invested effort as the stated justification for continuation despite forward-looking evidence favoring the alternative, and must not be explained away by deadline risk since schedule slack is available in this variant."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Decoy effect",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_02",
        "bias": "Halo effect",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_03",
        "bias": "Illusion of control",
        "strength": "subtle"
      },
      {
        "instance_id": "cb_04",
        "bias": "Sunk Cost Bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": "IS_Biased_4",
    "counterfactual_variable": {
      "name": "Sprint duration and deadline urgency structure",
      "original_state": "Six-week sprint window fixed by a hard external client renewal deadline",
      "changed_state": "Twelve-week sprint window aligned with a routine quarterly product review, with no external contractual deadline",
      "variables_to_hold_constant": [
        "Vendor proposal contents, pricing, and feature sets",
        "Candidate portfolios and documented capabilities",
        "Personalization rules engine test data, sample size, and Analytics Lead's flags",
        "Legacy component investment history and engineering migration estimate",
        "Budget ceiling for research and contractor work",
        "Engineering capacity (1.5 FTE)",
        "Design-system governance expectations",
        "Set of stakeholders and their goals",
        "All four decision points and their alternatives"
      ]
    },
    "scenario_id": "IS_Counterfactual_4",
    "domain_id": "IS",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias, each assigned to the same decision point as the paired base scenario IS_Biased_4 (Decoy effect -> vendor procurement comparison; Halo effect -> contractor competency inference; Illusion of control -> causal attribution of an ambiguous metric trend; Sunk Cost Bias -> continuation-vs-migration judgment), preserved unchanged across the counterfactual to isolate the effect of the deadline-urgency variable.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vendor proposal contents, pricing, and feature sets",
      "Candidate portfolios and documented capabilities",
      "Personalization rules engine test data, sample size, and Analytics Lead's flags",
      "Legacy component investment history and engineering migration estimate",
      "Budget ceiling for research and contractor work",
      "Engineering capacity (1.5 FTE)",
      "Design-system governance expectations",
      "Set of stakeholders and their goals",
      "All four decision points and their alternatives"
    ],
    "generation_warnings": []
  }}}
- Validation report: {{VALIDATION_REPORT}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
