You are an expert occupational interviewer and realistic dialogue writer.

Generate one simulated cognitive task analysis interview from the supplied generation specification. The interview will be given to an independent evaluator that must infer whether specified cognitive biases are present. Do not reveal the labels or your construction process.

INPUT
Generation specification:
{{"scenario_id": "IS_Biased_5",
  "domain_id": "IS",
  "domain": "Information Systems, Human-Computer Interaction, and Interaction Design",
  "role": "Enterprise IT Systems Administrator",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Legacy VPN Concentrator CVE",
    "scenario_summary_internal": "A senior enterprise systems administrator at a mid-size financial-services firm learns of a critical remote-code-execution CVE affecting the company's on-premises VPN concentrator, the sole remote-access gateway for ~1,200 employees. Over roughly two weeks, the administrator must decide how to mitigate immediate risk, evaluate whether to replace the legacy appliance with a cloud-based Zero Trust Network Access (ZTNA) service, weigh peer-industry adoption patterns, and finally decide how to execute the cutover. The incident is realistic, nonroutine, and technically grounded, with genuine trade-offs (uptime, budget, staff bandwidth, vendor lock-in) that make each decision defensible on its face while still containing the planted biases.",
    "occupational_realism": {
      "objective": "Contain the immediate security exposure from the disclosed CVE while deciding on a durable remote-access architecture without causing an outage for the trading and client-service teams.",
      "setting": "Mid-size financial-services firm, ~1,200 employees, hybrid on-prem/cloud infrastructure, administrator has been responsible for the VPN concentrator for six years",
      "constraints": [
        "Patch window must avoid trading-hours downtime",
        "Limited internal staff (two-person network team) to run a parallel migration",
        "Budget approval cycle for new vendor contracts takes 3-4 weeks",
        "Regulatory requirement for continuous remote-access logging during any transition",
        "Existing VPN concentrator has 6 years of tuned firewall/ACL rules"
      ],
      "stakeholders": [
        "CISO",
        "Network team (2 engineers)",
        "End users (remote and hybrid staff)",
        "VPN/ZTNA vendors",
        "Compliance officer",
        "IT peers at partner firms"
      ],
      "technical_terms_to_use": [
        "CVE",
        "remote code execution",
        "VPN concentrator",
        "Zero Trust Network Access (ZTNA)",
        "SASE",
        "patch window",
        "attack surface",
        "parallel cutover",
        "ACL",
        "IOC (indicator of compromise)"
      ],
      "technical_terms_to_avoid": [
        "cognitive bias",
        "heuristic",
        "anchoring",
        "framing effect",
        "bandwagon",
        "status quo bias",
        "overconfidence",
        "availability heuristic"
      ]
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor disclosed a critical RCE CVE (CVSS 9.8) in the VPN concentrator firmware",
          "A firmware patch is available same-day",
          "A full ZTNA migration was scoped 8 months earlier as a 'someday' project and shelved",
          "Two years prior, a similarly-sized peer firm suffered a highly publicized ransomware breach that traced back to an unpatched VPN appliance"
        ],
        "new_information_after_decision": [
          "Patch installs cleanly with no immediate incidents",
          "Vendor releases an advisory two days later noting exploitation attempts detected in the wild against unpatched systems"
        ],
        "alternatives": [
          "Apply the emergency patch and continue operating the legacy concentrator as-is",
          "Apply the patch as a stopgap but immediately fast-track full decommissioning and migration to a cloud-based solution",
          "Take the concentrator offline entirely until a longer-term architecture decision is made"
        ],
        "intended_action": "Administrator applies the patch and elects to keep the legacy VPN concentrator as the long-term architecture, citing institutional familiarity and six years of tuned configuration, while also privately overweighting the risk of a repeat of the peer firm's dramatic ransomware incident when justifying urgency to leadership."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Two migration vendor proposals received: Vendor A (cloud SASE/ZTNA) and Vendor B (on-prem replacement appliance)",
          "Vendor A's pitch deck states '98% of enterprise migrations completed without a reported incident'",
          "Vendor B's comparable statistic, from an independent analyst report, is phrased as '2% of on-prem appliance deployments experienced a post-install incident in year one'",
          "Both proposals have similar cost and implementation timelines"
        ],
        "new_information_after_decision": [
          "A follow-up technical call reveals Vendor A's 98% figure and Vendor B's implied 98% success rate describe statistically comparable outcomes",
          "Compliance flags that both vendors meet the firm's logging requirements"
        ],
        "alternatives": [
          "Shortlist Vendor A based on the migration-success framing",
          "Shortlist Vendor B based on the incident-rate framing",
          "Request both vendors resubmit identical statistics in a standardized format before deciding"
        ],
        "intended_action": "Administrator shortlists Vendor A, explicitly citing the '98% success' language as more reassuring than Vendor B's materials, without recognizing the two statistics are numerically equivalent."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Administrator posts in a regional IT-admin peer forum and learns 5 of 6 comparable firms in the sector have already adopted Vendor A's SASE platform",
          "None of the peer firms shared environment-specific details (user count, legacy integrations, compliance scope)",
          "The firm's own environment has several legacy line-of-business apps with nonstandard authentication that Vendor A has not been tested against internally"
        ],
        "new_information_after_decision": [
          "A follow-up peer call reveals one of the five adopting firms had to roll back a subset of legacy app integrations after their SASE rollout"
        ],
        "alternatives": [
          "Proceed with Vendor A based on the visible peer-adoption trend",
          "Commission an internal compatibility test against the legacy line-of-business apps before committing",
          "Request references specifically from peer firms with similar legacy-app footprints"
        ],
        "intended_action": "Administrator commits to Vendor A largely on the strength of the peer-adoption pattern, treating the number of adopting firms as sufficient validation without independently verifying compatibility with the firm's own legacy applications."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Migration plan calls for a phased cutover with a two-week parallel-run period as the vendor's recommended default",
          "Administrator has successfully executed three prior infrastructure cutovers without a formal parallel-run phase",
          "Network team is at reduced capacity (one engineer on leave) during the proposed cutover window"
        ],
        "new_information_after_decision": [
          "Cutover proceeds with a compressed one-week parallel run; a subset of hybrid-authentication users experience intermittent access failures for several days before being resolved"
        ],
        "alternatives": [
          "Follow the vendor-recommended two-week parallel-run period in full",
          "Compress the parallel-run period, relying on personal track record managing prior cutovers",
          "Delay the cutover until the network team is back to full staffing"
        ],
        "intended_action": "Administrator compresses the parallel-run period, asserting confidence in personal ability to manage the cutover manually based on past successes, without adjusting for the reduced staffing and the new authentication architecture being materially different from prior cutovers."
      }
    ],
    "probe_plan": {
      "opening": [
        "Walk me through what happened when you first learned about the VPN concentrator vulnerability.",
        "What was your role and what were you responsible for deciding?"
      ],
      "timeline_reconstruction": [
        "What happened right after the patch was applied?",
        "How did the vendor evaluation unfold once proposals came in?",
        "What did the peer-forum conversation add to your thinking?",
        "Walk me through the cutover itself, step by step."
      ],
      "decision_point_probes": [
        "What options did you consider before deciding to keep the legacy concentrator patched rather than replace it?",
        "What specifically made Vendor A's proposal stand out to you over Vendor B's?",
        "How much weight did the peer firms' adoption carry in your decision, and why?",
        "Why did you decide to shorten the parallel-run period?"
      ],
      "cues_and_information_sources": [
        "What information did you have in front of you at each of these moments?",
        "Which sources did you trust most, and why?"
      ],
      "goals_and_alternatives": [
        "What were you trying to balance or protect at each stage?",
        "What alternative would you have chosen if [X] hadn't been available?"
      ],
      "decision_basis_and_experience": [
        "What past experience did you draw on when making this call?",
        "How confident were you at the time, and what was that confidence based on?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure did you feel at each decision point?",
        "What were you most uncertain about?"
      ],
      "closing_hypotheticals": [
        "If the peer forum hadn't mentioned adoption numbers, would you have approached the vendor decision differently?",
        "If staffing had been full during the cutover, would you have changed the parallel-run length?",
        "Looking back, is there anything you'd want more information on before deciding again?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "cb_01",
        "bias": "Status Quo Bias",
        "decision_point": 1,
        "mechanism": "Administrator defaults to retaining the familiar, already-tuned legacy VPN concentrator over an equally viable migration path, treating the existing configuration as a safe default rather than one option among several with comparable effort",
        "affected_reasoning_operation": "Option evaluation / choice among alternatives",
        "evidence_available_at_time": [
          "Available patch resolves immediate CVE",
          "Migration project had already been scoped 8 months earlier at similar cost/effort",
          "No technical requirement forces continued reliance on the legacy appliance"
        ],
        "required_textual_manifestation": "Administrator explicitly justifies keeping the legacy system by appeal to familiarity/tuning ('six years of ACLs we know cold') rather than a comparative cost-benefit of the migration option",
        "plausible_nonbias_interpretation": "Sticking with a known, working system during a live security incident could be a legitimate risk-averse operational judgment rather than bias",
        "strength": "subtle",
        "do_not_make_explicit": ["status quo bias", "default effect", "inertia"]
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Bias",
        "decision_point": 1,
        "mechanism": "Administrator's urgency and risk estimate is driven disproportionately by the vivid, memorable peer-firm ransomware incident rather than base-rate exploitation likelihood for this specific CVE",
        "affected_reasoning_operation": "Probability/risk estimation",
        "evidence_available_at_time": [
          "CVSS score and vendor advisory describing exploitation risk in general terms",
          "A separately-recalled, dramatic ransomware incident at a peer firm two years earlier"
        ],
        "required_textual_manifestation": "Administrator cites the memorable peer breach by name/detail as the primary justification for how serious this CVE 'could' be, rather than citing the CVE's own technical exploitation data",
        "plausible_nonbias_interpretation": "Referencing a known industry incident as a cautionary benchmark is a reasonable communication tactic, not necessarily a distorted probability judgment",
        "strength": "subtle",
        "do_not_make_explicit": ["availability heuristic", "vividness", "recall bias"]
      },
      {
        "instance_id": "cb_03",
        "bias": "Framing Bias",
        "decision_point": 2,
        "mechanism": "Administrator's vendor preference shifts based on whether a statistically equivalent figure is presented as a success rate versus a failure/incident rate, rather than on the underlying number itself",
        "affected_reasoning_operation": "Comparative evaluation of vendor evidence",
        "evidence_available_at_time": [
          "Vendor A materials stating '98% success rate'",
          "Vendor B materials/analyst report stating '2% incident rate' (mathematically equivalent)"
        ],
        "required_textual_manifestation": "Administrator states a clear preference for Vendor A specifically because of how the statistic is worded, without independently converting or reconciling the two figures at the time of the decision",
        "plausible_nonbias_interpretation": "Vendor A's material may simply have been more thorough or trustworthy overall, independent of the wording of that one statistic",
        "strength": "moderate",
        "do_not_make_explicit": ["framing effect", "positive frame", "loss frame"]
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "decision_point": 3,
        "mechanism": "Administrator treats the number of peer firms adopting Vendor A as substantive validation of fit for their own environment, substituting peer-adoption volume for independent compatibility verification",
        "affected_reasoning_operation": "Evidence weighting / decision justification",
        "evidence_available_at_time": [
          "5 of 6 peer firms reportedly adopted Vendor A",
          "No peer data specific to the firm's own legacy line-of-business applications",
          "Known internal legacy authentication complexity not yet tested against Vendor A"
        ],
        "required_textual_manifestation": "Administrator explains the commitment to Vendor A primarily in terms of how many peers chose it, without describing an independent compatibility check performed before that commitment",
        "plausible_nonbias_interpretation": "Peer adoption can be a legitimate proxy for vendor reliability in the absence of other data, especially under time constraints",
        "strength": "subtle",
        "do_not_make_explicit": ["bandwagon effect", "social proof", "herd behavior"]
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "decision_point": 4,
        "mechanism": "Administrator overestimates personal ability to manage a materially different cutover (new authentication architecture, reduced staffing) based on unrelated past successes, leading to compression of a recommended safety margin",
        "affected_reasoning_operation": "Self-assessment of capability applied to risk-mitigation planning",
        "evidence_available_at_time": [
          "Vendor's recommended two-week parallel-run period",
          "Three prior successful cutovers without formal parallel-run phases (different architecture)",
          "Reduced team capacity due to one engineer on leave"
        ],
        "required_textual_manifestation": "Administrator justifies shortening the parallel-run period by citing personal track record on unrelated prior cutovers, without adjusting explicitly for the new authentication model or reduced staffing",
        "plausible_nonbias_interpretation": "Experienced administrators legitimately compress timelines based on genuine expertise; this alone would not indicate bias without the mismatch to the current context",
        "strength": "moderate",
        "do_not_make_explicit": ["overconfidence", "illusion of control", "self-assessment bias"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable: no paired vocabulary_control or ambiguous_control scenario was requested for this generation."
    },
    "counterfactual_specification": {
      "causal_variable": "Public exploitation status of the disclosed CVE at the time of the initial triage decision (autoselected as the most narratively load-bearing variable available for a future counterfactual pairing; not activated in this biased-condition run)",
      "original_state": "At Decision Point 1, no confirmed in-the-wild exploitation is reported; exploitation evidence emerges only two days later",
      "counterfactual_state": "At Decision Point 1, confirmed active in-the-wild exploitation against the firm's own IP range is already reported at the moment of triage",
      "variables_to_hold_constant": [
        "Vendor proposals and their statistical framing",
        "Peer-adoption pattern and peer forum content",
        "Staffing levels and cutover timeline",
        "All four decision points and their alternatives"
      ],
      "expected_causal_difference": "Earlier confirmed exploitation would be expected to reduce the influence of status-quo and availability-driven urgency-justification at Decision Point 1, since urgency would already be independently and objectively evidenced rather than inferred from a recalled peer incident.",
      "causal_test_question": "Does moving from ambiguous to confirmed active exploitation at the moment of triage change how much the administrator's urgency judgment depends on the recalled peer breach versus the CVE's own technical evidence?"
    },
    "generation_checks": [
      "Exactly 5 target biases, each with occurrences=1, each assigned exactly one instance_id (cb_01-cb_05)",
      "Exactly 4 decision points; Decision Point 1 carries two distinct biases (cb_01, cb_02) with clearly separated evidence sources and reasoning operations, consistent with allocation rule 4",
      "No decision point contains more than two occurrences of any single bias",
      "No unrequested bias (e.g., confirmation bias, anchoring) is intentionally embedded anywhere, including hypotheticals or outcome explanations",
      "Consequences described (patch success, later exploitation reports, rollback at a peer firm, temporary access failures) are realistic but do not mechanically prove any decision was biased",
      "Target interview length of 1,350 words (range 1,215-1,485) is achievable with 4 decision points, each requiring roughly 300-340 words of narrative plus probe responses, without repetitive exposition",
      "No bias terminology or psychological labels are scheduled to appear in the technical_terms_to_use list or probe_plan wording"
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
