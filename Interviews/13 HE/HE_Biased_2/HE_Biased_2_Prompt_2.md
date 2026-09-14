You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HE_Biased_2",
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
  }}}

WRITING REQUIREMENTS
1. Produce only the interview, with no preface, postscript, analysis, labels, answer key, bias names, or JSON.
2. Use approximately 1,350 words, with an acceptable range of 1,215–1,485 words.
3. Use exactly four decision points.
4. Write a natural semi-structured CTA interview between an interviewer and a domain-credible participant. Include both questions and answers.
5. Begin with a brief consent/role/context exchange, then obtain an incident account, reconstruct the timeline, revisit the four decision points, probe the participant's reasoning, and end with relevant hypotheticals.
6. Make the participant's account coherent, specific, and occupationally plausible. Include concrete cues, information sources, goals, constraints, alternatives, time pressure, uncertainty, prior experience, and consequences.
7. Make the target biases inferable from patterns of reasoning, not from vocabulary that names or defines them.
8. Do not make every decision biased. Preserve natural variation, including justified reasoning and uncertainty.
9. Do not equate an incorrect decision or bad outcome with a bias. Include enough context for alternative explanations to remain possible.
10. Keep the number of decision points, actors, technical terms, and narrative complexity aligned with the specification.
11. For multiple target biases, distribute them across the incident. Each bias must have a distinct manifestation, but interactions may occur naturally.
12. For `vocabulary_control`, preserve the same occupational vocabulary and narrative complexity while writing decisions supported by balanced evidence and reasonable consideration of alternatives. Do not insert target-bias evidence.
13. For `ambiguous_control`, include genuinely ambiguous reasoning that has plausible non-bias explanations, but do not intentionally instantiate a target bias. Do not use exaggerated contradiction or suspiciously artificial neutrality.
14. For `counterfactual`, minimally alter the specified causal variable. Preserve all other material facts, wording patterns, and decision structure as far as possible. Make the changed variable causally relevant, not merely correlated with the outcome.
15. Include at least one probe asking what information would have changed the decision and one probe asking what would have happened if a key feature had been different.
16. Do not add facts that contradict the generation specification.
17. Avoid stereotypes, protected-class generalizations, and gratuitous sensitive content.

RECOMMENDED STRUCTURE
- Opening and role context: 100–150 words.
- Initial incident account: 250–350 words.
- Timeline reconstruction: 150–200 words.
- Four decision-point sections with probes: 550–650 words total.
- Closing reflection and hypothetical: 150–250 words.

DIALOGUE STYLE
- Label turns as `Interviewer:` and `Participant:`.
- Let answers vary in length and certainty.
- Use natural repairs, qualifications, and references to evidence.
- Avoid repeatedly asking the same generic question.
- Do not explicitly state that the participant is biased, unbiased, rational, irrational, or subject to an experimental condition.

FINAL SILENT CHECK
Before outputting, verify word count, four decision points, domain realism, target-bias concealment, control fidelity, and causal minimality where applicable. If a target bias cannot be represented without becoming obvious or implausible, revise the incident rather than explaining the problem.

OUTPUT
Return only the interview text.
