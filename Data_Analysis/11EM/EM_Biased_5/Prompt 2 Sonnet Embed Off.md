You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. This is a debrief interview, not a review — nothing here goes into your personnel file, and you can decline to answer anything. Is that okay?

Participant: Yeah, that's fine. I figured you'd want to talk about the Riverside call eventually.

Interviewer: Exactly. Can you start by telling me your role that shift and what you knew before you got there?

Participant: I was IC, first-due battalion. Dispatch had it as a small trash fire, exterior, rear alley of an industrial unit — auto parts store up front, warehouse space in the back. No hazmat flag, no history on the address. Two engines and a truck were coming with me.

Interviewer: What was your objective once you rolled up?

Participant: Same as always — knock it down fast, keep it from extending into the structure, make sure nobody's inside. Straightforward call, or so it looked.

Interviewer: Walk me through what actually happened, start to finish.

Participant: We pulled up and there was a moderate smoke column, more than I'd expect from a trash fire, but honestly that's not unusual — dumpster fires with pallets or packaging can push a decent amount of smoke. Dispatch had said small and exterior, so I put my first-in crew on a quick knockdown line rather than sending someone around back first. We got water on it within a couple minutes. Once the crew got to the rear of the building, that's when things changed — heavier smoke, a chemical smell, and they found a stack of drums against the rear wall, a couple of them with fire exposure. So now I've got a fire that started as trash-can-sized turning into a possible hazmat exposure.

Interviewer: What did you do at that point?

Participant: Called for a hazmat tech and requested a second alarm for staffing. We shifted into more of a hybrid posture — fire attack continuing, but treating the rear as an isolation zone until we knew what we were dealing with.

Interviewer: Let's go back to that very first call — committing the line before checking the rear. What went into that?

Participant: Dispatch said small trash fire, and that's usually reliable enough to act on immediately — you don't want to sit on a fire waiting for a full 360 when speed matters. The smoke was heavier than I'd expect for that call type, I noticed it, but I didn't want to lose time doing a full walk-around on what was described as a contained exterior fire.

Interviewer: What would have made you hold back and do the 360 first?

Participant: If dispatch had said anything about chemical storage back there, I'd have gone defensive immediately and skipped the quick-attack option entirely. Without that flag, I went with what was called in.

Interviewer: Was time pressure a factor?

Participant: Some. Every minute a small fire sits, it can grow, so there's always pressure to commit. But if I'm honest, the call type is what I leaned on more than the visual.

Interviewer: Once the hazmat tech got there, how did you go about identifying what was in those drums?

Participant: There was a placard on one drum, partially legible — rust and fire damage had eaten some of the numbers. The tech's read was that it lined up with a common solvent, the kind sold in the retail section up front, which made sense to us — warehouse storing overflow of what they sell. The night manager was on scene too, pretty shaken, and he said something like "no, that's not what's back there, it's something different," but he was contradicting himself on other details too — couldn't remember which door led where, that kind of thing.

Interviewer: How did that statement factor into your PPE and agent decisions?

Participant: We didn't weight it heavily. He was rattled, giving inconsistent answers generally, and the placard read supported what we already expected to find. We moved forward with PPE and foam suited for that solvent class.

Interviewer: Did you look for a second placard or manifest confirmation before committing?

Participant: We didn't stop operations to go find one. In hindsight, there was a second drum with an intact placard a few feet away, and it showed a different hazard class. We found the manifest fragment later, in a file cabinet, and it didn't match either.

Interviewer: What would have changed your read at the time?

Participant: A clean placard would've done it immediately. The occupant's statement alone — I probably needed more than that, given how confused he was on everything else.

Interviewer: Let's talk about the perimeter. How did that get set?

Participant: The first-arriving officer put an initial isolation line at 150 meters, standard distance for an unknown chemical exposure situation. By the time I was thinking hard about it, mutual aid units were already staging off that line, and the battalion chief who came in was operating off it too — didn't question it, just built his sector around it.

Interviewer: Did you have any reservations about that distance?

Participant: A little. Wind had started shifting toward the residential block, and I remember thinking we might want to push it out, but everybody was already set up on 150, command posts, staging, hose lays — recalculating and moving all of that would've been a real disruption, and nobody else seemed to be flagging it as a problem. So I left it.

Interviewer: What happened with the wind?

Participant: It fully shifted about twenty minutes later, confirmed by a weather update, and then air monitoring near the edge of our line came back close to the action threshold. We had to push the perimeter out on short notice, which is never clean — reshuffling people, moving apparatus.

Interviewer: If you'd recalculated independently earlier, do you think it would've gone differently?

Participant: Possibly. I had the wind information sooner than we acted on it.

Interviewer: Last decision point — the search. Tell me about that.

Participant: Interior team had cleared about ninety percent of the structure. The last piece was a small storage room right next to the drum stack, and by then the crew had been in there over half an hour, visibly gassed. The chemical ID still wasn't nailed down, and drum integrity in that room was unknown.

Interviewer: What was the call?

Participant: The battalion chief said something like, "we can't call this search done and leave one room unaccounted for — that's the difference between a cleared building and one we're guessing about." Framed that way, leaving it unresolved felt like accepting a gap we couldn't defend. So I authorized the crew to go finish it.

Interviewer: What did you find?

Participant: Room was empty. But one of the drums in there was leaking slightly, so that crew got more exposure time near an unresolved hazard than I'd have liked, in a room we didn't need to enter for life safety, since it turned out to be unoccupied.

Interviewer: Looking back at that whole call — does anything stand out as something that should have been obvious at the time?

Participant: Honestly, yeah. That smoke column at the very start was heavier than a trash fire should produce. I think if I'd trusted that visual over the dispatch description, I'd have sent someone to check the rear before committing the line. It feels like the signs were there from minute one.

Interviewer: What would you tell a newer commander to watch for in a similar situation?

Participant: Don't let the initial call type set your whole picture — cross-check it against what you're actually seeing, especially smoke volume and color. And when a perimeter's already been set by someone else, still run your own numbers if conditions change, because everyone assumes someone else already checked it.

Interviewer: Anything else you want to add?

Participant: Just that none of these calls looked wrong in the moment. It's only once you line them all up afterward that you see where it could've gone differently.

Interviewer: That's helpful. Thanks for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Biased_5",
  "domain_id": "EM",
  "domain": "Emergency management and Civil Protection",
  "role": "Incident Commander (Structural Fire/Hazmat Response)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Riverside Industrial Park: Structural Fire with Concealed Chemical Storage",
    "scenario_summary_internal": "An Incident Commander responds to a reported small trash fire at a mixed-use industrial building (auto-parts retail front, rear warehouse storing unlabeled solvent/chemical drums). Over roughly 40 minutes, the incident escalates from a routine knockdown to a multi-company hazmat-involved structural fire with an uncertain chemical identity, a shifting wind threatening a nearby residential block, and a partially searched structure. The interview reconstructs four sequential decisions the IC made under time pressure, incomplete information, and social/organizational pressure from arriving mutual aid officers.",
    "occupational_realism": {
      "objective": "Achieve life safety for occupants and crews, contain the fire, prevent an uncontrolled chemical release, and protect nearby exposures while resources build up on scene.",
      "setting": "Early evening, single-story industrial park unit with a retail auto-parts storefront and an attached rear warehouse used for solvent and chemical storage; residential block approximately 200m downwind; intermittent radio/dispatch reliability.",
      "constraints": [
        "Only two engines, one truck, and one battalion chief on scene at initial size-up",
        "Original dispatch information described the incident as a small exterior trash fire",
        "Chemical storage manifest for the rear warehouse is incomplete and partially fire-damaged",
        "Wind direction shifts mid-incident toward a residential area",
        "Night manager/occupant is present but shaken and gives inconsistent statements",
        "Search team fatigue increases after 30+ minutes of interior operations",
        "Mutual aid battalion chief arrives and begins directing perimeter decisions alongside the IC"
      ],
      "stakeholders": [
        "Incident Commander (interviewee)",
        "First-arriving engine company officer",
        "Hazmat technician assigned to identify chemical contents",
        "Mutual aid battalion chief",
        "Interior search team",
        "Night shift facility manager/occupant",
        "Dispatch center"
      ],
      "technical_terms_to_use": [
        "size-up",
        "offensive strategy",
        "defensive strategy",
        "NFPA 704 placard",
        "exposure",
        "isolation perimeter",
        "PPE level",
        "IDLH",
        "staging area",
        "unified command",
        "personnel accountability report (PAR)",
        "decon corridor",
        "Emergency Response Guidebook (ERG)"
      ],
      "technical_terms_to_avoid": [
        "anchoring",
        "confirmation bias",
        "framing effect",
        "bandwagon effect",
        "hindsight bias",
        "cognitive bias",
        "heuristic",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch reported 'small trash fire, rear alley' with no mention of chemical storage",
          "Light-to-moderate smoke column visible from the street on arrival",
          "No prior incident history at this address in dispatch notes"
        ],
        "new_information_after_decision": [
          "Heavier smoke and a chemical odor detected once the first crew reaches the rear of the building",
          "Visible drums are discovered stacked against the rear wall, some showing fire exposure"
        ],
        "alternatives": [
          "Commit a single attack line immediately for a quick knockdown consistent with the dispatched call type",
          "Hold the initial line at a defensive stand-off distance and complete a full 360-degree size-up, including the rear of the structure, before committing"
        ],
        "intended_action": "The IC commits the first-arriving crew to an offensive quick-knockdown attack based on the dispatched description, without confirming rear-of-building conditions first."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "A partially obscured NFPA diamond is visible on one drum; some hazard numbers are unreadable due to rust and fire damage",
          "The hazmat technician's preliminary read suggests a common solvent (consistent with items normally sold in the retail front)",
          "The night manager states, inconsistently, that 'something different' is stored in that section of the warehouse"
        ],
        "new_information_after_decision": [
          "A second, fully intact placard is later located on an adjacent drum showing a different hazard class than initially assumed",
          "The manifest fragment recovered from an office file cabinet does not match the assumed solvent"
        ],
        "alternatives": [
          "Pause PPE and tactical decisions until the placard and manifest can be independently cross-checked against the ERG",
          "Proceed with the preliminary solvent identification and select PPE/extinguishing agent consistent with that assumption"
        ],
        "intended_action": "The IC and hazmat technician treat the ambiguous placard reading as consistent with the assumed common solvent, discount the occupant's contradicting statement as unreliable, and proceed with PPE and foam selection built around that assumption."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The first-arriving officer set an initial 150-meter isolation perimeter before wind data was considered",
          "Multiple mutual aid units and the arriving battalion chief have already begun operating and staging based on the 150-meter line",
          "Wind direction has begun shifting toward the residential block, though the shift is not yet fully confirmed"
        ],
        "new_information_after_decision": [
          "Wind shift is confirmed by a later weather update",
          "Air monitoring near the edge of the established perimeter shows readings close to the action threshold, prompting a last-minute perimeter adjustment"
        ],
        "alternatives": [
          "Independently recalculate the isolation distance using current wind data and the ERG guidance for the (still-uncertain) chemical",
          "Adopt the perimeter already agreed upon by the first-arriving officer and endorsed by the incoming battalion chief and other units"
        ],
        "intended_action": "Despite personal uncertainty about whether 150 meters is sufficient given the wind shift, the IC defers to the perimeter already accepted and reinforced by multiple arriving officers rather than independently recalculating it."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Interior search team reports approximately 90% of the structure has been cleared",
          "The remaining unsearched area is a small storage room adjacent to the drum stack",
          "Crew fatigue is visibly increasing after more than 30 minutes of interior work",
          "Chemical identity and drum integrity in that area remain unresolved"
        ],
        "new_information_after_decision": [
          "The final room is found empty of occupants",
          "One drum in that room is later found to be slightly leaking, increasing the exposure that occurred during the extended interior operation"
        ],
        "alternatives": [
          "Withdraw interior crews to defensive/exterior operations given the unresolved chemical risk near the final search area",
          "Send the search team back in to finish clearing the last 10% of the structure quickly"
        ],
        "intended_action": "After the battalion chief frames the choice as 'not wasting the search already completed' rather than as 'entering an unresolved chemical risk area,' the IC authorizes the crew to re-enter and complete the search."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how the call came in and what you knew before you arrived on scene.",
        "What was your overall objective for this incident once you pulled up?"
      ],
      "timeline_reconstruction": [
        "Talk me through what happened, step by step, from arrival to the point crews began interior operations.",
        "At what point did the situation change from what dispatch had described?",
        "What information came in that you didn't have when you first arrived?"
      ],
      "decision_point_probes": [
        "What options did you consider at that point, and why did you choose the one you did?",
        "What specific information were you relying on when you made that call?",
        "Was anyone else's input or agreement part of how you settled on that course of action?",
        "How confident were you in that information at the time, and what would have changed your mind?",
        "How much time pressure were you under when you made that decision?",
        "Had you handled a situation like this before, and did that experience shape your choice?"
      ],
      "closing_hypotheticals": [
        "If you had known earlier what the placard and manifest actually showed, would you have done anything differently?",
        "Looking back now, does anything about how the incident unfolded seem like it should have been obvious at the time?",
        "If the wind hadn't shifted, do you think the perimeter decision would have turned out differently?",
        "What would you tell a newer commander to watch for in a similar call?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "anchor_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Initial strategy commitment is pulled toward the dispatch-provided description ('small trash fire') rather than being adjusted to match the moderate smoke column actually observed on arrival.",
        "affected_reasoning_operation": "Initial size-up and strategy selection (offensive vs. defensive/full assessment)",
        "evidence_available_at_time": [
          "Dispatch description of a small exterior trash fire",
          "Visible moderate smoke column from the street",
          "No stated information yet about rear warehouse contents"
        ],
        "required_textual_manifestation": "IC explicitly references the dispatched call type as the primary basis for committing the initial attack line, and only mentions the smoke column as a secondary or dismissed detail, without describing an independent re-assessment before committing.",
        "plausible_nonbias_interpretation": "A fast offensive knockdown on a small reported fire is a standard, experience-based tactical default; committing quickly could simply reflect efficient triage rather than an anchored estimate.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "initial estimate bias", "adjustment failure"]
      },
      {
        "instance_id": "hindsight_01",
        "bias": "Hindsight bias",
        "decision_point": 1,
        "mechanism": "During retrospective reflection on the same initial strategy decision, the IC characterizes the eventual escalation as something that 'should have been obvious' from the smoke conditions, overstating the foreseeability of the outcome relative to what was actually knowable at the time of the decision.",
        "affected_reasoning_operation": "Retrospective evaluation/causal judgment of a past decision's foreseeability, distinct from the real-time strategy selection itself",
        "evidence_available_at_time": [
          "Outcome knowledge available only at interview time: drums, hazmat escalation, eventual perimeter and search complications",
          "Contemporaneous information that was actually available before phase 1's decision (dispatch call type, limited smoke view)"
        ],
        "required_textual_manifestation": "In response to a closing hypothetical probe, the IC states in substance that the escalation 'should have been obvious' or 'was really there to see' from the early smoke conditions, without acknowledging that this information was not equally clear before the outcome was known.",
        "plausible_nonbias_interpretation": "Experienced commanders often identify genuine early warning signs in retrospect; noting a missed cue could reflect accurate professional learning rather than distorted foreseeability judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight", "foreseeability", "knew-it-all-along", "outcome knowledge distortion"]
      },
      {
        "instance_id": "confirm_01",
        "bias": "Confirmation Bias",
        "decision_point": 2,
        "mechanism": "The ambiguous placard and manifest fragment are interpreted as supporting the initially guessed solvent, while the occupant's contradicting statement is actively discounted rather than weighed as disconfirming evidence.",
        "affected_reasoning_operation": "Evidence weighting and hazard identification during PPE/agent selection",
        "evidence_available_at_time": [
          "Partially obscured NFPA placard consistent with, but not conclusive of, the assumed solvent",
          "Occupant statement suggesting a different chemical is stored in that section",
          "Hazmat technician's preliminary read favoring the common solvent"
        ],
        "required_textual_manifestation": "IC describes treating the unclear placard reading as confirming the initial guess and explicitly gives a reason for setting aside or downplaying the occupant's contrary statement (e.g., citing the occupant's shaken state) rather than seeking independent verification.",
        "plausible_nonbias_interpretation": "Occupant statements during active emergencies are often unreliable, so discounting one contradicting account could reflect sound risk-based judgment rather than selective evidence use.",
        "strength": "moderate",
        "do_not_make_explicit": ["confirmation bias", "selective evidence", "disconfirming evidence", "motivated reasoning"]
      },
      {
        "instance_id": "bandwagon_01",
        "bias": "Bandwagon effect",
        "decision_point": 3,
        "mechanism": "The IC adopts the perimeter distance already set and reinforced by multiple other officers and the mutual aid battalion chief, despite privately holding doubts about its sufficiency given the shifting wind, rather than independently recalculating it.",
        "affected_reasoning_operation": "Perimeter/isolation-distance decision under converging peer agreement",
        "evidence_available_at_time": [
          "150-meter perimeter already established by the first-arriving officer",
          "Multiple additional units and the mutual aid battalion chief operating consistently with that line",
          "Early, not-yet-confirmed indication of a wind shift toward the residential block"
        ],
        "required_textual_manifestation": "IC states that other units and the battalion chief were already operating on the existing perimeter and describes going along with it, while separately acknowledging personal uncertainty about whether the distance was adequate given the wind.",
        "plausible_nonbias_interpretation": "Maintaining a single established perimeter avoids conflicting instructions and confusion across multiple companies, so preserving it could reflect legitimate incident-command coordination rather than social conformity.",
        "strength": "moderate",
        "do_not_make_explicit": ["bandwagon", "social proof", "conformity", "peer pressure"]
      },
      {
        "instance_id": "framing_01",
        "bias": "Framing Effect",
        "decision_point": 4,
        "mechanism": "The decision to re-enter and finish the search is driven by the battalion chief's presentation of the choice as avoiding wasted effort ('not wasting the search already completed') rather than as accepting continued exposure to an unresolved chemical risk; the same factual choice, framed around loss-of-effort, shifts the IC toward the risk-tolerant option.",
        "affected_reasoning_operation": "Risk-based go/no-go decision on completing interior search",
        "evidence_available_at_time": [
          "90% of the structure already cleared",
          "Remaining area adjacent to unresolved drum stack",
          "Battalion chief's verbal framing emphasizing completed effort over remaining risk",
          "Visible crew fatigue"
        ],
        "required_textual_manifestation": "IC recounts the battalion chief's specific framing of the remaining decision (effort-already-invested framing) as a stated reason for authorizing re-entry, rather than independently weighing the unresolved chemical risk on its own terms.",
        "plausible_nonbias_interpretation": "Completing a nearly finished search to confirm no occupants remain is a defensible life-safety priority independent of how the choice was phrased.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "loss framing", "sunk cost of effort", "gain/loss frame"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', no paired control scenario supplied."
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
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Each decision point includes information available before the decision and new information learned afterward.",
      "Exactly five intended bias instances are planned, one per manifest entry, matching the exact-occurrence rules.",
      "No bias names, definitions, or psychological terminology appear in the planned public interview content.",
      "anchor_01 and hindsight_01 share decision point 1 but involve distinct reasoning operations (real-time estimation vs. retrospective foreseeability judgment) and distinct evidence traces.",
      "Each occurrence has a documented plausible non-bias interpretation to prevent mechanical bias attribution from outcomes.",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals as required.",
      "Target interview length of 1,350 words (range 1,215-1,485) is achievable given four decision points and five embedded instances without repetitive exposition."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Framing Effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an externally supplied verbal frame (loss/effort framing) from the battalion chief that shifts the IC's risk decision at decision point 4."
      },
      {
        "bias": "Hindsight bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest only during retrospective/closing-hypothetical reflection on decision point 1, not during the real-time decision narration."
      },
      {
        "bias": "Bandwagon effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as deference to converging agreement among multiple other officers/battalion chief at decision point 3, with the IC acknowledging private doubt."
      },
      {
        "bias": "Anchoring Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as reliance on the initial dispatch description at decision point 1, insufficiently adjusted for observed smoke conditions."
      },
      {
        "bias": "Confirmation Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as interpreting ambiguous placard/manifest evidence as supporting the initial solvent guess while discounting the occupant's contradicting statement at decision point 2."
      }
    ],
    "target_bias_names": [
      "Framing Effect",
      "Hindsight bias",
      "Bandwagon effect",
      "Anchoring Bias",
      "Confirmation Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Framing Effect", "requested_occurrences": 1 },
      { "bias": "Hindsight bias", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 },
      { "bias": "Confirmation Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "anchor_01", "bias": "Anchoring Bias" },
      { "instance_id": "hindsight_01", "bias": "Hindsight bias" },
      { "instance_id": "confirm_01", "bias": "Confirmation Bias" },
      { "instance_id": "bandwagon_01", "bias": "Bandwagon effect" },
      { "instance_id": "framing_01", "bias": "Framing Effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "anchor_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "hindsight_01", "bias": "Hindsight bias", "decision_point": 1 },
      { "instance_id": "confirm_01", "bias": "Confirmation Bias", "decision_point": 2 },
      { "instance_id": "bandwagon_01", "bias": "Bandwagon effect", "decision_point": 3 },
      { "instance_id": "framing_01", "bias": "Framing Effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "anchor_01",
        "bias": "Anchoring Bias",
        "mechanism": "Strategy commitment insufficiently adjusted away from the initial dispatch-provided call description despite contrary visual cues.",
        "affected_reasoning_operation": "Initial size-up/strategy selection",
        "evidence_source": "Dispatch call description vs. observed smoke column",
        "distinctiveness_requirement": "Occurs at the moment of real-time strategy commitment, before any outcome is known; distinct from hindsight_01, which occurs only during later retrospective reflection on the same decision."
      },
      {
        "instance_id": "hindsight_01",
        "bias": "Hindsight bias",
        "mechanism": "Retrospective overstatement of the foreseeability of escalation, given outcome knowledge unavailable at the time of the original decision.",
        "affected_reasoning_operation": "Retrospective causal/foreseeability judgment",
        "evidence_source": "Closing hypothetical probe response referencing the smoke column and the eventual escalation",
        "distinctiveness_requirement": "Occurs only in retrospective narration/probe response, temporally and operationally separate from the contemporaneous anchoring judgment in anchor_01."
      },
      {
        "instance_id": "confirm_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective interpretation of ambiguous placard/manifest evidence as consistent with the prior solvent assumption, paired with active discounting of a contradicting occupant statement.",
        "affected_reasoning_operation": "Evidence weighting for hazard identification and PPE selection",
        "evidence_source": "Partial placard, manifest fragment, and occupant statement",
        "distinctiveness_requirement": "Sole confirmation-bias instance; tied to decision point 2's evidence-selection act, not repeated elsewhere."
      },
      {
        "instance_id": "bandwagon_01",
        "bias": "Bandwagon effect",
        "mechanism": "Adoption of an already-established perimeter distance because multiple other units and a superior officer are already operating on it, despite unresolved personal doubt.",
        "affected_reasoning_operation": "Perimeter/isolation-distance decision under peer convergence",
        "evidence_source": "Existing 150-meter perimeter and multi-unit operational alignment on it",
        "distinctiveness_requirement": "Sole bandwagon instance; tied specifically to decision point 3's social-convergence dynamic."
      },
      {
        "instance_id": "framing_01",
        "bias": "Framing Effect",
        "mechanism": "Decision outcome shifts based on the battalion chief's effort/loss-oriented verbal framing of the choice, rather than independent evaluation of the underlying chemical risk.",
        "affected_reasoning_operation": "Risk-based go/no-go decision for completing interior search",
        "evidence_source": "Battalion chief's stated framing of the remaining search decision",
        "distinctiveness_requirement": "Sole framing instance; tied to decision point 4's externally supplied frame, distinct from all other decision points."
      }
    ],
    "intended_strength": [
      { "instance_id": "anchor_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "hindsight_01", "bias": "Hindsight bias", "strength": "subtle" },
      { "instance_id": "confirm_01", "bias": "Confirmation Bias", "strength": "moderate" },
      { "instance_id": "bandwagon_01", "bias": "Bandwagon effect", "strength": "moderate" },
      { "instance_id": "framing_01", "bias": "Framing Effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Biased_5",
    "domain_id": "EM",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Automatic assignment per mechanism fit and narrative realism: each bias mapped to the decision point whose evidentiary structure and reasoning operation most plausibly produces that bias in an Incident Commander's retrospective account; anchor_01 and hindsight_01 co-located at decision point 1 only because they represent temporally and operationally distinct reasoning acts (contemporaneous estimation vs. retrospective foreseeability judgment) on the same underlying event, satisfying the distinct-evidence-source/moment requirement for shared decision points.",
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
          "segment_id": "seg_dp1",
          "speaker": "Participant",
          "segment_type": "Decision point 1: initial size-up and retrospective reflection",
          "raw_interview_anchor": "Dispatch said small trash fire ... The smoke was heavier than I'd expect ... I didn't want to lose time doing a full walk-around. Later: That smoke column at the very start was heavier than a trash fire should produce ... the signs were there from minute one.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "anchor_01",
            "hindsight_01"
          ],
          "ground_truth_rationale": "The IC cites the dispatched call type as the primary reason for committing the quick-knockdown line, acknowledges heavier-than-expected smoke, but declines a full 360 before committing. In the closing reflection, the IC says the early smoke made the escalation obvious and that the signs were there from minute one, after learning about the drums and hazmat complications."
        },
        {
          "segment_id": "seg_dp2",
          "speaker": "Participant",
          "segment_type": "Decision point 2: chemical identification and PPE/agent selection",
          "raw_interview_anchor": "The tech's read was that it lined up with a common solvent ... the manager ... said ... it's something different ... We didn't weight it heavily ... the placard read supported what we already expected to find.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "confirm_01"
          ],
          "ground_truth_rationale": "The IC treats the partially legible placard as supporting the assumed common solvent, discounts the manager's contrary statement because he was rattled, and proceeds with solvent-specific PPE and foam without independent verification."
        },
        {
          "segment_id": "seg_dp3",
          "speaker": "Participant",
          "segment_type": "Decision point 3: isolation-perimeter distance under shifting wind",
          "raw_interview_anchor": "Wind had started shifting toward the residential block ... recalculating and moving all of that would've been a real disruption, and nobody else seemed to be flagging it as a problem. So I left it.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "bandwagon_01"
          ],
          "ground_truth_rationale": "The IC remembers wanting to push the 150-meter line out as wind shifted, but leaves it because mutual-aid units and the battalion chief were already set up and nobody else flagged a problem."
        },
        {
          "segment_id": "seg_dp4",
          "speaker": "Participant",
          "segment_type": "Decision point 4: go/no-go decision on completing the interior search",
          "raw_interview_anchor": "We can't call this search done and leave one room unaccounted for ... Framed that way, leaving it unresolved felt like accepting a gap we couldn't defend. So I authorized the crew to go finish it.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "framing_01"
          ],
          "ground_truth_rationale": "The IC says the battalion chief framed leaving one room as an indefensible gap after clearing 90%, which led to authorizing re-entry despite fatigue and unresolved chemical risk near the drums."
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
    "analysis_scope_note": "No retrieved corpus passages were provided for this analysis. Bias labels and definitions therefore draw on general knowledge of established cognitive and social-influence biases."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "social proof bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring effect",
      "alternative_labels": [
        "anchoring bias",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information when making subsequent judgments, even when later or competing information suggests that adjustment is warranted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial fire-attack commitment without a rear 360",
      "decision_point_description": "Whether to commit the first crew to a quick knockdown line immediately or first conduct a full walk-around/reconnaissance of the building.",
      "affected_reasoning_operation": "Interpretation of smoke volume and selection of initial tactical action",
      "bias_specific_mechanism": "The dispatch description 'small trash fire' functioned as an anchor. Although the participant observed a moderate smoke column heavier than expected for that call type, he did not sufficiently adjust away from the initial dispatch label and framed a fuller 360 as something that would lose time rather than as a check of an anomaly.",
      "manifestation_in_interview": "The participant explicitly states that dispatch said small and exterior and that he put the first crew on a quick knockdown line rather than checking the rear first. Later he notes the smoke was heavier than he would expect, but says he leaned on the call type more than the visual.",
      "effect_on_reasoning_or_decision": "The initial anchor likely delayed recognition that the fire involved a chemical or hazmat source at the rear, leading to water on the fire before the rear hazard was identified.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Dispatch had said small and exterior, so I put my first-in crew on a quick knockdown line rather than sending someone around back first.",
          "evidence_explanation": "Shows the initial dispatch description directly shaped the immediate tactical choice before the scene was verified."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The smoke was heavier than I'd expect for that call type, I noticed it, but I didn't want to lose time doing a full walk-around on what was described as a contained exterior fire.",
          "evidence_explanation": "He noticed conflicting visual information but treated the initial call type as the more decisive input rather than adjusting his picture."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, the call type is what I leaned on more than the visual.",
          "evidence_explanation": "Direct statement of overweighting the initial anchor relative to the observed scene information."
        }
      ],
      "correction_or_counterevidence": "There was also ordinary time pressure and a legitimate desire to attack the fire quickly; dispatch information is generally reliable. However, the participant's explicit statement that he leaned on the call type more than the visual supports anchoring beyond ordinary heuristics.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and definition draw on general knowledge of established cognitive biases.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "selective information search",
        "premature closure"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, or remember information in ways that confirm an existing hypothesis while giving less weight to or failing to search for disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Chemical identification and PPE/agent commitments",
      "decision_point_description": "Whether to accept the initial solvent identification from a partially legible placard or seek additional placard/manifest confirmation before committing to PPE and foam.",
      "affected_reasoning_operation": "Hazard identification and selection of PPE and agent",
      "bias_specific_mechanism": "After the tech read a partially legible placard as a common solvent consistent with the business context, the participant's command team formed a plausible hypothesis. They then weighed the supporting placard read more heavily and did not search for a second placard or manifest confirmation, even though an occupant offered a contradictory statement.",
      "manifestation_in_interview": "The participant says the solvent reading 'made sense' and later says the placard read 'supported what we already expected to find.' He also says they did not stop operations to look for a second placard or manifest before committing.",
      "effect_on_reasoning_or_decision": "The command team selected PPE and foam suited for the initially identified solvent class without confirming the identification; later evidence suggested the hazard was different.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The tech's read was that it lined up with a common solvent, the kind sold in the retail section up front, which made sense to us — warehouse storing overflow of what they sell.",
          "evidence_explanation": "The hypothesis was rendered especially plausible by a coherent business story, increasing confidence in an unverified identification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We didn't weight it heavily. He was rattled, giving inconsistent answers generally, and the placard read supported what we already expected to find.",
          "evidence_explanation": "This pairs discounting contradictory information with the phrase 'supported what we already expected,' which is consistent with confirmation-oriented reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We didn't stop operations to go find one.",
          "evidence_explanation": "Shows an absence of active search for disconfirming placard or manifest information before commitment."
        }
      ],
      "correction_or_counterevidence": "The occupant's contradiction was legitimately weakened by his confusion and inconsistent details; acting quickly on a partial placard may also be standard given fireground uncertainty. These factors create a competing non-bias explanation, which is why confidence is low.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and definition draw on general knowledge of established cognitive biases.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "social proof bias",
      "alternative_labels": [
        "social proof",
        "conformity bias",
        "groupthink"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely on the inaction or behavior of others as evidence for what is correct, leading an individual to suppress their own divergent safety-relevant judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Perimeter adjustment decision after wind shift",
      "decision_point_description": "Whether to recalculate and expand the initial 150-meter isolation perimeter when the wind began shifting toward a residential block.",
      "affected_reasoning_operation": "Risk assessment and perimeter control decision",
      "bias_specific_mechanism": "The participant had an independent concern that the perimeter should be moved, but he interpreted the absence of others flagging the issue and the fact that the command structure was already built on 150 meters as evidence that the current line was acceptable. He then suppressed his own initiative to recalculate.",
      "manifestation_in_interview": "He says he remembered thinking they might want to push the perimeter out, but everyone was already set up and no one else seemed to be flagging it as a problem, so he left it.",
      "effect_on_reasoning_or_decision": "The perimeter remained at 150 meters despite changing wind toward a residential block; it later had to be pushed out on short notice after the wind shifted and air monitoring near the edge approached the action threshold.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Wind had started shifting toward the residential block, and I remember thinking we might want to push it out, but everybody was already set up on 150, command posts, staging, hose lays — recalculating and moving all of that would've been a real disruption, and nobody else seemed to be flagging it as a problem. So I left it.",
          "evidence_explanation": "The quote captures both the independent doubt and the use of others' non-action plus operational inertia as reasons not to act."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly. I had the wind information sooner than we acted on it.",
          "evidence_explanation": "Confirms he possessed relevant information earlier but did not act on it, which aligns with social influence overriding his own read."
        }
      ],
      "correction_or_counterevidence": "Maintaining a 150-meter perimeter had legitimate operational advantages, and altering it would have disrupted command posts, staging, and hose lays. The initial distance was also standard for unknown chemical exposure. The bias is that the participant deferred to the existing group baseline despite his own changing-condition judgment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and definition draw on general knowledge of established social-influence biases.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "framing effect",
      "alternative_labels": [
        "plan continuation bias",
        "risky choice framing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A change in decision-making or risk preference caused by the way options are described, particularly when one option is framed as an unacceptable loss or failure.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final search room entry under unresolved hazards",
      "decision_point_description": "Whether to authorize the already-fatigued crew to enter and clear the last small storage room adjacent to the drum stack before chemical ID and drum integrity were known.",
      "affected_reasoning_operation": "Risk-benefit judgment about search completion",
      "bias_specific_mechanism": "The battalion chief framed stopping as 'a building we're guessing about' and framed completing the room as the difference between a cleared building and an indefensible gap. This loss-framing made the risky completion option feel more defensible and led the participant to authorize entry despite concurrent hazard cues.",
      "manifestation_in_interview": "The participant states the room was next to the drum stack, the crew was visibly gassed, chemical ID was unresolved, and drum integrity unknown, yet he authorized the entry after the chief's framing.",
      "effect_on_reasoning_or_decision": "The crew entered the room and received additional exposure time near a leaking drum; the room turned out to be unoccupied, so the additional exposure carried no identified life-safety benefit.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Interior team had cleared about ninety percent of the structure. The last piece was a small storage room right next to the drum stack, and by then the crew had been in there over half an hour, visibly gassed. The chemical ID still wasn't nailed down, and drum integrity in that room was unknown.",
          "evidence_explanation": "These are risk-relevant cues that would normally favor caution or pause; the decision is made despite these cues."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The battalion chief said something like, 'we can't call this search done and leave one room unaccounted for — that's the difference between a cleared building and one we're guessing about.' Framed that way, leaving it unresolved felt like accepting a gap we couldn't defend. So I authorized the crew to go finish it.",
          "evidence_explanation": "The participant explicitly attributes the authorization to the way the choice was framed, rather than to a fresh risk assessment."
        }
      ],
      "correction_or_counterevidence": "Completing a search is a legitimate fireground objective, and at the time the room could have contained a victim. The later finding that it was empty does not by itself prove the decision was biased; the bias evidence is the participant's explicit account of the frame driving the risk acceptance.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; the label and definition draw on general knowledge of established cognitive biases.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-incident reflection on early smoke column",
      "supporting_interview_quote": "It feels like the signs were there from minute one.",
      "plausible_mechanism": "Knowing the later escalation and hazmat identification, the participant now treats the early moderate smoke as more obviously diagnostic than it may have been at the time.",
      "why_not_identified": "The participant also states that he noticed the smoke at the time and that he leaned on the call type then, so the retrospective statement may reflect regret or normal after-action review rather than a clear biased hindsight judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages were not provided to the analyst; all corpus_evidence arrays are empty and labels rely on general knowledge.",
    "The analysis is based on retrospective self-report; contemporaneous reasoning was inferred from the participant's described thoughts and decisions."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Biased_5_Sonnet_off",
  "interview_id": "EM_Biased_5",
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
