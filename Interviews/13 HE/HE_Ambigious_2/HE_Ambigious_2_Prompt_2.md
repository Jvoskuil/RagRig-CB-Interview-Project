You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HE_Ambigious_2",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Fire Investigator (Origin and Cause)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Mixed-Use Building Fire: Origin and Cause Under Ambiguous Evidence",
    "scenario_summary_internal": "A certified fire investigator is called to determine the origin and cause of a fire that gutted the rear storage/kitchen area of a two-story mixed-use building (ground-floor café, upstairs apartment). Physical evidence is heavily degraded by fire suppression water damage and partial structural collapse, and two independent ignition hypotheses (electrical distribution panel fault vs. deep-fryer/appliance malfunction) remain plausible after initial excavation. The investigator must sequence evidence collection, interpret ambiguous burn patterns and inconsistent witness accounts, decide which components to retain for lab testing under a tight report deadline set by the insurer, and issue a final origin-and-cause determination despite unresolved uncertainty. No named cognitive bias is intentionally embedded; the case is designed so that underdetermined evidence and reasonable professional judgment calls could be mistaken for bias by an untrained observer, but every decision has a plausible non-biased justification.",
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
          "No clear single V-pattern due to ventilation-limited burning"
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
        "intended_action": "Investigator sequences excavation starting with the zone judged to have the clearest fire-pattern indicators, documenting rationale for the sequencing choice."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Upstairs tenant reports smelling 'an electrical, burning-plastic smell' roughly 20 minutes before flames were visible",
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
        "intended_action": "Investigator integrates witness statements into a working timeline while flagging the discrepancy with dispatch data for further reconciliation."
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
        "intended_action": "Investigator selects one component for retention and documents the reasoning and the irreversible trade-off involved."
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
        "intended_action": "Investigator finalizes the report classification under time pressure and documents the basis and residual uncertainty."
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
        "What specific cues led you to excavate that zone first rather than the other?",
        "How did you weigh the two witness accounts against each other and against the dispatch log?",
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
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "HE_Biased_2",
      "features_to_match": [
        "Same domain vocabulary (fire pattern analysis, NFPA 921 terms, arc mapping, spalling)",
        "Same building type, fire scenario structure, and stakeholder cast",
        "Same four decision points and their sequencing",
        "Same emotional tone (professional, time-pressured, uncertainty-laden)",
        "Same difficulty level (subtle) and word-count target"
      ],
      "features_to_remove_or_change": [
        "Remove any deliberate false-memory manifestation in witness/investigator recall (e.g., no invented or distorted recollection of a detail not actually present in the original record)",
        "Remove any deliberate familiarity-bias manifestation (e.g., no over-reliance on a superficially similar past case to short-circuit evaluation of this case's distinct evidence)",
        "Ensure all reasoning gaps are attributable to genuine evidentiary ambiguity, resource constraints, or reasonable professional judgment rather than a named bias mechanism"
      ],
      "ambiguity_boundary": "Underdetermined evidence (ambiguous burn patterns, imperfectly corroborated witness timing, forced single-component retention, and deadline-driven classification) may create outcomes resembling biased reasoning, but each must remain explainable by legitimate evidentiary limits, resource constraints, or accepted investigative heuristics (e.g., NFPA 921-consistent pattern reasoning), not by systematic misremembering or inappropriate reliance on surface-level case similarity."
    },
    "counterfactual_specification": {
      "causal_variable": "not_applicable_for_ambiguous_control",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A - this scenario is an ambiguous_control instance, not a counterfactual instance; no causal manipulation is performed here.",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Confirm zero intended instances of False memory and Familiarity bias are embedded anywhere in the interview text.",
      "Confirm exactly four decision points, each with at least two plausible alternatives.",
      "Confirm every decision point has a documented plausible non-bias explanation available in the probe answers.",
      "Confirm no bias labels, definitions, or psychological terminology appear in the interview.",
      "Confirm the interview text length falls between 1,215 and 1,485 words.",
      "Confirm vocabulary, decision count, tone, and difficulty are matched to paired scenario HE_Biased_2 for control comparability.",
      "Confirm no unintended bias-consistent pattern (e.g., invented recall detail, over-reliance on a similar past case) appears in witness integration or timeline reconstruction sections."
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
