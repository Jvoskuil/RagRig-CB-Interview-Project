You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a confidential process-improvement debrief, not part of any disciplinary record. Okay to proceed?

Participant: Yes, that's fine.

Interviewer: Can you describe your role and what you were responsible for during this incident?

Participant: I'm the Environmental/Safety Compliance Officer at the plant. I own air permit compliance site-wide, including the Solvent Recovery Unit in Building 3. My job here was to figure out what was actually happening, decide what needed to be reported under our Title V permit, and try to keep the production line moving if that could be justified.

Interviewer: Walk me through what happened.

Participant: At 6:40 in the morning, a VOC sensor near the SRU tripped above the action threshold. At that point there was nothing else—no complaints, no other data. We'd had two drift-related false alarms on that same sensor array in the past month, so I flagged that as relevant background, but I didn't want to just assume drift and move on. I sent a technician out with a handheld meter right away rather than waiting to see if anything else developed. About half an hour later, the hotline got a call about a chemical smell near the fenceline, which raised the stakes. The handheld readings came back elevated but in a grey zone—not clearly over the limit. We were also mid-batch on a large customer order due in two days, so an unnecessary shutdown wasn't something anyone wanted. I talked it through with the production supervisor and we agreed to tighten our sampling interval and schedule a full continuous emissions monitoring pull within a short, defined window rather than letting it drift indefinitely or shutting down that same morning. That held for about two days until a contractor doing unrelated maintenance work flagged a data logger showing sustained high readings during that exact alarm window. That's when we moved to a fuller investigation. I pulled the three-year maintenance history, which showed gasket seep as the most common cause of past VOC events here by a wide margin. I was also aware of a valve failure at our sister plant in Ohio a couple weeks earlier—big fine, local news, we'd covered it in a corporate webinar—but I didn't want that one dramatic case to drive where we looked first. I prioritized the gasket line based on the site's own history, and separately scheduled a quick, low-cost check of the valve as a precaution, given how bad a valve failure would be if it did happen. The teardown confirmed a worn gasket seal, consistent with our historical pattern. From there I had to decide how to calculate cumulative emissions, since the outcome affected whether we crossed into reportable territory under our 24-hour notification clock, with the production deadline two days out.

Interviewer: Let's reconstruct the timeline a bit more precisely. What did you do in the first thirty minutes?

Participant: I looked at the alarm log, noted the drift history, but didn't stop there—I dispatched the technician immediately to get independent field data rather than waiting to see if the alarm cleared on its own.

Interviewer: And between the odor complaint and the teardown?

Participant: The handheld readings came in that same morning. Then it was about two days of tighter monitoring until the contractor flagged the data logger, which is what triggered the deeper investigation.

Interviewer: When did the teardown findings come in relative to your reporting decision?

Participant: Right before. Once the gasket was confirmed, I moved straight into the emissions calculation question.

Interviewer: Going back to that first decision—how did you decide not to just classify it as drift outright?

Participant: The drift history was real, and it made drift a reasonable starting hypothesis, but two false alarms in a month isn't the same as certainty. I didn't want to commit to an explanation before I had any field data to check it against, so getting the technician out immediately felt like the right way to test the hypothesis rather than just assume it.

Interviewer: What information sources did you weigh before deciding on the CEM data pull, and how did you land on timing?

Participant: I looked at the grey-zone handheld readings, the cost of a partial shutdown—about $40,000 a day—and the fact that a full data pull would take real analyst hours we didn't have a lot of slack for. I talked to the production supervisor about the batch schedule. Rather than treating it as an all-or-nothing choice, we tightened the interim sampling and locked in a specific date for the full pull, so we weren't just sitting on ambiguous data indefinitely.

Interviewer: What alternatives did you weigh when deciding where to start the physical inspection?

Participant: Gasket seep versus the valve. The maintenance log made the gasket the statistically obvious first stop—it's what's caused nearly every minor event here for three years. The Ohio case was in the back of my mind because the consequences there were so severe, so I added a quick valve check as a low-cost precaution, but I was explicit with the team that the log, not the Ohio story, was driving where we started.

Interviewer: What was your basis for the exceedance calculation methodology?

Participant: I compared both calculation approaches against the permit language and how we'd handled similar situations in past audits, and picked the one that held up best under that precedent.

Interviewer: How much time pressure did you feel at each stage?

Participant: It was there throughout, especially with the production deadline, but it didn't override any single step—it mostly meant we had to be efficient about sequencing rather than skipping analysis.

Interviewer: How confident were you at each stage, and what would have shifted that?

Participant: Early on, moderate confidence at best—drift was plausible but unproven. By the time the data logger turned up, confidence dropped further until the teardown gave us a physical answer. Clearer field readings on day one would have resolved a lot of that uncertainty sooner.

Interviewer: If the sensor drift history hadn't existed, would your initial response have gone differently?

Participant: Probably not dramatically—I still would have wanted field confirmation before classifying anything, though I might have dispatched with a bit more urgency from the start.

Interviewer: If you hadn't known about the Ohio incident, would your inspection order have changed?

Participant: Honestly, I don't think so. The maintenance log was doing the real work there; the Ohio case just justified adding a cheap secondary check.

Interviewer: Looking back, what single piece of information, if available earlier, would have most changed your approach?

Participant: The data logger readings from day one. Getting those immediately instead of two days later would have let us move to the teardown that much sooner.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Imaginability Bias",
        "occurrences": 0,
        "mechanism_constraint": "Must not appear; causal attribution at decision point 3 must be explicitly base-rate led with vivid-incident consideration clearly framed as a secondary, severity-based precaution rather than a driver of prioritization."
      },
      {
        "bias": "Ostrich effect",
        "occurrences": 0,
        "mechanism_constraint": "Must not appear; the CEM data pull decision at decision point 2 must show workload/risk-based reasoning, not avoidance of an unwelcome confirmatory finding."
      },
      {
        "bias": "Primacy Effect",
        "occurrences": 0,
        "mechanism_constraint": "Must not appear; the initial triage at decision point 1 must show active cross-checking before classification rather than anchoring on the first hypothesis."
      }
    ],
    "target_bias_names": ["Imaginability Bias", "Ostrich effect", "Primacy Effect"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Imaginability Bias", "requested_occurrences": 0 },
      { "bias": "Ostrich effect", "requested_occurrences": 0 },
      { "bias": "Primacy Effect", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IP_Biased_3",
    "counterfactual_variable": {
      "name": "Officer's recent exposure to a vivid comparable incident narrative (Ohio sister-plant valve failure) prior to causal-narrative construction",
      "original_state": "Officer attended a corporate webinar two weeks before the incident describing the Ohio valve failure",
      "changed_state": "Officer had no recent exposure to any vivid comparable incident narrative",
      "variables_to_hold_constant": [
        "Sensor alarm timing and drift history",
        "Community odor complaint",
        "Production deadline and shutdown cost figures",
        "Maintenance log base rates for gasket seep vs. valve failure",
        "Number and sequencing of decision points",
        "Difficulty level and word count target"
      ]
    },
    "scenario_id": "IP_Vocab_Control_3",
    "domain_id": "IP",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; per vocabulary_control condition rules, zero intended instances of all three named biases are planned. Domain vocabulary, structure, stakeholders, constraints, and four-decision-point sequencing are matched to the paired biased scenario IP_Biased_3, with each decision point rewritten to show proportionate, evidence-based reasoning in place of the biased mechanism it mirrors.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Setting, actors, and stakeholder roles",
      "Four-decision-point structure and sequencing",
      "Difficulty level (challenging)",
      "Emotional tone and time-pressure framing",
      "Technical vocabulary list",
      "Target word count range (1,215-1,485)",
      "Background facts: sensor drift history, Ohio webinar exposure, production deadline, staffing constraint"
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
