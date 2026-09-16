# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific project experience, it'll be recorded for research purposes, and you can skip anything you'd rather not discuss. Sound okay? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me a bit about your role and the project we're discussing? Participant: Sure. I'm the software architect on our customer portal modernization. We were rebuilding the self-service portal for retail banking customers — new interaction design, plus re-architecting the backend off a fairly old monolith. I owned the technical direction end to end, working with a UX researcher, our backend team, security and compliance, and an external vendor who helped with the front-end migration. Interviewer: What was the objective when the project kicked off? Participant: We had a hard deadline — six months — tied to a regulatory reporting change, so the date wasn't negotiable. The goal was a portal that was both more usable and could scale better, since the existing system was tightly coupled to our core banking platform and every change took forever to ship. Interviewer: Walk me through how the project actually unfolded, from your perspective. Participant: It started with scoping. We brought in a vendor to help estimate the front-end migration piece, since we didn't have deep in-house experience with the newer framework we wanted to use. Around the same time, we kicked off early usability testing on a new navigation model I'd designed — basically restructuring how customers move between the dashboard and their account details. That ran in parallel with an architecture debate on the backend: whether to do a more conservative monolith refactor or go further and decompose into microservices. That decision took a few weeks and involved looking at what similar firms had done. Once we picked a direction, we moved into execution, and about four months in we hit some turbulence — delays, a couple of outages, and separately, a mandate from security to change our authentication approach. That's roughly the shape of it. Interviewer: Let's go back to the very beginning — the budget number. What happened there? Participant: Finance needed a number within about a week to lock the budget, and we didn't have a detailed internal estimate yet — that takes real engineering time to build properly. So we did a scoping call with the vendor, and they gave us a rough order-of-magnitude figure for the migration, both cost and timeline. Interviewer: What did you do with that figure? Participant: I used it. Submitted it as our working budget baseline since it was the only concrete number on the table and finance needed something. Interviewer: Did you consider other options — waiting, or giving a range instead? Participant: We could have waited two more weeks for a real internal estimate, or given a range with caveats. I thought about the range option, actually, but figured a single number would be easier for finance to plan around, and the vendor had done similar migrations before, so it seemed like a reasonable placeholder. Interviewer: What happened once the internal team produced their own estimate? Participant: It came in about 40% higher. Some scope items the vendor hadn't accounted for — data migration edge cases, mostly. When I brought it to finance, I remember framing it as an overrun against the original number rather than as, you know, the number we probably should have started with. It became this whole conversation about why we were 40% over, when really the vendor's figure was just thin to begin with. Interviewer: Looking back, how much weight do you think that early vendor number carried in later conversations? Participant: Probably more than it should have. Every budget check-in after that referenced it as the baseline, even once we knew it wasn't built on solid scoping. Interviewer: Let's move to the usability testing. What did that process look like? Participant: We ran a round with ten beta users on the new navigation model. Results were mixed — six of ten had trouble moving between the dashboard and account sections, four completed tasks quickly and gave positive feedback. Our UX researcher's write-up flagged the navigation confusion as the top issue. Interviewer: How did you interpret that split? Participant: Honestly, I went back through the transcripts looking for more of the positive comments to include in the stakeholder readout. The four successful users had some pretty specific praise for the new layout, and I wanted that represented well. For the confusion cases, my read was that a lot of it looked like people just not being used to the new pattern yet — more of an onboarding gap than a structural flaw in the design. Interviewer: Did you apply the same level of scrutiny to the positive responses as the negative ones? Participant: That's a fair question. I don't think I dug into the positive transcripts looking for problems the same way I dug into the negative ones looking for mitigating explanations. I was fairly confident in the navigation model going in, so I think I was reading the results through that lens somewhat. Interviewer: What did the follow-up round show? Participant: Similar confusion rate with a different cohort. So it wasn't a one-off. Interviewer: Now, the architecture decision — monolith refactor versus microservices. How did that get resolved? Participant: That one took real debate. Monolith refactor was lower risk but wouldn't buy us much scalability. Microservices was a bigger lift but matched what we'd seen at a few peer firms — three other financial companies had presented case studies on similar decompositions at a conference a few months earlier. Our own backend risk memo called the microservices path 'moderate risk, manageable with phased rollout.' Interviewer: What tipped the decision toward microservices? Participant: The peer examples carried real weight for me, honestly. If three firms our size had gone that direction and it worked out, it felt like a validated path rather than something experimental. That was alongside the internal risk memo, but I'd say the industry pattern was part of what made me comfortable recommending it. Interviewer: Around that time there was also a demo incident. Can you describe that? Participant: Yeah — during a live demo for the executive sponsor, one beta session crashed. Visible, in the room, bad timing. That was against a backdrop of pretty strong pilot metrics otherwise — 92% of transactions completing successfully that week. Interviewer: How did that crash factor into the risk assessment you presented afterward? Participant: I'd be lying if I said it didn't dominate the narrative. When I put together the risk framing for leadership, that incident got a lot of airtime — more, probably, than a single session out of a whole pilot week statistically deserved. The 92% success rate was in there, but the crash was what people remembered, and honestly what I emphasized too when talking about where the risk actually sat. Interviewer: Did you know at that point what caused the crash? Participant: Not yet. Log review came later and traced it to a test-environment misconfiguration, not the architecture itself. But that came after the risk framing had already been shaped. Interviewer: Let's get to four months in. What was happening then? Participant: We'd cut over two of five planned services, both later than planned, integration bugs slowing things down. A monitoring report showed rising latency and two customer-facing outages tied to the new service mesh. On top of that, security formally mandated we switch to a centralized identity provider for authentication, citing a compliance finding. Interviewer: What was your reaction to the mandate? Participant: My first reaction, honestly, was frustration that it was being handed down as a directive rather than a conversation. We'd already built out our own authentication approach and gotten it partway implemented. I ended up drafting an alternative design that would satisfy the compliance finding a different way — partly because I wanted us to keep some control over that part of the architecture rather than just adopting what we were told to. Interviewer: Did you have a specific technical concern with the mandated identity provider itself? Participant: Not really a strong one at that point — we hadn't done a full technical comparison yet. It was more that being told 'do it this way' rubbed me the wrong way given the work we'd already put in. Interviewer: And the decision to keep going with the migration despite the delays and outages? Participant: We talked about pausing. But we'd already cut over two services, and reverting those felt like it would waste months of work. Given the timeline pressure too, continuing forward seemed like the only path that didn't throw away what we'd built. Interviewer: Did you weigh that against the possibility that continuing might cost more than stopping? Participant: Not as rigorously as maybe I should have. The sunk work was very present in my mind at that moment. Interviewer: If the vendor's early number had never come up, do you think the budget conversation would have gone differently? Participant: Probably. Without an anchor point, finance might have pushed harder for the detailed estimate up front instead of accepting a placeholder. Interviewer: If the demo crash hadn't happened in front of the executive sponsor, would your risk framing have looked different? Participant: Almost certainly. I think the 92% number would have carried more weight in isolation. Interviewer: If the security mandate had come as a suggestion rather than a directive, would your response have changed? Participant: I think so. I might have approached the comparison more on the merits rather than looking for an alternative right away. Interviewer: Looking back across all four moments, what would you do differently? Participant: Push for the range instead of a single budget number, apply the same scrutiny to positive and negative usability feedback, separate the peer-adoption story from the actual risk memo, and evaluate the identity provider mandate on technical grounds before reacting to how it was delivered.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.85s · gen 130.70s · total 136.5s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0220 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0220 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0220 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0201 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
5. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0195 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
6. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0190 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0189 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0181 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
11. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0176 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
13. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
14. **Hallihan_etal_DTM_12.pdf** — 0.0169 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
15. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0168 (rrf) — _# Cognitive Biases in Technical Communication We are surrounded by stimuli. The new experiences _
16. **ijcma-08-2012-0064.pdf** — 0.0168 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
17. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0166 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
18. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
21. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
22. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
23. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0161 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
24. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0160 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
25. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
27. **ijcma-08-2012-0064.pdf** — 0.0156 (rrf) — _# 382 I used this with a man and woman team, both of whom I knew didn’t care for each other busi_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0154 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0153 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0152 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
32. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0151 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
35. **Hallihan_etal_DTM_12.pdf** — 0.0148 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
36. **ijcma-08-2012-0064.pdf** — 0.0148 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
37. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0146 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
39. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0145 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
40. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
41. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0144 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
42. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
43. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
45. **Hallihan_etal_DTM_12.pdf** — 0.0142 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
46. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0141 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
47. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
48. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0138 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
49. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0138 (rrf) — _# Cognitive Biases in Technical Communication | | journey? Where do we place rewards in that jou_
50. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0138 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated the interview transcript for affirmatively demonstrated cognitive biases, using retrieved literature for support where available and applying conservative diagnostic thresholds; candidate patterns were separated from identified occurrences."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Psychological reactance",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Sunk cost fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring-and-adjustment heuristic",
        "Anchoring effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information, or anchor, and make insufficient adjustments away from it in subsequent judgments or estimates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial budget baseline adoption",
      "decision_point_description": "Selecting a working budget number to submit to finance under time pressure",
      "affected_reasoning_operation": "Numerical estimation and baseline framing",
      "bias_specific_mechanism": "The vendor's rough order-of-magnitude figure became the initial reference point for the project budget. Later internal estimates and financial discussions were interpreted relative to that anchor, with insufficient adjustment for the vendor figure's lower reliability.",
      "manifestation_in_interview": "The participant accepted the vendor figure as the working budget baseline, then framed the later internal estimate as a 40% overrun rather than revising the baseline.",
      "effect_on_reasoning_or_decision": "Budget expectations and subsequent check-ins remained tied to a thin vendor figure, making the more detailed internal estimate appear deviant rather than corrective.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I used it. Submitted it as our working budget baseline since it was the only concrete number on the table and finance needed something.",
          "evidence_explanation": "Shows the initial vendor figure was adopted as the anchor under time pressure."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It came in about 40% higher. Some scope items the vendor hadn't accounted for — data migration edge cases, mostly. When I brought it to finance, I remember framing it as an overrun against the original number rather than as, you know, the number we probably should have started with.",
          "evidence_explanation": "Shows the later estimate was assimilated to the anchor; the discrepancy was interpreted as an overrun from the vendor figure rather than evidence against that initial baseline."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Every budget check-in after that referenced it as the baseline, even once we knew it wasn't built on solid scoping.",
          "evidence_explanation": "Demonstrates the persistent influence of the anchor on later evaluations even after its weakness was known."
        }
      ],
      "correction_or_counterevidence": "The internal estimate eventually provided stronger scope information, but it was absorbed into the anchored baseline rather than resetting it. A legitimate time-pressure explanation exists for initially using the vendor figure, but the persistent baseline use after reliability concerns supports insufficient adjustment.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The Rastogi et al. source directly names and describes anchoring-and-adjustment in decision-making and supports the mechanism used here.",
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": "Deciding fast and slow: The role of cognitive biases in AI-assisted decision-making",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "We focus on anchoring bias and the associated anchoringandadjustment heuristic that is important towards optimizing team performance.",
          "mechanism_supported_by_source": "The source identifies anchoring bias and the anchoring-and-adjustment heuristic as a recognized mechanism influencing decision-making.",
          "relevance_to_this_occurrence": "It supports labeling the participant's reliance on the early vendor figure as an anchoring process."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory bias",
        "Myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm one's pre-existing beliefs or expectations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Usability test interpretation",
      "decision_point_description": "Interpreting mixed usability results for a stakeholder readout",
      "affected_reasoning_operation": "Evidence weighting and interpretation",
      "bias_specific_mechanism": "Prior confidence in the navigation model led the participant to seek positive feedback, discount negative findings as user onboarding gaps, and fail to apply equivalent scrutiny to positive and negative evidence.",
      "manifestation_in_interview": "The participant looked for positive comments to include in the stakeholder readout and explained away confusion cases while not scrutinizing positive responses for problems.",
      "effect_on_reasoning_or_decision": "The stakeholder readout emphasized positive feedback and downplayed navigation confusion, potentially delaying recognition of a design flaw later confirmed in a follow-up round.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I went back through the transcripts looking for more of the positive comments to include in the stakeholder readout.",
          "evidence_explanation": "Shows active search for supportive evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "For the confusion cases, my read was that a lot of it looked like people just not being used to the new pattern yet — more of an onboarding gap than a structural flaw in the design.",
          "evidence_explanation": "Shows asymmetric discounting of disconfirming evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I don't think I dug into the positive transcripts looking for problems the same way I dug into the negative ones looking for mitigating explanations. I was fairly confident in the navigation model going in, so I think I was reading the results through that lens somewhat.",
          "evidence_explanation": "Explicitly describes belief-consistent interpretation and uneven scrutiny."
        }
      ],
      "correction_or_counterevidence": "The follow-up round showed a similar confusion rate with a different cohort, providing independent counterevidence after the initial interpretation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a definition or mechanism for confirmation bias; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "Salience bias",
        "Vividness effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging the frequency, likelihood, or importance of an event by how easily examples come to mind or by their vividness or salience.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-demo risk framing",
      "decision_point_description": "Framing pilot-week risk for leadership after a live demo crash",
      "affected_reasoning_operation": "Risk assessment and emphasis allocation",
      "bias_specific_mechanism": "A single vivid, emotionally salient demo crash was easily recalled and therefore disproportionately weighted in the participant's risk narrative, overshadowing aggregate pilot metrics showing 92% transaction success.",
      "manifestation_in_interview": "The participant acknowledged giving the crash more airtime than statistically warranted and emphasizing it when discussing where risk actually sat.",
      "effect_on_reasoning_or_decision": "Leadership risk perception was shaped around a single salient failure rather than the broader reliability data; later log review attributed the crash to test-environment misconfiguration.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I put together the risk framing for leadership, that incident got a lot of airtime — more, probably, than a single session out of a whole pilot week statistically deserved.",
          "evidence_explanation": "Shows the participant recognized the incident received disproportionate weight relative to its statistical frequency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The 92% success rate was in there, but the crash was what people remembered, and honestly what I emphasized too when talking about where the risk actually sat.",
          "evidence_explanation": "Demonstrates that the vivid crash, not the aggregate reliability data, dominated the risk narrative."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not yet. Log review came later and traced it to a test-environment misconfiguration, not the architecture itself. But that came after the risk framing had already been shaped.",
          "evidence_explanation": "Confirms the salient event influenced the risk story before diagnostic information was available."
        }
      ],
      "correction_or_counterevidence": "Later log review found the crash was due to test-environment misconfiguration, not architecture, but this came after the risk framing had been shaped.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus directly addresses the availability heuristic; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Psychological reactance",
      "alternative_labels": [
        "Reactance bias",
        "Not-invented-here bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A motivational reaction to threats to behavioral freedom or autonomy in which individuals resist or reject external directives and work to restore control.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Mandated authentication approach response",
      "decision_point_description": "Responding to a security mandate to switch to a centralized identity provider",
      "affected_reasoning_operation": "Option generation and technical evaluation",
      "bias_specific_mechanism": "The security directive threatened the participant's autonomy and ownership over the authentication approach already built. The participant drafted an alternative design before completing a technical comparison, driven by the desire to retain control rather than by a specific technical concern.",
      "manifestation_in_interview": "The participant reported frustration with the directive, then created an alternative compliance design partly to avoid simply adopting what was mandated.",
      "effect_on_reasoning_or_decision": "The mandated identity provider may have been rejected or deprioritized on non-technical grounds, funneling effort into an alternative design before full technical assessment.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction, honestly, was frustration that it was being handed down as a directive rather than a conversation. We'd already built out our own authentication approach and gotten it partway implemented. I ended up drafting an alternative design that would satisfy the compliance finding a different way — partly because I wanted us to keep some control over that part of the architecture rather than just adopting what we were told to.",
          "evidence_explanation": "Shows the motivational response and alternative design search were prompted by autonomy threat rather than technical evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really a strong one at that point — we hadn't done a full technical comparison yet. It was more that being told 'do it this way' rubbed me the wrong way given the work we'd already put in.",
          "evidence_explanation": "Confirms the reaction was motivated by the delivery and prior investment rather than a specific technical deficiency."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think so. I might have approached the comparison more on the merits rather than looking for an alternative right away.",
          "evidence_explanation": "Counterfactual evidence that a non-directive framing would have led to more technical, merit-based evaluation."
        }
      ],
      "correction_or_counterevidence": "The alternative design may still have satisfied the compliance finding, and the participant's desire for architectural control could also reflect legitimate professional ownership; however, the participant explicitly stated that a full technical comparison had not yet occurred and that the delivery was the stronger driver.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage supplied a definition or mechanism for psychological reactance; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Sunk cost fallacy",
      "alternative_labels": [
        "Escalation of commitment",
        "Plan continuation bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue a course of action because of prior invested resources, even when continuing is no longer justified by future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Continuation decision after integration setbacks",
      "decision_point_description": "Deciding whether to continue the microservices migration or pause/revert after delays and outages",
      "affected_reasoning_operation": "Cost-benefit evaluation and continuation decision",
      "bias_specific_mechanism": "The participant's decision to continue the migration was disproportionately influenced by work already completed and the desire not to waste it, rather than a rigorous comparison of continuing versus stopping.",
      "manifestation_in_interview": "Despite delays, outages, and partial cutover, the participant framed continuing as the only path because reverting would waste months of work.",
      "effect_on_reasoning_or_decision": "Continuation of a troubled microservices migration without a rigorous stop-go analysis, potentially increasing subsequent cost and risk.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We talked about pausing. But we'd already cut over two services, and reverting those felt like it would waste months of work. Given the timeline pressure too, continuing forward seemed like the only path that didn't throw away what we'd built.",
          "evidence_explanation": "Shows prior investment and wasted-work framing dominating the continuation decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not as rigorously as maybe I should have. The sunk work was very present in my mind at that moment.",
          "evidence_explanation": "Explicitly acknowledges that sunk work influenced the decision more than a rigorous forward-looking comparison."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged the analysis was asymmetric; delays and outages were evidence for pausing, but prior investment dominated. Timeline pressure was also present as a non-bias constraint, though it does not explain the admitted lack of rigorous stop-go evaluation.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage directly defines sunk cost fallacy; a retrieved cockpit paper mentions plan continuation bias, but insufficient mechanism-level support was available.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Bandwagon effect",
      "alternative_labels": [
        "Social proof",
        "Availability heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Backend architecture selection",
      "supporting_interview_quote": "The peer examples carried real weight for me, honestly. If three firms our size had gone that direction and it worked out, it felt like a validated path rather than something experimental.",
      "plausible_mechanism": "The salience and ease of recalling three peer case studies may have made the microservices path seem more validated than the baseline evidence justified, potentially reflecting availability or social-proof influence.",
      "why_not_identified": "Peer examples are a reasonable professional input; the transcript does not clearly demonstrate disproportionate distortion because an internal risk memo also independently assessed the path as moderate risk, and the participant did not ignore that evidence."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus directly supports anchoring but provides limited definitions for confirmation, availability, reactance, and sunk-cost mechanisms; those classifications rely on established cognitive-science knowledge.",
    "The analysis is based on a single self-report interview and cannot independently verify whether some behaviors reflect legitimate professional judgment under constraint.",
    "Some retrieved passages are OCR-fragmented and were used conservatively to avoid unsupported attribution.",
    "Confidence ratings reflect the strength of transcript evidence and were constrained by possible non-bias explanations such as time pressure, professional autonomy, and legitimate use of industry precedent."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific project experience, it'll be recorded for research purposes, and you can skip anything you'd rather not discuss. Sound okay? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me a bit about your role and the project we're discussing? Participant: Sure. I'm the software architect on our customer portal modernization. We were rebuilding the self-service portal for retail banking customers — new interaction design, plus re-architecting the backend off a fairly old monolith. I owned the technical direction end to end, working with a UX researcher, our backend team, security and compliance, and an external vendor who helped with the front-end migration. Interviewer: What was the objective when the project kicked off? Participant: We had a hard deadline — six months — tied to a regulatory reporting change, so the date wasn't negotiable. The goal was a portal that was both more usable and could scale better, since the existing system was tightly coupled to our core banking platform and every change took forever to ship. Interviewer: Walk me through how the project actually unfolded, from your perspective. Participant: It started with scoping. We brought in a vendor to help estimate the front-end migration piece, since we didn't have deep in-house experience with the newer framework we wanted to use. Around the same time, we kicked off early usability testing on a new navigation model I'd designed — basically restructuring how customers move between the dashboard and their account details. That ran in parallel with an architecture debate on the backend: whether to do a more conservative monolith refactor or go further and decompose into microservices. That decision took a few weeks and involved looking at what similar firms had done. Once we picked a direction, we moved into execution, and about four months in we hit some turbulence — delays, a couple of outages, and separately, a mandate from security to change our authentication approach. That's roughly the shape of it. Interviewer: Let's go back to the very beginning — the budget number. What happened there? Participant: Finance needed a number within about a week to lock the budget, and we didn't have a detailed internal estimate yet — that takes real engineering time to build properly. So we did a scoping call with the vendor, and they gave us a rough order-of-magnitude figure for the migration, both cost and timeline. Interviewer: What did you do with that figure? Participant: I used it. Submitted it as our working budget baseline since it was the only concrete number on the table and finance needed something. Interviewer: Did you consider other options — waiting, or giving a range instead? Participant: We could have waited two more weeks for a real internal estimate, or given a range with caveats. I thought about the range option, actually, but figured a single number would be easier for finance to plan around, and the vendor had done similar migrations before, so it seemed like a reasonable placeholder. Interviewer: What happened once the internal team produced their own estimate? Participant: It came in about 40% higher. Some scope items the vendor hadn't accounted for — data migration edge cases, mostly. When I brought it to finance, I remember framing it as an overrun against the original number rather than as, you know, the number we probably should have started with. It became this whole conversation about why we were 40% over, when really the vendor's figure was just thin to begin with. Interviewer: Looking back, how much weight do you think that early vendor number carried in later conversations? Participant: Probably more than it should have. Every budget check-in after that referenced it as the baseline, even once we knew it wasn't built on solid scoping. Interviewer: Let's move to the usability testing. What did that process look like? Participant: We ran a round with ten beta users on the new navigation model. Results were mixed — six of ten had trouble moving between the dashboard and account sections, four completed tasks quickly and gave positive feedback. Our UX researcher's write-up flagged the navigation confusion as the top issue. Interviewer: How did you interpret that split? Participant: Honestly, I went back through the transcripts looking for more of the positive comments to include in the stakeholder readout. The four successful users had some pretty specific praise for the new layout, and I wanted that represented well. For the confusion cases, my read was that a lot of it looked like people just not being used to the new pattern yet — more of an onboarding gap than a structural flaw in the design. Interviewer: Did you apply the same level of scrutiny to the positive responses as the negative ones? Participant: That's a fair question. I don't think I dug into the positive transcripts looking for problems the same way I dug into the negative ones looking for mitigating explanations. I was fairly confident in the navigation model going in, so I think I was reading the results through that lens somewhat. Interviewer: What did the follow-up round show? Participant: Similar confusion rate with a different cohort. So it wasn't a one-off. Interviewer: Now, the architecture decision — monolith refactor versus microservices. How did that get resolved? Participant: That one took real debate. Monolith refactor was lower risk but wouldn't buy us much scalability. Microservices was a bigger lift but matched what we'd seen at a few peer firms — three other financial companies had presented case studies on similar decompositions at a conference a few months earlier. Our own backend risk memo called the microservices path 'moderate risk, manageable with phased rollout.' Interviewer: What tipped the decision toward microservices? Participant: The peer examples carried real weight for me, honestly. If three firms our size had gone that direction and it worked out, it felt like a validated path rather than something experimental. That was alongside the internal risk memo, but I'd say the industry pattern was part of what made me comfortable recommending it. Interviewer: Around that time there was also a demo incident. Can you describe that? Participant: Yeah — during a live demo for the executive sponsor, one beta session crashed. Visible, in the room, bad timing. That was against a backdrop of pretty strong pilot metrics otherwise — 92% of transactions completing successfully that week. Interviewer: How did that crash factor into the risk assessment you presented afterward? Participant: I'd be lying if I said it didn't dominate the narrative. When I put together the risk framing for leadership, that incident got a lot of airtime — more, probably, than a single session out of a whole pilot week statistically deserved. The 92% success rate was in there, but the crash was what people remembered, and honestly what I emphasized too when talking about where the risk actually sat. Interviewer: Did you know at that point what caused the crash? Participant: Not yet. Log review came later and traced it to a test-environment misconfiguration, not the architecture itself. But that came after the risk framing had already been shaped. Interviewer: Let's get to four months in. What was happening then? Participant: We'd cut over two of five planned services, both later than planned, integration bugs slowing things down. A monitoring report showed rising latency and two customer-facing outages tied to the new service mesh. On top of that, security formally mandated we switch to a centralized identity provider for authentication, citing a compliance finding. Interviewer: What was your reaction to the mandate? Participant: My first reaction, honestly, was frustration that it was being handed down as a directive rather than a conversation. We'd already built out our own authentication approach and gotten it partway implemented. I ended up drafting an alternative design that would satisfy the compliance finding a different way — partly because I wanted us to keep some control over that part of the architecture rather than just adopting what we were told to. Interviewer: Did you have a specific technical concern with the mandated identity provider itself? Participant: Not really a strong one at that point — we hadn't done a full technical comparison yet. It was more that being told 'do it this way' rubbed me the wrong way given the work we'd already put in. Interviewer: And the decision to keep going with the migration despite the delays and outages? Participant: We talked about pausing. But we'd already cut over two services, and reverting those felt like it would waste months of work. Given the timeline pressure too, continuing forward seemed like the only path that didn't throw away what we'd built. Interviewer: Did you weigh that against the possibility that continuing might cost more than stopping? Participant: Not as rigorously as maybe I should have. The sunk work was very present in my mind at that moment. Interviewer: If the vendor's early number had never come up, do you think the budget conversation would have gone differently? Participant: Probably. Without an anchor point, finance might have pushed harder for the detailed estimate up front instead of accepting a placeholder. Interviewer: If the demo crash hadn't happened in front of the executive sponsor, would your risk framing have looked different? Participant: Almost certainly. I think the 92% number would have carried more weight in isolation. Interviewer: If the security mandate had come as a suggestion rather than a directive, would your response have changed? Participant: I think so. I might have approached the comparison more on the merits rather than looking for an alternative right away. Interviewer: Looking back across all four moments, what would you do differently? Participant: Push for the range instead of a single budget number, apply the same scrutiny to positive and negative usability feedback, separate the peer-adoption story from the actual risk memo, and evaluate the identity provider mandate on technical grounds before reacting to how it was delivered.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.58s · gen 161.20s · total 166.6s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0220 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0220 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0220 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0201 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
5. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0195 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
6. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0190 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0189 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0181 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
11. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0176 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
13. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
14. **Hallihan_etal_DTM_12.pdf** — 0.0169 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
15. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0168 (rrf) — _# Cognitive Biases in Technical Communication We are surrounded by stimuli. The new experiences _
16. **ijcma-08-2012-0064.pdf** — 0.0168 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
17. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0166 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
18. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
21. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
22. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
23. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0161 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
24. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0160 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
25. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
27. **ijcma-08-2012-0064.pdf** — 0.0156 (rrf) — _# 382 I used this with a man and woman team, both of whom I knew didn’t care for each other busi_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0154 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0153 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0152 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
32. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0151 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
35. **Hallihan_etal_DTM_12.pdf** — 0.0148 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
36. **ijcma-08-2012-0064.pdf** — 0.0148 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
37. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0146 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
39. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0145 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
40. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
41. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0144 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
42. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
43. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
45. **Hallihan_etal_DTM_12.pdf** — 0.0142 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
46. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0141 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
47. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
48. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0138 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
49. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0138 (rrf) — _# Cognitive Biases in Technical Communication | | journey? Where do we place rewards in that jou_
50. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0138 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative mechanism-first analysis of the Participant's reported reasoning in budgeting, usability interpretation, architecture selection, risk communication, security response, and migration continuation. Corpus support was available for anchoring and confirmation bias; other labels use widely established cognitive-science terminology from general knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "anchoring bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "psychological reactance",
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
        "anchoring-and-adjustment heuristic",
        "anchoring effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to rely too heavily on an initial piece of information, or anchor, when making estimates or decisions, with insufficient adjustment away from that anchor.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Selection of initial budget baseline and later framing of cost deviations",
      "decision_point_description": "Whether to submit the vendor's rough order-of-magnitude figure as the working budget baseline when finance needed a number within a week.",
      "affected_reasoning_operation": "Budget estimation and subsequent framing of cost deviations",
      "bias_specific_mechanism": "The early vendor figure became the initial reference point; later internal estimates were assessed against that anchor, and deviations were framed as overruns rather than as corrections of a thin initial placeholder.",
      "manifestation_in_interview": "The Participant used the vendor's rough figure as the working baseline, then later framed the internal estimate as 40% over the original number even though the original number was not built on solid scoping.",
      "effect_on_reasoning_or_decision": "The budget baseline was anchored to a thin order-of-magnitude vendor figure, and subsequent budget conversations continued to treat that figure as the reference point.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Finance needed a number within about a week to lock the budget, and we didn't have a detailed internal estimate yet — that takes real engineering time to build properly. So we did a scoping call with the vendor, and they gave us a rough order-of-magnitude figure for the migration, both cost and timeline.",
          "evidence_explanation": "This establishes that the vendor figure was an early rough estimate accepted under time pressure, creating the initial anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I used it. Submitted it as our working budget baseline since it was the only concrete number on the table and finance needed something.",
          "evidence_explanation": "The Participant explicitly says the early concrete figure was adopted as the baseline, which is the anchoring event."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I brought it to finance, I remember framing it as an overrun against the original number rather than as, you know, the number we probably should have started with.",
          "evidence_explanation": "This shows insufficient adjustment from the anchor: the later estimate was interpreted relative to the original figure instead of replacing it."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Every budget check-in after that referenced it as the baseline, even once we knew it wasn't built on solid scoping.",
          "evidence_explanation": "The anchor persisted across later reasoning episodes despite awareness that the original number was weak."
        }
      ],
      "correction_or_counterevidence": "The Participant did consider giving a range or waiting for an internal estimate, and the vendor had relevant migration experience, making the placeholder defensible under deadline pressure.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The label and mechanism are supported by the retrieved Rastogi et al. passage on anchoring bias and anchoring-and-adjustment.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "We focus on anchoring bias and the associated anchoringandadjustment heuristic that is important towards optimizing team performance. We validate the use of time as an eective strategy for mitigating anchoring bias through a user study.",
          "mechanism_supported_by_source": "The source supports anchoring bias and the anchoring-and-adjustment heuristic as decision-making phenomena that can be mitigated with specific strategies.",
          "relevance_to_this_occurrence": "The Participant's reliance on an early vendor figure and later failure to fully adjust away from it mirrors the anchoring-and-adjustment mechanism described in the source."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "myside bias",
        "selective exposure"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's prior beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation and communication of usability test results",
      "decision_point_description": "How to interpret mixed usability results for the stakeholder readout.",
      "affected_reasoning_operation": "Interpretation of usability test results and preparation of stakeholder communication",
      "bias_specific_mechanism": "The Participant sought confirming positive feedback and generated mitigating explanations for negative feedback while not applying the same scrutiny to positive responses, consistent with a prior belief in the navigation model.",
      "manifestation_in_interview": "The Participant looked through transcripts for positive comments to feature, interpreted confusion as an onboarding gap, and acknowledged reading results through a pre-existing lens.",
      "effect_on_reasoning_or_decision": "The stakeholder readout was shaped to represent positive comments favorably while downplaying the most common usability problem, later confirmed in a follow-up round.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I went back through the transcripts looking for more of the positive comments to include in the stakeholder readout.",
          "evidence_explanation": "This is selective searching for evidence consistent with the Participant's favored design."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The four successful users had some pretty specific praise for the new layout, and I wanted that represented well. For the confusion cases, my read was that a lot of it looked like people just not being used to the new pattern yet — more of an onboarding gap than a structural flaw in the design.",
          "evidence_explanation": "The Participant favored positive evidence and constructed a mitigating explanation for disconfirming evidence rather than treating it as a potential design flaw."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I don't think I dug into the positive transcripts looking for problems the same way I dug into the negative ones looking for mitigating explanations. I was fairly confident in the navigation model going in, so I think I was reading the results through that lens somewhat.",
          "evidence_explanation": "This is an explicit acknowledgment of asymmetric scrutiny driven by prior confidence in the design."
        }
      ],
      "correction_or_counterevidence": "The UX researcher's write-up flagged navigation confusion as the top issue, and a follow-up round with a different cohort showed a similar confusion rate; these are later corrective signals, but the initial stakeholder interpretation was already affected.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved space flight systems passage supports confirmation-like mechanisms: people weight hypothesis-supporting evidence more heavily and scrutinize disconfirming evidence critically.",
      "corpus_evidence": [
        {
          "source_identifier": null,
          "paper_title": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Lord et al found that participants we critical of evidence that refuted their beliefs tha information in support [10]. Other researchers [4] found that people give greater weight to evidence t supports a previously adopted hypothesis.",
          "mechanism_supported_by_source": "People give greater weight to evidence supporting a previously adopted hypothesis and are more critical of evidence contradicting their beliefs.",
          "relevance_to_this_occurrence": "The Participant gave favorable weight to positive usability comments and was more dismissive of negative findings, consistent with the confirmatory weighting mechanism described in the source."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "bandwagon effect",
      "alternative_labels": [
        "social proof",
        "imitation heuristic"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to adopt a belief, practice, or behavior because other people or peer organizations have done so, sometimes treating adoption by others as stronger evidence of correctness than the underlying case.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Architecture decision between monolith refactor and microservices",
      "decision_point_description": "Selection of the backend architecture direction after considering internal risk and peer case studies.",
      "affected_reasoning_operation": "Architecture recommendation and risk judgment",
      "bias_specific_mechanism": "Peer adoption by three similar financial firms made the larger-lift microservices path feel like a validated path rather than an experimental one, increasing comfort with the option beyond what the internal risk memo alone provided.",
      "manifestation_in_interview": "The Participant reported that peer examples carried real weight and made the microservices direction feel validated because other firms had followed that path.",
      "effect_on_reasoning_or_decision": "The decision tipped toward microservices partly through perceived validation from peer adoption rather than purely on internal risk analysis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Microservices was a bigger lift but matched what we'd seen at a few peer firms — three other financial companies had presented case studies on similar decompositions at a conference a few months earlier.",
          "evidence_explanation": "This establishes that peer adoption was a salient input to the architecture choice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The peer examples carried real weight for me, honestly. If three firms our size had gone that direction and it worked out, it felt like a validated path rather than something experimental.",
          "evidence_explanation": "The Participant describes the mechanism: peer success made the option feel validated rather than experimental, implying reduced perceived uncertainty from social proof."
        }
      ],
      "correction_or_counterevidence": "The internal risk memo independently described microservices as moderate risk and manageable with phased rollout, so peer adoption may have been a legitimate input rather than a decisive bias. The Participant used peer examples alongside the risk memo.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the bandwagon effect label was not available; the label and mechanism are drawn from widely established cognitive-science literature.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias",
        "salience bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge frequency, probability, or risk based on how easily examples come to mind, with salient or vivid events often overweighted.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Risk assessment framing after live demo crash",
      "decision_point_description": "How to frame pilot risk to leadership after one visible demo crash despite strong aggregate completion metrics.",
      "affected_reasoning_operation": "Risk assessment and communication after a pilot incident",
      "bias_specific_mechanism": "A single vivid, publicly visible demo crash became the most mentally available risk example and dominated the risk narrative, despite being statistically minor compared with the 92% success rate.",
      "manifestation_in_interview": "The Participant emphasized the crash in risk framing and acknowledged it received more weight than a single session out of the pilot week statistically deserved.",
      "effect_on_reasoning_or_decision": "Leadership risk perception was shaped around a salient crash rather than aggregate pilot performance; the 92% success rate was present but not the dominant narrative.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I put together the risk framing for leadership, that incident got a lot of airtime — more, probably, than a single session out of a whole pilot week statistically deserved.",
          "evidence_explanation": "This directly expresses that a salient event received disproportionate weight in risk judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The 92% success rate was in there, but the crash was what people remembered, and honestly what I emphasized too when talking about where the risk actually sat.",
          "evidence_explanation": "The ease of recalling the vivid crash, rather than the base rate of success, shaped the risk emphasis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Almost certainly. I think the 92% number would have carried more weight in isolation.",
          "evidence_explanation": "The Participant confirms that without the salient crash, the aggregate metric would likely have dominated the framing."
        }
      ],
      "correction_or_counterevidence": "The crash was objectively visible and occurred during a live executive demo, so emphasizing it may have been defensible for stakeholder trust. The later log review identified a test-environment misconfiguration, but that came after the risk framing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the availability heuristic label was not available; the label and mechanism are drawn from widely established cognitive-science literature.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "psychological reactance",
      "alternative_labels": [
        "reactance",
        "reactance bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A motivational reaction to perceived threats to autonomy that can bias evaluation and decision-making, leading people to resist or devalue an option because it is imposed.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to security authentication mandate",
      "decision_point_description": "Whether to evaluate the mandated identity provider on technical merits or immediately draft an alternative design.",
      "affected_reasoning_operation": "Evaluation of a security architecture mandate and generation of an alternative design",
      "bias_specific_mechanism": "The directive nature of the mandate triggered frustration and a desire to retain control, leading the Participant to draft an alternative before performing a full technical comparison.",
      "manifestation_in_interview": "The Participant reported feeling rubbed the wrong way by being told what to do and acknowledged that a suggestion would likely have led to a more merits-based comparison.",
      "effect_on_reasoning_or_decision": "The Participant began an alternative design partly to preserve architectural control rather than because the mandated provider had been found technically inferior.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction, honestly, was frustration that it was being handed down as a directive rather than a conversation. We'd already built out our own authentication approach and gotten it partway implemented.",
          "evidence_explanation": "This identifies the emotional reaction to perceived autonomy threat, not to the technical content of the mandated identity provider."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up drafting an alternative design that would satisfy the compliance finding a different way — partly because I wanted us to keep some control over that part of the architecture rather than just adopting what we were told to.",
          "evidence_explanation": "The alternative was driven partly by control preservation, which is the reactance mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "It was more that being told 'do it this way' rubbed me the wrong way given the work we'd already put in.",
          "evidence_explanation": "The Participant explicitly says the reaction was to being told what to do rather than to a technical concern."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I might have approached the comparison more on the merits rather than looking for an alternative right away.",
          "evidence_explanation": "This shows the directive framing changed the reasoning process, shifting it away from a merits-based technical evaluation."
        }
      ],
      "correction_or_counterevidence": "There was a compliance finding requiring some change, and the Participant may have had legitimate architectural control and existing implementation concerns. He also acknowledged no full technical comparison had yet been made.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the psychological reactance label was not available; the label and mechanism are drawn from widely established cognitive-science literature.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an endeavor or to weigh prior unrecoverable investments as relevant to future decisions, rather than evaluating only future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to continue migration after delays and outages",
      "decision_point_description": "Whether to pause or continue the microservices migration after two services were cut over late, with latency issues and customer-facing outages.",
      "affected_reasoning_operation": "Continuation-versus-pause decision under schedule pressure",
      "bias_specific_mechanism": "The time and work already invested in cutting over two services made reverting feel like wasted months, causing the Participant to favor continuation without rigorously weighing future costs and risks.",
      "manifestation_in_interview": "The Participant reported that the sunk work was very present and that continuing felt like the only path that did not throw away what had been built.",
      "effect_on_reasoning_or_decision": "The migration continued despite delays and outages, with the explicit acknowledgment that stopping was not rigorously weighed against continuing.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We talked about pausing. But we'd already cut over two services, and reverting those felt like it would waste months of work.",
          "evidence_explanation": "The framing of reverting as waste indicates that past investment was treated as a primary reason to continue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Given the timeline pressure too, continuing forward seemed like the only path that didn't throw away what we'd built.",
          "evidence_explanation": "The decision rule favored preserving prior work rather than comparing future costs and benefits of continuing versus pausing."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not as rigorously as maybe I should have. The sunk work was very present in my mind at that moment.",
          "evidence_explanation": "This is an explicit acknowledgment that sunk cost loomed large in the reasoning process."
        }
      ],
      "correction_or_counterevidence": "The regulatory deadline and the practical difficulty of reverting two cut-over services were legitimate constraints; continuing may still have been rational under time pressure.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the sunk cost fallacy label was not available; the label and mechanism are drawn from widely established cognitive-science literature.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The provided corpus support was sparse and partly domain-specific or OCR-degraded; some labels rely on general knowledge rather than retrieved passages.",
    "The analysis relies on the Participant's retrospective self-report, which may introduce memory or self-presentation distortions.",
    "The interview does not include independent confirmation of the documented project events or decision outcomes.",
    "Some bias attributions have plausible non-bias explanations, such as legitimate time pressure, salience of a visible failure, or reasonable use of peer evidence."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to confirm, this is a voluntary conversation about a specific project experience, it'll be recorded for research purposes, and you can skip anything you'd rather not discuss. Sound okay? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you start by telling me a bit about your role and the project we're discussing? Participant: Sure. I'm the software architect on our customer portal modernization. We were rebuilding the self-service portal for retail banking customers — new interaction design, plus re-architecting the backend off a fairly old monolith. I owned the technical direction end to end, working with a UX researcher, our backend team, security and compliance, and an external vendor who helped with the front-end migration. Interviewer: What was the objective when the project kicked off? Participant: We had a hard deadline — six months — tied to a regulatory reporting change, so the date wasn't negotiable. The goal was a portal that was both more usable and could scale better, since the existing system was tightly coupled to our core banking platform and every change took forever to ship. Interviewer: Walk me through how the project actually unfolded, from your perspective. Participant: It started with scoping. We brought in a vendor to help estimate the front-end migration piece, since we didn't have deep in-house experience with the newer framework we wanted to use. Around the same time, we kicked off early usability testing on a new navigation model I'd designed — basically restructuring how customers move between the dashboard and their account details. That ran in parallel with an architecture debate on the backend: whether to do a more conservative monolith refactor or go further and decompose into microservices. That decision took a few weeks and involved looking at what similar firms had done. Once we picked a direction, we moved into execution, and about four months in we hit some turbulence — delays, a couple of outages, and separately, a mandate from security to change our authentication approach. That's roughly the shape of it. Interviewer: Let's go back to the very beginning — the budget number. What happened there? Participant: Finance needed a number within about a week to lock the budget, and we didn't have a detailed internal estimate yet — that takes real engineering time to build properly. So we did a scoping call with the vendor, and they gave us a rough order-of-magnitude figure for the migration, both cost and timeline. Interviewer: What did you do with that figure? Participant: I used it. Submitted it as our working budget baseline since it was the only concrete number on the table and finance needed something. Interviewer: Did you consider other options — waiting, or giving a range instead? Participant: We could have waited two more weeks for a real internal estimate, or given a range with caveats. I thought about the range option, actually, but figured a single number would be easier for finance to plan around, and the vendor had done similar migrations before, so it seemed like a reasonable placeholder. Interviewer: What happened once the internal team produced their own estimate? Participant: It came in about 40% higher. Some scope items the vendor hadn't accounted for — data migration edge cases, mostly. When I brought it to finance, I remember framing it as an overrun against the original number rather than as, you know, the number we probably should have started with. It became this whole conversation about why we were 40% over, when really the vendor's figure was just thin to begin with. Interviewer: Looking back, how much weight do you think that early vendor number carried in later conversations? Participant: Probably more than it should have. Every budget check-in after that referenced it as the baseline, even once we knew it wasn't built on solid scoping. Interviewer: Let's move to the usability testing. What did that process look like? Participant: We ran a round with ten beta users on the new navigation model. Results were mixed — six of ten had trouble moving between the dashboard and account sections, four completed tasks quickly and gave positive feedback. Our UX researcher's write-up flagged the navigation confusion as the top issue. Interviewer: How did you interpret that split? Participant: Honestly, I went back through the transcripts looking for more of the positive comments to include in the stakeholder readout. The four successful users had some pretty specific praise for the new layout, and I wanted that represented well. For the confusion cases, my read was that a lot of it looked like people just not being used to the new pattern yet — more of an onboarding gap than a structural flaw in the design. Interviewer: Did you apply the same level of scrutiny to the positive responses as the negative ones? Participant: That's a fair question. I don't think I dug into the positive transcripts looking for problems the same way I dug into the negative ones looking for mitigating explanations. I was fairly confident in the navigation model going in, so I think I was reading the results through that lens somewhat. Interviewer: What did the follow-up round show? Participant: Similar confusion rate with a different cohort. So it wasn't a one-off. Interviewer: Now, the architecture decision — monolith refactor versus microservices. How did that get resolved? Participant: That one took real debate. Monolith refactor was lower risk but wouldn't buy us much scalability. Microservices was a bigger lift but matched what we'd seen at a few peer firms — three other financial companies had presented case studies on similar decompositions at a conference a few months earlier. Our own backend risk memo called the microservices path 'moderate risk, manageable with phased rollout.' Interviewer: What tipped the decision toward microservices? Participant: The peer examples carried real weight for me, honestly. If three firms our size had gone that direction and it worked out, it felt like a validated path rather than something experimental. That was alongside the internal risk memo, but I'd say the industry pattern was part of what made me comfortable recommending it. Interviewer: Around that time there was also a demo incident. Can you describe that? Participant: Yeah — during a live demo for the executive sponsor, one beta session crashed. Visible, in the room, bad timing. That was against a backdrop of pretty strong pilot metrics otherwise — 92% of transactions completing successfully that week. Interviewer: How did that crash factor into the risk assessment you presented afterward? Participant: I'd be lying if I said it didn't dominate the narrative. When I put together the risk framing for leadership, that incident got a lot of airtime — more, probably, than a single session out of a whole pilot week statistically deserved. The 92% success rate was in there, but the crash was what people remembered, and honestly what I emphasized too when talking about where the risk actually sat. Interviewer: Did you know at that point what caused the crash? Participant: Not yet. Log review came later and traced it to a test-environment misconfiguration, not the architecture itself. But that came after the risk framing had already been shaped. Interviewer: Let's get to four months in. What was happening then? Participant: We'd cut over two of five planned services, both later than planned, integration bugs slowing things down. A monitoring report showed rising latency and two customer-facing outages tied to the new service mesh. On top of that, security formally mandated we switch to a centralized identity provider for authentication, citing a compliance finding. Interviewer: What was your reaction to the mandate? Participant: My first reaction, honestly, was frustration that it was being handed down as a directive rather than a conversation. We'd already built out our own authentication approach and gotten it partway implemented. I ended up drafting an alternative design that would satisfy the compliance finding a different way — partly because I wanted us to keep some control over that part of the architecture rather than just adopting what we were told to. Interviewer: Did you have a specific technical concern with the mandated identity provider itself? Participant: Not really a strong one at that point — we hadn't done a full technical comparison yet. It was more that being told 'do it this way' rubbed me the wrong way given the work we'd already put in. Interviewer: And the decision to keep going with the migration despite the delays and outages? Participant: We talked about pausing. But we'd already cut over two services, and reverting those felt like it would waste months of work. Given the timeline pressure too, continuing forward seemed like the only path that didn't throw away what we'd built. Interviewer: Did you weigh that against the possibility that continuing might cost more than stopping? Participant: Not as rigorously as maybe I should have. The sunk work was very present in my mind at that moment. Interviewer: If the vendor's early number had never come up, do you think the budget conversation would have gone differently? Participant: Probably. Without an anchor point, finance might have pushed harder for the detailed estimate up front instead of accepting a placeholder. Interviewer: If the demo crash hadn't happened in front of the executive sponsor, would your risk framing have looked different? Participant: Almost certainly. I think the 92% number would have carried more weight in isolation. Interviewer: If the security mandate had come as a suggestion rather than a directive, would your response have changed? Participant: I think so. I might have approached the comparison more on the merits rather than looking for an alternative right away. Interviewer: Looking back across all four moments, what would you do differently? Participant: Push for the range instead of a single budget number, apply the same scrutiny to positive and negative usability feedback, separate the peer-adoption story from the actual risk memo, and evaluate the identity provider mandate on technical grounds before reacting to how it was delivered.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.55s · gen 123.59s · total 129.0s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0220 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
2. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0220 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0220 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0201 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
5. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0195 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
6. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
7. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0190 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
8. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0189 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0185 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
10. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0181 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
11. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0176 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
13. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
14. **Hallihan_etal_DTM_12.pdf** — 0.0169 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
15. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0168 (rrf) — _# Cognitive Biases in Technical Communication We are surrounded by stimuli. The new experiences _
16. **ijcma-08-2012-0064.pdf** — 0.0168 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
17. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0166 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
18. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0162 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
21. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
22. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
23. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0161 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
24. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0160 (rrf) — _# TOWARD A SYN THESIS OF COGNITIVE BIASES… ∑ ∑ ( ̂) ∑ ∑ ( ) ( ̂\| ∑ ∑ ( ̂\| ) transition matrix,_
25. **Hallihan_etal_DTM_12.pdf** — 0.0158 (rrf) — _protocol analysis , including A total of 107 instances were identified as confirmation descripti_
26. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0158 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
27. **ijcma-08-2012-0064.pdf** — 0.0156 (rrf) — _# 382 I used this with a man and woman team, both of whom I knew didn’t care for each other busi_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0154 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
29. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0153 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
30. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0152 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
31. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0152 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
32. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0151 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
33. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0150 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
35. **Hallihan_etal_DTM_12.pdf** — 0.0148 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
36. **ijcma-08-2012-0064.pdf** — 0.0148 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
37. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0146 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
38. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## lIs sues in wo whThe see Whlation of natural selection. Ruffed grouse, North American game bi_
39. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0145 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
40. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight Nevertheless, participants all believed they had so control over the operation _
41. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0144 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
42. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0143 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
43. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0143 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0143 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
45. **Hallihan_etal_DTM_12.pdf** — 0.0142 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
46. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0141 (rrf) — _We embedded behavioral measures in all three of our games to assess shortand longterm effects an_
47. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0139 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
48. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0138 (rrf) — _# 4.2 Answering our RQs AI & SOCIETY the AI’s recommendation, provided as a second opinion, alig_
49. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0138 (rrf) — _# Cognitive Biases in Technical Communication | | journey? Where do we place rewards in that jou_
50. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0138 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Mechanism-first analysis of bias-specific reasoning in a voluntary project retrospective; only affirmative transcript evidence was classified, and hypothetical, generic, or self-corrected cognition was excluded."
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
      "bias_label": "Bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Psychological reactance",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Sunk cost fallacy",
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
        "Anchoring-and-adjustment heuristic",
        "Anchoring effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Overreliance on an initial numeric value as a reference point and insufficient adjustment away from it.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Initial budget baseline submission",
      "decision_point_description": "Decision to submit the vendor's rough order-of-magnitude figure to finance as the working budget baseline.",
      "affected_reasoning_operation": "Numerical estimation and budget planning",
      "bias_specific_mechanism": "The vendor's rough order-of-magnitude number served as an anchor; later budget judgments were made by insufficiently adjusting away from that initial reference point.",
      "manifestation_in_interview": "The participant accepted and submitted the vendor's early figure because it was concrete and timely, then later interpreted the internal team's higher estimate as an overrun against that original number.",
      "effect_on_reasoning_or_decision": "The early vendor number became the baseline against which all later budget information was judged, making the 40% higher internal estimate appear as an overrun instead of a more realistic initial plan.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Finance needed a number within about a week to lock the budget, and we didn't have a detailed internal estimate yet — that takes real engineering time to build properly.",
          "evidence_explanation": "This establishes the time pressure and absence of a well-grounded internal estimate, making an external rough number more likely to be used as an anchor."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I used it. Submitted it as our working budget baseline since it was the only concrete number on the table and finance needed something.",
          "evidence_explanation": "This directly shows the initial adoption of the vendor figure as the baseline, the first step in the anchoring process."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "When I brought it to finance, I remember framing it as an overrun against the original number rather than as, you know, the number we probably should have started with.",
          "evidence_explanation": "The participant explicitly reports judging the new evidence relative to the initial anchor, rather than treating the internal estimate as the more valid baseline."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably more than it should have. Every budget check-in after that referenced it as the baseline, even once we knew it wasn't built on solid scoping.",
          "evidence_explanation": "This shows the anchor continued to influence later budget conversations despite awareness that it lacked solid scoping, demonstrating insufficient adjustment and persistence."
        }
      ],
      "correction_or_counterevidence": "The internal team later produced an estimate about 40% higher, and the participant eventually recognized the early vendor figure was 'thin' and not solidly scoped; however, the bias had already shaped budget framing and ongoing check-ins.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf",
          "paper_title": null,
          "authors": "Rastogi et al.",
          "publication_year": "2022",
          "retrieved_passage_or_finding": "We focus on anchoring bias and the associated anchoringandadjustment heuristic that is important towards optimizing team performance.",
          "mechanism_supported_by_source": "The paper identifies anchoring bias and the anchoring-and-adjustment heuristic as a decision-making mechanism.",
          "relevance_to_this_occurrence": "Supports the classification of the early vendor numeric figure as an anchor that shaped later budget baselines and adjustments."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmation tendencies",
        "Myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to seek, interpret, and weight information in ways that affirm existing beliefs or hypotheses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Usability test interpretation and stakeholder readout",
      "decision_point_description": "Interpretation of mixed usability-test results for the new navigation model and preparation of the stakeholder readout.",
      "affected_reasoning_operation": "Evidence evaluation and interpretation",
      "bias_specific_mechanism": "Asymmetric scrutiny: positive feedback was recruited for the stakeholder narrative, while negative feedback was explained away as an onboarding gap rather than a design flaw, consistent with prior confidence in the navigation model.",
      "manifestation_in_interview": "The participant reported going back through transcripts specifically to find positive comments, while treating confusion cases as users not being used to the new pattern.",
      "effect_on_reasoning_or_decision": "The stakeholder readout emphasized positive feedback and downplayed navigation confusion; a later round with a different cohort showed similar confusion, suggesting the initial interpretation was biased.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, I went back through the transcripts looking for more of the positive comments to include in the stakeholder readout.",
          "evidence_explanation": "This demonstrates an information-search pattern aimed at gathering belief-consistent positive evidence rather than evaluating all evidence evenly."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "For the confusion cases, my read was that a lot of it looked like people just not being used to the new pattern yet — more of an onboarding gap than a structural flaw in the design.",
          "evidence_explanation": "This shows belief-consistent reinterpretation of disconfirming evidence as temporary or external rather than informative about the design."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I don't think I dug into the positive transcripts looking for problems the same way I dug into the negative ones looking for mitigating explanations. I was fairly confident in the navigation model going in, so I think I was reading the results through that lens somewhat.",
          "evidence_explanation": "The participant explicitly acknowledges asymmetric scrutiny and prior belief as the lens driving interpretation, directly evidencing the confirmation-bias mechanism."
        }
      ],
      "correction_or_counterevidence": "The UX researcher's write-up flagged navigation confusion as the top issue, and a follow-up round with a different cohort showed a similar confusion rate, providing later disconfirming evidence against the participant's initial interpretation.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": null,
      "corpus_evidence": [
        {
          "source_identifier": "Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Lord et al found that participants we critical of evidence that refuted their beliefs tha information in support [10]. Other researchers [4] found that people give greater weight to evidence t supports a previously adopted hypothesis.",
          "mechanism_supported_by_source": "Describes confirmation bias as greater scrutiny of disconfirming evidence and greater weight given to evidence supporting a previously adopted hypothesis.",
          "relevance_to_this_occurrence": "Supports classification of the participant's asymmetric interpretation of positive and negative usability-test evidence."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "Bandwagon effect",
      "alternative_labels": [
        "Social proof",
        "Herd behavior"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to adopt a position or action because others have adopted it, rather than based solely on independent technical merits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Architecture selection recommendation",
      "decision_point_description": "Recommendation between a conservative monolith refactor and a microservices decomposition.",
      "affected_reasoning_operation": "Technology risk assessment and architectural recommendation",
      "bias_specific_mechanism": "Social-proof or bandwagon inference: adoption by three similar firms was interpreted as evidence that the microservices path was validated and non-experimental, increasing comfort beyond the project-specific risk evidence.",
      "manifestation_in_interview": "The participant reported that peer examples carried real weight and made the microservices path feel validated rather than experimental.",
      "effect_on_reasoning_or_decision": "Peer adoption likely shaped the participant's comfort recommending microservices, combining with, but potentially overweighting, the external examples relative to the internal risk memo.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The peer examples carried real weight for me, honestly. If three firms our size had gone that direction and it worked out, it felt like a validated path rather than something experimental.",
          "evidence_explanation": "This demonstrates that adoption by other firms was used as evidence of the path's validity, the core mechanism of social proof rather than purely independent technical analysis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "That was alongside the internal risk memo, but I'd say the industry pattern was part of what made me comfortable recommending it.",
          "evidence_explanation": "This supports that the social-proof signal contributed materially to the architectural recommendation, not merely as background color."
        }
      ],
      "correction_or_counterevidence": "An internal backend risk memo described the microservices path as 'moderate risk, manageable with phased rollout,' providing a legitimate project-specific basis; peer case studies are not inherently irrelevant evidence for architectural decisions.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for this specific label; the label is applied from general cognitive-science and social-influence knowledge rather than from retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Availability bias",
      "alternative_labels": [
        "Availability heuristic",
        "Vividness bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Overweighting easily recalled or vivid information when judging frequency, risk, or importance.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Post-demo risk framing for leadership",
      "decision_point_description": "Construction of the risk assessment framing presented to leadership after the live demo crash.",
      "affected_reasoning_operation": "Risk perception and communication",
      "bias_specific_mechanism": "The live demo crash was vivid, recent, publicly salient, and emotionally charged, making it highly available in memory and therefore overweighted relative to aggregate pilot success data.",
      "manifestation_in_interview": "A single demo crash dominated the risk narrative despite a 92% transaction success rate during the pilot week.",
      "effect_on_reasoning_or_decision": "The participant's risk framing emphasized the crash over statistically representative success data, likely shaping leadership's perception of where project risk actually sat.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I put together the risk framing for leadership, that incident got a lot of airtime — more, probably, than a single session out of a whole pilot week statistically deserved. The 92% success rate was in there, but the crash was what people remembered, and honestly what I emphasized too when talking about where the risk actually sat.",
          "evidence_explanation": "The participant explicitly states that the single vivid incident received disproportionate weighting relative to the aggregate statistical evidence, directly evidencing availability-based reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Almost certainly. I think the 92% number would have carried more weight in isolation.",
          "evidence_explanation": "This counterfactual admission confirms that the presence of the vivid crash specifically altered the risk framing, rather than the framing being based purely on balanced evidence."
        }
      ],
      "correction_or_counterevidence": "The pilot metrics showed 92% transaction success, and later log review traced the crash to a test-environment misconfiguration rather than the architecture itself, though the corrected causal explanation came after the risk framing had already been shaped.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for this specific label; the label is applied from general cognitive-science knowledge rather than from retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Psychological reactance",
      "alternative_labels": [
        "Reactance bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Motivational reaction to perceived threats to autonomy, leading to resistance or rejection of a directive independent of its technical merits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to security authentication mandate",
      "decision_point_description": "Decision to draft an alternative authentication design after security mandated a centralized identity provider.",
      "affected_reasoning_operation": "Technical evaluation and architectural response selection",
      "bias_specific_mechanism": "Perceived threat to decision autonomy from the directive produced motivational resistance, prompting an alternative design before a full technical comparison of the mandated provider.",
      "manifestation_in_interview": "The participant reacted to being told what to do by drafting an alternative that would keep control over that architecture area, despite not yet having a strong technical concern with the mandated identity provider.",
      "effect_on_reasoning_or_decision": "The participant committed effort to an alternative path before evaluating the mandated approach on technical merits, potentially shaping the subsequent architecture choice.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction, honestly, was frustration that it was being handed down as a directive rather than a conversation. We'd already built out our own authentication approach and gotten it partway implemented. I ended up drafting an alternative design that would satisfy the compliance finding a different way — partly because I wanted us to keep some control over that part of the architecture rather than just adopting what we were told to.",
          "evidence_explanation": "This directly evidences autonomy-threat reactance shaping the decision to draft an alternative before technical evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really a strong one at that point — we hadn't done a full technical comparison yet. It was more that being told 'do it this way' rubbed me the wrong way given the work we'd already put in.",
          "evidence_explanation": "The participant acknowledges the absence of strong technical grounds at that moment, isolating the directive delivery and autonomy threat as the main driver of resistance."
        }
      ],
      "correction_or_counterevidence": "The security mandate cited a compliance finding, so there was a legitimate external reason for the change; the participant also acknowledged no strong technical concern with the mandated identity provider at that point.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for this specific label; the label is applied from general motivational/social-influence knowledge rather than from retrieval.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Sunk cost fallacy",
      "alternative_labels": [
        "Escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue an endeavor because of already-invested resources, rather than based solely on future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to continue migration despite delays and outages",
      "decision_point_description": "Decision not to pause or revert the microservices migration after two services had been cut over, integration bugs appeared, and two customer-facing outages occurred.",
      "affected_reasoning_operation": "Project continuation decision under adverse evidence",
      "bias_specific_mechanism": "Previously invested cutover work made stopping feel like a loss; the decision was framed around avoiding waste rather than a rigorous comparison of future marginal costs and benefits.",
      "manifestation_in_interview": "The participant reported that reversing cutovers felt like wasting months of work and that sunk work was very present when deciding to continue.",
      "effect_on_reasoning_or_decision": "The participant continued the migration despite delays, integration bugs, and outages, with the sunk work and time pressure making continuing seem like the only path rather than the result of rigorous cost-benefit analysis.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We talked about pausing. But we'd already cut over two services, and reverting those felt like it would waste months of work. Given the timeline pressure too, continuing forward seemed like the only path that didn't throw away what we'd built.",
          "evidence_explanation": "This directly shows continuation being justified by irrecoverable past work rather than by a forward-looking analysis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not as rigorously as maybe I should have. The sunk work was very present in my mind at that moment.",
          "evidence_explanation": "The participant explicitly identifies sunk work as the salient factor and acknowledges insufficient rigor in comparing continuation against stopping."
        }
      ],
      "correction_or_counterevidence": "There was genuine hard deadline pressure, and reversing cutover services may have had real costs; the transcript does not provide a full cost-benefit calculation proving continuation was wrong, only that the participant's own emphasis was on sunk work rather than rigorous forward-looking analysis.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support was unavailable for this specific label; the label is applied from general cognitive-science knowledge rather than from retrieval.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus coverage was sparse for several identified labels, including availability bias, bandwagon effect, psychological reactance, and sunk cost fallacy.",
    "The analysis relies on participant self-report within a retrospective CTA interview and does not include independent verification of objective decision processes or outcomes."
  ]
}
