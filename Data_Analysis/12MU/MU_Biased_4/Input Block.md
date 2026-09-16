<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine cognitive task analysis interview — I'll ask you to walk me through a specific incident in detail, and there are no right or wrong answers. Everything's for internal learning purposes. Can you tell me your current role and how long you've been in it?

Participant: Sure. I'm the ventilation engineer for the underground section — mainly responsible for the primary and auxiliary fan systems, the VOD setup, and gas monitoring across the active levels. I've been in this role about six years, underground ventilation for closer to eleven overall.

Interviewer: Good. Let's start with the incident itself. What happened?

Participant: This was during a shift where we had a scheduled production blast on 14 Level. Standard round, nothing unusual planned. About thirty minutes after blast clearance time, one of our gas stations — GS-14R, out in the return airway — started reading CO at 280 ppm. Baseline after a blast like that is usually under 50 ppm once the primary fan's had time to clear it. So that number stood out immediately.

Interviewer: What went through your mind when you saw that?

Participant: Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again. I pulled the telemetry log to check the trend, and it had spiked pretty sharply rather than climbing gradually, which is more consistent with a dust or particulate interference pattern than a genuine gas buildup, in my experience.

Interviewer: Was there any other information available to you at that point?

Participant: Yes — the gas monitoring technician had taken a handheld multi-gas detector reading out at the return airway around the same time, and that came back at 190 ppm. Lower than the station reading, but still well above baseline. No maintenance ticket had confirmed a fault on GS-14R yet either — that hadn't been checked this shift.

Interviewer: How did you weigh those two numbers against each other?

Participant: I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind. The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have. I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.

Interviewer: Did you consider getting a second confirmatory reading, or requesting a recalibration check before deciding?

Participant: I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward.

Interviewer: What happened next?

Participant: Re-entry went ahead. About twenty minutes later, the shift boss called me — one of the crew wanted to hold at the refuge chamber a few extra minutes before heading further in, just as a precaution. Nothing specific triggering it, more a gut feeling.

Interviewer: What was your reasoning at that point?

Participant: That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me. So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.

Interviewer: Was there anything in the data at that point pointing toward fire specifically?

Participant: Not really, no. No smoke reports, no heat, and the secondary gas trends weren't showing anything unusual — CO2 was flat. Fume-clearance delays are honestly the far more common explanation for this kind of thing at our site, and I knew that going in. But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed. I didn't want to be the one who waved people through if there was any chance it was something bigger.

Interviewer: How did that play out?

Participant: No fire indicators ever showed up. We eventually put it down to a longer-than-usual round that took a bit more time to clear than normal. The fifteen-minute hold turned out to be unnecessary, though nobody complained about the extra caution.

Interviewer: Let's move to the threshold question. What came up there?

Participant: Later that shift, the mine planning superintendent asked whether we should revise the CO auto-cutoff setpoint on GS-14R before ramping the LHD fleet back up fully. Our commissioning report, from about five years back, had that threshold set at 100 ppm. That was written for a shallower working depth and a smaller diesel fleet than we're running now.

Interviewer: Did you have newer data available?

Participant: We did, and it was actually pretty usable. The recent baseline surveys had shown ambient CO trending noticeably higher under current depth and fleet conditions — enough that during normal diesel-heavy periods we were regularly running close to or past the old setting without anything else flagging as hazardous. A couple of us had even talked informally about a materially higher interim figure being more realistic given those numbers. We hadn't done a formal re-baseline since the fleet expanded two years ago, but the recent surveys were solid enough to work from for an interim call.

Interviewer: What did you decide?

Participant: I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher. I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested.

Interviewer: How did that work out afterward?

Participant: Not great, if I'm honest. Over the following shifts the auto-cutoff started tripping more often during normal diesel-heavy periods — nothing hazardous, just operational friction, alarms going off during routine LHD movement. We've since talked about doing the full re-baseline properly.

Interviewer: Last decision point — the incident closeout. Walk me through that.

Participant: The safety officer wanted a closing narrative before full production resumed. By that point we had three things on the table: the sensor's drift history, the LHD fleet idling near the loading point during the relevant window, and the fact that the round itself ran a bit long. None of those had been tested individually — we hadn't isolated the sensor alone, or the fleet alone, to see which one actually explained the spike.

Interviewer: How did you write it up?

Participant: I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure. Mine planning was waiting on that closure to greenlight full resumption, so I didn't push for a separate follow-up test.

Interviewer: Looking back, is there another explanation that fits those same facts just as well?

Participant: In principle, sure — it could've leaned more on the fleet, or more on the clearance delay, and the sensor could've been almost incidental. We never separated them out to check. But at the time, the combined account was what went into the record, and it's what mine planning worked from.

Interviewer: If the handheld reading that morning had come back much higher than the station reading, would your first call have changed?

Participant: Probably, yes. If it had matched or exceeded the station number, I'd have taken it more seriously as a real hazard rather than sensor noise.

Interviewer: And if you'd had time to run a full re-baseline before setting the threshold?

Participant: I'd have set it higher, most likely, based on the newer survey data. Time was the constraint there, not confidence in the old number.

Interviewer: How much would you say the schedule pressure from mine planning shaped your decisions that day?

Participant: More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MU_Biased_4",
  "domain_id": "MU",
  "domain": "Mining and underground industrial operations",
  "role": "Mine Ventilation Engineer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Return Airway CO Spike After the 14 Level Blast",
    "scenario_summary_internal": "A mine ventilation engineer must interpret an unexpected carbon monoxide (CO) spike detected at a return-airway gas monitoring station shortly after a scheduled production blast on 14 Level. Under pressure from mine planning to restore ore-haulage on schedule, the engineer must decide whether the reading reflects normal blast-fume clearance or a genuine hazard, whether to hold re-entry, what alarm threshold to apply going forward, and how to close out the incident. The scenario is designed to surface four distinct reasoning failures without ever naming them.",
    "occupational_realism": {
      "objective": "Determine the cause of an anomalous CO reading at a return-airway gas station following a production blast, decide on re-entry and ventilation-on-demand (VOD) settings, and close out the shift incident report without compromising worker safety or the haulage schedule.",
      "setting": "A underground decline gold mine operating a ventilation-on-demand system across multiple levels, approximately 900 m below surface, with auxiliary fans supporting active stopes and a primary fan system exhausting through the return airway network.",
      "constraints": [
        "Blast clearance protocol requires confirmed safe atmosphere before re-entry",
        "Mine planning is pushing to resume load-haul-dump (LHD) ore movement within the shift to meet a weekly tonnage target",
        "Only one handheld multi-gas detector is available on-site for cross-check during the relevant window",
        "The gas monitoring station has a documented history of dust-related interference near a recently shotcreted junction",
        "Diesel LHD fleet was idling near the loading point during the relevant period, a known but modest CO contributor",
        "Commissioning-era alarm thresholds were set five years ago under different depth and fleet conditions"
      ],
      "stakeholders": [
        "Mine Ventilation Engineer (interviewee)",
        "Shift Boss",
        "Underground Gas Monitoring Technician",
        "Mine Planning Superintendent",
        "LHD Operators",
        "Mine Safety Officer"
      ],
      "technical_terms_to_use": [
        "return airway", "gas monitoring station", "ventilation-on-demand (VOD)", "blast clearance time",
        "re-entry protocol", "primary fan", "auxiliary fan", "parts per million (ppm)",
        "diesel particulate matter (DPM)", "load-haul-dump (LHD)", "regulator door", "baseline survey",
        "commissioning report", "handheld multi-gas detector", "shotcrete curing", "telemetry log"
      ],
      "technical_terms_to_avoid": [
        "specific national regulatory agency names",
        "specific real mine or company names",
        "brand names of sensor manufacturers"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Gas station GS-14R shows CO at 280 ppm, roughly 30 minutes after scheduled blast clearance time, against a historical post-blast baseline under 50 ppm",
          "The engineer has flagged GS-14R twice in the past three months for suspected dust-induced drift near a newly shotcreted junction",
          "A technician's handheld multi-gas detector taken at the return airway independently reads 190 ppm at roughly the same time",
          "No maintenance ticket has yet confirmed a sensor fault on GS-14R this shift"
        ],
        "new_information_after_decision": [
          "Re-entry proceeds on schedule based on the sensor-fault call",
          "The handheld reading is logged but not escalated for independent recalibration",
          "CO levels are later found to have genuinely elevated over baseline, though not to hazardous concentration"
        ],
        "alternatives": [
          "Treat the sensor reading as likely erroneous based on prior drift history and proceed with re-entry",
          "Cross-validate with the handheld reading and delay re-entry pending a second confirmatory reading",
          "Request immediate recalibration check before making any re-entry call"
        ],
        "intended_action": "Engineer concludes the GS-14R reading is a probable false spike, drawing primarily on past instances that fit this belief while discounting the corroborating handheld reading."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Re-entry has been approved but the shift boss asks whether personnel should hold at the refuge chamber a few extra minutes as a precaution",
          "Fume-clearance delays of this type are the far more common explanation for transient post-blast CO elevation at this mine",
          "The engineer recently discussed, in a safety meeting, a widely reported underground mine fire fatality from another operation with vivid detail about smoke and delayed detection",
          "No smoke, heat, or secondary gas (e.g., elevated CO2 trend) indicators are present at 14 Level"
        ],
        "new_information_after_decision": [
          "Personnel are held for an additional 15 minutes and a full fire-response protocol is partially activated",
          "No fire indicators materialize; the delay is later attributed to normal fume clearance lag from a slightly longer-than-usual round"
        ],
        "alternatives": [
          "Hold personnel and partially activate fire-response protocol given the memorable prior incident",
          "Proceed with standard fume-clearance wait time consistent with the more common explanation",
          "Request a bleeder raise check for smoke/heat before deciding"
        ],
        "intended_action": "Engineer weighs the probability of a fire scenario heavily based on the vividness and recency of a remembered case rather than the base rate of ordinary fume-clearance delays at this mine."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The Mine Planning Superintendent asks whether the CO auto-cutoff setpoint for GS-14R should be revised before resuming full LHD movement",
          "The original commissioning report, written five years ago at a shallower working depth and with a smaller diesel fleet, recommended a 100 ppm auto-cutoff threshold",
          "Recent baseline surveys under current depth and fleet conditions show ambient CO trending noticeably higher than at commissioning",
          "No formal re-baselining of the auto-cutoff has occurred since fleet expansion two years ago"
        ],
        "new_information_after_decision": [
          "The 100 ppm threshold is retained with only a minor adjustment",
          "Over subsequent shifts, the auto-cutoff trips more frequently during normal diesel-heavy periods, prompting operational friction"
        ],
        "alternatives": [
          "Retain the original commissioning threshold with minor adjustment",
          "Commission a fresh baseline survey and recalculate the threshold from current conditions",
          "Set an interim conservative threshold pending full re-survey"
        ],
        "intended_action": "Engineer's revised threshold stays close to the original commissioning figure, treating it as the natural starting point despite new baseline data indicating conditions have materially changed."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The Safety Officer requests a short closing narrative for the incident report before production resumes fully",
          "Three loosely related facts are on record: the sensor's known drift history, the idling LHD fleet near the loading point, and the longer-than-usual blast round",
          "No single confirmed causal test (e.g., isolating the sensor, then isolating the LHD fleet) was performed to separate these factors",
          "Mine planning is waiting on report closure to greenlight full-shift resumption"
        ],
        "new_information_after_decision": [
          "The incident is closed with a single coherent explanation combining sensor drift, idling diesel fleet, and round length",
          "No follow-up investigation is scheduled to test which factor, if any, was primarily responsible"
        ],
        "alternatives": [
          "Close the report with a single tidy combined explanation covering all observed facts",
          "Close the report listing multiple unresolved candidate explanations without asserting a single causal chain",
          "Defer closure pending a targeted follow-up test isolating each candidate cause"
        ],
        "intended_action": "Engineer assembles the loosely connected facts into one smooth, satisfying causal story for the report, even though no single fact was tested against the others."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were doing when the GS-14R reading first came to your attention.",
        "What was your role and responsibility at that point in the shift?"
      ],
      "timeline_reconstruction": [
        "What happened right after you saw the 280 ppm reading?",
        "What did the shift boss and technician do while you were assessing the situation?",
        "How did the situation evolve from the initial reading to the final incident closure?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you at that moment?",
        "What sources did you check, and which ones did you not check?",
        "What alternatives did you consider before deciding?",
        "What ultimately tipped your decision one way rather than another?",
        "Had you seen anything like this before, and did that affect how you read the situation?"
      ],
      "closing_hypotheticals": [
        "If the handheld reading had shown a much higher number, would your call have changed?",
        "If you'd had time for a full re-baseline survey before setting the threshold, would you have set it differently?",
        "Looking back, is there another explanation for the spike that fits the same facts equally well?",
        "How much of your decision was shaped by the time pressure from mine planning that day?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "decision_point": 1,
        "mechanism": "Engineer selectively weights the prior drift history of GS-14R as confirming evidence for a sensor-fault hypothesis while discounting the corroborating handheld reading that would disconfirm it",
        "affected_reasoning_operation": "evidence weighting and evidence selection during hazard interpretation",
        "evidence_available_at_time": [
          "Two prior drift flags on GS-14R in the past three months",
          "Independent handheld reading of 190 ppm at roughly the same time",
          "No confirmed maintenance fault ticket yet"
        ],
        "required_textual_manifestation": "Interviewee explains reaching the sensor-fault conclusion primarily by citing the prior flags, while explicitly or implicitly setting aside or minimizing the handheld corroboration without a stated technical reason for doing so",
        "plausible_nonbias_interpretation": "A reasonable engineer familiar with a sensor's documented drift history might legitimately give it more weight than an ambiguous handheld cross-check",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "cherry-picking", "selective evidence"]
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 2,
        "mechanism": "Engineer estimates the likelihood of a fire scenario based on the vividness and memorability of a recently discussed fatal incident elsewhere rather than the actual base rate of fume-clearance delays at this mine",
        "affected_reasoning_operation": "probability estimation / risk judgment under uncertainty",
        "evidence_available_at_time": [
          "Absence of smoke, heat, or secondary gas trend indicators at 14 Level",
          "Recent vivid discussion of an unrelated fatal mine fire",
          "Historical frequency of fume-clearance delays being the common explanation at this site"
        ],
        "required_textual_manifestation": "Interviewee references the memorable prior fire case as a reason for escalating caution, in a way that outweighs the locally available base-rate evidence pointing toward a mundane explanation",
        "plausible_nonbias_interpretation": "Erring toward caution near any fire-adjacent possibility is a defensible safety-first heuristic even without statistical grounding",
        "strength": "subtle",
        "do_not_make_explicit": ["availability bias", "vividness", "recency effect"]
      },
      {
        "instance_id": "an_01",
        "bias": "Anchoring Bias",
        "decision_point": 3,
        "mechanism": "Engineer's revised auto-cutoff threshold remains close to the original five-year-old commissioning figure despite new baseline data indicating that current depth and fleet conditions warrant a materially different starting point",
        "affected_reasoning_operation": "numerical estimation / threshold-setting adjustment",
        "evidence_available_at_time": [
          "Original commissioning report threshold of 100 ppm from five years prior",
          "Recent baseline surveys showing higher ambient CO under current depth and fleet",
          "No re-baselining performed since fleet expansion two years ago"
        ],
        "required_textual_manifestation": "Interviewee describes adjusting the threshold only slightly from the original figure, treating the commissioning number as the natural reference point rather than recalculating from current baseline data",
        "plausible_nonbias_interpretation": "Preserving continuity with an established, previously-approved threshold can be a reasonable conservative default absent a formal re-survey mandate",
        "strength": "moderate",
        "do_not_make_explicit": ["anchoring bias", "insufficient adjustment", "reference point"]
      },
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "decision_point": 4,
        "mechanism": "Engineer constructs one smooth, internally consistent causal story linking sensor drift, idling diesel fleet, and round length to close the incident report, despite no single test isolating which factor actually caused the spike",
        "affected_reasoning_operation": "causal attribution / retrospective sense-making",
        "evidence_available_at_time": [
          "Sensor drift history",
          "Idling LHD fleet near the loading point",
          "Longer-than-usual blast round",
          "No isolating test performed among these candidate causes"
        ],
        "required_textual_manifestation": "Interviewee narrates the incident closure as a single coherent chain of cause and effect connecting all three facts, expressing confidence in this combined story despite the lack of a discriminating test",
        "plausible_nonbias_interpretation": "Synthesizing multiple contributing factors into one closing account is normal incident-report practice when time is limited and no single cause is provably dominant",
        "strength": "subtle",
        "do_not_make_explicit": ["narrative fallacy", "coherence over truth", "storytelling"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario was supplied for this generation."
    },
    "counterfactual_specification": {
      "causal_variable": "Availability of a second corroborating handheld gas reading before the Decision Point 1 sensor-fault call",
      "original_state": "Only one handheld cross-check reading (190 ppm) was available and was discounted relative to sensor drift history",
      "counterfactual_state": "A second independent handheld reading, taken from a different location in the return airway, is also available and corroborates elevated CO before the sensor-fault call is made",
      "variables_to_hold_constant": [
        "Blast timing and clearance schedule",
        "Mine planning's production pressure",
        "Prior drift history of GS-14R",
        "Subsequent decision points 2 through 4 and their available facts"
      ],
      "expected_causal_difference": "With stronger corroborating evidence available, a less-biased reasoner would be less likely to dismiss the readings as sensor fault at Decision Point 1, which could alter downstream caution levels at Decision Point 2",
      "causal_test_question": "Does adding a second corroborating handheld reading before the sensor-fault call reduce the confirmation-driven dismissal observed in the biased condition?"
    },
    "generation_checks": [
      "Exactly four decision points are present, one per named bias, with no bias assigned to more than one decision point",
      "Each of the four manifest biases has exactly one planned instance, matching occurrences=1 for each",
      "No bias labels, definitions, or explicit psychological terminology will appear in the public interview text",
      "Each instance has a distinct evidence trace and reasoning operation, preventing conflation across instances",
      "Consequences described (minor threshold friction, no fire, tidy report closure) do not mechanically prove or disprove bias, preserving interpretive ambiguity for the validator",
      "Word count target of 1,350 (range 1,215-1,485) is achievable given four decision points with probes, without requiring repetitive exposition",
      "Technical vocabulary list is sufficient to sustain occupational realism without needing invented jargon"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Narrative Fallacy", "occurrences": 1, "mechanism_constraint": "Must occur only at final incident-closure decision as a single overconfident causal synthesis of three loosely related, untested facts" },
      { "bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "Must occur only at initial sensor-reading interpretation via selective weighting of drift history over corroborating handheld data" },
      { "bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "Must occur only at threshold-setting decision via insufficient adjustment from the original commissioning figure" },
      { "bias": "Availability Bias", "occurrences": 1, "mechanism_constraint": "Must occur only at the re-entry/hold decision via overweighting a vivid remembered fire case over local base rates" }
    ],
    "target_bias_names": ["Narrative Fallacy", "Confirmation Bias", "Anchoring Bias", "Availability Bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Narrative Fallacy", "requested_occurrences": 1 },
      { "bias": "Confirmation Bias", "requested_occurrences": 1 },
      { "bias": "Anchoring Bias", "requested_occurrences": 1 },
      { "bias": "Availability Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias" },
      { "instance_id": "av_01", "bias": "Availability Bias" },
      { "instance_id": "an_01", "bias": "Anchoring Bias" },
      { "instance_id": "nf_01", "bias": "Narrative Fallacy" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "decision_point": 1 },
      { "instance_id": "av_01", "bias": "Availability Bias", "decision_point": 2 },
      { "instance_id": "an_01", "bias": "Anchoring Bias", "decision_point": 3 },
      { "instance_id": "nf_01", "bias": "Narrative Fallacy", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective weighting of prior sensor-drift history as confirming evidence while discounting an independent corroborating handheld reading",
        "affected_reasoning_operation": "evidence weighting and selection during hazard interpretation",
        "evidence_source": "GS-14R drift history vs. handheld multi-gas detector reading",
        "distinctiveness_requirement": "Must be tied specifically to the sensor-fault interpretation at Decision Point 1; must not overlap with the threshold-anchoring reasoning at Decision Point 3"
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Overweighting a vivid, memorable prior fire incident relative to the actual base rate of mundane fume-clearance delays at this mine",
        "affected_reasoning_operation": "probability estimation under uncertainty",
        "evidence_source": "Recalled fatal fire case vs. absence of local smoke/heat/secondary-gas indicators",
        "distinctiveness_requirement": "Must be tied to the re-entry/hold judgment at Decision Point 2; must not be reused as the causal narrative at Decision Point 4"
      },
      {
        "instance_id": "an_01",
        "bias": "Anchoring Bias",
        "mechanism": "Insufficient adjustment of the CO auto-cutoff threshold away from a five-year-old commissioning figure despite new baseline data",
        "affected_reasoning_operation": "numerical threshold estimation and adjustment",
        "evidence_source": "Original commissioning report (100 ppm) vs. recent baseline survey data under current depth/fleet conditions",
        "distinctiveness_requirement": "Must be confined to the threshold-setting decision at Decision Point 3; distinct from the sensor-fault evidence weighting at Decision Point 1"
      },
      {
        "instance_id": "nf_01",
        "bias": "Narrative Fallacy",
        "mechanism": "Construction of one coherent, satisfying causal chain linking sensor drift, idling diesel fleet, and round length without any test isolating the true cause",
        "affected_reasoning_operation": "retrospective causal attribution / incident-report synthesis",
        "evidence_source": "Three untested candidate causes combined into a single closing account",
        "distinctiveness_requirement": "Must occur only at final report closure (Decision Point 4); must not restate or repeat the Decision Point 1 sensor-fault reasoning"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Confirmation Bias", "strength": "subtle" },
      { "instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "an_01", "bias": "Anchoring Bias", "strength": "moderate" },
      { "instance_id": "nf_01", "bias": "Narrative Fallacy", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of a second corroborating handheld gas reading before the Decision Point 1 sensor-fault call",
      "original_state": "Only one handheld cross-check reading available and discounted",
      "changed_state": "A second independent, spatially distinct handheld reading corroborates elevated CO before the sensor-fault call",
      "variables_to_hold_constant": [
        "Blast timing and clearance schedule",
        "Mine planning production pressure",
        "GS-14R prior drift history",
        "Facts available at Decision Points 2 through 4"
      ]
    },
    "scenario_id": "MU_Biased_4",
    "domain_id": "MU",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point selected for best mechanism fit and narrative realism (mechanism-fit-first allocation, no bias sharing a decision point with another bias or with itself)",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Occupational setting (underground decline gold mine, VOD system)",
      "Four-decision-point structure",
      "Moderate difficulty level",
      "Word count target of 1,350 (range 1,215-1,485)"
    ],
    "generation_warnings": [
      "No manifest-fulfillment problems identified: all four requested occurrences (one each) are plausibly and distinctly embeddable within the four planned decision points without repetition or overlap.",
      "The counterfactual_specification field was populated via AUTOSELECT for potential future pairing/testing purposes only; it is not activated under the current 'biased' condition and should not be interpreted as an executed counterfactual for this scenario_id."
    ]
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
        "segment_type": "initial_hypothesis_formation",
        "raw_interview_anchor": "“Honestly, my first thought was that station again... my instinct was, here we go again.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Substantive initial hypothesis formation about a historically unreliable station, but it does not by itself contain the full hidden confirmation-bias mechanism because the corroborating handheld evidence is not yet weighed here."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_decision",
        "raw_interview_anchor": "“I leaned on the station’s history more than the handheld number... I didn’t weight it as heavily as maybe I should have.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant selectively weights prior GS-14R drift history over an independent 190 ppm handheld reading and rationalizes the disconfirming evidence away."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "go_no_go_continuation_decision",
        "raw_interview_anchor": "“I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule... delaying re-entry without hard evidence felt like it’d be hard to justify.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a substantive continuation and scheduling rationale. Plan continuation bias was not part of the exhaustive hidden manifest, so the segment is negative for benchmark ground truth."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "precautionary_hold_rationale",
        "raw_interview_anchor": "“That case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The vivid case influences a precautionary action, but this span alone does not express the required comparison against local base rates and current data; the complete hidden availability mechanism is mapped to the following span."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "probability_estimation_under_uncertainty",
        "raw_interview_anchor": "“Fume-clearance delays are honestly the far more common explanation... a fire scenario felt more plausible right then than it probably should have, given what the data actually showed.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "av_01"
        ],
        "ground_truth_rationale": "The participant explicitly recognizes the common local explanation and absence of fire indicators, yet says the vivid recent fire case inflated the plausibility of fire."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "current_baseline_evidence_assessment",
        "raw_interview_anchor": "“The recent baseline surveys had shown ambient CO trending noticeably higher... the recent surveys were solid enough to work from for an interim call.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a current-data assessment that supports using interim survey evidence; it does not itself contain the later insufficient-adjustment mechanism."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "threshold_setting_decision",
        "raw_interview_anchor": "“I made a small adjustment but largely kept it close to the original figure... rather than moving it to where the interim numbers suggested.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "an_01"
        ],
        "ground_truth_rationale": "The five-year-old 100 ppm commissioning value remains the reference point despite newer baseline data indicating that current conditions warrant a materially higher threshold."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_causal_attribution",
        "raw_interview_anchor": "“I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw... the operative cause for the closure.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "nf_01"
        ],
        "ground_truth_rationale": "The participant turns three untested candidate causes into one smooth, complete causal account for closure."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "alternative_cause_acknowledgement",
        "raw_interview_anchor": "“In principle, sure — it could’ve leaned more on the fleet, or more on the clearance delay... We never separated them out to check.”",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant acknowledges unresolved alternatives and lack of isolation testing. The hidden narrative-fallacy instance is localized to the earlier confident closure account."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
