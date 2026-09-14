You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal research purposes only, and you can pause or skip anything. Is that alright?

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

Interviewer: That's really helpful — thank you for walking through it in this much detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
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
