You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process-review purposes, and it's fine to speak candidly about decisions, including ones that didn't pan out the way you expected. Can you start by telling me your role and how you got pulled into the micro-pitting issue on the anodizing line?

Participant: Sure. I'm the process engineer responsible for surface treatment qualification on new equipment. I got pulled in when QA flagged intermittent pitting on aluminum brackets coming off the new anodizing line — this was about three weeks before a customer PPAP submission, so there wasn't a lot of slack in the schedule.

Interviewer: Walk me through what happened when you were first assigned.

Participant: The first thing on my desk that morning was a handoff note from the night-shift operator saying the bath temperature had spiked overnight and he suspected that was causing the pitting. That made immediate sense to me — anodizing bath temperature is a classic culprit for pitting, it's easy to check, and it fit a story I could act on right away. So I started there. I pulled the chiller maintenance history and had our tech verify the temperature controller. There was actually a short rectifier-log summary sitting in the same folder that flagged a calibration deviation from a few days earlier, but I didn't open it that week — the temperature story was already the frame I was working from, so the chiller took priority and the rectifier note just sat there.

Interviewer: What was your objective at that point?

Participant: Just to stop the bleeding — figure out the root cause fast enough that we could run a clean trial lot and still hit the PPAP window.

Interviewer: Let's reconstruct the timeline a bit before we get into specifics. What information did you have on day one versus what came later?

Participant: Day one, I had the operator's note, the unopened rectifier summary, and a defect-rate report showing day-shift batches were pitting more than night-shift batches. Coil certs also existed but I hadn't reviewed them. Within about a day we fixed the chiller and temperatures stabilized. But pitting didn't disappear — it dropped, but a low rate persisted. That told me temperature wasn't the whole story. From there we moved into looking at the dosing system, since the residual defect pattern looked more like a chemistry consistency issue.

Interviewer: When you saw that day-shift batches had a higher defect rate than night-shift, what was your read on that?

Participant: Honestly, my first instinct was that the day-shift operator was less careful — he's newer, and I'd noticed him rushing rack loading a couple times. I flagged it in my notes as a contributing factor. Looking back, I didn't spend much time asking whether the equipment was in worse condition during the day, or whether the chemistry itself might drift over the course of a shift. I focused on him.

Interviewer: Did you consider other explanations for that gap?

Participant: Not seriously at the time, no. It seemed like a reasonably clean explanation given what I'd observed of him.

Interviewer: Let's move to the second decision — selecting a corrective dosing technology. What were you weighing?

Participant: Once we knew residual pitting was chemistry-related, we needed a better dosing control system. There were two options. Vendor A had an automated retrofit already running at three of our sister plants. Vendor B had a newer inline sensor-based system with a stronger spec sheet on paper — actually stronger on the sensing and control criteria we cared about most — but only one reference installation, and their documentation was thin, with gaps in the install manual and unclear commissioning steps.

Interviewer: How did you decide between them?

Participant: I called a couple of engineers at sister plants, and they were generally happy with Vendor A — three plants running it gave me some confidence it was a known quantity. We'd started a requirement-by-requirement comparison of the two systems, and early on it was actually tilting toward Vendor B on the technical side. But once I had three sister plants confirming Vendor A worked, that was enough for me — I didn't finish walking through the rest of the comparison. Vendor B's applications engineer even offered to walk us through the open commissioning questions, and there wasn't any identified incompatibility, but the unresolved gaps still felt less acceptable to me than Vendor A's familiar unknowns, so I didn't take him up on it.

Interviewer: Did anything about Vendor A's track record give you pause?

Participant: One of the three plants had reported mixed results with it. I knew that going in. But with three plants running it versus one incomplete installation elsewhere, it felt like the safer bet.

Interviewer: What happened after installation?

Participant: Retrofit went in within three days. First two batches still showed minor pitting, which was a little concerning. Then the next five batches came back completely clean.

Interviewer: What was your interpretation of that pattern?

Participant: Honestly, after those two rough batches, having five clean ones in a row felt like the process had settled the score — like whatever bad luck or instability had been in the system early on had been used up, so another rough batch felt a lot less likely right then. I remember telling the quality manager the odds of another bad one showing up were pretty low, given the run we'd had.

Interviewer: Did you complete the full SPC sample size that's normally recommended before declaring a process stable?

Participant: No, we hadn't hit the full sample yet. We started prepping the certification paperwork in parallel because the timeline demanded it, not because I was ready to call the process stable — I was still treating that call as open. The streak affected my gut read more than it should have, but the certification-prep timing itself was really about the calendar.

Interviewer: Was there anything else happening during that same window that could have contributed to the improvement?

Participant: There was a routine bath chemistry replenishment scheduled in there too. But honestly, I attributed most of the turnaround to the manual rectifier voltage adjustments I was making between runs — small tweaks based on how the previous batch looked. I felt like I was actively steering it back into spec. I never really separated the two effects out.

Interviewer: That leads to the final decision — signing off for PPAP. What did that process look like?

Participant: We had a full two-week trial dataset with real variability in the earlier lots, and then a final validation lot the day before the deadline that came back completely clean. The customer SQE needed the sign-off memo within 24 hours.

Interviewer: How did you weigh the earlier variability against that final lot?

Participant: The final lot was really what tipped my confidence. It was the cleanest result we'd seen, run right before submission, so it felt like the truest picture of where the process actually stood. I referenced the earlier trial data in the memo, but the final lot carried most of the weight in my recommendation to certify.

Interviewer: Was there any other data available at that point, like the Cpk finding from the independent audit?

Participant: There was a marginal Cpk result from a quality audit, yes, but it had been filed separately from the sign-off packet, so it wasn't front and center when I was writing the recommendation.

Interviewer: Under less time pressure, would you have handled that differently?

Participant: Maybe. I think I would have pulled that Cpk data into the memo directly rather than letting the last lot speak for itself.

Interviewer: Let me ask a couple of hypotheticals. If you'd reviewed the rectifier calibration logs before the operator's temperature note, do you think the investigation would have unfolded differently?

Participant: Possibly — if the rectifier deviation had been the first thing in front of me, I probably would have chased that first instead of the chiller. It's hard to say which one I'd have found more compelling, but the order I got things in definitely shaped where I looked first.

Interviewer: And if that final validation lot had shown pitting instead of coming back clean?

Participant: Then I'd have had to delay and either extend the deadline or issue something conditional. It would have forced a harder look at the full dataset rather than leaning on one result.

Interviewer: Looking back, is there anything about how you weighed the evidence you'd reconsider?

Participant: Probably how much credit I gave myself for the manual adjustments versus the chemistry replenishment — I never really separated those out. And I'd want to revisit that attribution I made about the day-shift operator; I never fully ruled out equipment or process factors there. I'd also go back and actually open that rectifier summary on day one instead of letting the first explanation carry the week. Otherwise, given the time we had, I think the calls were defensible.

Interviewer: That's a helpful place to stop. Thanks for walking through this in detail.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Primacy Effect", "occurrences": 1, "mechanism_constraint": "Must manifest as disproportionate weighting of the first-received diagnostic explanation over later-arriving evidence." },
      { "bias": "Fundamental Attribution Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as personal/dispositional attribution for a performance gap where situational factors are also plausible and available." },
      { "bias": "Gambler's Fallacy", "occurrences": 1, "mechanism_constraint": "Must manifest as treating independent sequential batch outcomes as statistically compensatory." },
      { "bias": "Illusion of control", "occurrences": 1, "mechanism_constraint": "Must manifest as overattributing a process outcome to personal manual intervention over a concurrent uncontrolled factor." },
      { "bias": "Ambiguity effect", "occurrences": 1, "mechanism_constraint": "Must manifest as avoidance of an option due to unclear/incomplete information despite favorable known attributes." },
      { "bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "Must manifest as decision weighting driven by peer/prevalence adoption rather than independent technical evaluation." },
      { "bias": "Recency effect", "occurrences": 1, "mechanism_constraint": "Must manifest as overweighting the most recently obtained result relative to the fuller historical dataset in a final judgment." }
    ],
    "target_bias_names": [
      "Primacy Effect",
      "Fundamental Attribution Bias",
      "Gambler's Fallacy",
      "Illusion of control",
      "Ambiguity effect",
      "Bandwagon effect",
      "Recency effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Primacy Effect", "requested_occurrences": 1 },
      { "bias": "Fundamental Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Gambler's Fallacy", "requested_occurrences": 1 },
      { "bias": "Illusion of control", "requested_occurrences": 1 },
      { "bias": "Ambiguity effect", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Recency effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Primacy Effect" },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias" },
      { "instance_id": "cb_03", "bias": "Ambiguity effect" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect" },
      { "instance_id": "cb_05", "bias": "Gambler's Fallacy" },
      { "instance_id": "cb_06", "bias": "Illusion of control" },
      { "instance_id": "cb_07", "bias": "Recency effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias", "decision_point": 1 },
      { "instance_id": "cb_03", "bias": "Ambiguity effect", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "decision_point": 2 },
      { "instance_id": "cb_05", "bias": "Gambler's Fallacy", "decision_point": 3 },
      { "instance_id": "cb_06", "bias": "Illusion of control", "decision_point": 3 },
      { "instance_id": "cb_07", "bias": "Recency effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Primacy Effect",
        "mechanism": "Disproportionate weight given to the first-received explanation (temperature-spike report) over later-reviewed rectifier/material evidence.",
        "affected_reasoning_operation": "Hypothesis prioritization at investigation start",
        "evidence_source": "Order of arrival of diagnostic reports",
        "distinctiveness_requirement": "Must be distinguished from cb_02 by relying on order-of-information-receipt rather than personnel-performance data."
      },
      {
        "instance_id": "cb_02",
        "bias": "Fundamental Attribution Bias",
        "mechanism": "Attribution of a shift-level defect-rate gap to operator personal traits rather than situational/process factors.",
        "affected_reasoning_operation": "Causal attribution of personnel performance difference",
        "evidence_source": "Defect-rate comparison report between shifts",
        "distinctiveness_requirement": "Must be distinguished from cb_01 by relying on personnel-performance comparison data at a different moment in the same decision point."
      },
      {
        "instance_id": "cb_03",
        "bias": "Ambiguity effect",
        "mechanism": "Rejection of a technically favorable option specifically because of incomplete/unclear documentation.",
        "affected_reasoning_operation": "Option elimination under incomplete information",
        "evidence_source": "Vendor B documentation completeness and spec sheet",
        "distinctiveness_requirement": "Must be distinguished from cb_04 by focusing on documentation clarity for the rejected option, not peer adoption of the chosen option."
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "mechanism": "Vendor selection driven by peer/sister-plant prevalence rather than independent technical merit.",
        "affected_reasoning_operation": "Vendor selection weighting",
        "evidence_source": "Informal peer engineer endorsements and sister-plant adoption count",
        "distinctiveness_requirement": "Must be distinguished from cb_03 by relying on peer-adoption evidence for the chosen option, not documentation ambiguity of the rejected option."
      },
      {
        "instance_id": "cb_05",
        "bias": "Gambler's Fallacy",
        "mechanism": "Sequential independent batch outcomes treated as statistically self-correcting ('due' for good results).",
        "affected_reasoning_operation": "Probabilistic interpretation of outcome sequence",
        "evidence_source": "Chronological batch outcome log",
        "distinctiveness_requirement": "Must be distinguished from cb_06 by relying on the sequence/count of batch outcomes, not on causal credit for a specific intervention."
      },
      {
        "instance_id": "cb_06",
        "bias": "Illusion of control",
        "mechanism": "Overattribution of process stabilization to personal manual voltage adjustments over a concurrent uncontrolled factor (chemistry replenishment).",
        "affected_reasoning_operation": "Causal credit assignment for outcome with confounded personal and external factors",
        "evidence_source": "Engineer's own process-log annotations and concurrent replenishment record",
        "distinctiveness_requirement": "Must be distinguished from cb_05 by relying on personal-action attribution rather than sequence-based probability reasoning."
      },
      {
        "instance_id": "cb_07",
        "bias": "Recency effect",
        "mechanism": "Overweighting of the most recent validation lot relative to the full two-week trial dataset in the final certification judgment.",
        "affected_reasoning_operation": "Evidence weighting in final go/no-go judgment",
        "evidence_source": "Comparison of final lot result versus full trial-lot dataset",
        "distinctiveness_requirement": "Single instance; distinguished from earlier decision points by occurring only in the final sign-off judgment, not during trial monitoring."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Primacy Effect", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Ambiguity effect", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Gambler's Fallacy", "strength": "subtle" },
      { "instance_id": "cb_06", "bias": "Illusion of control", "strength": "moderate" },
      { "instance_id": "cb_07", "bias": "Recency effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Order in which diagnostic evidence sources were reviewed at the start of the investigation",
      "original_state": "Operator's temperature-spike report reviewed first",
      "changed_state": "Rectifier calibration logs reviewed first",
      "variables_to_hold_constant": [
        "Underlying true root cause(s) of the micro-pitting defect",
        "Deadline pressure and PPAP audit timing",
        "Vendor options and their documentation quality",
        "Batch outcome sequence during trial runs",
        "Personnel and stakeholder roles"
      ]
    },
    "scenario_id": "IP_Biased_7",
    "domain_id": "IP",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across 4 decision points with a maximum of two distinct biases co-located per decision point (DP1: cb_01/cb_02, DP2: cb_03/cb_04, DP3: cb_05/cb_06, DP4: cb_07 alone); no bias assigned more than one instance total, so intra-bias separation rules were not triggered; co-located instances at the same decision point use distinct evidence sources and reasoning operations per instance as documented in intended_mechanisms.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Underlying true root cause(s) of the micro-pitting defect",
      "Deadline pressure and PPAP audit timing",
      "Vendor options and their documentation quality",
      "Batch outcome sequence during trial runs",
      "Personnel and stakeholder roles"
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
