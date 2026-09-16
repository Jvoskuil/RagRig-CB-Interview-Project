You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": ["Interviewer", "Participant"],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Analyzed the participant's reported reasoning and decision episodes, plus secondhand reports of the Flood Branch Director's reasoning, for affirmative evidence of bias-specific cognitive mechanisms. No occurrence met the mechanism-first evidentiary standard; several plausible but under-evidenced mechanisms are recorded as candidates only."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "normalcy bias",
        "alternative_labels": ["false sense of normality"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Initial flood advisory decision",
        "supporting_interview_quote": "The wording was pretty standard operational language — not alarmist, but not something I'd call reassuring either. Our downstream gauges were showing a gradual rise at that point, nothing that clearly told you how big this was going to get.",
        "plausible_mechanism": "Normalcy bias could operate by treating ambiguous or non-alarming cues as evidence that the situation remains within normal bounds, leading toward a monitor-and-prepare posture rather than immediate warning.",
        "why_not_identified": "The participant did not disregard the threat; they acknowledged uncertainty, documented specific upgrade thresholds, weighed the Director's qualified concerns, and chose active monitoring. There is no affirmative evidence of threat disbelief or a false sense of normality affecting the decision."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "status quo bias",
        "alternative_labels": ["default bias", "default effect"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Evacuation radius decision under degraded gauge coverage",
        "supporting_interview_quote": "But going beyond what the protocol lays out felt like it would've been guessing past the point where I had a documented basis for the call.",
        "plausible_mechanism": "A status quo or default bias could favor adhering to the protocol's default evacuation radius rather than expanding beyond it, even when the information environment is severely degraded and may have warranted a more precautionary expansion.",
        "why_not_identified": "The participant explicitly considered expanding beyond the protocol and provided a reasoned, uncertainty-management justification for following the contingency standard. The decision appears to reflect policy-guided risk management rather than an automatic or affective preference for the default option."
      },
      {
        "candidate_id": "cand_003",
        "classification_status": "candidate",
        "proposed_bias_label": "hindsight bias",
        "alternative_labels": ["knew-it-all-along effect"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Hot-wash review of the initial advisory decision",
        "supporting_interview_quote": "Other parts — like the uncertain storm-duration forecast — in hindsight, maybe should've pushed us toward an earlier tier upgrade. It's not a clean verdict either way.",
        "plausible_mechanism": "Hindsight bias could distort retrospective judgment by making the uncertain storm-duration forecast seem more decision-relevant in light of the known outcome than it would have seemed at the time.",
        "why_not_identified": "The participant used an after-action template specifically designed to separate known-at-time information from known-now information and explicitly resisted outcome-driven memory distortion. No affirmative evidence shows their retrospective evaluation was distorted by outcome knowledge."
      },
      {
        "candidate_id": "cand_004",
        "classification_status": "candidate",
        "proposed_bias_label": "availability heuristic",
        "alternative_labels": ["availability bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Flood Branch Director (as reported by Participant)",
        "possible_decision_episode_label": "Initial flood advisory assessment",
        "supporting_interview_quote": "Our flood Branch Director looked at it and said the pattern looked similar to releases he'd seen before, but he also flagged that the rainfall forecast for this particular storm cell was less certain than in past events — he wasn't fully reassuring, just giving me his honest read on both sides of it.",
        "plausible_mechanism": "Availability could operate if the Director over-weighted easily recalled past releases with similar features when forming an initial pattern judgment.",
        "why_not_identified": "The evidence is a secondhand summary of another person's reasoning, and the Director is reported to have given a qualified, two-sided read rather than an overconfident one. The participant also weighed the Director's read against actual gauge data, so no affirmative evidence links an availability effect to the decision."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "The transcript includes some secondhand reporting of the Flood Branch Director's reasoning, limiting direct evidence about other actors' cognitive mechanisms.",
      "Retrieved corpus support was not used for identified occurrences because none met the identification bar; the available retrieved material was generally domain-shifted from emergency management."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "EM_Ambigious_7_Sonnet_on",
  "interview_id": "EM_Ambigious_7",
  "system_prompt_id": "Sonnet",
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
