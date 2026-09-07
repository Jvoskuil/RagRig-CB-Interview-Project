You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EI_Biased_6",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "School District Curriculum Committee Member",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Adopting the New Middle-School Math Curriculum",
    "scenario_summary_internal": "A veteran curriculum committee member recounts a six-week process to recommend a replacement math curriculum for grades 6-8 after state test scores dipped. The committee must choose among three vetted publishers under a tight adoption-calendar deadline, reconcile a pilot classroom's experience with a larger review process, and finalize a recommendation to the school board. The account traces four decision points: initial shortlist framing, mid-process reweighting after a persuasive stakeholder meeting, resolution of dissenting pilot-teacher feedback, and final consensus scoring before board submission.",
    "occupational_realism": {
      "objective": "Recommend one K-8 math curriculum for board adoption that best addresses recent standardized test score declines within a fixed 6-week review window.",
      "setting": "Mid-size public school district; curriculum committee of 7 members (teachers, an instructional coach, an assistant principal, a parent representative) meeting weekly, with one 3-week classroom pilot in two schools.",
      "constraints": [
        "State-mandated adoption calendar with a hard board-submission deadline",
        "Limited district budget covering only one full curriculum purchase plus materials",
        "Only two schools able to run a live classroom pilot due to staffing",
        "Committee members have other full-time teaching or administrative duties, limiting review depth",
        "Vendor presentations and conference sessions occur on a compressed schedule"
      ],
      "stakeholders": [
        "Committee chair (assistant principal)",
        "Two pilot classroom teachers",
        "District math instructional coach",
        "Parent representative",
        "Three curriculum publisher sales representatives",
        "Superintendent's office (deadline enforcement)",
        "School board (final approval body)"
      ],
      "technical_terms_to_use": [
        "scope and sequence",
        "standards alignment matrix",
        "pilot implementation data",
        "adoption cycle",
        "rubric-based scoring",
        "differentiated instruction support",
        "formative assessment tools",
        "vertical articulation"
      ],
      "technical_terms_to_avoid": [
        "bandwagon effect",
        "groupthink",
        "availability bias",
        "anchoring bias",
        "confirmation bias",
        "averaging bias",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three publishers submitted proposals: Curriculum A, B, and C",
          "State test scores in 6th-grade math dropped 8 points district-wide last spring",
          "A neighboring district adopted Curriculum B the prior year and reported early enthusiasm at a regional conference",
          "Initial standards-alignment matrices exist for all three but have not been deeply reviewed"
        ],
        "new_information_after_decision": [
          "Two committee members later find gaps in Curriculum B's alignment matrix that were not checked before shortlisting",
          "Publisher A's proposal contained a more detailed differentiation plan that received less scrutiny"
        ],
        "alternatives": [
          "Shortlist all three curricula equally for full review",
          "Prioritize Curriculum B for deeper review based on the neighboring district's reported enthusiasm",
          "Request additional independent alignment data before shortlisting any curriculum"
        ],
        "intended_action": "Committee narrows early attention toward Curriculum B, treating the neighboring district's positive conference buzz as a leading signal, while giving cursory review to A and C."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "A recent vendor stakeholder meeting for Curriculum B included several enthusiastic testimonials from other district committee members",
          "Committee's own pilot data collection has not yet started",
          "One member recalls a vivid, well-told anecdote from the meeting about a struggling classroom turning around with Curriculum B",
          "Statistical pilot data from a comparable district exists but was only briefly mentioned in the meeting"
        ],
        "new_information_after_decision": [
          "The vivid anecdote later turns out to be from a single classroom, not representative of district-wide results",
          "The comparable-district statistical report, when later retrieved, shows mixed results across schools"
        ],
        "alternatives": [
          "Weight the vivid classroom anecdote heavily as the deciding evidence for Curriculum B's promise",
          "Request the full statistical pilot report from the comparable district before adjusting confidence",
          "Table further weighting until the district's own pilot data is available"
        ],
        "intended_action": "Committee members most affected by the memorable anecdote recall it more easily than the statistical report and let it disproportionately shape their sense of Curriculum B's likely success."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "One pilot teacher reports mixed results with Curriculum B mid-pilot, citing pacing problems in one unit",
          "The majority of committee members have already expressed favorable views of Curriculum B in prior meetings",
          "Meeting time is limited and the chair wants to move to consensus before the next session",
          "No committee member has yet independently reviewed data contradicting Curriculum B's fit"
        ],
        "new_information_after_decision": [
          "The dissenting pilot teacher's pacing concern is later validated by a second classroom during full implementation",
          "A member who had gone along with the majority privately admits afterward they had unspoken reservations"
        ],
        "alternatives": [
          "Pause to formally investigate the pacing concern with additional classroom observation",
          "Move quickly toward consensus on Curriculum B to preserve meeting time and momentum",
          "Assign one member to independently verify the concern before the committee's next vote"
        ],
        "intended_action": "Facing time pressure and a strong shared preference already forming, the committee suppresses full airing of the dissenting pacing concern and moves toward apparent unanimous agreement without dedicated discussion of the doubt."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Each committee member has submitted individual rubric scores for Curricula A, B, and C across five criteria",
          "Scores show a wide spread on the 'differentiation support' criterion for Curriculum A, with two very high scores and two very low scores",
          "Scores for Curriculum B cluster more tightly across all criteria",
          "The chair needs one final composite score per curriculum for the board memo"
        ],
        "new_information_after_decision": [
          "A closer look after submission shows the two low scorers for Curriculum A had not reviewed the differentiation appendix, while the two high scorers had",
          "The board later asks why the widely disputed criterion was treated as a single averaged figure"
        ],
        "alternatives": [
          "Average all rubric scores directly into one composite figure per curriculum for the board memo",
          "Flag criteria with wide score spread for separate discussion before finalizing composites",
          "Investigate why scorers diverged before combining any numbers"
        ],
        "intended_action": "The chair combines all individual scores into a single averaged composite per curriculum, including the widely split differentiation-support scores for Curriculum A, without flagging or investigating the disagreement."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how the curriculum review process started and what triggered it?",
        "What was your role on the committee, and what was the committee trying to accomplish?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through the vendor stakeholder meeting — what stood out to you from it?",
        "What happened when the pilot teacher raised concerns mid-pilot?",
        "How did the committee arrive at final scores for the board memo?"
      ],
      "decision_point_probes": [
        "At the point where the committee narrowed focus to Curriculum B, what alternatives did you consider, and why did B rise to the top?",
        "When weighing the vendor meeting information, what made the classroom anecdote stand out compared to other data mentioned?",
        "When the pilot teacher's pacing concern came up, what discussion happened around it, and how was the decision to move forward made?",
        "When combining the rubric scores into one composite, was the spread in scores discussed? Why or why not?"
      ],
      "decision_basis": [
        "What evidence ultimately mattered most in each of these moments?",
        "Looking back, was there information you didn't get a chance to fully use?"
      ],
      "prior_experience": [
        "Had you been through a curriculum adoption cycle like this before? How did that shape your expectations this time?"
      ],
      "time_pressure": [
        "How much did the adoption deadline affect how quickly the committee moved through discussions?"
      ],
      "uncertainty": [
        "At any point, did you feel unsure whether the committee had the full picture? What did you do about that?"
      ],
      "closing_hypotheticals": [
        "If the pilot teacher's pacing concern had come up earlier in the process, do you think it would have changed the outcome?",
        "If the neighboring district hadn't mentioned Curriculum B at the conference, do you think the shortlist would have looked different?",
        "If you had to redo the scoring step, would you handle the split scores differently?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "bw_01",
        "bias": "Bandwagon effect",
        "decision_point": 1,
        "mechanism": "Committee elevates Curriculum B for deeper review primarily because of a neighboring district's reported enthusiasm and conference buzz, rather than because of independent evidence review of all three curricula.",
        "affected_reasoning_operation": "Initial evidence-selection / shortlisting judgment",
        "evidence_available_at_time": [
          "Three unreviewed standards-alignment matrices of comparable completeness",
          "Neighboring district's verbal enthusiasm reported secondhand at a conference"
        ],
        "required_textual_manifestation": "Interviewee explains that the committee gave Curriculum B priority attention specifically because another district's positive reception made it feel like the frontrunner, before the committee's own review had substantively differentiated the three options.",
        "plausible_nonbias_interpretation": "A neighboring district's real-world adoption could be treated as a legitimate practical signal warranting closer look, not necessarily an appeal to popularity.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon", "popularity", "social proof", "peer pressure"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "Under time pressure and with a strong emerging majority preference for Curriculum B, the committee moves toward apparent consensus without substantively investigating a dissenting teacher's pacing concern, and a member later admits privately withheld reservations.",
        "affected_reasoning_operation": "Group deliberation / dissent evaluation before consensus decision",
        "evidence_available_at_time": [
          "One pilot teacher's mid-pilot report of pacing problems",
          "Majority of committee members' previously stated favorable views of Curriculum B",
          "Limited remaining meeting time before the next scheduled vote"
        ],
        "required_textual_manifestation": "Interviewee describes the committee moving to agreement quickly after the pacing concern was raised, without a dedicated discussion, and mentions or implies that at least one member did not voice full reservations at the time.",
        "plausible_nonbias_interpretation": "The committee may have reasonably judged the pacing issue as a minor, fixable implementation detail rather than a substantive risk, warranting a quick move to consensus.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "consensus pressure", "conformity", "self-censorship"]
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "A vivid, memorable classroom anecdote from the vendor meeting is recalled and weighted more heavily than a less memorable statistical pilot report mentioned in the same meeting, despite the anecdote representing a single classroom.",
        "affected_reasoning_operation": "Recall and weighting of evidence when forming confidence in Curriculum B's likely success",
        "evidence_available_at_time": [
          "One vivid, well-told anecdote about a single classroom's turnaround",
          "A brief mention of a statistical pilot report from a comparable district covering multiple schools"
        ],
        "required_textual_manifestation": "Interviewee recalls the anecdote in specific, vivid detail while treating the statistical report as an afterthought or something they meant to follow up on later, and connects the anecdote to their growing confidence in Curriculum B.",
        "plausible_nonbias_interpretation": "A concrete classroom story could be reasonably viewed as more diagnostic of real classroom fit than an aggregate statistic that lacks context.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability", "memorable", "vividness", "recall bias"]
      },
      {
        "instance_id": "an_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "The initial framing of Curriculum B as the likely frontrunner (from decision point 1's shortlisting moment) persists as a reference point that subsequent review of Publisher A's differentiation plan and Publisher C's materials is implicitly measured against, rather than each option being evaluated independently.",
        "affected_reasoning_operation": "Comparative evaluation of subsequent evidence relative to an initial reference point",
        "evidence_available_at_time": [
          "Curriculum B established early as the committee's presumptive leading option",
          "Curriculum A's differentiation plan, reviewed afterward, described as more detailed but assessed relative to whether it could 'beat' B rather than on its own terms"
        ],
        "required_textual_manifestation": "Interviewee describes evaluating Curriculum A's differentiation plan in terms of whether it was strong enough to change the committee's mind away from B, rather than assessing it independently on its own merits from the outset.",
        "plausible_nonbias_interpretation": "Comparative evaluation against a frontrunner can be a legitimate, efficient review strategy under time constraints rather than a distorting anchor.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "reference point", "initial estimate"]
      },
      {
        "instance_id": "cf_01",
        "bias": "Confirmation bias",
        "decision_point": 2,
        "mechanism": "After forming early favorable impressions of Curriculum B, committee members seek out or accept the vendor meeting's positive testimonials readily while deferring or delaying retrieval of the comparable-district statistical report that could complicate the favorable view.",
        "affected_reasoning_operation": "Selective evidence-seeking and evidence-acceptance following an existing preference",
        "evidence_available_at_time": [
          "Multiple enthusiastic testimonials for Curriculum B at the stakeholder meeting",
          "An available but unretrieved comparable-district statistical report that later showed mixed results"
        ],
        "required_textual_manifestation": "Interviewee explains that the testimonials felt reassuring and consistent with what the committee already expected, and that pursuing the fuller statistical report felt like a lower priority at the time, only being retrieved later.",
        "plausible_nonbias_interpretation": "Prioritizing readily available qualitative input during a busy meeting, with intent to review data later, can reflect reasonable time management rather than selective evidence-seeking.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "seeking supporting evidence", "selective attention"]
      },
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "decision_point": 4,
        "mechanism": "The chair combines widely divergent individual rubric scores for Curriculum A's differentiation-support criterion into a single averaged composite without flagging or investigating the disagreement, treating the average as representative despite the split reflecting different levels of review rather than genuine convergence.",
        "affected_reasoning_operation": "Aggregation of conflicting quantitative judgments into a summary decision metric",
        "evidence_available_at_time": [
          "Two very high and two very low individual scores for Curriculum A on 'differentiation support'",
          "Tightly clustered scores for Curriculum B across all criteria"
        ],
        "required_textual_manifestation": "Interviewee describes the final composite scores being calculated as straightforward averages of individual rubric entries, including the split scores for Curriculum A, without describing any step to investigate or resolve why scorers disagreed before combining them.",
        "plausible_nonbias_interpretation": "Averaging individual rubric scores is a standard, procedurally simple method for aggregating committee input, and could be a defensible default without implying dismissal of disagreement.",
        "strength": "subtle",
        "do_not_make_explicit": ["averaging bias", "aggregation error", "masking disagreement"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, not a control variant."
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
      "Confirm exactly 4 decision points are present and numbered 1-4.",
      "Confirm exactly one instance planned per bias: Bandwagon effect, Groupthink, Availability Bias, Anchoring Bias, Confirmation bias, Averaging Bias (6 total instances).",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text.",
      "Confirm each instance is tied to a distinct decision point and evidence trace, with no overlapping textual manifestation between bw_01 and an_01 despite both being anchored at decision point 1 (bw_01 concerns initial shortlisting attention; an_01 concerns later comparative evaluation of Curriculum A/C against the already-formed B preference).",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points, opening, timeline reconstruction, and closing hypothetical probes without repetitive exposition.",
       "Confirm consequences described (test score outcomes, board approval) do not conclusively prove or disprove bias presence.",
      "Confirm technical vocabulary list is used naturally and bias-related terms are excluded from the public interview."
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
