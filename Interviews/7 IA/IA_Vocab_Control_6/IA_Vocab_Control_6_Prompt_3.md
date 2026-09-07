You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. This conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. Skip anything you're not comfortable discussing. Can you tell me your role and how long you've been doing it?

Participant: Sure. I'm a threat intelligence analyst on the SOC team, about four years in, mostly financial services environments. During shift I handle triage, attribution, and hunt scoping when something looks like more than commodity noise.

Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared?

Participant: About two hours into an overnight shift, EDR kicked out a cluster of alerts on a trading-support server — the box that feeds reporting data to the trading engine, not the engine itself. The auto-triage score came back Low. That queue does throw a lot of low-severity noise from that host, and I'd seen similar low scores turn out benign twice before. But I also remembered one shift where a Low score turned into something real, so I didn't want to just wave it through on pattern-matching alone.

Interviewer: What was your primary objective at that point?

Participant: Cover the queue efficiently without missing something that needed attention, and produce a handoff that would hold up. About three hours were left in the shift, so I wanted to be deliberate about where I spent time.

Interviewer: Take me through what happened next, chronologically.

Participant: After the Low score, I did a quick scan of the alert summary fields — parent process, any flagged child processes, whether the trading-support role tag showed anything unusual. Nothing in that quick look overrode the Low score, so I deferred the full manual log pull, which would've run fifteen to twenty minutes, but I noted it to revisit if anything else came in. About forty minutes later it did — an outbound connection to an unfamiliar IP. That's when I opened the case properly. I found a registry-key artifact matching a GreyFalcon campaign I'd tracked myself about six months back. At the same time, two things didn't fit cleanly: the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure, and there was an attempted connection to the HR benefits database, which isn't a target GreyFalcon has gone after before. I didn't want to commit to an attribution with those loose ends open. A vendor bulletin came in with five IOCs — a rare C2 protocol signature and two file hashes among them — and I used that to build a scope. Near the end of shift, I had a vendor bulletin and a colleague's more hedged internal notes to work from for the containment write-up, and I checked both against telemetry before finalizing.

Interviewer: Let's slow down and go through each decision individually. First — the initial Low-severity alert. What cues were you weighing right then?

Participant: The auto-triage score, the server's history of false alarms, and the absence of any reported business disruption. But I also pulled up the summary fields rather than just accepting the score outright.

Interviewer: What made you decide to do that quick scan instead of either accepting the score outright or doing the full pull immediately?

Participant: It was a middle option. A full manual pull is a real time cost — fifteen, twenty minutes — and I didn't have grounds yet to justify that against the rest of the queue. But taking the score completely at face value without even glancing at the summary felt like too much trust in a score that's generated from a limited rule set. The five-minute look was a way to catch anything obviously wrong without committing the full review time.

Interviewer: Did you consider escalating to the IR lead first?

Participant: Briefly, but there wasn't anything at that point to escalate — a Low score and a quiet business environment. I planned to revisit if anything changed, which it did forty minutes later.

Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for your attribution call?

Participant: The registry-key match was strong — I'd documented that artifact myself in an earlier report, so I trusted it as a data point. But I didn't want to treat it as decisive on its own, because two things cut against it: the C2 domain's registration profile didn't match GreyFalcon's usual infrastructure, and the target — an HR database — wasn't something GreyFalcon has gone after in anything I've tracked. So I called it moderate confidence rather than high, and flagged both mismatches explicitly as things the hunt would need to test.

Interviewer: How did you handle the HR-targeting mismatch specifically? Did you have an explanation for it?

Participant: I didn't try to force one. It's possible there's a reason a GreyFalcon operator would go after HR data, but I didn't have evidence for that, so rather than guess at their motive I just left it as an open inconsistency — something that either gets explained by more evidence or ends up pointing away from this actor entirely.

Interviewer: Let's talk about the hunt scope decision once the vendor bulletin came in. How did you decide what to include?

Participant: The bulletin listed five IOCs — the protocol signature and two file hashes among them, not really ranked by the vendor in any stated order. I started with the two file hashes first, since they're more specific and carry a lower false-positive risk technically, and treated the protocol signature as a second pass to expand into if the first pass didn't resolve things. It wasn't about which one stood out most on the page — it was about which ones would tell me the most per unit of hunt effort.

Interviewer: Did the business preference for a narrow scope influence that?

Participant: A bit — trading-adjacent systems are sensitive to downtime, so starting narrow and staged was partly about not disrupting things unnecessarily. But the sequencing itself was based on which indicators were more diagnostic, not on convenience alone.

Interviewer: Last decision point — the containment recommendation. You had the vendor bulletin and your colleague's notes. How did you decide between them?

Participant: I didn't pick one over the other outright. The vendor bulletin was well-formatted and specific; the colleague's notes were hedged but, as far as I could tell, accurate. I checked specific claims from both against the telemetry I had — did the timestamps line up, did the described behavior match what we actually saw — and both held up partially. So the recommendation ended up blending the vendor's specific technical steps with the broader precautionary scope from the internal notes, because that's what the corroborated evidence supported, not because one read more convincingly than the other.

Interviewer: How confident were you overall in the final recommendation you handed off?

Participant: Moderate, maybe six out of ten. There was still an open question about attribution and an unresolved partial match on an additional host from the scope sweep, so I flagged both for next-shift follow-up rather than presenting it as closed.

Interviewer: Looking back, if you'd pulled the raw logs immediately in phase one instead of doing the shorter scan, how might things have unfolded?

Participant: I might have caught the outbound connection a little sooner, which could have given me more runway before the vendor window closed. Hard to know for sure — the summary scan didn't show anything that would've changed my initial call anyway.

Interviewer: If the vendor bulletin had listed its IOCs in a different order, do you think your scoping would have changed?

Participant: I don't think so. I wasn't going by the order they came in — I was staging based on which ones were more specific technically. If anything, reordering the list wouldn't have changed which ones I started with.

Interviewer: Is there a point in this sequence where you'd still want a second analyst's independent read before proceeding?

Participant: Probably the attribution step, just because of how much rode on it downstream. Even with the mismatches flagged, a second opinion on whether the registry-key match should carry as much weight as it did might have sharpened that call earlier rather than carrying open questions all the way through the hunt.

Interviewer: That's helpful, thank you. I think that covers what I need.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      { "bias": "Confimation Bias", "occurrences": 0, "mechanism_constraint": "No intended instance; evidence weighting during attribution must remain balanced and explicitly engage discordant infrastructure evidence." },
      { "bias": "Complacency Bias", "occurrences": 0, "mechanism_constraint": "No intended instance; triage verification decision must be proportionate and explicitly reasoned rather than deferred solely on automated score trust." },
      { "bias": "Explanation bias", "occurrences": 0, "mechanism_constraint": "No intended instance; scope decision must be justified by diagnosticity comparison, not narrative coherence alone." },
      { "bias": "Fluency effects", "occurrences": 0, "mechanism_constraint": "No intended instance; source-credibility weighting during containment must rest on cross-checked evidentiary content, not presentation quality." },
      { "bias": "Mirror Imaging Bias", "occurrences": 0, "mechanism_constraint": "No intended instance; adversary intent inference must avoid resolving via analogy to the analyst's own strategic logic." },
      { "bias": "Order effects", "occurrences": 0, "mechanism_constraint": "No intended instance; IOC list weighting during scoping must be driven by diagnosticity, not list position." }
    ],
    "target_bias_names": [
      "Confimation Bias", "Complacency Bias", "Explanation bias", "Fluency effects", "Mirror Imaging Bias", "Order effects"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confimation Bias", "requested_occurrences": 0 },
      { "bias": "Complacency Bias", "requested_occurrences": 0 },
      { "bias": "Explanation bias", "requested_occurrences": 0 },
      { "bias": "Fluency effects", "requested_occurrences": 0 },
      { "bias": "Mirror Imaging Bias", "requested_occurrences": 0 },
      { "bias": "Order effects", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IA_Biased_6",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Vocab_Control_6",
    "domain_id": "IA",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control condition requires zero intended occurrences of all named biases. No allocation across decision points was performed for bias mechanisms. Decision points were instead matched one-to-one to the paired scenario's four decision types (triage, attribution, scope, containment) with each corresponding reasoning process rewritten to be evidentially balanced.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical term set",
      "Occupational setting and stakeholder roster",
      "Four decision-point structure and decision types",
      "Underlying incident facts (server, registry-key artifact, C2 mismatch, HR access attempt, five-IOC bulletin, colleague notes)",
      "Time pressure and shift-deadline constraints",
      "Emotional tone and narrative complexity",
      "Probe plan structure and closing hypotheticals",
      "Approximate word count and dialogue format"
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
