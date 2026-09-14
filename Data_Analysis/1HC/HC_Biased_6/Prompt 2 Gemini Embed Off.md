You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks
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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "No retrieved RAG corpus passages were supplied with the interview transcript; classifications rely on established cognitive-science knowledge and are marked as lacking retrieved corpus support."
  },
  "identified_bias_summary": [
    {
      "bias_label": "ambiguity aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
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
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging likelihood or causality by the ease with which examples come to mind rather than by systematically weighing all relevant evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 12 ALT causality classification",
      "decision_point_description": "Assigning a causality category to Participant 12's ALT elevation using the protocol categories related, possibly related, or unrelated.",
      "affected_reasoning_operation": "causal attribution / adverse event causality classification",
      "bias_specific_mechanism": "A recent, vivid team-meeting discussion about another participant's enzyme bump was highly available in memory and was used as the primary comparison point, displacing a systematic review of Participant 12's own medication list and dosing timeline.",
      "manifestation_in_interview": "The participant stated that the recent conversation was the first thing that came to mind and that it became the comparison point even though it was not necessarily the most similar case.",
      "effect_on_reasoning_or_decision": "The participant leaned toward classifying Participant 12's ALT elevation as unrelated partly because of the salient recent case rather than case-specific evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.",
          "evidence_explanation": "This quote demonstrates that a recent, easily recalled case became the initial comparison point for a new ambiguous case."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed.",
          "evidence_explanation": "This quote directly demonstrates that vividness and recency influenced the reasoning process, reducing case-specific evidence review."
        }
      ],
      "correction_or_counterevidence": "The PI later asked the participant to pull the full lab history and prior meds before finalizing. The participant acknowledged that this should have been done up front. This does not erase the initial bias but did create a later verification step.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage was provided in the RAG context; this classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "ambiguity aversion",
      "alternative_labels": [
        "need for closure",
        "ambiguity effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Preference for a definitive or unambiguous option over an ambiguous one, even when the available evidence more strongly supports the ambiguous option.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 12 ALT causality classification",
      "decision_point_description": "Deciding between the 'possibly related' category, which the participant acknowledged best fit the data, and the more definitive 'unrelated' category.",
      "affected_reasoning_operation": "classification under uncertainty / handling of ambiguous evidence",
      "bias_specific_mechanism": "The participant experienced the ambiguous 'possibly related' category as burdensome because it implied follow-up and open paperwork, and this desire for closure pushed him toward a definitive 'unrelated' classification.",
      "manifestation_in_interview": "The participant explicitly stated that the ambiguous category would generate more work and that he wanted something he could close out.",
      "effect_on_reasoning_or_decision": "The participant selected a definitive category partly to avoid the discomfort and administrative burden of ambiguity, even though he acknowledged the ambiguous category best matched the data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.",
          "evidence_explanation": "This quote shows that avoidance of ambiguity and follow-up work drove the selection of a definitive category rather than the data-supported ambiguous category."
        }
      ],
      "correction_or_counterevidence": "A plausible competing explanation is that the participant was under workload pressure and may have been using a pragmatic triage approach. However, because he admitted the data best supported 'possibly related' and still chose 'unrelated' to achieve closure, the motivational distortion is affirmative. The PI's later request for additional records provided a check on the chosen classification.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage was provided in the RAG context; this classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Continuing an endeavor because of previously invested resources, even when those resources cannot be recovered and should not influence the forward-looking decision.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 case report form reconciliation discrepancy",
      "decision_point_description": "Deciding whether to continue reconciliation, flag the discrepancy as a deviation, or obtain a second reviewer after a major dosing-record discrepancy emerged.",
      "affected_reasoning_operation": "continued investment decision / escalation of commitment",
      "bias_specific_mechanism": "The participant treated the already-invested twenty hours as a reason to continue working, even though those hours were irrecoverable and should not have determined the forward-looking decision.",
      "manifestation_in_interview": "The participant said the twenty hours felt too large to walk away from and that stopping felt like wasting everything already done.",
      "effect_on_reasoning_or_decision": "The participant committed additional hours to reconciliation rather than immediately flagging or seeking review, and the additional effort did not change the eventual outcome.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Twenty hours felt like too much to walk away from without one more push.",
          "evidence_explanation": "This quote directly evidences sunk cost reasoning: past irrecoverable time was used as a reason for continued investment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.",
          "evidence_explanation": "This quote shows that avoiding perceived waste of prior effort influenced the decision to continue."
        }
      ],
      "correction_or_counterevidence": "There was also a legitimate trial-integrity reason to investigate the discrepancy. However, the participant's own account identifies the prior time investment as a driver. The discrepancy was ultimately unresolvable and was flagged later, so the extra effort did not change the outcome.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage was provided in the RAG context; this classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "framing effect",
      "alternative_labels": [
        "loss aversion",
        "prospect theory framing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Choices are influenced by whether outcomes are presented as losses or gains, with loss-framed outcomes typically having greater psychological impact.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 case report form reconciliation discrepancy",
      "decision_point_description": "Interpreting the Site Director's email and deciding whether continued reconciliation was justified or whether the work should be flagged as a deviation.",
      "affected_reasoning_operation": "evaluation of decision alternatives / risk and effort allocation",
      "bias_specific_mechanism": "The Site Director's message framed continued effort in terms of losing a fifth of the evaluable per-protocol population rather than as a neutral evaluation of whether further work was worth the time. The participant internalized this loss frame, making continued effort feel heavier and more necessary.",
      "manifestation_in_interview": "The participant said the loss framing stuck with him and that it changed the decision from being about hours to being about what would be given up.",
      "effect_on_reasoning_or_decision": "The loss-framed presentation contributed to the participant continuing reconciliation for additional hours instead of stopping or escalating earlier.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that.",
          "evidence_explanation": "This quote documents that the decision was presented with a loss framing rather than a neutral framing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up.",
          "evidence_explanation": "This quote shows that the participant's reasoning was directly affected by the loss-framed presentation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Framed as a loss, it felt heavier than it maybe should have.",
          "evidence_explanation": "This retrospective statement explicitly identifies the loss frame as a distortion in the participant's evaluation."
        }
      ],
      "correction_or_counterevidence": "The participant later reflected that a neutral framing might have led to stopping sooner. There is no evidence of contemporaneous correction, though the continued work did not resolve the discrepancy.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage was provided in the RAG context; this classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "prototype bias",
        "base-rate neglect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging probability or category membership by how much an individual resembles a typical or prototypical member of a category, while underweighting objective criteria or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Screening prioritization for new Wednesday referral",
      "decision_point_description": "Deciding how to prioritize a new referral for screening against other lock-week tasks.",
      "affected_reasoning_operation": "eligibility judgment / screening queue prioritization",
      "bias_specific_mechanism": "The participant judged the referral's likely eligibility based on resemblance to the typical enrolled patient prototype rather than the objective inclusion and exclusion criteria.",
      "manifestation_in_interview": "The participant stated that the referral did not match the usual patient pattern and therefore was initially assumed unlikely to be a good fit.",
      "effect_on_reasoning_or_decision": "The referral was deprioritized in the screening queue based on a prototype mismatch rather than objective eligibility criteria.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him.",
          "evidence_explanation": "This quote shows that the initial eligibility judgment was based on resemblance to a typical patient rather than objective criteria."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.",
          "evidence_explanation": "This direct admission confirms that the reasoning relied on representativeness rather than the formal eligibility criteria."
        }
      ],
      "correction_or_counterevidence": "When screened, the referral met every inclusion criterion. The participant noted that this did not necessarily prove the deprioritization wrong but acknowledged the judgment was not evidence-based.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage was provided in the RAG context; this classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "bandwagon effect",
      "alternative_labels": [
        "social proof",
        "herd behavior"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Adopting a belief or behavior because many others have adopted it, often without independent evaluation of the underlying evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Source data verification method change ahead of lock",
      "decision_point_description": "Deciding whether to switch from the site's established source data verification approach to a quicker method mentioned by other sites.",
      "affected_reasoning_operation": "procedure change / validation adoption decision",
      "bias_specific_mechanism": "The participant used the number of other sites that had already switched as a substitute for validation data, despite having no error-rate information and despite the current method's clean audit history.",
      "manifestation_in_interview": "The participant said that hearing most other sites had moved made staying with the old method feel like being behind and prompted a switch without seeking validating data.",
      "effect_on_reasoning_or_decision": "The site switched verification methods without documented rationale, and the monitor later questioned the change.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
          "evidence_explanation": "This quote directly demonstrates social-proof-based adoption without independent validation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have a great answer beyond 'everyone else was doing it too.'",
          "evidence_explanation": "This admission confirms that the primary rationale was the behavior of others rather than data."
        }
      ],
      "correction_or_counterevidence": "The monitor subsequently asked for a documented rationale. The participant had no evidentiary rationale, and there was no prior problem with the existing method other than speed.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage was provided in the RAG context; this classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied with the interview transcript; corpus support is therefore marked unavailable for all occurrences.",
    "Findings are based on self-reported retrospective accounts, which may be incomplete or subject to memory and self-presentation effects.",
    "Confidence levels reflect transcript evidence only and do not incorporate objective outcome data or independent observation of the decisions."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HC_Biased_6_Gemini_off",
  "interview_id": "HC_Biased_6",
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
