You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Biased_4",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "DNA Forensic Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Windowsill Swab: Mixture Interpretation in a Residential Burglary-Assault Case",
    "scenario_summary_internal": "A forensic DNA analyst at a regional crime laboratory processes a low-template, mixed blood/touch-DNA sample recovered from a broken windowsill in a burglary that escalated to an assault on the homeowner. Before analysis, the analyst is told by the submitting detective that a named suspect with a prior burglary conviction was found nearby and 'is almost certainly good for it.' Across four decision points—case intake and parameter-setting, electropherogram allele calling near the stochastic threshold, mixture deconvolution against elimination profiles, and final statistical reporting/peer sign-off—the analyst must decide how to weigh ambiguous, low-copy-number genetic evidence. The case is designed so that the suspect's profile is a plausible but not conclusive contributor, and equally plausible alternative explanations (an ex-boyfriend of the victim who had visited days earlier, a delivery worker) are not pursued with the same rigor applied to ruling in the suspect.",
    "occupational_realism": {
      "objective": "Determine, from a low-template mixed DNA sample recovered at a burglary/assault scene, whether the named suspect can be included as a contributor with a statistically supportable likelihood ratio, and produce a technically defensible report.",
      "setting": "Regional public forensic DNA laboratory; casework bench with capillary electrophoresis output, elimination database access, and a two-analyst technical review workflow.",
      "constraints": [
        "Low template quantity (under 100 pg) producing stochastic peak height variation",
        "24-hour turnaround pressure from the district attorney's office ahead of a bail hearing",
        "Only one elimination sample (the homeowner) initially available; two other potential contributors not yet swabbed",
        "Lab validation protocol requires a stochastic threshold and peak height ratio check before allele calls are finalized",
        "Backlog means only one technical reviewer available that week, who is also the analyst's direct supervisor"
      ],
      "stakeholders": [
        "Submitting detective",
        "Lab technical reviewer/supervisor",
        "District attorney's office",
        "Named suspect",
        "Victim/homeowner",
        "Defense counsel (post-hoc)"
      ],
      "technical_terms_to_use": [
        "electropherogram",
        "stochastic threshold",
        "peak height ratio",
        "minor contributor",
        "stutter peak",
        "mixture deconvolution",
        "likelihood ratio",
        "elimination sample",
        "low-template DNA",
        "allele call",
        "technical review",
        "heterozygote peak imbalance",
        "CODIS"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "contextual bias",
        "feature positive effect",
        "coherence-based reasoning",
        "rationalization",
        "cognitive bias",
        "motivated reasoning",
        "asymmetrical skepticism"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Case submission form lists a named suspect with a prior burglary conviction",
          "Detective's cover note states the suspect 'is almost certainly good for it' and was found two blocks away",
          "Sample is a low-template swab from a broken windowsill, quantity under 100 pg",
          "Lab protocol requires the analyst to set stochastic threshold and amplification parameters before typing"
        ],
        "new_information_after_decision": [
          "Amplification yields a partial, low-template profile with several peaks near the stochastic threshold",
          "Supervisor later notes the case file review sheet already had the suspect's name filled into the 'expected contributor' field"
        ],
        "alternatives": [
          "Set parameters and proceed to typing without reviewing detective's suspicion narrative, treating the sample as an unknown-source mixture",
          "Review the detective's note first and mentally frame the analysis as 'confirming' the suspect, then set parameters",
          "Request additional quantity/re-extraction before typing to reduce stochastic effects"
        ],
        "intended_action": "The analyst reads the detective's narrative before touching the electropherogram and frames the upcoming interpretation task as testing whether the evidence supports the already-named suspect, rather than as an open comparison against all possible contributors."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Electropherogram shows several allele peaks above threshold matching the suspect's known profile at multiple loci",
          "Two loci show expected suspect alleles missing or below the stochastic threshold, and one locus shows an extra unexplained peak",
          "Peak height ratios at several loci fall outside the typical heterozygote balance range, consistent with degraded or mixed low-template DNA"
        ],
        "new_information_after_decision": [
          "The finalized allele table foregrounds matching loci; the missing/extra peaks are logged only as 'inconclusive' footnotes",
          "A second reviewer later asks specifically about the missing alleles and the unexplained peak"
        ],
        "alternatives": [
          "Give equal analytic weight to present matching peaks and to absent/unexplained peaks when deciding how to characterize the profile",
          "Emphasize the matching peaks as the profile's defining feature and treat missing/extra peaks as noise to be footnoted rather than actively explained",
          "Flag the profile as too degraded for a reportable comparison and request retesting"
        ],
        "intended_action": "In summarizing the electropherogram for the case notes, the analyst highlights and elaborates on the loci where alleles matching the suspect are present, while the loci with missing expected alleles and the one unexplained extra peak receive only a brief, non-elaborated footnote."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Victim mentions during a follow-up call that an ex-boyfriend had visited the house three days before the break-in and that a delivery driver had also been at the door that week",
          "Only the homeowner's elimination profile has been run; ex-boyfriend and delivery driver samples are not available",
          "The suspect's profile is consistent with being a contributor to the mixture under the alternative hypothesis, but so would an unknown, unsampled contributor under a defense hypothesis",
          "Turnaround deadline for the bail hearing is the next morning"
        ],
        "new_information_after_decision": [
          "The report proceeds with the suspect-inclusion hypothesis as primary without requesting the ex-boyfriend or delivery driver samples",
          "Defense counsel later requests, during discovery, why alternative contributors were never sampled or statistically modeled"
        ],
        "alternatives": [
          "Apply the same evidentiary threshold used to accept the suspect-inclusion hypothesis to the alternative contributor hypotheses before ruling them out",
          "Treat the suspect-inclusion hypothesis as sufficiently supported and treat the unsampled alternative contributors as a documentation footnote rather than a competing hypothesis requiring the same scrutiny",
          "Delay the report and request rush elimination swabs from the ex-boyfriend and delivery driver before finalizing"
        ],
        "intended_action": "The analyst subjects the suspect-inclusion hypothesis to comparatively light scrutiny (accepting partial, ambiguous matches as adequate) while treating the unsampled alternative-contributor hypotheses as needing much stronger evidence before being taken seriously, without formally testing either hypothesis under matched criteria."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Draft likelihood ratio calculation is moderate, not overwhelming, given the partial profile and stochastic effects",
          "The written narrative section of the report already frames the sample as connecting the suspect to the point of entry",
          "Technical reviewer (the analyst's supervisor) is under the same 24-hour deadline and is reviewing quickly",
          "Some inconsistencies (missing alleles, unsampled alternative contributors) remain undocumented as open questions in the draft"
        ],
        "new_information_after_decision": [
          "The final report presents the moderate likelihood ratio alongside a narrative describing the suspect's presence 'near the scene' and prior record, woven into a single consistent account",
          "During later cross-examination, defense highlights that the statistical strength of the DNA evidence alone was moderate, not the strong match implied by the report's narrative framing"
        ],
        "alternatives": [
          "Report the statistical result (moderate likelihood ratio) separately from, and without narrative blending with, the non-genetic case facts (proximity, prior record)",
          "Integrate the moderate statistical result with the proximity and prior-record narrative into a single fluent account that reads as mutually reinforcing and internally consistent",
          "Flag the moderate strength explicitly as insufficient on its own and recommend against using it as primary evidence at the bail hearing"
        ],
        "intended_action": "In finalizing the report for peer sign-off, the analyst blends the moderate genetic likelihood ratio with the non-genetic narrative details (proximity, prior conviction) into one smooth, internally consistent story, resolving the earlier ambiguities as if they had never been open questions."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this case first came to your bench.",
        "What information did you have about the case before you began the analysis?"
      ],
      "timeline_reconstruction": [
        "What happened right after you received the sample and case file?",
        "Take me through what the electropherogram showed and how you interpreted it.",
        "What happened when the victim mentioned other people who had been in the house?",
        "Walk me through how you put the final report together."
      ],
      "decision_point_probes": [
        "What cues in the case file or detective's note stood out to you before you started typing the sample?",
        "What sources of information did you rely on when deciding how to characterize the electropherogram?",
        "What were you weighing when you decided not to pursue elimination samples from the ex-boyfriend or delivery driver?",
        "What was your goal when you wrote the narrative section of the final report?",
        "What alternatives did you consider at each of those points, and why did you rule them out or in?",
        "What was your basis for treating the matching loci differently from the missing or unexplained peaks?",
        "How much time pressure were you under at each stage, and did that affect what you checked or didn't check?",
        "How confident were you in the suspect-inclusion hypothesis compared to the alternative hypotheses, and why?",
        "Had you handled a similar low-template mixture case before? How did that shape your approach here?"
      ],
      "closing_hypotheticals": [
        "If the detective's note had not named a suspect before you started typing, would you have approached the electropherogram differently?",
        "If elimination samples from the ex-boyfriend and delivery driver had been available before your deadline, how might the report have changed?",
        "If the missing alleles at those two loci had been the ones matching the suspect instead of extra ones, would your write-up have looked different?",
        "Looking back, is there a point where you'd want to redo the analysis with different information available first?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cx_01",
        "bias": "Contextual Bias",
        "decision_point": 1,
        "mechanism": "Exposure to non-scientific, domain-irrelevant contextual information (detective's suspicion narrative and suspect's prior record) before examining the physical evidence shapes the analyst's interpretive frame for the upcoming genetic analysis.",
        "affected_reasoning_operation": "Task framing / expectation-setting prior to evidence examination",
        "evidence_available_at_time": [
          "Detective's cover note naming the suspect and expressing confidence in guilt",
          "Suspect's prior conviction listed on the submission form",
          "No genetic data yet reviewed"
        ],
        "required_textual_manifestation": "The analyst describes reading the detective's note and suspect information first, and frames the subsequent analysis in terms of testing/confirming that specific person rather than as an open, unknown-source comparison.",
        "plausible_nonbias_interpretation": "Reviewing all submitted case information, including detective notes, before analysis is a normal and required intake step; doing so is not itself proof of bias.",
        "strength": "subtle",
        "do_not_make_explicit": ["contextual bias", "priming", "expectation effect"]
      },
      {
        "instance_id": "fp_01",
        "bias": "Feature positive effect",
        "decision_point": 2,
        "mechanism": "Present, matching allele peaks (a positive, salient feature) receive elaborated analytic attention and description, while absent expected alleles and an unexplained extra peak (negative/discrepant features) receive comparatively minimal, non-elaborated treatment despite being equally diagnostic.",
        "affected_reasoning_operation": "Evidence weighting during allele-table summarization",
        "evidence_available_at_time": [
          "Multiple loci with peaks matching the suspect's known profile above threshold",
          "Two loci with expected suspect alleles missing or below threshold",
          "One locus with an unexplained extra peak"
        ],
        "required_textual_manifestation": "The analyst's account elaborates in detail on the matching loci but disposes of the missing-allele loci and the unexplained peak with only a brief footnote-style mention, without walking through what they might indicate.",
        "plausible_nonbias_interpretation": "Matching loci may simply be more straightforward to describe, while ambiguous or below-threshold data are conventionally logged as inconclusive per protocol.",
        "strength": "subtle",
        "do_not_make_explicit": ["feature positive effect", "salience", "negative evidence neglect"]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "decision_point": 3,
        "mechanism": "The analyst applies a lower evidentiary bar to accept the suspect-inclusion hypothesis than the bar applied to alternative-contributor hypotheses (ex-boyfriend, delivery driver), scrutinizing the disconfirming/competing possibilities far more skeptically than the favored one.",
        "affected_reasoning_operation": "Hypothesis evaluation and evidentiary threshold-setting when comparing competing source hypotheses",
        "evidence_available_at_time": [
          "Partial, ambiguous profile consistent with suspect as a contributor",
          "Victim's report of an ex-boyfriend and delivery driver with recent house access",
          "No elimination samples yet obtained from those alternative individuals",
          "Deadline pressure for the bail hearing"
        ],
        "required_textual_manifestation": "The analyst explains accepting the suspect-inclusion hypothesis as adequately supported by the partial match while dismissing or deprioritizing the alternative-contributor possibilities as unsampled footnotes, without applying a comparable evidentiary standard to both.",
        "plausible_nonbias_interpretation": "Time constraints legitimately limited the ability to obtain additional elimination samples before the hearing deadline.",
        "strength": "moderate",
        "do_not_make_explicit": ["confirmation bias", "asymmetrical skepticism", "double standard"]
      },
      {
        "instance_id": "co_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 4,
        "mechanism": "A moderate, individually ambiguous statistical result is blended together with unrelated non-genetic case facts (proximity, prior record) into one fluent, internally consistent narrative, so that the whole account feels more certain than the underlying statistical evidence alone supports.",
        "affected_reasoning_operation": "Final synthesis and narrative construction for the report",
        "evidence_available_at_time": [
          "Moderate, not overwhelming, likelihood ratio",
          "Unresolved open questions (missing alleles, unsampled alternatives) from earlier phases",
          "Non-genetic case facts: suspect's proximity to scene, prior conviction"
        ],
        "required_textual_manifestation": "The analyst describes writing the final report so that the moderate statistical finding and the non-genetic facts are folded into a single, smoothly consistent story, with earlier ambiguities resolved as though they had not been open questions.",
        "plausible_nonbias_interpretation": "Reports conventionally synthesize multiple lines of evidence into a coherent narrative for readability; doing so is a standard reporting practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["coherence-based reasoning", "rationalization", "narrative fallacy"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is 'biased', no paired control scenario was supplied in this generation request."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": "Not applicable: condition is 'biased', not 'counterfactual'. The caller marked counterfactual_variable as AUTOSELECT, but since no counterfactual condition was requested, no causal variable was selected or manipulated.",
      "causal_test_question": null
    },
    "generation_checks": [
      "Exactly four decision points are present, one per manifest bias, with no bias assigned to more than one decision point.",
      "Each of the four biases has exactly one planned instance with a unique instance_id (cx_01, fp_01, cb_01, co_01).",
      "No bias labels, technical bias terminology, or explicit psychological explanations appear in the technical_terms_to_use list or are permitted in the public interview.",
      "Each occurrence has a distinct evidence trace, decision point, and plausible non-bias interpretation, preventing accidental double-counting.",
      "Target word count (1,350 words, range 1,215-1,485) is achievable with four decision points, each requiring roughly 250-320 words of narrative plus probes, without repetitive exposition.",
      "Consequences described (bail hearing outcome, cross-examination) do not mechanically confirm or deny that any decision was biased.",
      "Counterfactual and control fields are correctly marked not applicable given condition='biased' and no paired scenario supplied."
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
