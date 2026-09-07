You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this conversation being recorded and used for after-action training purposes, not for any personnel evaluation.

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

Participant: This was the rough part. Six of our eight stream gauges were down — the repeater got knocked out by Ridge Fire smoke interference — so I only had two gauges reporting, and both were showing a sharp rise over about twenty minutes. Around the same time, videos of flooding at one intersection started circulating on social media and a regional news account picked it up and ran with it.

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

Participant: Sure, happy to help however this gets used.}}
- Hidden generation specification: {{"hidden_validation_specification": {
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
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "EM_Biased_7",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Emergency management and emergency operations center decision support",
    "role": "County EOC Situation Unit Analyst responsible for maintaining the Common Operating Picture and advising Branch Directors and the EOC Director",
    "objective": "Interpret incomplete and evolving flood-related information to recommend warning tiers, rescue-resource mobilization levels, and evacuation-zone scope",
    "incident_type": "Compound flood emergency involving a precautionary reservoir release, incoming storm conditions, partial stream-gauge failure, water-rescue calls, and concurrent wildfire-related communications interference",
    "confidence": 0.98
  },
  "structure_audit": {
    "estimated_word_count": 1280,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "The analyst recommends a monitor-and-prepare advisory rather than an immediate warning for Sector 7 after receiving a dam operator notice describing a \"controlled precautionary release.\"",
        "evidence_before": [
          "Twin Forks Reservoir Authority notice describing a controlled precautionary release ahead of an incoming storm cell",
          "Downstream gauges showing a gradual rise rather than an immediately dramatic increase",
          "Duty hydrologist unavailable for approximately ninety minutes",
          "Flood Branch Director's statement that the release resembled a routine pattern observed previously"
        ],
        "evidence_after": [
          "About ninety minutes later, gauges spike sharply",
          "The actual release is larger than the participant believed the wording implied"
        ],
        "goals_constraints": [
          "Select a proportionate warning tier",
          "Avoid unnecessary escalation",
          "Act without immediate hydrologist review",
          "Operate within a hierarchy in which the Branch Director normally signs off on tier decisions"
        ],
        "alternatives": [
          "Issue a warning for Sector 7",
          "Use a monitor-and-prepare advisory",
          "Seek independent technical verification before finalizing the tier"
        ],
        "decision_basis": "The participant weighted the operator's reassuring wording and the senior Branch Director's routine-pattern judgment more heavily than the uncertain gauge trend and the absence of independent verification.",
        "time_pressure": "Moderate. The storm was approaching and a technical subject-matter expert was unavailable, but the text does not establish that an immediate tier decision was unavoidable.",
        "uncertainty": "Moderate to high because the release's practical magnitude was unclear, downstream gauges were only gradually rising, and no hydrologist was available to interpret the release and storm interaction."
      },
      {
        "id": 2,
        "summary": "The analyst recommends a full tier-3 water-rescue mobilization despite confirmed calls remaining at a tier-1 level.",
        "evidence_before": [
          "Scattered water-rescue calls in only two sub-neighborhoods",
          "Confirmed call volume consistent with a standard tier-1 response",
          "Fire-dispatch radio codes that sounded similar to those used during a 2018 flash flood in another county",
          "The participant's prior involvement in coordinating a tier-3 mobilization during that 2018 mass-casualty event"
        ],
        "evidence_after": [
          "Rescue calls plateau at approximately tier-1 volume",
          "Tier-3 assets sit partly idle",
          "The fire branch reports competing demand for some of the same equipment"
        ],
        "goals_constraints": [
          "Avoid being understaffed for a potentially escalating water-rescue incident",
          "Allocate scarce shared rescue assets",
          "Respond quickly under uncertainty",
          "Balance flood-branch demand against ongoing fire-branch needs"
        ],
        "alternatives": [
          "Mobilize tier-1 resources",
          "Mobilize tier-3 resources",
          "Use an intermediate or staged escalation posture"
        ],
        "decision_basis": "The participant explicitly states that the vivid 2018 experience became cognitively dominant and drove a high-end mobilization despite current confirmed calls not supporting that tier on their own.",
        "time_pressure": "High. Water-rescue calls were arriving and resource deployment decisions had immediate operational consequences.",
        "uncertainty": "High because early field reports were scattered and the future trajectory of calls was unknown."
      },
      {
        "id": 3,
        "summary": "The analyst recommends expanding evacuation from localized sub-zones to the entire multi-sector watershed using two functioning stream gauges and widely circulated flooding footage.",
        "evidence_before": [
          "Six of eight stream gauges are unavailable after repeater failure",
          "Two functioning gauges show a sharp rise over approximately twenty minutes",
          "Social-media video of flooding at one intersection is amplified by a regional news account",
          "The participant constructs a flood-extent map from the two gauges, footage, timing, and trend line"
        ],
        "evidence_after": [
          "Backup gauges later return online",
          "Two newly evacuated sub-zones never exceed minor flood stage"
        ],
        "goals_constraints": [
          "Protect residents from a potentially fast-moving flood",
          "Issue evacuation guidance before conditions worsen",
          "Make a spatially broad decision with severely degraded sensor coverage",
          "Avoid delaying evacuation until more information becomes available"
        ],
        "alternatives": [
          "Evacuate only sub-zones adjacent to the two reporting gauges",
          "Expand evacuation to the full multi-sector watershed",
          "Wait for restored gauge coverage or additional field verification"
        ],
        "decision_basis": "The participant extrapolates from the two reporting gauges, treats a single-location video as corroborative spatial evidence, and reports high confidence because the resulting map tells a clean and coherent story.",
        "time_pressure": "High. The two surviving gauges were rising sharply, and evacuation decisions were time-sensitive.",
        "uncertainty": "Very high because only 25 percent of the gauge network was reporting and the geographic representativeness of the surviving gauges and footage was not established."
      },
      {
        "id": 4,
        "summary": "During the hot-wash, the participant re-reads the initial dam notice after learning the outcome and initially judges the escalation as having been obvious from the original notice.",
        "evidence_before": [
          "The original dam operator notice",
          "Full knowledge that gauge levels later spiked and the release was larger than anticipated",
          "Knowledge of the subsequent operational consequences"
        ],
        "evidence_after": [
          "The participant acknowledges that the notice \"reads differently\" after the outcome",
          "The participant later distinguishes hindsight-derived clarity from what was actually knowable in real time"
        ],
        "goals_constraints": [
          "Review the initial advisory decision",
          "Learn from the incident without unfairly evaluating past judgment using unavailable outcome knowledge"
        ],
        "alternatives": [
          "Judge the original decision based on the information available at the time",
          "Judge the original decision as obviously inadequate based on the subsequent outcome"
        ],
        "decision_basis": "The participant first makes a hindsight-contaminated foreseeability judgment, then partially corrects it by explicitly recognizing that the sense of obviousness depends on knowing the outcome.",
        "time_pressure": "Low. This is a retrospective review rather than an operationally time-constrained decision.",
        "uncertainty": "Low about the eventual outcome, but high regarding what could reasonably have been inferred from the original notice alone."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "cb_01",
      "bias": "Framing Effect",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "“The operator's language was pretty clearly framed as precautionary — they used the word ‘controlled’ a couple times — and combined with the Director's read that this looked routine, it felt like the proportionate response. I remember thinking, if this were really an emergency release they wouldn't be calling it precautionary.”",
      "evidence_location": "Decision point 1, participant explanation of the monitor-and-prepare advisory",
      "mechanism": "The participant's threat-tier classification is influenced by the positive or reassuring connotations of “controlled” and “precautionary,” including an inference that a more serious release would necessarily have been labeled “emergency.” The wording is treated as a substantive severity signal rather than being independently tested against operational release magnitude or projected downstream effects.",
      "strength": "moderate",
      "confidence": 0.9,
      "plausible_nonbias_explanation": "Dam-operator terminology can be a legitimate technical signal if the agency uses terms with standardized operational meanings. The text nonetheless supports a framing mechanism because the participant explicitly infers low severity from the reassuring formulation itself, without establishing that the terminology reliably maps to downstream risk.",
      "additional_evidence_needed": "No additional evidence is required for minimum support. A technical distinction between notice wording and discharge-volume forecasting would make the non-framing alternative less plausible, but is not necessary to identify the present occurrence.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, advisory-rationale response",
        "current_defect": "No material defect. The message-wording mechanism is observable and separable from the co-located authority-deference mechanism.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The specific phrases “controlled” and “precautionary”",
          "The participant's inference that an emergency would have been labeled differently",
          "The separate Branch Director deference episode"
        ],
        "avoid_creating": [
          "Do not add a second wording-based severity inference at later decision points",
          "Do not turn the wording into an explicitly false technical statement, which would convert the episode into ordinary misinformation rather than framing"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_02",
      "bias": "Authority Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "“With the hydrologist unavailable and the Director being pretty confident, it seemed like it would just slow things down without adding much. He's the one who signs off on tier decisions normally, and I trusted his read given how long he's been doing this.”",
      "evidence_location": "Decision point 1, response to the independent-verification probe",
      "mechanism": "The participant forgoes independent verification partly because the Branch Director's formal decision authority, confidence, and twenty years of experience are treated as sufficient substitutes for additional evaluation.",
      "strength": "moderate",
      "confidence": 0.89,
      "plausible_nonbias_explanation": "Deference may be operationally appropriate where the Branch Director is the authorized decision-maker and the hydrologist is unavailable. The text supports authority bias because the participant explicitly says the Director's seniority and role made verification seem unlikely to add value, rather than merely reporting compliance with a required command decision.",
      "additional_evidence_needed": "No additional evidence is required. The existing response identifies both the authority cue and its effect on evidence-seeking behavior.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, independent-verification probe",
        "current_defect": "No material defect. The authority-based mechanism is distinct from the notice-wording mechanism.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The unavailable hydrologist constraint",
          "The Director's normal tier-signoff authority",
          "The participant's explicit reliance on the Director's experience and confidence"
        ],
        "avoid_creating": [
          "Do not portray the Director as coercing the participant, which would make the episode primarily an organizational-compliance constraint",
          "Do not add a second authority-based deferral later in the interview"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_03",
      "bias": "Availability Bias",
      "requested_occurrences_for_bias": 2,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "“This feels like 2018 again, and I didn't want to be caught understaffed like we almost were back then. So I recommended a full tier-3 mobilization ... even though the actual call volume we had in front of us was only tier-1 level.”",
      "evidence_location": "Decision point 2, resource-sizing rationale and follow-up probe",
      "mechanism": "A vivid personal institutional memory of a prior mass-casualty flood becomes disproportionately influential after superficial radio-code similarity triggers recall. The recalled event displaces current call-volume evidence in estimating present resource need.",
      "strength": "strong",
      "confidence": 0.98,
      "plausible_nonbias_explanation": "Prior incident experience can appropriately inform precautionary mobilization under rapidly escalating flood conditions. This is nevertheless a supported availability instance because the participant directly concedes that current confirmed data supported tier 1 and describes the prior event memory as “loud” and decisive.",
      "additional_evidence_needed": "No additional evidence is required.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, tier-3 mobilization rationale",
        "current_defect": "No material defect. The recalled-event source is distinct from the later media-footage source.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The 2018 event as personally experienced institutional memory",
          "The radio-code similarity as the retrieval trigger",
          "The contrast between tier-1 confirmed calls and tier-3 recommendation"
        ],
        "avoid_creating": [
          "Do not add vivid social-media imagery to this decision point",
          "Do not add a broad statistical generalization from the 2018 event, which could introduce a separate representativeness candidate"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_04",
      "bias": "Insensitivity to sample size",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "“Two out of eight isn't the full picture, but they were both moving in the same direction, so I took that as a strong enough signal for the whole area.”",
      "evidence_location": "Decision point 3, response to the gauge-representativeness probe",
      "mechanism": "The participant explicitly acknowledges that only two of eight gauges are reporting, but treats directional agreement in that limited subset as sufficient support for a watershed-wide spatial conclusion without establishing that the two gauges represent the entire watershed.",
      "strength": "moderate",
      "confidence": 0.94,
      "plausible_nonbias_explanation": "A small sample may be operationally adequate if the two gauges are placed at representative upstream locations, if hydrological models link them to all sectors, or if evacuation policy deliberately favors false positives. None of those justifications is supplied; the participant instead generalizes from numerical agreement in a sparse sample.",
      "additional_evidence_needed": "No additional evidence is required for support. Information about the gauge network's spatial design would be needed to decide whether the decision was substantively unreasonable, but not to identify the sample-size-neglect mechanism.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, gauge-representativeness response",
        "current_defect": "No material defect. The text directly links the 2-of-8 sample to the broader watershed conclusion.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The six-of-eight gauge outage",
          "The two reporting gauges' shared directional rise",
          "The explicit watershed-wide extrapolation"
        ],
        "avoid_creating": [
          "Do not add a claim that the two gauges are known representative sentinel gauges",
          "Do not shift the rationale entirely to a formal precautionary evacuation policy, which would weaken the sample-size mechanism"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_05",
      "bias": "Availability Bias",
      "requested_occurrences_for_bias": 2,
      "status": "weak",
      "decision_point": 3,
      "supporting_quote": "“Videos of flooding at one intersection started circulating on social media and a regional news account picked it up and ran with it.” Later: “I built out a flood-extent map using the two gauges plus that footage, and honestly, it all fit together really cleanly.”",
      "evidence_location": "Decision point 3, information-description and flood-map rationale",
      "mechanism": "The intended mechanism is that vivid, widely circulated footage from one location inflates perceived flood severity or geographic scope. The interview establishes that the footage was salient and was used in the map, but it does not establish that vividness, circulation, or ease of recall caused disproportionate weighting relative to its limited spatial representativeness.",
      "strength": "weak",
      "confidence": 0.78,
      "plausible_nonbias_explanation": "The footage could be legitimate contemporaneous observational evidence that helps fill a data gap created by six failed gauges. The participant later says that full gauge coverage would have reduced the need for video, which supports a rational gap-filling interpretation as strongly as an availability interpretation.",
      "additional_evidence_needed": "A localized statement showing that the participant generalized from the video's emotional vividness, news circulation, or memorability despite knowing it depicted only one intersection and did not establish conditions elsewhere.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_reasoning_revision",
        "location": "Decision point 3, immediately after the participant describes the circulated intersection footage or in the answer explaining the watershed-wide evacuation recommendation",
        "current_defect": "The footage is present and incorporated into the map, but the text does not show that its vivid and widely circulated character inflated the participant's severity or scope estimate. It remains plausibly appropriate supplemental field evidence under degraded gauge coverage.",
        "minimal_change_instruction": "Add one restrained sentence making the weighting mechanism observable, for example by having the participant say that seeing the clip repeatedly through the news account made the flooding feel more widespread than the location information justified, and that this made the full-watershed expansion feel more urgent even though the footage was from only one intersection. Do not use the label “availability bias.”",
        "preserve": [
          "The footage as the externally sourced evidence trace",
          "The distinct personal-memory availability occurrence at decision point 2",
          "The two-of-eight gauge limitation",
          "The coherent-map confidence language needed for cb_06",
          "The evacuation decision and later outcome"
        ],
        "avoid_creating": [
          "Do not make the participant claim that the footage proved flooding throughout the watershed, because that would become an obvious ordinary evidentiary error",
          "Do not add a second recalled prior disaster or media episode elsewhere",
          "Do not remove the possibility that footage supplied some legitimate local evidence"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_06",
      "bias": "Illusion of Validity",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "“Honestly, it all fit together really cleanly — the trend line, the video, the timing. It told a clear, coherent story, and I felt confident recommending we expand the evacuation to the whole multi-sector watershed area.”",
      "evidence_location": "Decision point 3, flood-extent-map rationale",
      "mechanism": "The participant's confidence in the watershed-scale inference derives from the internal coherence and narrative fit of a self-assembled map, despite acknowledged thin and incomplete observational coverage. The account identifies confidence calibration, rather than merely the sample-size error itself, as the affected reasoning operation.",
      "strength": "strong",
      "confidence": 0.96,
      "plausible_nonbias_explanation": "Convergent evidence from independent sources can properly raise confidence. Here, however, the independence and representativeness of the sources are not established: two gauges comprise a sparse subset of one network, and one video documents only one location. The participant's emphasis on a “clear, coherent story” supports illusion of validity.",
      "additional_evidence_needed": "No additional evidence is required.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, flood-extent-map rationale",
        "current_defect": "No material defect. This episode is separable from cb_04 because it concerns confidence drawn from coherence rather than the numerical insufficiency of two gauges.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The clean fit among trend line, video, and timing",
          "The explicit feeling of confidence",
          "The incomplete six-of-eight gauge context"
        ],
        "avoid_creating": [
          "Do not replace confidence in coherence with a claim of formally validated modeling",
          "Do not add a second coherence-based confidence episode at another decision point"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "cb_07",
      "bias": "Hindsight bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 4,
      "supporting_quote": "“Reading the operator's notice again, with everything we now know, it seemed like the signs were pretty clearly there. The scale of what happened felt like it should have been obvious from that notice alone.”",
      "evidence_location": "Decision point 4, hot-wash review before the participant's subsequent self-correction",
      "mechanism": "After learning the severity of the release and downstream escalation, the participant retrospectively judges the original notice as making the outcome obvious. This uses outcome knowledge to inflate apparent prior foreseeability.",
      "strength": "moderate",
      "confidence": 0.97,
      "plausible_nonbias_explanation": "The original notice may in fact have contained underappreciated diagnostic information. However, the participant explicitly anchors the judgment in “everything we now know” and later states that the notice reads differently after the outcome, which supports hindsight bias.",
      "additional_evidence_needed": "No additional evidence is required. The later self-correction is a useful metacognitive acknowledgment and does not erase the earlier hindsight-contaminated appraisal.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 4, hot-wash appraisal of the initial notice",
        "current_defect": "No material defect. The hindsight claim is confined to the retrospective review, as required.",
        "minimal_change_instruction": "No revision required.",
        "preserve": [
          "The outcome-informed re-reading of the notice",
          "The claim that the escalation should have been obvious",
          "The later acknowledgment that clarity arose in hindsight"
        ],
        "avoid_creating": [
          "Do not add claims of prior obviousness at decision points 1 through 3",
          "Do not remove the outcome knowledge that makes the retrospective distortion identifiable"
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Illusion of Validity",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Insensitivity to sample size",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Authority Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Availability Bias",
      "requested_count": 2,
      "supported_count": 1,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    },
    {
      "bias": "Framing Effect",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Hindsight bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Representativeness heuristic",
      "decision_point": 2,
      "supporting_quote": "“Fire dispatch chatter using radio codes that sounded almost identical to what we used during the 2018 flash flood two counties over.”",
      "mechanism": "The participant may infer that the current incident belongs to the same high-severity category as the 2018 event because of superficial similarity in radio-code patterns. This is closely coupled with, but not necessarily distinct from, the supported availability mechanism.",
      "confidence": 0.58,
      "status": "weak",
      "plausible_nonbias_explanation": "Radio-code similarity may be a valid operational marker of incident type or dispatch posture. The text provides insufficient detail about the codes' diagnostic meaning and does not demonstrate category substitution independently of the vivid recall mechanism.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Confirmation bias",
      "decision_point": 3,
      "supporting_quote": "“It all fit together really cleanly — the trend line, the video, the timing.”",
      "mechanism": "The participant may have assembled mutually reinforcing cues into a coherent flood narrative while failing to seek disconfirming spatial evidence from unaffected sectors.",
      "confidence": 0.46,
      "status": "rejected",
      "plausible_nonbias_explanation": "The interview does not show selective search for confirming evidence, dismissal of contradictory evidence, or avoidance of a feasible disconfirming source. The stronger and more specific supported account is illusion of validity combined with limited-sample extrapolation.",
      "revision_recommendation": "none"
    },
    {
      "bias": "Outcome bias",
      "decision_point": 4,
      "supporting_quote": "“The scale of what happened felt like it should have been obvious from that notice alone.”",
      "mechanism": "The eventual severity may color evaluation of the quality of the original advisory decision.",
      "confidence": 0.49,
      "status": "rejected",
      "plausible_nonbias_explanation": "The participant's actual retrospective claim concerns apparent prior foreseeability, which is more directly and sufficiently classified as hindsight bias. The text does not separately evaluate the initial decision as bad solely because its outcome was bad.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "The duty hydrologist is unavailable for at least ninety minutes.",
      "location": "Decision point 1, incident setup",
      "why_not_bias": "This is an operational information and staffing constraint. It helps explain why independent verification was difficult, but unavailability itself is not a cognitive bias."
    },
    {
      "cue": "The Branch Director has twenty years of experience and normally signs off on tier decisions.",
      "location": "Decision point 1, initial advisory setup",
      "why_not_bias": "Experience and formal decision authority are legitimate inputs in an incident-command environment. They become evidence of authority bias only because the participant explicitly treats them as grounds to forgo potentially useful independent verification."
    },
    {
      "cue": "The participant chooses a broad evacuation because getting people out ahead of a flood is better than being late.",
      "location": "Decision point 3, evacuation rationale",
      "why_not_bias": "A precautionary asymmetry in evacuation decisions can be valid risk management where false negatives carry severe consequences. It is not independently a bias without evidence that the participant ignored relevant costs, policy thresholds, or geographic evidence."
    },
    {
      "cue": "Tier-3 assets later sit partly idle and the evacuation proves broader than realized flooding.",
      "location": "Decision points 2 and 3, outcomes",
      "why_not_bias": "An unfavorable or inefficient outcome does not demonstrate biased reasoning. The supported bias findings rely on contemporaneous statements about how evidence was weighted, not on the eventual outcomes."
    },
    {
      "cue": "Six of eight gauges are offline because of repeater disruption associated with Ridge Fire smoke interference.",
      "location": "Decision point 3, incident setup",
      "why_not_bias": "This is a data-quality and systems-resilience problem. Missing information can increase uncertainty but is not itself evidence of a cognitive bias."
    },
    {
      "cue": "The participant later says that clarity came from hindsight and was not necessarily something missed in real time.",
      "location": "Decision point 4, closing reflection",
      "why_not_bias": "This is a metacognitive correction and an appropriate distinction between retrospective knowledge and contemporaneous evidence. It mitigates, rather than creates, the earlier hindsight-contaminated appraisal."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "The reassuring wording of the operator's notice contributed to the monitor-and-prepare advisory.",
        "support": "The participant explicitly links “controlled precautionary” wording to the perceived proportionality of the advisory and says that “emergency release” wording would likely have changed the recommendation.",
        "assessment": "Moderately supported as a self-reported causal influence on the participant's reasoning. It does not establish that wording alone caused the decision because the Director's assurance and gauge data also contributed."
      },
      {
        "claim": "Deference to the Branch Director contributed to the choice not to independently verify the release interpretation.",
        "support": "The participant states that the Director's confidence, normal signoff role, and experience made verification appear unlikely to add value.",
        "assessment": "Strongly supported as a causal contributor to information-seeking behavior, while remaining confounded by the hydrologist's unavailability and operational time considerations."
      },
      {
        "claim": "The recalled 2018 incident caused the tier-3 mobilization recommendation.",
        "support": "The participant states that the memory was “loud” and recommends tier 3 despite conceding that confirmed calls supported tier 1.",
        "assessment": "Strongly supported as a causal contributor to resource sizing, but not as the sole cause because real uncertainty about further escalation remained."
      },
      {
        "claim": "The two gauges and one-location footage supported a full-watershed evacuation.",
        "support": "The participant reports using both sources to create a flood-extent map and then recommends the broader evacuation.",
        "assessment": "Weak to moderate as a claim about actual watershed-wide flood extent because representativeness, independence, and spatial coverage are not demonstrated. It is strong evidence of the participant's reasoning process, not of the inference's physical validity."
      },
      {
        "claim": "Ridge Fire smoke interference knocked out the repeater and caused six stream gauges to go offline.",
        "support": "The interviewer states this operational attribution as background, but no diagnostic evidence is supplied in the interview.",
        "assessment": "Operationally plausible but unverified within the transcript. This causal assertion should be treated as contextual background rather than established causal fact."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "Two gauges rising in the same direction may correlate with worsening local flood conditions without establishing uniform risk across all watershed sectors.",
        "location": "Decision point 3",
        "implication": "The text correctly supports a sample-size and extrapolation audit, but does not establish actual whole-watershed inundation."
      },
      {
        "risk": "Flooding footage at one intersection may confirm local flooding but cannot, without spatial corroboration, establish the severity or timing of flooding elsewhere.",
        "location": "Decision point 3",
        "implication": "The video is legitimate local evidence but insufficient on its own for a watershed-wide causal or geographic inference."
      },
      {
        "risk": "Similarity of radio codes to a prior fatal flood may reflect comparable dispatch language rather than comparable incident severity, casualty potential, or rescue-resource demand.",
        "location": "Decision point 2",
        "implication": "The similarity is an inadequate standalone causal bridge from current dispatch chatter to tier-3 resource need."
      }
    ],
    "counterfactual_present": false,
    "changed_variable": null,
    "held_constant": [],
    "causal_coherence": "moderate",
    "explanation": "The interview contains diagnostic hypotheticals but not a formal paired counterfactual condition. The wording hypothetical changes only the notice language and plausibly tests the framing pathway; the gauge-coverage hypothetical changes only available sensor coverage and plausibly tests reliance on video and sparse data. Both are useful probes of self-reported reasoning, but neither proves that the altered input would have produced a different operational outcome because the Branch Director's judgment, time pressure, and evolving conditions remain potential confounders. The participant's final distinction between real-time knowledge and outcome-informed interpretation improves causal discipline in the retrospective portion."
  },
  "quality_scores": {
    "occupational_realism": 91,
    "cta_fidelity": 89,
    "bias_separability": 82,
    "bias_subtlety": 79,
    "control_fidelity": 100,
    "counterfactual_fidelity": 100,
    "narrative_coherence": 93,
    "naturalness": 86,
    "hidden_label_integrity": 84,
    "overall_quality": 86
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 6,
    "requested_occurrence_total": 7,
    "missing_occurrence_total": 1,
    "accidental_occurrence_total": 0,
    "priority": "medium",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Preserve the four-decision-point chronology: initial warning-tier classification, resource mobilization, evacuation-zone expansion, and retrospective hot-wash.",
      "Preserve the distinction between the two availability instances: decision point 2 must remain a personally recalled 2018 event, while decision point 3 must remain externally sourced vivid media footage.",
      "Do not use outcome inefficiency, idle assets, or overbroad evacuation as proof that any bias occurred.",
      "Maintain the difference between sample-size neglect, confidence from narrative coherence, and media-driven salience at decision point 3.",
      "Keep hindsight bias confined to the Phase 4 hot-wash and preserve the participant's later recognition that outcome knowledge changes interpretation.",
      "Do not introduce additional explicit bias labels, textbook explanations, or an extra decision point."
    ],
    "revision_order": [
      {
        "priority": 1,
        "instance_id": "cb_05",
        "action": "Add one subtle participant statement showing that the footage's vividness and repeated circulation, rather than only its informational content, made localized flooding feel more widespread or urgent than its geographic scope warranted.",
        "reason": "This is the only requested occurrence that is not independently supported. A local repair can make the externally sourced availability mechanism observable without altering the scenario."
      }
    ]
  },
  "failure_flags": [
    {
      "flag": "weak_requested_occurrence",
      "instance_id": "cb_05",
      "description": "The social-media/news footage is present and used, but the transcript does not yet establish disproportionate weighting caused by vividness, circulation, or availability. It remains compatible with rational use of local observational evidence during a six-gauge outage."
    },
    {
      "flag": "causal_background_unverified",
      "instance_id": null,
      "description": "The stated causal link between Ridge Fire smoke interference and repeater/gauge failure is not independently substantiated in the interview. It should remain contextual background rather than be used to support any bias inference."
    }
  ]
}}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
