You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our internal review process, not a disciplinary hearing — you can decline to answer anything. Can you start by telling me your role on this voyage?

Participant: Sure. I'm master of the Kestrel Bay, bulk carrier, about 76,000 deadweight. This was the inbound leg to Rotterdam, Berth 7, with a grain cargo that had a fairly tight delivery clause attached to it.

Interviewer: And before we get into the specifics — what did you know about the passage plan going in?

Participant: The passage plan had been filed and approved before we sailed from the load port. Standard route through the Maasgeul into the Nieuwe Waterweg. Nothing unusual about it at that stage.

Interviewer: Okay. Let's start with your account of what happened, in your own words, and then we'll go back through it in more detail.

Participant: Right, so we were maybe three hours out from the tidal gate when NAVTEX came through with an update — a newly surveyed shoal patch near our filed track, reduced depth compared to the charted figure. There was an alternate channel that was deeper, but it would've added about forty minutes to the transit. Given our tidal window was already tight because of the charter penalty clause on the cargo, I decided to stick with the original plan. It had already been coordinated with the agent and the pilot station, and my read at the time was that the revision was probably minor — these shoal notices come through fairly often and a lot of them are conservative. Chief Officer flagged afterward that our under-keel clearance margin near that patch would be tighter than usual given the datum tide, and once you add squat effect at our transit speed, the margin gets thinner still. But by then we were committed to the route.

We came into the approach channel around dusk, patchy fog rolling in, and a squall building further out. ECDIS had the countdown to the tidal gate running prominently on the display — that was the thing everyone kept glancing at, because if we missed it we'd be looking at hours of delay and tugs and pilot slots getting reshuffled. Radar showed a handful of contacts, small fishing vessels bunched near the edge of the fairway, plus one slower, ambiguous return that the OOW mentioned in passing near the deep-water part of the track. I told him to keep an eye on the deep water and let me know if anything closed in — my attention at that point was really on the gate timing and getting the berth logistics locked down with the agent.

About twenty minutes later the Chief Engineer called up to report the main engine cooling water temperature was running above normal. He recommended dropping to half power for about twenty minutes to inspect it. I've had that alarm before — more than once in fifteen years — and it's almost always a sensor lag issue that resolves itself. So I told him I'd seen it before and we'd hold speed. He called back later saying the trend didn't look like the usual lag pattern, more sustained, but by then VTS had come through with a traffic advisory identifying that ambiguous contact as a drifting fishing vessel without power, closer to the centerline than we'd plotted. That's when things got busy.

Interviewer: Let's walk through the sequence again, a bit slower this time. What information were you drawing on at each stage?

Participant: NAVTEX for the shoal update, ECDIS for the route and the gate countdown, radar and ARPA for traffic, VTS for the broader picture, and engine room reports over the phone. Each one came in at a different point, so it wasn't like I had the full picture at any single moment — you're building it as you go.

Interviewer: And what were you and the officers focused on as you entered the channel?

Participant: Mostly the tide gate and the berth coordination. That was the pressure point. The OOW was watching traffic, I was managing timing and talking to the agent about tug availability.

Interviewer: Let's go back to the NAVTEX update. What alternatives did you weigh, and why did you choose to keep the original route?

Participant: The alternate channel was the obvious other option, and slowing down to get an updated survey confirmation was theoretically on the table too. But re-filing the route means coordinating again with the pilot station and probably losing the slot anyway, so functionally it felt like the same outcome as just taking the delay. The original plan was already approved and everyone downstream was expecting it. I didn't really re-run the numbers on the new depth against our draft and the tide — it felt like something that would've been flagged harder by the agency if it were serious.

Interviewer: During the channel transit, what cues were you attending to, and is there anything you think you might have missed?

Participant: Honestly, the gate countdown was dominating my attention, and the berth call. The fishing boat cluster registered as background traffic — normal for that stretch. The one ambiguous contact, I noted it, told the OOW to watch it, but I didn't personally re-plot it or push VTS for a read on it myself. In hindsight there was a window there where I could've asked more directly what that contact actually was instead of just filing it as "probably fine, keep an eye on it."

Interviewer: When the Chief Engineer raised the temperature reading, what gave you confidence in your call to hold speed?

Participant: Mostly just having seen that specific alarm pattern before, multiple times, without it turning into anything. It's a judgment built on a lot of runs on similar plant. I didn't ask him to pull fresh diagnostics before deciding — I made the call fairly quickly based on that history.

Interviewer: When VTS issued the traffic advisory, what options did you weigh before acting?

Participant: Abort the gate attempt entirely and anchor to reassess, take a smaller late adjustment to clear both the contact and the shoal, or call for pilot and tug assistance immediately and slow right down. I went with the smaller adjustment — full abort felt disproportionate given how close we already were, and I judged we had enough margin to thread it.

Interviewer: What information, if it had arrived earlier, would have changed your decision at the route stage?

Participant: If the NAVTEX update had come through before we'd filed and departed, I think I'd have just taken the deeper channel without a second thought — there'd have been no schedule cost attached to it yet. Timing of when it landed relative to our commitment really shaped how I weighed it.

Interviewer: Looking back now, how clear were the warning signs about the shoal at the time you made that routing call?

Participant: Looking back, it was pretty clear that the alternate channel was the sounder option — the depth reduction plus squat plus the tide state, once you line it all up, points obviously to being cautious there. It's hard now not to see it as something I should have caught immediately.

Interviewer: What would you do differently if you faced the same engine-temperature situation again?

Participant: Probably ask for a fresh reading or a short trend check before deciding, rather than leaning purely on what I remembered from past incidents.

Interviewer: Last one — if the fishing vessel hadn't been drifting without power, just moving normally, do you think the outcome would have played out differently given how the attention was allocated during the transit?

Participant: Probably would've passed without anyone thinking twice about it, which is part of why it didn't feel urgent in the moment. The margin for error was just a lot thinner than any of us realized while it was actually happening.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MO_Biased_4",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Ship Master / Vessel Captain",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Tidal Gate at Rotterdam: The Kestrel Bay Passage",
    "scenario_summary_internal": "Master of the bulk carrier MV Kestrel Bay must thread a narrow tidal window into Port of Rotterdam via a channel affected by a newly surveyed shoal, deteriorating visibility, a developing main-engine cooling anomaly, and charter-penalty schedule pressure. Four sequential decisions (route retention, attention allocation in the narrow channel, response to an engine alarm, and post-incident reconstruction) are engineered to independently elicit Status Quo Bias, Selective Attention/Inattentional Blindness, Overconfidence Bias, and Hindsight Bias respectively, without ever naming or explaining these constructs in the interview text.",
    "occupational_realism": {
      "objective": "Bring the vessel safely alongside Berth 7, Port of Rotterdam, within a closing tidal window, while managing a perishable cargo penalty clause, deteriorating weather, and an emergent propulsion concern.",
      "setting": "Approach and inbound transit of the Maasgeul/Nieuwe Waterweg approach channel toward Rotterdam, dusk into night, patchy fog and a developing squall, moderate vessel traffic including fishing activity near the fairway edge.",
      "constraints": [
        "Tidal window at the lock/berth closes in approximately 3 hours from the first decision point",
        "Charter party penalty clause for missed berthing slot",
        "Perishable/time-sensitive bulk cargo aboard",
        "Reduced visibility from patchy fog and squall activity",
        "Limited tug and pilot boarding slots if the ETA slips",
        "Main engine cooling water temperature trending upward",
        "Company standing orders emphasizing schedule adherence when 'safely practicable'"
      ],
      "stakeholders": [
        "Ship Master (interviewee)",
        "Chief Officer / Officer of the Watch",
        "Chief Engineer",
        "VTS Rotterdam",
        "Harbor Pilot",
        "Company Operations / Charterer representative"
      ],
      "technical_terms_to_use": [
        "passage plan",
        "ECDIS",
        "NAVTEX",
        "under keel clearance (UKC)",
        "squat effect",
        "ARPA/radar plot",
        "tidal gate",
        "VTS traffic report",
        "AIS contact",
        "sea speed / half power",
        "datum tide",
        "fairway/traffic separation scheme"
      ],
      "technical_terms_to_avoid": [
        "hindsight bias",
        "overconfidence bias",
        "status quo bias",
        "selective attention",
        "inattentional blindness",
        "cognitive bias",
        "heuristic",
        "anchoring",
        "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Original passage plan via the primary channel was filed and approved before departure",
          "A NAVTEX update received en route reports a newly surveyed shoal patch with reduced depth near the filed route",
          "Alternate deeper channel adds approximately 40 minutes transit time",
          "Tidal window at the destination lock is already tight"
        ],
        "new_information_after_decision": [
          "Chief Officer flags that under-keel clearance margin near the shoal will be tighter than usual at the current datum tide",
          "Squat effect at planned speed further reduces effective clearance"
        ],
        "alternatives": [
          "Retain the originally filed passage plan through the shoal-affected channel",
          "Amend the route to the alternate deeper channel per the NAVTEX update",
          "Reduce speed and request an updated survey/VTS confirmation before deciding"
        ],
        "intended_action": "Master retains the original filed plan, reasoning that re-filing and coordinating a route change would cost time and that the shoal warning is 'probably a minor revision,' without independently re-evaluating the new depth data against current tide and draft."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vessel is entering the narrow approach channel in patchy fog",
          "ECDIS prominently displays a countdown to the tidal gate closure",
          "Radar/ARPA shows multiple returns including a cluster of small fishing vessels near the fairway edge",
          "OOW reports one ambiguous, slow-moving contact near the deep-water route"
        ],
        "new_information_after_decision": [
          "VTS later transmits a traffic advisory naming the same contact as a drifting fishing vessel without engine power",
          "The contact's closest point of approach narrows faster than initially plotted"
        ],
        "alternatives": [
          "Keep attention on the tidal-gate countdown and cargo/berth logistics while trusting the OOW to call all contacts",
          "Actively cross-check ARPA plots and personally query the ambiguous contact",
          "Slow further and request a dedicated VTS traffic update on fishing activity in the fairway"
        ],
        "intended_action": "Master remains focused on the tide-gate timing and berth coordination, instructs the OOW to 'just watch the deep water,' and does not personally query or re-plot the ambiguous slow contact until VTS calls it out."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief Engineer reports a rise in main engine cooling water temperature above normal range",
          "Chief Engineer recommends reducing to half power for roughly 20 minutes to inspect the cooling system",
          "Master has encountered similar temperature alarms multiple times over a 15-year career without resulting incident",
          "Reducing power now risks missing the tidal gate"
        ],
        "new_information_after_decision": [
          "Temperature continues to climb over the next 30 minutes",
          "Chief Engineer repeats the recommendation with more urgency, noting the trend is not consistent with prior sensor-lag episodes"
        ],
        "alternatives": [
          "Reduce speed/power per the Chief Engineer's recommendation",
          "Maintain full sea speed, treating the reading as likely sensor lag based on past experience",
          "Reduce power moderately as a compromise while continuing toward the gate"
        ],
        "intended_action": "Master maintains full sea speed, telling the Chief Engineer 'I've seen this before, it's just a sensor lag,' relying on personal track record rather than requesting fresh diagnostic data before continuing."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "VTS issues a late warning about the drifting fishing vessel now close to the fairway centerline",
          "Under-keel clearance near the shoal is now marginal given tide, squat, and draft",
          "Engine temperature remains elevated but has not triggered a shutdown",
          "Master must decide on late avoiding action and whether to abort the tidal-gate attempt"
        ],
        "new_information_after_decision": [
          "Vessel takes late avoiding action, passes the fishing vessel with a reduced but adequate margin, and clears the shoal with a narrow UKC margin",
          "Vessel makes the berth slightly behind schedule but without grounding, collision, or engine failure",
          "Post-arrival debrief and this interview reconstruct the earlier decisions"
        ],
        "alternatives": [
          "Take immediate large-scale avoiding action and abort the tidal-gate attempt, anchoring to reassess",
          "Take a smaller late course/speed adjustment to clear the contact and shoal while preserving the tidal gate",
          "Request pilot/tug assistance immediately and slow to minimum safe speed"
        ],
        "intended_action": "Master takes the smaller late adjustment, clears both hazards narrowly, and reaches berth slightly late; during the debrief interview, when asked to explain the original route decision, the master characterizes the shoal warning as having been 'completely clear at the time,' asserting the correct choice was obvious rather than acknowledging the genuine ambiguity that existed before the outcome was known."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role and responsibilities on this voyage leg.",
        "Walk me through what you knew about the passage before you received the NAVTEX update."
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from receiving the NAVTEX update to arriving at berth.",
        "What information sources were you drawing on at each stage — ECDIS, radar, VTS, engine room reports?",
        "What were you and your officers focused on as you entered the narrow channel?"
      ],
      "decision_point_probes": [
        "What alternatives did you consider when the NAVTEX update came in, and why did you choose the one you did?",
        "What cues were you attending to during the channel transit, and what, if anything, might you have missed?",
        "When the Chief Engineer flagged the temperature rise, what made you confident in your assessment?",
        "When VTS called the traffic advisory, what options did you weigh before acting?"
      ],
      "closing_hypotheticals": [
        "If the NAVTEX update had arrived an hour earlier, would your route decision have changed?",
        "Looking back, how clear were the warning signs about the shoal at the time you made the routing decision?",
        "What would you do differently if you faced the same engine-temperature situation again?",
        "How much of your confidence in the engine reading came from this specific voyage versus your overall experience?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_04",
        "bias": "Status Quo Bias",
        "decision_point": 1,
        "mechanism": "Master defaults to the previously filed and approved passage plan despite new depth information, treating the cost of changing the plan as more salient than the cost of re-evaluating it",
        "affected_reasoning_operation": "Route re-evaluation under new information",
        "evidence_available_at_time": [
          "NAVTEX shoal update",
          "Filed/approved passage plan",
          "Tight tidal window"
        ],
        "required_textual_manifestation": "Master explicitly cites the existing filed plan and the hassle of re-coordination as reasons to not re-evaluate, rather than assessing the new depth data on its own merits",
        "plausible_nonbias_interpretation": "A reasonable master might rationally judge the extra 40-minute alternate route not worth the schedule cost if the shoal margin still appears adequate under a genuine (if brief) risk assessment",
        "strength": "subtle",
        "do_not_make_explicit": [
          "status quo bias",
          "default effect",
          "switching cost"
        ]
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 2,
        "mechanism": "Master's attention is captured by the salient tidal-gate countdown and berth logistics, causing an ambiguous but relevant radar/AIS contact to go unqueried until an external party (VTS) flags it",
        "affected_reasoning_operation": "Real-time cue selection and evidence sampling from radar/ARPA and OOW reports",
        "evidence_available_at_time": [
          "ECDIS tidal-gate countdown display",
          "ARPA plot showing multiple returns including one ambiguous slow contact",
          "OOW's initial mention of the ambiguous contact"
        ],
        "required_textual_manifestation": "Master describes directing focus toward timing/logistics and instructing the OOW to 'watch the deep water' without personally cross-checking the ambiguous contact until VTS calls it",
        "plausible_nonbias_interpretation": "Delegating contact-tracking to the OOW while the master manages overall passage timing is a normal division of bridge labor, not inherently a lapse",
        "strength": "moderate",
        "do_not_make_explicit": [
          "inattentional blindness",
          "selective attention",
          "tunnel vision"
        ]
      },
      {
        "instance_id": "cb_03",
        "bias": "Overconfidence Bias",
        "decision_point": 3,
        "mechanism": "Master weights personal experience with prior sensor-lag episodes more heavily than the Chief Engineer's current, specific recommendation and trend data, maintaining speed without seeking fresh verification",
        "affected_reasoning_operation": "Risk assessment and calibration of confidence in own judgment versus specialist input",
        "evidence_available_at_time": [
          "Chief Engineer's report of rising cooling water temperature",
          "Chief Engineer's explicit recommendation to reduce power",
          "Master's 15-year history of similar alarms resolving as sensor lag"
        ],
        "required_textual_manifestation": "Master states confidence based on personal track record ('I've seen this before') and declines the recommended power reduction without requesting updated diagnostics",
        "plausible_nonbias_interpretation": "An experienced master may have legitimate domain expertise that makes a measured deviation from a junior recommendation reasonable, especially under schedule constraints",
        "strength": "moderate",
        "do_not_make_explicit": [
          "overconfidence bias",
          "expertise bias",
          "miscalibration"
        ]
      },
      {
        "instance_id": "cb_01",
        "bias": "Hindsight Bias",
        "decision_point": 4,
        "mechanism": "In reconstructing the decision-1 routing choice after the outcome (a narrow but safe passage) is known, master retrospectively asserts the shoal warning was obviously decisive, understating the genuine ambiguity present at the time of the original decision",
        "affected_reasoning_operation": "Retrospective causal attribution and memory reconstruction of a prior decision, elicited via closing probe",
        "evidence_available_at_time": [
          "Known safe outcome of the voyage",
          "Master's own account of decision point 1",
          "Interviewer probe about clarity of warning signs at the time"
        ],
        "required_textual_manifestation": "Master states the shoal warning was 'completely clear' or the correct route 'obvious' at the time, in a way that is inconsistent with the genuine uncertainty described earlier in the same interview",
        "plausible_nonbias_interpretation": "A master might reasonably conclude, on sober reflection with full information, that the alternate route was the better choice without this reflecting a distortion of what was knowable beforehand",
        "strength": "subtle",
        "do_not_make_explicit": [
          "hindsight bias",
          "creeping determinism",
          "outcome bias"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable in this run: condition is 'biased' with no paired control requested."
    },
    "counterfactual_specification": {
      "causal_variable": "Timing of the NAVTEX shoal update relative to route commitment (auto-selected as the most decision-relevant single causal lever in this scenario)",
      "original_state": "NAVTEX update arrives after the passage plan is already filed and underway, when re-routing carries a visible schedule cost",
      "counterfactual_state": "NAVTEX update arrives before departure, when re-routing carries no schedule cost",
      "variables_to_hold_constant": [
        "Vessel type and cargo",
        "Weather and visibility conditions",
        "Engine cooling anomaly and its timing",
        "Tidal window constraint",
        "Crew composition and stated experience level"
      ],
      "expected_causal_difference": "Earlier warning timing removes the switching-cost pressure that supports the Status Quo Bias instance at decision point 1, allowing a test of whether the master's route choice changes when commitment cost is absent",
      "causal_test_question": "Does the master choose the alternate deeper channel when the same depth information arrives before any commitment cost exists, versus retaining the original plan when it arrives after commitment?"
    },
    "generation_checks": [
      "Exactly four decision points are present and each maps to exactly one intended bias instance",
      "No bias name, definition, or psychological explanation appears in probe wording or intended actions",
      "Each instance has a distinct evidence trace and reasoning operation from the other three",
      "Plausible non-bias explanations exist for every planned instance",
      "Narrative supports the 1,215–1,485 word target without repetitive exposition across four phases and four probe categories",
      "No unrequested bias (e.g., confirmation bias, sunk cost) is intentionally embedded"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Hindsight Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as retrospective causal attribution during decision-4 probe response about decision 1, not as a repeated summary"
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as real-time cue-sampling failure during the channel transit, distinct from any later summary of the event"
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as miscalibrated reliance on personal track record over specialist current data at the engine-alarm decision"
      },
      {
        "bias": "Status Quo Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as default retention of the pre-existing filed plan despite new information at decision point 1"
      }
    ],
    "target_bias_names": [
      "Hindsight Bias",
      "Selective Attention Bias or Inattentional Blindness",
      "Overconfidence Bias",
      "Status Quo Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Hindsight Bias", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 },
      { "bias": "Status Quo Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_04", "bias": "Status Quo Bias" },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "cb_03", "bias": "Overconfidence Bias" },
      { "instance_id": "cb_01", "bias": "Hindsight Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_04", "bias": "Status Quo Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Overconfidence Bias", "decision_point": 3 },
      { "instance_id": "cb_01", "bias": "Hindsight Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_04",
        "bias": "Status Quo Bias",
        "mechanism": "Default retention of previously filed passage plan despite new depth information",
        "affected_reasoning_operation": "Route re-evaluation under new information",
        "evidence_source": "NAVTEX shoal update versus filed passage plan",
        "distinctiveness_requirement": "Only instance tied to the pre-departure/route-filing decision; must not repeat in later phases"
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Attentional capture by tidal-gate countdown suppresses processing of an ambiguous radar/AIS contact",
        "affected_reasoning_operation": "Real-time cue selection from ARPA/radar and OOW reports",
        "evidence_source": "ARPA plot and OOW verbal report of ambiguous contact",
        "distinctiveness_requirement": "Distinct evidence source (radar/AIS contact) and moment (channel transit) from all other instances"
      },
      {
        "instance_id": "cb_03",
        "bias": "Overconfidence Bias",
        "mechanism": "Over-weighting of personal historical track record relative to current specialist diagnostic input",
        "affected_reasoning_operation": "Risk calibration versus specialist recommendation",
        "evidence_source": "Chief Engineer's temperature report and recommendation versus master's prior experience claim",
        "distinctiveness_requirement": "Distinct evidence source (engine room data) and decision (power/speed) from all other instances"
      },
      {
        "instance_id": "cb_01",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospective assertion that outcome-relevant information was obviously decisive at the time, contradicting the genuine ambiguity described earlier",
        "affected_reasoning_operation": "Retrospective causal attribution during closing probe",
        "evidence_source": "Master's own earlier account of decision 1 versus post-outcome probe response",
        "distinctiveness_requirement": "Only instance occurring in the post-outcome interview reconstruction; must not be conflated with the original decision-1 status quo instance"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_04", "bias": "Status Quo Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Overconfidence Bias", "strength": "moderate" },
      { "instance_id": "cb_01", "bias": "Hindsight Bias", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Timing of NAVTEX shoal update relative to route commitment",
      "original_state": "Update arrives after passage plan is filed and underway (switching cost present)",
      "changed_state": "Update arrives before departure (no switching cost)",
      "variables_to_hold_constant": [
        "Vessel type and cargo",
        "Weather and visibility conditions",
        "Engine cooling anomaly and its timing",
        "Tidal window constraint",
        "Crew composition and stated experience level"
      ]
    },
    "scenario_id": "MO_Biased_4",
    "domain_id": "MO",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One instance per named bias, each assigned to a distinct decision point (1–4) selected for mechanism fit: default-retention framing at the initial route decision (Status Quo), attentional-capture framing during the narrow-channel transit (Selective Attention/Inattentional Blindness), specialist-versus-self-trust framing at the engine alarm (Overconfidence), and retrospective-attribution framing during the closing probe about the near-miss outcome (Hindsight). No decision point received more than one occurrence of any single bias, satisfying the two-occurrence cap trivially since each bias occurs only once overall.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vessel type and cargo",
      "Weather and visibility conditions",
      "Engine cooling anomaly and its timing",
      "Tidal window constraint",
      "Crew composition and stated experience level"
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
          "segment_type": "route-selection rationale",
          "raw_interview_anchor": "Given our tidal window was already tight ... I decided to stick with the original plan.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_04"],
          "ground_truth_rationale": "The previously approved route remained the default after new shoal information, without a fresh depth assessment."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "post-decision commitment explanation",
          "raw_interview_anchor": "Chief Officer flagged afterward ... But by then we were committed to the route.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This reports later information and commitment, not a separately planned bias occurrence."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "attention-allocation decision",
          "raw_interview_anchor": "ECDIS had the countdown ... my attention at that point was really on the gate timing",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_02"],
          "ground_truth_rationale": "Gate timing and logistics captured attention while the reported ambiguous contact was delegated without personal inquiry."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "engine-alarm judgment",
          "raw_interview_anchor": "I've had that alarm before ... So I told him I'd seen it before and we'd hold speed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_03"],
          "ground_truth_rationale": "Past benign alarms outweighed the Chief Engineer's current recommendation without fresh diagnostics."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "route-choice retrospective elaboration",
          "raw_interview_anchor": "I didn't really re-run the numbers on the new depth against our draft and the tide",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This corroborates the route decision mapped to seg_001 rather than creating another occurrence."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "traffic-attention retrospective elaboration",
          "raw_interview_anchor": "The one ambiguous contact ... I didn't personally re-plot it or push VTS for a read",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This revisits the attention-allocation episode mapped to seg_003 rather than adding another occurrence."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "engine-judgment retrospective elaboration",
          "raw_interview_anchor": "Mostly just having seen that specific alarm pattern before ... I didn't ask him to pull fresh diagnostics",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This explains the same engine decision mapped to seg_004."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "late avoiding-action choice",
          "raw_interview_anchor": "I went with the smaller adjustment — full abort felt disproportionate",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The hidden manifest specifies no independent plan-continuation occurrence at this decision; the stated margin judgment and operational costs allow a non-bias interpretation."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "counterfactual route judgment",
          "raw_interview_anchor": "If the NAVTEX update had come through before we'd filed and departed",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The response identifies how commitment timing would change the choice; it is not another actual biased decision."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "post-outcome causal attribution",
          "raw_interview_anchor": "Looking back, it was pretty clear ... points obviously to being cautious there.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_01"],
          "ground_truth_rationale": "The master retrospectively treats the safer route as obvious despite describing uncertainty and discounting the warning at the original decision."
        },
        {
          "segment_id": "seg_011",
          "speaker": "Participant",
          "segment_type": "future-action judgment",
          "raw_interview_anchor": "Probably ask for a fresh reading or a short trend check",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a proposed verification step, not an additional biased occurrence."
        },
        {
          "segment_id": "seg_012",
          "speaker": "Participant",
          "segment_type": "counterfactual traffic judgment",
          "raw_interview_anchor": "Probably would've passed without anyone thinking twice about it",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The response speculates about a different vessel state and does not establish another actual bias."
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
    "analysis_scope_note": "Strictly transcript-grounded bias detection. No retrieved corpus passages were supplied; occurrences are labeled from established cognitive-science knowledge and corpus support is disclosed as unavailable."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Attentional tunneling",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Hindsight bias",
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
      "bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Plan continuation error",
        "Get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an existing plan or course of action even after new information indicates it may no longer be safe or optimal.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Routing decision after NAVTEX shoal update",
      "decision_point_description": "Whether to continue with the originally filed route or divert to the deeper alternate channel after the shoal survey update.",
      "affected_reasoning_operation": "Risk evaluation and route-selection decision under new hazard information",
      "bias_specific_mechanism": "Commitment to the already approved passage plan, schedule coordination, and downstream expectations made the new shoal warning feel insufficient to trigger a full re-evaluation; the original plan was treated as the default and the warning was minimized without recalculating under-keel clearance.",
      "manifestation_in_interview": "The participant reports receiving a newly surveyed reduced-depth shoal patch near the filed track, but decides to stick with the original plan. He later states that he did not re-run the numbers and assumed the agency would have flagged a serious hazard more strongly.",
      "effect_on_reasoning_or_decision": "The original route was retained without a fresh draft/tide/squat clearance calculation, narrowing the safety margin.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given our tidal window was already tight because of the charter penalty clause on the cargo, I decided to stick with the original plan.",
          "evidence_explanation": "Shows the continuation decision was tied to schedule pressure and the existing plan rather than a re-evaluation of the new hazard."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The original plan was already approved and everyone downstream was expecting it.",
          "evidence_explanation": "Explicitly frames the existing plan and coordination as a reason not to change course, a hallmark of plan continuation reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't really re-run the numbers on the new depth against our draft and the tide — it felt like something that would've been flagged harder by the agency if it were serious.",
          "evidence_explanation": "Demonstrates that the participant dismissed the updated hazard through an unverified assumption rather than active re-calculation."
        }
      ],
      "correction_or_counterevidence": "The Chief Officer later flagged that under-keel clearance near the patch would be tighter than usual due to tide and squat, but the participant reports the vessel was already committed to the route by then.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; this label and mechanism are assigned from general cognitive-science/human-factors knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Attentional tunneling",
      "alternative_labels": [
        "Cognitive tunneling",
        "Goal fixation",
        "Attentional narrowing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to allocate attention narrowly to a salient task or display and under-process peripheral information, even when that peripheral information may be safety-relevant.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Channel transit monitoring of an ambiguous radar contact",
      "decision_point_description": "How to allocate attention and respond to an ambiguous radar contact while approaching the tidal gate.",
      "affected_reasoning_operation": "Attention allocation and threat surveillance during high-workload transit",
      "bias_specific_mechanism": "The prominent ECDIS tidal-gate countdown and berth logistics task captured attention, causing the ambiguous radar contact to be processed only superficially as probably fine and delegated rather than verified.",
      "manifestation_in_interview": "The participant says the gate countdown was dominating his attention, the fishing boat cluster registered as background traffic, and he did not personally re-plot the ambiguous contact or push VTS for identification.",
      "effect_on_reasoning_or_decision": "The ambiguous contact was not identified as a drifting fishing vessel until VTS issued a later traffic advisory, reducing the response buffer.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "ECDIS had the countdown to the tidal gate running prominently on the display — that was the thing everyone kept glancing at",
          "evidence_explanation": "Identifies the display element that captured attention at routine intervals."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "my attention at that point was really on the gate timing and getting the berth logistics locked down with the agent",
          "evidence_explanation": "Explicitly places the participant's attention on the gate and berth tasks rather than on the ambiguous radar contact."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the gate countdown was dominating my attention, and the berth call.",
          "evidence_explanation": "Confirms the attentional capture during the transit."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The one ambiguous contact, I noted it, told the OOW to watch it, but I didn't personally re-plot it or push VTS for a read on it myself.",
          "evidence_explanation": "Shows that a potentially relevant peripheral contact remained unverified because attention stayed on the dominant task."
        }
      ],
      "correction_or_counterevidence": "The participant did note the contact and delegated monitoring to the OOW, which partially mitigated the missed identification; however, the contact was not personally re-checked or verified.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; this label and mechanism are assigned from general cognitive-science/human-factors knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood or cause of an event by the ease with which similar past instances come to mind, rather than by current diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Engine cooling-water over-temperature response",
      "decision_point_description": "Whether to reduce power immediately or hold speed when the Chief Engineer reported elevated cooling-water temperature.",
      "affected_reasoning_operation": "Diagnostic judgment and operational risk assessment of an engine alarm",
      "bias_specific_mechanism": "The participant retrieved frequent past cases of the same alarm pattern turning out to be sensor lag and used those remembered examples to classify the current event as probably benign, without gathering fresh trend data.",
      "manifestation_in_interview": "The participant states he had seen the alarm before, judged it almost always to be sensor lag, made the hold-speed call quickly from that history, and did not ask for fresh diagnostics first.",
      "effect_on_reasoning_or_decision": "The vessel held speed instead of slowing or investigating immediately; the Chief Engineer later reported the trend did not look like the usual lag pattern.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I've had that alarm before — more than once in fifteen years — and it's almost always a sensor lag issue that resolves itself.",
          "evidence_explanation": "Shows reliance on the availability of similar remembered events to judge the current alarm."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So I told him I'd seen it before and we'd hold speed.",
          "evidence_explanation": "The past-based judgment immediately translated into an operational risk decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't ask him to pull fresh diagnostics before deciding — I made the call fairly quickly based on that history.",
          "evidence_explanation": "Explicitly contrasts current diagnostic evidence with remembered history as the basis for the decision."
        }
      ],
      "correction_or_counterevidence": "The Chief Engineer called back later reporting that the trend did not look like the usual lag pattern, though by then attention had shifted to the VTS traffic advisory.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; this label and mechanism are assigned from general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Hindsight bias",
      "alternative_labels": [
        "Knew-it-all-along effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency, after an outcome is known, to overestimate the predictability or foreseeability of that outcome.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Retrospective assessment of shoal warning clarity",
      "decision_point_description": "Evaluating how clear the warning signs were at the time of the original routing decision.",
      "affected_reasoning_operation": "Retrospective causal and predictability judgment",
      "bias_specific_mechanism": "Knowledge of the later thin-margin outcome made the earlier depth reduction, tide state, and squat effect appear more obviously diagnostic than they were treated at the time; the participant now sees the hazard as something he should have caught immediately.",
      "manifestation_in_interview": "The participant states that looking back it was pretty clear the alternate channel was sounder and that the factors pointed obviously to being cautious; he also says it is hard now not to see it as something he should have caught immediately.",
      "effect_on_reasoning_or_decision": "The participant's retrospective account may overstate the clarity of the hazard at the time of the original routing call, potentially distorting the incident debrief.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, it was pretty clear that the alternate channel was the sounder option — the depth reduction plus squat plus the tide state, once you line it all up, points obviously to being cautious there.",
          "evidence_explanation": "Shows outcome knowledge making the combined hazard appear plainly predictable after the fact."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It's hard now not to see it as something I should have caught immediately.",
          "evidence_explanation": "Classic expression of hindsight bias: difficulty ignoring what is now known."
        }
      ],
      "correction_or_counterevidence": null,
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; this label and mechanism are assigned from general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overconfidence bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "VTS traffic-advisory response: choosing a smaller late adjustment rather than full abort",
      "supporting_interview_quote": "I judged we had enough margin to thread it.",
      "plausible_mechanism": "The participant may have overestimated the available navigation margin under time pressure and high workload; the later statement that the margin was a lot thinner than realized is consistent with overconfidence but is also outcome-informed.",
      "why_not_identified": "There is no affirmative contemporaneous evidence that the confidence judgment itself was distorted; the later margin statement could reflect ordinary uncertainty or hindsight rather than a demonstrated overconfidence mechanism at the time."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied, so retrieved_corpus_support_used is false and all labels rely on general cognitive-science knowledge.",
    "The analysis relies on a single retrospective self-report; original decisions may be filtered by memory and outcome knowledge.",
    "Some after-the-fact judgments were directly solicited by the interviewer; they are used only where they evidence a separate hindsight-related reasoning distortion."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MO_Biased_4_Sonnet_off",
  "interview_id": "MO_Biased_4",
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
