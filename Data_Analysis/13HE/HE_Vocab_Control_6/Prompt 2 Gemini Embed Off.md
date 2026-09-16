You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for talking with me. This is for a plan-review case study, it's voluntary, and you can skip anything you'd rather not go into. Can you tell me about your role and how the Meridian Tower conversion came to you?

Participant: Happy to. I'm a plan review official in the building and fire division—permitting and life-safety sign-off, mainly. Meridian Tower was an adaptive reuse, a 22-story former office tower going to mixed-use residential and retail. The complication was the atrium, a large central void running most of the building height. It didn't fit the prescriptive smoke control provisions in our code, so the design team came in with a performance-based alternative instead.

Interviewer: What was your objective going in?

Participant: Get the review done correctly within our statutory window. We had a 30-day clock, the department was short-staffed that quarter, and there was pressure from the city to keep housing projects moving. All of that mattered, but the core job was still making sure the building would actually perform the way the code intends if there's a fire.

Interviewer: Walk me through what happened, from the start.

Participant: The engineer of record was Halkirk & Vance, a regional firm with a lot of atrium experience—dozens of approved performance-based designs, and a neighboring jurisdiction had approved something similar from them the year before. They submitted a CFD-based smoke control model in place of the prescriptive system. We didn't have budget for an outside peer review that cycle, so I went through the documentation myself. One assumption stood out—how the model handled stack effect if a door were left partially open during an event—and I wasn't satisfied it was addressed clearly enough, so I sent that back to them in writing before finalizing anything. After that we moved into commissioning planning, where we had to choose between two verification protocols. Construction got underway, and about six weeks in, our inspector flagged fire-rated door deficiencies on three floors. Later, as we were approaching occupancy, the developer requested an early certificate before full integration testing was complete. Near the end of construction there was a small trash-chute fire—sprinklers handled it, no injuries—which led us to take another look at the atrium system, though it turned out to be a separate issue.

Interviewer: Let's put the order together more precisely. What did you know before the first major decision, and what came in after?

Participant: Before approving the design, I had the CFD report, the firm's general track record, and the neighboring jurisdiction's approval. After I sent back the question on the stack-effect assumption, they responded with additional documentation, and I approved based on that exchange. Then came the commissioning protocol decision. After that, construction started, and the door issue came up. The occupancy request was near the end, and the trash-chute fire happened after that decision was made, not before.

Interviewer: Let's take the first decision—approving the performance-based design. What carried the most weight?

Participant: The firm's documentation carried real weight, and so did the neighboring jurisdiction's approval—that told me the overall modeling approach had held up under scrutiny elsewhere. But I still went through the assumptions myself, and the stack-effect piece wasn't fully addressed for our specific geometry. I asked for a written clarification on that point specifically rather than taking the package at face value or sending the whole thing out for a full outside review, which would have added about three weeks.

Interviewer: Was a full peer review ever seriously on the table?

Participant: It was one of the options, yes. I decided a targeted clarification on the one assumption that mattered most for egress got me most of the benefit without the full delay.

Interviewer: Second decision—the commissioning protocol. What were you weighing?

Participant: Two options. Option A was a newer risk-informed test, better matched to this atrium's geometry according to the guidance, but its thresholds were only partly and qualitatively defined. Option B was the older prescriptive smoke test—clean binary pass-fail, but less sensitive to some of the failure modes this atrium could actually have.

Interviewer: Which did you choose, and why?

Participant: Option A, but not without addressing the enforcement problem. I built in defined interim checkpoints and documentation standards so the qualitative thresholds would still be auditable if anyone questioned the sign-off later. I didn't want to trade technical fit for administrative convenience, but I also didn't want a protocol I couldn't defend.

Interviewer: Third decision—the door deficiencies. What did you see, and how did you respond?

Participant: The inspector found bad fire-door installations on floors 8, 11, and 14. My first instinct was to wonder if we had a specific crew problem. But crews were rotated randomly across the building, and it was three deficiencies out of roughly 150 doors checked at that point—which is within the range you'd expect from ordinary variation on a project this size. So I kept the original random-sample inspection plan across all floors rather than concentrating just on those three.

Interviewer: What did the rest of the inspection show?

Participant: The building-wide sample came back with a defect rate consistent with what we'd already seen—nothing suggesting those three floors were actually worse than the rest.

Interviewer: Fourth decision—the temporary occupancy request. What was your basis?

Participant: The developer had a financing deadline, and full integration testing on the alarm and smoke systems was still about three weeks out. The contractor had a good record on other city jobs, and a colleague mentioned a nearby building that had gotten early partial occupancy without incident. But our own five-year data show something like a 15 percent rework rate on these atrium integration tests citywide, and that number is specific to the exact system we hadn't tested yet. So I granted occupancy only for the floors that didn't depend on the untested atrium system, and held back the rest until testing was done.

Interviewer: What would have made you grant broader occupancy at that point?

Participant: A completed, passed integration test, basically. Nothing short of that for the floors relying on that system.

Interviewer: How much uncertainty did you feel across these decisions?

Participant: Fairly consistent, honestly. The door situation had some ambiguity until the wider sample came back. The occupancy call had the most riding on it, which is part of why I drew the line where I did rather than treating the contractor's general history as settling the question.

Interviewer: Looking back now, after the trash-chute fire, how do you view the original design approval?

Participant: It held up fine, as it turned out—the fire was in the chute enclosure, unrelated to the atrium system. If anything, it reinforced that the clarification I'd asked for on the stack-effect assumption was worth pursuing at the time, though I wouldn't say the fire proved anything either way about that decision.

Interviewer: If you had to make the temporary occupancy call again with the same information, would you do anything differently?

Participant: No, I think I'd draw the same line. The rework rate was too specific to ignore just because of a good general track record elsewhere.

Interviewer: Last question—what would you tell a newer reviewer facing a similar submittal?

Participant: Don't let a strong firm's name stand in for checking the one assumption that actually matters for your building, and don't let a small pattern in early data override what a proper sample tells you.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "HE_Vocab_Control_6",
  "domain_id": "HE",
  "domain": "High-risk Engineering and Fire Engineering",
  "role": "Building/Fire Code Official (Plan Review and Permitting)",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The Meridian Tower Atrium Retrofit: Balanced Plan Review and Occupancy Decision",
    "scenario_summary_internal": "A municipal Building/Fire Code Official handles the adaptive-reuse permit for Meridian Tower, a 22-story former office building being converted to mixed-use residential/commercial with a large central atrium. The atrium geometry cannot meet prescriptive smoke-control provisions, so the design team submits a performance-based alternative. The official evaluates the alternative design on its technical merits, selects a commissioning/verification protocol by weighing fit against defensibility, responds to a small cluster of fire-door deficiencies discovered during construction with appropriately calibrated statistical reasoning, and decides whether to grant temporary occupancy before full fire-alarm/smoke-control integration testing is complete by explicitly weighing case-specific risk data. A minor trash-chute fire late in construction (contained by sprinklers, no injuries) prompts a retrospective review that remains evidentially grounded in what was actually known beforehand.",
    "occupational_realism": {
      "objective": "Ensure the Meridian Tower conversion meets life-safety code requirements for smoke control, fire-rated separations, and alarm integration while managing statutory review deadlines and the developer's financing-driven schedule.",
      "setting": "Municipal Building & Fire Department, plan review and permitting division; site visits to a 22-story adaptive-reuse construction project during active build-out.",
      "constraints": [
        "30-day statutory plan review deadline",
        "Department staffing shortage limiting time for independent technical review",
        "No budget authorized for third-party peer review on this project",
        "Developer financing deadline tied to a move-in date",
        "City council pressure to expedite housing supply projects",
        "Ongoing active construction limiting full-building inspection access"
      ],
      "stakeholders": [
        "Plan review official (interviewee)",
        "Fire protection engineer of record (Halkirk & Vance engineering firm)",
        "General contractor",
        "Developer/project owner",
        "Building official supervisor",
        "Construction inspector colleague",
        "Future building occupants"
      ],
      "technical_terms_to_use": [
        "performance-based design",
        "alternative means and methods",
        "smoke control system",
        "CFD modeling",
        "commissioning/acceptance testing",
        "fire-rated door assembly",
        "integration testing",
        "equivalent level of safety",
        "temporary certificate of occupancy"
      ],
      "technical_terms_to_avoid": [
        "clustering illusion",
        "base-rate neglect",
        "optimism bias",
        "ambiguity effect",
        "authority bias",
        "hindsight bias",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Halkirk & Vance submitted a CFD-based performance design for the atrium smoke control system because the geometry does not meet prescriptive NFPA 92/IBC atrium provisions",
          "Halkirk & Vance is a nationally recognized regional fire-engineering firm with dozens of previously approved performance-based designs",
          "A neighboring jurisdiction approved a similar atrium design from the same firm the prior year",
          "No budget was authorized for an independent third-party peer review of the CFD assumptions"
        ],
        "new_information_after_decision": [
          "The official identified a specific input assumption (stack-effect behavior under partial door-open conditions) that warranted direct clarification from the design team before conditions were finalized"
        ],
        "alternatives": [
          "Approve the alternative design based on the firm's documentation with standard conditions",
          "Request a targeted written clarification of the specific stack-effect assumption from the design team before approval, without commissioning a full external peer review",
          "Require a full independent third-party peer review of the CFD assumptions before approval, adding roughly three weeks to the review"
        ],
        "intended_action": "Approve the performance-based design only after requesting and receiving a written clarification of the specific CFD assumption most relevant to occupant egress, balancing review-time constraints against a targeted technical check rather than either blanket deference or a full external review."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two candidate commissioning/acceptance test protocols were submitted for the smoke control system",
          "Option A is a newer risk-informed acceptance protocol whose pass/fail thresholds are only partially and qualitatively defined in current guidance",
          "Option B is a traditional prescriptive visual smoke test with clearly defined binary pass/fail criteria but known lower sensitivity to certain atrium failure modes",
          "Available technical guidance suggests Option A is better matched to this atrium's specific risk profile"
        ],
        "new_information_after_decision": [
          "The permit conditions specify Option A as the primary commissioning protocol, supplemented with defined interim checkpoints to make the qualitative thresholds auditable"
        ],
        "alternatives": [
          "Require Option A alone, accepting the administrative burden of qualitative thresholds",
          "Require Option B alone, accepting weaker sensitivity to relevant failure modes",
          "Require Option A supplemented with defined interim checkpoints and documentation standards to make its criteria auditable"
        ],
        "intended_action": "Select Option A as the primary protocol because it better matches the atrium's risk profile, while adding documented interim checkpoints so the qualitative thresholds remain defensible for enforcement purposes."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Inspection reports show fire-rated door deficiencies on floors 8, 11, and 14 out of 22",
          "Floor assignments to installation crews were rotated randomly across the building, not fixed by floor",
          "3 deficiencies were found among roughly 150 doors inspected so far, a rate consistent with typical random defect rates on comparable projects",
          "The three flagged floors are non-contiguous"
        ],
        "new_information_after_decision": [
          "A building-wide random sample inspection is completed and finds a defect rate consistent with the original three floors, indicating no floor-specific concentration"
        ],
        "alternatives": [
          "Treat the three-floor pattern as evidence of a localized crew or workmanship problem and concentrate follow-up inspection there",
          "Recognize the sample size is too small to indicate a systemic pattern and continue the originally planned random-sample inspection across all floors"
        ],
        "intended_action": "Continue the originally planned random-sample inspection across all floors, explicitly noting that three deficiencies among 150 doors with randomly rotated crews is within the range expected from ordinary variation and does not by itself indicate a localized cause."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Full fire-alarm and smoke-control integration testing is scheduled in three weeks",
          "The developer requests a temporary certificate of occupancy for completed lower floors, citing a financing deadline",
          "This general contractor's overall track record on other city projects has been favorable",
          "The department's own five-year inspection data show a roughly 15% integration-test failure/rework rate for atrium smoke-control systems citywide",
          "A colleague mentions that a nearby, similar building recently received early partial occupancy without incident"
        ],
        "new_information_after_decision": [
          "A minor trash-chute fire occurs during the remaining construction period; sprinklers contain it, no injuries occur, and the smoke migration pattern is later found consistent with the trash-chute enclosure rather than a defect in the atrium system"
        ],
        "alternatives": [
          "Grant temporary occupancy for completed lower floors with monitoring conditions, pending full integration testing",
          "Deny temporary occupancy and require full integration testing to be completed and passed before any occupancy is granted",
          "Grant a narrowly conditioned occupancy limited to floors served by fire-rated separations independent of the untested atrium smoke system"
        ],
        "intended_action": "Grant a narrowly conditioned temporary occupancy limited to floors that do not rely on the untested atrium smoke system, explicitly citing the citywide 15% integration-test rework rate as the reason for withholding broader occupancy despite the contractor's favorable general record and the nearby building's outcome."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through your role in the Meridian Tower conversion project and what made it nonroutine?",
        "What was your primary objective when you first received the atrium smoke control alternative-compliance submittal?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you know at that point?",
        "What new information came in after each major decision you made?",
        "Were there moments where the sequence of events surprised you?"
      ],
      "decision_point_probes": [
        "What specific evidence or documents did you rely on when approving the atrium smoke control design, and what made you ask for further clarification?",
        "What alternatives did you consider before choosing the commissioning protocol, and what tipped the balance?",
        "When the door deficiencies came in on floors 8, 11, and 14, how did you decide whether that pattern was meaningful?",
        "What made you confident about the scope of the temporary occupancy decision, and what information shaped where you drew the line?",
        "How much time pressure did you feel at each of these points, and how did that affect what you checked versus what you took on trust?",
        "What did you consider the biggest source of uncertainty at each decision, and how did you resolve it?"
      ],
      "closing_hypotheticals": [
        "If the third-party peer review budget had been available from the start, would your initial approval have gone differently?",
        "Looking back at your original approval of the atrium design, how do you now see the decision given what happened with the trash-chute fire?",
        "If you had to make the temporary occupancy call again with the same information you had then, what would you do differently, if anything?",
        "What would you tell a newer plan reviewer to watch for in a similar performance-based design submittal?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "HE_Biased_6",
      "features_to_match": [
        "Domain vocabulary (performance-based design, CFD modeling, commissioning/acceptance testing, fire-rated door assembly, integration testing, temporary certificate of occupancy)",
        "Occupational setting, stakeholders, and role of the interviewee",
        "Four-decision-point structure and topical sequence (design approval, commissioning protocol, door-deficiency response, temporary occupancy)",
        "Difficulty level and narrative complexity",
        "Emotional tone (measured, professional, moderate pressure)",
        "Overall word count and dialogue format"
      ],
      "features_to_remove_or_change": [
        "Remove reliance on firm reputation as a substitute for technical verification at Decision Point 1",
        "Remove selection of a protocol primarily for criterion clarity over technical fit at Decision Point 2",
        "Remove inference of a systemic localized cause from a small random sample at Decision Point 3",
        "Remove reliance on general contractor reputation as the basis for confidence in an untested system at Decision Point 4",
        "Remove discounting of the citywide base rate in favor of an anecdote at Decision Point 4",
        "Remove retrospective claims of foreseeability inconsistent with what was actually known at the time of the original decision"
      ],
      "ambiguity_boundary": "Genuine technical trade-offs (e.g., qualitative thresholds versus binary criteria, small-sample inspection data, competing schedule pressures) may remain visible and undetermined in places, but every decision must be accompanied by an evidence-consistent, non-biased justification, and no decision may rely on the mechanisms described in features_to_remove_or_change."
    },
    "counterfactual_specification": {
      "causal_variable": "engineering_firm_reputation (autoselected candidate retained for consistency with the paired biased scenario; not applied in this vocabulary_control generation)",
      "original_state": "Design submitted and stamped by a nationally recognized, previously-approved fire protection engineering firm (Halkirk & Vance)",
      "counterfactual_state": "Not applicable in this generation run; condition is vocabulary_control, not counterfactual",
      "variables_to_hold_constant": [
        "Atrium geometry and code non-conformance",
        "Statutory review timeline and staffing constraints",
        "Developer schedule pressure",
        "All four decision points and their topical sequence"
      ],
      "expected_causal_difference": "Not applicable: no causal manipulation is performed in this control condition.",
      "causal_test_question": "Not applicable in this generation run."
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two plausible alternatives.",
      "Zero intended instances of all six named biases are embedded, consistent with the vocabulary_control condition rule overriding the input manifest's occurrence counts.",
      "Each decision point includes an evidence-consistent, non-biased justification that mirrors the topical structure of HE_Biased_6 without reusing its biased mechanisms.",
      "Domain vocabulary, actors, setting, difficulty, and decision-count match HE_Biased_6.",
      "Bias names, definitions, and psychological terminology are excluded from all public-facing timeline, probe, and dialogue content.",
      "Word count target of 1,350 (range 1,215-1,485) is achievable given 4 decision points with moderate-depth probes without repetitive exposition.",
      "Consequences (minor contained fire, no injuries) do not mechanically confirm or deny whether any specific decision was correct or incorrect.",
      "No accidental instance of Clustering illusion, Probability neglect/Base-Rate Neglect, Optimism bias, Ambiguity effect, Authority Bias, or Hindsight bias is introduced anywhere in the timeline or probes."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      {
        "bias": "Clustering illusion",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Probability neglect or Base-Rate Neglect",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Optimism bias",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Ambiguity effect",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Authority Bias",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      },
      {
        "bias": "Hindsight bias",
        "occurrences": 0,
        "mechanism_constraint": "Control condition requires zero intended instances; input manifest occurrence count of 1 is overridden per vocabulary_control condition rules."
      }
    ],
    "target_bias_names": [
      "Clustering illusion",
      "Probability neglect or Base-Rate Neglect",
      "Optimism bias",
      "Ambiguity effect",
      "Authority Bias",
      "Hindsight bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Clustering illusion", "requested_occurrences": 0 },
      { "bias": "Probability neglect or Base-Rate Neglect", "requested_occurrences": 0 },
      { "bias": "Optimism bias", "requested_occurrences": 0 },
      { "bias": "Ambiguity effect", "requested_occurrences": 0 },
      { "bias": "Authority Bias", "requested_occurrences": 0 },
      { "bias": "Hindsight bias", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "HE_Biased_6",
    "counterfactual_variable": {
      "name": "engineering_firm_reputation",
      "original_state": "Nationally recognized, previously-approved fire protection engineering firm (Halkirk & Vance)",
      "changed_state": "Not applicable in this generation run; condition is vocabulary_control, not counterfactual",
      "variables_to_hold_constant": [
        "Atrium geometry and code non-conformance",
        "Statutory review timeline and staffing constraints",
        "Developer schedule pressure",
        "All four decision points and their topical sequence"
      ]
    },
    "scenario_id": "HE_Vocab_Control_6",
    "domain_id": "HE",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable: vocabulary_control condition mandates zero intended bias instances for every bias in the paired target set, overriding the occurrence counts listed in the input manifest. Decision-point topics were matched one-to-one against HE_Biased_6's four decision points to preserve structure while each was rewritten with an evidence-consistent, non-biased justification.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical terminology",
      "Occupational setting and stakeholders",
      "Four-decision-point structure and topical sequence",
      "Difficulty level and narrative complexity",
      "Emotional tone and overall word count",
      "Dialogue format (Interviewer/Participant turns)"
    ],
    "generation_warnings": [
      "The input occurrence manifest listed 1 occurrence for each of the six named biases; per the vocabulary_control condition rule, all occurrence counts were overridden to 0 in this generation, and the manifest above records that override explicitly rather than silently omitting the originally supplied counts."
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
          "segment_type": "objective_and_priority_rationale",
          "raw_interview_anchor": "Get the review done correctly within our statutory window... the core job was still making sure the building would actually perform the way the code intends if there's a fire.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant explicitly balances deadline and staffing pressure against the life-safety objective without a hidden bias mechanism."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "design_approval_evidence_weighting",
          "raw_interview_anchor": "The firm's documentation carried real weight, and so did the neighboring jurisdiction's approval—that told me the overall modeling approach had held up under scrutiny elsewhere.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Reputation and prior approval are considered as evidence, but the control specification requires independent checking and contains no manifested authority-based distortion."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "targeted_clarification_and_review_scope",
          "raw_interview_anchor": "I asked for a written clarification on that point specifically rather than taking the package at face value or sending the whole thing out for a full outside review, which would have added about three weeks.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant identifies a project-specific assumption, requests clarification, and chooses a proportionate review scope."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "commissioning_protocol_tradeoff",
          "raw_interview_anchor": "Option A was a newer risk-informed test, better matched to this atrium's geometry... Option B was the older prescriptive smoke test—clean binary pass-fail, but less sensitive to some of the failure modes this atrium could actually have.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant states the technical-fit versus administrative-clarity tradeoff without selecting an option through the hidden ambiguity mechanism."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "commissioning_protocol_choice_rationale",
          "raw_interview_anchor": "I built in defined interim checkpoints and documentation standards so the qualitative thresholds would still be auditable... I didn't want to trade technical fit for administrative convenience.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Option A is selected for technical fit and supplemented with controls that address enforceability."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "initial_door_deficiency_interpretation",
          "raw_interview_anchor": "My first instinct was to wonder if we had a specific crew problem.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "An initial possibility is considered but is not adopted as a causal conclusion; the control specification explicitly excludes an accidental manifested clustering instance."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "door_sampling_plan_rationale",
          "raw_interview_anchor": "Crews were rotated randomly across the building, and it was three deficiencies out of roughly 150 doors checked... So I kept the original random-sample inspection plan across all floors rather than concentrating just on those three.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant uses random assignment and sample size to reject a localized-cause inference and retain the planned sample."
        },
        {
          "segment_id": "seg_008",
          "speaker": "Participant",
          "segment_type": "follow_up_sample_interpretation",
          "raw_interview_anchor": "The building-wide sample came back with a defect rate consistent with what we'd already seen—nothing suggesting those three floors were actually worse than the rest.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "Later sample evidence is interpreted as confirming the absence of floor-specific concentration; it is not used as hindsight to justify the original decision."
        },
        {
          "segment_id": "seg_009",
          "speaker": "Participant",
          "segment_type": "occupancy_evidence_comparison",
          "raw_interview_anchor": "The contractor had a good record on other city jobs, and a colleague mentioned a nearby building... But our own five-year data show something like a 15 percent rework rate on these atrium integration tests citywide.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "General reputation and anecdote are weighed against system-specific base-rate data, with no manifested optimism or probability-neglect mechanism."
        },
        {
          "segment_id": "seg_010",
          "speaker": "Participant",
          "segment_type": "temporary_occupancy_scope_decision",
          "raw_interview_anchor": "I granted occupancy only for the floors that didn't depend on the untested atrium system, and held back the rest until testing was done.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant makes a narrowly conditioned occupancy decision tied to the untested system and specific risk evidence."
        },
        {
          "segment_id": "seg_011",
          "speaker": "Participant",
          "segment_type": "post_event_retrospective_reasoning",
          "raw_interview_anchor": "The fire was in the chute enclosure, unrelated to the atrium system... I wouldn't say the fire proved anything either way about that decision.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant separates the later fire from the earlier atrium decision and explicitly avoids treating the outcome as proof."
        },
        {
          "segment_id": "seg_012",
          "speaker": "Participant",
          "segment_type": "occupancy_counterfactual_consistency",
          "raw_interview_anchor": "The rework rate was too specific to ignore just because of a good general track record elsewhere.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The participant's counterfactual answer reaffirms the same evidence-specific reasoning and does not claim the later outcome was foreseeable."
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
      "analysis_scope_note": "No retrieved scientific-passage context was supplied in the prompt. The evaluation therefore relies on the transcript as the sole factual authority and applies established cognitive-science knowledge only, with corpus support explicitly unavailable."
    },
    "identified_bias_summary": [],
    "identified_occurrences": [],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "Authority bias",
        "alternative_labels": ["Halo effect"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Approving the performance-based atrium smoke control design",
        "supporting_interview_quote": "The firm's documentation carried real weight, and so did the neighboring jurisdiction's approval—that told me the overall modeling approach had held up under scrutiny elsewhere.",
        "plausible_mechanism": "The firm's prior approvals and regional reputation could act as a credibility heuristic, reducing the depth of independent scrutiny.",
        "why_not_identified": "The participant explicitly went through the assumptions himself, singled out a stack-effect issue specific to this building geometry, and required written clarification. The transcript does not show that the firm's reputation or prior approval materially distorted the final approval decision."
      },
      {
        "candidate_id": "cand_002",
        "classification_status": "candidate",
        "proposed_bias_label": "Clustering illusion",
        "alternative_labels": ["Illusory correlation"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Responding to fire-door deficiencies on floors 8, 11, and 14",
        "supporting_interview_quote": "My first instinct was to wonder if we had a specific crew problem. But crews were rotated randomly across the building, and it was three deficiencies out of roughly 150 doors checked at that point—which is within the range you'd expect from ordinary variation on a project this size.",
        "plausible_mechanism": "Three deficiency findings clustered on specific floors could be perceived as a non-random pattern, prompting an inference about a specific crew or localized cause.",
        "why_not_identified": "The participant explicitly considered random crew rotation, the small numerator relative to the sample, and expected ordinary variation before deciding. The initial impulse was corrected before it influenced the inspection plan or final interpretation."
      },
      {
        "candidate_id": "cand_003",
        "classification_status": "candidate",
        "proposed_bias_label": "Availability heuristic",
        "alternative_labels": ["Salience bias"],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Temporary occupancy request before full integration testing",
        "supporting_interview_quote": "The contractor had a good record on other city jobs, and a colleague mentioned a nearby building that had gotten early partial occupancy without incident. But our own five-year data show something like a 15 percent rework rate on these atrium integration tests citywide, and that number is specific to the exact system we hadn't tested yet.",
        "plausible_mechanism": "A colleague's anecdote about nearby early occupancy without incident could make a successful outcome more mentally available, potentially influencing the occupancy decision.",
        "why_not_identified": "The participant did not rely on the anecdote or the contractor's general record; instead, the decision was anchored to agency-specific rework data and restricted to floors not dependent on the untested atrium system. No distorting effect is shown."
      }
    ],
    "no_supported_biases_found": true,
    "limitations": [
      "No retrieved corpus passages were supplied, so corpus-backed diagnostic criteria could not be applied.",
      "The transcript is retrospective self-report, which may underrepresent automatic or implicit influences that were not verbalized.",
      "The analysis does not consider experimental conditions, benchmark hypotheses, or counterfactual interview arms."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "HE_Vocab_Control_6_Gemini_off",
  "interview_id": "HE_Vocab_Control_6",
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
