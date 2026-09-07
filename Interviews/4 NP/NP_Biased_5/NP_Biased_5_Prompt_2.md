You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "NP_Biased_5",
  "domain_id": "NP",
  "domain": "Nuclear power and Process-control operations",
  "role": "Procedure Engineer / Technical Procedure Writer",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "AFW Instrumentation Procedure Revision Under Deadline",
    "scenario_summary_internal": "A procedure engineer at a nuclear station must revise the Emergency Operating Procedure (EOP) step sequence for Auxiliary Feedwater (AFW) initiation after a design change replaces an analog level transmitter with a new digital unit. The revision must be completed before the next scheduled outage window closes, incorporating a newly issued industry Operating Experience (OE) report describing an instrumentation-related event at another plant. The engineer works through triage of the OE report, drafting of validation steps, weighting of historical test data, and final sign-off under time pressure, each step offering at least two plausible paths.",
    "occupational_realism": {
      "objective": "Revise and validate the AFW initiation procedure steps to correctly reflect the new digital level transmitter before the outage-driven implementation deadline, while ensuring the change is defensible under the site's 10CFR50.59 screening and human-factors review.",
      "setting": "Procedure engineering office and control room simulator mock-up at a pressurized water reactor station, three days before the scheduled outage window for procedure implementation.",
      "constraints": [
        "Hard deadline tied to outage schedule; procedure must be approved before implementation window opens",
        "Limited access to the full OE database due to a concurrent audit locking some records",
        "Only one qualified peer reviewer available due to staffing rotation",
        "New transmitter has different response curve and failure modes than legacy unit",
        "Procedure change must pass human-factors and V&V review before submission to plant approval board"
      ],
      "stakeholders": [
        "Procedure Engineer (interviewee)",
        "Shift Technical Advisor",
        "Instrumentation & Controls engineer who executed the design change",
        "Independent peer reviewer",
        "Outage planning coordinator",
        "Plant approval board"
      ],
      "technical_terms_to_use": [
        "Emergency Operating Procedure (EOP)",
        "Auxiliary Feedwater (AFW)",
        "level transmitter",
        "setpoint",
        "Operating Experience (OE) report",
        "design change package",
        "10CFR50.59 screening",
        "verification and validation (V&V)",
        "independent peer review",
        "surveillance test",
        "control room walkthrough",
        "nonconformance report"
      ],
      "technical_terms_to_avoid": [
        "similarity bias",
        "habit intrusion",
        "bounded rationality",
        "recency bias",
        "imperfect rationality",
        "cognitive bias",
        "heuristic error"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "A new OE report describes a transmitter failure at another station using a similar-looking digital unit from a different vendor family",
          "The design change package for this station's new transmitter has different calibration and failure-mode documentation",
          "Outage schedule leaves limited time to fully cross-reference the OE report against the local design change"
        ],
        "new_information_after_decision": [
          "The I&C engineer later notes the OE report's transmitter uses a different sensing technology than the one installed locally"
        ],
        "alternatives": [
          "Treat the OE report as directly applicable and adopt its recommended step language without further comparison",
          "Request the I&C engineer confirm technical equivalence between the two transmitter models before incorporating OE guidance",
          "Table the OE report as low relevance and proceed with the original design change package only"
        ],
        "intended_action": "Engineer judges the OE event as applicable based on surface resemblance (both are 'new digital level transmitters') and begins drafting revised steps around it."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The new transmitter requires a distinct verification step involving a two-point calibration check not previously required for the legacy analog unit",
          "The engineer has written dozens of prior AFW-related procedure revisions using a standard verification template",
          "Time is limited before the draft must go to peer review"
        ],
        "new_information_after_decision": [
          "The peer reviewer flags that the two-point calibration check is missing from the draft"
        ],
        "alternatives": [
          "Draft the new verification section from the design change package's specific requirements",
          "Reuse the standard template sequence from prior revisions and adapt wording only superficially",
          "Consult the I&C engineer directly before drafting any verification steps"
        ],
        "intended_action": "Engineer defaults to the familiar template sequence used across many past revisions, carrying over the accustomed verification pattern rather than building the sequence from the new transmitter's specific requirements."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "The engineer has access to five years of historical AFW surveillance test data, plus a test performed just two weeks earlier on an unrelated but recently revised procedure",
          "The two-week-old test used a similar-looking verification form",
          "Older test data covers more operating conditions relevant to the current transmitter's failure modes"
        ],
        "new_information_after_decision": [
          "A later data review shows the older test set included conditions closer to the actual transmitter fault signature"
        ],
        "alternatives": [
          "Weight the full five-year historical data set proportionally to its relevance",
          "Anchor primarily on the two-week-old test as the most representative baseline",
          "Request additional historical data pulls before finalizing validation criteria"
        ],
        "intended_action": "Engineer gives outsized weight to the two-week-old test result when setting validation criteria, treating it as the most representative baseline because it is freshest in mind."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Deadline is now less than 24 hours away",
          "Only the control room log and the engineer's own notes are readily at hand; the locked-audit OE database section cannot be accessed in time",
          "The draft procedure has passed an initial informal check but not full independent V&V",
          "The engineer must judge whether residual failure-mode risk from the new transmitter is acceptable for submission"
        ],
        "new_information_after_decision": [
          "The approval board later requests a supplemental risk note before final sign-off, revealing a failure mode not addressed in the submitted draft"
        ],
        "alternatives": [
          "Submit the draft as sufficiently validated based on readily available records and proceed to approval",
          "Request a short extension to complete a fuller independent search of the OE database",
          "Escalate the unresolved failure-mode question to the Shift Technical Advisor before submission"
        ],
        "intended_action": "Engineer stops searching once the readily accessible records seem adequate (satisficing under time and access constraints), then finalizes a risk judgment using a simplified mental estimate of failure-mode coverage rather than a fuller structured analysis."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this procedure revision was for and why it came up?",
        "What was your main objective when you started this task?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what information did you have at that point?",
        "Walk me through each step you took from receiving the design change package to submitting the draft.",
        "What new information came in as you worked through the revision?"
      ],
      "decision_point_probes": [
        "At the point you reviewed the OE report, what made you decide it applied to this transmitter?",
        "When drafting the verification steps, what sources did you rely on and why?",
        "How did you decide which historical test data to weight most heavily?",
        "When time got short, how did you decide the draft was ready to submit?",
        "What alternatives did you consider at each of these points, and why did you rule them out?"
      ],
      "closing_hypotheticals": [
        "If you'd had another full day, would you have approached the OE report review differently?",
        "If the audit hadn't locked part of the OE database, what would you have checked?",
        "Looking back, is there a point where you'd have wanted a second set of eyes earlier?",
        "How confident were you in the final risk judgment at the time, versus now?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "sb_01",
        "bias": "Similarity Bias",
        "decision_point": 1,
        "mechanism": "Engineer judges the OE report applicable to the local design change primarily because both involve 'new digital level transmitters,' relying on surface-level resemblance rather than confirmed technical equivalence.",
        "affected_reasoning_operation": "Relevance/applicability judgment during evidence triage",
        "evidence_available_at_time": [
          "OE report describing a different vendor's transmitter",
          "Local design change package with distinct calibration and failure-mode documentation"
        ],
        "required_textual_manifestation": "Engineer states the OE event 'looked like the same kind of situation' and proceeds to incorporate its guidance before checking whether the sensing technologies match.",
        "plausible_nonbias_interpretation": "A cautious engineer might reasonably treat any OE report on similar equipment as worth incorporating as a precaution, regardless of exact technical match.",
        "strength": "subtle",
        "do_not_make_explicit": ["similarity", "bias", "surface resemblance"]
      },
      {
        "instance_id": "hi_01",
        "bias": "Habit Intrusion",
        "decision_point": 2,
        "mechanism": "Engineer's drafting defaults to the standard verification template used across numerous prior AFW procedure revisions, a well-practiced behavioral pattern, rather than being generated fresh from the new transmitter's specific design change requirements.",
        "affected_reasoning_operation": "Action selection during procedure drafting",
        "evidence_available_at_time": [
          "Design change package specifying a distinct two-point calibration requirement",
          "Engineer's long history of writing similar procedures with a standard template"
        ],
        "required_textual_manifestation": "Engineer describes writing the verification section 'the way I always do it' before realizing later that the template didn't include the new calibration step.",
        "plausible_nonbias_interpretation": "Using a proven template could be a reasonable efficiency practice when time is short, not necessarily an error.",
        "strength": "moderate",
        "do_not_make_explicit": ["habit", "intrusion", "automatic pattern"]
      },
      {
        "instance_id": "rb_01",
        "bias": "Recency Bias",
        "decision_point": 3,
        "mechanism": "Engineer disproportionately weights the two-week-old test result as the representative baseline for validation criteria, despite older historical data covering conditions more relevant to the transmitter's actual failure signature.",
        "affected_reasoning_operation": "Evidence weighting during validation-criteria setting",
        "evidence_available_at_time": [
          "Five years of historical AFW surveillance test data",
          "A recent (two-week-old) test using a similar-looking form"
        ],
        "required_textual_manifestation": "Engineer explains choosing the recent test as the anchor because 'it was the freshest data I had in mind,' without weighing it against the fuller historical set.",
        "plausible_nonbias_interpretation": "Recent test data could genuinely be considered more current and thus preferable on procedural-currency grounds.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency", "bias", "freshest in mind"]
      },
      {
        "instance_id": "br_01",
        "bias": "Bounded Rationality",
        "decision_point": 4,
        "mechanism": "Under deadline and access constraints, engineer stops the information search once readily available records (control room log, own notes) seem minimally sufficient, rather than continuing to seek fuller information as an unconstrained search would.",
        "affected_reasoning_operation": "Information-gathering termination decision",
        "evidence_available_at_time": [
          "Locked audit preventing full OE database access",
          "Control room log and personal notes readily accessible",
          "Less than 24 hours remaining before deadline"
        ],
        "required_textual_manifestation": "Engineer states they 'went with what was on hand because there wasn't time to dig further,' treating the limited accessible evidence as adequate for closure.",
        "plausible_nonbias_interpretation": "Given a genuine hard deadline and blocked database access, stopping the search could be a reasonable resource-constrained judgment call.",
        "strength": "moderate",
        "do_not_make_explicit": ["bounded rationality", "satisficing", "limited search"]
      },
      {
        "instance_id": "ir_01",
        "bias": "Imperfect Rationality",
        "decision_point": 4,
        "mechanism": "In forming the final risk judgment on residual failure-mode coverage, engineer relies on a simplified mental estimate ('it's probably fine, most of the cases are covered') rather than a structured comparison against the full failure-mode list, producing a judgment that deviates from what a fuller analysis would show.",
        "affected_reasoning_operation": "Final risk-acceptability synthesis prior to submission",
        "evidence_available_at_time": [
          "Draft procedure with incomplete independent V&V",
          "Partial failure-mode documentation from the design change package",
          "Engineer's own rough mental tally of covered versus uncovered scenarios"
        ],
        "required_textual_manifestation": "Engineer describes concluding the residual risk was acceptable based on a quick mental tally rather than a systematic failure-mode-by-failure-mode check, later shown incomplete when the approval board requests a supplemental risk note.",
        "plausible_nonbias_interpretation": "Experienced engineers often use rapid holistic judgment as legitimate expert shortcut when full analysis isn't feasible in time available.",
        "strength": "moderate",
        "do_not_make_explicit": ["imperfect rationality", "systematic deviation", "heuristic judgment"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable for biased condition; no control variant generated under this specification."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable — no counterfactual condition requested",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Exactly 5 total bias instances planned across exactly 4 decision points",
      "No decision point contains more than one instance of the same bias",
      "Decision point 4 contains two distinct biases (Bounded Rationality, Imperfect Rationality) with clearly differentiated reasoning operations (search termination vs. final judgment synthesis)",
      "No bias label, definition, or psychological terminology appears in probe_plan or timeline wording",
      "Each instance has a plausible non-bias explanation to avoid mechanical detectability",
      "Target word count 1,215–1,485 achievable given 4 decision points with moderate probe depth"
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
