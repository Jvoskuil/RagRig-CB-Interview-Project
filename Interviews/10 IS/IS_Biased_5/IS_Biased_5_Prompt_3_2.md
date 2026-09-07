You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal process review, and that's fine with you?

Participant: Yeah, that's fine.

Interviewer: Great. Can you tell me your role and roughly how long you've been in it?

Participant: I'm the senior systems administrator for network infrastructure. I've owned our remote-access stack — VPN concentrator, firewall, related ACLs — for about six years now. Small team, just me and one other engineer.

Interviewer: Perfect. I'd like you to walk me through a specific incident — the VPN concentrator vulnerability from earlier this year. Just give me the whole story first, then we'll go back through it in detail.

Participant: Sure. So the vendor disclosed a critical remote-code-execution CVE in our concentrator's firmware — a 9.8 on the CVSS scale, about as bad as it gets. Same day, they released a patch. I applied it within a few hours, tested it, no issues. That part was straightforward. The bigger question was what to do longer-term. We'd actually scoped a full move to a cloud-based Zero Trust setup about eight months earlier, but it got shelved — budget cycle, other priorities. When this CVE hit, leadership asked whether we should revisit that. I ended up recommending we stay on the concentrator, patched and hardened, rather than restart the migration project right then.

Interviewer: And that decision stuck for how long?

Participant: About two weeks, until I actually did start engaging vendors — Vendor A, a cloud SASE/ZTNA platform, and Vendor B, an on-prem replacement appliance. I went back and forth, ended up shortlisting Vendor A. Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit. Migration got approved, and we scheduled the cutover. Vendor recommended a two-week parallel run where old and new systems operate side by side. I compressed that to one week based on how previous cutovers had gone for me. We had some rough days afterward — a subset of users with hybrid authentication had intermittent access failures for several days before we sorted it out.

Interviewer: Let's build the timeline in order. What happened right after you applied the patch?

Participant: It installed clean, no service interruption, users never noticed. Two days later the vendor put out a follow-up advisory saying they were seeing exploitation attempts in the wild against systems that hadn't patched yet. That validated the urgency, but we were already covered.

Interviewer: And the vendor evaluation — how did that actually unfold once proposals came in?

Participant: Vendor A's deck opened with a stat — 98% of their enterprise migrations completed without a reported incident. Vendor B's numbers came through an analyst report, phrased differently: 2% of their on-prem deployments had a post-install incident in year one. Cost and timeline were basically a wash between the two. A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A.

Interviewer: What did the peer-forum conversation add?

Participant: I posted in a regional admin group, and the response was pretty clear — five of six comparable firms in our sector had already gone with Vendor A's platform. Nobody shared much detail about their own environments, though. One of those five later told me, in a follow-up call, that they'd had to roll back some legacy application integrations after their rollout.

Interviewer: Let's slow down on decision one — patch and stay versus migrate immediately versus take the concentrator offline. Walk me through your reasoning there.

Participant: Taking it fully offline wasn't realistic — that's our only remote-access path for twelve hundred people, including trading desk staff. Between patching-and-staying versus fast-tracking a full migration, I leaned toward staying. We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one. I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically.

Interviewer: What information did you have in front of you at that moment, versus what you were recalling from memory?

Participant: In front of me: the CVSS score, the patch itself, and honestly not much detail yet on real-world exploitation — that came two days later. What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally.

Interviewer: Moving to the vendor decision — what specifically made Vendor A stand out?

Participant: Honestly, that 98% figure just read better. "98% success" sounds a lot more solid than "2% incident rate," even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials.

Interviewer: How much weight did the peer adoption numbers carry when you committed to Vendor A?

Participant: A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable.

Interviewer: And the parallel-run decision — why compress it to one week?

Participant: We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had. I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record. Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call.

Interviewer: What would have changed your decision at that last step?

Participant: If I'd mapped out specifically how the new authentication flow differed from what I'd handled before, rather than just leaning on "I've done this kind of thing before," I might have kept the full two weeks or pushed the date until we were fully staffed.

Interviewer: Last few questions. If the peer forum hadn't mentioned adoption numbers at all, do you think you'd have approached the vendor decision differently?

Participant: Probably. I think I'd have leaned more on the technical call that reconciled the two vendors' statistics, and maybe pushed harder for referenceable environments similar to ours before committing.

Interviewer: And if staffing had been full during the cutover?

Participant: I might still have compressed the timeline — that instinct came from my own history with cutovers, not just the staffing gap. But I probably would've caught the authentication mismatch sooner if I'd had a second set of eyes free to dig into it.

Interviewer: Anything you'd want more information on, if you were facing this again?

Participant: A cleaner side-by-side of vendor stats up front, normalized to the same format, so wording doesn't do the persuading. And probably a harder look at how similar peer environments actually were to ours before treating their choice as a green light.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Status Quo Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Framing Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Bandwagon effect",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Status Quo Bias",
      "Framing Bias",
      "Bandwagon effect",
      "Overconfidence Bias",
      "Availability Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Status Quo Bias", "requested_occurrences": 1 },
      { "bias": "Framing Bias", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 },
      { "bias": "Availability Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias" },
      { "instance_id": "cb_02", "bias": "Availability Bias" },
      { "instance_id": "cb_03", "bias": "Framing Bias" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "cb_03", "bias": "Framing Bias", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Status Quo Bias",
        "mechanism": "Defaulting to retaining the familiar legacy VPN concentrator over an equally viable migration alternative, justified by familiarity rather than comparative analysis",
        "affected_reasoning_operation": "Option evaluation / choice among alternatives",
        "evidence_source": "Availability of an equally-costed migration option scoped 8 months prior, versus decision to retain legacy system",
        "distinctiveness_requirement": "Distinguished from cb_02 by concerning the choice of architecture itself, not the probability estimate of harm"
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Bias",
        "mechanism": "Overweighting a vivid, memorable peer-firm ransomware incident when estimating the likelihood/severity of the current CVE, rather than relying on the CVE's own technical exploitation evidence",
        "affected_reasoning_operation": "Probability/risk estimation",
        "evidence_source": "Recalled peer-firm breach narrative versus CVSS/technical advisory data",
        "distinctiveness_requirement": "Distinguished from cb_01 by concerning risk-severity judgment, not the architectural choice; uses a different evidence source (recalled incident vs. institutional familiarity)"
      },
      {
        "instance_id": "cb_03",
        "bias": "Framing Bias",
        "mechanism": "Vendor preference shifts based on whether a statistically equivalent figure is presented as a success rate versus an incident rate",
        "affected_reasoning_operation": "Comparative evaluation of vendor evidence",
        "evidence_source": "Vendor A '98% success' framing versus Vendor B '2% incident' framing of an equivalent statistic",
        "distinctiveness_requirement": "Unique to Decision Point 2; no other instance involves numerically equivalent statistics presented in different valence"
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "mechanism": "Treating peer-adoption volume as sufficient validation of vendor fit, substituting for independent compatibility verification",
        "affected_reasoning_operation": "Evidence weighting / decision justification",
        "evidence_source": "Peer forum report that 5 of 6 comparable firms adopted Vendor A, absent environment-specific compatibility data",
        "distinctiveness_requirement": "Unique to Decision Point 3; concerns social-proof weighting rather than statistical framing or architectural inertia"
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "mechanism": "Overestimating personal capability to manage a materially different cutover based on unrelated past successes, leading to compression of a recommended safety margin under reduced staffing",
        "affected_reasoning_operation": "Self-assessment of capability applied to risk-mitigation planning",
        "evidence_source": "Three prior successful cutovers (different architecture) cited to justify shortening the vendor-recommended parallel-run period despite reduced staffing and a new authentication model",
        "distinctiveness_requirement": "Unique to Decision Point 4; concerns self-assessed capability, not external social or vendor evidence"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Framing Bias", "strength": "moderate" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Public exploitation status of the CVE at the time of initial triage",
      "original_state": "No confirmed in-the-wild exploitation reported at Decision Point 1; confirmation arrives two days later",
      "changed_state": "Confirmed active in-the-wild exploitation against the firm's own IP range already reported at Decision Point 1",
      "variables_to_hold_constant": [
        "Vendor proposals and statistical framing",
        "Peer-adoption pattern and forum content",
        "Staffing levels and cutover timeline",
        "All four decision points and their alternatives"
      ]
    },
    "scenario_id": "IS_Biased_5",
    "domain_id": "IS",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points per mechanism fit and narrative realism; Decision Point 1 hosts two distinct biases (Status Quo Bias and Availability Bias) using separate evidence sources and reasoning operations (architectural choice vs. probability estimation), consistent with allocation rules 1-4. No bias exceeds one instance per decision point, so the same-bias co-location cap (rule 3) is not triggered.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vendor proposals and statistical framing",
      "Peer-adoption pattern and forum content",
      "Staffing levels and cutover timeline",
      "All four decision points and their alternatives"
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
