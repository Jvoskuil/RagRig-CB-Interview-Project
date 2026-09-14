You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a routine case-review interview for our lab's cognitive task analysis project — we're documenting how analysts actually reason through casework, not evaluating your performance. Everything's de-identified before it goes anywhere. Okay if we record and talk through a recent case?

Participant: Sure, that's fine. Which case did you want to walk through?

Interviewer: The windowsill swab from the burglary-assault — the one that went to a bail hearing a few months back. Can you start by telling me how it landed on your bench?

Participant: It came in as a rush request. Patrol had picked up a guy about two blocks from the house maybe forty minutes after the call came in — broken window, homeowner had a cut on his arm from being shoved into a doorframe during the break-in. The detective's submission note said the suspect had a prior burglary conviction and that he was, in his words, "almost certainly good for it." The swab itself was blood and touch DNA off the broken windowsill glass. Quantity came back under 100 picograms on quant, so I knew going in this was going to be a low-template situation — lots of stochastic effects, peak height imbalance, that kind of thing.

Interviewer: What was your objective at that point?

Participant: Determine whether the suspect could be included as a contributor to that mixture, generate a likelihood ratio if the data supported one, and get a technically defensible report out. We had a 24-hour turnaround because the DA wanted it ahead of the bail hearing. And logistically, my supervisor was the only technical reviewer available that week, so whatever I produced, she'd be the one signing off, fast.

Interviewer: Let's reconstruct the sequence. What happened first?

Participant: I pulled the case file to set up my analysis parameters — stochastic threshold, amplification target, all standard. Before I got to the profile itself, I read through the detective's cover note and the submission form, which already had the suspect's name and known profile listed. Then I ran the amplification. Came back partial — several peaks near the stochastic threshold, which is typical for that DNA quantity. I built out the allele table, flagged the ambiguous loci, and moved into the comparison stage. A few days later the victim called back and mentioned an ex-boyfriend had been in the house three days before the break-in, and a delivery driver had been at the door earlier that week. That complicated the elimination picture, since we'd only swabbed the homeowner. I finished the report and sent it up for technical review the night before the hearing.

Interviewer: Let's slow down at that first step — reading the file before setting up the analysis. Walk me through what was going through your mind.

Participant: Honestly, it's just how intake works. You read the submission form, you see what the detective knows, you set your parameters. The note stood out because it was pretty confident — "found two blocks away," "almost certainly good for it." I remember thinking, okay, this is probably him, let's see if the DNA backs that up. So when I sat down with the electropherogram, I was looking at it as, does this data support what we've already got on this guy, rather than starting cold and asking who could this mixture belong to.

Interviewer: Did you consider setting parameters before reading the narrative part of the note?

Participant: Not really — the form comes as one packet. I suppose I could've separated the suspect information from the case narrative and looked at the profile blind first, then compared. I didn't do that here. In hindsight I'm not sure it would've changed the amplification parameters themselves, but it probably shaped how I was thinking about the comparison before I even looked at a single peak.

Interviewer: Let's go to the electropherogram itself. What did you see, and how did you write it up?

Participant: There were several loci where the peaks lined up cleanly with the suspect's known profile, right where you'd expect them, above threshold. I spent a good amount of time on those — peak heights, confirming they weren't stutter, checking the ratios. But there were also two loci where alleles I'd have expected from him were missing or sitting below threshold, and one locus had an extra peak I couldn't immediately place. Those went into the notes, but more as a line — "inconclusive due to low template" — rather than something I dug into the way I dug into the matching loci.

Interviewer: What made you treat those differently?

Participant: Partly it's just efficiency — the matching loci are easy to describe, they're clean. The missing and extra peaks are messier, and with low-template DNA, you do get dropout and occasional artifact peaks, so logging them as inconclusive isn't unusual practice. But if I'm being honest, I probably gave the matching data more narrative attention because it was doing more work for the story I was building, and the messy stuff got less airtime, not because it was less real.

Interviewer: Later, the victim mentions two other people who'd been in the house. What did you do with that?

Participant: That came in after I'd already built most of the comparison. We only had the homeowner's elimination sample at that point. I flagged internally that the ex-boyfriend and delivery driver were unsampled, but I didn't request rush swabs from either of them. Partly that's the deadline — the hearing was the next morning, there wasn't time to get new elimination samples processed. But I also remember thinking the suspect profile already fit well enough that chasing two more elimination samples felt like it would just confirm what we already had.

Interviewer: How did you weigh the suspect-inclusion hypothesis against those alternative sources?

Participant: I accepted the suspect as a plausible contributor based on the partial match we had — I didn't require additional testing to feel comfortable with that. For the ex-boyfriend or the driver, though, my instinct was that without their samples, there was no real basis to seriously entertain them, so I treated that as an open question for someone else to chase, not something that needed to hold up the report. Looking back, I didn't apply quite the same bar to both sides — the suspect got in on a partial match, but the alternatives needed a full sample before I'd take them seriously at all.

Interviewer: Is there a version of this where you'd have paused the report instead?

Participant: If the deadline had been longer, yeah, I think I'd have pushed for rush swabs on both of them before finalizing anything.

Interviewer: Let's talk about the final report. The likelihood ratio came back moderate, not overwhelming. How did that shape the writing?

Participant: Right, it wasn't a slam-dunk statistic on its own. But by that point I had the proximity — suspect found two blocks away shortly after the call — and his prior conviction sitting in the file too. When I wrote the narrative section, I pulled those together with the DNA finding into one account: the profile is consistent with him, he was near the scene, he's done this before. Read together it feels like a solid picture. My supervisor reviewed it quickly given her own deadline and signed off without flagging the open items — the missing alleles, the unsampled alternatives — as things that needed more work first.

Interviewer: Did you consider presenting the statistical result separately from those other facts?

Participant: I didn't, really. It felt more useful to the DA's office to have it all in one coherent narrative rather than a dry, hedged statistic sitting by itself. Later, during cross-examination, the defense made a point of separating them back out — saying the DNA evidence alone was moderate, and it was really the narrative framing that made it sound stronger than the number supported. That stung a little, but I don't think what I wrote was inaccurate exactly.

Interviewer: If the detective's note hadn't named a suspect before you started typing the sample, do you think you'd have approached the electropherogram differently?

Participant: Possibly. I might've gone in more neutral, treating it purely as an unknown mixture, and maybe I'd have spent as much time on the missing alleles as the matching ones, since there'd be no name pulling my attention toward one profile over another.

Interviewer: And if the ex-boyfriend and delivery driver's elimination samples had come back before the deadline?

Participant: If either of them had matched better than the suspect did, that would've changed everything about how I wrote the conclusion. I just didn't have that data in time, and I made a call with what I had.

Interviewer: Last one — anything you'd want to redo, given what you know now?

Participant: I'd want to look at the electropherogram before reading the detective's narrative, just to see if my read changes. And I'd push harder for those elimination samples even under time pressure, rather than letting the deadline decide that for me.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "LE_Biased_4",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as an evidentiary double standard between the favored suspect-inclusion hypothesis and unsampled alternative-contributor hypotheses at decision point 3."
      },
      {
        "bias": "Feature positive effect",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as elaborated attention to present/matching allele peaks versus minimal treatment of absent/unexplained peaks at decision point 2."
      },
      {
        "bias": "Contextual Bias",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as pre-analysis exposure to non-scientific case-context information shaping the interpretive frame at decision point 1."
      },
      {
        "bias": "Coherence-based reasoning or Rationalisation",
        "occurrences": 1,
        "mechanism_constraint": "Must manifest as blending a moderate statistical result with non-genetic narrative facts into one fluent, internally consistent account at decision point 4."
      }
    ],
    "target_bias_names": [
      "Confirmation Bias and Asymmetrical skepticism",
      "Feature positive effect",
      "Contextual Bias",
      "Coherence-based reasoning or Rationalisation"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confirmation Bias and Asymmetrical skepticism", "requested_occurrences": 1 },
      { "bias": "Feature positive effect", "requested_occurrences": 1 },
      { "bias": "Contextual Bias", "requested_occurrences": 1 },
      { "bias": "Coherence-based reasoning or Rationalisation", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cx_01", "bias": "Contextual Bias" },
      { "instance_id": "fp_01", "bias": "Feature positive effect" },
      { "instance_id": "cb_01", "bias": "Confirmation Bias and Asymmetrical skepticism" },
      { "instance_id": "co_01", "bias": "Coherence-based reasoning or Rationalisation" }
    ],
    "intended_decision_points": [
      { "instance_id": "cx_01", "bias": "Contextual Bias", "decision_point": 1 },
      { "instance_id": "fp_01", "bias": "Feature positive effect", "decision_point": 2 },
      { "instance_id": "cb_01", "bias": "Confirmation Bias and Asymmetrical skepticism", "decision_point": 3 },
      { "instance_id": "co_01", "bias": "Coherence-based reasoning or Rationalisation", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cx_01",
        "bias": "Contextual Bias",
        "mechanism": "Non-scientific case-context information (detective's suspicion narrative, suspect's prior record) is reviewed before physical evidence examination and frames the interpretive task as confirming a named individual rather than as an open comparison.",
        "affected_reasoning_operation": "Task framing / expectation-setting prior to evidence examination",
        "evidence_source": "Detective's cover note and suspect submission form, reviewed before electropherogram analysis",
        "distinctiveness_requirement": "Must occur strictly at intake/pre-analysis (decision point 1), before any genetic data is examined; distinct from the evidence-weighting operations at decision points 2 and 3."
      },
      {
        "instance_id": "fp_01",
        "bias": "Feature positive effect",
        "mechanism": "Present/matching allele peaks receive elaborated descriptive attention while absent/unexplained peaks receive minimal, non-elaborated treatment during allele-table summarization.",
        "affected_reasoning_operation": "Evidence weighting during allele-table summarization",
        "evidence_source": "Electropherogram allele peaks at multiple loci, some matching suspect profile and some missing/unexplained",
        "distinctiveness_requirement": "Must occur strictly during within-sample allele-level interpretation (decision point 2), distinguishable from the hypothesis-level scrutiny asymmetry at decision point 3."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "mechanism": "A lower evidentiary bar is applied to accept the suspect-inclusion hypothesis than the bar applied to alternative-contributor hypotheses, with competing possibilities scrutinized more skeptically than the favored one.",
        "affected_reasoning_operation": "Hypothesis evaluation and evidentiary threshold-setting across competing source hypotheses",
        "evidence_source": "Comparison between suspect's partial match and unsampled alternative contributors (ex-boyfriend, delivery driver) named by the victim",
        "distinctiveness_requirement": "Must occur strictly at the hypothesis-comparison stage (decision point 3), operating on hypothesis-level evidentiary standards rather than single-sample peak description (fp_01) or pre-analysis framing (cx_01)."
      },
      {
        "instance_id": "co_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "mechanism": "A moderate, individually ambiguous statistical result is synthesized with unrelated non-genetic facts into one fluent, internally consistent narrative that resolves prior open ambiguities without independent justification.",
        "affected_reasoning_operation": "Final synthesis and narrative construction for the report",
        "evidence_source": "Draft likelihood ratio combined with non-genetic case facts (proximity, prior conviction) at report finalization",
        "distinctiveness_requirement": "Must occur strictly at final report synthesis (decision point 4), operating on narrative integration across multiple evidence types, distinct from the single-hypothesis evidentiary threshold issue at decision point 3."
      }
    ],
    "intended_strength": [
      { "instance_id": "cx_01", "bias": "Contextual Bias", "strength": "subtle" },
      { "instance_id": "fp_01", "bias": "Feature positive effect", "strength": "subtle" },
      { "instance_id": "cb_01", "bias": "Confirmation Bias and Asymmetrical skepticism", "strength": "moderate" },
      { "instance_id": "co_01", "bias": "Coherence-based reasoning or Rationalisation", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "LE_Biased_4",
    "domain_id": "LE",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per distinct decision point, selected for mechanism fit and narrative realism: contextual bias assigned to pre-analysis intake (DP1), feature positive effect to within-sample allele interpretation (DP2), confirmation bias/asymmetrical skepticism to cross-hypothesis evidentiary comparison (DP3), and coherence-based reasoning/rationalisation to final narrative synthesis (DP4). No bias shares a decision point with another instance of itself or another named bias.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Case type (residential burglary escalating to assault)",
      "Sample type (low-template mixed DNA from windowsill swab)",
      "Number of decision points (four)",
      "Deadline pressure (24-hour turnaround before bail hearing)",
      "Cast of stakeholders (detective, supervisor/technical reviewer, victim, suspect, DA)"
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
      "segment_type": "technical_expectation",
      "raw_interview_anchor": "Quantity came back under 100 picograms on quant, so I knew going in this was going to be a low-template situation — lots of stochastic effects, peak height imbalance, that kind of thing.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "This is a technical expectation about low-template DNA and stochastic effects. It does not express one of the hidden bias mechanisms."
    },
    {
      "segment_id": "seg_002",
      "speaker": "Participant",
      "segment_type": "case_context_assessment",
      "raw_interview_anchor": "A few days later the victim called back and mentioned an ex-boyfriend had been in the house three days before the break-in, and a delivery driver had been at the door earlier that week. That complicated the elimination picture, since we'd only swabbed the homeowner.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The participant recognizes that additional people complicate the elimination picture, but this statement does not yet apply different evidentiary standards to the suspect and alternatives."
    },
    {
      "segment_id": "seg_003",
      "speaker": "Participant",
      "segment_type": "intake_procedure_rationale",
      "raw_interview_anchor": "Honestly, it's just how intake works. You read the submission form, you see what the detective knows, you set your parameters.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "This describes routine intake practice. Exposure to a case file alone is not the hidden instance; the suspect-specific framing is mapped separately."
    },
    {
      "segment_id": "seg_004",
      "speaker": "Participant",
      "segment_type": "pre_analysis_task_framing",
      "raw_interview_anchor": "The note stood out because it was pretty confident — 'found two blocks away,' 'almost certainly good for it.' I remember thinking, okay, this is probably him, let's see if the DNA backs that up. So when I sat down with the electropherogram, I was looking at it as, does this data support what we've already got on this guy, rather than starting cold and asking who could this mixture belong to.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "cx_01"
      ],
      "ground_truth_rationale": "Before examining the profile, the participant describes framing the analysis as testing whether the DNA supports the named suspect, following exposure to the detective's suspicion and the suspect's prior record."
    },
    {
      "segment_id": "seg_005",
      "speaker": "Participant",
      "segment_type": "blind_review_reflection",
      "raw_interview_anchor": "I suppose I could've separated the suspect information from the case narrative and looked at the profile blind first, then compared. I didn't do that here. In hindsight I'm not sure it would've changed the amplification parameters themselves, but it probably shaped how I was thinking about the comparison before I even looked at a single peak.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "cx_01"
      ],
      "ground_truth_rationale": "This reflects on the same pre-analysis contextual framing and says the narrative probably shaped the comparison before any peak was examined. It is not a separate planned occurrence."
    },
    {
      "segment_id": "seg_006",
      "speaker": "Participant",
      "segment_type": "allele_evidence_weighting",
      "raw_interview_anchor": "There were several loci where the peaks lined up cleanly with the suspect's known profile, right where you'd expect them, above threshold. I spent a good amount of time on those — peak heights, confirming they weren't stutter, checking the ratios. But there were also two loci where alleles I'd have expected from him were missing or sitting below threshold, and one locus had an extra peak I couldn't immediately place. Those went into the notes, but more as a line — 'inconclusive due to low template' — rather than something I dug into the way I dug into the matching loci.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "fp_01"
      ],
      "ground_truth_rationale": "The participant reports elaborating on matching loci while giving missing expected alleles and an unexplained peak only brief treatment."
    },
    {
      "segment_id": "seg_007",
      "speaker": "Participant",
      "segment_type": "evidence_weighting_rationale",
      "raw_interview_anchor": "But if I'm being honest, I probably gave the matching data more narrative attention because it was doing more work for the story I was building, and the messy stuff got less airtime, not because it was less real.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "fp_01"
      ],
      "ground_truth_rationale": "The participant explicitly says matching features received more narrative attention while discrepant features received less, completing the evidence-weighting manifestation."
    },
    {
      "segment_id": "seg_008",
      "speaker": "Participant",
      "segment_type": "alternative_testing_decision",
      "raw_interview_anchor": "I flagged internally that the ex-boyfriend and delivery driver were unsampled, but I didn't request rush swabs from either of them. Partly that's the deadline — the hearing was the next morning, there wasn't time to get new elimination samples processed. But I also remember thinking the suspect profile already fit well enough that chasing two more elimination samples felt like it would just confirm what we already had.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "cb_01"
      ],
      "ground_truth_rationale": "The participant declined to pursue alternatives partly because the suspect already seemed to fit, alongside the legitimate deadline constraint."
    },
    {
      "segment_id": "seg_009",
      "speaker": "Participant",
      "segment_type": "comparative_evidentiary_threshold",
      "raw_interview_anchor": "I accepted the suspect as a plausible contributor based on the partial match we had — I didn't require additional testing to feel comfortable with that. For the ex-boyfriend or the driver, though, my instinct was that without their samples, there was no real basis to seriously entertain them ... Looking back, I didn't apply quite the same bar to both sides — the suspect got in on a partial match, but the alternatives needed a full sample before I'd take them seriously at all.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "cb_01"
      ],
      "ground_truth_rationale": "This explicitly states the lower evidentiary bar for the suspect and higher bar for alternatives, matching the hidden hypothesis-level double standard."
    },
    {
      "segment_id": "seg_010",
      "speaker": "Participant",
      "segment_type": "counterfactual_resource_decision",
      "raw_interview_anchor": "If the deadline had been longer, yeah, I think I'd have pushed for rush swabs on both of them before finalizing anything.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "This is a hindsight counterfactual about what the participant might have done with more time. It does not independently establish another manifestation beyond the contemporaneous double standard."
    },
    {
      "segment_id": "seg_011",
      "speaker": "Participant",
      "segment_type": "final_evidence_synthesis",
      "raw_interview_anchor": "Right, it wasn't a slam-dunk statistic on its own. But by that point I had the proximity — suspect found two blocks away shortly after the call — and his prior conviction sitting in the file too. When I wrote the narrative section, I pulled those together with the DNA finding into one account: the profile is consistent with him, he was near the scene, he's done this before. Read together it feels like a solid picture.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "co_01"
      ],
      "ground_truth_rationale": "The participant combines a moderate DNA statistic with proximity and prior-record facts into one narrative that feels stronger as a whole."
    },
    {
      "segment_id": "seg_012",
      "speaker": "Participant",
      "segment_type": "report_communication_choice",
      "raw_interview_anchor": "I didn't, really. It felt more useful to the DA's office to have it all in one coherent narrative rather than a dry, hedged statistic sitting by itself. Later, during cross-examination, the defense made a point of separating them back out — saying the DNA evidence alone was moderate, and it was really the narrative framing that made it sound stronger than the number supported.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "co_01"
      ],
      "ground_truth_rationale": "The participant describes choosing a coherent combined account and reports that the framing made the moderate DNA result sound stronger than its standalone statistic."
    },
    {
      "segment_id": "seg_013",
      "speaker": "Participant",
      "segment_type": "retrospective_process_recommendation",
      "raw_interview_anchor": "I'd want to look at the electropherogram before reading the detective's narrative, just to see if my read changes. And I'd push harder for those elimination samples even under time pressure, rather than letting the deadline decide that for me.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "This is a retrospective recommendation for a different process. It is not evidence of an additional contemporaneous bias occurrence."
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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single case-review transcript analyzed for cognitive bias occurrences in the participant's reported forensic DNA reasoning. Only mechanisms with affirmative interview evidence were identified; structural constraints such as time pressure were not treated as biases unless a distinct cognitive mechanism was also present."
  },
  "identified_bias_summary": [
    {
      "bias_label": "biased assimilation",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "narrative bias",
      "identified_occurrence_count": 1
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
        "suspect bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's existing beliefs, expectations, or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial hypothesis formation after reading the case file before DNA profile analysis",
      "decision_point_description": "Choosing whether to approach the DNA profile blind or after reading the detective's suspect-focused narrative and known suspect profile.",
      "affected_reasoning_operation": "Hypothesis generation and framing of the DNA comparison",
      "bias_specific_mechanism": "The detective's suspect-centered contextual information created a prior expectation that the suspect was the contributor, leading the analyst to frame the DNA comparison as a test of whether the data supported the already-suspected person rather than starting neutrally from the mixture.",
      "manifestation_in_interview": "The analyst reports reading the detective's confident narrative and the known suspect profile before examining the electropherogram, and describes thinking the suspect was probably the source before seeing the DNA data.",
      "effect_on_reasoning_or_decision": "The analyst approached the profile as suspect-confirming rather than neutral, which likely shaped the subsequent comparison and interpretation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The detective's submission note said the suspect had a prior burglary conviction and that he was, in his words, 'almost certainly good for it.'",
          "evidence_explanation": "This contextual information is irrelevant to whether the DNA profile itself matches the suspect, but it supplied a strong prior."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I remember thinking, okay, this is probably him, let's see if the DNA backs that up.",
          "evidence_explanation": "This explicitly states a suspect-confirming hypothesis before the profile had been analyzed."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I was looking at it as, does this data support what we've already got on this guy, rather than starting cold and asking who could this mixture belong to.",
          "evidence_explanation": "This shows the framing of the comparison as seeking support for an already-suspected individual."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "it probably shaped how I was thinking about the comparison before I even looked at a single peak.",
          "evidence_explanation": "The analyst self-reports that the contextual information affected his comparison approach."
        }
      ],
      "correction_or_counterevidence": "The participant notes that intake normally includes reading the submission form and that separating the narrative might not have changed amplification parameters. He also discusses the issue reflectively, but this does not negate the self-reported effect on comparison framing.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support describes how irrelevant contextual case information can bias forensic examiners even when they believe they are objective; the specific 'confirmation bias' label is assigned from general cognitive science.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Human expert performance in forensic decision making  Seven different sources of bias .pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Irrelevant Case Information. This source of bias refers to a whole range of contextual information that is not relevant to the forensic examiner and their work, but nevertheless may influence and bias... Although they believe their conclusions are solely based on the bone fragment evidence, and are objective, in fact their exposure to irrelevant case information biases their work.",
          "mechanism_supported_by_source": "Irrelevant contextual information can bias forensic conclusions despite examiners' belief that they are objective.",
          "relevance_to_this_occurrence": "The detective's suspect-focused note and prior-conviction information were contextual rather than DNA-profile evidence, and the analyst reports they shaped his initial hypothesis."
        },
        {
          "source_identifier": null,
          "paper_title": "cognitive-and-human-factors-in-expert-decision-making-six-fallacies-and-the-eight-sources-of-bias.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "the suspect driving the analysis rather than the evidence itself.",
          "mechanism_supported_by_source": "A named suspect can bias the analysis by making the suspect rather than the evidence drive the comparison.",
          "relevance_to_this_occurrence": "The analyst described approaching the electropherogram with the suspect already in mind rather than starting cold from the mixture."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "biased assimilation",
      "alternative_labels": [
        "confirmation bias",
        "selective scrutiny"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to accept belief-consistent evidence with relatively little scrutiny while subjecting belief-inconsistent evidence to more skeptical or dismissive evaluation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of electropherogram matching and nonmatching loci",
      "decision_point_description": "Deciding how much scrutiny and narrative attention to allocate to matching loci versus missing expected alleles, below-threshold alleles, and an extra peak.",
      "affected_reasoning_operation": "Evidence evaluation and weighting during DNA profile interpretation",
      "bias_specific_mechanism": "Loci consistent with the favored suspect were examined thoroughly and treated as meaningful supporting data, while inconsistent loci were recorded as 'inconclusive due to low template' without equivalent scrutiny, explicitly because they did not fit the story being built.",
      "manifestation_in_interview": "The analyst spent considerable time on matching loci, checking peak heights, stutter, and ratios, but logged missing and extra alleles with comparatively little attention.",
      "effect_on_reasoning_or_decision": "Confirming DNA data received more evidential weight and narrative prominence than potentially undercutting data, leading to a one-sided interpretation of the mixture.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I spent a good amount of time on those — peak heights, confirming they weren't stutter, checking the ratios.",
          "evidence_explanation": "Shows detailed scrutiny of hypothesis-consistent loci."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But there were also two loci where alleles I'd have expected from him were missing or sitting below threshold, and one locus had an extra peak I couldn't immediately place. Those went into the notes, but more as a line — 'inconclusive due to low template' — rather than something I dug into the way I dug into the matching loci.",
          "evidence_explanation": "Shows differential treatment of hypothesis-inconsistent information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I probably gave the matching data more narrative attention because it was doing more work for the story I was building, and the messy stuff got less airtime, not because it was less real.",
          "evidence_explanation": "Explicitly identifies the biasing mechanism: confirming evidence was favored because it supported the emerging suspect narrative."
        }
      ],
      "correction_or_counterevidence": "The participant notes that efficiency and low-template stochastic effects can make missing or extra peaks legitimately difficult to resolve. However, he then states directly that the mismatch data received less attention because it did not support the story, not merely because it was less probative.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the specific label 'biased assimilation' was not available; label and mechanism are assigned from general cognitive science.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "myside bias",
        "asymmetric evidence standards"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to favor a currently held hypothesis by seeking or accepting evidence that supports it while applying a higher standard to alternative hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Considering unsampled alternative contributors after the victim reported an ex-boyfriend and delivery driver",
      "decision_point_description": "Deciding whether to request rush elimination swabs from the alternative contributors or hold the report pending additional testing.",
      "affected_reasoning_operation": "Comparison of the favored suspect hypothesis against alternative source hypotheses",
      "bias_specific_mechanism": "The suspect was accepted as a plausible contributor on a partial match, while the ex-boyfriend and delivery driver were not seriously considered without full reference samples; the analyst applied a lower evidential bar to the suspect and a higher bar to alternatives.",
      "manifestation_in_interview": "The analyst did not request rush swabs for the alternatives and treated them as an open question rather than something that needed to hold up the report.",
      "effect_on_reasoning_or_decision": "The favored suspect hypothesis was retained despite unresolved alternative contributors, reducing the likelihood of disconfirmation and shaping the final report.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I accepted the suspect as a plausible contributor based on the partial match we had — I didn't require additional testing to feel comfortable with that.",
          "evidence_explanation": "Shows a relatively low acceptance threshold for the suspect hypothesis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "For the ex-boyfriend or the driver, though, my instinct was that without their samples, there was no real basis to seriously entertain them, so I treated that as an open question for someone else to chase, not something that needed to hold up the report.",
          "evidence_explanation": "Shows a higher threshold for alternative hypotheses."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I didn't apply quite the same bar to both sides — the suspect got in on a partial match, but the alternatives needed a full sample before I'd take them seriously at all.",
          "evidence_explanation": "The analyst explicitly names the asymmetric evidential standard."
        }
      ],
      "correction_or_counterevidence": "There is a plausible non-bias factor: the alternatives were unsampled, while the suspect had actual DNA data, and requiring reference samples before comparison can be legitimate. The key biasing feature is the explicit asymmetric acceptance of the suspect on a partial match while alternatives were not seriously considered absent full samples.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support is indirect: it supports suspect-driven analysis rather than the specific asymmetric-evidence-standard mechanism, so the label also relies on general cognitive science.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "cognitive-and-human-factors-in-expert-decision-making-six-fallacies-and-the-eight-sources-of-bias.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "the suspect driving the analysis rather than the evidence itself.",
          "mechanism_supported_by_source": "A named suspect can bias analysis so that the suspect, rather than the evidence, drives interpretation.",
          "relevance_to_this_occurrence": "The analyst's favored suspect hypothesis shaped how seriously he weighed alternative contributors and whether he required additional testing."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "narrative bias",
      "alternative_labels": [
        "coherence effect",
        "narrative fallacy"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to integrate information into a coherent causal story, which can make the overall account feel more persuasive than the individual pieces of evidence support.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Writing the final report narrative",
      "decision_point_description": "Deciding how to present a moderate DNA likelihood ratio in relation to non-DNA contextual facts.",
      "affected_reasoning_operation": "Integration and communication of evidence in the final report",
      "bias_specific_mechanism": "The analyst combined independent pieces—the moderate DNA likelihood ratio, proximity to the scene, and prior conviction—into a single coherent narrative, making the overall picture feel stronger than the statistical DNA result alone supported.",
      "manifestation_in_interview": "The analyst wrote the DNA finding together with proximity and prior conviction as one account, stating that read together it felt like a solid picture.",
      "effect_on_reasoning_or_decision": "The report communicated a stronger overall impression than the moderate DNA statistic alone warranted, as the defense later highlighted during cross-examination.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right, it wasn't a slam-dunk statistic on its own. But by that point I had the proximity — suspect found two blocks away shortly after the call — and his prior conviction sitting in the file too.",
          "evidence_explanation": "Shows that the DNA statistic alone was moderate and other contextual facts were available."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I wrote the narrative section, I pulled those together with the DNA finding into one account: the profile is consistent with him, he was near the scene, he's done this before. Read together it feels like a solid picture.",
          "evidence_explanation": "Demonstrates coherence-based integration producing a strengthened subjective picture."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It felt more useful to the DA's office to have it all in one coherent narrative rather than a dry, hedged statistic sitting by itself.",
          "evidence_explanation": "Shows the decision to present the information as a narrative rather than as separate evidentiary components."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Later, during cross-examination, the defense made a point of separating them back out — saying the DNA evidence alone was moderate, and it was really the narrative framing that made it sound stronger than the number supported. That stung a little, but I don't think what I wrote was inaccurate exactly.",
          "evidence_explanation": "Provides external and self-reported evidence that the narrative framing increased perceived strength beyond the numerical DNA result."
        }
      ],
      "correction_or_counterevidence": "The non-DNA facts may be legitimately relevant to the broader case narrative, and the participant denies that the written account was inaccurate. The issue is the coherence-induced inflation of perceived evidence strength rather than a false factual claim.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the specific 'narrative bias' label was not available; label and mechanism are assigned from general cognitive science.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Single-case retrospective self-report; causal influence on the original decisions cannot be directly verified.",
    "Some labels and mechanisms, including biased assimilation and narrative bias, are assigned from general cognitive science because retrieved corpus support was unavailable.",
    "The analysis is based on the participant's own description, which may include retrospective reconstruction and self-presentation effects.",
    "No external ground truth or experimental benchmark is used to determine correctness of the case decisions.",
    "Time pressure and missing reference samples are structural constraints in this case and were not classified as biases unless accompanied by a distinct cognitive mechanism."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "LE_Biased_4_Sonar_on",
  "interview_id": "LE_Biased_4",
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
