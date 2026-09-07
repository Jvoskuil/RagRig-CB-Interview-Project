You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'm trying to understand your reasoning process during the AFW procedure revision, not evaluating performance. Everything stays de-identified in my notes. Sound okay?

Participant: Sure, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me what this revision was for and why it came up?

Participant: So we had a design change package come through — the legacy analog level transmitter on one of the AFW trains got swapped for a new digital unit. Different response curve, different failure modes than what the old EOP steps were written around. My job was to update the Emergency Operating Procedure sequence so the initiation steps matched the new instrumentation, get it through V&V and human-factors review, and have it ready before the outage window opened. We had about three days.

Interviewer: What was your main objective going in?

Participant: Get an accurate, defensible procedure revision done on time. Accurate matters obviously, but the deadline was real — outage planning had already built the implementation window around this, so slipping it wasn't really an option without a whole scheduling conversation nobody wanted to have.

Interviewer: Walk me through the incident from the beginning.

Participant: Right when I started, an industry OE report landed in my queue — a transmitter failure at another station involving a new digital level transmitter. My first reaction was, okay, this is directly relevant, new digital unit, level transmitter, similar failure. I started pulling language from it into my draft pretty quickly. It was only later, when I looped in the I&C engineer who'd actually executed our design change, that he pointed out the OE unit used a different sensing technology than ours — different vendor family entirely. So the applicability wasn't as clean as I'd assumed.

From there I moved into drafting the actual verification steps. The new transmitter needed a two-point calibration check that the old analog unit never required. I've written a lot of these AFW revisions over the years, so I built the verification section using the template sequence I normally use. That went to peer review, and the reviewer caught that the calibration check wasn't in there at all — I'd basically carried over the old pattern without building it fresh around the new requirement.

Interviewer: What happened next?

Participant: I had to set validation criteria — basically, what surveillance test data to use as the benchmark for confirming the new steps work as intended. We've got five years of AFW surveillance history, but I also had a test from two weeks earlier on a different, unrelated procedure that happened to use a similar-looking verification form. That one was fresh in my head, so I anchored the validation criteria around it. Turned out later, when someone did a fuller data pull, that some of the older historical tests actually covered operating conditions closer to this transmitter's actual fault signature than the recent one did.

Interviewer: And the final stretch?

Participant: Last day, deadline under 24 hours out. I wanted to check the OE database more thoroughly, but part of it was locked because of a concurrent audit. So I worked off what I had — control room log, my own notes — and judged that was enough to close it out. I did a mental run-through of the failure modes and figured we'd covered the main ones, so I signed off and sent it to the approval board. They came back afterward asking for a supplemental risk note because there was a failure mode the draft hadn't addressed.

Interviewer: Let's go back to that OE report moment. What specifically made you decide it applied to your transmitter?

Participant: Honestly, the framing — "new digital level transmitter failure" — matched our situation closely enough that it registered as the same kind of event. I didn't stop to verify the sensing technology before I started drafting around it. In hindsight I probably should've asked the I&C engineer first, but it read as applicable on its face.

Interviewer: What alternatives did you consider there?

Participant: I could've tabled it as low relevance until I confirmed equivalence, or gone straight to the I&C engineer before touching the draft. I didn't do either — I just moved forward with incorporating it.

Interviewer: On the verification steps — what sources did you actually rely on when drafting?

Participant: Mostly my own prior work. I've done this enough times that I have a rhythm to how these sections get built. I did have the design change package open, but I wrote the structure first and meant to reconcile it against the specific requirements after — that reconciliation step is where the calibration check got missed.

Interviewer: Was consulting the I&C engineer before drafting ever on the table?

Participant: It was an option. I just didn't think I needed it at that stage — this felt like standard territory.

Interviewer: How did you decide which historical test data to weight most heavily for the validation criteria?

Participant: The two-week-old test was just top of mind — I'd looked at that form recently for something else, and it seemed like a reasonable proxy. I didn't go back and systematically compare it against the older data set for relevance to this transmitter's specific fault modes. In hindsight, the older data had more operating conditions represented.

Interviewer: When time got short at the end, how did you decide the draft was ready to submit?

Participant: I looked at what was actually accessible — the control room log, my notes — and it felt like enough to call it done. The audit had the fuller OE records locked up, and requesting an extension felt like it would just push the whole outage schedule, so I didn't pursue that. On the risk side, I ran through the failure modes I could recall from the design package, felt like the major ones were addressed, and made the call that residual risk was acceptable.

Interviewer: Did escalating to the Shift Technical Advisor come up as an option?

Participant: It did cross my mind, but I didn't think the open question was significant enough to escalate at the time.

Interviewer: If you'd had another full day for the OE report review, would you have handled that differently?

Participant: Probably — I'd have gotten the I&C engineer's read on technical equivalence before drafting anything, rather than after.

Interviewer: If the audit hadn't locked the database, what would you have checked?

Participant: I'd have wanted to search for any other OE items involving this exact transmitter model, and cross-check the failure-mode list more completely instead of relying on memory.

Interviewer: Looking back, is there a point you'd have wanted a second set of eyes earlier?

Participant: Probably right after the OE report came in, before I started building language around it.

Interviewer: How confident were you in that final risk judgment at the time, compared to now?

Participant: At the time, reasonably confident — it felt sufficient given what I had access to. Now, knowing the board found a gap, I'd say I was more confident than the evidence actually supported.

Interviewer: That's really helpful. Thanks for walking through all of that in detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Similarity Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Habit Intrusion",
        "occurrences": 1,
        "mechanism_constraint": "human performance often can be captured by familiar behavioral patterns that occur so frequently in their experiences."
      },
      {
        "bias": "Bounded Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Recency Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Imperfect Rationality",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Similarity Bias",
      "Habit Intrusion",
      "Bounded Rationality",
      "Recency Bias",
      "Imperfect Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Similarity Bias", "requested_occurrences": 1},
      {"bias": "Habit Intrusion", "requested_occurrences": 1},
      {"bias": "Bounded Rationality", "requested_occurrences": 1},
      {"bias": "Recency Bias", "requested_occurrences": 1},
      {"bias": "Imperfect Rationality", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "sb_01", "bias": "Similarity Bias"},
      {"instance_id": "hi_01", "bias": "Habit Intrusion"},
      {"instance_id": "rb_01", "bias": "Recency Bias"},
      {"instance_id": "br_01", "bias": "Bounded Rationality"},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality"}
    ],
    "intended_decision_points": [
      {"instance_id": "sb_01", "bias": "Similarity Bias", "decision_point": 1},
      {"instance_id": "hi_01", "bias": "Habit Intrusion", "decision_point": 2},
      {"instance_id": "rb_01", "bias": "Recency Bias", "decision_point": 3},
      {"instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 4},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "sb_01",
        "bias": "Similarity Bias",
        "mechanism": "Applicability judged from surface resemblance between OE report equipment and local transmitter rather than confirmed technical equivalence",
        "affected_reasoning_operation": "Relevance/applicability judgment during evidence triage",
        "evidence_source": "OE report vs. local design change package",
        "distinctiveness_requirement": "Only instance of Similarity Bias; occurs solely at decision point 1 during initial OE triage, not repeated elsewhere"
      },
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "mechanism": "Well-practiced standard procedure-writing template is applied automatically instead of the new transmitter's specific requirements",
        "affected_reasoning_operation": "Action selection during procedure drafting",
        "evidence_source": "Design change package requirement vs. engineer's habitual template use",
        "distinctiveness_requirement": "Only instance of Habit Intrusion; occurs solely at decision point 2 during drafting, distinct from OE triage or data weighting"
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "mechanism": "Most recently encountered test result is disproportionately weighted as the representative baseline over more relevant older historical data",
        "affected_reasoning_operation": "Evidence weighting during validation-criteria setting",
        "evidence_source": "Five-year historical test data vs. two-week-old test result",
        "distinctiveness_requirement": "Only instance of Recency Bias; occurs solely at decision point 3 during data weighting, distinct from drafting or final judgment"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Information search terminated once readily accessible records seem minimally sufficient, under time and access constraints, rather than continuing an exhaustive search",
        "affected_reasoning_operation": "Information-gathering termination decision",
        "evidence_source": "Control room log and personal notes vs. inaccessible locked OE database",
        "distinctiveness_requirement": "Shares decision point 4 with ir_01 but addresses the search-termination operation, using a different evidence source (accessible records) and occurring earlier in the DP4 sequence than the final judgment"
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "mechanism": "Final risk-acceptability judgment relies on a simplified holistic mental estimate rather than structured failure-mode-by-failure-mode analysis",
        "affected_reasoning_operation": "Final risk-acceptability synthesis prior to submission",
        "evidence_source": "Partial failure-mode documentation and engineer's own rough mental tally",
        "distinctiveness_requirement": "Shares decision point 4 with br_01 but addresses the final judgment-synthesis operation, occurring after the search-termination step and using the incomplete failure-mode list as its distinct evidence basis"
      }
    ],
    "intended_strength": [
      {"instance_id": "sb_01", "bias": "Similarity Bias", "strength": "subtle"},
      {"instance_id": "hi_01", "bias": "Habit Intrusion", "strength": "moderate"},
      {"instance_id": "rb_01", "bias": "Recency Bias", "strength": "subtle"},
      {"instance_id": "br_01", "bias": "Bounded Rationality", "strength": "moderate"},
      {"instance_id": "ir_01", "bias": "Imperfect Rationality", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Not applicable — no counterfactual condition requested",
      "original_state": "N/A",
      "changed_state": "N/A",
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_5",
    "domain_id": "NP",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences distributed across 4 decision points by mechanism fit and narrative realism: one bias per decision point at DPs 1-3 (Similarity Bias at OE triage, Habit Intrusion at drafting, Recency Bias at data weighting), with two distinct biases (Bounded Rationality, Imperfect Rationality) co-located at DP4 because both naturally arise under the same terminal time-pressured submission decision but target different reasoning operations (search termination vs. final judgment synthesis) with separate evidence sources, satisfying the same-bias co-location restriction and the distinct-evidence requirement.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
