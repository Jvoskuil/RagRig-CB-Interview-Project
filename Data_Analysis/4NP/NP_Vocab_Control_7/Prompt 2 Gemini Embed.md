You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  null
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
    "analysis_scope_note": "Evaluated the participant's recounted process-control decisions and reasoning across alarm handling, handover information integration, feed-rate increase, post-shimmer diagnostic assessment, and time-pressured corrective action. No affirmative evidence of a distorting cognitive-bias mechanism was found; several bias patterns were considered by the participant and actively counteracted before influencing decisions."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "automation complacency",
      "alternative_labels": [
        "complacency effect",
        "automation bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial high-temperature alarm acknowledgment",
      "supporting_interview_quote": "That specific point has been noisy lately — I want to say it tripped something like eleven times over the past month, all logged as instrument drift.",
      "plausible_mechanism": "A repeated nuisance-alarm history could plausibly reduce alarm verification and monitoring, consistent with automation complacency or automation bias.",
      "why_not_identified": "The participant did not accept or silence the alarm based on its history; instead, he cross-checked the pressure-differential trend, treated the combination as potentially non-routine, and dispatched a field operator for independent thermocouple verification. No distorted monitoring or accepting response was demonstrated."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-shimmer diagnostic assessment of heater anomaly",
      "supporting_interview_quote": "The pattern — alarm, temperature climb, shimmer — had some resemblance to a compressor surge event I'd handled about a year and a half ago on a similar unit. There's also a tube-rupture incident from a couple years back that people still bring up in briefings, more dramatic, shut the unit down for weeks. Both crossed my mind.",
      "plausible_mechanism": "Salient, memorable past incidents could anchor the diagnosis or increase the subjective likelihood that the current event matched one of those patterns.",
      "why_not_identified": "The participant explicitly checked disconfirming diagnostic markers for each historical event, found that neither matched cleanly, and then treated the current case as independent by pulling fresh heater-specific diagnostic data and requesting an independent instrument check. No availability-driven distortion of judgment was affirmatively shown."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": [
        "get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Feed-rate increase before regeneration window",
      "supporting_interview_quote": "Production wanted the feed rate bumped to bank throughput before our regeneration window, about six hours out at that point.",
      "plausible_mechanism": "A production schedule and a closing operational window could plausibly create pressure to continue the planned feed-rate increase despite concerning signals.",
      "why_not_identified": "The participant did not simply execute the standard routine sequence; he considered full delay and deep investigation, then deliberately chose a modified, more conservative ramp with closer monitoring specifically because the drift note had not been confirmed resolved. No unreasoned continuation was demonstrated."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "The analysis relies on a single retrospective verbal report rather than direct behavioral observation or independent process data.",
    "The available corpus passages informed candidate bias labels and mechanisms but provided no evidence that any bias actually operated in this interview.",
    "The transcript includes extensive self-reported debiasing behavior; such self-report can be incomplete or subject to memory and self-presentation effects."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "NP_Vocab_Control_7_Gemini_on",
  "interview_id": "NP_Vocab_Control_7",
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
