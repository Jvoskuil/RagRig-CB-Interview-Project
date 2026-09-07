You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "LE_Biased_6",
  "domain_id": "LE",
  "domain": "Law enforcement",
  "role": "Polygraph Examiner / Interview Specialist",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Distribution Center Inventory Theft Exam",
    "scenario_summary_internal": "A police department's polygraph examiner is asked by a detective to administer a specific-issue exam on a logistics supervisor suspected of orchestrating a six-figure inventory theft at a regional distribution center, ahead of a client-imposed audit deadline. The examiner reviews the detective's case briefing, participates in a pre-test team huddle, conducts and scores the exam under time pressure, and must decide how to communicate an ambiguous result to the investigative team.",
    "occupational_realism": {
      "objective": "Determine, via a specific-issue polygraph examination and structured pre/post-test interview, whether the logistics supervisor's denial of involvement in the inventory theft is credible, and communicate a defensible finding to the investigative team before a client audit deadline.",
      "setting": "Regional police department forensic services unit, small interview/testing room adjoining a detective bureau, over a single afternoon with a same-day debrief.",
      "constraints": [
        "Client (distribution company) audit deadline creates same-day pressure for a finding",
        "Detective supervising the case has already built an investigative theory naming the supervisor as primary suspect",
        "Only one examiner and one polygraph instrument available; no time for a second full retest",
        "Chain-of-custody and testing protocol require pre-test interview, instrument calibration, and standardized comparison-question technique",
        "Examiner reports to a multi-person case team including the lead detective and a junior detective"
      ],
      "stakeholders": [
        "Polygraph examiner (subject of CTA)",
        "Lead detective (case owner)",
        "Junior detective (present at pre-test huddle)",
        "Logistics supervisor (examinee)",
        "Distribution company liaison (external pressure source, not present)"
      ],
      "technical_terms_to_use": [
        "specific-issue exam",
        "comparison question technique (CQT)",
        "relevant question",
        "comparison question",
        "chart",
        "electrodermal activity",
        "respiration tracing",
        "inconclusive result",
        "pre-test interview",
        "post-test interview",
        "numerical scoring"
      ],
      "technical_terms_to_avoid": [
        "contextual bias",
        "coherence-based reasoning",
        "rationalisation",
        "cognitive dissonance",
        "feature positive effect",
        "groupthink",
        "any explicit bias label or psychological term naming the manifest biases"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Detective's written briefing describing supervisor as the 'clear person of interest' with narrative details about opportunity and financial strain",
          "Supervisor's personnel file with no prior disciplinary record",
          "No physiological data yet collected"
        ],
        "new_information_after_decision": [
          "Supervisor's pretest interview responses, some hesitant, some fluent",
          "Supervisor discloses unrelated personal stress (divorce) as reason for nervousness"
        ],
        "alternatives": [
          "Conduct pretest interview treating the briefing as one unverified input among several, independently establishing rapport and baseline behavior",
          "Let the detective's narrative frame question wording and interpretation of the supervisor's demeanor from the outset"
        ],
        "intended_action": "Examiner allows the briefing narrative to shape how ambiguous pretest behavior (hesitation, avoidance of eye contact) is read, treating it as corroborating the detective's theory rather than as neutral behavior needing independent baseline."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Pre-test huddle with lead and junior detective, both expressing confidence suspect is guilty",
          "Junior detective briefly notes an alternative internal candidate (temp worker) but does not press the point",
          "Time pressure to finalize test format before audit-driven deadline"
        ],
        "new_information_after_decision": [
          "Instrument calibrated; baseline physiological tracings collected",
          "First test chart shows a marked reaction on the relevant question about the missing inventory"
        ],
        "alternatives": [
          "Independently select comparison questions and test structure based on standard protocol regardless of team sentiment, and note the temp-worker lead for follow-up",
          "Adopt the team's consensus framing of the case, aligning comparison-question choice and initial reaction categorization with the shared expectation of the supervisor's guilt, without revisiting the temp-worker lead"
        ],
        "intended_action": "Examiner goes along with the team's unanimous framing, finalizes a comparison-question set matching the detective's theory, and lets the group's shared confidence substitute for independently probing the alternative lead."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Chart shows a clear electrodermal spike on the relevant question about hiding inventory records",
          "Comparison questions show similarly flat or minimal reactivity, which is itself informative but easy to overlook",
          "Numerical scoring guidelines call for evaluating relative reactivity across all question types, not isolated spikes"
        ],
        "new_information_after_decision": [
          "A second, independent scorer later flags that comparison-question reactivity was weaker than typical, which would normally reduce confidence in a deceptive call",
          "Supervisor's post-test interview reasserts denial calmly and consistently"
        ],
        "alternatives": [
          "Complete full numerical scoring comparing relevant vs. comparison zone reactivity before drawing any conclusion, and treat the case as inconclusive if data are mixed",
          "Highlight the presence of the relevant-question spike as decisive, treating the absence of comparable reactivity on comparison questions as unremarkable rather than as data reducing confidence in a deceptive finding"
        ],
        "intended_action": "Examiner flags the visible spike as the dominant, quotable finding, discounts the diagnostic value of the muted comparison-question reactivity, and privately reconciles the ambiguous overall chart with the guilt conclusion already voiced to the team by building a narrative that ties the spike, the earlier hesitant demeanor, and the financial-strain detail into one consistent story of deception."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Examiner has already told the detectives mid-afternoon that results 'look deceptive'",
          "Full scoring sheet, once completed, sits closer to inconclusive than clearly deceptive",
          "Team debrief scheduled before the audit deadline, with detectives expecting a definitive call"
        ],
        "new_information_after_decision": [
          "Report is filed with a finding that supports the detective's original theory",
          "Weeks later, inventory reconciliation records surface that only partially implicate the supervisor and also point to the temp worker mentioned earlier"
        ],
        "alternatives": [
          "Report the numerically inconclusive result as inconclusive, explaining the mixed chart data and unresolved temp-worker lead to the team even though it contradicts the earlier verbal impression",
          "Align the final written report with the earlier verbal 'deceptive' impression and the team's shared expectation, presenting the finding as more conclusive than the numerical scoring supports"
        ],
        "intended_action": "In the debrief, the junior detective's hesitant question about the borderline scores is met with reassurance from the lead detective and no one revisits it further; the examiner finalizes a report consistent with the group's shared expectation rather than the more equivocal numerical scoring."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through how this case came to you and what you knew before you met the supervisor.",
        "What was your objective going into this exam?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you know at that point?",
        "What new information came in after the pre-test interview, and how did it change your plan?",
        "Describe the huddle with the detectives before testing began.",
        "Walk me through scoring the chart step by step."
      ],
      "decision_point_probes": [
        "What cues from the briefing or interview stood out to you, and why?",
        "What information sources did you rely on at each stage, and how did you weigh them against each other?",
        "What was your goal at that specific moment, and did it conflict with any other goal?",
        "What alternatives did you consider before finalizing the comparison questions and the scoring?",
        "What was your decision basis for calling the result deceptive versus inconclusive?",
        "How did your prior experience with similar cases shape your read of the charts?",
        "How much time pressure did you feel, and did it affect what you checked or didn't check?",
        "How confident were you at each stage, and did that confidence change?",
        "If you had gotten a dissenting opinion from a colleague at that point, what would you have done differently?"
      ],
      "closing_hypotheticals": [
        "If the junior detective had pushed harder on the temp-worker lead, how would that have changed your approach?",
        "If you had scored the chart before telling the detectives your impression, do you think your conclusion would have been different?",
        "What would you do differently if you ran this exam again today?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Contextual Bias",
        "decision_point": 1,
        "mechanism": "Extraneous case-narrative information (detective's briefing framing supervisor as the clear suspect) contaminates interpretation of ambiguous pretest behavioral cues before any physiological data exist.",
        "affected_reasoning_operation": "Interpretation of demeanor/behavioral cues during pretest interview",
        "evidence_available_at_time": [
          "Detective's briefing narrative naming supervisor as primary suspect",
          "Supervisor's neutral personnel file",
          "No physiological data yet"
        ],
        "required_textual_manifestation": "Examiner explicitly describes reading the supervisor's hesitation/avoidance as corroborating guilt because of what the briefing said, rather than as neutral behavior warranting independent baseline assessment.",
        "plausible_nonbias_interpretation": "Reviewing a case file before an interview is standard, professional practice and does not by itself indicate biased judgment.",
        "strength": "subtle",
        "do_not_make_explicit": ["contextual bias", "priming", "anchoring"]
      },
      {
        "instance_id": "gt_01",
        "bias": "Groupthink",
        "decision_point": 2,
        "mechanism": "Unanimous verbal consensus among detectives in the pre-test huddle suppresses the examiner's independent evaluation of test design and the junior detective's alternative lead, favoring group harmony over dissent.",
        "affected_reasoning_operation": "Selection of comparison-question structure and evaluation of an alternative suspect lead",
        "evidence_available_at_time": [
          "Detectives' unanimous verbal confidence in supervisor's guilt",
          "Junior detective's brief, unpursued mention of a temp-worker alternative",
          "Deadline pressure"
        ],
        "required_textual_manifestation": "Examiner describes adopting the team's shared framing for the test structure and not revisiting the temp-worker lead because the room was in agreement, without independent verification.",
        "plausible_nonbias_interpretation": "Deferring to a lead detective's case knowledge is a normal division-of-labor practice in investigative teams.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "conformity", "consensus pressure"]
      },
      {
        "instance_id": "fpe_01",
        "bias": "Feature positive effect",
        "decision_point": 3,
        "mechanism": "The examiner disproportionately weights the presence of a visible relevant-question spike while failing to register the diagnostic significance of the absence of comparable reactivity on comparison questions.",
        "affected_reasoning_operation": "Chart scoring and evidence weighting",
        "evidence_available_at_time": [
          "Visible electrodermal spike on the relevant question",
          "Flat/minimal reactivity on comparison questions",
          "Numerical scoring protocol requiring comparison of both zones"
        ],
        "required_textual_manifestation": "Examiner recounts flagging the relevant-question spike as the standout finding while describing the comparison-question flatness as unremarkable or not worth mentioning.",
        "plausible_nonbias_interpretation": "A strong, clear physiological reaction is a legitimate and commonly emphasized scoring feature in polygraph practice.",
        "strength": "moderate",
        "do_not_make_explicit": ["feature positive effect", "absence blindness", "salience bias"]
      },
      {
        "instance_id": "cd_01",
        "bias": "Cognitive dissonance",
        "decision_point": 3,
        "mechanism": "Having already stated aloud to the detectives that results 'look deceptive,' the examiner experiences discomfort reconciling the borderline numerical scoring with that public commitment, and resolves it by discounting the mixed evidence rather than revising the stated impression.",
        "affected_reasoning_operation": "Updating a conclusion in light of new, disconfirming scoring information",
        "evidence_available_at_time": [
          "Earlier verbal statement to detectives calling the result 'deceptive'",
          "Numerical scoring trending toward inconclusive",
          "Supervisor's calm, consistent post-test denial"
        ],
        "required_textual_manifestation": "Examiner describes feeling uncomfortable with the borderline score given what was already said to the team and resolves the tension by minimizing the weight of the disconfirming data rather than revisiting the earlier statement.",
        "plausible_nonbias_interpretation": "Sticking with an initial professional impression can reflect legitimate confidence built from experience, not necessarily bias.",
        "strength": "moderate",
        "do_not_make_explicit": ["cognitive dissonance", "commitment bias", "belief perseverance"]
      },
      {
        "instance_id": "cr_01",
        "bias": "Coherence-based reasoning or Rationalisation",
        "decision_point": 3,
        "mechanism": "The examiner constructs a single tidy narrative linking the relevant-question spike, the earlier pretest hesitation, and the financial-strain detail into a mutually reinforcing story of guilt, even though each element individually is weak or ambiguous.",
        "affected_reasoning_operation": "Integration of disparate evidence into a final causal narrative",
        "evidence_available_at_time": [
          "Relevant-question spike",
          "Earlier pretest hesitation (already reinterpreted via briefing)",
          "Supervisor's disclosed financial strain",
          "Weak/ambiguous comparison-question data"
        ],
        "required_textual_manifestation": "Examiner explicitly ties together the spike, hesitant demeanor, and financial-strain detail as a coherent unified account of deception, smoothing over the individually weak or ambiguous nature of each piece.",
        "plausible_nonbias_interpretation": "Synthesizing multiple pieces of evidence into a coherent case theory is a normal and often necessary investigative skill.",
        "strength": "moderate",
        "do_not_make_explicit": ["coherence-based reasoning", "narrative fallacy", "rationalisation"]
      },
      {
        "instance_id": "gt_02",
        "bias": "Groupthink",
        "decision_point": 4,
        "mechanism": "In the final debrief, the junior detective's hesitant question about the borderline scores is met with reassurance and dropped without scrutiny, and the examiner finalizes a report matching the group's shared expectation rather than the more equivocal scoring, prioritizing team alignment over dissenting doubt.",
        "affected_reasoning_operation": "Finalization of the written report and resolution of a dissenting question",
        "evidence_available_at_time": [
          "Borderline/inconclusive-leaning numerical scoring",
          "Junior detective's hesitant question about the scores",
          "Lead detective's reassurance and the group's shared expectation of a deceptive finding",
          "Audit deadline pressure"
        ],
        "required_textual_manifestation": "Examiner describes the junior detective's question being smoothed over by the lead detective's reassurance, and finalizes the report in line with group expectation rather than probing the dissent further.",
        "plausible_nonbias_interpretation": "Trusting a supervising detective's judgment on how to close out a report is a normal chain-of-command practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["groupthink", "conformity", "dissent suppression"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition specification with no paired control requested in this call."
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
      "Target interview length 1,350 words (acceptable range 1,215-1,485 words); do not pad with repetitive exposition to hit the range.",
      "Exactly four decision points, each with at least two plausible alternatives.",
      "No bias name, definition, or psychological label appears anywhere in the public interview text.",
      "Each of the 6 planned instances appears exactly once, tied to the specific decision point and evidence source listed in occurrence_embedding_plan_internal.",
      "No additional unrequested instance of Contextual Bias, Coherence-based reasoning/Rationalisation, Cognitive dissonance, Feature positive effect, or Groupthink appears in probes, hypotheticals, or the outcome/consequence narrative.",
      "Consequences (partial implication of supervisor, emergence of temp-worker lead) must not mechanically confirm or deny that any decision was biased; they should remain interpretively open.",
      "Maintain distinct evidentiary bases for gt_01 (pre-test huddle/test design) and gt_02 (final debrief/report finalization) so they are independently identifiable.",
      "Maintain distinct evidentiary bases for fpe_01 (spike vs. absent comparison reactivity) and cd_01/cr_01 (dissonance from prior public statement vs. narrative integration) even though all three sit at decision point 3."
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
