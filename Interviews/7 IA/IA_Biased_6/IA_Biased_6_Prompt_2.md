You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IA_Biased_6",
  "domain_id": "IA",
  "domain": "Intelligence analysis and information-intensive analytic work",
  "role": "Cyber Threat Intelligence Analyst",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The GreyFalcon Alert Cluster",
    "scenario_summary_internal": "A CTI analyst on a financial-services SOC shift investigates a cluster of EDR/SIEM alerts that may indicate an intrusion by a previously observed APT group ('GreyFalcon') or may be lower-severity commodity activity. Across four decisions—initial triage, attribution, scope determination, and containment/reporting—the analyst must weigh automated tool output, a vendor threat-intel bulletin, historical campaign similarity, and internal telemetry under time pressure, with the possibility of ongoing exfiltration.",
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
          "The analyst recalls two prior shifts where similar low-score alerts were false positives.",
          "Raw process logs are available but require manual pull and review (15-20 minutes).",
          "No immediate business disruption reported."
        ],
        "new_information_after_decision": [
          "A follow-up alert 40 minutes later shows an outbound connection from the same host to an unfamiliar external IP."
        ],
        "alternatives": [
          "Accept the automated Low severity score and defer manual log review until later in shift.",
          "Immediately pull raw process and network logs from the flagged host regardless of the automated score.",
          "Escalate directly to the IR lead for a second opinion before doing anything else."
        ],
        "intended_action": "Analyst defers manual verification, accepting the EDR's Low severity classification without independently reviewing raw logs."
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
          "Treat the registry-key match as one data point among several and actively search for both corroborating and disconfirming IOCs before assigning attribution.",
          "Assign high attribution confidence to GreyFalcon based on the registry-key match and proceed to scope the hunt around that actor's known playbook.",
          "Assign low attribution confidence and treat the activity as an unclustered or commodity threat pending further evidence."
        ],
        "intended_action": "Analyst assigns high confidence to GreyFalcon attribution based primarily on the registry-key match, and interprets the attacker's interest in the HR system as consistent with what the analyst's own team would prioritize if seeking maximum leverage, rather than testing why the target selection diverges from GreyFalcon's documented pattern."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "A vendor threat-intel bulletin lists five IOCs, with the most dramatic (a rare C2 protocol signature) listed first and two more mundane, arguably more diagnostic file-hash IOCs listed last.",
          "Business unit owners want scope kept narrow to avoid unnecessary downtime.",
          "Internal telemetry could plausibly support either an APT narrative or a commodity-malware-plus-insider-misconfiguration narrative.",
          "The analyst has already built a working attribution narrative from phase 2."
        ],
        "new_information_after_decision": [
          "A subsequent sweep of systems excluded from the hunt scope reveals unrelated benign activity, neither confirming nor disconfirming the chosen scope."
        ],
        "alternatives": [
          "Scope the hunt broadly across all systems touched by any of the five listed IOCs, regardless of listing order.",
          "Scope the hunt narrowly around the first-listed C2 protocol signature and systems that fit the existing GreyFalcon narrative.",
          "Scope the hunt around the two file-hash IOCs first, since they are more specific and lower false-positive-prone, then expand if needed."
        ],
        "intended_action": "Analyst scopes the hunt narrowly around the first-listed IOC and the systems that fit the already-constructed GreyFalcon narrative, treating the coherence of that story as sufficient grounds for the scope decision rather than weighing the later-listed, more diagnostic IOCs."
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
          "Recommend convening a short joint review before finalizing containment scope."
        ],
        "intended_action": "Analyst recommends containment steps drawn primarily from the polished vendor bulletin, treating its confident presentation as an indicator of higher reliability relative to the hedged internal notes, without separately evaluating the underlying evidentiary rigor of each source."
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
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cp_01",
        "bias": "Complacency Bias",
        "decision_point": 1,
        "mechanism": "Over-reliance on automated EDR severity scoring leads to reduced independent verification despite available time and capability to check.",
        "affected_reasoning_operation": "Verification/evidence-gathering decision",
        "evidence_available_at_time": [
          "EDR auto-triage score of 'Low'",
          "Availability of raw logs for manual review",
          "Prior shift history of similar low-score false positives"
        ],
        "required_textual_manifestation": "Analyst explicitly defers manual log review because the tool already scored the alert low, citing trust in the automated system rather than independent judgment.",
        "plausible_nonbias_interpretation": "Reasonable triage prioritization under limited shift time, deferring low-priority items is a standard, defensible practice.",
        "strength": "subtle",
        "do_not_make_explicit": ["complacency", "automation bias", "over-reliance"]
      },
      {
        "instance_id": "cb_01",
        "bias": "Confimation Bias",
        "decision_point": 2,
        "mechanism": "Analyst selectively treats the registry-key IOC match as decisive evidence for a favored attribution hypothesis while not actively seeking or weighting the discordant C2 infrastructure pattern.",
        "affected_reasoning_operation": "Evidence weighting during attribution",
        "evidence_available_at_time": [
          "Registry-key artifact matching prior GreyFalcon campaign",
          "C2 domain registration pattern diverging from GreyFalcon's historical pattern"
        ],
        "required_textual_manifestation": "Analyst cites the registry-key match as confirming GreyFalcon attribution and does not describe actively testing or seeking evidence against that hypothesis, despite the divergent C2 pattern being available.",
        "plausible_nonbias_interpretation": "A single strong artifact match can reasonably raise attribution confidence, and full IOC divergence analysis may simply not have been prioritized given time constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["confirmation bias", "cherry-picking", "selective evidence"]
      },
      {
        "instance_id": "mi_01",
        "bias": "Mirror Imaging Bias",
        "decision_point": 2,
        "mechanism": "Analyst interprets the attacker's target selection (HR database) through the lens of what the analyst's own team would prioritize, rather than testing alternative adversary motivations or capability constraints.",
        "affected_reasoning_operation": "Inference about adversary intent from a different evidence source (target-selection telemetry, not the IOC-matching evidence used in cb_01)",
        "evidence_available_at_time": [
          "Internal telemetry showing attempted HR database access",
          "GreyFalcon's historical targeting pattern favoring trading/financial data, not HR systems"
        ],
        "required_textual_manifestation": "Analyst rationalizes the mismatched target by reasoning about what would make sense 'if I were trying to maximize leverage,' projecting own strategic logic onto the adversary instead of flagging the mismatch as a reason to question attribution.",
        "plausible_nonbias_interpretation": "Adversaries do sometimes pursue secondary objectives, so this could be a reasonable, non-biased inference about opportunistic behavior.",
        "strength": "subtle",
        "do_not_make_explicit": ["mirror imaging", "projecting", "assumes adversary thinks like us"]
      },
      {
        "instance_id": "ex_01",
        "bias": "Explanation bias",
        "decision_point": 3,
        "mechanism": "Analyst treats the internal coherence of the already-constructed GreyFalcon narrative as sufficient justification for the scope decision, rather than independently testing an equally plausible alternative explanation (commodity malware plus insider misconfiguration).",
        "affected_reasoning_operation": "Scope-determination reasoning integrating multiple evidence pieces into a single account",
        "evidence_available_at_time": [
          "Working GreyFalcon narrative carried over from decision point 2",
          "Telemetry plausibly consistent with an alternative, non-APT explanation"
        ],
        "required_textual_manifestation": "Analyst justifies the narrow scope choice by describing how well it 'fits the story so far' rather than by comparing it against the alternative explanation on its own evidentiary merits.",
        "plausible_nonbias_interpretation": "Focusing hunt scope on the leading working hypothesis is a common, resource-efficient triage strategy.",
        "strength": "subtle",
        "do_not_make_explicit": ["explanation bias", "narrative coherence", "need for a story"]
      },
      {
        "instance_id": "oe_01",
        "bias": "Order effects",
        "decision_point": 3,
        "mechanism": "The listing order of IOCs in the vendor bulletin (dramatic signature first, diagnostic hashes last) disproportionately shapes the scope decision toward the first-listed indicator, a different reasoning operation and evidence source (bulletin ordering) than ex_01's narrative-coherence reasoning.",
        "affected_reasoning_operation": "Weighting of listed evidence items during scope selection",
        "evidence_available_at_time": [
          "Vendor bulletin listing five IOCs in a fixed order",
          "Relative diagnosticity of file-hash IOCs listed later in the bulletin"
        ],
        "required_textual_manifestation": "Analyst's stated rationale for scope references the first-listed IOC prominently, with little or no discussion of the later-listed, more diagnostic hashes, and the decision would plausibly differ if the list order were reversed.",
        "plausible_nonbias_interpretation": "The first-listed IOC might genuinely be the most operationally significant, independent of its position, so leading with it could reflect a size or severity ranking rather than a position effect.",
        "strength": "subtle",
        "do_not_make_explicit": ["order effects", "primacy", "list position", "anchoring"]
      },
      {
        "instance_id": "fl_01",
        "bias": "Fluency effects",
        "decision_point": 4,
        "mechanism": "The polished, confidently written vendor bulletin is treated as more reliable than the hedged, uncertainty-laden internal analyst notes, independent of the actual evidentiary rigor of each source.",
        "affected_reasoning_operation": "Source-credibility weighting during containment recommendation",
        "evidence_available_at_time": [
          "Professionally formatted vendor bulletin with confident language",
          "Internal colleague's raw notes with explicit hedges and uncertainty markers"
        ],
        "required_textual_manifestation": "Analyst explains preferring the vendor bulletin's guidance by referencing its clarity, polish, or confident tone rather than a comparison of underlying evidence quality between the two sources.",
        "plausible_nonbias_interpretation": "Vendor bulletins may in fact undergo more rigorous internal review than informal notes, so preferring them could reflect a reasonable institutional-trust heuristic.",
        "strength": "subtle",
        "do_not_make_explicit": ["fluency effect", "polish", "presentation quality", "processing ease"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is 'biased' with no paired control specified."
    },
    "counterfactual_specification": {
      "causal_variable": "Not applicable for this generation (condition is 'biased', not 'counterfactual'); AUTOSELECT resolved to no counterfactual variable required.",
      "original_state": null,
      "counterfactual_state": null,
      "variables_to_hold_constant": [],
      "expected_causal_difference": null,
      "causal_test_question": null
    },
    "generation_checks": [
      "Confirm exactly 6 intended bias instances are embedded, one per manifest entry.",
      "Confirm exactly 4 decision points, each with at least two alternatives.",
      "Confirm no bias terminology, labels, or psychological explanations appear in the public interview text.",
      "Confirm each instance has a distinct evidence source or reasoning operation from any other instance of a different bias at the same decision point (mi_01 vs cb_01 at DP2; oe_01 vs ex_01 at DP3).",
      "Confirm word count target of 1,350 (range 1,215-1,485) is achievable given four decision points, probe plan, and six instance manifestations without repetitive exposition.",
      "Confirm consequences described (phase 4 outcome) do not mechanically prove or disprove bias presence."
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
