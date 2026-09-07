You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EI_Biased_4",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "School Principal / Building Administrator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Cafeteria Video Incident: Discipline, Rumor, and a Threatened Walkout",
    "scenario_summary_internal": "A mid-size public high school principal must respond within a single school day to a filmed physical altercation between two students that circulates on social media, triggers conflicting eyewitness accounts, provokes accusations of unequal disciplinary treatment along racial/social-group lines, and escalates into a planned student walkout by mid-afternoon. The principal must decide how to open the investigation, how to assign discipline under incomplete information, how to communicate with parents/media, and how to manage the walkout threat while maintaining safety and legal defensibility — all inside roughly five hours with no time for a full formal investigation.",
    "occupational_realism": {
      "objective": "Contain a fast-moving disciplinary and reputational crisis while protecting student safety, ensuring fair and defensible discipline, and maintaining trust with families and staff, all before the end of the school day.",
      "setting": "A public high school of approximately 1,100 students; incident begins at 11:40 AM during lunch period and must be substantially resolved by the 3:15 PM dismissal bell.",
      "constraints": [
        "No more than 5 hours before dismissal and a planned walkout",
        "Only partial video footage and conflicting witness statements available",
        "District policy requires discipline decisions to be defensible under due-process review",
        "Assistant principal and school resource officer have competing priorities and limited availability",
        "Parents and a local news reporter are already calling the front office",
        "Superintendent's office expects a same-day incident summary"
      ],
      "stakeholders": [
        "Principal (protagonist)",
        "Assistant Principal",
        "School Resource Officer",
        "Two students involved in the altercation and their families",
        "Classroom teachers and lunch monitors",
        "District communications office",
        "Student body / informal leaders organizing the walkout"
      ],
      "technical_terms_to_use": [
        "progressive discipline matrix",
        "due process notice",
        "restorative conference",
        "incident report",
        "chain of custody (for video evidence)",
        "de-escalation protocol"
      ],
      "technical_terms_to_avoid": [
        "bounded rationality",
        "satisficing",
        "confirmation bias",
        "rationalization",
        "self-serving attribution",
        "illusion of understanding",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "A 12-second video clip showing one student shoving another near the cafeteria exit",
          "Two lunch monitors' brief verbal reports, partially contradictory",
          "A crowd of roughly 30 students dispersing before staff arrived",
          "No footage of what happened immediately before the shove"
        ],
        "new_information_after_decision": [
          "A second, longer video surfaces an hour later showing the sequence differently",
          "A teacher reports overhearing a verbal provocation not visible in the first clip"
        ],
        "alternatives": [
          "Open a full multi-witness investigation before separating students, delaying lunch dismissal",
          "Act immediately on the first video and monitor statements to separate and question the two students, deferring further evidence-gathering",
          "Call the resource officer to hold both students until every available witness is interviewed"
        ],
        "intended_action": "Principal separates the two students and begins questioning based only on the first clip and monitor reports, treating this as sufficient to proceed."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The second video and the overheard provocation, which complicate who instigated the conflict",
          "One student has two prior minor conduct referrals; the other has none",
          "Assistant principal's preliminary notes lean toward the student with prior referrals being primarily at fault",
          "Parents of the student with no prior record are already on their way to the school"
        ],
        "new_information_after_decision": [
          "A third witness later states the provocation came from the student with no prior referrals",
          "Discipline decision is issued before this third statement is logged"
        ],
        "alternatives": [
          "Pause the discipline decision until the third witness can be located and interviewed",
          "Finalize a discipline decision consistent with the emerging narrative that fits the prior-referral history",
          "Apply an interim, reversible consequence (e.g., short cooling-off removal) pending full review"
        ],
        "intended_action": "Principal finalizes an in-school suspension for the student with prior referrals, integrating the new video and prior history into a single confident account of what happened, explaining away the parts that don't fit."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Rumors are circulating that discipline was applied unevenly based on the students' social groups",
          "District communications office requests a same-day public statement",
          "Principal has not yet reviewed the third witness statement or consulted the school counselor about group dynamics",
          "Principal feels confident the situation is now fully explained based on the video and referral history"
        ],
        "new_information_after_decision": [
          "The counselor later notes an unresolved peer conflict dating back weeks that neither video nor referral history captured",
          "Several students state the walkout is about fairness perceptions, not just this single incident"
        ],
        "alternatives": [
          "Issue a statement acknowledging the incident is still under review and details may change",
          "Issue a confident, finalized public statement asserting the sequence of events and rationale for discipline as fully understood",
          "Delay any public statement until the counselor's input and all witness statements are collected"
        ],
        "intended_action": "Principal issues a confident public statement describing the incident and discipline rationale as fully resolved and understood, without flagging remaining uncertainty."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Walkout occurs briefly at 2:45 PM but ends peacefully within 20 minutes with no injuries",
          "Assistant principal and resource officer contributed significantly to on-the-ground de-escalation during the walkout",
          "District superintendent asks the principal for an end-of-day summary of how the crisis was handled",
          "Some staff privately note the walkout was defused partly by lucky timing (a scheduled fire drill nearby drew students back inside)"
        ],
        "new_information_after_decision": [
          "Follow-up review two days later finds the discipline decision needs partial revision once the third witness statement is fully weighed",
          "Staff feedback survey shows mixed views on whether the crisis was handled well"
        ],
        "alternatives": [
          "Attribute the peaceful outcome broadly to the full team's efforts and acknowledge the role of chance factors",
          "Frame the peaceful resolution primarily as a result of the principal's own quick judgment and leadership decisions",
          "Withhold judgment on the outcome's causes until a fuller after-action review is completed"
        ],
        "intended_action": "Principal frames the end-of-day summary to the superintendent as evidence of the principal's own effective, decisive leadership, downplaying the resource officer's, assistant principal's, and circumstantial contributions."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were told when this incident first came to your attention.",
        "What was your overall goal in the first few minutes after hearing about the altercation?"
      ],
      "timeline_reconstruction": [
        "What information did you have at each stage, and what changed as the day went on?",
        "When did the second video and the additional witness statements reach you, and how did that affect your thinking?"
      ],
      "decision_point_probes": [
        "At the point you separated the students, what alternatives did you consider besides acting on the first clip?",
        "When you finalized the discipline decision, how did you weigh the new video against the prior referral history?",
        "What made you confident enough to issue a public statement when you did?",
        "In your summary to the superintendent, how did you decide which factors to highlight as reasons the walkout ended peacefully?"
      ],
      "information_sources": [
        "Which sources did you trust most at each stage — video, staff reports, student accounts — and why?",
        "Was there information you didn't have time to seek out? How did you handle that gap?"
      ],
      "goals_and_alternatives": [
        "What competing goals were you balancing at each decision point?",
        "Looking back, what other options were realistically available to you at the time?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision at each of these four points?"
      ],
      "prior_experience": [
        "Did past incidents like this one shape how you read this situation?"
      ],
      "time_pressure_and_uncertainty": [
        "How much uncertainty did you feel you were operating under, and how did that affect your confidence in your conclusions?",
        "Where did the time constraint most affect the quality of information you could gather?"
      ],
      "closing_hypotheticals": [
        "If you'd had the third witness statement before finalizing discipline, would anything have changed?",
        "If the walkout had turned confrontational instead of peaceful, how would you describe today differently?",
        "What would you do differently if a similar incident happened again tomorrow?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 1,
        "mechanism": "Under severe time pressure and incomplete evidence, the principal treats the first available video clip and two brief monitor reports as an adequate basis for immediate action rather than seeking a fuller (but slower) investigation, satisficing on a workable-but-incomplete information set.",
        "affected_reasoning_operation": "Evidence sufficiency judgment / stopping rule for information search",
        "evidence_available_at_time": [
          "12-second video clip",
          "two partially contradictory monitor reports",
          "dispersed crowd with no other immediate witnesses"
        ],
        "required_textual_manifestation": "Principal explicitly states that pursuing a fuller investigation before acting was 'not realistic' given lunch-period logistics and proceeds to question and separate students using only the two available accounts.",
        "plausible_nonbias_interpretation": "A reasonable administrator might argue that immediate separation is a safety-first best practice regardless of evidentiary completeness.",
        "strength": "subtle",
        "do_not_make_explicit": ["bounded rationality", "satisficing", "limited information processing capacity"]
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 2,
        "mechanism": "When the second video and overheard provocation complicate the emerging story, the principal integrates the new, partially conflicting information into a single tidy narrative consistent with the prior-referral student being at fault, rather than treating the inconsistency as genuinely unresolved.",
        "affected_reasoning_operation": "Integration of new evidence into an existing causal narrative",
        "evidence_available_at_time": [
          "second video complicating who instigated",
          "overheard provocation not visible in first clip",
          "one student's prior referral history",
          "assistant principal's preliminary lean"
        ],
        "required_textual_manifestation": "Principal describes explaining away the provocation detail as 'consistent with' the student's known pattern, producing a single coherent account rather than acknowledging the account is still contested.",
        "plausible_nonbias_interpretation": "Weighing prior conduct history as a legitimate risk factor in a progressive discipline matrix is a defensible policy practice.",
        "strength": "moderate",
        "do_not_make_explicit": ["rationalization", "coherence-based reasoning", "motivated reasoning"]
      },
      {
        "instance_id": "iu_01",
        "bias": "Illusion of understanding",
        "decision_point": 3,
        "mechanism": "Before issuing a public statement, the principal expresses confident, complete understanding of the incident's causes and dynamics, despite not having reviewed the third witness statement or consulted the counselor about the underlying weeks-long peer conflict.",
        "affected_reasoning_operation": "Confidence calibration about causal knowledge prior to public commitment",
        "evidence_available_at_time": [
          "video and referral-history-based narrative from decision point 2",
          "unreviewed third witness statement",
          "uncontacted counselor with relevant background information",
          "rumors of unequal treatment perception"
        ],
        "required_textual_manifestation": "Principal states the situation is 'fully understood' or equivalent and issues a finalized public account without flagging that key sources (counselor, third witness) were not yet consulted.",
        "plausible_nonbias_interpretation": "A principal might reasonably feel a public statement needs to project confidence to reassure parents, independent of actual epistemic certainty.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of understanding", "overconfidence", "epistemic miscalibration"]
      },
      {
        "instance_id": "se_01",
        "bias": "Self-Enhancement or Self-serving Bias",
        "decision_point": 4,
        "mechanism": "In summarizing the peaceful resolution of the walkout to the superintendent, the principal attributes the favorable outcome primarily to their own decisive leadership while downplaying the assistant principal's and resource officer's on-the-ground contributions and the fortuitous, unrelated fire drill that helped disperse students.",
        "affected_reasoning_operation": "Causal attribution of a favorable outcome to self versus external/team/chance factors",
        "evidence_available_at_time": [
          "assistant principal and resource officer's active de-escalation role during the walkout",
          "the incidental fire drill that helped draw students back inside",
          "mixed staff feedback on the day's handling"
        ],
        "required_textual_manifestation": "Principal's account of the end-of-day summary foregrounds their own judgment and decisions as the reason things ended well, mentioning colleagues and the fire drill only briefly or not as causal factors.",
        "plausible_nonbias_interpretation": "A principal reporting to a superintendent may reasonably emphasize their own decision-making because that is the information the superintendent specifically requested.",
        "strength": "subtle",
        "do_not_make_explicit": ["self-serving bias", "self-enhancement", "attribution bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control specified in this request."
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
      "Confirm exactly four decision points are present, each with at least two plausible alternatives.",
      "Confirm each of the four bias instances is embedded at its assigned decision point and nowhere else.",
      "Confirm no bias label, definition, or psychological terminology appears in the interview text.",
      "Confirm total word count falls between 1,215 and 1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm consequences (peaceful walkout end, later partial revision of discipline) do not mechanically prove or disprove bias presence.",
      "Confirm each instance has a distinguishable evidence trace separate from the other three instances."
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
