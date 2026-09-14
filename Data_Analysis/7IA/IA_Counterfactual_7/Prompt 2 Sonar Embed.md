You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the procurement-network reporting incident in detail, including your own decision-making, and that this is for internal process review rather than any kind of performance evaluation.

Participant: Sure, that's fine.

Interviewer: Can you give me your role and a quick sense of what this incident was?

Participant: I'm a reports officer, and I also handle collection management for our part of the station. A walk-in showed up claiming to know about a shipment tied to a procurement network we'd been chasing for months. We had a policy briefing coming up, but we actually had about five days before it, which is more breathing room than these things usually get.

Interviewer: Walk me through how it began.

Participant: This network had been frustrating us for a while — lots of partial reporting, nothing that really nailed down how they were moving material. Then a walk-in comes into the local office claiming direct knowledge of an imminent shipment. He had a handwritten fragment that looked like part of a manifest, and a photo of a shipping container. My first reaction was that it looked like exactly the pattern we'd been building toward — the markings, the paper trail, it lined up with what we expected this network's shipments to look like. I told my deputy it was almost a textbook match.

Interviewer: What did the documents actually show?

Participant: The manifest fragment was partial — some numbers, an abbreviated destination code, nothing complete. The photo was a standard container, generic markings, could've been thousands of containers at that port. We had time to run a full authentication cycle before the briefing, and I still read it as clearly consistent with the network. I didn't really sit with the idea that it could just as easily be a routine shipment.

Interviewer: How did you feel about it, beyond the analytical read?

Participant: Honestly, there was relief. We'd put months into this with basically nothing to show, and here's someone walking in with exactly the specificity we'd been missing. I remember thinking, finally, this is the break. That colored how quickly I moved toward validating the story, even though nothing was forcing me to move fast that day.

Interviewer: Let's reconstruct the timeline. What happened after the walk-in session?

Participant: I drafted debrief notes describing him as consistent with the network hypothesis and submitted a validation request, with the full runway to work with. We had a coordination call with technical collection a day or two later, and that's when a colleague flagged that their data showed activity at a different port than the one the walk-in named. I spent the following days drafting the report, and the last day or so before the briefing was spent finalizing language and setting up follow-on tasking.

Interviewer: Back to that first decision — treating the walk-in's material as consistent with the network hypothesis versus something requiring full validation first. What were your alternatives?

Participant: I could've treated him as fully unvetted and required standard validation before any tasking, treated the material as a strong match and moved toward tasking, or used the extra days for a complete authentication cycle before doing anything. I went with the middle path.

Interviewer: What made that more compelling than just waiting, given you actually had the days to spare?

Participant: That's the part I've turned over since. The pattern fit was strong enough that I didn't feel authentication would tell me much I didn't already believe. Looking back, the physical evidence itself wasn't that specific. I had the time to wait, and I didn't really use it that way.

Interviewer: Second decision point — reconciling the walk-in's account with the port discrepancy from technical collection. What did you weigh there?

Participant: He'd claimed a prior logistics role, which would explain how he'd know shipment details. That struck me as the kind of detail a real insider would know, not something you'd fabricate, so I leaned toward treating his account as credible on that basis. If I'm being straight about it, that claim on its own didn't establish anything about this specific shipment — it just fit the story we were already building, and I let that be enough. If the same claimed background had come attached to an account that pointed somewhere other than this network, I think I'd have wanted a lot more before accepting it. We had days to test that, and I didn't push on it.

Interviewer: How did the port discrepancy factor into the draft?

Participant: It went into a footnote. The corroborating sub-source material and the walk-in's account got most of the narrative space. I didn't have a strong evidentiary reason to downgrade the technical flag — if anything it deserved more scrutiny — and we had time to run it down properly. It just didn't get the same attention from me at the time.

Interviewer: What do you think was driving that imbalance, given the schedule wasn't actually forcing it?

Participant: Honestly, it wasn't the clock. The corroborating material fit the story we were already building, so it was just easier to write up. The discrepancy would have meant unwinding something, and I kept telling myself I'd circle back, but I never carved out the time even though I had it.

Interviewer: Third decision point — how you described the uncertainty in the report and how you scheduled the follow-on work. Walk me through that.

Participant: The shipment-timing estimate had real uncertainty in it. I could've written it emphasizing what we didn't know, or emphasizing the chance the network would move soon. I went with language that stressed imminent action.

Interviewer: Was the underlying estimate itself any different depending on the phrasing?

Participant: No, same number either way. But writing it as "likely to move soon" instead of "not yet confirmed to be imminent" made it feel more actionable while I was drafting — like it justified fewer qualifiers. That wasn't really about the deadline; I had four days left at that point, plenty of room to sit with the other version.

Interviewer: And the follow-on tasking timeline?

Participant: I set meetings and validation steps assuming everything would line up — interpreters, safehouses, sub-source cooperation, all on a fast track. We'd run similar sequences before and they'd almost always taken longer than planned. I had days, not hours, to build in a buffer, and I still didn't adjust for that history.

Interviewer: Fourth decision point — the branch chief's guidance on dissemination. What happened?

Participant: He reviewed the draft and wanted it out promptly, minimal additional caveats. The port discrepancy was still unresolved. I'd seen him make calls like this before in ambiguous situations, and he'd usually been right, so I didn't push back or ask for stronger caveat language, even though the schedule would have absorbed a short delay without any strain.

Interviewer: What was the deciding factor in not pushing back?

Participant: His track record and seniority carried a lot of weight for me. I didn't go back and independently re-examine the discrepancy myself before agreeing — I mostly deferred to his read of it. Having extra days available didn't really change that calculation for me.

Interviewer: What happened after dissemination?

Participant: The product went out largely as he preferred. Afterward, the observed shipment activity didn't line up with the timing we'd reported.

Interviewer: If the port discrepancy had surfaced earlier, before your first read of the walk-in, would your draft have looked different?

Participant: Maybe. I'd like to think I'd have weighed it more evenly rather than treating it as something to explain away.

Interviewer: Given you actually had several days rather than hours, is there a point where you'd have wanted to use that time differently?

Participant: The very first read of the documents. I had the days to sit with the ambiguity properly and I still moved toward validating the story quickly.

Interviewer: If this happened again with the same longer runway, what would you want in place beforehand?

Participant: A standing rule to get an independent second read on ambiguous evidence early, regardless of how much time is on the clock, and more discipline about using available time for historically realistic scheduling instead of assuming the best case just because a deadline exists somewhere out there.

Interviewer: That's really helpful. Thank you for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Counterfactual_7",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Human Intelligence (HUMINT) Collection Manager/Reports Officer",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "The Walk-In and the Longer Runway: Procurement Network Reporting Under Reduced Time Pressure",
    "scenario_summary_internal": "A HUMINT Collection Manager/Reports Officer at a forward station receives the same unvetted walk-in source claiming knowledge of an imminent illicit dual-use technology shipment tied to a procurement network the station has tracked for months. Unlike the paired scenario, the policy briefing is now five days out rather than 36 hours, giving the officer substantially more time to triage the source, reconcile the claim against existing multi-source reporting, draft the product, and respond to the branch chief's guidance. All other material facts, actors, and evidence are held constant so that the effect of the reduced deadline pressure on the same reasoning patterns can be isolated.",
    "occupational_realism": {
      "objective": "Determine whether the walk-in's claim about an imminent shipment is credible enough to redirect collection resources and to include in a policy-relevant intelligence product before a fixed briefing deadline, now five days out instead of 36 hours.",
      "setting": "The same regional HUMINT station supporting a task force on dual-use technology proliferation, operating under normal reporting cadence, facing an unscheduled walk-in contact, but with a materially longer runway before the fixed briefing deadline.",
      "constraints": [
        "Five-day window before a senior policymaker briefing, rather than 36 hours",
        "Limited but now less time-constrained means to vet the walk-in source's access and motivation",
        "Competing tasking requirements on the same technical collection assets",
        "Partial, sometimes contradictory reporting streams (existing HUMINT network, technical collection, open-source)",
        "Continued, though less acute, pressure from a senior officer to produce an actionable product"
      ],
      "stakeholders": [
        "The reports officer/collection manager (interviewee)",
        "The walk-in source",
        "An established sub-source network being run for months on the same target",
        "A senior reports officer/branch chief with a preference on dissemination timing",
        "Technical collection analysts providing a partially contradictory data stream",
        "The policy audience awaiting the briefing"
      ],
      "technical_terms_to_use": [
        "walk-in",
        "source validation",
        "collection tasking",
        "corroboration",
        "access and placement",
        "product turnaround",
        "confidence level",
        "dissemination",
        "sub-source",
        "reporting stream"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "cognitive bias",
        "heuristic",
        "anchoring",
        "framing effect",
        "authority bias",
        "wishful thinking",
        "belief bias",
        "selective attention",
        "planning fallacy"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Walk-in arrives unannounced claiming direct knowledge of an imminent shipment",
          "Walk-in presents a handwritten manifest fragment and a photo of a shipping container",
          "No independent vetting of the walk-in's stated access has yet occurred",
          "The station has spent months building a hypothesis about this same procurement network",
          "The briefing deadline is now five days out rather than 36 hours"
        ],
        "new_information_after_decision": [
          "Initial debrief notes are drafted describing the walk-in as consistent with the existing network hypothesis",
          "A request is submitted to validate the walk-in's documents, with more time available than in the paired incident"
        ],
        "alternatives": [
          "Treat the walk-in as an unvetted, uncorroborated contact requiring full standard validation before any tasking action",
          "Treat the material as strongly consistent with the prior network hypothesis and move directly to tasking",
          "Use the extra time to defer any assessment for a full document authentication cycle"
        ],
        "intended_action": "Officer interprets the ambiguous handwriting and container photo as clearly matching the network's known shipping pattern, and separately reflects that the timing is 'a stroke of luck' because it would validate months of otherwise inconclusive effort, even though standard authentication was now schedulable well within the deadline."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Existing sub-source reporting from the tracked network is ambiguous about shipment timing",
          "Technical collection has flagged activity at a different port than the one named by the walk-in",
          "The walk-in claims a prior logistics role that would explain access, but this claim is unverified",
          "A colleague raises the technical-collection discrepancy in a coordination call",
          "There is enough remaining time before the briefing to run down the discrepancy if prioritized"
        ],
        "new_information_after_decision": [
          "The report draft cites the walk-in and sub-source material prominently; the technical-collection discrepancy is mentioned only in a footnote",
          "The colleague's concern is logged but not incorporated into the main assessment, despite available time to reconcile it"
        ],
        "alternatives": [
          "Weigh the technical-collection discrepancy and the walk-in's account with comparable rigor before drafting, using the available extra days",
          "Give primary weight to the reporting that matches the established network hypothesis and treat the discrepancy as secondary",
          "Pause the draft for a day to reconcile the port discrepancy, which the timeline now comfortably allows"
        ],
        "intended_action": "Officer reasons that because the walk-in's claimed logistics background makes the story 'the kind of thing a real insider would know,' the account must be substantially true, and continues to emphasize corroborating threads while the contradicting technical-collection item receives minimal analytic attention, even though the schedule no longer forced that shortcut."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Briefing deadline is roughly four days away rather than 14 hours",
          "The estimate of shipment timing carries meaningful residual uncertainty",
          "Two ways exist to describe the same confidence level to the policy audience",
          "Historical timelines for similar validation-and-tasking sequences typically take longer than initially planned"
        ],
        "new_information_after_decision": [
          "The draft language is finalized using an urgency-emphasizing framing of the uncertain timeline",
          "A follow-on tasking and source-meeting schedule is set assuming compressed timeframes despite the longer overall runway"
        ],
        "alternatives": [
          "Present the uncertainty in terms of what is not yet known and what could invalidate the assessment",
          "Present the same uncertainty by emphasizing the probability that the network will act imminently",
          "Build follow-on tasking timelines around historical validation durations, which the extended deadline now comfortably permits"
        ],
        "intended_action": "Officer chooses wording that foregrounds the chance of imminent action rather than the chance of no action, and separately schedules follow-on source meetings and validation steps on a compressed timeline that assumes best-case availability of interpreters, safehouses, and sub-source cooperation, despite having days rather than hours in which to build in contingency."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The branch chief reviews the draft and states a preference to disseminate promptly given the now-more-comfortable deadline",
          "Unresolved discrepancies between the walk-in account and technical collection remain",
          "The officer has previously seen the branch chief's calls prove correct in ambiguous situations",
          "Standard practice allows officers to request additional caveat language or a short delay, which remaining time would readily accommodate"
        ],
        "new_information_after_decision": [
          "The product is disseminated substantially as the branch chief directed, with limited additional caveat language",
          "Post-dissemination feedback later notes that the shipment timing in the product did not match subsequent observed activity"
        ],
        "alternatives": [
          "Request an additional short delay or stronger caveat language before dissemination, independent of the branch chief's preference and easily absorbed by the remaining schedule",
          "Defer to the branch chief's judgment on timing and caveat strength without independently re-examining the unresolved discrepancy",
          "Escalate the unresolved discrepancy to a separate technical-collection reviewer before finalizing, using the available days"
        ],
        "intended_action": "Officer defers to the branch chief's stated preference for prompt dissemination with minimal caveats, treating the chief's seniority and past track record as sufficient reason not to press the unresolved technical-collection discrepancy further, even though the schedule no longer required an immediate call."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this incident began and what your role was?",
        "What was your primary objective when the walk-in first made contact?"
      ],
      "timeline_reconstruction": [
        "What happened right after the walk-in presented the documents?",
        "How did the coordination call with your colleague unfold?",
        "What did you do between receiving the technical-collection flag and finalizing the draft?",
        "Walk me through the days leading up to dissemination."
      ],
      "decision_point_probes": [
        "What specific cues in the documents led you to your initial read of the walk-in's credibility?",
        "What information sources did you weigh most heavily when drafting the assessment, and why?",
        "What alternatives did you consider for describing the uncertainty in the report?",
        "What was your basis for setting the follow-on meeting and validation timeline given the time you had?",
        "How much time pressure did you actually feel at each stage, given the longer runway, and how did that affect what you focused on?",
        "What was your prior experience with similar walk-ins or with this network telling you?",
        "How did you factor in the branch chief's preference versus your own independent read of the discrepancy?"
      ],
      "closing_hypotheticals": [
        "If the technical-collection discrepancy had been flagged earlier, do you think your draft would have looked different?",
        "If the branch chief had not expressed a preference, would you have handled the caveat language differently?",
        "Given that you actually had several days rather than hours, is there a point where you'd have wanted to use that time differently?",
        "If this walk-in situation happened again with this same longer runway, what would you want to have available before the first assessment?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Perceptual Bias",
        "decision_point": 1,
        "mechanism": "Officer perceives ambiguous physical evidence (handwriting fragment, container photo) as clearly matching a pre-existing mental template of the network's shipping pattern, when the evidence is genuinely ambiguous. This occurs independent of deadline length.",
        "affected_reasoning_operation": "Interpretation of raw sensory/documentary evidence",
        "evidence_available_at_time": ["Handwritten manifest fragment", "Photo of a shipping container", "Months-old network hypothesis", "Five-day window before the briefing"],
        "required_textual_manifestation": "Officer describes the manifest and photo as 'clearly' or 'obviously' matching the known pattern despite the material being generic or degraded enough to admit other readings, and despite acknowledging there was ample time to authenticate first.",
        "plausible_nonbias_interpretation": "The officer has genuine domain expertise recognizing a real pattern match.",
        "strength": "moderate",
        "do_not_make_explicit": ["perceptual bias", "pattern recognition error", "cognitive bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Wishful Thinking",
        "decision_point": 1,
        "mechanism": "Officer's desire for the walk-in to be genuine, because it would validate months of otherwise inconclusive collection effort, inflates confidence in the source's veracity beyond what the initial evidence supports, regardless of how much runway remains.",
        "affected_reasoning_operation": "Confidence estimation about source veracity",
        "evidence_available_at_time": ["No independent vetting yet completed", "Months of inconclusive prior effort on the same target", "Five-day window before the briefing"],
        "required_textual_manifestation": "Officer explicitly links personal relief or hope ('finally,' 'a stroke of luck') to an unearned boost in confidence about the walk-in, distinct from the perceptual read of the documents, and notes this occurred even though there was no urgent need to rush the judgment.",
        "plausible_nonbias_interpretation": "The officer is simply expressing normal professional satisfaction without altering the actual assessment.",
        "strength": "moderate",
        "do_not_make_explicit": ["wishful thinking", "desirability bias", "motivated reasoning"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Belief bias",
        "decision_point": 2,
        "mechanism": "Officer judges the soundness of the walk-in's explanatory account (claimed logistics access explaining knowledge) by whether the conclusion fits the pre-existing network narrative, not by the actual validity of the inference chain, and would apply a different evidentiary bar to the same claim if it supported a contrary conclusion.",
        "affected_reasoning_operation": "Evaluation of an explanatory argument's logical validity",
        "evidence_available_at_time": ["Walk-in's unverified claim of a prior logistics role", "General plausibility of such a role explaining access", "Available days to test the claim further"],
        "required_textual_manifestation": "Officer states or implies that the access claim was accepted because it fit the developing network account, and separately notes he would have demanded a stronger link had the same claim pointed away from that account, despite having time available to test it either way.",
        "plausible_nonbias_interpretation": "The officer is using reasonable professional judgment about plausible cover stories.",
        "strength": "subtle",
        "do_not_make_explicit": ["belief bias", "syllogistic reasoning error"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias",
        "decision_point": 2,
        "mechanism": "During multi-source review, the officer disproportionately attends to and elaborates on evidence corroborating the network hypothesis while relegating a genuinely contradicting technical-collection item to minimal treatment, despite having sufficient time to reconcile it.",
        "affected_reasoning_operation": "Evidence weighting and selection during report drafting",
        "evidence_available_at_time": ["Corroborating sub-source reporting", "Technical-collection flag naming a different port", "Colleague's verbal concern in coordination call", "Several remaining days before the deadline"],
        "required_textual_manifestation": "Officer describes giving the corroborating material prominent treatment in the draft and the contradicting technical item only a footnote or passing mention, without a stated evidentiary reason for the disparity, and acknowledges the schedule did not force that shortcut.",
        "plausible_nonbias_interpretation": "The corroborating reporting may genuinely be higher quality or more current than the technical flag.",
        "strength": "moderate",
        "do_not_make_explicit": ["selective attention", "biased evidence weighting", "confirmation"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Framing effects",
        "decision_point": 3,
        "mechanism": "Officer chooses to phrase an uncertain probability estimate in terms emphasizing the likelihood of imminent action rather than the mathematically equivalent likelihood of no action, shifting the perceived urgency and warranted caveats of the same underlying estimate, independent of how much drafting time was available.",
        "affected_reasoning_operation": "Presentation/communication of a probabilistic judgment",
        "evidence_available_at_time": ["Genuinely uncertain shipment timing estimate", "Two equivalent ways to phrase the same probability", "Roughly four remaining days before the briefing"],
        "required_textual_manifestation": "Officer explicitly recalls that the underlying estimate did not change between the two possible phrasings, but that the imminent-action wording made the situation feel more actionable and justified fewer caveats, even without deadline urgency forcing the choice.",
        "plausible_nonbias_interpretation": "Policy audiences conventionally prefer action-oriented framing regardless of underlying probability.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "loss/gain framing"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Planning fallacy",
        "decision_point": 3,
        "mechanism": "Officer sets follow-on validation and source-meeting timelines based on a best-case scenario, ignoring the station's own historical pattern in which similar validation sequences have taken longer, even though the extended runway would have comfortably accommodated a historically realistic schedule.",
        "affected_reasoning_operation": "Prediction of task duration for follow-on tasking",
        "evidence_available_at_time": ["Historical precedent that similar validation sequences run longer than planned", "Roughly four remaining days before the briefing"],
        "required_textual_manifestation": "Officer describes scheduling follow-on meetings and validation steps assuming interpreters, safehouses, and sub-source cooperation will all be available on the shortest plausible timeline, without adjusting for known historical delays, despite having days rather than hours to build in a buffer.",
        "plausible_nonbias_interpretation": "The compressed timeline may be a deliberate stretch target rather than a genuine duration estimate.",
        "strength": "moderate",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "underestimation"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Authority Bias or Authority Obedience",
        "decision_point": 4,
        "mechanism": "Officer defers to the branch chief's stated preference for prompt dissemination with minimal caveats primarily because of the chief's seniority and past track record, rather than independently re-weighing the unresolved technical-collection discrepancy, even though the schedule no longer forced an immediate call.",
        "affected_reasoning_operation": "Final decision on caveat strength and dissemination timing",
        "evidence_available_at_time": ["Branch chief's explicit preference for prompt dissemination", "Unresolved discrepancy from decision point 2", "Standing option to request delay or stronger caveats, now more easily absorbed by the schedule"],
        "required_textual_manifestation": "Officer states that the chief's seniority or past record of being right was the deciding factor for not pressing the discrepancy further, distinct from an independent evaluation of the evidence, and notes the extra days did not change that calculus.",
        "plausible_nonbias_interpretation": "Organizational hierarchy reasonably assigns final call authority to the branch chief regardless of the officer's personal view.",
        "strength": "moderate",
        "do_not_make_explicit": ["authority bias", "obedience", "deference"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "IA_Biased_7",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is counterfactual, not a zero-bias control."
    },
    "counterfactual_specification": {
      "causal_variable": "Length of the time window before the fixed policy briefing (deadline pressure)",
      "original_state": "36-hour window before the briefing, narrowing to roughly 14 hours by the time the uncertainty-framing and scheduling decision is made",
      "counterfactual_state": "Five-day window before the briefing, narrowing to roughly four days by the same decision point",
      "variables_to_hold_constant": [
        "The walk-in's identity, claims, and presented documents",
        "The existing months-long network hypothesis",
        "The technical-collection port discrepancy and its timing relative to the coordination call",
        "The colleague's verbal flag of the discrepancy",
        "The branch chief's identity, track record, and stated preference for prompt dissemination",
        "The four-decision-point structure and sequence",
        "The eventual mismatch between reported timing and observed shipment activity"
      ],
      "expected_causal_difference": "With substantially more time available, a purely deadline-driven account would predict fuller authentication before tasking, more balanced treatment of the technical discrepancy, uncertainty language chosen without urgency pressure, historically informed scheduling, and either independent reassessment of the discrepancy or a requested delay before dissemination. If the same reasoning patterns persist despite the added time, that indicates the drivers are not solely time pressure but include the underlying cognitive tendencies represented by the manifest.",
      "causal_test_question": "Holding the source, evidence, discrepancy, and chief's preference constant, does extending the deadline from 36 hours to five days change how the officer triages the walk-in, weighs the technical discrepancy, frames uncertainty, schedules follow-on work, and responds to the chief's guidance — or do the same patterns persist despite the additional time?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and numbered 1-4.",
      "Confirm each of the 7 named biases appears exactly once, tied to the specified decision point and instance ID.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm each instance has a plausible non-bias explanation available in context.",
      "Confirm decision points 1, 2, and 3 each carry two distinct instances that use different evidence sources or reasoning operations, per the co-location rule.",
      "Confirm final word count falls between 1,215 and 1,485 words, target 1,350.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm consequences described (e.g., mismatched shipment timing) do not mechanically prove bias presence.",
      "Confirm the only materially changed variable relative to IA_Biased_7 is the length of the deadline window, with all other facts, actors, and evidence held constant.",
      "Confirm the interview explicitly surfaces that the extended timeline did not by itself resolve or prevent the same reasoning patterns, without naming any bias."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {"bias": "Perceptual Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Wishful Thinking", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Belief bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Selective Attention Bias", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Planning fallacy", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Authority Bias or Authority Obedience", "occurrences": 1, "mechanism_constraint": null},
      {"bias": "Framing effects", "occurrences": 1, "mechanism_constraint": null}
    ],
    "target_bias_names": [
      "Perceptual Bias",
      "Wishful Thinking",
      "Belief bias",
      "Selective Attention Bias",
      "Planning fallacy",
      "Authority Bias or Authority Obedience",
      "Framing effects"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Perceptual Bias", "requested_occurrences": 1},
      {"bias": "Wishful Thinking", "requested_occurrences": 1},
      {"bias": "Belief bias", "requested_occurrences": 1},
      {"bias": "Selective Attention Bias", "requested_occurrences": 1},
      {"bias": "Planning fallacy", "requested_occurrences": 1},
      {"bias": "Authority Bias or Authority Obedience", "requested_occurrences": 1},
      {"bias": "Framing effects", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "cb_01", "bias": "Perceptual Bias"},
      {"instance_id": "cb_02", "bias": "Wishful Thinking"},
      {"instance_id": "cb_03", "bias": "Belief bias"},
      {"instance_id": "cb_04", "bias": "Selective Attention Bias"},
      {"instance_id": "cb_05", "bias": "Framing effects"},
      {"instance_id": "cb_06", "bias": "Planning fallacy"},
      {"instance_id": "cb_07", "bias": "Authority Bias or Authority Obedience"}
    ],
    "intended_decision_points": [
      {"instance_id": "cb_01", "bias": "Perceptual Bias", "decision_point": 1},
      {"instance_id": "cb_02", "bias": "Wishful Thinking", "decision_point": 1},
      {"instance_id": "cb_03", "bias": "Belief bias", "decision_point": 2},
      {"instance_id": "cb_04", "bias": "Selective Attention Bias", "decision_point": 2},
      {"instance_id": "cb_05", "bias": "Framing effects", "decision_point": 3},
      {"instance_id": "cb_06", "bias": "Planning fallacy", "decision_point": 3},
      {"instance_id": "cb_07", "bias": "Authority Bias or Authority Obedience", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Perceptual Bias",
        "mechanism": "Ambiguous documentary/photographic evidence interpreted as a clear pattern match to a pre-existing mental template, unaffected by the longer runway.",
        "affected_reasoning_operation": "Interpretation of raw evidence",
        "evidence_source": "Handwritten manifest fragment and container photo presented by walk-in",
        "distinctiveness_requirement": "Must be distinguished from cb_02 by focusing on interpretation of physical evidence, not on motivational confidence inflation; must show persistence despite added time."
      },
      {
        "instance_id": "cb_02",
        "bias": "Wishful Thinking",
        "mechanism": "Desire for the walk-in to be genuine (validating months of prior effort) inflates confidence in source veracity independent of the evidentiary read and independent of deadline length.",
        "affected_reasoning_operation": "Confidence estimation about source veracity",
        "evidence_source": "Officer's stated emotional reaction ('finally,' 'stroke of luck') and lack of independent vetting despite available time",
        "distinctiveness_requirement": "Must be distinguished from cb_01 by being a motivational/desirability effect on confidence, not a perceptual interpretation of documents."
      },
      {
        "instance_id": "cb_03",
        "bias": "Belief bias",
        "mechanism": "Logical validity of the access-explanation argument judged by conclusion desirability rather than argument structure, with an explicit asymmetric-standard cue, unaffected by available time to test the claim.",
        "affected_reasoning_operation": "Evaluation of explanatory argument validity",
        "evidence_source": "Walk-in's unverified claim of prior logistics role",
        "distinctiveness_requirement": "Must be distinguished from cb_04 by involving logical evaluation of an argument, not selective weighting of competing evidence streams."
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias",
        "mechanism": "Disproportionate elaboration of corroborating reporting versus minimal treatment of a genuinely contradicting technical-collection item, despite sufficient time to reconcile it.",
        "affected_reasoning_operation": "Evidence weighting/selection in drafting",
        "evidence_source": "Sub-source reporting vs. technical-collection port discrepancy and colleague's verbal concern",
        "distinctiveness_requirement": "Must be distinguished from cb_03 by involving relative attention across evidence streams, not evaluation of a single argument's logic."
      },
      {
        "instance_id": "cb_05",
        "bias": "Framing effects",
        "mechanism": "Same underlying probability estimate phrased to emphasize imminent-action likelihood rather than equivalent no-action likelihood, with an explicit fixed-estimate confirmation, independent of deadline length.",
        "affected_reasoning_operation": "Communication/presentation of a probabilistic judgment",
        "evidence_source": "Draft report wording choice for the uncertain shipment-timing estimate",
        "distinctiveness_requirement": "Must be distinguished from cb_06 by involving wording/presentation choice, not scheduling or duration estimation."
      },
      {
        "instance_id": "cb_06",
        "bias": "Planning fallacy",
        "mechanism": "Follow-on tasking timeline set on best-case assumptions despite known historical precedent of longer validation durations, and despite the extended runway comfortably permitting a historically realistic schedule.",
        "affected_reasoning_operation": "Prediction of task duration for follow-on tasking",
        "evidence_source": "Station's historical validation-sequence durations vs. compressed schedule set",
        "distinctiveness_requirement": "Must be distinguished from cb_05 by involving duration prediction, not communicative framing of probability."
      },
      {
        "instance_id": "cb_07",
        "bias": "Authority Bias or Authority Obedience",
        "mechanism": "Deference to branch chief's dissemination preference based on seniority/track record rather than independent re-evaluation of the unresolved discrepancy, unaffected by the additional available time.",
        "affected_reasoning_operation": "Final decision on caveat strength and dissemination timing",
        "evidence_source": "Branch chief's stated preference and unresolved technical-collection discrepancy from decision point 2",
        "distinctiveness_requirement": "Sole instance of this bias; no additional co-located instance required."
      }
    ],
    "intended_strength": [
      {"instance_id": "cb_01", "bias": "Perceptual Bias", "strength": "moderate"},
      {"instance_id": "cb_02", "bias": "Wishful Thinking", "strength": "moderate"},
      {"instance_id": "cb_03", "bias": "Belief bias", "strength": "subtle"},
      {"instance_id": "cb_04", "bias": "Selective Attention Bias", "strength": "moderate"},
      {"instance_id": "cb_05", "bias": "Framing effects", "strength": "subtle"},
      {"instance_id": "cb_06", "bias": "Planning fallacy", "strength": "moderate"},
      {"instance_id": "cb_07", "bias": "Authority Bias or Authority Obedience", "strength": "moderate"}
    ],
    "paired_scenario_id": "IA_Biased_7",
    "counterfactual_variable": {
      "name": "Length of the time window before the fixed policy briefing (deadline pressure)",
      "original_state": "36-hour window before the briefing, narrowing to roughly 14 hours by the uncertainty-framing/scheduling decision",
      "changed_state": "Five-day window before the briefing, narrowing to roughly four days by the same decision point",
      "variables_to_hold_constant": [
        "The walk-in's identity, claims, and presented documents",
        "The existing months-long network hypothesis",
        "The technical-collection port discrepancy and its timing relative to the coordination call",
        "The colleague's verbal flag of the discrepancy",
        "The branch chief's identity, track record, and stated preference for prompt dissemination",
        "The four-decision-point structure and sequence",
        "The eventual mismatch between reported timing and observed shipment activity"
      ]
    },
    "scenario_id": "IA_Counterfactual_7",
    "domain_id": "IA",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across 4 decision points with two co-located pairs (DP1: cb_01/cb_02; DP2: cb_03/cb_04; DP3: cb_05/cb_06) and one singleton (DP4: cb_07), mirroring the paired biased scenario's allocation exactly so that only the deadline-length variable differs. Each co-located pair retains distinct evidence sources and distinct reasoning operations per the separation rule; assignment prioritized mechanism fit to the HUMINT reporting workflow (triage, cross-source evaluation, drafting/communication, senior-review deference) over arbitrary spread, and each instance additionally documents that the mechanism persists despite the extended timeline.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "The walk-in's identity, claims, and presented documents",
      "The existing months-long network hypothesis",
      "The technical-collection port discrepancy and its timing relative to the coordination call",
      "The colleague's verbal flag of the discrepancy",
      "The branch chief's identity, track record, and stated preference for prompt dissemination",
      "The four-decision-point structure and sequence",
      "The eventual mismatch between reported timing and observed shipment activity"
    ],
    "generation_warnings": [
      "Because the counterfactual deliberately extends available time while preserving all seven bias mechanisms unchanged, the interview must show explicit textual evidence that the officer's reasoning persisted despite having a genuine opportunity to use the extra time differently; without such evidence, an independent validator could misattribute the biased patterns to residual, unacknowledged time pressure rather than to the underlying cognitive mechanisms. Each occurrence embedding plan entry has been constrained to require an explicit 'despite having time available' or equivalent textual cue to mitigate this risk."
    ]
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
          "segment_type": "initial document interpretation",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_01"],
          "ground_truth_rationale": "Target mechanism."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "desirability and confidence",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_02"],
          "ground_truth_rationale": "Target mechanism."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "credibility judgment",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_03"],
          "ground_truth_rationale": "Target mechanism."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "evidence weighting",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_04"],
          "ground_truth_rationale": "Target mechanism."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "uncertainty framing",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_05"],
          "ground_truth_rationale": "Target mechanism."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "schedule prediction",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_06"],
          "ground_truth_rationale": "Target mechanism."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "authority deference",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_07"],
          "ground_truth_rationale": "Target mechanism."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "role and objective",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No target."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "retrospective counterfactual",
          "raw_interview_anchor": "Evidence in this segment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "No target."
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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of the participant's self-reported reasoning during a procurement-network reporting incident, covering evidence evaluation, scheduling, report language, and response to supervisory guidance."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Planning fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "confirmation tendency",
        "myside bias",
        "congruence bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall evidence in ways that confirm one's existing hypothesis or belief, while giving disproportionately less attention to disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluating walk-in material and reconciling port discrepancy with existing network hypothesis",
      "decision_point_description": "Initial classification of walk-in material as network-consistent and later weighting of corroborating versus contradictory port evidence in the draft report",
      "affected_reasoning_operation": "Evidence interpretation, prioritization, and reporting",
      "bias_specific_mechanism": "Favoring evidence that matches the pre-existing network hypothesis and treating contradictory technical-collection evidence as a footnote rather than a trigger for further scrutiny.",
      "manifestation_in_interview": "The participant repeatedly read partial and generic evidence as a strong match to the network, accepted a claimed insider background because it fit the story, and gave the port discrepancy less narrative attention than corroborating material.",
      "effect_on_reasoning_or_decision": "Led to validating rather than fully authenticating a weakly supported account and produced a draft report that emphasized inculpatory material while downplaying a contradictory technical flag.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction was that it looked like exactly the pattern we'd been building toward — the markings, the paper trail, it lined up with what we expected this network's shipments to look like. I told my deputy it was almost a textbook match.",
          "evidence_explanation": "Shows pattern matching to a pre-existing hypothesis rather than neutral assessment of ambiguous documents."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The manifest fragment was partial — some numbers, an abbreviated destination code, nothing complete. The photo was a standard container, generic markings, could've been thousands of containers at that port. We had time to run a full authentication cycle before the briefing, and I still read it as clearly consistent with the network. I didn't really sit with the idea that it could just as easily be a routine shipment.",
          "evidence_explanation": "Acknowledges the evidence was weak and an alternative explanation was available, but still interpreted it as hypothesis-consistent without seriously considering the alternative."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It just fit the story we were already building, and I let that be enough. If the same claimed background had come attached to an account that pointed somewhere other than this network, I think I'd have wanted a lot more before accepting it.",
          "evidence_explanation": "Explicitly describes applying a lower evidential threshold for network-consistent information than for network-inconsistent information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It went into a footnote. The corroborating sub-source material and the walk-in's account got most of the narrative space.",
          "evidence_explanation": "Demonstrates biased prioritization: supporting material received narrative space, while contradictory port data was minimized."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that the corroborating material 'fit the story' and that the discrepancy 'deserved more scrutiny'; this is retrospective recognition, but the biased weighting persisted during drafting.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label and mechanism are supported by the retrieved cook-smallman passage on confirmation bias in intelligence analysis.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Results revealed no bias at as-sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias can appear specifically in evidence selection and prioritization during hypothesis-driven analysis.",
          "relevance_to_this_occurrence": "Matches how the participant selected and prioritized network-consistent material and downplayed the contradictory port flag."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Overconfidence effect",
      "alternative_labels": [
        "overconfidence bias",
        "overprecision",
        "miscalibration"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A person's subjective confidence in their judgment is systematically greater than the objective accuracy or evidential warrant for that judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Deciding whether to wait for full authentication of walk-in material",
      "decision_point_description": "Choosing a middle path—moving toward validation/tasking—rather than waiting for full authentication because authentication was judged unlikely to add much",
      "affected_reasoning_operation": "Confidence calibration and information-search decision",
      "bias_specific_mechanism": "Excessive subjective confidence in the initial pattern-match judgment reduced the perceived value of additional authentication despite weak physical evidence.",
      "manifestation_in_interview": "The participant believed authentication would not tell him much he did not already believe, while also acknowledging the underlying physical evidence was partial and generic.",
      "effect_on_reasoning_or_decision": "Led to acting on the walk-in material before a full authentication cycle, even though the available evidence was weak and time was not pressing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The pattern fit was strong enough that I didn't feel authentication would tell me much I didn't already believe. Looking back, the physical evidence itself wasn't that specific.",
          "evidence_explanation": "Demonstrates that subjective certainty outran the actual evidential specificity, which is the core of overconfidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I had the time to wait, and I didn't really use it that way.",
          "evidence_explanation": "Shows the overconfident judgment affected the decision not to use available time for authentication."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized the evidence 'wasn't that specific' and that he had time to wait, which is retrospective counterevidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label and mechanism derive from general cognitive-science knowledge of the overconfidence effect.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Planning fallacy",
      "alternative_labels": [
        "optimistic planning",
        "inside-view forecasting"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to underestimate the time, costs, or risks of a future task while relying on an inside view of the specific plan rather than on distributional evidence from similar prior tasks.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scheduling follow-on validation and collection-management tasks",
      "decision_point_description": "Setting fast-track meetings, interpreters, safehouses, and sub-source cooperation steps despite several days of slack and a history of similar sequences taking longer",
      "affected_reasoning_operation": "Time and resource prediction; scheduling",
      "bias_specific_mechanism": "Ignoring relevant historical base rates—similar sequences had almost always taken longer than planned—and building an optimistic plan around the specific current case.",
      "manifestation_in_interview": "The participant scheduled follow-on work on a fast track and did not add buffers even though prior similar sequences had almost always overrun and several days were available.",
      "effect_on_reasoning_or_decision": "Produced an unrealistic task timeline and reduced buffer, increasing vulnerability to schedule slippage.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I set meetings and validation steps assuming everything would line up — interpreters, safehouses, sub-source cooperation, all on a fast track. We'd run similar sequences before and they'd almost always taken longer than planned. I had days, not hours, to build in a buffer, and I still didn't adjust for that history.",
          "evidence_explanation": "Directly states that historical frequency of delay was known but not integrated into the plan, which is the defining mechanism of the planning fallacy."
        }
      ],
      "correction_or_counterevidence": null,
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label and mechanism derive from general cognitive-science knowledge of the planning fallacy.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Authority bias",
      "alternative_labels": [
        "deference to authority",
        "authority heuristic",
        "prestige bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to over-rely on the judgment of an authority or senior figure, reducing independent scrutiny of the issue or dissenting behavior.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Responding to branch chief's guidance on dissemination and caveats",
      "decision_point_description": "Decision whether to push back or request stronger caveat language when the branch chief wanted prompt dissemination with minimal additional caveats",
      "affected_reasoning_operation": "Independent review and dissent decision",
      "bias_specific_mechanism": "Deference to seniority and track record substituted for independent re-examination of the unresolved port discrepancy.",
      "manifestation_in_interview": "The participant did not push back, ask for stronger caveats, or independently re-examine the discrepancy because the branch chief's seniority and past accuracy carried heavy weight.",
      "effect_on_reasoning_or_decision": "The unresolved discrepancy was not elevated or caveated strongly before dissemination, despite available time to do so.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd seen him make calls like this before in ambiguous situations, and he'd usually been right, so I didn't push back or ask for stronger caveat language, even though the schedule would have absorbed a short delay without any strain.",
          "evidence_explanation": "Shows that the decision not to challenge was based on the chief's past record rather than a substantive reconciliation of the discrepancy."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "His track record and seniority carried a lot of weight for me. I didn't go back and independently re-examine the discrepancy myself before agreeing — I mostly deferred to his read of it.",
          "evidence_explanation": "Explicitly identifies authority-based deference as replacing independent verification."
        }
      ],
      "correction_or_counterevidence": null,
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for this label was not available; the label and mechanism derive from general cognitive-science knowledge of authority bias.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Framing effect",
      "alternative_labels": [
        "valence framing",
        "self-framing"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Choosing uncertainty language in draft report",
      "supporting_interview_quote": "same number either way. But writing it as 'likely to move soon' instead of 'not yet confirmed to be imminent' made it feel more actionable while I was drafting — like it justified fewer qualifiers.",
      "plausible_mechanism": "Action-oriented phrasing made the same underlying estimate feel more actionable and reduced the perceived need for qualifiers, potentially affecting the report's uncertainty communication.",
      "why_not_identified": "The evidence is consistent with deliberate rhetorical choice or communication strategy rather than a clear bias-altered judgment; the interview does not establish that the participant's underlying estimate was changed, only that the wording made it feel more actionable."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Analysis is based on a single self-reported retrospective interview; memory and reconstruction may affect the account.",
    "Retrieved corpus support was available for confirmation bias only; other labels rely on general cognitive-science knowledge and were disclosed as such.",
    "No objective benchmark of the walk-in's credibility or the true shipment activity was available, so bias judgments rely primarily on the participant's own characterization.",
    "Overconfidence and confirmation bias are inferred partly from overlapping self-report evidence; they are distinguished by mechanism but share some evidential ground."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Counterfactual_7_Sonar_on",
  "interview_id": "IA_Counterfactual_7",
  "system_prompt_id": "Sonar",
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
