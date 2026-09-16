You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": [
        "Interviewer",
        "Participant"
      ],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Analysis examined the fire investigator participant's reasoning about scene assessment, excavation order, witness statement weighting, sole forensic lab component retention, and final origin-and-cause classification. The participant demonstrated explicit uncertainty calibration, documented alternative hypotheses, and issued a conditional conclusion. No bias-specific mechanism was affirmatively identified."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Availability heuristic",
        "alternative_labels": [
          "availability bias"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Selection of panel breaker versus fryer assembly for sole forensic lab testing",
        "supporting_interview_quote": "panel-related fires are something I've dealt with successfully identifying before, so I had a reasonably fast, defensible chain-of-custody process ready for that specific type of component",
        "plausible_mechanism": "Ease of recalling prior panel-related fires may have increased the perceived support for the panel hypothesis and the procedural attractiveness of retaining the panel breaker, despite the fryer assembly remaining a plausible alternative.",
        "why_not_identified": "The participant also provided independent case-specific reasons for the panel-side focus, including visual heat severity, the utility inspector's preliminary read, debris accessibility, and resource constraints. He explicitly framed the final classification as conditional with the fryer as a documented secondary possibility. The interview does not affirmatively show that ease of recall distorted the reasoning outcome versus functioning as ordinary expert experience under resource constraints."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "The analysis relies on retrospective self-report, which may not perfectly capture real-time reasoning.",
      "No retrieved corpus passage specifically supported an identified occurrence of availability heuristic; the candidate label uses general cognitive-science knowledge.",
      "Resource, timeline, and demolition constraints are prominent in the transcript and were treated as non-bias structural factors absent a distinct cognitive mechanism.",
      "The retrieved corpus passages primarily address aviation, forensic pathology, usability testing, and fire evacuation contexts, limiting direct transfer to fire investigation."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Ambigious_2_Sonar_on",
  "interview_id": "HE_Ambigious_2",
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
