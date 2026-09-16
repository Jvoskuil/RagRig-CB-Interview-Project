You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal research-practice review, and I'll be asking you to walk me through a specific project in detail. You can skip anything you're not comfortable discussing. Can you start by telling me your role and how long you've been doing UX research here?

Participant: Sure. I'm a UX researcher on the productivity tools team, been here about four years. Most of my work is usability testing and discovery research feeding into our quarterly release cycles.

Interviewer: Great. I want to focus on the Smart Suggestions study. Can you walk me through how that project came about?

Participant: So Smart Suggestions is a recommendation feature — it watches what you're doing in the app and surfaces contextual actions. It came to me already pretty far along. Our VP had seen a competitor demo and decided we were building it. My brief wasn't "should we ship this," it was "help us ship it right." That framing came directly from him, almost word for word, in the kickoff.

Interviewer: How did that framing affect how you approached the study?

Participant: Honestly, it put me in a slightly defensive posture. The original plan I'd sketched was pretty lean — five moderated sessions, look at task completion and basic usability heuristics, done in a week. But hearing "this is happening regardless" made me not want to just rubber-stamp something. So before I even looked at the budget, I decided to add an unmoderated diary study on top of the moderated sessions, specifically to give people more room to surface friction over time, not just in a single session.

Interviewer: What did you know at that point that made you confident the expansion was the right call?

Participant: I had some prior data — a similar recommendation pattern we shipped in another product line got mixed reactions, so I knew these features aren't automatically loved. That backed up the diary study idea. But if I'm being fully honest, part of it was wanting to make sure the study had enough teeth that it couldn't just be waved through.

Interviewer: Did anyone push back on the expanded scope?

Participant: Research ops flagged that moderated sessions plus a diary cohort would eat most of our remaining budget. And engineering said the diary study would push the readout back a week. I considered just keeping the original five-session plan, and I also thought about pausing to renegotiate the study's purpose with the VP directly. In the end I went with the expanded version anyway.

Interviewer: Let's move to the discussion guide. What happened there?

Participant: Our PM shared a transcript from an earlier internal demo — a stakeholder said something like "this feels like it reads my mind." She sent it to me before I'd finalized the guide and said, "make sure the guide can capture moments like this." At that point my draft was pretty neutral — open prompts about task completion, satisfaction, that kind of thing.

Interviewer: What did you do with that transcript?

Participant: I went back through the guide and revised a couple of probes to more closely echo that framing — things like asking participants to describe moments where the suggestion "anticipated" what they needed. I thought I was just sharpening vague questions with a concrete example. Screener criteria were still being locked down around the same time, so there was a lot happening at once.

Interviewer: Did you consider leaving the original wording as-is?

Participant: Yeah, that was one option. Another was asking her to hold off sharing examples until after I'd locked the guide. I didn't do either. I finalized the revised version.

Interviewer: What happened once sessions started?

Participant: Two of the pilot participants used almost identical language to that transcript — "it's like it knows what I want." Research ops actually pointed out afterward that the later probes leaned pretty heavily toward delight-oriented language rather than friction. I hadn't really clocked that until she said it.

Interviewer: Let's talk about synthesis. What did the fuller pilot data look like?

Participant: Once we had ten moderated sessions plus the diary entries, it was mixed. Four sessions had real frustration — suggestions popping up mid-task, interrupting flow. Three were clearly positive. The diary entries kept circling back to timing as an issue.

Interviewer: How did you approach coding that?

Participant: This is where it got complicated. I'd given the steering committee an informal update about two weeks earlier — after just the first couple of sessions — saying early signs looked promising. So when the frustration cluster showed up, I coded it separately, as edge cases tied to atypical workflows, rather than merging it with the positive theme into one "mixed reception" finding.

Interviewer: What made atypical workflows the right explanation, in your view at the time?

Participant: Some of those users did have unusual task patterns — multi-window setups, non-standard shortcuts. So there was a real basis for it. But when a second researcher sat in on the affinity mapping and asked why we weren't just calling it "mixed reception" outright, I remember thinking that would be a harder story to tell after already saying things looked promising. That consideration was in my head when I made the call.

Interviewer: Was pausing for more sessions ever on the table?

Participant: Briefly. Engineering was also asking whether the timing complaints were serious enough to change the rollout configuration, and we didn't have time to run more sessions before the readout, so I moved forward with the edge-case framing.

Interviewer: Walk me through the final recommendation.

Participant: The synthesis doc described the feature as largely positive with a small caveat about timing. Engineering wanted one of three things: ship as-is, ship with a timing adjustment, or delay for redesign. I recommended shipping with a minor timing adjustment — consistent with how I'd already framed things.

Interviewer: How did the readout go?

Participant: The steering committee approved it, asked for a follow-up study post-launch. The VP thanked me for "confirming the direction was right all along." That phrase stuck with me a bit.

Interviewer: What information, if you'd had it earlier, might have changed any of these decisions?

Participant: If I'd had the full ten-session data set before I ever spoke informally to the committee, I might have described the early signal more cautiously. Not giving that update at all would have removed a constraint I was working around later.

Interviewer: If the product manager hadn't shared that transcript before you finalized the guide, do you think the probes would have looked different?

Participant: Probably. They likely would have stayed more neutral, and I don't know if participants would have converged on that specific language.

Interviewer: Looking back, is there anything about the process you'd reconsider?

Participant: I think I'd separate the informal updates from the analysis phase more strictly — maybe not report anything upward until coding was finalized. And I'd want a second pass on the guide before sharing any example transcripts, just to keep those inputs from bleeding into the wording. The frustration data was real; I just wonder now whether "edge case" was the cleanest read of it or the most convenient one at the time.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IS_Biased_3",
  "domain_id": "IS",
  "domain": "Information Systems, Human-Computer Interaction, and Interaction Design",
  "role": "UX Researcher",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Smart Suggestions Mandate: A Contested Usability Study",
    "scenario_summary_internal": "A UX Researcher at a mid-size software company is asked to validate a 'Smart Suggestions' recommendation feature that leadership has already decided to ship, ostensibly to gather supporting evidence rather than to test feasibility. The researcher must scope a mixed-methods study (moderated sessions, screener, diary study), design a discussion guide under influence from a product manager's framing example, synthesize pilot data that partially contradicts an earlier informal endorsement, and finally decide what to recommend to a steering committee. The narrative traces four sequential decisions from kickoff to final readout, embedding one instance each of reactance, priming effect, and cognitive dissonance without naming or explaining them.",
    "occupational_realism": {
      "objective": "Determine whether the mandated 'Smart Suggestions' feature is usable and beneficial enough to justify its planned rollout scope, and produce an evidence-based recommendation for the steering committee.",
      "setting": "Enterprise software company, UX research team embedded in a product organization, six-week research sprint ahead of a quarterly release train.",
      "constraints": [
        "Leadership has already approved the feature for release; the study's stated purpose is to inform rollout configuration, not go/no-go.",
        "Limited recruiting budget allows only 10 moderated sessions plus a small unmoderated diary cohort.",
        "Three-week timeline before the steering committee readout.",
        "Product manager wants findings to support a specific interaction pattern already prototyped.",
        "Researcher gave an informal positive update to the steering committee after an earlier exploratory session."
      ],
      "stakeholders": [
        "UX Researcher (participant of the interview)",
        "Product Manager for Smart Suggestions",
        "Engineering lead",
        "VP of Product (mandate source)",
        "Research operations coordinator",
        "Pilot cohort end users"
      ],
      "technical_terms_to_use": [
        "discussion guide",
        "screener",
        "moderated session",
        "unmoderated diary study",
        "think-aloud protocol",
        "affinity mapping",
        "thematic synthesis",
        "pilot cohort",
        "north-star metric",
        "steering committee readout",
        "rollout configuration",
        "usability heuristic"
      ],
      "technical_terms_to_avoid": [
        "reactance",
        "priming",
        "priming effect",
        "cognitive dissonance",
        "confirmation bias",
        "anchoring",
        "psychological bias",
        "cognitive bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "VP frames the Smart Suggestions feature as 'happening regardless' and says the study should 'make sure we ship it right.'",
          "Original research plan called for a lightweight 5-session moderated study.",
          "Researcher has prior data suggesting mixed reactions to similar recommendation UI patterns in another product line."
        ],
        "new_information_after_decision": [
          "Research ops flags that the expanded scope (moderated sessions plus a diary study) will consume most of the remaining budget.",
          "Engineering lead notes the extra diary study will delay the readout by one week."
        ],
        "alternatives": [
          "Keep the original lightweight 5-session moderated plan focused on usability of the current prototype.",
          "Expand scope to add an unmoderated diary study explicitly aimed at surfacing friction and negative reactions.",
          "Propose a short pause to renegotiate the study's purpose with the VP before proceeding."
        ],
        "intended_action": "Researcher expands the study scope to add the diary study, framing it internally as 'being thorough' in response to being told the outcome was predetermined."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Product manager shares a transcript excerpt from an earlier internal demo where a stakeholder reacted enthusiastically ('this feels like it reads my mind') and asks the researcher to 'make sure the guide can capture moments like this.'",
          "Draft discussion guide has neutral, open-ended prompts about task completion and satisfaction.",
          "Screener criteria are still being finalized."
        ],
        "new_information_after_decision": [
          "Two pilot participants use language nearly identical to the shared transcript when describing the feature.",
          "Research ops coordinator notes the guide's later probes lean toward eliciting delight-oriented language rather than friction."
        ],
        "alternatives": [
          "Finalize the discussion guide using only the original neutral, task-based prompts.",
          "Revise several probes to explicitly invite comparisons to the shared 'mind-reading' example.",
          "Ask the product manager not to share example reactions until after guide finalization."
        ],
        "intended_action": "Researcher revises specific probes to more closely echo the language and framing of the shared example transcript before finalizing the guide."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Researcher gave an informal update to the steering committee two weeks earlier stating early signs 'looked promising.'",
          "Pilot data now includes four sessions with clear frustration around unwanted suggestions interrupting workflow, alongside three sessions with positive reactions.",
          "Diary study entries show a recurring complaint about suggestion timing."
        ],
        "new_information_after_decision": [
          "Affinity mapping session with a second researcher flags that the frustration theme is being coded separately from the positive theme rather than merged into a single 'mixed reception' finding.",
          "Engineering lead asks whether the timing complaints are severe enough to change the rollout configuration."
        ],
        "alternatives": [
          "Code the frustration and positive reactions as a single, integrated 'mixed reception' theme reflecting the full pilot cohort.",
          "Treat the frustration sessions as isolated edge cases tied to atypical user workflows, preserving the earlier promising narrative.",
          "Pause synthesis and request additional pilot sessions to clarify the split before drawing conclusions."
        ],
        "intended_action": "Researcher characterizes the frustration sessions as edge cases attributable to unusual workflows, preserving consistency with the earlier informal 'promising' update to the steering committee."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Synthesis document frames the feature as largely positive with a small, edge-case caveat about suggestion timing.",
          "Steering committee readout is scheduled in two days.",
          "Engineering lead has asked for a clear recommendation: ship as-is, ship with timing adjustments, or delay for redesign."
        ],
        "new_information_after_decision": [
          "Steering committee approves shipping with a minor timing adjustment and asks for a follow-up study after launch.",
          "VP thanks the researcher for 'confirming the direction was right all along.'"
        ],
        "alternatives": [
          "Recommend shipping as-is with no configuration changes.",
          "Recommend shipping with a specific timing adjustment addressing the friction theme.",
          "Recommend a short delay to redesign the suggestion-timing logic before any rollout."
        ],
        "intended_action": "Researcher recommends shipping with a minor timing adjustment, consistent with the synthesis framing established in phase 3."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this research project came about?",
        "What was your understanding of the study's purpose when it was first assigned to you?"
      ],
      "timeline_reconstruction": [
        "What happened right after the VP described the feature as already decided?",
        "Walk me through how the discussion guide came together before the pilot sessions.",
        "What did the pilot data look like once sessions started coming in?",
        "How did you move from the synthesized findings to the final recommendation?"
      ],
      "decision_point_probes": [
        "What information did you have at the moment you decided to expand the study scope?",
        "What alternatives did you consider besides adding the diary study?",
        "When the product manager shared that transcript, how did it affect how you finalized the guide?",
        "What made you decide to revise those specific probes rather than leave the original wording?",
        "When you saw the frustration sessions, what made you categorize them the way you did?",
        "How did your earlier update to the steering committee factor into how you framed the findings?",
        "What ultimately tipped your final recommendation toward a timing adjustment rather than shipping as-is or delaying?"
      ],
      "cues": [
        "What specific words or reactions from participants or stakeholders stood out to you at each stage?"
      ],
      "information_sources": [
        "Which sources of information did you rely on most heavily at each decision point, and which did you set aside?"
      ],
      "goals": [
        "At each stage, whose goals were you trying to satisfy, and did that shift over time?"
      ],
      "alternatives": [
        "Looking back, what other paths could you have taken at each decision point?"
      ],
      "decision_basis": [
        "What ultimately justified each choice you made, in your own words?"
      ],
      "prior_experience": [
        "Did anything from past projects shape how you approached this one?"
      ],
      "time_pressure": [
        "How much did the timeline affect your choices at each stage?"
      ],
      "uncertainty": [
        "Where did you feel least certain about what the data was telling you?"
      ],
      "closing_hypotheticals": [
        "If the VP had never framed the feature as already decided, do you think your study scope would have looked different?",
        "If the product manager hadn't shared that transcript before the guide was finalized, would your probes have been worded differently?",
        "If you hadn't given that earlier 'promising' update to the steering committee, do you think you'd have coded the frustration sessions the same way?",
        "Looking back, is there anything about your final recommendation you'd reconsider?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Reactance",
        "decision_point": 1,
        "mechanism": "Being told the outcome (ship the feature) was non-negotiable triggers an assertive counter-response: the researcher unilaterally expands scope beyond what the research question requires, partly to reassert professional autonomy against the perceived restriction on the study's purpose.",
        "affected_reasoning_operation": "Scope-setting decision under a perceived constraint on research freedom",
        "evidence_available_at_time": [
          "VP's framing that the feature is 'happening regardless'",
          "Original lightweight 5-session plan already fit the research question",
          "Budget and timeline constraints flagged by research ops"
        ],
        "required_textual_manifestation": "Researcher explicitly links the scope expansion to the feeling of being told what the outcome should be, using language like 'wanted to make sure we weren't just rubber-stamping it' before naming budget/timeline tradeoffs.",
        "plausible_nonbias_interpretation": "A diary study is a legitimate methodological addition to capture longitudinal friction that moderated sessions alone might miss.",
        "strength": "subtle",
        "do_not_make_explicit": ["reactance", "psychological reactance", "asserting autonomy", "resisting mandate"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Priming effect",
        "decision_point": 2,
        "mechanism": "Exposure to the product manager's enthusiastic example transcript, presented immediately before guide finalization, shapes the wording and emphasis of subsequent probes toward eliciting similar delight-oriented language, independent of the guide's original neutral design intent.",
        "affected_reasoning_operation": "Instrument design / probe wording selection",
        "evidence_available_at_time": [
          "Shared transcript excerpt with specific 'mind-reading' phrasing",
          "Original neutral, task-based draft guide",
          "Research ops note about guide balance before finalization"
        ],
        "required_textual_manifestation": "Researcher describes revising 'a couple of probes' to more closely mirror the shared example's phrasing, and later notes participants used near-identical language, without recognizing the guide itself invited that language.",
        "plausible_nonbias_interpretation": "Incorporating a concrete example of positive engagement is a reasonable way to sharpen vague probes and ensure the guide can capture strong reactions if they occur.",
        "strength": "subtle",
        "do_not_make_explicit": ["priming", "priming effect", "anchoring on example", "unconscious influence"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Cognitive Dissonance",
        "decision_point": 3,
        "mechanism": "Having earlier publicly stated to the steering committee that results 'looked promising,' the researcher encounters contradicting frustration data and resolves the inconsistency by reinterpreting the negative sessions as atypical edge cases rather than integrating them into the overall finding, preserving consistency with the prior public commitment.",
        "affected_reasoning_operation": "Data synthesis and thematic categorization",
        "evidence_available_at_time": [
          "Four sessions showing clear frustration with suggestion timing",
          "Three sessions showing positive reactions",
          "Diary study entries repeating the timing complaint",
          "Researcher's own prior informal 'promising' statement to the steering committee"
        ],
        "required_textual_manifestation": "Researcher justifies separating frustration sessions as 'atypical workflows' specifically by referencing the need for the findings to line up with what was already told to the steering committee, rather than purely on data grounds.",
        "plausible_nonbias_interpretation": "Some usability studies do find that friction clusters around specific workflow types, making an edge-case categorization a legitimate analytical choice.",
        "strength": "subtle",
        "do_not_make_explicit": ["cognitive dissonance", "reducing dissonance", "rationalization", "consistency motive"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', not a control condition."
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
      "Exactly four decision points are present, each with at least two alternatives, prior facts, and post-decision information.",
      "Exactly one instance each of Reactance, Priming effect, and Cognitive Dissonance is embedded, at decision points 1, 2, and 3 respectively.",
      "Decision point 4 contains no new intended bias instance; it reflects downstream consequences only.",
      "No bias names, definitions, or explanations appear in probe wording or intended interview content.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and closing hypotheticals.",
      "Each occurrence has a distinct evidence trace, decision point, and plausible non-bias interpretation, satisfying the instance independence rule.",
      "Target length of 1,350 words (range 1,215-1,485) is achievable given four decision points with moderate probe depth and no repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Reactance",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as scope expansion in direct response to a mandate framed as non-negotiable, not as generic dislike of the feature."
      },
      {
        "bias": "Priming effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as instrument (discussion guide) wording shift following exposure to a specific example, prior to and independent of actual pilot data."
      },
      {
        "bias": "Cognitive Dissonance",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as reinterpretation of contradicting data specifically to preserve consistency with a prior public statement, not as generic optimism."
      }
    ],
    "target_bias_names": ["Reactance", "Priming effect", "Cognitive Dissonance"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Reactance", "requested_occurrences": 1},
      {"bias": "Priming effect", "requested_occurrences": 1},
      {"bias": "Cognitive Dissonance", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Reactance"},
      {"instance_id": "cb_02", "bias": "Priming effect"},
      {"instance_id": "cb_03", "bias": "Cognitive Dissonance"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Reactance", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Priming effect", "decision_point": 2},
      {"instance_id": "cb_03", "bias": "Cognitive Dissonance", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Reactance",
        "mechanism": "Scope expansion asserted in direct response to a mandate framed as removing the researcher's discretion over the study's purpose.",
        "affected_reasoning_operation": "Scope-setting under perceived constraint on research freedom",
        "evidence_source": "VP's mandate framing plus researcher's stated rationale for adding the diary study",
        "distinctiveness_requirement": "Must be tied explicitly to the mandate framing, not to methodological necessity alone."
      },
      {
        "instance_id": "cb_02",
        "bias": "Priming effect",
        "mechanism": "Guide-wording revision following exposure to a specific enthusiastic example transcript shared immediately before finalization.",
        "affected_reasoning_operation": "Instrument design / probe wording selection",
        "evidence_source": "Product manager's shared transcript and resulting probe revisions, plus later echoed participant language",
        "distinctiveness_requirement": "Must occur before pilot data collection and be traceable to the shared example, distinct from cb_03's data-synthesis-stage mechanism."
      },
      {
        "instance_id": "cb_03",
        "bias": "Cognitive Dissonance",
        "mechanism": "Reclassification of contradicting frustration data as 'edge cases' specifically to remain consistent with an earlier public 'promising' statement.",
        "affected_reasoning_operation": "Data synthesis and thematic categorization",
        "evidence_source": "Mixed pilot session data plus researcher's prior informal steering-committee update",
        "distinctiveness_requirement": "Must occur at data-synthesis stage and be motivated by consistency with a prior public commitment, distinct from cb_01's mandate-driven and cb_02's instrument-driven mechanisms."
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Reactance", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Priming effect", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Cognitive Dissonance", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IS_Biased_3",
    "domain_id": "IS",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Each bias assigned to a distinct decision point (1, 2, 3) based on mechanism fit and narrative realism: reactance at the mandate-driven scope decision, priming at the instrument-design decision, cognitive dissonance at the data-synthesis decision. Decision point 4 intentionally left free of new intended instances. No bias shares a decision point, so no sub-allocation of evidence sources within a single decision point was required.",
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
        {"segment_id":"seg_001","speaker":"Participant","segment_type":"scope-setting decision rationale","raw_interview_anchor":"The original plan I'd sketched was pretty lean ... made me not want to just rubber-stamp something ... I decided to add an unmoderated diary study.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["cb_01"],"ground_truth_rationale":"The participant links expanding the study beyond the original plan to the mandate that the outcome was predetermined and to resistance to rubber-stamping it."},
        {"segment_id":"seg_002","speaker":"Participant","segment_type":"methodological justification","raw_interview_anchor":"I had some prior data ... these features aren't automatically loved ... part of it was wanting to make sure the study had enough teeth.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This is a plausible methodological and professional-rigor rationale; it is not itself a hidden instance."},
        {"segment_id":"seg_003","speaker":"Participant","segment_type":"resource-tradeoff decision","raw_interview_anchor":"Research ops flagged ... engineering said ... I considered just keeping the original five-session plan ... In the end I went with the expanded version anyway.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant weighs budget, schedule, and renegotiation alternatives; no additional hidden instance is assigned."},
        {"segment_id":"seg_004","speaker":"Participant","segment_type":"instrument-design decision rationale","raw_interview_anchor":"I went back through the guide and revised a couple of probes to more closely echo that framing ... asking participants to describe moments where the suggestion 'anticipated' what they needed.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["cb_02"],"ground_truth_rationale":"The guide wording shifts toward the specific enthusiastic transcript example before pilot data is collected."},
        {"segment_id":"seg_005","speaker":"Participant","segment_type":"instrument-design alternatives","raw_interview_anchor":"Yeah, that was one option. Another was asking her to hold off sharing examples ... I didn't do either. I finalized the revised version.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This records alternatives considered and rejected, without a separate hidden instance."},
        {"segment_id":"seg_006","speaker":"Participant","segment_type":"post-pilot interpretation","raw_interview_anchor":"Research ops actually pointed out afterward that the later probes leaned pretty heavily toward delight-oriented language rather than friction. I hadn't really clocked that until she said it.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This is later recognition of an instrument effect, not a separate intended occurrence."},
        {"segment_id":"seg_007","speaker":"Participant","segment_type":"interim communication choice","raw_interview_anchor":"I'd given the steering committee an informal update ... after just the first couple of sessions ... saying early signs looked promising.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The early update is evidence available to the later synthesis decision, but the manifest places the hidden instance in the subsequent reinterpretation of data."},
        {"segment_id":"seg_008","speaker":"Participant","segment_type":"evidence-coding decision","raw_interview_anchor":"When the frustration cluster showed up, I coded it separately, as edge cases tied to atypical workflows, rather than merging it with the positive theme into one 'mixed reception' finding.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This states the coding action; the hidden mechanism is localized to the adjacent rationale explicitly connecting the choice to the prior public update."},
        {"segment_id":"seg_009","speaker":"Participant","segment_type":"evidence-interpretation rationale","raw_interview_anchor":"Some of those users did have unusual task patterns ... But ... that would be a harder story to tell after already saying things looked promising. That consideration was in my head when I made the call.","eligible_reasoning_segment":true,"ground_truth_bias_present":true,"ground_truth_instance_ids":["cb_03"],"ground_truth_rationale":"The participant explicitly says the prior promising statement influenced reclassification of contradictory frustration data as edge cases."},
        {"segment_id":"seg_010","speaker":"Participant","segment_type":"synthesis timing decision","raw_interview_anchor":"We didn't have time to run more sessions before the readout, so I moved forward with the edge-case framing.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"Time pressure explains continuing, but is not independently credited as a bias occurrence."},
        {"segment_id":"seg_011","speaker":"Participant","segment_type":"recommendation rationale","raw_interview_anchor":"The synthesis doc described the feature as largely positive ... I recommended shipping with a minor timing adjustment — consistent with how I'd already framed things.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This is a downstream recommendation reflecting the prior framing; phase 4 contains no new hidden instance."},
        {"segment_id":"seg_012","speaker":"Participant","segment_type":"counterfactual reflection","raw_interview_anchor":"If I'd had the full ten-session data set before I ever spoke informally to the committee, I might have described the early signal more cautiously.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This is hindsight counterfactual reasoning and is not independently credited."},
        {"segment_id":"seg_013","speaker":"Participant","segment_type":"counterfactual reflection","raw_interview_anchor":"They likely would have stayed more neutral, and I don't know if participants would have converged on that specific language.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"This supports the phase 2 causal reflection but is not a new occurrence."},
        {"segment_id":"seg_014","speaker":"Participant","segment_type":"process-reconsideration reflection","raw_interview_anchor":"I'd separate the informal updates from the analysis phase more strictly ... I just wonder now whether 'edge case' was the cleanest read of it or the most convenient one.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"Retrospective process improvement and uncertainty do not create an additional hidden instance."}
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
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analyzed the transcript for affirmative evidence of bias-specific mechanisms affecting reasoning, judgment, interpretation, or decisions. Only occurrences meeting the mechanism-first standard are reported."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring effect",
        "suggestive question wording"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "An initial piece of information serves as a reference point and disproportionately influences subsequent judgments, wording, or decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Revision of discussion-guide probes after receiving the PM's example transcript",
      "decision_point_description": "Choosing whether to incorporate language from an internal stakeholder transcript into probes that were originally neutral.",
      "affected_reasoning_operation": "Question wording and study-instrument design",
      "bias_specific_mechanism": "The stakeholder phrase 'reads my mind' functioned as a semantic anchor. The researcher adjusted later probes toward that specific delight/anticipation framing rather than preserving the original neutral, friction-oriented prompts.",
      "manifestation_in_interview": "The participant reports receiving a transcript in which a stakeholder said the feature 'reads my mind,' then revising neutral probes to ask about moments where suggestions 'anticipated' needs. Pilot participants later used almost identical language.",
      "effect_on_reasoning_or_decision": "The guide became oriented toward delight/anticipation language, likely shaping participant responses toward language consistent with the initial anchor and under-capturing friction during the pilot sessions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our PM shared a transcript from an earlier internal demo — a stakeholder said something like 'this feels like it reads my mind.' She sent it to me before I'd finalized the guide and said, 'make sure the guide can capture moments like this.'",
          "evidence_explanation": "Shows that a vivid stakeholder phrase entered the study-design process before the guide was finalized, providing the anchor for later question revisions."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I went back through the guide and revised a couple of probes to more closely echo that framing — things like asking participants to describe moments where the suggestion 'anticipated' what they needed.",
          "evidence_explanation": "Demonstrates the anchoring effect directly: the neutral guide language was adjusted toward the specific framing supplied by the initial transcript."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Two of the pilot participants used almost identical language to that transcript — 'it's like it knows what I want.'",
          "evidence_explanation": "Suggests the anchored guide language may have prompted convergent participant language rather than capturing spontaneously generated wording."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably. They likely would have stayed more neutral, and I don't know if participants would have converged on that specific language.",
          "evidence_explanation": "The participant retrospectively connects the example transcript to the change in guide wording and the observed convergence in participant language."
        }
      ],
      "correction_or_counterevidence": "Research ops later flagged that the later probes leaned heavily toward delight-oriented language rather than friction; the participant had not noticed this until the external flag, so the correction came after the guide had already been used.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context. The label 'anchoring bias' is assigned from established cognitive-science knowledge rather than retrieved sources.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "commitment and consistency bias",
        "motivated reasoning"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's prior beliefs, expectations, or commitments.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Synthesis coding of frustration clusters after an early positive update to the steering committee",
      "decision_point_description": "Deciding whether to code the frustration data as edge cases tied to atypical workflows or to merge it into a broader 'mixed reception' finding.",
      "affected_reasoning_operation": "Qualitative coding, thematic synthesis, and final recommendation framing",
      "bias_specific_mechanism": "The participant had already communicated an early positive signal to the steering committee. When later data were mixed, the frustration cluster was interpreted as a set of atypical-workflow edge cases rather than as evidence that reception was mixed. The participant states that the difficulty of telling a different story after the earlier update was considered when making this coding call.",
      "manifestation_in_interview": "The participant reports coding frustration separately as edge cases rather than merging it with positive themes into a mixed-reception finding. A second researcher directly asked why the data were not being called 'mixed reception.'",
      "effect_on_reasoning_or_decision": "The synthesis presented the feature as largely positive with only a small timing caveat, and the final recommendation to ship with a minor timing adjustment was consistent with this prior framing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd given the steering committee an informal update about two weeks earlier — after just the first couple of sessions — saying early signs looked promising. So when the frustration cluster showed up, I coded it separately, as edge cases tied to atypical workflows, rather than merging it with the positive theme into one 'mixed reception' finding.",
          "evidence_explanation": "Directly links the earlier positive update to the later interpretive choice to isolate rather than integrate the frustration data, a pattern consistent with confirmation bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But when a second researcher sat in on the affinity mapping and asked why we weren't just calling it 'mixed reception' outright, I remember thinking that would be a harder story to tell after already saying things looked promising. That consideration was in my head when I made the call.",
          "evidence_explanation": "Explicitly states that the earlier commitment influenced the coding decision, demonstrating the mechanism rather than merely describing the topic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The synthesis doc described the feature as largely positive with a small caveat about timing.",
          "evidence_explanation": "Shows the downstream effect of the interpretation: the mixed findings were shaped into a predominantly positive account."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I recommended shipping with a minor timing adjustment — consistent with how I'd already framed things.",
          "evidence_explanation": "Demonstrates that the final recommendation preserved the earlier positive framing rather than reflecting the mixed or timing-friction picture more fully."
        }
      ],
      "correction_or_counterevidence": "A second researcher challenged the edge-case coding by asking why the data were not being called 'mixed reception' outright. The participant also acknowledged that some users did have unusual task patterns, which provided a real basis for the edge-case coding, but this did not eliminate the stated consistency-based consideration.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context. The label 'confirmation bias' is assigned from established cognitive-science knowledge rather than retrieved sources.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "overconfidence bias",
      "alternative_labels": [
        "premature closure",
        "small-sample bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Early informal steering-committee update after only two sessions",
      "supporting_interview_quote": "I'd given the steering committee an informal update about two weeks earlier — after just the first couple of sessions — saying early signs looked promising.",
      "plausible_mechanism": "The participant may have treated a very small initial sample as sufficient for a directional early communication, which later constrained synthesis.",
      "why_not_identified": "There is insufficient affirmative evidence that the early update was overconfident rather than a tentative interim report. The later mixed results alone do not establish that the initial update was a biased judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided in the RAG context, so corpus_evidence arrays are empty and bias labels rely on general knowledge rather than retrieval.",
    "The analysis is based on participant self-report within a CTA interview, without independent coding of the original study materials or data."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Biased_3_Sonnet_off",
  "interview_id": "IS_Biased_3",
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
