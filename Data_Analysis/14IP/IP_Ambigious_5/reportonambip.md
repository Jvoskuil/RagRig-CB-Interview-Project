# RAG Benchmark — 2026-09-14

## Gemini Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is a cognitive task analysis interview — I want to understand how you actually worked through a specific production problem, including what you knew at each point and why you chose what you did. There are no right answers I'm grading you against. Okay to start? Participant: Sure, no problem. I've got a decent example — the Line 3 flash issue before our Meridian shipment a few weeks back. Interviewer: Great, let's use that. Can you describe the overall situation and what you were trying to accomplish? Participant: We had a 72-hour window to ship a Meridian order off Line 3 — interior clips, tight tolerances. Partway through a night shift, scrap jumped from about 1.8% to 6.4%, mostly flash, some short shots. My goal was to get us back under 2% without missing the ship date and without a full shutdown, since that needs VP sign-off and we didn't have time for that process anyway. Interviewer: What were the first signs something was wrong? Participant: Quality flagged the scrap numbers, and the SPC chart showed cavity pressure drifting starting mid-shift. That drift range is one of those things that's ambiguous on its own — we've seen similar magnitudes tied to humidity issues before, but also to early tooling wear. So it didn't point cleanly in one direction. Interviewer: Did anything from past experience come to mind? Participant: We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying. But we'd since put in a new dehumidifier, so I honestly wasn't sure how comparable that case even was anymore. It could easily have been a red herring. Interviewer: So what did you do with that uncertainty? Participant: I didn't want to bet the sequencing on either guess, so I had two techs pull humidity logs and tooling wear data at the same time — they'd take roughly the same amount of time either way, so there wasn't a good reason to prioritize one over the other. Interviewer: What came back? Participant: Humidity logs were normal. Tooling data showed moderate wear had built up. So the wear side turned out to be the real thread, but I couldn't have known that going in — it really could have gone either way based on what we had. Interviewer: Let's reconstruct the next couple of days. What happened once wear was confirmed? Participant: That's decision point two. Wear was real, but the reading was right on the line — borderline between our threshold for a simple hold-pressure adjustment and the threshold for a full insert swap. My tooling lead and one of the shift supervisors actually disagreed about which side of that line we were on. Interviewer: How did you resolve that? Participant: We had a press-down window open right then, shared with two other product runs, and it wouldn't come around again for five days. A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap. Interviewer: Did that resolve things? Participant: Partially. Scrap improved but didn't fully get back to baseline. Could mean the wear diagnosis was right but incomplete, or that there's a second factor we haven't isolated. I genuinely don't know which. Interviewer: Take me to the third point — the call with the sister plant. Participant: Right, this was day two, when my quality engineer was out sick, so I had less support than usual. I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match. Interviewer: What did you know about how well it would apply to your line specifically? Participant: My engineer had partially validated it against our resin lot before going out sick, but hadn't finished testing it against our specific cavity geometry. Corporate quality said results across the network looked promising but not conclusive yet. Interviewer: So what did you decide? Participant: I adopted it based on the partial validation we already had. I'll be honest, it could reasonably have gone the other way — waiting for full geometry testing, or rolling out a more conservative version first. I weighed the incomplete testing against the shipment clock and made a call I can defend, but I wouldn't say it was obviously the right one. Interviewer: What happened after? Participant: Short-term, flash defects dropped. Then two shifts later we got a new warping issue on some parts, cause not yet clear. Might be related to the cooling change, might not. Interviewer: Last decision point — the rollout call. Participant: Right. By the final stretch, our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability. Corporate quality asked if we should roll the fix to Lines 4 and 6. Interviewer: What made that decision hard? Participant: Lines 4 and 6 have different tooling age profiles than Line 3, so I couldn't just assume the fix would transfer cleanly either way. Given the mixed trend and those differences, I didn't think a full rollout to both lines was justified yet, but sitting on it entirely wasn't really an option with the deadline bearing down. Interviewer: So what did you approve? Participant: A limited pilot on one line with extra monitoring, rather than pushing it to both. I said as much to corporate — that the data didn't support going all-in yet, but doing nothing wasn't realistic either. Interviewer: What came of the pilot? Participant: Initial improvement, then a new tooling alarm showed up on that line that we hadn't seen before. A fuller week-long review later suggested the underlying wear issue was only partly addressed. Interviewer: What information would have made these calls easier? Participant: Faster wear measurements at decision two, and full geometry validation before decision three. Those were the two spots where I felt like I was deciding on incomplete information out of necessity, not preference. Interviewer: If the last shift's numbers had come in worse instead of better, would decision four have gone differently? Participant: Possibly less generous — maybe I'd have held off on even the pilot. But given how mixed the broader trend already was, I think I was already treating that last shift as one data point, not the whole answer. Interviewer: Anything you'd do differently if this happened again? Participant: Build in a standing arrangement for a second wear reading that doesn't cost us the press-down window, and push corporate for full geometry validation timelines before protocols spread across plants. Otherwise, honestly, most of these calls I'd probably make the same way again given the same constraints. Interviewer: This has been really helpful, thank you. Participant: Anytime.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.55s · gen 48.36s · total 52.0s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0263 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0263 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0248 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0235 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0226 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0210 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0210 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0205 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
10. **Lyell Automation bias and verification complexity.pdf** — 0.0190 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0180 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
15. **Hallihan_etal_DTM_12.pdf** — 0.0174 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
16. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0174 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
17. **Hallihan_etal_DTM_12.pdf** — 0.0174 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0173 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
19. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0171 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
22. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0163 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0159 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
28. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0157 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
29. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0157 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
30. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
32. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0153 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
37. **Hallihan_etal_DTM_12.pdf** — 0.0152 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0151 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
39. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
41. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0149 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
42. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0148 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
47. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0143 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
48. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0141 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
49. **ijcma-08-2012-0064.pdf** — 0.0141 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
50. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0139 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative mechanism-first review of a single cognitive task analysis interview. The participant described several decision points under uncertainty and time pressure, but no transcript evidence reached the threshold for an affirmative cognitive bias occurrence. Candidate bias patterns were retained where mechanisms were plausible but insufficiently evidenced or actively counterbalanced by the participant."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Recency effect",
      "alternative_labels": ["Recency bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision four: rollout to Lines 4 and 6",
      "supporting_interview_quote": "Most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability.",
      "plausible_mechanism": "The most recent favorable shift data may be salient and could disproportionately influence the rollout decision.",
      "why_not_identified": "The participant explicitly integrated the broader four-day trend and stated that the last shift was treated as one data point rather than the whole answer. There is no affirmative evidence that the recent data point distorted the reasoning or decision."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Bandwagon effect",
      "alternative_labels": ["Social proof", "Conformity"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision three: adoption of cooling-time reduction protocol",
      "supporting_interview_quote": "I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. ... I adopted it based on the partial validation we already had.",
      "plausible_mechanism": "Adoption may have been influenced by the fact that multiple sister plants had already adopted the protocol.",
      "why_not_identified": "The participant noted material differences in resin and cavity geometry, described partial local validation, and weighed incomplete testing against the shipment clock. The transcript presents this as a reasoned decision under constraint rather than a conformity-driven distortion."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Anchoring bias",
      "alternative_labels": ["Anchoring-and-adjustment"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial diagnosis: humidity versus tooling wear",
      "supporting_interview_quote": "We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying.",
      "plausible_mechanism": "The prior humidity episode could serve as an initial anchor in diagnostic reasoning.",
      "why_not_identified": "The participant explicitly described the prior case as possibly a red herring and collected humidity and tooling wear data in parallel. This demonstrates active adjustment away from any initial anchor rather than a biasing distortion."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "Only one interview was analyzed and no corroborating process data were available.",
    "Retrieved corpus passages did not cover all potential bias mechanisms; however, no affirmative distortion met the identification threshold.",
    "Self-reported cognitive task analysis may be subject to memory and self-presentation effects, but the transcript itself did not provide affirmative evidence of a specific cognitive bias occurrence."
  ]
}

## Sonar Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is a cognitive task analysis interview — I want to understand how you actually worked through a specific production problem, including what you knew at each point and why you chose what you did. There are no right answers I'm grading you against. Okay to start? Participant: Sure, no problem. I've got a decent example — the Line 3 flash issue before our Meridian shipment a few weeks back. Interviewer: Great, let's use that. Can you describe the overall situation and what you were trying to accomplish? Participant: We had a 72-hour window to ship a Meridian order off Line 3 — interior clips, tight tolerances. Partway through a night shift, scrap jumped from about 1.8% to 6.4%, mostly flash, some short shots. My goal was to get us back under 2% without missing the ship date and without a full shutdown, since that needs VP sign-off and we didn't have time for that process anyway. Interviewer: What were the first signs something was wrong? Participant: Quality flagged the scrap numbers, and the SPC chart showed cavity pressure drifting starting mid-shift. That drift range is one of those things that's ambiguous on its own — we've seen similar magnitudes tied to humidity issues before, but also to early tooling wear. So it didn't point cleanly in one direction. Interviewer: Did anything from past experience come to mind? Participant: We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying. But we'd since put in a new dehumidifier, so I honestly wasn't sure how comparable that case even was anymore. It could easily have been a red herring. Interviewer: So what did you do with that uncertainty? Participant: I didn't want to bet the sequencing on either guess, so I had two techs pull humidity logs and tooling wear data at the same time — they'd take roughly the same amount of time either way, so there wasn't a good reason to prioritize one over the other. Interviewer: What came back? Participant: Humidity logs were normal. Tooling data showed moderate wear had built up. So the wear side turned out to be the real thread, but I couldn't have known that going in — it really could have gone either way based on what we had. Interviewer: Let's reconstruct the next couple of days. What happened once wear was confirmed? Participant: That's decision point two. Wear was real, but the reading was right on the line — borderline between our threshold for a simple hold-pressure adjustment and the threshold for a full insert swap. My tooling lead and one of the shift supervisors actually disagreed about which side of that line we were on. Interviewer: How did you resolve that? Participant: We had a press-down window open right then, shared with two other product runs, and it wouldn't come around again for five days. A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap. Interviewer: Did that resolve things? Participant: Partially. Scrap improved but didn't fully get back to baseline. Could mean the wear diagnosis was right but incomplete, or that there's a second factor we haven't isolated. I genuinely don't know which. Interviewer: Take me to the third point — the call with the sister plant. Participant: Right, this was day two, when my quality engineer was out sick, so I had less support than usual. I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match. Interviewer: What did you know about how well it would apply to your line specifically? Participant: My engineer had partially validated it against our resin lot before going out sick, but hadn't finished testing it against our specific cavity geometry. Corporate quality said results across the network looked promising but not conclusive yet. Interviewer: So what did you decide? Participant: I adopted it based on the partial validation we already had. I'll be honest, it could reasonably have gone the other way — waiting for full geometry testing, or rolling out a more conservative version first. I weighed the incomplete testing against the shipment clock and made a call I can defend, but I wouldn't say it was obviously the right one. Interviewer: What happened after? Participant: Short-term, flash defects dropped. Then two shifts later we got a new warping issue on some parts, cause not yet clear. Might be related to the cooling change, might not. Interviewer: Last decision point — the rollout call. Participant: Right. By the final stretch, our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability. Corporate quality asked if we should roll the fix to Lines 4 and 6. Interviewer: What made that decision hard? Participant: Lines 4 and 6 have different tooling age profiles than Line 3, so I couldn't just assume the fix would transfer cleanly either way. Given the mixed trend and those differences, I didn't think a full rollout to both lines was justified yet, but sitting on it entirely wasn't really an option with the deadline bearing down. Interviewer: So what did you approve? Participant: A limited pilot on one line with extra monitoring, rather than pushing it to both. I said as much to corporate — that the data didn't support going all-in yet, but doing nothing wasn't realistic either. Interviewer: What came of the pilot? Participant: Initial improvement, then a new tooling alarm showed up on that line that we hadn't seen before. A fuller week-long review later suggested the underlying wear issue was only partly addressed. Interviewer: What information would have made these calls easier? Participant: Faster wear measurements at decision two, and full geometry validation before decision three. Those were the two spots where I felt like I was deciding on incomplete information out of necessity, not preference. Interviewer: If the last shift's numbers had come in worse instead of better, would decision four have gone differently? Participant: Possibly less generous — maybe I'd have held off on even the pilot. But given how mixed the broader trend already was, I think I was already treating that last shift as one data point, not the whole answer. Interviewer: Anything you'd do differently if this happened again? Participant: Build in a standing arrangement for a second wear reading that doesn't cost us the press-down window, and push corporate for full geometry validation timelines before protocols spread across plants. Otherwise, honestly, most of these calls I'd probably make the same way again given the same constraints. Interviewer: This has been really helpful, thank you. Participant: Anytime.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.50s · gen 55.20s · total 58.7s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0263 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0263 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0248 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0235 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0226 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0210 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0210 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0205 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
10. **Lyell Automation bias and verification complexity.pdf** — 0.0190 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0180 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
15. **Hallihan_etal_DTM_12.pdf** — 0.0174 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
16. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0174 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
17. **Hallihan_etal_DTM_12.pdf** — 0.0174 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0173 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
19. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0171 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
22. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0163 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0159 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
28. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0157 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
29. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0157 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
30. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
32. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0153 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
37. **Hallihan_etal_DTM_12.pdf** — 0.0152 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0151 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
39. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
41. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0149 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
42. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0148 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
47. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0143 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
48. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0141 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
49. **ijcma-08-2012-0064.pdf** — 0.0141 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
50. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0139 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "The transcript was analyzed for bias-specific mechanisms in the participant's production decisions under uncertainty, time pressure, and incomplete information. Retrieved corpus passages on anchoring, AI overreliance, confirmation bias, aerospace cognitive bias, and usability-testing biases were reviewed; none supported an identified occurrence because the participant's reasoning generally showed active uncertainty management, parallel evidence search, and explicit qualification rather than a distinct cognitive bias mechanism."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Social proof / Bandwagon effect",
      "alternative_labels": ["Bandwagon effect", "Social proof"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Adoption of sister plants' cooling-time reduction protocol",
      "supporting_interview_quote": "I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match.",
      "plausible_mechanism": "A practice may gain subjective plausibility because multiple peer plants have adopted it, even when the local fit is uncertain.",
      "why_not_identified": "The participant did not cite the peer adoption as the reason for adoption; he pointed to partial in-house validation and shipment-time pressure, and acknowledged the peer cases were not clean matches. No quote shows that the number of adopters itself changed his judgment."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Recency effect",
      "alternative_labels": ["Recent evidence overweighting"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Rollout decision for Lines 4 and 6",
      "supporting_interview_quote": "By the final stretch, our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability.",
      "plausible_mechanism": "Recent performance data can be overweighted relative to a longer and more variable trend when deciding whether to pilot a fix.",
      "why_not_identified": "The participant explicitly contrasted the recent shift with the messier four-day trend and rejected a full rollout, describing the last shift as 'one data point, not the whole answer.' He also said the pilot decision was constrained by the deadline. No statement indicates disproportionate reliance on the recent shift."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Action bias",
      "alternative_labels": ["Intervention bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Borderline wear reading and insert-swap decision",
      "supporting_interview_quote": "A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap.",
      "plausible_mechanism": "Under ambiguous diagnostic information, a person may favor an active or invasive intervention over waiting for more measurement because action reduces immediate uncertainty or feels more productive.",
      "why_not_identified": "The participant provided an explicit scheduling rationale for acting without remeasurement: the press-down window would close for five days and the fix would be much harder to schedule later. There is no evidence he acted merely to do something; the choice is readily explained by time and resource constraints."
    },
    {
      "candidate_id": "cand_004",
      "classification_status": "candidate",
      "proposed_bias_label": "Availability heuristic",
      "alternative_labels": ["Availability bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Initial interpretation of similar-looking defect pattern",
      "supporting_interview_quote": "We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying. But we'd since put in a new dehumidifier, so I honestly wasn't sure how comparable that case even was anymore. It could easily have been a red herring.",
      "plausible_mechanism": "A previous similar defect case could come to mind easily and shape hypothesis generation, even though conditions had changed.",
      "why_not_identified": "The participant treated the past case as potentially non-comparable, explicitly allowed that it could be a red herring, and collected humidity and tooling data in parallel rather than prioritizing the mentally available hypothesis."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "Single interview; no independent ground truth for optimal decisions.",
    "The retrospective account may be shaped by self-presentation or memory effects, but these were not classified without affirmative bias-specific evidence.",
    "Retrieved corpus support was limited and did not provide suitable definitions for all plausible candidate labels; candidate labels rely partly on general cognitive-science terminology.",
    "The absence of identified biases is not evidence that no bias occurred; it reflects a conservative mechanism-first threshold."
  ]
}

## Sonnet Prompt 8192

**Q1:** Interviewer: Thanks for sitting down with me. This is a cognitive task analysis interview — I want to understand how you actually worked through a specific production problem, including what you knew at each point and why you chose what you did. There are no right answers I'm grading you against. Okay to start? Participant: Sure, no problem. I've got a decent example — the Line 3 flash issue before our Meridian shipment a few weeks back. Interviewer: Great, let's use that. Can you describe the overall situation and what you were trying to accomplish? Participant: We had a 72-hour window to ship a Meridian order off Line 3 — interior clips, tight tolerances. Partway through a night shift, scrap jumped from about 1.8% to 6.4%, mostly flash, some short shots. My goal was to get us back under 2% without missing the ship date and without a full shutdown, since that needs VP sign-off and we didn't have time for that process anyway. Interviewer: What were the first signs something was wrong? Participant: Quality flagged the scrap numbers, and the SPC chart showed cavity pressure drifting starting mid-shift. That drift range is one of those things that's ambiguous on its own — we've seen similar magnitudes tied to humidity issues before, but also to early tooling wear. So it didn't point cleanly in one direction. Interviewer: Did anything from past experience come to mind? Participant: We had a similar-looking defect pattern about six months back that turned out to be humidity affecting resin drying. But we'd since put in a new dehumidifier, so I honestly wasn't sure how comparable that case even was anymore. It could easily have been a red herring. Interviewer: So what did you do with that uncertainty? Participant: I didn't want to bet the sequencing on either guess, so I had two techs pull humidity logs and tooling wear data at the same time — they'd take roughly the same amount of time either way, so there wasn't a good reason to prioritize one over the other. Interviewer: What came back? Participant: Humidity logs were normal. Tooling data showed moderate wear had built up. So the wear side turned out to be the real thread, but I couldn't have known that going in — it really could have gone either way based on what we had. Interviewer: Let's reconstruct the next couple of days. What happened once wear was confirmed? Participant: That's decision point two. Wear was real, but the reading was right on the line — borderline between our threshold for a simple hold-pressure adjustment and the threshold for a full insert swap. My tooling lead and one of the shift supervisors actually disagreed about which side of that line we were on. Interviewer: How did you resolve that? Participant: We had a press-down window open right then, shared with two other product runs, and it wouldn't come around again for five days. A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap. Interviewer: Did that resolve things? Participant: Partially. Scrap improved but didn't fully get back to baseline. Could mean the wear diagnosis was right but incomplete, or that there's a second factor we haven't isolated. I genuinely don't know which. Interviewer: Take me to the third point — the call with the sister plant. Participant: Right, this was day two, when my quality engineer was out sick, so I had less support than usual. I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems. But two of those three run a different resin lot and slightly different cavity geometry than we do, so it wasn't a clean match. Interviewer: What did you know about how well it would apply to your line specifically? Participant: My engineer had partially validated it against our resin lot before going out sick, but hadn't finished testing it against our specific cavity geometry. Corporate quality said results across the network looked promising but not conclusive yet. Interviewer: So what did you decide? Participant: I adopted it based on the partial validation we already had. I'll be honest, it could reasonably have gone the other way — waiting for full geometry testing, or rolling out a more conservative version first. I weighed the incomplete testing against the shipment clock and made a call I can defend, but I wouldn't say it was obviously the right one. Interviewer: What happened after? Participant: Short-term, flash defects dropped. Then two shifts later we got a new warping issue on some parts, cause not yet clear. Might be related to the cooling change, might not. Interviewer: Last decision point — the rollout call. Participant: Right. By the final stretch, our most recent shift showed scrap at 1.5%, best in four days. But the broader four-day trend, counting the warping issue, was messier — more like 2.9% average with real variability. Corporate quality asked if we should roll the fix to Lines 4 and 6. Interviewer: What made that decision hard? Participant: Lines 4 and 6 have different tooling age profiles than Line 3, so I couldn't just assume the fix would transfer cleanly either way. Given the mixed trend and those differences, I didn't think a full rollout to both lines was justified yet, but sitting on it entirely wasn't really an option with the deadline bearing down. Interviewer: So what did you approve? Participant: A limited pilot on one line with extra monitoring, rather than pushing it to both. I said as much to corporate — that the data didn't support going all-in yet, but doing nothing wasn't realistic either. Interviewer: What came of the pilot? Participant: Initial improvement, then a new tooling alarm showed up on that line that we hadn't seen before. A fuller week-long review later suggested the underlying wear issue was only partly addressed. Interviewer: What information would have made these calls easier? Participant: Faster wear measurements at decision two, and full geometry validation before decision three. Those were the two spots where I felt like I was deciding on incomplete information out of necessity, not preference. Interviewer: If the last shift's numbers had come in worse instead of better, would decision four have gone differently? Participant: Possibly less generous — maybe I'd have held off on even the pilot. But given how mixed the broader trend already was, I think I was already treating that last shift as one data point, not the whole answer. Interviewer: Anything you'd do differently if this happened again? Participant: Build in a standing arrangement for a second wear reading that doesn't cost us the press-down window, and push corporate for full geometry validation timelines before protocols spread across plants. Otherwise, honestly, most of these calls I'd probably make the same way again given the same constraints. Interviewer: This has been really helpful, thank you. Participant: Anytime.

_ranker=rrf · t=0.04 · k=50 → 50 in context · 8192 ctx · emb 1.51s · gen 58.79s · total 62.3s_

**Retrieved** (ranked by store ranker):
1. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0263 (rrf) — _# 4 Anchoring bias Figure 2. Results of experiment 1. time allocations in experiment 1. answer u_
2. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0263 (rrf) — _# 188 task, the top performer of each batch was rewarded with a bonus of $3. Out of 260 particip_
3. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0248 (rrf) — _# 5. Discussion conditions (14 out of 25) finding, t he researcher disproportionately if a large_
4. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0235 (rrf) — _## Types of Cognitive Biases with?” vs. “What did you think of the material the device was made _
5. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0226 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration 400 and management_
6. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0215 (rrf) — _# 6. Conclusion fter a gap in the research was discovered aimed to establish what the most commo_
7. **cook-smallman-2008-human-factors-of-the-confirmation-bias-in-intelligence-analysis-decision-support-from-graphical.pdf** — 0.0210 (rrf) — _# Page 8 developed by Wason (1960, 1968). Rule certaintylaboratively participating and no real a_
8. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0210 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration - 402 discounting _
9. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0205 (rrf) — _# 5. Discussion This study evolved over two years a concerning the concept of cognitive bias and_
10. **Lyell Automation bias and verification complexity.pdf** — 0.0190 (rrf) — _## INTRODUCTION 51 which required subjects to view that varied between high and low accuracy. un_
11. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0182 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION | was deemed as not helpful. So, if a participant said it_
12. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0181 (rrf) — _## Types of Cognitive Biases example, especially in focus groups, if some people respond to a qu_
13. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0180 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration The underlying det_
14. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0179 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration during a test sess_
15. **Hallihan_etal_DTM_12.pdf** — 0.0174 (rrf) — _disconfirming and 3 confirming 5.2.4. Results . The data collected from Problem 2 are seen in Ta_
16. **Mitigating cognitive bias with clinical decision support systems  an experimental study.pdf** — 0.0174 (rrf) — _# support Student 52 female (69.3 %) 75 (72.8 %) 25.53 (SD = 5.02) 25 (range = 19–52) 4.57 (SD =_
17. **Hallihan_etal_DTM_12.pdf** — 0.0174 (rrf) — _5.1.3. Discussion . These results closely replicate the findings from earlier experiments on con_
18. **INCOSE International Symp - 2020 - McDermott - Addressing Cognitive Bias in Systems Engineering Teams.pdf** — 0.0173 (rrf) — _# , Leadership, At the start of this week’s meeting, before the saf his lack of involvement to t_
19. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0171 (rrf) — _# 6 Discussion the task progresses, based on their interaction with the AI. Dynamic Markov model_
20. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0171 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration conducting real AT_
21. **natesan-et-al-2016-cognitive-bias-in-usability-testing.pdf** — 0.0170 (rrf) — _## Types of Cognitive Biases Moderator Bias Experimenter Effect. The tendency for individuals to_
22. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0166 (rrf) — _# 4.2 Answering our RQs 4.2.1 RQ1: What are the causal or mediator factors of automation bias? A_
23. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0163 (rrf) — _# Experiment 3 e postexperimental questions in Experiment 3 were the same as in Experiment 2, bu_
24. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0161 (rrf) — _# 5. Discussion onset of plan continuation bias bias tends to occur towards the end of evidence _
25. **Hallihan_etal_DTM_12.pdf** — 0.0161 (rrf) — _5.2.3. Measurement . Participants in the control group were instructed to use blank sheets of pa_
26. **Greavu-Şerban et al. (2025) Exploring Heuristics and Biases in Cybersecurity_ A Factor Analysis of Social Engineering Vulnerabilities.pdf** — 0.0159 (rrf) — _# Appendix A. Survey Questionnaire • google.com • googl е .com • All of the above • None of the _
27. **Romeo & Conti (2025) Exploring automation bias in human AI collaboration_a review and implications for explainable AI.pdf** — 0.0158 (rrf) — _## 1Introduction 1.2 Dening automation bias: a cognitive limitation in human–automation interact_
28. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0157 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study undermining confirmation _
29. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0157 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization 5.4 Limitations 154 b_
30. **Hallihan_etal_DTM_12.pdf** — 0.0156 (rrf) — _research on design fixation (Hallihan & Shu, 2011) believe confirmation bias could prevent desig_
31. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0154 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration A similar result e_
32. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0153 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization between quantities se_
33. **Clinical-decision-making--Cognitive-biases-and-heu_2025_The-American-Journal.pdf** — 0.0153 (rrf) — _## Uwe Dulleck, PhD learnthroughpractice.AsDanielKahnemanarguesinhisbook Fast, and Slow , expert_
34. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0153 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration from relevant cock_
35. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0152 (rrf) — _## a nd Prey | space of possible social goals is large and needs to be pared down before you de-_
36. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0152 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration mation bias (Mosie_
37. **Hallihan_etal_DTM_12.pdf** — 0.0152 (rrf) — _overconfidence in design is associated with no judgment arising from a reliance on confirmation _
38. **Dimara et al. (2018). A Task-Based Taxonomy of Cognitive biases for information Visualization.pdf** — 0.0151 (rrf) — _## A Task-Based Taxonomy of Cognitive Biases for Information Visualization Method 3.b was used w_
39. **Cognitive_Biases_in_Software_Engineering_A_Systematic_Mapping_Study.pdf** — 0.0150 (rrf) — _# Cognitive Biases in Software Engineering: A Systematic Mapping Study Thinkaloud protocol analy_
40. **parasuraman-manzey-2010-complacency-and-bias-in-human-use-of-automation-an-attentional-integration.pdf** — 0.0149 (rrf) — _# Complacency and Bias in Human Use of Automation: An Attentional Integration automation failure_
41. **Vicente & Matute (2023) Humans inherit artificial intelligence biases.pdf** — 0.0149 (rrf) — _# Experiment 1 Method. the methodology reported in this article and the experiments were conduct_
42. **Rastogi et al. (2022) Deciding fast and slow_The role of cognitive biases in AI-assisted decision-making.pdf** — 0.0148 (rrf) — _# 4 Anchoring bias Task and AI model. to predict whether a student would pass or fail a class, b_
43. **The_Handbook_of_Evolutionary_Psychology.pdf** — 0.0147 (rrf) — _## Afterword 978 A FTERWORD short comi shoddy, but they are of a type that is in principle remed_
44. **Cognitive bias in the cockpit A deadly false sense of normality Sam OConnor (1).pdf** — 0.0146 (rrf) — _# 2. Literature Review changing environment may result in a loss of SA which can impact the deci_
45. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0145 (rrf) — _# f Space Flight ( \| ) = , where (2) Figure 2. Attributing Results to a Process set of inputs (_
46. **Cognitive_bias_in_the_verification_and_validation_of_space_flight_systems.pdf** — 0.0144 (rrf) — _# f Space Flight quickly \[14\]. Lord et al found that participants we critical of evidence that_
47. **Cognitive_Biases_in_Technical_Communication.pdf** — 0.0143 (rrf) — _# Cognitive Biases in Technical Communication The Sun k Cost Fallacy refers to t decisions that _
48. **Bucinca et al. (2021) To Trust or to Think_Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making.pdf** — 0.0141 (rrf) — _# 188 | the ingredient to replace and an ingredient to replace it with, each from a list that co_
49. **ijcma-08-2012-0064.pdf** — 0.0141 (rrf) — _# 382 involved. In sum, cognitive misperceptions can highly bias the human behavior when making _
50. **Azzopardi (2021). Cognitive Biases in Search.pdf** — 0.0139 (rrf) — _# 4 DISCUSSION AND CRITICAL REFLECTION rather than maximisers ( HM9 , first acceptable result, r_

{
  "analysis_metadata": {
    "task": "cognitive_bias_analysis",
    "interview_speakers_detected": ["Interviewer", "Participant"],
    "retrieved_corpus_support_used": false,
    "analysis_scope_note": "Conservative mechanism-first review of the CTA transcript. Findings require affirmative evidence of a bias-specific mechanism; structural constraints such as deadline pressure, incomplete information, and scheduling tradeoffs were not treated as bias unless a distinct cognitive mechanism was separately evidenced."
  },
  "identified_bias_summary": [],
  "identified_occurrences": [],
  "candidate_biases": [
    {
      "candidate_id": "cand_001",
      "classification_status": "candidate",
      "proposed_bias_label": "Recency effect",
      "alternative_labels": ["Recency bias"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision four — pilot rollout to Lines 4 and 6",
      "supporting_interview_quote": "Possibly less generous — maybe I'd have held off on even the pilot. But given how mixed the broader trend already was, I think I was already treating that last shift as one data point, not the whole answer.",
      "plausible_mechanism": "The final shift's improved scrap rate (1.5%) may have made a limited pilot seem more attractive than the messier four-day average (2.9%) alone would support.",
      "why_not_identified": "The participant explicitly described treating the last shift as one data point, and the actual decision was a limited single-line pilot rather than full rollout; this is insufficient for affirmative identification of recency-based overweighting."
    },
    {
      "candidate_id": "cand_002",
      "classification_status": "candidate",
      "proposed_bias_label": "Bandwagon effect",
      "alternative_labels": ["Social proof", "Informational social influence"],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision three — adoption of cooling-time reduction protocol",
      "supporting_interview_quote": "I learned three of our four sister plants had adopted a cooling-time reduction protocol for similar flash problems.",
      "plausible_mechanism": "Adoption by three of four sister plants may have served as social or informational evidence in favor of the protocol despite incomplete validation for the local line.",
      "why_not_identified": "The participant acknowledged differences in resin lot and cavity geometry and grounded the decision in partial validation and shipment clock rather than showing disproportionate reliance on sister-plant adoption."
    },
    {
      "candidate_id": "cand_003",
      "classification_status": "candidate",
      "proposed_bias_label": "Action bias",
      "alternative_labels": [],
      "taxonomy_status": "established_label",
      "speaker_or_attributed_person": "Participant",
      "possible_decision_episode_label": "Decision two — insert swap under a closing press-down window",
      "supporting_interview_quote": "We had a press-down window open right then, shared with two other product runs, and it wouldn't come around again for five days. A second measurement might have settled the disagreement, but not fast enough to still make the window. So it came down to: closing window, ambiguous reading, and a fix that would be much harder to schedule later. I went with the insert swap.",
      "plausible_mechanism": "The combination of ambiguity, time pressure, and a closing scheduling window may have favored taking an immediate corrective action over gathering additional disambiguating information.",
      "why_not_identified": "The transcript offers explicit operational scheduling costs and a reasoned tradeoff as the basis for the choice, so time pressure and incomplete measurement alone do not provide affirmative evidence of a bias-specific preference for action over inaction."
    }
  ],
  "no_supported_biases_found": true,
  "limitations": [
    "Retrieved corpus passages did not directly address the specific manufacturing decision context; this analysis relies on transcript evidence and general bias taxonomies.",
    "The interview is a retrospective self-report, so some reasoning processes may be reconstructed rather than directly observed, and motivational or organizational factors may be underreported.",
    "Candidate biases are listed only where a plausible mechanism was present but lacked the affirmative evidence required for identification."
  ]
}

