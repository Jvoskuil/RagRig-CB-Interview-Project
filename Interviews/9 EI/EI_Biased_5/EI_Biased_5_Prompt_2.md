You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EI_Biased_5",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "University Admissions Officer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Borderline Transfer File",
    "scenario_summary_internal": "An undergraduate admissions officer manages a borderline international transfer applicant through file screening, an interview disrupted by a citywide transit strike, committee deliberation over a foreign grading scale and a late-surfacing disciplinary note, and a final comparative vote against a network-affiliated finalist, all under a tight decision-cycle deadline.",
    "occupational_realism": {
      "objective": "Decide whether a borderline transfer applicant should be admitted, waitlisted, or denied within a fixed decision-cycle deadline, using a holistic file review, an interview, and committee deliberation.",
      "setting": "Undergraduate admissions office of a mid-size university during a regular transfer-cycle deadline week, involving file review software, an interview room, and a committee meeting.",
      "constraints": [
        "Fixed committee decision deadline with no extension",
        "Limited staff time to independently verify foreign credentials",
        "Interview slots compressed due to a citywide transit strike",
        "Committee must rank multiple borderline finalists against each other",
        "Only one credential-evaluation request can be expedited per cycle"
      ],
      "stakeholders": [
        "Admissions officer (primary decision-maker)",
        "Applicant (international transfer student)",
        "Secondary reference (guidance counselor)",
        "Admissions committee members",
        "International credentials office",
        "Rival borderline finalist and their reference"
      ],
      "technical_terms_to_use": [
        "holistic file review",
        "credential conversion scale",
        "committee deliberation",
        "decision cycle",
        "recommendation letter",
        "interview rubric",
        "waitlist tier",
        "legacy affiliation",
        "disciplinary note",
        "standardized test threshold"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "halo effect",
        "fundamental attribution error",
        "ingroup",
        "ambiguity aversion",
        "belief perseverance",
        "attitude polarization",
        "cognitive",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Applicant transcript from an unfamiliar national exam system",
          "Strong personal essay",
          "Recommendation letter from a teacher at a nationally renowned magnet school with a strong track record of alumni at this university",
          "Standardized test score slightly below the usual admit threshold"
        ],
        "new_information_after_decision": [
          "Later review reveals the recommendation letter used largely generic, template-style language"
        ],
        "alternatives": [
          "Fast-track the file to interview based on the applicant's school reputation and letter",
          "Hold the file for additional independent verification of the below-threshold test score before proceeding"
        ],
        "intended_action": "Officer fast-tracks the applicant to interview, treating the school's reputation and letter as sufficient to offset the below-threshold score."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Interview scheduled during a week of citywide transit strikes",
          "Applicant arrives 12 minutes late and appears flustered",
          "Applicant gives short, hesitant answers in the first several minutes, then improves noticeably"
        ],
        "new_information_after_decision": [
          "Admissions administration later confirms the transit strike caused delays across most interview slots that day"
        ],
        "alternatives": [
          "Note the lateness and initial hesitation as likely tied to the day's transit disruption",
          "Record the lateness and hesitation as reflecting the applicant's personal time-management and composure"
        ],
        "intended_action": "Officer records the lateness and early hesitation in the interview rubric as a personal time-management and composure concern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A second reference (guidance counselor) flags a minor, already-resolved disciplinary note that contrasts with the polished profile formed earlier",
          "The applicant's transcript uses a 20-point national grading scale from a recently reformed system",
          "The international credentials office's guidance for that specific reformed scale is incomplete and flagged as provisional"
        ],
        "new_information_after_decision": [
          "An appeals reviewer later notes the conservative conversion likely undervalued the applicant's actual standing",
          "The reinterpretation of the disciplinary note goes unchallenged in the file"
        ],
        "alternatives": [
          "Revisit and reweight the overall assessment in light of the disciplinary note",
          "Reinterpret the note as inconsequential to preserve the existing favorable assessment",
          "Request an expedited formal credential evaluation for precise conversion of the reformed grading scale",
          "Apply a conservative standard conversion table despite acknowledged uncertainty, to avoid delay"
        ],
        "intended_action": "Officer reinterprets the disciplinary note as inconsequential and applies the conservative conversion table rather than requesting the expedited evaluation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two borderline finalists remain for the last open seat",
          "One finalist has a legacy/regional alumni connection matching the officer's own undergraduate network",
          "The other finalist is unaffiliated with the university's alumni network but has equally borderline metrics"
        ],
        "new_information_after_decision": [
          "The enrollment office later flags that admit rates for network-affiliated legacy candidates in the officer's portfolio are statistically higher than for non-affiliated peers with similar metrics, without clear evidence of differential merit"
        ],
        "alternatives": [
          "Apply identical evaluation weighting to both finalists",
          "Extend discretionary benefit-of-the-doubt weighting to the finalist sharing the officer's own alumni network"
        ],
        "intended_action": "Officer extends discretionary weighting in favor of the network-affiliated finalist during the final committee vote."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this transfer file first came to your attention.",
        "What was your overall objective when you began reviewing this case?"
      ],
      "timeline_reconstruction": [
        "What happened after the file was fast-tracked to interview?",
        "What did you learn between the interview and the committee meeting?",
        "How did the committee deliberation unfold once the disciplinary note surfaced?"
      ],
      "decision_point_probes": [
        "What specific cues in the file led you to fast-track it? What alternative was available?",
        "What information sources did you rely on when scoring the interview, and what was your goal at that moment?",
        "When the disciplinary note came up, what alternatives did you consider, and what tipped your decision?",
        "Why did you choose the conversion table over requesting the expedited credential evaluation?",
        "In the final vote, what was the basis for weighting one finalist over the other? What alternatives existed?",
        "Had you handled a similar borderline case before, and did that prior experience shape this one?"
      ],
      "closing_hypotheticals": [
        "If the applicant had attended a less well-known school, would your initial fast-track decision have been the same?",
        "If the transit strike hadn't happened, do you think your interview notes would read differently?",
        "If neither finalist had any alumni connection to you, would the final vote have gone the same way?",
        "Looking back, was there a moment of real uncertainty you wish you had resolved differently, and why?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Halo effect",
        "decision_point": 1,
        "mechanism": "Positive global impression from the applicant's prestigious feeder school and its alumni track record spills over to inflate confidence in unrelated dimensions (test score adequacy, letter quality).",
        "affected_reasoning_operation": "Evidence weighting during initial file screening",
        "evidence_available_at_time": [
          "School reputation and alumni placement history",
          "Below-threshold standardized test score",
          "Recommendation letter"
        ],
        "required_textual_manifestation": "Officer explicitly cites the school's reputation as the reason for overlooking or downweighting the below-threshold test score, without evaluating the letter's actual content.",
        "plausible_nonbias_interpretation": "Officer reasonably uses school-quality context as one holistic factor among several, consistent with standard holistic review practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["halo effect", "bias", "reputation spillover"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Fundamental Attribution Bias",
        "decision_point": 2,
        "mechanism": "Officer attributes the applicant's lateness and early hesitation to internal disposition (poor time-management, weak composure) while underweighting the known situational cause (transit strike).",
        "affected_reasoning_operation": "Causal attribution of observed interview behavior",
        "evidence_available_at_time": [
          "Known citywide transit strike that day",
          "Applicant's 12-minute lateness and early hesitation",
          "Improvement in the applicant's answers later in the interview"
        ],
        "required_textual_manifestation": "Officer records the lateness/hesitation on the rubric as a personal trait concern rather than noting the transit disruption as a likely cause, despite being aware of the strike.",
        "plausible_nonbias_interpretation": "Interview composure is a legitimately assessed competency, and some hesitation may reflect genuine communication skill gaps independent of the strike.",
        "strength": "moderate",
        "do_not_make_explicit": ["attribution", "situational versus dispositional", "bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Ambiguity Aversion",
        "decision_point": 3,
        "mechanism": "Faced with an acknowledged-incomplete conversion guidance for the reformed grading scale, officer avoids the uncertain, effort-intensive resolution path (expedited evaluation) and defaults to a familiar but admittedly conservative standard, even though the file will be undervalued.",
        "affected_reasoning_operation": "Information-source selection under acknowledged uncertainty",
        "evidence_available_at_time": [
          "Reformed 20-point grading scale from applicant's country",
          "International credentials office guidance flagged as provisional/incomplete",
          "Availability of an expedited formal credential evaluation option"
        ],
        "required_textual_manifestation": "Officer states awareness that the standard conversion table is likely imprecise for this reformed scale, but chooses it anyway specifically to avoid the uncertain, slower evaluation process.",
        "plausible_nonbias_interpretation": "Deadline pressure could justify using the fastest available method regardless of any discomfort with ambiguity.",
        "strength": "subtle",
        "do_not_make_explicit": ["ambiguity aversion", "uncertainty avoidance", "bias"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Belief Perserverence and Attitude Polarisation",
        "decision_point": 3,
        "mechanism": "New disconfirming evidence (the disciplinary note) is reinterpreted to fit and even reinforce the officer's original favorable impression from phase 1, rather than prompting genuine reassessment.",
        "affected_reasoning_operation": "Belief updating in response to disconfirming evidence",
        "evidence_available_at_time": [
          "Original favorable impression formed at file screening",
          "Second reference's disclosure of a minor, resolved disciplinary note",
          "Absence of any new information supporting the original impression"
        ],
        "required_textual_manifestation": "Officer explicitly frames the disciplinary note as further proof the applicant is fundamentally strong (e.g., 'shows resilience'), rather than treating it as genuinely new evidence to weigh, and the original assessment ends up more confident than before.",
        "plausible_nonbias_interpretation": "A resolved, minor disciplinary matter may legitimately carry little evidentiary weight in a holistic review.",
        "strength": "moderate",
        "do_not_make_explicit": ["belief perseverance", "polarization", "disconfirming evidence", "bias"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Ingroup Favoritism or In-group bias",
        "decision_point": 4,
        "mechanism": "Shared alumni/regional network membership between the officer and one finalist leads to extending discretionary benefit-of-the-doubt weighting not applied equally to the non-affiliated finalist with comparable metrics.",
        "affected_reasoning_operation": "Comparative evaluation and discretionary weighting between two similarly qualified finalists",
        "evidence_available_at_time": [
          "Legacy/regional alumni connection of one finalist matching the officer's own network",
          "Comparable borderline metrics for both finalists",
          "No documented merit differential between the two"
        ],
        "required_textual_manifestation": "Officer explains the final vote by referencing shared network ties or familiarity with that finalist's community, applying looser standards to that candidate than to the unaffiliated one.",
        "plausible_nonbias_interpretation": "Officer may believe the network connection provides genuinely useful, verifiable context about the finalist's fit and character.",
        "strength": "subtle",
        "do_not_make_explicit": ["ingroup", "in-group bias", "favoritism", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition, no control pairing supplied."
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
      "Confirm exactly 4 decision points exist, each with at least two plausible alternatives.",
      "Confirm each of the 5 requested biases has exactly 1 planned instance with a unique instance_id.",
      "Confirm decision point 3 hosts two distinct instances (cb_03, cb_04) with separate evidence sources: reformed grading scale versus disciplinary note.",
      "Confirm no bias-name or psychological-mechanism vocabulary appears in the public interview text.",
      "Confirm each instance includes a plausible non-bias interpretation retained only in internal metadata.",
      "Confirm consequences described (letter quality, strike confirmation, undervalued conversion, admit-rate flag) do not themselves conclusively prove bias.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and five embedded instances without repetitive exposition."
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
