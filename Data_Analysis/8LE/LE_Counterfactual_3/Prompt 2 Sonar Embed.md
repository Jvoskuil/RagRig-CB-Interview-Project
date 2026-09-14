You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. This is for our case-review research file — I'll ask you to walk through your decision-making on the Riverside apartment case, and it's fine to say you don't recall something exactly. Okay to start?

Participant: Sure, go ahead.

Interviewer: Can you start with your role and how the case came to you?

Participant: I was lead detective, my partner and I caught it together after patrol secured the scene. Apartment homicide, young woman, found by a coworker who came by when she missed a shift. We split canvass and paperwork like usual.

Interviewer: Walk me through the scene.

Participant: No forced entry, deadbolt engaged from inside. That tells you something — either she let someone in, or it's somebody with access. Pulled her phone, found a breakup with her ex about three weeks back, some heated texts, and he had a prior domestic disturbance call at that same address, maybe eight months earlier. Scene damage was mostly contained to the bedroom. Between the lock, the texts, and his history, that's where my attention went first. We also swabbed the scene and pushed it to an expedited lab track — there was already some media interest building, so we had a faster turnaround than usual, maybe a day instead of two or three.

Interviewer: What was the objective at that stage?

Participant: Get a working theory solid enough to direct the canvass without locking in before we had more to go on. Same clock as always — witness memory starts fading fast, and if it is someone connected to her, you don't want to give them time to get comfortable or leave town.

Interviewer: Let's reconstruct the timeline.

Participant: Day one, scene work, the ex's history surfaces, swabs go out on the expedited track. Overnight, the lab actually gets back to us — negative, no DNA match to him at the scene. Day two morning, we walk into the unit briefing already knowing that. Alibi still has a two-hour gap at that point. Day three, a second witness closes that gap, and we finally sit down properly with the rear-entrance witness, who gives us a much sharper description — turns out to match a guy with a burglary record in that block. Day four, we're drafting the referral for the DA liaison.

Interviewer: First decision point — naming the ex as primary on day one, before any lab results.

Participant: Right, nothing back yet at that point. We could've waited on forensics and the full canvass, or treated the rear-entrance sighting as equally weighted from the start. I named him primary anyway — the domestic history, the breakup timing, the locked door, that's a pattern worth acting on with the manpower we had. The rear entrance was just one line from a passerby at that stage, nothing to build resources around yet.

Interviewer: What made that combination feel strong enough to commit to over waiting?

Participant: Mostly experience. You don't get to split resources evenly on day one, so you go where the documented history points. That felt like a defensible use of the shift.

Interviewer: Second decision point — the unit briefing, and this time you already had the negative DNA result in hand.

Participant: Right, that's the part that made that morning different. We walk in already knowing the swab didn't match him. My partner still laid out the domestic-call history pretty forcefully, made the case that the DNA gap didn't mean much on its own. One of the junior guys raised the rear-entrance lead again, said it was worth a real look given the negative result, but it didn't get much traction — people moved on to warrant logistics for the ex fairly quickly. By the end of that meeting the case log still had him as primary, and nobody was formally assigned to run down the loitering report.

Interviewer: How did you square keeping him primary with a negative result already sitting in front of the room?

Participant: I didn't see it as ignoring it. The domestic history and the locked door were still unexplained either way, and everyone in the room seemed to land in the same place once my partner made the case — the DNA on its own didn't feel like it outweighed that. Reopening it right then would've meant pulling someone off the warrant work we were already moving on, and with the room settled, that didn't feel like the priority.

Interviewer: Was there a point where the negative result almost changed the direction of that meeting?

Participant: Briefly, when the junior detective brought it up. But once my partner and the lieutenant seemed comfortable holding the line, it didn't really get pushed further.

Interviewer: Third decision point — day three, alibi closes and the rear-entrance description sharpens.

Participant: That was the harder morning. Second witness closes the two-hour gap completely, and the rear-entrance guy's description gets a lot more specific — matches someone with a burglary record nearby. I still didn't shift the primary theory. The DNA was already a known factor by then, so it wasn't new information exactly — what was new was the alibi and the detailed description, and I kept coming back to the fact that it wasn't enough to undo what we'd already built around him, even though I could see it was chipping away at the case in a way the DNA result alone hadn't. On their own, without independent corroboration, I didn't treat them as decisive enough to flip the case. I logged the alternative as secondary and kept digging on our end.

Interviewer: What was the basis for treating the closed alibi and the new description as not yet decisive?

Participant: One witness closing a gap and one detailed description aren't the same as physical evidence tying someone to the scene. The domestic history was still sitting there unaddressed if it wasn't him. I didn't want to swing the whole case on two pieces of testimony without corroboration.

Interviewer: Fourth decision point — drafting the referral memo.

Participant: By day four we had two live threads: the ex, thinner now, and the burglary-record guy, whose statement was the freshest and most detailed thing in the file. When I wrote the summary for the DA liaison, that statement got the most space and read as the strongest piece on the page, more than the older scene notes or the original canvass material.

Interviewer: What gave it that weight in the writing itself?

Participant: Partly the detail — clearer description, better timing. But honestly, it was also just the last substantial thing that had come in before I sat down to write, so it was what was fresh in my head. I hadn't gone back and stacked it against the earlier material for corroboration, it just carried into the draft that way. The DA liaison ended up asking for supplemental work before filing on either of them.

Interviewer: If the DNA result had come back after the briefing instead of before it, do you think the meeting would have gone differently?

Participant: Possibly. Walking in without that result already known, the room might have leaned harder into the domestic history with less friction, since there'd have been nothing to explain away yet. Having it already on the table at least got it mentioned, even if it didn't change the outcome much.

Interviewer: Had you seen a case before where a negative result early on still didn't shift the team's direction?

Participant: A couple times, yeah. It's usually a reminder to keep digging on the alternative rather than treating one result as the final word either way.

Interviewer: Looking back, is there a moment you'd want to redo?

Participant: Probably assigning someone concretely to the rear-entrance lead right at that second briefing, once the negative result was already in the room. That felt like the moment a small procedural step could've changed the pace of everything after it.

Interviewer: Anything else you'd want on record about how the case moved through those points?

Participant: Just that nothing felt reckless in the moment. Every step had something behind it. It's only looking at the whole thing end to end now that the gaps stand out more.

Interviewer: That's a good place to stop. Thanks for going through it in this detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Counterfactual_3",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Homicide Detective",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "The Riverside Apartment Homicide - Early Forensic Return Variant",
    "scenario_summary_internal": "A homicide detective is interviewed about the same Riverside apartment case as the paired scenario, but with one causal variable changed: the forensic lab returns the negative DNA result before the unit briefing instead of after it. This means the team already knows the ex-partner's DNA does not match the scene when they collectively commit to him as primary suspect, rather than learning it after commitment. All other material facts, actors, evidence items, and the four-decision-point structure are held constant. The interview probes how the team weighed a known disconfirming result during collective decision-making, how the detective reconciled subsequently closing alibi and alternative-suspect evidence, and how the final referral memo was drafted.",
    "occupational_realism": {
      "objective": "Identify and build a prosecutable case against the individual responsible for the victim's death within the critical 72-hour investigative window.",
      "setting": "Mid-size city homicide unit; apartment crime scene, precinct briefing room, and follow-up canvass over a 4-5 day period, with an expedited forensic lab turnaround due to media attention",
      "constraints": [
        "72-hour window before witness memory degrades and suspect can flee jurisdiction",
        "expedited lab turnaround (results available within roughly 24 hours given media pressure)",
        "pressure from lieutenant and DA liaison for a chargeable theory",
        "partner detective present at most decisions, creating shared accountability",
        "media attention increasing pressure for a quick resolution"
      ],
      "stakeholders": [
        "lead detective (interviewee)",
        "partner detective",
        "homicide unit lieutenant",
        "crime scene technicians",
        "DA liaison",
        "victim's family",
        "ex-boyfriend (initial suspect)",
        "neighbor witness"
      ],
      "technical_terms_to_use": [
        "scene canvass",
        "chain of custody",
        "working theory",
        "case referral",
        "timeline reconstruction",
        "corroborating statement",
        "probable cause",
        "expedited turnaround"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "cognitive dissonance",
        "groupthink",
        "recency effect",
        "anchoring",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "victim found deceased in locked apartment, no forced entry",
          "recent breakup with ex-boyfriend documented in texts",
          "ex-boyfriend has a prior domestic disturbance call at victim's address",
          "no immediate signs of struggle beyond bedroom",
          "scene swabs collected and sent to an expedited lab track given media interest"
        ],
        "new_information_after_decision": [
          "ex-boyfriend's alibi partially corroborated by a coworker but with a two-hour gap",
          "unidentified male seen loitering near the building's rear entrance per a passerby, unconfirmed at this stage"
        ],
        "alternatives": [
          "treat ex-boyfriend as primary working theory and prioritize resources on his alibi and history",
          "hold off naming a primary theory until scene forensics and full canvass are complete",
          "pursue the rear-entrance sighting as an equally weighted lead"
        ],
        "intended_action": "Detective designates the ex-boyfriend as the primary working theory and directs the team to focus canvass and warrant efforts around him, before any forensic results are back."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "unit briefing held the next morning; lieutenant and three colleagues present",
          "expedited lab result has just returned: no DNA match to the ex-boyfriend at the scene",
          "partner detective still voices support for the ex-boyfriend theory citing the prior domestic call and breakup timing",
          "one junior detective mentions the rear-entrance sighting is worth pursuing given the negative DNA result but is not pressed further",
          "alibi gap of two hours has not yet been resolved"
        ],
        "new_information_after_decision": [
          "team consensus recorded in the case log as ex-boyfriend remaining the primary suspect despite the negative DNA result",
          "the junior detective's rear-entrance lead is deprioritized without a documented follow-up assignment"
        ],
        "alternatives": [
          "revise the working theory toward equal weighting of the rear-entrance lead given the known negative DNA result",
          "assign a team member to independently verify the rear-entrance sighting before finalizing the case direction",
          "adopt the group's converging view that the domestic history still justifies treating the ex-boyfriend as primary"
        ],
        "intended_action": "The detective aligns with the team's converging view that the ex-boyfriend should remain primary notwithstanding the known negative DNA result, without assigning independent verification of the dissenting lead."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "a second witness closes the ex-boyfriend's two-hour alibi gap",
          "the rear-entrance witness is re-interviewed and gives a detailed description matching an individual with a prior burglary record in the area",
          "the negative DNA result from phase 2 remains on file and undisputed"
        ],
        "new_information_after_decision": [
          "detective requests additional review focused on reconciling the closed alibi and the detailed alternative description with the existing theory rather than broadening the suspect pool",
          "case referral memo to the DA liaison still lists the ex-boyfriend as primary person of interest, with the new witness description noted as a secondary, unresolved lead"
        ],
        "alternatives": [
          "revise the primary theory to prioritize the burglary-record individual given the closed alibi and fresh, detailed statement",
          "maintain the ex-boyfriend as primary suspect and treat the alibi closure and detailed statement as insufficient to override the existing theory",
          "pause the referral and request a fresh case review from an uninvolved detective"
        ],
        "intended_action": "The detective maintains the ex-boyfriend as the primary theory, characterizing the closed alibi and the detailed alternative description as not yet dispositive, and proceeds toward referral."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "final pre-referral case review meeting",
          "the most recently obtained statement (burglary-record individual's description) is the most vivid and detailed piece of evidence in the file",
          "older canvass statements and the initial scene assessment are comparatively thin on physical detail",
          "DA liaison requests the detective's best-supported theory for filing"
        ],
        "new_information_after_decision": [
          "case is referred to the DA with the most recent witness statement weighted heavily in the summary, overshadowing earlier, less detailed but equally relevant scene evidence",
          "DA liaison requests supplemental investigation before filing charges on either individual"
        ],
        "alternatives": [
          "weight all evidence according to its evidentiary strength and chain of custody rather than recency",
          "give disproportionate emphasis to the most recently gathered statement when drafting the referral summary",
          "request a formal weighted timeline review before submitting"
        ],
        "intended_action": "The detective drafts the referral summary giving the most recently obtained witness statement disproportionate prominence relative to earlier evidence of comparable or greater relevance."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how you were first briefed on this case.",
        "What was your initial read on the scene when you arrived?"
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from scene arrival to case referral.",
        "What information came in at each stage, and when, particularly the forensic result?"
      ],
      "decision_point_probes": [
        "What cues led you to focus on the ex-boyfriend before any lab results were back?",
        "How did the team's discussion change once the DNA result was already on the table at the briefing?",
        "What alternatives did you or the team consider once the negative result was known?",
        "What was the basis for maintaining the theory after the alibi gap closed?",
        "Had you seen cases before where an early theory didn't hold up despite a negative forensic result? How did that shape your approach here?",
        "How much time pressure did you feel at each of these points?",
        "How confident were you in the theory at each stage, and what would have changed that confidence?",
        "If the DNA result had come back after the briefing instead of before it, how do you think the team's discussion would have gone?"
      ],
      "closing_hypotheticals": [
        "If the lab turnaround had been slower and the negative result had arrived after the briefing instead of before, do you think the team's direction would have looked different?",
        "What would you tell a junior detective about weighing a known disconfirming result against team consensus?",
        "Looking back, was there a moment you'd want to redo?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 2,
        "mechanism": "Detective adopts the team's converging view to retain the ex-boyfriend as primary suspect even though the negative DNA result is already known at the time of the briefing, without assigning independent verification of the dissenting rear-entrance lead",
        "affected_reasoning_operation": "collective decision adoption and dissent evaluation",
        "evidence_available_at_time": [
          "negative DNA result, already returned before the briefing",
          "partner detective's continued vocal support for the ex-boyfriend theory",
          "junior detective's brief mention of the rear-entrance lead given the negative result",
          "lieutenant's presence and implicit expectation of a unified direction"
        ],
        "required_textual_manifestation": "detective recounts the briefing occurring after the DNA result was already in hand, describes the room converging on retaining the ex-boyfriend as primary despite that result, and notes the dissenting lead was mentioned but not assigned for independent follow-up, framed as a natural outcome of the meeting rather than a contested choice",
        "plausible_nonbias_interpretation": "the domestic-call history and locked-door context may still have been judged, in the room, as outweighing a single negative swab, making team convergence a reasonable reflection of the totality of evidence rather than pressure to conform",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "conformity", "consensus pressure", "dissent suppression"]
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "decision_point": 3,
        "mechanism": "Detective reinterprets the closed alibi gap and the newly detailed alternative-suspect description as insufficient to override the already-committed ex-boyfriend theory, continuing to treat the previously known negative DNA result as non-dispositive rather than revising the theory",
        "affected_reasoning_operation": "evidence reconciliation and theory revision",
        "evidence_available_at_time": [
          "alibi gap closed by a second witness",
          "newly detailed description of an alternative individual with a burglary record",
          "the already-known negative DNA result from the prior briefing"
        ],
        "required_textual_manifestation": "detective explicitly frames the closing alibi and the detailed alternative statement as not yet decisive while continuing to treat the ex-boyfriend as primary suspect, without engaging substantively with the alternative lead's specifics",
        "plausible_nonbias_interpretation": "detective could reasonably argue that an alibi correction and a single detailed description, without independent corroboration, do not by themselves establish a different suspect",
        "strength": "subtle",
        "do_not_make_explicit": ["cognitive dissonance", "rationalization", "reducing discomfort"]
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "decision_point": 4,
        "mechanism": "The most recently obtained witness statement is given disproportionate weight in the referral summary relative to earlier, comparably or more relevant scene evidence, driven partly by its recency of acquisition rather than solely its evidentiary strength",
        "affected_reasoning_operation": "evidence weighting and summary drafting",
        "evidence_available_at_time": [
          "recent detailed witness description of alternative individual",
          "earlier, thinner canvass statements and initial scene notes",
          "chain-of-custody documentation for all evidence"
        ],
        "required_textual_manifestation": "detective describes drafting the referral summary and explains giving the newest statement prominent placement or emphasis, noting it was the last substantial account received and remained most mentally available even without established corroboration, alongside its greater descriptive detail",
        "plausible_nonbias_interpretation": "the most recent statement could genuinely be the most detailed and probative evidence, warranting emphasis on its merits alone",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "recency bias", "most recent information"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "LE_Biased_3",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "not applicable to counterfactual condition"
    },
    "counterfactual_specification": {
      "causal_variable": "timing of the forensic DNA result relative to the unit briefing",
      "original_state": "In the paired scenario (LE_Biased_3), the negative DNA result returns on day three, after the day-two unit briefing has already formalized the ex-boyfriend as primary suspect through team consensus.",
      "counterfactual_state": "In this scenario, an expedited lab track returns the same negative DNA result before the day-two unit briefing, so the team already knows the result is negative at the moment it collectively commits to the ex-boyfriend as primary suspect.",
      "variables_to_hold_constant": [
        "victim, scene facts, and locked-door context",
        "ex-boyfriend's domestic-call history and breakup timeline",
        "rear-entrance witness and eventual detailed description matching a burglary-record individual",
        "personnel present (partner detective, lieutenant, junior detective, DA liaison)",
        "four-decision-point structure and overall chronology length",
        "the three targeted bias instances and their general character",
        "referral drafting process and DA liaison's request for supplemental work"
      ],
      "expected_causal_difference": "Because the disconfirming result is known at the point of collective commitment rather than discovered afterward, the groupthink instance now involves the team converging on the theory in the face of already-known disconfirming evidence, while the cognitive dissonance instance is triggered by the subsequently closing alibi and detailed alternative description rather than by the DNA result itself, which has already been absorbed into the team's shared narrative.",
      "causal_test_question": "Does moving the disconfirming forensic result earlier, so it is known before the team's collective commitment rather than encountered after it, change how the team and the detective process that evidence relative to the paired scenario, or does the same reasoning pattern persist regardless of when the disconfirming evidence arrives?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points appear in the interview",
      "Confirm exactly 1 groupthink instance embedded only at decision point 2, now incorporating the already-known negative DNA result",
      "Confirm exactly 1 cognitive dissonance instance embedded only at decision point 3, triggered by alibi closure and detailed alternative description rather than by the DNA result",
      "Confirm exactly 1 recency effects instance embedded only at decision point 4",
      "Confirm no bias labels or psychological terminology appear in the public interview text",
      "Confirm word count falls between 1215 and 1485 words",
      "Confirm each decision point includes at least two plausible alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm consequences described do not mechanically prove bias presence",
      "Confirm decision point 1 contains no intended bias instance and remains a neutral/realistic anchor decision",
      "Confirm only the DNA-result timing variable changed relative to LE_Biased_3, with all other material facts held constant",
      "Confirm the counterfactual causal variable is singular and not confounded with an unrelated second change"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "counterfactual",
    "exact_occurrence_manifest": [
      {
        "bias": "Cognitive dissonance",
        "occurrences": 1,
        "mechanism_constraint": "must be triggered by the alibi closure and detailed alternative description at decision point 3, not by the DNA result itself, since the DNA result is already known by that point"
      },
      {
        "bias": "Recency Effects",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Groupthink",
        "occurrences": 1,
        "mechanism_constraint": "must occur at decision point 2 with the negative DNA result already known in the room at the time of convergence"
      }
    ],
    "target_bias_names": ["Cognitive dissonance", "Recency Effects", "Groupthink"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Cognitive dissonance", "requested_occurrences": 1 },
      { "bias": "Recency Effects", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "gt_01", "bias": "Groupthink" },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance" },
      { "instance_id": "re_01", "bias": "Recency Effects" }
    ],
    "intended_decision_points": [
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 2 },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "decision_point": 3 },
      { "instance_id": "re_01", "bias": "Recency Effects", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Team converges on retaining the ex-boyfriend as primary suspect despite an already-known negative DNA result, without assigning independent verification of the dissenting rear-entrance lead",
        "affected_reasoning_operation": "collective decision adoption and dissent evaluation",
        "evidence_source": "briefing discussion occurring after the DNA result is already in hand; partner's continued support; junior detective's dissenting mention",
        "distinctiveness_requirement": "must occur at decision point 2, distinct from the individual-level reconciliation at decision point 3 (cd_01) and the weighting behavior at decision point 4 (re_01); the disconfirming DNA evidence must already be present in the room rather than arriving afterward, distinguishing this instance from the paired biased scenario's version"
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "mechanism": "Reinterpreting the closed alibi gap and the newly detailed alternative-suspect statement as insufficient to override the already-committed theory, while treating the earlier-known negative DNA result as settled rather than reopening it",
        "affected_reasoning_operation": "evidence reconciliation and theory revision",
        "evidence_source": "closed alibi statement and detailed alternative-suspect description at decision point 3",
        "distinctiveness_requirement": "must occur at decision point 3 and must be triggered by the alibi closure and detailed statement, not by the DNA result, since the DNA result was already processed collectively at decision point 2 in this counterfactual variant"
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "mechanism": "Disproportionate weighting of the most recently obtained witness statement over earlier comparable evidence when drafting the referral summary, tied partly to recency of acquisition",
        "affected_reasoning_operation": "evidence weighting and summary drafting",
        "evidence_source": "most recent witness description versus earlier canvass statements and scene notes",
        "distinctiveness_requirement": "must occur during final referral drafting at decision point 4, tied specifically to recency of acquisition rather than theory commitment or group consensus, unchanged in character from the paired biased scenario"
      }
    ],
    "intended_strength": [
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "subtle" },
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "strength": "subtle" },
      { "instance_id": "re_01", "bias": "Recency Effects", "strength": "subtle" }
    ],
    "paired_scenario_id": "LE_Biased_3",
    "counterfactual_variable": {
      "name": "timing of the forensic DNA result relative to the unit briefing",
      "original_state": "Negative DNA result returns on day three, after the day-two unit briefing has already formalized the ex-boyfriend as primary suspect (LE_Biased_3).",
      "changed_state": "Negative DNA result returns before the day-two unit briefing via an expedited lab track, so the team already knows the result when it converges on the ex-boyfriend as primary suspect.",
      "variables_to_hold_constant": [
        "victim, scene facts, and locked-door context",
        "ex-boyfriend's domestic-call history and breakup timeline",
        "rear-entrance witness and eventual detailed description matching a burglary-record individual",
        "personnel present (partner detective, lieutenant, junior detective, DA liaison)",
        "four-decision-point structure and overall chronology length",
        "the three targeted bias instances and their general character",
        "referral drafting process and DA liaison's request for supplemental work"
      ]
    },
    "scenario_id": "LE_Counterfactual_3",
    "domain_id": "LE",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per bias, reallocated relative to the paired scenario to accommodate the shifted timing of the DNA result: groupthink remains at decision point 2 but now incorporates the already-known negative result as the disconfirming evidence present at the moment of convergence; cognitive dissonance shifts its trigger evidence to the alibi closure and detailed alternative description at decision point 3, since the DNA result is no longer novel at that point; recency effects remains unchanged at decision point 4. Decision point 1 held bias-free as a neutral anchor, matching the paired scenario.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "victim, scene facts, and locked-door context",
      "ex-boyfriend's domestic-call history and breakup timeline",
      "rear-entrance witness and eventual detailed description matching a burglary-record individual",
      "personnel present (partner detective, lieutenant, junior detective, DA liaison)",
      "four-decision-point structure and overall chronology length",
      "the three targeted bias instances and their general character",
      "referral drafting process and DA liaison's request for supplemental work",
      "target word count range (1,215-1,485 words)"
    ],
    "generation_warnings": [
      "Shifting the DNA result earlier necessarily changes the evidentiary content available at decision point 2 (it now includes a negative forensic result) and at decision point 3 (which no longer includes a fresh negative DNA shock). This is an intended consequence of the single causal-variable change and does not constitute a second uncontrolled variable, but validators should confirm that no second unrelated fact (e.g., personnel, tone, or unrelated timeline length) was altered when auditing causal minimality."
    ]
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "dp1_initial_primary_theory",
          "speaker": "Participant",
          "segment_type": "decision_point_1",
          "raw_interview_anchor": "\"I named him primary anyway — the domestic history, the breakup timing, the locked door, that's a pattern worth acting on\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The detective designates the ex as a working theory before forensic results, with a documented plausible resource-allocation rationale and no hidden target bias assigned to this segment."
        },
        {
          "segment_id": "dp2_briefing_known_negative_dna",
          "speaker": "Participant",
          "segment_type": "decision_point_2",
          "raw_interview_anchor": "\"We walk in already knowing the swab didn't match him\"; \"once my partner made the case ... the DNA on its own didn't feel like it outweighed that\"; \"nobody was formally assigned to run down the loitering report\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gt_01"
          ],
          "ground_truth_rationale": "Groupthink target: the team converges on retaining the ex as primary despite the known negative DNA result, and the dissenting rear-entrance lead receives no independent follow-up."
        },
        {
          "segment_id": "dp3_alibi_closed_alternative_sharpened",
          "speaker": "Participant",
          "segment_type": "decision_point_3",
          "raw_interview_anchor": "\"Second witness closes the two-hour gap completely\"; \"I kept coming back to the fact that it wasn't enough to undo what we'd already built around him\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cd_01"
          ],
          "ground_truth_rationale": "Cognitive dissonance target: the closed alibi and detailed alternative description are framed as insufficient to override the already-committed ex theory, with the known negative DNA treated as non-dispositive."
        },
        {
          "segment_id": "dp4_referral_memo_recent_statement",
          "speaker": "Participant",
          "segment_type": "decision_point_4",
          "raw_interview_anchor": "\"that statement got the most space and read as the strongest piece on the page\"; \"it was also just the last substantial thing that had come in\"",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "re_01"
          ],
          "ground_truth_rationale": "Recency Effects target: the newest detailed witness statement receives disproportionate prominence in the referral memo partly because it was fresh in memory rather than because of a complete comparative evidence review."
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
    "analysis_scope_note": "Single interview transcript analyzed for bias-specific mechanisms in case-review reasoning; resource constraints, ordinary uncertainty, and absence of information were not classified as biases unless a distinct cognitive mechanism was evident."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "recency effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring and adjustment heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial value or hypothesis and to make insufficient adjustments when subsequent information arrives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-three case-theory update after alibi closure and rear-entrance description",
      "decision_point_description": "Whether to shift the primary suspect from the ex to the burglary-record individual after the second witness closed the ex's alibi gap and the rear-entrance description sharpened.",
      "affected_reasoning_operation": "Evidence weighting / hypothesis updating",
      "bias_specific_mechanism": "The initial ex-suspect hypothesis functions as an anchor; new contradictory information is evaluated relative to that existing theory and is adjusted insufficiently rather than triggering full re-evaluation.",
      "manifestation_in_interview": "Despite negative DNA, a closed alibi, and a more specific rear-entrance description matching a local burglary suspect, the participant retained the ex as primary and logged the alternative only as secondary.",
      "effect_on_reasoning_or_decision": "The case direction remained anchored on the initial suspect, so the alternative lead did not receive primary status at that point, likely delaying fuller pursuit of the alternative suspect.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I still didn't shift the primary theory. The DNA was already a known factor by then, so it wasn't new information exactly — what was new was the alibi and the detailed description, and I kept coming back to the fact that it wasn't enough to undo what we'd already built around him, even though I could see it was chipping away at the case in a way the DNA result alone hadn't. On their own, without independent corroboration, I didn't treat them as decisive enough to flip the case. I logged the alternative as secondary and kept digging on our end.",
          "evidence_explanation": "The phrase \"what we'd already built around him\" shows the prior case theory serving as the reference point; new evidence is judged by whether it is sufficient to \"undo\" the initial hypothesis, a classic insufficient-adjustment pattern."
        }
      ],
      "correction_or_counterevidence": "The participant logged the alternative as secondary and continued investigating, and he offered legitimate non-bias reasons such as lack of physical corroboration and unaddressed domestic history. These considerations weaken but do not eliminate the anchoring mechanism because the new information was not treated as triggering a full re-evaluation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "A retrieved passage from Rastogi et al. (2022) supports the anchoring-and-adjustment mechanism and insufficient adjustment away from an anchor; the interview shows an analogous failure to sufficiently adjust away from an initial suspect.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "Anchoringandadjustment. ipants’ likelihood of suciently adjusting away from the incorrect AI prediction increased as the time allocated increased. This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "Insufficient adjustment away from an initial anchor; de-anchoring is affected by available time and cognitive resources.",
          "relevance_to_this_occurrence": "The participant's reasoning shows the same insufficient-adjustment pattern: the initial suspect hypothesis remained the reference point and was not sufficiently revised despite accumulating counterevidence."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "recency effect",
      "alternative_labels": [
        "recency bias",
        "availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency for recently encountered information to be more available in memory and therefore weighted more heavily than older information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-four drafting of DA referral memo",
      "decision_point_description": "How much weight and space to give the two suspect threads in the written summary for the DA liaison.",
      "affected_reasoning_operation": "Information weighting / written communication decision",
      "bias_specific_mechanism": "Recency-based memory accessibility made the latest substantial witness statement easier to recall, so it was weighted as the strongest item without systematic comparison against earlier material.",
      "manifestation_in_interview": "The newest witness statement received the most space in the referral memo and read as the strongest piece; the participant acknowledged that freshness influenced the weighting.",
      "effect_on_reasoning_or_decision": "The memo presented the burglary-record lead as the strongest thread, and the DA liaison requested supplemental work before filing; earlier scene notes and canvass material were not re-evaluated for corroboration before drafting.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Partly the detail — clearer description, better timing. But honestly, it was also just the last substantial thing that had come in before I sat down to write, so it was what was fresh in my head. I hadn't gone back and stacked it against the earlier material for corroboration, it just carried into the draft that way.",
          "evidence_explanation": "The participant explicitly identifies recency (\"the last substantial thing\") and memory freshness (\"what was fresh in my head\") as a determinant of the memo's weighting, and states that he did not systematically compare it with older material."
        }
      ],
      "correction_or_counterevidence": "The participant also cited genuinely relevant features of the new statement—clearer description and better timing—as legitimate reasons for its weight. This means recency was not necessarily the only cause, but the explicit reliance on freshness and lack of corroboration check supports a recency effect.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the recency-effect/availability mechanism was unavailable; the label derives from general knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "conformity bias",
      "alternative_labels": [
        "groupthink",
        "social proof",
        "authority bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant / team decision",
      "possible_decision_episode_label": "Day-two unit briefing decision to keep ex as primary despite negative DNA",
      "supporting_interview_quote": "Briefly, when the junior detective brought it up. But once my partner and the lieutenant seemed comfortable holding the line, it didn't really get pushed further.",
      "plausible_mechanism": "The expressed comfort of the partner and lieutenant may have functioned as social or authority evidence that the existing primary theory was acceptable, reducing continued scrutiny of the rear-entrance lead.",
      "why_not_identified": "The interview does not clearly show that the participant privately disagreed or changed his own evaluation because of social pressure; normal operational consensus and his stated reliance on the domestic history and locked door are plausible competing explanations."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is retrospective self-report, so real-time reasoning may be reconstructed or incomplete.",
    "There is no experimental baseline, so classifications rest on the participant's own description of reasoning rather than direct measurement.",
    "Retrieved corpus support was available for anchoring bias but not for the recency effect; the recency finding relies on general cognitive-science knowledge.",
    "The analysis does not classify initial reliance on documented history under time pressure as a bias unless a distinct bias-specific mechanism was evident in the reported reasoning."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Counterfactual_3_Sonar_on",
  "interview_id": "LE_Counterfactual_3",
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
