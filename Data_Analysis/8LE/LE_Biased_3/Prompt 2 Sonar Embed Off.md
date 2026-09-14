You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is for our case-review research file — I'll be asking you to walk me through your decision-making on the Riverside apartment case, and it's fine to say "I don't remember" if something's unclear. Sound okay?

Participant: Yeah, that's fine. It's not a case I've forgotten much about anyway.

Interviewer: Good. Can you start with your role and how you came into the case?

Participant: I was lead detective, second-in on scene after patrol secured it. My partner and I caught it together — we split the canvass and the paperwork most of the time. It was a apartment homicide, young woman, found by a coworker who came by when she didn't show up for a shift.

Interviewer: Walk me through what you found when you got there.

Participant: No forced entry, door was locked from inside, deadbolt engaged. That narrows things fast — either she let someone in, or it's someone with access. We pulled her phone and found a breakup with her ex about three weeks prior, some heated texts. He'd also had a prior domestic disturbance call at that same address, maybe eight months back, neighbor called it in. Scene itself was contained mostly to the bedroom — no real struggle elsewhere in the apartment. So between the lock, the ex's history, and the texts, that's where my head went first.

Interviewer: What was the objective at that point?

Participant: Build a working theory fast enough to direct the canvass and get ahead of any warrant we'd need, but not so fast we lock ourselves in before the scene work comes back. We had the usual clock — 72 hours or so before witness memory gets soft and, frankly, before a suspect who's alarmed has time to leave the area.

Interviewer: Let's reconstruct the timeline. What came in, and when?

Participant: Day one, scene work and the ex's history surface. Day one evening, we get a partial alibi from his coworker, but there's a two-hour gap in it. Same day, a passerby mentions a man loitering near the rear entrance — unconfirmed, no real description yet. Day two morning, unit briefing. Swabs go to the lab. Day three, lab comes back negative for the ex's DNA at the scene, and a second witness closes his alibi gap. Same day, we finally sit down properly with the rear-entrance witness and get a much better description — turns out to match a guy with a burglary record in that block. Day four, we're drafting the referral for the DA liaison.

Interviewer: Let's go decision by decision. First one — naming the ex as the primary theory on day one. What alternatives did you weigh?

Participant: We could've held off naming anybody until forensics and the full canvass were in, or we could've treated the rear-entrance sighting as equally weighted from the start. I chose to name him primary and put resources there — the domestic call history plus the locked door plus the breakup timing, that's a real pattern you see in these cases. I wasn't ignoring the loitering report, it just wasn't developed yet. It was one line from a passerby.

Interviewer: What made that pattern feel decisive enough to commit resources rather than split them?

Participant: Experience, mostly. I've had cases where the ex is exactly who you think it is, and cases where it's a stranger. At that stage you don't have enough to split evenly, so you go where the strongest documented history points. That felt like the responsible use of limited manpower on day one.

Interviewer: Second decision point — the unit briefing on day two.

Participant: My partner laid out the domestic-call history to the lieutenant and the rest of the group, made the case for the ex pretty strongly. One of the junior guys mentioned the rear-entrance sighting was worth a proper follow-up, but it didn't really get picked up in the room — people nodded and moved on to warrant logistics for the ex. By the end of that briefing the case log had the ex documented as primary suspect, and nobody was formally tasked with running down the loitering lead.

Interviewer: How did you feel about that outcome walking out of the room?

Participant: Comfortable, honestly. Everyone was reading from the same page, which after a chaotic scene day felt like progress. My partner's read matched mine, the lieutenant didn't push back, so we had a direction the whole unit could move on together. I didn't specifically assign someone to chase the rear-entrance thing — it felt like it could wait until we had bandwidth, and right then the room's energy was behind the ex.

Interviewer: Did anyone actually set the rear-entrance lead side by side with the ex-partner theory before the room moved on, or did it just get dropped once things felt settled?

Participant: No, nobody laid them out next to each other. Once my partner and the lieutenant were on the same page, going back to relitigate the junior guy's point felt like it would've slowed us down for no clear reason — like reopening something the room had already moved past. It wasn't that I thought it was wrong, exactly, just that pushing on it right then would've read as second-guessing a direction everybody had already settled into.

Interviewer: Was there a moment where you considered pausing to verify the sighting before locking that direction in?

Participant: Not really, no. It would have meant pulling someone off the warrant work, and with everyone already aligned, it didn't seem like the priority use of the next shift.

Interviewer: Third decision point — day three, the lab result and the alibi correction come back.

Participant: That was a harder morning. DNA didn't match him, and the coworker's second witness basically closed the two-hour gap we'd been counting on. Normally that's the kind of thing that makes you step back. But we'd also just gotten the better description on the rear-entrance guy, and rather than shift the whole frame onto him immediately, I treated the DNA gap as something forensics might still explain — maybe he wore gloves, maybe the negative result reflects a partial or degraded sample rather than absence. I kept him as primary and logged the new description as a secondary, unresolved lead pending more digging.

Interviewer: What was the basis for treating the DNA result as an exception rather than as evidence pointing away from him?

Participant: The domestic-call history and the locked door were still sitting there unexplained if it wasn't him. A negative swab doesn't automatically clear someone — it happens on cases that still hold up later. I didn't want to throw out the whole frame on one lab result without understanding why it came back that way.

Interviewer: Fourth decision point — drafting the referral memo for the DA liaison.

Participant: By day four we had two live threads: the ex, thinner now but with the original history behind him, and the burglary-record guy, whose description was fresh and detailed, still had that first flat line report backing it. When I wrote the summary for the DA liaison, the newest statement — the detailed one — got the most space and came across as the strongest piece in the file, more than the early scene notes or the original canvass statements, which were older and thinner on detail by comparison.

Interviewer: What made the newer statement carry more weight in the writing itself, as opposed to the older material?

Participant: It was just more vivid — clearer physical description, more specific timing. The older notes were accurate but sparse, so when I was putting the narrative together, the recent statement was what stood out and read strongest on the page. Honestly, it was also just the last substantial thing that had come in before I sat down to write, so it was what was fresh in my head — I hadn't gone back and weighed it against the earlier canvass material for corroboration, it just carried into the draft on its own. The DA liaison ended up asking for supplemental work before filing on either of them.

Interviewer: Had you seen a case before where an early theory didn't hold up the way you expected?

Participant: Sure, more than once. It usually teaches you to keep digging on alternatives even when the main line looks solid. I'd say I tried to do that here by keeping the second lead open rather than dropping it outright.

Interviewer: If the rear-entrance sighting had come in fully detailed on day one instead of day three, how do you think the briefing would have gone differently?

Participant: Probably would've split our attention from the start, maybe even changed who got named primary at that meeting. Coming in early and vague versus coming in late and sharp made a real difference in how much room it got.

Interviewer: Looking back, is there a point you'd want to redo?

Participant: Maybe assigning someone concretely to the rear-entrance lead right at the briefing instead of letting it just get mentioned and dropped. That's probably the one moment where a small procedural change could've shifted the whole pace of the case.

Interviewer: Anything else you'd want on the record about how the case moved through those four points?

Participant: Just that none of it felt reckless in the moment. Every step had something behind it. It's only looking at it end to end now that I can see where things could've gone differently.

Interviewer: That's a good place to stop. Thanks for walking through it in this much detail.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Biased_3",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Homicide Detective",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Riverside Apartment Homicide - Third Shift Handoff",
    "scenario_summary_internal": "A homicide detective is interviewed about a case in which a young woman was found dead in her apartment. Early in the investigation the detective and partner formed a working theory pointing to the victim's ex-boyfriend. A team briefing solidified that theory. Midway through, a neighbor's late-arriving statement about a stranger seen near the building complicated the timeline, and the detective had to decide how to weigh it against team consensus and their own prior commitment to the ex-boyfriend theory. The interview traces four decision points from initial scene assessment through case referral to the DA, probing how evidence was gathered, weighted, and reconciled under time pressure and team dynamics.",
    "occupational_realism": {
      "objective": "Identify and build a prosecutable case against the individual responsible for the victim's death within the critical 72-hour investigative window.",
      "setting": "Mid-size city homicide unit; apartment crime scene, precinct briefing room, and follow-up canvass over a 5-day period",
      "constraints": [
        "72-hour window before witness memory degrades and suspect can flee jurisdiction",
        "limited forensic lab turnaround (48-72 hours for DNA/toxicology)",
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
        "probable cause"
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
          "no immediate signs of struggle beyond bedroom"
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
        "intended_action": "Detective designates the ex-boyfriend as the primary working theory and directs the team to focus canvass and warrant efforts around him."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "unit briefing held; lieutenant and three colleagues present",
          "partner detective voices support for the ex-boyfriend theory citing prior domestic call",
          "one junior detective mentions the rear-entrance sighting is worth pursuing but is not pressed further",
          "forensic swabs sent to lab, results pending"
        ],
        "new_information_after_decision": [
          "team consensus recorded in the case log as ex-boyfriend being the primary suspect",
          "the junior detective's rear-entrance lead is deprioritized without a documented follow-up assignment"
        ],
        "alternatives": [
          "assign a team member to independently verify the rear-entrance sighting before finalizing the case direction",
          "adopt the group's converging view and move forward with a warrant request for the ex-boyfriend",
          "table the decision until lab results return"
        ],
        "intended_action": "The detective aligns with the team's converging view, formally adopting the ex-boyfriend theory as the unit's direction without assigning independent verification of the dissenting lead."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "lab results return: no DNA match to ex-boyfriend at the scene",
          "ex-boyfriend's coworker alibi gap now closed by a second witness placing him elsewhere",
          "the rear-entrance witness is finally re-interviewed and gives a more detailed description matching an unrelated individual with a prior burglary record in the area"
        ],
        "new_information_after_decision": [
          "detective requests additional forensic review focused on reconciling the negative DNA result with the existing theory rather than broadening the suspect pool",
          "case referral memo to the DA liaison still lists the ex-boyfriend as primary person of interest, with the new witness description noted as a secondary, unresolved lead"
        ],
        "alternatives": [
          "revise the primary theory to prioritize the burglary-record individual given the fresh, detailed statement",
          "maintain the ex-boyfriend as primary suspect and treat the DNA and alibi gap as explainable exceptions",
          "pause the referral and request a fresh case review from an uninvolved detective"
        ],
        "intended_action": "The detective maintains the ex-boyfriend as the primary theory, characterizing the negative DNA and alibi correction as anomalies rather than as reasons to re-center the investigation, and proceeds toward referral."
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
        "What information came in at each stage, and when?"
      ],
      "decision_point_probes": [
        "What cues led you to focus on the ex-boyfriend early on?",
        "What sources of information did you rely on most at the briefing, and why?",
        "What alternatives did you or the team consider before settling on a direction?",
        "What was the basis for maintaining the theory after the DNA result came back?",
        "Had you seen cases before where an early theory didn't hold up? How did that shape your approach here?",
        "How much time pressure did you feel at each of these points?",
        "How confident were you in the theory at each stage, and what would have changed that confidence?",
        "If the rear-entrance sighting had been detailed from the start, how might your team's direction have changed?"
      ],
      "closing_hypotheticals": [
        "If you were reviewing this case fresh today with all the evidence in front of you at once, would you have weighted anything differently?",
        "What would you tell a junior detective about balancing team consensus against a dissenting lead?",
        "Looking back, was there a moment you'd want to redo?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "decision_point": 3,
        "mechanism": "Detective reinterprets disconfirming evidence (negative DNA match, corrected alibi) as anomalies to preserve consistency with the already-committed ex-boyfriend theory rather than revising the theory",
        "affected_reasoning_operation": "evidence reconciliation and theory revision",
        "evidence_available_at_time": [
          "negative DNA result at scene",
          "alibi gap closed by second witness",
          "newly detailed description of an alternative individual"
        ],
        "required_textual_manifestation": "detective explicitly frames the disconfirming lab and alibi evidence as explainable exceptions while continuing to treat the ex-boyfriend as primary suspect, without engaging substantively with the alternative lead's specifics",
        "plausible_nonbias_interpretation": "detective could argue prior domestic history still gives reasonable cause to keep the ex-boyfriend as a person of interest pending further review",
        "strength": "subtle",
        "do_not_make_explicit": ["cognitive dissonance", "rationalization", "reducing discomfort"]
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "decision_point": 4,
        "mechanism": "The most recently obtained witness statement is given disproportionate weight in the referral summary relative to earlier, comparably or more relevant scene evidence, driven by its recency rather than its evidentiary strength",
        "affected_reasoning_operation": "evidence weighting and summary drafting",
        "evidence_available_at_time": [
          "recent detailed witness description of alternative individual",
          "earlier, thinner canvass statements and initial scene notes",
          "chain-of-custody documentation for all evidence"
        ],
        "required_textual_manifestation": "detective describes drafting the referral summary and explains giving the newest statement prominent placement or emphasis specifically because it was the most recently gathered, with limited justification tied to its actual evidentiary strength",
        "plausible_nonbias_interpretation": "the most recent statement could genuinely be the most detailed and probative evidence, warranting emphasis on its merits alone",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "recency bias", "most recent information"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 2,
        "mechanism": "Detective adopts the converging view expressed at the team briefing and formalizes it as unit direction without independently verifying or assigning follow-up to the dissenting junior detective's alternative lead, prioritizing consensus over critical evaluation",
        "affected_reasoning_operation": "collective decision adoption and dissent evaluation",
        "evidence_available_at_time": [
          "partner detective's vocal support for ex-boyfriend theory",
          "junior detective's brief mention of rear-entrance sighting",
          "lieutenant's presence and implicit expectation of a unified direction"
        ],
        "required_textual_manifestation": "detective recounts the briefing and describes going along with the team's shared view, noting the dissenting lead was mentioned but not assigned for independent follow-up, framed as a natural outcome of the meeting rather than a contested choice",
        "plausible_nonbias_interpretation": "the ex-boyfriend theory may have had the strongest objective support at that time, making team convergence a reasonable reflection of the evidence rather than pressure to conform",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "conformity", "consensus pressure", "dissent suppression"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "not applicable to biased condition"
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "not applicable; condition is biased, not counterfactual",
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 4 decision points appear in the interview",
      "Confirm exactly 1 cognitive dissonance instance embedded only at decision point 3",
      "Confirm exactly 1 recency effects instance embedded only at decision point 4",
      "Confirm exactly 1 groupthink instance embedded only at decision point 2",
      "Confirm no bias labels or psychological terminology appear in the public interview text",
      "Confirm word count falls between 1215 and 1485 words",
      "Confirm each decision point includes at least two plausible alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm consequences described do not mechanically prove bias presence",
      "Confirm decision point 1 contains no intended bias instance and remains a neutral/realistic anchor decision"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Cognitive dissonance",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Recency Effects",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Groupthink",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": ["Cognitive dissonance", "Recency Effects", "Groupthink"],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Cognitive dissonance", "requested_occurrences": 1 },
      { "bias": "Recency Effects", "requested_occurrences": 1 },
      { "bias": "Groupthink", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cd_01", "bias": "Cognitive dissonance" },
      { "instance_id": "re_01", "bias": "Recency Effects" },
      { "instance_id": "gt_01", "bias": "Groupthink" }
    ],
    "intended_decision_points": [
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "decision_point": 3 },
      { "instance_id": "re_01", "bias": "Recency Effects", "decision_point": 4 },
      { "instance_id": "gt_01", "bias": "Groupthink", "decision_point": 2 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "mechanism": "Reinterpreting disconfirming DNA and alibi evidence as anomalies to preserve consistency with the prior committed theory",
        "affected_reasoning_operation": "evidence reconciliation and theory revision",
        "evidence_source": "lab DNA report and corrected alibi statement",
        "distinctiveness_requirement": "must involve active reinterpretation of new disconfirming evidence at decision point 3, distinct from the groupthink adoption at decision point 2 and the weighting behavior at decision point 4"
      },
      {
        "instance_id": "re_01",
        "bias": "Recency Effects",
        "mechanism": "Disproportionate weighting of the most recently obtained witness statement over earlier comparable evidence when drafting the referral summary",
        "affected_reasoning_operation": "evidence weighting and summary drafting",
        "evidence_source": "most recent witness description versus earlier canvass statements and scene notes",
        "distinctiveness_requirement": "must occur during final referral drafting at decision point 4, tied specifically to recency of acquisition rather than theory commitment or group consensus"
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "mechanism": "Adopting team consensus at the briefing and formalizing it without independently verifying or assigning follow-up to a dissenting lead",
        "affected_reasoning_operation": "collective decision adoption and dissent evaluation",
        "evidence_source": "briefing discussion, partner's supportive statement, junior detective's dissenting mention",
        "distinctiveness_requirement": "must occur at the team briefing decision point 2, distinct from the individual reasoning shown in cd_01 and re_01"
      }
    ],
    "intended_strength": [
      { "instance_id": "cd_01", "bias": "Cognitive dissonance", "strength": "subtle" },
      { "instance_id": "re_01", "bias": "Recency Effects", "strength": "subtle" },
      { "instance_id": "gt_01", "bias": "Groupthink", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Biased_3",
    "domain_id": "LE",
    "total_requested_occurrences": 3,
    "total_planned_occurrences": 3,
    "allocation_rule_used": "One occurrence per bias; each assigned to the decision point offering the strongest mechanism fit and narrative realism: groupthink at the team briefing (decision point 2), cognitive dissonance at the disconfirming-evidence juncture (decision point 3), and recency effects at the final referral drafting stage (decision point 4). Decision point 1 held bias-free as a neutral anchor to avoid overloading early narrative and to preserve plausible deniability structure.",
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
          "segment_type": "initial_scene_inference",
          "raw_interview_anchor": "No forced entry ... that's where my head went first.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive initial suspect inference, but decision point 1 is a neutral anchor in the hidden manifest."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "objective_and_time_pressure",
          "raw_interview_anchor": "Build a working theory fast enough ... but not so fast we lock ourselves in.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Explicit objective and constraint balancing without a hidden bias instance."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "day_one_theory_selection",
          "raw_interview_anchor": "We could've held off naming anybody ... I chose to name him primary and put resources there.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive alternative comparison and resource choice at the neutral first decision point."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "day_two_team_briefing",
          "raw_interview_anchor": "Once my partner and the lieutenant were on the same page ... second-guessing a direction everybody had already settled into.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "gt_01"
          ],
          "ground_truth_rationale": "The briefing adopts the converging view, leaves dissent unassigned, and treats reopening it as second-guessing consensus."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "day_three_disconfirming_evidence_reconciliation",
          "raw_interview_anchor": "I treated the DNA gap as something forensics might still explain ... I kept him as primary.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "cd_01"
          ],
          "ground_truth_rationale": "Negative DNA, corrected alibi, and a stronger alternative are reframed as explainable exceptions while the prior theory remains primary."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "day_four_referral_drafting",
          "raw_interview_anchor": "The newest statement ... got the most space ... it was what was fresh in my head.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "re_01"
          ],
          "ground_truth_rationale": "The newest statement gets disproportionate narrative prominence partly because it is fresh and vivid, without corroboration-based comparison."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "prior_case_learning",
          "raw_interview_anchor": "It usually teaches you to keep digging on alternatives even when the main line looks solid.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive reflection on prior cases and an adopted investigative lesson, without a hidden bias instance."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "counterfactual_team_direction",
          "raw_interview_anchor": "Probably would've split our attention from the start ... Coming in early and vague versus coming in late and sharp made a real difference.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Participant gives a substantive counterfactual prediction about information timing; no hidden bias is assigned."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "procedural_redo",
          "raw_interview_anchor": "Maybe assigning someone concretely to the rear-entrance lead right at the briefing ...",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Participant identifies a concrete process change in hindsight; no hidden bias is manifested in the proposed redo."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "retrospective_process_assessment",
          "raw_interview_anchor": "None of it felt reckless in the moment ... looking at it end to end now that I can see where things could've gone differently.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Substantive retrospective assessment and proposed procedural change, but no hidden bias is manifested."
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
    "analysis_scope_note": "No scientific-paper corpus passages were provided for retrieval. Bias labels and mechanisms are drawn from general cognitive-science knowledge and the interview text."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Groupthink",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Recency bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Groupthink",
      "alternative_labels": ["Common knowledge effect", "Shared information bias", "Conformity bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A pattern of group decision-making in which the desire for consensus or cohesion suppresses the expression and evaluation of dissenting or alternative information, leading to an illusion of unanimity and incomplete appraisal of alternatives.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-2 unit briefing prioritization of the ex-partner theory",
      "decision_point_description": "Deciding whether to formally assign follow-up to the rear-entrance sighting after a junior officer raised it during the briefing.",
      "affected_reasoning_operation": "Group decision-making and allocation of investigative follow-up",
      "bias_specific_mechanism": "Consensus-seeking and perceived unanimity suppressed the unique rear-entrance lead: the participant interpreted the room's alignment as progress, avoided reopening the issue, and did not assign follow-up because dissent would have felt like second-guessing.",
      "manifestation_in_interview": "The participant reports that the junior officer's rear-entrance point did not get picked up in the room; he felt comfortable because everyone was on the same page; and he did not assign the follow-up because going back would have felt like reopening a settled direction.",
      "effect_on_reasoning_or_decision": "The rear-entrance sighting remained unassigned after the briefing, while the ex-partner continued to be documented as primary suspect, reducing early scrutiny of an alternative lead.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "One of the junior guys mentioned the rear-entrance sighting was worth a proper follow-up, but it didn't really get picked up in the room — people nodded and moved on to warrant logistics for the ex.",
          "evidence_explanation": "Shows that an alternative lead was raised but not integrated into the group's decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Comfortable, honestly. Everyone was reading from the same page, which after a chaotic scene day felt like progress. My partner's read matched mine, the lieutenant didn't push back, so we had a direction the whole unit could move on together.",
          "evidence_explanation": "Perceived consensus produced positive affect and reduced deliberation about the alternative lead."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No, nobody laid them out next to each other. Once my partner and the lieutenant were on the same page, going back to relitigate the junior guy's point felt like it would've slowed us down for no clear reason — like reopening something the room had already moved past. It wasn't that I thought it was wrong, exactly, just that pushing on it right then would've read as second-guessing a direction everybody had already settled into.",
          "evidence_explanation": "Directly demonstrates suppression of a dissenting point because of perceived group agreement, a key groupthink mechanism."
        }
      ],
      "correction_or_counterevidence": "The junior officer did voice the rear-entrance lead, so the group was not unanimously ignoring it; the participant later identifies assigning that lead as the procedural change he would make.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available; the label and mechanism are from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Belief perseverance", "Biased assimilation", "Motivated reasoning"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to evaluate new evidence in a way that protects an existing hypothesis or belief, overweighting confirming information and discounting or explaining away disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-3 response to DNA non-match and alibi correction",
      "decision_point_description": "Whether to demote the ex-partner as primary suspect after the lab returned no DNA match and a witness closed the alibi gap.",
      "affected_reasoning_operation": "Evidence evaluation and suspect prioritization",
      "bias_specific_mechanism": "Rather than treating the exculpatory DNA and alibi evidence as reasons to shift focus, the participant generated protective explanations such as gloves or a degraded sample and retained the ex as primary because the original circumstantial pattern remained unexplained without him.",
      "manifestation_in_interview": "The participant describes treating the DNA gap as something forensics might still explain and keeping the ex as primary; he later justifies this on the grounds that the domestic history and locked door would remain unexplained if the ex were not the suspect.",
      "effect_on_reasoning_or_decision": "The ex-partner remained the primary suspect and the detailed rear-entrance lead remained secondary, directing investigative resources and the eventual DA referral emphasis away from the newer suspect.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "DNA didn't match him, and the coworker's second witness basically closed the two-hour gap we'd been counting on. Normally that's the kind of thing that makes you step back. But we'd also just gotten the better description on the rear-entrance guy, and rather than shift the whole frame onto him immediately, I treated the DNA gap as something forensics might still explain — maybe he wore gloves, maybe the negative result reflects a partial or degraded sample rather than absence.",
          "evidence_explanation": "Shows recognition of disconfirming evidence followed by generating ad hoc explanations to preserve the existing primary theory."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The domestic-call history and the locked door were still sitting there unexplained if it wasn't him. A negative swab doesn't automatically clear someone — it happens on cases that still hold up later. I didn't want to throw out the whole frame on one lab result without understanding why it came back that way.",
          "evidence_explanation": "Demonstrates asymmetric treatment: old inculpatory evidence is treated as robust while new exculpatory evidence is discounted rather than integrated as a reason to reduce confidence in the ex-partner theory."
        }
      ],
      "correction_or_counterevidence": "A negative swab does not automatically clear a suspect, and retaining a hypothesis pending forensic explanation is not inherently unreasonable; the participant also kept the rear-entrance lead open rather than dropping it entirely.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available; the label and mechanism are from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Recency bias",
      "alternative_labels": ["Availability heuristic", "Recency effect", "Serial position effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which more recent or more vividly recalled information is given greater weight in judgment or communication than older or less salient information, independent of its actual probative value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Day-4 drafting of the DA liaison referral memo",
      "decision_point_description": "Deciding how much weight to give the recent detailed rear-entrance statement relative to older canvass and scene notes in the memo summary.",
      "affected_reasoning_operation": "Evidence weighting and narrative summarization",
      "bias_specific_mechanism": "The participant weighted the newest, more vivid statement more heavily because of its salience and temporal recency; he explicitly says he did not go back and weigh it against the earlier material for corroboration.",
      "manifestation_in_interview": "The participant reports that the recent statement got the most space and read as the strongest piece in the file, explaining that it was more vivid, fresh in his head, and had not been reweighed against earlier canvass material.",
      "effect_on_reasoning_or_decision": "The referral memo gave disproportionate prominence to the recent detailed statement, shaping the DA liaison's initial view and leading to a request for supplemental work before filing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "By day four we had two live threads: the ex, thinner now but with the original history behind him, and the burglary-record guy, whose description was fresh and detailed, still had that first flat line report backing it. When I wrote the summary for the DA liaison, the newest statement — the detailed one — got the most space and came across as the strongest piece in the file, more than the early scene notes or the original canvass statements, which were older and thinner on detail by comparison.",
          "evidence_explanation": "Shows explicit differential weighting based on recency and detail rather than corroborated validity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was just more vivid — clearer physical description, more specific timing. The older notes were accurate but sparse, so when I was putting the narrative together, the recent statement was what stood out and read strongest on the page. Honestly, it was also just the last substantial thing that had come in before I sat down to write, so it was what was fresh in my head — I hadn't gone back and weighed it against the earlier canvass material for corroboration, it just carried into the draft on its own.",
          "evidence_explanation": "Direct admission that temporal recency and vividness, not a comparative probative assessment, drove the emphasis in the memo."
        }
      ],
      "correction_or_counterevidence": "The DA liaison did ask for supplemental work, so the memo's emphasis did not necessarily produce a final filing decision; the participant also acknowledges he had not reweighed the material against earlier corroboration.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus support was available; the label and mechanism are from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific corpus was available; all bias labels derive from general cognitive-science knowledge.",
    "The analysis is based on a retrospective self-report, so it cannot establish whether these biases operated during the original decisions or only in the retelling.",
    "Occurrence boundaries are constrained to the narrative decision points described by the participant."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Biased_3_Sonar_off",
  "interview_id": "LE_Biased_3",
  "system_prompt_id": "Sonar",
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
