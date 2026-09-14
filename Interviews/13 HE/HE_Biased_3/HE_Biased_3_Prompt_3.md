You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a research review of design decision-making, nothing you say will be tied to your name in any report, and you can skip anything you're not comfortable discussing. Sound okay?

Participant: Yeah, that's fine. I've done these before for our internal lessons-learned process, so I'm used to it.

Interviewer: Great. Can you start by telling me what your role was on this project and what the assignment involved?

Participant: Sure. I'm the lead design engineer on a sprinkler retrofit for a distribution warehouse, about 140,000 square feet, tilt-up concrete. The building owner was bringing in a new third-party logistics tenant who needed part of the floor converted to high-piled rack storage, double-row selective rack up to 32 feet. My job was to take the existing system, which was designed for a much lighter occupancy, and redesign it to handle the new storage configuration, get it through plan review, and get it installed before the tenant's lease start.

Interviewer: What made this one more complicated than a typical retrofit?

Participant: Mainly the schedule. We had about three weeks from kickoff to permit submission because the tenant's stocking schedule was locked in and the owner didn't want to renegotiate the lease start. On top of that, the existing water supply and riser sizing were set up for the old, lower-hazard use, so I was working within infrastructure that wasn't originally built for this.

Interviewer: Walk me through the incident from the beginning, in your own words.

Participant: We got the go-ahead and I needed to nail down the commodity classification pretty fast, because that drives everything else, the density, the rack sprinkler requirements, all of it. I hadn't gotten a finalized SKU or packaging list from the tenant yet, they were still finalizing their own inventory plans, but the owner wanted the classification locked so he could set the retrofit budget. I'd done two other jobs for similar 3PL operators in the past couple of years, so I had a sense of what that kind of tenant typically stores. Based on that, I classified it as Class III commodity and moved forward with design. From there I pulled the NFPA design density and area curves for that classification at 32 feet of rack height, picked a density/area point that cleared the code minimum, and built out the hydraulic calculations. That went to the owner for a value engineering pass, since the number came in over his budget, and we had a conversation about trimming the in-rack sprinkler allowance to bring the cost down. After the system was installed, we got to commissioning, and even with the schedule tight, I made sure we did the full witnessed flow test before sign-off, which the AHJ requires.

Interviewer: Let's reconstruct that chronologically. What came first?

Participant: Classification first, in the first few days. Then the hydraulic calc and density selection, maybe a week and a half in, right before permit submission. The value-engineering conversation with the owner happened after plan review comments came back, so maybe two and a half weeks in. Commissioning was right at the end, days before the tenant's move-in date.

Interviewer: What did you learn after the classification that you didn't know at the time you made it?

Participant: A partial inventory list came through a bit later, and it showed a decent chunk of exposed unexpanded plastics mixed in with the cartoned goods, more than I'd assumed. That pushed the actual profile closer to a plastics classification than straight Class III.

Interviewer: Let's go back to that classification decision specifically. What information did you actually have in hand at that point?

Participant: I had the tenant's general business type, third-party logistics handling retail goods, and I had my own history with two comparable clients. I didn't have their SKU list yet.

Interviewer: What other approaches did you consider before settling on Class III?

Participant: I could have asked for a preliminary packaging sample list before finalizing anything, or gone conservative and designed to a worst-case plastics assumption until the data came in.

Interviewer: Why didn't you go with either of those?

Participant: Honestly, this type of tenant, in my experience, usually runs cartoned retail goods, maybe some mixed packaging, but nothing that changes the classification much. The two prior jobs I'd done for similar operators both landed at Class III, so I went with that pattern rather than waiting on the tenant's list, especially with the owner pushing to lock the budget.

Interviewer: What would have made you wait for the SKU data instead?

Participant: If something about this particular tenant's business model had stood out as different, like if they'd mentioned handling electronics or aerosols specifically. Nothing in the early conversations flagged that, so I didn't press for the list before moving forward.

Interviewer: Let's move to the density selection. What alternatives were actually on the table?

Participant: There were several density/area points that would satisfy the code minimum for Class III at that rack height, some requiring more in-rack sprinklers, some less. I could have compared those against the specific rack configuration and aisle widths, or checked the manufacturer's design guide for something tailored to that layout.

Interviewer: What did you actually do?

Participant: I took the first density/area point that cleared the minimum for the assumed classification and built the calc package around it. We were up against the submission deadline, and that point technically satisfied the requirement, so I ran with it rather than working through the other combinations.

Interviewer: Did the plan reviewer have any comments on that later?

Participant: Yeah, the AHJ reviewer flagged that the point I'd chosen was pretty close to the edge of the applicable curve for the actual rack configuration. Not a rejection, just a note.

Interviewer: What was going through your mind when the owner asked for value engineering?

Participant: He wanted the number under budget, and the in-rack sprinkler allowance was the biggest line item I could trim. Retaining it would've kept more margin against the classification uncertainty, since I knew the plastics content wasn't fully confirmed yet. But we've got two more retrofit jobs pending with this same owner, and I didn't want that relationship to get strained over this one line item, so I recommended pulling the in-rack allowance to hit his number.

Interviewer: Did you lay out the classification uncertainty as part of that recommendation?

Participant: Not in as much detail as I probably could have. I mentioned it in passing but framed the removal as a reasonable trade-off rather than walking him through how much margin we'd be giving up.

Interviewer: Last decision point, commissioning. What determined how much testing you pursued?

Participant: The AHJ requires a witnessed flow test regardless, so that wasn't really optional. With the move-in date bearing down, I could have leaned on the contractor's certification paperwork and expedited sign-off, or done a partial test on just the modified risers. I decided to do the full witnessed test anyway.

Interviewer: How did that turn out?

Participant: It passed, but the value came in close to the required minimum, close enough that I flagged it for monitoring going forward.

Interviewer: If you'd had the tenant's full SKU list before classifying the commodity, would you have done anything differently?

Participant: Probably, yeah. If I'd seen the plastics percentage upfront, I'd have leaned toward a more conservative classification from the start rather than defaulting to what I'd seen on similar jobs.

Interviewer: If there'd been no ongoing relationship with the building owner, do you think the value-engineering conversation would have gone differently?

Participant: Maybe. I'd like to think I'd have pushed harder on keeping the in-rack allowance, but I can't say for certain the outcome would've changed.

Interviewer: Looking back, is there a point where you'd make a different call given the same information you had at the time?

Participant: The classification, probably. Everything downstream followed from that first call, and I had the means to ask for more data before locking it in.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Incentive bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Satisficing",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Stereotyping",
        "occurrences": 1,
        "mechanism_constraint": null
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
        "mechanism": "Category-based inference about tenant storage hazard substituted for case-specific inventory verification",
        "affected_reasoning_operation": "Evidence-selection/classification during commodity classification",
        "evidence_source": "Similarity to two prior 3PL clients vs. absent tenant-specific SKU/packaging data",
        "distinctiveness_requirement": "Only stereotyping instance in the scenario; occurs solely at Decision Point 1 tied to classification, distinct from the Decision Point 2 satisficing instance which concerns density selection, not categorization."
      },
      {
        "instance_id": "sf_01",
        "bias": "Satisficing",
        "mechanism": "Premature stopping at the first code-minimum-satisfying design option instead of comparing configuration-specific alternatives",
        "affected_reasoning_operation": "Alternative-generation and comparison during hydraulic density/area selection",
        "evidence_source": "Multiple available density/area curve points and manufacturer guidance vs. schedule pressure",
        "distinctiveness_requirement": "Only satisficing instance in the scenario; occurs solely at Decision Point 2 tied to density/area selection, distinct from the Decision Point 1 classification act and the Decision Point 3 recommendation act."
      },
      {
        "instance_id": "ib_01",
        "bias": "Incentive bias",
        "mechanism": "Recommendation shaped by desire to preserve an ongoing multi-project client relationship rather than neutral risk weighing",
        "affected_reasoning_operation": "Selective emphasis in risk-tradeoff communication during value-engineering recommendation",
        "evidence_source": "Owner's budget request and pending future projects vs. unresolved classification-uncertainty risk from Decision Point 1",
        "distinctiveness_requirement": "Only incentive-bias instance in the scenario; occurs solely at Decision Point 3 tied to the value-engineering recommendation, distinct from the classification and density-selection acts at earlier decision points."
      }
    ],
    "intended_strength": [
      {"instance_id": "st_01", "bias": "Stereotyping", "strength": "subtle"},
      {"instance_id": "sf_01", "bias": "Satisficing", "strength": "subtle"},
      {"instance_id": "ib_01", "bias": "Incentive bias", "strength": "moderate"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Biased_3",
    "domain_id": "HE",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences spread one-per-bias across three distinct, mechanism-fitting decision points (Stereotyping at Decision Point 1 - classification; Satisficing at Decision Point 2 - density/area selection; Incentive bias at Decision Point 3 - value-engineering recommendation); Decision Point 4 (commissioning/sign-off) deliberately left free of intentional bias instances to serve as a non-biased comparison point and to avoid exceeding the two-instances-per-decision-point limit unnecessarily.",
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
