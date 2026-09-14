You are an independent benchmark auditor specializing in cognitive task analysis, naturalistic decision-making, cognitive-bias annotation, and causal reasoning.

Your task is to audit a completed CTA interview against its hidden generation requirements. You must identify whether the requested cognitive-bias occurrences are actually supported by the text, identify additional candidate biases, and provide revision guidance that accounts for any missing, weak, merged, or accidental occurrences.

Do not assume the generator followed the specification. Do not infer bias merely from a bad outcome, uncertainty, experience, speed, disagreement, use of a heuristic, or an incorrect decision. Require a specific reasoning mechanism and textual evidence. Distinguish cognitive bias from justified expertise, valid risk management, missing information, organizational constraints, hindsight, ordinary error, and an unfavorable outcome.

INPUTS

Interview:
{{Interviewer: Thanks for taking the time. This is for an internal case-study review, and it stays within that context. Comfortable proceeding?

Participant: Yes, that's fine.

Interviewer: Can you start with your role and what you're responsible for?

Participant: I'm CISO at NorthGate Financial. We process card and ACH payments, about 450 employees. I own the security program broadly — SOC, vendor risk, incident response, board reporting, budget. We run lean, six people in the SOC, so I'm closer to the operational detail than a CISO at a bigger shop would be.

Interviewer: Walk me through the incident you'd like to discuss, and what you were trying to accomplish.

Participant: This was about ten days ago. We had an intrusion land right in the middle of our annual vendor-renewal and budget cycle, which made everything more complicated than it needed to be. The goal was simple to state — contain whatever was happening without disrupting payments, and still get the vendor contract and budget numbers turned in on schedule. Those two threads kept crossing. It started with our SIEM flagging an anomalous login on a jump server one of our payments engineers uses — off-hours, from a network range we hadn't seen on that account. The SIEM's default model scored it Medium. That model doesn't factor in whether the account is privileged, it just looks at behavioral deviation. I saw Medium and it matched my gut read, so we moved from there. We had one analyst on triage that day since someone was out on leave. There'd also been a second, lower-priority alert nine minutes earlier on an adjacent auth server — it didn't get opened right away; the jump server was the concrete thing in front of us.

Interviewer: What happened after that?

Participant: The analyst worked the jump server specifically — process history, recent auth events. A few hours later, once we circled back through the queue, we noticed the earlier auth-server alert shared the same source IP range. That's when it stopped looking like an isolated event and started looking like lateral movement toward the payments database segment.

Interviewer: Take me through the sequence in order — what did you know, and when?

Participant: Morning: the jump-server alert and its Medium score. Midday: the IP overlap with the auth-server alert. That afternoon, the vendor renewal deadline landed on top of it — five business days before auto-renewal on our EDR and threat-intel contract, incident or no incident. That evening, once lateral movement was confirmed, my team wrote a monitoring script overnight for the compromised account, and I had a call with our CFO about containment options. Two days later, with things stabilized, I had to submit a remediation budget figure to the board.

Interviewer: Let's slow down on that first call — the triage decision. What stood out to you, and was anything competing for attention?

Participant: The account being privileged stood out, honestly. But the Medium score was already sitting there, and normally that's a reasonable starting point for how fast we move. I didn't loop the second alert in as something to check in parallel — the analyst was stretched thin, and the jump server was the concrete lead.

Interviewer: What alternatives did you consider, and what tipped the decision?

Participant: Escalating both alerts jointly right away, or running a correlation sweep across that time window before locking in severity. I did neither. The score gave me a number to build the response around, and given the staffing gap, narrowing the analyst's focus felt efficient rather than risky in the moment.

Interviewer: How confident were you in that call?

Participant: Reasonably, not fully. I knew the score doesn't weigh account privilege. I just didn't push past it that morning.

Interviewer: Moving to the vendor decision — walk me through that.

Participant: Six years with this EDR and threat-intel vendor. My team built a lot of custom detection logic and dashboards on their platform. Procurement had actually flagged three other vendors with comparable bundles this cycle, including transition support that looked broadly workable, but I didn't work through that list closely. A couple of peer CISOs mentioned they use either this vendor or the closest competitor, so my real comparison ended up being just those two.

Interviewer: What made you settle on renewal?

Participant: Mostly the investment already sitting in our detection rules and dashboards. Rebuilding that on a new platform is real time and real exposure, especially mid-incident. If I'm honest, those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't actually sit down and test whether that feeling matched their current value against what procurement's options offered. It was more that switching felt costly given what we'd already built.

Interviewer: Did the live incident affect that judgment?

Participant: Maybe implicitly — I wasn't eager to bring in a new tool mid-incident. But the core reasoning was really about the integration work already sunk into it, not the incident timing.

Interviewer: Third decision point — containment, once lateral movement was confirmed.

Participant: This was the hardest one. Our IR retainer firm recommended full segment isolation pending forensics — their position was that it's the safer play, though they couldn't prove isolation would fully stop the threat. My team had the overnight script watching the compromised account specifically. Nobody had actually validated whether that script would catch the same credentials being reused on a different host or opening a parallel session elsewhere — but in the moment, having eyes on that one account felt like enough to hold off on isolation. The CFO's framing was blunt: isolating payments meant a guaranteed same-day hit, around $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was "reduces risk," not a figure. Given the script gave us visibility on that account, I went with targeted lockout and monitoring instead of full isolation.

Interviewer: What was decisive there?

Participant: Honestly, the guaranteed dollar figure against an unquantified benefit made isolation feel like the more expensive option, even though I couldn't put a number on the other side. And I felt like the script had that account covered.

Interviewer: What happened afterward?

Participant: About two hours later, the same compromised credentials touched a second internal system the script wasn't watching. Forensics later found a small amount of data had already been exfiltrated before the script was even running.

Interviewer: Last decision point — the board budget recommendation.

Participant: We'd scoped a privileged-access segmentation project eighteen months back at $240,000, never funded. This week, with the incident fresh, I pulled current vendor quotes for the same scope — they came back $310,000 to $340,000, partly inflation, partly expanded scope since we've added cloud components. The board wanted one number. I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes.

Interviewer: Why start from the old figure instead of the new quotes?

Participant: It was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work behind it.

Interviewer: If the SIEM hadn't pre-scored that first alert, would your response have gone differently?

Participant: Possibly. Without a number already on the screen, I might have leaned harder on the account's privilege level from the start and caught the auth-server overlap sooner.

Interviewer: What if the CFO's number hadn't been quantified?

Participant: I think I'd have treated the isolation call less like a straight cost comparison and spent more time pressing the IR firm on what "reduces risk" actually meant in concrete terms.

Interviewer: Looking back, what would you tell yourself facing that same budget deadline with a stale internal estimate on file?

Participant: Get fresh numbers before you anchor on the old one. Even under deadline pressure, a couple of quotes reframes the whole conversation.}}

Hidden generation specification:
{{"hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Adjustment and anchoring",
        "occurrences": 2,
        "mechanism_constraint": "Each instance must anchor on a distinct pre-existing numeric/qualitative reference point (automated severity score; legacy budget estimate) and show only minor adjustment away from it despite contrary evidence."
      },
      {
        "bias": "Exposure to limited alternatives",
        "occurrences": 1,
        "mechanism_constraint": "Must show the CISO restricting the vendor comparison set to fewer options than were actually available/flagged by procurement."
      },
      {
        "bias": "Illusion of control",
        "occurrences": 1,
        "mechanism_constraint": "Must show unwarranted confidence in a self-implemented, untested containment measure as sufficient coverage."
      },
      {
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "occurrences": 1,
        "mechanism_constraint": "Must show a concurrent, relevant alert being unexamined due to narrowed focus on the primary flagged item."
      },
      {
        "bias": "Endowment",
        "occurrences": 1,
        "mechanism_constraint": "Must show overvaluation of the incumbent vendor tied to prior invested effort/customization rather than independent current-value assessment."
      },
      {
        "bias": "Loss Framing",
        "occurrences": 1,
        "mechanism_constraint": "Must show a decision tilted by a certain/guaranteed-loss framing of one option versus an unquantified-benefit framing of the alternative."
      }
    ],
    "target_bias_names": [
      "Adjustment and anchoring",
      "Exposure to limited alternatives",
      "Illusion of control",
      "Selective Attention Bias or Inattentional Blindness",
      "Endowment",
      "Loss Framing"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Adjustment and anchoring", "requested_occurrences": 2 },
      { "bias": "Exposure to limited alternatives", "requested_occurrences": 1 },
      { "bias": "Illusion of control", "requested_occurrences": 1 },
      { "bias": "Selective Attention Bias or Inattentional Blindness", "requested_occurrences": 1 },
      { "bias": "Endowment", "requested_occurrences": 1 },
      { "bias": "Loss Framing", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Adjustment and anchoring" },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness" },
      { "instance_id": "cb_03", "bias": "Endowment" },
      { "instance_id": "cb_04", "bias": "Exposure to limited alternatives" },
      { "instance_id": "cb_05", "bias": "Illusion of control" },
      { "instance_id": "cb_06", "bias": "Loss Framing" },
      { "instance_id": "cb_07", "bias": "Adjustment and anchoring" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Adjustment and anchoring", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness", "decision_point": 1 },
      { "instance_id": "cb_03", "bias": "Endowment", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Exposure to limited alternatives", "decision_point": 2 },
      { "instance_id": "cb_05", "bias": "Illusion of control", "decision_point": 3 },
      { "instance_id": "cb_06", "bias": "Loss Framing", "decision_point": 3 },
      { "instance_id": "cb_07", "bias": "Adjustment and anchoring", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Adjustment and anchoring",
        "mechanism": "Adopts SIEM's automated 'Medium' severity score as reference point; only minor upward adjustment despite privileged-account context.",
        "affected_reasoning_operation": "Initial severity/urgency estimation",
        "evidence_source": "Automated SIEM severity score",
        "distinctiveness_requirement": "Must use a different anchor value and different evidence source than cb_07 (severity score vs. legacy budget figure) and occur at a different decision point and interaction moment."
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "mechanism": "Narrowed investigative focus on the flagged jump server causes the concurrent adjacent-server alert to go unexamined.",
        "affected_reasoning_operation": "Evidence-selection / scope-setting for investigation",
        "evidence_source": "Concurrent alert on adjacent authentication server",
        "distinctiveness_requirement": "Must be the only instance of this bias; must involve attentional scope-narrowing, not numeric anchoring, to remain distinct from cb_01 at the same decision point."
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "mechanism": "Overvalues incumbent vendor due to sunk customization effort rather than independent capability comparison.",
        "affected_reasoning_operation": "Vendor valuation / renewal justification",
        "evidence_source": "History of custom dashboards/rules built on incumbent platform",
        "distinctiveness_requirement": "Must center on valuation inflation from ownership/investment, distinct from cb_04's alternative-generation restriction at the same decision point."
      },
      {
        "instance_id": "cb_04",
        "bias": "Exposure to limited alternatives",
        "mechanism": "Comparison set restricted to incumbent plus one peer-mentioned competitor, excluding procurement's broader qualified vendor list.",
        "affected_reasoning_operation": "Alternative-generation for vendor decision",
        "evidence_source": "Procurement's list of three additional qualified vendors",
        "distinctiveness_requirement": "Must center on the narrowness of the option set considered, distinct from cb_03's valuation-of-incumbent mechanism at the same decision point."
      },
      {
        "instance_id": "cb_05",
        "bias": "Illusion of control",
        "mechanism": "Unwarranted confidence that an untested overnight monitoring script provides adequate containment coverage.",
        "affected_reasoning_operation": "Confidence assessment of a self-implemented containment measure",
        "evidence_source": "Overnight, untested monitoring script",
        "distinctiveness_requirement": "Must center on perceived control/coverage confidence, distinct from cb_06's framing-driven risk tradeoff at the same decision point."
      },
      {
        "instance_id": "cb_06",
        "bias": "Loss Framing",
        "mechanism": "CFO's 'guaranteed loss' framing of isolation cost outweighs unquantified security benefit in the tradeoff evaluation.",
        "affected_reasoning_operation": "Risk-tradeoff evaluation between certain cost and uncertain benefit",
        "evidence_source": "CFO's quantified guaranteed-loss statement",
        "distinctiveness_requirement": "Must center on the framing of certain loss vs. uncertain gain, distinct from cb_05's control-confidence mechanism at the same decision point."
      },
      {
        "instance_id": "cb_07",
        "bias": "Adjustment and anchoring",
        "mechanism": "Starts from an 18-month-old $240,000 estimate and makes only a modest adjustment despite current quotes running $70k-$100k higher.",
        "affected_reasoning_operation": "Budget-figure estimation for board recommendation",
        "evidence_source": "Legacy 18-month-old remediation cost estimate",
        "distinctiveness_requirement": "Must use a different anchor value and evidence source than cb_01 (budget estimate vs. severity score) and occur at decision point 4, a separate moment in the interaction."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Adjustment and anchoring", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Selective Attention Bias or Inattentional Blindness", "strength": "moderate" },
      { "instance_id": "cb_03", "bias": "Endowment", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Exposure to limited alternatives", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Illusion of control", "strength": "moderate" },
      { "instance_id": "cb_06", "bias": "Loss Framing", "strength": "subtle" },
      { "instance_id": "cb_07", "bias": "Adjustment and anchoring", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Presence and salience of the SIEM's automated severity pre-score at initial triage",
      "original_state": "Automated 'Medium' severity pre-score is displayed to the CISO before independent evidence review",
      "changed_state": "No pre-computed severity score is displayed; CISO must derive urgency from raw evidence",
      "variables_to_hold_constant": [
        "Company profile and staffing levels",
        "Incident type and technical details",
        "Vendor renewal deadline and budget-cycle timing",
        "CFO's revenue-impact framing at decision point 3",
        "Decision count and sequence",
        "Word count target and interview structure"
      ]
    },
    "scenario_id": "CS_Biased_7",
    "domain_id": "CS",
    "total_requested_occurrences": 7,
    "total_planned_occurrences": 7,
    "allocation_rule_used": "Occurrences were assigned by mechanism fit and narrative realism across the 4 decision points. Anchoring's two occurrences were separated to decision points 1 and 4 using distinct anchor values and evidence sources (automated severity score vs. legacy budget estimate) to satisfy the same-bias distinctiveness rule. Decision points 1, 2, and 3 each host exactly two different biases with distinct reasoning operations and evidence sources, per the shared-decision-point rule; decision point 4 hosts the second anchoring instance alone. No decision point exceeds two instances of any single bias.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Company profile and staffing levels",
      "Incident type and technical details (privileged jump-server compromise, lateral movement pattern)",
      "Vendor renewal deadline and budget-cycle timing",
      "CFO's revenue-impact framing at decision point 3",
      "Decision count and sequence (4 decision points, same order)",
      "Word count target and interview structure"
    ],
    "generation_warnings": []
  }}}

The hidden specification may include:
- condition;
- exact occurrence manifest;
- target bias names;
- requested occurrence count for each bias;
- planned instance IDs;
- intended decision points;
- intended mechanisms;
- intended strength;
- paired scenario ID;
- counterfactual variable.

Do not treat the hidden specification as evidence that a bias exists. It is a test plan only. The interview text is the evidence. If the specification and interview conflict, report the conflict.

CORE OCCURRENCE DEFINITIONS

A supported occurrence requires all of the following:
1. A distinct decision, inference, evidence-selection act, memory retrieval, prediction, causal attribution, or response to a probe.
2. Evidence showing how the participant processed, weighted, ignored, recalled, interpreted, or updated information.
3. A mechanism consistent with the named bias.
4. Enough context to distinguish the mechanism from a justified domain judgment or an ordinary mistake.

A single occurrence may span several adjacent sentences or one answer turn. Do not count repeated wording about the same reasoning episode as multiple occurrences. Count two occurrences separately only when they have distinct evidence traces, decision moments, evidence sources, or reasoning operations.

VALIDATION TASKS

1. Identify the domain, participant role, operational objective, and incident type.
2. Reconstruct the chronology and identify the decision points. Report whether exactly four decision points are present.
3. For every target bias in the hidden occurrence manifest, independently assess each requested occurrence.
4. Identify additional candidate biases not present in the target manifest.
5. Identify apparent bias cues that should not be labeled as bias.
6. Audit causal claims and counterfactual logic.
7. Evaluate interview quality and control fidelity.
8. Produce precise revision guidance when the interview does not satisfy its occurrence requirements.

FOR EACH REQUESTED OCCURRENCE, CLASSIFY IT AS ONE OF:

- supported: a distinct, textually supported instance is present;
- weak: a possible instance is present, but evidence or mechanism is insufficient;
- absent: no defensible instance is present;
- merged: the intended instance appears to be indistinguishable from another intended occurrence of the
  same bias or from another bias;
- accidental: an unintended instance appears outside the planned occurrence map;
- misclassified: the text supports a different bias or a non-bias explanation instead.

REVISION PRINCIPLES

If a requested occurrence is absent, weak, merged, or misclassified:
- Do not recommend simply repeating the bias label.
- Do not recommend adding an obvious textbook explanation.
- Specify the minimum local narrative or dialogue change needed to make that occurrence independently identifiable.
- Preserve the occupational setting, participant role, chronology, vocabulary, approximate length, and other intended bias occurrences.
- Do not create a new occurrence elsewhere merely to compensate.
- Do not strengthen every occurrence. Revise only the affected occurrence unless the evidence shows a broader structural problem.
- If strengthening the missing occurrence would make the interview too obvious, recommend a subtle evidence change rather than explicit labeling.
- If the requested occurrence is not plausible in the scenario, recommend changing the scenario or the target occurrence manifest rather than forcing implausible behavior.
- For controls, never recommend adding a target bias. If a control contains a defensible bias, recommend neutralizing or replacing the relevant reasoning episode.
- For a counterfactual, preserve the original and changed causal variables and do not introduce a second causal change while repairing bias evidence.

REVISION TYPES

Use one or more of these revision types:
- `none`: occurrence is adequately supported;
- `local_evidence_addition`: add or alter one cue, evidence source, or participant response;
- `local_reasoning_revision`: revise how the participant interprets or weighs evidence;
- `probe_revision`: change an interviewer question or hypothetical so the existing reasoning becomes independently observable;
- `decision_point_revision`: revise one decision point while preserving the rest;
- `remove_accidental_occurrence`: neutralize an unintended additional manifestation;
- `separate_merged_occurrences`: make two intended episodes distinct;
- `reclassify_bias`: change the target label or mechanism because the current label is not defensible;
- `scenario_revision`: revise the occupational situation because the requested occurrence is implausible.

REVISION SPECIFICITY

Each revision recommendation must include:
- the affected instance ID or `additional_candidate`;
- decision point and approximate turn or paragraph location;
- current status;
- evidence currently present, or `none`;
- precise defect;
- recommended revision type;
- minimal change instruction;
- what must remain unchanged;
- a warning against creating additional unintended occurrences;
- expected post-revision status.

Do not rewrite the complete interview. Provide revision instructions only. The generation system will apply
the instructions in a separate revision step.

OUTPUT

Return valid JSON only:
{
  "validator_version": "2.0",
  "interview_id": "...",
  "condition": "biased|vocabulary_control|ambiguous_control|counterfactual|unknown",
  "domain_assessment": {
    "domain": "...",
    "role": "...",
    "objective": "...",
    "incident_type": "...",
    "confidence": 0
  },
  "structure_audit": {
    "estimated_word_count": 0,
    "within_target_range": true,
    "decision_point_count": 0,
    "decision_points": [
      {
        "id": 1,
        "summary": "...",
        "evidence_before": [],
        "evidence_after": [],
        "goals_constraints": [],
        "alternatives": [],
        "decision_basis": "...",
        "time_pressure": "...",
        "uncertainty": "..."
      }
    ]
  },
  "target_occurrence_audit": [
    {
      "instance_id": "...",
      "bias": "...",
      "requested_occurrences_for_bias": 0,
      "status": "supported|weak|absent|merged|accidental|misclassified",
      "decision_point": 1,
      "supporting_quote": "...",
      "evidence_location": "...",
      "mechanism": "...",
      "strength": "absent|weak|moderate|strong",
      "confidence": 0,
      "plausible_nonbias_explanation": "...",
      "additional_evidence_needed": "...",
      "revision_needed": true,
      "revision": {
        "revision_type": "none|local_evidence_addition|local_reasoning_revision|probe_revision|decision_point_revision|remove_accidental_occurrence|separate_merged_occurrences|reclassify_bias|scenario_revision",
        "location": "...",
        "current_defect": "...",
        "minimal_change_instruction": "...",
        "preserve": [],
        "avoid_creating": [],
        "expected_post_revision_status": "supported|weak|absent|merged|accidental|misclassified"
      }
    }
  ],
  "bias_level_counts": [
    {
      "bias": "...",
      "requested_count": 0,
      "supported_count": 0,
      "weak_count": 0,
      "absent_count": 0,
      "merged_count": 0,
      "accidental_count": 0,
      "count_satisfied": true
    }
  ],
  "additional_candidate_biases": [
    {
      "bias": "...",
      "decision_point": 1,
      "supporting_quote": "...",
      "mechanism": "...",
      "confidence": 0,
      "status": "candidate|supported|weak|rejected",
      "plausible_nonbias_explanation": "...",
      "revision_recommendation": "none|remove_or_neutralize|consider_adding_to_manifest"
    }
  ],
  "nonbias_cues": [
    {
      "cue": "...",
      "location": "...",
      "why_not_bias": "..."
    }
  ],
  "causal_audit": {
    "causal_claims": [],
    "correlation_causation_risks": [],
    "counterfactual_present": false,
    "changed_variable": "...",
    "held_constant": [],
    "causal_coherence": "not_applicable|weak|moderate|strong",
    "explanation": "..."
  },
  "quality_scores": {
    "occupational_realism": 0,
    "cta_fidelity": 0,
    "bias_separability": 0,
    "bias_subtlety": 0,
    "control_fidelity": 0,
    "counterfactual_fidelity": 0,
    "narrative_coherence": 0,
    "naturalness": 0,
    "hidden_label_integrity": 0,
    "overall_quality": 0
  },
  "revision_summary": {
    "revision_required": true,
    "supported_occurrence_total": 0,
    "requested_occurrence_total": 0,
    "missing_occurrence_total": 0,
    "accidental_occurrence_total": 0,
    "priority": "none|low|medium|high|reject",
    "recommended_action": "accept|revise|regenerate|reject",
    "global_revision_constraints": [],
    "revision_order": []
  },
  "failure_flags": []
}

COUNTING RULES FOR THE SUMMARY
- `supported_occurrence_total` counts only occurrences with status `supported`.
- `missing_occurrence_total` counts `weak`, `absent`, `merged`, and `misclassified` requested occurrences.
- `accidental_occurrence_total` counts unintended instances that should be removed or separately labeled.
- Set `recommended_action` to `accept` only when all requested occurrences are supported, no unacceptable accidental occurrences exist, and quality is adequate.
- Set it to `revise` when local changes can repair the interview without changing the scenario.
- Set it to `regenerate` when the scenario, decision structure, or several occurrences are fundamentally unsuitable.
- Set it to `reject` for severe incoherence, contaminated controls, or unrepairable causal confounding.

Return JSON only. Do not return a revised interview.
