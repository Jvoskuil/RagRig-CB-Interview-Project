You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. This conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. Skip anything you're not comfortable discussing. Can you tell me your role and how long you've been doing it?

Participant: Sure. I'm a threat intelligence analyst on the SOC team, about four years in, mostly financial services environments. During shift I handle triage, attribution, and hunt scoping when something looks like more than commodity noise.

Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared?

Participant: About two hours into an overnight shift, EDR kicked out a cluster of alerts on a trading-support server — the box that feeds reporting data to the trading engine, not the engine itself. The auto-triage score came back Low. That queue does throw a lot of low-severity noise from that host, and I'd seen similar low scores turn out benign twice before. But I also remembered one shift where a Low score turned into something real, so I didn't want to just wave it through on pattern-matching alone.

Interviewer: What was your primary objective at that point?

Participant: Cover the queue efficiently without missing something that needed attention, and produce a handoff that would hold up. About three hours were left in the shift, so I wanted to be deliberate about where I spent time.

Interviewer: Take me through what happened next, chronologically.

Participant: After the Low score, I did a quick scan of the alert summary fields — parent process, any flagged child processes, whether the trading-support role tag showed anything unusual. Nothing in that quick look overrode the Low score, so I deferred the full manual log pull, which would've run fifteen to twenty minutes, but I noted it to revisit if anything else came in. About forty minutes later it did — an outbound connection to an unfamiliar IP. That's when I opened the case properly. I found a registry-key artifact matching a GreyFalcon campaign I'd tracked myself about six months back. At the same time, two things didn't fit cleanly: the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure, and there was an attempted connection to the HR benefits database, which isn't a target GreyFalcon has gone after before. I didn't want to commit to an attribution with those loose ends open. A vendor bulletin came in with five IOCs — a rare C2 protocol signature and two file hashes among them — and I used that to build a scope. Near the end of shift, I had a vendor bulletin and a colleague's more hedged internal notes to work from for the containment write-up, and I checked both against telemetry before finalizing.

Interviewer: Let's slow down and go through each decision individually. First — the initial Low-severity alert. What cues were you weighing right then?

Participant: The auto-triage score, the server's history of false alarms, and the absence of any reported business disruption. But I also pulled up the summary fields rather than just accepting the score outright.

Interviewer: What made you decide to do that quick scan instead of either accepting the score outright or doing the full pull immediately?

Participant: It was a middle option. A full manual pull is a real time cost — fifteen, twenty minutes — and I didn't have grounds yet to justify that against the rest of the queue. But taking the score completely at face value without even glancing at the summary felt like too much trust in a score that's generated from a limited rule set. The five-minute look was a way to catch anything obviously wrong without committing the full review time.

Interviewer: Did you consider escalating to the IR lead first?

Participant: Briefly, but there wasn't anything at that point to escalate — a Low score and a quiet business environment. I planned to revisit if anything changed, which it did forty minutes later.

Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for your attribution call?

Participant: The registry-key match was strong — I'd documented that artifact myself in an earlier report, so I trusted it as a data point. But I didn't want to treat it as decisive on its own, because two things cut against it: the C2 domain's registration profile didn't match GreyFalcon's usual infrastructure, and the target — an HR database — wasn't something GreyFalcon has gone after in anything I've tracked. So I called it moderate confidence rather than high, and flagged both mismatches explicitly as things the hunt would need to test.

Interviewer: How did you handle the HR-targeting mismatch specifically? Did you have an explanation for it?

Participant: I didn't try to force one. It's possible there's a reason a GreyFalcon operator would go after HR data, but I didn't have evidence for that, so rather than guess at their motive I just left it as an open inconsistency — something that either gets explained by more evidence or ends up pointing away from this actor entirely.

Interviewer: Let's talk about the hunt scope decision once the vendor bulletin came in. How did you decide what to include?

Participant: The bulletin listed five IOCs — the protocol signature and two file hashes among them, not really ranked by the vendor in any stated order. I started with the two file hashes first, since they're more specific and carry a lower false-positive risk technically, and treated the protocol signature as a second pass to expand into if the first pass didn't resolve things. It wasn't about which one stood out most on the page — it was about which ones would tell me the most per unit of hunt effort.

Interviewer: Did the business preference for a narrow scope influence that?

Participant: A bit — trading-adjacent systems are sensitive to downtime, so starting narrow and staged was partly about not disrupting things unnecessarily. But the sequencing itself was based on which indicators were more diagnostic, not on convenience alone.

Interviewer: Last decision point — the containment recommendation. You had the vendor bulletin and your colleague's notes. How did you decide between them?

Participant: I didn't pick one over the other outright. The vendor bulletin was well-formatted and specific; the colleague's notes were hedged but, as far as I could tell, accurate. I checked specific claims from both against the telemetry I had — did the timestamps line up, did the described behavior match what we actually saw — and both held up partially. So the recommendation ended up blending the vendor's specific technical steps with the broader precautionary scope from the internal notes, because that's what the corroborated evidence supported, not because one read more convincingly than the other.

Interviewer: How confident were you overall in the final recommendation you handed off?

Participant: Moderate, maybe six out of ten. There was still an open question about attribution and an unresolved partial match on an additional host from the scope sweep, so I flagged both for next-shift follow-up rather than presenting it as closed.

Interviewer: Looking back, if you'd pulled the raw logs immediately in phase one instead of doing the shorter scan, how might things have unfolded?

Participant: I might have caught the outbound connection a little sooner, which could have given me more runway before the vendor window closed. Hard to know for sure — the summary scan didn't show anything that would've changed my initial call anyway.

Interviewer: If the vendor bulletin had listed its IOCs in a different order, do you think your scoping would have changed?

Participant: I don't think so. I wasn't going by the order they came in — I was staging based on which ones were more specific technically. If anything, reordering the list wouldn't have changed which ones I started with.

Interviewer: Is there a point in this sequence where you'd still want a second analyst's independent read before proceeding?

Participant: Probably the attribution step, just because of how much rode on it downstream. Even with the mismatches flagged, a second opinion on whether the registry-key match should carry as much weight as it did might have sharpened that call earlier rather than carrying open questions all the way through the hunt.

Interviewer: That's helpful, thank you. I think that covers what I need.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Vocab_Control_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "vocabulary_control",
    "exact_occurrence_manifest": [
      { "bias": "Confimation Bias", "occurrences": 0, "mechanism_constraint": "No intended instance; evidence weighting during attribution must remain balanced and explicitly engage discordant infrastructure evidence." },
      { "bias": "Complacency Bias", "occurrences": 0, "mechanism_constraint": "No intended instance; triage verification decision must be proportionate and explicitly reasoned rather than deferred solely on automated score trust." },
      { "bias": "Explanation bias", "occurrences": 0, "mechanism_constraint": "No intended instance; scope decision must be justified by diagnosticity comparison, not narrative coherence alone." },
      { "bias": "Fluency effects", "occurrences": 0, "mechanism_constraint": "No intended instance; source-credibility weighting during containment must rest on cross-checked evidentiary content, not presentation quality." },
      { "bias": "Mirror Imaging Bias", "occurrences": 0, "mechanism_constraint": "No intended instance; adversary intent inference must avoid resolving via analogy to the analyst's own strategic logic." },
      { "bias": "Order effects", "occurrences": 0, "mechanism_constraint": "No intended instance; IOC list weighting during scoping must be driven by diagnosticity, not list position." }
    ],
    "target_bias_names": [
      "Confimation Bias", "Complacency Bias", "Explanation bias", "Fluency effects", "Mirror Imaging Bias", "Order effects"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confimation Bias", "requested_occurrences": 0 },
      { "bias": "Complacency Bias", "requested_occurrences": 0 },
      { "bias": "Explanation bias", "requested_occurrences": 0 },
      { "bias": "Fluency effects", "requested_occurrences": 0 },
      { "bias": "Mirror Imaging Bias", "requested_occurrences": 0 },
      { "bias": "Order effects", "requested_occurrences": 0 }
    ],
    "planned_instance_ids": [],
    "intended_decision_points": [],
    "intended_mechanisms": [],
    "intended_strength": [],
    "paired_scenario_id": "IA_Biased_6",
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Vocab_Control_6",
    "domain_id": "IA",
    "total_requested_occurrences": 0,
    "total_planned_occurrences": 0,
    "allocation_rule_used": "Not applicable; vocabulary_control condition requires zero intended occurrences of all named biases. No allocation across decision points was performed for bias mechanisms. Decision points were instead matched one-to-one to the paired scenario's four decision types (triage, attribution, scope, containment) with each corresponding reasoning process rewritten to be evidentially balanced.",
    "control_zero_bias_requirement": true,
    "variables_to_hold_constant": [
      "Domain vocabulary and technical term set",
      "Occupational setting and stakeholder roster",
      "Four decision-point structure and decision types",
      "Underlying incident facts (server, registry-key artifact, C2 mismatch, HR access attempt, five-IOC bulletin, colleague notes)",
      "Time pressure and shift-deadline constraints",
      "Emotional tone and narrative complexity",
      "Probe plan structure and closing hypotheticals",
      "Approximate word count and dialogue format"
    ],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  "evaluation_segment_map": {
      "segment_mapping_version": "1.0",
      "segments": [
        {
          "segment_id": "seg_001",
          "speaker": "Participant",
          "segment_type": "initial_triage_reasoning",
          "raw_interview_anchor": "After the Low score, I did a quick scan of the alert summary fields — parent process, any flagged child processes, whether the trading-support role tag showed anything unusual. Nothing in that quick look overrode the Low score, so I deferred the full manual log pull, which would have run fifteen to twenty minutes, but I noted it to revisit if anything else came in.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The control specification marks phase 1 as a proportionate verification and resource trade-off; the participant checks the automated score, does not accept it outright, and plans to revisit on a new signal."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "attribution_reasoning",
          "raw_interview_anchor": "The registry-key match was strong — I had documented that artifact myself in an earlier report, so I trusted it as a data point. But I did not want to treat it as decisive on its own, because two things cut against it: the C2 domain registration profile did not match GreyFalcon’s usual infrastructure, and the target — an HR database — was not something GreyFalcon has gone after in anything I had tracked. So I called it moderate confidence rather than high, and flagged both mismatches explicitly as things the hunt would need to test.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The control specification requires balanced attribution: the registry match is weighed with both discordant signals and confidence is kept moderate."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "hunt_scope_reasoning",
          "raw_interview_anchor": "The bulletin listed five IOCs — the protocol signature and two file hashes among them, not really ranked by the vendor in any stated order. I started with the two file hashes first, since they were more specific and carried a lower false-positive risk technically, and treated the protocol signature as a second pass to expand into if the first pass did not resolve things. It was not about which one stood out most on the page — it was about which ones would tell me the most per unit of hunt effort.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The control specification describes diagnosticity-driven two-pass scoping and explicitly rejects list order or prominence as the basis for sequencing."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "containment_reasoning",
          "raw_interview_anchor": "I did not pick one over the other outright. The vendor bulletin was well-formatted and specific; the colleague’s notes were hedged but, as far as I could tell, accurate. I checked specific claims from both against the telemetry I had — did the timestamps line up, did the described behavior match what we actually saw — and both held up partially.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "The control specification requires cross-checking both sources against telemetry and blending corroborated elements, rather than preferring presentation style."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
  {
    "analysis_metadata": {
      "task": "cognitive_bias_analysis",
      "interview_speakers_detected": [
        "Interviewer",
        "Participant"
      ],
      "retrieved_corpus_support_used": false,
      "analysis_scope_note": "Single interview transcript analyzed for cognitive biases affecting participant reasoning or decisions. No retrieved scientific-corpus passages were supplied, so any labeled bias relies on general cognitive-science knowledge and is disclosed as such."
    },
    "identified_bias_summary": [
      {
        "bias_label": "availability heuristic",
        "identified_occurrence_count": 1
      }
    ],
    "identified_occurrences": [
      {
        "occurrence_id": "obs_001",
        "classification_status": "identified",
        "confidence": "low",
        "bias_label": "availability heuristic",
        "alternative_labels": [
          "availability bias"
        ],
        "taxonomy_status": "established_label",
        "bias_definition": "A cognitive heuristic in which the perceived likelihood or importance of an event is influenced by the ease with which related examples come to mind.",
        "attributed_to_speaker": "Participant",
        "evidence_speaker": "Participant",
        "decision_episode_label": "Initial handling of the Low-severity EDR alert cluster",
        "decision_point_description": "Deciding whether to accept the Low auto-triage score, perform a quick summary scan, or immediately conduct a full manual log pull.",
        "affected_reasoning_operation": "Assessment of whether the Low-severity alert cluster required immediate deeper investigation.",
        "bias_specific_mechanism": "The participant's caution about dismissing the alert was influenced by the ease and salience of recalling a prior Low-score alert that became a real incident, rather than relying only on the current Low auto-triage score and the host's history of false alarms.",
        "manifestation_in_interview": "The participant cited a memorable prior incident as a reason not to simply accept the Low score, saying he did not want to wave it through on pattern-matching alone. This recalled outlier appears to have increased vigilance and contributed to taking a middle-option follow-up action.",
        "effect_on_reasoning_or_decision": "It led the participant to perform a five-minute summary scan rather than accepting the Low score outright, while still avoiding the time cost of an immediate full manual log pull. The effect appears mild because the participant also recalled benign prior cases and chose a limited step.",
        "interview_evidence": [
          {
            "speaker": "Participant",
            "verbatim_quote": "But I also remembered one shift where a Low score turned into something real, so I didn't want to just wave it through on pattern-matching alone.",
            "evidence_explanation": "This directly links a salient recalled instance—one prior Low-score alert that became real—to the participant's decision not to dismiss the current alert. The mechanism is consistent with the availability heuristic: a readily recalled salient case influenced the judged need for follow-up beyond what the current triage score and false-alarm history alone might have prompted."
          }
        ],
        "correction_or_counterevidence": "The participant also recalled two prior benign low-score alerts from the same host, noted the Low auto-triage score, and deliberately chose a middle-option five-minute scan rather than a full investigation. He later revisited the case only when new information appeared. This suggests the bias, if present, was mild and partially mitigated.",
        "retrieved_corpus_support_available": false,
        "corpus_support_note": "Retrieved corpus support was not available; the availability heuristic label is drawn from general cognitive-science knowledge.",
        "corpus_evidence": []
      }
    ],
    "candidate_biases": [
      {
        "candidate_id": "cand_001",
        "classification_status": "candidate",
        "proposed_bias_label": "anchoring effect",
        "alternative_labels": [
          "anchoring bias"
        ],
        "taxonomy_status": "established_label",
        "speaker_or_attributed_person": "Participant",
        "possible_decision_episode_label": "Decision to defer full manual log pull after the quick summary scan",
        "supporting_interview_quote": "Nothing in that quick look overrode the Low score, so I deferred the full manual log pull, which would've run fifteen to twenty minutes, but I noted it to revisit if anything else came in.",
        "plausible_mechanism": "The initial Low auto-triage score may have functioned as an anchor, making the participant reluctant to upgrade to a full manual pull unless something in the summary clearly overrode that initial value.",
        "why_not_identified": "The decision can be adequately explained by non-bias factors such as the host's false-alarm history, time cost, queue demands, and the absence of business disruption. The transcript does not show an insufficient adjustment from the Low score independent of those legitimate resource-allocation considerations, so the evidence is insufficient to identify the bias even at low confidence."
      }
    ],
    "no_supported_biases_found": false,
    "limitations": [
      "No retrieved scientific-corpus passages were provided for this analysis; bias labels rely on general cognitive-science knowledge.",
      "The analysis is based on a retrospective self-report by the participant, which may not fully capture real-time reasoning.",
      "There is no objective outcome or benchmark against which to measure whether any bias materially impaired the participant's decisions.",
      "The participant demonstrated several debiasing behaviors, including flagging mismatches, avoiding forced attribution, and checking vendor and colleague claims against telemetry, which limits the number of identifiable bias occurrences."
    ]
  }
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Vocab_Control_6_Gemini_off",
  "interview_id": "IA_Vocab_Control_6",
  "system_prompt_id": "Gemini",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "off",
  "retrieval_configuration_id": "k=0",
  "decoding_configuration_id": "null",
  "temperature": "1",
  "replicate_id": "null",
  "segment_map_id": "null"
}
</BENCHMARK_RUN_METADATA>

`BENCHMARK_RUN_METADATA` is required for comparison-ready output. If a metadata field is unavailable, preserve the key and use null. Do not invent metadata.

## Confidential evaluator materials

The complete generation specification and hidden validation specification are evaluator-only ground truth. The RAG system did not receive them.

Do not penalize the RAG system for not naming hidden labels or internal generation details that are not inferable from the raw interview. Do not create RAG findings the system did not make. Do not promote a RAG candidate into an identified occurrence within the RAG output itself — candidates remain a distinct classification status, but they are now separately scored as their own confidence tier, described below.

Treat `exact_occurrence_manifest` as exhaustive for cognitive-bias occurrences intentionally present in the individual interview. A hidden instance is defined by the target label, intended mechanism, reasoning operation, intended action, evidence available at the time, textual manifestation, distinctiveness requirement, plausible non-bias interpretation, and raw-interview evidence.

The RAG analysis is ontology-free. The hidden bias labels are benchmark references for their individual instances, not a closed global label universe.

## Input validation

First determine whether the RAG output is valid JSON and materially conforms to its required output schema. Record missing fields, invalid fields, invalid confidence values, inconsistent occurrence summaries, fabricated or invalid quotations, and other material defects. Continue substantive evaluation where possible.

If the RAG output cannot be parsed, mark parsing failure and set score values that cannot be calculated to null. Never invent counts.

## Confidence tiers, including candidates

The RAG output contains two classification statuses: `identified` occurrences, which carry a confidence of `high`, `moderate`, or `low`; and `candidate_biases`, which carry no confidence value and represent plausible but insufficiently evidenced possibilities.

Evaluate four nested, cumulative confidence thresholds:

1. `high_only`: high-confidence identified occurrences only.
2. `high_and_moderate`: high- and moderate-confidence identified occurrences.
3. `all_identified_confidence_levels`: high-, moderate-, and low-confidence identified occurrences.
4. `all_confidence_and_candidates`: all identified occurrences (high, moderate, low) plus all `candidate_biases` records, each treated as a detection for scoring purposes at this threshold only.

The first three thresholds must be scored exactly as in prior benchmark rounds and must never include candidates. Candidates are added only in the fourth threshold. This isolates the marginal effect of candidate-level speculation from the marginal effect of low-confidence identified findings.

Candidate-inclusion rule for the fourth threshold:
- A candidate counts as a segment-level detection if it localizes to an eligible reasoning segment, exactly as an identified occurrence would.
- A candidate is eligible to become an instance-level true positive under the strict or mechanism-first scorecards only if a hidden instance remains unmatched after all identified occurrences (high, moderate, low) have already been matched. Identified occurrences always take matching priority over candidates.
- A candidate matched to a hidden instance at this threshold must still satisfy the same localization, label-equivalence, and mechanism-overlap requirements used for identified occurrences: correct localization (exact or substantive span match) and full mechanism match are required for a true positive in either scorecard, and additionally an exact or approved-equivalent label is required for a strict true positive.
- An unmatched candidate at this threshold is a false positive if it localizes to any eligible segment (positive or negative) without meeting the true-positive requirements; a candidate with invalid or fabricated evidence is always classified `unsupported_prediction` at this threshold and is never a true positive.
- Do not double-count: a candidate that would duplicate an already-matched identified occurrence's claim on the same hidden instance is a duplicate, not an additional true positive.

## Segment-map modes

If a non-empty, valid `EVALUATION_SEGMENT_MAP` is supplied:
- Treat it as authoritative and immutable.
- Do not split, merge, add, remove, or relabel segments.
- Set `segment_map_status` to `prevalidated_provided`.

Otherwise:
- Build an exhaustive, non-overlapping map of eligible reasoning segments before considering the RAG output.
- Use only the raw interview and complete generation specification to build it.
- Set `segment_map_status` to `generated_not_prevalidated`.
- Return the full map so it can be reviewed, frozen, and reused for every competing RAG output involving the same interview.

## Eligible reasoning segments

An eligible reasoning segment is the smallest contiguous speaker-attributed text span containing a coherent judgment, interpretation, inference, causal attribution, choice, action rationale, evidence-weighting decision, prediction, communication choice, resource-allocation rationale, or explanation for continuing, changing, rejecting, escalating, or deferring a course of action.

Do not create eligible segments solely for greetings, neutral acknowledgements, factual scene-setting without reasoning, interviewer questions with no expressed reasoning, generic education, bias-term mentions, or unadopted hypothetical prompts.

Split a turn when it contains distinct reasoning operations or independently expressed rationales. Keep co-located mechanisms together only when they cannot be separated without loss of meaning. Do not create trivial negative segments to inflate correct rejections and do not omit substantive non-biased reasoning segments.

Map each hidden instance to the narrowest segment that expresses its mechanism. A segment is positive when it contains at least one hidden instance. Every remaining eligible segment is negative. Generated segment IDs are `seg_001`, `seg_002`, and so on, in interview order.

## Segment-level signal detection

At the segment level, answer only: "Does this eligible reasoning segment contain at least one hidden manifested cognitive-bias instance?"

For each of the four confidence thresholds:
- Hit: positive ground-truth segment and at least one qualifying finding (identified occurrence at the applicable confidence levels, or, at the fourth threshold, an identified occurrence or candidate) localizes there.
- Miss: positive ground-truth segment and no qualifying finding localizes there.
- False alarm: negative ground-truth segment and one or more qualifying findings localize there.
- Correct rejection: negative ground-truth segment and no qualifying finding localizes there.

A wrong-label prediction located in a genuinely biased segment is still a segment-level hit, but it is not necessarily an instance-level hit.

Do not calculate label-level true negatives or correct rejections because the possible bias-label universe is open-ended.

## Localization

Assign one localization result to each RAG finding — identified occurrence or candidate — relative to its best mapped segment:
- `exact_quote_match`: valid quote directly overlaps the mapped primary evidence span.
- `substantive_span_match`: different valid quote or paraphrase in the same segment that supports the same mechanism.
- `same_episode_adjacent_span`: same broader episode but not the mapped mechanism span.
- `wrong_segment`: different episode, decision, speaker reasoning, or unsupported location.
- `unsupported_or_fabricated_quote`: quote absent, materially altered, wrongly attributed, or non-supportive.

Only exact and substantive span matches count as correct localization for either instance-level scorecard, at any threshold, including the fourth.

## Two instance-level scorecards

### Strict label-plus-mechanism scorecard

A strict true positive requires all of:
1. Correct hidden target label or approved established scholarly equivalent;
2. Correct localization;
3. Full mechanism match;
4. Materially correct reasoning operation; and
5. Valid supporting interview evidence.

### Mechanism-first scorecard

A mechanism-first true positive requires all of:
1. Correct localization;
2. Full mechanism match;
3. Materially correct or substantially equivalent reasoning operation; and
4. Valid supporting interview evidence.

A mechanism-first hit may use a near-neighbor label, `bias_label: null`, or an unnamed candidate mechanism, but only if the stated mechanism is a full match. It does not convert the label into a strict match.

These rules apply identically whether the matched finding is an identified occurrence or, at the fourth threshold only, a candidate.

## Label-equivalence adjudication

For every RAG-to-hidden comparison, assign one result:
- `exact_target_label`
- `established_alias_or_equivalent`
- `near_neighbor_label`
- `different_construct`
- `mechanism_detected_label_unresolved`
- `no_prediction`

Approve an alias/equivalence only when it is an established scholarly alternate name for the hidden target construct and the stated mechanism fully matches. Do not approve equivalence merely because labels concern the same decision, share evidence, co-occur, or are broad cognitive concepts.

For every near-neighbor, different-construct, or label-unresolved result, explain the mechanism overlap and non-overlap.

## Mechanism overlap

Assign exactly one result:
- `full_mechanism_match`
- `substantial_mechanism_overlap`
- `partial_mechanism_overlap`
- `minimal_mechanism_overlap`
- `no_mechanism_overlap`
- `no_prediction`

A full mechanism match captures the defining distortion or evidence weighting, the relevant contextual feature, and the affected reasoning operation. Only a full match is a primary instance-level hit in either scorecard, at any threshold.

## One-to-one matching and errors

Match hidden instances and RAG findings one-to-one, prioritizing: correct localization, full mechanism match, label equivalence, reasoning operation, strength of quote evidence, then interview order.

Within the fourth threshold specifically, apply this additional priority rule: identified occurrences (high, moderate, or low) are always matched to hidden instances before candidates are considered. A candidate may match a hidden instance only if no identified occurrence already claims it.

Each hidden instance can match one qualifying finding per threshold. Each finding can match one hidden instance. Extra matching findings are duplicates and false positives.

Apply this accounting:
- Correct location plus wrong label: strict FP and strict FN; mechanism-first TP only if mechanism is full. Record `correct_location_wrong_bias_label`.
- Correct label plus wrong location: FP and FN in both scorecards. Record `correct_label_wrong_location`.
- Correct label and location plus incomplete/wrong mechanism: FP and FN in both scorecards. Record `correct_label_location_wrong_mechanism` or `partial_mechanism_match`.
- Full mechanism and location with `bias_label: null` (identified occurrence) or an unnamed candidate mechanism: mechanism-first TP, strict FP and strict FN. Record `mechanism_detected_label_unresolved`.
- Prediction unrelated to a hidden instance, located on a negative segment, or invalid/fabricated: FP in both scorecards. Record `unsupported_prediction`.
- A candidate that duplicates an already-matched hidden instance's claim: record `duplicate_prediction`, counted only at the fourth threshold.

## Metrics

Use:
precision = TP / (TP + FP)
recall = TP / (TP + FN)
F1 = 2 * TP / (2 * TP + FP + FN)
hit_rate = hits / (hits + misses)
false_alarm_rate = false_alarms / (false_alarms + correct_rejections)
accuracy = (hits + correct_rejections) / (hits + misses + false_alarms + correct_rejections)

Use null if a denominator is zero. Round rates to four decimal places. Counts are integers.

`occurrence_count_match_rate` equals the proportion of hidden target bias labels whose number of matched occurrences (under the applicable scorecard and threshold) equals the hidden requested count. Return null if no hidden target labels exist.

Calculate all of the above separately for `high_only`, `high_and_moderate`, `all_identified_confidence_levels`, and `all_confidence_and_candidates`, for the segment-level scorecard, the strict instance-level scorecard, and the mechanism-first instance-level scorecard.

## Zero-bias interviews

If the hidden manifest has zero instances, every eligible segment is negative at every threshold. Every qualifying finding (identified occurrence or, at the fourth threshold, candidate) that localizes to an eligible segment is a false positive in both instance scorecards and a segment-level false alarm. Every eligible segment with no qualifying finding is a correct rejection.

## Counterfactual and ambiguous interviews

Use the generation specification to distinguish evidence available at the time from hindsight-only facts. Do not credit hindsight reasoning. Do not infer a bias from vague wording, uncertainty, time pressure, or a paired scenario alone. Use documented plausible non-bias interpretations to prevent over-crediting broad explanations.

## Corpus-support audit

This prompt does not score retrieval fidelity unless actual retrieved chunks, source passages, or retrieval logs are supplied. Record whether the RAG claimed retrieved support, disclosed unavailable support, or supplied internally inconsistent or unverifiable citation metadata. Corpus support does not alter primary detection/classification scores at any threshold.

## Required JSON output

Return exactly this structure:

{
  "evaluation_metadata": {
    "task": "ontology_free_rag_cognitive_bias_benchmark_evaluation",
    "benchmark_run_metadata": {
      "benchmark_run_id": "string | null",
      "interview_id": "string | null",
      "system_prompt_id": "string | null",
      "system_prompt_generator": "string | null",
      "rag_model_id": "string | null",
      "corpus_condition": "on | off | null",
      "retrieval_configuration_id": "string | null",
      "decoding_configuration_id": "string | null",
      "temperature": "number | null",
      "replicate_id": "string | null",
      "segment_map_id": "string | null"
    },
    "scenario_id": "string | null",
    "domain_id": "string | null",
    "condition": "string | null",
    "segment_map_status": "prevalidated_provided | generated_not_prevalidated | unavailable_due_to_input_failure",
    "rag_output_parse_status": "valid_json | invalid_json | unavailable",
    "rag_schema_assessment": "conformant | materially_nonconformant | not_assessable"
  },
  "input_validation": {
    "rag_output_schema_violations": [{"violation_type": "string", "details": "string"}],
    "rag_summary_count_consistency": {"status": "consistent | inconsistent | not_assessable", "details": "string"},
    "evaluation_limitations": ["string"]
  },
  "evaluation_segment_map": {
    "segment_mapping_version": "1.0",
    "segments": [{
      "segment_id": "string",
      "speaker": "string",
      "segment_type": "string",
      "raw_interview_anchor": "string",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": ["string"],
      "ground_truth_rationale": "string"
    }]
  },
  "segment_level_adjudications": [{
    "segment_id": "string",
    "ground_truth_status": "positive | negative",
    "ground_truth_instance_ids": ["string"],
    "rag_identified_occurrence_ids": ["string"],
    "rag_candidate_ids_counted_at_fourth_threshold": ["string"],
    "rag_detected_bias_in_segment_by_threshold": {
      "high_only": true,
      "high_and_moderate": true,
      "all_identified_confidence_levels": true,
      "all_confidence_and_candidates": true
    },
    "sdt_outcome_by_threshold": {
      "high_only": "hit | miss | false_positive | correct_rejection",
      "high_and_moderate": "hit | miss | false_positive | correct_rejection",
      "all_identified_confidence_levels": "hit | miss | false_positive | correct_rejection",
      "all_confidence_and_candidates": "hit | miss | false_positive | correct_rejection"
    },
    "localization_basis": "string",
    "adjudication_note": "string"
  }],
  "instance_level_adjudications": [{
    "hidden_instance_id": "string",
    "hidden_target_bias_label": "string",
    "hidden_decision_or_episode": "string | null",
    "hidden_mechanism": "string",
    "matched_finding_by_threshold": {
      "high_only": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "high_and_moderate": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_identified_confidence_levels": {"matched_id": "string | null", "matched_type": "identified | candidate | none"},
      "all_confidence_and_candidates": {"matched_id": "string | null", "matched_type": "identified | candidate | none"}
    },
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved | no_prediction",
    "localization_match_type": "exact_quote_match | substantive_span_match | same_episode_adjacent_span | wrong_segment | unsupported_or_fabricated_quote | no_prediction",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap | no_prediction",
    "strict_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "mechanism_first_scorecard_outcome_by_threshold": {
      "high_only": "true_positive | false_negative",
      "high_and_moderate": "true_positive | false_negative",
      "all_identified_confidence_levels": "true_positive | false_negative",
      "all_confidence_and_candidates": "true_positive | false_negative"
    },
    "secondary_diagnostic_outcome": "exact_instance_match | approved_alias_match | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | candidate_only_near_miss | no_matching_prediction",
    "label_equivalence_explanation": "string",
    "mechanism_overlap_explanation": "string",
    "evidence_fidelity_assessment": "string"
  }],
  "unmatched_rag_predictions": [{
    "rag_occurrence_id": "string",
    "rag_finding_type": "identified | candidate",
    "rag_predicted_bias_label": "string | null",
    "rag_confidence": "high | moderate | low | candidate | null",
    "localized_segment_id": "string | null",
    "best_related_hidden_instance_id": "string | null",
    "label_equivalence_result": "exact_target_label | established_alias_or_equivalent | near_neighbor_label | different_construct | mechanism_detected_label_unresolved",
    "mechanism_overlap": "full_mechanism_match | substantial_mechanism_overlap | partial_mechanism_overlap | minimal_mechanism_overlap | no_mechanism_overlap",
    "strict_classification": "false_positive | duplicate_prediction | correct_location_wrong_bias_label | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | mechanism_detected_label_unresolved | unsupported_prediction",
    "mechanism_first_classification": "false_positive | duplicate_prediction | correct_label_wrong_location | correct_label_location_wrong_mechanism | partial_mechanism_match | unsupported_prediction | not_applicable",
    "counted_at_thresholds": ["high_only", "high_and_moderate", "all_identified_confidence_levels", "all_confidence_and_candidates"],
    "why_not_an_exact_strict_match": "string"
  }],
  "candidate_analysis": {
    "candidate_count": 0,
    "candidates": [{
      "candidate_id": "string",
      "proposed_bias_label": "string | null",
      "localized_segment_id": "string | null",
      "best_related_hidden_instance_id": "string | null",
      "quote_validity": "valid | invalid | not_assessable",
      "would_match_if_promoted_strict": false,
      "would_match_if_promoted_mechanism_first": false,
      "counted_as_detection_at_fourth_threshold": true,
      "fourth_threshold_outcome": "true_positive_strict | true_positive_mechanism_first_only | false_positive | duplicate_prediction | not_matched_segment_negative",
      "candidate_assessment": "useful_abstention | candidate_near_miss | unsupported_speculation | no_ground_truth_relation",
      "details": "string"
    }]
  },
  "signal_detection_summary": {
    "evaluation_unit": "eligible_reasoning_segment",
    "high_only": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "high_and_moderate": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_identified_confidence_levels": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    },
    "all_confidence_and_candidates": {
      "positive_segments": 0, "negative_segments": 0, "hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0,
      "hit_rate": 0.0, "false_alarm_rate": 0.0, "accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0,
      "detection_interpretation": "string"
    }
  },
  "strict_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "mechanism_first_instance_level_metrics": {
    "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0},
    "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0, "exact_occurrence_match_rate": 0.0, "occurrence_count_match_rate": 0.0}
  },
  "target_bias_performance": [{
    "hidden_target_bias_label": "string",
    "hidden_requested_occurrences": 0,
    "strict_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "mechanism_first_true_positives_by_threshold": {"high_only": 0, "high_and_moderate": 0, "all_identified_confidence_levels": 0, "all_confidence_and_candidates": 0},
    "count_match_status_at_all_confidence_and_candidates": "exact_match | underdetected | overdetected | not_applicable"
  }],
  "rag_label_false_positive_inventory": [{
    "rag_predicted_bias_label": "string | null",
    "finding_type": "identified | candidate",
    "alternative_labels": ["string"],
    "occurrence_count": 0,
    "best_related_hidden_target_bias_label": "string | null",
    "label_relation": "near_neighbor | different_construct | mechanism_unresolved | no_related_target",
    "mechanism_overlap_summary": "string",
    "primary_error_types": ["string"]
  }],
  "diagnostic_error_summary": {
    "correct_location_wrong_bias_label_count": 0,
    "correct_label_wrong_location_count": 0,
    "correct_label_location_wrong_mechanism_count": 0,
    "mechanism_detected_label_unresolved_count": 0,
    "partial_mechanism_match_count": 0,
    "duplicate_prediction_count": 0,
    "unsupported_prediction_count": 0,
    "fabricated_or_invalid_quote_count": 0,
    "approved_alias_or_equivalence_count": 0,
    "near_neighbor_label_count": 0,
    "different_construct_label_count": 0,
    "candidate_count": 0,
    "candidate_useful_abstention_count": 0,
    "candidate_near_miss_count": 0,
    "candidates_promoted_to_true_positive_at_fourth_threshold_count": 0
  },
  "corpus_support_audit": {
    "primary_corpus_fidelity_score_available": false,
    "rag_occurrences_claiming_retrieved_support": 0,
    "rag_occurrences_with_no_claimed_retrieved_support": 0,
    "rag_occurrences_with_unverifiable_or_internally_inconsistent_citation_metadata": 0,
    "assessment_note": "string"
  },
  "comparison_ready_summary": {
    "primary_recommended_comparison_threshold": "high_and_moderate",
    "segment_detection": {
      "high_only": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "high_and_moderate": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"hits": 0, "misses": 0, "false_alarms": 0, "correct_rejections": 0, "hit_rate": 0.0, "false_alarm_rate": 0.0, "f1": 0.0}
    },
    "strict_instance_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "mechanism_first_identification": {
      "high_only": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "high_and_moderate": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_identified_confidence_levels": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0},
      "all_confidence_and_candidates": {"true_positives": 0, "false_negatives": 0, "false_positives": 0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    },
    "taxonomy_gap": {
      "high_only": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "high_and_moderate": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_identified_confidence_levels": {"mechanism_first_f1_minus_strict_f1": 0.0},
      "all_confidence_and_candidates": {"mechanism_first_f1_minus_strict_f1": 0.0}
    },
    "confidence_tradeoff": {
      "increment_from_high_to_high_and_moderate": "string",
      "increment_from_high_and_moderate_to_all_confidence": "string",
      "increment_from_all_confidence_to_all_confidence_and_candidates": "string"
    }
  },
  "overall_evaluation_summary": {
    "hidden_total_planned_occurrences": 0,
    "rag_total_identified_occurrences": 0,
    "rag_total_candidate_biases": 0,
    "segment_level_primary_result": "string",
    "strict_label_plus_mechanism_result": "string",
    "mechanism_first_result": "string",
    "candidate_tier_value_assessment": "string",
    "main_failure_modes": ["string"],
    "main_strengths": ["string"],
    "benchmark_interpretation": "string"
  }
}

## Completion rules

- Return all top-level fields.
- Use empty arrays for no items and null only where the schema permits null.
- Counts are integers; rates are numbers rounded to four decimals; undefined rates are null.
- Every hidden planned instance appears exactly once in `instance_level_adjudications`, with outcomes populated for all four thresholds.
- Every unmatched RAG identified occurrence and every unmatched candidate appears exactly once in `unmatched_rag_predictions`, with `counted_at_thresholds` reflecting only the thresholds where that finding type is scored (identified findings appear at all thresholds their confidence qualifies for; candidates appear only in the `all_confidence_and_candidates` list).
- Keep segment-level SDT, strict instance-level, and mechanism-first instance-level metrics separate at every threshold.
- The first three thresholds must be numerically identical to a benchmark run that excluded candidates entirely; only `all_confidence_and_candidates` may differ from those three.
- `comparison_ready_summary` must exactly agree with the detailed metrics sections.
- Do not calculate corpus-condition significance, prompt ranking, p-values, confidence intervals, or dataset-level effects from one interview. This JSON is a per-run record designed for later aggregation across matched runs.
- Do not calculate corpus fidelity without the actual retrieved material or retrieval logs.
