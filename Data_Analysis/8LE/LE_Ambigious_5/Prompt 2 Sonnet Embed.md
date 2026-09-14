You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time. This is a voluntary session for internal research on how IA reviews get worked, not a disciplinary matter. You can decline any question. Good with that?

Participant: Sure, that's fine.

Interviewer: Can you tell me your role and experience with complaint reviews?

Participant: Internal Affairs investigator, about five years. I handle use-of-force complaints mostly, some policy violations.

Interviewer: Walk me through the case.

Participant: Traffic stop on Cedar Street, expired registration, ended with a takedown. The driver, Mr. Alvarez, alleges excessive force by Officer Marquez, came away with a wrist fracture. Marquez's report says Alvarez became resistant and pulled his arm away, necessitating the takedown. His partner, Officer Chen, corroborates that. Marquez has nine years in, two prior complaints, both closed unfounded. Alvarez has two prior arrests, one for resisting.

Interviewer: What was your initial read on credibility before you'd seen any footage?

Participant: Genuinely unresolved. Two competing accounts, both plausible on their face, and I didn't have enough yet to prefer one.

Interviewer: What did you do first when you opened the file?

Participant: Requested background on both sides—Alvarez's arrest history and Marquez's disciplinary and training file. Alvarez's record came back within a day, since it's just a records-system pull. Marquez's full file took almost a week because it required a request through the union rep and a records custodian. So for several days I had a fuller picture of one side than the other, which I noted explicitly in my log as a limitation, not a conclusion.

Interviewer: Did that timing gap affect how you approached the rest of the review?

Participant: I tried not to let it. I flagged it as an open item—"complainant background received, officer background pending"—so anyone reading the file later would know the record was uneven at that point, not that I'd already decided anything based on it. Dispatch audio later confirmed it was a routine stop, not flagged high-risk. Medical report confirmed the fracture but didn't tell me which account caused it.

Interviewer: Let's go to the footage.

Participant: Eighteen minutes, with a forty-second gap right after initial contact—his camera didn't reactivate cleanly. Early part is calm, verbal exchange, some de-escalation language from Marquez. Final ninety seconds: Alvarez pulls his arm back, Marquez takes him down.

Interviewer: How did you weigh the earlier footage against that final sequence?

Participant: Honestly, I couldn't fully resolve it on the first pass. The takedown is obviously central since that's where the injury happened, but the gap sits right before the point where things start escalating, and I don't know what's in it. I logged both segments as carrying weight and noted the gap as a limiting factor on any proportionality conclusion I might draw. I didn't want to lock in a read before the consultant weighed in.

Interviewer: What came out of the consultant review?

Participant: A slowed-frame audio pass caught Marquez raising his voice and stepping closer about three minutes before the takedown. The consultant said it's relevant context but not dispositive on its own—doesn't resolve whether the final force was proportionate, just adds texture.

Interviewer: How did that sit with you?

Participant: It complicated things more than it clarified them, if I'm honest. It's the kind of detail that could support either read, depending on what else you believe about the encounter.

Interviewer: Tell me about the case conference.

Participant: Day six. Me, the sergeant, two peer investigators. The sergeant supervised Marquez for three years, said something like "he's generally solid, but I wasn't in the car, so take that for what it's worth." One of the other investigators raised the forty-second gap, said it needed to be addressed before we went further.

Interviewer: How did the room handle that?

Participant: We actually sat with it. There wasn't a quick consensus—two of us thought the gap was potentially significant given the timing relative to the escalation audio, one thought Chen's corroboration and the visible resisting motion carried it regardless. We didn't resolve that disagreement in the room. I logged the dissenting view by name in the case file and noted the preliminary summary as tentative pending the gap issue.

Interviewer: Did the sergeant's history with Marquez shape the discussion?

Participant: It was mentioned, and it's fair to say it's not nothing—people listen when a three-year supervisor speaks. But he qualified it himself, and the discussion kept coming back to what was and wasn't on the tape rather than settling on his character read. I can't say for certain it had zero influence, but I also can't point to a moment where it overrode the evidentiary discussion.

Interviewer: What happened with the eyewitness on day ten?

Participant: A civilian witness we'd had trouble reaching finally called back. She said Marquez was "aggressive from the start," which cuts against how I'd been characterizing the early footage. That came two days after I'd sent the Deputy Chief a preliminary note—explicitly marked tentative, pending the gap and the consultant review.

Interviewer: How did you weigh her statement against what you already had?

Participant: We ran a supplemental check—she had an unobstructed view but was about thirty-five feet out, evening light. I weighed that against the footage on its own terms: is a thirty-five-foot, unobstructed view enough to outweigh eighteen minutes of direct recording? I didn't think it fully was, but I also didn't think it was nothing, especially given the earlier escalation audio the consultant had flagged. I ended up revising the briefing language to reflect that the finding remained more open than the initial note suggested, rather than either adopting her account outright or setting it aside.

Interviewer: Did the fact that you'd already briefed command shape how you handled her statement?

Participant: Command asked whether the preliminary note still held, and I told them it needed updating. It wasn't comfortable revising something I'd already sent up, but the distance and lighting were the actual basis for how much weight I gave her account—not really about protecting what I'd said earlier. I'd rather have gotten it right than tidy.

Interviewer: What's the part of this case you're least confident about?

Participant: The forty-second gap, still. I don't know what happened in it, and I don't know how much that should move the needle either way.

Interviewer: If the eyewitness statement had come in on day two instead of day ten, would your review have gone differently?

Participant: Possibly. I'd have had it earlier alongside the footage instead of layering it onto a note I'd already sent, though I think I'd have weighed it the same way on the merits—distance and view, not timing.

Interviewer: If you'd been the only reviewer, without the case conference, same finding?

Participant: Hard to say. I might have sat with the gap even longer alone. The conference didn't rush me toward a view, but group discussion does move differently than solo review.

Interviewer: Anything you'd sequence differently next time?

Participant: I'd push to get officer background files moving faster at intake, so that gap doesn't sit open as long. Otherwise, I think the uncertainty here was mostly the case itself, not how I worked it.

Interviewer: Appreciate you walking through it.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Ambigious_5",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Internal Affairs Investigator",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "The Cedar Street Stop: Use-of-Force Complaint Review (Ambiguous Control)",
    "scenario_summary_internal": "Paired control for LE_Biased_5, using the same Cedar Street traffic-stop use-of-force complaint, the same actors, the same four-phase chronology, and the same evidentiary gaps (BWC camera lapse, prior histories on both sides, a late-arriving eyewitness). The investigator's reasoning at each decision point is genuinely underdetermined by the available evidence, with multiple defensible readings remaining open throughout, but no decision is written to instantiate confirmation bias/asymmetrical skepticism, recency effects, groupthink, or cognitive dissonance. Ambiguity arises from resource constraints, witness-reliability tradeoffs, incomplete footage, and honestly-acknowledged uncertainty rather than from any of the named reasoning distortions.",
    "occupational_realism": {
      "objective": "Determine whether Officer Marquez's use of force during the Cedar Street stop was objectively reasonable and consistent with department use-of-force policy, and issue a sustained/unsustained/exonerated finding supported by the case file.",
      "setting": "Municipal police department Internal Affairs Bureau, over a 12-day review period following a citizen complaint filed the morning after the incident.",
      "constraints": [
        "14-day departmental deadline to issue a preliminary finding",
        "BWC footage has a 40-second gap due to a camera reactivation delay",
        "Complainant has two prior arrests, one for resisting arrest, known to the investigator before the interview",
        "Officer Marquez has 9 years of service, two prior complaints both closed as unfounded",
        "Sergeant on the review panel supervised Marquez for 3 years and offers a supportive but explicitly qualified opinion at the case conference",
        "A civilian eyewitness statement is not collected until day 10 due to delayed callback"
      ],
      "stakeholders": [
        "Internal Affairs Investigator (interviewee)",
        "Officer R. Marquez (subject officer)",
        "Officer T. Chen (witness officer, Marquez's partner)",
        "Complainant D. Alvarez",
        "Civilian eyewitness (late-disclosed)",
        "IA Sergeant (case conference lead)",
        "Deputy Chief (command, receives preliminary briefing)"
      ],
      "technical_terms_to_use": [
        "use-of-force continuum",
        "objectively reasonable standard",
        "sustained/unsustained/exonerated finding",
        "body-worn camera (BWC) review",
        "totality of circumstances",
        "preliminary briefing",
        "case conference",
        "administrative investigation timeline"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "asymmetrical skepticism",
        "recency effect",
        "groupthink",
        "cognitive dissonance",
        "any explicit bias-naming or psychological labeling"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Complainant's written statement alleging excessive force",
          "Complainant's prior record includes a resisting-arrest arrest",
          "Officer Marquez's incident report describing a compliant-turned-resistant subject",
          "Two prior unfounded complaints against Marquez on file"
        ],
        "new_information_after_decision": [
          "Dispatch audio confirms a routine stop for expired registration, not a high-risk call",
          "Medical report shows a wrist fracture consistent with either resistance or excessive force"
        ],
        "alternatives": [
          "Request equivalent background and corroboration checks for both the complainant and the officer before forming any working view",
          "Prioritize whichever record is administratively fastest to obtain, acknowledging that the resulting file may be temporarily lopsided",
          "Delay any credibility assessment until dispatch audio and medical records arrive"
        ],
        "intended_action": "Investigator requests records for both parties but notes that the complainant's file (arrest history) returns faster than a formal review of the officer's disciplinary and training file, producing a genuinely uneven evidentiary picture at intake that is openly flagged as incomplete rather than treated as settled."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Full 18-minute BWC footage (with a 40-second reactivation gap)",
          "Early footage shows a calm verbal exchange and Marquez's initial de-escalation attempts",
          "Final 90 seconds show a rapid takedown after the subject pulls his arm away",
          "Written report from Officer Chen corroborating the takedown as necessary"
        ],
        "new_information_after_decision": [
          "Slowed-frame audio analysis reveals Marquez raised his voice and stepped into the subject's space nearly 3 minutes before the takedown",
          "Use-of-force expert consultant states the earlier positioning is relevant but not independently dispositive"
        ],
        "alternatives": [
          "Score proportionality using the full sequence, explicitly weighing the unresolved 40-second gap as a limiting factor on any conclusion",
          "Treat the takedown segment as the operative use-of-force event for review purposes while flagging the earlier minutes as requiring a second pass",
          "Commission a formal frame-by-frame review before forming any working assessment, accepting the added delay"
        ],
        "intended_action": "Investigator documents that both the injury-producing segment and the earlier interaction carry some evidentiary weight, explicitly states that the 40-second gap prevents a fully confident proportionality read, and defers a firm characterization pending the consultant's input rather than settling on one segment as controlling."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Case conference with IA Sergeant and two peer investigators scheduled on day 6",
          "Sergeant supervised Marquez for 3 years and offers a favorable but explicitly qualified view ('generally solid, but I wasn't there')",
          "One peer investigator raises the unaddressed 40-second BWC gap as worth flagging",
          "Preliminary written summary due to the Deputy Chief within 48 hours of the conference"
        ],
        "new_information_after_decision": [
          "The peer investigator's concern about the BWC gap is formally logged as an open item in the case file",
          "The Deputy Chief's briefing note explicitly states the finding is preliminary and that the gap remains unresolved"
        ],
        "alternatives": [
          "Formally table the BWC gap as an open item requiring follow-up before any preliminary characterization is finalized",
          "Reach a working majority view while explicitly recording the dissenting concern and the reasons it was not resolved",
          "Postpone the preliminary summary until the gap is addressed, accepting schedule risk against the 48-hour window"
        ],
        "intended_action": "Investigator and the panel discuss differing readings of the footage and the sergeant's characterization, explicitly weigh the unresolved gap, and produce a preliminary summary that states the finding is tentative and flags the dissenting concern by name in the file, without the group converging prematurely or the dissent being dropped."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary briefing already delivered to the Deputy Chief on day 8, explicitly described as tentative pending outstanding items",
          "On day 10, a civilian eyewitness statement is obtained, describing Marquez as 'aggressive from the start' and disputing the calm-exchange characterization",
          "The eyewitness account partially conflicts with the early BWC minutes previously reviewed",
          "Deadline for final determination is day 14"
        ],
        "new_information_after_decision": [
          "A supplemental review by a second investigator confirms the eyewitness had an unobstructed view but was 35 feet away",
          "Command asks whether the preliminary briefing should be revised in light of the new statement"
        ],
        "alternatives": [
          "Treat the eyewitness statement as one additional data point, weighed against footage and distance/reliability factors, and update the briefing accordingly",
          "Conclude the eyewitness statement, while relevant, does not on its own resolve the proportionality question given its distance limitations, and document that reasoning explicitly",
          "Request additional canvassing before finalizing, given that one late statement conflicts with an otherwise reviewed record"
        ],
        "intended_action": "Investigator weighs the eyewitness statement's reliability (distance, view, timing) against the footage record on its merits, explicitly revises the briefing language to reflect residual uncertainty rather than either fully adopting or fully discounting the new statement, and documents the reasoning for the resulting mixed determination."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how you first received and triaged this complaint.",
        "What was your initial read on the credibility of each party before reviewing any footage?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of the BWC review, minute by minute if you can.",
        "When did the case conference happen relative to your evidence review, and who was present?",
        "When exactly did the eyewitness statement come in, and how did that fit into your existing timeline?"
      ],
      "decision_point_probes": [
        "What made the background checks come back at different speeds, and how did that affect your intake picture?",
        "How did you handle the fact that the footage has a gap right after initial contact?",
        "What was said in the case conference, and how did the group handle the disagreement about the gap?",
        "How did you weigh the eyewitness statement against the footage you'd already reviewed?"
      ],
      "cues_information_sources": [
        "What cues told you the BWC gap mattered, or that it might not matter much?",
        "Which document or footage segment felt least resolved to you, and why?"
      ],
      "goals_alternatives": [
        "What were you trying to protect or establish at each stage—department credibility, officer fairness, complainant fairness?",
        "What alternative approach to the case conference did you consider, if any?"
      ],
      "decision_basis": [
        "What specific evidence, in your own words, left you most uncertain in this case?",
        "If you had to defend your final determination to an outside auditor, what would you point to first, and what would you concede is still unresolved?"
      ],
      "prior_experience": [
        "Had you worked with Officer Marquez's file before? Did that history inform your expectations?",
        "Has a case conference ever surfaced a disagreement that stayed unresolved through to the final finding? What was different this time?"
      ],
      "time_pressure": [
        "How did the 14-day deadline affect your review pace, especially once the eyewitness statement came in late?"
      ],
      "uncertainty": [
        "What part of this case are you least confident about, even now?",
        "Was there a point where you felt the evidence was genuinely ambiguous, in a way you couldn't fully resolve?"
      ],
      "closing_hypotheticals": [
        "If the eyewitness statement had arrived on day 2 instead of day 10, do you think your review would have unfolded differently?",
        "If you had been the only reviewer, without a case conference, do you think your finding would have been the same?",
        "Looking back, is there a point where you'd handle the sequencing of evidence review differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "LE_Biased_5",
      "features_to_match": [
        "Same domain, role, actors (Marquez, Chen, Alvarez, Sergeant, Deputy Chief, civilian eyewitness)",
        "Same incident facts: Cedar Street expired-registration stop, takedown, wrist fracture, 40-second BWC gap, two prior unfounded complaints against Marquez, two prior arrests for Alvarez including resisting arrest",
        "Same four-phase chronology: intake, BWC review, case conference, late-evidence finalization",
        "Same administrative constraints: 14-day deadline, 48-hour briefing window, day-10 eyewitness statement, 35-foot viewing distance",
        "Same technical vocabulary and difficulty level",
        "Same emotional tone: professional, reflective, moderately self-critical"
      ],
      "features_to_remove_or_change": [
        "Remove unequal verification effort between complainant and officer; replace with resource-driven asymmetry that is explicitly flagged as incomplete rather than treated as settled",
        "Remove anchoring of proportionality judgment on the final footage segment alone; replace with an explicitly deferred, gap-acknowledging assessment",
        "Remove rapid unchallenged consensus formation at the case conference; replace with a documented, unresolved dissent that is formally logged",
        "Remove disproportionate weighting of the late eyewitness statement due to freshness; replace with a reliability-based (distance/view) weighing that is stated on its own terms",
        "Remove reconciliation of new evidence with a prior communicated command position for consistency's sake; replace with an explicit revision of the briefing language to reflect genuine residual uncertainty"
      ],
      "ambiguity_boundary": "The interview must leave real interpretive uncertainty at every decision point—e.g., whether the resource-driven records asymmetry at intake was fair, whether the BWC gap should have blocked a preliminary view, whether the sergeant's qualified endorsement unduly colored the room, and whether the eyewitness's distance undermines her account enough to discount it. These remain open and multiply explicable by ordinary operational constraints and reasonable disagreement, but the text must not describe reasoning that matches the mechanism of confirmation bias/asymmetrical skepticism, recency effects, groupthink, or cognitive dissonance as defined in the paired manifest."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 4 decision points, each with at least 2 stated alternatives.",
      "Confirm zero intended bias instances are embedded for any of the four named biases.",
      "Confirm the BWC gap, the sergeant's framing, the late eyewitness statement, and the prior command briefing are all present but resolved through explicitly reasoned, non-mechanistic handling (flagged uncertainty, logged dissent, reliability-based weighing, explicit revision).",
      "Confirm no bias name, definition, or psychological label appears in the public interview text.",
      "Confirm the scenario matches LE_Biased_5 in actors, facts, chronology, vocabulary, and difficulty, differing only in how each decision is reasoned through.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm final word count target of 1,350 words falls within 1,215-1,485 words.",
      "Confirm ambiguity is achieved through genuine operational constraint and documented disagreement, not through exaggerated contradiction or artificial neutrality."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      { "bias": "Cognitive dissonance", "occurrences": 0, "mechanism_constraint": "No post-commitment reconciliation of a prior communicated position may be embedded; any evidence revision must be explicitly reasoned on reliability grounds." },
      { "bias": "Recency Effects", "occurrences": 0, "mechanism_constraint": "No disproportionate weighting of the most-recently-reviewed footage segment or most-recently-obtained testimony due to temporal position may be embedded." },
      { "bias": "Groupthink", "occurrences": 0, "mechanism_constraint": "No rapid unchallenged consensus formation with unpursued dissent may be embedded; dissent must be explicitly logged." },
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "occurrences": 0, "mechanism_constraint": "No unequal verification effort applied to the complainant versus the officer may be embedded; any asymmetry must be resource-driven and explicitly flagged as incomplete." }
    ],
    "target_bias_names": [
      "Cognitive dissonance",
      "Recency Effects",
      "Groupthink",
      "Confirmation Bias and Asymmetrical skepticism"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Cognitive dissonance", "requested_occurrences": 0 },
      { "bias": "Recency Effects", "requested_occurrences": 0 },
      { "bias": "Groupthink", "requested_occurrences": 0 },
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "LE_Biased_5",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Ambigious_5",
    "domain_id": "LE",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, which mandates zero intended occurrences of every bias named in the paired manifest regardless of the nonzero counts supplied in the caller's input manifest. The supplied manifest ([Cognitive dissonance:1, Recency Effects:2, Groupthink:1, Confirmation Bias and Asymmetrical skepticism:1]) is treated as identifying the paired target-bias set from LE_Biased_5 for exclusion purposes only, not as an occurrence count to embed.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and role (Internal Affairs Investigator, municipal PD)",
      "Core incident facts (Cedar Street expired-registration stop, takedown, wrist fracture)",
      "All named actors and their prior histories",
      "The 40-second BWC gap",
      "The 14-day deadline and 48-hour briefing window",
      "The day-10 eyewitness statement and 35-foot viewing distance",
      "Four-decision-point structure and approximate word count",
      "Technical vocabulary and difficulty level"
    ],
    "generation_warnings": [
      "The caller's input manifest for this scenario specifies nonzero occurrence counts (1, 2, 1, 1) identical to the paired biased scenario LE_Biased_5, which conflicts with the ambiguous_control condition rule requiring zero intended occurrences of all named target biases. Per the CONDITION RULES, the condition value governs: this specification implements zero intended occurrences for every listed bias and repurposes the supplied manifest solely as the definition of the paired target-bias set to be avoided, not as an embedding instruction. The dataset controller should confirm this interpretation before validation."
    ]
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "seg_001",
          "speaker": "Participant",
          "segment_type": "intake_background_reasoning",
          "raw_interview_anchor": "Alvarez's record came back within a day, since it's just a records-system pull. Marquez's full file took almost a week because it required a request through the union rep and a records custodian. So for several days I had a fuller picture of one side than the other, which I noted explicitly in my log as a limitation, not a conclusion.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden validation manifest requires zero occurrences. The resource-driven record asymmetry is explicitly flagged as incomplete rather than used as unequal verification or a settled credibility judgment."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "bwc_gap_and_proportionality_reasoning",
          "raw_interview_anchor": "I logged both segments as carrying weight and noted the gap as a limiting factor on any proportionality conclusion I might draw. I didn't want to lock in a read before the consultant weighed in.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden validation manifest requires zero occurrences. Both footage segments are weighed and the gap is treated as a limiting uncertainty, with no temporal overweighting of the final segment."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "case_conference_reasoning",
          "raw_interview_anchor": "There wasn't a quick consensus—two of us thought the gap was potentially significant given the timing relative to the escalation audio, one thought Chen's corroboration and the visible resisting motion carried it regardless. We didn't resolve that disagreement in the room. I logged the dissenting view by name in the case file and noted the preliminary summary as tentative pending the gap issue.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden validation manifest requires zero occurrences. The conference preserves disagreement, logs dissent, and keeps the summary tentative rather than forming rapid unchallenged consensus."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "late_evidence_revision_reasoning",
          "raw_interview_anchor": "I ended up revising the briefing language to reflect that the finding remained more open than the initial note suggested, rather than either adopting her account outright or setting it aside.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden validation manifest requires zero occurrences. The late eyewitness is weighed by distance, view, and lighting, and the prior briefing is explicitly revised rather than defended for consistency."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": ["Interviewer", "Participant"],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Conservative, mechanism-first analysis of self-reported IA review reasoning. The participant repeatedly identified and logged uncertainty, noted informational asymmetry as a limitation rather than a conclusion, and revised a preliminary judgment in response to new evidence. No affirmative evidence of a bias-specific mechanism affecting a specific reasoning operation or outcome met the occurrence standard; plausible social/information influences are listed as candidates only."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Authority bias",
        "alternative_labels": ["Authority gradient", "Status bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant during case conference",
        "possible_decision_episode_label": "Weighting of sergeant's supervisor history with Officer Marquez during case conference",
        "supporting_interview_quote": "It was mentioned, and it's fair to say it's not nothing—people listen when a three-year supervisor speaks. But he qualified it himself, and the discussion kept coming back to what was and wasn't on the tape rather than settling on his character read. I can't say for certain it had zero influence, but I also can't point to a moment where it overrode the evidentiary discussion.",
        "plausible_mechanism": "Authority/status-based social influence could lead participants to overweight the sergeant's character assessment even when the discussion appears focused on evidence.",
        "why_not_identified": "The participant explicitly qualified the influence, could not identify any specific decision overridden, and the group logged dissent and kept returning to tape evidence; no reasoning operation or outcome is affirmatively shown to have been affected."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "Anchoring",
        "alternative_labels": ["Anchoring and adjustment", "Confirmation bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Initial asymmetry of background records before officer file arrived",
        "supporting_interview_quote": "Alvarez's record came back within a day, since it's just a records-system pull. Marquez's full file took almost a week because it required a request through the union rep and a records custodian. So for several days I had a fuller picture of one side than the other, which I noted explicitly in my log as a limitation, not a conclusion.",
        "plausible_mechanism": "Earlier exposure to Alvarez's prior arrests could anchor initial impressions or make complainant-favorable information more available before the officer's background arrived.",
        "why_not_identified": "The participant logged it as a limitation rather than a conclusion and stated he tried not to let it affect his approach; no specific judgment or decision is shown to have been anchored by the uneven record."
      },
      {
        "candidate_id": "cand_003",
        "classification_status": "candidate",
        "proposed_bias_label": "Commitment and consistency bias",
        "alternative_labels": ["Escalation of commitment", "Consistency bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Incorporation of late eyewitness statement after preliminary note to Deputy Chief",
        "supporting_interview_quote": "It wasn't comfortable revising something I'd already sent up, but the distance and lighting were the actual basis for how much weight I gave her account—not really about protecting what I'd said earlier. I'd rather have gotten it right than tidy.",
        "plausible_mechanism": "Having already sent a preliminary note may create commitment to the prior assessment, making it harder to incorporate contradictory evidence fully or biasing that incorporation toward the prior view.",
        "why_not_identified": "The participant reports revising the briefing, attributes the weighting to distance and lighting, and explicitly disclaims protecting the earlier note; no affirmative effect on the final reasoning or decision is demonstrated."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "The analysis relies on participant self-report, which may under-report implicit social influence or motivated reasoning.",
      "The retrieved corpus was sparse and not directly aligned with internal-affairs review context; no retrieved source was used for an identified occurrence.",
      "The analysis cannot compare the participant's account with actual case-file evidence, video footage, or other reviewers' decision processes."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Ambigious_5_Sonnet_on",
  "interview_id": "LE_Ambigious_5",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
