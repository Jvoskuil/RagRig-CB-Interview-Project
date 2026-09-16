You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Before we start, I want to confirm this is being recorded for internal process review, and that's fine with you?

Participant: Yeah, that's fine.

Interviewer: Great. Can you tell me your role and roughly how long you've been in it?

Participant: I'm the senior systems administrator for network infrastructure. I've owned our remote-access stack — VPN concentrator, firewall, related ACLs — for about six years now. Small team, just me and one other engineer.

Interviewer: Perfect. I'd like you to walk me through a specific incident — the VPN concentrator vulnerability from earlier this year. Just give me the whole story first, then we'll go back through it in detail.

Participant: Sure. So the vendor disclosed a critical remote-code-execution CVE in our concentrator's firmware — a 9.8 on the CVSS scale, about as bad as it gets. Same day, they released a patch. I applied it within a few hours, tested it, no issues. That part was straightforward. The bigger question was what to do longer-term. We'd actually scoped a full move to a cloud-based Zero Trust setup about eight months earlier, but it got shelved — budget cycle, other priorities. When this CVE hit, leadership asked whether we should revisit that. I ended up recommending we stay on the concentrator, patched and hardened, rather than restart the migration project right then.

Interviewer: And that decision stuck for how long?

Participant: About two weeks, until I actually did start engaging vendors — Vendor A, a cloud SASE/ZTNA platform, and Vendor B, an on-prem replacement appliance. I went back and forth, ended up shortlisting Vendor A. Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit. Migration got approved, and we scheduled the cutover. Vendor recommended a two-week parallel run where old and new systems operate side by side. I compressed that to one week based on how previous cutovers had gone for me. We had some rough days afterward — a subset of users with hybrid authentication had intermittent access failures for several days before we sorted it out.

Interviewer: Let's build the timeline in order. What happened right after you applied the patch?

Participant: It installed clean, no service interruption, users never noticed. Two days later the vendor put out a follow-up advisory saying they were seeing exploitation attempts in the wild against systems that hadn't patched yet. That validated the urgency, but we were already covered.

Interviewer: And the vendor evaluation — how did that actually unfold once proposals came in?

Participant: Vendor A's deck opened with a stat — 98% of their enterprise migrations completed without a reported incident. Vendor B's numbers came through an analyst report, phrased differently: 2% of their on-prem deployments had a post-install incident in year one. Cost and timeline were basically a wash between the two. A follow-up technical call later clarified those were actually describing the same rate, just worded differently. But by then I'd already shortlisted A.

Interviewer: What did the peer-forum conversation add?

Participant: I posted in a regional admin group, and the response was pretty clear — five of six comparable firms in our sector had already gone with Vendor A's platform. Nobody shared much detail about their own environments, though. One of those five later told me, in a follow-up call, that they'd had to roll back some legacy application integrations after their rollout.

Interviewer: Let's slow down on decision one — patch and stay versus migrate immediately versus take the concentrator offline. Walk me through your reasoning there.

Participant: Taking it fully offline wasn't realistic — that's our only remote-access path for twelve hundred people, including trading desk staff. Between patching-and-staying versus fast-tracking a full migration, I leaned toward staying. We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one. I'll admit, I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically.

Interviewer: What information did you have in front of you at that moment, versus what you were recalling from memory?

Participant: In front of me: the CVSS score, the patch itself, and honestly not much detail yet on real-world exploitation — that came two days later. What I was recalling was that other firm's incident, which I remembered in a lot of detail because it got so much attention at the time. I used that story more than the actual advisory language when I was framing the urgency internally.

Interviewer: Moving to the vendor decision — what specifically made Vendor A stand out?

Participant: Honestly, that 98% figure just read better. "98% success" sounds a lot more solid than "2% incident rate," even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials.

Interviewer: How much weight did the peer adoption numbers carry when you committed to Vendor A?

Participant: A lot, probably more than I'd like to admit. Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable.

Interviewer: And the parallel-run decision — why compress it to one week?

Participant: We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had. I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record. Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call.

Interviewer: What would have changed your decision at that last step?

Participant: If I'd mapped out specifically how the new authentication flow differed from what I'd handled before, rather than just leaning on "I've done this kind of thing before," I might have kept the full two weeks or pushed the date until we were fully staffed.

Interviewer: Last few questions. If the peer forum hadn't mentioned adoption numbers at all, do you think you'd have approached the vendor decision differently?

Participant: Probably. I think I'd have leaned more on the technical call that reconciled the two vendors' statistics, and maybe pushed harder for referenceable environments similar to ours before committing.

Interviewer: And if staffing had been full during the cutover?

Participant: I might still have compressed the timeline — that instinct came from my own history with cutovers, not just the staffing gap. But I probably would've caught the authentication mismatch sooner if I'd had a second set of eyes free to dig into it.

Interviewer: Anything you'd want more information on, if you were facing this again?

Participant: A cleaner side-by-side of vendor stats up front, normalized to the same format, so wording doesn't do the persuading. And probably a harder look at how similar peer environments actually were to ours before treating their choice as a green light.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IS_Biased_5",
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
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {
        "bias": "Status Quo Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Framing Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Bandwagon effect",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Overconfidence Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      },
      {
        "bias": "Availability Bias",
        "occurrences": 1,
        "mechanism_constraint": null
      }
    ],
    "target_bias_names": [
      "Status Quo Bias",
      "Framing Bias",
      "Bandwagon effect",
      "Overconfidence Bias",
      "Availability Bias"
    ],
    "requested_occurrence_count_for_each_bias": [
      { "bias": "Status Quo Bias", "requested_occurrences": 1 },
      { "bias": "Framing Bias", "requested_occurrences": 1 },
      { "bias": "Bandwagon effect", "requested_occurrences": 1 },
      { "bias": "Overconfidence Bias", "requested_occurrences": 1 },
      { "bias": "Availability Bias", "requested_occurrences": 1 }
    ],
    "planned_instance_ids": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias" },
      { "instance_id": "cb_02", "bias": "Availability Bias" },
      { "instance_id": "cb_03", "bias": "Framing Bias" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias" }
    ],
    "intended_decision_points": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias", "decision_point": 1 },
      { "instance_id": "cb_02", "bias": "Availability Bias", "decision_point": 1 },
      { "instance_id": "cb_03", "bias": "Framing Bias", "decision_point": 2 },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "decision_point": 3 },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "decision_point": 4 }
    ],
    "intended_mechanisms": [
      {
        "instance_id": "cb_01",
        "bias": "Status Quo Bias",
        "mechanism": "Defaulting to retaining the familiar legacy VPN concentrator over an equally viable migration alternative, justified by familiarity rather than comparative analysis",
        "affected_reasoning_operation": "Option evaluation / choice among alternatives",
        "evidence_source": "Availability of an equally-costed migration option scoped 8 months prior, versus decision to retain legacy system",
        "distinctiveness_requirement": "Distinguished from cb_02 by concerning the choice of architecture itself, not the probability estimate of harm"
      },
      {
        "instance_id": "cb_02",
        "bias": "Availability Bias",
        "mechanism": "Overweighting a vivid, memorable peer-firm ransomware incident when estimating the likelihood/severity of the current CVE, rather than relying on the CVE's own technical exploitation evidence",
        "affected_reasoning_operation": "Probability/risk estimation",
        "evidence_source": "Recalled peer-firm breach narrative versus CVSS/technical advisory data",
        "distinctiveness_requirement": "Distinguished from cb_01 by concerning risk-severity judgment, not the architectural choice; uses a different evidence source (recalled incident vs. institutional familiarity)"
      },
      {
        "instance_id": "cb_03",
        "bias": "Framing Bias",
        "mechanism": "Vendor preference shifts based on whether a statistically equivalent figure is presented as a success rate versus an incident rate",
        "affected_reasoning_operation": "Comparative evaluation of vendor evidence",
        "evidence_source": "Vendor A '98% success' framing versus Vendor B '2% incident' framing of an equivalent statistic",
        "distinctiveness_requirement": "Unique to Decision Point 2; no other instance involves numerically equivalent statistics presented in different valence"
      },
      {
        "instance_id": "cb_04",
        "bias": "Bandwagon effect",
        "mechanism": "Treating peer-adoption volume as sufficient validation of vendor fit, substituting for independent compatibility verification",
        "affected_reasoning_operation": "Evidence weighting / decision justification",
        "evidence_source": "Peer forum report that 5 of 6 comparable firms adopted Vendor A, absent environment-specific compatibility data",
        "distinctiveness_requirement": "Unique to Decision Point 3; concerns social-proof weighting rather than statistical framing or architectural inertia"
      },
      {
        "instance_id": "cb_05",
        "bias": "Overconfidence Bias",
        "mechanism": "Overestimating personal capability to manage a materially different cutover based on unrelated past successes, leading to compression of a recommended safety margin under reduced staffing",
        "affected_reasoning_operation": "Self-assessment of capability applied to risk-mitigation planning",
        "evidence_source": "Three prior successful cutovers (different architecture) cited to justify shortening the vendor-recommended parallel-run period despite reduced staffing and a new authentication model",
        "distinctiveness_requirement": "Unique to Decision Point 4; concerns self-assessed capability, not external social or vendor evidence"
      }
    ],
    "intended_strength": [
      { "instance_id": "cb_01", "bias": "Status Quo Bias", "strength": "subtle" },
      { "instance_id": "cb_02", "bias": "Availability Bias", "strength": "subtle" },
      { "instance_id": "cb_03", "bias": "Framing Bias", "strength": "moderate" },
      { "instance_id": "cb_04", "bias": "Bandwagon effect", "strength": "subtle" },
      { "instance_id": "cb_05", "bias": "Overconfidence Bias", "strength": "moderate" }
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": "Public exploitation status of the CVE at the time of initial triage",
      "original_state": "No confirmed in-the-wild exploitation reported at Decision Point 1; confirmation arrives two days later",
      "changed_state": "Confirmed active in-the-wild exploitation against the firm's own IP range already reported at Decision Point 1",
      "variables_to_hold_constant": [
        "Vendor proposals and statistical framing",
        "Peer-adoption pattern and forum content",
        "Staffing levels and cutover timeline",
        "All four decision points and their alternatives"
      ]
    },
    "scenario_id": "IS_Biased_5",
    "domain_id": "IS",
    "total_requested_occurrences": 5,
    "total_planned_occurrences": 5,
    "allocation_rule_used": "Occurrences spread across 4 decision points per mechanism fit and narrative realism; Decision Point 1 hosts two distinct biases (Status Quo Bias and Availability Bias) using separate evidence sources and reasoning operations (architectural choice vs. probability estimation), consistent with allocation rules 1-4. No bias exceeds one instance per decision point, so the same-bias co-location cap (rule 3) is not triggered.",
    "control_zero_bias_requirement": false,
    "variables_to_hold_constant": [
      "Vendor proposals and statistical framing",
      "Peer-adoption pattern and forum content",
      "Staffing levels and cutover timeline",
      "All four decision points and their alternatives"
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
          "segment_type": "operational_constraint_reasoning",
          "raw_interview_anchor": "Taking it fully offline wasn't realistic — that's our only remote-access path for twelve hundred people, including trading desk staff.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A substantive continuity and availability constraint supporting the decision, without a hidden bias mechanism."
        },
        {
          "segment_id": "seg_002",
          "speaker": "Participant",
          "segment_type": "architecture_choice_reasoning",
          "raw_interview_anchor": "We have six years of ACLs and firewall rules tuned exactly to how our network behaves — I know that system cold. Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_01"],
          "ground_truth_rationale": "The participant explicitly gives the familiar existing system extra weight and does not comparatively evaluate the migration alternative, matching Status Quo Bias."
        },
        {
          "segment_id": "seg_003",
          "speaker": "Participant",
          "segment_type": "risk_estimation_and_urgency_reasoning",
          "raw_interview_anchor": "That breach a peer firm had a couple years back ... was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically. ... I used that story more than the actual advisory language when I was framing the urgency internally.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_02"],
          "ground_truth_rationale": "A vivid recalled peer ransomware incident was given more weight than the current advisory when communicating risk, matching Availability Bias."
        },
        {
          "segment_id": "seg_004",
          "speaker": "Participant",
          "segment_type": "comparative_vendor_evaluation",
          "raw_interview_anchor": "Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_03"],
          "ground_truth_rationale": "The participant preferred statistically equivalent information because of its positive versus negative wording, matching Framing Bias."
        },
        {
          "segment_id": "seg_005",
          "speaker": "Participant",
          "segment_type": "peer_evidence_weighting",
          "raw_interview_anchor": "Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint ... I figured if that many peers were comfortable, the risk was manageable.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_04"],
          "ground_truth_rationale": "Peer-adoption volume substituted for independent compatibility verification, matching the Bandwagon effect."
        },
        {
          "segment_id": "seg_006",
          "speaker": "Participant",
          "segment_type": "staffing_constraint_reasoning",
          "raw_interview_anchor": "We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": false,
          "ground_truth_instance_ids": [],
          "ground_truth_rationale": "A genuine staffing-based operational rationale; the hidden Overconfidence instance is mapped to the separate generalization from prior cutovers."
        },
        {
          "segment_id": "seg_007",
          "speaker": "Participant",
          "segment_type": "cutover_risk_mitigation_reasoning",
          "raw_interview_anchor": "I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable ... those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["cb_05"],
          "ground_truth_rationale": "The participant generalized from prior successes to a materially different architecture and compressed a recommended safety margin, matching Overconfidence Bias."
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
    "analysis_scope_note": "This analysis covers the single participant interview transcript. It identifies affirmative, mechanism-grounded cognitive bias occurrences. No retrieved RAG corpus passages were supplied, so classifications rely on established cognitive-science knowledge and are marked as lacking retrieved corpus support."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Overconfidence effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Status quo bias",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Status quo bias",
      "alternative_labels": [
        "Default bias",
        "Status quo preference"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to prefer the current state of affairs and to treat the status quo as a reference point, weighting potential losses from change more heavily than equivalent gains.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision one: patch-and-stay vs migrate immediately vs take concentrator offline",
      "decision_point_description": "Leadership asked whether to revisit the cloud Zero Trust migration after a critical VPN concentrator firmware CVE; the participant recommended staying on the patched concentrator.",
      "affected_reasoning_operation": "Option evaluation and recommendation under uncertainty",
      "bias_specific_mechanism": "The participant overweighted retaining the existing VPN concentrator because it was the known current environment, without systematically evaluating a fast-tracked migration's rollback plan or transition controls.",
      "manifestation_in_interview": "The participant reported giving staying extra weight because the system was familiar and treating the change as an unknown risk, rather than comparing the alternatives analytically.",
      "effect_on_reasoning_or_decision": "The recommendation was biased toward retaining the patched concentrator and left the fast-track migration option insufficiently evaluated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I didn't sit down and actually work through what a fast-tracked migration's rollback plan or transition controls would have looked like on that timeline; I just gave staying extra weight because it was the environment I already knew inside and out. Ripping it out mid-crisis felt like trading a known, contained problem for an unknown one.",
          "evidence_explanation": "The participant explicitly states that familiarity with the current system caused him to overweight staying and that he did not analytically compare the migration alternative, which is the core status quo mechanism."
        }
      ],
      "correction_or_counterevidence": "The patch was technically appropriate and urgent, and staying on a patched system could also be a defensible risk-avoidance strategy under uncertainty; however, the explicit overweighting of the current state was not corrected during the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG corpus passages were supplied. Status quo bias classification uses established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A mental shortcut in which the perceived likelihood or importance of an event is influenced by how easily examples come to mind.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Risk and urgency framing after the VPN concentrator patch",
      "decision_point_description": null,
      "affected_reasoning_operation": "Risk perception and urgency communication",
      "bias_specific_mechanism": "The vivid, easily recalled ransomware incident at a peer firm disproportionately influenced the participant's internal framing of urgency, more than the actual advisory language or CVSS specifics.",
      "manifestation_in_interview": "The participant described recalling a peer firm's unpatched VPN breach in detail and using that story more than the vendor advisory when framing urgency internally.",
      "effect_on_reasoning_or_decision": "It amplified the salience of the breach narrative in the participant's urgency framing, shaping internal risk communication even though the formal CVSS severity already justified patching.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I was also thinking about that breach a peer firm had a couple years back — their whole incident started with an unpatched VPN box, and it got ugly, ransomware, the works. That was very much in my head when I was explaining to leadership why we needed to move fast on the patch specifically.",
          "evidence_explanation": "The participant's recollection of a highly salient past incident was actively used to frame current urgency, indicating availability-based weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I used that story more than the actual advisory language when I was framing the urgency internally.",
          "evidence_explanation": "This explicitly confirms that the remembered example received greater weight than the current advisory information, a hallmark of the availability heuristic."
        }
      ],
      "correction_or_counterevidence": "The CVSS score and later exploitation advisory independently supported urgent patching, so the heuristic may not have changed the patch decision itself, but it did affect the internal framing and emphasis.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG corpus passages were supplied. Availability heuristic classification uses established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Framing effect",
      "alternative_labels": [
        "Attribute framing",
        "Valence framing",
        "Equivalence framing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which equivalent information presented with different wording or valence systematically changes judgment or choice.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor evaluation and shortlisting",
      "decision_point_description": "Choosing between Vendor A, a cloud SASE/ZTNA platform, and Vendor B, an on-prem replacement appliance, after proposals were received.",
      "affected_reasoning_operation": "Comparative vendor risk and quality assessment",
      "bias_specific_mechanism": "The participant evaluated statistically equivalent outcome rates differently based on positive versus negative framing, favoring the 98% success frame over the 2% incident frame without normalizing them before shortlisting.",
      "manifestation_in_interview": "The participant reported that the 98% success figure read better, that it colored his reading of the rest of Vendor A's materials, and that he did not perform the equivalence conversion at the time.",
      "effect_on_reasoning_or_decision": "It made Vendor A appear stronger than Vendor B despite equivalent underlying incident rates, influencing the shortlist decision before the technical clarification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, that 98% figure just read better. '98% success' sounds a lot more solid than '2% incident rate,' even though — yeah, in hindsight those are the same number. At the time I didn't sit down and do that conversion. I took the framing at face value and it colored how I read the rest of their materials.",
          "evidence_explanation": "This directly shows that statistically equivalent information was judged more favorably when framed as success rather than incident, and that this framing influenced the participant's broader assessment of Vendor A before the shortlist decision."
        }
      ],
      "correction_or_counterevidence": "A later technical call clarified the equivalence, but the shortlisting had already occurred by then, indicating the distortion was not corrected before the choice.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG corpus passages were supplied. Framing effect classification uses established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Bandwagon effect",
      "alternative_labels": [
        "Social proof",
        "Herd behavior"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a belief or course of action because many others have done so, rather than based on independent evaluation of the evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor evaluation and commitment",
      "decision_point_description": "After informal outreach, the participant used peer adoption information to commit to Vendor A.",
      "affected_reasoning_operation": "Evidence weighting and risk assessment in vendor choice",
      "bias_specific_mechanism": "Five of six peer firms using Vendor A was treated as a strong risk-reducing signal, and the participant did not investigate whether peers shared the organization's legacy authentication and application footprint.",
      "manifestation_in_interview": "The participant stated that the peer adoption count carried substantial weight and that he did not push hard on environmental differences, inferring manageable risk from majority adoption.",
      "effect_on_reasoning_or_decision": "It increased commitment to Vendor A based on majority adoption, reducing scrutiny of fit-specific risks.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Five out of six firms choosing the same platform felt like a strong signal on its own. I didn't push hard on whether any of them had our specific legacy app footprint — nonstandard authentication stuff we run for a couple of older line-of-business systems. I figured if that many peers were comfortable, the risk was manageable.",
          "evidence_explanation": "The participant explicitly treated the majority choice as sufficient evidence of manageable risk and acknowledged failing to investigate whether the peer environments actually matched the organization's specific footprint."
        }
      ],
      "correction_or_counterevidence": "Peer adoption can be informative in technology markets; however, the participant later acknowledged the environments may not have been comparable, and one peer had not shared its rollback issues before the commitment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG corpus passages were supplied. Bandwagon effect classification uses established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Overconfidence effect",
      "alternative_labels": [
        "Overconfidence bias",
        "Overprecision",
        "Illusion of validity"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A bias in which a person's subjective confidence in their judgments or decisions is greater than their objective accuracy, often supported by over-reliance on personal experience.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Parallel-run scheduling and cutover execution",
      "decision_point_description": "Deciding whether to accept the vendor's two-week parallel run or compress it to one week while down a staff member.",
      "affected_reasoning_operation": "Risk estimation and schedule decision",
      "bias_specific_mechanism": "The participant relied on a personal history of successful cutovers without accounting for material differences in the new platform's authentication model, producing overconfidence in a shorter parallel-run window.",
      "manifestation_in_interview": "The participant described compressing the parallel run because prior cutovers had gone fine, then acknowledged that those earlier cutovers were on familiar architecture while the new platform used a different authentication model.",
      "effect_on_reasoning_or_decision": "It led to a compressed one-week parallel run, contributing to several days of access failures for some users.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We were down a person — my other engineer was out — and the vendor's two-week default felt like it assumed more hands than we had. I've done three cutovers before without any formal parallel-run phase at all and they went fine, so a compressed one-week window with the new platform felt reasonable to me based on that track record.",
          "evidence_explanation": "The participant used prior successful cutover experiences to justify confidence in a shorter parallel run despite a different staffing context and platform."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, those earlier cutovers were on architecture I already knew well. This was a genuinely different authentication model, and I didn't really weigh that difference when I made the call.",
          "evidence_explanation": "This shows that the confidence was based on experiences that differed materially from the current situation, and that those differences were not incorporated into the schedule decision."
        }
      ],
      "correction_or_counterevidence": "Staffing constraints were real; however, the participant's own counterfactual indicates that mapping the authentication differences might have changed the schedule, and some users experienced access failures.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No RAG corpus passages were supplied. Overconfidence effect classification uses established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Confirmation bias",
      "alternative_labels": [
        "Myside bias",
        "Selective exposure"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Post-shortlisting peer outreach and vendor commitment",
      "supporting_interview_quote": "Then I did some informal outreach to peers at other firms our size, learned a lot of them had already gone with Vendor A. That helped me commit.",
      "plausible_mechanism": "The participant may have sought or weighted peer evidence that supported the already-formed Vendor A shortlist and did not seek out or weigh disconfirming examples.",
      "why_not_identified": "The transcript does not demonstrate that the outreach process was structured to confirm the shortlist; reference checking is also a legitimate evaluation step, and there is no clear evidence that contradictory peer signals were available and ignored."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were provided; classifications rely on established cognitive-science knowledge rather than supplied RAG evidence.",
    "The interview is retrospective and self-reported, so memory and reconstruction may affect the precision of bias attributions.",
    "The analysis is limited to the single transcript and does not include actual decision artifacts, emails, or third-party accounts.",
    "Low-confidence findings reflect plausible but less direct evidence, and competing explanations cannot be fully excluded."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Biased_5_Gemini_off",
  "interview_id": "IS_Biased_5",
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
