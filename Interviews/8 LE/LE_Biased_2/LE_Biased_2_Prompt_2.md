You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Biased_2",
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
