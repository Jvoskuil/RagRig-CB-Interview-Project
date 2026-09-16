You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with me recording this conversation for internal research on how curriculum decisions get made, and that anything you share will be used in de-identified form. Is that all right?

Participant: Yes, that's fine.

Interviewer: Great. Can you tell me a bit about your role on the committee and what you were tasked with?

Participant: I've been on the district's curriculum committee for about five years, mostly representing the middle school math teachers. Last fall, after our sixth-grade state test scores dropped eight points district-wide, the superintendent's office asked us to run a full adoption cycle for a new K-8 math curriculum. We had six weeks to land on a recommendation for the board, which is tight given everyone on the committee still has a full teaching or admin load.

Interviewer: Walk me through how the process actually started.

Participant: Three publishers submitted proposals — I'll just call them Curriculum A, B, and C. Each came with a standards alignment matrix, sample units, and vendor support materials. Normally we'd sit with all three for a couple of weeks before narrowing anything down. But right around the time proposals came in, two of our members went to a regional math conference, and a neighboring district's team was there presenting on their experience adopting Curriculum B the year before. They were genuinely excited about it — said it had turned around their pacing problems. Our folks came back energized, and honestly, that shaped how we opened our first working session. We spent most of that meeting digging into B's materials and gave A and C a lighter pass, more of a checklist review than a deep one.

Interviewer: Was that split in attention a deliberate committee decision, or did it happen more organically?

Participant: A little of both. Nobody said "let's only look at B." But once people were talking about what the neighboring district found, it became the natural center of gravity. We told ourselves we'd circle back to A and C in depth later.

Interviewer: Did you?

Participant: Somewhat. Later on, when we got into scoring, we did revisit Curriculum A's proposal, and it actually had a more detailed differentiated-instruction support plan than B's. But by then the conversation kept framing it as "is this good enough to change our minds about B," rather than just asking how strong A was on its own. It's a subtle thing, but I noticed it happening even in how I phrased my own notes.

Interviewer: Let's move to the vendor stakeholder meeting. What happened there?

Participant: That was about two and a half weeks in. Curriculum B's rep organized a session with committee members from other districts already using it. A couple of them told a really specific story about a struggling classroom that turned around within a semester — kids who'd been behind were suddenly hitting grade-level benchmarks. It was vivid, it was well told, and I remember it clearly even now. Somewhere in the same meeting, someone also mentioned there was a statistical pilot report from a comparable district, multiple schools, showing outcomes over a full year. I didn't retain much from that part at all.

Interviewer: What made the classroom story stick with you more than the statistical report?

Participant: Honestly, I think it's just more concrete. You can picture it — a teacher, specific kids, a specific unit. The report was a couple of sentences and some numbers I didn't have in front of me. I remember thinking, "I should get a copy of that," but it wasn't until weeks later, closer to our final scoring, that anyone actually pulled it up. When we did, it showed mixed results across schools, not a clean success story. But by then, my gut sense of B's promise was already pretty well formed.

Interviewer: How did that gut sense affect the testimonials versus the report going forward?

Participant: The testimonials felt like they confirmed what we already suspected from the conference buzz, so they didn't feel like they needed extra scrutiny. The statistical report, when it came up, felt more like something to double check later rather than something urgent to chase down immediately. Looking back, that's probably backwards in terms of which one deserved more weight.

Interviewer: Let's talk about the pilot. What happened when concerns came up mid-pilot?

Participant: We ran a three-week classroom pilot of Curriculum B in two schools. About halfway through, one of the pilot teachers flagged pacing problems in one of the units — said the lesson sequencing didn't match how her students were actually progressing. By that point, though, most of the committee had already spoken favorably about B in prior meetings, and we were coming up on a meeting where the chair wanted to move toward consensus so we wouldn't lose time before the board deadline.

Interviewer: How was that concern handled in the meeting?

Participant: It got mentioned, acknowledged, and then the conversation moved on fairly quickly toward agreement. Nobody shot it down exactly, but nobody dug into it either. We didn't send someone to observe the second pilot classroom, we didn't ask the teacher for more detail in writing. We just kind of nodded and kept going. I found out afterward, informally, that one of our members told a colleague they'd actually had some reservations that day but didn't say so out loud, given how the room felt.

Interviewer: Did that pacing issue turn out to matter?

Participant: Yes, actually. When we rolled out further, a second classroom hit the same pacing snag. So the concern was real. It just didn't get a real hearing in the moment.

Interviewer: Last decision point — the final scoring. How did that work?

Participant: Each of us submitted rubric scores across five criteria for all three curricula. When the chair compiled them, Curriculum A had a strange split on the differentiated-instruction-support criterion — two of us scored it very high, two very low. B's scores were tighter across the board. The chair needed one composite number per curriculum for the board memo, so the scores just got averaged straight across, including that split on A. Once that single number came back looking like a solid, middling score for A, it read as settled — nobody asked what was underneath it or suggested pulling the individual ratings back apart before we moved on.

Interviewer: Was the disagreement on Curriculum A discussed before the numbers were combined?

Participant: Not really. It went into the spreadsheet like the rest, and the composite itself seemed to close the question rather than open it. It was only afterward, when someone asked why the differentiation score for A looked so middling despite that internal splitting, that we realized the two low scorers hadn't actually reviewed A's differentiation appendix, while the two high scorers had. So the average wasn't really representing consensus — it was masking a difference in how thoroughly people had reviewed the material.

Interviewer: Did the board notice that?

Participant: They asked about it, yeah. Why a criterion with that much internal disagreement was reported as one clean number. We didn't have a great answer beyond "that's how we compile scores."

Interviewer: Stepping back — was there a point in this process where you felt uncertain whether the committee had the full picture?

Participant: A few times, honestly. The pacing concern is the one that sits with me most. I don't think anyone was acting in bad faith. We were just moving fast, and B already felt like the likely outcome by the time real friction showed up.

Interviewer: If the pilot teacher's pacing concern had surfaced earlier in the process, do you think the outcome would have changed?

Participant: Possibly. If it had come up before the vendor meeting, before people's minds were as made up, I think it would've gotten a more serious look. Coming when it did, it was fighting a lot of momentum.

Interviewer: And if the neighboring district hadn't mentioned Curriculum B at that conference at all?

Participant: I've wondered that. I think we would have given A and C a more even start. B still might have won out — its materials were solid — but the early spotlight wouldn't have been there from day one.

Interviewer: One last one — if you had the scoring step to do over, would you handle the split differently?

Participant: Yes. I'd flag any criterion with a wide spread and ask why, before collapsing it into one number. In this case, the spread was actually telling us something useful, and averaging it just erased that signal.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Biased_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Bandwagon effect", "occurrences": 1, "mechanism_constraint": "Elevation of a curriculum based on external district enthusiasm/popularity signal rather than independent evidence review" },
      { "bias": "Groupthink", "occurrences": 1, "mechanism_constraint": "Suppression of dissenting pilot-teacher feedback under time pressure and majority preference, with a member's unvoiced reservation" },
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Overweighting a vivid single-classroom anecdote over a less memorable statistical report" },
      { "bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "Evaluating subsequent curricula relative to an early-formed frontrunner reference point" },
      { "bias": "Confirmation bias", "occurrences": 1, "mechanism_constraint": "Readily accepting supporting testimonials while delaying retrieval of potentially disconfirming statistical data" },
      { "bias": "Averaging Bias", "occurrences": 1, "mechanism_constraint": "Averaging widely divergent rubric scores into a single composite without investigating the disagreement" }
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
      { "instance_id": "bw_01", "bias": "Bandwagon effect" },
      { "instance_id": "gt_01", "bias": "Groupthink" },
      { "instance_id": "av_01", "bias": "Availability Bias" },
      { "instance_id": "an_01", "bias": "Anchoring Bias" },
      { "instance_id": "cf_01", "bias": "Confirmation bias" },
      { "instance_id": "avg_01", "bias": "Averaging Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "bw_01", "bias": "Bandwagon effect", "decision_point": 1 },
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 3 },
      { "instance_id": "av_01", "bias": "Availability Bias", "decision_point": 2 },
      { "instance_id": "an_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "cf_01", "bias": "Confirmation bias", "decision_point": 2 },
      { "instance_id": "avg_01", "bias": "Averaging Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "bw_01",
        "bias": "Bandwagon effect",
        "mechanism": "Shortlisting attention allocated to Curriculum B based on secondhand reports of another district's enthusiasm rather than substantive independent review",
        "affected_reasoning_operation": "Initial evidence-selection / shortlisting judgment",
        "evidence_source": "Conference report of neighboring district's reception of Curriculum B",
        "distinctiveness_requirement": "Occurs at the shortlisting moment before any committee-generated evidence exists; distinct from an_01's later comparative evaluation of already-shortlisted options"
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Committee suppresses full airing of a dissenting pilot teacher's pacing concern under time pressure and pre-existing majority preference, moving to apparent consensus",
        "affected_reasoning_operation": "Group deliberation / dissent evaluation before consensus decision",
        "evidence_source": "Pilot teacher's mid-pilot pacing report and the unvoiced reservation of one committee member",
        "distinctiveness_requirement": "Distinct from cf_01 in that it concerns suppression of an internal dissenting voice within a group deliberation moment, not selective external evidence-seeking"
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "A vivid single-classroom anecdote is recalled and weighted more heavily in confidence-formation than a less memorable statistical report from the same meeting",
        "affected_reasoning_operation": "Recall and weighting of evidence for confidence formation",
        "evidence_source": "Vendor meeting anecdote vs. comparable-district statistical pilot report",
        "distinctiveness_requirement": "Distinct from cf_01: concerns differential recall/salience of two pieces of evidence encountered simultaneously, not selective retrieval based on prior preference"
      },
      {
        "instance_id": "an_01",
        "bias": "Anchoring Bias",
        "mechanism": "Early-formed frontrunner status of Curriculum B persists as an implicit reference point against which subsequently reviewed options are measured",
        "affected_reasoning_operation": "Comparative evaluation of new evidence relative to an established reference point",
        "evidence_source": "Curriculum A's differentiation plan, reviewed and judged relative to Curriculum B's presumptive lead",
        "distinctiveness_requirement": "Occurs during later comparative evaluation, distinct from bw_01's earlier shortlisting-attention moment at the same decision point"
      },
      {
        "instance_id": "cf_01",
        "bias": "Confirmation bias",
        "mechanism": "Committee members readily accept testimonials consistent with existing favorable view of Curriculum B while deprioritizing retrieval of a statistical report that could complicate that view",
        "affected_reasoning_operation": "Selective evidence-seeking and evidence-acceptance following an existing preference",
        "evidence_source": "Vendor testimonials (accepted readily) vs. comparable-district statistical report (retrieval delayed)",
        "distinctiveness_requirement": "Distinct from av_01: concerns motivated prioritization of evidence-seeking effort based on prior preference, not passive differential memorability"
      },
      {
        "instance_id": "avg_01",
        "bias": "Averaging Bias",
        "mechanism": "Chair combines widely divergent individual rubric scores into a single composite without investigating the underlying disagreement",
        "affected_reasoning_operation": "Aggregation of conflicting quantitative judgments into a summary decision metric",
        "evidence_source": "Individual rubric scores on the differentiation-support criterion for Curriculum A",
        "distinctiveness_requirement": "Sole aggregation-stage occurrence; not related to any other instance's evidence source"
      }
    ],
    "intended_strength": [
      { "instance_id": "bw_01", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "an_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "cf_01", "bias": "Confirmation bias", "strength": "subtle" },
      { "instance_id": "avg_01", "bias": "Averaging Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Biased_6",
    "domain_id": "EI",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences spread across distinct decision points where mechanism fit permitted (decision points 1 and 2 each host two biases but with clearly separated evidence sources and reasoning operations per instance; decision points 3 and 4 each host one bias). No decision point holds more than two instances of the same bias (each bias occurs only once total, satisfying constraint trivially). Assignment prioritized mechanism-context fit: bandwagon and anchoring both relate to initial/comparative shortlisting judgments (decision point 1) but target distinct moments (initial attention vs. later comparison); availability and confirmation both relate to processing the same vendor-meeting evidence (decision point 2) but target distinct cognitive operations (passive recall/salience vs. motivated evidence-seeking); groupthink fits the group-consensus moment (decision point 3); averaging bias fits the numerical aggregation moment (decision point 4).",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the interview transcript for affirmatively demonstrated cognitive biases in curriculum committee decision-making. Classifications were limited to mechanisms with clear transcript evidence; a scoring-aggregation concern was retained as a candidate rather than a confirmed bias."
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
      "bias_label": "Groupthink",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring and adjustment", "Anchoring heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which an initial value, reference point, or impression exerts disproportionate influence on subsequent judgments, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant / curriculum committee",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial curriculum review and later scoring comparisons",
      "decision_point_description": "Allocation of review attention among Curriculum A, B, and C, and later framing of Curriculum A relative to Curriculum B during scoring.",
      "affected_reasoning_operation": "Evidence weighting, comparative evaluation, and information-search allocation",
      "bias_specific_mechanism": "The neighboring district’s enthusiastic presentation of Curriculum B created an initial reference point that became the default or anchor; subsequent review of alternatives was conducted against that anchor, with insufficient adjustment away from it.",
      "manifestation_in_interview": "The committee spent most of the first working session on Curriculum B, gave A and C only checklist-level review, and later framed Curriculum A as needing to be good enough to change minds about B rather than evaluating A independently.",
      "effect_on_reasoning_or_decision": "Alternatives were not evaluated independently from the outset; the early advantage for B was carried forward into scoring and likely shaped the final preference.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We spent most of that meeting digging into B's materials and gave A and C a lighter pass, more of a checklist review than a deep one.",
          "evidence_explanation": "Shows asymmetric attention immediately following the B-focused conference presentation, consistent with an initial anchor shaping information search."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But by then the conversation kept framing it as 'is this good enough to change our minds about B,' rather than just asking how strong A was on its own.",
          "evidence_explanation": "Demonstrates that Curriculum B became the reference point against which Curriculum A was judged, rather than evaluating A independently, a hallmark of anchoring."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once people were talking about what the neighboring district found, it became the natural center of gravity.",
          "evidence_explanation": "Shows that the initial B-related information became the organizing focus of the committee’s subsequent inquiry."
        }
      ],
      "correction_or_counterevidence": "No explicit correction occurred, though the participant later acknowledged that Curriculum B might still have won without the early spotlight; the counterfactual does not undo the asymmetric evaluative process.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Rastogi et al. (2022) passage supports the anchoring-and-adjustment mechanism and its influence on decision-making under time constraints.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Time allocation. To investigate the eect of time on the anchoringandadjustment heuristic in AIassisted decisionmaking... This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The passage describes anchoring-and-adjustment as a decision heuristic in which an initial reference point influences subsequent judgment, with adjustment varying by available time or effort.",
          "relevance_to_this_occurrence": "Supports the claim that an initial reference point, here the neighboring district’s recommendation, can anchor subsequent evaluation and lead to insufficient adjustment."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Availability heuristic",
      "alternative_labels": ["Vividness effect", "Salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which ease of retrieval or vividness of information inflates its judged frequency, importance, or evidentiary weight.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor stakeholder meeting and evidence weighting",
      "decision_point_description": "Weighting of a vivid classroom testimony versus a multi-school statistical pilot report.",
      "affected_reasoning_operation": "Memory retrieval and evidence weighting",
      "bias_specific_mechanism": "The concrete, emotionally vivid classroom story was more easily remembered and mentally available than the abstract statistical pilot findings, leading to disproportionate influence on the committee’s emerging judgment.",
      "manifestation_in_interview": "The participant recalled the classroom story clearly but did not retain the statistical report details; the story then anchored a positive gut sense of Curriculum B despite later mixed statistical results.",
      "effect_on_reasoning_or_decision": "Testimonial evidence was overweighted relative to statistical evidence, with the report chased only after a preliminary preference had already formed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "A couple of them told a really specific story about a struggling classroom that turned around within a semester — kids who'd been behind were suddenly hitting grade-level benchmarks. It was vivid, it was well told, and I remember it clearly even now. Somewhere in the same meeting, someone also mentioned there was a statistical pilot report from a comparable district, multiple schools, showing outcomes over a full year. I didn't retain much from that part at all.",
          "evidence_explanation": "Directly contrasts strong memory for a vivid anecdote with poor memory for statistical findings, indicating differential mental availability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I think it's just more concrete. You can picture it — a teacher, specific kids, a specific unit. The report was a couple of sentences and some numbers I didn't have in front of me.",
          "evidence_explanation": "Attributes the differential recall to concreteness and imageability, classic drivers of the availability heuristic."
        }
      ],
      "correction_or_counterevidence": "The statistical report was later pulled and showed mixed results, but this occurred after the anecdote-influenced gut sense was already formed, so the correction did not prevent the bias from affecting early judgment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressing the availability heuristic or vividness effect was supplied; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Confirmatory information search", "Myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, favor, or recall information in ways that confirm prior beliefs or expectations, while giving less scrutiny to disconfirming or mixed evidence.",
      "attributed_to_speaker": "Participant / curriculum committee",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluation of testimonials and statistical pilot report",
      "decision_point_description": "Whether to prioritize immediate scrutiny of testimonial and statistical evidence bearing on Curriculum B.",
      "affected_reasoning_operation": "Evidence interpretation and information-search prioritization",
      "bias_specific_mechanism": "Once a positive prior impression of Curriculum B formed, confirmatory testimonials were accepted with little scrutiny while mixed statistical evidence was deferred and treated as non-urgent; this preserved the existing favorable judgment.",
      "manifestation_in_interview": "The participant described testimonials as feeling like they confirmed prior conference-derived expectations and the statistical report as something to check later; mixed results arrived only after the gut sense had formed.",
      "effect_on_reasoning_or_decision": "Disconfirming or mixed evidence was not incorporated into initial preference formation, increasing confidence in Curriculum B without adequate scrutiny.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The testimonials felt like they confirmed what we already suspected from the conference buzz, so they didn't feel like they needed extra scrutiny.",
          "evidence_explanation": "Shows that prior expectations reduced scrutiny of confirmatory evidence, a core confirmation-bias mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The statistical report, when it came up, felt more like something to double check later rather than something urgent to chase down immediately. Looking back, that's probably backwards in terms of which one deserved more weight.",
          "evidence_explanation": "Demonstrates deprioritization of potentially disconfirming evidence, consistent with a confirmatory information-search pattern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When we did, it showed mixed results across schools, not a clean success story. But by then, my gut sense of B's promise was already pretty well formed.",
          "evidence_explanation": "Indicates that the prior belief was already consolidated before the mixed evidence was examined, so the inconsistent evidence did not receive timely weight."
        }
      ],
      "correction_or_counterevidence": "No in-the-moment correction; the participant retrospectively noted that the relative weighting was probably backwards.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Cook and Smallman (2008) passage supports confirmation bias as a bias in selecting and prioritizing evidence, validating the mechanism of favoritism toward confirmatory material.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human Factors of the Confirmation Bias in Intelligence Analysis: Decision Support from Graphical Evidence",
          "authors": "Cook & Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source identifies confirmation bias as a bias in selecting and prioritizing evidence during analysis.",
          "relevance_to_this_occurrence": "Supports the occurrence of prioritizing confirmatory testimonials while deferring mixed statistical evidence."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Groupthink",
      "alternative_labels": ["Self-censorship", "Illusion of unanimity"],
      "taxonomy_status": "established_label",
      "bias_definition": "A group decision-making phenomenon in which the desire for cohesion or consensus suppresses dissent, skeptical inquiry, and open evaluation of alternatives.",
      "attributed_to_speaker": "Unnamed committee member / curriculum committee",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Mid-pilot pacing concern discussion",
      "decision_point_description": "Whether to investigate the pilot teacher's pacing concern or proceed toward consensus on Curriculum B.",
      "affected_reasoning_operation": "Group judgment and evaluation of disconfirming operational evidence",
      "bias_specific_mechanism": "Perceived room consensus and momentum toward agreement discouraged voicing contrary reservations; the concern was acknowledged but not interrogated, creating false agreement.",
      "manifestation_in_interview": "The pilot teacher’s concern was mentioned and quickly passed over. A member with reservations did not speak up because of how the room felt, and the committee did not investigate further.",
      "effect_on_reasoning_or_decision": "A real pacing issue was left unexamined and later recurred; the committee’s confidence in its recommendation proceeded without incorporating the concern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It got mentioned, acknowledged, and then the conversation moved on fairly quickly toward agreement. Nobody shot it down exactly, but nobody dug into it either. We didn't send someone to observe the second pilot classroom, we didn't ask the teacher for more detail in writing. We just kind of nodded and kept going.",
          "evidence_explanation": "Demonstrates consensus-seeking behavior and failure to investigate dissenting evidence during group discussion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I found out afterward, informally, that one of our members told a colleague they'd actually had some reservations that day but didn't say so out loud, given how the room felt.",
          "evidence_explanation": "Provides direct evidence of self-censorship due to perceived group atmosphere, a core groupthink mechanism."
        }
      ],
      "correction_or_counterevidence": "The pacing concern later recurred in a second classroom, showing that it was valid; no contemporaneous correction occurred within the meeting.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically addressing groupthink or self-censorship in group decision-making was supplied; classification relies on established cognitive-science and social-psychology knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": null,
      "alternative_labels": ["Averaging/aggregation bias", "Insensitivity to distributional variance"],
      "taxonomy_status": "label_uncertain",
      "speaker_or_attributed_person": "Curriculum committee / chair",
      "possible_decision_episode_label": "Final scoring of Curriculum A differentiated-instruction-support criterion",
      "supporting_interview_quote": "The chair needed one composite number per curriculum for the board memo, so the scores just got averaged straight across, including that split on A. Once that single number came back looking like a solid, middling score for A, it read as settled — nobody asked what was underneath it or suggested pulling the individual ratings back apart before we moved on.",
      "plausible_mechanism": "A single summary statistic, the mean, was accepted as a meaningful consensus signal even though it masked bimodal ratings produced by different levels of review thoroughness; this may reflect overreliance on an aggregated number or insensitivity to distributional variance.",
      "why_not_identified": "The transcript identifies a decision-process flaw but does not affirm a specific cognitive mechanism beyond standard aggregation or procedural practice; it could be explained by ordinary rubric compilation, time pressure, or limited attention rather than a distinct cognitive bias."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus was limited and did not cover all identified mechanisms; the availability heuristic and groupthink classifications rely on general cognitive-science and social-psychology knowledge rather than supplied passages.",
    "The analysis is based on a single retrospective interview, so group-level attributions rely on the interviewed participant's summary rather than direct observation of all committee members.",
    "Quotations reflect the participant’s recall and framing, which may itself be influenced by memory biases, though the reported decision process provides sufficient evidence for the identified mechanisms."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Biased_6_Gemini_on",
  "interview_id": "EI_Biased_6",
  "system_prompt_id": "Gemini",
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
