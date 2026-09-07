You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time this week — I know decision-cycle deadlines are brutal right now. Before we start, this is just for our internal process review, nothing goes in any personnel file, and you can skip anything you'd rather not discuss. Sound okay?

Participant: Sure, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me a bit about your role and then give me an overview of the case we're discussing?

Participant: I've been an admissions officer here for about six years, mostly handling transfer applications. The file in question was a transfer student applying mid-cycle from abroad — strong essay, came from a magnet school that's sent us a good number of successful students over the years. It ended up being one of the more complicated files I handled this cycle, partly because of timing and partly because it landed right next to another borderline case at the very end.

Interviewer: Walk me through how it first came across your desk.

Participant: It came in through the regular transfer queue. I do an initial holistic file review — essay, transcript, test scores, letters — before deciding whether to move someone to interview or hold them for more information. This one had a personal essay that was genuinely strong, a transcript from a system I wasn't deeply familiar with, and a standardized test score that was a little under our usual threshold. The recommendation letter came from a teacher at that magnet school, which has a track record of producing students who do well here. Given the deadline pressure, I don't have time to deep-dive every file equally, so I lean on signals like that to triage.

Interviewer: And what did you decide at that point?

Participant: I fast-tracked it to interview. Honestly, the school's reputation carried a lot of weight for me there — we've had strong outcomes from that pipeline before, so a slightly low test score didn't worry me much. If I'm being fully honest, part of it was just an assumption that students coming out of that school are generally more prepared than the raw number suggested, and I didn't really check whether this particular transcript or the letter itself backed that up. I didn't go back and closely reread the letter itself; I registered who it was from and moved forward.

Interviewer: If the test score had been under threshold but the applicant came from a school you didn't recognize, do you think you'd have made the same call?

Participant: Probably not as quickly. I might have held it for a second look first. That said, we do sometimes hold unfamiliar-school files just to verify things, so it's not purely about the score.

Interviewer: What happened next?

Participant: The interview got scheduled during that week of transit strikes downtown, which threw off a lot of appointments. The applicant showed up twelve minutes late, visibly rattled, and the first several minutes of answers were short and hesitant. Answers picked up noticeably as the interview went on.

Interviewer: How did you score that?

Participant: I noted the late arrival and the rocky start on the rubric as a composure concern — some uncertainty about how this person handles pressure or manages time. I was aware the strike was happening citywide, but interview presentation is something we're asked to assess directly, so I documented what I observed.

Interviewer: Did you factor the strike into the written note at all?

Participant: Not explicitly, no. I think I treated the lateness itself as the data point rather than digging into why it happened. Later, admin confirmed the strike had delayed most interview slots that day, which in hindsight probably should have shaped how I read those first few minutes.

Interviewer: What would you have needed at that moment to write the note differently?

Participant: If I'd had that transit confirmation in hand during the interview instead of afterward, I probably would have framed the early hesitation as circumstantial rather than a personal trait note.

Interviewer: Let's move to the committee stage. What came up there?

Participant: Two things landed close together. First, a second reference — the guidance counselor — mentioned a minor disciplinary note from earlier in the applicant's schooling, already resolved, nothing serious. Second, the transcript used a twenty-point scale from a recently reformed grading system, and our credentials office guidance for that specific reform was still provisional — flagged as incomplete.

Interviewer: How did you handle the disciplinary note?

Participant: I talked it through with the committee. Given everything else — the essay, the school, the interview — my read was that the note didn't change the overall picture. If anything, I framed it as the kind of thing that shows a student worked through something and came out fine, which fit with the profile we'd already built of a strong, resilient applicant. Nobody pushed back hard on that framing.

Interviewer: Was there a version of that conversation where the note carried more weight?

Participant: I suppose so. Someone could argue we should treat new information as new information regardless of what came before. We didn't really revisit the earlier assessment from scratch — it got folded into the existing story rather than tested against it.

Interviewer: And the grading scale issue?

Participant: We only get one expedited credential evaluation slot per cycle, and I'd already flagged it for a different file. The credentials office did mention I could request a short same-day consult, or ask the committee to approve reallocating that slot after a quick review, but I didn't pursue either option. So for this one I used our standard conversion table, even knowing it wasn't built for the reformed scale and would probably lowball the actual grades. It was faster, and we were up against the deadline.

Interviewer: What made the table more appealing than pushing for that consult or the reallocation, deadline aside?

Participant: Honestly, some of it was just not wanting to open a longer back-and-forth with the credentials office over a system I wasn't sure how to interpret. Even the short consult felt like it would drag me into a conversation I didn't have a good handle on. The table gave me a number I could work with right away, even flagged as rough.

Interviewer: Understood. Last stage — the final committee vote.

Participant: We had two finalists left for one open seat, both borderline on paper, roughly comparable metrics. One had a legacy connection — same undergraduate network I came through myself, actually, same regional alumni chapter. The other had no alumni tie here at all.

Interviewer: How did you weigh the two?

Participant: We're supposed to apply the same criteria to both. In practice, I found myself giving the network-affiliated finalist a bit more benefit of the doubt on the softer parts of the file — I felt like I had more context on that community, more sense of what their outcomes tend to look like. I probably held the other finalist to a slightly tighter standard on the same soft factors.

Interviewer: Had you noticed that pattern before this case?

Participant: Enrollment did flag afterward that admit rates for network-affiliated legacy candidates in my portfolio run higher than for similar non-affiliated ones, without an obvious merit gap explaining it. I hadn't consciously tracked that before they raised it.

Interviewer: If neither finalist had any connection to your own network, do you think the vote goes the same way?

Participant: Hard to say for certain. I'd like to think the metrics alone would have decided it, but I can't rule out that the tie mattered more than it should have.

Interviewer: Looking back across the whole file, is there one moment you'd want to redo?

Participant: Probably the disciplinary note conversation. I moved through that too fast because it fit what I already believed. If I'd slowed down there the way I eventually did with the grading scale, the file might have landed somewhere different — though I genuinely don't know if the outcome would have changed.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Belief Perserverence and Attitude Polarisation", "occurrences": 1, "mechanism_constraint": "Must involve reinterpretation of newly disclosed disconfirming evidence (disciplinary note) to reinforce, not merely maintain, the pre-existing favorable impression." },
      { "bias": "Fundamental Attribution Bias", "occurrences": 1, "mechanism_constraint": "Must involve attributing observed interview behavior to disposition despite known situational cause (transit strike) available at the time." },
      { "bias": "Halo effect", "occurrences": 1, "mechanism_constraint": "Must involve spillover from a global reputation cue (school prestige) to an unrelated specific judgment (test score adequacy)." },
      { "bias": "Ingroup Favoritism or In-group bias", "occurrences": 1, "mechanism_constraint": "Must involve discretionary weighting favoring a finalist sharing the officer's own alumni/regional network over an equally qualified non-affiliated finalist." },
      { "bias": "Ambiguity Aversion", "occurrences": 1, "mechanism_constraint": "Must involve choosing a familiar but acknowledged-imprecise method over an available but uncertain/effort-intensive resolution path." }
    ],
    "target_bias_names": [
      "Belief Perserverence and Attitude Polarisation",
      "Fundamental Attribution Bias",
      "Halo effect",
      "Ingroup Favoritism or In-group bias",
      "Ambiguity Aversion"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Belief Perserverence and Attitude Polarisation", "requested_occurrences": 1 },
      { "bias": "Fundamental Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Halo effect", "requested_occurrences": 1 },
      { "bias": "Ingroup Favoritism or In-group bias", "requested_occurrences": 1 },
      { "bias": "Ambiguity Aversion", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Halo effect" },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias" },
      { "instance_id": "cb_03", "bias": "Ambiguity Aversion" },
      { "instance_id": "cb_04", "bias": "Belief Perserverence and Attitude Polarisation" },
      { "instance_id": "cb_05", "bias": "Ingroup Favoritism or In-group bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Halo effect", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Ambiguity Aversion", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Belief Perserverence and Attitude Polarisation", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Ingroup Favoritism or In-group bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Halo effect",
        "mechanism": "Global reputation cue (feeder school prestige/alumni record) spills over to inflate confidence in an unrelated specific metric (below-threshold test score).",
        "affected_reasoning_operation": "Evidence weighting at initial file screening",
        "evidence_source": "School reputation and alumni placement record versus standardized test score",
        "distinctiveness_requirement": "Distinct from cb_04 because it concerns spillover from a positive reputational cue onto a co-occurring negative metric at first screening, not reinterpretation of later disconfirming evidence."
      },
      {
        "instance_id": "cb_02",
        "bias": "Fundamental Attribution Bias",
        "mechanism": "Dispositional attribution of behavior despite known situational cause (transit strike) being available at decision time.",
        "affected_reasoning_operation": "Causal attribution during interview scoring",
        "evidence_source": "Applicant's lateness/hesitation versus known citywide transit strike",
        "distinctiveness_requirement": "Sole instance of this bias; occurs only at decision point 2 via the interview rubric entry."
      },
      {
        "instance_id": "cb_03",
        "bias": "Ambiguity Aversion",
        "mechanism": "Avoidance of an uncertain, provisional-guidance resolution path (expedited credential evaluation) in favor of a familiar but acknowledged-imprecise standard method.",
        "affected_reasoning_operation": "Information-source selection under acknowledged incomplete guidance",
        "evidence_source": "Provisional/incomplete conversion guidance for the reformed grading scale versus availability of expedited evaluation",
        "distinctiveness_requirement": "Distinct from cb_04 within the same decision point: concerns handling of the ambiguous grading-scale evidence, not the disciplinary-note evidence."
      },
      {
        "instance_id": "cb_04",
        "bias": "Belief Perserverence and Attitude Polarisation",
        "mechanism": "Disconfirming evidence (disciplinary note) is reinterpreted to reinforce, not merely preserve, the pre-existing favorable belief, resulting in increased confidence rather than neutral or reduced confidence.",
        "affected_reasoning_operation": "Belief updating in response to new disconfirming evidence",
        "evidence_source": "Second reference's disclosure of a minor disciplinary note versus original phase-1 impression",
        "distinctiveness_requirement": "Distinct from cb_03 within the same decision point: concerns handling of the disciplinary-note evidence and belief-confidence trajectory, not the grading-scale conversion choice."
      },
      {
        "instance_id": "cb_05",
        "bias": "Ingroup Favoritism or In-group bias",
        "mechanism": "Shared alumni/regional network membership between evaluator and candidate produces unequal discretionary weighting relative to an equally qualified non-affiliated candidate.",
        "affected_reasoning_operation": "Comparative discretionary weighting in final committee vote",
        "evidence_source": "Finalist's alumni/regional network tie to the officer versus comparable metrics of the non-affiliated finalist",
        "distinctiveness_requirement": "Sole instance of this bias; occurs only at decision point 4 during the final comparative vote."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Halo effect", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Fundamental Attribution Bias", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Ambiguity Aversion", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Belief Perserverence and Attitude Polarisation", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Ingroup Favoritism or In-group bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Biased_5",
    "domain_id": "EI",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points with a maximum of one instance per bias overall; decision point 3 hosts two distinct biases (cb_03, cb_04) drawing on separate evidence sources (grading-scale ambiguity versus disciplinary-note reinterpretation) per the shared-decision-point distinctiveness rule; remaining decision points assigned by mechanism fit (reputation cue at screening, situational-cue interview behavior, network-tie discretionary vote).",
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
