You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HC_Biased_6",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
