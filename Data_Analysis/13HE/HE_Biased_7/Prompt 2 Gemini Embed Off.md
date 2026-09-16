You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. As discussed, this is for our post-incident learning review, not a disciplinary process — I want to understand how you saw and processed the situation as it developed. Anything you share stays within the review process. You good to start?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role and a bit about your background before we get into the incident itself?

Participant: I'm the on-shift Incident Commander for the site brigade — I've been in this role about six years, twelve years on the brigade total. Mostly hydrocarbon and solvent handling areas, so tank farm fires aren't unfamiliar to me.

Interviewer: Good. So walk me through what you saw and were told when you arrived on scene.

Participant: Control room paged it as a flammable liquid tank fire in the solvent storage area, described as contained, dark smoke visible. When I pulled up, I had a heavy black column coming off one of the four tanks in the bunded area. Wind was light, shifting a bit, not pushing smoke hard in any one direction. Visually it looked almost identical to a fire we had three years back in the same general area — same kind of column, same rough intensity. That one we knocked down clean with an offensive foam attack, crews in with exposure lines, no real drama. So my first read was, this looks like that one.

Interviewer: What was your main objective at that point?

Participant: Get the fire knocked down before it could threaten the second tank or the production building next door, and do it without losing anybody. Standard priorities — life safety, then stabilize, then protect property.

Interviewer: And the manifest — did you know exactly what was burning?

Participant: Not confirmed yet, no. Four tanks in that bund, different products, and hazmat hadn't given me a firm ID. But the call came through as contained, and visually it read the same as the one I already knew how to fight, so I went with what I had. Honestly, hearing it called contained made it sound like it was staying inside the kind of tank fire we handle all the time — so getting the manifest nailed down didn't feel like something I had to sort out before we started moving lines in.

Interviewer: Let's reconstruct the sequence phase by phase. What happened right after you made that initial call?

Participant: I committed two crews in with foam lines and set exposure protection on the neighboring tank. Shortly after that, hazmat got on scene and told me the burning tank actually held a more volatile mix than the one from that earlier fire — different product entirely, just looked similar from the outside. By then the lines were already in and crews were positioned close, maybe fifteen meters off the shell.

Interviewer: How did that change your read of the situation?

Participant: It should have, and it registered, but we were already committed at that point. Pulling two charged lines and repositioning crews mid-attack isn't something you do lightly — there's real risk in that movement itself. So the plan stayed as it was; we didn't stop and rebuild the IAP around the new information, we just kept pushing the attack we'd already started.

Interviewer: Let's stay on that moment. What options did you actually weigh once you had the shell temperature alarms rising?

Participant: Either pull back to a defensive perimeter and go to unmanned monitors, or hold position and add a second foam line for more knockdown. We'd only really sat down and reviewed the plan once, right at the start. Nothing after that forced a formal stop-and-reassess — no single trigger big enough on its own — so we just kept executing what we'd already briefed. Looking back, the volatile-product call and the climbing temperature together probably should have been enough to warrant a fresh look, but since nobody formally called for a stop, we treated that as reason enough to keep running with the plan we already had.

Interviewer: What told you to add the second line rather than withdraw?

Participant: Partly the alarms themselves, wanting more suppression on the seat of the fire. But honestly, part of it was that we already had people and hose in position — pulling that back felt like giving up ground we'd already paid for in terms of setup time and risk getting in.

Interviewer: Understood. Let's move to the next phase. What was happening on the radio and at your command post around this time?

Participant: The mutual aid engine companies were on our shared channel, and a couple of their officers came on saying it looked like a standard tank fire, keep pushing the interior attack. Multiple voices, same read. At the post, our safety officer raised a concern about how close our crews were sitting relative to the second tank's exposure. We talked about it for maybe a minute.

Interviewer: How was that concern handled?

Participant: We acknowledged it, but the room moved fast — everybody sort of nodded that we were fine to continue, and we didn't really dig into it past that. It wasn't dismissed outright, it just didn't get a long conversation before we moved on.

Interviewer: Once the group had nodded along, did anyone go back and test the safety officer's concern more directly?

Participant: Not really. Nobody asked him to lay out specifically what he was seeing or walk us through why he thought the exposure risk was higher than we'd assessed. No one was assigned to argue the other side or double-check it. Once the room had settled on continuing, it just didn't come back up.

Interviewer: Did the mutual aid officers' agreement factor into your decision?

Participant: Yeah, some. When you've got multiple experienced officers on the net independently saying the same thing, that carries weight. It reinforced that we were reading the incident the way most people out there were reading it.

Interviewer: What came in right after that?

Participant: A relief crew came off shift and mentioned they thought they saw the second tank shell bulging slightly, maybe some vibration. Nothing measured, just an observation.

Interviewer: Let's go to the final phase. What did the data look like as you approached the withdrawal decision?

Participant: We'd had a shell temperature trend on that second tank climbing steadily for about twenty minutes, radioed in multiple times, consistent rise. Then right at the point where I was deciding whether to call full withdrawal, a spotter came on and said it looked stable now, based on a quick visual check.

Interviewer: How did you weigh those two things against each other?

Participant: The spotter's call was the most current thing I had in my ear at that exact moment, so it carried real weight in the decision. I held off on ordering the full pull-back a bit longer than the trend alone probably would have justified, because that last report suggested things had settled.

Interviewer: How confident were you in that spotter's assessment versus the trend data?

Participant: Reasonably — he's experienced, and a visual read from someone right there has value the instruments don't always capture. But looking back, that trend had been consistent for twenty minutes, and one quick look doesn't necessarily overturn that.

Interviewer: What ended up happening?

Participant: The tank vented on its own, no rupture, nobody hurt. Fire was knocked down maybe forty minutes after that. Could've gone worse; can't say for certain the timing of withdrawal is what mattered most.

Interviewer: Looking back, if the hazmat report on tank contents had come in before you committed crews, would your first call have gone differently?

Participant: Possibly — I might have held the lines back until we confirmed exactly what we were dealing with rather than moving straight to the offensive attack.

Interviewer: And if the mutual aid officers on the net had been split or silent at that middle phase, do you think the outcome there changes?

Participant: Maybe. Without that agreement, the safety officer's point might have gotten more airtime, and we might've paused longer before continuing.

Interviewer: Last one — what single piece of information do you wish had carried more weight at the very end?

Participant: The twenty-minute trend, honestly. It was right there the whole time. I let one fresh comment outweigh a much longer pattern that had already told a consistent story.

Interviewer: Appreciate you walking through all of that in detail.

Participant: No problem. It's useful to go back over it like this.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Biased_6",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Emergency Response/Incident Commander (Industrial Fire Brigade)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Tank Farm Solvent Fire — Offensive Commitment Under Escalating Thermal Warning",
    "scenario_summary_internal": "An industrial fire brigade Incident Commander responds to a fire in a four-tank solvent storage/blending area at a chemical processing site. The IC initially frames the event as a routine, contained tank fire similar to one handled successfully years earlier, commits an offensive foam attack, and progressively resists tactical reassessment as new hazmat, structural, and thermal data accumulate, while command-post and mutual-aid social dynamics reinforce continuation of the original plan until a final withdrawal-timing decision.",
    "occupational_realism": {
      "objective": "Extinguish or control the tank fire and prevent catastrophic tank shell failure while protecting brigade personnel and adjacent production assets, without a mechanically 'wrong' outcome revealing bias.",
      "setting": "Onsite industrial fire brigade responding to a fire in a bunded above-ground storage tank (AST) farm at a chemical processing/solvent blending facility, with municipal mutual aid engine companies supporting on a shared radio net.",
      "constraints": [
        "Limited initial information on exact tank contents pending hazmat/manifest confirmation",
        "Light, variable wind affecting smoke and vapor dispersion",
        "Personnel and hoselines already committed to close-quarters positions",
        "Time pressure from rising shell temperature indicators",
        "Multiple radio channels with municipal mutual aid officers weighing in",
        "Command post staffed by IC, safety officer, and hazmat/structural specialist"
      ],
      "stakeholders": [
        "Incident Commander (interviewee)",
        "Plant control room operator",
        "Hazmat technician",
        "Structural/process safety engineer",
        "Safety officer at command post",
        "Municipal mutual aid engine company officers",
        "Interior attack crews"
      ],
      "technical_terms_to_use": [
        "defensive perimeter",
        "master stream/monitor",
        "shell temperature indicator",
        "exposure protection",
        "incident action plan (IAP)",
        "bunded area",
        "radiant heat",
        "foam concentrate",
        "exclusion zone",
        "size-up"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "groupthink",
        "sunk cost",
        "framing"
      ],
      "excluded_themes": []
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch report describes a 'contained flammable liquid tank fire' with dark smoke",
          "IC's visual size-up shows a smoke column resembling a tank fire he successfully controlled with offensive foam attack three years earlier",
          "Tank farm manifest not yet confirmed; four tanks present with differing contents",
          "Wind light and variable"
        ],
        "new_information_after_decision": [
          "Hazmat technician arrives and reports the specific burning tank holds a more volatile solvent mixture than the one from the earlier incident the IC recalled"
        ],
        "alternatives": [
          "Launch immediate offensive foam attack with exposure protection lines while confirming contents",
          "Establish a defensive stand-off perimeter and hold attack until tank contents and manifest are verified"
        ],
        "intended_action": "IC commits crews to an offensive attack, treating the fire as functionally identical to the earlier successful incident and accepting the dispatcher's 'contained' characterization as the operative risk frame."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Thermal imaging and shell temperature alarms show a rising trend on the burning tank",
          "Two crews and hoselines already positioned within 15 meters under the original plan",
          "IAP has been reviewed only once, at the initial size-up"
        ],
        "new_information_after_decision": [
          "Structural/hazmat specialist flags an accelerating temperature trend on the adjacent (second) tank as a possible early warning sign"
        ],
        "alternatives": [
          "Withdraw interior crews to a defensive perimeter and switch to unmanned monitor streams",
          "Continue current offensive positions and reinforce with an additional foam line"
        ],
        "intended_action": "IC keeps crews in their committed interior positions and reinforces rather than withdrawing, without formally revisiting the IAP against the new alarm data."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Multiple municipal mutual-aid officers on the shared radio net voice support for continuing the interior foam attack",
          "Safety officer at the command post raises a verbal concern about exposure risk to interior crews",
          "Command post discussion is brief; no formal risk re-assessment log is opened"
        ],
        "new_information_after_decision": [
          "A relief crew reports visible bulging or vibration on the adjacent tank shell"
        ],
        "alternatives": [
          "Escalate to full site evacuation and adopt a defensive-only stance",
          "Maintain the current offensive plan, consistent with the on-net consensus"
        ],
        "intended_action": "IC affirms continuation of the offensive plan based on the audible agreement of multiple mutual-aid officers, and the command post reaches quick unanimous agreement without substantively engaging the safety officer's objection."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "A 20-minute instrument trend log shows a steady, repeatedly radioed rise in shell temperature on the adjacent tank",
          "A spotter's single, most recent verbal report states the tank 'looks stable now' based on a brief visual check"
        ],
        "new_information_after_decision": [
          "Outcome is ambiguous: the tank vents without catastrophic failure, but post-incident review cannot cleanly attribute this to the timing decision"
        ],
        "alternatives": [
          "Order immediate full withdrawal based on the sustained instrument trend",
          "Delay the withdrawal order, weighting the spotter's latest verbal update"
        ],
        "intended_action": "IC delays the withdrawal order, giving the most recent single verbal report more practical weight than the accumulated instrument trend data."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you saw and were told as you arrived on scene.",
        "What was your primary objective when you took command?"
      ],
      "timeline_reconstruction": [
        "What happened right after your initial strategy decision, phase by phase?",
        "At what points did new information arrive, and from which source?",
        "How did your read of the situation change (or not change) as the incident progressed?"
      ],
      "decision_point_probes": [
        "What options did you consider at that moment, and why did you choose the one you did?",
        "What specific cues or reports drove that call?",
        "Had you seen a similar situation before, and did that influence you here?",
        "How much time pressure did you feel at that point?",
        "How confident were you in the information you were acting on?",
        "Did anyone on scene or on the radio express a different view, and how was that handled?"
      ],
      "closing_hypotheticals": [
        "If the hazmat report had come in before you committed crews, would your initial call have differed?",
        "If the mutual-aid officers on the net had been silent or split, would phase three have gone differently?",
        "Looking back, what single piece of information do you wish had carried more weight at the end?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "rh_01",
        "bias": "Representative heuristic",
        "decision_point": 1,
        "mechanism": "IC classifies the current fire as belonging to the same category as a prior successfully-resolved tank fire based on superficial visual similarity (smoke color/column shape), overriding the need to verify base-rate-relevant differences (contents, tank design).",
        "affected_reasoning_operation": "Situation classification / analogical categorization prior to strategy selection",
        "evidence_available_at_time": ["Visual smoke column resembling a prior incident", "Unconfirmed tank contents manifest"],
        "required_textual_manifestation": "IC explicitly links the current smoke/appearance to the specific earlier fire and treats that resemblance as sufficient basis for applying the same offensive tactic, before contents are confirmed.",
        "plausible_nonbias_interpretation": "Experienced pattern-based size-up is a legitimate, trained skill; using prior experience is not inherently biased.",
        "strength": "subtle",
        "do_not_make_explicit": ["representative heuristic", "base rate", "pattern-matching bias"]
      },
      {
        "instance_id": "fr_01",
        "bias": "Framing effect",
        "decision_point": 1,
        "mechanism": "The dispatcher's verbal label 'contained flammable liquid tank fire' anchors the IC's risk framing toward a low-severity, manageable-event schema, shaping the offensive/defensive choice independently of the visual and manifest ambiguity.",
        "affected_reasoning_operation": "Initial risk framing / threat categorization from a verbal report",
        "evidence_available_at_time": ["Dispatch radio language describing the event as 'contained'"],
        "required_textual_manifestation": "IC recalls the dispatcher's specific wording and describes treating it as an accurate characterization of severity that shaped the choice of an offensive posture.",
        "plausible_nonbias_interpretation": "Dispatch information is a normal, necessary input to size-up and reasonably guides initial posture.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "anchoring on wording"]
      },
      {
        "instance_id": "sc_01",
        "bias": "Sunk cost bias",
        "decision_point": 2,
        "mechanism": "IC's decision to keep crews in committed interior positions is justified partly by reference to resources already deployed (crews, hoselines) rather than solely by the current risk data.",
        "affected_reasoning_operation": "Resource-continuation decision under new alarm data",
        "evidence_available_at_time": ["Two crews and hoselines already positioned within 15m", "Rising shell temperature alarm"],
        "required_textual_manifestation": "IC references the existing commitment of crews/hoselines as a reason to continue and reinforce rather than withdraw, in response to the new thermal data.",
        "plausible_nonbias_interpretation": "Repositioning committed crews has real operational cost and risk, so caution about immediate withdrawal can be a reasonable tactical judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment"]
      },
      {
        "instance_id": "sq_01",
        "bias": "Status quo bias",
        "decision_point": 2,
        "mechanism": "The command team continues the original IAP without formally revisiting it against the new alarm data, defaulting to 'no change' absent an explicit prompt to reassess, distinct from the resource-justification reasoning of sc_01.",
        "affected_reasoning_operation": "Plan-maintenance decision / failure to trigger IAP re-evaluation",
        "evidence_available_at_time": ["IAP reviewed only once at initial size-up", "New structural/hazmat flag on adjacent tank"],
        "required_textual_manifestation": "IC describes not reopening or formally reassessing the IAP despite the new specialist flag, treating the original plan as the default absent a strong forcing event.",
        "plausible_nonbias_interpretation": "Continuous re-planning during active suppression can itself be disruptive; sticking with a plan can reflect disciplined execution.",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "default option", "inertia"]
      },
      {
        "instance_id": "bw_01",
        "bias": "Bandwagon Effect",
        "decision_point": 3,
        "mechanism": "IC weights the tactical judgment of continuing the offensive attack more heavily because multiple mutual-aid officers on the shared radio net vocally support it, treating the number of agreeing voices as evidence of correctness.",
        "affected_reasoning_operation": "Evidence-selection / social-proof-driven inference from radio traffic",
        "evidence_available_at_time": ["Multiple mutual-aid officers voicing agreement on the net"],
        "required_textual_manifestation": "IC cites the fact that several other officers agreed on the radio as a reason reinforcing the continuation decision, separate from the command-post internal dynamics.",
        "plausible_nonbias_interpretation": "Peer officers' input is a legitimate collaborative input in multi-agency incidents.",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon effect", "social proof", "peer consensus bias"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 3,
        "mechanism": "Within the internal command post, the safety officer's dissenting concern is raised but not substantively engaged, and the small command team reaches rapid unanimous agreement, reflecting suppressed dissent and an illusion of unanimity distinct from the external radio-based bw_01 dynamic.",
        "affected_reasoning_operation": "Internal group deliberation / dissent handling in the command post",
        "evidence_available_at_time": ["Safety officer's verbal exposure-risk concern at the command post", "Absence of a formal risk re-assessment log"],
        "required_textual_manifestation": "IC describes the command post's brief internal discussion in which the safety officer's concern is acknowledged but not pursued, and the team quickly aligns on continuing.",
        "plausible_nonbias_interpretation": "Efficient, decisive command-post communication is valued during active incidents and can look similar to suppressed dissent without being biased.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "illusion of unanimity", "self-censorship"]
      },
      {
        "instance_id": "mr_01",
        "bias": "Modality effect or Recency effect",
        "decision_point": 4,
        "mechanism": "IC gives disproportionate practical weight to the single most recently received verbal report ('looks stable now') relative to a 20-minute, repeatedly radioed instrument trend showing a steady temperature rise, when timing the withdrawal order.",
        "affected_reasoning_operation": "Final evidence-weighting / withdrawal-timing decision",
        "evidence_available_at_time": ["20-minute logged instrument trend of rising shell temperature", "Single most recent spotter verbal report of apparent stability"],
        "required_textual_manifestation": "IC explains delaying the withdrawal call by referencing the latest verbal update as more decisive than the accumulated trend data leading up to it.",
        "plausible_nonbias_interpretation": "A trained visual spotter's real-time report is a legitimate, sometimes more current, data point than a lagging instrument trend.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "modality effect", "most recent information bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable — condition is 'biased', not a control condition."
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
      "Confirm exactly 4 decision points are present in the timeline",
      "Confirm each of the 7 instance IDs maps to exactly one decision point and one distinct evidence source",
      "Confirm decision points 1, 2, and 3 each carry exactly two instances with clearly distinct evidence sources or reasoning operations, and decision point 4 carries exactly one",
      "Confirm no bias term, definition, or explicit psychological label appears in any interviewee-facing text",
      "Confirm each instance has a plausible non-bias interpretation available in the narrative",
      "Confirm consequences at the end (tank vents without catastrophic failure) do not mechanically prove or disprove any bias",
      "Confirm total word count target of 1,350 (range 1,215–1,485) is achievable given 4 decision points, probes, and 7 non-repetitive instance manifestations"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Representative heuristic", "occurrences": 1, "mechanism_constraint": "Superficial visual/pattern similarity to a prior incident overriding contents/base-rate verification"},
      {"bias": "Sunk cost bias", "occurrences": 1, "mechanism_constraint": "Justification via already-committed resources (crews/hoselines) rather than current risk data"},
      {"bias": "Status quo bias", "occurrences": 1, "mechanism_constraint": "Default continuation of existing IAP absent formal re-evaluation trigger"},
      {"bias": "Framing effect", "occurrences": 1, "mechanism_constraint": "Verbal dispatch label anchoring initial severity framing"},
      {"bias": "Bandwagon Effect", "occurrences": 1, "mechanism_constraint": "Weighting of tactical judgment based on number of agreeing external radio voices"},
      {"bias": "Modality effect or Recency effect", "occurrences": 1, "mechanism_constraint": "Overweighting the single most recent verbal report relative to accumulated instrument trend"},
      {"bias": "Groupthink", "occurrences": 1, "mechanism_constraint": "Suppressed dissent and rapid unanimity within the internal command post"}
    ],
    "target_bias_names": [
      "Representative heuristic",
      "Sunk cost bias",
      "Status quo bias",
      "Framing effect",
      "Bandwagon Effect",
      "Modality effect or Recency effect",
      "Groupthink"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Representative heuristic", "requested_occurrences": 1},
      {"bias": "Sunk cost bias", "requested_occurrences": 1},
      {"bias": "Status quo bias", "requested_occurrences": 1},
      {"bias": "Framing effect", "requested_occurrences": 1},
      {"bias": "Bandwagon Effect", "requested_occurrences": 1},
      {"bias": "Modality effect or Recency effect", "requested_occurrences": 1},
      {"bias": "Groupthink", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "rh_01", "bias": "Representative heuristic"},
      {"instance_id": "fr_01", "bias": "Framing effect"},
      {"instance_id": "sc_01", "bias": "Sunk cost bias"},
      {"instance_id": "sq_01", "bias": "Status quo bias"},
      {"instance_id": "bw_01", "bias": "Bandwagon Effect"},
      {"instance_id": "gt_01", "bias": "Groupthink"},
      {"instance_id": "mr_01", "bias": "Modality effect or Recency effect"}
    ],
    "intended_decision_points": [
      {"instance_id": "rh_01", "bias": "Representative heuristic", "decision_point": 1},
      {"instance_id": "fr_01", "bias": "Framing effect", "decision_point": 1},
      {"instance_id": "sc_01", "bias": "Sunk cost bias", "decision_point": 2},
      {"instance_id": "sq_01", "bias": "Status quo bias", "decision_point": 2},
      {"instance_id": "bw_01", "bias": "Bandwagon Effect", "decision_point": 3},
      {"instance_id": "gt_01", "bias": "Groupthink", "decision_point": 3},
      {"instance_id": "mr_01", "bias": "Modality effect or Recency effect", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "rh_01",
        "bias": "Representative heuristic",
        "mechanism": "Classifying the current fire as the same category as a prior resolved incident based on superficial visual resemblance, bypassing contents/base-rate verification",
        "affected_reasoning_operation": "Situation classification prior to strategy selection",
        "evidence_source": "Visual smoke column comparison to a specific prior incident",
        "distinctiveness_requirement": "Must be tied to a specific named prior incident and visual cue, not merely 'experience says so'"
      },
      {
        "instance_id": "fr_01",
        "bias": "Framing effect",
        "mechanism": "Anchoring risk framing on the dispatcher's specific verbal label ('contained') independent of the visual/manifest ambiguity",
        "affected_reasoning_operation": "Initial risk framing from a verbal report",
        "evidence_source": "Dispatch radio wording",
        "distinctiveness_requirement": "Must reference the dispatcher's specific language as the operative frame, distinct from rh_01's visual pattern-match"
      },
      {
        "instance_id": "sc_01",
        "bias": "Sunk cost bias",
        "mechanism": "Justifying continuation of interior positions by reference to already-invested crews/hoselines rather than current risk data",
        "affected_reasoning_operation": "Resource-continuation decision under new alarm data",
        "evidence_source": "Deployed crews and hoselines already in place",
        "distinctiveness_requirement": "Must explicitly invoke the cost/effort already spent, distinct from sq_01's absence-of-trigger reasoning"
      },
      {
        "instance_id": "sq_01",
        "bias": "Status quo bias",
        "mechanism": "Defaulting to the original IAP without formal re-evaluation, absent an explicit forcing prompt",
        "affected_reasoning_operation": "Plan-maintenance / failure to trigger reassessment",
        "evidence_source": "Structural/hazmat specialist's new temperature-trend flag on adjacent tank",
        "distinctiveness_requirement": "Must show the plan continuing purely because no formal review was reopened, not because of resource investment"
      },
      {
        "instance_id": "bw_01",
        "bias": "Bandwagon Effect",
        "mechanism": "Weighting continuation decision by the number of externally agreeing mutual-aid officers on the radio net",
        "affected_reasoning_operation": "Evidence-selection via social proof from external radio traffic",
        "evidence_source": "Multiple mutual-aid officer voices on shared net",
        "distinctiveness_requirement": "Must be external, multi-officer, radio-based agreement, distinct from gt_01's internal command-post dynamic"
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Suppressing/under-engaging the safety officer's internal dissent and reaching rapid unanimous agreement within the small command post",
        "affected_reasoning_operation": "Internal group deliberation and dissent handling",
        "evidence_source": "Safety officer's verbal concern at command post, unresolved",
        "distinctiveness_requirement": "Must be internal command-team dynamic with a specific dissenting individual, distinct from bw_01's external social-proof mechanism"
      },
      {
        "instance_id": "mr_01",
        "bias": "Modality effect or Recency effect",
        "mechanism": "Overweighting the single most recently received verbal report relative to a longer accumulated instrument trend when timing the withdrawal decision",
        "affected_reasoning_operation": "Final evidence-weighting for withdrawal timing",
        "evidence_source": "Most recent spotter verbal report vs. 20-minute instrument trend log",
        "distinctiveness_requirement": "Must explicitly contrast the most-recent single report against the accumulated trend data"
      }
    ],
    "intended_strength": [
      {"instance_id": "rh_01", "bias": "Representative heuristic", "strength": "subtle"},
      {"instance_id": "fr_01", "bias": "Framing effect", "strength": "subtle"},
      {"instance_id": "sc_01", "bias": "Sunk cost bias", "strength": "subtle"},
      {"instance_id": "sq_01", "bias": "Status quo bias", "strength": "subtle"},
      {"instance_id": "bw_01", "bias": "Bandwagon Effect", "strength": "subtle"},
      {"instance_id": "gt_01", "bias": "Groupthink", "strength": "subtle"},
      {"instance_id": "mr_01", "bias": "Modality effect or Recency effect", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Biased_6",
    "domain_id": "HE",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across the 4 mandated decision points by mechanism fit and narrative realism: decision point 1 received the two initial size-up biases (representative heuristic, framing effect) sharing the initial classification moment but drawing on distinct evidence sources (visual pattern vs. dispatch wording); decision point 2 received the two continuation biases (sunk cost, status quo) distinguished by resource-justification vs. absence-of-reassessment reasoning; decision point 3 received the two social/consensus biases (bandwagon, groupthink) distinguished by external radio social-proof vs. internal command-post dissent suppression; decision point 4 received the single recency/modality instance tied to the final withdrawal-timing evidence contrast. No decision point received more than two instances of any single bias, and all co-located pairs use distinct evidence sources per the instance independence rule.",
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
          "segment_type": "visual situation classification and strategy rationale",
          "raw_interview_anchor": "Visually it looked almost identical to a fire we had three years back ... So my first read was, this looks like that one.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rh_01"
          ],
          "ground_truth_rationale": "The participant classifies the current fire from a specific prior incident using superficial visual similarity before contents are confirmed."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "objective and priority rationale",
          "raw_interview_anchor": "Get the fire knocked down before it could threaten the second tank or the production building next door, and do it without losing anybody.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a standard life-safety, stabilization, and property-protection objective without a hidden bias mechanism."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "verbal risk framing and information-prioritization rationale",
          "raw_interview_anchor": "The call came through as contained ... getting the manifest nailed down didn't feel like something I had to sort out before we started moving lines in.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "fr_01"
          ],
          "ground_truth_rationale": "The dispatcher's specific 'contained' wording is treated as an operative low-severity frame despite unconfirmed contents."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "plan monitoring and reassessment rationale",
          "raw_interview_anchor": "It should have, and it registered, but we were already committed ... the plan stayed as it was; we didn't stop and rebuild the IAP.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sq_01"
          ],
          "ground_truth_rationale": "The original IAP continues because no formal stop or reassessment is triggered after material new hazard information."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "resource-continuation rationale under alarm data",
          "raw_interview_anchor": "We already had people and hose in position — pulling that back felt like giving up ground we'd already paid for.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sc_01"
          ],
          "ground_truth_rationale": "Continuation is partly justified by already-invested setup time, crews, hose, and risk."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "internal dissent handling and consensus rationale",
          "raw_interview_anchor": "Everybody sort of nodded that we were fine to continue ... Nobody asked him to lay out specifically what he was seeing ... it just didn't come back up.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gt_01"
          ],
          "ground_truth_rationale": "The command post acknowledges but does not substantively test the safety officer's dissent before reaching rapid agreement."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "external social-proof evidence weighting",
          "raw_interview_anchor": "When you've got multiple experienced officers on the net independently saying the same thing, that carries weight.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "bw_01"
          ],
          "ground_truth_rationale": "Multiple agreeing mutual-aid officers on the shared radio net reinforce continuation of the existing tactical interpretation."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "final evidence integration and withdrawal timing",
          "raw_interview_anchor": "The spotter's call was the most current thing I had in my ear ... I let one fresh comment outweigh a much longer pattern that had already told a consistent story.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "mr_01"
          ],
          "ground_truth_rationale": "A single recent verbal report is weighted over a sustained twenty-minute instrument trend in the withdrawal decision."
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
    "analysis_scope_note": "Conservative, mechanism-level review of the interview transcript for affirmative cognitive bias occurrences. No experimental condition or benchmark hypothesis considered."
  },
  "identified_bias_summary": [
    {
      "bias_label": "groupthink",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "social proof",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": ["representative heuristic", "similarity heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the probability or category of an event by its superficial similarity to a stored prototype or prior instance, while underweighting unique or base-rate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial size-up and offensive attack commitment",
      "decision_point_description": "Whether to commit crews to offensive foam attack before confirming the actual product in the burning tank.",
      "affected_reasoning_operation": "Categorization and probabilistic judgment of the incident type",
      "bias_specific_mechanism": "The participant categorized the current tank fire as equivalent to a visually similar prior fire, using superficial perceptual similarity to override uncertainty about the actual product identity.",
      "manifestation_in_interview": "The participant explicitly linked the current heavy black column and rough intensity to a prior successful offensive attack and proceeded without confirmed manifest information.",
      "effect_on_reasoning_or_decision": "Led to an offensive commitment based on perceived similarity before product identity was established.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Visually it looked almost identical to a fire we had three years back in the same general area — same kind of column, same rough intensity. That one we knocked down clean with an offensive foam attack, crews in with exposure lines, no real drama. So my first read was, this looks like that one.",
          "evidence_explanation": "This shows similarity-based classification substituting for a confirmed assessment of the current event."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But the call came through as contained, and visually it read the same as the one I already knew how to fight, so I went with what I had. Honestly, hearing it called contained made it sound like it was staying inside the kind of tank fire we handle all the time — so getting the manifest nailed down didn't feel like something I had to sort out before we started moving lines in.",
          "evidence_explanation": "The participant used the 'contained' description and visual similarity as sufficient evidence to proceed, reducing the perceived need for disconfirming product information."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the product was not confirmed before moving lines in. The later hazmat report disconfirmed the assumed similarity, but the bias operated at the initial commitment point.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context. Classification relies on established cognitive-science knowledge of the representativeness heuristic.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": ["sunk cost effect", "escalation of commitment"],
      "taxonomy_status": "established_label",
      "bias_definition": "Continuing a course of action because resources have already been invested, even when forward-looking evaluation no longer supports continuation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Mid-attack response to hazmat product identification and rising shell temperatures",
      "decision_point_description": "Whether to continue the offensive attack and add a second foam line, or withdraw to a defensive posture after new risk information and rising temperature alarms.",
      "affected_reasoning_operation": "Cost-benefit and withdrawal decision under risk",
      "bias_specific_mechanism": "The participant treated already committed personnel, hose, and setup effort as reasons to continue the attack rather than evaluating only forward-looking costs and benefits.",
      "manifestation_in_interview": "The participant stated that pulling back felt like giving up ground already paid for in setup time and risk.",
      "effect_on_reasoning_or_decision": "The attack was maintained and a second foam line was added instead of withdrawing, despite changing product and temperature information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It should have, and it registered, but we were already committed at that point. Pulling two charged lines and repositioning crews mid-attack isn't something you do lightly — there's real risk in that movement itself. So the plan stayed as it was; we didn't stop and rebuild the IAP around the new information, we just kept pushing the attack we'd already started.",
          "evidence_explanation": "The participant emphasizes being already committed and the cost of movement, while giving less weight to the changed risk picture."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Partly the alarms themselves, wanting more suppression on the seat of the fire. But honestly, part of it was that we already had people and hose in position — pulling that back felt like giving up ground we'd already paid for in terms of setup time and risk getting in.",
          "evidence_explanation": "This explicitly frames withdrawal as losing an investment already made, a hallmark of sunk cost reasoning."
        }
      ],
      "correction_or_counterevidence": "There was a legitimate forward-looking safety risk in repositioning charged lines, but the participant's own explanation also invokes irrecoverable setup cost and ground already paid for.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context. Classification relies on established cognitive-science knowledge of the sunk cost fallacy and escalation of commitment.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["plan continuation error", "cognitive fixation on plan"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to continue an existing plan even when new information and changing conditions suggest the plan should be reassessed or revised.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hazard information update and rising temperature alarms",
      "decision_point_description": "Whether to formally halt and reassess the incident action plan after the volatile-product report and climbing shell temperatures.",
      "affected_reasoning_operation": "Plan review and revision decision",
      "bias_specific_mechanism": "The participant and command post continued the previously briefed plan because no single formal trigger or explicit stop-and-reassess occurred, despite accumulating indicators that together warranted review.",
      "manifestation_in_interview": "The participant reported that the plan was reviewed only once at the start and that later risk information did not force a formal reassessment.",
      "effect_on_reasoning_or_decision": "The team continued executing the original plan without a structured fresh assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd only really sat down and reviewed the plan once, right at the start. Nothing after that forced a formal stop-and-reassess — no single trigger big enough on its own — so we just kept executing what we'd already briefed. Looking back, the volatile-product call and the climbing temperature together probably should have been enough to warrant a fresh look, but since nobody formally called for a stop, we treated that as reason enough to keep running with the plan we already had.",
          "evidence_explanation": "This shows continued plan execution without a formal re-evaluation step, even though accumulating cues crossed a threshold the participant later recognized."
        }
      ],
      "correction_or_counterevidence": "Absence of a single formal trigger is a procedural factor, but the participant's own account indicates multiple accumulating risk indicators were available and were not used to force a formal reassessment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context. Classification relies on established cognitive-science knowledge of plan continuation bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "social proof",
      "alternative_labels": ["informational social influence", "consensus heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Using others' behavior or expressed judgments as evidence for the correct course of action, especially under uncertainty.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Middle-phase assessment of attack posture with mutual aid radio traffic",
      "decision_point_description": "Whether to continue the interior attack in light of external mutual aid officer agreement and the safety officer's concern.",
      "affected_reasoning_operation": "Integration of social information into operational decision-making",
      "bias_specific_mechanism": "The participant weighted multiple experienced officers' agreement on the radio as reinforcing evidence that the current course was correct, rather than treating it as one more input requiring independent verification.",
      "manifestation_in_interview": "The participant said the agreement carried weight and reinforced that they were reading the incident the way most people were reading it.",
      "effect_on_reasoning_or_decision": "Increased confidence in continuing the interior attack and reduced the perceived need to scrutinize the safety officer's concern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The mutual aid engine companies were on our shared channel, and a couple of their officers came on saying it looked like a standard tank fire, keep pushing the interior attack. Multiple voices, same read.",
          "evidence_explanation": "The participant noted multiple external voices endorsing the current course."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, some. When you've got multiple experienced officers on the net independently saying the same thing, that carries weight. It reinforced that we were reading the incident the way most people out there were reading it.",
          "evidence_explanation": "This shows social consensus being used as confirmation of the participant's own approach."
        }
      ],
      "correction_or_counterevidence": "Consulting experienced officers can be legitimate, but the bias operated by using agreement as reinforcing consensus rather than testing the current plan independently.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context. Classification relies on established cognitive-science knowledge of social proof and consensus heuristics.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "groupthink",
      "alternative_labels": ["group conformity", "illusion of unanimity"],
      "taxonomy_status": "established_label",
      "bias_definition": "A group decision-making style in which consensus and harmony override realistic appraisal of dissenting views or risk information.",
      "attributed_to_speaker": "Participant and command post group",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Command post discussion of safety officer's exposure concern",
      "decision_point_description": "Whether to investigate the safety officer's concern about crew proximity to the second tank and reconsider the current position.",
      "affected_reasoning_operation": "Group evaluation of dissenting risk information",
      "bias_specific_mechanism": "The command post group acknowledged the safety officer's concern but moved quickly to consensus without structured follow-up, devil's advocacy, or detailed exploration of the dissenting observation.",
      "manifestation_in_interview": "The participant described everyone nodding that they were fine to continue and no one asking the safety officer to explain the concern in detail.",
      "effect_on_reasoning_or_decision": "The safety concern was not rigorously tested, and the group remained committed to the existing plan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We acknowledged it, but the room moved fast — everybody sort of nodded that we were fine to continue, and we didn't really dig into it past that. It wasn't dismissed outright, it just didn't get a long conversation before we moved on.",
          "evidence_explanation": "This shows rapid movement toward consensus without deep evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really. Nobody asked him to lay out specifically what he was seeing or walk us through why he thought the exposure risk was higher than we'd assessed. No one was assigned to argue the other side or double-check it. Once the room had settled on continuing, it just didn't come back up.",
          "evidence_explanation": "This indicates absence of structured dissent-checking or assigned red-team behavior, a groupthink feature."
        }
      ],
      "correction_or_counterevidence": "The concern was not dismissed outright, and time pressure may have been real, but the absence of any structured follow-up or devil's advocacy suggests the group over-weighted consensus.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context. Classification relies on established cognitive-science knowledge of groupthink.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency bias",
      "alternative_labels": ["recency effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Overweighting the most recently presented information relative to longer-run trends or prior information when making judgments or decisions.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final withdrawal decision after spotter report",
      "decision_point_description": "Whether to order full withdrawal based on a consistent twenty-minute rising shell temperature trend versus a newer spotter visual report that the tank looked stable.",
      "affected_reasoning_operation": "Weighting of trend data versus latest spotter observation",
      "bias_specific_mechanism": "The participant allowed the most recent spotter comment to outweigh a longer consistent instrument trend because it was temporally salient and current at the decision moment.",
      "manifestation_in_interview": "The participant held off on withdrawal longer than the trend alone justified, citing the spotter's latest stability report as carrying weight because it was the most current input.",
      "effect_on_reasoning_or_decision": "Delayed the full withdrawal decision despite a longer consistent temperature trend.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd had a shell temperature trend on that second tank climbing steadily for about twenty minutes, radioed in multiple times, consistent rise. Then right at the point where I was deciding whether to call full withdrawal, a spotter came on and said it looked stable now, based on a quick visual check.",
          "evidence_explanation": "The contrast between the longer trend and the newer report is established."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The spotter's call was the most current thing I had in my ear at that exact moment, so it carried real weight in the decision. I held off on ordering the full pull-back a bit longer than the trend alone probably would have justified, because that last report suggested things had settled.",
          "evidence_explanation": "This directly identifies temporal recency as the reason the spotter report was overweighted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The twenty-minute trend, honestly. It was right there the whole time. I let one fresh comment outweigh a much longer pattern that had already told a consistent story.",
          "evidence_explanation": "The participant explicitly contrasts one fresh comment with a longer consistent pattern and identifies the distortion."
        }
      ],
      "correction_or_counterevidence": "A direct visual check can add diagnostic value, but the participant's own statement acknowledges that the fresh comment outweighed the longer trend rather than being integrated with it.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided in the RAG context. Classification relies on established cognitive-science knowledge of the recency bias or recency effect.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied in the RAG context; bias labels and definitions are based on established cognitive-science knowledge rather than corpus-grounded citations.",
    "The analysis uses a single interview transcript and does not rely on post-incident outcome information to impute bias.",
    "Some episodes involve overlapping individual and group mechanisms, which were separated conservatively at the narrowest decision point available."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Biased_7_Gemini_off",
  "interview_id": "HE_Biased_7",
  "system_prompt_id": "Gemini",
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
