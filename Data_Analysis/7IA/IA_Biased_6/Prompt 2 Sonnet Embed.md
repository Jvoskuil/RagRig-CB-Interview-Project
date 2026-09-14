You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this conversation is being recorded for internal process review, and I'll ask you to walk me through a specific shift in detail. You can skip anything you're not comfortable sharing. Can you tell me your role and how long you've been doing it?

Participant: Sure. I'm a threat intelligence analyst on the SOC team, been in this seat about four years, mostly financial services environments. My job during shift is triage, attribution, and hunt scoping when something looks like it's more than commodity noise.

Interviewer: Good. Let's start broad. Can you walk me through what this shift looked like when the alert cluster first appeared?

Participant: It was maybe two hours into an overnight shift. EDR kicked out a cluster of alerts on a trading-support server — not the trading engine itself, but a box that feeds reporting data to it. The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing.

Interviewer: What was your primary objective at that point?

Participant: Get through the queue, keep the shift moving, and not waste the incident response lead's time on something that turns out to be benign. We only had about three hours left in the shift, and I wanted whatever I handed off to be solid, not a guess.

Interviewer: Take me through what happened next, chronologically.

Participant: So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet. About forty minutes later, a follow-up alert showed an outbound connection from that same host to an IP I didn't recognize. That's when I actually opened the case properly. I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me. Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway. Then I pulled a vendor bulletin that had just come in — the vendor portal access was closing soon, so I read it quickly. It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that. Near the end of shift, I had to write up a containment recommendation for the IR lead, and I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of "possibly" and "unclear."

Interviewer: Let's slow down and go through each of those decisions one at a time. First one — the initial Low-severity alert. What cues were you weighing right then?

Participant: Mainly the auto-triage score and my own memory of that server generating false alarms before. No unusual business disruption was reported either, which reinforced it felt routine.

Interviewer: What made you decide to defer the manual log pull rather than doing it right away?

Participant: Time, mostly. The score was Low, I had precedent that Low from that host usually meant nothing, and pulling raw logs is a real time cost. Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me. It felt like a reasonable use of triage priority rather than checking every single alert by hand.

Interviewer: Did you consider escalating to the IR lead first instead?

Participant: I thought about it, but that seemed like overkill for a Low score with no other signal at that point. In hindsight, I probably could've spent the fifteen minutes given how the next forty minutes went, but at the time it didn't seem to justify interrupting anyone.

Interviewer: Understood. Let's move to the attribution decision after the outbound connection appeared. What was the basis for assigning GreyFalcon?

Participant: The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in.

Interviewer: You mentioned the C2 domain's registration pattern looked different from GreyFalcon's usual infrastructure. How did that factor in?

Participant: It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.

Interviewer: And the HR database access attempt — GreyFalcon has typically gone after trading or financial data in your prior tracking. How did you read that mismatch?

Participant: My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly. So it didn't strike me as inconsistent with the group, more like an opportunistic pivot they'd make if they were being efficient about it.

Interviewer: Did you weigh that explanation against the possibility that it wasn't GreyFalcon at all?

Participant: Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.

Interviewer: Let's talk about the hunt scope decision, once the vendor bulletin came in. Walk me through how you decided what to include.

Participant: The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources. There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary.

Interviewer: The bulletin listed two file-hash IOCs last — how much did those factor into the scope?

Participant: Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.

Interviewer: Was there consideration of scoping broadly across all five IOCs regardless of order?

Participant: There was, briefly — business owners wanted it narrow anyway to avoid downtime on trading-adjacent systems, so narrow scope aligned with what they wanted too. That made it easier to just go with the scope that already made sense to me.

Interviewer: Last decision point — the containment recommendation. You mentioned leaning on the vendor bulletin over a colleague's notes. What drove that?

Participant: Time pressure, for one — I needed something to hand the IR lead within the hour. But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — "possibly," "unclear if," that kind of thing. The vendor version gave me something concrete to act on.

Interviewer: Did you compare the actual evidence underlying each source, separate from how they were written?

Participant: Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.

Interviewer: How confident were you overall in the final recommendation you handed off?

Participant: Reasonably confident, maybe seven out of ten. Enough uncertainty that I flagged it as needing follow-up validation next shift, but I felt the containment steps were defensible given what I had.

Interviewer: Looking back across the shift, if you'd pulled the raw logs immediately in phase one instead of deferring, how do you think things would've unfolded differently?

Participant: I might have caught the odd outbound connection sooner, maybe before the vendor window closed, which could've changed how much I leaned on that bulletin later. Hard to say for certain.

Interviewer: If the vendor bulletin had listed its IOCs in reverse order, hash-based ones first, do you think your scoping would have changed?

Participant: Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope.

Interviewer: Is there a point in this sequence where you'd want a second analyst's independent read before proceeding?

Participant: Probably the attribution step. That's where I moved fastest from one piece of strong evidence to a full working theory, and a second set of eyes might have pushed back on the infrastructure mismatch or the HR access pattern before I built the rest of the shift around it.

Interviewer: That's helpful, thank you. I think that covers what I need.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IA_Biased_6",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      { "bias": "Confimation Bias", "occurrences": 1, "mechanism_constraint": "Selective weighting of registry-key IOC over discordant C2 infrastructure pattern during attribution." },
      { "bias": "Complacency Bias", "occurrences": 1, "mechanism_constraint": "Deferred manual verification due to trust in automated EDR severity scoring." },
      { "bias": "Explanation bias", "occurrences": 1, "mechanism_constraint": "Scope decision justified by narrative coherence rather than independent testing of alternative explanation." },
      { "bias": "Fluency effects", "occurrences": 1, "mechanism_constraint": "Preference for polished vendor bulletin over hedged internal notes based on presentation, not evidentiary rigor." },
      { "bias": "Mirror Imaging Bias", "occurrences": 1, "mechanism_constraint": "Adversary target-selection interpreted via analyst's own strategic logic rather than tested against alternative adversary motivations." },
      { "bias": "Order effects", "occurrences": 1, "mechanism_constraint": "Scope decision disproportionately shaped by first-listed IOC in vendor bulletin." }
    ],
    "target_bias_names": [
      "Confimation Bias", "Complacency Bias", "Explanation bias", "Fluency effects", "Mirror Imaging Bias", "Order effects"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Confimation Bias", "requested_occurrences": 1 },
      { "bias": "Complacency Bias", "requested_occurrences": 1 },
      { "bias": "Explanation bias", "requested_occurrences": 1 },
      { "bias": "Fluency effects", "requested_occurrences": 1 },
      { "bias": "Mirror Imaging Bias", "requested_occurrences": 1 },
      { "bias": "Order effects", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cp_01", "bias": "Complacency Bias" },
      { "instance_id": "cb_01", "bias": "Confimation Bias" },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias" },
      { "instance_id": "ex_01", "bias": "Explanation bias" },
      { "instance_id": "oe_01", "bias": "Order effects" },
      { "instance_id": "fl_01", "bias": "Fluency effects" }
    ],
    "intended_decision_points": [
      { "instance_id": "cp_01", "bias": "Complacency Bias", "decision_point": 1 },
      { "instance_id": "cb_01", "bias": "Confimation Bias", "decision_point": 2 },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias", "decision_point": 2 },
      { "instance_id": "ex_01", "bias": "Explanation bias", "decision_point": 3 },
      { "instance_id": "oe_01", "bias": "Order effects", "decision_point": 3 },
      { "instance_id": "fl_01", "bias": "Fluency effects", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cp_01",
        "bias": "Complacency Bias",
        "mechanism": "Trust in automated EDR triage score substitutes for independent manual log verification despite available time.",
        "affected_reasoning_operation": "Verification/evidence-gathering decision",
        "evidence_source": "EDR auto-triage severity score vs. available raw logs",
        "distinctiveness_requirement": "Only complacency instance; tied uniquely to automated tool trust at DP1, distinct from all other instances by decision point and evidence source."
      },
      {
        "instance_id": "cb_01",
        "bias": "Confimation Bias",
        "mechanism": "Registry-key IOC match is treated as confirming evidence for GreyFalcon attribution while the discordant C2 registration pattern is not actively sought or weighted.",
        "affected_reasoning_operation": "Evidence weighting during attribution",
        "evidence_source": "Registry-key artifact match vs. C2 domain registration pattern",
        "distinctiveness_requirement": "Distinct from mi_01 (same DP2) by evidence source: cb_01 uses IOC-matching evidence; mi_01 uses target-selection telemetry and adversary-intent reasoning."
      },
      {
        "instance_id": "mi_01",
        "bias": "Mirror Imaging Bias",
        "mechanism": "Adversary's HR-database target selection is explained via the analyst's own strategic logic ('what I would do to maximize leverage') rather than by testing alternative adversary motivations against GreyFalcon's documented historical pattern.",
        "affected_reasoning_operation": "Inference about adversary intent",
        "evidence_source": "Internal telemetry on HR database access attempt vs. GreyFalcon's historical targeting pattern",
        "distinctiveness_requirement": "Distinct from cb_01 by reasoning operation (intent inference vs. attribution-evidence weighting) though sharing DP2."
      },
      {
        "instance_id": "ex_01",
        "bias": "Explanation bias",
        "mechanism": "Scope decision is justified by the internal coherence of the pre-existing GreyFalcon narrative rather than by independently comparing it against an equally plausible alternative explanation.",
        "affected_reasoning_operation": "Scope-determination reasoning via narrative integration",
        "evidence_source": "Working attribution narrative vs. alternative commodity-malware/insider-misconfiguration explanation",
        "distinctiveness_requirement": "Distinct from oe_01 (same DP3) by mechanism: ex_01 is about narrative-coherence justification, not IOC list ordering."
      },
      {
        "instance_id": "oe_01",
        "bias": "Order effects",
        "mechanism": "The fixed listing order of the vendor bulletin's five IOCs (dramatic signature first) disproportionately shapes the scope decision toward the first-listed item over later, more diagnostic hashes.",
        "affected_reasoning_operation": "Weighting of listed evidence items during scope selection",
        "evidence_source": "Vendor bulletin IOC list order",
        "distinctiveness_requirement": "Distinct from ex_01 by reasoning operation: positional weighting of a list vs. narrative-fit justification, though both occur at DP3."
      },
      {
        "instance_id": "fl_01",
        "bias": "Fluency effects",
        "mechanism": "Confident, polished presentation of the vendor bulletin is treated as an indicator of reliability relative to hedged internal notes, independent of underlying evidentiary rigor.",
        "affected_reasoning_operation": "Source-credibility weighting during containment recommendation",
        "evidence_source": "Vendor bulletin presentation quality vs. internal analyst's hedged raw notes",
        "distinctiveness_requirement": "Only fluency instance; uniquely tied to DP4 containment decision and presentation-based credibility judgment."
      }
    ],
    "intended_strength": [
      { "instance_id": "cp_01", "bias": "Complacency Bias", "strength": "subtle" },
      { "instance_id": "cb_01", "bias": "Confimation Bias", "strength": "subtle" },
      { "instance_id": "mi_01", "bias": "Mirror Imaging Bias", "strength": "subtle" },
      { "instance_id": "ex_01", "bias": "Explanation bias", "strength": "subtle" },
      { "instance_id": "oe_01", "bias": "Order effects", "strength": "subtle" },
      { "instance_id": "fl_01", "bias": "Fluency effects", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IA_Biased_6",
    "domain_id": "IA",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Occurrences spread across 4 decision points respecting mechanism fit: DP1=1 (Complacency), DP2=2 (Confirmation, Mirror Imaging; distinguished by evidence source and reasoning operation), DP3=2 (Explanation bias, Order effects; distinguished by mechanism), DP4=1 (Fluency effects). No decision point received more than two instances, and no two instances of the same bias were assigned, satisfying the manifest's per-bias count of 1 each.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
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
      "segment_type": "initial_assessment",
      "raw_interview_anchor": "My first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The participant judges the alert likely benign from prior false-positive experience. The hidden complacency instance requires the later decision to let the automated score suppress manual verification; this initial impression alone does not meet that mechanism."
    },
    {
      "segment_id": "seg_002",
      "speaker": "Participant",
      "segment_type": "objective_and_resource_rationale",
      "raw_interview_anchor": "Get through the queue, keep the shift moving, and not waste the incident response lead's time on something that turns out to be benign. We only had about three hours left in the shift, and I wanted whatever I handed off to be solid, not a guess.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "This is an explicit workload and handoff objective, a plausible non-bias constraint rather than a hidden target mechanism."
    },
    {
      "segment_id": "seg_003",
      "speaker": "Participant",
      "segment_type": "decision_rationale",
      "raw_interview_anchor": "So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The participant defers because of time and queue pressure. Without the later statement that the score did the deciding, this span alone remains consistent with the documented reasonable-triage interpretation."
    },
    {
      "segment_id": "seg_004",
      "speaker": "Participant",
      "segment_type": "evidence_interpretation",
      "raw_interview_anchor": "I found a registry-key artifact that matched something documented in a GreyFalcon campaign from about six months back — I remembered writing that report myself, so it stuck with me.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "cb_01"
      ],
      "ground_truth_rationale": "The previously known registry-key match is treated as salient evidence in the attribution sequence. This is one chronological manifestation of cb_01, not an additional planned occurrence."
    },
    {
      "segment_id": "seg_005",
      "speaker": "Participant",
      "segment_type": "decision_rationale",
      "raw_interview_anchor": "Around the same time, internal telemetry showed an attempted connection to the HR benefits database from that host, which was strange, but I moved forward with attribution anyway.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The participant notes an anomaly and proceeds, but this span does not yet express the hidden mirror-imaging mechanism of projecting the analyst’s own strategic logic onto the adversary."
    },
    {
      "segment_id": "seg_006",
      "speaker": "Participant",
      "segment_type": "time_allocation_rationale",
      "raw_interview_anchor": "The vendor portal access was closing soon, so I read it quickly.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "This is a time-based reading decision and does not establish a presentation-driven source-credibility judgment."
    },
    {
      "segment_id": "seg_007",
      "speaker": "Participant",
      "segment_type": "scope_choice",
      "raw_interview_anchor": "It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "oe_01"
      ],
      "ground_truth_rationale": "The first-listed IOC is the scope anchor in the chronological account; this is a manifestation of the single planned order-effects instance."
    },
    {
      "segment_id": "seg_008",
      "speaker": "Participant",
      "segment_type": "source_credibility_rationale",
      "raw_interview_anchor": "I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of \"possibly\" and \"unclear.\"",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "fl_01"
      ],
      "ground_truth_rationale": "The participant favors the bulletin by reference to its clean and confident presentation over hedged notes; this is the same planned DP4 fluency instance described again later."
    },
    {
      "segment_id": "seg_009",
      "speaker": "Participant",
      "segment_type": "cue_weighting",
      "raw_interview_anchor": "Mainly the auto-triage score and my own memory of that server generating false alarms before. No unusual business disruption was reported either, which reinforced it felt routine.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The participant lists multiple operational cues, including historical false positives and no reported disruption. This does not by itself meet the hidden requirement that the score explicitly substitutes for independent verification."
    },
    {
      "segment_id": "seg_010",
      "speaker": "Participant",
      "segment_type": "evidence_weighting_and_verification",
      "raw_interview_anchor": "Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "cp_01"
      ],
      "ground_truth_rationale": "This directly manifests the hidden complacency mechanism: the Low score overrides an available anomalous cue and suppresses manual review."
    },
    {
      "segment_id": "seg_011",
      "speaker": "Participant",
      "segment_type": "escalation_rationale",
      "raw_interview_anchor": "I thought about it, but that seemed like overkill for a Low score with no other signal at that point. In hindsight, I probably could've spent the fifteen minutes given how the next forty minutes went, but at the time it didn't seem to justify interrupting anyone.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The participant gives a plausible triage and interruption-cost rationale, while the statement is not needed to establish the explicit tool-overrides-cue mechanism mapped to seg_010."
    },
    {
      "segment_id": "seg_012",
      "speaker": "Participant",
      "segment_type": "attribution_evidence_weighting",
      "raw_interview_anchor": "The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "cb_01"
      ],
      "ground_truth_rationale": "The familiar registry match is elevated into the GreyFalcon frame. This is another textual span for the one planned confirmation-bias instance."
    },
    {
      "segment_id": "seg_013",
      "speaker": "Participant",
      "segment_type": "disconfirming_evidence_weighting",
      "raw_interview_anchor": "It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "cb_01"
      ],
      "ground_truth_rationale": "The participant acknowledges and underweights the discordant infrastructure evidence instead of testing whether it should lower attribution confidence; this is the narrowest full expression of cb_01 and the best RAG localization."
    },
    {
      "segment_id": "seg_014",
      "speaker": "Participant",
      "segment_type": "adversary_intent_inference",
      "raw_interview_anchor": "My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "mi_01"
      ],
      "ground_truth_rationale": "The analyst explains adversary target selection through the analyst’s own strategic logic, the defining mirror-imaging mechanism."
    },
    {
      "segment_id": "seg_015",
      "speaker": "Participant",
      "segment_type": "alternative_hypothesis_assessment",
      "raw_interview_anchor": "Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "mi_01"
      ],
      "ground_truth_rationale": "The participant accepts the projected motive without testing the alternative attribution; this is a separate interview span reiterating the same planned MI instance."
    },
    {
      "segment_id": "seg_016",
      "speaker": "Participant",
      "segment_type": "scope_evidence_weighting",
      "raw_interview_anchor": "The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "oe_01"
      ],
      "ground_truth_rationale": "The first-listed IOC and prior working frame shape the chosen scope; this is another span of the same planned order-effects occurrence."
    },
    {
      "segment_id": "seg_017",
      "speaker": "Participant",
      "segment_type": "narrative_based_scope_justification",
      "raw_interview_anchor": "It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "ex_01"
      ],
      "ground_truth_rationale": "The narrative’s coherence is offered as the reason to allocate hunt resources, matching the hidden explanation-bias mechanism."
    },
    {
      "segment_id": "seg_018",
      "speaker": "Participant",
      "segment_type": "alternative_explanation_assessment",
      "raw_interview_anchor": "There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "ex_01"
      ],
      "ground_truth_rationale": "The participant explicitly declines a test of the alternative because the existing GreyFalcon story seems to explain the evidence; this is the narrowest full expression of ex_01."
    },
    {
      "segment_id": "seg_019",
      "speaker": "Participant",
      "segment_type": "IOC_order_effect_assessment",
      "raw_interview_anchor": "Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "oe_01"
      ],
      "ground_truth_rationale": "The participant explicitly underweights later, more diagnostic hashes because of their list position and says reversing order would change the anchor. This is the best localization for obs_003."
    },
    {
      "segment_id": "seg_020",
      "speaker": "Participant",
      "segment_type": "business_constraint_scope_rationale",
      "raw_interview_anchor": "There was, briefly — business owners wanted it narrow anyway to avoid downtime on trading-adjacent systems, so narrow scope aligned with what they wanted too. That made it easier to just go with the scope that already made sense to me.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The participant cites a legitimate business constraint that independently supports a narrow scope; it does not add a distinct planned bias instance."
    },
    {
      "segment_id": "seg_021",
      "speaker": "Participant",
      "segment_type": "source_credibility_weighting",
      "raw_interview_anchor": "But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — \"possibly,\" \"unclear if,\" that kind of thing. The vendor version gave me something concrete to act on.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "fl_01"
      ],
      "ground_truth_rationale": "Presentation and confident tone substitute for a comparison of underlying evidence, directly manifesting the hidden fluency instance."
    },
    {
      "segment_id": "seg_022",
      "speaker": "Participant",
      "segment_type": "source_comparison_rationale",
      "raw_interview_anchor": "Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "fl_01"
      ],
      "ground_truth_rationale": "The participant confirms that the subjective solidity of the bulletin drove the choice without an evidence comparison; this repeats the same planned fluency instance."
    },
    {
      "segment_id": "seg_023",
      "speaker": "Participant",
      "segment_type": "confidence_and_validation_judgment",
      "raw_interview_anchor": "Reasonably confident, maybe seven out of ten. Enough uncertainty that I flagged it as needing follow-up validation next shift, but I felt the containment steps were defensible given what I had.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "The participant calibrates confidence and requests later validation; this does not itself manifest one of the hidden instances."
    },
    {
      "segment_id": "seg_024",
      "speaker": "Participant",
      "segment_type": "retrospective_counterfactual",
      "raw_interview_anchor": "I might have caught the odd outbound connection sooner, maybe before the vendor window closed, which could've changed how much I leaned on that bulletin later. Hard to say for certain.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "This is a hindsight prediction about an alternative timeline, not a new bias manifestation."
    },
    {
      "segment_id": "seg_025",
      "speaker": "Participant",
      "segment_type": "counterfactual_order_assessment",
      "raw_interview_anchor": "Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": true,
      "ground_truth_instance_ids": [
        "oe_01"
      ],
      "ground_truth_rationale": "The explicit reverse-order counterfactual confirms the positional mechanism for the single planned order-effects instance."
    },
    {
      "segment_id": "seg_026",
      "speaker": "Participant",
      "segment_type": "retrospective_review_judgment",
      "raw_interview_anchor": "Probably the attribution step. That's where I moved fastest from one piece of strong evidence to a full working theory, and a second set of eyes might have pushed back on the infrastructure mismatch or the HR access pattern before I built the rest of the shift around it.",
      "eligible_reasoning_segment": true,
      "ground_truth_bias_present": false,
      "ground_truth_instance_ids": [],
      "ground_truth_rationale": "This is hindsight recognition of a point that could use review. Per the rubric it does not create or extend a hidden bias occurrence."
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
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the interview for affirmative transcript evidence of bias-specific cognitive mechanisms affecting reasoning or decisions. Retrospective self-reports were used only where they demonstrated a mechanism operating at the time of the described decisions."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "Authority bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring and adjustment",
        "Insufficient adjustment",
        "Automation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information and to adjust insufficiently away from that anchor when new or contradictory information is available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial Low-severity alert triage",
      "decision_point_description": "Deciding whether to immediately pull raw logs or defer manual inspection and continue with the queue.",
      "affected_reasoning_operation": "Triage prioritization and alert interpretation",
      "bias_specific_mechanism": "The automated Low severity score and two prior false-positive episodes anchored the participant's initial judgment that the alert was probably another false positive; when an unfamiliar parent process appeared in the alert summary, the participant did not sufficiently adjust away from the Low anchor and therefore did not inspect it.",
      "manifestation_in_interview": "The participant stated that the Low score 'kind of did the deciding' and that an unfamiliar parent process did not receive closer inspection because the Low label was 'sitting on top of it.'",
      "effect_on_reasoning_or_decision": "The participant deferred manual log review and moved to other queue items, delaying discovery of the outbound connection by approximately forty minutes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It was maybe two hours into an overnight shift. EDR kicked out a cluster of alerts on a trading-support server — not the trading engine itself, but a box that feeds reporting data to it. The auto-triage score came back Low. Historically, that queue throws a lot of low-severity noise, especially from that server, so my first instinct was it's probably another false positive. I'd seen that exact pattern twice in prior shifts and both times it was nothing.",
          "evidence_explanation": "Shows the initial Low score and prior false-positive history supplied the anchor for interpreting the alert as routine."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "So right after the Low score, I moved on to other queue items rather than pulling the raw logs myself — that would've taken fifteen, twenty minutes I didn't think I had yet.",
          "evidence_explanation": "Demonstrates that the anchor affected the immediate triage action: deferral of manual inspection."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back at the alert summary, there was actually an unfamiliar parent process listed next to the trading-support role tag, but with the Low label sitting on top of it, that detail didn't feel like it needed a closer look right then — the score kind of did the deciding for me.",
          "evidence_explanation": "Directly states that the Low score inhibited adjustment to a potentially contradictory cue, which is the anchoring-and-adjustment mechanism."
        }
      ],
      "correction_or_counterevidence": "At the time, the participant framed the deferral as a reasonable use of triage priority, time constraints, and prior base rates; in hindsight he said he probably could have spent the fifteen minutes, but no contemporaneous correction occurred.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Rastogi et al. (2022) describes anchoring-and-adjustment in AI-assisted decisions, including insufficient adjustment away from an initial AI-provided value.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports the anchoring-and-adjustment heuristic and insufficient adjustment away from an initial automated prediction.",
          "relevance_to_this_occurrence": "The participant encountered an automated triage score and showed insufficient adjustment from that initial Low anchor, paralleling the source's finding that anchoring on automated predictions can persist under time constraints."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Hypothesis confirmation",
        "Selective information processing",
        "Tunnel vision"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in a way that confirms or supports one's existing beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "GreyFalcon attribution",
      "decision_point_description": "Assigning the observed activity to GreyFalcon and deciding whether to revise that attribution when encountering infrastructure and target mismatches.",
      "affected_reasoning_operation": "Hypothesis generation, evidence integration, and attribution",
      "bias_specific_mechanism": "After the registry-key artifact activated the GreyFalcon hypothesis, the participant interpreted subsequent ambiguous or mismatching cues as consistent with GreyFalcon and did not test alternative explanations such as commodity malware or non-GreyFalcon actors.",
      "manifestation_in_interview": "The participant noted a registrar/domain age mismatch and an unusual HR database access attempt but continued attribution; he described the GreyFalcon story as accounting for everything and therefore did not run a simple comparative check.",
      "effect_on_reasoning_or_decision": "Reinforced attribution to GreyFalcon and reduced search for disconfirming evidence, affecting subsequent hunt scoping and containment recommendations.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The registry-key match was the strongest single piece of evidence I had. I'd seen that exact artifact before, in a campaign I'd tracked myself, so it registered immediately as meaningful. That, plus the fact that we were already dealing with something that escalated from Low to active, made GreyFalcon feel like the right frame to work in.",
          "evidence_explanation": "Shows initial hypothesis activation and the subjective strength given to the matching artifact."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It did stand out — different registrar, different age profile than what they've used before. I noted it, but the registry-key artifact felt like the stronger signal, so I didn't go back and dig into whether the infrastructure mismatch should've pulled the confidence down. I was fairly set on the attribution track by then.",
          "evidence_explanation": "Demonstrates disregarding disconfirming infrastructure evidence due to the strength of the initial confirmatory cue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My thinking was that if I were an operator inside that environment trying to get maximum value fast, HR data — personal info, banking details for payroll — is actually a pretty efficient thing to grab if the primary target is locked down or harder to reach quickly. So it didn't strike me as inconsistent with the group, more like an opportunistic pivot they'd make if they were being efficient about it.",
          "evidence_explanation": "Shows reinterpretation of an unusual target-access pattern as consistent with the GreyFalcon hypothesis rather than as disconfirming evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really in depth, no. It fit well enough with a plausible motive that I didn't stop and treat it as a reason to question the attribution itself.",
          "evidence_explanation": "Direct admission that the mismatching HR access pattern was not weighed as a reason to question the attribution."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "There was a simple check I could've run — pulling comparable hosts to see whether that same signature showed up without the registry-key artifact alongside it, which would've pointed more toward a misconfigured admin tool or commodity malware reusing that protocol instead of GreyFalcon specifically. It crossed my mind, but the GreyFalcon story already accounted for everything I was seeing well enough that running it didn't feel necessary.",
          "evidence_explanation": "Shows a disconfirming check was available but omitted because the existing GreyFalcon narrative already felt sufficient."
        }
      ],
      "correction_or_counterevidence": "The participant later identified the attribution step as the point where a second analyst's independent read would have helped, and acknowledged moving rapidly from one piece of strong evidence to a full working theory; however, no contemporaneous correction occurred.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Cook and Smallman (2008) documents confirmation bias in intelligence-analysis evidence selection and prioritization.",
      "corpus_evidence": [
        {
          "source_identifier": "cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf",
          "paper_title": "Human factors of the confirmation bias in intelligence analysis: decision support from graphical evidence",
          "authors": "Cook and Smallman",
          "publication_year": "2008",
          "retrieved_passage_or_finding": "Results revealed no bias at assessment but a strong and pervasive confirmation bias for selecting and prioritizing evidence.",
          "mechanism_supported_by_source": "The source supports the presence of confirmation bias in selecting and prioritizing evidence in intelligence analysis.",
          "relevance_to_this_occurrence": "The participant selected and prioritized the registry-key match as strongly confirmatory while underweighting inconsistent infrastructure and target-access evidence, consistent with the source's confirmation-bias finding."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Order effect",
        "Primacy effect",
        "Serial-position effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information and to adjust insufficiently away from that anchor when subsequent information is available.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Hunt scope construction from vendor bulletin",
      "decision_point_description": "Deciding which IOCs to prioritize when building a hunt scope from a five-item vendor bulletin.",
      "affected_reasoning_operation": "Hunt scope selection and evidence weighting",
      "bias_specific_mechanism": "The first IOC in the bulletin, a rare C2 protocol signature, served as an anchor; later IOCs, including two file-hash IOCs that may have been more specific or lower false-positive risk, were underweighted because the initial anchor had already structured the scope.",
      "manifestation_in_interview": "The participant built the hunt scope mostly around the first-listed IOC and admitted the file-hash IOCs factored less because they came at the bottom; he said reversing the order would likely have changed the anchor and the scope.",
      "effect_on_reasoning_or_decision": "Produced a narrower hunt scope centered on the first IOC, reducing consideration of alternative causes and potentially affecting resource allocation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "It listed five IOCs, led with a rare C2 protocol signature, and I built my hunt scope mostly around that.",
          "evidence_explanation": "Shows the first-listed IOC was used as the primary basis for the hunt scope."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The bulletin had five IOCs. The first one was this fairly rare C2 protocol signature, which lined up well with what I already believed was happening. I scoped the hunt around systems that showed signs of that signature and the broader GreyFalcon pattern I'd already built up. It felt coherent — the pieces were fitting into one picture, so that's where I put the hunt resources.",
          "evidence_explanation": "Demonstrates that the first IOC and its coherence with the existing belief structured the hunt resource allocation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, less. They were more specific technically, lower false-positive risk probably, but they came at the bottom of the list and by the time I got to them I'd already built out the scope around the first item and the story I had going. If they'd been listed first, I might have started the scoping from a different anchor entirely.",
          "evidence_explanation": "Explicitly attributes underweighting to the serial position of the file-hash IOCs and acknowledges the influence of the initial anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yes. I think I would've anchored on those instead and maybe ended up with a different, possibly broader, scope.",
          "evidence_explanation": "Directly supports the anchoring mechanism by indicating that different initial information would likely have produced a different scope."
        }
      ],
      "correction_or_counterevidence": "The participant briefly considered scoping across all five IOCs, but business owners' preference for a narrow scope aligned with the already anchored scope; the later acknowledgment that reversed IOC order would likely change the scope is retrospective rather than a contemporaneous correction.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved support from Rastogi et al. (2022) describes anchoring-and-adjustment in decision tasks involving AI-generated information.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "This strengthens the argument that the anchoringandadjustment heuristic is a resourcerational tradeo between time and accuracy (Lieder et al., 2018).",
          "mechanism_supported_by_source": "The source supports the anchoring-and-adjustment heuristic and insufficient adjustment away from an initial anchor.",
          "relevance_to_this_occurrence": "The participant anchored on the first IOC in the vendor bulletin and insufficiently adjusted the scope based on later, potentially higher-value IOCs, consistent with the anchoring-and-adjustment mechanism described in the source."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Authority bias",
      "alternative_labels": [
        "Source credibility bias",
        "Authority heuristic",
        "Presentation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to attribute greater accuracy or credibility to information based on the perceived authority, confidence, or formatting of its source rather than on the quality of the underlying evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment recommendation source selection",
      "decision_point_description": "Choosing whether to base the containment recommendation primarily on the vendor bulletin or on a colleague's notes.",
      "affected_reasoning_operation": "Source reliability assessment and recommendation formulation",
      "bias_specific_mechanism": "The participant inferred evidentiary solidity from the vendor bulletin's clean formatting and confident language while discounting the more hedged colleague's notes, without directly comparing the underlying evidence or reliability of each source.",
      "manifestation_in_interview": "The participant said the vendor bulletin 'just read as more authoritative' because it was clean, formatted well, and confident; he also stated he did not compare the evidence underlying the two sources side by side.",
      "effect_on_reasoning_or_decision": "The containment recommendation was based primarily on the vendor bulletin, reducing the influence of potentially accurate but hedged analyst notes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Near the end of shift, I had to write up a containment recommendation for the IR lead, and I leaned on that vendor bulletin pretty heavily since it was clean and specific compared to a colleague's notes, which were full of 'possibly' and 'unclear.'",
          "evidence_explanation": "Shows that the participant favored the vendor source partly because of its apparent clarity and specificity relative to the hedged notes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But honestly, the vendor bulletin just read as more authoritative. It was clean, formatted well, confident in its language. My colleague's notes were accurate as far as I could tell, but they were full of hedges — 'possibly,' 'unclear if,' that kind of thing. The vendor version gave me something concrete to act on.",
          "evidence_explanation": "Explicitly identifies source authority as inferred from presentation and confident language rather than from an evidence comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not directly side by side, no. I read the vendor one, it felt solid, and I went with it.",
          "evidence_explanation": "Confirms the participant did not compare the actual underlying evidence before selecting the source."
        }
      ],
      "correction_or_counterevidence": "The participant flagged the final recommendation for follow-up validation next shift and retained some uncertainty, but this occurred after the source-selection decision and did not reduce the influence of source presentation at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for authority bias. This widely established label is used from general cognitive-science knowledge, not from retrieval.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support is sparse and does not include all identified bias labels; authority bias is assigned from general cognitive-science knowledge rather than retrieval.",
    "The interview is a retrospective self-report, so the analysis captures reported reasoning rather than objectively observed behavior.",
    "The retrieved passages contain OCR noise and incomplete formatting, limiting the precision of quotations from scientific sources."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IA_Biased_6_Sonnet_on",
  "interview_id": "IA_Biased_6",
  "system_prompt_id": "Sonnet",
  "system_prompt_generator": "Prompt 1_2",
  "rag_model_id": "v1.0.0",
  "corpus_condition": "on",
  "retrieval_configuration_id": "k=50",
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
