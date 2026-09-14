<RAW_INTERVIEW>
Interviewer: Thanks for making time this week of all weeks. Before we start, this is just for our internal process-improvement review — I'll ask you to walk me through a recent stretch of work, and there's no wrong answer. That okay?

Participant: Sure, happy to. Lock week is a good time to talk about it, honestly, everything's still fresh.

Interviewer: Great. Can you remind me of your role and what was on your plate?

Participant: I'm the CRC for our site on the Phase III trial — the oncology drug study. I handle adverse event triage, case report form cleanup, and screening new referrals. That week we were seven days out from the interim data lock for the DSMB, so basically everything converged at once.

Interviewer: Walk me through what that week looked like.

Participant: Monday morning I got a lab flag on Participant 12 — an ALT elevation, elevated but not dramatically so, and the timeline relative to dosing wasn't clean. Could've been drug-related, could've been something else entirely, maybe even diet or an OTC medication he didn't mention. I had to assign a causality category for the AE report. Same day, I was also mid-reconciliation on Participant 07's case report forms — that one had been a slog for almost two weeks, lots of inconsistent entries between the source charts and the CRF. Then Wednesday a new referral came in for screening, and Thursday there was a multi-site coordinator call about verification procedures ahead of lock. So four distinct things, all against the same deadline.

Interviewer: Let's start with Participant 12. What did you have in front of you?

Participant: His ALT was elevated, but in a range where you genuinely can't tell just from the number whether it's the study drug. Our protocol has three buckets — related, possibly related, unrelated — for exactly this kind of situation. I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.

Interviewer: How did that shape the classification?

Participant: I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed.

Interviewer: What about the "possibly related" option?

Participant: Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But "possibly related" kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.

Interviewer: What happened after?

Participant: The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after.

Interviewer: Let's move to Participant 07.

Participant: That one's been painful. I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records. Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that.

Interviewer: What did you do with that discrepancy?

Participant: I kept going. Twenty hours felt like too much to walk away from without one more push. And honestly the "losing a fifth of our population" framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it.

Interviewer: Did you consider flagging it as a deviation instead?

Participant: I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.

Interviewer: How did it turn out?

Participant: The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later.

Interviewer: Let's talk about the new referral on Wednesday.

Participant: He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has.

Interviewer: What did you do with that instinct?

Participant: I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he "probably" wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.

Interviewer: What happened when you did screen him?

Participant: He met every inclusion criterion. Clean screen, no issues. Which doesn't tell you much either way about whether deprioritizing him was the right call — I just got lucky that lock week didn't cost us his enrollment.

Interviewer: Last one — the coordinator call about verification.

Participant: Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever.

Interviewer: What made you switch?

Participant: Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.

Interviewer: Any pushback since?

Participant: The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond "everyone else was doing it too."

Interviewer: If you could go back, what single piece of information would have changed any of these calls?

Participant: For Participant 12, if I'd pulled his full history first instead of after, I might not have leaned so hard on that other case. For the verification switch, actual error-rate data would've mattered — I just didn't have it and didn't chase it down in time.

Interviewer: What if that Monday meeting about the other participant's enzyme case had never come up?

Participant: I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind.

Interviewer: And if the Site Director's email had framed Participant 07 differently — say, just asking whether continued reconciliation was worth the time?

Participant: I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have.

Interviewer: Last one — if none of the other sites had mentioned switching methods on that call?

Participant: I probably would've stuck with what we had. It's passed every audit. There wasn't really a problem to solve, other than speed.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HC_Biased_6",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Clinical Research Coordinator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Interim Lock Week: Safety Signal, Salvage Data, and a New Referral",
    "scenario_summary_internal": "A Clinical Research Coordinator (CRC) at an academic oncology trials unit is managing final data cleanup, safety-signal triage, and screening tasks in the seven days before a Phase III trial's interim DSMB data lock. She must classify an ambiguous liver-enzyme adverse event, decide whether to keep salvaging a problematic participant's inconsistent case report forms, screen an atypical new referral for eligibility, and decide whether to adopt a network-wide data verification shortcut other sites have started using. Time pressure from the lock deadline and competing priorities (safety reporting, enrollment targets, data completeness) create realistic conditions for subtle reasoning shortcuts without any decision mechanically proving bias.",
    "occupational_realism": {
      "objective": "Finalize safety classifications, resolve data discrepancies, screen a new referral, and align site data practices before the interim DSMB data lock in 7 days.",
      "setting": "Oncology clinical trials unit at an academic medical center, coordinating a multi-site Phase III drug trial in its final week before interim analysis lock.",
      "constraints": [
        "Interim data lock deadline in 7 days",
        "Limited CRC bandwidth split across safety reporting, data cleanup, and screening",
        "Expedited adverse event reporting timelines under GCP/ICH-E6",
        "Site enrollment targets tied to funding milestones",
        "Reliance on multi-site coordinator calls for shared practices"
      ],
      "stakeholders": [
        "Principal Investigator (PI)",
        "Site Director",
        "Data Safety Monitoring Board (DSMB) liaison",
        "Participant 07 (data-quality case)",
        "New referral participant",
        "Network coordinators at other trial sites"
      ],
      "technical_terms_to_use": [
        "adverse event (AE)",
        "causality assessment",
        "case report form (CRF)",
        "protocol deviation",
        "per-protocol population",
        "source data verification",
        "interim data lock",
        "eligibility screening",
        "inclusion/exclusion criteria"
      ],
      "technical_terms_to_avoid": [
        "ambiguity bias",
        "sunk cost bias",
        "representativeness heuristic",
        "bandwagon effect",
        "framing effect",
        "recency bias",
        "any explicit bias/heuristic terminology"
      ]
    },
    "timeline": [
      {
        "phase": 0,
        "decision_point": false,
        "facts_available_before_decision": [
          "Interim DSMB lock is in 7 days",
          "CRC has three open workstreams: AE review, Participant 07 data cleanup, new referral screening"
        ],
        "new_information_after_decision": [],
        "alternatives": [],
        "intended_action": "Establish setting and workload context; no decision made."
      },
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Participant 12's liver enzyme (ALT) result is elevated but within a range where causality to study drug is genuinely uncertain",
          "Protocol requires a causality classification of 'related,' 'possibly related,' or 'unrelated' for AE reporting",
          "Team discussed a different participant's clearly unrelated enzyme elevation in a meeting three days earlier"
        ],
        "new_information_after_decision": [
          "PI later requests the source labs and prior medical history be re-reviewed for Participant 12"
        ],
        "alternatives": [
          "Classify as 'possibly related' pending further workup",
          "Classify as 'unrelated' based on resemblance to the recently discussed case",
          "Escalate immediately for expedited safety reporting"
        ],
        "intended_action": "CRC leans toward 'unrelated,' anchoring the judgment on the most recently discussed similar-sounding case rather than working through Participant 12's own concurrent medications and timeline."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "CRC has logged roughly 20 hours reconciling Participant 07's inconsistent CRFs",
          "A new, larger discrepancy is discovered in Participant 07's dosing records",
          "Site Director sends an email framing the choice as either 'recovering the data already invested in' or 'losing a fifth of the site's evaluable per-protocol population'"
        ],
        "new_information_after_decision": [
          "Additional reconciliation work reveals the dosing discrepancy is not resolvable from existing source documents"
        ],
        "alternatives": [
          "Continue reconciliation to try to salvage Participant 07's data",
          "Flag as a protocol deviation and exclude from the per-protocol analysis",
          "Request an independent second reviewer before deciding"
        ],
        "intended_action": "CRC commits additional hours to salvaging Participant 07's record, citing the time already spent, and is swayed toward continuing by the Site Director's loss-framed email rather than reassessing the discrepancy fresh."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "New referral is younger, physically active, and has no visible comorbidities, unlike most enrolled participants who are older with multiple comorbidities",
          "Protocol eligibility criteria are objective (biomarker status, prior treatment lines, organ function) and do not reference age or comorbidity profile as exclusion factors",
          "CRC has processed dozens of referrals matching the 'typical' older, comorbid profile this trial cycle"
        ],
        "new_information_after_decision": [
          "Formal eligibility screening later confirms the referral meets all inclusion criteria"
        ],
        "alternatives": [
          "Proceed with full standard eligibility screening regardless of how the referral 'looks'",
          "Deprioritize the referral as an unlikely candidate given how atypical the profile seems",
          "Ask the PI for a quick opinion before screening"
        ],
        "intended_action": "CRC initially deprioritizes and slow-walks the referral's screening because the participant doesn't resemble the trial's 'typical' enrolled profile, rather than applying the written criteria directly."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "On a multi-site coordinator call, several other sites mention they have already switched to a faster source data verification shortcut ahead of lock",
          "No independent validation data on the shortcut's error rate has been shared or reviewed by this site",
          "The current site's own verification method has passed monitoring audits with no findings"
        ],
        "new_information_after_decision": [
          "The monitor later asks why the site changed its verification method without documented rationale"
        ],
        "alternatives": [
          "Adopt the shortcut method because most other sites have already switched",
          "Retain the current, audited verification method",
          "Request the network's validation data before deciding"
        ],
        "intended_action": "CRC adopts the network's shortcut method mainly because most other sites are already using it, without seeking or reviewing independent validation data first."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what this week looked like leading up to the interim lock.",
        "What were you ultimately responsible for delivering before the lock date?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you notice that made you pause?",
        "What information did you have in hand at each step, and what came in afterward?"
      ],
      "decision_point_probes": [
        "What options did you consider for Participant 12's AE classification, and what tipped it?",
        "What made you decide to keep working on Participant 07 rather than flag the deviation?",
        "What was your initial read on the new referral, and what changed it?",
        "What led you to adopt the verification shortcut the other sites were using?"
      ],
      "decision_basis": [
        "What specific piece of information mattered most in each decision?",
        "Did anything from a prior case or conversation influence how you saw the current one?"
      ],
      "alternatives": [
        "What other options did you consider at each point, and why didn't you choose them?"
      ],
      "prior_experience": [
        "Have you handled a similar AE classification, data salvage decision, or referral before? How did that shape your thinking here?"
      ],
      "time_pressure_and_uncertainty": [
        "How much did the lock deadline weigh on how quickly you moved through these decisions?",
        "Where did you feel most uncertain, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the recent team discussion about the other case hadn't happened, would your AE classification have gone differently?",
        "If the Site Director's email had been framed differently, would you have made the same call on Participant 07?",
        "If the new referral had looked like your 'typical' participant, would screening have moved faster?",
        "If no other sites had mentioned switching methods, would you have adopted the shortcut?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "amb_01",
        "bias": "Ambiguity Bias",
        "decision_point": 1,
        "mechanism": "Avoids committing to the genuinely uncertain 'possibly related' causality category and instead resolves the ambiguity by defaulting to a more certain-feeling classification not fully supported by Participant 12's own data.",
        "affected_reasoning_operation": "Causality classification under genuine probabilistic uncertainty",
        "evidence_available_at_time": [
          "Participant 12's ALT elevation with unclear causal link",
          "Availability of an intermediate 'possibly related' category in the protocol's AE classification scheme"
        ],
        "required_textual_manifestation": "CRC explicitly avoids the 'possibly related' option because it feels unresolved, choosing a definite label despite acknowledging the evidence doesn't clearly support it.",
        "plausible_nonbias_interpretation": "CRC may have reasonably weighed the labs and concluded 'unrelated' based on legitimate clinical judgment about the timeline.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity bias", "ambiguity aversion"]
      },
      {
        "instance_id": "rec_01",
        "bias": "Recency Bias",
        "decision_point": 1,
        "mechanism": "Overweights the most recently discussed AE case from a team meeting days earlier when forming the causality judgment, rather than weighting Participant 12's full concurrent medication and symptom history equally.",
        "affected_reasoning_operation": "Recall and weighting of comparison cases during causality assessment",
        "evidence_available_at_time": [
          "Team discussion of a different, recently reviewed unrelated enzyme elevation case",
          "Participant 12's own longer-term medication and lab history"
        ],
        "required_textual_manifestation": "CRC references the recently discussed case as the primary point of comparison, giving it more influence than a systematic review of Participant 12's own record.",
        "plausible_nonbias_interpretation": "The recent case may be genuinely clinically similar and a legitimately useful reference point.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency bias", "recency effect"]
      },
      {
        "instance_id": "sunk_01",
        "bias": "Sunk Costs Bias",
        "decision_point": 2,
        "mechanism": "Justifies continuing to invest additional hours in Participant 07's reconciliation primarily by reference to the roughly 20 hours already spent, rather than by an independent assessment of the discrepancy's resolvability going forward.",
        "affected_reasoning_operation": "Continue/discontinue resource-allocation decision under new negative information",
        "evidence_available_at_time": [
          "Log of ~20 hours already spent reconciling Participant 07's CRFs",
          "Newly discovered, larger dosing discrepancy"
        ],
        "required_textual_manifestation": "CRC cites the hours already invested as a reason to keep going, separate from any forward-looking estimate of whether the new discrepancy is actually resolvable.",
        "plausible_nonbias_interpretation": "Continuing could be a reasonable bet if the CRC believed the new discrepancy was likely resolvable with modest extra effort.",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "sunk cost fallacy"]
      },
      {
        "instance_id": "fram_01",
        "bias": "Framing Effect",
        "decision_point": 2,
        "mechanism": "The decision to continue is shaped by the Site Director's email framing the choice as avoiding a loss ('losing a fifth of the evaluable population') rather than as a data-quality gain, independent of the sunk-cost reasoning.",
        "affected_reasoning_operation": "Option evaluation under a loss-framed versus gain-framed description of the same underlying outcome",
        "evidence_available_at_time": [
          "Site Director's email framing continuation as loss-avoidance",
          "The underlying decision content, which is logically equivalent regardless of framing"
        ],
        "required_textual_manifestation": "CRC's stated rationale echoes the loss-framed language from the email (e.g., avoiding losing part of the per-protocol population) as a distinct driver from the hours-invested reasoning.",
        "plausible_nonbias_interpretation": "The Site Director's framing might accurately reflect a real statistical power concern the CRC independently agrees with.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "loss framing", "gain framing"]
      },
      {
        "instance_id": "rep_01",
        "bias": "Representativeness",
        "decision_point": 3,
        "mechanism": "Judges the new referral's likelihood of eligibility based on how closely the participant resembles the 'typical' enrolled profile (older, comorbid) rather than applying the protocol's actual objective inclusion/exclusion criteria.",
        "affected_reasoning_operation": "Prioritization/likelihood judgment for screening a new case against a category prototype",
        "evidence_available_at_time": [
          "Referral's age, activity level, and lack of visible comorbidities",
          "Written protocol eligibility criteria unrelated to age or comorbidity appearance"
        ],
        "required_textual_manifestation": "CRC explains deprioritizing the referral by describing how it 'doesn't look like' the usual participant, rather than by any criterion actually listed in the protocol.",
        "plausible_nonbias_interpretation": "CRC might have deprioritized simply due to a full queue, unrelated to the participant's profile.",
        "strength": "subtle",
        "do_not_make_explicit": ["representativeness", "base rate", "stereotype"]
      },
      {
        "instance_id": "band_01",
        "bias": "Bandwagon effect",
        "decision_point": 4,
        "mechanism": "Adopts the network's data verification shortcut primarily because most other sites have already switched, without independently seeking or reviewing validation evidence, despite the current method's clean audit history.",
        "affected_reasoning_operation": "Adoption decision for a process change under peer/majority influence",
        "evidence_available_at_time": [
          "Multiple other sites reporting they switched to the shortcut method",
          "Absence of shared validation data on the shortcut's error rate",
          "Current site's clean audit history with the existing method"
        ],
        "required_textual_manifestation": "CRC's stated reason for switching centers on 'everyone else already doing it' rather than on any independent evaluation of the shortcut's validity.",
        "plausible_nonbias_interpretation": "Switching could be a reasonable time-saving move under lock-week pressure regardless of peer behavior.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon effect", "social proof", "conformity"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control generated in this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "NOT_APPLICABLE_FOR_BIASED_CONDITION (autoselected candidate for future pairing: presence vs. absence of the multi-site coordinator call disclosing the verification shortcut before Decision Point 4)",
      "original_state": "Coordinator call occurs and discloses that other sites have switched methods",
      "counterfactual_state": "No coordinator call occurs; CRC evaluates the verification method change in isolation",
      "variables_to_hold_constant": [
        "Interim lock deadline",
        "Participant 07 data discrepancy details",
        "Participant 12 AE facts",
        "New referral profile and true eligibility outcome"
      ],
      "expected_causal_difference": "Without the peer-disclosure trigger, adoption of the shortcut would need to rest on independently sought validation evidence rather than majority practice, plausibly reducing or eliminating the bandwagon-driven adoption instance.",
      "causal_test_question": "Does removing the multi-site call disclosure change whether the CRC adopts the unverified shortcut method?"
    },
    "generation_checks": [
      "Confirm exactly 6 total bias instances are embedded, one per manifest entry.",
      "Confirm exactly 4 decision points exist and each has at least two alternatives.",
      "Confirm no bias name, definition, or psychological label appears in the public interview text.",
      "Confirm Decision Point 1 contains two distinct instances (ambiguity, recency) with separate evidence sources and reasoning operations.",
      "Confirm Decision Point 2 contains two distinct instances (sunk cost, framing) with separate evidence sources and reasoning operations.",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and the probe plan without repetitive exposition.",
      "Confirm consequences described do not conclusively prove bias (e.g., referral turning out eligible does not itself prove representativeness occurred)."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Ambiguity Bias", "occurrences": 1, "mechanism_constraint": "avoidance of an intermediate/uncertain causality category in favor of a more definite classification" },
      { "bias": "Sunk Costs Bias", "occurrences": 1, "mechanism_constraint": "continuation justified by hours already invested rather than forward-looking resolvability" },
      { "bias": "Representativeness", "occurrences": 1, "mechanism_constraint": "eligibility likelihood judged by resemblance to typical enrolled profile rather than written criteria" },
      { "bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "adoption of a practice because most peer sites have already adopted it, absent independent validation" },
      { "bias": "Framing Effect", "occurrences": 1, "mechanism_constraint": "decision swayed by loss-framed vs. gain-framed description of an equivalent outcome" },
      { "bias": "Recency Bias", "occurrences": 1, "mechanism_constraint": "overweighting the most recently encountered comparison case relative to fuller case history" }
    ],
    "target_bias_names": [
      "Ambiguity Bias",
      "Sunk Costs Bias",
      "Representativeness",
      "Bandwagon effect",
      "Framing Effect",
      "Recency Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Ambiguity Bias", "requested_occurrences": 1 },
      { "bias": "Sunk Costs Bias", "requested_occurrences": 1 },
      { "bias": "Representativeness", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Framing Effect", "requested_occurrences": 1 },
      { "bias": "Recency Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "amb_01", "bias": "Ambiguity Bias" },
      { "instance_id": "sunk_01", "bias": "Sunk Costs Bias" },
      { "instance_id": "rep_01", "bias": "Representativeness" },
      { "instance_id": "band_01", "bias": "Bandwagon effect" },
      { "instance_id": "fram_01", "bias": "Framing Effect" },
      { "instance_id": "rec_01", "bias": "Recency Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "amb_01", "bias": "Ambiguity Bias", "decision_point": 1 },
      { "instance_id": "rec_01", "bias": "Recency Bias", "decision_point": 1 },
      { "instance_id": "sunk_01", "bias": "Sunk Costs Bias", "decision_point": 2 },
      { "instance_id": "fram_01", "bias": "Framing Effect", "decision_point": 2 },
      { "instance_id": "rep_01", "bias": "Representativeness", "decision_point": 3 },
      { "instance_id": "band_01", "bias": "Bandwagon effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "amb_01",
        "bias": "Ambiguity Bias",
        "mechanism": "Avoids the genuinely uncertain 'possibly related' causality category, resolving discomfort with ambiguity by choosing a more definite label not fully supported by the evidence.",
        "affected_reasoning_operation": "Causality classification under probabilistic uncertainty",
        "evidence_source": "Participant 12 lab/AE record and protocol classification categories",
        "distinctiveness_requirement": "Must center on avoidance of the ambiguous category itself, not on comparison to another case (that is rec_01's mechanism)."
      },
      {
        "instance_id": "rec_01",
        "bias": "Recency Bias",
        "mechanism": "Overweights a recently discussed comparison case relative to Participant 12's own fuller medication/lab history when forming the causality judgment.",
        "affected_reasoning_operation": "Recall/weighting of comparison evidence",
        "evidence_source": "Team meeting discussion of a different recent case",
        "distinctiveness_requirement": "Must center on comparative overweighting of a recent case, not on category avoidance (that is amb_01's mechanism)."
      },
      {
        "instance_id": "sunk_01",
        "bias": "Sunk Costs Bias",
        "mechanism": "Justifies continued investment in Participant 07's reconciliation by reference to hours already spent rather than forward-looking resolvability of the new discrepancy.",
        "affected_reasoning_operation": "Continue/discontinue resource allocation decision",
        "evidence_source": "Internal hours-logged tracking for Participant 07",
        "distinctiveness_requirement": "Must center on past-cost justification, not on the framing language used by the Site Director (that is fram_01's mechanism)."
      },
      {
        "instance_id": "fram_01",
        "bias": "Framing Effect",
        "mechanism": "Decision to continue is shaped by the Site Director's loss-framed description of the outcome, independent of the sunk-cost reasoning.",
        "affected_reasoning_operation": "Option evaluation under loss- vs gain-framed description",
        "evidence_source": "Site Director's email framing",
        "distinctiveness_requirement": "Must center on reaction to the specific loss-framed wording, not on the hours-invested justification (that is sunk_01's mechanism)."
      },
      {
        "instance_id": "rep_01",
        "bias": "Representativeness",
        "mechanism": "Judges eligibility likelihood by resemblance to the typical enrolled profile rather than by the protocol's actual written criteria.",
        "affected_reasoning_operation": "Prioritization/likelihood judgment against a category prototype",
        "evidence_source": "New referral's demographic/clinical appearance vs. protocol criteria",
        "distinctiveness_requirement": "Must center on profile resemblance reasoning, distinguishable from any capacity/queue-based justification."
      },
      {
        "instance_id": "band_01",
        "bias": "Bandwagon effect",
        "mechanism": "Adopts an unverified verification shortcut primarily because most peer sites have already adopted it.",
        "affected_reasoning_operation": "Process-adoption decision under peer/majority influence",
        "evidence_source": "Multi-site coordinator call disclosures",
        "distinctiveness_requirement": "Must center on majority-adoption as the stated driver, not on independent efficiency analysis."
      }
    ],
    "intended_strength": [
      { "instance_id": "amb_01", "bias": "Ambiguity Bias", "strength": "subtle" },
      { "instance_id": "sunk_01", "bias": "Sunk Costs Bias", "strength": "subtle" },
      { "instance_id": "rep_01", "bias": "Representativeness", "strength": "subtle" },
      { "instance_id": "band_01", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "fram_01", "bias": "Framing Effect", "strength": "subtle" },
      { "instance_id": "rec_01", "bias": "Recency Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE_FOR_BIASED_CONDITION (autoselected candidate: presence vs. absence of multi-site coordinator call disclosure before Decision Point 4)",
      "original_state": "Coordinator call occurs and discloses peer sites' switch to the shortcut method",
      "changed_state": "No coordinator call occurs; CRC evaluates the method change without peer-disclosure",
      "variables_to_hold_constant": [
        "Interim lock deadline",
        "Participant 07 data discrepancy details",
        "Participant 12 AE facts",
        "New referral profile and eligibility outcome"
      ]
    },
    "scenario_id": "HC_Biased_6",
    "domain_id": "HC",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences spread across 4 decision points with a maximum of 2 per point (DP1: Ambiguity Bias + Recency Bias via distinct evidence sources and reasoning operations; DP2: Sunk Costs Bias + Framing Effect via distinct evidence sources and reasoning operations; DP3: Representativeness alone; DP4: Bandwagon effect alone), chosen for mechanism fit and narrative realism per rules 1-4.",
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
        "segment_type": "causality_comparison_and_classification_rationale",
        "raw_interview_anchor": "The recent conversation was the first thing that came to mind as a comparison point; it was the most vivid thing in my head, not necessarily the most similar case.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rec_01"
        ],
        "ground_truth_rationale": "A recently discussed comparison case was overweighted over Participant 12's fuller record."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "uncertainty_resolution_and_causality_choice",
        "raw_interview_anchor": "Possibly related kind of kicked the can down the road; I wanted something I could close out.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "amb_01"
        ],
        "ground_truth_rationale": "The participant avoided the intermediate category because it felt unresolved and burdensome."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "post_decision_correction_reflection",
        "raw_interview_anchor": "The PI asked me to pull his full lab history and prior meds before finalizing it; I probably should have done that up front.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive correction reflection without a hidden bias mechanism."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "resource_allocation_continuation_rationale",
        "raw_interview_anchor": "Twenty hours felt like too much to walk away from without one more push.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "sunk_01"
        ],
        "ground_truth_rationale": "Continuation was justified by prior investment rather than forward-looking resolvability."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "loss_framing_and_option_evaluation",
        "raw_interview_anchor": "The 'losing a fifth of our population' framing stuck with me; it became about what we'd be giving up.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "fram_01"
        ],
        "ground_truth_rationale": "The loss-oriented wording changed evaluation of the continuation decision."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "referral_triage_and_eligibility_likelihood_judgment",
        "raw_interview_anchor": "I put him lower in the queue because he probably wasn't going to qualify; it was more that he didn't match the pattern I'm used to seeing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rep_01"
        ],
        "ground_truth_rationale": "Screening was deprioritized based on prototype mismatch rather than objective criteria."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "outcome_interpretation_and_counterevidence",
        "raw_interview_anchor": "He met every inclusion criterion. Which doesn't tell you much either way about whether deprioritizing him was the right call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant correctly limits retrospective inference from the outcome."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "process_adoption_and_evidence_evaluation",
        "raw_interview_anchor": "Most of the other sites had already moved to it, which made staying with our old method feel like we were behind; I did not look for validation data.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "band_01"
        ],
        "ground_truth_rationale": "The shortcut was adopted because peer sites had adopted it despite absent validation data."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[ontology-free RAG JSON output]
</RAG_ANALYSIS_OUTPUT>
