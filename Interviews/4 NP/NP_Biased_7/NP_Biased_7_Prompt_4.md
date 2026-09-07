You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary debrief for our operations learning file, not a disciplinary review — anything you share is for process improvement. Can you state your role and how long you've been on this unit?

Participant: Sure. I'm a process control operator on the catalytic reforming unit, been on this board for about six years, refinery for eleven. I run the DCS console during my shift — feed rates, heater duty, reactor temps, that kind of thing.

Interviewer: Good. Let's start broad — walk me through the incident from the beginning.

Participant: It started right at shift handover, early morning. I'd just sat down at the console when the high-temperature alarm came up on the feed heater outlet. Annunciator panel lit up red, audible tone too. Honestly, my first thought was "here we go again" — that specific alarm point has been a headache for a month. Log showed it, I want to say, eleven times in the past few weeks, and every single one turned out to be instrument drift on that thermocouple. So I acknowledged it, silenced the tone, and kept going with handover.

Interviewer: Did you check anything else at that point?

Participant: Not right away, no. I was focused on the panel itself — it's the loudest thing in the room when it goes off. There was actually a pressure-differential trend creeping up on one of the other screens, but it's a quieter kind of alarm, just a slow line drifting upward, no flashing, nothing urgent-looking. I didn't pull that screen up until later in the shift.

Interviewer: Okay, let's keep going chronologically. What happened during the handover conversation itself?

Participant: Night operator gave me the rundown — said the unit had been "stable, unremarkable" for his last four hours. That matched what I was seeing on the immediate trend, so I took that at face value. There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but that felt like old news at that point since the recent hours looked clean.

Interviewer: And then?

Participant: Production wanted a feed rate bump before our regeneration window — we had about six hours before that outage started, and the schedule needed the extra throughput banked before then. So I ran the standard feed-increase sequence, same steps I've done probably a hundred times. Valve line-up, setpoint ramp, watch the outlet temp settle. I didn't stop to reconsider the sequence given the alarm and the drift note — it's just the sequence you run.

Interviewer: What happened after the increase?

Participant: Outlet temperature climbed further than I expected. Then the field operator called in from a walkdown and mentioned some heat shimmer near the firebox — visually noticeable, he said, not normal. That's when it started feeling like more than a nuisance alarm.

Interviewer: Let's go back and unpack that first decision — acknowledging the alarm as nuisance. What information did you actually have in front of you at that moment?

Participant: The alarm itself, the log history showing repeat false trips, and that pressure trend I mentioned, which I hadn't really looked at yet.

Interviewer: What alternatives did you consider?

Participant: I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality.

Interviewer: How confident were you in that read?

Participant: Pretty confident, honestly. Maybe overconfident looking back. Eleven-for-eleven is a strong pattern in your head.

Interviewer: Moving to the feed increase decision — what alternatives were on the table?

Participant: I could've delayed the increase and gone back through the multi-day trend log, or looped in the process engineer before touching setpoints. Neither felt necessary given how clean the last few hours looked.

Interviewer: When you ran the sequence, were you consciously deciding it was the right call, or was it more automatic?

Participant: If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump.

Interviewer: Let's move to the third phase, after the shimmer report. What was going through your mind?

Participant: The combination — alarm, temperature climb, shimmer — it reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template. At the same time, there's this other incident everyone still talks about, a tube rupture on a feed heater here about two years back — pretty dramatic, shut the unit down for weeks. That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing.

Interviewer: Did the current data support either of those comparisons specifically?

Participant: Looking back, not entirely. The surge event had a distinct vibration signature on the compressor — we didn't have that here at all. I didn't really stop to check for that difference before leaning toward the surge-response approach. And the tube-rupture case, our engineer later pointed out, none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.

Interviewer: What alternatives existed at that point?

Participant: I could've treated it as a new case entirely and pulled fresh heater-specific data before picking a diagnostic path, or requested an independent instrument check to test both of those past events against current readings. I did neither immediately.

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
}}
- Hidden generation specification: {{"hidden_validation_specification": {
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
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "NP_Biased_7",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Refinery process operations and control-room decision-making",
    "role": "Catalytic reforming-unit process control operator operating a DCS console",
    "objective": "Maintain safe and stable heater and unit operation while meeting a planned pre-regeneration production target",
    "incident_type": "Escalating feed-heater temperature excursion with rising pressure differential, abnormal heat-shimmer observation, and an incompletely resolved underlying fault",
    "confidence": 0.98
  },
  "structure_audit": {
    "estimated_word_count": 1120,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "The operator acknowledges and initially treats a high feed-heater outlet-temperature alarm as a recurring nuisance rather than immediately investigating it or reviewing the concurrent pressure-differential trend.",
        "evidence_before": [
          "High-temperature alarm with red annunciator indication and audible tone",
          "Operator's stated recollection or review of repeated prior nuisance trips",
          "Pressure-differential trend rising on another screen"
        ],
        "evidence_after": [
          "Pressure-differential trend is not reviewed until later",
          "The alarm is later understood as potentially meaningful in combination with other indicators"
        ],
        "goals_constraints": [
          "Complete shift handover",
          "Manage an immediately disruptive audible and visual alarm",
          "Maintain control-room situational awareness"
        ],
        "alternatives": [
          "Dispatch a field operator to independently verify the thermocouple",
          "Open the pressure-differential trend alongside the alarm",
          "Treat the alarm as potentially process-related pending corroboration"
        ],
        "decision_basis": "The operator regarded the alarm as likely spurious because it had reportedly produced repeated prior false trips and gave more attention to the prominent annunciator than to the quieter trend display.",
        "time_pressure": "Low to moderate; handover was occurring, but no immediate trip condition is described.",
        "uncertainty": "Moderate; the operator had an alarm, prior-event history, and an unreviewed contradictory trend."
      },
      {
        "id": 2,
        "summary": "The operator accepts the night-shift report of stability, discounts an older unresolved heater-duty drift note, and executes the routine feed-increase sequence without adapting it to the abnormal precursor conditions.",
        "evidence_before": [
          "Night-shift report that the unit was stable and unremarkable over the prior four hours",
          "Immediate trend that appeared consistent with recent stability",
          "Older board-log note documenting unresolved upward drift in heater duty",
          "Earlier high-temperature alarm and unreviewed pressure-differential trend"
        ],
        "evidence_after": [
          "Feed rate is increased using the normal sequence",
          "Outlet temperature rises more than expected",
          "Field operator reports abnormal heat shimmer near the firebox"
        ],
        "goals_constraints": [
          "Bank additional throughput before a regeneration outage",
          "Complete the planned feed increase",
          "Operate within a roughly six-hour production window"
        ],
        "alternatives": [
          "Delay the feed increase",
          "Review the multi-day trend and unresolved drift note",
          "Consult the process engineer before changing setpoints",
          "Modify or suspend the routine feed-increase sequence"
        ],
        "decision_basis": "The operator relied on the recent handover and immediate trend, while executing a highly familiar feed-increase procedure automatically.",
        "time_pressure": "Moderate; six hours remained before the regeneration outage.",
        "uncertainty": "Moderate to high; recent apparent stability conflicted with unresolved longer-horizon evidence and abnormal precursor signals."
      },
      {
        "id": 3,
        "summary": "After the temperature rise and shimmer report, the operator initially applies a diagnostic response template from a prior compressor-surge event and also considers a memorable historical tube rupture disproportionately likely.",
        "evidence_before": [
          "High-temperature alarm",
          "Unexpected temperature rise after feed increase",
          "Heat shimmer near the firebox",
          "Memory of a past compressor surge event",
          "Memory of a widely discussed prior feed-heater tube rupture"
        ],
        "evidence_after": [
          "The operator does not immediately obtain heater-specific data or an independent instrument check",
          "Later engineering review finds that neither the compressor-surge signature nor tube-rupture-specific markers were present"
        ],
        "goals_constraints": [
          "Rapidly diagnose an emerging abnormal condition",
          "Choose a response path under increasing operational concern"
        ],
        "alternatives": [
          "Treat the event as a novel heater-specific case",
          "Review fresh heater-specific process data before selecting a diagnostic template",
          "Request independent instrument verification",
          "Explicitly test current observations against the differentiating markers of both historical incidents"
        ],
        "decision_basis": "The operator used recalled prior incidents as diagnostic anchors despite missing distinguishing evidence.",
        "time_pressure": "Moderate and increasing; no trip setpoint is yet reached, but the condition is worsening.",
        "uncertainty": "High; available observations were compatible with multiple causes, while key discriminating signals were absent."
      },
      {
        "id": 4,
        "summary": "With less than 90 minutes before regeneration and worsening trends, the operator selects the first checklist action that appears likely to stabilize the immediate condition rather than comparing the full set of corrective options or escalating fully.",
        "evidence_before": [
          "Less than 90 minutes before the regeneration window",
          "Temperature and pressure still climbing but below trip setpoints",
          "A standard heater-excursion checklist",
          "A full process-engineer escalation estimated to require 20 to 30 minutes"
        ],
        "evidence_after": [
          "The selected action stabilizes the immediate trend",
          "A later review identifies another checklist action that may have addressed the underlying cause more completely"
        ],
        "goals_constraints": [
          "Stabilize the process promptly",
          "Avoid losing the regeneration-window opportunity",
          "Avoid escalation delay during a worsening condition"
        ],
        "alternatives": [
          "Compare all relevant checklist options",
          "Fully escalate to the process engineer",
          "Briefly consult the engineer before final action",
          "Select a corrective action aimed at root-cause resolution rather than immediate stabilization alone"
        ],
        "decision_basis": "The operator selected the first workable option under time and attention constraints without an exhaustive comparison.",
        "time_pressure": "High; the regeneration window was closing and process indicators were worsening.",
        "uncertainty": "Moderate; the immediate stabilization objective was clear, but the underlying fault and best corrective action remained uncertain."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "av_01",
      "bias": "Availability Bias",
      "requested_occurrences_for_bias": 2,
      "status": "misclassified",
      "decision_point": 1,
      "supporting_quote": "Log showed it, I want to say, eleven times in the past few weeks, and every single one turned out to be instrument drift on that thermocouple.",
      "evidence_location": "Decision point 1, initial alarm account and later retrospective explanation of the alarm-acknowledgment decision.",
      "mechanism": "The intended mechanism is availability-based probability estimation from ease of recall. However, the stated evidence is an apparently objective, highly relevant alarm-history base rate: 11 recent events, all reportedly attributable to instrument drift. Reliance on a documented and highly consistent event history is not, by itself, availability bias.",
      "strength": "weak",
      "confidence": 0.89,
      "plausible_nonbias_explanation": "The operator made an understandable, though incomplete, base-rate judgment from a repeated and specific alarm-history pattern. The error may instead be inadequate corroboration in the presence of a conflicting process trend.",
      "additional_evidence_needed": "Evidence that the operator relied on the ease of recalling salient nuisance events rather than checking the actual record, failed to assess whether the previous events were comparable, or gave recalled history disproportionate weight despite a known change in operating context.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_reasoning_revision",
        "location": "Decision point 1, participant's first explanation of why the high-temperature alarm was treated as a nuisance.",
        "current_defect": "The wording makes the alarm history a valid factual frequency signal rather than a distorted likelihood judgment driven by retrievability.",
        "minimal_change_instruction": "Retain the history of recurring nuisance trips, but add one subtle distinction showing that the operator did not verify current comparability or the actual history at the console and instead relied on how readily the recent nuisance episodes came to mind. For example, establish that the operator recalled the repeated past calls and treated that recollection as sufficient even though the current process context or alarm characteristics had not been checked against those prior cases.",
        "preserve": [
          "The same high-temperature alarm decision",
          "The repeated nuisance-alarm background",
          "The simultaneous quieter pressure-differential trend",
          "The separate salience-bias evidence at decision point 1",
          "The subtle intended strength"
        ],
        "avoid_creating": [
          "A second salience episode",
          "An explicit textbook statement that the operator was biased",
          "A new unsupported anchoring or confirmation-bias episode",
          "A change that makes the prior alarm history wholly irrelevant"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "sal_01",
      "bias": "Salience Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 1,
      "supporting_quote": "I was focused on the panel itself — it's the loudest thing in the room when it goes off. There was actually a pressure-differential trend creeping up on one of the other screens... I didn't pull that screen up until later in the shift.",
      "evidence_location": "Decision point 1, response to the question about checking anything else after the high-temperature alarm.",
      "mechanism": "A visually and audibly prominent annunciator alarm captured attention, while a less conspicuous but relevant pressure-differential trend was not examined. This is an attention-allocation mechanism distinct from the probability judgment associated with the alarm's prior history.",
      "strength": "moderate",
      "confidence": 0.96,
      "plausible_nonbias_explanation": "Alarm-management procedure may require immediate acknowledgment of the loud annunciator. Nonetheless, the participant explicitly links the alarm's prominence to failure to inspect competing relevant information, which supports the bias occurrence.",
      "additional_evidence_needed": "None required.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 1, alarm and pressure-trend account.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No change needed.",
        "preserve": [
          "The contrast between the loud, flashing alarm and the quiet, slow trend",
          "The delayed review of the pressure-differential screen",
          "The separation from the alarm-history reasoning"
        ],
        "avoid_creating": [
          "Additional claims that the pressure trend was hidden or unavailable",
          "An unnecessary second salience episode later in the narrative"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "rec_01",
      "bias": "Recency Bias",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 2,
      "supporting_quote": "There was an older note in the board log, a few days back, flagging a slow upward drift in heater duty that never really got resolved, but that felt like old news at that point since the recent hours looked clean.",
      "evidence_location": "Decision point 2, participant's account of the handover and decision to proceed with the feed increase.",
      "mechanism": "The operator appears to weight the recent four-hour handover and immediate trend more heavily than an older unresolved drift note. However, recent observations can legitimately be more diagnostic of the current process state, and the text does not establish that the older unresolved trend was discounted solely because it was older rather than because it was reasonably regarded as superseded.",
      "strength": "weak",
      "confidence": 0.77,
      "plausible_nonbias_explanation": "A four-hour stable period and current clean trend may reasonably reduce concern about an older note, particularly if the operator inferred that the issue had resolved.",
      "additional_evidence_needed": "Evidence that the operator treated temporal recency itself as clearing an unresolved condition without checking whether the earlier drift had actually stopped, been corrected, or remained causally relevant.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_reasoning_revision",
        "location": "Decision point 2, the participant's explanation for discounting the multi-day heater-duty drift note.",
        "current_defect": "The passage implies recency weighting but does not distinguish it from a justified reliance on more current operating evidence.",
        "minimal_change_instruction": "Add a concise statement that the operator treated the last four stable hours as sufficient to dismiss the unresolved multi-day trend without checking whether the drift had been corrected or whether the apparent stability merely masked it. Keep the issue centered on the older item's age and not on its frequency or memorability.",
        "preserve": [
          "The night-shift stability report",
          "The older unresolved heater-duty drift note",
          "The decision to proceed with the feed increase",
          "The separate automatic-sequence evidence for habit intrusion"
        ],
        "avoid_creating": [
          "A second availability-bias cue based on repeated alarms",
          "A new authority-bias claim based solely on accepting handover",
          "An explicit statement that recent data are always less reliable"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "hab_01",
      "bias": "Habit Intrusion",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "If I'm honest, automatic. It's muscle memory at this point. I wasn't sitting there weighing pros and cons — I was just executing the steps I always execute for a feed bump.",
      "evidence_location": "Decision point 2, response to whether the feed-increase decision was conscious or automatic.",
      "mechanism": "A highly rehearsed feed-increase action sequence was automatically executed in a context containing abnormal precursor conditions that warranted adaptation or interruption. The participant describes automatic behavioral execution rather than a deliberate evaluative judgment.",
      "strength": "strong",
      "confidence": 0.98,
      "plausible_nonbias_explanation": "Routine procedures can appropriately reduce workload. Here, however, the explicit failure to pause or adapt the routine in light of the alarm and unresolved drift evidence supports habit intrusion rather than merely skilled execution.",
      "additional_evidence_needed": "None required.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, automatic feed-increase sequence explanation.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No change needed.",
        "preserve": [
          "The automatic and frequently practiced nature of the sequence",
          "The abnormal precursor conditions",
          "The distinction between routine action execution and the separate recency-weighting judgment"
        ],
        "avoid_creating": [
          "A claim that procedure-following is inherently biased",
          "A second habit episode at the final checklist decision"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "sim_01",
      "bias": "Similarity Bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "It reminded me a lot of a compressor surge event I dealt with about a year and a half ago on a similar unit. Handled that one fine, so my instinct was to pull that same response template... The surge event had a distinct vibration signature on the compressor — we didn't have that here at all.",
      "evidence_location": "Decision point 3, account of diagnostic reasoning after the heat-shimmer report and subsequent acknowledgement of missing vibration evidence.",
      "mechanism": "The operator transferred a response template from a superficially similar historical compressor-surge event despite the absence of that event's key distinguishing vibration signature. This is pattern-matching diagnostic categorization, not merely recall-based likelihood estimation.",
      "strength": "strong",
      "confidence": 0.97,
      "plausible_nonbias_explanation": "Analogical diagnosis from a prior incident can be appropriate as an initial hypothesis. It becomes biased here because the operator did not pause to test the absent distinguishing signal before leaning into the surge-response path.",
      "additional_evidence_needed": "None required.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, compressor-surge comparison.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No change needed.",
        "preserve": [
          "The past surge event",
          "The missing vibration signature",
          "The operator's failure to test the disconfirming difference before selecting a response template",
          "The separate tube-rupture availability episode"
        ],
        "avoid_creating": [
          "A claim that all use of analogous experience is erroneous",
          "Additional hindsight-only evidence that was unavailable at the decision time"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "av_02",
      "bias": "Availability Bias",
      "requested_occurrences_for_bias": 2,
      "status": "supported",
      "decision_point": 3,
      "supporting_quote": "That one jumped to mind too, and honestly it felt like the more likely explanation just because it's the one people bring up in every shift briefing... none of the specific markers for that failure mode were actually present. It just felt present because it's such a memorable event.",
      "evidence_location": "Decision point 3, participant's comparison of the current case with the prior tube-rupture incident.",
      "mechanism": "The operator overestimates the likelihood of tube rupture because the prior incident is vivid, repeatedly discussed, and easy to retrieve, despite the current absence of the failure mode's specific markers. This is distinct from av_01 because it relies on memorability and vividness rather than recalled recurring frequency.",
      "strength": "strong",
      "confidence": 0.99,
      "plausible_nonbias_explanation": "A prior severe tube rupture could properly justify prompt consideration of that failure mode. The explicit admission that it felt likely because it was memorable, combined with absent diagnostic markers, supports availability bias.",
      "additional_evidence_needed": "None required.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 3, tube-rupture comparison.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No change needed.",
        "preserve": [
          "The vivid and repeatedly discussed historical incident",
          "The absent tube-rupture-specific markers",
          "The distinction from similarity-based transfer of the compressor-surge template"
        ],
        "avoid_creating": [
          "A second similarity-bias occurrence based on the tube-rupture case",
          "A causal claim that the past incident caused the present equipment fault"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "br_01",
      "bias": "Bounded Rationality",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 4,
      "supporting_quote": "I went with the first checklist option that looked like it would stabilize things. Didn't run through the rest of the list comparing them — just needed something workable fast.",
      "evidence_location": "Decision point 4, participant's description of the final checklist selection under the closing regeneration window.",
      "mechanism": "Under a closing time window, worsening process indicators, and escalation costs, the operator satisficed by choosing the first action judged workable rather than comparing alternatives. The participant explicitly identifies skipped comparison of other checklist actions and does not retrospectively claim the chosen option was known to be best.",
      "strength": "strong",
      "confidence": 0.97,
      "plausible_nonbias_explanation": "Rapid stabilization can be a justified risk-management choice during a worsening operational event. The occurrence remains supported because the operator had multiple listed options, selected the first workable action without comparison, and later recognized that another available option may have better addressed the underlying problem.",
      "additional_evidence_needed": "None required.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 4, final checklist selection.",
        "current_defect": "None material.",
        "minimal_change_instruction": "No change needed.",
        "preserve": [
          "The under-90-minute constraint",
          "The checklist alternatives",
          "The distinction between immediate stabilization and root-cause resolution",
          "The absence of a claim that the first option was definitely best"
        ],
        "avoid_creating": [
          "A claim that all time-constrained decisions are biased",
          "A second habit-intrusion episode based solely on use of a checklist"
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Availability Bias",
      "requested_count": 2,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    },
    {
      "bias": "Recency Bias",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    },
    {
      "bias": "Habit Intrusion",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Salience Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Similarity Bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Bounded Rationality",
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
      "bias": "Premature closure",
      "decision_point": 1,
      "supporting_quote": "I could've dispatched the field guy right then to verify the thermocouple independently, or pulled up the pressure trend side by side before acknowledging. I didn't do either — the history just made it feel like a formality.",
      "mechanism": "The operator may have accepted the nuisance-alarm explanation before checking readily available disconfirming or corroborating evidence.",
      "confidence": 0.62,
      "status": "weak",
      "plausible_nonbias_explanation": "This may simply be the downstream consequence of the same alarm-history assessment and salience-driven allocation of attention, rather than an independently identifiable diagnostic-closure bias.",
      "revision_recommendation": "remove_or_neutralize"
    },
    {
      "bias": "Normalcy bias",
      "decision_point": 2,
      "supporting_quote": "Night operator gave me the rundown — said the unit had been stable, unremarkable for his last four hours. That matched what I was seeing on the immediate trend.",
      "mechanism": "The operator may have maintained a stable-unit interpretation despite an unresolved longer-term drift and earlier alarm.",
      "confidence": 0.45,
      "status": "rejected",
      "plausible_nonbias_explanation": "The handover and immediate trend could reasonably support a stable-current-state judgment; the text does not establish an unwarranted belief that adverse change could not be occurring.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "The prior alarm history reportedly contains 11 recent events, all attributed to thermocouple instrument drift.",
      "location": "Decision point 1, initial participant account.",
      "why_not_bias": "A documented, relevant, and consistent history is legitimate evidence for a base-rate judgment. It becomes availability bias only if the decision depends disproportionately on ease of recall or untested perceived frequency rather than appropriately assessed historical comparability."
    },
    {
      "cue": "The operator accepts the night-shift report that the prior four hours were stable.",
      "location": "Decision point 2, handover account.",
      "why_not_bias": "Handover information is a normal operational evidence source. Acceptance alone is not authority bias; the relevant concern is whether the operator improperly discounted unresolved older information because of its age."
    },
    {
      "cue": "The selected checklist action stabilized the immediate process trend.",
      "location": "Decision point 4, outcome account.",
      "why_not_bias": "A favorable immediate outcome does not establish that the decision was unbiased, and a less complete root-cause response does not establish that the initial stabilization decision was wrong."
    },
    {
      "cue": "The operator had less than 90 minutes before regeneration and faced a potential 20-to-30-minute escalation discussion.",
      "location": "Decision point 4, final-decision account.",
      "why_not_bias": "Time pressure and limited cognitive resources are contextual constraints, not bias by themselves. The supported bounded-rationality occurrence depends on the explicit first-workable-option selection and skipped comparison of known alternatives."
    },
    {
      "cue": "The participant says, Maybe overconfident looking back.",
      "location": "Decision point 1, retrospective confidence probe.",
      "why_not_bias": "Retrospective self-criticism does not independently demonstrate overconfidence at the time of the decision. No pre-decision confidence calibration or unsupported certainty threshold is supplied."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "Earlier review of the pressure-differential trend would have reframed the incident sooner.",
        "support": "The participant states that seeing the trend alongside the alarm at the beginning would have changed the interpretation.",
        "assessment": "Plausible counterfactual claim, but retrospective and untested; it identifies an information-timing mechanism rather than proving that the eventual escalation would have been prevented."
      },
      {
        "claim": "Selecting another corrective checklist step probably would have addressed the underlying issue better.",
        "support": "The participant reports that a later review flagged another available checklist step.",
        "assessment": "Plausible but qualified. The term probably appropriately signals uncertainty, and the interview does not provide technical root-cause evidence sufficient to establish the claim conclusively."
      },
      {
        "claim": "Recent apparent stability justified treating an unresolved multi-day drift as old news.",
        "support": "The participant cites a stable four-hour handover and clean immediate trend.",
        "assessment": "The causal link is underdeveloped. The account does not establish whether the recent stability reflected genuine resolution, masking, different operating conditions, or a failure to inspect persistence of the drift."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "The narrative could imply that the earlier alarm-history judgment caused the later excursion.",
        "explanation": "The interview supports a possible contribution through delayed investigation, but it does not establish that the alarm response caused the physical heater fault or the ensuing temperature rise."
      },
      {
        "risk": "The later-review finding could be treated as proof that the skipped checklist action would have prevented the incident.",
        "explanation": "The available account supports only a retrospective possibility that another action would have been more complete; it does not provide a controlled comparison or technical failure analysis."
      }
    ],
    "counterfactual_present": true,
    "changed_variable": "The participant poses two retrospective hypothetical changes: earlier simultaneous visibility of the pressure-differential trend, and more time before the regeneration window closed.",
    "held_constant": [],
    "causal_coherence": "moderate",
    "explanation": "The interview contains useful participant-level counterfactual probes, but it is not a formal paired counterfactual. The first hypothetical isolates information timing reasonably well, although other conditions are only implicit. The second changes available time while also invoking both broader checklist comparison and engineer consultation, so it does not isolate one decision mechanism. These limitations do not conflict with the hidden specification because no paired scenario or counterfactual variable was required."
  },
  "quality_scores": {
    "occupational_realism": 91,
    "cta_fidelity": 88,
    "bias_separability": 79,
    "bias_subtlety": 82,
    "control_fidelity": 100,
    "counterfactual_fidelity": 71,
    "narrative_coherence": 90,
    "naturalness": 86,
    "hidden_label_integrity": 86,
    "overall_quality": 83
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 5,
    "requested_occurrence_total": 7,
    "missing_occurrence_total": 2,
    "accidental_occurrence_total": 0,
    "priority": "medium",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Preserve the four-decision-point chronology and catalytic-reforming control-room setting.",
      "Do not alter the supported salience, habit-intrusion, similarity, vividness-based availability, or bounded-rationality episodes.",
      "Repair av_01 by distinguishing memory availability from objectively warranted alarm-history base-rate reasoning.",
      "Repair rec_01 by showing that unresolved older evidence was discounted because it was older, not merely because recent information was legitimately more diagnostic.",
      "Avoid adding explicit bias labels, didactic explanations, or new causal claims about the physical root cause.",
      "Do not create an additional premature-closure or authority-bias occurrence while clarifying the two weak mechanisms."
    ],
    "revision_order": [
      "Revise av_01 locally at decision point 1 to make recalled nuisance-event accessibility, rather than verified frequency, the driver of the likelihood judgment.",
      "Revise rec_01 locally at decision point 2 to establish unjustified temporal discounting of an unresolved drift condition.",
      "Re-audit the revised text to ensure that av_01 and rec_01 are independently identifiable and that the changes have not created additional accidental bias occurrences."
    ]
  },
  "failure_flags": [
    "av_01 is labeled Availability Bias in the manifest, but the present text primarily supports an objectively grounded alarm-history base-rate judgment rather than availability bias.",
    "rec_01 does not yet adequately distinguish improper recency weighting from potentially justified reliance on more recent operating evidence.",
    "The interview's retrospective counterfactual probes are informative but do not hold alternative causal variables explicitly constant."
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
