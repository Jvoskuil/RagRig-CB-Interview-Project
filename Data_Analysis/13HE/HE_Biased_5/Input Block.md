<RAW_INTERVIEW>
**Interviewer:** Thanks for taking the time. Just to confirm — this is a cognitive task analysis interview, it's confidential, and I'll be asking you to reconstruct a specific incident in detail. There's no evaluation of your performance here, just your reasoning process. Can you start by telling me your role and roughly when this happened?

**Participant:** Sure. I'm a process safety engineer at the site — I cover the batch nitration unit among others. This was about four months ago, night shift transition. I'd just come on when the trend started.

**Interviewer:** Good. Before we get into the sequence, what was the operational objective that shift?

**Participant:** Straightforward — get the batch through its exothermic hold step cleanly and into the next unit operation without deviation, so we could hand off a clean batch at shift change. Nothing unusual planned.

**Interviewer:** Walk me through what first drew your attention to the reactor.

**Participant:** The DCS trend. Pressure was running about eight percent above the expected curve for that stage of the hold. Temperature was fine, right in band, which is usually the first thing you check because if temperature's climbing too you're thinking runaway. It wasn't. So it read more like an instrumentation quirk than a reaction problem, at least on the surface.

**Interviewer:** What did you do with that information?

**Participant:** Well, by the time I'd pulled up the trend, the shift supervisor and two operators were already standing around the panel talking about it. And honestly, that conversation shaped things a lot. Someone said "this looks like the same thing we saw in March," and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier. I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure. We'd had two prior deviations like this, both chalked up to sensor drift, no incident either time. That history was doing a lot of work in the room.

**Interviewer:** So what was the actual decision at that point — stop the batch, escalate, or continue?

**Participant:** Continue monitoring. We didn't interrupt. Looking back, the alternative was to call an emergency hold pending manual inspection, or escalate straight to the on-call plant manager. I didn't push for either. The shared read in the room was "probably the same sensor issue," and that's the frame I went with.

**Interviewer:** What happened next?

**Participant:** Pressure kept climbing, slowly, over about twenty minutes. Eventually the relief valve lifted — you could hear it, a distinct pop — and then pressure fell back and reseated. No release beyond the relief line, nobody hurt. But at that point we genuinely didn't know if the batch chemistry itself was compromised.

**Interviewer:** How did you move from "we had a relief lift" to a root cause?

**Participant:** I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion. A full instrument and kinetics review would've taken three to four hours, and that would blow past shift changeover, so there was real pressure to land on something workable.

**Interviewer:** Did anything about this batch differ from the two prior "drift" events?

**Participant:** Yeah, actually — this batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily. It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review.

**Interviewer:** How confident were you in that diagnosis at the time?

**Participant:** Fairly confident, honestly. I've been on this unit a long time, I've seen this signature before. It felt like a case I recognized rather than a case I needed to dig into further.

**Interviewer:** What did you learn afterward that touched on that conclusion?

**Participant:** A partial calibration spot-check later showed the transmitter was actually within tolerance. That undercuts the drift explanation somewhat. And nobody had gone back and independently reviewed the new catalyst lot's exotherm profile. So the diagnosis I'd settled on quickly was never really closed out on the chemistry side.

**Interviewer:** Let's move to the mitigation decision. What options were in front of you?

**Participant:** The external relief-system contractor reviewed the incident and came back with a data package showing our existing relief system had a narrower margin than we'd assumed, specifically for this catalyst lot. Their recommendation was to add an automated high-pressure interlock trip before restart. It's a system with a decent track record at two comparable plants. The alternative was keeping our current manual response procedure, which has run for years here without failure.

**Interviewer:** What did you decide?

**Participant:** I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet. Our manual process, whatever its limits, was a known quantity.

**Interviewer:** How did you weigh the contractor's margin data against that operational familiarity?

**Participant:** I didn't dismiss the margin data, I just — I think I gave more weight to the fact that the interlock was unproven here specifically, on our unit, with our people. The margin reduction was real on paper, but it hadn't caused an actual failure yet either. The known system winning out over the new one felt like the safer bet.

**Interviewer:** Any information afterward relevant to that call?

**Participant:** The plant manager pointed out later that adding the interlock then would've cost about one shift of downtime, versus none for keeping status quo. And no further excursions happened for the rest of the campaign, so we never really got a clean test of whether the interlock would've mattered.

**Interviewer:** Take me into the MOC meeting. Who was there and what was the disagreement?

**Participant:** Myself, the senior process safety engineer — he was on the original commissioning team for this unit, well known across the plant for a strong safety record — and the contractor. The senior engineer backed my sensor-drift read, said it matched his experience with the unit over the years. The contractor's written analysis flagged the catalyst-lot kinetics as an open gap and recommended keeping the MOC open until that was resolved. No new data had come in since the calibration check.

**Interviewer:** How did you resolve that?

**Participant:** I sided with the senior engineer's view. He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site. And frankly, his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it. The contractor's point was on paper, but it felt like an outside read compared to someone who's actually run this unit for fifteen years.

**Interviewer:** What happened after the MOC closed?

**Participant:** We restarted without the kinetics review. Production since then hasn't clearly proven or disproven that call either way.

**Interviewer:** Looking back across the shift, where did time pressure weigh most heavily?

**Participant:** Definitely the root cause call and the MOC closure — both had that shift-changeover clock running, and neither had a hard deadline forcing an answer, but it felt like there was one.

**Interviewer:** If the contractor's report had arrived before the control-room discussion instead of after, do you think the outcome changes?

**Participant:** Possibly. If that margin data had been sitting on the table before everyone converged on "probably fine," it might have slowed the room down. Order mattered more than I'd like to admit.

**Interviewer:** If a less senior colleague had proposed the sensor-drift explanation in that MOC meeting, would you have accepted it as readily?

**Participant:** Probably not with the same confidence, no.

**Interviewer:** What would you do differently with a similar deviation on a new catalyst lot?

**Participant:** Flag the lot change explicitly, early, before pattern-matching to prior events — treat it as its own case rather than assuming it inherits the old explanation.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Biased_5",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Process Safety Engineer (Chemical/Industrial Facility)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Pressure Excursion During Batch Nitration Reaction – Emergency MOC Review",
    "scenario_summary_internal": "A process safety engineer at a specialty chemicals plant is called in when a batch nitration reactor shows an unexpected pressure trend during an exothermic hold step. Over roughly six hours, the engineer must judge whether to interrupt production, diagnose the anomaly's root cause, decide on a mitigation path before restart, and then defend or revise that plan in a Management of Change (MOC) review meeting attended by senior colleagues and an external relief-system contractor. The incident resolves as a near-miss (no release, but a relief valve lifted briefly), leaving the true root cause only partially confirmed, which allows reasoning quality to be assessed independently of outcome.",
    "occupational_realism": {
      "objective": "Determine the safe path to diagnose and resolve an unexplained pressure rise in a batch nitration reactor and decide whether/how to modify the safety system before restart, without an unplanned release or unnecessary production loss.",
      "setting": "Control room and MOC meeting room at a mid-sized specialty chemicals plant running a batch nitration process with an exothermic hold step, relief valve, rupture disc, and DCS trend monitoring.",
      "constraints": [
        "Batch is mid-cycle; halting risks a hazardous off-spec intermediate requiring costly neutralization",
        "Only one other process safety engineer with deep nitration experience is on-site",
        "External relief-system contractor's recommendation would require a capital change request and 48-hour delay",
        "Plant management wants restart before the next shift changeover",
        "Historical sensor drift on this unit has occurred twice before with no consequence"
      ],
      "stakeholders": [
        "Process Safety Engineer (interviewee)",
        "Senior Process Safety Engineer (long-tenured colleague, original commissioning team)",
        "Shift Supervisor",
        "External Relief System Contractor",
        "Plant Manager"
      ],
      "technical_terms_to_use": [
        "exothermic hold step",
        "relief valve lift",
        "rupture disc",
        "Management of Change (MOC)",
        "batch nitration",
        "DCS trend",
        "runaway reaction",
        "set-point deviation",
        "interlock",
        "root cause analysis"
      ],
      "technical_terms_to_avoid": [
        "group polarization",
        "Dunning-Kruger",
        "illusion of understanding",
        "risk aversion bias",
        "in-group bias",
        "halo effect",
        "cognitive bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "DCS trend shows reactor pressure 8% above the expected curve for this stage of the hold step",
          "Temperature readings remain within normal band",
          "Similar deviations twice before were attributed to sensor drift with no incident",
          "Shift supervisor and two operators are already discussing the trend informally in the control room"
        ],
        "new_information_after_decision": [
          "Pressure continues to climb slowly over the next 20 minutes, prompting a relief valve lift with an audible pop before pressure falls back",
          "No release beyond the relief line; batch integrity uncertain"
        ],
        "alternatives": [
          "Initiate an emergency hold/interrupt of the batch pending manual inspection",
          "Continue monitoring per the group's shared read that this is 'probably the same sensor issue as before'",
          "Escalate immediately to the on-call plant manager before any further trend data"
        ],
        "intended_action": "Continue monitoring alongside the control room team after their discussion converges on a shared, more confident read that the deviation is benign, rather than independently interrupting the batch"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Relief valve has lifted and reseated; no operators injured, no offsite release",
          "Historical precedent of sensor drift exists but was never confirmed by calibration record",
          "Reaction chemistry for this batch involves a newer catalyst lot not present in the two prior 'drift' events",
          "Full instrument calibration check would take 3-4 hours and delay restart past shift changeover"
        ],
        "new_information_after_decision": [
          "A partial calibration spot-check later shows the pressure transmitter was within tolerance, weakly undercutting the sensor-drift explanation",
          "The new catalyst lot's exotherm profile has not been independently reviewed"
        ],
        "alternatives": [
          "Commission a full instrument and reaction-kinetics root cause review before concluding on a cause",
          "Conclude quickly that this matches the known sensor-drift pattern based on surface similarity to prior events",
          "Treat the cause as indeterminate and hold restart until confirmed"
        ],
        "intended_action": "Quickly conclude the cause is the familiar sensor-drift pattern, treating personal familiarity with two prior similar-looking events as sufficient understanding of this batch's more complex reaction-kinetics picture"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "External contractor's data package shows the existing relief system has a narrower margin for this catalyst lot than previously assumed",
          "Contractor recommends adding an automated high-pressure interlock trip before restart",
          "The interlock has an established reliability record at two comparable plants but is unfamiliar to this site's operators",
          "Existing manual response procedure has functioned without failure for years on this unit"
        ],
        "new_information_after_decision": [
          "Plant manager later notes the interlock addition would have cost one shift of downtime versus none",
          "No further pressure excursions occur during the remaining campaign, leaving the counterfactual value of the interlock unresolved"
        ],
        "alternatives": [
          "Approve the automated interlock addition given the contractor's margin analysis",
          "Retain the current manual response procedure, citing its long unblemished track record",
          "Approve a phased trial of the interlock on the next batch only"
        ],
        "intended_action": "Retain the current manual procedure, weighting the small, unfamiliar risk of introducing a new interlock more heavily than the demonstrated margin reduction it would address"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "MOC meeting includes the senior process safety engineer (original commissioning team member, well regarded plant-wide for a strong safety record) and the external contractor",
          "Senior engineer states his view aligns with the interviewee's sensor-drift explanation, citing 'years of experience with this unit'",
          "Contractor's written analysis flags unreviewed catalyst-lot kinetics as an open technical gap and recommends against closing the MOC until resolved",
          "No new instrumentation or kinetics data has been generated since phase 2"
        ],
        "new_information_after_decision": [
          "MOC is closed and batch restarted without kinetics review",
          "Later production data does not clearly confirm or refute the closure decision, leaving the basis for review"
        ],
        "alternatives": [
          "Weigh the contractor's documented technical gap independently of who raised it and keep the MOC open pending kinetics review",
          "Side with the senior in-house engineer's read because he is a known, trusted colleague from the original commissioning team",
          "Request a neutral third review to break the disagreement"
        ],
        "intended_action": "Side with the senior colleague's conclusion partly because he is a trusted long-standing in-house team member rather than the outside contractor, and give his view added weight because of his broader plant-wide safety reputation rather than the specific technical merits of this catalyst-lot question"
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first drew your attention to this reactor on that shift?",
        "What was your role and what was the operational objective at that moment?"
      ],
      "timeline_reconstruction": [
        "What happened right after the pressure trend was first noticed?",
        "Walk me through the sequence from the relief valve lift to the MOC closure.",
        "What information did you have at each stage, and what changed afterward?"
      ],
      "decision_point_probes": [
        "At the point of the initial pressure deviation, what cues made you continue monitoring rather than interrupt the batch?",
        "What sources of information shaped your read of the control room discussion?",
        "When you settled on the sensor-drift explanation, what alternatives did you consider and why did you rule them out?",
        "How confident were you in that diagnosis, and what would have changed that confidence?",
        "What made you favor keeping the manual response procedure over the contractor's interlock proposal?",
        "How did you weigh the contractor's margin analysis against operational familiarity with the existing system?",
        "In the MOC meeting, how did you resolve the disagreement between the senior engineer and the contractor?",
        "What role did each person's background or track record play in how you weighed their input?",
        "Looking back, how much time pressure did you feel at each stage, and how did that affect your reasoning?",
        "Where did you feel most uncertain, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the contractor's report had arrived before the control room discussion instead of after, do you think the outcome would have changed?",
        "If a different, less senior engineer had proposed the sensor-drift explanation, would you have accepted it as readily?",
        "What would you do differently if a similar pressure deviation occurred again with a new catalyst lot?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "gp_01",
        "bias": "Group Polarization",
        "decision_point": 1,
        "mechanism": "Informal control-room discussion among the supervisor, operators, and the engineer converges toward a more extreme, more confident version of the initial mild leaning ('probably fine') than any individual held before talking, leading to continued monitoring instead of an independent interrupt",
        "affected_reasoning_operation": "Group risk judgment formation prior to an interrupt/continue decision",
        "evidence_available_at_time": [
          "8% pressure deviation from expected curve",
          "normal temperature readings",
          "two prior benign 'drift' precedents",
          "ongoing informal group discussion in the control room"
        ],
        "required_textual_manifestation": "Interviewee describes the group's shared confidence increasing through discussion beyond what any one person initially felt, and cites that collective confidence as the reason for not interrupting the batch independently",
        "plausible_nonbias_interpretation": "Consulting colleagues before an operationally costly interrupt could be framed as reasonable teamwork rather than polarization",
        "strength": "subtle",
        "do_not_make_explicit": ["group polarization", "peer pressure", "risky shift"]
      },
      {
        "instance_id": "dk_01",
        "bias": "Dunning-Kruger effect or Illusion of understanding",
        "decision_point": 2,
        "mechanism": "Interviewee treats surface similarity to two prior sensor-drift events as sufficient basis for a confident causal conclusion, without recognizing that the new catalyst lot introduces a reaction-kinetics variable outside that prior experience, overestimating the completeness of their diagnostic picture",
        "affected_reasoning_operation": "Causal attribution / root cause conclusion under incomplete data",
        "evidence_available_at_time": [
          "no confirmed calibration record for prior 'drift' events",
          "new catalyst lot not present in prior events",
          "time pressure to avoid a 3-4 hour full root cause review"
        ],
        "required_textual_manifestation": "Interviewee expresses high confidence in the sensor-drift conclusion drawn quickly from pattern-matching, without acknowledging the catalyst-lot kinetics as an unreviewed unknown, and frames the quick conclusion as adequately thorough",
        "plausible_nonbias_interpretation": "Using pattern recognition from prior experience is a legitimate expert heuristic under time pressure",
        "strength": "moderate",
        "do_not_make_explicit": ["Dunning-Kruger", "illusion of understanding", "overconfidence"]
      },
      {
        "instance_id": "ra_01",
        "bias": "Risk aversion bias",
        "decision_point": 3,
        "mechanism": "Interviewee disproportionately weights the small, unfamiliar risk of introducing a new automated interlock (change-related risk) over the better-documented, larger margin-reduction risk of retaining the current manual procedure, despite the contractor's data favoring the change",
        "affected_reasoning_operation": "Mitigation option selection under asymmetric framing of gains versus losses",
        "evidence_available_at_time": [
          "contractor's margin analysis showing narrower safety margin for the new catalyst lot",
          "interlock's established reliability record at comparable plants",
          "unit's long-standing manual procedure track record"
        ],
        "required_textual_manifestation": "Interviewee justifies keeping the manual procedure primarily by pointing to the unfamiliarity and novelty risk of the interlock, giving that more weight than the documented margin reduction the interlock would address",
        "plausible_nonbias_interpretation": "Preferring a proven procedure over an unfamiliar automated system could reflect a legitimate reliability-engineering caution about untested interfaces",
        "strength": "subtle",
        "do_not_make_explicit": ["risk aversion", "loss aversion", "status quo bias"]
      },
      {
        "instance_id": "ig_01",
        "bias": "In-group bias",
        "decision_point": 4,
        "mechanism": "Interviewee gives the senior in-house colleague's conclusion added credibility specifically because he is a long-standing member of the original commissioning team (an in-house, in-group source), independent of the technical content of his argument, while discounting the external contractor's dissenting written analysis",
        "affected_reasoning_operation": "Evidence-source weighting during a technical disagreement at MOC closure",
        "evidence_available_at_time": [
          "senior colleague's verbal agreement citing tenure with the unit",
          "contractor's written report flagging unreviewed catalyst-lot kinetics",
          "no new technical data generated since phase 2"
        ],
        "required_textual_manifestation": "Interviewee explains siding with the senior colleague by referencing his being part of 'our team' or the original commissioning group, treating that affiliation as a reason to discount the outside contractor's technical flag",
        "plausible_nonbias_interpretation": "In-house staff often do have superior tacit knowledge of a specific unit, so deferring to them could be a legitimate expertise judgment",
        "strength": "subtle",
        "do_not_make_explicit": ["in-group bias", "outsider distrust", "us versus them"]
      },
      {
        "instance_id": "he_01",
        "bias": "Halo effect",
        "decision_point": 4,
        "mechanism": "Interviewee extends the senior colleague's general plant-wide reputation for a strong safety record into an unwarranted assumption that his specific claim about catalyst-lot kinetics is also technically sound, without separately evaluating that specific claim",
        "affected_reasoning_operation": "Credibility transfer from general reputation to a specific unverified technical claim",
        "evidence_available_at_time": [
          "senior colleague's plant-wide reputation for safety performance",
          "his specific claim on this batch's kinetics is unverified by new data",
          "contractor's specific, documented technical gap remains unaddressed"
        ],
        "required_textual_manifestation": "Interviewee cites the senior colleague's overall reputation or track record as a reason to trust his specific, unverified claim about this batch's chemistry, treating the general trait as evidence for the specific one",
        "plausible_nonbias_interpretation": "A strong track record can be legitimately relevant background context when time does not allow full independent verification",
        "strength": "subtle",
        "do_not_make_explicit": ["halo effect", "reputation transfer", "trait generalization"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, not a control variant"
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
      "Confirm exactly 4 decision points and exactly 5 planned bias instances, one per manifest entry",
      "Confirm ig_01 and he_01 share decision point 4 but use distinct evidence sources (verbal in-group affiliation claim vs. general reputation-to-specific-claim transfer) per co-location rule",
      "Confirm no bias term, definition, or label appears in probes or intended dialogue content",
      "Confirm each instance has a plausible non-bias interpretation documented",
      "Confirm consequences (near-miss, unresolved root cause, no clear outcome proof) do not mechanically validate or invalidate any single decision",
      "Confirm target length 1,350 words (range 1,215-1,485) is achievable given 4 decision points, 5 instances, and required probe coverage without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Group Polarization",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via observable shift toward group extremity in a collective monitoring decision, not individual reasoning alone"
      },
      {
        "bias": "Dunning-Kruger effect or Illusion of understanding",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via overconfident causal conclusion drawn from incomplete pattern-matching, ignoring a known unknown (new catalyst lot)"
      },
      {
        "bias": "Risk aversion bias",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via disproportionate weighting of unfamiliar-change risk over documented status-quo risk in a mitigation choice"
      },
      {
        "bias": "In-group bias",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via crediting an in-house colleague's view due to team affiliation rather than technical content"
      },
      {
        "bias": "Halo effect",
        "occurrences": 1,
        "mechanism_constraint": "must manifest via transferring general reputation to credibility of a specific unverified technical claim"
      }
    ],
    "target_bias_names": [
      "Group Polarization",
      "Dunning-Kruger effect or Illusion of understanding",
      "Risk aversion bias",
      "In-group bias",
      "Halo effect"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Group Polarization", "requested_occurrences": 1 },
      { "bias": "Dunning-Kruger effect or Illusion of understanding", "requested_occurrences": 1 },
      { "bias": "Risk aversion bias", "requested_occurrences": 1 },
      { "bias": "In-group bias", "requested_occurrences": 1 },
      { "bias": "Halo effect", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "gp_01", "bias": "Group Polarization" },
      { "instance_id": "dk_01", "bias": "Dunning-Kruger effect or Illusion of understanding" },
      { "instance_id": "ra_01", "bias": "Risk aversion bias" },
      { "instance_id": "ig_01", "bias": "In-group bias" },
      { "instance_id": "he_01", "bias": "Halo effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "gp_01", "bias": "Group Polarization", "decision_point": 1 },
      { "instance_id": "dk_01", "bias": "Dunning-Kruger effect or Illusion of understanding", "decision_point": 2 },
      { "instance_id": "ra_01", "bias": "Risk aversion bias", "decision_point": 3 },
      { "instance_id": "ig_01", "bias": "In-group bias", "decision_point": 4 },
      { "instance_id": "he_01", "bias": "Halo effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "gp_01",
        "bias": "Group Polarization",
        "mechanism": "Collective discussion in the control room shifts the group's confidence toward a more extreme benign judgment than any individual initially held, driving continued monitoring instead of an independent interrupt",
        "affected_reasoning_operation": "Group risk judgment formation before interrupt/continue decision",
        "evidence_source": "Informal control-room discussion among supervisor, operators, and engineer",
        "distinctiveness_requirement": "Only instance of this bias; occurs at decision point 1 via group discussion dynamics, not individual cognition"
      },
      {
        "instance_id": "dk_01",
        "bias": "Dunning-Kruger effect or Illusion of understanding",
        "mechanism": "Confident causal conclusion drawn from superficial pattern match to prior events, unaware that the new catalyst lot places the current situation outside prior experience",
        "affected_reasoning_operation": "Causal attribution / root cause conclusion under incomplete data",
        "evidence_source": "Two prior 'drift' precedents plus new, unreviewed catalyst-lot variable",
        "distinctiveness_requirement": "Only instance of this bias; occurs at decision point 2 as an individual diagnostic judgment, distinct in evidence and operation from gp_01"
      },
      {
        "instance_id": "ra_01",
        "bias": "Risk aversion bias",
        "mechanism": "Disproportionate weight given to the unfamiliar risk of a new interlock relative to the better-documented margin-reduction risk of the status quo procedure",
        "affected_reasoning_operation": "Mitigation option selection under asymmetric gain/loss framing",
        "evidence_source": "Contractor's margin analysis versus unit's manual-procedure track record",
        "distinctiveness_requirement": "Only instance of this bias; occurs at decision point 3, involving a change-versus-status-quo choice distinct from prior decision points"
      },
      {
        "instance_id": "ig_01",
        "bias": "In-group bias",
        "mechanism": "Crediting a colleague's conclusion because of shared team membership, discounting an outsider's written technical objection",
        "affected_reasoning_operation": "Evidence-source weighting during MOC technical disagreement",
        "evidence_source": "Senior colleague's verbal agreement citing team tenure",
        "distinctiveness_requirement": "Shares decision point 4 with he_01 but uses a distinct evidence source (team-affiliation statement) and reasoning operation (source-of-origin weighting) rather than trait-based credibility transfer"
      },
      {
        "instance_id": "he_01",
        "bias": "Halo effect",
        "mechanism": "General reputation for safety performance is used to validate an unrelated, specific, unverified technical claim about catalyst-lot kinetics",
        "affected_reasoning_operation": "Credibility transfer from general trait to specific claim",
        "evidence_source": "Senior colleague's plant-wide reputation record",
        "distinctiveness_requirement": "Shares decision point 4 with ig_01 but uses a distinct evidence source (reputation record) and reasoning operation (trait-to-claim generalization) rather than group-affiliation weighting"
      }
    ],
    "intended_strength": [
      { "instance_id": "gp_01", "bias": "Group Polarization", "strength": "subtle" },
      { "instance_id": "dk_01", "bias": "Dunning-Kruger effect or Illusion of understanding", "strength": "moderate" },
      { "instance_id": "ra_01", "bias": "Risk aversion bias", "strength": "subtle" },
      { "instance_id": "ig_01", "bias": "In-group bias", "strength": "subtle" },
      { "instance_id": "he_01", "bias": "Halo effect", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "HE_Biased_5",
    "domain_id": "HE",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points by mechanism fit and narrative realism: one bias per decision point at DP1-DP3; DP4 hosts two biases (In-group bias and Halo effect) because the MOC closure moment naturally involves both source-affiliation weighting and reputation-based credibility transfer, kept distinct via separate evidence sources and reasoning operations per co-location rule (max two per decision point, no more than two of the same bias anywhere).",
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
          "segment_type": "initial interpretation",
          "raw_interview_anchor": "The participant interprets the pressure trend as more likely an instrumentation quirk than a reaction problem because temperature remains in band.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A plausible initial technical interpretation is expressed, but no hidden bias manifestation is required in this span."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "group-influenced decision rationale",
          "raw_interview_anchor": "The participant describes entering the control-room discussion unsure, becoming more confident after others converged on the prior sensor-issue interpretation, and using that shared read to continue monitoring.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gp_01"
          ],
          "ground_truth_rationale": "The group discussion amplifies confidence beyond the participant's initial uncertainty and supports continuing monitoring rather than independently interrupting or escalating."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "causal diagnosis",
          "raw_interview_anchor": "After the relief-valve lift, the participant quickly concludes that the event is the familiar sensor-drift pattern, acknowledges the new catalyst lot, but says he did not weight that difference heavily and did not wait for the fuller review.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "dk_01"
          ],
          "ground_truth_rationale": "The participant treats surface similarity and prior familiarity as sufficient for a confident causal conclusion despite an unreviewed catalyst-lot variable and incomplete diagnostic picture."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "mitigation option selection",
          "raw_interview_anchor": "The participant recommends retaining the manual response procedure because operators know it, the interlock is unfamiliar, and the known system feels safer despite the contractor's documented margin reduction.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ra_01"
          ],
          "ground_truth_rationale": "The small unfamiliarity risk of the interlock is weighted more heavily than the documented safety-margin risk that the interlock would address."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "MOC evidence weighting and closure",
          "raw_interview_anchor": "In the MOC meeting, the participant sides with the senior in-house engineer, citing the original team, long unit experience, excellent safety record, and the contractor's status as an outside read, then closes the MOC without the kinetics review.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "ig_01",
            "he_01"
          ],
          "ground_truth_rationale": "This span contains both affiliation-based discounting of the outside contractor and transfer of the senior colleague's general safety reputation to a specific unverified technical claim."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "retrospective rationale",
          "raw_interview_anchor": "The participant identifies shift-changeover time pressure as influential in the root-cause call and MOC closure.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Time pressure is contextual information and is not itself a hidden bias manifestation."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "counterfactual information-order assessment",
          "raw_interview_anchor": "The participant says receiving the contractor report before the control-room discussion might have slowed convergence and that order mattered.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a retrospective counterfactual and does not create an additional hidden instance."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "future corrective action",
          "raw_interview_anchor": "For a future deviation with a new catalyst lot, the participant would flag the lot change early and treat the case independently rather than pattern-match to prior events.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "This is a corrective reflection on future practice, not a separate biased decision in the incident."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
