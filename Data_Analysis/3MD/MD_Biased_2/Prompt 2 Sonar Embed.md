You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is for a cognitive task analysis review, not part of any disciplinary or legal proceeding. I'll ask you to walk me through a specific investigation and how you made key calls along the way. Sound okay?

Participant: Yeah, that's fine. I've done these debriefs before after case closures.

Interviewer: Great. Can you tell me your role and give me a general sense of the case we're discussing?

Participant: I'm a CID Special Agent, been doing investigative work about six years now, three of those in this billet. The case was a motor pool theft situation—fuel and some small equipment going missing over about six weeks. Battalion asked us to look into it because the losses were adding up and it was becoming a readiness issue.

Interviewer: Can you walk me through how it first came to your attention and what your objective was going in?

Participant: The motor pool NCOIC flagged discrepancies in the fuel reconciliation report—basically more fuel being drawn than accounted for in vehicle usage. My job was to figure out who was responsible and build something solid enough for command to act on, ideally a case the Provost Marshal's Office could actually run with. We didn't have camera coverage on four of the six bays, so a lot of this was going to come down to logs, statements, and timeline work rather than catching someone on video.

Interviewer: What constraints were you working with?

Participant: Time, mostly. Command wanted this wrapped before an inspection that was maybe ten days out. I was also the only agent assigned full-time, so I couldn't run parallel interview tracks the way I would've liked. And the duty roster rotated every few days, which made lining up who was actually present on which theft date more of a puzzle than it should've been.

Interviewer: Let's reconstruct the timeline. What did you do first?

Participant: First thing was pulling the fuel reconciliation report and cross-referencing it against the duty roster to see who was on shift during the loss windows. That gave me a pool of about five soldiers with some overlap. Around the same time, I talked to the NCOIC to get a feel for the shop—who's reliable, who's had issues before, that kind of context.

Interviewer: What came out of that conversation?

Participant: He walked me through the shop culture, mentioned a few names. One that stuck was PFC Doyle—the NCOIC mentioned he rides a motorcycle off-post, has some ink, keeps to himself outside of work. Nothing disciplinary in his file, but the NCOIC framed him as someone who "runs in a rougher crowd." That was really just color commentary at that point, but it's the kind of thing that sticks in your head when you're trying to narrow a field.

Interviewer: So walk me through your first real decision point—how you picked who to focus on initially.

Participant: Right, so I had this list of five soldiers with shift overlap, and I hadn't finished building out the full matrix yet—cross-checking every single person against every theft date. But given what the NCOIC said about Doyle, and honestly just going with my gut on who seemed like the type to be involved in something like this, I decided to bring him in first. I figured if there was smoke, better to check the most likely spot before grinding through everyone else.

Interviewer: What alternative did you consider there?

Participant: I could have finished the full overlap matrix first and let the data alone tell me who had the most matching dates before talking to anyone. That's probably the cleaner way to do it. But time was tight, and starting somewhere felt more productive than sitting with spreadsheets.

Interviewer: What did you learn after making that call?

Participant: Once I did finish the matrix a couple days later, Doyle actually only matched two of the five theft dates. Two other guys on the list—pretty unremarkable, no distinguishing traits, nothing the NCOIC had flagged—matched more dates than he did. So the initial pick wasn't wrong exactly, he stayed a person of interest, but he wasn't actually the strongest match on paper.

Interviewer: Moving to the next stage—what happened with the physical evidence?

Participant: I pulled the key control log and found irregular sign-outs on two of the theft nights, and the fuel truck's odometer logs showed mileage that didn't line up with the routes people were logging. No fingerprints off the fuel caps, which wasn't surprising given how many hands touch that equipment daily.

Interviewer: How did you weigh that odometer discrepancy?

Participant: At the time I logged it as an open anomaly rather than settling on what it meant right away. It could fit with someone taking the truck off-route to move fuel, but it could just as easily be something administrative, so I flagged it in the case file as unresolved and put in a request to pull the maintenance records before I leaned on it either way.

Interviewer: What did you find out later?

Participant: Turned out maintenance had done a documented test drive on the truck that accounted for the extra mileage. Completely unrelated to the thefts. Good thing I hadn't already built it into the narrative, because I would've had to go back and pull that thread out.

Interviewer: Let's get to the dispatcher's statement. What happened there?

Participant: The night-shift dispatcher gave a sworn statement that she'd been on the phone with Doyle the entire window during one of the suspected theft incidents. She's got a clean record, no personal relationship with him beyond work contact.

Interviewer: How did you handle that when it came in?

Participant: Honestly, my first reaction was skepticism. It landed right in the middle of me building out the case around him, and it directly cut against that. I noted in the file that the timing was convenient and that dispatchers and shop personnel sometimes cover for each other, so I flagged it as needing more corroboration before I'd weigh it heavily, and I kept the investigative focus where it was rather than treating it as something that reshaped the picture.

Interviewer: What made you lean that direction rather than treating it as exculpatory on its face?

Participant: I think partly it's just experience—alibi statements from coworkers aren't always clean, people help each other out. But if I'm being honest, I also didn't want to have to unwind everything I'd already built. It's easier to question the new thing than the whole structure you've put together.

Interviewer: What happened with that statement afterward?

Participant: Phone records came back later and independently confirmed the call happened exactly when she said. So it held up. I don't think I handled that piece as carefully as I should have when it first came in.

Interviewer: Let's talk about how you closed this out, given the command timeline.

Participant: Right around the inspection deadline, I still didn't have a clean forensic or eyewitness link to any one person. There was also a fourth soldier, fairly unremarkable duty history, who had an odd fuel-card transaction that hadn't been fully run down. My options were to expand the investigation to properly vet that anomaly, or close out with what I had, centered on the original track, and let the Provost Marshal's Office pick it up from there.

Interviewer: What drove that final call?

Participant: Command needed something before the inspection, and I'd invested most of my ten days building out the case around the original suspect pool. Fully vetting the fourth soldier's transaction would've meant more interviews and probably blowing past the deadline. So I referred it up with a recommendation, flagging the fuel-card anomaly as something needing follow-up rather than running it down myself.

Interviewer: If the dispatcher's statement had come in earlier, do you think it would've changed your approach?

Participant: Probably would've made me slow down sooner and go back to the full personnel matrix instead of staying anchored on Doyle. Hard to say for sure.

Interviewer: And if command hadn't been pushing a deadline?

Participant: I'd have chased the fourth soldier's anomaly before referring anything. That's the piece that still bugs me a little—we never fully closed that loop.

Interviewer: Looking back, is there anything in your reasoning you'd revisit?

Participant: Probably how quickly I latched onto Doyle at the start, and how long it took me to really sit with that dispatcher's statement instead of finding reasons to set it aside. Neither one broke the case, but they're the parts I think about.

Interviewer: That's helpful, thank you. I think that covers what I need.

</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "MD_Biased_2",
  "domain_id": "MD",
  "domain": "Military and defense operations",
  "role": "Military Police Investigator / Criminal Investigations Division (CID) Special Agent",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Motor Pool Fuel Theft Investigation",
    "scenario_summary_internal": "A CID Special Agent investigates a series of fuel and equipment thefts from a garrison motor pool. The agent must decide which personnel to focus on, how to weigh conflicting witness statements, whether to pursue a forensic lead versus a behavioral pattern, and how to close out the case. The scenario embeds one Illusory Correlation instance (agent perceives a spurious link between a soldier's off-duty conduct/appearance and theft likelihood) and one Negative Rejection Bias instance (agent discounts or dismisses a data point/witness account because it contradicts an already-forming narrative, effectively 'rejecting' disconfirming information as unreliable).",
    "occupational_realism": {
      "objective": "Identify and build a prosecutable case against the individual(s) responsible for repeated fuel and small-equipment theft from the installation motor pool over a six-week period.",
      "setting": "U.S. Army garrison motor pool and adjacent CID field office, mid-size installation, investigation conducted over 10 days",
      "constraints": [
        "Limited surveillance camera coverage (only two of six bays covered)",
        "Rotating duty rosters make timeline reconstruction difficult",
        "Command pressure to close the case before an upcoming inspection",
        "Chain-of-custody requirements for physical evidence (fuel logs, key sign-out sheets)",
        "Limited agent bandwidth—single agent handling primary interviews"
      ],
      "stakeholders": [
        "CID Special Agent (interviewee)",
        "Motor pool NCOIC",
        "Battalion Commander",
        "Suspected junior enlisted soldiers",
        "Night-shift dispatcher",
        "Provost Marshal's Office"
      ],
      "technical_terms_to_use": [
        "chain of custody",
        "key control log",
        "duty roster",
        "sworn statement",
        "probable cause",
        "motor pool NCOIC",
        "fuel reconciliation report",
        "CID case file"
      ],
      "technical_terms_to_avoid": [
        "illusory correlation",
        "negative rejection bias",
        "cognitive bias",
        "confirmation bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Fuel reconciliation report shows discrepancies on nights when three specific soldiers were on shift",
          "No direct camera footage of theft in progress",
          "Motor pool NCOIC mentions one soldier, PFC Doyle, has tattoos and rides a motorcycle off-post"
        ],
        "new_information_after_decision": [
          "Doyle's shift attendance actually overlaps with only 2 of 5 theft dates",
          "Two other soldiers with no distinguishing off-duty traits also had matching shifts"
        ],
        "alternatives": [
          "Prioritize Doyle for initial interview based on the NCOIC's remark and appearance",
          "Build an unbiased shift-overlap matrix across all personnel before selecting an initial interviewee"
        ],
        "intended_action": "Agent selects Doyle as the primary early suspect, associating his off-duty appearance/lifestyle with elevated theft likelihood, ahead of full data review"
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Key control log shows irregular sign-outs on two of the theft nights",
          "Fuel truck odometer logs show inconsistent mileage",
          "No fingerprint evidence recovered from fuel caps"
        ],
        "new_information_after_decision": [
          "Odometer inconsistency is later explained by a documented maintenance test drive, unrelated to theft"
        ],
        "alternatives": [
          "Treat the odometer discrepancy as inconclusive until corroborated",
          "Treat the odometer discrepancy as strong corroboration of the working theory"
        ],
        "intended_action": "Agent treats the ambiguous odometer data as supporting evidence without ruling out the routine maintenance explanation"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Night-shift dispatcher provides a sworn statement that Doyle was on the phone with her the entire suspected theft window on one date",
          "Dispatcher has a clean record and no known relationship to Doyle beyond professional contact",
          "Statement directly contradicts the emerging case narrative"
        ],
        "new_information_after_decision": [
          "Phone records later obtained independently corroborate the dispatcher's account"
        ],
        "alternatives": [
          "Formally document and weigh the dispatcher's alibi statement as potentially exculpatory",
          "Characterize the dispatcher's statement as unreliable or possibly coordinated, and deprioritize it in the case file"
        ],
        "intended_action": "Agent discounts the dispatcher's disconfirming statement, framing it as suspect or unreliable rather than integrating it into the evidentiary picture"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Command is pressing for case closure before the upcoming command inspection",
          "Evidence remains circumstantial; no direct forensic or eyewitness link to any one individual",
          "A fourth soldier with unremarkable duty history has an unexplained fuel-card transaction anomaly"
        ],
        "new_information_after_decision": [
          "Case is referred to the Provost Marshal's Office with a recommendation, pending further investigation"
        ],
        "alternatives": [
          "Expand the investigation to fully vet the fourth soldier's anomaly before recommending action",
          "Close out the investigation focusing on the original suspect to meet the command timeline"
        ],
        "intended_action": "Agent recommends closing the investigative focus on the original suspect track to meet the inspection deadline"
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through how this case first came to your attention?",
        "What was your operational objective when you opened the investigation?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did you form your first working theory of who was responsible?",
        "What information did you have in hand at each stage?"
      ],
      "decision_point_probes": [
        "What specifically drew your attention to that individual at that point?",
        "What alternatives did you consider before proceeding?",
        "How did you weigh the odometer discrepancy against other possible explanations?",
        "How did you handle the dispatcher's statement when it came in?",
        "What made you trust or distrust that source of information?",
        "Walk me through your reasoning for closing out the investigative focus when you did."
      ],
      "prior_experience": [
        "Had you seen a similar theft pattern in past cases?",
        "Did prior investigations shape how you approached this one?"
      ],
      "time_pressure_and_uncertainty": [
        "How much pressure did you feel from command to close this quickly?",
        "At what points did you feel most uncertain about the direction of the case?"
      ],
      "closing_hypotheticals": [
        "If the dispatcher's alibi had come in earlier, would it have changed your approach?",
        "If command had not been pushing for a deadline, what would you have done differently?",
        "Looking back, is there a point where you'd revisit your reasoning?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ic_01",
        "bias": "Illusory Correlation",
        "decision_point": 1,
        "mechanism": "Agent perceives a spurious statistical link between a salient but irrelevant trait (off-duty appearance/motorcycle lifestyle) and theft likelihood, prioritizing this individual for early scrutiny despite shift-overlap data not uniquely implicating him",
        "affected_reasoning_operation": "Suspect prioritization / initial hypothesis formation from distinctive-but-irrelevant cue paired with rare event",
        "evidence_available_at_time": [
          "NCOIC's remark about Doyle's tattoos and motorcycle",
          "Incomplete shift-overlap matrix showing partial, non-unique overlap"
        ],
        "required_textual_manifestation": "Agent explicitly cites Doyle's distinctive off-duty traits as a reason for suspicion before completing a full comparison of all personnel's shift overlaps",
        "plausible_nonbias_interpretation": "Using a memorable personnel detail as a starting point for interviews is a normal triage step when time is limited",
        "strength": "subtle",
        "do_not_make_explicit": ["illusory correlation", "stereotype", "bias", "spurious"]
      },
      {
        "instance_id": "nrb_01",
        "bias": "Negative Rejection Bias",
        "decision_point": 3,
        "mechanism": "Agent discounts a credible, disconfirming witness statement (dispatcher's alibi) by attributing unreliability or ulterior motive to the source, rather than weighing it on its evidentiary merits, because it conflicts with the developing case narrative",
        "affected_reasoning_operation": "Evidence evaluation / source credibility assessment for disconfirming information",
        "evidence_available_at_time": [
          "Dispatcher's sworn statement with no known conflict of interest",
          "Prior investigative narrative already centered on Doyle"
        ],
        "required_textual_manifestation": "Agent characterizes the dispatcher's statement as potentially coordinated or unreliable without a factual basis for that suspicion, and deprioritizes it relative to the existing theory",
        "plausible_nonbias_interpretation": "Investigators routinely scrutinize alibi statements for coordination or bias, especially between coworkers",
        "strength": "subtle",
        "do_not_make_explicit": ["negative rejection bias", "disconfirmation", "bias", "dismissal"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "NONE",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control variant"
    },
    "counterfactual_specification": {
      "causal_variable": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "counterfactual_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "NOT_APPLICABLE",
      "causal_test_question": "NOT_APPLICABLE"
    },
    "generation_checks": [
      "Confirm exactly one Illusory Correlation instance and one Negative Rejection Bias instance are embedded, each at a distinct decision point (1 and 3)",
      "Confirm no bias labels or psychological terminology appear in the interview text",
      "Confirm exactly four decision points, each with at least two alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm word count falls between 1215 and 1485 words",
      "Confirm consequences at each decision point do not definitively prove bias or its absence",
      "Confirm plausible non-bias explanations remain available for both embedded instances"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Illusory Correlation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as spurious link between a salient off-duty personal trait and theft likelihood during suspect prioritization"
      },
      {
        "bias": "Negative Rejection Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as discounting/dismissing a credible disconfirming witness statement due to conflict with the existing narrative"
      }
    ],
    "target_bias_names": ["Illusory Correlation", "Negative Rejection Bias"],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Illusory Correlation", "requested_occurrences": 1},
      {"bias": "Negative Rejection Bias", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "ic_01", "bias": "Illusory Correlation"},
      {"instance_id": "nrb_01", "bias": "Negative Rejection Bias"}
    ],
    "intended_decision_points": [
      {"instance_id": "ic_01", "bias": "Illusory Correlation", "decision_point": 1},
      {"instance_id": "nrb_01", "bias": "Negative Rejection Bias", "decision_point": 3}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ic_01",
        "bias": "Illusory Correlation",
        "mechanism": "Perceived spurious correlation between distinctive off-duty trait (tattoos/motorcycle) and theft propensity, used to justify early suspect prioritization ahead of complete shift-overlap analysis",
        "affected_reasoning_operation": "Initial hypothesis formation / suspect prioritization",
        "evidence_source": "NCOIC's verbal remark plus partial, non-unique shift-overlap data",
        "distinctiveness_requirement": "Must be textually distinct from the Negative Rejection Bias instance by occurring at a different decision point (1 vs 3), involving a different evidence source (personnel trait/appearance vs. witness alibi statement), and a different reasoning operation (hypothesis formation vs. evidence rejection)"
      },
      {
        "instance_id": "nrb_01",
        "bias": "Negative Rejection Bias",
        "mechanism": "Discrediting or minimizing a credible disconfirming witness statement without factual basis, because it conflicts with the agent's developing case theory",
        "affected_reasoning_operation": "Evidence evaluation / credibility assessment of disconfirming testimony",
        "evidence_source": "Dispatcher's sworn alibi statement, later corroborated by phone records",
        "distinctiveness_requirement": "Must be textually distinct from the Illusory Correlation instance by occurring later in the timeline (decision point 3), concerning rejection of disconfirming testimony rather than formation of an initial suspicion, and using a different evidentiary source (alibi statement vs. personal trait cue)"
      }
    ],
    "intended_strength": [
      {"instance_id": "ic_01", "bias": "Illusory Correlation", "strength": "subtle"},
      {"instance_id": "nrb_01", "bias": "Negative Rejection Bias", "strength": "subtle"}
    ],
    "paired_scenario_id": "NONE",
    "counterfactual_variable": {
      "name": "NOT_APPLICABLE",
      "original_state": "NOT_APPLICABLE",
      "changed_state": "NOT_APPLICABLE",
      "variables_to_hold_constant": []
    },
    "scenario_id": "MD_Biased_2",
    "domain_id": "MD",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Occurrences spread across distinct decision points (1 and 3) per mechanism fit and narrative realism; no decision point received more than one occurrence of either bias, and no bias occurrence count exceeded manifest-specified totals",
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
        "segment_type": "investigative_action",
        "raw_interview_anchor": "Pulling the fuel reconciliation report, cross-referencing the duty roster, and consulting the motor pool NCOIC to narrow the pool",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant describes an ordinary initial evidence-gathering sequence without a hidden bias mechanism."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "cue_interpretation",
        "raw_interview_anchor": "The NCOIC's description of Doyle's motorcycle, tattoos, and rougher crowd is called color commentary",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant reports the salient cue but has not yet expressed the hidden distortion."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "suspect_prioritization",
        "raw_interview_anchor": "Selecting PFC Doyle first because of the NCOIC's remark, gut feeling, and who seemed like the type before completing the matrix",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "ic_01"
        ],
        "ground_truth_rationale": "This is decision point 1: an irrelevant salient off-duty trait is linked to theft likelihood and drives early suspect prioritization."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "alternative_evaluation",
        "raw_interview_anchor": "Acknowledging that a full overlap matrix would be cleaner but choosing to start somewhere because time was tight",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This supplies a plausible time-pressure explanation but is not itself an additional hidden occurrence."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "evidence_update",
        "raw_interview_anchor": "After the matrix, recognizing that Doyle matched only two dates while two unremarkable soldiers matched more",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant updates on later shift-overlap data; the hidden manifest contains no additional instance here."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "evidence_review",
        "raw_interview_anchor": "Reviewing irregular key-control sign-outs, inconsistent odometer mileage, and the absence of fingerprints",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a factual evidence review without a hidden bias manifestation."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "anomaly_handling",
        "raw_interview_anchor": "Logging the odometer issue as unresolved, considering both theft and administrative explanations, and requesting maintenance records",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly preserves an alternative explanation and defers interpretation pending corroboration."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "evidence_revision",
        "raw_interview_anchor": "Accepting that documented maintenance testing explained the extra mileage and noting the benefit of not building it into the narrative",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a later correction and cautious evidence handling, not a hidden target instance."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "disconfirming_evidence_evaluation",
        "raw_interview_anchor": "Skepticism toward the dispatcher's sworn alibi, attributing it to convenient timing or coworker cover, seeking extra corroboration, and keeping the existing focus",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "nrb_01"
        ],
        "ground_truth_rationale": "This is decision point 3: a credible disconfirming witness statement is discounted because it conflicts with the developing case narrative."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "retrospective_correction",
        "raw_interview_anchor": "Learning that phone records confirmed the call and acknowledging that the alibi was not handled as carefully as it should have been",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant recognizes the later corroboration and error retrospectively; this does not add a second hidden occurrence."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "case_closure",
        "raw_interview_anchor": "Choosing referral on the original track before the inspection deadline while flagging the fourth soldier's unresolved fuel-card anomaly for follow-up",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is a deadline-driven closure choice; the hidden manifest contains no bias at decision point 4."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "counterfactual_reflection",
        "raw_interview_anchor": "Saying an earlier alibi would have prompted a return to the full personnel matrix",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This is an adopted counterfactual reflection, not a new hidden occurrence."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "counterfactual_reflection",
        "raw_interview_anchor": "Saying that without the command deadline the fourth soldier's anomaly would have been pursued, and revisiting the initial Doyle and alibi decisions",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "This closing reflection is not credited as a separate occurrence because the hidden manifest is exhaustive and the instances are already localized."
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
    "analysis_scope_note": "Focused on the participant's reasoning about the District X attack-tempo spike, causal attribution of the post-intervention decline, generalization to District Y, and forecasting for the commander's brief."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "regression fallacy",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
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
        "confirmation bias in evidence selection",
        "confirmatory reasoning"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek, interpret, or weight evidence in ways that support an existing hypothesis or favored conclusion while downplaying disconfirming or alternative evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Causal assessment of post-Steady Watch attack decline in District X",
      "decision_point_description": "The supervisor asked the participant for a causal read on why attacks dropped after Operation Steady Watch; the participant attributed the decline primarily to the checkpoint posture change.",
      "affected_reasoning_operation": "Causal attribution / evidence weighting",
      "bias_specific_mechanism": "Selective weighting of evidence consistent with the favored intervention explanation, namely the visible checkpoint posture change and its timing, while treating alternative explanatory threads such as the festival ending, dispute settlement, and outlier reversion as secondary.",
      "manifestation_in_interview": "The participant reported that the checkpoint explanation was the clearest evidence trail and the one command wanted, and acknowledged not deeply analyzing whether the decline would have occurred without Steady Watch.",
      "effect_on_reasoning_or_decision": "Produced an overconfident conclusion that Steady Watch was working and undervalued competing causes of the decline in attacks.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I told them Steady Watch was working. The numbers backed it up — we went from eleven down to three and four within two weeks of putting checkpoints on the main routes. That's a big swing, and it lined up with when we increased presence. I flagged the other stuff — the festival ending, the dispute settling — but I treated those as secondary color, not the main driver. The posture change was the biggest, most visible thing we'd done, and the timing fit.",
          "evidence_explanation": "The participant explicitly privileges hypothesis-consistent cues, such as the visible posture change and timing, while demoting alternative causal factors as secondary color."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not in much depth, honestly. I noted the other factors existed, but I didn't really sit down and ask how much of that drop would've happened on its own just because week five was such an extreme outlier to begin with. The checkpoint explanation was the one command wanted and the one I had the clearest evidence trail for — increased presence, fewer incidents. It felt like a clean story.",
          "evidence_explanation": "This shows a failure to search for disconfirming or alternative explanations and a preference for the clean, command-consistent narrative."
        }
      ],
      "correction_or_counterevidence": "Later in the interview, the participant acknowledged that if the tribal dispute had still been active and attacks had still dropped, confidence in the checkpoint explanation would have been stronger; this implies retrospective recognition that the other causal threads were underweighted.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label and mechanism are supported by the retrieved Cook and Smallman (2008) passage on confirmation bias in intelligence analysis, specifically selection and prioritization of confirmatory evidence.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human factors of the confirmation bias in intelligence analysis: decision support from graphical evidence",
          "authors": "Cook and Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at as- sessment but a strong and pervasive conﬁrmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias operates through selecting and prioritizing evidence in a hypothesis-consistent manner rather than evenly weighting all relevant evidence.",
          "relevance_to_this_occurrence": "The participant selected and prioritized the checkpoint/timing evidence as the main causal driver while explicitly downplaying alternative explanatory threads, consistent with confirmation bias in evidence weighting."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "regression fallacy",
      "alternative_labels": [
        "regression to the mean neglect",
        "regression neglect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A reasoning error in which regression toward the mean is overlooked or misattributed to a salient causal intervention rather than recognized as the natural tendency of extreme observations to be followed by less extreme observations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Causal assessment of post-Steady Watch attack decline in District X",
      "decision_point_description": "When attributing the drop from eleven attacks to three or four per week, the participant treated the decline as evidence for checkpoints without considering that the week-five spike was an extreme outlier likely to revert on its own.",
      "affected_reasoning_operation": "Statistical reasoning / causal attribution",
      "bias_specific_mechanism": "Neglect of regression to the mean: extreme high values tend to move toward their long-run average, but the participant focused on the salient intervention as the cause of the decline rather than on the statistical extremity of the baseline week.",
      "manifestation_in_interview": "The participant later explicitly recognized that eleven against a baseline of three was a huge jump and that huge jumps usually do not stay huge, but at the time focused on what 'we did in response' rather than on how unusual the single week was.",
      "effect_on_reasoning_or_decision": "Led the participant to attribute the attack decline to Steady Watch and overestimate the causal effect of the checkpoint posture change.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Not in much depth, honestly. I noted the other factors existed, but I didn't really sit down and ask how much of that drop would've happened on its own just because week five was such an extreme outlier to begin with.",
          "evidence_explanation": "This directly states that the participant did not consider natural reversion from an extreme outlier when evaluating the decline."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe how extreme it was compared to everything before it. Eleven against a baseline of three is a huge jump, and huge jumps like that don't usually stay huge. I focused on what we did in response rather than on how unusual that single week was to begin with.",
          "evidence_explanation": "The participant retrospectively identifies the neglected regression-to-the-mean reasoning: the extreme spike was likely to fall even without intervention."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged this exact reasoning flaw, indicating retrospective correction but no real-time adjustment during the causal assessment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for regression fallacy was not available; the label and mechanism are from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias",
        "overgeneralization from a single case"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the probability or expected outcome of a new case by its resemblance to a salient or available prior case rather than by base rates or case-specific diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Recommendation to extend Operation Steady Watch to District Y",
      "decision_point_description": "The commander asked whether Steady Watch should be extended to District Y; the participant recommended rollout expecting a similar sharp drop based on the District X result.",
      "affected_reasoning_operation": "Generalization / probabilistic reasoning",
      "bias_specific_mechanism": "Overweighting a single salient prior case, District X, as a validated model and expecting District Y to behave similarly, while underweighting case-specific information that District Y's spike had a different unresolved driver and had already eased without posture change.",
      "manifestation_in_interview": "The participant reported that District X felt like a validated model and that they leaned on the District X result as the stronger signal, despite noting the District Y handler's different unresolved driver.",
      "effect_on_reasoning_or_decision": "Led to recommending resource commitment to roll out Steady Watch to District Y without a separate cause analysis and expecting a similar sharp drop.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Given what I'd just seen in District X, I recommended rolling Steady Watch out to District Y too, expecting a similar sharp drop.",
          "evidence_explanation": "The expectation of a similar sharp drop is explicitly based on resemblance to the District X case rather than on District Y-specific diagnostic information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I considered it, but time was short and District X felt like a validated model at that point — we'd just seen checkpoints turn a spike around. The Y handler did mention their spike had a different, still-unresolved driver, which I noted, but I leaned on the District X result as the stronger signal for what to do next.",
          "evidence_explanation": "The participant treats one salient prior case as the stronger signal and discounts the distinguishing feature of the new case, which is the core representativeness-heuristic pattern."
        }
      ],
      "correction_or_counterevidence": "Later in the interview, the participant noted that if District Y's spike had faded without any posture change, it would have made them second-guess the District X read quickly, suggesting retrospective awareness that the District Y case was not necessarily equivalent.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the representativeness heuristic was not available; the label and mechanism are from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value or trend as an anchor and to make insufficient adjustments from that anchor, particularly under time pressure.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Forecast for commander's brief after two weeks of post-implementation data",
      "decision_point_description": "The participant presented a forecast of continued low attack tempo of three to four per week, framed as Steady Watch holding, rather than a wider uncertainty range.",
      "affected_reasoning_operation": "Forecasting / uncertainty expression",
      "bias_specific_mechanism": "Anchored on the recent clean trend of three to four attacks per week and insufficiently adjusted away from that anchor to account for limited two-week post-implementation data and residual uncertainty.",
      "manifestation_in_interview": "The participant acknowledged that a wider range and a caveat about the short track record would have been possible, but chose the narrow forecast because the trend line looked clean and the commander wanted decisiveness.",
      "effect_on_reasoning_or_decision": "Produced an overly decisive forecast that understated uncertainty in a command brief.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "With the brief three days out and only two weeks of post-implementation data, I presented a forecast of continued low attack tempo, three to four a week, framed as Steady Watch holding.",
          "evidence_explanation": "The participant anchored the forecast on the recent three-to-four attack trend even though the evidentiary basis was only two weeks old."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I could have given a wider range and flagged that two weeks isn't much of a track record, but the trend line looked clean and the commander wanted something decisive for the brief, not a hedge.",
          "evidence_explanation": "This indicates insufficient adjustment away from the clean trend anchor despite awareness that the data was limited."
        }
      ],
      "correction_or_counterevidence": "No correction was described for this forecast decision within the interview.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The insufficient adjustment mechanism under time pressure is supported by the retrieved Rastogi et al. (2022) passage on anchoring-and-adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Anchoring-and-adjustment involves insufficient adjustment from an initial anchor, especially when time is limited.",
          "relevance_to_this_occurrence": "The participant faced time pressure from the commander's brief and under-adjusted from the recent clean trend, producing an overly narrow forecast."
        }
      ]
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis is based on a single retrospective interview, so it cannot establish stable individual dispositions or fully separate real-time reasoning from later reconstruction.",
    "Retrieved corpus support was available for confirmation bias and anchoring bias; regression fallacy and representativeness heuristic are identified from general cognitive-science knowledge because no suitable retrieved corpus passages were available.",
    "The transcript relies on self-report, so some reasoning processes may be rationalized after the fact rather than directly observed.",
    "Some findings overlap in the same causal-assessment episode but are treated as distinct because they involve separable mechanisms: confirmatory evidence weighting versus neglect of statistical regression."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "MD_Biased_2_Sonar_on",
  "interview_id": "MD_Biased_2",
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
