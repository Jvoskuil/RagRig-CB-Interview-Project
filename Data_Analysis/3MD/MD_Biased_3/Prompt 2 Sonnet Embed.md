You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for a cognitive task analysis study, not for any evaluation of your performance or record. You can decline to answer anything. Are you okay to proceed?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you tell me your role and what your responsibilities were that night?

Participant: I was the Battle Captain on the night shift at the JOC, so I'm the watch officer responsible for the common operational picture, coordinating sensor and ISR tasking, and making the call on escalation — QRF alerts, higher headquarters notifications, that kind of thing. That night we were short an intel analyst, so the S2 shop was thinner than usual, and we only had one UAV available for the whole sector.

Interviewer: Walk me through what happened, starting from the first indication something was off.

Participant: Around 0215 a perimeter sensor near NAI-7, up on the northern boundary, logged a motion alert. Single sensor, no visual confirmation, and the weather that night — some ground fog — was already degrading sensor reliability. We didn't have any HUMINT or SIGINT corroborating it yet. Normally that's the kind of thing you'd log and keep an eye on. But I'll be honest, that specific sensor and that specific stretch of perimeter rang a bell for me. About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away.

Interviewer: What exactly about the current alert reminded you of that earlier incident?

Participant: Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way.

Interviewer: Okay. What happened next?

Participant: I had the S2 analyst start pulling historical activity for the sector while I looked at tasking the UAV. That's where things got tight, because we only had the one asset and there were competing requests elsewhere in the sector that night.

Interviewer: Let's stay on that first call for a second — classifying the alert as elevated. What alternatives did you consider?

Participant: I could've left it routine and waited for more data, or reached out to the adjacent unit for corroboration before deciding priority. Comms with them were spotty that night, intermittent SATCOM, so that would've cost time. I went with elevating it based on what I already knew.

Interviewer: How confident were you in that classification at the time?

Participant: Moderately. I didn't have hard evidence, just the pattern match in my head to the earlier event.

Interviewer: Understood. So then you moved to the ISR tasking decision — walk me through that.

Participant: Right, with only one UAV, I had to justify diverting it to NAI-7 over the other requests. To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first.

Interviewer: Were there other sources you could have checked?

Participant: Sure, there's the adjacent-unit SIGACT log and a sector-wide pattern-of-life database that tracks things like livestock movement and civilian traffic patterns near the perimeter. Both were accessible that night despite the comms issue — the pattern-of-life database is stored locally, actually.

Interviewer: Did you look at those before tasking the UAV?

Participant: No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later.

Interviewer: What made you stick with just the own-sector feed?

Participant: Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes.

Interviewer: What did the UAV feed show once it arrived on station?

Participant: Ambiguous thermal signatures. Could've been a small dismounted element, could've been livestock — genuinely hard to tell from the imagery alone. No weapons visible, no confirmed hostile indicators.

Interviewer: What did you do with that information?

Participant: I put the QRF on 15-minute alert status.

Interviewer: What alternatives were on the table at that point?

Participant: I could've held the current posture and requested more UAV dwell time to get a clearer picture, or asked the adjacent unit to send a ground patrol to verify visually before touching QRF readiness at all.

Interviewer: What tipped you toward alerting QRF instead of those options?

Participant: We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time.

Interviewer: Did the thermal evidence itself favor the ambush interpretation over livestock?

Participant: Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other.

Interviewer: What happened after QRF went to alert status?

Participant: Additional analyst review came back later and assessed the signatures as most consistent with livestock movement, based on movement speed and clustering patterns. QRF was never launched, just held at readiness.

Interviewer: How did you handle the final reporting for shift change?

Participant: I wrote it up as a genuinely mixed picture — noted the initial elevation, the QRF alert, and then the follow-up analyst assessment leaning non-hostile. I didn't want to call it a clean false alarm because the imagery was ambiguous enough that I couldn't rule out the dismounted-element read. I also didn't want to overstate it as an ongoing threat given what the analyst found. Higher headquarters ended up asking for a follow-up clarification the next day, which is pretty normal for anything left open like that.

Interviewer: Was there a point where you considered recommending a sensor review for NAI-7 instead?

Participant: I mentioned it as a secondary note, since that spot generates a fair number of ambiguous alerts, but I didn't want to bury the main SITREP under an infrastructure recommendation when the operational question was still open.

Interviewer: Stepping back — if the alert had come in during a quiet stretch with no recent similar incident in your memory, do you think you'd have classified it the same way?

Participant: Probably not as quickly to elevated. I think I'd have waited for the S2 pull before deciding priority.

Interviewer: If you'd checked the adjacent-unit and pattern-of-life data first, before your own-sector feed, do you think the tasking decision changes?

Participant: The UAV probably still goes to NAI-7 — that part of the call felt justified regardless. But I think how I framed the justification would've been different, maybe more grounded in actual cross-referenced history instead of just what was in front of me.

Interviewer: And if you hadn't run that ambush rehearsal in training recently, would you have read the thermal imagery differently?

Participant: Yeah, I think so. Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way.

Interviewer: Last question — looking back with everything you know now, what would you change?

Participant: Honestly, probably slow down at each of those first three points and force myself to check the wider data before trusting my first read. None of the individual calls were unreasonable given what I had in front of me, but I can see now where I leaned on what came to mind fastest instead of what was actually available.

Interviewer: That's really helpful. Thanks for walking through it in that much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Biased_3",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Joint Operations Center (JOC) Watch Officer / Battle Captain",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Perimeter Anomaly at FOB Sentinel: Night Shift Escalation",
    "scenario_summary_internal": "During an overnight shift at a forward operating base's Joint Operations Center, a Battle Captain receives an ambiguous sensor/HUMINT indicator of possible hostile activity near the perimeter's northern named area of interest (NAI). With a single ISR asset, degraded communications with an adjacent unit, and shift-change time pressure, the officer must triage the report, allocate limited reconnaissance capability, decide whether to alert the Quick Reaction Force (QRF), and finally characterize the event for the shift log and higher headquarters. The incident tests how recalled precedent, habitual information-search patterns, and vividly imagined threat scenarios shape risk judgments under uncertainty.",
    "occupational_realism": {
      "objective": "Correctly assess an ambiguous perimeter threat indicator and allocate scarce ISR and response assets without triggering unnecessary QRF activation or missing a genuine threat.",
      "setting": "Joint Operations Center (JOC) at Forward Operating Base Sentinel, 0200-0500 local, night shift with reduced staffing and intermittent SATCOM connectivity to an adjacent sector's watch floor.",
      "constraints": [
        "Only one UAV/RPA (ISR asset) available for tasking during the shift window",
        "Degraded communications link with adjacent unit's operations center",
        "Shift-change reporting deadline in three hours",
        "QRF activation requires justification in the after-action log and carries opportunity cost for other taskings",
        "Watch floor is short one intelligence analyst due to illness"
      ],
      "stakeholders": [
        "Battle Captain (interviewee)",
        "Shift NCOIC",
        "On-duty S2 intelligence analyst",
        "QRF commander",
        "Higher headquarters liaison officer",
        "Adjacent unit watch officer"
      ],
      "technical_terms_to_use": [
        "JOC", "Battle Captain", "watch officer", "SIGACT", "ISR", "UAV/RPA", "QRF", "SITREP", "pattern-of-life", "sensor cueing", "named area of interest (NAI)", "common operational picture (COP)", "TOC", "shift log"
      ],
      "technical_terms_to_avoid": [
        "availability heuristic", "confirmation bias", "anchoring", "cognitive bias", "heuristic", "recall bias", "search set bias", "imaginability bias", "retrievability bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "A perimeter sensor logs a single unconfirmed motion alert near NAI-7, no visual confirmation",
          "No corroborating HUMINT or SIGINT reporting yet received",
          "Weather and lighting conditions reduce sensor reliability"
        ],
        "new_information_after_decision": [
          "Sensor alert is logged as elevated-priority in the COP",
          "S2 analyst begins pulling historical activity data for the sector"
        ],
        "alternatives": [
          "Log the alert as routine/low-priority pending further data",
          "Immediately elevate the alert to high-priority based on recalled precedent",
          "Request adjacent unit corroboration before classifying priority"
        ],
        "intended_action": "Battle Captain classifies the alert as high-priority, prompted by vivid recollection of a similar-looking infiltration attempt weeks earlier, without first checking whether the current indicator actually matches that precedent's specific signature."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Only one UAV/RPA available for tasking",
          "Multiple competing tasking requests exist across the sector",
          "S2 section maintains several intelligence repositories: own-sector SIGINT summaries, adjacent-unit SIGACT logs, and a sector-wide pattern-of-life database"
        ],
        "new_information_after_decision": [
          "UAV is tasked toward NAI-7 based on a narrow review of own-sector reporting only",
          "Adjacent-unit historical data (later found relevant) was never consulted"
        ],
        "alternatives": [
          "Pull data from own-sector SIGINT summaries only (the readily available, habitual source)",
          "Cross-check adjacent-unit SIGACT logs and the sector-wide pattern-of-life database before tasking",
          "Defer tasking decision until the S2 analyst completes a full-spectrum review"
        ],
        "intended_action": "Battle Captain directs the ISR tasking decision using only the familiar own-sector SIGINT feed that comes readily to mind, without expanding the information search to adjacent-unit or pattern-of-life repositories that were equally accessible."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "UAV feed shows ambiguous thermal signatures near NAI-7, consistent with either livestock or a small dismounted element",
          "No confirmed weapons or hostile intent observed",
          "Recent JOC training exercise rehearsed a small-unit ambush scenario in similar terrain"
        ],
        "new_information_after_decision": [
          "QRF is placed on 15-minute alert status",
          "Additional analyst review later assesses the signatures as most consistent with livestock movement"
        ],
        "alternatives": [
          "Maintain current alert posture and request additional UAV dwell time for clarification",
          "Alert QRF to 15-minute readiness based on a vividly imagined ambush scenario",
          "Request adjacent-unit ground patrol to visually verify before any QRF posture change"
        ],
        "intended_action": "Battle Captain elevates QRF readiness because the ambush scenario from the recent training exercise is easy to picture in vivid detail, making that outcome feel more probable than the more mundane livestock explanation, despite the ambiguous evidence supporting either interpretation equally."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Follow-up analyst assessment leans toward a non-hostile explanation (livestock/pattern-of-life)",
          "QRF was placed on alert but not launched",
          "Shift-change SITREP is due to higher headquarters"
        ],
        "new_information_after_decision": [
          "Event is logged in the shift log and passed to the incoming Battle Captain",
          "Higher headquarters requests a follow-up clarification the next day"
        ],
        "alternatives": [
          "Characterize the event as a resolved false alarm with no further action",
          "Characterize the event as an unresolved indicator warranting continued monitoring",
          "Recommend a sector-wide review of NAI-7 sensor placement"
        ],
        "intended_action": "Battle Captain writes a balanced SITREP entry noting both the initial escalation and the analyst's subsequent non-hostile assessment, without an intended bias instance at this phase; alternative explanations are treated on their evidentiary merits."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you were doing when the first alert came in.",
        "What was your role and responsibility during this shift?"
      ],
      "timeline_reconstruction": [
        "What happened right after the sensor alert appeared on the COP?",
        "What did you do between tasking the UAV and receiving the thermal imagery?",
        "How did the situation evolve after the QRF was placed on alert?"
      ],
      "decision_point_probes": [
        "What specific cues made you classify the alert the way you did?",
        "What information sources did you consult before tasking the UAV, and were there others available?",
        "What alternatives did you consider before recommending QRF readiness?",
        "What was the basis for your final characterization in the shift log?",
        "Had you seen anything like this before? Did that influence your judgment?",
        "How much time pressure were you under at each of these moments?",
        "How confident were you in the evidence at each stage, and why?"
      ],
      "closing_hypotheticals": [
        "If the sensor alert had come in during a quiet week with no recent similar incidents, would your initial classification have differed?",
        "If the adjacent-unit data had been the first thing you checked instead of your own-sector feed, do you think the ISR tasking decision would have changed?",
        "If you hadn't recently rehearsed an ambush scenario in training, would you have assessed the thermal signature differently?",
        "Looking back, what would you do differently with the same information available at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "MD3_retr_01",
        "bias": "Retrievability Bias",
        "decision_point": 1,
        "mechanism": "A recent, emotionally salient personal memory (a prior infiltration attempt) is more easily retrieved than base-rate or dissimilar precedent, inflating perceived likelihood of the current ambiguous alert being a genuine threat.",
        "affected_reasoning_operation": "Initial probability/priority classification of an ambiguous sensor alert",
        "evidence_available_at_time": [
          "Single unconfirmed motion alert, no visual confirmation",
          "No corroborating reports yet",
          "Degraded sensor reliability due to weather"
        ],
        "required_textual_manifestation": "Interviewee explains classifying the alert as high-priority primarily because it 'reminded him of' the specific recent infiltration incident, without articulating an evidentiary basis for why the current alert actually resembles that incident's signature.",
        "plausible_nonbias_interpretation": "A cautious officer reasonably erring toward higher priority given genuine sector risk and imperfect sensors.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "recall bias", "cognitive bias"]
      },
      {
        "instance_id": "MD3_ss_01",
        "bias": "Search set Bias",
        "decision_point": 2,
        "mechanism": "The officer restricts the scope of information search to the habitual, most familiar repository (own-sector SIGINT summaries) rather than the full set of equally accessible sources (adjacent-unit logs, pattern-of-life database), skewing the evidentiary basis for the tasking decision toward whatever that narrow search set happened to contain.",
        "affected_reasoning_operation": "Evidence-gathering and information-source selection prior to ISR asset tasking",
        "evidence_available_at_time": [
          "Own-sector SIGINT summaries readily open on the COP terminal",
          "Adjacent-unit SIGACT logs and sector-wide pattern-of-life database equally available but not queried",
          "Single ISR asset requiring justified tasking"
        ],
        "required_textual_manifestation": "Interviewee describes pulling only the familiar own-sector feed to justify the tasking decision and, when asked directly, acknowledges the other repositories existed but were not part of his habitual search routine that night.",
        "plausible_nonbias_interpretation": "Time pressure reasonably limited how many sources could be checked before tasking a scarce asset.",
        "strength": "subtle",
        "do_not_make_explicit": ["search set bias", "sampling bias", "information search bias"]
      },
      {
        "instance_id": "MD3_im_01",
        "bias": "Imaginability Bias",
        "decision_point": 3,
        "mechanism": "A vividly rehearsed ambush scenario from recent training is easy to visualize in concrete detail, causing the officer to judge that outcome as more probable than an equally evidenced but less vividly imaginable mundane explanation (livestock movement).",
        "affected_reasoning_operation": "Risk assessment and QRF readiness decision based on ambiguous thermal imagery",
        "evidence_available_at_time": [
          "Ambiguous thermal signatures consistent with either livestock or dismounted personnel",
          "No confirmed weapons or hostile intent",
          "Recent training exercise rehearsing a similar ambush scenario"
        ],
        "required_textual_manifestation": "Interviewee explains that the ambush scenario 'played out' vividly in his mind based on the recent rehearsal, and that this mental picture weighed more heavily in raising QRF readiness than the objectively ambiguous thermal evidence itself.",
        "plausible_nonbias_interpretation": "Prudent force-protection posture given inherent uncertainty and the cost asymmetry of an unaddressed ambush.",
        "strength": "moderate",
        "do_not_make_explicit": ["imaginability bias", "simulation heuristic", "vividness bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the biased-condition scenario with no paired control specified in this generation pass."
    },
    "counterfactual_specification": {
      "causal_variable": "Availability of adjacent-unit and pattern-of-life data at the moment of ISR tasking (autoselected as the counterfactual variable most tightly coupled to the Search set Bias instance)",
      "original_state": "Battle Captain consults only own-sector SIGINT summaries when tasking the UAV, omitting adjacent-unit SIGACT logs and pattern-of-life database despite their availability",
      "counterfactual_state": "Battle Captain's habitual workflow automatically surfaces adjacent-unit and pattern-of-life data alongside own-sector summaries at tasking time",
      "variables_to_hold_constant": [
        "Initial sensor alert content and ambiguity",
        "Single available ISR asset",
        "Time pressure and staffing shortfall",
        "Subsequent QRF and reporting decisions",
        "Personnel and stakeholders involved"
      ],
      "expected_causal_difference": "With broader data automatically available, the ISR tasking rationale would likely reference cross-source corroboration rather than a single familiar feed, potentially altering confidence language at decision point 2 without necessarily changing the tasking outcome itself.",
      "causal_test_question": "Does automatic surfacing of adjacent-unit and pattern-of-life data change the evidentiary basis the officer cites for the ISR tasking decision, independent of whether the same asset is ultimately tasked?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points exist in the timeline",
      "Confirm exactly 3 total intended bias instances (1 Retrievability, 1 Search set, 1 Imaginability)",
      "Confirm no bias terminology or explicit psychological labels appear in probes or intended actions",
      "Confirm decision point 4 contains no intended bias instance and presents balanced alternative explanations",
      "Confirm each instance has a distinct decision point, evidence source, and reasoning operation",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points and probe density",
      "Confirm consequences at each decision point do not mechanically prove or disprove bias presence"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Retrievability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as reliance on an easily-recalled recent personal precedent rather than base-rate or matching-signature reasoning" },
      { "bias": "Search set Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as restricting information search to the habitual/familiar repository while equally accessible alternative sources go unconsulted" },
      { "bias": "Imaginability Bias", "occurrences": 1, "mechanism_constraint": "Must manifest as a vividly imaginable rehearsed scenario inflating perceived probability over an equally evidenced but less vivid alternative" }
    ],
    "target_bias_names": ["Retrievability Bias", "Search set Bias", "Imaginability Bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Retrievability Bias", "requested_occurrences": 1 },
      { "bias": "Search set Bias", "requested_occurrences": 1 },
      { "bias": "Imaginability Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias" },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias" },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias", "decision_point": 1 },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias", "decision_point": 2 },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias", "decision_point": 3 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "MD3_retr_01",
        "bias": "Retrievability Bias",
        "mechanism": "Ease of recalling a recent, salient infiltration precedent inflates perceived likelihood of the current ambiguous alert being a genuine threat",
        "affected_reasoning_operation": "Initial priority classification of an ambiguous sensor alert",
        "evidence_source": "Officer's own recollection of a prior incident, contrasted with the actual (weaker) evidentiary content of the current alert",
        "distinctiveness_requirement": "Must be tied specifically to memory recall driving classification, not to search-source restriction (MD3_ss_01) or to imagined future scenarios (MD3_im_01)"
      },
      {
        "instance_id": "MD3_ss_01",
        "bias": "Search set Bias",
        "mechanism": "Restriction of the information search to the habitual own-sector repository skews the evidentiary basis for ISR tasking despite equally available alternative repositories",
        "affected_reasoning_operation": "Evidence-gathering/source-selection prior to ISR tasking",
        "evidence_source": "Comparison between the repository actually consulted (own-sector SIGINT) and the repositories available but not consulted (adjacent-unit logs, pattern-of-life database)",
        "distinctiveness_requirement": "Must be tied specifically to which sources were queried, not to memory retrieval (MD3_retr_01) or to vividness of imagined outcomes (MD3_im_01)"
      },
      {
        "instance_id": "MD3_im_01",
        "bias": "Imaginability Bias",
        "mechanism": "A vividly rehearsed ambush scenario is easier to mentally simulate than the equally evidenced mundane alternative, inflating its perceived probability and driving QRF escalation",
        "affected_reasoning_operation": "Risk assessment and QRF readiness decision based on ambiguous thermal imagery",
        "evidence_source": "Officer's account of the mental scenario constructed from recent training, contrasted with the genuinely ambiguous thermal evidence",
        "distinctiveness_requirement": "Must be tied specifically to vividness/ease of mental simulation of an outcome, not to memory of a past real event (MD3_retr_01) or to which information sources were searched (MD3_ss_01)"
      }
    ],
    "intended_strength": [
      { "instance_id": "MD3_retr_01", "bias": "Retrievability Bias", "strength": "subtle" },
      { "instance_id": "MD3_ss_01", "bias": "Search set Bias", "strength": "subtle" },
      { "instance_id": "MD3_im_01", "bias": "Imaginability Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Availability of adjacent-unit and pattern-of-life data at ISR tasking time",
      "original_state": "Officer consults only own-sector SIGINT summaries",
      "changed_state": "Officer's workflow automatically surfaces adjacent-unit and pattern-of-life data alongside own-sector summaries",
      "variables_to_hold_constant": [
        "Initial sensor alert content and ambiguity",
        "Single available ISR asset",
        "Time pressure and staffing shortfall",
        "Subsequent QRF and reporting decisions",
        "Personnel and stakeholders involved"
      ]
    },
    "scenario_id": "MD_Biased_3",
    "domain_id": "MD",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "Occurrences spread across distinct decision points (1, 2, 3) per mechanism fit and narrative realism; decision point 4 reserved as bias-free reporting/closure phase; no bias assigned to more than one decision point; no two occurrences share a decision point so no cross-evidence-source separation was required.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Initial sensor alert content and ambiguity",
      "Single available ISR asset",
      "Time pressure and staffing shortfall",
      "Personnel and stakeholders involved",
      "Overall four-decision-point structure"
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
        "segment_type": "initial_priority_classification",
        "raw_interview_anchor": "The participant elevates the single-sensor NAI-7 alert because it reminds him of a recent infiltration and acknowledges relying on a pattern match rather than hard evidence.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "MD3_retr_01"
        ],
        "ground_truth_rationale": "Recent salient recollection drives threat prioritization despite weak current evidence and no signature comparison."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "information_source_selection",
        "raw_interview_anchor": "The participant justifies UAV tasking using only the familiar own-sector SIGINT feed, despite accessible adjacent-unit and pattern-of-life sources.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "MD3_ss_01"
        ],
        "ground_truth_rationale": "The search scope is restricted to the habitual repository rather than the full set of equally accessible sources."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_assessment",
        "raw_interview_anchor": "The participant describes the UAV thermal signatures as ambiguous and consistent with either livestock or a dismounted element, with no weapons or confirmed hostile indicators.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an evidence characterization without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "QRF_escalation_rationale",
        "raw_interview_anchor": "The participant says a recently rehearsed ambush scenario played out vividly in his mind and pushed him to alert QRF despite equally compatible evidence for livestock.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "MD3_im_01"
        ],
        "ground_truth_rationale": "Ease of mentally simulating the ambush inflates its perceived probability over an equally evidenced mundane alternative."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "post_decision_evidence_update",
        "raw_interview_anchor": "The participant reports the later analyst assessment favoring livestock and notes that QRF remained on alert without launching.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a subsequent evidence update and operational outcome, not a hidden bias occurrence."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "shift_change_reporting",
        "raw_interview_anchor": "The participant reports a balanced mixed picture in the SITREP, noting both escalation and the later non-hostile assessment.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification explicitly reserves this reporting phase as bias-free."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "secondary_recommendation",
        "raw_interview_anchor": "The participant mentions a sensor review as a secondary note but avoids letting it obscure the unresolved operational question.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a communication and prioritization choice without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "counterfactual_priority_reflection",
        "raw_interview_anchor": "The participant says he would likely have waited for the S2 pull during a quiet period without the recent similar incident.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a counterfactual reflection, not an additional occurrence."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "counterfactual_tasking_reflection",
        "raw_interview_anchor": "The participant says broader data might have changed the justification framing without necessarily changing the UAV tasking outcome.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is counterfactual reasoning about the search process, not a separate occurrence."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "counterfactual_imagery_reflection",
        "raw_interview_anchor": "The participant says that without the recent ambush rehearsal he might have requested more dwell time.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a counterfactual reflection on the already-localized QRF decision."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "closing_self_assessment",
        "raw_interview_anchor": "The participant reflects that he relied on what came to mind fastest and should have checked wider data before trusting his first read.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This retrospective summary does not create a fourth hidden instance."
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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of the CTA transcript. No experimental condition or intended bias count was inferred. Retrieved passages were used only for conceptual grounding; transcript evidence determines whether a bias occurred."
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
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias",
        "similarity-based judgment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood or classification of an event by superficial similarity to a previously observed or remembered instance, while underweighting diagnostic evidence and base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial sensor alert classification at NAI-7",
      "decision_point_description": "At 0215, deciding whether to treat a single unconfirmed perimeter sensor alert as routine or elevated.",
      "affected_reasoning_operation": "Classification and priority judgment under uncertainty",
      "bias_specific_mechanism": "The current alert matched the prior infiltration on two superficial features, location and time. The participant treated that resemblance as diagnostic and elevated priority without comparing actual signature data or requiring corroboration.",
      "manifestation_in_interview": "The participant said the alert 'rang a bell' and that his gut said the situation looked like the earlier infiltration, then bumped it to elevated priority in the COP before obtaining hard evidence.",
      "effect_on_reasoning_or_decision": "The single unconfirmed sensor alert was escalated to elevated priority in the COP, bypassing the usual watch-and-wait/corroboration step.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "About five weeks earlier we'd had an actual infiltration attempt in almost the same area, similar time of night. That one turned out real. So when this alert popped up, my gut said this looks like that, and I bumped it to elevated priority in the COP pretty much right away.",
          "evidence_explanation": "Shows a recent, salient prior event being used as the template for the current alert, leading to immediate escalation based on felt similarity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the location and the hour. Both around 0200, both NAI-7. I didn't go back and pull the actual signature data from that prior event to compare — sensor duration, movement pattern, anything like that. It just felt like the same situation, so I treated it that way.",
          "evidence_explanation": "Demonstrates that the judgment relied on superficial matching features rather than diagnostic signature data, which is core to representativeness."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Moderately. I didn't have hard evidence, just the pattern match in my head to the earlier event.",
          "evidence_explanation": "Confirms the reasoning operation was an explicit pattern match rather than evidence-based discrimination."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged moderate confidence and lack of hard evidence; he considered leaving the alert routine or obtaining adjacent-unit corroboration but rejected those alternatives. Later analyst review of subsequent imagery leaned non-hostile, though it did not specifically re-evaluate the initial sensor alert.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied to this analyzer specifically defined representativeness heuristic or its mechanism; the label is assigned from widely established cognitive-science knowledge rather than retrieved corpus evidence.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "anchoring-and-adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Relying too heavily on an initial piece of information or first-accessed source and making insufficient adjustment when additional relevant information is available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "UAV ISR tasking justification",
      "decision_point_description": "Deciding which sources to use to justify diverting the sole UAV to NAI-7 over competing sector requests.",
      "affected_reasoning_operation": "Information retrieval and justification for a resource allocation decision",
      "bias_specific_mechanism": "The habitual own-sector SIGINT feed was used as the initial informational anchor. The participant did not check accessible adjacent-unit SIGACT or the pattern-of-life database, leaving the tasking justification insufficiently adjusted from that first source.",
      "manifestation_in_interview": "The participant pulled only the own-sector summaries he checks nightly, used that feed to make the call, and tasked the UAV without consulting other available repositories that he later acknowledged were relevant.",
      "effect_on_reasoning_or_decision": "The UAV was tasked to NAI-7 on the basis of a narrower own-sector justification. The participant believed the final diversion might not have changed, but the reasoning and framing would have been more grounded with broader cross-referenced data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "To build that justification, I pulled the own-sector SIGINT summaries, the reports our own analysts had generated over the past couple weeks. That's the feed I always have open on my terminal, it's second nature to check that first.",
          "evidence_explanation": "Shows that the first-pulled source was the familiar, habitually checked feed, establishing the informational anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. I used the own-sector summaries to make the call and tasked the UAV toward NAI-7 on that basis. Looking back, the adjacent-unit log had some relevant history for that stretch of terrain that I didn't know about until later.",
          "evidence_explanation": "Shows he made the call based on the initially accessed source despite accessible alternatives, and later learned there was relevant history elsewhere."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Habit, mostly. That's the one I check every night, it's fast, and with the clock running on the shift-change SITREP I didn't feel like I had time to dig through three different repositories. In hindsight the pattern-of-life database would've taken maybe five extra minutes.",
          "evidence_explanation": "Shows incomplete adjustment away from the initial source: additional relevant repositories were skipped even though one would have taken only about five minutes."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the pattern-of-life database would have taken only five extra minutes and that the UAV likely still would have gone, limiting the effect to justification quality rather than necessarily the final allocation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passages address anchoring-and-adjustment generally and in AI-assisted decision-making. They support the label and mechanism but do not by themselves prove the occurrence.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent research has elaborated upon it. In brief, it has been observed people make estimates based on an initial answer, and adjustments from there based on additional information. Tversky and Kahneman put it, “adjustments are typically insufficient.”",
          "mechanism_supported_by_source": "Anchoring-and-adjustment: people start from an initial answer and insufficiently adjust with additional information.",
          "relevance_to_this_occurrence": "The participant started from the habitual own-sector feed and did not adequately adjust with accessible additional repositories."
        },
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Anchoring-and-adjustment as a resource-rational tradeoff; adjustment away from an initial anchor is often insufficient under time constraints.",
          "relevance_to_this_occurrence": "The participant cited time pressure as a reason for not checking additional repositories, consistent with incomplete adjustment away from the initially accessed feed."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "ease of imagination",
        "vividness heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Assessing the likelihood or plausibility of an interpretation by how easily and vividly it can be brought to mind or mentally simulated, rather than by objective evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "QRF alert decision after ambiguous thermal imagery",
      "decision_point_description": "Deciding whether to place QRF on 15-minute alert, hold current posture, or request more UAV dwell time.",
      "affected_reasoning_operation": "Interpretation of ambiguous thermal imagery and escalation readiness decision",
      "bias_specific_mechanism": "A recent, vivid training exercise made the ambush scenario easy to imagine and mentally simulate. The livestock explanation was not as vivid, so the participant treated the easily imagined scenario as more likely despite equal evidence.",
      "manifestation_in_interview": "The participant said he could 'basically see' the rehearsed ambush scenario and 'picture exactly how it would unfold,' and he explicitly stated the livestock explanation did not have the same vividness.",
      "effect_on_reasoning_or_decision": "He placed QRF on 15-minute alert instead of holding current posture or requesting further UAV dwell time, despite ambiguous thermal signatures with no confirmed hostile indicators.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd just run a training exercise a couple weeks prior that rehearsed almost this exact scenario — small-unit ambush approaching from that same kind of terrain, dismounted element using thermal-masking terrain features. When I looked at that imagery, I could basically see that rehearsed scenario playing out. It was vivid, like I could picture exactly how it would unfold if it were real. That's what pushed me to alert QRF rather than sit on more dwell time.",
          "evidence_explanation": "Shows a mentally available recent training scenario being used as a vivid simulation and driving the escalation decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, if I'm honest. The signatures were consistent with either. It was more that the ambush scenario was the one I could picture clearly, step by step, from the training run. The livestock explanation didn't have that same vividness to it, even though the evidence didn't really favor one over the other.",
          "evidence_explanation": "Explicitly shows interpretation was based on vividness or ease of imagination rather than diagnostic evidence, which is the core availability mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, I think so. Without that scenario fresh in my head, I might have leaned toward requesting more dwell time instead of alerting QRF right away, since the imagery on its own really didn't point clearly either way.",
          "evidence_explanation": "Counterfactual admission supports the conclusion that the easily available training scenario, not the imagery itself, caused the QRF alert."
        }
      ],
      "correction_or_counterevidence": "The imagery was objectively ambiguous and the participant acknowledged it did not favor either interpretation. Later analyst review assessed the signatures as most consistent with livestock, and QRF was never launched.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied to this analyzer specifically defined the availability heuristic or its imaginative-vividness route; the label is assigned from widely established cognitive-science knowledge rather than retrieved corpus evidence.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus passages did not include definitions or mechanisms for representativeness or availability heuristics; those labels are based on general knowledge and are disclosed as such.",
    "The anchoring occurrence has a plausible competing time-pressure/habit explanation, so it was rated moderate rather than high.",
    "Some retrieved passages contained OCR artifacts; only retrieved text exactly as supplied was used."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Biased_3_Sonnet_on",
  "interview_id": "MD_Biased_3",
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
