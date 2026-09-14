You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. Before we start, just to confirm—this is a confidential debrief for our internal process-improvement study, not part of any disciplinary or compliance record. Is that okay with you?

Participant: Yes, that's fine. I've done these before.

Interviewer: Great. Can you tell me your role and what your responsibilities were during this incident?

Participant: I'm the Environmental/Safety Compliance Officer at the plant. I own air permit compliance for the whole site, including the Solvent Recovery Unit in Building 3. During this event my job was to figure out what actually happened, decide what needed to be reported to the state, and keep production moving if I could justify it.

Interviewer: Walk me through what happened, starting from the beginning.

Participant: Sure. It started at 6:40 in the morning—a VOC sensor near the SRU tripped above the action threshold. Nothing else had happened yet, no complaints, nothing. We'd had two drift-related false alarms on that same sensor array in the past month, so that was fresh in my mind. My first read was that it was probably drift again. About half an hour later, before I'd done much else, the hotline got a call from someone near the fenceline complaining about a chemical smell. That obviously raised the stakes, so I sent a technician out with a handheld VOC meter. The readings he brought back were elevated, but not dramatically—kind of a grey zone, not clearly over the permit limit. We were also mid-batch on a large customer order due in two days, so a shutdown wasn't something anyone wanted to trigger without good reason. I decided to hold off on pulling the full continuous emissions monitoring data and just kept an eye on it with recalibration scheduled. That stayed the plan for about two days, until a contractor doing unrelated maintenance work noticed a data logger showing sustained high readings during that exact window. That's when I really dug in. I pulled the maintenance history, and separately, I was thinking about a valve failure that happened at our sister plant in Ohio—I'd just seen a corporate webinar on it two weeks earlier, big fine, made the local news. So initially my draft notes on the incident leaned toward a valve issue. Eventually the teardown showed it was actually a worn gasket seal, which is honestly the most common cause we've had here over the last few years. Once that was confirmed, I had to decide how to calculate the emissions and whether it crossed into reportable territory, given the permit's 24-hour notification clock and our production deadline.

Interviewer: Let's reconstruct that timeline a bit more precisely. What did you do in the first thirty minutes after the alarm?

Participant: I checked the alarm log, saw the drift history, and made a quick call that we'd treat it as probable drift and schedule recalibration for later in the shift. I didn't dispatch the field team immediately—that came after the odor complaint.

Interviewer: And between the odor complaint and the teardown, what new information came in, and when?

Participant: The field readings came in that same morning—inconclusive, as I said. Then nothing new for about two days until the contractor flagged the data logger. That's really what forced a fuller investigation.

Interviewer: When did the teardown findings become available relative to your draft report?

Participant: The teardown happened after I'd already started drafting my incident summary and had briefed the plant manager verbally on what I thought we were dealing with.

Interviewer: Let's go back to that very first decision—treating the alarm as probable drift. What cues drove that?

Participant: Mainly the history. We'd had two false alarms in a month from that same array, so drift felt like the obvious explanation. It was the first thing that made sense, and honestly once I had that in my head, the readings the technician brought back later didn't strike me as clearly contradicting it—they were ambiguous enough that I read them as consistent with drift rather than as a red flag on their own.

Interviewer: Did you consider the possibility of a real release before the odor complaint came in?

Participant: Not seriously, no. There was no other reason to at that point.

Interviewer: What information sources did you consult before deciding whether to pull the full CEM dataset, and which did you set aside?

Participant: I looked at the handheld readings and the recent drift history. I didn't pull the full continuous emissions monitoring data at that stage. I knew that was the more thorough option—it would have given us a much clearer picture—but our analyst time is tight, we're basically a two-person team, and a full data pull plus lab confirmation would have taken hours we didn't have with the production deadline looming. If it had come back showing an exceedance, we'd have been on a 24-hour reporting clock, which would have complicated the week considerably. So I told myself the grey-zone readings weren't conclusive enough to justify pulling everyone off other work yet.

Interviewer: What alternatives did you consider when drafting the incident narrative, and why did the Ohio incident come to mind?

Participant: I thought about gasket seep, which is genuinely our most common issue based on the maintenance log—three years of data point that way. But the Ohio valve failure was just very present for me. I'd sat through that whole webinar, seen the numbers, the fine, the news coverage. So when I started framing the draft report and thinking about where to send the inspection team first, the valve scenario is what I wrote down and what I asked maintenance to check first, even before the gasket line was inspected.

Interviewer: What was your basis for choosing the exceedance calculation methodology at the end?

Participant: Once the gasket was confirmed, I had two methodologies I could reasonably apply, and they gave different exceedance outcomes. I went through the permit language and the historical way we'd calculated similar events, and picked the one I felt was most defensible given how our last few audits went.

Interviewer: How much time pressure did you feel at each of these moments?

Participant: Constant, honestly. The production deadline was hanging over almost every decision, from the initial triage to whether to escalate.

Interviewer: How confident were you in your interpretation at each stage, and what would have made you less confident?

Participant: Early on, fairly confident it was drift—maybe too confident, looking back. By the time the data logger turned up, I was much less sure of anything. If the field readings that first morning had been sharper, either clearly high or clearly normal, that would have changed how much weight I put on the drift explanation.

Interviewer: If the sensor drift history hadn't existed, would your initial triage have gone differently?

Participant: Probably. Without that history I think I'd have dispatched the field team right away instead of waiting.

Interviewer: If you hadn't attended the webinar about the Ohio incident, do you think your investigation would have started elsewhere?

Participant: That's a fair question. I'd like to think the maintenance log would have driven it regardless, but I honestly can't rule out that the webinar shaped where I looked first.

Interviewer: Looking back, what single piece of information, if available earlier, would have most changed your approach?

Participant: The data logger readings from that first day. If I'd seen those immediately instead of two days later, I think the whole sequence would have moved faster and with less back-and-forth.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Imaginability Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as disproportionate causal-narrative weighting toward a vivid, recently recalled comparable incident over a statistically dominant base-rate cause, at decision point 3 only."
      },
      {
        "bias": "Ostrich effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as conscious deferral of an information-gathering step (full CEM pull/lab confirmation) motivated by avoidance of an unwelcome confirmatory finding, at decision point 2 only."
      },
      {
        "bias": "Primacy Effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an early-formed hypothesis anchoring interpretation of subsequently received, more ambiguous evidence, at decision point 1 only."
      }
    ],
    "target_bias_names": ["Imaginability Bias", "Ostrich effect", "Primacy Effect"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Imaginability Bias", "requested_occurrences": 1 },
      { "bias": "Ostrich effect", "requested_occurrences": 1 },
      { "bias": "Primacy Effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Primacy Effect" },
      { "instance_id": "cb_02", "bias": "Ostrich effect" },
      { "instance_id": "cb_03", "bias": "Imaginability Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Ostrich effect", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Imaginability Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "mechanism": "Early alarm-log-based drift hypothesis anchors interpretation of subsequent ambiguous field readings",
        "affected_reasoning_operation": "Initial hypothesis formation / subsequent evidence interpretation",
        "evidence_source": "Alarm log and sensor drift history reviewed within minutes of the alarm",
        "distinctiveness_requirement": "Distinct from cb_03 by occurring at first evidence encounter (drift history) rather than at narrative construction from a recalled external incident"
      },
      {
        "instance_id": "cb_02",
        "bias": "Ostrich effect",
        "mechanism": "Deliberate deferral of full CEM data pull/lab confirmation to avoid confirming a costly reportable exceedance",
        "affected_reasoning_operation": "Information-seeking behavior under threat of unwelcome confirmation",
        "evidence_source": "Grey-zone field VOC readings and known cost/reporting consequences of a confirmed exceedance",
        "distinctiveness_requirement": "Distinct from cb_01 and cb_03 in involving active avoidance of an available information-gathering action rather than misweighting evidence already in hand"
      },
      {
        "instance_id": "cb_03",
        "bias": "Imaginability Bias",
        "mechanism": "Vivid, recently recalled sister-plant valve-failure incident disproportionately shapes causal attribution over the statistically dominant gasket-seep base rate",
        "affected_reasoning_operation": "Causal attribution / hypothesis prioritization for incident narrative",
        "evidence_source": "Three-year maintenance log base rates versus recalled corporate webinar narrative",
        "distinctiveness_requirement": "Distinct from cb_01 by involving retrieval of an external, emotionally vivid memory to override base-rate statistical evidence, rather than anchoring on the first internally generated hypothesis"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Ostrich effect", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Imaginability Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
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
    "scenario_id": "IP_Biased_3",
    "domain_id": "IP",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (1, 2, 3) selected for mechanism fit and narrative realism; decision point 4 deliberately left free of intended bias instrumentation to serve as an undetermined control judgment within the same interview.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Setting, actors, and stakeholder roles",
      "Four-decision-point structure",
      "Difficulty level (challenging)",
      "Emotional tone and time-pressure framing",
      "Target word count range (1,215-1,485)"
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
