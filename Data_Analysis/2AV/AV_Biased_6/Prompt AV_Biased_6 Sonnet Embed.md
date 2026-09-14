You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first analysis of a dispatcher CTA interview for cognitive biases affecting dispatch decisions and communications, using retrieved corpus material where applicable."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "hindsight bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "plan continuation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": ["anchoring effect", "expectation bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's existing beliefs, expectations, or plans.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-release weather monitoring and enroute evaluation of the amended forecast, model runs, and PIREP",
      "decision_point_description": "After the initial Lisbon/Porto release, the dispatcher had to decide how much weight to give to new information that conflicted with the existing fuel and alternate plan.",
      "affected_reasoning_operation": "Weighting and interpretation of updated forecast information against the existing plan",
      "bias_specific_mechanism": "The dispatcher used the already issued release as a reference point and preferentially credited later information consistent with it while discounting contradictory information as insufficient or non-leading.",
      "manifestation_in_interview": "The participant stated that later checks were about confirming the release figure rather than starting over, and he leaned on the model consistent with the previously briefed trend while downplaying the PIREP and slower-recovery model.",
      "effect_on_reasoning_or_decision": "This reduced the likelihood of a fundamental reassessment of the fuel or alternate plan, preserving the original Lisbon/Porto release even when new information suggested slower fog burn-off.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Once that release was built, honestly, that became my working number for the rest of the watch — the later checks I did were more about confirming that figure still held rather than starting over and asking whether a completely different fuel or alternate plan made more sense from scratch.",
          "evidence_explanation": "This explicitly describes a confirmatory mental frame: later information was used to verify the initial number rather than to reconsider the plan from scratch."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The model that lined up with the trend I'd already briefed felt more current and more consistent with what we'd been seeing on other flights that shift, so I leaned on that one. The PIREP was useful, but a single pilot report felt like one data point against a fuller model picture, so I passed the update to the crew framed around the improving trend, noting the other read existed but wasn't the lead story.",
          "evidence_explanation": "This shows selective weighting in favor of information consistent with the prior view and downweighting of conflicting evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered it, yeah. It just didn't feel like enough on its own to justify walking back guidance I'd already given the crew.",
          "evidence_explanation": "This indicates resistance to revising prior guidance, reinforcing that the existing plan was protected from the contradictory evidence."
        }
      ],
      "correction_or_counterevidence": "The participant did consider both model runs and the PIREP, and a single PIREP versus model guidance and shift experience could legitimately be given less weight in professional weather assessment. He did not completely ignore the contradiction; he noted it to the crew.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "found that the crew’s confirmation bias was supported by being able to visually identify cues that supported their mental model such as yellow markers on the taxiway which were perceived to be yellow runway markers. Similarly for flight Comair 5191 (2006) which took off from the incorrect runway in darkness and VMC conditions, the investigation found that the visual cues available to the crew induced a state of confirmation bias which led them to ignore other evidence, such as the aircraft instruments, that would contradict the aircraft’s position.",
          "mechanism_supported_by_source": "The source describes confirmation bias as relying on cues consistent with an established mental model and ignoring contradictory evidence.",
          "relevance_to_this_occurrence": "The dispatcher similarly favored the model consistent with his briefed trend and downplayed the contradictory PIREP, preserving the original release rather than reevaluating it."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "plan continuation bias",
      "alternative_labels": ["plan continuation error"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue with an original plan despite new information suggesting that a change may be warranted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Top-of-descent continue-versus-divert recommendation",
      "decision_point_description": "With visibility near minima and the Porto ground-power window closing, the dispatcher had to recommend whether to continue to Lisbon or divert.",
      "affected_reasoning_operation": "Risk assessment and selection between continuing with the planned destination and diverting to the alternate",
      "bias_specific_mechanism": "Commitment to the original Lisbon plan made diverting feel like abandoning a viable plan that had held up, reducing responsiveness to later cues favoring diversion.",
      "manifestation_in_interview": "The participant said diverting felt like abandoning the plan and that the numbers on paper still supported continuing, even though visibility was at minima and the Porto GPU window was closing.",
      "effect_on_reasoning_or_decision": "It contributed to a continue recommendation under conditions of real uncertainty and a closing alternate window.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The remaining fuel and time margin still looked workable, and the plan all along had been Lisbon with Porto as backup if things really fell apart. Diverting felt like abandoning a plan that had held up reasonably well to that point, and the numbers on paper still supported continuing. I recommended continue.",
          "evidence_explanation": "This directly reveals plan continuation reasoning: the original plan and subjective reluctance to abandon it are listed as reasons for continuing, not only the objective fuel margin."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Genuinely, moderately confident, not fully. There was real uncertainty in that visibility trend.",
          "evidence_explanation": "This shows the continue recommendation was made despite substantial unresolved uncertainty, strengthening the inference that commitment to the plan rather than clear evidence supported the recommendation."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged only moderate confidence and real uncertainty. Objective fuel and time margins were still positive, which could support a legitimate decision to continue; the near-minima visibility and closing GPU window are probabilistic risk factors rather than definitive no-go criteria.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The accident report concluded that while the flight crew were aware of the icing conditions, “their decision to continue with the original plan to depart was influenced by continuation bias, as they perceived the initial and sustained cues that supported their plan as more compelling than the later cues that suggested another course of action” (Transportation Safety Board of Canada, 2021, p. 184)",
          "mechanism_supported_by_source": "The source describes plan continuation bias as continuing with an original plan while treating cues supporting the plan as more compelling than later cues suggesting another course of action.",
          "relevance_to_this_occurrence": "The dispatcher similarly continued with the original Lisbon plan and framed diversion as abandoning a plan that had held up, despite later visibility and GPU-window cues supporting a divert case."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "hindsight bias",
      "alternative_labels": ["outcome bias", "creeping determinism"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency, after learning an outcome, to reconstruct or communicate one's prior judgment as more predictable, certain, or settled than it actually was.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-flight operations log write-up",
      "decision_point_description": "After the uneventful landing, the dispatcher wrote the operations log entry characterizing the flight and decision.",
      "affected_reasoning_operation": "Retrospective recall and communication of the decision's uncertainty",
      "bias_specific_mechanism": "The participant's written account minimized the uncertainty he had felt in the moment, producing a record that read as more settled than his actual judgment.",
      "manifestation_in_interview": "The participant wrote the log cleanly and later noticed it read more settled than the situation had felt at the time.",
      "effect_on_reasoning_or_decision": "The log entry communicated greater post-hoc certainty about the continue decision, potentially distorting the operational learning record.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I wrote it up fairly cleanly — noted that conditions supported continuing to Lisbon and that the fuel plan held throughout. Reading it back now, it reads a bit more settled than it actually felt in the moment.",
          "evidence_explanation": "This shows a shift between in-the-moment uncertainty and the retrospective written account, consistent with hindsight bias in the communication of prior judgment."
        }
      ],
      "correction_or_counterevidence": "The participant himself identifies the discrepancy when reading the log back, which is a post-hoc correction or debiasing observation. A concise operational log may also reflect professional conventions rather than a cognitive bias, so the evidence is suggestive rather than definitive.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage specifically supported hindsight bias; the label is used from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Attribute substitution",
      "alternative_labels": ["answering the easier question", "narrow framing"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Answering the crew's continue-versus-divert risk query",
      "supporting_interview_quote": "I answered mostly with the fuel numbers — we had healthy reserves, well above minimums, comfortable margin to hold if needed. That's a real and necessary part of the answer. Whether I fully separated out the visibility-and-GPU-window piece as its own question, distinct from just 'do we have gas,' I'm less sure about now.",
      "plausible_mechanism": "The dispatcher may have answered the easier fuel-sufficiency question instead of the broader visibility/GPU-window continue-or-divert risk question.",
      "why_not_identified": "The transcript shows the answer was incomplete and the participant is uncertain about question separation, but it does not clearly demonstrate an automatic substitution mechanism rather than ordinary partial/incomplete analysis of a complex query."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus text is partially garbled and covers only a limited set of bias labels.",
    "The interview relies on self-reported retrospective accounts, which may themselves be influenced by recall and impression management.",
    "Analyst did not have access to objective weather or fuel data, so some decisions could have been justified by operational evidence not fully detailed in the transcript."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "AV_Biased_6_Sonnet_on",
  "interview_id": "AV_Biased_6",
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
