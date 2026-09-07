You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IA_Biased_5",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Counterterrorism Analyst (Team Lead, Fusion Center)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The 72-Hour Marathon Threat Stream",
    "scenario_summary_internal": "A regional fusion center's counterterrorism team lead receives an uncorroborated walk-in tip warning of a possible attack tied to a major public marathon occurring in 72 hours. Under staffing pressure from a concurrent gang-violence surge and a hard event deadline, the team lead triages the tip, consults a senior JTTF liaison, runs a rushed team meeting to characterize the threat and request resources, and finally drafts the pre-event threat bulletin. The interview reconstructs this chronology and probes the analyst's reasoning at each juncture without ever naming or explaining the biases embedded in the narrative.",
    "occupational_realism": {
      "objective": "Determine whether an uncorroborated tip about a possible attack on a public marathon within 72 hours warrants escalation, resource reallocation, and a formal threat bulletin, while managing a competing open investigation and limited staff.",
      "setting": "Regional multi-agency fusion center supporting a metropolitan police department, FBI Joint Terrorism Task Force (JTTF) liaison office, and city event-security coordination, three days before a large public marathon.",
      "constraints": [
        "72-hour window before the marathon with no ability to postpone the event",
        "Analyst team is short-staffed because most personnel are pulled into an ongoing gang-violence surge investigation",
        "Only one new, previously unused walk-in source with no track record",
        "Partial and ambiguous SIGINT corroboration that does not cleanly match the tip's specifics",
        "Political pressure from city officials wanting either reassurance or decisive action, not ambiguity",
        "Hard deadline for issuing a pre-event situational awareness bulletin"
      ],
      "stakeholders": [
        "Fusion Center Director",
        "Senior JTTF Liaison",
        "Junior Intelligence Analyst (dissenting voice)",
        "City Police Counterterrorism Unit Commander",
        "Marathon event organizers and city officials",
        "Patrol and event-security field commanders"
      ],
      "technical_terms_to_use": [
        "walk-in source",
        "HUMINT",
        "SIGINT",
        "corroboration",
        "threat stream",
        "indicators and warnings (I&W)",
        "threat matrix",
        "JTTF",
        "situational awareness bulletin",
        "confidence level",
        "actionable intelligence",
        "tearline",
        "source reliability rating"
      ],
      "technical_terms_to_avoid": [
        "bias",
        "heuristic",
        "anchoring",
        "framing",
        "groupthink",
        "overconfidence",
        "authority bias",
        "cognitive",
        "psychology",
        "confirmation"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "New walk-in source with no prior reporting history claims a device is 'hidden near the finish-line corridor' of the marathon route",
          "Source reliability rating is unassigned pending vetting",
          "No SIGINT or other corroboration yet reviewed"
        ],
        "new_information_after_decision": [
          "A later SIGINT partial hit surfaces in a different sector of the route, roughly two miles from the named finish-line corridor",
          "The SIGINT hit is logged but not re-tasked as a primary collection priority"
        ],
        "alternatives": [
          "Treat the tip as low-confidence pending corroboration and direct broad collection across the entire event footprint",
          "Lock collection scope immediately to the specific corridor named by the source"
        ],
        "intended_action": "Analyst directs all follow-up SIGINT and HUMINT tasking to the named finish-line corridor based on the source's specific wording, and downweights the later hit in a different sector as likely unrelated."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Senior JTTF liaison, with 20 years of counterterrorism experience, reviews the tip and states it 'resembles the pattern' of a plot thwarted two years earlier",
          "Liaison recommends elevating the internal threat level based on this resemblance",
          "No independent comparison of tactic, target type, or actor profile has been completed by the analyst's own team"
        ],
        "new_information_after_decision": [
          "A subsequent case-file review shows the earlier thwarted plot involved a different tactic (vehicle-borne device vs. this tip's claimed placed device) and a different target type",
          "The resemblance is later assessed as superficial rather than substantive"
        ],
        "alternatives": [
          "Independently re-verify the source's reliability and the substance of the pattern match before recommending escalation to the Director",
          "Elevate the threat level on the liaison's recommendation without independent re-verification, given his seniority and track record"
        ],
        "intended_action": "Analyst recommends elevating the threat level to the Fusion Center Director primarily on the strength of the liaison's seniority and stated resemblance, without independently re-checking the pattern match."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Team meets under time pressure to decide how to characterize the threat and what resources to request",
          "A junior analyst raises the corroboration gap (mismatched location, superficial pattern match) and requests 24 more hours before escalating",
          "Team lead must phrase the resource request to the Director and city officials"
        ],
        "new_information_after_decision": [
          "The Director approves a large surge in patrol and screening resources based on the phrasing used",
          "A retrospective review later notes that an equivalent request phrased around the probability of a safe event, rather than the probability of an attack, might have received a smaller or delayed resource allocation"
        ],
        "alternatives": [
          "Formally log the junior analyst's dissent and request the additional 24 hours for corroboration before finalizing a resource ask",
          "Reach quick unanimous agreement to escalate immediately, closing discussion once the majority view emerges",
          "Present the resource request framed around the probability of an attack occurring",
          "Present the same underlying evidence framed around the probability of the event proceeding safely"
        ],
        "intended_action": "The team quickly converges on immediate escalation without formally recording the dissent, and the team lead frames the request to leadership in terms of attack probability, which noticeably increases the resources approved."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Deadline for the pre-event situational awareness bulletin has arrived",
          "Unresolved contradictions remain: location mismatch, superficial pattern match, unlogged dissent",
          "No new corroborating source has emerged in the final hours"
        ],
        "new_information_after_decision": [
          "The marathon proceeds without any incident at the named corridor or elsewhere on the route",
          "It remains unresolved whether the protective posture deterred an actual plot or whether no credible plot existed at all"
        ],
        "alternatives": [
          "Issue the bulletin with calibrated, moderate-confidence language that explicitly flags the unresolved corroboration gaps",
          "Issue the bulletin with high-confidence language stating an attack at the named corridor is highly likely, to maximize protective posture"
        ],
        "intended_action": "Analyst issues a high-confidence bulletin naming the specific corridor as the likely target, despite the unresolved gaps, stating strong personal confidence in the assessment during the pre-event briefing."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this tip first came to your attention.",
        "What was your initial read on the situation, before you did anything else?"
      ],
      "timeline_reconstruction": [
        "What happened right after you received the walk-in report?",
        "What did the liaison call add to your understanding, and when did it happen relative to the team meeting?",
        "What was decided in the team meeting, and how did that lead to the final bulletin?"
      ],
      "decision_point_probes": [
        "What specific cues in the source's statement drove where you focused collection? (Phase 1)",
        "What other information sources did you consider consulting before locking the collection scope? (Phase 1)",
        "What was your goal in accepting or questioning the liaison's pattern comparison? (Phase 2)",
        "What alternatives did you weigh before recommending escalation to the Director? (Phase 2)",
        "What was the basis for closing discussion so quickly in the team meeting? (Phase 3)",
        "How did you decide how to phrase the resource request to leadership? (Phase 3)",
        "How much time pressure did you feel finalizing the bulletin, and how did that affect the confidence language you chose? (Phase 4)",
        "What uncertainty remained at the time you issued the bulletin, and how did you communicate it? (Phase 4)"
      ],
      "closing_hypotheticals": [
        "If the walk-in source's statement had been vaguer about location, how do you think your collection tasking would have differed?",
        "If a less senior person had made the pattern comparison, would your recommendation have changed?",
        "If the junior analyst's dissent had been formally logged and circulated, do you think the outcome of the meeting would have changed?",
        "Looking back, would you phrase the resource request the same way if you had to do it again?",
        "What would have made you issue a lower-confidence bulletin?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Analyst's downstream collection scope and interpretation remain fixed on the source's initial specific claim (the named corridor), causing later, non-confirming SIGINT information from a different sector to be discounted rather than triggering a scope re-evaluation.",
        "affected_reasoning_operation": "Evidence weighting and collection prioritization following initial exposure to a specific numeric/locational claim",
        "evidence_available_at_time": [
          "Uncorroborated walk-in claim naming a specific corridor",
          "No source reliability rating yet assigned",
          "Later partial SIGINT hit in a different route sector, received after scope was already locked"
        ],
        "required_textual_manifestation": "Analyst explicitly explains locking tasking to the named corridor because of the source's specific wording, and explains downweighting the later SIGINT hit as 'probably unrelated' without giving an independent evidentiary reason for the dismissal.",
        "plausible_nonbias_interpretation": "Focusing scarce collection resources on the most specific, actionable detail available is a defensible triage heuristic under time pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "first number", "initial estimate"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Authority Bias or Authority Obedience",
        "decision_point": 2,
        "mechanism": "Analyst adopts and forwards the senior liaison's pattern-match conclusion and escalation recommendation primarily because of the liaison's seniority and reputation, rather than because of independently verified evidentiary similarity.",
        "affected_reasoning_operation": "Acceptance and forwarding of a threat assessment without independent verification of its evidentiary basis",
        "evidence_available_at_time": [
          "Liaison's verbal assertion of pattern resemblance to a past thwarted plot",
          "No independent case-file comparison completed at the time of the recommendation",
          "Liaison's stated seniority and prior track record"
        ],
        "required_textual_manifestation": "Analyst states that the recommendation was adopted because the liaison 'has seen this before' and has 20 years of experience, without describing any independent check of the tactic or target-type match before escalating.",
        "plausible_nonbias_interpretation": "Deferring to a demonstrably experienced colleague under time pressure is a reasonable use of expertise and division of labor.",
        "strength": "subtle",
        "do_not_make_explicit": ["authority", "deference", "seniority bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "The team reaches rapid unanimous agreement to escalate immediately, and the dissenting junior analyst's corroboration concerns are not formally logged, discussed, or resolved before the group moves to consensus.",
        "affected_reasoning_operation": "Group decision convergence and handling of dissenting input under time pressure",
        "evidence_available_at_time": [
          "Junior analyst's stated concern about location mismatch and superficial pattern match",
          "Explicit request for 24 more hours of corroboration",
          "Time pressure from the approaching bulletin deadline"
        ],
        "required_textual_manifestation": "Analyst describes the meeting moving quickly to agreement once 'most people were on the same page,' and confirms the junior analyst's dissent was not written into the record or revisited before the group finalized its position.",
        "plausible_nonbias_interpretation": "Reaching quick alignment under a hard deadline is a practical necessity when the team must act before the event begins.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "consensus pressure", "suppressed dissent"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Framing effects",
        "decision_point": 3,
        "mechanism": "The identical underlying evidence produces a larger resource request when the team lead phrases it in terms of probability of an attack occurring rather than probability of the event proceeding safely, and the analyst chooses the attack-probability phrasing without treating the choice of framing as consequential.",
        "affected_reasoning_operation": "Communication and packaging of a probability estimate to decision-makers, distinct from the group-consensus process itself",
        "evidence_available_at_time": [
          "Same underlying threat-matrix data available under either phrasing",
          "Director's known preference for clear, decisive language",
          "Awareness that phrasing affects how much resource leadership tends to approve"
        ],
        "required_textual_manifestation": "Analyst recalls choosing to present the request as '10% chance of an incident' rather than '90% chance the event proceeds safely' and notes, in hindsight, that the size of the approved resource surge might have differed under the alternate phrasing, without treating this as evidentiarily meaningful.",
        "plausible_nonbias_interpretation": "Choosing vivid, decision-actionable language for leadership is a normal communication practice in briefings.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "loss framing", "gain framing"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Analyst issues a high-confidence bulletin and expresses strong personal certainty about the specific corridor being the target, despite openly acknowledged unresolved contradictions in the evidence base at the time of drafting.",
        "affected_reasoning_operation": "Calibration of stated confidence level relative to the actual strength and completeness of supporting evidence",
        "evidence_available_at_time": [
          "Unresolved location mismatch between the tip and the SIGINT hit",
          "Superficial, unverified pattern match from Phase 2",
          "Unlogged dissent from Phase 3",
          "No new corroboration in the final hours before the deadline"
        ],
        "required_textual_manifestation": "Analyst describes drafting the bulletin with high-confidence language naming the specific corridor and recalls feeling 'very sure' of the assessment during the briefing, despite acknowledging, when asked, that the underlying contradictions were never resolved.",
        "plausible_nonbias_interpretation": "Under a hard deadline with no time for further corroboration, decisive language can be operationally necessary to drive protective action.",
        "strength": "subtle",
        "do_not_make_explicit": ["overconfidence", "miscalibration", "confidence bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control variant."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable",
      "original_state": "Not applicable",
      "counterfactual_state": "Not applicable",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable",
      "causal_test_question": "Not applicable"
    },
    "generation_checks": [
      "Interview must contain exactly four decision points corresponding to Phases 1-4.",
      "No bias name, definition, or psychological term may appear in the public interview text.",
      "Each of the five planned instances (cb_01 through cb_05) must be independently identifiable from distinct textual evidence tied to its assigned decision point.",
      "Decision Point 3 must contain two distinct, separately identifiable manifestations (cb_03 Groupthink, cb_04 Framing effects) tied to different reasoning operations (group consensus vs. message framing), not a single blended passage.",
      "Consequences (safe event outcome) must be presented as inconclusive regarding whether any decision was biased.",
      "Total interview length must fall between 1,215 and 1,485 words, with target 1,350 words.",
      "Probes must cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes across the four decision points.",
      "No additional, unrequested instance of any of the five named biases may be introduced in probes, hypotheticals, or the outcome narration."
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
