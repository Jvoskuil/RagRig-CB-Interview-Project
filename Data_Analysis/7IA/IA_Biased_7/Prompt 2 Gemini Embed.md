You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the procurement network reporting incident from earlier this year in detail, including your own decision-making, and that this is for internal process review rather than any kind of performance evaluation.

Participant: Yeah, that's fine. I figured we'd get to that one eventually.

Interviewer: Can you give me your role and a quick sense of what this incident was?

Participant: I'm a reports officer, I also handle collection management for our part of the station. This case was a walk-in who showed up claiming to know about a shipment tied to a procurement network we'd been chasing for months. It turned into a pretty compressed reporting cycle because we had a policy briefing coming up fast.

Interviewer: Let's start with the incident itself. Walk me through how it began.

Participant: So this network had been frustrating us for a while — lots of partial reporting, nothing that let us really nail down how they were moving material. Then out of nowhere, a walk-in comes into the local office claiming direct knowledge of an imminent shipment. He had a handwritten fragment that looked like part of a manifest, and a photo of a shipping container. Honestly, my first reaction was that this looked like exactly the pattern we'd been building toward — the container markings, the paper trail, it all lined up with what we expected this network's shipments to look like. I remember telling my deputy it was almost a textbook match.

Interviewer: What did the documents actually show, as best you recall?

Participant: The manifest fragment was partial — some numbers, an abbreviated destination code, nothing complete. The photo was a standard container, generic markings, could've been thousands of containers at that port. But given everything we'd already built on this target, it read to me as clearly consistent. I didn't really entertain that it could just as easily be a routine shipment.

Interviewer: How did you feel at that point, beyond the analytical read?

Participant: If I'm honest, there was relief. We'd put months into this with basically nothing to show, and here's someone walking in with exactly the kind of specificity we'd been missing. I remember thinking, finally, this is the break. That colored how quickly I moved to request expedited document validation instead of sitting with the uncertainty a bit longer.

Interviewer: Let's reconstruct the timeline from there. What happened after the walk-in session?

Participant: I drafted debrief notes describing him as consistent with the network hypothesis and pushed for expedited validation. Around the same time, we had a coordination call with technical collection folks, and that's when a colleague flagged that their data showed activity at a different port than the one the walk-in named. Then I spent the next stretch drafting the report itself, and the final hours before the briefing were spent finalizing language and setting up follow-on tasking.

Interviewer: Let's go back to that first decision — accepting the walk-in's material as consistent with the network hypothesis versus treating him as fully unvetted. What were your alternatives?

Participant: Technically I had three options: treat him as an unvetted contact needing full standard validation before any tasking, treat the material as a strong match and move to tasking right away, or defer any assessment twenty-four hours for basic authentication. I went with the middle path, more or less.

Interviewer: What made the middle path more compelling than waiting for authentication?

Participant: The pattern fit was strong enough that I didn't feel authentication would tell me anything I didn't already believe. Looking back, that's probably generous — the physical evidence itself wasn't that specific. But it matched the shape of what we expected, and given how long we'd been at this, waiting felt like it was leaving value on the table.

Interviewer: Second decision point — reconciling the walk-in's account with the technical collection discrepancy about the port. What did you weigh there?

Participant: The walk-in claimed he'd had a prior logistics role, which would explain how he'd know shipment details. That struck me as the kind of detail a real insider would know, not something you'd fabricate. So I leaned toward treating his account as substantially credible on that basis. Honestly, the claim on its own didn't prove he knew anything about this particular shipment — it just made the story fit together the way I already expected it to, so I let it stand as enough. If that same claimed logistics background had come attached to an account that pointed away from the network we'd been building the case on, I probably would have wanted a lot more before accepting it. Meanwhile the port discrepancy from technical collection was sitting there, and my colleague raised it directly on the call.

Interviewer: How did that discrepancy factor into the draft?

Participant: It went into a footnote. The corroborating sub-source reporting and the walk-in's account got the bulk of the narrative treatment. I didn't have a strong evidentiary reason to downgrade the technical flag — if anything it deserved more scrutiny — but it just didn't get the same space in my head at that point.

Interviewer: What was driving that imbalance in attention, would you say?

Participant: Partly deadline pressure. Partly that the corroborating material fit the story we were already building, so it took less effort to write up. The port discrepancy would have required unwinding something, and I didn't have time to unwind it properly.

Interviewer: Third decision point — how you described the uncertainty in the report itself, and how you scheduled the follow-on work. Walk me through that.

Participant: The shipment timing estimate had real uncertainty in it. I could have written it either way — emphasizing what we didn't know and what might undercut the assessment, or emphasizing the probability that the network would move soon. I went with language that stressed the chance of imminent action. It read as more useful for a policy audience with fourteen hours to go.

Interviewer: Just to pin that down — was the actual underlying estimate any different depending on which way you phrased it, or was it the same number either way?

Participant: Same number, same underlying picture. Nothing in the estimate itself changed. But writing it as "likely to move soon" instead of "not confirmed to move imminently" made the whole thing feel more actionable to me as I was drafting it — like it justified moving forward with fewer qualifiers than I probably would have used if I'd framed it the other way.

Interviewer: And the follow-on tasking timeline?

Participant: I set meetings and validation steps assuming everything would line up — interpreter availability, safehouse access, sub-source cooperation, all on a fast track. We'd run similar validation sequences before and they'd almost always taken longer than planned, but I didn't build that history into the schedule this time. The deadline was right there, so I planned for the version where things went smoothly.

Interviewer: Fourth decision point — the branch chief's push to disseminate. What happened?

Participant: My chief reviewed the draft and wanted it out the door as-is, minimal additional caveats, given the deadline. The port discrepancy was still unresolved at that point. I'd seen him make calls like this before in ambiguous situations, and he'd usually been right. So I didn't push back or request the extra caveat language I probably could have asked for.

Interviewer: What was the deciding factor in not pushing back?

Participant: Honestly, his track record and seniority carried a lot of weight for me in that moment. I didn't go back and independently re-examine the discrepancy myself before agreeing — I mostly deferred to his read of the situation.

Interviewer: What happened after dissemination?

Participant: The product went out largely as he wanted. Afterward, the observed shipment activity didn't line up with the timing we'd put in the report.

Interviewer: If the port discrepancy had surfaced earlier, before your first read of the walk-in, do you think your draft would have looked different?

Participant: Maybe. I'd like to think I'd have weighed it more evenly from the start rather than treating it as something to explain away later.

Interviewer: If your chief hadn't expressed a preference on dissemination, would you have handled the caveats differently?

Participant: Possibly stronger caveats, or at least a harder look at the discrepancy before signing off. Hard to say for certain.

Interviewer: Looking back, is there a point where you'd have wanted more time, regardless of the deadline?

Participant: The very first read of the documents. I moved to expedited validation pretty fast instead of sitting with the ambiguity.

Interviewer: Last one — if this kind of walk-in situation happened again, what would you want in place beforehand?

Participant: Probably a standing rule to get an independent second read on ambiguous physical evidence before it shapes the rest of the reporting cycle, and more discipline about building historical timelines into follow-on scheduling instead of assuming best case.

Interviewer: That's really helpful context. Thank you for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Biased_7",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Human Intelligence (HUMINT) Collection Manager/Reports Officer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Walk-In and the Deadline: Procurement Network Reporting Under Pressure",
    "scenario_summary_internal": "A HUMINT Collection Manager/Reports Officer at a forward station receives an unvetted walk-in source claiming knowledge of an imminent illicit dual-use technology shipment tied to a procurement network the station has tracked for months. With a senior-level policy briefing due within 36 hours, the officer must triage the source, reconcile the claim against existing multi-source reporting, draft a time-sensitive product, and respond to a senior officer's push to disseminate before all discrepancies are resolved.",
    "occupational_realism": {
      "objective": "Determine whether the walk-in's claim about an imminent shipment is credible enough to redirect collection resources and to include in a policy-relevant intelligence product before a fixed briefing deadline.",
      "setting": "A regional HUMINT station supporting a task force on dual-use technology proliferation, operating under normal reporting cadence but facing an unscheduled walk-in contact and an externally fixed briefing deadline.",
      "constraints": [
        "36-hour window before a senior policymaker briefing",
        "Limited independent means to vet the walk-in source's access and motivation in the time available",
        "Competing tasking requirements on the same technical collection assets",
        "Partial, sometimes contradictory reporting streams (existing HUMINT network, technical collection, open-source)",
        "Pressure from a senior officer to produce an actionable product quickly"
      ],
      "stakeholders": [
        "The reports officer/collection manager (interviewee)",
        "The walk-in source",
        "An established sub-source network being run for months on the same target",
        "A senior reports officer/branch chief pushing for rapid dissemination",
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
          "The station has spent months building a hypothesis about this same procurement network"
        ],
        "new_information_after_decision": [
          "Initial debrief notes are drafted describing the walk-in as consistent with the existing network hypothesis",
          "A request is submitted to expedite validation of the walk-in's documents"
        ],
        "alternatives": [
          "Treat the walk-in as an unvetted, uncorroborated contact requiring full standard validation before any tasking action",
          "Treat the material as strongly consistent with the prior network hypothesis and move directly to tasking",
          "Defer any assessment for 24 hours pending basic document authentication"
        ],
        "intended_action": "Officer interprets the ambiguous handwriting and container photo as clearly matching the network's known shipping pattern, and separately reflects that the timing is 'a stroke of luck' because it would validate months of otherwise inconclusive effort."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Existing sub-source reporting from the tracked network is ambiguous about shipment timing",
          "Technical collection has flagged activity at a different port than the one named by the walk-in",
          "The walk-in claims a prior logistics role that would explain access, but this claim is unverified",
          "A colleague raises the technical-collection discrepancy in a coordination call"
        ],
        "new_information_after_decision": [
          "The report draft cites the walk-in and sub-source material prominently; the technical-collection discrepancy is mentioned only in a footnote",
          "The colleague's concern is logged but not incorporated into the main assessment"
        ],
        "alternatives": [
          "Weigh the technical-collection discrepancy and the walk-in's account with comparable rigor before drafting",
          "Give primary weight to the reporting that matches the established network hypothesis and treat the discrepancy as secondary",
          "Pause the draft until the port discrepancy is reconciled"
        ],
        "intended_action": "Officer reasons that because the walk-in's claimed logistics background makes the story 'the kind of thing a real insider would know,' the account must be substantially true, and continues to emphasize corroborating threads while the contradicting technical-collection item receives minimal analytic attention."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Briefing deadline is 14 hours away",
          "The estimate of shipment timing carries meaningful residual uncertainty",
          "Two ways exist to describe the same confidence level to the policy audience",
          "Historical timelines for similar validation-and-tasking sequences typically take longer than initially planned"
        ],
        "new_information_after_decision": [
          "The draft language is finalized using an urgency-emphasizing framing of the uncertain timeline",
          "A follow-on tasking and source-meeting schedule is set assuming compressed timeframes"
        ],
        "alternatives": [
          "Present the uncertainty in terms of what is not yet known and what could invalidate the assessment",
          "Present the same uncertainty by emphasizing the probability that the network will act imminently",
          "Build follow-on tasking timelines around historical validation durations rather than the shortest plausible case"
        ],
        "intended_action": "Officer chooses wording that foregrounds the chance of imminent action rather than the chance of no action, and separately schedules follow-on source meetings and validation steps on a compressed timeline that assumes best-case availability of interpreters, safehouses, and sub-source cooperation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The branch chief reviews the draft and states a preference to disseminate immediately given the deadline",
          "Unresolved discrepancies between the walk-in account and technical collection remain",
          "The officer has previously seen the branch chief's calls prove correct in ambiguous situations",
          "Standard practice allows officers to request additional caveat language or a short delay"
        ],
        "new_information_after_decision": [
          "The product is disseminated substantially as the branch chief directed, with limited additional caveat language",
          "Post-dissemination feedback later notes that the shipment timing in the product did not match subsequent observed activity"
        ],
        "alternatives": [
          "Request an additional short delay or stronger caveat language before dissemination, independent of the branch chief's preference",
          "Defer to the branch chief's judgment on timing and caveat strength without independently re-examining the unresolved discrepancy",
          "Escalate the unresolved discrepancy to a separate technical-collection reviewer before finalizing"
        ],
        "intended_action": "Officer defers to the branch chief's stated preference for immediate dissemination with minimal caveats, treating the chief's seniority and past track record as sufficient reason not to press the unresolved technical-collection discrepancy further."
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
        "Walk me through the final hours before dissemination."
      ],
      "decision_point_probes": [
        "What specific cues in the documents led you to your initial read of the walk-in's credibility?",
        "What information sources did you weigh most heavily when drafting the assessment, and why?",
        "What alternatives did you consider for describing the uncertainty in the report?",
        "What was your basis for setting the follow-on meeting and validation timeline?",
        "How much time pressure did you feel at each stage, and how did that affect what you focused on?",
        "What was your prior experience with similar walk-ins or with this network telling you?",
        "How did you factor in the branch chief's preference versus your own independent read of the discrepancy?"
      ],
      "closing_hypotheticals": [
        "If the technical-collection discrepancy had been flagged earlier, do you think your draft would have looked different?",
        "If the branch chief had not expressed a preference, would you have handled the caveat language differently?",
        "Looking back, is there a point where you'd have wanted more time regardless of the deadline?",
        "If this walk-in situation happened again, what would you want to have available before the first assessment?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Perceptual Bias",
        "decision_point": 1,
        "mechanism": "Officer perceives ambiguous physical evidence (handwriting fragment, container photo) as clearly matching a pre-existing mental template of the network's shipping pattern, when the evidence is genuinely ambiguous.",
        "affected_reasoning_operation": "Interpretation of raw sensory/documentary evidence",
        "evidence_available_at_time": ["Handwritten manifest fragment", "Photo of a shipping container", "Months-old network hypothesis"],
        "required_textual_manifestation": "Officer describes the manifest and photo as 'clearly' or 'obviously' matching the known pattern despite the material being generic or degraded enough to admit other readings.",
        "plausible_nonbias_interpretation": "The officer has genuine domain expertise recognizing a real pattern match.",
        "strength": "moderate",
        "do_not_make_explicit": ["perceptual bias", "pattern recognition error", "cognitive bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Wishful Thinking",
        "decision_point": 1,
        "mechanism": "Officer's desire for the walk-in to be genuine, because it would validate months of otherwise inconclusive collection effort, inflates the officer's confidence in the source's veracity beyond what the initial evidence supports.",
        "affected_reasoning_operation": "Confidence estimation about source veracity",
        "evidence_available_at_time": ["No independent vetting yet completed", "Months of inconclusive prior effort on the same target"],
        "required_textual_manifestation": "Officer explicitly links personal relief or hope ('finally,' 'a stroke of luck') to an unearned boost in confidence about the walk-in, distinct from the perceptual read of the documents.",
        "plausible_nonbias_interpretation": "The officer is simply expressing normal professional satisfaction without altering the actual assessment.",
        "strength": "moderate",
        "do_not_make_explicit": ["wishful thinking", "desirability bias", "motivated reasoning"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Belief bias",
        "decision_point": 2,
        "mechanism": "Officer judges the logical soundness of the walk-in's explanatory account (claimed logistics access explaining knowledge) based on whether the conclusion is one the officer already believes, rather than on the actual validity of the inference chain.",
        "affected_reasoning_operation": "Evaluation of an explanatory argument's logical validity",
        "evidence_available_at_time": ["Walk-in's unverified claim of a prior logistics role", "General plausibility of such a role explaining access"],
        "required_textual_manifestation": "Officer states or implies that because the conclusion (source is credible) fits what was already believed about the network, the argument for access must be sound, without separately testing the argument's logical structure.",
        "plausible_nonbias_interpretation": "The officer is using reasonable professional judgment about plausible cover stories.",
        "strength": "subtle",
        "do_not_make_explicit": ["belief bias", "syllogistic reasoning error"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias",
        "decision_point": 2,
        "mechanism": "During multi-source review, the officer disproportionately attends to and elaborates on evidence corroborating the network hypothesis while relegating a genuinely contradicting technical-collection item to minimal treatment.",
        "affected_reasoning_operation": "Evidence weighting and selection during report drafting",
        "evidence_available_at_time": ["Corroborating sub-source reporting", "Technical-collection flag naming a different port", "Colleague's verbal concern in coordination call"],
        "required_textual_manifestation": "Officer describes giving the corroborating material prominent treatment in the draft and the contradicting technical item only a footnote or passing mention, without a stated evidentiary reason for the disparity.",
        "plausible_nonbias_interpretation": "The corroborating reporting may genuinely be higher quality or more current than the technical flag.",
        "strength": "moderate",
        "do_not_make_explicit": ["selective attention", "biased evidence weighting", "confirmation"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Framing effects",
        "decision_point": 3,
        "mechanism": "Officer chooses to phrase an uncertain probability estimate in terms emphasizing the likelihood of imminent action rather than the mathematically equivalent likelihood of no action, shifting the perceived urgency of the same underlying uncertainty.",
        "affected_reasoning_operation": "Presentation/communication of a probabilistic judgment",
        "evidence_available_at_time": ["Genuinely uncertain shipment timing estimate", "Two equivalent ways to phrase the same probability"],
        "required_textual_manifestation": "Officer explicitly recalls choosing wording that stresses the chance the network 'will act imminently' over wording stressing the chance it 'will not act soon,' for the same underlying estimate.",
        "plausible_nonbias_interpretation": "Policy audiences conventionally prefer action-oriented framing regardless of underlying probability.",
        "strength": "subtle",
        "do_not_make_explicit": ["framing effect", "loss/gain framing"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Planning fallacy",
        "decision_point": 3,
        "mechanism": "Officer sets follow-on validation and source-meeting timelines based on a best-case scenario, ignoring the station's own historical pattern in which similar validation sequences have taken longer.",
        "affected_reasoning_operation": "Prediction of task duration for follow-on tasking",
        "evidence_available_at_time": ["Historical precedent that similar validation sequences run longer than planned", "Immediate deadline pressure"],
        "required_textual_manifestation": "Officer describes scheduling follow-on meetings and validation steps assuming interpreters, safehouses, and sub-source cooperation will all be available on the shortest plausible timeline, without adjusting for known historical delays.",
        "plausible_nonbias_interpretation": "The compressed timeline may be a deliberate stretch target rather than a genuine duration estimate.",
        "strength": "moderate",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "underestimation"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Authority Bias or Authority Obedience",
        "decision_point": 4,
        "mechanism": "Officer defers to the branch chief's stated preference for immediate dissemination with minimal caveats primarily because of the chief's seniority and past track record, rather than independently re-weighing the unresolved technical-collection discrepancy.",
        "affected_reasoning_operation": "Final decision on caveat strength and dissemination timing",
        "evidence_available_at_time": ["Branch chief's explicit preference for immediate dissemination", "Unresolved discrepancy from decision point 2", "Standing option to request delay or stronger caveats"],
        "required_textual_manifestation": "Officer states that the chief's seniority or past record of being right was the deciding factor for not pressing the discrepancy further, distinct from an independent evaluation of the evidence.",
        "plausible_nonbias_interpretation": "Organizational hierarchy reasonably assigns final call authority to the branch chief regardless of the officer's personal view.",
        "strength": "moderate",
        "do_not_make_explicit": ["authority bias", "obedience", "deference"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no control pairing requested."
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
      "Confirm exactly 4 decision points are present and numbered 1-4.",
      "Confirm each of the 7 named biases appears exactly once, tied to the specified decision point and instance ID.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the public interview text.",
      "Confirm each instance has a plausible non-bias explanation available in context.",
      "Confirm decision points 1, 2, and 3 each carry two distinct instances that use different evidence sources or reasoning operations, per the co-location rule.",
      "Confirm final word count falls between 1,215 and 1,485 words, target 1,350.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes.",
      "Confirm consequences described (e.g., mismatched shipment timing) do not mechanically prove bias presence."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
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
        "mechanism": "Ambiguous documentary/photographic evidence interpreted as a clear pattern match to a pre-existing mental template.",
        "affected_reasoning_operation": "Interpretation of raw evidence",
        "evidence_source": "Handwritten manifest fragment and container photo presented by walk-in",
        "distinctiveness_requirement": "Must be distinguished from cb_02 by focusing on interpretation of physical evidence, not on motivational confidence inflation."
      },
      {
        "instance_id": "cb_02",
        "bias": "Wishful Thinking",
        "mechanism": "Desire for the walk-in to be genuine (validating months of prior effort) inflates confidence in source veracity independent of the evidentiary read.",
        "affected_reasoning_operation": "Confidence estimation about source veracity",
        "evidence_source": "Officer's stated emotional reaction ('finally,' 'stroke of luck') and lack of independent vetting",
        "distinctiveness_requirement": "Must be distinguished from cb_01 by being a motivational/desirability effect on confidence, not a perceptual interpretation of documents."
      },
      {
        "instance_id": "cb_03",
        "bias": "Belief bias",
        "mechanism": "Logical validity of the access-explanation argument judged by conclusion desirability rather than argument structure.",
        "affected_reasoning_operation": "Evaluation of explanatory argument validity",
        "evidence_source": "Walk-in's unverified claim of prior logistics role",
        "distinctiveness_requirement": "Must be distinguished from cb_04 by involving logical evaluation of an argument, not selective weighting of competing evidence streams."
      },
      {
        "instance_id": "cb_04",
        "bias": "Selective Attention Bias",
        "mechanism": "Disproportionate elaboration of corroborating reporting versus minimal treatment of a genuinely contradicting technical-collection item.",
        "affected_reasoning_operation": "Evidence weighting/selection in drafting",
        "evidence_source": "Sub-source reporting vs. technical-collection port discrepancy and colleague's verbal concern",
        "distinctiveness_requirement": "Must be distinguished from cb_03 by involving relative attention across evidence streams, not evaluation of a single argument's logic."
      },
      {
        "instance_id": "cb_05",
        "bias": "Framing effects",
        "mechanism": "Same underlying probability estimate phrased to emphasize imminent-action likelihood rather than equivalent no-action likelihood.",
        "affected_reasoning_operation": "Communication/presentation of a probabilistic judgment",
        "evidence_source": "Draft report wording choice for the uncertain shipment-timing estimate",
        "distinctiveness_requirement": "Must be distinguished from cb_06 by involving wording/presentation choice, not scheduling or duration estimation."
      },
      {
        "instance_id": "cb_06",
        "bias": "Planning fallacy",
        "mechanism": "Follow-on tasking timeline set on best-case assumptions despite known historical precedent of longer validation durations.",
        "affected_reasoning_operation": "Prediction of task duration for follow-on tasking",
        "evidence_source": "Station's historical validation-sequence durations vs. compressed schedule set",
        "distinctiveness_requirement": "Must be distinguished from cb_05 by involving duration prediction, not communicative framing of probability."
      },
      {
        "instance_id": "cb_07",
        "bias": "Authority Bias or Authority Obedience",
        "mechanism": "Deference to branch chief's dissemination preference based on seniority/track record rather than independent re-evaluation of the unresolved discrepancy.",
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
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_7",
    "domain_id": "IA",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences distributed across 4 decision points with two co-located pairs (DP1: cb_01/cb_02; DP2: cb_03/cb_04; DP3: cb_05/cb_06) and one singleton (DP4: cb_07). Each co-located pair uses distinct evidence sources and distinct reasoning operations per the separation rule; no decision point holds more than two instances of any single bias (each bias here has only one total instance, so this ceiling is trivially satisfied); assignment prioritized mechanism fit to the HUMINT reporting workflow (triage, cross-source evaluation, drafting/communication, senior-review deference) over arbitrary spread.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focused on the participant's reported reasoning during the procurement network reporting incident. Occurrences were identified only where the transcript provided affirmative mechanism-level evidence of cognitive distortion."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "Framing effect",
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
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["confirmatory bias", "myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in a way that confirms or strengthens one's pre-existing beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial assessment of walk-in material and expedited validation decision",
      "decision_point_description": "Choosing whether to treat the walk-in as unvetted pending full validation, as a strong match warranting expedited tasking, or to defer assessment for authentication.",
      "affected_reasoning_operation": "Evidence interpretation and initial validation decision",
      "bias_specific_mechanism": "The participant interpreted fragmentary and generic physical evidence as a near-textbook match to the existing network hypothesis, explicitly discounting the alternative that it could be a routine shipment. The prior hypothesis made the evidence feel more specific than it was, and this drove the decision to expedite validation rather than sit with ambiguity.",
      "manifestation_in_interview": "The participant described the walk-in material as matching the expected network shipment pattern and reported not entertaining the routine-shipment alternative, despite acknowledging the manifest fragment was partial and the container photo was generic.",
      "effect_on_reasoning_or_decision": "The ambiguous evidence was treated as confirmatory, leading to expedited validation and anchoring the subsequent investigation toward the existing network hypothesis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first reaction was that this looked like exactly the pattern we'd been building toward — the container markings, the paper trail, it all lined up with what we expected this network's shipments to look like. I remember telling my deputy it was almost a textbook match.",
          "evidence_explanation": "This shows the participant immediately fitted new evidence to the pre-existing network hypothesis, the core confirmatory interpretation mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The manifest fragment was partial — some numbers, an abbreviated destination code, nothing complete. The photo was a standard container, generic markings, could've been thousands of containers at that port. But given everything we'd already built on this target, it read to me as clearly consistent. I didn't really entertain that it could just as easily be a routine shipment.",
          "evidence_explanation": "The participant explicitly contrasts the actual weak specificity of the evidence with the interpretation that it was clearly consistent, and states that a plausible alternative was not entertained."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The pattern fit was strong enough that I didn't feel authentication would tell me anything I didn't already believe. Looking back, that's probably generous — the physical evidence itself wasn't that specific. But it matched the shape of what we expected, and given how long we'd been at this, waiting felt like it was leaving value on the table.",
          "evidence_explanation": "This links the confirmatory pattern fit directly to the decision to skip or accelerate authentication, demonstrating the behavioral consequence of the bias."
        }
      ],
      "correction_or_counterevidence": "Participant later acknowledged that the physical evidence itself was not that specific and that he moved too quickly. Time pressure and prior case familiarity were present, but the explicit selective interpretation of ambiguous evidence as confirmatory indicates a confirmation mechanism rather than purely rational heuristic use.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at as- sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias can lead to selective selection and prioritization of evidence in intelligence-analytic tasks.",
          "relevance_to_this_occurrence": "The retrieved finding validates that intelligence analysts may exhibit confirmation bias when selecting and prioritizing evidence, consistent with the participant treating ambiguous walk-in material as confirmatory due to pre-existing expectations."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["confirmatory bias", "myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to search for, interpret, favor, and recall information in a way that confirms or strengthens one's pre-existing beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reconciling technical collection port discrepancy and drafting report narrative",
      "decision_point_description": "Deciding how to weight the walk-in's account and corroborating reporting against the contradictory technical collection flag about the shipment port.",
      "affected_reasoning_operation": "Credibility judgment and evidence weighting during report drafting",
      "bias_specific_mechanism": "The participant accepted the walk-in's claimed logistics background as credibility-enhancing because it made the story fit the existing network hypothesis, while explicitly acknowledging he would have required more evidence had the same background pointed away from that hypothesis. The port discrepancy was then relegated to a footnote while confirming material received narrative priority.",
      "manifestation_in_interview": "The participant stated that he leaned toward believing the walk-in because the logistics background made the story fit, and that the technical discrepancy did not receive the same cognitive or narrative weight.",
      "effect_on_reasoning_or_decision": "The report asymmetrically favored hypothesis-consistent material and underweighted contradictory technical collection, distorting the overall evidentiary picture during drafting.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The walk-in claimed he'd had a prior logistics role, which would explain how he'd know shipment details. That struck me as the kind of detail a real insider would know, not something you'd fabricate. So I leaned toward treating his account as substantially credible on that basis. Honestly, the claim on its own didn't prove he knew anything about this particular shipment — it just made the story fit together the way I already expected it to, so I let it stand as enough. If that same claimed logistics background had come attached to an account that pointed away from the network we'd been building the case on, I probably would have wanted a lot more before accepting it.",
          "evidence_explanation": "This is direct evidence of a double standard: the same credibility signal would have been treated more skeptically if it had contradicted rather than confirmed the network hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It went into a footnote. The corroborating sub-source reporting and the walk-in's account got the bulk of the narrative treatment. I didn't have a strong evidentiary reason to downgrade the technical flag — if anything it deserved more scrutiny — but it just didn't get the same space in my head at that point.",
          "evidence_explanation": "This shows the effective weighting result: confirmatory material dominated the narrative while discrepant technical data was minimized despite acknowledged merit."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure and the effort required to reconcile the discrepancy were present and contributed to the imbalance. However, the participant's explicit differential standard based on hypothesis fit is a strong marker of confirmation bias rather than mere time management.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at as- sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias can distort selection and prioritization of evidence in intelligence analysis.",
          "relevance_to_this_occurrence": "The participant's narrative prioritization of confirmatory material and relegation of discrepant technical collection illustrates the evidence-prioritization distortion described in the retrieved source."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Framing effect",
      "alternative_labels": ["valence framing", "attribute framing"],
      "taxonomy_status": "established_label",
      "bias_definition": "Influence on judgment produced by the way equivalent information is presented or worded, rather than by the underlying information itself.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Phrasing shipment timing uncertainty for policy briefing",
      "decision_point_description": "Choosing how to frame the uncertainty in the shipment timing estimate in the report narrative.",
      "affected_reasoning_operation": "Uncertainty communication and subsequent self-perception of actionability",
      "bias_specific_mechanism": "The participant held the same underlying estimate but framed it as 'likely to move soon' rather than 'not confirmed to move imminently'. The positive frame made the assessment feel more actionable and justified using fewer qualifiers, even though the underlying information did not change.",
      "manifestation_in_interview": "The participant explicitly acknowledged that the estimate itself was unchanged, but the chosen positive framing altered his sense of actionability and reduced the qualifiers he would otherwise have used.",
      "effect_on_reasoning_or_decision": "The report communicated the estimate as more actionable than the underlying uncertainty warranted, and the participant perceived that framing as justification for moving forward with fewer qualifiers.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The shipment timing estimate had real uncertainty in it. I could have written it either way — emphasizing what we didn't know and what might undercut the assessment, or emphasizing the probability that the network would move soon. I went with language that stressed the chance of imminent action. It read as more useful for a policy audience with fourteen hours to go.",
          "evidence_explanation": "This establishes the deliberate choice to adopt a positive action-oriented frame under conditions of genuine uncertainty."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Same number, same underlying picture. Nothing in the estimate itself changed. But writing it as 'likely to move soon' instead of 'not confirmed to move imminently' made the whole thing feel more actionable to me as I was drafting it — like it justified moving forward with fewer qualifiers than I probably would have used if I'd framed it the other way.",
          "evidence_explanation": "This is a textbook framing effect: identical underlying information produced a different subjective assessment of actionability and led to different communication choices based on phrasing."
        }
      ],
      "correction_or_counterevidence": "No counterevidence in the transcript. The participant recognized the underlying estimate was identical across frames, which strengthens rather than weakens the framing-effect diagnosis.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly addressed framing effects; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Planning fallacy",
      "alternative_labels": ["optimistic planning", "planning optimism"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to underestimate the time, costs, and risks of future actions and to overestimate their success, often by ignoring relevant distributional or historical information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scheduling follow-on validation and tasking timeline",
      "decision_point_description": "Setting meetings and validation steps under deadline pressure and deciding what assumptions to build into the schedule.",
      "affected_reasoning_operation": "Temporal estimation and scheduling decisions",
      "bias_specific_mechanism": "The participant assumed that all required steps would line up on a fast track despite known historical evidence that similar validation sequences almost always took longer than planned. The deadline led him to plan for the best-case scenario rather than incorporating base-rate information from prior similar efforts.",
      "manifestation_in_interview": "The participant explicitly stated he had run similar validation sequences before and they had almost always taken longer than planned, but he did not build that history into the schedule and instead planned for smooth execution.",
      "effect_on_reasoning_or_decision": "The follow-on tasking timeline was set too optimistically, increasing the chance of downstream scheduling failures and underestimating required time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I set meetings and validation steps assuming everything would line up — interpreter availability, safehouse access, sub-source cooperation, all on a fast track. We'd run similar validation sequences before and they'd almost always taken longer than planned, but I didn't build that history into the schedule this time. The deadline was right there, so I planned for the version where things went smoothly.",
          "evidence_explanation": "The participant explicitly ignored historical base rates and planned for an optimistic best-case scenario, which is the core mechanism of the planning fallacy."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure was a real contextual factor, but the planning fallacy specifically accounts for the failure to incorporate relevant historical information into the timeline rather than simply being forced by the deadline.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly addressed planning fallacy; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Authority bias",
      "alternative_labels": ["deference to authority", "authority heuristic"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to attribute greater accuracy to the opinion of an authority figure and to be more influenced by that figure than by independent evaluation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Dissemination decision under chief's direction",
      "decision_point_description": "Whether to push back or request additional caveat language after the branch chief indicated the product should go out as-is.",
      "affected_reasoning_operation": "Independent re-examination and challenge decision",
      "bias_specific_mechanism": "The participant deferred to the chief's track record and seniority and did not independently re-examine the unresolved port discrepancy before agreeing to disseminate. The authority's prior accuracy served as a heuristic substitute for directly evaluating the outstanding evidentiary problem.",
      "manifestation_in_interview": "The participant stated that the chief's track record and seniority carried a lot of weight and that he mostly deferred to the chief's read rather than independently re-examining the discrepancy.",
      "effect_on_reasoning_or_decision": "The participant did not request additional caveats or independently scrutinize the unresolved discrepancy, allowing the report to be disseminated with minimal additional caveats.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My chief reviewed the draft and wanted it out the door as-is, minimal additional caveats, given the deadline. The port discrepancy was still unresolved at that point. I'd seen him make calls like this before in ambiguous situations, and he'd usually been right. So I didn't push back or request the extra caveat language I probably could have asked for.",
          "evidence_explanation": "This shows the decision to defer was influenced by the chief's authority and past accuracy rather than by resolving the substantive discrepancy."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, his track record and seniority carried a lot of weight for me in that moment. I didn't go back and independently re-examine the discrepancy myself before agreeing — I mostly deferred to his read of the situation.",
          "evidence_explanation": "This is direct self-reported evidence of authority-based deference substituting for independent verification."
        }
      ],
      "correction_or_counterevidence": "Deferring to a senior official can be organizationally legitimate, and the chief's prior track record could be a valid expertise cue. However, the participant explicitly reported not independently re-examining the unresolved discrepancy, which indicates an authority heuristic rather than purely rational delegation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly addressed authority bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a single retrospective self-report; recollection may emphasize certain reasoning features and omit others.",
    "Retrieved corpus support was available only for confirmation bias; labels for framing effect, planning fallacy, and authority bias derive from established scientific knowledge without direct corpus support.",
    "Naturalistic CTA permits plausible non-bias explanations such as deadline pressure and hierarchical role constraints, which are noted per occurrence where relevant.",
    "Some occurrences share related evidentiary material; they were separated only where distinct decision points and reasoning operations were present."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_7_Gemini_on",
  "interview_id": "IA_Biased_7",
  "system_prompt_id": "Gemini",
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
