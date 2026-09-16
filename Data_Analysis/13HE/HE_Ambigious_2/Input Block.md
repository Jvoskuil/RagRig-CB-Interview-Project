<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary cognitive task analysis session—I'm interested in how you actually reasoned through the case, not in evaluating your final report. You can decline to answer anything. Can you state your role and certification background briefly?

Participant: Sure. I'm a certified fire investigator, IAAI-CFI, been doing origin and cause work for about eleven years, mostly commercial and mixed-use structures. Before that I was on the suppression side for six years.

Interviewer: Good. Let's start with the incident itself. Walk me through what you saw and were told when you first arrived on scene.

Participant: This was a two-story building, café on the ground floor, an apartment above. Fire had been knocked down by the time I got there, moderate involvement, but the rear of the building—dry storage and part of the kitchen—had a partial ceiling collapse. The electrical panel was mounted on the wall right next to that storage room, maybe eight feet from the fryer exhaust duct. Suppression crew told me they'd hit heavy smoke logging before they even got through the back door, which tells you it had been burning a while in a low-oxygen environment before anyone noticed. That's important because ventilation-limited burning distorts your pattern reading—you don't get a clean V-pattern pointing straight at an origin. Everything in that back room was charred fairly evenly, high up and low down, which made the visual read ambiguous from the start.

Interviewer: What was your primary objective going in?

Participant: Get a defensible origin and cause determination that would hold up for the insurer and, if it came to it, in a legal setting. NFPA 921 methodology, systematic elimination of ignition sources, document everything. The complication here was the clock—insurer wanted the report inside 48 hours because a demolition permit was already queued.

Interviewer: Let's reconstruct the sequence. What happened first, and how did your thinking evolve?

Participant: First thing was scene assessment and photography before touching anything. Heaviest char and the collapse were both concentrated in that rear zone, so that's where excavation had to start—that part wasn't really a choice, that's just where the fire did its damage. Within that zone, though, I had two candidate sources sitting close together: the panel and the fryer. I made a call on which to excavate first. Then came witness statements, which didn't line up cleanly with each other or with the dispatch log. Then a resource constraint—I could only send one component out for full lab testing before the site got demolished. And finally, the report itself had to go out with the evidence I had, not the evidence I wished I had.

Interviewer: Let's slow down on each of those. Starting with the excavation sequence—what specific cues led you to start where you did?

Participant: I started at the panel side. The breaker for that circuit showed heat damage that looked more severe on initial visual than the fryer wiring, and panel failures are a common competent ignition source in older commercial buildings—I've seen it plenty. The alternative would have been starting at the fryer given it's a higher fuel-load area and gets heavy daily use, or splitting the crew to hit both zones at once, which we discussed and rejected because it would've thinned out documentation quality on both sides.

Interviewer: What made the panel side win out over the fryer side, given both were physically plausible?

Participant: Honestly, the visual severity tipped it, plus accessibility—the collapse debris made the fryer area harder to reach safely at that hour, so starting where we could actually work safely made practical sense too. I want to be clear, though: that sequencing decision doesn't by itself tell you which one caused the fire. Excavating one zone first is a logistics call, not a conclusion.

Interviewer: Understood. Now the witness statements. How did you weigh those against each other and against the dispatch log?

Participant: The upstairs tenant said she smelled something like burning plastic or an electrical smell roughly twenty minutes before she saw flame. The café employee said the fryer had been left on, unattended, longer than normal before closing. Neither timestamp matched the 911 log precisely—people are bad at estimating time under stress, that's just standard. I logged both accounts as provisional, flagged the discrepancy explicitly in my notes, and treated neither as more reliable than the other without physical corroboration. I didn't have a strong basis to prefer one witness's timeline over the other's at that point.

Interviewer: What would have changed that weighting for you?

Participant: If either estimate had matched the dispatch window closely, I'd have leaned into that account more. Since neither did, I kept both as soft data points, not anchors.

Interviewer: Third decision point—the lab retention call. Walk me through that.

Participant: This was the hard one. Demolition was scheduled, budget only covered forensic testing on one major component, and I had two candidates: the panel breaker or the fryer control and wiring assembly. The utility company's field inspector had looked at the panel and said, informally, that it looked consistent with an internal fault, but that wasn't a written finding yet, just his gut read on-site. I weighed that against the fryer component's condition, which was also degraded enough that lab testing could still be informative. I chose to retain the panel breaker.

Interviewer: What drove that specific choice over sending the fryer assembly instead?

Participant: A few things together—the visual severity from excavation, the utility inspector's preliminary read, and the fact that panel-related fires are something I've dealt with successfully identifying before, so I had a reasonably fast, defensible chain-of-custody process ready for that specific type of component. I did consider requesting a deadline extension to preserve both, but the insurer pushed back hard on timeline, and structurally, waiting risked losing both components to further collapse.

Interviewer: Is there a scenario where you'd have picked differently?

Participant: If the fryer had shown clearer independent ignition indicators—like burn patterns radiating from the appliance itself rather than the panel—I'd have sent that instead. It wasn't a coin flip, but it also wasn't airtight.

Interviewer: Last decision point—the final report classification under deadline.

Participant: With the clock running out and no new physical evidence expected, I had three options: issue a determinate finding, call it undetermined pending lab results, or issue a conditional finding naming both candidates with relative likelihood. I went with the conditional finding—electrical panel fault as the primary hypothesis, fryer malfunction as a documented secondary possibility—because the evidence genuinely supported more than one explanation and I didn't think forcing a single determinate answer was honest given what I actually had.

Interviewer: What alternative did you reject, and why?

Participant: I rejected calling it fully undetermined because that felt like it was underselling the pattern evidence and the inspector's preliminary read—there was more direction in the data than a blank "undetermined" would convey. I rejected a hard determinate call because the fryer possibility hadn't been eliminated, and NFPA 921 wants you to rule things out, not just pick a favorite.

Interviewer: Looking back, what single piece of missing evidence would have most changed your confidence?

Participant: Independent lab results on both components, honestly. Losing the fryer assembly to demolition is the piece I'd redo if I could—getting a deadline extension for preservation, even partial, would have mattered more than anything else.

Interviewer: How much of your final call would you attribute to prior cases versus the specifics of this one?

Participant: Mostly this case's own evidence. My experience shaped how fast I could process what I was seeing and gave me a working process for the panel component specifically, but the conditional finding came from what the debris and testimony actually showed, not from assuming this fire had to resemble something I'd seen before.

Interviewer: Anything you'd flag for someone reviewing this file cold?

Participant: Just that the ambiguity was real. Ventilation-limited burning, two plausible sources sitting close together, imperfect witness timing—none of that resolves cleanly, and I'd rather the file reflect that honestly than look more certain than the evidence actually was.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
  {
    "spec_version": "3.0",
    "scenario_id": "HE_Ambigious_2",
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
    },
    "hidden_validation_specification": {
      "hidden_spec_version": "1.0",
      "condition": "ambiguous_control",
      "exact_occurrence_manifest": [
        {
          "bias": "False memory",
          "occurrences": 0,
          "mechanism_constraint": "Control condition: no intended instance embedded. Paired biased scenario HE_Biased_2 specifies 1 occurrence for this bias."
        },
        {
          "bias": "Familiarity bias",
          "occurrences": 0,
          "mechanism_constraint": "Control condition: no intended instance embedded. Paired biased scenario HE_Biased_2 specifies 1 occurrence for this bias."
        }
      ],
      "target_bias_names": [
        "False memory",
        "Familiarity bias"
      ],
      "requested_occurrence_count_for_each_bias": [
        {
          "bias": "False memory",
          "requested_occurrences": 0
        },
        {
          "bias": "Familiarity bias",
          "requested_occurrences": 0
        }
      ],
      "planned_instance_ids": [],
      "intended_decision_points": [],
      "intended_mechanisms": [],
      "intended_strength": [],
      "paired_scenario_id": "HE_Biased_2",
      "counterfactual_variable": {
        "name": "not_applicable",
        "original_state": "N/A",
        "changed_state": "N/A",
        "variables_to_hold_constant": []
      },
      "scenario_id": "HE_Ambigious_2",
      "domain_id": "HE",
      "total_requested_occurrences": 0,
      "total_planned_occurrences": 0,
      "allocation_rule_used": "Not applicable: condition is ambiguous_control, which requires zero intended instances of all named target biases regardless of any occurrence counts supplied for the paired biased scenario. No allocation across decision points was performed since no instances are planned.",
      "control_zero_bias_requirement": true,
      "variables_to_hold_constant": [
        "Building type and layout (mixed-use café/apartment)",
        "Fire scenario structure and physical evidence types",
        "Four-decision-point sequence and sequencing logic",
        "Stakeholder cast (owner, adjuster, marshal, utility inspector, two witnesses)",
        "Time-pressure and resource-constraint framing",
        "Professional tone and difficulty level (subtle)",
        "Target word count (1,350 words, range 1,215-1,485)"
      ],
      "generation_warnings": [
        "The supplied exact-occurrence manifest lists False memory=1 and Familiarity bias=1, but the supplied condition for this scenario is ambiguous_control. Per CONDITION RULES, ambiguous_control requires zero intended instances of all named biases. The manifest values were therefore treated as the target set for the paired biased scenario (HE_Biased_2) only, and zero instances of False memory or Familiarity bias were planned or embedded in HE_Ambigious_2. This is not a reduction of a requested count within the biased condition; it is the correct application of the control-condition rule to a manifest that describes the paired experimental factor.",
        "Because zero occurrences are planned, occurrence_embedding_plan_internal, planned_instance_ids, intended_decision_points, intended_mechanisms, and intended_strength are intentionally empty arrays for this scenario."
      ]
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
        "segment_type": "initial_pattern_interpretation",
        "raw_interview_anchor": "Suppression crew told me they'd hit heavy smoke logging before they even got through the back door... ventilation-limited burning distorts your pattern reading... which made the visual read ambiguous from the start.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant interprets smoke logging and degraded fire patterns as sources of ambiguity. The control specification requires no False memory or Familiarity bias instance."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "objective_and_constraint_reasoning",
        "raw_interview_anchor": "Get a defensible origin and cause determination that would hold up for the insurer and, if it came to it, in a legal setting... The complication here was the clock...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states the investigative objective, methodology, and deadline constraint; no hidden bias is planned in this control."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "origin_zone_selection",
        "raw_interview_anchor": "First thing was scene assessment and photography before touching anything. Heaviest char and the collapse were both concentrated in that rear zone, so that's where excavation had to start...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The excavation starting area is selected from damage concentration and documentation practice, with a plausible non-bias explanation."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "excavation_sequence_choice",
        "raw_interview_anchor": "The breaker for that circuit showed heat damage that looked more severe on initial visual than the fryer wiring... Honestly, the visual severity tipped it, plus accessibility...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The panel-first excavation choice is justified by observed damage severity and safe accessibility, and the participant explicitly separates sequencing from causal conclusion."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "witness_evidence_weighting",
        "raw_interview_anchor": "I logged both accounts as provisional, flagged the discrepancy explicitly in my notes, and treated neither as more reliable than the other without physical corroboration.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant treats conflicting witness accounts as equally uncertain pending corroboration, matching the documented non-bias interpretation."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "timeline_update_rule",
        "raw_interview_anchor": "If either estimate had matched the dispatch window closely, I'd have leaned into that account more. Since neither did, I kept both as soft data points, not anchors.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant describes a conditional evidence-weighting rule rather than a biased timeline commitment."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "lab_retention_evidence_weighting",
        "raw_interview_anchor": "The utility company's field inspector had looked at the panel and said, informally, that it looked consistent with an internal fault... I weighed that against the fryer component's condition... I chose to retain the panel breaker.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The component-retention decision weighs preliminary testimony, component condition, budget, demolition timing, and the irreversible trade-off. The control specification identifies no hidden bias."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "lab_retention_rationale",
        "raw_interview_anchor": "A few things together—the visual severity from excavation, the utility inspector's preliminary read, and the fact that panel-related fires are something I've dealt with successfully identifying before...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Prior experience is presented as process familiarity and chain-of-custody readiness alongside case-specific evidence, not as a shortcut replacing evaluation of this case."
      },
      {
        "segment_id": "seg_009",
        "speaker": "Participant",
        "segment_type": "alternative_component_counterfactual",
        "raw_interview_anchor": "If the fryer had shown clearer independent ignition indicators... I'd have sent that instead. It wasn't a coin flip, but it also wasn't airtight.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant states what evidence would have changed the retention choice and acknowledges residual uncertainty."
      },
      {
        "segment_id": "seg_010",
        "speaker": "Participant",
        "segment_type": "final_classification_choice",
        "raw_interview_anchor": "I went with the conditional finding—electrical panel fault as the primary hypothesis, fryer malfunction as a documented secondary possibility—because the evidence genuinely supported more than one explanation...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The conditional report classification is explicitly based on unresolved competing explanations and an evidentiary-honesty judgment."
      },
      {
        "segment_id": "seg_011",
        "speaker": "Participant",
        "segment_type": "rejected_alternatives_reasoning",
        "raw_interview_anchor": "I rejected calling it fully undetermined because that felt like it was underselling the pattern evidence... I rejected a hard determinate call because the fryer possibility hadn't been eliminated...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explains why both alternative classifications were rejected using evidence sufficiency and NFPA 921-consistent elimination logic."
      },
      {
        "segment_id": "seg_012",
        "speaker": "Participant",
        "segment_type": "missing_evidence_confidence_assessment",
        "raw_interview_anchor": "Independent lab results on both components, honestly. Losing the fryer assembly to demolition is the piece I'd redo if I could...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant identifies missing evidence and a preservation decision that would have changed confidence; this is reflective uncertainty, not a hidden bias instance."
      },
      {
        "segment_id": "seg_013",
        "speaker": "Participant",
        "segment_type": "experience_vs_case_evidence_attribution",
        "raw_interview_anchor": "Mostly this case's own evidence. My experience shaped how fast I could process what I was seeing... but the conditional finding came from what the debris and testimony actually showed...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The participant explicitly distinguishes procedural expertise from inappropriate reliance on a similar past case."
      },
      {
        "segment_id": "seg_014",
        "speaker": "Participant",
        "segment_type": "overall_ambiguity_assessment",
        "raw_interview_anchor": "Just that the ambiguity was real. Ventilation-limited burning, two plausible sources sitting close together, imperfect witness timing...",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "The closing assessment reiterates legitimate evidentiary ambiguity and rejects overstating certainty; no hidden bias is planned."
      }
    ]
  }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
