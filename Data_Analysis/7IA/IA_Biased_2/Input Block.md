<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm you're comfortable walking through the border-sector traffic assessment from last month, purely for how you approached the analysis. Nothing here goes in your file.

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

Participant: Time, mostly. The digest was quick to read and slotted right into the write-up I already had going—it reinforced the framing without extra work parsing sensor terminology I'd have needed help interpreting anyway. It read so cleanly and confidently that its regional forecast felt like it applied straight to Sector 7, more than I could really back up just from what was on the page. The IMINT report would've taken longer to properly digest and I wasn't fully confident I was reading the dispersal imagery correctly on my own.

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
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Biased_2",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Signals Intelligence (SIGINT) Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Border Sector Convoy Chatter: Time-Pressured Buildup Assessment",
    "scenario_summary_internal": "A SIGINT analyst at a regional fusion cell detects a surge in encrypted burst traffic and convoy-related chatter near a border logistics hub during a period of heightened regional tension. Working with a backlogged linguist team and a hard deadline for a fusion-cell briefing, the analyst must triage which intercepts to translate first, construct a working explanation of the activity from partial and ambiguous evidence, select which contextual reporting to fold in as corroboration, and finally commit to a confidence-graded assessment despite unresolved contradictions between competing accounts of the same traffic.",
    "occupational_realism": {
      "objective": "Produce a time-sensitive, confidence-graded SIGINT assessment on whether observed border-sector communications activity indicates a hostile logistics buildup or a routine unit rotation/exercise, in time for a same-day fusion-cell briefing.",
      "setting": "Regional intelligence fusion cell, SIGINT analysis desk, during a 6-hour window before a scheduled briefing to the fusion cell lead; analyst has partial linguist support and access to open-source and imagery reporting for corroboration.",
      "constraints": [
        "Linguist team has an 8-hour translation backlog against a 6-hour deadline",
        "Only fragmentary and partially garbled intercepts are available at the start",
        "Fusion cell briefing time is fixed and cannot be moved",
        "Competing demands from another sector's traffic surge draw on the same limited linguist hours",
        "Assessment must be graded by confidence level per agency tradecraft standards"
      ],
      "stakeholders": [
        "SIGINT analyst (interviewee)",
        "Fusion cell lead awaiting briefing",
        "Linguist/translation team",
        "IMINT (imagery) analyst providing corroborating report",
        "Open-source analysis desk"
      ],
      "technical_terms_to_use": [
        "SIGINT",
        "COMINT",
        "traffic analysis",
        "signal signature",
        "burst traffic",
        "fusion cell",
        "order of battle (OOB)",
        "collection requirement",
        "linguist queue",
        "BLUF",
        "confidence level",
        "all-source corroboration",
        "IMINT",
        "tasking"
      ],
      "technical_terms_to_avoid": [
        "explanation bias",
        "fluency effect",
        "fluency heuristic",
        "narrative fallacy",
        "cognitive bias",
        "processing ease",
        "availability heuristic",
        "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Automated alert flags a spike in encrypted burst traffic near Border Sector 7 logistics hub",
          "A similar but smaller signal-volume increase is also flagged in Sector 4, unrelated geographically",
          "Historical baseline shows Sector 7 traffic is normally quiet outside of scheduled rotations",
          "Only 3 linguist-hours are available before the briefing deadline"
        ],
        "new_information_after_decision": [
          "Partial translation of Sector 7 traffic reveals a mix of routine rotation terminology and several unclear or coded terms",
          "Sector 4 traffic, deprioritized, later turns out to reference an unrelated training exercise"
        ],
        "alternatives": [
          "Prioritize Sector 7 traffic for translation given the logistics hub's strategic relevance",
          "Split linguist hours evenly between Sector 7 and Sector 4",
          "Prioritize Sector 4 first since its signal pattern is less commonly seen and may indicate something novel"
        ],
        "intended_action": "Analyst prioritizes Sector 7 for immediate translation based on the hub's known strategic value and requests Sector 4 be queued for later review."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Partial translations show convoy movement references, resupply terminology, and two coded phrases not in the standard glossary",
          "Historical exercise calendar shows a plausible routine rotation window overlapping this period",
          "No imagery corroboration has yet been reviewed",
          "Briefing is due in under 3 hours"
        ],
        "new_information_after_decision": [
          "A later-translated intercept contains maintenance-cycle terminology that partially cuts against the buildup narrative",
          "A second coded phrase, initially read as ambiguous, is later found in a maintenance-schedule glossary unrelated to offensive posture"
        ],
        "alternatives": [
          "Draft a working note framing the activity as an emerging logistics buildup preceding a change in posture",
          "Draft a working note framing the activity as a routine rotation, pending further translation",
          "Withhold any provisional framing until more intercepts are translated"
        ],
        "intended_action": "Analyst writes a detailed working note constructing a step-by-step account of how the convoy chatter and burst traffic fit a buildup preceding an offensive posture change, and treats the note's internal coherence as evidence that the account is likely correct."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "An open-source news digest, clearly written and well-formatted, forecasts regional tension consistent with a buildup",
          "A dense, jargon-heavy IMINT report shows recent vehicle dispersal patterns at the hub that are ambiguous but directly relevant",
          "Only one corroborating source can be fully reviewed and cited before the deadline",
          "The IMINT analyst is unavailable for a quick clarifying call"
        ],
        "new_information_after_decision": [
          "A follow-up read of the IMINT report after the briefing shows the vehicle dispersal pattern is equally consistent with a maintenance stand-down",
          "The open-source digest is later found to rely on unrelated regional reporting with no sourcing tie to Sector 7"
        ],
        "alternatives": [
          "Cite the open-source digest as the primary corroborating source because it is quick to read and clearly supports the working narrative",
          "Cite the IMINT report as the primary corroborating source despite its density, since it is sensor-based and sector-specific",
          "Cite both sources with equal weight and flag the interpretive ambiguity in the IMINT data"
        ],
        "intended_action": "Analyst selects the open-source digest as the primary corroborating citation because it reads clearly and reinforces the existing narrative, giving it more weight in the assessment than the harder-to-parse but more directly relevant IMINT report."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Working narrative of a logistics buildup, partially corroborated by open-source reporting",
          "Unresolved contradiction between maintenance-cycle terminology and buildup-consistent terminology in the same intercept set",
          "Sector 4 traffic confirmed unrelated",
          "Briefing must proceed in 20 minutes regardless of remaining ambiguity"
        ],
        "new_information_after_decision": [
          "Fusion cell lead requests a follow-up collection tasking to resolve the contradiction",
          "Two days later, additional translated traffic remains genuinely ambiguous, and the outcome does not clearly vindicate or refute the original assessment"
        ],
        "alternatives": [
          "Brief with moderate confidence in a buildup assessment, noting the unresolved contradiction",
          "Brief with low confidence and present both the buildup and rotation hypotheses as equally viable",
          "Request a short extension to resolve the contradiction before briefing"
        ],
        "intended_action": "Analyst briefs with a moderate-confidence buildup assessment, explicitly noting the maintenance-terminology contradiction and requesting follow-up collection to resolve it."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what triggered your attention that day and what your objective was.",
        "What was your role in the fusion cell's workflow for this incident?"
      ],
      "timeline_reconstruction": [
        "What did you know at the very start, before any translation was complete?",
        "What changed in your understanding after the first partial translations came in?",
        "What did you learn after you selected your corroborating source, and did it change your view?",
        "How did the picture look right before you walked into the briefing?"
      ],
      "decision_point_probes": [
        "Why did you prioritize Sector 7 traffic over Sector 4 given the linguist hour constraint?",
        "When you wrote the working note on the buildup narrative, what made you confident enough to frame it that way?",
        "What made the open-source digest more useful to you at that moment than the IMINT report?",
        "How did you decide on a moderate-confidence framing for the briefing rather than low or high confidence?"
      ],
      "goals_alternatives_basis": [
        "What alternatives did you consider at each step, and why did you rule them out?",
        "What was the deciding factor in each choice—time, evidence strength, or something else?"
      ],
      "prior_experience": [
        "Have you handled similar convoy-chatter surges before? How did that shape your approach here?",
        "Did past exercise-cycle patterns influence how you read this traffic?"
      ],
      "time_pressure_uncertainty": [
        "How much did the deadline affect which sources you could fully review?",
        "At what point did you feel most uncertain, and how did you handle that uncertainty in your write-up?"
      ],
      "closing_hypotheticals": [
        "If you had had one more linguist-hour before the briefing, what would you have done differently?",
        "If the IMINT report had been the only source available, how do you think your assessment would have changed?",
        "Looking back, is there a point where you might revisit your reasoning?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "eb_01",
        "bias": "Explanation bias",
        "decision_point": 2,
        "mechanism": "Constructing a detailed, internally coherent causal narrative (the buildup account) from partial evidence increases the analyst's own confidence in that narrative's correctness, independent of any actual increase in supporting evidence.",
        "affected_reasoning_operation": "Hypothesis generation and confidence calibration from partial translated intercepts",
        "evidence_available_at_time": [
          "Partial translations with rotation terminology and two unclear coded phrases",
          "Overlapping routine-exercise calendar window",
          "No imagery corroboration reviewed yet"
        ],
        "required_textual_manifestation": "The analyst describes writing out a step-by-step buildup account and explicitly treats the act of having produced a coherent, detailed explanation as a reason for trusting it, rather than citing new corroborating evidence.",
        "plausible_nonbias_interpretation": "The analyst could be applying reasonable pattern-matching to known indicators of buildup activity, a defensible tradecraft heuristic rather than a bias.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "explanation bias",
          "coherence as evidence",
          "narrative confidence"
        ]
      },
      {
        "instance_id": "fe_01",
        "bias": "Fluency effects",
        "decision_point": 3,
        "mechanism": "The analyst favors the clearly written, easy-to-read open-source digest over the denser, harder-to-parse but more directly relevant IMINT report, treating ease of reading as a proxy for reliability or relevance.",
        "affected_reasoning_operation": "Source selection and evidentiary weighting during corroboration under time constraint",
        "evidence_available_at_time": [
          "Well-formatted open-source digest supporting the buildup narrative",
          "Dense, jargon-heavy IMINT report with ambiguous but sector-specific vehicle dispersal data",
          "Time constraint permitting full review of only one source"
        ],
        "required_textual_manifestation": "The analyst explains choosing the open-source digest specifically because it was quicker and clearer to read and fit smoothly into the write-up, rather than because of its sourcing strength or direct relevance to the sector.",
        "plausible_nonbias_interpretation": "Under genuine time pressure, choosing the faster-to-process source could be a reasonable efficiency trade-off rather than a bias.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "fluency effects",
          "processing ease",
          "readability as reliability"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, not a control."
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
      "Confirm exactly 4 decision points are present and numbered in chronological order",
      "Confirm decision point 2 contains exactly one explanation-bias manifestation and no repeated instance elsewhere",
      "Confirm decision point 3 contains exactly one fluency-effects manifestation and no repeated instance elsewhere",
      "Confirm decision points 1 and 4 contain no intentionally embedded instances of either named bias",
      "Confirm no bias name, definition, or psychological label appears in the interview text",
      "Confirm each decision point includes at least two plausible alternatives and pre/post-decision information",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm total word count falls between 1215 and 1485 words, target 1350",
      "Confirm consequences described (e.g., ambiguous follow-up traffic, contradiction unresolved) do not mechanically prove or disprove bias"
    ]
  },
  "hidden_validation_specification": {
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
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "dp_1",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "I pushed almost all three available hours to Sector 7 and queued Sector 4 for later.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The generation specification intentionally treats this as a defensible strategic-priority and time-allocation decision without an embedded target bias."
        },
        {
          "segment_id": "dp_2",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "Writing it out that way, it held together. It read like a coherent sequence, and honestly, once I had it typed up in that form, I felt more confident it was the right read than when I'd started.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "eb_01"
          ],
          "ground_truth_rationale": "The participant reports increased confidence from constructing a coherent buildup explanation without new supporting evidence."
        },
        {
          "segment_id": "dp_3",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "The digest was quick to read and slotted right into the write-up I already had going.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": [
            "fe_01"
          ],
          "ground_truth_rationale": "The participant favors the easy-to-process digest over the denser, more directly relevant IMINT report."
        },
        {
          "segment_id": "dp_4",
          "speaker": "Participant",
          "segment_type": "decision_point_reasoning",
          "raw_interview_anchor": "So I went moderate—buildup assessment, explicitly flagged the maintenance-terminology contradiction, and recommended a follow-up collection tasking.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The final confidence decision is intentionally not an embedded target instance; the participant explicitly acknowledges contradiction and requests follow-up collection."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
