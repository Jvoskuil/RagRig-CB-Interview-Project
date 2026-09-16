You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a debrief on the finance-server incident from a few weeks back, it's being recorded for internal process review, and you're free to skip anything you're not comfortable detailing. Sound okay?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start with your role that night and what you were responsible for?

Participant: I'm the on-call DFIR analyst, so I was solo overnight — it was a Sunday going into quarter-end close, which matters because that file server is basically untouchable without a director sign-off during that window. My senior lead was reachable on chat but not really available to jump on calls. So triage, scoping, containment, remediation — all of it was on me until morning.

Interviewer: Walk me through what happened.

Participant: Around 1 a.m. I got a SIEM alert for an off-hours process spawning a staging directory on the finance file server. Honestly, my first reaction was "here we go again" — I'd closed six tickets in the past three weeks that all started exactly like this, staging directory, off-hours process, and every one of those turned out to be ransomware-precursor activity. So the pattern was extremely familiar. There was also a quieter log line underneath it — a single authenticated session copying files in small batches out to an external cloud storage endpoint over a few hours. But no ransom note, no encryption, no mass renaming, so nothing screaming "this is it" yet.

Interviewer: How did you weigh those two signals?

Participant: I opened the ticket under the ransomware-precursor category. That staging-directory behavior is just what I've been seeing constantly lately, so it felt like the obvious bucket. The batch-copy line registered, but it felt secondary — slower, quieter, didn't match the urgency of what I'd been dealing with recently. In hindsight, when I actually looked at what was in those batches later, they were finance close spreadsheets, not the file types those recent ransomware precursors usually go after. And the external endpoint had no ransomware C2 history in threat intel. But at 1 a.m. I went with the category that matched what I'd just spent three weeks fighting.

Interviewer: Let's reconstruct the rest of the timeline. What came next?

Participant: Within the first ten minutes I set the ticket scope at 3 endpoints, based on the initial SIEM correlation window. About 40 minutes later, an EDR sweep came back showing authentication artifacts touching 9 more hosts — lower confidence, but there. Around then, the finance director started pinging for an update ahead of the 6 a.m. close deadline, so there was real pressure to say something concrete. I decided the 9-host signal was probably noise from that same original window and kept the scope close to 3. A later, fuller sweep ended up confirming lateral movement had actually touched 7 of those 9 hosts.

Interviewer: What made you treat that second signal as noise rather than expansion?

Participant: Partly the confidence rating on it, it wasn't a clean hit. But I'll be honest, I'd already told the director "3 hosts, contained," and adjusting that number upward with only 40 minutes of new low-confidence data felt like it'd cause more panic than it was worth before I had something firmer. So I stuck close to the original number and figured I'd revisit if something else lit up.

Interviewer: Move on to containment. What did you actually do?

Participant: I ran my own PowerShell isolation and log-collection script — I wrote that thing two years ago, and it's worked well on plenty of past incidents. My lead pinged me suggesting I use the EDR platform's one-click network isolation feature instead, said it'd be faster and less error-prone, especially now that we were looking at more hosts. That feature's only been live about three months and I've used it maybe twice.

Interviewer: What went into sticking with your script over that suggestion?

Participant: I know exactly how my script behaves, what it logs, where it's failed before and how I fixed that. The EDR feature, I just don't have the same feel for it yet. My lead's point about the host count was fair, and I didn't really have anything showing my script would hold up better at that scale — I just wanted to give it the benefit of the doubt because it's mine, I built it, I've kept it running this long, and it felt like it deserved the first shot before I'd fall back on the platform's version. So I kept running my script across the hosts, and only tried the EDR isolation on a couple of them after my lead brought it up a second time. In the end, isolating everything with my script took a good 90 minutes longer than the EDR route probably would have at that host count. It wasn't built for a scope that size, honestly, it's more of a one-or-two-host tool.

Interviewer: Did the delay change your view of which tool to use for the rest of containment?

Participant: Not really in the moment — I was mid-process and switching tools halfway through felt like it'd create more inconsistency in the logs than just finishing what I started.

Interviewer: Let's talk remediation. What options were in front of you?

Participant: The ticketing system's playbook for that category gave me exactly two actions: reset affected credentials, and reimage the affected endpoints. Neither one said anything about preserving a forensic image of the staging directory first, or checking whether that external cloud endpoint triggered any legal notification requirement.

Interviewer: Did you consider anything outside those two?

Participant: There's an escalation path to our external IR retainer that could've given a broader set of options, but it's not built into the playbook flow, you have to go looking for it separately. I didn't go down that road. I just worked through the two actions on the screen since that's what the category pointed me to.

Interviewer: Was there a point where that choice got revisited?

Participant: Two days later, compliance asked whether we'd preserved a forensic image of the staging directory before reimaging, since that affects whether this gets reported as a data exposure. That's when it became clear the playbook's two options hadn't covered that angle at all.

Interviewer: Looking back, if the staging-directory pattern hadn't been so common in your recent caseload, do you think you'd have categorized this the same way?

Participant: Probably not as quickly. If I hadn't just closed six of those tickets, I think the batch-copy line would've stood out more on its own merits instead of getting overshadowed.

Interviewer: If the EDR isolation feature had been the tool you knew best instead of your script, would containment have gone differently?

Participant: Almost certainly faster. I think I'd have reached for it first instead of treating it as the backup option.

Interviewer: And if the playbook screen had shown four remediation options instead of two?

Participant: Hard to say for sure, but I'd like to think the forensic-preservation piece would've been visible instead of something I only heard about after compliance asked.

Interviewer: Last question — what's one point where more time or information would have changed your approach?

Participant: Probably right after that second EDR sweep. If I'd had another 20 minutes before the director needed an answer, I think I'd have pushed the scope number instead of holding it, and maybe things downstream would've looked a bit different.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Biased_4",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Incident Responder (Digital Forensics and Incident Response)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Quarterly-End Exfiltration Ambiguity",
    "scenario_summary_internal": "A DFIR analyst at a mid-size financial services firm is paged for an anomaly on a finance-department file server during a high-pressure quarter-end close. The analyst must (1) triage/categorize the anomaly, (2) scope the affected environment, (3) choose a containment approach, and (4) select a remediation/eradication path. Ambiguous log signatures could indicate either commodity ransomware staging or a slower, quieter insider-assisted data exfiltration. The narrative allows realistic space for four decision points where prior experience, initial estimates, personal tooling attachment, and a narrow set of presented options can plausibly (but not necessarily) shape judgment, without the outcome mechanically proving bias.",
    "occupational_realism": {
      "objective": "Correctly identify the nature and scope of a suspicious file-server event, contain it without disrupting quarter-end financial close, and remediate root cause while preserving forensic integrity.",
      "setting": "Mid-size financial services company, on-call DFIR analyst working a Sunday night page during quarter-end close, hybrid on-prem file server plus cloud SIEM/EDR stack, limited overnight staffing.",
      "constraints": [
        "Quarter-end close means the finance file server cannot be taken fully offline without executive escalation",
        "Analyst is working solo overnight with a senior colleague reachable only by chat, not immediately available",
        "SIEM retention only covers 14 days of full packet logs",
        "Company has an EDR platform with an isolation feature rolled out three months ago that the analyst has used only twice",
        "Vendor-supplied IR playbook in the ticketing system lists a fixed set of remediation actions per alert category"
      ],
      "stakeholders": [
        "On-call DFIR analyst (interviewee)",
        "Senior DFIR lead (remote, chat-only)",
        "Finance department director (concerned about close deadline)",
        "IT operations on-call engineer",
        "External incident-response retainer vendor"
      ],
      "technical_terms_to_use": [
        "SIEM alert",
        "EDR isolation",
        "lateral movement",
        "staging directory",
        "exfiltration beacon",
        "volume shadow copy",
        "playbook category",
        "indicators of compromise (IOCs)",
        "chain of custody"
      ],
      "technical_terms_to_avoid": [
        "availability heuristic",
        "anchoring",
        "endowment effect",
        "limited alternatives bias",
        "cognitive bias",
        "heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "SIEM alert fires for unusual off-hours process spawning a staging directory on the finance file server",
          "Analyst has closed six ransomware-precursor tickets in the past three weeks, all following a similar staging-directory pattern",
          "A separate, less prominent log line shows a single authenticated session copying files in small batches to an external cloud storage endpoint over several hours",
          "No ransom note, encryption activity, or mass file-renaming has occurred yet"
        ],
        "new_information_after_decision": [
          "Follow-up review shows the copied files were finance close-related spreadsheets, not the file types typically targeted by the recent ransomware precursors",
          "The external cloud endpoint has no prior history of ransomware C2 use in threat intel feeds"
        ],
        "alternatives": [
          "Categorize as ransomware-precursor staging (matches recent frequent pattern)",
          "Categorize as low-and-slow data exfiltration (matches the batch-copy behavior)",
          "Categorize as indeterminate pending further log correlation before committing to a playbook"
        ],
        "intended_action": "Analyst labels the event as ransomware-precursor staging and opens the ticket under that category, citing how often that pattern has appeared recently."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Initial ticket scope, set within the first ten minutes, lists 3 affected endpoints based on the first SIEM correlation window",
          "EDR sweep run 40 minutes later shows authentication artifacts touching 9 additional hosts, though with lower-confidence indicators",
          "Time pressure: finance director is asking for an update before the 6 AM close deadline"
        ],
        "new_information_after_decision": [
          "A later, more complete EDR sweep confirms lateral movement touched 7 of the 9 additional hosts, not just the original 3"
        ],
        "alternatives": [
          "Keep scope at 3 endpoints, revisit only if new alerts fire",
          "Expand scope moderately to account for the 9 flagged hosts pending confirmation",
          "Treat scope as fully open and re-run a clean-slate host discovery before any containment"
        ],
        "intended_action": "Analyst keeps the scope close to the original 3-endpoint estimate, treating the 9-host signal as probably noise from the same original window rather than materially updating the case scope."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Analyst personally wrote a PowerShell-based isolation and log-collection script two years ago and has used it successfully on past incidents",
          "The company's EDR platform has a one-click network isolation feature, rolled out three months ago, that the senior lead recommends by chat as faster and less error-prone",
          "The custom script requires manual execution on each host and is not built to handle the newly expanded host count efficiently"
        ],
        "new_information_after_decision": [
          "The chosen containment method takes noticeably longer to isolate all affected hosts than the alternative would have, delaying full containment by roughly 90 minutes"
        ],
        "alternatives": [
          "Continue using the personally-built PowerShell isolation script across all affected hosts",
          "Switch to the EDR platform's built-in one-click isolation feature",
          "Use a hybrid approach, isolating the most critical hosts first with either tool"
        ],
        "intended_action": "Analyst continues relying primarily on the personally-built script, citing familiarity and past success with it, and only reluctantly tries the EDR isolation feature on a couple of hosts after the lead repeats the suggestion."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The ticketing system's playbook for the assigned category presents exactly two listed remediation actions: reset affected credentials, and reimage affected endpoints",
          "Neither listed action explicitly addresses preserving a forensic image of the staging directory or validating whether the external cloud endpoint requires legal/compliance notification",
          "The external IR retainer vendor, if consulted, could suggest additional remediation paths, but reaching them requires an extra escalation step not built into the playbook workflow"
        ],
        "new_information_after_decision": [
          "Two days later, compliance asks whether a forensic image of the staging directory was preserved before reimaging, which affects whether the incident must be reported as a data exposure"
        ],
        "alternatives": [
          "Follow the two playbook-listed actions (reset credentials, reimage) as presented",
          "Pause to escalate to the external retainer vendor for a broader review of remediation options before acting",
          "Independently research whether forensic preservation should precede reimaging, beyond what the playbook lists"
        ],
        "intended_action": "Analyst proceeds directly with the two remediation actions listed in the playbook screen, without escalating to the retainer vendor or independently researching whether other remediation paths (such as forensic preservation before reimaging) should be considered."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what happened the night this incident came in.",
        "What was your role and what were you responsible for deciding?"
      ],
      "timeline_reconstruction": [
        "What was the very first piece of information you saw, and what did you do with it?",
        "At what point did the scope of the incident change, and how did you learn that?",
        "What tools or methods did you use at each stage, and why those?"
      ],
      "decision_point_probes": [
        "What categories did you consider for this alert, and what made you settle on the one you chose?",
        "How did you arrive at the initial scope estimate, and what did you do when new host data came in?",
        "What made you choose the containment method you used over the alternative available to you?",
        "How did you decide which remediation steps to take, and where did that list of options come from?"
      ],
      "closing_hypotheticals": [
        "If the staging-directory pattern hadn't been so common in your recent caseload, do you think you'd have categorized this differently?",
        "If the EDR isolation feature had been the tool you were most experienced with instead of your script, would containment have gone differently?",
        "If the playbook screen had shown four remediation options instead of two, do you think you'd have chosen differently?",
        "Looking back, what's one point where more time or information would have changed your approach?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Availability Frequency",
        "decision_point": 1,
        "mechanism": "Ease of recalling a frequently-seen recent category (ransomware-precursor staging) causes the analyst to select that category over the data-exfiltration category, even though the batch-copy evidence is a better fit for exfiltration.",
        "affected_reasoning_operation": "Categorization/classification of the anomaly under a playbook category",
        "evidence_available_at_time": [
          "Staging-directory pattern matching six recent ransomware-precursor tickets",
          "A separate batch-copy-to-external-endpoint log line",
          "Absence of encryption or ransom-note activity"
        ],
        "required_textual_manifestation": "Analyst explicitly justifies the ransomware-precursor categorization by referencing how often that pattern has come up recently, while giving comparatively little weight to the batch-copy evidence, without a stated technical reason why staging is more likely than exfiltration here.",
        "plausible_nonbias_interpretation": "The staging-directory signature could be a genuinely stronger technical indicator of ransomware precursors in this environment, independent of recall frequency.",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "frequency of recall", "cognitive bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Adjustment and anchoring",
        "decision_point": 2,
        "mechanism": "The analyst anchors on the initial 3-endpoint scope set early in the investigation and insufficiently adjusts that estimate despite new EDR evidence suggesting a substantially larger affected host count.",
        "affected_reasoning_operation": "Scope estimation and revision under new evidence",
        "evidence_available_at_time": [
          "Original 3-endpoint scope from the first correlation window",
          "EDR sweep showing 9 additional hosts with lower-confidence indicators",
          "Time pressure from the finance close deadline"
        ],
        "required_textual_manifestation": "Analyst describes treating the 9-host signal as probably noise from the same original window and keeps the scope near the original 3, rather than substantively revising the estimate to reflect the new data.",
        "plausible_nonbias_interpretation": "The 9-host indicators were genuinely lower-confidence and reasonably deprioritized pending confirmation, which is a defensible triage judgment under time pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "insufficient adjustment"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "decision_point": 3,
        "mechanism": "The analyst overvalues their own previously-built containment script relative to the platform's newer isolation feature, continuing to rely on it primarily because it is theirs, despite a colleague's suggestion and its slower performance at the newly expanded scale.",
        "affected_reasoning_operation": "Tool/method selection for containment",
        "evidence_available_at_time": [
          "Personally-built PowerShell isolation script with past successful use",
          "EDR one-click isolation feature recommended by the senior lead",
          "Expanded host count making manual per-host execution slower"
        ],
        "required_textual_manifestation": "Analyst expresses attachment to the self-built script's familiarity and past success as the main reason for continuing to use it, and only tries the alternative reluctantly after repeated suggestion, rather than switching based on a stated efficiency comparison.",
        "plausible_nonbias_interpretation": "Sticking with a well-understood, previously validated tool under time pressure is a reasonable risk-averse choice, especially if the analyst is uncertain about the newer feature's reliability.",
        "strength": "subtle",
        "do_not_make_explicit": ["endowment effect", "ownership bias", "overvaluing own tool"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Exposure to limited alternatives",
        "decision_point": 4,
        "mechanism": "The analyst's remediation decision is shaped entirely by the two options the ticketing system's playbook screen happens to display, without seeking out or considering additional remediation paths (such as forensic preservation or vendor escalation) that were not presented on that screen.",
        "affected_reasoning_operation": "Generation and selection of remediation alternatives",
        "evidence_available_at_time": [
          "Playbook screen listing exactly two remediation actions",
          "Availability of an escalation path to the external IR retainer vendor",
          "No explicit playbook option addressing forensic preservation before reimaging"
        ],
        "required_textual_manifestation": "Analyst describes proceeding with the two listed playbook actions as essentially the full option set considered, without describing any independent search for, or consideration of, alternatives beyond what the screen presented.",
        "plausible_nonbias_interpretation": "Following a standardized, vendor-approved playbook under time pressure is a normal and often required operational practice, not necessarily a sign of restricted option-generation.",
        "strength": "subtle",
        "do_not_make_explicit": ["limited alternatives", "restricted option set", "narrow framing"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this is the biased-condition scenario with no paired control generated in this specification."
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
      "Exactly four decision points, one per manifest bias, each with at least two plausible alternatives",
      "Each occurrence assigned to a distinct decision point to maximize independence and narrative realism",
      "No bias labels, definitions, or explanations appear in the technical_terms_to_use list or intended for the public interview text",
      "Each occurrence has a plausible non-bias interpretation to avoid mechanically proving bias from outcome alone",
      "Target word count of 1,350 (range 1,215-1,485) is achievable given four decision points with opening, timeline, decision-point, and closing-hypothetical probes without repetitive exposition",
      "No unrequested bias (e.g., confirmation bias, sunk cost, overconfidence) is intentionally embedded anywhere in the timeline or probes"
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Availability Frequency",
        "occurrences": 1,
        "mechanism_constraint": "ease of recall of one category over that of another leading to the selection of that category even if the other category is a better fit."
      },
      {
        "bias": "Adjustment and anchoring",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Endowment",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Exposure to limited alternatives",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Availability Frequency",
      "Adjustment and anchoring",
      "Endowment",
      "Exposure to limited alternatives"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Availability Frequency", "requested_occurrences": 1 },
      { "bias": "Adjustment and anchoring", "requested_occurrences": 1 },
      { "bias": "Endowment", "requested_occurrences": 1 },
      { "bias": "Exposure to limited alternatives", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Availability Frequency" },
      { "instance_id": "cb_02", "bias": "Adjustment and anchoring" },
      { "instance_id": "cb_03", "bias": "Endowment" },
      { "instance_id": "cb_04", "bias": "Exposure to limited alternatives" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Availability Frequency", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Adjustment and anchoring", "decision_point": 2 },
      { "instance_id": "cb_03", "bias": "Endowment", "decision_point": 3 },
      { "instance_id": "cb_04", "bias": "Exposure to limited alternatives", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Availability Frequency",
        "mechanism": "Ease of recall of the frequently-seen ransomware-precursor category leads to its selection over the better-fitting data-exfiltration category.",
        "affected_reasoning_operation": "Categorization of the anomaly under a playbook category",
        "evidence_source": "Log pattern comparison: staging-directory frequency vs. batch-copy exfiltration signal",
        "distinctiveness_requirement": "Must be tied specifically to categorization at DP1 based on recall frequency of a category, not to scoping, tool choice, or remediation option selection."
      },
      {
        "instance_id": "cb_02",
        "bias": "Adjustment and anchoring",
        "mechanism": "Initial 3-endpoint scope estimate anchors subsequent scope judgment, causing insufficient adjustment despite new evidence of 9 additional hosts.",
        "affected_reasoning_operation": "Scope revision under new EDR evidence",
        "evidence_source": "Comparison of initial correlation-window scope vs. later EDR sweep results",
        "distinctiveness_requirement": "Must be tied specifically to numeric/scope-estimate revision at DP2, distinct from the categorical judgment in DP1 or tool/option choices in DP3-DP4."
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "mechanism": "Overvaluation of the self-built containment script relative to the platform's isolation feature, driven by ownership rather than a stated performance comparison.",
        "affected_reasoning_operation": "Containment tool/method selection",
        "evidence_source": "Comparison of self-built script usage history vs. colleague-recommended EDR feature and observed containment delay",
        "distinctiveness_requirement": "Must be tied specifically to tool ownership/attachment at DP3, distinct from category or scope judgments and from the option-set framing in DP4."
      },
      {
        "instance_id": "cb_04",
        "bias": "Exposure to limited alternatives",
        "mechanism": "Remediation decision is constrained to the two options displayed on the playbook screen, with no independent search for additional remediation paths.",
        "affected_reasoning_operation": "Generation/selection of remediation alternatives",
        "evidence_source": "Playbook screen option set vs. unexplored escalation path to retainer vendor and forensic-preservation option",
        "distinctiveness_requirement": "Must be tied specifically to the narrowness of the presented option set at DP4, distinct from the tool attachment reasoning in DP3."
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Availability Frequency", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Adjustment and anchoring", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Endowment", "strength": "subtle" },
      { "instance_id": "cb_04", "bias": "Exposure to limited alternatives", "strength": "subtle" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "CS_Biased_4",
    "domain_id": "CS",
    "total_requested_occurrences": 4,
    "total_planned_occurrences": 4,
    "allocation_rule_used": "One occurrence per named bias, each assigned to a distinct decision point (DP1-DP4) selected for mechanism fit and narrative realism; no bias shares a decision point since each has only one requested occurrence.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [],
    "generation_warnings": []
  }
}
</COMPLETE_GENERATION_SPECIFICATION>

<EVALUATION_SEGMENT_MAP>
  null
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
    "analysis_scope_note": "Evaluated the primary interview transcript for affirmatively demonstrated cognitive biases in DFIR incident triage, scoping, containment, and remediation reasoning. Retrieval context supplied direct support for anchoring and adjustment; availability and ownership/IKEA-effect classifications rely on established general cognitive-science knowledge because no direct corpus passage was available."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring and adjustment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "IKEA effect",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "recency effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which the ease or recency with which instances of a category come to mind inflates its perceived probability, frequency, or importance.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Incident categorization of initial SIEM signals",
      "decision_point_description": "Choice of ticket category and relative weighting of the staging-directory signal versus the quieter external copy/batch signal at approximately 1 a.m.",
      "affected_reasoning_operation": "Signal weighting and category assignment",
      "bias_specific_mechanism": "Recent repeated exposure to six ransomware-precursor tickets with similar staging-directory indicators made that category highly available, causing the participant to treat the quieter batch-copy/external cloud signal as secondary even though its content and threat-intel profile did not match recent ransomware precursors.",
      "manifestation_in_interview": "The participant explicitly stated that the staging-directory pattern was constantly seen lately and felt like the obvious bucket, while the batch-copy line was overshadowed by recent experience. Retrospective self-assessment confirmed that without the recent tickets the batch-copy line would likely have stood out on its own merits.",
      "effect_on_reasoning_or_decision": "The incident was categorized under the ransomware-precursor category, weighting the familiar indicator over a potentially more diagnostic exfiltration signal.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd closed six tickets in the past three weeks that all started exactly like this, staging directory, off-hours process, and every one of those turned out to be ransomware-precursor activity. So the pattern was extremely familiar.",
          "evidence_explanation": "Establishes highly available recent experience from repeated similar cases."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I opened the ticket under the ransomware-precursor category. That staging-directory behavior is just what I've been seeing constantly lately, so it felt like the obvious bucket. The batch-copy line registered, but it felt secondary — slower, quieter, didn't match the urgency of what I'd been dealing with recently.",
          "evidence_explanation": "Directly connects the recency and frequency of prior cases to the weighting of the current signals."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I hadn't just closed six of those tickets, I think the batch-copy line would've stood out more on its own merits instead of getting overshadowed.",
          "evidence_explanation": "Retrospective self-assessment confirms the availability mechanism behind the initial categorization."
        }
      ],
      "correction_or_counterevidence": "Later inspection showed the batch-copy files were finance close spreadsheets and the external endpoint lacked ransomware C2 history, suggesting the category was probably incorrect. However, this correction occurred after the categorization decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly defines availability heuristic or recency effects; classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "anchoring and adjustment",
      "alternative_labels": [
        "anchor effect",
        "anchoring heuristic",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Estimates are influenced by an initially presented or considered value, with subsequent adjustment from that anchor typically insufficient.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment scope determination after second EDR sweep",
      "decision_point_description": "Whether to expand the covered host scope from the initial 3 endpoints after lower-confidence EDR artifacts implicated 9 additional hosts.",
      "affected_reasoning_operation": "Numerical scope estimation and evidence updating",
      "bias_specific_mechanism": "The initial SIEM correlation scope of 3 endpoints served as an anchor; after a later EDR sweep showed 9 additional hosts with lower-confidence authentication artifacts, the participant adjusted insufficiently and labeled the new signal as noise, keeping scope close to 3. Announcing the anchor to the finance director and time pressure further inhibited adjustment.",
      "manifestation_in_interview": "The participant initially set scope at 3 endpoints, then kept the scope close to 3 after the later EDR sweep, even though a fuller sweep eventually confirmed lateral movement had touched 7 of the 9 additional hosts.",
      "effect_on_reasoning_or_decision": "The intrusion scope was underestimated, likely delaying recognition of lateral movement across additional hosts.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Within the first ten minutes I set the ticket scope at 3 endpoints, based on the initial SIEM correlation window. About 40 minutes later, an EDR sweep came back showing authentication artifacts touching 9 more hosts — lower confidence, but there.",
          "evidence_explanation": "Establishes the initial anchor value and the later contradictory evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I decided the 9-host signal was probably noise from that same original window and kept the scope close to 3.",
          "evidence_explanation": "Demonstrates insufficient adjustment away from the initial 3-host anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But I'll be honest, I'd already told the director '3 hosts, contained,' and adjusting that number upward with only 40 minutes of new low-confidence data felt like it'd cause more panic than it was worth before I had something firmer.",
          "evidence_explanation": "Reveals commitment to the announced anchored value, which further inhibited adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "A later, fuller sweep ended up confirming lateral movement had actually touched 7 of those 9 hosts.",
          "evidence_explanation": "Provides objective evidence that the anchored scope estimate was materially inaccurate."
        }
      ],
      "correction_or_counterevidence": "The later fuller EDR sweep confirmed 7 of the 9 hosts had lateral movement, and the participant acknowledged that with 20 more minutes he likely would have pushed the scope number upward. The initial non-adjustment may also have been influenced by time pressure and low confidence, not solely anchoring.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The supplied space-flight-systems corpus explicitly describes anchoring and adjustment and the typical insufficiency of adjustments.",
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "The anchoring and adjustment heuristic was described Tversky and Kahneman in 1974, and subsequent resear has elaborated upon it. In brief, it has been obser people make estimates based on an initial answer, a adjustments from there based on additional informat Tversky and Kahneman put it, “adjustments are typic insufficient.”",
          "mechanism_supported_by_source": "Initial values anchor estimates, and adjustments from that anchor are typically insufficient.",
          "relevance_to_this_occurrence": "Directly matches the participant's initial 3-host scope serving as an anchor and the insufficient upward adjustment after the second EDR sweep."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "IKEA effect",
      "alternative_labels": [
        "endowment effect",
        "ownership bias",
        "effort justification"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Higher valuation of self-created or self-assembled products, beyond their objective performance, due to ownership and personal investment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment tool selection",
      "decision_point_description": "Choice between the participant's custom PowerShell isolation script and the EDR platform's one-click network isolation feature.",
      "affected_reasoning_operation": "Tool evaluation and choice under competing options",
      "bias_specific_mechanism": "The participant overvalued his self-built script due to ownership and personal investment, giving it the benefit of the doubt despite lacking evidence that it would perform better at scale and despite a reasonable alternative.",
      "manifestation_in_interview": "The participant acknowledged no data showed his script would hold up better at scale and that his lead's host-count concern was fair, but selected the script first because he had built and maintained it.",
      "effect_on_reasoning_or_decision": "Selected the slower, less scalable containment tool; isolation took an estimated 90 minutes longer than the EDR route would likely have taken.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I know exactly how my script behaves, what it logs, where it's failed before and how I fixed that. The EDR feature, I just don't have the same feel for it yet.",
          "evidence_explanation": "Shows familiarity and subjective comfort with the self-created tool, but does not by itself prove ownership bias."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "My lead's point about the host count was fair, and I didn't really have anything showing my script would hold up better at that scale — I just wanted to give it the benefit of the doubt because it's mine, I built it, I've kept it running this long, and it felt like it deserved the first shot before I'd fall back on the platform's version.",
          "evidence_explanation": "Directly states ownership and self-creation as the reason for preference despite the absence of supporting performance evidence at scale."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In the end, isolating everything with my script took a good 90 minutes longer than the EDR route probably would have at that host count. It wasn't built for a scope that size, honestly, it's more of a one-or-two-host tool.",
          "evidence_explanation": "Demonstrates the material cost of the choice and that the tool was objectively mismatched to the current scope."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Almost certainly faster. I think I'd have reached for it first instead of treating it as the backup option.",
          "evidence_explanation": "Confirms that if the EDR feature had been equally familiar, the participant would likely have chosen it first."
        }
      ],
      "correction_or_counterevidence": "The participant later tried EDR isolation on a couple of hosts after the lead raised it a second time, and retrospectively acknowledged that greater familiarity with EDR would have made containment faster. Retaining the script also had a plausible log-consistency rationale once the process was underway.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus addresses IKEA effect, ownership bias, or endowment effects; classification relies on established general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "default effect",
      "alternative_labels": [
        "status quo bias",
        "narrow framing",
        "choice architecture effect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Remediation action selection from ticketing-system playbook",
      "supporting_interview_quote": "I didn't go down that road. I just worked through the two actions on the screen since that's what the category pointed me to.",
      "plausible_mechanism": "The design of the playbook presented exactly two highly salient options, making them the de facto default set and reducing the likelihood of searching for an external escalation path or self-generating forensic/legal-preservation steps.",
      "why_not_identified": "Evidence is suggestive but not definitive; following a standard category playbook may represent legitimate operational procedure or structural/tooling constraint. The transcript does not conclusively establish a cognitive distortion independent of the system design."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The supplied retrieval context contains direct support for anchoring and adjustment only; availability heuristic and IKEA/ownership-effect classifications rely on established general cognitive-science knowledge.",
    "The interview is retrospective self-report; some decisions occurred under time pressure, low-information conditions, and operational constraints that may explain portions of the behavior.",
    "The remediation playbook pattern was classed as a candidate bias rather than an identified occurrence because following a standard playbook may reflect structural/tooling constraints rather than a definitively demonstrated individual cognitive distortion."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Biased_4_Gemini_on",
  "interview_id": "CS_Biased_4",
  "system_prompt_id": "Gemini",
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
