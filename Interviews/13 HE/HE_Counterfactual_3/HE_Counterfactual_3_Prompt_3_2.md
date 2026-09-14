You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for sitting down with me. This is part of a research review on design decision-making, it's recorded, nothing gets tied to your name, and you can pass on anything you'd rather not get into. Okay?

Participant: Sure, no problem.

Interviewer: Tell me about your role on this project and what it involved.

Participant: I was lead design engineer on a sprinkler retrofit for a distribution warehouse, 140,000 square feet, tilt-up concrete. The owner was bringing in a new third-party logistics tenant who needed part of the floor converted to high-piled rack storage, double-row selective rack up to 32 feet. I had to redesign the existing system, which was sized for a lighter occupancy, get it through plan review, and get it installed before the tenant's lease started.

Interviewer: How did the schedule on this one compare to a typical retrofit?

Participant: Actually pretty comfortable, for once. We had six weeks from kickoff to permit submission, which is more breathing room than I usually get. The existing water supply and riser sizing were still set up for the old, lower-hazard use, so that part of the challenge was still there, but I wasn't fighting the calendar the way I sometimes am.

Interviewer: Walk me through the incident from the start.

Participant: Early on I needed to settle the commodity classification, since that drives the density, the rack sprinkler requirements, everything downstream. I didn't have a finalized SKU or packaging list from the tenant yet, they were still working that out on their end, and the owner wanted the classification locked so he could fix the retrofit budget. There wasn't really a schedule reason it had to happen that week, I could have waited and asked for a sample of their packaging list, but I'd done two other jobs for similar 3PL operators and had a good sense of what that kind of tenant typically stores. I went with Class III based on that pattern and moved on. Then I pulled the NFPA density and area curves for that classification at 32 feet, picked a point that cleared the code minimum, and built the hydraulic calculations. There was still plenty of runway before submission, so I could have run a few more combinations against the actual rack layout, but I didn't loop back to compare. That package went to the owner, who wanted a value-engineering pass since it came in over budget, and we talked about trimming the in-rack sprinkler allowance. Once the system was installed, we got to commissioning, and with the schedule no longer tight, we did the full witnessed flow test without any rush.

Interviewer: Let's reconstruct that in order. What happened first?

Participant: Classification, in the first week or so. Density and area selection maybe two and a half weeks in. Value engineering came after plan review comments, around week four. Commissioning was near the end, but we still had days to spare before move-in.

Interviewer: What did you learn after the classification that you didn't know when you made it?

Participant: A partial inventory list came in later and showed more exposed unexpanded plastics mixed with the cartoned goods than I'd assumed, closer to a plastics classification than straight Class III.

Interviewer: Going back to that first call, what did you actually have in hand, and how much time did you have to get more?

Participant: I had the tenant's general business type and my history with two comparable clients. I didn't have their SKU list, but with six weeks on the clock, I probably had time to ask for a preliminary sample and wait a bit.

Interviewer: Did you consider requesting that data before finalizing?

Participant: I thought about it briefly. But in my experience, this type of tenant runs cartoned retail goods, maybe some mixed packaging, and both of the prior jobs landed at Class III. I went with that pattern instead of waiting on their list.

Interviewer: If you'd had the SKU list before classifying, would you have done anything differently?

Participant: Probably, yeah, if the plastics share had been visible upfront I'd have leaned more conservative from the start.

Interviewer: What would have made you press for that data given you had the time?

Participant: Something specific standing out, like if they'd mentioned electronics or aerosols. Nothing in the early conversations flagged that, so it didn't feel urgent to chase down.

Interviewer: Moving to the density selection. What alternatives were actually available to you?

Participant: Several density and area points would have satisfied code minimum for Class III at that height, some needing more in-rack sprinklers. I could have compared those against the specific rack configuration and aisle widths, or checked the manufacturer's guide for something tailored to the layout.

Interviewer: With several weeks still on the calendar, what determined which one you picked?

Participant: I took the first point that cleared the minimum for the assumed classification and built the calc package around it. I had the time to run more comparisons, honestly, I just didn't loop back once I had something that worked.

Interviewer: Did the plan reviewer comment on that later?

Participant: Yeah, flagged that the point I'd chosen was close to the edge of the applicable curve for the actual rack configuration. Not a rejection, just a note to be aware of.

Interviewer: What went through your mind when the owner asked for value engineering?

Participant: He wanted the number under budget, and the in-rack allowance was the biggest thing I could trim. Keeping it would've given more margin against the classification uncertainty I already knew about. But we've got two more retrofit jobs pending with him, and I didn't want friction over one line item, so I recommended pulling the allowance to hit his number.

Interviewer: Did you walk him through the classification uncertainty as part of that?

Participant: Not in much depth. I mentioned it, but I framed the removal as a reasonable trade rather than spelling out how much margin we'd be giving up.

Interviewer: If there'd been no ongoing relationship with the owner, would that conversation have gone differently?

Participant: Possibly. I'd like to think I'd have pushed harder to keep the allowance, but I can't say for sure.

Interviewer: Last decision point, commissioning. What determined the testing you pursued?

Participant: The AHJ requires the witnessed flow test regardless, and with days to spare before move-in, there wasn't a reason to cut corners. I did the full test.

Interviewer: How did it turn out?

Participant: Passed comfortably, well above the required minimum. No concerns there.

Interviewer: Looking back, given that schedule wasn't really the constraint here, is there a decision you'd make differently?

Participant: The classification, still. Everything downstream followed from that first call, and I had the time to ask for more data before locking it in. I just didn't use it that way.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Incentive bias",
        "occurrences": 1,
        "mechanism_constraint": "Must be held constant relative to HE_Biased_3, unaffected by the schedule-length manipulation"
      },
      {
        "bias": "Satisficing",
        "occurrences": 1,
        "mechanism_constraint": "Must be shown to occur despite calendar time remaining, not attributable to schedule scarcity"
      },
      {
        "bias": "Stereotyping",
        "occurrences": 1,
        "mechanism_constraint": "Must be shown to occur despite feasible opportunity to obtain tenant-specific data within the extended window"
      }
    ],
    "target_bias_names": ["Incentive bias", "Satisficing", "Stereotyping"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Incentive bias", "requested_occurrences": 1},
      {"bias": "Satisficing", "requested_occurrences": 1},
      {"bias": "Stereotyping", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "st_01", "bias": "Stereotyping"},
      {"instance_id": "sf_01", "bias": "Satisficing"},
      {"instance_id": "ib_01", "bias": "Incentive bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "st_01", "bias": "Stereotyping", "decision_point": 1},
      {"instance_id": "sf_01", "bias": "Satisficing", "decision_point": 2},
      {"instance_id": "ib_01", "bias": "Incentive bias", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "st_01",
        "bias": "Stereotyping",
        "mechanism": "Category-based inference about tenant storage hazard substituted for case-specific inventory verification, persisting despite feasible time to verify",
        "affected_reasoning_operation": "Evidence-selection/classification during commodity classification",
        "evidence_source": "Similarity to two prior 3PL clients vs. absent tenant-specific SKU/packaging data, with six-week schedule allowing time to request it",
        "distinctiveness_requirement": "Only stereotyping instance in the scenario; occurs solely at Decision Point 1 tied to classification; distinguished from the paired base scenario by the explicit absence of schedule pressure as an available justification."
      },
      {
        "instance_id": "sf_01",
        "bias": "Satisficing",
        "mechanism": "Premature stopping at the first code-minimum-satisfying design option instead of comparing configuration-specific alternatives, despite remaining calendar time",
        "affected_reasoning_operation": "Alternative-generation and comparison during hydraulic density/area selection",
        "evidence_source": "Multiple available density/area curve points and manufacturer guidance vs. several weeks of schedule slack remaining",
        "distinctiveness_requirement": "Only satisficing instance in the scenario; occurs solely at Decision Point 2 tied to density/area selection; distinguished from the paired base scenario by removing the time-scarcity justification available in HE_Biased_3."
      },
      {
        "instance_id": "ib_01",
        "bias": "Incentive bias",
        "mechanism": "Recommendation shaped by desire to preserve an ongoing multi-project client relationship rather than neutral risk weighing; unaffected by the schedule-length manipulation",
        "affected_reasoning_operation": "Selective emphasis in risk-tradeoff communication during value-engineering recommendation",
        "evidence_source": "Owner's budget request and pending future projects vs. unresolved classification-uncertainty risk from Decision Point 1",
        "distinctiveness_requirement": "Only incentive-bias instance in the scenario; occurs solely at Decision Point 3 tied to the value-engineering recommendation; held constant across base and counterfactual scenarios since the manipulated causal variable is schedule length, not the client relationship."
      }
    ],
    "intended_strength": [
      {"instance_id": "st_01", "bias": "Stereotyping", "strength": "subtle"},
      {"instance_id": "sf_01", "bias": "Satisficing", "strength": "moderate"},
      {"instance_id": "ib_01", "bias": "Incentive bias", "strength": "moderate"}
    ],
    "paired_scenario_id": "HE_Biased_3",
    "counterfactual_variable": {
      "name": "Length of the design schedule before permit submission deadline",
      "original_state": "Three-week compressed design window",
      "changed_state": "Six-week design window before permit submission deadline",
      "variables_to_hold_constant": [
        "Building, tenant type, and rack configuration",
        "Fixed retrofit budget set before classification confirmation",
        "Ongoing multi-project relationship between the engineer's firm and the building owner",
        "Existing water supply and riser infrastructure limitations",
        "AHJ requirement for hydraulic calculations and witnessed flow test",
        "The four decision points, their alternatives, and their sequencing",
        "The three targeted bias instances and their assigned decision points and mechanisms"
      ]
    },
    "scenario_id": "HE_Counterfactual_3",
    "domain_id": "HE",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences spread one-per-bias across three distinct, mechanism-fitting decision points, mirroring the base scenario's allocation (Stereotyping at Decision Point 1, Satisficing at Decision Point 2, Incentive bias at Decision Point 3), with Decision Point 4 left free of intentional bias instances. The schedule-length causal variable is manipulated to strip away the time-pressure justification available at Decision Points 1 and 2 in the base scenario, while the relationship-driven mechanism at Decision Point 3 is deliberately held constant as it is orthogonal to the manipulated variable.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Building, tenant type, and rack configuration",
      "Fixed retrofit budget set before classification confirmation",
      "Ongoing multi-project relationship between the engineer's firm and the building owner",
      "Existing water supply and riser infrastructure limitations",
      "AHJ requirement for hydraulic calculations and witnessed flow test",
      "The four decision points, their alternatives, and their sequencing",
      "The three targeted bias instances and their assigned decision points and mechanisms"
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
