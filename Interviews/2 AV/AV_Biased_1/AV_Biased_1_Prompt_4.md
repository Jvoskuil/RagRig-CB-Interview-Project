You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for an internal reliability-process review, not a safety investigation into you personally — we're trying to understand how these calls actually get made in practice. That okay with you?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me your role and how this particular case landed on your desk?

Participant: Sure. I'm a reliability engineer in Maintenance Control. Part of my job is watching for repetitive write-ups across the fleet and deciding when something crosses from "normal noise" into something that needs a formal corrective action. This one came up because tail 738 logged a third APU bleed air valve write-up inside 45 flight days. Two earlier ones had been closed out as operational check normal, no parts changed, which is pretty typical — a lot of these clear on the bench.

Interviewer: Walk me through the incident from the beginning, in your own words.

Participant: So the third write-up on 738 is what actually got my attention, because three in that short a window is unusual even though our fleet-wide removal rate for that valve was still sitting inside the OEM's published MTBUR. Nothing screamed "fleet problem" yet — it looked like it could just be a stubborn individual aircraft. I opened a focused review on that tail rather than calling it a fleet issue outright, and I put a flag on it so I'd get pinged if anything similar showed up elsewhere. Two days later it did — tail 712 logged a lower-severity version of basically the same complaint. That's when line maintenance told me the valve is genuinely hard to bench-test, which raised the possibility we had an intermittent fault that ground checks weren't catching. At that point I pulled the two tails' component histories together and found they shared the same valve batch lot number. That felt like a real thread to pull.

Interviewer: What did you do with that lot-number connection?

Participant: Company policy is we don't like repeated MEL carryover on the same defect — dispatching with the APU inoperative under MEL is allowed, but doing it leg after leg on the same fault is a flag in itself. Neither aircraft had had an actual in-flight consequence; both faults were caught on the ground. So grounding both outright felt like more than the evidence supported at that point. I put an interim restriction on — one leg of MEL carryover maximum, then it has to be addressed — on both tails, and opened a formal root-cause investigation tied to that lot number.

Interviewer: What came back from that investigation?

Participant: The vendor quality engineer confirmed that lot had a documented seal-material change about six months earlier. That's a real, traceable cause — not a guess. And our in-house teardown of the valve we'd pulled off 738 showed seal degradation that was consistent with exactly that material change. So by that point I had two independent lines — vendor documentation and physical teardown — pointing at the same thing.

Interviewer: Let's slow down on that moment, because I want to understand what happened next. What were you weighing?

Participant: Right, so this is the part before I finalized anything for the Reliability Control Board. I had ten days to the RCB deadline. The existing evidence — the vendor's lot documentation plus our own teardown — already lined up on the seal material as the cause. Technically that was enough to write the corrective action request. But there was also an option to send the valve out to an external metallurgical lab for an independent composition assay, which would be a fully independent third data point rather than relying on the vendor's own account of their material.

Interviewer: And what did you decide?

Participant: I sent it out. I wanted the submission to be as solid as possible — this is a corrective action request that could turn into a fleet campaign, and I didn't want to hand the board something that was only two-thirds independently verified. Having a truly outside lab confirm it felt like it would make the whole package more defensible, even knowing the lab's turnaround was about three weeks, which meant we'd blow through the RCB deadline before that data came back.

Interviewer: At the time you sent it out, was there anything the assay could tell you that would have changed which corrective action you recommended?

Participant: Honestly... probably not the underlying conclusion. The seal-material story was already coherent — vendor records and physical teardown agreed. I think I was thinking more about the strength of the case than whether the case would actually change.

Interviewer: What happened with the deadline?

Participant: We missed presenting a finalized recommendation at that RCB cycle. It slipped to submit-pending-lab-results. When the assay results did eventually land, they confirmed the same seal-material change the vendor had already told us about — nothing new in it.

Interviewer: Let's move to the final decision — what you actually recommended once everything was in.

Participant: Once the root cause was locked down, the OEM tech rep raised the idea of a broader design review of the valve seal spec generally, as a longer-term option. But that's a slow, separate track. What I had in front of me was a specific, bounded problem: one vendor lot, identifiable serial ranges. I wrote the corrective action request to replace valves from that lot specifically, not a fleet-wide swap of every valve regardless of lot, and not just deferring to wait on the OEM's broader review.

Interviewer: Why bounded to the lot rather than fleet-wide?

Participant: Because a fleet-wide replacement would have pulled serviceable, unaffected valves for no reason — that's cost and downtime with no reliability benefit. The evidence pointed specifically at that lot, so that's what I scoped the action to.

Interviewer: What happened after you submitted it?

Participant: RCB approved the lot-based campaign. Both tails got their valves replaced, and there haven't been further events on either aircraft since. The OEM's broader design review got pushed into a separate long-term study, which is still open as far as I know.

Interviewer: Looking back at the whole sequence — is there a point where, with hindsight, you'd handle it differently?

Participant: The one thing I go back and forth on is the external lab. If I'd known going in that it would just restate what we already had, I might have submitted on the original ten-day timeline and let the RCB approve based on the vendor and teardown evidence alone. I don't think it was wrong to want outside confirmation — this becomes a fleet-level safety call, and I'd rather be too careful than not careful enough. But I'll admit, looking at it now, I'm not sure that extra data point actually changed anything I ended up recommending.

Interviewer: If the assay had come back showing something different from the vendor's account — a different degradation mechanism, say — what would you have done?

Participant: Then it would've mattered a lot, and I'd have had to go back and possibly widen the scope beyond that one lot. That's part of why it felt worth doing at the time.

Interviewer: And if this exact pattern showed up again on a different fleet type — same lot-based signature, same timeline pressure — would you send it out for independent lab work again?

Participant: Probably, yeah, if the timing allowed it. Though I think I'd ask myself earlier on whether the extra data was likely to change the recommendation or just make me feel better about it, and weigh that against the deadline more explicitly than I did this time.

Interviewer: That's a good place to stop. Thanks for the detail — this is exactly the kind of reconstruction we needed.

Participant: No problem. Happy to follow up if anything else comes to mind.}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Information bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as seeking additional data that cannot change the pending corrective-action decision, motivated by a belief that more information improves decision quality/defensibility rather than by actual decision relevance."
      }
    ],
    "target_bias_names": [
      "Information bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Information bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
        "mechanism": "Commissioning a costly, schedule-delaying external metallurgical assay that duplicates already-sufficient vendor and in-house evidence, pursued because more information is assumed to be inherently valuable/defensible rather than because it can change the corrective-action recommendation.",
        "affected_reasoning_operation": "Evidence-sufficiency assessment prior to finalizing a root-cause-based recommendation",
        "evidence_source": "External metallurgical assay request vs. existing vendor lot documentation and in-house teardown results",
        "distinctiveness_requirement": "Single instance only; must not be echoed as a second, differently-worded instance at any other decision point, probe, or hypothetical."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ib_01",
        "bias": "Information bias",
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
    "scenario_id": "AV_Biased_1",
    "domain_id": "AV",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point (phase 3, evidence-selection prior to corrective-action recommendation) offering the best mechanism fit for information bias, where sufficient decision-relevant evidence already existed and additional information-seeking could not alter the outcome; no split across multiple points was needed since occurrences = 1.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "AV_Biased_1",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Commercial aviation maintenance reliability and corrective-action governance",
    "role": "Maintenance Control reliability engineer",
    "objective": "Identify the cause and appropriate scope of corrective action for recurrent APU bleed-air valve faults while managing dispatch, maintenance, and Reliability Control Board timing constraints",
    "incident_type": "Repeated ground-detected APU bleed-air valve write-ups on two aircraft linked to a common vendor valve lot and suspected seal-material degradation",
    "confidence": 0.99
  },
  "structure_audit": {
    "estimated_word_count": 1240,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "Open a focused tail-specific review rather than characterize the initial pattern as a fleet-wide problem",
        "evidence_before": [
          "Tail 738 recorded three APU bleed-air valve write-ups within 45 flight days",
          "Two earlier write-ups were closed as operational check normal with no parts replaced",
          "Fleet-wide valve removal rate remained within OEM MTBUR"
        ],
        "evidence_after": [
          "Tail 712 recorded a lower-severity similar complaint two days later",
          "The two aircraft shared a valve batch lot number"
        ],
        "goals_constraints": [
          "Detect a potentially recurrent reliability problem",
          "Avoid prematurely declaring a fleet-wide issue",
          "Monitor for similar events elsewhere"
        ],
        "alternatives": [
          "Treat the event as normal operational noise",
          "Declare a fleet-wide reliability problem immediately",
          "Conduct a focused review of tail 738 while monitoring the fleet"
        ],
        "decision_basis": "The recurrence on one tail was unusual but fleet-level removal data did not yet support a fleet-wide conclusion.",
        "time_pressure": "No explicit acute deadline at this point.",
        "uncertainty": "Whether the recurrence reflected an isolated aircraft issue, intermittent fault, or broader component-lot problem."
      },
      {
        "id": 2,
        "summary": "Impose a one-leg maximum MEL carryover restriction on the two affected tails and open a lot-based root-cause investigation rather than ground both aircraft outright",
        "evidence_before": [
          "A second aircraft showed a similar complaint",
          "Line maintenance reported that the valve was difficult to bench-test and could have an intermittent fault",
          "The affected valves shared a batch lot number",
          "Neither aircraft had experienced an in-flight consequence"
        ],
        "evidence_after": [
          "Vendor documentation identified a seal-material change for the lot",
          "The teardown of the removed valve showed degradation consistent with that change"
        ],
        "goals_constraints": [
          "Limit repeated dispatch under MEL for the same defect",
          "Maintain operational availability where evidence did not yet justify grounding",
          "Establish root cause and lot scope"
        ],
        "alternatives": [
          "Ground both aircraft",
          "Allow normal MEL carryover",
          "Limit carryover to one leg and investigate the implicated lot"
        ],
        "decision_basis": "The recurrence and common lot justified a restriction and investigation, but the absence of in-flight consequences made immediate grounding appear disproportionate.",
        "time_pressure": "Operational dispatch and MEL carryover considerations.",
        "uncertainty": "Whether the intermittent issue represented a safety-relevant defect requiring broader operational action."
      },
      {
        "id": 3,
        "summary": "Commission an external metallurgical assay before submitting the corrective-action package, despite a ten-day RCB deadline and already convergent vendor and teardown evidence",
        "evidence_before": [
          "Vendor quality documentation identified a seal-material change in the relevant lot",
          "In-house teardown showed seal degradation consistent with that material change",
          "The available evidence was described as technically sufficient to write the corrective-action request",
          "An external assay would take approximately three weeks while the RCB deadline was ten days away"
        ],
        "evidence_after": [
          "The RCB submission was delayed pending lab results",
          "The assay confirmed the vendor-reported seal-material change and supplied no new finding"
        ],
        "goals_constraints": [
          "Submit a defensible corrective-action request",
          "Meet the RCB cycle deadline",
          "Ensure that a potentially fleet-relevant action rests on adequate evidence"
        ],
        "alternatives": [
          "Submit on the ten-day timeline using vendor documentation and in-house teardown",
          "Commission the external assay and submit after results return"
        ],
        "decision_basis": "The participant prioritized an independent third data point and perceived defensibility over deadline adherence.",
        "time_pressure": "Ten days to the RCB deadline versus an approximately three-week laboratory turnaround.",
        "uncertainty": "Whether independent composition testing could reveal a different degradation mechanism and change the recommended action's scope."
      },
      {
        "id": 4,
        "summary": "Recommend replacement only for the implicated lot and serial range rather than a fleet-wide replacement or deferral pending a broader OEM design review",
        "evidence_before": [
          "Vendor lot documentation and teardown findings converged on a lot-specific seal-material issue",
          "The OEM representative suggested a broader design review as a longer-term option",
          "The affected serial ranges were identifiable"
        ],
        "evidence_after": [
          "RCB approved the lot-based replacement campaign",
          "The two affected tails had no further reported events after replacement",
          "The broader OEM design review continued separately"
        ],
        "goals_constraints": [
          "Correct the identified failure mechanism",
          "Avoid unnecessary removal of serviceable components",
          "Separate immediate corrective action from a longer-term design question"
        ],
        "alternatives": [
          "Replace valves only from the implicated lot",
          "Replace all fleet valves",
          "Defer action until completion of the OEM's broader design review"
        ],
        "decision_basis": "The causal evidence and traceability pointed to one lot, while fleet-wide replacement was represented as cost and downtime without demonstrated incremental reliability benefit.",
        "time_pressure": "The prior RCB-cycle delay had occurred, but no separate explicit deadline is stated at this point.",
        "uncertainty": "Whether the lot-specific mechanism also reflected a broader valve-design vulnerability."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "ib_01",
      "bias": "Information bias",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 3,
      "supporting_quote": "“Technically that was enough to write the corrective action request.” ... “I wanted the submission to be as solid as possible ... I didn't want to hand the board something that was only two-thirds independently verified.” ... “Honestly... probably not the underlying conclusion.”",
      "evidence_location": "Decision-point-3 exchange beginning with the ten-day RCB deadline, continuing through the decision to commission the external assay and the subsequent probe concerning whether the assay could change the recommendation.",
      "mechanism": "The participant sought an additional, schedule-delaying independent data point after stating that available vendor documentation and physical teardown were enough to write the request. The stated motive is greater defensibility and confidence in the package rather than a clearly identified decision-relevant information gap.",
      "strength": "weak",
      "confidence": 0.79,
      "plausible_nonbias_explanation": "Independent testing can be justified in a safety-relevant reliability decision because an assay that revealed a different degradation mechanism could legitimately alter the intervention's scope. The participant expressly acknowledges that a discordant result might have required widening the action beyond the implicated lot. That admission prevents a finding that the information could not change the pending decision.",
      "additional_evidence_needed": "Evidence that the participant had already committed to the same lot-based corrective-action recommendation regardless of the assay result, and that the external assay's defined scope could only duplicate the already-established material finding rather than test a plausible alternative mechanism or alter the recommendation.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_reasoning_revision",
        "location": "Decision point 3, especially the answer to “At the time you sent it out, was there anything the assay could tell you that would have changed which corrective action you recommended?” and the later hypothetical about a different result.",
        "current_defect": "The text simultaneously supplies evidence of information bias and a decision-relevant justification for the assay. The participant says the assay probably would not change the underlying conclusion, but also says a different result could have changed the scope. This makes the additional information potentially action-relevant rather than clearly noninstrumental.",
        "minimal_change_instruction": "Keep the external assay, three-week turnaround, missed RCB cycle, vendor documentation, and teardown unchanged. Revise the participant's reasoning so the assay request is explicitly limited to independent confirmation of the already documented seal-material substitution, after the participant has already determined that the lot-based replacement request will proceed on the existing evidence. Replace or narrow the later hypothetical so that it does not introduce an untested alternative mechanism capable of widening the recommendation; the participant can instead state that a contradictory result would trigger a separate follow-up investigation after the same pending lot action is submitted.",
        "preserve": [
          "The aviation reliability setting and Maintenance Control role",
          "The ten-day RCB deadline and approximately three-week laboratory turnaround",
          "The two convergent evidence sources: vendor lot documentation and in-house teardown",
          "The single assay episode as the only intended information-bias occurrence",
          "The eventual lot-based corrective-action recommendation"
        ],
        "avoid_creating": [
          "A second information-bias instance through repeated restatements of the same assay rationale",
          "A new confirmation-bias cue such as dismissing genuinely contradictory assay evidence",
          "A portrayal of the participant as disregarding a required safety, regulatory, or governance control"
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Information bias",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Confirmation bias",
      "decision_point": 3,
      "supporting_quote": "“The seal-material story was already coherent — vendor records and physical teardown agreed. I think I was thinking more about the strength of the case than whether the case would actually change.”",
      "mechanism": "The wording could superficially suggest seeking confirmatory evidence for an established conclusion.",
      "confidence": 0.22,
      "status": "rejected",
      "plausible_nonbias_explanation": "The participant chose an external laboratory specifically because it was independent of the vendor, and later states that a discordant finding would have mattered substantially. This is not selective exposure to congenial evidence or dismissal of disconfirming evidence.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Outcome bias or hindsight bias",
      "decision_point": 3,
      "supporting_quote": "“If I'd known going in that it would just restate what we already had, I might have submitted on the original ten-day timeline.”",
      "mechanism": "The retrospective result could be mistaken for judging the original decision solely by its eventual outcome.",
      "confidence": 0.18,
      "status": "rejected",
      "plausible_nonbias_explanation": "The participant retains the original uncertainty, recognizes why independent confirmation felt valuable at the time, and identifies a prospective decision-relevance test for future cases. The reflection is calibrated hindsight rather than an outcome-based condemnation of the original decision.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "Opening a tail-specific review rather than immediately declaring a fleet-wide problem",
      "location": "Early incident reconstruction, after the third write-up on tail 738",
      "why_not_bias": "The participant integrates the unusual recurrence with fleet-wide MTBUR data, takes a proportionate intermediate action, and creates a monitoring flag. This is a calibrated response to incomplete evidence, not underreaction, status-quo bias, or normalcy bias."
    },
    {
      "cue": "Imposing a one-leg MEL carryover maximum rather than grounding both aircraft",
      "location": "Decision point 2",
      "why_not_bias": "The decision is grounded in explicit policy, no reported in-flight consequence, and a stated concern that immediate grounding would exceed the available evidence. It is a risk-management tradeoff, not evidence of omission bias or risk-seeking."
    },
    {
      "cue": "Relying in part on vendor documentation",
      "location": "Root-cause investigation and decision point 3",
      "why_not_bias": "Vendor documentation is a traceable evidence source and is corroborated by an in-house teardown. Reliance on a supplier record is not itself authority bias, particularly where the participant seeks independent corroboration."
    },
    {
      "cue": "Recommending a lot-specific campaign rather than fleet-wide replacement",
      "location": "Decision point 4",
      "why_not_bias": "The recommendation follows identifiable serial ranges, lot-specific documentation, and physical evidence. Limiting scope to evidence-supported components is justified proportionality, not narrow framing or anchoring."
    },
    {
      "cue": "No further events after replacement",
      "location": "Post-submission outcome",
      "why_not_bias": "The participant reports an operational outcome but does not use it as the sole basis for the earlier causal inference. It is weak confirmatory follow-up evidence, not independently decisive proof."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "A documented seal-material change in the implicated vendor lot caused the observed seal degradation and recurrent valve complaints.",
        "support": "Vendor documentation identifies the material change; teardown of the valve removed from tail 738 found degradation described as consistent with that change; the external assay reportedly confirmed the same material change.",
        "assessment": "Moderately supported causal attribution. The evidence is convergent and mechanism-linked, but the transcript does not describe a comparative failure analysis, testing of unaffected valves, or exclusion of alternative contributors."
      },
      {
        "claim": "A lot-specific replacement campaign was the appropriate corrective action.",
        "support": "The lot and serial range were identifiable, and the evidence was represented as specific to that lot.",
        "assessment": "Reasonably coherent decision logic, conditional on the lot-specific causal attribution. The interview does not independently establish that no other lots carried the same material or degradation risk."
      },
      {
        "claim": "Replacing the valves resolved the issue.",
        "support": "The two affected tails had no further reported events after replacement.",
        "assessment": "Weak post-intervention support only. Two aircraft and an unspecified observation interval cannot rule out regression to the mean, low event frequency, changed operating conditions, or incomplete reporting."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "The shared lot number is initially correlational evidence rather than proof of causation.",
        "mitigation_present": "The transcript adds vendor change documentation and physical teardown findings, which are stronger than the common-lot association alone."
      },
      {
        "risk": "The absence of later events is treated narratively as favorable but could be overread as confirmation that the campaign caused resolution.",
        "mitigation_needed": "State the duration of follow-up, denominator of exposure, and whether comparable unaffected or replaced components were examined before treating the outcome as strong causal validation."
      }
    ],
    "counterfactual_present": true,
    "changed_variable": "The hypothetical external assay result: instead of confirming the vendor account, it indicates a different degradation mechanism.",
    "held_constant": [
      "The same two affected aircraft and implicated lot",
      "The existing vendor documentation and in-house teardown evidence",
      "The pending corrective-action context"
    ],
    "causal_coherence": "moderate",
    "explanation": "The counterfactual is coherent as a decision-sensitivity probe: a genuinely different degradation mechanism could justify reconsidering the action's scope. However, this same logic weakens the intended information-bias mechanism because it demonstrates that the assay might have decision relevance. The counterfactual should be narrowed if the intended test condition requires information that cannot alter the pending corrective action."
  },
  "quality_scores": {
    "occupational_realism": 91,
    "cta_fidelity": 88,
    "bias_separability": 61,
    "bias_subtlety": 84,
    "control_fidelity": 100,
    "counterfactual_fidelity": 72,
    "narrative_coherence": 93,
    "naturalness": 90,
    "hidden_label_integrity": 67,
    "overall_quality": 78
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 0,
    "requested_occurrence_total": 1,
    "missing_occurrence_total": 1,
    "accidental_occurrence_total": 0,
    "priority": "medium",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Retain exactly four decision points.",
      "Retain one and only one information-bias episode, located at decision point 3.",
      "Do not convert justified lot-specific risk management, independent corroboration, or bounded corrective-action scope into bias.",
      "Do not add a second causal change to the assay counterfactual while repairing decision irrelevance.",
      "Preserve the distinction between the immediate lot-based campaign and the separate longer-term OEM design review."
    ],
    "revision_order": [
      "Revise the decision-relevance framing of the external assay at decision point 3.",
      "Narrow the later hypothetical so it no longer establishes that assay information could alter the pending lot-based recommendation.",
      "Recheck that the revised interview still contains one distinct assay decision episode and no additional information-seeking episode with the same mechanism."
    ]
  },
  "failure_flags": [
    {
      "flag": "target_mechanism_not_fully_satisfied",
      "severity": "medium",
      "detail": "The intended information-bias instance is not fully supported because the interview explicitly gives the external assay a plausible ability to change the corrective-action scope if it identifies a different mechanism."
    },
    {
      "flag": "specification_text_conflict",
      "severity": "medium",
      "detail": "The hidden specification requires additional information that cannot change the pending corrective-action decision, while the participant's counterfactual says a different assay result could require widening the scope beyond one lot."
    }
  ]
}}}

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
