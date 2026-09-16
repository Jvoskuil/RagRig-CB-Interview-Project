You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this conversation being recorded and used for after-action training purposes, not for any personnel evaluation.

Participant: Yeah, that's fine. I've done these debriefs before.

Interviewer: Can you tell me your role and what you were responsible for when this incident started?

Participant: I'm the Situation Unit Analyst for the county EOC. My job during an activation is to build and maintain the Common Operating Picture — pulling in field reports, sensor data, weather, whatever's coming in — and turning that into something the Branch Directors and the EOC Director can actually make calls from. That night I was covering both the flood side and keeping an eye on the fire branch, since Ridge Fire was still active and eating into our smoke-camera and aerial coverage.

Interviewer: Walk me through how the incident began.

Participant: It started with a notice from the Twin Forks Reservoir Authority around 9 PM. They said they were doing a controlled precautionary release ahead of the storm cell that was coming in — basically getting ahead of it so the reservoir wouldn't be over capacity when the rain hit. Our downstream gauges at that point were showing a gradual rise, nothing dramatic. The duty hydrologist was tied up on another call and wasn't going to be free for at least ninety minutes, so I didn't have anyone to sanity-check the numbers against. Our flood Branch Director, who's been doing this about twenty years, looked at the same notice and said this was a routine pattern, that he'd seen the reservoir do exactly this kind of release two or three times before.

Interviewer: What did you decide to do with that information?

Participant: I recommended we go with a monitor-and-prepare advisory rather than jump straight to a warning for Sector 7. The operator's language was pretty clearly framed as precautionary — they used the word "controlled" a couple times — and combined with the Director's read that this looked routine, it felt like the proportionate response. I remember thinking, if this were really an emergency release they wouldn't be calling it precautionary.

Interviewer: Did you consider verifying that independently before finalizing the advisory?

Participant: I thought about it, but with the hydrologist unavailable and the Director being pretty confident, it seemed like it would just slow things down without adding much. He's the one who signs off on tier decisions normally, and I trusted his read given how long he's been doing this.

Interviewer: What happened next?

Participant: About ninety minutes later the gauges spiked hard — much faster than the operator's language had implied. The release turned out to be a lot bigger than "controlled precautionary" suggested. That's when things started moving fast.

Interviewer: Let's talk about the resource request that followed. What was happening at that point?

Participant: Our field liaison started getting scattered water-rescue calls, but only in two sub-neighborhoods — small numbers, really consistent with a standard tier-1 response. At the same time I was hearing fire dispatch chatter using radio codes that sounded almost identical to what we used during the 2018 flash flood two counties over, the one with multiple fatalities. I'd helped coordinate the tier-3 mobilization on that one.

Interviewer: How did that connection affect your recommendation?

Participant: Honestly, it hit me pretty hard. I remember thinking, this feels like 2018 again, and I didn't want to be caught understaffed like we almost were back then. So I recommended a full tier-3 mobilization — extra swift-water teams, extra staging — even though the actual call volume we had in front of us was only tier-1 level.

Interviewer: Did the current data support tier-3 on its own?

Participant: Not really, no. If you just looked at the confirmed calls, tier-1 would've covered it. But that memory was loud in my head.

Interviewer: What ended up happening with those resources?

Participant: The rescue calls plateaued at basically tier-1 volume. So we had tier-3 assets sitting partly idle for a few hours, which the fire branch wasn't thrilled about since they needed some of that same equipment.

Interviewer: Let's move to the evacuation zone decision. What information did you have at that stage?

Participant: This was the rough part. Six of our eight stream gauges were down — the repeater got knocked out by Ridge Fire smoke interference — so I only had two gauges reporting, and both were showing a sharp rise over about twenty minutes. Around the same time, videos of flooding at one intersection started circulating on social media and a regional news account picked it up and ran with it. That clip kept popping up everywhere — I must've seen it shared four or five times through different channels — and after a while it started feeling like the flooding was happening all over, even though it was really just the one intersection.

Interviewer: How did you put that together into a recommendation?

Participant: I built out a flood-extent map using the two gauges plus that footage, and honestly, it all fit together really cleanly — the trend line, the video, the timing. It told a clear, coherent story, and I felt confident recommending we expand the evacuation to the whole multi-sector watershed area rather than just the sub-zones next to those two gauges.

Interviewer: Did you weigh how much of the watershed those two gauges actually represented?

Participant: I mean, two out of eight isn't the full picture, but they were both moving in the same direction, so I took that as a strong enough signal for the whole area. Getting people out ahead of a flood is better than being late, so I leaned toward the wider expansion.

Interviewer: What came out of that afterward?

Participant: Once the backup gauges came back online later that night, it turned out two of the newly evacuated sub-zones never actually exceeded minor flood stage. So the expansion was broader than what materialized, though obviously nobody could've known that for certain in the moment.

Interviewer: Let's go to the hot-wash review. What was discussed there?

Participant: We went back over the original advisory decision — the one from the start of the night — now that we knew how bad it actually got. Reading the operator's notice again, with everything we now know, it seemed like the signs were pretty clearly there. The scale of what happened felt like it should have been obvious from that notice alone.

Interviewer: When you say "obvious," obvious based on what was known that night, or knowing how it turned out?

Participant: Looking back at it now, it just reads differently. Knowing what happened after, the wording in that notice looks like it was underselling things pretty clearly.

Interviewer: If the operator's notice had used different language that night — less "controlled," more urgent — do you think your initial recommendation would have changed?

Participant: Probably, yeah. If it had said something like "emergency release" instead of "precautionary," I think I'd have pushed harder for a warning tier instead of an advisory, regardless of what the Director's initial read was.

Interviewer: And if all eight gauges had stayed online through the evacuation decision, would that have changed things?

Participant: I'd like to think I'd have waited for a fuller picture instead of leaning as hard on those two data points and the footage. With full coverage I probably wouldn't have needed the video to fill in the gaps at all.

Interviewer: Looking back across the whole night, how do you separate what you actually knew in the moment from what became clear afterward?

Participant: It's harder than it sounds. In the moment you're working with partial data and you're making the best call you can with what's in front of you. It's only once you have the full outcome that certain things start looking like they should have been flagged earlier — but I try to remind myself that clarity came from hindsight, not from anything I necessarily missed in real time.

Interviewer: That's a good place to stop. Thanks for walking through this in detail.

Participant: Sure, happy to help however this gets used.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Biased_7",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Emergency Operations Center (EOC) Situation Unit Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Twin Forks Flash Flood and Ridge Fire Smoke Incident",
    "scenario_summary_internal": "Over a 14-hour operational period, a Situation Unit Analyst at a county EOC manages the Common Operating Picture during a compound event: an unplanned high-volume release from Twin Forks Reservoir coincides with a monsoonal storm cell and reduced aerial/sensor visibility from active Ridge Fire smoke. The analyst must classify the threat and decide on public warning tier, mobilize rescue resources, decide on evacuation zone expansion using degraded sensor coverage, and later participate in a hot-wash review of the initial decision after the outcome is known.",
    "occupational_realism": {
      "objective": "Maintain an accurate, timely Common Operating Picture and recommend warning/evacuation/resource decisions that protect life safety under degraded information conditions.",
      "setting": "County Emergency Operations Center, Situation Unit, during a compound flash-flood and wildfire-smoke incident affecting a river-adjacent residential sector (Sector 7-12 watershed).",
      "constraints": [
        "Two of eight stream gauges offline due to smoke-damaged repeater",
        "Duty hydrologist unavailable for first 90 minutes",
        "Aerial reconnaissance limited by wildfire smoke",
        "Dual-hazard workload competing for EOC attention (fire branch and flood branch)",
        "Public messaging must go through a single unified tone to avoid contradicting the dam operator's release notice"
      ],
      "stakeholders": [
        "Twin Forks Reservoir Authority dam operator",
        "EOC Branch Director (flood operations)",
        "Field liaison / incident commander at Sector 7",
        "Fire dispatch (Ridge Fire)",
        "Regional news/social media monitoring desk",
        "Downstream Sector 7-12 residents"
      ],
      "technical_terms_to_use": [
        "Common Operating Picture (COP)",
        "stream gauge threshold",
        "tier-1/tier-3 mobilization",
        "advisory vs. warning tier",
        "watershed sub-zone",
        "hot-wash review",
        "swift-water rescue asset"
      ],
      "technical_terms_to_avoid": [
        "illusion of validity",
        "availability heuristic",
        "authority bias",
        "framing effect",
        "hindsight bias",
        "insensitivity to sample size",
        "any explicit cognitive-bias terminology or psychological jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dam operator notice describes the release as a 'controlled precautionary release to manage reservoir levels ahead of the storm system'",
          "Downstream gauge readings show a gradual, modest level rise consistent with routine operations",
          "Duty hydrologist is unavailable for independent verification",
          "The flood Branch Director, a respected 20-year veteran, states this pattern 'is routine, we've seen this before'"
        ],
        "alternatives": [
          "Issue an immediate evacuation warning for low-lying Sector 7",
          "Issue a lower-tier 'monitor and prepare' advisory only",
          "Hold any public messaging pending independent hydrological verification"
        ],
        "intended_action": "Analyst adopts the advisory-only tier, deferring to the Branch Director's framing and the dam operator's characterization without requesting independent verification.",
        "new_information_after_decision": [
          "Within 90 minutes, gauge levels exceed the warning threshold rapidly",
          "The release volume was substantially larger than the 'controlled' framing implied"
        ]
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Field liaison reports scattered water-rescue calls in two sub-neighborhoods, consistent with tier-1 staffing",
          "Fire dispatch chatter uses radio codes similar to those from a widely publicized 2018 neighboring-county mass-casualty flash flood the analyst helped coordinate",
          "No new gauge or rainfall data has arrived since the last COP update"
        ],
        "alternatives": [
          "Request a standard tier-1 rescue package matching current confirmed calls",
          "Request a large tier-3 mobilization sized to match the recalled 2018 event",
          "Hold current staffing and reassess in 30 minutes"
        ],
        "intended_action": "Analyst requests tier-3 mobilization, sized to the vividly remembered 2018 event rather than the smaller confirmed current call volume.",
        "new_information_after_decision": [
          "Actual rescue calls plateau at a volume consistent with tier-1 need",
          "Tier-3 assets are partly idle, straining resources needed elsewhere for the fire branch"
        ]
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Only 2 of 8 planned stream gauges are transmitting; the rest are offline due to smoke-damaged repeaters",
          "Both reporting gauges show a sharp rise over a 20-minute window",
          "Social media videos of flooding at one visually dramatic intersection are circulating widely and being amplified by a regional news account",
          "The analyst's projected flood-extent map, built from the two gauges plus the viral footage, appears internally coherent and is presented with high confidence"
        ],
        "alternatives": [
          "Expand evacuation to the entire multi-sector watershed area based on the two gauges and viral footage",
          "Expand evacuation only to sub-zones adjacent to the two reporting gauges pending more data",
          "Request emergency deployment of backup gauge readings or aerial confirmation before expanding"
        ],
        "intended_action": "Analyst expands the evacuation order to the full multi-sector watershed area, expressing strong confidence in the derived flood map despite thin, unrepresentative sensor coverage.",
        "new_information_after_decision": [
          "Backup gauges are restored later and show two of the newly evacuated sub-zones never exceeded minor flood stage"
        ]
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The event has stabilized; full outcome data (major flooding, evacuations, resource strain) is now known",
          "EOC leadership convenes a hot-wash review of the Phase 1 advisory-only decision",
          "The dam operator's original notice wording is being re-read in light of what is now known"
        ],
        "alternatives": [
          "Conclude the original advisory decision was a clear, foreseeable error given 'obvious' warning signs in the notice",
          "Evaluate the Phase 1 decision using only the information that was available at that time",
          "Defer judgment pending full data reconciliation"
        ],
        "intended_action": "Analyst states the escalation 'should have been obvious' from the dam notice wording alone, reconstructing the earlier decision as clearly negligent in light of the now-known outcome.",
        "new_information_after_decision": []
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were responsible for when this incident began.",
        "What was your understanding of the operational objective at the start of your shift?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from the initial dam notice to the evacuation expansion.",
        "What information sources were feeding your Common Operating Picture at each stage?",
        "When did new information arrive relative to each decision you made?"
      ],
      "decision_point_probes": [
        "What cues stood out to you most at that moment, and why?",
        "What alternatives did you consider, and what ruled the others out?",
        "Whose input carried the most weight in that decision, and why?",
        "How confident were you in the picture you had at the time, and what was that confidence based on?",
        "What role did time pressure play in how you weighed the available data?",
        "Had you handled a similar situation before? How did that prior experience shape your read of this one?",
        "How much uncertainty did you feel you were operating under at that point?"
      ],
      "closing_hypotheticals": [
        "If the dam operator's notice had used different wording, do you think your initial call would have changed?",
        "If all eight gauges had been online throughout, would the evacuation decision have gone differently?",
        "Looking back now, how do you separate what was knowable at the time from what became clear afterward?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Framing Effect",
        "decision_point": 1,
        "mechanism": "The dam operator's positively-valenced characterization ('controlled precautionary release') shapes the analyst's threat classification more than the underlying gauge data would independently warrant.",
        "affected_reasoning_operation": "Threat-tier classification / risk categorization",
        "evidence_available_at_time": [
          "Dam operator notice text framed as routine/controlled",
          "Modest gradual gauge rise",
          "No independent hydrological verification yet obtained"
        ],
        "required_textual_manifestation": "Analyst explicitly references the operator's wording ('controlled,' 'precautionary') as the basis for choosing the lower advisory tier, rather than citing independent gauge trend analysis.",
        "plausible_nonbias_interpretation": "Given genuinely limited gradual gauge rise, an advisory tier could be a reasonable proportional response absent framing influence.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "wording bias", "anchoring on language"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Authority Bias",
        "decision_point": 1,
        "mechanism": "Analyst defers to the Branch Director's confident verbal assessment ('this is routine, we've seen this before') on the basis of the Director's seniority/title rather than independent verification of current data.",
        "affected_reasoning_operation": "Evidence weighting / deference in decision authorization",
        "evidence_available_at_time": [
          "Branch Director's verbal assurance, delivered with confidence and citing tenure",
          "Absence of the duty hydrologist to independently confirm"
        ],
        "required_textual_manifestation": "Analyst names the Director's experience/seniority as the specific reason for not seeking further verification before finalizing the advisory tier.",
        "plausible_nonbias_interpretation": "Trusting an experienced supervisor under time pressure is a normal chain-of-command heuristic in EOC operations.",
        "strength": "subtle",
        "do_not_make_explicit": ["authority bias", "deference to hierarchy", "credential-based trust"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "A vivid, personally salient memory of the 2018 mass-casualty flash flood (triggered by superficially similar radio codes) is used to size the current resource request instead of the actual current call volume.",
        "affected_reasoning_operation": "Resource-need estimation / prediction of rescue demand",
        "evidence_available_at_time": [
          "Current confirmed rescue calls limited to two sub-neighborhoods (tier-1 consistent)",
          "Radio chatter superficially resembling the 2018 event's codes",
          "No new gauge or rainfall data since last update"
        ],
        "required_textual_manifestation": "Analyst explicitly attributes the tier-3 mobilization request to the memory of the 2018 event ('this reminded me of...') rather than to current call-volume data.",
        "plausible_nonbias_interpretation": "Erring toward a larger mobilization could be framed as a defensible precautionary safety margin.",
        "strength": "moderate",
        "do_not_make_explicit": ["availability bias", "vivid memory", "recency/salience of recall"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Insensitivity to sample size",
        "decision_point": 3,
        "mechanism": "Analyst extrapolates a watershed-wide flood extent from only two of eight gauges (a small, non-representative sample) as though it were as reliable as full-network coverage.",
        "affected_reasoning_operation": "Statistical/spatial extrapolation from sensor data to a broader geographic conclusion",
        "evidence_available_at_time": [
          "Only 2 of 8 stream gauges transmitting",
          "Sharp 20-minute rise at those two gauges",
          "Six gauges offline with unknown readings"
        ],
        "required_textual_manifestation": "Analyst treats the two-gauge trend as sufficient basis for a full multi-sector watershed conclusion without qualifying the limited coverage.",
        "plausible_nonbias_interpretation": "Acting on partial data under time pressure is a defensible precautionary approach in life-safety contexts.",
        "strength": "moderate",
        "do_not_make_explicit": ["insensitivity to sample size", "small-sample extrapolation", "statistical representativeness"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Availability Bias",
        "decision_point": 3,
        "mechanism": "Widely circulated, emotionally vivid social-media/news footage of one dramatic flooded intersection disproportionately elevates the analyst's perceived severity and geographic scope of the flood, distinct from the earlier institutional-memory-based recall in cb_03.",
        "affected_reasoning_operation": "Severity/scope estimation from media salience rather than systematic sensor coverage",
        "evidence_available_at_time": [
          "Viral video/footage of one dramatic flooded intersection",
          "Amplification by a regional news account",
          "Sparse underlying gauge network"
        ],
        "required_textual_manifestation": "Analyst cites the viral footage's vividness or reach as adding confidence to expanding the evacuation zone, separate from and additional to the two-gauge data point.",
        "plausible_nonbias_interpretation": "Incorporating public-facing visual reports as a supplementary corroborating source is a legitimate multi-source verification practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability bias", "media salience", "vividness effect"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Illusion of Validity",
        "decision_point": 3,
        "mechanism": "Analyst expresses high subjective confidence in the internally coherent flood-extent map despite the map being built on thin, unrepresentative evidence; the coherence of the narrative substitutes for its actual predictive reliability.",
        "affected_reasoning_operation": "Confidence calibration in a predictive/inferential model",
        "evidence_available_at_time": [
          "Internally consistent flood-extent map assembled from two gauges and viral footage",
          "No cross-validation against the six offline gauges or aerial confirmation"
        ],
        "required_textual_manifestation": "Analyst describes feeling confident the map 'told a clear story' or 'all fit together,' explicitly linking that coherence to confidence in accuracy, despite acknowledging the thin data underlying it.",
        "plausible_nonbias_interpretation": "Producing a best-available operational picture under time constraints is standard EOC practice, and expressed confidence could reflect professional decisiveness rather than miscalibration.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of validity", "overconfidence from coherence", "narrative fallacy"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Hindsight bias",
        "decision_point": 4,
        "mechanism": "Knowing the eventual severe outcome, the analyst reconstructs the Phase 1 decision as having had 'obvious' warning signs, overestimating how foreseeable the escalation was from the information actually available at the time.",
        "affected_reasoning_operation": "Retrospective causal attribution / reconstruction of past decision quality",
        "evidence_available_at_time": [
          "Now-known full outcome data (major flooding, evacuations, resource strain)",
          "Re-reading of the original dam notice wording with outcome knowledge"
        ],
        "required_textual_manifestation": "Analyst states the escalation 'should have been obvious' from the original notice alone, without acknowledging that this judgment depends on information only available after the fact.",
        "plausible_nonbias_interpretation": "A genuinely reasonable after-action critique could identify real process gaps without inflating their foreseeability at the time.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "outcome knowledge distorting judgment", "creeping determinism"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition primary generation, no paired control specified in this call."
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
      "Confirm exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Confirm exactly 7 total bias instances are embedded: 1 Illusion of Validity, 1 Insensitivity to sample size, 1 Authority Bias, 2 Availability Bias, 1 Framing Effect, 1 Hindsight bias.",
      "Confirm no bias name, definition, or psychological label appears in the public interview text.",
      "Confirm the two Availability Bias instances (cb_03, cb_05) use distinct evidence sources (institutional memory of a past event vs. viral social-media footage) and occur at different decision points.",
      "Confirm decision point 3 contains three distinct bias instances (cb_04, cb_05, cb_06) with non-overlapping mechanisms and no repeated bias.",
      "Confirm each instance has a plausible non-bias explanation present in context so the bias is inferable, not asserted.",
      "Confirm hindsight bias (cb_07) is expressed only in the Phase 4 retrospective decision point and not leaked into earlier decision points or closing hypotheticals.",
      "Confirm total interview length falls within 1,215-1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals as required.",
      "Confirm consequences described do not mechanically prove bias (i.e., bad outcomes are shown as possible under both biased and non-biased reasoning)."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Illusion of Validity", "occurrences": 1, "mechanism_constraint": "Confidence must derive from narrative coherence of a thin-evidence flood map, not from accurate calibration."},
      {"bias": "Insensitivity to sample size", "occurrences": 1, "mechanism_constraint": "Must involve extrapolation from 2-of-8 gauges to a broader watershed conclusion."},
      {"bias": "Authority Bias", "occurrences": 1, "mechanism_constraint": "Must be tied to deference based on the Branch Director's seniority/title, not independent verification."},
      {"bias": "Availability Bias", "occurrences": 2, "mechanism_constraint": "Each instance must use a distinct evidence source: (1) personal institutional memory of a past event, (2) vivid circulated media footage."},
      {"bias": "Framing Effect", "occurrences": 1, "mechanism_constraint": "Must be tied to the dam operator's specific wording ('controlled precautionary release') shaping the tier decision."},
      {"bias": "Hindsight bias", "occurrences": 1, "mechanism_constraint": "Must occur only in the Phase 4 retrospective hot-wash review, using outcome knowledge to judge foreseeability."}
    ],
    "target_bias_names": [
      "Illusion of Validity",
      "Insensitivity to sample size",
      "Authority Bias",
      "Availability Bias",
      "Framing Effect",
      "Hindsight bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Illusion of Validity", "requested_occurrences": 1},
      {"bias": "Insensitivity to sample size", "requested_occurrences": 1},
      {"bias": "Authority Bias", "requested_occurrences": 1},
      {"bias": "Availability Bias", "requested_occurrences": 2},
      {"bias": "Framing Effect", "requested_occurrences": 1},
      {"bias": "Hindsight bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Framing Effect"},
      {"instance_id": "cb_02", "bias": "Authority Bias"},
      {"instance_id": "cb_03", "bias": "Availability Bias"},
      {"instance_id": "cb_04", "bias": "Insensitivity to sample size"},
      {"instance_id": "cb_05", "bias": "Availability Bias"},
      {"instance_id": "cb_06", "bias": "Illusion of Validity"},
      {"instance_id": "cb_07", "bias": "Hindsight bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Framing Effect", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Authority Bias", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Availability Bias", "decision_point": 2},
      {"instance_id": "cb_04", "bias": "Insensitivity to sample size", "decision_point": 3},
      {"instance_id": "cb_05", "bias": "Availability Bias", "decision_point": 3},
      {"instance_id": "cb_06", "bias": "Illusion of Validity", "decision_point": 3},
      {"instance_id": "cb_07", "bias": "Hindsight bias", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Framing Effect",
        "mechanism": "Threat-tier choice driven by the dam operator's positively-valenced wording rather than gauge trend analysis.",
        "affected_reasoning_operation": "Threat-tier classification",
        "evidence_source": "Dam operator release notice text",
        "distinctiveness_requirement": "Sole instance of Framing Effect; must not overlap with cb_02's authority-based mechanism even though co-located at decision point 1."
      },
      {
        "instance_id": "cb_02",
        "bias": "Authority Bias",
        "mechanism": "Deference to Branch Director's seniority/title in lieu of independent verification.",
        "affected_reasoning_operation": "Evidence weighting / authorization deference",
        "evidence_source": "Branch Director's verbal assurance",
        "distinctiveness_requirement": "Sole instance of Authority Bias; distinguished from cb_01 by relying on person-based credibility rather than message wording."
      },
      {
        "instance_id": "cb_03",
        "bias": "Availability Bias",
        "mechanism": "Resource sizing driven by vivid recall of the 2018 mass-casualty event triggered by superficial radio-code similarity.",
        "affected_reasoning_operation": "Resource-need estimation",
        "evidence_source": "Analyst's personal/institutional memory of a prior incident",
        "distinctiveness_requirement": "First of two Availability Bias instances; uses internally-recalled past-event memory as evidence source, distinct from cb_05's externally-sourced media footage."
      },
      {
        "instance_id": "cb_04",
        "bias": "Insensitivity to sample size",
        "mechanism": "Treating a 2-of-8 gauge sample as sufficient basis for a watershed-wide conclusion.",
        "affected_reasoning_operation": "Statistical/spatial extrapolation",
        "evidence_source": "Two functioning stream gauges out of eight",
        "distinctiveness_requirement": "Sole instance; distinguished from cb_06 (illusion of validity) by focusing on sample-size neglect rather than overall narrative-coherence confidence."
      },
      {
        "instance_id": "cb_05",
        "bias": "Availability Bias",
        "mechanism": "Perceived severity/scope inflated by vivid, widely circulated social-media footage of one flooded location.",
        "affected_reasoning_operation": "Severity/scope estimation",
        "evidence_source": "Viral social-media/news footage",
        "distinctiveness_requirement": "Second of two Availability Bias instances; uses externally-sourced viral media as evidence, distinct from cb_03's internally-recalled memory, and occurs at a different decision point."
      },
      {
        "instance_id": "cb_06",
        "bias": "Illusion of Validity",
        "mechanism": "High subjective confidence attributed to the internal coherence of the flood-extent map rather than its actual evidentiary reliability.",
        "affected_reasoning_operation": "Confidence calibration in predictive model",
        "evidence_source": "Self-assembled flood-extent map from gauges and footage",
        "distinctiveness_requirement": "Sole instance; distinguished from cb_04 by addressing confidence/coherence rather than sample-size neglect per se."
      },
      {
        "instance_id": "cb_07",
        "bias": "Hindsight bias",
        "mechanism": "Retrospective claim that the escalation was 'obvious' from Phase 1 information, using now-known outcome to judge past foreseeability.",
        "affected_reasoning_operation": "Retrospective causal attribution",
        "evidence_source": "Re-read of original dam notice combined with full outcome knowledge",
        "distinctiveness_requirement": "Sole instance; confined strictly to the Phase 4 retrospective decision point, must not appear in earlier decision points or closing hypotheticals."
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Framing Effect", "strength": "subtle"},
      {"instance_id": "cb_02", "bias": "Authority Bias", "strength": "subtle"},
      {"instance_id": "cb_03", "bias": "Availability Bias", "strength": "moderate"},
      {"instance_id": "cb_04", "bias": "Insensitivity to sample size", "strength": "moderate"},
      {"instance_id": "cb_05", "bias": "Availability Bias", "strength": "subtle"},
      {"instance_id": "cb_06", "bias": "Illusion of Validity", "strength": "moderate"},
      {"instance_id": "cb_07", "bias": "Hindsight bias", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Biased_7",
    "domain_id": "EM",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences spread across 4 decision points by mechanism fit and narrative realism: decision point 1 hosts framing/authority (message-framing and hierarchical trust both operate on the same initial classification act via different evidentiary channels); decision point 2 hosts one availability instance tied to internally recalled memory; decision point 3 hosts sample-size neglect, the second availability instance (externally-sourced media), and illusion of validity (confidence in the resulting synthesis), each addressing a distinct reasoning operation on distinct evidence; decision point 4 hosts hindsight bias exclusively, isolated to the retrospective review act. No bias exceeds two occurrences at any single decision point, and the two Availability Bias instances use fully independent evidence sources and occur at different decision points per the distinctiveness rule.",
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
          "segment_type": "Decision point 1: initial warning-tier classification",
          "raw_interview_anchor": "The operator calls it a 'controlled precautionary release'; the Branch Director says it is routine; the analyst recommends monitor-and-prepare and does not independently verify.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01",
            "cb_02"
          ],
          "ground_truth_rationale": "The analyst uses the operator's framing and the senior Director's confident assessment to choose an advisory-only response despite no independent hydrological check."
        },
        {
          "segment_id": "seg_dp2",
          "speaker": "Participant",
          "segment_type": "Decision point 2: rescue-resource mobilization",
          "raw_interview_anchor": "The analyst hears tier-1-level calls but says 'this feels like 2018 again' and recommends full tier-3 mobilization.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_03"
          ],
          "ground_truth_rationale": "The vivid 2018 flood memory, rather than current confirmed call volume, drives the resource estimate."
        },
        {
          "segment_id": "seg_dp3",
          "speaker": "Participant",
          "segment_type": "Decision point 3: evacuation-zone expansion",
          "raw_interview_anchor": "Six of eight gauges are down; two rise sharply; repeated video of one intersection feels representative; the analyst builds a coherent map and expands evacuation to the whole watershed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_04",
            "cb_05",
            "cb_06"
          ],
          "ground_truth_rationale": "The analyst generalizes from a two-gauge sample, lets widely repeated footage shape perceived scope, and treats a coherent composite story as sufficiently valid for a watershed-wide order."
        },
        {
          "segment_id": "seg_dp4",
          "speaker": "Participant",
          "segment_type": "Decision point 4: hot-wash review of the initial advisory",
          "raw_interview_anchor": "After the outcome is known, the analyst says the original notice reads as if the warning signs were obvious and that it undersold the danger.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_07"
          ],
          "ground_truth_rationale": "The retrospective judgment uses the known outcome to make the earlier risk appear clearly foreseeable."
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
    "analysis_scope_note": "Analysis of one interview transcript for affirmative evidence of bias-specific reasoning mechanisms. No retrieved scientific-paper passages were provided in the RAG context; bias labels draw on general cognitive-science knowledge rather than retrieved corpus evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "Hindsight bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which perceived likelihood, importance, or risk is shaped by how easily vivid or emotionally salient examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Resource request recommendation after scattered rescue calls and fire dispatch chatter",
      "decision_point_description": "Whether to recommend tier-3 mobilization or a lower response based on current confirmed rescue call volume.",
      "affected_reasoning_operation": "Risk appraisal and resource-allocation recommendation",
      "bias_specific_mechanism": "The salient, emotionally charged memory of the 2018 fatal flash flood became highly available after hearing similar fire dispatch codes, leading the participant to overestimate current escalation risk despite objective tier-1 call volume.",
      "manifestation_in_interview": "The participant explicitly reports that the 2018 memory was 'loud' in his head and drove a tier-3 mobilization even though current data only supported tier-1.",
      "effect_on_reasoning_or_decision": "The participant recommended full tier-3 mobilization, resulting in partly idle assets and some conflict with the fire branch over shared equipment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, it hit me pretty hard. I remember thinking, this feels like 2018 again, and I didn't want to be caught understaffed like we almost were back then. So I recommended a full tier-3 mobilization — extra swift-water teams, extra staging — even though the actual call volume we had in front of us was only tier-1 level.",
          "evidence_explanation": "Shows that a salient past event influenced the resource recommendation more than current objective call-volume data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. If you just looked at the confirmed calls, tier-1 would've covered it. But that memory was loud in my head.",
          "evidence_explanation": "Directly contrasts current low call volume with the subjective availability of the prior flood memory as the deciding driver."
        }
      ],
      "correction_or_counterevidence": "The participant recognized that current data supported tier-1, but this recognition did not change the recommendation at the time. Pre-positioning resources may also have some protective rationale, though not from the confirmed call volume.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided in the RAG context; the availability-heuristic label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "availability bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which judgments are shaped by how easily or vividly examples come to mind, rather than by a full evidence base.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evacuation zone expansion after partial stream-gauge outage and viral flood footage",
      "decision_point_description": "Whether to expand evacuation from sub-zones near the two reporting gauges to the whole multi-sector watershed area.",
      "affected_reasoning_operation": "Flood-extent estimation and protective-action recommendation",
      "bias_specific_mechanism": "Repeated exposure to one vivid single-intersection flooding video made that localized example mentally available as a proxy for widespread flooding, reducing weight given to the limited gauge coverage.",
      "manifestation_in_interview": "The participant said the clip 'kept popping up everywhere' and that it began to feel like flooding was happening all over, even though it was just one intersection. He then used the video with only two gauges to support a broad evacuation map.",
      "effect_on_reasoning_or_decision": "The participant recommended evacuating the whole multi-sector watershed; later backup gauges showed two newly evacuated sub-zones never exceeded minor flood stage.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That clip kept popping up everywhere — I must've seen it shared four or five times through different channels — and after a while it started feeling like the flooding was happening all over, even though it was really just the one intersection.",
          "evidence_explanation": "Explicitly links repeated exposure to a vivid single-location example with a subjective sense of widespread flooding."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I mean, two out of eight isn't the full picture, but they were both moving in the same direction, so I took that as a strong enough signal for the whole area.",
          "evidence_explanation": "Shows limited gauge data being treated as broadly representative, consistent with the availability-driven impression rather than a full-evidence flood-extent estimate."
        }
      ],
      "correction_or_counterevidence": "A precautionary motive may also have supported evacuation: the participant said getting people out early is better than being late. Later gauge data showed the expansion was broader than actual flooding, though this could not have been known with certainty at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided in the RAG context; the availability-heuristic label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect",
        "creeping determinism"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive an outcome as having been more foreseeable or obvious once the outcome is known.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hot-wash review of the original advisory decision",
      "decision_point_description": "Retrospective assessment of whether the reservoir operator's notice should have prompted a stronger initial warning.",
      "affected_reasoning_operation": "Retrospective evaluation of the original notice and initial advisory decision",
      "bias_specific_mechanism": "Knowledge of the later severe flooding made pre-outcome wording in the operator's notice appear more clearly indicative of severity than it did at the time of the initial decision.",
      "manifestation_in_interview": "The participant reported that with current outcome knowledge, the notice read differently and the scale of what happened seemed like it should have been obvious from the notice alone.",
      "effect_on_reasoning_or_decision": "The participant's after-action review judged the original advisory decision against outcome-informed clarity, potentially distorting whether the initial response was reasonable based on information available that night.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Reading the operator's notice again, with everything we now know, it seemed like the signs were pretty clearly there. The scale of what happened felt like it should have been obvious from that notice alone.",
          "evidence_explanation": "Shows outcome knowledge changing the perceived foreseeability of the event from the original notice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back at it now, it just reads differently. Knowing what happened after, the wording in that notice looks like it was underselling things pretty clearly.",
          "evidence_explanation": "Directly attributes the revised reading of the notice to hindsight rather than to information available at the time."
        }
      ],
      "correction_or_counterevidence": "The participant later showed some meta-awareness, saying he tries to remind himself that clarity came from hindsight rather than from something necessarily missed in real time. However, the hot-wash statements still displayed hindsight infringement in the moment of review.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific-paper passages were provided in the RAG context; the hindsight-bias label and mechanism derive from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Authority bias",
      "alternative_labels": [
        "authority heuristic",
        "expert deference"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial monitor-and-prepare advisory decision after the reservoir authority notice",
      "supporting_interview_quote": "He's the one who signs off on tier decisions normally, and I trusted his read given how long he's been doing this.",
      "plausible_mechanism": "Deference to the senior Branch Director's experience may have substituted for independent verification of the reservoir release notice, potentially lowering perceived risk.",
      "why_not_identified": "The Director's judgment was domain-relevant and potentially legitimate, and the hydrologist's unavailability created a practical constraint. The transcript does not clearly show a distinct authority-triggered distortion rather than reasonable consultation of an experienced decision-maker."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Framing effect",
      "alternative_labels": [
        "wording effect",
        "label framing"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial interpretation of the reservoir release notice as precautionary rather than emergent",
      "supporting_interview_quote": "The operator's language was pretty clearly framed as precautionary — they used the word 'controlled' a couple times — and combined with the Director's read that this looked routine, it felt like the proportionate response.",
      "plausible_mechanism": "The 'controlled precautionary' wording may have framed the release as non-emergency, making an advisory seem more appropriate than a warning.",
      "why_not_identified": "The language carried substantive operational meaning rather than being a purely equivalent frame variant, and no baseline demonstrates that the same underlying risk was presented differently. Therefore a framing effect is plausible but not affirmatively identified."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Only one participant's self-report was available; no independent incident records, decision logs, or other personnel accounts were available to verify reported decisions or outcomes.",
    "No retrieved scientific-paper passages were provided in the RAG context, so bias labels and mechanisms rely on general cognitive-science knowledge rather than the specified retrieved corpus.",
    "Several decisions occurred under genuine uncertainty, time pressure, and missing data, which may have non-bias explanations; the analysis seeks to distinguish those from affirmative bias-specific mechanisms."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Biased_7_Sonar_off",
  "interview_id": "EM_Biased_7",
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
