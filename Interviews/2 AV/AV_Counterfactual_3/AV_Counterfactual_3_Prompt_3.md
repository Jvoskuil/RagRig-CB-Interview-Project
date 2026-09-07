You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just so you know, I'll ask you to walk through a specific turnaround and explain your thinking as it unfolded, not just what ended up happening. Can you tell me your role and a bit about your background?

Participant: Sure. I've been a load controller about nine years, mostly narrow-body combi work. Normally I build the load sheet, issue the loading instruction to the ramp, check weight and balance against structural limits, and finalize the NOTOC for the captain. This one wasn't a normal turn, though—the inbound aircraft came in late, so instead of our usual 45 minutes on the ground, we were looking at more like 30 before the slot.

Interviewer: How did that change things going in?

Participant: Right away I knew I'd be compressing steps I'd normally spread out a bit more. Nothing about the flight itself was unusual—same route, same aircraft type—it was just less time to work with.

Interviewer: Walk me through what happened.

Participant: I got the cargo manifest with about 30 minutes left. Mixed load—regular bags, some mail, and one item that stood out: a piece of machinery, irregular shape, heavier than what typically goes through, not palletized. Our load-control software generates an automatic load instruction, and it put that machinery item into hold 3. That system's been reliable for this fleet for as long as I've used it, and with the clock already working against us, I issued the ALI to the ramp basically as generated so they could start loading immediately. About fifteen minutes later, the ramp called and said the aircraft was sitting slightly tail-heavy—not out of limits, just aft of where you'd expect.

Interviewer: What did you do with that?

Participant: Logged it and kept going, because right then an LMC came in—about 380 kilos of mail plus six late bags that missed the original manifest. That mail got assigned to hold 5, our aft bulk hold. With the time we had left, I looked at the total weight, saw it was in line with the LMCs we'd been getting all week on this route—three similar ones, same range, none of those needed redistribution—and cleared it on that basis so I could move to the trim sheet.

Interviewer: And the trim sheet itself?

Participant: I pulled the dispatch log for a quick check, given the tail-heavy call from the ramp. Saw the previous two flights on this same rotation—different tails, one to a different destination—had both needed aft trim corrections. With barely any time left before I had to finalize, that plus the ramp's report was enough for me to treat the rotation as running tail-heavy that day, so I shifted some cargo forward beyond what my own index actually required.

Interviewer: Let's go through each of those moments in more detail. Starting with the ALI and the machinery item—what specifically told you it was fine to run with as generated?

Participant: Mostly the system's history—it's been solid on this fleet for months. I did notice the item was irregular, not on a pallet, heavier than usual. That registered. But with only 30 minutes and the ramp already waiting, stopping to hand-verify felt like it would eat time I didn't have, so I went with what the system gave me.

Interviewer: Was there a manual chart you could have checked against for that kind of cargo?

Participant: There is, for exactly that situation. I know where it is. I just didn't reach for it that day.

Interviewer: What would have made you stop and pull it?

Participant: If we'd had the full 45, probably. Or if the system itself had thrown some kind of flag saying this needs manual sign-off. Neither of those happened, so I treated it like any other ALI.

Interviewer: On the LMC—what exactly did you compare when the mail and bags came in?

Participant: Total weight against what we'd seen from this week's other LMCs. That was the number I had on hand and could check fastest.

Interviewer: Did you look at where hold 5 sits relative to where those earlier LMCs went?

Participant: No, not specifically. The earlier ones went forward, into hold 2 I believe. This one went aft, into 5. I didn't run the index shift for that particular placement—the weight matched what I'd seen before, and with the time squeeze, that's what I used to clear it.

Interviewer: What would it have taken to run that calculation directly?

Participant: A few extra minutes at the trim computer. It wasn't unavailable to me. I just didn't think it was worth the time against the schedule we were on.

Interviewer: On the trim sheet redistribution—how did you connect the two previous flights to this one?

Participant: They were on the same rotation, back to back, and both needed aft correction. Two in a row felt like it meant something about how the rotation was running that day, so I built in a forward shift before signing off, and honestly, with the time we had left, I didn't feel like there was room to dig into it further.

Interviewer: What did your own calculated index for this flight show on its own?

Participant: It was fine—within the normal forward range with margin. The redistribution wasn't because my numbers were bad. It was more that seeing two prior aft trims made me not fully trust it, and I didn't have the minutes to sit with that discomfort.

Interviewer: Did you find out afterward why those two flights ran tail-heavy?

Participant: Yeah—one was a fuel imbalance, the other had extra catering loaded late. Different tails, unrelated causes. Nothing tying them to each other or to this flight.

Interviewer: Last one—the final sign-off. What was the situation?

Participant: Closeout figures looked clean, within limits. But the ramp tally was one bag short of the NOTOC and manifest. Small discrepancy, and the slot was closing faster than a normal turn would allow.

Interviewer: What did you decide, and what were you weighing?

Participant: I signed and released with the figures as they stood. I weighed the delay risk against a one-bag discrepancy that's usually just a miscount, not a safety concern by itself. It turned out to be a manifest correction afterward—the weight and balance conclusion didn't change. I can see someone holding a couple minutes to chase it down instead. Neither call feels obviously wrong to me.

Interviewer: How confident were you in each of these at the time, versus now?

Participant: The ALI and the LMC, fairly confident in the moment, more than I'd be now looking back. The trim redistribution, less sure even then—it felt like caution more than certainty. The sign-off, I'm still not positive I made the better call, but I don't think it was unreasonable given the time.

Interviewer: If you'd had the full 45 minutes instead of 30, would you have handled the machinery cargo differently?

Participant: Probably, yes. I think I'd have pulled the manual chart. The shorter window is what pushed me to just trust the system's history instead.

Interviewer: If the mail had gone to the usual forward hold instead of hold 5?

Participant: Then the weight comparison would've actually held up fine, since placement wouldn't have mattered as much. It was the aft location that made that comparison misleading, not the comparison itself.

Interviewer: If you'd known upfront the two prior tail-heavy events were unrelated, would you have redistributed the same way?

Participant: No. I'd have trusted my own numbers for this flight instead of layering in a correction based on two other tails.

Interviewer: Anything you'd do differently facing this same sequence again, under the same shortened window?

Participant: Pull the manual chart for anything irregular no matter how tight the clock is, and keep this flight's numbers separate from what happened on previous ones unless I actually know there's a shared cause. The LMC piece I'd still have to think through—weight alone wasn't the full story that day, and less time made that easier to miss, not harder.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Substitution bias", "occurrences": 1, "mechanism_constraint": "Must manifest as answering an easier proxy question (aggregate weight similarity) in place of the harder question (placement-specific index/moment impact) at decision point 2, with time scarcity cited as contributing justification." },
      { "bias": "Apophenia or Correlation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as inferring a causal recurring pattern from two temporally adjacent but causally unrelated trim events at decision point 3, with time scarcity cited as the reason further checking was skipped." },
      { "bias": "Automaticity or Automation Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as bypassing an independent manual check on an automated system output specifically for an atypical/non-standard case at decision point 1, with the compressed schedule cited as reinforcing justification." }
    ],
    "target_bias_names": [
      "Substitution bias",
      "Apophenia or Correlation Bias",
      "Automaticity or Automation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Substitution bias", "requested_occurrences": 1 },
      { "bias": "Apophenia or Correlation Bias", "requested_occurrences": 1 },
      { "bias": "Automaticity or Automation Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias" },
      { "instance_id": "sub_01", "bias": "Substitution bias" },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias", "decision_point": 1 },
      { "instance_id": "sub_01", "bias": "Substitution bias", "decision_point": 2 },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "au_01",
        "bias": "Automaticity or Automation Bias",
        "mechanism": "Skipping manual cross-check for irregular cargo based on general system reliability, reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Verification of system-generated output before action",
        "evidence_source": "ALI output plus known irregularity of the machinery cargo item plus stated 30-minute window",
        "distinctiveness_requirement": "Must be the only instance in the interview where a system output is accepted without a check specifically warranted by an atypical case; not repeated elsewhere."
      },
      {
        "instance_id": "sub_01",
        "bias": "Substitution bias",
        "mechanism": "Substituting an easier proxy question (weight similarity) for the harder question (placement-specific index impact), reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Evaluation of whether new evidence (LMC) requires full recalculation",
        "evidence_source": "LMC weight and placement data compared against historical LMC pattern, under stated time scarcity",
        "distinctiveness_requirement": "Must be the only instance where a harder quantitative question is answered via an easier proxy comparison; distinct from au_01 in that no automated system output is involved."
      },
      {
        "instance_id": "ap_01",
        "bias": "Apophenia or Correlation Bias",
        "mechanism": "Inferring a causal recurring pattern from two coincidental, causally unrelated prior events, reinforced by compressed schedule framing",
        "affected_reasoning_operation": "Causal attribution/generalization applied to override a current, independently valid computed value",
        "evidence_source": "Trim log history of two preceding flights on the same rotation, under stated time scarcity",
        "distinctiveness_requirement": "Must be the only instance involving inference of a causal pattern from a small historical sample; distinct from sub_01, which involves comparing current data to past data without asserting causality."
      }
    ],
    "intended_strength": [
      { "instance_id": "au_01", "bias": "Automaticity or Automation Bias", "strength": "subtle" },
      { "instance_id": "sub_01", "bias": "Substitution bias", "strength": "subtle" },
      { "instance_id": "ap_01", "bias": "Apophenia or Correlation Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": "AV_Biased_3",
    "counterfactual_variable": {
      "name": "Length of the turnaround window before the fixed departure slot",
      "original_state": "Routine 45-minute turnaround with no additional schedule compression",
      "changed_state": "Compressed ~30-minute turnaround due to a delayed inbound aircraft, same fixed departure slot",
      "variables_to_hold_constant": [
        "Cargo mix and weights, including the irregular machinery item",
        "LMC content, weight, and hold placement",
        "Rotation trim history and its two prior unrelated causes",
        "Aircraft type and route",
        "Actors and stakeholder roles",
        "ALI system behavior and its lack of a mandatory manual-check flag",
        "The final bag-count discrepancy and its resolution"
      ]
    },
    "scenario_id": "AV_Counterfactual_3",
    "domain_id": "AV",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Each of the three requested biases was assigned to exactly one distinct decision point (DP1, DP2, DP3), mirroring the allocation used in the paired base scenario AV_Biased_3, so that only the turnaround-window causal variable differs between the pair. Decision point 4 was deliberately left free of intended bias instances to preserve an ambiguous, non-mechanical outcome, consistent with the base scenario.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Cargo mix and weights, including the irregular machinery item",
      "LMC content, weight, and hold placement",
      "Rotation trim history and its two prior unrelated causes",
      "Aircraft type and route",
      "Actors and stakeholder roles",
      "ALI system behavior and its lack of a mandatory manual-check flag",
      "The final bag-count discrepancy and its resolution"
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
