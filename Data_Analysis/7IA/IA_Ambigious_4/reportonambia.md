# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is being recorded for internal case-review purposes only, and you can skip anything you'd rather not go into. Can you start by telling me your role and background? Participant: Sure. I'm a financial crime intelligence analyst on the FIU team, been in this specific role about six years, mostly trade finance and sanctions typologies before that. Interviewer: I want to walk through a specific case — the Halcyon Freight matter. Can you tell me how it came to your attention and what you were trying to achieve? Participant: It came in as part of a batch alert — four counterparties flagged together. Halcyon Freight Partners was one of them, along with a commodities trader, a small logistics subcontractor, and a shipping agent. My objective was the usual one: figure out whether there was enough here to warrant an escalation to compliance and possibly law enforcement, and do it within the ten-day filing window. Interviewer: What did the batch actually show you? Participant: Halcyon had one indicator that stood out — an invoice value gap, meaning the declared value didn't match what we'd expect for the goods described. No beneficial-ownership overlap with anything I'd seen before, so it wasn't ringing any specific bells. The commodities trader had a minor documentation gap, but nothing typologically interesting. It was a fairly normal week workload-wise, nothing especially heavy. Interviewer: Walk me through what you did once you had that picture. Participant: I prioritized Halcyon first, since the invoice gap was the clearest indicator I had to work with, and documented a plan to get through the other three that same week. I didn't ignore them — I just sequenced based on which indicator looked most substantive on its face. Interviewer: What made you order it that way rather than, say, splitting time evenly or going by transaction size? Participant: Honestly, either of those would have been defensible too. I went with indicator strength because that's usually a decent proxy for where the real risk sits, but I'll admit transaction size might have surfaced something different. I made a note of the reasoning in case anyone asked. Interviewer: Did anyone ask? Participant: Yeah, my team lead did, later. Wanted to know why I'd sequenced it that way. I walked her through the invoice-gap rationale and she was fine with it — it wasn't the only reasonable choice, but it wasn't unreasonable either. Interviewer: What came out of the other three once you got to them? Participant: The shipping agent turned out to have an administrative filing delay — paperwork lag, not a risk issue at all. Nothing on the logistics subcontractor either. So the sequencing didn't really cost us anything in the end, though I can't say for certain it wouldn't have mattered in a different case. Interviewer: Let's move to the vendor report. What happened there? Participant: A few days in, our OSINT vendor sent a report saying Halcyon's ownership structure was 'plausibly consistent' with a known layering pattern. Importantly, they flagged it as moderate confidence themselves and noted one registry link hadn't been independently verified yet. Interviewer: How did you decide how much weight to give that? Participant: A colleague suggested we get a second data pull to firm up that specific link before leaning on the report too heavily. I thought that was reasonable, so I treated the report as partial corroboration — enough to keep building the file, not enough to treat as settled — while the second pull was requested in parallel. Interviewer: Was there a version of this where you'd have leaned harder on the report, or set it aside entirely? Participant: Sure, both were on the table. If it had come in with high confidence and no caveats, I probably would have moved faster. If a colleague hadn't raised the registry-link point, I might have just taken it at face value. Setting it aside completely felt like it would slow us down without much benefit, since the report was self-aware about its own gap. Interviewer: What did the second data pull show? Participant: It confirmed the registry link, actually. Compliance counsel later said treating it as partial rather than definitive was the right call, though I don't think that outcome alone tells you the initial judgment was necessarily correct — it could've gone the other way too. Interviewer: Let's talk about the correspondent bank. What was that situation? Participant: We'd requested SWIFT records and hadn't heard back. This particular correspondent's turnaround history is all over the place — I've seen requests take anywhere from five to fourteen business days, no real pattern to it. We were six days out from the filing deadline, and the liaison had just logged it as 'standard priority,' no timeline attached either way. Interviewer: What did you decide to do while you waited? Participant: Kept building the file and wrote up a contingency note — basically, what we'd file if the records didn't show up in time. Given how mixed the history was on turnaround, I didn't feel like I had grounds to assume either a fast or slow outcome, so I planned for both. Interviewer: What actually happened? Participant: Partial records came back on day six. Enough to inform the file, not enough to close every gap. My team lead noted we'd at least had the contingency plan ready, which helped. Interviewer: Last stretch — the time estimate for remaining work. Participant: Reconciling two invoice sets, drafting the narrative, compliance sign-off. Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week. Interviewer: What made you lean toward the lower end rather than the middle or upper end of that range? Participant: The task list itself looked manageable, and I didn't have anything else competing hard for my time. I did flag internally that if a reconciliation issue came up, that number could slip. Interviewer: How did it actually play out? Participant: Pretty close. One clarifying question came up during reconciliation that cost half a day, and sign-off took about as long as I'd have expected given the case's complexity. Nothing dramatic. Interviewer: Looking back across all four points, what were you least sure about at the time? Participant: Probably the correspondent bank timing — that one genuinely could have gone either way, and I don't think there was a way to know in advance. The vendor report's registry link was a close second. Interviewer: A few hypotheticals. If the shipping agent's delay had turned out to be substantive rather than administrative, what would you have done? Participant: I'd have reshuffled priorities immediately and probably pulled in a second analyst. Interviewer: If the vendor's report had come in high-confidence instead of moderate? Participant: I likely would have moved to drafting the escalation sooner rather than waiting on the second pull. Interviewer: If you'd known the records would land on day six rather than later? Participant: Honestly, not much would've changed — the contingency plan already assumed something like that. Interviewer: And if a colleague had reviewed your time estimate beforehand? Participant: They might have pushed me toward the midpoint just to be safe, but I think they'd have accepted four days as reasonable given the task list. Interviewer: That's really helpful, thank you.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.26s · gen 81.00s · total 85.8s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0276 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0243 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0236 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0235 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0234 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0233 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
7. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0232 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
9. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0202 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0202 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0188 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
12. **Hallihan_etal_DTM_12.pdf** — 0.0186 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
13. **Hallihan_etal_DTM_12.pdf** — 0.0184 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0182 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0181 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
17. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0178 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
18. **ijcma-08-2012-0064.pdf** — 0.0173 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0171 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0170 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0163 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0163 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
23. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
26. **ijcma-08-2012-0064.pdf** — 0.0155 (rrf) — _# 382 descriptive approach. In fact, every study analyzed just one bias, only a few studies Refe_
27. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0151 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
29. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
30. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0148 (rrf) — _assume the role of an interviewer evaluating an interviewee or a potential and cues as possible _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **ijcma-08-2012-0064.pdf** — 0.0147 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
34. **ijcma-08-2012-0064.pdf** — 0.0146 (rrf) — _# 382 on heuristics and results in more biased judgments (Bazerman and Moore, 2009). Gladwin and_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 3. Methodology Each test produces a hypothesis in this study a considered to be good evidence _
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0146 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
38. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0145 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 8. References Rand, J.W. (2002) ‘Understandng Why Good Lawyers Go Bad: Using Case Studies in C_
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
42. **ijcma-08-2012-0064.pdf** — 0.0141 (rrf) — _# 382 analyzed the sources of framing influences on negotiator behavior (Neale the impact of fra_
43. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0141 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
46. **ijcma-08-2012-0064.pdf** — 0.0140 (rrf) — _# 378 et al. , 1994), Downloaded from http://www.emerald.com/ijcma/articlepdf/24/4/374/817133/ij_
47. **Hallihan_etal_DTM_12.pdf** — 0.0139 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
48. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0139 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The interview was reviewed for affirmative, mechanism-grounded evidence of cognitive bias in the participant's case reasoning. Several reasoning episodes were considered, but each was accompanied by explicit calibration, alternative consideration, documented rationale, or debiasing checks. No occurrence met the threshold for positive identification; three plausible candidate patterns are recorded separately."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring and adjustment",
      "alternative_labels": ["anchoring bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Prioritization of batch alerts",
      "supporting_interview_quote": "I prioritized Halcyon first, since the invoice gap was the clearest indicator I had to work with, and documented a plan to get through the other three that same week. I didn't ignore them — I just sequenced based on which indicator looked most substantive on its face.",
      "plausible_mechanism": "The participant may have anchored to the most salient initial indicator, the invoice value gap, and allocated attention disproportionately, potentially underweighting transaction size or other alert features.",
      "why_not_identified": "The participant explicitly considered alternative prioritization criteria, documented the rationale, and the team lead found it reasonable; there is no affirmative evidence of inadequate adjustment or distorted risk judgment."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "confirmation bias",
      "alternative_labels": ["confirmatory bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Weighting of OSINT vendor report",
      "supporting_interview_quote": "If a colleague hadn't raised the registry-link point, I might have just taken it at face value.",
      "plausible_mechanism": "A report consistent with a known layering pattern could have been treated as positive confirmation of initial suspicion without independent verification, a classic confirmation-bias pathway.",
      "why_not_identified": "The quote is counterfactual about what might have happened; in the actual episode, the participant treated the moderate-confidence report as partial corroboration and sought a second data pull, which is inconsistent with an affirmative confirmation-bias occurrence."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "planning fallacy",
      "alternative_labels": ["optimism bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Remaining-work time estimate",
      "supporting_interview_quote": "Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week.",
      "plausible_mechanism": "Selecting the lower bound of a historical range could reflect an inside-view or optimistic task-completion estimate.",
      "why_not_identified": "The participant explicitly used the historical distribution, grounded the estimate in task-specific analysis, flagged possible slippage, and the actual outcome was close; this is better explained as calibrated estimation under uncertainty than as planning fallacy."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "Single retrospective interview; self-reported reasoning may omit or rationalize cognitive processes.",
    "Retrieved corpus passages were present but no identified occurrence required corpus support; therefore retrieved_corpus_support_used is false.",
    "The analysis is conservative and does not infer bias from hypothetical or counterfactual statements, appropriate heuristics, or ordinary uncertainty."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is being recorded for internal case-review purposes only, and you can skip anything you'd rather not go into. Can you start by telling me your role and background? Participant: Sure. I'm a financial crime intelligence analyst on the FIU team, been in this specific role about six years, mostly trade finance and sanctions typologies before that. Interviewer: I want to walk through a specific case — the Halcyon Freight matter. Can you tell me how it came to your attention and what you were trying to achieve? Participant: It came in as part of a batch alert — four counterparties flagged together. Halcyon Freight Partners was one of them, along with a commodities trader, a small logistics subcontractor, and a shipping agent. My objective was the usual one: figure out whether there was enough here to warrant an escalation to compliance and possibly law enforcement, and do it within the ten-day filing window. Interviewer: What did the batch actually show you? Participant: Halcyon had one indicator that stood out — an invoice value gap, meaning the declared value didn't match what we'd expect for the goods described. No beneficial-ownership overlap with anything I'd seen before, so it wasn't ringing any specific bells. The commodities trader had a minor documentation gap, but nothing typologically interesting. It was a fairly normal week workload-wise, nothing especially heavy. Interviewer: Walk me through what you did once you had that picture. Participant: I prioritized Halcyon first, since the invoice gap was the clearest indicator I had to work with, and documented a plan to get through the other three that same week. I didn't ignore them — I just sequenced based on which indicator looked most substantive on its face. Interviewer: What made you order it that way rather than, say, splitting time evenly or going by transaction size? Participant: Honestly, either of those would have been defensible too. I went with indicator strength because that's usually a decent proxy for where the real risk sits, but I'll admit transaction size might have surfaced something different. I made a note of the reasoning in case anyone asked. Interviewer: Did anyone ask? Participant: Yeah, my team lead did, later. Wanted to know why I'd sequenced it that way. I walked her through the invoice-gap rationale and she was fine with it — it wasn't the only reasonable choice, but it wasn't unreasonable either. Interviewer: What came out of the other three once you got to them? Participant: The shipping agent turned out to have an administrative filing delay — paperwork lag, not a risk issue at all. Nothing on the logistics subcontractor either. So the sequencing didn't really cost us anything in the end, though I can't say for certain it wouldn't have mattered in a different case. Interviewer: Let's move to the vendor report. What happened there? Participant: A few days in, our OSINT vendor sent a report saying Halcyon's ownership structure was 'plausibly consistent' with a known layering pattern. Importantly, they flagged it as moderate confidence themselves and noted one registry link hadn't been independently verified yet. Interviewer: How did you decide how much weight to give that? Participant: A colleague suggested we get a second data pull to firm up that specific link before leaning on the report too heavily. I thought that was reasonable, so I treated the report as partial corroboration — enough to keep building the file, not enough to treat as settled — while the second pull was requested in parallel. Interviewer: Was there a version of this where you'd have leaned harder on the report, or set it aside entirely? Participant: Sure, both were on the table. If it had come in with high confidence and no caveats, I probably would have moved faster. If a colleague hadn't raised the registry-link point, I might have just taken it at face value. Setting it aside completely felt like it would slow us down without much benefit, since the report was self-aware about its own gap. Interviewer: What did the second data pull show? Participant: It confirmed the registry link, actually. Compliance counsel later said treating it as partial rather than definitive was the right call, though I don't think that outcome alone tells you the initial judgment was necessarily correct — it could've gone the other way too. Interviewer: Let's talk about the correspondent bank. What was that situation? Participant: We'd requested SWIFT records and hadn't heard back. This particular correspondent's turnaround history is all over the place — I've seen requests take anywhere from five to fourteen business days, no real pattern to it. We were six days out from the filing deadline, and the liaison had just logged it as 'standard priority,' no timeline attached either way. Interviewer: What did you decide to do while you waited? Participant: Kept building the file and wrote up a contingency note — basically, what we'd file if the records didn't show up in time. Given how mixed the history was on turnaround, I didn't feel like I had grounds to assume either a fast or slow outcome, so I planned for both. Interviewer: What actually happened? Participant: Partial records came back on day six. Enough to inform the file, not enough to close every gap. My team lead noted we'd at least had the contingency plan ready, which helped. Interviewer: Last stretch — the time estimate for remaining work. Participant: Reconciling two invoice sets, drafting the narrative, compliance sign-off. Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week. Interviewer: What made you lean toward the lower end rather than the middle or upper end of that range? Participant: The task list itself looked manageable, and I didn't have anything else competing hard for my time. I did flag internally that if a reconciliation issue came up, that number could slip. Interviewer: How did it actually play out? Participant: Pretty close. One clarifying question came up during reconciliation that cost half a day, and sign-off took about as long as I'd have expected given the case's complexity. Nothing dramatic. Interviewer: Looking back across all four points, what were you least sure about at the time? Participant: Probably the correspondent bank timing — that one genuinely could have gone either way, and I don't think there was a way to know in advance. The vendor report's registry link was a close second. Interviewer: A few hypotheticals. If the shipping agent's delay had turned out to be substantive rather than administrative, what would you have done? Participant: I'd have reshuffled priorities immediately and probably pulled in a second analyst. Interviewer: If the vendor's report had come in high-confidence instead of moderate? Participant: I likely would have moved to drafting the escalation sooner rather than waiting on the second pull. Interviewer: If you'd known the records would land on day six rather than later? Participant: Honestly, not much would've changed — the contingency plan already assumed something like that. Interviewer: And if a colleague had reviewed your time estimate beforehand? Participant: They might have pushed me toward the midpoint just to be safe, but I think they'd have accepted four days as reasonable given the task list. Interviewer: That's really helpful, thank you.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.19s · gen 205.36s · total 209.9s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0276 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0243 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0236 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0235 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0234 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0233 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
7. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0232 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
9. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0202 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0202 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0188 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
12. **Hallihan_etal_DTM_12.pdf** — 0.0186 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
13. **Hallihan_etal_DTM_12.pdf** — 0.0184 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0182 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0181 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
17. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0178 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
18. **ijcma-08-2012-0064.pdf** — 0.0173 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0171 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0170 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0163 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0163 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
23. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
26. **ijcma-08-2012-0064.pdf** — 0.0155 (rrf) — _# 382 descriptive approach. In fact, every study analyzed just one bias, only a few studies Refe_
27. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0151 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
29. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
30. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0148 (rrf) — _assume the role of an interviewer evaluating an interviewee or a potential and cues as possible _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **ijcma-08-2012-0064.pdf** — 0.0147 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
34. **ijcma-08-2012-0064.pdf** — 0.0146 (rrf) — _# 382 on heuristics and results in more biased judgments (Bazerman and Moore, 2009). Gladwin and_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 3. Methodology Each test produces a hypothesis in this study a considered to be good evidence _
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0146 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
38. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0145 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 8. References Rand, J.W. (2002) ‘Understandng Why Good Lawyers Go Bad: Using Case Studies in C_
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
42. **ijcma-08-2012-0064.pdf** — 0.0141 (rrf) — _# 382 analyzed the sources of framing influences on negotiator behavior (Neale the impact of fra_
43. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0141 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
46. **ijcma-08-2012-0064.pdf** — 0.0140 (rrf) — _# 378 et al. , 1994), Downloaded from http://www.emerald.com/ijcma/articlepdf/24/4/374/817133/ij_
47. **Hallihan_etal_DTM_12.pdf** — 0.0139 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
48. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0139 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Single-interview analysis of the participant's reasoning about case prioritization, vendor-report weighting, correspondent-bank uncertainty, and time estimation. Retrieved corpus provided material on anchoring, confirmation bias, AI/support-system overreliance, and aviation biases, but no passage directly addressed time-estimation/planning-fallacy mechanisms."
  },
  "identified_bias_summary": [
    {
      "bias_label": "Planning fallacy",
      "identified_occurrence_count": 1
    }
  ],
  "identified_occurrences": [
    {
      "occurrence_id": "obs_001",
      "classification_status": "identified",
      "confidence": "low",
      "bias_label": "Planning fallacy",
      "alternative_labels": ["Optimism bias"],
      "taxonomy_status": "established_label",
      "bias_definition": "The tendency to underestimate the time required to complete a future task, even when similar tasks have taken longer historically, often by focusing on case-specific plans rather than distributional base-rate information.",
      "attributed_to_speaker": "Participant",
      "evidence_speaker": "Participant",
      "decision_episode_label": "Estimating time needed for remaining casework",
      "decision_point_description": "Choosing a four-day estimate near the lower end of a four-to-eight-day historical range for reconciling invoice sets, drafting the narrative, and obtaining compliance sign-off.",
      "affected_reasoning_operation": "Time forecasting / task-completion estimation",
      "bias_specific_mechanism": "Inside-view forecasting: the participant explicitly acknowledges a wide historical range of four to eight days but selects the lower bound based on case-specific features, such as a manageable task list and no competing critical cases, rather than using the historical distribution and potential unknown complications as the primary basis.",
      "manifestation_in_interview": "When asked why he leaned toward the lower end, the participant cited the specific task list and low competing workload rather than giving a distributional reason for departing from the midpoint or upper end of the comparable-case range.",
      "effect_on_reasoning_or_decision": "It produced a low-end schedule estimate, potentially increasing the chance that an unexpected reconciliation issue or sign-off delay could cause the plan to slip.",
      "interview_evidence": [
        {
          "speaker": "Participant",
          "verbatim_quote": "Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week.",
          "evidence_explanation": "The statement shows the participant had explicit historical distribution information but relied on case-specific, inside-view factors to select the lower bound rather than treating the historical range as the primary basis."
        },
        {
          "speaker": "Participant",
          "verbatim_quote": "The task list itself looked manageable, and I didn't have anything else competing hard for my time.",
          "evidence_explanation": "This is a typical inside-view rationale: forecasting future time from current task manageability and low workload rather than from the historical range of comparable cases."
        }
      ],
      "correction_or_counterevidence": "The participant qualified the estimate by flagging that a reconciliation issue could make it slip, and the actual outcome was close with only a half-day clarifying question. A reviewer might also have accepted four days as reasonable; these factors reduce confidence.",
      "retrieved_corpus_support_available": false,
      "corpus_support_note": "The planning-fallacy label comes from general cognitive-science knowledge. The retrieved corpus passages did not directly address time-estimation or planning-fallacy mechanisms, so no retrieved corpus evidence is cited.",
      "corpus_evidence": []
    }
  ],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Confirmation bias",
      "alternative_labels": ["Biased assimilation"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Interpreting the vendor report on Halcyon's ownership structure",
      "supporting_interview_quote": "I treated the report as partial corroboration — enough to keep building the file, not enough to treat as settled — while the second pull was requested in parallel... If a colleague hadn't raised the registry-link point, I might have just taken it at face value.",
      "plausible_mechanism": "The participant could have given disproportionate corroborative weight to a moderate-confidence report consistent with the initial Halcyon risk hypothesis, especially if the registry-link caveat had not been flagged by a colleague.",
      "why_not_identified": "The actual reported reasoning was calibrated rather than clearly biased: he acknowledged the moderate-confidence caveat, treated the report as provisional rather than settled, and requested a second data pull. The strongest evidence for biased acceptance is counterfactual/hypothetical, not an actual biased decision."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring",
      "alternative_labels": ["Anchoring and adjustment"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Prioritizing the four counterparties from the batch alert",
      "supporting_interview_quote": "I prioritized Halcyon first, since the invoice gap was the clearest indicator I had to work with... I went with indicator strength because that's usually a decent proxy for where the real risk sits, but I'll admit transaction size might have surfaced something different.",
      "plausible_mechanism": "The prominent invoice-value-gap indicator could have served as an initial anchor, concentrating attention on Halcyon and influencing later sequencing and corroboration-seeking without explicit consideration of alternative risk-ordering bases.",
      "why_not_identified": "The participant gave a plausible risk-prioritization rationale, documented the reasoning, considered alternatives, and the team lead found the choice defensible. There is insufficient evidence of insufficient adjustment or distorted judgment from an anchor."
    }
  ],
  "no_supported_biases_found": false,
  "limitations": [
    "The retrieved corpus lacked a directly applicable passage on planning fallacy or time-estimation bias, so the identified label relies on established general knowledge rather than retrieved scientific support.",
    "The analysis is based on self-reported retrospective interview responses, which may be affected by memory error or self-presentation.",
    "No experimental benchmark or ground-truth decision outcome is available to validate the identified bias.",
    "Several possible bias mechanisms were present only as hypotheticals or were mitigated by safeguards, so they are treated as candidates rather than identified occurrences."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for taking the time. This is being recorded for internal case-review purposes only, and you can skip anything you'd rather not go into. Can you start by telling me your role and background? Participant: Sure. I'm a financial crime intelligence analyst on the FIU team, been in this specific role about six years, mostly trade finance and sanctions typologies before that. Interviewer: I want to walk through a specific case — the Halcyon Freight matter. Can you tell me how it came to your attention and what you were trying to achieve? Participant: It came in as part of a batch alert — four counterparties flagged together. Halcyon Freight Partners was one of them, along with a commodities trader, a small logistics subcontractor, and a shipping agent. My objective was the usual one: figure out whether there was enough here to warrant an escalation to compliance and possibly law enforcement, and do it within the ten-day filing window. Interviewer: What did the batch actually show you? Participant: Halcyon had one indicator that stood out — an invoice value gap, meaning the declared value didn't match what we'd expect for the goods described. No beneficial-ownership overlap with anything I'd seen before, so it wasn't ringing any specific bells. The commodities trader had a minor documentation gap, but nothing typologically interesting. It was a fairly normal week workload-wise, nothing especially heavy. Interviewer: Walk me through what you did once you had that picture. Participant: I prioritized Halcyon first, since the invoice gap was the clearest indicator I had to work with, and documented a plan to get through the other three that same week. I didn't ignore them — I just sequenced based on which indicator looked most substantive on its face. Interviewer: What made you order it that way rather than, say, splitting time evenly or going by transaction size? Participant: Honestly, either of those would have been defensible too. I went with indicator strength because that's usually a decent proxy for where the real risk sits, but I'll admit transaction size might have surfaced something different. I made a note of the reasoning in case anyone asked. Interviewer: Did anyone ask? Participant: Yeah, my team lead did, later. Wanted to know why I'd sequenced it that way. I walked her through the invoice-gap rationale and she was fine with it — it wasn't the only reasonable choice, but it wasn't unreasonable either. Interviewer: What came out of the other three once you got to them? Participant: The shipping agent turned out to have an administrative filing delay — paperwork lag, not a risk issue at all. Nothing on the logistics subcontractor either. So the sequencing didn't really cost us anything in the end, though I can't say for certain it wouldn't have mattered in a different case. Interviewer: Let's move to the vendor report. What happened there? Participant: A few days in, our OSINT vendor sent a report saying Halcyon's ownership structure was 'plausibly consistent' with a known layering pattern. Importantly, they flagged it as moderate confidence themselves and noted one registry link hadn't been independently verified yet. Interviewer: How did you decide how much weight to give that? Participant: A colleague suggested we get a second data pull to firm up that specific link before leaning on the report too heavily. I thought that was reasonable, so I treated the report as partial corroboration — enough to keep building the file, not enough to treat as settled — while the second pull was requested in parallel. Interviewer: Was there a version of this where you'd have leaned harder on the report, or set it aside entirely? Participant: Sure, both were on the table. If it had come in with high confidence and no caveats, I probably would have moved faster. If a colleague hadn't raised the registry-link point, I might have just taken it at face value. Setting it aside completely felt like it would slow us down without much benefit, since the report was self-aware about its own gap. Interviewer: What did the second data pull show? Participant: It confirmed the registry link, actually. Compliance counsel later said treating it as partial rather than definitive was the right call, though I don't think that outcome alone tells you the initial judgment was necessarily correct — it could've gone the other way too. Interviewer: Let's talk about the correspondent bank. What was that situation? Participant: We'd requested SWIFT records and hadn't heard back. This particular correspondent's turnaround history is all over the place — I've seen requests take anywhere from five to fourteen business days, no real pattern to it. We were six days out from the filing deadline, and the liaison had just logged it as 'standard priority,' no timeline attached either way. Interviewer: What did you decide to do while you waited? Participant: Kept building the file and wrote up a contingency note — basically, what we'd file if the records didn't show up in time. Given how mixed the history was on turnaround, I didn't feel like I had grounds to assume either a fast or slow outcome, so I planned for both. Interviewer: What actually happened? Participant: Partial records came back on day six. Enough to inform the file, not enough to close every gap. My team lead noted we'd at least had the contingency plan ready, which helped. Interviewer: Last stretch — the time estimate for remaining work. Participant: Reconciling two invoice sets, drafting the narrative, compliance sign-off. Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week. Interviewer: What made you lean toward the lower end rather than the middle or upper end of that range? Participant: The task list itself looked manageable, and I didn't have anything else competing hard for my time. I did flag internally that if a reconciliation issue came up, that number could slip. Interviewer: How did it actually play out? Participant: Pretty close. One clarifying question came up during reconciliation that cost half a day, and sign-off took about as long as I'd have expected given the case's complexity. Nothing dramatic. Interviewer: Looking back across all four points, what were you least sure about at the time? Participant: Probably the correspondent bank timing — that one genuinely could have gone either way, and I don't think there was a way to know in advance. The vendor report's registry link was a close second. Interviewer: A few hypotheticals. If the shipping agent's delay had turned out to be substantive rather than administrative, what would you have done? Participant: I'd have reshuffled priorities immediately and probably pulled in a second analyst. Interviewer: If the vendor's report had come in high-confidence instead of moderate? Participant: I likely would have moved to drafting the escalation sooner rather than waiting on the second pull. Interviewer: If you'd known the records would land on day six rather than later? Participant: Honestly, not much would've changed — the contingency plan already assumed something like that. Interviewer: And if a colleague had reviewed your time estimate beforehand? Participant: They might have pushed me toward the midpoint just to be safe, but I think they'd have accepted four days as reasonable given the task list. Interviewer: That's really helpful, thank you.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.08s · gen 80.07s · total 84.3s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0276 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0243 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0236 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
4. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0235 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
5. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0234 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
6. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0233 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
7. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0232 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0203 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
9. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0202 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
10. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0202 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0188 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_
12. **Hallihan_etal_DTM_12.pdf** — 0.0186 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
13. **Hallihan_etal_DTM_12.pdf** — 0.0184 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
14. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0184 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
15. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0182 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
16. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0181 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
17. **qt4gm120pg_noSplash_4550b57d9ad2cd7daa100f254373abc0.pdf** — 0.0178 (rrf) — _# Appendices in the article. - based task. S olor traces which are purely red and once we are as_
18. **ijcma-08-2012-0064.pdf** — 0.0173 (rrf) — _# 382 though negotiators were presented with identical, unbiased information about a dispute, th_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0171 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0170 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0163 (rrf) — _# 5. Discussion The biggest strength, but possibly also the biggest challenge to this study was _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0163 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
23. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0159 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0157 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0156 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
26. **ijcma-08-2012-0064.pdf** — 0.0155 (rrf) — _# 382 descriptive approach. In fact, every study analyzed just one bias, only a few studies Refe_
27. **Goh et al. (2025) Physician clinical decision modification and bias assessment in a randomized controlled trial of AI assistance.pdf** — 0.0151 (rrf) — _# fi cation ecisionquestions,basedonevidencehttps://doi.org/10.1038/s43856-025-00781-2 sentation_
28. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0151 (rrf) — _### I movi around you is movement: waves of breeze through the tall grass, branches, and leaves _
29. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0150 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
30. **Mitigating Bias and Improving Professional Decision-Making through Persuasive Training Games_26_01_25_23_55_15.pdf** — 0.0148 (rrf) — _assume the role of an interviewer evaluating an interviewee or a potential and cues as possible _
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0148 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **ijcma-08-2012-0064.pdf** — 0.0147 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
34. **ijcma-08-2012-0064.pdf** — 0.0146 (rrf) — _# 382 on heuristics and results in more biased judgments (Bazerman and Moore, 2009). Gladwin and_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0146 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
36. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 3. Methodology Each test produces a hypothesis in this study a considered to be good evidence _
37. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0146 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
38. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0145 (rrf) — _# arXiv:2010.07938v2 \[cs.HC\] 4 Apr 2022 agreement with the AI prediction. Thus, by measuring t_
39. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0144 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
40. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 8. References Rand, J.W. (2002) ‘Understandng Why Good Lawyers Go Bad: Using Case Studies in C_
41. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
42. **ijcma-08-2012-0064.pdf** — 0.0141 (rrf) — _# 382 analyzed the sources of framing influences on negotiator behavior (Neale the impact of fra_
43. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0141 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
44. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0140 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
45. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0140 (rrf) — _# Results d along with the results. occur during incidents and accidents? in the reports. ssocia_
46. **ijcma-08-2012-0064.pdf** — 0.0140 (rrf) — _# 378 et al. , 1994), Downloaded from http://www.emerald.com/ijcma/articlepdf/24/4/374/817133/ij_
47. **Hallihan_etal_DTM_12.pdf** — 0.0139 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
48. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0139 (rrf) — _# Page 3 The background color of the interface transitioned from red to green, from left to righ_
49. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0137 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
50. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0135 (rrf) — _## Neurocognitive Designed for Social Exchange LEDA COSMIDES and JOHN TOOBY y of this to you. Wh_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Mechanism-first review of the participant's reported reasoning across batch prioritization, vendor report weighting, correspondent-bank planning, and remaining-time estimation. No bias-specific mechanism met the affirmative-evidence standard."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Planning fallacy",
      "alternative_labels": ["Optimism bias", "Overconfidence effect"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Estimating remaining work duration for Halcyon case",
      "supporting_interview_quote": "Comparable cases have run anywhere from four to eight days historically — a pretty wide band. I landed on four days, near the lower end, based on the specific tasks left and the fact that neither of my other two cases was at a critical point that week.",
      "plausible_mechanism": "A prediction at the lower bound of a historical range could reflect an inside-view/optimistic planning pattern in which task-specific manageability is weighted over base-rate distributional information.",
      "why_not_identified": "The transcript does not affirmatively show neglect of historical base rates or motivated optimism; the participant cited task-specific factors, flagged that a reconciliation issue could extend the estimate, and the actual outcome was consistent with the estimate."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "Retrospective self-report; cognitive mechanisms are inferred from spoken reasoning rather than direct observation.",
    "No identified occurrences met the conservative mechanism-first evidentiary standard, so retrieved corpus support was not used.",
    "Hypothetical interviewer prompts were considered but not classified as bias occurrences."
  ]
}

