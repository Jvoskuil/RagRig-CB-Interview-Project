You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Biased_5",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Internal Affairs Investigator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Cedar Street Stop: Use-of-Force Complaint Review",
    "scenario_summary_internal": "An Internal Affairs (IA) investigator is assigned to review a citizen complaint alleging excessive force by Officer R. Marquez during a late-night traffic stop that ended in a takedown and a minor injury to the driver. The investigator must triage the complaint, review body-worn camera (BWC) footage and written reports, consult with peer investigators and a sergeant at a case conference, and reach a final sustained/unsustained determination after a delayed witness statement surfaces. The case is nonroutine because the complainant has a prior record (creating scrutiny asymmetry), the officer is well-regarded and previously cleared in two prior complaints (creating in-group trust), and new evidence arrives late in the process, after the investigator has already reported a preliminary impression to command.",
    "occupational_realism": {
      "objective": "Determine whether Officer Marquez's use of force during the Cedar Street stop was objectively reasonable and consistent with department use-of-force policy, and issue a sustained/unsustained/exonerated finding supported by the case file.",
      "setting": "Municipal police department Internal Affairs Bureau, over a 12-day review period following a citizen complaint filed the morning after the incident.",
      "constraints": [
        "14-day departmental deadline to issue a preliminary finding",
        "BWC footage has a 40-second gap due to a camera reactivation delay",
        "Complainant has two prior arrests, one for resisting arrest, which is known to the investigator before the interview",
        "Officer Marquez has 9 years of service, two prior complaints both closed as unfounded",
        "Sergeant on the review panel supervised Marquez for 3 years and voices strong support early in the case conference",
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
          "Open a full parallel review of both accounts with equal initial scrutiny and independent evidence requests",
          "Prioritize verifying the complainant's account for inconsistencies before scheduling the officer interview",
          "Request an expedited command briefing before any evidence review"
        ],
        "intended_action": "Investigator opens the file by requesting corroborating detail for the complainant's account (criminal history, prior conduct) while accepting the officer's report as a working baseline pending contrary evidence."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Full BWC footage (18 minutes) covering the stop from approach to handcuffing",
          "Early footage shows a calm verbal exchange and Marquez's initial de-escalation attempts",
          "Final 90 seconds show a rapid takedown after the subject pulls his arm away",
          "Written report from Officer Chen corroborating the takedown as necessary"
        ],
        "new_information_after_decision": [
          "Slowed-frame audio analysis reveals Marquez raised his voice and stepped into the subject's space nearly 3 minutes before the takedown, a detail not emphasized in either report",
          "Use-of-force expert consultant notes the earlier positioning as relevant to reasonableness"
        ],
        "alternatives": [
          "Score proportionality based on the full 18-minute sequence, weighting early de-escalation and late escalation equally",
          "Focus the proportionality assessment primarily on the final takedown sequence since that is what generated the injury",
          "Request a third-party use-of-force expert review before forming any working assessment"
        ],
        "intended_action": "Investigator's working assessment of proportionality is anchored heavily on the final takedown sequence, treating the earlier de-escalation minutes as largely settled and less relevant to the reasonableness judgment."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Case conference with IA Sergeant and two peer investigators scheduled on day 6",
          "Sergeant supervised Marquez for 3 years and states early in the meeting that Marquez has 'never been a problem'",
          "One peer investigator raises the unaddressed 40-second BWC gap as worth flagging",
          "Preliminary written summary due to the Deputy Chief within 48 hours of the conference"
        ],
        "new_information_after_decision": [
          "The peer investigator who raised the BWC gap later privately tells the investigator she still had reservations but did not press the point in the room",
          "The Deputy Chief's briefing note reflects the majority view reached in the meeting, not the flagged concern"
        ],
        "alternatives": [
          "Formally table the BWC gap as an open item requiring follow-up before any preliminary characterization is finalized",
          "Adopt the room's quickly-formed consensus that the force was likely justified and move to drafting the preliminary summary",
          "Request a recorded dissent or minority note be attached to the case file"
        ],
        "intended_action": "Investigator aligns with the sergeant-led consensus that the force was likely justified, and the unresolved BWC gap is set aside without documented follow-up, matching the group's converging view rather than the individual reservation raised in the room."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary briefing already delivered to the Deputy Chief on day 8 indicating a likely exonerated finding",
          "On day 10, a civilian eyewitness statement is finally obtained, describing Marquez as 'aggressive from the start' and disputing the calm-exchange characterization",
          "The eyewitness account partially conflicts with the early BWC minutes previously reviewed",
          "Deadline for final determination is day 14"
        ],
        "new_information_after_decision": [
          "A supplemental review by a second investigator confirms the eyewitness had an unobstructed view but was 35 feet away",
          "Command asks for confirmation that the preliminary briefing still stands"
        ],
        "alternatives": [
          "Treat the new eyewitness statement as one data point to be weighed alongside the full BWC record and re-open the proportionality analysis",
          "Give the most recently obtained eyewitness statement primary weight in finalizing the determination since it is the newest account",
          "Formally revise the preliminary briefing to reflect uncertainty and request additional time before finalizing"
        ],
        "intended_action": "Investigator both over-weights the newly obtained eyewitness statement relative to the earlier BWC record when finalizing language, and separately reconciles the tension between the earlier command briefing (already committed to an exonerated leaning) and the new conflicting evidence by minimizing the eyewitness account's relevance rather than revising the briefing, preserving consistency with the position already reported upward."
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
        "What specifically made you request more detail on the complainant's background before the officer's account?",
        "How did you weigh the first 15 minutes of footage against the final 90 seconds when forming your proportionality judgment?",
        "What was said in the case conference that shaped the room's direction, and did anyone disagree?",
        "How did the eyewitness statement change your written determination, if at all?"
      ],
      "cues_information_sources": [
        "What cues told you the dispatch call type mattered or didn't matter?",
        "Which document or footage segment carried the most weight in your mind, and why?"
      ],
      "goals_alternatives": [
        "What were you trying to protect or establish at each stage—department credibility, officer fairness, complainant fairness?",
        "What alternative approach to the case conference did you consider, if any?"
      ],
      "decision_basis": [
        "What specific evidence, in your own words, most drove your preliminary finding?",
        "If you had to defend your final determination to an outside auditor, what would you point to first?"
      ],
      "prior_experience": [
        "Had you worked with Officer Marquez's file before? Did that history inform your expectations?",
        "Has a case conference ever changed your individual view before? What was different this time?"
      ],
      "time_pressure": [
        "How did the 14-day deadline affect your review pace, especially once the eyewitness statement came in late?"
      ],
      "uncertainty": [
        "What part of this case are you least confident about, even now?",
        "Was there a point where you felt the evidence was genuinely ambiguous?"
      ],
      "closing_hypotheticals": [
        "If the eyewitness statement had arrived on day 2 instead of day 10, would your review have unfolded differently?",
        "If you had been the only reviewer, without a case conference, do you think your finding would have been the same?",
        "Looking back, is there a point where you'd handle the sequencing of evidence review differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cbas_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "decision_point": 1,
        "mechanism": "Investigator applies differential scrutiny: actively seeking disconfirming background detail (prior arrests) on the complainant while accepting the officer's incident report as a default baseline without an equivalent verification request.",
        "affected_reasoning_operation": "Initial evidence-selection and credibility weighting at case intake",
        "evidence_available_at_time": [
          "Complainant's written statement",
          "Complainant's prior arrest record",
          "Officer's incident report",
          "Two prior unfounded complaints against the officer"
        ],
        "required_textual_manifestation": "Investigator explicitly describes requesting corroboration/background checks for the complainant but not initiating equivalent independent verification of the officer's narrative at the same stage.",
        "plausible_nonbias_interpretation": "Standard intake procedure may reasonably prioritize checking complainant credibility first since a formal report already exists from the officer's side.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "asymmetrical skepticism", "double standard of proof"]
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "decision_point": 2,
        "mechanism": "In weighing an 18-minute BWC sequence, the investigator's proportionality judgment is anchored on the final 90-second takedown segment, treating earlier de-escalation minutes as settled and discounting their relevance to the overall reasonableness assessment.",
        "affected_reasoning_operation": "Integration and weighting of sequential evidence when forming an overall judgment",
        "evidence_available_at_time": [
          "Full 18-minute BWC footage",
          "Early calm exchange and de-escalation attempt",
          "Final takedown sequence",
          "Officer Chen's corroborating report"
        ],
        "required_textual_manifestation": "Investigator, when asked how proportionality was assessed, describes the takedown moment as the primary basis for judgment and treats the earlier minutes as background rather than integral evidence.",
        "plausible_nonbias_interpretation": "The takedown is the moment force was actually applied, so focusing there could be a legitimate scoping choice tied to the injury being reviewed.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "primacy vs recency", "anchoring on final segment"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "In the case conference, the sergeant's strong early framing produces rapid convergence toward a shared 'likely justified' view; a peer investigator's dissenting concern about the BWC gap is raised but not pursued once the group direction is set, and the investigator adopts the consensus without documenting the unresolved concern.",
        "affected_reasoning_operation": "Group deliberation and consensus formation prior to a preliminary determination",
        "evidence_available_at_time": [
          "Sergeant's supervisory history and framing statement",
          "Peer investigator's flagged concern about the 40-second BWC gap",
          "Draft preliminary summary due to command"
        ],
        "required_textual_manifestation": "Investigator recounts the case conference discussion, notes the sergeant's early framing, mentions the dissenting concern being raised, and describes the group settling on a shared view without a documented follow-up on the dissent.",
        "plausible_nonbias_interpretation": "Team consensus could reflect genuinely convergent, independently-reasoned judgments rather than social pressure to conform.",
        "strength": "moderate",
        "do_not_make_explicit": ["groupthink", "social conformity pressure", "suppressed dissent"]
      },
      {
        "instance_id": "re_02",
        "bias": "Recency Effects",
        "decision_point": 4,
        "mechanism": "When finalizing the determination, the investigator gives the newly obtained (day 10) eyewitness statement disproportionate weight relative to the earlier, more extensive BWC record, because it was the most recently acquired piece of evidence.",
        "affected_reasoning_operation": "Final evidence-integration and re-weighting near decision closure",
        "evidence_available_at_time": [
          "Late-arriving civilian eyewitness statement (day 10)",
          "Full BWC footage reviewed on day 3",
          "Supplemental review noting eyewitness distance (35 feet)"
        ],
        "required_textual_manifestation": "Investigator describes the eyewitness statement as significantly shifting the picture in the final determination discussion, disproportionate to its evidentiary weight relative to the earlier, fuller BWC record.",
        "plausible_nonbias_interpretation": "New eyewitness testimony can legitimately warrant serious consideration, especially if it directly contradicts a prior characterization.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "most-recent-evidence weighting", "primacy vs recency"]
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "decision_point": 4,
        "mechanism": "Having already delivered a preliminary briefing to the Deputy Chief indicating a likely exonerated finding, the investigator resolves the discomfort of new conflicting eyewitness evidence by minimizing its relevance rather than revising the previously communicated position, preserving consistency with the earlier commitment.",
        "affected_reasoning_operation": "Post-commitment evidence reconciliation and self-justification",
        "evidence_available_at_time": [
          "Preliminary briefing already delivered to command (day 8)",
          "New conflicting eyewitness statement (day 10)",
          "Command's request to confirm the preliminary briefing still stands"
        ],
        "required_textual_manifestation": "Investigator explains the decision to downplay the eyewitness account's relevance in a way that is tied to having already told command a different conclusion, rather than to an independent evidentiary reassessment.",
        "plausible_nonbias_interpretation": "A reasonable investigator might legitimately conclude the eyewitness account carries less weight due to distance and viewing conditions, independent of any prior commitment.",
        "strength": "moderate",
        "do_not_make_explicit": ["cognitive dissonance", "commitment consistency", "post-hoc rationalization"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for this biased-condition scenario; no paired control is being generated under this specification."
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
      "Confirm exactly 5 total bias instances embedded: 1 confirmation-bias/asymmetrical-skepticism, 2 recency-effect, 1 groupthink, 1 cognitive-dissonance.",
      "Confirm no bias name, definition, or psychological label appears in the public interview text.",
      "Confirm re_01 and re_02 use distinct evidence sources (BWC sequence weighting vs. late eyewitness statement weighting) and occur at different decision points.",
      "Confirm cd_01 and re_02 at decision point 4 are textually distinguishable: re_02 concerns evidentiary weighting, cd_01 concerns reconciliation with a prior committed position.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm final word count target of 1,350 words falls within 1,215-1,485 words.",
      "Confirm no unrequested bias (e.g., anchoring, hindsight bias) is intentionally embedded as a labeled instance."
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
