You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EI_Counterfactual_6",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "School District Curriculum Committee Member",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Adopting the New Middle-School Math Curriculum — Extended Timeline Variant",
    "scenario_summary_internal": "A paired counterfactual to EI_Biased_6. The same committee, same three publisher proposals, same neighboring-district conference account, same vendor stakeholder meeting, same pilot, and same final rubric-scoring event occur, but the district grants a twelve-week adoption window instead of the original six-week deadline. This tests whether the same six cognitive-bias mechanisms still emerge when acute time pressure is substantially reduced, isolating deadline pressure as a contributing but not solely necessary condition for the biased pattern.",
    "occupational_realism": {
      "objective": "Recommend one K-8 math curriculum for board adoption that best addresses recent standardized test score declines, now within a twelve-week review window instead of six.",
      "setting": "Mid-size public school district; curriculum committee of 7 members (teachers, an instructional coach, an assistant principal, a parent representative) meeting weekly, with one 3-week classroom pilot in two schools, under a doubled adoption-cycle timeline.",
      "constraints": [
        "State-mandated adoption calendar now allows twelve weeks instead of six before board submission",
        "Limited district budget covering only one full curriculum purchase plus materials",
        "Only two schools able to run a live classroom pilot due to staffing",
        "Committee members have other full-time teaching or administrative duties, limiting review depth despite the longer window",
        "Vendor presentations and conference sessions still occur on their own external schedule, independent of the district's extended timeline"
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
          "Initial standards-alignment matrices exist for all three but have not been deeply reviewed",
          "The committee now has twelve weeks rather than six before the board submission deadline"
        ],
        "new_information_after_decision": [
          "Two committee members later find gaps in Curriculum B's alignment matrix that were not checked before shortlisting",
          "Publisher A's proposal contained a more detailed differentiation plan that received less scrutiny despite the additional available time"
        ],
        "alternatives": [
          "Shortlist all three curricula equally for full review given the extra weeks available",
          "Prioritize Curriculum B for deeper review based on the neighboring district's reported enthusiasm",
          "Request additional independent alignment data before shortlisting any curriculum"
        ],
        "intended_action": "Even with a longer runway, the committee still narrows early attention toward Curriculum B, treating the neighboring district's positive conference buzz as a leading signal, while giving cursory review to A and C in the opening sessions."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "A vendor stakeholder meeting for Curriculum B included several enthusiastic testimonials from other district committee members",
          "Committee's own pilot data collection has not yet started",
          "One member recalls a vivid, well-told anecdote from the meeting about a struggling classroom turning around with Curriculum B",
          "Statistical pilot data from a comparable district exists but was only briefly mentioned in the meeting",
          "The committee has roughly nine remaining weeks before the deadline at this point, considerably more slack than in the original timeline"
        ],
        "new_information_after_decision": [
          "The vivid anecdote later turns out to be from a single classroom, not representative of district-wide results",
          "The comparable-district statistical report, when later retrieved, shows mixed results across schools"
        ],
        "alternatives": [
          "Weight the vivid classroom anecdote heavily as the deciding evidence for Curriculum B's promise",
          "Request the full statistical pilot report from the comparable district promptly, since the extended timeline allows time to do so",
          "Table further weighting until the district's own pilot data is available"
        ],
        "intended_action": "Despite having ample calendar time to retrieve and review the statistical report immediately, committee members most affected by the memorable anecdote recall it more easily and let it disproportionately shape their sense of Curriculum B's likely success, delaying the report's retrieval anyway."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "One pilot teacher reports mixed results with Curriculum B mid-pilot, citing pacing problems in one unit",
          "The majority of committee members have already expressed favorable views of Curriculum B in prior meetings",
          "Several weeks of runway still remain before the board deadline, so schedule pressure alone cannot fully explain rushing",
          "No committee member has yet independently reviewed data contradicting Curriculum B's fit"
        ],
        "new_information_after_decision": [
          "The dissenting pilot teacher's pacing concern is later validated by a second classroom during full implementation",
          "A member who had gone along with the majority privately admits afterward they had unspoken reservations"
        ],
        "alternatives": [
          "Pause to formally investigate the pacing concern with additional classroom observation, which the extended timeline comfortably allows",
          "Move quickly toward consensus on Curriculum B anyway, citing a preference to finish early",
          "Assign one member to independently verify the concern before the committee's next vote"
        ],
        "intended_action": "Even though the twelve-week window leaves enough slack to investigate further, the committee still suppresses full airing of the dissenting pacing concern and moves toward apparent unanimous agreement without dedicated discussion of the doubt, favoring early closure over the available time to verify."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Each committee member has submitted individual rubric scores for Curricula A, B, and C across five criteria",
          "Scores show a wide spread on the 'differentiation support' criterion for Curriculum A, with two very high scores and two very low scores",
          "Scores for Curriculum B cluster more tightly across all criteria",
          "The chair still needs one final composite score per curriculum for the board memo, though the submission date is now weeks away rather than days"
        ],
        "new_information_after_decision": [
          "A closer look after submission shows the two low scorers for Curriculum A had not reviewed the differentiation appendix, while the two high scorers had",
          "The board later asks why the widely disputed criterion was treated as a single averaged figure"
        ],
        "alternatives": [
          "Average all rubric scores directly into one composite figure per curriculum for the board memo",
          "Flag criteria with wide score spread for separate discussion before finalizing composites, which the extended timeline would easily accommodate",
          "Investigate why scorers diverged before combining any numbers"
        ],
        "intended_action": "Despite having no acute scheduling emergency at this stage, the chair still combines all individual scores into a single averaged composite per curriculum, including the widely split differentiation-support scores for Curriculum A, without flagging or investigating the disagreement, and treats the resulting mean as a settled figure."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this curriculum review process started and what triggered it?",
        "What was your role on the committee, and what was the committee trying to accomplish this cycle?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through the vendor stakeholder meeting — what stood out to you from it?",
        "What happened when the pilot teacher raised concerns mid-pilot?",
        "How did the committee arrive at final scores for the board memo?"
      ],
      "decision_point_probes": [
        "At the point where the committee narrowed focus to Curriculum B, what alternatives did you consider, and why did B rise to the top, especially with more weeks available than usual?",
        "When weighing the vendor meeting information, what made the classroom anecdote stand out compared to the statistical report, given you had time to chase either down?",
        "When the pilot teacher's pacing concern came up, what discussion happened around it, and how was the decision to move forward made?",
        "When combining the rubric scores into one composite, was the spread in scores discussed? Why or why not?"
      ],
      "decision_basis": [
        "What evidence ultimately mattered most in each of these moments?",
        "Looking back, was there information you had time to use but didn't?"
      ],
      "prior_experience": [
        "Had you been through a curriculum adoption cycle like this before? How did that shape your expectations this time, especially with the longer runway?"
      ],
      "time_pressure": [
        "With twelve weeks instead of six, how much did scheduling actually factor into how quickly the committee moved through discussions?"
      ],
      "uncertainty": [
        "At any point, did you feel unsure whether the committee had the full picture? What did you do about that, given the extra time available?"
      ],
      "closing_hypotheticals": [
        "If the pilot teacher's pacing concern had come up earlier in the process, do you think it would have changed the outcome?",
        "If the neighboring district hadn't mentioned Curriculum B at the conference, do you think the shortlist would have looked different?",
        "If you had to redo the scoring step, would you handle the split differently, even with no imminent deadline?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cfbw_01",
        "bias": "Bandwagon effect",
        "decision_point": 1,
        "mechanism": "Committee elevates Curriculum B for deeper review primarily because of a neighboring district's reported enthusiasm and conference buzz, rather than independent evidence review of all three curricula, even though the twelve-week window removed any urgency to shortcut this step.",
        "affected_reasoning_operation": "Initial evidence-selection / shortlisting judgment",
        "evidence_available_at_time": [
          "Three unreviewed standards-alignment matrices of comparable completeness",
          "Neighboring district's verbal enthusiasm reported secondhand at a conference",
          "A twelve-week runway that removed the original schedule-based justification for uneven review"
        ],
        "required_textual_manifestation": "Interviewee explains that the committee gave Curriculum B priority attention specifically because another district's positive reception made it feel like the frontrunner, and notes that this happened even though there was no scheduling reason to skip a balanced first look at A and C.",
        "plausible_nonbias_interpretation": "A neighboring district's real-world adoption could be treated as a legitimate practical signal warranting closer look regardless of how much time is available.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon", "popularity", "social proof", "peer pressure"]
      },
      {
        "instance_id": "cfan_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "The initial framing of Curriculum B as the likely frontrunner persists as a reference point that subsequent review of Publisher A's differentiation plan is implicitly measured against, rather than each option being evaluated independently, despite ample remaining calendar time to reset that framing.",
        "affected_reasoning_operation": "Comparative evaluation of subsequent evidence relative to an initial reference point",
        "evidence_available_at_time": [
          "Curriculum B established early as the committee's presumptive leading option",
          "Curriculum A's differentiation plan, reviewed weeks later, described as more detailed but assessed relative to whether it could 'beat' B rather than on its own terms"
        ],
        "required_textual_manifestation": "Interviewee describes evaluating Curriculum A's differentiation plan, even much later in the extended timeline, in terms of whether it was strong enough to change the committee's mind away from B, rather than assessing it independently from the outset.",
        "plausible_nonbias_interpretation": "Comparative evaluation against an established frontrunner can be a legitimate, efficient review strategy independent of how much time is available.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "reference point", "initial estimate"]
      },
      {
        "instance_id": "cfav_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "A vivid, memorable classroom anecdote from the vendor meeting is recalled and weighted more heavily than a less memorable statistical pilot report mentioned in the same meeting, despite the committee having plenty of remaining weeks to retrieve and study the report promptly.",
        "affected_reasoning_operation": "Recall and weighting of evidence when forming confidence in Curriculum B's likely success",
        "evidence_available_at_time": [
          "One vivid, well-told anecdote about a single classroom's turnaround",
          "A brief mention of a statistical pilot report from a comparable district covering multiple schools",
          "Roughly nine weeks of remaining runway that made prompt retrieval of the report logistically easy"
        ],
        "required_textual_manifestation": "Interviewee recalls the anecdote in specific, vivid detail while treating the statistical report as an afterthought that could have been retrieved right away but wasn't, and connects the anecdote to growing confidence in Curriculum B.",
        "plausible_nonbias_interpretation": "A concrete classroom story could be reasonably viewed as more diagnostic of real classroom fit than an aggregate statistic lacking context, regardless of available time.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability", "memorable", "vividness", "recall bias"]
      },
      {
        "instance_id": "cfcf_01",
        "bias": "Confirmation bias",
        "decision_point": 2,
        "mechanism": "After forming early favorable impressions of Curriculum B, committee members readily accept the vendor meeting's positive testimonials while deprioritizing retrieval of the comparable-district statistical report that could complicate the favorable view, even though the extended timeline removed any practical barrier to pursuing it sooner.",
        "affected_reasoning_operation": "Selective evidence-seeking and evidence-acceptance following an existing preference",
        "evidence_available_at_time": [
          "Multiple enthusiastic testimonials for Curriculum B at the stakeholder meeting",
          "An available but unretrieved comparable-district statistical report that later showed mixed results",
          "Ample scheduled weeks that made timely follow-up entirely feasible"
        ],
        "required_textual_manifestation": "Interviewee explains that the testimonials felt reassuring and consistent with what the committee already expected, so pursuing the fuller statistical report felt like a low priority even though there was no scheduling reason to delay it.",
        "plausible_nonbias_interpretation": "Prioritizing readily available qualitative input, with intent to review data later, can reflect ordinary task sequencing rather than selective evidence-seeking.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "seeking supporting evidence", "selective attention"]
      },
      {
        "instance_id": "cfgt_01",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "With a strong emerging majority preference for Curriculum B, the committee moves toward apparent consensus without substantively investigating a dissenting teacher's pacing concern, and a member later admits privately withheld reservations, even though several weeks of slack remained before the deadline and made deeper investigation logistically easy.",
        "affected_reasoning_operation": "Group deliberation / dissent evaluation before consensus decision",
        "evidence_available_at_time": [
          "One pilot teacher's mid-pilot report of pacing problems",
          "Majority of committee members' previously stated favorable views of Curriculum B",
          "Several remaining weeks before the board deadline, removing the original schedule-based justification for rushing"
        ],
        "required_textual_manifestation": "Interviewee describes the committee moving to agreement quickly after the pacing concern was raised, without a dedicated discussion, and notes that time was not actually the binding constraint at that point, while at least one member did not voice full reservations at the time.",
        "plausible_nonbias_interpretation": "The committee may have reasonably judged the pacing issue as a minor, fixable implementation detail not warranting further investigation, independent of how much time was left.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "consensus pressure", "conformity", "self-censorship"]
      },
      {
        "instance_id": "cfavg_01",
        "bias": "Averaging Bias",
        "decision_point": 4,
        "mechanism": "The chair combines widely divergent individual rubric scores for Curriculum A's differentiation-support criterion into a single averaged composite without flagging or investigating the disagreement, treating the average as a settled, adequate figure despite there being no imminent scheduling emergency requiring immediate compression of the scores.",
        "affected_reasoning_operation": "Aggregation of conflicting quantitative judgments into a summary decision metric",
        "evidence_available_at_time": [
          "Two very high and two very low individual scores for Curriculum A on 'differentiation support'",
          "Tightly clustered scores for Curriculum B across all criteria",
          "Several weeks of remaining time before the board memo was actually due"
        ],
        "required_textual_manifestation": "Interviewee describes the final composite scores being calculated as straightforward averages of individual rubric entries, including the split scores for Curriculum A, and notes that the resulting mean read as a settled figure that closed off further inspection, despite there being time available to investigate the disagreement first.",
        "plausible_nonbias_interpretation": "Averaging individual rubric scores is a standard, procedurally simple aggregation method that committees may default to regardless of how much time is available.",
        "strength": "subtle",
        "do_not_make_explicit": ["averaging bias", "aggregation error", "masking disagreement"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "EI_Biased_6",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is counterfactual, not a zero-bias control variant."
    },
    "counterfactual_specification": {
      "causal_variable": "Length of the committee's adoption-cycle deadline",
      "original_state": "Six-week hard deadline from the superintendent's office to produce a board recommendation, creating acute schedule pressure throughout the process",
      "counterfactual_state": "Twelve-week deadline (doubled review window), substantially reducing acute schedule pressure at each decision point while leaving all other facts, actors, evidence, and events unchanged",
      "variables_to_hold_constant": [
        "The three publisher proposals (Curriculum A, B, and C) and their content",
        "The neighboring district's conference testimony about Curriculum B",
        "The vendor stakeholder meeting, its anecdote, and its brief mention of the statistical report",
        "The three-week, two-school classroom pilot structure",
        "The pilot teacher's mid-pilot pacing concern and its later recurrence",
        "The final rubric-scoring process and the two-high/two-low split on Curriculum A's differentiation criterion",
        "Committee composition, roles, and the board's eventual questions",
        "The overall six-decision-point... i.e., four-decision-point narrative structure and sequence of events"
      ],
      "expected_causal_difference": "If schedule pressure were the sole necessary driver of the biased pattern, doubling the timeline should visibly reduce or eliminate the rushed, under-investigated reasoning at each decision point. Instead, the same six bias mechanisms are expected to persist even with ample slack, indicating that social, evidentiary, and procedural dynamics — not acute time pressure alone — sustain the pattern.",
      "causal_test_question": "Does substantially lengthening the adoption-cycle deadline change whether the committee investigates dissenting evidence, retrieves disconfirming data promptly, and disaggregates divided scores, or do these patterns persist regardless of the extra available time?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and numbered 1-4, mirroring EI_Biased_6's structure.",
      "Confirm exactly one instance planned per bias: Bandwagon effect, Groupthink, Availability Bias, Anchoring Bias, Confirmation bias, Averaging Bias (6 total instances).",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text.",
      "Confirm only the deadline-length causal variable differs from EI_Biased_6; all other material facts, actors, and event sequence remain constant.",
      "Confirm each decision point contains an explicit or implicit acknowledgment that reduced time pressure did not prevent the same reasoning pattern, without naming the causal variable as an explanation for bias.",
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
