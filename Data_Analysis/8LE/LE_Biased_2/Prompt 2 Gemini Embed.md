You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I just want to confirm—this is a routine case-review interview, we're reconstructing your reasoning on a specific case, and it's fine to speak candidly since this isn't a disciplinary review. Sound good?

Participant: Sure, that's fine. I've done these debriefs before.

Interviewer: Great. Can you tell me a bit about your role and how this case landed on your desk?

Participant: I'm a latent print examiner, been doing casework about nine years. This one came through as a burglary submission—pry bar recovered from a residential break-in, latent lifted off the metal surface, plus a known print card for a suspect already booked. Standard comparison request, but they wanted it fast, ahead of a bail hearing.

Interviewer: Walk me through how the case actually came in—what did you know before you looked at the print itself?

Participant: The detective dropped the evidence off personally, which doesn't always happen. He mentioned, kind of in passing, that the suspect had already confessed and had two prior burglary convictions. I remember thinking, okay, that's helpful context, but my job is still to look at the ridges. I logged it in, noted his comments in the file, and got started. We don't have a strict blind-review setup here—some labs do, we don't—so it's normal for that kind of information to come with the evidence.

Interviewer: Did you consider handling the intake differently, given what he told you?

Participant: I thought about it for a second. I could've asked someone else to look at it fresh, or flagged it to my supervisor since he'd shared outcome information. But honestly, with the turnaround we had, that would've meant a delay we didn't have room for, and it's not like the confession changes what's on the pry bar. I proceeded normally.

Interviewer: Let's reconstruct the timeline. What was the physical state of the latent when you got into the analysis?

Participant: Partial print, fair amount of smudging, and there was a distorted region around the periphery—looked like it picked up texture from the tool grip itself, which throws off the ridge flow. The core area, though, was clean. Ten minutiae in that clear zone, no question about it.

Interviewer: And after you drafted your preliminary read?

Participant: I wrote it up, sent it to verification. Then the verifying examiner came back with a flag on that same peripheral area—didn't see it the way I did. That's when I had to reconcile things before the report went out.

Interviewer: Let's slow down on the comparison itself. When you got to that distorted peripheral region, what were you actually looking at, and how did you land on your read?

Participant: The ten minutiae in the clear zone were enough on their own, honestly—textbook sufficiency. The peripheral area was rougher, ridge flow was broken up by the distortion. I went back and forth on it. But when I lined it up against the known card, the flow direction seemed to pick back up in a way that fit the suspect's print. I remember thinking, given everything else pointing his way—he'd already admitted to it—this piece just confirmed what was already lining up. So I folded it into the individualization call as consistent rather than calling it indeterminate.

Interviewer: What alternatives were on the table at that point?

Participant: I could've treated that region as indeterminate and rested the conclusion purely on the ten clear minutiae—which honestly would've been sufficient by itself. Or I could've called for better imaging before committing either way. Those were both live options.

Interviewer: What would you say tipped you toward reading it as consistent rather than going with one of those?

Participant: The pattern looked plausible to me. I won't pretend the case context wasn't in my head at that point—it's hard to fully compartmentalize once you've heard something like that. But I also want to be clear, the ridge flow genuinely looked continuous to me in that section.

Interviewer: Moving to the verification step—what did you send over, and did you weigh other options?

Participant: I sent the full worksheet with my conclusion attached, along with the images. I could've sent just the images without my determination, let the verifier come in blind. We only had one other qualified examiner available that day, and with the clock running on the bail hearing, I went with the standard route—full packet, conclusion included.

Interviewer: Any hesitation there?

Participant: A little. Blind verification is theoretically cleaner, I know that. But it's not our default practice, and slowing things down to arrange it felt like more friction than the situation called for.

Interviewer: Let's talk about the discrepancy. The verifying examiner flagged that same peripheral region differently than you did. What went through your mind?

Participant: My first reaction was, okay, this is the distorted area, that's exactly the kind of spot where two examiners can read things differently. The ten core minutiae weren't in dispute—she agreed on those. So I looked at the discrepancy again and thought about what could explain it without it actually being a mismatch. Tool-surface texture causing pressure variance in that specific region made sense to me, and it's a documented thing that happens with textured surfaces like pry bars. I wrote that into the file as the explanation and kept the individualization conclusion standing.

Interviewer: Did you consider downgrading the conclusion instead?

Participant: I thought about calling it inconclusive until we could get a better lift or additional processing. That was on the table. But the ten minutiae were solid regardless, the deadline was same-day, and the distortion explanation accounted for what she was seeing without requiring me to throw out the whole determination.

Interviewer: What else, besides distortion, could have explained what she saw?

Participant: Could've genuinely been a non-matching area—maybe that region just doesn't belong to the same source. I didn't rule that out entirely, but it felt less likely to me once I had the distortion explanation in hand.

Interviewer: How confident were you in that peripheral read, if you had to put a number on it?

Participant: Maybe a six or seven out of ten on its own. But paired with the ten minutiae, I felt solid on the overall call.

Interviewer: Has this kind of distortion situation come up before in your casework?

Participant: Yeah, textured tool surfaces are a known headache. Usually if the core detail's strong, we don't let a rough edge area derail things.

Interviewer: Last few questions. If the detective had never mentioned the confession or the priors, do you think your read of that ambiguous region would've gone differently?

Participant: Possibly. I'd like to think I'd have called it the same way, but I can't say for certain the extra confidence wasn't doing some work there.

Interviewer: If the verifier's discrepancy had come up before you drafted your conclusion instead of after, would things have gone differently?

Participant: Maybe. Seeing it flagged first might've made me treat that region as indeterminate from the start rather than reconciling it after the fact.

Interviewer: What would you change if you had this case again with no deadline?

Participant: I'd probably request a fresh lift or enhanced imaging on that peripheral area before committing to anything, and maybe ask for a blind second look. Not because I think the outcome was wrong, but because that region deserved more room than we gave it that day.

Interviewer: Appreciate the candor. That's everything I need.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Biased_2",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Latent Fingerprint Examiner",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Confession Print: Weapon Latent in the Ridgeline Burglary",
    "scenario_summary_internal": "A latent print examiner at a state crime lab is asked to compare a partial, distorted latent print lifted from a pry bar recovered at a violent residential burglary against the known prints of a suspect already in custody. The submitting detective volunteers, unprompted, that the suspect has confessed and has two prior burglary convictions. The examiner must triage the case, perform the ACE-V comparison, decide whether/how to route the case for verification, and finalize the report after a verifier flags an unexplained discrepancy in one ridge area. The scenario is designed to allow one clean instance of contextual bias (case information coloring interpretation of ambiguous minutiae during the comparison decision) and one clean instance of coherence-based reasoning/rationalization (explaining away a verifier's discrepancy to preserve the prior conclusion rather than treating it as disconfirming evidence).",
    "occupational_realism": {
      "objective": "Determine whether the latent print recovered from the pry bar can be individualized to the suspect, excluded, or deemed inconclusive, and produce a defensible report before a bail hearing deadline.",
      "setting": "Regional crime laboratory latent print unit; two-person verification chain; 36-hour turnaround requested ahead of a bail hearing.",
      "constraints": [
        "Latent print is partial, with smudging and pressure distortion from a textured tool surface",
        "Lab protocol nominally supports linear ACE-V but does not enforce blind verification",
        "Detective has informally shared case-outcome information (confession, prior record) before analysis",
        "36-hour deadline before bail hearing creates time pressure",
        "Only one other qualified examiner is available same-day for verification",
        "Ten identifiable minutiae are present in the clearest region; a peripheral ridge area is ambiguous due to distortion"
      ],
      "stakeholders": [
        "Submitting detective",
        "Suspect (in custody)",
        "Verifying examiner",
        "Lab supervisor",
        "Prosecuting attorney awaiting report for bail hearing"
      ],
      "technical_terms_to_use": [
        "ACE-V (Analysis, Comparison, Evaluation, Verification)",
        "minutiae",
        "individualization",
        "inconclusive determination",
        "exclusion",
        "ridge distortion",
        "latent print",
        "known print card",
        "verification examiner",
        "sufficiency for identification"
      ],
      "technical_terms_to_avoid": [
        "contextual bias",
        "confirmation bias",
        "cognitive bias",
        "rationalization",
        "motivated reasoning",
        "coherence-based reasoning"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Case submitted with pry bar swab and latent print card",
          "Detective mentions suspect confessed and has two prior burglary convictions",
          "36-hour deadline before bail hearing",
          "Lab has no mandatory blind-review policy"
        ],
        "new_information_after_decision": [
          "Examiner logs the case and begins analysis under standard (non-blinded) conditions",
          "Print quality assessed as partial with a distorted peripheral region"
        ],
        "alternatives": [
          "Proceed with standard case intake, retaining the detective's contextual remarks",
          "Request that case-outcome information be withheld and ask a colleague to perform an independent blind analysis first",
          "Flag the case for supervisor review before analysis due to information exposure"
        ],
        "intended_action": "Examiner accepts the case as routed, notes the detective's comments in the case file, and begins the Analysis phase without requesting a blind reassignment."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Ten minutiae are clear and consistent in the well-preserved region of the latent",
          "One peripheral ridge area shows ambiguous, distorted detail that could be read multiple ways",
          "Known print card from suspect available for side-by-side comparison",
          "Detective's earlier remarks about confession and prior record are still in memory"
        ],
        "new_information_after_decision": [
          "Examiner reaches a preliminary individualization determination",
          "Comparison worksheet is drafted citing the ten clear minutiae plus an interpretation of the ambiguous region as 'consistent'"
        ],
        "alternatives": [
          "Interpret the ambiguous peripheral region as consistent with the known print, supporting individualization",
          "Treat the ambiguous region as indeterminate and base the conclusion solely on the ten unambiguous minutiae",
          "Classify the comparison as inconclusive pending better-quality imaging of the distorted area"
        ],
        "intended_action": "Examiner resolves the ambiguous peripheral detail in favor of a match, folding it into a preliminary individualization conclusion. [Planned Contextual Bias instance ctx_01]"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Preliminary individualization determination drafted",
          "Only one other qualified examiner is available same-day",
          "Lab protocol permits either blind or non-blind verification routing",
          "Deadline pressure ahead of the bail hearing"
        ],
        "new_information_after_decision": [
          "Case is routed to the available verifying examiner with the worksheet and conclusion visible",
          "Verifying examiner begins independent review same afternoon"
        ],
        "alternatives": [
          "Send the case for verification with the full worksheet, conclusion, and case notes attached",
          "Send the case for verification with only the latent and known images, withholding the preliminary conclusion",
          "Delay verification a day to seek a second available examiner for a fully blind review"
        ],
        "intended_action": "Examiner routes the case for standard (non-blind) verification, attaching the preliminary conclusion and worksheet to meet the deadline."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Verifying examiner agrees on the ten clear minutiae but flags the peripheral region as showing a possible discrepancy rather than a match",
          "Deadline for the bail hearing is same day",
          "Original examiner's report draft already states an individualization conclusion",
          "No new imaging or additional evidence has been obtained"
        ],
        "new_information_after_decision": [
          "Final report is submitted to the prosecuting attorney ahead of the bail hearing",
          "Discrepancy is documented in the file as 'explained by pressure distortion,' not as a basis for revising the conclusion"
        ],
        "alternatives": [
          "Treat the discrepancy as disconfirming and downgrade the conclusion to inconclusive pending further review",
          "Construct an explanation for why the discrepancy is compatible with the original individualization (e.g., attributing it to tool-surface distortion or pressure variance) and finalize the report as individualization",
          "Request additional latent processing or re-lifting before finalizing any conclusion"
        ],
        "intended_action": "Examiner incorporates the verifier's discrepancy into a distortion-based explanation that preserves the original individualization conclusion and finalizes the report on schedule. [Planned Coherence-based reasoning instance coh_01]"
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this case came to your bench.",
        "What was your objective when you opened the case file?"
      ],
      "timeline_reconstruction": [
        "What did you know about the case before you looked at the latent print itself?",
        "Describe the physical condition of the latent print when you first examined it.",
        "What happened after you drafted your preliminary conclusion?",
        "How did the verification step unfold?"
      ],
      "decision_point_probes": [
        "At intake, what options did you consider for how to proceed given what the detective told you, and why did you choose the one you did?",
        "When comparing the peripheral, distorted ridge area, what specific features did you rely on, and how did you decide it was consistent rather than indeterminate?",
        "When you routed the case for verification, what information did you include, and what alternatives did you weigh?",
        "When the verifying examiner flagged a discrepancy, what alternatives did you consider, and what led you to the explanation you settled on?"
      ],
      "cues": [
        "What in the print itself, versus what you'd been told, drove your read of the ambiguous region?",
        "What cue made the discrepancy seem explainable rather than concerning?"
      ],
      "information_sources": [
        "Which sources of information did you weigh most heavily at each stage: the print image, the known card, or case context?"
      ],
      "goals": [
        "What was your primary goal at each stage — accuracy, timeliness, or something else?"
      ],
      "alternatives": [
        "What other conclusions could a reasonable examiner have reached at the comparison stage?",
        "What else could explain the verifier's discrepancy besides distortion?"
      ],
      "decision_basis": [
        "What specifically tipped your final conclusion?"
      ],
      "prior_experience": [
        "Has distortion of this kind come up in past cases, and how did you handle it then?"
      ],
      "time_pressure": [
        "How did the bail hearing deadline affect your pace or thoroughness?"
      ],
      "uncertainty": [
        "How confident were you in the peripheral-region read, on a scale you'd use professionally?"
      ],
      "closing_hypotheticals": [
        "If the detective had never mentioned the confession or prior record, would your read of the ambiguous region have been different?",
        "If the verifier's discrepancy had appeared before your first draft rather than after, would your conclusion have changed?",
        "What would you do differently if you had this case again with no deadline?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "decision_point": 2,
        "mechanism": "Extraneous case information (confession, prior convictions) received before analysis shifts interpretation of genuinely ambiguous minutiae toward a conclusion consistent with guilt, rather than the ambiguous data being resolved on print evidence alone.",
        "affected_reasoning_operation": "Evaluation/interpretation of ambiguous perceptual evidence (peripheral ridge detail) during the Comparison/Evaluation phase of ACE-V",
        "evidence_available_at_time": [
          "Ten clear, unambiguous minutiae supporting comparison",
          "One peripheral ridge region with genuinely distorted, multi-interpretable detail",
          "Detective's unsolicited remarks about confession and prior convictions, retained in memory during analysis"
        ],
        "required_textual_manifestation": "The examiner's account of the comparison decision should reference, directly or through the reasoning offered, that the case context (confession/priors) made the ambiguous region feel consistent with a match, and should show the ambiguous detail being resolved toward inculpation without independent, print-based justification for that specific resolution.",
        "plausible_nonbias_interpretation": "An examiner could genuinely believe the ambiguous ridge detail is consistent with the known print based purely on pattern continuity, independent of any case information — this must remain a viable alternative reading unless the interview shows the case information actively entering the reasoning.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "contextual bias",
          "cognitive bias",
          "confirmation bias",
          "any explicit psychological labeling of the phenomenon"
        ]
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 4,
        "mechanism": "Upon receiving verifier feedback that contradicts the standing conclusion, the examiner constructs a post-hoc explanation (distortion/pressure variance) that renders the discrepancy compatible with the pre-existing individualization conclusion, rather than treating the discrepancy as evidence that should update the conclusion's probability.",
        "affected_reasoning_operation": "Evaluation of disconfirming evidence and belief-updating during final report reconciliation",
        "evidence_available_at_time": [
          "Verifying examiner's independent flag of a possible discrepancy in the peripheral region",
          "No new physical evidence, re-lift, or improved imaging obtained since the preliminary conclusion",
          "Existing report draft already stating individualization",
          "Same-day deadline for the bail hearing"
        ],
        "required_textual_manifestation": "The examiner's account of finalizing the report should show the discrepancy being folded into a narrative (e.g., attributed to tool-surface pressure distortion) that preserves the original conclusion, with the explanation arising after the conclusion was already fixed rather than being tested against alternative accounts (e.g., partial non-match) before being accepted.",
        "plausible_nonbias_interpretation": "Pressure distortion is a real, recognized phenomenon in latent print examination, so attributing a discrepancy to distortion could be a legitimate technical judgment rather than a rationalization — the interview must leave enough ambiguity that this remains a defensible alternative reading.",
        "strength": "moderate",
        "do_not_make_explicit": [
          "coherence-based reasoning",
          "rationalization",
          "motivated reasoning",
          "cognitive bias"
        ]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable to this biased-condition scenario; no paired control specified in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence versus absence of unsolicited case-outcome information (confession, prior convictions) at intake",
      "original_state": "Detective volunteers confession and prior-record information before analysis begins",
      "counterfactual_state": "Detective provides no outcome information; examiner receives only the physical evidence and case number (blind submission)",
      "variables_to_hold_constant": [
        "Print quality and distortion pattern",
        "Number and clarity of minutiae",
        "Deadline pressure",
        "Verification routing and staffing availability",
        "Verifier's discrepancy finding at phase 4"
      ],
      "expected_causal_difference": "Under the counterfactual (blind) condition, the ambiguous peripheral region would more plausibly be resolved as indeterminate or the case downgraded to inconclusive at decision point 2, removing the basis for the contextual-bias instance while leaving the coherence-based reasoning risk at decision point 4 structurally available but less likely to be triggered by an unresolved ambiguity.",
      "causal_test_question": "Does removing unsolicited case-outcome information at intake change how the examiner resolves the ambiguous peripheral ridge detail at the comparison stage?"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points are present and explicitly marked",
      "Confirm exactly one Contextual Bias instance is embedded, located at decision point 2, with no repetition elsewhere",
      "Confirm exactly one Coherence-based reasoning/Rationalisation instance is embedded, located at decision point 4, with no repetition elsewhere",
      "Confirm no bias names, definitions, or psychological labels appear in the public interview text",
      "Confirm each decision point offers at least two plausible alternatives",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm word count target of 1,350 (range 1,215–1,485) is achievable given four decision points and probe density",
      "Confirm consequences (bail hearing report submission) do not mechanically prove bias presence or absence",
      "Confirm plausible non-bias explanations remain viable for both planned instances"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Contextual Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as case-outcome information (confession/priors) influencing resolution of a genuinely ambiguous print feature during comparison, not as a general statement of belief in guilt."
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as a post-hoc explanation constructed to preserve a pre-existing conclusion after disconfirming verifier feedback, not as a routine technical judgment offered independent of the prior conclusion."
      }
    ],
    "target_bias_names": [
      "Contextual Bias",
      "Coherence-based reasoning or Rationalisation"
    ],
    "requested_occurrence_count_for_each_bias": [
      {
        "bias": "Contextual Bias",
        "requested_occurrences": 1
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "requested_occurrences": 1
      }
    ],
    "planned_instance_ids": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias"
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation"
      }
    ],
    "intended_decision_points": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "decision_point": 2
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 4
      }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "mechanism": "Extraneous confession/prior-record information received pre-analysis shifts interpretation of an ambiguous peripheral ridge region toward a match-consistent reading, absent independent print-based justification for that specific resolution.",
        "affected_reasoning_operation": "Evaluation/interpretation of ambiguous perceptual evidence during Comparison/Evaluation",
        "evidence_source": "Detective's unsolicited case-outcome remarks retained during analysis of the distorted peripheral ridge area",
        "distinctiveness_requirement": "Distinct from coh_01: occurs at the analysis/comparison stage on ambiguous perceptual data, before any conclusion has been challenged, and is driven by pre-analysis extraneous information rather than by defending an already-stated conclusion against disconfirming feedback."
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "After the verifying examiner flags a discrepancy, the examiner generates a distortion-based explanation that renders the discrepancy compatible with the already-fixed individualization conclusion, rather than treating it as evidence warranting downgrade.",
        "affected_reasoning_operation": "Evaluation of disconfirming evidence and belief updating during final report reconciliation",
        "evidence_source": "Verifying examiner's independent discrepancy flag on the peripheral ridge region, evaluated against the pre-existing draft conclusion",
        "distinctiveness_requirement": "Distinct from ctx_01: occurs post-conclusion, triggered by external disconfirming feedback from a second examiner, and operates through explanatory construction to preserve coherence with a prior commitment rather than through initial ambiguous-evidence interpretation."
      }
    ],
    "intended_strength": [
      {
        "instance_id": "ctx_01",
        "bias": "Contextual Bias",
        "strength": "moderate"
      },
      {
        "instance_id": "coh_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "strength": "moderate"
      }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence versus absence of unsolicited case-outcome information at intake",
      "original_state": "Detective volunteers confession and prior-record information before analysis begins",
      "changed_state": "Case submitted blind, with no outcome information disclosed to the examiner",
      "variables_to_hold_constant": [
        "Print quality and distortion pattern",
        "Number and clarity of minutiae",
        "Deadline pressure",
        "Verification routing and staffing availability",
        "Verifier's discrepancy finding at phase 4"
      ]
    },
    "scenario_id": "LE_Biased_2",
    "domain_id": "LE",
    "total_requested_occurrences": 2,
    "total_planned_occurrences": 2,
    "allocation_rule_used": "One occurrence per named bias, each assigned to the decision point offering the best mechanism fit and narrative realism: Contextual Bias at the initial ambiguous-comparison decision (phase 2), where pre-analysis case information most plausibly biases perceptual interpretation; Coherence-based reasoning/Rationalisation at the final report-reconciliation decision (phase 4), where disconfirming verifier feedback most plausibly triggers a conclusion-preserving explanation. Decision points were kept distinct (no shared decision point) to maximize independent identifiability and avoid overlap between mechanisms.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Print quality and distortion pattern",
      "Number and clarity of minutiae",
      "Deadline pressure",
      "Staffing and verification availability",
      "Verifier's discrepancy finding"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  null
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first evaluation of a latent print examiner's case reasoning for affirmative cognitive bias evidence. Retrieved passages were used to validate confirmation-bias and contextual-bias mechanisms."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 2
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "contextual bias",
        "expectation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall evidence in ways that confirm or support one's existing beliefs, expectations, or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of distorted peripheral region during latent print comparison",
      "decision_point_description": "Choosing whether to treat the distorted peripheral ridge detail as consistent, indeterminate, or to request better imaging.",
      "affected_reasoning_operation": "Evidence interpretation and weighting of ambiguous ridge detail",
      "bias_specific_mechanism": "Prior contextual expectations—specifically the suspect's confession and prior burglary convictions—made the participant more likely to interpret ambiguous peripheral ridge flow as consistent with the suspect and to classify it as confirmatory evidence rather than as indeterminate.",
      "manifestation_in_interview": "The participant explicitly stated that the suspect's confession and priors were in his mind, described the ambiguous peripheral region as confirming what was already lining up, and then folded that region into the individualization call as consistent rather than calling it indeterminate.",
      "effect_on_reasoning_or_decision": "The ambiguous peripheral detail was included in the individualization conclusion rather than being treated as indeterminate or referred for better imaging, despite the participant acknowledging the region was distorted.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The detective dropped the evidence off personally, which doesn't always happen. He mentioned, kind of in passing, that the suspect had already confessed and had two prior burglary convictions. I remember thinking, okay, that's helpful context, but my job is still to look at the ridges.",
          "evidence_explanation": "This establishes that the participant received outcome-related and prior-conviction context before the comparison, creating a prior expectation about the suspect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking, given everything else pointing his way—he'd already admitted to it—this piece just confirmed what was already lining up. So I folded it into the individualization call as consistent rather than calling it indeterminate.",
          "evidence_explanation": "This directly links the contextual expectation to the interpretation of ambiguous ridge detail and shows the participant classified the detail as confirmatory rather than indeterminate."
        }
      ],
      "correction_or_counterevidence": "The participant also had ten clear core minutiae that he believed were independently sufficient, and he later acknowledged that he could not be certain the contextual confidence was not doing work. The verifying examiner later disagreed about the peripheral region.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved forensic decision-making and confirmation-bias passages support the mechanism by which irrelevant case information and prior expectations bias evidence interpretation.",
      "corpus_evidence": [
        {
          "source_identifier": "Human expert performance in forensic decision making Seven different sources of bias.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Although they believe their conclusions are solely based on the bone fragment evidence, and are objective, in fact their exposure to irrelevant case information biases their work.",
          "mechanism_supported_by_source": "Exposure to irrelevant case information can bias forensic judgment even when examiners believe their conclusions are solely evidence-based.",
          "relevance_to_this_occurrence": "Supports the contextual expectation mechanism that influenced the participant's interpretation of the ambiguous peripheral region."
        },
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "These results closely replicate the findings from earlier experiments on confirmation bias (Wason, 1968) but with a situation more relevant to design.",
          "mechanism_supported_by_source": "Documents confirmation bias as a phenomenon in which prior expectations shape evidence interpretation.",
          "relevance_to_this_occurrence": "Supports labeling the participant's reasoning as confirmation bias rather than merely neutral contextual influence."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "belief perseverance",
        "motivated reasoning"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall evidence in ways that confirm or support one's existing beliefs, expectations, or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Reassessment after verifying examiner's discrepant finding",
      "decision_point_description": "Deciding whether to downgrade the conclusion, accept the verifier's concern, or retain the individualization by explaining the discrepancy.",
      "affected_reasoning_operation": "Evaluation of conflicting verification evidence and alternative explanations",
      "bias_specific_mechanism": "The participant's existing individualization conclusion motivated an explanatory search for an account that would preserve that conclusion, leading him to discount the possibility that the flagged peripheral region was a true non-matching area.",
      "manifestation_in_interview": "When the verifying examiner flagged the same peripheral region, the participant reported looking specifically for an explanation that would avoid a mismatch, then wrote a distortion-based explanation into the file and kept the individualization conclusion standing.",
      "effect_on_reasoning_or_decision": "The participant retained the individualization conclusion instead of downgrading to inconclusive or treating the verifier's concern as a substantive non-match.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "So I looked at the discrepancy again and thought about what could explain it without it actually being a mismatch.",
          "evidence_explanation": "This statement shows a confirmatory search strategy aimed at preserving the existing individualization conclusion rather than neutrally evaluating why the verifier disagreed."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Could've genuinely been a non-matching area—maybe that region just doesn't belong to the same source. I didn't rule that out entirely, but it felt less likely to me once I had the distortion explanation in hand.",
          "evidence_explanation": "This shows that the competing non-matching explanation was considered but discounted after a conclusion-consistent explanation became available, consistent with confirmation-biased differential weighting."
        }
      ],
      "correction_or_counterevidence": "The participant did explicitly consider downgrading to inconclusive, and he cited a documented distortion pattern from textured tool surfaces. The ten core minutiae were undisputed and independently sufficient, which provides a plausible non-bias basis for retaining the overall conclusion.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved confirmation-bias passages support the mechanism of selectively favoring a hypothesis-consistent explanation over a disconfirming alternative.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive confirmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "Confirmation bias can operate by shaping which evidence analysts select and prioritize when evaluating an existing hypothesis.",
          "relevance_to_this_occurrence": "Relevant to the participant's prioritization of a distortion explanation consistent with his existing conclusion over a non-matching alternative."
        },
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "These results closely replicate the findings from earlier experiments on confirmation bias (Wason, 1968) but with a situation more relevant to design.",
          "mechanism_supported_by_source": "Confirmation bias affects hypothesis testing and evidence interpretation.",
          "relevance_to_this_occurrence": "Supports the classification of the participant's mismatch-avoidance and alternative-discounting behavior as confirmation bias."
        }
      ]
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "status quo bias",
      "alternative_labels": [
        "default bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Choice of verification packaging under time pressure",
      "supporting_interview_quote": "I could've sent just the images without my determination, let the verifier come in blind. We only had one other qualified examiner available that day, and with the clock running on the bail hearing, I went with the standard route—full packet, conclusion included.",
      "plausible_mechanism": "Sticking with standard non-blind verification despite acknowledging a cleaner alternative, possibly because time pressure and institutional default reduced willingness to change practice.",
      "why_not_identified": "The decision is substantially explained by institutional standard practice and deadline pressure; the transcript does not clearly demonstrate a distinct cognitive distortion rather than an operational constraint."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "base rate expectation bias",
      "alternative_labels": [
        "experience-based expectation"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Interpretation of peripheral distortion based on prior textured-tool cases",
      "supporting_interview_quote": "Yeah, textured tool surfaces are a known headache. Usually if the core detail's strong, we don't let a rough edge area derail things.",
      "plausible_mechanism": "Previous case experience may create a base-rate expectation that rough edge areas can be discounted when core detail is strong, potentially reducing scrutiny of ambiguous regions.",
      "why_not_identified": "This may reflect a legitimate professional heuristic rather than a bias. The transcript does not show a distinct distortion separate from the already-identified confirmation-bias mechanism."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "Single interview transcript without independent examination of the latent print, case file, or verification worksheet.",
    "Retrieved corpus passages are fragmented and often lack full publication metadata; some classifications also rely on established general cognitive-science knowledge.",
    "The analysis is blind to experimental condition and cannot rule out that the participant was role-playing or reconstructing a hypothetical case."
  ]
}
</RAG_ANALYSIS_OUTPUT>

<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Biased_2_Gemini_on",
  "interview_id": "LE_Biased_2",
  "system_prompt_id": "Gemini",
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
