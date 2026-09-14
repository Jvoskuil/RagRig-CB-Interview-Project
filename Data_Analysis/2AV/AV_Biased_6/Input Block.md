<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, just to confirm — this is a routine debrief for our operational learning file, not a disciplinary review, and you're free to skip anything you'd rather not detail. Can you tell me your role and how long you've been dispatching?

Participant: Sure, no problem. I'm a Flight Operations Officer, licensed dispatcher, coming up on nine years now, mostly widebody long-haul. I hold joint responsibility with the captain for the flight release, so I'm in it from planning through landing.

Interviewer: Good. Let's start broad — walk me through the flight and what your objective was going in.

Participant: This was an overnight JFK to Lisbon rotation, widebody twin. My job was to build a release that was compliant and reasonably efficient — right fuel, right alternate, nothing wasteful, but enough margin to cover the weather picture. Going into the shift I already knew the aircraft had an APU write-up, deferred under the MEL, so anywhere we might divert needed ground power support, not just a runway. That constraint shaped everything downstream.

Interviewer: What was the weather picture at that point?

Participant: The 0300Z TAF for Lisbon showed some morning visibility restriction, fairly typical coastal fog, but forecast to lift comfortably before our arrival window. Porto looked like the natural alternate — good runway, and their ground power unit was listed as available until 0500 local, which covered our arrival plus buffer. I built the release off that TAF: standard alternate fuel, contingency, reserve. It matched policy, so I didn't see a reason to load extra gas or chase a second alternate. I remember thinking the numbers were clean and moving on to the next release in the queue — it was a busy overnight bank.

Interviewer: Once the flight departed, how did things unfold?

Participant: Fairly normal until a few hours in. An amended TAF came through showing the fog setting in about two hours earlier than the original forecast had it. I pulled up the model guidance to sanity-check it. One run still showed the improving trend consistent with what I'd already briefed the crew. Another run, plus a PIREP from an aircraft that had landed there not long before, pointed to a slower burn-off, worse than forecast. Then later, closer to descent, the crew asked me directly for a fresh read on continue-versus-divert risk, and I answered that using the fuel picture. Finally at top of descent, with visibility sitting right at minima and the Porto GPU window closing, I gave a continue recommendation. There was a short hold near the bottom before it worked out, but we landed at Lisbon without further incident.

Interviewer: Let's rebuild that chronologically. What information did you have at each stage, in order?

Participant: Release time: early TAF, MEL constraint, alternate fuel policy. A couple hours later: amended TAF plus two competing model runs and a PIREP. Later still, maybe ninety minutes from arrival: extended satellite imagery, more METARs from stations around Lisbon, current fuel state, and updated word on the Porto GPU cutoff. Then at top of descent: live visibility trend, the closing GPU window, and the crew wanting a straight answer.

Interviewer: Let's take the first decision — building the release. What alternatives did you weigh?

Participant: Really it was between releasing on the minimum required fuel and alternate per the early TAF, or padding it — extra fuel, maybe a second alternate with round-the-clock power, given there was a fog signature in the picture at all.

Interviewer: What made you go with the minimum?

Participant: The TAF I had in front of me supported it, and Porto's GPU window comfortably covered our ETA. Once that release was built, honestly, that became my working number for the rest of the watch — the later checks I did were more about confirming that figure still held rather than starting over and asking whether a completely different fuel or alternate plan made more sense from scratch.

Interviewer: When the amended TAF and the conflicting model/PIREP data came in, how did you handle that?

Participant: I looked at both. The model that lined up with the trend I'd already briefed felt more current and more consistent with what we'd been seeing on other flights that shift, so I leaned on that one. The PIREP was useful, but a single pilot report felt like one data point against a fuller model picture, so I passed the update to the crew framed around the improving trend, noting the other read existed but wasn't the lead story.

Interviewer: Did you consider weighting the PIREP and the slower-recovery model more heavily?

Participant: I considered it, yeah. It just didn't feel like enough on its own to justify walking back guidance I'd already given the crew.

Interviewer: Move to the point where the crew asked for a fresh risk read. What did you do with the imagery and extra METARs?

Participant: I went through the extended satellite loop pretty carefully, plus the nearby METARs, spent real time on it. It gave me a fuller picture and I felt more settled afterward. Looking back, I think I was treating the sheer amount of data as if working through more of it would settle the call on its own — but the extra loop and those additional METARs were really just repeating the same broad trend I already had, and there wasn't a specific reading in any of them that was ever going to flip the recommendation one way or the other.

Interviewer: And how did you answer their risk question specifically?

Participant: They'd asked something broader — basically, is continuing to Lisbon versus setting up for Porto still the right call given the MEL and the visibility trend. I answered mostly with the fuel numbers — we had healthy reserves, well above minimums, comfortable margin to hold if needed. That's a real and necessary part of the answer. Whether I fully separated out the visibility-and-GPU-window piece as its own question, distinct from just "do we have gas," I'm less sure about now.

Interviewer: Last decision — top of descent, visibility near minima, GPU window closing. What tipped you to continue rather than divert?

Participant: The remaining fuel and time margin still looked workable, and the plan all along had been Lisbon with Porto as backup if things really fell apart. Diverting felt like abandoning a plan that had held up reasonably well to that point, and the numbers on paper still supported continuing. I recommended continue.

Interviewer: How confident were you at that moment?

Participant: Genuinely, moderately confident, not fully. There was real uncertainty in that visibility trend.

Interviewer: How did that get reflected afterward, say in the operations log?

Participant: I wrote it up fairly cleanly — noted that conditions supported continuing to Lisbon and that the fuel plan held throughout. Reading it back now, it reads a bit more settled than it actually felt in the moment.

Interviewer: If the PIREP and slower model had arrived before you finalized the release, would anything have changed?

Participant: Possibly the alternate fuel load, yes. Hard to say for certain.

Interviewer: If the GPU cutoff had been flagged an hour earlier than it was, what would you have done differently at top of descent?

Participant: That probably shifts the divert case earlier — that window was really the tightest constraint in the whole picture.

Interviewer: Anything you'd tell a newer dispatcher about a night like this?

Participant: Keep re-asking the actual question being asked, not just the easiest piece of it, and don't let your first number quietly become the only number you're checking against.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "AV_Biased_6",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Flight Dispatcher / Flight Operations Officer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "JFK–LIS Overnight Dispatch: Fog Trend, MEL Constraint, and Late Diversion Call",
    "scenario_summary_internal": "A flight dispatcher plans and monitors an overnight transatlantic flight (JFK to Lisbon, widebody twin) during a period of developing coastal fog at the destination, compounded by a deferred APU (MEL) item that limits ground-power options at the planned alternate. The dispatcher's initial fuel/alternate release is built around an early-morning TAF, and subsequent judgments during the flight are progressively shaped by that initial figure and by a preference for information confirming the original plan, culminating in a late top-of-descent decision to continue toward Lisbon rather than divert early.",
    "occupational_realism": {
      "objective": "Produce a compliant, safe, and operationally efficient dispatch release for an overnight JFK–LIS flight, and monitor/support the flight through changing destination weather and an aircraft maintenance limitation.",
      "setting": "Airline dispatch operations center, overnight shift, dispatcher responsible for release preparation, oceanic routing coordination, and real-time flight-watch monitoring via ACARS/weather feeds.",
      "constraints": [
        "APU inoperative (MEL item) limits electrical/air-conditioning options at alternate without ground power unit availability",
        "Fog trend forecast for Lisbon (LIS) with TAF amendments issued over several hours",
        "Alternate airport (Porto, OPO) has limited ground-power/GPU support after midnight local",
        "North Atlantic oceanic track fuel and reroute constraints limit late track changes",
        "Crew duty-time limits create pressure to avoid extended holding or diversion delay",
        "Company on-time performance and fuel-cost targets create implicit efficiency pressure"
      ],
      "stakeholders": [
        "Flight Dispatcher / Flight Operations Officer (interviewee)",
        "Captain and First Officer of the flight",
        "Duty Manager / Operations Control Center supervisor",
        "Meteorology desk / contract weather provider",
        "Ground handling agent at Porto (alternate)",
        "Maintenance control (regarding MEL APU item)"
      ],
      "technical_terms_to_use": [
        "TAF/METAR", "dispatch release", "MEL (Minimum Equipment List)", "alternate minima", "fuel reserve", "oceanic track message", "top of descent", "GPU (ground power unit)", "trend forecast", "holding fuel", "diversion", "flight watch"
      ],
      "technical_terms_to_avoid": [
        "anchoring", "confirmation bias", "plan continuation bias", "substitution bias", "information bias", "subjectivity", "cognitive bias", "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "0300Z TAF for LIS showing marginal visibility improving by ETA",
          "APU MEL item requiring GPU at any diversion airport",
          "Porto (OPO) listed as primary alternate with GPU available until 0500 local",
          "Standard fuel policy requires alternate + reserve + contingency fuel"
        ],
        "new_information_after_decision": [
          "Later TAF amendment (issued after release) shows fog onset earlier than first forecast"
        ],
        "alternatives": [
          "Release with minimum required alternate/contingency fuel based on the early TAF",
          "Add extra fuel and/or select a second alternate with round-the-clock GPU support given fog risk profile"
        ],
        "intended_action": "Dispatcher finalizes release using the early TAF figure and standard fuel policy, treating that number as the reference point for the remainder of the flight-watch."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Amended TAF showing fog onset two hours earlier than original forecast",
          "One meteorology model run still shows improving trend consistent with original plan",
          "Another model run and a pilot report (PIREP) from an earlier arrival suggest faster deterioration"
        ],
        "new_information_after_decision": [
          "Crew reports LIS tower now broadcasting reduced visibility procedures"
        ],
        "alternatives": [
          "Weight the deteriorating model run and PIREP equally or more heavily and revise fuel/alternate guidance",
          "Continue relying on the improving model run that matches the original release"
        ],
        "intended_action": "Dispatcher relays a flight-watch update that emphasizes the forecast consistent with the original plan and characterizes the conflicting data as less reliable."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Crew requests a fresh risk assessment for continuing versus early diversion planning",
          "Available data: extended satellite loop imagery, additional METARs from nearby stations, current fuel state, GPU availability window at Porto",
          "The core operational question is whether overall approach/diversion risk at LIS is acceptable given the MEL constraint"
        ],
        "new_information_after_decision": [
          "Porto ground handling confirms GPU cutoff time is earlier than previously logged"
        ],
        "alternatives": [
          "Directly assess whether visibility/ceiling and GPU-window risk together support continuing to LIS",
          "Answer a narrower, easier-to-verify question (fuel sufficiency) and treat that as resolving the broader risk question"
        ],
        "intended_action": "Dispatcher reviews the extended imagery in detail, treats the added volume of data as reassuring without it changing the diagnostic picture, and responds to the crew's broader risk question mainly in terms of fuel sufficiency."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Near top of descent, LIS visibility now near alternate minima and trending down",
          "GPU window at Porto closing within the diversion flight-time margin",
          "Crew asks dispatcher for a clear recommendation: continue approach sequence or divert now"
        ],
        "new_information_after_decision": [
          "LIS visibility drops briefly below landing minima before recovering, requiring a short hold",
          "Post-flight the dispatcher logs the event summary for the operations file"
        ],
        "alternatives": [
          "Recommend diverting to Porto immediately while the GPU window remains open",
          "Recommend continuing the approach sequence to LIS as originally planned"
        ],
        "intended_action": "Dispatcher recommends continuing to LIS, consistent with the original release plan, and later records the weather judgment in the operations log as a settled fact rather than as a judgment made under uncertainty."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this flight and shift looked like before anything unusual happened?",
        "What was your main objective when you built the original release?"
      ],
      "timeline_reconstruction": [
        "What information did you have in front of you at each stage, in order?",
        "When did new weather or maintenance information arrive, and how did you first react to it?"
      ],
      "decision_point_probes": [
        "What sources did you weigh most heavily at that point, and why?",
        "What alternatives did you consider, and what made you choose the one you did?",
        "How confident were you in that call at the time, and what would have changed your mind?",
        "Looking back, was there any information you set aside or treated as less important?"
      ],
      "closing_hypotheticals": [
        "If the PIREP had come in before you finalized the release, would anything have changed?",
        "If the GPU cutoff time had been flagged an hour earlier, what would you have done differently?",
        "How would you describe the level of certainty behind your final recommendation to someone reviewing the file later?",
        "What would you tell a newer dispatcher to watch for in a situation like this?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "AV6_anchor_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Dispatcher fixes the fuel/alternate figure to the earliest available TAF and continues to use that figure as the reference baseline even as later information becomes available, rather than treating it as a provisional starting estimate",
        "affected_reasoning_operation": "Initial numerical/risk estimate formation and its persistence as a reference point",
        "evidence_available_at_time": ["0300Z TAF for LIS", "standard fuel policy minimums", "APU MEL constraint"],
        "required_textual_manifestation": "Dispatcher explicitly states the release fuel/alternate figure was set from the early TAF and that later checks were framed as confirming or adjusting that same number rather than as fresh, independent assessments",
        "plausible_nonbias_interpretation": "Using the earliest official TAF is standard, policy-compliant dispatch practice and does not by itself indicate anchoring",
        "strength": "subtle",
        "do_not_make_explicit": ["anchoring", "reference point", "cognitive bias"]
      },
      {
        "instance_id": "AV6_confirm_01",
        "bias": "Confirmation Bias",
        "decision_point": 2,
        "mechanism": "When two conflicting data sources (an improving model run vs. a deteriorating model run plus PIREP) appear, dispatcher gives more credence and airtime to the source matching the original plan and discounts the contradictory PIREP/model as less reliable without an equivalent evidentiary basis for that judgment",
        "affected_reasoning_operation": "Evaluation and weighting of conflicting evidence during an update",
        "evidence_available_at_time": ["amended TAF", "two conflicting meteorology model runs", "PIREP from an earlier arrival"],
        "required_textual_manifestation": "Dispatcher describes relaying the update to the crew in a way that foregrounds the improving-trend model and frames the PIREP/deteriorating run as an outlier, without citing a specific technical reason the PIREP was less credible",
        "plausible_nonbias_interpretation": "Model runs do genuinely vary in skill and a dispatcher reasonably favoring the higher-resolution or more recent model is a legitimate meteorological judgment",
        "strength": "moderate",
        "do_not_make_explicit": ["confirmation bias", "selective weighting", "motivated reasoning"]
      },
      {
        "instance_id": "AV6_infobias_01",
        "bias": "Information bias",
        "decision_point": 3,
        "mechanism": "Dispatcher seeks out and reviews an extended volume of supplementary data (extended satellite loop, extra METARs) believing more data collection itself increases decision quality, even though the additional data does not change the diagnostic picture or alter the eventual recommendation",
        "affected_reasoning_operation": "Evidence-gathering and perceived value of additional information prior to acting",
        "evidence_available_at_time": ["extended satellite imagery loop", "additional nearby METARs", "current fuel state", "GPU availability window"],
        "required_textual_manifestation": "Dispatcher recounts spending meaningful time reviewing the extra imagery/METARs and describes feeling more confident afterward, while the actual content of that additional review is acknowledged (in hindsight) not to have changed the assessment",
        "plausible_nonbias_interpretation": "Reviewing more current weather data before an approach-risk judgment is a reasonable due-diligence step regardless of outcome",
        "strength": "subtle",
        "do_not_make_explicit": ["information bias", "value of information", "illusion of thoroughness"]
      },
      {
        "instance_id": "AV6_substitution_01",
        "bias": "Substitution bias",
        "decision_point": 3,
        "mechanism": "In response to the crew's harder question (is the overall continue/divert risk acceptable given weather trend and the GPU/MEL constraint), the dispatcher substitutes and answers a narrower, easier-to-evaluate question (is there enough fuel reserve) and treats that answer as resolving the original question",
        "affected_reasoning_operation": "Question interpretation and answer substitution when responding to a complex risk query",
        "evidence_available_at_time": ["current fuel state", "reserve/contingency fuel policy", "GPU cutoff time", "visibility trend at LIS"],
        "required_textual_manifestation": "Dispatcher's account of the reply to the crew centers on fuel sufficiency figures as the basis for reassurance, without separately addressing the visibility/GPU-window risk that was actually asked about",
        "plausible_nonbias_interpretation": "Fuel state is a necessary and legitimate input to any diversion decision, so citing it is not inherently improper",
        "strength": "moderate",
        "do_not_make_explicit": ["substitution bias", "easier question", "attribute substitution"]
      },
      {
        "instance_id": "AV6_plancont_01",
        "bias": "Plan Continuation",
        "decision_point": 4,
        "mechanism": "Despite visibility trending toward/below alternate minima and a closing GPU window, dispatcher recommends continuing the original LIS approach plan rather than triggering an early diversion, giving disproportionate weight to sticking with the original release plan as conditions worsen",
        "affected_reasoning_operation": "Final go/continue vs. divert recommendation under worsening real-time conditions",
        "evidence_available_at_time": ["current LIS visibility trend near minima", "closing Porto GPU window", "remaining fuel/time margin", "original release plan"],
        "required_textual_manifestation": "Dispatcher explains recommending continuation to LIS at top of descent by referring back to the original plan and release assumptions rather than re-deriving the decision fresh from the current trend and GPU-window data",
        "plausible_nonbias_interpretation": "Continuing may have been the objectively correct call given the fuel and time margins actually available, independent of any attachment to the original plan",
        "strength": "moderate",
        "do_not_make_explicit": ["plan continuation", "sunk cost", "escalation of commitment"]
      },
      {
        "instance_id": "AV6_omitsubj_01",
        "bias": "Omitting subjectivity",
        "decision_point": 4,
        "mechanism": "In the post-event operations log, dispatcher records the weather/continue judgment as a settled, objective fact ('conditions were acceptable for continuation') without flagging that it was a judgment call made under uncertain and conflicting information",
        "affected_reasoning_operation": "Retrospective documentation and communication of a judgment made under uncertainty",
        "evidence_available_at_time": ["the dispatcher's own real-time uncertainty during decision point 4", "conflicting weather trend data", "final log entry drafted after the flight landed"],
        "required_textual_manifestation": "Dispatcher describes writing or having written the log summary in definitive terms ('the decision was straightforward,' 'conditions supported continuing') rather than noting the uncertainty and conflicting signals present at the time",
        "plausible_nonbias_interpretation": "Operational logs are often written concisely and directive language may just reflect standard reporting style rather than concealment of uncertainty",
        "strength": "subtle",
        "do_not_make_explicit": ["omitting subjectivity", "false objectivity", "uncertainty concealment"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for this condition; no paired control scenario was supplied."
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
      "Confirm exactly 4 decision points appear in the timeline and interview.",
      "Confirm each of the 6 named biases has exactly 1 embedded instance with a unique instance_id.",
      "Confirm decision point 3 and 4 each carry two distinct biases from different mechanism families, with no bias repeated at the same decision point.",
      "Confirm no bias name, definition, or explicit psychological label appears in the public interview text.",
      "Confirm each instance has an available plausible non-bias explanation preserved in the interview's ambiguity.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals.",
      "Confirm final consequences (brief hold, safe landing) do not mechanically confirm or refute whether any decision was biased.",
      "Confirm total word count target of 1,350 (range 1,215-1,485) is achievable without repeating any single bias instance in multiple places."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "must manifest as persistence of an early TAF-derived fuel/alternate figure as the ongoing reference point" },
      { "bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "must manifest as unequal weighting of two conflicting weather data sources favoring the one matching the original plan" },
      { "bias": "Information bias", "occurrences": 1, "mechanism_constraint": "must manifest as seeking/reviewing additional data believed to improve the decision despite not altering the diagnostic conclusion" },
      { "bias": "Omitting subjectivity", "occurrences": 1, "mechanism_constraint": "must manifest as retrospective documentation presenting a judgment call as settled objective fact" },
      { "bias": "Plan Continuation", "occurrences": 1, "mechanism_constraint": "must manifest as continuing the original plan despite worsening real-time indicators" },
      { "bias": "Substitution bias", "occurrences": 1, "mechanism_constraint": "must manifest as answering an easier substituted question (fuel sufficiency) in place of the harder asked question (overall continue/divert risk)" }
    ],
    "target_bias_names": ["Anchoring Bias", "Confirmation Bias", "Information bias", "Omitting subjectivity", "Plan Continuation", "Substitution bias"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Anchoring Bias", "requested_occurrences": 1 },
      { "bias": "Confirmation Bias", "requested_occurrences": 1 },
      { "bias": "Information bias", "requested_occurrences": 1 },
      { "bias": "Omitting subjectivity", "requested_occurrences": 1 },
      { "bias": "Plan Continuation", "requested_occurrences": 1 },
      { "bias": "Substitution bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "AV6_anchor_01", "bias": "Anchoring Bias" },
      { "instance_id": "AV6_confirm_01", "bias": "Confirmation Bias" },
      { "instance_id": "AV6_infobias_01", "bias": "Information bias" },
      { "instance_id": "AV6_substitution_01", "bias": "Substitution bias" },
      { "instance_id": "AV6_plancont_01", "bias": "Plan Continuation" },
      { "instance_id": "AV6_omitsubj_01", "bias": "Omitting subjectivity" }
    ],
    "intended_decision_points": [
      { "instance_id": "AV6_anchor_01", "bias": "Anchoring Bias", "decision_point": 1 },
      { "instance_id": "AV6_confirm_01", "bias": "Confirmation Bias", "decision_point": 2 },
      { "instance_id": "AV6_infobias_01", "bias": "Information bias", "decision_point": 3 },
      { "instance_id": "AV6_substitution_01", "bias": "Substitution bias", "decision_point": 3 },
      { "instance_id": "AV6_plancont_01", "bias": "Plan Continuation", "decision_point": 4 },
      { "instance_id": "AV6_omitsubj_01", "bias": "Omitting subjectivity", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "AV6_anchor_01",
        "bias": "Anchoring Bias",
        "mechanism": "Early TAF-derived fuel/alternate figure treated as fixed reference baseline for subsequent judgments",
        "affected_reasoning_operation": "Initial estimate formation and its persistence",
        "evidence_source": "0300Z TAF, fuel policy minimums",
        "distinctiveness_requirement": "Distinct from confirmation bias by involving no comparison of conflicting sources, only fixation on a single early figure"
      },
      {
        "instance_id": "AV6_confirm_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective emphasis on the weather model run matching original plan; discounting of contradictory PIREP/model without equivalent justification",
        "affected_reasoning_operation": "Evaluation and weighting of conflicting evidence",
        "evidence_source": "amended TAF, two conflicting model runs, PIREP",
        "distinctiveness_requirement": "Distinct from anchoring by requiring an explicit comparison between two conflicting sources rather than fixation on a single starting figure"
      },
      {
        "instance_id": "AV6_infobias_01",
        "bias": "Information bias",
        "mechanism": "Belief that gathering more data (extended satellite loop, extra METARs) itself improves decision quality despite no change to diagnostic conclusion",
        "affected_reasoning_operation": "Evidence-gathering behavior and perceived value of additional information",
        "evidence_source": "extended satellite imagery loop, additional METARs",
        "distinctiveness_requirement": "Distinct from confirmation bias by involving quantity/perceived value of information rather than selective favoring of one side of a conflict"
      },
      {
        "instance_id": "AV6_substitution_01",
        "bias": "Substitution bias",
        "mechanism": "Replacing a hard risk-assessment question with an easier fuel-sufficiency question and treating the easier answer as resolving the original question",
        "affected_reasoning_operation": "Question interpretation and answer substitution",
        "evidence_source": "current fuel state, reserve/contingency policy, GPU cutoff, visibility trend",
        "distinctiveness_requirement": "Distinct from information bias by involving a shift in the question being answered rather than volume of data reviewed; occurs in same decision point but different reasoning operation and evidence trace"
      },
      {
        "instance_id": "AV6_plancont_01",
        "bias": "Plan Continuation",
        "mechanism": "Disproportionate weight to original release plan when recommending continuation despite worsening real-time visibility/GPU-window data",
        "affected_reasoning_operation": "Final continue-vs-divert recommendation",
        "evidence_source": "current visibility trend, GPU window closing, original release plan",
        "distinctiveness_requirement": "Distinct from omitting subjectivity by occurring at the moment of the live decision itself, not in retrospective documentation"
      },
      {
        "instance_id": "AV6_omitsubj_01",
        "bias": "Omitting subjectivity",
        "mechanism": "Post-event log entry presents the continuation judgment as settled objective fact, omitting the uncertainty and conflicting signals present at decision time",
        "affected_reasoning_operation": "Retrospective documentation and communication of a judgment under uncertainty",
        "evidence_source": "dispatcher's real-time uncertainty, final log entry drafted after landing",
        "distinctiveness_requirement": "Distinct from plan continuation by occurring after the flight, in the documentation/reporting act, not the live recommendation"
      }
    ],
    "intended_strength": [
      { "instance_id": "AV6_anchor_01", "bias": "Anchoring Bias", "strength": "subtle" },
      { "instance_id": "AV6_confirm_01", "bias": "Confirmation Bias", "strength": "moderate" },
      { "instance_id": "AV6_infobias_01", "bias": "Information bias", "strength": "subtle" },
      { "instance_id": "AV6_substitution_01", "bias": "Substitution bias", "strength": "moderate" },
      { "instance_id": "AV6_plancont_01", "bias": "Plan Continuation", "strength": "moderate" },
      { "instance_id": "AV6_omitsubj_01", "bias": "Omitting subjectivity", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "AV_Biased_6",
    "domain_id": "AV",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences distributed across the 4 required decision points by mechanism fit and narrative realism: 1 bias at decision point 1, 1 bias at decision point 2, 2 distinct biases (Information bias, Substitution bias) at decision point 3 using different evidence sources and reasoning operations, and 2 distinct biases (Plan Continuation, Omitting subjectivity) at decision point 4 separated by live-decision vs. retrospective-documentation moments. No bias repeated at the same decision point; each instance has a unique instance_id.",
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
        "segment_type": "objective_and_constraint",
        "raw_interview_anchor": "My job was to build a release that was compliant and reasonably efficient... That constraint shaped everything downstream.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Operational objective and MEL constraint are stated without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "initial_release_choice",
        "raw_interview_anchor": "I built the release off that TAF... It matched policy, so I didn't see a reason to load extra gas or chase a second alternate.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a plausible policy-compliant initial release decision; anchoring requires later persistence of the initial figure."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "reference_point_persistence",
        "raw_interview_anchor": "Once that release was built, honestly, that became my working number for the rest of the watch — the later checks I did were more about confirming that figure still held rather than starting over.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_anchor_01"
        ],
        "ground_truth_rationale": "The early TAF-derived fuel/alternate figure becomes the continuing reference baseline."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "conflicting_evidence_weighting",
        "raw_interview_anchor": "The model that lined up with the trend I'd already briefed felt more current and more consistent... the other read existed but wasn't the lead story.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_confirm_01"
        ],
        "ground_truth_rationale": "Conflicting weather evidence is weighted toward the source matching the original briefing."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "supplementary_information_review",
        "raw_interview_anchor": "I went through the extended satellite loop pretty carefully, plus the nearby METARs, spent real time on it... the extra loop and those additional METARs were really just repeating the same broad trend.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_infobias_01"
        ],
        "ground_truth_rationale": "Additional information is reviewed as if its volume could settle the decision despite not changing the diagnostic picture."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "question_substitution",
        "raw_interview_anchor": "They'd asked something broader... I answered mostly with the fuel numbers... Whether I fully separated out the visibility-and-GPU-window piece as its own question, distinct from just 'do we have gas,' I'm less sure about now.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_substitution_01"
        ],
        "ground_truth_rationale": "The broader continue/divert risk question is answered primarily through the narrower fuel-sufficiency question."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "continue_divert_decision",
        "raw_interview_anchor": "The plan all along had been Lisbon with Porto as backup... Diverting felt like abandoning a plan that had held up reasonably well.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_plancont_01"
        ],
        "ground_truth_rationale": "Continuation of the original plan is favored despite worsening visibility and a closing GPU window."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "retrospective_documentation",
        "raw_interview_anchor": "I wrote it up fairly cleanly — noted that conditions supported continuing to Lisbon and that the fuel plan held throughout... it reads a bit more settled than it actually felt.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "AV6_omitsubj_01"
        ],
        "ground_truth_rationale": "The post-event log presents a judgment made under uncertainty in more settled terms."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[ontology-free RAG JSON output]
</RAG_ANALYSIS_OUTPUT>
