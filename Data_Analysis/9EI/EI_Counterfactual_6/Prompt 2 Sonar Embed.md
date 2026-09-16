You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, is it okay if I record this conversation for internal research on curriculum decision-making, with everything used in de-identified form?

Participant: Sure, that's fine.

Interviewer: Can you tell me about your role and what this particular adoption cycle involved?

Participant: I've served on the district curriculum committee for about five years, representing middle school math. Last fall, after sixth-grade state scores dropped eight points district-wide, the superintendent's office asked us to run a full adoption cycle for a new K-8 math curriculum. This time we actually had twelve weeks instead of the usual six, since the state calendar shifted and gave us extra room. Everyone was glad for the breathing space, honestly — most of us still teach or run buildings full-time.

Interviewer: Walk me through how the review actually started.

Participant: Three publishers submitted proposals — Curriculum A, B, and C. Each had a standards-alignment matrix, sample units, vendor support materials, the usual package. With twelve weeks, we had every intention of giving all three a genuinely deep look before narrowing anything down. But right around when the proposals landed, two of our members came back from a regional math conference where a neighboring district presented on their experience adopting Curriculum B. They were enthusiastic — said it fixed their pacing issues. Our people came back energized, and even with all that extra runway, our first working session ended up centered on B. A and C got more of a checklist pass.

Interviewer: Given you had twelve weeks instead of six, was there a reason A and C didn't get the same depth early on?

Participant: That's the part I keep turning over. There wasn't really a scheduling reason. We had time. It's just that once people were talking about what the neighboring district found, B became the thing everyone wanted to dig into first. We told ourselves we'd circle back to A and C properly, and we had the calendar to do it.

Interviewer: Did you?

Participant: Eventually, yes — around scoring, we went back to Curriculum A's proposal, and it actually had a stronger differentiated-instruction plan than B's. But by then, even weeks into a much longer process, the conversation was still framed as "is this good enough to make us reconsider B," instead of just asking how strong A was standing on its own.

Interviewer: Let's move to the vendor meeting. What happened there?

Participant: That was maybe three weeks in, so still plenty of runway left — something like nine weeks to go. Curriculum B's rep brought in committee members from other districts using it. One of them told a really vivid story about a struggling classroom that turned around within a semester. I still remember the details clearly. Somewhere in that same meeting, someone mentioned a statistical pilot report from a comparable district, covering multiple schools over a full year. I barely registered that part.

Interviewer: You had time to go get that report right away. What happened instead?

Participant: I kept meaning to. It sat on my list for weeks. The story was just more vivid — a real teacher, real kids, a real unit. The report was two sentences and some numbers I didn't have in front of me. It wasn't until we were close to final scoring that anyone actually pulled the report up. When we did, it showed mixed results across schools, not the clean win the anecdote suggested. But by then my sense of B's promise was already pretty locked in.

Interviewer: Did the extra time change how you weighed the testimonials versus the report?

Participant: Honestly, not as much as it should have. The testimonials felt like they confirmed what we already believed from the conference, so they didn't feel like they needed more scrutiny. The report felt like something to get to eventually rather than something urgent, even though nothing was stopping us from pulling it the same week.

Interviewer: Let's talk about the pilot. What happened when concerns came up?

Participant: We ran a three-week pilot of Curriculum B in two schools. About halfway through, one of the pilot teachers flagged pacing problems in a unit — said the sequencing didn't match how her students were actually progressing. By that point most of the committee had already spoken favorably about B in earlier meetings. We still had several weeks before the deadline, so there wasn't really an urgent reason to rush past it.

Interviewer: How was the concern handled?

Participant: It got mentioned, acknowledged, and the conversation moved along toward agreement fairly quickly anyway. We didn't send anyone to observe the second pilot classroom, even though we had the calendar space to do that easily. We just nodded and kept going. I found out afterward that one member had reservations that day but didn't voice them, given how the room felt.

Interviewer: Did that pacing issue end up mattering?

Participant: It did. A second classroom hit the same snag during full rollout. So the concern was real. It just didn't get a real hearing when it came up, even with time on our side.

Interviewer: Last decision point — final scoring. How did that go?

Participant: Everyone submitted rubric scores across five criteria for all three curricula. When the chair compiled them, Curriculum A had an odd split on differentiated-instruction support — two very high scores, two very low. B's scores were tighter across the board. The chair still needed one composite number per curriculum for the board memo, even though the memo wasn't due for weeks. The scores just got averaged straight across, split included. Once that single number came back, it read as a settled, middling score for A, and nobody suggested pulling it apart to see what was underneath.

Interviewer: Was the disagreement on Curriculum A discussed before combining the numbers?

Participant: Not really, even with all that time available. It went into the spreadsheet like everything else. It was only afterward, when someone asked why A's differentiation score looked so unremarkable despite that split, that we found out the two low scorers hadn't reviewed the differentiation appendix, while the two high scorers had. The average wasn't really consensus — it was masking a difference in how much people had actually read.

Interviewer: Did the board notice?

Participant: They asked. Why a criterion with that much internal disagreement got reported as one clean number. We didn't have a great answer beyond "that's how we compile scores."

Interviewer: Stepping back — with twelve weeks instead of six, did scheduling actually drive how quickly things moved?

Participant: Less than I expected, if I'm honest. We had room to slow down at almost every point, and mostly didn't use it. The pacing concern is the one that sits with me. Nobody was acting in bad faith. B just already felt like the likely outcome by the time real friction showed up, deadline or no deadline.

Interviewer: If the pacing concern had surfaced earlier, would the outcome have changed?

Participant: Possibly. Before people's minds were as made up, I think it would've gotten a more serious look, regardless of how much calendar time was left.

Interviewer: And if the neighboring district hadn't mentioned Curriculum B at that conference at all?

Participant: I've wondered that. I think A and C would've gotten a more even start from day one. B's materials were genuinely solid, so it might still have won out. But the early spotlight wouldn't have been there from the beginning.

Interviewer: If you had the scoring step to redo, even with no deadline pressure, would you handle the split differently?

Participant: Yes. I'd flag any criterion with a wide spread and ask why before folding it into one number. The spread itself was telling us something. Averaging it away just erased that, and having extra weeks available didn't stop us from doing it anyway.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Counterfactual_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "Elevation of a curriculum based on external district enthusiasm/popularity signal rather than independent evidence review, persisting despite absence of scheduling pressure to justify uneven review" },
      { "bias": "Groupthink", "occurrences": 1, "mechanism_constraint": "Suppression of dissenting pilot-teacher feedback under majority preference, with a member's unvoiced reservation, occurring despite ample remaining time before the deadline" },
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Overweighting a vivid single-classroom anecdote over a less memorable statistical report, despite ample time available to retrieve the report promptly" },
      { "bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "Evaluating subsequent curricula relative to an early-formed frontrunner reference point, persisting despite extended review time" },
      { "bias": "Confirmation bias", "occurrences": 1, "mechanism_constraint": "Readily accepting supporting testimonials while delaying retrieval of potentially disconfirming statistical data, despite no scheduling barrier to prompt retrieval" },
      { "bias": "Averaging Bias", "occurrences": 1, "mechanism_constraint": "Averaging widely divergent rubric scores into a single composite without investigating the disagreement, despite no imminent scheduling emergency" }
    ],
    "target_bias_names": [
      "Bandwagon effect",
      "Groupthink",
      "Availability Bias",
      "Anchoring Bias",
      "Confirmation bias",
      "Averaging Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 },
      { "bias": "Availability Bias", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 },
      { "bias": "Confirmation bias", "requested_occurrences": 1 },
      { "bias": "Averaging Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cfbw_01", "bias": "Bandwagon effect" },
      { "instance_id": "cfgt_01", "bias": "Groupthink" },
      { "instance_id": "cfav_01", "bias": "Availability Bias" },
      { "instance_id": "cfan_01", "bias": "Anchoring Bias" },
      { "instance_id": "cfcf_01", "bias": "Confirmation bias" },
      { "instance_id": "cfavg_01", "bias": "Averaging Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cfbw_01", "bias": "Bandwagon effect", "decision_point": 1 },
      { "instance_id": "cfgt_01", "bias": "Groupthink", "decision_point": 3 },
      { "instance_id": "cfav_01", "bias": "Availability Bias", "decision_point": 2 },
      { "instance_id": "cfan_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "cfcf_01", "bias": "Confirmation bias", "decision_point": 2 },
      { "instance_id": "cfavg_01", "bias": "Averaging Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cfbw_01",
        "bias": "Bandwagon effect",
        "mechanism": "Shortlisting attention allocated to Curriculum B based on secondhand reports of another district's enthusiasm rather than substantive independent review, unchanged despite a doubled review window",
        "affected_reasoning_operation": "Initial evidence-selection / shortlisting judgment",
        "evidence_source": "Conference report of neighboring district's reception of Curriculum B",
        "distinctiveness_requirement": "Occurs at the shortlisting moment before any committee-generated evidence exists; distinct from cfan_01's later comparative evaluation of already-shortlisted options"
      },
      {
        "instance_id": "cfgt_01",
        "bias": "Groupthink",
        "mechanism": "Committee suppresses full airing of a dissenting pilot teacher's pacing concern under pre-existing majority preference, moving to apparent consensus despite ample remaining weeks before the deadline",
        "affected_reasoning_operation": "Group deliberation / dissent evaluation before consensus decision",
        "evidence_source": "Pilot teacher's mid-pilot pacing report and the unvoiced reservation of one committee member",
        "distinctiveness_requirement": "Distinct from cfcf_01 in that it concerns suppression of an internal dissenting voice within a group deliberation moment, not selective external evidence-seeking"
      },
      {
        "instance_id": "cfav_01",
        "bias": "Availability Bias",
        "mechanism": "A vivid single-classroom anecdote is recalled and weighted more heavily in confidence-formation than a less memorable statistical report from the same meeting, despite ample time to retrieve the report promptly",
        "affected_reasoning_operation": "Recall and weighting of evidence for confidence formation",
        "evidence_source": "Vendor meeting anecdote vs. comparable-district statistical pilot report",
        "distinctiveness_requirement": "Distinct from cfcf_01: concerns differential recall/salience of two pieces of evidence encountered simultaneously, not selective retrieval based on prior preference"
      },
      {
        "instance_id": "cfan_01",
        "bias": "Anchoring Bias",
        "mechanism": "Early-formed frontrunner status of Curriculum B persists as an implicit reference point against which subsequently reviewed options are measured, unchanged by additional available review time",
        "affected_reasoning_operation": "Comparative evaluation of new evidence relative to an established reference point",
        "evidence_source": "Curriculum A's differentiation plan, reviewed and judged relative to Curriculum B's presumptive lead",
        "distinctiveness_requirement": "Occurs during later comparative evaluation, distinct from cfbw_01's earlier shortlisting-attention moment at the same decision point"
      },
      {
        "instance_id": "cfcf_01",
        "bias": "Confirmation bias",
        "mechanism": "Committee members readily accept testimonials consistent with existing favorable view of Curriculum B while deprioritizing retrieval of a statistical report that could complicate that view, despite no scheduling barrier to prompt retrieval",
        "affected_reasoning_operation": "Selective evidence-seeking and evidence-acceptance following an existing preference",
        "evidence_source": "Vendor testimonials (accepted readily) vs. comparable-district statistical report (retrieval delayed)",
        "distinctiveness_requirement": "Distinct from cfav_01: concerns motivated prioritization of evidence-seeking effort based on prior preference, not passive differential memorability"
      },
      {
        "instance_id": "cfavg_01",
        "bias": "Averaging Bias",
        "mechanism": "Chair combines widely divergent individual rubric scores into a single composite without investigating the underlying disagreement, treating the mean as settled despite no imminent scheduling emergency",
        "affected_reasoning_operation": "Aggregation of conflicting quantitative judgments into a summary decision metric",
        "evidence_source": "Individual rubric scores on the differentiation-support criterion for Curriculum A",
        "distinctiveness_requirement": "Sole aggregation-stage occurrence; not related to any other instance's evidence source"
      }
    ],
    "intended_strength": [
      { "instance_id": "cfbw_01", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "cfgt_01", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "cfav_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "cfan_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cfcf_01", "bias": "Confirmation bias", "strength": "subtle" },
      { "instance_id": "cfavg_01", "bias": "Averaging Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": "EI_Biased_6",
    "counterfactual_variable": {
      "name": "Length of the committee's adoption-cycle deadline",
      "original_state": "Six-week hard deadline creating acute schedule pressure throughout the process",
      "changed_state": "Twelve-week deadline (doubled review window), substantially reducing acute schedule pressure at each decision point",
      "variables_to_hold_constant": [
        "The three publisher proposals and their content",
        "The neighboring district's conference testimony about Curriculum B",
        "The vendor stakeholder meeting, anecdote, and statistical report",
        "The pilot structure, pacing concern, and its later recurrence",
        "The final rubric-scoring process and the two-high/two-low split on Curriculum A",
        "Committee composition and the board's eventual questions",
        "The four-decision-point narrative structure and sequence of events"
      ]
    },
    "scenario_id": "EI_Counterfactual_6",
    "domain_id": "EI",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences mirror EI_Biased_6's allocation exactly (decision points 1 and 2 each host two biases at distinct moments/evidence sources; decision points 3 and 4 each host one bias), since the counterfactual condition requires holding the bias-embedding structure constant while varying only the deadline-length causal variable. No decision point holds more than two instances of the same bias (each bias occurs only once total). Assignment prioritized mechanism-context fit identically to the paired scenario: bandwagon and anchoring both relate to initial/comparative shortlisting judgments (decision point 1) but target distinct moments; availability and confirmation both relate to processing the same vendor-meeting evidence (decision point 2) but target distinct cognitive operations; groupthink fits the group-consensus moment (decision point 3); averaging bias fits the numerical aggregation moment (decision point 4).",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "The three publisher proposals and their content",
      "The neighboring district's conference testimony about Curriculum B",
      "The vendor stakeholder meeting, anecdote, and statistical report",
      "The pilot structure, pacing concern, and its later recurrence",
      "The final rubric-scoring process and the two-high/two-low split on Curriculum A",
      "Committee composition and the board's eventual questions",
      "The four-decision-point narrative structure and sequence of events"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "seg_01",
          "speaker": "Participant",
          "segment_type": "decision_point_1_shortlisting",
          "raw_interview_anchor": "Two members returned from a regional math conference enthusiastic about Curriculum B; the first working session centered on B and A and C received a checklist pass.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cfbw_01"
          ],
          "ground_truth_rationale": "Curriculum B received priority attention because of another district's positive reception, even though the committee had twelve weeks and no scheduling reason to skip an even initial review."
        },
        {
          "segment_id": "seg_02",
          "speaker": "Participant",
          "segment_type": "decision_point_1_later_comparison",
          "raw_interview_anchor": "Around scoring, Curriculum A was found to have a stronger differentiated-instruction plan, but discussion remained framed as whether A was good enough to make the committee reconsider B.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cfan_01"
          ],
          "ground_truth_rationale": "Curriculum B remained the implicit reference point for judging A after the initial shortlisting, despite the extended timeline."
        },
        {
          "segment_id": "seg_03",
          "speaker": "Participant",
          "segment_type": "decision_point_2_salient_evidence",
          "raw_interview_anchor": "At the vendor meeting, a vivid struggling-classroom turnaround story was remembered clearly while the statistical report covering multiple schools was barely registered and retrieved only weeks later.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cfav_01"
          ],
          "ground_truth_rationale": "The concrete anecdote was more readily recalled and weighted than the less vivid statistical report, despite ample time for prompt retrieval."
        },
        {
          "segment_id": "seg_04",
          "speaker": "Participant",
          "segment_type": "decision_point_2_confirmatory_evidence",
          "raw_interview_anchor": "The testimonials felt like confirmation of what the committee already believed; the report was treated as something to get to eventually even though nothing prevented retrieving it that week.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cfcf_01"
          ],
          "ground_truth_rationale": "Evidence consistent with the favorable view of B was accepted with less scrutiny while potentially complicating evidence was deprioritized."
        },
        {
          "segment_id": "seg_05",
          "speaker": "Participant",
          "segment_type": "decision_point_3_dissent",
          "raw_interview_anchor": "A pilot teacher flagged pacing problems; the concern was acknowledged and the conversation moved toward agreement, no second classroom was observed, and one member later said reservations were not voiced because of how the room felt.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cfgt_01"
          ],
          "ground_truth_rationale": "The group moved toward apparent consensus without fully airing or investigating dissent, although several weeks remained."
        },
        {
          "segment_id": "seg_06",
          "speaker": "Participant",
          "segment_type": "decision_point_4_aggregation",
          "raw_interview_anchor": "Curriculum A had two very high and two very low differentiation scores; the scores were averaged directly into a settled middling composite without discussing the split, and later it emerged that reviewers had read different appendices.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cfavg_01"
          ],
          "ground_truth_rationale": "A wide disagreement was collapsed into a single mean without investigating the underlying divergence despite no urgent deadline."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a single retrospective interview about a K-8 math curriculum adoption cycle. Only bias-specific reasoning mechanisms with affirmative interview evidence are reported; organizational and statistical practices are not treated as biases absent a distinct cognitive mechanism."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Conformity bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "anchoring-and-adjustment heuristic",
        "anchoring effect",
        "focalism"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information as a reference point and to make insufficient adjustments from that anchor in subsequent judgment.",
      "attributed_to_speaker": "Curriculum committee including Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial review and early narrowing of curriculum proposals after the regional conference",
      "decision_point_description": "Choosing how to allocate deep review among Curriculum A, Curriculum B, and Curriculum C after two members returned from a math conference.",
      "affected_reasoning_operation": "Attention allocation and later comparative evaluation of curricula",
      "bias_specific_mechanism": "The neighboring district's endorsement of Curriculum B became an initial focal value. The committee centered its first working session on B and later assessed alternatives relative to B rather than evaluating them independently.",
      "manifestation_in_interview": "Despite having twelve weeks, the first session centered on B, while A and C received only a checklist pass. Later, Curriculum A's strengths were framed as possible reasons to reconsider B rather than assessed on their own merits.",
      "effect_on_reasoning_or_decision": "It narrowed early exploration and made Curriculum B the default comparison standard, likely distorting later scoring and adoption decisions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our people came back energized, and even with all that extra runway, our first working session ended up centered on B. A and C got more of a checklist pass.",
          "evidence_explanation": "The initial Curriculum B endorsement immediately oriented the committee's attention toward B, with disproportionate depth allocated to B despite available time."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "even weeks into a much longer process, the conversation was still framed as 'is this good enough to make us reconsider B,' instead of just asking how strong A was standing on its own.",
          "evidence_explanation": "This shows the anchor persisting: Curriculum A was evaluated relative to B rather than independently."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "B just already felt like the likely outcome by the time real friction showed up, deadline or no deadline.",
          "evidence_explanation": "The initial anchor remained the default expected outcome even when conflicting evidence emerged."
        }
      ],
      "correction_or_counterevidence": "The committee did eventually revisit Curriculum A before final scoring and found it had a stronger differentiated-instruction plan, but the review remained framed relative to B, limiting correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support for anchoring-and-adjustment is available from Rastogi et al. (2022), although that study concerns AI-assisted decisions; the anchoring mechanism is treated as transferable.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source documents anchoring-and-adjustment as a heuristic involving insufficient adjustment from an initial anchor.",
          "relevance_to_this_occurrence": "The committee insufficiently adjusted away from the initial Curriculum B anchor despite having extra time, consistent with the anchoring-and-adjustment mechanism described in the source."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "vividness bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the weight or relevance of information based on how easily a vivid or memorable example comes to mind, rather than on more diagnostic statistical evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Weighing vendor-meeting evidence about Curriculum B",
      "decision_point_description": "Deciding how much weight to give a vivid teacher success story versus a statistical pilot report from a comparable district.",
      "affected_reasoning_operation": "Evidence weighting and judgment about Curriculum B's likely success",
      "bias_specific_mechanism": "The concrete, emotionally vivid classroom success story was highly memorable and easy to bring to mind, while the abstract statistical report was not. This ease of recall led to overweighting the anecdote and delaying the report.",
      "manifestation_in_interview": "The participant recalled the story in detail but barely registered the statistical report. The report was left unexamined for weeks even though it was available.",
      "effect_on_reasoning_or_decision": "It contributed to a locked-in sense of Curriculum B's promise before the diagnostic statistical evidence was reviewed; the report later showed mixed results.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "One of them told a really vivid story about a struggling classroom that turned around within a semester. I still remember the details clearly. Somewhere in that same meeting, someone mentioned a statistical pilot report from a comparable district, covering multiple schools over a full year. I barely registered that part.",
          "evidence_explanation": "The contrast between the vivid narrative and the barely registered statistical report shows evidence weighting driven by mental availability rather than diagnostic value."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The story was just more vivid — a real teacher, real kids, a real unit. The report was two sentences and some numbers I didn't have in front of me.",
          "evidence_explanation": "The participant explicitly identifies vividness as the reason the story dominated, a core feature of the availability heuristic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When we did, it showed mixed results across schools, not the clean win the anecdote suggested. But by then my sense of B's promise was already pretty locked in.",
          "evidence_explanation": "The more diagnostic statistical evidence arrived too late to shift the judgment already disproportionately influenced by the vivid anecdote."
        }
      ],
      "correction_or_counterevidence": "The statistical report was eventually pulled before final scoring and showed mixed results, but the participant reports that the prior sense of B's promise was already locked in.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the availability heuristic was not available; this label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "congeniality bias",
        "myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, or prioritize information in ways that support an existing belief, while discounting or delaying disconfirming evidence.",
      "attributed_to_speaker": "Curriculum committee including Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluating testimonials, the pilot report, and the pacing concern during Curriculum B review",
      "decision_point_description": "Deciding whether to scrutinize supportive testimonials, when to review the mixed pilot report, and how seriously to investigate a pilot teacher's pacing concern.",
      "affected_reasoning_operation": "Evidence evaluation and belief updating about Curriculum B",
      "bias_specific_mechanism": "Once Curriculum B was favored, favorable testimonials were accepted as confirmatory with little scrutiny, a mixed statistical report was treated as non-urgent, and a pilot concern was acknowledged but not deeply investigated.",
      "manifestation_in_interview": "The participant states that testimonials 'felt like they confirmed what we already believed' and therefore did not need scrutiny, while the report felt like something to get to eventually. The pilot concern was mentioned and then passed over.",
      "effect_on_reasoning_or_decision": "The committee maintained its Curriculum B preference despite mixed data and missed an early signal that the pacing problem was real.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The testimonials felt like they confirmed what we already believed from the conference, so they didn't feel like they needed more scrutiny. The report felt like something to get to eventually rather than something urgent, even though nothing was stopping us from pulling it the same week.",
          "evidence_explanation": "This explicitly describes confirmatory evidence being accepted uncritically while less supportive information was deprioritized."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It got mentioned, acknowledged, and the conversation moved along toward agreement fairly quickly anyway. We didn't send anyone to observe the second pilot classroom, even though we had the calendar space to do that easily.",
          "evidence_explanation": "The pacing concern was disconfirming evidence about Curriculum B, but it was not investigated despite available time, consistent with discounting disconfirming information."
        }
      ],
      "correction_or_counterevidence": "The statistical report was eventually examined, and the pacing issue later recurred in full rollout, but these did not trigger meaningful reevaluation at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support for confirmation bias is available from the Cook and Smallman source, though it concerns intelligence analysis rather than curriculum adoption.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human Factors of the Confirmation Bias in Intelligence Analysis",
          "authors": "Cook and Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "The first bias-reducing technique, graphical ... revealed no bias at as- sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source documents confirmation bias as a strong tendency to select and prioritize evidence in a belief-consistent way.",
          "relevance_to_this_occurrence": "The committee selectively prioritized confirmatory testimonials and deferred the less supportive statistical report, matching the confirmatory evidence-prioritization pattern in the source."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Conformity bias",
      "alternative_labels": [
        "social conformity",
        "self-censorship",
        "groupthink-related self-censorship"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to align one's expressed views with the perceived majority, or to suppress dissent, due to social pressure or the perceived climate of the group.",
      "attributed_to_speaker": "Unidentified committee member",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Handling of the pilot teacher's pacing concern during a committee meeting",
      "decision_point_description": "Whether committee members voiced their reservations about the pacing concern as the group moved toward agreement.",
      "affected_reasoning_operation": "Willingness to voice disagreement in a group decision",
      "bias_specific_mechanism": "A committee member had substantive reservations but did not voice them because the perceived mood or majority of the room favored moving ahead.",
      "manifestation_in_interview": "The participant later learned that one member remained silent about reservations due to how the room felt.",
      "effect_on_reasoning_or_decision": "It reduced the diversity of expressed input and allowed the pacing concern to receive less scrutiny than it otherwise might have.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I found out afterward that one member had reservations that day but didn't voice them, given how the room felt.",
          "evidence_explanation": "The member's silence is directly attributed to the perceived social climate, indicating conformity-based self-censorship rather than agreement."
        }
      ],
      "correction_or_counterevidence": "The pacing concern itself was raised by a pilot teacher, so the issue did reach the committee; the bias is limited to one member's unvoiced reservations.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for conformity bias was not available; this label is drawn from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Planning fallacy",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Curriculum committee including Participant",
      "possible_decision_episode_label": "Initial plan to give all three curriculum proposals a deep review during the twelve-week cycle",
      "supporting_interview_quote": "With twelve weeks, we had every intention of giving all three a genuinely deep look before narrowing anything down. But right around when the proposals landed, two of our members came back from a regional math conference where a neighboring district presented on their experience adopting Curriculum B.",
      "plausible_mechanism": "The committee formed an optimistic plan about how evenly its review time would be allocated, but attention was quickly captured by Curriculum B and the plan was not followed despite adequate time.",
      "why_not_identified": "The transcript does not show an explicit optimistic underestimation of time or difficulty; the early focus on B is better explained by anchoring on the conference endorsement than by a planning-fallacy mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective self-report interview; recollections may be shaped by memory or narrative reconstruction.",
    "Availability heuristic and conformity bias lack direct retrieved corpus support and rely on general cognitive-science knowledge.",
    "Retrieved corpus support for anchoring and confirmation comes from AI-assisted decision-making and intelligence analysis contexts respectively, so applicability to curriculum adoption is analogical rather than task-matched.",
    "No controlled benchmark or behavioral measure is available; confidence levels reflect strength of interview evidence only."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Counterfactual_6_Sonar_on",
  "interview_id": "EI_Counterfactual_6",
  "system_prompt_id": "Sonar",
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
