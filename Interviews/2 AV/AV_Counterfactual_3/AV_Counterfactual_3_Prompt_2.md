You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "AV_Counterfactual_3",
  "domain_id": "AV",
  "domain": "Aviation",
  "role": "Load Controller / Loadmaster (Commercial)",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "Late Reload and Trim Discrepancy on a Compressed Narrow-Body Turnaround",
    "scenario_summary_internal": "This is the causal-variable counterfactual pairing of AV_Biased_3. The incident, cargo mix, LMC, rotation trim history, and final bag-count discrepancy are held materially constant. The single causal variable changed is the length of the turnaround window: instead of a routine 45-minute turnaround, an inbound delay compresses the ground time to approximately 30 minutes before the fixed departure slot. All other facts, actors, and the sequence of four decision points are preserved so that any difference in the load controller's reasoning can be attributed to the tighter time window rather than to a different incident. The same three intended bias instances are implemented at the same decision points as in the base scenario: automation bias at decision point 1 (accepting the automatically generated load instruction for atypical cargo without an independent manual cross-check), substitution bias at decision point 2 (using aggregate LMC weight similarity as a proxy for placement-specific index verification), and apophenia/correlation bias at decision point 3 (inferring a causal recurring trim pattern from two unrelated preceding events). Decision point 4 remains neutral and genuinely ambiguous.",
    "occupational_realism": {
      "objective": "Produce and sign off a compliant final load sheet (weight, balance, and CG within structural and CG envelope limits) before a fixed departure slot that now allows less buffer than usual, while correctly incorporating a non-standard cargo item and a late cargo addition.",
      "setting": "Regional hub airport ramp and load control office; ground time compressed to roughly 30 minutes because the inbound aircraft arrived late, on a narrow-body combi aircraft with belly holds 1-5.",
      "constraints": [
        "Compressed ~30-minute turnaround due to a delayed inbound aircraft, with the same fixed departure slot as originally scheduled",
        "Atypical, irregularly shaped machinery cargo requiring non-standard hold placement",
        "Late cargo/baggage change (LMC) received after the initial load instruction was generated",
        "Dangerous goods segregation and NOTOC accuracy requirements",
        "Structural per-hold and cumulative weight limits",
        "Reliance on a load-control software system (ALI generator) validated for standard palletized loads",
        "Heightened ramp crew and dispatcher time pressure relative to the base scenario, competing with verification thoroughness"
      ],
      "stakeholders": [
        "Load controller (interviewee)",
        "Ramp supervisor",
        "Ground handling agents",
        "Dispatcher / operations control",
        "Captain (recipient of NOTOC and final load sheet)"
      ],
      "technical_terms_to_use": [
        "load sheet", "weight and balance (W&B)", "center of gravity (CG)", "unit load device (ULD)",
        "automatic load instruction (ALI)", "last-minute change (LMC)", "NOTOC", "zero fuel weight (ZFW)",
        "trim sheet", "index units", "mean aerodynamic chord (MAC)", "bulk hold", "closeout figures"
      ],
      "technical_terms_to_avoid": [
        "automation bias", "substitution bias", "apophenia", "correlation bias", "heuristic",
        "cognitive bias", "anchoring", "pattern recognition error"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Inbound delay has compressed ground time to about 30 minutes, less than the usual 45",
          "Load-control software has generated a correct ALI for this fleet type over many months",
          "An irregularly shaped machinery cargo item (heavier and non-palletized) has been assigned to hold 3 by the ALI",
          "Ramp crew is waiting, now with less buffer than usual, for the final hold assignment"
        ],
        "new_information_after_decision": [
          "Ramp later reports the aircraft trimming slightly tail-heavy after loading per the ALI-assigned placement"
        ],
        "alternatives": [
          "Accept the automatically generated ALI as-is and issue loading instructions immediately given the shorter window",
          "Independently cross-check the ALI's hold assignment for the irregular machinery item against the manual structural limits chart before issuing instructions"
        ],
        "intended_action": "Loadmaster accepts the ALI output without the independent manual cross-check specifically indicated for non-standard/irregular cargo, citing the system's long track record of accuracy and the now-tighter schedule."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "An LMC of approximately 380kg of mail plus 6 late bags arrives after the initial load sheet was drafted, with even less time remaining than in a normal turn",
          "The mail is assigned to aft hold 5, a smaller hold not typically used for this route's routine LMCs",
          "The past three flights this week had LMCs of comparable total weight that did not require redistribution"
        ],
        "new_information_after_decision": [
          "The specific aft placement in hold 5 produces a larger index/moment shift than prior weeks' LMCs, which were placed forward"
        ],
        "alternatives": [
          "Run a full recalculation of the index/moment shift specific to placing this LMC in hold 5",
          "Judge the LMC acceptable based on its total weight being similar to this week's routine LMCs, without checking placement-specific index impact"
        ],
        "intended_action": "Loadmaster judges the LMC acceptable primarily because its aggregate weight resembles this week's typical LMCs, without independently verifying the placement-specific index effect of the aft hold assignment, under greater time constraint than the base scenario."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Dispatch log shows the previous two flights on this aircraft rotation (different tail numbers, one to a different destination) required aft trim adjustments",
          "This flight's own computed index, based on its actual load configuration, falls within the normal forward range",
          "Very little time remains before the trim sheet must be finalized given the compressed window"
        ],
        "new_information_after_decision": [
          "The two prior tail-heavy events are later attributed to unrelated causes: one to a fuel imbalance, the other to additional catering load, not a rotation-wide pattern"
        ],
        "alternatives": [
          "Base the trim sheet strictly on this flight's own computed index and load configuration",
          "Pre-emptively shift cargo distribution forward because the same rotation trended tail-heavy on the two preceding flights"
        ],
        "intended_action": "Loadmaster pre-emptively redistributes cargo forward based on an inferred recurring 'tail-heavy rotation' pattern drawn from two unrelated preceding events, rather than relying on this flight's own within-limits computed index, reasoning that there is no time left to investigate further."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Closeout figures appear balanced and within limits under the current load sheet",
          "A minor discrepancy of one bag count is noted between the ramp tally and the NOTOC/baggage manifest",
          "The compressed departure slot window is closing faster than usual, and holding for re-verification risks a delay"
        ],
        "new_information_after_decision": [
          "The bag-count discrepancy is resolved shortly after release, either matching a clerical miscount or requiring a minor manifest correction, without changing the overall weight and balance conclusion"
        ],
        "alternatives": [
          "Sign and release the final load sheet with the current closeout figures",
          "Request a short hold to re-verify the closeout figures and bag count against the NOTOC before final sign-off"
        ],
        "intended_action": "Loadmaster weighs the operational cost of a short hold, now more costly given the compressed schedule, against the apparent minor nature of the discrepancy, and makes a judgment call; no intended bias is embedded here, and either choice remains professionally defensible."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and what this particular turnaround looked like compared to a typical one?",
        "Walk me through what changed when you learned the ground time would be shorter than planned."
      ],
      "timeline_reconstruction": [
        "What was the first piece of information you received about the cargo mix for this flight?",
        "When did the last-minute change come in, and how did the shorter window affect how you handled it?",
        "What did the trim history for this rotation look like leading up to this flight?",
        "What happened right before you finalized and signed the load sheet, given how little time was left?"
      ],
      "decision_point_probes": [
        "What specific cues told you the automated load instruction was ready to use as generated, especially with less time available?",
        "What information sources did you consult when the mail and late bags came in, and what did you rely on most under that time constraint?",
        "What was your goal when you decided to adjust the cargo distribution forward before finalizing the trim sheet?",
        "What alternatives did you consider at each of these points, and did the shorter window change which alternative felt realistic?",
        "How much time pressure were you under at each of these moments compared to a normal turn, and how did that affect your approach?",
        "How confident were you in each of these judgments at the time, versus after the fact?",
        "Had you seen similar situations before in your experience, and how did that shape your response this time?"
      ],
      "closing_hypotheticals": [
        "If you had had the full 45 minutes instead of 30, do you think you would have handled the machinery cargo differently?",
        "If the LMC mail had been placed in the usual forward hold instead of hold 5, would your assessment have differed?",
        "Looking back, if you had known the two prior tail-heavy events had unrelated causes, would you have redistributed the cargo the same way?",
        "What would you do differently if you faced this exact sequence of events again, with the same shortened window?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "au_01",
        "bias": "Automaticity or Automation Bias",
        "decision_point": 1,
        "mechanism": "Over-reliance on the automatically generated ALI for an atypical, irregularly shaped machinery cargo item, treating the system's general track record on standard palletized loads as sufficient justification to skip the manual cross-check specifically indicated for non-standard cargo, now reinforced by the compressed schedule.",
        "affected_reasoning_operation": "Verification/checking of a system-generated output before acting on it",
        "evidence_available_at_time": [
          "System's consistent accuracy over months on standard loads",
          "Awareness that this cargo item is irregular and non-standard",
          "Heightened time pressure from the compressed ~30-minute turnaround"
        ],
        "required_textual_manifestation": "Loadmaster explicitly cites the system's past reliability and the shorter window as reasons for not independently checking the hold assignment for the atypical item, despite acknowledging its non-standard nature.",
        "plausible_nonbias_interpretation": "Reasonable trust in a validated tool under an unusually tight schedule, consistent with normal operational triage when time is scarce.",
        "strength": "subtle",
        "do_not_make_explicit": ["automation bias", "over-reliance", "system trust heuristic"]
      },
      {
        "instance_id": "sub_01",
        "bias": "Substitution bias",
        "decision_point": 2,
        "mechanism": "Replacing the harder question ('what precise index/moment shift does this specific LMC placement in hold 5 produce') with an easier proxy question ('does this LMC's total weight resemble this week's routine LMCs'), and treating the proxy answer as resolving the original question, under greater time scarcity than the base scenario.",
        "affected_reasoning_operation": "Evaluation of whether a new piece of evidence (the LMC) requires a full recalculation",
        "evidence_available_at_time": [
          "Total weight of the new LMC (~380kg plus 6 bags)",
          "Historical pattern of similar-weight LMCs this week",
          "Fact that this LMC's hold placement (aft, hold 5) differs from prior LMCs (forward holds)"
        ],
        "required_textual_manifestation": "Loadmaster states or implies that the LMC was judged acceptable mainly by comparing its total weight to past LMCs, without describing a placement-specific index check for hold 5, and references the shorter window as part of the justification.",
        "plausible_nonbias_interpretation": "A reasonable use of pattern-based experience to triage low-risk changes under unusually tight time pressure, when weight similarity is genuinely informative in most cases.",
        "strength": "subtle",
        "do_not_make_explicit": ["substitution bias", "proxy question", "attribute substitution"]
      },
      {
        "instance_id": "ap_01",
        "bias": "Apophenia or Correlation Bias",
        "decision_point": 3,
        "mechanism": "Inferring a causal, recurring 'tail-heavy rotation' pattern from two temporally adjacent but causally unrelated trim events on different tail numbers, and using that inferred pattern to override this flight's own within-limits computed index, with the compressed schedule cited as the reason further investigation was skipped.",
        "affected_reasoning_operation": "Causal attribution and generalization from a small, coincidental sample to guide a current decision",
        "evidence_available_at_time": [
          "Two prior flights on the same rotation logged aft trim adjustments",
          "Those two flights differed in tail number and one differed in destination",
          "This flight's own index, computed from its actual load, was within normal forward range"
        ],
        "required_textual_manifestation": "Loadmaster explains the pre-emptive forward redistribution by referencing the rotation's recent trim history as if it were a causal or recurring property of the rotation, rather than treating the two events as potentially coincidental, and notes there was no time left to check further.",
        "plausible_nonbias_interpretation": "A cautious, experience-based safety margin applied given recent operational history and limited time, which is a defensible judgment call absent further information.",
        "strength": "subtle",
        "do_not_make_explicit": ["apophenia", "correlation bias", "illusory pattern", "small sample"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "AV_Biased_3",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: this is a counterfactual pairing, not a vocabulary or ambiguous control."
    },
    "counterfactual_specification": {
      "causal_variable": "Length of the turnaround window before the fixed departure slot",
      "original_state": "A routine 45-minute turnaround with no additional schedule compression (as in AV_Biased_3)",
      "counterfactual_state": "A compressed ~30-minute turnaround caused by a delayed inbound aircraft, with the same fixed departure slot",
      "variables_to_hold_constant": [
        "Cargo mix and weights, including the irregular machinery item",
        "LMC content, weight, and hold placement",
        "Rotation trim history and its two prior unrelated causes",
        "Aircraft type and route",
        "Actors and stakeholder roles",
        "ALI system behavior and its lack of a mandatory manual-check flag",
        "The final bag-count discrepancy and its resolution"
      ],
      "expected_causal_difference": "The same three reasoning patterns (automation reliance, weight-based proxy judgment, and unrelated-event pattern inference) are expected to persist, but should be framed more explicitly around time scarcity as the stated justification, testing whether the same bias mechanisms are attributed mainly to the shorter window rather than disappearing under greater pressure.",
      "causal_test_question": "Does compressing the turnaround from 45 to 30 minutes change how strongly the load controller invokes time pressure as the reason for the same three reasoning shortcuts, without changing whether those shortcuts occur?"
    },
    "generation_checks": [
      "Exactly 3 total intended bias instances planned, matching the manifest sum (1+1+1)",
      "Exactly 4 decision points defined, each with at least two alternatives",
      "Each bias instance assigned to a distinct decision point (DP1, DP2, DP3), matching the base scenario's assignment; DP4 left intentionally neutral/ambiguous",
      "Only the turnaround-window variable and its direct time-pressure framing differ from AV_Biased_3; all other material facts are held constant",
      "No bias terminology or psychological labels appear in probe plan or timeline text",
      "Each instance has a plausible non-bias interpretation distinct from its intended mechanism",
      "Decision point 4 contains no intended bias instance and has a genuinely ambiguous, non-mechanical outcome",
      "Target word count (1,215-1,485 words) is achievable given four decision points with probes, without repetitive exposition"
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
