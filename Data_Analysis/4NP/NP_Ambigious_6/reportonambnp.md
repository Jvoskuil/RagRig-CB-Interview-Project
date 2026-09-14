# RAG Benchmark — 2026-09-12

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is a routine cognitive task analysis interview — I want to understand how you actually worked through the feedwater heater trend during the ascension test, not evaluate your performance. It'll be de-identified for training and procedure review. Okay with you? Participant: Sure, no problem. Interviewer: Let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend? Participant: We were about three hours into the ascension test, sitting around 90 percent power, working toward a dispatch commitment at end of shift. I was doing my normal rounds on the trend recorders and caught that heater 1B outlet temperature had come up about three degrees over maybe twenty minutes. Train 1A was steady, no alarm, nothing outside our Tech Spec limit. My first thought was that it looked like the calibration deviation we'd had on that sensor last cycle — but I didn't want to just assume that, because I didn't actually remember the details of that event well enough to say it matched. Interviewer: What was going through your head in terms of goals and pressures? Participant: Getting to a hundred percent within the dispatch window, with about two hours of slack at that point. I wasn't rushed, but I was aware of the clock. At the same time, I didn't want to just label the drift and move on without checking whether it actually fit. Interviewer: Let's reconstruct the timeline before we get into the decisions. What happened after you noticed the drift? Participant: I pulled the closed-out fault report from last cycle to compare against what I was seeing. About fifteen minutes later the trend was still creeping, still shallow. Then, maybe forty minutes in total, a maintenance tech on an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. I asked him to take a second reading. Shortly after that the trend recorder started flattening as we came up on the final ascension step. Interviewer: Okay, let's go through this decision by decision. First: when you noticed the drift, what alternatives did you actually weigh? Participant: Either treat it as the same calibration issue from last cycle, or treat it as an open question and get an independent check before assuming anything. I ended up somewhere in between — I pulled up the old fault log to see how closely the pattern matched. Interviewer: What did that comparison tell you? Participant: Honestly, it was partial. The timing and the size of the rise were similar. But the rate of onset — how fast it ramped at the very start — wasn't something the old log tracked consistently, so I couldn't really say whether that piece matched or not. I logged it as a probable but unconfirmed recurrence, which felt like the most honest way to write it up given what I had. Interviewer: Did that ambiguity bother you? Participant: A little. I would've liked a cleaner match one way or the other. But I didn't think it was worth pulling I&C off other work for a value that was still well inside limits. Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available to brief the STA before continuing. What went into that call? Participant: That one I thought about for a bit. The STA was right there. Part of me thought, with the comparison being inconclusive, maybe I should just brief him now and let him weigh in. But I also didn't have much to brief him with yet — just an unconfirmed resemblance to an old fault. So I decided to keep trending for a defined stretch, I think I gave it another fifteen minutes in my head, with the idea that either the data would firm up enough to justify a briefing, or it would settle down and not need one. Interviewer: Was the schedule part of that? Participant: A bit, sure. But it wasn't the deciding factor — I genuinely thought waiting a short, bounded amount of time would give me better information either way. Interviewer: Right after that, the technician's infrared call came in. How did you weigh that against the trend recorder? Participant: That's the one where I felt most uncertain. His reading suggested localized heating, which could point to fouling, but it could also just be a warm spot from wherever that drifted sensor sits — I honestly wasn't sure which. The trend recorder showed a smooth rise, which didn't obviously rule either explanation in or out. Rather than pick one, I asked him to take a second reading and tell me what the scan conditions were, since I wanted something to compare against rather than deciding off one data point. Interviewer: What came back? Participant: A similar but not identical reading. He mentioned the scan angle and surface conditions weren't perfectly controlled either time, so even the comparison didn't fully resolve it. At that point I had two data sources that each pointed somewhere, but neither one closed the question. Interviewer: How did you feel about leaving it open like that? Participant: A little uneasy, if I'm honest. Usually you want a cleaner answer before you keep moving. But nothing in front of me demanded an immediate call, so I didn't force one. Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed? Participant: The flattening helped, but I didn't treat it as proof the earlier question was settled. I still had that inconclusive infrared comparison sitting unresolved. What I did was log it as an open item — wrote it up for the oncoming shift and put in a request for maintenance to follow up — and then proceeded with the step, since there wasn't a procedural or Tech Spec basis to hold at that point. Interviewer: Did you consider holding anyway, just to close out the comparison first? Participant: I did think about it. It came down to whether an unconfirmed field reading, with no limit approached, was enough reason to interrupt a scheduled step. I decided documenting it and handing it off was the more defensible path, but I won't pretend that was the only reasonable call. Interviewer: What single piece of information would have changed that decision? Participant: If the repeat scan had come back clean and consistent — clearly showing localized heating with good scan conditions both times — I think I would've held and gotten the STA involved before the final step. Interviewer: And if the trend had kept climbing instead of flattening? Participant: Then the flattening wouldn't have been there to lean on, and I think the open item alone would've been enough to justify a hold. Interviewer: Looking back, is there a point where you wish you'd had better information, even if the decision felt reasonable at the time? Participant: The infrared piece, definitely. I'd have liked a way to get a controlled comparison reading rather than two scans taken under different conditions. That's really where most of my uncertainty sat the whole time. Interviewer: One last thing for the record, unrelated to how you reasoned through it at the time — a maintenance work order filed after your shift ended found early-stage fouling on the 1B heater, separate from the old calibration issue. That wasn't information you had available during the ascension, so I'm just noting it for the file. Participant: Understood — that's good to have documented either way. Interviewer: That's really helpful, thank you.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 2.94s · gen 42.63s · total 47.9s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0306 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0270 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0267 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0262 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0261 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
7. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0227 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0221 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
9. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0219 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
10. **Hallihan_etal_DTM_12.pdf** — 0.0218 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0211 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
14. **Hallihan_etal_DTM_12.pdf** — 0.0184 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
15. **Lyell Automation bias and verification complexity.pdf** — 0.0183 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0176 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
18. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0174 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0174 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0167 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
23. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0164 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0160 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
29. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0158 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
38. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0147 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
40. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
45. **cognitive-and-human-factors-in-expert-decision-making-six-fallacies-and-the-eight-sources-of-bias.pdf** — 0.0140 (rrf) — _### ACCESS | | 46 | causes an expectation to what the results should be. | | we actually perceiv_
46. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0139 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
49. **Lyell Automation bias and verification complexity.pdf** — 0.0138 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The transcript was analyzed as the sole factual authority for cognitive bias occurrences. Retrieved scientific passages were reviewed for terminology and mechanism support, but no interviewed reasoning episode met the threshold for an affirmative bias identification."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory hypothesis testing",
        "Positive test strategy"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Comparison of 1B heater outlet temperature drift to prior calibration-deviation fault log",
      "supporting_interview_quote": "I pulled the closed-out fault report from last cycle to compare against what I was seeing. About fifteen minutes later the trend was still creeping, still shallow. Then, maybe forty minutes in total, a maintenance tech on an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner.",
      "plausible_mechanism": "An initial calibration-deviation hypothesis may have focused information search on a matching prior fault log rather than an independent diagnostic path, consistent with confirmatory hypothesis testing.",
      "why_not_identified": "The participant explicitly considered an independent check, acknowledged the comparison was only partial, and did not ignore disconfirming or ambiguous information; the transcript lacks affirmative evidence that confirmatory search distorted a judgment or decision."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Get-there-itis",
        "Plan continuation error"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to proceed with final ascension step despite unresolved 1B heater infrared and temperature anomalies",
      "supporting_interview_quote": "It came down to whether an unconfirmed field reading, with no limit approached, was enough reason to interrupt a scheduled step. I decided documenting it and handing it off was the more defensible path, but I won't pretend that was the only reasonable call.",
      "plausible_mechanism": "The dispatch commitment and scheduled ascent could have biased the participant toward continuing the planned final step despite an unresolved anomalous reading.",
      "why_not_identified": "The participant stated schedule was not the deciding factor, identified no procedural or Tech Spec basis to hold, used bounded monitoring, documented an open item, and considered holding; the transcript does not affirmatively demonstrate that plan continuation distorted the decision."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "The analysis relies solely on the participant's self-reported reasoning and decision process, which may omit or reconstruct cognitive processes.",
    "No independent behavioral, system, or outcome data were available in the transcript to corroborate or contradict the reported reasoning.",
    "Retrieved scientific passages were used only for candidate terminology and mechanism review; no retrieved source provided affirmative support for an identified occurrence.",
    "The interview contains explicit self-monitoring, uncertainty acknowledgment, and bounded information-gathering behavior, which reduced the strength of plausible bias candidates."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is a routine cognitive task analysis interview — I want to understand how you actually worked through the feedwater heater trend during the ascension test, not evaluate your performance. It'll be de-identified for training and procedure review. Okay with you? Participant: Sure, no problem. Interviewer: Let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend? Participant: We were about three hours into the ascension test, sitting around 90 percent power, working toward a dispatch commitment at end of shift. I was doing my normal rounds on the trend recorders and caught that heater 1B outlet temperature had come up about three degrees over maybe twenty minutes. Train 1A was steady, no alarm, nothing outside our Tech Spec limit. My first thought was that it looked like the calibration deviation we'd had on that sensor last cycle — but I didn't want to just assume that, because I didn't actually remember the details of that event well enough to say it matched. Interviewer: What was going through your head in terms of goals and pressures? Participant: Getting to a hundred percent within the dispatch window, with about two hours of slack at that point. I wasn't rushed, but I was aware of the clock. At the same time, I didn't want to just label the drift and move on without checking whether it actually fit. Interviewer: Let's reconstruct the timeline before we get into the decisions. What happened after you noticed the drift? Participant: I pulled the closed-out fault report from last cycle to compare against what I was seeing. About fifteen minutes later the trend was still creeping, still shallow. Then, maybe forty minutes in total, a maintenance tech on an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. I asked him to take a second reading. Shortly after that the trend recorder started flattening as we came up on the final ascension step. Interviewer: Okay, let's go through this decision by decision. First: when you noticed the drift, what alternatives did you actually weigh? Participant: Either treat it as the same calibration issue from last cycle, or treat it as an open question and get an independent check before assuming anything. I ended up somewhere in between — I pulled up the old fault log to see how closely the pattern matched. Interviewer: What did that comparison tell you? Participant: Honestly, it was partial. The timing and the size of the rise were similar. But the rate of onset — how fast it ramped at the very start — wasn't something the old log tracked consistently, so I couldn't really say whether that piece matched or not. I logged it as a probable but unconfirmed recurrence, which felt like the most honest way to write it up given what I had. Interviewer: Did that ambiguity bother you? Participant: A little. I would've liked a cleaner match one way or the other. But I didn't think it was worth pulling I&C off other work for a value that was still well inside limits. Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available to brief the STA before continuing. What went into that call? Participant: That one I thought about for a bit. The STA was right there. Part of me thought, with the comparison being inconclusive, maybe I should just brief him now and let him weigh in. But I also didn't have much to brief him with yet — just an unconfirmed resemblance to an old fault. So I decided to keep trending for a defined stretch, I think I gave it another fifteen minutes in my head, with the idea that either the data would firm up enough to justify a briefing, or it would settle down and not need one. Interviewer: Was the schedule part of that? Participant: A bit, sure. But it wasn't the deciding factor — I genuinely thought waiting a short, bounded amount of time would give me better information either way. Interviewer: Right after that, the technician's infrared call came in. How did you weigh that against the trend recorder? Participant: That's the one where I felt most uncertain. His reading suggested localized heating, which could point to fouling, but it could also just be a warm spot from wherever that drifted sensor sits — I honestly wasn't sure which. The trend recorder showed a smooth rise, which didn't obviously rule either explanation in or out. Rather than pick one, I asked him to take a second reading and tell me what the scan conditions were, since I wanted something to compare against rather than deciding off one data point. Interviewer: What came back? Participant: A similar but not identical reading. He mentioned the scan angle and surface conditions weren't perfectly controlled either time, so even the comparison didn't fully resolve it. At that point I had two data sources that each pointed somewhere, but neither one closed the question. Interviewer: How did you feel about leaving it open like that? Participant: A little uneasy, if I'm honest. Usually you want a cleaner answer before you keep moving. But nothing in front of me demanded an immediate call, so I didn't force one. Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed? Participant: The flattening helped, but I didn't treat it as proof the earlier question was settled. I still had that inconclusive infrared comparison sitting unresolved. What I did was log it as an open item — wrote it up for the oncoming shift and put in a request for maintenance to follow up — and then proceeded with the step, since there wasn't a procedural or Tech Spec basis to hold at that point. Interviewer: Did you consider holding anyway, just to close out the comparison first? Participant: I did think about it. It came down to whether an unconfirmed field reading, with no limit approached, was enough reason to interrupt a scheduled step. I decided documenting it and handing it off was the more defensible path, but I won't pretend that was the only reasonable call. Interviewer: What single piece of information would have changed that decision? Participant: If the repeat scan had come back clean and consistent — clearly showing localized heating with good scan conditions both times — I think I would've held and gotten the STA involved before the final step. Interviewer: And if the trend had kept climbing instead of flattening? Participant: Then the flattening wouldn't have been there to lean on, and I think the open item alone would've been enough to justify a hold. Interviewer: Looking back, is there a point where you wish you'd had better information, even if the decision felt reasonable at the time? Participant: The infrared piece, definitely. I'd have liked a way to get a controlled comparison reading rather than two scans taken under different conditions. That's really where most of my uncertainty sat the whole time. Interviewer: One last thing for the record, unrelated to how you reasoned through it at the time — a maintenance work order filed after your shift ended found early-stage fouling on the 1B heater, separate from the old calibration issue. That wasn't information you had available during the ascension, so I'm just noting it for the file. Participant: Understood — that's good to have documented either way. Interviewer: That's really helpful, thank you.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.70s · gen 83.24s · total 87.0s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0306 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0270 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0267 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0262 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0261 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
7. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0227 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0221 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
9. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0219 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
10. **Hallihan_etal_DTM_12.pdf** — 0.0218 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0211 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
14. **Hallihan_etal_DTM_12.pdf** — 0.0184 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
15. **Lyell Automation bias and verification complexity.pdf** — 0.0183 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0176 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
18. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0174 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0174 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0167 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
23. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0164 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0160 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
29. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0158 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
38. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0147 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
40. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
45. **cognitive-and-human-factors-in-expert-decision-making-six-fallacies-and-the-eight-sources-of-bias.pdf** — 0.0140 (rrf) — _### ACCESS | | 46 | causes an expectation to what the results should be. | | we actually perceiv_
46. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0139 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
49. **Lyell Automation bias and verification complexity.pdf** — 0.0138 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": [
      "Interviewer",
      "Participant"
    ],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative, mechanism-first screening of a retrospective de-identified interview. No benchmark or experimental condition was inferred; only reasoning processes with affirmative evidence of a bias-specific mechanism were considered."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring bias",
      "alternative_labels": [
        "Anchoring-and-adjustment heuristic"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial interpretation of the heater 1B temperature drift as a possible recurrence of the prior calibration deviation",
      "supporting_interview_quote": "My first thought was that it looked like the calibration deviation we'd had on that sensor last cycle — but I didn't want to just assume that, because I didn't actually remember the details of that event well enough to say it matched.",
      "plausible_mechanism": "The earlier calibration-deviation event may have served as an anchor, shaping the reference point or initial hypothesis for evaluating the current drift.",
      "why_not_identified": "The participant explicitly resisted assuming the prior cause, consulted the old fault log as a comparison, acknowledged missing rate-of-onset data, and considered an open-question alternative. The transcript does not affirmatively show failure to adjust away from the initial anchor."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Confirmation bias",
      "alternative_labels": [
        "Confirmatory hypothesis testing"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Comparing the new heater trend to the old calibration fault report and logging it as a probable recurrence",
      "supporting_interview_quote": "The timing and the size of the rise were similar. But the rate of onset — how fast it ramped at the very start — wasn't something the old log tracked consistently, so I couldn't really say whether that piece matched or not. I logged it as a probable but unconfirmed recurrence, which felt like the most honest way to write it up given what I had.",
      "plausible_mechanism": "Evaluating the current trend mainly for similarity to the initial calibration hypothesis could privilege consistent features over missing or inconsistent features.",
      "why_not_identified": "The participant explicitly recognized the missing comparison data, described the recurrence as unconfirmed, and did not treat the partial match as definitive. There is no affirmative evidence of one-sided search, interpretation, or memory selection."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Plan continuation bias",
      "alternative_labels": [
        "Get-there-itis"
      ],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision to proceed with the final 100 percent step despite an unresolved infrared comparison",
      "supporting_interview_quote": "What I did was log it as an open item — wrote it up for the oncoming shift and put in a request for maintenance to follow up — and then proceeded with the step, since there wasn't a procedural or Tech Spec basis to hold at that point.",
      "plausible_mechanism": "Commitment to the scheduled dispatch window could bias continuation of the planned ascension despite an unresolved ambiguous cue.",
      "why_not_identified": "The participant stated schedule pressure was not the deciding factor, considered holding, documented the open item, and cited the absence of any procedural or Tech Spec basis to hold. The reasoning appears primarily structural rather than evidence of a distinct cognitive mechanism."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "The interview is retrospective and de-identified, so real-time cognitive processes cannot be directly observed.",
    "The later maintenance finding of fouling was not available to the participant during the ascension and was not used as evidence that the participant was biased at the time.",
    "The retrieved corpus contained relevant aviation and bias material, but no passage provided suitable affirmative support for a positive identification in this interview.",
    "The absence of identified bias should not be interpreted as evidence that the participant's decisions were optimal, only that the transcript lacks affirmative evidence of a bias-specific mechanism."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is a routine cognitive task analysis interview — I want to understand how you actually worked through the feedwater heater trend during the ascension test, not evaluate your performance. It'll be de-identified for training and procedure review. Okay with you? Participant: Sure, no problem. Interviewer: Let's start broad. Can you walk me through what you were doing when you first noticed the temperature trend? Participant: We were about three hours into the ascension test, sitting around 90 percent power, working toward a dispatch commitment at end of shift. I was doing my normal rounds on the trend recorders and caught that heater 1B outlet temperature had come up about three degrees over maybe twenty minutes. Train 1A was steady, no alarm, nothing outside our Tech Spec limit. My first thought was that it looked like the calibration deviation we'd had on that sensor last cycle — but I didn't want to just assume that, because I didn't actually remember the details of that event well enough to say it matched. Interviewer: What was going through your head in terms of goals and pressures? Participant: Getting to a hundred percent within the dispatch window, with about two hours of slack at that point. I wasn't rushed, but I was aware of the clock. At the same time, I didn't want to just label the drift and move on without checking whether it actually fit. Interviewer: Let's reconstruct the timeline before we get into the decisions. What happened after you noticed the drift? Participant: I pulled the closed-out fault report from last cycle to compare against what I was seeing. About fifteen minutes later the trend was still creeping, still shallow. Then, maybe forty minutes in total, a maintenance tech on an unrelated walkdown radioed that the 1B heater shell felt warmer than usual on his infrared scanner. I asked him to take a second reading. Shortly after that the trend recorder started flattening as we came up on the final ascension step. Interviewer: Okay, let's go through this decision by decision. First: when you noticed the drift, what alternatives did you actually weigh? Participant: Either treat it as the same calibration issue from last cycle, or treat it as an open question and get an independent check before assuming anything. I ended up somewhere in between — I pulled up the old fault log to see how closely the pattern matched. Interviewer: What did that comparison tell you? Participant: Honestly, it was partial. The timing and the size of the rise were similar. But the rate of onset — how fast it ramped at the very start — wasn't something the old log tracked consistently, so I couldn't really say whether that piece matched or not. I logged it as a probable but unconfirmed recurrence, which felt like the most honest way to write it up given what I had. Interviewer: Did that ambiguity bother you? Participant: A little. I would've liked a cleaner match one way or the other. But I didn't think it was worth pulling I&C off other work for a value that was still well inside limits. Interviewer: Second decision point. The trend kept climbing slightly, and you had a discretionary hold point available to brief the STA before continuing. What went into that call? Participant: That one I thought about for a bit. The STA was right there. Part of me thought, with the comparison being inconclusive, maybe I should just brief him now and let him weigh in. But I also didn't have much to brief him with yet — just an unconfirmed resemblance to an old fault. So I decided to keep trending for a defined stretch, I think I gave it another fifteen minutes in my head, with the idea that either the data would firm up enough to justify a briefing, or it would settle down and not need one. Interviewer: Was the schedule part of that? Participant: A bit, sure. But it wasn't the deciding factor — I genuinely thought waiting a short, bounded amount of time would give me better information either way. Interviewer: Right after that, the technician's infrared call came in. How did you weigh that against the trend recorder? Participant: That's the one where I felt most uncertain. His reading suggested localized heating, which could point to fouling, but it could also just be a warm spot from wherever that drifted sensor sits — I honestly wasn't sure which. The trend recorder showed a smooth rise, which didn't obviously rule either explanation in or out. Rather than pick one, I asked him to take a second reading and tell me what the scan conditions were, since I wanted something to compare against rather than deciding off one data point. Interviewer: What came back? Participant: A similar but not identical reading. He mentioned the scan angle and surface conditions weren't perfectly controlled either time, so even the comparison didn't fully resolve it. At that point I had two data sources that each pointed somewhere, but neither one closed the question. Interviewer: How did you feel about leaving it open like that? Participant: A little uneasy, if I'm honest. Usually you want a cleaner answer before you keep moving. But nothing in front of me demanded an immediate call, so I didn't force one. Interviewer: Last decision point. As you approached the final step to a hundred percent, the trend had started flattening. What led you to proceed? Participant: The flattening helped, but I didn't treat it as proof the earlier question was settled. I still had that inconclusive infrared comparison sitting unresolved. What I did was log it as an open item — wrote it up for the oncoming shift and put in a request for maintenance to follow up — and then proceeded with the step, since there wasn't a procedural or Tech Spec basis to hold at that point. Interviewer: Did you consider holding anyway, just to close out the comparison first? Participant: I did think about it. It came down to whether an unconfirmed field reading, with no limit approached, was enough reason to interrupt a scheduled step. I decided documenting it and handing it off was the more defensible path, but I won't pretend that was the only reasonable call. Interviewer: What single piece of information would have changed that decision? Participant: If the repeat scan had come back clean and consistent — clearly showing localized heating with good scan conditions both times — I think I would've held and gotten the STA involved before the final step. Interviewer: And if the trend had kept climbing instead of flattening? Participant: Then the flattening wouldn't have been there to lean on, and I think the open item alone would've been enough to justify a hold. Interviewer: Looking back, is there a point where you wish you'd had better information, even if the decision felt reasonable at the time? Participant: The infrared piece, definitely. I'd have liked a way to get a controlled comparison reading rather than two scans taken under different conditions. That's really where most of my uncertainty sat the whole time. Interviewer: One last thing for the record, unrelated to how you reasoned through it at the time — a maintenance work order filed after your shift ended found early-stage fouling on the 1B heater, separate from the old calibration issue. That wasn't information you had available during the ascension, so I'm just noting it for the file. Participant: Understood — that's good to have documented either way. Interviewer: That's really helpful, thank you.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.71s · gen 114.66s · total 118.4s_

**Retrieved** (ranked by store ranker):
1. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0306 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
2. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0270 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
3. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0267 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
4. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0262 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
5. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0261 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
6. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0240 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
7. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0227 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
8. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0221 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
9. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0219 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
10. **Hallihan_etal_DTM_12.pdf** — 0.0218 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
11. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0211 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
12. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0191 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0188 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
14. **Hallihan_etal_DTM_12.pdf** — 0.0184 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
15. **Lyell Automation bias and verification complexity.pdf** — 0.0183 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
16. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0181 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
17. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0176 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
18. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0174 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
19. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0174 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
20. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0174 (rrf) — _# 3Results On this point, Rezazade Mehrizi et al. (2023) investigated how AI explainability tool_
21. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0171 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
22. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0167 (rrf) — _# f Space Flight the lander would go into a sleep mode during the Ma night, and wake up periodic_
23. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0164 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
24. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
25. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0160 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0160 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0160 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
28. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
29. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0158 (rrf) — _# Page 4 Our bias metric was the mean rating of evidence from 1 = strongly refutes, through 4 = _
30. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0156 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
31. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0155 (rrf) — _## ion of Morality ELFISHNESS AND M ORALITY un selfish as an individual refraining from fosterin_
32. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _# Foreword xii F OREWORD ins ight which tapped deeper principles to show why something it is, as_
33. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0150 (rrf) — _# 592 G k ids the rule, Of course, teenagers are sometimes irresponsible. You are interested in _
34. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0150 (rrf) — _# Experiment 3 Experiment 3 tried to replicate the bias inheritance eect observed in Experiment _
35. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0149 (rrf) — _# 3. Methodology over control of the bias could not always be collected. However, the reports an_
36. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0149 (rrf) — _## lIs sues in 156 F OUNDATIONS OF odds that the indirect methods of cognitive and social psycho_
37. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0147 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
38. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0147 (rrf) — _# General discussion explicitly present. us, AI biases could have the potential to propagate thr_
39. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0146 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration regarded as compla_
40. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0146 (rrf) — _## Uwe Dulleck, PhD framing bias (for de fi nitions of cognitive biases, see Supplementary Table_
41. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0145 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
42. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0144 (rrf) — _# 5. Discussion Regarding authority gradient, the analysis revealed that not all the reports inv_
43. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0143 (rrf) — _# 2. Literature Review (NTSB, 2018) 2. 4.3 Confirmation bias Confirmation bias is defined people_
44. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0142 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
45. **cognitive-and-human-factors-in-expert-decision-making-six-fallacies-and-the-eight-sources-of-bias.pdf** — 0.0140 (rrf) — _### ACCESS | | 46 | causes an expectation to what the results should be. | | we actually perceiv_
46. **Human expert performance in forensic decision making  Seven different sources of bias .pdf** — 0.0139 (rrf) — _# i cdecision are trained and try to look at every Xray, their experience tells them that there _
47. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0139 (rrf) — _# RE FE R ENCES summing up of all 34 chapters? Too ambitious. A prophetic “Whither evolutio nary_
48. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0139 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
49. **Lyell Automation bias and verification complexity.pdf** — 0.0138 (rrf) — _# ACKNOWLEDGMENTS 10 Comparing studies was difficult. nificance for the presence of automation b_
50. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0138 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative, mechanism-first review of participant reasoning during a feedwater heater trend. Only affirmative transcript evidence of bias-specific mechanisms was classified as identified. Later-learned maintenance findings were excluded as hindsight."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "plan continuation bias",
      "alternative_labels": ["get-there-itis", "plan continuation error"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Final ascension step decision to proceed despite unresolved 1B heater infrared/trend anomalies",
      "supporting_interview_quote": "I did think about it. It came down to whether an unconfirmed field reading, with no limit approached, was enough reason to interrupt a scheduled step. I decided documenting it and handing it off was the more defensible path, but I won't pretend that was the only reasonable call.",
      "plausible_mechanism": "Continued commitment to the planned power escalation and dispatch window despite accumulating ambiguous anomaly cues could reflect plan continuation bias.",
      "why_not_identified": "The participant explicitly considered holding, said schedule was not the deciding factor, cited absence of a procedural or Tech Spec hold basis, and documented an open item with maintenance follow-up. These actions are better explained by ordinary uncertainty and structural constraints than by a bias-specific mechanism."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "anchoring bias",
      "alternative_labels": ["anchoring and adjustment"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial classification of 1B heater outlet temperature drift as probable recurrence of prior calibration deviation",
      "supporting_interview_quote": "My first thought was that it looked like the calibration deviation we'd had on that sensor last cycle — but I didn't want to just assume that, because I didn't actually remember the details of that event well enough to say it matched.",
      "plausible_mechanism": "The initial calibration-deviation hypothesis could function as an anchor for subsequent comparison and causal attribution, especially when partial similarities were later logged as probable recurrence.",
      "why_not_identified": "The participant avoided assumption, retrieved an actual closed-out fault report, characterized the match as partial, and logged the recurrence as unconfirmed. The transcript lacks affirmative evidence of insufficient adjustment from the anchor rather than a reasonable hypothesis check."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "Retrieved corpus passages were sparse and not directly specific to this operational context; no identified occurrence required corpus-supported classification.",
    "Internal mental states are inferred only from the participant's retrospective verbal report.",
    "Later maintenance evidence of early-stage fouling was disclosed but excluded from bias classification to avoid hindsight-based inference."
  ]
}

