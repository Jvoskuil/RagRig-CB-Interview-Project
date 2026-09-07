You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "EM_Biased_3",
  "domain_id": "EM",
  "domain": "Emergency Management and Civil Protection",
  "role": "Local Emergency Manager (County/Municipal Level)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Millbrook Creek Flash Flood Escalation",
    "scenario_summary_internal": "A county emergency manager responsible for a river-valley jurisdiction with a documented history of minor, manageable flooding must respond to a rapidly evolving flash flood threat driven by an atypical, slow-moving convective storm cell. The manager must decide when to escalate monitoring, whether and when to order evacuation of a low-lying mobile home community, how to allocate limited shelter and staffing resources under a compressed timeline, and how to frame the response afterward during an after-action review. The scenario is designed to elicit one instance each of Normality Bias (underweighting an atypical threat signal because of a benign local flood history), Planning Fallacy (underestimating time and resource needs for evacuation logistics based on best-case past performance), and Bias Blind Spot (recognizing bias in a colleague's judgment while failing to recognize an analogous pattern in one's own reasoning during reflective probing).",
    "occupational_realism": {
      "objective": "Protect life safety in the Millbrook Creek floodplain by making timely, well-resourced evacuation and resource-allocation decisions during a fast-developing flash flood event.",
      "setting": "County Office of Emergency Management, Emergency Operations Center (EOC), and field liaison with county sheriff, public works, and a regional Red Cross chapter during a 14-hour flash flood event.",
      "constraints": [
        "Limited EOC staffing (skeleton night shift until escalation)",
        "Single road access/egress for the Millbrook Mobile Home Park",
        "State mutual aid resources require 4-6 hour lead time to mobilize",
        "Shelter capacity limited to two designated sites with partial ADA accessibility",
        "Historical gauge data shows only minor, non-damaging overflow events at this location for 15 years",
        "Forecast uncertainty regarding storm cell movement and rainfall totals"
      ],
      "stakeholders": [
        "County Emergency Manager (interviewee)",
        "Sheriff's Office watch commander",
        "Public Works director",
        "Red Cross regional coordinator",
        "Mobile home park residents",
        "National Weather Service (NWS) forecaster",
        "County Board liaison"
      ],
      "technical_terms_to_use": [
        "flash flood watch/warning",
        "EOC activation level",
        "gauge height",
        "evacuation order vs. advisory",
        "mutual aid request",
        "shelter-in-place",
        "after-action review (AAR)"
      ],
      "technical_terms_to_avoid": [
        "normalcy bias",
        "planning fallacy",
        "bias blind spot",
        "cognitive bias",
        "heuristic",
        "anchoring",
        "overconfidence bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "NWS issues a flash flood watch citing an unusually slow-moving, high-precipitable-water storm cell",
          "Gauge at Millbrook Creek is at normal seasonal level",
          "Fifteen years of records show only minor, non-damaging overflow at this gauge during comparable watches",
          "Duty forecaster verbally flags this event as atypical in structure"
        ],
        "new_information_after_decision": [
          "Radar-estimated rainfall totals exceed the watch threshold within two hours",
          "Gauge begins rising faster than any prior watch-level event on record"
        ],
        "alternatives": [
          "Activate EOC to Level 2 and pre-position resources immediately",
          "Maintain routine monitoring and wait for a warning (not just a watch) before escalating",
          "Request an informal check-in call with NWS forecaster before deciding"
        ],
        "intended_action": "Maintain routine monitoring, citing the area's consistent history of manageable events, and defer formal escalation until a warning is issued."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Gauge has now crossed the warning threshold; NWS upgrades to a flash flood warning",
          "Millbrook Mobile Home Park (140 residents, single-road egress) sits in the most exposed zone",
          "Past voluntary evacuations of this park have been completed in under 90 minutes",
          "Current event involves nighttime conditions and a portion of residents without vehicles"
        ],
        "new_information_after_decision": [
          "Actual evacuation notification and loading takes over three hours due to door-to-door contact needs and one blocked access point",
          "Shuttle buses requested from Public Works arrive later than estimated"
        ],
        "alternatives": [
          "Order evacuation with a timeline built on the fastest prior comparable evacuation",
          "Order evacuation with contingency buffer time and pre-stage additional transport before ordering",
          "Issue a shelter-in-place advisory for upper units, evacuate only ground-level units first"
        ],
        "intended_action": "Order full evacuation using a timeline modeled on the fastest previous evacuation of the same park, without adding contingency time for nighttime conditions or reduced staffing."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two designated shelters have uneven capacity; one is nearing its limit",
          "Red Cross coordinator flags that overflow routing to shelter B will require additional staff not yet on site",
          "Public Works reports the access road may close within the hour due to rising water",
          "Mutual aid request has not yet been formally submitted"
        ],
        "new_information_after_decision": [
          "Shelter B reaches capacity faster than shelter A due to uneven routing",
          "Mutual aid resources arrive after the access road has already closed"
        ],
        "alternatives": [
          "Submit the mutual aid request immediately alongside shelter routing decisions",
          "Delay mutual aid request until shelter capacity data is fully confirmed",
          "Split resources evenly between shelters regardless of real-time capacity reports"
        ],
        "intended_action": "Route evacuees primarily to shelter A based on initial capacity assumptions, and delay the mutual aid request pending further confirmation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Event concludes with no fatalities but a near-miss when the access road closed with a transport vehicle still en route",
          "After-action review is being conducted; a Sheriff's Office colleague is criticized in the room for having doubted the initial watch severity",
          "Interviewer asks the emergency manager to reflect on decision quality across the event",
          "Manager has direct visibility into their own decision log from phases 1-3"
        ],
        "new_information_after_decision": [
          "AAR panel later flags the same monitoring-escalation lag in the manager's own timeline that was criticized in the colleague's account",
          "Documentation shows the manager's evacuation and shelter estimates also relied on best-case historical benchmarks"
        ],
        "alternatives": [
          "Acknowledge that one's own escalation and estimation judgments may share the same pattern being criticized in the colleague",
          "Attribute the colleague's hesitation to a personal or situational shortcoming distinct from one's own decision-making",
          "Request a structured, criteria-based comparison of both decision timelines before drawing conclusions"
        ],
        "intended_action": "Critique the colleague's initial hesitation as a personal misjudgment while describing one's own escalation and estimation decisions as sound and well-reasoned given the information at the time."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first caught your attention about this event?",
        "What was your role and objective at the very start of the shift?"
      ],
      "timeline_reconstruction": [
        "What information did you have at each stage, and where did it come from?",
        "What changed between the watch and the warning, and when did you learn it?",
        "Walk me through what happened at the mobile home park step by step."
      ],
      "decision_point_probes": [
        "What alternatives did you consider before deciding to hold at routine monitoring?",
        "How did you arrive at the evacuation timeline estimate?",
        "What made you choose shelter A as the primary routing destination?",
        "How did you weigh the mutual aid timing decision against road-closure risk?"
      ],
      "closing_hypotheticals": [
        "If the storm had behaved exactly like a typical prior event, what would you have done differently, if anything?",
        "Looking back at the after-action discussion, do you see anything in your own decisions that mirrors what was raised about your colleague?",
        "If you had unlimited staffing from the outset, what would you change about the evacuation plan?",
        "What would you tell a newer emergency manager to watch for in a similar event next time?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "nb_01",
        "bias": "Normality Bias",
        "decision_point": 1,
        "mechanism": "Manager discounts an explicit forecaster warning that the storm is atypical, instead anchoring the threat assessment to fifteen years of benign local outcomes at the same gauge.",
        "affected_reasoning_operation": "Risk assessment / threat classification under initial ambiguous evidence",
        "evidence_available_at_time": [
          "NWS flash flood watch citing atypical storm structure",
          "Direct verbal flag from duty forecaster that the event differs from past patterns",
          "Fifteen-year benign outcome history at the gauge"
        ],
        "required_textual_manifestation": "Manager explicitly justifies delaying escalation by referencing the gauge's consistent past behavior, without addressing the forecaster's specific atypicality flag.",
        "plausible_nonbias_interpretation": "Resource-conscious managers reasonably avoid over-escalating on every watch given staffing costs and false-alarm fatigue.",
        "strength": "subtle",
        "do_not_make_explicit": ["normalcy bias", "base rate", "historical bias", "cognitive bias"]
      },
      {
        "instance_id": "pf_01",
        "bias": "Planning Fallacy",
        "decision_point": 2,
        "mechanism": "Evacuation timeline is built from the single fastest historical evacuation of the same park, ignoring known complicating factors present in this event (nighttime, reduced staffing, no-vehicle residents) that were absent in the reference case.",
        "affected_reasoning_operation": "Duration/resource estimation for a multi-step logistics task",
        "evidence_available_at_time": [
          "Prior evacuation records showing a 90-minute best case",
          "Known nighttime conditions and partial lack of resident vehicles",
          "Single-road egress constraint"
        ],
        "required_textual_manifestation": "Manager states the evacuation was planned around the fastest prior completion time without incorporating adjustments for the differing conditions, and expresses surprise when the real duration triples.",
        "plausible_nonbias_interpretation": "Using a recent successful precedent as a planning baseline is a common and often reasonable heuristic when time is short.",
        "strength": "moderate",
        "do_not_make_explicit": ["planning fallacy", "optimism bias", "reference class", "underestimation bias"]
      },
      {
        "instance_id": "bbs_01",
        "bias": "Bias Blind Spot",
        "decision_point": 4,
        "mechanism": "During the after-action reflection, the manager readily identifies a judgment flaw (hesitation despite a warning) in a colleague's account but does not recognize the same pattern of discounting atypical evidence and using best-case estimates in their own documented decisions from the same event.",
        "affected_reasoning_operation": "Self-referential judgment evaluation during retrospective causal attribution",
        "evidence_available_at_time": [
          "Colleague's criticized hesitation described in the AAR discussion",
          "Manager's own decision log from phases 1-3, directly accessible in the same review",
          "AAR panel's later note that both timelines show a similar escalation lag"
        ],
        "required_textual_manifestation": "Manager critiques the colleague's judgment in specific terms while describing their own analogous decisions as sound and appropriately reasoned, despite having the same information available for self-comparison.",
        "plausible_nonbias_interpretation": "It is reasonable to believe one had more context or better justification for a decision than an outside observer initially credits.",
        "strength": "subtle",
        "do_not_make_explicit": ["bias blind spot", "self-serving bias", "third-person bias", "meta-bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired control scenario is specified for this generation request."
    },
    "counterfactual_specification": {
      "causal_variable": "Lead time between forecaster's atypicality flag and formal EOC escalation decision",
      "original_state": "Manager defers escalation until a formal warning is issued, roughly two hours after the atypicality flag and rainfall exceedance",
      "counterfactual_state": "Manager escalates EOC activation immediately upon receiving the forecaster's atypicality flag, prior to formal warning issuance",
      "variables_to_hold_constant": [
        "Storm behavior and rainfall totals",
        "Mobile home park population and access constraints",
        "Shelter capacity and staffing availability",
        "Mutual aid lead time requirements",
        "After-action review structure and participants"
      ],
      "expected_causal_difference": "Earlier escalation would likely compress the evacuation and shelter-routing timeline, reducing the near-miss at the access road, and would provide a direct causal contrast for isolating the effect of the Normality Bias instance at decision point 1.",
      "causal_test_question": "Would earlier EOC escalation, holding storm behavior and population constant, have prevented the downstream evacuation and routing time pressure observed in the biased condition?"
    },
    "generation_checks": [
      "Confirm interview draft falls between 1,215 and 1,485 words",
      "Confirm exactly 4 decision points are present and clearly demarcated",
      "Confirm each of nb_01, pf_01, bbs_01 appears exactly once with sufficient evidence trace",
      "Confirm no bias name, definition, or psychological label appears in interview text",
      "Confirm each decision point offers at least two plausible alternatives",
      "Confirm probes cover cues, sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm consequences described do not mechanically prove bias presence",
      "Confirm no unintended additional instance of any named bias is introduced in probes, hypotheticals, or summaries"
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
