You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "HC_Counterfactual_5",
  "domain_id": "HC",
  "domain": "Healthcare",
  "role": "Physical Therapist with outpatients",
  "condition": "counterfactual",
  "generation_specification": {
    "scenario_title_internal": "The ACL Return-to-Sport Progression — Open Authorization Variant",
    "scenario_summary_internal": "A counterfactual variant of HC_Biased_5 in which the outpatient physical therapist manages the same 16-week-equivalent post-ACL-reconstruction rehab course for the same competitive amateur soccer player, but the insurer has approved an open-ended authorization with no fixed visit cap or hard expiration deadline. All clinical facts, personal history, session outcomes, and reasoning patterns are held constant; only the insurance-authorization constraint is changed. The same five reasoning distortions recur at the same four decision points, demonstrating that they are not artifacts of the authorization deadline.",
    "occupational_realism": {
      "objective": "Safely progress a post-surgical outpatient toward objective return-to-sport criteria while minimizing re-injury risk and meeting clinic productivity expectations, now without a hard insurance deadline forcing the pace.",
      "setting": "Outpatient orthopedic physical therapy clinic; primary patient is an amateur adult soccer player 8-16 weeks post-ACL reconstruction (hamstring autograft). The insurer has granted an open-ended authorization for this case rather than a capped visit count.",
      "constraints": [
        "Insurer has approved an open-ended authorization with no fixed visit cap or expiration deadline for this case",
        "Isokinetic dynamometer shared across the clinic and only available two days a week",
        "Clinic productivity targets requiring efficient visit throughput",
        "Patient's strong motivation to return to competitive play before season start",
        "Referring orthopedic surgeon requires periodic progress updates before sign-off"
      ],
      "stakeholders": [
        "Patient (adult recreational/competitive soccer player)",
        "Referring orthopedic surgeon",
        "Insurance case manager",
        "Clinic supervisor",
        "Treating physical therapist (interviewee)"
      ],
      "technical_terms_to_use": [
        "quadriceps strength index",
        "single-leg hop test symmetry index",
        "isokinetic dynamometer",
        "return-to-sport criteria",
        "plyometric progression",
        "closed-chain vs open-chain exercise",
        "graft maturation timeline",
        "patient-reported outcome measures (PROMs)",
        "functional movement screen",
        "open-ended authorization"
      ],
      "technical_terms_to_avoid": [
        "loss aversion",
        "framing effect",
        "gambler's fallacy",
        "base rate",
        "optimism bias",
        "risk tolerance",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Quadriceps strength index at 78% of uninvolved limb (typical progression threshold cited as 80-85%)",
          "No reported pain or effusion",
          "Physician clearance for advanced loading still pending written confirmation",
          "PT recalls a prior unrelated patient who re-tore a graft after early plyometric progression two years earlier",
          "No fixed visit cap is in play; the patient's own soccer-season timeline still motivates a reasonably prompt pace"
        ],
        "new_information_after_decision": [
          "Physician clearance arrives days later confirming no structural concerns",
          "Patient reports frustration at perceived slow pace relative to peers"
        ],
        "alternatives": [
          "Progress to modified closed-chain/plyometric loading now given absence of pain and near-threshold strength",
          "Hold at current loading level and reassess strength index in two weeks",
          "Progress partially with a reduced-intensity plyometric subset while monitoring"
        ],
        "intended_action": "PT elects to hold progression well beyond what the 78% index and pain-free status would typically justify, citing the earlier unrelated case as the primary reason rather than this patient's actual data, even though there is no authorization deadline forcing caution or urgency either way."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient has completed three consecutive sessions of pain-free single-leg hopping drills with steadily improving form",
          "No fatigue, swelling, or PROM decline reported",
          "Isokinetic dynamometer is available this week for a scheduled hop-symmetry test, though slots remain limited to two clinic days per week"
        ],
        "new_information_after_decision": [
          "Test is delayed a week; patient's fourth session also goes well with no setback",
          "The delay costs a scarce dynamometer slot but does not threaten any authorization deadline"
        ],
        "alternatives": [
          "Proceed with the scheduled single-leg hop test this week as planned",
          "Delay testing one additional week, reasoning the streak of good sessions makes a setback likely soon",
          "Run a modified, lower-load version of the test to hedge against an anticipated decline"
        ],
        "intended_action": "PT postpones the scheduled hop test, reasoning aloud that because the patient has had an unusually good run of sessions, a decline is 'due,' despite no clinical indicator of fatigue or regression and despite no expiring-authorization pressure to test promptly."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Patient has met roughly 85% of interim functional milestones and reports strong confidence",
          "Insurance case manager performs a routine utilization check-in and asks for a recommendation: continue supervised clinic visits or transition to a home exercise program",
          "Objective measures (PROMs, strength index) are within a range that could reasonably support either path",
          "No visit cap or deadline is pressing the decision either way"
        ],
        "new_information_after_decision": [
          "Case manager approves the PT's recommended path without further review",
          "Patient later expresses some anxiety about the framing used to justify continued in-clinic visits"
        ],
        "alternatives": [
          "Recommend transition to a structured home exercise program with periodic check-ins",
          "Recommend continued twice-weekly supervised clinic visits",
          "Recommend a tapered hybrid schedule reducing clinic frequency gradually"
        ],
        "intended_action": "PT frames the choice to the case manager and patient primarily around what would be lost by stopping clinic visits ('you'll lose the strength gains you've made') rather than presenting the equally valid gains of independence, and recommends continued clinic visits largely on that framing rather than a balanced read of the functional data, even though there is no expiring authorization creating urgency to decide one way."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Single-leg hop symmetry index reaches 88%, near the higher end of the typical return-to-sport threshold",
          "Quadriceps strength index at 91%",
          "PT recalls that this patient's numbers are among the best she has seen in her caseload this year",
          "Surgeon requests a discharge/return-to-sport recommendation",
          "No authorization deadline is forcing an early or rushed clearance decision"
        ],
        "new_information_after_decision": [
          "PT drafts the clearance summary and discusses expected outcome with the patient and surgeon",
          "Patient asks directly about the chance of re-injury upon returning to competitive play"
        ],
        "alternatives": [
          "Clear the patient for full return to competitive soccer based on her individual test scores",
          "Clear with a structured, sport-specific reconditioning phase and reinforced monitoring given known population-level re-injury patterns after ACL reconstruction",
          "Delay clearance pending an additional functional movement screen"
        ],
        "intended_action": "PT tells the patient she is very likely to return to play injury-free given how strong her individual numbers are, without incorporating the well-documented population-level second-injury incidence for athletes returning to pivoting sports after ACL reconstruction, and finalizes an unqualified clearance recommendation, despite having no deadline pressure to clear her quickly."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you describe your role and typical caseload in this clinic?",
        "Walk me through this particular patient's case from referral to discharge."
      ],
      "timeline_reconstruction": [
        "Take me through the treatment course week by week.",
        "What information did you have available at each check-in point?",
        "What changed in the patient's presentation between phases?"
      ],
      "decision_point_probes": [
        "What cues in the patient's presentation stood out to you at that point?",
        "What information sources did you rely on for that decision?",
        "What were you ultimately trying to achieve at that stage?",
        "What other options did you consider, and why did you rule them out?",
        "What was the main basis for the choice you made?",
        "Had you seen a similar situation before, and did that affect your thinking?",
        "Given there was no fixed visit cap here, did scheduling pressure factor into that call at all?",
        "How confident were you in the data you had at that point?",
        "If a key fact had been different, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "Given the open-ended authorization here, is there anything you'd have done differently if there had instead been a hard visit cap?",
        "If this had been a different sport or activity level, how might your recommendation differ?",
        "If you had earlier access to the isokinetic dynamometer, would that have changed your timeline?",
        "Looking back, what would you tell a colleague facing the same case?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Risk Tolerance/aversion",
        "decision_point": 1,
        "mechanism": "PT's progression decision is driven by an emotionally salient unrelated prior case rather than this patient's objective near-threshold strength index and absence of pain, producing caution disproportionate to actual clinical risk, and this persists even though no authorization deadline is forcing a particular pace.",
        "affected_reasoning_operation": "Risk-weighting of a progression decision under uncertainty",
        "evidence_available_at_time": [
          "78% quadriceps strength index, near typical progression threshold",
          "No pain or effusion",
          "Pending but expected physician clearance",
          "No fixed visit cap pressing the timeline"
        ],
        "required_textual_manifestation": "PT explicitly cites the unrelated prior patient's re-injury as the reason for holding progression, more than the current patient's own metrics, and notes the absence of deadline pressure did not change that reasoning.",
        "plausible_nonbias_interpretation": "A cautious clinician conservatively erring on the side of safety near a threshold value, which alone would be a defensible clinical judgment call rather than a distortion.",
        "strength": "subtle",
        "do_not_make_explicit": ["risk aversion", "risk tolerance", "bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Gambler's Fallacy",
        "decision_point": 2,
        "mechanism": "PT infers that a consecutive run of pain-free, well-performed sessions makes a decline 'due' or statistically likely soon, treating session-to-session outcomes as if they must balance out, independent of whether an authorization deadline exists.",
        "affected_reasoning_operation": "Prediction of near-term outcome from a short streak of independent-ish observations",
        "evidence_available_at_time": [
          "Three consecutive pain-free, improving hopping sessions",
          "No fatigue, swelling, or PROM decline reported",
          "No authorization deadline shortening the available window"
        ],
        "required_textual_manifestation": "PT states or implies that the good streak means a setback is 'due' and delays testing on that basis, absent any clinical fatigue indicator, and confirms the reasoning was not about the deadline.",
        "plausible_nonbias_interpretation": "A prudent clinician spacing out demanding tests to avoid overuse, which would be a legitimate load-management rationale rather than a distortion.",
        "strength": "subtle",
        "do_not_make_explicit": ["gambler's fallacy", "streak", "due for"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Loss/gain Framing effect",
        "decision_point": 3,
        "mechanism": "PT's recommendation to the case manager and patient is shaped by presenting the choice in terms of what will be lost by stopping clinic visits, rather than an equally valid gain-framed or neutral presentation, and this framing measurably tilts the recommendation despite ambiguous data and despite no expiring authorization forcing urgency.",
        "affected_reasoning_operation": "Formulation and communication of a recommendation under an ambiguous decision boundary",
        "evidence_available_at_time": [
          "~85% of interim functional milestones met",
          "PROMs and strength index within a range compatible with either path",
          "Routine utilization check-in, not a deadline-driven request"
        ],
        "required_textual_manifestation": "PT's own account shows she emphasized 'losing gains' language when recommending continued clinic visits, and this framing—not the ambiguous data or any deadline—is what she cites as driving the recommendation.",
        "plausible_nonbias_interpretation": "A clinician using motivational language to support adherence, which could be a legitimate communication technique rather than a distortion of the underlying decision.",
        "strength": "moderate",
        "do_not_make_explicit": ["framing effect", "loss frame", "gain frame"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Optimism Bias",
        "decision_point": 4,
        "mechanism": "PT projects a high personal likelihood of injury-free return specifically for this patient based on her individual test scores being 'among the best' she has seen, overestimating this particular patient's favorable outcome beyond what the test scores alone support, unrelated to any deadline pressure.",
        "affected_reasoning_operation": "Individual outcome prediction from personal comparative impression",
        "evidence_available_at_time": [
          "88% hop symmetry index, 91% strength index",
          "PT's subjective ranking of this patient against her own caseload",
          "No deadline forcing a rushed clearance"
        ],
        "required_textual_manifestation": "PT tells the patient she is 'very likely' to return injury-free, anchoring the confidence explicitly on how her numbers compare favorably to other patients the PT has personally treated, and acknowledges this went beyond what those scores alone could justify.",
        "plausible_nonbias_interpretation": "A clinician reasonably encouraged by strong objective test results, which alone would be a defensible read of good data.",
        "strength": "subtle",
        "do_not_make_explicit": ["optimism bias", "overconfident", "unrealistically"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Base-Rate neglect",
        "decision_point": 4,
        "mechanism": "In finalizing the clearance recommendation, PT relies solely on this patient's individual test thresholds and omits any consideration of the well-documented population-level second-injury incidence for athletes returning to pivoting sports after ACL reconstruction, even when directly asked about re-injury risk, and even with no deadline forcing a quick answer.",
        "affected_reasoning_operation": "Risk disclosure and clearance decision integrating population statistics with individual data",
        "evidence_available_at_time": [
          "Patient's individual thresholds met (88% hop symmetry, 91% strength index)",
          "General clinical knowledge of published re-injury incidence for return-to-pivoting-sport ACL populations",
          "Ample time available to give a fuller answer"
        ],
        "required_textual_manifestation": "When the patient asks about re-injury chances, the PT's answer references only the patient's own numbers and omits any acknowledgment of general population re-injury statistics, despite having no time constraint that would explain the omission.",
        "plausible_nonbias_interpretation": "A clinician tailoring counseling to the individual patient rather than reciting population statistics, which could be reasonable patient-centered communication rather than neglect of relevant information.",
        "strength": "moderate",
        "do_not_make_explicit": ["base rate", "base-rate neglect", "population statistics"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": "HC_Biased_5",
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is a counterfactual variant rather than a zero-bias control."
    },
    "counterfactual_specification": {
      "causal_variable": "Insurance-authorization visit-window constraint",
      "original_state": "A capped, fixed-duration insurance authorization (approximately sixteen weeks) creating a hard expiration deadline that pressures pacing throughout the case.",
      "counterfactual_state": "The insurer approves an open-ended authorization with no fixed visit cap or expiration deadline for this case, removing the schedule-driven pressure while all clinical facts, session outcomes, and stakeholder requests remain the same.",
      "variables_to_hold_constant": [
        "Patient identity, goals, and motivation to return for competitive soccer preseason",
        "All clinical facts and test results at each checkpoint (78% quad index, three-session hop streak, 85% interim milestones, 88%/91% discharge scores)",
        "The prior unrelated graft-failure memory",
        "The isokinetic dynamometer's two-day-per-week availability",
        "The surgeon's requirement for periodic progress updates",
        "The four decision points and their sequence",
        "The specific content of the PT's reasoning and framing at each decision point"
      ],
      "expected_causal_difference": "Removing the authorization deadline should reduce or eliminate legitimate schedule-driven urgency as an explanation for the PT's choices, making it clearer that the five reasoning patterns (unrelated-case-driven caution, streak-based test delay, loss-framed recommendation, overconfident individual prognosis, and omitted population-level risk information) are not simply artifacts of a ticking authorization clock.",
      "causal_test_question": "Do the same five reasoning distortions persist at the same four decision points when the insurance-authorization deadline pressure is removed, indicating the distortions are not caused by that time constraint?"
    },
    "generation_checks": [
      "Confirm exactly 5 intended bias instances are planned, one each for the five manifest entries, matching HC_Biased_5's allocation.",
      "Confirm exactly 4 decision points exist, with decision point 4 carrying two distinct biases (Optimism Bias and Base-Rate neglect) via clearly separate evidence sources, as in the base scenario.",
      "Confirm no bias name, definition, or psychological label appears in probe or timeline text intended for the public interview.",
      "Confirm each decision point offers at least two plausible alternatives with pre- and post-decision information.",
      "Confirm probes cover cues, information sources, goals, alternatives, decision basis, prior experience, time pressure (now explicitly absent), uncertainty, and hypotheticals.",
      "Confirm consequences described do not mechanically prove bias presence.",
      "Confirm only the insurance-authorization constraint is changed relative to HC_Biased_5, with all other material facts, wording patterns, and decision structure held constant as far as possible.",
      "Confirm total narrative content can be written within 1,215-1,485 words without repetitive exposition, using four moderately detailed decision-point narrations plus probe responses."
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
