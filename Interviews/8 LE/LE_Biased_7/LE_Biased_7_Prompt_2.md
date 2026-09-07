You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Biased_7",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Crime Scene Investigator (CSI) / Forensic Scene Examiner",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Staircase Fall: Elderly Decedent Scene Processing",
    "scenario_summary_internal": "A CSI is dispatched to a residence where an 82-year-old man is found deceased at the base of an interior staircase. Patrol has already framed the incident as an accidental fall consistent with the decedent's known mobility issues. Over the course of a single scene visit, the CSI documents physical evidence, interviews family and a neighbor, and synthesizes findings into a scene report, while an ambiguous bruise pattern and lividity inconsistency are never fully resolved. The scenario is designed to embed exactly seven bias instances across four decision points without any decision or outcome mechanically proving bias.",
    "occupational_realism": {
      "objective": "Independently and objectively document, interpret, and report physical evidence at a sudden-death scene to support the medical examiner's and detective's determination of manner of death.",
      "setting": "Single-family residence, interior staircase and first-floor landing, mid-afternoon call, single CSI working with one assisting patrol officer, family present nearby, detective reachable by phone but not on scene until later.",
      "constraints": [
        "CSI is queued for a second scene later that day, creating time pressure",
        "Family is present and distressed, limiting length/intrusiveness of on-scene interviews",
        "Medical examiner investigator has not yet arrived to formally assess the body",
        "Detective is handling the case remotely by phone for most of the visit",
        "Scene has already been lightly disturbed by first responders checking for signs of life"
      ],
      "stakeholders": [
        "CSI (protagonist/interviewee)",
        "First-arriving patrol officer",
        "Decedent's adult daughter and son-in-law (family present at scene)",
        "Next-door neighbor",
        "Lead detective (by phone)",
        "Medical examiner investigator (arrives late in timeline)"
      ],
      "technical_terms_to_use": [
        "scene walkthrough",
        "chain of custody",
        "livor mortis / lividity",
        "scale marker",
        "point-of-origin documentation",
        "manner of death",
        "scene reconstruction",
        "corroborating statement"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "cognitive dissonance",
        "contextual bias",
        "feature positive effect",
        "recency effect",
        "coherence-based reasoning",
        "asymmetrical skepticism",
        "heuristic",
        "any explicit bias-naming or psychological jargon"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch note: 'elderly male, found at bottom of stairs, unresponsive'",
          "Patrol officer's verbal briefing on arrival: decedent has fallen twice before, uses a walker, family says he was 'unsteady lately'",
          "Decedent found supine at base of staircase, walker overturned nearby"
        ],
        "new_information_after_decision": [
          "CSI's initial framing note in the scene log: 'apparent accidental fall, elderly male with mobility history'"
        ],
        "alternatives": [
          "Adopt the fall framing conveyed by patrol as the working orientation for the walkthrough",
          "Conduct a neutral, framing-free walkthrough first and form a working hypothesis only after independent observation",
          "Request the patrol officer withhold prior-history commentary until after the CSI's own initial assessment"
        ],
        "intended_action": "CSI accepts and adopts patrol's fall framing before completing an independent walkthrough, orienting subsequent documentation around confirming that frame."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Overturned walker approximately two feet from the body",
          "Staircase runner shows no visible drag or scuff marks",
          "Faint bruising visible on the decedent's upper left arm, not obviously explained by the fall trajectory",
          "Limited time before the CSI must relocate to a second queued scene"
        ],
        "new_information_after_decision": [
          "Multiple detailed photographs and measurements taken of the stairs and walker",
          "Single, non-scaled photograph taken of the arm bruise"
        ],
        "alternatives": [
          "Give the walker/staircase area and the arm bruise equal photographic and measurement rigor",
          "Prioritize documentation of the walker and stairs as the most probative fall-consistent evidence",
          "Flag the absent drag marks as an explicit data point requiring follow-up",
          "Treat the bruise as a priority item warranting scaled photography and measurement before other evidence"
        ],
        "intended_action": "CSI documents the walker/staircase area with high rigor, treats the absence of drag marks as a non-event, and gives the arm bruise only cursory, non-scaled documentation."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Family states decedent was on a new blood-pressure medication that 'made him dizzy'",
          "A pill bottle is visible on the nightstand but dosage/timing is not verified",
          "Neighbor volunteers that she heard 'raised voices' from the house two nights earlier",
          "The bruise and the fall trajectory remain only loosely reconciled"
        ],
        "new_information_after_decision": [
          "Scene notes record the medication explanation as an established fact",
          "Scene notes annotate the neighbor's statement as unconfirmed and note inability to corroborate the timeline",
          "A running narrative is drafted linking dizziness, medication, the walker, and the stairs into a single fall sequence, with the bruise folded in as fall-related"
        ],
        "alternatives": [
          "Apply the same corroboration standard to both the family's and the neighbor's statements",
          "Treat the medication claim as unconfirmed pending verification and pursue the neighbor's statement with equal or lesser scrutiny",
          "Separately test the bruise against the fall trajectory before folding it into the narrative",
          "Note the bruise as an open, unresolved item rather than integrating it into the fall account"
        ],
        "intended_action": "CSI treats the family's account as established without verification while subjecting the neighbor's account to pointed scrutiny, and separately drafts a single fluent fall narrative that absorbs the unexplained bruise without independent testing."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Earlier field notes (mid-visit) contain a hedge: 'bruise pattern warrants further review'",
          "Detective calls near the end of the visit and reiterates that the case 'looks like a straightforward fall'",
          "During a final body check before the ME investigator arrives, lividity pattern appears inconsistent with the body's found position",
          "CSI has already verbally told the detective the scene appears consistent with a fall"
        ],
        "new_information_after_decision": [
          "Final scene report closing summary echoes the detective's fall framing and omits the earlier hedge language",
          "Lividity inconsistency is noted briefly and attributed to 'possible positional shift during discovery' without further testing"
        ],
        "alternatives": [
          "Preserve the earlier hedge language and flag the lividity inconsistency as unresolved in the final report",
          "Contact the ME investigator immediately to jointly evaluate the lividity finding before finalizing the report",
          "Revise the classification pending toxicology and autopsy rather than closing the narrative on scene",
          "Finalize the report consistent with the detective's most recent framing and the already-stated fall conclusion"
        ],
        "intended_action": "CSI's final report adopts the detective's last-stated framing over earlier ambiguous notes, and the lividity inconsistency is minimized/rationalized to remain consistent with the conclusion already communicated to the detective."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what you knew before you got out of your vehicle at this scene.",
        "What was your first impression when you arrived, and where did that impression come from?"
      ],
      "timeline_reconstruction": [
        "Take me step by step through the order in which you examined and photographed the scene.",
        "At what point did family members or the neighbor speak with you, and what did each of them say?",
        "When did you first notice the bruise on the arm, and what did you do with that observation at the time?"
      ],
      "decision_point_probes": [
        "Why did you orient your initial walkthrough the way you did? What options did you consider?",
        "How did you decide how much documentation effort to give the walker and stairs versus the bruise? What alternatives did you weigh?",
        "How did you evaluate the family's statement about medication compared to the neighbor's statement about raised voices? What would have made you treat them differently?",
        "Walk me through how the final classification in your report came together. What changed between your mid-visit notes and your closing summary?"
      ],
      "decision_basis": [
        "What specific piece of evidence most influenced each of these decisions?",
        "Was there a moment where two pieces of evidence seemed to point in different directions? How did you resolve that?"
      ],
      "prior_experience": [
        "Have you worked similar elderly-fall scenes before? How did that experience shape what you looked for here?"
      ],
      "time_pressure": [
        "How did having another scene queued that day affect how you allocated your time here?"
      ],
      "uncertainty": [
        "At any point, did you feel unsure about the fall explanation? What did you do with that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the neighbor had spoken to you before the family did, do you think your notes would look different?",
        "If the detective had called earlier in the visit instead of near the end, would your final report have come out the same way?",
        "If the lividity finding had come up first thing at the scene instead of near the end, how might you have handled it?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "CB_01",
        "bias": "Contextual Bias",
        "decision_point": 1,
        "mechanism": "Extraneous prior information from patrol's briefing (fall history, unsteady gait) is adopted as the initial interpretive frame before independent observation of the scene occurs, shaping what is subsequently looked for.",
        "affected_reasoning_operation": "Initial hypothesis formation / perceptual framing of the scene",
        "evidence_available_at_time": [
          "Dispatch note",
          "Patrol officer's verbal history summary",
          "Body position and overturned walker"
        ],
        "required_textual_manifestation": "CSI's opening scene-log entry and description of the walkthrough order explicitly reflect having adopted the 'accidental fall' frame from patrol before independently assessing the scene.",
        "plausible_nonbias_interpretation": "Using an experienced patrol officer's on-scene assessment as an efficient starting point for triage is a reasonable operational heuristic.",
        "strength": "subtle",
        "do_not_make_explicit": ["contextual bias", "priming", "framing effect"]
      },
      {
        "instance_id": "FPE_01",
        "bias": "Feature positive effect",
        "decision_point": 2,
        "mechanism": "A salient present cue (the overturned walker) is heavily weighted in the documentation, while the absence of an expected corroborating cue (drag/scuff marks) is not registered as a comparably weighted data point.",
        "affected_reasoning_operation": "Evidence weighting during on-scene documentation",
        "evidence_available_at_time": [
          "Position of overturned walker",
          "Condition of staircase runner (no visible drag marks)"
        ],
        "required_textual_manifestation": "CSI describes noting and photographing the walker's position in detail, but describes the absence of drag marks only as something 'not really relevant to note' or omits discussing it as a finding in its own right.",
        "plausible_nonbias_interpretation": "Photographing a conspicuous displaced object before assessing subtler surface conditions is standard scene practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["feature positive effect", "absence blindness"]
      },
      {
        "instance_id": "CB2_01",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "decision_point": 2,
        "mechanism": "Documentation effort and evidentiary rigor are applied unevenly: high rigor (multiple angles, measurements) to evidence supporting the fall theory, minimal rigor (single unscaled photo) to a physical finding that could complicate it.",
        "affected_reasoning_operation": "Selective allocation of documentation effort based on fit with the working hypothesis",
        "evidence_available_at_time": [
          "Walker and staircase geometry",
          "Faint bruise on upper left arm"
        ],
        "required_textual_manifestation": "CSI's account of photographing/measuring the stairs and walker in detail contrasts with a described lack of scale marker or close-up treatment of the bruise, framed as a lower priority.",
        "plausible_nonbias_interpretation": "Time constraints require triaging documentation toward the most spatially central evidence first.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "asymmetrical skepticism"]
      },
      {
        "instance_id": "CB2_02",
        "bias": "Confirmation Bias and Asymmetrical skepticism",
        "decision_point": 3,
        "mechanism": "Two witness statements are held to different evidentiary standards: one supporting the working hypothesis is accepted without corroboration, the other (potentially complicating) is flagged for lack of corroboration and pursued more skeptically.",
        "affected_reasoning_operation": "Testimonial evidence evaluation / differential scrutiny of witness statements",
        "evidence_available_at_time": [
          "Family's statement about medication-induced dizziness",
          "Unverified pill bottle on nightstand",
          "Neighbor's statement about raised voices two nights earlier"
        ],
        "required_textual_manifestation": "CSI describes recording the family's medication explanation as settled while describing follow-up questions, caveats, or corroboration concerns applied specifically to the neighbor's account.",
        "plausible_nonbias_interpretation": "Family members are often better positioned to know a decedent's recent health status than a neighbor.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "asymmetrical skepticism", "differential scrutiny"]
      },
      {
        "instance_id": "COH_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 3,
        "mechanism": "Disparate evidentiary elements are assembled into a single fluent narrative, and the narrative's internal fit is treated as evidence of its accuracy, allowing an unexplained detail to be absorbed rather than independently tested.",
        "affected_reasoning_operation": "Narrative synthesis / causal reconstruction of events",
        "evidence_available_at_time": [
          "Medication claim",
          "Walker position",
          "Staircase geometry",
          "Unexplained arm bruise"
        ],
        "required_textual_manifestation": "CSI narrates a smooth sequential account (dizziness → reaching for walker → missed step → fall) that folds the bruise in as 'likely from the fall' without describing any biomechanical basis for that attribution.",
        "plausible_nonbias_interpretation": "Constructing a plausible sequence of events is a normal and necessary part of scene reconstruction.",
        "strength": "moderate",
        "do_not_make_explicit": ["coherence-based reasoning", "rationalization", "narrative fallacy"]
      },
      {
        "instance_id": "REC_01",
        "bias": "Recency Effects",
        "decision_point": 4,
        "mechanism": "Information received most recently (the detective's closing phone call) is given disproportionate weight relative to earlier, more ambiguous field observations recorded hours before, shaping the final judgment.",
        "affected_reasoning_operation": "Final synthesis and weighting of accumulated evidence over time",
        "evidence_available_at_time": [
          "Earlier hedge note: 'bruise pattern warrants further review'",
          "Detective's late call reiterating the fall theory"
        ],
        "required_textual_manifestation": "CSI's description of the closing report explicitly echoes the detective's just-received phrasing and describes the earlier hedge as having been dropped or softened in the final version.",
        "plausible_nonbias_interpretation": "A detective may have legitimately new information justifying an updated framing.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "primacy-recency", "last information dominance"]
      },
      {
        "instance_id": "CD_01",
        "bias": "Cognitive dissonance",
        "decision_point": 4,
        "mechanism": "Having already verbally committed to the fall conclusion with the detective, the CSI encounters evidence (lividity inconsistency) that conflicts with that commitment; the resulting discomfort is resolved by minimizing/reinterpreting the evidence rather than revisiting the conclusion.",
        "affected_reasoning_operation": "Post-commitment evaluation of disconfirming evidence",
        "evidence_available_at_time": [
          "Lividity pattern observed during final body check",
          "Prior verbal statement already given to the detective"
        ],
        "required_textual_manifestation": "CSI describes noticing the lividity mismatch, a moment of hesitation or discomfort, and then explains it away (e.g., 'positional shift') without describing any attempt to test that explanation, tying the resolution to having already told the detective the scene looked like a fall.",
        "plausible_nonbias_interpretation": "Livor mortis timing can genuinely be affected by minor repositioning of a body during discovery or first-responder checks.",
        "strength": "moderate",
        "do_not_make_explicit": ["cognitive dissonance", "commitment consistency", "post-decisional rationalization"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' with no paired control scenario supplied."
    },
    "counterfactual_specification": {
      "causal_variable": null,
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 7 total bias instances are embedded: 1 Feature positive effect, 1 Contextual Bias, 1 Coherence-based reasoning/Rationalisation, 1 Cognitive dissonance, 1 Recency Effects, 2 Confirmation Bias and Asymmetrical skepticism.",
      "Confirm no bias term, definition, or psychological label appears in the public interview text.",
      "Confirm exactly 4 decision points, each with at least 2 plausible alternatives.",
      "Confirm CB2_01 and CB2_02 use distinct evidence sources (physical evidence documentation vs. testimonial scrutiny) and distinct decision points.",
      "Confirm FPE_01 and CB2_01, though co-located at decision point 2, address different reasoning operations (salience weighting vs. differential documentation rigor) and different evidence framing.",
      "Confirm total interview length target is 1,350 words within 1,215–1,485 word range without repetitive exposition.",
      "Confirm each instance has a plausible non-bias explanation available in the text.",
      "Confirm no consequence in the timeline mechanically proves or disproves bias (manner-of-death determination remains open/pending ME and toxicology at scenario close)."
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
