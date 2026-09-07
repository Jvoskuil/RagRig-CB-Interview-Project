You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "MO_Ambigious_7",
  "domain_id": "MO",
  "domain": "Maritime Operations",
  "role": "Dynamic Positioning Operator (Offshore Support Vessel)",
  "condition": "ambiguous_control",
  "generation_specification": {
    "scenario_title_internal": "Reference Drift During Cargo Transfer at North Sea Platform (Ambiguous Control)",
    "scenario_summary_internal": "Paired ambiguous-control counterpart to MO_Biased_7. A DPO aboard the same class of DP2 offshore support vessel conducts a scheduled cargo transfer alongside a fixed platform under a closing weather window, encountering the same four structural decision points: a reference-system discrepancy on approach, a thruster caution mid-transfer, a late environmental cue during the final lift, and an OIM query about finishing the last lift. In this version, each decision is genuinely underdetermined: the available evidence supports more than one reasonable course of action, the DPO's stated reasoning references defensible operational heuristics and workload constraints, and no decision is driven by selective evidence weighting, automated deference, attentional fixation, sunk-cost justification, default preservation, or a skewed decision frame. The incident still ends as a near-miss with an early suspension of the final lift, preserving outcome ambiguity so that the sequence cannot be judged biased or unbiased purely from its result.",
    "occupational_realism": {
      "objective": "Complete a scheduled cargo transfer of deck cargo and bulk material from the OSV to a fixed offshore platform under DP2 station-keeping, within a forecast weather window, without breaching safe approach distance or DP capability limits.",
      "setting": "North Sea fixed platform, DP2-class offshore support vessel on standby/cargo-transfer duty, daylight, forecast deteriorating sea state (rising from 2.5m to 3.5m Hs) over a 4-hour window, cargo crane operations alongside the platform leg.",
      "constraints": [
        "Closing weather window before conditions exceed platform crane operating limits",
        "Limited remaining vessel time on charter before transit to next location",
        "DP2 redundancy requirement (loss of one reference system must not compromise position-keeping)",
        "Crew fatigue from an extended shift",
        "Communication lag between crane operator, platform OIM, and bridge team"
      ],
      "stakeholders": [
        "Dynamic Positioning Operator (interviewee)",
        "Master / DP2 co-operator",
        "Platform Installation Manager (OIM)",
        "Crane operator",
        "Vessel superintendent (shore-based, schedule pressure)"
      ],
      "technical_terms_to_use": [
        "DP2 redundancy concept",
        "reference system (DGPS, HPR, laser/Fanbeam)",
        "footprint plot",
        "consequence analysis",
        "thruster caution alarm",
        "green/yellow/red DP status",
        "safe working envelope",
        "watch circle",
        "weather window"
      ],
      "technical_terms_to_avoid": [
        "confirmation bias",
        "automation bias",
        "inattentional blindness",
        "hindsight bias",
        "sunk cost",
        "status quo bias",
        "framing effect",
        "any explicit bias or heuristic terminology"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "DGPS1 and HPR show a 1.7m position discrepancy during final approach",
          "DGPS2 agrees closely with DGPS1",
          "DP system auto-selected DGPS1/DGPS2 as the weighted reference pair, showing overall GREEN status",
          "HPR has a minor, previously logged intermittent fault history from a prior voyage, since cleared but not re-certified"
        ],
        "new_information_after_decision": [
          "HPR discrepancy is later attributed to a plausible combination of the prior intermittent fault history and structural multipath near the platform, with no single definitive cause identified",
          "The discrepancy trend remains within the DP2 alert threshold throughout the approach"
        ],
        "alternatives": [
          "Accept the DP system's auto-weighted reference pair, noting HPR's own uncertain fault history as a reason to deprioritize it",
          "Pause briefly to manually query HPR's fault log and current diagnostic state before closing distance"
        ],
        "intended_action": "DPO cross-references HPR's known intermittent fault history against the current discrepancy, reasonably concludes that a previously flagged reference carries more uncertainty than two freshly agreeing units, and proceeds while noting the ambiguity for the log rather than treating it as fully resolved."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Approximately 55% of cargo has been transferred; two lifts remain",
          "Thruster 3 shows a yellow caution for reduced power availability",
          "DP consequence analysis shows adequate capability with the caution active, but with reduced margin compared to the start of the job",
          "Weather forecast confirms Hs will exceed platform crane limits within roughly 70 minutes",
          "A conservative mode change would add an estimated 20-25 minutes to remaining completion time"
        ],
        "new_information_after_decision": [
          "Thruster 3 caution persists at a stable but unresolved severity through the remaining transfer",
          "The added time cost of a conservative mode change is later confirmed to have been a reasonable estimate, making the original trade-off assessment defensible in retrospect"
        ],
        "alternatives": [
          "Suspend the transfer, move to standby distance, and reassess DP capability before continuing",
          "Switch to a more conservative operating mode at the cost of additional time within the closing weather window",
          "Continue the transfer at the current pace, citing the consequence analysis and the time cost of switching modes"
        ],
        "intended_action": "DPO weighs the consequence analysis result against the time cost of switching to a more conservative mode within the specific closing weather window, and continues at current pace, explicitly citing the capability margin rather than the amount of cargo already completed as the deciding factor."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "DPO's attention is concentrated on the crane boom position display during the final lift, per the vessel's standard lift-monitoring procedure",
          "A new wind-shift alert changes the vessel's heading/footprint recommendation on the DP plot",
          "The environmental sensor trend line has shifted for roughly 90 seconds prior to the lift's completion",
          "The co-operator is occupied at that moment with a separate radio exchange confirming the next lift's rigging status"
        ],
        "new_information_after_decision": [
          "The wind shift is confirmed moments later by the Master, who notices the vessel's heel/attitude change",
          "Review shows both the crane task and the radio exchange were legitimate concurrent demands on the two-person bridge team at that moment"
        ],
        "alternatives": [
          "Interrupt the co-operator's radio exchange to reassign footprint monitoring during the final lift",
          "Rely on the standard procedure of prioritizing crane-boom monitoring during an active lift, with footprint checks resuming immediately after",
          "Pause the lift briefly to allow a full instrument scan before continuing"
        ],
        "intended_action": "DPO follows the standard procedure of prioritizing crane-boom monitoring during the active lift while the co-operator is legitimately occupied with a concurrent rigging confirmation, resulting in a short delay before the wind shift is registered, consistent with normal two-person workload division rather than a fixed or evidence-driven pattern."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "One final, smaller lift remains, estimated at 8-10 minutes",
          "Wind and swell have increased since Phase 3, narrowing the safe working envelope",
          "Thruster 3 caution and the earlier reference discrepancy are both still present but not escalated to red/alarm status",
          "OIM asks whether the vessel can finish the last lift or should stand off",
          "DPO has both the time estimate and the current separation/capability readout available on adjacent display panels"
        ],
        "new_information_after_decision": [
          "The vessel's separation from the platform decreases more than expected during the final maneuvering, prompting an early suspension of the lift",
          "Post-event review shows the margin readout and the time estimate were both consulted, but the margin trend accelerated faster than either figure had indicated at the moment of decision"
        ],
        "alternatives": [
          "Suspend the final lift now given the narrowing envelope",
          "Complete the final lift after checking both the time estimate and the current margin readout, judging the margin still adequate for the estimated duration"
        ],
        "intended_action": "DPO reviews both the completion-time estimate and the current separation/capability readout, judges the margin adequate for the short remaining duration, and elects to proceed with the final lift before conditions force an early suspension when the margin narrows faster than anticipated."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe your role and responsibilities during this cargo transfer operation.",
        "Walk me through what a routine transfer alongside this platform normally looks like."
      ],
      "timeline_reconstruction": [
        "Take me through the operation from approach to the final lift, in the order things happened.",
        "What were you monitoring at each stage, and how did that change as the job progressed?"
      ],
      "decision_point_probes": [
        "At the point where the reference systems disagreed, what information did you use to decide which was correct?",
        "What made you comfortable continuing the transfer once the thruster caution appeared?",
        "What were you focused on during the final lift, and how did you become aware of the wind shift?",
        "When the OIM asked about finishing the last lift, what factors did you weigh in your answer?",
        "What alternatives did you consider at each of these points, and why did you rule them out?"
      ],
      "closing_hypotheticals": [
        "If the HPR discrepancy had appeared without any prior fault history, would your approach have differed?",
        "Looking back, do you think there were earlier indications of the eventual close approach to the platform, or does it look that way mainly because of how it ended?",
        "If you were advising a newer DPO facing a similar sequence, what would you tell them to watch for?",
        "What, if anything, would you do differently if this situation arose again?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "MO_Biased_7",
      "features_to_match": [
        "Same DP2 vessel class, platform setting, and closing weather window",
        "Same four-decision-point chronology: reference discrepancy, thruster caution, missed footprint cue, OIM final-lift query",
        "Same stakeholders, technical vocabulary, difficulty, and near-miss outcome structure",
        "Same emotional tone (measured, professional, moderate time pressure) and interview probe structure"
      ],
      "features_to_remove_or_change": [
        "Remove selective reliance on agreeing references as confirmation of a pre-existing view; replace with an explicit, defensible fault-history-based justification for deprioritizing HPR",
        "Remove deference to automated GREEN status alone as the stated reason for inaction; replace with reasoning that references the underlying diagnostic data directly",
        "Remove reliance on cargo/time already invested as the stated reason to continue after the thruster caution; replace with a forward-looking capability-versus-time-cost trade-off",
        "Remove default retention of configuration without comparison; replace with an explicit, reasoned comparison that still results in continuing",
        "Remove attentional fixation on the crane display as an unexplained default; replace with a stated, procedure-based workload allocation between two occupied bridge personnel",
        "Remove framing of the final decision purely around time; replace with an account showing both time and margin figures were consulted",
        "Remove retrospective overstatement of foreseeability; replace with a hypothetical answer that explicitly questions whether the pattern was really foreseeable at the time or only appears so in retrospect"
      ],
      "ambiguity_boundary": "Each decision point must remain genuinely underdetermined: the DPO's account should show real information gaps, competing legitimate priorities, or reasonable trade-offs, such that a reader cannot confidently classify the reasoning as biased or as optimally rational. Do not resolve the ambiguity toward either a clearly biased pattern or an artificially perfect textbook decision process; avoid contrived neutrality where the DPO recites all alternatives mechanically without genuine trade-off tension."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable - ambiguous_control condition does not implement a counterfactual manipulation",
      "original_state": "N/A",
      "counterfactual_state": "N/A",
      "variables_to_hold_constant": [],
      "expected_causal_difference": "N/A",
      "causal_test_question": "N/A"
    },
    "generation_checks": [
      "Confirm exactly 4 decision points, each with at least two plausible alternatives",
      "Confirm zero intended bias instances of any of the seven named biases",
      "Confirm each decision point contains genuine underdetermination with a stated non-bias justification that is at least as plausible as any bias-consistent reading",
      "Confirm no bias terminology, labels, or explanations appear in the public interview text",
      "Confirm structural parity with MO_Biased_7: same stakeholders, vocabulary, four-phase chronology, near-miss outcome ambiguity, and interview probe structure",
      "Confirm final word count falls between 1,215 and 1,485 words",
      "Confirm consequences described (near-approach, suspension) do not mechanically prove the presence or absence of biased reasoning",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Confirm the closing hypothetical explicitly surfaces the foreseeability question without the participant resolving it toward an inflated retrospective certainty"
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
