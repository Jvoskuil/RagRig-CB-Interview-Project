You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time for this. Just to confirm, this is a voluntary debrief for our internal learning review, not a disciplinary process — anything you share helps us understand decision-making under uncertainty, not to assign blame. Can you start by telling me your role and what you were responsible for during this incident?

**Participant:** Sure. I'm the ground control specialist for the site — geotech engineer by training. I cover support design, monitoring interpretation, and sign-off on ground conditions for active headings. During this shift I was working from the surface office but on call for anything flagged at the 4200 development face and the adjacent bolted heading next to it.

**Interviewer:** Good. Before we get into specifics, can you give me a general account of what happened, start to finish?

**Participant:** It started with a call from the shift boss — minor rib spalling near the 4200 face, right after a blast, with a bit of dust puffing off the wall. Nobody was hurt, the crew paused on their own. Our extensometer near that face had been down for about two days — the bolting rig had knocked the cable loose — so I didn't have fresh convergence numbers for that specific spot. That gap mattered to me; I flagged it as something we'd need to close before I could really trust any read on that area. I also had the 3800 panel in the back of my mind — a similar-looking spalling event about six months earlier that we'd traced to aggressive undercutting by the operator at the time. But I didn't want to lean on that too hard, since one analogy from a different crew and a different round doesn't tell you much about stress conditions here. I authorized continued mucking with a visual check, treating both the operator-technique angle and the possibility of something geological as open questions.

A bit later the scaling crew called in bigger slabs than first described, plus a hairline fracture pattern we hadn't logged. We're roughly fifteen to twenty meters from a mapped fault splay there, though the exact position is fuzzy. I ran our convergence model using the nearest working stations, which weren't right at the face. It came back with a low displacement forecast, but the technician reminded me the model's calibration came from a different rock mass domain, so I didn't take the number at face value — I discounted it and tied continuing the round to a specific follow-up scaling check afterward.

After the round, spalling showed up in the adjacent bolted heading too. The shift boss asked about mesh and bolts before the next rotation, and the mine manager flagged the schedule hit. I treated the second location as new information rather than just an extension of what I already believed, so I ordered spot bolts at the fracture and a targeted scaling check instead of either a full upgrade or a full deferral. A couple hours later a crack opened along a bolt row. The technician wanted immediate evacuation. I authorized a restricted, technician-accompanied entry instead of routine access, since I didn't think the crack could just be read as more of the same. Not long after, we had a larger fall in that section. No one was hurt — an unrelated alarm cleared people out just before it happened — but it could have gone differently.

**Interviewer:** Let's reconstruct the timeline a bit more precisely. What exactly did you know at the moment of that first call?

**Participant:** Just the spalling, the dust, no injuries, crew stopped on their own. And that our monitoring near that face was blind because of the extensometer outage — that was very much on my mind, not something I set aside.

**Interviewer:** And after the scaling crew's second report?

**Participant:** That's when the picture got more complicated — bigger slabs, a fracture pattern, and the fault splay proximity became more relevant. It pushed me to actually run the model rather than rely on judgment alone.

**Interviewer:** When did you first pull up the convergence model output, and what did you do with it?

**Participant:** Right after that second report. I wanted a second line of evidence, but I went in already expecting to have to adjust for the domain mismatch.

**Interviewer:** Walk me through the gap between finishing the round and the evacuation call.

**Participant:** Round finished, spalling in the adjacent heading came up, I ordered the spot check rather than closing the question either way, then the crack appeared maybe two hours later, and the technician pushed for evacuation almost immediately after that.

**Interviewer:** Let's go through the first decision — authorizing continued mucking. What alternatives did you weigh?

**Participant:** Stopping everything for a full inspection, or restricting a buffer zone and resequencing the round. I went with the visual-check option, but I didn't treat it as a closed case.

**Interviewer:** How did you weigh the 3800 comparison against the missing extensometer data?

**Participant:** I tried to hold both at once. The 3800 case gave me one plausible read, but the missing monitoring meant I genuinely didn't know what the ground was doing locally, and I didn't want that gap to just disappear because I had a tidier story available. I made a point of telling the shift boss I wanted that extensometer back online as soon as the rig work allowed.

**Interviewer:** Second decision — using the convergence model output to justify finishing the round. How did you decide how much weight to give it?

**Participant:** Given the domain mismatch the technician flagged, I didn't treat the low-displacement number as decisive on its own — more as one data point that shifted my confidence somewhat, conditional on a scaling check afterward. If that check had come back worse, I'd have stopped regardless of what the model said.

**Interviewer:** What was the technician's concern, specifically, and how did you incorporate it?

**Participant:** She said the model's calibration came from a different rock mass domain and might not transfer well this close to the fault splay. I built that into how much I let the forecast move my decision — I leaned on it less than I would have on a panel where I trusted the calibration fit.

**Interviewer:** Third decision — the adjacent heading. What led you to the spot-check option rather than a full upgrade or a full deferral?

**Participant:** The new location mattered to me — it wasn't just the same spalling showing up again, it was a second area behaving in a way the earlier forecast hadn't covered. A full deferral felt like ignoring that; a full upgrade felt premature without more specific data on where the fracture actually was. The spot bolts and scaling check were a way to act on the new information without overcommitting either direction.

**Interviewer:** What would have changed that decision?

**Participant:** Fresh convergence readings right at that heading, or if the crack had shown up before I made the call instead of after.

**Interviewer:** Fourth decision — allowing entry after the crack appeared. What was your reasoning?

**Participant:** The model hadn't been rerun with the crack data, so I didn't extend the earlier forecast to cover it — that felt like a different question. I authorized a restricted entry with the technician present rather than routine access, treating the crack as something we still needed to understand rather than something already explained by what we'd seen at the face.

**Interviewer:** How much did time pressure factor into that specific call?

**Participant:** A fair amount. The next crew was due within the hour, and a full lockout would have meant a second schedule hit in one shift. That pressure was real, but it's why I restricted the entry rather than just clearing it outright.

**Interviewer:** Looking back, if the extensometer had been working the entire time, do you think your decisions would have gone differently?

**Participant:** Probably at the first and third points especially. Real numbers instead of partial analogies and adjusted model output would have given me something firmer to act on earlier.

**Interviewer:** And if the 3800 investigation had reached a different conclusion — say it had been traced to stress redistribution near a geological structure instead of operator technique — do you think you'd have read this situation differently?

**Participant:** Maybe somewhat, but I'd hope I'd still have tried to treat it as one data point rather than the deciding factor, given how different the local conditions were here.

**Interviewer:** Last one — what would you do differently if a similar sequence came in again?

**Participant:** Push even harder to get monitoring restored before any round decision, and probably formalize the follow-up conditions I attach to model output, rather than keeping them informal in my own head.

**Interviewer:** That's really helpful detail. Thanks for walking through it so openly.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Vocab_Control_2",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Geotechnical Engineer / Ground Control Specialist",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Roof Fall Precursor at the 4200 Panel Development Face (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A geotechnical engineer at an underground metal mine is called in after a contractor crew reports minor rib spalling and unusual dust puffing near a development face advancing toward a known fault splay. Over roughly 14 hours, the engineer works through the same four decisions as the paired biased scenario — continue mucking, use a convergence model to justify finishing the round, decide on supplemental support in an adjacent heading, and decide whether to permit entry after a crack appears — but at each point weighs the same evidence types (prior incident history, model track record, schedule pressure, monitoring gaps) in a balanced way, explicitly considering situational/geological explanations alongside crew-technique explanations and explicitly qualifying the convergence model's applicability. The incident still culminates in a contained roof fall in the adjacent bolted heading, but the participant's reasoning at no point relies on an unexamined dispositional attribution or unadjusted confidence in the model.",
    "occupational_realism": {
      "objective": "Determine whether the 4200 development face and adjacent bolted heading can continue safely under current ground behavior, or require support upgrades, re-sequencing, or evacuation, while maintaining the shift's advance schedule.",
      "setting": "Underground hard-rock mine, sublevel development heading approaching a mapped fault splay; mixed contractor and mine-employed crew; engineer works from a surface geotech office with intermittent underground inspection visits.",
      "constraints": [
        "Production schedule requires the 4200 face to advance a full round before shift change",
        "Fault splay location is only approximately known from exploration drilling, not fully delineated",
        "Convergence monitoring points near the face have gaps due to recent bolt installation disturbing extensometers",
        "Contractor crew reports are relayed through a shift boss, introducing communication lag",
        "A prior incident report the engineer authored six months earlier attributed a rib failure at a different panel primarily to an operator's aggressive undercutting rather than ground stress"
      ],
      "stakeholders": [
        "Geotechnical Engineer (interviewee)",
        "Shift Boss overseeing the 4200 crew",
        "Contractor drill-and-blast operator",
        "Mine Manager tracking weekly advance targets",
        "Ground control technician monitoring extensometers and convergence stations"
      ],
      "technical_terms_to_use": [
        "rib spalling",
        "convergence monitoring",
        "fault splay",
        "extensometer",
        "ground support density",
        "cut cycle",
        "stress redistribution",
        "scaling",
        "bolt pattern",
        "development face"
      ],
      "technical_terms_to_avoid": [
        "attribution bias",
        "illusion of validity",
        "cognitive bias",
        "heuristic",
        "confirmation",
        "overconfidence"
      ],
      "excluded_themes": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Shift boss reports minor rib spalling and a dust puff near the 4200 face after the last blast",
          "No injuries; crew paused work voluntarily",
          "Extensometer near the face has been offline for two days due to bolt rig interference",
          "Six months earlier, a similar-sounding rib spalling event at Panel 3800 was attributed in the engineer's report to an operator's aggressive undercutting technique"
        ],
        "new_information_after_decision": [
          "The engineer authorizes continued mucking and a visual-only inspection after weighing both the 3800 comparison and the missing local monitoring as open, unresolved factors",
          "Scaling crew finds slightly larger loose slabs than initially described"
        ],
        "alternatives": [
          "Halt all work at the face pending a full geotechnical inspection",
          "Allow mucking to continue with a visual-only check by the shift boss",
          "Restrict access to a buffer zone and reroute the round sequence"
        ],
        "intended_action": "Engineer authorizes continued mucking with a visual check, explicitly noting that the 3800 comparison is only a partial analogy, that the current operator's technique is one relevant but not dispositive factor, and that the missing extensometer data is a real gap that will need to be closed before further judgments are made."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Scaling crew reports larger-than-expected loose slabs and a hairline fracture pattern not previously logged",
          "Geological mapping shows the face is within 15-20 meters of the projected fault splay, with real position uncertain",
          "No updated convergence data is available due to the offline extensometer"
        ],
        "new_information_after_decision": [
          "The engineer runs the in-house convergence prediction model using nearby (but not adjacent) station data and treats the low-displacement forecast as one input among several, explicitly discounting it for the acknowledged domain mismatch",
          "The ground control technician's caveat about calibration domain is incorporated into a more conservative reading of the forecast, and the engineer sets a specific condition (a follow-up scaling check) before relying on it further"
        ],
        "alternatives": [
          "Delay the model output's use until a representative extensometer is reinstalled near the face",
          "Treat the fracture pattern as an independent red flag requiring a stop regardless of model output",
          "Rely on the convergence model's forecast, adjusted downward for domain mismatch, to justify proceeding with the round under a defined follow-up check"
        ],
        "intended_action": "Engineer uses the convergence model's forecast as a qualified, partial input, explicitly reduces confidence in it because of the acknowledged rock-mass domain mismatch, and pairs the decision to proceed with a concrete follow-up condition rather than treating the model output as sufficient on its own."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Round is completed; minor further spalling observed in the adjacent bolted heading, not just the development face",
          "Shift boss asks whether additional bolting or mesh should be ordered before the next crew rotation",
          "Mine Manager flags that ordering additional support will push the weekly advance behind target"
        ],
        "new_information_after_decision": [
          "Engineer defers a full support upgrade but orders a targeted scaling and spot-bolt check specifically because the second location of spalling is new information that was not covered by the earlier forecast",
          "A ground crack becomes visible along a bolt row in the adjacent heading two hours later"
        ],
        "alternatives": [
          "Order immediate supplemental bolting and mesh in the adjacent heading",
          "Defer additional support pending the next scheduled inspection",
          "Install spot bolts only at the fracture location while deferring full mesh and bolting"
        ],
        "intended_action": "Engineer treats the appearance of spalling in a second location as new evidence that revises, rather than merely extends, the earlier assessment, and responds with a scoped intermediate action (spot bolting and a scaling check) rather than either dismissing the new location or fully deferring based on the earlier forecast."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Visible crack has propagated along the bolt row; ground control technician requests immediate evacuation of the adjacent heading",
          "Model forecast has not been rerun with the new crack data because no new convergence readings exist",
          "Next crew is due to enter the heading within the hour"
        ],
        "new_information_after_decision": [
          "Engineer treats the new crack as a materially different signal from the earlier spalling, explicitly declines to extend the earlier forecast to cover it, and authorizes only a restricted, technician-accompanied inspection entry rather than routine access",
          "A larger roof fall occurs in the adjacent bolted section shortly after entry, though no injuries result because the crew evacuates in time following an unrelated alarm"
        ],
        "alternatives": [
          "Deny entry until convergence monitoring is restored and re-evaluated",
          "Allow a restricted, technician-accompanied inspection entry pending re-evaluation",
          "Require full re-support of the heading before any personnel access"
        ],
        "intended_action": "Engineer authorizes a restricted inspection entry while explicitly treating the crack as an open, unresolved question rather than as confirmation of the earlier benign account, balancing the technician's evacuation recommendation against the narrow inspection need."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first drew your attention to the 4200 face that shift?",
        "What was your role and what were you responsible for deciding at that point?"
      ],
      "timeline_reconstruction": [
        "What did you know at the moment the shift boss first called in the spalling report?",
        "What changed in your understanding after the scaling crew's second report?",
        "When did you first look at the convergence model output, and what did you do with it?",
        "Take me through the hours between the round completion and the final evacuation."
      ],
      "decision_point_probes": [
        "What alternatives did you consider before authorizing continued mucking after the first report?",
        "How did you weigh the 3800 comparison against the missing extensometer data?",
        "How did you decide how much weight to give the convergence model's forecast?",
        "What was the technician's concern about the model, and how did you incorporate it?",
        "What led you to order a spot check rather than either a full upgrade or a full deferral in the adjacent heading?",
        "What information would have changed your decision to allow entry after the crack appeared?"
      ],
      "prior_experience_probes": [
        "How did the 3800 panel incident shape how you read this situation?",
        "Have you used this convergence model in similar fault-proximal conditions before?"
      ],
      "uncertainty_and_time_pressure_probes": [
        "How much uncertainty did you feel about the fault splay's exact location, and how did that factor in?",
        "How much did the production schedule weigh on your decisions that shift?"
      ],
      "closing_hypotheticals": [
        "If the extensometer near the face had been working the whole time, would your decisions have changed?",
        "If the 3800 investigation had reached a different conclusion about its cause, do you think you'd have read the spalling differently?",
        "Looking back, what would you do differently if a similar sequence of reports came in again?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MU_Biased_2",
      "features_to_match": [
        "Underground hard-rock mining domain vocabulary (rib spalling, convergence monitoring, fault splay, extensometer, cut cycle, scaling, bolt pattern)",
        "Same setting, stakeholders, and role (geotechnical engineer / ground control specialist)",
        "Same four-decision-point structure and same chronological incident skeleton (initial spalling report, model-informed round completion, adjacent-heading support decision, crack/entry decision)",
        "Same emotional tone: measured, professionally reflective, mildly self-critical in hindsight",
        "Same difficulty level and same underlying uncertainty sources (offline extensometer, imprecise fault-splay location, model domain mismatch, schedule pressure)",
        "Same eventual outcome (contained roof fall with no injuries due to an unrelated alarm)",
        "Same probe categories and similar probe wording where possible"
      ],
      "features_to_remove_or_change": [
        "Remove the dispositional, analogy-driven causal attribution of the current spalling to operator technique at decision point 1; replace with explicit, balanced weighing of situational and dispositional explanations",
        "Remove the unadjusted confidence in the convergence model's forecast at decision point 2; replace with an explicit downward adjustment for the acknowledged domain mismatch and a defined follow-up condition",
        "Remove the carry-forward reuse of the operator-technique frame at decision point 3; replace with treatment of the second spalling location as revising evidence",
        "Remove the treatment of the crack as confirming prior benign surface behavior at decision point 4; replace with explicit treatment of the crack as an open, unresolved signal"
      ],
      "ambiguity_boundary": "Not applicable; this is a vocabulary_control condition designed to hold domain content constant while removing all intended bias mechanisms. Genuine occupational uncertainty (imprecise fault-splay location, monitoring gaps, model domain mismatch) is retained, but the participant's reasoning must not exhibit an unexamined dispositional attribution or unadjusted confidence in a validity source at any decision point."
    },
    "counterfactual_specification": {
      "causal_variable": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "counterfactual_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "NOT_APPLICABLE",
      "causal_test_question": "NOT_APPLICABLE"
    },
    "generation_checks": [
      "Confirm zero intended instances of Attribution Bias and zero intended instances of Illusion of validity are embedded anywhere in the interview",
      "Confirm domain vocabulary, setting, stakeholders, role, and four-decision-point structure match the paired biased scenario MU_Biased_2",
      "Confirm each decision point includes explicit, balanced consideration of at least two candidate explanations (dispositional/technique vs. situational/geological; model confidence vs. model limitation) rather than an unexamined default",
      "Confirm no bias terminology or psychological labels appear in probes or narrative",
      "Confirm four decision points each have at least two alternatives and pre/post decision information",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and probe density",
      "Confirm the final roof-fall outcome is retained without being used to prove or disprove the quality of any decision",
      "Confirm the participant's tone, difficulty level, and emotional register match the paired biased scenario as closely as vocabulary_control requires"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Attribution Bias",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended instances. Decision point 1 reasoning must explicitly balance dispositional (operator-technique) and situational (ground-stress) explanations rather than defaulting to either without examination."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 0,
        "mechanism_constraint": "Zero intended instances. Decision point 2 reasoning must explicitly discount the convergence model's forecast for the acknowledged domain mismatch and attach a concrete follow-up condition rather than treating the forecast as sufficient on its own."
      }
    ],
    "target_bias_names": ["Attribution Bias", "Illusion of validity"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Attribution Bias", "requested_occurrences": 0 },
      { "bias": "Illusion of validity", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "MU_Biased_2",
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "changed_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MU_Vocab_Control_2",
    "domain_id": "MU",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "No occurrences allocated. Vocabulary-control condition requires zero intended instances of both named biases at all four decision points; the paired biased scenario's decision-point structure, evidence types, and vocabulary are matched while the reasoning at each decision point is rewritten to explicitly weigh competing explanations and explicitly qualify model confidence, removing the mechanisms that would otherwise instantiate the target biases.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Underground hard-rock mining setting and role (geotechnical engineer / ground control specialist)",
      "Stakeholder set (shift boss, contractor operator, mine manager, ground control technician)",
      "Four-decision-point chronological structure and incident skeleton",
      "Production schedule pressure and its narrative placement",
      "Extensometer outage near the 4200 face",
      "Fault splay proximity and positional uncertainty",
      "Convergence model's domain mismatch as a known, acknowledged fact",
      "Prior 3800 incident as a referenced case with the same stated operator-undercutting cause",
      "Final roof fall outcome and the unrelated-alarm evacuation detail",
      "Probe categories and approximate probe density",
      "Target word count and difficulty level"
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
      "segment_id": "seg_001",
      "speaker": "Participant",
      "segment_type": "decision_rationale",
      "raw_interview_anchor": "I authorized continued mucking with a visual check, treating both the operator-technique angle and the possibility of something geological as open questions.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_002",
      "speaker": "Participant",
      "segment_type": "model_evidence_weighting",
      "raw_interview_anchor": "I discounted it and tied continuing the round to a specific follow-up scaling check afterward.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_003",
      "speaker": "Participant",
      "segment_type": "decision_rationale",
      "raw_interview_anchor": "I treated the second location as new information rather than just an extension of what I already believed.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_004",
      "speaker": "Participant",
      "segment_type": "access_decision_rationale",
      "raw_interview_anchor": "I authorized a restricted, technician-accompanied entry instead of routine access.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_005",
      "speaker": "Participant",
      "segment_type": "evidence_awareness",
      "raw_interview_anchor": "That gap mattered to me; I flagged it as something we'd need to close before I could really trust any read on that area.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_006",
      "speaker": "Participant",
      "segment_type": "method_selection_rationale",
      "raw_interview_anchor": "It pushed me to actually run the model rather than rely on judgment alone.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_007",
      "speaker": "Participant",
      "segment_type": "model_qualification",
      "raw_interview_anchor": "I wanted a second line of evidence, but I went in already expecting to have to adjust for the domain mismatch.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_008",
      "speaker": "Participant",
      "segment_type": "timeline_decision_reconstruction",
      "raw_interview_anchor": "I ordered the spot check rather than closing the question either way.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_009",
      "speaker": "Participant",
      "segment_type": "alternatives_considered",
      "raw_interview_anchor": "Stopping everything for a full inspection, or restricting a buffer zone and resequencing the round. I went with the visual-check option.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_010",
      "speaker": "Participant",
      "segment_type": "analogy_evidence_weighting",
      "raw_interview_anchor": "The 3800 case gave me one plausible read, but the missing monitoring meant I genuinely didn't know what the ground was doing locally.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_011",
      "speaker": "Participant",
      "segment_type": "model_decision_rationale",
      "raw_interview_anchor": "I didn't treat the low-displacement number as decisive on its own — more as one data point that shifted my confidence somewhat, conditional on a scaling check afterward.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_012",
      "speaker": "Participant",
      "segment_type": "model_limitation_integration",
      "raw_interview_anchor": "I built that into how much I let the forecast move my decision — I leaned on it less than I would have on a panel where I trusted the calibration fit.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_013",
      "speaker": "Participant",
      "segment_type": "support_decision_rationale",
      "raw_interview_anchor": "The spot bolts and scaling check were a way to act on the new information without overcommitting either direction.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_014",
      "speaker": "Participant",
      "segment_type": "decision_change_conditions",
      "raw_interview_anchor": "Fresh convergence readings right at that heading, or if the crack had shown up before I made the call.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_015",
      "speaker": "Participant",
      "segment_type": "crack_entry_rationale",
      "raw_interview_anchor": "I didn't extend the earlier forecast to cover it — that felt like a different question.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_016",
      "speaker": "Participant",
      "segment_type": "time_pressure_rationale",
      "raw_interview_anchor": "That pressure was real, but it's why I restricted the entry rather than just clearing it outright.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_017",
      "speaker": "Participant",
      "segment_type": "counterfactual_reflection",
      "raw_interview_anchor": "Real numbers instead of partial analogies and adjusted model output would have given me something firmer to act on earlier.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_018",
      "speaker": "Participant",
      "segment_type": "counterfactual_evidence_weighting",
      "raw_interview_anchor": "I'd still have tried to treat it as one data point rather than the deciding factor, given how different the local conditions were here.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
    },
    {
      "segment_id": "seg_019",
      "speaker": "Participant",
      "segment_type": "hindsight_improvement_rationale",
      "raw_interview_anchor": "Push even harder to get monitoring restored before any round decision, and probably formalize the follow-up conditions I attach to model output.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "Vocabulary-control hidden manifest specifies zero intended instances of Attribution Bias and Illusion of validity."
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
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Analyzed the full transcript for bias occurrences using a mechanism-first standard. No retrieved corpus passages were provided, so corpus-based labels were unavailable and candidate labels rely on general knowledge."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "availability heuristic",
        "alternative_labels": [
          "availability bias"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Initial authorization of continued mucking after minor spalling with missing extensometer data",
        "supporting_interview_quote": "I also had the 3800 panel in the back of my mind — a similar-looking spalling event about six months earlier that we'd traced to aggressive undercutting by the operator at the time. But I didn't want to lean on that too hard, since one analogy from a different crew and a different round doesn't tell you much about stress conditions here.",
        "plausible_mechanism": "A salient, easily recalled prior incident could have supplied a ready operator-technique hypothesis and influenced initial risk assessment despite the different geological and crew context.",
        "why_not_identified": "The participant explicitly acknowledged the analogy's limitations, stated he did not want to lean on it heavily, and kept geological and operator causes open; there is insufficient affirmative evidence that ease of recall materially biased the decision to authorize continued mucking."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "plan continuation bias",
        "alternative_labels": [
          "get-there-itis"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Decision after crack appeared to authorize restricted entry rather than immediate evacuation",
        "supporting_interview_quote": "A fair amount. The next crew was due within the hour, and a full lockout would have meant a second schedule hit in one shift. That pressure was real, but it's why I restricted the entry rather than just clearing it outright.",
        "plausible_mechanism": "Time pressure and commitment to the next crew schedule may have reduced willingness to fully halt access after a new crack, favoring a modified continuation of the plan even though a technician recommended evacuation.",
        "why_not_identified": "The participant did change the plan by ordering restricted, technician-accompanied entry rather than routine access, and the statement describes schedule pressure rather than a distinct irrational continuation mechanism; absent stronger evidence of biased risk discounting, time pressure alone is not enough to classify the decision as a bias occurrence."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No retrieved scientific-paper corpus was available for this analysis; candidate labels are supplied from general cognitive-science knowledge and are not corpus-supported.",
      "The analysis relies solely on the participant's self-report and cannot reconstruct contemporaneous operational data or risk calculations.",
      "Because the participant frequently articulated debiasing considerations, such as not over-relying on a prior analogy and treating new locations as new information, caution was used to avoid inferring bias from suboptimal outcomes or time pressure alone."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Vocab_Control_2_Sonar_off",
  "interview_id": "MU_Vocab_Control_2",
  "system_prompt_id": "Sonar",
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
