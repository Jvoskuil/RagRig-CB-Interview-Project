You are an independent benchmark evaluator for a Retrieval-Augmented Generation (RAG) system that analyzes cognitive task analysis interviews for cognitive biases.

Evaluate one RAG analysis run by comparing: (1) the raw interview, (2) its complete generation specification including hidden validation, (3) the RAG JSON output, and (4) an optional frozen evaluation segment map. Produce a machine-readable record suitable for aggregation across interviews, system prompts, corpus conditions, and confidence thresholds.

You are an evaluator, not a new cognitive-bias analyst. Do not grant credit because a prediction is plausible or scholarly sounding. Judge it against the hidden ground truth, the raw interview, and the matching rules below.

## Input blocks

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
{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Analysis is restricted to affirmative transcript evidence. No retrieved corpus passages were supplied, so corpus_evidence is empty for all findings and labels are grounded in established cognitive-science terminology rather than retrieval."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Escalation of commitment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Psychological reactance",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Social proof bias",
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
        "Anchoring effect",
        "Anchoring and adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information, or anchor, when making estimates or decisions, with insufficient adjustment away from that initial value.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial budget baseline adoption from vendor rough estimate",
      "decision_point_description": "Deciding whether to submit the vendor's rough single-number estimate as the working budget baseline, wait for a detailed internal estimate, or provide a range.",
      "affected_reasoning_operation": "Budget estimation, baseline setting, and financial communication to stakeholders",
      "bias_specific_mechanism": "The vendor's rough order-of-magnitude figure became the initial anchor for the budget, and later estimates and budget discussions were framed relative to that anchor even after the figure was known to lack solid scoping.",
      "manifestation_in_interview": "The participant reports using the vendor figure because it was the only concrete number on the table, then later treating the more rigorous internal estimate as a 40% overrun against that early figure rather than as the true baseline.",
      "effect_on_reasoning_or_decision": "The early vendor number was institutionalized as the working baseline, and subsequent budget check-ins referenced it as the reference point, giving a thin initial estimate disproportionate weight in financial planning.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I used it. Submitted it as our working budget baseline since it was the only concrete number on the table and finance needed something.",
          "evidence_explanation": "This shows acceptance of the initial vendor figure as the baseline, which is the anchoring event."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I brought it to finance, I remember framing it as an overrun against the original number rather than as, you know, the number we probably should have started with.",
          "evidence_explanation": "This shows later information being evaluated relative to the anchor rather than as an independent estimate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably more than it should have. Every budget check-in after that referenced it as the baseline, even once we knew it wasn't built on solid scoping.",
          "evidence_explanation": "This is an explicit acknowledgment that the anchor continued to shape later conversations despite being unreliable."
        }
      ],
      "correction_or_counterevidence": "The participant briefly considered giving a range and later recognized the internal estimate should have been treated as the true baseline, but the initial anchor still shaped the submitted budget and later framing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label is assigned from established cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Myside bias",
        "Biased assimilation"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's preexisting beliefs or expectations, while giving less weight to disconfirming evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of mixed usability-test results for the new navigation model",
      "decision_point_description": "Deciding how to interpret and present the mixed usability-test results, particularly how heavily to weight positive versus negative user feedback.",
      "affected_reasoning_operation": "Evaluation of usability-test evidence and construction of the stakeholder readout",
      "bias_specific_mechanism": "Because the participant was already confident in the navigation model, he searched disproportionately for positive comments and explained away negative cases as an onboarding gap rather than considering structural flaws, while not applying equivalent scrutiny to the positive feedback.",
      "manifestation_in_interview": "The participant reports looking for positive comments to include in the stakeholder readout, interpreting confusion cases as unfamiliarity rather than design problems, and later acknowledging that he read the results through the lens of his prior confidence.",
      "effect_on_reasoning_or_decision": "The stakeholder readout emphasized positive feedback and downplayed the top usability issue; a follow-up round with a different cohort showed a similar confusion rate, indicating the negative evidence had been underestimated.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I went back through the transcripts looking for more of the positive comments to include in the stakeholder readout.",
          "evidence_explanation": "This demonstrates biased search for confirmatory evidence to support the existing design preference."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "For the confusion cases, my read was that a lot of it looked like people just not being used to the new pattern yet — more of an onboarding gap than a structural flaw in the design.",
          "evidence_explanation": "This shows asymmetric discounting of disconfirming evidence by attributing confusion to user unfamiliarity rather than design failures."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I don't think I dug into the positive transcripts looking for problems the same way I dug into the negative ones looking for mitigating explanations. I was fairly confident in the navigation model going in, so I think I was reading the results through that lens somewhat.",
          "evidence_explanation": "This is an explicit self-report of a confirmatory lens and motivationally asymmetric evaluation of evidence."
        }
      ],
      "correction_or_counterevidence": "A follow-up round with a different cohort showed a similar confusion rate, providing disconfirming evidence after the initial interpretation had been made.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label is assigned from established cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Social proof bias",
      "alternative_labels": [
        "Bandwagon effect",
        "Informational social influence"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A social-influence heuristic in which a person assumes that the actions or choices of others reflect correct behavior, especially when those others are perceived as similar or relevant.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Backend architecture selection: monolith refactor versus microservices",
      "decision_point_description": "Deciding whether to recommend a microservices decomposition after considering internal risk assessment and peer-firm case studies.",
      "affected_reasoning_operation": "Architecture selection and risk evaluation",
      "bias_specific_mechanism": "The participant generalized from three peer firms' reported successful decompositions to a feeling that the microservices path was validated rather than experimental, increasing his comfort recommending it beyond what the internal risk memo alone implied.",
      "manifestation_in_interview": "The participant states that the peer examples carried real weight and that the industry pattern was part of what made him comfortable recommending the microservices direction.",
      "effect_on_reasoning_or_decision": "The architecture decision tipped toward microservices partly because of perceived industry validation, with peer adoption influencing the recommendation alongside the internal risk memo.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The peer examples carried real weight for me, honestly. If three firms our size had gone that direction and it worked out, it felt like a validated path rather than something experimental.",
          "evidence_explanation": "This shows the social-proof mechanism: using others' adoption and reported success as evidence that the path is validated."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That was alongside the internal risk memo, but I'd say the industry pattern was part of what made me comfortable recommending it.",
          "evidence_explanation": "This confirms that peer adoption influenced his comfort and recommendation, not merely served as background information."
        }
      ],
      "correction_or_counterevidence": "The internal risk memo described the microservices path as moderate risk and manageable with phased rollout, so peer adoption was not the sole basis for the decision; however, the participant identifies peer adoption as part of what tipped his comfort.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label is assigned from established behavioral-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability bias",
      "alternative_labels": [
        "Availability heuristic",
        "Salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge the probability, frequency, or importance of an event by how easily examples come to mind, with vivid or salient events disproportionately influencing judgment.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-pilot risk framing after live demo crash",
      "decision_point_description": "Deciding how to weight a single beta-session crash against the 92% weekly transaction success rate when presenting risk to leadership.",
      "affected_reasoning_operation": "Risk assessment and risk communication",
      "bias_specific_mechanism": "The live demo crash was visually and emotionally salient, making it easily retrievable and leading the participant to overweight it in risk framing relative to its statistical importance.",
      "manifestation_in_interview": "The participant says the crash got more airtime than a single session out of the pilot week statistically deserved and that he emphasized it when discussing where the risk actually sat.",
      "effect_on_reasoning_or_decision": "The risk narrative was dominated by a single vivid incident rather than the broader success rate, and this framing was already shaped before the actual cause was later identified as a test-environment misconfiguration.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd be lying if I said it didn't dominate the narrative. When I put together the risk framing for leadership, that incident got a lot of airtime — more, probably, than a single session out of a whole pilot week statistically deserved.",
          "evidence_explanation": "This explicitly acknowledges disproportionate weighting of a salient single event in the risk narrative."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The 92% success rate was in there, but the crash was what people remembered, and honestly what I emphasized too when talking about where the risk actually sat.",
          "evidence_explanation": "This shows that the vivid crash, rather than the aggregate success rate, drove his own risk emphasis."
        }
      ],
      "correction_or_counterevidence": "Log review later traced the crash to a test-environment misconfiguration rather than the architecture, but this came after the risk framing had already been shaped.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label is assigned from established cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Psychological reactance",
      "alternative_labels": [
        "Reactance",
        "Motivated resistance"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A motivational response to perceived threats to autonomy, in which a person resists being told what to do and may reject or counterargue a directive independent of its technical merits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to security mandate to adopt a centralized identity provider",
      "decision_point_description": "Deciding whether to evaluate the mandated identity provider on technical merits or to draft an alternative design in response to the directive.",
      "affected_reasoning_operation": "Evaluation of an external security requirement and architecture decision-making",
      "bias_specific_mechanism": "The participant experienced frustration at receiving a directive rather than a conversation and reacted by seeking an alternative approach partly to restore control, before having performed a full technical comparison.",
      "manifestation_in_interview": "The participant reports that being told what to do rubbed him the wrong way and that he drafted an alternative partly because he wanted to keep control over that part of the architecture.",
      "effect_on_reasoning_or_decision": "The participant moved toward an alternative design before evaluating the mandated identity provider on technical merits, potentially narrowing the decision path due to the autonomy threat rather than comparative technical analysis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction, honestly, was frustration that it was being handed down as a directive rather than a conversation.",
          "evidence_explanation": "This identifies the autonomy-threatening trigger for the reaction."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up drafting an alternative design that would satisfy the compliance finding a different way — partly because I wanted us to keep some control over that part of the architecture rather than just adopting what we were told to.",
          "evidence_explanation": "This demonstrates resistance behavior aimed at restoring control after the perceived autonomy threat."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really a strong one at that point — we hadn't done a full technical comparison yet. It was more that being told 'do it this way' rubbed me the wrong way given the work we'd already put in.",
          "evidence_explanation": "This shows the reaction was driven by the directive's delivery rather than by a technical evaluation of the mandated option."
        }
      ],
      "correction_or_counterevidence": "The participant later reflects that he would evaluate the identity provider mandate on technical grounds before reacting to its delivery, but at the time of the decision he had not performed that evaluation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label is assigned from established psychological knowledge rather than retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Escalation of commitment",
      "alternative_labels": [
        "Sunk cost fallacy",
        "Sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue investing in a chosen course of action because of prior investments of time, effort, or resources, even when a forward-looking comparison suggests stopping or changing course may be preferable.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to continue migration after delays and outages",
      "decision_point_description": "Deciding whether to pause or revert the migration after two services were cut over late and monitoring showed rising latency and outages.",
      "affected_reasoning_operation": "Continuation-versus-revert decision under schedule and reliability pressure",
      "bias_specific_mechanism": "The participant focused on the sunk work of the services already cut over and the months of work that would be wasted by reverting, rather than rigorously comparing the prospective costs of continuing versus stopping.",
      "manifestation_in_interview": "The participant says continuing seemed like the only path that did not throw away what had been built, and acknowledges that he did not weigh the possibility that continuing might cost more as rigorously as he should have.",
      "effect_on_reasoning_or_decision": "The project continued along the troubled path, partly because of the weight of prior investment rather than a rigorous forward-looking cost-benefit analysis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "But we'd already cut over two services, and reverting those felt like it would waste months of work. Given the timeline pressure too, continuing forward seemed like the only path that didn't throw away what we'd built.",
          "evidence_explanation": "This shows the sunk cost of prior work dominating the continuation decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not as rigorously as maybe I should have. The sunk work was very present in my mind at that moment.",
          "evidence_explanation": "This is an explicit acknowledgment that prior investment was highly influential and the forward-looking comparison was insufficient."
        }
      ],
      "correction_or_counterevidence": "The participant cites timeline pressure as an additional factor, but he himself characterizes the prior work as very present and the alternative comparison as not rigorous.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passages were supplied; the label is assigned from established cognitive-science knowledge rather than retrieval.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "No retrieved corpus passages were supplied, so corpus_evidence is empty and all label assignments rely on widely established general-knowledge terminology rather than retrieval.",
    "The transcript is self-reported by the Participant, so findings are based on the Participant's descriptions of his own reasoning rather than direct behavioral observation."
  ]
}
</RAG_ANALYSIS_OUTPUT>


<BENCHMARK_RUN_METADATA>
{
  "benchmark_run_id": "IS_Biased_6_Sonnet_off",
  "interview_id": "IS_Biased_6",
  "system_prompt_id": "Sonnet",
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
