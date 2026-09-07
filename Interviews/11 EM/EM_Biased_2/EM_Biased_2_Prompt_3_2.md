You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{**Interviewer:** Thanks for making time for this. Just to confirm — this is a voluntary debrief for our after-action learning file, not a performance review. I'll ask you to walk me through the Riverside facility fire from your role as PIO, and I may pause to dig into specific moments. Sound okay?

**Participant:** Sure, happy to do it. It's still pretty fresh — that was a long shift.

**Interviewer:** Good. Before we get into detail, can you give me a quick overview of the incident and what you were trying to accomplish?

**Participant:** Basically, we had a fire break out at the solvent recycling facility on the east side, maybe three hundred meters from a residential block and not far from the elementary school. My job was to get accurate public messaging out fast — warn people if they needed to shelter, keep the media from running ahead of us, and coordinate with the school and health officer so nobody's getting conflicting instructions. Objective was simple to state, hard to execute: protect people without causing panic, and don't say anything we'd have to walk back.

**Interviewer:** Walk me through how it started.

**Participant:** Dispatch got the call a little after 1pm. Within ten minutes we had confirmation of a working fire, heavy smoke, and wind carrying it toward the neighborhood. 911 was lighting up with people reporting a chemical smell. Problem was, we didn't have the facility's chemical manifest yet — that takes time to pull and verify with the fire marshal. So I'm standing in the JIC with a wind direction, an odor complaint pattern, and no confirmed hazard identity. I recommended we go out with a precautionary shelter-in-place advisory rather than wait, because closing windows and staying put costs us very little if it turns out to be nothing, but waiting costs a lot if it's not nothing.

**Interviewer:** What information came in after that first call?

**Participant:** Within about forty minutes the manifest came back — mostly low-toxicity solvents, not the worst-case chemical we'd feared. Wind also shifted slightly, pushing the plume a bit more over open ground. So the initial risk picture actually eased some, which was a relief, but by then we'd already committed to the advisory, which I think was still the right call given what we knew at the time.

**Interviewer:** Let's reconstruct the next couple hours. What happened after that initial advisory went out?

**Participant:** We had about a ninety-minute window where the air monitoring wasn't fully stood up yet, so we were operating a little blind on the contaminant side. Meanwhile the Incident Commander is focused on suppression, the health officer wants to weigh in on any health guidance, and our elected officials are asking me for updates every twenty minutes. Then social media started moving faster than we could — somebody posted early speculation that it was a "chemical explosion," which wasn't accurate, and we had to spend cycles knocking that down instead of just informing.

**Interviewer:** That's around when you had to choose how to actually push out that first advisory — which system to use. Tell me about that decision.

**Participant:** Right, so our comms team had two options. There's the reverse-911 system, which got upgraded last year — it can geotarget down to the block level, so you're only alerting people actually in the plume path. Then there's our Community Alert Network, the CAN system, which is the one we've used in every drill and every real incident for at least five years. I know that script cold, I know how the spokesperson delivery works with it, I know what it sounds like when it goes out.

**Interviewer:** And you went with CAN.

**Participant:** I did. It's just the one that's always worked for us. Somebody on the comms desk mentioned reverse-911 had a couple of successful tests on the books, but I didn't pull the test log or ask the on-call tech what the fallback would be if it hiccupped mid-broadcast — I just had this sense that a system I hadn't personally run live could have bugs, and that was enough to steer me back to what I already knew. I was aware CAN would blast countywide instead of just the plume area, which isn't really a great fit for a localized smoke event, but that didn't weigh very heavily against just going with the familiar option.

**Interviewer:** Did you weigh the two options against each other on any specific criteria — reach accuracy, message length, anything like that?

**Participant:** Not in a formal sense, no. It was more that CAN is the one I trust because I've been using it for years. In hindsight the countywide reach did cause some issues — we got a bunch of calls from people way outside the plume who got scared for no reason — but at the time it felt like the safer choice just because it was the tool I knew.

**Interviewer:** Let's move to the third decision point — the escalation discussion. What was happening then?

**Participant:** About two hours in, the health officer's sensor readings were coming through — text table, updated every fifteen minutes — and contaminant levels were sitting in the advisory range, not danger range. But right around the same time, a resident's photo of this huge black smoke plume went viral locally, just an incredibly dramatic shot, rooftops with this black column behind them. Media started calling, asking if we were about to order an evacuation.

**Interviewer:** How did that shape your thinking?

**Participant:** Honestly, looking at that photo, my gut said this looks bad, we should be moving toward evacuation language. I actually had a draft evacuation recommendation half-written. The sensor table was open right there on my second monitor the whole time, showing levels weren't at that threshold, but the image was what I kept coming back to when I was talking through it with the team — how thick and dark that smoke looked. We ended up holding at shelter-in-place because the health officer pushed back hard on the data, not because I'd fully talked myself out of the escalation.

**Interviewer:** What did you learn afterward?

**Participant:** The follow-up readings thirty minutes later confirmed levels had stayed stable the whole time. And it turned out that black smoke was mostly from a stockpile of packaging material catching fire, not the solvents themselves. So visually it looked like the worst-case scenario, but the actual air data never supported that story.

**Interviewer:** Last decision point — the all-clear.

**Participant:** By hour five, suppression's basically done, Incident Commander says fire's under control. But we've got parents showing up at the school reunification point, some residents still smelling residual smoke, and the health officer recommends lifting shelter-in-place but keeping a window-closure advisory for two more hours as a buffer. I went with that phased approach instead of a full all-clear right away.

**Interviewer:** Any pushback on that?

**Participant:** A handful of residents said the phased message was confusing — they wanted a clean yes-or-no. But given we still had some odor reports, I felt the cautious, staged approach was more defensible than an immediate blanket all-clear, even if it wasn't as tidy a message.

**Interviewer:** If the reverse-911 system had already been used successfully in a live incident before this one, do you think you'd have made a different channel choice?

**Participant:** Probably, yeah. If I'd seen it perform live even once, I think I'd have trusted it enough to use it instead of CAN, especially given the geotargeting benefit.

**Interviewer:** And if that photo had never circulated — does the escalation conversation go differently?

**Participant:** I think it's calmer, honestly. The sensor data alone was pretty steady the whole time. Without that image driving the room's mood, we probably stay at shelter-in-place without ever drafting the evacuation language.

**Interviewer:** Anything you'd evaluate differently with the same information again?

**Participant:** Maybe build in a habit of stating the data source out loud before reacting to whatever's most visually striking in the moment. And for channel choice, I'd want someone to actually pull the reverse-911 test record and talk to the on-call tech before I default to the tool I already know, so familiarity isn't doing all the deciding. Otherwise, given what we knew at each point, I think the calls were reasonable.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Mere Exposure",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as channel/template preference driven by repeated past use/familiarity rather than comparative performance criteria."
      },
      {
        "bias": "Picture Superiority",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a vivid image disproportionately shaping severity judgment relative to concurrently available textual/numeric sensor data."
      }
    ],
    "target_bias_names": [
      "Mere Exposure",
      "Picture Superiority"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Mere Exposure",
        "requested_occurrences": 1
      },
      {
        "bias": "Picture Superiority",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure"
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure",
        "decision_point": 2
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure",
        "mechanism": "Repeated-use familiarity with the CAN template/spokesperson drives channel selection over a comparatively superior but unfamiliar reverse-911 geotargeting option.",
        "affected_reasoning_operation": "Channel/tool selection under uncertainty",
        "evidence_source": "Five years of drill/incident usage history for CAN vs. two successful non-live tests of reverse-911",
        "distinctiveness_requirement": "Must be distinguishable from Picture Superiority by involving a tool/channel choice grounded in repetition history, not visual/imagery salience."
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority",
        "mechanism": "A vivid viral photograph disproportionately shapes the severity assessment relative to concurrently available textual sensor readings.",
        "affected_reasoning_operation": "Evidence weighting/severity assessment during message escalation",
        "evidence_source": "Viral social media photo of smoke vs. live text-based air quality sensor table",
        "distinctiveness_requirement": "Must be distinguishable from Mere Exposure by involving image-driven salience during a live severity judgment, not repetition-driven familiarity with a tool."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "meb_01",
        "bias": "Mere Exposure",
        "strength": "subtle"
      },
      {
        "instance_id": "pse_01",
        "bias": "Picture Superiority",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Biased_2",
    "domain_id": "EM",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Automatic assignment: each bias assigned to a distinct decision point (2 and 3 respectively) selected for mechanism fit and narrative realism per rules 1-4; no decision point received more than one instance of a given bias since each bias has only one requested occurrence.",
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
