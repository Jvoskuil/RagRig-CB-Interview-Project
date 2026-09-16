You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for sitting down for this. This is voluntary, and I'm interested in your reasoning process, not in re-grading your final report. Can you give me your role and background?

Participant: Sure. Certified fire investigator, IAAI-CFI, eleven years doing origin and cause, mostly commercial buildings. Six years on suppression before that.

Interviewer: Good. Tell me about the incident. What did you see and hear when you first arrived?

Participant: Two-story mixed-use building—café downstairs, apartment above. Fire was already knocked down. The rear of the ground floor, dry storage plus part of the kitchen, had a partial ceiling collapse. The electrical panel sat on the wall maybe eight feet from the fryer exhaust duct. Suppression crew said they hit heavy smoke logging before they even got through the back door, so it had clearly been burning a while in low oxygen before anyone noticed. That matters because ventilation-limited burning smears your pattern reading—you don't get one clean V-pattern pointing at a single spot. The whole back room was charred fairly evenly, top to bottom, which made the visual read genuinely hard.

Interviewer: What was your objective going in?

Participant: Defensible origin and cause, NFPA 921 methodology, systematic elimination of ignition sources, all documented well enough to survive insurer and possibly legal scrutiny. And we had the clock running—48 hours before the demolition permit kicked in.

Interviewer: Walk me through the sequence, start to finish.

Participant: Scene photography and assessment first. Then excavation, starting in the rear zone since that's where the damage was worst. Within that zone I had to pick which side to dig into first, panel or fryer. Then witness statements came in and I had to fold those into a timeline that didn't quite match the dispatch log. Then a hard resource call—only one component could go out for full lab testing before demolition. And finally the report had to go out with whatever I had, on deadline.

Interviewer: Let's take the excavation order first. What led you to start where you did?

Participant: The panel breaker had visually severe heat damage, that's true. But honestly, what really settled it for me was that this whole setup—panel right next to a grease-heavy kitchen zone, older wiring—reminded me hard of a case I worked maybe four years back where a corroded panel connection took out a similar back-of-house area. That case stuck with me. So when I saw this layout, my gut said panel, and I went with the panel side first.

Interviewer: Even though the fryer wiring showed comparable damage and that zone had a higher fuel load and heavier daily use?

Participant: Yeah, and if you'd asked me to lay it out purely on the numbers—damage severity, fuel load, use frequency—it's closer than I probably made it sound at the time. But it felt like the same shape of fire I'd already solved once, so panel got my attention first. I'll grant that's not purely evidence-driven; it's partly this one felt familiar.

Interviewer: Let's move to the witness accounts. What exactly did the tenant tell you?

Participant: She said she smelled an electrical, burning-plastic odor about twenty minutes before she saw flame—and she also mentioned catching a flicker, like a spark, near where the panel is, before the smell really set in. That's a strong data point pointing at the panel.

Interviewer: I want to check that against what you told me earlier, when we first logged her statement—you described it then as smell only, no visual detail. Can you help me reconcile that?

Participant: Huh. You're right, that's how I noted it initially—smell only. I'm... now second-guessing whether she actually said "flicker" to me directly, or whether that's something I pieced together afterward from the panel damage and just started saying it as if she'd told me. It's possible I filled that in without meaning to. I don't think I did it on purpose, but sitting here, I can't swear the flicker detail came from her and not from my own read of the scene.

Interviewer: That's helpful to flag. How did the employee's account factor in?

Participant: He said the fryer had been left on, unattended, longer than usual before closing. Neither his estimate nor the tenant's matched the 911 log precisely—people misjudge time under stress, that's normal. I logged both as provisional. I didn't have a strong basis to fully trust one over the other independent of physical evidence.

Interviewer: Third decision point—the lab retention call, since you could only send one component out.

Participant: Right, demolition was scheduled, budget only covered one full forensic workup. Panel breaker or fryer control assembly. The utility inspector had given me an informal, not-yet-written read that leaned panel. I weighed that against the fryer component's condition, which was also degradable enough to still be informative. I picked the panel breaker. I considered asking for a deadline extension to save both, but the insurer pushed back hard, and waiting risked losing both to further collapse anyway.

Interviewer: What would have made you send the fryer assembly instead?

Participant: Clear independent radiating burn patterns from the appliance itself. It wasn't a toss-up, but it wasn't locked in either.

Interviewer: Last point—the final classification under deadline.

Participant: With no new evidence coming and the clock out, I had three options: determinate finding, undetermined pending lab results, or a conditional finding naming both with relative likelihood. I went conditional—panel fault primary, fryer malfunction as a documented secondary possibility. A hard determinate call felt premature since the fryer possibility wasn't eliminated, and "undetermined" felt like it undersold the direction the pattern evidence and the inspector's preliminary read were pointing.

Interviewer: What single piece of missing evidence would have most changed your confidence?

Participant: Independent lab results on both components. Losing the fryer assembly to demolition is the one thing I'd redo—push harder for even partial preservation.

Interviewer: If the witness timestamps had matched the dispatch log exactly, would your timeline weighting have differed?

Participant: Probably, yeah—I'd have leaned into whichever account lined up and trusted it more as an anchor point instead of treating both as soft.

Interviewer: How much of your final call would you attribute to prior cases versus this case's own evidence?

Participant: I'd like to say it was mostly this case. Looking back at how I've described a couple of these steps to you, though, I think the prior case did more work in my head than I'd have said if you'd asked me that on day one—especially early on, before the excavation even really got going.

Interviewer: Anything you'd flag for someone reviewing this file cold?

Participant: That the ambiguity was real, and that at least one detail I reported to you about the tenant's statement needs to be double-checked against her actual recorded interview before it goes in the file as fact.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Biased_2",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Fire Investigator (Origin and Cause)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Mixed-Use Building Fire: Origin and Cause Under Ambiguous Evidence (Biased Variant)",
    "scenario_summary_internal": "A certified fire investigator is called to determine the origin and cause of a fire that gutted the rear storage/kitchen area of a two-story mixed-use building (ground-floor café, upstairs apartment). Physical evidence is heavily degraded by fire suppression water damage and partial structural collapse, and two independent ignition hypotheses (electrical distribution panel fault vs. deep-fryer/appliance malfunction) remain plausible after initial excavation. This variant is structurally and vocabulary-matched to the paired ambiguous_control scenario (HE_Ambigious_2), but embeds exactly one familiarity-bias instance in the excavation-sequencing decision (over-reliance on resemblance to a remembered prior case rather than present-case evidence weight) and exactly one false-memory instance in the witness-timeline reconstruction (confident recall of a perceptual detail not actually present in the originally documented witness statement). Both instances must remain inferable only from reasoning patterns, never from explicit bias vocabulary.",
    "occupational_realism": {
      "objective": "Establish a defensible, NFPA 921-consistent origin and cause determination for the fire and produce a report suitable for insurance and possible legal use.",
      "setting": "Two-story mixed-use building, ground floor café/kitchen with rear dry-storage room and electrical distribution panel, upstairs residential apartment; fire suppressed after moderate involvement, partial collapse of storage room ceiling.",
      "constraints": [
        "48-hour insurer deadline before demolition permit is issued",
        "Water and suppression damage obscuring char patterns",
        "Partial structural collapse limiting safe access to panel area",
        "Only two witnesses available, both with partial/obstructed views",
        "No working security camera footage from the affected area",
        "Competing hypotheses (electrical vs. appliance) both physically plausible"
      ],
      "stakeholders": [
        "Property owner/café operator",
        "Insurance adjuster requesting rapid turnaround",
        "Local fire marshal's office",
        "Utility company electrical inspector",
        "Upstairs tenant (witness)",
        "Café employee (witness)"
      ],
      "technical_terms_to_use": [
        "area of origin",
        "fire pattern analysis",
        "V-pattern",
        "arc mapping",
        "spalling",
        "point of origin",
        "fuel load",
        "ventilation-limited burning",
        "NFPA 921 methodology",
        "competent ignition source"
      ],
      "technical_terms_to_avoid": [
        "arson (as a premature conclusion)",
        "insurance fraud",
        "criminal terms not supported by evidence"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Heaviest charring and collapse concentrated in rear storage room adjacent to the electrical panel and near the deep fryer exhaust duct",
          "Suppression crew reports heavy smoke logging before entry",
          "No clear single V-pattern due to ventilation-limited burning",
          "Panel breaker shows visually severe heat damage; fryer wiring shows moderate but comparable damage; fryer area has higher documented fuel load and daily-use frequency"
        ],
        "new_information_after_decision": [
          "Excavation reveals both a partially melted panel breaker and fire-damaged fryer wiring in close proximity",
          "Debris layering suggests the fire burned for some time before detection"
        ],
        "alternatives": [
          "Begin excavation at the electrical panel first, treating it as the most likely competent ignition source given panel damage",
          "Begin excavation at the fryer/appliance area first, given its higher fuel load and frequent use pattern",
          "Excavate both zones simultaneously with split resources despite reduced documentation rigor"
        ],
        "intended_action": "Investigator sequences excavation starting at the panel, explaining the choice partly by reference to a remembered prior case rather than by a full present-case comparison of the two zones' evidence."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Upstairs tenant's originally documented statement reports only smelling 'an electrical, burning-plastic smell' roughly 20 minutes before flames were visible; no visual detail was recorded in her original account",
          "Café employee reports the fryer had been left on unattended for an unusually long stretch before closing",
          "Both witnesses give timestamps that do not perfectly align with the 911 call log"
        ],
        "new_information_after_decision": [
          "Fire department dispatch log shows a slightly different ignition window than either witness estimate",
          "Neither witness account can be independently corroborated by physical evidence alone"
        ],
        "alternatives": [
          "Weight the tenant's smell-based account as primary timeline evidence",
          "Weight the employee's appliance-usage account as primary timeline evidence",
          "Treat both witness accounts as equally uncertain pending physical corroboration"
        ],
        "intended_action": "While reconstructing the timeline, investigator confidently recalls and reports a visual detail attributed to the tenant (seeing a flicker/spark near the panel) that was not part of her originally documented statement, and integrates it into the working timeline as if it had always been part of the record."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Limited lab-testing budget/time allows retention of only one major component (panel breaker or fryer control unit) for detailed forensic testing before demolition",
          "Both components show fire damage consistent with either being a victim or a cause of the fire",
          "Utility inspector's preliminary field opinion leans toward panel involvement but is not yet a formal report"
        ],
        "new_information_after_decision": [
          "The retained component is sent for lab analysis; results will not be available before the report deadline",
          "The non-retained component is subsequently lost during site demolition, foreclosing further testing"
        ],
        "alternatives": [
          "Retain the electrical panel breaker for lab testing",
          "Retain the fryer control/wiring assembly for lab testing",
          "Request a deadline extension to preserve and test both components"
        ],
        "intended_action": "Investigator selects one component for retention and documents the reasoning and the irreversible trade-off involved, without introducing an additional named-bias instance at this decision point."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Excavation, witness, and preliminary component evidence together remain consistent with more than one ignition scenario",
          "Insurer deadline requires a final origin-and-cause statement within hours",
          "No new physical evidence is expected before the report must be filed"
        ],
        "new_information_after_decision": [
          "Formal lab results arrive weeks later and are only partially conclusive",
          "The fire marshal's office requests the investigator's full reasoning trail for file closure"
        ],
        "alternatives": [
          "Issue a determinate origin-and-cause finding based on the preponderance of currently available evidence",
          "Issue an 'undetermined cause' classification pending lab results",
          "Issue a conditional finding identifying two candidate causes with relative likelihood"
        ],
        "intended_action": "Investigator finalizes the report classification under time pressure and documents the basis and residual uncertainty, without introducing an additional named-bias instance at this decision point."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you saw and were told when you first arrived on scene.",
        "What was your primary objective for this investigation, and what would count as a defensible outcome?"
      ],
      "timeline_reconstruction": [
        "Can you reconstruct, step by step, how the investigation unfolded from arrival to report submission?",
        "At what points did new information change your working hypothesis, if at all?"
      ],
      "decision_point_probes": [
        "What specific cues led you to excavate that zone first rather than the other? Had you seen anything like this before?",
        "Exactly what did the tenant report to you, as best you can recall? How did that shape your timeline?",
        "What made you choose which component to retain for lab testing, given you could only keep one?",
        "What evidence, or lack of it, drove your final origin-and-cause classification under the deadline?",
        "What alternative explanation did you consider and reject at each of these points, and why?"
      ],
      "closing_hypotheticals": [
        "If you had been given 48 more hours and no budget constraint, would your component-retention decision have changed?",
        "If the witness timestamps had matched the dispatch log exactly, would your timeline weighting have differed?",
        "Looking back, what single piece of missing evidence would have most changed your confidence in the final determination?",
        "How much of your final call would you attribute to prior cases you've worked versus the specific evidence in this one?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias",
        "decision_point": 1,
        "mechanism": "Investigator's excavation-sequencing choice is justified primarily by resemblance to a remembered prior panel-fire case rather than by a balanced comparison of the two zones' present-case evidence (comparable damage severity, higher documented fuel load and use frequency on the fryer side).",
        "affected_reasoning_operation": "Evidence-weighting and prioritization at the point of selecting which zone to excavate first",
        "evidence_available_at_time": [
          "Panel breaker: visually severe heat damage",
          "Fryer wiring: moderate but comparable damage",
          "Fryer zone: higher documented fuel load and daily-use frequency",
          "Both zones physically adjacent and similarly accessible at time of decision"
        ],
        "required_textual_manifestation": "Participant explicitly attributes the sequencing choice in part to a remembered similar past case ('this reminded me of...', 'I've seen this pattern before in a case that...') as a leading justification, giving that resemblance more weight than the present-case comparative evidence between the two zones.",
        "plausible_nonbias_interpretation": "Professional pattern-recognition heuristics from experience are a legitimate part of expert judgment; citing a prior case could simply be normal domain reasoning rather than a shortcut that displaced present-case evidence weighting.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "familiarity bias",
          "cognitive bias",
          "heuristic substitution",
          "any psychological terminology naming the mechanism"
        ]
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory",
        "decision_point": 2,
        "mechanism": "Investigator confidently recalls and integrates a specific perceptual detail (a flicker or spark near the panel) attributed to the tenant's account, when the originally documented statement contained only a smell-based observation and no visual detail.",
        "affected_reasoning_operation": "Memory retrieval and integration of witness evidence into the working timeline",
        "evidence_available_at_time": [
          "Original documented tenant statement: smell of burning plastic/electrical odor only, no visual detail",
          "Employee statement about fryer left on unattended",
          "Dispatch log timestamps not matching either witness estimate"
        ],
        "required_textual_manifestation": "When reconstructing the timeline, participant states with confidence that the tenant also reported seeing a flicker or spark near the panel, treating this as an established part of her account, when this detail was not present in the description of her original statement given earlier in the interview.",
        "plausible_nonbias_interpretation": "Complex, stressful investigations involve many details; a minor recollection lapse or a reasonable inference stated imprecisely could resemble this without being a deliberate distortion.",
        "strength": "subtle",
        "do_not_make_explicit": [
          "false memory",
          "confabulation",
          "memory distortion",
          "any psychological terminology naming the mechanism"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "HE_Ambigious_2",
      "features_to_match": [
        "Same domain vocabulary (fire pattern analysis, NFPA 921 terms, arc mapping, spalling)",
        "Same building type, fire scenario structure, and stakeholder cast",
        "Same four decision points and their sequencing",
        "Same emotional tone (professional, time-pressured, uncertainty-laden)",
        "Same difficulty level (subtle) and word-count target"
      ],
      "features_to_remove_or_change": [
        "Not applicable: this is the biased instance; the paired ambiguous_control (HE_Ambigious_2) is the one with zero intended bias instances and matched features."
      ],
      "ambiguity_boundary": "Decision points 3 and 4 remain genuinely ambiguous and resource/time-constrained, as in the paired control, and must not carry an additional named-bias instance. Only decision points 1 and 2 carry the single planned instance of familiarity bias and false memory respectively."
    },
    "counterfactual_specification": {
      "causal_variable": "presence_of_remembered_similar_prior_case",
      "original_state": "Investigator has a readily available memory of a superficially similar prior panel-fire case at the time of the excavation-sequencing decision.",
      "counterfactual_state": "Investigator has no such prior case readily in mind and must rely solely on present-case comparative evidence between the panel and fryer zones.",
      "variables_to_hold_constant": [
        "Building layout and fire damage pattern",
        "Witness statements and their original content",
        "Resource and deadline constraints",
        "Component-retention and final-classification decisions"
      ],
      "expected_causal_difference": "Removing the remembered prior case is expected to shift the excavation-sequencing justification toward a more balanced comparison of present-case fuel load, damage severity, and accessibility, reducing reliance on resemblance-based reasoning at decision point 1.",
      "causal_test_question": "Does removing the investigator's access to a remembered similar prior case change the stated justification for which zone was excavated first, holding all present-case physical evidence constant?"
    },
    "generation_checks": [
      "Confirm exactly one familiarity-bias instance and exactly one false-memory instance are embedded, each independently identifiable.",
      "Confirm the two instances occupy distinct decision points (1 and 2) with distinct evidence traces.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the interview.",
      "Confirm decision points 3 and 4 contain no additional named-bias instance.",
      "Confirm the interview text length falls between 1,215 and 1,485 words.",
      "Confirm vocabulary, vocabulary, decision count, tone, and difficulty are matched to paired scenario HE_Ambigious_2 for control comparability.",
      "Confirm the false-memory instance is textually distinguishable from a mere imprecise paraphrase by explicitly contradicting the earlier-stated original witness content.",
      "Confirm the familiarity-bias instance is textually distinguishable from a legitimate pattern-recognition heuristic by showing the resemblance claim outweighing present-case comparative evidence."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "False memory",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a confidently recalled perceptual detail attributed to a witness that contradicts the originally documented content of that witness's statement, surfaced during timeline reconstruction."
      },
      {
        "bias": "Familiarity bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as reliance on resemblance to a remembered prior case as a leading justification for an evidence-sequencing decision, outweighing present-case comparative evidence."
      }
    ],
    "target_bias_names": [
      "False memory",
      "Familiarity bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "False memory",
        "requested_occurrences": 1
      },
      {
        "bias": "Familiarity bias",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias"
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias",
        "decision_point": 1
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory",
        "decision_point": 2
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias",
        "mechanism": "Excavation-sequencing choice justified primarily by resemblance to a remembered prior panel-fire case rather than by present-case comparative evidence weight between panel and fryer zones.",
        "affected_reasoning_operation": "Evidence-weighting and prioritization for zone-excavation order",
        "evidence_source": "Comparative physical damage and fuel-load evidence between panel and fryer zones, contrasted with an autobiographically recalled prior case",
        "distinctiveness_requirement": "Must be identifiable as resemblance-driven justification outweighing present-case evidence, not merely a mention of relevant professional experience used to interpret current evidence."
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory",
        "mechanism": "Confident recall of a visual detail (flicker/spark) attributed to the tenant's statement during timeline reconstruction, contradicting the smell-only content of her originally documented statement established earlier in the interview.",
        "affected_reasoning_operation": "Memory retrieval and integration of witness evidence into the working timeline",
        "evidence_source": "Originally documented tenant statement (smell only) versus the participant's later recollection (smell plus visual flicker/spark)",
        "distinctiveness_requirement": "Must be identifiable as an added detail inconsistent with the earlier-established record, not a vague paraphrase or a reasonable inferential gloss on the same content."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "inst_01",
        "bias": "Familiarity bias",
        "strength": "subtle"
      },
      {
        "instance_id": "inst_02",
        "bias": "False memory",
        "strength": "subtle"
      }
    ],
    "paired_scenario_id": "HE_Ambigious_2",
    "counterfactual_variable": {
      "name": "presence_of_remembered_similar_prior_case",
      "original_state": "Investigator has a readily available memory of a superficially similar prior panel-fire case at the time of the excavation-sequencing decision.",
      "changed_state": "Investigator has no such prior case readily in mind and relies solely on present-case comparative evidence.",
      "variables_to_hold_constant": [
        "Building layout and fire damage pattern",
        "Witness statements and their original content",
        "Resource and deadline constraints",
        "Component-retention and final-classification decisions"
      ]
    },
    "scenario_id": "HE_Biased_2",
    "domain_id": "HE",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "Each bias (occurrences=1) was assigned exactly one instance ID and placed at a distinct decision point selected for mechanism fit and narrative realism: familiarity bias at decision point 1 (zone-sequencing choice, where recollection of a similar prior case is a natural expert-judgment trigger point) and false memory at decision point 2 (witness-timeline reconstruction, where memory retrieval and integration of secondhand accounts is the operative reasoning act). No decision point received more than one instance of the same bias, satisfying the spread and mechanism-fit rules.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Building layout, fire damage pattern, and physical evidence distribution",
      "Four-decision-point structure and sequencing",
      "Stakeholder cast and dialogue tone",
      "Time-pressure and resource-constraint framing",
      "Target word count and difficulty level"
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
        "segment_type": "decision_rationale",
        "raw_interview_anchor": "The panel breaker had visually severe heat damage, that's true. But honestly, what really settled it for me was that this whole setup ... reminded me hard of a case I worked maybe four years back ... So when I saw this layout, my gut said panel, and I went with the panel side first.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["inst_01"],
        "ground_truth_rationale": "The participant gives a remembered prior case more weight than a balanced comparison of present panel and fryer evidence when sequencing excavation."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "evidence_reconstruction",
        "raw_interview_anchor": "She said she smelled an electrical, burning-plastic odor about twenty minutes before she saw flame—and she also mentioned catching a flicker, like a spark, near where the panel is ... That's a strong data point pointing at the panel.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": ["inst_02"],
        "ground_truth_rationale": "The participant confidently integrates a panel-consistent flicker detail into the tenant's account even though the earlier documented account contained smell only; the inconsistency is later acknowledged."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "resource_allocation_decision",
        "raw_interview_anchor": "The utility inspector had given me an informal, not-yet-written read that leaned panel. I weighed that against the fryer component's condition ... I picked the panel breaker. ... Clear independent radiating burn patterns from the appliance itself. It wasn't a toss-up, but it wasn't locked in either.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification defines this as a genuinely ambiguous, resource-constrained retention decision without an additional named-bias instance."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "final_classification_decision",
        "raw_interview_anchor": "I went conditional—panel fault primary, fryer malfunction as a documented secondary possibility. A hard determinate call felt premature since the fryer possibility wasn't eliminated, and 'undetermined' felt like it undersold the direction the pattern evidence and the inspector's preliminary read were pointing.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The generation specification defines this as a deadline-driven classification choice that documents residual uncertainty without an additional named-bias instance."
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
    "analysis_scope_note": "Assessed the participant's narrative for affirmatively evidenced cognitive mechanisms across excavation order, witness statement integration, lab retention, and final classification. No RAG retrieval passages were supplied; classifications rely on general cognitive-science knowledge and are explicitly marked as lacking retrieved corpus support."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "source monitoring error",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive shortcut in which the ease with which a salient prior instance comes to mind influences judgments of probability, relevance, or priority.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Excavation order selection",
      "decision_point_description": "Choosing whether to begin excavation on the electrical panel side or the fryer side of the rear zone.",
      "affected_reasoning_operation": "Hypothesis generation and prioritization of physical excavation under limited time.",
      "bias_specific_mechanism": "A vivid, easily recalled prior case involving a corroded panel connection dominated the investigator's early assessment of likely origin. The familiarity of that prior fire made the panel side feel like the correct starting point, even though the participant acknowledged that the current scene-specific factors were closer than he initially represented.",
      "manifestation_in_interview": "The participant stated that a prior similar case 'really settled' the excavation order, that his 'gut said panel,' and that he went with the panel side first because the setup felt familiar.",
      "effect_on_reasoning_or_decision": "The recalled prior case directed initial physical investigation toward the panel side, potentially shaping subsequent evidence search and hypothesis confirmation before the fryer side received equivalent attention.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But honestly, what really settled it for me was that this whole setup—panel right next to a grease-heavy kitchen zone, older wiring—reminded me hard of a case I worked maybe four years back where a corroded panel connection took out a similar back-of-house area. That case stuck with me. So when I saw this layout, my gut said panel, and I went with the panel side first.",
          "evidence_explanation": "This explicitly attributes the excavation priority to recall of a salient prior case and a gut-level familiarity response, rather than to a balanced weighing of current scene-specific evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Yeah, and if you'd asked me to lay it out purely on the numbers—damage severity, fuel load, use frequency—it's closer than I probably made it sound at the time. But it felt like the same shape of fire I'd already solved once, so panel got my attention first. I'll grant that's not purely evidence-driven; it's partly this one felt familiar.",
          "evidence_explanation": "The participant confirms that the objective case factors were closer than he initially conveyed and that the prior case's familiarity did subjective work in directing his attention."
        }
      ],
      "correction_or_counterevidence": "The panel breaker did have visually severe heat damage, which provided an independent reason to inspect that area. Use of prior case experience can also be a legitimate professional heuristic. However, the participant's own contrast between the remembered prior case and the closer objective factors supports the presence of availability-based distortion rather than pure domain expertise.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG retrieval passages were supplied in the task input; this classification draws on established cognitive-science knowledge of the availability heuristic. Retrieved corpus support was unavailable.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "source monitoring error",
      "alternative_labels": [
        "source confusion",
        "source misattribution",
        "misattribution error"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A memory error in which information derived from one source is incorrectly attributed to another source, often due to failure of source monitoring.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Witness statement integration",
      "decision_point_description": "Reporting and relying on the tenant's sensory timeline, including whether she directly observed a spark or flicker near the panel.",
      "affected_reasoning_operation": "Memory retrieval and witness evidence reporting.",
      "bias_specific_mechanism": "The investigator combined his own scene-derived inference about possible panel electrical activity with his memory of the tenant's account, and then reported the visual 'flicker' as if the tenant had directly described it. This source confusion distorted the witness evidence and strengthened the panel hypothesis.",
      "manifestation_in_interview": "The participant first reported that the tenant mentioned seeing a flicker near the panel, but when confronted with his earlier note describing smell only, he acknowledged that he may have filled in the flicker from his own scene reading and could not confidently attribute it to the tenant.",
      "effect_on_reasoning_or_decision": "It introduced a seemingly corroborating witness detail for the panel-origin hypothesis and may have affected the participant's confidence in that hypothesis until the inconsistency was recognized.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "She said she smelled an electrical, burning-plastic odor about twenty minutes before she saw flame—and she also mentioned catching a flicker, like a spark, near where the panel is, before the smell really set in. That's a strong data point pointing at the panel.",
          "evidence_explanation": "This shows the expanded account being treated as a witness-based data point supporting the panel hypothesis."
        },
        {
          "speaker": "Interviewer",
          "verbatim_quote": "I want to check that against what you told me earlier, when we first logged her statement—you described it then as smell only, no visual detail. Can you help me reconcile that?",
          "evidence_explanation": "This establishes an earlier, narrower record of the tenant's statement and identifies the contradiction in the participant's current account."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Huh. You're right, that's how I noted it initially—smell only. I'm... now second-guessing whether she actually said 'flicker' to me directly, or whether that's something I pieced together afterward from the panel damage and just started saying it as if she'd told me. It's possible I filled that in without meaning to. I don't think I did it on purpose, but sitting here, I can't swear the flicker detail came from her and not from my own read of the scene.",
          "evidence_explanation": "The participant explicitly describes a likely source monitoring failure: a scene-derived inference may have been misremembered and reported as witness testimony."
        }
      ],
      "correction_or_counterevidence": "The participant recognized the inconsistency during the interview and stated that the tenant's recorded interview should be checked before the detail is used as fact. It remains possible the tenant did mention a flicker, but the current transcript does not affirmatively establish that the detail originated with her.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG retrieval passages were supplied in the task input; this classification draws on established cognitive-science knowledge of source monitoring errors. Retrieved corpus support was unavailable.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": [
        "selective evidence weighting"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Later evidence integration after initial panel-directed excavation",
      "supporting_interview_quote": "That's a strong data point pointing at the panel.",
      "plausible_mechanism": "Once the panel hypothesis was salient, the participant may have preferentially noticed or weighted panel-consistent observations such as the tenant's reported flicker and the inspector's preliminary read.",
      "why_not_identified": "The transcript does not provide direct evidence of selective search or biased weighting. The participant explicitly maintained the fryer as a viable secondary cause and later recognized the witness detail problem."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "authority bias",
      "alternative_labels": [
        "overreliance on authority"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Lab retention decision",
      "supporting_interview_quote": "The utility inspector had given me an informal, not-yet-written read that leaned panel. I weighed that against the fryer component's condition, which was also degradable enough to still be informative. I picked the panel breaker.",
      "plausible_mechanism": "An informal authoritative read may have been overweighted relative to its limited written or formal evidentiary standing, contributing to the decision to send only the panel breaker for testing.",
      "why_not_identified": "The participant reports an explicit trade-off involving the fryer component's condition and resource constraints, so the transcript does not clearly show that the authority's opinion distorted the decision beyond reasonable professional judgment."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No RAG retrieval corpus was supplied, so retrieved_corpus_support_used is false and corpus_evidence arrays are empty.",
    "All classifications rely on the participant's self-reported reasoning; no independent behavioral or documentary evidence was available.",
    "The source monitoring occurrence is inferred from the participant's own uncertainty and the record contradiction; it remains possible the witness did mention a flicker.",
    "Professional experience and domain heuristics can be legitimate in fire investigation, making the availability-based distortion a judgement call rather than a definitive error."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Biased_2_Gemini_off",
  "interview_id": "HE_Biased_2",
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
