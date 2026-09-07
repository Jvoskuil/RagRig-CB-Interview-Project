You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Biased_3",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Homicide Detective",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Riverside Apartment Homicide - Third Shift Handoff",
    "scenario_summary_internal": "A homicide detective is interviewed about a case in which a young woman was found dead in her apartment. Early in the investigation the detective and partner formed a working theory pointing to the victim's ex-boyfriend. A team briefing solidified that theory. Midway through, a neighbor's late-arriving statement about a stranger seen near the building complicated the timeline, and the detective had to decide how to weigh it against team consensus and their own prior commitment to the ex-boyfriend theory. The interview traces four decision points from initial scene assessment through case referral to the DA, probing how evidence was gathered, weighted, and reconciled under time pressure and team dynamics.",
    "occupational_realism": {
      "objective": "Identify and build a prosecutable case against the individual responsible for the victim's death within the critical 72-hour investigative window.",
      "setting": "Mid-size city homicide unit; apartment crime scene, precinct briefing room, and follow-up canvass over a 5-day period",
      "constraints": [
        "72-hour window before witness memory degrades and suspect can flee jurisdiction",
        "limited forensic lab turnaround (48-72 hours for DNA/toxicology)",
        "pressure from lieutenant and DA liaison for a chargeable theory",
        "partner detective present at most decisions, creating shared accountability",
        "media attention increasing pressure for a quick resolution"
      ],
      "stakeholders": [
        "lead detective (interviewee)",
        "partner detective",
        "homicide unit lieutenant",
        "crime scene technicians",
        "DA liaison",
        "victim's family",
        "ex-boyfriend (initial suspect)",
        "neighbor witness"
      ],
      "technical_terms_to_use": [
        "scene canvass",
        "chain of custody",
        "working theory",
        "case referral",
        "timeline reconstruction",
        "corroborating statement",
        "probable cause"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "cognitive dissonance",
        "groupthink",
        "recency effect",
        "anchoring",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "victim found deceased in locked apartment, no forced entry",
          "recent breakup with ex-boyfriend documented in texts",
          "ex-boyfriend has a prior domestic disturbance call at victim's address",
          "no immediate signs of struggle beyond bedroom"
        ],
        "new_information_after_decision": [
          "ex-boyfriend's alibi partially corroborated by a coworker but with a two-hour gap",
          "unidentified male seen loitering near the building's rear entrance per a passerby, unconfirmed at this stage"
        ],
        "alternatives": [
          "treat ex-boyfriend as primary working theory and prioritize resources on his alibi and history",
          "hold off naming a primary theory until scene forensics and full canvass are complete",
          "pursue the rear-entrance sighting as an equally weighted lead"
        ],
        "intended_action": "Detective designates the ex-boyfriend as the primary working theory and directs the team to focus canvass and warrant efforts around him."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "unit briefing held; lieutenant and three colleagues present",
          "partner detective voices support for the ex-boyfriend theory citing prior domestic call",
          "one junior detective mentions the rear-entrance sighting is worth pursuing but is not pressed further",
          "forensic swabs sent to lab, results pending"
        ],
        "new_information_after_decision": [
          "team consensus recorded in the case log as ex-boyfriend being the primary suspect",
          "the junior detective's rear-entrance lead is deprioritized without a documented follow-up assignment"
        ],
        "alternatives": [
          "assign a team member to independently verify the rear-entrance sighting before finalizing the case direction",
          "adopt the group's converging view and move forward with a warrant request for the ex-boyfriend",
          "table the decision until lab results return"
        ],
        "intended_action": "The detective aligns with the team's converging view, formally adopting the ex-boyfriend theory as the unit's direction without assigning independent verification of the dissenting lead."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "lab results return: no DNA match to ex-boyfriend at the scene",
          "ex-boyfriend's coworker alibi gap now closed by a second witness placing him elsewhere",
          "the rear-entrance witness is finally re-interviewed and gives a more detailed description matching an unrelated individual with a prior burglary record in the area"
        ],
        "new_information_after_decision": [
          "detective requests additional forensic review focused on reconciling the negative DNA result with the existing theory rather than broadening the suspect pool",
          "case referral memo to the DA liaison still lists the ex-boyfriend as primary person of interest, with the new witness description noted as a secondary, unresolved lead"
        ],
        "alternatives": [
          "revise the primary theory to prioritize the burglary-record individual given the fresh, detailed statement",
          "maintain the ex-boyfriend as primary suspect and treat the DNA and alibi gap as explainable exceptions",
          "pause the referral and request a fresh case review from an uninvolved detective"
        ],
        "intended_action": "The detective maintains the ex-boyfriend as the primary theory, characterizing the negative DNA and alibi correction as anomalies rather than as reasons to re-center the investigation, and proceeds toward referral."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "final pre-referral case review meeting",
          "the most recently obtained statement (burglary-record individual's description) is the most vivid and detailed piece of evidence in the file",
          "older canvass statements and the initial scene assessment are comparatively thin on physical detail",
          "DA liaison requests the detective's best-supported theory for filing"
        ],
        "new_information_after_decision": [
          "case is referred to the DA with the most recent witness statement weighted heavily in the summary, overshadowing earlier, less detailed but equally relevant scene evidence",
          "DA liaison requests supplemental investigation before filing charges on either individual"
        ],
        "alternatives": [
          "weight all evidence according to its evidentiary strength and chain of custody rather than recency",
          "give disproportionate emphasis to the most recently gathered statement when drafting the referral summary",
          "request a formal weighted timeline review before submitting"
        ],
        "intended_action": "The detective drafts the referral summary giving the most recently obtained witness statement disproportionate prominence relative to earlier evidence of comparable or greater relevance."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how you were first briefed on this case.",
        "What was your initial read on the scene when you arrived?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from scene arrival to case referral.",
        "What information came in at each stage, and when?"
      ],
      "decision_point_probes": [
        "What cues led you to focus on the ex-boyfriend early on?",
        "What sources of information did you rely on most at the briefing, and why?",
        "What alternatives did you or the team consider before settling on a direction?",
        "What was the basis for maintaining the theory after the DNA result came back?",
        "Had you seen cases before where an early theory didn't hold up? How did that shape your approach here?",
        "How much time pressure did you feel at each of these points?",
        "How confident were you in the theory at each stage, and what would have changed that confidence?",
        "If the rear-entrance sighting had been detailed from the start, how might your team's direction have changed?"
      ],
      "closing_hypotheticals": [
        "If you were reviewing this case fresh today with all the evidence in front of you at once, would you have weighted anything differently?",
        "What would you tell a junior detective about balancing team consensus against a dissenting lead?",
        "Looking back, was there a moment you'd want to redo?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "decision_point": 3,
        "mechanism": "Detective reinterprets disconfirming evidence (negative DNA match, corrected alibi) as anomalies to preserve consistency with the already-committed ex-boyfriend theory rather than revising the theory",
        "affected_reasoning_operation": "evidence reconciliation and theory revision",
        "evidence_available_at_time": [
          "negative DNA result at scene",
          "alibi gap closed by second witness",
          "newly detailed description of an alternative individual"
        ],
        "required_textual_manifestation": "detective explicitly frames the disconfirming lab and alibi evidence as explainable exceptions while continuing to treat the ex-boyfriend as primary suspect, without engaging substantively with the alternative lead's specifics",
        "plausible_nonbias_interpretation": "detective could argue prior domestic history still gives reasonable cause to keep the ex-boyfriend as a person of interest pending further review",
        "strength": "subtle",
        "do_not_make_explicit": ["cognitive dissonance", "rationalization", "reducing discomfort"]
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "decision_point": 4,
        "mechanism": "The most recently obtained witness statement is given disproportionate weight in the referral summary relative to earlier, comparably or more relevant scene evidence, driven by its recency rather than its evidentiary strength",
        "affected_reasoning_operation": "evidence weighting and summary drafting",
        "evidence_available_at_time": [
          "recent detailed witness description of alternative individual",
          "earlier, thinner canvass statements and initial scene notes",
          "chain-of-custody documentation for all evidence"
        ],
        "required_textual_manifestation": "detective describes drafting the referral summary and explains giving the newest statement prominent placement or emphasis specifically because it was the most recently gathered, with limited justification tied to its actual evidentiary strength",
        "plausible_nonbias_interpretation": "the most recent statement could genuinely be the most detailed and probative evidence, warranting emphasis on its merits alone",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "recency bias", "most recent information"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 2,
        "mechanism": "Detective adopts the converging view expressed at the team briefing and formalizes it as unit direction without independently verifying or assigning follow-up to the dissenting junior detective's alternative lead, prioritizing consensus over critical evaluation",
        "affected_reasoning_operation": "collective decision adoption and dissent evaluation",
        "evidence_available_at_time": [
          "partner detective's vocal support for ex-boyfriend theory",
          "junior detective's brief mention of rear-entrance sighting",
          "lieutenant's presence and implicit expectation of a unified direction"
        ],
        "required_textual_manifestation": "detective recounts the briefing and describes going along with the team's shared view, noting the dissenting lead was mentioned but not assigned for independent follow-up, framed as a natural outcome of the meeting rather than a contested choice",
        "plausible_nonbias_interpretation": "the ex-boyfriend theory may have had the strongest objective support at that time, making team convergence a reasonable reflection of the evidence rather than pressure to conform",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "conformity", "consensus pressure", "dissent suppression"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "not applicable to biased condition"
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "not applicable; condition is biased, not counterfactual",
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 4 decision points appear in the interview",
      "Confirm exactly 1 cognitive dissonance instance embedded only at decision point 3",
      "Confirm exactly 1 recency effects instance embedded only at decision point 4",
      "Confirm exactly 1 groupthink instance embedded only at decision point 2",
      "Confirm no bias labels or psychological terminology appear in the public interview text",
      "Confirm word count falls between 1215 and 1485 words",
      "Confirm each decision point includes at least two plausible alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm consequences described do not mechanically prove bias presence",
      "Confirm decision point 1 contains no intended bias instance and remains a neutral/realistic anchor decision"
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
