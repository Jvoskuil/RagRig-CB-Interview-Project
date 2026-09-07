You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IA_Vocab_Control_6",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Cyber Threat Intelligence Analyst",
  "condition": "vocabulary_control",
  "generation_specification": {
    "scenario_title_internal": "The GreyFalcon Alert Cluster — Vocabulary-Matched Control",
    "scenario_summary_internal": "A CTI analyst on the same financial-services SOC shift investigates a structurally identical alert cluster potentially tied to the 'GreyFalcon' APT group or lower-severity commodity activity. Across the same four decision types—initial triage, attribution, scope determination, and containment/reporting—the analyst weighs automated tool output, a vendor threat-intel bulletin, historical campaign similarity, and internal telemetry under matched time pressure, but each decision is supported by proportionate verification, balanced evidence weighting, and explicit consideration of alternatives, with no intended cognitive-bias mechanism embedded.",
    "occupational_realism": {
      "objective": "Determine whether the alert cluster represents a genuine intrusion by an advanced persistent threat actor, establish attribution confidence, define hunt/containment scope, and produce a timely recommendation to the incident response lead before end of shift.",
      "setting": "Security operations center (SOC) of a mid-sized financial services firm, during a live 24-hour shift; incident response and threat intel functions are integrated.",
      "constraints": [
        "Shift ends in under three hours, and handoff quality depends on a defensible recommendation.",
        "Business-critical trading systems cannot be taken offline without CISO sign-off, limiting immediate isolation options.",
        "Only partial log retention is available for the suspected initial-access system.",
        "External vendor threat-intel access is time-limited and was consumed during this shift.",
        "Possible active exfiltration creates pressure to decide quickly rather than wait for full log correlation."
      ],
      "stakeholders": [
        "CTI analyst (interviewee)",
        "Incident response lead",
        "CISO",
        "Third-party threat intelligence vendor",
        "Business unit system owner (trading platform)",
        "Legal/compliance liaison"
      ],
      "technical_terms_to_use": [
        "IOC", "TTP", "MITRE ATT&CK", "EDR", "SIEM", "C2 infrastructure", "lateral movement",
        "exfiltration", "playbook", "attribution confidence", "IOC pivoting", "threat actor cluster",
        "YARA rule", "sandbox detonation", "triage severity score"
      ],
      "technical_terms_to_avoid": [
        "bias", "cognitive", "heuristic", "confirmation", "complacency", "anchoring",
        "fluency", "narrative bias", "mirror imaging", "primacy effect", "psychology"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "EDR auto-triage flags a cluster of alerts on a trading-support server as 'Low' severity based on its scoring model.",
          "The analyst recalls two prior shifts where similar low-score alerts were false positives, but also recalls one occasion where a Low score preceded a real incident.",
          "Raw process logs are available but require manual pull and review (15-20 minutes).",
          "No immediate business disruption reported."
        ],
        "new_information_after_decision": [
          "A follow-up alert 40 minutes later shows an outbound connection from the same host to an unfamiliar external IP."
        ],
        "alternatives": [
          "Accept the automated Low severity score and defer manual log review until later in shift.",
          "Immediately pull raw process and network logs from the flagged host regardless of the automated score.",
          "Do a quick five-minute scan of the alert summary fields before deciding whether a full manual pull is warranted."
        ],
        "intended_action": "Analyst performs a brief proportional check of the alert summary, notes nothing that overrides the Low score, and defers the full manual log pull with an explicit plan to revisit if any new signal appears, explaining the trade-off between verification cost and queue coverage."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "A registry-key artifact on the host matches one previously documented in a GreyFalcon campaign six months earlier.",
          "The current C2 domain's registration pattern (registrar, age, WHOIS privacy config) differs notably from GreyFalcon's historical infrastructure pattern.",
          "Internal telemetry shows attempted access to an HR benefits database, not the trading or financial data systems GreyFalcon has historically targeted.",
          "Time is limited before the vendor threat-intel portal access window closes."
        ],
        "new_information_after_decision": [
          "Later log correlation shows the HR database access attempt failed and was not repeated, while trading-adjacent systems saw no anomalous access at all during this window."
        ],
        "alternatives": [
          "Assign high attribution confidence to GreyFalcon based on the registry-key match alone.",
          "Assign moderate attribution confidence, explicitly flagging the infrastructure and targeting mismatches as open questions requiring further evidence before scoping.",
          "Assign low attribution confidence and treat the activity as an unclustered or commodity threat pending further evidence."
        ],
        "intended_action": "Analyst assigns moderate attribution confidence, explicitly naming both the registry-key match and the two discordant signals (infrastructure pattern, HR targeting) as open items, and defers a firm attribution call until the hunt can test which explanation better fits the full evidence set."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A vendor threat-intel bulletin lists five IOCs, with a rare C2 protocol signature and two file-hash IOCs among them, in no particular order of operational priority stated by the vendor.",
          "Business unit owners want scope kept narrow to avoid unnecessary downtime.",
          "Internal telemetry could plausibly support either an APT narrative or a commodity-malware-plus-insider-misconfiguration narrative.",
          "The analyst's attribution confidence remains moderate and openly contested from phase 2."
        ],
        "new_information_after_decision": [
          "A subsequent sweep of systems included in the hunt scope surfaces one additional host with a partial IOC match, prompting a follow-up review rather than a conclusive resolution."
        ],
        "alternatives": [
          "Scope the hunt broadly across all systems touched by any of the five listed IOCs, regardless of listing order.",
          "Scope the hunt narrowly around whichever single IOC seems most memorable or dramatic.",
          "Scope the hunt in two passes: first the two file-hash IOCs as lower-false-positive indicators, then expand to the protocol signature if the first pass is inconclusive."
        ],
        "intended_action": "Analyst scopes the hunt in a staged approach, starting with the two file-hash IOCs precisely because they are more diagnostic and lower false-positive risk, then expanding to the protocol signature and related systems, explicitly weighing diagnosticity over any single indicator's prominence in the bulletin."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The vendor bulletin is professionally formatted with confident, polished language and clean visual IOC tables.",
          "An internal colleague's raw incident notes, written in hedged language with explicit uncertainty markers, suggest a lower-confidence, broader containment approach.",
          "The IR lead needs a containment recommendation within the hour.",
          "Both sources cover overlapping but not identical evidence."
        ],
        "new_information_after_decision": [
          "Containment is applied based on the chosen recommendation; whether the underlying attribution was correct remains unresolved at end of shift and is not immediately testable from the containment outcome alone."
        ],
        "alternatives": [
          "Recommend containment steps modeled closely on the vendor bulletin's confident, specific guidance.",
          "Recommend a broader, more conservative containment approach reflecting the internal analyst's hedged uncertainty.",
          "Cross-check specific claims in both sources against raw telemetry before finalizing, regardless of how each source is written."
        ],
        "intended_action": "Analyst cross-checks the specific factual claims in both the vendor bulletin and the internal notes against available telemetry, finds both sources partially corroborated, and recommends a containment approach that blends the vendor's specific technical steps with the colleague's broader precautionary scope, explaining the choice by evidentiary overlap rather than by which source read more confidently."
      }
    ],
    "probe_plan": {
      "opening": [
        "Can you walk me through what this shift looked like when the alert cluster first appeared?",
        "What was your primary objective at the point you first saw these alerts?"
      ],
      "timeline_reconstruction": [
        "What happened first, and what did you do next?",
        "At what point did you form a working view of what was going on?",
        "What information came in after each of your decisions that changed or didn't change your view?"
      ],
      "decision_point_probes": [
        "What cues drew your attention at that point?",
        "What information sources did you rely on, and which did you set aside?",
        "What were you trying to accomplish with that decision?",
        "What other options did you consider, and why didn't you choose them?",
        "What was the main basis for the choice you made?",
        "Had you seen a similar pattern before? How did that affect your read of this one?",
        "How much time pressure did you feel at that moment?",
        "How confident were you in that call, and what would have changed your confidence?",
        "If you'd had access to different information at that point, would you have decided differently?"
      ],
      "closing_hypotheticals": [
        "If the vendor bulletin had listed its IOCs in a different order, do you think your scoping would have changed?",
        "If you had pulled the raw logs immediately in phase one, how might the rest of the shift have unfolded?",
        "Looking back, is there a point where you'd want a second analyst's independent read before proceeding?"
      ]
    },
    "occurrence_embedding_plan_internal": [],
    "control_specification": {
      "paired_scenario_id": "IA_Biased_6",
      "features_to_match": [
        "Domain vocabulary (IOC, TTP, MITRE ATT&CK, EDR, SIEM, C2 infrastructure, lateral movement, exfiltration, playbook, attribution confidence, IOC pivoting, threat actor cluster, YARA rule, sandbox detonation, triage severity score)",
        "Setting: financial-services SOC, overnight shift, integrated IR/CTI function",
        "Actors: CTI analyst, IR lead, CISO, vendor, business unit owner, legal/compliance",
        "Same four decision types: initial triage, attribution, hunt scope, containment/reporting",
        "Same underlying incident facts: trading-support server, registry-key artifact matching a GreyFalcon campaign, discordant C2 infrastructure pattern, HR database access attempt, five-IOC vendor bulletin, colleague's hedged notes",
        "Same emotional tone: measured, mildly time-pressured, professionally reflective",
        "Same time constraints: three hours left in shift, fifteen-to-twenty-minute log pull cost, one-hour containment deadline",
        "Same probe structure and closing hypotheticals",
        "Approximate word count and dialogue format"
      ],
      "features_to_remove_or_change": [
        "Remove the deferral of manual verification without any proportional check (phase 1); replace with a brief proportional check that is explicitly reasoned and revisited on new signal",
        "Remove the exclusive reliance on the registry-key match without engaging discordant evidence (phase 2); replace with an explicit moderate-confidence stance that names both mismatches as open questions",
        "Remove the self-referential 'if I were an operator' projection used to explain the HR-targeting mismatch (phase 2); replace with an explicit statement that attribution is deferred pending further evidence rather than resolved via analogy to the analyst's own reasoning",
        "Remove the narrative-coherence justification for scope and the disproportionate weight on the first-listed IOC (phase 3); replace with a staged, diagnosticity-driven scoping approach that treats all five IOCs on their evidentiary merits",
        "Remove the presentation-based preference for the vendor bulletin over the colleague's hedged notes (phase 4); replace with an explicit cross-check of factual claims from both sources against telemetry, with a containment recommendation justified by evidentiary overlap"
      ],
      "ambiguity_boundary": "The scenario retains the same amount of underlying evidentiary uncertainty as the paired biased scenario (discordant infrastructure pattern, ambiguous HR-targeting, unordered vendor IOC list, conflicting source styles), but every decision-point resolution in this control version is reached through an explicit, proportionate reasoning process that engages the discordant or ambiguous evidence directly, rather than resolving it through a biased shortcut. Residual uncertainty is preserved and explicitly acknowledged by the participant rather than eliminated."
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
      "Confirm zero intended bias instances are embedded anywhere in the interview.",
      "Confirm exactly 4 decision points, each with at least two alternatives, matching the paired scenario's decision types.",
      "Confirm domain vocabulary, actors, setting, constraints, and emotional tone match the paired scenario IA_Biased_6.",
      "Confirm each decision point shows the analyst explicitly engaging discordant or ambiguous evidence rather than resolving it through narrative shortcut, positional weighting, presentation-based trust, automation deference, or self-projection.",
      "Confirm no bias terminology, labels, or psychological explanations appear in the public interview text.",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points, probe plan, and matched narrative complexity without repetitive exposition.",
      "Confirm consequences described (phase 4 outcome) remain genuinely unresolved and do not mechanically prove correctness of any decision."
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
