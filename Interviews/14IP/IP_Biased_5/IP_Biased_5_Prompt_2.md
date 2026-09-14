You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IP_Biased_5",
  "domain_id": "IP",
  "domain": "Industrial Production Processes",
  "role": "Plant/Industrial Production Manager",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Line 3 Flash Defect Spike Before the Meridian Shipment",
    "scenario_summary_internal": "A plant manager at a mid-size injection molding facility must diagnose and correct a sudden rise in flash/short-shot defects on Line 3 in the four days before a large customer (Meridian Automotive) shipment deadline. The manager must balance throughput, scrap cost, and quality risk while under time pressure, incomplete sensor data, and pressure from corporate and sister-plant precedent. The narrative follows four sequential decision points: initial root-cause diagnosis, selection of a corrective fix, adoption of a plant-wide standard proposed by peers, and the final call to scale the fix to two additional lines before shipment.",
    "occupational_realism": {
      "objective": "Restore Line 3 output to spec-compliant quality (scrap rate back under 2%) in time to fulfill the Meridian shipment without triggering a full line shutdown or missing the ship date.",
      "setting": "A 24/7 mid-size automotive-parts injection molding plant running three shifts, with a quality lab, a maintenance/tooling team, and a corporate quality network linking four sister plants.",
      "constraints": [
        "72-hour window before the Meridian shipment must ship",
        "Limited access to the sister plant's full defect log, only a summary shared in a call",
        "Tooling change requires a scheduled press-down window shared with two other product runs",
        "Quality engineer is out sick during the second day, reducing statistical support",
        "Corporate directive discourages full-line shutdowns without VP sign-off"
      ],
      "stakeholders": [
        "Plant/Industrial Production Manager (interviewee)",
        "Shift supervisors (Shift A, B, C)",
        "Quality engineer",
        "Tooling/maintenance lead",
        "Sister-plant production manager (peer)",
        "Corporate quality director",
        "Meridian Automotive account representative"
      ],
      "technical_terms_to_use": [
        "flash defect",
        "short shot",
        "cycle time",
        "scrap rate",
        "mold cavity pressure",
        "resin lot",
        "tooling wear",
        "SPC chart",
        "press-down window",
        "hold pressure"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "anchoring",
        "availability heuristic",
        "bandwagon",
        "overconfidence",
        "recency effect",
        "heuristic",
        "psychological"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Scrap rate on Line 3 jumped from 1.8% to 6.4% over the last 12-hour shift",
          "SPC chart shows a cavity-pressure drift starting mid-shift",
          "Six months earlier, a nearly identical defect pattern was traced to ambient humidity affecting resin drying",
          "Current humidity readings are within normal range and have not been checked yet"
        ],
        "new_information_after_decision": [
          "Humidity logs come back normal, ruling out the prior cause",
          "Tooling lead flags that the mold has accumulated wear cycles since the last inspection"
        ],
        "alternatives": [
          "Order an immediate humidity/resin-drying check based on the prior incident pattern",
          "Pull current cavity-pressure and tooling-wear data before assuming a cause",
          "Run a short diagnostic mold-inspection alongside a parallel resin check"
        ],
        "intended_action": "Manager directs the team to first re-check drying/humidity conditions because 'this looks just like the case from six months ago,' delaying the tooling-wear check."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Tooling wear confirmed as a contributing factor; wear is moderate, not severe",
          "Two candidate fixes exist: incremental hold-pressure adjustment (lower risk, slower to validate) or a full mold-insert swap (faster perceived fix, requires press-down window)",
          "Three months ago, a widely discussed insert failure on Line 5 caused a two-day shutdown and was the subject of a plant-wide safety debrief that is still fresh in staff conversation"
        ],
        "new_information_after_decision": [
          "The insert swap is completed within the available press-down window",
          "Early results show partial improvement but scrap rate does not fully return to baseline"
        ],
        "alternatives": [
          "Choose the insert swap, citing the memorable Line 5 case as the reason for urgency",
          "Choose the incremental hold-pressure adjustment and monitor over several cycles",
          "Run both a small-scale hold-pressure trial and schedule the swap as a contingency"
        ],
        "intended_action": "Manager selects the full insert swap, explaining the decision mainly by referencing how vividly the Line 5 insert failure is remembered by the team, rather than by comparing current wear severity data against swap thresholds."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A call with the sister-plant manager reveals that three of the four sister plants adopted a standardized 'aggressive cooling time reduction' protocol for similar flash issues",
          "The plant's own quality engineer (now back) has not yet independently validated whether cooling-time reduction fits Line 3's specific resin lot and cavity geometry",
          "Corporate quality director mentions the protocol is becoming the informal network standard"
        ],
        "new_information_after_decision": [
          "Applying the cooling-time reduction produces a short-term drop in flash defects",
          "A new, unrelated warping issue emerges on a subset of parts two shifts later"
        ],
        "alternatives": [
          "Adopt the cooling-time reduction protocol because most sister plants are already using it",
          "Request the quality engineer validate the protocol against Line 3's specific resin lot before adopting",
          "Adopt a modified, more conservative version of the protocol pending local validation"
        ],
        "intended_action": "Manager adopts the sister-plant protocol largely because it is already the shared practice across the network, without waiting for the quality engineer's line-specific validation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The most recent shift (last 8 hours) shows scrap rate down to 1.5%, the best reading in four days",
          "The full four-day trend, including the warping issue from phase 3, is more mixed and shows only 2.9% average improvement with unresolved variability",
          "Meridian shipment must be finalized within hours, and the corporate quality director is asking whether the fix should be rolled out to Lines 4 and 6"
        ],
        "new_information_after_decision": [
          "Lines 4 and 6 initially show improvement, but one line later reports a new tooling alarm not previously seen",
          "A fuller week-long data review shows the underlying wear-related root cause was only partially addressed"
        ],
        "alternatives": [
          "Approve immediate rollout to Lines 4 and 6 based on the strong latest-shift numbers",
          "Request one more full day of Line 3 data across all shifts before recommending rollout",
          "Approve a limited pilot rollout to one additional line with added monitoring"
        ],
        "intended_action": "Manager expresses high confidence that the root cause is fully resolved and approves rollout to both additional lines, citing the strong last-shift numbers as sufficient proof, while downplaying the more mixed multi-day trend and the earlier warping incident."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what first indicated something was wrong on Line 3?",
        "What was your primary objective when you were first notified?"
      ],
      "timeline_reconstruction": [
        "What happened right after you were told about the scrap rate spike?",
        "Walk me through the sequence of checks, calls, and decisions over the four days.",
        "What information came in after each major decision, and how did it change things?"
      ],
      "decision_point_probes": [
        "At that moment, what options did you consider, and why did you rule the others out?",
        "What evidence or past experience were you drawing on when you made that call?",
        "Who else was involved, and how much did their input shape your decision?",
        "Looking back, what information did you have available that you didn't use, or used less than others?"
      ],
      "closing_hypotheticals": [
        "If the sister plants had not shared their protocol, would your approach have been different?",
        "If the last shift's numbers had looked worse instead of better, would you have made the same rollout call?",
        "What would you do differently if a similar defect spike happened again next quarter?",
        "How much uncertainty did you feel you were operating under at each stage, in hindsight?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Initial diagnostic hypothesis is fixed on the six-month-old humidity/resin-drying cause because of surface similarity, and subsequent inquiry is organized around confirming or ruling out that anchor before considering other current evidence (tooling wear) already partially available.",
        "affected_reasoning_operation": "Initial hypothesis formation and information-gathering sequencing",
        "evidence_available_at_time": [
          "SPC cavity-pressure drift data",
          "Prior six-month-old humidity-related incident",
          "Untouched current humidity readings"
        ],
        "required_textual_manifestation": "Manager states the pattern 'looks just like' the earlier case and orders the humidity check first, delaying the tooling-wear check despite pressure data being available.",
        "plausible_nonbias_interpretation": "Checking a known prior cause first is a reasonable triage step given limited time.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchoring", "cognitive bias", "heuristic"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Heuristic",
        "decision_point": 2,
        "mechanism": "The choice of corrective fix is driven by how memorable and recently-discussed the Line 5 insert failure is, rather than by comparing current wear-severity data against objective swap-versus-adjustment thresholds.",
        "affected_reasoning_operation": "Option evaluation and justification for corrective action",
        "evidence_available_at_time": [
          "Confirmed moderate (not severe) tooling wear",
          "Two candidate fixes with different risk/time profiles",
          "Recent, widely-discussed Line 5 insert failure and debrief"
        ],
        "required_textual_manifestation": "Manager justifies choosing the full insert swap primarily by referencing how vivid and recent the Line 5 case is in staff memory, rather than citing wear-severity thresholds.",
        "plausible_nonbias_interpretation": "Choosing the faster, more thorough fix is a reasonable risk-averse choice given schedule pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "cognitive bias", "vividness"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Bandwagon effect",
        "decision_point": 3,
        "mechanism": "Adoption of the cooling-time reduction protocol is driven mainly by the fact that most sister plants and the corporate network already treat it as standard practice, ahead of the plant's own line-specific validation being completed.",
        "affected_reasoning_operation": "Selection of a corrective standard/protocol under social/organizational consensus",
        "evidence_available_at_time": [
          "Sister-plant adoption reported by peer manager",
          "Corporate framing of protocol as emerging network standard",
          "Quality engineer's validation not yet completed"
        ],
        "required_textual_manifestation": "Manager cites the fact that three of four sister plants already use the protocol as the main reason for adopting it now, ahead of local validation.",
        "plausible_nonbias_interpretation": "Leveraging proven practice from sister plants is a legitimate way to save diagnostic time under a deadline.",
        "strength": "moderate",
        "do_not_make_explicit": ["bandwagon", "social proof", "cognitive bias"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Recency effect",
        "decision_point": 4,
        "mechanism": "The rollout decision is disproportionately weighted toward the most recent 8-hour shift's strong numbers, while the more mixed four-day trend, including the intervening warping issue, is discounted in the manager's stated reasoning.",
        "affected_reasoning_operation": "Weighting of sequential performance data when forming a judgment of resolution",
        "evidence_available_at_time": [
          "Most recent shift's low scrap rate (1.5%)",
          "Four-day trend showing mixed results (2.9% average, unresolved variability)",
          "Prior warping incident from phase 3"
        ],
        "required_textual_manifestation": "Manager foregrounds the latest shift's numbers as the key evidence for resolution while giving comparatively little weight to the multi-day trend and the warping incident when explaining the basis for the decision.",
        "plausible_nonbias_interpretation": "The latest shift is the freshest and most direct evidence of whether the fix is working.",
        "strength": "subtle",
        "do_not_make_explicit": ["recency effect", "cognitive bias", "weighting"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "The manager expresses high certainty that the root cause is fully resolved and approves rollout to two additional lines, exceeding what the available multi-day, multi-line evidence supports, and without acknowledging the earlier partial-improvement and warping signals as sources of uncertainty.",
        "affected_reasoning_operation": "Confidence calibration in final causal judgment and generalization decision",
        "evidence_available_at_time": [
          "Partial improvement noted after the insert swap (phase 2)",
          "Warping issue emerging after protocol adoption (phase 3)",
          "Only one strong shift of data supporting full resolution"
        ],
        "required_textual_manifestation": "Manager states strong certainty ('this has fully resolved it') and approves rollout to both additional lines without qualifying the claim against the mixed evidence already known at that point.",
        "plausible_nonbias_interpretation": "A production manager under deadline pressure may reasonably need to make a decisive call with available data.",
        "strength": "moderate",
        "do_not_make_explicit": ["overconfidence", "cognitive bias", "calibration"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a biased-condition scenario with no paired control specified in this request."
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
      "Verify exactly 5 total intended bias instances are embedded, one per manifest entry.",
      "Verify each instance is tied to a distinct decision point and evidence source, with cb_04 and cb_05 both at decision point 4 but drawing on different evidence operations (trend-weighting vs. confidence calibration).",
      "Verify no bias name, definition, or psychological label appears in probes or narrative text.",
      "Verify exactly four decision points, each with at least two plausible alternatives.",
      "Verify consequences at each decision point do not mechanically confirm or deny whether the decision was biased.",
      "Verify total narrative length target of 1,350 words (range 1,215-1,485) is achievable without repetitive exposition, given four decision points and moderate probe density.",
      "Verify probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypothetical changes."
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
