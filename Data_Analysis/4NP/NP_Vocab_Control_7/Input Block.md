<RAW_INTERVIEW>
Interviewer: Thanks for sitting down with me. This is for our operations learning file, not a disciplinary review — nothing here goes in your personnel record. Can you tell me your role and background?

Participant: Sure. I'm a process control operator on the catalytic reforming unit, six years on this board, eleven at the refinery overall. I run the DCS console — feed rates, heater duty, reactor temps, that side of things.

Interviewer: Good. Let's start broad — walk me through the incident from the beginning.

Participant: It kicked off right at shift handover, early morning. I'd just settled in when the high-temperature alarm came up on the feed heater outlet. Annunciator lit up, tone sounded. That specific point has been noisy lately — I want to say it tripped something like eleven times over the past month, all logged as instrument drift. But before I acknowledged it, I pulled up the pressure-differential trend on the adjacent screen too, since that's a habit of mine with recurring alarms — you want to see if anything else is moving with it. That trend had been creeping upward for a couple hours, slower and less obvious than the alarm itself, but it was there. Seeing both together made me less comfortable calling it a pure nuisance trip like the others had been, so I got the field operator moving to verify the thermocouple directly rather than just silencing it and continuing on.

Interviewer: What did the field check turn up?

Participant: Confirmed the outlet reading was accurate — not an instrument fault. So now I've got a real alarm and a real trend, and I flagged both for closer attention going into handover.

Interviewer: Walk me through the handover conversation.

Participant: Night operator said things had been "stable, unremarkable" for his last four hours, which matched what I was seeing on the immediate trend. But there was an older note in the board log, a few days back, about a slow upward drift in heater duty that had been flagged and never formally closed out. Rather than just assume it had resolved itself because the recent hours looked clean, I asked him directly whether that drift had actually been corrected or just stopped showing up in the short-term data. He wasn't sure — said it hadn't come up again, but nobody had gone back and verified the root cause.

Interviewer: How did that affect what you did next?

Participant: Production wanted the feed rate bumped to bank throughput before our regeneration window, about six hours out at that point. Given the alarm, the trend, and the unresolved drift note, I didn't just run the standard increase sequence the way I normally would. I ramped it more conservatively than usual and kept a closer eye on outlet temperature through the whole move, rather than treating it as routine.

Interviewer: What happened after that?

Participant: Temperature climbed some, as expected with any increase, but then the field operator called in from a walkdown and mentioned heat shimmer near the firebox — visually distinct, not something he'd normally flag. That raised the stakes.

Interviewer: Let's go back and unpack the first decision — cross-checking the pressure trend before acknowledging. What information did you actually have at that point?

Participant: The alarm, the recent trip history, and that pressure trend, which I made a point of looking at before doing anything else.

Interviewer: What alternatives did you weigh?

Participant: I could've just silenced it like the last eleven times — would've been the fast option. Or dispatched the field guy without checking the trend first. I did a version of both, but in a specific order: checked the trend, saw it didn't look like the earlier isolated trips, then sent the field operator to verify independently rather than assuming it was drift again.

Interviewer: How confident were you in that read at the time?

Participant: Moderately. I wasn't certain something was wrong, but the combination was enough that I didn't want to treat it as routine.

Interviewer: Moving to the feed increase decision — what alternatives were on the table?

Participant: Full delay and a deep dive into the multi-day trend log, looping in the engineer before touching setpoints, or proceeding as planned. I landed somewhere in the middle — proceeded, but modified, with tighter monitoring, specifically because the drift note hadn't been confirmed resolved.

Interviewer: Was that a deliberate call, or did you default to the usual procedure?

Participant: Deliberate. I actually thought about skipping the modification since the last four hours looked fine, but the unresolved log entry bothered me enough that I didn't want to run it exactly like every other routine bump.

Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind?

Participant: The pattern — alarm, temperature climb, shimmer — had some resemblance to a compressor surge event I'd handled about a year and a half ago on a similar unit. There's also a tube-rupture incident from a couple years back that people still bring up in briefings, more dramatic, shut the unit down for weeks. Both crossed my mind. But instead of just running with either, I checked specifically for the vibration signature that had shown up in the surge event — wasn't present here at all. And I asked the engineer whether the current data showed any of the specific markers tied to the tube-rupture failure mode. It didn't match either one cleanly.

Interviewer: What did you do given that neither precedent matched?

Participant: Treated it as its own case. Pulled fresh heater-specific diagnostic data and requested an independent instrument check rather than forcing it into either historical bucket.

Interviewer: Final decision — regeneration window closing in.

Participant: Under ninety minutes left. Temps and pressure still climbing, not at trip setpoints yet. I had a short checklist of standard corrective actions. Full engineer consultation would've eaten twenty to thirty minutes I didn't have to spare, but I also didn't want to just grab the first option on the list.

Interviewer: How did you choose?

Participant: I compared the top two or three checklist options against what the diagnostic data was actually showing, picked the one that matched the pattern best, not just the first one listed, and briefed the engineer by radio while I implemented it so he could flag anything I'd missed in real time.

Interviewer: What was the outcome?

Participant: Stabilized the trend. Later review said the comparison held up reasonably well given the time we had, though the full underlying cause took longer to pin down completely.

Interviewer: If the alarm's history had been clean instead of noisy, would you have handled that first moment differently?

Participant: Probably would've moved even faster to dispatch the field operator — less hesitation about whether it was worth the disruption. The noisy history didn't stop me from checking, but it's fair to say it added a beat of consideration before I did.

Interviewer: What single piece of information, if you'd had it sooner, would have changed the most?

Participant: Confirmation on whether that multi-day drift had genuinely resolved. I was operating on an unanswered question there, and if I'd known definitively either way, the feed-increase decision would've been more clear-cut.

Interviewer: And with more time before the regeneration window?

Participant: I'd have gotten the full engineer consultation rather than the quick radio brief. The comparison I did was reasonable, but a full conversation would've added confidence.

Interviewer: Anything else stand out looking back?

Participant: Just that none of these calls were obvious in the moment. Each one had a real alternative I seriously considered, and I don't think the outcome tells you definitively whether any single step was the right one — it worked out, but there was real uncertainty the whole way through.

Interviewer: That's a good place to stop. Thanks for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "NP_Vocab_Control_7",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Process Control Operator (Chemical/Petrochemical Refinery)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "Reactor Feed Heater Temperature Excursion During Night-to-Day Shift Handover (Vocabulary-Matched Control)",
    "scenario_summary_internal": "A control-room operator at a petrochemical refinery's catalytic reforming unit encounters a developing high-temperature/high-pressure excursion on the reactor feed heater train during a shift handover under production-throughput pressure. The operator methodically cross-checks the alarm against corroborating trend data, weighs both recent and older log evidence, adapts the routine feed-increase procedure to the abnormal conditions, tests candidate diagnostic hypotheses against available discriminating signals, and selects a corrective action after comparing the available checklist options against the closing regeneration window. The scenario mirrors the paired biased scenario's setting, actors, constraints, and decision structure, but every decision is supported by balanced consideration of available evidence and alternatives.",
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
          "Field operator confirms outlet thermocouple reading is accurate, not drifting",
          "Pressure-differential trend is already noted as a corroborating factor when the alarm is addressed"
        ],
        "alternatives": [
          "Acknowledge and silence alarm as likely nuisance based on history, continue monitoring",
          "Dispatch field operator immediately to verify heater outlet temperature independently",
          "Cross-check the pressure-differential trend alongside the alarm before deciding"
        ],
        "intended_action": "Operator pulls up the pressure-differential trend alongside the alarm before acknowledging, notes that the two together are less consistent with a pure nuisance trip than prior isolated occurrences, and dispatches the field operator to verify the thermocouple independently while continuing to monitor both trends."
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
          "Feed rate increase proceeds at a reduced initial ramp with closer monitoring of outlet temperature",
          "Field operator reports unusual heat shimmer near the heater firebox during walkdown"
        ],
        "alternatives": [
          "Proceed with the standard feed-rate increase sequence used for routine handovers",
          "Delay the increase and review the multi-day trend log before acting",
          "Consult the process engineer before adjusting feed rate"
        ],
        "intended_action": "Operator reviews the older drift note against the current handover report, confirms with the night operator whether the drift had actually been corrected or simply stopped appearing in recent readings, and proceeds with a modified, closer-monitored version of the feed-increase sequence rather than the unmodified routine steps."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Combined alarm and shimmer observations could resemble a compressor surge event handled 18 months ago on a similar unit",
          "A separate, more dramatic feed heater tube-rupture incident from about 2 years ago at this same refinery is well known and often discussed in shift briefings",
          "Current instrumentation shows temperature and pressure trending abnormally but does not show the vibration signature that accompanied the earlier compressor surge"
        ],
        "new_information_after_decision": [
          "Heater-specific diagnostic data is gathered and does not match either historical precedent closely",
          "Process engineer confirms that neither the surge vibration signature nor tube-rupture-specific markers are present"
        ],
        "alternatives": [
          "Apply the diagnostic and response template from the prior compressor surge event",
          "Treat the situation as a fresh case and gather heater-specific data before selecting a diagnostic path",
          "Request an independent instrument check to compare against both remembered precedents"
        ],
        "intended_action": "Operator treats the current symptom pattern as a fresh case, checks explicitly for the compressor's vibration signature and the tube-rupture-specific markers before drawing any parallel, and requests an independent instrument check when neither historical signature is confirmed."
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
          "The selected corrective action, chosen after a brief comparison of the checklist options, stabilizes the trend and addresses more of the underlying condition than a first-available choice would have",
          "Post-incident review confirms the comparison was reasonable given the time available"
        ],
        "alternatives": [
          "Select the first standard corrective action on the checklist that appears workable",
          "Pause production and conduct a full diagnostic review before acting",
          "Escalate immediately to the process engineer and wait for full guidance"
        ],
        "intended_action": "Operator quickly compares the two or three most relevant checklist options against the available diagnostic data, selects the option best matched to the observed pattern rather than simply the first one listed, and briefs the process engineer concurrently by radio while implementing the action."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what you were doing when the alarm first activated?",
        "What was your initial read on the situation?"
      ],
      "timeline_reconstruction": [
        "What happened right after you addressed the alarm?",
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
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "NP_Biased_7",
      "features_to_match": [
        "Domain vocabulary (reactor feed heater, catalytic reforming unit, DCS trend screen, annunciator panel, compressor surge, regeneration window, board operator log)",
        "Setting: central control room, day-to-night shift handover, same stakeholders",
        "Structure: exactly 4 decision points in the same chronological sequence and phase order",
        "Difficulty: same operational complexity and moderate ambiguity of underlying cause",
        "Actors: incoming operator, outgoing night operator, field operator, shift supervisor, process engineer",
        "Emotional tone: measured, procedural, mild time pressure escalating across the incident",
        "Same 6-hour regeneration-window constraint and same closing 90-minute final decision window",
        "Same surface incident facts: alarm history, pressure-differential trend, handover report, older drift note, heat shimmer, compressor-surge and tube-rupture precedents, closing checklist decision"
      ],
      "features_to_remove_or_change": [
        "Remove reliance on recalled alarm frequency alone as sufficient grounds for judgment; replace with active cross-checking of the pressure trend before acknowledging",
        "Remove automatic, unmodified execution of the routine feed-increase sequence; replace with a deliberate, adapted response given the abnormal precursor conditions",
        "Remove attention capture by the alarm's prominence alone; replace with explicit joint review of both the alarm and the quieter trend",
        "Remove unweighted discounting of the older drift note due to its age; replace with an explicit check of whether the drift had actually resolved",
        "Remove uncritical template transfer from the prior surge event; replace with an explicit check for the differentiating vibration signature before acting",
        "Remove overweighting of the vivid tube-rupture precedent; replace with an evidence-based comparison against current diagnostic markers",
        "Remove selection of the first workable checklist option without comparison; replace with a brief but real comparison of the top candidate options before choosing"
      ],
      "ambiguity_boundary": "The underlying cause of the excursion remains genuinely uncertain throughout the interview, and the final corrective action's completeness is not fully confirmed until after the interview period, but every decision shown is supported by an active, reasonably thorough evidence-weighing process rather than by a shortcut in reasoning."
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
      "Confirm exactly 4 decision points are present in the timeline, matching the paired scenario's phase structure",
      "Confirm zero intended instances of Availability Bias, Recency Bias, Habit Intrusion, Salience Bias, Similarity Bias, and Bounded Rationality appear anywhere in the interview",
      "Confirm domain vocabulary, setting, stakeholders, constraints, and emotional tone match the paired biased scenario",
      "Confirm each decision point offers at least two plausible alternatives and shows evidence of balanced consideration",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm final interview length falls within 1,215-1,485 words",
      "Confirm consequences described do not mechanically prove decisions were unbiased, preserving genuine uncertainty about root cause",
      "Confirm no bias label, definition, or psychological terminology appears in the public interview text",
      "Confirm the operator's reasoning at each decision point reflects active cross-checking, adaptation, or comparison rather than shortcut-driven judgment"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      { "bias": "Availability Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Recency Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Habit Intrusion", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Salience Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Similarity Bias", "occurrences": 0, "mechanism_constraint": null },
      { "bias": "Bounded Rationality", "occurrences": 0, "mechanism_constraint": null }
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
      { "bias": "Availability Bias", "requested_occurrences": 0 },
      { "bias": "Recency Bias", "requested_occurrences": 0 },
      { "bias": "Habit Intrusion", "requested_occurrences": 0 },
      { "bias": "Salience Bias", "requested_occurrences": 0 },
      { "bias": "Similarity Bias", "requested_occurrences": 0 },
      { "bias": "Bounded Rationality", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "NP_Biased_7",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "NP_Vocab_Control_7",
    "domain_id": "NP",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "No bias occurrences are planned or allocated; this is a vocabulary-matched zero-bias control paired to NP_Biased_7. All four decision points are constructed to mirror the paired scenario's structure, phase order, actors, constraints, and vocabulary, with each decision resolved through active, evidence-weighing reasoning rather than any shortcut mechanism associated with the six target biases.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Occupational setting (catalytic reforming unit control room)",
      "Participant role and seniority",
      "Four-decision-point chronological structure",
      "Stakeholders (night operator, field operator, shift supervisor, process engineer)",
      "Core constraints (6-hour regeneration window, alarm nuisance history, limited field-verification availability, proxy-sensor limitation)",
      "Surface incident facts (alarm, pressure-differential trend, handover report, older drift note, heat shimmer, surge and tube-rupture precedents, closing checklist decision)",
      "Emotional tone and escalating time pressure",
      "Interview format, probe categories, and approximate word count"
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
          "segment_type": "decision_reasoning",
          "raw_interview_anchor": "The recurring alarm history prompts a pressure-trend cross-check and independent field verification before acknowledgment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "evidence_weighting",
          "raw_interview_anchor": "Accurate thermocouple confirmation leads the operator to flag both signals for closer attention.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "evidence_integration",
          "raw_interview_anchor": "The stable handover report is weighed against an older unresolved heater-duty drift, prompting direct clarification.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "choice_rationale",
          "raw_interview_anchor": "Production pressure and unresolved evidence lead to a conservative feed-rate ramp with closer monitoring.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "diagnostic_hypothesis",
          "raw_interview_anchor": "Heat shimmer and the resemblance to memorable surge and tube-rupture events are considered as possible analogies.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "diagnostic_testing",
          "raw_interview_anchor": "The operator checks discriminating markers, finds neither precedent matches, and gathers fresh heater-specific data with an independent check.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "time_constrained_choice",
          "raw_interview_anchor": "Closing time, rising trends, trip margin, and checklist options frame the final corrective-action choice.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "option_comparison",
          "raw_interview_anchor": "Checklist options are compared against diagnostic data; the best match is selected and the engineer is briefed concurrently.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "outcome_assessment",
          "raw_interview_anchor": "Trend stabilization is reported and later review is described as reasonably supportive but incomplete.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "counterfactual_reasoning",
          "raw_interview_anchor": "A clean alarm history would have reduced hesitation, while the noisy history did not prevent checking.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_011",
          "speaker": "Participant",
          "segment_type": "information_value",
          "raw_interview_anchor": "Earlier confirmation of the multi-day drift’s resolution would have clarified the feed-increase decision.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        },
        {
          "segment_id": "seg_012",
          "speaker": "Participant",
          "segment_type": "uncertainty_reflection",
          "raw_interview_anchor": "More time would have enabled full consultation; the operator emphasizes real alternatives and uncertainty.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Zero-bias control: no hidden bias instance is planned."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
