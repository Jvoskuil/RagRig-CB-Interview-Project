You are a controlled CTA interview editor. Revise the interview only where explicitly instructed by the validation report.

Inputs:
- Original interview: {{Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the border-sector traffic assessment from last month, purely for how you approached the analysis. Nothing here goes in your file.

Participant: Sure, no problem. That one's still fresh anyway.

Interviewer: Good. Can you give me your role in the fusion cell and what your objective was that day?

Participant: I'm the SIGINT desk analyst for that regional cell. My job that day was to turn a raw traffic spike into a confidence-graded assessment for the fusion cell lead—basically, tell him whether what we were seeing near the Sector 7 logistics hub was something operational or just noise.

Interviewer: Take me through the incident from the top.

Participant: Around 0700 the automated system flagged a jump in encrypted burst traffic near the Sector 7 hub—well above baseline, and Sector 7 is normally quiet outside scheduled rotations. About the same time, Sector 4 showed a smaller bump too, but that's a different area entirely, no obvious connection. I had a hard deadline: the lead wanted a briefing in six hours. My linguists were already sitting on an eight-hour backlog from other tasking, so I knew from the jump I wasn't going to get everything translated.

Interviewer: What did you know before you made any calls?

Participant: Just the signal signature data—volume, timing, burst patterns—and the historical baseline for both sectors. No content yet. Sector 7's hub has strategic weight, it's tied to a known logistics node in the order of battle, so a spike there gets attention regardless. Sector 4's pattern was actually less typical, statistically, but there was no obvious link to anything sensitive.

Interviewer: So what did you do with your linguist hours?

Participant: I pushed almost all three available hours to Sector 7 and queued Sector 4 for later. The alternative was splitting time evenly, or even flipping it and doing Sector 4 first because its pattern was more unusual. But given the deadline, I couldn't do both properly, and Sector 7's hub mattered more if something real was happening there.

Interviewer: What came back from that first batch of translation?

Participant: A mix. Some convoy-movement language, some resupply terms, and two coded phrases that weren't in our standard glossary. Also some fairly mundane rotation talk. It wasn't clean either way.

Interviewer: How did you interpret that mix?

Participant: I started drafting a working note. My instinct was that convoy references plus burst traffic plus unexplained code phrases fit a pattern I'd want to flag—an emerging logistics buildup ahead of some posture change. I laid it out step by step: the signal surge, then the convoy chatter, then the coded terms as probable concealment for something they didn't want plain-language. Writing it out that way, it held together. It read like a coherent sequence, and honestly, once I had it typed up in that form, I felt more confident it was the right read than when I'd started.

Interviewer: Was there anything at that point that argued the other way?

Participant: The exercise calendar showed a rotation window that plausibly overlapped, and no imagery corroboration had come in yet. I noted the rotation possibility in the draft, but I led with the buildup framing because it explained more of the pieces at once—the convoy talk, the burst pattern, and the coded phrases all fit under one story, whereas the rotation explanation left the coded phrases dangling.

Interviewer: Did anything come in afterward that touched that account?

Participant: Yes—a later intercept had maintenance-cycle terminology in it, which cuts somewhat against the buildup idea. And one of those two coded phrases turned out to be in a maintenance-schedule glossary, not anything to do with offensive posture. That came in after I'd already built the note around the buildup framing.

Interviewer: Let's move to sourcing. You had two corroborating options—walk me through that.

Participant: Right, I had an open-source digest, well-written, clearly formatted, forecasting regional tension in a way that lined up with what I already had drafted. And I had an IMINT report on vehicle dispersal at the hub—more directly relevant to the actual location, but dense, heavy on sensor jargon, and I only had time to fully absorb one of them before the deadline. The IMINT analyst wasn't reachable for a quick walk-through either.

Interviewer: What tipped it toward the digest?

Participant: Time, mostly. The digest was quick to read and slotted right into the write-up I already had going—it reinforced the framing without extra work parsing sensor terminology I'd have needed help interpreting anyway. The IMINT report would've taken longer to properly digest and I wasn't fully confident I was reading the dispersal imagery correctly on my own.

Interviewer: Did you consider weighting them evenly, or leaning on IMINT instead?

Participant: I considered it. IMINT is sensor-based and specific to that hub, so on paper it's the stronger source. But given the time I had, citing the source I could actually process well and confidently seemed like the more responsible choice than citing something I might misread under pressure.

Interviewer: What did you learn about those sources afterward?

Participant: After the briefing, going back through the IMINT report more carefully, the dispersal pattern was actually just as consistent with a maintenance stand-down as with a buildup. And the digest, it turned out, was drawing on general regional reporting that didn't specifically tie back to Sector 7 at all.

Interviewer: Now the final call—how did you land on your confidence level for the briefing?

Participant: I had twenty minutes before I had to walk in. I had a buildup narrative, partial open-source support, and this unresolved contradiction with the maintenance terminology. I considered going high confidence, but the contradiction made that feel wrong. Low confidence felt like it undersold the pattern I was seeing. So I went moderate—buildup assessment, explicitly flagged the maintenance-terminology contradiction, and recommended a follow-up collection tasking to resolve it.

Interviewer: How did the lead respond?

Participant: He took the moderate framing at face value and tasked the follow-up collection, which was really the right outcome regardless of which way the underlying truth eventually goes.

Interviewer: And has that follow-up traffic settled it either way?

Participant: Not really. Two days on, the new traffic is still genuinely mixed. It hasn't confirmed the buildup and it hasn't ruled it out either.

Interviewer: If you'd had one more linguist-hour before the briefing, what would you have done differently?

Participant: Probably gone back to that second coded phrase earlier rather than letting it sit unresolved in the draft. It might have surfaced the maintenance angle sooner.

Interviewer: If the IMINT report had been your only corroborating option, how do you think your assessment would have looked?

Participant: Honestly, I think I'd have spent more time forcing myself through the sensor detail, and the ambiguity in the dispersal pattern might have shown up in my write-up earlier instead of after the fact. I might have hedged more going into the briefing.

Interviewer: Looking back, is there a point in this you'd want to revisit?

Participant: Probably the moment I locked in the buildup framing in the working note. It wasn't wrong to consider it, but I built it out pretty fully before I'd seen the maintenance-terminology intercept, and once it was written that clearly, it was hard to hold as loosely as I probably should have.

Interviewer: That's helpful. I think that covers everything I need.

Participant: Glad to walk through it.
}}
- Hidden generation specification: {{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Explanation bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as confidence increase from narrative construction itself, not from new evidence"
      },
      {
        "bias": "Fluency effects",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as source preference driven by ease of reading/processing rather than sourcing strength or relevance"
      }
    ],
    "target_bias_names": [
      "Explanation bias",
      "Fluency effects"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Explanation bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Fluency effects",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias"
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias",
        "decision_point": 2
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects",
        "decision_point": 3
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias",
        "mechanism": "Constructing a coherent, detailed causal narrative from partial intercepts increases the analyst's confidence in that narrative, independent of new supporting evidence",
        "affected_reasoning_operation": "Hypothesis generation and confidence calibration",
        "evidence_source": "Partial translated intercepts (rotation terminology plus two unclear coded phrases) and overlapping exercise calendar",
        "distinctiveness_requirement": "Distinct from fe_01 in decision point, evidence type (intercept translation vs. open-source/IMINT corroboration), and reasoning operation (narrative construction vs. source selection)"
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects",
        "mechanism": "Ease of reading the open-source digest is mistaken for a proxy of its reliability or relevance relative to the denser IMINT report",
        "affected_reasoning_operation": "Source selection and evidentiary weighting for corroboration",
        "evidence_source": "Open-source news digest versus dense IMINT vehicle-dispersal report",
        "distinctiveness_requirement": "Distinct from eb_01 in decision point, evidence type, and reasoning operation (source weighting vs. narrative generation)"
      }
    ],
    "intended_strength": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias",
        "strength": "subtle"
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_2",
    "domain_id": "IA",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias assigned to a distinct decision point (explanation bias at decision point 2, fluency effects at decision point 3) selected for mechanism fit: explanation bias fits the narrative-construction moment after partial translation, fluency effects fits the corroborating-source selection moment; decision points 1 and 4 were kept free of intended bias instances to preserve narrative realism and avoid over-concentration.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }}}
- Validation report: {{{
  "validator_version": "2.0",
  "interview_id": "IA_Biased_2",
  "condition": "biased",
  "domain_assessment": {
    "domain": "Intelligence analysis / SIGINT-supported fusion-cell assessment",
    "role": "SIGINT desk analyst in a regional fusion cell",
    "objective": "Produce a confidence-graded assessment of whether an encrypted-traffic spike near the Sector 7 logistics hub represented an operational logistics buildup or routine/non-operational activity.",
    "incident_type": "Time-constrained assessment of anomalous encrypted communications with incomplete translation and competing corroborating sources.",
    "confidence": 0.99
  },
  "structure_audit": {
    "estimated_word_count": 1395,
    "within_target_range": true,
    "decision_point_count": 4,
    "decision_points": [
      {
        "id": 1,
        "summary": "Allocate limited linguist time between the strategically important Sector 7 traffic spike and the statistically less typical Sector 4 anomaly.",
        "evidence_before": [
          "Sector 7 showed encrypted burst traffic well above baseline near a known logistics node.",
          "Sector 4 showed a smaller but statistically less typical pattern.",
          "No content was available initially.",
          "The analyst had three linguist-hours, an eight-hour backlog, and a six-hour briefing deadline."
        ],
        "evidence_after": [
          "Partial Sector 7 translation returned convoy-movement language, resupply terms, two unexplained coded phrases, and routine rotation talk."
        ],
        "goals_constraints": [
          "Identify operationally meaningful activity.",
          "Provide a briefing within six hours.",
          "Allocate only three available linguist-hours.",
          "Avoid spreading scarce translation capacity too thinly."
        ],
        "alternatives": [
          "Split linguist time evenly between Sector 7 and Sector 4.",
          "Prioritize Sector 4 because its pattern was more statistically unusual.",
          "Prioritize Sector 7 because of its strategic importance."
        ],
        "decision_basis": "The analyst prioritized Sector 7 because a possible development at a known logistics hub carried greater operational consequence under the deadline.",
        "time_pressure": "High: six-hour briefing deadline and only three available linguist-hours.",
        "uncertainty": "High: no message content initially and no established connection between the sectors."
      },
      {
        "id": 2,
        "summary": "Construct and provisionally privilege a logistics-buildup explanation from partial Sector 7 translations and signal-pattern evidence.",
        "evidence_before": [
          "Burst-traffic surge near Sector 7.",
          "Partial translations included convoy and resupply language.",
          "Two coded phrases were unresolved.",
          "Some traffic concerned ordinary rotations.",
          "The exercise calendar plausibly overlapped a rotation window.",
          "No imagery corroboration was yet available."
        ],
        "evidence_after": [
          "A later intercept contained maintenance-cycle terminology.",
          "One previously unexplained coded phrase was identified in a maintenance-schedule glossary."
        ],
        "goals_constraints": [
          "Produce an intelligible working assessment from mixed and incomplete evidence.",
          "Maintain a usable draft under time pressure.",
          "Distinguish potential buildup from routine rotation or maintenance activity."
        ],
        "alternatives": [
          "Frame the evidence primarily as an emerging logistics buildup.",
          "Frame it primarily as a scheduled rotation or maintenance-related activity.",
          "Maintain competing explanations without giving either a leading narrative."
        ],
        "decision_basis": "The analyst judged the buildup account to explain more observed elements and then became more confident after arranging those elements into a coherent written sequence.",
        "time_pressure": "Moderate to high: the analyst was drafting toward the same six-hour briefing deadline.",
        "uncertainty": "High: translations were partial, coded language was unresolved, and contradictory routine explanations remained plausible."
      },
      {
        "id": 3,
        "summary": "Select and weight an easily processed open-source digest rather than a denser, more location-specific IMINT report for corroboration.",
        "evidence_before": [
          "The open-source digest was well-written, clearly formatted, and forecast regional tension consistent with the existing draft.",
          "The IMINT report concerned vehicle dispersal at the actual hub and was more directly relevant.",
          "The IMINT report was dense, jargon-heavy, and its analyst was unavailable.",
          "The analyst believed there was time to fully absorb only one source."
        ],
        "evidence_after": [
          "The IMINT dispersal pattern was later assessed as consistent with both maintenance stand-down and buildup.",
          "The digest was based on general regional reporting and did not specifically tie to Sector 7."
        ],
        "goals_constraints": [
          "Obtain usable corroboration before the briefing.",
          "Avoid misreading sensor terminology without analyst support.",
          "Use the limited remaining time responsibly."
        ],
        "alternatives": [
          "Use the open-source digest as the principal corroborating source.",
          "Prioritize the more relevant IMINT report.",
          "Weight both sources cautiously while explicitly limiting claims.",
          "Avoid treating either source as meaningful corroboration until assessed."
        ],
        "decision_basis": "The analyst chose the digest because it was quicker to process, fit the developing write-up, and felt less likely to be misunderstood than the dense IMINT product.",
        "time_pressure": "High: only enough time to fully absorb one source before the deadline.",
        "uncertainty": "Moderate to high: the analyst lacked IMINT-domain support and did not know the digest's Sector 7 specificity at the time."
      },
      {
        "id": 4,
        "summary": "Set the final briefing confidence at moderate, present buildup as the assessment, flag the maintenance contradiction, and request follow-up collection.",
        "evidence_before": [
          "A drafted buildup narrative.",
          "Partial open-source support.",
          "An unresolved maintenance-terminology contradiction.",
          "No definitive imagery interpretation.",
          "Twenty minutes remained before the briefing."
        ],
        "evidence_after": [
          "The lead accepted the moderate framing and tasked follow-up collection.",
          "Two days of follow-up traffic remained mixed and did not resolve the hypothesis."
        ],
        "goals_constraints": [
          "Communicate an actionable assessment without overstating confidence.",
          "Surface material contradictory evidence.",
          "Recommend collection that could resolve the uncertainty."
        ],
        "alternatives": [
          "High-confidence buildup assessment.",
          "Low-confidence assessment.",
          "Moderate-confidence buildup assessment with an explicit contradiction and follow-up tasking."
        ],
        "decision_basis": "The analyst selected moderate confidence because the pattern appeared meaningful but the maintenance evidence precluded a high-confidence conclusion.",
        "time_pressure": "Very high: twenty minutes before the briefing.",
        "uncertainty": "High: available evidence remained genuinely mixed."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "eb_01",
      "bias": "Explanation bias",
      "requested_occurrences_for_bias": 1,
      "status": "supported",
      "decision_point": 2,
      "supporting_quote": "“Writing it out that way, it held together. It read like a coherent sequence, and honestly, once I had it typed up in that form, I felt more confident it was the right read than when I'd started.”",
      "evidence_location": "Decision point 2; participant response immediately after describing the first partial translation batch.",
      "mechanism": "The analyst reports an increase in confidence caused by constructing and writing a coherent causal sequence from already available, partial evidence. No new supporting evidence is identified as causing the increase. This directly supports explanation bias affecting both hypothesis generation and confidence calibration.",
      "strength": "moderate",
      "confidence": 0.97,
      "plausible_nonbias_explanation": "The narrative may have legitimately made the evidentiary structure easier to inspect. However, the participant explicitly attributes greater confidence to the account's coherence after it was written, despite unresolved rotation evidence and coded terms whose meanings were not yet known.",
      "additional_evidence_needed": "None for occurrence validation. The existing self-report identifies the confidence change, the triggering cognitive operation, and the unchanged evidence base.",
      "revision_needed": false,
      "revision": {
        "revision_type": "none",
        "location": "Decision point 2, working-note construction response.",
        "current_defect": "None material. The episode is independently identifiable and textually tied to confidence increasing through explanatory construction rather than new evidence.",
        "minimal_change_instruction": "Retain the current wording. If edited for style, preserve the explicit temporal relation: evidence was unchanged, the account was written into a coherent sequence, and confidence increased afterward.",
        "preserve": [
          "Partial and mixed nature of the translated intercepts",
          "Rotation and maintenance alternatives",
          "Absence of new supporting evidence at the moment confidence rises",
          "Decision-point separation from corroborating-source selection"
        ],
        "avoid_creating": [
          "A second explanation-bias episode at final confidence calibration",
          "An explicit textbook bias label",
          "Language implying that the narrative itself proves the buildup hypothesis"
        ],
        "expected_post_revision_status": "supported"
      }
    },
    {
      "instance_id": "fe_01",
      "bias": "Fluency effects",
      "requested_occurrences_for_bias": 1,
      "status": "weak",
      "decision_point": 3,
      "supporting_quote": "“The digest was quick to read and slotted right into the write-up I already had going—it reinforced the framing without extra work parsing sensor terminology.”",
      "evidence_location": "Decision point 3; participant explanation of selecting the open-source digest over the IMINT report.",
      "mechanism": "The participant selected the more fluent source in part because it was easy to read and integrate. However, the text does not adequately establish that ease was mistaken for reliability, relevance, or evidentiary strength. The participant explicitly recognizes that IMINT is more specific and stronger “on paper,” and gives a credible non-bias reason: avoiding a potentially erroneous interpretation of unfamiliar sensor detail without specialist support.",
      "strength": "weak",
      "confidence": 0.76,
      "plausible_nonbias_explanation": "This can be justified bounded rationality and risk management under a real deadline: the analyst had time to understand only one source, lacked confidence interpreting IMINT, and could not consult the IMINT analyst. The later finding that IMINT was itself ambiguous further weakens an inference that the choice was simply a fluency-driven evidentiary error.",
      "additional_evidence_needed": "A subtle indication that the digest's clarity or ease of processing increased its perceived trustworthiness, relevance, or corroborative weight beyond what its underlying sourcing warranted, while the analyst knew the IMINT report was more directly tied to Sector 7.",
      "revision_needed": true,
      "revision": {
        "revision_type": "local_evidence_addition",
        "location": "Decision point 3, immediately after the participant says that the digest was quick to read and easy to slot into the draft.",
        "current_defect": "The current account establishes ease-of-processing and selection under time pressure, but it also provides a strong legitimate explanation for selecting the digest. It does not clearly show fluency being used as a proxy for source quality or relevance.",
        "minimal_change_instruction": "Add one restrained participant sentence indicating that the digest's polished, easy-to-follow presentation made its regional claims feel more dependable or more applicable to Sector 7 than the analyst could actually establish from its sourcing. Preserve the participant's awareness that IMINT was more location-specific. Do not state or name “fluency bias.”",
        "preserve": [
          "The six-hour deadline and limited time to fully assess one source",
          "The analyst's inability to obtain a quick IMINT walk-through",
          "The digest's general regional rather than Sector 7-specific basis",
          "The IMINT report's actual ambiguity",
          "The existing explanation-bias episode at decision point 2",
          "The final moderate-confidence decision and collection recommendation"
        ],
        "avoid_creating": [
          "A second target occurrence at decision point 3",
          "An overt claim that readability objectively establishes credibility",
          "A stronger confirmation-bias episode based solely on choosing a source that agrees with the buildup draft",
          "A change that makes the IMINT report definitively exculpatory or definitively confirmatory"
        ],
        "expected_post_revision_status": "supported"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "Explanation bias",
      "requested_count": 1,
      "supported_count": 1,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    },
    {
      "bias": "Fluency effects",
      "requested_count": 1,
      "supported_count": 0,
      "weak_count": 1,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": false
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "Confirmation bias",
      "decision_point": 3,
      "supporting_quote": "“The digest was quick to read and slotted right into the write-up I already had going—it reinforced the framing.”",
      "mechanism": "The analyst preferentially selected a source whose forecast aligned with an already drafted buildup account, rather than first resolving the more directly relevant but difficult IMINT evidence.",
      "confidence": 0.58,
      "status": "weak",
      "plausible_nonbias_explanation": "The digest was also selected because it could be processed quickly and the analyst reasonably feared misreading the IMINT product without technical support. The text does not establish that agreement with the buildup narrative, rather than operational usability, was decisive.",
      "revision_recommendation": "remove_or_neutralize"
    },
    {
      "bias": "Anchoring / premature commitment",
      "decision_point": 2,
      "supporting_quote": "“Once it was written that clearly, it was hard to hold as loosely as I probably should have.”",
      "mechanism": "Early commitment to the buildup framing may have made later contradictory maintenance information harder to integrate neutrally.",
      "confidence": 0.47,
      "status": "weak",
      "plausible_nonbias_explanation": "This is largely a retrospective restatement of the supported explanation-bias episode, not a distinct later failure to update. The analyst did acknowledge the contradiction and downgraded the final judgment to moderate confidence.",
      "revision_recommendation": "none"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "Prioritizing Sector 7 over the statistically more unusual Sector 4 pattern.",
      "location": "Decision point 1; linguist-hour allocation.",
      "why_not_bias": "The choice rests on stated strategic consequence, known order-of-battle relevance, finite translation capacity, and a deadline. Statistical unusualness alone does not compel priority when operational significance differs."
    },
    {
      "cue": "Treating convoy movement, resupply terms, and burst traffic as potentially compatible with a logistics buildup.",
      "location": "Decision point 2; interpretation of partial translations.",
      "why_not_bias": "This is a plausible hypothesis-generation step. It becomes bias-relevant only because the participant reports that narrative construction itself increased confidence without new evidence."
    },
    {
      "cue": "Avoiding reliance on a technical IMINT report the analyst may misread.",
      "location": "Decision point 3; source selection.",
      "why_not_bias": "A concern about one's competence to interpret unfamiliar sensor terminology, especially without access to the reporting analyst, can be appropriate epistemic caution rather than a cognitive bias."
    },
    {
      "cue": "Selecting moderate rather than high confidence and explicitly flagging contradictory maintenance terminology.",
      "location": "Decision point 4; final briefing confidence.",
      "why_not_bias": "The analyst incorporates disconfirming evidence, avoids overconfidence, and recommends discriminating follow-up collection. The later mixed traffic does not retroactively make the original decision biased."
    },
    {
      "cue": "The lead's acceptance of the moderate assessment and the eventual tasking decision.",
      "location": "Post-briefing outcome.",
      "why_not_bias": "A supervisor's response and a procedurally useful collection task do not validate or invalidate the analyst's cognitive process."
    }
  ],
  "causal_audit": {
    "causal_claims": [
      {
        "claim": "Convoy references, burst traffic, and coded phrases jointly indicate an emerging logistics buildup.",
        "assessment": "Plausible inferential hypothesis but not established causal proof. The participant appropriately later acknowledges rotation and maintenance alternatives."
      },
      {
        "claim": "The coded phrases were probably concealment for activity not intended to be in plain language.",
        "assessment": "Weakly supported at the time stated. The later glossary identification of one phrase as maintenance-related demonstrates that coded or unexplained terminology should not itself be treated as evidence of concealment."
      },
      {
        "claim": "Writing the causal narrative increased confidence in the buildup interpretation.",
        "assessment": "Strongly supported as a self-reported cognitive-process claim and is the key evidence for explanation bias."
      }
    ],
    "correlation_causation_risks": [
      {
        "risk": "The buildup narrative groups co-occurring signal volume, convoy language, resupply terms, and coded phrases into one causal story without independently demonstrating that they arose from the same operation.",
        "mitigation_present": "The analyst notes an overlapping rotation window, maintenance terminology, lack of imagery corroboration, and ultimately uses moderate confidence."
      },
      {
        "risk": "General regional-tension reporting is treated as partial corroboration of a Sector 7-specific assessment.",
        "mitigation_present": "The later source review establishes that the digest did not specifically tie to Sector 7."
      }
    ],
    "counterfactual_present": true,
    "changed_variable": "Availability of corroborating sources: the interviewer asks how the assessment would have differed if the IMINT report had been the only corroborating option.",
    "held_constant": [
      "The underlying Sector 7 traffic and translation evidence",
      "The analyst's role",
      "The briefing deadline",
      "The IMINT report's ambiguity",
      "The lack of an IMINT analyst walk-through"
    ],
    "causal_coherence": "moderate",
    "explanation": "The counterfactual changes one identifiable variable—availability of the easy open-source alternative—and produces a coherent predicted pathway: more effort on IMINT detail, earlier recognition of ambiguity, and greater hedging. It remains self-reported and hypothetical, so it cannot independently prove that source fluency caused the original weighting decision. It also supports the need to distinguish a fluency mechanism from rational competence management."
  },
  "quality_scores": {
    "occupational_realism": 9,
    "cta_fidelity": 9,
    "bias_separability": 7,
    "bias_subtlety": 8,
    "control_fidelity": 10,
    "counterfactual_fidelity": 8,
    "narrative_coherence": 9,
    "naturalness": 9,
    "hidden_label_integrity": 9,
    "overall_quality": 8
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 1,
    "requested_occurrence_total": 2,
    "missing_occurrence_total": 1,
    "accidental_occurrence_total": 0,
    "priority": "medium",
    "recommended_action": "revise",
    "global_revision_constraints": [
      "Retain exactly four decision points.",
      "Keep explanation bias confined to the working-note construction episode at decision point 2.",
      "Repair only the evidentiary mechanism for fluency effects at decision point 3.",
      "Do not treat the eventual mixed follow-up outcome as evidence of bias.",
      "Preserve the analyst's appropriate final acknowledgment of uncertainty and recommendation for follow-up collection.",
      "Do not convert the interview into an overt bias-recognition exercise or introduce diagnostic bias labels."
    ],
    "revision_order": [
      "Revise fe_01 locally at decision point 3 to show that presentation fluency inflated perceived evidentiary value, not merely that the digest was quicker and safer to process.",
      "Review the revised wording to ensure that agreement with the existing buildup draft remains secondary and does not create a separate supported confirmation-bias occurrence.",
      "Verify that the decision point 4 moderate-confidence calibration remains an appropriate response to conflicting evidence rather than a second explanation-bias episode."
    ]
  },
  "failure_flags": [
    {
      "flag": "FLUENCY_MECHANISM_UNDERDETERMINED",
      "severity": "medium",
      "detail": "The planned fluency-effects occurrence is plausible but not fully defensible because the participant explicitly recognizes the IMINT report as more relevant and offers a credible competence-and-time-based reason for not relying on it."
    },
    {
      "flag": "POTENTIAL_CONFIRMATION_CUE",
      "severity": "low",
      "detail": "The selected digest both aligns with and is easy to insert into the pre-existing buildup write-up. Current evidence is insufficient to count confirmation bias, but revisions to fe_01 should avoid making alignment with the preferred conclusion the decisive reason for source selection."
    }
  ]
}}}

Rules:
1. Apply only revisions with revision_needed = true.
2. Preserve all supported occurrences exactly in mechanism and approximate location.
3. Repair every requested occurrence marked weak, absent, merged, or misclassified according to its minimal_change_instruction.
4. Remove or neutralize accidental occurrences when instructed.
5. Do not add any occurrence not requested in the hidden specification.
6. Do not name or define cognitive biases.
7. Preserve the occupational setting, participant role, four-decision-point structure, dialogue format, approximate length, vocabulary level, causal variable, and counterfactual conditions.
8. Do not make the target bias obvious through exaggerated or textbook-like language.
9. If a requested occurrence is not plausible under the scenario, do not force it; return REVISION_BLOCKED with a concise explanation rather than fabricating behavior.
10. Return only the revised interview text, unless revision is blocked.

Before outputting, silently check the requested occurrence count, accidental occurrence risk, word count, and preservation constraints.
