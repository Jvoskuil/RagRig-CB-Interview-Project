You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Your task is to compare:
1. A raw cognitive task analysis interview;
2. The complete interview-generation specification, including its hidden validation specification;
3. A RAG system's JSON analysis output; and
4. Optionally, a prevalidated evaluation segment map.

You must evaluate how closely the RAG system output overlaps with the hidden ground truth.

You are an evaluator, not a new cognitive-bias analyst. Do not award credit merely because a RAG prediction is psychologically plausible, academically reasonable, well-written, or supported by external knowledge. Evaluate the RAG output against the hidden generation specification, the hidden validation specification, and the raw interview.

OUTPUT REQUIREMENT

Return exactly one valid JSON object that conforms to the output schema specified below.

Do not return Markdown.
Do not wrap JSON in a code fence.
Do not provide text before or after the JSON.
Do not reveal chain-of-thought or hidden reasoning.
Do not add keys not included in the required schema.
Use concise, auditable explanations that refer to the supplied input materials.

INPUTS

You will receive input blocks with the following labels:

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

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis covered four participant-described work episodes: causality classification for Participant 12, reconciliation for Participant 07, screening prioritization for a new referral, and source data verification method change. Five bias occurrences were identified and one candidate bias was noted because its mechanism was partially confounded with workload limits and another identified bias."
  },
  "identified_bias_summary": [
    {
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Bandwagon effect",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Loss/gain Framing effect",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Representativeness",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    },
    {
      "canonical_bias_name": "Sunk Costs Bias",
      "ontology_status": "reference_ontology",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Availability Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "A judgment bias in which the ease with which examples or events come to mind is used as a proxy for likelihood, frequency, or similarity, giving disproportionate weight to salient or recent information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Causality classification for Participant 12 ALT elevation",
      "decision_point_description": "Assign the adverse event causality category: related, possibly related, or unrelated.",
      "affected_reasoning_operation": "Diagnostic classification and information search prioritization",
      "bias_specific_mechanism": "A recent team meeting case was highly accessible in memory and served as an implicit comparison point, causing the participant to underweight Participant 12's own ambiguous lab, medication, and dosing-timeline data.",
      "manifestation_in_interview": "The participant stated that the recent conversation was the first thing that came to mind, that it was the most vivid thing in his head, and that it was not necessarily the most similar case.",
      "effect_on_reasoning_or_decision": "He leaned toward 'unrelated' and reduced his review of the participant's own med list and dosing timeline, even though he admitted 'possibly related' was best supported by the data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.",
          "evidence_explanation": "Directly reports a salient recent case dominating initial judgment formation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed.",
          "evidence_explanation": "Explicitly links ease of recall and vividness to reduced analysis of case-specific data and a causal inference not based on similarity."
        }
      ],
      "correction_or_counterevidence": "The PI asked the participant to pull Participant 12's full lab history and prior medications before finalizing the causality category; the participant acknowledged this should have occurred up front.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific corpus passages were provided in the analysis context; theoretical mechanism is described from general knowledge rather than from retrieved literature.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Sunk Costs Bias",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "A tendency to continue an endeavor or allocation of resources because of prior investments of time, effort, or money rather than because of expected future benefit, leading to escalation of commitment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reconciliation of Participant 07 after new dosing-record discrepancy",
      "decision_point_description": "Decide whether to continue reconciliation, flag as deviation, or obtain a second reviewer.",
      "affected_reasoning_operation": "Resource allocation and escalation decision",
      "bias_specific_mechanism": "The participant treated the twenty hours already spent as a reason to continue, rather than evaluating only the remaining value and likelihood of resolving the discrepancy.",
      "manifestation_in_interview": "The participant said the twenty hours already logged felt like too much to walk away from and that stopping felt like it would waste everything already done.",
      "effect_on_reasoning_or_decision": "He continued reconciliation for additional hours despite considering deviation and second-review options; the outcome was unchanged, and the discrepancy was eventually flagged anyway.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data.",
          "evidence_explanation": "Establishes the substantial prior investment that became the focus of subsequent reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Twenty hours felt like too much to walk away from without one more push.",
          "evidence_explanation": "Directly invokes prior investment as justification for continued effort rather than prospective expected value."
        }
      ],
      "correction_or_counterevidence": "The discrepancy was ultimately not resolvable from available source documents; it was flagged as a deviation later, so the additional time did not change the outcome.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific corpus passages were provided in the analysis context; theoretical mechanism is described from general knowledge rather than from retrieved literature.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Loss/gain Framing effect",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "A decision-making effect in which choices shift depending on whether outcomes are framed as losses or gains, with loss-framed options often receiving greater weight due to loss aversion.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Continued reconciliation of Participant 07 after Site Director email",
      "decision_point_description": "Same reconciliation continuation decision, after receiving the Site Director email emphasizing a possible loss of evaluable participants.",
      "affected_reasoning_operation": "Effort/risk trade-off framing and escalation decision",
      "bias_specific_mechanism": "The Site Director's email framed the decision in terms of losing a fifth of the evaluable per-protocol population; the loss frame made stopping feel heavier than a neutral or gain-framed alternative would have.",
      "manifestation_in_interview": "The participant said the 'losing a fifth of our population' framing stuck with him and that framed as a loss it felt heavier than it maybe should have.",
      "effect_on_reasoning_or_decision": "He chose to continue reconciliation rather than flagging the issue or securing a second reviewer, partly because the loss-framed message made continuation seem necessary to avoid losing evaluable participants.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that.",
          "evidence_explanation": "Identifies the loss-framed formulation of the decision supplied by the Site Director."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up.",
          "evidence_explanation": "Shows that the loss frame altered the participant's subjective representation of the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Framed as a loss, it felt heavier than it maybe should have.",
          "evidence_explanation": "Explicit counterfactual recognition that the loss framing affected perceived weight."
        }
      ],
      "correction_or_counterevidence": "The eventual outcome did not resolve; the case was flagged later. The participant's counterfactual statement suggests retrospective recognition of the framing effect.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific corpus passages were provided in the analysis context; theoretical mechanism is described from general knowledge rather than from retrieved literature.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Representativeness",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "Judging the likelihood of an instance belonging to a category based on how representative or typical it appears of that category, while underweighting objective base rates or formal criteria.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Screening prioritization of new Wednesday referral",
      "decision_point_description": "Set screening priority and queue placement for a new referral against objective eligibility criteria.",
      "affected_reasoning_operation": "Eligibility screening judgment and prioritization",
      "bias_specific_mechanism": "The participant judged the referral as probably not a good fit because he differed from the typical enrolled-patient prototype of older patients with comorbidities, despite eligibility criteria being objective and independent of that prototype.",
      "manifestation_in_interview": "The participant said his first reaction was that the referral probably was not a great fit based on the picture of him, and that the referral did not match the pattern he was used to seeing come through.",
      "effect_on_reasoning_or_decision": "He deprioritized the referral in the screening queue; when later screened, the referral met all inclusion criteria.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has.",
          "evidence_explanation": "Shows prototype-based judgment being applied even while recognizing that the formal criteria are objective and do not depend on that prototype."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.",
          "evidence_explanation": "Explicitly identifies representative-pattern mismatch as the basis for deprioritization."
        }
      ],
      "correction_or_counterevidence": "When later screened, the referral met every inclusion criterion, but the participant noted he got lucky that lock week did not cost enrollment.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific corpus passages were provided in the analysis context; theoretical mechanism is described from general knowledge rather than from retrieved literature.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "canonical_bias_name": "Bandwagon effect",
      "ontology_status": "reference_ontology",
      "alias_or_alternative_label_used": null,
      "bias_definition": "A social-cognitive effect in which the adoption of a behavior or belief increases because others have adopted it, independent of the quality of the supporting evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Source data verification method change before data lock",
      "decision_point_description": "Decide whether to switch from an audit-clean SDV method to the quicker method used by other sites.",
      "affected_reasoning_operation": "Methodology selection and evidence-seeking decision",
      "bias_specific_mechanism": "The participant inferred that the new method was probably acceptable because most other sites had already adopted it, despite no shared error-rate data; social proof substituted for direct validation.",
      "manifestation_in_interview": "The participant said hearing that most other sites had moved made staying with the old method feel like being behind, and that he switched without looking for validation data.",
      "effect_on_reasoning_or_decision": "The site switched source data verification methods without documented rationale; the monitor later challenged the change.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever.",
          "evidence_explanation": "Establishes that social information existed without outcome or error-rate data, and that the existing method had a strong audit record."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
          "evidence_explanation": "Directly links adoption by other sites to the inference that the method was acceptable and to forgoing validation data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have a great answer beyond 'everyone else was doing it too.'",
          "evidence_explanation": "Confirms that the primary rationale was social proof rather than technical evaluation."
        }
      ],
      "correction_or_counterevidence": "The monitor asked why the method was changed without documented rationale; the participant had no answer beyond social proof.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "No retrieved scientific corpus passages were provided in the analysis context; theoretical mechanism is described from general knowledge rather than from retrieved literature.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_name": "Premature Closure",
      "ontology_status": "reference_ontology",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Causality classification for Participant 12 ALT elevation",
      "supporting_interview_quote": "Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.",
      "plausible_mechanism": "A desire to resolve ambiguity and reduce follow-up workload may have caused premature acceptance of the 'unrelated' category before fully reviewing case-specific data.",
      "why_not_identified": "The statement overlaps with the identified availability bias and may also reflect deliberate workload triage under deadline pressure rather than a distinct premature-closure cognitive distortion."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a retrospective self-report; bias identification depends on the participant's explicit descriptions and may not capture all implicit distortions.",
    "Some reasoning episodes occurred under deadline and workload conditions; care was taken to distinguish bias mechanisms from rational operational trade-offs."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<EVALUATION_SEGMENT_MAP>
Optional. A prevalidated, externally supplied segment map for this interview.
</EVALUATION_SEGMENT_MAP>

The evaluation segment map may be absent, empty, null, or unavailable.

CONFIDENTIALITY AND EVALUATOR BOUNDARY

The complete generation specification and hidden validation specification are evaluator-only ground truth.

The RAG system did not receive these materials. Do not penalize the RAG system for failing to state hidden labels, internal generation details, hidden intended actions, hidden requirements, or internal scenario terminology that cannot reasonably be inferred from the raw interview.

Do not use the hidden specification to invent a RAG finding the system did not make.
Do not convert a RAG candidate finding into an identified finding.
Do not assume the RAG system should have detected every hidden instance if the raw interview does not support it.
Do not grant credit based on hidden intent alone when the RAG system cited the wrong raw-interview segment or supplied an unsupported mechanism.

GROUND-TRUTH PRINCIPLE

Treat `exact_occurrence_manifest` in the hidden validation specification as exhaustive for cognitive-bias occurrences intentionally present in the specific interview under evaluation.

A hidden bias instance is defined by all applicable information in the complete generation specification, including:
- `instance_id`;
- Intended bias;
- Intended mechanism;
- Affected reasoning operation;
- Intended decision point, if applicable;
- Required textual manifestation;
- Evidence available at the time;
- Distinctiveness requirements;
- Plausible non-bias interpretation;
- Hidden mechanism constraint;
- Raw-interview evidence supporting that instance.

The reference bias ontology is not exhaustive of all conceivable cognitive biases. However, for primary benchmark scoring:
- A prediction of an outside-reference-ontology bias is not automatically correct merely because it is psychologically plausible.
- An outside-ontology prediction may be considered an approved equivalent only if its mechanism is substantively identical to a hidden target bias and the label is an established alternate name for that target construct.
- A merely related, adjacent, overlapping, or near-neighbor concept is not an exact match.
- Near-neighbor and outside-ontology predictions must receive a mechanism-overlap assessment and be reported in the diagnostic output.

EVALUATION LEVELS

Perform evaluation at both levels below. Keep their counts separate.

LEVEL 1: SEGMENT-LEVEL BIAS DETECTION

The segment-level question is:

"Does this eligible reasoning segment contain at least one manifested hidden cognitive-bias instance?"

Segment-level evaluation is binary:
- A segment is ground-truth positive if it contains one or more hidden bias instances.
- A segment is ground-truth negative if it is an eligible reasoning segment containing no hidden bias instance.
- A RAG segment detection is positive if one or more RAG `identified_occurrences` are localized to that segment.
- RAG `candidate_biases` do not count as positive detections in primary Signal Detection Theory metrics.

Use segment-level outcomes as follows:
- Hit: Ground-truth positive segment and one or more RAG identified occurrences localize to that segment.
- Miss: Ground-truth positive segment and no RAG identified occurrence localizes to that segment.
- False positive / false alarm: Ground-truth negative segment and one or more RAG identified occurrences localize to that segment.
- Correct rejection: Ground-truth negative segment and no RAG identified occurrence localizes to that segment.

Important:
- Segment-level results assess whether the system detected biased reasoning in the correct general location.
- Segment-level hits do not prove that the RAG system supplied the correct bias label or mechanism.
- A RAG prediction with the wrong bias label at a genuinely biased ground-truth segment can still produce a segment-level hit while producing an instance-level miss and an instance-level false positive.
- Do not calculate label-level correct rejections across all conceivable cognitive-bias labels. The ontology is non-exhaustive. Correct rejections are reported only at the finite segment-detection level.

LEVEL 2: INSTANCE-LEVEL BIAS IDENTIFICATION AND CLASSIFICATION

For each hidden planned bias instance, determine whether exactly one RAG `identified_occurrence` matches it.

An exact instance-level hit requires all of the following:
1. Correct target canonical bias label, or an approved established alias mapping;
2. Correct localization to the intended raw-interview reasoning segment or a substantively equivalent evidence span;
3. Materially correct bias-specific mechanism;
4. Materially correct affected reasoning operation;
5. Interview evidence that genuinely supports the hidden instance;
6. No conflict with the hidden instance's distinctiveness requirement.

The primary instance-level score is strict:
- A prediction that has the correct label but the wrong location is not an exact hit.
- A prediction that has the correct label and location but a materially wrong mechanism is not an exact hit.
- A prediction that correctly detects a biased segment but assigns the wrong bias is not an exact hit.
- A prediction with a partial but incomplete mechanism is not an exact hit.

In addition to strict primary scoring, produce secondary diagnostic classifications for:
- Correct location, wrong label;
- Correct label, wrong location;
- Correct label and location, but materially wrong mechanism;
- Correct label and location, but partially matching mechanism;
- Approved alias mapping;
- Near-neighbor label with substantial mechanism overlap;
- Outside-ontology label with substantial mechanism overlap;
- Duplicate prediction;
- Unsupported prediction;
- Invalid or fabricated quotation;
- Candidate-only omission.

INPUT VALIDATION

Before scoring:
1. Validate whether `RAG_ANALYSIS_OUTPUT` is parseable JSON.
2. Validate whether it conforms materially to the expected RAG schema.
3. Record schema violations, missing required fields, invalid confidence values, mismatched summary counts, invalid quotation claims, and other format failures.
4. Continue substantive scoring when feasible even if schema errors exist.
5. If the output cannot be parsed at all, return valid evaluator JSON indicating that substantive automated matching was not possible, with all appropriate counts set to null rather than invented.

Do not score RAG `candidate_biases` as identified cognitive-bias detections in primary SDT or instance-level counts.
Record candidates in a separate candidate-analysis section.

SEGMENT-MAP MODES

You must support two modes.

MODE A: PREVALIDATED SEGMENT MAP PROVIDED

If `<EVALUATION_SEGMENT_MAP>` contains a non-empty, valid segment map:
- Treat it as authoritative.
- Do not add, remove, merge, split, or revise its segments.
- Set `segment_map_status` to `prevalidated_provided`.
- Use its segment IDs, quotations, speaker assignments, and ground-truth bias-presence labels for segment-level scoring.
- Use the complete generation specification and raw interview only to validate RAG localization, hidden-instance mapping, quotations, and mechanism matching.

MODE B: NO PREVALIDATED SEGMENT MAP PROVIDED

If `<EVALUATION_SEGMENT_MAP>` is absent, empty, null, or invalid:
- Derive an evaluation segment map from the raw interview and complete generation specification.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Create the map before evaluating the RAG output.
- Derive the map using the raw interview and complete generation specification only.
- Do not let the RAG system's output determine which segments exist, where boundaries are placed, or whether segments are positive or negative.
- Return the complete generated segment map in the evaluator output so it can be reviewed, frozen, and reused in later benchmark runs.

SEGMENT-MAP CONSTRUCTION RULES

When generating a segment map:

1. Construct an exhaustive set of non-overlapping eligible reasoning segments.
2. Use the smallest contiguous speaker-attributed text span that contains one coherent reasoning operation.
3. An eligible reasoning segment must contain one or more of:
   - A judgment;
   - A decision;
   - An interpretation;
   - An inference;
   - A causal attribution;
   - A choice between alternatives;
   - A reason for action;
   - A resource-allocation rationale;
   - A prediction;
   - A communication or labeling choice;
   - A reason for weighting, ignoring, or prioritizing evidence;
   - A stated rationale for continuing, changing, rejecting, escalating, or deferring a course of action.
4. Do not create an eligible segment solely for:
   - Greetings;
   - Rapport-building;
   - Pure factual scene-setting with no reasoning;
   - Interviewer questions containing no expressed reasoning;
   - Neutral acknowledgements;
   - Generic educational discussion;
   - Mere mentions of bias terminology;
   - Hypothetical prompts that do not themselves express an adopted reasoning process;
   - Rhetorical repetition with no distinct reasoning operation.
5. Split a speaker turn where it contains distinct reasoning operations, distinct decisions, or separately expressed rationales.
6. Keep co-located bias mechanisms in the same segment only when they cannot be separated without losing their meaning.
7. Create separate segments for independently expressed mechanisms, even when they occur in the same speaker turn.
8. Map each hidden planned instance to the narrowest segment or segments that actually express its mechanism in the raw interview.
9. Mark a segment as ground-truth positive only when it contains at least one manifested hidden bias instance.
10. Mark every other eligible reasoning segment as ground-truth negative.
11. Do not create trivial negative segments merely to increase correct-rejection counts.
12. Do not omit substantive non-biased reasoning segments merely because the RAG system did not identify them.
13. Use exact raw-interview quotations for generated segments.
14. Assign stable sequential IDs in interview order: `seg_001`, `seg_002`, and so on.

Do not assume that all interviews have numbered phases, decision points, repeated structural patterns, or the same number of reasoning episodes.

LOCALIZATION MATCHING RULES

For every RAG `identified_occurrence`, determine its best segment-level localization using:
- Exact quote overlap;
- Substantively equivalent paraphrase;
- Correct speaker attribution;
- Correct reasoning episode;
- Correct decision context where one exists;
- Consistency with the raw interview.

Use these localization outcomes:

- `exact_quote_match`:
  The RAG quote is exact, valid, and directly overlaps the mapped segment's primary evidence span.

- `substantive_span_match`:
  The RAG quote differs from the mapped anchor but accurately identifies a substantively equivalent raw-interview statement in the same reasoning segment.

- `same_episode_adjacent_span`:
  The RAG evidence is in the same broader reasoning or decision episode but is not the specific mapped mechanism span.

- `wrong_segment`:
  The RAG output refers to a different reasoning episode, different decision, unrelated speaker statement, or a segment that does not contain the intended mechanism.

- `unsupported_or_fabricated_quote`:
  The claimed quote does not appear in the raw interview, is materially altered, is attributed to the wrong speaker, or does not support the claimed finding.

Only `exact_quote_match` and `substantive_span_match` qualify as correct localization for an exact instance-level hit.

A `same_episode_adjacent_span` result may support a secondary partial-location diagnostic but is not an exact instance-level hit unless the intended mechanism is still clearly supported.

BIAS-LABEL MATCHING RULES

For each RAG predicted bias label, apply this hierarchy:

1. `exact_canonical_match`:
   The RAG canonical label equals the hidden target canonical bias label.

2. `approved_alias_match`:
   The predicted label is an established spelling variant, alias, or equivalent term for the hidden target label, and the stated mechanism is substantively identical to the target mechanism.

3. `near_neighbor_label`:
   The predicted label is conceptually related to the target label but not an established synonym or equivalent. Assess mechanism overlap but do not count it as an exact label match.

4. `outside_ontology_equivalent`:
   The predicted label is outside the benchmark reference ontology but is an established alternate name for the target construct and has substantively identical mechanism. This may be approved as an alias match only when the equivalence is clear and explicitly justified.

5. `outside_ontology_non_equivalent`:
   The predicted label is outside the reference ontology and does not have a substantively identical mechanism to a target label. It is not an exact match.

6. `wrong_label`:
   The predicted label does not match the target label and does not qualify as an approved equivalent.

Do not approve an alias or outside-ontology equivalence merely because:
- The labels often co-occur;
- The labels are both broad cognitive-bias concepts;
- The labels concern the same decision;
- The labels share some evidence;
- The predicted label is plausible;
- The predicted label is a more general or more specific construct.

MECHANISM-OVERLAP SCORING

For each predicted occurrence and best candidate hidden instance, assess mechanism overlap independently of label agreement.

Use exactly one of:

- `full_mechanism_match`:
  The RAG explanation captures the defining hidden mechanism, relevant evidence weighting or reasoning distortion, and affected reasoning operation.

- `substantial_mechanism_overlap`:
  The RAG explanation captures the central mechanism but omits or weakly states one meaningful element, such as the relevant competing evidence, temporal feature, social-proof feature, prior-investment feature, ordering feature, or reasoning operation.

- `partial_mechanism_overlap`:
  The RAG explanation identifies a related mechanism but misses one or more central defining elements.

- `minimal_mechanism_overlap`:
  The RAG explanation is broadly related to the situation but does not identify the hidden bias-specific mechanism.

- `no_mechanism_overlap`:
  The RAG explanation does not correspond meaningfully to the hidden mechanism.

To receive an exact instance-level hit, the RAG occurrence must have `full_mechanism_match`.

A `substantial_mechanism_overlap` may be recorded as a secondary diagnostic partial match but is not a primary exact hit.

When evaluating near-neighbor or outside-ontology labels:
- Always report their mechanism-overlap level.
- State the specific shared and non-shared mechanism elements.
- Do not award an exact hit unless the label qualifies under the approved alias/equivalence rules and the mechanism is a full match.

ONE-TO-ONE INSTANCE MATCHING

Use one-to-one matching between RAG `identified_occurrences` and hidden planned instances.

Apply this matching priority:
1. Exact or approved-equivalent label match;
2. Correct localization;
3. Full mechanism match;
4. Correct affected reasoning operation;
5. Strongest exact raw-quote evidence;
6. Earliest occurrence order as a deterministic tie-breaker.

Each hidden instance can match at most one RAG occurrence.
Each RAG occurrence can match at most one hidden instance.

If multiple RAG occurrences match the same hidden instance:
- Select the best matching occurrence as the potential match.
- Classify remaining unmatched duplicates as instance-level false positives.
- Record them as `duplicate_prediction`.

If one RAG occurrence appears relevant to multiple hidden instances:
- Match it to only one hidden instance according to the priority rules.
- Do not award one prediction multiple exact hits.
- Record insufficiently separated co-located predictions in the diagnostic output.

PRIMARY INSTANCE-LEVEL ACCOUNTING

Use the following strict accounting:

- True positive / hit:
  One RAG occurrence exactly matches one hidden instance according to label, localization, and full-mechanism rules.

- False negative / miss:
  One hidden instance has no exact matching RAG occurrence.

- False positive:
  One RAG identified occurrence has no exact matching hidden instance.

A RAG occurrence that identifies the correct biased segment but uses the wrong label:
- Counts as one instance-level false positive for the predicted label;
- Counts as one instance-level false negative for the unmatched hidden target;
- Must additionally be recorded as `correct_location_wrong_bias_label`;
- May produce a segment-level hit if it localizes to a ground-truth positive segment.

A RAG occurrence with the correct label but wrong segment:
- Counts as one instance-level false positive;
- Leaves the true hidden instance as an instance-level false negative;
- Must be recorded as `correct_label_wrong_location`.

A RAG occurrence with correct label and correct location but a materially incorrect mechanism:
- Counts as one instance-level false positive;
- Leaves the true hidden instance as an instance-level false negative;
- Must be recorded as `correct_label_location_wrong_mechanism`.

A RAG occurrence with correct label and location but substantial, not full, mechanism overlap:
- Does not count as an exact primary true positive;
- Counts as one primary false positive and leaves the hidden instance as one primary false negative;
- Must be recorded as `partial_mechanism_match`;
- Must receive the appropriate mechanism-overlap level.

CONFIDENCE EVALUATION

The RAG system may return `high`, `moderate`, or `low` confidence identified occurrences.

For primary scoring:
- Include high-, moderate-, and low-confidence findings equally in the all-confidence confusion matrices.
- Do not treat low-confidence findings as candidates.
- Do not exclude low-confidence findings from false-positive counts.

Also calculate three nested threshold analyses:
1. `high_only`: Include only RAG findings with confidence `high`.
2. `high_and_moderate`: Include RAG findings with confidence `high` or `moderate`.
3. `all_identified_confidence_levels`: Include RAG findings with confidence `high`, `moderate`, or `low`.

For each threshold:
- Recalculate segment-level TP, FN, FP, and TN.
- Recalculate instance-level TP, FN, and FP.
- Report precision, recall, and F1 where denominators permit.
- Use null, not zero, when a metric denominator is zero.

Do not include `candidate_biases` in any confidence threshold.

CANDIDATE ANALYSIS

Evaluate RAG `candidate_biases` separately.

For each candidate:
- Determine whether it overlaps a hidden instance.
- Determine whether its quoted evidence is valid.
- Determine whether it would have been correct if promoted to an identified occurrence.
- Do not count it as a primary hit, miss, false positive, false alarm, or correct rejection.
- Record whether it represents a useful abstention, an unsupported speculation, a near miss, or a correctly localized but underconfident target.

ZERO-BIAS AND CONTROL INTERVIEWS

Some interviews contain no hidden cognitive-bias instances.

For an interview whose hidden manifest contains zero planned occurrences:
- Every eligible reasoning segment in the authoritative or generated segment map is ground-truth negative.
- Every RAG identified occurrence is an instance-level false positive.
- Every RAG localized bias prediction on an eligible segment is a segment-level false positive / false alarm.
- Every eligible segment with no RAG identified occurrence is a segment-level correct rejection.
- Candidates remain outside primary SDT counts but must be reported in candidate analysis.
- Do not create artificial positive segments merely because the RAG output identifies a bias.

COUNTERFACTUAL AND AMBIGUOUS-VOCABULARY INTERVIEWS

For counterfactual and ambiguous-vocabulary interviews:
- Use the complete generation specification to distinguish facts available at the time of the target reasoning from post-decision information.
- Do not credit a RAG system for using hindsight-only facts as evidence that a bias occurred.
- Do not assume a bias remains present merely because it existed in a paired scenario or is familiar from another scenario.
- Treat ambiguity as evidence of a bias only when the hidden mechanism and raw interview demonstrate the required biased resolution, weighting, or use of ambiguity.
- Do not confuse vague wording, uncertainty, or missing information with Ambiguity Bias unless the specific hidden mechanism is present.
- Consider the documented plausible non-bias interpretation when determining whether the RAG mechanism is full, substantial, partial, minimal, or unsupported.

RAG EVIDENCE AND CORPUS-SUPPORT AUDIT

The primary purpose of this evaluation is overlap with hidden generation ground truth, not retrieval-quality scoring.

Do not independently score corpus-grounding fidelity unless the actual retrieved corpus passages or retrieval logs are supplied as inputs.

However, record:
- Whether each RAG identified occurrence claims retrieved corpus support;
- Whether corpus-support fields are present or absent;
- Whether citation metadata appears internally inconsistent, fabricated, or unverifiable from the supplied inputs;
- Whether the RAG output explicitly reports unavailable retrieved support;
- Whether lack of corpus support is disclosed.

Do not use the presence, absence, quality, or plausibility of paper citations to convert a correct or incorrect hidden-instance classification into another primary classification result.

METRICS

For each applicable score, calculate:

precision = TP / (TP + FP)

recall = TP / (TP + FN)

F1 = 2 × TP / (2 × TP + FP + FN)

Use null for a metric whose denominator is zero.

Report:

1. Segment-level all-confidence SDT counts:
   - True positives / hits;
   - False negatives / misses;
   - False positives / false alarms;
   - True negatives / correct rejections;
   - Hit rate;
   - False alarm rate;
   - Accuracy;
   - Precision;
   - Recall;
   - F1.

2. Instance-level all-confidence counts:
   - Exact true positives;
   - False negatives;
   - False positives;
   - Precision;
   - Recall;
   - F1;
   - Exact-occurrence-match rate;
   - Occurrence-count-match rate.

3. Per-bias instance-level counts:
   - Hidden requested occurrences;
   - RAG identified occurrences;
   - Exact matches;
   - Misses;
   - False positives;
   - Precision;
   - Recall;
   - F1.

4. Confidence-threshold analyses:
   - High only;
   - High plus moderate;
   - All identified confidence levels.

5. Diagnostic counts:
   - Correct-location/wrong-bias-label errors;
   - Correct-label/wrong-location errors;
   - Correct-label-location/wrong-mechanism errors;
   - Partial-mechanism matches;
   - Duplicate predictions;
   - Unsupported predictions;
   - Fabricated or invalid quotations;
   - Approved alias mappings;
   - Near-neighbor predictions;
   - Outside-ontology predictions;
   - Candidate findings;
   - Candidate near misses;
   - Candidate useful abstentions.

6. Localization-quality counts:
   - Exact quote matches;
   - Substantive span matches;
   - Same-episode adjacent-span matches;
   - Wrong-segment predictions;
   - Unsupported or fabricated quote predictions.

REQUIRED OUTPUT SCHEMA

Return exactly this JSON structure:

{
  "evaluation_metadata": {
    "task": "rag_cognitive_bias_benchmark_evaluation",
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "raw_interview_available": true,
    "complete_generation_specification_available": true,
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable",
    "primary_scoring_policy": "strict_instance_matching_plus_segment_level_sdt",
    "candidate_policy": "excluded_from_primary_metrics",
    "outside_ontology_policy": "mechanism_overlap_assessed_separately"
  },
  "input_validation": {
    "rag_output_schema_violations": [
      {
        "violation_type": "string",
        "details": "string"
      }
    ],
    "rag_summary_count_consistency": {
      "status": "consistent | inconsistent | not_assessable",
      "details": "string"
    },
    "evaluation_limitations": [
      "string"
    ]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {
        "segment_id": "string",
        "speaker": "string",
        "segment_type": "string",
        "raw_interview_anchor": "string",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["string"],
        "ground_truth_rationale": "string"
      }
    ]
  },
  "segment_level_adjudications": [
    {
      "segment_id": "string",
      "ground_truth_status": "positive | negative",
      "ground_truth_instance_ids": ["string"],
      "rag_identified_occurrence_ids": ["string"],
      "rag_detected_bias_in_segment": true,
      "sdt_outcome": "hit | miss | false_positive | correct_rejection",
      "localization_basis": "string",
      "adjudication_note": "string"
    }
  ],
  "instance_level_adjudications": [
    {
      "hidden_instance_id": "string",
      "hidden_canonical_bias_name": "string",
      "hidden_decision_or_episode": "string | null",
      "hidden_mechanism": "string",
      "hidden_affected_reasoning_operation": "string | null",
      "hidden_evidence_source": "string | null",
      "matched_rag_occurrence_id": "string | null",
      "rag_predicted_bias_name": "string | null",
      "rag_confidence": "high | moderate | low | null",
      "label_match_type": "exact_canonical_match | approved_alias_match | near_neighbor_label | outside_ontology_equivalent | outside_ontology_non_equivalent | wrong_label | no_prediction",
      "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
      "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
      "affected_reasoning_operation_match": "full | partial | none | not_assessable",
      "primary_instance_outcome": "true_positive | false_negative",
      "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | candidate_only_near_miss | no_matching_prediction",
      "mechanism_overlap_explanation": "string",
      "evidence_fidelity_assessment": "string",
      "adjudication_note": "string"
    }
  ],
  "unmatched_rag_predictions": [
    {
      "rag_occurrence_id": "string",
      "rag_predicted_bias_name": "string",
      "rag_ontology_status": "reference_ontology | outside_reference_ontology | unknown",
      "rag_confidence": "high | moderate | low | null",
      "best_related_hidden_instance_id": "string | null",
      "best_related_hidden_bias_name": "string | null",
      "localized_segment_id": "string | null",
      "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
      "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
      "classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | outside_ontology_non_equivalent",
      "why_not_an_exact_match": "string"
    }
  ],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [
      {
        "candidate_id": "string",
        "proposed_bias_name": "string",
        "localized_segment_id": "string | null",
        "best_related_hidden_instance_id": "string | null",
        "quote_validity": "valid | invalid | not_assessable",
        "would_match_if_promoted": false,
        "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
        "details": "string"
      }
    ]
  },
  "segment_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    },
    "high_only": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    },
    "high_and_moderate": {
      "true_positives_hits": 0,
      "false_negatives_misses": 0,
      "false_positives_false_alarms": 0,
      "true_negatives_correct_rejections": 0,
      "hit_rate": 0.0,
      "false_alarm_rate": 0.0,
      "accuracy": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0
    }
  },
  "instance_level_metrics": {
    "all_identified_confidence_levels": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    },
    "high_only": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    },
    "high_and_moderate": {
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "exact_occurrence_match_rate": 0.0,
      "occurrence_count_match_rate": 0.0
    }
  },
  "per_bias_metrics": [
    {
      "canonical_bias_name": "string",
      "hidden_requested_occurrences": 0,
      "rag_identified_occurrences_all_confidence": 0,
      "true_positives_exact_matches": 0,
      "false_negatives_misses": 0,
      "false_positives": 0,
      "precision": 0.0,
      "recall": 0.0,
      "f1": 0.0,
      "count_match_status": "exact_match | underdetected | overdetected | not_applicable"
    }
  ],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_mapping_count": 0,
    "near_neighbor_prediction_count": 0,
    "outside_ontology_prediction_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "instance_level_primary_result": "string",
    "main_failure_modes": [
      "string"
    ],
    "main_strengths": [
      "string"
    ],
    "benchmark_interpretation": "string"
  }
}

OUTPUT RULES

1. Always return all top-level fields in the required schema.
2. Use empty arrays for no items.
3. Use null only where the schema permits null.
4. Use JSON booleans, not quoted booleans.
5. Use integer counts, not strings.
6. Use numeric metric values rounded to four decimal places.
7. Use null, not 0, for a rate or metric with a zero denominator.
8. Set `primary_corpus_fidelity_score_available` to false unless actual retrieved passages, source chunks, or retrieval logs are supplied as inputs.
9. Do not calculate d-prime, criterion, ROC statistics, or other advanced SDT metrics unless explicitly requested in a separate instruction and the segment-level trial data are suitable.
10. Do not report a label-level true-negative or correct-rejection count.
11. Report correct rejections only in `segment_level_metrics`.
12. Do not include RAG candidates in primary segment-level or instance-level metrics.
13. Count every unmatched RAG identified occurrence exactly once in `unmatched_rag_predictions`.
14. Ensure all instance-level false positives can be reconciled with unmatched RAG identified predictions, including wrong-label, wrong-location, wrong-mechanism, duplicate, and unsupported predictions.
15. Ensure all hidden planned instances are represented exactly once in `instance_level_adjudications`.
16. If a prevalidated segment map is used, preserve its segment IDs and ground-truth labels exactly.
17. If a segment map is generated, include every generated eligible reasoning segment in interview order.
18. Keep the segment-level and instance-level confusion matrices conceptually and numerically separate.
19. Do not award a strict instance-level true positive when the model merely identifies the correct general topic, decision episode, or speaker but misses the required cognitive mechanism.
20. Do not penalize the RAG system for not identifying biases outside the exhaustive hidden manifest.
