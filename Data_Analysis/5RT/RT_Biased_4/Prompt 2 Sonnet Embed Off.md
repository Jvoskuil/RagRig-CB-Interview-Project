You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and there's no evaluation of your performance attached to it — I'm strictly interested in how you thought through the situation. Sound okay?

Participant: Yeah, that's fine. I figured this was coming after the milepost 214 write-up.

Interviewer: Right. Can you start by telling me your role and roughly how long you've been in it?

Participant: I'm the Division Superintendent for the subdivision, been in this seat about six years, twenty years total with the railroad, most of it on this same territory as a trainmaster and roadmaster before I moved up.

Interviewer: Good. So walk me through what first came to your attention that morning regarding milepost 214.

Participant: I got a call from our track inspector around 7 a.m. He'd run the ultrasonic test on the curve as part of the regular cycle, and it came back showing an internal transverse defect at 4 millimeters. That segment had a flaw logged three weeks earlier at 2 millimeters, so it had grown. He flagged it to me directly instead of just filing it because he wanted me aware before the day got going.

Interviewer: What was your objective once that report came in?

Participant: Keep the railroad safe, obviously, but also keep things moving. We had Q-119, one of our priority intermodal trains, scheduled through that same territory later that day, and there's a contractual on-time window — if we blow past two hours late, we eat a penalty. So I'm balancing the defect against keeping that train on schedule, and we've also got a cold snap coming that night, temperatures dropping about 25 degrees, which matters for rail integrity in continuous welded rail.

Interviewer: What happened right after the ultrasonic results came in?

Participant: I pulled the defect log for that curve. It's had small flaws before — bolted rail sections nearby had similar-sized readings that just sat there and never went anywhere. My first read was, this looks like the kind of thing we've seen. I told the inspector I wanted to keep it classified as monitor status, retest in two weeks, standard for a flaw in that size range.

Interviewer: Did the inspector push back on that?

Participant: He mentioned the growth was faster than what we'd typically seen — doubling in three weeks is quicker than the other cases in the log, which had been pretty flat over a couple months. I heard him on that, but doubling from 2 to 4 millimeters is still a small number in absolute terms. It didn't strike me as enough to change the call. We'd retest in two weeks like normal.

Interviewer: What information did you have in front of you at the moment you made that classification?

Participant: The two readings, the growth comparison the inspector gave me verbally, the historical log showing similar flaws stabilizing, and the fact the segment's rated for 60 miles an hour under our current track class. Nothing in front of me suggested immediate failure, just a number that had gone up.

Interviewer: How certain were you about the growth rate at that point?

Participant: Fairly certain — the inspector's numbers are reliable. I just didn't weigh the rate itself as the deciding factor. I was weighing it against "we've handled dozens of these," and none of them ever became anything.

Interviewer: Let's move to later that morning. What led into the next decision?

Participant: The inspector called back to make sure I'd registered that this stretch is continuous welded rail, laid about five years ago — different from most of the bolted-rail spots where we'd seen flaws stabilize before. He also mentioned tonnage on that curve is up about 15 percent year over year. I heard both points.

Interviewer: What made you confident this flaw would behave like the earlier ones?

Participant: I've personally been through this scenario more times than I can count. I can think of three specific cases off the top of my head — one back around 2019, another maybe two years ago — where we had a flaw that size, kept it under monitor status, and it never amounted to anything. That's twenty years of pattern on this same stretch. When you've watched the same thing play out that many times, you trust what you've seen.

Interviewer: Did the CWR construction or the tonnage increase change your thinking?

Participant: I registered it, but those three cases felt close enough to this one that it didn't move me off keeping the curve at track speed. We held off on any interim slow order and left it at the two-week retest.

Interviewer: What alternatives did you consider?

Participant: Putting in an interim slow order just through that curve, or restricting it only for certain train types until the retest. I thought about the interim order, but given how those other cases went, it felt like overkill for what looked like the same pattern I already knew.

Interviewer: Let's go to the afternoon, the call about Q-119. What led up to that?

Participant: As we got closer to Q-119's window, the chief dispatcher, the trainmaster, and the road foreman got on a short call with me to decide whether to run it through at track speed, put a temporary slow order on it, or reroute it around the adjoining subdivision. Customer service had already flagged that a reroute or hold risked blowing our two-hour window with the customer.

Interviewer: What was everyone's position going into that call?

Participant: The trainmaster had texted beforehand saying it was probably fine but he was a little nervous. The road foreman said he was leaning toward running it but wouldn't mind a slow order. So people had some reservations, nothing dramatic.

Interviewer: How did the group's view change over the course of the call?

Participant: It moved pretty quickly. Once we started talking, everybody's confidence built on everybody else's. By the end we'd landed on releasing Q-119 at full track speed, no slow order at all — more decisive than where any of us individually started. The whole call took maybe six minutes. Nobody raised an objection at the end.

Interviewer: Does that six-minute timeframe feel fast for that kind of call, looking back?

Participant: In the moment it felt efficient. We all had the same information, everyone seemed to be arriving at the same place, so there wasn't a sense we needed to slow down and hash it out further.

Interviewer: After Q-119 went through, what happened?

Participant: A following local crew radioed in they'd noticed an unusual sound at the wheel-rail interface passing that same stretch — no visible damage, nothing measurable, just an odd noise. That prompted us to get a debrief together before shift change.

Interviewer: Who was in that debrief?

Participant: Myself, the trainmaster, and the chief dispatcher. Our assistant engineer from track engineering asked to sit in — he wanted to raise concerns about how we'd classified the defect and handled the speed decision — but the meeting was scheduled tight, fifteen minutes before shift change, and he wasn't looped in beforehand, so he ended up not joining. Between the three of us, we also figured he'd come in and push on the CWR classification again like he had before, and nobody was especially eager to reopen that discussion this late in the shift.

Interviewer: What was discussed, or not discussed, in that debrief?

Participant: We went through the wheel-rail sound, agreed pretty quickly it was unrelated to the flaw — probably debris or a joint bar, nothing tied to milepost 214 specifically. We didn't get into re-examining the retest interval or walking back through the earlier classification call. It felt like we'd already covered that ground, so there wasn't much appetite to go back over it again.

Interviewer: Was there any dissent in the room?

Participant: No, everybody agreed it was a non-event. The minutes just note we concluded the process worked as intended.

Interviewer: What alternatives did you weigh in that closing meeting?

Participant: We could have pulled the assistant engineer in after the fact, or kicked it up to the chief engineer for an independent look at the classification. Given how it played out with the sound being unrelated, it didn't feel necessary to extend the meeting further.

Interviewer: How much time pressure did you feel across these four moments — the morning classification, the track-speed call, the release decision, and the debrief?

Participant: The debrief and the release call were the tightest, shift change and the two-hour window respectively. The morning classification had the least pressure — that was just me and the inspector working through the numbers.

Interviewer: If the retest interval had been one week instead of two, would anything about your classification have changed?

Participant: Possibly. A tighter retest window would have given us another data point sooner, which might have shifted how I read the growth rate. As it stood, two weeks felt like standard practice.

Interviewer: If the assistant engineer had been on the original conference call about Q-119, do you think the release decision would have gone differently?

Participant: Hard to say for certain. He tends to be more conservative about CWR segments specifically, so it's possible his voice in that room would have slowed us down or gotten someone to push back on going full speed.

Interviewer: Looking back, is there a point where you'd have wanted a dissenting voice to speak up more forcefully?

Participant: Probably the debrief. He was asking to be included for a reason, and we didn't make room for that given the schedule. Might've been worth five more minutes.

Interviewer: Last one — if this same flaw had shown up on a curve you hadn't worked before, do you think your approach would have been different?

Participant: Yeah, honestly, probably. On unfamiliar territory I'd likely lean more on the inspector's read of the growth rate itself rather than my own sense of how these things usually go, since I wouldn't have twenty years of watching that particular stretch to fall back on.

Interviewer: That's helpful, thank you. I appreciate you walking through it in this much detail.

Participant: No problem. It's useful to talk it through, honestly — you don't always get the chance to go back over the reasoning like this.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Biased_4",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Division Superintendent / Operations Manager",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Milepost 214 Rail Flaw and the Q-119 Release Decision",
    "scenario_summary_internal": "A division superintendent manages an evolving situation on a busy subdivision: an ultrasonic test flags a growing internal rail flaw on a curve near milepost 214 just as a winter cold front approaches and a high-priority intermodal train (Q-119) is due through the territory. Over several hours, the superintendent must interpret updated defect data, decide whether to impose a slow order, consult with a small operations group by conference call about releasing Q-119 at track speed, and finally run a post-incident debrief after a minor wheel-rail anomaly is reported downstream. The case is designed to elicit under-updating on new severity data, over-reliance on personal tenure with similar-looking past defects, a group discussion that pushes an initially moderate position toward a more extreme one, and a rapid, dissent-suppressing consensus in the closing meeting.",
    "occupational_realism": {
      "objective": "Maintain safe train operations across the subdivision while minimizing unnecessary delay to a contractual priority intermodal service during a developing rail-defect and weather situation.",
      "setting": "Division dispatch office and territory covering a 90-mile freight subdivision with a curved, high-tonnage segment near milepost 214, during a forecast overnight temperature drop of 25°F.",
      "constraints": [
        "Only one qualified track inspector available for re-testing before Q-119's scheduled window",
        "Contractual on-time performance penalty if Q-119 is delayed beyond a two-hour window",
        "Falling temperatures increase risk of rail contraction breaks in continuous welded rail (CWR)",
        "Limited extra-board crew availability for a potential reroute",
        "Communication only by phone/radio conference call, no in-person meeting possible before the decision window closes"
      ],
      "stakeholders": [
        "Division Superintendent (interviewee)",
        "Track Inspector",
        "Chief Dispatcher",
        "Trainmaster",
        "Road Foreman of Engines",
        "Assistant Engineer (track engineering)",
        "Intermodal customer service desk"
      ],
      "technical_terms_to_use": [
        "ultrasonic rail flaw detection",
        "continuous welded rail (CWR)",
        "slow order",
        "FRA Track Safety Standards / track class",
        "wheel-rail interface",
        "cold weather rail break risk",
        "extra board crew",
        "priority intermodal train",
        "on-time performance (OTP) metric",
        "defect growth rate"
      ],
      "technical_terms_to_avoid": [
        "conservatism bias",
        "experience bias",
        "group polarization",
        "groupthink",
        "anchoring",
        "cognitive bias",
        "heuristic",
        "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Morning ultrasonic test flags a 4mm internal transverse defect near milepost 214, previously logged at 2mm three weeks earlier",
          "Track is currently classified for 60 mph freight operation",
          "Historical defect log shows this curve has had similar small flaws in the past that stabilized without incident",
          "Overnight low forecast to drop 25°F by evening"
        ],
        "new_information_after_decision": [
          "Track inspector notes the growth rate (2mm to 4mm in three weeks) is faster than the prior flaws referenced in the log",
          "Superintendent classifies the defect as 'monitor, retest in two weeks' consistent with past practice for similarly sized flaws"
        ],
        "alternatives": [
          "Classify defect as 'monitor' per historical pattern and schedule routine retest",
          "Immediately impose a slow order pending same-day retest given the elevated growth rate",
          "Request emergency inspection support from an adjoining division"
        ],
        "intended_action": "Superintendent adopts the 'monitor' classification, treating the new growth-rate figure as within the range of previously seen, self-resolving flaws, without adjusting the assessment to reflect that this defect is growing faster than prior cases."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Track inspector raises concern that this segment is CWR laid five years ago, unlike the bolted-rail segments where most prior 'stabilized' flaws were found",
          "Current tonnage on the curve has increased roughly 15% year-over-year",
          "Superintendent has handled dozens of similar-looking flaw reports over a 20-year career on this subdivision",
          "No slow order currently in effect"
        ],
        "new_information_after_decision": [
          "Superintendent recalls three specific past cases from memory where a flaw of similar visual size 'turned out fine' and decides this case will behave the same way",
          "Decision is made to hold off on a slow order and keep the curve at track speed pending the two-week retest"
        ],
        "alternatives": [
          "Impose an interim slow order given the CWR construction and higher tonnage, distinct from the bolted-rail precedents being recalled",
          "Keep track speed based on the reasoning that similar past flaws resolved without incident",
          "Split the difference: reduce speed only for identified defect-adjacent train movements"
        ],
        "intended_action": "Superintendent generalizes directly from remembered past incidents without accounting for the material differences (CWR vs bolted rail, higher tonnage, cold-weather timing) and keeps the segment at track speed."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chief Dispatcher, Trainmaster, and Road Foreman join a short conference call to decide whether to release Q-119 through milepost 214 at track speed or hold it for a reroute",
          "Individually, each participant has expressed mild caution beforehand: Trainmaster texted 'probably fine but a little nervous,' Road Foreman said 'leaning toward yes but wouldn't mind a slow order'",
          "The customer service desk has flagged the two-hour delay penalty as a live financial consequence"
        ],
        "new_information_after_decision": [
          "During the call, participants reinforce each other's confidence, and the group lands on releasing Q-119 at full track speed with no slow order at all, more decisively than any individual had proposed beforehand",
          "The call ends in under six minutes with no dissent voiced"
        ],
        "alternatives": [
          "Release Q-119 at track speed as the group ultimately decided",
          "Release Q-119 with a temporary slow order through the milepost 214 curve only",
          "Hold Q-119 for a reroute via the adjoining subdivision"
        ],
        "intended_action": "The group discussion shifts the collective position toward a more extreme, more risk-tolerant decision (full track speed, no slow order) than the moderate caution any individual member expressed going into the call."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "After Q-119 passes, a following local crew reports a minor unusual wheel-rail sound near milepost 214 but no measurable damage",
          "Assistant Engineer, not on the earlier call, requests to join the debrief to raise concerns about the defect classification and speed decision",
          "Debrief meeting is scheduled for 15 minutes before shift change"
        ],
        "new_information_after_decision": [
          "The debrief group (Superintendent, Trainmaster, Chief Dispatcher) quickly agrees the wheel-rail sound was unrelated to the flaw and closes the meeting without inviting the Assistant Engineer or reviewing the retest timeline",
          "Minutes record unanimous agreement that 'the process worked as intended' with no dissenting view logged"
        ],
        "alternatives": [
          "Extend the debrief to include the Assistant Engineer's concerns and reassess the retest interval",
          "Quickly ratify the existing plan and close the meeting before shift change, as occurred",
          "Escalate to the chief engineer for an independent review of the defect classification"
        ],
        "intended_action": "The debrief group reaches rapid, unanimous closure, excludes a dissenting voice, and does not seriously entertain alternative explanations or a review of the classification decision, treating the quick consensus as confirmation that the process was sound."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what first came to your attention that morning regarding milepost 214.",
        "What was your overall objective for the shift once the flaw report came in?"
      ],
      "timeline_reconstruction": [
        "What happened right after the ultrasonic test results came in?",
        "What led up to the conference call about Q-119?",
        "What happened between the call ending and the debrief meeting?"
      ],
      "decision_point_probes": [
        "What information did you have in front of you when you classified the defect as 'monitor'?",
        "What made you confident that this flaw would behave like the ones you recalled from earlier in your career?",
        "How did the group's view change, if at all, over the course of the conference call?",
        "What was discussed, or not discussed, in the debrief before it closed?",
        "What alternatives did you weigh at each of these points, and why did you rule the others out?",
        "How much time pressure did you feel at each of these moments?",
        "How certain were you about the defect's growth rate at the time you made the classification?"
      ],
      "closing_hypotheticals": [
        "If the retest interval had been one week instead of two, would anything about your classification have changed?",
        "If the Assistant Engineer had been on the original conference call, do you think the release decision would have gone differently?",
        "Looking back, is there a point where you'd have wanted a dissenting voice to speak up more forcefully?",
        "If this same flaw had appeared on a different curve you hadn't worked before, would your approach have changed?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Conservatism Bias",
        "decision_point": 1,
        "mechanism": "Superintendent under-adjusts the risk classification despite new quantitative evidence (doubled defect size, faster growth rate than prior cases) indicating the situation has materially worsened, retaining the prior 'monitor' belief instead of updating toward a more urgent classification.",
        "affected_reasoning_operation": "Belief updating in response to new diagnostic evidence",
        "evidence_available_at_time": [
          "Ultrasonic test result showing growth from 2mm to 4mm in three weeks",
          "Track inspector's verbal flag that this growth rate exceeds prior logged cases"
        ],
        "required_textual_manifestation": "Interviewee acknowledges the new, larger/faster reading but explains the classification stayed at 'monitor, retest in two weeks' essentially unchanged from the prior visit, treating the new number as not warranting a shift in urgency.",
        "plausible_nonbias_interpretation": "A defensible judgment that 4mm is still within an established retest-rather-than-immediate-action threshold under track safety standards.",
        "strength": "subtle",
        "do_not_make_explicit": ["conservatism", "underweighting new evidence", "belief updating"]
      },
      {
        "instance_id": "eb_01",
        "bias": "Experience Bias",
        "decision_point": 2,
        "mechanism": "Superintendent draws on personally recalled past cases with superficial similarity (visual flaw size) while discounting material contextual differences (CWR vs bolted rail, higher tonnage, cold-weather timing) that distinguish the current case from those precedents.",
        "affected_reasoning_operation": "Analogical retrieval and generalization from personal case memory",
        "evidence_available_at_time": [
          "Track inspector's statement that this segment is CWR, unlike prior stabilized-flaw segments",
          "15% year-over-year tonnage increase on the curve",
          "Superintendent's 20 years of personal experience with similarly sized flaws"
        ],
        "required_textual_manifestation": "Interviewee explicitly references three specific remembered past cases as the basis for expecting this flaw to resolve similarly, without addressing why the CWR/tonnage/season differences might make the analogy weaker.",
        "plausible_nonbias_interpretation": "Reasonable use of pattern recognition built from decades of tenure on the same physical territory.",
        "strength": "subtle",
        "do_not_make_explicit": ["experience bias", "overgeneralization", "pattern matching"]
      },
      {
        "instance_id": "gp_01",
        "bias": "Group Polarization",
        "decision_point": 3,
        "mechanism": "Individually moderate, mildly cautious pre-call positions from the Trainmaster and Road Foreman shift, through group discussion, toward a more extreme collective position (full track speed, zero slow order) than any individual endorsed beforehand.",
        "affected_reasoning_operation": "Collective risk-position formation through group discussion",
        "evidence_available_at_time": [
          "Trainmaster's pre-call text expressing mild nervousness",
          "Road Foreman's pre-call statement leaning toward release but open to a slow order",
          "Financial penalty information from the customer service desk raised during the call"
        ],
        "required_textual_manifestation": "Interviewee describes the call's outcome as more decisively pro-release than the individual sentiments going in, and notes the call was short and ended without any dissenting voice moderating the final position.",
        "plausible_nonbias_interpretation": "The group may have simply been persuaded by a genuinely strong operational case for release that emerged during discussion.",
        "strength": "moderate",
        "do_not_make_explicit": ["group polarization", "risky shift", "social amplification"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 4,
        "mechanism": "The debrief group reaches fast, unanimous closure, actively excludes a stakeholder with a known dissenting concern, and records an illusion of unanimity without examining alternative explanations for the wheel-rail sound or revisiting the classification/speed decisions.",
        "affected_reasoning_operation": "Group consensus formation and alternative-generation under time pressure",
        "evidence_available_at_time": [
          "Assistant Engineer's request to join the debrief to raise concerns",
          "Local crew's report of an unusual wheel-rail sound",
          "15-minute time window before shift change"
        ],
        "required_textual_manifestation": "Interviewee describes the debrief closing quickly with unanimous agreement that 'the process worked,' the Assistant Engineer not being included, and no alternative explanations or reconsideration of the retest timeline being discussed.",
        "plausible_nonbias_interpretation": "A legitimately quick meeting because the wheel-rail sound was, in fact, minor and unrelated, and shift-change timing genuinely limited discussion.",
        "strength": "moderate",
        "do_not_make_explicit": ["groupthink", "illusion of unanimity", "self-censorship", "dissent suppression"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario was supplied for this generation (paired/base scenario ID is NONE)."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable: condition is 'biased', not 'counterfactual'; no counterfactual variable was instantiated for this generation despite AUTOSELECT being permitted by input, since the condition field governs generation mode.",
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly four decision points are present, each with at least two plausible alternatives.",
      "Each of the four manifest biases (Conservatism Bias, Experience Bias, Group Polarization, Groupthink) has exactly one planned instance, mapped to a distinct decision point.",
      "No bias name, definition, or psychological label appears in probes or narrative content.",
      "Each instance has a distinguishable evidence trail sufficient for independent identification without relying on outcome-based judgment.",
      "Consequences described (minor wheel-rail sound, no measurable damage) do not conclusively prove or disprove whether any decision was biased.",
      "Target word count of 1,350 (range 1,215-1,485) is achievable via four decision-point narrations plus probes without repetitive exposition.",
      "Technical vocabulary reflects rail operations terminology consistent with a Division Superintendent role.",
      "Group-level biases (Group Polarization, Groupthink) are each given moderate strength to ensure sufficient multi-actor dialogue evidence within the word budget."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Conservatism Bias", "occurrences": 1, "mechanism_constraint": "Under-adjustment of risk classification despite new quantitative severity/growth-rate evidence at decision point 1 only." },
      { "bias": "Experience Bias", "occurrences": 1, "mechanism_constraint": "Reliance on personally recalled superficially similar past cases while discounting material contextual differences at decision point 2 only." },
      { "bias": "Group Polarization", "occurrences": 1, "mechanism_constraint": "Collective shift to a more extreme position than individual pre-discussion positions during the decision point 3 conference call only." },
      { "bias": "Groupthink", "occurrences": 1, "mechanism_constraint": "Rapid unanimous closure with exclusion of a dissenting stakeholder and no alternative-explanation review at decision point 4 only." }
    ],
    "target_bias_names": ["Conservatism Bias", "Experience Bias", "Group Polarization", "Groupthink"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Conservatism Bias", "requested_occurrences": 1 },
      { "bias": "Experience Bias", "requested_occurrences": 1 },
      { "bias": "Group Polarization", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Conservatism Bias" },
      { "instance_id": "eb_01", "bias": "Experience Bias" },
      { "instance_id": "gp_01", "bias": "Group Polarization" },
      { "instance_id": "gt_01", "bias": "Groupthink" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Conservatism Bias", "decision_point": 1 },
      { "instance_id": "eb_01", "bias": "Experience Bias", "decision_point": 2 },
      { "instance_id": "gp_01", "bias": "Group Polarization", "decision_point": 3 },
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Conservatism Bias",
        "mechanism": "Retains prior 'monitor' classification despite new evidence (doubled defect size, faster growth rate) that should have triggered a more urgent reassessment.",
        "affected_reasoning_operation": "Belief updating on new diagnostic evidence",
        "evidence_source": "Ultrasonic test comparison (2mm to 4mm over three weeks) and inspector's growth-rate flag",
        "distinctiveness_requirement": "Must be tied specifically to the initial defect-severity classification act, not to any subsequent speed or release decision."
      },
      {
        "instance_id": "eb_01",
        "bias": "Experience Bias",
        "mechanism": "Generalizes from remembered visually-similar past flaws while ignoring stated contextual differences (CWR construction, higher tonnage, cold-weather timing).",
        "affected_reasoning_operation": "Analogical retrieval from personal case memory",
        "evidence_source": "Superintendent's cited personal recollections of three prior cases plus inspector's CWR/tonnage caveat",
        "distinctiveness_requirement": "Must be tied specifically to the track-speed-vs-slow-order decision based on personal case memory, distinct from the growth-rate evidence used in cb_01."
      },
      {
        "instance_id": "gp_01",
        "bias": "Group Polarization",
        "mechanism": "Group discussion moves the collective decision to a more extreme risk-tolerant position (full speed, no slow order) than any individual's stated pre-call position.",
        "affected_reasoning_operation": "Collective risk-position formation via group discussion",
        "evidence_source": "Pre-call individual statements (Trainmaster, Road Foreman) versus the call's final unanimous outcome",
        "distinctiveness_requirement": "Must show a measurable shift between individual pre-positions and the group's post-discussion position, not merely group agreement."
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Debrief group reaches fast unanimous closure, excludes a known dissenting stakeholder, and does not examine alternative explanations or revisit prior decisions.",
        "affected_reasoning_operation": "Group consensus formation and alternative-generation under time pressure",
        "evidence_source": "Assistant Engineer's exclusion, debrief meeting minutes recording unanimity, absence of alternative-explanation discussion",
        "distinctiveness_requirement": "Must show exclusion of dissent and absence of alternative consideration, distinct from gp_01's individual-to-group position shift."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Conservatism Bias", "strength": "subtle" },
      { "instance_id": "eb_01", "bias": "Experience Bias", "strength": "subtle" },
      { "instance_id": "gp_01", "bias": "Group Polarization", "strength": "moderate" },
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "RT_Biased_4",
    "domain_id": "RT",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One instance per named bias, each assigned to a distinct decision point (1:1 mapping across the four decision points) selected for mechanism fit: individual diagnostic under-updating (DP1), individual analogical over-reliance on tenure (DP2), multi-actor discussion dynamics (DP3), and multi-actor post-incident consensus dynamics (DP4). No bias shares a decision point, satisfying the spread and non-duplication rules; group-level biases were placed at the two decision points involving multiple stakeholders to match mechanism and narrative realism.",
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
        "segment_type": "objective_and_tradeoff_reasoning",
        "raw_interview_anchor": "Keep the railroad safe, obviously, but also keep things moving; Q-119's on-time window and the cold snap.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant frames competing safety, schedule, and weather considerations without a manifested target bias."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_classification_rationale",
        "raw_interview_anchor": "Similar small flaws that just sat there; my first read was, this looks like the kind of thing we've seen.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is the initial assessment based on historical cases, before the inspector's explicit comparison of the growth rate with prior cases. The generation specification documents a plausible non-bias interpretation for a monitor classification at this size."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_and_decision",
        "raw_interview_anchor": "Doubling in three weeks is quicker ... still a small number in absolute terms. It didn't strike me as enough to change the call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant recognizes the faster growth evidence but discounts it as insufficient to change the existing monitor classification, matching the hidden Conservatism Bias instance at decision point 1."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "evidence_interpretation",
        "raw_interview_anchor": "Nothing in front of me suggested immediate failure, just a number that had gone up.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "This explanation again minimizes the significance of the increase despite the known readings and growth comparison. It is evidence from the same hidden decision-point-1 occurrence, not a separate occurrence."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_weighting_explanation",
        "raw_interview_anchor": "I just didn't weigh the rate itself as the deciding factor. I was weighing it against 'we've handled dozens of these,' and none of them ever became anything.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant explicitly gives prior non-events greater weight than the reliable growth-rate evidence, further expressing the same under-updating instance."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "analogical_reasoning",
        "raw_interview_anchor": "Three specific cases ... where we had a flaw that size ... it never amounted to anything. That's twenty years of pattern.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "eb_01"
        ],
        "ground_truth_rationale": "The participant relies on specific personally recalled cases as the basis for expecting the present flaw to resolve similarly, despite the material context differences raised by the inspector."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "alternative_evaluation",
        "raw_interview_anchor": "Those three cases felt close enough ... We held off on any interim slow order ... it felt like overkill.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "eb_01"
        ],
        "ground_truth_rationale": "The participant rejects a slow order by relying on the recalled cases as sufficiently similar, continuing the same hidden decision-point-2 occurrence."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "group_decision_reasoning",
        "raw_interview_anchor": "Everybody's confidence built on everybody else's ... more decisive than where any of us individually started.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gp_01"
        ],
        "ground_truth_rationale": "The participant reports that group discussion shifted initially cautious positions toward the more extreme risk-tolerant decision to release at full speed, matching Group Polarization."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "consensus_interpretation",
        "raw_interview_anchor": "The whole call took maybe six minutes. Nobody raised an objection ... there wasn't a sense we needed to slow down and hash it out further.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gp_01"
        ],
        "ground_truth_rationale": "The short call and absence of voiced dissent are part of the same hidden group-polarization episode; they do not constitute a separate occurrence."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "stakeholder_inclusion_reasoning",
        "raw_interview_anchor": "The assistant engineer ... wanted to raise concerns ... he wasn't looped in beforehand ... nobody was especially eager to reopen that discussion.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The group excludes a known dissenting stakeholder in part to avoid reopening the disputed classification, matching part of the hidden Groupthink instance."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "debrief_evidence_interpretation",
        "raw_interview_anchor": "Agreed pretty quickly it was unrelated ... didn't get into re-examining the retest interval or walking back through the earlier classification call.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The group rapidly dismisses ambiguous evidence and avoids reviewing the earlier decision, matching part of the hidden Groupthink instance."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "consensus_recording",
        "raw_interview_anchor": "Everybody agreed it was a non-event. The minutes just note we concluded the process worked as intended.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The participant describes unanimous closure and a record that the process worked as intended without a dissenting view, part of the same hidden Groupthink instance."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "alternative_review_rationale",
        "raw_interview_anchor": "We could have pulled the assistant engineer in ... or kicked it up ... Given how it played out ... it didn't feel necessary.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "gt_01"
        ],
        "ground_truth_rationale": "The participant acknowledges independent review options but dismisses them based on the group's benign interpretation of the sound, continuing the same hidden debrief instance."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "retrospective_reflection",
        "raw_interview_anchor": "Probably the debrief. He was asking to be included for a reason ... Might've been worth five more minutes.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a retrospective recognition that dissent might have been useful, not a new biased decision or an additional hidden occurrence."
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
    "analysis_scope_note": "Conservative, mechanism-first CTA bias analysis restricted to transcript evidence. No retrieved corpus passages were supplied, so labeled biases rely on established cognitive-science knowledge and the absence of retrieval support is disclosed."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "group polarization",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "groupthink",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A heuristic in which judgments of frequency, probability, or likely future outcomes are shaped by the ease with which similar instances come to mind, rather than by a full analysis of current diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Milepost 214 defect classification and interim speed decision",
      "decision_point_description": "Classification of a 4 mm internal transverse defect as monitor status with a two-week retest and no interim slow order, after growth from 2 mm in three weeks and the inspector's later continuous welded rail and tonnage concerns.",
      "affected_reasoning_operation": "Risk assessment of rail defect progression and selection of track speed restriction",
      "bias_specific_mechanism": "The probability that the flaw would become a failure was judged primarily by the ease of recalling similar historical flaws that had stabilized, rather than by integrating the current growth rate, continuous welded rail construction, and increased tonnage as diagnostic evidence.",
      "manifestation_in_interview": "The participant repeatedly framed the decision through past cases he could recall: he said the flaw looked like the kind of thing they had seen before, explicitly weighed those recalled prior stable flaws over the growth rate, and later said he would have relied more on the inspector's growth-rate read on unfamiliar territory where he lacked those memories.",
      "effect_on_reasoning_or_decision": "The participant retained the flaw as monitor status, kept the curve at track speed, and left a two-week retest interval despite a faster growth rate and new CWR/tonnage information.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first read was, this looks like the kind of thing we've seen. I told the inspector I wanted to keep it classified as monitor status, retest in two weeks, standard for a flaw in that size range.",
          "evidence_explanation": "This shows the participant immediately matching the current defect to recalled prior cases and using that familiarity as the basis for the initial classification."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I just didn't weigh the rate itself as the deciding factor. I was weighing it against 'we've handled dozens of these,' and none of them ever became anything.",
          "evidence_explanation": "This explicitly states that the current diagnostic growth rate was outperformed by recollections of previous similar defects that had remained stable, which is the core availability-heuristic mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I registered it, but those three cases felt close enough to this one that it didn't move me off keeping the curve at track speed. We held off on any interim slow order and left it at the two-week retest.",
          "evidence_explanation": "This demonstrates that even after receiving CWR and tonnage information, the recall of three specific prior stable cases dominated the risk judgment and preserved the original decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "On unfamiliar territory I'd likely lean more on the inspector's read of the growth rate itself rather than my own sense of how these things usually go, since I wouldn't have twenty years of watching that particular stretch to fall back on.",
          "evidence_explanation": "This counterfactual admission links the biased reasoning directly to the availability of personal experience on this familiar territory rather than to a general diagnostic principle."
        }
      ],
      "correction_or_counterevidence": "The inspector pushed back that the growth rate was faster than prior cases and later highlighted continuous welded rail and a 15 percent tonnage increase. The participant acknowledged these points but did not revise the classification or slow-order decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; availability heuristic is used as an established cognitive-science label from general knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "group polarization",
      "alternative_labels": ["risky shift"],
      "taxonomy_status": "established_label",
      "bias_definition": "A group decision bias in which discussion among like-minded members strengthens the average pre-existing leaning and produces a more extreme group decision than the initial individual positions.",
      "attributed_to_speaker": "Q-119 conference call group, including the Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Q-119 track-speed release conference call",
      "decision_point_description": "Group decision whether to release Q-119 at full track speed, impose a temporary slow order, or reroute it around the adjoining subdivision.",
      "affected_reasoning_operation": "Group risk evaluation and consensus decision under uncertainty",
      "bias_specific_mechanism": "During a short discussion among individuals with similar initial leanings, mutual confirmation and the absence of explicit dissent increased confidence, causing the group to adopt a position more extreme than the initial individual attitudes.",
      "manifestation_in_interview": "The participant reported that the trainmaster and road foreman entered the call with reservations, but after discussion confidence built among group members. The result was a unanimous full-track-speed release with no slow order, more decisive than any individual's initial preference.",
      "effect_on_reasoning_or_decision": "The group shifted from individually cautious or ambivalent positions to a unanimous no-slow-order full-track-speed release, leaving individual reservations unrepresented in the final decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The trainmaster had texted beforehand saying it was probably fine but he was a little nervous. The road foreman said he was leaning toward running it but wouldn't mind a slow order. So people had some reservations, nothing dramatic.",
          "evidence_explanation": "This establishes that the pre-discussion positions were not as extreme as the eventual group decision; at least two members voiced or favored some caution."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Once we started talking, everybody's confidence built on everybody else's. By the end we'd landed on releasing Q-119 at full track speed, no slow order at all — more decisive than where any of us individually started. The whole call took maybe six minutes. Nobody raised an objection at the end.",
          "evidence_explanation": "This explicitly describes a group-induced confidence increase and a more extreme final decision than the initial individual positions, which is the defining pattern of group polarization."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We all had the same information, everyone seemed to be arriving at the same place, so there wasn't a sense we needed to slow down and hash it out further.",
          "evidence_explanation": "This illustrates how perceived agreement during the call suppressed further scrutiny and reinforced the emerging extreme consensus."
        }
      ],
      "correction_or_counterevidence": "No in-call correction or dissenting check occurred; the call ended with no objection. A later local crew report of an unusual wheel-rail sound prompted a debrief, but that did not reverse the release decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; group polarization is used as an established cognitive-science label from general knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "groupthink",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "bias_definition": "A group decision bias in which the desire for consensus and avoidance of dissent suppresses critical evaluation, leading to incomplete consideration of alternatives and potentially unfounded unanimity.",
      "attributed_to_speaker": "Milepost 214 debrief group, including the Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-Q-119 wheel-rail sound debrief",
      "decision_point_description": "Closing debrief decision to treat the reported wheel-rail sound as unrelated and not re-examine the defect classification or retest interval.",
      "affected_reasoning_operation": "Post-event interpretation, dissent management, and decision to re-examine prior classification",
      "bias_specific_mechanism": "The group prioritized consensus and avoided reopening a settled classification: it excluded a known potential dissenter, quickly assimilated an ambiguous noise report as unrelated, and treated the absence of dissent as evidence that the process worked.",
      "manifestation_in_interview": "The assistant engineer who asked to raise concerns was not included, and the participant reported that the group was not eager to reopen the CWR classification. The debrief then quickly agreed the wheel-rail sound was unrelated, did not re-examine the retest interval, and recorded that the process worked as intended.",
      "effect_on_reasoning_or_decision": "The debrief concluded the wheel-rail sound was a non-event, did not re-examine the retest interval or classification, and produced minutes stating that the process worked as intended.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our assistant engineer from track engineering asked to sit in — he wanted to raise concerns about how we'd classified the defect and handled the speed decision — but the meeting was scheduled tight, fifteen minutes before shift change, and he wasn't looped in beforehand, so he ended up not joining. Between the three of us, we also figured he'd come in and push on the CWR classification again like he had before, and nobody was especially eager to reopen that discussion this late in the shift.",
          "evidence_explanation": "This demonstrates exclusion of a potential dissenting voice and a preference for avoiding re-opening the prior classification, both characteristic of groupthink."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We went through the wheel-rail sound, agreed pretty quickly it was unrelated to the flaw — probably debris or a joint bar, nothing tied to milepost 214 specifically. We didn't get into re-examining the retest interval or walking back through the earlier classification call. It felt like we'd already covered that ground, so there wasn't much appetite to go back over it again.",
          "evidence_explanation": "This shows rapid consensus on an ambiguous cue and deliberate avoidance of re-examining the prior risk decision, reflecting collective rationalization and suppression of deeper review."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, everybody agreed it was a non-event. The minutes just note we concluded the process worked as intended.",
          "evidence_explanation": "This records an illusion of unanimity and a positive conclusion about the process, despite the concerns and ambiguous noise report that were not fully examined."
        }
      ],
      "correction_or_counterevidence": "Participant later reflected, \"He was asking to be included for a reason, and we didn't make room for that given the schedule. Might've been worth five more minutes.\" This retrospective acknowledgement did not change the debrief outcome.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; groupthink is used as an established cognitive-science label from general knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided, so corpus_evidence could not be supplied; named labels are grounded in established cognitive-science knowledge rather than retrieval.",
    "Analysis is limited to the reasoning as reported in the transcript; no independent outcome or condition information was used."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Biased_4_Sonnet_off",
  "interview_id": "RT_Biased_4",
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
