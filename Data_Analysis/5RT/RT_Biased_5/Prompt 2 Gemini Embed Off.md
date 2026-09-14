You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time. Before we start, I want to confirm you're okay with me recording this for internal process-improvement purposes, and that we can talk candidly about a project that didn't go entirely to plan.

Participant: Sure, that's fine. This one's still fresh for me anyway.

Interviewer: Can you describe your role and what the project was meant to accomplish?

Participant: I'm the capital projects manager for a corridor interlocking replacement — we were swapping out an aging interlocking and signal system on one of our busiest commuter segments, integrating it with our PTC interface. Federal grant money covered a good chunk of it, which meant a fixed obligation deadline. Miss it, and we risk losing part of the funding.

Interviewer: What made this project different from others you'd run?

Participant: The combination, really. Live revenue service running through the work zone, so we only had certain possession windows at night and weekends. A fixed-price design-build contract, so change orders were painful. And a hard federal clock ticking the whole time.

Interviewer: Walk me through what happened, start to finish.

Participant: We kicked off with a baseline schedule and budget. Then during early design we hit a scope question around underground utilities — old conduit, some of it undocumented. We made a call there and moved forward. Mid-construction, that came back to bite us: crews hit an unmapped high-voltage duct and we had a safety stand-down for a couple weeks. Contractor followed that up with a big risk report on cost and schedule impact. Then near the end, we had to decide how to handle systems integration testing with the deadline bearing down on us. We got through commissioning, the system passed, and we hit the funding deadline. But it was tighter than I'd like.

Interviewer: Let's go back to that baseline. What information did you have when you set the schedule?

Participant: The contractor's proposal assumed pretty efficient crew productivity — their best-case numbers. We also had data from a couple of peer agencies that had done similar interlocking swaps, and those ran 28 to 34 months typically. Leadership wanted to show the board real progress against the grant, so there was pressure to commit to something aggressive.

Interviewer: How did you weigh the contractor's numbers against those peer projects?

Participant: Honestly, I leaned on the contractor's proposal more. The peer projects weren't identical setups — different signal vendors, different corridor configurations — so I didn't think the comparison held up perfectly. We went with 24 months. I figured our team was sharper on execution than what those other durations reflected.

Interviewer: Did you revisit that historical range later, once things started slipping?

Participant: Yeah, once productivity started trailing plan, it looked a lot more like those other projects than I'd assumed going in.

Interviewer: Let's move to the utility question. What were you facing there, and what were your options?

Participant: Our utility maps for that stretch were over five years old, and the contractor flagged a few spots near the bore path where they weren't confident what was actually in the ground. We could pay for an updated survey — about $150,000 and three extra weeks — or proceed on the existing maps and manage anything that came up through our normal process.

Interviewer: What tipped it toward proceeding without the survey?

Participant: We have a solid weekly risk-review cadence, and a change-order tracking process that's pretty tight. I felt like if something came up, we'd catch it fast and deal with it through that mechanism rather than paying upfront to eliminate the uncertainty. It felt like an acceptable trade — spend the time and money there, or trust the oversight we already had running.

Interviewer: And what happened after that decision?

Participant: A few months into construction, crews struck a high-voltage duct that wasn't on any of our maps. Full stop on that segment for safety, about two weeks lost, plus the cost of the incident response and re-sequencing.

Interviewer: Looking back at that now, how foreseeable does it feel?

Participant: Honestly? In hindsight it feels almost obvious — that corridor's old, the utility ownership records were a mess, of course something was going to be down there that we didn't know about. It's the kind of thing you look at now and think, how did we not expect that.

Interviewer: At the time, though, how was that risk actually rated?

Participant: Our risk register had it logged as low likelihood. The team didn't flag it as a top concern going in.

Interviewer: Let's talk about the risk report the contractor sent after the strike. What did that process look like?

Participant: It was a substantial document — forty pages, laying out a projected 12 percent cost overrun and about ten weeks of schedule impact. Those numbers were bad enough that I didn't really want to carry them over to the grant side until the next monitoring cycle gave us something a little less ugly to bring forward. I had five business days to sign off. Problem was, that same week I was buried in quarterly board prep.

Interviewer: How did you handle the review given that?

Participant: I read the executive summary, delegated the detailed analysis to one of my leads, and told the team to keep monitoring things as they came in. I didn't ask my lead for a readout on what the detailed numbers actually showed, and I didn't loop in the grant administrator or escalate it up the chain at that point — I figured we'd get a clearer picture once the monitoring caught up.

Interviewer: Did the risk picture change in the following weeks?

Participant: It got worse before we brought it back into focus. We ended up escalating later and requesting a schedule accommodation from the grant side, which added its own headache.

Interviewer: Let's go to the testing decision near the end. What was the situation?

Participant: We had six weeks left before the grant obligation deadline. Standard systems integration testing protocol for this kind of interlocking work is eight weeks. Our signal engineering lead wanted the full eight weeks — no shortcuts. But the grants officer was clear that missing the milestone put around $4 million of funding at risk.

Interviewer: What alternatives did you consider?

Participant: We could ask the federal administrator for a formal extension and keep the full eight-week protocol, or compress testing to five weeks, trimming some of the redundant verification cycles, and hit the deadline as scheduled.

Interviewer: How did you land on compressing it?

Participant: We couldn't afford to lose that $4 million. That was really the driver. The engineering lead's case for the full protocol was sound, but against a funding number that size, protecting the grant took priority.

Interviewer: If the funding situation had been reversed — say that $4 million wasn't already secured, but finishing on time would have earned you an extra $4 million instead — do you think you'd have made the same call?

Participant: Probably not, honestly. If it were more like a bonus we might land versus something we already had in hand, I think we'd have leaned toward keeping the full eight weeks. Protecting money that was already ours felt different than chasing the same amount as upside.

Interviewer: How did the testing decision play out?

Participant: Testing finished in the compressed window, system passed, we hit the deadline and kept the funding. Whether those trimmed verification cycles matter down the road, I honestly don't know yet — too early to say.

Interviewer: If you'd had unlimited time and budget for that survey, would the utility decision have gone differently?

Participant: Probably, yeah — I'd have just paid for it and taken the three weeks. It wasn't that much money relative to the project.

Interviewer: If the grant deadline had had more flexibility, would the testing call have changed?

Participant: Almost certainly. Without that clock, I think we default straight to the full eight weeks, no debate.

Interviewer: What would you tell a peer walking into a similar fixed-price, fixed-deadline project?

Participant: Get your ground-truth data early, before you're locked into a schedule you can't easily unwind. And build in a real buffer against the funding clock so you're not making testing-scope decisions under that kind of pressure at the very end.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "RT_Biased_5",
  "domain_id": "RT",
  "domain": "Rail Transportation",
  "role": "Project Manager / Capital Projects Manager (Rail Infrastructure)",
  "condition": "biased_counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Corridor Interlocking Replacement: Schedule, Survey, and Grant-Deadline Pressure",
    "scenario_summary_internal": "A regional rail agency Capital Projects Manager oversees a design-build replacement of an aging interlocking/signaling system on a busy commuter corridor, funded in part by a federal infrastructure grant with a hard obligation deadline. The PM sets an aggressive baseline schedule, elects to skip an updated utility survey in favor of relying on active oversight processes, later underreacts to a contractor risk report flagging cost/schedule overrun after an unmapped utility strike, and finally compresses systems-integration testing to protect grant funding as the deadline nears. The interview reconstructs these four decisions retrospectively.",
    "occupational_realism": {
      "objective": "Deliver a signal/interlocking replacement on a commuter rail corridor on schedule and within the federal grant's obligation window, while maintaining safety-critical testing standards.",
      "setting": "Mid-size regional commuter rail agency; design-build capital project; corridor with active revenue service requiring possession/outage windows for construction.",
      "constraints": [
        "Fixed federal grant obligation deadline with risk of partial defunding on slippage",
        "Limited track possession/outage windows shared with revenue operations",
        "Fixed-price design-build contract with limited change-order flexibility",
        "Aging, incompletely documented underground utility infrastructure in the corridor",
        "PM's competing obligations to board reporting, grant compliance officer, and field operations"
      ],
      "stakeholders": [
        "Capital Projects Manager (interviewee)",
        "Design-build contractor project manager",
        "Agency chief engineer",
        "Signal/systems integration engineering lead",
        "Grants and compliance officer",
        "Rail operations/dispatch department",
        "Third-party utility owners",
        "Federal grant administrator"
      ],
      "technical_terms_to_use": [
        "interlocking replacement",
        "signal cutover",
        "positive train control (PTC) interface",
        "utility conduit conflict",
        "geotechnical/utility survey",
        "fixed-price design-build contract",
        "systems integration testing",
        "possession window",
        "change order",
        "risk register",
        "grant obligation deadline",
        "commissioning protocol"
      ],
      "technical_terms_to_avoid": [
        "aviation-specific terminology",
        "maritime terminology",
        "unrelated software engineering jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Grant obligation deadline is 30 months from project initiation",
          "Comparable interlocking replacement projects at peer agencies took 28-34 months historically",
          "Contractor's proposal assumes best-case crew productivity rates",
          "Agency leadership wants visible grant utilization progress reported to the board"
        ],
        "new_information_after_decision": [
          "Actual crew productivity later trails the plan, consistent with the historical range the PM had access to at baseline"
        ],
        "alternatives": [
          "Adopt an aggressive 24-month baseline schedule to build political margin",
          "Adopt a 30-month baseline schedule anchored to historical analogous project durations"
        ],
        "intended_action": "PM selects the aggressive 24-month schedule, anchoring on the contractor's best-case estimate and discounting historical overrun patterns on comparable projects."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Existing utility maps for the corridor are over five years old",
          "Contractor flags several unmapped conduit locations near the planned bore path",
          "An updated survey would cost $150K and add three weeks to baseline",
          "PM has established a weekly risk-review and change-order tracking process"
        ],
        "new_information_after_decision": [
          "Mid-construction, crews strike an unmapped high-voltage utility duct, triggering a multi-week safety stand-down"
        ],
        "alternatives": [
          "Commission an updated utility/geotechnical survey before finalizing the fixed-price schedule",
          "Proceed on existing maps, relying on the weekly risk-review cadence to catch and manage conflicts as they surface"
        ],
        "intended_action": "PM proceeds without the survey, judging that active weekly oversight and change-order discipline will let the team manage unknown conditions as they arise."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Contractor delivers a 40-page risk/cost report following the utility strike, projecting a 12% cost overrun and 10-week delay",
          "Report requires PM sign-off within five business days",
          "PM's calendar is consumed by quarterly board preparation"
        ],
        "new_information_after_decision": [
          "Overrun risk compounds over the following weeks, eventually requiring formal escalation and a deadline-renegotiation request to the grant administrator"
        ],
        "alternatives": [
          "Block dedicated time to fully review the report and convene a risk workshop with the engineering lead",
          "Skim the executive summary, delegate detailed review, and continue the existing reporting cadence without escalating"
        ],
        "intended_action": "PM defers detailed engagement with the report's underlying analysis, tells the team to 'keep monitoring,' and does not escalate to leadership or the grant administrator at this stage."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Six weeks remain before the grant obligation deadline",
          "Systems integration testing normally requires an eight-week protocol",
          "Signal engineering lead recommends the full eight-week test window",
          "Grants officer states a milestone slip risks roughly $4M in partial defunding"
        ],
        "new_information_after_decision": [
          "Testing completes within the compressed window and the system passes, but with fewer redundant verification cycles; funding is preserved but long-term reliability implications are not yet known at interview time"
        ],
        "alternatives": [
          "Request a formal deadline extension from the grant administrator while completing the full eight-week protocol",
          "Compress testing to five weeks, cutting some redundant verification cycles, to preserve the funding"
        ],
        "intended_action": "PM frames the decision around not losing the $4M and compresses the testing timeline, prioritizing funding preservation over the engineering team's full recommended protocol."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role on this project and what the corridor interlocking replacement was meant to achieve.",
        "What made this project nonroutine compared to prior capital projects you've managed?"
      ],
      "timeline_reconstruction": [
        "Walk me through the project chronologically from initiation to commissioning.",
        "What cues or signals prompted you to move from one phase to the next?",
        "At what point did you first sense the project might not go as planned?"
      ],
      "decision_point_probes": [
        "What information did you have available when you set the baseline schedule, and how did you weigh it?",
        "What alternatives did you consider for the utility survey question, and why did you choose the path you did?",
        "When the contractor's risk report came in, what was your process for reviewing it and deciding next steps?",
        "How did you weigh the testing protocol recommendation against the grant deadline pressure?",
        "How much time pressure did you feel at each of these moments, and how did that affect your options?",
        "What was your level of uncertainty at each decision, and how did you handle it?",
        "Had you faced a similar situation before? How did that experience shape your choice this time?"
      ],
      "closing_hypotheticals": [
        "If you had unlimited budget and time for the utility survey, would you have decided differently?",
        "If the grant deadline had been flexible, would your testing decision have changed?",
        "Looking back, was the utility strike something the team could have anticipated at the time?",
        "What would you tell a peer facing a similar fixed-price, fixed-deadline project?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "decision_point": 1,
        "mechanism": "PM anchors the baseline schedule on the contractor's best-case productivity estimate while discounting the distribution of durations from comparable historical projects that were available to them at the time.",
        "affected_reasoning_operation": "Estimation/forecasting of project duration",
        "evidence_available_at_time": [
          "Contractor's optimistic productivity-based proposal",
          "Historical duration range (28-34 months) from peer agency projects"
        ],
        "required_textual_manifestation": "PM explains choosing the 24-month schedule primarily by citing the contractor's proposal and board pressure, while acknowledging but setting aside the historical range as 'not really comparable to our team.'",
        "plausible_nonbias_interpretation": "PM could argue the peer projects had different scope or team composition, making the shorter estimate a reasonable domain judgment rather than a forecasting error.",
        "strength": "subtle",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "underestimation bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Control",
        "decision_point": 2,
        "mechanism": "PM substitutes confidence in an active management process (weekly risk reviews, change-order tracking) for actually reducing the underlying informational uncertainty (outdated utility maps), treating procedural oversight as equivalent to control over physical/ground conditions.",
        "affected_reasoning_operation": "Risk evaluation and decision to accept incomplete information",
        "evidence_available_at_time": [
          "Outdated utility maps (5+ years old)",
          "Contractor flag of unmapped conduit locations",
          "Existence of PM's weekly risk-review process"
        ],
        "required_textual_manifestation": "PM states that skipping the survey was acceptable because 'we track everything weekly and would catch issues fast,' framing internal process rigor as sufficient to manage an external, unknown physical condition.",
        "plausible_nonbias_interpretation": "PM could argue that time and cost tradeoffs justified accepting the survey gap as a calculated, budget-conscious risk rather than an overestimate of control.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control", "overconfidence in process"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Hindsight Bias",
        "decision_point": 2,
        "mechanism": "In a retrospective probe about the utility strike, PM recalls the conflict as having been 'clearly predictable' given the corridor's age, which is inconsistent with the team's contemporaneous risk register that had rated the utility conflict as low likelihood at the time of the decision.",
        "affected_reasoning_operation": "Retrospective causal attribution / memory reconstruction of past uncertainty",
        "evidence_available_at_time": [
          "Contemporaneous risk register entry rating utility conflict as low likelihood",
          "Post-hoc knowledge of the actual utility strike outcome"
        ],
        "required_textual_manifestation": "When asked to reflect on the strike, PM says something like 'looking back, it was obvious this corridor was going to have hidden utilities—we should have seen it coming,' contradicting the low-likelihood rating the team itself assigned beforehand.",
        "plausible_nonbias_interpretation": "PM could be expressing legitimate updated risk literacy for future projects rather than misremembering the foreseeability of the specific outcome.",
        "strength": "subtle",
        "do_not_make_explicit": ["hindsight bias", "creeping determinism"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Ostrich Effect",
        "decision_point": 3,
        "mechanism": "Facing a detailed adverse risk/cost report, PM avoids engaging with its underlying data (skims summary, delegates without follow-up, does not escalate) rather than confronting the unfavorable information directly, despite having the time-bounded sign-off obligation.",
        "affected_reasoning_operation": "Information-seeking and evidence engagement under threat of unfavorable news",
        "evidence_available_at_time": [
          "40-page contractor risk/cost report projecting 12% overrun and 10-week delay",
          "Five-business-day sign-off window",
          "PM's own calendar constraints"
        ],
        "required_textual_manifestation": "PM describes skimming only the executive summary, delegating the detailed review without following up, and telling the team to 'keep monitoring' instead of opening the full analysis or escalating, despite recognizing the report's seriousness.",
        "plausible_nonbias_interpretation": "PM could argue that delegation was a legitimate time-management choice given competing board-reporting duties, not avoidance of bad news.",
        "strength": "moderate",
        "do_not_make_explicit": ["ostrich effect", "avoidance of negative information"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Aversion or Loss Framing effect",
        "decision_point": 4,
        "mechanism": "PM frames the testing-schedule decision predominantly around avoiding the loss of the $4M in grant funding rather than symmetrically weighing the safety/reliability value of the full test protocol, producing a choice that overweights the framed loss relative to the foregone verification benefit.",
        "affected_reasoning_operation": "Tradeoff evaluation between funding risk and safety/reliability protocol completeness",
        "evidence_available_at_time": [
          "Grants officer's statement that a slip risks ~$4M defunding",
          "Signal engineering lead's recommendation for the full eight-week protocol",
          "Six weeks remaining before the deadline"
        ],
        "required_textual_manifestation": "PM explicitly states the decision was driven by 'we couldn't afford to lose that $4M' and describes compressing testing to preserve funding, giving comparatively little explicit weight to the engineering lead's full-protocol rationale.",
        "plausible_nonbias_interpretation": "PM could argue the compressed protocol still met minimum safety-certification requirements, making this a defensible resource-constrained engineering tradeoff rather than a framing-driven distortion.",
        "strength": "moderate",
        "do_not_make_explicit": ["loss aversion", "loss framing", "prospect theory"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is the biased_counterfactual condition, not a control."
    },
    "counterfactual_specification": {
      "causal_variable": "Whether the Capital Projects Manager commissioned an updated utility/geotechnical survey before finalizing the fixed-price baseline schedule",
      "original_state": "Survey requested/considered but not commissioned; baseline schedule and fixed-price contract finalized using outdated (5+ year old) utility maps",
      "counterfactual_state": "PM proceeds to skip the survey entirely, relying on the weekly risk-review/change-order process to manage unmapped-utility risk as it surfaces, rather than resolving the uncertainty upfront",
      "variables_to_hold_constant": [
        "Grant obligation deadline (30 months) and $4M defunding risk",
        "Contractor identity and fixed-price contract structure",
        "Agency staffing and PM's role/authority",
        "Corridor location and general utility-age profile",
        "Occurrence of the eventual utility strike and downstream schedule/cost impacts"
      ],
      "expected_causal_difference": "Skipping the survey (versus commissioning it) removes the three-week/$ 150K upfront cost but leaves the unmapped-conduit risk unresolved, causally enabling the mid-construction utility strike, the subsequent risk-report avoidance at decision point 3, and the funding-driven testing compression at decision point 4.",
      "causal_test_question": "Would the mid-construction utility strike, the cost/schedule overrun, and the compressed testing decision have occurred if the PM had commissioned the updated utility survey before finalizing the baseline schedule?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and each has at least two plausible alternatives.",
      "Confirm each of the 5 planned instances is tied to a single, identifiable decision/inference/probe response with distinguishable evidence.",
      "Confirm no bias term, definition, or explicit psychological label appears in the drafted interview text.",
      "Confirm cb_02 and cb_03 at decision point 2 use different reasoning operations (in-the-moment risk evaluation vs. retrospective causal attribution) and different evidence traces.",
      "Confirm word count target of 1,350 words (acceptable range 1,215-1,485) is achievable given 4 decision points, probe plan, and 5 embedded instances without repetitive exposition.",
      "Confirm consequences at each decision point are consistent with either a biased or a reasonable-judgment account (non-mechanical proof of bias).",
      "Confirm the counterfactual variable holds all other material facts constant and changes only the survey-commissioning decision."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased_counterfactual",
    "exact_occurrence_manifest": [
      { "bias": "Hindsight Bias", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Illusion of Control", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Loss Aversion or Loss Framing effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Ostrich Effect", "occurrences": 1, "mechanism_constraint": null },
      { "bias": "Planning Fallacy", "occurrences": 1, "mechanism_constraint": null }
    ],
    "target_bias_names": [
      "Hindsight Bias",
      "Illusion of Control",
      "Loss Aversion or Loss Framing effect",
      "Ostrich Effect",
      "Planning Fallacy"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Hindsight Bias", "requested_occurrences": 1 },
      { "bias": "Illusion of Control", "requested_occurrences": 1 },
      { "bias": "Loss Aversion or Loss Framing effect", "requested_occurrences": 1 },
      { "bias": "Ostrich Effect", "requested_occurrences": 1 },
      { "bias": "Planning Fallacy", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy" },
      { "instance_id": "cb_02", "bias": "Illusion of Control" },
      { "instance_id": "cb_03", "bias": "Hindsight Bias" },
      { "instance_id": "cb_04", "bias": "Ostrich Effect" },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Illusion of Control", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Hindsight Bias", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Ostrich Effect", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Planning Fallacy",
        "mechanism": "Anchoring baseline schedule on contractor's best-case estimate while discounting available historical duration data from comparable projects.",
        "affected_reasoning_operation": "Duration estimation/forecasting",
        "evidence_source": "Contractor proposal vs. historical peer-agency project durations",
        "distinctiveness_requirement": "Occurs at initiation/baseline-setting; involves forward-looking forecasting, not retrospective judgment or risk-control belief."
      },
      {
        "instance_id": "cb_02",
        "bias": "Illusion of Control",
        "mechanism": "Substituting confidence in an internal management process (weekly risk review) for actual reduction of external physical uncertainty (unmapped utilities).",
        "affected_reasoning_operation": "Risk evaluation under incomplete information at the moment of the survey decision",
        "evidence_source": "PM's own process description vs. outdated utility maps/flagged unknowns",
        "distinctiveness_requirement": "Occurs in-the-moment at the survey/schedule decision, distinct from the later retrospective recall at the same decision point (cb_03)."
      },
      {
        "instance_id": "cb_03",
        "bias": "Hindsight Bias",
        "mechanism": "Retrospectively characterizing the utility conflict as obviously foreseeable, inconsistent with the team's contemporaneous low-likelihood risk rating.",
        "affected_reasoning_operation": "Post-hoc causal attribution / memory reconstruction in response to a reflection probe",
        "evidence_source": "Contemporaneous risk-register rating vs. post-outcome recollection",
        "distinctiveness_requirement": "Occurs only in a later reflective probe response about decision point 2's outcome, not in the original in-the-moment decision (cb_02)."
      },
      {
        "instance_id": "cb_04",
        "bias": "Ostrich Effect",
        "mechanism": "Avoiding direct engagement with an unfavorable, detailed risk/cost report by skimming, delegating without follow-up, and not escalating within the required review window.",
        "affected_reasoning_operation": "Information engagement/evidence-seeking under threat of unfavorable news",
        "evidence_source": "Contractor's 40-page risk/cost report and PM's review behavior",
        "distinctiveness_requirement": "Confined to decision point 3's report-handling behavior; not a repetition of cb_02's control belief or cb_01's forecasting."
      },
      {
        "instance_id": "cb_05",
        "bias": "Loss Aversion or Loss Framing effect",
        "mechanism": "Framing the testing-schedule tradeoff predominantly around avoiding the $4M funding loss rather than symmetrically weighing full-protocol safety/reliability value.",
        "affected_reasoning_operation": "Tradeoff evaluation between funding risk and protocol completeness",
        "evidence_source": "Grants officer's loss framing vs. engineering lead's full-protocol recommendation",
        "distinctiveness_requirement": "Occurs at the final decision point only, tied to explicit loss-framed language distinct from all prior instances."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Planning Fallacy", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Illusion of Control", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Hindsight Bias", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Ostrich Effect", "strength": "moderate" },
      { "instance_id": "cb_05", "bias": "Loss Aversion or Loss Framing effect", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Commissioning of an updated utility/geotechnical survey before finalizing the fixed-price baseline schedule",
      "original_state": "Survey requested/considered but not commissioned prior to baseline finalization",
      "changed_state": "Survey skipped entirely; PM relies on active weekly risk-review process to manage unmapped-utility risk as it surfaces",
      "variables_to_hold_constant": [
        "30-month grant obligation deadline and ~$4M defunding risk",
        "Contractor identity and fixed-price contract terms",
        "PM's role, authority, and team composition",
        "Corridor location and utility-age profile",
        "Occurrence and timing of the eventual utility strike"
      ]
    },
    "scenario_id": "RT_Biased_5",
    "domain_id": "RT",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points with mechanism-fit prioritization; decision point 2 hosts two distinct biases (Illusion of Control at time of decision, Hindsight Bias in a later reflective probe about the same decision's outcome), using different reasoning operations and evidence sources as required when a decision point hosts more than one instance.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "30-month grant obligation deadline and ~$4M defunding risk",
      "Contractor identity and fixed-price contract terms",
      "PM's role, authority, and team composition",
      "Corridor location and utility-age profile",
      "Occurrence and timing of the eventual utility strike"
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
          "segment_type": "Baseline duration estimate",
          "raw_interview_anchor": "Participant leans on contractor's best-case proposal, discounts peer projects, and selects 24 months.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "Contractor's best-case estimate is privileged over known peer durations, matching cb_01."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "Retrospective schedule recalibration",
          "raw_interview_anchor": "After productivity slips, participant says actuals look more like peer-project durations.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Eligible retrospective judgment but no separate hidden instance."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "Utility-survey risk decision",
          "raw_interview_anchor": "Participant trusts weekly risk review and change-order tracking to catch unmapped utilities.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_02"
          ],
          "ground_truth_rationale": "Process confidence is treated as control over unknown physical conditions, matching cb_02."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "Retrospective foreseeability judgment",
          "raw_interview_anchor": "After the strike, participant calls it almost obvious despite the contemporaneous low-likelihood rating.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_03"
          ],
          "ground_truth_rationale": "Post-outcome obviousness conflicts with the prior low-likelihood assessment, matching cb_03."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "Contractor risk-report review and escalation",
          "raw_interview_anchor": "Report-handling reasoning: did not want to carry bad numbers to the grant side; skimmed summary, delegated without follow-up, did not escalate, and waited for monitoring.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_04"
          ],
          "ground_truth_rationale": "Adverse-information avoidance through shallow review and deferred escalation, matching cb_04."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "Systems-integration testing tradeoff",
          "raw_interview_anchor": "Avoiding the $4M funding loss drove the choice to compress testing despite the engineering lead's sound case.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_05"
          ],
          "ground_truth_rationale": "Decision is framed around avoiding a $4M loss, matching cb_05."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "Post-test uncertainty",
          "raw_interview_anchor": "System passed, but participant says it is too early to know whether trimmed cycles matter.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Uncertainty about future effects is acknowledged without another bias."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "Advice for a similar project",
          "raw_interview_anchor": "Recommends early ground-truth data and a schedule buffer against the funding clock.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Forward-looking recommendation; no hidden target instance."
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
    "analysis_scope_note": "No retrieved corpus passages were supplied in the prompt; classifications rely on established cognitive-science knowledge and are explicitly not grounded in retrieved corpus evidence."
  },
  "identified_bias_summary": [
    {
      "bias_label": "hindsight bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "loss aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "ostrich effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "planning fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "planning fallacy",
      "alternative_labels": [
        "optimism bias",
        "inside view"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to underestimate the time, costs, and risks of future actions while overestimating their benefits, often by relying on plan-specific best-case scenarios instead of distributional data from similar prior projects.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Baseline schedule duration setting",
      "decision_point_description": "Choosing the project baseline schedule duration based on contractor estimates, peer agency data, and leadership expectations.",
      "affected_reasoning_operation": "Duration estimation and risk calibration",
      "bias_specific_mechanism": "The participant discounted relevant base-rate evidence from peer projects indicating 28 to 34 months and relied instead on the contractor's best-case productivity assumptions plus an unsupported belief that his team would execute more efficiently than those comparators, producing an aggressive 24-month schedule.",
      "manifestation_in_interview": "When describing how the baseline schedule was set, the participant reported leaning on the contractor's best-case proposal and dismissing peer agency durations as non-comparable while asserting superior team execution.",
      "effect_on_reasoning_or_decision": "Adoption of a 24-month schedule below the historical peer range; later productivity slippage made the project resemble those peer projects more closely than the original estimate assumed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The contractor's proposal assumed pretty efficient crew productivity — their best-case numbers. We also had data from a couple of peer agencies that had done similar interlocking swaps, and those ran 28 to 34 months typically.",
          "evidence_explanation": "Shows the participant had distributional base-rate information indicating a longer typical duration than the contractor's best-case proposal."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I leaned on the contractor's proposal more. The peer projects weren't identical setups — different signal vendors, different corridor configurations — so I didn't think the comparison held up perfectly. We went with 24 months. I figured our team was sharper on execution than what those other durations reflected.",
          "evidence_explanation": "Demonstrates plan-specific optimism and selective discounting of historical base rates in favor of an unreliable self-assessment of superior execution."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, once productivity started trailing plan, it looked a lot more like those other projects than I'd assumed going in.",
          "evidence_explanation": "Corroborates that the original schedule estimate was unrealistically lower than the historical baseline range."
        }
      ],
      "correction_or_counterevidence": "Leadership pressure and the fixed grant deadline may have incentivized an aggressive baseline, but the cognitive distortion is specifically the selective discounting of peer data and the adoption of an unsupported superior-execution assumption.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; classification relies on established cognitive-science knowledge of the planning fallacy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "overconfidence effect",
      "alternative_labels": [
        "illusion of control",
        "optimism bias",
        "risk underestimation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which a person's subjective confidence in their judgments or abilities is reliably greater than their objective accuracy or the actual controllability of outcomes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Utility survey decision",
      "decision_point_description": "Deciding whether to commission an updated underground utility survey or proceed on existing maps using the existing risk-review and change-order processes.",
      "affected_reasoning_operation": "Risk assessment and probability estimation",
      "bias_specific_mechanism": "Faced with known uncertainty about underground utilities, the participant overestimated the ability of existing weekly risk-review and change-order processes to detect and manage unknown utilities, reducing the perceived value of eliminating uncertainty through an upfront survey.",
      "manifestation_in_interview": "The participant described the choice and explained that he trusted the existing oversight cadence rather than paying to eliminate uncertainty; the risk register also rated the utility risk as low likelihood.",
      "effect_on_reasoning_or_decision": "The project proceeded without the survey, later encountering an unmapped high-voltage duct strike that caused a safety stand-down, approximately two weeks of delay, and incident response and re-sequencing costs.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Our utility maps for that stretch were over five years old, and the contractor flagged a few spots near the bore path where they weren't confident what was actually in the ground.",
          "evidence_explanation": "Establishes that there was known, specific uncertainty about subsurface utilities."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "We could pay for an updated survey — about $150,000 and three extra weeks — or proceed on the existing maps and manage anything that came up through our normal process.",
          "evidence_explanation": "Defines the discrete risk-management choice point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I felt like if something came up, we'd catch it fast and deal with it through that mechanism rather than paying upfront to eliminate the uncertainty.",
          "evidence_explanation": "Directly expresses overestimated confidence that existing management processes could control an uncertain subsurface hazard."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Our risk register had it logged as low likelihood. The team didn't flag it as a top concern going in.",
          "evidence_explanation": "Shows consequent underestimation of risk despite recognized data-quality problems."
        }
      ],
      "correction_or_counterevidence": "The decision could be viewed as a routine cost-schedule-risk trade-off under fixed budget and deadline constraints, and the survey would have required time and money. However, the explicit belief that existing processes would allow fast detection and management of an unknown underground utility, combined with the low likelihood rating, supports an overconfidence mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; classification relies on established cognitive-science knowledge of overconfidence and illusion of control.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "hindsight bias",
      "alternative_labels": [
        "knew-it-all-along effect",
        "creeping determinism"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to perceive past events as having been more predictable or foreseeable after the outcome is known than they actually were before they occurred.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Retrospective foreseeability assessment of the utility strike",
      "decision_point_description": null,
      "affected_reasoning_operation": "Retrospective causal judgment and foreseeability estimation",
      "bias_specific_mechanism": "After learning that construction crews struck an unmapped high-voltage duct, the participant reconstructed the risk as almost obvious and expressed that the event was something he should have expected, despite the at-time risk being logged as low likelihood.",
      "manifestation_in_interview": "When asked how foreseeable the utility issue felt in retrospect, the participant said it felt almost obvious and that he now thought, \"how did we not expect that.\"",
      "effect_on_reasoning_or_decision": "Distorted retrospective perception of the original risk, making the outcome appear more predictable than the contemporaneous risk assessment indicated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly? In hindsight it feels almost obvious — that corridor's old, the utility ownership records were a mess, of course something was going to be down there that we didn't know about. It's the kind of thing you look at now and think, how did we not expect that.",
          "evidence_explanation": "Expresses a classic hindsight-bias reconstruction: the outcome is judged as highly foreseeable after the fact."
        }
      ],
      "correction_or_counterevidence": "The participant may be engaging in candid self-criticism or learning rather than making a formal probabilistic claim. However, the explicit \"in hindsight it feels almost obvious\" language indicates a distorted retrospective foreseeability judgment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; classification relies on established cognitive-science knowledge of hindsight bias.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "ostrich effect",
      "alternative_labels": [
        "information avoidance",
        "selective exposure",
        "motivated avoidance"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Motivated avoidance of negative or threatening information, leading to delayed attention, incomplete review, or failure to escalate adverse signals.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor risk report review and escalation",
      "decision_point_description": "Deciding how thoroughly to review a substantial contractor risk report and whether to escalate its projected cost and schedule impacts to the grant administrator or leadership before the next monitoring cycle.",
      "affected_reasoning_operation": "Information seeking and risk escalation",
      "bias_specific_mechanism": "The participant avoided the full negative implications of the risk report because the projected cost and schedule impacts were aversive; he delegated detailed analysis without obtaining a readout and delayed escalation in the hope that future monitoring would present a less unfavorable picture.",
      "manifestation_in_interview": "The participant reported reading only the executive summary, delegating detailed analysis, and not asking for a readout or escalating, while describing the numbers as \"bad enough\" and wanting something \"less ugly\" to bring forward.",
      "effect_on_reasoning_or_decision": "Risk information was not fully integrated into timely decision-making, escalation was delayed, and the risk picture worsened before it was brought back into focus.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Those numbers were bad enough that I didn't really want to carry them over to the grant side until the next monitoring cycle gave us something a little less ugly to bring forward.",
          "evidence_explanation": "Shows explicit motivation to avoid communicating aversive risk information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I read the executive summary, delegated the detailed analysis to one of my leads, and told the team to keep monitoring things as they came in. I didn't ask my lead for a readout on what the detailed numbers actually showed, and I didn't loop in the grant administrator or escalate it up the chain at that point — I figured we'd get a clearer picture once the monitoring caught up.",
          "evidence_explanation": "Demonstrates selective attention and avoidance of detailed negative analysis, with an expectation of a more favorable future monitoring picture."
        }
      ],
      "correction_or_counterevidence": "The participant was also under workload pressure from quarterly board preparation, which may partially explain shallow review. However, the explicit \"didn't really want\" and hope for something \"less ugly\" indicate a motivational information-avoidance mechanism rather than mere time constraint.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; classification relies on established cognitive-science knowledge of the ostrich effect and information avoidance.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "loss aversion",
      "alternative_labels": [
        "framing effect",
        "prospect theory loss aversion",
        "endowment effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to weigh potential losses more heavily than equivalent potential gains, producing risk preferences that depend on whether an outcome is framed as a loss or a gain.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Systems integration testing scope decision",
      "decision_point_description": "Deciding between compressing systems integration testing to five weeks to preserve secured grant funding or requesting a formal extension and retaining the full eight-week protocol.",
      "affected_reasoning_operation": "Risk trade-off and option evaluation",
      "bias_specific_mechanism": "The participant evaluated the $4 million funding as a loss to be protected rather than an equivalent gain; the asymmetric valuation of losing already-secured money over gaining the same amount pushed the decision toward testing compression despite the engineering lead's sound case for full verification.",
      "manifestation_in_interview": "The participant said the funding loss was the driver, and in a gain-framed counterfactual he indicated he likely would have made the opposite call because money already in hand \"felt different\" from the same amount as upside.",
      "effect_on_reasoning_or_decision": "Led to compressing systems integration testing to five weeks and trimming redundant verification cycles to avoid losing $4 million, while the same amount framed as a potential gain would not have produced the same decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We couldn't afford to lose that $4 million. That was really the driver. The engineering lead's case for the full protocol was sound, but against a funding number that size, protecting the grant took priority.",
          "evidence_explanation": "Shows that the choice was dominated by avoiding a loss of secured funding rather than a symmetric comparison of testing risk and funding value."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably not, honestly. If it were more like a bonus we might land versus something we already had in hand, I think we'd have leaned toward keeping the full eight weeks. Protecting money that was already ours felt different than chasing the same amount as upside.",
          "evidence_explanation": "Explicitly demonstrates loss-gain asymmetric valuation: the same $4 million is treated differently depending on whether it is framed as a loss of an existing entitlement or a forgone gain."
        }
      ],
      "correction_or_counterevidence": "Protecting secured grant funding could be normatively justified if loss of the grant had budget or legal implications beyond the mere $4 million. The testing ultimately passed and the deadline was met, so no negative operational outcome is asserted. The bias evidence is the contrast between loss-framed and gain-framed reasoning.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were provided; classification relies on established cognitive-science knowledge of loss aversion and framing effects from prospect theory.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied; bias labels and mechanisms are based on established cognitive-science knowledge rather than retrieval-grounded literature.",
    "The analysis relies on a single participant's retrospective self-report, which may omit or reframe contemporaneous reasoning.",
    "The transcript describes real project decisions with institutional constraints; separation of cognitive bias from bounded rational response under time, resource, and deadline pressure requires inference.",
    "Occurrences were limited to episodes where the transcript affirmatively manifested a bias-specific mechanism; ambiguous or merely plausible distortions were not classified."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "RT_Biased_5_Gemini_off",
  "interview_id": "RT_Biased_5",
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
