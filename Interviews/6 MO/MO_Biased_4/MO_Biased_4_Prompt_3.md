You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our internal review process, not a disciplinary hearing — you can decline to answer anything. Can you start by telling me your role on this voyage?

Participant: Sure. I'm master of the Kestrel Bay, bulk carrier, about 76,000 deadweight. This was the inbound leg to Rotterdam, Berth 7, with a grain cargo that had a fairly tight delivery clause attached to it.

Interviewer: And before we get into the specifics — what did you know about the passage plan going in?

Participant: The passage plan had been filed and approved before we sailed from the load port. Standard route through the Maasgeul into the Nieuwe Waterweg. Nothing unusual about it at that stage.

Interviewer: Okay. Let's start with your account of what happened, in your own words, and then we'll go back through it in more detail.

Participant: Right, so we were maybe three hours out from the tidal gate when NAVTEX came through with an update — a newly surveyed shoal patch near our filed track, reduced depth compared to the charted figure. There was an alternate channel that was deeper, but it would've added about forty minutes to the transit. Given our tidal window was already tight because of the charter penalty clause on the cargo, I decided to stick with the original plan. It had already been coordinated with the agent and the pilot station, and my read at the time was that the revision was probably minor — these shoal notices come through fairly often and a lot of them are conservative. Chief Officer flagged afterward that our under-keel clearance margin near that patch would be tighter than usual given the datum tide, and once you add squat effect at our transit speed, the margin gets thinner still. But by then we were committed to the route.

We came into the approach channel around dusk, patchy fog rolling in, and a squall building further out. ECDIS had the countdown to the tidal gate running prominently on the display — that was the thing everyone kept glancing at, because if we missed it we'd be looking at hours of delay and tugs and pilot slots getting reshuffled. Radar showed a handful of contacts, small fishing vessels bunched near the edge of the fairway, plus one slower, ambiguous return that the OOW mentioned in passing near the deep-water part of the track. I told him to keep an eye on the deep water and let me know if anything closed in — my attention at that point was really on the gate timing and getting the berth logistics locked down with the agent.

About twenty minutes later the Chief Engineer called up to report the main engine cooling water temperature was running above normal. He recommended dropping to half power for about twenty minutes to inspect it. I've had that alarm before — more than once in fifteen years — and it's almost always a sensor lag issue that resolves itself. So I told him I'd seen it before and we'd hold speed. He called back later saying the trend didn't look like the usual lag pattern, more sustained, but by then VTS had come through with a traffic advisory identifying that ambiguous contact as a drifting fishing vessel without power, closer to the centerline than we'd plotted. That's when things got busy.

Interviewer: Let's walk through the sequence again, a bit slower this time. What information were you drawing on at each stage?

Participant: NAVTEX for the shoal update, ECDIS for the route and the gate countdown, radar and ARPA for traffic, VTS for the broader picture, and engine room reports over the phone. Each one came in at a different point, so it wasn't like I had the full picture at any single moment — you're building it as you go.

Interviewer: And what were you and the officers focused on as you entered the channel?

Participant: Mostly the tide gate and the berth coordination. That was the pressure point. The OOW was watching traffic, I was managing timing and talking to the agent about tug availability.

Interviewer: Let's go back to the NAVTEX update. What alternatives did you weigh, and why did you choose to keep the original route?

Participant: The alternate channel was the obvious other option, and slowing down to get an updated survey confirmation was theoretically on the table too. But re-filing the route means coordinating again with the pilot station and probably losing the slot anyway, so functionally it felt like the same outcome as just taking the delay. The original plan was already approved and everyone downstream was expecting it. I didn't really re-run the numbers on the new depth against our draft and the tide — it felt like something that would've been flagged harder by the agency if it were serious.

Interviewer: During the channel transit, what cues were you attending to, and is there anything you think you might have missed?

Participant: Honestly, the gate countdown was dominating my attention, and the berth call. The fishing boat cluster registered as background traffic — normal for that stretch. The one ambiguous contact, I noted it, told the OOW to watch it, but I didn't personally re-plot it or push VTS for a read on it myself. In hindsight there was a window there where I could've asked more directly what that contact actually was instead of just filing it as "probably fine, keep an eye on it."

Interviewer: When the Chief Engineer raised the temperature reading, what gave you confidence in your call to hold speed?

Participant: Mostly just having seen that specific alarm pattern before, multiple times, without it turning into anything. It's a judgment built on a lot of runs on similar plant. I didn't ask him to pull fresh diagnostics before deciding — I made the call fairly quickly based on that history.

Interviewer: When VTS issued the traffic advisory, what options did you weigh before acting?

Participant: Abort the gate attempt entirely and anchor to reassess, take a smaller late adjustment to clear both the contact and the shoal, or call for pilot and tug assistance immediately and slow right down. I went with the smaller adjustment — full abort felt disproportionate given how close we already were, and I judged we had enough margin to thread it.

Interviewer: What information, if it had arrived earlier, would have changed your decision at the route stage?

Participant: If the NAVTEX update had come through before we'd filed and departed, I think I'd have just taken the deeper channel without a second thought — there'd have been no schedule cost attached to it yet. Timing of when it landed relative to our commitment really shaped how I weighed it.

Interviewer: Looking back now, how clear were the warning signs about the shoal at the time you made that routing call?

Participant: Looking back, it was pretty clear that the alternate channel was the sounder option — the depth reduction plus squat plus the tide state, once you line it all up, points obviously to being cautious there. It's hard now not to see it as something I should have caught immediately.

Interviewer: What would you do differently if you faced the same engine-temperature situation again?

Participant: Probably ask for a fresh reading or a short trend check before deciding, rather than leaning purely on what I remembered from past incidents.

Interviewer: Last one — if the fishing vessel hadn't been drifting without power, just moving normally, do you think the outcome would have played out differently given how the attention was allocated during the transit?

Participant: Probably would've passed without anyone thinking twice about it, which is part of why it didn't feel urgent in the moment. The margin for error was just a lot thinner than any of us realized while it was actually happening.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Hindsight Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as retrospective causal attribution during decision-4 probe response about decision 1, not as a repeated summary"
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as real-time cue-sampling failure during the channel transit, distinct from any later summary of the event"
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as miscalibrated reliance on personal track record over specialist current data at the engine-alarm decision"
      },
      {
        "bias": "Status Quo Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as default retention of the pre-existing filed plan despite new information at decision point 1"
      }
    ],
    "target_bias_names": [
      "Hindsight Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Overconfidence Bias",
      "Status Quo Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Hindsight Bias", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 },
      { "bias": "Status Quo Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_04", "bias": "Status Quo Bias" },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "cb_03", "bias": "Overconfidence Bias" },
      { "instance_id": "cb_01", "bias": "Hindsight Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_04", "bias": "Status Quo Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Overconfidence Bias", "decision_point": 3 },
      { "instance_id": "cb_01", "bias": "Hindsight Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_04",
        "bias": "Status Quo Bias",
        "mechanism": "Default retention of previously filed passage plan despite new depth information",
        "affected_reasoning_operation": "Route re-evaluation under new information",
        "evidence_source": "NAVTEX shoal update versus filed passage plan",
        "distinctiveness_requirement": "Only instance tied to the pre-departure/route-filing decision; must not repeat in later phases"
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Attentional capture by tidal-gate countdown suppresses processing of an ambiguous radar/AIS contact",
        "affected_reasoning_operation": "Real-time cue selection from ARPA/radar and OOW reports",
        "evidence_source": "ARPA plot and OOW verbal report of ambiguous contact",
        "distinctiveness_requirement": "Distinct evidence source (radar/AIS contact) and moment (channel transit) from all other instances"
      },
      {
        "instance_id": "cb_03",
        "bias": "Overconfidence Bias",
        "mechanism": "Over-weighting of personal historical track record relative to current specialist diagnostic input",
        "affected_reasoning_operation": "Risk calibration versus specialist recommendation",
        "evidence_source": "Chief Engineer's temperature report and recommendation versus master's prior experience claim",
        "distinctiveness_requirement": "Distinct evidence source (engine room data) and decision (power/speed) from all other instances"
      },
      {
        "instance_id": "cb_01",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospective assertion that outcome-relevant information was obviously decisive at the time, contradicting the genuine ambiguity described earlier",
        "affected_reasoning_operation": "Retrospective causal attribution during closing probe",
        "evidence_source": "Master's own earlier account of decision 1 versus post-outcome probe response",
        "distinctiveness_requirement": "Only instance occurring in the post-outcome interview reconstruction; must not be conflated with the original decision-1 status quo instance"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_04", "bias": "Status Quo Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Overconfidence Bias", "strength": "moderate" },
      { "instance_id": "cb_01", "bias": "Hindsight Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Timing of NAVTEX shoal update relative to route commitment",
      "original_state": "Update arrives after passage plan is filed and underway (switching cost present)",
      "changed_state": "Update arrives before departure (no switching cost)",
      "variables_to_hold_constant": [
        "Vessel type and cargo",
        "Weather and visibility conditions",
        "Engine cooling anomaly and its timing",
        "Tidal window constraint",
        "Crew composition and stated experience level"
      ]
    },
    "scenario_id": "MO_Biased_4",
    "domain_id": "MO",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One instance per named bias, each assigned to a distinct decision point (1–4) selected for mechanism fit: default-retention framing at the initial route decision (Status Quo), attentional-capture framing during the narrow-channel transit (Selective Attention/Inattentional Blindness), specialist-versus-self-trust framing at the engine alarm (Overconfidence), and retrospective-attribution framing during the closing probe about the near-miss outcome (Hindsight). No decision point received more than one occurrence of any single bias, satisfying the two-occurrence cap trivially since each bias occurs only once overall.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vessel type and cargo",
      "Weather and visibility conditions",
      "Engine cooling anomaly and its timing",
      "Tidal window constraint",
      "Crew composition and stated experience level"
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
