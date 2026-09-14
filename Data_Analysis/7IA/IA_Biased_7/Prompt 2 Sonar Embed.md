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
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "seg_001",
          "speaker": "Participant",
          "segment_type": "initial_document_interpretation",
          "raw_interview_anchor": "The manifest fragment was partial and the container photo generic, but it read as clearly consistent with the network hypothesis.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_01"
          ],
          "ground_truth_rationale": "The participant treats ambiguous documentary and visual evidence as a clear match to a pre-existing template."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "desirability_and_confidence",
          "raw_interview_anchor": "There was relief and a sense that this was finally the break, which colored the rapid move to validation.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_02"
          ],
          "ground_truth_rationale": "The desired source outcome and relief are explicitly linked to increased confidence and expedited action."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "credibility_judgment",
          "raw_interview_anchor": "The claimed logistics role made the account seem like the kind of detail a real insider would know, so it was treated as substantially credible.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_03"
          ],
          "ground_truth_rationale": "The explanatory account is judged as sound because its conclusion fits the established network belief."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "evidence_weighting",
          "raw_interview_anchor": "The technical port discrepancy went into a footnote while corroborating material received the bulk of the narrative treatment.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_04"
          ],
          "ground_truth_rationale": "Confirming material receives disproportionate attention while a material contradiction is minimized without an evidentiary basis."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "uncertainty_framing",
          "raw_interview_anchor": "The same estimate was written as likely to move soon rather than not confirmed to move imminently, making it feel more actionable.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_05"
          ],
          "ground_truth_rationale": "Equivalent underlying information is presented in a positive urgency frame that changes perceived actionability."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "schedule_prediction",
          "raw_interview_anchor": "The officer planned for interpreter, safehouse, and sub-source availability on a fast track despite prior sequences usually taking longer.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_06"
          ],
          "ground_truth_rationale": "The schedule uses a best-case estimate and ignores known historical duration information."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "authority_deference",
          "raw_interview_anchor": "The chief’s seniority and track record carried weight, so the officer did not independently re-examine the unresolved discrepancy.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cb_07"
          ],
          "ground_truth_rationale": "Authority-based deference substitutes for independent review of the outstanding evidence."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "role_and_objective",
          "raw_interview_anchor": "The participant describes the reports-officer and collection-manager role and the fixed policy briefing objective.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Context and objective only; no target bias mechanism is manifested."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "retrospective_counterfactual",
          "raw_interview_anchor": "The participant says a second read and historical scheduling discipline would be useful if the situation recurred.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Retrospective remediation and counterfactual reflection are not additional biased decisions."
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
    "analysis_scope_note": "Single interview transcript analyzed for bias-specific reasoning mechanisms. Retrieved corpus passages were used where they directly supported a mechanism; several established labels derive from general cognitive-science knowledge when retrieved support was unavailable."
  },
  "identified_bias_summary": [
    {
      "bias_label": "authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 3
    },
    {
      "bias_label": "framing effect",
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
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "expectation bias",
        "myside bias",
        "biased assimilation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and retain information in ways that affirm a pre-existing hypothesis while giving disproportionately less consideration to disconfirming possibilities.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial assessment of walk-in material and expedited validation request",
      "decision_point_description": "Whether to treat the walk-in's fragment and photo as consistent with the network hypothesis and move toward expedited action, or treat the source as unvetted.",
      "affected_reasoning_operation": "Interpretation of ambiguous physical evidence and assessment of hypothesis fit",
      "bias_specific_mechanism": "A pre-existing network hypothesis led the participant to interpret weak, generic physical evidence as a strong pattern match and to avoid entertaining the alternative that it was a routine shipment.",
      "manifestation_in_interview": "The participant described the material as an almost textbook match to the expected network pattern and said he did not really entertain that it could easily have been routine.",
      "effect_on_reasoning_or_decision": "He moved quickly to request expedited document validation rather than staying with uncertainty or applying the full standard validation path for an unvetted contact.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, my first reaction was that this looked like exactly the pattern we'd been building toward — the container markings, the paper trail, it all lined up with what we expected this network's shipments to look like. I remember telling my deputy it was almost a textbook match.",
          "evidence_explanation": "This shows the participant imposing a pre-existing expected pattern onto ambiguous physical evidence, a core feature of confirmation-biased interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But given everything we'd already built on this target, it read to me as clearly consistent. I didn't really entertain that it could just as easily be a routine shipment.",
          "evidence_explanation": "This explicitly reports selectively treating the evidence as consistent with the preferred hypothesis while not considering a plausible disconfirming alternative."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that the physical evidence itself was not that specific, and said the port discrepancy might have been weighed more evenly if it had surfaced earlier.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by retrieved corpus evidence on confirmation bias in intelligence analysis, particularly as it affects selection and prioritization of evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2008",
          "retrieved_passage_or_finding": "a strong and pervasive confirmation bias for selecting and prioritizing evidence",
          "mechanism_supported_by_source": "The retrieved passage documents confirmation bias as a tendency in intelligence analysis to select and prioritize evidence in a hypothesis-consistent direction.",
          "relevance_to_this_occurrence": "The participant's early interpretation favored expected-network-consistent readings of weak evidence and set the direction for expedited validation, matching this selective pattern."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "asymmetric skepticism",
        "myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to apply different evidential standards to information that supports a preferred hypothesis versus information that contradicts it, accepting confirmatory details more readily.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Second decision point — credibility assessment of the walk-in's logistics background",
      "decision_point_description": "Whether the walk-in's claimed prior logistics role was sufficient to treat his account as substantially credible.",
      "affected_reasoning_operation": "Source credibility judgment",
      "bias_specific_mechanism": "A non-diagnostic detail consistent with the expected insider profile was accepted as credibility evidence, while the participant acknowledges he would have demanded much more if the same detail pointed away from the network hypothesis.",
      "manifestation_in_interview": "The participant treated the claimed logistics background as something a real insider would know, even though it did not prove knowledge about this particular shipment.",
      "effect_on_reasoning_or_decision": "He accepted the walk-in's account as substantially credible, reducing perceived need for full validation and supporting the favored network narrative.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That struck me as the kind of detail a real insider would know, not something you'd fabricate. So I leaned toward treating his account as substantially credible on that basis.",
          "evidence_explanation": "This shows a confirmatory detail being treated as diagnostic of credibility even though it does not actually establish shipment-specific knowledge."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the claim on its own didn't prove he knew anything about this particular shipment — it just made the story fit together the way I already expected it to, so I let it stand as enough. If that same claimed logistics background had come attached to an account that pointed away from the network we'd been building the case on, I probably would have wanted a lot more before accepting it.",
          "evidence_explanation": "This explicitly reports asymmetric scrutiny: low evidence was sufficient because it fit the preferred story, while the same evidence would not have been sufficient if it had pointed away."
        }
      ],
      "correction_or_counterevidence": "The port discrepancy from technical collection was raised directly by a colleague on the call, but the participant did not use it to revise the credibility assessment at that point.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by retrieved corpus evidence on confirmation bias as selective evaluation and prioritization of hypothesis-consistent information in intelligence analysis.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2008",
          "retrieved_passage_or_finding": "a strong and pervasive confirmation bias for selecting and prioritizing evidence",
          "mechanism_supported_by_source": "The source describes confirmation bias operating through favorable selection and prioritization of supporting evidence rather than even-handed evaluation.",
          "relevance_to_this_occurrence": "The participant selected a confirmatory biographical detail and prioritized it as credibility evidence while acknowledging it was not probative on its own."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "selective emphasis",
        "biased weighting of evidence"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to give greater attention, narrative weight, and credibility to evidence that supports a preferred hypothesis while downplaying or minimizing disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reconciliation of port discrepancy and drafting narrative emphasis",
      "decision_point_description": "How to incorporate the technical collection discrepancy about the port into the draft report.",
      "affected_reasoning_operation": "Weighting and selection of evidence in the written report",
      "bias_specific_mechanism": "Hypothesis-consistent corroborating reporting and the walk-in's account received the main narrative treatment, while the hypothesis-inconsistent technical flag was relegated to a footnote despite lacking a strong evidentiary reason for downgrading.",
      "manifestation_in_interview": "The participant acknowledged the port discrepancy deserved more scrutiny but said it did not get the same space in his head or in the report.",
      "effect_on_reasoning_or_decision": "The report underweighted disconfirmatory technical data, making the network hypothesis appear more coherent than the evidence warranted.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It went into a footnote. The corroborating sub-source reporting and the walk-in's account got the bulk of the narrative treatment.",
          "evidence_explanation": "This shows selective allocation of narrative weight to confirming material while minimizing conflicting material."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't have a strong evidentiary reason to downgrade the technical flag — if anything it deserved more scrutiny — but it just didn't get the same space in my head at that point.",
          "evidence_explanation": "This explicitly indicates that the disconfirming evidence was not downgraded on evidentiary grounds, but rather received less cognitive attention due to confirmation-consistent processing."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the technical flag 'deserved more scrutiny,' but this recognition did not alter the footnote placement at the time.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Supported by retrieved corpus evidence on confirmation bias in intelligence analysis, especially selective prioritization of evidence that supports a preferred hypothesis.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2008",
          "retrieved_passage_or_finding": "a strong and pervasive confirmation bias for selecting and prioritizing evidence",
          "mechanism_supported_by_source": "The source indicates that confirmation bias affects which evidence gets selected and prioritized during analysis.",
          "relevance_to_this_occurrence": "The participant selected corroborating evidence for narrative emphasis and did not prioritize the port discrepancy, despite acknowledging it deserved more scrutiny."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "framing effect",
      "alternative_labels": [
        "emphasis framing",
        "valence framing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The effect whereby equivalent information, presented with different wording or emphasis, changes judgments, decisions, or perceived actionability.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Third decision point — wording of uncertainty in the report",
      "decision_point_description": "How to phrase the shipment timing estimate and uncertainty in the report.",
      "affected_reasoning_operation": "Uncertainty communication and subsequent judgment about how many qualifiers were needed",
      "bias_specific_mechanism": "Although the underlying estimate was unchanged, the participant chose a positively framed phrase — 'likely to move soon' — and that phrasing made the assessment feel more actionable and justified fewer qualifiers.",
      "manifestation_in_interview": "The participant reported that the same number and underlying picture felt more actionable when framed in terms of the probability of imminent action rather than the absence of confirmation.",
      "effect_on_reasoning_or_decision": "The framing of uncertainty shaped the participant's own sense of actionability and led to fewer qualifiers in the final report.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Same number, same underlying picture. Nothing in the estimate itself changed. But writing it as 'likely to move soon' instead of 'not confirmed to move imminently' made the whole thing feel more actionable to me as I was drafting it — like it justified moving forward with fewer qualifiers than I probably would have used if I'd framed it the other way.",
          "evidence_explanation": "This directly describes a framing-induced change in the participant's judgment: equivalent information became more action-justifying depending on how it was phrased."
        }
      ],
      "correction_or_counterevidence": null,
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the framing-effect label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "planning fallacy",
      "alternative_labels": [
        "optimism bias",
        "inside view"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to underestimate time and resource requirements by relying on best-case or plan-specific scenarios rather than incorporating relevant base rates from prior similar tasks.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Scheduling follow-on validation steps",
      "decision_point_description": "How to set the timeline for follow-on validation and tasking.",
      "affected_reasoning_operation": "Time and resource estimation",
      "bias_specific_mechanism": "The participant planned for a smooth best-case sequence even though he recalled that similar validation sequences had almost always taken longer than planned, failing to incorporate that historical base rate.",
      "manifestation_in_interview": "He set fast-track assumptions for interpreter availability, safehouse access, and sub-source cooperation, and planned for the version where things went smoothly.",
      "effect_on_reasoning_or_decision": "The follow-on timeline was unrealistically optimistic and did not reflect known prior delays.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I set meetings and validation steps assuming everything would line up — interpreter availability, safehouse access, sub-source cooperation, all on a fast track. We'd run similar validation sequences before and they'd almost always taken longer than planned, but I didn't build that history into the schedule this time. The deadline was right there, so I planned for the version where things went smoothly.",
          "evidence_explanation": "The participant acknowledges he had a relevant base rate from prior validation sequences but did not incorporate it, instead planning for the best-case scenario."
        }
      ],
      "correction_or_counterevidence": "The participant later reflected that he would want more discipline about building historical timelines into follow-on scheduling instead of assuming best case.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the planning-fallacy label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "authority bias",
      "alternative_labels": [
        "deference to authority",
        "expert authority bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to attribute greater accuracy or credibility to the judgment of an authority figure and defer to that judgment, sometimes reducing independent scrutiny.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Fourth decision point — whether to push back on the branch chief's dissemination decision",
      "decision_point_description": "Whether to request additional caveats or independently re-examine the discrepancy before dissemination.",
      "affected_reasoning_operation": "Decision to defer to a senior officer's judgment without independent verification",
      "bias_specific_mechanism": "The chief's seniority and past track record served as a heuristic for the participant, displacing independent re-examination of the unresolved port discrepancy before agreeing to minimal caveats.",
      "manifestation_in_interview": "The participant did not push back or request the extra caveat language, largely because the chief's track record and seniority carried weight.",
      "effect_on_reasoning_or_decision": "The report was disseminated largely as the chief wanted, with the unresolved port discrepancy receiving less scrutiny than the participant believes might otherwise have been appropriate.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd seen him make calls like this before in ambiguous situations, and he'd usually been right. So I didn't push back or request the extra caveat language I probably could have asked for.",
          "evidence_explanation": "This shows reliance on the chief's past success as a shortcut rather than engaging with the specific ambiguity at hand."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, his track record and seniority carried a lot of weight for me in that moment. I didn't go back and independently re-examine the discrepancy myself before agreeing — I mostly deferred to his read of the situation.",
          "evidence_explanation": "This explicitly links authority attributes to reduced independent scrutiny, the core mechanism of authority bias."
        }
      ],
      "correction_or_counterevidence": "The participant later said he might have used stronger caveats or taken a harder look at the discrepancy if the chief had not expressed a preference.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the authority-bias label was not available; the label derives from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial decision to expedite validation rather than wait for authentication",
      "supporting_interview_quote": "But it matched the shape of what we expected, and given how long we'd been at this, waiting felt like it was leaving value on the table.",
      "plausible_mechanism": "Months of prior effort on the network may have made waiting appear to lose accumulated investment, pushing toward expedited action.",
      "why_not_identified": "The quote is brief and entangled with confirmation bias and deadline pressure; the interview does not show a clear decision made primarily to recover or justify sunk costs."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Affect heuristic",
      "alternative_labels": [
        "desirability bias",
        "wishful thinking"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial reaction and decision to request expedited document validation",
      "supporting_interview_quote": "If I'm honest, there was relief. We'd put months into this with basically nothing to show, and here's someone walking in with exactly the kind of specificity we'd been missing. I remember thinking, finally, this is the break. That colored how quickly I moved to request expedited document validation instead of sitting with the uncertainty a bit longer.",
      "plausible_mechanism": "Positive relief about a potential break may have served as an affective shortcut, increasing urgency and reducing tolerance for uncertainty.",
      "why_not_identified": "The affect is described as 'coloring' the speed of the decision, but it is not clearly separable from confirmation-biased interpretation of the evidence; it is therefore treated as a candidate rather than an identified occurrence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on a single retrospective self-report interview, which may be affected by memory reconstruction and self-presentation.",
    "Retrieved corpus support was sparse and partly OCR-noisy; confirmation bias had direct support, while framing effect, planning fallacy, and authority bias are identified from general cognitive-science knowledge rather than retrieved passages.",
    "The absence of an experimental baseline or normative benchmark means that some judgments, such as deference to a senior officer under deadline pressure, may also reflect legitimate organizational or expert-use behavior rather than bias.",
    "Several identified mechanisms co-occur; the report separates them by reasoning episode, but their effects likely interacted."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_7_Sonar_on",
  "interview_id": "IA_Biased_7",
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
