<RAW_INTERVIEW>
Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific project experience, it'll be recorded for research purposes, and you can skip anything you'd rather not discuss. Sound okay?

Participant: Yeah, that's fine. Happy to walk through it.

Interviewer: Great. Can you start by telling me a bit about your role and the project we're discussing?

Participant: Sure. I'm the software architect on our customer portal modernization. We were rebuilding the self-service portal for retail banking customers — new interaction design, plus re-architecting the backend off a fairly old monolith. I owned the technical direction end to end, working with a UX researcher, our backend team, security and compliance, and an external vendor who helped with the front-end migration.

Interviewer: What was the objective when the project kicked off?

Participant: We had a hard deadline — six months — tied to a regulatory reporting change, so the date wasn't negotiable. The goal was a portal that was both more usable and could scale better, since the existing system was tightly coupled to our core banking platform and every change took forever to ship.

Interviewer: Walk me through how the project actually unfolded, from your perspective.

Participant: It started with scoping. We brought in a vendor to help estimate the front-end migration piece, since we didn't have deep in-house experience with the newer framework we wanted to use. Around the same time, we kicked off early usability testing on a new navigation model I'd designed — basically restructuring how customers move between the dashboard and their account details. That ran in parallel with an architecture debate on the backend: whether to do a more conservative monolith refactor or go further and decompose into microservices. That decision took a few weeks and involved looking at what similar firms had done. Once we picked a direction, we moved into execution, and about four months in we hit some turbulence — delays, a couple of outages, and separately, a mandate from security to change our authentication approach. That's roughly the shape of it.

Interviewer: Let's go back to the very beginning — the budget number. What happened there?

Participant: Finance needed a number within about a week to lock the budget, and we didn't have a detailed internal estimate yet — that takes real engineering time to build properly. So we did a scoping call with the vendor, and they gave us a rough order-of-magnitude figure for the migration, both cost and timeline.

Interviewer: What did you do with that figure?

Participant: I used it. Submitted it as our working budget baseline since it was the only concrete number on the table and finance needed something.

Interviewer: Did you consider other options — waiting, or giving a range instead?

Participant: We could have waited two more weeks for a real internal estimate, or given a range with caveats. I thought about the range option, actually, but figured a single number would be easier for finance to plan around, and the vendor had done similar migrations before, so it seemed like a reasonable placeholder.

Interviewer: What happened once the internal team produced their own estimate?

Participant: It came in about 40% higher. Some scope items the vendor hadn't accounted for — data migration edge cases, mostly. When I brought it to finance, I remember framing it as an overrun against the original number rather than as, you know, the number we probably should have started with. It became this whole conversation about why we were 40% over, when really the vendor's figure was just thin to begin with.

Interviewer: Looking back, how much weight do you think that early vendor number carried in later conversations?

Participant: Probably more than it should have. Every budget check-in after that referenced it as the baseline, even once we knew it wasn't built on solid scoping.

Interviewer: Let's move to the usability testing. What did that process look like?

Participant: We ran a round with ten beta users on the new navigation model. Results were mixed — six of ten had trouble moving between the dashboard and account sections, four completed tasks quickly and gave positive feedback. Our UX researcher's write-up flagged the navigation confusion as the top issue.

Interviewer: How did you interpret that split?

Participant: Honestly, I went back through the transcripts looking for more of the positive comments to include in the stakeholder readout. The four successful users had some pretty specific praise for the new layout, and I wanted that represented well. For the confusion cases, my read was that a lot of it looked like people just not being used to the new pattern yet — more of an onboarding gap than a structural flaw in the design.

Interviewer: Did you apply the same level of scrutiny to the positive responses as the negative ones?

Participant: That's a fair question. I don't think I dug into the positive transcripts looking for problems the same way I dug into the negative ones looking for mitigating explanations. I was fairly confident in the navigation model going in, so I think I was reading the results through that lens somewhat.

Interviewer: What did the follow-up round show?

Participant: Similar confusion rate with a different cohort. So it wasn't a one-off.

Interviewer: Now, the architecture decision — monolith refactor versus microservices. How did that get resolved?

Participant: That one took real debate. Monolith refactor was lower risk but wouldn't buy us much scalability. Microservices was a bigger lift but matched what we'd seen at a few peer firms — three other financial companies had presented case studies on similar decompositions at a conference a few months earlier. Our own backend risk memo called the microservices path "moderate risk, manageable with phased rollout."

Interviewer: What tipped the decision toward microservices?

Participant: The peer examples carried real weight for me, honestly. If three firms our size had gone that direction and it worked out, it felt like a validated path rather than something experimental. That was alongside the internal risk memo, but I'd say the industry pattern was part of what made me comfortable recommending it.

Interviewer: Around that time there was also a demo incident. Can you describe that?

Participant: Yeah — during a live demo for the executive sponsor, one beta session crashed. Visible, in the room, bad timing. That was against a backdrop of pretty strong pilot metrics otherwise — 92% of transactions completing successfully that week.

Interviewer: How did that crash factor into the risk assessment you presented afterward?

Participant: I'd be lying if I said it didn't dominate the narrative. When I put together the risk framing for leadership, that incident got a lot of airtime — more, probably, than a single session out of a whole pilot week statistically deserved. The 92% success rate was in there, but the crash was what people remembered, and honestly what I emphasized too when talking about where the risk actually sat.

Interviewer: Did you know at that point what caused the crash?

Participant: Not yet. Log review came later and traced it to a test-environment misconfiguration, not the architecture itself. But that came after the risk framing had already been shaped.

Interviewer: Let's get to four months in. What was happening then?

Participant: We'd cut over two of five planned services, both later than planned, integration bugs slowing things down. A monitoring report showed rising latency and two customer-facing outages tied to the new service mesh. On top of that, security formally mandated we switch to a centralized identity provider for authentication, citing a compliance finding.

Interviewer: What was your reaction to the mandate?

Participant: My first reaction, honestly, was frustration that it was being handed down as a directive rather than a conversation. We'd already built out our own authentication approach and gotten it partway implemented. I ended up drafting an alternative design that would satisfy the compliance finding a different way — partly because I wanted us to keep some control over that part of the architecture rather than just adopting what we were told to.

Interviewer: Did you have a specific technical concern with the mandated identity provider itself?

Participant: Not really a strong one at that point — we hadn't done a full technical comparison yet. It was more that being told "do it this way" rubbed me the wrong way given the work we'd already put in.

Interviewer: And the decision to keep going with the migration despite the delays and outages?

Participant: We talked about pausing. But we'd already cut over two services, and reverting those felt like it would waste months of work. Given the timeline pressure too, continuing forward seemed like the only path that didn't throw away what we'd built.

Interviewer: Did you weigh that against the possibility that continuing might cost more than stopping?

Participant: Not as rigorously as maybe I should have. The sunk work was very present in my mind at that moment.

Interviewer: If the vendor's early number had never come up, do you think the budget conversation would have gone differently?

Participant: Probably. Without an anchor point, finance might have pushed harder for the detailed estimate up front instead of accepting a placeholder.

Interviewer: If the demo crash hadn't happened in front of the executive sponsor, would your risk framing have looked different?

Participant: Almost certainly. I think the 92% number would have carried more weight in isolation.

Interviewer: If the security mandate had come as a suggestion rather than a directive, would your response have changed?

Participant: I think so. I might have approached the comparison more on the merits rather than looking for an alternative right away.

Interviewer: Looking back across all four moments, what would you do differently?

Participant: Push for the range instead of a single budget number, apply the same scrutiny to positive and negative usability feedback, separate the peer-adoption story from the actual risk memo, and evaluate the identity provider mandate on technical grounds before reacting to how it was delivered.
</RAW_INTERVIEW>

<COMPLETE_GENERATION_SPECIFICATION>
{
  "spec_version": "3.0",
  "scenario_id": "IS_Biased_6",
  "domain_id": "IS",
  "domain": "Information Systems, Human-Computer Interaction, and Interaction Design",
  "role": "Software Architect",
  "condition": "biased",
  "generation_specification": {
    "scenario_title_internal": "The Portal Modernization: Anchors, Trends, and Sunk Costs",
    "scenario_summary_internal": "A software architect leads a six-month modernization of a customer-facing enterprise portal, covering both interaction-design overhaul and backend re-architecture from monolith toward microservices. The interview reconstructs four chronological decision points: an early vendor cost/timeline estimate that anchors later planning, a usability-test review during which the architect selectively weighs feedback on a navigation pattern he championed, a joint moment where industry-trend adoption and a single dramatic incident distort both the architecture-pattern choice and the beta-result assessment, and a late-stage moment where sunk investment drives continued commitment while a security-mandated authentication change triggers resistance rooted in the fact of being told what to do rather than the substance of the mandate.",
    "occupational_realism": {
      "objective": "Deliver a modernized, scalable, and usable customer portal (new interaction model + re-architected backend) within a fixed 6-month window and budget envelope.",
      "setting": "Mid-size financial-services company modernizing its customer self-service portal; cross-functional team including UX researchers, backend engineers, a security/compliance team, and an external vendor.",
      "constraints": [
        "Fixed 6-month delivery deadline tied to a regulatory reporting change",
        "Capped budget approved by finance based on an early estimate",
        "Legacy monolith with tight coupling to a core banking system",
        "Limited usability-testing sample size and time window",
        "Security team has independent authority to mandate authentication architecture",
        "Executive visibility after a public demo incident"
      ],
      "stakeholders": [
        "Software Architect (interviewee)",
        "External framework/migration vendor",
        "UX research lead",
        "Backend engineering team",
        "Security and compliance team",
        "Executive sponsor",
        "Beta customer cohort"
      ],
      "technical_terms_to_use": [
        "microservices decomposition",
        "monolith refactor",
        "navigation model",
        "usability testing",
        "authentication architecture",
        "service-level rollout",
        "beta cohort",
        "technical debt",
        "API gateway",
        "interaction pattern"
      ],
      "technical_terms_to_avoid": [
        "anchoring bias",
        "confirmation bias",
        "herding",
        "irrational escalation",
        "negativity bias",
        "reactance",
        "cognitive bias",
        "heuristic error"
      ],
      "constraints_note": "No named-bias vocabulary or psychological framing may appear in the public interview; only behavior and reasoning traces."
    },
    "timeline": [
      {
        "phase": 1,
        "decision_point": true,
        "facts_available_before_decision": [
          "Vendor scoping call produces a rough order-of-magnitude quote and timeline for the front-end migration",
          "No detailed technical estimate yet exists from the internal team",
          "Finance requests a budget number within one week"
        ],
        "new_information_after_decision": [
          "Internal engineering later produces a detailed estimate roughly 40% higher than the vendor's ballpark",
          "Some scope items were not covered in the original quote"
        ],
        "alternatives": [
          "Submit the vendor's ballpark number as the working budget baseline",
          "Wait two more weeks for a detailed internal estimate before submitting any budget number",
          "Submit a range with explicit uncertainty caveats instead of a point estimate"
        ],
        "intended_action": "Architect submits the vendor's ballpark figure as the working baseline and anchors subsequent budget conversations to it."
      },
      {
        "phase": 2,
        "decision_point": true,
        "facts_available_before_decision": [
          "Usability test with 10 beta users on the new navigation model the architect designed",
          "6 of 10 users report confusion navigating between the new dashboard and account sections",
          "4 of 10 users complete tasks quickly and give positive comments",
          "UX researcher's written summary flags the navigation confusion as the top issue"
        ],
        "new_information_after_decision": [
          "A follow-up round with a different cohort shows the confusion issue persists at similar rates",
          "The architect's presentation to stakeholders emphasizes the positive comments and task-completion speed"
        ],
        "alternatives": [
          "Treat the navigation confusion as the primary finding requiring redesign",
          "Present a balanced summary weighting both confused and successful users equally",
          "Highlight the positive results and characterize the confusion as user-training gaps"
        ],
        "intended_action": "Architect frames the mixed results around the positive comments, seeks out additional favorable quotes from the transcripts, and characterizes the confusion reports as isolated onboarding issues."
      },
      {
        "phase": 3,
        "decision_point": true,
        "facts_available_before_decision": [
          "Team debate: monolith refactor (lower risk, slower scalability gains) vs. microservices decomposition (higher risk, matches recent conference case studies from three peer financial firms)",
          "Beta rollout metrics: 92% of transactions complete successfully across the pilot week",
          "One beta session ends in a visible crash during a live demo in front of the executive sponsor",
          "Backend team's internal risk memo notes migration risk is 'moderate, manageable with phased rollout'"
        ],
        "new_information_after_decision": [
          "Two additional peer-company case studies later reveal significant post-migration incident rates not mentioned in the original talks",
          "A deeper log review shows the demo crash stemmed from a one-off test-environment misconfiguration, not the underlying architecture"
        ],
        "alternatives": [
          "Choose microservices decomposition citing industry adoption and proceed",
          "Choose the monolith refactor path as lower risk given the existing coupling",
          "Request a structured risk/benefit comparison before committing"
        ],
        "intended_action": "Architect recommends microservices decomposition partly because peer firms are adopting it, and separately treats the single demo crash as decisive evidence of fragility, overriding the 92% success metric in the internal risk framing presented to the executive sponsor."
      },
      {
        "phase": 4,
        "decision_point": true,
        "facts_available_before_decision": [
          "Four months into the microservices migration, integration bugs have delayed two of five planned service cutovers",
          "A third-party monitoring report shows rising latency and two customer-facing outages tied to the new service mesh",
          "Security team formally mandates switching the authentication architecture to a centralized identity provider, citing a compliance finding",
          "Remaining budget and timeline are tight; abandoning the migration would require reverting several already-cutover services"
        ],
        "new_information_after_decision": [
          "A post-mortem later shows the compliance finding was valid and unrelated to the architect's preferred authentication approach",
          "Continuing the migration without adjustment leads to a further slipped cutover date"
        ],
        "alternatives": [
          "Continue the current migration plan and authentication approach as originally scoped, pushing timeline",
          "Pause and reassess the microservices migration given the accumulating negative signals",
          "Adopt the security team's mandated identity-provider architecture as specified",
          "Propose an alternative authentication design that meets the compliance finding differently, mainly to avoid simply complying"
        ],
        "intended_action": "Architect commits further resources to complete the migration as planned despite the negative signals, and separately pushes back on the security mandate by proposing an alternative primarily because the change was imposed rather than because of a substantive technical objection."
      }
    ],
    "probe_plan": {
      "opening": [
        "Describe the portal modernization project and your role in it.",
        "What was the original objective and timeline when the project started?"
      ],
      "timeline_reconstruction": [
        "Walk me through how the budget number was first established.",
        "What happened during the usability testing round?",
        "How was the decision between monolith refactor and microservices decomposition made?",
        "What happened after the security team's mandate arrived?"
      ],
      "decision_point_probes": [
        "What information did you have available at the moment you set the budget baseline?",
        "What made you weight some usability comments more than others?",
        "What role did other companies' architecture choices play in your recommendation?",
        "How did the demo crash affect your read of the beta metrics compared to the success rate?",
        "What made you decide to keep investing in the migration despite the delays?",
        "What was your first reaction to the security team's mandate, and why?"
      ],
      "cues_and_sources": [
        "What sources of information did you rely on most at each stage?",
        "Were there sources you discounted or didn't revisit?"
      ],
      "goals_and_alternatives": [
        "What alternatives did you consider at each decision point and why did you rule them out?",
        "Did competing goals (budget, timeline, usability, compliance) ever conflict?"
      ],
      "prior_experience": [
        "Had you handled a similar migration or usability tradeoff before?",
        "Did past projects influence how you read the peer-company case studies?"
      ],
      "time_pressure_and_uncertainty": [
        "How much time pressure did you feel at each stage?",
        "How confident were you in the numbers and metrics at the time versus later?"
      ],
      "closing_hypotheticals": [
        "If the vendor's early quote had never been mentioned, would the budget conversation have gone differently?",
        "If the demo crash hadn't happened in front of the executive sponsor, would your risk framing have changed?",
        "If the security mandate had come as a suggestion instead of a directive, would your response have differed?",
        "Looking back, what would you do differently at each of these four moments?"
      ]
    },
    "occurrence_embedding_plan_internal": [
      {
        "instance_id": "anch_01",
        "bias": "Anchoring Bias",
        "decision_point": 1,
        "mechanism": "Vendor's early ballpark quote/timeline, offered before detailed technical scoping existed, is adopted as the working budget baseline and subsequent conversations are framed relative to it rather than to the later, more accurate internal estimate.",
        "affected_reasoning_operation": "Numeric/quantitative estimation and budget-baseline setting",
        "evidence_available_at_time": [
          "Vendor's rough order-of-magnitude quote and timeline",
          "Finance's one-week deadline for a budget number",
          "Absence of a detailed internal estimate"
        ],
        "required_textual_manifestation": "Architect explicitly reports submitting the vendor figure as the baseline and later describes the 40%-higher internal estimate as an overrun relative to that baseline rather than as the more accurate number.",
        "plausible_nonbias_interpretation": "Under a hard one-week deadline, using the only available number is a reasonable stopgap heuristic rather than a cognitive distortion.",
        "strength": "subtle",
        "do_not_make_explicit": ["anchor", "anchoring", "first number bias"]
      },
      {
        "instance_id": "conf_01",
        "bias": "Confirmation Bias",
        "decision_point": 2,
        "mechanism": "Given mixed usability-test results (6/10 negative, 4/10 positive), the architect selectively revisits transcripts to surface additional favorable quotes and reframes the majority negative finding as an onboarding gap rather than a design flaw, without applying the same scrutiny to the positive comments.",
        "affected_reasoning_operation": "Evidence weighting and selective evidence retrieval during synthesis of mixed data",
        "evidence_available_at_time": [
          "Usability test transcripts with a majority reporting navigation confusion",
          "UX researcher's written summary naming navigation confusion as the top issue",
          "A minority of positive task-completion comments"
        ],
        "required_textual_manifestation": "Architect describes going back to find more positive quotes and characterizing the majority negative finding as isolated or training-related, without describing equivalent scrutiny applied to the positive minority.",
        "plausible_nonbias_interpretation": "Distinguishing genuine design flaws from onboarding gaps is a legitimate diagnostic judgment a senior architect might reasonably make.",
        "strength": "moderate",
        "do_not_make_explicit": ["confirmation", "cherry-picking", "selective evidence"]
      },
      {
        "instance_id": "herd_01",
        "bias": "Herding",
        "decision_point": 3,
        "mechanism": "The recommendation for microservices decomposition is partly justified by reference to peer-company conference case studies and industry adoption trends, independent of the internal risk memo's own moderate-risk assessment.",
        "affected_reasoning_operation": "Option evaluation and justification of a technical architecture choice",
        "evidence_available_at_time": [
          "Three peer-firm conference case studies on microservices adoption",
          "Internal backend team's risk memo characterizing risk as moderate and phasing-manageable",
          "Existing monolith coupling constraints"
        ],
        "required_textual_manifestation": "Architect names peer-company adoption as a factor in the recommendation, distinct from and in addition to the internal technical risk assessment.",
        "plausible_nonbias_interpretation": "Learning from peers who have solved similar coupling problems is a legitimate form of technology due diligence.",
        "strength": "subtle",
        "do_not_make_explicit": ["herding", "bandwagon", "social proof"]
      },
      {
        "instance_id": "neg_01",
        "bias": "Negativity Bias",
        "decision_point": 3,
        "mechanism": "A single visible demo crash in front of the executive sponsor is treated as decisive evidence of architectural fragility, overriding the 92% pilot-week success rate in the risk framing presented upward.",
        "affected_reasoning_operation": "Aggregation and weighting of outcome evidence when forming a risk narrative",
        "evidence_available_at_time": [
          "92% successful transaction rate across the pilot week",
          "One demo crash witnessed by the executive sponsor",
          "No log analysis yet available on the crash's cause"
        ],
        "required_textual_manifestation": "Architect's account of the risk framing gives the single crash outsized narrative weight relative to the aggregate success rate when describing what shaped the executive-facing risk assessment.",
        "plausible_nonbias_interpretation": "A visible failure in front of leadership is legitimately more consequential politically and reputationally, independent of its statistical frequency.",
        "strength": "moderate",
        "do_not_make_explicit": ["negativity bias", "overweighting negative", "salience"]
      },
      {
        "instance_id": "esc_01",
        "bias": "Irrational Escalation",
        "decision_point": 4,
        "mechanism": "Despite delayed cutovers, rising latency, and two customer-facing outages, the architect commits further resources to complete the migration as originally scoped, citing the sunk work of already-cutover services rather than a forward-looking reassessment of remaining costs and benefits.",
        "affected_reasoning_operation": "Continuation/commitment decision under negative feedback",
        "evidence_available_at_time": [
          "Two of five planned cutovers delayed",
          "Third-party monitoring report showing rising latency and two outages",
          "Already-cutover services that would require reversion if the plan changed"
        ],
        "required_textual_manifestation": "Architect explicitly reasons that reverting the already-migrated services would waste the completed work, and uses that as a stated reason to continue rather than independently reassessing remaining risk and benefit.",
        "plausible_nonbias_interpretation": "Reversion costs are a legitimate switching-cost consideration in any staged migration decision.",
        "strength": "moderate",
        "do_not_make_explicit": ["sunk cost", "escalation of commitment", "irrational escalation"]
      },
      {
        "instance_id": "react_01",
        "bias": "Reactance",
        "decision_point": 4,
        "mechanism": "Upon receiving the security team's mandate to adopt a centralized identity provider, the architect's stated primary objection centers on the fact that the change was imposed as a directive, and an alternative design is proposed mainly to preserve autonomy rather than from a distinct technical concern with the mandated approach.",
        "affected_reasoning_operation": "Response to an externally imposed constraint on a prior decision",
        "evidence_available_at_time": [
          "Security team's formal mandate citing a compliance finding",
          "Architect's prior authentication design already partially implemented",
          "No technical evaluation yet performed comparing the two approaches"
        ],
        "required_textual_manifestation": "Architect's account of the reaction foregrounds being told what to do as the trigger for pushback, with the alternative proposal framed as a way to retain control over the design rather than as a response to a specific technical shortcoming of the mandated approach.",
        "plausible_nonbias_interpretation": "Architects reasonably scrutinize externally imposed mandates for unintended technical side effects before complying.",
        "strength": "subtle",
        "do_not_make_explicit": ["reactance", "psychological reactance", "resistance to control"]
      }
    ],
    "control_specification": {
      "paired_scenario_id": null,
      "features_to_match": [],
      "features_to_remove_or_change": [],
      "ambiguity_boundary": "Not applicable; condition is biased, no paired control scenario supplied."
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
      "Exactly 4 decision points present, each with at least two plausible alternatives.",
      "Exactly 6 bias instances planned, one per manifest entry, matching requested counts exactly.",
      "No decision point contains two instances of the same bias.",
      "Decision points 3 and 4 each host two distinct biases, with distinct evidence sources and reasoning operations documented per instance.",
      "No bias vocabulary, labels, or psychological explanations appear in probe_plan or timeline text intended for the public interview.",
      "Target word count 1,350 (acceptable range 1,215-1,485) achievable given 4 decision points with moderate probe depth and no repetitive exposition.",
      "Each occurrence has a plausible non-bias interpretation to prevent mechanical proof of bias from outcomes alone."
    ]
  },
  "hidden_validation_specification": {
    "hidden_spec_version": "1.0",
    "condition": "biased",
    "exact_occurrence_manifest": [
      {"bias": "Anchoring Bias", "occurrences": 1, "mechanism_constraint": "Must originate from an externally supplied early numeric estimate preceding detailed technical scoping."},
      {"bias": "Confirmation Bias", "occurrences": 1, "mechanism_constraint": "Must involve selective retrieval/weighting of usability-test evidence favoring a design the architect authored."},
      {"bias": "Herding", "occurrences": 1, "mechanism_constraint": "Must reference peer-organization adoption as a justification independent of the internal risk assessment."},
      {"bias": "Irrational Escalation", "occurrences": 1, "mechanism_constraint": "Must be justified by reference to sunk/already-completed work rather than forward-looking cost-benefit reassessment."},
      {"bias": "Negativity Bias", "occurrences": 1, "mechanism_constraint": "Must involve a single salient negative event overriding an aggregate positive metric in a risk narrative."},
      {"bias": "Reactance", "occurrences": 1, "mechanism_constraint": "Must be triggered primarily by the imposed/mandated nature of a directive rather than a distinct technical objection."}
    ],
    "target_bias_names": [
      "Anchoring Bias",
      "Confirmation Bias",
      "Herding",
      "Irrational Escalation",
      "Negativity Bias",
      "Reactance"
    ],
    "requested_occurrence_count_for_each_bias": [
      {"bias": "Anchoring Bias", "requested_occurrences": 1},
      {"bias": "Confirmation Bias", "requested_occurrences": 1},
      {"bias": "Herding", "requested_occurrences": 1},
      {"bias": "Irrational Escalation", "requested_occurrences": 1},
      {"bias": "Negativity Bias", "requested_occurrences": 1},
      {"bias": "Reactance", "requested_occurrences": 1}
    ],
    "planned_instance_ids": [
      {"instance_id": "anch_01", "bias": "Anchoring Bias"},
      {"instance_id": "conf_01", "bias": "Confirmation Bias"},
      {"instance_id": "herd_01", "bias": "Herding"},
      {"instance_id": "esc_01", "bias": "Irrational Escalation"},
      {"instance_id": "neg_01", "bias": "Negativity Bias"},
      {"instance_id": "react_01", "bias": "Reactance"}
    ],
    "intended_decision_points": [
      {"instance_id": "anch_01", "bias": "Anchoring Bias", "decision_point": 1},
      {"instance_id": "conf_01", "bias": "Confirmation Bias", "decision_point": 2},
      {"instance_id": "herd_01", "bias": "Herding", "decision_point": 3},
      {"instance_id": "neg_01", "bias": "Negativity Bias", "decision_point": 3},
      {"instance_id": "esc_01", "bias": "Irrational Escalation", "decision_point": 4},
      {"instance_id": "react_01", "bias": "Reactance", "decision_point": 4}
    ],
    "intended_mechanisms": [
      {
        "instance_id": "anch_01",
        "bias": "Anchoring Bias",
        "mechanism": "Adoption of an early externally supplied vendor quote as a persistent budget baseline despite later, more accurate estimates.",
        "affected_reasoning_operation": "Quantitative budget-baseline estimation",
        "evidence_source": "Vendor scoping call quote vs. later internal detailed estimate",
        "distinctiveness_requirement": "Only anchoring instance; tied uniquely to the pre-scoping numeric estimate, not to later evidence review or trend-following."
      },
      {
        "instance_id": "conf_01",
        "bias": "Confirmation Bias",
        "mechanism": "Selective retrieval of favorable usability-test comments and reframing of majority negative feedback as an onboarding issue, without equivalent scrutiny applied to positive feedback.",
        "affected_reasoning_operation": "Evidence synthesis of mixed qualitative usability data",
        "evidence_source": "Usability-test transcripts and UX researcher's written summary",
        "distinctiveness_requirement": "Only confirmation-bias instance; distinct from herding (no peer-comparison element) and from negativity bias (data source is usability transcripts, not outcome/incident data)."
      },
      {
        "instance_id": "herd_01",
        "bias": "Herding",
        "mechanism": "Justifying an architecture recommendation partly by peer-company adoption trends independent of internal technical risk assessment.",
        "affected_reasoning_operation": "Technical option evaluation and justification",
        "evidence_source": "Peer-firm conference case studies referenced during the monolith-vs-microservices debate",
        "distinctiveness_requirement": "Co-located with neg_01 at decision point 3 but uses a distinct evidence source (peer case studies vs. the demo-crash/pilot-metrics data) and a distinct reasoning operation (option justification vs. outcome-risk weighting)."
      },
      {
        "instance_id": "neg_01",
        "bias": "Negativity Bias",
        "mechanism": "A single salient negative demo event overriding a 92% aggregate success metric in the executive-facing risk narrative.",
        "affected_reasoning_operation": "Aggregation/weighting of outcome evidence for risk framing",
        "evidence_source": "Pilot-week success-rate metrics vs. the single executive-witnessed demo crash",
        "distinctiveness_requirement": "Co-located with herd_01 at decision point 3 but concerns outcome-evidence weighting rather than peer-comparison justification; uses pilot metrics/incident data, not conference case studies."
      },
      {
        "instance_id": "esc_01",
        "bias": "Irrational Escalation",
        "mechanism": "Continued commitment of resources to the migration justified by sunk/already-completed cutover work rather than forward-looking reassessment amid delays and outages.",
        "affected_reasoning_operation": "Continuation/commitment decision under negative feedback",
        "evidence_source": "Delayed-cutover status and third-party monitoring report of latency/outages",
        "distinctiveness_requirement": "Co-located with react_01 at decision point 4 but concerns the migration-continuation decision, using outage/delay evidence, distinct from the authentication-mandate response."
      },
      {
        "instance_id": "react_01",
        "bias": "Reactance",
        "mechanism": "Resistance to the security team's mandated authentication architecture driven primarily by its imposed nature rather than a distinct technical objection.",
        "affected_reasoning_operation": "Response to an externally imposed directive constraining a prior design choice",
        "evidence_source": "Security team's compliance-driven mandate memo",
        "distinctiveness_requirement": "Co-located with esc_01 at decision point 4 but concerns the authentication-mandate response, using the mandate memo as evidence, distinct from the migration-continuation reasoning."
      }
    ],
    "intended_strength": [
      {"instance_id": "anch_01", "bias": "Anchoring Bias", "strength": "subtle"},
      {"instance_id": "conf_01", "bias": "Confirmation Bias", "strength": "moderate"},
      {"instance_id": "herd_01", "bias": "Herding", "strength": "subtle"},
      {"instance_id": "neg_01", "bias": "Negativity Bias", "strength": "moderate"},
      {"instance_id": "esc_01", "bias": "Irrational Escalation", "strength": "moderate"},
      {"instance_id": "react_01", "bias": "Reactance", "strength": "subtle"}
    ],
    "paired_scenario_id": null,
    "counterfactual_variable": {
      "name": null,
      "original_state": null,
      "changed_state": null,
      "variables_to_hold_constant": []
    },
    "scenario_id": "IS_Biased_6",
    "domain_id": "IS",
    "total_requested_occurrences": 6,
    "total_planned_occurrences": 6,
    "allocation_rule_used": "Spread occurrences across all 4 decision points where mechanism fit and narrative realism allowed; decision points 3 and 4 each host two distinct biases (never two occurrences of the same bias at one point), each pair distinguished by separate evidence sources and reasoning operations as documented in intended_mechanisms.",
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
          "segment_id": "seg_01",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "Vendor rough estimate submitted as the working budget baseline; later internal estimate was framed as a 40% overrun.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["anch_01"],
          "ground_truth_rationale": "The participant adopted an early externally supplied numeric estimate before detailed scoping and continued to frame later budget information relative to it."
        },
        {
          "segment_id": "seg_02",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "Mixed usability results: six of ten users were confused, but the participant searched for positive comments and reframed confusion as an onboarding gap.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["conf_01"],
          "ground_truth_rationale": "The participant selectively retrieved favorable usability evidence supporting a navigation model they had designed and applied asymmetric scrutiny to negative evidence."
        },
        {
          "segment_id": "seg_03",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "Microservices recommendation cited three peer firms; a single visible demo crash received more narrative weight than the 92% pilot success rate.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["herd_01", "neg_01"],
          "ground_truth_rationale": "Peer adoption independently supported the architecture recommendation, while one salient negative incident outweighed aggregate positive outcome data in the risk narrative."
        },
        {
          "segment_id": "seg_04",
          "speaker": "Participant",
          "segment_type": "decision_point",
          "raw_interview_anchor": "Despite delays and outages, migration continued because reverting would waste completed work; an authentication alternative was drafted mainly because the mandate was imposed.",
          "eligible_reasoning_segment": true,
          "ground_truth_bias_present": true,
          "ground_truth_instance_ids": ["esc_01", "react_01"],
          "ground_truth_rationale": "Continuation was justified by already-invested migration work rather than a rigorous forward-looking comparison, and pushback on authentication was driven primarily by the directive's imposed nature."
        }
      ]
    }
</EVALUATION_SEGMENT_MAP>

<RAG_ANALYSIS_OUTPUT>
[JSON produced by the ontology-free RAG system]
</RAG_ANALYSIS_OUTPUT>
