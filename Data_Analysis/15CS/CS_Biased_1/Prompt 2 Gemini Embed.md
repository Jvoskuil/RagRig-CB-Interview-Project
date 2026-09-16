You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal research purposes only, and you can pause or skip anything. Is that alright?

Participant: Yep, that's fine.

Interviewer: Great. Can you start by telling me your role and roughly how long you've been doing it?

Participant: I'm a Security Architect. I've been at the company about five years, and for the last three I've owned most of our network segmentation architecture — design, implementation, the whole Zero Trust rollout.

Interviewer: Let's talk through the incident we discussed scheduling this around. What triggered it?

Participant: We had an external penetration test as part of prep for our annual audit cycle. The report came back with three findings. One was a segmentation gap allowing lateral movement between two zones we thought were isolated. Another was stale service-account credentials, and the third was incomplete log retention. Only the segmentation one was rated critical.

Interviewer: What was your objective once you saw that report?

Participant: Close the critical gap before the compliance window, without blowing up the rest of the Zero Trust program or causing outages. We had six weeks. Engineering bandwidth was tight — I basically had myself and one platform engineer who could help part-time. Any vendor spend needed budget sign-off, and leadership wanted an actual remediation plan, not just "we found a problem."

Interviewer: Walk me through what happened first.

Participant: First thing was triage. Three findings, limited hands, six weeks. I looked at severity and exploitability — the segmentation gap was the only one that let an attacker actually traverse between trust zones, so it was the obvious pick to go first. Credential rotation is scriptable and fast, log retention is a config change, neither needed the same urgency. So I told the CISO we'd tackle segmentation first and run the other two in parallel at lower priority, mostly automated.

Interviewer: What information did you have at that point versus what you learned afterward?

Participant: Initially I just had severity ratings. Once we dug in, we confirmed the lateral movement path was real — not just theoretical — between two zones that were supposed to be firewalled from each other. That's when platform engineering told me they genuinely didn't have spare capacity to fix all three at full depth simultaneously, which confirmed the sequencing call.

Interviewer: Let's go deeper on that first decision. Any alternative you seriously considered?

Participant: Running all three in parallel at reduced depth crossed my mind, but diluting effort across three findings when only one is critical felt like the wrong risk math. I ruled it out fairly quickly.

Interviewer: Once segmentation was the priority, how did you approach fixing it?

Participant: That's the part that took the most back-and-forth. The segmentation layer runs on a framework I built myself when we started the Zero Trust program. I know its internals cold — every policy enforcement point, every identity-aware proxy hook. The pentest vendor actually flagged that a vendor-managed ZTNA platform could close the same gap with less custom engineering, and there were some independent benchmarks suggesting similar coverage.

Interviewer: What sources did you pull in to compare the two paths?

Participant: I looked at our own effort estimates mostly. Patching the in-house framework was about four weeks of engineering time, with some uncertainty on edge-case coverage. The vendor path was quoted around three weeks including their security review, and they were offering coverage guarantees in writing.

Interviewer: So the vendor path was faster and came with a written guarantee. What made you go with the in-house patch?

Participant: Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but "guarantee" from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years.

Interviewer: Did you apply that same validation standard to the in-house patch — proving it against your topology before trusting it?

Participant: Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown.

Interviewer: Had you evaluated ZTNA vendors before this incident?

Participant: We'd looked at two platforms about a year earlier for a different project, and didn't move forward, mostly on cost. So there was some familiarity, but no deep hands-on testing.

Interviewer: How did time pressure factor into that decision?

Participant: There was pressure, but not extreme — six weeks was workable either way at that point. It wasnns't really the deadline pushing me toward the in-house option; it was more that I was confident I understood exactly what patching would take.

Interviewer: What did you present to the CISO?

Participant: I recommended patching and extending the existing framework, and that's what we went with. Afterward, platform engineering raised some integration concerns — mainly around a legacy service that didn't fit cleanly into the updated policy model — that hadn't been fully weighted when I made the original comparison.

Interviewer: Let's move to rollout. Once the patch was ready, what were your options?

Participant: Two real choices: a narrow pilot on one trust zone first, or roll out to all affected zones at once to save time, since we were now down to four weeks. There was also a middle option — stage it by risk tier over two weeks.

Interviewer: What did you choose and why?

Participant: Staged by risk tier. Full rollout all at once felt too risky if something broke — you'd have no isolated blast radius. A narrow pilot alone would've been safer but slower, and we didn't have four weeks to spare on a single-zone pilot before expanding. Staging let us validate against the highest-risk zones first while still making progress elsewhere.

Interviewer: Did anything unexpected come up during that rollout?

Participant: Yes — a legacy service ended up bypassing the new policy enforcement point entirely. It wasn't something we'd flagged as a risk going in. Platform engineering said fixing it properly would need more time than we had left.

Interviewer: What information, if you'd had it earlier, would have changed that rollout decision?

Participant: If we'd known about that legacy service's behavior beforehand, I probably would've included a targeted pilot on that specific service before staging everything else, rather than finding out mid-rollout.

Interviewer: Final decision point — reporting to the audit committee with two weeks left and an unresolved edge case. What were your options?

Participant: Report it as fully remediated, report as substantially remediated with a compensating control and a follow-up date, or ask for a deadline extension.

Interviewer: What did you decide?

Participant: Substantially remediated, with a documented compensating control on the legacy service and a committed date to close it out next sprint. Fully remediated would've been inaccurate given the open edge case, and I didn't think an extension was necessary since the core lateral-movement path was actually closed.

Interviewer: How confident were you in that characterization?

Participant: Reasonably confident. The committee accepted it with a follow-up item, which is roughly what I expected.

Interviewer: Looking back — if a different engineer, someone no longer at the company, had originally built that segmentation framework instead of you, do you think the remediation choice at decision point two plays out the same way?

Participant: That's a fair question. I'd like to think I'd have weighed the vendor option the same either way, but I'll admit — if it were someone else's code, someone I couldn't personally vouch for at 2 a.m. if something broke, I might have leaned harder on the vendor's written guarantees instead of my own confidence in the system.

Interviewer: And if the vendor platform had been proposed to replace someone else's system rather than yours?

Participant: I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default.

Interviewer: Last one — anything you'd do differently facing this same situation again?

Participant: Maybe get an outside technical review of both options before I made the call, just to check my own read on the comparison. Overall the outcome was fine, but I can see how the sequence of judgments got there.

Interviewer: That's really helpful — thank you for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Biased_1",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Security Architect",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Segmentation Framework Decision",
    "scenario_summary_internal": "A Security Architect at a mid-size fintech must remediate findings from an external penetration test that flags weaknesses in a Zero Trust micro-segmentation framework the architect personally designed and built three years earlier. A vendor-managed ZTNA/SASE platform is available as an alternative remediation path. Across four decision points (triage of findings, remediation option selection, rollout/testing approach, and escalation/reporting to leadership), the architect must weigh the in-house framework's continued viability against a comparably capable vendor alternative, under time pressure from a compliance deadline. At decision point 2, the architect exhibits endowment bias: overvaluing the self-built framework relative to its objective remediation cost and risk profile, and demanding a higher burden of proof from the vendor alternative than from the incumbent system.",
    "occupational_realism": {
      "objective": "Remediate a critical pentest finding regarding lateral-movement exposure in the network segmentation layer before a regulatory compliance deadline, while minimizing operational disruption and preserving the integrity of the broader Zero Trust program.",
      "setting": "Mid-size fintech company, internal security architecture team, six weeks before an annual SOC 2 / regulatory audit window, following a third-party penetration test.",
      "constraints": [
        "Compliance deadline in six weeks",
        "Limited engineering headcount available for remediation work",
        "Vendor procurement and security review adds lead time",
        "Existing framework is deeply integrated with internal CI/CD and identity systems",
        "Budget approval required for any new vendor spend",
        "Leadership expects a remediation plan, not just a diagnosis"
      ],
      "stakeholders": [
        "Security Architect (interviewee)",
        "CISO",
        "Penetration testing vendor",
        "Platform engineering lead",
        "Compliance/audit manager",
        "ZTNA vendor sales engineer"
      ],
      "technical_terms_to_use": [
        "micro-segmentation",
        "lateral movement",
        "Zero Trust Network Access (ZTNA)",
        "policy enforcement point",
        "identity-aware proxy",
        "attack surface",
        "compensating control",
        "remediation SLA"
      ],
      "technical_terms_to_avoid": [
        "endowment effect",
        "cognitive bias",
        "sunk cost",
        "loss aversion",
        "ownership bias"
      ],
      "excluded_themes": "NONE"
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pentest report lists three findings: segmentation gap, stale service-account credentials, incomplete log retention",
          "Only one finding is marked 'critical severity'",
          "Compliance deadline is six weeks out"
        ],
        "new_information_after_decision": [
          "Deeper triage reveals the segmentation gap allows lateral movement between two previously 'isolated' trust zones",
          "Platform engineering confirms limited bandwidth to fix all three findings in parallel"
        ],
        "alternatives": [
          "Prioritize the segmentation finding first as highest business risk",
          "Prioritize credential rotation first as fastest to close",
          "Run all three remediations in parallel with reduced depth on each"
        ],
        "intended_action": "Architect selects the segmentation finding as top priority based on severity and lateral-movement risk."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "In-house segmentation framework was designed and implemented by the architect three years prior",
          "A vendor ZTNA/SASE platform is available that independent benchmarks and the pentest vendor suggest would close the same gap with less custom engineering",
          "Fixing the in-house framework requires an estimated four weeks of engineering effort with residual uncertainty about coverage",
          "Vendor platform requires a security review and migration plan estimated at three weeks, with vendor-provided coverage guarantees"
        ],
        "new_information_after_decision": [
          "The chosen remediation path is presented to the CISO as the recommended fix",
          "Platform engineering raises concerns about integration effort that were not fully weighted in the original comparison"
        ],
        "alternatives": [
          "Patch and extend the in-house framework to close the gap",
          "Migrate the affected segment to the vendor ZTNA platform",
          "Deploy a temporary compensating control while evaluating both options further"
        ],
        "intended_action": "Architect chooses to patch and extend the in-house framework, citing familiarity and control, while applying a stricter evidentiary standard to the vendor option than to the in-house one. [ENDOWMENT BIAS INSTANCE cb_01]"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patched framework is ready for testing",
          "Two testing approaches are available: narrow pilot on one trust zone, or full rollout across all affected zones",
          "Compliance deadline is now four weeks away"
        ],
        "new_information_after_decision": [
          "Pilot or rollout surfaces an edge case where a legacy service bypasses the new policy enforcement point",
          "Platform engineering flags additional remediation time needed"
        ],
        "alternatives": [
          "Run a narrow pilot first, then expand if successful",
          "Roll out to all affected zones simultaneously to save time",
          "Stage rollout by risk tier over two weeks"
        ],
        "intended_action": "Architect selects a staged rollout by risk tier to balance validation confidence against the compressed timeline."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Staged rollout has closed the original lateral-movement path but the legacy-service edge case remains partially unresolved",
          "Compliance deadline is two weeks away",
          "CISO needs a status report for the audit committee"
        ],
        "new_information_after_decision": [
          "Audit committee accepts the report with a follow-up remediation item",
          "The unresolved edge case is scheduled for a subsequent sprint"
        ],
        "alternatives": [
          "Report the finding as fully remediated",
          "Report as substantially remediated with a documented compensating control and follow-up date",
          "Request a deadline extension pending full closure"
        ],
        "intended_action": "Architect reports the finding as substantially remediated with a documented compensating control and a committed follow-up date."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what triggered this incident and what your role was.",
        "What was your overall objective when you first reviewed the pentest report?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did the segmentation finding become the focus?",
        "What information did you have at each stage, and what changed afterward?"
      ],
      "decision_point_probes": [
        "What cues or evidence stood out to you when triaging the three findings?",
        "What information sources did you consult when comparing the in-house framework to the vendor platform?",
        "What alternatives did you consider at that point, and why did you rule the others out?",
        "What was the basis for your decision to extend the in-house framework rather than migrate?",
        "Had you evaluated vendor ZTNA platforms before? How did that prior experience factor in?",
        "How much time pressure did you feel at each stage, and how did that affect your evaluation?",
        "How confident were you in the coverage estimate for each remediation option?",
        "During the rollout decision, what made you choose a staged approach over a full rollout?",
        "When reporting to the audit committee, what led you to characterize the finding as 'substantially remediated'?"
      ],
      "closing_hypotheticals": [
        "If a different engineer had originally built the segmentation framework, do you think the remediation choice would have unfolded differently?",
        "If the vendor platform had been proposed as a replacement for someone else's system rather than your own, would your evaluation criteria have changed?",
        "Looking back, what would you do differently if you faced this same choice again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Endowment",
        "decision_point": 2,
        "mechanism": "The architect assigns disproportionately higher value to the in-house segmentation framework because they personally designed and built it, applying a stricter evidentiary bar to the vendor alternative than to the incumbent system despite comparable or superior objective indicators for the vendor option.",
        "affected_reasoning_operation": "Comparative evaluation and weighting of two remediation alternatives (in-house patch vs. vendor migration)",
        "evidence_available_at_time": [
          "Independent benchmarks and pentest vendor commentary favoring the vendor ZTNA platform's coverage guarantees",
          "Estimated engineering effort: 4 weeks (in-house) vs. 3 weeks (vendor) with vendor-provided coverage guarantees",
          "Architect's personal authorship of the in-house framework three years prior"
        ],
        "required_textual_manifestation": "The architect explicitly favors extending their own framework, citing 'knowing exactly how it works' and control over the code, while describing the vendor option's guarantees as unproven or requiring more validation than the self-built system received, without citing a comparable objective risk analysis for the in-house option.",
        "plausible_nonbias_interpretation": "Familiarity with an internally maintained system can legitimately reduce integration risk and operational uncertainty, which is a defensible engineering rationale independent of authorship attachment.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "endowment effect",
          "bias",
          "ownership attachment",
          "sunk cost"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": "Authorship of the incumbent segmentation framework (self-built vs. built by a different, now-departed engineer)",
      "original_state": "Architect personally designed and built the in-house segmentation framework being evaluated for remediation.",
      "counterfactual_state": "The in-house segmentation framework was originally built by a different, now-departed engineer, and the interviewee is only its current maintainer.",
      "variables_to_hold_constant": [
        "Pentest findings and severity ratings",
        "Compliance deadline and timeline pressure",
        "Vendor platform capabilities and cost estimates",
        "Staffing and engineering bandwidth constraints",
        "Rollout and reporting decisions at phases 1, 3, and 4"
      ],
      "expected_causal_difference": "Without personal authorship, the architect is expected to apply a symmetric evidentiary standard to both remediation options, reducing or eliminating the endowment-driven preference for the in-house framework observed at decision point 2.",
      "causal_test_question": "Does removing personal authorship of the incumbent system change the relative weighting applied to the in-house vs. vendor remediation options at decision point 2?"
    },
    "generation_checks": [
      "Exactly one endowment bias instance planned, matching manifest occurrences=1",
      "Endowment instance assigned to decision point 2 only, per automatic allocation since no allowed_decision_points was specified",
      "No bias labels, definitions, or psychological terms appear in probe_plan or timeline text intended for the public interview",
      "Four decision points defined, each with at least two alternatives",
      "Consequences at each decision point are ambiguous as to whether the decision was correct, avoiding mechanical proof of bias",
      "Target word count 1,350 (acceptable range 1,215-1,485) achievable given four decision points with proportionate probe depth",
      "No unrequested bias types intentionally embedded in any phase"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Endowment",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as disproportionate valuation of the self-built segmentation framework relative to the vendor alternative, expressed through asymmetric evidentiary standards applied to the two options during the remediation-option decision."
      }
    ],
    "target_bias_names": [
      "Endowment"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Endowment",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Endowment"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Endowment",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Endowment",
        "mechanism": "Overvaluation of the self-authored segmentation framework due to ownership/authorship, resulting in a stricter evidentiary bar for the vendor alternative than for the incumbent system.",
        "affected_reasoning_operation": "Comparative evaluation and weighting of remediation alternatives",
        "evidence_source": "Architect's stated rationale during comparison of in-house patch vs. vendor migration, including differential treatment of coverage evidence for each option",
        "distinctiveness_requirement": "Single occurrence; no requirement to distinguish from a second instance since occurrences=1."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Endowment",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Authorship of the incumbent segmentation framework",
      "original_state": "Architect personally designed and built the in-house segmentation framework.",
      "changed_state": "The in-house segmentation framework was built by a different, now-departed engineer; interviewee is only its maintainer.",
      "variables_to_hold_constant": [
        "Pentest findings and severity ratings",
        "Compliance deadline and timeline pressure",
        "Vendor platform capabilities and cost estimates",
        "Staffing and engineering bandwidth constraints",
        "Rollout and reporting decisions at phases 1, 3, and 4"
      ]
    },
    "scenario_id": "CS_Biased_1",
    "domain_id": "CS",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point offering the clearest mechanism fit (comparative evaluation of self-built vs. external remediation option) and greatest narrative realism for a Security Architect role; no allowed_decision_points were specified by the caller, so automatic assignment rules 1-4 were applied trivially given occurrences=1.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Pentest findings and severity ratings",
      "Compliance deadline and timeline pressure",
      "Vendor platform capabilities and cost estimates",
      "Staffing and engineering bandwidth constraints",
      "Rollout and reporting decisions at phases 1, 3, and 4"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  null
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
    "analysis_scope_note": "Mechanism-first evaluation of the participant's self-reported reasoning during a security incident remediation decision chain. Only affirmative, evidence-supported distortions were classified as identified occurrences; plausible but unconfirmed patterns were retained as candidates."
  },
  "identified_bias_summary": [
    {
      "bias_label": "IKEA effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "IKEA effect",
      "alternative_labels": [
        "Not invented here bias",
        "Effort justification"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overvalue objects, solutions, or systems that one has created or assembled, leading to inflated trust or preference relative to externally produced alternatives even when objective attributes do not justify that preference.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Remediation approach selection: in-house patch vs vendor-managed ZTNA",
      "decision_point_description": "Choice between patching the internally built segmentation framework and adopting a vendor-managed ZTNA platform to close the critical segmentation gap.",
      "affected_reasoning_operation": "Evaluation and weighting of alternative remediation options; comparative risk/benefit and trust assessment before recommendation to the CISO.",
      "bias_specific_mechanism": "The participant treated the self-built in-house system as a trusted baseline by default and applied an asymmetrical validation standard: the vendor platform was required to prove itself against the environment, while the in-house system was not. This inflated the relative perceived value of the self-created option and led to discounting the vendor's objectively favorable attributes, including shorter estimated timeline and written coverage guarantees.",
      "manifestation_in_interview": "The participant acknowledged the vendor path was faster and came with written guarantees, but recommended the in-house patch based on trust in code he wrote. He explicitly stated he did not require the same validation of the in-house system, and later admitted that if someone else had built the framework, he might have weighed the vendor option differently.",
      "effect_on_reasoning_or_decision": "The recommendation was directed toward the self-built system despite an objectively competitive or advantageous external option. Platform engineering later raised integration concerns that had not been fully weighted in the original comparison.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I trust what I built. I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider. The vendor's guarantee sounds good on paper, but 'guarantee' from a sales engineer isn't the same as proof in our specific environment. I wanted to see their platform actually validated against our topology before I'd trust it the way I trust code I wrote and have watched in production for three years.",
          "evidence_explanation": "Shows default trust in the self-built system and a higher evidentiary demand for the vendor option despite the vendor's favorable attributes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really the same way, no. I mean, I've lived with that system for three years, so it's not like I needed to re-prove it from scratch. It's more that the vendor is the newer unknown.",
          "evidence_explanation": "Directly demonstrates the asymmetrical validation standard: the in-house solution was exempted from the proof requirement applied to the vendor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd like to think I'd have weighed the vendor option the same either way, but I'll admit — if it were someone else's code, someone I couldn't personally vouch for at 2 a.m. if something broke, I might have leaned harder on the vendor's written guarantees instead of my own confidence in the system.",
          "evidence_explanation": "Counterfactual admission that self-ownership, rather than purely technical evidence, influenced the relative weighting of options."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I probably would've asked for the same proof-of-concept against our topology from both sides, rather than treating my own system as the trusted baseline by default.",
          "evidence_explanation": "Acknowledges that the self-built system was treated as a default trusted baseline rather than being compared symmetrically with the external alternative."
        }
      ],
      "correction_or_counterevidence": "The in-house system had a real operational track record, and the participant had legitimate technical familiarity with it. Requiring vendor validation before trusting an external platform was not entirely irrational. However, the explicit asymmetry in validation demands and the counterfactual self-report indicate that self-creation/ownership bias materially distorted the comparison.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The supplied retrieval context did not include passages on the IKEA effect, not-invented-here bias, or effort justification. Classification relies on established general cognitive-science knowledge rather than the retrieved corpus.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overestimation",
        "Planning fallacy"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "In-house patch planning and rollout risk assessment",
      "supporting_interview_quote": "I know exactly how it behaves under load, how it interacts with our CI/CD pipeline and identity provider.",
      "plausible_mechanism": "Excessive confidence in the completeness of the participant's knowledge about the self-built system may have led to underweighting integration risks and failing to anticipate the legacy service bypass later encountered during rollout.",
      "why_not_identified": "The transcript also includes recognition that the in-house patch had uncertainty on edge-case coverage, and the later legacy service issue may reflect incomplete operational information rather than a distinct overconfidence distortion at the time of the decision."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was not available for the identified IKEA effect/not-invented-here mechanism, so the label and mechanism were supplied from general cognitive-science knowledge.",
    "The analysis relies on participant self-report, which may omit or rationalize aspects of the reasoning.",
    "A legitimate expertise-based explanation for preferring the known in-house system cannot be fully excluded, although the asymmetrical validation standard supports the bias classification."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Biased_1_Gemini_on",
  "interview_id": "CS_Biased_1",
  "system_prompt_id": "Gemini",
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
