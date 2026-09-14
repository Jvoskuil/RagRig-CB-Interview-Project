You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
    "analysis_scope_note": "Evaluates the participant's reasoning episodes from initial repeated hydraulic caution-light interpretation through final RTS certification. Only findings with affirmative mechanism-grounded interview evidence are classified as identified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which people judge the likelihood or frequency of an event by how easily similar examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth caution event: reset and continue flying versus full FIM isolation",
      "decision_point_description": "Whether to accept the OEM field rep's and in-house remembered pattern as sufficient to avoid the full fault isolation procedure.",
      "affected_reasoning_operation": "Diagnostic probability judgment / fault classification",
      "bias_specific_mechanism": "The participant used the ease and vividness of two recalled similar cases, the OEM rep's service-bulletin pattern and an in-house caution-light event, to infer that the current fault was the same benign software/BITE quirk, without verifying whether the cases matched current conditions or explaining the speed brake anomaly.",
      "manifestation_in_interview": "The participant stated that the OEM read and memory made it feel like they already had the answer, and later admitted those recollections tipped the decision despite not checking whether the old in-house case matched on flight hours or component batch.",
      "effect_on_reasoning_or_decision": "The participant overrode the senior hydraulics engineer's recommendation for full FIM isolation and kept the aircraft on a reset-and-continue path, delaying discovery of a possible mechanical source.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Between the OEM read and that memory, it felt like we already had the answer, so I told my engineer we'd hold off on the full isolation, do the reset, and keep flying it.",
          "evidence_explanation": "This directly ties the decision to readily recalled examples rather than diagnostic data, the mechanism underlying availability-based inference."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the OEM rep's experience and the in-house case were what tipped it. I didn't go back and check whether that old in-house case actually matched this one on flight hours or component batch—it just felt like the same animal.",
          "evidence_explanation": "The participant explicitly acknowledges reliance on recalled cases and failure to compare diagnostic specifics, which is a hallmark availability heuristic distortion."
        }
      ],
      "correction_or_counterevidence": "The senior hydraulics engineer argued that the speed brake anomaly changed the picture and wanted the formal FIM procedure; later hydraulic pump seal residue suggested a mechanical source rather than the assumed benign BITE quirk.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": ["sunk cost bias", "escalation of commitment"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue a course of action because resources have already been invested, even when changing course would better serve future goals.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-residue repair decision: seal replacement versus full pump replacement",
      "decision_point_description": "Whether to escalate to full hydraulic pump replacement after new residue evidence, or complete the existing incremental repair path with a seal replacement.",
      "affected_reasoning_operation": "Resource allocation and escalation decision",
      "bias_specific_mechanism": "The participant treated unrecoverable labor already spent on the existing repair path as a reason not to open a larger job, explicitly noting that full pump replacement would make some past work 'for nothing.'",
      "manifestation_in_interview": "When asked whether prior work affected the choice, the participant acknowledged that it factored in and framed the seal fix as a way to close out without starting over.",
      "effect_on_reasoning_or_decision": "The participant chose to replace the seal and continue the incremental plan rather than escalating to full pump replacement, even though the new residue suggested a possible mechanical source and the participant later stated that fresh evaluation would favor full pump replacement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd sunk real hours into the path we were on, and pulling the pump entirely would've meant some of that work was for nothing. The seal fix looked like it would close it out without starting over.",
          "evidence_explanation": "Explicitly uses past investment to justify continuing the current course, the core diagnostic feature of sunk cost reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Coming in fresh, without hours already spent, I think full pump replacement looks more obviously like the right call.",
          "evidence_explanation": "Removing sunk costs changes the participant's evaluation, reinforcing that unrecoverable effort distorted the forward-looking repair decision."
        }
      ],
      "correction_or_counterevidence": "There were legitimate logistical factors such as part availability and downtime pressure, and the residue was minor; however these do not explain the participant's explicit reliance on past hours spent.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "overconfidence effect",
      "alternative_labels": ["overconfidence bias", "overprecision"],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to have greater subjective confidence in a judgment than the available evidence warrants, or to overestimate the precision of one's knowledge.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Final RTS certification after ground leak check",
      "decision_point_description": "Whether to sign the RTS certification and return the aircraft to the schedule without a same-day functional test flight.",
      "affected_reasoning_operation": "Risk assessment and certification confidence",
      "bias_specific_mechanism": "The participant expressed high confidence that the leak-based repair resolved the intermittent fault while simultaneously acknowledging that ground static tests could not reproduce the in-flight warning condition; this indicates subjective confidence exceeding the diagnostic evidence.",
      "manifestation_in_interview": "The participant told operations he was confident the issue was resolved and later said he was 'pretty sure,' despite the known limitation of the ground checks.",
      "effect_on_reasoning_or_decision": "The aircraft was released to service without a test flight, with high confidence communicated to the ops desk.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Ground data looked good—leak check passed, static test clean—so I signed the RTS certification. I told the ops desk I was confident this was resolved.",
          "evidence_explanation": "Shows high confidence in resolution based on ground checks alone."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Pretty sure, honestly. I knew the ground checks couldn't reproduce the exact in-flight condition that triggered the caution—static testing just isn't the same environment. But a passed leak check is normally what we'd treat as proof a leak-based repair worked, and I didn't see a reason to hold the airplane on top of that.",
          "evidence_explanation": "Acknowledges a major evidence gap but nonetheless maintains strong confidence and generalizes a standard test result to the unresolved in-flight failure mode, consistent with overconfidence."
        }
      ],
      "correction_or_counterevidence": "No post-release outcome is reported, so objective miscalibration cannot be confirmed. A passed leak check may be a legitimate domain heuristic, which is why this occurrence is assigned low confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved scientific passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": ["biased assimilation", "confirmatory bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Fourth caution event: weighing OEM rep and in-house case against engineer's FIM request",
      "supporting_interview_quote": "He wasn't thrilled. He felt the speed brake anomaly changed the picture and wanted the formal procedure regardless. But the OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
      "plausible_mechanism": "The participant may have preferentially weighted or selected information confirming the initial nuisance-signal interpretation and discounted the engineer's disconfirming speed brake anomaly.",
      "why_not_identified": "The transcript does not clearly establish motivated information search or weighting independent of legitimate reliance on broader OEM expertise; the core distortion is better explained by the availability heuristic and therefore this remains candidate."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "normalcy bias",
      "alternative_labels": ["normalcy bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Early repeated CND events: interpreting recurrent hydraulic cautions as nuisance signal",
      "supporting_interview_quote": "Intermittent hydraulic caution lights aren't unusual, honestly. Sensors can be noisy, especially early in a duty cycle. Each event was short—two seconds, three seconds, then about five—and with nothing showing on inspection, my read was this was probably a nuisance signal that would settle down on its own once we cycled the system a few more times.",
      "plausible_mechanism": "Normalcy bias could have produced under-reaction to an escalating warning pattern by normalizing repeated intermittent cautions.",
      "why_not_identified": "The assessment may have been a reasonable diagnostic prior based on clean inspections and absent corroborating hydraulic data; no affirmative distortion is established."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "authority bias",
      "alternative_labels": ["expert deference"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Fourth caution event: OEM field rep opinion versus internal engineer recommendation",
      "supporting_interview_quote": "The OEM rep works this aircraft type across a lot of operators, so I leaned toward his read over running a full teardown-style isolation on a holiday week.",
      "plausible_mechanism": "The participant may have over-weighted the OEM rep's opinion because of perceived authority or outside expertise rather than the diagnostic content of the advice.",
      "why_not_identified": "Deference to an OEM field representative with relevant fleet experience can be a legitimate professional heuristic; there is insufficient evidence of a status-based distortion."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus was supplied in the RAG context, so all labels and mechanisms are based on established cognitive-science knowledge rather than retrieved passages.",
    "No post-release operational outcome is reported; the overconfidence finding is based on stated certainty relative to acknowledged evidence gaps rather than objective miscalibration.",
    "The analysis relies on self-reported interview testimony, which may be affected by retrospective reconstruction.",
    "Several plausible distortions are recorded as candidates rather than identified occurrences due to the conservative evidence threshold."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Biased_5_Gemini_off",
  "interview_id": "AV_Biased_5",
  "system_prompt_id": "Gemini",
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
