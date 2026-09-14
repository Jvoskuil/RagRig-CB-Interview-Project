You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific inspection you handled, purely for understanding how you approached the decisions — not an audit of your conclusions. That okay with you?

Participant: Sure, no problem. I've got the file pulled up if I need to check dates.

Interviewer: Great. Can you give me your role and a bit of background first?

Participant: I'm a fire inspector, been doing building code compliance for about nine years now, mostly commercial and mixed-use properties. This particular case was an annual re-inspection tied to a certificate of occupancy renewal for a three-story building — retail on the ground floor, offices above. They'd just finished a tenant fit-out renovation, so the stakes were a little higher than a routine annual check.

Interviewer: Walk me through what happened, from arrival to wrap-up.

Participant: I got there in the morning, met the building manager — I've worked with him for probably four years across different properties he's managed. Good guy, very responsive, easy to deal with. The building was operating normally, tenants open, so I had to work around foot traffic in a few spots. First thing I did was the egress corridors. Near the loading dock there's a secondary egress path, and I found it partially narrowed by stacked delivery pallets. He told me it was just for that morning's delivery. I measured it anyway — clear width was under the code minimum with the pallets there. I wrote that up as a formal minor violation with a short correction window, regardless of what he said about the timing. Later, actually, one of the retail staff mentioned in passing that the pallets had been sitting there off and on for a couple weeks, not just that morning. Didn't change my classification, but it stuck with me.

Then we went up to check the secondary stairwell door. That's when I found the self-closing device disconnected — the arm was just hanging loose. That's a meaningful finding; a fire door that won't close on its own defeats the whole point of the assembly during smoke or fire conditions. He was pretty apologetic about it, said maintenance had already been told about it the week before, and he offered to have someone reattach it right then while I was standing there.

Interviewer: And the alarm system?

Participant: Right, that was next. I pulled the monthly test log and there was a gap — one month with nothing recorded. He said the test had definitely happened, it just hadn't been logged properly. I didn't take that at face value. I asked for the monitoring company's records instead of just accepting the verbal explanation, and I flagged the gap as an open documentation item pending that verification rather than closing it out.

Interviewer: Let's go through each of those decisions in a bit more detail, starting with the pallets. What made you decide to formally cite that instead of just noting it informally?

Participant: The corridor width is objective — I measured it, it was under the minimum, full stop. Doesn't matter what the explanation is for why it's narrow. That one felt straightforward to me; the measurement does the talking.

Interviewer: And the door closer — how did you land on an advisory note instead of a formal citation, given you just described it as a meaningful life-safety item?

Participant: Yeah, that one I went back and forth on a bit. Technically, sure, it's a significant deficiency — no-questions-asked at the code level. But he was really upfront about it, apologized a couple times, said his team already knew and it just hadn't been actioned yet, and he wanted to fix it right there in front of me. After four years of him being straight with me on other properties, going in hard with a formal citation over something he was already fixing on the spot felt like more friction than the moment called for. So I logged it as an advisory note instead — get it corrected, follow up next visit, no formal paperwork trail.

Interviewer: Did you check the maintenance ticket he referenced, or look at whether this had come up before at that building?

Participant: Not in the moment, no. I didn't pull the ticket timestamp, and I didn't cross-check last year's report right there. In hindsight I probably should have — turned out the ticket was only logged that morning, not the week before like he said, and there'd actually been a near-identical closer issue flagged and marked corrected in last year's inspection. So it wasn't new, it was a repeat. I didn't know that at the time I made the call, though.

Interviewer: What was going through your mind that made the apology and the offer to fix it feel like enough?

Participant: Honestly, it just felt like the reasonable, low-friction way to handle it with someone who's generally cooperative. I wasn't thinking about whether it had happened before — I was thinking about the guy standing in front of me being embarrassed about it and already moving to fix it. Writing him up formally in that moment felt like it would've been an unnecessarily hard line to take.

Interviewer: Third decision — the alarm log gap. Why request outside verification there but not for the door closer?

Participant: Different kind of claim, I think. "The test happened but wasn't logged" is something I can actually check against a third party — the monitoring company has their own records independent of him. There's no equivalent independent record for a closer that's already been reattached; once it's fixed, the evidence is gone. So partly it was about what was still verifiable versus what wasn't.

Interviewer: Fourth decision — writing the final recommendation. How did you weigh the three findings together?

Participant: I recommended conditional renewal — correct the pallet obstruction, get the alarm verification resolved, and monitor the door closer as an open advisory item. My supervisor actually pushed back a little, asked why the closer wasn't a formal citation given the classification. I explained the on-site correction and the manager's responsiveness. He wasn't fully satisfied but didn't override it. The manager also messaged me afterward thanking me for being reasonable during the visit.

Interviewer: What information, if you'd had it at the time, would have changed your call on the door closer?

Participant: Knowing it was a repeat finding from last year would have changed things for sure — that's a pattern, not a one-off. If I'd pulled that file before finalizing the note instead of after, I think I'd have citied it formally.

Interviewer: If the manager had reacted differently — say, defensively or dismissively instead of apologetically — do you think your classification would have been different?

Participant: Probably, yeah. If he'd pushed back or acted like it wasn't a big deal, I think I'd have gone straight to a formal citation without much hesitation. The fact that he was already owning it and fixing it changed how I approached writing it up.

Interviewer: Looking back, is there a point where you'd want more information before deciding again?

Participant: The closer, for sure. I'd want the maintenance ticket pulled and last year's report checked before I finalize any classification, not after.

Interviewer: Anything you'd tell a newer inspector handling a similar situation with a cooperative, familiar contact?

Participant: Probably to separate the paperwork from the personal read on the guy. The relationship can tell you how a conversation's going to go, but it shouldn't really be what decides the classification — the classification should hold up the same whether the person in front of you is anxious about it or not.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Courtesy Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a softened severity classification tied to interpersonal politeness toward a specific stakeholder at one decision point, not as a general disposition or repeated behavior."
      }
    ],
    "target_bias_names": [
      "Courtesy Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Courtesy Bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "mechanism": "Downgrading a life-safety-significant fire door closer deficiency from a formal citation to an informal advisory note in direct response to the building manager's apologetic, relationship-invoking demeanor, without independently re-verifying the maintenance ticket timeline or prior-year recurrence.",
        "affected_reasoning_operation": "Severity classification / risk categorization judgment under interpersonal pressure",
        "evidence_source": "In-person interaction with the building manager (apology, reassurance, appeal to cooperative history) combined with an unverified maintenance-ticket claim",
        "distinctiveness_requirement": "This is the sole instance; no other decision point may contain a second softened classification driven by interpersonal courtesy toward any stakeholder."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "cb_01",
        "bias": "Courtesy Bias",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Building manager's interpersonal demeanor during the door-closer finding",
      "original_state": "Apologetic, cordial, relationship-invoking response from the manager",
      "changed_state": "Neutral or defensive response with identical factual content",
      "variables_to_hold_constant": [
        "Underlying technical deficiency and code classification standard",
        "Time pressure and same-day deadline",
        "All other decision points and findings",
        "Building type, layout, and renovation context"
      ]
    },
    "scenario_id": "HE_Biased_1",
    "domain_id": "HE",
    "total_requested_occurrences": 1,
    "total_planned_occurrences": 1,
    "allocation_rule_used": "Single occurrence assigned to the decision point with the strongest mechanism fit (interpersonal interaction during a severity-classification judgment); no splitting needed since occurrences=1.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Underlying technical deficiency and code classification standard",
      "Time pressure and same-day deadline",
      "All other decision points and findings",
      "Building type, layout, and renovation context"
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
