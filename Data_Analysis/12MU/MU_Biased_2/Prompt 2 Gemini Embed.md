You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
**Interviewer:** Thanks for making time for this. Just to confirm, this is a voluntary debrief for our internal learning review, not a disciplinary process — anything you share helps us understand decision-making under uncertainty, not to assign blame. Can you start by telling me your role and what you were responsible for during this incident?

**Participant:** Sure. I'm the ground control specialist for the site — geotech engineer by training. I cover support design, monitoring interpretation, and sign-off on ground conditions for active headings. During this shift I was working from the surface office but on call for anything flagged at the 4200 development face and the adjacent bolted heading next to it.

**Interviewer:** Good. Before we get into specifics, can you give me a general account of what happened, start to finish?

**Participant:** It started with a call from the shift boss — minor rib spalling near the 4200 face, right after a blast, with a bit of dust puffing off the wall. Nobody was hurt, the crew actually paused on their own, which I give them credit for. Our extensometer near that face had been down for about two days — the bolting rig had knocked the cable loose — so I didn't have fresh convergence numbers for that specific spot. I authorized them to keep mucking with a visual check, because honestly this looked a lot like something we'd seen at the 3800 panel about six months back, where the cause turned out to be the operator undercutting too aggressively on the bottom of the round.

A bit later the scaling crew called in with bigger slabs than first described, plus a hairline fracture pattern we hadn't logged before. We're roughly fifteen to twenty meters from a mapped fault splay there, though the exact position is fuzzy — exploration drilling only gives you so much. I ran our convergence model using the nearest working stations, which weren't right at the face, and it came back with a low displacement forecast. That gave me enough to let the round finish.

After the round, spalling showed up in the adjacent bolted heading too. The shift boss asked if we should mesh and bolt before the next rotation, and the mine manager reminded me that would blow our weekly advance number. I held off. A couple hours later a crack opened along a bolt row in that heading. Technician wanted an immediate evacuation. I let a short monitored entry happen instead. Not long after, we had a larger fall in that section. No one was hurt — an unrelated alarm actually cleared people out just before it happened — but it could have gone differently.

**Interviewer:** Let's reconstruct the timeline a bit more precisely. What exactly did you know at the moment of that first call?

**Participant:** Just the spalling, the dust, no injuries, crew stopped on their own initiative. And that our monitoring near that face was blind because of the extensometer outage.

**Interviewer:** And after the scaling crew's second report?

**Participant:** That's when the picture got more complicated — bigger slabs, a fracture pattern, and the fault splay proximity became more relevant in my head.

**Interviewer:** When did you first pull up the convergence model output, and what did you do with it?

**Participant:** Right after that second report. I wanted something more than visual judgment before letting the round finish.

**Interviewer:** Walk me through the gap between finishing the round and the evacuation call.

**Participant:** Round finished, spalling in the adjacent heading came up, I deferred the support order, then the crack appeared maybe two hours later, and the technician pushed for evacuation almost immediately after that.

**Interviewer:** Let's go through the first decision — authorizing continued mucking. What alternatives did you weigh?

**Participant:** I could've stopped everything for a full inspection, or restricted a buffer zone and resequenced the round. I chose the visual-check option.

**Interviewer:** What made the 3800 comparison feel relevant enough to lean on here?

**Participant:** The symptoms looked similar — spalling right after a blast cycle. At 3800 we'd traced that to the operator undercutting on the bottom of the round, and once that case was in my head, my first read here was that we were probably looking at something similar — a shallow, crew-induced spall out of the cut or cleanup sequence, not necessarily anything structural. I didn't actually have anything from this round confirming that; it was more that the 3800 case gave me a ready-made explanation to reach for.

**Interviewer:** Did the missing extensometer data factor into that judgment?

**Participant:** Honestly, less than it should have. Once I'd settled on the crew-sequence explanation, the monitoring gap felt like a secondary concern rather than something that should have pushed me toward taking the geological angle more seriously.

**Interviewer:** Second decision — using the convergence model output to justify finishing the round. How did you decide it applied here?

**Participant:** That model's been solid for us — it called ground behavior accurately on a panel we ran last year. So when it came back low-displacement, I trusted that read.

**Interviewer:** The technician mentioned a calibration concern. Can you describe that?

**Participant:** She said the model was built on data from a different rock mass domain and might not transfer well this close to the fault splay. I heard her, but between the track record and the schedule pressure, I went with the output as it stood.

**Interviewer:** Third decision — deferring the supplemental support order. What was the basis?

**Participant:** The model's forecast was still sitting there as stable, so nothing had come in that reset the picture I already had. I treated it as the same authorization carrying forward from the face decision, rather than reopening the question, and the manager had flagged the schedule impact on top of that. I was planning to revisit support once we had updated readings from that heading.

**Interviewer:** What would have changed that decision?

**Participant:** Fresh convergence readings right at that heading, honestly. Or if the crack had shown up before I made the call instead of after.

**Interviewer:** Fourth decision — allowing the brief entry after the crack appeared. What was your reasoning?

**Participant:** I didn't have a fresh geotechnical read on the crack itself — nobody had run a new assessment specific to it — so I was essentially still operating inside the decision I'd made earlier in the shift. Given the timeline we were on, I opted for a short, monitored entry instead of a full lockout, treating it as a controlled check on an open question rather than something I'd already settled one way or the other.

**Interviewer:** How much did time pressure factor into that specific call?

**Participant:** A fair amount. The next crew was due within the hour, and stopping everything again would have meant a second schedule hit in one shift.

**Interviewer:** Looking back, if the extensometer had been working the entire time, do you think your decisions would have gone differently?

**Participant:** Probably, at least at the first and third points. Real numbers instead of an analogy might have shifted things earlier.

**Interviewer:** And if the 3800 investigation had reached a different conclusion at the time — say it had been traced to unanticipated stress redistribution near a geological structure instead of the operator's undercutting, with everything else about that case the same — do you think you'd have read this situation differently, given the same monitoring outage and schedule pressure you actually had?

**Participant:** Probably, yeah. If that case had taught me to expect a geological cause behind those symptoms, I think I'd have leaned harder on the fault-splay possibility from the first report, instead of defaulting to a crew-sequence explanation, even with the same blind spot on the extensometer and the same push to keep the round moving.

**Interviewer:** Last one — what would you do differently if a similar sequence came in again?

**Participant:** Push harder to get monitoring restored before trusting any model output, and probably treat a new fracture pattern as its own signal rather than folding it into a story that already made sense to me.

**Interviewer:** That's really helpful detail. Thanks for walking through it so openly.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Biased_2",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Geotechnical Engineer / Ground Control Specialist",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Roof Fall Precursor at the 4200 Panel Development Face",
    "scenario_summary_internal": "A geotechnical engineer at an underground metal mine is called in after a contractor crew reports minor rib spalling and unusual dust puffing near a development face that is advancing toward a known fault splay. Over roughly 14 hours, the engineer must decide whether to halt advance, reduce the cut cycle, order additional support, or clear the crew to continue, while balancing production targets, a previous incident he personally investigated (which he attributes largely to a specific junior operator's error rather than ground conditions), and an in-house convergence model he trusts because it performed well on a past, structurally different panel. The incident culminates in a larger, contained roof fall in an adjacent bolted section after the engineer clears the area based on the model's benign forecast, requiring the interview to probe how prior causal attributions and confidence in the model shaped four sequential decisions.",
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
          "The engineer authorizes continued mucking and a visual-only inspection rather than an immediate stop, reasoning that the current crew is more careful than the 3800 operator was",
          "Scaling crew finds slightly larger loose slabs than initially described"
        ],
        "alternatives": [
          "Halt all work at the face pending a full geotechnical inspection",
          "Allow mucking to continue with a visual-only check by the shift boss",
          "Restrict access to a buffer zone and reroute the round sequence"
        ],
        "intended_action": "Engineer authorizes continued mucking based partly on his belief that the current operator's careful technique makes ground-condition causes less likely, given his prior attribution of a similar event to operator error rather than geology."
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
          "The engineer runs the in-house convergence prediction model using nearby (but not adjacent) station data and interprets its low-displacement forecast as confirming stable ground",
          "The ground control technician notes verbally that the model was calibrated on a different rock mass domain but is overruled by the schedule pressure"
        ],
        "alternatives": [
          "Delay the model output's use until a representative extensometer is reinstalled near the face",
          "Treat the fracture pattern as an independent red flag requiring a stop regardless of model output",
          "Rely on the convergence model's forecast to justify proceeding with the round"
        ],
        "intended_action": "Engineer places high confidence in the convergence model's benign forecast and uses it to justify proceeding, because the model performed accurately during a past panel he considers analogous, without adjusting for the model's untested fit to the current fault-proximal domain."
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
          "Engineer defers additional support, citing the model's stable forecast and his assessment that the spalling pattern resembles the 3800 incident's operator-driven cause rather than a stress-related one",
          "A ground crack becomes visible along a bolt row in the adjacent heading two hours later"
        ],
        "alternatives": [
          "Order immediate supplemental bolting and mesh in the adjacent heading",
          "Defer additional support pending the next scheduled inspection",
          "Split the difference: install spot bolts only at the fracture location"
        ],
        "intended_action": "Engineer defers the supplemental support order, again attributing the spalling to crew technique rather than reconsidering the ground-stress explanation, and treating the model's earlier reassurance as sufficient basis for confidence."
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
          "Engineer clears personnel to enter for a brief inspection based on the model's last (unrevised) forecast, believing the crack is a surface phenomenon consistent with the earlier operator-driven interpretation",
          "A larger roof fall occurs in the adjacent bolted section shortly after entry, though no injuries result because the crew evacuates in time following an unrelated alarm"
        ],
        "alternatives": [
          "Deny entry until convergence monitoring is restored and re-evaluated",
          "Allow a brief, monitored inspection entry as the engineer decided",
          "Require full re-support of the heading before any personnel access"
        ],
        "intended_action": "Engineer authorizes entry based on continued trust in the outdated model output and a persistent framing of the spalling as behavior-driven, setting up the final incident without directly proving the reasoning was flawed."
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
        "What made you confident the spalling pattern was similar to the 3800 incident?",
        "How did you decide the convergence model's forecast was applicable to this location?",
        "What was the technician's concern about the model, and how did you weigh it?",
        "What led you to defer the supplemental support order in the adjacent heading?",
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
        "If the 3800 incident had never happened, do you think you would have read the spalling differently?",
        "Looking back, what would you do differently if a similar sequence of reports came in again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "decision_point": 1,
        "mechanism": "Engineer attributes the cause of the current spalling event to operator technique/behavior (dispositional cause), by analogy to a past incident he personally attributed to operator error, rather than attributing it to situational/geological factors (stress redistribution near the fault splay) despite comparable surface cues.",
        "affected_reasoning_operation": "Causal attribution of an observed anomaly (rib spalling, dust puff) under incomplete evidence",
        "evidence_available_at_time": [
          "Minor rib spalling and dust puff reported by shift boss",
          "Extensometer offline, no ground-stress data available",
          "Engineer's own prior report attributing a similar-sounding event to operator's aggressive undercutting"
        ],
        "required_textual_manifestation": "In answering why he allowed mucking to continue, the engineer explicitly reasons that the current operator's more careful technique makes the spalling less concerning, drawing a direct comparison to the 3800 operator he blamed previously, without weighing the missing ground-stress data as an alternative cause.",
        "plausible_nonbias_interpretation": "A reasonable engineer might legitimately consider operator technique as one relevant factor among several, especially if the current operator has a known careful track record.",
        "strength": "subtle",
        "do_not_make_explicit": ["attribution bias", "dispositional", "situational", "bias"]
      },
      {
        "instance_id": "iov_01",
        "bias": "Illusion of validity",
        "decision_point": 2,
        "mechanism": "Engineer expresses high confidence in the convergence model's benign forecast based on its past accuracy on a structurally different panel, treating internal consistency of the model's output (and his fluency in reading it) as a signal of predictive validity, without accounting for the model's poor fit to the current fault-proximal, data-sparse domain.",
        "affected_reasoning_operation": "Confidence calibration when interpreting a quantitative forecast under known model-domain mismatch",
        "evidence_available_at_time": [
          "Convergence model output showing low predicted displacement using non-adjacent station data",
          "Ground control technician's verbal caveat that the model was calibrated on a different rock mass domain",
          "Model's strong track record on a past, structurally different panel"
        ],
        "required_textual_manifestation": "The engineer describes trusting the model's forecast strongly enough to justify proceeding, citing its past reliability, while the technician's domain-mismatch caveat is acknowledged but not treated as reducing his confidence in the current prediction.",
        "plausible_nonbias_interpretation": "Relying on a validated in-house model with a track record could be a reasonable engineering judgment call under time pressure and data scarcity.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "overconfidence", "calibration", "bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control specified in this generation cycle."
    },
    "counterfactual_specification": {
      "causal_variable": "Whether the engineer's prior 3800 incident report attributed the earlier failure to operator error versus ground stress",
      "original_state": "Engineer's prior report attributed the 3800 rib failure primarily to operator's aggressive undercutting technique",
      "counterfactual_state": "Engineer's prior report attributed the 3800 rib failure primarily to unanticipated stress redistribution near a geological structure",
      "variables_to_hold_constant": [
        "Production schedule pressure",
        "Extensometer outage near the 4200 face",
        "Convergence model's domain mismatch",
        "Sequence and content of the four decision points",
        "Scaling crew and technician reports",
        "Final roof fall outcome"
      ],
      "expected_causal_difference": "With a situational prior attribution, the engineer would more readily treat the current spalling as a possible ground-stress signal, likely triggering earlier support upgrades or evacuation rather than deferral.",
      "causal_test_question": "Does changing the causal framing of the engineer's prior incident report (operator error vs. ground stress) alter his interpretation of the current spalling and his willingness to trust the convergence model?"
    },
    "generation_checks": [
      "Confirm exactly one Attribution Bias instance and one Illusion of validity instance are embedded, each at a distinct decision point",
      "Confirm no bias terminology or psychological labels appear in probes or narrative",
      "Confirm four decision points each have at least two alternatives and pre/post decision information",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points and probe density",
      "Confirm consequences (final roof fall) do not explicitly confirm or deny whether reasoning was biased",
      "Confirm plausible non-bias explanations exist for both embedded instances"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Attribution Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as dispositional (operator-technique) causal attribution of current spalling, anchored to a prior analogous incident attribution, over situational (ground-stress) attribution, at decision point 1 only."
      },
      {
        "bias": "Illusion of validity",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as overconfidence in the convergence model's forecast based on past track record, despite acknowledged domain mismatch, at decision point 2 only."
      }
    ],
    "target_bias_names": ["Attribution Bias", "Illusion of validity"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Attribution Bias", "requested_occurrences": 1 },
      { "bias": "Illusion of validity", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "attr_01", "bias": "Attribution Bias" },
      { "instance_id": "iov_01", "bias": "Illusion of validity" }
    ],
    "intended_decision_points": [
      { "instance_id": "attr_01", "bias": "Attribution Bias", "decision_point": 1 },
      { "instance_id": "iov_01", "bias": "Illusion of validity", "decision_point": 2 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "attr_01",
        "bias": "Attribution Bias",
        "mechanism": "Dispositional (operator-error) causal attribution of ambiguous ground behavior, anchored to a prior analogous case the engineer personally attributed to operator error, over situational (geological) attribution",
        "affected_reasoning_operation": "Causal attribution under incomplete evidence at the point of authorizing continued mucking",
        "evidence_source": "Shift boss's spalling/dust report combined with the engineer's own prior 3800 incident report",
        "distinctiveness_requirement": "Must be the only instance of dispositional-over-situational causal misattribution in the interview; must occur at decision point 1 and not be repeated in later decision points, probes, or the closing hypotheticals as a separate instance."
      },
      {
        "instance_id": "iov_01",
        "bias": "Illusion of validity",
        "mechanism": "Confidence in a predictive model's output derived from its past track record and internal coherence, unadjusted for an acknowledged domain mismatch (different rock mass calibration) and sparse current data",
        "affected_reasoning_operation": "Confidence calibration when interpreting the convergence model's forecast at decision point 2",
        "evidence_source": "Convergence model output using non-adjacent station data, plus technician's verbal domain-mismatch caveat",
        "distinctiveness_requirement": "Must be the only instance of unwarranted forecast confidence in the interview; occurs at decision point 2; later reliance on the same stale model output at decision points 3 and 4 must be narrated as a consequence of this single occurrence, not as additional independent instances."
      }
    ],
    "intended_strength": [
      { "instance_id": "attr_01", "bias": "Attribution Bias", "strength": "subtle" },
      { "instance_id": "iov_01", "bias": "Illusion of validity", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Causal framing of the engineer's prior 3800 incident attribution (operator error vs. ground stress)",
      "original_state": "Attributed to operator's aggressive undercutting technique",
      "changed_state": "Attributed to unanticipated stress redistribution near a geological structure",
      "variables_to_hold_constant": [
        "Production schedule pressure",
        "Extensometer outage near the 4200 face",
        "Convergence model's domain mismatch",
        "Sequence and content of the four decision points",
        "Scaling crew and technician reports",
        "Final roof fall outcome"
      ]
    },
    "scenario_id": "MU_Biased_2",
    "domain_id": "MU",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias assigned to a distinct decision point (attribution bias at decision point 1, illusion of validity at decision point 2) based on mechanism fit: attribution bias fits the earliest causal-interpretation moment, illusion of validity fits the model-reliance moment; subsequent decision points (3 and 4) narrate downstream consequences of these same two instances without introducing new independent instances.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Production schedule pressure",
      "Extensometer outage near the 4200 face",
      "Convergence model's domain mismatch",
      "Sequence and content of the four decision points",
      "Scaling crew and technician reports",
      "Final roof fall outcome"
    ],
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
    "analysis_scope_note": "Single-interview CTA-style debrief evaluated for affirmative cognitive bias occurrences. Retrieved passages were used only for labels, definitions, and mechanism support."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Automation complacency",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring and adjustment",
      "alternative_labels": ["Anchoring bias", "Insufficient adjustment"],
      "taxonomy_status": "established_label",
      "bias_definition": "A judgmental heuristic in which an initial value, prior case, or first impression serves as an anchor, and subsequent adjustments away from that anchor are insufficient when new information arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial authorization of continued mucking after first spalling report",
      "decision_point_description": "Whether to stop work for a full inspection/buffer zone or allow continued mucking with visual checks after rib spalling and dust were reported at the 4200 face.",
      "affected_reasoning_operation": "Causal hypothesis generation and initial risk classification",
      "bias_specific_mechanism": "The participant anchored on the salient 3800 panel case as a ready-made causal template for shallow, crew-induced spalling and adjusted insufficiently for the current absence of face-level extensometer data and the absence of current-round confirmation.",
      "manifestation_in_interview": "The participant explicitly described the 3800 case as providing a ready-made explanation and acknowledged that the monitoring gap became secondary once the crew-sequence explanation was adopted.",
      "effect_on_reasoning_or_decision": "It produced a low-risk initial interpretation, leading to continued mucking with only visual checks and reducing early consideration of a structural or geological cause.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I authorized them to keep mucking with a visual check, because honestly this looked a lot like something we'd seen at the 3800 panel about six months back, where the cause turned out to be the operator undercutting too aggressively on the bottom of the round.",
          "evidence_explanation": "Shows the use of a prior similar case as the initial explanation for the current symptoms."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "once that case was in my head, my first read here was that we were probably looking at something similar — a shallow, crew-induced spall out of the cut or cleanup sequence, not necessarily anything structural. I didn't actually have anything from this round confirming that; it was more that the 3800 case gave me a ready-made explanation to reach for.",
          "evidence_explanation": "Directly demonstrates anchoring on the prior case without current-round verification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once I'd settled on the crew-sequence explanation, the monitoring gap felt like a secondary concern rather than something that should have pushed me toward taking the geological angle more seriously.",
          "evidence_explanation": "Shows insufficient adjustment away from the anchor despite a missing data source that should have increased uncertainty."
        }
      ],
      "correction_or_counterevidence": "No real-time correction occurred. In hindsight, the participant stated that a working extensometer and a different 3800 case conclusion likely would have changed the first and third decisions.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved space-flight verification/validation passage defines anchoring and adjustment as initial values dominating later estimates with typically insufficient adjustment, supporting the general mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive Bias in the Verification and Validation of Space Flight Systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.” [16]",
          "mechanism_supported_by_source": "Describes anchoring and adjustment as an initial-answer-based heuristic with typically insufficient subsequent adjustment.",
          "relevance_to_this_occurrence": "Supports the classification of the participant's use of the 3800 case as an initial anchor from which he adjusted insufficiently when the monitoring gap and later geological cues emerged."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Automation complacency",
      "alternative_labels": ["Complacency in automation use", "Automation overtrust"],
      "taxonomy_status": "established_label",
      "bias_definition": "A failure to adequately monitor or verify an automated aid's output because of trust in its reliability or prior performance, resulting in acceptance of the aid's recommendation without sampling sufficient independent information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Use of convergence model output to allow round completion after second scaling report",
      "decision_point_description": "Whether the low-displacement convergence model forecast justified finishing the round despite larger slabs, a new fracture pattern, and concerns about model transferability near the fault splay.",
      "affected_reasoning_operation": "Interpretation and weighting of automated model output versus contradictory monitoring/calibration evidence",
      "bias_specific_mechanism": "The participant accepted the model's low-displacement forecast based on its prior track record and did not sufficiently verify or adjust for the model's known domain mismatch and lack of face-level data; the technician's calibration concern was heard but not acted upon.",
      "manifestation_in_interview": "The participant stated he trusted the model read because the model had been solid before, and after the technician raised the domain-mismatch concern he still went with the output as it stood.",
      "effect_on_reasoning_or_decision": "The model output was treated as sufficient evidence to finish the round, preventing more stringent investigation or support action at that decision point.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I ran our convergence model using the nearest working stations, which weren't right at the face, and it came back with a low displacement forecast. That gave me enough to let the round finish.",
          "evidence_explanation": "Shows that the model output from non-face-level stations was accepted as sufficient despite the absence of direct monitoring data at the face."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That model's been solid for us — it called ground behavior accurately on a panel we ran last year. So when it came back low-displacement, I trusted that read.",
          "evidence_explanation": "Demonstrates trust based on past automation performance rather than verification of current applicability."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She said the model was built on data from a different rock mass domain and might not transfer well this close to the fault splay. I heard her, but between the track record and the schedule pressure, I went with the output as it stood.",
          "evidence_explanation": "Shows a specific warning about the model's validity was received but not used to verify or reject the automated recommendation."
        }
      ],
      "correction_or_counterevidence": "Schedule pressure was also present, but the bias-specific mechanism is the inadequate verification of the model's applicability despite a specific contradiction. No immediate correction occurred before the fall.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The Parasuraman and Manzey passage provides the core operational definition of complacency as sampling less information than necessary to verify an automated aid's recommendation.",
      "corpus_evidence": [
        {
          "source_identifier": "parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf",
          "paper_title": "Complacency and Bias in Human Use of Automation: An Attentional Integration",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "According to this logic, any participant who accessed just the information appropriate to verify a given diagnosis before accepting it was regarded as showing noncomplacent (eutactic) behavior in interaction with the aid. However, participants sampling less information than that necessary to completely verify the aid’s recommendation were",
          "mechanism_supported_by_source": "Defines complacency as failing to sample enough independent information to verify an automated aid's recommendation.",
          "relevance_to_this_occurrence": "The participant accepted the convergence model's low-displacement output without independently verifying its applicability to the fault-splay zone, despite a specific calibration concern."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Plan continuation bias",
      "alternative_labels": ["Plan continuation", "Get-there-itis", "Continuation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to continue with an original plan or course of action despite evidence that conditions have changed or risk has increased, often under schedule or goal pressure.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deferral of supplemental support and monitored entry after adjacent heading spalling and crack",
      "decision_point_description": "Whether to stop and install mesh/bolt support before the next rotation, and later whether to evacuate immediately or permit a short monitored entry after a crack opened along a bolt row.",
      "affected_reasoning_operation": "Risk reassessment and course-of-action revision in response to escalating hazard indicators",
      "bias_specific_mechanism": "The participant treated the existing stability model and prior authorization as continuing rather than reopening the decision when new spalling and a crack appeared; schedule impact and the goal of preserving advance reinforced continuation of the original plan despite accumulating disconfirming ground behavior.",
      "manifestation_in_interview": "He held off on support after adjacent heading spalling; after the crack, he framed the entry as still operating inside the earlier decision and cited timeline pressure.",
      "effect_on_reasoning_or_decision": "Delayed supplemental support and allowed a monitored entry instead of full evacuation or lockout, increasing exposure before the larger fall.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "After the round, spalling showed up in the adjacent bolted heading too. The shift boss asked if we should mesh and bolt before the next rotation, and the mine manager reminded me that would blow our weekly advance number. I held off.",
          "evidence_explanation": "Shows continuation of the original plan at the first new warning following the round."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The model's forecast was still sitting there as stable, so nothing had come in that reset the picture I already had. I treated it as the same authorization carrying forward from the face decision, rather than reopening the question, and the manager had flagged the schedule impact on top of that.",
          "evidence_explanation": "Demonstrates staying with the prior authorization rather than conducting a fresh risk evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have a fresh geotechnical read on the crack itself — nobody had run a new assessment specific to it — so I was essentially still operating inside the decision I'd made earlier in the shift. Given the timeline we were on, I opted for a short, monitored entry instead of a full lockout, treating it as a controlled check on an open question rather than something I'd already settled one way or the other.",
          "evidence_explanation": "Shows continued adherence to the earlier plan even after a crack appeared and without a new assessment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A fair amount. The next crew was due within the hour, and stopping everything again would have meant a second schedule hit in one shift.",
          "evidence_explanation": "Confirms schedule/goal pressure was a reinforcing factor in continuing the plan."
        }
      ],
      "correction_or_counterevidence": "External schedule pressure from the manager could explain part of the decision, but the participant's own framing shows cognitive continuation of the prior authorization rather than a fresh risk assessment. The fall occurred after an unrelated alarm cleared people out.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved cockpit-cognition paper names plan continuation as a cognitive bias found in operational incidents; it does not provide a detailed mechanistic definition, but the label fits the same continuing-with-plan pattern.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "paper_title": "Cognitive bias in the cockpit: A deadly false sense of normality",
          "authors": "Sam O'Connor",
          "publication_year": null,
          "retrieved_passage_or_finding": "Finally, it was found that the cognitive bias plan continua runway excursions were the most common outcome.",
          "mechanism_supported_by_source": "Names plan continuation bias as a cognitive bias associated with continuing an operational plan despite changing conditions.",
          "relevance_to_this_occurrence": "Supports using the label for the participant's continuation of the original shift plan after new hazard indicators; the source is aviation-specific but describes a structurally similar operational pattern."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Confirmation bias",
      "alternative_labels": ["Biased assimilation", "Case-building"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Interpretation of later fracture pattern, adjacent heading spalling, and crack",
      "supporting_interview_quote": "Push harder to get monitoring restored before trusting any model output, and probably treat a new fracture pattern as its own signal rather than folding it into a story that already made sense to me.",
      "plausible_mechanism": "New information may have been selectively interpreted as consistent with the existing low-risk story, with disconfirmatory cues such as the new fracture pattern, fault-splay proximity, and eventual crack underweighted.",
      "why_not_identified": "The transcript strongly suggests confirmatory processing, but the evidence is interwoven with the identified anchoring, automation complacency, and plan continuation mechanisms; identifying it separately would risk double-counting the same underlying bias-specific processing."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single retrospective participant account; no independent sensor, observational, or outcome data beyond the interview transcript.",
    "Retrieved corpus support is sparse and partially OCR-degraded; sources give high-level mechanism definitions or labels rather than geotechnical-specific validation.",
    "Schedule and managerial pressures are present as contextual factors, requiring care to distinguish plan continuation bias from external organizational constraints.",
    "The analysis is blind to experimental conditions and does not assess blame, accident causation, or organizational responsibility."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Biased_2_Gemini_on",
  "interview_id": "MU_Biased_2",
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
