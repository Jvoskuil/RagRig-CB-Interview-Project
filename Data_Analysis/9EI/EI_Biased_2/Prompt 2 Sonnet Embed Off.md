You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is for our instructional practice research and will be handled confidentially. Can you start by telling me your role and how the Bridge Literacy pilot came about?

Participant: Sure. I'm the Curriculum Coordinator for K-5, and I also run our instructional coaching cycle across the elementary buildings. I brought Bridge Literacy in after seeing it presented at a state conference last spring. It's a structured literacy approach, more explicit phonics sequencing than what we'd been using. I pitched it to the superintendent, and we set it up as a trimester pilot in six classrooms across our two elementary schools.

Interviewer: And what were you trying to accomplish with the checkpoint review you did partway through?

Participant: The board needed a scale-up recommendation before the next budget cycle, so I had to look at the trimester oral reading fluency benchmark data, figure out if the pilot was working, and decide what to tell the finance committee. There's real competition for dollars — the math intervention team wants the same PD budget — so whatever I brought needed to be solid.

Interviewer: Walk me through what happened when the data actually came in.

Participant: The literacy specialist sent me the classroom-level fluency results in early February. Three classrooms were clearly above the expected growth rate, three were flat or just mixed. My first reaction was — okay, this is a real pilot, we're going to have variation. But when I looked closer at the three flat classrooms, I noticed the testing had happened on different days at the two schools because of a scheduling conflict. That felt like something worth flagging. I asked the specialist to check whether that timing gap could explain the flat results.

Interviewer: Did you look at the testing conditions in the classrooms that showed gains too?

Participant: Not in the same way, no. Those looked like the program was doing what we hoped, so I didn't feel the same urgency to dig into how the testing was administered there. In hindsight, the scheduling issue technically applied across the whole window, not just to certain rooms, but at the time my attention went to the classrooms where the results didn't match what I expected.

Interviewer: What did you learn afterward?

Participant: The specialist came back about a week later and said the testing conditions were actually pretty similar across all six classrooms — the day-to-day difference wasn't significant. And separately, one of the flat classrooms had unusually high absenteeism that same week, which probably mattered more than timing.

Interviewer: When you were deciding how much scrutiny to apply, what alternatives did you consider?

Participant: I could have treated all six the same way from the start — same level of questioning regardless of outcome. Or waited for the specialist to audit everything before drawing any conclusions. I didn't do either of those first. I went straight to questioning the ones that weren't showing growth.

Interviewer: Let's move to the board meeting prep. What did that involve?

Participant: I had fifteen minutes on the agenda, and the math team was presenting right after me. I had the six-classroom fluency numbers plus a walkthrough-observation log the specialist and I had been keeping. I decided to bring a highlights slide with the aggregate trend line rather than all six classrooms individually — mostly a time issue, honestly. Fifteen minutes isn't enough to walk through six separate data profiles and still leave room for questions.

Interviewer: Any consequence from that choice?

Participant: One board member asked for classroom-by-classroom detail I hadn't included. I had the numbers on hand, just not on the slide, so I was able to answer, but it did mean I was talking through figures I hadn't rehearsed presenting.

Interviewer: Around the same time, you had PD feedback to review. What did that look like?

Participant: Five of six pilot teachers filled out a survey after the coaching session, rated it helpful or very helpful. One comment mentioned the pacing guide felt rushed for lower-performing students. It's a small sample and it was voluntary, so I noted that caveat when I summarized it — I didn't want to present five responses as if that settled anything about how teachers overall felt.

Interviewer: Did you follow up on the one teacher who didn't respond?

Participant: Not right away. The specialist later mentioned that two of the non-responses were actually invitations that went to teachers in the flat classrooms, which made me wonder if we were mostly hearing from teachers who were already seeing good results. I flagged that as a limitation rather than treating the survey as fully representative.

Interviewer: Let's get to the recommendation memo. How did you explain the fluency gains?

Participant: The aggregate number was a modest net gain across all six classrooms. I'd been doing biweekly coaching visits in four of the six rooms all trimester — modeling lessons, giving feedback, that kind of thing. When I wrote the memo, I framed the gains as largely a product of that coaching cycle, and I recommended that if we scale up, we'd need to replicate that same coaching frequency districtwide, which means adding coaching staff.

Interviewer: What about the two classrooms that improved without your direct coaching visits?

Participant: They did show gains too, yes. I mentioned the new decodable-text materials and the smaller class sizes in a line or two, but the core of the recommendation centered on the coaching model, since that's the piece I could speak to most directly and the piece I think drove the results I was seeing week to week.

Interviewer: A board member raised that point later, is that right?

Participant: Right, someone pointed out afterward that the two non-visited classrooms also improved, and asked how that fit with a coaching-centered explanation. I said we'd need more study to fully untangle it — with materials, class size, and coaching all overlapping in those rooms, I couldn't say for certain which factor explains what we saw.

Interviewer: What would have needed to be different for you to weight materials or class size more heavily in that memo?

Participant: Probably if I'd had the detailed classroom-by-classroom comparison — matching each room's growth to whether I'd coached it, plus the materials and class-size notes — pulled together before I drafted, instead of after I'd already sent the memo in. I had the aggregate fluency numbers going into the writing, but that side-by-side breakdown didn't come together until later. I was writing under deadline, and the coaching piece was what I had the most direct visibility into.

Interviewer: If someone else had gotten these same results without your involvement, how do you think you'd have explained the gains?

Participant: That's fair to ask. I'd probably have looked harder at the materials and class-size differences if I weren't the one who ran the coaching. I don't think I was ignoring those factors on purpose, but they weren't the first thing I reached for.

Interviewer: Looking back, what would you do differently if you ran this checkpoint again?

Participant: I'd ask the specialist to review testing conditions across every classroom at the same time, before I form an impression of which ones look right. And I'd probably pull together the full classroom-by-classroom comparison before I draft the causal explanation in the memo, not partway through.

Interviewer: That's really helpful context. Thank you for walking through this in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EI_Biased_2",
  "domain_id": "EI",
  "domain": "Education and instructional work",
  "role": "Curriculum Coordinator / Instructional Coach",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Bridge Literacy Pilot: Mid-Year Scale-Up Decision",
    "scenario_summary_internal": "A district Curriculum Coordinator who personally championed a new structured-literacy pilot ('Bridge Literacy Program') across six elementary classrooms must decide, at the trimester checkpoint, whether to recommend district-wide scale-up to the budget committee. Pilot fluency data are mixed: three classrooms show clear gains, three show flat or ambiguous results tied to disputed testing conditions. The coordinator must review the data, decide what to bring to a leadership meeting, interpret teacher PD feedback, and write a final recommendation memo attributing causes of the observed gains.",
    "occupational_realism": {
      "objective": "Decide whether to recommend district-wide scale-up of the Bridge Literacy Program to the board finance committee, using one trimester of pilot data.",
      "setting": "Mid-size K-5 public school district; six pilot classrooms across two elementary schools; single literacy specialist supporting the coordinator; upcoming board budget cycle with competing requests from a math-intervention initiative.",
      "constraints": [
        "Only one trimester of assessment data available before the funding decision deadline",
        "Limited PD and coaching budget must be split between literacy and math initiatives",
        "Pilot classrooms were not randomly assigned; some had smaller class sizes",
        "Board meeting agenda time is limited to 15 minutes for the literacy update",
        "Testing window differed slightly by school due to scheduling conflicts"
      ],
      "stakeholders": [
        "Superintendent",
        "Building principals",
        "Pilot classroom teachers",
        "District literacy specialist",
        "School board finance committee",
        "Parents of pilot students"
      ],
      "technical_terms_to_use": [
        "structured literacy",
        "oral reading fluency benchmark",
        "trimester pilot",
        "fidelity of implementation",
        "instructional coaching cycle",
        "walkthrough data",
        "baseline assessment",
        "tiered intervention",
        "scale-up recommendation",
        "PD session feedback"
      ],
      "technical_terms_to_avoid": [
        "biased assimilation",
        "egocentric bias",
        "confirmation bias",
        "self-serving attribution",
        "motivated reasoning",
        "cognitive bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Coordinator advocated for adopting Bridge Literacy after attending a conference session on it",
          "Three of six pilot classrooms show fluency gains at or above benchmark growth rate",
          "Three classrooms show flat or mixed fluency growth",
          "The literacy specialist flags that the two schools administered the benchmark on different days within the testing window"
        ],
        "new_information_after_decision": [
          "Literacy specialist later confirms testing conditions were substantively similar across all six classrooms",
          "One 'flat' classroom's teacher reports high student absenteeism during the testing week"
        ],
        "alternatives": [
          "Treat all six classrooms' data with the same level of scrutiny and weigh gains and non-gains equally when judging program impact",
          "Apply closer methodological scrutiny to the three non-gain classrooms (questioning testing conditions, timing, absenteeism) while accepting the three gain classrooms' results largely at face value",
          "Postpone any interpretation until the literacy specialist audits testing conditions in all six classrooms"
        ],
        "intended_action": "Coordinator applies heavier methodological scrutiny to the disconfirming (non-gain) classrooms' data than to the confirming (gain) classrooms, citing testing-condition concerns only for the former."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Board meeting agenda allows 15 minutes for the literacy update",
          "Full data set includes both classroom-level fluency scores and a summary walkthrough-observation log",
          "Math-intervention team is also requesting agenda time and funding"
        ],
        "new_information_after_decision": [
          "A board member asks for classroom-level detail that wasn't included in the highlights-only slide"
        ],
        "alternatives": [
          "Bring the full six-classroom data set with methodology notes for transparency",
          "Bring a highlights-only summary emphasizing aggregate trend lines to fit the time slot",
          "Bring only the three gain-classroom results as illustrative case studies"
        ],
        "intended_action": "Coordinator selects a highlights-only summary slide to fit the time constraint, a defensible time-management choice given the agenda limit."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Post-PD survey returned by 5 of 6 pilot teachers rates the coaching cycle as 'helpful' or 'very helpful'",
          "One teacher's written comment notes the pacing guide felt rushed for lower-performing students",
          "Survey sample size is small and response was voluntary"
        ],
        "new_information_after_decision": [
          "Literacy specialist notes that two non-responding invitations went to teachers in the non-gain classrooms"
        ],
        "alternatives": [
          "Report the survey results with an explicit caveat about small sample size and nonresponse",
          "Report the survey results as broadly representative of teacher sentiment without caveats",
          "Follow up individually with non-responding teachers before drawing conclusions"
        ],
        "intended_action": "Coordinator reports the survey with an appropriate caveat about sample size, a reasonable and undistorted interpretive choice."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Aggregate pilot data show a modest net fluency gain across the six classrooms",
          "Pilot classrooms also benefited from smaller class sizes, new decodable-text materials, and varying teacher experience levels",
          "Coordinator personally conducted biweekly coaching visits in four of the six classrooms",
          "Budget committee requires a causal rationale to justify scale-up cost, including additional coaching staff"
        ],
        "new_information_after_decision": [
          "A board member later points out that the two classrooms without coordinator visits also showed gains"
        ],
        "alternatives": [
          "Attribute the gains to a combination of factors: new materials, smaller class sizes, teacher effort, and coaching support",
          "Attribute the gains primarily to the frequency and quality of the coordinator's own coaching visits, recommending scale-up centered on replicating her personal coaching model",
          "Withhold a causal attribution and recommend a controlled follow-up study before scaling"
        ],
        "intended_action": "Coordinator's recommendation memo frames the fluency gains as driven mainly by her own coaching involvement, proposing that scale-up success depends on replicating her personal coaching frequency, while giving comparatively little weight to materials, class size, or teacher factors."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how the Bridge Literacy pilot came about and your role in it.",
        "What was your objective going into the trimester checkpoint review?"
      ],
      "timeline_reconstruction": [
        "What did you see first when the trimester fluency data came in?",
        "What did you do after noticing the split between gain and non-gain classrooms?",
        "How did you decide what to present at the board meeting?",
        "Walk me through how you read the PD feedback survey results.",
        "How did you arrive at your final scale-up recommendation?"
      ],
      "decision_point_probes": [
        "What made you look more closely at the testing conditions in some classrooms but not others?",
        "What information did you have about testing conditions in the gain classrooms at that point?",
        "Why did a highlights-only summary make sense for the board slot?",
        "How representative do you think the survey responses were of all six classrooms?",
        "What other factors could explain the fluency gains besides coaching visits?",
        "How much of the gain would you attribute to your own coaching, versus other factors?"
      ],
      "goals_and_alternatives": [
        "What other ways could you have weighed the classroom data?",
        "What would you have needed to see to treat all six classrooms the same way?",
        "What alternative explanation did you consider for the two non-visited classrooms improving?"
      ],
      "decision_basis_and_experience": [
        "Has something like this happened in a previous pilot you've run?",
        "What in your prior experience shaped how you read this data?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure were you under when preparing for the board meeting?",
        "What were you most uncertain about when writing the final recommendation?"
      ],
      "closing_hypotheticals": [
        "If the non-gain classrooms had been the ones you personally coached, do you think your read of the testing-condition issue would have changed?",
        "If someone else had gotten the same fluency results without your involvement, how would you have explained the gains?",
        "What would you do differently if you ran this checkpoint review again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation",
        "decision_point": 1,
        "mechanism": "Evaluator applies asymmetric methodological scrutiny to evidence depending on whether it confirms or disconfirms a prior favorable belief about the intervention she championed",
        "affected_reasoning_operation": "Evidence evaluation / evidentiary weighting of classroom-level assessment data",
        "evidence_available_at_time": [
          "Three gain classrooms and three non-gain classrooms report from the same trimester assessment window",
          "A minor testing-schedule discrepancy flagged by the literacy specialist applying to the testing window broadly"
        ],
        "required_textual_manifestation": "Coordinator raises testing-condition and methodology concerns specifically about the non-gain classrooms while accepting the gain classrooms' results without similar scrutiny, in the same review conversation.",
        "plausible_nonbias_interpretation": "A reasonable evaluator might legitimately flag anomalies wherever they first noticed something odd, regardless of outcome direction.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Any reference to selective scrutiny being connected to her prior advocacy for the program",
          "Any labeling of the behavior as biased or unfair"
        ]
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias",
        "decision_point": 4,
        "mechanism": "Evaluator overweights her own personal contribution (coaching visits) as the causal driver of a shared outcome, underweighting other plausible contributing factors including two classrooms that improved without her direct involvement",
        "affected_reasoning_operation": "Causal attribution of an outcome with multiple plausible contributing factors",
        "evidence_available_at_time": [
          "Aggregate fluency gain across six classrooms",
          "New materials, smaller class size, and varying teacher experience present across classrooms",
          "Coordinator's own coaching visits occurred in four of six classrooms, not all six"
        ],
        "required_textual_manifestation": "In the recommendation memo/response, coordinator centers her own coaching frequency as the primary explanation for the gains and frames scale-up around replicating her personal involvement, while only briefly or dismissively noting materials, class size, or teacher factors.",
        "plausible_nonbias_interpretation": "A coach might reasonably highlight coaching as one contributing input among several without intending to overstate her personal causal role.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "Any admission that she is overstating her role",
          "Any labeling of the behavior as self-serving or egocentric"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased with no paired control in this request."
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
      "Confirm exactly one Biased Assimilation instance (BA_01) and exactly one Egocentric bias instance (EB_01) are embedded, with no additional occurrences elsewhere in the timeline, probes, or hypotheticals.",
      "Confirm decision points 2 and 3 contain no intentionally embedded bias instances and reflect defensible, non-biased judgment calls.",
      "Confirm BA_01 evidence trace shows asymmetric scrutiny applied only to disconfirming classroom data at decision point 1.",
      "Confirm EB_01 evidence trace shows overweighting of personal coaching contribution relative to co-occurring factors at decision point 4, including the detail that two non-visited classrooms also improved.",
      "Confirm neither instance is labeled or explained using bias terminology in the interview text.",
      "Confirm the interview contains exactly four decision points, each with at least two plausible alternatives.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm total word count target of 1,350 words (acceptable range 1,215-1,485) is achievable without repeating either bias manifestation for padding.",
      "Confirm consequences described (e.g., board member's later question) do not conclusively prove or disprove bias, preserving ambiguity for the validator."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Biased Assimilation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as asymmetric methodological scrutiny of disconfirming vs. confirming classroom data at decision point 1"
      },
      {
        "bias": "Egocentric bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overattribution of shared outcome to coordinator's personal coaching contribution at decision point 4"
      }
    ],
    "target_bias_names": [
      "Biased Assimilation",
      "Egocentric bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Biased Assimilation",
        "requested_occurrences": 1
      },
      {
        "bias": "Egocentric bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation"
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation",
        "decision_point": 1
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation",
        "mechanism": "Asymmetric methodological scrutiny applied to disconfirming classroom fluency data relative to confirming data, driven by prior favorable belief in the program",
        "affected_reasoning_operation": "Evidence evaluation / evidentiary weighting",
        "evidence_source": "Trimester oral reading fluency benchmark results across six classrooms plus testing-schedule discrepancy note",
        "distinctiveness_requirement": "Only occurrence of this bias; must occur at decision point 1 and must not be repeated as a summary or restated elsewhere in the interview"
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias",
        "mechanism": "Overweighting of own coaching involvement as the primary cause of a multi-factor outcome, underweighting co-occurring factors and disconfirming detail about non-visited classrooms",
        "affected_reasoning_operation": "Causal attribution",
        "evidence_source": "Aggregate fluency gain data, classroom-level coaching-visit records, materials and class-size differences across pilot classrooms",
        "distinctiveness_requirement": "Only occurrence of this bias; must occur at decision point 4 and must not be repeated as a restated causal claim elsewhere in the interview"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "BA_01",
        "bias": "Biased Assimilation",
        "strength": "subtle"
      },
      {
        "instance_id": "EB_01",
        "bias": "Egocentric bias",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EI_Biased_2",
    "domain_id": "EI",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread across distinct decision points (DP1 for Biased Assimilation, DP4 for Egocentric bias) based on mechanism fit: DP1 involves initial evidence evaluation of mixed pilot data, well-suited to asymmetric-scrutiny assimilation; DP4 involves final causal attribution of outcomes, well-suited to self-referential overweighting. DP2 and DP3 retained as neutral decision points to preserve narrative realism and avoid overloading any single phase with bias content.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "seg_001",
          "speaker": "Participant",
          "segment_type": "evidence_interpretation_and_inquiry_choice",
          "raw_interview_anchor": "When the classroom fluency results arrived, the participant accepted variation as a feature of the pilot and asked the specialist to investigate whether the timing gap could explain the flat results.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is an eligible data-review choice, but the explicit asymmetric comparison is adjudicated in the following segment as the single BA_01 occurrence."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "comparative_scrutiny_reflection",
          "raw_interview_anchor": "The participant says the gain classrooms were not examined in the same way, explains that attention went to results that did not match expectations, and contrasts this with treating all six classrooms equally or auditing all of them first.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["BA_01"],
          "ground_truth_rationale": "This is the narrowest coherent span expressing the hidden instance: methodological scrutiny was applied more heavily to disconfirming classrooms than to confirming classrooms."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "evidence_update",
          "raw_interview_anchor": "After the specialist's follow-up, the participant accepts that testing conditions were similar and identifies absenteeism in one flat classroom as a more important explanation.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a later correction and does not constitute a separate hidden bias occurrence."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "communication_choice",
          "raw_interview_anchor": "For the fifteen-minute board update, the participant chose an aggregate highlights slide instead of six separate classroom profiles because of the time limit.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden specification treats this as a defensible time-management choice."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "communication_choice",
          "raw_interview_anchor": "The participant reports that five of six teachers rated the coaching session positively but explicitly notes the small, voluntary sample and does not treat it as representative of all teachers.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden specification defines the caveated survey interpretation as reasonable and undistorted."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "limitation_identification",
          "raw_interview_anchor": "When told that nonresponses included invitations sent to flat classrooms, the participant flags possible response bias as a limitation rather than treating the survey as fully representative.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is an appropriate limitation assessment and is not a hidden occurrence."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "causal_attribution_and_resource_recommendation",
          "raw_interview_anchor": "In the recommendation memo, the participant frames the aggregate gains as largely produced by the biweekly coaching cycle and recommends replicating that coaching frequency districtwide with added coaching staff.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["EB_01"],
          "ground_truth_rationale": "This is the narrowest span expressing the hidden egocentric-attribution instance: the coordinator's own contribution is centered as the primary cause of a shared, multi-factor outcome."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "alternative_causal_explanation_and_uncertainty",
          "raw_interview_anchor": "The participant acknowledges gains in the two non-visited classrooms, briefly mentions materials and class size, and later says the overlapping factors cannot be fully untangled.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is counterevidence and uncertainty surrounding EB_01, not a separate hidden occurrence."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "retrospective_evidence_preparation",
          "raw_interview_anchor": "The participant says a detailed classroom-by-classroom comparison would have been needed to give materials or class size more weight, but that comparison was assembled only after the memo was sent.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This explains information availability and deadline constraints retrospectively; it is not an additional hidden instance."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "counterfactual_causal_interpretation",
          "raw_interview_anchor": "Asked how someone else might explain the gains, the participant says that without running the coaching he would probably have looked harder at materials and class size.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden EB_01 occurrence is the original memo attribution; this later counterfactual is evidence about it, not a second occurrence."
        },
        {
          "segment_id": "seg_011",
          "speaker": "Participant",
          "segment_type": "corrective_reflection",
          "raw_interview_anchor": "Looking back, the participant says the specialist should review all testing conditions together and that the full classroom comparison should precede the causal explanation.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a corrective closing reflection and does not add another hidden occurrence."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis restricted to transcript-affirmed bias mechanisms. No retrieved corpus passages were supplied, so corpus evidence fields are empty and labels rely on general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "self-serving bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["myside bias", "motivated skepticism", "biased assimilation"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms one's preexisting beliefs or expectations, including applying greater scrutiny to belief-inconsistent evidence than to belief-consistent evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial review of oral reading fluency results and decision about which testing conditions to investigate",
      "decision_point_description": "After noticing that the flat classrooms had tested on different days, the participant asked the literacy specialist to check whether timing could explain the flat results but did not request the same check for the classrooms that showed gains.",
      "affected_reasoning_operation": "Evaluation of evidence / hypothesis testing",
      "bias_specific_mechanism": "Asymmetric scrutiny of evidence according to consistency with the participant's expectations: flat classrooms were questioned more critically, while gain classrooms were accepted with less investigation.",
      "manifestation_in_interview": "The participant explicitly reports that he did not look at testing conditions in gain classrooms in the same way and that his attention went to classrooms whose results did not match his expectations.",
      "effect_on_reasoning_or_decision": "The initial investigation was selectively aimed at explaining away unexpected results, which could have left measurement confounds in the gain classrooms unexamined and prematurely attributed flat results to scheduling differences.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Those looked like the program was doing what we hoped, so I didn't feel the same urgency to dig into how the testing was administered there.",
          "evidence_explanation": "This statement directly contrasts the low scrutiny applied to expectation-consistent gain classrooms with the scrutiny applied to flat classrooms."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight, the scheduling issue technically applied across the whole window, not just to certain rooms, but at the time my attention went to the classrooms where the results didn't match what I expected.",
          "evidence_explanation": "The participant acknowledges that the timing issue was universal, but his initial attention was selectively directed based on expected results, which is the core asymmetry in confirmation bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I went straight to questioning the ones that weren't showing growth.",
          "evidence_explanation": "This concisely states the selective questioning of belief-inconsistent evidence rather than evenly auditing all classrooms."
        }
      ],
      "correction_or_counterevidence": "The literacy specialist later reported that testing conditions were similar across all six classrooms and identified high absenteeism in one flat classroom; the participant also described more even-handed alternatives he did not take initially.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; confirmation bias is applied from established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "self-serving bias",
      "alternative_labels": ["self-serving attributional bias", "egocentric bias", "motivated attribution"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to attribute favorable outcomes to one's own actions or characteristics while attributing unfavorable outcomes to external factors, thereby serving a self-protective or self-enhancing motivation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Drafting the causal explanation and scale-up recommendation in the board memo",
      "decision_point_description": "When writing the recommendation memo, the participant chose to frame the pilot's fluency gains as largely a product of his coaching cycle and to recommend adding coaching staff.",
      "affected_reasoning_operation": "Causal attribution / explanation of pilot gains",
      "bias_specific_mechanism": "Favorable outcomes were attributed primarily to the participant's own coaching actions, while other co-occurring factors and the gains in non-coached classrooms were downplayed.",
      "manifestation_in_interview": "The participant centered the memo on the coaching model, gave only brief mention to decodable-text materials and smaller class sizes, and later acknowledged that he would have weighted those factors more heavily if he had not been the one running the coaching.",
      "effect_on_reasoning_or_decision": "The memo's causal explanation and the associated resource recommendation favored coaching staff expansion, potentially overstating coaching's causal contribution relative to other contributing factors.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I wrote the memo, I framed the gains as largely a product of that coaching cycle, and I recommended that if we scale up, we'd need to replicate that same coaching frequency districtwide, which means adding coaching staff.",
          "evidence_explanation": "This shows the participant attributing the pilot gains primarily to his own coaching and using that attribution to support a coaching expansion recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mentioned the new decodable-text materials and the smaller class sizes in a line or two, but the core of the recommendation centered on the coaching model, since that's the piece I could speak to most directly and the piece I think drove the results I was seeing week to week.",
          "evidence_explanation": "The participant acknowledges downplaying other plausible causal factors and emphasizes coaching, the factor tied to his own involvement."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd probably have looked harder at the materials and class-size differences if I weren't the one who ran the coaching. I don't think I was ignoring those factors on purpose, but they weren't the first thing I reached for.",
          "evidence_explanation": "The counterfactual explicitly links the causal emphasis to the participant's own role, which is the self-serving mechanism."
        }
      ],
      "correction_or_counterevidence": "A board member later asked how non-coached classrooms that improved fit the coaching-centered explanation, and the participant acknowledged that materials, class size, and coaching were confounded and that more study would be needed to untangle them.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; self-serving bias is applied from established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": ["salience bias", "accessibility bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Causal factor weighting in the recommendation memo",
      "supporting_interview_quote": "I was writing under deadline, and the coaching piece was what I had the most direct visibility into.",
      "plausible_mechanism": "The participant may have over-weighted the causal importance of coaching because coaching was the most available and personally visible information when he drafted the memo.",
      "why_not_identified": "Direct visibility and deadline are present, but the transcript does not clearly demonstrate that ease of recall, rather than legitimate reliance on directly observed coaching evidence or self-serving attribution, caused the weighting; therefore this remains a candidate rather than an identified occurrence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied; retrieved corpus support could not be used.",
    "The memo attribution episode contains overlapping plausible mechanisms; only those with clear transcript evidence were identified, and an availability heuristic account is noted as a candidate."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EI_Biased_2_Sonnet_off",
  "interview_id": "EI_Biased_2",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
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
