You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MO_Biased_2",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Watchkeeping Officer (Bridge Watch)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "Fishing Fleet Crossing in the Strait Squall",
    "scenario_summary_internal": "A second officer stands a night watch aboard a mid-size containership transiting a congested strait during intermittent monsoon squalls. A low-radar-cross-section fishing boat closes on a crossing track while ARPA ranks it as low priority relative to larger tracked targets. As visibility drops further, a cluster of fishing boats appears near a waypoint where a serious near-miss was documented in a recent company safety bulletin. The officer must manage attention across multiple contacts, decide when to depart from the automated system's risk ranking, and judge the actual probability of a repeat incident versus the vivid recalled case, while a genuinely converging bulk carrier requires separate assessment.",
    "occupational_realism": {
      "objective": "Maintain a safe, COLREGs-compliant passage through a congested strait during the 0000-0400 watch, correctly prioritizing collision risk among multiple concurrent contacts under degraded visibility.",
      "setting": "Bridge of a mid-size containership transiting a busy international strait at night, intermittent monsoon squalls, moderate fishing-fleet activity, ARPA/ECDIS-equipped bridge, single OOW plus lookout, Master on standby call.",
      "constraints": [
        "Reduced visibility from intermittent squalls",
        "Multiple simultaneous radar/AIS contacts of varying reliability",
        "Small wooden fishing vessels with low radar cross-section and no functioning AIS",
        "Fixed passage schedule and traffic separation scheme requirements",
        "Single qualified lookout available to supplement OOW",
        "Master not immediately on the bridge, contactable but not present"
      ],
      "stakeholders": [
        "Officer of the Watch (subject)",
        "Lookout/AB on watch",
        "Master (on standby call)",
        "Crews of nearby fishing vessels",
        "Approaching bulk carrier's bridge team",
        "Company safety/fleet office (source of prior bulletin)"
      ],
      "technical_terms_to_use": [
        "ARPA", "CPA", "TCPA", "COLREGs", "AIS", "OOW", "VHF", "radar plot",
        "safe speed", "close-quarters situation", "lookout", "squall",
        "fishing fleet", "waypoint", "bridge team", "Master", "traffic separation scheme",
        "radar cross-section", "give-way vessel", "stand-on vessel"
      ],
      "technical_terms_to_avoid": [
        "automation bias", "availability bias", "availability heuristic",
        "overreliance", "anchoring", "cognitive bias", "heuristic", "algorithm trust"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "ARPA has acquired and is tracking 5 targets, none flagged critical by CPA/TCPA",
          "VHF traffic mentions active fishing fleet operating in the area",
          "Weather forecast indicates intermittent squalls reducing visibility to under 1nm for short intervals",
          "Passage plan requires holding course to next waypoint in the TSS"
        ],
        "new_information_after_decision": [
          "A small wooden fishing boat, not previously acquired by ARPA, is sighted visually at approximately 3nm on a converging bearing",
          "The lookout reports the boat's navigation light is dim and intermittent"
        ],
        "alternatives": [
          "Rely on the ARPA-generated target list and its CPA/TCPA ranking to allocate scanning attention",
          "Conduct an independent visual and radar sweep specifically to catch low-cross-section contacts not shown by ARPA"
        ],
        "intended_action": "OOW splits attention between ARPA monitoring and periodic manual visual sweeps, catching the unacquired fishing boat via lookout report rather than system alert."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The fishing boat is now within 2nm, still not firmly held by ARPA due to weak radar return",
          "ARPA's overall risk ranking (based on the 5 tracked targets) still shows no target above the alarm threshold",
          "The lookout reports the fishing boat appears to be altering course erratically, inconsistent with a steady CPA solution",
          "Own ship's speed and heading are within the TSS lane requirements"
        ],
        "new_information_after_decision": [
          "The fishing boat continues on a track that reduces range faster than the manually estimated plot suggested",
          "No response is received to two VHF calls directed at the fishing boat"
        ],
        "alternatives": [
          "Treat the fishing boat as low-priority because the ARPA system has not elevated it on the ranked target list, and continue standard monitoring",
          "Independently plot the fishing boat by hand using visual bearings and take early avoiding action regardless of its ARPA ranking"
        ],
        "intended_action": "OOW defers to the system's overall low-priority ranking and delays independent maneuvering action, continuing to monitor rather than altering course early. [AUTOMATION_BIAS_INSTANCE: ab_01]"
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A squall reduces visibility sharply; radar shows a loose cluster of 3-4 small contacts near the upcoming waypoint",
          "This waypoint is the same location referenced in a company safety bulletin describing a serious near-miss with a fishing-boat cluster two weeks earlier in similar fog conditions",
          "A separate, larger contact identified as a bulk carrier is closing from the OOW's starboard bow with a computed CPA inside 1nm",
          "Current plotted spacing and bearing drift of the fishing cluster do not yet indicate an especially high closing rate"
        ],
        "new_information_after_decision": [
          "The bulk carrier's CPA continues to tighten and requires a genuine collision-avoidance response shortly after",
          "The fishing cluster passes at a wider margin than initially feared, without requiring emergency action"
        ],
        "alternatives": [
          "Judge the current risk level primarily by how closely the situation resembles the vividly recalled bulletin incident, prioritizing attention and evasive planning toward the fishing cluster",
          "Judge current risk using the actual plotted spacing, bearing drift, and closing rates of all contacts, including the bulk carrier, independent of the recalled incident"
        ],
        "intended_action": "OOW reallocates attention and prepares an evasive maneuver oriented toward the fishing cluster because the recalled bulletin incident makes that outcome feel highly likely, temporarily under-attending to the bulk carrier's tightening CPA. [AVAILABILITY_BIAS_INSTANCE: av_01]"
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Both the fishing cluster and the bulk carrier situations have been resolved without collision",
          "The Master calls the bridge for a status update before the watch handover",
          "The remainder of the watch will pass through one more area with reported fishing activity"
        ],
        "new_information_after_decision": [
          "The relieving officer requests a full brief on both contacts and the reasoning used during the encounter"
        ],
        "alternatives": [
          "Log the encounter as routinely resolved and hand over the watch without changes to standing orders",
          "Recommend to the Master that an additional lookout be posted for the remainder of the transit given the fishing activity"
        ],
        "intended_action": "OOW briefs the Master and recommends an additional lookout for the remaining fishing-activity area, based on the plotted contact behavior observed during the watch."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe the overall situation on the bridge that night and what you were responsible for.",
        "What was your main objective during this watch?"
      ],
      "timeline_reconstruction": [
        "Walk me through the sequence of contacts you dealt with, in order.",
        "At what point did the fishing boat become a concern, and how did that unfold?",
        "What happened when visibility dropped near the waypoint?"
      ],
      "decision_point_probes": [
        "At the point you first noticed the unacquired fishing boat, what information sources were you using, and how did you decide where to focus attention?",
        "When the fishing boat closed to about 2nm without ARPA elevating it, what made you decide to continue monitoring rather than take early action? What alternatives did you consider?",
        "When the squall hit and the cluster appeared near that waypoint, what specifically drove your sense of how dangerous the situation was? How did that compare with the bulk carrier's situation?",
        "When you briefed the Master afterward, how did you decide what to recommend for the rest of the watch?"
      ],
      "cues": [
        "What specific cues told you the fishing boat's light was unreliable?",
        "What cues, if any, made the fishing cluster feel similar to the earlier bulletin incident?"
      ],
      "information_sources": [
        "Which instruments or reports did you rely on most at each stage, and why?"
      ],
      "goals": [
        "How did you balance schedule/passage requirements against collision-avoidance caution?"
      ],
      "alternatives": [
        "What other options did you consider and reject at each decision point?"
      ],
      "decision_basis": [
        "What ultimately tipped your decision at the point you delayed action on the fishing boat?",
        "What ultimately tipped your attention toward the fishing cluster over the bulk carrier?"
      ],
      "prior_experience": [
        "Had you encountered a similar situation before, and did that affect how you read this one?"
      ],
      "time_pressure": [
        "How much time did you feel you had to decide at each of these points?"
      ],
      "uncertainty": [
        "What were you most uncertain about at each stage, and how did you handle that uncertainty?"
      ],
      "closing_hypotheticals": [
        "If the ARPA had flagged the fishing boat early as high-risk, do you think you would have acted differently?",
        "If there had been no recent bulletin about a similar incident, do you think your attention would have been distributed differently between the fishing cluster and the bulk carrier?",
        "What would you do differently if you faced this same combination of contacts again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "ab_01",
        "bias": "Automation Bias",
        "decision_point": 2,
        "mechanism": "OOW defers to ARPA's aggregate risk ranking (based on well-tracked large targets) as the basis for inaction on a weakly-tracked, erratically-moving small craft, despite an independent lookout report suggesting elevated risk.",
        "affected_reasoning_operation": "Risk prioritization and choice of when to escalate to manual avoidance action",
        "evidence_available_at_time": [
          "ARPA target list showing no target above alarm threshold",
          "Lookout report of erratic small-craft movement inconsistent with a steady ARPA-style solution",
          "Two unanswered VHF calls"
        ],
        "required_textual_manifestation": "OOW explicitly cites the system's ranking/alarm status as the reason for not escalating, while acknowledging the lookout's conflicting visual read, and delays independent plotting or maneuver until range has closed further.",
        "plausible_nonbias_interpretation": "It is reasonable domain practice to trust a calibrated ARPA alarm threshold when workload is high and to avoid premature helm action on an unconfirmed contact.",
        "strength": "moderate",
        "do_not_make_explicit": ["automation bias", "overreliance on automation", "algorithm trust"]
      },
      {
        "instance_id": "av_01",
        "bias": "Availability Bias",
        "decision_point": 3,
        "mechanism": "OOW's estimate of the fishing cluster's danger is driven by the vividness and recency of a specific bulletin-reported near-miss at the same waypoint, rather than by the current plotted spacing/closing-rate data, leading to a temporary misallocation of attention away from the bulk carrier, whose CPA data indicated the more pressing risk.",
        "affected_reasoning_operation": "Probability/risk estimation and attention allocation across concurrent contacts",
        "evidence_available_at_time": [
          "Recalled bulletin narrative describing a similar fog/fishing-cluster near-miss at the same waypoint",
          "Current radar plot showing fishing cluster spacing and bearing drift not yet indicating high closing rate",
          "Bulk carrier's tightening CPA data"
        ],
        "required_textual_manifestation": "OOW explains the shift in attention toward the fishing cluster primarily by reference to how similar the situation felt to the recalled incident, rather than by citing the cluster's own plotted numbers, while the bulk carrier's tightening CPA is mentioned as secondary or noticed late.",
        "plausible_nonbias_interpretation": "Drawing on a recent, relevant safety bulletin about the same waypoint is a legitimate use of institutional learning and precaution, not necessarily a distortion of current risk assessment.",
        "strength": "moderate",
        "do_not_make_explicit": ["availability bias", "availability heuristic", "recency effect"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: condition is biased, not a control condition."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence/absence and vividness of the recent company safety bulletin describing a near-miss at the same waypoint (autoselected as the most causally testable factor for a future counterfactual pairing)",
      "original_state": "Bulletin exists and is vivid/recently discussed, shaping the OOW's risk estimate at Decision Point 3",
      "counterfactual_state": "No such bulletin exists or was never discussed on board; OOW must estimate cluster risk purely from current plotted data",
      "variables_to_hold_constant": [
        "Vessel type and passage route",
        "Weather sequence (squall timing and severity)",
        "Contact set and their kinematics (fishing boat, fishing cluster, bulk carrier)",
        "Watch composition and workload",
        "Decision count and structure"
      ],
      "expected_causal_difference": "Without the bulletin, attention allocation at Decision Point 3 should track the bulk carrier's tightening CPA more directly, since the fishing cluster no longer benefits from anecdotal salience.",
      "causal_test_question": "Does the OOW's attention shift toward the fishing cluster depend on the recalled bulletin narrative rather than on the cluster's own plotted risk data?"
    },
    "generation_checks": [
      "Exactly 4 decision points are present, each with at least two alternatives.",
      "Automation Bias instance is confined to Decision Point 2; Availability Bias instance is confined to Decision Point 3.",
      "Decision Points 1 and 4 contain no intentionally planned bias instances.",
      "No bias terminology or psychological labels appear in timeline, probes, or intended actions.",
      "Each planned instance has a distinct evidence source and reasoning operation from any other instance.",
      "Scenario content and probe set are sized to fit 1,215-1,485 words without repetitive exposition.",
      "Consequences (safe passage of both contacts) do not by themselves confirm or refute whether either decision was biased."
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
