You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for taking the time. This is for an internal case-study review, and it stays within that context. Comfortable proceeding?

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

Participant: Get fresh numbers before you anchor on the old one. Even under deadline pressure, a couple of quotes reframes the whole conversation.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "CS_Biased_7",
  "domain_id": "CS",
  "domain": "Cyber Security",
  "role": "Chief Information Security Officer (CISO)",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Anomalous Login and the Threat-Intel Renewal",
    "scenario_summary_internal": "Elena Voss, CISO of a mid-size fintech (NorthGate Financial), is midway through the annual security-vendor budget cycle when a SOC analyst flags an anomalous privileged login on a payments-adjacent host. Elena must triage the alert, decide whether to renew the incumbent threat-intel/EDR vendor or run a competitive RFP, decide how aggressively to contain the suspected intrusion given revenue-impact framing from the CFO, and finally decide how to reallocate the annual security budget after the incident is closed. The scenario is designed to surface anchoring on automated severity scores and legacy budget figures, narrow vendor consideration due to habitual sourcing, attentional narrowing onto the flagged host, overconfidence in a hastily built monitoring script, loss-framed reluctance to isolate a revenue-generating segment, and attachment to the incumbent vendor relationship.",
    "occupational_realism": {
      "objective": "Detect, triage, and contain a suspected credential-based intrusion while making a concurrent annual vendor-renewal and budget decision without disrupting payment operations.",
      "setting": "Mid-size fintech company (NorthGate Financial, ~450 employees) processing card and ACH payments; SOC operates with a 6-person team; annual security budget cycle overlaps with a live security alert.",
      "constraints": [
        "Board-mandated deadline to finalize next fiscal year's security vendor contracts within the week",
        "Payments processing segment cannot be taken fully offline without significant revenue and SLA penalty exposure",
        "SOC team is short-staffed due to one analyst on leave",
        "Existing EDR/threat-intel vendor contract auto-renews unless canceled within 5 business days",
        "Regulatory expectation (PCI DSS) to document incident response decisions and rationale"
      ],
      "stakeholders": [
        "Elena Voss, CISO (interview subject)",
        "SOC Lead Analyst",
        "CFO",
        "VP of Payments Operations",
        "Incumbent EDR/Threat-Intel Vendor Account Manager",
        "External Incident Response Retainer Firm"
      ],
      "technical_terms_to_use": [
        "SIEM", "EDR", "SOC", "lateral movement", "privileged access", "IOC", "playbook",
        "containment", "network segmentation", "MFA", "threat intelligence feed", "RFP",
        "MTTR", "SOAR", "vendor risk assessment", "credential stuffing", "tabletop exercise",
        "risk appetite", "board reporting", "CVE"
      ],
      "technical_terms_to_avoid": [
        "anchoring", "anchor", "endowment effect", "sunk cost", "illusion of control",
        "loss aversion", "loss framing", "selective attention", "inattentional blindness",
        "limited alternatives bias", "cognitive bias", "heuristic", "confirmation bias"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "SOC's SIEM auto-classified the login anomaly as 'Medium' severity based on a default risk-scoring model",
          "The flagged host is a jump server used by a payments engineer",
          "A second, lower-priority alert fired nine minutes earlier on an adjacent authentication server but was not opened",
          "SOC analyst is handling both alerts alone due to short staffing"
        ],
        "new_information_after_decision": [
          "The adjacent authentication server alert, once reviewed hours later, is found to share the same source IP range as the jump-server anomaly",
          "The automated 'Medium' score did not account for the privileged nature of the account involved"
        ],
        "alternatives": [
          "Escalate immediately to full incident response and open both alerts jointly",
          "Accept the automated 'Medium' classification and schedule standard next-business-day follow-up",
          "Request the analyst correlate all authentication alerts from the same time window before deciding severity"
        ],
        "intended_action": "Elena defers to the SIEM's default 'Medium' score and directs the SOC analyst to focus solely on the flagged jump server, without requesting a broader correlation sweep of concurrent alerts."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "The incumbent EDR/threat-intel vendor contract must be renewed or canceled within 5 business days",
          "NorthGate has used this vendor for six years and Elena's team built custom detection rules and dashboards on top of it",
          "Two peer fintech CISOs, contacted informally, mentioned they also use the same vendor or its closest competitor",
          "No formal RFP has been issued this cycle; procurement flagged that three other vendors offer comparable EDR/threat-intel bundles"
        ],
        "new_information_after_decision": [
          "A newer entrant vendor, not considered, later publishes a case study showing faster detection times for the same attack pattern involved in this incident",
          "Procurement notes the renewal was signed without a comparative bid on file"
        ],
        "alternatives": [
          "Run a short competitive RFP against at least one vendor outside the two informally referenced by peers",
          "Renew the incumbent vendor because of the custom integrations and team familiarity",
          "Request a 90-day contract extension to allow time for a proper market scan"
        ],
        "intended_action": "Elena renews the incumbent vendor, citing the effort already invested in custom dashboards and rules, and limits her comparison to the vendor and the one competitor her peers happened to mention."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Correlated logs now show lateral movement attempts from the compromised jump-server account toward the payments database segment",
          "Elena's team wrote a quick monitoring script overnight to watch for further movement from that account",
          "The CFO states that isolating the payments segment for containment will cause a guaranteed processing outage costing an estimated $180,000 in same-day transaction fees",
          "The external IR retainer firm recommends full segment isolation pending forensic review; there is no confirmed evidence yet that isolation would fully stop the threat"
        ],
        "new_information_after_decision": [
          "Two hours after the decision, the compromised account is used to access a second internal system that the monitoring script did not cover",
          "Forensics later determines the attacker had already exfiltrated a small dataset before the monitoring script was deployed"
        ],
        "alternatives": [
          "Isolate the payments segment fully as the IR retainer recommends, accepting the guaranteed short-term revenue impact",
          "Rely on the newly written monitoring script and targeted account lockout instead of full isolation",
          "Isolate only the specific subnet touched so far while keeping broader payments processing online"
        ],
        "intended_action": "Elena chooses to rely on the overnight monitoring script and a targeted account lockout rather than full segment isolation, treating the script as sufficient coverage and treating the CFO's framing of a 'guaranteed' revenue loss as decisive against isolation."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "The incident is now contained; a post-incident budget review is due to the board in three days",
          "A remediation project (privileged-access segmentation) was scoped 18 months ago with a cost estimate of $240,000, never funded",
          "Current vendor quotes for the same scope, gathered this week, range from $310,000 to $340,000 due to inflation and expanded scope",
          "The board has asked for a single recommended remediation budget figure"
        ],
        "new_information_after_decision": [
          "Procurement flags that the submitted budget figure is below every current vendor quote received this week",
          "The finance team later notes the original $240,000 estimate excluded cloud components added to the environment since it was scoped"
        ],
        "alternatives": [
          "Recommend a budget based on the current vendor quotes gathered this week",
          "Recommend the original $240,000 figure with a modest contingency",
          "Commission a fresh, narrow-scope estimate before submitting any number to the board"
        ],
        "intended_action": "Elena recommends a remediation budget close to the original 18-month-old $240,000 estimate, treating it as the reasonable baseline and only lightly adjusting it upward despite current quotes running well above that figure."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through your role and responsibilities as CISO at NorthGate Financial.",
        "Describe, in your own words, the incident you're about to walk me through and what the overall objective was."
      ],
      "timeline_reconstruction": [
        "Take me through the sequence of events from the first alert to the incident being closed, in the order they happened.",
        "At each stage, what did you know, and when did you learn it?"
      ],
      "decision_point_probes": [
        "What cues in the alert or dashboard drew your attention first, and what, if anything, competed for your attention at that moment?",
        "What information sources did you consult before making this call, and were there sources you didn't check?",
        "What alternatives did you consider at this point, and why did you rule the others out?",
        "What was the main basis for your decision here?",
        "Had you handled a similar situation before, and did that experience shape this decision?",
        "How much time pressure were you under when you made this call?",
        "How confident were you in the information you were acting on, and what was still uncertain?",
        "If you'd had an extra day or an extra analyst, would this decision have gone differently?"
      ],
      "closing_hypotheticals": [
        "If the SIEM hadn't pre-scored the alert's severity, do you think your initial response would have changed?",
        "If procurement had required a formal RFP regardless of timeline, how might the vendor decision have gone?",
        "If the CFO had not quantified the outage cost, would the containment call have been different?",
        "Looking back, what would you tell a CISO facing the same budget-review deadline with an 18-month-old cost estimate on file?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Adjustment and anchoring",
        "decision_point": 1,
        "mechanism": "Elena adopts the SIEM's automatically generated 'Medium' severity score as the reference point and makes only a minor upward adjustment in urgency, rather than independently assessing severity from the underlying evidence (privileged account, jump-server role).",
        "affected_reasoning_operation": "Initial severity/urgency estimation",
        "evidence_available_at_time": [
          "Automated 'Medium' severity score from SIEM",
          "Knowledge that the account is privileged and tied to payments infrastructure"
        ],
        "required_textual_manifestation": "Elena explicitly references the automated score as her starting point and describes adjusting her own urgency assessment only slightly from it, despite having independent reasons (privileged account) to weight it higher.",
        "plausible_nonbias_interpretation": "Trusting a validated automated triage tool could be a reasonable efficiency practice under staffing constraints.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "reference point", "bias"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Selective Attention Bias or Inattentional Blindness",
        "decision_point": 1,
        "mechanism": "Having locked onto the flagged jump server as the object of concern, Elena directs the analyst to focus exclusively there, causing the concurrent, related alert on the adjacent authentication server to go unexamined until much later.",
        "affected_reasoning_operation": "Evidence-selection / scope-setting for investigation",
        "evidence_available_at_time": [
          "A second alert on an adjacent authentication server that fired nine minutes earlier",
          "Single analyst available to review both alerts"
        ],
        "required_textual_manifestation": "Elena describes narrowing the analyst's focus to the jump server without mentioning the second alert as something she asked to be checked in parallel; the connection is only made much later.",
        "plausible_nonbias_interpretation": "With one analyst and limited time, focusing on the most concrete alert first is a defensible triage sequencing choice.",
        "strength": "moderate",
        "do_not_make_explicit": ["selective attention", "inattentional blindness", "missed", "overlooked"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Endowment",
        "decision_point": 2,
        "mechanism": "Elena overvalues the incumbent vendor relationship because of the custom dashboards and detection rules her team has already built on it, treating that built-up investment as making the incumbent inherently more valuable than a comparable alternative would be if evaluated fresh.",
        "affected_reasoning_operation": "Vendor valuation / renewal justification",
        "evidence_available_at_time": [
          "Six years of custom rules and dashboards built on the incumbent platform",
          "Three other vendors flagged by procurement as offering comparable bundles"
        ],
        "required_textual_manifestation": "Elena cites the team's built investment in the incumbent's platform as the primary reason to keep it, without separately establishing that the incumbent's current capability outperforms the alternatives on their own merits.",
        "plausible_nonbias_interpretation": "Switching costs and integration risk are legitimate factors in vendor retention decisions.",
        "strength": "subtle",
        "do_not_make_explicit": ["endowment", "sunk cost", "overvalue"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Exposure to limited alternatives",
        "decision_point": 2,
        "mechanism": "Elena restricts her comparison set to the incumbent and the single competitor mentioned informally by peer CISOs, never engaging procurement's list of three other qualified vendors, so the renewal decision is made against an artificially narrow option set.",
        "affected_reasoning_operation": "Alternative-generation for vendor decision",
        "evidence_available_at_time": [
          "Procurement's list of three vendors offering comparable bundles",
          "Informal peer mentions of one alternative vendor"
        ],
        "required_textual_manifestation": "Elena describes her comparison as being between the incumbent and 'the vendor a couple of peers use,' without describing having reviewed procurement's broader vendor list.",
        "plausible_nonbias_interpretation": "Relying on trusted peer recommendations can be an efficient, low-risk way to shortlist vendors under time pressure.",
        "strength": "subtle",
        "do_not_make_explicit": ["limited alternatives", "narrow options", "restricted search"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Illusion of control",
        "decision_point": 3,
        "mechanism": "Elena treats the overnight, hastily built monitoring script as providing reliable coverage of the compromised account's activity, expressing confidence in containment through that script despite it being untested and narrow in scope relative to the actual threat surface.",
        "affected_reasoning_operation": "Confidence assessment of a self-implemented containment measure",
        "evidence_available_at_time": [
          "A monitoring script built overnight by the team, not independently tested",
          "IR retainer firm's recommendation for full segment isolation pending forensic review"
        ],
        "required_textual_manifestation": "Elena describes feeling that the script 'had it covered' or gave her team the visibility they needed, in place of full isolation, without qualifying its actual tested scope.",
        "plausible_nonbias_interpretation": "Deploying a rapid custom monitoring measure while avoiding a costly full isolation is a legitimate proportional-response strategy under uncertainty.",
        "strength": "moderate",
        "do_not_make_explicit": ["illusion of control", "overconfidence", "false sense of coverage"]
      },
      {
        "instance_id": "cb_06",
        "bias": "Loss Framing",
        "decision_point": 3,
        "mechanism": "The CFO's presentation of the isolation option as a 'guaranteed' $180,000 loss, versus an uncertain security benefit, leads Elena to weight the certain financial loss far more heavily than the uncertain security gain, tilting her decision away from isolation.",
        "affected_reasoning_operation": "Risk-tradeoff evaluation between certain cost and uncertain benefit",
        "evidence_available_at_time": [
          "CFO's framing of isolation as a guaranteed $180,000 same-day loss",
          "IR retainer's recommendation, framed only in terms of risk reduction, not quantified certainty"
        ],
        "required_textual_manifestation": "Elena explicitly recalls the CFO's 'guaranteed loss' framing as the decisive factor tipping her away from isolation, contrasted with the less concretely stated security benefit.",
        "plausible_nonbias_interpretation": "Weighing a certain, quantified operational cost against an unquantified security benefit is a standard part of risk-based decision-making.",
        "strength": "subtle",
        "do_not_make_explicit": ["loss framing", "framing effect", "certain loss versus uncertain gain"]
      },
      {
        "instance_id": "cb_07",
        "bias": "Adjustment and anchoring",
        "decision_point": 4,
        "mechanism": "Elena starts from the 18-month-old $240,000 remediation estimate and makes only a modest upward adjustment for the board recommendation, rather than re-deriving the figure from this week's actual vendor quotes, which all exceed that adjusted figure.",
        "affected_reasoning_operation": "Budget-figure estimation for board recommendation",
        "evidence_available_at_time": [
          "18-month-old remediation cost estimate of $240,000",
          "Current vendor quotes ranging from $310,000-$340,000"
        ],
        "required_textual_manifestation": "Elena describes taking the old estimate as her starting figure and nudging it up 'a bit' for the board, rather than basing the recommendation on the range of current quotes she has in hand.",
        "plausible_nonbias_interpretation": "Using a prior internal estimate as a starting point for continuity in board reporting can be a reasonable practice absent stronger signals to deviate.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "stale estimate", "starting point"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; this generation is the primary 'biased' condition with no paired control specified in this request."
    },
    "counterfactual_specification": {
      "causal_variable": "Presence and salience of the SIEM's automated severity pre-score at the moment of initial triage (autoselected as the highest-leverage single causal lever, given its downstream role in anchoring cb_01 and its narrative connection to attention allocation in cb_02)",
      "original_state": "The SIEM displays a default automated 'Medium' severity score to Elena before she reviews underlying evidence",
      "counterfactual_state": "The SIEM displays raw event data without a pre-computed severity score, requiring Elena to derive urgency independently",
      "variables_to_hold_constant": [
        "Company profile and staffing levels",
        "Incident type and technical details (privileged jump-server compromise, lateral movement pattern)",
        "Vendor renewal deadline and budget-cycle timing",
        "CFO's revenue-impact framing at decision point 3",
        "Decision count and sequence (4 decision points, same order)",
        "Word count target and interview structure"
      ],
      "expected_causal_difference": "Without a displayed pre-score, Elena would be expected to derive severity from the privileged-account context directly, plausibly increasing early escalation and reducing the delay in correlating the second alert.",
      "causal_test_question": "Does removing the automated severity pre-score change the CISO's initial escalation urgency and the speed of alert correlation, independent of all other incident facts?"
    },
    "generation_checks": [
      "Exactly 7 total occurrence instances planned, matching the sum of the manifest (2+1+1+1+1+1=7)",
      "Adjustment and anchoring instances (cb_01, cb_07) are placed at different decision points with distinct evidence sources (automated severity score vs. legacy budget estimate)",
      "Decision points 1, 2, and 3 each host two distinct biases with different reasoning operations and evidence sources, satisfying the shared-decision-point distinctiveness rule",
      "No decision point hosts more than two instances of any single bias",
      "No bias names, definitions, or explanations appear in planned interview text; only behavioral manifestations are specified",
      "Each instance has a plausible non-bias interpretation to avoid mechanical bias-proof consequences",
      "Exactly four decision points are planned, each with at least three alternatives",
      "Probe plan covers cues, information sources, goals, alternatives, decision basis, prior experience, time pressure, uncertainty, and hypotheticals",
      "Narrative content across 4 phases is scoped to fit within 1,215-1,485 words without repetitive exposition"
    ]
  },
  "hidden_validation_specification": {
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
        "segment_type": "objective_and_constraints",
        "raw_interview_anchor": "Participant: The goal was to contain the intrusion without disrupting payments while still meeting the vendor-contract and budget deadlines.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": false,
        "ground_truth_instance_ids": [],
        "ground_truth_rationale": "Competing operational and deadline objectives are stated, but no hidden bias mechanism or biased choice is manifested in this span."
      },
      {
        "segment_id": "seg_002",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Participant: The account being privileged stood out, honestly. But the Medium score was already sitting there, and normally that's a reasonable starting point for how fast we move.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_01"
        ],
        "ground_truth_rationale": "The participant adopts the automated Medium score as the starting reference despite recognizing that the account was privileged and the score omitted privilege."
      },
      {
        "segment_id": "seg_003",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Participant: I didn't loop the second alert in as something to check in parallel — the analyst was stretched thin, and the jump server was the concrete lead.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_02"
        ],
        "ground_truth_rationale": "Attention is narrowed to the concrete jump-server lead, leaving the concurrent related authentication-server alert unexamined."
      },
      {
        "segment_id": "seg_004",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Participant: Procurement had actually flagged three other vendors with comparable bundles this cycle, but I didn't work through that list closely. My real comparison ended up being just the incumbent and its closest competitor.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_04"
        ],
        "ground_truth_rationale": "The comparison set is restricted to two familiar vendors despite procurement identifying three additional comparable options."
      },
      {
        "segment_id": "seg_005",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Participant: Those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't test whether that feeling matched their current value against procurement's options. Switching felt costly given what we'd already built.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_03"
        ],
        "ground_truth_rationale": "The incumbent is overvalued because of prior team-built customization and invested effort rather than an independent current-value comparison."
      },
      {
        "segment_id": "seg_006",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Participant: Nobody had validated whether the script would catch credential reuse on another host or a parallel session — but having eyes on that one account felt like enough to hold off on isolation.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_05"
        ],
        "ground_truth_rationale": "The participant treats an untested, narrow monitoring script as sufficient containment coverage."
      },
      {
        "segment_id": "seg_007",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Participant: The guaranteed dollar figure against an unquantified benefit made isolation feel like the more expensive option, even though I couldn't put a number on the other side.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_06"
        ],
        "ground_truth_rationale": "The certain $180,000 loss framing is weighted more heavily than the unquantified security benefit, tilting the isolation decision."
      },
      {
        "segment_id": "seg_008",
        "speaker": "Participant",
        "segment_type": "decision_reasoning",
        "raw_interview_anchor": "Participant: The old figure was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000.",
        "eligible_reasoning_segment": true,
        "ground_truth_bias_present": true,
        "ground_truth_instance_ids": [
          "cb_07"
        ],
        "ground_truth_rationale": "The stale $240,000 estimate remains the starting point despite current quotes of $310,000–$340,000."
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
    "analysis_scope_note": "Evaluated the interview transcript as the primary evidence for affirmative cognitive bias occurrences. No retrieved scientific-corpus passages were supplied, so classifications rely on established cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 2
    },
    {
      "bias_label": "certainty effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "endowment effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring effect",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information when making subsequent judgments, with insufficient adjustment from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial SIEM triage prioritization",
      "decision_point_description": "Deciding whether to treat the jump-server Medium alert as isolated and prioritize it, versus escalating or correlating it with the earlier auth-server alert.",
      "affected_reasoning_operation": "Severity assessment and triage prioritization",
      "bias_specific_mechanism": "The SIEM Medium severity score served as an initial numerical anchor. The participant recognized that the score did not incorporate the account's privileged status but did not sufficiently adjust the severity assessment or widen the investigation scope away from the anchored Medium rating.",
      "manifestation_in_interview": "The participant acknowledged that the Medium score was already present and provided a number to build the response around, despite knowing it omitted privileged-account risk; he did not escalate or correlate the earlier alert until later.",
      "effect_on_reasoning_or_decision": "The initial triage treated the jump-server alert as a manageable Medium event, delaying correlation with the auth-server alert and likely delaying recognition of lateral movement.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The account being privileged stood out, honestly. But the Medium score was already sitting there, and normally that's a reasonable starting point for how fast we move.",
          "evidence_explanation": "Shows the pre-existing Medium score anchored the initial severity impression even though a diagnostic risk factor—account privilege—was salient."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The score gave me a number to build the response around, and given the staffing gap, narrowing the analyst's focus felt efficient rather than risky in the moment.",
          "evidence_explanation": "Explicitly describes building the response around the anchor value rather than independently deriving severity."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I knew the score doesn't weigh account privilege. I just didn't push past it that morning.",
          "evidence_explanation": "Confirms the anchor was accepted despite known missing information, indicating insufficient adjustment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Without a number already on the screen, I might have leaned harder on the account's privilege level from the start and caught the auth-server overlap sooner.",
          "evidence_explanation": "Counterfactual from the participant supports that the pre-existing numeric score causally altered the reasoning path."
        }
      ],
      "correction_or_counterevidence": "The IP overlap was later noticed midday and the incident was escalated, but this occurred only after a delay; the eventual correction does not erase the initial anchoring effect on the triage decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue or maintain a course of action because of previously invested resources, even when future costs and benefits do not justify it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR and threat-intel vendor renewal decision",
      "decision_point_description": "Choosing whether to renew the incumbent vendor or evaluate and potentially switch to procurement-flagged alternatives.",
      "affected_reasoning_operation": "Vendor evaluation and renewal choice",
      "bias_specific_mechanism": "Past investments in custom detection logic and dashboards were treated as a primary justification for renewal, rather than evaluating current and future value against alternatives.",
      "manifestation_in_interview": "The participant stated that renewal was mostly driven by existing investment and that switching felt costly because of what had already been built, without closely evaluating procurement's alternative options.",
      "effect_on_reasoning_or_decision": "Reduced the considered vendor set to the incumbent and one peer competitor, and biased the decision toward renewal.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Mostly the investment already sitting in our detection rules and dashboards. Rebuilding that on a new platform is real time and real exposure, especially mid-incident.",
          "evidence_explanation": "Shows the renewal rationale foregrounded irrecoverable past investment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was more that switching felt costly given what we'd already built.",
          "evidence_explanation": "Direct statement that past build costs drove the perceived costliness of switching."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Procurement had actually flagged three other vendors with comparable bundles this cycle, including transition support that looked broadly workable, but I didn't work through that list closely.",
          "evidence_explanation": "Demonstrates that lower-transition-cost alternatives were available but not fully evaluated due to the focus on sunk investment."
        }
      ],
      "correction_or_counterevidence": "The participant noted a possible legitimate concern that switching mid-incident creates exposure; however, he stated the core reasoning was sunk integration work, which is not a forward-looking cost-benefit rationale.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "endowment effect",
      "alternative_labels": [
        "ownership bias",
        "IKEA effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to ascribe greater value to objects or assets because one owns or has built them, independent of objective market value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "EDR and threat-intel vendor renewal decision",
      "decision_point_description": "Valuing the existing custom detection dashboards and their role in the renewal decision.",
      "affected_reasoning_operation": "Valuation of existing in-house asset relative to alternatives",
      "bias_specific_mechanism": "Ownership of the custom-built dashboards inflated their perceived current value; the participant explicitly did not test this feeling against procurement's alternatives.",
      "manifestation_in_interview": "The participant said the dashboards felt more valuable because they were 'ours,' and that he did not actually sit down and test whether that feeling matched current value.",
      "effect_on_reasoning_or_decision": "Reinforced the renewal decision by making the incumbent investment appear more valuable than an objective comparison might support.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, those dashboards just felt more valuable because they were ours — built by my own team over years — and I didn't actually sit down and test whether that feeling matched their current value against what procurement's options offered.",
          "evidence_explanation": "Direct expression of ownership-based valuation and failure to test it against external benchmarks."
        }
      ],
      "correction_or_counterevidence": "Some subjective value may be legitimate if the team's tacit knowledge materially reduces future customization costs; however, the participant explicitly acknowledged he did not verify this, so the ownership distortion remains evident.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "overconfidence effect",
      "alternative_labels": [
        "overprecision",
        "illusion of certainty"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A well-established tendency for subjective confidence in a judgment or capability to exceed objective accuracy or support.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment decision after lateral movement confirmation",
      "decision_point_description": "Deciding between full segment isolation and targeted lockout/monitoring based on the unvalidated monitoring script.",
      "affected_reasoning_operation": "Assessment of monitoring control adequacy as a risk management safeguard",
      "bias_specific_mechanism": "The participant relied on a monitoring script as sufficient coverage despite the team having no evidence that it could detect the same credentials being reused on another host or parallel session.",
      "manifestation_in_interview": "He acknowledged the script had not been validated, but reported that 'having eyes on that one account felt like enough to hold off on isolation.'",
      "effect_on_reasoning_or_decision": "Lowered the perceived need for isolation and contributed to the choice of targeted lockout and monitoring; the compromise later touched a second system the script did not watch.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Nobody had actually validated whether that script would catch the same credentials being reused on a different host or opening a parallel session elsewhere — but in the moment, having eyes on that one account felt like enough to hold off on isolation.",
          "evidence_explanation": "Demonstrates confidence in the script beyond its empirical support directly shaped the containment choice."
        }
      ],
      "correction_or_counterevidence": "Subsequent events showed that the compromise touched a second system the script was not watching, confirming the confidence was misplaced; this is outcome evidence, but the transcript already establishes that no validation existed at the time.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "certainty effect",
      "alternative_labels": [
        "ambiguity aversion"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to overweight outcomes that are certain relative to outcomes that are merely possible or poorly quantified.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Containment decision after lateral movement confirmation",
      "decision_point_description": "Weighing a certain near-term revenue-processing loss against an unquantified security benefit from full segment isolation.",
      "affected_reasoning_operation": "Risk–benefit tradeoff and containment selection",
      "bias_specific_mechanism": "The certain $180,000 processing-fee loss from isolation was salient and quantified, while the security benefit of isolation was unquantified; the participant treated the certain loss as making isolation 'feel like the more expensive option' despite being unable to quantify the alternative.",
      "manifestation_in_interview": "The participant explicitly said the guaranteed dollar figure against an unquantified benefit made isolation feel more expensive.",
      "effect_on_reasoning_or_decision": "Tipped the containment decision toward targeted lockout and monitoring rather than full isolation, even though the relative expected cost had not been calculated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The CFO's framing was blunt: isolating payments meant a guaranteed same-day hit, around $180,000 in processing fees. That number was concrete and immediate. The security upside from isolating wasn't quantified the same way — it was 'reduces risk,' not a figure.",
          "evidence_explanation": "Shows the decision inputs were asymmetric: one side was certain and quantified, the other vague."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, the guaranteed dollar figure against an unquantified benefit made isolation feel like the more expensive option, even though I couldn't put a number on the other side.",
          "evidence_explanation": "Direct statement of certainty-based weighting rather than calculated expected-value comparison."
        }
      ],
      "correction_or_counterevidence": "Avoiding a certain $180,000 loss might be a defensible operational choice under ambiguity, but the participant's own description indicates isolation was judged through the felt weight of the certain loss rather than a structured assessment of the unquantified security benefit.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "anchoring bias",
      "alternative_labels": [
        "anchoring effect",
        "insufficient adjustment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial number when estimating or deciding, with insufficient adjustment from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Board remediation budget recommendation",
      "decision_point_description": "Selecting a single budget number for the board after receiving current quotes of $310,000–$340,000.",
      "affected_reasoning_operation": "Budget estimation and numerical recommendation",
      "bias_specific_mechanism": "The stale $240,000 figure from 18 months earlier served as an anchor; current quotes were available, but the participant adjusted only slightly from the historical reference rather than re-basing on the new data.",
      "manifestation_in_interview": "He reported choosing a figure close to the original $240,000, nudged up, and explained that it was the existing reference point in his head.",
      "effect_on_reasoning_or_decision": "The board recommendation likely understated current project costs relative to this week's vendor quotes.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with something close to the original $240,000, nudged up a bit, rather than building the recommendation off this week's actual quotes.",
          "evidence_explanation": "Directly shows the old figure, not new quotes, was the basis for the recommendation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was already the reference point in my head from prior planning cycles. Adjusting it felt like less friction than justifying a jump straight to $340,000 without more scoping work behind it.",
          "evidence_explanation": "Explains the anchor-plus-insufficient-adjustment process."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Get fresh numbers before you anchor on the old one. Even under deadline pressure, a couple of quotes reframes the whole conversation.",
          "evidence_explanation": "The participant's own retrospective advice confirms he recognizes the old estimate acted as an anchor."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure and lack of scoping work could partially explain reluctance to jump to $340,000; however, the participant himself identified the stale figure as an anchor and did not use the fresh quotes as the base case.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied in the RAG context; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "attentional bias",
      "alternative_labels": [
        "tunnel vision",
        "selective attention"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial concurrent SIEM alert handling",
      "supporting_interview_quote": "I didn't loop the second alert in as something to check in parallel — the analyst was stretched thin, and the jump server was the concrete lead.",
      "plausible_mechanism": "The more concrete jump-server alert captured attention and may have narrowed processing of the earlier lower-priority alert.",
      "why_not_identified": "The transcript also describes a real staffing shortage and a deliberate security triage choice; resource constraints and normal prioritization are plausible non-bias explanations, so a distinct attentional distortion was not affirmatively isolated."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "social proof",
      "alternative_labels": [
        "bandwagon effect",
        "normative social influence"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Vendor shortlist construction",
      "supporting_interview_quote": "A couple of peer CISOs mentioned they use either this vendor or the closest competitor, so my real comparison ended up being just those two.",
      "plausible_mechanism": "Social information from peers may have narrowed the option set to the choices others use.",
      "why_not_identified": "Peer references are a common and often reasonable input in vendor selection; there is insufficient evidence that social proof caused the constrained comparison rather than simply informing it."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "status quo bias",
      "alternative_labels": [
        "default bias"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "EDR and threat-intel vendor renewal decision",
      "supporting_interview_quote": "Switching felt costly given what we'd already built.",
      "plausible_mechanism": "Preference for the current vendor may have been reinforced by the status quo, independent of sunk costs.",
      "why_not_identified": "The more specific and explicitly evidenced mechanisms in this episode are sunk-cost fallacy and endowment effect; status quo bias is plausible but not independently confirmed."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved scientific-corpus passages were provided as RAG context; bias labels and mechanisms rely on established cognitive-science knowledge rather than corpus citations.",
    "Analysis is based on a single self-reported interview, so diagnostic confidence depends on the participant's narrative fidelity and may include post-hoc rationalization.",
    "The interview was not conducted under controlled experimental conditions; operational constraints and legitimate heuristics may overlap with bias mechanisms.",
    "Only biases with affirmative transcript evidence were classified; other plausible but under-evidenced patterns are listed as candidates."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "CS_Counterfactual_7_Gemini_off",
  "interview_id": "CS_Counterfactual_7",
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
