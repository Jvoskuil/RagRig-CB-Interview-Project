You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process-improvement purposes only, and I'll be asking you to walk me through a specific incident in detail. Can you tell me your role and how long you've been in it?

Participant: Sure. I'm a maintenance reliability engineer, been in this plant about eight years, and in reliability specifically for the last four. I cover rotating equipment mostly—pumps, compressors, some turbines.

Interviewer: Great. I want to focus on the recent situation with feedwater pump P-204. Can you walk me through what first told you something was wrong?

Participant: So this was the third bearing failure on P-204 in about five months. Each one roughly five to six weeks apart, which is not normal—this pump used to run a year or more between issues. I got the call from the control room that vibration alarms had tripped, and by the time I got out there the bearing housing was already running hot. We pulled the vibration spectrum and it showed both a thermal signature and some mechanical components, so it wasn't a clean single-cause picture right away.

Interviewer: What was your goal walking into that?

Participant: Get the pump back in service inside our outage window—we had 48 hours before production needed full output—and actually figure out why this keeps happening instead of just swapping the bearing again and hoping.

Interviewer: Can you reconstruct the sequence of what happened next?

Participant: First I pulled maintenance history on all three failures. Then I looked at who'd done the last PM—that was Marco, one of our newer techs, about six weeks before this failure. After that I looped in our vibration analyst to get a second opinion on the spectrum data. Once we had a working theory, I had to decide on an alignment approach, and in parallel we were sourcing a replacement bearing. Each of those steps fed into the next, and we were watching the clock the whole time.

Interviewer: Let's start with the root cause piece. What information did you have when you were trying to explain this third failure?

Participant: I had Marco's work order from the PM, and I noticed he'd used a slightly different locknut torque sequence than the guy who did the prior two PMs—not wrong exactly, just not identical to what I'd have done. I also knew our lubrication interval had been stretched from three months to four months a couple of quarters back, that was a corporate cost initiative. And I had the ambiguous vibration data.

Interviewer: How did you weigh those pieces of information against each other?

Participant: Honestly, the technique difference jumped out at me first. Marco's newer, he's still building his feel for these bigger pumps, and when I saw the different sequence I figured that was probably it—a slightly under- or over-torqued locknut can absolutely walk itself into a bearing failure over a few weeks. I flagged it in the RCFA as the primary contributing factor and had him redo that step with me watching next time.

Interviewer: Did you weigh the lubrication interval change the same way?

Participant: I noted it in the report, sure, but I didn't dig into it hard at that point. It felt like a secondary factor—we'd been running on that interval for a couple of quarters without an obvious spike in failures across the fleet, so my attention went to what was different about this specific failure, which was Marco's install.

Interviewer: What would have made you look harder at the interval instead?

Participant: If I'd pulled the records on the other two failures side by side right then, I'd have seen all three happened under that same extended interval, regardless of who did the install. I did eventually see that, just not at that first pass.

Interviewer: Let's move to the next decision—whether to add any extra monitoring before the next run. What was on the table?

Participant: Two options. Run it on the standard schedule, or add interim vibration checks partway through the run, maybe even shorten the run interval until we trusted the fix. The interim monitoring would've added a few hours to the outage.

Interviewer: What tipped you toward the standard schedule?

Participant: Time pressure was real—production wanted the pump back. But if I'm honest, part of my thinking was that we'd just had three failures in a row, and it felt like we were due for a clean run. Three bad ones back to back, statistically it seemed like the streak had to break at some point.

Interviewer: Was there anything in the failure data that supported that expectation specifically?

Participant: Not really, when you put it that way. Each failure had its own distinct cause—heat, then lubrication, then this install variance. They weren't linked to each other mechanically. I think I was reading the run of bad luck as meaning something about what came next, more than the data actually supported.

Interviewer: How confident were you in that call at the time?

Participant: Fairly confident, honestly. It felt intuitive in the moment.

Interviewer: Third decision point—the alignment work. What were you weighing there?

Participant: Our vibration analyst wanted a specialist in with the laser alignment rig, because we still weren't 100% sure if misalignment or thermal growth was the bigger driver. Problem was, the specialist and the laser tool weren't available for 24 hours, and that would've eaten deep into our window.

Interviewer: What made you decide to do it yourself instead?

Participant: I've done manual dial-indicator alignments on pumps like this dozens of times, going back years, generally with good results. I know how it should feel when the shaft's tracking right. So I told the team I'd handle it manually and we'd keep the outage on schedule.

Interviewer: Did anything give you pause about that approach specifically for this pump?

Participant: In hindsight, yes—the alignment tolerance standard for this bearing class has actually tightened since I first learned my manual method. My old technique was validated against a looser tolerance band. And we still didn't know for sure that misalignment was even the main driver versus thermal growth. But at the time I was pretty confident my hands-on feel would get it close enough.

Interviewer: Last decision—the bearing part itself. What were the two options?

Participant: Reorder the same legacy bearing we've always used, or install the OEM's newer sealed-bearing housing. The legacy part has a known pattern—it's not great, failures roughly every five to six weeks under current conditions, but at least we know exactly what we're dealing with. The OEM upgrade is supposedly more reliable, but their literature was vague—no actual failure-rate numbers for our application, just general claims.

Interviewer: What drove your final choice?

Participant: The lack of hard numbers on the OEM side bothered me. I didn't want to swap in something with an unclear track record during a tight outage when I at least understood the legacy part's behavior, even if it wasn't good behavior. So we reordered the same bearing.

Interviewer: Looking back, how do you weigh that against the fact that the legacy part's known performance was already failing every five to six weeks?

Participant: When you say it like that, it does sound strange to stick with something I know is inadequate over something that might be better just because I couldn't quantify the "might." I think not having a number to point to made it feel riskier than it maybe was.

Interviewer: If the lubrication interval had never been extended, do you think this would have played out differently?

Participant: Probably—less thermal stress, maybe none of the three failures happen the way they did. Hard to know for sure with the sample we have.

Interviewer: If the OEM had given you a specific failure-rate figure, would that have changed your bearing decision?

Participant: Possibly. If they'd said something like a documented multiple-of-improvement over our legacy MTBF, I think I'd have pushed harder to make the schedule work for the upgrade.

Interviewer: Anything you'd do differently if this came up again?

Participant: I'd probably pull the full failure history side by side earlier, before settling on a cause. And I'd think twice about doing the alignment myself if the tolerance standard has moved since I last checked my technique against it.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Fundamental Attribution Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dispositional attribution (Marco's character/skill) overriding an available situational cause (lubrication interval change) at decision point 1 only."
      },
      {
        "bias": "Gambler's Fallacy",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as treating independent failure events as sequentially dependent ('due for a clean run') at decision point 2 only."
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overestimating personal skill's ability to determine a diagnostically uncertain outcome at decision point 3 only."
      },
      {
        "bias": "Ambiguity effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as avoidance of the option with unknown/ambiguous probability information in favor of a known-but-worse option at decision point 4 only."
      }
    ],
    "target_bias_names": [
      "Fundamental Attribution Bias",
      "Gambler's Fallacy",
      "Illusion of control",
      "Ambiguity effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Fundamental Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Gambler's Fallacy", "requested_occurrences": 1 },
      { "bias": "Illusion of control", "requested_occurrences": 1 },
      { "bias": "Ambiguity effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias" },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy" },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control" },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias", "decision_point": 1 },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy", "decision_point": 2 },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control", "decision_point": 3 },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "IP_Biased_4_FAB_01",
        "bias": "Fundamental Attribution Bias",
        "mechanism": "Dispositional attribution of failure to Marco's personal technique/character rather than the shared situational lubrication-interval change.",
        "affected_reasoning_operation": "Causal attribution during root cause diagnosis",
        "evidence_source": "Maintenance PM record, lubrication interval change log",
        "distinctiveness_requirement": "Only intended instance of this bias; must not recur as a summary or outcome explanation later in the interview."
      },
      {
        "instance_id": "IP_Biased_4_GF_01",
        "bias": "Gambler's Fallacy",
        "mechanism": "Belief that a streak of independent failures makes the next outcome more likely to be favorable, absent any causal dependency.",
        "affected_reasoning_operation": "Prediction of near-term equipment reliability",
        "evidence_source": "Failure interval history, statistical independence of proximate causes across the three failures",
        "distinctiveness_requirement": "Must use failure-streak reasoning distinct from the attribution reasoning in decision point 1; no overlap in evidence source."
      },
      {
        "instance_id": "IP_Biased_4_IOC_01",
        "bias": "Illusion of control",
        "mechanism": "Overestimation of personal skill's capacity to guarantee a correct outcome despite unresolved diagnostic uncertainty and tightened external tolerance standards.",
        "affected_reasoning_operation": "Selection of repair method and self-assessed confidence in outcome control",
        "evidence_source": "Specialist recommendation, current alignment tolerance standard, engineer's self-reported track record",
        "distinctiveness_requirement": "Distinct from ambiguity effect at decision point 4: this instance concerns confidence in personal action, not comparison of two probability-labeled options."
      },
      {
        "instance_id": "IP_Biased_4_AE_01",
        "bias": "Ambiguity effect",
        "mechanism": "Avoidance of the OEM option due to its unknown/ambiguous success probability, favoring a known-but-inferior legacy option.",
        "affected_reasoning_operation": "Choice between two repair options under differing information quality",
        "evidence_source": "OEM vendor claims (no specific failure-rate data), legacy bearing's documented failure history",
        "distinctiveness_requirement": "Distinct from illusion of control at decision point 3: this instance concerns comparative evaluation of two options' probability information, not personal-control belief."
      }
    ],
    "intended_strength": [
      { "instance_id": "IP_Biased_4_FAB_01", "bias": "Fundamental Attribution Bias", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_GF_01", "bias": "Gambler's Fallacy", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_IOC_01", "bias": "Illusion of control", "strength": "subtle" },
      { "instance_id": "IP_Biased_4_AE_01", "bias": "Ambiguity effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IP_Biased_4",
    "domain_id": "IP",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per bias assigned to a distinct decision point (1:1 mapping across the four decision points), selected for mechanism fit and narrative realism per allocation rules 1-4; no decision point received more than one bias instance, so the shared-decision-point distinctiveness rule was not triggered.",
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
