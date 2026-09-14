# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through a specific project, not whether the outcome was good or bad. Everything you share stays with the research team, and you can skip anything you'd rather not discuss. Sound okay? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role and give me a general sense of the project we're going to talk about? Participant: Sure, I'm a UX designer on the product team at an analytics SaaS company. Back in Q4 we had a six-week window to redesign our onboarding wizard before a big client renewal review. Leadership wanted to see a real bump in activation rate going into that meeting, so there was a lot riding on it. Interviewer: What made this project different from a routine update? Participant: Normally we'd have more runway — like a full quarter. This one was compressed, and the budget for outside help was capped, so every dollar and every hour had to be justified. Engineering could only give us maybe one and a half people. It was tight. Interviewer: Walk me through how it unfolded, from the start. Participant: So the first thing on my plate was research. We knew the wizard's drop-off was concentrated in three flows, and I needed outside eyes on it fast. I got three vendor proposals in the same week. One was a cheap self-serve platform, six grand, five sessions, but basically no synthesis — you get raw recordings and that's it. Then there were two full-service options: one at twenty-one thousand for ten sessions with a written synthesis, and another at twenty-three for twelve sessions plus dashboard integration and two follow-up rounds. I ended up going with the twenty-three thousand one. Interviewer: What tipped it that direction? Participant: Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. For two grand more you got two more sessions, the dashboard hookup, and follow-ups baked in. The middle option just looked like a worse version of the top one at almost the same price. It felt like an easy call. Interviewer: Did you look closely at whether the cheaper self-serve option would've covered what you actually needed? Participant: I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from. Interviewer: Got it. What happened after you picked that vendor? Participant: The findings were usable, but we later realized two of the twelve sessions basically repeated data we already had internally. And the dashboard integration they promised only half worked at delivery, so I had to patch a lot of that manually anyway. Interviewer: Let's move to the next stage. What came after research? Participant: We needed a contractor to build the actual micro-interactions for the new flow — transitions, progress indicators, that kind of thing. Two candidates were shortlisted. One, let's call him Candidate X, had done flagship interaction work at a pretty well-known unicorn startup — gorgeous portfolio. The other, Candidate Y, had a less flashy portfolio but included actual test scripts, metrics, iteration logs, the whole documented process. Interviewer: What made you choose between them? Participant: I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. It seemed like a safe bet given where he'd come from. Interviewer: Did you verify that documentation and communication piece directly — maybe ask for writing samples or how he'd handled testing on past projects? Participant: Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall. Interviewer: How did that play out? Participant: The micro-interactions themselves were beautiful. But he skipped documenting the reasoning behind two key transitions, and when the Head of Design asked for the testing basis, there wasn't really anything to show her. Interviewer: Let's talk about the third stage — the personalization engine. Participant: Right, so in parallel we were running a small test on the rules engine — about a hundred forty users — and I'd manually adjusted two of the onboarding rule weights that same week. The activation numbers on the dashboard ticked up right after. Interviewer: What did you make of that? Participant: I took it as a sign the adjustments were working. I went to the Data lead and asked to expand my manual tuning authority so I could keep pushing on it before the renewal review. Interviewer: Was there anything at the time that complicated that read? Participant: She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver. Interviewer: What happened the following week? Participant: The uptick partly reversed once the email campaign ended, and she noted the causal driver was still unconfirmed. So it's genuinely unclear how much of that first bump was actually the rule changes. Interviewer: Last stage — tell me about the legacy component decision. Participant: We'd spent three sprints customizing our old step-wizard component to fit the new flow. Then engineering flagged an accessibility defect and a rendering performance issue, and said a newer modular framework would fix both in about a sprint. Interviewer: What did you decide? Participant: I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us. Interviewer: Setting aside the sprints already spent, how did the one-sprint migration estimate compare on its own terms to continuing? Participant: If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built. Interviewer: What ended up happening with that component? Participant: The accessibility issue surfaced again during the pre-renewal QA pass, and by then the migration would've cost more than the original estimate because we'd layered on even more customization in the meantime. Interviewer: If Vendor B had been priced the same as Vendor C, would you have chosen differently? Participant: Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all. Interviewer: If Candidate Y's portfolio had come from a more recognizable company, would the hiring call have gone differently? Participant: Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have. Interviewer: And if the significance threshold had been strictly enforced before you could act on the rules engine data? Participant: I'd have waited, or at least run the isolated test first. I just didn't want to lose the momentum. Interviewer: Last one — if none of the three sprints had already gone into the legacy component, would you still have kept it? Participant: No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back. Interviewer: This has been really useful. Thank you for being so candid about where things were uncertain. Participant: Of course — it's easier to see some of this clearly now than it was in the middle of the sprint.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.23s · gen 143.11s · total 148.0s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0265 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0229 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0221 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0218 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
5. **Hallihan_etal_DTM_12.pdf** — 0.0216 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0202 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
7. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0193 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0190 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0183 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Hallihan_etal_DTM_12.pdf** — 0.0175 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
15. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0174 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0174 (rrf) — _# Experiment 2 e purpose of Experiment 2 was (a) to replicate the observation of Experiment 1 th_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0169 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
18. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0163 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
21. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
22. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
23. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0161 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study First, experiments are cl_
24. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
25. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0159 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0159 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
27. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _prototyping (Viswanathan & Linsey, 2011). However, cognitive heuristics and biases have been stu_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
30. **Hallihan_etal_DTM_12.pdf** — 0.0155 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
31. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0155 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
32. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
33. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
34. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Technical Communication Make Decisions . https://www.nngroup.com/articles/_
35. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0153 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
37. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0150 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization , We collected all In_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
40. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0149 (rrf) — _# 4Discussion - - viewing CFFs as more cognitively demanding. Although coming at the cost of use_
41. **Hallihan_etal_DTM_12.pdf** — 0.0146 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
42. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0145 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
43. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0144 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 As a step towards studying human cognition in AIassist_
44. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0143 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
46. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0143 (rrf) — _# ( " = 0 . 44 ) . 188:18 Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos Third, our r_
47. **Hallihan_etal_DTM_12.pdf** — 0.0142 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
49. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0141 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Evaluation restricted to transcribed reasoning episodes; retrieved passages are used only where they directly support a classified mechanism."
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
      "confidence": "low",
      "bias_label": "attraction effect",
      "alternative_labels": [
        "asymmetric dominance effect",
        "decoy effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The attraction effect occurs when the presence of a relatively worse but similar option makes a target option appear more attractive, shifting evaluation away from absolute requirements toward local contrast.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor selection for usability research",
      "decision_point_description": "Choose among three vendor proposals for external usability research under a compressed timeline.",
      "affected_reasoning_operation": "Preference construction and option evaluation",
      "bias_specific_mechanism": "The participant evaluated the two full-service packages side by side, and the stark contrast between the 21k and 23k options became the frame, causing the cheaper self-serve option to drop out of active consideration even though it may have covered the core flows.",
      "manifestation_in_interview": "The participant selected the 23k vendor, then disclosed that the self-serve option was not seriously evaluated once the full-service comparison took over, and that a changed price gap would have prompted more scrutiny of the top package.",
      "effect_on_reasoning_or_decision": "The participant committed substantially more budget than the self-serve option required and did not fully assess whether the top package's additional features were necessary at the time.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I ended up going with the twenty-three thousand one.",
          "evidence_explanation": "Directly identifies the selected option, establishing the actual decision outcome."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from.",
          "evidence_explanation": "Shows that evaluation was driven by a local contrast between two similar options rather than by whether the cheaper option met the actual need."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all.",
          "evidence_explanation": "Counterfactual confirms that the price-contrast frame, rather than an absolute needs assessment, influenced the choice."
        }
      ],
      "correction_or_counterevidence": "A plausible non-bias explanation is that the top package offered more sessions and features for only a modest price increase. However, the participant's admission that the self-serve option likely covered the needed flows and that the contrast became the working frame supports a context-driven distortion.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly addressed attraction/decoy or context-driven choice; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "halo effect",
      "alternative_labels": [
        "halo error"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The halo effect is the tendency for a positive impression in one salient attribute to spread to unrelated attributes, distorting overall evaluation.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor selection for micro-interaction build",
      "decision_point_description": "Choose between two shortlisted contractors for implementation of wizard micro-interactions.",
      "affected_reasoning_operation": "Trait inference and evidence weighting in personnel selection",
      "bias_specific_mechanism": "A visually polished portfolio and prestigious prior employer generated a global positive impression that generalized to documentation and communication skills without direct verification.",
      "manifestation_in_interview": "The participant chose Candidate X based on visual work and company name recognition, assumed documentation rigor would follow, and undervalued Candidate Y's direct evidence of documented process and testing.",
      "effect_on_reasoning_or_decision": "The participant selected Candidate X, later resulting in missing documentation for two transitions and no testing basis when the Head of Design requested evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here.",
          "evidence_explanation": "Shows that perceived excellence in visual interaction work and employer prestige was generalized to unrelated documentation and communication competencies."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall.",
          "evidence_explanation": "Confirms that the participant did not verify the inferred traits and that a global 'wow factor' distorted the comparison with Candidate Y's more relevant evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have.",
          "evidence_explanation": "Directly acknowledges that brand recognition influenced judgment beyond its evidential value."
        }
      ],
      "correction_or_counterevidence": "Candidate X may have had transferable skills from a relevant role, and the project did require high-polish interaction design. However, the documentation and communication assumptions were made without direct evidence, and Candidate Y's portfolio contained the specific evidence needed.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly addressed halo effect; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "confirmation bias",
      "alternative_labels": [
        "confirmatory bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Confirmation bias is the tendency to seek, interpret, or weight evidence in ways that support pre-existing beliefs while underweighting disconfirming information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Rules engine activation data interpretation",
      "decision_point_description": "Decide whether to treat observed activation uptick as causal and request expanded manual tuning authority.",
      "affected_reasoning_operation": "Causal inference and evidence interpretation",
      "bias_specific_mechanism": "The participant's prior belief that the manual rule changes were effective led him to interpret the dashboard uptick as confirmatory, while discounting the Data lead's warnings about low sample size and a concurrent marketing email.",
      "manifestation_in_interview": "The participant took the uptick as a sign the adjustments were working and requested expanded tuning authority, even though methodological and confounding factors had been explicitly flagged.",
      "effect_on_reasoning_or_decision": "The participant acted on an unconfirmed causal attribution by seeking expanded manual tuning authority before the renewal review.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "The activation numbers on the dashboard ticked up right after. I took it as a sign the adjustments were working.",
          "evidence_explanation": "Demonstrates interpretation of ambiguous temporal evidence as confirmatory of the participant's prior belief about the rule changes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver.",
          "evidence_explanation": "Shows explicit awareness of disconfirming methodological and confounding information, while still maintaining the confirmatory causal interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I just didn't want to lose the momentum.",
          "evidence_explanation": "Indicates that the decision to act was driven by commitment to the favored interpretation rather than by resolving uncertainty."
        }
      ],
      "correction_or_counterevidence": "The Data lead identified the small sample and concurrent email campaign as alternative explanations, and the uptick partly reversed after the campaign ended, leaving the causal driver unconfirmed. However, the biased interpretation already influenced the participant's action to request expanded authority.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved passage from Hallihan et al. directly supports the definitional mechanism of confirmation bias.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "A central component of the confirmation bias is that it manifests itself in a tendency to seek out or interpret evidence in a way that will confirm pre - existing beliefs.",
          "mechanism_supported_by_source": "The source defines confirmation bias as interpreting evidence to confirm pre-existing beliefs.",
          "relevance_to_this_occurrence": "The participant interpreted the dashboard uptick as confirming that his manual adjustments worked while discounting Data lead flags about small sample and concurrent email marketing."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "sunk cost effect",
        "escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The sunk cost fallacy is the tendency to continue an endeavor because of past irrecoverable investments, even when prospective cost and risk favor a different course.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Legacy wizard component migration decision",
      "decision_point_description": "Decide whether to continue customizing the legacy component or migrate to a newer modular framework.",
      "affected_reasoning_operation": "Continuation and resource allocation decision",
      "bias_specific_mechanism": "The three already-spent sprints created psychological commitment and a sense that abandoning the legacy component would waste past work, causing past investment to dominate prospective cost-risk evaluation.",
      "manifestation_in_interview": "The participant pushed to keep customizing the legacy component despite recognizing that the one-sprint migration estimate was probably better on cost and risk.",
      "effect_on_reasoning_or_decision": "The participant continued customizing the legacy component; the accessibility issue later recurred during pre-renewal QA, and migration subsequently became more expensive than the original estimate.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us.",
          "evidence_explanation": "Shows the continuation decision was motivated by irrecoverable past investment rather than purely future cost and risk."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built.",
          "evidence_explanation": "Explicitly contrasts the superior prospective option with the psychological difficulty of abandoning sunk work."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back.",
          "evidence_explanation": "Counterfactual isolates the sunk investment as the decisive distorting factor."
        }
      ],
      "correction_or_counterevidence": "Deadline pressure and uncertainty about the migration estimate may also have contributed, but the participant's explicit counterfactual indicates that past sunk effort was the primary reason for continuing.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied RAG context directly defined sunk cost fallacy; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The supplied RAG context is sparse and does not contain retrieved passages for every classified bias; classifications for attraction effect, halo effect, and sunk cost fallacy rely on established cognitive-science knowledge rather than corpus support.",
    "The analysis is based on a self-reported interview, so recall and self-presentation may affect the evidence, though the relevant mechanisms are explicitly described by the participant.",
    "Some episodes may involve overlapping or interacting biases; only primary mechanisms are labeled to avoid over-fragmenting.",
    "The vendor selection occurrence is classified with low confidence because a plausible rational account remains."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through a specific project, not whether the outcome was good or bad. Everything you share stays with the research team, and you can skip anything you'd rather not discuss. Sound okay? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role and give me a general sense of the project we're going to talk about? Participant: Sure, I'm a UX designer on the product team at an analytics SaaS company. Back in Q4 we had a six-week window to redesign our onboarding wizard before a big client renewal review. Leadership wanted to see a real bump in activation rate going into that meeting, so there was a lot riding on it. Interviewer: What made this project different from a routine update? Participant: Normally we'd have more runway — like a full quarter. This one was compressed, and the budget for outside help was capped, so every dollar and every hour had to be justified. Engineering could only give us maybe one and a half people. It was tight. Interviewer: Walk me through how it unfolded, from the start. Participant: So the first thing on my plate was research. We knew the wizard's drop-off was concentrated in three flows, and I needed outside eyes on it fast. I got three vendor proposals in the same week. One was a cheap self-serve platform, six grand, five sessions, but basically no synthesis — you get raw recordings and that's it. Then there were two full-service options: one at twenty-one thousand for ten sessions with a written synthesis, and another at twenty-three for twelve sessions plus dashboard integration and two follow-up rounds. I ended up going with the twenty-three thousand one. Interviewer: What tipped it that direction? Participant: Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. For two grand more you got two more sessions, the dashboard hookup, and follow-ups baked in. The middle option just looked like a worse version of the top one at almost the same price. It felt like an easy call. Interviewer: Did you look closely at whether the cheaper self-serve option would've covered what you actually needed? Participant: I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from. Interviewer: Got it. What happened after you picked that vendor? Participant: The findings were usable, but we later realized two of the twelve sessions basically repeated data we already had internally. And the dashboard integration they promised only half worked at delivery, so I had to patch a lot of that manually anyway. Interviewer: Let's move to the next stage. What came after research? Participant: We needed a contractor to build the actual micro-interactions for the new flow — transitions, progress indicators, that kind of thing. Two candidates were shortlisted. One, let's call him Candidate X, had done flagship interaction work at a pretty well-known unicorn startup — gorgeous portfolio. The other, Candidate Y, had a less flashy portfolio but included actual test scripts, metrics, iteration logs, the whole documented process. Interviewer: What made you choose between them? Participant: I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. It seemed like a safe bet given where he'd come from. Interviewer: Did you verify that documentation and communication piece directly — maybe ask for writing samples or how he'd handled testing on past projects? Participant: Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall. Interviewer: How did that play out? Participant: The micro-interactions themselves were beautiful. But he skipped documenting the reasoning behind two key transitions, and when the Head of Design asked for the testing basis, there wasn't really anything to show her. Interviewer: Let's talk about the third stage — the personalization engine. Participant: Right, so in parallel we were running a small test on the rules engine — about a hundred forty users — and I'd manually adjusted two of the onboarding rule weights that same week. The activation numbers on the dashboard ticked up right after. Interviewer: What did you make of that? Participant: I took it as a sign the adjustments were working. I went to the Data lead and asked to expand my manual tuning authority so I could keep pushing on it before the renewal review. Interviewer: Was there anything at the time that complicated that read? Participant: She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver. Interviewer: What happened the following week? Participant: The uptick partly reversed once the email campaign ended, and she noted the causal driver was still unconfirmed. So it's genuinely unclear how much of that first bump was actually the rule changes. Interviewer: Last stage — tell me about the legacy component decision. Participant: We'd spent three sprints customizing our old step-wizard component to fit the new flow. Then engineering flagged an accessibility defect and a rendering performance issue, and said a newer modular framework would fix both in about a sprint. Interviewer: What did you decide? Participant: I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us. Interviewer: Setting aside the sprints already spent, how did the one-sprint migration estimate compare on its own terms to continuing? Participant: If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built. Interviewer: What ended up happening with that component? Participant: The accessibility issue surfaced again during the pre-renewal QA pass, and by then the migration would've cost more than the original estimate because we'd layered on even more customization in the meantime. Interviewer: If Vendor B had been priced the same as Vendor C, would you have chosen differently? Participant: Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all. Interviewer: If Candidate Y's portfolio had come from a more recognizable company, would the hiring call have gone differently? Participant: Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have. Interviewer: And if the significance threshold had been strictly enforced before you could act on the rules engine data? Participant: I'd have waited, or at least run the isolated test first. I just didn't want to lose the momentum. Interviewer: Last one — if none of the three sprints had already gone into the legacy component, would you still have kept it? Participant: No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back. Interviewer: This has been really useful. Thank you for being so candid about where things were uncertain. Participant: Of course — it's easier to see some of this clearly now than it was in the middle of the sprint.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.34s · gen 141.15s · total 145.9s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0265 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0229 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0221 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0218 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
5. **Hallihan_etal_DTM_12.pdf** — 0.0216 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0202 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
7. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0193 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0190 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0183 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Hallihan_etal_DTM_12.pdf** — 0.0175 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
15. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0174 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0174 (rrf) — _# Experiment 2 e purpose of Experiment 2 was (a) to replicate the observation of Experiment 1 th_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0169 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
18. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0163 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
21. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
22. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
23. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0161 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study First, experiments are cl_
24. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
25. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0159 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0159 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
27. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _prototyping (Viswanathan & Linsey, 2011). However, cognitive heuristics and biases have been stu_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
30. **Hallihan_etal_DTM_12.pdf** — 0.0155 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
31. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0155 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
32. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
33. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
34. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Technical Communication Make Decisions . https://www.nngroup.com/articles/_
35. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0153 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
37. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0150 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization , We collected all In_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
40. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0149 (rrf) — _# 4Discussion - - viewing CFFs as more cognitively demanding. Although coming at the cost of use_
41. **Hallihan_etal_DTM_12.pdf** — 0.0146 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
42. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0145 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
43. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0144 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 As a step towards studying human cognition in AIassist_
44. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0143 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
46. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0143 (rrf) — _# ( " = 0 . 44 ) . 188:18 Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos Third, our r_
47. **Hallihan_etal_DTM_12.pdf** — 0.0142 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
49. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0141 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis of a single cognitive task analysis interview for bias-specific mechanisms in four project reasoning episodes."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Attraction effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Halo effect",
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
      "bias_label": "Attraction effect",
      "alternative_labels": ["Decoy effect", "Asymmetric dominance effect", "Context effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A context effect in which the presence of an inferior or decoy option in a choice set increases preference for a target option relative to another alternative.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Vendor selection for onboarding wizard usability research",
      "decision_point_description": "Choice among one cheap self-serve vendor option and two full-service vendor packages.",
      "affected_reasoning_operation": "Option evaluation and vendor choice",
      "bias_specific_mechanism": "The stark comparison between the 21k and 23k full-service packages created a local evaluative frame in which the 23k package appeared clearly superior; this frame displaced continued consideration of the cheaper self-serve option that might have satisfied the actual research needs.",
      "manifestation_in_interview": "The participant reports comparing the two full-service packages side by side and making an easy call for the top package, while the self-serve package dropped out of the comparison after only a glance.",
      "effect_on_reasoning_or_decision": "The participant selected the highest-cost vendor package after the cheaper option fell out of the comparison, rather than independently assessing the cheaper option's fit with project requirements.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. For two grand more you got two more sessions, the dashboard hookup, and follow-ups baked in. The middle option just looked like a worse version of the top one at almost the same price. It felt like an easy call.",
          "evidence_explanation": "Shows that the preference was formed through the local contrast between the two full-service options rather than through an independent assessment of project needs."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from.",
          "evidence_explanation": "Explicitly describes the decoy-like comparison frame that removed the cheaper option from serious consideration."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all.",
          "evidence_explanation": "Counterfactual indicates that the comparison framing, rather than a needs-based evaluation, shaped the decision."
        }
      ],
      "correction_or_counterevidence": "The top package had objectively more deliverables for a modest price increment, so selecting it could be justified on value grounds. The participant also acknowledges that the cheaper self-serve package probably could have handled the needed flows.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the attraction/decoy-effect label was not available; the label derives from general knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Halo effect",
      "alternative_labels": ["Representativeness heuristic", "Prestige bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which a positive global impression or salient positive attribute influences judgments about specific unrelated attributes.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor selection for micro-interaction build",
      "decision_point_description": "Choosing between Candidate X, with visually impressive work from a recognizable company, and Candidate Y, with documented testing and iteration process evidence.",
      "affected_reasoning_operation": "Inference about unobserved candidate competencies and hiring choice",
      "bias_specific_mechanism": "The visual polish and recognizable company provenance of Candidate X created a positive global impression that was overgeneralized to documentation, communication, and testing rigor, despite no direct evidence for those attributes. Candidate Y's direct evidence for those attributes was discounted because it lacked the same wow factor.",
      "manifestation_in_interview": "The participant chose Candidate X, assumed documentation and communication skills would follow from visual work and company name recognition, and did not verify those skills directly.",
      "effect_on_reasoning_or_decision": "The hiring decision was made without directly verifying documentation and communication competencies; later, the candidate lacked documentation for two key transitions.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. It seemed like a safe bet given where he'd come from.",
          "evidence_explanation": "Shows overgeneralization from visual polish and company provenance to unrelated professional practices like documentation and communication."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall.",
          "evidence_explanation": "Explicitly acknowledges that visual impression was generalized to unverified attributes and that relevant direct evidence was discounted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have.",
          "evidence_explanation": "Acknowledges that a non-diagnostic cue, name recognition, influenced the hiring inference."
        }
      ],
      "correction_or_counterevidence": "Candidate X's visual work was relevant and strong, so the selection was not based on irrelevant information. The participant later recognized the unwarranted assumption.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the halo-effect label was not available; the label derives from general knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Motivated reasoning", "Myside bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to seek out or interpret evidence in a way that confirms pre-existing beliefs.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of rules-engine activation uptick after manual tuning",
      "decision_point_description": "Deciding whether manually adjusted rule weights caused the activation uptick and whether to expand manual tuning authority.",
      "affected_reasoning_operation": "Causal attribution and evidence evaluation",
      "bias_specific_mechanism": "After manually adjusting rule weights, the participant treated a temporally salient dashboard uptick as confirmatory evidence that the adjustments were working. The Data lead's disconfirming cautions about small sample size, lack of isolation, and a concurrent email campaign were acknowledged but set aside because the timing felt too compelling.",
      "manifestation_in_interview": "The participant interpreted the uptick as a sign that the adjustments were working and asked to expand manual tuning authority, despite being told the result was below the pre-registered significance threshold and confounded.",
      "effect_on_reasoning_or_decision": "The participant sought expanded tuning authority prematurely based on confirmatory interpretation of ambiguous evidence; the subsequent reversal left the causal driver unconfirmed.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Right, so in parallel we were running a small test on the rules engine — about a hundred forty users — and I'd manually adjusted two of the onboarding rule weights that same week. The activation numbers on the dashboard ticked up right after.",
          "evidence_explanation": "Establishes the temporal association and the participant's prior involvement in the changes, which gave the participant a reason to expect the changes were working."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I took it as a sign the adjustments were working. I went to the Data lead and asked to expand my manual tuning authority so I could keep pushing on it before the renewal review.",
          "evidence_explanation": "Shows ambiguous evidence being interpreted as confirmation of the participant's expectation and then acted on."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver.",
          "evidence_explanation": "Demonstrates that qualifying or disconfirming information was acknowledged but discounted in favor of the salient confirming cue."
        }
      ],
      "correction_or_counterevidence": "The Data lead explicitly flagged the small sample and confounds at the time. The following week, the uptick partly reversed after the email campaign ended, and the participant now says the causal driver was unclear.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Label and mechanism supported by a retrieved corpus passage on confirmation bias.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "A central component of the confirmation bias is that it manifests itself in a tendency to seek out or interpret evidence in a way that will confirm pre - existing beliefs.",
          "mechanism_supported_by_source": "The source defines confirmation bias as interpreting evidence in ways that confirm pre-existing beliefs.",
          "relevance_to_this_occurrence": "The participant interpreted the activation uptick as support for the pre-existing belief that the manual rule changes were working, while discounting the Data lead's cautions about sample size and confounds."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Sunk cost fallacy",
      "alternative_labels": ["Escalation of commitment", "Sunk cost effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue an endeavor once an investment of money, effort, or time has been made, even when forward-looking cost-benefit analysis favors an alternative.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Decision to continue customizing legacy step-wizard component versus migrating",
      "decision_point_description": "Engineering offered a one-sprint migration to a newer modular framework to fix accessibility and rendering issues after three sprints had already been spent customizing the legacy component.",
      "affected_reasoning_operation": "Decision to continue versus switch",
      "bias_specific_mechanism": "The participant treated the prior three sprints of customization as a reason to keep going, even though those costs were sunk and should not influence the forward-looking cost-risk comparison. The participant explicitly described restarting as feeling like throwing work away and had difficulty letting go of what had already been built.",
      "manifestation_in_interview": "The participant pushed to keep customizing the legacy component rather than migrate, even though the one-sprint migration estimate was probably a better bet purely on cost and risk.",
      "effect_on_reasoning_or_decision": "The participant continued the legacy customization path; the accessibility issue later resurfaced during QA, and migration would then have cost more than the original estimate.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us.",
          "evidence_explanation": "Directly states that prior unrecoverable work drove the decision to continue."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built.",
          "evidence_explanation": "Acknowledges that the forward-looking comparison favored migration, while the prior investment blocked that choice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back.",
          "evidence_explanation": "Counterfactual isolates the sunk cost as the decisive factor in the continuation decision."
        }
      ],
      "correction_or_counterevidence": "The participant recognized the sunk-cost pull during the interview. There was no contemporaneous correction, and the accessibility defect later resurfaced.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Retrieved corpus support for the sunk-cost label was not available; the label derives from general knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The interview is a retrospective self-report, so the identified mechanisms are inferred from the participant's reconstructed account rather than from direct observation.",
    "Retrieved corpus support was available for only one identified occurrence; the remaining labels were assigned from general knowledge and are not supported by retrieved passages.",
    "The analysis targets reasoning processes evident in the interview and does not presume that objectively better alternatives would necessarily have produced better outcomes."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time for this. Just to set expectations, this is a cognitive task analysis interview — I'm interested in how you actually reasoned through a specific project, not whether the outcome was good or bad. Everything you share stays with the research team, and you can skip anything you'd rather not discuss. Sound okay? Participant: Yeah, that's fine. Happy to walk through it. Interviewer: Great. Can you tell me your role and give me a general sense of the project we're going to talk about? Participant: Sure, I'm a UX designer on the product team at an analytics SaaS company. Back in Q4 we had a six-week window to redesign our onboarding wizard before a big client renewal review. Leadership wanted to see a real bump in activation rate going into that meeting, so there was a lot riding on it. Interviewer: What made this project different from a routine update? Participant: Normally we'd have more runway — like a full quarter. This one was compressed, and the budget for outside help was capped, so every dollar and every hour had to be justified. Engineering could only give us maybe one and a half people. It was tight. Interviewer: Walk me through how it unfolded, from the start. Participant: So the first thing on my plate was research. We knew the wizard's drop-off was concentrated in three flows, and I needed outside eyes on it fast. I got three vendor proposals in the same week. One was a cheap self-serve platform, six grand, five sessions, but basically no synthesis — you get raw recordings and that's it. Then there were two full-service options: one at twenty-one thousand for ten sessions with a written synthesis, and another at twenty-three for twelve sessions plus dashboard integration and two follow-up rounds. I ended up going with the twenty-three thousand one. Interviewer: What tipped it that direction? Participant: Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. For two grand more you got two more sessions, the dashboard hookup, and follow-ups baked in. The middle option just looked like a worse version of the top one at almost the same price. It felt like an easy call. Interviewer: Did you look closely at whether the cheaper self-serve option would've covered what you actually needed? Participant: I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from. Interviewer: Got it. What happened after you picked that vendor? Participant: The findings were usable, but we later realized two of the twelve sessions basically repeated data we already had internally. And the dashboard integration they promised only half worked at delivery, so I had to patch a lot of that manually anyway. Interviewer: Let's move to the next stage. What came after research? Participant: We needed a contractor to build the actual micro-interactions for the new flow — transitions, progress indicators, that kind of thing. Two candidates were shortlisted. One, let's call him Candidate X, had done flagship interaction work at a pretty well-known unicorn startup — gorgeous portfolio. The other, Candidate Y, had a less flashy portfolio but included actual test scripts, metrics, iteration logs, the whole documented process. Interviewer: What made you choose between them? Participant: I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. It seemed like a safe bet given where he'd come from. Interviewer: Did you verify that documentation and communication piece directly — maybe ask for writing samples or how he'd handled testing on past projects? Participant: Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall. Interviewer: How did that play out? Participant: The micro-interactions themselves were beautiful. But he skipped documenting the reasoning behind two key transitions, and when the Head of Design asked for the testing basis, there wasn't really anything to show her. Interviewer: Let's talk about the third stage — the personalization engine. Participant: Right, so in parallel we were running a small test on the rules engine — about a hundred forty users — and I'd manually adjusted two of the onboarding rule weights that same week. The activation numbers on the dashboard ticked up right after. Interviewer: What did you make of that? Participant: I took it as a sign the adjustments were working. I went to the Data lead and asked to expand my manual tuning authority so I could keep pushing on it before the renewal review. Interviewer: Was there anything at the time that complicated that read? Participant: She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver. Interviewer: What happened the following week? Participant: The uptick partly reversed once the email campaign ended, and she noted the causal driver was still unconfirmed. So it's genuinely unclear how much of that first bump was actually the rule changes. Interviewer: Last stage — tell me about the legacy component decision. Participant: We'd spent three sprints customizing our old step-wizard component to fit the new flow. Then engineering flagged an accessibility defect and a rendering performance issue, and said a newer modular framework would fix both in about a sprint. Interviewer: What did you decide? Participant: I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us. Interviewer: Setting aside the sprints already spent, how did the one-sprint migration estimate compare on its own terms to continuing? Participant: If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built. Interviewer: What ended up happening with that component? Participant: The accessibility issue surfaced again during the pre-renewal QA pass, and by then the migration would've cost more than the original estimate because we'd layered on even more customization in the meantime. Interviewer: If Vendor B had been priced the same as Vendor C, would you have chosen differently? Participant: Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all. Interviewer: If Candidate Y's portfolio had come from a more recognizable company, would the hiring call have gone differently? Participant: Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have. Interviewer: And if the significance threshold had been strictly enforced before you could act on the rules engine data? Participant: I'd have waited, or at least run the isolated test first. I just didn't want to lose the momentum. Interviewer: Last one — if none of the three sprints had already gone into the legacy component, would you still have kept it? Participant: No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back. Interviewer: This has been really useful. Thank you for being so candid about where things were uncertain. Participant: Of course — it's easier to see some of this clearly now than it was in the middle of the sprint.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.74s · gen 111.31s · total 116.7s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0265 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0229 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
3. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0221 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
4. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0218 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
5. **Hallihan_etal_DTM_12.pdf** — 0.0216 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0202 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
7. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0193 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
8. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
9. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0190 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
11. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0189 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
12. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0183 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
13. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0181 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
14. **Hallihan_etal_DTM_12.pdf** — 0.0175 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
15. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0174 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0174 (rrf) — _# Experiment 2 e purpose of Experiment 2 was (a) to replicate the observation of Experiment 1 th_
17. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0169 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
18. **Hallihan_etal_DTM_12.pdf** — 0.0164 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0163 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0163 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
21. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0162 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
22. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0161 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
23. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0161 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study First, experiments are cl_
24. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0159 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
25. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0159 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
26. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0159 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
27. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _prototyping (Viswanathan & Linsey, 2011). However, cognitive heuristics and biases have been stu_
28. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# ( " = 0 . 44 ) . \[1\] GaganBansal,BesmiraNushi,EceKamar,WalterSLasecki,DanielSWeld,andEricHor_
29. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_
30. **Hallihan_etal_DTM_12.pdf** — 0.0155 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
31. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0155 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
32. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0155 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
33. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
34. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0153 (rrf) — _# Cognitive Biases in Technical Communication Make Decisions . https://www.nngroup.com/articles/_
35. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0153 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
36. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0151 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
37. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study In the context of artifac_
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0150 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization , We collected all In_
39. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
40. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0149 (rrf) — _# 4Discussion - - viewing CFFs as more cognitively demanding. Although coming at the cost of use_
41. **Hallihan_etal_DTM_12.pdf** — 0.0146 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
42. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0145 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
43. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0144 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 As a step towards studying human cognition in AIassist_
44. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0143 (rrf) — _considered the most relevant, and may serve as an anchor that influences how searchers answer qu_
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
46. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0143 (rrf) — _# ( " = 0 . 44 ) . 188:18 Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos Third, our r_
47. **Hallihan_etal_DTM_12.pdf** — 0.0142 (rrf) — _development, a series of events must occur; even when the individual likelihood of success for e_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0141 (rrf) — _# 5. Discussion which is an interesting finding and supports much of the research it is” syndrom_
49. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0141 (rrf) — _# 188 simulated AI always provided suggestions for replacing the ingredient highest in carbohydr_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0140 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analyzed the full CTA interview for affirmative evidence of bias-specific mechanisms. Retrospective outcomes and counterfactual admissions were used only as supporting admissions or counterevidence, not as proof that a speaker was biased at the time."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Confirmation bias",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Decoy effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "Halo effect",
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
      "bias_label": "Decoy effect",
      "alternative_labels": ["Attraction effect", "Asymmetric dominance effect", "Contrast effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "A choice bias in which adding an asymmetrically dominated option, or decoy, makes a target option appear more attractive and shifts preference away from an absolute evaluation of needs.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Research vendor selection",
      "decision_point_description": "Selection among a cheap self-serve research platform, a $21,000 full-service option, and a $23,000 full-service option with more sessions and dashboard integration.",
      "affected_reasoning_operation": "Comparative evaluation of vendor proposals under budget and time constraints",
      "bias_specific_mechanism": "The $21,000 full-service option served as an asymmetrically dominated contrast or decoy, making the $23,000 option appear disproportionately better for only $2,000 more; this contrast frame caused the cheap self-serve option, which likely could have handled the three known flows, to drop out of consideration.",
      "manifestation_in_interview": "The participant framed the vendor decision around the two full-service packages and chose the top option because it dominated the middle option on features for a small price increment. The self-serve option was dismissed even though it probably covered the session count needed for the three flows.",
      "effect_on_reasoning_or_decision": "The participant selected the $23,000 vendor, later realizing some paid features were duplicative or partially unavailable at delivery, while a lower-cost option may have been sufficient for the actual research need.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, once I laid the twenty-one and twenty-three side by side, it wasn't close. For two grand more you got two more sessions, the dashboard hookup, and follow-ups baked in. The middle option just looked like a worse version of the top one at almost the same price.",
          "evidence_explanation": "This shows the choice was driven by relative comparison between the top and middle options rather than by an absolute assessment of project needs."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I glanced at it. It probably could've handled the three flows we cared about, session-count-wise. But once I was comparing the two full-service packages, the smaller one kind of dropped out of the conversation — the contrast between the other two was just so stark that it became the frame I was working from.",
          "evidence_explanation": "This directly demonstrates the decoy/contrast mechanism: the attractive dominated middle option changed the comparison frame and excluded a sufficient lower-cost option."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Maybe — without that price gap, I probably would've looked harder at whether we needed everything in the top package at all.",
          "evidence_explanation": "This admission links the choice to the decoy-like price/feature contrast rather than to a needs-based decision."
        }
      ],
      "correction_or_counterevidence": "The participant retroactively acknowledged that without the price gap, he likely would have examined whether the top package's extra features were actually necessary.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus specifically addressed the decoy/attraction effect or asymmetric dominance; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Halo effect",
      "alternative_labels": ["Halo error", "Brand name bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "A cognitive bias in which a positive evaluation in one salient domain spreads to unrelated attributes, producing unwarranted inferences about quality or competence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Contractor selection for micro-interactions",
      "decision_point_description": "Selection between Candidate X, with strong visual work from a well-known company, and Candidate Y, with documented test scripts, metrics, and iteration logs.",
      "affected_reasoning_operation": "Inference about unobserved candidate competencies from observed visual portfolio and company reputation",
      "bias_specific_mechanism": "The prestige and visual polish of Candidate X's shipped work at a recognizable company created a global positive impression that spread to unrelated attributes, leading the participant to assume Candidate X would also be rigorous in documentation and stakeholder communication.",
      "manifestation_in_interview": "The participant chose Candidate X because his portfolio and company background were impressive, then explicitly said he assumed the documentation and communication skills would follow from that visible work rather than verifying them directly. Candidate Y's evidence of process was discounted because it lacked the same wow factor.",
      "effect_on_reasoning_or_decision": "The participant hired Candidate X without verifying documentation or testing process. The micro-interactions were visually strong, but key transitions lacked documented reasoning and testing evidence when the Head of Design requested it.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I went with Candidate X. The work he'd shipped at that company was the kind of polish we wanted for this wizard, and if he could deliver that caliber of interaction design there, I figured he'd bring the same rigor to documenting decisions and communicating with stakeholders here. It seemed like a safe bet given where he'd come from.",
          "evidence_explanation": "This shows an inference from a salient positive attribute, visual polish and company prestige, to unrelated attributes of documentation rigor and communication.",
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Not really, no. I looked at the visual work and sort of assumed the rest would follow. In hindsight, Candidate Y's portfolio had exactly what we needed evidence-wise, but it didn't have the same wow factor, so it read as less impressive overall.",
          "evidence_explanation": "The participant explicitly admits that visual impressiveness generalized to an assumption about other competencies, while direct evidence of those competencies was underweighted."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Probably, yeah. It's uncomfortable to admit, but the name recognition was doing more work in my head than it should have.",
          "evidence_explanation": "This admission identifies company name recognition as an undue influence on the hiring judgment."
        }
      ],
      "correction_or_counterevidence": "The interviewer asked whether documentation and communication had been verified directly, and the participant admitted they had not. The participant later acknowledged that name recognition was doing more work than it should have.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus specifically addressed the halo effect; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Confirmation bias",
      "alternative_labels": ["Myside bias", "Confirmation seeking"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to search for, interpret, favor, and recall information in ways that confirm or support one's existing beliefs, hypotheses, or desires.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Interpretation of rules-engine activation uptick",
      "decision_point_description": "Decision to ask the Data lead for expanded manual tuning authority after observing an activation uptick following manual rule-weight changes.",
      "affected_reasoning_operation": "Causal interpretation of activation data and decision to act on the rule-change hypothesis",
      "bias_specific_mechanism": "The participant favored the pre-existing belief that his manual rule-weight changes caused the activation uptick. He treated favorable timing as confirming evidence while discounting methodological warnings that the sample was below the significance threshold and that a concurrent marketing email blast could have been responsible.",
      "manifestation_in_interview": "The participant saw the uptick as a sign the adjustments were working and requested expanded tuning authority. When the Data lead flagged inadequate sample size and a confounding email campaign, the participant acknowledged but dismissed those concerns because the timing felt too clean.",
      "effect_on_reasoning_or_decision": "The participant acted on an unconfirmed causal inference by requesting expanded manual tuning authority. The next week the uptick partially reversed after the email campaign ended, leaving the causal driver unclear.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I took it as a sign the adjustments were working. I went to the Data lead and asked to expand my manual tuning authority so I could keep pushing on it before the renewal review.",
          "evidence_explanation": "This shows the participant interpreted the uptick as evidence for his prior belief and made a decision based on that interpretation."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "She flagged that the sample was below our pre-registered threshold for significance, and we hadn't run anything isolating my rule changes from other things happening that week — there was a marketing email blast running concurrently. I heard that, but the timing felt too clean to ignore. It really did look like my changes were the driver.",
          "evidence_explanation": "This demonstrates confirmation bias directly: disconfirming or competing methodological information was acknowledged but not incorporated, while the favored causal explanation was retained."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd have waited, or at least run the isolated test first. I just didn't want to lose the momentum.",
          "evidence_explanation": "This admission confirms that the participant bypassed a stricter evidence standard that would have been required to test his belief."
        }
      ],
      "correction_or_counterevidence": "The Data lead immediately flagged the small sample and concurrent marketing email confound. The following week the uptick partly reversed after the email campaign ended, and the causal driver remained unconfirmed.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus support was identified from Hallihan et al. (DTM_12), which defines confirmation bias in terms of interpreting evidence to confirm pre-existing beliefs.",
      "corpus_evidence": [
        {
          "source_identifier": "Hallihan_etal_DTM_12.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent designers from fully  considering the value of alternative design solutions. ... A central component of the confirmation bias is that it manifests itself in a tendency to seek out or interpret evidence in a way that will confirm pre - existing beliefs.",
          "mechanism_supported_by_source": "Confirmation bias involves interpreting evidence in a way that confirms pre-existing beliefs, even when alternative explanations or disconfirming information are available.",
          "relevance_to_this_occurrence": "The participant interpreted the activation uptick as confirming his rule-change hypothesis while discounting the Data lead's methodological warnings about sample size and the concurrent email campaign."
        }
      ]
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Sunk cost fallacy",
      "alternative_labels": ["Escalation of commitment", "Sunk cost effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to continue an endeavor or invest further once resources have been committed, even when future costs and benefits favor a different course, because past irrecoverable costs are treated as losses that must be honored.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Legacy component continuation versus migration",
      "decision_point_description": "Decision to continue customizing the legacy step-wizard component instead of migrating to a newer modular framework after engineering identified accessibility and rendering defects.",
      "affected_reasoning_operation": "Decision whether to continue investing in a legacy component or migrate to a newer framework",
      "bias_specific_mechanism": "Past investment of three sprints in legacy customization was mentally treated as a non-recoverable loss. Migration felt like throwing that work away, so the participant escalated commitment to the legacy component even though the one-sprint migration estimate was likely better on forward-looking cost and risk.",
      "manifestation_in_interview": "The participant pushed to keep customizing the legacy component because three sprints had already been spent and restarting felt wasteful. He admitted that, setting aside those sunk sprints, the migration estimate was probably a better bet purely on cost and risk.",
      "effect_on_reasoning_or_decision": "The participant continued the legacy path. The accessibility issue resurfaced during pre-renewal QA, and by then migration would have cost more than the original estimate because additional customization had been layered on.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I pushed to keep customizing the legacy component rather than migrate. We'd already put three sprints into it — restarting felt like throwing that away with the deadline bearing down on us.",
          "evidence_explanation": "This shows the decision was influenced by irrecoverable past effort rather than future cost, risk, and benefit."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "If I'm honest, the one-sprint number was probably a better bet purely on cost and risk. But it was hard to mentally let go of what we'd already built.",
          "evidence_explanation": "This explicitly contrasts the forward-looking case for migration with the psychological pull of sunk costs."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "No. If we were starting fresh, the defects alone would've pushed me toward the new framework immediately. It was really the work already sunk into it that kept pulling me back.",
          "evidence_explanation": "This counterfactual isolates the sunk-cost mechanism: without past investment, the participant would have chosen differently."
        }
      ],
      "correction_or_counterevidence": "The interviewer asked the participant to set aside the sprints already spent. The participant acknowledged migration was probably a better bet on cost and risk and that without prior investment the defects alone would have led to immediate migration.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage in the supplied corpus specifically addressed the sunk cost fallacy or escalation of commitment; the label is applied from general cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus was sparse and largely focused on AI-assisted decision-making, so several identified bias labels rely on general cognitive-science knowledge rather than retrieved corpus support.",
    "Single-interview transcript was analyzed; no independent verification of the participant's reported decisions or outcomes was available.",
    "Vendor naming was partly prompted by the interviewer using Vendor B and Vendor C; the underlying decision evidence, however, was supplied by the participant."
  ]
}

