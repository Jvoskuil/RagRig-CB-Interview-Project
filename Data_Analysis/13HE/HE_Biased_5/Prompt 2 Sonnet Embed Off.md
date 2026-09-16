You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The transcript was analyzed for bias-specific mechanisms using a conservative, mechanism-first standard. No retrieved corpus passages were supplied with this task; therefore, labels reflect established cognitive-science taxonomy from general knowledge and are not retrieval-grounded."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Group polarization",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Representativeness heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Group polarization",
      "alternative_labels": [
        "Social proof",
        "Bandwagon effect",
        "Informational social influence"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Group polarization is the tendency for discussion to strengthen the dominant point of view and produce a final group position that is more confident or extreme than the average pre-discussion individual position.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial pressure deviation assessment and continue-monitoring decision",
      "decision_point_description": "Whether to continue monitoring, stop the batch, or escalate after seeing pressure running about eight percent above the expected curve.",
      "affected_reasoning_operation": "Risk judgment / interpretation of ambiguous instrument deviation",
      "bias_specific_mechanism": "The participant's initial uncertainty about the pressure deviation was reduced by listening to others in the control room who already treated it as benign, resulting in a collectively amplified confidence in the sensor-drift explanation.",
      "manifestation_in_interview": "Before joining the conversation the participant was unsure; afterward he adopted the consensus benign frame and did not push for an emergency hold or escalation. He explicitly attributes the confidence shift to the room discussion and prior drift events.",
      "effect_on_reasoning_or_decision": "The group's settled benign interpretation led to a continue-monitoring decision, so no manual inspection or escalation was initiated during the initial deviation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Someone said 'this looks like the same thing we saw in March,' and someone else agreed, and by the time I'd joined in, the feeling in the room was pretty settled — everyone was more confident it was benign than any one of us probably was on our own five minutes earlier.",
          "evidence_explanation": "This directly states that the group converged on a stronger benign interpretation than any individual held before the discussion."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking, going into that conversation, I wasn't sure, but coming out of it I felt fairly sure.",
          "evidence_explanation": "This shows the participant's judgment changed from individual uncertainty to collective confidence through the group interaction."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The shared read in the room was 'probably the same sensor issue,' and that's the frame I went with.",
          "evidence_explanation": "This demonstrates adoption of the group frame for the subsequent monitoring decision."
        }
      ],
      "correction_or_counterevidence": "A non-bias explanation might be that the group rationally pooled prior similar events. However, the participant's explicit statement that the group became more confident than any individual had been before supports a group-polarization mechanism rather than simple information aggregation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus evidence was supplied; this label is assigned from general cognitive-science knowledge and should not be treated as retrieval-grounded.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": [
        "Confirmation bias",
        "Availability heuristic",
        "Anchoring effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The representativeness heuristic is judging the probability or category membership of an event by how similar it is to a familiar prototype while ignoring diagnostic base-rate or individuating information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-relief root-cause diagnosis",
      "decision_point_description": "Whether to classify the relief-lift event as recurring sensor drift or to initiate a fuller instrument/kinetics review.",
      "affected_reasoning_operation": "Causal attribution / diagnostic inference",
      "bias_specific_mechanism": "The participant classified the current event as belonging to the same sensor-drift category based on surface similarity to two prior drift events and underweighted the novel catalyst-lot feature, which was individuating information that made this batch different.",
      "manifestation_in_interview": "He quickly concluded drift after the relief valve lifted, acknowledged that the new catalyst lot differed from the earlier drift events, but explicitly said he did not weight that feature heavily and was comfortable calling it drift without a fuller review.",
      "effect_on_reasoning_or_decision": "The diagnosis of sensor drift remained in place, and a full instrument/kinetics review was not initiated before shift changeover; the catalyst-lot exotherm profile was not evaluated at that time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I concluded fairly quickly it was the same sensor drift pattern we'd seen before. It matched — same unit, same kind of gradual pressure creep, no temperature excursion.",
          "evidence_explanation": "This shows category membership was inferred from surface similarity to prior drift events."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, actually — this batch was running a newer catalyst lot. Neither of the earlier drift events used that lot. I knew that going in, but I didn't weight it heavily.",
          "evidence_explanation": "This demonstrates that a diagnostically important individuating feature was recognized but underweighted, consistent with the representativeness heuristic."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It looked enough like the earlier pattern that I was comfortable calling it drift without waiting on the fuller review.",
          "evidence_explanation": "This shows that similarity to the past prototype was treated as sufficient for diagnosis despite unresolved review."
        }
      ],
      "correction_or_counterevidence": "A plausible non-bias explanation is that experienced engineers often rely on pattern recognition under time pressure. However, the participant explicitly identified the new catalyst-lot difference and stated he did not weight it heavily, which is affirmative evidence of representativeness-based reasoning rather than solely resource-limited judgment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus evidence was supplied; this label is assigned from general cognitive-science knowledge and should not be treated as retrieval-grounded.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Status quo bias",
      "alternative_labels": [
        "Familiarity bias",
        "Ambiguity aversion",
        "Default bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Status quo bias is a preference for the current state of affairs, leading decision makers to favor maintaining an existing procedure over changing to a new option even when evidence favors change.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Restart mitigation decision",
      "decision_point_description": "Whether to accept the contractor-recommended automated high-pressure interlock trip or keep the existing manual response procedure for restart.",
      "affected_reasoning_operation": "Risk management / option evaluation under uncertainty",
      "bias_specific_mechanism": "The participant overweighted familiarity and current practice as a known quantity while underweighting the contractor's quantitative data showing a narrower relief-system margin for the new catalyst lot.",
      "manifestation_in_interview": "He acknowledged the margin data was real but favored the manual procedure because staff were not hands-on with the interlock and the existing system had not failed yet. He framed the choice as the known system winning over the new one.",
      "effect_on_reasoning_or_decision": "He recommended keeping the manual procedure for restart, so the automated high-pressure interlock was not added at that time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I recommended keeping the manual procedure for this restart. The interlock wasn't something our operators had hands-on familiarity with, and introducing something new felt like it carried its own risk profile that we hadn't lived with yet.",
          "evidence_explanation": "This shows preference for the existing procedure based on familiarity rather than a comparative risk assessment of the new evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Our manual process, whatever its limits, was a known quantity.",
          "evidence_explanation": "This explicitly frames the current state as favored despite acknowledged limits."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I gave more weight to the fact that the interlock was unproven here specifically, on our unit, with our people. The known system winning out over the new one felt like the safer bet.",
          "evidence_explanation": "This demonstrates overweighting the local status quo and treating familiarity as safety."
        }
      ],
      "correction_or_counterevidence": "A plausible non-bias explanation is that the manual procedure had a long run without failure, which is relevant operational experience. However, the participant's framing that the known system winning out felt safer despite the contractor's margin data indicates a status-quo preference rather than a purely quantitative risk comparison.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus evidence was supplied; this label is assigned from general cognitive-science knowledge and should not be treated as retrieval-grounded.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Halo effect",
      "alternative_labels": [
        "Authority bias",
        "Expert deference"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The halo effect is the tendency for a positive overall impression of a person in one domain to influence judgments about that person's specific judgments or recommendations in another domain.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "MOC meeting disagreement and closure",
      "decision_point_description": "Whether to close the MOC in line with the senior engineer's sensor-drift view or keep it open because the contractor flagged catalyst-lot kinetics as an unresolved gap.",
      "affected_reasoning_operation": "Evaluation of conflicting expert recommendations",
      "bias_specific_mechanism": "The participant accepted the senior engineer's sensor-drift assessment because of his long experience, original commissioning role, and excellent overall safety record, rather than because of new technical data. This global positive impression overrode the contractor's specific unresolved kinetics concern.",
      "manifestation_in_interview": "He stated that the senior engineer's experience carries weight and that his excellent safety record led him to trust the assessment even without new numbers behind it, while dismissing the contractor's written point as an outside read.",
      "effect_on_reasoning_or_decision": "He sided with the senior engineer and closed the MOC without the kinetics review; the restart proceeded without resolving the catalyst-lot question.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He's someone I've worked alongside for years, part of the original team that built this unit — that carries weight with me, knowing he's lived with this reactor longer than most people on-site.",
          "evidence_explanation": "This shows the participant using the senior engineer's experience and history as a generalized reason to trust his technical judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "his overall safety record here is excellent, so when he says something lines up with his experience, I tend to trust that assessment even without new numbers behind it.",
          "evidence_explanation": "This is strong evidence of the halo effect: an excellent overall safety record is treated as validating a specific technical conclusion in the absence of new data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The contractor's point was on paper, but it felt like an outside read compared to someone who's actually run this unit for fifteen years.",
          "evidence_explanation": "This shows the contractor's specific analysis was devalued based on source or perceived outsider status rather than its technical content."
        }
      ],
      "correction_or_counterevidence": "A non-bias explanation is that the senior engineer did have relevant unit-specific expertise. However, the participant explicitly cited the engineer's overall safety record and experience as a reason to trust the assessment without new numbers, which is the bias-specific mechanism rather than content-based evaluation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus evidence was supplied; this label is assigned from general cognitive-science knowledge and should not be treated as retrieval-grounded.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied; bias labels are grounded in general cognitive-science knowledge rather than retrieval.",
    "The analysis relies on a retrospective self-report interview, so it cannot independently verify objective decision behavior.",
    "Some statements reflect post-hoc reflection and counterfactual reasoning, which were not treated as primary evidence of bias."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Biased_5_Sonnet_off",
  "interview_id": "HE_Biased_5",
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
