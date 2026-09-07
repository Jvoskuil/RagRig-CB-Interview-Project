You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a routine case-review interview for our lab's cognitive task analysis project — we're documenting how analysts actually reason through casework, not evaluating your performance. Everything's de-identified before it goes anywhere. Okay if we record and talk through a recent case?

Participant: Sure, that's fine. Which case did you want to walk through?

Interviewer: The windowsill swab from the burglary-assault — the one that went to a bail hearing a few months back. Can you start by telling me how it landed on your bench?

Participant: It came in as a rush request. Patrol had picked up a guy about two blocks from the house maybe forty minutes after the call came in — broken window, homeowner had a cut on his arm from being shoved into a doorframe during the break-in. The detective's submission note said the suspect had a prior burglary conviction and that he was, in his words, "almost certainly good for it." The swab itself was blood and touch DNA off the broken windowsill glass. Quantity came back under 100 picograms on quant, so I knew going in this was going to be a low-template situation — lots of stochastic effects, peak height imbalance, that kind of thing.

Interviewer: What was your objective at that point?

Participant: Determine whether the suspect could be included as a contributor to that mixture, generate a likelihood ratio if the data supported one, and get a technically defensible report out. We had a 24-hour turnaround because the DA wanted it ahead of the bail hearing. And logistically, my supervisor was the only technical reviewer available that week, so whatever I produced, she'd be the one signing off, fast.

Interviewer: Let's reconstruct the sequence. What happened first?

Participant: I pulled the case file to set up my analysis parameters — stochastic threshold, amplification target, all standard. Before I got to the profile itself, I read through the detective's cover note and the submission form, which already had the suspect's name and known profile listed. Then I ran the amplification. Came back partial — several peaks near the stochastic threshold, which is typical for that DNA quantity. I built out the allele table, flagged the ambiguous loci, and moved into the comparison stage. A few days later the victim called back and mentioned an ex-boyfriend had been in the house three days before the break-in, and a delivery driver had been at the door earlier that week. That complicated the elimination picture, since we'd only swabbed the homeowner. I finished the report and sent it up for technical review the night before the hearing.

Interviewer: Let's slow down at that first step — reading the file before setting up the analysis. Walk me through what was going through your mind.

Participant: Honestly, it's just how intake works. You read the submission form, you see what the detective knows, you set your parameters. The note stood out because it was pretty confident — "found two blocks away," "almost certainly good for it." I remember thinking, okay, this is probably him, let's see if the DNA backs that up. So when I sat down with the electropherogram, I was looking at it as, does this data support what we've already got on this guy, rather than starting cold and asking who could this mixture belong to.

Interviewer: Did you consider setting parameters before reading the narrative part of the note?

Participant: Not really — the form comes as one packet. I suppose I could've separated the suspect information from the case narrative and looked at the profile blind first, then compared. I didn't do that here. In hindsight I'm not sure it would've changed the amplification parameters themselves, but it probably shaped how I was thinking about the comparison before I even looked at a single peak.

Interviewer: Let's go to the electropherogram itself. What did you see, and how did you write it up?

Participant: There were several loci where the peaks lined up cleanly with the suspect's known profile, right where you'd expect them, above threshold. I spent a good amount of time on those — peak heights, confirming they weren't stutter, checking the ratios. But there were also two loci where alleles I'd have expected from him were missing or sitting below threshold, and one locus had an extra peak I couldn't immediately place. Those went into the notes, but more as a line — "inconclusive due to low template" — rather than something I dug into the way I dug into the matching loci.

Interviewer: What made you treat those differently?

Participant: Partly it's just efficiency — the matching loci are easy to describe, they're clean. The missing and extra peaks are messier, and with low-template DNA, you do get dropout and occasional artifact peaks, so logging them as inconclusive isn't unusual practice. But if I'm being honest, I probably gave the matching data more narrative attention because it was doing more work for the story I was building, and the messy stuff got less airtime, not because it was less real.

Interviewer: Later, the victim mentions two other people who'd been in the house. What did you do with that?

Participant: That came in after I'd already built most of the comparison. We only had the homeowner's elimination sample at that point. I flagged internally that the ex-boyfriend and delivery driver were unsampled, but I didn't request rush swabs from either of them. Partly that's the deadline — the hearing was the next morning, there wasn't time to get new elimination samples processed. But I also remember thinking the suspect profile already fit well enough that chasing two more elimination samples felt like it would just confirm what we already had.

Interviewer: How did you weigh the suspect-inclusion hypothesis against those alternative sources?

Participant: I accepted the suspect as a plausible contributor based on the partial match we had — I didn't require additional testing to feel comfortable with that. For the ex-boyfriend or the driver, though, my instinct was that without their samples, there was no real basis to seriously entertain them, so I treated that as an open question for someone else to chase, not something that needed to hold up the report. Looking back, I didn't apply quite the same bar to both sides — the suspect got in on a partial match, but the alternatives needed a full sample before I'd take them seriously at all.

Interviewer: Is there a version of this where you'd have paused the report instead?

Participant: If the deadline had been longer, yeah, I think I'd have pushed for rush swabs on both of them before finalizing anything.

Interviewer: Let's talk about the final report. The likelihood ratio came back moderate, not overwhelming. How did that shape the writing?

Participant: Right, it wasn't a slam-dunk statistic on its own. But by that point I had the proximity — suspect found two blocks away shortly after the call — and his prior conviction sitting in the file too. When I wrote the narrative section, I pulled those together with the DNA finding into one account: the profile is consistent with him, he was near the scene, he's done this before. Read together it feels like a solid picture. My supervisor reviewed it quickly given her own deadline and signed off without flagging the open items — the missing alleles, the unsampled alternatives — as things that needed more work first.

Interviewer: Did you consider presenting the statistical result separately from those other facts?

Participant: I didn't, really. It felt more useful to the DA's office to have it all in one coherent narrative rather than a dry, hedged statistic sitting by itself. Later, during cross-examination, the defense made a point of separating them back out — saying the DNA evidence alone was moderate, and it was really the narrative framing that made it sound stronger than the number supported. That stung a little, but I don't think what I wrote was inaccurate exactly.

Interviewer: If the detective's note hadn't named a suspect before you started typing the sample, do you think you'd have approached the electropherogram differently?

Participant: Possibly. I might've gone in more neutral, treating it purely as an unknown mixture, and maybe I'd have spent as much time on the missing alleles as the matching ones, since there'd be no name pulling my attention toward one profile over another.

Interviewer: And if the ex-boyfriend and delivery driver's elimination samples had come back before the deadline?

Participant: If either of them had matched better than the suspect did, that would've changed everything about how I wrote the conclusion. I just didn't have that data in time, and I made a call with what I had.

Interviewer: Last one — anything you'd want to redo, given what you know now?

Participant: I'd want to look at the electropherogram before reading the detective's narrative, just to see if my read changes. And I'd push harder for those elimination samples even under time pressure, rather than letting the deadline decide that for me.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an evidentiary double standard between the favored suspect-inclusion hypothesis and unsampled alternative-contributor hypotheses at decision point 3."
      },
      {
        "bias": "Feature positive effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as elaborated attention to present/matching allele peaks versus minimal treatment of absent/unexplained peaks at decision point 2."
      },
      {
        "bias": "Contextual Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as pre-analysis exposure to non-scientific case-context information shaping the interpretive frame at decision point 1."
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as blending a moderate statistical result with non-genetic narrative facts into one fluent, internally consistent account at decision point 4."
      }
    ],
    "target_bias_names": [
      "Confirmation Bias and Asymmetrical skepticism",
      "Feature positive effect",
      "Contextual Bias",
      "Coherence-based reasoning or Rationalisation"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "requested_occurrences": 1 },
      { "bias": "Feature positive effect", "requested_occurrences": 1 },
      { "bias": "Contextual Bias", "requested_occurrences": 1 },
      { "bias": "Coherence-based reasoning or Rationalisation", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cx_01", "bias": "Contextual Bias" },
      { "instance_id": "fp_01", "bias": "Feature positive effect" },
      { "instance_id": "cb_01", "bias": "Confirmation Bias and Asymmetrical skepticism" },
      { "instance_id": "co_01", "bias": "Coherence-based reasoning or Rationalisation" }
    ],
    "intended_decision_points": [
      { "instance_id": "cx_01", "bias": "Contextual Bias", "decision_point": 1 },
      { "instance_id": "fp_01", "bias": "Feature positive effect", "decision_point": 2 },
      { "instance_id": "cb_01", "bias": "Confirmation Bias and Asymmetrical skepticism", "decision_point": 3 },
      { "instance_id": "co_01", "bias": "Coherence-based reasoning or Rationalisation", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cx_01",
        "bias": "Contextual Bias",
        "mechanism": "Non-scientific case-context information (detective's suspicion narrative, suspect's prior record) is reviewed before physical evidence examination and frames the interpretive task as confirming a named individual rather than as an open comparison.",
        "affected_reasoning_operation": "Task framing / expectation-setting prior to evidence examination",
        "evidence_source": "Detective's cover note and suspect submission form, reviewed before electropherogram analysis",
        "distinctiveness_requirement": "Must occur strictly at intake/pre-analysis (decision point 1), before any genetic data is examined; distinct from the evidence-weighting operations at decision points 2 and 3."
      },
      {
        "instance_id": "fp_01",
        "bias": "Feature positive effect",
        "mechanism": "Present/matching allele peaks receive elaborated descriptive attention while absent/unexplained peaks receive minimal, non-elaborated treatment during allele-table summarization.",
        "affected_reasoning_operation": "Evidence weighting during allele-table summarization",
        "evidence_source": "Electropherogram allele peaks at multiple loci, some matching suspect profile and some missing/unexplained",
        "distinctiveness_requirement": "Must occur strictly during within-sample allele-level interpretation (decision point 2), distinguishable from the hypothesis-level scrutiny asymmetry at decision point 3."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "mechanism": "A lower evidentiary bar is applied to accept the suspect-inclusion hypothesis than the bar applied to alternative-contributor hypotheses, with competing possibilities scrutinized more skeptically than the favored one.",
        "affected_reasoning_operation": "Hypothesis evaluation and evidentiary threshold-setting across competing source hypotheses",
        "evidence_source": "Comparison between suspect's partial match and unsampled alternative contributors (ex-boyfriend, delivery driver) named by the victim",
        "distinctiveness_requirement": "Must occur strictly at the hypothesis-comparison stage (decision point 3), operating on hypothesis-level evidentiary standards rather than single-sample peak description (fp_01) or pre-analysis framing (cx_01)."
      },
      {
        "instance_id": "co_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "A moderate, individually ambiguous statistical result is synthesized with unrelated non-genetic facts into one fluent, internally consistent narrative that resolves prior open ambiguities without independent justification.",
        "affected_reasoning_operation": "Final synthesis and narrative construction for the report",
        "evidence_source": "Draft likelihood ratio combined with non-genetic case facts (proximity, prior conviction) at report finalization",
        "distinctiveness_requirement": "Must occur strictly at final report synthesis (decision point 4), operating on narrative integration across multiple evidence types, distinct from the single-hypothesis evidentiary threshold issue at decision point 3."
      }
    ],
    "intended_strength": [
      { "instance_id": "cx_01", "bias": "Contextual Bias", "strength": "subtle" },
      { "instance_id": "fp_01", "bias": "Feature positive effect", "strength": "subtle" },
      { "instance_id": "cb_01", "bias": "Confirmation Bias and Asymmetrical skepticism", "strength": "moderate" },
      { "instance_id": "co_01", "bias": "Coherence-based reasoning or Rationalisation", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Biased_4",
    "domain_id": "LE",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per distinct decision point, selected for mechanism fit and narrative realism: contextual bias assigned to pre-analysis intake (DP1), feature positive effect to within-sample allele interpretation (DP2), confirmation bias/asymmetrical skepticism to cross-hypothesis evidentiary comparison (DP3), and coherence-based reasoning/rationalisation to final narrative synthesis (DP4). No bias shares a decision point with another instance of itself or another named bias.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Case type (residential burglary escalating to assault)",
      "Sample type (low-template mixed DNA from windowsill swab)",
      "Number of decision points (four)",
      "Deadline pressure (24-hour turnaround before bail hearing)",
      "Cast of stakeholders (detective, supervisor/technical reviewer, victim, suspect, DA)"
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
