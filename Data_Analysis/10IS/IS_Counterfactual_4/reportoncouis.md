# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. Quick reminder — this is a cognitive task analysis interview, so I'm interested in how you reasoned through things, not in grading the outcome. You can decline any question. Okay to start? Participant: Sure, sounds good. Interviewer: Can you give me your role and a general sense of the project? Participant: I'm a UX designer on the product team at a B2B analytics company. Last year I led a redesign of our onboarding wizard, aiming to cut first-week drop-off. We had a twelve-week window that lined up with our quarterly product review — nothing contractual riding on it, just the usual expectation that we'd show some lift in activation rate. Interviewer: Twelve weeks is a decent runway. What made this project stand out otherwise? Participant: Mostly the scope — three flows needed real research, we needed outside build help, and there was a personalization system already running in the background that we wanted to lean on more. Interviewer: Walk me through how it played out from the start. Participant: Sure. Early on, three research vendor proposals came in. One was a cheap self-serve platform — six thousand dollars, five sessions, no synthesis, just raw recordings. Then two full-service options: twenty-one thousand for ten sessions with a written synthesis, and twenty-three thousand for twelve sessions plus dashboard integration and two follow-up rounds. I had plenty of time to sit with these, and I ended up going with the twenty-three thousand option. Interviewer: What drove that? Participant: When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it. Interviewer: Did you weigh the cheaper self-serve option against your actual scope — you only needed three flows validated? Participant: I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly. Interviewer: What came of that vendor choice? Participant: The findings were fine, though two of the twelve sessions turned out to duplicate internal data we already had. And the dashboard piece only half worked when it was delivered — I ended up patching a lot of it myself. Interviewer: Next stage? Participant: Hiring a contractor for the micro-interactions — transitions, progress indicators. Two candidates: one had flagship work at a well-known unicorn startup, gorgeous portfolio, but not much documented process. The other had a plainer portfolio but included actual test scripts, metrics, iteration logs. Interviewer: How did you choose, given you had time for a trial task if you wanted one? Participant: I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too. I did consider running a paid trial with both — we had the weeks for it — but it felt like an unnecessary step given his track record. Interviewer: Did you check the documentation and communication side directly? Participant: Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in. Interviewer: What happened with his deliverables? Participant: Beautiful interactions, but he skipped documenting the reasoning for two key transitions, and when the Head of Design asked for the testing basis later, there wasn't much to show her. Interviewer: Let's talk about the personalization engine. Participant: We had a small test running — about a hundred forty users — on the rules engine, and I'd manually tuned two onboarding rule weights that same week. Right after, the activation number ticked up on the dashboard. Interviewer: What did you take from that? Participant: That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it. Interviewer: Was there anything complicating that read? Participant: She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence. Interviewer: What happened afterward? Participant: The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed. Interviewer: Last stage — the legacy component. Participant: We'd put three sprints into customizing our old step-wizard component for the new flow. Then engineering flagged an accessibility defect and a rendering issue, and said a newer modular framework would fix both in about a sprint. We still had roughly six weeks left, so a one-sprint migration wouldn't have threatened the review date at all. Interviewer: What did you decide? Participant: I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare. Interviewer: Setting the prior sprints aside, how did the one-sprint estimate compare to continuing, on its own terms? Participant: Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me. Interviewer: What happened with the component? Participant: The accessibility issue came back up during QA before the review, and by then migrating would have cost more than the original estimate, since we'd layered on even more customization by that point. Interviewer: If Vendor B had been priced the same as Vendor C, would you have decided differently? Participant: Possibly — I might've actually gone back and checked whether we needed the top-tier package at all. Interviewer: If the second candidate's portfolio had come from a more recognizable company? Participant: Probably would have hired her instead. That recognition factor carried more weight than it should have. Interviewer: If the significance threshold had been strictly enforced before you could act? Participant: I'd have waited — we had the schedule for it, I just didn't want to lose momentum. Interviewer: And if none of those three sprints had already gone into the legacy component? Participant: No question, I'd have migrated right away given the defects. Interviewer: Last one — if this had been the original six-week sprint with the hard renewal deadline instead, do you think any of this would have gone differently? Participant: Maybe the vendor and hiring calls would've felt more forced. But honestly, looking back, I'm not sure the extra time changed as much as it should have — I still landed in mostly the same places. Interviewer: That's really helpful context. Thank you for walking through it so openly. Participant: No problem — easier to spot in hindsight than it was in the moment.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.84s · gen 140.67s · total 144.8s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0296 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0247 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0228 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0203 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0202 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0197 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0193 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
8. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0191 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0190 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0185 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
14. **Hallihan_etal_DTM_12.pdf** — 0.0175 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
15. **Hallihan_etal_DTM_12.pdf** — 0.0170 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
17. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0165 (rrf) — _# Experiment 2 e purpose of Experiment 2 was (a) to replicate the observation of Experiment 1 th_
19. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
20. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0164 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
21. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0163 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
22. **Hallihan_etal_DTM_12.pdf** — 0.0159 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
26. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0155 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0154 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 As a step towards studying human cognition in AIassist_
29. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0154 (rrf) — _# 3.4 \| Theme 2 measurement of cognitive bias answer - items were devised for each case. To str_
30. **ijcma-08-2012-0064.pdf** — 0.0153 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
31. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
32. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0150 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
33. **Hallihan_etal_DTM_12.pdf** — 0.0150 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# ( " = 0 . 44 ) . 188:18 Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos Third, our r_
35. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0149 (rrf) — _# ( " = 0 . 44 ) . Proc. ACM Hum.-Comput. Interact., Vol. 5, No. CSCW1, Article 188. Publication_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0148 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
38. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0148 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
39. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0147 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
40. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0147 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
41. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0146 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
42. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Technical Communication Make Decisions . https://www.nngroup.com/articles/_
43. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0146 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
44. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0145 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
46. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0140 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization , We collected all In_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0139 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
50. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0139 (rrf) — _## Cognitive Bias and Its Importance Cognitive bias is the tendency to The purpose of usability _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluated participant reasoning episodes across vendor selection, contractor hiring, personalization engine interpretation, and legacy component migration decisions."
  },
  "identified_bias_summary": [
    {
      "bias_label": "attraction effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
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
      "confidence": "moderate",
      "bias_label": "attraction effect",
      "alternative_labels": [
        "decoy effect",
        "asymmetric dominance effect",
        "contrast effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A decision bias in which adding a decoy option that is asymmetrically dominated by a target option increases preference for the target, because the target seems comparatively superior even though its absolute qualities are unchanged.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor selection for UX research",
      "decision_point_description": "Choice among three research vendor proposals: a self-serve package, a mid-tier full-service package, and a top-tier full-service package.",
      "affected_reasoning_operation": "Option evaluation and multi-attribute choice",
      "bias_specific_mechanism": "The participant evaluated the top full-service package mainly against the adjacent middle package. The middle package was dominated by the top package on the quoted features, making the top package appear clearly superior, while the cheaper self-serve package fell out of active consideration.",
      "manifestation_in_interview": "The participant explicitly said the contrast between the two full-service packages was what he was reacting to, and that the smaller self-serve option had fallen out of view even though it may have covered the scope.",
      "effect_on_reasoning_or_decision": "The participant chose the top-tier package without fully mapping the self-serve option to the actual scope. Later, two sessions duplicated internal data and the dashboard piece only partly worked.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it.",
          "evidence_explanation": "This shows the choice was framed as a local comparison between the two full-service packages rather than a full multi-option evaluation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.",
          "evidence_explanation": "This directly states that the contrast with the adjacent mid-tier package displaced evaluation of the self-serve option, which is the mechanism of the attraction effect."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly — I might've actually gone back and checked whether we needed the top-tier package at all.",
          "evidence_explanation": "This counterfactual response indicates that the presence or pricing of the middle package influenced the perceived need for the top package."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that the self-serve option probably could have covered the needed sessions and that the contrast between the two full-service packages was what drove his reaction. Findings later partly duplicated internal data and the dashboard integration only partly worked.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context addressed the attraction effect, decoy effect, or contrast effect; classification relies on established decision-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "halo effect",
      "alternative_labels": [
        "halo error"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which a positive impression in one domain influences perception of unrelated attributes in another domain.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor hiring for micro-interactions",
      "decision_point_description": "Choice between two contractor candidates: one with visually strong flagship work but little documented process, and one with direct evidence of testing and iteration.",
      "affected_reasoning_operation": "Personnel evaluation and inference under uncertainty",
      "bias_specific_mechanism": "The participant generalized from visual craft quality and company recognition to unrelated documentation and communication ability, without directly checking those attributes.",
      "manifestation_in_interview": "The participant hired the visually strong candidate and explicitly stated that he extended trust from the visual work to the rest, even though the other candidate's portfolio contained the needed evidence.",
      "effect_on_reasoning_or_decision": "The participant selected the candidate whose visual work was strongest, but later lacked documentation and testing rationale when the Head of Design requested it.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too.",
          "evidence_explanation": "This shows a positive impression in visual work was used to infer unrelated documentation and communication competence without direct evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in.",
          "evidence_explanation": "This explicitly describes the halo mechanism: trust generalized from visual work to the rest of the candidate's qualifications."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that the other candidate had exactly the needed documentation evidence, and the hired candidate skipped documenting reasoning for two key transitions.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context addressed the halo effect; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias",
        "myside bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall evidence in ways that confirm existing beliefs or expectations, while giving disproportionately less consideration to contradictory evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting activation metric after personalization adjustments",
      "decision_point_description": "Judgment about whether manual rule-weight adjustments caused an activation uptick and whether to request more manual control from the Analytics Lead.",
      "affected_reasoning_operation": "Causal attribution and evidence evaluation",
      "bias_specific_mechanism": "The participant had an existing expectation that his manual adjustments were working. He weighted the temporally coincident uptick as supporting evidence while underweighting warnings that the sample was below threshold and confounded by a marketing send.",
      "manifestation_in_interview": "The participant acknowledged the sample-size and confounding caveats but still treated the timing of the uptick as real evidence and requested more manual control.",
      "effect_on_reasoning_or_decision": "The participant acted on an unsupported causal inference by requesting more manual control. The activation bump later partly reversed once the email campaign ended, and the actual driver remained unconfirmed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it.",
          "evidence_explanation": "This shows the participant formed a confirming causal interpretation and took action based on it before the inference was validated."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.",
          "evidence_explanation": "This shows contradictory information was available but the participant continued to favor temporally coincident evidence, consistent with confirmation bias."
        }
      ],
      "correction_or_counterevidence": "The Analytics Lead flagged the sample size and marketing confound. Later, the bump partly reversed after the email campaign ended and the actual driver remained unconfirmed.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved Natesan et al. passage provided a direct definition of confirmation bias, supporting the identified mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": "Cognitive Bias in Usability Testing",
          "authors": "Natesan et al.",
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Confirmation Bias. The tendency for individuals to look for proof of their expectations rather than contradictory information.",
          "mechanism_supported_by_source": "The source defines confirmation bias as seeking proof of expectations instead of contradictory information.",
          "relevance_to_this_occurrence": "The participant interpreted the activation uptick as proof that his manual adjustments worked despite the Analytics Lead's contradictory warnings about sample size and confound."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "Concorde fallacy"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A decision bias in which previously invested resources are treated as a reason to continue a course of action, even when prospective evidence favors an alternative.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Legacy component migration decision",
      "decision_point_description": "Decision whether to keep customizing a legacy step-wizard component or migrate to a newer modular framework that would fix accessibility and rendering issues in about one sprint.",
      "affected_reasoning_operation": "Project decision under prospective cost-benefit comparison",
      "bias_specific_mechanism": "The participant treated the three prior sprints of customization as a reason to continue customizing, even though a one-sprint migration was available with enough schedule remaining.",
      "manifestation_in_interview": "The participant argued to keep the legacy component because three sprints had already been sunk and switching felt like giving that up.",
      "effect_on_reasoning_or_decision": "The participant continued customizing the legacy component. The accessibility issue returned before review, and migration later became more expensive than the original estimate.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "We'd put three sprints into customizing our old step-wizard component for the new flow. Then engineering flagged an accessibility defect and a rendering issue, and said a newer modular framework would fix both in about a sprint. We still had roughly six weeks left, so a one-sprint migration wouldn't have threatened the review date at all.",
          "evidence_explanation": "This establishes that a viable, lower-cost prospective alternative existed with adequate schedule slack."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare.",
          "evidence_explanation": "This directly shows the prior investment was used as a justification for continuing, which is the sunk cost mechanism."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.",
          "evidence_explanation": "This confirms that the prospective comparison favored the alternative, but the past investment distorted the decision process."
        }
      ],
      "correction_or_counterevidence": "Engineering proposed a one-sprint migration with six weeks remaining. The accessibility issue recurred before review, and migration later cost more than the original estimate after further customization.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context addressed sunk cost fallacy or escalation of commitment; classification relies on established judgment-and-decision-making knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "insensitivity to sample size",
      "alternative_labels": [
        "belief in law of small numbers",
        "sample size neglect"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Interpreting activation metric after personalization adjustments",
      "supporting_interview_quote": "She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.",
      "plausible_mechanism": "The participant drew a causal conclusion from a small, below-threshold sample, possibly due to insensitivity to sample size or belief in the law of small numbers.",
      "why_not_identified": "This is tightly intertwined with the identified confirmation bias in the same evidence-evaluation episode and cannot be cleanly separated as an independent distortion; the participant's own account emphasizes needing to see his adjustments as effective."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis uses the participant's retrospective account, which may itself be shaped by hindsight and self-presentation.",
    "Several episodes contain overlapping reasoning mechanisms; boundaries were drawn conservatively based on the most clearly evidenced primary mechanism.",
    "Retrieved corpus support was available for confirmation bias only; the remaining classifications rely on established cognitive-science knowledge."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. Quick reminder — this is a cognitive task analysis interview, so I'm interested in how you reasoned through things, not in grading the outcome. You can decline any question. Okay to start? Participant: Sure, sounds good. Interviewer: Can you give me your role and a general sense of the project? Participant: I'm a UX designer on the product team at a B2B analytics company. Last year I led a redesign of our onboarding wizard, aiming to cut first-week drop-off. We had a twelve-week window that lined up with our quarterly product review — nothing contractual riding on it, just the usual expectation that we'd show some lift in activation rate. Interviewer: Twelve weeks is a decent runway. What made this project stand out otherwise? Participant: Mostly the scope — three flows needed real research, we needed outside build help, and there was a personalization system already running in the background that we wanted to lean on more. Interviewer: Walk me through how it played out from the start. Participant: Sure. Early on, three research vendor proposals came in. One was a cheap self-serve platform — six thousand dollars, five sessions, no synthesis, just raw recordings. Then two full-service options: twenty-one thousand for ten sessions with a written synthesis, and twenty-three thousand for twelve sessions plus dashboard integration and two follow-up rounds. I had plenty of time to sit with these, and I ended up going with the twenty-three thousand option. Interviewer: What drove that? Participant: When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it. Interviewer: Did you weigh the cheaper self-serve option against your actual scope — you only needed three flows validated? Participant: I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly. Interviewer: What came of that vendor choice? Participant: The findings were fine, though two of the twelve sessions turned out to duplicate internal data we already had. And the dashboard piece only half worked when it was delivered — I ended up patching a lot of it myself. Interviewer: Next stage? Participant: Hiring a contractor for the micro-interactions — transitions, progress indicators. Two candidates: one had flagship work at a well-known unicorn startup, gorgeous portfolio, but not much documented process. The other had a plainer portfolio but included actual test scripts, metrics, iteration logs. Interviewer: How did you choose, given you had time for a trial task if you wanted one? Participant: I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too. I did consider running a paid trial with both — we had the weeks for it — but it felt like an unnecessary step given his track record. Interviewer: Did you check the documentation and communication side directly? Participant: Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in. Interviewer: What happened with his deliverables? Participant: Beautiful interactions, but he skipped documenting the reasoning for two key transitions, and when the Head of Design asked for the testing basis later, there wasn't much to show her. Interviewer: Let's talk about the personalization engine. Participant: We had a small test running — about a hundred forty users — on the rules engine, and I'd manually tuned two onboarding rule weights that same week. Right after, the activation number ticked up on the dashboard. Interviewer: What did you take from that? Participant: That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it. Interviewer: Was there anything complicating that read? Participant: She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence. Interviewer: What happened afterward? Participant: The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed. Interviewer: Last stage — the legacy component. Participant: We'd put three sprints into customizing our old step-wizard component for the new flow. Then engineering flagged an accessibility defect and a rendering issue, and said a newer modular framework would fix both in about a sprint. We still had roughly six weeks left, so a one-sprint migration wouldn't have threatened the review date at all. Interviewer: What did you decide? Participant: I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare. Interviewer: Setting the prior sprints aside, how did the one-sprint estimate compare to continuing, on its own terms? Participant: Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me. Interviewer: What happened with the component? Participant: The accessibility issue came back up during QA before the review, and by then migrating would have cost more than the original estimate, since we'd layered on even more customization by that point. Interviewer: If Vendor B had been priced the same as Vendor C, would you have decided differently? Participant: Possibly — I might've actually gone back and checked whether we needed the top-tier package at all. Interviewer: If the second candidate's portfolio had come from a more recognizable company? Participant: Probably would have hired her instead. That recognition factor carried more weight than it should have. Interviewer: If the significance threshold had been strictly enforced before you could act? Participant: I'd have waited — we had the schedule for it, I just didn't want to lose momentum. Interviewer: And if none of those three sprints had already gone into the legacy component? Participant: No question, I'd have migrated right away given the defects. Interviewer: Last one — if this had been the original six-week sprint with the hard renewal deadline instead, do you think any of this would have gone differently? Participant: Maybe the vendor and hiring calls would've felt more forced. But honestly, looking back, I'm not sure the extra time changed as much as it should have — I still landed in mostly the same places. Interviewer: That's really helpful context. Thank you for walking through it so openly. Participant: No problem — easier to spot in hindsight than it was in the moment.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.65s · gen 115.07s · total 118.9s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0296 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0247 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0228 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0203 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0202 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0197 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0193 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
8. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0191 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0190 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0185 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
14. **Hallihan_etal_DTM_12.pdf** — 0.0175 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
15. **Hallihan_etal_DTM_12.pdf** — 0.0170 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
17. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0165 (rrf) — _# Experiment 2 e purpose of Experiment 2 was (a) to replicate the observation of Experiment 1 th_
19. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
20. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0164 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
21. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0163 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
22. **Hallihan_etal_DTM_12.pdf** — 0.0159 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
26. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0155 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0154 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 As a step towards studying human cognition in AIassist_
29. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0154 (rrf) — _# 3.4 \| Theme 2 measurement of cognitive bias answer - items were devised for each case. To str_
30. **ijcma-08-2012-0064.pdf** — 0.0153 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
31. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
32. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0150 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
33. **Hallihan_etal_DTM_12.pdf** — 0.0150 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# ( " = 0 . 44 ) . 188:18 Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos Third, our r_
35. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0149 (rrf) — _# ( " = 0 . 44 ) . Proc. ACM Hum.-Comput. Interact., Vol. 5, No. CSCW1, Article 188. Publication_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0148 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
38. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0148 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
39. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0147 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
40. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0147 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
41. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0146 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
42. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Technical Communication Make Decisions . https://www.nngroup.com/articles/_
43. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0146 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
44. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0145 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
46. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0140 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization , We collected all In_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0139 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
50. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0139 (rrf) — _## Cognitive Bias and Its Importance Cognitive bias is the tendency to The purpose of usability _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of the participant's reported reasoning about vendor selection, contractor hiring, personalization-engine interpretation, and legacy-component migration."
  },
  "identified_bias_summary": [
    {
      "bias_label": "confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "contrast effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
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
      "bias_label": "contrast effect",
      "alternative_labels": ["context effect", "decoy effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to evaluate an option relative to adjacent comparison options rather than against independent, task-relevant criteria, so the same option can appear more or less attractive depending on the comparison set.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor selection for onboarding research",
      "decision_point_description": "Choosing among three research vendor proposals: a low-cost self-serve package, a mid-tier full-service package, and a top-tier full-service package.",
      "affected_reasoning_operation": "Comparative evaluation and choice among vendor packages",
      "bias_specific_mechanism": "The top-tier package was evaluated against the adjacent mid-tier package, making it appear especially strong; the self-serve option was then insufficiently compared against actual project scope.",
      "manifestation_in_interview": "The participant reported that once the two full-service packages were compared side-by-side, the top package looked clearly better and the cheaper option fell out of view.",
      "effect_on_reasoning_or_decision": "Led to selection of the top-tier package and omitted a scope-based evaluation of the cheaper self-serve option that might have covered the project needs.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it.",
          "evidence_explanation": "Shows the choice was shaped by comparison between adjacent options rather than by absolute fit with research needs."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.",
          "evidence_explanation": "Explicitly identifies the contrast-driven reasoning and acknowledges the self-serve option was neglected despite time to evaluate it properly."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged having enough time to compare the self-serve option to actual scope but did not; later outcome information about duplicated sessions and a partly working dashboard is retrospective and does not negate the initial mechanism.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derives from general knowledge because retrieved corpus support for contrast/context effects was not available.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "halo effect",
      "alternative_labels": ["representativeness heuristic", "overgeneralization"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency for a salient positive impression or attribute to influence judgments about unrelated attributes of the same person or thing.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor selection for micro-interactions",
      "decision_point_description": "Choosing between a candidate with strong visual work from a recognizable company and a candidate with documented testing and iteration process.",
      "affected_reasoning_operation": "Inference and candidate evaluation",
      "bias_specific_mechanism": "A positive visible trait, strong visual portfolio work from a well-known company, was generalized to unobserved documentation and communication competence without direct evidence.",
      "manifestation_in_interview": "The participant selected the visually impressive candidate on the assumption that high-caliber visual work would extend to process habits, and explicitly said he extended trust from visual work to the rest.",
      "effect_on_reasoning_or_decision": "Led to hiring a contractor whose lack of documented reasoning later created a gap, while the candidate with direct process evidence was not selected.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too.",
          "evidence_explanation": "Shows a specific positive attribute was used to infer unrelated desirable attributes without checking them."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in.",
          "evidence_explanation": "Directly states the overgeneralization from visual work to other competencies, and acknowledges that relevant evidence in the other portfolio was underweighted."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that the other candidate's portfolio contained the needed evidence; this retrospect does not eliminate the initial halo-based inference.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derives from general knowledge because retrieved corpus support for halo effect was not available.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": ["motivated reasoning"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to seek, interpret, or weight information in ways that support an existing expectation or hypothesis while underweighting contradictory information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting activation uptick after manual rule-weight tuning",
      "decision_point_description": "Deciding whether to pursue more manual control based on an activation increase from a small, confounded sample.",
      "affected_reasoning_operation": "Causal interpretation and decision to request additional manual control",
      "bias_specific_mechanism": "The participant treated the timing of the activation uptick as confirmatory evidence for his manual-tuning hypothesis while downplaying the Analytics Lead's warning about small sample size and a concurrent marketing send.",
      "manifestation_in_interview": "Despite acknowledging the statistical and confound concerns, the participant felt the timing was real evidence and requested more manual control to continue.",
      "effect_on_reasoning_or_decision": "Produced action on an unconfirmed causal link; the bump later partly reversed and the actual driver remained unconfirmed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it.",
          "evidence_explanation": "Shows the uptick was interpreted as evidence supporting the participant's existing hypothesis that his manual changes had worked."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.",
          "evidence_explanation": "Demonstrates that contradictory information was available and acknowledged, but the participante still favored confirmatory temporal evidence."
        }
      ],
      "correction_or_counterevidence": "The Analytics Lead supplied disconfirming information, and the participant acknowledged time was available for a larger or isolated test. The activation bump later partly reversed after the email campaign ended.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism supported by the retrieved corpus passage from natesan et al. (2016).",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Confirmation Bias. The tendency for individuals to look for proof of their expectations rather than contradictory information.",
          "mechanism_supported_by_source": "Defines confirmation bias as weighting proof of expectations over contradictory information.",
          "relevance_to_this_occurrence": "The participant treated a temporally coincident activation uptick as real evidence for his manual-tuning effect while downplaying the Analytics Lead's contradictory flags."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": ["escalation of commitment"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue a course of action because of previously invested resources, even when those investments are irrecoverable and future prospects favor a different course.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Legacy step-wizard component decision",
      "decision_point_description": "Choosing between continuing to customize a legacy component and migrating to a newer framework that would fix known defects in about one sprint.",
      "affected_reasoning_operation": "Project decision under cost-benefit alternatives",
      "bias_specific_mechanism": "Prior investment of three sprints was treated as a reason to continue customizing the legacy component, even though those sunk costs were not recoverable and the future-oriented comparison favored migration.",
      "manifestation_in_interview": "The participant argued to keep customizing because three sprints had already been spent and switching felt like giving that up, despite time to spare.",
      "effect_on_reasoning_or_decision": "Continued on the legacy path; the accessibility issue later recurred during QA and migration became more expensive after additional customization.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare.",
          "evidence_explanation": "Shows the decision to continue was based on irrecoverable past investment rather than future cost and benefit."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.",
          "evidence_explanation": "Acknowledges that the forward-looking comparison favored migration, while the sunk sprints still biased the choice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No question, I'd have migrated right away given the defects.",
          "evidence_explanation": "Counterfactual evidence that without the prior spent sprints, the participant would have chosen migration, supporting sunk-cost-specific reasoning."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledges the migration estimate was probably better on its own terms and says that with no prior sprints he would have migrated immediately.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label derives from general knowledge because retrieved corpus support for sunk cost fallacy was not available.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus support was sparse; only confirmation bias had an applicable retrieved passage.",
    "The analysis relies on retrospective self-report, so mechanisms are inferred from the participant's descriptions rather than direct observation.",
    "The interviewer's counterfactual prompts may shape later statements, though identified mechanisms are based on affirmative participant descriptions of reasoning."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. Quick reminder — this is a cognitive task analysis interview, so I'm interested in how you reasoned through things, not in grading the outcome. You can decline any question. Okay to start? Participant: Sure, sounds good. Interviewer: Can you give me your role and a general sense of the project? Participant: I'm a UX designer on the product team at a B2B analytics company. Last year I led a redesign of our onboarding wizard, aiming to cut first-week drop-off. We had a twelve-week window that lined up with our quarterly product review — nothing contractual riding on it, just the usual expectation that we'd show some lift in activation rate. Interviewer: Twelve weeks is a decent runway. What made this project stand out otherwise? Participant: Mostly the scope — three flows needed real research, we needed outside build help, and there was a personalization system already running in the background that we wanted to lean on more. Interviewer: Walk me through how it played out from the start. Participant: Sure. Early on, three research vendor proposals came in. One was a cheap self-serve platform — six thousand dollars, five sessions, no synthesis, just raw recordings. Then two full-service options: twenty-one thousand for ten sessions with a written synthesis, and twenty-three thousand for twelve sessions plus dashboard integration and two follow-up rounds. I had plenty of time to sit with these, and I ended up going with the twenty-three thousand option. Interviewer: What drove that? Participant: When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it. Interviewer: Did you weigh the cheaper self-serve option against your actual scope — you only needed three flows validated? Participant: I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly. Interviewer: What came of that vendor choice? Participant: The findings were fine, though two of the twelve sessions turned out to duplicate internal data we already had. And the dashboard piece only half worked when it was delivered — I ended up patching a lot of it myself. Interviewer: Next stage? Participant: Hiring a contractor for the micro-interactions — transitions, progress indicators. Two candidates: one had flagship work at a well-known unicorn startup, gorgeous portfolio, but not much documented process. The other had a plainer portfolio but included actual test scripts, metrics, iteration logs. Interviewer: How did you choose, given you had time for a trial task if you wanted one? Participant: I went with the first candidate. His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too. I did consider running a paid trial with both — we had the weeks for it — but it felt like an unnecessary step given his track record. Interviewer: Did you check the documentation and communication side directly? Participant: Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in. Interviewer: What happened with his deliverables? Participant: Beautiful interactions, but he skipped documenting the reasoning for two key transitions, and when the Head of Design asked for the testing basis later, there wasn't much to show her. Interviewer: Let's talk about the personalization engine. Participant: We had a small test running — about a hundred forty users — on the rules engine, and I'd manually tuned two onboarding rule weights that same week. Right after, the activation number ticked up on the dashboard. Interviewer: What did you take from that? Participant: That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it. Interviewer: Was there anything complicating that read? Participant: She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence. Interviewer: What happened afterward? Participant: The bump partly reversed once the email campaign ended, and she noted the actual driver was still unconfirmed. Interviewer: Last stage — the legacy component. Participant: We'd put three sprints into customizing our old step-wizard component for the new flow. Then engineering flagged an accessibility defect and a rendering issue, and said a newer modular framework would fix both in about a sprint. We still had roughly six weeks left, so a one-sprint migration wouldn't have threatened the review date at all. Interviewer: What did you decide? Participant: I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare. Interviewer: Setting the prior sprints aside, how did the one-sprint estimate compare to continuing, on its own terms? Participant: Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me. Interviewer: What happened with the component? Participant: The accessibility issue came back up during QA before the review, and by then migrating would have cost more than the original estimate, since we'd layered on even more customization by that point. Interviewer: If Vendor B had been priced the same as Vendor C, would you have decided differently? Participant: Possibly — I might've actually gone back and checked whether we needed the top-tier package at all. Interviewer: If the second candidate's portfolio had come from a more recognizable company? Participant: Probably would have hired her instead. That recognition factor carried more weight than it should have. Interviewer: If the significance threshold had been strictly enforced before you could act? Participant: I'd have waited — we had the schedule for it, I just didn't want to lose momentum. Interviewer: And if none of those three sprints had already gone into the legacy component? Participant: No question, I'd have migrated right away given the defects. Interviewer: Last one — if this had been the original six-week sprint with the hard renewal deadline instead, do you think any of this would have gone differently? Participant: Maybe the vendor and hiring calls would've felt more forced. But honestly, looking back, I'm not sure the extra time changed as much as it should have — I still landed in mostly the same places. Interviewer: That's really helpful context. Thank you for walking through it so openly. Participant: No problem — easier to spot in hindsight than it was in the moment.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.64s · gen 129.01s · total 132.8s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0296 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0247 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0228 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0203 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0202 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
6. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0197 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0193 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
8. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0191 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0190 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0189 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0185 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0180 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
14. **Hallihan_etal_DTM_12.pdf** — 0.0175 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
15. **Hallihan_etal_DTM_12.pdf** — 0.0170 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
16. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0167 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
17. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
18. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0165 (rrf) — _# Experiment 2 e purpose of Experiment 2 was (a) to replicate the observation of Experiment 1 th_
19. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
20. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0164 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
21. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0163 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
22. **Hallihan_etal_DTM_12.pdf** — 0.0159 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
23. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_
24. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0156 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
25. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
26. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0155 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
27. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0155 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
28. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0154 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 As a step towards studying human cognition in AIassist_
29. **Journal of Clinical Nursing - 2023 - Jala - Cognitive bias during clinical decision‐making and its influence on patient.pdf** — 0.0154 (rrf) — _# 3.4 \| Theme 2 measurement of cognitive bias answer - items were devised for each case. To str_
30. **ijcma-08-2012-0064.pdf** — 0.0153 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
31. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study anchor. Anchoring bias is_
32. **Malberg et al. (2024) A comprehensive evaluation of cognitive biases in LLMs.pdf** — 0.0150 (rrf) — _# A Comprehensive Evaluation of Cognitive Biases in LLMs opinions when presented with new eviden_
33. **Hallihan_etal_DTM_12.pdf** — 0.0150 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
34. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0150 (rrf) — _# ( " = 0 . 44 ) . 188:18 Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos Third, our r_
35. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0149 (rrf) — _# ( " = 0 . 44 ) . Proc. ACM Hum.-Comput. Interact., Vol. 5, No. CSCW1, Article 188. Publication_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0148 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
38. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0148 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
39. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0147 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
40. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0147 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
41. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0146 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
42. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0146 (rrf) — _# Cognitive Biases in Technical Communication Make Decisions . https://www.nngroup.com/articles/_
43. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0146 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
44. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0145 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0141 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
46. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0140 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization , We collected all In_
47. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0139 (rrf) — _# 188 | to the one in the | explanation condition). Informed by prior work that a slow algorithm_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
49. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
50. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0139 (rrf) — _## Cognitive Bias and Its Importance Cognitive bias is the tendency to The purpose of usability _

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Mechanism-first review of participant reasoning in a CTA interview. Four bias occurrences were identified from the participant's explicit reasoning admissions. Retrieved corpus passages did not directly support the specific labels identified, so labels rest on general cognitive-science knowledge."
  },
  "identified_bias_summary": [
    {
      "bias_label": "decoy effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "halo effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "illusion of causality",
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
      "bias_label": "decoy effect",
      "alternative_labels": ["attraction effect", "asymmetric dominance effect", "contrast effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A choice bias in which the presence of a third, less attractive option makes one of the other options appear disproportionately appealing; here the middle full-service package functioned as the comparison point that made the top-tier package look like an obvious step up.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Research vendor selection",
      "decision_point_description": "Selection among a low-cost self-serve platform, a mid-tier full-service package, and a top-tier full-service package.",
      "affected_reasoning_operation": "Evaluating and choosing among research vendor proposals against project scope.",
      "bias_specific_mechanism": "Local side-by-side comparison with the middle package dominated the evaluation; the top package's incremental features were judged relative to the middle package rather than against the project's actual need, causing the smaller self-serve option to be excluded from consideration.",
      "manifestation_in_interview": "When comparing the $21k and $23k full-service packages, the participant described the middle package as thin and the top package as an obvious choice. He acknowledged the cheaper self-serve option fell out of view and that he reacted to the contrast rather than mapping it against scope.",
      "effect_on_reasoning_or_decision": "He chose the $23k package without fully assessing whether the low-cost option satisfied the session needs; later two sessions duplicated internal data and dashboard integration was only partially functional.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I put the twenty-one and twenty-three side by side, it wasn't a close call — two more sessions, dashboard hookup, follow-ups included, for two grand more. The middle package just looked thin next to it.",
          "evidence_explanation": "Directly shows the side-by-side comparison making the top package look more attractive because the middle package served as a weak comparison point."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I looked at it briefly. It probably could have covered what we needed session-count-wise. But by the time I was comparing the two full packages, that smaller option had sort of fallen out of view — the contrast between the other two was what I was reacting to, even though I had the runway to sit down and actually map Vendor A against the scope properly.",
          "evidence_explanation": "Confirms that the comparison-driven mechanism displaced scope-based evaluation of the cheaper self-serve option."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Possibly — I might've actually gone back and checked whether we needed the top-tier package at all.",
          "evidence_explanation": "Counterfactual admission that if the middle comparison were neutralized, the top-tier choice was no longer obvious, supporting the comparison-driven bias."
        }
      ],
      "correction_or_counterevidence": "Participant acknowledged the low-cost option could have sufficed and later noted two sessions duplicated internal data and the dashboard was only half-working.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed decoy/attraction/contrast-driven vendor choice; label and mechanism are grounded in general decision-making literature.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "halo effect",
      "alternative_labels": ["halo bias", "prestige bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency for a positive global impression or salient positive feature to spill over into evaluations of unrelated attributes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor selection",
      "decision_point_description": "Choosing between a candidate with prestigious flagship work and a candidate with explicit process evidence.",
      "affected_reasoning_operation": "Evaluating contractor documentation, communication, and process capabilities alongside visual and company prestige.",
      "bias_specific_mechanism": "A positive impression from the recognizable company and visually polished portfolio generalized to independent traits—documentation, communication, and process discipline—without direct verification.",
      "manifestation_in_interview": "He chose the first candidate because his shipped work at a well-known company was the caliber the team wanted, assumed that operating at that level naturally included solid documentation, declined a paid trial, and admitted extending trust from visual work to the rest of the candidate's abilities.",
      "effect_on_reasoning_or_decision": "Hired a candidate who later lacked documented reasoning for two key transitions. When the Head of Design asked for the testing basis, there was not much to show.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "His shipped work at that company was the caliber we wanted, and I figured someone operating at that level would naturally bring solid documentation and communication habits too.",
          "evidence_explanation": "Shows the global positive impression from company prestige being used to infer unrelated competencies."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I did consider running a paid trial with both — we had the weeks for it — but it felt like an unnecessary step given his track record.",
          "evidence_explanation": "Shows the halo reduced the perceived need to collect direct evidence on documentation and communication."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really. I extended trust from the visual work to the rest of it. Looking back, the other candidate's portfolio had exactly the evidence we needed, but it didn't carry the same weight walking in.",
          "evidence_explanation": "Explicit admission of halo-based generalization and underweighting of direct evidence from the other candidate."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably would have hired her instead. That recognition factor carried more weight than it should have.",
          "evidence_explanation": "Counterfactual admission that recognizable-company prestige drove the decision beyond its informative value."
        }
      ],
      "correction_or_counterevidence": "The other candidate's portfolio contained the needed process evidence; participant acknowledged the recognition factor carried too much weight, but only after the decision.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed halo effects in hiring or contractor evaluation; label and mechanism are grounded in general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "illusion of causality",
      "alternative_labels": ["causal illusion", "illusory correlation", "post hoc ergo propter hoc"],
      "taxonomy_status": "established_label",
      "bias_definition": "Perceiving a causal relationship between an action and an outcome based on temporal contiguity or salience, while underweighting confounds and sample limitations.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpreting personalization engine activation bump",
      "decision_point_description": "After manual tuning of two rule weights, the activation metric ticked up; participant decided to request more manual control.",
      "affected_reasoning_operation": "Causal attribution of activation metric movement to the participant's manual tuning changes.",
      "bias_specific_mechanism": "Temporal contiguity between the participant's tuning activities and an uptick in the activation metric fostered a causal attribution, while insufficient sample size and a concurrent marketing send were acknowledged but not integrated into the decision.",
      "manifestation_in_interview": "The participant interpreted the activation bump as evidence that his adjustments were working and requested more manual control, even though the Analytics Lead had flagged that the sample was under the significance threshold and the changes had not been isolated from other events.",
      "effect_on_reasoning_or_decision": "He asked the Analytics Lead for more manual control to keep pushing on the tuning. The bump partly reversed once the email campaign ended, and the actual driver remained unconfirmed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "That my adjustments were doing something. I asked the Analytics Lead for more manual control so I could keep pushing on it.",
          "evidence_explanation": "Shows that a causal inference led directly to a resource-control action."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She flagged that the sample was under our significance threshold, and that we hadn't isolated my changes from other things happening — there was a marketing send running the same week. I registered that, and honestly, we had time to just wait for a bigger sample or run an isolated test. But the timing lined up so well with what I'd changed that it felt like real evidence.",
          "evidence_explanation": "Directly demonstrates temporal contiguity overriding statistical caution, the core mechanism of causal illusion."
        }
      ],
      "correction_or_counterevidence": "The Analytics Lead flagged the insufficient sample and concurrent marketing send; the bump partly reversed after the email campaign ended, and the actual driver was still unconfirmed.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed causal illusion from temporal contiguity in dashboard metrics; label and mechanism are grounded in general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": ["sunk cost effect", "escalation of commitment"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue with an endeavor because of previously invested resources rather than a forward-looking comparison of future costs and benefits.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Legacy component migration decision",
      "decision_point_description": "Engineering recommended a one-sprint migration to a modular framework to fix defects; participant argued to continue customizing the legacy component.",
      "affected_reasoning_operation": "Deciding whether to migrate from a customized legacy component to a newer modular framework.",
      "bias_specific_mechanism": "Prior three sprints were experienced as losses that would be sacrificed by switching, so switching was evaluated as giving up prior investment rather than as a forward-looking choice based on future costs and benefits.",
      "manifestation_in_interview": "He argued to keep customizing the legacy piece because the team had already sunk three sprints into it, and switching felt like giving that up, even with time to spare. He admitted that, setting the prior sprints aside, the one-sprint migration was probably better.",
      "effect_on_reasoning_or_decision": "He continued customizing the legacy component. The accessibility issue came back during QA before the review, and by then migration would have cost more than the original estimate because more customization had been layered on.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I argued to keep customizing the legacy piece. We'd already sunk three sprints in, and switching felt like giving that up, even with time to spare.",
          "evidence_explanation": "Explicitly states a sunk-cost rationale: prior investment treated as a reason to continue rather than evaluate the switch independently."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably better, if I'm honest. But it was hard to treat the three sprints as separate from the decision in front of me.",
          "evidence_explanation": "Shows the forward-looking evaluation favored migration, but sunk-cost framing prevented treating it separately."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No question, I'd have migrated right away given the defects.",
          "evidence_explanation": "Counterfactual confirms that without the prior three sprints, the participant would have made a different decision, isolating prior investment as the operative mechanism."
        }
      ],
      "correction_or_counterevidence": "Engineering provided a one-sprint migration estimate that would fit the remaining schedule; participant later acknowledged migration was probably better on its own terms.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed sunk cost fallacy in project continuation decisions; label and mechanism are grounded in general decision-making literature.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved RAG context did not include passages on decoy effect, halo effect, illusion of causality, or sunk cost fallacy; these labels rest on general knowledge rather than retrieved corpus support.",
    "The interview is retrospective self-report, so some differentiation between bias-specific mechanisms and post-hoc narration is inherently limited.",
    "No observational or archival data were available to cross-check participant accounts of the decisions and outcomes."
  ]
}

