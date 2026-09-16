<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. Just to confirm, you're okay with this being recorded for after-action training purposes only, not for any personnel review?

Participant: Yeah, that's fine.

Interviewer: Can you describe your role and what you were responsible for when this incident began?

Participant: I'm the Situation Unit Analyst for the county EOC. During an activation, I build and maintain the Common Operating Picture — pulling together field reports, gauge data, weather updates, whatever's coming in — and I turn that into something the Branch Directors can actually act on. That night I was covering the flood side while also keeping half an eye on the fire branch, since Ridge Fire was still active and was interfering with some of our sensor and repeater coverage.

Interviewer: Walk me through how the incident began.

Participant: Around 9 PM we got a notice from the Twin Forks Reservoir Authority about a release tied to the incoming storm cell. The wording was pretty standard operational language — not alarmist, but not something I'd call reassuring either. Our downstream gauges were showing a gradual rise at that point, nothing that clearly told you how big this was going to get. The duty hydrologist was tied up on another call for at least ninety minutes, so I didn't have a technical read to lean on. Our flood Branch Director looked at it and said the pattern looked similar to releases he'd seen before, but he also flagged that the rainfall forecast for this particular storm cell was less certain than in past events — he wasn't fully reassuring, just giving me his honest read on both sides of it.

Interviewer: What did you do with that information?

Participant: I went with a monitor-and-prepare advisory rather than an immediate warning. It wasn't really one factor — it was the gradual gauge trend, the Director's qualified take, and the fact that jumping straight to a warning without more to go on has its own costs, in terms of credibility and resource strain if it turns out to be nothing. I documented specific thresholds that would trigger an upgrade if the gauges moved past them, so it wasn't an open-ended wait.

Interviewer: Did you consider seeking independent verification before finalizing that?

Participant: I did think about it, but with the hydrologist unavailable, the choice was really between acting on the best synthesis I had or delaying any messaging at all, which carries its own risk. I weighed the Director's read alongside the actual gauge numbers rather than just taking his word for it.

Interviewer: What happened next?

Participant: About ninety minutes later, the gauges spiked much faster than the early trend had suggested. The release turned out to be larger than what the gradual rise had implied.

Interviewer: Let's talk about the resource decision that followed.

Participant: Our field liaison started getting scattered water-rescue calls in two sub-neighborhoods, but the call intervals were irregular — hard to say if that was tapering off or about to surge. Around the same time, the weather service bumped up their estimate of how long the storm cell would sit over us, and a neighboring jurisdiction let us know their swift-water assets were available on a limited-time mutual-aid hold.

Interviewer: How did you decide what to request?

Participant: I went with a staged tier-2 mobilization instead of matching the confirmed calls exactly or going straight to tier-3. Part of it was the call pattern being ambiguous, part of it was the extended storm estimate, and part of it was that mutual-aid window — if I waited and needed more later, those assets might not be there. None of those three things alone would've pushed me to tier-2, but together they did.

Interviewer: Was there a specific past incident that shaped that call?

Participant: Not really one specific case I was drawing on. It was more just weighing what was in front of me that shift.

Interviewer: How did that play out?

Participant: Calls plateaued at a level that, looking back, either tier-1 or tier-2 could've handled. Some of the mutual-aid assets got used, some stayed in reserve. Hard to say in hindsight whether tier-1 would've been enough or whether we got lucky with tier-2.

Interviewer: Let's move to the evacuation decision.

Participant: This was the hardest one. Six of eight gauges were down from repeater damage tied to the Ridge Fire smoke, so I only had two reporting, both rising sharply over about twenty minutes. We do have a contingency protocol for this — when network coverage drops below half, there's a default evacuation radius around any gauge that crosses threshold. Field spotters were also seeing street flooding near one of the two working gauges, though nothing yet from the other sub-zones.

Interviewer: How did you apply that?

Participant: I followed the protocol and expanded evacuation to the zones adjacent to those two gauges. I was explicit with the team that the radius is a policy compromise — it's not a claim that we know what's happening in the unmonitored zones, it's just the standard response when coverage is this degraded. I didn't feel like I had enough to justify going wider than the protocol called for, and I also didn't think it was responsible to wait for full confirmation given the rate of rise.

Interviewer: Did you weigh expanding further than the protocol specified?

Participant: I considered it, honestly. Two gauges isn't much of the network. But going beyond what the protocol lays out felt like it would've been guessing past the point where I had a documented basis for the call.

Interviewer: What came out of that?

Participant: When backup gauges came back later, the adjacent zones matched the protocol's assumptions in some spots and not others. So it's genuinely mixed — the protocol got some of it right and missed some of it.

Interviewer: Let's talk about the hot-wash review of the initial advisory decision.

Participant: We used our standard after-action template, which forces you to separate what was known at the time from what's known now. Going through it point by point, some parts of the original advisory call still look reasonable to me given the gradual trend and the Director's qualified comment. Other parts — like the uncertain storm-duration forecast — in hindsight, maybe should've pushed us toward an earlier tier upgrade. It's not a clean verdict either way.

Interviewer: Do you think the outcome makes that decision look worse than it actually was?

Participant: That's the tension the template is designed to catch. I try to ask what a reasonable person would've concluded with only the 9 PM information, not what's obvious now that we know the release was bigger than expected. Some of it holds up under that test, some of it doesn't.

Interviewer: If the dam operator's notice had used clearly urgent language instead of standard language, would your initial call have changed?

Participant: Possibly, but it wouldn't have been the only thing driving it — I'd still have been weighing the actual gauge trend and the Director's forecast concerns alongside it.

Interviewer: And if all eight gauges had stayed online through the evacuation decision?

Participant: I'd have had a fuller picture to work with, which might have let us tighten or widen the radius with more confidence either way. Hard to say which direction it would've gone.

Interviewer: Looking back, how do you separate what was knowable in the moment from what only became clear afterward?

Participant: I lean on the template for that specifically, because otherwise it's easy to let the outcome color your memory of how clear things actually were at 9 PM. Some calls hold up, some don't, and I try not to flatten that into a single before-and-after story either way.

Interviewer: That's a good place to stop. Thanks for walking through this.

Participant: No problem.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "EM_Ambigious_7",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Emergency Operations Center (EOC) Situation Unit Analyst",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Twin Forks Flash Flood and Ridge Fire Smoke Incident (Ambiguous Control)",
    "scenario_summary_internal": "Over a 14-hour operational period, a Situation Unit Analyst at a county EOC manages the Common Operating Picture during a compound event: an unplanned high-volume release from Twin Forks Reservoir coincides with a monsoonal storm cell and reduced aerial/sensor visibility from active Ridge Fire smoke. The analyst classifies the threat and sets a warning tier, mobilizes rescue resources, decides on evacuation zone scope using degraded sensor coverage, and later participates in a hot-wash review of the initial decision. All four decisions are genuinely underdetermined by the available evidence, and the analyst's reasoning reflects reasonable, defensible judgment calls under uncertainty rather than any systematic distortion.",
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
        "tier-1/tier-2/tier-3 mobilization",
        "advisory vs. warning tier",
        "watershed sub-zone",
        "hot-wash review",
        "swift-water rescue asset",
        "contingency radius protocol"
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
          "Dam operator notice describes the release using standard operational language that is genuinely open to more than one reading",
          "Downstream gauge readings show a gradual, modest level rise, not clearly diagnostic of eventual magnitude",
          "Duty hydrologist is unavailable for independent verification",
          "The flood Branch Director notes the pattern resembles prior releases, while also flagging that this storm cell's rainfall forecast is less certain than in past events"
        ],
        "alternatives": [
          "Issue an immediate evacuation warning for low-lying Sector 7",
          "Issue a lower-tier 'monitor and prepare' advisory only",
          "Hold any public messaging pending independent hydrological verification"
        ],
        "intended_action": "Analyst selects the advisory-only tier after weighing the gradual gauge trend, the Director's qualified read (routine pattern but uncertain storm forecast), and the operational cost of over-escalating, documenting the monitoring plan that would trigger an upgrade.",
        "new_information_after_decision": [
          "Within 90 minutes, gauge levels exceed the warning threshold rapidly",
          "The release volume was larger than the gradual early trend had suggested"
        ]
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Field liaison reports scattered water-rescue calls in two sub-neighborhoods, with an unclear trend line since call intervals are irregular",
          "Weather service updates the storm cell's projected duration upward by an uncertain margin",
          "No new gauge or rainfall data has arrived since the last COP update",
          "A neighboring jurisdiction's mutual-aid swift-water assets are available on a limited-time hold"
        ],
        "alternatives": [
          "Request a standard tier-1 rescue package matching current confirmed calls",
          "Request a staged tier-2 mobilization to preserve the mutual-aid hold window",
          "Request full tier-3 mobilization to cover a wide range of possible escalation paths"
        ],
        "intended_action": "Analyst requests a staged tier-2 mobilization, citing the irregular call trend, the extended storm duration estimate, and the closing mutual-aid window as jointly justifying a middle-tier request rather than either extreme.",
        "new_information_after_decision": [
          "Rescue calls plateau at a volume that, in hindsight, could have been served by either tier-1 or tier-2 staffing",
          "The mutual-aid assets are partially used, with some held in reserve for the remainder of the shift"
        ]
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Only 2 of 8 planned stream gauges are transmitting; the rest are offline due to smoke-damaged repeaters",
          "Both reporting gauges show a sharp rise over a 20-minute window",
          "The EOC's degraded-sensor contingency protocol specifies a default evacuation radius around any gauge exceeding threshold when network coverage falls below 50 percent",
          "Field spotters report localized street flooding near one of the two active gauges, with no reports yet from other sub-zones"
        ],
        "alternatives": [
          "Expand evacuation only to sub-zones adjacent to the two reporting gauges, per the contingency radius protocol",
          "Expand evacuation to the entire multi-sector watershed area as a wider precaution",
          "Request emergency deployment of backup gauge readings or aerial confirmation before expanding further"
        ],
        "intended_action": "Analyst applies the documented contingency radius protocol and expands evacuation to the zones adjacent to the two reporting gauges, explicitly noting that the protocol's radius is a policy compromise rather than a claim about actual conditions in unmonitored sub-zones.",
        "new_information_after_decision": [
          "Backup gauges are restored later and show that flooding in the adjacent zones matched the protocol's assumptions in some areas but not others"
        ]
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The event has stabilized; outcome data (moderate flooding, partial evacuations, staged resource use) is now known",
          "EOC leadership convenes a hot-wash review of the Phase 1 advisory-only decision",
          "The review uses a structured after-action template that separates 'information available at time of decision' from 'information available now'"
        ],
        "alternatives": [
          "Conclude the original advisory decision was reasonable given what was known, while noting specific data points that would have justified earlier escalation had they been available",
          "Conclude the original decision under-responded and should be revised in the SOP without fully separating hindsight knowledge from real-time knowledge",
          "Defer judgment pending a fuller data reconciliation across all four decision points"
        ],
        "intended_action": "Analyst walks through the after-action template point by point, explicitly separating what the gradual gauge trend and qualified Director comment supported at the time from what is now known, and reaches a mixed conclusion: some elements of the advisory choice look defensible in hindsight, others look like they could have been escalated sooner, without asserting that the outcome was clearly foreseeable from the outset.",
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
        "How did you weigh the different pieces of information you had at that point?",
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
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "EM_Biased_7",
      "features_to_match": [
        "Domain vocabulary (COP, stream gauge threshold, tier-1/2/3 mobilization, advisory vs. warning tier, watershed sub-zone, hot-wash review, swift-water rescue asset)",
        "Same four-decision-point structure and chronology (threat classification, resource mobilization, evacuation scope, retrospective hot-wash)",
        "Same actors and stakeholders (dam operator, Branch Director, field liaison, fire dispatch, downstream residents)",
        "Same emotional tone: measured, professional, moderate time pressure",
        "Same moderate difficulty and degraded-information constraints (partial gauge outage, unavailable hydrologist, smoke-limited aerial recon)"
      ],
      "features_to_remove_or_change": [
        "Remove single-cause reliance on notice wording alone in Phase 1; replace with joint weighing of gradual trend and an explicitly qualified (not purely reassuring) Director comment",
        "Remove explicit reliance on a single vivid past-event memory as the stated driver of the Phase 2 resource tier; replace with multiple stated factors (call trend, forecast duration, mutual-aid window)",
        "Remove treatment of a 2-of-8 gauge sample as sufficient for a full watershed-wide inference in Phase 3; replace with an explicit, policy-based contingency radius applied consistently regardless of the sample-size question",
        "Remove narrative-coherence-driven overconfidence in Phase 3; replace with an explicit caveat that the protocol is a compromise, not a claim of certainty",
        "Remove outcome-driven 'should have been obvious' retrospective claim in Phase 4; replace with a structured, mixed after-action judgment that explicitly separates real-time and outcome knowledge throughout"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined: the analyst's choice should be explainable by legitimate, stated operational reasoning (protocol compliance, resource scarcity, forecast uncertainty, structured after-action method) such that a reasonable observer cannot confidently attribute the choice to any single named bias mechanism. Do not resolve the ambiguity by making the decision obviously correct or obviously erroneous, and do not insert cues that uniquely fit one of the six target bias mechanisms (reassuring wording as sole driver, authority-based deference as sole driver, single vivid memory as sole driver, small-sample overgeneralization stated as sufficient on its own, coherence-based overconfidence, or outcome-contaminated foreseeability claims)."
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
      "Confirm zero intended bias instances are embedded for any of the six target biases (Illusion of Validity, Insensitivity to sample size, Authority Bias, Availability Bias, Framing Effect, Hindsight bias).",
      "Confirm no bias name, definition, or psychological label appears in the public interview text.",
      "Confirm each decision point's reasoning is supported by an explicit, stated non-bias operational justification (protocol, resource constraint, forecast uncertainty, structured review method).",
      "Confirm Phase 1 does not rely solely on notice wording or solely on Director authority as the stated decisive factor; both must be present as one of several jointly weighed factors, none singularly determinative.",
      "Confirm Phase 2 does not attribute the tier choice to a single vivid recalled event; multiple stated factors must jointly justify the staged tier.",
      "Confirm Phase 3 does not treat the 2-of-8 gauge sample as self-evidently sufficient for the full watershed, and does not express coherence-based overconfidence; the protocol-compliance framing must carry the decision with an explicit uncertainty caveat.",
      "Confirm Phase 4 does not include an outcome-contaminated foreseeability claim; the structured after-action method must produce a genuinely mixed conclusion.",
      "Confirm total interview length falls within 1,215-1,485 words.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals as required.",
      "Confirm consequences described remain ambiguous as to whether decisions were well- or poorly-calibrated, avoiding outcomes that mechanically prove or disprove reasoning quality."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "ambiguous_control",
    "exact_occurrence_manifest": [
      {"bias": "Illusion of Validity", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; any confidence expressed must be tied to explicit, stated evidentiary or policy grounds, not narrative coherence alone."},
      {"bias": "Insensitivity to sample size", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; any use of partial gauge data must be framed through explicit protocol compliance with an acknowledged uncertainty caveat, not through treating the sample as sufficient on its own."},
      {"bias": "Authority Bias", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; deference to the Branch Director, if present, must be one of several jointly weighed factors, not the stated sole reason for forgoing verification."},
      {"bias": "Availability Bias", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; recalled past events or salient media, if mentioned at all, must not be stated as the decisive driver of a resource or severity estimate."},
      {"bias": "Framing Effect", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; the dam operator's wording, if referenced, must not be stated as the decisive driver of the tier classification."},
      {"bias": "Hindsight bias", "occurrences": 0, "mechanism_constraint": "Must not be intentionally instantiated; the retrospective review must explicitly separate real-time knowledge from outcome knowledge and avoid asserting that the outcome was clearly foreseeable from the outset."}
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
      {"bias": "Illusion of Validity", "requested_occurrences": 0},
      {"bias": "Insensitivity to sample size", "requested_occurrences": 0},
      {"bias": "Authority Bias", "requested_occurrences": 0},
      {"bias": "Availability Bias", "requested_occurrences": 0},
      {"bias": "Framing Effect", "requested_occurrences": 0},
      {"bias": "Hindsight bias", "requested_occurrences": 0}
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "EM_Biased_7",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "EM_Ambigious_7",
    "domain_id": "EM",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: condition is ambiguous_control, so no bias occurrences are allocated to any decision point. The four decision points instead each carry a genuinely underdetermined judgment call supported by an explicit non-bias operational justification (joint weighing of factors in Phase 1, multi-factor staged mobilization in Phase 2, protocol-based contingency radius with explicit uncertainty caveat in Phase 3, structured after-action separation of real-time vs. outcome knowledge in Phase 4), constructed to match the paired biased scenario's structure, vocabulary, actors, and decision count without reproducing any of its bias-specific mechanisms.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational domain and role (EOC Situation Unit Analyst)",
      "Four-decision-point chronology and topic sequence (threat classification, resource mobilization, evacuation scope, retrospective hot-wash)",
      "Stakeholder set and organizational hierarchy",
      "Technical vocabulary and terminology level",
      "Moderate difficulty and degraded-information constraints (partial gauge outage, unavailable hydrologist, smoke-limited aerial recon)",
      "Overall narrative tone and time-pressure profile",
      "Target interview length (1,215-1,485 words)"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
"evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [
      {"segment_id":"seg_001","speaker":"Participant","segment_type":"threat_evidence_assessment","raw_interview_anchor":"Around 9 PM we got a notice from the Twin Forks Reservoir Authority about a release tied to the incoming storm cell... the rainfall forecast for this particular storm cell was less certain than in past events.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant interprets multiple information sources and explicitly describes uncertainty; the hidden manifest contains no bias instance."},
      {"segment_id":"seg_002","speaker":"Participant","segment_type":"warning_tier_action_rationale","raw_interview_anchor":"I went with a monitor-and-prepare advisory rather than an immediate warning. It wasn't really one factor... I documented specific thresholds that would trigger an upgrade.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The action is justified by jointly weighed evidence, operational costs, and explicit escalation thresholds; no hidden bias is present."},
      {"segment_id":"seg_003","speaker":"Participant","segment_type":"verification_reasoning","raw_interview_anchor":"I did think about it, but with the hydrologist unavailable, the choice was really between acting on the best synthesis I had or delaying any messaging at all... rather than just taking his word for it.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant considers independent verification and distinguishes the Director's input from the gauge data; no hidden bias is present."},
      {"segment_id":"seg_004","speaker":"Participant","segment_type":"resource_evidence_assessment","raw_interview_anchor":"Our field liaison started getting scattered water-rescue calls... the call intervals were irregular... the weather service bumped up their estimate... and a neighboring jurisdiction... made their swift-water assets available.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant reports ambiguous trend information and several operational inputs without a bias mechanism."},
      {"segment_id":"seg_005","speaker":"Participant","segment_type":"resource_mobilization_rationale","raw_interview_anchor":"I went with a staged tier-2 mobilization... Part of it was the call pattern being ambiguous, part of it was the extended storm estimate, and part of it was that mutual-aid window.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The tier choice is explicitly multi-factor and not driven by a single salient memory or cue; no hidden bias is present."},
      {"segment_id":"seg_006","speaker":"Participant","segment_type":"prior_experience_assessment","raw_interview_anchor":"Not really one specific case I was drawing on. It was more just weighing what was in front of me that shift.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant rejects reliance on a specific past incident and describes current-evidence weighing; no hidden bias is present."},
      {"segment_id":"seg_007","speaker":"Participant","segment_type":"resource_outcome_assessment","raw_interview_anchor":"Calls plateaued at a level that, looking back, either tier-1 or tier-2 could've handled... Hard to say in hindsight whether tier-1 would've been enough or whether we got lucky with tier-2.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant preserves uncertainty about the retrospective resource assessment; no hidden bias is present."},
      {"segment_id":"seg_008","speaker":"Participant","segment_type":"evacuation_evidence_assessment","raw_interview_anchor":"Six of eight gauges were down... I only had two reporting, both rising sharply... We do have a contingency protocol... Field spotters were also seeing street flooding near one of the two working gauges.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"Partial data are acknowledged and interpreted through the documented contingency protocol and field reports; no hidden bias is present."},
      {"segment_id":"seg_009","speaker":"Participant","segment_type":"evacuation_action_rationale","raw_interview_anchor":"I followed the protocol and expanded evacuation to the zones adjacent to those two gauges. I was explicit with the team that the radius is a policy compromise...","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant states an explicit policy basis, uncertainty caveat, and bounded response; the hidden manifest contains no bias instance."},
      {"segment_id":"seg_010","speaker":"Participant","segment_type":"evacuation_scope_counterfactual","raw_interview_anchor":"I considered it, honestly. Two gauges isn't much of the network. But going beyond what the protocol lays out felt like it would've been guessing past the point where I had a documented basis.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant considers a wider alternative and explains why the documented basis constrained the choice; no hidden bias is present."},
      {"segment_id":"seg_011","speaker":"Participant","segment_type":"evacuation_outcome_assessment","raw_interview_anchor":"When backup gauges came back later, the adjacent zones matched the protocol's assumptions in some spots and not others. So it's genuinely mixed.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant gives a mixed outcome assessment rather than a categorical retrospective conclusion; no hidden bias is present."},
      {"segment_id":"seg_012","speaker":"Participant","segment_type":"hot_wash_review","raw_interview_anchor":"We used our standard after-action template, which forces you to separate what was known at the time from what's known now... It's not a clean verdict either way.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The structured review explicitly separates real-time and outcome knowledge and reaches a mixed conclusion; no hidden bias is present."},
      {"segment_id":"seg_013","speaker":"Participant","segment_type":"hindsight_control_reasoning","raw_interview_anchor":"That's the tension the template is designed to catch. I try to ask what a reasonable person would've concluded with only the 9 PM information, not what's obvious now...","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant explicitly guards against outcome knowledge contaminating the assessment; no hidden bias is present."},
      {"segment_id":"seg_014","speaker":"Participant","segment_type":"wording_counterfactual","raw_interview_anchor":"Possibly, but it wouldn't have been the only thing driving it — I'd still have been weighing the actual gauge trend and the Director's forecast concerns alongside it.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The counterfactual treats wording as one factor among several rather than a decisive frame; no hidden bias is present."},
      {"segment_id":"seg_015","speaker":"Participant","segment_type":"sensor_coverage_counterfactual","raw_interview_anchor":"I'd have had a fuller picture to work with, which might have let us tighten or widen the radius with more confidence either way. Hard to say which direction it would've gone.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant acknowledges improved information without claiming a determinate counterfactual outcome; no hidden bias is present."},
      {"segment_id":"seg_016","speaker":"Participant","segment_type":"real_time_vs_outcome_reasoning","raw_interview_anchor":"I lean on the template for that specifically, because otherwise it's easy to let the outcome color your memory... Some calls hold up, some don't.","eligible_reasoning_segment":true,"ground_truth_bias_present":false,"ground_truth_instance_ids":[],"ground_truth_rationale":"The participant uses a structured method to separate what was knowable from what became clear later; no hidden bias is present."}
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
