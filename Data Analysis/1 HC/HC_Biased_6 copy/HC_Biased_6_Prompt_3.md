You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm—this is a confidential debrief about how you handled a specific stretch of the trial, not an audit. I'll ask you to walk me through what happened and how you made a few key calls. Sound okay?

Participant: Sure, that's fine. I've talked through the quarter with the monitor already, so I don't mind going over it again.

Interviewer: Great. Can you give me a sense of your role and what this trial looked like during that period?

Participant: I'm the lead coordinator on a Phase III oncology study at our site, one of about fourteen sites nationally. I was also splitting time across two other trials, so hours were tight. We were roughly three weeks from the end of a quarterly enrollment window and about four patients behind target, which matters because the sponsor ties site continuation funding to pace.

Interviewer: What was the main thing you were trying to protect during that stretch?

Participant: Mainly staying compliant while not losing the site's enrollment allocation. Those two goals don't always pull in the same direction.

Interviewer: Walk me through the incident from the start.

Participant: It kicked off with a screening visit. We'd just gotten an amended protocol that changed the organ-function language to something looser—"adequate organ function"—without giving us a lab cutoff table like the old version had. A patient came in who fit almost everything except that his labs were borderline under the old thresholds. Our PI was traveling and only reachable by short messages, not a real conversation. Given where we stood on enrollment, I read the new wording as intentionally more permissive and enrolled him without flagging the ambiguity to anyone first. A few weeks later the sponsor sent a clarifying memo with explicit cutoffs, and his labs didn't clearly meet them. The monitor flagged it for query at the next visit.

Around the same time, I was still trying to get a referral pipeline going with a partner clinic—training their staff, building scheduling templates, that kind of thing. I'd put in something like forty hours on it, but after six weeks it had only produced one enrollee. There was an untried option—reviewing our own oncology charts for candidates—that a colleague thought could move faster. I kept most of my hours on the partner-clinic pipeline anyway. Part of it was that I'd already built the infrastructure and didn't want to abandon it prematurely. Separately, a coordinator newsletter came out saying a couple of peer sites were ahead of pace using a similar clinic-referral approach, and that made me more comfortable sticking with it rather than testing the chart-review idea.

Then we had an adverse event: a newly enrolled patient developed a grade 2 rash and some fatigue about nine days after his first infusion. It looked a lot like the classic hypersensitivity vignette in the investigator brochure. He'd also just finished an antibiotic course and has a history of seasonal allergies, both in his chart already. The day before I drafted my assessment, a peer-site coordinator had described an almost identical rash on a call, attributed to the study drug. My draft leaned toward drug-related, mostly because the case matched the brochure picture so well, and that recent peer case reinforced it for me.

Last piece: the eligibility ambiguity resurfaced as a monitor query, and I had to summarize it in writing for the sponsor's trial manager. The PI floated two ways to describe it—"minor administrative eligibility clarification" or "protocol deviation requiring corrective action." Both were defensible given how the language had been written. I went with the milder version, partly because it came up first and just sounded less serious.

Interviewer: Let's slow down and go through each of those in order. Starting with the screening decision—what did you actually have in front of you right then?

Participant: The new protocol text, the patient's lab values, and the fact that our PI wasn't reachable for a real discussion. I also had the enrollment count in the back of my mind.

Interviewer: What alternatives did you consider?

Participant: I could have held the screening and pushed the ambiguity up to the PI or the sponsor's medical monitor before deciding anything, or just declined him outright until the wording was clarified. I didn't do either—I made the call myself and moved forward.

Interviewer: What made you settle on your own interpretation instead of escalating?

Participant: Honestly, escalating would have meant losing him as a candidate for that window, and we needed the number. I told myself the new language was probably meant to be more flexible, so I read it that way and enrolled him.

Interviewer: Moving to the referral pathway—what alternatives did you weigh?

Participant: Keep pushing the partner-clinic pipeline, redirect hours to chart review, or split time between both. I stayed with the partner-clinic route.

Interviewer: What tipped the balance?

Participant: Two things, really. I'd already sunk forty hours into setting it up, so switching felt like throwing that away. And then seeing that other sites were reportedly doing well with a similar setup made it easier to justify staying the course rather than testing something untried.

Interviewer: On the adverse event—how did you arrive at your causality read?

Participant: The presentation matched the brochure's example almost point for point, so that was my anchor. And having just heard about that near-identical case on the peer call the day before made it feel confirmed, so I leaned toward drug-related in my draft.

Interviewer: Did the antibiotic course or allergy history factor into that draft?

Participant: They were in the chart, but I didn't weigh them heavily going in—I mentioned them but treated the pattern match and the peer case as the stronger signal.

Interviewer: And the sponsor note—how did you land on that specific wording?

Participant: The PI mentioned the "minor clarification" phrasing first when we talked it through, and it just felt like the lower-friction option, so that's what I used.

Interviewer: Was there anything at that point pulling you toward the other description?

Participant: Not really pulling me—I knew "protocol deviation" was equally accurate, but by the time I sat down to write the note, the milder framing was already the one in my head.

Interviewer: How much uncertainty did you feel at each of these moments?

Participant: Screening felt rushed more than uncertain. The pathway decision felt more like frustration than doubt. The AE read, I was fairly confident at the time, less so after the allergy testing came back. The note-writing, I didn't feel uncertain at all in the moment, which looking back maybe I should have.

Interviewer: If the sponsor's clarifying memo had landed a day before that screening visit, would things have gone differently?

Participant: Probably—I'd have had the actual cutoffs and wouldn't have needed to guess.

Interviewer: And if you hadn't seen the peer newsletter or heard about that rash case beforehand?

Participant: The pathway decision might have gone to chart review sooner. The AE draft, I'm less sure—the pattern match alone might have gotten me there anyway, just maybe with less confidence.

Interviewer: If the PI had suggested "protocol deviation" first instead of the milder phrase?

Participant: I think I'd have gone with that one instead, honestly.

Interviewer: Looking back, is there a point where you'd want clearer guidance before deciding?

Participant: The eligibility language, definitely—a real threshold table instead of open wording would have saved me from guessing under pressure.
}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Ambiguity Bias", "occurrences": 1, "mechanism_constraint": "unresolved interpretation of ambiguous eligibility language resolved unilaterally toward preferred outcome"},
      {"bias": "Sunk Costs Bias", "occurrences": 1, "mechanism_constraint": "continued resource commitment justified by prior invested effort rather than current yield"},
      {"bias": "Representativeness", "occurrences": 1, "mechanism_constraint": "causal judgment driven by surface pattern match to a textbook vignette over base-rate/chart evidence"},
      {"bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "decision influenced by peer-site social proof rather than own-site performance data"},
      {"bias": "Framing Effect", "occurrences": 1, "mechanism_constraint": "wording choice for a compliance report driven by presentation order/valence of description rather than underlying facts"},
      {"bias": "Recency Bias", "occurrences": 1, "mechanism_constraint": "disproportionate weight given to the most recently encountered comparator case"}
    ],
    "target_bias_names": [
      "Ambiguity Bias",
      "Sunk Costs Bias",
      "Representativeness",
      "Bandwagon effect",
      "Framing Effect",
      "Recency Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Ambiguity Bias", "requested_occurrences": 1},
      {"bias": "Sunk Costs Bias", "requested_occurrences": 1},
      {"bias": "Representativeness", "requested_occurrences": 1},
      {"bias": "Bandwagon effect", "requested_occurrences": 1},
      {"bias": "Framing Effect", "requested_occurrences": 1},
      {"bias": "Recency Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "hc6_01", "bias": "Ambiguity Bias"},
      {"instance_id": "hc6_02", "bias": "Sunk Costs Bias"},
      {"instance_id": "hc6_03", "bias": "Bandwagon effect"},
      {"instance_id": "hc6_04", "bias": "Representativeness"},
      {"instance_id": "hc6_05", "bias": "Recency Bias"},
      {"instance_id": "hc6_06", "bias": "Framing Effect"}
    ],
    "intended_decision_points": [
      {"instance_id": "hc6_01", "bias": "Ambiguity Bias", "decision_point": 1},
      {"instance_id": "hc6_02", "bias": "Sunk Costs Bias", "decision_point": 2},
      {"instance_id": "hc6_03", "bias": "Bandwagon effect", "decision_point": 2},
      {"instance_id": "hc6_04", "bias": "Representativeness", "decision_point": 3},
      {"instance_id": "hc6_05", "bias": "Recency Bias", "decision_point": 3},
      {"instance_id": "hc6_06", "bias": "Framing Effect", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "hc6_01",
        "bias": "Ambiguity Bias",
        "mechanism": "Unilateral resolution of genuinely ambiguous eligibility wording toward the enrollment-favoring interpretation, without escalation or documentation",
        "affected_reasoning_operation": "Interpretation of underspecified eligibility criteria",
        "evidence_source": "Amended protocol text and PI unavailability at screening",
        "distinctiveness_requirement": "Sole ambiguity-resolution act in the interview; must not recur in decision points 2-4"
      },
      {
        "instance_id": "hc6_02",
        "bias": "Sunk Costs Bias",
        "mechanism": "Continued time allocation to an underperforming pathway justified by hours already invested rather than recent yield",
        "affected_reasoning_operation": "Resource-reallocation decision under prior investment",
        "evidence_source": "Prior 40 hours of pathway setup work and its low six-week yield",
        "distinctiveness_requirement": "Must be argued via 'effort already spent' language, distinct from hc6_03's peer-comparison language at the same decision point"
      },
      {
        "instance_id": "hc6_03",
        "bias": "Bandwagon effect",
        "mechanism": "Decision to persist with the pathway additionally driven by peer-site network reports of being 'ahead of pace,' independent of own-site data",
        "affected_reasoning_operation": "Weighting of social/peer proof versus own performance data",
        "evidence_source": "Coordinator-network newsletter describing peer-site progress",
        "distinctiveness_requirement": "Must be argued via peer/network reference language, distinct from hc6_02's sunk-effort language at the same decision point"
      },
      {
        "instance_id": "hc6_04",
        "bias": "Representativeness",
        "mechanism": "Causality lean determined by surface resemblance to a textbook AE vignette, with contrary chart evidence underweighted",
        "affected_reasoning_operation": "Diagnostic/causal categorization of an adverse event",
        "evidence_source": "Investigator brochure vignette compared to symptom presentation",
        "distinctiveness_requirement": "Must be argued via pattern-resemblance language, distinct from hc6_05's recency-of-report language at the same decision point"
      },
      {
        "instance_id": "hc6_05",
        "bias": "Recency Bias",
        "mechanism": "Disproportionate weight assigned to the peer-site AE report discussed the day before, over longer-standing chart evidence, due to its recency",
        "affected_reasoning_operation": "Integration of external comparator evidence into a causality judgment",
        "evidence_source": "Peer-site AE report discussed on a call the day before assessment",
        "distinctiveness_requirement": "Must be argued via temporal-recency language, distinct from hc6_04's pattern-resemblance language at the same decision point"
      },
      {
        "instance_id": "hc6_06",
        "bias": "Framing Effect",
        "mechanism": "Selection of milder compliance-report wording because it was presented first and sounds less consequential, despite factual equivalence of alternatives",
        "affected_reasoning_operation": "Selection of description/label for an ambiguous compliance event",
        "evidence_source": "Two PI-suggested, equally defensible descriptions of the same event",
        "distinctiveness_requirement": "Sole framing/labeling act in the interview; must not recur in decision points 1-3"
      }
    ],
    "intended_strength": [
      {"instance_id": "hc6_01", "bias": "Ambiguity Bias", "strength": "subtle"},
      {"instance_id": "hc6_02", "bias": "Sunk Costs Bias", "strength": "subtle"},
      {"instance_id": "hc6_03", "bias": "Bandwagon effect", "strength": "subtle"},
      {"instance_id": "hc6_04", "bias": "Representativeness", "strength": "subtle"},
      {"instance_id": "hc6_05", "bias": "Recency Bias", "strength": "subtle"},
      {"instance_id": "hc6_06", "bias": "Framing Effect", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "not_applicable",
      "original_state": "not_applicable",
      "changed_state": "not_applicable",
      "variables_to_hold_constant": []
    },
    "scenario_id": "HC_Biased_6",
    "domain_id": "HC",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across 4 decision points by mechanism fit and narrative realism (DP1:1, DP2:2, DP3:2, DP4:1); no decision point contains two instances of the same bias; co-located instances (DP2, DP3) use distinct evidence sources and reasoning operations per the instance independence rule.",
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
