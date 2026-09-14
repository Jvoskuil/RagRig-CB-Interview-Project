<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're okay with this being used for a maintenance decision-making review, and that we can reference the tail number and event details generically without naming crew.

Participant: That's fine, go ahead.

Interviewer: Great. Can you tell me your role and how you came into this event?

Participant: I'm the Director of Maintenance at our base station. I oversee line maintenance sign-offs, RTS certifications, and I'm the one who ultimately owns whether an aircraft goes back into the schedule. This one landed on my desk because it kept coming back.

Interviewer: Walk me through what the issue looked like when you first became aware of it.

Participant: We had a Hydraulic System B caution light show up on one of our E175s—momentary, cleared itself, crew wrote it up. Maintenance ran the BITE test, came back clean, no fault found. Classic CND. It happened three times over about two weeks. Each time, no fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL. The aircraft kept flying its line.

Interviewer: What did you make of that pattern at the time?

Participant: Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times. We had the holiday peak coming up and needed the airframe in rotation, so grounding it for an open-ended isolation hunt on a CND item felt like overkill at that point.

Interviewer: Did the increasing duration register as significant to you?

Participant: I noticed it, sure. But two to five seconds isn't a big jump in absolute terms, and without any corroborating fluid or pressure data, I didn't see it as a trend that was going anywhere serious. I figured we'd keep an eye on it.

Interviewer: What happened next?

Participant: Next flight day, it came back a fourth time, and this one ran about twelve seconds—longer than anything before—and the crew also noted a brief speed brake anomaly on the same leg. That's when my senior hydraulics engineer came to me and wanted to pull the aircraft and run the full fault isolation procedure out of the FIM.

Interviewer: What did you decide at that point, and how did you get there?

Participant: While we were talking about it, our OEM field rep happened to be at the hangar working a different tail. I flagged him down and asked what he thought. He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up. One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back. Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.

Interviewer: How did your engineer take that?

Participant: He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.

Interviewer: What information did you weigh most heavily there, and what didn't you dig into?

Participant: Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal. We reset the BITE and flew it two cycles without a recurrence.

Interviewer: What came after that?

Participant: A few days later, during an unrelated task, one of the techs was near the hydraulic pump and noticed some residue around the seal. Small amount, hadn't been documented before. That was new—nothing like that had shown up in any of the earlier CND checks.

Interviewer: What did that change for you?

Participant: It told us there might be an actual mechanical source rather than just a sensor quirk. At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan. Full pump replacement would've meant more downtime and we didn't have the part on the shelf yet. Since we were most of the way through the incremental plan already, and the residue was minor, I decided to just replace the seal and finish what we'd started rather than open up a bigger job.

Interviewer: Did the amount of work already done factor into that choice?

Participant: I'd say it factored in some. We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.

Interviewer: After the seal replacement, what did you see?

Participant: Leak check passed on the ground, static test showed no residue. Clean.

Interviewer: What happened at the final sign-off?

Participant: We needed the aircraft that afternoon for the holiday schedule, and we didn't have a test-flight crew available same-day. Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved.

Interviewer: Given the aircraft's history—three CND events, the fourth longer one with the speed brake note, and the fact that the seal residue never really explained why the caution happened in flight in the first place—how sure were you that this was actually fixed?

Participant: Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.

Interviewer: If you'd had a test-flight crew available that day, would that have changed your certainty?

Participant: It would've been a nice extra data point, but I don't think it would've changed my decision to release it.

Interviewer: Looking back across the whole event, is there a point where, with the same information you had then, you'd make a different call?

Participant: Maybe the fourth event—the twelve-second one with the speed brake anomaly. If I'd leaned more toward my engineer's read there instead of the OEM rep's, we might have caught the seal issue earlier instead of a few days later.

Interviewer: If the OEM rep hadn't been on-site that day, what do you think you'd have done instead?

Participant: Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction.

Interviewer: Last one—if the seal residue had turned up before you'd started the component swaps, would the escalation decision have gone differently?

Participant: Probably, yeah. Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Biased_5",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Director of Maintenance (DOM)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Intermittent Hydraulic Caution Light Ahead of Holiday Peak Schedule",
    "scenario_summary_internal": "A regional airline DOM manages a recurring, intermittently-clearing Hydraulic System B caution light on an E175 across a five-day window while under pressure to keep the aircraft flying into a holiday traffic peak. The DOM downplays an early worsening trend, defers to an informally-consulted OEM rep and a superficially similar past case over his own senior engineer's request for full fault isolation, continues an incremental repair path partly because of hours/parts already invested once a real leak is found, and finally certifies return-to-service on ground-only data with more certainty than the evidence supports.",
    "occupational_realism": {
      "objective": "Restore the aircraft to safe, dispatch-reliable service while meeting a schedule commitment for an upcoming holiday travel peak.",
      "setting": "Line maintenance hangar at a regional carrier's base station, over a five-day period involving three flight days and two ground/troubleshooting days.",
      "constraints": [
        "Holiday peak schedule requiring the aircraft back in rotation within days",
        "Limited hangar slot availability and competing aircraft needing the same bay",
        "Parts lead time for hydraulic components",
        "Pressure from VP of Operations on dispatch reliability metrics",
        "Limited access to OEM engineering support beyond an informally present field rep",
        "No dedicated test-flight crew available same-day as final repair"
      ],
      "stakeholders": [
        "Director of Maintenance (interviewee)",
        "Senior avionics/hydraulics engineer (line maintenance)",
        "OEM field technical representative",
        "VP of Operations",
        "Scheduling/Ops control",
        "Line pilots reporting the squawks",
        "Quality assurance / RTS signoff authority"
      ],
      "technical_terms_to_use": [
        "MEL (Minimum Equipment List)",
        "CND (could not duplicate)",
        "BITE test",
        "Hydraulic System B",
        "non-routine card",
        "fault isolation manual (FIM)",
        "accumulator",
        "pump seal residue",
        "leak check",
        "return to service (RTS)",
        "squawk",
        "test flight",
        "service bulletin"
      ],
      "technical_terms_to_avoid": [
        "optimism bias",
        "authority bias",
        "sunk cost fallacy",
        "representativeness heuristic",
        "overconfidence bias",
        "cognitive bias",
        "heuristic",
        "confirmation",
        "anchoring"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Three pilot writeups over two weeks of momentary Hydraulic System B caution light, each cleared as CND on ground BITE test",
          "No fluid loss or visible leakage found on any inspection",
          "Aircraft has continued flying on schedule with no MEL restriction",
          "Duration of the caution light has crept up slightly across the three events (roughly 2, 3, then 5 seconds)"
        ],
        "new_information_after_decision": [
          "A fourth occurrence the next day with the light lasting about 12 seconds",
          "Crew also notes a brief speed brake anomaly during that same flight"
        ],
        "alternatives": [
          "Ground the aircraft for extended fault isolation (pump pressure decay test) before the holiday peak",
          "Sign off as an intermittent nuisance and continue dispatch under monitoring, deferring deep troubleshooting to the next scheduled check"
        ],
        "intended_action": "DOM authorizes continued dispatch with informal monitoring rather than immediate deep troubleshooting."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Fourth, longer-duration caution light event plus a speed brake anomaly",
          "Senior line engineer requests a full fault isolation procedure per the FIM",
          "OEM field rep, present at the hangar for an unrelated aircraft, is asked informally for a read on the symptom pattern",
          "OEM rep recalls a service bulletin describing a benign software/BITE quirk on another operator's fleet with similar symptoms",
          "A team member recalls a prior in-house case with a hydraulic caution light that resolved after a simple reset"
        ],
        "new_information_after_decision": [
          "BITE reset performed; aircraft flies two clean cycles",
          "A cursory pump seal inspection during a later task turns up small fluid residue not previously documented"
        ],
        "alternatives": [
          "Ground the aircraft for the senior engineer's proposed full isolation procedure",
          "Accept the OEM rep's informal read and the recalled prior case, reset BITE, and clear the aircraft to continue flying"
        ],
        "intended_action": "DOM overrides the senior engineer's isolation request, accepts the OEM rep's casual assessment and the recalled similar case, and clears the aircraft after a reset."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pump seal residue confirmed on inspection, a new finding not present in the earlier CND checks",
          "14 labor hours and several replaced components (accumulator, sensor) already invested in the prior troubleshooting path",
          "The incremental component-swap plan is nearly complete; only the seal remains to be addressed",
          "Full hydraulic pump replacement would require additional downtime and parts not yet on hand"
        ],
        "new_information_after_decision": [
          "Seal is replaced; ground leak check passes",
          "Static ground test shows no further visible residue"
        ],
        "alternatives": [
          "Escalate to a full hydraulic pump teardown/replacement given the new leak evidence",
          "Continue the already-planned incremental path and replace only the seal"
        ],
        "intended_action": "DOM approves the seal-only fix and declines full pump replacement, citing the work and parts already committed to the current path."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Ground leak check passed after seal replacement",
          "Static test shows no residue, but no post-repair test flight has been performed",
          "No test-flight crew available same day; aircraft is needed for an afternoon departure into the holiday peak",
          "History of three prior CND events and one earlier misdiagnosis of the same general system on this tail"
        ],
        "new_information_after_decision": [
          "Aircraft is dispatched on the scheduled flight",
          "Outcome of the flight is not yet known at the time of the interview"
        ],
        "alternatives": [
          "Require a test flight or extended ground run before certifying return to service",
          "Certify return to service immediately based on ground-only data"
        ],
        "intended_action": "DOM signs the RTS certification expressing high confidence the issue is resolved, based on ground test data alone."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what this aircraft's hydraulic issue looked like when you first became aware of it.",
        "What was your role in this event day to day?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you learn at each step?",
        "What changed between the first CND write-up and the fourth event?",
        "Who did you talk to as this unfolded, and what did each of them tell you?"
      ],
      "decision_point_probes": [
        "At the point you decided to keep flying it after the third write-up, what specific information made you comfortable with that?",
        "When the OEM rep gave his read, how much weight did that carry compared to your own engineer's request, and why?",
        "Once the seal residue turned up, what made you stick with the seal-only plan rather than escalating?",
        "When you signed the RTS certification, what evidence were you relying on, and how sure were you it would hold?"
      ],
      "information_sources": [
        "What sources of information did you trust most during this event, and why?",
        "Was there any data you didn't look at or didn't request? Why not?"
      ],
      "goals_and_alternatives": [
        "What other options did you consider at each stage, and why did you rule them out?",
        "How did the schedule pressure factor into which option you picked?"
      ],
      "decision_basis": [
        "If you had to justify this decision to a regulator afterward, what would you point to?",
        "How confident were you at each stage, on a scale of 1-10, and what moved that number?"
      ],
      "prior_experience": [
        "Had you seen anything like this before? How did that history shape your read of this case?"
      ],
      "time_pressure_and_uncertainty": [
        "How much did the holiday schedule weigh on your timeline for these decisions?",
        "What were you still uncertain about when you made the final call?"
      ],
      "closing_hypotheticals": [
        "If the OEM rep hadn't been on-site that day, what do you think you would have done differently?",
        "If the seal residue had shown up before the component swaps instead of after, would your approach have changed?",
        "Looking back, is there a point where you'd make a different call with the same information you had at the time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ob_01",
        "bias": "Optimism Bias",
        "decision_point": 1,
        "mechanism": "DOM interprets an increasing-duration trend across three intermittent events as unlikely to worsen or recur meaningfully, favoring continued dispatch over deeper investigation.",
        "affected_reasoning_operation": "Risk/trend projection from repeated CND events",
        "evidence_available_at_time": [
          "Three CND write-ups with slightly increasing caution-light duration",
          "No fluid loss found on inspection"
        ],
        "required_textual_manifestation": "DOM states or implies expectation that the issue will likely resolve itself or stay minor, despite the visible upward trend in duration, and chooses monitoring over isolation.",
        "plausible_nonbias_interpretation": "A reasonable read that CND-with-no-fluid-loss findings genuinely support low urgency under MEL policy.",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "trend denial", "risk underestimation"]
      },
      {
        "instance_id": "ab_01",
        "bias": "Authority Bias",
        "decision_point": 2,
        "mechanism": "DOM gives disproportionate weight to the informally-offered opinion of the OEM field rep (present for an unrelated task) over the formal, procedure-based recommendation of his own senior engineer.",
        "affected_reasoning_operation": "Weighting of competing expert recommendations",
        "evidence_available_at_time": [
          "OEM rep's casual, unofficial verbal assessment referencing a different fleet's bulletin",
          "Senior engineer's formal request to run the FIM fault isolation procedure"
        ],
        "required_textual_manifestation": "DOM explains overriding or setting aside the senior engineer's request because the OEM rep's title/affiliation carried more weight, without evaluating whether the rep's informal opinion was actually procedurally grounded for this case.",
        "plausible_nonbias_interpretation": "OEM reps do carry specialized fleet-wide knowledge, so deferring to one is often reasonable practice.",
        "strength": "moderate",
        "do_not_make_explicit": ["authority bias", "deference to titles", "status-based weighting"]
      },
      {
        "instance_id": "rh_01",
        "bias": "Representativeness Heuristic",
        "decision_point": 2,
        "mechanism": "Team matches the current symptom set (caution light + hydraulic system) to a superficially similar prior in-house case and infers the same root cause and fix, without checking dissimilar underlying details (different flight-hour history, different component batch, no borescope check).",
        "affected_reasoning_operation": "Case-pattern matching / categorical inference from surface similarity",
        "evidence_available_at_time": [
          "Recalled prior case file involving a hydraulic caution light resolved by reset",
          "Absence of comparison on flight hours, component batch, or physical inspection depth between the two cases"
        ],
        "required_textual_manifestation": "DOM or team member cites the prior case as reason to expect the same resolution, without probing whether the underlying mechanism actually matches.",
        "plausible_nonbias_interpretation": "Drawing on past maintenance history is a legitimate diagnostic starting point in troubleshooting.",
        "strength": "moderate",
        "do_not_make_explicit": ["representativeness heuristic", "base rate neglect", "surface similarity"]
      },
      {
        "instance_id": "scf_01",
        "bias": "Sunk Cost Fallacy",
        "decision_point": 3,
        "mechanism": "DOM continues the incremental component-replacement plan primarily because of labor hours and parts already spent, discounting the new leak evidence that arguably warrants escalation to full pump replacement.",
        "affected_reasoning_operation": "Cost-based justification for continuing a diagnostic path versus updating on new evidence",
        "evidence_available_at_time": [
          "14 labor hours and multiple replaced components already committed",
          "Newly discovered pump seal residue not accounted for in the original plan"
        ],
        "required_textual_manifestation": "DOM references the hours/parts already invested as a reason to finish the current plan rather than escalate, in a way that is tied to past investment rather than the new evidence.",
        "plausible_nonbias_interpretation": "Completing an almost-finished diagnostic path before escalating can be a legitimate efficiency judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment", "past investment justification"]
      },
      {
        "instance_id": "ocb_01",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "DOM certifies RTS with a stated or implied high degree of certainty that the fix has resolved the issue, exceeding what ground-only test data (no test flight, prior CND/misdiagnosis history) can support.",
        "affected_reasoning_operation": "Calibration of confidence in a decision against the actual strength of supporting evidence",
        "evidence_available_at_time": [
          "Passed ground leak check and clean static test",
          "No post-repair test flight",
          "History of three prior CND events and one earlier misdiagnosis of the same system"
        ],
        "required_textual_manifestation": "DOM expresses strong certainty ('confident this is resolved') in the RTS decision without qualifying that the fix has not been flight-verified.",
        "plausible_nonbias_interpretation": "Ground-based leak checks are an accepted, standard basis for RTS decisions in many maintenance contexts.",
        "strength": "moderate",
        "do_not_make_explicit": ["overconfidence bias", "miscalibration", "unverified certainty"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased condition, no paired control generated in this specification."
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
      "Exactly 4 decision points are defined in the timeline",
      "Exactly 5 total bias instances planned, matching the manifest total",
      "No two instances of the same bias occur; each named bias has exactly 1 occurrence as requested",
      "Decision point 2 carries two distinct biases (authority, representativeness) with clearly separate evidence sources",
      "No bias labels, definitions, or psychological terminology appear in probe_plan or timeline content intended for the public interview",
      "Each occurrence has a documented plausible non-bias interpretation",
      "Consequences described (test-flight-free RTS, unresolved final outcome) do not mechanically confirm or deny bias",
      "Target word count 1,215-1,485 achievable given 4 decision points with probes and chronological narrative"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Optimism Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Authority Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Sunk Cost Fallacy", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Representativeness Heuristic", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Overconfidence Bias", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Optimism Bias",
      "Authority Bias",
      "Sunk Cost Fallacy",
      "Representativeness Heuristic",
      "Overconfidence Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Optimism Bias", "requested_occurrences": 1 },
      { "bias": "Authority Bias", "requested_occurrences": 1 },
      { "bias": "Sunk Cost Fallacy", "requested_occurrences": 1 },
      { "bias": "Representativeness Heuristic", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "ob_01", "bias": "Optimism Bias" },
      { "instance_id": "ab_01", "bias": "Authority Bias" },
      { "instance_id": "rh_01", "bias": "Representativeness Heuristic" },
      { "instance_id": "scf_01", "bias": "Sunk Cost Fallacy" },
      { "instance_id": "ocb_01", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "ob_01", "bias": "Optimism Bias", "decision_point": 1 },
      { "instance_id": "ab_01", "bias": "Authority Bias", "decision_point": 2 },
      { "instance_id": "rh_01", "bias": "Representativeness Heuristic", "decision_point": 2 },
      { "instance_id": "scf_01", "bias": "Sunk Cost Fallacy", "decision_point": 3 },
      { "instance_id": "ocb_01", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ob_01",
        "bias": "Optimism Bias",
        "mechanism": "Projects a benign trajectory from a worsening-duration CND pattern, favoring continued dispatch over isolation",
        "affected_reasoning_operation": "Risk/trend projection",
        "evidence_source": "Three CND write-ups with increasing light duration",
        "distinctiveness_requirement": "Only instance tied to trend projection at decision point 1; must not repeat at other points"
      },
      {
        "instance_id": "ab_01",
        "bias": "Authority Bias",
        "mechanism": "Overweights informal OEM rep opinion over senior engineer's formal procedural request based on rep's perceived status/affiliation",
        "affected_reasoning_operation": "Weighting of competing expert recommendations",
        "evidence_source": "OEM rep's verbal, informal assessment",
        "distinctiveness_requirement": "Must be evidenced via deference to rep specifically, distinct from rh_01's case-matching evidence"
      },
      {
        "instance_id": "rh_01",
        "bias": "Representativeness Heuristic",
        "mechanism": "Infers same root cause/fix from superficial symptom similarity to a prior case without checking dissimilar underlying facts",
        "affected_reasoning_operation": "Case-pattern matching",
        "evidence_source": "Recalled prior in-house case file",
        "distinctiveness_requirement": "Must be evidenced via case-recall/pattern-matching, distinct from ab_01's deference-to-person evidence, even though co-located at decision point 2"
      },
      {
        "instance_id": "scf_01",
        "bias": "Sunk Cost Fallacy",
        "mechanism": "Continues incremental repair plan due to hours/parts already invested rather than updating fully on new leak evidence",
        "affected_reasoning_operation": "Cost-based justification vs. evidence updating",
        "evidence_source": "14 labor hours and replaced components already committed",
        "distinctiveness_requirement": "Sole instance tied to past-investment justification at decision point 3"
      },
      {
        "instance_id": "ocb_01",
        "bias": "Overconfidence Bias",
        "mechanism": "Expresses certainty in fix exceeding what ground-only, non-flight-verified evidence supports",
        "affected_reasoning_operation": "Confidence calibration against evidence strength",
        "evidence_source": "Ground leak check and static test results only, no test flight",
        "distinctiveness_requirement": "Sole instance tied to final RTS certification confidence at decision point 4"
      }
    ],
    "intended_strength": [
      { "instance_id": "ob_01", "bias": "Optimism Bias", "strength": "subtle" },
      { "instance_id": "ab_01", "bias": "Authority Bias", "strength": "moderate" },
      { "instance_id": "rh_01", "bias": "Representativeness Heuristic", "strength": "moderate" },
      { "instance_id": "scf_01", "bias": "Sunk Cost Fallacy", "strength": "subtle" },
      { "instance_id": "ocb_01", "bias": "Overconfidence Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_5",
    "domain_id": "AV",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points by mechanism fit and narrative realism; decision point 2 hosts two distinct biases (Authority Bias, Representativeness Heuristic) each with a separate evidence source (informal OEM rep statement vs. recalled prior case file) per rule 4 of allocation guidance; no decision point contains two occurrences of the same bias.",
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
        "segment_type": "maintenance_decision_reasoning",
        "raw_interview_anchor": "No fluid loss, nothing on inspection, so operationally we didn't have grounds to restrict it under the MEL.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "A procedural/MEL-based dispatch rationale without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "risk_trend_interpretation",
        "raw_interview_anchor": "This was probably a nuisance signal that would settle down on its own... I didn't see it as a trend that was going anywhere serious.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ob_01"
        ],
        "ground_truth_rationale": "The participant projects a benign trajectory despite increasing caution duration and chooses monitoring over deeper isolation."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "case_pattern_matching",
        "raw_interview_anchor": "It felt like we already had the answer... it just felt like the same animal.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "rh_01"
        ],
        "ground_truth_rationale": "The prior in-house case is treated as matching without checking flight hours or component-batch differences."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "expert_evidence_weighting",
        "raw_interview_anchor": "The OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ab_01"
        ],
        "ground_truth_rationale": "The informal OEM representative's status and experience are weighted over the senior engineer's formal procedural recommendation."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "repair_scope_decision",
        "raw_interview_anchor": "We'd sunk real hours into the path we were on... the seal fix looked like it would close it out without starting over.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "scf_01"
        ],
        "ground_truth_rationale": "Prior labor and component investment materially support continuing the incremental plan despite new leak evidence."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "confidence_calibration",
        "raw_interview_anchor": "Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition... but I didn't see a reason to hold the airplane.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ocb_01"
        ],
        "ground_truth_rationale": "The participant expresses strong certainty while acknowledging that ground testing did not reproduce the relevant in-flight condition."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analyzed the full CTA interview for affirmatively evidenced cognitive-bias mechanisms only. No retrieved corpus passages were provided, so any named labels rely on general cognitive-science knowledge with that limitation disclosed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "authority bias",
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
      "bias_label": "escalation of commitment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["selective evidence weighting", "congeniality bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to seek, interpret, favor, and recall information in ways that confirm one's pre-existing beliefs while giving disproportionately little weight to disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth recurrent hydraulic event escalation decision",
      "decision_point_description": "Choosing between the senior engineer's recommendation to run full fault isolation and the OEM rep's suggestion that a reset would clear the software/BITE quirk.",
      "affected_reasoning_operation": "Weighing conflicting diagnostic evidence",
      "bias_specific_mechanism": "The participant's initial nuisance-signal interpretation persisted as a hypothesis, leading him to favor the OEM rep's congruent read and the in-house memory while discounting the engineer's disconfirming speed-brake anomaly.",
      "manifestation_in_interview": "After a clean CND pattern, the participant maintained a nuisance-signal belief and treated the OEM and in-house anecdotal confirmation as sufficient; he did not investigate whether the remembered similar case actually matched.",
      "effect_on_reasoning_or_decision": "He decided against the formal fault isolation and continued flying after a reset, delaying the discovery of mechanical seal residue.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times.",
          "evidence_explanation": "Establishes the pre-existing belief that later becomes the lens through which new evidence is filtered."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
          "evidence_explanation": "Shows contradictory engineering evidence being set aside in favor of an external read consistent with the participant's nuisance-signal hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "Indicates a failure to seek disconfirming diagnostic detail after adopting the congruent answer."
        }
      ],
      "correction_or_counterevidence": "The senior engineer expressly disagreed and argued that the speed brake anomaly changed the picture; the participant did not adopt this disconfirming view at that decision point.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "authority bias",
      "alternative_labels": ["expert authority heuristic", "credibility heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to assign excessive weight to an opinion because of the source's authority, status, or expertise, independently of the strength of the underlying evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth recurrent hydraulic event escalation decision",
      "decision_point_description": "Deciding whether to accept the OEM field rep's reset recommendation or the senior engineer's formal fault isolation recommendation.",
      "affected_reasoning_operation": "Evaluation and acceptance of diagnostic information from different sources",
      "bias_specific_mechanism": "The participant used the OEM rep's type experience across operators as the dominant reason to prefer that read over the local engineer's procedure, even though the engineer had direct aircraft-specific and speed-brake anomaly information.",
      "manifestation_in_interview": "The participant explicitly says he leaned toward the OEM rep's read because the rep works the aircraft type across many operators, and later confirms that without the outside read he probably would have let the engineer run isolation.",
      "effect_on_reasoning_or_decision": "The participant declined the formal fault isolation and selected a reset, reducing diagnostic scrutiny of the speed brake anomaly.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He said he'd seen this pattern before—some kind of software or BITE quirk that another operator's fleet had flagged in a service bulletin, and that a reset usually cleared it up.",
          "evidence_explanation": "Provides the expert suggestion that was adopted as the likely answer."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
          "evidence_explanation": "Explicitly grounds the decision in the source's authority/experience rather than in verification of the hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably would've let my engineer run the full isolation. Having an outside read available in the moment made it easy to go a different direction.",
          "evidence_explanation": "Counterfactually confirms the social-influence effect of the OEM rep's presence on the decision."
        }
      ],
      "correction_or_counterevidence": "The senior engineer was not in favor and wanted the formal procedure regardless; the participant noted this but did not follow it.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["representativeness heuristic", "analogical overgeneralization"],
      "taxonomy_status": "established_label",
      "bias_definition": "Cognitive shortcut whereby judgments are influenced by the ease with which a relevant instance or example comes to mind, potentially leading to overgeneralization from a salient case.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth recurrent hydraulic event escalation decision",
      "decision_point_description": "Use of an in-house past case as evidence that a reset would clear the current hydraulic caution pattern.",
      "affected_reasoning_operation": "Diagnostic analogy and probability judgment",
      "bias_specific_mechanism": "A single, easily recalled past case of a caution light resolving after a reset dominated the diagnostic judgment, without checking whether the old case matched the present aircraft's hours or component batch.",
      "manifestation_in_interview": "The participant treated the remembered in-house case as 'the same animal' despite not comparing relevant attributes.",
      "effect_on_reasoning_or_decision": "Reinforced the choice to skip the full fault isolation and pursue the reset path.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "One of my own guys also remembered we'd had something similar in-house a while back, a caution light that went away after a reset and never came back.",
          "evidence_explanation": "Shows the salient recalled instance that became central to the diagnostic judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "Demonstrates judgment by felt similarity to the recalled case rather than diagnostic matching."
        }
      ],
      "correction_or_counterevidence": "No check of the old case's flight hours, component batch, or diagnostic details was performed; the engineer's concern was another unexamined contrary signal.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "escalation of commitment",
      "alternative_labels": ["sunk cost fallacy", "sunk cost effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "An increased commitment to a previous course of action because of previously invested resources, even when prospective evidence or cost/benefit analysis favors a different course.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Seal residue discovered after 14 hours of troubleshooting",
      "decision_point_description": "Choosing between a seal replacement and completing the existing incremental plan versus opening a full pump replacement job.",
      "affected_reasoning_operation": "Maintenance action selection after new physical evidence",
      "bias_specific_mechanism": "The participant explicitly weighed already sunk labor and the desire to avoid making prior work 'for nothing' when deciding not to move to a full pump replacement.",
      "manifestation_in_interview": "After discovering residue indicating a possible mechanical source, the participant continued the original incremental path partly because fourteen hours had already been spent.",
      "effect_on_reasoning_or_decision": "He selected seal replacement and finished the current path rather than escalating to the full pump replacement that, by his own later counterfactual, might have been more clearly indicated if the residue had appeared earlier.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "At that point we'd already put about fourteen hours into troubleshooting—swapped the accumulator, replaced a sensor—chasing the original plan.",
          "evidence_explanation": "Establishes the prior investment that entered the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.",
          "evidence_explanation": "Explicit sunk-cost rationale: avoiding loss of prior work influenced the decision to stay on the existing path."
        }
      ],
      "correction_or_counterevidence": "There were also non-bias constraints: full pump replacement required more downtime and the part was not on the shelf; however the transcript separately evidences the sunk-cost reasoning itself.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence effect",
      "alternative_labels": ["overconfidence bias", "overprecision"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency for subjective confidence in a judgment or decision to exceed the objective evidentiary basis or calibration of that judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final RTS certification after ground leak and static checks",
      "decision_point_description": "Signing the return-to-service certification without a same-day flight-test crew.",
      "affected_reasoning_operation": "Assessment of repair verification sufficiency",
      "bias_specific_mechanism": "The participant acknowledged that ground checks could not reproduce the in-flight condition that triggered the caution, yet expressed high confidence that the repair was resolved and that the release decision was correct.",
      "manifestation_in_interview": "He told operations he was confident this was resolved and said the absence of a flight test would not have changed his decision.",
      "effect_on_reasoning_or_decision": "The aircraft was released despite an acknowledged gap between ground validation and the original in-flight fault condition.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved.",
          "evidence_explanation": "Shows high confidence in the release decision based on ground checks."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.",
          "evidence_explanation": "Demonstrates certainty exceeding the acknowledged limitations of the verification evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It would've been a nice extra data point, but I don't think it would've changed my decision to release it.",
          "evidence_explanation": "Further expresses high confidence in the release decision even without the missing flight-test validation."
        }
      ],
      "correction_or_counterevidence": "Practical constraints existed: no same-day test-flight crew was available and the holiday schedule required the aircraft; release may also have been consistent with standard practice, but the expressed confidence over the known validation gap supports the finding.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied. The label and mechanism are assigned from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "normalcy bias",
      "alternative_labels": ["anchoring bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial interpretation of first three intermittent hydraulic caution events",
      "supporting_interview_quote": "Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times.",
      "plausible_mechanism": "The participant may have under-weighted an emerging warning pattern by anchoring to the initial CND/nuisance-signal baseline and assuming continued normal operation.",
      "why_not_identified": "The transcript also supplies ordinary technical and evidential reasons—small absolute duration differences, no corroborating fluid/pressure data, and no MEL restriction—that can explain the initial interpretation without requiring a distinct normalcy/anchoring mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were available in the RAG context, so no corpus-backed evidence could be supplied for any occurrence.",
    "Several findings converge on the same fourth-event escalation decision; occurrences were separated because each rests on a distinguishable mechanism and evidence source.",
    "Operational constraints such as holiday schedule pressure, part availability, and lack of a test-flight crew are not classified as biases unless a distinct bias-specific mechanism is directly evidenced."
  ]
}
</RAG_ANALYSIS_OUTPUT>
