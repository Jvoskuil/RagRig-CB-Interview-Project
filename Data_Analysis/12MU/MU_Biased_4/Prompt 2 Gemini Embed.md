You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single CTA interview analyzed for affirmatively demonstrated cognitive biases; retrieved corpus used for mechanism grounding where available."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["expectation bias", "selective evidence weighting", "myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm existing beliefs or expectations while discounting disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial assessment of GS-14R CO spike",
      "decision_point_description": "Interpreting whether the GS-14R CO reading represented a genuine gas hazard or a sensor artifact.",
      "affected_reasoning_operation": "Evidence weighting and hypothesis evaluation",
      "bias_specific_mechanism": "Pre-existing expectation of GS-14R sensor failure caused selective weighting of station history and telemetry features as confirmatory, while the handheld reading—a disconfirmatory but independent data point—was rationalized away as possible calibration drift.",
      "manifestation_in_interview": "The participant immediately categorized the high CO reading as another GS-14R sensor problem, interpreted the sharp spike as consistent with dust interference, and gave less weight to the 190 ppm handheld reading despite it still being well above baseline.",
      "effect_on_reasoning_or_decision": "The participant classified the spike as likely sensor artifact, underweighting the handheld reading, which supported immediate re-entry rather than precautionary verification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was that station again. GS-14R sits near a junction we shotcreted a couple months back, and I'd flagged that station twice already for what looked like dust interference throwing off the readings. So my instinct was, here we go again.",
          "evidence_explanation": "Demonstrates a pre-existing expectation about GS-14R sensor reliability that directed initial hypothesis formation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I leaned on the station's history more than the handheld number, honestly. We'd had two prior incidents where GS-14R gave us a spike that turned out to be nothing, so that pattern was fresh in my mind.",
          "evidence_explanation": "Shows selective weighting of history consistent with the participant's existing belief about the sensor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The handheld reading was lower than the station number, and handhelds can have their own calibration drift depending on how they're stored, so I didn't weight it as heavily as maybe I should have.",
          "evidence_explanation": "Explicitly acknowledges discounting an independent disconfirmatory reading through a plausible but unverified rationalization."
        }
      ],
      "correction_or_counterevidence": "The handheld was 190 ppm, still well above baseline, and no maintenance ticket had confirmed a GS-14R fault. The participant later acknowledged that if the handheld had matched or exceeded the station reading, he would have taken it more seriously. Eventual closeout suggested a longer round/clearance delay, though this was not known at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus mentioned confirmation bias only by name without providing an operational definition or mechanism; classification uses established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis", "plan continuation error"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an existing or planned course of action despite changing conditions or cues indicating it may be unsafe or inappropriate.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to proceed with scheduled re-entry after anomalous CO reading",
      "decision_point_description": "Choosing whether to delay re-entry for confirmatory sensor diagnostics or proceed on schedule.",
      "affected_reasoning_operation": "Risk assessment and go/no-go scheduling decision under uncertainty",
      "bias_specific_mechanism": "The default plan of re-entry/restart created commitment to continue; schedule pressure from mine planning increased the cost of delay and made continuation more attractive despite unresolved anomalous CO evidence.",
      "manifestation_in_interview": "The participant considered a second confirmatory reading or recalibration check but decided to proceed with scheduled re-entry after logging the handheld reading, partly because mine planning was waiting on restart timing.",
      "effect_on_reasoning_or_decision": "Re-entry went ahead without a second confirmatory reading or recalibration check, preserving production schedule at the expense of diagnostic certainty.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I made the call that this was probably another sensor issue and we could proceed with re-entry on schedule.",
          "evidence_explanation": "Shows the decision to continue with the original re-entry plan despite an unresolved anomalous CO reading."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I thought about it, but mine planning was already asking about restart timing for the LHD fleet, and delaying re-entry without hard evidence felt like it'd be hard to justify. So we logged the handheld reading and moved forward.",
          "evidence_explanation": "Shows schedule pressure directly influenced the decision not to obtain a confirmatory reading or recalibration check."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "More than I'd like, probably. It didn't override safety, but it definitely pushed me toward decisions that let production keep moving rather than ones that added delay.",
          "evidence_explanation": "Explicitly links production schedule pressure to decisions that favored continuation over delay."
        }
      ],
      "correction_or_counterevidence": "There were legitimate operational constraints, including mine planning pressure and lack of hard evidence, and the prior station false alarms made sensor error plausible. The eventual outcome did not show a fire or acute gas emergency.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus mentioned plan continuation bias by name but did not provide an operational definition or mechanism; classification uses general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias", "salience bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge event likelihood by the ease with which vivid or recent instances come to mind, producing overestimation of salient risks.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Precautionary hold after crew gut feeling",
      "decision_point_description": "Deciding whether to grant the shift boss's request to hold crew and trigger partial fire-response protocol.",
      "affected_reasoning_operation": "Risk probability estimation and precautionary resource allocation",
      "bias_specific_mechanism": "The vivid, recent safety briefing about a fatal underground fire made fire scenarios mentally available and emotionally salient, inflating their subjective plausibility relative to base rates and current data.",
      "manifestation_in_interview": "When the shift boss requested a precautionary hold, the participant allowed the recent fire-fatality briefing to make a fire scenario feel more plausible than the objective data indicated.",
      "effect_on_reasoning_or_decision": "He approved a crew hold and partially triggered the fire-response protocol despite no fire-specific indicators.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That one actually made me more cautious than I expected. A few weeks earlier we'd had a safety briefing that went over a fatality at another operation — underground fire, delayed detection, pretty grim details about smoke filling a drift before anyone realized what was happening. It stuck with me.",
          "evidence_explanation": "Identifies a vivid, recent safety event that was mentally available during the subsequent risk judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So when the shift boss raised the hold request, that case was sort of front and center, and I said yes, hold them, and we partially triggered the fire-response protocol just to be safe.",
          "evidence_explanation": "Shows the available fire case directly influenced the precautionary decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But with that briefing still sitting in the back of my mind, a fire scenario felt more plausible right then than it probably should have, given what the data actually showed.",
          "evidence_explanation": "Explicitly acknowledges that subjective plausibility of fire was inflated by the remembered briefing rather than by current evidence."
        }
      ],
      "correction_or_counterevidence": "No fire indicators were present—no smoke, no heat, CO2 flat—and fume-clearance delay was the more common explanation. The hold was precautionary and not harmful, but the participant acknowledged the fire scenario felt more plausible than the data supported.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied an availability heuristic definition; classification relies on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment heuristic", "anchor effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value and make insufficient adjustments when incorporating subsequent information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Revision of CO auto-cutoff setpoint",
      "decision_point_description": "Deciding whether to keep the 100 ppm CO auto-cutoff setpoint or adjust it toward newer baseline survey values.",
      "affected_reasoning_operation": "Numeric threshold estimation and adjustment",
      "bias_specific_mechanism": "The existing 100 ppm commissioning setpoint served as an anchor; newer survey data indicating higher ambient CO were treated as insufficient justification to move far from the anchor, resulting in only a minor adjustment.",
      "manifestation_in_interview": "Despite newer baseline surveys showing ambient CO trending materially higher under current depth and fleet conditions, the participant made only a small adjustment and kept the setpoint close to the five-year-old commissioning figure.",
      "effect_on_reasoning_or_decision": "The setpoint remained near the old 100 ppm value; subsequent normal diesel-heavy periods caused frequent auto-cutoff trips and operational friction.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our commissioning report, from about five years back, had that threshold set at 100 ppm.",
          "evidence_explanation": "Identifies the initial value that served as the anchor for later judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I made a small adjustment but largely kept it close to the original figure. The commissioning number had been through proper review when it was set, and it just felt like the number to stay near, even with the newer data pointing higher.",
          "evidence_explanation": "Shows the anchor was treated as an appropriate default despite newer data supporting a larger change."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have time that day to commission a full re-survey, so I treated the existing figure as basically sound with a minor tweak rather than moving it to where the interim numbers suggested.",
          "evidence_explanation": "Demonstrates insufficient adjustment from the anchor despite usable recent survey data."
        }
      ],
      "correction_or_counterevidence": "The commissioning number had undergone formal review, and a full re-survey was not possible that day. However, newer baseline surveys and diesel-heavy operating data pointed toward a higher interim setpoint; subsequent auto-cutoff trips confirmed the retained anchor was too low.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus provided a description of anchoring and adjustment, including insufficient adjustment from an initial value, directly supporting the mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described by Tversky and Kahneman in 1974... people make estimates based on an initial answer, and adjustments from there based on additional information... Tversky and Kahneman put it, \"adjustments are typically insufficient.\"",
          "mechanism_supported_by_source": "Initial values serve as anchors, and subsequent adjustments are typically insufficient.",
          "relevance_to_this_occurrence": "The participant used the five-year-old 100 ppm commissioning setpoint as an anchor and made only a small adjustment despite newer baseline data supporting a materially higher threshold."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "narrative fallacy",
      "alternative_labels": ["coherence bias", "illusion of explanatory depth"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Incident closeout causal attribution",
      "supporting_interview_quote": "I pulled them together into one explanation — drift-prone sensor plus idling diesel fleet plus a longer round, all compounding to produce the reading we saw. It read as a clean, complete account, it covered everything we'd logged, and that's what I put down as the operative cause for the closure.",
      "plausible_mechanism": "Coherence of a multi-causal narrative may have substituted for isolation testing, increasing perceived completeness and reducing the perceived need to test individual causes.",
      "why_not_identified": "Insufficient affirmative evidence that story coherence, rather than ordinary causal judgment under time and resource constraints, materially distorted the written causal attribution; the participant did not explicitly state overconfidence in the combined narrative."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages were OCR-impaired and provided limited mechanistic definitions for several labels.",
    "Single interview narrative may be affected by retrospective reconstruction and self-presentation, though temporal reasoning was evaluated from information available at the time.",
    "Low-confidence plan-continuation finding overlaps with legitimate production schedule constraints and should be interpreted cautiously.",
    "No follow-up evidence or independent verification of the incident details was available."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MU_Biased_4_Gemini_on",
  "interview_id": "MU_Biased_4",
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
