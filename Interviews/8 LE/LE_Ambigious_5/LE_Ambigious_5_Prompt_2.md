You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Ambigious_5",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
