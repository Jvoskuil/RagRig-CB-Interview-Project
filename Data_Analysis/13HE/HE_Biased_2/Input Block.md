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
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
