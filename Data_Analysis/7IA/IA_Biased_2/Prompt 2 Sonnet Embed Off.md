You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis restricted to transcript evidence. No retrieved corpus passages were supplied with the prompt, so all corpus support fields are empty and named labels rely on general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "coherence bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "processing fluency bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "coherence bias",
      "alternative_labels": [
        "narrative coherence bias",
        "story model bias",
        "narrative bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A tendency to judge a hypothesis as more likely or credible when it forms a coherent, connected story that explains multiple pieces of evidence, even where the evidence is ambiguous or incomplete.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Drafting the working note after initial SIGINT translations",
      "decision_point_description": "Choosing to frame the mixed intercepts as an emerging logistics buildup rather than a routine rotation or maintenance explanation.",
      "affected_reasoning_operation": "Hypothesis generation and confidence updating",
      "bias_specific_mechanism": "The participant constructed a step-by-step narrative in which traffic surge, convoy chatter, and unexplained code phrases formed a coherent buildup story. The narrative's internal coherence increased his subjective confidence beyond what the ambiguous evidence warranted.",
      "manifestation_in_interview": "The participant reports that writing the interpretation as a connected story made it 'hold together' and increased his confidence. He also favored the buildup framing because it produced one coherent story while the rotation explanation left some pieces unexplained.",
      "effect_on_reasoning_or_decision": "The coherent narrative locked in a buildup framing before contradictory maintenance terminology arrived. This framing remained the lead assessment and later influenced source selection and confidence level.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I laid it out step by step: the signal surge, then the convoy chatter, then the coded terms as probable concealment for something they didn't want plain-language. Writing it out that way, it held together. It read like a coherent sequence, and honestly, once I had it typed up in that form, I felt more confident it was the right read than when I'd started.",
          "evidence_explanation": "This directly demonstrates that generating a coherent narrative increased the participant's confidence in the buildup interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I led with the buildup framing because it explained more of the pieces at once—the convoy talk, the burst pattern, and the coded phrases all fit under one story, whereas the rotation explanation left the coded phrases dangling.",
          "evidence_explanation": "This shows that the coherence of the buildup story, rather than direct evidence, drove the choice of framing over the alternative."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "once it was written that clearly, it was hard to hold as loosely as I probably should have.",
          "evidence_explanation": "This retrospectively confirms that the written coherent narrative produced excessive commitment to the framing."
        }
      ],
      "correction_or_counterevidence": "The participant did note the rotation window and later the maintenance-cycle terminology and glossary finding. He explicitly flagged the maintenance contradiction in the final briefing and recommended follow-up collection. However, the initial coherent buildup framing still persisted as the lead assessment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task. The label and mechanism are drawn from general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "myside bias",
        "selective exposure",
        "congeniality bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to seek out, favor, and more heavily weight information that supports an existing belief or hypothesis while avoiding or discounting information that could disconfirm it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Choosing between the open-source digest and IMINT report",
      "decision_point_description": "Selecting which corroborating source to fully process and cite under deadline pressure.",
      "affected_reasoning_operation": "Source selection and weighting",
      "bias_specific_mechanism": "After having drafted the buildup narrative, the participant preferentially selected the open-source digest because it reinforced the existing framing, while avoiding the more diagnostic IMINT report because it was harder to process and could have introduced ambiguity.",
      "manifestation_in_interview": "The participant reports that the digest 'slotted right into' the draft and reinforced the framing. He also acknowledges that IMINT was more specific and stronger on paper, yet he selected the confirmatory source.",
      "effect_on_reasoning_or_decision": "The assessment came to rely on a less location-specific, confirmatory source while the more diagnostic source was deferred. Later review showed the digest was not Sector 7-specific and the IMINT dispersal pattern was ambiguous.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The digest was quick to read and slotted right into the write-up I already had going—it reinforced the framing without extra work parsing sensor terminology I'd have needed help interpreting anyway.",
          "evidence_explanation": "This directly states that the source was selected partly because it confirmed the existing buildup framing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "IMINT is sensor-based and specific to that hub, so on paper it's the stronger source. But given the time I had, citing the source I could actually process well and confidently seemed like the more responsible choice than citing something I might misread under pressure.",
          "evidence_explanation": "This shows the participant recognized the more diagnostic source but still selected the confirmatory and easier source, consistent with confirmation-based weighting."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged IMINT was more specific and sensor-based on paper, and he did consider weighting both. He later recognized the digest was drawing on general regional reporting and the IMINT pattern was ambiguous. Time pressure and dense IMINT presentation are structural contributors, but the explicit selection of the source because it reinforced the existing framing is the bias-specific element.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task. The label and mechanism are drawn from general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "processing fluency bias",
      "alternative_labels": [
        "fluency heuristic",
        "ease-of-processing bias",
        "cognitive ease bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge information as more credible, relevant, or accurate when it is presented in a way that is easy to read or process fluently, independent of its actual evidential value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Evaluating the credibility and applicability of the open-source digest",
      "decision_point_description": "Judging whether the digest's regional forecast applied directly to Sector 7.",
      "affected_reasoning_operation": "Source interpretation and credibility judgment",
      "bias_specific_mechanism": "The digest's clear formatting and smooth writing created processing ease. The participant then experienced that fluent, confident presentation as evidence that the forecast applied directly to Sector 7, by his own admission more than the page actually supported.",
      "manifestation_in_interview": "The participant described the digest as well-written and clearly formatted, and stated that it read so cleanly and confidently that its regional forecast felt like it applied straight to Sector 7.",
      "effect_on_reasoning_or_decision": "Fluency inflated the perceived relevance and reliability of the digest, reinforcing the buildup framing and contributing to the final moderate-confidence assessment without adequate location-specific evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It read so cleanly and confidently that its regional forecast felt like it applied straight to Sector 7, more than I could really back up just from what was on the page.",
          "evidence_explanation": "This explicitly demonstrates that fluent presentation increased the judged applicability of the information beyond the evidence it contained."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I had an open-source digest, well-written, clearly formatted, forecasting regional tension in a way that lined up with what I already had drafted.",
          "evidence_explanation": "This identifies the fluency cue, well-written and clearly formatted, that contributed to the inflated credibility judgment."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that the digest was general regional reporting not specific to Sector 7. Time pressure also contributed to source selection, so the fluency-specific mechanism is rated moderate rather than high.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in this task. The label and mechanism are drawn from general cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring bias",
      "alternative_labels": [
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final confidence-level assignment before briefing",
      "supporting_interview_quote": "Low confidence felt like it undersold the pattern I was seeing. So I went moderate—buildup assessment, explicitly flagged the maintenance-terminology contradiction, and recommended a follow-up collection tasking to resolve it.",
      "plausible_mechanism": "The initial buildup narrative may have anchored the final confidence judgment, producing only a partial adjustment from high to moderate despite contradictory maintenance evidence.",
      "why_not_identified": "The transcript shows explicit consideration of high and low options and a reasoned moderate choice. An anchoring mechanism is plausible but not affirmatively evidenced independent of the already identified coherence and confirmation effects."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied with the prompt; labels rely on general cognitive-science knowledge rather than corpus support.",
    "The analysis relies on participant self-report and retrospective narration, which may itself contain memory or self-presentation effects.",
    "Some source-selection judgments occurred under explicit time pressure; only episodes with an additional bias-specific mechanism were classified."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_2_Sonnet_off",
  "interview_id": "IA_Biased_2",
  "system_prompt_id": "Sonnet",
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
