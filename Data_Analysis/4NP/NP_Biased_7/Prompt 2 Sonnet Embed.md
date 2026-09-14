You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations learning file, not a disciplinary review — anything you share is for process improvement. Can you state your role and how long you've been on this unit?

Participant: Sure. I'm a process control operator on the catalytic reforming unit, been on this board for about six years, refinery for eleven. I run the DCS console during my shift — feed rates, heater duty, reactor temps, that kind of thing.

Interviewer: Good. Let's start broad — walk me through the incident from the beginning.

Participant: It started right at shift handover, early morning. I'd just sat down at the console when the high-temperature alarm came up on the feed heater outlet. Annunciator panel lit up red, audible tone too. Honestly, my first thought was "here we go again" — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast. I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own. So I acknowledged it, silenced the tone, and kept going with handover.

Interviewer: Did you check anything else at that point?

Participant: Not right away, no. I was focused on the panel itself — it's the loudest thing in the room when it goes off. There was actually a pressure-differential trend creeping up on one of the other screens, but it's a quieter kind of alarm, just a slow line drifting upward, no flashing, nothing urgent-looking. I didn't pull that screen up until later in the shift.

Interviewer: Okay, let's keep going chronologically. What happened during the handover conversation itself?

Participant: Night operator gave me the rundown — said the unit had been "stable, unremarkable" for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value. There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours. It felt like old news at that point since the recent hours looked clean.

Interviewer: And then?

Participant: Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run.

Interviewer: What happened after the increase?

Participant: Outlet temperature climbed further than I expected. Then the field operator called in from a walkdown and mentioned some heat shimmer near the firebox — visually noticeable, he said, not normal. That's when it started feeling like more than a nuisance alarm.

Interviewer: Let's go back and unpack that first decision — acknowledging the alarm as nuisance. What information did you actually have in front of you at that moment?

Participant: The alarm itself, my memory of that alarm going off a lot recently, and that pressure trend I mentioned, which I hadn't really looked at yet.

Interviewer: What alternatives did you consider?

Participant: I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality.

Interviewer: How confident were you in that read?

Participant: Pretty confident, honestly. Maybe overconfident looking back. Eleven-for-eleven is a strong pattern in your head, even if I hadn't actually gone back through the log to confirm it.

Interviewer: Moving to the feed increase decision — what alternatives were on the table?

Participant: I could've delayed the increase and gone back through the multi-day trend log, or looped in the process engineer before touching setpoints. Neither felt necessary given how clean the last few hours looked.

Interviewer: When you ran the sequence, were you consciously deciding it was the right call, or was it more automatic?

Participant: If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump.

Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind?

Participant: The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template. At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing.

Interviewer: Did the current data support either of those comparisons specifically?

Participant: Looking back, not entirely. The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach. And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.

Interviewer: What alternatives existed at that point?

Participant: I could've treated it as a new case entirely and pulled fresh heater-specific data before picking a diagnostic path, or requested an independent instrument check to compare against both remembered precedents.

Interviewer: Let's talk about the final decision, with the regeneration window closing in.

Participant: Under ninety minutes left. Temps and pressure still climbing but not at trip setpoints yet. I had the standard checklist for heater excursions, and I could've paused everything to escalate fully to the process engineer, but that's a twenty-to-thirty-minute conversation minimum, and the clock was working against us.

Interviewer: How did you decide?

Participant: I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast.

Interviewer: What was the outcome?

Participant: It did stabilize the immediate trend, which was the priority. Root cause wasn't fully addressed though — a later review flagged another corrective step on that same checklist that probably would've hit the underlying issue better. Wasn't wrong exactly, just not the most complete answer.

Interviewer: If the alarm's history had been different — say, no prior nuisance trips at all — would you have handled that first moment the same way?

Participant: No, honestly no. If that alarm had been clean before, I'd have jumped on the pressure trend immediately instead of treating it as background noise.

Interviewer: What single piece of information, if you'd had it earlier, would have changed the most for you?

Participant: Probably the pressure-differential trend, pulled up right alongside the alarm at the very start. That would've reframed the whole thing much sooner instead of it building quietly in the background.

Interviewer: And if you'd had more time before the regeneration window closed?

Participant: I'd have gone through more of the checklist options side by side, maybe gotten the engineer on the line even for ten minutes. It wasn't that I thought the first option was definitely best — it was available and it worked well enough given the clock.

Interviewer: Anything else stand out looking back?

Participant: Just that a lot of small, reasonable-feeling calls stacked up into something bigger than any one of them looked like at the time. Nothing felt like a wrong decision in the moment.

Interviewer: That's a good place to close. Thanks for walking through this in detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Biased_7",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Process Control Operator (Chemical/Petrochemical Refinery)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Reactor Feed Heater Temperature Excursion During Night-to-Day Shift Handover",
    "scenario_summary_internal": "A control-room operator at a petrochemical refinery's catalytic reforming unit must interpret a developing high-temperature/high-pressure excursion on the reactor feed heater train during a shift handover under production-throughput pressure. The operator must decide how to weigh a persistently noisy alarm history, a recent stable-trend handover report, a habitual startup sequence, a superficially similar past incident, and a vivid past major event, ultimately making a time-constrained corrective decision before a scheduled catalyst regeneration window closes.",
    "occupational_realism": {
      "objective": "Diagnose and correct an abnormal thermal/pressure trend on the reforming unit's feed heater and lead reactor before it threatens catalyst integrity or triggers an automatic unit trip, while minimizing unplanned production loss ahead of a scheduled regeneration outage.",
      "setting": "Central control room of a catalytic reforming unit at a mid-size petrochemical refinery, day-to-night shift transition, DCS (distributed control system) console with trend screens, alarm annunciator panel, radio contact with outside field operators.",
      "constraints": [
        "Production target tied to a narrow regeneration outage window in 6 hours",
        "Limited outside operator availability for field verification during shift change",
        "Alarm system has a known history of nuisance/false alarms on this specific sensor loop",
        "Time pressure to resolve the trend before board handover documentation is due",
        "No direct real-time catalyst bed temperature profile, only proxy sensors"
      ],
      "stakeholders": [
        "Incoming day-shift Process Control Operator (interviewee)",
        "Outgoing night-shift operator",
        "Field operator",
        "Unit shift supervisor",
        "Process engineer on call"
      ],
      "technical_terms_to_use": [
        "reactor feed heater",
        "catalytic reforming unit",
        "DCS trend screen",
        "high-temperature alarm setpoint",
        "catalyst bed",
        "compressor surge",
        "regeneration window",
        "annunciator panel",
        "board operator log"
      ],
      "technical_terms_to_avail": [],
      "technical_terms_to_avoid": [
        "nuclear reactor",
        "radiation",
        "containment breach",
        "core meltdown"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "High-temperature alarm activates on reactor feed heater outlet",
          "Operator log shows this same alarm has triggered 11 times in the past month, all resolved as instrument drift",
          "A slower, less visually prominent pressure-differential trend on an adjacent screen has begun a gradual rise over the last 2 hours"
        ],
        "new_information_after_decision": [
          "Field operator later confirms outlet thermocouple reading is accurate, not drifting",
          "Pressure-differential trend continues climbing after the alarm is acknowledged and silenced"
        ],
        "alternatives": [
          "Acknowledge and silence alarm as likely nuisance based on history, continue monitoring",
          "Dispatch field operator immediately to verify heater outlet temperature independently",
          "Cross-check the pressure-differential trend alongside the alarm before deciding"
        ],
        "intended_action": "Operator acknowledges the alarm as probable nuisance, citing frequent past occurrences, and does not immediately cross-reference the pressure trend."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Night-shift handover report describes 'stable, unremarkable' readings for the last 4 hours",
          "Board operator log (older entries, several days back) shows a slow upward drift in feed heater duty that was flagged but not resolved",
          "Production schedule calls for a feed rate increase to meet output target before the regeneration window"
        ],
        "new_information_after_decision": [
          "Feed rate increase raises heater outlet temperature further",
          "Field operator reports unusual heat shimmer near the heater firebox during walkdown"
        ],
        "alternatives": [
          "Proceed with the standard feed-rate increase sequence used for routine handovers",
          "Delay the increase and review the multi-day trend log before acting",
          "Consult the process engineer before adjusting feed rate"
        ],
        "intended_action": "Operator executes the familiar step-by-step valve and setpoint sequence normally used for routine feed increases, weighting the recent stable handover report over the older drift trend, without pausing to reassess given the abnormal precursor."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Combined alarm and shimmer observations now resemble the operator's memory of a compressor surge event handled successfully 18 months ago on a similar unit",
          "A separate, more dramatic feed heater tube-rupture incident from about 2 years ago at this same refinery is well known and often discussed in shift briefings",
          "Current instrumentation shows temperature and pressure trending abnormally but does not show the vibration signature that accompanied the earlier compressor surge"
        ],
        "new_information_after_decision": [
          "Applying the surge-event checklist does not address the temperature excursion",
          "Process engineer later notes the vibration signature characteristic of a true surge event was absent from current data"
        ],
        "alternatives": [
          "Apply the diagnostic and response template from the prior compressor surge event",
          "Treat the situation as a fresh case and gather heater-specific data before selecting a diagnostic path",
          "Request an independent instrument check to compare against both remembered precedents"
        ],
        "intended_action": "Operator maps the response template from the previously experienced surge event onto the current case based on surface resemblance, and separately treats the vivid tube-rupture incident from two years ago as the more likely explanation because it comes readily to mind, without weighing how infrequent that scenario actually is relative to more mundane causes."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Regeneration window closes in under 90 minutes",
          "Temperature and pressure trends continue to climb but have not yet reached automatic trip setpoints",
          "Process engineer is reachable but a full consultation would take 20-30 minutes",
          "Board checklist offers a short list of standard corrective actions for heater excursions"
        ],
        "new_information_after_decision": [
          "The selected corrective action stabilizes the immediate trend but does not fully resolve the underlying cause",
          "A post-incident review later identifies an alternative corrective option that would have addressed the root cause more directly"
        ],
        "alternatives": [
          "Select the first standard corrective action on the checklist that appears workable",
          "Pause production and conduct a full diagnostic review before acting",
          "Escalate immediately to the process engineer and wait for full guidance"
        ],
        "intended_action": "Operator, under time and cognitive load constraints, selects the first checklist action that appears sufficient to stabilize the trend rather than exhaustively evaluating all corrective alternatives."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you were doing when the alarm first activated?",
        "What was your initial read on the situation?"
      ],
      "timeline_reconstruction": [
        "What happened right after you acknowledged the alarm?",
        "Walk me through the shift handover conversation and what stood out to you.",
        "What did you notice during the field walkdown report?",
        "What happened as the regeneration window approached?"
      ],
      "decision_point_probes": [
        "What information did you have available at that moment?",
        "What alternatives did you consider, and why did you rule them out?",
        "What made you settle on that particular course of action?",
        "How did your past experience with similar situations factor into this decision?",
        "How much time pressure did you feel, and how did that affect your choice?",
        "How confident were you in your read of the situation at the time?"
      ],
      "closing_hypotheticals": [
        "If the alarm history had been different, would you have responded the same way?",
        "If you had had more time before the regeneration window, what would you have done differently?",
        "Looking back, is there a moment where a different piece of information would have changed your decision?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 1,
        "mechanism": "Operator estimates the probability that the alarm is a false positive based on how easily instances of past nuisance alarms come to mind, rather than on current corroborating or contradicting evidence.",
        "affected_reasoning_operation": "Probability estimation from recalled frequency",
        "evidence_available_at_time": [
          "Log showing 11 recent nuisance alarms from the same sensor",
          "An unexamined adjacent pressure-differential trend"
        ],
        "required_textual_manifestation": "Operator explicitly cites the frequent recent alarm history as the primary reason for judging this alarm minor, without mentioning having checked the pressure trend at that moment.",
        "plausible_nonbias_interpretation": "A reasonable operator might legitimately deprioritize a historically noisy alarm as an efficient use of limited attention.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "base rate", "cognitive bias"]
      },
      {
        "instance_id": "sal_01",
        "bias": "Salience Bias",
        "decision_point": 1,
        "mechanism": "The visually and audibly prominent flashing/blaring alarm captures disproportionate attention, causing the operator to overlook the less visually striking but diagnostically relevant pressure-differential trend on an adjacent screen.",
        "affected_reasoning_operation": "Attention allocation across simultaneous evidence sources",
        "evidence_available_at_time": [
          "Flashing high-temperature alarm on annunciator panel",
          "Quietly rising pressure-differential trend on a separate trend screen"
        ],
        "required_textual_manifestation": "Operator describes focusing on the alarm panel and admits, when asked, not having looked at the pressure trend screen until later.",
        "plausible_nonbias_interpretation": "Alarm panels are designed to draw attention first as part of standard operating procedure.",
        "strength": "subtle",
        "do_not_make_explicit": ["salience", "attention bias"]
      },
      {
        "instance_id": "rec_01",
        "bias": "Recency Bias",
        "decision_point": 2,
        "mechanism": "Operator gives disproportionate weight to the most recent handover report describing stable conditions over the last 4 hours, discounting the older multi-day drift trend documented earlier in the log.",
        "affected_reasoning_operation": "Weighting of sequential evidence when forming a current-state judgment",
        "evidence_available_at_time": [
          "Night-shift handover report describing 4 hours of stable readings",
          "Older log entries showing a multi-day upward drift in heater duty"
        ],
        "required_textual_manifestation": "Operator states that because the last few hours looked stable, they felt comfortable proceeding, without referencing the older drift entries as a counterweight.",
        "plausible_nonbias_interpretation": "Recent data is often the most operationally relevant for immediate decisions.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "cognitive bias"]
      },
      {
        "instance_id": "hab_01",
        "bias": "Habit Intrusion",
        "decision_point": 2,
        "mechanism": "Operator performs the familiar, highly practiced valve/setpoint sequence used routinely for feed-rate increases as an automatic behavioral pattern, without consciously adapting the steps to account for the abnormal precursor conditions present this time.",
        "affected_reasoning_operation": "Execution of a well-rehearsed action sequence under conditions requiring deviation from the routine",
        "evidence_available_at_time": [
          "Standard feed-increase procedure performed dozens of times before",
          "Abnormal precursor conditions (alarm history, drift trend) present but not integrated into the action plan"
        ],
        "required_textual_manifestation": "Operator describes going through the 'usual steps' for a feed increase and, when probed, acknowledges not consciously pausing to modify the sequence despite the unusual circumstances.",
        "plausible_nonbias_interpretation": "Standardized procedures exist precisely to be followed consistently for efficiency and safety.",
        "strength": "moderate",
        "do_not_make_explicit": ["habit intrusion", "automaticity", "slip"]
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "decision_point": 3,
        "mechanism": "Operator matches the current symptom pattern to a superficially similar prior compressor surge event and applies that event's diagnostic/response template, despite the absence of a key differentiating signal (vibration signature) that was present in the original case.",
        "affected_reasoning_operation": "Pattern-matching for diagnostic categorization",
        "evidence_available_at_time": [
          "Memory of a prior compressor surge event with generally similar temperature/pressure behavior",
          "Absence of the vibration signature that characterized that prior event"
        ],
        "required_textual_manifestation": "Operator explains choosing the surge-response approach because 'it looked like' the earlier event, without addressing the missing vibration signal as a distinguishing factor.",
        "plausible_nonbias_interpretation": "Drawing on a structurally similar past case is a normal and often effective diagnostic heuristic.",
        "strength": "subtle",
        "do_not_make_explicit": ["similarity heuristic", "representativeness"]
      },
      {
        "instance_id": "av_02",
        "bias": "Availability Bias",
        "decision_point": 3,
        "mechanism": "Operator judges a rare, dramatic tube-rupture incident from about two years ago as the more likely explanation for the current excursion because it is vivid and frequently discussed, rather than because current evidence supports it over more mundane causes.",
        "affected_reasoning_operation": "Likelihood judgment driven by vividness/memorability of a distinct recalled event, separate from the frequency-based recall in av_01",
        "evidence_available_at_time": [
          "Widely discussed, memorable tube-rupture incident from about two years prior",
          "Current data lacking specific markers that would confirm that rare failure mode"
        ],
        "required_textual_manifestation": "Operator mentions the two-year-old incident unprompted as feeling like the likely cause 'because everyone still talks about it,' distinct from the earlier nuisance-alarm frequency reasoning in decision point 1.",
        "plausible_nonbias_interpretation": "Considering a known catastrophic failure mode as a precaution is prudent risk awareness.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "vividness effect"]
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 4,
        "mechanism": "Facing time pressure and cognitive load from the closing regeneration window, the operator satisfices by selecting the first checklist action that appears adequate rather than exhaustively evaluating all available corrective alternatives.",
        "affected_reasoning_operation": "Option generation and selection under constrained time and cognitive resources",
        "evidence_available_at_time": [
          "Closing regeneration window (under 90 minutes)",
          "A short standard checklist of corrective actions",
          "Availability of the process engineer for fuller consultation, at a time cost"
        ],
        "required_textual_manifestation": "Operator states choosing the first workable checklist option to save time, and acknowledges not comparing it against other listed alternatives before acting.",
        "plausible_nonbias_interpretation": "Selecting a known, pre-approved corrective action quickly is a defensible response to genuine time constraints.",
        "strength": "moderate",
        "do_not_make_explicit": ["bounded rationality", "satisficing"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control specified in this generation cycle."
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
      "Confirm exactly 7 total bias instances are embedded: 2 Availability, 1 Recency, 1 Habit Intrusion, 1 Salience, 1 Similarity, 1 Bounded Rationality",
      "Confirm av_01 and av_02 use distinct evidence sources (frequency-based nuisance-alarm recall vs. vividness-based recall of a distinct rare incident) and occur at different decision points",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text",
      "Confirm each decision point offers at least two plausible alternatives",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm final interview length falls within 1,215-1,485 words",
      "Confirm consequences described do not mechanically confirm or refute bias presence",
      "Confirm Habit Intrusion instance reflects an automatic, frequently-practiced behavioral pattern rather than a deliberate reasoning error, per mechanism_constraint"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 2, "mechanism_constraint": null },
      { "bias": "Recency Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Habit Intrusion", "occurrences": 1, "mechanism_constraint": "human performance often can be captured by familiar behavioral patterns that occur so frequently in their experiences." },
      { "bias": "Salience Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Similarity Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Bounded Rationality", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Availability Bias",
      "Recency Bias",
      "Habit Intrusion",
      "Salience Bias",
      "Similarity Bias",
      "Bounded Rationality"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Availability Bias", "requested_occurrences": 2 },
      { "bias": "Recency Bias", "requested_occurrences": 1 },
      { "bias": "Habit Intrusion", "requested_occurrences": 1 },
      { "bias": "Salience Bias", "requested_occurrences": 1 },
      { "bias": "Similarity Bias", "requested_occurrences": 1 },
      { "bias": "Bounded Rationality", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "av_01", "bias": "Availability Bias" },
      { "instance_id": "av_02", "bias": "Availability Bias" },
      { "instance_id": "rec_01", "bias": "Recency Bias" },
      { "instance_id": "hab_01", "bias": "Habit Intrusion" },
      { "instance_id": "sal_01", "bias": "Salience Bias" },
      { "instance_id": "sim_01", "bias": "Similarity Bias" },
      { "instance_id": "br_01", "bias": "Bounded Rationality" }
    ],
    "intended_decision_points": [
      { "instance_id": "av_01", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "sal_01", "bias": "Salience Bias", "decision_point": 1 },
      { "instance_id": "rec_01", "bias": "Recency Bias", "decision_point": 2 },
      { "instance_id": "hab_01", "bias": "Habit Intrusion", "decision_point": 2 },
      { "instance_id": "sim_01", "bias": "Similarity Bias", "decision_point": 3 },
      { "instance_id": "av_02", "bias": "Availability Bias", "decision_point": 3 },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "mechanism": "Probability of alarm being false judged via ease of recalling frequent past nuisance-alarm occurrences",
        "affected_reasoning_operation": "Probability estimation from recalled frequency",
        "evidence_source": "Alarm log showing 11 recent nuisance alarms",
        "distinctiveness_requirement": "Must be based on frequency-of-recall reasoning, distinct from av_02's vividness-of-recall reasoning"
      },
      {
        "instance_id": "sal_01",
        "bias": "Salience Bias",
        "mechanism": "Visually/audibly prominent alarm draws attention away from a less prominent but relevant pressure-differential trend",
        "affected_reasoning_operation": "Attention allocation across simultaneous evidence sources",
        "evidence_source": "Annunciator panel alarm vs. adjacent trend screen",
        "distinctiveness_requirement": "Must involve competing simultaneous evidence sources at the same decision point as av_01 but a different reasoning operation (attention allocation, not frequency-based probability judgment)"
      },
      {
        "instance_id": "rec_01",
        "bias": "Recency Bias",
        "mechanism": "Overweighting the most recent handover report of stability over older documented drift trend",
        "affected_reasoning_operation": "Weighting of sequential evidence in current-state judgment",
        "evidence_source": "Night-shift handover report vs. multi-day log drift entries",
        "distinctiveness_requirement": "Must center on temporal recency of information, not frequency or vividness"
      },
      {
        "instance_id": "hab_01",
        "bias": "Habit Intrusion",
        "mechanism": "Automatic execution of a frequently-practiced feed-increase sequence without adapting to abnormal precursor conditions",
        "affected_reasoning_operation": "Execution of a well-rehearsed action sequence under conditions requiring deviation",
        "evidence_source": "Standard operating sequence performed routinely",
        "distinctiveness_requirement": "Must manifest as an automatic behavioral pattern/slip, not a deliberate judgment error, per mechanism_constraint"
      },
      {
        "instance_id": "sim_01",
        "bias": "Similarity Bias",
        "mechanism": "Diagnostic template from a superficially similar past compressor surge event applied despite a missing distinguishing signal",
        "affected_reasoning_operation": "Pattern-matching for diagnostic categorization",
        "evidence_source": "Memory of prior surge event vs. absence of vibration signature",
        "distinctiveness_requirement": "Must involve template transfer based on surface resemblance, distinct from av_02's likelihood judgment based on memorability"
      },
      {
        "instance_id": "av_02",
        "bias": "Availability Bias",
        "mechanism": "Likelihood of rare tube-rupture cause overestimated due to vividness/memorability of a widely discussed past incident",
        "affected_reasoning_operation": "Likelihood judgment driven by vividness of recall",
        "evidence_source": "Recollection of a two-year-old widely discussed incident",
        "distinctiveness_requirement": "Must be based on vividness-of-recall reasoning, distinct from av_01's frequency-of-recall reasoning, and occur at a different decision point"
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "mechanism": "Satisficing selection of the first workable checklist action under time and cognitive load constraints rather than exhaustive alternative evaluation",
        "affected_reasoning_operation": "Option generation and selection under constrained resources",
        "evidence_source": "Standard corrective-action checklist under closing time window",
        "distinctiveness_requirement": "Must reflect resource-constrained satisficing, not mere haste or a justified quick decision without evidence of skipped alternatives"
      }
    ],
    "intended_strength": [
      { "instance_id": "av_01", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "sal_01", "bias": "Salience Bias", "strength": "subtle" },
      { "instance_id": "rec_01", "bias": "Recency Bias", "strength": "subtle" },
      { "instance_id": "hab_01", "bias": "Habit Intrusion", "strength": "moderate" },
      { "instance_id": "sim_01", "bias": "Similarity Bias", "strength": "subtle" },
      { "instance_id": "av_02", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "br_01", "bias": "Bounded Rationality", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Biased_7",
    "domain_id": "NP",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across the 4 decision points by mechanism fit and narrative realism: decision point 1 hosts av_01 and sal_01 (distinct evidence sources: alarm-frequency log vs. competing trend screen); decision point 2 hosts rec_01 and hab_01 (distinct reasoning operations: temporal weighting vs. automatic action execution); decision point 3 hosts sim_01 and av_02 (distinct reasoning operations: pattern-matching template transfer vs. vividness-driven likelihood judgment, satisfying the same-bias distinctiveness rule for av_01/av_02 by using different evidence sources and different decision points); decision point 4 hosts br_01 alone under peak time pressure. No decision point exceeds two occurrences of any single bias.",
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
          "segment_type": "initial_alarm_classification",
          "raw_interview_anchor": "The alarm had fired repeatedly and the pattern in my head felt strong enough on its own, so I treated it as a nuisance.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "av_01"
          ],
          "ground_truth_rationale": "The participant estimated the likelihood that the alarm was false from easily recalled prior nuisance alarms without checking current corroborating evidence."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "attention_allocation",
          "raw_interview_anchor": "I was focused on the panel itself because it was the loudest thing in the room and did not pull up the quieter pressure trend until later.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sal_01"
          ],
          "ground_truth_rationale": "The prominent audible and visual alarm captured attention while a less salient but relevant pressure trend was overlooked."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "handover_evidence_weighting",
          "raw_interview_anchor": "The recent four hours looked clean, so I took the stable handover at face value and wrote off the older unresolved drift note as old news.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "rec_01"
          ],
          "ground_truth_rationale": "The participant overweighted the most recent stable report relative to the older unresolved drift evidence."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "routine_action_execution",
          "raw_interview_anchor": "I ran the standard feed-increase sequence, the same steps I had done about a hundred times, without stopping to reconsider the abnormal precursor.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "hab_01"
          ],
          "ground_truth_rationale": "A highly practiced action sequence was executed automatically without adapting it to the abnormal conditions."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "diagnostic_pattern_matching",
          "raw_interview_anchor": "The alarm, temperature climb, and shimmer reminded me of a prior compressor surge, so my instinct was to pull that same response template despite the missing vibration signature.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "sim_01"
          ],
          "ground_truth_rationale": "A superficially similar prior event was used as the diagnostic template despite the absence of a defining feature."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "diagnostic_likelihood_judgment",
          "raw_interview_anchor": "The tube-rupture incident felt like the more likely explanation because it was dramatic and people brought it up in every shift briefing.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "av_02"
          ],
          "ground_truth_rationale": "The likelihood of a rare failure mode was increased because the memorable incident was socially and mentally available."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "time_constrained_option_selection",
          "raw_interview_anchor": "I went with the first checklist option that looked workable and did not compare it with the rest because I needed something fast.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "br_01"
          ],
          "ground_truth_rationale": "Under a closing time window, the participant selected the first adequate option rather than evaluating all alternatives."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "outcome_reflection",
          "raw_interview_anchor": "The selected action stabilized the immediate trend, but a later review found another checklist step that would have addressed the underlying issue better.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a substantive retrospective outcome assessment without an intentionally embedded hidden bias instance."
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
    "analysis_scope_note": "Conservative mechanism-first screening of a voluntary operations debrief transcript; only bias-specific reasoning with affirmative transcript evidence was classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 2
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
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the likelihood or significance of an event by the ease with which relevant instances come to mind rather than by systematically verifying the current evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial high-temperature alarm classification",
      "decision_point_description": "Whether to acknowledge the feed-heater outlet high-temperature alarm as a nuisance instrument-drift event or to investigate it immediately.",
      "affected_reasoning_operation": "Alarm interpretation and response prioritization",
      "bias_specific_mechanism": "Readily recalled recent nuisance alarm instances were used as the primary basis for classifying the current alarm; the remembered pattern felt sufficiently diagnostic, so the participant did not consult the actual alarm log or the co-located pressure-differential trend.",
      "manifestation_in_interview": "The participant reported that past alarm events came to mind quickly, estimated 'eleven' prior trips from memory, and acknowledged/silenced the alarm without checking the log or the visible pressure-differential trend.",
      "effect_on_reasoning_or_decision": "The initial alarm was treated as background nuisance, delaying investigation of a developing pressure/thermal issue until later field evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first thought was 'here we go again' — that specific alarm point has been a headache for a month, and those past calls came to mind pretty fast.",
          "evidence_explanation": "Shows that readily recalled past alarm instances immediately framed the current alarm."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I want to say it's fired eleven times in the past few weeks, and every one I could remember got chalked up to instrument drift on that thermocouple. I didn't pull the actual log to check the dates or whether those prior trips looked like this one — the pattern in my head felt strong enough on its own.",
          "evidence_explanation": "Demonstrates that the participant relied on remembered instances instead of available log and trend data to conclude the alarm was another nuisance trip."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If that alarm had been clean before, I'd have jumped on the pressure trend immediately instead of treating it as background noise.",
          "evidence_explanation": "Counterfactual statement directly links the prior recall-based alarm history to the reduced urgency at the initial alarm."
        }
      ],
      "correction_or_counterevidence": "Later field report of heat shimmer, continued temperature climb, and the participant's subsequent statement that it began to feel like more than a nuisance alarm served as a delayed correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not provide a specific availability-heuristic definition; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchoring"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which an initial value or impression serves as an anchor and subsequent adjustments away from that anchor are typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Handover assessment of unit stability",
      "decision_point_description": "Whether to accept the night operator's 'stable, unremarkable' handover as sufficient or to review the older unresolved heater-duty drift note.",
      "affected_reasoning_operation": "Situation assessment and integration of recent and historical trend information",
      "bias_specific_mechanism": "The immediate handover and recent four-hour trend served as an anchor; the older log note about unresolved upward heater-duty drift should have prompted adjustment, but the participant treated it as old news without checking whether it had actually resolved.",
      "manifestation_in_interview": "The participant accepted the night operator's stable report and current immediate trend at face value and dismissed an older unresolved drift note because of its age, rather than reconciling it with the recent clean hours.",
      "effect_on_reasoning_or_decision": "He formed an unduly stable picture of the unit, which contributed to proceeding with the feed increase without reviewing multi-day trends.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Night operator gave me the rundown — said the unit had been 'stable, unremarkable' for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value.",
          "evidence_explanation": "Shows acceptance of the handover and immediate-trend signal as the initial anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but I mostly wrote it off just because it was a few days old — didn't go back and check whether that drift had actually stopped or just wasn't showing up in the last four hours.",
          "evidence_explanation": "Demonstrates insufficient adjustment away from the initial stable anchor when encountering an older unresolved-drift note."
        }
      ],
      "correction_or_counterevidence": "No immediate correction; later review and engineer input led to fuller reevaluation of the heater-duty drift.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passage provided direct definitional support for the anchoring-and-adjustment mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": "Cognitive bias in the verification and validation of space flight systems",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was describe Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "Defines anchoring-and-adjustment and notes that adjustment from an initial anchor is typically insufficient.",
          "relevance_to_this_occurrence": "The participant anchored on the stable handover report and recent clean trend, then made an insufficient adjustment when exposed to the older unresolved heater-duty drift note."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "similarity heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the likelihood of a diagnosis or the appropriateness of a response by the similarity of the current situation to a past or prototypical case, often without sufficiently weighting diagnostic feature mismatches.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-shimmer diagnostic response selection",
      "decision_point_description": "Whether to adopt the prior compressor-surge response template or to evaluate the current heater symptoms independently.",
      "affected_reasoning_operation": "Causal diagnosis and response-template selection",
      "bias_specific_mechanism": "The combination of current cues was matched to a remembered compressor-surge event; this similarity triggered retrieval of a prior response template, and the participant did not check for a defining feature—compressor vibration—that was absent in the current situation.",
      "manifestation_in_interview": "The participant explicitly said the situation reminded him of a compressor surge event, pulled the same response template, and later acknowledged he did not check for the defining vibration signature.",
      "effect_on_reasoning_or_decision": "It pulled diagnostic and response planning toward a previous incident template rather than a fresh analysis of the current heater-specific data.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template.",
          "evidence_explanation": "Shows similarity-based retrieval and action selection from a past case."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach.",
          "evidence_explanation": "Demonstrates the representativeness failure to incorporate a diagnostic feature mismatch before adopting the prior template."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged the missing vibration signature and that the current data did not specifically support the surge template.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not provide a specific representativeness-heuristic definition; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "salience bias",
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging an event as more likely or present because it is easily recalled or especially vivid and memorable, rather than because current diagnostic evidence supports it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-shimmer causal-likelihood comparison",
      "decision_point_description": "Whether the tube-rupture failure mode was the likely explanation for the current heater symptoms.",
      "affected_reasoning_operation": "Diagnostic likelihood judgment",
      "bias_specific_mechanism": "The dramatic, frequently discussed tube-rupture incident was highly available in memory; its memorability and rehearsal in shift briefings were used as a cue to likelihood, while current diagnostic markers for that failure mode were not initially checked.",
      "manifestation_in_interview": "The participant judged the tube-rupture case as more likely because it is discussed often, and later acknowledged that none of the specific markers for that failure mode were actually present.",
      "effect_on_reasoning_or_decision": "The tube-rupture hypothesis felt more probable than current evidence warranted, influencing the diagnostic path.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing.",
          "evidence_explanation": "Shows the participant using ease of recall and social rehearsal of a salient event as a likelihood cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.",
          "evidence_explanation": "Explicitly states that memorability substituted for actual diagnostic evidence."
        }
      ],
      "correction_or_counterevidence": "An engineer later pointed out that specific tube-rupture markers were absent; the participant acknowledged this in retrospect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus passages did not provide a specific availability-heuristic definition; the label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Feed-rate increase execution",
      "supporting_interview_quote": "Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run.",
      "plausible_mechanism": "Continuing the original schedule-driven plan despite accumulating cues that a deeper review may be warranted.",
      "why_not_identified": "Strong competing non-bias explanation: execution of a well-trained standard procedure under a production and regeneration-window schedule, without clear evidence of an isolated plan-continuation reasoning mechanism."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "satisficing",
      "alternative_labels": [
        "need for closure"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final checklist selection under regeneration-window time pressure",
      "supporting_interview_quote": "I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast.",
      "plausible_mechanism": "Selecting the first acceptable option rather than comparing alternatives under time pressure.",
      "why_not_identified": "External time pressure and operational constraints provide a sufficient non-bias explanation; no distinct bias-specific cognitive mechanism was affirmatively isolated."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The transcript is a retrospective self-report, so cognitive mechanisms are inferred from the participant's explicit descriptions rather than direct observation.",
    "Retrieved corpus coverage was sparse and contained OCR noise; not all identified heuristics had direct corpus support, requiring disclosure of general-knowledge labels.",
    "Some closely related mechanisms, such as availability, recency, and alarm complacency, are difficult to fully separate within a single unfolding incident."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Biased_7_Sonnet_on",
  "interview_id": "NP_Biased_7",
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
