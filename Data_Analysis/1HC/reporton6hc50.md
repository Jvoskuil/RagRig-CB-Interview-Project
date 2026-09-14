# RAG Benchmark — 2026-09-11

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for making time this week of all weeks. Before we start, this is just for our internal process-improvement review — I'll ask you to walk me through a recent stretch of work, and there's no wrong answer. That okay? Participant: Sure, happy to. Lock week is a good time to talk about it, honestly, everything's still fresh. Interviewer: Great. Can you remind me of your role and what was on your plate? Participant: I'm the CRC for our site on the Phase III trial — the oncology drug study. I handle adverse event triage, case report form cleanup, and screening new referrals. That week we were seven days out from the interim data lock for the DSMB, so basically everything converged at once. Interviewer: Walk me through what that week looked like. Participant: Monday morning I got a lab flag on Participant 12 — an ALT elevation, elevated but not dramatically so, and the timeline relative to dosing wasn't clean. Could've been drug-related, could've been something else entirely, maybe even diet or an OTC medication he didn't mention. I had to assign a causality category for the AE report. Same day, I was also mid-reconciliation on Participant 07's case report forms — that one had been a slog for almost two weeks, lots of inconsistent entries between the source charts and the CRF. Then Wednesday a new referral came in for screening, and Thursday there was a multi-site coordinator call about verification procedures ahead of lock. So four distinct things, all against the same deadline. Interviewer: Let's start with Participant 12. What did you have in front of you? Participant: His ALT was elevated, but in a range where you genuinely can't tell just from the number whether it's the study drug. Our protocol has three buckets — related, possibly related, unrelated — for exactly this kind of situation. I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point. Interviewer: How did that shape the classification? Participant: I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed. Interviewer: What about the 'possibly related' option? Participant: Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side. Interviewer: What happened after? Participant: The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after. Interviewer: Let's move to Participant 07. Participant: That one's been painful. I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records. Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that. Interviewer: What did you do with that discrepancy? Participant: I kept going. Twenty hours felt like too much to walk away from without one more push. And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it. Interviewer: Did you consider flagging it as a deviation instead? Participant: I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours. Interviewer: How did it turn out? Participant: The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later. Interviewer: Let's talk about the new referral on Wednesday. Participant: He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has. Interviewer: What did you do with that instinct? Participant: I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through. Interviewer: What happened when you did screen him? Participant: He met every inclusion criterion. Clean screen, no issues. Which doesn't tell you much either way about whether deprioritizing him was the right call — I just got lucky that lock week didn't cost us his enrollment. Interviewer: Last one — the coordinator call about verification. Participant: Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever. Interviewer: What made you switch? Participant: Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine. Interviewer: Any pushback since? Participant: The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.' Interviewer: If you could go back, what single piece of information would have changed any of these calls? Participant: For Participant 12, if I'd pulled his full history first instead of after, I might not have leaned so hard on that other case. For the verification switch, actual error-rate data would've mattered — I just didn't have it and didn't chase it down in time. Interviewer: What if that Monday meeting about the other participant's enzyme case had never come up? Participant: I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind. Interviewer: And if the Site Director's email had framed Participant 07 differently — say, just asking whether continued reconciliation was worth the time? Participant: I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have. Interviewer: Last one — if none of the other sites had mentioned switching methods on that call? Participant: I probably would've stuck with what we had. It's passed every audit. There wasn't really a problem to solve, other than speed.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.82s · gen 221.13s · total 225.2s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0249 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0246 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0237 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0201 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0199 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
11. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0188 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
12. **Hallihan_etal_DTM_12.pdf** — 0.0183 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
13. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0173 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
14. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0163 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
23. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0153 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
27. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0153 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
28. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0153 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
29. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0153 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0148 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
32. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0147 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0147 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
35. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0145 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0144 (rrf) — _# fi cation patient vignettes. JAMA Netw. Open 5. Ito, N. et al. The accuracy and potential raci_
37. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0144 (rrf) — _# Experiment 3 Mean number of misclassications on the three blocks of 40/60 trials in the AIassi_
38. **Lyell Automation bias and verification complexity.pdf** — 0.0144 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
39. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
40. **Lyell Automation bias and verification complexity.pdf** — 0.0141 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
42. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0139 (rrf) — _# support et al., 2019 ; Phillips-Wren, base rate data can in the estimate influenced by the pre_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0137 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. Chan, U. Dulleck et al. conductedadditionalana_
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
46. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0136 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# to Dangers from Humans I am more and more convinced that Man is a dangerous creature, and that_
48. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0134 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
49. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0133 (rrf) — _# Self - other Placement W ith no other evidence chance of success w ould also the p rinciple of_
50. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0133 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Conservative, mechanism-first review of a clinical research coordinator's self-reported work episodes during data-lock week. Only reasoning episodes with affirmative evidence of a distinct cognitive distortion mechanism were classified as identified occurrences."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "framing effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "satisficing",
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
      "bias_label": "availability heuristic",
      "alternative_labels": [
        "availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to judge likelihood, relevance, or similarity based on how easily examples come to mind rather than on objective evidence or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 12 ALT causality classification",
      "decision_point_description": "Classify Participant 12's ALT elevation into related, possibly related, or unrelated AE category.",
      "affected_reasoning_operation": "Causality classification and evidence weighting",
      "bias_specific_mechanism": "A recent Monday team discussion made another participant's enzyme bump highly accessible and vivid. That recent case was used as the primary comparison point, crowding out systematic review of Participant 12's own medication list and dosing timeline.",
      "manifestation_in_interview": "The participant stated that a recent team meeting case was the first thing that came to mind as a comparison point and later acknowledged leaning on it more than its similarity warranted because it was vivid.",
      "effect_on_reasoning_or_decision": "It produced an initial lean toward classifying the ALT elevation as unrelated before the participant had fully reviewed Participant 12's own file.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.",
          "evidence_explanation": "This shows that a readily available recent case, rather than the patient's own complete chart, initially shaped the comparison."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file.",
          "evidence_explanation": "This explicitly links the distortion to vividness and ease of recall rather than objective case similarity."
        }
      ],
      "correction_or_counterevidence": "The PI asked the participant to pull Participant 12's full lab history and prior meds before finalizing. The participant also admitted he probably should have done that upfront instead of after.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed the availability heuristic; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "satisficing",
      "alternative_labels": [
        "need for closure",
        "effort avoidance"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A decision strategy in which an option is accepted because it meets a minimal threshold or reduces effort, rather than optimizing based on full evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 12 AE category selection under closure pressure",
      "decision_point_description": "Choose between the data-supported but burdensome 'possibly related' category and a more closure-friendly category for the AE report.",
      "affected_reasoning_operation": "Categorization choice and burden-sensitivity in decision-making",
      "bias_specific_mechanism": "The participant recognized that the ambiguous 'possibly related' category was best supported by the data, but selected a definitive category to avoid additional paperwork and follow-up.",
      "manifestation_in_interview": "The participant said 'possibly related' was what the data supported best, but wanted something he could close out, so he picked a side.",
      "effect_on_reasoning_or_decision": "The final causality category was governed more by closure and workload avoidance than by the strength of the evidence.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.",
          "evidence_explanation": "This statement demonstrates that the participant knowingly selected a classification that was not the best supported by the data because it reduced follow-up burden."
        }
      ],
      "correction_or_counterevidence": "The PI later requested full lab history and prior meds before finalizing. The participant acknowledged that 'possibly related' was what the data supported best.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus text discusses satisficing as a decision process related to effort and information search, providing partial theoretical support for this classification.",
      "corpus_evidence": [
        {
          "source_identifier": "Azzopardi (2021). Cognitive Biases in Search.pdf",
          "paper_title": "Cognitive Biases in Search",
          "authors": "Azzopardi",
          "publication_year": "2021",
          "retrieved_passage_or_finding": "Alternatively, rather than trying to minimise effort, satisficing may be due to searchers trying to optimise the rate at which they encounter relevant information (as assumed in Information Foraging Theory and other related models of search based on Expected",
          "mechanism_supported_by_source": "The passage identifies satisficing as a distinct decision process involving reduced information evaluation in the presence of effort trade-offs.",
          "relevance_to_this_occurrence": "The participant selected a closure-friendly classification over the data-supported ambiguous option, consistent with satisficing under effort and workload considerations."
        }
      ]
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "sunk cost fallacy",
      "alternative_labels": [
        "escalation of commitment",
        "sunk cost effect"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Continuing a course of action because of previously invested resources, even when continued investment is unlikely to change the outcome.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 discrepancy resolution",
      "decision_point_description": "Decide whether to continue investigating Participant 07's dosing discrepancy or flag it as a deviation and/or obtain second review.",
      "affected_reasoning_operation": "Escalation and resource allocation decision",
      "bias_specific_mechanism": "Twenty hours of prior reconciliation effort made stopping feel wasteful, so the participant continued working despite limited evidence that the discrepancy could be resolved.",
      "manifestation_in_interview": "The participant reported that twenty hours felt like too much to walk away from without one more push, and later said stopping felt like it would waste everything already done.",
      "effect_on_reasoning_or_decision": "It delayed the decision to flag the discrepancy as a deviation and led to additional hours of work that did not change the outcome.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I kept going. Twenty hours felt like too much to walk away from without one more push.",
          "evidence_explanation": "This directly evidences sunk-sunk cost reasoning: prior effort justified further effort."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.",
          "evidence_explanation": "This further confirms escalation of commitment tied to previous investment and perceived loss."
        }
      ],
      "correction_or_counterevidence": "The discrepancy was ultimately not resolvable from available source documents; the extra time did not change the outcome, and it was flagged anyway, just later.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed the sunk cost fallacy; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "framing effect",
      "alternative_labels": [
        "loss aversion",
        "loss framing"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "A decision shift caused by whether equivalent outcomes are presented as losses or gains, with loss-framed outcomes typically exerting stronger influence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 discrepancy resolution under loss-framed email",
      "decision_point_description": "Evaluate whether continued reconciliation was worth the time after receiving the Site Director's email about the risk of losing evaluable participants.",
      "affected_reasoning_operation": "Risk interpretation and continuation decision",
      "bias_specific_mechanism": "The Site Director's email framed the issue as a potential loss of a fifth of the evaluable per-protocol population. This loss frame made the stakes feel heavier and independently reinforced continued effort.",
      "manifestation_in_interview": "The participant said the 'losing a fifth' framing stuck with him and later reflected that framed as a loss it felt heavier than it maybe should have.",
      "effect_on_reasoning_or_decision": "The loss frame increased perceived cost of stopping and reinforced the decision to keep working rather than flagging the case as a deviation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up.",
          "evidence_explanation": "This shows that the loss-framed presentation influenced the participant's reasoning beyond the objective information."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have.",
          "evidence_explanation": "This explicitly identifies the shift as due to framing rather than new evidence."
        }
      ],
      "correction_or_counterevidence": "The participant later recognized that the loss framing made the situation feel heavier than warranted, but only after the decision had already been made.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed framing effects or loss aversion; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "representativeness heuristic",
      "alternative_labels": [
        "representativeness bias",
        "prototype bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging probability or category membership by similarity to a mental prototype or stereotype, often ignoring objective criteria or base rates.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Wednesday referral screening triage",
      "decision_point_description": "Prioritize a new referral for screening under data-lock workload constraints.",
      "affected_reasoning_operation": "Eligibility screening and triage judgment",
      "bias_specific_mechanism": "The participant compared the new referral to the mental prototype of typical enrolled patients, who were older with multiple comorbidities. Because the referral did not match that pattern, the participant judged him as unlikely to qualify, despite the objective criteria being independent of that prototype.",
      "manifestation_in_interview": "The participant's first reaction was that the patient was probably not a great fit based on his picture, and he later acknowledged that this was not based on anything in the actual eligibility criteria but on a mismatch with the usual pattern.",
      "effect_on_reasoning_or_decision": "The participant placed the referral lower in the queue, delaying screening for a patient who ultimately met all inclusion criteria.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him.",
          "evidence_explanation": "This shows a rapid judgment based on perceived typicality rather than objective eligibility data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.",
          "evidence_explanation": "This confirms that the judgment relied on similarity to a familiar patient prototype rather than on the formal criteria."
        }
      ],
      "correction_or_counterevidence": "When eventually screened, the participant met every inclusion criterion. The participant acknowledged that deprioritizing him was not based on actual criteria, though a clean screen alone does not prove harm from the delay.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus text explicitly references representativeness bias as a clinical reasoning distortion involving case similarity to a targeted diagnosis or prototype.",
      "corpus_evidence": [
        {
          "source_identifier": "Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf",
          "paper_title": "Mitigating cognitive bias with clinical decision support systems: an experimental study",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "a description of a clinical manipulation to encourage representativeness bias ... increases the chance of ... targeted diagnosis",
          "mechanism_supported_by_source": "The source recognizes representativeness bias as a clinical reasoning distortion in which similarity to a targeted diagnostic pattern influences judgment.",
          "relevance_to_this_occurrence": "The participant used a mental prototype of the typical enrolled patient to triage a referral, rather than applying the objective eligibility criteria."
        }
      ]
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "moderate",
      "bias_label": "bandwagon effect",
      "alternative_labels": [
        "social proof",
        "herd behavior"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Adopting a behavior or decision because many others are doing it, rather than because of independent evidence that it is correct or superior.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Thursday coordinator call verification method switch",
      "decision_point_description": "Decide whether to switch from the site's audit-clean source data verification approach to the quicker method mentioned by other sites.",
      "affected_reasoning_operation": "Method selection and evidence evaluation",
      "bias_specific_mechanism": "Hearing that most other sites had already switched made staying with the current method feel like being behind. The participant did not seek or wait for validation data and treated consensus as sufficient evidence of quality.",
      "manifestation_in_interview": "The participant reported that no one shared error rates, but he switched anyway because many other sites were doing it and 'if that many sites were doing it, it was probably fine.'",
      "effect_on_reasoning_or_decision": "The site changed a previously audit-clean method without documented rationale, later prompting the monitor to question the decision.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
          "evidence_explanation": "This demonstrates that social consensus replaced independent evidence evaluation in the decision to switch."
        }
      ],
      "correction_or_counterevidence": "The monitor later asked why the method was changed without documented rationale. The participant had no evidence beyond 'everyone else was doing it too.'",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved corpus passage directly addressed the bandwagon effect or social proof; classification relies on established cognitive-science knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "The analysis relies on participant self-report, which may include post-hoc rationalization or incomplete recall of internal reasoning.",
    "Several classifications rely on established cognitive-science knowledge because direct retrieved corpus support was not available for every bias.",
    "The interview captures a single participant's experience during a high-workload period, so contextual and organizational constraints may also have influenced decisions.",
    "The retrieved corpus passages were limited and partially fragmented, especially for representativeness bias and satisficing."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for making time this week of all weeks. Before we start, this is just for our internal process-improvement review — I'll ask you to walk me through a recent stretch of work, and there's no wrong answer. That okay? Participant: Sure, happy to. Lock week is a good time to talk about it, honestly, everything's still fresh. Interviewer: Great. Can you remind me of your role and what was on your plate? Participant: I'm the CRC for our site on the Phase III trial — the oncology drug study. I handle adverse event triage, case report form cleanup, and screening new referrals. That week we were seven days out from the interim data lock for the DSMB, so basically everything converged at once. Interviewer: Walk me through what that week looked like. Participant: Monday morning I got a lab flag on Participant 12 — an ALT elevation, elevated but not dramatically so, and the timeline relative to dosing wasn't clean. Could've been drug-related, could've been something else entirely, maybe even diet or an OTC medication he didn't mention. I had to assign a causality category for the AE report. Same day, I was also mid-reconciliation on Participant 07's case report forms — that one had been a slog for almost two weeks, lots of inconsistent entries between the source charts and the CRF. Then Wednesday a new referral came in for screening, and Thursday there was a multi-site coordinator call about verification procedures ahead of lock. So four distinct things, all against the same deadline. Interviewer: Let's start with Participant 12. What did you have in front of you? Participant: His ALT was elevated, but in a range where you genuinely can't tell just from the number whether it's the study drug. Our protocol has three buckets — related, possibly related, unrelated — for exactly this kind of situation. I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point. Interviewer: How did that shape the classification? Participant: I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed. Interviewer: What about the 'possibly related' option? Participant: Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side. Interviewer: What happened after? Participant: The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after. Interviewer: Let's move to Participant 07. Participant: That one's been painful. I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records. Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that. Interviewer: What did you do with that discrepancy? Participant: I kept going. Twenty hours felt like too much to walk away from without one more push. And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it. Interviewer: Did you consider flagging it as a deviation instead? Participant: I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours. Interviewer: How did it turn out? Participant: The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later. Interviewer: Let's talk about the new referral on Wednesday. Participant: He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has. Interviewer: What did you do with that instinct? Participant: I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through. Interviewer: What happened when you did screen him? Participant: He met every inclusion criterion. Clean screen, no issues. Which doesn't tell you much either way about whether deprioritizing him was the right call — I just got lucky that lock week didn't cost us his enrollment. Interviewer: Last one — the coordinator call about verification. Participant: Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever. Interviewer: What made you switch? Participant: Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine. Interviewer: Any pushback since? Participant: The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.' Interviewer: If you could go back, what single piece of information would have changed any of these calls? Participant: For Participant 12, if I'd pulled his full history first instead of after, I might not have leaned so hard on that other case. For the verification switch, actual error-rate data would've mattered — I just didn't have it and didn't chase it down in time. Interviewer: What if that Monday meeting about the other participant's enzyme case had never come up? Participant: I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind. Interviewer: And if the Site Director's email had framed Participant 07 differently — say, just asking whether continued reconciliation was worth the time? Participant: I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have. Interviewer: Last one — if none of the other sites had mentioned switching methods on that call? Participant: I probably would've stuck with what we had. It's passed every audit. There wasn't really a problem to solve, other than speed.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.89s · gen 160.20s · total 164.2s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0249 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0246 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0237 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0201 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0199 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
11. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0188 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
12. **Hallihan_etal_DTM_12.pdf** — 0.0183 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
13. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0173 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
14. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0163 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
23. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0153 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
27. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0153 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
28. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0153 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
29. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0153 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0148 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
32. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0147 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0147 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
35. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0145 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0144 (rrf) — _# fi cation patient vignettes. JAMA Netw. Open 5. Ito, N. et al. The accuracy and potential raci_
37. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0144 (rrf) — _# Experiment 3 Mean number of misclassications on the three blocks of 40/60 trials in the AIassi_
38. **Lyell Automation bias and verification complexity.pdf** — 0.0144 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
39. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
40. **Lyell Automation bias and verification complexity.pdf** — 0.0141 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
42. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0139 (rrf) — _# support et al., 2019 ; Phillips-Wren, base rate data can in the estimate influenced by the pre_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0137 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. Chan, U. Dulleck et al. conductedadditionalana_
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
46. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0136 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# to Dangers from Humans I am more and more convinced that Man is a dangerous creature, and that_
48. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0134 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
49. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0133 (rrf) — _# Self - other Placement W ith no other evidence chance of success w ould also the p rinciple of_
50. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0133 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Single interview transcript analyzed for distinct cognitive-bias occurrences. Retrieved corpus support was used where available; several labels derive from general cognitive-science taxonomy because no suitable retrieved passage was present."
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
      "bias_label": "Representativeness heuristic",
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
      "bias_label": "Availability heuristic",
      "alternative_labels": [
        "Recency effect",
        "Availability bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judgments are influenced by the ease with which examples come to mind; recent, vivid, or salient cases are over-weighted as reference points.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Classification of Participant 12 ALT elevation causality",
      "decision_point_description": "Assign a causality category for Participant 12's AE report as related, possibly related, or unrelated.",
      "affected_reasoning_operation": "Causal attribution / classification of adverse event",
      "bias_specific_mechanism": "A recent, vivid team-meeting case came to mind easily and became the primary comparison point, displacing a fuller review of Participant 12's own file.",
      "manifestation_in_interview": "The participant explicitly says the recent conversation was 'the first thing that came to mind' and that he leaned on it more than he should have because it was 'the most vivid thing' in his head.",
      "effect_on_reasoning_or_decision": "He leaned toward classifying Participant 12's ALT elevation as unrelated and delayed reviewing Participant 12's own medication list and dosing timeline.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.",
          "evidence_explanation": "This shows accessibility of the recent event influencing the initial comparison for the current judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file.",
          "evidence_explanation": "The participant identifies that vividness/ease of recall, not case similarity, drove the influence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind.",
          "evidence_explanation": "This counterfactual explicitly links the recent accessible case to the reduced use of case-specific information."
        }
      ],
      "correction_or_counterevidence": "The PI asked for full lab history and prior meds before finalizing, and the participant acknowledged he should have done that up front. This was a corrective request after the initial leaning, not an in-the-moment neutralization.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "Retrieved corpus contains a recency-effect passage supporting the accessibility/recency component of the availability mechanism.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": "2016",
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Recent events are more easily remembered and can become the most accessible comparison or reference point.",
          "relevance_to_this_occurrence": "The participant's Monday team-meeting discussion was recent, and that recent case came to mind first and became the comparison point for classifying Participant 12."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Sunk cost fallacy",
      "alternative_labels": [
        "Escalation of commitment"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Tendency to continue an endeavor because of previously invested resources, even when the current information suggests stopping or changing course would be more rational.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 CRF reconciliation after new dosing discrepancy",
      "decision_point_description": "Decide whether to continue reconciliation or flag as a deviation / obtain a second reviewer after a new dosing-record discrepancy.",
      "affected_reasoning_operation": "Decision to continue vs stop after irrecoverable effort",
      "bias_specific_mechanism": "Previously invested hours were treated as a reason to continue rather than evaluating whether further effort was likely to resolve the discrepancy.",
      "manifestation_in_interview": "The participant says twenty hours felt like too much to walk away from and that stopping felt like it would waste everything already done.",
      "effect_on_reasoning_or_decision": "He continued reconciliation for another few hours instead of flagging the discrepancy or getting a second reviewer; the discrepancy was ultimately unresolved and flagged later.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records.",
          "evidence_explanation": "The prior investment is made salient immediately before the decision point about the new discrepancy."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I kept going. Twenty hours felt like too much to walk away from without one more push.",
          "evidence_explanation": "This explicitly bases continuation on the irrecoverable time already spent."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.",
          "evidence_explanation": "The participant treats past effort as something that would be wasted by stopping, a classic sunk-cost reasoning pattern."
        }
      ],
      "correction_or_counterevidence": "The participant did consider flagging as a deviation and obtaining a second reviewer, but sunk-cost reasoning prevailed. The extra time did not change the outcome; the discrepancy was flagged later anyway.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism derive from general cognitive-science taxonomy; no suitable retrieved passage was available in the provided corpus.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Framing effect",
      "alternative_labels": [
        "Loss aversion"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Choices shift depending on whether outcomes are presented as gains or losses, with losses typically weighted more heavily than equivalent gains.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Response to Site Director's loss-framed email about Participant 07",
      "decision_point_description": "Decide whether to continue reconciliation after the Site Director framed stopping as losing a fifth of the evaluable per-protocol population.",
      "affected_reasoning_operation": "Valuation of options under loss framing",
      "bias_specific_mechanism": "The choice was evaluated through a loss frame ('we lose a fifth of our evaluable per-protocol population'), making stopping feel heavier than a neutral or gain-framed evaluation.",
      "manifestation_in_interview": "The participant says the loss framing stuck with him and that, framed as a loss, it felt heavier than it maybe should have.",
      "effect_on_reasoning_or_decision": "The loss-framed communication amplified the perceived cost of stopping and reinforced the decision to continue reconciliation.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that.",
          "evidence_explanation": "The decision was explicitly presented in terms of a potential loss."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up.",
          "evidence_explanation": "The participant reports that the loss frame changed the perceived stakes."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Framed as a loss, it felt heavier than it maybe should have.",
          "evidence_explanation": "This explicitly identifies the loss frame as producing disproportionate weight in the decision."
        }
      ],
      "correction_or_counterevidence": "The participant later acknowledged that if the email had framed the question neutrally, he might have stopped sooner. This is retrospective awareness rather than an in-period correction.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism derive from general cognitive-science taxonomy; no suitable retrieved passage was available in the provided corpus.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Representativeness heuristic",
      "alternative_labels": [
        "Representativeness bias",
        "Prototype bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Judgments of likelihood or fit are based on similarity to a category prototype rather than on objective criteria, base rates, or diagnostic information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Screening prioritization of new referral",
      "decision_point_description": "Prioritize and assess the new referral relative to objective eligibility criteria.",
      "affected_reasoning_operation": "Screening prioritization / eligibility judgment",
      "bias_specific_mechanism": "The participant judged whether the referral was likely to qualify by matching him to the typical enrolled-patient prototype, rather than by applying the objective inclusion criteria.",
      "manifestation_in_interview": "The participant says his first reaction was that the referral probably was not a great fit 'just based on the picture of him' and that the judgment was not based on actual criteria but on the pattern he was used to seeing.",
      "effect_on_reasoning_or_decision": "He put the referral lower in the screening queue; the referral later met every inclusion criterion.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him.",
          "evidence_explanation": "This shows prototype matching as the basis for the initial eligibility impression."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway.",
          "evidence_explanation": "The prototype-based judgment affected a screening prioritization decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.",
          "evidence_explanation": "The participant explicitly distinguishes the prototype judgment from objective criteria."
        }
      ],
      "correction_or_counterevidence": "When screened, the referral met every inclusion criterion, showing that the initial prototype-based deprioritization was not diagnostically valid. The participant noted he got lucky that lock week did not cost enrollment.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism derive from general cognitive-science taxonomy; no suitable retrieved passage was available in the provided corpus.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "Bandwagon effect",
      "alternative_labels": [
        "Social proof",
        "Conformity bias"
      ],
      "taxonomy_status": "established_label",
      "bias_definition": "Adopting beliefs, actions, or practices because other people are doing so, rather than independently evaluating the evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Adoption of new source data verification method before lock",
      "decision_point_description": "Decide whether to switch from the existing source data verification approach to the method mentioned by other sites.",
      "affected_reasoning_operation": "Adoption of verification method",
      "bias_specific_mechanism": "The number of other sites using the method substituted for evidence about the method's error rate or appropriateness.",
      "manifestation_in_interview": "The participant says hearing that most other sites had moved to the new method made staying with the old method feel like being behind, and he did not seek validation data before switching.",
      "effect_on_reasoning_or_decision": "He changed verification methods without documented rationale or validation data, and later could only explain the change by saying others were doing it too.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind.",
          "evidence_explanation": "The social consensus, rather than evidence, is given as the reason for changing methods."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
          "evidence_explanation": "This explicitly shows the use of prevalence among sites as a substitute for evidence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.'",
          "evidence_explanation": "The participant's only available rationale was social conformity, confirming the bandwagon mechanism."
        }
      ],
      "correction_or_counterevidence": "The monitor questioned the lack of documented rationale, but no pre-decision correction or evidence review occurred.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "Label and mechanism derive from general cognitive-science taxonomy; no suitable retrieved passage was available in the provided corpus.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Single interview transcript, retrospectively self-reported; no independent performance or outcome data were available.",
    "Retrieved corpus support was available for only the recency/availability occurrence; other labels rely on established general cognitive-science taxonomy.",
    "The analysis is limited to what the participant reported and does not include direct observation of the decisions.",
    "Some quotations involve retrospective self-assessment, which may itself be affected by recall or self-presentation considerations."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for making time this week of all weeks. Before we start, this is just for our internal process-improvement review — I'll ask you to walk me through a recent stretch of work, and there's no wrong answer. That okay? Participant: Sure, happy to. Lock week is a good time to talk about it, honestly, everything's still fresh. Interviewer: Great. Can you remind me of your role and what was on your plate? Participant: I'm the CRC for our site on the Phase III trial — the oncology drug study. I handle adverse event triage, case report form cleanup, and screening new referrals. That week we were seven days out from the interim data lock for the DSMB, so basically everything converged at once. Interviewer: Walk me through what that week looked like. Participant: Monday morning I got a lab flag on Participant 12 — an ALT elevation, elevated but not dramatically so, and the timeline relative to dosing wasn't clean. Could've been drug-related, could've been something else entirely, maybe even diet or an OTC medication he didn't mention. I had to assign a causality category for the AE report. Same day, I was also mid-reconciliation on Participant 07's case report forms — that one had been a slog for almost two weeks, lots of inconsistent entries between the source charts and the CRF. Then Wednesday a new referral came in for screening, and Thursday there was a multi-site coordinator call about verification procedures ahead of lock. So four distinct things, all against the same deadline. Interviewer: Let's start with Participant 12. What did you have in front of you? Participant: His ALT was elevated, but in a range where you genuinely can't tell just from the number whether it's the study drug. Our protocol has three buckets — related, possibly related, unrelated — for exactly this kind of situation. I remembered we'd just talked about a different participant's enzyme bump in Monday's team meeting, and that one was pretty clearly unrelated, some pre-existing condition. When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point. Interviewer: How did that shape the classification? Participant: I ended up leaning unrelated. Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file. I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed. Interviewer: What about the 'possibly related' option? Participant: Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side. Interviewer: What happened after? Participant: The PI actually asked me to go back and pull his full lab history and prior meds before finalizing it. Which, fair — I probably should've done that up front instead of after. Interviewer: Let's move to Participant 07. Participant: That one's been painful. I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data. Then this new discrepancy showed up, bigger than the others, in his dosing records. Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that. Interviewer: What did you do with that discrepancy? Participant: I kept going. Twenty hours felt like too much to walk away from without one more push. And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up. So I dug in for another few hours trying to resolve it. Interviewer: Did you consider flagging it as a deviation instead? Participant: I did — that was one of the options on the table, along with getting a second reviewer to look before deciding. But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours. Interviewer: How did it turn out? Participant: The discrepancy wasn't resolvable from what we had. The source documents just didn't exist to fix it. So the extra time didn't change the outcome — we flagged it anyway, just later. Interviewer: Let's talk about the new referral on Wednesday. Participant: He was younger, active, no real comorbidities on paper — which is not what our typical enrolled patient looks like. Most of our participants are older with two or three coexisting conditions. My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him. Our actual eligibility criteria are objective — biomarker status, prior treatment lines, organ function — none of which care about age or how many other conditions someone has. Interviewer: What did you do with that instinct? Participant: I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway. In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through. Interviewer: What happened when you did screen him? Participant: He met every inclusion criterion. Clean screen, no issues. Which doesn't tell you much either way about whether deprioritizing him was the right call — I just got lucky that lock week didn't cost us his enrollment. Interviewer: Last one — the coordinator call about verification. Participant: Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method. Our own approach has passed every audit clean, no findings, ever. Interviewer: What made you switch? Participant: Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind. I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine. Interviewer: Any pushback since? Participant: The monitor asked why we changed methods without a documented rationale. I didn't have a great answer beyond 'everyone else was doing it too.' Interviewer: If you could go back, what single piece of information would have changed any of these calls? Participant: For Participant 12, if I'd pulled his full history first instead of after, I might not have leaned so hard on that other case. For the verification switch, actual error-rate data would've mattered — I just didn't have it and didn't chase it down in time. Interviewer: What if that Monday meeting about the other participant's enzyme case had never come up? Participant: I think I'd have gone through Participant 12's own file more carefully from scratch, instead of measuring him against something else that happened to be fresh in my mind. Interviewer: And if the Site Director's email had framed Participant 07 differently — say, just asking whether continued reconciliation was worth the time? Participant: I might've stopped sooner. Framed as a loss, it felt heavier than it maybe should have. Interviewer: Last one — if none of the other sites had mentioned switching methods on that call? Participant: I probably would've stuck with what we had. It's passed every audit. There wasn't really a problem to solve, other than speed.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.82s · gen 272.46s · total 276.4s_

**Retrieved** (ranked by store ranker):
1. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0249 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
2. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0246 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0242 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0237 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0201 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
7. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0199 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
8. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0191 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
9. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0191 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
10. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0191 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
11. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0188 (rrf) — _# fi cation afterward. I also felt attack in his early 60 Afterreviewingthecasevignetteandassoci_
12. **Hallihan_etal_DTM_12.pdf** — 0.0183 (rrf) — _Participant c onclusions participants were asked to evaluate, concluded that there was a signifi_
13. **From Mindless to Mindful Practice — Cognitive Bias and Clinical Decision Making.pdf** — 0.0173 (rrf) — _#### june 27, 2013 the resident and the attending physician regarding the management of posterio_
14. **Hallihan_etal_DTM_12.pdf** — 0.0173 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
15. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0173 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
16. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0173 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
17. **Hallihan_etal_DTM_12.pdf** — 0.0172 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
18. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0163 (rrf) — _# fi cation 13,14 studies . In either case, our statistical model (Supplementary Table 6) showed_
21. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0163 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
22. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0161 (rrf) — _# 4 Anchoring bias the coecient of a linear regression fit on average disagreement vs. time allo_
23. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
24. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0157 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
25. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
26. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0153 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
27. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0153 (rrf) — _### cKniff 2004 ; Radley et al., 2013 and reporting others about medication errors, and it foste_
28. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0153 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
29. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0153 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
30. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0148 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
31. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0148 (rrf) — _# References This appendix gives an introduction to the logic of noise influenced memory decisio_
32. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0147 (rrf) — _## Noise (Ê\|M) between Memory and Êstimate: the Confidence Bias TOWARD A SYN THESIS OF COGNITIV_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD pit e these strengths, our study has several limitations. First, our and use_
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0147 (rrf) — _# Experiment 1 about their own performance and about how they had perceived the AI’s performance_
35. **Cognitive bias and decision aid use under stressful conditions.pdf** — 0.0145 (rrf) — _### cKniff At the time of this study, CDSS were available to nurses in the form of computers and_
36. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0144 (rrf) — _# fi cation patient vignettes. JAMA Netw. Open 5. Ito, N. et al. The accuracy and potential raci_
37. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0144 (rrf) — _# Experiment 3 Mean number of misclassications on the three blocks of 40/60 trials in the AIassi_
38. **Lyell Automation bias and verification complexity.pdf** — 0.0144 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
39. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0142 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
40. **Lyell Automation bias and verification complexity.pdf** — 0.0141 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
41. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0140 (rrf) — _## Uwe Dulleck, PhD tive biases or risktaking behavior and triage accuracy varied according 2.1._
42. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0139 (rrf) — _# support et al., 2019 ; Phillips-Wren, base rate data can in the estimate influenced by the pre_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0138 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
44. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0137 (rrf) — _## Uwe Dulleck, PhD T.N. Egoda Kapuralalage, H.F. Chan, U. Dulleck et al. conductedadditionalana_
45. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0136 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
46. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0136 (rrf) — _# fi cation 8 demonstrating human biases in clinical interpretation. Participants were randomize_
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0136 (rrf) — _# to Dangers from Humans I am more and more convinced that Man is a dangerous creature, and that_
48. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0134 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
49. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0133 (rrf) — _# Self - other Placement W ith no other evidence chance of success w ould also the p rinciple of_
50. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0133 (rrf) — _## Uwe Dulleck, PhD researchshouldundertakecomparativeanalysesofthein nitive biases and heuristi_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": true,
    "analysis_scope_note": "Analysis focused on the participant's reported reasoning across four work episodes: adverse event causality classification, CRF/discrepancy reconciliation, referral screening prioritization, and source data verification method selection. Only mechanisms affirmatively evidenced in the participant's own statements were classified."
  },
  "identified_bias_summary": [
    {
      "bias_label": "availability heuristic",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "bandwagon effect",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "escalation of commitment",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "loss aversion",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "need for cognitive closure",
      "identified_occurrence_count": 1
    },
    {
      "bias_label": "representativeness heuristic",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "availability heuristic",
      "alternative_labels": ["availability bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judgment is influenced by the ease with which examples come to mind; a recent or vivid instance is overused as a comparison point.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 12 adverse event causality classification",
      "decision_point_description": "Assigning a causality category for Participant 12's elevated ALT lab flag.",
      "affected_reasoning_operation": "Causal attribution of an adverse event to study drug versus other causes.",
      "bias_specific_mechanism": "The participant used a recent, vivid team-meeting case about a different participant's enzyme bump as the primary comparison point, overweighting that example and reducing careful review of Participant 12's own file.",
      "manifestation_in_interview": "The participant states that the recent conversation was the first thing that came to mind as a comparison, and that he leaned on it more than he should have because it was vivid, not necessarily most similar.",
      "effect_on_reasoning_or_decision": "The participant leaned toward 'unrelated' and spent less time reviewing Participant 12's own medication list and dosing timeline than he otherwise would have.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "When I sat with Participant 12's chart, that recent conversation was sort of the first thing that came to mind as a comparison point.",
          "evidence_explanation": "Directly demonstrates that a recent example became the primary cognitive comparison, a hallmark of availability-based judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Looking back, I did lean on that other case more than I probably should have — it was the most vivid thing in my head, not necessarily the most similar case in the file.",
          "evidence_explanation": "Explicitly identifies vividness/recent availability rather than similarity or diagnostic evidence as the driver."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't spend as much time going back through his own med list and the dosing timeline as I would on a case that didn't remind me of something we'd just discussed.",
          "evidence_explanation": "Shows that the availability of the recent case changed the depth and direction of evidence search."
        }
      ],
      "correction_or_counterevidence": "The PI later asked the participant to pull Participant 12's full lab history and prior meds before finalizing; the participant acknowledged that this should have been done up front.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved source supports the recency/vividness component of this availability judgment; the broader availability heuristic label is also supported by general cognitive-science knowledge.",
      "corpus_evidence": [
        {
          "source_identifier": "natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf",
          "paper_title": null,
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "Recency Effect. The tendency for participants to remember recent events more clearly.",
          "mechanism_supported_by_source": "Recency increases salience or accessibility of recent events, mirroring why the recent Monday team-meeting case became the first comparison point.",
          "relevance_to_this_occurrence": "The participant explicitly attributes the availability of the comparison case to its recency and vividness, which the retrieved passage describes."
        }
      ]
    },
    {
      "occurrence_id": "obs_002",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "need for cognitive closure",
      "alternative_labels": ["closure bias", "premature closure"],
      "taxonomy_status": "established_label",
      "bias_definition": "A motivated tendency to seek an immediate, definite answer and avoid ambiguity, even when evidence is inconclusive.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 12 adverse event causality classification",
      "decision_point_description": "Choosing among the protocol causality categories when 'possibly related' was the best-supported but open-ended option.",
      "affected_reasoning_operation": "Selection of a causality category under ambiguity.",
      "bias_specific_mechanism": "The participant preferred a definitive category that could be closed out over an ambiguous category requiring further action, leading to a premature side choice.",
      "manifestation_in_interview": "The participant reports that 'possibly related' was technically best supported by the data but would create more paperwork and follow-up, then states that he wanted something he could close out and picked a side.",
      "effect_on_reasoning_or_decision": "The decision shifted away from the known-ambiguous but data-supported category toward a more definitive, closure-friendly classification.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Technically that's what the data supported best, if I'm honest. It's genuinely ambiguous — that's the whole problem. But 'possibly related' kind of kicks the can down the road, more paperwork, more follow-up, and I wanted something I could close out. So I picked a side.",
          "evidence_explanation": "Shows a motivational preference for closure over diagnostic accuracy and its direct effect on category choice."
        }
      ],
      "correction_or_counterevidence": "The PI's later request for full history and prior meds served as an external check; the participant recognized that the definitive choice had been premature.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically addressed need for cognitive closure; this label rests on established cognitive-scientific and motivated-cognition knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_003",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "escalation of commitment",
      "alternative_labels": ["sunk cost fallacy", "sunk cost effect"],
      "taxonomy_status": "established_label",
      "bias_definition": "Continued investment in a course of action based on the amount already invested, even when current evidence indicates that persistence is not justified.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 dosing discrepancy reconciliation",
      "decision_point_description": "Deciding whether to continue trying to resolve the discrepancy versus flagging it as a deviation or getting a second reviewer.",
      "affected_reasoning_operation": "Evaluation of whether to continue resource investment in an unresolved data discrepancy.",
      "bias_specific_mechanism": "The participant treated the prior 20 hours of work as a reason to continue even though those hours were sunk and could not be recovered, and overweighted the perceived waste of stopping.",
      "manifestation_in_interview": "The participant explicitly frames the 20 hours as too much to walk away from and says stopping felt like wasting everything already done, then invests more hours.",
      "effect_on_reasoning_or_decision": "The participant decided against stopping or flagging at that point and spent additional hours attempting reconciliation; the discrepancy later proved unresolvable.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "I'd logged something like twenty hours on it already — chasing source documents, calling the site nurse, re-entering data.",
          "evidence_explanation": "Establishes the irretrievable past investment used as a basis for persistence."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Twenty hours felt like too much to walk away from without one more push.",
          "evidence_explanation": "Directly expresses sunk-cost reasoning."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "But at the time, stopping felt like it would waste everything already done, and losing that many evaluable participants sounded worse than more of my hours.",
          "evidence_explanation": "Shows that anticipated waste drove continued investment; the loss component is addressed separately in the loss-aversion occurrence."
        }
      ],
      "correction_or_counterevidence": "The participant did consider flagging the issue as a deviation or getting a second reviewer; the discrepancy was ultimately not resolvable and was flagged later, so the extra time did not change the outcome.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically addressed escalation of commitment or sunk cost effects; this label rests on general cognitive-science knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_004",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "loss aversion",
      "alternative_labels": ["framing effect", "loss framing"],
      "taxonomy_status": "established_label",
      "bias_definition": "Losses are weighed more heavily than equivalent gains; decisions shift when options are framed in terms of avoiding losses.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Participant 07 dosing discrepancy reconciliation",
      "decision_point_description": "Whether to continue reconciliation after a new discrepancy when the Site Director framed stopping as losing a fifth of the evaluable per-protocol population.",
      "affected_reasoning_operation": "Weighting of potential losses versus gains in deciding whether to continue reconciliation.",
      "bias_specific_mechanism": "The Site Director's message framed the choice as a loss rather than as a neutral evaluation of continued effort; the participant experienced this loss framing as heavier than it should have been.",
      "manifestation_in_interview": "The participant reports that the 'losing a fifth of our population' framing stuck with him more than expected and later says that framed as a loss, it felt heavier than it should have.",
      "effect_on_reasoning_or_decision": "The loss framing made stopping feel more costly and contributed to the participant's decision to keep working on the discrepancy rather than flagging it or seeking review.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Around the same time, our Site Director emailed the team saying essentially: we either recover the work we've put into this case, or we lose a fifth of our evaluable per-protocol population. Framed exactly like that.",
          "evidence_explanation": "Shows the choice was framed around a potential loss, activating loss-sensitive weighting."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "And honestly the 'losing a fifth of our population' framing stuck with me more than I expected — it wasn't just about the hours anymore, it became about what we'd be giving up.",
          "evidence_explanation": "Directly demonstrates that the framing changed the participant's subjective weighting of the decision."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Framed as a loss, it felt heavier than it maybe should have.",
          "evidence_explanation": "Explicitly recognizes loss-aversion weighting."
        }
      ],
      "correction_or_counterevidence": "The participant acknowledged that if the email had framed the decision neutrally, he might have stopped sooner; the eventual outcome showed the discrepancy was not recoverable.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported loss aversion; this label rests on established judgment-and-decision-making knowledge.",
      "corpus_evidence": []
    },
    {
      "occurrence_id": "obs_005",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "representativeness heuristic",
      "alternative_labels": ["representativeness bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Judging likelihood or fit by similarity to a prototype or previously observed pattern rather than by applying objective criteria.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "New referral screening prioritization",
      "decision_point_description": "Whether to prioritize and screen a new referral who appeared atypical relative to the site's usual enrolled patient population.",
      "affected_reasoning_operation": "Initial assessment of patient fit and queue placement.",
      "bias_specific_mechanism": "The participant assessed eligibility by similarity to the prototype of an older patient with comorbidities rather than the objective protocol inclusion criteria; this pattern mismatch drove the preliminary judgment.",
      "manifestation_in_interview": "The participant reports a first reaction that the patient was probably not a great fit based on the picture of him, placed him lower in queue, and later acknowledged this was not based on actual criteria.",
      "effect_on_reasoning_or_decision": "The patient was deprioritized; although he eventually screened successfully, the prioritization decision was based on a mental prototype rather than objective eligibility factors.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "My first reaction honestly was that he probably wasn't a great fit, just based on the picture of him.",
          "evidence_explanation": "Shows prototype-based initial judgment."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I put him lower in the queue. I told myself I'd get to him after the other things settled down, since he 'probably' wasn't going to qualify anyway.",
          "evidence_explanation": "Shows the judgment affected queue/prioritization behavior."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "In hindsight that wasn't based on anything in the actual criteria — it was more that he didn't match the pattern I'm used to seeing come through.",
          "evidence_explanation": "Directly confirms reliance on similarity to a familiar pattern rather than objective criteria."
        }
      ],
      "correction_or_counterevidence": "When actually screened, the patient met every inclusion criterion; the participant acknowledged being lucky that lock week did not cost his enrollment.",
      "retrieved_corpus_support_available": true,
      "corpus_support_note": "The retrieved passage supports the use of representativeness bias in clinical diagnostic judgment tasks; the referral screening pattern-match mechanism is consistent with that described pattern.",
      "corpus_evidence": [
        {
          "source_identifier": "Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf",
          "paper_title": "Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf",
          "authors": null,
          "publication_year": null,
          "retrieved_passage_or_finding": "manipulation to encourage representativeness bias ... a description of a clinical ... targeted diagnosis.",
          "mechanism_supported_by_source": "The source discusses using clinical vignettes to induce representativeness bias in diagnostic probability judgments.",
          "relevance_to_this_occurrence": "The participant's screening judgment similarly used a familiar patient pattern rather than objective protocol criteria, consistent with representativeness-driven clinical judgment."
        }
      ]
    },
    {
      "occurrence_id": "obs_006",
      "classification_status": "identified",
      "confidence": "high",
      "bias_label": "bandwagon effect",
      "alternative_labels": ["social proof", "conformity bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "Adopting a belief or practice because many others appear to have adopted it, sometimes without seeking independent evidence.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Source data verification method switch",
      "decision_point_description": "Whether to continue the current audit-clean verification method or switch to the quicker method other sites had adopted.",
      "affected_reasoning_operation": "Selection of a clinical data verification procedure.",
      "bias_specific_mechanism": "Information about what most other sites were doing created a sense of lagging behind; the participant inferred the method was probably fine from perceived consensus without seeking error-rate data.",
      "manifestation_in_interview": "The participant reports switching after hearing most other sites had moved to the new method, says staying with the old method felt like being behind, and did not look for validation data.",
      "effect_on_reasoning_or_decision": "The site changed verification methods without documented rationale or validation data; the monitor later questioned the lack of rationale.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Thursday's call, a few other sites mentioned they'd already switched to a quicker source data verification approach to get through lock faster. Nobody on the call actually shared numbers on error rates for the new method.",
          "evidence_explanation": "Establishes that the decision relied on social information without performance data."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "Honestly, hearing that most of the other sites had already moved to it made staying with our old method feel like we were behind.",
          "evidence_explanation": "Shows that social consensus influenced the perceived status of the current practice."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "I didn't go looking for any validation data before switching — I just figured if that many sites were doing it, it was probably fine.",
          "evidence_explanation": "Directly states the bandwagon inference from quantity of adopters to validity."
        }
      ],
      "correction_or_counterevidence": "The monitor later asked why the method was changed without documented rationale; the participant had no answer beyond 'everyone else was doing it too.'",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "No retrieved passage specifically supported bandwagon or social proof effects; this label rests on established social-influence and heuristic knowledge.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [],
  "no_supported_biases_found": false,
  "limitations": [
    "Retrieved corpus coverage was sparse for several of the identified biases; availability, need for cognitive closure, escalation of commitment, loss aversion, and bandwagon effect rest on established general cognitive-science knowledge rather than retrieved passages.",
    "The transcript is a self-reported retrospective account, so some statements are recollections and may be shaped by reconstructive processes; classifications are based only on affirmative statements in that account."
  ]
}

